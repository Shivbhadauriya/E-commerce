from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("frontpage",views.frontpage,name="frontpage"),
    path("grocery",views.grocery,name="grocery"),
    path("mobile",views.mobile,name="mobile"),
    path("footer",views.footer,name="footer"),
]
