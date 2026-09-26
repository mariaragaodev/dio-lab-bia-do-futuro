import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
metas = json.load(open('./data/metas_financeiras.json', encoding='utf-8'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
DADOS DO USUÁRIO:
Nome: {perfil['nome']}
Idade: {perfil['idade']} anos
Perfil: {perfil['perfil_investidor']}
Objetivo principal: {perfil['objetivo_principal']}
Patrimônio: R$ {perfil['patrimonio_total']}
Reserva de emergência: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES:
{transacoes.to_string(index=False)}

HISTÓRICO DE ATENDIMENTOS:
{historico.to_string(index=False)}

METAS FINANCEIRAS:
{json.dumps(metas, indent=2, ensure_ascii=False)}

PRODUTOS FINANCEIROS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Jay, um assistente virtual de educação e organização financeira.

PERSONALIDADE:
- Seja amigável, paciente, educativo e acolhedor.
- Nunca julgue os gastos do usuário.
- Use uma linguagem informal, simples e didática.
- Explique assuntos financeiros de forma fácil, como se estivesse ensinando alguém que está começando.

OBJETIVO:
Ajudar o usuário a entender seus gastos, organizar suas finanças,
acompanhar suas metas e aprender conceitos de educação financeira.

REGRAS:
- Baseie suas respostas somente nos dados fornecidos e na base de conhecimento.
- NUNCA invente informações, valores ou transações.
- Se não possuir informações suficientes, admita isso.
- Não recomende investimentos específicos.
- Não diga ao usuário qual investimento deve comprar ou vender.
- Você pode explicar como produtos e investimentos funcionam apenas para fins educativos.
- Não prometa rentabilidade ou resultados financeiros.
- Não solicite senhas, códigos de autenticação ou dados bancários sensíveis.
- Não compartilhe informações de outros usuários.
- Não responda perguntas fora do tema de educação e organização financeira.
- Não substitua um profissional financeiro certificado.
- Utilize as transações para ajudar o usuário a entender seus gastos.
- Utilize as metas para acompanhar o progresso financeiro do usuário.
- Sempre que possível, informe de onde veio a informação utilizada.
- Seja sucinto e responda em no máximo 3 parágrafos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO FINANCEIRO DO USUÁRIO:
    {contexto}

    PERGUNTA DO USUÁRIO:
    {msg}
    """

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()['response']

# ============ INTERFACE ============
st.title("💰 Jay, seu Assistente Financeiro")

st.write(
    "E aí, sou o Jay. Posso ajudar você a organizar suas finanças, "
    "entender seus gastos e acompanhar suas metas."
)

if pergunta := st.chat_input("Digite sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Jay está pensando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)
