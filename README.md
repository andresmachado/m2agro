# m2agro
m2agro Challenge


# Informações
## Credenciais
admin:admin2016

## Rotina para atualizar preços médios
>> ./manage.py get_product_average_price

## Para servir XML
Basta apenas colocar o sufixo na url desejada.
> Ex.: http://localhost:8000/api/services.xml

## Pensamentos durante o desenvolvimento

* Vou precisar criar um model intermédiario para controlar os produtos e suas quantidades em cada serviço.
* Para criar a API de serviços, por padrão, o DRF não fornece o metódo CREATE para relações com model intermédiario, precisarei sobrescrever o metódo dentro do serializer.
* Precisarei também de um metódo UPDATE para atualizar os serviços.
* Para servir XML, vou precisar instalar um pacote de terceiros (o próprio DRF fornece isso?).
* Na rotina de atualização de preços, preciso otimizar as querys considerando a quantidade possivel de produtos dentro da base.
* Utiliza as funções internas do ORM do Django (Aggregate, Annotate, etc..)


## Boas práticas

* Seguir sempre a pep8
* Explicit is better then implicit
* Beautiful is better than ugly
* Readability counts
* Anybody can fix anything