from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='projects-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    # below adding endpoint for pledges:
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    # path('categories/<int:pk>/', views.CategoryList.as_view(), name='category-list'),
]
# look at plan of endpoints ^ if we go to /projects want to see all projects

urlpatterns = format_suffix_patterns(urlpatterns)
# 