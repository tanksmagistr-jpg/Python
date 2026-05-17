import pytest
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from database import Base


# --- 1. Определяем тестовую модель (сущность "Студент") ---
# В реальном проекте модель может лежать в другом файле,
# но для простоты примера определим её здесь
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)


# --- 2. Настраиваем фикстуры (fixtures) для pytest ---

@pytest.fixture(scope="session")
def engine():
    """Создаёт движок БД и все таблицы один раз для всех тестов."""
    # Используем тот же engine, что и для основного приложения
    from database import engine
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(engine):
    """
    КЛЮЧЕВАЯ ФИКСТУРА: создаёт новую сессию и транзакцию для каждого теста.
    После теста транзакция откатывается, оставляя базу в исходном состоянии.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session  # Здесь выполняется тело теста

    session.close()
    transaction.rollback()
    connection.close()


# --- 3. Пишем сами тесты ---

def test_create_student(db_session: Session):
    """Тест на добавление (CREATE) нового студента."""
    test_name = "Иван Петров"
    test_email = "ivan.petrov@example.com"

    new_student = Student(name=test_name, email=test_email)
    db_session.add(new_student)
    db_session.commit()

    found_student = (
        db_session.query(Student)
        .filter(Student.email == test_email)
        .first()
    )
    assert found_student is not None
    assert found_student.name == test_name


def test_update_student(db_session: Session):
    """Тест на обновление (UPDATE) данных студента."""
    original_name = "Анна Смирнова"
    student = Student(
        name=original_name,
        email="anna.smirnova@example.com"
    )
    db_session.add(student)
    db_session.commit()

    new_name = "Анна Иванова"
    student.name = new_name
    db_session.commit()

    updated_student = (
        db_session.query(Student)
        .filter(Student.id == student.id)
        .first()
    )
    assert updated_student.name == new_name


def test_delete_student(db_session: Session):
    """Тест на удаление (DELETE) студента."""
    student = Student(
        name="Петр Сидоров",
        email="petr.sidorov@example.com"
    )
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    deleted_student = (
        db_session.query(Student)
        .filter(Student.id == student.id)
        .first()
    )
    assert deleted_student is None
