from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    # below adding endpoint for pledges:
    path('pledges/', views.PledgeList.as_view()),
]
# look at plan of endpoints ^ if we go to /projects want to see all projects

urlpatterns = format_suffix_patterns(urlpatterns)
# 