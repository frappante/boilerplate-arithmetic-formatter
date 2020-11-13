def arithmetic_arranger(problems, tr = False):

# Maximum number of problems is 5
  if len(problems) > 5:
    return "Error: Too many problems."

  else: 

    ptop = ""
    pbottom = ""
    pline = ""
    ptotal = ""
    lp = len(problems) - 1
    space = "    "
    
    # Split problem into operands and operator
    for i,problem in enumerate(problems):
      n = problem.split()
      num1 = n[0] 
      op = n[1]
      num2 = n[2] 

      # Maximum number of digits is 4
      if (len(num1)>4 or len(num2)>4):
        return "Error: Numbers cannot be more than four digits."

      # Only integers are allowed
      if not (num1.isdecimal() and num2.isdecimal()):
        return "Error: Numbers must only contain digits."

      # Determine if addition or subtraction
      if op == "+":
        total = str(int(num1) + int(num2))
      elif op == "-":
        total = str(int(num1) - int(num2))
      else:
        return "Error: Operator must be '+' or '-'."


      # Set up output of all the rows
      plength = max(len(num1), len(num2)) + 2
      ptop += num1.rjust(plength)
      pbottom += op + num2.rjust(plength-1)
      pline += '-'*plength
      ptotal += total.rjust(plength) 

      # Adds 4 spaces between each problem, except for the last one
      if i < lp:
        ptop += space
        pbottom += space
        pline += space
        ptotal += space
      
      # Check if sum is requested
      if tr == True:
        arranged_problems = (ptop + "\n" + pbottom + "\n" + pline + "\n" + ptotal)
      else:
        arranged_problems = (ptop + "\n" + pbottom + "\n" + pline)

    return arranged_problems