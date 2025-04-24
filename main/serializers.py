from rest_framework import serializers

from main.models import Card, IFile


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'question', 'right_answer',
                  'answer1', 'answer2', 'answer3')


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IFile
        fields = ('value',)
