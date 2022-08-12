from django.urls import path

from jobs97test import views


urlpatterns = [
    # path('', MainpageView.as_view(), name='mainpage'),
    path('', views.jobs97_all, name='jobs97_all'),
    path('<int:pk>', views.jobs97_click, name='jobs97_click'),
]