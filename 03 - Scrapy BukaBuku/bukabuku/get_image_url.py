import pandas as pd

df = pd.read_csv('bukabuku.csv')

df_image = df['image_url']

df_image = df_image.to_csv('bukabuku_image_url.csv', index=False)