from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class BlogsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Mohammad',
            email='Mohammad@gmail.com',
            password='0000'
        )

        self.snack = Post.objects.create(
            title='mansaf',
            author=self.user,
            body='jameed karaky'
        )

    def test_snack_list_view(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('blog_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_update_view(self):
        response = self.client.post(reverse('update_blog', args='1'), {
            'title': '3adas',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '3adas')

    def test_create_view(self):
        response = self.client.post(reverse('create_blog'), {
            'title': 'knafeh',
            'author': self.user,
            'body' :'ga6or',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'knafeh')
        self.assertContains(response, 'ga6or')
        self.assertContains(response, 'Mohammad')

    def test_delete_view(self):
        response = self.client.get(reverse('delete_blog',args='1'))
        self.assertEqual(response.status_code, 200)