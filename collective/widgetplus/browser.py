from zope.publisher.browser import BrowserView
from zope.security.proxy import removeSecurityProxy


class WidgetView(BrowserView):

    def __init__(self,context,request):
        self.context = context
        self.request = request

    def __call__(self):
        self.request.response.setHeader('Content-Type','text/html')
        return removeSecurityProxy(self.context)()
