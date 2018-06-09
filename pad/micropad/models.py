from django.db import models
from django.utils.translation import ugettext_lazy as _
from boogie.rest import rest_api
from django.contrib.auth.models import User


#@rest_api()
class Folder(models.Model):
    """
    Represents a folder.
    """

    name = models.CharField(max_length=50)
    relates_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

#@rest_api()
class File(models.Model):
    """
    Represents a file.
    """
    folder = models.ForeignKey(Folder, related_name="files", on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=140)
    lock = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

