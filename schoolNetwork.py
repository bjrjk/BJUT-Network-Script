from bs4 import BeautifulSoup
import requests,time,sys
username = "Your Username";
password = "Your Password";

def Login():
	global username;
	global password;
	datas1={
		"DDDDD":username,"upass":password,"v46s":"0","v6ip":"","f4serip":"172.30.201.2","0MKKey":""
	};
	session = requests.Session();
	response1 = session.post("https://lgn6.bjut.edu.cn/V6?https://lgn.bjut.edu.cn", data=datas1, verify=False);
	bs = BeautifulSoup(response1.text, "html.parser");
	datas2={
		"DDDDD":username,"upass":password,"0MKKey":"Login","v6ip":bs.input()[2]['value']
	};
	response2 = session.post(bs.form['action'],data=datas2,verify=False);
	if response2.text.find("successfully")!=-1:
		print "Logged into network Successfully!";
	else:
		print "Logining failed! Please check!";
	
def Logout():
	response = requests.get("https://lgn.bjut.edu.cn/F.htm",verify=False);
	if response.text.find("successfully")!=-1:
		print "Logged out Successfully!";
	else:
		print "Log out failed! Please check!";
	
def Main():
	requests.packages.urllib3.disable_warnings()
	if len(sys.argv)==1:
		print "Usage: %s [login|logout]"%(sys.argv[0]);
	elif sys.argv[1]=='login':
		Login();
	elif sys.argv[1]=='logout':
		Logout();
	else:
		print "Command Error!\n"+"Usage: %s [login|logout]"%(sys.argv[0]);
	time.sleep(1);

if __name__ == '__main__':
	Main();