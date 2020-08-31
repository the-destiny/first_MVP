from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='이름',
    )
    email = models.EmailField(
        blank=True, 
        max_length=254,
        verbose_name='이메일',
    )
    lecture_count = models.PositiveIntegerField(
        default=0,
        verbose_name='시청한 강의 개수',
    )
    is_subscriber = models.BooleanField(
        default=False,
        verbose_name='구독의향',
    )
    is_staff = models.BooleanField(
        db_index=True,
        default=True,
        verbose_name='스태프',
    )
    is_active = models.BooleanField(
        db_index=True,
        default=True,
        verbose_name='계정 활성',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

        ordering = [
            '-is_subscriber',
            'username',
        ]

    def __str__(self):
        return '{is_subscriber}{username}/{email}'.format(
            username=self.username,
            email=self.email,
            is_subscriber='✅' if self.is_subscriber else '',
        )
