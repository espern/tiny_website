#Things to be initialized before menu.py

#website parameters fixture
if db(db.website_parameters.id > 0).count() == 0:
    db.website_parameters.insert(
    website_name="Fork me, I'm famous",
    website_name_long="my awesome website",
    website_url='http://www.my-awesome-website.com',
    contact_name='John doe',
    contact_trade_register_number='243 849 247 22 98',
    contact_address="""
    Route de l'aéroport 15
    1215 Geneva
    Switzerland
    """,
    contact_google_maps_plan_url=r"""
    http://maps.google.fr/maps?q=Geneva+International+Airport,+Meyrin,+Suisse&hl=fr&ll=46.237328,6.10857&spn=0.038054,0.104628&sll=46.230084,6.126595&sspn=0.038059,0.104628&oq=geneva+ai&t=h&hq=Geneva+International+Airport,+Meyrin,+Suisse&z=14&iwloc=A                                                                                         
    """,
    contact_telephone='123 456 789',                                                                                        
    contact_fax='987 654 321',
    contact_mobile='',                                                                        
    contact_form_email='user@test.com',
    contact_form_cc='',
    contact_form_bcc='',
    booking_form_email='user@test.com',
    booking_form_cc='',
    booking_form_bcc='',
    mailserver_url='smtp.test.com',
    mailserver_port=587,
    mailserver_sender_mail='user@test.com',
    mailserver_sender_login='user',
    mailserver_sender_pass='pass',
    google_analytics_id='UA-XXXXXXX-1'
    )


WEBSITE_PARAMETERS = db(db.website_parameters).select().first()
## configure email
mail = auth.settings.mailer
mail.settings.server = '%s:%s' %(WEBSITE_PARAMETERS.mailserver_url, WEBSITE_PARAMETERS.mailserver_port)
mail.settings.sender = WEBSITE_PARAMETERS.mailserver_sender_mail
mail.settings.login = '%s:%s' %(WEBSITE_PARAMETERS.mailserver_sender_login, WEBSITE_PARAMETERS.mailserver_sender_pass)

## your http://google.com/analytics id
response.google_analytics_id = None if request.is_local else WEBSITE_PARAMETERS.google_analytics_id

response.subtitle = WEBSITE_PARAMETERS.website_name
