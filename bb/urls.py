from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all-donor', views.all_donor, name="all-donor"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('user-add', views.user_add, name="user-add"),
    path('user-view', views.user_view, name="user-view"),
    path('birthday', views.birthday, name="birthday"),
    path('regular-donor', views.regular_donor, name="regular-donor"),
    path('due-date', views.due_date, name="due-date"),

# search urls
    path('search-address', views.search_address, name="search-address"),
    path('search-blood', views.search_blood, name="search-blood"),
    path('search-blood-rate-month', views.search_blood_rate_month, name="search-blood-rate-month"),
    path('search-blood-rate-year', views.search_blood_rate_year, name="search-blood-rate-year"),

# view urls
    path('stock-increase', views.stock_increase, name="stock-increase"),
    path('send-email', views.send_email, name="send-email"),
    path('stock-decrease', views.stock_decrease, name="stock-decrease"),
    path('donor-details/<int:id>', views.donor_details, name="donor-details"),
    path('donate/<int:id>', views.donate, name="donate"),
    path('reset/<int:id>', views.reset, name="reset"),

# updating urls
    path('try-sending-email/<int:id>', views.try_sending_email, name="try-sending-email"),
    path('bock-sending-email', views.bock_sending_email, name="bock-sending-email"),
    path('try-updating-donor/<int:id>', views.try_updating_donor, name="try-updating-donor"),
    path('update-donor/<int:id>', views.update_donor, name="update-donor"),
    path('try-updating-blood-group/<int:id>', views.try_updating_blood_group, name="try-updating-blood-group"),
    path('update-blood-group/<int:id>', views.update_blood_group, name="update-blood-group"),

# deleting urls
    path('delete-donor/<int:id>', views.delete_donor, name="delete-donor"),
    path('request-for-delete-donor/<int:id>', views.request_for_delete_donor, name="request-for-delete-donor"),
    path('delete-blood/<int:id>', views.delete_blood, name="delete-blood"),
    path('request-for-delete-blood/<int:id>', views.request_for_delete_blood, name="request-for-delete-blood"),
    path('delete-user/<int:id>', views.delete_user, name="delete-user"),
    path('request-for-delete-user/<int:id>', views.request_for_delete_user, name="request-for-delete-user"),
]