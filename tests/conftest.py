import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)  # Arrange


@pytest.fixture
def session():
    #  Abre conexão com banco de dados, e cria um bd volátil, na memória
    # e dura durante o teste, após o bd é destruído.
    engine = create_engine('sqlite:///:memory:')

    # Cria fisicamente as tabelas no bd (caso não exista) baseado nos modelos
    # definido no código. É como "materializar" as classes Python em tabelas
    # reais no bd conectado ao engine
    table_registry.metadata.create_all(engine)

    # gerenciamento de contexto
    with Session(engine) as session:
        yield session

    # Apaga as tablelas criadas em memória
    table_registry.metadata.drop_all(engine)
