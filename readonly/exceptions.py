from __future__ import absolute_import
from django.db.utils import DatabaseError


class DatabaseWriteDenied(DatabaseError):
    pass
