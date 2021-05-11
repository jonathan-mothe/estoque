from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from core.models import TimeStampedModel
from produto.models import Produto
from .managers import EstoqueEntradaManager, EstoqueSaidaManager


MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saída'),
)

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d - %m - %Y'))

    def get_absolute_url(self):
        return reverse_lazy("estoque:estoque_entrada_detail", kwargs={"pk": self.pk})
    

    def nf_formated(self):
        return str(self.nf).zfill(3)


class EstoqueEntrada(Estoque):

    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque estrada'
        verbose_name_plural = 'estoque entrada'


class EstoqueSaida(Estoque):

    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saída'
        verbose_name_plural = 'estoque saída'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque, 
        on_delete=models.CASCADE, 
        related_name='estoques'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
