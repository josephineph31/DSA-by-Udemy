#O(n)
def print_numbers(n):
 for i in range (n):
  print(i)
print_numbers(10)
#O(n^2)
def print_pairs(n):
 for i in range (n):
  for j in range(n):
    print(i, j)
print_pairs(3)