from django.urls import path

import users_app.views


urlpatterns = [
    path('my_account/', users_app.views.user_account, name='user_account'),
    path('<order_id>/give_back', users_app.views.give_back, name='give_back'),

]
