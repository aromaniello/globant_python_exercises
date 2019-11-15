class Matrix:
  def __init__(self, matrix):
    self.matrix = matrix
    self.rows = len(matrix)
    self.columns = len(matrix[0])

    for row in matrix:
      if len(row) != self.columns:
        raise InvalidMatrixException

  def add(self, other):
    # print(type(other))
    if self.rows != other.rows or self.columns != other.columns:
      raise InvalidMatrixOperationException

    result = []
    for i in range(self.rows):
      result.append([])
      for j in range(self.columns):
        result[i].append(self.matrix[i][j] + other.matrix[i][j])

    return Matrix(result)

  def scalar_product(self, scalar):
    result = []
    for i in range(self.rows):
      result.append([])
      for j in range(self.columns):
        result[i].append(self.matrix[i][j] * scalar)

    return Matrix(result)

  def matrix_product(self, other):
    if self.columns != other.rows:
      raise InvalidMatrixOperationException

    result = []
    for i in range(self.rows):
      result.append([])
      for j in range(other.columns):
        sum = 0
        for k in range(self.columns):
          sum += self.matrix[i][k] * other.matrix[k][j]
        result[i].append(sum)

    return Matrix(result)

  def transpose(self):
    result = []

    for i in range(self.columns):
      result.append([])
      for j in range(self.rows):
        result[i].append(self.matrix[j][i])

    return Matrix(result)

  def determinant(self):
    if self.rows != self.columns:
      raise InvalidMatrixOperationException

    m = self.matrix

    if self.rows == 2:
      return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    elif self.rows == 3:
      return m[0][0]*m[1][1]*m[2][2]+m[0][1]*m[1][2]*m[2][0]+m[0][2]*m[1][0]*m[2][1]-m[0][2]*m[1][1]*m[2][0]-m[0][1]*m[1][0]*m[2][2]-m[0][0]*m[1][2]*m[2][1]
    else:
      raise InvalidMatrixSizeException

  def get_rows(self, *args):
    result = []
    for row in args:
      result.append(self.matrix[row-1])

    return Matrix(result)

  def get_columns(self, *args):
    result = []
    for i in range(self.rows):
      result.append([])
      for column in args:
        result[i].append(self.matrix[i][column-1])

    return Matrix(result)

  def __str__(self):
    strg = ""
    for i in range(self.rows):
      strg += "("
      for j in range(self.columns):
        strg += " " + str(self.matrix[i][j])
      strg += " )\n"
    return strg



class InvalidMatrixException(Exception):
  pass

class InvalidMatrixOperationException(Exception):
  pass

class InvalidMatrixSizeException(Exception):
  pass
