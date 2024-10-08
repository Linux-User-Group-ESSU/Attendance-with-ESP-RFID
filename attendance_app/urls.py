from django.urls import path

from . import views


urlpatterns = [
    path('upload/',views.upload_file, name='upload_file'),
    path('logout/',views.logout_view, name='logout'),
    path("api/",views.api_attendance, name='api_attendance'),
    path("control_panel/",views.control_panel, name='control_panel'),
    path("dashboard/",views.dashboard, name='dashboard'),
    path('students/',views.students, name='students'),
    path('delete_device/<int:device_id>/',views.delete_device, name='delete_device'),
    path('student_attendance/<int:student_id>/',views.student_attendance, name='student_attendance'),
    path('delete_student/<int:student_id>/',views.delete_student, name='delete_student'),
    path('date_attendance/',views.date_attendance, name='date_attendance'),
    path('add_student/',views.add_student, name='add_student'),
    path("events/",views.events, name='events'),
    path("add_event/",views.add_event, name='add_event'),
    path("event/<int:event_id>/",views.event, name='event'),
    path("devices/",views.devices, name='devices'),
    path("attendance_for_today/<int:day_id>/",views.attendance_for_today, name="attendance_for_today"),
    path("add_day/<int:event_id>/",views.add_day, name='add_day'),
    path("add_device/",views.add_device, name='add_device'),
    path("",views.index, name='index')
]