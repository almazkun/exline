# exline
exile api

## Deploy to Heroku:
1. `pipenv install gunicorn whitenoise dj-database-url`
2. add to settings static files:
```py
#settings/settings.py
# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = BASE_DIR / "staticfiles"
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    BASE_DIR / "static",
)
# http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```
3. Add Whitenoise middleware after security middleware:
```py
# settings/settings.py
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```
4. Create `Procfile` and populate with the following `web: gunicorn settings.wsgi --log-file -`:
```sh
echo "web: gunicorn settings.wsgi --log-file -" > Procfile
```
5. Postgres DB, add default database to `settings.py`
```py
# settings/settings.py
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
```
