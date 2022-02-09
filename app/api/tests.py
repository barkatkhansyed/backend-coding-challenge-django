from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from .views import NotesView, NotesListView, NotesFilterView, NotesSearchView
import json

# TODO
# Composed the structure or how the code look like 
# But it has some bugs and needs time to be fixed.

class NotesApiTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        # Credentials
        self.admin_user_email = "admintest@unittest.com"
        self.admin_user_password = "admintest@123"
        self.user_email = "test@unittest.com"
        self.user_password = "test@123"
        # Create users
        self.admin_user = User.objects.create_superuser(
            self.admin_user_email,
            self.admin_user_password)
        self.user = User.objects.create_user(
            self.user_email,
            self.user_password,
            is_active=False)
        
    def test_add_notes(self):
        payload = {"title": "Public Note", "body": "I am a public test note", "tags":"public", "is_public": True}
        url = '/api/note'
        request = self.factory.post(url, 
                                    json.dumps(payload),
                                    content_type='application/json')
        # Bad request
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        
        force_authenticate(request, user=self.admin_user)
        
        # Successful request
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_update_notes(self):
        payload = {"title": "Updated Private Note", "body": "Before I was public, now I am a private test note", "tags":"private", "is_public": False}
        url = '/api/note/1'
        request = self.factory.put(url, 
                                    json.dumps(payload),
                                    content_type='application/json')
        
        # Bad request - updating without authentication
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 401)
        
        # Bad request - updating with invalid user
        force_authenticate(request, user=self.user)
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 401)
        
        # Successful request - updating with valid user
        force_authenticate(request, user=self.admin_user)
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_notes(self):
        url = '/api/note/1'
        request = self.factory.delete(url)
        
        # Bad request - deleting without authentication
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 401)
        
        # Bad request - deleting with invalid user
        force_authenticate(request, user=self.user)
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 401)
        
        # Successful request - deleting with valid user
        force_authenticate(request, user=self.admin_user)
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_list_all_notes(self):
        # There already exists a public note
        # Lets create a private note
        payload = {"title": "Private Note", "body": "I am a private test note", "tags":"private", "is_public": False}
        url = '/api/note'
        request = self.factory.post(url, 
                                    json.dumps(payload),
                                    content_type='application/json')
        
        force_authenticate(request, user=self.admin_user)
        
        # Private note successfully created request
        response = NotesView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        
        # Lets call listnotes
        # Atm it will fetch one note because unauthenticated
        url = '/api/listnotes'
        request = self.factory.get(url)
        response = NotesListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        force_authenticate(request, user=self.admin_user)
        response = NotesListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
    def test_filter_notes_with_tags(self):
        tag = 'private'
        url = '/api/filternotes/{tag}'.format(tag=tag)
        request = self.factory.get(url)
        force_authenticate(request, user=self.admin_user)
        response = NotesFilterView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    def test_search_notes_with_keywords(self):
        keyword = 'private'
        url = '/api/searchnotes/{keyword}'.format(keyword=keyword)
        request = self.factory.get(url)
        force_authenticate(request, user=self.admin_user)
        response = NotesSearchView.as_view()(request)
        self.assertEqual(response.status_code, 200)
