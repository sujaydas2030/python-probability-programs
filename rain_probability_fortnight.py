#Binomial Distribution formula
#Exact Rain Probability in a Fortnight
# Libraries (do not edit)
from ast import literal_eval
from math import factorial
# Function to calculate rain probability in a fortnight
def calculate_rain_probability_in_fortnight(n):
    # Write your code here
  single_day_probability_raining=0.3
  single_day_probability_not_raining=1-single_day_probability_raining
  total_trials=14
  desired_outcome=n
  result=(factorial(total_trials)/(factorial(total_trials-desired_outcome)*factorial(desired_outcome)))*(single_day_probability_raining**desired_outcome)*(single_day_probability_not_raining**(total_trials-desired_outcome))
  return result

# Input and output processing (do not edit

# Input and output processing (do not edit)
print(round(calculate_rain_probability_in_fortnight(literal_eval(input())), 4))
