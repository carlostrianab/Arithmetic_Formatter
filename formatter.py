def arithmetic_arranger(problems):

  arranged_problems = ""
  
  #ERROR HANDLING
  #Limit is five equations.
  if len(problems) > 5:
    return "Error: Too many problems."

  for element in problems:
    num1 = element.split(' ')[0]
    num2 = element.split(' ')[2]
    operator = element.split(' ')[1]
    #Each number should only contain digits
    if num1.isnumeric() and num2.isnumeric() != True:
      return "Error: Numbers must only contain digits."
    #Each operand has a maximum of 4 digits.
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
      
  #FORMATTING
  #Align to the right depending on the largest numer in the equation 
  def rightAlign(num1,num2):
    rightAlign = 0 
    if len(num1) > len(num2):
      rightAlign = len(num1) + 2
    else:
      rightAlign = len(num2) + 2
    return rightAlign

  #Calculating the space needed between the operator and the operand
  def spacing(num1,num2,operator):
    space = ' '
    counter = 0
    if len(num1) > len(num2):
      difference = len(num1)-len(num2)
      while counter < difference:
        space += ' '
        counter = counter + 1 
    return space

  
  #First line with operard and right alignment 
  for element in problems:
    num1 = element.split(' ')[0]
    operator = element.split(' ')[1]
    num2 = element.split(' ')[2]

    arranged_problems += num1.rjust(rightAlign(num1,num2))
    arranged_problems += '    '
  arranged_problems = arranged_problems[0:len(arranged_problems)-4] 
  arranged_problems += '\n'
  
  #Second line with the operator, spacing and second operand. Also right alignment
  for element in problems: 
    num1 = element.split(' ')[0]
    operator = element.split(' ')[1]
    num2 = element.split(' ')[2]
    
    
    arranged_problems += (operator + spacing(num1,num2,operator) + num2).rjust(rightAlign(num1,num2))
    arranged_problems += '    '
    
  arranged_problems = arranged_problems[0:len(arranged_problems)-4]
  arranged_problems += '\n'

  #Third line with the dashes separating the equation 
  for element in problems:
    num1 = element.split(' ')[0]
    operator = element.split(' ')[1]
    num2 = element.split(' ')[2]
  
    
    #Calculating the number of dashes needed to separate the equation and its answer 
    lines = ''
    linesLength = len(operator) + len(spacing(num1,num2,operator)) + len(num2)
    lineCounter = 0 
    
    while lineCounter < linesLength:
      lines += '-'
      lineCounter = lineCounter + 1
      
    arranged_problems += lines
    arranged_problems += '    '
    
  arranged_problems = arranged_problems[0:len(arranged_problems)-4]
  arranged_problems += '\n'

  #Fourth line with the answers of the equation with right alignment 
  for element in problems:
    num1 = element.split(' ')[0]
    operator = element.split(' ')[1]
    num2 = element.split(' ')[2]

    answer = ''

    if operator == '+':
      answer = str(int(num1) + int(num2))
    else:
      answer = str(int(num1) - int(num2))
    
    arranged_problems += answer.rjust(rightAlign(num1,num2))
    arranged_problems += '    '

   
  return arranged_problems

#TESTING

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))