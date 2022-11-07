from django.urls import path

from project import views
#
urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='projects'),
    path('new_project/', views.NewProjectCreateView.as_view(), name='new-project'),
    path('update_project/<int:pk>', views.ProjectUpdateView.as_view(), name='update-project'),
    path('delete_project_modal/<int:pk>', views.delete_project_modal, name='delete-project-modal'),
    path('details_project/<int:pk>', views.ProjectDetailView.as_view(), name='details_project')
]