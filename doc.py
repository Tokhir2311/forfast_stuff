'''
BIz birinchi navbatda requests kutubxonasini o`rnatib olamiz 
Globall ga . keyin jsonplaceholder ga request jo`natishni boshlaymiz.
Avvval response degan o`zgaruvchi ochib olamiz keyin uni 
requests.something  ga tenglashtiramiz. SOMETHING o`rnida command keladi
get, post va x.k   
print(response[varaiable]) orqali natijani olishimiz
.json() orqali json farmatni jamda .status_code orqali 
response code ni qo`lga kiritishimiz mumkin.


Keyingi qadamda aynan post lar orasidan
id si 1 ga teng bo`lgan postni .json() yordamida 
json formatda oldik.

endi esa shu url dagi postlar orasidan id si 
1 ga teng bo`lgan postning commentlarini 
chiqarib oldik, status code esa 200 yani success



yangi command post . bu yangi data qo`shish uchun ishlatiladi. syntax i 
o`zgaruvchi = requests.post(url = manzil, json = data) 
agar muvaffaqiyatli data qo`shilsa print(o`zgaruvchi.json()) 
orqali 201 ko`ramiz.


put command i . buni postdan farqi bor narsani o`zgartirish.
syntax post bilan birxil, status code esa 200 kelarkan.


patchni yurgizganda farqni sezmadim.
taxminan data hajmi ga bog`liq katta - put, kichik specific - patch


delete command. bu data ni o`chirish uchun ishlatilinadi. json()
formatida narsa qaytmaydi. successfull o`chirilishning status kodi 204
syntaxi o`zgaruvchi = requests.delete(url="link address")
print(o`zgaruvchi.status_code)


'''