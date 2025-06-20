# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QWidget)
import icons_rc

class Ui_mw_main(object):
    def setupUi(self, mw_main):
        if not mw_main.objectName():
            mw_main.setObjectName(u"mw_main")
        mw_main.resize(702, 225)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mw_main.sizePolicy().hasHeightForWidth())
        mw_main.setSizePolicy(sizePolicy)
        mw_main.setMinimumSize(QSize(700, 225))
        mw_main.setMaximumSize(QSize(16777215, 225))
        mw_main.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        mw_main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/Ultrix_U.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mw_main.setWindowIcon(icon)
        self.action_quit = QAction(mw_main)
        self.action_quit.setObjectName(u"action_quit")
        self.action_quit.setFont(font)
        self.action_open = QAction(mw_main)
        self.action_open.setObjectName(u"action_open")
        self.action_open.setFont(font)
        self.action_shuffle = QAction(mw_main)
        self.action_shuffle.setObjectName(u"action_shuffle")
        self.action_shuffle.setFont(font)
        self.centralwidget = QWidget(mw_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.pb_go = QPushButton(self.centralwidget)
        self.pb_go.setObjectName(u"pb_go")
        sizePolicy.setHeightForWidth(self.pb_go.sizePolicy().hasHeightForWidth())
        self.pb_go.setSizePolicy(sizePolicy)
        self.pb_go.setMinimumSize(QSize(75, 0))

        self.gridLayout_2.addWidget(self.pb_go, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.pb_quit = QPushButton(self.centralwidget)
        self.pb_quit.setObjectName(u"pb_quit")

        self.gridLayout_2.addWidget(self.pb_quit, 2, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cb_channels = QComboBox(self.widget)
        self.cb_channels.addItem("")
        self.cb_channels.addItem("")
        self.cb_channels.addItem("")
        self.cb_channels.addItem("")
        self.cb_channels.setObjectName(u"cb_channels")
        sizePolicy.setHeightForWidth(self.cb_channels.sizePolicy().hasHeightForWidth())
        self.cb_channels.setSizePolicy(sizePolicy)
        self.cb_channels.setMinimumSize(QSize(0, 0))
        self.cb_channels.setMaximumSize(QSize(55, 16777215))

        self.gridLayout.addWidget(self.cb_channels, 1, 4, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.pb_srcBrowse = QPushButton(self.widget)
        self.pb_srcBrowse.setObjectName(u"pb_srcBrowse")

        self.gridLayout.addWidget(self.pb_srcBrowse, 0, 9, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 8, 1, 1)

        self.cb_grouping = QComboBox(self.widget)
        self.cb_grouping.addItem("")
        self.cb_grouping.addItem("")
        self.cb_grouping.addItem("")
        self.cb_grouping.addItem("")
        self.cb_grouping.setObjectName(u"cb_grouping")
        sizePolicy.setHeightForWidth(self.cb_grouping.sizePolicy().hasHeightForWidth())
        self.cb_grouping.setSizePolicy(sizePolicy)
        self.cb_grouping.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.cb_grouping, 1, 7, 1, 1)

        self.sb_index = QSpinBox(self.widget)
        self.sb_index.setObjectName(u"sb_index")
        self.sb_index.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.sb_index.setMaximum(287)

        self.gridLayout.addWidget(self.sb_index, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.ck_leadingZero = QCheckBox(self.widget)
        self.ck_leadingZero.setObjectName(u"ck_leadingZero")

        self.gridLayout.addWidget(self.ck_leadingZero, 1, 9, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 5, 1, 1)

        self.le_outputFile = QLineEdit(self.widget)
        self.le_outputFile.setObjectName(u"le_outputFile")

        self.gridLayout.addWidget(self.le_outputFile, 2, 1, 1, 8)

        self.le_sourceFile = QLineEdit(self.widget)
        self.le_sourceFile.setObjectName(u"le_sourceFile")

        self.gridLayout.addWidget(self.le_sourceFile, 0, 1, 1, 8)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 6, 1, 1)

        self.pb_outBrowse = QPushButton(self.widget)
        self.pb_outBrowse.setObjectName(u"pb_outBrowse")

        self.gridLayout.addWidget(self.pb_outBrowse, 2, 9, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 10)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 4)

        mw_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 702, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        mw_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_main)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        mw_main.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.le_sourceFile, self.pb_srcBrowse)
        QWidget.setTabOrder(self.pb_srcBrowse, self.sb_index)
        QWidget.setTabOrder(self.sb_index, self.cb_channels)
        QWidget.setTabOrder(self.cb_channels, self.cb_grouping)
        QWidget.setTabOrder(self.cb_grouping, self.ck_leadingZero)
        QWidget.setTabOrder(self.ck_leadingZero, self.le_outputFile)
        QWidget.setTabOrder(self.le_outputFile, self.pb_outBrowse)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_shuffle)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)

        self.retranslateUi(mw_main)

        QMetaObject.connectSlotsByName(mw_main)
    # setupUi

    def retranslateUi(self, mw_main):
        mw_main.setWindowTitle(QCoreApplication.translate("mw_main", u"Ultrix Audio Shuffling Generator", None))
        self.action_quit.setText(QCoreApplication.translate("mw_main", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.action_quit.setShortcut(QCoreApplication.translate("mw_main", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("mw_main", u"&Open...", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("mw_main", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_shuffle.setText(QCoreApplication.translate("mw_main", u"&Shuffle", None))
#if QT_CONFIG(shortcut)
        self.action_shuffle.setShortcut(QCoreApplication.translate("mw_main", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.pb_go.setText(QCoreApplication.translate("mw_main", u"&Shuffle", None))
        self.pb_quit.setText(QCoreApplication.translate("mw_main", u"Quit", None))
        self.label.setText(QCoreApplication.translate("mw_main", u"Source File", None))
        self.cb_channels.setItemText(0, QCoreApplication.translate("mw_main", u"16", None))
        self.cb_channels.setItemText(1, QCoreApplication.translate("mw_main", u"8", None))
        self.cb_channels.setItemText(2, QCoreApplication.translate("mw_main", u"4", None))
        self.cb_channels.setItemText(3, QCoreApplication.translate("mw_main", u"2", None))

        self.label_4.setText(QCoreApplication.translate("mw_main", u"Audio Channels", None))
        self.pb_srcBrowse.setText(QCoreApplication.translate("mw_main", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("mw_main", u"Output File", None))
        self.cb_grouping.setItemText(0, QCoreApplication.translate("mw_main", u"Mono", None))
        self.cb_grouping.setItemText(1, QCoreApplication.translate("mw_main", u"Stereo", None))
        self.cb_grouping.setItemText(2, QCoreApplication.translate("mw_main", u"Quad", None))
        self.cb_grouping.setItemText(3, QCoreApplication.translate("mw_main", u"Octo", None))

        self.ck_leadingZero.setText(QCoreApplication.translate("mw_main", u"Leading Zero", None))
        self.label_5.setText(QCoreApplication.translate("mw_main", u"End Index", None))
        self.label_3.setText(QCoreApplication.translate("mw_main", u"Audio Grouping", None))
        self.pb_outBrowse.setText(QCoreApplication.translate("mw_main", u"Browse", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_main", u"&File", None))
    # retranslateUi

