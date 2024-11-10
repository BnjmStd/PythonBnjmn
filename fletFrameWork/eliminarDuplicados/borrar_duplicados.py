import hashlib
import os

def hash_file (filename):
    h = hashlib.md5() # crea un obj hash con algoritmo md5
    with open(filename, 'rb') as file: # abre file mode binario para leerlo como secuencia de bytes 
        while chunk := file.read(8192): # Lee el archivo en bloques de 8192 bytes. 
            h.update(chunk) # agrega cada bloque de datos leido al obj hash 
            # update : procesa los datos y los incorpora al calc del hash

    return h.hexdigest() # retorna el hash


def find_duplicates(folder):
    hashes = {} # diccionario
    duplicates = []
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            file_hash = hash_file(full_path)
            if file_hash in hashes:
                duplicates.append((full_path, hashes[file_hash]))      
            else:
                hashes[file_hash] = full_path

        return duplicates

def delete_file(filepath):
    try:
        os.remove(filepath)
        return True
    
    except Exception as e:
        return False