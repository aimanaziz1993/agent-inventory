from django.urls import path

from . import views

app_name = 'inventory_api'

urlpatterns = [
    path('', views.InventoryList.as_view(), name='inventory_list'),
    path('<int:id>', views.InvetoryDetailProp.as_view(), name='inventory_detail'),
    # path('<int:id>', views.InventoryDetail.as_view(), name='inventory_detail'),
    path('<str:slug>', views.InventoryProfileDetail.as_view(), name='detail-post'),


    path('listing-category', views.CategoryList.as_view(), name='category_list'),
    path('listing-propertytype', views.PropertyTypeList.as_view(),
         name='propertytype_list'),
]
