from django.db import models
from django.utils import timezone
from artist.models import Artist


class Record(models.Model):
    creator = models.OneToOneField('auth.User', related_name="creator")
    person_in_charge = models.ForeignKey('auth.User')
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=255)
    original_release_year = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.artist.name + ' - ' + self.title

# Create your models here.
