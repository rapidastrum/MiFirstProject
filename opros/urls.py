from django.urls import path
from . import views

app_name = 'opros'
urlpatterns = [
	path('', views.start_test, name='start_test'),
	path('question/', views.get_question, name='get_question'),
]
