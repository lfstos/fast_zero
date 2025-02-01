from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

#  Registra Metadados no banco de dados
table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    # Nome da tabela quando ela for criada no banco de dados
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
