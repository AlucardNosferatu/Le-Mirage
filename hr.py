# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:28:22 2018

@author: Administrator
"""
import serial
#import matplotlib.pyplot as plt

def hr(com):
    ser=serial.Serial(com,9600,timeout=0.5)
    if ser.isOpen():
        ser.close()
    ser.open()
    ecg=[]
    freq=0
    for i in range(2000):
        data=ser.read(3)
        if not cmp(data[0],' ') or not cmp(data[2],' '):
            ecg.append(int(data.strip(),16))
            if ecg[i]<87:
                if i>10:
                    if min(ecg[i-10:i-1])>=87:
                        freq+=1
        else:
            i=0
    ser.close()
    freq/=4
#    plt.plot(ecg)
    heartrate=freq*60
    return heartrate