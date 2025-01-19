# Module area
import requests  
import time
import threading  # Modul untuk multithreading
from datetime import datetime  # Untuk mendapatkan timestamp yang terbaru
# URL dan payload
url_1 = f"https://discord.com/api/v9/channels/{Channel}/messages"
payload_1 = {
    "content": msg_bot_1
}

payload_2 = {
    "content": msg_bot_2
}
payload_3 = {
    "content": msg_bot_3
}
payload_4 = {
    "content": msg_bot_4
}
payload_5 = {
    "content": msg_bot_5
}
payload_6 = {
    "content": msg_bot_6
}

# Header dengan dua Authorization berbeda untuk dua author yang berbeda
headers_1 = {
    "Authorization": key_bot_1
}

headers_2 = {
    "Authorization": key_bot_2
}
headers_3 = {
    "Authorization": key_bot_3
}
headers_4 = {
    "Authorization": key_bot_4
}
headers_5 = {
    "Authorization": key_bot_5
}
headers_6 = {
    "Authorization": key_bot_6
}

# Start awal
print("Script by rill_hv")
print("Discord server: https://discord.gg/MeHNCayCmu")
print(f"Tittle :  {Tittle}")

def send_report_to_webhook(webhook_url, message):
    # Mendapatkan timestamp saat ini
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Menyiapkan embed untuk webhook
    embed = {
        "embeds": [
            {
                "title": "Script By rill_hv",  # Judul embed
                "description": f"**Tittle: {Tittle}**\n<:chat1:1080231176658243674>**|Pesan: {message}**\n<a:ceklis:940153225166856233>**|Status: Terkirim**",  # Deskripsi embed
                "color": 0x03b2f8,  # Warna embed biru
                "author": {
                    "name": "[Sytem] AUTO SEND LOGS",  # Nama penulis embed
                    "url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRdglAS7d9GYDXsTkkRguKXyVoCZjM3-vL35sPVlra1iRRC0i2OR1CqVhI9jqyY9ri_i8Hq",
                    # "icon_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRdglAS7d9GYDXsTkkRguKXyVoCZjM3-vL35sPVlra1iRRC0i2OR1CqVhI9jqyY9ri_i8Hq"  # Icon penulis
                },
                "footer": {
                    "text": "Times",  # Teks footer
                    # "icon_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRdglAS7d9GYDXsTkkRguKXyVoCZjM3-vL35sPVlra1iRRC0i2OR1CqVhI9jqyY9ri_i8Hq",  # Ikon footer
                    "url": "https://www.google.com/"  # Link footer yang dapat diklik
                },
                "timestamp": timestamp,  # Timestamp yang diperbarui sesuai waktu pengiriman
                "image": {
                    "url": "https://media.discordapp.net/attachments/1224687667338547310/1224689594046349386/standard_5.gif?ex=664157d0&is=66400650&hm=da3f8715b1ed6a24e2aad577d7bb9f1abb52a4118129c662ba34fba41a8d8fe0&"  # Gambar dalam embed
                }
            }
        ]
    }
    res = requests.post(webhook_url, json=embed)

    if res.status_code == 204:
      pass
    else:
        print(f"Gagal mengirim pesan. Kode status: {res.status_code}")

# Fungsi untuk mengirim pesan ke URL dengan delay
def send_message_with_delay(url, payload, headers, delay, webhook_url):
    time.sleep(delay)  # Menunda eksekusi sesuai dengan delay yang diberikan
    res = requests.post(url, json=payload, headers=headers)
    
    # Membuat pesan laporan
    if res.status_code == 200 or res.status_code == 201:  # Status sukses untuk pengiriman pesan
        message = f"Pesan berhasil dikirim: {payload['content']}"
    elif res.status_code == 204:  # Untuk webhook, biasanya Discord mengembalikan 204 (No Content)
        message = f"Pesan berhasil dikirim melalui webhook (status 204)."
    else:
        message = f"Gagal mengirim pesan. Kode status: {res.status_code}"
    
    # Kirim laporan ke webhook
    send_report_to_webhook(webhook_url, message)

# Fungsi untuk mengirim pesan dari dua author secara bersamaan
def send_messages():
    # Mengonversi jam dan menit ke detik, kemudian menjumlahkan dengan detik
    delay_msg_seconds = (delay_bot_msg_jam * 3600) + (delay_bot_msg_menit * 60) + delay_bot_msg_detik
   

    # Membuat dua thread untuk mengirim pesan secara bersamaan
    # Membuat dua thread untuk mengirim pesan secara bersamaan
    thread_1 = threading.Thread(target=send_message_with_delay, args=(url_1, payload_1, headers_1, delay_msg_seconds, webhook_url))
    thread_2 = threading.Thread(target=send_message_with_delay, args=(url_1, payload_2, headers_2, delay_msg_seconds, webhook_url))
    thread_3 = threading.Thread(target=send_message_with_delay, args=(url_1, payload_3, headers_3, delay_msg_seconds, webhook_url))
    thread_4 = threading.Thread(target=send_message_with_delay, args=(url_1, payload_4, headers_4, delay_msg_seconds, webhook_url))
    thread_5 = threading.Thread(target=send_message_with_delay, args=(url_1, payload_5, headers_5, delay_msg_seconds, webhook_url))
    thread_6 = threading.Thread(target=send_message_with_delay, args=(url_1, payload_6, headers_6, delay_msg_seconds, webhook_url))

    # Memulai kedua thread
    thread_1.start()
    time.sleep(delay_msg_seconds)  
    thread_2.start()
    time.sleep(delay_msg_seconds)  # Delay setelah thread_1 dimulai
    thread_3.start()
    time.sleep(delay_msg_seconds)  # Delay setelah thread_1 dimulai
    thread_4.start()
    time.sleep(delay_msg_seconds)  # Delay setelah thread_1 dimulai
    thread_5.start()
    time.sleep(delay_msg_seconds)  # Delay setelah thread_1 dimulai
    thread_6.start()

    # Menunggu kedua thread selesai
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()
    thread_6.join()

# Loop utama untuk terus mengirim pesan
while True:
    send_messages()
    
