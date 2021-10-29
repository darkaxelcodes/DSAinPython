def find_buy_sell_stock_prices(a):
  cp = a[0]
  gsp = a[1]
  gp = gsp - cp
  
  for i in range(1, len(a)):
    p = a[i] - cp
    if p > gp:
      gp = p
      gsp = a[i]
    if a[i] < cp:
      cp = a[i]

  return((gsp - gp),gsp)