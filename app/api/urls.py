from django.urls import path
from .views import NotesView

urlpatterns = [
    path(r'note', NotesView.as_view(), name='notes-create')
]
