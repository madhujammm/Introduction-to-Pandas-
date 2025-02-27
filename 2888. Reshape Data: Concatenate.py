
#m1
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.DataFrame(df1, columns=['student_id', 'name', 'age'])
    df2 = pd.DataFrame(df2, columns=['student_id', 'name', 'age'])
    frames = [df1,df2]
    return pd.concat(frames)

#m2
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)
