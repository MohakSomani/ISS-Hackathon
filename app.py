from flask import *
import requests
from lxml import html


app = Flask(__name__)

names = []
post = []
lab = []
temp=[]
email = []
qualification = []
contact = []

print("Accessing page")
url = "https://www.iiit.ac.in/people/faculty/"
response = requests.get(url)

root = html.fromstring(response.content)

names.extend(root.xpath('//h3[@class="name"]/a/text()'))
# email.extend(root.xpath('//span[@class="genre"]/text()'))
lab.extend(root.xpath('//td/p/a/text()'))
temp.extend(root.xpath('//td/p[1]/text()'))
temp = [string.replace("\n", "") for string in temp]
temp = [string.strip() for string in temp]
temp.remove('20+ years in Software industry- Technology Products R&D & Innovation leadership.')
i=0
for ele in temp:
    if i==0:
        post.append(ele)
        i=1
    elif i==1:
        qualification.append(ele)
        i=0
for ele in names:
    teml=(ele).split(' ')
    if teml[0].lower()=='vishal':
        email.append(teml[0].lower()+"."+teml[1].lower()+"@iiit.ac.in")
    elif teml[len(teml)-1] == '[Onleave]':
        email.append(teml[0].lower()+"."+teml[len(teml)-2].lower()+"@iiit.ac.in")
    else:
        email.append(teml[0].lower()+"."+teml[len(teml)-1].lower()+"@iiit.ac.in")

specname=['Anil Kumar Vuppala','Dipti Misra Sharma','Girish Varma','Indranil Chakrabarty','Kavita Vemuri','Krishna Reddy P.',
          'Raghu Babu Reddy Y.','Rajeev Sangal','Ramachandra Prasad P.','Ramesh Loganathan','Samyadeb Bhattacharya',
          'Shantanav Chakraborty','Shatrunjay Rawat','Syed  Azeemuddin [Onleave]','Venkatesh Choppella ','Vikram Pudi',
          'Vishal Garg [onleave]']
for i in range (len(names)):
    if names[i]=='Jayanthi Sivaswamy' or names[i]=='Nimmi Rangaswamy' or names[i]=='Pradeep  Kumar Ramancharla [Onleave]' or names[i]=='Rajan K. S.' or names[i]=='Vasudeva Varma' or names[i]=='Venkateshwarlu M':
        lab[i]=lab[i]+','+lab[i+1]+','+lab[i+2]
        del lab[i+1]
        del lab[i+1]
    elif names[i] in specname:
        lab[i]=lab[i]+','+lab[i+1]
        del lab[i+1]
contacts=['7226037642', '7215139084', '7256354806', '7490520194','7027498259', '7277524117', '7696698694', '7308388884', '7898242521','7779760309', '7048428317', '7299882564', '7875372450', '7830591908',
    '7395117659', '7041949560', '7312239452', '7791874153', '7747113852','7840403059', '7306318149', '7034189013', '7754005040', '7332011117','7106939586', '7480087465', '7402780106', '7684070353', '7880852763','7363861183', '7987120449', '7204446637', '7006343246', '7797378531','7217106876', '7351843585', '7158853986', '7633894745', '7993329344''7069644374', '7550647007', '7817570548', '7274340484', '7378214674','7975308677', '7650490631', '7840030383', '7941717813', '7563828947','7242462517', '7385182273', '7686305483', '7472954593', '7838126794','7025859741', '7717909514', '7305437195', '7486567695', '7455413287','7987900077', '7099261970', '7052004206', '7258778804', '7937333437','7316334314', '7822255283', '7081020389', '7764361093', '7976093045','7072457873', '7993462196', '7974139578', '7800053871', '7901292162','7158568930', '7899848402', '7455850112', '7214227055', '7236348997','7550190787', '7255025864', '7757083556', '7125763384', '7592226827','7555665475', '7898593274', '7126193029', '7178580633', '7935626151','7026494358', '7176115656', '7378344658', '7768911737', '7935421349','7963351372', '7193753082', '7125031657', '7731458449', '7492969356','7788659002', '7257574412', '7474223019', '7867965839', '7991099202','7129775378', '7261717597', '7897447843', '7843578736', '7743478574'
]
print(len(names))
data=[]
for i in range (len(names)):
    data.append(names[i]+';--'+post[i]+';--'+qualification[i]+';--'+lab[i]+';--'+email[i]+';--'+contacts[i])


@app.route("/")
def home() -> str:
    return render_template("index.html")

@app.route("/about")
def abt() -> str:
    return render_template("about_page.html")


@app.route("/students")
def student() -> str:
    return render_template("student_page.html")


@app.route("/faculty")
def faculty() -> str:
    return render_template("faculty_page.html",data=data)

@app.route("/input1")
def inp() -> str:
    return render_template("input_page.html")


@app.route("/input")
def fir() -> str:
    return render_template("FirstPage.html")

if __name__ == "__main__":
    app.run(debug=True)
