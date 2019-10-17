from django.shortcuts import render
from criminal import forms

import datetime

navlinks = [("search", "Criminal Search", "/criminal/search"),
            ("info", "Criminal Info", "/criminal/info"),
            ("crimes", "Criminals Offenses", "/criminal/offense")
            ]


class CriminalView(object):
    def __init__(self, request, *args, **kw):	
        self.request = request
        self.ctx = {}
        self.session = request.session
        self.template_name = None
        self.view_name = None

    def get_nav_links(self):
        tablinks = []
        for nl in navlinks:
            tablink = {"link_text": nl[1],
                       "url": nl[2],
                       "isactive": False}
            if nl[0] == self.view_name:
                tablink["isactive"] = True
            tablinks.append(tablink)
        self.ctx["tablinks"] = tablinks


    def myrender(self, content_type="text/html",
                 status=200):
        return render(self.request, self.template_name, context=self.ctx,
                      status=status, content_type=content_type)

    def form_named(self):
        request = self.request
        if request.method == "POST" and "form_name" in request.POST:
            return request.POST["form_name"]
        return ""

    def search_view(self):
        ctx = self.ctx
        request = self.request
        self.template_name = "criminal/search.html"
        if request.method == "POST":
            pass
        else:
            ctx["search_form"] = forms.CrimeSearchForm()
        return self.myrender()

