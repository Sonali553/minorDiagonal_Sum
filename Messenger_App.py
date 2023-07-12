from abc import ABC,abstractmethod

class MessagingService(ABC):
    def sendMessage(self):
        pass
class SMSMessagingService(MessagingService):
    def __init__(self,phone_num,message):
        self.phone_num = phone_num
        self.message = message

    def sendMessage(self):
        print("The Mobile Number is :",self.phone_num)
        print("And the message sent was :",self.message)
class EmailMessagingService(MessagingService):
    def __init__(self,sender_email,receiver_email,subject,message):
        self.sender_email= sender_email
        self.receiver_email = receiver_email
        self.subject=subject
        self.message=message

        def sendMessage(self):
             print("The email sent by the person in following email:",self.sender_email)
             print("The email is sent to the person in the following email :",self.receiver_email)
             print("The subject of the mail is :",self.subject)
             print("The message in the mail is :",self.message)


class WhatsAppMessagingService(MessagingService):
      def __init__(self,mobile,isWhatsapp,message):
        self.mobile=mobile
        self.message=message
        self.isWhatsapp = isWhatsapp
      def sendMessage(self):

        if self.ismobile:
            print("The WhatsApp number is :",self.mobile)
            print("It is valid user in whatsapp")
            print("The message is :",self.message)
        else:
            print("The phone number is not a valid WhatsApp user")
m = 0
while m != 1:
    print("Enter 1 for SMS")
    print("Enter 2 for Email")
    print("Enter 3 for Whatsapp")
    print("Enter 4 for Exit")
    choice=int(input("Enter the messaging options:"))

    if choice==1:
        mobile=input("Enter the mobile number : ")
        if mobile[0] in "6789" and len(mobile)==10:
            message=input("Enter the message : ")
            sms=SMSMessagingService(mobile,message)
            sms.sendMessage()
        
        else:
            print("Invalid Mobile Number")
    elif choice==2:
        sender_email=input("Enter the senderEmail : ")
        if sender_email.split('.')[-1] in ['com','in'] and '@'in sender_email:
            pass
        else:
            print("Invalid Email")
        receiver_email=input("Enter the Receiver Email : ")
        if receiver_email.split('.')[-1] in ['com','in'] and '@'in receiver_email:
            subject=input("Enter Subject: ")
            message=input("Enter Message: ")
            em=EmailMessagingService(sender_email,receiver_email,subject,message)
            em.sendMessage()
        else:
            print("Invalid Email")
    elif choice==3:
        mobile=input("Enter the mobile : ")
        if mobile[0] in "6789" and len(mobile)==10:
            isWhatsapp=input("Enter whether it is a whatsapp number or not (T/F): ")
            if(isWhatsapp=='T'):
                isWhatsapp=True
            elif(isWhatsapp == 'F'):
                isWhatsapp = False
            message=input("Enter the message : ")
            whatsapp=WhatsAppMessagingService(mobile,isWhatsapp,message)
            whatsapp.sendMessage()
        else:
            print("The number may not be belongs to INDIA")
    elif choice == 4:
        print("Thank you!")
        m = 1

    else:
        print("Invalid Choice")
    

      

