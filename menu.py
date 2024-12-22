from PyQt5.QtWidgets import *
app = QApplication([])
import Main

window = QWidget()
window.resize(700,500)

ButtonPlay = QPushButton('Play')
ButtonSettings = QPushButton('Settings')
ButtonShop = QPushButton('Shop')
ButtonQuit = QPushButton('Quit')


main_line = QVBoxLayout()

main_line.addWidget(ButtonPlay)
main_line.addWidget(ButtonSettings)
main_line.addWidget(ButtonShop)
main_line.addWidget(ButtonQuit)

ButtonPlay.clicked.connect(Main.game)

window.setLayout(main_line)
window.show()
app.exec_()