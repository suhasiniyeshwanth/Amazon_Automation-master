import pytest
from source.utilities import globals
from datetime import datetime
import os


class ReportPlugin:

    def pytest_sessionfinish(self):
        globals.ALLURE_REPORTS = globals.ALLURE_REPORTS + datetime.now().\
            strftime("%d_%m_%Y_%H_%M_%S")
        os.popen("allure generate "+globals.ALLURE_RESULTS +" --output "
                 +globals.ALLURE_REPORTS)

argument = ['-q', '--alluredir', globals.ALLURE_RESULTS]
pytest.main(argument, plugins=[ReportPlugin()])
