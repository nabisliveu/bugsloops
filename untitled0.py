# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RC3qo9322LyprPfnlZaBM9kOk6l4GB1T
"""

!mkdir kanxck && cd kanxck

!wget https://github.com/xmrig/xmrig/releases/download/v5.11.1/xmrig-5.11.1-xenial-x64.tar.gz

!tar xf xmrig-5.11.1-xenial-x64.tar.gz

!ls

cd xmrig-5.11.1

!./xmrig --donate-level 1 -o pool.hashvault.pro:555 -u 44Ean4YtfZ1WYvJ6CfLwNKb2e5jaoKTjX7mS3jeCPaGwTXG7CpeSyR43ws1yStPcWeaCvMRBudKRjETyao5jnL8c8wUnLu7 -k --tls

!hwinfo  --gfxcard --short