from user_profile.models import UserProfile
from django.http import Http404
from django.db import models
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework import viewsets, generics, mixins
from user_profile.serializers import UserProfileSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserProfileView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    lookup_field = 'user__username'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserProfileSerializer

    def check_permissions(self, request):
        super().check_permissions(request)
        if not request.user.is_superuser and self.get_object().user != request.user and request.method not in SAFE_METHODS:
            self.permission_denied(
                request,
            )

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = UserProfileSerializer(obj, context={"request": request})
        return Response(serializer.data)

    def get_object(self):
        try:
            return self.get_queryset().get(user__username=self.kwargs['username'])
        except models.ObjectDoesNotExist:
            raise Http404
