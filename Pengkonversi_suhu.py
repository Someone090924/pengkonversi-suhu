import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def main():
    while True:
        clear_terminal()
        print("Pilih konversi suhu:")
        print("a: Celsius ke Fahrenheit")
        print("b: Fahrenheit ke Celsius")
        print("c: Celsius ke Kelvin")
        print("d: Kelvin ke Celsius")
        print("e: Keluar")
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "a":
            clear_terminal()
            celsius_input = float(input("Masukkan suhu dalam Celsius: "))
            fahrenheit_result = celsius_to_fahrenheit(celsius_input)
            print("Suhu dalam Fahrenheit:", fahrenheit_result , "°F")
        elif pilihan == "b":
            clear_terminal()
            fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit: "))
            celsius_result = fahrenheit_to_celsius(fahrenheit_input)
            print("Suhu dalam Celsius:", celsius_result , "°C")
        elif pilihan == "c":
            clear_terminal()
            celsius_input = float(input("Masukkan suhu dalam Celsius: "))
            kelvin_result = celsius_to_kelvin(celsius_input)
            print("Suhu dalam Kelvin:", kelvin_result , "K")
        elif pilihan == "d":
            clear_terminal()
            kelvin_input = float(input("Masukkan suhu dalam Kelvin: "))
            celsius_result = kelvin_to_celsius(kelvin_input)
            print("Suhu dalam Celsius:", celsius_result , "°C")
        elif pilihan == "e":
            clear_terminal()
            print("Terima kasih telah menggunakan konverter suhu!")
            break
        else:
            print("INPUT TIDAK VALID")

        ulangi = input("Ingin mengonversi lagi? (y/n): ")
        if ulangi.lower() != "y":
            print("Terima kasih telah menggunakan konverter suhu!")
            break

main()
