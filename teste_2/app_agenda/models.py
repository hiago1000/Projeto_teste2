from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone ceular', max_length=15,
                                        help_text = 'Número do telefone ceular no formato (99) 99999-9999',
                                        null = True, blank = True,
                                        )
    telefone_fixo = models.CharField('Telefone fixo', max_length=14,
                                    help_text = 'Número do telefone fixo no formato (99) 9999-9999',
                                    null = True, blank = True,
                                    )
    email = models.EmailField('E-mail', null = True, blank = True)


    def __str__(self):
        return self.nome

class Agenda(models.Model):
    class Meta:
        verbose_name = 'Agenda Particular'
        verbose_name_plural = 'Agenda Particular'

    titulo = models.CharField('título', max_length=128)
    anotacoes = models.TextField()
    publica = models.BooleanField(blank=True, null=True)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True, null=True)
    

class Agenda_Global(models.Model):
    class Meta:
        verbose_name = 'Agenda Institucional'
        verbose_name_plural = 'Agenda Institucional'

    titulo = models.CharField('título', max_length=128)
    anotacoes = models.TextField()
    publica = models.BooleanField(blank=True, null=True)
    data_publicacao = models.DateTimeField(blank=True, null=True)

