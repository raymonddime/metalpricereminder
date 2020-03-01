from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as Ureq
import itchat
import time

silver_low = 3980
silver_high = 4010
gold_low = 349
gold_high = 360
#Set price range gold and silver
silver_range = 10
gold_range = 0.3
#set extend value
from_addr = 'sender@126.com'
password = 'senderpassword'
to_addr = 'receiver@126.com'
smtp_server = 'smtp.126.com'
#Set sender and receiver information

def get_price():
    pass

#def wechat_msg(msgbody):
#    myname = itchat.search_friends(name=u'ND')
#    namemine = myname[0]['UserName']
#    itchat.send_msg(msgbody,toUserName=namemine)

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def mail_msg(subjectname,msgbody):
    msg = MIMEText(msgbody, 'plain', 'utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(subjectname)
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def notifyprice(price,type,updown):
    sub = 'attention! {} price {} to {}'.format(type,updown,price)
    attention_body = 'please attention {} price!!! current price is {} to {}'.format(type,updown,price)
#    wechat_msg(attention_body)
    mail_msg(sub,attention_body)




if __name__ == '__main__':
#    itchat.auto_login()
    while True:
        queryurl = ''
        #Set datasource here
        req = Ureq(queryurl)
        china_gold = 
        china_silver = 
        #your way of obtaining price data
        print('gold price is: {}'.format(china_gold))
        print('silver price is: {}'.format(china_silver))
        if china_silver>=silver_high or china_silver<=silver_low:
            if china_silver >= silver_high:
                notifyprice(china_silver,'silver','up')
                silver_high += silver_range
                print('silver notify range raised to {}'.format(silver_high))
            if china_silver <= silver_low:
                notifyprice(china_silver,'silver','down')
                silver_low -= silver_range
                print('silver notify range down to {}'.format(silver_low))

        if china_gold>=gold_high or china_gold<=gold_low:
            if china_gold >= gold_high:
                notifyprice(china_gold,'gold','up')
                gold_high += gold_range
                print('gold notify range raised to {}'.format(gold_high))
            if china_gold <= gold_low:
                notifyprice(china_gold,'gold','down')
                gold_low -= gold_low
                print('gold notify range down to {}'.format(gold_low))
        time.sleep(3)
