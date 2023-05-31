from django.db import models
from quizzes.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    correct_field = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct_field}"
