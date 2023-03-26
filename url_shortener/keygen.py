import secrets
import string

from django.db.models import Q

from url_shortener.models import UserShortURL


KEY_LENGTH = 6


def create_random_key(length: int = KEY_LENGTH) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))


def create_unique_random_key() -> str:
    key = create_random_key()
    while UserShortURL.objects.filter(Q(key__exact=key)).exists():
        key = create_random_key()
    return key
