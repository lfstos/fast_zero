from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    # Oraganização das coisas para poder testas
    client = TestClient(app)  # Arrange,

    # Act Fase de ação, que executa um bloco de código
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK  # Assert (garantindo)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert (garantindo)
