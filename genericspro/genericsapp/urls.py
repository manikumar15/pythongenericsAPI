from django.conf.urls import url

# from .views import GenericView_List,GenericView_Details
from genericsapp import views

urlpatterns = [
	url(r'^emp/$',views.GenericView_List.as_view()),
	url(r'^emp/(?P<pk>[0-9]+)',views.GenericView_Details.as_view()),

]