from django.test import TestCase
from .models import Post, Author
from django.urls import reverse
# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(title="This is a test")

    def test_model_content(self):
        self.assertEqual(self.post.title, "This is a test")
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'home.html')
    def test_tempate_content(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, 'This is a test')
