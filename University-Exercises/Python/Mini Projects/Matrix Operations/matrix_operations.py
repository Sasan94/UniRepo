#This function uses the while loop to show an infinite loop to show the menu until the user chooses one of the options 
def menu():
   while True:
      print(f"\n========== Matrix Operations ==========")
      print(f"\n1.Matrix Multiplication")
      print(f"2.Matrix Addition")
      print(f"3.Matrix Subtraction")
      print(f"4.Exit The Program...")
      print("\n ")
      #Try to get difits from the user
      try:
         choice = int(input("Select one of the options above: "))
      except ValueError:
         print("Enter Digits Only")
         continue
      #If the user chooses one of the option the function applicable to the number will be executed
      if choice == 1:
         matrix_multiplication()
      elif choice == 2:
         matrix_addition()
      elif choice == 3:
         matrix_subtraction()
      elif choice == 4:
         print("Exiting The Program")
         exit()

#The aim of this function is Matrix Multiplication
def matrix_multiplication():
   try:
      #Take the rows and columns of Matrix A from the user
      rows_A = int(input("Type the rows of the desired Matrix 'A': "))
      cols_A = int(input("Type the columns of the desired Matrix 'A': "))
      #Take the rows and columns of Matrix B from the user
      rows_B = int(input("Type the rows of the desired Matrix 'B': "))
      cols_B = int(input("Type the columns of the desired Matrix 'B': "))
   except ValueError:
      print("Plase Enter Digits Only")
      return
   #Check if the multiplication is allowed
   while cols_A != rows_B:
     print("\n")
     print("The columns of Matrix A are not equal the rows of Matrix B ... Try again")
     try:
        #Try to take the rows and columns of Matrix A from the user
        rows_A = int(input("Type the rows of the desired Matrix 'A': "))
        cols_A = int(input("Type the columns of the desired Matrix 'A': "))
        #Try to take the rows and columns of Matrix B from the user
        rows_B = int(input("Type the rows of the desired Matrix 'B': "))
        cols_B = int(input("Type the columns of the desired Matrix 'B': "))
     except ValueError:
         print("Please Enter Digits Only")
         return
   print("\n")
   #Create Matrix A
   matrix_A = []  
   for i in range(1,rows_A+1):
     temp = []
     for j in range(1,cols_A+1):
       try:
          value = int(input(f"Type the scalars [{i}],[{j}] of Matrix A : "))
       except ValueError:
          print("Please Enter Digits Only")
          return
       temp.append(value)
     matrix_A.append(temp)
   print(f"\nMatrix 'A'")
   for row in matrix_A:
     print(f"{row}")
   print("\n")
   #Create Matrix B
   matrix_B = []
   for i in range(1,rows_B+1):
     temp = []
     for j in range(1,cols_B+1):
       try:
          value = int(input(f"Type the scalars [{i}],[{j}] of Matrix B: "))
       except ValueError:
          print("Please Enter Digits Only")
          return
       temp.append(value)
     matrix_B.append(temp)
   print(f"\nMatrix 'B'")
   for column in matrix_B:
     print(f"{column}")
   #Create an empty matrix named 'C' to save the result of multiplication
   C = []
   for i in range(rows_A):
     col = []
     for j in range(cols_B):
       col.append(0)
     C.append(col)
   #Matrix A multiplied by Matrix B and then save the result in the Matrix C
   for i in range(rows_A):
     for j in range(cols_B):
       for k in range(rows_B):#The rows in matrix B are equal to the columns in matrix A
         C[i][j] = C[i][j] + matrix_A[i][k] * matrix_B[k][j]
   #Show the result of the multiplication
   print("\nMatrix A multiplied by Matrix B")
   for row in C:
     print(f"{row}")

#The aim of this function is Matrix Addition
def matrix_addition():
   try:
      #Take the rows and columns of matrix A from the user
      rows_A = int(input("Type the rows of the desired Matrix 'A': "))
      cols_A = int(input("Type the columns of the desired Matrix 'A': "))
      #Take the rows and columns of matrix B from the user
      rows_B = int(input("Type the rows of the desired Matrix 'B': "))
      cols_B = int(input("Type the columns of the desired Matrix 'B': "))
   except ValueError:
      print("Please Enter Digits Only")
      return
   #Check if the addition is allowed
   while rows_A != rows_B and cols_A != cols_B:
     print("\nThe rows and columns of both matrices must be equal...Try again")
     try:
        #Try to take the rows and columns of matrix A from the user
        rows_A = int(input("Type the rows of the desired Matrix 'A': "))
        cols_A = int(input("Type the columns of the desired Matrix 'A': "))
        #Tr to take the rows and columns of matrix B from the user
        rows_B = int(input("Type the rows of the desired Matrix 'B': "))
        cols_B = int(input("Type the columns of the desired Matrix 'B': "))
     except ValueError:
         print("Please Enter Digits Only")
         return
   print("\n")
   #Create Matrix A
   matrix_A = []
   for i in range(1,rows_A+1):
     new_matrix_A = []
     for j in range(1,cols_A+1):
       try:
          value = int(input(f"Type the scalars [{i}],[{j}] : "))
       except ValueError:
          print("Please Enter Digits Only")
          return
       new_matrix_A.append(value)
     matrix_A.append(new_matrix_A)
   print(f"\nMatrix 'A'")
   for row in matrix_A:
     print(f"{row}")
   print("\n")
   #Create Matrix B
   matrix_B = []
   for i in range(1,rows_B+1):
     new_matrix_B = []
     for j in range(1,cols_B+1):
       try:
          value = int(input(f"Type the scalars [{i}],[{j}] : "))
       except ValueError:
          print("Please Enter Digits Only")
          return
       new_matrix_B.append(value)
     matrix_B.append(new_matrix_B)
   print(f"\nMatrix 'B'")
   for column in matrix_B:
     print(f"{column}")
   #Create an empty matrix named 'C' to save the result of addition
   C = []
   for i in range(rows_A):
     col = []
     for j in range(rows_B):
       col.append(0)
     C.append(col)
   #Adding the Matrix A to the Matrix B and then save the result in the Matrix C
   for i in range(rows_A):
     for j in range(rows_B):
             C[i][j] = C[i][j] + (matrix_A[i][j] + matrix_B[i][j])
   #Show the result of addition
   print("\nMatrix A added to the Matrix B")
   for row in C:
     print(f"{row}") 

#The aim of this function is Matrix Subtraction 
def matrix_subtraction():
   try:
      #Take the rows and columns of Matrix A from the user
      rows_A = int(input("Type the rows of the desired Matrix 'A': "))
      cols_A = int(input("Type the columns of the desired Matrix 'A': "))
      #Take the rows and columns of Matrix B from the user
      rows_B = int(input("Type the rows of the desired Matrix 'B': "))
      cols_B = int(input("Type the columns of the desired Matrix 'B': "))
   except ValueError:
      print("Please Enter Digits Only")
      return
   #Check if the subtraction is allowed
   while rows_A != rows_B and cols_A != cols_B:
     print("\nThe rows and columns of both matrices must be equal...Try again")
     try:
        #Try to take the rows and columns of Matrix A from the user
        rows_A = int(input("Type the rows of the desired Matrix 'A': "))
        cols_A = int(input("Type the columns of the desired Matrix 'A': "))
        #Try to take the rows and columns of Matrix B from the user
        rows_B = int(input("Type the rows of the desired Matrix 'B': "))
        cols_B = int(input("Type the columns of the desired Matrix 'B': "))
     except ValueError:
         print("Please Enter Digits Only")
         return
   print("\n")
   #Create Matrix A
   matrix_A = []
   for i in range(1,rows_A+1):
     new_matrix_A = []
     for j in range(1,cols_A+1):
       try:
          value = int(input(f"Type the scalars [{i}],[{j}] : "))
       except ValueError:
          print("Please Enter Digits Only")
          return
       new_matrix_A.append(value)
     matrix_A.append(new_matrix_A)
   print(f"\nMatrix 'A'")
   for row in matrix_A:
     print(f"{row}")
   print("\n")
   #Create Matrix B
   matrix_B = []
   for i in range(1,rows_B+1):
     new_matrix_B = []
     for j in range(1,cols_B+1):
       try:
          value = int(input(f"Type the scalars [{i}],[{j}] : "))
       except ValueError:
          print("Please Enter Digits Only")
          return
       new_matrix_B.append(value)
     matrix_B.append(new_matrix_B)
   print(f"\nMatrix 'B'")
   for column in matrix_B:
     print(f"{column}")
   #Create an empty matrix named 'C' to save the result of subtraction
   C = []
   for i in range(rows_A):
     col = []
     for j in range(rows_B):
       col.append(0)
     C.append(col)
   #Matrix B subtracted from the Matrix A and then save the result in the Matrix C
   for i in range(rows_A):
     for j in range(rows_B):
             C[i][j] = C[i][j] + (matrix_A[i][j] - matrix_B[i][j])
   #Show the result of subtraction
   print("\nMatrix B subtracted from Matrix A")
   for row in C:
     print(f"{row}") 

menu()
