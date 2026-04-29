def  matrix_multiplication_cost_2(dimensions):
  if len(dimensions) !=3:
    raise ValueError("cant calaulate this")
  return dimensions[0]* dimensions[1]* dimensions[2]

def main():
  dimensions=[30, 35,15]
  cost=matrix_multiplication_cost_2(dimensions)
  print(F"cost of multiply tow metrix with dimensions {dimensions} is {cost})
  
  
