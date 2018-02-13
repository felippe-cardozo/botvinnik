from unittest import TestCase
from botvinnik.botvinnik import wiki, _help, veg, methods


class TestBotMethods(TestCase):

    def test_wiki_method(self):
        response = wiki.__wrapped__('\wiki yoga')
        self.assertTrue('Yoga' in response[0])

    def test_wiki_fails_gently(self):
        response = wiki.__wrapped__('\wiki afkhkafhkahf')
        error_string = ('Page id "afkhkafhkahf" does not match any pages.'
                        ' Try another id!')
        self.assertEqual(response, [error_string])

    def test_veg_dont_return_more_than_four_messages(self):
        response = veg.__wrapped__('\\veg batata')
        self.assertTrue(len(response) < 5)

    def test_veg_fails_gently(self):
        response = veg.__wrapped__('\\veg inexistensenonsense')
        self.assertEqual(response, ['Not found :/'])

    def test_help_describes_all_methods(self):
        response = _help.__wrapped__('..')[0]
        self.assertTrue(all([i.__name__ in response for i in methods]))
