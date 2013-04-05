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