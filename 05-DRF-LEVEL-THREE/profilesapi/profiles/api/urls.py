from django.urls import path
from profiles.api.views import ProfileList

urlpatterns = [
    path("profiles/", ProfileList.as_view(), name="profile-list")
]