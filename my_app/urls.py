from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',indexPageView,name='index'),
	path('post_detail/<str:post_id>/',postDetailPageView,name='post_detail'),
	path('category/<int:category_id>/',categoryPage,name='category'),
	path('post_edit/<int:pk>/',PostUpdateView.as_view(),name='post_edit'),
	path('post_delete/<int:pk>/',PostDeleteView.as_view(),name='post_delete'),
	path('post_create/',PostCreateView.as_view(),name='psot_create'),
	] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)