import pandas as pd
import matplotlib.pyplot as plt

# Datos
data = {
    "Año": [
        1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
        2020, 2021, 2022, 2023, 2024
    ],
    "Temperatura": [
        0.27, 0.33, 0.14, 0.31, 0.16, 0.12, 0.19, 0.33, 0.40, 0.29,
        0.44, 0.41, 0.23, 0.24, 0.32, 0.45, 0.33, 0.48, 0.63, 0.40,
        0.42, 0.54, 0.63, 0.62, 0.54, 0.67, 0.61, 0.61, 0.53, 0.64,
        0.72, 0.61, 0.64, 0.67, 0.74, 0.87, 0.99, 0.91, 0.85, 0.98,
        1.02, 0.85, 0.89, 1.14, 1.20
    ]
}
df = pd.DataFrame(data)

# Gráfico
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_facecolor("#E5F7F5")  # Fondo celeste claro

# Título
ax.set_title("El Reloj Climático Avanza (1980–2024)", fontsize=18, fontweight="bold", color="#67000d")

# Ejes
ax.set_xticks(range(1980, 2026, 4))  # Cada 4 años
ax.set_xlim(1980, 2025)  # Mostrar hasta 2025
ax.set_xlabel("Año", fontsize=12, fontweight="bold")
ax.set_ylabel("Anomalía de temperatura (°C)", fontsize=12, fontweight="bold")
ax.set_ylim(0, 2)  # Escala Y hasta 2°C

# Margenes
plt.margins(0)

# Grilla segmentada
ax.grid(True, color="grey", linestyle="--", linewidth=0.6, alpha=0.7)


# Línea principal
ax.plot(df["Año"], df["Temperatura"], marker="o", color="#ff0404", linewidth=2.5,
        label="Anomalía de temperatura", zorder=3)

# Últimos 4 años
ax.plot(df["Año"][-5:], df["Temperatura"][-5:], marker="o", color="#3d0400", linewidth=3,
        label=f"Últimos 4 años (Máx: {df['Temperatura'].max():.2f} °C en {df['Año'][df['Temperatura'].idxmax()]})",
        zorder=4)

# Valores en cada punto
for i in range(len(df)):
    ax.text(df["Año"][i], df["Temperatura"][i] + 0.03, f"{df['Temperatura'][i]:.2f}",
            ha='center', fontsize=8, color="black", zorder=5)

# Área sombreada debajo de la curva
ax.fill_between(df["Año"], df["Temperatura"], 0, color="orange", alpha=0.5, zorder=1)

# Línea horizontal en 1.5°C (grado de no retorno) con leyenda
ax.axhline(1.5, color="red", linestyle="--", linewidth=2, zorder=1,
           label="Punto de no retorno (1.5°C)")

# Leyenda
ax.legend(frameon=True, fancybox=True, shadow=True)

# Ajustar y mostrar
plt.tight_layout()
plt.show()
