from django.db import models
from django.utils.translation import ugettext_lazy as _
from boogie.rest import rest_api
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def no_slash_validator(st):
    if '/' in st:
        raise ValidationError('cannot include / on path name')

def starts_with_slash_validator(st):
    if not st.startswith('/'):
        raise ValidationError('url must start with /')


@rest_api()
class Folder(models.Model):
    """
    Represents a folder.
    """

    name = models.CharField(
        max_length=50,
        validators=[no_slash_validator],
    )
    parent = models.ForeignKey(
        'self', 
        related_name="children", 
        on_delete=models.CASCADE, 
        null=True,
    )

    @property
    def url(self):
        if not self.parent:
            return '/'
        else:
            return self.parent.url + self.name + '/'


    class Meta:
        unique_together = [('name', 'parent')]


@rest_api()
class File(models.Model):
    """
    Represents a file.
    """
    folder = models.ForeignKey(Folder, related_name="files", on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=50)
    ext = models.CharField(max_length=10)
    url = models.CharField(
        max_length=140, 
        unique=True,
        validators=[starts_with_slash_validator],
    )
    lock = models.BooleanField(default=False)
    owner_username = models.CharField(max_length=50, null=True)

    @property
    def url_with_slash(self):
        if self.url.startswith('/'):
            return self.url
        return '/' + self.url