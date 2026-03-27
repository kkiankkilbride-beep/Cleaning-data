"""

this code will make it so everrything in association column is consistent
for example, everything that is either neutralyou or youneutral will become youneutral

CGSC3601

Kian Kilbride 101267969
Danielle Picozzi 101301843
Jose Rodriguez 101104860

"""

import pandas as pd

df = pd.read_csv('clean_RGs_CGSC3601.csv')

mapping = {'neutralyou': 'youneutral',
           'happyyou': 'youhappy',
           'neutralfriend': 'friendneutral',
           'happyfriend': 'friendhappy'
           }

df['Association'] = df['Association'].replace(mapping)

df.to_csv('standardized_clean_RGs_CGSC3601.csv', index=False)

print("File saved as 'standardized_clean_RGs_CGSC3601.csv'")