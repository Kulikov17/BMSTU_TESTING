import logging.config
from Librabobus.Logs.log_config import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger('main')