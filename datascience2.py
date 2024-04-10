# def main():

#     bahasa = ["Phyton","R studio","PHP","C++"]
#     for x in bahasa:
#         print(x)
        
# if __name__== "__main__":
#     main()

# def main():

#     bilangan = ["1","3","5","7","9"]
#     for x in bilangan:
#         print(x)
        
# if __name__== "__main__":
#     main()

def main():
    # var = input("Masukan variabel untuk menghitung volume balok:")
    # print("Variabel " +var+ "yang diperlukan untuk menghitung volume balok")
    # print(a)

    p = int(input('Masukan panjang balok:'))
    l = int(input('Masukan lebar balok:'))
    t = int(input('Masukan tinggi balok:'))

    vol= p*l*t
    print('volume balok:', vol)

if __name__=="__main__":
    main()

def main():
    phi = 3.14
    r = int(input('Masukan jari-jari kerucut:'))
    t = int(input('Masukan tinggi kerucut:'))

    v = 1/3*(phi*(r**2)*t)
    e = r**2
    print ('volume kerucut tersebut adalah:', v)
    print (e)

if __name__=="__main__":
    main()