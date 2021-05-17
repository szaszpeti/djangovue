from rest_framework import generics, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from questions.models import Answer, Question
from rest_framework.permissions import IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly


class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all().order_by("-created_at")
	lookup_field = "slug"
	serializer_class = QuestionSerializer
	permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
	#allow ansewre single specific question based on our slug passed in the endpoint
	#check if the user already answered the question
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		request_user = self.request.user
		kwarg_slug = self.kwargs.get("slug")
		question = get_object_or_404(Question, slug=kwarg_slug)

		if question.answers.filter(author=request_user).exists():
			raise ValidationError("You have already answered this Question!")

		serializer.save(author=request_user, question=question)

class AnswerListAPIView(generics.ListAPIView):
	serializer_class = AnswerSerializer
	permission_classes = [IsAuthenticated]

	#override the queryset() get all the answeres given by the question's slug
	def get_queryset(self):
		kwarg_slug = self.kwargs.get("slug")
		return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
	permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class AnswerLikeAPIView(APIView):
	#Allow users to add/remove a like to/from an answer instance
	serializer_class = AnswerSerializer
	permission_classes = [IsAuthenticated]

	def delete(self, request, pk):
		#"""Remove request.user from the voters queryset of an answer instance."""
		answer = get_object_or_404(Answer, pk=pk)
		user = request.user

		answer.voters.remove(user)
		answer.save()

		#returning the serilized data for the specific instance
		serializer_context = {"request": request}
		serializer = self.serializer_class(answer, context=serializer_context)

		return Response(serializer.data, status=status.HTTP_200_OK)


	def post(self, request, pk):
		"""Add request.user to the voters queryset of an answer instance."""
		answer = get_object_or_404(Answer, pk=pk)
		user = request.user

		answer.voters.add(user)
		answer.save()

		serializer_context = {"request": request}
		serializer = self.serializer_class(answer, context=serializer_context)

		return Response(serializer.data, status=status.HTTP_200_OK)