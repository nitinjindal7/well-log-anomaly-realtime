def add_flag(df, preds):
    df['anomaly'] = (preds == -1).astype(int)
    return df
