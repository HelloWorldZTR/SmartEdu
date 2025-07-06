from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Resume, UserStats
from .serializers import UserSerializer, ResumeSerializer, UserStatsSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                username=serializer.validated_data['username'],
                password=request.data['password'],
                school=serializer.validated_data.get('school', ''),
                department=serializer.validated_data.get('department', '')
            )
            return Response(UserSerializer(user).data, status=201)
        return Response(serializer.errors, status=400)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user

class ResumeView(generics.RetrieveUpdateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return Resume.objects.get_or_create(user=self.request.user)[0]

class UserStatsView(generics.RetrieveAPIView):
    serializer_class = UserStatsSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return UserStats.objects.get(user_id=self.kwargs['pk'])
