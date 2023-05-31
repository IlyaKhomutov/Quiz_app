from django.db import models
import random
difficulty_levels = (
    ('easy', 'easy'),
    ('average', 'average'),
    ('hard', 'hard')
)


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    noq = models.IntegerField()
    duration = models.IntegerField(help_text="duration of the quiz")
    passing_score = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=7, choices=difficulty_levels)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.questions.all())
        random.shuffle(questions)
        return questions[:self.noq]

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
