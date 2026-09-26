# Base de Conhecimento

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
DADOS DO CLIENTE ():

PERFIL DO CLIENTE ():

TRANSAÇÕES DO CLIENTE ():

METAS DO CLIENTE ():

PRODUTOS DISPONÍVEIS PARA ENSINO ():
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
DADOS DO USUÁRIO

Nome: João Silva

PERFIL
Perfil: Moderado

TRANSAÇÕES RECENTES
- 01/11: Supermercado - R$ 450,00
- 03/11: Streaming - R$ 55,00
- 05/11: Transporte - R$ 120,00
- 08/11: Restaurante - R$ 150,00

METAS FINANCEIRAS
- Meta: Viagem
- Valor da meta: R$ 5.000,00
- Valor atual: R$ 2.000,00
- Valor restante: R$ 3.000,00

HISTÓRICO DE ATENDIMENTO
- Usuário perguntou anteriormente sobre organização de gastos.
- Usuário demonstrou interesse em acompanhar suas metas financeiras.

PRODUTOS FINANCEIROS
- Informações disponíveis sobre produtos financeiros para fins educativos.
- O Jay pode explicar as características dos produtos, mas não deve recomendar um produto específico ao usuário.
