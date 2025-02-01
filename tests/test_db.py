from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='fernando', email='test@test.com', password='password2'
    )

    # Adiciona um objeto(ex: user) à sessão para, marcando sinalizando para ser
    # inserida ao banco de dados (não executa a ação ainda)
    session.add(user)

    # Confirma todas as alterações(insert, update, delete) no banco,
    # tornando-as permanente.
    session.commit()

    # Garante que todas alterações no objeto reflitam no código,
    # se for alterado algum registro diretamente no bd, refletirá no código.
    # session.refresh(user)

    # Ao invés de atualizar o objeto utilizando refresh, vamos usar o select
    # do sqlalchemy, comando igual ao select do bd
    # scalar retorna o registro do bd no formato do objeto Python,
    # faz o mapeamento e traz esse objeto
    result = session.scalar(select(User).where(User.email == 'test@test.com'))

    assert result.username == 'fernando'
