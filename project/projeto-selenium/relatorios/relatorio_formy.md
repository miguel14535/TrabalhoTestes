# Relatório de Teste: Formy

## TC-005: Preenchimento e envio de formulário

**Objetivo:** Verificar se é possível preencher todos os campos do formulário e enviá-lo com sucesso.

**Passos Executados:**
1. Abrir o navegador Chrome
2. Navegar para https://formy-project.herokuapp.com/form
3. Preencher os seguintes campos:
   - First name: John
   - Last name: Doe
   - Job title: QA Engineer
   - Education: College (radio button)
   - Gender: Male (checkbox)
   - Years of experience: 2-4 (dropdown)
   - Date: 12/25/2023
4. Clicar no botão "Submit"
5. Aguardar a mensagem de sucesso
6. Verificar se a mensagem de sucesso é exibida corretamente

**Dados de Entrada:**
- First name: John
- Last name: Doe
- Job title: QA Engineer
- Education: College
- Gender: Male
- Years of experience: 2-4
- Date: 12/25/2023

**Resultado Esperado:**
- Mensagem de sucesso: "The form was successfully submitted!"

**Resultado Obtido:**
- Mensagem de sucesso: "The form was successfully submitted!"
- Screenshots salvos em:
  - ../relatorios/screenshots/tc_005_before_submit.png
  - ../relatorios/screenshots/tc_005_after_submit.png

**Status:** Passou

---

## Métricas de Execução

- Data de Execução: [Data atual]
- Início do TC-005: [Hora de início]
- Fim do TC-005: [Hora de término]
- Duração do TC-005: [Duração]

## Análise

O caso de teste para o Formy foi executado com sucesso. O sistema permite o preenchimento correto de todos os campos do formulário e exibe a mensagem de confirmação após o envio.

## Observações Técnicas

- Foram utilizadas diferentes técnicas de seleção de elementos:
  - Seleção por ID para campos de texto
  - Seleção por ID para radio buttons e checkboxes
  - Classe Select para o dropdown de experiência
- Foram capturados screenshots antes e depois do envio do formulário
- Todos os valores preenchidos foram registrados para o relatório