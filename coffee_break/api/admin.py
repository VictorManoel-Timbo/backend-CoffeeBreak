from django.contrib import admin
from .models import (
    Usuario,
    Categoria,
    Produto,
    Pedido,
    ProdutoPedido,
    Pagamento,
    Estoque,
    Ingrediente,
    ComposicaoProdutoEstoque,
)

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ProdutoPedido)
admin.site.register(Pagamento)
admin.site.register(Estoque)
admin.site.register(Ingrediente)
admin.site.register(ComposicaoProdutoEstoque)
