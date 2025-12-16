# Many-Sided Die and Many Rolls
# Libraries (do not edit)
from ast import literal_eval

def probability_of_outcome(num_sides, rolls, target_sum):
    # Write your code here
  set_of_outcomes=set(range(1,num_sides+1))
  total_roll_permutation=num_sides**rolls
  def correct_pair_finder(roll_left,current_sum):
    if roll_left==0:
      if current_sum==target_sum:
        return 1
      else:
        return 0
    counter=0 #how many times the sum of the rolls matches
    for outcome in set_of_outcomes:
      counter+=correct_pair_finder(roll_left-1,current_sum+outcome)
    return counter

  total_correct_pair=correct_pair_finder(rolls,0) #recursive function starts
  return total_correct_pair/total_roll_permutation

# Input and output processing (do not edit)
print(round(probability_of_outcome(*literal_eval(input())), 4))
