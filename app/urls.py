
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donor_register', views.donor_register, name='donor_register'),
    path('trust_register', views.trust_register, name='trust_register'),
    path('log_in', views.log_in, name='log_in'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('user_transactions', views.user_transactions, name='user_transactions'),
    path('trust_dashboard', views.trust_dashboard, name='trust_dashboard'),
    path('utilize_donation', views.utilize_donation, name='utilize_donation'),
    path('show_utilization', views.show_utilization, name='show_utilization'),
    path('show_donation', views.show_donation, name='show_donation'),
    path('donation', views.donation, name='donation'),
    path('trust_send_money', views.trust_send_money, name='trust_send_money'),
    path('receive_transactions', views.receive_transactions, name='receive_transactions'),
    path('view', views.view, name='view'),
    path('log_out', views.log_out, name='log_out'),

    path('super_admin_dashboard', views.super_admin_dashboard, name='super_admin_dashboard'),
    path(
    "super_admin_transactions",
    views.super_admin_transactions,
    name="super_admin_transactions"),

    path(
    "approve_utilization/<int:utilization_id>/",
    views.approve_utilization,
    name="approve_utilization"),

    path(
    "reject_utilization/<int:utilization_id>/",
    views.reject_utilization,
    name="reject_utilization"),
]
