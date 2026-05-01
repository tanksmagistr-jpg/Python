import pytest
from api_client import YougileAPIClient
from endpoints.projects_endpoints import ProjectsEndpoint

@pytest.fixture
def client():
    return YougileAPIClient()

@pytest.fixture
def projects_endpoint(client):
    return ProjectsEndpoint(client)

@pytest.fixture
def test_project_data():
    # Важно: не отправляйте поле users с невалидным UUID
    return {"title": "Test Project"}

@pytest.fixture
def test_project_update_data():
    return {"title": "Updated Project Name"}

@pytest.fixture
def test_project_id():
    """Список для хранения ID созданных проектов."""
    return []
