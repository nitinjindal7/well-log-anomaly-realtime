import pandas as pd, time
def stream_rows(path, delay=0.5):
    df = pd.read_csv(path)
    i = 0
    while True:
        yield pd.DataFrame([df.iloc[i % len(df)]])
        i += 1
        time.sleep(delay)
