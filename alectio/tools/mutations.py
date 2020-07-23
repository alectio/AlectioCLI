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

# UPLOAD_PARTNER_IMAGE_MUTATION = """mutation uploadPartnerImageMutation($file: Upload!) {
#     uploadPartnerImageMutation(file: $file) {
#        ok
#     }
# }"""

UPLOAD_PARTNER_IMAGE_MUTATION = """mutation uploadPartnerImageMutation($file: Upload!) {
    uploadPartnerImageMutation(file: $file) {
        ok
    }
}"""


# UPLOAD_PARTNER_TEXT_MUTATION = '''
#         mutation uploadPartnerTextMutation($file: Upload!) {
#             uploadPartnerTextMutation(file: $file) {
#                 ok
#             }
#         }
# '''


# UPLOAD_PARTNER_NUMERICAL_MUTATION = '''
#         mutation uploadPartnerNumericalMutation($file: Upload!) {
#             uploadPartnerNumericalMutation(file: $file) {
#                 ok
#             }
#         }
# '''