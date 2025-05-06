from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
import random
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_email_with_html_body(subjet:str, receivers:list, template:str, context:dict):
    ''' Envoyer un email personnaliser à un utilisateur spécifique. '''

    try:
        message = render_to_string(template, context)

        send_mail(
            subjet,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=True,
            html_message=message,
        )
        
        return True
        
    except Exception as e:
        logger.error(e)
        
    return False

def generate_verif_code():
    code = ''
    
    for i in range(6):
        code += str(random.randint(0, 9))
    
    return int(code)
