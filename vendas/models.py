from django.db import models
from clientes.models import Person
from django.db.models import Sum, F, FloatField, Max
from produtos.models import Produto
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    def __str__(self):
        return self.numero

    def get_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum(F('quantidade') * (F('produto__preco') - F('desconto')),output_field=FloatField())
        )['tot_ped'] or 0

        tot = tot - float(self.impostos) - float(self.desconto)
        self.valor = tot
        Venda.objects.filter(id=self.id).update(valor=tot)



class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.venda.numero + '-' + self.produto.descricao


@receiver(post_save, sender=ItemDoPedido)
def update_venda_total(sender, instance, **kwargs):
    instance.venda.get_total()

@receiver(post_save, sender=Venda)
def update_venda_total(sender, instance, **kwargs):
    instance.get_total()

