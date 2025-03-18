import uuid, random, requests, time ,os

os.system("clear")
uid=input(" !-! USERNAME or Number/Email: ")
ps=input(" !-! Password :")

data={
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': "#PWD_REACTNATIVE:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate'}
head={
                'User-Agent': '[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142836;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/AREEBA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200F;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000,40000000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'}
url="https://graph.facebook.com/auth/login"
rq=requests.post(url,data=data,headers=head,allow_redirects=False).json()
if "session_key" in rq:
    coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
    print(" Cookies: ",coki)
else:
    print(" !-! Use Another Account ")
