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

#Create a default user
if db(db.auth_user.email == "user@test.com").count() == 0:
    db.auth_user.insert(
        first_name='user',
        last_name='name',
		username='user',
        email='user@test.com',
        password=db.auth_user.password.validate('pass')[0]
)

#assign the default user to the manager group
manager_group = db(db.auth_group.role == "manager").select().first()
if manager_group:
	default_user = db(db.auth_user.email == "user@test.com").select().first()
	if default_user:
		if db(db.auth_membership.user_id == default_user.id)(db.auth_membership.group_id == manager_group.id).count() == 0:
			db.auth_membership.insert(
					user_id=default_user.id,
					group_id=manager_group.id
				)

if db(db.page_component.id > 0).count() == 0:
	db.page_component.insert(
		controller='images',
		name='photo_gallery.load',
		ajax=False,
		ajax_trap=False
	)
	db.page_component.insert(
		controller='news',
		name='news.load',
		ajax=False,
		ajax_trap=False
	)
	db.page_component.insert(
		controller='calendar',
		name='calendar.load',
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

#create a default index page if not exists
tmpContent = """
<p>
	This is the first page of your website
</p>
<p>
	You can connect using the following credentials to create / update / delete pages content. <br />
	Username : <strong>user</strong><br />
	Password : <strong>pass</strong><br />
</p>
<p>
	Once connected, try to add images in the photo gallery (<em>need to have python PIL installed</em>)
</p
<p>
	You can edit the website parameters in models/db_menu.py
</p>
"""
if db(db.page.is_index == True).count() == 0:
	news_component = db(db.page_component.name == 'news.load').select().first()
	gallery_component = db(db.page_component.name == 'photo_gallery.load').select().first()
	db.page.insert(
        title='Index',
        subtitle='The index page',
        url='index',
        content=tmpContent,
        is_index=True,
        left_sidebar_enabled=True,
        right_sidebar_enabled=True,
        left_sidebar_component=gallery_component,
        right_sidebar_component=news_component
    )

#create a default "root page"
if db(db.page.title == 'What about this website?').count() == 0:
    db.page.insert(
        title='What about this website?',
        subtitle='',
        content='',
        is_index=False,
        left_sidebar_enabled=False,
        right_sidebar_enabled=False
    )
root_page = db(db.page.title == 'What about this website?').select().first()

#create the first children page
if db(db.page.title == 'This website is cool!').count() == 0:
    db.page.insert(
    	parent=root_page,
        title='This website is cool!',
        subtitle='... as me',
        content='Try to change this content...',
        rank=1,
        is_index=False,
        left_sidebar_enabled=True,
        right_sidebar_enabled=True
    )

#create the second children page
if db(db.page.title == '... and easy to update').count() == 0:
    db.page.insert(
    	parent=root_page,
        title='... and easy to update',
        subtitle='You will fall in love with it',
        content='Try to change this content...',
        rank=2,
        is_index=False,
        left_sidebar_enabled=True,
        right_sidebar_enabled=True
    )

#create a news
if db(db.news).count() == 0:
	db.news.insert(
		title='First news published!',
		date=request.now,
		text='This is your first news',
		published_on=request.now
		)

#add default images
if db(db.image.name == "demo1").count() == 0:
	db.image.insert(
	    name='demo1',
	    alt='demo1',
	    comment='my first image',
	    file='demo1.jpg',
	    thumb='demo1.jpg',
	    show_in_gallery=True
	)
if db(db.image.name == "demo2").count() == 0:
	db.image.insert(
	    name='demo2',
	    alt='demo2',
	    comment='my first image',
	    file='demo2.jpg',
	    thumb='demo2.jpg',
	    show_in_gallery=True
	)
if db(db.image.name == "demo3").count() == 0:
	db.image.insert(
	    name='demo3',
	    alt='demo3',
	    comment='my first image',
	    file='demo3.jpg',
	    thumb='demo3.jpg',
	    show_in_gallery=True
	)
if db(db.image.name == "demo4").count() == 0:
	db.image.insert(
	    name='demo4',
	    alt='demo4',
	    comment='my first image',
	    file='demo4.jpg',
	    thumb='demo4.jpg',
	    show_in_gallery=True
	)
if db(db.image.name == "demo5").count() == 0:
	db.image.insert(
	    name='demo5',
	    alt='demo5',
	    comment='my first image',
	    file='demo5.jpg',
	    thumb='demo5.jpg',
	    show_in_gallery=True
	)
if db(db.image.name == "demo6").count() == 0:
	db.image.insert(
	    name='demo6',
	    alt='demo6',
	    comment='my first image',
	    file='demo6.jpg',
	    thumb='demo6.jpg',
	    show_in_gallery=True
	)

#Add a file to download
if db(db.file.title == "web2py manual 5th").count() == 0:
	db.file.insert(
	    title='web2py manual 5th',
	    comment='A really great web framework!',
	    file='demo.pdf'
	)
