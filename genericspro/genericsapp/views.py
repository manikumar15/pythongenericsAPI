from django.shortcuts import render
from rest_framework import generics
from .serializers import EmpSerializer
from .models import Emp


class GenericView_List(generics.ListCreateAPIView):
	queryset = Emp.objects.all()
	serializer_class = EmpSerializer

class GenericView_Details(generics.RetrieveUpdateDestroyAPIView):
	queryset = Emp.objects.all()
	serializer_class = EmpSerializer
