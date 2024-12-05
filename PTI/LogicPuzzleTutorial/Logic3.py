# SOAL FIBONACCI
# 1,1,2,3,5,8,13 (angka yang ditambah sebelumnya dan menghasilkan selanjutnya disebut fibonacci)
def fibonacci(a):
  if a <= 2:
    return 1
  else:
    return fibonacci(a - 1) + fibonacci(a - 2)
  
print(fibonacci(4))