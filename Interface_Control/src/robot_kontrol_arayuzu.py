#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_arayuzu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
import cv2
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication

import speech_recognition
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import chat
import oguu
from PyQt5.QtCore import Qt, QTimer
import ASL as rb 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1050, 850)
        Dialog.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(30, 100, 310, 370))
        self.imgLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setLineWidth(5)
        self.imgLabel.setText("")
        self.imgLabel.setTextFormat(QtCore.Qt.PlainText)
        self.imgLabel.setObjectName("imgLabel")
        self.Close = QtWidgets.QPushButton(Dialog)
        self.Close.setGeometry(QtCore.QRect(190, 480, 140, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Close.setFont(font)
        self.Close.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.Close.setObjectName("Close")
        self.gazebolabel = QtWidgets.QLabel(Dialog)
        self.gazebolabel.setGeometry(QtCore.QRect(720, 100, 310, 370))
        self.gazebolabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gazebolabel.setFrameShape(QtWidgets.QFrame.Box)
        self.gazebolabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gazebolabel.setLineWidth(5)
        self.gazebolabel.setText("")
        self.gazebolabel.setObjectName("gazebolabel")
        self.button_gazebo = QtWidgets.QPushButton(Dialog)
        self.button_gazebo.setGeometry(QtCore.QRect(730, 20, 291, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_gazebo.setFont(font)
        self.button_gazebo.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.button_gazebo.setObjectName("button_gazebo")
        self.buton_enter = QtWidgets.QPushButton(Dialog)
        self.buton_enter.setGeometry(QtCore.QRect(935, 650, 81, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_enter.setFont(font)
        self.buton_enter.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_enter.setObjectName("buton_enter")
        self.buton_j = QtWidgets.QPushButton(Dialog)
        self.buton_j.setGeometry(QtCore.QRect(650, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_j.setFont(font)
        self.buton_j.setMouseTracking(False)
        self.buton_j.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_j.setObjectName("buton_j")
        self.buton_u = QtWidgets.QPushButton(Dialog)
        self.buton_u.setGeometry(QtCore.QRect(650, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_u.setFont(font)
        self.buton_u.setMouseTracking(False)
        self.buton_u.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_u.setObjectName("buton_u")
        self.buton_a = QtWidgets.QPushButton(Dialog)
        self.buton_a.setGeometry(QtCore.QRect(81, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_a.setFont(font)
        self.buton_a.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buton_a.setMouseTracking(False)
        self.buton_a.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_a.setObjectName("buton_a")
        self.buton_v = QtWidgets.QPushButton(Dialog)
        self.buton_v.setGeometry(QtCore.QRect(367, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_v.setFont(font)
        self.buton_v.setMouseTracking(False)
        self.buton_v.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buton_v.setObjectName("buton_v")
        self.buton_x = QtWidgets.QPushButton(Dialog)
        self.buton_x.setGeometry(QtCore.QRect(178, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_x.setFont(font)
        self.buton_x.setMouseTracking(False)
        self.buton_x.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buton_x.setObjectName("buton_x")
        self.buton_b = QtWidgets.QPushButton(Dialog)
        self.buton_b.setGeometry(QtCore.QRect(461, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_b.setFont(font)
        self.buton_b.setMouseTracking(False)
        self.buton_b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buton_b.setObjectName("buton_b")
        self.buton_m = QtWidgets.QPushButton(Dialog)
        self.buton_m.setGeometry(QtCore.QRect(650, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_m.setFont(font)
        self.buton_m.setMouseTracking(False)
        self.buton_m.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_m.setObjectName("buton_m")
        self.buton_e = QtWidgets.QPushButton(Dialog)
        self.buton_e.setGeometry(QtCore.QRect(270, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_e.setFont(font)
        self.buton_e.setMouseTracking(False)
        self.buton_e.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_e.setObjectName("buton_e")
        self.buton_i = QtWidgets.QPushButton(Dialog)
        self.buton_i.setEnabled(True)
        self.buton_i.setGeometry(QtCore.QRect(745, 648, 80, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_i.setFont(font)
        self.buton_i.setMouseTracking(False)
        self.buton_i.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_i.setObjectName("buton_i")
        self.buton_g = QtWidgets.QPushButton(Dialog)
        self.buton_g.setGeometry(QtCore.QRect(460, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_g.setFont(font)
        self.buton_g.setMouseTracking(False)
        self.buton_g.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_g.setObjectName("buton_g")
        self.buton_h = QtWidgets.QPushButton(Dialog)
        self.buton_h.setGeometry(QtCore.QRect(555, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_h.setFont(font)
        self.buton_h.setMouseTracking(False)
        self.buton_h.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_h.setObjectName("buton_h")
        self.buton_n = QtWidgets.QPushButton(Dialog)
        self.buton_n.setGeometry(QtCore.QRect(556, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_n.setFont(font)
        self.buton_n.setMouseTracking(False)
        self.buton_n.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_n.setObjectName("buton_n")
        self.buton_space = QtWidgets.QPushButton(Dialog)
        self.buton_space.setGeometry(QtCore.QRect(841, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_space.setFont(font)
        self.buton_space.setMouseTracking(False)
        self.buton_space.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_space.setObjectName("buton_space")
        self.buton_p = QtWidgets.QPushButton(Dialog)
        self.buton_p.setEnabled(True)
        self.buton_p.setGeometry(QtCore.QRect(741, 750, 80, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_p.setFont(font)
        self.buton_p.setMouseTracking(False)
        self.buton_p.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_p.setObjectName("buton_p")
        self.buton_r = QtWidgets.QPushButton(Dialog)
        self.buton_r.setGeometry(QtCore.QRect(365, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_r.setFont(font)
        self.buton_r.setMouseTracking(False)
        self.buton_r.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_r.setObjectName("buton_r")
        self.buton_w = QtWidgets.QPushButton(Dialog)
        self.buton_w.setGeometry(QtCore.QRect(175, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_w.setFont(font)
        self.buton_w.setMouseTracking(False)
        self.buton_w.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_w.setObjectName("buton_w")
        self.buton_t = QtWidgets.QPushButton(Dialog)
        self.buton_t.setGeometry(QtCore.QRect(460, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_t.setFont(font)
        self.buton_t.setMouseTracking(False)
        self.buton_t.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_t.setObjectName("buton_t")
        self.buton_k = QtWidgets.QPushButton(Dialog)
        self.buton_k.setEnabled(True)
        self.buton_k.setGeometry(QtCore.QRect(745, 700, 80, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_k.setFont(font)
        self.buton_k.setMouseTracking(False)
        self.buton_k.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_k.setObjectName("buton_k")
        self.buton_z = QtWidgets.QPushButton(Dialog)
        self.buton_z.setGeometry(QtCore.QRect(81, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_z.setFont(font)
        self.buton_z.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buton_z.setMouseTracking(False)
        self.buton_z.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.buton_z.setObjectName("buton_z")
        self.buton_l = QtWidgets.QPushButton(Dialog)
        self.buton_l.setGeometry(QtCore.QRect(840, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_l.setFont(font)
        self.buton_l.setMouseTracking(False)
        self.buton_l.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_l.setObjectName("buton_l")
        self.buton_f = QtWidgets.QPushButton(Dialog)
        self.buton_f.setGeometry(QtCore.QRect(365, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_f.setFont(font)
        self.buton_f.setMouseTracking(False)
        self.buton_f.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_f.setObjectName("buton_f")
        self.buton_c = QtWidgets.QPushButton(Dialog)
        self.buton_c.setGeometry(QtCore.QRect(272, 750, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_c.setFont(font)
        self.buton_c.setMouseTracking(False)
        self.buton_c.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buton_c.setObjectName("buton_c")
        self.buton_o = QtWidgets.QPushButton(Dialog)
        self.buton_o.setGeometry(QtCore.QRect(840, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_o.setFont(font)
        self.buton_o.setMouseTracking(False)
        self.buton_o.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_o.setObjectName("buton_o")
        self.buton_d = QtWidgets.QPushButton(Dialog)
        self.buton_d.setGeometry(QtCore.QRect(270, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_d.setFont(font)
        self.buton_d.setMouseTracking(False)
        self.buton_d.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_d.setObjectName("buton_d")
        self.buton_s = QtWidgets.QPushButton(Dialog)
        self.buton_s.setGeometry(QtCore.QRect(175, 700, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_s.setFont(font)
        self.buton_s.setMouseTracking(False)
        self.buton_s.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_s.setObjectName("buton_s")
        self.buton_y = QtWidgets.QPushButton(Dialog)
        self.buton_y.setGeometry(QtCore.QRect(555, 648, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_y.setFont(font)
        self.buton_y.setMouseTracking(False)
        self.buton_y.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_y.setObjectName("buton_y")
        self.buton_q = QtWidgets.QPushButton(Dialog)
        self.buton_q.setGeometry(QtCore.QRect(80, 650, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_q.setFont(font)
        self.buton_q.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buton_q.setMouseTracking(False)
        self.buton_q.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_q.setObjectName("buton_q")
        self.Talk = QtWidgets.QPushButton(Dialog)
        self.Talk.setGeometry(QtCore.QRect(470, 540, 140, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Talk.setFont(font)
        self.Talk.setAutoFillBackground(False)
        self.Talk.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.Talk.setObjectName("Talk")
        self.START_2 = QtWidgets.QPushButton(Dialog)
        self.START_2.setGeometry(QtCore.QRect(40, 480, 140, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.START_2.setFont(font)
        self.START_2.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.START_2.setObjectName("START_2")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(190, 20, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ok.setFont(font)
        self.ok.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.ok.setObjectName("ok")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 180, 200, 70))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/chat.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Textimage = QtWidgets.QTextEdit(Dialog)
        self.Textimage.setGeometry(QtCore.QRect(40, 20, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Textimage.setFont(font)
        self.Textimage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Textimage.setReadOnly(True)
        self.Textimage.setObjectName("Textimage")
        self.textall = QtWidgets.QLineEdit(Dialog)
        self.textall.setGeometry(QtCore.QRect(380, 120, 300, 60))
        self.textall.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textall.setReadOnly(True)
        self.textall.setObjectName("textall")
        self.textfeedback = QtWidgets.QTextEdit(Dialog)
        self.textfeedback.setGeometry(QtCore.QRect(380, 250, 300, 280))
        self.textfeedback.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textfeedback.setReadOnly(True)
        self.textfeedback.setObjectName("textfeedback")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/ogu.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.buton_delete = QtWidgets.QPushButton(Dialog)
        self.buton_delete.setEnabled(True)
        self.buton_delete.setGeometry(QtCore.QRect(935, 750, 80, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buton_delete.setFont(font)
        self.buton_delete.setMouseTracking(False)
        self.buton_delete.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.buton_delete.setObjectName("buton_delete")

        self.retranslateUi(Dialog)
        self.Talk.pressed.connect(self.ses)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Close.setText(_translate("Dialog", "Close Camera"))
        self.button_gazebo.setText(_translate("Dialog", "Start Gazebo"))
        self.buton_enter.setText(_translate("Dialog", "ENTER"))
        self.buton_j.setText(_translate("Dialog", "J"))
        self.buton_u.setText(_translate("Dialog", "U"))
        self.buton_a.setText(_translate("Dialog", "A"))
        self.buton_v.setText(_translate("Dialog", "V"))
        self.buton_x.setText(_translate("Dialog", "X"))
        self.buton_b.setText(_translate("Dialog", "B"))
        self.buton_m.setText(_translate("Dialog", "M"))
        self.buton_e.setText(_translate("Dialog", "E"))
        self.buton_i.setText(_translate("Dialog", "I"))
        self.buton_g.setText(_translate("Dialog", "G"))
        self.buton_h.setText(_translate("Dialog", "H"))
        self.buton_n.setText(_translate("Dialog", "N"))
        self.buton_space.setText(_translate("Dialog", "SPACE"))
        self.buton_p.setText(_translate("Dialog", "P"))
        self.buton_r.setText(_translate("Dialog", "R"))
        self.buton_w.setText(_translate("Dialog", "W"))
        self.buton_t.setText(_translate("Dialog", "T"))
        self.buton_k.setText(_translate("Dialog", "K"))
        self.buton_z.setText(_translate("Dialog", "Z"))
        self.buton_l.setText(_translate("Dialog", "L"))
        self.buton_f.setText(_translate("Dialog", "F"))
        self.buton_c.setText(_translate("Dialog", "C"))
        self.buton_o.setText(_translate("Dialog", "O"))
        self.buton_d.setText(_translate("Dialog", "D"))
        self.buton_s.setText(_translate("Dialog", "S"))
        self.buton_y.setText(_translate("Dialog", "Y"))
        self.buton_q.setText(_translate("Dialog", "Q"))
        self.Talk.setText(_translate("Dialog", "Microphone"))
        self.START_2.setText(_translate("Dialog", "Start Camera"))
        self.ok.setText(_translate("Dialog", "OK"))
        self.Textimage.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buton_delete.setText(_translate("Dialog", "DELETE"))
        
        rospy.init_node("klavye_kontrol_arayuz",anonymous=True)
        
        self.rate = rospy.Rate(2) # 10
        
        self.pubij5 = rospy.Publisher('/anael/ij5_position_controller/command', Float64, queue_size=10)
        self.pubij4 = rospy.Publisher('/anael/ij4_position_controller/command', Float64, queue_size=10)
        self.pubij3 = rospy.Publisher('/anael/ij3_position_controller/command', Float64, queue_size=10)
        self.pubij1 = rospy.Publisher('/anael/ij1_position_controller/command', Float64, queue_size=10)
        
        self.puboj5 = rospy.Publisher('/anael/oj5_position_controller/command', Float64, queue_size=10)
        self.puboj4 = rospy.Publisher('/anael/oj4_position_controller/command', Float64, queue_size=10)
        self.puboj3 = rospy.Publisher('/anael/oj3_position_controller/command', Float64, queue_size=10)
        self.puboj1 = rospy.Publisher('/anael/oj1_position_controller/command', Float64, queue_size=10)
        
        self.pubyj5 = rospy.Publisher('/anael/yj5_position_controller/command', Float64, queue_size=10)
        self.pubyj4 = rospy.Publisher('/anael/yj4_position_controller/command', Float64, queue_size=10)
        self.pubyj3 = rospy.Publisher('/anael/yj3_position_controller/command', Float64, queue_size=10)
        self.pubyj1 = rospy.Publisher('/anael/yj1_position_controller/command', Float64, queue_size=10)
        
        self.pubsj5 = rospy.Publisher('/anael/sj5_position_controller/command', Float64, queue_size=10)
        self.pubsj4 = rospy.Publisher('/anael/sj4_position_controller/command', Float64, queue_size=10)
        self.pubsj3 = rospy.Publisher('/anael/sj3_position_controller/command', Float64, queue_size=10)
        self.pubsj1 = rospy.Publisher('/anael/sj1_position_controller/command', Float64, queue_size=10)
        
        self.pubbasj4 = rospy.Publisher('/anael/basj4_position_controller/command', Float64, queue_size=10)
        self.pubbasj3 = rospy.Publisher('/anael/basj3_position_controller/command', Float64, queue_size=10)
        self.pubbasj2 = rospy.Publisher('/anael/basj2_position_controller/command', Float64, queue_size=10)
        self.pubbasj1 = rospy.Publisher('/anael/basj1_position_controller/command', Float64, queue_size=10)
        
        self.pubbilekyaj = rospy.Publisher('/anael/bilekyaj_position_controller/command', Float64, queue_size=10)
        self.pubbilekssj = rospy.Publisher('/anael/bilekssj_position_controller/command', Float64, queue_size=10)

        self.positionij5 = Float64()
        self.positionij4 = Float64()
        self.positionij3 = Float64()
        self.positionij1 = Float64()
        
        self.positionoj5 = Float64()
        self.positionoj4 = Float64()
        self.positionoj3 = Float64()
        self.positionoj1 = Float64()
        
        self.positionyj5 = Float64()
        self.positionyj4 = Float64()
        self.positionyj3 = Float64()
        self.positionyj1 = Float64()
        
        self.positionsj5 = Float64()
        self.positionsj4 = Float64()
        self.positionsj3 = Float64()
        self.positionsj1 = Float64()
        
        self.positionbasj4 = Float64()
        self.positionbasj3 = Float64()
        self.positionbasj2 = Float64()
        self.positionbasj1 = Float64()
        
        self.positionbilekyaj = Float64()
        self.positionbilekssj = Float64()
        
    
        self.START_2.clicked.connect(self.timer)
        self.buton_q.clicked.connect(self.Q)
        self.buton_w.clicked.connect(self.W)
        self.buton_e.clicked.connect(self.E)
        self.buton_r.clicked.connect(self.R)
        self.buton_t.clicked.connect(self.T)
        self.buton_y.clicked.connect(self.Y)
        self.buton_u.clicked.connect(self.U)
        self.buton_i.clicked.connect(self.I)
        self.buton_o.clicked.connect(self.O)
        self.buton_p.clicked.connect(self.P)
        self.buton_a.clicked.connect(self.A)
        self.buton_s.clicked.connect(self.S)
        self.buton_d.clicked.connect(self.D)
        self.buton_f.clicked.connect(self.F)
        self.buton_g.clicked.connect(self.G)
        self.buton_h.clicked.connect(self.H)
        self.buton_j.clicked.connect(self.J)
        self.buton_k.clicked.connect(self.K)
        self.buton_l.clicked.connect(self.L)
        self.buton_z.clicked.connect(self.Z)
        self.buton_x.clicked.connect(self.X)
        self.buton_c.clicked.connect(self.C)
        self.buton_v.clicked.connect(self.V)
        self.buton_b.clicked.connect(self.B)
        self.buton_n.clicked.connect(self.N)
        self.buton_m.clicked.connect(self.M)
        self.buton_space.clicked.connect(self.space)
        self.buton_enter.clicked.connect(self.enter)
        self.button_gazebo.clicked.connect(self.kameraCallback) 
        self.Close.clicked.connect(self.stop_camera) 
        self.ok.clicked.connect(self.OK) 
   
        self.words = ['']  
        self.words1 = [''] 
        
        self.bridge = CvBridge()
        self.image_subscriber = rospy.Subscriber("camera/rgb/image_raw", Image, self.kameraCallback)
        

    def kameraCallback(self, mesaj):

            img = self.bridge.imgmsg_to_cv2(mesaj, "bgr8")
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img_rgb.shape
            bytesPerLine = ch * w
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(img_rgb.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888))
            self.updateImage(pixmap)
            QtWidgets.QApplication.processEvents()

    def updateImage(self, pixmap):
        self.gazebolabel.setPixmap(pixmap)
        self.gazebolabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def ses(self):
        
        self.words = speech_recognition.sestanıma()
        self.words = ''.join(self.words)
        self.textall.setText(self.words)
        
    def timer(self):
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.onClicked)
        self.timer.start(1)
    
    
    def start_camera(self,i):
       
       ret,frame = self.cap.read()
       if i==39:
           cv2.imwrite("temp.jpg",frame)
    #    self.rate.sleep()
       if ret:
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to QImage
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

            # Convert the QImage to QPixmap
            pixmap = QPixmap.fromImage(img)

            # Set the pixmap onto the label
            self.imgLabel.setPixmap(pixmap)

            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)



    def stop_camera(self):
        # Release the camera and stop the timer
        self.cap.release()
        self.timer.stop()   

    def onClicked(self):
        
        times = 40
        for i in range(times):
            # print(i)
            self.start_camera(i)
        
        self.Recognition()

    def Recognition(self):
        self.letter = rb.PredictviaCam()
        print("The next: ",self.letter)
        self.Textimage.setText(self.letter)
        
        
    def OK(self):
        self.words = list(self.words)
        self.words.append(self.letter)
     
        self.words = ''.join(self.words)
        self.textall.setText(self.words)
        
        

    def Q(self):
    
        self.words.append('Q')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def W(self):
         
        self.words.append('W')
        words = ''.join(self.words)
        self.textall.setText(words)
            
    def E(self):
        
        self.words.append('E')
        words = ''.join(self.words)
        self.textall.setText(words)
                 
    def R(self):
       
        self.words.append('R')
        words = ''.join(self.words)
        self.textall.setText(words)
            
    def T(self):
       
        self.words.append('T')
        words = ''.join(self.words)
        self.textall.setText(words)
    
    def Y(self):
        
        self.words.append('Y')
        words = ''.join(self.words)
        self.textall.setText(words)
    
        
    def U(self):
        
        self.words.append('U')
        words = ''.join(self.words)
        self.textall.setText(words)
                 
    def I(self):
        
        self.words.append('I')
        words = ''.join(self.words)
        self.textall.setText(words)
              
    def O(self):
       
        self.words.append('O')
        words = ''.join(self.words)
        self.textall.setText(words)
              
    def P(self):
        
        self.words.append('P')
        words = ''.join(self.words)
        self.textall.setText(words)
            
    def A(self):
    
        self.words.append('A')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def S(self):
      
        self.words.append('S')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def D(self):
      
        self.words.append('D')
        words = ''.join(self.words)
        self.textall.setText(words)
               
    def F(self):
        
        self.words.append('F')
        words = ''.join(self.words)
        self.textall.setText(words)
              
    def G(self):
      
        self.words.append('G')
        words = ''.join(self.words)
        self.textall.setText(words)
    
    def H(self):
       
        self.words.append('H')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def J(self):
        
        self.words.append('J')
        words = ''.join(self.words)
        self.textall.setText(words)
    
    def K(self):
        
        self.words.append('K')
        words = ''.join(self.words)
        self.textall.setText(words)
    
    def L(self):
         
        self.words.append('L')
        words = ''.join(self.words)
        self.textall.setText(words)
    
    def Z(self):

        self.words.append('Z')
        words = ''.join(self.words)
        self.textall.setText(words)
               
    def X(self):
         
        self.words.append('X')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def C(self):
             
        self.words.append('C')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def V(self):

        self.words.append('V')
        words = ''.join(self.words)
        self.textall.setText(words)
                    
    def B(self):
            
        self.words.append('B')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def N(self):
      
        self.words.append('N')
        words = ''.join(self.words)
        self.textall.setText(words)
        
    def M(self):
        
        self.words.append('M')
        words = ''.join(self.words)
        self.textall.setText(words)

    def space(self):
        
        self.words.append(' ')
        words = ''.join(self.words)
        self.textall.setText(words)

        
    def enter(self):
        self.words2= self.textall.text()
        self.textall.clear()
        self.words=list(self.words)

        for i in self.words:
            self.image_subscriber = rospy.Subscriber("camera/rgb/image_raw", Image, self.kameraCallback)
                                    
            self.rate.sleep()
            self.positionij5 = -0.1
            self.positionij4 = -0.1
            self.positionij3 = -0.1
            self.positionij1 = 0.0
            
            self.positionoj5 = -0.1
            self.positionoj4 = -0.1
            self.positionoj3 = -0.1
            self.positionoj1 = 0.0
            
            self.positionyj5 = -0.1
            self.positionyj4 = -0.1
            self.positionyj3 = -0.1
            self.positionyj1 = 0.0
            
            self.positionsj5 = -0.1
            self.positionsj4 = -0.1
            self.positionsj3 = -0.1
            self.positionsj1 = 0.0
            
            self.positionbasj4 = -0.1
            self.positionbasj3 = -0.1
            self.positionbasj2 = 0.0
            self.positionbasj1 = 0.0
            
            self.positionbilekyaj = 0.0
            self.positionbilekssj = 0.0
        
            #rospy.loginfo(position9)
            
            self.pubij1.publish(self.positionij1)
            self.pubij3.publish(self.positionij3)
            self.pubij4.publish(self.positionij4)
            self.pubij5.publish(self.positionij5)
            
            self.puboj1.publish(self.positionoj1)
            self.puboj3.publish(self.positionoj3)
            self.puboj4.publish(self.positionoj4)
            self.puboj5.publish(self.positionoj5)
            
            self.pubyj1.publish(self.positionyj1)
            self.pubyj3.publish(self.positionyj3)
            self.pubyj4.publish(self.positionyj4)
            self.pubyj5.publish(self.positionyj5)
            
            self.pubsj1.publish(self.positionsj1)
            self.pubsj3.publish(self.positionsj3)
            self.pubsj4.publish(self.positionsj4)
            self.pubsj5.publish(self.positionsj5)
            
            self.pubbasj1.publish(self.positionbasj1)
            self.pubbasj2.publish(self.positionbasj2)
            self.pubbasj3.publish(self.positionbasj3)
            self.pubbasj4.publish(self.positionbasj4)
            
            self.pubbilekyaj.publish(self.positionbilekyaj)
            self.pubbilekssj.publish(self.positionbilekssj)
                
            self.rate.sleep()
            
            
            if i=="Q" or i=="q":
              
                self.words1.append('Q')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -1.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                    
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 1.57
                self.positionbasj1 = 0.0
            
                self.positionbilekyaj = -1.4
                self.positionbilekssj = 0.0
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
            
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
                
                
                
            if i=="W"or i=="w":
           
                self.words1.append('W')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = -0.15
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.08
                self.positionyj4 = -0.08
                self.positionyj3 = -0.08
                self.positionyj1 = 0.15
                
                self.positionsj5 = -0.3
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.34
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -1.48
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
                
                
                
            if i=="E"or i=="e":
              
                self.words1.append('E')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -1.2
                self.positionij4 = -1.4
                self.positionij3 = -0.5
                self.positionij1 = 0.0
                 
                self.positionoj5 = -1.2
                self.positionoj4 = -1.4
                self.positionoj3 = -0.5
                self.positionoj1 = 0.0
            
                self.positionyj5 = -1.2
                self.positionyj4 = -1.4
                self.positionyj3 = -0.5
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.2
                self.positionsj4 = -1.4
                self.positionsj3 = -0.5
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.6
                self.positionbasj3 = -1.4
                self.positionbasj2 = 1.5
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                 #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
            
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
            
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
                 
        
            if i=="R"or i=="r":
             
                self.words1.append('R')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = 0.2
                    
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = -0.15
                
                self.positionyj5 = -1.48
                self.positionyj4 = -1.4
                self.positionyj3 = -1.1
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.48
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="T"or i=="t":
               
                self.words1.append('T')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.4
                self.positionij4 = -1.4
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                    
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.rate.sleep()
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.rate.sleep()
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                
                self.rate.sleep()
                

            if i=="Y" or i=="y":
                
                self.words1.append('Y')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.4
                self.positionij4 = -1.4
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.08
                self.positionsj4 = -0.08
                self.positionsj3 = -0.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 0.0
                self.positionbasj1 = 0.0
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="U" or i=="u":
                
                self.words1.append('U')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.1
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.4
                self.positionbasj1 = -0.24
                    
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                   
                   #rospy.loginfo(position9)
                   
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="I" or i=="i":
             
                self.words1.append('I')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.3
                self.positionij4 = -1.4
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.3
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.3
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.08
                self.positionsj4 = -0.08
                self.positionsj3 = -0.08
                self.positionsj1 = 0.1
                
                self.positionbasj4 = -0.6
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                    
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="O" or i=="o":
                
                self.words1.append('O')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.7
                self.positionij4 = -0.8
                self.positionij3 = -0.6
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.7
                self.positionoj4 = -0.8
                self.positionoj3 = -0.6
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.7
                self.positionyj4 = -0.8
                self.positionyj3 = -0.6
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.7
                self.positionsj4 = -0.8
                self.positionsj3 = -0.6
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.1
                self.positionbasj3 = -0.3
                self.positionbasj2 = 1.57
                self.positionbasj1 = 0.0
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="P" or i=="p":
               
                self.words1.append('P')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.2
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -1.48
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.48
                self.positionyj4 = -1.48
                self.positionyj3 = -1.48
                self.positionyj1 = 0.0
                    
                self.positionsj5 = -1.48
                self.positionsj4 = -1.48
                self.positionsj3 = -1.48
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.2
                self.positionbasj2 = 1.57
                self.positionbasj1 = 0.0
                
                self.positionbilekyaj = -1.2
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
    
            if i=="A" or i=="a":
              
                self.words1.append('A')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.2
                self.positionij4 = -1.4
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.2
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.2
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                    
                self.positionsj5 = -0.2
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 1.3
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                    
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="S" or i=="s":
               
                self.words1.append('S')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -1.4
                self.positionij4 = -1.4
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -1.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -1.0
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="D" or i=="d":
               
                self.words1.append('D')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.1
                self.positionij4 = -0.1
                self.positionij3 = -0.1
                self.positionij1 = 0.1
                
                self.positionoj5 = -0.7
                self.positionoj4 = -0.8
                self.positionoj3 = -1.0
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.7
                self.positionyj4 = -0.8
                self.positionyj3 = -1.0
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.7
                self.positionsj4 = -0.8
                self.positionsj3 = -1.0
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -1.4
                self.positionbasj2 = 1.2
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="F" or i=="f":
               
                self.words1.append('F')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.7
                self.positionij4 = -0.8
                self.positionij3 = -0.8
                self.positionij1 = 0.05
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.08
                self.positionyj4 = -0.08
                self.positionyj3 = -0.08
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.08
                self.positionsj4 = -0.08
                self.positionsj3 = -0.08
                self.positionsj1 = 0.15
                
                self.positionbasj4 = -1.0
                self.positionbasj3 = -0.1
                self.positionbasj2 = 1.0
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="G" or i=="g":
               
                self.words1.append('G')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -1.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 0.7
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = -1.4
                self.positionbilekssj = 0.78
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="H" or i=="h":
           
                self.words1.append('H')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = 0.1
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = 0.1
                
                self.positionyj5 = -0.2
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.2
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.6
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 1.4
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
                
            if i=="J" or i=="j":
              
                self.words1.append('J')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)  
                self.positionij5 = -0.3
                self.positionij4 = -1.4
                self.positionij3 = -1.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.3
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.3
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.08
                self.positionsj4 = -0.4
                self.positionsj3 = -0.08
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.6
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.4
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.78
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="K" or i=="k":
              
                self.words1.append('K')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.2
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.48
                self.positionyj4 = -1.48
                self.positionyj3 = -1.48
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.48
                self.positionsj4 = -1.48
                self.positionsj3 = -1.48
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.2
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="L" or i=="l":
               
                self.words1.append('L')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.1
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.1
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -0.1
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 0.0
                self.positionbasj1 = 0.0
                    
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
            
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="Z" or i=="z":
               
                self.words1.append('Z')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = 0.0
                
                self.positionoj5 = -1.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.4
                self.positionoj1 = 0.15
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.4
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.2
                self.positionbasj3 = -1.1
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
                
            if i=="X" or i=="x":
            
                self.words1.append('X')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)  
                self.positionij5 = -0.4
                self.positionij4 = -0.6
                self.positionij3 = -0.4
                self.positionij1 = 0.0
                
                self.positionoj5 = -1.4
                self.positionoj4 = -1.4
                self.positionoj3 = -1.1
                self.positionoj1 = 0.0
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.2
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.2
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
        
            if i=="C" or i=="c":
               
                self.words1.append('C')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.5
                self.positionij4 = -0.8
                self.positionij3 = -0.6
                self.positionij1 = 0.1
                
                self.positionoj5 = -0.5
                self.positionoj4 = -0.8
                self.positionoj3 = -0.6
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.5
                self.positionyj4 = -0.8
                self.positionyj3 = -0.6
                self.positionyj1 = -0.05
                
                self.positionsj5 = -0.5
                self.positionsj4 = -0.8
                self.positionsj3 = -0.6
                self.positionsj1 = -0.1
                
                self.positionbasj4 = -0.8
                self.positionbasj3 = -0.3
                self.positionbasj2 = 1.0
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
        
            if i=="V" or i=="v":
              
                self.words1.append('V')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = -0.15
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = 0.15
                
                self.positionyj5 = -1.4
                self.positionyj4 = -1.4
                self.positionyj3 = -1.1
                self.positionyj1 = 0.0
                
                self.positionsj5 = -1.4
                self.positionsj4 = -1.4
                self.positionsj3 = -1.4
                self.positionsj1 = 0.0
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -1.0
                self.positionbasj2 = 1.4
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                    
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.rate.sleep()
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
            if i=="B" or i=="b":
               
                self.words1.append('B')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -0.08
                self.positionij3 = -0.08
                self.positionij1 = 0.05
                
                self.positionoj5 = -0.08
                self.positionoj4 = -0.08
                self.positionoj3 = -0.08
                self.positionoj1 = 0.0
                
                self.positionyj5 = -0.08
                self.positionyj4 = -0.08
                self.positionyj3 = -0.08
                self.positionyj1 = -0.05
                
                self.positionsj5 = -0.08
                self.positionsj4 = -0.08
                self.positionsj3 = -0.08
                self.positionsj1 = -0.05
                
                self.positionbasj4 = -0.2
                self.positionbasj3 = -1.4
                self.positionbasj2 = 1.5
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                        
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
        
            if i=="N" or i=="n":
               
                self.words1.append('N')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -1.2
                self.positionij3 = -1.2
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.08
                self.positionoj4 = -1.2
                self.positionoj3 = -1.2
                self.positionoj1 = 0.15
                
                self.positionyj5 = -0.4
                self.positionyj4 = -1.48
                self.positionyj3 = -1.18
                self.positionyj1 = 0.34
                
                self.positionsj5 = -0.4
                self.positionsj4 = -1.48
                self.positionsj3 = -1.48
                self.positionsj1 = 0.34
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.rate.sleep()
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.rate.sleep()
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                self.rate.sleep()
                
                self.rate.sleep()
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.rate.sleep()
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.rate.sleep()
                
                
                
            if i=="M" or i=="m":
                
                self.words1.append('M')
                words1 = ''.join(self.words1)
                self.textall.setText(words1)
                self.positionij5 = -0.08
                self.positionij4 = -1.2
                self.positionij3 = -1.3
                self.positionij1 = 0.0
                
                self.positionoj5 = -0.08
                self.positionoj4 = -1.2
                self.positionoj3 = -1.3
                self.positionoj1 = 0.15
                
                self.positionyj5 = -0.08
                self.positionyj4 = -1.1
                self.positionyj3 = -1.3
                self.positionyj1 = 0.34
                
                self.positionsj5 = -0.3
                self.positionsj4 = -1.4
                self.positionsj3 = -1.44
                self.positionsj1 = 0.34
                
                self.positionbasj4 = -0.08
                self.positionbasj3 = -0.08
                self.positionbasj2 = 1.57
                self.positionbasj1 = -0.24
                
                self.positionbilekyaj = 0.0
                self.positionbilekssj = 0.0
                
                #rospy.loginfo(position9)
                
                self.rate.sleep()
                self.pubsj1.publish(self.positionsj1)
                self.pubsj3.publish(self.positionsj3)
                self.pubsj4.publish(self.positionsj4)
                self.pubsj5.publish(self.positionsj5)
                
                self.rate.sleep()
                self.pubbasj1.publish(self.positionbasj1)
                self.pubbasj2.publish(self.positionbasj2)
                self.pubbasj3.publish(self.positionbasj3)
                self.pubbasj4.publish(self.positionbasj4)
                
                self.pubbilekyaj.publish(self.positionbilekyaj)
                self.pubbilekssj.publish(self.positionbilekssj)
                
                self.rate.sleep()
                self.pubij1.publish(self.positionij1)
                self.pubij3.publish(self.positionij3)
                self.pubij4.publish(self.positionij4)
                self.pubij5.publish(self.positionij5)
                
                self.rate.sleep()
                self.puboj1.publish(self.positionoj1)
                self.puboj3.publish(self.positionoj3)
                self.puboj4.publish(self.positionoj4)
                self.puboj5.publish(self.positionoj5)
                
                self.rate.sleep()
                self.pubyj1.publish(self.positionyj1)
                self.pubyj3.publish(self.positionyj3)
                self.pubyj4.publish(self.positionyj4)
                self.pubyj5.publish(self.positionyj5)
                
                self.rate.sleep()
                
        self.textfeedback.append(self.words2) 
        self.words2=list(self.words2)
        self.words.clear()
        self.words2.clear()
        self.words1.clear()
        self.textall.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
