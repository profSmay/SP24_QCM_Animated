# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Car_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1143, 959)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp_Inputs = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_Inputs.sizePolicy().hasHeightForWidth())
        self.grp_Inputs.setSizePolicy(sizePolicy)
        self.grp_Inputs.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grp_Inputs.setFont(font)
        self.grp_Inputs.setFlat(False)
        self.grp_Inputs.setObjectName("grp_Inputs")
        self.gridLayout = QtWidgets.QGridLayout(self.grp_Inputs)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.le_k2 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_k2.sizePolicy().hasHeightForWidth())
        self.le_k2.setSizePolicy(sizePolicy)
        self.le_k2.setMinimumSize(QtCore.QSize(75, 0))
        self.le_k2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_k2.setFont(font)
        self.le_k2.setObjectName("le_k2")
        self.gridLayout.addWidget(self.le_k2, 5, 1, 1, 1)
        self.le_tmax = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_tmax.sizePolicy().hasHeightForWidth())
        self.le_tmax.setSizePolicy(sizePolicy)
        self.le_tmax.setMinimumSize(QtCore.QSize(75, 0))
        self.le_tmax.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_tmax.setObjectName("le_tmax")
        self.gridLayout.addWidget(self.le_tmax, 7, 1, 1, 1)
        self.lbl_CarSpeed = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CarSpeed.sizePolicy().hasHeightForWidth())
        self.lbl_CarSpeed.setSizePolicy(sizePolicy)
        self.lbl_CarSpeed.setObjectName("lbl_CarSpeed")
        self.gridLayout.addWidget(self.lbl_CarSpeed, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_m2 = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_m2.sizePolicy().hasHeightForWidth())
        self.lbl_m2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_m2.setFont(font)
        self.lbl_m2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_m2.setObjectName("lbl_m2")
        self.gridLayout.addWidget(self.lbl_m2, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_k2 = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_k2.sizePolicy().hasHeightForWidth())
        self.lbl_k2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_k2.setFont(font)
        self.lbl_k2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_k2.setObjectName("lbl_k2")
        self.gridLayout.addWidget(self.lbl_k2, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_Spring1 = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Spring1.sizePolicy().hasHeightForWidth())
        self.lbl_Spring1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Spring1.setFont(font)
        self.lbl_Spring1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Spring1.setObjectName("lbl_Spring1")
        self.gridLayout.addWidget(self.lbl_Spring1, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_c1 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_c1.sizePolicy().hasHeightForWidth())
        self.le_c1.setSizePolicy(sizePolicy)
        self.le_c1.setMinimumSize(QtCore.QSize(75, 0))
        self.le_c1.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_c1.setFont(font)
        self.le_c1.setObjectName("le_c1")
        self.gridLayout.addWidget(self.le_c1, 3, 1, 1, 1)
        self.le_m1 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_m1.sizePolicy().hasHeightForWidth())
        self.le_m1.setSizePolicy(sizePolicy)
        self.le_m1.setMinimumSize(QtCore.QSize(75, 0))
        self.le_m1.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_m1.setFont(font)
        self.le_m1.setObjectName("le_m1")
        self.gridLayout.addWidget(self.le_m1, 0, 1, 1, 1)
        self.lbl_tMax = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tMax.sizePolicy().hasHeightForWidth())
        self.lbl_tMax.setSizePolicy(sizePolicy)
        self.lbl_tMax.setObjectName("lbl_tMax")
        self.gridLayout.addWidget(self.lbl_tMax, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_v = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_v.sizePolicy().hasHeightForWidth())
        self.le_v.setSizePolicy(sizePolicy)
        self.le_v.setMinimumSize(QtCore.QSize(75, 0))
        self.le_v.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_v.setObjectName("le_v")
        self.gridLayout.addWidget(self.le_v, 1, 1, 1, 1)
        self.lbl_CarBodyMass = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CarBodyMass.sizePolicy().hasHeightForWidth())
        self.lbl_CarBodyMass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_CarBodyMass.setFont(font)
        self.lbl_CarBodyMass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_CarBodyMass.setObjectName("lbl_CarBodyMass")
        self.gridLayout.addWidget(self.lbl_CarBodyMass, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gv_Schematic = QtWidgets.QGraphicsView(self.grp_Inputs)
        self.gv_Schematic.setMinimumSize(QtCore.QSize(500, 500))
        self.gv_Schematic.setMaximumSize(QtCore.QSize(600, 600))
        self.gv_Schematic.setObjectName("gv_Schematic")
        self.gridLayout.addWidget(self.gv_Schematic, 15, 0, 1, 2)
        self.chk_IncludeAccel = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_IncludeAccel.setObjectName("chk_IncludeAccel")
        self.gridLayout.addWidget(self.chk_IncludeAccel, 12, 0, 1, 2, QtCore.Qt.AlignRight)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_calculate = QtWidgets.QPushButton(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calculate.sizePolicy().hasHeightForWidth())
        self.btn_calculate.setSizePolicy(sizePolicy)
        self.btn_calculate.setObjectName("btn_calculate")
        self.horizontalLayout_2.addWidget(self.btn_calculate, 0, QtCore.Qt.AlignRight)
        self.pb_Optimize = QtWidgets.QPushButton(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Optimize.sizePolicy().hasHeightForWidth())
        self.pb_Optimize.setSizePolicy(sizePolicy)
        self.pb_Optimize.setObjectName("pb_Optimize")
        self.horizontalLayout_2.addWidget(self.pb_Optimize, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 2)
        self.chk_ShowAccel = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_ShowAccel.setObjectName("chk_ShowAccel")
        self.gridLayout.addWidget(self.chk_ShowAccel, 11, 0, 1, 2, QtCore.Qt.AlignRight)
        self.lbl_MaxMinInfo = QtWidgets.QLabel(self.grp_Inputs)
        self.lbl_MaxMinInfo.setObjectName("lbl_MaxMinInfo")
        self.gridLayout.addWidget(self.lbl_MaxMinInfo, 14, 0, 1, 2, QtCore.Qt.AlignRight)
        self.lbl_RampANgle = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_RampANgle.sizePolicy().hasHeightForWidth())
        self.lbl_RampANgle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_RampANgle.setFont(font)
        self.lbl_RampANgle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_RampANgle.setObjectName("lbl_RampANgle")
        self.gridLayout.addWidget(self.lbl_RampANgle, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_k1 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_k1.sizePolicy().hasHeightForWidth())
        self.le_k1.setSizePolicy(sizePolicy)
        self.le_k1.setMinimumSize(QtCore.QSize(75, 0))
        self.le_k1.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_k1.setFont(font)
        self.le_k1.setObjectName("le_k1")
        self.gridLayout.addWidget(self.le_k1, 2, 1, 1, 1)
        self.le_m2 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_m2.sizePolicy().hasHeightForWidth())
        self.le_m2.setSizePolicy(sizePolicy)
        self.le_m2.setMinimumSize(QtCore.QSize(75, 0))
        self.le_m2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_m2.setFont(font)
        self.le_m2.setObjectName("le_m2")
        self.gridLayout.addWidget(self.le_m2, 4, 1, 1, 1)
        self.le_ang = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ang.sizePolicy().hasHeightForWidth())
        self.le_ang.setSizePolicy(sizePolicy)
        self.le_ang.setMinimumSize(QtCore.QSize(75, 0))
        self.le_ang.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_ang.setFont(font)
        self.le_ang.setObjectName("le_ang")
        self.gridLayout.addWidget(self.le_ang, 6, 1, 1, 1)
        self.layourhorizontal = QtWidgets.QHBoxLayout()
        self.layourhorizontal.setObjectName("layourhorizontal")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layourhorizontal.addItem(spacerItem1)
        self.chk_LogX = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_LogX.setObjectName("chk_LogX")
        self.layourhorizontal.addWidget(self.chk_LogX, 0, QtCore.Qt.AlignRight)
        self.chk_LogY = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_LogY.setObjectName("chk_LogY")
        self.layourhorizontal.addWidget(self.chk_LogY, 0, QtCore.Qt.AlignRight)
        self.chk_LogAccel = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_LogAccel.setObjectName("chk_LogAccel")
        self.layourhorizontal.addWidget(self.chk_LogAccel, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.layourhorizontal, 9, 0, 1, 2)
        self.lbl_Dashpot = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Dashpot.sizePolicy().hasHeightForWidth())
        self.lbl_Dashpot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Dashpot.setFont(font)
        self.lbl_Dashpot.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Dashpot.setObjectName("lbl_Dashpot")
        self.gridLayout.addWidget(self.lbl_Dashpot, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.grp_Inputs)
        self.layout_Plot = QtWidgets.QVBoxLayout()
        self.layout_Plot.setObjectName("layout_Plot")
        self.horizontalLayout.addLayout(self.layout_Plot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.grp_Inputs.setTitle(_translate("Form", "Model Inputs"))
        self.le_k2.setText(_translate("Form", "90000"))
        self.le_tmax.setText(_translate("Form", "3"))
        self.lbl_CarSpeed.setText(_translate("Form", "Car Speed (kph)"))
        self.lbl_m2.setText(_translate("Form", "Wheel mass (m2, kg)"))
        self.lbl_k2.setText(_translate("Form", "Tire spring constant (k2, N/m)"))
        self.lbl_Spring1.setText(_translate("Form", "Suspension Spring (k1, N/m)"))
        self.le_c1.setText(_translate("Form", "4500"))
        self.le_m1.setText(_translate("Form", "450"))
        self.lbl_tMax.setText(_translate("Form", "t, max plot (s)"))
        self.le_v.setText(_translate("Form", "120"))
        self.lbl_CarBodyMass.setText(_translate("Form", "Car body mass (m1, kg)"))
        self.chk_IncludeAccel.setText(_translate("Form", "Include Accel in Opt."))
        self.btn_calculate.setText(_translate("Form", "Calculate"))
        self.pb_Optimize.setText(_translate("Form", "Optimize Suspension"))
        self.chk_ShowAccel.setText(_translate("Form", "Plot Car Accel."))
        self.lbl_MaxMinInfo.setText(_translate("Form", "TextLabel"))
        self.lbl_RampANgle.setText(_translate("Form", "Ramp Angle (deg)"))
        self.le_k1.setText(_translate("Form", "15000"))
        self.le_m2.setText(_translate("Form", "20"))
        self.le_ang.setText(_translate("Form", "45"))
        self.chk_LogX.setText(_translate("Form", "log scale t"))
        self.chk_LogY.setText(_translate("Form", "log scale Y"))
        self.chk_LogAccel.setText(_translate("Form", "log scale Y\'\'"))
        self.lbl_Dashpot.setText(_translate("Form", "Suspension Shock Absorber (c1, N*s/m)"))