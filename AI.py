# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pt = plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
df = pd.read_csv("imdb_top_1000.csv")
#print("Lütfen IMDB puan sıralaması için deger girin.")

#IMDB Puanına göre filtreleme yapmak için kullanılır.

# value = input()
# value2 = int(input())
# filters = df.query("IMDB_Rating >" + value)
# df_filter = df[df["IMDB_Rating"] > value2]

# print(filters, df_filter)
# print(pt)

#Kendi oluşturduğum grafik.
plt.plot(label="x^2", color="red")
plt.xticks([1, 2, 3, 4])  #küsüratlarıda gösterebilir
plt.yticks([1, 4, 9, 16])
plt.title("ilk grafik")
plt.xlabel("x axix")
plt.ylabel("y axix")

#ikinci grafik çizgisi

x2 = np.arange(0, 5, 0.5)
plt.plot(x2, x2*2, color='red', linestyle="--", marker=".")
plt.legend(["This is my legend"], fontsize="large")
# plt.savefig("first graphic", dpi=300) # Oluşturulan grafiğin kaydedilmesini sağlar.
#plt.show() #Kullanılacağı zaman açılır

#Petrol fiyatlarını okuyup grafiğe çeviriyoruz.

gas = pd.read_csv("petrolfiyatlari.csv")
plt.figure(figsize=(9, 4))
plt.title("Petrol Fiyatları")
plt.plot(gas.Year, gas['USA'], 'b-', label='USA')
plt.plot(gas.Year, gas['Canada'], 'r-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='Korea')
plt.plot(gas.Year, gas['France'], 'y.-', label='France')
plt.plot(gas.Year, gas.Germany, color='purple', label='Germany')

plt.xlabel('Yıl')
plt.ylabel('Dolar')
plt.legend()
# plt.show() #Kullanılacağı zaman açılır

### NUMPY LİBARY ###

array1 = np.array([1, 3, 5])
array2 = np.array([5, 8, 11])
array2d = np.array([[1, 5, 9], [5, 8, 9]]) # 2 Boyutlu dizi

#Dosyadan sizi okumak için kullanılır.
filedata = np.genfromtxt('Dizi Örnekleri.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)