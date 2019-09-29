from django.urls import path
from criminal.views import CriminalView

# Create a new view object every time to avoid everyone sharing every request
# sharing a singleton
def gview(request, *args, **kw):
    cv = CriminalView(request, *args, **kw)
    func = getattr(cv, kw["view"] + "_view")
    return func()    

urlpatterns = [ path('search/', gview,{"view":"search"}, name="search"),
]










