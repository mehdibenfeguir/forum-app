from rest_framework import serializers
from ForumApp.models import Questions,Answers,Tags,CommentQuestions,CommentAnswers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions 
        fields=('QuestionId','description')
class CommentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentQuestions 
        fields=('CommentQuestionId','description','question')

class CommentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentAnswers 
        fields=('CommentAnswerId','description','answer')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answers 
        fields=('AnswerId','description','question')
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags 
        fields=('TagId','description','question')
