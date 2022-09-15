from django.test import TestCase

# Create your tests here.
from katalog.models import CatalogItem

# Create your tests here.
class Test_Run(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name = "MacBook Air M2",
            item_price = 17199000,
            item_stock = 1,
            description = "Ready Stock",
            rating = 5,
            item_url = "https://www.tokopedia.com/tokohapedia/apple-macbook-air-m2-chip-2022-13-256gb-512gb-midnight-silver-japan-set-256-silver?extParam=ivf%3Dfalse&src=topads")
        
        CatalogItem.objects.create(
            item_name = "AirTag",
            item_price = 489000,
            item_stock = 2,
            description = "Penyelamat benda hilang",
            rating = 5,
            item_url = "https://www.tokopedia.com/armyapple/apple-airtag-2021-original-1-4-pack-for-iphone-airtags-air-tag-tags-lose-pack?extParam=ivf%3Dfalse&src=topads")
        )
    
    def test(self):
        satu = CatalogItem.objects.get(item_name = "MacBook Air M2")
        dua = CatalogItem.objects.get(item_name = "AirTag")
        self.assertIn("Kacamata", satu.item_name)
        self.assertIn("AirTag", dua.item_name)
