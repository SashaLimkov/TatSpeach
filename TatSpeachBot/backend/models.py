from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=20, verbose_name="Телеграм ID")
    full_name = models.CharField(max_length=128, verbose_name="Пользователь")
    count_of_sintez_tat = models.IntegerField(verbose_name="Количство синтезированной татарской речи", default=0)
    count_of_sintez_rus = models.IntegerField(verbose_name="Количство синтезированной русской речи", default=0)
    count_of_detect_tat = models.IntegerField(verbose_name="Количство распознанной татарской речи", default=0)
    count_of_detect_rus  = models.IntegerField(verbose_name="Количство распознанной русской речи", default=0)
    selected_language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True, verbose_name="язык Бота", related_name="users_with_lang")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def __str__(self) -> str:
        return self.name
    
class Text(models.Model):
    key = models.CharField(max_length=128, verbose_name="ключ")

    class Meta:
        verbose_name = "Ключ"
        verbose_name_plural = "Ключи"

    def __str__(self) -> str:
        return self.key

class Translate(models.Model):
    key = models.ForeignKey(Text, on_delete=models.CASCADE, related_name="all_translates")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="all_text")
    translate = models.TextField(max_length=2048, verbose_name="Текст")
    
    class Meta:
        verbose_name = "Текст на языке"
        verbose_name_plural = "Тексты на языках"

    def __str__(self) -> str:
        return f"{self.key.key}: {self.translate}"

