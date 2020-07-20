"""
fragments related to to queries received
"""

EXPERIMENTS_QUERY_FRAGMENT = """
    query experimentsQuery($id: String!) {
        experiments(id: $id) {
            pk, 
            sk,
            name,
            alType,
            nLoops,
            nRecords
        }
    }
"""

MODELS_QUERY_FRAGMENT = """
    query modelsQuery($id: String!) {
        models(id: $id) {
            pk, 
            sk,
            name,
            checksum
        }
    }
"""

MODEL_QUERY_FRAGMENT = """
    query modelQuery($id: String!) {
        model(id: $id) {
            pk, 
            sk,
            name,
            checksum
        }
    }
"""

PROJECTS_QUERY_FRAGMENT = """
    query projectsQuery($id: String!) {
        projects(id: $id) {
            pk, 
            sk,
            name,
            type
        }
    }
"""


PROJECT_QUERY_FRAGMENT = """
    query projectQuery($userId: String!, $projectId: String!) {
        project(userId: $userId, projectId: $projectId) {
            pk, 
            sk,
            name,
            type
        }
    }
"""