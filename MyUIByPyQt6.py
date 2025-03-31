import random
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout
from PyQt6.QtGui import QIcon

from PlayGame import GameStats, guess_number
from userDataJson import UserManager


"""
2025/03/30：
创建QT类，用于初始化窗口界面和处理登录信息
窗口：主界面 
按钮：   登录，
        退出（关闭程序）
        
窗口：登录界面
输入框：  用户名
         密码

按钮：    登录
         取消
         返回主界面
         
窗口： 游戏窗口
输入框/显示框:   输入数字
               提示词
               得分
按钮：     退出
         
        
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        layout = QVBoxLayout()

        # 创建登录按钮
        login_button = QPushButton('登录')
        login_button.clicked.connect(self.switch_to_login_page)
        layout.addWidget(login_button)

        # 创建关闭按钮
        close_button = QPushButton('关闭')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        # 应用布局
        self.setLayout(layout)
        self.setWindowTitle('Welcome to guess number game!')
        self.setWindowIcon(QIcon('Icon/Icon1.png'))
        self.setGeometry(300, 300, 300, 200)

    def switch_to_login_page(self):
        # 隐藏当前界面
        self.hide()
        # 创建并显示登录界面
        self.login_page = LoginPage()
        self.login_page.show()


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        label = QLabel('Login')
        layout.addWidget(label)

        #创建用户名和密码输入文本框
        # 创建用户名标签和输入框
        username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)

        # 创建密码标签和输入框
        password_label = QLabel('密码:')
        self.password_input = QLineEdit()
        # 设置密码输入框为密文显示
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)

        # 创建登录和取消按钮
        login_button = QPushButton('登录')
        cancel_button = QPushButton('取消')
        login_button.clicked.connect(self.login)
        cancel_button.clicked.connect(self.close)

        layout.addWidget(login_button)
        layout.addWidget(cancel_button)


        back_button = QPushButton('返回主界面')
        back_button.clicked.connect(self.switch_back_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)
        self.setWindowTitle('登录界面')
        self.setWindowIcon(QIcon('Icon/Icon1.png'))
        self.setGeometry(300, 300, 300, 200)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(f'用户名: {username}, 密码: {password}')
        userVerify = UserManager()
        if userVerify.verify_user(username, password):
            self.switch_to_Game_page(username)
        else:
            QMessageBox.warning(self,"登录失败","用户名或密码错误，请重试。")

    def switch_to_Game_page(self,username):
        # 隐藏当前界面
        self.hide()
        # 创建并显示登录界面
        self.GamePage = GameWindow(username)
        self.GamePage.show()

    def switch_back_to_main(self):
        # 隐藏当前界面
        self.hide()
        # 重新显示主界面
        self.main_window = MainWindow()
        self.main_window.show()

class GameWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.secret_number = random.randint(1, 100)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.user_manager = UserManager()
        # 显示当前用户分数
        score = self.user_manager.get_user_score(self.username)
        score_label = QLabel(f"当前分数: {score}")
        score_layout = QHBoxLayout()
        score_layout.addStretch(1)
        score_layout.addWidget(score_label)
        layout.addLayout(score_layout)

        # 猜数输入框和确认按钮
        input_layout = QHBoxLayout()
        self.guess_input = QLineEdit()
        confirm_button = QPushButton('确认')
        confirm_button.clicked.connect(self.check_guess)
        input_layout.addWidget(self.guess_input)
        input_layout.addWidget(confirm_button)
        layout.addLayout(input_layout)

        # 退出按钮
        exit_button = QPushButton('退出')
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)
        self.setWindowTitle('游戏界面')
        self.setGeometry(300, 300, 300, 200)

    def check_guess(self):
        try:
            guess = int(self.guess_input.text())
            if guess == self.secret_number:
                new_score = self.user_manager.get_user_score(self.username) + 1
                self.user_manager.update_user_score(self.username, new_score)
                QMessageBox.information(self, "猜对了", f"恭喜你，猜对了！当前分数: {new_score}")
                self.secret_number = random.randint(1, 100)
            else:
                new_score = self.user_manager.get_user_score(self.username) - 2
                self.user_manager.update_user_score(self.username, new_score)
                if guess < self.secret_number:
                    message = f"猜小了，当前分数: {new_score}"
                else:
                    message = f"猜大了，当前分数: {new_score}"
                QMessageBox.warning(self, "猜错了", message)
            # 更新分数显示
            score_label = self.layout().itemAt(0).layout().itemAt(1).widget()
            score_label.setText(f"当前分数: {new_score}")
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的整数。")



"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
"""