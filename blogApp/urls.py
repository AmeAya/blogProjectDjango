from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, \
    BlogUpdateView, BlogDeleteView, homePageView, testCreateView

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='newPost'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='updatePost'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='deletePost'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('fakeHomePage', homePageView, name='fakeHome'),
    path('newTest', testCreateView, name='testView'),
    path('', BlogListView.as_view(), name='home'),
]
#qwe
