from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    senha = models.CharField(max_length=100)

    FUNCOES = [
        ("admin", "Administrador"),
        ("comum", "Comum"),
    ]
    funcao = models.CharField(max_length=20, choices=FUNCOES, default="comum")

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    imagem_url = models.TextField(blank=True, null=True)
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    image_url = models.TextField(blank=True, null=True)
    calorias = models.IntegerField(blank=True, null=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    forma_entrega = models.CharField(max_length=30, blank=True, null=True)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"


class ProdutoPedido(models.Model):
    quantidade = models.IntegerField()
    preco_unidade = models.DecimalField(max_digits=8, decimal_places=2)
    desconto = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    observacao = models.TextField(blank=True, null=True)
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no Pedido #{self.pedido.id}"


class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=30)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    parcelas = models.IntegerField(blank=True, null=True)
    pedido = models.OneToOneField("Pedido", on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Pagamento #{self.id} - Pedido #{self.pedido.id} - {self.metodo_pagamento}"
        )


class Estoque(models.Model):
    tipo = models.CharField(max_length=50)
    capacidade = models.IntegerField(blank=True, null=True)
    temperatura = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tipo


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    estoque_minimo = models.IntegerField(default=0)
    unidade_medida = models.CharField(max_length=20, blank=True, null=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class ComposicaoProdutoEstoque(models.Model):
    quantidade_necessaria = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_uso = models.CharField(max_length=50, blank=True, null=True)
    substituivel = models.BooleanField(default=False)
    reutilizavel = models.BooleanField(default=False)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    ingrediente = models.ForeignKey("Ingrediente", on_delete=models.CASCADE)
    estoque = models.ForeignKey("Estoque", on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.quantidade_necessaria} de {self.ingrediente.nome} "
            f"para {self.produto.nome} em {self.estoque.tipo}"
        )
