# Projeto de Testes com Selenium

Este projeto contém uma série de testes automatizados utilizando Selenium WebDriver para testar diferentes websites.

## Estrutura do Projeto

```
projeto-selenium/
├─ drivers/                # WebDrivers (ChromeDriver, GeckoDriver)
├─ scripts/                # Scripts de testes para cada caso de teste
│  ├─ tc_saucedemo.py      # Teste de login no SauceDemo
│  ├─ tc_dynamic_loading.py # Teste de carregamento dinâmico
│  ├─ tc_demoblaze.py      # Teste de fluxo de compra no DemoBlaze
│  └─ tc_formy.py          # Teste de preenchimento de formulário
├─ relatorios/             # Relatórios de cada caso de teste
│  ├─ relatorio_saucedemo.md
│  ├─ relatorio_dynamic_loading.md
│  ├─ relatorio_demoblaze.md
│  └─ relatorio_formy.md
├─ run_tests.py            # Script para executar todos os testes
└─ requirements.txt        # Dependências do projeto
```

## Casos de Teste

### TC-001 e TC-002: SauceDemo (Login)
- TC-001: Login bem-sucedido com usuário padrão
- TC-002: Login mal-sucedido com usuário inválido

### TC-003: The Internet (Dynamic Loading)
- Teste de espera por carregamento dinâmico de elementos

### TC-004: DemoBlaze
- Teste de fluxo completo de compra de um produto

### TC-005: Formy
- Teste de preenchimento e envio de formulário

## Requisitos

- Python 3.7+
- Chrome ou Firefox instalado
- Bibliotecas Python (ver requirements.txt)

## Instalação

1. Clone este repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução dos Testes

Para executar todos os testes:

```bash
python run_tests.py
```

Para executar um teste específico:

```bash
python run_tests.py --test saucedemo  # Executa apenas os testes do SauceDemo
python run_tests.py --test dynamic    # Executa apenas os testes de Dynamic Loading
python run_tests.py --test demoblaze  # Executa apenas os testes do DemoBlaze
python run_tests.py --test formy      # Executa apenas os testes do Formy
```

## Relatórios

Os relatórios dos testes são gerados na pasta `relatorios/`. Cada relatório inclui:

- Objetivo do teste
- Passos executados
- Dados de entrada
- Resultado esperado
- Resultado obtido
- Status (Passou/Falhou)
- Capturas de tela (quando aplicável)

## Notas Técnicas

- O projeto utiliza WebDriverManager para gerenciar automaticamente os drivers do Selenium
- Os testes incluem tratamento de exceções e timeouts adequados
- Screenshots são salvos na pasta `relatorios/screenshots/` para referência
