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
from PySide6.QtGui import (QAction, QActionGroup, QBrush, QColor,
    QConicalGradient, QCursor, QFont, QFontDatabase,
    QGradient, QIcon, QImage, QKeySequence,
    QLinearGradient, QPainter, QPalette, QPixmap,
    QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_mw_main(object):
    def setupUi(self, mw_main):
        if not mw_main.objectName():
            mw_main.setObjectName(u"mw_main")
        mw_main.resize(776, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mw_main.sizePolicy().hasHeightForWidth())
        mw_main.setSizePolicy(sizePolicy)
        mw_main.setMinimumSize(QSize(776, 200))
        mw_main.setMaximumSize(QSize(16777215, 16777215))
        mw_main.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        mw_main.setFont(font)
        mw_main.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
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
        self.actionLight = QAction(mw_main)
        self.actionLight.setObjectName(u"actionLight")
        self.actionLight.setCheckable(True)
        self.actionLight.setFont(font)
        self.actionDark = QAction(mw_main)
        self.actionDark.setObjectName(u"actionDark")
        self.actionDark.setCheckable(True)
        self.actionDark.setFont(font)
        self.actionSystem = QAction(mw_main)
        self.actionSystem.setObjectName(u"actionSystem")
        self.actionSystem.setCheckable(True)
        self.actionSystem.setChecked(True)
        self.actionSystem.setFont(font)
        self.group_view = QActionGroup(mw_main)
        self.group_view.setObjectName(u"group_view")
        self.action_light = QAction(self.group_view)
        self.action_light.setObjectName(u"action_light")
        self.action_light.setCheckable(True)
        self.action_dark = QAction(self.group_view)
        self.action_dark.setObjectName(u"action_dark")
        self.action_dark.setCheckable(True)
        self.action_system = QAction(self.group_view)
        self.action_system.setObjectName(u"action_system")
        self.action_system.setCheckable(True)
        self.action_system.setChecked(True)
        self.centralwidget = QWidget(mw_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_sourceFile = QLineEdit(self.centralwidget)
        self.le_sourceFile.setObjectName(u"le_sourceFile")

        self.horizontalLayout.addWidget(self.le_sourceFile)

        self.pb_srcBrowse = QPushButton(self.centralwidget)
        self.pb_srcBrowse.setObjectName(u"pb_srcBrowse")

        self.horizontalLayout.addWidget(self.pb_srcBrowse)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ck_start_index = QCheckBox(self.groupBox)
        self.ck_start_index.setObjectName(u"ck_start_index")
        self.ck_start_index.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ck_start_index.sizePolicy().hasHeightForWidth())
        self.ck_start_index.setSizePolicy(sizePolicy)
        self.ck_start_index.setChecked(False)

        self.horizontalLayout_3.addWidget(self.ck_start_index)

        self.sb_start_index = QSpinBox(self.groupBox)
        self.sb_start_index.setObjectName(u"sb_start_index")
        self.sb_start_index.setEnabled(False)
        self.sb_start_index.setMaximum(288)

        self.horizontalLayout_3.addWidget(self.sb_start_index)

        self.horizontalSpacer_2 = QSpacerItem(17, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sb_end_index = QSpinBox(self.groupBox)
        self.sb_end_index.setObjectName(u"sb_end_index")
        self.sb_end_index.setMaximum(288)

        self.horizontalLayout_3.addWidget(self.sb_end_index)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.cb_channels = QComboBox(self.groupBox)
        self.cb_channels.addItem("")
        self.cb_channels.addItem("")
        self.cb_channels.addItem("")
        self.cb_channels.addItem("")
        self.cb_channels.setObjectName(u"cb_channels")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_channels.sizePolicy().hasHeightForWidth())
        self.cb_channels.setSizePolicy(sizePolicy1)
        self.cb_channels.setMinimumSize(QSize(50, 0))
        self.cb_channels.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.cb_channels)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.cb_grouping = QComboBox(self.groupBox)
        self.cb_grouping.addItem("")
        self.cb_grouping.addItem("")
        self.cb_grouping.addItem("")
        self.cb_grouping.addItem("")
        self.cb_grouping.setObjectName(u"cb_grouping")

        self.horizontalLayout_3.addWidget(self.cb_grouping)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.ck_leadingZero = QCheckBox(self.groupBox)
        self.ck_leadingZero.setObjectName(u"ck_leadingZero")
        self.ck_leadingZero.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout_3.addWidget(self.ck_leadingZero)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_outputFile = QLineEdit(self.centralwidget)
        self.le_outputFile.setObjectName(u"le_outputFile")

        self.horizontalLayout_2.addWidget(self.le_outputFile)

        self.pb_outBrowse = QPushButton(self.centralwidget)
        self.pb_outBrowse.setObjectName(u"pb_outBrowse")

        self.horizontalLayout_2.addWidget(self.pb_outBrowse)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_shuffle = QPushButton(self.centralwidget)
        self.pb_shuffle.setObjectName(u"pb_shuffle")

        self.horizontalLayout_4.addWidget(self.pb_shuffle)

        self.pb_quit = QPushButton(self.centralwidget)
        self.pb_quit.setObjectName(u"pb_quit")

        self.horizontalLayout_4.addWidget(self.pb_quit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        mw_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 776, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setFont(font)
        mw_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_main)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        mw_main.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.le_sourceFile, self.pb_srcBrowse)
        QWidget.setTabOrder(self.pb_srcBrowse, self.ck_start_index)
        QWidget.setTabOrder(self.ck_start_index, self.sb_start_index)
        QWidget.setTabOrder(self.sb_start_index, self.sb_end_index)
        QWidget.setTabOrder(self.sb_end_index, self.cb_channels)
        QWidget.setTabOrder(self.cb_channels, self.cb_grouping)
        QWidget.setTabOrder(self.cb_grouping, self.ck_leadingZero)
        QWidget.setTabOrder(self.ck_leadingZero, self.le_outputFile)
        QWidget.setTabOrder(self.le_outputFile, self.pb_outBrowse)
        QWidget.setTabOrder(self.pb_outBrowse, self.pb_shuffle)
        QWidget.setTabOrder(self.pb_shuffle, self.pb_quit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_shuffle)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuView.addAction(self.action_light)
        self.menuView.addAction(self.action_dark)
        self.menuView.addAction(self.action_system)

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
        self.actionLight.setText(QCoreApplication.translate("mw_main", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("mw_main", u"Dark", None))
        self.actionSystem.setText(QCoreApplication.translate("mw_main", u"System", None))
        self.action_light.setText(QCoreApplication.translate("mw_main", u"&Light", None))
        self.action_dark.setText(QCoreApplication.translate("mw_main", u"&Dark", None))
        self.action_system.setText(QCoreApplication.translate("mw_main", u"&System", None))
        self.label.setText(QCoreApplication.translate("mw_main", u"Source File", None))
#if QT_CONFIG(tooltip)
        self.pb_srcBrowse.setToolTip(QCoreApplication.translate("mw_main", u"Find source file exported from Ultrix Sources table.", None))
#endif // QT_CONFIG(tooltip)
        self.pb_srcBrowse.setText(QCoreApplication.translate("mw_main", u"Browse...", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.ck_start_index.setToolTip(QCoreApplication.translate("mw_main", u"Set the index of the first source to use to generate audio sources.", None))
#endif // QT_CONFIG(tooltip)
        self.ck_start_index.setText(QCoreApplication.translate("mw_main", u"Start Index", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("mw_main", u"Set the index of the last source to use to generate audio sources.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("mw_main", u"End Index", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("mw_main", u"Set how many audio channels are in the database.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("mw_main", u"Channels", None))
        self.cb_channels.setItemText(0, QCoreApplication.translate("mw_main", u"16", None))
        self.cb_channels.setItemText(1, QCoreApplication.translate("mw_main", u"8", None))
        self.cb_channels.setItemText(2, QCoreApplication.translate("mw_main", u"4", None))
        self.cb_channels.setItemText(3, QCoreApplication.translate("mw_main", u"2", None))

#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("mw_main", u"Set how you would like the audio to be grouped.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("mw_main", u"Grouping", None))
        self.cb_grouping.setItemText(0, QCoreApplication.translate("mw_main", u"Mono", None))
        self.cb_grouping.setItemText(1, QCoreApplication.translate("mw_main", u"Stereo", None))
        self.cb_grouping.setItemText(2, QCoreApplication.translate("mw_main", u"Quad", None))
        self.cb_grouping.setItemText(3, QCoreApplication.translate("mw_main", u"Octo", None))

#if QT_CONFIG(tooltip)
        self.ck_leadingZero.setToolTip(QCoreApplication.translate("mw_main", u"Check to enable leading zeroes on single digit numbers.", None))
#endif // QT_CONFIG(tooltip)
        self.ck_leadingZero.setText(QCoreApplication.translate("mw_main", u"Leading Zeroes", None))
        self.label_2.setText(QCoreApplication.translate("mw_main", u"Output File", None))
#if QT_CONFIG(tooltip)
        self.pb_outBrowse.setToolTip(QCoreApplication.translate("mw_main", u"Set or use autogenerated default file path for output file.", None))
#endif // QT_CONFIG(tooltip)
        self.pb_outBrowse.setText(QCoreApplication.translate("mw_main", u"Browse...", None))
#if QT_CONFIG(tooltip)
        self.pb_shuffle.setToolTip(QCoreApplication.translate("mw_main", u"Generate audio shuffling sources based on options set above.", None))
#endif // QT_CONFIG(tooltip)
        self.pb_shuffle.setText(QCoreApplication.translate("mw_main", u"&Shuffle", None))
#if QT_CONFIG(tooltip)
        self.pb_quit.setToolTip(QCoreApplication.translate("mw_main", u"Exit the application.", None))
#endif // QT_CONFIG(tooltip)
        self.pb_quit.setText(QCoreApplication.translate("mw_main", u"&Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_main", u"&File", None))
        self.menuView.setTitle(QCoreApplication.translate("mw_main", u"&View", None))
    # retranslateUi

