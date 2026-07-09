from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .models import Job
from .serializer import JobSerializer


def home(request):
    return HttpResponse("Welcome to Zecpath AI Job Portal")


class JobListAPIView(APIView):

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


class JobCreateAPIView(APIView):

    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTestAPIView(APIView):

    def get(self, request):
        return Response({
            "message": "Hello User",
            "status": "Success",
            "course": "Django REST Framework"
        })