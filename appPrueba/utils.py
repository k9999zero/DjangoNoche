from rest_framework.response import Response
from rest_framework import status

def custom_response(success, body=None, code=status.HTTP_200_OK):
    """
    Genera una respuesta JSON consistente.

    Args:
        success (bool): Indica si la operación fue exitosa.
        message (str): Mensaje a incluir en la respuesta.
        body (dict, optional): Datos personalizados para la respuesta. Default: None.
        code (int): Código HTTP. Default: 200.

    Returns:
        Response: Objeto Response con el formato deseado.
    """
    return Response({
        "success": success,
        "body": body if body else {}
    }, status=code)
