def OperationsBinaryString(str):
  operand1 = None
  operand2 = None
  result = None
  for char in str:
    if char in '01':
      operand2 = int(char)
      if operand1 is not None:
        # Perform operation based on previous operand
        if result is None:
          result = perform_operation(operand1, operand2, char)
        else:
          result = perform_operation(result, operand2, char)
        operand1 = None
    else:
      operand1 = operand2 if operand2 is not None else result
  return result if result is not None else operand2

def perform_operation(a, b, op):
  if op == 'A':
    return a & b
  elif op == 'B':
    return a | b
  else:
    return a ^ b

# Example usage
result = OperationsBinaryString("1C0C1C1A0B1")
print(result)
