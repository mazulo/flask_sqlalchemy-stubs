from .model import DefaultMeta
from flask_sqlalchemy.model import Model as FlaskSQLAlchemyModel
from sqlalchemy import orm
from sqlalchemy.orm.session import Session as SessionBase
from typing import Any, Optional

models_committed: Any
before_models_committed: Any

class _DebugQueryTuple(tuple):
    statement: Any = ...
    parameters: Any = ...
    start_time: Any = ...
    end_time: Any = ...
    context: Any = ...
    @property
    def duration(self): ...

class SignallingSession(SessionBase):
    app: Any = ...
    def __init__(self, db: Any, autocommit: bool = ..., autoflush: bool = ..., **options: Any) -> None: ...
    def get_bind(self, mapper: Optional[Any] = ..., clause: Optional[Any] = ...): ...

class _SessionSignalEvents:
    @classmethod
    def register(cls, session: Any) -> None: ...
    @classmethod
    def unregister(cls, session: Any) -> None: ...
    @staticmethod
    def record_ops(session: Any, flush_context: Optional[Any] = ..., instances: Optional[Any] = ...) -> None: ...
    @staticmethod
    def before_commit(session: Any) -> None: ...
    @staticmethod
    def after_commit(session: Any) -> None: ...
    @staticmethod
    def after_rollback(session: Any) -> None: ...

class _EngineDebuggingSignalEvents:
    engine: Any = ...
    app_package: Any = ...
    def __init__(self, engine: Any, import_name: Any) -> None: ...
    def register(self) -> None: ...
    def before_cursor_execute(self, conn: Any, cursor: Any, statement: Any, parameters: Any, context: Any, executemany: Any) -> None: ...
    def after_cursor_execute(self, conn: Any, cursor: Any, statement: Any, parameters: Any, context: Any, executemany: Any) -> None: ...

def get_debug_queries(): ...

class Pagination:
    query: Any = ...
    page: Any = ...
    per_page: Any = ...
    total: Any = ...
    items: Any = ...
    def __init__(self, query: Any, page: Any, per_page: Any, total: Any, items: Any) -> None: ...
    @property
    def pages(self): ...
    def prev(self, error_out: bool = ...): ...
    @property
    def prev_num(self): ...
    @property
    def has_prev(self): ...
    def next(self, error_out: bool = ...): ...
    @property
    def has_next(self): ...
    @property
    def next_num(self): ...
    def iter_pages(self, left_edge: int = ..., left_current: int = ..., right_current: int = ..., right_edge: int = ...) -> None: ...

class BaseQuery(orm.Query):
    def get_or_404(self, ident: Any, description: Optional[Any] = ...): ...
    def first_or_404(self, description: Optional[Any] = ...): ...
    def paginate(self, page: Optional[Any] = ..., per_page: Optional[Any] = ..., error_out: bool = ..., max_per_page: Optional[Any] = ...) -> Pagination: ...

class _QueryProperty:
    sa: Any = ...
    def __init__(self, sa: Any) -> None: ...
    def __get__(self, obj: Any, type: Any): ...

class _EngineConnector:
    def __init__(self, sa: Any, app: Any, bind: Optional[Any] = ...) -> None: ...
    def get_uri(self): ...
    def get_engine(self): ...
    def get_options(self, sa_url: Any, echo: Any): ...

def get_state(app: Any): ...

class _SQLAlchemyState:
    db: Any = ...
    connectors: Any = ...
    def __init__(self, db: Any) -> None: ...

class SQLAlchemy:
    Query: Any = ...
    use_native_unicode: Any = ...
    session: Any = ...
    Model: FlaskSQLAlchemyModel = ...
    app: Any = ...
    def __init__(self, app: Optional[Any] = ..., use_native_unicode: bool = ..., session_options: Optional[Any] = ..., metadata: Optional[Any] = ..., query_class: Any = ..., model_class: Any = ..., engine_options: Optional[Any] = ...) -> None: ...
    @property
    def metadata(self): ...
    def create_scoped_session(self, options: Optional[Any] = ...): ...
    def create_session(self, options: Any): ...
    def make_declarative_base(self, model: Any, metadata: Optional[Any] = ...): ...
    def init_app(self, app: Any): ...
    def apply_pool_defaults(self, app: Any, options: Any) -> None: ...
    def apply_driver_hacks(self, app: Any, sa_url: Any, options: Any) -> None: ...
    @property
    def engine(self): ...
    def make_connector(self, app: Optional[Any] = ..., bind: Optional[Any] = ...): ...
    def get_engine(self, app: Optional[Any] = ..., bind: Optional[Any] = ...): ...
    def create_engine(self, sa_url: Any, engine_opts: Any): ...
    def get_app(self, reference_app: Optional[Any] = ...): ...
    def get_tables_for_bind(self, bind: Optional[Any] = ...): ...
    def get_binds(self, app: Optional[Any] = ...): ...
    def create_all(self, bind: str = ..., app: Optional[Any] = ...) -> None: ...
    def drop_all(self, bind: str = ..., app: Optional[Any] = ...) -> None: ...
    def reflect(self, bind: str = ..., app: Optional[Any] = ...) -> None: ...

class _BoundDeclarativeMeta(DefaultMeta):
    def __init__(cls, name: Any, bases: Any, d: Any) -> None: ...

class FSADeprecationWarning(DeprecationWarning): ...


