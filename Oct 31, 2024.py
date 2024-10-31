'''
Number: 152
Tasks: You are given the following dataframe and are asked to categorize each food into
        1 of 3 categories: meat, fruit, or other. Given this, write code to add a new column categorizing each row.
'''

import pandas as pd
#Initial Data
data = {
    "food": ["bacon", "STRAWBERRIES", "Bacon", "STRAWBERRIES", "BACON", "strawberries", "Strawberries", "pecans"],
    "pounds": [4.0, 3.5, 7.0, 3.0, 6.0, 9.0, 1.0, 3.0]
}
df = pd.DataFrame(data)

#Mapping dictionary to categorize food
category_map= {
    "bacon": "meat",
    "strawberries": "fruit"
}
#Add new column 'category' with the mapped values, using 'others' as default category
df['category'] = df['food'].str.lower().map(category_map).fillna("other")

print(df)