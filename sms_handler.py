import requests
import random

class MsgHandler():
    def __init__(self):
        # api methode 
        self.__params = {
        'FROM': '50002211311',
        'USERNAME': 'yourusername',
        'PASSWORD': 'yourpassword',
        'DOMAIN': '0098'
        }
        # server responses :
        self.__errores={
            '1' : 'invalide phone number',
            '2' : 'No phone number',
            '3' : 'No sender',
            '4' : 'No text to send',
            '5' : 'No user name',
            '6' : 'No password',
            '7' : 'No domain',
            '8' : 'invalide license',
            '9' : 'charge sms credit',
            '10': 'no linke for this number',
            '11': 'no license for to connect to link',
            '12': 'Ronge user name or password',
            '13': 'invalide character in message text',
            '0' : 'successful'
        } 
        # server url
        self.__sendsmslink = 'http://www.0098sms.com/sendsmslink.aspx'
    # send mesage method
    # use to see wich error happend
    def message_pretifier_password(self,password):
        return f'رمز یکبار مصرف: {password}'
        
    def Errores(self,res_value):
        return self.__errores[res_value]
    def __send_sms(self,message_text ,phone_number):
        params = self.__params.copy()
        params['Text'] = message_text
        params['To']   = phone_number
        send = requests.get(self.__sendsmslink,data=params)
        state = send.text[0]
        try:
            return self.Errores(state)
        except:
            return 'unexpected error'
    # publice send_message method no access to privet attr
    def user_send_otp(self,otp,phone_number):
        message = self.message_pretifier_password(otp)
        return self.__send_sms(message_text = message,phone_number=phone_number)
    def user_send_message(self,message_text,phone_number):
        return self.__send_sms(message_text = message_text,phone_number=phone_number)
    # send a message for selected group 
    def group_send(self,phones,message_text):
        states={}
        for number in phones:
            state = self.user_send_message(message_text=message_text,phone_number=number)
            states[number] = state
        return states

if __name__ == '__main__':
    message_handler = MsgHandler()
    message_handler.group_send(message_text="سلام دنیا" ,phones=['09981152473','09217708151','09154874358','09034715420'])
    message_handler.user_send_message(message_text="سلام دنیا" ,phone_number='09391971797')
    otp = str(random.randrange(123456,999999))
    print( message_handler.user_send_otp(otp = otp, phone_number='09981152473'))
