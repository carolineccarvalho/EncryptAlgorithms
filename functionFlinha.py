import numpy as np
import utilities

lineSBoxFirst = []
lineSBoxSecond = []


SBox = np.array([2,
                 3,
                 0,
                 1
                 ])

SBox2 = np.array([[0, 1],
                 [2, 3],
                 [0, 1],
                 [2, 3]
                 ])

Permutation = np.array([[0, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 1],
                        [0, 0, 1, 0]])

EP = np.array([[1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 1, 0],
               [0, 0, 0, 1, 0, 1],
               ])


def substituitionLinha(matrix):
    Matriz = []
    for row in matrix:
        newRow = []
        for i in range(0,4):
            if(row[0]*2+ row[1] == SBox[i]):
                newRow.append(utilities.int_to_binary_list(i)[0])
                newRow.append(utilities.int_to_binary_list(i)[1])

        for i in range(0,4):
            if(row[2]*2+ row[3] == SBox[i]):
                newRow.append(utilities.int_to_binary_list(i)[0])
                newRow.append(utilities.int_to_binary_list(i)[1])

        Matriz.append(newRow)
    
    return Matriz

#função de substituição utilizando a SBox
def substituition(matrix):
  new_matrix = []
  for row in matrix:
    result = int(row[0] * 2 + row[2])
    lineSBoxFirst.append(result)
    value = SBox2[result][int(row[1])]
    value1, value2 = utilities.int_to_binary_list(value)
    new_row = [value1, value2,int(row[3]),int(row[4]),int(row[5])]
    new_matrix.append(new_row)

  matrix = new_matrix
  new_matrix = []
  for row in matrix:
    result = int(row[0] * 2 + row[2])
    lineSBoxSecond.append(result)
    value = SBox2[result][int(row[1])]
    value1, value2 = utilities.int_to_binary_list(value)
    new_row = [value1, value2,int(row[3]),int(row[4])]
    new_matrix.append(new_row)

  return new_matrix

def encryption(key, part):
    line = int(len(part)/4)
    
    Matriz = np.array(part).reshape(line,4)
    result = np.dot(Matriz, EP).astype(int)
    newKey = utilities.expand(result.size, key)
    Key = np.array(newKey).reshape(result.shape)
    result_matrix = np.bitwise_xor(result, Key).astype(int)
    aux = substituition(result_matrix)
    aux = np.array(aux).astype(int)
    
    for i in range(1, aux.shape[0]):  # Começa de 1 para ignorar a primeira linha
        aux[i] = np.roll(aux[i], shift=1)  # Shift de 1 posição à direita

    new = np.dot(aux,Permutation)

    return (new.flatten().tolist(), lineSBoxFirst, lineSBoxSecond) 

