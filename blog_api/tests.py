from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Category, Post
from users.models import NewUser

class PostTests(APITestCase):

    def test_view_post(self):

        url = reverse('api-v1:blog_api:list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):

        self.test_category = Category.objects.create(name='django')
        self.testuser1 = NewUser.objects.create_user(user_name='test_user1', email='test@test.com', first_name='test1', password='123456789')

        self.client.login(user_name=self.testuser1.user_name, password='123456789')

        data = {
            "title": "new", 
            "author": 1,
            "excerpt": "new", 
            "content": "new",
            "slug": ""
        }

        url = reverse('api-v1:blog_api:list-create')
        response = self.client.post(url, data, format='json')
        # print(response)
        # Need to login first before test create
        # - this is currently return failure since not authenticated cannot create new post
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(len(response.data), 6)
        root = reverse(('api-v1:blog_api:detail-create'), kwargs={'pk': 1})
        response = self.client.get(root, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')
        # self.testuser1 = NewUser.objects.create_user(user_name='test_user1', password='123456789')
        self.testuser1 = NewUser.objects.create_user(user_name='test_user1', email='test@test.com', first_name='test1', password='123456789')
        # self.testuser2 = NewUser.objects.create_user(user_name='test_user2', password='123456789')
        self.testuser2 = NewUser.objects.create_user(user_name='test_user2', email='test2@test.com', first_name='test2', password='123456789')

        testpost = Post.objects.create(
            category_id=1, title='Post Title', excerpt='post excerpt', content='post content', 
            slug='post-title', author_id=1, status='published'
        )

        client.login(username=self.testuser1.username, password='123456789')

        url = reverse(('api-v1:blog_api:detail-create'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "id": 1,
                "title": "Post 1 Update",
                "author": 1,
                "excerpt": "Testing post 1",
                "content": "Testing post 1",
                "status": "published"
            },
            format='json'
        )

        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)