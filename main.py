# brinchi topshiriq
raqam = int(input("raqamni kriing: "))

zadniy_raqam = raqam - 1
pereduyushi_raqam = raqam + 1

print(f"Ortdagi raqam: {zadniy_raqam}")
print(f"Kiritilgan raqam: {raqam}")
print(f"Keyingi raqam: {pereduyushi_raqam}")


# ikkinchi topshiriq
x = int(input("Son kriting: "))
raqamlar = [str(x * i) for i in range(1, 6)]
natija = " --- ".join(raqamlar)
print(natija)

# uchunchi topshiriq

santimetr = int(input("Santimetr sonini kiriting: "))

metr = santimetr / 100  
qolgan_santimetr = santimetr % 100 

print(f"{santimetr} sanitemtr teng {metr} metr va {qolgan_santimetr} santimetr.")

# turtinchi topshiriq
minut = int(input("Введите количество минут: "))
soat = minut / 60
qolgan_minut = minut % 60

print(f"{minut} minut teng {soat} soat va {qolgan_minut} minut.")

# beshinchi topshiriq
parol = input("Parolni krit: ")
parol_tasdiqlash = input("Parolni tasdiqlang: ")

if parol == parol_tasdiqlash:
    print("Parol to'g'ri")
else:
    print("parol xato")

#beshinchi

class Texnika:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
    def info(self)  :
        print(self.brand,self.model,self.type)

class Notebook(Texnika):
    def __init__(self,brand,model,type,vedio_card,ram,display):
        super().__init__(brand,model,type)
        self.vedio_card = vedio_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(self.brand,self.model,self.type,self.vedio_card,self.ram,self.display)


class Televizior(Texnika):
    def __init__(self, brand, model, type,size,display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display
    def more_info(self):
        print(self.brand,self.model,self.type,self.size,self.display)



class Telefon(Texnika):
    def __init__(self, brand, model, type,size,sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count
    def more_info(self):
        print(self.brand,self.model,self.type,self.size,self.sim_count)


s1 = Texnika('Apple','14pro max','smartphone')
s1.info()

s2 = Notebook('macbook','new_mac','notebook','124px','34px','none')
s2.more_info()
s3 = Televizior('LG', '65 dyum', 'OledTV', '127 sm','Oled')
s3.more_info()

