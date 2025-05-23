# -*- coding: utf-8 -*-
"""gantt

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g0MKASgYC3mVDAUFkobkcMnouVhd9IVX
"""

import matplotlib.pyplot as plt

actividades = [
    "Reunión inicial y actas",
    "Especificación de requisitos",
    "Diseño de solución",
    "Registro de huéspedes",
    "Reservas y validaciones",
    "Check-out y facturación",
    "Administrador y reportes"
]


inicios = [0, 0, 1, 1, 2, 3, 4]

duraciones = [1, 2, 1, 2, 2, 2, 2]

fig, ax = plt.subplots(figsize=(10, 5))

for i, (inicio, duracion) in enumerate(zip(inicios, duraciones)):
    ax.barh(i, duracion, left=inicio, height=0.5, color='skyblue')

ax.set_yticks(range(len(actividades)))
ax.set_yticklabels(actividades)
ax.invert_yaxis()
ax.set_xlabel('Semana')
ax.set_title('Diagrama de Gantt - Actividades 1 a 7')

plt.tight_layout()
plt.savefig('gantt.png')