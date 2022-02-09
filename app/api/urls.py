from django.urls import path
from .views import NotesView, NotesListView, NotesFilterView, NotesSearchView

urlpatterns = [
    path(r'note', NotesView.as_view(), name='notes-create'),
    path(r'note/<int:pk>', NotesView.as_view(), name='notes-update/delete'),
    path('listnotes', NotesListView.as_view(), name='notes-list'),
    path('filternotes/<slug:tags>', NotesFilterView.as_view(),
         name='notes-filter'),
    path('searchnotes/<slug:keyword>', NotesSearchView.as_view(),
         name='notes-search'),
]
