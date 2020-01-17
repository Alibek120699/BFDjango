def alarm_clock(day, vacation):
  if not vacation and (day == 0 or day == 6):
    return '10:00'
  if vacation and (day == 0 or day == 6):
    return 'off'
  if vacation:
    return '10:00'
  return '7:00'
