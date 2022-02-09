from django.db import models
from crum import get_current_user


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    tags = models.CharField(max_length=25, blank=False, null=False)
    is_public = models.BooleanField(default=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='notes',
                              on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        current_user = get_current_user()
        if current_user:
            self.owner = current_user
            super(Note, self).save(*args, **kwargs)
