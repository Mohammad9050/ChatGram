from django.contrib.auth.models import User
from django.test import TestCase

from django.test import Client
from Accounts.models import Profile
from Chats.models import Text
from django.urls import reverse


class TextModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='test_pas', email='test@gmail.com')
        user2 = User.objects.create(username='test_user2', password='test_pas2', email='test2@gmail.com')
        profile = Profile.objects.create(user=user, username_id='test_id')
        profile2 = Profile.objects.create(user=user2, username_id='test_id2')
        Text.objects.create(from_user=profile, text='test text', to=profile2)

    def test_user_content(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.password, 'test_pas')
        self.assertEqual(user.email, 'test@gmail.com')

    def test_profile_content(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.user_id, 1)
        self.assertEqual(profile.username_id, 'test_id')
        self.assertEqual(profile.photo, 'photos/download.png')

    def test_text_content(self):
        text = Text.objects.get(id=1)
        self.assertEqual(text.from_user_id, 1)
        self.assertEqual(text.to_id, 2)
        self.assertEqual(text.text, 'test text')


class AccountViewTest(TestCase):
    def setUp(self):
        User.objects.create(username='test_user', password='test_pas', email='test@gamil.com')

    def test_url_location(self):
        resp = self.client.get('/account/sign_up')
        resp2 = self.client.get('/account/login')
        resp3 = self.client.get('/account/logout')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp3.status_code, 302)
        self.assertTemplateUsed(resp, 'Accounts/sign_up.html')
        self.assertTemplateUsed(resp2, 'accounts/login.html')


class FallowTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user')
        user.set_password('test_pas')
        user.save()
        user2 = User.objects.create(username='test_user2', password='test_pas2')
        Profile.objects.create(user=user, username_id='test_id')
        Profile.objects.create(user=user2, username_id='test_id2')
        self.client.login(username='test_user', password='test_pas')

    def test_add_friend(self):
        self.client.get(reverse('Chats:add', args='2'))
        profile1 = Profile.objects.get(id=1)
        profile2 = Profile.objects.get(id=2)
        self.assertEqual(profile1.following.get(id=profile2.id), profile2)
        self.assertEqual(profile2.follower.get(id=profile1.id), profile1)

    def test_remove_friend(self):
        resp = self.client.get(reverse('Chats:remove', args='2'))
        self.assertEqual(resp.status_code, 302)

