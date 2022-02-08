from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

class NotesView(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    """
    If logged in, Users can add, delete and modify their notes
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class NotesListView(APIView):
    """
    - Users can see a list of all their notes
    - Notes can be either public or private
    - Public notes can only be viewed without authentication
    """
    
    def get(self, request, *args, **kwargs):
        note_objs = Note.objects.filter(owner=request.user.id) if request.user.is_authenticated else Note.objects.filter(is_public=True, owner=request.user.id)
        serializer = NoteSerializer(note_objs, many=True)
        return Response(serializer.data)
