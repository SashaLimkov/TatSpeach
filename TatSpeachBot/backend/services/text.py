from backend.models import Translate, Language, Text

def get_text_by_language_and_key(lang:Language, key:str)->Translate:
    return Translate.objects.filter(key=key, language=lang).first().translate


def get_default_language():
    return Language.objects.first()

def get_all_languages():
    return Language.objects.all()