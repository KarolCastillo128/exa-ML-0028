import sys
import os
import io
import pandas as pd

print("Karol Castillo Machine Learning pandas, NC 0028")

# -------------------------------------------------------------------------
# 1. Configuración de Rutas e Importación del Módulo
# -------------------------------------------------------------------------
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Subir un nivel para acceder a 'datos-de-entrada-ml-0028'
ruta_datos_entrada = os.path.abspath(os.path.join(directorio_script, '..', 'datos-de-entrada-ml-0028'))

if ruta_datos_entrada not in sys.path:
    sys.path.append(ruta_datos_entrada)

try:
    import dicc_0028
except ModuleNotFoundError:
    ruta_alternativa = os.path.abspath(os.path.join(directorio_script, 'datos-de-entrada-ml-0028'))
    sys.path.append(ruta_alternativa)
    import dicc_0028

# -------------------------------------------------------------------------
# 2. Configuración del Reporte Markdown
# -------------------------------------------------------------------------
contenido_md = []
encabezado_pie = "Karol Castillo Machine Learning pandas, NC 0028"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# -------------------------------------------------------------------------
# 3. Obtención de Datos y Creación del DataFrame
# -------------------------------------------------------------------------
if hasattr(dicc_0028, 'datos_productos'):
    datos = dicc_0028.datos_productos
else:
    variables_disponibles = [
        attr for attr in dir(dicc_0028) 
        if not attr.startswith('__') and isinstance(getattr(dicc_0028, attr), (dict, list))
    ]
    
    if variables_disponibles:
        nombre_var = variables_disponibles[0]
        print(f"[Aviso] Usando la variable '{nombre_var}' de dicc_0028.py")
        datos = getattr(dicc_0028, nombre_var)
    else:
        print("\n[ERROR CRÍTICO] No se encontraron datos en dicc_0028.py")
        sys.exit(1)

df = pd.DataFrame(datos)

# Mapear nombres de columnas sin importar si están en mayúsculas o minúsculas
col_precio = next((col for col in df.columns if col.lower() == 'precio'), None)
col_stock = next((col for col in df.columns if col.lower() == 'stock'), None)

registrar("1. DataFrame Convertido", df)

# -------------------------------------------------------------------------
# 4. Análisis Exploratorio
# -------------------------------------------------------------------------
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3 y 4. Estadísticas y Orden por Precio
if col_precio:
    registrar(f"3. Estadísticas Generales de la Columna '{col_precio}'", df[col_precio].describe())
    df_asc_precio = df.sort_values(by=col_precio, ascending=True)
    registrar(f"4. Ordenar Ascendente por {col_precio}", df_asc_precio)
else:
    print(f"\n[Aviso] No se encontró columna de precio. Columnas disponibles: {list(df.columns)}")

# 5. Ordenar por Stock
if col_stock:
    df_desc_stock = df.sort_values(by=col_stock, ascending=False)
    registrar(f"5. Ordenar Descendente por {col_stock}", df_desc_stock)
else:
    print(f"\n[Aviso] No se encontró columna de stock. Columnas disponibles: {list(df.columns)}")

# -------------------------------------------------------------------------
# 5. Guardado del Archivo Markdown
# -------------------------------------------------------------------------
carpeta_resultados = os.path.abspath(os.path.join(directorio_script, '..', 'resultados-0028'))
os.makedirs(carpeta_resultados, exist_ok=True)

ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0028.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Karol Castillo Machine Learning pandas, NC 0028")