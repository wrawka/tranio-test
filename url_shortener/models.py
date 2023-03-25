from django.db import models
from django.utils.translation import gettext_lazy as _


class UserShortURL(models.Model):
    """Represents user submitted URL and it's properties."""

    url = models.URLField(verbose_name=_('User URL'))
    key = models.CharField(verbose_name=_('Access Key'), max_length=6)
    admin_key = models.CharField(verbose_name=_('Admin Key'))
    is_active = models.BooleanField(verbose_name=_('Is Active'))
    clicks = models.PositiveBigIntegerField(verbose_name='Clicks Count')

    def __str__(self) -> str:
        return f'URL:{self.key}'
