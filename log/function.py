import log

def test2():
    logger = log.set_log(module=__name__)
    logger.info("I'm in function")
    return 0