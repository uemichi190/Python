#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# save this as helloHelloPython2.py
# 行中の#以降は行末までコメントとなる(Python プログラムの実行に影響しない)

def propose(name):
    print("I love you,{}. Will you marry me?".format(name))

def Hello():
    for i in range(10):
        #propose("hoge")
        propose(i)
    print("I love you too.")

if __name__ == "__main__":
    Hello()