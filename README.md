<h1> 👾🎮 Space Defender </h1>
<br id="inicio">
<h2> :beginner: Sobre o projeto </h2>
<h4> Space Defender é um projeto com o intuito de produzir um jogo baseado no estilo space invaders, para praticar programação em Python. </h4>

<h2> :page_with_curl: Sobre o jogo </h2>
<h4> O Planeta Terra está prestes a ser invadido por uma grande frota de naves alienígenas, os extra-terrestres possuem o objetivo de destruir a humanidade e dominar completamente o planeta, e você, como o último piloto de elite na Terra, foi convocado para pilotar uma das naves espaciais mais poderosas já construídas, a "Space Defender". </h4>
<h4> O Chefe da maior agência espacial do mundo te deu um passe livre para chamar algum parceiro de confiança para essa missão, mas cuidado para não atingí-lo. </h4> 
<h4> Seu principal objetivo é enfrentar as hordas de naves alienígenas e manter a segurança do planeta (por enquanto). </h4>

<h2> 📌 Status do projeto </h2>
<h4> :white_check_mark: Concluído </h4>
<h4> 📅 Lançamento: 01/07/2023 </h4>

<h2> 🖥️ Tecnologia utilizada </h2>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<h2> 🕹️ Controles </h2>
<table>
  <th> Tecla </th>
  <th> Função </th>
  <tr>
    <td> Movimentação da nave (Player 1) </td>
    <td> W, A, S, D</td>
  </tr>
  <tr>
    <td align = center> Atirar (Player 1) </td>
    <td align = center> Espaço </td>
  </tr>
  <tr>
      <td> Movimentação da nave (Player 2) </td>
      <td> ⬆️ ⬅️ ⬇️ ➡️ </td>
  </tr>
  <tr>
      <td align=center> Atirar (Player 2) </td>
      <td align=center> Backspace ⬅️ </td>
  </tr>
  <tr>
    <td align= center>Jogar novamente </td>
    <td align=center> R </td>
  </tr>
</table>

<h2> 🎮 Como rodar o jogo</h2>
<h3> Opção 1 - Download do executável </h3>
<h4> 1. Acesse este link <a href="https://drive.google.com/drive/folders/19oQuNZC7s2HQzrWJwa-HCl4a_pUpXVhT?usp=sharing"> aqui </a> </h4>
<h4> 2. Baixe todos os arquivos da pasta e aguarde o download </h4>
<h4> 3. Clique na setinha para cima  e depois em "Mostrar na pasta" </h4>
<h4> 4. Após entrar na pasta "Downloads", clique com o botão direito na pasta compactada e extraia </h4>
<h5> 4.1 A opção pode variar de acordo com o sistema operacional, "Extrair aqui", "Extrair tudo". </h5>
<h4> 5. Depois de extraído, abra o SpaceDefender.exe </h4>
<h4> 6. Divirta-se! </h4>
<br>
<h3> Opção 2 - Clonar repositório </h3>
<h4> 1. É preciso que você possua o <a href="https://git-scm.com/downloads"> Git </a> e o <a href="https://www.python.org/downloads/"> Python </a> instalado. </h4>
<h4> 2. Pesquise por terminal na barra de tarefas  do seu dispositivo e abra o terminal. </h4>
<h4> 3. Clone o repositório inserindo este comando: </h4>

    git clone https://github.com/velipefieira/SpaceDefender.git

<h4> 4. Após clonar o repositório, entre na pasta do projeto. </h4>

    cd SpaceDefender

<h4> 5. Se preferir, crie um ambiente virtual para rodar o jogo com os seguintes comandos (opcional): </h4>

    python -m venv venv

<h4> 5.1 Caso tenha criado o ambiente virtual, ligue-o com o seguinte comando: </h4>

    .\venv\Scripts\activate

<h6> 5.2 Caso esteja utilizando um sistema operacional linux, utilize o seguinte comando: </h3>

    source venv\bin\activate

<h4> 6. Instale os requisitos para rodar o jogo utilizando o seguinte comando: </h4>

    python -r requirements.txt
    
<h4> 7. Rode o jogo com o seguinte comando e se divirta! </h4>

    python main.py
    
<h2> Esta é a aparência do jogo </h2>
<img src="/doc/v1_0.gif"/>

<h2> Versões criadas até o momento </h2>
<table>
  <th>
    Nome versão
  </th>
  <th>
    Tag
  </th>
  <tr>
    <td>
      Beta 1.0
    </td>
    <td align = center>
      <a href="https://github.com/velipefieira/SpaceDefender/tree/Beta1.0"> 🎟️ </a>
    </td>
  </tr>
  <tr>
    <td> Beta 1.1 </td>
    <td align = center>
      <a href="https://github.com/velipefieira/SpaceDefender/tree/Beta1.1"> 🎟️ </a>
    </td>
  </tr>
  <tr>
      <td> Beta 2.0 </td>
      <td align=center>
          <a href="https://github.com/velipefieira/SpaceDefender/tree/Beta2.0"> 🎟️ </a>
      </td>
  </tr>
    <tr>
      <td> V 1.0 </td>
      <td align=center>
          <a href="https://github.com/velipefieira/SpaceDefender/tree/V1.0"> 🎟️ </a>
      </td>
  </tr>
</table>

<h2> </h2>

<h2> Elementos do jogo </h2>
<table>
  <th> Nome </th>
  <th> Descrição </th>
  <th> Imagem </th>
  <tr>
    <td> Player </td>
    <td> Esta é a nave que você controla, você possui inicialmente 3 vidas, podendo ganhar ou perder vidas ao decorrer do jogo </td>
    <td align="center"> <img src="imgs/player.png" width="40px"/>
  </tr>
  <tr>
    <td> Míssil </td>
    <td> Este é o projetil que você pode lançar para destruir inimigos, podendo ser lançado apenas um por vez </td>
    <td align="center"> <img src="imgs/missil.png" width="40px"/>
  </tr>
  <tr>
    <td> Vida </td>
    <td> Este é o elemento que define a vida do jogador, o jogo termina após ela chegar em 0.</td>
    <td align="center"> <img src="imgs/vida.png" width="40px">
  </tr>
  <tr>
    <td> Alien Verde </td>
    <td> Este é o inimigo inicial, disponível logo após iniciar o jogo </td>
    <td align="center"> <img src="imgs/alienvd.png" width="40px">
  </tr>
  <tr>
    <td> Alien Azul </td>
    <td> Este é o inimigo "nível 2", disponível logo após alcançar a marca de 20 pontos </td>
    <td align="center"> <img src="imgs/alienaz.png" width="40px">
  </tr>
  <tr>
    <td> Alien Vermelho </td>
    <td> Este é o inimigo "nível 3", disponível logo após alcançar a marca de 40 pontos </td>
    <td align="center"> <img src="imgs/alienvm.png" width="40px">
  </tr>
  <tr>
    <td> Alien Cinza </td>
    <td> Este é o inimigo "nível 4", disponível logo após alcançar a marca de 60 pontos </td>
    <td align="center"> <img src="imgs/alienci.png" width="40px">
  </tr>
  <tr>
    <td> (Un)Lucky Item </td>
    <td> Este é um item misterioso, gerado ocasionalmente na gameplay, o qual pode oferecer efeitos positivos, como ganho de vida, velocidade e pontos, ou efeitos negativos, como perda de vida ou velocidade. </td>
    <td align="center"> <img src="imgs/lucky.png" width="40px">
  </tr>
  <tr>
     <td> Meteoros </td> 
      <td> Uma chuva de meteoros pode ser iniciada após pegar um (Un)Lucky Item, não é possível destruí-los e eles podem ser muito mais fortes do que você imagina. </td>
      <td align="center"> <img src="imgs/meteoro.png" width="40px"> </td>
  </tr>


</table>

<h3> :hammer: Funcionalidades </h3>
<table>
  <th> Nome </th>
  <th> Descrição </th>
  <th> Status </th>
  <tr>
    <td> Movimentação </td>
    <td> Controlar a nave por W, A, S, D ou setinhas </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
  <tr>
    <td> Disparo de projéteis </td>
    <td> Disparar projéteis que destruam as naves alienígenas </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
  <tr>
    <td> Inimigos </td>
    <td> Naves alienígenas que voam em direção ao player </td>
    <td> :white_check_mark: Concluído <td>
  </tr>
  <tr>
    <td> Sistema de vida e pontuação </td>
    <td> Perder vida ao ser atingido e ganhar pontos ao destruir uma nave alienígena </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
    <tr> 
    <td> Sistema de jogar novamente </td>
    <td> Permitir o usuário reiniciar o jogo clicando "R" </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
  <tr>
    <td> Interface gráfica </td>
    <td> Exibição da hud do jogo </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
  <tr>
    <td> Sistema de fases e progresso </td>
    <td> Permitir que sejam gerados mais inimigos ao passar do tempo </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
  <tr>
    <td> Geração de obstáculos </td>
    <td> Criar obstáculos que aparecem durante a gameplay, ex: Meteoros. </td>
    <td> :white_check_mark: Concluído </td>
  </tr>
  <tr>
    <td> Sistema de power-ups </td>
    <td> Permitir que o usuário colete power-ups de poder ou vida ao decorrero do jogo. </td>
    <td> :white_check_mark: Concluído </td>
 </tr>
   <tr>
    <td> Som e Áudio </td>
    <td> Música e efeitos sonoros que permitem uma maior imersão na gameplay </td>
    <td> :white_check_mark: Concluído  </td>
  </tr>
 <tr>
   <td> Multiplayer local </td>
   <td> Tornar disponíveis a gameplay para 1 ou 2 players </td>
   <td> :white_check_mark: Concluído </td>
 </tr>
</table>

<h2> Feedbacks e seguestões favor entrar em contato: </h2>
<a href="https://www.instagram.com/velipefieira"> <img src="https://img.shields.io/badge/Instagram-151515?style=for-the-badge&logo=instagram"/> </a>
<a href=""mailto:felipevieiragabriel@gmail.com""> <img src="https://img.shields.io/badge/Gmail-151515?style=for-the-badge&logo=gmail"></img></a>

<a href="#inicio">[Voltar ao início]</a>
