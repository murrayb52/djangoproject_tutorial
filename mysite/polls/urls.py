from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # Remember: due to /mysite/urls.py, the following urls will be at domain/polls/
    path('', views.IndexView.as_view(), name='index'),
    # The DetailView generic view expects the primary key value captured from the URL
    # to be called "pk", so we’ve changed question_id to pk for the generic views.
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
