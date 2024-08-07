import os

LOCAL = bool(True if os.getenv('STAGE', 'local') == 'local' else False)

if LOCAL is True:
    from dotenv import load_dotenv
    load_dotenv()

LOG_DB_TRANSACTIONS = True if os.getenv('LOG_DB_TRANSACTIONS') == '1' else False

LOG_LEVEL = os.getenv('POWERTOOLS_LOG_LEVEL', 'INFO')
LOG_EVENT = os.getenv('LOG_EVENT', 0) == '1'
CORS_ALLOW_ORIGIN = os.getenv('CORS_ALLOW_ORIGIN', '*')

EVENTS_BUS_NAME = os.environ.get('EVENTS_BUS')

STAGE = os.environ.get('STAGE', 'dev')
ENV = STAGE
