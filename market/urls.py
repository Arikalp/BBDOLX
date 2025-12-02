from django.urls import path
from . import views

urlpatterns = [
    # ---------- PUBLIC PAGES ----------
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),

    # ---------- PRODUCTS (USER) ----------
    path('product/add/', views.product_create, name='product_add'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_update, name='product_edit'),
    path('product/<int:pk>/sold/', views.mark_as_sold, name='product_sold'),

    # ---------- SELLER DASHBOARD ----------
    path('my-listings/', views.my_listings, name='my_listings'),

    # ---------- MODERATION (ADMIN / STAFF ONLY) ----------
    # main dashboard
    path('moderation/', views.moderation_dashboard, name='moderation_dashboard'),

    # optional older "pending only" view (you can remove if not using)
    path('moderation/pending/', views.pending_products, name='pending_products'),

    # actions
    path('moderation/approve/<int:pk>/', views.approve_product, name='approve_product'),
    path('moderation/reject/<int:pk>/', views.reject_product, name='reject_product'),
    path('moderation/<int:pk>/delete/', views.delete_product, name='delete_product'),

    # ---------- NOTIFICATIONS ----------
    path('notif/read/<int:pk>/', views.mark_notification_read, name='mark_notification_read'),
]
