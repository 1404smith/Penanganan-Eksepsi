def main():

    print("PROGRAM PEMBAGIAN BILANGAN"_
    
    try:
    
        a = float(input("Masukkan a: "))
        b = float(input("Masukkan b: "))
        
        hasil = a / b
    except ZeroDivisionError:
        print("\nERROR: Nilai b tidak boleh nol")
    except ValueError:
        print("\nERROR: a dan b harus berupa angka")
    except KeyboardInterrupt:
        print("\nERROR: Jangan tekan CTRL + C !")
    
    else:
        print("\na : ", a)
        print("b : ", b)
        print("a / b = ", hasil)
if __name__ == "__main__":
    main()
