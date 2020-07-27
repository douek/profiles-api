from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
]


# code without using router
# profile_list = ProfileViewSet.as_view({'get':'list'})

# profile_detail = ProfileViewSet.as_view({'get':'retrieve'})

# urlpatterns = [
#     path('profiles/',profile_list, name='profile-list'),
#     path('profiles/<int:pk>/',profile_detail, name='profile-detail'),
# ]