import socket
import time
import threading
from datetime import datetime
print("Script by rill_hv")
print("Discord server: https://discord.gg/MeHNCayCmu")

# Autor keys
key_bot_1 = key_1
key_bot_2 = key_2
key_bot_3 = key_3
key_bot_4 = key_4
key_bot_5 = key_5
key_bot_6 = key_6

# Socket setup for connection
HOST = hostServer
PORT = int(portServer)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function send messages to Discord via webhook
def send_report_to_webhook(webhook_url, message):
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    embed = {
        "embeds": [
            {
                "title": "Script By rill_hv",
                "description": f"**Tittle: {Tittle}**\n<:chat1:1080231176658243674>**|Pesan: {message}**\n<a:ceklis:940153225166856233>**|Status: Terkirim**",
                "color": 0x03b2f8,
                "author": {
                    "name": "[Sytem] AUTO SEND LOGS",
                    "url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRdglAS7d9GYDXsTkkRguKXyVoCZjM3-vL35sPVlra1iRRC0i2OR1CqVhI9jqyY9ri_i8Hq"
                },
                "footer": {
                    "text": "Times",
                    "url": "https://www.google.com/"
                },
                "timestamp": timestamp,
                "image": {
                    "url": "https://media.discordapp.net/attachments/1224687667338547310/1224689594046349386/standard_5.gif"
                }
            }
        ]
    }
    res = requests.post(webhook_url, json=embed)
    if res.status_code == 204:
        pass
    elif res.status_code != 429:
        print(f"Gagal mengirim pesan. Kode status: {res.status_code}")  # Tidak mencetak 429

# Function send message with delay
def send_message_with_delay(url, payload, headers, delay, webhook_url):
    time.sleep(delay)
    res = requests.post(url, json=payload, headers=headers)
    
    if res.status_code == 200 or res.status_code == 201:
        message = f"Pesan berhasil dikirim: {payload['content']}"
    elif res.status_code == 204:
        message = f"Pesan berhasil dikirim melalui webhook (status 204)."
    elif res.status_code == 429:
        # Jangan mencetak untuk status 429
        message = "Terlalu banyak permintaan. Cobalah lagi nanti."
    else:
        message = f"Gagal mengirim pesan. Kode status: {res.status_code}"
    
    send_report_to_webhook(webhook_url, message)

# Function for socket communication
def socket_communication():
    # Connect to pp.py server
    sock.connect((HOST, PORT))
    sock.sendall(b"Name: " + Tittle.encode())

    try:
        while True:
            time.sleep(5)
    finally:
        sock.close()

# Start sending messages in threads
def send_messages():
    delay_msg_seconds = (delay_bot_msg_jam * 3600) + (delay_bot_msg_menit * 60) + delay_bot_msg_detik
    thread_1 = threading.Thread(target=send_message_with_delay, args=(f"https://discord.com/api/v9/channels/{Channel}/messages", {"content": msg_bot_1}, {"Authorization": key_bot_1}, delay_msg_seconds, webhook_url))
    thread_2 = threading.Thread(target=send_message_with_delay, args=(f"https://discord.com/api/v9/channels/{Channel}/messages", {"content": msg_bot_2}, {"Authorization": key_bot_2}, delay_msg_seconds, webhook_url))
    thread_3 = threading.Thread(target=send_message_with_delay, args=(f"https://discord.com/api/v9/channels/{Channel}/messages", {"content": msg_bot_3}, {"Authorization": key_bot_3}, delay_msg_seconds, webhook_url))
    thread_4 = threading.Thread(target=send_message_with_delay, args=(f"https://discord.com/api/v9/channels/{Channel}/messages", {"content": msg_bot_4}, {"Authorization": key_bot_4}, delay_msg_seconds, webhook_url))
    thread_5 = threading.Thread(target=send_message_with_delay, args=(f"https://discord.com/api/v9/channels/{Channel}/messages", {"content": msg_bot_5}, {"Authorization": key_bot_5}, delay_msg_seconds, webhook_url))
    thread_6 = threading.Thread(target=send_message_with_delay, args=(f"https://discord.com/api/v9/channels/{Channel}/messages", {"content": msg_bot_6}, {"Authorization": key_bot_6}, delay_msg_seconds, webhook_url))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()
    thread_6.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()
    thread_6.join()

# Main loop
def main():
    socket_thread = threading.Thread(target=socket_communication)
    socket_thread.start()
    while True:
        send_messages()

if __name__ == "__main__":
    main()
