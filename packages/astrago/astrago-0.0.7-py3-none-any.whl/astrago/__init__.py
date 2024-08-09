from .tracking import *
from .val import workload_name, url
from .tracking import LoggingClient

__version__ = '0.0.7'
client = LoggingClient()
__all__ = (
    'log'
)


def log(log_data: Dict):
    client.log(log_data)
