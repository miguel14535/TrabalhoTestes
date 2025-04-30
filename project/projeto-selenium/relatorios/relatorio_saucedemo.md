# Relatório de Teste: SauceDemo

## TC-001: Login bem-sucedido com usuário padrão

**Objetivo:** Verificar se o login é bem-sucedido usando credenciais válidas.

**Passos Executados:**
1. Abrir o navegador Chrome
2. Navegar para https://www.saucedemo.com/
3. Localizar o campo de usuário pelo ID "user-name"
4. Localizar o campo de senha pelo ID "password"
5. Localizar o botão de login pelo ID "login-button"
6. Inserir "standard_user" no campo de usuário
7. Inserir "secret_sauce" no campo de senha
8. Clicar no botão de login
9. Verificar se a URL contém "inventory.html"
10. Verificar se o container de inventário está visível

**Dados de Entrada:**
- Usuário: standard_user
- Senha: secret_sauce

**Resultado Esperado:**
- Redirecionamento para a página de inventário
- Container de inventário visível

**Resultado Obtido:**
- URL contém "inventory.html"
- Container de inventário está visível
- Screenshot salvo em: ../relatorios/screenshots/tc_001_success.png

**Status:** Passou

---

## TC-002: Login mal-sucedido com usuário inválido

**Objetivo:** Verificar se o login falha usando credenciais inválidas.

**Passos Executados:**
1. Abrir o navegador Chrome
2. Navegar para https://www.saucedemo.com/
3. Localizar o campo de usuário pelo ID "user-name"
4. Localizar o campo de senha pelo ID "password"
5. Localizar o botão de login pelo ID "login-button"
6. Inserir "invalid_user" no campo de usuário
7. Inserir "wrong_password" no campo de senha
8. Clicar no botão de login
9. Verificar se o container de mensagem de erro está visível
10. Verificar se a mensagem de erro contém "Epic sadface"

**Dados de Entrada:**
- Usuário: invalid_user
- Senha: wrong_password

**Resultado Esperado:**
- Exibição de mensagem de erro
- Mensagem de erro contém "Epic sadface"

**Resultado Obtido:**
- Container de mensagem de erro está visível
- Mensagem de erro contém "Epic sadface"
- Screenshot salvo em: ../relatorios/screenshots/tc_002_failure.png

**Status:** Passou

---

## Métricas de Execução

- Data de Execução: [Data atual]
- Início do TC-001: [Hora de início]
- Fim do TC-001: [Hora de término]
- Duração do TC-001: [Duração]
- Início do TC-002: [Hora de início]
- Fim do TC-002: [Hora de término]
- Duração do TC-002: [Duração]

## Análise

Os dois casos de teste para o SauceDemo foram executados com sucesso. O sistema responde corretamente tanto para credenciais válidas quanto inválidas, mostrando o comportamento esperado em ambos os cenários.