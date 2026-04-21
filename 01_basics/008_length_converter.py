#Exercise 008: Convert meters to other metric units (km to mm). 
# Concepts: Sequential calculations, unit conversion, formatted output. 
# Note: Precision varies: 3 decimals for km, 0 for cm/mm.

m = float(input("Digite uma distância em metros:"))

km = m / 1000
hm = m /100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f"The distance of {m}m corresponds to: \n {km:.3f} km \n {hm:.3f} hm \n {dam:.2f} dam \n {dm:.2f} dm \n {cm:.0f} cm \n {mm:.0f} mm")
