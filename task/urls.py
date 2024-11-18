
from django.urls import path
# from.views  import dashboardView
from .views import DashboardView,AddTaskView,DeleteTaskView,EditTaskView,LandingView,RegView


urlpatterns = [
    # path('dashboard',DashboardView,name='dashboard'),
    path('dashboard',DashboardView.as_view(),name='dashboard'),
    path('add',AddTaskView.as_view(),name='add'),
     path('delete/<int:id>',DeleteTaskView.as_view(),name='delete'),
    
    path('edit/<int:id>',EditTaskView.as_view(),name='edit'),
    path('landing',LandingView.as_view(),name='landing'),
    path('reg',RegView.as_view(),name='reg'),
]