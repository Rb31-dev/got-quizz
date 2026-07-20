import streamlit as st

# Configurando a página para o formato Wide (tela cheia)
st.set_page_config(
    page_title="GoT Character Quiz",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização avançada para garantir o fundo branco, texto escuro de alto contraste, e campo de entrada claro
st.markdown("""
<style>
    /* Força o fundo da tela inteiro a ser branco puro */
    .stApp {
        background-color: #ffffff !important;
    }

    /* Reset de margens superiores padrões do Streamlit para o cabeçalho colar no topo */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        background-color: #ffffff !important;
    }
    
    /* Configuração de fontes globais */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* FORÇAR TEXTOS E TÍTULOS DO STREAMLIT A SEREM ESCUROS (Corrige o bug da imagem) */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp li, .stApp div {
        color: #1e293b;
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
    
    /* Garante que o texto de dentro do cabeçalho azul continue sempre branco */
    .header-container * {
        color: #ffffff !important;
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
    
    /* Menu com visibilidade máxima (branco puro e negrito) */
    .menu-item {
        text-decoration: none;
        font-weight: 700 !important;
        font-size: 15px;
        transition: color 0.2s;
        cursor: pointer;
    }
    
    /* Efeito ao passar o mouse por cima do menu */
    .menu-item:hover {
        color: #ffd700 !important;
    }
    
    .login-btn {
        background-color: #ffffff;
        color: #1e3c72 !important;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700 !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* FORÇAR A CAIXA DE TEXTO A SER CLARA E COM BORDAS DEFINIDAS (Corrige caixa preta da imagem) */
    div[data-testid="stTextInput"] input {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        border: 2px solid #b0b0b0 !important;
        border-radius: 6px !important;
        padding: 10px !important;
    }
    
    div[data-testid="stTextInput"] input::placeholder {
        color: #64748b !important;
    }
    
    div[data-testid="stTextInput"] label p {
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }

    /* Ajuste de contraste para o widget de progresso (st.metric) */
    div[data-testid="stMetricValue"] > div {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 32px !important;
    }
    div[data-testid="stMetricLabel"] > div > p {
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* Classes CSS para as células da grade com divisórias bem nítidas (#b0b0b0) */
    .grid-cell {
        border-left: 1px solid #b0b0b0 !important;
        border-right: 1px solid #b0b0b0 !important;
        border-bottom: 1px solid #b0b0b0 !important;
        padding: 10px 8px;
        font-size: 13px;
        text-align: center;
        transition: background-color 0.3s;
    }

    .grid-cell-empty {
        color: #d0d0d0 !important;
        background-color: #fbfbfb !important;
    }

    .grid-cell-found {
        background-color: #e6f4ea !important;
        color: #137333 !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# Renderizando o cabeçalho estético com menu visível e protegido contra Dark Mode
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

# Título principal com tags HTML para garantir a cor escura
st.markdown("<h1 style='color: #1e293b; margin-bottom: 5px;'>⚔️ Quiz de Personagens: Universo de Game of Thrones</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 16px; margin-bottom: 25px;'>Digite o nome dos personagens mais marcantes de GoT e House of the Dragon!</p>", unsafe_allow_html=True)

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

def checar_resposta():
    # Coleta a resposta digitada
    resposta = st.session_state.campo_texto.lower().strip()
    if resposta:
        # Se for um personagem válido e não repetido, adiciona na lista de acertos
        if resposta in todos_personagens:
            if resposta not in st.session_state.acertos:
                st.session_state.acertos.append(resposta)
        # LIMPA O INPUT AUTOMATICAMENTE apagar o texto digitado na sessão atual
        st.session_state.campo_texto = ""

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
        # Cabeçalho azul individual de cada coluna com cantos arredondados e borda lateral
        st.markdown(
            f"<div style='background-color:#2a5298; color:white; padding:12px; text-align:center; font-weight:bold; font-size:14px; border-radius:5px 5px 0px 0px; min-height: 45px; display: flex; align-items: center; justify-content: center; border: 1px solid #2a5298;'>{casa}</div>", 
            unsafe_allow_html=True
        )
        
        # Renderizando cada item daquela coluna
        for p in personagens:
            if p in st.session_state.acertos:
                # Caixa com o personagem descoberto (verde com borda nítida de cor #b0b0b0)
                st.markdown(
                    f"<div class='grid-cell grid-cell-found'>{p.title()}</div>", 
                    unsafe_allow_html=True
                )
            else:
                # Caixa vazia (linhas de segredo com borda nítida de cor #b0b0b0)
                st.markdown(
                    "<div class='grid-cell grid-cell-empty'>---</div>", 
                    unsafe_allow_html=True
                )

st.write(" ")
st.write(" ")

# Botão para resetar o jogo de forma limpa
if st.button("🔄 Reiniciar e Zerar Quiz"):
    st.session_state.acertos = []
    st.session_state.campo_texto = ""
    st.rerender() if hasattr(st, "rerender") else st.experimental_rerun()
