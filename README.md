# Metacritic_comments_analysis
This projects involve extracting user and critic reviews and determining pros and cons of each game according to these reviews<br>
Project involves multiple steps:<br>
1. extract comments and form up a well structured dataset usilizing web scrapping methods. resulted dataset must be in below shape:<br><br>

| id  | Game  |Reviewer  |Reviewer type | Date |  Review  | Score |
| ------------- | ------------- | ------------- |------------- | ------------- | ------------- | ------------- |
| review id  | name of game  | name of user or critic  | user or critic  |date review submitted  | text of review  | 1-10  |
| 569541  | Makimat  |user  | Dec 17, 2024  | After 550 hours i can say its the best videogame ever made. ️️️️️ So many ways to play it. | 10  |
<br>
2. use a pre-train model to extract aspects of each comment result in another dataset:<br><br>

| id  | Aspects  |
| ------------- | ------------- |
| review id  | Aspects  |
| 569541  | Long Gameplay:positive, Addictive:positive  |

<br><br>
3. Create two new datasets one represents pros and one represents cons:<br><br>

| id  | Pros  |
| ------------- | ------------- |
| review id  | Pros  |
| 569541  | Long Gameplay, Addictive |

<br><br>

| id  | Cons  |
| ------------- | ------------- |
| review id  | Cons  |
| 569541  | |

<br><br>
4. by counting number of occurance of each aspect we create two diagrams representing aspects and number of ocurances
