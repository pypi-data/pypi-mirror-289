# lambda_app_common

```
pip install lambda_app_common
```

## Usage API Proxy Handler Controller

```python
import traceback
from http import HTTPStatus

from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig, Response
from aws_lambda_powertools.event_handler.exceptions import (InternalServerError)
from aws_lambda_powertools.utilities.typing import LambdaContext

from lambda_app_common import Organization, env_vars
req_handler = Organization.ApiRequestHandler('Application', 'Service')

cors_config = CORSConfig(allow_origin=env_vars.CORS_ALLOW_ORIGIN, max_age=300)
app = APIGatewayRestResolver(cors=cors_config)

examples = Examples()

@app.get("/examples")
def get_examples():
    try:
        response = examples.find_all()
    except Exception as e:
        examples.logger.exception(e)
        print(traceback.format_exc())
        raise InternalServerError(f"get_organization {str(e)}") from e

    return Response(status_code=HTTPStatus.OK.value, content_type="application/json",
                    body=req_handler.body_data(response))



# @tracer.capture_lambda_handler()
@examples.logger.inject_lambda_context(log_event=env_vars.LOG_EVENT)
@examples.metrics.log_metrics(capture_cold_start_metric=True)
def proxy_handler(event, context: LambdaContext):
    req_handler.event = event

    req_handler.init_metrics(examples.metrics)
    # req_handler.init_tracer(admin_organization.tracer)
    req_handler.init_logger(examples.logger)

    examples.context = req_handler.get_user_context()

    response = app.resolve(event, context)
    return response

```



```python
from lambda_app_common.Service import DbOrganizationService, OrganizationService

class DbOrganizationService(OrganizationService):
    def __init__(self,
                 service_name: str,
                 database: Database,
                 repository: ModelRepository,
                 event_bus: OrganizationEventBus,
                 logger: Logger,
                 tracer=None,
                 metrics=None
                 ):
        super().__init__(service_name, event_bus, logger, tracer, metrics)
        self.database = database
        self.repository = repository


class OrganizationService(PlatformService):

    def __init__(self,
                 service_name: str,
                 event_bus: OrganizationEventBus,
                 logger: Logger,
                 tracer=None,
                 metrics=None
                 ):
        super().__init__(service_name, event_bus, logger, tracer, metrics)
        self._context = None
        self._organization = None
        self._username = None
        self._user_groups = None
        self.user_applications = None
        self.user_branches = None
        self.user_zoneinfo = None
        self.user_locale = None
        self.user_env = None



class PlatformService(ABC):
    def __init__(self,
                 service_name: str,
                 event_bus: OrganizationEventBus,
                 logger: Logger,
                 tracer=None,
                 metrics=None
                 ):
        self.service_name: str = service_name
        self.current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.current_date = datetime.now().strftime('%Y-%m-%d')
        self._event_bus = event_bus
        self._logger = logger
        self._tracer = tracer
        self._metrics = metrics
```