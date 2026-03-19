from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests
import random
from datetime import datetime
import traceback
import urllib3

# --- Protobuf Imports ---
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==============================================================================
# PB2 MERGED DIRECTLY INTO APP.PY (No external folders needed)
# ==============================================================================
_sym_db = _symbol_database.Default()

# 1. MajorLoginReq
DESCRIPTOR_REQ = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginReq.proto\"\xfa\n\n\nMajorLogin\x12\x12\n\nevent_time\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x13\n\x0bplatform_id\x18\x05 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x07 \x01(\t\x12\x17\n\x0fsystem_software\x18\x08 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\t \x01(\t\x12\x18\n\x10telecom_operator\x18\n \x01(\t\x12\x14\n\x0cnetwork_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\r\x12\x15\n\rscreen_height\x18\r \x01(\r\x12\x12\n\nscreen_dpi\x18\x0e \x01(\t\x12\x19\n\x11processor_details\x18\x0f \x01(\t\x12\x0e\n\x06memory\x18\x10 \x01(\r\x12\x14\n\x0cgpu_renderer\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x18\n\x10unique_device_id\x18\x13 \x01(\t\x12\x11\n\tclient_ip\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x18 \x01(\t\x12\'\n\x10memory_available\x18\x19 \x01(\x0b\x32\r.GameSecurity\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x17\n\x0fplatform_sdk_id\x18\x1e \x01(\x05\x12\x1a\n\x12network_operator_a\x18) \x01(\t\x12\x16\n\x0enetwork_type_a\x18* \x01(\t\x12\x1c\n\x14\x63lient_using_version\x18\x39 \x01(\t\x12\x1e\n\x16\x65xternal_storage_total\x18< \x01(\x05\x12\"\n\x1a\x65xternal_storage_available\x18= \x01(\x05\x12\x1e\n\x16internal_storage_total\x18> \x01(\x05\x12\"\n\x1ainternal_storage_available\x18? \x01(\x05\x12#\n\x1bgame_disk_storage_available\x18@ \x01(\x05\x12\x1f\n\x17game_disk_storage_total\x18\x41 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_avail_storage\x18\x42 \x01(\x05\x12%\n\x1d\x65xternal_sdcard_total_storage\x18\x43 \x01(\x05\x12\x10\n\x08login_by\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x12\n\nreg_avatar\x18L \x01(\x05\x12\x15\n\rlibrary_token\x18M \x01(\t\x12\x14\n\x0c\x63hannel_type\x18N \x01(\x05\x12\x10\n\x08\x63pu_type\x18O \x01(\x05\x12\x18\n\x10\x63pu_architecture\x18Q \x01(\t\x12\x1b\n\x13\x63lient_version_code\x18S \x01(\t\x12\x14\n\x0cgraphics_api\x18V \x01(\t\x12\x1d\n\x15supported_astc_bitset\x18W \x01(\r\x12\x1a\n\x12login_open_id_type\x18X \x01(\x05\x12\x18\n\x10\x61nalytics_detail\x18Y \x01(\x0c\x12\x14\n\x0cloading_time\x18\\ \x01(\r\x12\x17\n\x0frelease_channel\x18] \x01(\t\x12\x12\n\nextra_info\x18^ \x01(\t\x12 \n\x18\x61ndroid_engine_init_flag\x18_ \x01(\r\x12\x0f\n\x07if_push\x18\x61 \x01(\x05\x12\x0e\n\x06is_vpn\x18\x62 \x01(\x05\x12\x1c\n\x14origin_platform_type\x18\x63 \x01(\t\x12\x1d\n\x15primary_platform_type\x18\x64 \x01(\t\"5\n\x0cGameSecurity\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x14\n\x0chidden_value\x18\x08 \x01(\x04\x62\x06proto3')
_globals_req = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR_REQ, _globals_req)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR_REQ, 'MajorLoginReq_pb2', _globals_req)

# 2. MajorLoginRes
DESCRIPTOR_RES = _descriptor_pool.Default().AddSerializedFile(b'\n\x13MajorLoginRes.proto\"|\n\rMajorLoginRes\x12\x13\n\x0b\x61\x63\x63ount_uid\x18\x01 \x01(\x04\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\n \x01(\t\x12\x11\n\ttimestamp\x18\x15 \x01(\x03\x12\x0b\n\x03key\x18\x16 \x01(\x0c\x12\n\n\x02iv\x18\x17 \x01(\x0c\x62\x06proto3')
_globals_res = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR_RES, _globals_res)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR_RES, 'MajorLoginRes_pb2', _globals_res)
# ==============================================================================


app = Flask(__name__)

# --- কনফিগুরেশন ---
AES_KEY = b'Yg&tc%DEuh6%Zc^8'
AES_IV = b'6oyZDr22E3ychjM%'

HEADERS = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB52"
}

def encrypt_data(data):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    return cipher.encrypt(pad(data, 16))

def get_session_token(uid, password):
    session = requests.Session()
    try:
        # Step 1: Get Guest Token from Garena
        auth_url = "https://100067.connect.garena.com/oauth/guest/token/grant"
        auth_data = {
            "uid": uid, "password": password, "response_type": "token",
            "client_type": "2", "client_id": "100067",
            "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
        }
        auth_res = session.post(auth_url, data=auth_data, headers=HEADERS, verify=False)
        
        if auth_res.status_code != 200:
            print("[Error] Garena Token Grant Failed!")
            return None
            
        j = auth_res.json()
        open_id = j.get("open_id")
        access_token = j.get("access_token")

        if not open_id or not access_token:
            return None

        # Step 2: Major Login Payload (Using embedded protobufs)
        major_login = MajorLogin()
        major_login.event_time = str(datetime.now())[:-7]
        major_login.game_name = "free fire"
        major_login.platform_id = 1
        major_login.client_version = "1.120.1"
        major_login.system_software = "Android OS 10 / API-29 (QP1A.190711.020/A515FXXU4CTJ1)"
        major_login.system_hardware = "mt6769t"
        major_login.telecom_operator = "Grameenphone"
        major_login.network_type = "WIFI"
        major_login.screen_width = 1080
        major_login.screen_height = 2340
        major_login.screen_dpi = "440"
        major_login.processor_details = "AArch64 Processor rev 4 (aarch64) | 8 cores"
        major_login.memory = 4096
        major_login.gpu_renderer = "Mali-G52 MC2"
        major_login.gpu_version = "OpenGL ES 3.2 v1.r14p0-01rel0"
        major_login.unique_device_id = f"android|{random.randint(10000000,99999999)}"
        major_login.client_ip = "127.0.0.1"
        major_login.language = "en"
        major_login.open_id = open_id
        major_login.open_id_type = "4"
        major_login.device_type = "Handheld"
        major_login.access_token = access_token
        major_login.platform_sdk_id = 1
        major_login.network_operator_a = "Grameenphone"
        major_login.network_type_a = "WIFI"
        major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
        major_login.external_storage_total = 114441
        major_login.external_storage_available = 25432
        major_login.internal_storage_total = 114441
        major_login.internal_storage_available = 25432
        major_login.game_disk_storage_available = 25432
        major_login.game_disk_storage_total = 114441
        major_login.external_sdcard_avail_storage = 25432
        major_login.external_sdcard_total_storage = 114441
        major_login.login_by = 3
        major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
        major_login.reg_avatar = 1
        major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
        major_login.channel_type = 3
        major_login.cpu_type = 2
        major_login.cpu_architecture = "64"
        major_login.client_version_code = "2019118695"
        major_login.graphics_api = "OpenGLES2"
        major_login.supported_astc_bitset = 16383
        major_login.login_open_id_type = 4
        major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
        major_login.loading_time = random.randint(12000, 15000)
        major_login.release_channel = "android"
        major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
        major_login.android_engine_init_flag = 110009
        major_login.if_push = 1
        major_login.is_vpn = 0
        major_login.origin_platform_type = "4"
        major_login.primary_platform_type = "4"
        major_login.memory_available.version = 55
        major_login.memory_available.hidden_value = 81
        
        serialized_payload = major_login.SerializeToString()
        encrypted_payload = encrypt_data(serialized_payload)

        # Step 3: Major Login Call
        login_url = "https://loginbp.ggblueshark.com/MajorLogin"
        login_res = session.post(login_url, data=encrypted_payload, headers=HEADERS, verify=False)
        
        if login_res.status_code == 200:
            proto_res = MajorLoginRes()
            proto_res.ParseFromString(login_res.content)
            return proto_res.token 
        else:
            return None
            
    except Exception as e:
        print(f"[Error] Exception in login: {e}")
        return None

# --- ২. লং বায়ো প্রোটো তৈরি ---
def create_long_bio_proto(bio_text):
    field_2 = b'\x08\x11'
    field_5 = b'\x2A\x00'
    field_6 = b'\x32\x00'
    
    bio_bytes = bio_text.encode('utf-8')
    bio_len = len(bio_bytes)
    
    def encode_varint(value):
        encoded = []
        while value > 127:
            encoded.append((value & 0x7F) | 0x80)
            value >>= 7
        encoded.append(value)
        return bytes(encoded)
    
    field_8 = b'\x42' + encode_varint(bio_len) + bio_bytes
    
    field_9 = b'\x48\x01'
    field_11 = b'\x5A\x00'
    field_12 = b'\x62\x00'
    
    return field_2 + field_5 + field_6 + field_8 + field_9 + field_11 + field_12

# --- ৩. মেইন এপিআই এন্ডপয়েন্ট ---
@app.route('/run-bio', methods=['POST'])
def run_bio_script():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided!"}), 400

    bio1 = data.get('bio1', '')
    bio2 = data.get('bio2', '')
    bio3 = data.get('bio3', '')
    uid = data.get('bot_id', '')
    password = data.get('bot_pass', '')

    if not uid or not password:
        return jsonify({"error": "bot_id and bot_pass are required!"}), 400

    full_bio = f"{bio1}\n{bio2}\n{bio3}"
    
    print(f"\n[⏳] Processing UID: {uid}")
    
    token = get_session_token(uid, password)
    if not token:
        return jsonify({"status": "error", "message": "Login failed! Invalid ID/Pass."}), 401
        
    print("[✅] Got Login Token.")

    try:
        update_url = "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo"
        proto_data = create_long_bio_proto(full_bio)
        encrypted_bio = encrypt_data(proto_data)

        headers = HEADERS.copy()
        headers['Content-Type'] = "application/octet-stream"
        headers['Authorization'] = f"Bearer {token}"

        response = requests.post(update_url, data=encrypted_bio, headers=headers, verify=False)

        if response.status_code == 200:
            print("[✅] Bio Updated Successfully!")
            return jsonify({
                "status": "success",
                "message": "Long bio updated successfully!",
                "uid": uid,
                "bio_preview": full_bio
            }), 200
        else:
            return jsonify({"status": "error", "message": f"Server returned HTTP {response.status_code}"}), 500

    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("[*] API Server Running on port 5000...")
    app.run(host='0.0.0.0', port=5000)