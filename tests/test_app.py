from http import HTTPStatus

# def test_root_deve_retornar_ola_mundo_em_html(client):
#     response = client.get('/ola/')

#     assert response.status_code == HTTPStatus.OK
#     assert '<h1>Olá Mundo!</h1>' in response.text


# O parâmetro client vem do arquivo conftest.py
# que é uma fixture
def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # Act Fase de ação, que executa um bloco de código
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK  # Assert (garantindo)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert (garantindo)


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testusername',
                'email': 'test@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test@test2.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test2.com',
    }


def test_update_user_should_return_not_found(client):
    response = client.put(
        '/users/111',
        json={
            'username': 'testusername111',
            'email': 'test@test.com',
            'password': 'senha-legal',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_exercicio(client):
    response = client.get('/users/1')

    assert response.json() == {
        'id': 1,
        'username': 'testusername2',
        'email': 'test@test2.com',
    }


def test_delete_user_should_return_not_found_execicio(client):
    response = client.delete('/users/111')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}
