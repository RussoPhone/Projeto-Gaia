class Gtime:
    def __init__(self, mtksptk):
        self.mtk = 0 # microticks
        self.mtksptk = mtksptk # microticks por tick, tk são ticks
    def adv(self):
        self.mtk = self.mtk + 1

    def get_tk(self):
        return self.mtk // self.mtksptk

    def get_pos(self):
        return self.mtk % self.mtksptk

    def get_progress(self):
        return self.get_pos() / self.mtksptk

    def debug_text(self):
        return f"MTK: {self.mtk}, TK: {self.get_tk()}, POS: {self.get_pos()}, PROGRESS: {self.get_progress(): .0%}"
