from django.shortcuts import render

import datetime

class CriminalView(object):
    def __init__(self, request, *args, **kw):	
        self.request = request
        self.ctx = {}
        self.session = request.session

    def myrender(self, template_name,content_type="text/html",
                 status=200):
        return render(self.request, template_name, context=self.ctx,
                      status=status, content_type=content_type)
    def search_view(self):
        template_file = "criminal/search.html"
        self.ctx["content"] = "Test content"
        return self.myrender(template_file)

