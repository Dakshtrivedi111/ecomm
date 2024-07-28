from django.core.mail import send_mail, get_connection
from django.conf import settings

def send_account_activation_email(email,email_token):  
    '''with get_connection(
          host=settings.EMAIL_HOST, 
          port=settings.EMAIL_PORT,
          username=settings.EMAIL_HOST_USER, 
          password=settings.EMAIL_HOST_PASSWORD, 
          use_tls=settings.EMAIL_USE_TLS  
       ) as connection:'''  
    subject = 'Your account needs to be verified'  
    email_from = settings.EMAIL_HOST_USER  
    recipient_list = [email]  
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'  
    send_mail(subject, message, email_from, recipient_list)
 