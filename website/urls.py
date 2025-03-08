from django.urls import path

from . import views

urlpatterns = [
    # Create a home page
    path("", views.home, name="home"),
    # path("login/", views.login_user, name="login"),  # this line left in case we want to make a separate login page
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.get_customer_record, name="record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path("add_record/", views.add_record, name="add_record"),
    path("update_record/<int:pk>", views.update_record, name="update_record"),
]
