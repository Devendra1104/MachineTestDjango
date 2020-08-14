from .serializers import UserSerializer,ClientSerializer,ProjectSerializer,ClientProjectSerializer,CreateProjectSerializer
from .models import Project,Client
from rest_framework import generics
from django.utils import timezone


# Get list of clients
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Create new Client
class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

# Update Client info
class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user,updated_at = timezone.now())

# Delete Client
class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Get clients project details.
class ClientProjectView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientProjectSerializer


class UserProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(created_by = self.request.user)

class CreateProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = CreateProjectSerializer










