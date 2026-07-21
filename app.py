import streamlit as st
import streamlit.components.v1 as components

# Configuração inicial da página Streamlit
st.set_page_config(
    page_title="GoT Character Quiz",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #ffffff;
            color: #0f172a;
            padding: 0;
            margin: 0;
            padding-bottom: 40px;
        }

        /* Cabeçalho superior azul com menu */
        .header-container {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 16px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            margin-bottom: 25px;
        }

        .header-logo {
            font-size: 22px;
            font-weight: 800;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 10px;
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
            transition: color 0.2s;
        }

        .menu-item:hover {
            color: #ffd700 !important;
        }

        .login-btn {
            background-color: #ffffff;
            color: #1e3c72 !important;
            padding: 6px 18px;
            border-radius: 20px;
            font-weight: 700;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        /* Conteúdo central */
        .main-content {
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 20px;
        }

        h1 {
            color: #0f172a;
            font-size: 26px;
            margin-bottom: 6px;
            font-weight: 800;
        }

        p.subtitle {
            color: #475569;
            font-size: 15px;
            margin-bottom: 20px;
        }

        /* Caixa de busca / input */
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

        .search-input {
            width: 100%;
            padding: 14px 18px;
            font-size: 16px;
            border: 2px solid #94a3b8;
            border-radius: 8px;
            background-color: #f8fafc;
            color: #0f172a;
            outline: none;
            transition: all 0.2s ease;
        }

        .search-input:focus {
            border-color: #2a5298;
            background-color: #ffffff;
            box-shadow: 0 0 0 3px rgba(42, 82, 152, 0.15);
        }

        /* Placar de progresso */
        .score-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #f1f5f9;
            border: 1px solid #cbd5e1;
            padding: 12px 20px;
            border-radius: 8px;
            margin-bottom: 25px;
        }

        .score-title {
            font-size: 14px;
            color: #475569;
            font-weight: 600;
        }

        .score-number {
            font-size: 24px;
            font-weight: 800;
            color: #1e3c72;
        }

        /* Grade de colunas */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
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
        }

        .column-header {
            background-color: #2a5298;
            color: #ffffff;
            padding: 12px 8px;
            text-align: center;
            font-weight: 700;
            font-size: 13px;
            border-radius: 6px 6px 0 0;
            min-height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Células da tabela com bordas nítidas */
        .cell {
            border-left: 1px solid #b0b0b0;
            border-right: 1px solid #b0b0b0;
            border-bottom: 1px solid #b0b0b0;
            padding: 9px 6px;
            text-align: center;
            font-size: 13px;
            transition: background-color 0.25s, color 0.25s;
        }

        .cell-empty {
            background-color: #fafafa;
            color: #cbd5e1;
        }

        .cell-found {
            background-color: #e6f4ea;
            color: #137333;
            font-weight: 800;
        }

        .reset-btn {
            background-color: #ef4444;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 10px;
            transition: background-color 0.2s;
        }

        .reset-btn:hover {
            background-color: #dc2626;
        }
    </style>
</head>
<body>

    <!-- Header Azul -->
    <div class="header-container">
        <div class="header-logo">🛡️ PORTAL QUIZ</div>
        <div class="header-menu">
            <span class="menu-item">Início</span>
            <span class="menu-item">Mais Quizzes</span>
            <span class="menu-item">Como Jogar</span>
            <span class="menu-item login-btn">Entrar</span>
        </div>
    </div>

    <div class="main-content">
        <h1>⚔️ Quiz de Personagens: Universo de Game of Thrones</h1>
        <p class="subtitle">Digite o nome dos personagens (aceita o primeiro nome ou apelidos como Dany, Jon, Tyrion, Sansa)!</p>

        <!-- Input com escuta instantânea -->
        <div class="input-group">
            <label class="input-label" for="quizInput">Digite o nome de um personagem:</label>
            <input 
                type="text" 
                id="quizInput" 
                class="search-input"  
                autocomplete="off"
                autofocus
            />
        </div>

        <!-- Placar -->
        <div class="score-container">
            <span class="score-title">📊 Seu Progresso Atual</span>
            <span id="scoreText" class="score-number">0 / 80 encontrados</span>
        </div>

        <!-- Grade com os nomes e casas -->
        <div class="grid-container" id="gridContainer"></div>

        <button class="reset-btn" onclick="resetGame()">🔄 Reiniciar e Zerar Quiz</button>
    </div>

    <script>
        const quizData = {
            "Casa Stark & Norte": [
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
            "Casa Lannister & Coroa": [
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
            "Casa Targaryen & Dragões": [
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
            ],
            "Essos & Aliados Importantes": [
                { id: "jorah", name: "Jorah Mormont", aliases: ["jorah mormont", "jorah"] },
                { id: "brienne", name: "Brienne de Tarth", aliases: ["brienne de tarth", "brienne", "briene"] },
                { id: "samwell", name: "Samwell Tarly", aliases: ["samwell tarly", "samwell", "sam tarly", "sam"] },
                { id: "davos", name: "Davos Seaworth", aliases: ["davos seaworth", "davos", "cavaleiro das cebolas", "onion knight"] },
                { id: "melisandre", name: "Melisandre", aliases: ["melisandre", "mulher vermelha", "red woman"] },
                { id: "barristan", name: "Barristan Selmy", aliases: ["barristan selmy", "barristan", "barristan o ousado"] },
                { id: "missandei", name: "Missandei", aliases: ["missandei"] },
                { id: "greyworm", name: "Verme Cinzento", aliases: ["verme cinzento", "grey worm"] },
                { id: "drogo", name: "Khal Drogo", aliases: ["khal drogo", "drogo"] },
                { id: "syrio", name: "Syrio Forel", aliases: ["syrio forel", "syrio"] },
                { id: "jaqen", name: "Jaqen H'ghar", aliases: ["jaqen hghar", "jaqen h'ghar", "jaqen"] },
                { id: "daario", name: "Daario Naharis", aliases: ["daario naharis", "daario"] },
                { id: "gendry", name: "Gendry Baratheon", aliases: ["gendry baratheon", "gendry"] },
                { id: "shae", name: "Shae", aliases: ["shae"] },
                { id: "gilly", name: "Gilly", aliases: ["gilly"] }
            ]
        };

        let foundSet = new Set(JSON.parse(localStorage.getItem('got_quiz_acertos') || '[]'));
        let totalCharacters = 0;

        // Calcular total de personagens
        Object.values(quizData).forEach(group => {
            totalCharacters += group.length;
        });

        const gridContainer = document.getElementById('gridContainer');
        const searchInput = document.getElementById('quizInput');
        const scoreText = document.getElementById('scoreText');

        // Normalização para ignorar acentos e maiúsculas
        function normalizeString(str) {
            return str.toLowerCase()
                      .normalize("NFD")
                      .replace(/[\u0300-\u036f]/g, "")
                      .trim();
        }

        // Renderizar a grade inicial
        function renderGrid() {
            gridContainer.innerHTML = '';

            Object.entries(quizData).forEach(([houseName, characters]) => {
                const colBox = document.createElement('div');
                colBox.className = 'column-box';

                const header = document.createElement('div');
                header.className = 'column-header';
                header.innerText = houseName;
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

        // ESCUTA EM TEMPO REAL A CADA LETRA DIGITADA
        searchInput.addEventListener('input', (e) => {
            const typedVal = normalizeString(e.target.value);
            if (!typedVal) return;

            // Percorre todas as casas e personagens
            for (const [house, characters] of Object.entries(quizData)) {
                for (const char of characters) {
                    if (!foundSet.has(char.id)) {
                        // Verifica se o texto bate com qualquer um dos apelidos/primeiros nomes
                        const isMatch = char.aliases.some(alias => normalizeString(alias) === typedVal);
                        
                        if (isMatch) {
                            // ACERTOU!
                            foundSet.add(char.id);
                            localStorage.setItem('got_quiz_acertos', JSON.stringify(Array.from(foundSet)));
                            
                            // Atualiza a célula instantaneamente na tela
                            const cell = document.getElementById('cell-' + char.id);
                            if (cell) {
                                cell.className = 'cell cell-found';
                                cell.innerText = char.name;
                            }

                            // Limpa a caixa de texto de imediato sem apertar Enter!
                            searchInput.value = '';
                            updateScore();
                            return;
                        }
                    }
                }
            }
        });

        function resetGame() {
            if (confirm("Deseja realmente zerar o jogo?")) {
                foundSet.clear();
                localStorage.removeItem('got_quiz_acertos');
                searchInput.value = '';
                renderGrid();
            }
        }

        // Inicializar a tela
        renderGrid();
    </script>
</body>
</html>
"""

components.html(html_code, height=1300, scrolling=True)
