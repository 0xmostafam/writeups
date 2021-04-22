# Parcel

---

## Description

That's a lot of magick

---

## Solution

lets first use file to identify the file that we downloaded and rename it

```bash
$  file Parcel
Parcel: gzip compressed data, from Unix, original size modulo 2^32 759456
$  mv Parcel Parcel.gz
renamed 'Parcel' -> 'Parcel.gz'
$  gzip -d Parcel.gz 
```

after extracting it looks like a large file full of base64 images due to my lack of skills i have to do it manually so these images are the ones i extracted from the file

![img](https://cdn.discordapp.com/attachments/700342408411480214/830173245470408754/aKFWvXxj0DAAAAAAD2bU64AwAAAABAAII7AAAAAAAEILgDAAAAAEAAgjsAAAAAAAQguAMAAAAAQACCOwAAAAAABCC4AwAAAABAAI.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830173368342151198/uGsj1OvAGioino2u6d5SellA48cfEXqLQA0Bvn33ffmm8uWpZ4BAAAAAAANmyfcAQAAAAAggOAOAAAAAAABBHcAAAAAAAgguAMAA.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830173512094187590/8P8lqD9AT5oIFAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTA0LTA5VDE4OjU2OjAzKzAwOjAwpQr1jQAAACV0RVh0ZGF0ZTptb2R.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830173632083787816/V6BcQAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDQtMDlUMTg6NTY6MDMrMDA6MDClCvWNAAAAJXRFWHRkYXRlOm1vZGlmeQAyMD.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830173729005764638/H7yZHaZo765AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTA0LTA5VDE4OjU2OjAzKzAwOjAwpQr1jQAAACV0RVh0ZGF0ZTptb2RpZ.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830173846325035089/A1Pzg6pnEO1AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTA0LTA5VDE4OjU2OjAzKzAwOjAwpQr1jQAAACV0RVh0ZGF0ZTptb2RpZ.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830174049166164028/xEu07pyqRMBsAtzQLttpmar5R51FgAazFYPc0ZrSYdOa9T3GJTUif7hDRnFDHcWCvtANBJetmL8c8oDdRZAtlI3a2dv5VPL5003T.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830174157114441788/nWtwAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDQtMDlUMTg6NTY6MDMrMDA6MDClCvWNAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDI.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830174248952660009/fK5rKo8Kz4YAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDQtMDlUMTg6NTY6MDMrMDA6MDClCvWNAAAAJXRFWHRkYXRlOm1vZGlm.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830180607908773948/h9PXvc0TCKP9AAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMS0wNC0wOVQxODo1NjowMyswMDowMKUK9Y0AAAAldEVYdGRhdGU6bW9ka.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830180735260033074/68LWJHtfl8r7B7RhAs0QwhSJAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTA0LTA5VDE4OjU2OjAzKzAwOjAwpQr1jQAAACV0RVh0.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830180796395421776/hjePKUh46M8AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDQtMDlUMTg6NTY6MDMrMDA6MDClCvWNAAAAJXRFWHRkYXRlOm1vZGlm.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830180879211954236/9wX49yw6bF3n5hx8CtH1DiqbuzfY4A4BHcAAAAAAAggHXsAAAAAAACUBII7AAAAAAAEILgDAAAAAEAAgjsAAAAAAAQguAMAAAAAQ.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830181022749556776/lulR1aYXWGt7pAWAweEzz2OhRPO3tJ9Yu1aRb4A7F5EwjZDQUV1tAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTA0LTA5VDE4OjU2.png)

![img](https://cdn.discordapp.com/attachments/700342408411480214/830181205801566208/KFwpciuA6AAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMS0wNC0wOVQxODo1NjowMyswMDowMKUK9Y0AAAAldEVYdGRhdGU6bW9kaWZ5.png)

after manually forming it together manually i got the flag

---

## Flag

RS{Im_doing_a_v1rtual_puzzl3}