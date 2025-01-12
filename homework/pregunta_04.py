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

def df_to_series(df):
    current_index = df.index
    new_response = []
    for i in range(df.shape[0]):
        new_response.append(df.iloc[i])
    return pd.Series(new_response, index=current_index, name="c2")

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    df = tbl0[["c1", "c2"]].groupby("c1").mean()
    response = df_to_series(df["c2"])
    return response