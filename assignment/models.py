from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.utils.translation import gettext_lazy as _


class Boss(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('boss')
        verbose_name_plural = _('boss')


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='employee', null=True)
    position = models.CharField(max_length=50, verbose_name='position')
    salary = models.PositiveBigIntegerField(verbose_name='salary')
    boss = models.ForeignKey(Boss, related_name='employees', on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')

