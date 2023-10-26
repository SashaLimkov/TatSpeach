from backend.models import Language, TelegramUser


def get_profile_by_telegram_id(telegram_id):
    return TelegramUser.objects.filter(telegram_id=telegram_id).first()

def create_user(telegram_id: int, full_name: str, language: Language) -> TelegramUser:
    return TelegramUser.objects.create(
        telegram_id=telegram_id,
        full_name=full_name,
        selected_language=language,
    )

def update_selected_language(telegram_id, language):
    user = get_profile_by_telegram_id(telegram_id=telegram_id)
    user.selected_language = language
    user.save()
