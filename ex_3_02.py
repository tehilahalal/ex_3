import numpy as np
def create_matrix():
  matrix = np.array([[
    [ 1, 2, 3, 4],
    [ 7, 8, 9, 10],
    [13, 14, 15, 16],
    ], 
    [[ 1, 2, 2, 4], 
    [ 2, 5, 8, 2],
    [ 8, 5, 8, 8]]], dtype=float)
  return matrix

def main():
  matrix = create_matrix()
  print(matrix.ndim)
  print(matrix.shape)
  print(matrix.dtype)

if __name__=='__main__':
main()
