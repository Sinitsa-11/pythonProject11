import sqlite3
import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

welcome = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>757</width>
    <height>340</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>150</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Учитель</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>200</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Ученик</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>60</y>
      <width>181</width>
      <height>71</height>
     </rect>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Добро пожаловать!&lt;/span&gt;&lt;/p&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Выберите свой статус&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>757</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
teacher_hi = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>651</width>
    <height>235</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="login">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>60</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="password">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>110</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>60</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Логин</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>110</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
   <widget class="QPushButton" name="enter_t">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>80</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>651</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''
student_hi = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>807</width>
    <height>290</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>60</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Логин</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>110</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
   <widget class="QPushButton" name="enter_st">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>80</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>60</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="password">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>110</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>807</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''

'''программа работает с базой данных, которая состоит из 3 таблиц:
1. exercises со столбцами id (номер задания), name (его название), text (задание), answer (варианты ответов) 
и key (правильные ответы)
формат answer - текст с пропусками, которые обозначены англ буквами
answer - ответы под цифрами
key - A 3, B 1, C 4, D 7, E 2, F 5
2. logs - login, password, role (ученик или учитель), name (ФИО)
3. grades - name, id, result (оценка за задание)'''


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(welcome)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.teacher)  # выбор роли
        self.pushButton_2.clicked.connect(self.student)

    def teacher(self):
        t = io.StringIO(teacher_hi)
        uic.loadUi(t, self)
        self.con = sqlite3.connect("569.sqlite")
        self.enter_t.clicked.connect(self.entrance_t)

    def entrance_t(self):  # вход в систему для учителя
        cur = self.con.cursor()
        result = cur.execute("SELECT name FROM logs WHERE login=? and password=? and role='teacher'",
                             (log_id := self.login.text(), pass_id := self.password.text())).fetchall()
        if not result:
            self.enter_t.clicked.connect(self.teacher)  # если логин или пароль неверный, поля очищаются
        if result:
            self.enter_t.clicked.connect(self.teacher_options)

    def teacher_options(self):  # все возможности учителя. подключения к соответствующим фунциям
        uic.loadUi('t_options.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.lookButton.clicked.connect(self.look_tasks)
        self.changeButton.clicked.connect(self.change_tasks)
        self.deleteButton.clicked.connect(self.delete_tasks)
        self.addButton.clicked.connect(self.add_tasks)

        self.removeButton.clicked.connect(self.remove_student)
        self.knowButton.clicked.connect(self.know_student)
        self.inviteButton.clicked.connect(self.invite_student)

        self.gradeButton.clicked.connect(self.students_grade)
        self.avrgButton.clicked.connect(self.average_grade)

    # работа с оценками учеников
    def average_grade(self):  # подсчет среднего балла всех учащихся. выводится сразу
        uic.loadUi('average.ui', self)
        cur = self.con.cursor()
        result = cur.execute("SELECT result FROM grades").fetchall()
        summ = 0
        cnt = 0
        for elem in result:
            if elem[0]:
                summ += int(elem[0])
            cnt += 1
        self.listWidget.addItem(f'{summ / cnt}')
        self.backButton.clicked.connect(self.teacher_options)

    def students_grade(self):  # функция загружает ui-файл и вызывает grade, которая работает с ним
        uic.loadUi('grade.ui', self)
        self.con = sqlite3.connect('569.sqlite')
        self.pushButton.clicked.connect(self.grade)
        self.backButton.clicked.connect(self.teacher_options)

    def grade(self):
        cur = self.con.cursor()  # сбор и вывод информации об оценке ученика за конкретное задание
        try:
            res = cur.execute('select name from logs where login = ?', (log := self.lineEdit.text(),)).fetchall()[0][0]
            result = cur.execute("SELECT result FROM grades where name = ? and id = ?",
                                 (res, id_id := self.lineEdit_2.text())).fetchall()
            self.listWidget.addItem(f'{result[0][0]}')
        except:
            self.listWidget.addItem('Проверьте написание логина и корректность задания')

    # работа с учениками
    def invite_student(self):
        uic.loadUi('invite.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.newButton.clicked.connect(self.invite)

    def invite(self):
        cur = self.con.cursor()
        self.backButton.clicked.connect(self.teacher_options)
        check_log = cur.execute('select name from logs where login = ?', (log := self.new_login.text(),)).fetchall()
        if check_log or len(self.new_password.text()) < 6 or all(x.islower() for x in self.new_password.text()) or \
                all(x.isupper() for x in self.new_password.text()):
            self.newButton.clicked.connect(self.invite_student)
        else:
            s = self.surname.text() + " " + self.stname.text() + " " + self.patronymic.text()
            cur.execute("insert into logs(login, password, role, name) values (?, ?, ?, ?)",
                        (login := self.new_login.text(), password := self.new_password.text(),
                         role := 'student', name := s)).fetchall()
            self.con.commit()

    def know_student(self):
        uic.loadUi('know.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.pushButton.clicked.connect(self.know)
        self.backButton.clicked.connect(self.teacher_options)

    def know(self):
        s = self.lineEdit_3.text() + " " + self.lineEdit_2.text() + " " + self.lineEdit.text()
        cur = self.con.cursor()  # выводятся логин и пароль по ФИО
        log_result = cur.execute("SELECT login FROM logs where name = ?", (s,)).fetchall()
        pass_result = cur.execute("SELECT password FROM logs where name = ?", (s,)).fetchall()
        if log_result and pass_result:
            self.listWidget.addItem(f"Логин: {log_result[0][0]}, пароль: {pass_result[0][0]}")
        else:
            self.listWidget.addItem("Ученик не найден")

    def remove_student(self):
        uic.loadUi('remove.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.pushButton.clicked.connect(self.remove)
        self.backButton.clicked.connect(self.teacher_options)

    def remove(self):
        cur = self.con.cursor()  # удаление ученика по логину
        try:
            res = cur.execute('select name from logs where login = ?', (log := self.lineEdit.text(),)).fetchall()
            cur.execute('delete from grades where name = ?', (res[0][0],)).fetchall()
            cur.execute("delete from logs WHERE login = ?",
                        (log := self.lineEdit.text(),)).fetchall()
        except:
            pass
        self.con.commit()

    # работа с заданиями
    def add_tasks(self):
        uic.loadUi('add.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.pushButton.clicked.connect(self.add)
        self.backButton.clicked.connect(self.teacher_options)

    def add(self):  # для добавления задания вводятся все параметры кроме автоинкрементного id
        cur = self.con.cursor()
        cur.execute("insert into exercises(name, text, answer, key) values (?, ?, ?, ?)",
                    (name := self.nameEdit.text(), text := self.textEdit.text(),
                     answer := self.answerEdit.text(), key := self.keyEdit.text())).fetchall()
        self.con.commit()

    def delete_tasks(self):
        uic.loadUi('delete.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.pushButton.clicked.connect(self.delete)
        self.backButton.clicked.connect(self.teacher_options)

    def delete(self):
        cur = self.con.cursor()  # удаление задания по номеру
        cur.execute("delete from exercises WHERE id = ?",
                    (id_id := self.lineEdit.text(),)).fetchall()
        self.con.commit()

    def change_tasks(self):
        uic.loadUi('change.ui', self)  # изменение любой ячейки кроме id
        self.con = sqlite3.connect("569.sqlite")
        self.nameButton.clicked.connect(self.name)
        self.textButton.clicked.connect(self.text)
        self.answerButton.clicked.connect(self.answer)
        self.keyButton.clicked.connect(self.key)
        self.backButton.clicked.connect(self.teacher_options)

    def text(self):
        cur = self.con.cursor()
        cur.execute("UPDATE exercises SET text = ? WHERE id = ?",
                    (text_id := self.textLine.text(), id_id := self.lineEdit.text())).fetchall()
        self.con.commit()

    def answer(self):
        cur = self.con.cursor()
        cur.execute("UPDATE exercises SET answer = ? WHERE id = ?",
                    (answer_id := self.answerLine.text(), id_id := self.lineEdit.text())).fetchall()
        self.con.commit()

    def key(self):
        cur = self.con.cursor()
        cur.execute("UPDATE exercises SET key = ? WHERE id = ?",
                    (key_id := self.keyLine.text(), id_id := self.lineEdit.text())).fetchall()
        self.con.commit()

    def name(self):
        cur = self.con.cursor()
        cur.execute("UPDATE exercises SET name = ? WHERE id = ?",
                    (name_id := self.nameLine.text(), id_id := self.lineEdit.text())).fetchall()
        self.con.commit()

    def look_tasks(self):  # сразу выводятся все данные таблицы exercises
        uic.loadUi('taskslist.ui', self)
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM exercises").fetchall()
        for elem in result:
            self.tasksList.addItem(f'{elem}')
        self.backButton.clicked.connect(self.teacher_options)

    def student(self):
        st = io.StringIO(student_hi)
        uic.loadUi(st, self)
        self.con = sqlite3.connect("569.sqlite")
        self.enter_st.clicked.connect(self.entrance_st)

    def entrance_st(self):  # вход для ученика
        cur = self.con.cursor()
        result = cur.execute("SELECT name FROM logs WHERE login=? and password=? and role='student'",
                             (log_id := self.login.text(), pass_id := self.password.text())).fetchall()
        self.lg = self.login.text()
        if not result:
            print('try again')
            self.enter_st.clicked.connect(self.student)
        if result:
            self.enter_st.clicked.connect(self.student_options)

    def student_options(self):  # возможности ученика
        uic.loadUi('st_options.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.solveButton.clicked.connect(self.solve_task)
        self.allmarksButton.clicked.connect(self.all_marks)

    def all_marks(self):  # сразу выводятся все оценки и средний балл
        cur = self.con.cursor()
        res = cur.execute('select name from logs where login = ?', (log := self.lg,)).fetchall()[0][0]
        tasks = cur.execute('select id from grades where name=?', (res,)).fetchall()
        marks = cur.execute('select result from grades where name=?', (res,)).fetchall()
        uic.loadUi('allmarks.ui', self)
        summ = 0
        cnt = 0
        for i in range(len(tasks)):
            self.listWidget.addItem(f'Задание: {tasks[i][0]}, оценка: {marks[i][0]}')
            if marks[i][0]:
                summ += int(marks[i][0])
            cnt += 1
        self.listWidget.addItem(f'Средний балл: {summ / cnt}')
        self.backButton.clicked.connect(self.student_options)

    def solve_task(self):
        uic.loadUi('solve_num.ui', self)
        self.con = sqlite3.connect("569.sqlite")
        self.pushButton.clicked.connect(self.solve)
        self.backButton.clicked.connect(self.student_options)

    def solve(self):
        # находится и выводится задание
        try:
            cur = self.con.cursor()
            name = cur.execute("SELECT name FROM exercises WHERE id=?",
                               (id_id := self.numLine.text())).fetchall()[0][0]
            text = cur.execute("SELECT text FROM exercises WHERE id=?",
                               (id_id := self.numLine.text())).fetchall()[0][0].split('. ')
            answer = cur.execute("SELECT answer FROM exercises WHERE id=?",
                                 (id_id := self.numLine.text())).fetchall()[0][0]
            self.num = self.numLine.text()
            uic.loadUi('solve.ui', self)
            self.nameList.addItem(name)
            for x in text:
                self.textList.addItem(x)
            self.answerList.addItem(answer)
            self.replyButton.clicked.connect(self.check)
        except:
            pass

    def check(self):
        # проверка ответа и вывод результата
        cur = self.con.cursor()
        try:
            key = cur.execute("SELECT key FROM exercises WHERE id=?",
                              (id_id := self.num)).fetchall()[0][0]
            key = key.split(', ')
            students_ans = self.ansEdit.text().split(', ')
            cnt = 0
            for i in range(len(key)):
                if key[i] == students_ans[i]:
                    cnt += 1
            percent = cnt / len(key)
            uic.loadUi('right_or_not.ui', self)
            self.backButton.clicked.connect(self.student_options)
            self.cntList.addItem(f'{cnt} из {len(key)}')
            if 0.9 <= percent <= 1:
                self.gradeList.addItem('5')
                number = 5
            elif 0.75 <= percent < 0.9:
                self.gradeList.addItem('4')
                number = 4
            elif 0.5 <= percent < 0.75:
                self.gradeList.addItem('3')
                number = 3
            else:
                self.gradeList.addItem('2')
                number = 2
            res = cur.execute('select name from logs where login = ?', (log := self.lg,)).fetchall()[0][0]
            cur.execute("INSERT INTO grades(name, id, result) VALUES(?, ?, ?)",
                        (res, num_id := self.num, number)).fetchall()
        except:
            pass
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
