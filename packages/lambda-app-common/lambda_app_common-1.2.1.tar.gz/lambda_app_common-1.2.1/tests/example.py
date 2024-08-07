from lambda_app_common import Organization
api_handler = Organization.ApiRequestHandler('Application', 'Service')

event = Organization.OrganizationEvent('Application', 'Service')

api_handler.event = {}
api_handler.context = {}
api_handler.organization = 'Organization'
