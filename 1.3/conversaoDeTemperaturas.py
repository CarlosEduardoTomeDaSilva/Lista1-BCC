C = float(input())

def celsiusToKelvin():
	return (C + 273.15)

def celsiusToFahrenheit():
	return 32 + 1.8 * C

print(int(celsiusToFahrenheit()), "F", int(celsiusToKelvin()), "K")