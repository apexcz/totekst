from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):

    def test_is_correct_addition(self):
        a = 4
        b = 5
        self.assertIs(a+b == 3,False)