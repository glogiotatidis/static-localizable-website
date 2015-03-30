# Static Website with localization support

Parses [Jinja2](http://jinja.pocoo.org/docs/) templates to produce localized static websites. Serves static content using [WhiteNoise](noise.evans.io/whitenoise) and [gunicorn](http://gunicorn.org/) through a custom wsgi app that extract browser's preferred language through the `HTTP_ACCEPT_LANGUAGE` header and redirects accordingly.

## Develop Website

* Run the server `docker-compose up`.
* Visit [http://localhost:8000](http://localhost:8000).
* Edit contents in [src](src) directory. Use `trans` blocks or `_()`
  to mark localizable strings.
* Re-build by running `docker-compose run web ./build`.

## Extract strings

* Run `docker-compose run web ./makemessages --all`.

## Compile strings

* Run `docker-compose run web ./compilemessages`.
