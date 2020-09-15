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



# TODO: refractor + reformat
EXPERIMENT_CREATE_FRAGMENT = """
    mutation CreateExperiment($userId: String!, $projectId: String!, $experimentId: String!, $name: String!, $nLoops: Int!, $nRecords: Int!, $qs: String!,
    $alType: String!, $date: String!) {
        createExperiment(userId: $userId, projectId: $projectId, experimentId: $experimentId, name: $name, nLoops: $nLoops, nRecords: $nRecords, qs: $qs, alType: $alType, date: $date) {
            ok
        }
    }
"""

PROJECT_CREATE_FRAGMENT = """
    mutation CreateProject($userId: String!, $preLabeled: String!, $alectioDataset: String!, $modelType: String!,
               $problemType: String!, $s3Bucket: String!, $premise: String!, $projectName: String!, $dataFormat: String!,
               $date: String!, $labelingType: Boolean!, $labelingCompany: Boolean!, $testLen: Int!, $trainLen: Int!, $allLabeled: Boolean!, $alectioDir: String!, $preLoadedModel: Boolean!
               $dockerUrl: String!, $ip: String!, $port: Int!){
        createProject(userId: $userId, preLabeled: $preLabeled, alectioDataset: $alectioDataset,
        modelType: $modelType, problemType: $problemType, s3Bucket: $s3Bucket, premise: $premise,
        projectName: $projectName, dataFormat: $dataFormat, date: $date, labelingType: $labelingType,
        labelingCompany: $labelingCompany, testLen: $testLen, trainLen: $trainLen, allLabeled: $allLabeled,
        alectioDir: $alectioDir, preLoadedModel: $preLoadedModel, dockerUrl: $dockerUrl, ip: $ip, port: $port) {
            ok
        }
    }
"""


JOBS_QUERY_FRAGMENT = """
    query jobsQuery($id: String!, $userId: String!) {
        jobs(id: $id, userId: $userId) {
            pk,
            sk,
            indices,
            dataUploaded,
            dataType,
        }
    }
"""
