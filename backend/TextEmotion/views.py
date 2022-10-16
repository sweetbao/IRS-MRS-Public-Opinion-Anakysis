from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Tweet, Topic
from .serializers import TweetSerializer,TopicSerializer
from .service import get_latestTopic



class TweetViewSet(viewsets.ModelViewSet):

     queryset = Tweet.objects.all().order_by('-retrievetime')
     serializer_class = TweetSerializer
     def get_queryset(self):
        title = self.request.query_params.get("title", None)
        if title:
            qs = Tweet.objects.filter()
            qs = qs.filter(title=title)

            return qs

        return super().get_queryset()

class TopicViewSet(viewsets.ModelViewSet):

     queryset = Topic.objects.all().order_by('rank')
     serializer_class = TopicSerializer


def addTopic(request):
    topicList = get_latestTopic()
    Topics = []
    rank = 1
    for topic in topicList:
        topicN = Topic(rank = rank,name = topic)
        topicN.save()
    return