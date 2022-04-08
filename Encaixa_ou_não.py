n = int(input())
for i in range(n):
  x, y = list(map(str, input().split()))
  ans = ""
  teste = 0
  cont = 0
  if len(x) < len(y):
    ans = "nao "
  else:
    for j in range(len(y)):
      teste -= 1
      cont += 1 if x[teste] == y[teste] else 0
    ans = "nao " if cont != len(y) else ""
  print(ans + "encaixa")
