#polls/urls.py (URLconf)

# using django.conf.urls.url for now but may be deprecated soon
from django.conf.urls import url
# django.urls.path is only available in Django 2.0
#from django.urls import path

from . import views

# understand difference between django.conf.urls.url and django.urls.path

# should a regex be given as first argument of url?
urlpatterns = [
    # ex: /polls/
    url('', views.index, name='index'),
    # ex: /polls/5/
    url('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    url('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    url('<int:question_id>/vote/', views.vote, name='vote'),
]

"""
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""