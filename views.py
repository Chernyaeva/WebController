from framework.renderer import render

class NotFound:
    def __call__(self, request):
        return '404 WHAT', render('PageNotFound.html')

class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))

class About:
    def __call__(self, request):
        return '200 OK', render('about.html')

