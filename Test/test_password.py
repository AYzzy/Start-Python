from unittest import TestCase

from corn_flakes.password import check_email_validation


class TestPassword(TestCase):
    def test_that_email_is_valid(self):
        input_password = 'example123@domain.com'
        self.assertEqual(check_email_validation(input_password), True)

    def test_that_email_is_valid2(self):
        input_password = "omoniyiayomide798@gmail.com"
        self.assertEqual(check_email_validation(input_password), True)

    def test_that_other_symbols_can_be_add_at_the_middle_from_the_start_till_At_Symbol(self):
        input_password = "ayomide_danieltheboy798@gmail.com"
        self.assertEqual(check_email_validation(input_password), False)

    def test_that_other_symbol_can_be_add_at_the_middle_from_the_start_till_At_Symbol2(self):
        input_password = "ayom.daniel798@gmail.com"
        self.assertEqual(check_email_validation(input_password), False)

    def test_to_start_with_number(self):
        input_password = "124@gmail.com"
        self.assertEqual(check_email_validation(input_password), True)
