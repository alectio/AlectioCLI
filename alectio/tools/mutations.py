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