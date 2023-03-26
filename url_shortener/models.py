from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserShortURL(TimeStampedMixin):
    """Represents user submitted URL and it's properties."""

    url = models.URLField(verbose_name=_('User URL'))
    key = models.CharField(verbose_name=_('Access Key'), max_length=6)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)
    clicks = models.PositiveBigIntegerField(verbose_name='Clicks Count', default=0)

    def __str__(self) -> str:
        return f'URL:{self.key}'
