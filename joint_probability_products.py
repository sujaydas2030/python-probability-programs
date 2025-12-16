#Joint Probability of Product Preferences
# Libraries (do not edit)
from ast import literal_eval

def calculate_joint_probability(products_and_probabilities):
    # Your code here
    joint_probability= 1
    for product,probability in products_and_probabilities.items():
      joint_probability*=probability
    return joint_probability

# Input and output processing (do not edit)
print(round(calculate_joint_probability(literal_eval(input())), 4))
