"""#Se va a colocar un tiempo de caducidad para el token

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


from datetime import timedelta, datetime
from django.utils import timezone
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):
#Del codigo fuente del framework
    expired = False

    #Calcula el tiempo de expiracion del token
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created #Calcula la hora actual con la hora de creacion del token
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time


    #Calcula y confirma si el token ha expirado
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta( seconds = 0)


    #Obtiene el valor de las funciones anteriores de que si ha expirado el token
    def token_expired_handler(self, token):
        is_expire = self.is_token_expired(token)
        
        if is_expire:
            self.expired = True
            user = token.user
            token.delete()# se borra el token para volverlo a crear, manejando el uso de sesiones
            token = self.get_model().objects.create(user = user)

        return is_expire, token


    def authenticate_credentials(self, key):
        message,token,user = None,None,None     #Si encuentra el message lo imprime, para que los mensajes no se dupliquen
        try:
            token = self.get_model().objects.select_related('user').get(key = key)#El get_model() ahorra la importacion de modelo token. devuelve el modelo si es None. Viende dentro del codigo de DRF
            user = token.user

        except self.get_model().DoesNotExist: 
            message = "Token invalido"
            self.expired = True

            #Con esto evitamos hacer el llamado al error 500 que no es recomendable
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario inactivo o eliminado.'


            #Se llama la variable para que ejecute el calculo
            is_expire = self.token_expired_handler(token)
            if is_expire:
                message = "Su token ha expirado"

        
        return (user, token, message, self.expired) #Una especie de contexto para los mensajes. si el message es None es que todo ha salido correcto"""