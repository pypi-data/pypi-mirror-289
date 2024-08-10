import time


class XiaoSuSuTooGoodError(Exception):
    pass


class XiaoSu:
    def __init__(self, __a=None):
        if __a is None or __a != "小溯溯真棒":
            raise XiaoSuSuTooGoodError("Xiao su su is too good for you to init.")
        self.gold = "小溯溯真棒"

    @classmethod
    def love(cls):
        print("Xiao su su is shocked by you and decided to fix a bug for you.")
        return cls("小溯溯真棒")

    def run_hyper_bot(self):
        raise XiaoSuSuTooGoodError("HypeR Bot is a 抽象 platform, you'd better use nonebot.")

    def run_mu_rain_bot(self):
        print(self.gold)
        time.sleep(5)
        raise XiaoSuSuTooGoodError("You cannot use websocket connection because Xiao su su is really good.")

    def run_lgr_installer(self):
        print(self.gold)
        time.sleep(5)
        raise XiaoSuSuTooGoodError("我tm分块下载没修复，怎么会有这种报错啊啊啊啊啊")

