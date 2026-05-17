import pytest


class TestProjectsAPI:
    """Тесты для эндпоинтов проектов."""

    # --- Тесты для POST /api-v2/projects ---
    @pytest.mark.positive
    def test_create_project_success(
            self,
            projects_endpoint,
            test_project_data,
            test_project_id):
        """Позитивный тест: создание проекта с валидными данными."""
        response = projects_endpoint.create_project(test_project_data)
        assert response.status_code == 201, (
            f"Expected 201, got {
                response.status_code}. Response: {
                response.text}"
        )
        data = response.json()
        assert "id" in data, "Response should contain an 'id' field"
        test_project_id.append(data["id"])

    @pytest.mark.negative
    def test_create_project_missing_title(self, projects_endpoint):
        """Негативный тест: попытка создать проект без
        обязательного поля 'title'."""
        invalid_data = {"users": {"some-user-id": "admin"}}
        response = projects_endpoint.create_project(invalid_data)
        assert response.status_code == 400, (
            f"Expected 400, got {
                response.status_code}. Response: {
                response.text}"
        )

    # --- Тесты для PUT /api-v2/projects/{id} ---
    @pytest.mark.positive
    def test_update_project_success(
            self,
            projects_endpoint,
            test_project_id,
            test_project_update_data):
        """Позитивный тест: обновление существующего проекта."""
        if not test_project_id:
            pytest.skip("No project ID from previous test")
        project_id = test_project_id[0]
        response = projects_endpoint.update_project(
            project_id, test_project_update_data)
        assert response.status_code == 200

    @pytest.mark.negative
    def test_update_nonexistent_project(self, projects_endpoint):
        """Негативный тест: обновление несуществующего проекта."""
        nonexistent_id = "00000000-0000-0000-0000-000000000000"
        update_data = {"title": "Ghost Project"}
        response = projects_endpoint.update_project(
            nonexistent_id, update_data)
        assert response.status_code == 404

    # --- Тесты для GET /api-v2/projects/{id} ---
    @pytest.mark.positive
    def test_get_project_success(self, projects_endpoint, test_project_id):
        """Позитивный тест: получение данных существующего проекта."""
        if not test_project_id:
            pytest.skip("No project ID from previous test")
        project_id = test_project_id[0]
        response = projects_endpoint.get_project(project_id)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id

    @pytest.mark.negative
    def test_get_nonexistent_project(self, projects_endpoint):
        """Негативный тест: попытка получить несуществующий проект."""
        nonexistent_id = "00000000-0000-0000-0000-000000000000"
        response = projects_endpoint.get_project(nonexistent_id)
        assert response.status_code == 404
