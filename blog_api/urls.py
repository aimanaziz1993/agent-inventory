from django.urls import path

# from rest_framework.routers import DefaultRouter

from . import views

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', views.PostList, basename='posts')
# urlpatterns = router.urls

urlpatterns = [
    path('posts/<str:slug>/', views.PostDetail.as_view(), name='detail-post'),
    path('query', views.PostListDetailfilter.as_view(), name='postsearch'),
    path('', views.PostList.as_view(), name='list-create'),

    # Post Admin URLs
    path('admin/create/', views.CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', views.AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', views.EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', views.DeletePost.as_view(), name='deletepost'),
]


