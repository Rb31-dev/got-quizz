import streamlit as st

# Configurando a página para o formato Wide (tela cheia)
st.set_page_config(
    page_title="GoT Character Quiz",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização personalizada para garantir fundo limpo, fontes modernas e o cabeçalho azul premium
st.markdown("""
<style>
    /* Reset de margens superiores padrões do Streamlit para o cabeçalho colar no topo */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Configuração de fontes globais */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Estilo do cabeçalho azul com menu de navegação estético */
    .header-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 15px 40px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 0 0 8px 8px;
        margin-bottom: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .header-logo {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 1px;
    }
    
    .header-menu {
        display: flex;
        gap: 25px;
        align-items: center;
    }
    
    .menu-item {
        color: rgba(255, 255, 255, 0.85);
        text-decoration: none;
        font-weight: 500;
        font-size: 15px;
        transition: color 0.2s;
        cursor: pointer;
    }
    
    .menu-item:hover {
        color: #ffffff;
    }
    
    .login-btn {
        background-color: #ffffff;
        color: #1e3c72 !important;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600 !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-container">
    <div class="header-logo">🛡️ PORTAL QUIZ</div>
    <div class="header-menu">
        <span class="menu-item">Início</span>
        <span class="menu-item">Mais Quizzes</span>
        <span class="menu-item">Como Jogar</span>
        <span class="menu-item login-btn">Entrar</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.title("⚔️ Quiz de Personagens: Universo de Game of Thrones")
st.write("Digite o nome dos personagens mais marcantes de GoT e House of the Dragon!")

# O banco de dados foi expandido com os nomes principais e secundários relevantes, separados em 5 colunas temáticas
gabarito = {
    "Casa Stark & Norte": [
        "jon snow", "arya stark", "sansa stark", "bran stark", "ned stark", 
        "robb stark", "catelyn stark", "rickon stark", "benjen stark", "lyanna stark",
        "hodor", "tormund", "ygritte", "meera reed", "jojen reed", 
        "roose bolton", "ramsay bolton", "theon greyjoy"
    ],
    "Casa Lannister & Coroa": [
        "tyrion lannister", "cersei lannister", "jaime lannister", "tywin lannister", 
        "joffrey baratheon", "myrcella baratheon", "tommen baratheon", "robert baratheon",
        "sandor clegane", "gregor clegane", "bronn", "petyr baelish", "varys", 
        "qyburn", "podrick payne", "lancel lannister", "grand maester pycelle"
    ],
    "Casa Targaryen & Dragões": [
        "daenerys targaryen", "viserys targaryen", "rhaenyra targaryen", "daemon targaryen", 
        "viserys i targaryen", "aemond targaryen", "aegon ii targaryen", "alicent hightower", 
        "otto hightower", "corlys velaryon", "rhaenys targaryen", "criston cole", 
        "rhaegar targaryen", "aerys ii targaryen", "jacaerys velaryon", "helaena targaryen"
    ],
    "Grandes Casas de Westeros": [
        "stannis baratheon", "renly baratheon", "margaery tyrell", "olenna tyrell", 
        "loras tyrell", "mace tyrell", "oberyn martell", "ellaria sand", "doran martell", 
        "yara greyjoy", "euron greyjoy", "balon greyjoy", "lysa arryn", "robin arryn"
    ],
    "Essos & Aliados Importantes": [
        "jorah mormont", "brienne de tarth", "samwell tarly", "davos seaworth", 
        "melisandre", "barristan selmy", "missandei", "verme cinzento", "khal drogo", 
        "syrio forel", "jaqen hghar", "daario naharis", "gendry baratheon", "shae", "gilly"
    ]
}

# Criando lista unificada em minúsculo para checagem rápida de respostas
todos_personagens = []
for lista in gabarito.values():
    todos_personagens.extend(lista)

if "acertos" not in st.session_state:
    st.session_state.acertos = []
if "limpar_input" not in st.session_state:
    st.session_state.limpar_input = 0

# Função de validação sem comandos que travam o Streamlit Cloud
def checar_resposta():
    # .lower() remove distinção de maiúsculas e .strip() remove espaços extras
    resposta = st.session_state.campo_texto.lower().strip()
    if resposta:
        if resposta in todos_personagens:
            if resposta not in st.session_state.acertos:
                st.session_state.acertos.append(resposta)
        # Força o campo de texto a limpar seu valor interno
        st.session_state.limpar_input += 1

st.text_input(
    "Digite o nome de um personagem:", 
    key="campo_texto", 
    on_change=checar_resposta,
    value="",
    placeholder="Ex: Jon Snow, Rhaenyra Targaryen..."
)

total_personagens = len(todos_personagens)
total_acertos = len(st.session_state.acertos)

# Painel de progresso visual do jogador
st.metric(label="📊 Seu Progresso Atual", value=f"{total_acertos} / {total_personagens} encontrados")

st.write("---")

colunas_interface = st.columns(len(gabarito))

# Loop por todas as colunas do gabarito para desenhar as caixas
for i, (casa, personagens) in enumerate(gabarito.items()):
    with colunas_interface[i]:
        # Cabeçalho azul individual de cada coluna com cantos arredondados
        st.markdown(
            f"<div style='background-color:#2a5298; color:white; padding:12px; text-align:center; font-weight:bold; font-size:14px; border-radius:5px 5px 0px 0px; min-height: 45px; display: flex; align-items: center; justify-content: center;'>{casa}</div>", 
            unsafe_allow_html=True
        )
        
        # Renderizando cada item daquela coluna
        for p in personagens:
            if p in st.session_state.acertos:
                # Estilo moderno para itens descobertos (verde pastel suave com texto em verde escuro)
                st.markdown(
                    f"<div style='border-left: 1px solid #ddd; border-right: 1px solid #ddd; border-bottom: 1px solid #ddd; padding: 8px; background-color: #e6f4ea; color: #137333; font-weight: bold; font-size: 13px; text-align:center;'>{p.title()}</div>", 
                    unsafe_allow_html=True
                )
            else:
                # Estilo para itens vazios (linhas pontilhadas/suaves, parecidas com gabarito em branco)
                st.markdown(
                    "<div style='border-left: 1px solid #ddd; border-right: 1px solid #ddd; border-bottom: 1px solid #ddd; padding: 8px; color: #d0d0d0; background-color: #fafafa; font-size: 13px; text-align:center;'>---</div>", 
                    unsafe_allow_html=True
                )

st.write(" ")
st.write(" ")

if st.button("🔄 Reiniciar e Zerar Quiz"):
    st.session_state.acertos = []
    st.session_state.limpar_input += 1
    st.rerender() if hasattr(st, "rerender") else st.experimental_rerun()
