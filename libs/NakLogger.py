import logging

logging.basicConfig(filename='marvin.log',level=logging.DEBUG)
logger = logging.getLogger('MARVIN')
logger.setLevel(logging.DEBUG)


def consoleDebugActive(consoleActivated):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if(consoleActivated):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warn(message):
    logger.warn(message)

def error(message):
    logger.error(message)

def critical(message):
    logger.critical(message)
