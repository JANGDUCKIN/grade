from django.urls import path
from . import views

app_name = 'scoring'

urlpatterns = [
	# /scoring/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),


    # 사용자에게 필요한것 
    path('register/', views.UserFormView.as_view(), name='register'),

    path('logout_user/', views.logout_user, name='logout_user'),

    path('login_user/', views.login_user, name='login_user'),

    # /scoring/<ui_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /scoring/uploadfile/add/
    path('uploadfile/add/', views.UploadFileCreate.as_view(), name='uploadfile-add'),

    # /scoring/uploadfile/<ui_id>/
    path('uploadfile/<int:pk>/', views.UploadFileUpdate.as_view(), name='uploadfile-update'),
 
    # /scoring/uploadfile/<ui_id>/delete
    path('uploadfile/<int:pk>/delete/', views.UploadFileDelete.as_view(), name='uploadfile-delete'),

]
