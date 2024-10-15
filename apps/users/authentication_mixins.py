#Desarrollo del sistema de autenticacion para todas las vistas

"""from rest_framework.authentication import get_authorization_header
from apps.users.authentication import ExpiringTokenAuthentication

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status 

class Authentication(object):
    user = None
    user_token_expired = False

    def get_user(self, request):
        token = get_authorization_header(request).split()

        if token:
            try: #No envia el error de fuera de rango
                token = token[1].decode() #Decodifica el token para verlo en consola
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            
            user,token,message, self.user_token_expired = token_expire.authenticate_credentials(token)# Envia al archivo authentication.py para hacer la validacion
            if user != None and token != None:
                self.user = user 
                return user
            return message
        
        return None


        En el archivo authetication.py validamos que el message si es None quiere decir que todo ha ido bien
        en este archivo valor a validar que el usuario y el token no sean None ejecuta el bloque de arriba y verifica
        si user is not None que nos retorne un mensaje o el usuario.



    def dispatch(self, request, *args, **kwargs): # se ejecuta primero en django y cancela la secuencia
        user = self.get_user(request)

        #Found some token in request
        if user is not None:
            if type(user) == str:
                response = Response({'error':user, 'expired':self.user_token_expired}, status = status.HTTP_401_UNAUTHORIZED)#'expired':self.user_token_expired hace saber al front-end si el token expiro o no
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'application/json'
                response.renderer_context = {}
                return response
            if not self.user_token_expired:
                return super().dispatch(request, *args, **kwargs)
        
        response =  Response({'error':'No se han enviado las credenciales'}, status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response


    No se puede enviar un response dentro de una clase que no herede de ninguna condicion por defectp
        de rest_framwork como ListView, ViewSet para que se pueda dar manejo al response de debe poner 
        el acept_renderer para que renderise tipo JSON"""