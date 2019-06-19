from django.test import TestCase

class test_bad_maths(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)