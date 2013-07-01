from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class MyApp(CMSApp):
    name = _("My App") # give your app a name, this is required
    urls = ["myapp.urls"] # link your app to url configuration(s)

apphook_pool.register(MyApp) # register your app
