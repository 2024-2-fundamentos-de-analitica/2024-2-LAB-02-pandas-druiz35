"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
from pathlib import Path

# Path files
tbl0 = pd.read_csv(Path(__file__).resolve().parents[1].joinpath("./files/input/tbl0.tsv"), sep='\t')
tbl1 = pd.read_csv(Path(__file__).resolve().parents[1].joinpath("./files/input/tbl1.tsv"), sep='\t')
tbl2 = pd.read_csv(Path(__file__).resolve().parents[1].joinpath("./files/input/tbl2.tsv"), sep='\t')



def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    merged_table = pd.merge(tbl0, tbl1, on="c0")[["c0", "c4"]]
    agg_funct = lambda x: str(sorted(list(x))).replace("'", "").replace(", ", ",").replace("[", "").replace("]", "")
    return merged_table.groupby("c0").agg(agg_funct).reset_index()