import strong_password_detection
import unittest


class TestDataCheck (unittest.TestCase):
    def test_is_password_long(self):
        self.assertTrue(strong_password_detection.is_passowrd_long("12345678"))
        self.assertFalse(strong_password_detection.is_passowrd_long("1234567"))
        self.assertTrue(strong_password_detection.is_passowrd_long("aabbccddeeff"))


    def test_is_contains_lower_character(self):
        self.assertTrue(strong_password_detection.is_contains_lower_character("abcABC#2"))
        self.assertFalse(strong_password_detection.is_contains_lower_character("ABCABC#2"))
    

    def test_is_contains_upper_character(self):
        self.assertTrue(strong_password_detection.is_contains_upper_character("abcABC#2"))
        self.assertFalse(strong_password_detection.is_contains_upper_character("abcabc#2"))


    def test_is_contains_decimal_character(self):
        self.assertTrue(strong_password_detection.is_contains_decimal_character("abcABC#2"))
        self.assertTrue(strong_password_detection.is_contains_decimal_character("225"))
        self.assertFalse(strong_password_detection.is_contains_decimal_character("abcabc#%$"))

     
    def test_is_contains_special_characters(self):
        self.assertTrue(strong_password_detection.is_contains_special_characters("abcABC#2"))
        self.assertTrue(strong_password_detection.is_contains_special_characters("abcABC?"))
        self.assertFalse(strong_password_detection.is_contains_special_characters("abcABC12"))


    def test_is_strong_password(self):
        self.assertTrue(strong_password_detection.is_strong_password("abcABC#2"))
        self.assertTrue(strong_password_detection.is_strong_password("225#abcA"))
        self.assertFalse(strong_password_detection.is_strong_password("aB2$")) #to short
        self.assertFalse(strong_password_detection.is_strong_password("abcabc#%$2")) #without upper
        self.assertFalse(strong_password_detection.is_strong_password("abcaBC222")) #without special characters
        self.assertFalse(strong_password_detection.is_strong_password("abcAbc#%$")) #without num





if __name__ == '__main__':
    unittest.main()