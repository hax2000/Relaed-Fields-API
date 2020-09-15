from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import MainTableSerializer


class MainTableUploadView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    @action(['post'], detail=False)
    def upload_records(self, request, *args, **kwargs):
        seriazlizer = MainTableSerializer(data=request.data, many=True)
        seriazlizer.is_valid(raise_exception=True)
        seriazlizer.save(owner=request.user)
        return Response(seriazlizer.data)
