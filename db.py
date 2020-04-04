# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:55:54 2018

@author: Scrooge
"""

import mysql.connector as con
config = {
        'user':'lostxmas',
        'password':'20160712',
        'host':'123.207.237.11',
        'database':'lostxmas',
        'charset':'utf8',
        }

def read(KEY,NAME):
    cnx = con.connect(**config)
    cursor=cnx.cursor()
    cursor.execute("SELECT `"+KEY+"` FROM `PLAYERS` WHERE `NAME`='"+NAME+"'")
    data = cursor.fetchone()
    cnx.close()
    return str(data[0]).decode('utf8')

def write(VALUE,KEY,NAME):
    cnx = con.connect(**config)
    cursor=cnx.cursor()
    cursor.execute("UPDATE `PLAYERS` SET `"+KEY+"`="+VALUE+" WHERE `NAME`='"+NAME+"'")
    cnx.commit()
    cnx.close()
    
def reg(NAME,PASSWD):
    cnx = con.connect(**config)
    cursor=cnx.cursor()
    cursor.execute("INSERT INTO `PLAYERS` (`NAME`, `PASSWD`) VALUES ('"+NAME+"', '"+PASSWD+"')")
    cnx.commit()
    cnx.close()