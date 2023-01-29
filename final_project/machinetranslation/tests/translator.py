"""
Module for handling language translations using IBM Watson Language Translator service
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('2vLYyGeJ_ero9lJ6dltvNygHlBfAApI91cLQIZFJJi3S')
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def english_to_french(english_text: str):
    """
    Translate the given english text to french
    """
    french_text = translator.translate(text=english_text, source='en', target='fr').get_result()
    return french_text['translations'][0]['translation']


def french_to_english(french_text: str):
    """
    Translate the given french text to english
    """
    english_text = translator.translate(text=french_text, source='fr', target='en').get_result()
    return english_text['translations'][0]['translation']
