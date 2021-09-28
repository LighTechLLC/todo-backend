from split_settings.tools import optional, include

include(
    'base.py',
    'templates.py',
    'databases.py',
    'swagger.py',
    'rest.py',

    optional('local_settings.py'),
)
