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


##### FILE UPLOAD MUTATIONS #####

UPLOAD_PARTNER_IMAGE_MUTATION = """mutation uploadPartnerImageMutation($files: Upload!) {
    uploadPartnerImageMutation(files: $files) {
        ok
    }
}"""


UPLOAD_PARTNER_TEXT_MUTATION = """mutation uploadPartnerTextMutation($files: Upload!) {
    uploadPartnerTextMutation(files: $files) {
        ok
    }
}"""


UPLOAD_PARTNER_NUMERICAL_MUTATION = """mutation uploadPartnerNumericalMutation($files: Upload!) {
    uploadPartnerNumericalMutation(files: $files) {
        ok
    }
}"""

##### FILE DOWNLOAD MUTATIONS #####