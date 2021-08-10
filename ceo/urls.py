from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
#from .router import router
#from rest_framework.authtoken import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    # path('ceo/', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),

]