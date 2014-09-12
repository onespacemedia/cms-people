=====
People
=====

People just adds a person management module to the Onespacemedia CMS, it needs
the Onespacemedia CMS to run as it uses dependencies from that app.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "people" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'people',
    )

2. Run `python manage.py migrate` to create the models.
