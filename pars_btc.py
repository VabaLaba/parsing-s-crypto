import code
import smtplib
import warnings
from email.header import Header
from email.mime.text import MIMEText
import sys
import requests
import resp as resp
from bs4 import BeautifulSoup
import time

from win32com.server import exception

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'accept': '*/*'
}
url = 'https://coinmarketcap.com/currencies/bitcoin/markets/'


class Currency_check ( ):



    def get_html (self, url):
        warnings.filterwarnings ( "ignore", category=UserWarning, module='bs4' )
        r = requests.get ( url, headers=HEADERS
                           )
        return r

    def get_full_pages (self, html: object):

        soup = BeautifulSoup ( html, 'html.parser' )

        items = soup.find ( 'span', class_='cmc-details-panel-price__price' )

        price_of_btc: str = items.text



        items_market_cap: object = soup.find ( 'ul', class_='sc-15acgj0-0 dyvdrp cmc-details-panel-stats' ).get_text (
            strip=True )


        print ( "объем торгов - ", items_market_cap, end="\n" )

        print ( f'цена за btc = {price_of_btc}' )
        self.mail_sender: str = 'ametopsluk@gmail.com'

        self.mail_receiver: str = 'ametopsluk@gmail.com'
        self.username = 'ametopsluk@gmail.com'

        try:
            # подгтовка данных пользователя

            self.password = input ( "vvedi password :" )  # ''
            server = smtplib.SMTP ( 'smtp.gmail.com:587' )

            # Формируем тело письма
            subject = u'Курс биткойна и объем торгов сейас' + str ( )

            body = f'Цена за биткойн сейчас =' + str (
                price_of_btc ) + "\n\n" + f'Объем торгов -{str ( items_market_cap )}'

            msg = MIMEText ( body, 'plain', 'utf-8' )
            msg ['Subject'] = Header ( subject, 'utf-8' )

            # Отпавляем письмо


            server.starttls ( )
            server.ehlo ( )
            server.login ( self.username, self.password )
            while True:


                server.sendmail ( self.mail_sender, self.mail_receiver, msg.as_string ( ) )

                time.sleep ( 60)
                # server.quit ( )



                ## ATTEMPTING SMTP LOGIN


        except smtplib.SMTPAuthenticationError:
            smtplib.SMTPAuthenticationError = True
            print ( f"problem with password - password:{self.password} is wrong " )

            sys.exit ( )

        except:
            pass

    def parser (self):




            html = self.get_html ( url )

            if html.status_code == 200:
                self.get_full_pages ( html.text )





result_parsing_of_btc = Currency_check ( )
result_parsing_of_btc.parser ( )
