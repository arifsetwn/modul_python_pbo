def division(a, b):
  try:
    print("{0} / {1} = {2}".format(a, b, a / b))
  except ZeroDivisionError:
    print("Tidak bisa membagi angka dengan 0.")
  except TypeError:
    print("Inputan harus berupa angka.")
  else:
    print("Tidak ada exception yang terjadi.")
  finally:
    print("Program selesai dieksekusi.")

division(10, 2)