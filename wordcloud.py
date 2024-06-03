import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
df = pd.read_excel("Resources/Online Retail - Cleaned.xlsx")
stop_words = ['union', 'jack', 'tin', '', 'white', 'small', 't', '', 'basil', 'rabbit']
text = ' '.join(df['Description'].str.lower())
wc = WordCloud(collocations=False, stopwords=stop_words, background_color='#fff0db').generate(text)
print(wc.words_.keys())
plt.figure(figsize=(10, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
