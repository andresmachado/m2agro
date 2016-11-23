from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum
from api.models import Product

class Command(BaseCommand):
    help = """
        Calcula o preço médio de todos os produtos baseados nos serviços em que estão relacionados.
        
        Ex.: Temos 2 serviços para o mês de Janeiro, cada um usamos o produto DIESEL e 5L, e o custo de cada serviço é de R$ 100. 
            O preço médio seria: (100+100) / 10 = R$20. Esses R$20 devem serão atualizados na tabela do respectivo produto.

        """
    def handle(self, *args, **kwargs):
        actual_month = datetime.now().month
        actual_year = datetime.now().year
        
        products = Product.objects.all()

        for product in products.iterator():
            total_value = product.services.filter(initial_date__year=actual_year,
                                                  initial_date__month=actual_month).aggregate(value=Sum('total_cost'))
            total_items = product.productservicerelationship_set.filter(service__initial_date__year=actual_year,
                                                                        service__initial_date__month=actual_month).aggregate(items=Sum("quantity"))
            parsed_value = float(total_value['value'])
            parsed_items = int(total_items['items'])
            
            average_price = parsed_value / parsed_items
            
            product.price = Decimal(average_price)
            
            product.save()

        self.stdout.write(self.style.SUCCESS("Preços atualizados"))
