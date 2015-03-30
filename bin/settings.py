import os


LANGUAGES = [
    ('en', 'English'),
    ('el', 'Greek'),
]

LANGUAGE_NAMES = dict(LANGUAGES)
DEFAULT_LANGUAGE = 'en'

SUPPORTED_FILES = [
    '.html'
]


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BUILD_DIRECTORY = os.path.join(BASE_DIR, 'build')
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')
SRC_DIR = os.path.join(BASE_DIR, 'src')
