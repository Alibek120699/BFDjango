def date_fashion(you, date):
  if you>7 and date<3:
    return 0
  if you<3 and date>7:
    return 0
  if you<3 or date<3:
    return 0
  if you>7 or date>7:
    return 2
  return 1
