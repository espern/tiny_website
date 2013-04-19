# coding: utf8

#Fixtures for mandatory content

if db(db.page_component.name == 'photo_gallery.load').count() == 0:
	db.page_component.insert(
		controller='images',
		name='photo_gallery.load',
		ajax=False,
		ajax_trap=False
	)
if db(db.page_component.name == 'news.load').count() == 0:
	db.page_component.insert(
		controller='news',
		name='news.load',
		ajax=False,
		ajax_trap=False
	)
if db(db.page_component.name == 'calendar.load').count() == 0:
	db.page_component.insert(
		controller='calendar',
		name='calendar.load',
		ajax=False,
		ajax_trap=False
	)
if db(db.page_component.name == 'files.load').count() == 0:
	db.page_component.insert(
		controller='files',
		name='files.load',
		ajax=False,
		ajax_trap=False
	)
if db(db.page_component.name == 'address.load').count() == 0:
	db.page_component.insert(
		controller='default',
		name='address.load',
		ajax=False,
		ajax_trap=False
	)
	#address comopnent didn't exist and was mandatory for all pages. We apply it to all existing pages at this moment
	pages=db(db.page)
	if pages:
		address_component = db(db.page_component.name == 'address.load').select().first()
		if address_component:
			pages.update(left_footer_component=address_component)	

if db(db.page_component.name == 'newsletter.load').count() == 0:
	db.page_component.insert(
		controller='default',
		name='newsletter.load',
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