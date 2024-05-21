import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout, QTabWidget, QComboBox
from PyQt5.QtGui import QColor, QIcon
from math import sqrt

class Cotacao(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cotação de Ações")
        self.setGeometry(300, 300, 530, 300)

        app_icon = QIcon("Logo.png")
        QApplication.instance().setWindowIcon(app_icon)

        tabWidget = QTabWidget()
        tabWidget.addTab(self.createPrecoJustoTab(), "Preço Justo")
        tabWidget.addTab(self.createTetoPorAcaoTab(), "Teto por Ação")
        tabWidget.addTab(self.createBuscarAcaoTab(), "Buscar Ação")
        tabWidget.addTab(self.createSimuladorGanhoTab(), "Simulador de Ganhos")

        layout = QVBoxLayout()
        layout.addWidget(tabWidget)
        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
            }
            QLineEdit {
                font-size: 12px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 12px;
                padding: 5px;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: #fff;
            }
            QPushButton:hover {
                background-color: #3e8e41;
            }
            QLabel#resultadoLabel {
                font-size: 14px;
                font-weight: bold;
            }
            QComboBox{
                font-size: 12px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;     
            }
        """)

    def createPrecoJustoTab(self):
        widget = QWidget()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.nomeLabel = QLabel("Nome da Ação:")
        gridLayout.addWidget(self.nomeLabel, 0, 0)

        self.nomeEdit = QLineEdit()
        gridLayout.addWidget(self.nomeEdit, 0, 1)

        self.lpaLabel = QLabel("LPA:")
        gridLayout.addWidget(self.lpaLabel, 1, 0)

        self.lpaEdit = QLineEdit()
        gridLayout.addWidget(self.lpaEdit, 1, 1)

        self.vpaLabel = QLabel("VPA:")
        gridLayout.addWidget(self.vpaLabel, 2, 0)

        self.vpaEdit = QLineEdit()
        gridLayout.addWidget(self.vpaEdit, 2, 1)

        self.valorAtualLabel = QLabel("Valor Atual:")
        gridLayout.addWidget(self.valorAtualLabel, 3, 0)

        self.valorAtualEdit = QLineEdit()
        gridLayout.addWidget(self.valorAtualEdit, 3, 1)

        self.calcularButton = QPushButton("Calcular")
        gridLayout.addWidget(self.calcularButton, 4, 0, 1, 2)
        self.calcularButton.clicked.connect(self.calcularPrecoJusto)

        self.resultadoLabel = QLabel("")
        gridLayout.addWidget(self.resultadoLabel, 5, 0, 1, 2)

        widget.setLayout(gridLayout)
        return widget

    def createTetoPorAcaoTab(self):
        widget = QWidget()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.nomeTetoLabel = QLabel("Nome da Ação:")
        gridLayout.addWidget(self.nomeTetoLabel, 0, 0)

        self.nomeTetoEdit = QLineEdit()
        gridLayout.addWidget(self.nomeTetoEdit, 0, 1)

        self.precoAtualLabel = QLabel("Preço Atual:")
        gridLayout.addWidget(self.precoAtualLabel, 1, 0)

        self.precoAtualEdit = QLineEdit()
        gridLayout.addWidget(self.precoAtualEdit, 1, 1)

        self.pvpLabel = QLabel("P/VP:")
        gridLayout.addWidget(self.pvpLabel, 2, 0)

        self.pvpEdit = QLineEdit()
        gridLayout.addWidget(self.pvpEdit, 2, 1)

        self.dividendosLabel = QLabel("Dividendos pagos dos Últimos 6 Anos (separado por vírgula):")
        gridLayout.addWidget(self.dividendosLabel, 3, 0)

        self.dividendosEdit = QLineEdit()
        gridLayout.addWidget(self.dividendosEdit, 3, 1)

        self.calcularTetoButton = QPushButton("Calcular Teto")
        gridLayout.addWidget(self.calcularTetoButton, 4, 0, 1, 2)
        self.calcularTetoButton.clicked.connect(self.calcularTetoPorAcao)

        self.resultadoTetoLabel = QLabel("")
        gridLayout.addWidget(self.resultadoTetoLabel, 5, 0, 1, 2)

        widget.setLayout(gridLayout)
        return widget

    def createBuscarAcaoTab(self):
        widget = QWidget()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.nomeBuscaLabel = QLabel("Nome da Ação:")
        gridLayout.addWidget(self.nomeBuscaLabel, 0, 0)

        self.nomeBuscaEdit = QLineEdit()
        gridLayout.addWidget(self.nomeBuscaEdit, 0, 1)

        self.buscarButton = QPushButton("Buscar Ação")
        gridLayout.addWidget(self.buscarButton, 1, 0, 1, 2)
        self.buscarButton.clicked.connect(self.buscarAcao)

        widget.setLayout(gridLayout)
        return widget

    def createSimuladorGanhoTab(self):
        widget = QWidget()
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.nomeSimuladorLabel = QLabel("Nome da Ação:")
        gridLayout.addWidget(self.nomeSimuladorLabel, 0, 0)

        self.nomeSimuladorEdit = QLineEdit()
        gridLayout.addWidget(self.nomeSimuladorEdit, 0, 1)

        self.dividendoPorAcaoLabel = QLabel("Dividendos por Ação (R$):")
        gridLayout.addWidget(self.dividendoPorAcaoLabel, 1, 0)

        self.dividendoPorAcaoEdit = QLineEdit()
        gridLayout.addWidget(self.dividendoPorAcaoEdit, 1, 1)

        self.quantidadeCotasLabel = QLabel("Quantidade de Cotas:")
        gridLayout.addWidget(self.quantidadeCotasLabel, 2, 0)

        self.quantidadeCotasEdit = QLineEdit()
        gridLayout.addWidget(self.quantidadeCotasEdit, 2, 1)

        self.frequenciaLabel = QLabel("Frequência dos Dividendos:")
        gridLayout.addWidget(self.frequenciaLabel, 3, 0)

        self.frequenciaCombo = QComboBox()
        self.frequenciaCombo.addItems(["Mensal", "Trimestral"])
        gridLayout.addWidget(self.frequenciaCombo, 3, 1)

        self.calcularSimuladorButton = QPushButton("Calcular Ganhos")
        gridLayout.addWidget(self.calcularSimuladorButton, 4, 0, 1, 2)
        self.calcularSimuladorButton.clicked.connect(self.calcularSimuladorGanho)

        self.resultadoSimuladorLabel = QLabel("")
        gridLayout.addWidget(self.resultadoSimuladorLabel, 5, 0, 1, 2)

        widget.setLayout(gridLayout)
        return widget

    def calcularPrecoJusto(self):
        nome = self.nomeEdit.text()
        try:
            lpa = float(self.lpaEdit.text())
            vpa = float(self.vpaEdit.text())
            valor_atual = float(self.valorAtualEdit.text())
        except ValueError:
            self.resultadoLabel.setText("Erro: valores inválidos")
            return

        resultado = sqrt(22.5 * lpa * vpa)

        if resultado < valor_atual:
            cor = QColor("red")
            mensagem = f"O valor justo da cota {nome} é de R$ {resultado:.2f} (a cota não está boa para comprar)"
        else:
            cor = QColor("green")
            mensagem = f"O valor justo da cota {nome} é de R$ {resultado:.2f} (a cota está boa para comprar)"

        razao = (resultado / valor_atual) * 100
        mensagem += f"\nRazão: {razao:.2f}%"

        self.resultadoLabel.setText(mensagem)
        self.resultadoLabel.setStyleSheet(f"color: {cor.name()}")

    def calcularTetoPorAcao(self):
        nome = self.nomeTetoEdit.text()
        try:
            preco_atual = float(self.precoAtualEdit.text())
            pvp = float(self.pvpEdit.text())
            dividendos = list(map(float, self.dividendosEdit.text().split(',')))
            if len(dividendos) != 6:
                raise ValueError("Número incorreto de dividendos")
        except ValueError:
            self.resultadoTetoLabel.setText("Erro: valores inválidos")
            return

        media_dividendos = sum(dividendos) / 6
        teto = media_dividendos / 0.06

        if preco_atual < teto and pvp <= 2:
            cor = QColor("green")
            mensagem = f"O teto por ação da cota {nome} é de R$ {teto:.2f} (a cota está boa para comprar)"
        else:
            cor = QColor("red")
            mensagem = f"O teto por ação da cota {nome} é de R$ {teto:.2f} (a cota não está boa para comprar)"

        self.resultadoTetoLabel.setText(mensagem)
        self.resultadoTetoLabel.setStyleSheet(f"color: {cor.name()}")

    def buscarAcao(self):
        nome = self.nomeBuscaEdit.text().strip().replace(" ", "-").lower()
        if nome:
            url = f"https://investidor10.com.br/acoes/{nome}"
            webbrowser.get().open_new_tab(url)

    def calcularSimuladorGanho(self):
        nome = self.nomeSimuladorEdit.text()
        try:
            dividendo_por_acao = float(self.dividendoPorAcaoEdit.text())
            quantidade_cotas = int(self.quantidadeCotasEdit.text())
            frequencia = self.frequenciaCombo.currentText()
        except ValueError:
            self.resultadoSimuladorLabel.setText("Erro: valores inválidos")
            return

        ganho_por_periodo = dividendo_por_acao * quantidade_cotas

        if frequencia == "Mensal":
            ganho_anual = ganho_por_periodo * 12
            mensagem = f"O ganho mensal da cota {nome} é de R$ {ganho_por_periodo:.2f}\n"
            mensagem += f"O ganho anual é de R$ {ganho_anual:.2f}"
        else:  # Trimestral
            ganho_anual = ganho_por_periodo * 3
            mensagem = f"O ganho trimestral da cota {nome} é de R$ {ganho_por_periodo:.2f}\n"
            mensagem += f"O ganho anual é de R$ {ganho_anual:.2f}"

        self.resultadoSimuladorLabel.setText(mensagem)
        self.resultadoSimuladorLabel.setStyleSheet("color: green")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cotacao = Cotacao()
    cotacao.show()
    sys.exit(app.exec_())
