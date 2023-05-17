import cv2
import numpy as np
import PIL.Image as Img
import PIL.ImageEnhance as Enhance
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

from uidb_from_bat import Ui_Dialog as DialogForm


class Ui_MainWindow(object):
    def __init__(self):
        self.db_name = 'sppr.sqlite'
        self.image_path = ''
        self.transformed_image_as_array = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 550)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(515, 250, 125, 31))
        self.comboBox.setObjectName("comboBox")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(495, 250, 20, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(515, 290, 91, 31))
        self.changeButton.setObjectName("changeButton")

        self.shotButton = QtWidgets.QPushButton(MainWindow)
        self.shotButton.setGeometry(QtCore.QRect(515, 420, 91, 31))
        self.shotButton.setObjectName("shotButton")

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(515, 450, 145, 31))
        self.saveButton.setObjectName("push_button_delete")

        self.pore_area_label = QtWidgets.QLabel(self.centralwidget)
        self.pore_area_label.setGeometry(640, 255, 100, 16)
        self.pore_area_label.setObjectName("pore_area_label")

        self.pore_area_value_label = QtWidgets.QLabel(self.centralwidget)
        self.pore_area_value_label.setGeometry(640, 275, 100, 16)
        self.pore_area_value_label.setObjectName("pore_area_value_label")

        self.pore_area_std_label = QtWidgets.QLabel(self.centralwidget)
        self.pore_area_std_label.setGeometry(640, 295, 100, 16)
        self.pore_area_std_label.setObjectName("pore_area_std_label")

        self.pore_area_std_value_label = QtWidgets.QLabel(self.centralwidget)
        self.pore_area_std_value_label.setGeometry(680, 295, 100, 16)
        self.pore_area_std_value_label.setObjectName("pore_area_std_value_label")

        self.porous_label = QtWidgets.QLabel(self.centralwidget)
        self.porous_label.setGeometry(640, 330, 100, 16)
        self.porous_label.setObjectName("porous_label")

        self.porous_value_label = QtWidgets.QLabel(self.centralwidget)
        self.porous_value_label.setGeometry(640, 350, 100, 16)
        self.porous_value_label.setObjectName("porous_value_label")

        self.porous_std_label = QtWidgets.QLabel(self.centralwidget)
        self.porous_std_label.setGeometry(640, 370, 100, 16)
        self.porous_std_label.setObjectName("porous_std_label")

        self.porous_std_value_label = QtWidgets.QLabel(self.centralwidget)
        self.porous_std_value_label.setGeometry(680, 370, 100, 16)
        self.porous_std_value_label.setObjectName("porous_std_value_label")

        self.pore_number_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.pore_number_label_1.setGeometry(QtCore.QRect(280, 380, 180, 16))
        self.pore_number_label_1.setObjectName("pore_number_label_1")

        self.pore_number_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pore_number_label_2.setGeometry(QtCore.QRect(280, 400, 180, 16))
        self.pore_number_label_2.setObjectName("pore_number_label_2")

        self.pore_number_value_label = QtWidgets.QLabel(self.centralwidget)
        self.pore_number_value_label.setGeometry(QtCore.QRect(280, 420, 180, 16))
        self.pore_number_value_label.setObjectName("pore_number_value_label")

        self.report_lable_1 = QtWidgets.QLabel(self.centralwidget)
        self.report_lable_1.setGeometry(QtCore.QRect(280, 300, 180, 16))
        self.report_lable_1.setObjectName("report_lable_1")

        self.report_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.report_label_2.setGeometry(QtCore.QRect(280, 320, 180, 16))
        self.report_label_2.setObjectName("report_label_2")

        self.report_porous_number_label = QtWidgets.QLabel(self.centralwidget)
        self.report_porous_number_label.setGeometry(QtCore.QRect(365, 320, 180, 16))
        self.report_porous_number_label.setObjectName("report_porous_number_label")

        self.report_porous_status_label = QtWidgets.QLabel(self.centralwidget)
        self.report_porous_status_label.setGeometry(QtCore.QRect(280, 340, 180, 16))
        self.report_porous_status_label.setObjectName("report_porous_status_label")

        self.report_porous_status_value_label = QtWidgets.QLabel(self.centralwidget)
        self.report_porous_status_value_label.setGeometry(QtCore.QRect(365, 340, 180, 16))
        self.report_porous_status_value_label.setObjectName("report_porous_status_value_label")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 0, 480, 500))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.transform_img = QtWidgets.QLabel(self.widget)
        self.transform_img.setObjectName('transform_image')
        self.gridLayout.addWidget(self.transform_img, 0, 0, 1, 1)

        self.transformed_frame = QtWidgets.QLabel(self.widget)
        self.transformed_frame.setObjectName('transformed_frame')
        self.gridLayout.addWidget(self.transformed_frame, 0, 1, 1, 1)

        self.explored_img = QtWidgets.QLabel(self.widget)
        self.explored_img.setObjectName('explored_img')
        self.gridLayout.addWidget(self.explored_img, 1, 0, 1, 1)

        self.slider_widgets = QtWidgets.QWidget(self.centralwidget)
        self.slider_widgets.setGeometry(QtCore.QRect(500, 20, 231, 191))
        self.slider_widgets.setObjectName("slider_widgets")

        self.slider_layout = QtWidgets.QVBoxLayout(self.slider_widgets)
        self.slider_layout.setContentsMargins(0, 0, 0, 0)
        self.slider_layout.setObjectName("slider_layout")

        self.contrast_widget = QtWidgets.QWidget(self.slider_widgets)
        self.contrast_widget.setObjectName("contrast_widget")

        self.contrast_slider = QtWidgets.QSlider(self.contrast_widget)
        self.contrast_slider.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.contrast_slider.setMouseTracking(False)
        self.contrast_slider.setAutoFillBackground(True)
        self.contrast_slider.setValue(50)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setInvertedAppearance(False)
        self.contrast_slider.setRange(-200, 200)
        self.contrast_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.contrast_slider.setObjectName("contrast_slider")

        self.contrast_label = QtWidgets.QLabel(self.contrast_widget)
        self.contrast_label.setGeometry(QtCore.QRect(10, 10, 100, 16))
        self.contrast_label.setObjectName("contrast_label")
        self.slider_layout.addWidget(self.contrast_widget)

        self.brightness_widget = QtWidgets.QWidget(self.slider_widgets)
        self.brightness_widget.setObjectName("brightness_widget")

        self.brightness_slider = QtWidgets.QSlider(self.brightness_widget)
        self.brightness_slider.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.brightness_slider.setMouseTracking(False)
        self.brightness_slider.setAutoFillBackground(True)
        self.brightness_slider.setValue(50)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setInvertedAppearance(False)
        self.brightness_slider.setRange(-200, 200)
        self.brightness_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.brightness_slider.setObjectName("brightness_slider")

        self.brightness_label = QtWidgets.QLabel(self.brightness_widget)
        self.brightness_label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.brightness_label.setObjectName("brightness_label")
        self.slider_layout.addWidget(self.brightness_widget)

        self.sharpness_widget = QtWidgets.QWidget(self.slider_widgets)
        self.sharpness_widget.setObjectName("sharpness_widget")

        self.sharpness_slider = QtWidgets.QSlider(self.sharpness_widget)
        self.sharpness_slider.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.sharpness_slider.setMouseTracking(False)
        self.sharpness_slider.setAutoFillBackground(True)
        self.sharpness_slider.setValue(50)
        self.sharpness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sharpness_slider.setInvertedAppearance(False)
        self.sharpness_slider.setRange(-200, 200)
        self.sharpness_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sharpness_slider.setObjectName("sharpness_slider")

        self.sharpness_label = QtWidgets.QLabel(self.sharpness_widget)
        self.sharpness_label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.sharpness_label.setObjectName("sharpness_label")
        self.slider_layout.addWidget(self.sharpness_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setObjectName("open_action")
        self.menu.addAction(self.open_action)

        self.webcam_action = QtWidgets.QAction(MainWindow)
        self.webcam_action.setObjectName("webcam_action")
        self.menu.addAction(self.webcam_action)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quality porous material"))

        self.changeButton.setText(_translate("MainWindow", "Изменить"))
        self.changeButton.clicked.connect(self.open_dialog)

        self.shotButton.setText(_translate("MainWindow", "Снимок"))
        self.shotButton.clicked.connect(self.explore_img)
        self.saveButton.setText(_translate("MainWindow", "Сохранить в отчет"))

        self.pore_area_label.setText(_translate("MainWindow", "Площадь поры"))
        self.porous_label.setText(_translate("MainWindow", "Пористость"))
        self.porous_std_label.setText(_translate('MainWindow', 'Откл. '))
        self.pore_area_std_label.setText(_translate('MainWindow', 'Откл. '))

        self.pore_number_label_1.setText(_translate("MainWindow", "Количество пор, площадь"))
        self.pore_number_label_2.setText(_translate("MainWindow", "которых превышает норму:"))

        self.report_lable_1.setText(_translate("MainWindow", "Отчет:"))
        self.report_label_2.setText(_translate("MainWindow", "пористость = "))
        self.report_porous_status_label.setText(_translate("MainWindow", "пористость"))

        self.contrast_label.setText(_translate("MainWindow", "контрастность"))
        self.brightness_label.setText(_translate("MainWindow", "яркость"))
        self.sharpness_label.setText(_translate("MainWindow", "резкость"))

        self.menu.setTitle(_translate("MainWindow", "Исходные данные для анализа"))
        self.open_action.setText(_translate("MainWindow", "Open"))
        self.open_action.setShortcut(QtGui.QKeySequence.Open)
        self.open_action.setStatusTip(_translate("MainWindow", "Open an existing file"))
        self.open_action.triggered.connect(self.open_image)
        self.webcam_action.setText(_translate("MainWindow", "Webcam"))

        self.contrast_slider.actionTriggered.connect(self.slider_triggered)
        self.brightness_slider.actionTriggered.connect(self.slider_triggered)
        self.sharpness_slider.actionTriggered.connect(self.slider_triggered)

        self.set_up_combo()

    def set_up_combo(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        self.comboBox.clear()
        for row in cur.execute('SELECT NAME FROM Materials'):
            self.comboBox.addItem(row[0])
        conn.close()

        self.comboBox.activated[str].connect(self.combo_on_activated)

    def combo_on_activated(self, text):
        self.set_up_combo()
        try:
            conn = sqlite3.connect(self.db_name)
            cur = conn.cursor()
            res = cur.execute(
                f'''
                    SELECT PORE_AREA_MEAN, PORE_AREA_STD, POROUS_MEAN, POROUS_STD 
                    FROM Materials 
                    WHERE NAME="{text}"
                '''
            )
            res = res.fetchone()
            conn.close()

            self.comboBox.setCurrentText(text)
            self.pore_area_value_label.setText(f'{res[0]}')
            self.pore_area_std_value_label.setText(f'{res[1]}')
            self.porous_value_label.setText(f'{res[2]}')
            self.porous_std_value_label.setText(f'{res[3]}')
        except TypeError:
            self.pore_area_value_label.setText('')
            self.pore_area_std_value_label.setText('')
            self.porous_value_label.setText('')
            self.porous_std_value_label.setText('')
        except Exception as e:
            raise e

    @staticmethod
    def open_dialog():
        dialog = QtWidgets.QDialog()
        dialog.ui = DialogForm()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_image(self):
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName()

        if image_path:
            pixmap = QtGui.QPixmap(image_path)
            pixmap = pixmap.scaled(self.transform_img.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
            self.transform_img.setPixmap(pixmap)
            self.image_path = image_path

    def set_transformed_frame(self, image_path):
        image = Img.open(image_path)

        image = Enhance.Contrast(image).enhance(self.contrast_slider.value()/10)
        image = Enhance.Brightness(image).enhance(self.brightness_slider.value() / 10)
        image = Enhance.Sharpness(image).enhance(self.sharpness_slider.value() / 10)

        image = np.array(image)
        self.transformed_image_as_array = np.copy(image)
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        pixmap = pixmap.scaled(self.transformed_frame.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        self.transformed_frame.setPixmap(pixmap)

    def slider_triggered(self):
        if self.transform_img.pixmap():
            self.set_transformed_frame(self.image_path)

    def explore(self, image):
        """
        Входной параметр:
            image - исследуемое изображение
        Выход:
            image - изображение с контурами пор
            area_c - отношение площади всех пор ко всей площади изображения (пористость)
            len(bad_conrours) - количество 'плохих' пор
        """
        image = np.copy(image)

        # дополнительная обработка шумов
        blured = cv2.GaussianBlur(image, (5, 5), 0)

        # конвертация BGR формата в формат HSV
        hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)

        lower_black = np.array([0, 0, 0])
        upper_black = np.array([120, 120, 120])

        # определяем маску для обнаружения контуров пор.
        # будут выделены поры в заданном диапозоне
        mask = cv2.inRange(hsv, lower_black, upper_black)

        # получаем массив конутров
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        good_contours = []
        bad_contours = []
        area_c = 0
        # находим поры, не превышающие нормативную площадь
        for contour in contours:
            # также подсчитываем общую площадь пор
            area_c += cv2.contourArea(contour)
            try:
                if float(self.pore_area_value_label.text()) - float(self.pore_area_std_value_label.text()) \
                        <= cv2.contourArea(contour) \
                        <= float(self.pore_area_value_label.text()) + float(self.pore_area_std_value_label.text()):
                    good_contours.append(contour)
                else:
                    bad_contours.append(contour)
            except ValueError:
                raise ValueError
            except Exception as e:
                raise e
        area_c = area_c / (image.shape[0] * image.shape[1])
        # выделяем 'хорошие' поры зеленым цветом
        cv2.drawContours(image, good_contours, -1, (0, 255, 0), 3)
        # выделяем 'плохие' поры красным цветом
        cv2.drawContours(image, bad_contours, -1, (255, 0, 0), 3)

        return image, area_c, len(bad_contours)

    def explore_img(self):
        try:
            image, area_c, bad_contours_number = self.explore(self.transformed_image_as_array)
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(image)
            pixmap = pixmap.scaled(self.explored_img.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
            self.explored_img.setPixmap(pixmap)
            self.report_porous_number_label.setText(f'{area_c:.7f}')
            self.pore_number_value_label.setText(f'{bad_contours_number}')
            if area_c > float(self.porous_value_label.text()):
                self.pore_number_value_label.setStyleSheet("color: red")
                self.report_porous_status_value_label.setText("выше нормы")
                self.report_porous_status_value_label.setStyleSheet("color: red")
            else:
                self.pore_number_value_label.setStyleSheet("color: green")
                self.report_porous_status_value_label.setText("в норме")
                self.report_porous_status_value_label.setStyleSheet("color: green")

        except ValueError:
            pass
        except Exception as e:
            raise e
