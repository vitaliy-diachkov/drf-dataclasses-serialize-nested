from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.dataclasses import User
from apps.users.selectors import get_users
from apps.users.serializers import CustomDataclassSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = get_users()
        serializer = CustomDataclassSerializer(
            instance=users,
            dataclass=User,
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
