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
6. `heroku config:set DISABLE_COLLECTSTATIC=1 -a exline`


## Usage:
1. Update city list from exline API
`http://exline.herokuapp.com/e/update/`
2. Search for City by name:
`http://exline.herokuapp.com/e/search/?search=Алматы`
3. Get list of all Cities:
`http://exline.herokuapp.com/e/cities/`
4. Calculate shipping price from Almaty to other City (destination_id and weight required):
`http://exline.herokuapp.com/e/calculate/?destination_id=4&weight=2.5`
