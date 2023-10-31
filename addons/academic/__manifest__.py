{
    'name': 'Academic',
    'version': '1.0',
    'category': 'Education',
    'description': 'Academic Module',
    'depends': ['base'],
    'data': [
        'views/my_view.xml',
        'views/menu.xml',
        'views/session.xml',
        'views/attendee.xml',
        'views/partner.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}