import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_null_frenchToEnglish(self):
        self.assertIsNotNone(french_to_english(None),False)
    
    def test_null_englishToFrench(self):
        self.assertIsNotNone(english_to_french(None),False)

    def test_word_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_word_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
