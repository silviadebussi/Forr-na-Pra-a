from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    # Adicione outros campos conforme necessário

    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_pagamento = models.DateField(default=timezone.now)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    pago = models.BooleanField(default=False)  # Se o pagamento foi feito ou não

    def __str__(self):
        return f'{self.usuario.nome} - {self.data_pagamento}'


class ControleFinanceiro(models.Model):
    data = models.DateField(default=timezone.now)
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.descricao} - {self.valor}'
