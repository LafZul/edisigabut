import matplotlib.pyplot as plt
import pandas as pd
negara=input(str("Input nama Negara:  "))

x=[1]
y=[5]
I=5

data = pd.read_excel (r'C:/Users/IQBAL EUY/.PyCharmCE2018.2/config/scratches/qw.xls')
df = pd.DataFrame(data, columns= [negara])
df.values.tolist()
#print(df)

x = [1]

if (negara == 'Afganistan'):
    N = 38928346
    nhari = 300
    y = [4]
    I = 4
if (negara == 'Arab'):
    N = 34813871
    nhari = 302
    y = [5]
    I = 5
if (negara == 'Cina'):
    N = 1439323776
    nhari = 365
    y = [27]
    I = 27
if (negara == 'India'):
    N = 1380004385
    nhari = 307
    y = [3]
    I = 3
if (negara == 'Inggris'):
    N = 67886011
    nhari = 330
    y = [9]
    I = 9
if (negara == 'Itali'):
    N = 60461826
    nhari = 316
    y = [20]
    I = 20
if (negara == 'Singapura'):
    N = 5850342
    nhari = 345
    y = [1]
    I = 1
else:
    print("",end='')

data=(df[:nhari])
#print(data)

print('Separate2:  ',end="")
Separate2 =int(input())
print('Separate3:  ',end="")
Separate3=int(input())
print('Separate4:  ',end="")
Separate4=int(input())
print('Separate5:  ',end="")
Separate5=int(input())

print('R0_1:  ',end="")
R0_1 =float(input())
print('D_1:  ',end="")
D_1=float(input())

print('R0_2:  ',end="")
R0_2=float(input())
print('D_2:  ',end="")
D_2=float(input())

print('R0_3:  ',end="")
R0_3 =float(input())
print('D_3:  ',end="")
D_3=float(input())

print('R0_4:  ',end="")
R0_4=float(input())
print('D_4:  ',end="")
D_4=float(input())

print('R0_5:  ',end="")
R0_5=float(input())
print('D_5:  ',end="")
D_5=float(input())

for i in range (nhari - 1):
    if i <= Separate2: #prediksi pertama lu
        I =(R0_1 * N * I) / (N + (R0_1 - 1 + D_1) * I)
        I=round(I)
    if Separate2 < i <= Separate3: #prediksi kedua lu
        I = (R0_2 * N * I) / (N + (R0_2 - 1 + D_2) * I)
        I = round(I)
    if Separate3 < i <= Separate4: #prediksi ketiga lu
        I = (R0_3 * N * I) / (N + (R0_3 - 1 + D_3) * I)
        I = round(I)
    if Separate4 < i <= Separate5: #prediksi keempat lu
        I = (R0_4 * N * I) / (N + (R0_4 - 1 + D_4) * I)
        I = round(I)
    if Separate5 < i :  # prediksi kelima lu
        I = (R0_5 * N * I) / (N + (R0_5 - 1 + D_5) * I)
        I = round(I)
    else: #style gua ini mah jarang gunain else
        print("", end = '')

    x.append(i + 2)
    y.append(I)
    #print(I)
#print(df)
#print(x)
#print(y)
print (len(x))
print (len(y))
print(nhari)

plt.plot(x,data)
plt.plot(x,y)
plt.show()

