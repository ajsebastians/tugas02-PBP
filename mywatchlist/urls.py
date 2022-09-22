from django.urls import path
from mywatchlist.views import show_Movies
from mywatchlist.views import show_xml, show_json, show_json_by_id, show_xml_by_id
app_name = 'mywatchlist'

urlpatterns = [
    path('', show_Movies, name='show_mywatchlist'),
    path('html/', show_Movies, name='show_mywatchlist'),
    path('xml/', show_xml, name='watchlist_xml'),
    path('json/', show_json, name='watchlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_jason_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]