from TatSpeachBot.backend.models import Language
from TatSpeachBot.backend.services.text import get_text_by_language_and_key


def get_text(key:str, lang:Language):
    return get_text_by_language_and_key(key=key, lang=lang)