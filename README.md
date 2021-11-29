# get_post_server

jika ingin menjalankan di local bersamaan dengan menjalankan flutter, gunakan ipadress yang berbeda dengan `127.0.0.1`.

cara mengetahui ipaddress yang bisa dipakai selain `127.0.0.1`

1. buka terminal
2. ketik ipconfig lalu enter
3. usahakan anda terkoneksi internet atau WiFi (walau tanpa internet)
4. jika terhubung dengan WiFi lihat dibagian `Wireless LAN adapter WiFi`

```
...
Wireless LAN adapter WiFi:

Connection-specific DNS Suffix  . :
Link-local IPv6 Address . . . . . : fe80::7833:fca4:ea45:d0c%17
IPv4 Address. . . . . . . . . . . : 192.168.100.101
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 192.168.100.1
...
```

isi `IPv4 Addres` yaitu `192.168.100.101` ini bisa digunakan sebagai ipaddres pengganti `127.0.0.1`

5. jalankan server python dengan `py manage.py runserver 0.0.0.0:8000`
6. buka browser dengan url `http://<ipadaress>:8080` dengan `ipaddress` disesuaikan dengan computer masing-masing
7. jika berhasil maka tampilan awal dari django akan muncul
8. untuk melihat json yang dikirim, buka `http://<ipadaress>:8080/data/`



Silahkan ubah pada fungsi `index` di file `views.py`, sesuaikan dengan kebutuhan.


> Note : jika ada error saat menjalankan flutter dengan web browser, silahkan coba dengan menggunakan ponsel atau emulator
