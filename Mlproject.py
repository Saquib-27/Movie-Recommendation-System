import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
 'movie_id': [1, 2, 3, 4, 5],
 'title': ['Inception', 'Interstellar', 'The Dark Knight', 'Avengers', 'Titanic'],
 'genre': ['Sci-Fi', 'Sci-Fi', 'Action', 'Action', 'Romance']
}

df = pd.DataFrame(movies)
cv = CountVectorizer()xm
count_matrix = cv.fit_transform(df['genre'])
cosine_sim = cosine_similarity(count_matrix)

def recommend(movie_title):
 idx = df[df['title'] == movie_title].index[0]
 scores = list(enumerate(cosine_sim[idx]))
 scores = sorted(scores, key=lambda x: x[1], reverse=True)
 recommended = [df.iloc[i[0]]['title'] for i in scores[1:4]]
 return recommended

print('Recommendations for Interstellar:')
print(recommend('Interstellar'))
print(recommend('Interstellar'))