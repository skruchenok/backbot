from django.db import models


class TelegramUser(models.Model):
    telegram_chat_id = models.IntegerField()

    def __str__(self):
        return str(self.telegram_chat_id)


class Post(models.Model):
    telegram_user = models.ForeignKey(
        "core.TelegramUser",
        on_delete=models.CASCADE,
        related_name='posts'
    )
    link = models.URLField()

    def __str__(self):
        return f'{self.telegram_user} - {self.id}'


class Like(models.Model):
    telegram_user = models.ForeignKey(
        "core.TelegramUser",
        on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        "core.TelegramUser",
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = ('telegram_user', 'post')
