

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 171)
        Form.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout_2.addWidget(self.image_label)
        self.image_label2 = QtWidgets.QLabel(Form)
        self.image_label2.setObjectName("image_label2")
        self.horizontalLayout_2.addWidget(self.image_label2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        self.control_bt3 = QtWidgets.QPushButton(Form)
        self.control_bt3.setObjectName("control_bt3")
        self.verticalLayout.addWidget(self.control_bt3)
        self.control_bt2 = QtWidgets.QPushButton(Form)
        self.control_bt2.setObjectName("control_bt2")
        self.verticalLayout.addWidget(self.control_bt2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Project realized by Bellahna Boubker \"bbellahna@gmail.com\""))
        self.image_label.setText(_translate("Form", "............................................................................................."))
        self.image_label2.setText(_translate("Form", ""))
        self.control_bt.setText(_translate("Form", "start"))
        self.control_bt3.setText(_translate("Form", "take pic"))
        self.control_bt2.setText(_translate("Form", "close"))

