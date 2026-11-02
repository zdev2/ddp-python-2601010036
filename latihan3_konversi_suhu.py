while True:
    try:
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        if celsius < -273.15:
            print("Suhu tidak boleh di bawah nol mutlak (-273.15 °C), coba lagi.")
            continue
        break
    except ValueError:
        print("Input harus berupa angka, coba lagi.")
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{fahrenheit:.2f} °F dan {kelvin:.2f} K")
