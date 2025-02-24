import pandas as pd
#From typing import List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
        return pd.DataFrame(student_data, columns=['student_id', 'age'])
#df = createDataframe(student_data)
#print(df)
