from django.contrib import admin
from django.urls import path
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import debug_toolbar
from.url_base import get_url_patterns as get_url_patterns_base
from.url_spartaqube import get_url_patterns as get_url_patterns_spartaqube
handler404='project.sparta_fe3ca028a6.sparta_25f7a4bd64.qube_180bbf8648.sparta_ad52089d23'
handler500='project.sparta_fe3ca028a6.sparta_25f7a4bd64.qube_180bbf8648.sparta_5a5250df9a'
handler403='project.sparta_fe3ca028a6.sparta_25f7a4bd64.qube_180bbf8648.sparta_8b75663556'
handler400='project.sparta_fe3ca028a6.sparta_25f7a4bd64.qube_180bbf8648.sparta_dd9efa4d6b'
urlpatterns=get_url_patterns_base()+get_url_patterns_spartaqube()
if settings.B_TOOLBAR:urlpatterns+=[path('__debug__/',include(debug_toolbar.urls))]