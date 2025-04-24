import json

from main.models import Card, IFile
from main.serializers import CardSerializer, UploadedFileSerializer
from main.tools import call_ai, extract_text_from_file

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class ReadCardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(detail=False, methods=['post'])
    def clear(self, request):
        count = Card.objects.count()
        Card.objects.all().delete()
        IFile.objects.all().delete()
        return Response(
            {"message": f"{count} карточек было удалено."},
            status=status.HTTP_200_OK
        )


FIXED_PROMPT = """
Составь 10 тестовых вопросов по следующему тексту. У каждого вопроса должно быть 4 варианта ответа, один из которых правильный. Ответ верни в формате JSON:

[
  {
    "question": "Текст вопроса?",
    "right_answer": "Правильный ответ",
    "answer1": "Неверный ответ 1",
    "answer2": "Неверный ответ 2",
    "answer3": "Неверный ответ 3"
  },
  ...
]

Вот текст:
"""


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = IFile.objects.all()
    serializer_class = UploadedFileSerializer

    def perform_create(self, serializer):
        uploaded_file = serializer.save()
        file_path = uploaded_file.value.path
        text = extract_text_from_file(file_path)

        try:
            answer = call_ai(FIXED_PROMPT, text)
            cards = json.loads(answer)
            for item in cards:
                Card.objects.create(
                    question=item["question"],
                    right_answer=item["right_answer"],
                    answer1=item["answer1"],
                    answer2=item["answer2"],
                    answer3=item["answer3"]
                )
        except Exception as e:
            print("Ошибка при обработке файла:", e)
