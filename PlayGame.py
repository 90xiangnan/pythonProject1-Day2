import random
import time


"""
2025/03/30
定义游戏规则
按照提示输入
1，选择对应难度
2，输入所猜测的数字
3，猜测正确输出游戏信息， 超过7次后，挑战失败

"""
class GameStats:
    def __init__(self):
        self.start_time = time.time()
        self.guesses = []
    def add_guess(self, guess):
        self.guesses.append(guess)
    def show_report(self, target):
        duration = time.time() - self.start_time
        print(f"\n===游戏统计===")
        print(f"耗时:{duration:.1f}秒")
        print(f"猜测记录:{self.guesses}")
        if self.guesses:
            average_deviation = sum(abs(g[0]-target) for g in self.guesses) / len(self.guesses)
            print(f"平均偏差:{average_deviation:.1f}")
        else:
            print("平均偏差:无（没有猜测记录")
        #print(f"平均偏差:{sum(abs(g-target) for g in self.guesses/len(self.guesses):.1f)}")
class InvalidGuessError(Exception):
    """自定义异常类型"""
    def __init__(self, value, min_val, max_val):
        self.value = value
        self.range = f"{min_val}-{max_val}"
        super().__init__(f"无效数值:{value} (有效范围:{self.range})")
    def validate_guess(guess, min_val, max_val):
        if not min_val <= guess <= max_val:
            raise InvalidGuessError(guess,min_val,max_val)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#定义一个难度的字典
DIFFICULTIES = {
    "1": {"range": (1, 50), "chances":10},
    "2": {"range": (1,200), "chances":7},
    "3": {"range": (1,500), "changes":5}
}

def select_difficulty():
    print("请选择难度：\n 1.简单（1-50） \n 2.中等（1-200） \n3.困难（1-500）")
    while True:
        choice = input("请虚输入选项（1/2/3）：")
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("无效输入，请重新选择")



def guess_number():
    difficultyNumber: (1,100) = select_difficulty()["range"]
    #secret = random.randint(1,100)
    secret = random.randint(difficultyNumber[0], difficultyNumber[1])
    attempts = 0
    guess_Data = []
    #设置最大次数常量
    MAX_ATTEMPTS = 7 #常量全大写

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"猜数字{difficultyNumber}："))
            if guess<difficultyNumber[0] or guess >difficultyNumber[1]:
                raise ValueError("超出有效范围")
            else:
                guess_Data.append(guess)

            attempts +=1

            if guess <secret:
                print("猜小了")
            elif guess > secret:
                print("猜大了")
            else:
                print(f"恭喜！用了{attempts}次猜中")
                break

        except ValueError as e:
            print(f"错误{e}！")

    else: #循环正常结束执行
        print(f"挑战失败！ 正确答案是{secret}")
    return guess_Data