import logging

logger: logging.Logger = logging.getLogger('telegram-steam')

def set_logger():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s](%(filename)s:%(lineno)d) - %(levelname)s - %(message)s", \
            datefmt="%Y-%m-%d %I:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

set_logger()
