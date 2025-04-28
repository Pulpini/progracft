# Calcular ml caídos por los 7 días de la semana
# Debe constar de valores de 0ml a 30ml
# Debe calcular ademas promedio de ml por semana
# Informal cuantos días hubo 25 ml
# Cuantos dias superaron el promedio de la semana

ml = list(range(0,31))
Dias = 7  
import random  
mll = random.sample(ml, Dias)  
print("ml caídos por los 7 días de la semana:", mll)
promedio = sum(mll) / Dias
print("Promedio de ml por semana:", promedio)
dias_25_ml = ml.count(25)
print("Días con 25 ml:", dias_25_ml)
dias_superaron_promedio = sum(1 for m in mll if m > promedio)
print("Días que superaron el promedio:", dias_superaron_promedio)