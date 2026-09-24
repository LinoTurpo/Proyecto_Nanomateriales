[README.md](https://github.com/user-attachments/files/32589856/README.md)
# Proyecto_Nanomateriales# Simulación Óptica de Litografía — Modelo de Difracción

Modelo computacional en C/C++ para calcular patrones de intensidad de luz generados por difracción, aplicado al proceso de litografía óptica.

## Descripción

Este proyecto implementa un modelo de propagación de luz basado en la teoría de difracción de **Fresnel/Fraunhofer** (ajustar según el régimen que uses), con el objetivo de predecir el patrón de intensidad luminosa que incide sobre el sustrato (fotorresistente) a partir de una máscara o abertura definida.

El marco teórico central es el **principio de Huygens-Fresnel**, según el cual cada punto de un frente de onda actúa como fuente secundaria de ondículas esféricas; la superposición coherente de estas ondículas en el plano de observación determina el patrón de difracción resultante.

## Fundamento físico

- **Ecuación de difracción de Fresnel** (campo cercano) o **Fraunhofer** (campo lejano) — especificar cuál usa el modelo.
- Parámetros físicos relevantes:
  - Longitud de onda (λ) de la fuente de iluminación
  - Distancia máscara–sustrato (z)
  - Geometría de la abertura/máscara
  - Índice de refracción del medio (si aplica)

> Ajusta esta sección con la formulación matemática exacta (integral de difracción, aproximaciones usadas, condiciones de contorno) que implementaste.

## Estructura del proyecto

```
proyecto-litografia/
├── src/            # Código fuente (.c / .cpp)
├── include/         # Headers (.h / .hpp)
├── data/            # Máscaras/patrones de entrada
├── output/          # Resultados de simulación (patrones de intensidad)
├── Makefile
└── README.md
```

> Ajusta este árbol a la estructura real de tu repositorio.

## Requisitos

- Compilador compatible con C/C++11 o superior (GCC, Clang, MSVC)
- `make` (opcional, si usas Makefile)
- Librerías externas: *(especificar, p. ej. FFTW para transformadas de Fourier, si aplica)*

## Instalación y compilación

```bash
git clone https://github.com/tu-usuario/proyecto-litografia.git
cd proyecto-litografia
make
```

O compilación manual:

```bash
g++ -std=c++17 -O2 src/*.cpp -o simulacion
```

## Uso

```bash
./simulacion --mascara data/patron.txt --lambda 405e-9 --distancia 0.01
```

| Parámetro | Descripción | Unidad |
|---|---|---|
| `--mascara` | Archivo con la geometría de la abertura | — |
| `--lambda` | Longitud de onda de la fuente | metros |
| `--distancia` | Distancia máscara–sustrato | metros |

> Reemplaza estos parámetros por los argumentos reales que acepta tu programa.

## Resultados

El programa genera un archivo con el patrón de intensidad `I(x, y)` en el plano del sustrato, que puede visualizarse con herramientas externas (Python/Matplotlib, MATLAB, etc.).

## Contribuir

1. Haz un fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcion`
3. Haz commit de tus cambios: `git commit -m "Agrega X"`
4. Sube la rama: `git push origin feature/nueva-funcion`
5. Abre un Pull Request

## Autor

Desarrollado por [tu nombre] — Ingeniería Física, UNI.

## Licencia

MIT (o la que corresponda a tu proyecto).
