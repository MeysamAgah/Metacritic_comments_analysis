import pandas as pd
from langdetect import detect

def clean_data(df,
               dropna=True, # remove any row with missing values in any column
               drop_duplicated=True,
               remove_spoiler=True, # remove comments containing spoiler
               all_languages=False, # will hold all comments in any language
               selected_languages=['en']): #list of selected languages
    """
    arguments:
      df: dataframe of reviews.

    output:
      cleaned df
    """
    # drop missing values
    if dropna:
      df = df.dropna()
    
    # drop duplicated
    if drop_duplicated:
      df = df.drop_duplicates()
    
    # Remove spoiler alert notices
    if remove_spoiler:
      df = df[df['review_text'] != "[SPOILER ALERT: This review contains spoilers.]"]

    if all_languages:
      pass
    else:   
      # Remove non-English comments
      langs = []
      for r in df['review_text']:
        try:
          langs.append(detect(r))
        except:
          langs.append('unknown')
      df['language'] = langs
      df = df[df['language'] == 'en']

    # removing language column in case there is all or only one language (not necessary in this case)
    if len(selected_languages) <= 1:
      df.drop(columns=['language'], inplace=True)

    return df
