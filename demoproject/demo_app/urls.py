from . import views
from django.urls import path

urlpatterns = [
    # path('',views.home,name="home"),
    # path('about/',views.about,name="about"),
    # path('contact/',views.contact,name="contact"),
    # path('detail/',views.detail,name="detail"),
    # path('thanx/',views.thanx,name="thanx"),
    # path('',views.operation,name="operation"),
    # path('res/',views.result,name="result"),
    path('',views.demo,name='demo')


]