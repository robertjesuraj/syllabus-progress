from django.urls import path

from . import views

app_name = 'kichu'
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.SyllabusList.as_view(), name='syllabus_list'),
    path('new', views.SyllabusCreate.as_view(), name='syllabus_new'),
    path('edit/<int:pk>', views.SyllabusUpdate.as_view(), name='syllabus_edit'),
    path('delete/<int:pk>', views.SyllabusDelete.as_view(), name='syllabus_delete'),
    ]
