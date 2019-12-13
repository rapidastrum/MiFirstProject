from django.urls import path
from . import views

app_name = "opros"

urlpatterns = [
	path('start_quiz/', views.start_quiz, name="start_quiz"),
]
