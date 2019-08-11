import time
from threading import  Thread



class Solution:
    def __init__(self,characters,interval):
        """

        :param characters: 列表
        :param interval: 间隔
        """
        self.characters = characters
        self.interval = interval
        self.result = [None] * len(self.characters) * (self.interval + 2)

    def number(self):
        for i in range(self.interval * len(self.characters)):
            for j in range(len(self.result)):
                if j % (self.interval + 2) < self.interval and not self.result[j]:
                    self.result[j] = i + 1
                    break

    def print_(self):
        result = ""
        for item in self.result:
            if not item:
                # print(result,end=" ")
                result = ""
                continue
            result += str(item)

    def run(self):
        t = Thread(target=self.number())
        t.start()
        for i in range(len(self.characters)):
            for j in range(len(self.result)):
                if j % (self.interval + 2) == self.interval and not self.result[j]:
                    self.result[j] = self.characters[i]
                    break
        self.print_()

if __name__ == '__main__':
    interval = 2
    characters = ("A", "B", "C", "D", "E", "F")
    s = Solution(characters, interval)
    s.run()