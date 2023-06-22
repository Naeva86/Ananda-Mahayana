hash_table = [None] * 10

def hashing_func(value):
    return len(value) % 10

def insert(hash_table, value):
    hash_key = hashing_func(value)
    hash_table[hash_key] = value
    
def search(hash_table, value):
    return hash_table[hashing_func(value)]

insert(hash_table, 'Nepal')
insert(hash_table, 'Indonesia')
insert(hash_table, 'USA')
insert(hash_table, 'UK')

print (hash_table)
negara = 'Indonesia'
print (search(hash_table, negara),'ditemukan pada indeks ke- ',hashing_func(negara))