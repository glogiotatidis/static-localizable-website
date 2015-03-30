from whitenoise import WhiteNoise

from settings import BUILD_DIRECTORY, DEFAULT_LANGUAGE, LANGUAGE_NAMES


def application(env, start_response):
    if env.get('PATH_INFO') == '/':
        for language in env.get('HTTP_ACCEPT_LANGUAGE').split(';')[0].split(','):
            if language in LANGUAGE_NAMES:
                break
        else:
            language = DEFAULT_LANGUAGE
        start_response('302 Found', [('Location', '{}/index.html'.format(language))])
    return [b'']


application = WhiteNoise(application)
application.add_files(BUILD_DIRECTORY)
