from django.test import TestCase
from datetime import datetime
#from .models import Event
from accounts.models import CustomUser

class CustomUserModelTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		#Create Custom User
		CustomUser.objects.create(
            username="test_user_1",
            email="email@testcharity.com",
            password='test_user_1',
            charity_name="Test Charity",
            charity_address_line_1="Main Road",
            charity_address_line_2="London",
            charity_postcode="LON234",
            charity_website_url="http://www.testcharity.com",
            charity_bio="A test charity number 1",
            charity_country='AU',
            charity_operating_continent="oc",
            charity_image="test_user_image.jpg"
        )

    def test_custom_user_details_saved_correctly(self):
    	custom_user = CustomUser.objects.get(username="test_user_1")
    	self.assertEqual(custom_user.username, "test_user_1")
    	self.assertEqual(custom_user.email, "email@test_charity.com")
    	self.assertEqual(custom_user.charity_name, "Test Charity")
    	self.assertEqual(custom_user.charity_bio, "A test charity number 1")

    def test_charity_name_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_name').max_length
        self.assertEqual(max_length, 255)

    def test_charity_address_line_1_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_address_line_1').max_length
        self.assertEqual(max_length, 500)

    def test_charity_address_line_2_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_address_line_2').max_length
        self.assertEqual(max_length, 500)

    def test_charity_postcode_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_postcode').max_length
        self.assertEqual(max_length, 50)

    def test_charity_website_url_help_text(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        help_text = custom_user._meta.get_field('charity_website_url').help_text
        self.assertEqual(help_text, "Please enter a full URL starting with 'http://www...'")

    def test_charity_bio_max_length(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        max_length = custom_user._meta.get_field('charity_bio').max_length
        self.assertEqual(max_length, 2000)

    def test_charity_bio_help_text(self):
        custom_user = CustomUser.objects.get(username="test_user_1")
        help_text = custom_user._meta.get_field('charity_bio').help_text
        self.assertEqual(help_text, 'Add a short description as to what your charity does and who it benefits.')
