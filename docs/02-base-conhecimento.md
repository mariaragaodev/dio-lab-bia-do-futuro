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

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
