from logging.config import dictConfig
import logging


dictConfig({
    'version': 1
    , 'formatters': {
        'default': {
            'format': '[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] %(message)s'
        }
    }
    , 'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
            , 'formatter': 'default'
            , 'level': 'DEBUG'
            # , 'stream': 'ext://sys.stdout'
            # filters: [allow_foo]
        }
        , 'file': {
            'class': 'logging.handlers.RotatingFileHandler'
            , 'formatter': 'default'
            , 'level': 'DEBUG'
            , 'filename': 'logconfig.log'
            , 'maxBytes': 1024
            , 'backupCount': 3
        }
    }
    , 'root': {
        'level': 'NOTSET'
        , 'handlers': ['console']
    }
})

# create logger instance
logger = logging.getLogger(__name__)

# create formatter for logger instance
# formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] %(message)s')

# create handler (stream, file)
# console log use only
# streamHandler = logging.StreamHandler()

# set formatter on logger instance
# streamHandler.setFormatter(formatter)

# set handler on logger instance
# logger.addHandler(streamHandler)

# print log by using logger instance
# logger.setLevel(level=logging.DEBUG)
# logger.debug('my DEBUG log')
# logger.info('my INFO log')
# logger.warning('my WARNING log')
# logger.error('my ERROR log')
# logger.critical('my CRITICAL log')

