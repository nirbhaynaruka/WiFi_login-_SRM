from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException

usernameStr = 'ns9930'
passwordStr = 'Nsn@1999'

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template(index.html)


# @app.route('/getData', methods=['POST'])
# def getData():
#     usernameStr = request.form['username']
#     passwordStr = request.form['password']

# if __name__ == "__main__":
#     app.run(debug=True)


# timeout = 3
options = Options()
# options.headless = True
# browser = webdriver.Firefox(
#    options=options, executable_path=r'E:\New Project\Scrapsrm by Python\geckodriver.exe')
browser = webdriver.Chrome()
browser.implicitly_wait(30)
browser.get(('https://iac.srmist.edu.in/connect/PortalMain'))
# browser.get('https://www.facebook.com/')
# browser.find_element_by_id("moreInformationDropdownLink").click()
# browser.find_element_by_id("invalidcert_continue").click()

username = browser.find_element_by_id('LoginUserPassword_auth_username')
username.clear()
password = browser.find_element_by_id('LoginUserPassword_auth_password')
username.clear()
username.send_keys(usernameStr)
password.send_keys(passwordStr)

browser.find_element_by_id("UserCheck_Login_Button").click()
# browser.find_element_by_id('u_0_a').click()
# logo = browser.find_element_by_class_name('header-png')
# link = browser.find_element_by_link_text("My Time Table & Attendance")
# link.click()
# browser.find_element_by_link_text("#View:My_Time_Table_2019_20_Odd")
# browser.get('https://academia.srmuniv.ac.in/#View:My_Time_Table_2019_20_Odd')
# browser.find_element(By.CLASS_NAME, 'zc-tabmenu').click()

screenshot = browser.save_screenshot('snap3.png')

browser.quit()
