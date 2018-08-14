from django.urls import path

import accounts_app.views


urlpatterns = [
    path('signup', accounts_app.views.signup, name='signup'),
    path('login', accounts_app.views.login, name='login'),
    path('logout', accounts_app.views.logout, name='logout'),

    ]
