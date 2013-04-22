# coding: utf8

#Create a "manager" group
if db(db.auth_group.role == "manager").count() == 0:
    db.auth_group.insert(
        role='manager',
        description='Those who can edit pages...'
)

#Create a "booking_manager" group
if db(db.auth_group.role == "booking_manager").count() == 0:
    db.auth_group.insert(
        role='booking_manager',
        description='Those who can edit the booking requests...'
)

#Fixtures for mandatory content
component = db(db.page_component.name == 'photo_gallery.load').select().first()
component_description = 'Show random images of the photo gallery'
if component:
	#add component description
	if not component.description:
		component.description = component_description
		component.update_record()
else:
	db.page_component.insert(
		controller='images',
		name='photo_gallery.load',
		description=component_description,
		ajax=False,
		ajax_trap=False
	)

component = db(db.page_component.name == 'news.load').select().first()
component_description = 'Show latest news'
if component:
	#add component description
	if not component.description:
		component.description = component_description
		component.update_record()
else:
	db.page_component.insert(
		controller='news',
		name='news.load',
		description=component_description,
		ajax=False,
		ajax_trap=False
	)

component = db(db.page_component.name == 'calendar.load').select().first()
component_description = 'Allow booking requests for the page and show availability on a calendar'
if component:
	#add component description
	if not component.description:
		component.description = component_description
		component.update_record()
else:
	db.page_component.insert(
		controller='calendar',
		name='calendar.load',
		description=component_description,
		ajax=False,
		ajax_trap=False
	)

component = db(db.page_component.name == 'files.load').select().first()
component_description = 'Allow user to download files linked to the page'
if component:
	#add component description
	if not component.description:
		component.description = component_description
		component.update_record()
else:
	db.page_component.insert(
		controller='files',
		name='files.load',
		description=component_description,
		ajax=False,
		ajax_trap=False
	)

component = db(db.page_component.name == 'address.load').select().first()
component_description = 'Show the address defined in settings table'
if component:
	#add component description
	if not component.description:
		component.description = component_description
		component.update_record()
else:
	db.page_component.insert(
		controller='default',
		name='address.load',
		description=component_description,
		ajax=False,
		ajax_trap=False
	)
	#address comopnent didn't exist and was mandatory for all pages. We apply it to all existing pages at this moment
	pages=db(db.page)
	if pages:
		address_component = db(db.page_component.name == 'address.load').select().first()
		if address_component:
			pages.update(left_footer_component=address_component)	


component = db(db.page_component.name == 'newsletter.load').select().first()
component_description = 'Users can register to receive newsletter'
if component:
	#add component description
	if not component.description:
		component.description = component_description
		component.update_record()
else:
	db.page_component.insert(
		controller='default',
		name='newsletter.load',
		description=component_description,
		ajax=False,
		ajax_trap=True
	)
	#newsletter comopnent didn't exist and was mandatorw for all pages. We apply it to all existing pages at this moment
	pages=db(db.page)
	if pages:
		newsletter_component = db(db.page_component.name == 'newsletter.load').select().first()
		if newsletter_component:
			pages.update(right_footer_component=newsletter_component)


#Create the default calendar durations
if db(db.calendar_duration.id > 0).count() == 0:
	db.calendar_duration.insert(
		name = 'The morning',
		start_hour = '00:00:00',
		duration_in_minutes = 60*12-1
		)
	db.calendar_duration.insert(
		name = "The afternoon",
		start_hour = '12:00:00',
		duration_in_minutes = 60*12-1
		)
	db.calendar_duration.insert(
		name = 'The day',
		start_hour = '00:00:00',
		duration_in_minutes = 60*24-1
		)
	db.calendar_duration.insert(
		name = 'The weekend',
		start_hour = '00:00:00',
		duration_in_minutes = 60*24*2-1
		)

#Correct elements where I added default boolean fields (correct None values)
pages = db(db.page.is_index==None)
if pages:
	pages.update(is_index=False)

if WEBSITE_PARAMETERS:
	update_record = False
	if WEBSITE_PARAMETERS.with_banner==None:
		WEBSITE_PARAMETERS.with_banner=True
		update_record=True
	if WEBSITE_PARAMETERS.navbar_inverse==None:
		WEBSITE_PARAMETERS.navbar_inverse=True
		update_record=True
	if WEBSITE_PARAMETERS.max_old_news_to_show==None:
		WEBSITE_PARAMETERS.max_old_news_to_show=2
		update_record=True
	if update_record:
		WEBSITE_PARAMETERS.update_record()