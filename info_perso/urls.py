from django.urls import path
from . import views


urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('theme1', views.theme1, name='theme1'),
    path('theme2', views.theme2, name='theme2'),
    path('theme3', views.theme3, name='theme3'),
    path('theme4', views.theme4, name='theme4'),
    path('theme5', views.theme5, name='theme5'),
    path('theme6', views.theme6, name='theme6'),
    path('info_perso', views.info_perso, name='info_perso'),
    path('profile_info', views.profile_info, name='profile_info'),
    path('formation_info',views.formation_info,name='formation_info'),
    path('experience_info',views.experience_info,name='experience_info'),
    path('competence_info',views.competence_info,name='competence_info'),
    path("langue_info", views.langue_info, name="langue_info"),
    path('centre_interet_info',views.centre_interet_info,name='centre_interet_info'),
    path('upload_image', views.upload_image, name='upload_image'),
    #path('b', views.b, name='b'),
    path('s', views.s, name='s'),

    path('cv', views.cv, name='cv'),
]