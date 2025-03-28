import time

class GameStats:
    def __init__(self):
        self.start_time = time.time()
        self.guesses = []

    def show_report(self):
        duration = time.time() - self.start_time
        print(f"\n===游戏统计===")
        print(f"耗时:{duration:.1f}秒")
        print(f"猜测记录:{self.guesses}")
        #print(f"平均偏差:{sum(abs(g-target) for g in self.guesses/len(self.guesses):.1f)}")
