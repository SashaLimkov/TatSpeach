from backend.models import Translate, Language, Text

def get_text_by_language_and_key(lang:Language, key:str)->Translate:
    print(key)
    text_key = Text.objects.filter(key=key).first()
    return Translate.objects.filter(text_key=text_key, language=lang).first().translate


def get_default_language():
    return Language.objects.first()

def get_all_languages():
    return Language.objects.all()


def get_language_by_name(lang_name:str)->Language:
    return Language.objects.filter(name=lang_name).first()