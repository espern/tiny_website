def news():
    """
    Allows to access the "news" component

    :request.vars.container_id: id of the "containing" page
        (i.e the id of the page which contains the calendar)
    :type container_id: int.
    """

    # Create a Manager toolbar to Create/Update/Delete the files. See db.py model
    # for more informations on ManagerToolbar class
    manager_toolbar = ManagerToolbar('news')

    rows = db(db.news).select(orderby=~db.news.date|~db.news.published_on)

    # Select all the news more recent than the current date
    newsS = [row for row in rows.find(lambda row: row.date >= request.now.date())]

    # how many old news (date < current date) should we show?
    max_news = WEBSITE_PARAMETERS.max_old_news_to_show if WEBSITE_PARAMETERS.max_old_news_to_show is not None else 0

    # add old news (date < current date)
    newsS += [row for row in rows.find(lambda row: row.date < request.now.date())[:max_news]]
    return dict(newsS=newsS,
                manager_toolbar=manager_toolbar)

@auth.requires(auth.has_membership('manager') or auth.has_membership('news_manager'))
def edit_news():
    """
    Edit a news

    :request.args(0): id of the news
    :type request.args(0): int.
    """
    news = db.news(request.args(0))
    crud.settings.update_deletable=False
    if len(request.args) and news:
        form = crud.update(db.news,news,next=URL('default','index'))
    else:
        form = crud.create(db.news,URL('default','index'))
    return dict(news=news, form=form)

@auth.requires(auth.has_membership('manager') or auth.has_membership('news_manager'))
def delete_news():
    """
    Delete a news

    :request.args(0): id of the news
    :type request.args(0): int.
    """
    news = db.news(request.args(0))
    if len(request.args) and news:  
        form = FORM.confirm(T('Yes, I really want to delete this news'),{T('Back'):URL('index')})
        if form.accepted:
            # remove from the DB
            db(db.news.id==news.id).delete()
            session.flash = T('News deleted')
            redirect(URL('default', 'index'))
    return dict(news=news, form=form)


def newsletter_unsubscribe():
    """
    Manually unsubscribe a user from the newsletter.
    This controller can be accessed from a link added in the emails sent to the users.
    See news_mail_send() function in "scheduler.py" model

    :request.vars.email: email to unsubscribe
    :type request.vars.email: str.
    """
    if request.vars.email:
        q = db.registered_user.email==request.vars.email
        user = db(q).select()
        if user:
            db(q).update(subscribe_to_newsletter=False)
            return dict(text=T("You have been successfully unsubscribed from the newsletter. You won't receive any email anymore."))
    return dict(text=T("This email is not recognized. We cannot unsubscribe you."))


def rss_news():
    """
    Show the latest news in RSS format
    """
    from controllers_tools import strip_accents
    
    newsS = db(db.news).select(orderby=~db.news.date|~db.news.published_on)
    return dict(title=strip_accents(T('%s latest news',WEBSITE_PARAMETERS.website_name)),
                link=WEBSITE_PARAMETERS.website_url if WEBSITE_PARAMETERS.website_url else '',
                description=strip_accents(T('%s latest news',WEBSITE_PARAMETERS.website_name)),
                entries=[
                  dict(title=strip_accents(news.title),
                  link=WEBSITE_PARAMETERS.website_url if WEBSITE_PARAMETERS.website_url else '',
                  created_on = news.published_on,
                  description=strip_accents(news.text)) for news in newsS
                ])