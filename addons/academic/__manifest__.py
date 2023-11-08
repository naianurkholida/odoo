{
    'name': 'Academic',
    'version': '1.0',
    'category': 'Education',
    'description': 'Academic Module',
    'depends': ['base','account', 'board'],
    'data': [
        'views/my_view.xml',
        'views/menu.xml',
        'views/session.xml',
        'views/dashboard.xml',
        'views/attendee.xml',
        'views/partner.xml',
        'security/group.xml',
        'security/ir.model.access.csv',
        'report/session.xml',
    ],
    'installable': True,
    'auto_install': False,
    
}