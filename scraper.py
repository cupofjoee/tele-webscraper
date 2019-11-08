import mechanize
from bs4 import BeautifulSoup
from urllib.request import urlopen
import http.cookiejar as cookie
from datetime import datetime

def fetch_data():
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

    clean_data = process_text(texts)
    return clean_data

def process_text(lst):   
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    def new_line_filter(x):
        if '\n\n\n' in x:
            return False
        else:
            return True

    filter1 = lst[42:201] #cut out irrelevant text
    filter2 = list(filter(new_line_filter, filter1)) #filter the "\n\n\n"
    filter3 = []
    filter4 = [dt_string]
    for i in range(len(filter2)): 
        if ((i - 3) % 7 == 0) or ((i - 4) % 7 == 0) or ((i - 5) % 7 == 0) : #cut out irrelevant column 4, 5 and 6 
            pass
        else:
            a = filter2[i].strip("\n") #strip all \n
            if a == '\xa0': #null leave information
                a = "no-leave"
            filter3.append(a)
    for i in range(0, len(filter3), 4):
        filter4.append(" | ".join(filter3[i:i+4]))
    return filter4

# raw data for testing
# texts = ['\n\nMy Records\n\n', 'My Records', '', '\n\nMy Profile\n\n', 'My Profile', '', '\n\nLeave\n\n', 'Leave', '', '\n\nRoom Checking\n\n', 'Room Checking', '\n\nChange Password\n\n', 'Change Password', '\n\nMy Defect Records\n\n', 'My Defect Records', '\n\nMy Feedback Records\n\n', 'My Feedback Records', '\n\nEdit Profile\n\n', 'Edit Profile', '\n\nActive Leaves\n\n', 'Active Leaves', '\n\nAttendance Listing\n\n', 'Attendance Listing', '\n\nRoom Check Report By Boarder\n\n', 'Room Check Report By Boarder', '\nDate From', '  ', 'To', ' ', 'NRIC/FIN', ' ', 'Name', ' ', 'Block', '\n--All--\nHullett 1\nHullett 2\n', 'Finger Print Scanning Status', '\nYesNo\n', 'No Paging:', '', '', '\n', '\n1\n\n\n', '91048440', '\nNITITHUM BHAK\n', 'Hullett 1/5.01/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n2\n\n\n', '85048360', '\nHO THUY SON\n', 'Hullett 1/5.01/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n3\n\n\n', '98606990', '\nYap Bing Yu\n', 'Hullett 1/5.02/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n4\n\n\n', '84315370', '\nLAM WENG CHUNG\n', 
# 'Hullett 1/5.02/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n5\n\n\n', '83016910', '\nVU TIEN LUC\n', 'Hullett 1/5.03/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n6\n\n\n', '84012592', '\nTAN YIMING\n', 'Hullett 1/5.03/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n7\n\n\n', '91749334', '\nLEI LINGKAI\n', 'Hullett 1/3.06/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n8\n\n\n', '82492987', '\nMA JINGXUAN\n', 'Hullett 1/5.04/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n9\n\n\n', '86530287', '\nSun Siliang\n', 'Hullett 1/5.05/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n10\n\n\n', '91037745', '\nClaudeon Reinard Susanto\n', 'Hullett 1/5.05/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n11\n\n\n', '86728748', '\nLI ZHENGXUAN\n', 'Hullett 1/5.08/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n12\n\n\n', '84146316', '\nMEN CHENGKAI\n', 'Hullett 1/5.08/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n13\n\n\n', '86515424', '\nChen Siyu\n', 'Hullett 1/5.10/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n14\n\n\n', '84557410', '\nWen Dengboyu\n', 'Hullett 1/5.10/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n15\n\n\n', '94671632', '\nLIU LEKANG\n', 
# 'Hullett 1/4.01/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n16\n\n\n', '83154078', '\nChen Muzi\n', 'Hullett 1/4.02/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n17\n\n\n', '87102056', '\nGuoli Zhiru\n', 'Hullett 1/4.02/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n18\n\n\n', '83718971', '\nTRAN PHUOC MY\n', 'Hullett 1/4.03/A', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n19\n\n\n', '83577128', '\nNGUYEN AN KHANH\n', 'Hullett 1/4.03/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n20\n\n\n', '82858255', '\nYUAN SHUAI\n', 'Hullett 1/4.04/B', '29/10/2019', '\xa0', '\xa0', '\xa0', '\n\n123456\n\n', '1', '2', '3', '4', '5', '6']

# print(process_text(texts))