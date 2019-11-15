# Test addition
m1 = Matrix([[1,2,3],[1,2,3]])
m2 = Matrix([[3,2,1],[3,2,1]])
result = m1.add(m2)
print("\nAdding " + str(m1.matrix) + " and " + str(m2.matrix) + ", result: " + str(result.matrix))
if result.matrix == [[4,4,4],[4,4,4]]:
  print("Addition test successful")
else:
  print("Addition test failed")

# Test scalar product
m1 = Matrix([[1,2,3],[4,5,6]])
scalar = 2
result = m1.scalar_product(scalar)
print("\nMultiplying " + str(m1.matrix) + " by scalar " + str(scalar) + ", result: " + str(result.matrix))
if result.matrix == [[2,4,6],[8,10,12]]:
  print("Scalar product test successful")
else:
  print("Scalar product test failed")

# Test matrix product
m1 = Matrix([[1,2,3],[4,5,6]])
m2 = Matrix([[7,8],[9,10],[11,12]])
result = m1.matrix_product(m2)
print("\nMultiplying " + str(m1.matrix) + " by matrix " + str(m2.matrix) + ", result: " + str(result.matrix))
if result.matrix == [[58,64],[139,154]]:
  print("Matrix product test successful")
else:
  print("Matrix product test failed")

# Test transpose
m1 = Matrix([[1,2],[3,4],[5,6]])
result = m1.transpose()
print("\nTransposing " + str(m1.matrix) + ", result: " + str(result.matrix))
if result.matrix == [[1,3,5],[2,4,6]]:
  print("Transpose test successful")
else:
  print("Transpose test failed")

# Test determinant 2x2
m1 = Matrix([[3,8],[4,6]])
result = m1.determinant()
print("\nDeterminant of " + str(m1.matrix) + " is " + str(result))
if result == -14:
  print("Determinant 2x2 test successful")
else:
  print("Determinant 2x2 test failed")

# Test determinant 3x3
m1 = Matrix([[6,1,1],[4,-2,5],[2,8,7]])
result = m1.determinant()
print("\nDeterminant of " + str(m1.matrix) + " is " + str(result))
if result == -306:
  print("Determinant 3x3 test successful")
else:
  print("Determinant 3x3 test failed")

# Test get_rows
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
result = m1.get_rows(2,4)
print("\nGetting rows 2 and 4 of " + str(m1.matrix) + ", result: " + str(result.matrix))
if result.matrix == [[4,5,6],[10,11,12]]:
  print("Rows test successful")
else:
  print("Rows test failed")

# Test get_columns
m1 = Matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
result = m1.get_columns(2,4)
print("\nGetting columns 2 and 4 of " + str(m1.matrix) + ", result: " + str(result.matrix))
if result.matrix == [[2,4],[7,9],[12,14]]:
  print("Columns test successful")
else:
  print("Columns test failed")

# str test
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print("\nTesting __str__ implementation:")
print(str(m1))
