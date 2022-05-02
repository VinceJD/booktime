from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestPage(TestCase):
    def test_home_page_works(self):
        reponse = self.client.get("/")
        self.assertEqual(reponse.status_code, 200)
        self.assertTemplateUsed(reponse, 'pages/home.html')
        self.assertContains(reponse, 'Booktime')
    
    def test_about_us_works(self):
        reponse = self.client.get("/about_us/")
        self.assertEqual(reponse.status_code, 200)
        self.assertTemplateUsed(reponse, 'pages/aboutus.html')
        self.assertContains(reponse, 'Booktime')

