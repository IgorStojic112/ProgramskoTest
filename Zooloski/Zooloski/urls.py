from django.urls import path
from . import views
#URL konfiguracija

urlpatterns = [
    path('', views.pocetna, name='pocetna'),
    path('nastambe/', views.nastamba_list, name='nastamba_list'),  # Prikaz svih nastambi
    path('nastambe/<int:id>/', views.nastamba_detail, name='nastamba_detail'),  # Detaljan prikaz nastambe
    path('nastambe/dodaj/', views.nastamba_create, name='nastamba_create'),  # Kreiranje nove nastambe
    path('nastambe/<int:id>/uredi/', views.nastamba_update, name='nastamba_update'),  # Uređivanje nastambe
    path('nastambe/<int:id>/arhiviraj/', views.nastamba_archive, name='nastamba_archive'),  # Arhiviranje nastambe (soft delete)
    path('report/zivotinje',views.report_zivotinje,name='report_zivotinje') # Izvjestaj troskova zivotinja
]
