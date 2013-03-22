def files_list():
    """
    Allows to access the "files" component
    """
    def sizeof_file(num):
        for x in [T('bytes'),T('KB'),T('MB'),T('GB')]:
            if num < 1024.0 and num > -1024.0:
                return "%3.1f%s" % (num, x)
            num /= 1024.0
        return "%3.1f%s" % (num, T('TB'))

    manager_toolbar = ManagerToolbar('file')
    files = db(db.file).select()
    return dict(files=files,
                sizeof_file=sizeof_file,
                left_sidebar_enabled=True,
                right_sidebar_enabled=True,
                manager_toolbar=manager_toolbar)

@auth.requires_membership('manager')
def edit_file():
    a_file = db.file(request.args(0))
    crud.settings.update_deletable=False
    if len(request.args) and a_file:
        crud.settings.update_deletable = False
        form = crud.update(db.file,a_file,next='files_list')
    else:
        form = crud.create(db.file)
    return dict(a_file=a_file, form=form)


@auth.requires_membership('manager')
def delete_file():
    a_file = db.file(request.args(0))
    if len(request.args) and a_file:  
        form = FORM.confirm(T('Yes, I really want to delete this file'),{T('Back'):URL('files_list')})
        if form.accepted:
            #remove the file
            db(db.file.id==a_file.id).delete()
            session.flash = T('File deleted')
            redirect(URL('files_list'))
    return dict(a_file=a_file, form=form)