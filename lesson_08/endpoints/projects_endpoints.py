class ProjectsEndpoint:
    def __init__(self, client):
        self.client = client
        self.base_path = '/api-v2/projects'

    def create_project(self, project_data):
        """POST /api-v2/projects: Создание нового проекта."""
        return self.client.post(self.base_path, json_data=project_data)

    def update_project(self, project_id, project_data):
        """PUT /api-v2/projects/{id}: Обновление проекта по ID."""
        return self.client.put(
            f"{self.base_path}/{project_id}", json_data=project_data)

    def get_project(self, project_id):
        """GET /api-v2/projects/{id}: Получение проекта по ID."""
        return self.client.get(f"{self.base_path}/{project_id}")
