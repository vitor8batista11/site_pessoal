import streamlit as st

def projeto_componente(nome, descricao, link, confidencial = False):
    with st.expander(nome):
        st.write(descricao)
        if not confidencial:
            st.write(f"**Link de Acesso:** [{nome}]( {link})")

# Título da página
st.title("Página Pessoal - Vítor Batista")

# Seção "Sobre Mim"
st.header("Sobre Mim")
st.markdown('<span style="font-size: 18px;">Sou um entusiasta da estatística. Para mim, números são como quebra-cabeças esperando para serem resolvidos. Formei-me em Estatística na UFMG e atualmente estou buscando aprimorar meus conhecimentos no mestrado da UNICAMP. Adoro transformar dados em soluções práticas e resolver problemas do mundo real. Se você precisa de ajuda com seus dados, não hesite em me contatar. Vamos conversar e encontrar soluções juntos!</span>', unsafe_allow_html=True)

# Seção "Projetos"
st.header("Projetos")
st.markdown('<span style="font-size: 18px;">Aqui estão alguns dos meus projetos:</span>', unsafe_allow_html=True)

col1, col2 = st.columns((1,1))
with col1:
    projeto_componente(
        nome="Complexidade de Textos",
        descricao="Este projeto foi meu TCC na graduação. Sob orientação do professor José Francisco Soares, criei uma plataforma que calcula a complexidade de textos infantis, para auxiliar na seleção de textos que serão expostos às crianças que estão sendo alfabetizadas.",
        link="https://vitorbatista.shinyapps.io/portal_textos/")
    projeto_componente(
        nome="Acidentes Rodoviários",
        descricao="Construí um dashboard para analisar os dados públicos de acidentes rodoviários no Brasil entre 2007 e 2020.",
        link="https://vitorbatista.shinyapps.io/acidentes/")
    projeto_componente(
        nome="Aprendizado de Frações",
        descricao="Atuei como consultor em um projeto que visava verificar a eficácia de uma nova metodologia para o ensino de frações (tópico de matemática básica) a alunos do ensino fundamental. A solução final foi o ajuste de uma Regressão Poisson com efeitos aleatórios.",
        link="",
        confidencial=True)

with col2:
    projeto_componente(
        nome="Insuficiência Cardíaca",
        descricao="Atuei como consultor em um projeto que visava verificar a relação entre o perfil hemodinâmico de pacientes admitidos com insuficiência cardíaca e a mortalidade. A solução final foi o ajuste de uma Regressão Logística.",
        link="",
        confidencial=True)
    projeto_componente(
        nome="Impactos da COVID-19 na Gravidez",
        descricao="Atuei como consultor em um projeto que visava mensurar os impactos do COVID-19 em diversos marcadores biológicos de mulheres grávidas. Como os dados não são públicos, não posso divulgar mais informações sobre esse projeto.",
        link="",
        confidencial=True)
    projeto_componente(
        nome="Burnout em Árbitros de Volei",
        descricao="Atuei como consultor em um projeto que visava verificar como as estratégias de enfrentamento utilizadas por árbitros de vôlei impactavam seus níveis de burnout. A solução final foi o ajuste de uma Regressão Poisson.",
        link="",
        confidencial=True)

# Seção "Habilidades"
st.header("Habilidades")
st.markdown('''<span style="font-size: 18px;">Minhas habilidades incluem:<ul>
                <li>Conhecimentos avançados em estatística</li>
                <li>R e Python avançados</li>
                <li>Experiência com Machine Learning</li>
                <li>Experiência com SQL, GitHub e AWS</li>
                <li>I speak english at an advanced level</li>
                <li>Je parle le français aussi!</li>
            </ul></span>''', unsafe_allow_html=True)

# Seção "Contato"
st.header("Contato")
st.markdown('<span style="font-size: 18px;">Você pode entrar em contato comigo por email: vitor8batista11@gmail.com</span>', unsafe_allow_html=True)