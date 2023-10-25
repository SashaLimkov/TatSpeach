from backend.models import TelegramUser


def get_profile_by_telegram_id(telegram_id):
    return TelegramUser.objects.filter(telegram_id=telegram_id).first()

def create_user(telegram_id: int, full_name: str) -> TelegramUser:
    return TelegramUser.objects.create(
        telegram_id=telegram_id,
        full_name=full_name
    )
