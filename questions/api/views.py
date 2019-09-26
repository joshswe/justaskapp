from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from questions.api.serializers import QuestionSerializer, AnswerSerializer
from questions.models import Question, Answer
from questions.api.permissions import IsAuthorOrReadOnly

# Provide CRUD functionality for questions
class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer

    # The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)


# Allow users to answer a question instance if they haven't already
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this Question!")
        serializer.save(author=self.request.user, question=question)


# Provide the answers queryset of a specific question
class AnswerListAPIView(generics.ListAPIView):
    
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")


# Provide RUD (retrieve, update and destroy) functionality for an answer instance to its author
class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]


# Allow users to add/remove like to/from an answer instance
class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer,context = serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer,context = serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)