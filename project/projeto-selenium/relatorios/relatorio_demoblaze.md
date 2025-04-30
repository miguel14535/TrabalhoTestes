# Relatório de Teste: DemoBlaze

## TC-004: Simulação de compra de produto

**Objetivo:** Verificar se é possível completar o fluxo de compra de um produto.

**Passos Executados:**
1. Abrir o navegador Chrome
2. Navegar para https://www.demoblaze.com/
3. Selecionar aleatoriamente um produto da lista
4. Clicar no botão "Add to cart"
5. Aceitar o alerta que aparece
6. Navegar para o carrinho de compras
7. Verificar se o produto está no carrinho
8. Clicar no botão "Place Order"
9. Preencher o formulário de compra com os seguintes dados:
   - Nome: Test User
   - País: Test Country
   - Cidade: Test City
   - Cartão de crédito: 4111111111111111
   - Mês: 12
   - Ano: 2025
10. Clicar no botão "Purchase"
11. Verificar se a mensagem de confirmação aparece
12. Extrair e registrar o ID do pedido e o valor total

**Dados de Entrada:**
- Nome: Test User
- País: Test Country
- Cidade: Test City
- Cartão de crédito: 4111111111111111
- Mês: 12
- Ano: 2025

**Resultado Esperado:**
- Mensagem de confirmação de compra com texto "Thank you"
- Exibição do ID do pedido e valor total

**Resultado Obtido:**
- Produto selecionado: [Nome do produto]
- Mensagem de confirmação contém "Thank you"
- ID do pedido: [ID do pedido]
- Valor total: [Valor] USD
- Screenshot salvo em: ../relatorios/screenshots/tc_004_confirmation.png

**Status:** Passou

---

## Métricas de Execução

- Data de Execução: [Data atual]
- Início do TC-004: [Hora de início]
- Fim do TC-004: [Hora de término]
- Duração do TC-004: [Duração]

## Análise

O caso de teste para o DemoBlaze foi executado com sucesso. O sistema permite a seleção de um produto, adição ao carrinho, preenchimento do formulário de compra e conclusão da transação. A confirmação da compra é exibida corretamente com as informações do pedido.

## Observações Técnicas

- Foi utilizado tratamento de alertas JavaScript
- Foi implementada a seleção aleatória de produtos para maior cobertura de teste
- Os detalhes da confirmação de compra (ID e valor) foram extraídos usando expressões regulares
- O teste inclui verificações em cada etapa do processo de compra