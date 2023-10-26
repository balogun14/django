from django.test import SimpleTestCase
from django.shortcuts import make_toast


class MakeToastTests(SimpleTestCase):
    """
    This is a class that is a child to the simple testcase
    and the function checks whether the make_toast() methods returns the string toast
    """

    def test_make_toast(self):
        self.assertEqual(make_toast(), "toast")
