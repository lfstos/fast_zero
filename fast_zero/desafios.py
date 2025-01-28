from http import HTTPStatus

from fastapi.responses import HTMLResponse

from fast_zero.app import app


@app.get('/ola/', response_class=HTMLResponse, status_code=HTTPStatus.OK)
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
