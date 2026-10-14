# Reporte de Análisis de Datos - Pandas

`Karol Castillo Machine Learning pandas, NC 0028`

## 1. DataFrame Convertido
```text
        Pais       Capital  Poblacion
0     México          CDMX  128000000
1     España        Madrid   47000000
2  Argentina  Buenos Aires   45000000
3   Colombia        Bogotá   51000000
4      Chile      Santiago   19000000
5       Perú          Lima   33000000
```

## 2.1 Primeras Filas (head)
```text
     Pais Capital  Poblacion
0  México    CDMX  128000000
1  España  Madrid   47000000
```

## 2.2 Últimas Filas (tail)
```text
    Pais   Capital  Poblacion
4  Chile  Santiago   19000000
5   Perú      Lima   33000000
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Pais           str
Capital        str
Poblacion    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Pais       6 non-null      str  
 1   Capital    6 non-null      str  
 2   Poblacion  6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

`Karol Castillo Machine Learning pandas, NC 0028`