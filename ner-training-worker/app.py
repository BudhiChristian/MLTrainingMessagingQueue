import yaml
import logging
import logging.config

from training_module.main import train_data
from messaging_module import Messenger

with open('./config.yml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)

with open('./logging/log.config.yml', 'r') as log_config_file:
    log_config = yaml.load(log_config_file, Loader=yaml.FullLoader)
    logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

messenger = Messenger(config['messagingConfiguration'])
messenger.start(train_data)