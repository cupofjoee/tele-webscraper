import mechanize
from bs4 import BeautifulSoup
from urllib.request import urlopen
import http.cookiejar as cookie
import text-processing as tp

cj = cookie.CookieJar()
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_cookiejar(cj)
br.open("https://bms.ri.edu.sg/login.aspx")

br.select_form(nr = 0)
br.form['txtLoginID'] = '***REMOVED***'
br.form['txtPassword'] = '***REMOVED***'
br.submit()

attendance_url = "https://bms.ri.edu.sg/staff/Attendance.aspx"

br.open(attendance_url)

htmltxt = br.response().read()
soup = BeautifulSoup(htmltxt, 'lxml')
texts = []
for td in soup.find_all('td'):
    texts.append(td.text)

clean_data = tp.process_text(texts)