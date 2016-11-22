from django.db import models

# Create your models here.


class Harvest(models.Model):
    name = models.CharField('Nome', max_length=255)
    initial_date = models.DateField('Data inicial')
    end_date = models.DateField('Data final')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Safra'
        verbose_name_plural = 'Safras'


class Service(models.Model):
    harvest = models.ForeignKey(Harvest, verbose_name='Safra', related_name='services')
    name = models.CharField('Nome', max_length=255)
    initial_date = models.DateField('Data inicial')
    end_date = models.DateField('Data final')
    total_cost = models.DecimalField('Custo total', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class Product(models.Model):
    UNITS = (
        ('l', 'L'),
        ('cx', 'CX'),
        ('un', 'UN')
    )
    service = models.ForeignKey(Service, verbose_name='Serviço', related_name='products')
    name = models.CharField('Nome', max_length=255)
    quantity = models.PositiveSmallIntegerField('Quantidade', default=0)
    unit = models.CharField('Unidade', max_length=5, choices=UNITS)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'