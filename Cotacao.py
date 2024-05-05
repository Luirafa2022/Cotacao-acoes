import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout
from PySide2.QtGui import QColor, QFont, QIcon
from math import sqrt

class Cotacao(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cotação de Ações")
        self.setGeometry(300, 300, 450, 250)

        app_icon = QIcon("Logo.png")
        QApplication.instance().setWindowIcon(app_icon)

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
        self.calcularButton.clicked.connect(self.calcular)

        self.resultadoLabel = QLabel("")
        gridLayout.addWidget(self.resultadoLabel, 5, 0, 1, 2)

        self.setLayout(gridLayout)

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
        """)

    def calcular(self):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cotacao = Cotacao()
    cotacao.show()
    sys.exit(app.exec_())