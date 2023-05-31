from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'quizzes'

urlpatterns = [
    path('', login_required(QuizListView.as_view(), login_url='accounts:login'), name='main-view'),
    path('<int:pk>/', quiz_view, name='quiz-view'),
    path('<int:pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('results/', ResultsListView.as_view(), name='results'),

]
