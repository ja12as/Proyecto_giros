# Proyecto Giros

Este proyecto proporciona una API que facilita la conexión y análisis de los giros realizados por el Ministerio de Salud a sus prestadores por los conceptos de cápita y evento. Los datos se procesan, almacenan en una base de datos SQL, y se generan análisis con visualizaciones interactivas.

## Estructura del Proyecto

```bash
proyecto_giros/
│
├── api/
│   ├── __init__.py
│   ├── main.py            # Archivo principal para inicializar la API
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── giros.py       # Rutas relacionadas con los giros
│   │   ├── eps.py         # Rutas para EPS
│   │   └── ips.py         # Rutas para IPS
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py    # Configuración de la base de datos
│   │   ├── giros.py       # Modelo para los giros
│   │   ├── eps.py         # Modelo para EPS
│   │   └── ips.py         # Modelo para IPS
│   ├── services/
│       ├── __init__.py
│       ├── data_loader.py # Lógica de carga y normalización de datos
│       └── analytics.py   # Funciones para análisis de datos
│
├── data/
│   ├── raw/               # Archivos descargados sin procesar
│   ├── processed/         # Archivos normalizados o procesados
│   └── insights/          # Salidas de análisis como gráficos o reportes
│
├── notebooks/
│   ├── exploratory.ipynb  # Análisis exploratorio inicial
│   ├── cleaning.ipynb     # Limpieza de datos
│   └── analysis.ipynb     # Análisis y visualizaciones
│
├── sql/
│   ├── schema.sql         # Script de creación de tablas
│   ├── queries.sql        # Consultas útiles para análisis
│   └── seed.sql           # Datos de prueba o iniciales
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py        # Pruebas para la API
│   └── test_models.py     # Pruebas para los modelos
│
├── .env                   # Variables de entorno (credenciales)
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
└── .gitignore             # Archivos y carpetas a ignorar por Git
