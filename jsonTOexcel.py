import json
import pandas as pd
file_json = ".json"
file_excel = ".xlsx"
with open ('' + file_json) as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data)

df.to_excel('' + file_excel)
