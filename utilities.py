def expand(size, key):
    keyCopy = key.copy()
    i = 0
    while(len(keyCopy) < size):
                keyCopy.insert(0,key[i])
                i = i + 1
                if(i==len(key)):
                    i = 0

   
    while(len(keyCopy) > size):
        keyCopy.pop(0)

    return keyCopy

def int_to_binary_list(n):
  binary_list = []
  while n > 0:
    bit = n % 2
    binary_list.insert(0, bit) 
    n //= 2

  if(len(binary_list) == 0):
    binary_list.append(0)
    binary_list.append(0)

  if(len(binary_list) == 1):
    binary_list.append(0)
    binary_list.reverse()

  return binary_list

