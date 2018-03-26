from django.conf.urls import url
from readandpick.views import book_list, book_details  # , book_create, book_edit

urlpatterns = [
    url(r'^books/$', book_list, name='readandpick_book_list'),
    url(r'^books/(?P<id>\d+)/$', book_details, name='readandpick_book_details'),
]
