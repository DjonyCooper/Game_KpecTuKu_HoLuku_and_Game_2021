# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие "а,б,в"
# text = "У лукоморья дуб зелёный, златая цепь на дубе том: и днём и ночью кот учёный всё ходит по цепи кругом"
# word = text.split()
# search_word = []
# print(f"» Исходный текст: {text}")
# for search in word:
#     for letter in range(len(search)):
#             if search[letter] == "а" or search[letter] == "б" or search[letter] == "в":
#                 text.replace(search, "")
#                 if search not in search_word:
#                     search_word.append(search)
# new_text = [word for word in word if word.lower() not in search_word]
# text = " ".join(new_text)
# print(f"• Список слов, подлежащих замене: {search_word}\n")
# print(f"» Получившийся текст: {text}")

# Задача 2: Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#                 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#                 Все конфеты оппонента достаются сделавшему последний ход.
#                 Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота ""интеллектом""

# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QGridLayout, QSpinBox, QMessageBox, QAbstractSpinBox
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QPixmap
# import random
#
# class Main(QWidget):
#     def __init__(self):
#         super(Main, self).__init__()
#         self.setMinimumSize(300, 300)
#         self.setWindowTitle("Игра 2021 конфета")
#
#         self.num_candy_player_1 = []
#         self.num_candy_player_2 = []
#         self.num_candy_bot = []
#
#         maket = QGridLayout()
#         maket.addWidget(self.label_game(), 0, 0, 1, 2, Qt.AlignCenter)
#         maket.addWidget(self.l_prog_img(), 0, 0, 1, 2, Qt.AlignCenter)
#         maket.addWidget(self.l_all_candy(), 1, 0, 1, 1)
#         maket.addWidget(self.l_choice_mode(), 0, 0, 1, 2, Qt.AlignCenter)
#         maket.addWidget(self.button_return_menu(), 0, 1, 1, 1, Qt.AlignRight)
#         maket.addWidget(self.l_num_candy_me(), 2, 0, 1, 1, Qt.AlignCenter)
#         maket.addWidget(self.l_num_candy_opponent(), 2, 1, 1, 1, Qt.AlignCenter)
#         maket.addWidget(self.l_num_candy_bot(), 2, 1, 1, 1, Qt.AlignCenter)
#         maket.addWidget(self.le_num_candy(), 1, 1, 1, 1)
#         maket.addWidget(self.le_num_candy_me(), 3, 0, 1, 1)
#         maket.addWidget(self.le_num_candy_opponent(), 3, 1, 1, 1)
#         maket.addWidget(self.le_num_candy_bot(), 3, 1, 1, 1)
#         maket.addWidget(self.button_start_game_two_player(), 1, 0, 1, 2, Qt.AlignCenter)
#         maket.addWidget(self.button_start_game_bot_mode(), 2, 0, 1, 2, Qt.AlignCenter)
#         maket.addWidget(self.button_take_candy_player_1(), 4, 0, 1, 1)
#         maket.addWidget(self.button_take_candy_player_1_bot_mode(), 4, 0, 1, 2)
#         maket.addWidget(self.button_take_candy_player_2(), 4, 1, 1, 1)
#         maket.addWidget(self.button_shuffling(), 5, 0, 1, 2)
#         maket.addWidget(self.button_shuffling_bot_mode(), 5, 0, 1, 2)
#         maket.addWidget(self.button_return_game(), 6, 0, 1, 2)
#         maket.addWidget(self.button_return_game_bot_mode(), 6, 0, 1, 2)
#         maket.addWidget(self.button_exit_game(), 7, 0, 1, 2)
#         maket.addWidget(self.button_start(), 1, 0, 1, 2)
#         self.setLayout(maket)
#
#     def label_game(self):
#         self.label_game = QLabel()
#         self.label_game.setText('<center style=font-size:9pt><FONT FACE="Century Gothic" color="dark" >Игра<br><FONT FACE="Century Gothic" color="red" style=font-size:70pt><b><center>2021</FONT><br><FONT FACE="Century Gothic" color="dark" style=font-size:32pt><b>конфетa</b>')
#         return self.label_game
#
#     def button_start(self):
#         self.b_start = QPushButton("Начать игру")
#         self.b_start.setMinimumSize(100, 100)
#         self.b_start.clicked.connect(self.func_start_game)
#         return self.b_start
#
#     def l_prog_img(self):
#         self.l_prog_img = QLabel()
#         self.l_prog_img.hide()
#         pixmap = QPixmap("images/candy.ico")
#         psmaller_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
#         self.l_prog_img.setPixmap(psmaller_pixmap)
#         return self.l_prog_img
#
#     def l_choice_mode(self):
#         self.l_choice_mode = QLabel("Выберите режим игры:")
#         self.l_choice_mode.hide()
#         return self.l_choice_mode
#
#     def l_all_candy(self):
#         self.l_all_candy = QLabel("Конфет в коробке:")
#         self.l_all_candy.hide()
#         return self.l_all_candy
#
#     def l_num_candy_me(self):
#         self.l_num_candy_me = QLabel("Конфет у Вас:")
#         self.l_num_candy_me.hide()
#         return self.l_num_candy_me
#
#     def l_num_candy_opponent(self):
#         self.l_num_candy_opponent = QLabel("Конфет у второго игрока:")
#         self.l_num_candy_opponent.hide()
#         return self.l_num_candy_opponent
#
#     def l_num_candy_bot(self):
#         self.l_num_candy_bot = QLabel("Конфет у компьютера:")
#         self.l_num_candy_bot.hide()
#         return self.l_num_candy_bot
#
#     def le_num_candy(self):
#         self.le_num_candy = QSpinBox()
#         self.le_num_candy.setButtonSymbols(QAbstractSpinBox.NoButtons)
#         self.le_num_candy.setReadOnly(True)
#         self.le_num_candy.setMinimum(0)
#         self.le_num_candy.setMaximum(2021)
#         self.le_num_candy.setValue(2021)
#         self.le_num_candy.hide()
#         self.le_num_candy.setAlignment(Qt.AlignCenter)
#         return self.le_num_candy
#
#     def le_num_candy_me(self):
#         self.le_num_candy_me = QSpinBox()
#         self.le_num_candy_me.setButtonSymbols(QAbstractSpinBox.NoButtons)
#         self.le_num_candy_me.setMinimum(0)
#         self.le_num_candy_me.setMaximum(28)
#         self.le_num_candy_me.setValue(0)
#         self.le_num_candy_me.hide()
#         self.le_num_candy_me.setAlignment(Qt.AlignCenter)
#         return self.le_num_candy_me
#
#     def le_num_candy_opponent(self):
#         self.le_num_candy_opponent = QSpinBox()
#         self.le_num_candy_opponent.setButtonSymbols(QAbstractSpinBox.NoButtons)
#         self.le_num_candy_opponent.setMinimum(0)
#         self.le_num_candy_opponent.setMaximum(28)
#         self.le_num_candy_opponent.setValue(0)
#         self.le_num_candy_opponent.hide()
#         self.le_num_candy_opponent.setAlignment(Qt.AlignCenter)
#         return self.le_num_candy_opponent
#
#     def le_num_candy_bot(self):
#         self.le_num_candy_bot = QSpinBox()
#         self.le_num_candy_bot.setButtonSymbols(QAbstractSpinBox.NoButtons)
#         self.le_num_candy_bot.setReadOnly(True)
#         self.le_num_candy_bot.setMinimum(0)
#         self.le_num_candy_bot.setMaximum(2021)
#         self.le_num_candy_bot.setValue(0)
#         self.le_num_candy_bot.hide()
#         self.le_num_candy_bot.setAlignment(Qt.AlignCenter)
#         return self.le_num_candy_bot
#
#     def button_take_candy_player_1(self):
#         self.button_take_candy_player_1 = QPushButton("Взять конфет!\nИгрок 1")
#         self.button_take_candy_player_1.hide()
#         self.button_take_candy_player_1.setEnabled(False)
#         self.button_take_candy_player_1.clicked.connect(self.func_start_game)
#         self.button_take_candy_player_1.setStyleSheet("""QPushButton:!hover {background-color: rgba(0, 0, 0, 5);
#                                                                              background-position: center;}
#                                                          QPushButton:hover  {border : 1px solid lightgreen;
#                                                                              background-color: rgba(0, 0, 0, 5);
#                                                                              background-position: center;}
#                                                          QPushButton:pressed{border : 1px solid dark;
#                                                                              background-color: lightgreen;
#                                                                              background-position: center;}
#                                                         """)
#         self.button_take_candy_player_1.clicked.connect(self.func_take_candy_me)
#         return self.button_take_candy_player_1
#
#     def button_take_candy_player_1_bot_mode(self):
#         self.button_take_candy_player_1_bot_mode = QPushButton("Взять конфет!\nИгрок")
#         self.button_take_candy_player_1_bot_mode.hide()
#         self.button_take_candy_player_1_bot_mode.setEnabled(False)
#         self.button_take_candy_player_1_bot_mode.clicked.connect(self.func_start_game)
#         self.button_take_candy_player_1_bot_mode.setStyleSheet("""QPushButton:!hover {background-color: rgba(0, 0, 0, 5);
#                                                                              background-position: center;}
#                                                          QPushButton:hover  {border : 1px solid lightgreen;
#                                                                              background-color: rgba(0, 0, 0, 5);
#                                                                              background-position: center;}
#                                                          QPushButton:pressed{border : 1px solid dark;
#                                                                              background-color: lightgreen;
#                                                                              background-position: center;}
#                                                         """)
#         self.button_take_candy_player_1_bot_mode.clicked.connect(self.func_take_candy_me_bot_mode)
#         return self.button_take_candy_player_1_bot_mode
#
#     def button_take_candy_player_2(self):
#         self.button_take_candy_player_2 = QPushButton("Взять конфет!\nИгрок 2")
#         self.button_take_candy_player_2.hide()
#         self.button_take_candy_player_2.setEnabled(False)
#         self.button_take_candy_player_2.setStyleSheet("""QPushButton:!hover {background-color: rgba(0, 0, 0, 5);
#                                                                              background-position: center;}
#                                                          QPushButton:hover  {border : 1px solid red;
#                                                                              background-color: rgba(0, 0, 0, 5);
#                                                                              background-position: center;}
#                                                          QPushButton:pressed{border : 1px solid dark;
#                                                                              background-color: red;
#                                                                              background-position: center;}
#                                                         """)
#         self.button_take_candy_player_2.clicked.connect(self.func_take_candy_opponent)
#         return self.button_take_candy_player_2
#
#     def button_exit_game(self):
#         self.b_exit_game = QPushButton("Закончить игру")
#         self.b_exit_game.hide()
#         self.b_exit_game.setMinimumSize(100, 30)
#         self.b_exit_game.clicked.connect(self.func_exit_game)
#         return self.b_exit_game
#
#     def button_return_game(self):
#         self.b_return_game = QPushButton("Может еще разок?")
#         self.b_return_game.hide()
#         self.b_return_game.setMinimumSize(100, 30)
#         self.b_return_game.clicked.connect(self.func_return_game)
#         return self.b_return_game
#
#     def button_return_game_bot_mode(self):
#         self.b_return_game_bot_mode = QPushButton("Может еще разок?")
#         self.b_return_game_bot_mode.hide()
#         self.b_return_game_bot_mode.setMinimumSize(100, 30)
#         self.b_return_game_bot_mode.clicked.connect(self.func_return_game_bot_mode)
#         return self.b_return_game_bot_mode
#
#     def button_shuffling(self):
#         self.b_shuffling = QPushButton("Жеребьевка")
#         self.b_shuffling.hide()
#         self.b_shuffling.setMinimumSize(100, 30)
#         self.b_shuffling.clicked.connect(self.func_shuffling)
#         return self.b_shuffling
#
#     def button_shuffling_bot_mode(self):
#         self.b_shuffling_bot_mode = QPushButton("Жеребьевка")
#         self.b_shuffling_bot_mode.hide()
#         self.b_shuffling_bot_mode.setMinimumSize(100, 30)
#         self.b_shuffling_bot_mode.clicked.connect(self.func_shuffling_bot_mode)
#         return self.b_shuffling_bot_mode
#
#     def button_start_game_two_player(self):
#         self.b_start_two_player = QPushButton("Режим:\nИГРОК против ИГРОКА")
#         self.b_start_two_player.setMinimumSize(280, 100)
#         self.b_start_two_player.hide()
#         self.b_start_two_player.clicked.connect(self.func_start_game_two_player)
#         return self.b_start_two_player
#
#     def button_start_game_bot_mode(self):
#         self.b_start_game_bot_mode = QPushButton("Режим:\nИГРОК против КОМПЬЮТЕРА")
#         self.b_start_game_bot_mode.setMinimumSize(280, 100)
#         self.b_start_game_bot_mode.hide()
#         self.b_start_game_bot_mode.clicked.connect(self.func_start_game_bot_mode)
#         return self.b_start_game_bot_mode
#
#     def button_return_menu(self):
#         self.b_return_menu = QPushButton()
#         self.b_return_menu.setStyleSheet("""
#                                        QPushButton:!hover {background-image : url(images/return_menu.ico);
#                                                            border : none;
#                                                            background-color: rgba(0, 0, 0, 5);
#                                                            background-position: center;}
#                                        QPushButton:hover { background-image : url(images/return_menu.ico);
#                                                            border-radius: 50px;
#                                                            border : 1px solid lightgreen;
#                                                            background-color: rgba(0, 0, 0, 5);
#                                                            background-position: center;}
#                                        QPushButton:pressed {background-image : url(images/return_menu.ico);
#                                                             border-radius: 50px;
#                                                            border : 2px solid lightgreen;
#                                                            background-color: rgba(0, 0, 0, 5);
#                                                            background-position: center;}
#                                  """)
#         self.b_return_menu.setMinimumSize(30, 30)
#         self.b_return_menu.hide()
#         self.b_return_menu.clicked.connect(self.func_return_menu)
#         return self.b_return_menu
#
#     def message_box(self, title, text, type_but):
#         self.message = QMessageBox()
#         self.message.setWindowTitle(title)
#         self.message.setText(text)
#         self.message.setStandardButtons(type_but)
#         self.message.exec_()
#
#     def func_start_game(self):
#         self.b_start.hide()
#         self.label_game.hide()
#         self.b_start_two_player.show()
#         self.b_start_game_bot_mode.show()
#         self.l_choice_mode.show()
#
#     def func_start_game_bot_mode(self):
#         self.l_choice_mode.hide()
#         self.b_start_two_player.hide()
#         self.b_start_game_bot_mode.hide()
#         self.b_return_menu.show()
#         self.button_take_candy_player_1_bot_mode.show()
#         self.l_prog_img.show()
#         self.l_all_candy.show()
#         self.le_num_candy.show()
#         self.l_num_candy_me.show()
#         self.l_num_candy_bot.show()
#         self.le_num_candy_me.show()
#         self.le_num_candy_bot.show()
#         self.b_shuffling_bot_mode.show()
#         self.b_return_game_bot_mode.show()
#         self.b_exit_game.show()
#
#     def func_start_game_two_player(self):
#         self.l_choice_mode.hide()
#         self.b_start_two_player.hide()
#         self.b_start_game_bot_mode.hide()
#         self.b_return_menu.show()
#         self.l_prog_img.show()
#         self.l_all_candy.show()
#         self.le_num_candy.show()
#         self.l_num_candy_me.show()
#         self.l_num_candy_opponent.show()
#         self.le_num_candy_me.show()
#         self.le_num_candy_opponent.show()
#         self.button_take_candy_player_1.show()
#         self.button_take_candy_player_2.show()
#         self.b_shuffling.show()
#         self.b_return_game.show()
#         self.b_exit_game.show()
#
#     def func_take_candy_me(self):
#         self.l_choice_mode.hide()
#         self.b_start_two_player.hide()
#         self.b_start_game_bot_mode.hide()
#         self.random_num_take_me = self.le_num_candy_me.value()
#         if self.random_num_take_me > self.le_num_candy.value():
#             self.num_candy_player_1.append(self.le_num_candy.value())
#         else:
#             self.num_candy_player_1.append(self.random_num_take_me)
#         sum_numbers = sum(self.num_candy_player_1)
#         self.le_num_candy_me.setValue(sum_numbers)
#         self.new_value_first = self.le_num_candy.value() - self.random_num_take_me
#         self.le_num_candy.setValue(self.new_value_first)
#         self.button_take_candy_player_1.setEnabled(False)
#         self.button_take_candy_player_2.setEnabled(True)
#         self.le_num_candy_me.setValue(0)
#         if self.le_num_candy.value() == 0:
#             self.func_message()
#             self.button_take_candy_player_1.setEnabled(False)
#             self.button_take_candy_player_2.setEnabled(False)
#
#     def func_take_candy_me_bot_mode(self):
#         self.l_choice_mode.hide()
#         self.b_start_two_player.hide()
#         self.b_start_game_bot_mode.hide()
#         self.random_num_take_me = self.le_num_candy_me.value()
#         if self.random_num_take_me > self.le_num_candy.value():
#             self.num_candy_player_1.append(self.le_num_candy.value())
#         else:
#             self.num_candy_player_1.append(self.random_num_take_me)
#         sum_numbers = sum(self.num_candy_player_1)
#         self.le_num_candy_me.setValue(sum_numbers)
#         self.new_value_first = self.le_num_candy.value() - self.random_num_take_me
#         self.le_num_candy.setValue(self.new_value_first)
#         self.button_take_candy_player_1_bot_mode.setEnabled(False)
#         self.le_num_candy_me.setValue(0)
#         self.func_take_candy_bot_timer()
#
#
#     def func_take_candy_opponent(self):
#         self.random_num_take_opp = self.le_num_candy_opponent.value()
#         if self.random_num_take_opp > self.le_num_candy.value():
#             self.num_candy_player_2.append(self.le_num_candy.value())
#         else:
#             self.num_candy_player_2.append(self.random_num_take_opp)
#         sum_numbers = sum(self.num_candy_player_2)
#         self.le_num_candy_opponent.setValue(sum_numbers)
#         self.new_value_first = self.le_num_candy.value() - self.random_num_take_opp
#         self.le_num_candy.setValue(self.new_value_first)
#         self.le_num_candy_opponent.setValue(0)
#         self.button_take_candy_player_1.setEnabled(True)
#         self.button_take_candy_player_2.setEnabled(False)
#         if self.le_num_candy.value() == 0:
#             self.func_message()
#             self.button_take_candy_player_1.setEnabled(False)
#             self.button_take_candy_player_2.setEnabled(False)
#
#     def func_take_candy_bot(self):
#         self.l_choice_mode.hide()
#         self.b_start_two_player.hide()
#         self.b_start_game_bot_mode.hide()
#         self.random_num_take_bot = random.randint(1, 28)
#         if self.random_num_take_bot > self.le_num_candy.value():
#             self.num_candy_bot.append(self.le_num_candy.value())
#         else:
#             self.num_candy_bot.append(self.random_num_take_bot)
#         self.le_num_candy_bot.setValue(self.random_num_take_bot)
#         self.new_value_bot = self.le_num_candy.value() - self.random_num_take_bot
#         self.le_num_candy.setValue(self.new_value_bot)
#         self.button_take_candy_player_1_bot_mode.setEnabled(True)
#         if self.le_num_candy.value() == 0:
#             self.func_message_bot_mode()
#             self.button_take_candy_player_1.setEnabled(False)
#
#     def func_take_candy_bot_timer(self):
#         if self.le_num_candy.value() == 0:
#             self.button_take_candy_player_1_bot_mode.setEnabled(False)
#             self.func_message_bot_mode()
#         else:
#             QTimer.singleShot(1000, self.func_take_candy_bot)
#
#
#
#     def func_message(self):
#         if self.le_num_candy_me.value() > self.le_num_candy_opponent.value():
#             self.message_box('Поздрвляю!',
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Игрок 1 победил!</b></center></FONT>'
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Теперь, все конфеты ваши!</b></center></FONT>',
#                              QMessageBox.Ok)
#             self.le_num_candy_me.setMaximum(2021)
#             self.le_num_candy_me.setValue(2021)
#             self.le_num_candy_opponent.setValue(0)
#         else:
#             self.message_box('Поздрвляю!',
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Игрок 2 победил!</b></center></FONT>'
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Теперь, все конфеты ваши!</b></center></FONT>',
#                              QMessageBox.Ok)
#             self.le_num_candy_opponent.setMaximum(2021)
#             self.le_num_candy_opponent.setValue(2021)
#             self.le_num_candy_me.setValue(0)
#
#
#     def func_message_bot_mode(self):
#         if self.le_num_candy_me.value() > self.le_num_candy_bot.value():
#             self.message_box('Поздрвляю!',
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Вы победили, поздравляю!</b></center></FONT>'
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Теперь, все конфеты ваши!</b></center></FONT>',
#                              QMessageBox.Ok)
#
#             self.le_num_candy_me.setMaximum(2021)
#             self.le_num_candy_me.setValue(2021)
#             self.le_num_candy_bot.setValue(0)
#         else:
#             self.message_box('Эх..!',
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Увы, компьютер победил</b></center></FONT>'
#                              '<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Теперь все его микросхемы слипнутся!</b></center></FONT>',
#                              QMessageBox.Ok)
#             self.le_num_candy_bot.setValue(2021)
#             self.le_num_candy_me.setValue(0)
#
#     def func_return_game(self):
#         self.num_candy_player_1 = []
#         self.num_candy_player_2 = []
#         self.le_num_candy_me.setValue(0)
#         self.le_num_candy_opponent.setValue(0)
#         self.le_num_candy.setValue(2021)
#         self.button_take_candy_player_1.setEnabled(False)
#         self.button_take_candy_player_2.setEnabled(False)
#         self.b_shuffling.setEnabled(True)
#
#     def func_return_game_bot_mode(self):
#         self.num_candy_player_1 = []
#         self.num_candy_bot = []
#         self.le_num_candy_me.setValue(0)
#         self.le_num_candy_bot.setValue(0)
#         self.le_num_candy.setValue(2021)
#         self.button_take_candy_player_1_bot_mode.setEnabled(False)
#         self.b_shuffling_bot_mode.setEnabled(True)
#
#     def func_shuffling(self):
#         random_num_take = random.randint(1, 2)
#         self.message_box('Внимание!',
#                          f'<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Начинает: Игрок {random_num_take}</b></center></FONT>',
#                          QMessageBox.Ok)
#         if random_num_take == 1:
#             self.button_take_candy_player_1.setEnabled(True)
#         else:
#             self.button_take_candy_player_2.setEnabled(True)
#         self.b_shuffling.setEnabled(False)
#
#     def func_shuffling_bot_mode(self):
#         random_num_take = random.randint(1, 2)
#         if random_num_take == 1:
#             self.message_box('Внимание!',
#                              f'<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Начинает: Игрок</b></center></FONT>',
#                              QMessageBox.Ok)
#             self.button_take_candy_player_1_bot_mode.setEnabled(True)
#         else:
#             self.message_box('Внимание!',
#                              f'<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">Начинает: Компьютер</b></center></FONT>',
#                              QMessageBox.Ok)
#             self.b_shuffling_bot_mode.setEnabled(False)
#             self.func_take_candy_bot()
#
#
#     def func_return_menu(self):
#         if self.le_num_candy_me.isVisible() == True:
#             message = QMessageBox()
#             message.setWindowTitle('Внимание!')
#             message.setText('<center><br/><b style=font-size:8pt><FONT FACE="Century Gothic">В случае возврата в меню,<br>весь текущий прогресс <FONT color = "red">будет утерян.</FONT>'
#                             '<br>Хотите продолжить?</b></center></FONT>')
#             message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#             result = message.exec_()
#             if result == QMessageBox.Ok:
#                 self.func_return_game()
#                 self.func_return_game_bot_mode()
#                 self.l_choice_mode.show()
#                 self.b_start_two_player.show()
#                 self.b_start_game_bot_mode.show()
#                 self.l_prog_img.hide()
#                 self.l_all_candy.hide()
#                 self.le_num_candy.hide()
#                 self.l_num_candy_me.hide()
#                 self.l_num_candy_opponent.hide()
#                 self.le_num_candy_me.hide()
#                 self.le_num_candy_opponent.hide()
#                 self.button_take_candy_player_1.hide()
#                 self.button_take_candy_player_2.hide()
#                 self.b_shuffling.hide()
#                 self.b_return_game.hide()
#                 self.b_exit_game.hide()
#                 self.button_take_candy_player_1_bot_mode.hide()
#                 self.l_num_candy_bot.hide()
#                 self.le_num_candy_bot.hide()
#                 self.b_shuffling_bot_mode.hide()
#                 self.b_return_game_bot_mode.hide()
#                 self.b_return_menu.hide()
#
#     def func_exit_game(self):
#         self.close()
#
#
# if __name__ == ('__main__'):
#     import sys
#     app = QApplication(sys.argv)
#     w = Main()
#     w.show()
#     app.exec_()

# Задача 3: Создайте программу для игры в ""Крестики-нолики"".
#
# from PyQt5 import QtWidgets, QtGui
# from PyQt5.Qt import *
#
#
# class Button(QPushButton):
#     def __init__(self, text):
#         super().__init__()
#
#         self.setText(f'{text}')
#         self.setFixedSize(150, 150)
#
#         self.setStyleSheet("""  QPushButton:!hover {border : 1px solid gray;}
#                                 QPushButton: hover {border : 1px solid lightgreen;}
#                                 QPushButton:pressed{border : 2px solid lightgreen;}
#                            """)
#         self.setFont(QtGui.QFont("Times", 100, QtGui.QFont.Bold))
#
#
# class Game(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label_change = QLabel("Выберите, кто\nначнёт\n(по умолчанию\nначинает O):")
#         self.label_x = QLabel("X")
#         self.label_o = QLabel("O")
#         self.check_box_x = QtWidgets.QCheckBox()
#         self.check_box_o = QtWidgets.QCheckBox()
#         self.reset = QPushButton("Сброс")
#
#
#         layout = QGridLayout(self)
#
#         for step in range(9):
#             btn = Button(' ')
#             btn.clicked.connect(lambda but, b=btn: self.onClicked(b))
#             layout.addWidget(btn, step // 3, step % 3)
#             self.reset.clicked.connect(lambda text, b = btn: self.clear_btn(b))
#         layout.addWidget(self.label_change, 0, 4, 1, 2, Qt.AlignTop)
#         layout.addWidget(self.label_x, 1, 4, Qt.AlignRight)
#         layout.addWidget(self.label_o, 2, 4, Qt.AlignRight)
#         layout.addWidget(self.check_box_x, 1, 4, 1, 2, Qt.AlignLeft)
#         layout.addWidget(self.check_box_o, 2, 4, 1, 2, Qt.AlignLeft)
#         layout.addWidget(self.reset, 2, 4, 1, 2, Qt.AlignBottom)
#
#     def onClicked(self, btn):
#         if self.check_box_x.isChecked():
#             btn.setText("X")
#             self.check_box_x.setChecked(False)
#             self.check_box_o.setChecked(True)
#         else:
#             btn.setText("O")
#             self.check_box_x.setChecked(True)
#             self.check_box_o.setChecked(False)
#
#     def clear_btn(self, btn):
#         btn.setText(' ')
#
#     def clear_text(self, btn):
#         btn.setText(' ')
#
#
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     w = Game()
#     w.show()
#     sys.exit(app.exec_())

# Задача 4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализация модуля сжатия:
# text = "WWWWWWWWWWWWWWWWWWRRRRRRRRRRRRRWWWWWSSSSSSSSSSPPPPP"
# co = []
# search_word = []
# print(f"Исходный текст: {text}")
# for letter in range(len(text)):
#     if text[letter - 1] != text[letter]:
#         search_word.append(text[letter])
#         co.append(letter)
# co.append(letter)
# num = [x - y for x, y in zip(co[1:], co)]
# res = [x for y in zip(num, search_word) for x in y]
# print(f'Реализация модуля сжатия: {"".join(map(str, res))}')
# Реализация модуля восстановления:
# text = "18W13R5W10S4P"
# decode = ''
# count = ''
# print(f"Исходный текст: {text}")
# for char in text:
#     if char.isdigit():
#         count += char
#     else:
#         decode += char * int(count)
#         count = ''
# print(f'Реализация модуля восстановления: {"".join(map(str, decode))}')
