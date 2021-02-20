import scrapy, smtplib, ssl, os
from cryptography.fernet import Fernet
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class VideoCardChecker (scrapy.Spider):
    name = "VideoCardChecker"
    start_urls =  [
            'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
        ]
        
    def send_email(self):
        #email settings
        f = open(os.path.dirname(__file__) + "/../secret.py", "r")
        k = open(os.path.dirname(__file__) + "/../key.py", "r")
        key = bytes(k.read(),"utf8")
        suite = Fernet(key)
        password = suite.decrypt(bytes(f.read(),"utf8")).decode("utf-8")
        port = 465
        context = ssl.create_default_context()
        sender_email="jwaxington@gmail.com"
        receiver_email="m.jones12209@gmail.com"
        message = MIMEMultipart("alternative")
        message["Subject"] = "Your GeForce 3060 TI Founders Edition"
        message["From"] = sender_email
        message["To"] = receiver_email
        messageHTML = f"""\
            <html>
               <body>
                 <p>Hey Mike,<br>
                    <b>GO ORDER YOUR VIDEO CARD NOW!!!!</b><br>
                <a href="{self.start_urls[0]}">NVidia GeForce 3060TI Founders Edition</a> <br>
                Have a great day!!
                </p>
               </body>
            </html>
            """
        htmlObject = MIMEText(messageHTML, "html")
        message.attach(htmlObject)
        #send email
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login("jwaxington@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        
    def parse(self, response):
        self.send_email()
        #button
        fulfillmentButton = response.css('button.add-to-cart-button::text').re(r'Sold Out')[0]
        print("It worked")
        #condition when to email
        if (fulfillmentButton[0] != 'Sold Out'):
           self.send_email()