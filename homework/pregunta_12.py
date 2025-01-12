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



def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    def combine_columns(col1, col2, df):
        response = []
        for i in range(df[col1].size):
            row_1 = df[col1][i]
            row_2 = df[col2][i]
            new_value_list = []
            for j in range(len(row_1)):
                val_1 = row_1[j]
                val_2 = row_2[j]
                new_val = val_1 + ":" + str(val_2)
                new_value_list.append(new_val)
            new_value_list.sort()
            new_value_list = str(new_value_list).replace(", ", ",").replace("[", "").replace("]", "").replace("'", "")
            response.append(new_value_list)
        return pd.Series(response)
    grouped_table = tbl2.groupby("c0").agg(lambda x: list(x)).reset_index()
    grouped_table["c5"] = combine_columns("c5a", "c5b", grouped_table)
    return grouped_table[["c0", "c5"]]