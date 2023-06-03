total = 0
def sum(nominal):
  global total
  total += float(nominal)

price = input("Masukkan Harga: ")
sum(price)
print("Total Harga : {0}".format(total))