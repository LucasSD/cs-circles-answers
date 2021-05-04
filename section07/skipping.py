counter = 0
while True:
  lineIn = input()
  if lineIn=='SKIP': continue
  if lineIn=='END': break
  counter += 1
  print('line', counter, '=', lineIn)