from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Category, Post, PhotoGallery
from users.models import NewUser

class Test_Create_Post(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = NewUser.objects.create_user(email='test@test.com', user_name='test_user1', first_name='test1', password='123456789')
        testphotogallery = PhotoGallery.objects.create(id=1)
        testpost = Post.objects.create(
            category_id=1, 
            title='Post Title', 
            excerpt='post excerpt', 
            content='post content', 
            slug='post-title', 
            author_id=1,
            photos_id=1, 
            status='published'
        )

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        slug = f'{post.slug}'
        photos = f'{post.photos}'

        status = f'{post.status}'

        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(excerpt, 'post excerpt')
        self.assertEqual(content, 'post content')
        self.assertEqual(slug, 'post-title')
        self.assertEqual(photos, 1)
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'django')
