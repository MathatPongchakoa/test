from django.urls import path
from .views import *
from .views import EditCourseView

urlpatterns = [
   path('',courseList,name='courseList'),
   path('s/',course_idsearch,name='search_id'),
   path('e/<str:pk>/',EditCourseView.as_view(),name='Edit'),
   path('d/<str:pk>/',delete.as_view(),name='delete'),
]