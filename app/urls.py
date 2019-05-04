from django.urls import path, re_path, include
from django.conf.urls import url
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryViewSet
from .views import FormulaViewSet
from .views import CustomAuthToken

router = DefaultRouter()
router.register(r'formula', FormulaViewSet, basename='formula')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),    
]

urlpatterns += [
    url(r'^api-token-auth/', CustomAuthToken.as_view())
]