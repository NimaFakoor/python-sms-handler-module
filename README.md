# python-sms-handler-module

sms handler python module in IRAN for  0098SMS  

شرکت پنل اس ام اس 

0098sms

==========

&nbsp;

این برنامه به شما این توانایی را میدهد که به راحتی برای کار های خود پیامک ارسال کنید.

 برای استفاده ابتدا حساب خود را در
  
  https://www.0098sms.com/
  
 ایجاد کنید و نام کاربری و رمز عبور خود را دریافت کنید
 

سپس کافی است در برنامه در قسمت

    def __init__(self):
        # api methode 
        self.__params = {
        'FROM': '50002211311',
        'USERNAME': 'yourusername',
        'PASSWORD': 'yourpassword',
        'DOMAIN': '0098'
        }
        
مقادیر

        'USERNAME': 'yourusername',
        'PASSWORD': 'yourpassword',

خود را قرار دهید.

حال یک ابجکت از

  MsgHandler
  
بسازید.

سپس با استفاده از متود های تعریف شده پیام فردی یا گروهی خود را ارسال کنید

    message_handler = MsgHandler()
    message_handler.group_send(message_text="سلام دنیا" ,phones=['09981152473','09217708151','09154874358','09034715420'])
    message_handler.user_send_message(message_text="سلام دنیا" ,phone_number='09391971797')
    
