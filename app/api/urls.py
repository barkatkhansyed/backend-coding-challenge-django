from django.urls import path
from .views import NotesView, NotesListView

urlpatterns = [
    path(r'note', NotesView.as_view(), name='notes-create'),
    path(r'note/<int:pk>', NotesView.as_view(), name='notes-update/delete'),
    path('listnotes', NotesListView.as_view(), name='notes-list'),
]
