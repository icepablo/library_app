from django.urls import path

import authors_app.views


urlpatterns = [
    path('', authors_app.views.authors, name='authors'),
    path('<int:author_id>/', authors_app.views.author_detail, name='author_detail'),

]
