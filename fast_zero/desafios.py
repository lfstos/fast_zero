from http import HTTPStatus

from fast_zero.schemas import Message


@app.get('/ola-mundo', response_model=Message, status_code=HTTPStatus.OK)
def ola_mundo():
    return """
        <html>
        <head>
            <title>Nosso olá mundo!</title>
        </head>
        <body>
          <h1>Olá Mundo!</h1>
        </body
        </html>
    """
