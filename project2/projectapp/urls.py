from django.urls import path


from projectapp import views

urlpatterns=[
    path('',views.first,name='first'),
    path('student_sign',views.student_sign,name='student_sign'),
    path('admin_sign',views.admin_sign,name='admin_sign'),

    path('studpage',views.studpage,name='studpage'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('log',views.log,name='log'),
    path('studentview',views.studentview,name='studentview'),
    path('add_mark',views.add_mark,name='add_mark'),
    path('view_mark',views.view_mark,name='view_mark'),
    path('view_mark_stud',views.view_mark_stud,name='view_mark_stud'),
    path('stud_profile_view',views.stud_profile_view,name='stud_profile_view'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
    path('logout_stud',views.logout_stud,name='logout_stud'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
    path('mark_update/<int:id>/',views.mark_update, name='mark_update'),
    path('mark_delete/<int:id>/',views.mark_delete, name='mark_delete'),

]