"""
query fragments
"""


##### QUERIES ##### 

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

EXPERIMENT_QUERY_FRAGMENT = """
    query experimentQuery($id: String!) {
        experiment(id: $id) {
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
            type,
            onPremField
        }
    }
"""


PROJECT_QUERY_FRAGMENT = """
    query projectQuery($userId: String!, $projectId: String!) {
        project(userId: $userId, projectId: $projectId) {
            pk, 
            sk,
            name,
            type,
            onPremField
        }
    }
"""

USER_PAID_QUERY_FRAGMENT = """
    query userQuery($id: String!) {
        user(id: $id) {
            isPaid
        }
    }
"""