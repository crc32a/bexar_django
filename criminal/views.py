from django.shortcuts import render
from criminal import forms, models

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
        if self.form_named() == "CrimeSearchForm":
            form = forms.CrimeSearchForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data # search criminals
                qs = models.Criminal.objects
                if "First Name" in data["search_by_field"]:
                    fn = data["first_name"]
                    if fn:
                        qs = qs.filter(full_name__icontains = fn)
                if "Last Name" in data["search_by_field"]:
                    ln = data["last_name"]
                    if ln:
                        qs = qs.filter(full_name__icontains = ln)
                if "Birth data" in data["search_by_field"]:
                    bd = data["birthdate"]
                    if bd:
                        qs = qs.filter(birthdata = bd)
                if "SID number" in data["search_by_field"]:
                    sid = data["sid"]
                    if sid and sid > 0:
                        qs = qs.filter(sid = sid)
                criminals = qs.order_by("birthdate").all()
                n = len(criminals)
                ctx["n_criminals"] = n
                if n >= 1:
                    ctx["criminals"] = []
                    for c in criminals:
                        criminal = {}
                        criminal["full_name"] = c.full_name
                        criminal["sex"] = c.sex
                        criminal["birthdate"] = c.birthdate
                        criminal["sid"] = c.sid
                        ctx["criminals"].append(criminal)

        else:
            form = forms.CrimeSearchForm()
        ctx["search_form"] = form
        return self.myrender()

