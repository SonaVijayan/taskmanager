from django.urls import path
from .views import *

urlpatterns=[
    path('pdash',ProjectDashboardView.as_view(),name='pdash'),
    path('padd',AddProjectView.as_view(),name='padd'),
    path('pdel/<int:id>',DeleteTaskView.as_view(),name='pdel'),
     path('pedit/<int:id>',EditProjectView.as_view(),name='pedit')

]