# ******************************************************************************
#  (c) 2019-2021. Nurul GC                                                     *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicaçoes                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from words_qt import palavras
from PyQt5.Qt import *
from sys import argv, exit
from time import sleep
from random import randint
import webbrowser
from history_qt import connection,tabela_jogo,add_pontos,view_pontos,apagar_historico

__nome__ = "Jogo Adivinha Palavra"
__version__ = "0.5-032021"
__copyright__ = "© 2019-2021 Nurul-GC"
__trademark__ = "™ ArtesGC"


class J3A7P6:

    NUMERO_TENTATIVA = 0
    PONTOS = 0
    JOGADA = 0
    PALAVRAS = palavras()

    def __init__(self):
        
        db=connection()
        tabela_jogo()
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle("Adivinha Palavra")
        self.ferramentas.setStyleSheet(
            'background-color:cadetblue; font-family:consolas; font-size:10pt;')
        self.ferramentas.setWindowIcon(QIcon("img/adivinhapalavra-icon.png"))
        self.ferramentas.setFixedSize(600, 550)

        # ******* criando abas para melhor organização *******
        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 30, 600, 520)

        # ******* variáveis *******
        self.janela02 = None
        self.janela03 = None
        self.janela04 = None
        self.janela05 = None
        self.nomeJogador = None
        self.nivel = None
        self.letraJogador = None

        # ******* menu *******
        menuFerramentas = QMenuBar(self.ferramentas)
        self.reiniciarJogo = menuFerramentas.addAction("Reiniciar")
        self.reiniciarJogo.setEnabled(False)
        self.reiniciarJogo.triggered.connect(self._reiniciarJogo)

        opcoes = menuFerramentas.addMenu("Opções")

        instr = opcoes.addAction("Instruções")
        instr.triggered.connect(self._instr)
        opcoes.addSeparator()

        palavraSecretas = opcoes.addAction("Palavras Secretas")
        palavraSecretas.triggered.connect(self._palavrasSecretas)
        opcoes.addSeparator()

        sair = opcoes.addAction("Sair")
        sair.triggered.connect(self._sair)

        sobre = menuFerramentas.addAction("Historico")
        sobre.triggered.connect(self._historico)

        sobre = menuFerramentas.addAction("Sobre")
        sobre.triggered.connect(self._sobre)

        self.janelaPrincipal()

    def _historico(self):
        if self.janela05 is None:
            return self.hhistory()
        try:
            self.tab.setCurrentWidget(self.janela05)
        except Exception as e:
            self.tab.removeTab(1)
            return self.hhistory()
        else:
            self.tab.removeTab(1)
            return self.hhistory()


    def hhistory(self):
        self.janela05 = QWidget()

        layout = QVBoxLayout()
        
        labelIntro = QLabel("<b>" + ".  . " * 5 +
                            "Historico" + 5 * " .  ." + "</b>")

        labelIntro.setAlignment(Qt.AlignHCenter)
        
        layout.addWidget(labelIntro)
        
        
        listaPalavras = QListWidget()
        layout = QFormLayout()


        #labelname = QLabel("<table><thead><tr><th>#</th><th>Nome</th><th>Pontos</th><th>Jogada</th><th>Nivel</th></tr></thead><tbody> "for vl in lo[]: " <tr><td><span>{}</span></td></tr></tbody></table>")
        

        

        for dados in view_pontos():
            tr= f"""<tr>
                        <td>
                            <span> </span>
                        </td>
                        
                        <td>
                            <span>{dados[0]}</span>
                        </td>
                        
                        <td>
                            <span>{str(dados[1])}</span>
                        </td>

                        <td>
                            <span>{str(dados[2])}</span>
                        </td>

                        <td>
                            <span>{str(dados[3])}</span>
                        </td>
                </tr>"""
            labelname = QLabel(f"""
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Nome</th>
                    <th>Pontos</th>
                    <th>Jogada</th>
                    <th>Nivel</th>
                </tr>
            </thead>
            <tbody>
            
                {tr}
                
            </tbody>
        </table>
        """)
            labelname.setStyleSheet(""" 
            padding: 0.75rem;vertical-align: top;border-top: 1px solid #dee2e6;
            """)
            layout.addWidget(labelname)

        def fechar(): return self.tab.removeTab(self.tab.currentIndex())
        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;margin-top: 350px;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)
        self.janela05.setLayout(layout)
        self.tab.addTab(self.janela05, 'Historico')
        self.tab.setCurrentWidget(self.janela05)



    def _reiniciarJogo(self):
        if self.janela02 is None:
            return self.dadosJogador()
        try:
            self.tab.setCurrentWidget(self.janela02)
        except Exception as e:
            self.tab.removeTab(0)
            return self.dadosJogador()
        else:
            self.tab.removeTab(0)
            return self.dadosJogador()

    def _palavrasSecretas(self):
        if self.janela04 is None:
            return self.palavrasSecretas()
        try:
            self.tab.setCurrentWidget(self.janela04)
        except Exception as e:
            self.tab.removeTab(1)
            return self.palavrasSecretas()
        else:
            self.tab.removeTab(1)
            return self.palavrasSecretas()

    def _instr(self):
        QMessageBox.information(self.ferramentas, 'Instruções', """
Olá Que a Paz e Bençãos de Deus Estejam Sobre Ti e Toda Tua Família..
Este Jogo Consiste em Ganhar o Máximo de Pontos Possiveis em Poucas Tentativas,
acertando Que Palavra Foi Definida (LETRA POR LETRA)..

Para uma melhor experiência de jogo:
- Conte quantas letras tem a suposta palavra
- identificada pelos simbolos '_' (referem-se as letras da palavra)
- e use a lista de palavras que estão escondidas no menu de opções (Palavras Secretas)
- Use as como referência para as suas tentativas!

Que Deus Te Ilumine Nessa Aventura!

Dica:
Códigos de Honra;

Muito Obrigado pelo apoio!
© 2019-2021 Nurul GC
™ ArtesGC Inc
""")

    def _sobre(self):
        QMessageBox.information(self.ferramentas, 'Sobre', '''
Nome: Jogo Adivinha Palavra
Versão: 0.6-052021
Designer e Programador: Nurul GC
Empresa: ArtesGC Inc.
''')

    def _sair(self):
        sair = QMessageBox.question(
            self.ferramentas, "Sair", "Tem mesmo a certeza que deseja sair?")
        if sair == QMessageBox.Yes:
            exit(0)
        else:
            pass

    def janelaPrincipal(self):
        janela01 = QWidget()
        layout = QVBoxLayout()

        labelImagem = QLabel()
        labelImagem.setPixmap(
            QPixmap("img/adivinhapalavra-logo.png").scaled(QSize(570, 400)))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelImagem)

        barraProgresso = QProgressBar()
        barraProgresso.setGeometry(200, 100, 200, 30)
        barraProgresso.setAlignment(Qt.AlignHCenter)
        barraProgresso.setStyleSheet("border: 1px solid; border-radius: 3px;")
        layout.addWidget(barraProgresso)

        def processar():
            n = randint(1, 5)
            sec = 0.5
            if n < 3:
                sec = 0.1
            for i in range(0, 101, n):
                sleep(sec)
                barraProgresso.setValue(i)
            self.tab.removeTab(0)
            self.dadosJogador()

        botaoIniciar = QPushButton("Iniciar Jogo")
        botaoIniciar.setStyleSheet("background-color:#D1C399;padding:50px;")
        botaoIniciar.clicked.connect(processar)
        layout.addWidget(botaoIniciar)

        janela01.setLayout(layout)
        self.tab.addTab(janela01, "Bem-Vindo")
        self.tab.setCurrentWidget(janela01)

    def dadosJogador(self):
        # activar a opção de reiniciar jogo
        self.reiniciarJogo.setEnabled(True)

        def jogo():
            if self.nomeJogador.text() == "" or self.nomeJogador.text().isspace() or None:
                QMessageBox.warning(self.ferramentas, 'Aviso',
                                    'Nome do jogador não definido..')
            else:
                if self.nivel.currentText() == '3':
                    self.NUMERO_TENTATIVA = 15
                    self.PONTOS = 0
                    self.tab.removeTab(0)
                    self.jogo()
                elif self.nivel.currentText() == '2':
                    self.NUMERO_TENTATIVA = 20
                    self.PONTOS = 0
                    self.tab.removeTab(0)
                    self.jogo()
                elif self.nivel.currentText() == '1':
                    self.NUMERO_TENTATIVA = 25
                    self.PONTOS = 0
                    self.tab.removeTab(0)
                    self.jogo()
                else:
                    QMessageBox.warning(
                        self.ferramentas, 'Aviso', 'Nível não definido..')

        QMessageBox.information(self.ferramentas, "Atenção", "Para uma melhor experiência de jogo leia as instruções que se encontram na barra de menu.."
                                                             "\nObrigado pelo apoio! - ArtesGC")
        self.janela02 = QWidget()
        layout = QFormLayout()
        layout.setVerticalSpacing(30)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap("img/03.png"))
        labelImagem.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelImagem)

        labelExtra = QLabel("<b>" + ".  . " * 5 +
                            "DADOS DO JOGADOR" + " .  ." * 5 + "</b>")
        labelExtra.setAlignment(Qt.AlignCenter)
        layout.addRow(labelExtra)

        self.nomeJogador = QLineEdit()
        self.nomeJogador.setPlaceholderText("Digite o seu nome..")
        layout.addRow(self.nomeJogador)

        niveis = ['1', '2', '3']
        self.nivel = QComboBox()
        self.nivel.addItems(niveis)
        self.nivel.setToolTip(
            'Nível 1 - 25 tentativas\nNível 2 - 20 tentativas\nNível 3 - 15 tentativas')
        layout.addRow("<b>Selecione o &Nível:</b>", self.nivel)

        botaoJogar = QPushButton("Jogar")
        botaoJogar.setDefault(True)
        botaoJogar.setStyleSheet("background-color:green;padding:10px;")
        botaoJogar.clicked.connect(jogo)
        layout.addRow(botaoJogar)

        def browser(p): return webbrowser.open('https://artesgc.home.blog')
        labelCopyright = QLabel(
            "<a href='#' style='text-decoration:none;'>ArtesGC Inc.</a>")
        labelCopyright.setAlignment(Qt.AlignRight)
        labelCopyright.setToolTip('Acesso a pagina oficial da ArtesGC!')
        labelCopyright.linkActivated.connect(browser)
        layout.addWidget(labelCopyright)

        self.janela02.setLayout(layout)
        self.tab.addTab(self.janela02, "Jogador")
        self.tab.setCurrentWidget(self.janela02)

    def jogo(self):
        tamanhoListaPalavras = len(self.PALAVRAS)
        selecionaPalavraAleatoria = self.PALAVRAS[randint(
            0, tamanhoListaPalavras - 1)]
        agrupaLetrasPalavra = ['_' for letra in selecionaPalavraAleatoria]

        def validaJogada():
            if self.letraJogador.text() == "" or self.letraJogador.text().isspace() or None:
                QMessageBox.warning(self.ferramentas, 'Aviso',
                                    'Letra para tentativa não atribuida..')
            elif not self.letraJogador.text().isalpha():
                QMessageBox.warning(self.ferramentas, 'Aviso',
                                    'Letra para tentativa não atribuida..')
            else:
                def novoJogo():
                    self.JOGADA = 0
                    self.tab.removeTab(0)
                    self.jogo()

                self.JOGADA += 1
                posicao = 0
                acertou = '_' not in agrupaLetrasPalavra

                if self.letraJogador.text().upper() in selecionaPalavraAleatoria:
                    for letra in selecionaPalavraAleatoria:
                        if self.letraJogador.text().upper() == letra:
                            self.PONTOS += 100
                            agrupaLetrasPalavra[posicao] = self.letraJogador.text(
                            ).upper()

                            labelJogo.setText(f"""
        Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

        (^.^) Obaa..
        VOCÊ ACERTOU {self.nomeJogador.text()}!

        {agrupaLetrasPalavra}

        Pontos {self.PONTOS}
        """)
                            labelJogo.setStyleSheet(
                                "background-color:white; color:blue; border-radius: 3px; border: 2px solid; padding:50px;")
                        posicao += 1
                else:
                    self.PONTOS -= 50
                    labelJogo.setText(f"""
        Nível: {self.nivel.currentText()} - Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}

        (O_O) Upss..
        VOCÊ ERROU {self.nomeJogador.text()}!

        Pontos {self.PONTOS}
        """)
                    labelJogo.setStyleSheet(
                        "background-color:white; color:red; border-radius: 3px; border: 2px solid; padding:50px;")
                if acertou:
                    criar_historico = add_pontos(self.nomeJogador.text(),self.PONTOS,self.JOGADA,self.nivel.currentText())
                    labelJogo.setText(f"""
        (^3^) Parabéns {self.nomeJogador.text()}
        VOCÊ GANHOU..

        {agrupaLetrasPalavra}

        • Pontuação
        Nível: {self.nivel.currentText()}
        Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
        Pontos: {self.PONTOS}
        """)
                    labelJogo.setStyleSheet(
                        "background-color:white; color:green; border-radius: 3px; border: 2px solid; padding:50px;")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)
                elif self.JOGADA == self.NUMERO_TENTATIVA:
                    criar_historico = add_pontos(self.nomeJogador.text(),self.PONTOS,self.JOGADA,self.nivel.currentText())
                    labelJogo.setText(f"""
(T.T) Lamento {self.nomeJogador.text()}
VOCÊ ESGOTOU TODAS AS SUAS TENTATIVAS..

Palavra Secreta: {selecionaPalavraAleatoria}

• Pontuação
Nível: {self.nivel.currentText()}
Rodada: {self.JOGADA} de {self.NUMERO_TENTATIVA}
Pontos: {self.PONTOS}
""")


            


 
                    labelJogo.setStyleSheet(
                        "background-color:white; color:red; border-radius: 3px; border: 2px solid; padding:50px;")
                    botaoValida.setText('Novo Jogo')
                    botaoValida.clicked.connect(novoJogo)

        janela03 = QWidget()
        layout = QFormLayout()
        layout.setSpacing(20)

        labelInfo = QLabel(f"<h3>Bem-Vindo <i>{self.nomeJogador.text()}</i><br>"
                           f"Tente Adivinhar Qual é a Palavra Secreta..<br>"
                           f"{agrupaLetrasPalavra}</h3>")
        labelInfo.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelInfo)

        labelJogo = QLabel('\n.  .  .  .  .')
        labelJogo.setStyleSheet(
            "background-color: white; border-radius: 3px; border: 2px solid; padding:100px;")
        labelJogo.setAlignment(Qt.AlignHCenter)
        layout.addRow(labelJogo)

        labelExtra = QLabel("<b>" + ".  . " * 5 +
                            "JOGANDO" + " .  ." * 5 + "</b>")
        labelExtra.setAlignment(Qt.AlignCenter)
        layout.addRow(labelExtra)

        self.letraJogador = QLineEdit()
        self.letraJogador.setMaxLength(1)
        self.letraJogador.setPlaceholderText(
            "Digite a letra e pressione ENTER..")
        self.letraJogador.returnPressed.connect(validaJogada)
        layout.addRow(self.letraJogador)

        botaoValida = QPushButton('Validar Jogada')
        botaoValida.setDefault(True)
        botaoValida.clicked.connect(validaJogada)
        botaoValida.setStyleSheet('background-color:cyan;')

        botaoFimJogo = QPushButton('Terminar o Jogo')
        botaoFimJogo.clicked.connect(self._sair)
        botaoFimJogo.setStyleSheet('background-color:red;')
        layout.addRow(botaoValida, botaoFimJogo)

        janela03.setLayout(layout)
        self.tab.addTab(janela03, 'Jogando')
        self.tab.setCurrentWidget(janela03)

    def palavrasSecretas(self):
        self.janela04 = QWidget()
        layout = QVBoxLayout()

        labelIntro = QLabel("<b>" + ".  . " * 5 +
                            "PALAVRAS SECRETAS" + 5 * " .  ." + "</b>")
        labelIntro.setAlignment(Qt.AlignHCenter)
        layout.addWidget(labelIntro)

        listaPalavras = QListWidget()
        for palavra in sorted(self.PALAVRAS):
            listaPalavras.addItem(palavra)
        listaPalavras.setAlternatingRowColors(True)
        layout.addWidget(listaPalavras)

        labelExtra = QLabel(f"<i>* {len(self.PALAVRAS)} palavras..</i>")
        labelExtra.setAlignment(Qt.AlignRight)
        labelExtra.setStyleSheet("color:#D1C399;")
        layout.addWidget(labelExtra)

        def fechar(): return self.tab.removeTab(self.tab.currentIndex())
        botaoFechar = QPushButton("Fechar")
        botaoFechar.setStyleSheet('background-color:red;')
        botaoFechar.clicked.connect(fechar)
        layout.addWidget(botaoFechar)

        self.janela04.setLayout(layout)
        self.tab.addTab(self.janela04, 'Palavras Secretas')
        self.tab.setCurrentWidget(self.janela04)


if __name__ == '__main__':
    app = J3A7P6()
    app.ferramentas.show()
    app.gc.exec_()
