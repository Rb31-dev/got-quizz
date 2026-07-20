import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="GoT Quiz", layout="wide")

st.title("⚔️ Quiz: Personagens de Game of Thrones")
st.write("Digite o máximo de personagens que você lembrar do universo de GoT e House of the Dragon!")

# 2. Banco de dados de personagens (Você pode adicionar quantos quiser aqui!)
# Deixe sempre em letras minúsculas aqui para facilitar a validação
gabarito = {
    "Casa Stark": ["jon snow", "arya stark", "sansa stark", "bran stark", "ned stark", "robb stark", "catelyn stark"],
    "Casa Lannister": ["tyrion lannister", "cersei lannister", "jaime lannister", "tywin lannister", "joffrey baratheon"],
    "Casa Targaryen": ["daenerys targaryen", "viserys targaryen", "rhaenyra targaryen", "daemon targaryen", "aemond targaryen"],
    "Outros / Aliados": ["brianne de tarth", "samwell tarly", "petyr baelish", "varys", "sandor clegane", "jorah mormont"]
}

# Criar uma lista única com todos os nomes válidos para checagem rápida
todos_personagens = []
for lista in gabarito.values():
    todos_personagens.extend(lista)

# 3. Inicializar o estado do jogo (para não apagar os acertos quando a página recarregar)
if "acertos" not in st.session_state:
    st.session_state.acertos = []

# 4. Campo de texto para o usuário digitar
# O uso de .lower().strip() remove espaços extras e ignora letras maiúsculas/minúsculas
resposta_usuario = st.text_input("Digite o nome de um personagem:", value="").lower().strip()

# 5. Lógica de validação
if resposta_usuario:
    if resposta_usuario in todos_personagens:
        if resposta_usuario not in st.session_state.acertos:
            st.session_state.acertos.append(resposta_usuario)
            st.success(f"Boa! Você acertou um!")
            # Recarrega a página para limpar o campo de texto automaticamente
            st.rerender()
        else:
            st.warning("Você já acertou esse!")
    else:
        st.error("Nome incorreto ou não cadastrado.")

# Mostrar o placar atual
total_personagens = len(todos_personagens)
total_acertos = len(st.session_state.acertos)
st.metric(label="Seu Placar", value=f"{total_acertos} / {total_personagens}")

st.write("---")

# 6. Criar as colunas visuais (igual ao seu exemplo)
colunas_interface = st.columns(len(gabarito))

# Preencher cada coluna com as Casas e os nomes (em verde se acertou, em branco se não)
for i, (casa, personagens) in enumerate(gabarito.items()):
    with colunas_interface[i]:
        # Cabeçalho da coluna (estilizado em azul)
        st.markdown(
            f"<div style='background-color:#2b5cbe; color:white; padding:10px; text-align:center; font-weight:bold; border-radius:5px 5px 0px 0px;'>{casa}</div>", 
            unsafe_allow_html=True
        )
        
        # Lista os personagens daquela categoria
        for p in personagens:
            if p in st.session_state.acertos:
                # Se acertou, mostra o nome em verde e negrito
                st.markdown(
                    f"<div style='border: 1px solid #ddd; padding: 8px; background-color: #e6f4ea; color: #137333; font-weight: bold; text-align:center;'>{p.title()}</div>", 
                    unsafe_allow_html=True
                )
            else:
                # Se não acertou, deixa o espaço em branco (ou com linhas vazias igual ao seu exemplo)
                st.markdown(
                    "<div style='border: 1px solid #ddd; padding: 8px; color: transparent; text-align:center;'>---</div>", 
                    unsafe_allow_html=True
                )

# Botão para resetar o jogo se quiser começar de novo
if st.button("Reiniciar Jogo"):
    st.session_state.acertos = []
    st.rerender()
