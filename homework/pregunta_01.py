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



def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    return tbl0.shape[0]