from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

#create a router and register our viewset with it.
router =DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)


urlpatterns = (
    url(r'^', include(router.urls)),
)