
from django.contrib import admin
from .models import Usuario, Pagamento, ControleFinanceiro

admin.site.register(Usuario)
admin.site.register(Pagamento)
admin.site.register(ControleFinanceiro)

