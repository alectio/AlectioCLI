"""
mutations commands to update / create resources
"""

##### MUTATIONS #####

UPDATE_IP_PORT_MUTATION = """mutation updateProjectIp($userId: String!, $projectId: String!, $ip: String, $port: Int) {
    updateProjectIp(userId: $userId, projectId: $projectId, ip: $ip, port: $port) {
        project {
            onPremField
        }
    }
}"""


UPLOAD_QUERY_STRATEGY_MUTATION = """mutation uploadQueryStrategyMutation($queryStratData: [QueryStrategyInput], $projectId: String!, $experimentId: String!, $type: String!, $mode: String!) {
    uploadQueryStrategyMutation(queryStratData: $queryStratData, projectId:$projectId, experimentId:$experimentId, type:$type, mode:$mode) {
        ok
        message
    }
}"""

##### FILE UPLOAD MUTATIONS #####

UPLOAD_PARTNER_IMAGE_MUTATION = """mutation uploadPartnerImageMutation($files: Upload!, $records: [RecordsInput],  $jobId: String!) {
    uploadPartnerImageMutation(files: $files, records: $records, jobId: $jobId) {
        ok
    }
}"""

# TODO: support for this
UPLOAD_PARTNER_TEXT_MUTATION = """mutation uploadPartnerTextMutation($files: Upload!, $records: [RecordsInput],  $jobId: String!) {
    uploadPartnerTextMutation(files: $files, records: $records, jobId: $jobId) {
        ok
    }
}"""

# TODO: support fo this
UPLOAD_PARTNER_NUMERICAL_MUTATION = """mutation uploadPartnerNumericalMutation($files: Upload!, $records: [RecordsInput],  $jobId: String!) {
    uploadPartnerNumericalMutation(files: $files, records: $records, jobId: $jobId) {
        ok
    }
}"""

START_EXPERIMENT_MUTATION = """mutation startExperimentMutation($userId: String!, $projectId: String!, $experimentId: String!) {
    startExperimentMutation(userId: $userId, projectId: $projectId, experimentId: $experimentId) {
        ok
    }
}"""

UPLOAD_CLASS_LABELS_MUTATION = """mutation uploadClassLabelsMutation($userId: String!, $projectId: String!, $classLabels: String!) {
    uploadClassLabelsMutation(userId: $userId, projectId: $projectId, classLabels: $classLabels) {
        ok
    }
}"""

##### FILE DOWNLOAD MUTATIONS #####
