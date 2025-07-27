import pandas as pd
history = pd.read_json("watch-history.json")
history = pd.DataFrame(history)

print(history.loc[19])