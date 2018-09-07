# coding:utf-8

"""
@author: neo
@contact: z.yong.cool@163.com
@software: PyCharm
@file: blockchain_demo.py
@time: 2018-9-7 10:49
"""


class Blockchain(object):
    """类规划"""
    def __init__(self):
        # 存储我们的区块链列表
        self.chain = []
        # 保存交易的列表
        self.current_transactions = []
        # 创世区块
        self.new_block()

    def new_block(self):
        """创建一个新区块并添加入区块链列表chain"""
        pass

    def new_transaction(self):
        """创建一个新transaction并添加入交易列表current_transactions"""
        pass

    @staticmethod
    def hash(block):
        """对block进行SHA-256处理"""
        pass

    @property
    def last_block(self):
        """返回区块链列表中最后一个块"""
        # Returns the last Block in the chain
        return self.chain[-1]
