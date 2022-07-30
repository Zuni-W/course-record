#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mymd5

samplehash = "571580b26c65f306376d4f64e53cb5c7"
# 将哈希值分为四段,并反转该四字节为小端序,作为64第二次循环的输入幻书
s1 = 0xb2801557
s2 = 0x06f3656c
s3 = 0x644f6d37
s4 = 0xc7b53ce5
# exp
secret = "A" * 15
secret_admin = secret + 'adminadmin{padding}'
padding = '\x80{zero}\xc8\x00\x00\x00\x00\x00\x00\x00'.format(zero="\x00" * (64 - 15 - 10 - 1 - 8))
secret_admin = secret_admin.format(padding=padding) + 'dawn'
r = mymd5.deal_rawInputMsg(secret_admin)
inp = r[len(r) / 2:]  # 我们需要截断的地方，也是我们需要控制的地方
print("getmein:" + mymd5.run_md5(s1, s2, s3, s4, inp))
