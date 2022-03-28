from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from ForumApp.models import Questions,Answers,Tags,CommentQuestions,CommentAnswers
from ForumApp.serializers import QuestionSerializer,CommentQuestionSerializer,CommentAnswerSerializer,AnswerSerializer,TagSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def commentQuestionApi(request,id=0):
    if request.method=='GET':
        commentQuestions = CommentQuestions.objects.all()
        commentQuestions_serializer=CommentQuestionSerializer(commentQuestions,many=True)
        return JsonResponse(commentQuestions_serializer.data,safe=False)
    elif request.method=='POST':
        commentQuestion_data=JSONParser().parse(request)
        commentQuestions_serializer=CommentQuestionSerializer(data=commentQuestion_data)
        if commentQuestions_serializer.is_valid():
            commentQuestions_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        commentQuestion_data=JSONParser().parse(request)
        commentQuestion=CommentQuestions.objects.get(CommentQuestionId=commentQuestion_data['CommentQuestionId'])
        commentQuestions_serializer=CommentQuestionSerializer(commentQuestion,data=commentQuestion_data)
        if commentQuestions_serializer.is_valid():
            commentQuestions_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        commentQuestion=CommentQuestions.objects.get(CommentQuestionId=id)
        commentQuestion.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def commentAnswerApi(request,id=0):
    if request.method=='GET':
        commentAnswers = CommentAnswers.objects.all()
        commentAnswers_serializer=CommentAnswerSerializer(commentAnswers,many=True)
        return JsonResponse(commentAnswers_serializer.data,safe=False)
    elif request.method=='POST':
        commentAnswer_data=JSONParser().parse(request)
        commentAnswers_serializer=CommentAnswerSerializer(data=commentAnswer_data)
        if commentAnswers_serializer.is_valid():
            commentAnswers_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        commentAnswer_data=JSONParser().parse(request)
        commentAnswer=CommentAnswers.objects.get(CommentAnswerId=commentAnswer_data['CommentAnswerId'])
        commentAnswers_serializer=CommentAnswerSerializer(commentAnswer,data=commentAnswer_data)
        if commentAnswers_serializer.is_valid():
            commentAnswers_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        commentAnswer=CommentAnswers.objects.get(CommentAnswerId=id)
        commentAnswer.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def questionApi(request,id=0):
    if request.method=='GET':
        questions = Questions.objects.all()
        questions_serializer=QuestionSerializer(questions,many=True)
        return JsonResponse(questions_serializer.data,safe=False)
    elif request.method=='POST':
        question_data=JSONParser().parse(request)
        questions_serializer=QuestionSerializer(data=question_data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        question_data=JSONParser().parse(request)
        question=Questions.objects.get(QuestionId=question_data['QuestionId'])
        questions_serializer=QuestionSerializer(question,data=question_data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        question=Questions.objects.get(QuestionId=id)
        question.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def answerApi(request,id=0):
    if request.method=='GET':
        answers = Answers.objects.all()
        answers_serializer=AnswerSerializer(answers,many=True)
        return JsonResponse(answers_serializer.data,safe=False)
    elif request.method=='POST':
        answer_data=JSONParser().parse(request)
        answers_serializer=AnswerSerializer(data=answer_data)
        if answers_serializer.is_valid():
            answers_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        answer_data=JSONParser().parse(request)
        answer=Answers.objects.get(AnswerId=answer_data['AnswerId'])
        answers_serializer=AnswerSerializer(answer,data=answer_data)
        if answers_serializer.is_valid():
            answers_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        answer=Answers.objects.get(AnswerId=id)
        answer.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def tagApi(request,id=0):
    if request.method=='GET':
        tags = Tags.objects.all()
        tags_serializer=TagSerializer(tags,many=True)
        return JsonResponse(tags_serializer.data,safe=False)
    elif request.method=='POST':
        tag_data=JSONParser().parse(request)
        tags_serializer=TagSerializer(data=tag_data)
        if tags_serializer.is_valid():
            tags_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        tag_data=JSONParser().parse(request)
        tag=Tags.objects.get(TagId=tag_data['TagId'])
        tags_serializer=TagSerializer(tag,data=tag_data)
        if tags_serializer.is_valid():
            tags_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        tag=Tags.objects.get(AnswerId=id)
        tag.delete()
        return JsonResponse("Deleted Successfully",safe=False)

