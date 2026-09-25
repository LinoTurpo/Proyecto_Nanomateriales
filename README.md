# Sistema de Litografía Láser de Bajo Costo para Investigación

## 📌 Problemática

En el Perú existe una carencia significativa de instrumentación especializada para procesos de **litografía láser** orientados a la investigación en ciencia de materiales y microfabricación. La ausencia de equipos accesibles limita:

- El desarrollo de líneas de investigación en microfabricación dentro de universidades y centros de investigación nacionales.
- La formación práctica de estudiantes e investigadores en procesos de fabricación a microescala.
- La dependencia tecnológica frente a la importación de equipos de litografía comerciales, cuyo costo es alto para la mayoría de laboratorios universitarios del país.

## 🎯 Objetivo

Desarrollar un sistema de litografía láser **accesible y especializado**, que permita realizar procesos de fabricación a microescala con un costo significativamente menor al de los equipos comerciales, sin sacrificar la precisión necesaria para aplicaciones de investigación.

### Objetivos específicos

- [ ] Diseñar la arquitectura óptica y mecánica del sistema (fuente láser, sistema de posicionamiento XY/XYZ, óptica de enfoque).
- [ ] Implementar el sistema de control (firmware/software) para la generación de patrones.
- [ ] Caracterizar la resolución espacial y repetibilidad del sistema.
- [ ] Validar el sistema mediante casos de prueba de fabricación real.
- [ ] Documentar el proceso completo para facilitar su réplica en otros laboratorios.

## 🔬 Aplicaciones

El sistema está orientado a la investigación en la fabricación de:

- **Microchips** — prototipado de circuitos integrados a escala de laboratorio.
- **Sensores** — fabricación de sensores basados en patrones microestructurados.
- **Semiconductores** — procesamiento de obleas para investigación en dispositivos semiconductores.
- **Circuitos** — fabricación de circuitos impresos y microcircuitos personalizados.
- Otros procesos de microfabricación que requieran patrones de alta resolución.

## 🧩 Marco conceptual

La litografía láser es un proceso de fabricación aditiva/sustractiva que utiliza un haz láser enfocado para transferir un patrón geométrico sobre un sustrato recubierto con material fotosensible (fotorresistencia). El sistema propuesto se basa en los principios de:

- **Óptica de formación de imagen** (enfoque, difracción, límite de resolución).
- **Sistemas de posicionamiento de precisión** (control de movimiento en ejes X-Y).
- **Fotolitografía directa (maskless lithography)**, evitando el uso de máscaras físicas costosas.

## 🛠️ Estructura del repositorio

```
├── hardware/         # Diseños CAD, esquemas ópticos y mecánicos
├── firmware/         # Código embebido para control del sistema
├── software/         # Software de generación y control de patrones
├── docs/             # Documentación técnica y de diseño
├── tests/            # Resultados de caracterización y pruebas
└── README.md
```

## 🚧 Estado del proyecto

> **Fase inicial / prueba de concepto.** Este repositorio parte de un prototipo rudimentario: el objetivo actual no es construir un instrumento de precisión terminado, sino sentar la primera piedra — validar el principio de funcionamiento con componentes básicos y accesibles, antes de iterar hacia versiones más precisas y robustas.

## 📚 Referencias y motivación técnica

Este proyecto se enmarca dentro de la necesidad de fortalecer capacidades locales de I+D en microfabricación, siguiendo el enfoque de instrumentación científica de bajo costo (*open-source scientific hardware*) que ha demostrado ser efectivo en otros contextos de investigación con recursos limitados.

## 👤 Autor

**Ingeniero Lino** — Ingeniería Física, Universidad Nacional de Ingeniería (UNI), Lima, Perú.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Ver el archivo [`LICENSE`](LICENSE) para más detalles.

