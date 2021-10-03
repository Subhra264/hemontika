from rest_framework import status
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from .models import Recitation
from .serializers import (
    CreateDestroyRecitationSerializer,
    ListRecitationSerializer,
    RetrieveRecitationSerializer,
    UpdateRecitationSerializer,
)
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView


class ListRecitationView(ListAPIView):
    queryset = Recitation.objects.all()
    serializer_class = ListRecitationSerializer


class CreateRecitationView(CreateAPIView):
    queryset = Recitation.objects.all()
    serializer_class = CreateDestroyRecitationSerializer

    def perform_create(self, serializer):
        return serializer.save(reciter=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        serialized_instance = RetrieveRecitationSerializer(instance)
        return Response(serialized_instance.data)


class RetrieveUpdateDeleteRecitationView(RetrieveUpdateDestroyAPIView):
    queryset = Recitation.objects.all()
    serializer_class = RetrieveRecitationSerializer

    def get_serializer_class(self):
        print("self.request.method ", self.request.method)
        if self.request.method == "GET":
            return self.serializer_class
        elif self.request.method == "PATCH" or self.request.method == "DELETE":
            return UpdateRecitationSerializer
        elif self.request.method == "PUT":
            raise NotAcceptable("The request method is not acceptable")

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Recitation object deleted successfully"}, status=status.HTTP_200_OK)
