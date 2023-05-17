import sqlite3

from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.db_name = 'sppr.sqlite'
        self.materials = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 550)

        self.ok_button = QtWidgets.QDialogButtonBox(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(370, 500, 341, 32))
        self.ok_button.setOrientation(QtCore.Qt.Horizontal)
        self.ok_button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.ok_button.setObjectName("ok_button")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 711, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 120)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 360, 711, 61))
        self.groupBox.setObjectName("groupBox")

        self.push_button_add = QtWidgets.QPushButton(self.groupBox)
        self.push_button_add.setGeometry(QtCore.QRect(610, 23, 91, 32))  # 370, 500, 341, 32
        self.push_button_add.setObjectName("push_button_add")

        self.text_edit_material_name = QtWidgets.QPlainTextEdit(self.groupBox)
        self.text_edit_material_name.setGeometry(QtCore.QRect(10, 23, 150, 31))
        self.text_edit_material_name.setObjectName("text_edit_material_name")

        self.text_edit_material_area = QtWidgets.QPlainTextEdit(self.groupBox)
        self.text_edit_material_area.setGeometry(QtCore.QRect(165, 23, 100, 31))
        self.text_edit_material_area.setObjectName("text_edit_material_area")

        self.text_edit_material_area_std = QtWidgets.QPlainTextEdit(self.groupBox)
        self.text_edit_material_area_std.setGeometry(QtCore.QRect(270, 23, 100, 31))
        self.text_edit_material_area_std.setObjectName("text_edit_material_area_std")

        self.text_edit_material_porous = QtWidgets.QPlainTextEdit(self.groupBox)
        self.text_edit_material_porous.setGeometry(QtCore.QRect(375, 23, 100, 31))
        self.text_edit_material_porous.setObjectName("text_edit_material_porous")

        self.text_edit_material_porous_std = QtWidgets.QPlainTextEdit(self.groupBox)
        self.text_edit_material_porous_std.setGeometry(QtCore.QRect(480, 23, 110, 31))
        self.text_edit_material_porous_std.setObjectName("text_edit_material_porous_std")

        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 420, 711, 61))
        self.groupBox_2.setObjectName("groupBox_2")

        self.push_button_delete = QtWidgets.QPushButton(self.groupBox_2)
        self.push_button_delete.setGeometry(QtCore.QRect(610, 23, 91, 32))
        self.push_button_delete.setObjectName("push_button_delete")

        self.text_edit_material_id = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.text_edit_material_id.setGeometry(QtCore.QRect(10, 23, 100, 31))
        self.text_edit_material_id.setObjectName("text_edit_material_id")

        self.retranslateUi(Dialog)
        self.ok_button.rejected.connect(Dialog.reject) # type: ignore
        self.ok_button.accepted.connect(Dialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление/удаление материалов"))

        header_id = self.tableWidget.horizontalHeaderItem(0)
        header_id.setText(_translate("Dialog", "ID"))
        header_name = self.tableWidget.horizontalHeaderItem(1)
        header_name.setText(_translate("Dialog", "Наименование"))
        header_pore_area = self.tableWidget.horizontalHeaderItem(2)
        header_pore_area.setText(_translate("Dialog", "Площадь поры"))
        header_pore_std = self.tableWidget.horizontalHeaderItem(3)
        header_pore_std.setText(_translate("Dialog", "Откл. от площади"))
        header_porous = self.tableWidget.horizontalHeaderItem(4)
        header_porous.setText(_translate("Dialog", "Пористость"))
        header_porous_std = self.tableWidget.horizontalHeaderItem(5)
        header_porous_std.setText(_translate("Dialog", "Откл. от пористоти"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(_translate("Dialog", "Добавить запись"))
        self.push_button_add.setText(_translate("Dialog", "Добавить"))
        self.push_button_add.clicked.connect(self.push_button_add_click)

        self.text_edit_material_name.setPlaceholderText(_translate("Dialog", "название материала"))
        self.text_edit_material_area.setPlaceholderText(_translate("Dialog", "площадь поры"))
        self.text_edit_material_area_std.setPlaceholderText(_translate("Dialog", "откл. от площ."))
        self.text_edit_material_porous.setPlaceholderText(_translate("Dialog", "пористость"))
        self.text_edit_material_porous_std.setPlaceholderText(_translate("Dialog", "откл. от порист."))

        self.groupBox_2.setTitle(_translate("Dialog", "Удалить запись"))
        self.push_button_delete.setText(_translate("Dialog", "Удалить"))
        self.push_button_delete.clicked.connect(self.push_button_delete_click)

        self.text_edit_material_id.setPlaceholderText(_translate("Dialog", "номер записи"))

        self.load_materials()
        self.fill_table()

    def push_button_add_click(self):
        material_name = self.text_edit_material_name.toPlainText()
        material_area = self.text_edit_material_area.toPlainText()
        material_area_std = self.text_edit_material_area_std.toPlainText()
        material_porous = self.text_edit_material_porous.toPlainText()
        material_porous_std = self.text_edit_material_porous_std.toPlainText()
        data = (material_name, material_area, material_area_std, material_porous, material_porous_std)

        flag = [True if (m is not None and m != '') else False for m in data]

        if False not in flag:
            try:
                material_area = float(material_area)
                material_area_std = float(material_area_std)
                material_porous = float(material_porous)
                material_porous_std = float(material_porous_std)
                data = (material_name, material_area, material_area_std, material_porous, material_porous_std)

                connect = sqlite3.connect(self.db_name)
                crsr = connect.cursor()
                crsr.execute(
                    '''
                        INSERT INTO Materials 
                        (NAME, PORE_AREA_MEAN, PORE_AREA_STD, POROUS_MEAN, POROUS_STD)
                        VALUES (?,?,?,?,?)
                    ''', data
                )
                connect.commit()
                connect.close()

                self.load_materials()
                self.fill_table()
            except ValueError as e:
                pass
            except Exception as e:
                raise e
            finally:
                self.text_edit_material_name.setPlainText('')
                self.text_edit_material_name.clear()
                self.text_edit_material_area.setPlainText('')
                self.text_edit_material_area.clear()
                self.text_edit_material_area_std.setPlainText('')
                self.text_edit_material_area_std.clear()
                self.text_edit_material_porous.setPlainText('')
                self.text_edit_material_porous.clear()
                self.text_edit_material_porous_std.setPlainText('')
                self.text_edit_material_porous_std.clear()

    def load_materials(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cur = conn.cursor()
            res = cur.execute(
                '''
                    SELECT ID, NAME, PORE_AREA_MEAN, PORE_AREA_STD, POROUS_MEAN, POROUS_STD 
                    FROM Materials 
                '''
            )
            self.materials = res.fetchall()
            conn.close()
        except Exception as e:
            raise e

    def fill_table(self):
        self.tableWidget.setRowCount(len(self.materials))

        row_index = 0
        for material in self.materials:
            self.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(material[0])))
            self.tableWidget.setItem(row_index, 1, QtWidgets.QTableWidgetItem(material[1]))
            self.tableWidget.setItem(row_index, 2, QtWidgets.QTableWidgetItem(str(material[2])))
            self.tableWidget.setItem(row_index, 3, QtWidgets.QTableWidgetItem(str(material[3])))
            self.tableWidget.setItem(row_index, 4, QtWidgets.QTableWidgetItem(str(material[4])))
            self.tableWidget.setItem(row_index, 5, QtWidgets.QTableWidgetItem(str(material[5])))
            row_index += 1

    def push_button_delete_click(self):
        index = self.text_edit_material_id.toPlainText()
        try:
            index = int(index) - 1
            if 0 <= index <= len(self.materials) - 1:
                connect = sqlite3.connect(self.db_name)
                crsr = connect.cursor()
                row = self.materials.pop(index)
                material_id = row[0]
                crsr.execute('DELETE FROM Materials WHERE ID=?', (material_id,))
                connect.commit()
                connect.close()

                self.load_materials()
                self.fill_table()

        except Exception as e:
            print(e)

        self.text_edit_material_id.setPlainText('')
        self.text_edit_material_id.clear()
