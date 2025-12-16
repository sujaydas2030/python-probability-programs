#Books List Genres Distribution
def calculate_genre_probability(selected_genres):
    # Code here
  prob=0
  for i in range(len(selected_genres)):
    if selected_genres[i] in genre_distribution:
      prob+=genre_distribution[selected_genres[i]]
  return prob


# Input and output processing (do not edit)
from ast import literal_eval
genre_distribution = {'Drama': 0.30, 'Poetry': 0.25, 'Science': 0.15, 'History': 0.10, 'Fantasy': 0.05, 'Mystery': 0.05, 'Romance': 0.04, 'Thriller': 0.03, 'Biography': 0.02, 'Self-Help': 0.01}
print(round(calculate_genre_probability(literal_eval(input())), 4))
