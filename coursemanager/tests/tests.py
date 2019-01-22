from django.test import TestCase

class FailingTest(TestCase):

    def test_fail(self):
        self.assertEqual(True, False)