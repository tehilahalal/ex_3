def enumerate_parentheses(operands):
  if len(operands)==1:
    return operands
  elif len(operands)==2:
    return [operands]
    
  result = []
  
  for i in range(1,len(operands)):
    left= operands[:i]
    right= operands[i:]
    
    left_options = enumerate_parentheses(left)
    right_options = enumerate_parentheses(right)
    if isinstance(left_options, str):
            left_options = [left_options]
        if isinstance(right_options, str):
            right_options = [right_options]
          
    for l in left_options:
      for r in right_options:
        result.append([l,r])
