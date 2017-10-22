{
    'name': 'First page after login',
    'category': 'base',
    'summary': 'Set up different first page after login for each user.',
    'version': '10.0',
    'description': """Set up different first page after login for each user.""",
    'depends': ['auth_signup'],
    'data': [
        'views/users.xml',
    ],
    'qweb': [
        ],
    'installable': True,
    'auto_install': False,
}

