import streamlit as st
import streamlit.components.v1 as components

# Configuração inicial da página Streamlit
st.set_page_config(
    page_title="Lovewen'S - Quizzes de Personagens",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização global do Streamlit para ocupar tela cheia
st.markdown("""
<style>
    /* Ocultar elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    .stApp {
        background-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lovewen'S Quizzes</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #f8fafc;
            color: #0f172a;
            padding: 0;
            margin: 0;
            padding-bottom: 50px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        /* Tema Escuro Ativo (quando jogar Coraline) */
        body.dark-theme {
            background-color: #0d1117;
            color: #f0f6fc;
        }

        /* Header superior fixo */
        .header-container {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 14px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 25px;
            transition: background 0.4s ease;
        }

        body.dark-theme .header-container {
            background: linear-gradient(135deg, #2d124d 0%, #1a0b2e 100%);
            border-bottom: 2px solid #6b21a8;
        }

        .header-logo {
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
        }

        .header-menu {
            display: flex;
            gap: 20px;
            align-items: center;
        }

        .menu-item {
            color: #ffffff !important;
            text-decoration: none;
            font-weight: 700;
            font-size: 14px;
            cursor: pointer;
            transition: color 0.2s, transform 0.1s;
            user-select: none;
        }

        .menu-item:hover {
            color: #ffd700 !important;
            transform: translateY(-1px);
        }

        body.dark-theme .menu-item:hover {
            color: #c084fc !important;
        }

        .login-btn {
            background-color: #ffffff;
            color: #1e3c72 !important;
            padding: 7px 20px;
            border-radius: 20px;
            font-weight: 700;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        }

        body.dark-theme .login-btn {
            background-color: #a855f7;
            color: #ffffff !important;
        }

        /* Conteúdo principal */
        .main-content {
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 20px;
        }

        h1 {
            color: #0f172a;
            font-size: 28px;
            margin-bottom: 6px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        body.dark-theme h1 {
            color: #f3e8ff;
        }

        p.subtitle {
            color: #475569;
            font-size: 15px;
            margin-bottom: 20px;
        }

        body.dark-theme p.subtitle {
            color: #c084fc;
        }

        /* Input de busca */
        .input-group {
            margin-bottom: 20px;
        }

        .input-label {
            display: block;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 8px;
            font-size: 15px;
        }

        body.dark-theme .input-label {
            color: #e9d5ff;
        }

        .search-input {
            width: 100%;
            padding: 14px 18px;
            font-size: 16px;
            border: 2px solid #94a3b8;
            border-radius: 8px;
            background-color: #ffffff;
            color: #0f172a;
            outline: none;
            transition: all 0.2s ease;
        }

        body.dark-theme .search-input {
            border: 2px solid #6b21a8;
            background-color: #161b22;
            color: #f0f6fc;
        }

        .search-input:focus {
            border-color: #2a5298;
            box-shadow: 0 0 0 3px rgba(42, 82, 152, 0.2);
        }

        body.dark-theme .search-input:focus {
            border-color: #a855f7;
            box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.25);
        }

        /* Placar de progresso */
        .score-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 14px 20px;
            border-radius: 8px;
            margin-bottom: 25px;
        }

        body.dark-theme .score-container {
            background-color: #161b22;
            border-color: #30363d;
        }

        .score-title {
            font-size: 15px;
            color: #475569;
            font-weight: 600;
        }

        body.dark-theme .score-title {
            color: #94a3b8;
        }

        .score-number {
            font-size: 24px;
            font-weight: 800;
            color: #1e3c72;
        }

        body.dark-theme .score-number {
            color: #c084fc;
        }

        /* Grade do Quiz */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 30px;
        }

        @media (max-width: 900px) {
            .grid-container {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 500px) {
            .grid-container {
                grid-template-columns: 1fr;
            }
        }

        .column-box {
            display: flex;
            flex-direction: column;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #cbd5e1;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }

        body.dark-theme .column-box {
            background-color: #161b22;
            border-color: #30363d;
        }

        .column-header {
            background-color: #2a5298;
            color: #ffffff;
            padding: 12px 8px;
            text-align: center;
            font-weight: 700;
            font-size: 13px;
            min-height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 1px solid #1e3c72;
        }

        body.dark-theme .column-header {
            background: linear-gradient(135deg, #581c87 0%, #3b0764 100%);
            border-bottom: 1px solid #6b21a8;
            color: #f3e8ff;
        }

        /* Células das colunas */
        .cell {
            border-bottom: 1px solid #e2e8f0;
            padding: 10px 8px;
            text-align: center;
            font-size: 13px;
            transition: all 0.25s ease;
        }

        body.dark-theme .cell {
            border-bottom: 1px solid #21262d;
        }

        .cell:last-child {
            border-bottom: none;
        }

        .cell-empty {
            background-color: #f8fafc;
            color: #94a3b8;
        }

        body.dark-theme .cell-empty {
            background-color: #0d1117;
            color: #484f58;
        }

        .cell-found {
            background-color: #e6f4ea;
            color: #137333;
            font-weight: 800;
        }

        body.dark-theme .cell-found {
            background-color: #14532d;
            color: #4ade80;
        }

        .reset-btn {
            background-color: #ef4444;
            color: white;
            border: none;
            padding: 12px 22px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 10px;
            transition: background-color 0.2s;
        }

        .reset-btn:hover {
            background-color: #dc2626;
        }

        /* MODAL / POPUP PARA SELEÇÃO DE QUIZZES */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(4px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }

        .modal-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 30px;
            width: 90%;
            max-width: 600px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            transform: translateY(20px);
            transition: transform 0.3s ease;
            position: relative;
        }

        body.dark-theme .modal-card {
            background: #161b22;
            border: 1px solid #30363d;
            color: #f0f6fc;
        }

        .modal-overlay.active .modal-card {
            transform: translateY(0);
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 15px;
        }

        body.dark-theme .modal-header {
            border-bottom-color: #30363d;
        }

        .modal-title {
            font-size: 20px;
            font-weight: 800;
            color: #0f172a;
        }

        body.dark-theme .modal-title {
            color: #f3e8ff;
        }

        .close-btn {
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #64748b;
            line-height: 1;
        }

        .close-btn:hover {
            color: #0f172a;
        }

        body.dark-theme .close-btn:hover {
            color: #ffffff;
        }

        .quiz-option-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .quiz-option-card {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 16px;
            border-radius: 12px;
            border: 2px solid #e2e8f0;
            cursor: pointer;
            transition: all 0.2s ease;
            background-color: #f8fafc;
        }

        body.dark-theme .quiz-option-card {
            background-color: #0d1117;
            border-color: #30363d;
        }

        .quiz-option-card:hover {
            border-color: #2a5298;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        body.dark-theme .quiz-option-card:hover {
            border-color: #a855f7;
            box-shadow: 0 4px 12px rgba(168, 85, 247, 0.2);
        }

        .quiz-option-card.active {
            border-color: #2a5298;
            background-color: #eff6ff;
        }

        body.dark-theme .quiz-option-card.active {
            border-color: #a855f7;
            background-color: #2e1065;
        }

        .quiz-icon {
            font-size: 32px;
        }

        .quiz-info h3 {
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .quiz-info p {
            font-size: 13px;
            color: #64748b;
        }

        body.dark-theme .quiz-info p {
            color: #94a3b8;
        }
    </style>
</head>
<body>

    <div class="header-container">
        <div class="header-logo" onclick="switchQuiz('got')">
            <span style="font-size: 26px;">🎮</span>
            <span>Lovewen'S</span>
        </div>
        <div class="header-menu">
            <span class="menu-item" onclick="switchQuiz('got')">Início</span>
            <span class="menu-item" onclick="openModal('quizzesModal')">Mais Quizzes</span>
            <span class="menu-item" onclick="openModal('howToPlayModal')">Como Jogar</span>
            <span class="menu-item login-btn">Entrar</span>
        </div>
    </div>

    <div class="main-content">
        <h1 id="quizTitle">⚔️ O Quiz Definitivo de Game of Thrones</h1>
        <p class="subtitle" id="quizSubtitle">O quanto você conhece do universo de GOT?</p>

        <div class="input-group">
            <label class="input-label" for="quizInput" id="inputLabelText">Digite um nome:</label>
            <input 
                type="text" 
                id="quizInput" 
                class="search-input" 
                autocomplete="off"
                autofocus
                placeholder="Digite aqui e os acertos preencherão automaticamente..."
            />
        </div>

        <div class="score-container">
            <span class="score-title">📊 Seu Progresso Atual</span>
            <span id="scoreText" class="score-number">0 / 0 encontrados</span>
        </div>

        <div class="grid-container" id="gridContainer"></div>

        <button class="reset-btn" onclick="resetGame()">🔄 Reiniciar e Zerar Quiz</button>
    </div>

    <!-- Modal: Mais Quizzes -->
    <div class="modal-overlay" id="quizzesModal">
        <div class="modal-card">
            <div class="modal-header">
                <span class="modal-title">🎯 Escolha um Quiz</span>
                <button class="close-btn" onclick="closeModal('quizzesModal')">&times;</button>
            </div>
            <div class="quiz-option-list">
                <div class="quiz-option-card" id="card-got" onclick="switchQuiz('got')">
                    <span class="quiz-icon">⚔️</span>
                    <div class="quiz-info">
                        <h3>Game of Thrones</h3>
                        <p>65 Personagens das grandes casas de Westeros</p>
                    </div>
                </div>
                <div class="quiz-option-card" id="card-coraline" onclick="switchQuiz('coraline')">
                    <span class="quiz-icon">🗝️</span>
                    <div class="quiz-info">
                        <h3>Coraline e o Mundo Secreto</h3>
                        <p>19 Moradores, elementos e segredos do Palácio Cor-de-Rosa</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal: Como Jogar -->
    <div class="modal-overlay" id="howToPlayModal">
        <div class="modal-card">
            <div class="modal-header">
                <span class="modal-title">📖 Como Jogar</span>
                <button class="close-btn" onclick="closeModal('howToPlayModal')">&times;</button>
            </div>
            <div style="line-height: 1.6; font-size: 14px;">
                <p style="margin-bottom: 12px;"><strong>1. Digite no campo de busca:</strong> À medida que você digita o nome correto de um personagem ou elemento, ele é reconhecido e preenchido na tabela automaticamente!</p>
                <p style="margin-bottom: 12px;"><strong>2. Sem se preocupar com acentos:</strong> O sistema aceita nomes sem acentos e apelidos populares.</p>
                <p style="margin-bottom: 12px;"><strong>3. Salvo automaticamente:</strong> Seu progresso é salvo no seu próprio navegador para você poder continuar a qualquer momento.</p>
            </div>
        </div>
    </div>

    <script>
        // Banco de dados dos Quizzes
        const allQuizzes = {
            got: {
                title: "⚔️ O Quiz Definitivo de Game of Thrones",
                subtitle: "O quanto você conhece do universo de GOT?",
                theme: "light",
                inputLabel: "Digite um nome do universo de GoT:",
                storageKey: "got_quiz_acertos",
                data: {
                    "O norte": [
                        { id: "jon", name: "Jon Snow", aliases: ["jon snow", "jon", "john", "john snow"] },
                        { id: "arya", name: "Arya Stark", aliases: ["arya stark", "arya"] },
                        { id: "sansa", name: "Sansa Stark", aliases: ["sansa stark", "sansa"] },
                        { id: "bran", name: "Bran Stark", aliases: ["bran stark", "bran", "brandon stark"] },
                        { id: "ned", name: "Ned Stark", aliases: ["ned stark", "ned", "eddard stark", "eddard"] },
                        { id: "robb", name: "Robb Stark", aliases: ["robb stark", "robb", "rob stark", "rob"] },
                        { id: "catelyn", name: "Catelyn Stark", aliases: ["catelyn stark", "catelyn", "cat stark"] },
                        { id: "rickon", name: "Rickon Stark", aliases: ["rickon stark", "rickon"] },
                        { id: "benjen", name: "Benjen Stark", aliases: ["benjen stark", "benjen"] },
                        { id: "lyanna", name: "Lyanna Stark", aliases: ["lyanna stark", "lyanna"] },
                        { id: "hodor", name: "Hodor", aliases: ["hodor", "walder"] },
                        { id: "tormund", name: "Tormund", aliases: ["tormund", "tormund giantsbane"] },
                        { id: "ygritte", name: "Ygritte", aliases: ["ygritte"] },
                        { id: "meera", name: "Meera Reed", aliases: ["meera reed", "meera"] },
                        { id: "jojen", name: "Jojen Reed", aliases: ["jojen reed", "jojen"] },
                        { id: "roose", name: "Roose Bolton", aliases: ["roose bolton", "roose"] },
                        { id: "ramsay", name: "Ramsay Bolton", aliases: ["ramsay bolton", "ramsay", "ramsey bolton", "ramsey"] },
                        { id: "theon", name: "Theon Greyjoy", aliases: ["theon greyjoy", "theon", "fedor", "reek"] }
                    ],
                    "Terras Ocidentais": [
                        { id: "tyrion", name: "Tyrion Lannister", aliases: ["tyrion lannister", "tyrion", "tyron", "tirion"] },
                        { id: "cersei", name: "Cersei Lannister", aliases: ["cersei lannister", "cersei", "cerse"] },
                        { id: "jaime", name: "Jaime Lannister", aliases: ["jaime lannister", "jaime", "jamie lannister", "jamie"] },
                        { id: "tywin", name: "Tywin Lannister", aliases: ["tywin lannister", "tywin"] },
                        { id: "joffrey", name: "Joffrey Baratheon", aliases: ["joffrey baratheon", "joffrey", "jofrey"] },
                        { id: "myrcella", name: "Myrcella Baratheon", aliases: ["myrcella baratheon", "myrcella"] },
                        { id: "tommen", name: "Tommen Baratheon", aliases: ["tommen baratheon", "tommen"] },
                        { id: "robert", name: "Robert Baratheon", aliases: ["robert baratheon", "robert"] },
                        { id: "sandor", name: "Sandor Clegane", aliases: ["sandor clegane", "sandor", "cao de caca", "hound", "the hound"] },
                        { id: "gregor", name: "Gregor Clegane", aliases: ["gregor clegane", "gregor", "montanha", "mountain", "the mountain"] },
                        { id: "bronn", name: "Bronn", aliases: ["bronn"] },
                        { id: "petyr", name: "Petyr Baelish", aliases: ["petyr baelish", "petyr", "minhocao", "littlefinger", "dedinho"] },
                        { id: "varys", name: "Varys", aliases: ["varys", "aranha"] },
                        { id: "qyburn", name: "Qyburn", aliases: ["qyburn"] },
                        { id: "podrick", name: "Podrick Payne", aliases: ["podrick payne", "podrick", "pod"] },
                        { id: "lancel", name: "Lancel Lannister", aliases: ["lancel lannister", "lancel"] },
                        { id: "pycelle", name: "Grand Maester Pycelle", aliases: ["pycelle", "maester pycelle", "grand maester pycelle"] }
                    ],
                    "Terras da Coroa (Targaryen)": [
                        { id: "daenerys", name: "Daenerys Targaryen", aliases: ["daenerys targaryen", "daenerys", "dany", "khaleesi"] },
                        { id: "viserys", name: "Viserys Targaryen", aliases: ["viserys targaryen", "viserys"] },
                        { id: "rhaenyra", name: "Rhaenyra Targaryen", aliases: ["rhaenyra targaryen", "rhaenyra"] },
                        { id: "daemon", name: "Daemon Targaryen", aliases: ["daemon targaryen", "daemon"] },
                        { id: "viserys1", name: "Viserys I Targaryen", aliases: ["viserys i", "viserys 1", "rei viserys"] },
                        { id: "aemond", name: "Aemond Targaryen", aliases: ["aemond targaryen", "aemond"] },
                        { id: "aegon2", name: "Aegon II Targaryen", aliases: ["aegon ii", "aegon 2", "aegon targaryen", "aegon"] },
                        { id: "alicent", name: "Alicent Hightower", aliases: ["alicent hightower", "alicent"] },
                        { id: "otto", name: "Otto Hightower", aliases: ["otto hightower", "otto"] },
                        { id: "corlys", name: "Corlys Velaryon", aliases: ["corlys velaryon", "corlys", "sea snake", "serpente do mar"] },
                        { id: "rhaenys", name: "Rhaenys Targaryen", aliases: ["rhaenys targaryen", "rhaenys"] },
                        { id: "criston", name: "Criston Cole", aliases: ["criston cole", "criston", "cole"] },
                        { id: "rhaegar", name: "Rhaegar Targaryen", aliases: ["rhaegar targaryen", "rhaegar"] },
                        { id: "aerys", name: "Aerys II Targaryen", aliases: ["aerys targaryen", "aerys", "rei louco", "mad king"] },
                        { id: "jacaerys", name: "Jacaerys Velaryon", aliases: ["jacaerys velaryon", "jacaerys", "jace"] },
                        { id: "helaena", name: "Helaena Targaryen", aliases: ["helaena targaryen", "helaena"] }
                    ],
                    "Grandes Casas de Westeros": [
                        { id: "stannis", name: "Stannis Baratheon", aliases: ["stannis baratheon", "stannis"] },
                        { id: "renly", name: "Renly Baratheon", aliases: ["renly baratheon", "renly"] },
                        { id: "margaery", name: "Margaery Tyrell", aliases: ["margaery tyrell", "margaery", "margery"] },
                        { id: "olenna", name: "Olenna Tyrell", aliases: ["olenna tyrell", "olenna", "rainha dos espinhos"] },
                        { id: "loras", name: "Loras Tyrell", aliases: ["loras tyrell", "loras"] },
                        { id: "mace", name: "Mace Tyrell", aliases: ["mace tyrell", "mace"] },
                        { id: "oberyn", name: "Oberyn Martell", aliases: ["oberyn martell", "oberyn", "vibora vermelha", "red viper"] },
                        { id: "ellaria", name: "Ellaria Sand", aliases: ["ellaria sand", "ellaria"] },
                        { id: "doran", name: "Doran Martell", aliases: ["doran martell", "doran"] },
                        { id: "yara", name: "Yara Greyjoy", aliases: ["yara greyjoy", "yara", "asha greyjoy"] },
                        { id: "euron", name: "Euron Greyjoy", aliases: ["euron greyjoy", "euron"] },
                        { id: "balon", name: "Balon Greyjoy", aliases: ["balon greyjoy", "balon"] },
                        { id: "lysa", name: "Lysa Arryn", aliases: ["lysa arryn", "lysa"] },
                        { id: "robin", name: "Robin Arryn", aliases: ["robin arryn", "robin", "sweetrobin"] }
                    ]
                }
            },
            coraline: {
                title: "🗝️ Coraline e o Mundo Secreto",
                subtitle: "Lembre o nome de todos os moradores e elementos do Palácio Cor-de-Rosa!",
                theme: "dark",
                inputLabel: "Digite um nome ou elemento de Coraline:",
                storageKey: "coraline_quiz_acertos_v1",
                data: {
                    "Principais & Família": [
                        { id: "coraline", name: "Coraline Jones", aliases: ["coraline jones", "coraline", "caroline"] },
                        { id: "mae_real", name: "Mel Jones (Mãe)", aliases: ["mel jones", "mel", "mae", "mae da coraline", "melanie jones"] },
                        { id: "pai_real", name: "Charlie Jones (Pai)", aliases: ["charlie jones", "charlie", "pai", "pai da coraline"] },
                        { id: "wybie", name: "Wybie Lovat", aliases: ["wybie lovat", "wybie", "wyborn", "wyborn lovat"] },
                        { id: "gato", name: "O Gato Preto", aliases: ["o gato preto", "gato preto", "gato", "o gato"] }
                    ],
                    "Vizinhos": [
                        { id: "bobinsky", name: "Sr. Bobinsky", aliases: ["sr bobinsky", "bobinsky", "sergei alexander bobinsky", "senhor bobinsky", "sergei bobinsky"] },
                        { id: "spink", name: "Srta. Spink", aliases: ["srta spink", "spink", "miss spink", "april spink"] },
                        { id: "forcible", name: "Srta. Forcible", aliases: ["srta forcible", "forcible", "miss forcible", "miriam forcible"] },
                        { id: "avo_wybie", name: "Avó do Wybie", aliases: ["avo do wybie", "avo", "sra lovat", "mrs lovat", "avo wybie"] }
                    ],
                    "Outro Mundo": [
                        { id: "beldam", name: "Outra Mãe (Beldam)", aliases: ["outra mae", "beldam", "a outra mae", "outra mae beldam"] },
                        { id: "outro_pai", name: "Outro Pai", aliases: ["outro pai", "o outro pai"] },
                        { id: "outro_wybie", name: "Outro Wybie", aliases: ["outro wybie", "o outro wybie"] },
                        { id: "outro_bobinsky", name: "Outro Bobinsky", aliases: ["outro bobinsky", "o outro bobinsky"] },
                        { id: "outra_spink", name: "Outra Spink", aliases: ["outra spink", "a outra spink"] },
                        { id: "outra_forcible", name: "Outra Forcible", aliases: ["outra forcible", "a outra forcible"] }
                    ],
                    "Elementos & Espíritos": [
                        { id: "fantasmas", name: "Crianças Fantasmas", aliases: ["criancas fantasmas", "fantasmas", "criancas fantasma", "fantasma"] },
                        { id: "ratos", name: "Ratos Saltadores", aliases: ["ratos saltadores", "camundongos", "ratos", "camundongos saltadores"] },
                        { id: "chave", name: "Chave de Botão", aliases: ["chave de botao", "chave"] },
                        { id: "pedra", name: "Pedra Furada", aliases: ["pedra furada", "pedra", "pedra com furo"] },
                        { id: "boneca", name: "Boneca de Pano", aliases: ["boneca de pano", "boneca", "boneca da coraline"] },
                        { id: "palacio", name: "Palácio Cor-de-Rosa", aliases: ["palacio cor de rosa", "palacio cor-de-rosa", "palacio rosa", "casa"] }
                    ]
                }
            }
        };

        // Estado Atual
        let currentQuizKey = localStorage.getItem('lovewens_active_quiz') || 'got';
        let foundSet = new Set();
        let totalCharacters = 0;

        const gridContainer = document.getElementById('gridContainer');
        const searchInput = document.getElementById('quizInput');
        const scoreText = document.getElementById('scoreText');

        function normalizeString(str) {
            return str.toLowerCase()
                      .normalize("NFD")
                      .replace(/[\u0300-\u036f]/g, "")
                      .trim();
        }

        // Troca de Quiz
        function switchQuiz(quizKey) {
            currentQuizKey = quizKey;
            localStorage.setItem('lovewens_active_quiz', quizKey);

            const quiz = allQuizzes[quizKey];

            // Atualiza tema do body
            if (quiz.theme === 'dark') {
                document.body.classList.add('dark-theme');
            } else {
                document.body.classList.remove('dark-theme');
            }

            // Atualiza textos da interface
            document.getElementById('quizTitle').innerText = quiz.title;
            document.getElementById('quizSubtitle').innerText = quiz.subtitle;
            document.getElementById('inputLabelText').innerText = quiz.inputLabel;

            // Destaque do card no modal
            document.querySelectorAll('.quiz-option-card').forEach(card => card.classList.remove('active'));
            const activeCard = document.getElementById('card-' + quizKey);
            if (activeCard) activeCard.classList.add('active');

            // Carrega respostas salvas
            foundSet = new Set(JSON.parse(localStorage.getItem(quiz.storageKey) || '[]'));

            // Calcula total do quiz
            totalCharacters = 0;
            Object.values(quiz.data).forEach(group => {
                totalCharacters += group.length;
            });

            closeModal('quizzesModal');
            renderGrid();
        }

        // Renderiza a grade de colunas
        function renderGrid() {
            gridContainer.innerHTML = '';
            const quiz = allQuizzes[currentQuizKey];

            Object.entries(quiz.data).forEach(([groupName, characters]) => {
                const colBox = document.createElement('div');
                colBox.className = 'column-box';

                const header = document.createElement('div');
                header.className = 'column-header';
                header.innerText = groupName;
                colBox.appendChild(header);

                characters.forEach(char => {
                    const cell = document.createElement('div');
                    cell.id = 'cell-' + char.id;
                    
                    if (foundSet.has(char.id)) {
                        cell.className = 'cell cell-found';
                        cell.innerText = char.name;
                    } else {
                        cell.className = 'cell cell-empty';
                        cell.innerText = '---';
                    }

                    colBox.appendChild(cell);
                });

                gridContainer.appendChild(colBox);
            });

            updateScore();
        }

        function updateScore() {
            scoreText.innerText = `${foundSet.size} / ${totalCharacters} encontrados`;
        }

        // Listener de validação ao digitar
        searchInput.addEventListener('input', (e) => {
            const typedVal = normalizeString(e.target.value);
            if (!typedVal) return;

            const quiz = allQuizzes[currentQuizKey];

            for (const [group, characters] of Object.entries(quiz.data)) {
                for (const char of characters) {
                    if (!foundSet.has(char.id)) {
                        const isMatch = char.aliases.some(alias => normalizeString(alias) === typedVal);
                        
                        if (isMatch) {
                            foundSet.add(char.id);
                            localStorage.setItem(quiz.storageKey, JSON.stringify(Array.from(foundSet)));
                            
                            const cell = document.getElementById('cell-' + char.id);
                            if (cell) {
                                cell.className = 'cell cell-found';
                                cell.innerText = char.name;
                            }

                            searchInput.value = '';
                            updateScore();
                            return;
                        }
                    }
                }
            }
        });

        // Reset do jogo ativo
        let isResetting = false;
        function resetGame() {
            const btn = document.querySelector('.reset-btn');
            if (!isResetting) {
                isResetting = true;
                btn.innerText = "⚠️ Clique para confirmar zerar";
                setTimeout(() => {
                    isResetting = false;
                    btn.innerText = "🔄 Reiniciar e Zerar Quiz";
                }, 3000);
            } else {
                const quiz = allQuizzes[currentQuizKey];
                foundSet.clear();
                localStorage.removeItem(quiz.storageKey);
                searchInput.value = '';
                btn.innerText = "🔄 Reiniciar e Zerar Quiz";
                isResetting = false;
                renderGrid();
            }
        }

        // Controles dos Modais
        function openModal(id) {
            document.getElementById(id).classList.add('active');
        }

        function closeModal(id) {
            document.getElementById(id).classList.remove('active');
        }

        // Inicializar com o quiz selecionado
        switchQuiz(currentQuizKey);
    </script>
</body>
</html>
"""

components.html(html_code, height=1200, scrolling=True)
