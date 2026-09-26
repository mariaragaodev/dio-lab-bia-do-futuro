# Base de Conhecimento
> [!TIP]
> Prompt usado para esta etapa:
> Organize a base de conhecimento do agente "Jay" usando os 5 arquivos da pasta data/ (em anexo). Explique pra > que serve cada arquivo e monte um exemplo de contexto formatado que será enviado pro LLM. Preencha o template > abaixo.
>
>[cole ou anexe o template 02-base-conhecimento.md pra contexto]

## Dados Utilizados

Para o funcionamento do Jay, serão utilizados dados financeiros fictícios e estruturados, com o objetivo de simular a realidade financeira dos usuários. Os dados são utilizados para contextualizar as respostas do agente e auxiliar na organização financeira.

| Arquivo | Formato | Para que serve no Jay? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar as explicações das dúvidas |
| `produtos_financeiros.json` | JSON | Conhecer os produtos para que possam ser explicados ao usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar as informações de forma didática |
| `metas_financeiras.json` | JSON | Consultar e acompanhar as metas financeiras do usuário |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados disponíveis na pasta data/ foram adaptados para atender à proposta do agente Jay, com foco em organização e educação financeira.

Foi adicionado o arquivo metas_financeiras.json, utilizado para armazenar e acompanhar as metas financeiras dos usuários, como valor da meta, valor já alcançado e prazo para atingir o objetivo.

Os demais arquivos (transacoes.csv, historico_atendimento.csv, perfil_investidor.json e produtos_financeiros.json) foram utilizados como base de contexto para o agente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + c, Ctrl + v) ou carregar os arquivos via código, como no exemplo abaixo: 
```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")

# JSONs
with open ("data/perfil_investidor.json", "r", encoding='utf-8') as f:
   perfil = json.load(f)
with open ("data/produtos_financeiros.json", "r", encoding='utf-8') as f:
   produtos = json.load(f)
with open ("data/metas_financeiras.json", "r", encoding='utf-8') as f:
   metas = json.load(f)

```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o Jay tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

PERFIL DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

TRANSAÇÕES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

METAS DO CLIENTE (data/metas_financeiras.json):
{
  "metas_financeiras": [
    {
      "id": 1,
      "usuario_id": 1,
      "nome": "Viagem",
      "descricao": "Economizar para uma viagem de férias",
      "valor_meta": 3000.00,
      "valor_atual": 1200.00,
      "prazo_meses": 6,
      "status": "em_andamento"
    },
    {
      "id": 2,
      "usuario_id": 1,
      "nome": "Reserva de emergência",
      "descricao": "Criar uma reserva para situações inesperadas",
      "valor_meta": 5000.00,
      "valor_atual": 2000.00,
      "prazo_meses": 12,
      "status": "em_andamento"
    },
    {
      "id": 3,
      "usuario_id": 2,
      "nome": "Curso",
      "descricao": "Guardar dinheiro para realizar um curso",
      "valor_meta": 1500.00,
      "valor_atual": 900.00,
      "prazo_meses": 4,
      "status": "em_andamento"
    }
  ]
}

PRODUTOS DISPONÍVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
CONTEXTO DO USUÁRIO

Nome: João Silva
Idade: 32 anos
Profissão: Analista de Sistemas
Renda mensal: R$ 5.000,00
Objetivo principal: Construir reserva de emergência

ÚLTIMAS TRANSAÇÕES:
- 01/10: Salário - R$ 5.000,00 - Receita
- 02/10: Aluguel - R$ 1.200,00 - Moradia
- 03/10: Supermercado - R$ 450,00 - Alimentação
- 05/10: Netflix - R$ 55,90 - Lazer
- 07/10: Farmácia - R$ 89,00 - Saúde
- 10/10: Restaurante - R$ 120,00 - Alimentação
- 12/10: Uber - R$ 45,00 - Transporte
- 15/10: Conta de Luz - R$ 180,00 - Moradia
- 20/10: Academia - R$ 99,00 - Saúde
- 25/10: Combustível - R$ 250,00 - Transporte

METAS FINANCEIRAS:
- Reserva de emergência: R$ 2.000,00 de R$ 5.000,00
- Viagem: R$ 1.200,00 de R$ 3.000,00

HISTÓRICO DE ATENDIMENTO:
- Cliente já perguntou sobre organização financeira.
- Cliente já acompanhou o progresso de uma meta financeira.
- Cliente já solicitou explicações sobre produtos financeiros.

