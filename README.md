# Metacritic_comments_analysis
This projects involve extracting user and critic reviews and determining pros and cons of each game according to these reviews<br>
Project involves multiple steps:<br>
1. Scrape Data from Metacritic website and form up a dataframe containing: <br>
- reviewr name<br>
- review text<br>
- rating score<br>
- review date<br>
- platform of reviewr<br>
2. Cleaning data:<br>
- removing null values
- removing duplicated values
- removing reviews containing spoiler
- filtering reviews to one or multiple languages
3. finding aspects of each review for aspect based sentiment analysis using PyABSA pre-trained model according to pre-determined aspects as inputs.
4. and finally present a diagram to show positive and negative sentiments for each defined aspect.
