
import calculos as calc

primer_numero = 10
segundo_numero = 2

suma = calc.sumar(primer_numero, segundo_numero)
resta = calc.restar(primer_numero, segundo_numero)
multiplicación = calc.multiplicar(primer_numero, segundo_numero)
división = calc.dividir(primer_numero, segundo_numero)

print(f"El resultado de sumar", primer_numero,"y",segundo_numero,"es: ",suma)
print(f"El resultado de restar", primer_numero,"y",segundo_numero,"es: ",resta)
print(f"El resultado de multiplicar", primer_numero,"y",segundo_numero,"es: ",multiplicación)
print(f"El resultado de dividir", primer_numero,"y",segundo_numero,"es: ",división)