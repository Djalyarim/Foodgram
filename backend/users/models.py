from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


class Follow(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'following'],
                       name='unique_following')]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
