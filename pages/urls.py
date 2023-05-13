# Here we will import the HomePageView and set the path again to the empty string ""
# Note that we provide an optional but recommended named URL of "home" at the end
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
