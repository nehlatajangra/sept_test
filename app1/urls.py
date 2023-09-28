from django.urls import path
from . import views
from rest_framework  import routers
router=routers.DefaultRouter()
router.register('person',views.PersonViewset,basename='person')

urlpatterns = [
    path('',views.index,name='index' ),
    path('crud/',views.crud,name='crud'),
    path('template/',views.templatePage,name='template'),
    path('query/',views.QueryPage,name="query"),
    path('accordian/',views.accordianPage,name="accordian"),
    path('multistepform/',views.multistepForm,name='multistepform')
]
urlpatterns+=router.urls