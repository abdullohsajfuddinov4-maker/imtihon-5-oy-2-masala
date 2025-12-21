from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, CreateCommentView, \
    DeleteCommentView
from .views import ProductCategory ,UpdateCommentView
urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('category/<int:pk>', ProductCategory.as_view(), name='category'),
    path('create', ProductCreate.as_view(), name='create'),
    path('dateil/<int:pk>', ProductDetail.as_view(), name='detail'),
    path('comment/create/<int:pk>/', CreateCommentView.as_view(), name='create_comment'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='delete'),
    path('update_comment/<int:pk>', UpdateCommentView.as_view(), name='update_comment'),
path('delete_comment/<int:pk>/',DeleteCommentView.as_view(),name='delete_comment'),

]
