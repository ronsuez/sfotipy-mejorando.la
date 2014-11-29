from django.test import TestCase

# Create your tests here.

from .models import Artist


class TestArtist(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(first_name="Jhon", last_name="Doe")

    def view_exists_test(self):
        res = self.client.get('/artist/%d/' % self.artist.id)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('Jhon' in res.content)

    def view_not_exists_test(self):
        old_id = self.artist.id
        self.artist.delete()
        res = self.client.get('/artist/%d/' % old_id)
        self.assertEqual(res.status_code, 404)