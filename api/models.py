from django.db import models
from django.core.validators import (
    EmailValidator,
    MinLengthValidator,
    validate_ipv4_address,
    ValidationError
)
# Create your models here.


def event_level_validate(event):
    if event not in (
        'CRITICAL',
        'DEBUG',
        'ERROR',
        'WARNING',
            'INFO'):
        raise ValidationError('Level not found')


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Ultimo Acesso', auto_now=True)
    email = models.CharField('Email', max_length=254, validators=[
                             EmailValidator('Insira um email válido')])
    password = models.CharField('Senha', max_length=50, validators=[
                                MinLengthValidator(8)])


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Versao', max_length=5)
    address = models.CharField('Endereco', max_length=39, validators=[
                               validate_ipv4_address])


class Event(models.Model):
    level = models.CharField('Level', max_length=20,
                             validators=[event_level_validate])
    data = models.TextField('Dado')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Data', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
