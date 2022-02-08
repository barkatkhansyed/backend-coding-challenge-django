from django.db import models

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    tags = models.CharField(max_length=25, blank=False, null=False)
    is_public = models.BooleanField(default=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE, default=None)
