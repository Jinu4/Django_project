from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun, name='fun'),
    path('cate', views.cate, name='cate'),
    path('search/', views.searching, name='search'),
    path('details/', views.details, name='details'),
    path('<slug:c_slug>/', views.cate, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.details, name='details')

]
