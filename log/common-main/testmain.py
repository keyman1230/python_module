import log
import function



if __name__ == "__main__":
    logger = log.set_log(module=__name__)
    function.test2()
    logger.info("im in main.py")
