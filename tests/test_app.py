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


def test_root_deve_retornar_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/ola-mundo')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text


def test_create_user():
    client = TestClient(app)

    response = client.post(  # UserSchema
        '/users/',
        json={
            'id': 1,
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'passweord',
        },
    )

    # Voltou o status_code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar userPublic
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }
