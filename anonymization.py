import functionFlinha
import keyGenerator
import ipaddress


dec_to_bin = lambda ip: bin(int(ipaddress.ip_address(ip)))  

    
def split(lista) -> tuple[str, str]:
    half = int(len(lista) / 2)
    return (lista[:half], lista[half:])

def size(classe) -> tuple[str, str]:
    return (16, 16)

def xor_vectors(vec1, vec2):
    assert len(vec1) == len(vec2), "Os vetores devem ter o mesmo tamanho."
    return [a ^ b for a, b in zip(vec1, vec2)]

def octetos(parts):
    aux = 0 
    q1 = ""
    while aux<8:
        q1 = q1 + str(parts[0][aux])
        aux += 1
            
    q2 = ""
    while aux<16:
        q2 = q2 + str(parts[0][aux])
        aux += 1     
            
    aux = 0 
    q3 = ""
    while aux<8:
        q3 = q3 + str(parts[1][aux])
        aux += 1
            
    q4 = ""
    while aux<16:
        q4 = q4 + str(parts[1][aux])
        aux += 1 
            
    
    return(q1,q2,q3,q4)



def encrypt(ip, key, round):
    listKey = keyGenerator.keyGenerator(key, round) 
    binary = dec_to_bin(ip)[2:]
    
    while(len(binary)!=32):
            binary = '0' + binary

    list_binary = keyGenerator.bin_to_list(binary)

    parts = split(list_binary)
    
    
    i = 0
    
    while(i!=round):
        if(i%2==0):
                esquerda = parts[0]
                direita = parts[1]
                anom = functionFlinha.encryption(listKey[i], esquerda)
                aux = xor_vectors(anom[0], esquerda)
                parts = [direita, aux]
           
        else:
                direita = parts[0]
                esquerda = parts[1]
                anom = functionFlinha.encryption(listKey[i], direita)
                aux = xor_vectors(anom[0], parts[1])
                parts = [esquerda, aux]
            
        i = i + 1
    
    ans = octetos(parts)
    
    return(str(int(ans[0],2)) + "." + str(int(ans[1],2)) + "." + str(int(ans[2],2)) + "." + str(int(ans[3],2)))


print(encrypt("223.123.3.99","strong_key_nbits",16))
print(encrypt("223.123.57.80", "strong_key_nbits", 16))