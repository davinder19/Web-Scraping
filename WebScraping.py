import requests
from bs4 import BeautifulSoup

data = requests.get("https://davinder19.github.io/davinder-portfolio/")
# use BeautifulSoup(data.content)  method used to understand  body of responseHtml nad pass 2 parameters data.content
# data is response object   we apply content method on this variable and pass to BS soap
# how to pass it so pass Html parser
soup = BeautifulSoup(data.content, 'html.parser')
HeroHeader = soup.find('div', {'class': 'content'})
print(HeroHeader.text)
Navbar = soup.find('div', {'class': 'nav-contain'})
print(Navbar.text)




Specialties = soup.find('div', {'class': 'about'})
Header = Specialties.find('h1').text
print("*************", Header, "*****************")
SubHeader = Specialties.findAll('h2')
for Sub in SubHeader:
    print(Sub.text)
print("******************  PROJECTS ***********************")
Projects = soup.find('div', {'class': 'projects-contianer'})
Titles = Projects.findAll('h2')

Count = 0
for Title in Titles:
    Count = Count+1
    print(Title.text)
print("Total Projects is:", Count)
print("************************  SKILLS ***********************")

SkillTable = soup.find('div',{'class': 'myskills'})
Percentages = SkillTable.findAll('h4')
# print(SkillTable)
Skills = SkillTable.findAll('h3')
SkillCount = 0
for Skill in Skills:
    SkillCount = SkillCount+1
    print( Skill.text)
print("Total Skiils is:", SkillCount)
# *********************** Testing  Page ***************************************************************
print("# *********************** Testing  Page ***************************************************************")
NavUls = Navbar.findAll('li')
SubUrl = NavUls[1].a['href']
SubData = requests.get("https://davinder19.github.io/davinder-portfolio/"+SubUrl)
# print(SubData.text)
NextPage = BeautifulSoup(SubData.content, 'html.parser')
MainHeader = NextPage.find('div',{'class': 'bug-fre'})
print(MainHeader.text)
ToolsHeaders = NextPage.findAll('div',{'class': 'agile-box-bd-2'})
for ToolsHeader in ToolsHeaders:
    print(ToolsHeader.text)
BugTester = NextPage.findAll('div',{'class': 'bug-test-section'})
for BugTest in BugTester:
    print(BugTest.text)

Intro = soup.find('div',{'class': 'address-item'})
print(Intro.text)
print("*****************Thank You****************************************")


















