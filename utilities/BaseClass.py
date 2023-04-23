import inspect
import logging
import pytest
import datetime

@pytest.mark.usefixtures("setup")
class BaseClass:
    @staticmethod
    def getLogger():
        # Get the current date and time
        now = datetime.datetime.now()
        # Format the date as YYYY-MM-DD
        date_string = now.strftime("%Y-%m-%d")
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(f"C:\\Users\\amuly\\PycharmProjects1\\SeleniumPythonFramework\\Output\\logfile_{date_string}.log", mode="w")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger



