import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(None), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

def test_frenchToEnglish(self):
    self.assertEqual(frenchToEnglish(None), '')
    self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if name =='main':
unittest.main()