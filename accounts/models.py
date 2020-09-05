from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)
from django.db import models
from lectures.models import Lecture

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
    lecture_history = models.ManyToManyField(
        Lecture, 
        through='History',
        through_fields=('user', 'lecture'),
        verbose_name='시청한 강의',
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
        default=False,
        verbose_name='스태프',
    )
    is_active = models.BooleanField(
        db_index=True,
        default=True,
        verbose_name='계정 활성',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
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


class History(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name="사용자", 
        on_delete=models.CASCADE,
    )
    lecture = models.ForeignKey(
        Lecture,
        verbose_name="강의",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = '시청기록'
        verbose_name_plural = '시청기록'

        ordering = [
            '-created_at',
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'lecture'],
                name='history_pair'
            ),
        ]

    def __str__(self):
        return '{user}-{lecture}'.format(
            user=self.user,
            lecture=self.lecture,
        )
