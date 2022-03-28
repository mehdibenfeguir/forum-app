from django.conf.urls import url
from ForumApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^comment-question$',views.commentQuestionApi),
    url(r'^comment-question/([0-9]+)$',views.commentQuestionApi), 

    url(r'^comment-answer$',views.commentAnswerApi),
    url(r'^comment-answer/([0-9]+)$',views.commentAnswerApi), 

    url(r'^question$',views.questionApi),
    url(r'^question/([0-9]+)$',views.questionApi),

    url(r'^answer$',views.answerApi),
    url(r'^answer/([0-9]+)$',views.answerApi),

    url(r'^tag$',views.tagApi),
    url(r'^tag/([0-9]+)$',views.tagApi),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)