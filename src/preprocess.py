import pandas as pd
def load_logs(path):
    df = pd.read_csv(path)
    return df[['GR','RHOB','NPHI']].dropna().reset_index(drop=True)
