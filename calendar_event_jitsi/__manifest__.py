# Copyright (C) 2020-Today: Druidoo (<https://www.druidoo.io>)
{
    "name": "Jitsi Calendar Event",
    "summary": "This module used to create Jitsi meeting from Odoo event",
    "category": "Tools",
    "author": "Druidoo",
    "maintainers": ["ivantodorovich"],
    "development_status": "Beta",
    "website": "https://www.druidoo.io/",
    "license": "AGPL-3",
    "version": "13.0.2.0.0",
    "depends": ["calendar"],
    'data': [
        'views/calendar_views.xml',
        'data/mail_template_data.xml',
    ],
    "installable": True,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
}