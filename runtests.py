#!/usr/bin/env python
import sys
from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',

        # Uncomment below to run tests with mysql
        #DATABASE_ENGINE='django.db.backends.mysql',
        #DATABASE_NAME='readonly_test',
        #DATABASE_USER='readonly_test',
        #DATABASE_HOST='/var/mysql/mysql.sock',
        INSTALLED_APPS=[
            'readonly',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
        SITE_READ_ONLY=True,
    )


def runtests(*test_args):
    from django.test.runner import DiscoverRunner
    failures = DiscoverRunner(
        verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
