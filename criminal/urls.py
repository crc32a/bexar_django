from django.urls import path
from criminal.views import CriminalView

# Create a new view object every time to avoid everyone sharing every request
# sharing a singleton
def gview(request, *args, **kw):
    view_name = kw.pop("view")
    cv = CriminalView(request)
    cv.view_name = view_name
    cv.get_nav_links()
    func = getattr(cv, view_name + "_view")
    return func(*args, **kw)

urlpatterns = [ path('search/', gview,{"view":"search"}, name="search"),
                path('sid/<int:sid>/', gview, {"view":"sid"}, name="sid"),
                path('crime/<int:crime_id>/', gview,{"view":"crime"},
                     name="crime")
]










