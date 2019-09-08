class Test:
  def test(self):
    for i in range(3):
      yield print(i,)

class Test2():
  def test(self):
    idx = 0
    for i in range(5):
      yield idx
t1 = Test()
t2 = Test2()
dictionary = {"1":t1.test(), "2":t2.test()}
for i in dictionary["2"]:
  i
