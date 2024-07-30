import requests
import socks
import socket
original_socket = socket.socket
print(original_socket)
# Set up SOCKS proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 1080)
socket.socket = socks.socksocket
print(socket.socket)
headers = {
    'Connection': 'keep-alive',
    'Authorization': 'Basic c3lzYWRtaW46U3lzYWRtaW5AMTIz',
}
# Making an HTTP request through the SOCKS proxy
try:
    response = requests.get("http://visiontest.nethiwgan.vcngqsxe.oraclevcn.com:8000", headers=headers, timeout=5)
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
except requests.exceptions.RequestException as e:
    print("Error during request:", e)
socket.socket = original_socket
