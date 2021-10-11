from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.selectors import get_users
from apps.users.serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = get_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
