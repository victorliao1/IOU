import django_tables2 as tables
from .models import MoneyOwed

class MoneyOwedTable(tables.Table):
    class Meta:
        model = MoneyOwed
        template_name = 'django_tables2/bootstrap.html'
        exclude = ['id']