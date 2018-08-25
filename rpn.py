#!/usr/bin/python

input_string = raw_input("Please enter an expression in Reverse Polish Notation and I will evaluate it: ")

operators = {
  "+" : (lambda a, b : a + b),
  "-" : (lambda a, b: a - b),
  "/" : (lambda a, b: a / b),
  "*" : (lambda a, b: a * b),
  "x" : (lambda a, b: a * b)
}

def eval_rpn(expression):
  """ Calculate a Reverse Polish Notation sequence """
  stack = []

  for token in expression.split(' '):
    if token in operators:
      # pull off the last 2 entries on the stack
      num2 = stack.pop()
      num1 = stack.pop()
      # do the requested operation on them
      result = operators[token](num1,num2)
      # push the result back onto the stack
      stack.append(result) 
    else:
      # if it's not an operator, push it onto the stock for later processing
      stack.append(int(token))

  return stack.pop()

print(eval_rpn(input_string))
