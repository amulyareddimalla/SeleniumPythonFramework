#this is a centralized fixture which executes before running actual test case
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

#request instance comes by default when we declare a fixture
@pytest.fixture(scope="class")
def setup(request):

    browser_name=request.config.getoption("browser_name") #will pull the value from 'browser_name' which you passed at run time
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service("C:/Users/amuly/PycharmProjects1/SeleniumPythonFramework/Drivers/chromedriver.exe"))
        driver.maximize_window()
    elif browser_name == "edge":
        # Set the path to the Edge webdriver executable file
        edge_driver_path = r"C:/Users/amuly/PycharmProjects1/SeleniumPythonFramework/Drivers/msedgedriver.exe"
        # Create an instance of the Edge webdriver service
        edge_service = Service(executable_path=edge_driver_path)
        # Create an instance of the Edge options object
        edge_options = Options()
        # Create an instance of the Edge webdriver, passing in the service and options objects
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        driver.maximize_window()
    #assigning local driver to class driver so which ever class uses this fixture can use this driver
    request.cls.driver=driver
    yield
    driver.close()

###### Pytest HTML Report ######
#it is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Open Cart Selenium with Python Automation for Associate Architect'
    #config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Amulya Reddimalla'

#it is hook to delete or modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

