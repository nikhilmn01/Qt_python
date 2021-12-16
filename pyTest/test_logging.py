import logging


def test_loggingDemo():
    log = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('myLogs.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    log.addHandler(fileHandler)

    log.setLevel(logging.WARNING)

    log.debug("A debug statement is executed")
    log.info("Information statement")
    log.debug("A debug statement is executed")
    log.warning("Something is in warning mode")
    log.error("A Major error has happened")
    log.critical("Critical issue")
