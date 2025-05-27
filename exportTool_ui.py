# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportTool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 770)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dbSettingsFrame = QFrame(self.centralwidget)
        self.dbSettingsFrame.setObjectName(u"dbSettingsFrame")
        self.dbSettingsFrame.setGeometry(QRect(10, 30, 451, 211))
        self.dbSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dbSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.testConnectionPushButton = QPushButton(self.dbSettingsFrame)
        self.testConnectionPushButton.setObjectName(u"testConnectionPushButton")
        self.testConnectionPushButton.setGeometry(QRect(20, 170, 91, 24))
        self.testConnectionPushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.dbSettingsFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 401, 136))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ServerLabel = QLabel(self.layoutWidget)
        self.ServerLabel.setObjectName(u"ServerLabel")

        self.gridLayout.addWidget(self.ServerLabel, 0, 0, 1, 1)

        self.serverLineEdit = QLineEdit(self.layoutWidget)
        self.serverLineEdit.setObjectName(u"serverLineEdit")

        self.gridLayout.addWidget(self.serverLineEdit, 0, 1, 1, 1)

        self.portLabel = QLabel(self.layoutWidget)
        self.portLabel.setObjectName(u"portLabel")

        self.gridLayout.addWidget(self.portLabel, 1, 0, 1, 1)

        self.portLineEdit = QLineEdit(self.layoutWidget)
        self.portLineEdit.setObjectName(u"portLineEdit")

        self.gridLayout.addWidget(self.portLineEdit, 1, 1, 1, 1)

        self.databaseLabel = QLabel(self.layoutWidget)
        self.databaseLabel.setObjectName(u"databaseLabel")

        self.gridLayout.addWidget(self.databaseLabel, 2, 0, 1, 1)

        self.databaseLineEdit = QLineEdit(self.layoutWidget)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")

        self.gridLayout.addWidget(self.databaseLineEdit, 2, 1, 1, 1)

        self.userNameLabel = QLabel(self.layoutWidget)
        self.userNameLabel.setObjectName(u"userNameLabel")

        self.gridLayout.addWidget(self.userNameLabel, 3, 0, 1, 1)

        self.userNameLineEdit = QLineEdit(self.layoutWidget)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")

        self.gridLayout.addWidget(self.userNameLineEdit, 3, 1, 1, 1)

        self.passwordLabel = QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 4, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.gridLayout.addWidget(self.passwordLineEdit, 4, 1, 1, 1)

        self.dbSettingsLabel = QLabel(self.centralwidget)
        self.dbSettingsLabel.setObjectName(u"dbSettingsLabel")
        self.dbSettingsLabel.setGeometry(QRect(30, 0, 171, 21))
        self.objectNameLabel = QLabel(self.centralwidget)
        self.objectNameLabel.setObjectName(u"objectNameLabel")
        self.objectNameLabel.setGeometry(QRect(530, 270, 101, 16))
        self.exportPushButton = QPushButton(self.centralwidget)
        self.exportPushButton.setObjectName(u"exportPushButton")
        self.exportPushButton.setGeometry(QRect(530, 200, 161, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.exportPushButton.setFont(font)
        self.exportPushButton.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.previewTableWidget = QTableWidget(self.centralwidget)
        self.previewTableWidget.setObjectName(u"previewTableWidget")
        self.previewTableWidget.setGeometry(QRect(10, 340, 851, 221))
        self.previewLabel = QLabel(self.centralwidget)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(10, 320, 151, 16))
        self.objectTypeComboBox = QComboBox(self.centralwidget)
        self.objectTypeComboBox.setObjectName(u"objectTypeComboBox")
        self.objectTypeComboBox.setGeometry(QRect(300, 290, 221, 24))
        self.objectNameComboBox = QComboBox(self.centralwidget)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")
        self.objectNameComboBox.setGeometry(QRect(530, 290, 331, 24))
        self.objectTypeLabel = QLabel(self.centralwidget)
        self.objectTypeLabel.setObjectName(u"objectTypeLabel")
        self.objectTypeLabel.setGeometry(QRect(300, 270, 131, 16))
        self.separatorGroupBox = QGroupBox(self.centralwidget)
        self.separatorGroupBox.setObjectName(u"separatorGroupBox")
        self.separatorGroupBox.setGeometry(QRect(470, 20, 141, 161))
        self.commaRadioButton = QRadioButton(self.separatorGroupBox)
        self.commaRadioButton.setObjectName(u"commaRadioButton")
        self.commaRadioButton.setGeometry(QRect(10, 60, 92, 20))
        self.semicolonRadioButton = QRadioButton(self.separatorGroupBox)
        self.semicolonRadioButton.setObjectName(u"semicolonRadioButton")
        self.semicolonRadioButton.setGeometry(QRect(10, 30, 92, 20))
        self.semicolonRadioButton.setChecked(True)
        self.tabRadioButton = QRadioButton(self.separatorGroupBox)
        self.tabRadioButton.setObjectName(u"tabRadioButton")
        self.tabRadioButton.setGeometry(QRect(10, 90, 92, 20))
        self.otherSeparatorRadioButton = QRadioButton(self.separatorGroupBox)
        self.otherSeparatorRadioButton.setObjectName(u"otherSeparatorRadioButton")
        self.otherSeparatorRadioButton.setGeometry(QRect(10, 120, 92, 20))
        self.separatorLineEdit = QLineEdit(self.separatorGroupBox)
        self.separatorLineEdit.setObjectName(u"separatorLineEdit")
        self.separatorLineEdit.setGeometry(QRect(60, 120, 31, 22))
        self.qualifierGroupBox = QGroupBox(self.centralwidget)
        self.qualifierGroupBox.setObjectName(u"qualifierGroupBox")
        self.qualifierGroupBox.setGeometry(QRect(620, 20, 151, 161))
        self.doubleQuotationmarkRadioButton = QRadioButton(self.qualifierGroupBox)
        self.doubleQuotationmarkRadioButton.setObjectName(u"doubleQuotationmarkRadioButton")
        self.doubleQuotationmarkRadioButton.setGeometry(QRect(10, 60, 151, 20))
        self.quotationmarkRadioButton = QRadioButton(self.qualifierGroupBox)
        self.quotationmarkRadioButton.setObjectName(u"quotationmarkRadioButton")
        self.quotationmarkRadioButton.setGeometry(QRect(10, 90, 151, 20))
        self.otherQualifierRadioButton = QRadioButton(self.qualifierGroupBox)
        self.otherQualifierRadioButton.setObjectName(u"otherQualifierRadioButton")
        self.otherQualifierRadioButton.setGeometry(QRect(10, 120, 92, 20))
        self.qualifierLineEdit = QLineEdit(self.qualifierGroupBox)
        self.qualifierLineEdit.setObjectName(u"qualifierLineEdit")
        self.qualifierLineEdit.setGeometry(QRect(60, 120, 31, 22))
        self.withoutRadioButton = QRadioButton(self.qualifierGroupBox)
        self.withoutRadioButton.setObjectName(u"withoutRadioButton")
        self.withoutRadioButton.setGeometry(QRect(10, 30, 92, 20))
        self.withoutRadioButton.setCheckable(True)
        self.databaseComboBox = QComboBox(self.centralwidget)
        self.databaseComboBox.setObjectName(u"databaseComboBox")
        self.databaseComboBox.setGeometry(QRect(10, 290, 271, 24))
        self.chooseDbLabel = QLabel(self.centralwidget)
        self.chooseDbLabel.setObjectName(u"chooseDbLabel")
        self.chooseDbLabel.setGeometry(QRect(10, 270, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1062, 33))
        self.menuOhje = QMenu(self.menubar)
        self.menuOhje.setObjectName(u"menuOhje")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOhje.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.testConnectionPushButton.setText(QCoreApplication.translate("MainWindow", u"Testaa yhteys", None))
        self.ServerLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.serverLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Palvelimen nimi tai IP-osoite", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TCP-portin numero, oletus 5432", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.databaseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tietokannan nimi, hallintatietokanta postgres", None))
        self.userNameLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus, oletusp\u00e4\u00e4k\u00e4ytt\u00e4j\u00e4 postgres", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4n salasana", None))
        self.dbSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokantayhteydenasetukset", None))
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin nimi", None))
        self.exportPushButton.setText(QCoreApplication.translate("MainWindow", u"Vie tiedostoon", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.objectTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin tyyppi", None))
        self.separatorGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sarake-erotin ", None))
        self.commaRadioButton.setText(QCoreApplication.translate("MainWindow", u"pilkku(,)", None))
        self.semicolonRadioButton.setText(QCoreApplication.translate("MainWindow", u"puolipiste (;)", None))
        self.tabRadioButton.setText(QCoreApplication.translate("MainWindow", u"Sarkain ", None))
        self.otherSeparatorRadioButton.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.qualifierGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tekstin tunniste", None))
        self.doubleQuotationmarkRadioButton.setText(QCoreApplication.translate("MainWindow", u"lainausmerkit (\")", None))
        self.quotationmarkRadioButton.setText(QCoreApplication.translate("MainWindow", u"puolilainausmerkit (')", None))
        self.otherQualifierRadioButton.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.withoutRadioButton.setText(QCoreApplication.translate("MainWindow", u"Ei mit\u00e4\u00e4n", None))
        self.chooseDbLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.menuOhje.setTitle(QCoreApplication.translate("MainWindow", u"Ohje", None))
    # retranslateUi

