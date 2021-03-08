# python-sms-handler-module

sms handler python module in IRAN for  0098SMS  

SMS panel 0098sms .co

==========

## سریع استفاده کنید

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
        
   مقادیر نام کاربری و رمز عبور را 

        'USERNAME': 'yourusername',
        'PASSWORD': 'yourpassword',

 قرار دهید.
 
 ماژول را در برنامه خود اضافه کنید.
 
 
حال در برنامه خود یک ابجکت از

    MsgHandler
  
بسازید.

سپس با استفاده از متود های تعریف شده پیام فردی یا گروهی خود را ارسال کنید

    message_handler = MsgHandler()
    message_handler.group_send(message_text="سلام دنیا" ,phones=['09981152473','09217708151','09154874358','09034715420'])
    message_handler.user_send_message(message_text="سلام دنیا" ,phone_number='09391971797')
    
==========

## متود ها



این ماژول شامل هفت متود میباشد که برای به کاربر یا توسعه دهنده اجازه میدهد با استفاده از متود های عمومی پیام کوتاه خود را ارسال کند.

توجه کنید که پارامتر های تمامی توابع عمومی بصورت رشته یا

string 

است.

  
==========

## مثال
 
 
    if __name__ == '__main__':
        message_handler = MsgHandler()
        message_handler.group_send(message_text="سلام دنیا" ,phones=['09981152473','09217708151','09154874358','09034715420'])
        message_handler.user_send_message(message_text="سلام دنیا" ,phone_number='09391971797')
        otp = str(random.randrange(123456,999999))
        message_handler.user_send_otp(otp = otp, phone_number='09981152473')
