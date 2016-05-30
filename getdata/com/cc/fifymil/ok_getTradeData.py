'''
Created on 2016年4月25日

@author: caiwx
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from WindPy import w
import pymysql

w.start();

def saveTradeDate(tradeDates):
    if tradeDates.ErrorCode!=0:
        print('error code:'+str(tradeDates.ErrorCode)+'\n');
        return();
    print('Data length:',len(tradeDates.Data[0]))
    conn=pymysql.connect(host='192.168.10.222',port='3306',user='cc',passwd='cc2718281828',db='AMGMH',charset='utf8')
    cur=conn.cursor()
    for i in range(0,len(tradeDates.Data[0])):
        strTemp=''
        #if len(tradeDates.Times)>1:
        #    strTemp=str(tradeDates.Times[i])+' '
        for k in range(0, len(tradeDates.Fields)):
            strTemp=strTemp+str(tradeDates.Data[k][i])+' '
            sta=cur.execute('insert into TDays values('+'\'SHE\','+str(tradeDates.Data[k][i])+')')
            print(sta)
        print(strTemp)
        
        
tradeDate = w.tdays('2016-03-25', '2016-12-31', 'TradingCalendar=SZSE')
saveTradeDate(tradeDate)
w.stop();

