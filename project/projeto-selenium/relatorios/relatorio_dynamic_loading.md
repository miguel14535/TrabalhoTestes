# Relatório de Teste: Dynamic Loading

## TC-003: Espera pelo carregamento dinâmico de elemento

**Objetivo:** Verificar se o texto "Hello World!" aparece após clicar no botão Start.

**Passos Executados:**
1. Abrir o navegador Chrome
2. Navegar para https://the-internet.herokuapp.com/dynamic_loading
3. Clicar no link do Example 1
4. Localizar e clicar no botão "Start"
5. Aguardar até que o elemento com o texto "Hello World!" esteja visível (timeout de 30 segundos)
6. Verificar se o elemento está visível e contém o texto esperado

**Dados de Entrada:**
- Nenhum dado de entrada necessário

**Resultado Esperado:**
- Texto "Hello World!" aparece após o carregamento

**Resultado Obtido:**
- O texto "Hello World!" foi exibido após [Tempo de espera] segundos
- Screenshot salvo em: ../relatorios/screenshots/tc_003_success.png

**Status:** Passou

---

## Métricas de Execução

- Data de Execução: [Data atual]
- Início do TC-003: [Hora de início]
- Fim do TC-003: [Hora de término]
- Duração do TC-003: [Duração]
- Tempo de espera para o elemento carregar: [Tempo de espera] segundos

## Análise

O caso de teste para o Dynamic Loading foi executado com sucesso. O sistema carrega corretamente o elemento após clicar no botão Start e exibe o texto "Hello World!" conforme esperado. O uso de Explicit Wait (WebDriverWait) permitiu que o teste aguardasse o tempo necessário para o carregamento do elemento, evitando falhas por timing.

## Observações Técnicas

- Foi utilizado WebDriverWait com expected_conditions para aguardar o carregamento do elemento
- O tempo total de espera foi registrado para análise de performance
- O teste inclui tratamento de exceções caso o elemento não apareça dentro do timeout definido