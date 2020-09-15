def activate_django_env():
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'rfa.settings')
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
