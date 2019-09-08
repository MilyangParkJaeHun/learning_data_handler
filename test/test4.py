def test():
  a = 1
  b = 2
  def test2(c, d):
    print(a, b, c, d)

  def test3(c, d):
    print(d, c, b, a)
  return {"1":test2, "2":test3}



test3 = test()
print(test3["2"](3,4))
