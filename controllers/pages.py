#from gluon.debug import dbg

def show_page():
    """
        Show the requested page
    """
    manager_toolbar = ManagerToolbar('page')
    if request.args(0).isdigit():
        page = db.page(request.args(0))
    else:
        page = db(db.page.url==request.args(0)).select().first()
     
    # if page:    #set the "active" page in menu
    #     for index, menu in enumerate(response.menu):
    #         if menu[0]==page.title:
    #             is_enabled=True
    #         else:
    #             is_enabled=False
    #         response.menu[index]=menu[:1]+(is_enabled,)+menu[2:]
    # else:
    if not page:
        if request.args(0).lower() == 'images':
            redirect(URL('images'))
        else:
            page = db(db.page.is_index==True).select().first()

    left_sidebar_component = db.page_component(page.left_sidebar_component)
    right_sidebar_component = db.page_component(page.right_sidebar_component)
    return dict(page=page,
                left_sidebar_enabled=page.left_sidebar_enabled,
                right_sidebar_enabled=page.right_sidebar_enabled,
                left_sidebar_component=left_sidebar_component,
                right_sidebar_component=right_sidebar_component,
                manager_toolbar=manager_toolbar)

@auth.requires_membership('manager')
def delete_page():
    if request.args(0).isdigit():
        page = db.page(request.args(0))
    else:
        page = db(db.page.url==request.args(0)).select().first()
    if len(request.args) and page:  
        form = FORM.confirm(T('Yes, I really want to delete this page'),{T('Back'):URL('show_page', args=page.id)})
        if form.accepted:
            #remove images linked to the page
            pathname = os.path.join(request.folder,'static','images', 'pages_content', str(form.vars.id))
            if os.path.exists(pathname):
                shutil.rmtree(pathname)
            #remove the page
            db(db.page.id==page.id).delete()
            session.flash = T('Page deleted')
            redirect(URL('default', 'index'))
    return dict(page=page, form=form)

@auth.requires_membership('manager')
def edit_page():
    """
    """
    page_id = request.args(0)
    if page_id:
        if page_id.isdigit():
            page = db.page(page_id)
        else:
            page = db(db.page.url==page_id).select().first()
    if len(request.args) and page:  
        crud.settings.update_deletable = False
        form = crud.update(db.page,page,next=URL('show_page', args=page.id))
    else:
        #Hide the "content" of the page : the page has no title
        #and this is impossible to initialise the upload field with page.url
        db.page.content.readable = db.page.content.writable = False
        form = crud.create(db.page,next='edit_page/[id]')
    return dict(form=form)
