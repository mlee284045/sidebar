from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import serializers, viewsets, routers
from sidebar import settings
from slides.models import Slide, Resource, Person


class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slide
        fields = ('pres_title', 'slide_title', 'url', 'text', 'content')


class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer

router = routers.DefaultRouter()
router.register(r'slides', SlideViewSet)



# class ResourceSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Resource
#         fields = ('creator', 'date', 'text', 'slide')
#
#
# class ResourceViewSet(viewsets.ModelViewSet):
#     queryset = Resource.objects.all()
#     serializer_class = ResourceSerializer
#
# router = routers.DefaultRouter()
# router.register(r'resources', ResourceViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'slides.views.slides_home', name='slides_home'),
    url("^index/$", 'slides.views.index', name="index"),
    url("^search_page/$", 'slides.views.search_page', name="search_page"),
    url("^search_results/$", 'slides.views.search_results', name="search_results"),
    url("^edit_account/$", 'slides.views.edit_account', name="edit_account"),
    url(r"^update_account/$", 'slides.views.update_account', name="update_account"),
    url("^add_resource/$", 'slides.views.add_resource', name="add_resource"),
    url("^save_resource/$", 'slides.views.save_resource', name="save_resource"),
    # url("^get_slide_info/Welcome!/$", 'slides.views.get_slide_info', name="get_slide_info"),
    url("^get_slide_info/$", 'slides.views.get_slide_info', name="get_slide_info"),
    url("^get_resource_info/$", 'slides.views.get_resource_info', name="get_resource_info"),
    url("^sidebar/$", 'slides.views.sidebar', name="sidebar"),


    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),


    # Week 1 - OO Python
    url("^week1/$", TemplateView.as_view(template_name="week1/0.html"), name="week1"),
    url("^week1/1/$", TemplateView.as_view(template_name="week1/1.html"), name="week1_day1"),
    url("^week1/2/$", TemplateView.as_view(template_name="week1/2.html"), name="week1_day2"),
    url("^week1/3/$", TemplateView.as_view(template_name="week1/3.html"), name="week1_day3"),
    url("^week1/4_am/$", TemplateView.as_view(template_name="week1/4_am.html"), name="week1_day4_am"),
    url("^week1/4_pm/$", TemplateView.as_view(template_name="week1/4_pm.html"), name="week1_day4_pm"),

    # Week 2 - DB Intro + Introductory Django
    url("^week2/$", TemplateView.as_view(template_name="week2/0.html"), name="week2"),
    url("^week2/1_am/$", TemplateView.as_view(template_name="week2/1_am.html"), name="week2_day1_am"),
    url("^week2/1_pm/$", TemplateView.as_view(template_name="week2/1_pm.html"), name="week2_day1_pm"),
    url("^week2/2_am/$", TemplateView.as_view(template_name="week2/2_am.html"), name="week2_day2_am"),
    url("^week2/2_pm/$", TemplateView.as_view(template_name="week2/2_pm.html"), name="week2_day2_pm"),
    url("^week2/3_am/$", TemplateView.as_view(template_name="week2/3_am.html"), name="week2_day3_am"),
    url("^week2/3_pm/$", TemplateView.as_view(template_name="week2/3_pm.html"), name="week2_day3_pm"),
    url("^week2/4_am/$", TemplateView.as_view(template_name="week2/4_am.html"), name="week2_day4_am"),
    url("^week2/4_pm/$", TemplateView.as_view(template_name="week2/4_pm.html"), name="week2_day4_pm"),
    url("^week2/5_am/$", TemplateView.as_view(template_name="week2/5_am.html"), name="week2_day5_am"),
    url("^week2/5_pm/$", TemplateView.as_view(template_name="week2/5_pm.html"), name="week2_day5_pm"),

    # Start Project Cheatsheet
    url("^start_project_cheatsheet/$", TemplateView.as_view(template_name="start_project.html"), name="start_project"),

    # Week 3 - Introductory Django
    url("^week3/$", TemplateView.as_view(template_name="week3/0.html"), name="week3"),
    url("^week3/1_am/$", TemplateView.as_view(template_name="week3/1_am.html"), name="week3_day1_am"),
    url("^week3/1_pm/$", TemplateView.as_view(template_name="week3/1_pm.html"), name="week3_day1_pm"),
    url("^week3/2_am/$", TemplateView.as_view(template_name="week3/2_am.html"), name="week3_day2_am"),
    url("^week3/2_pm/$", TemplateView.as_view(template_name="week3/2_pm.html"), name="week3_day2_pm"),
    url("^week3/3_am/$", TemplateView.as_view(template_name="week3/3_am.html"), name="week3_day3_am"),
    url("^week3/3_pm/$", TemplateView.as_view(template_name="week3/3_pm.html"), name="week3_day3_pm"),
    url("^week3/lab/$", TemplateView.as_view(template_name="week3/lab.html"), name="week3_lab"),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()