Django Simple SASS
==================

This package simply compiles all the [SASS](https://sass-lang.com/)
files it finds in your Django project and places the compiled CSS
files in the same directory. The goal is to simplify both the
development and the deployment of SASS source files.

To use Simple SASS, perform the following steps:

1. Install: `pip install git+https://github.com/rtts/django-simplesass.git`

2. Add `simplesass` to your `INSTALLED_APPS`:

    INSTALLED_APPS += ['simplesass']

3. Add the following middleware:

    MIDDLEWARE += ['simplesass.middleware.SimpleSassMiddleware']

Finally, it's **very important** that you run the development server
with the `--nostatic` command line argument. Otherwise, the middleware
will be ignored for static files. During development, however, you
will need those static files to be served. You can do so by manually
invoking the `staticfiles_urlpatterns()` function:

    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns = []

    if settings.DEBUG:
        urlpatterns += staticfiles_urlpatterns()
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
