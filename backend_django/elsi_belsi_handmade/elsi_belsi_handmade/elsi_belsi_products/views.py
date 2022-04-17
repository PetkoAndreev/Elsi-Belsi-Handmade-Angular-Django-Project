from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SimpleView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'messsage': 'It works',
        })
