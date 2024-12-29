from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from File_Save import *

from File_Save import read_from_file, write_in_file


def windowShop():
    window = QDialog()

    catalog = [
        {
            "name": "Tea",
            "PhotoSkins": "tea.png",
            "price": 20000000
        },
        {
            "name": "skin 2",
            "PhotoSkins": "ufo.png",
            "price": 250
        },
        {
            "name": "skin 3",
            "PhotoSkins": "rocket.png",
            "price": 250
        },
    ]
    data = read_from_file()
    score_lbl = QLabel("Score: " + str(data['score']))
    main_line = QVBoxLayout()
    main_line.addWidget(score_lbl)

    h1 = QHBoxLayout()
    def buy_func(p, skin):
        data = read_from_file()
        print(p)
        if data["score"] >= p:
            data["score"] -= p
            data["skin"] = skin
        write_in_file(data)

    for element in catalog:
        v1 = QVBoxLayout()
        name = QLabel(element['name'])
        PhotoSkins = QLabel("PhotoSkins")
        pixmap = QPixmap(element['PhotoSkins'])
        pixmap = pixmap.scaledToWidth(100)
        PhotoSkins.setPixmap(pixmap)
        price = QLabel(str(element['price']))
        buy_btn = QPushButton("Buy")
        buy_btn.clicked.connect(lambda _,
                                       my_price=element['price'],
                                       skin=element['PhotoSkins']:
                                buy_func(my_price,skin))
        v1.addWidget(name)
        v1.addWidget(PhotoSkins)
        v1.addWidget(price)
        v1.addWidget(buy_btn)
        h1.addLayout(v1)
    main_line.addLayout(h1)
    window.setLayout(main_line)
    window.exec()