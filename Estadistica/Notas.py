from scipy import stats
# Datos de los dos métodos
T1 = [10,6,4,5,4]
T2 = [4,8,6,6,2,3]
# Realizar la prueba de Levene para la homogeneidad de varianzas
levene_stat, levene_p_value = stats.levene(T1, T2)

# Mostrar el resultado de la prueba
print("Estadístico de Levene:", levene_stat)
print("Valor p de la prueba de Levene:", levene_p_value)
t_stat, p_value = stats.ttest_ind(
    T1,
    T2,
    equal_var=False  # Welch
)

print("t (Welch):", t_stat)
print("p-valor (bilateral):", p_value)