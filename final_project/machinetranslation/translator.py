"""
Translator method
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv



load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Translate text from english to french"""
    if english_text is not None:
        french_text = language_translator.translate(
        text=english_text,
        source='en',
        target='fr',
        ).get_result()

        return french_text['translations'][0]['translation']
   
    return False

    



def french_to_english(french_text):
    """ Translate text from french to english """
    if french_text is not None:
        english_text = language_translator.translate(
        text=french_text,
        source='fr',
        target='en',
        ).get_result()

        return english_text['translations'][0]['translation']
    return False
