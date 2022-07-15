from views import index, create_news, get_all_news, get_one_news, update_news, delete_news


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/create', create_news, name='create_news')
    app.router.add_get('/get', get_all_news, name='get_news')
    app.router.add_get('/get/{id}', get_one_news, name='get_one_news')
    app.router.add_post('/update/{id}', update_news, name='update_news')
    app.router.add_post('/delete/{id}', delete_news, name='delete_news')