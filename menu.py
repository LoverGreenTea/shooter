from PyQt5.QtWidgets import *
app = QApplication([])

window = QWidget()
window.resize(700,500)

ButtonPlay = QPushButton('Play')
ButtonSettings = QPushButton('Settings')
ButtonQuit = QPushButton('Quit')


main_line = QVBoxLayout()

main_line.addWidget(ButtonPlay)
main_line.addWidget(ButtonSettings)
main_line.addWidget(ButtonQuit)



window.setLayout(main_line)
window.show()
app.exec_()