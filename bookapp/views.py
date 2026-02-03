from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, BookSerializer
from django.contrib.auth.models import User
from .models import Book
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status=status.HTTP_200_OK)
    
class BookCreateView(APIView):
    permission_classes = [IsAuthenticated]
    # create book
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Book Created Successfully",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get all books
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
class BookUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    # get single book
    def get(self,request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({
                "message":"Book Not Found for this ID",
            },status=status.HTTP_404_NOT_FOUND)
        return Response(BookSerializer(book).data)
    
    # update book
    def put(self,request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({
                "message":"Book Not Found for this ID",
            },status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Book Updated Successfully",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # delete book
    def delete(self,request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({
                "message":"Book Not Found for this ID",
            },status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({
            "message":"Book Deleted Successfully"
        },status=status.HTTP_200_OK)