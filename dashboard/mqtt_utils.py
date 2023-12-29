import paho.mqtt.client as mqtt
import ssl
from dashboard.models import MQTTData
import paho.mqtt.subscribe as subscribe

def publish_to_hivemq(topic, message):
    # Buat klien MQTT
    client = mqtt.Client()

    # Konfigurasi TLS jika diperlukan (pastikan Anda memiliki sertifikat TLS)
    sslContext = ssl.create_default_context()
    client.tls_set_context(sslContext)

    # Konfigurasi otentikasi jika diperlukan (ganti dengan informasi otentikasi Anda)
    client.username_pw_set(username='RamaPMPD', password='Kerasakti123')

    # Hubungkan ke broker HiveMQ (ganti dengan alamat host dan port HiveMQ yang sesuai)
    client.connect('b5208bedc9794c2397ead6f7870bb494.s1.eu.hivemq.cloud', port=8883)

    # Publish pesan ke topik tertentu
    client.publish(topic, message)

    # Menunggu pesan diproses dan kemudian menutup koneksi dengan broker
    client.loop_start()

def save_to_database(payload):
    data = payload.split(' ')
    mqtt_data = MQTTData(
            temperature=data[0],
            current=data[1],
            vibration=data[2],
         )
    mqtt_data.save()

def subs_baru():
    username = "RamaPMPD"
    password = "Kerasakti123"
    host = "b5208bedc9794c2397ead6f7870bb494.s1.eu.hivemq.cloud"
    port = 8883
    topic = "dataSensor"
    msg = subscribe.simple(
        topic,
        hostname=host,
        port=port,
        auth={"username": username, "password": password},
        tls={"ca_certs": None, "certfile": None, "keyfile": None},
    )
    print(msg.payload.decode())
    save_to_database(payload=msg.payload.decode())