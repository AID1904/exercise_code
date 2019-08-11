from threading import Thread, Lock


class Solution:
    def __init__(self, target_tuple, interval):
        self.list_result = []
        self.lock = Lock()
        self.index_ = 0
        self.characters = target_tuple
        self.interval = interval

    def add_num(self):
        with self.lock:
            for i in range(self.interval):
                self.list_result.append(self.interval * self.index_ + i + 1)

    def print_(self):
        for item in self.list_result:
            # print(item, end="")
            pass

    def run(self):
        for i in range(len(self.characters)):
            t = Thread(target=self.add_num)
            t.start()
            with self.lock:
                self.list_result.append(self.characters[i])
                self.list_result.append(" ")
                self.index_ += 1
        self.print_()


if __name__ == '__main__':
    interval = 6
    target_tuple = ("A", "B", "C", "D", "E", "F")
    s = Solution(interval,target_tuple)
    s.run()