##Payroll calculations
def payrollsoftware():
  # Basic input information
  empname = input('Name: ')
  while empname == '':
    print('Payroll finished! Exiting...')
    exit()
  emppos = input('Position: ')

  # Hours worked (italics)
  print("\x1B[3mHow many hours did they work? Input a list of hours through Monday - Sunday (example : 1 2 8 0 ect...) Include all days, don't miss 0's\x1B[0m")
  mo, tu, we, th, fr, sa, su = map(int, input('Hours worked: ').split())

  #fix capitalization
  empname = empname.lower();
  empname = empname.capitalize();
  emppos = emppos.lower();
  emppos = emppos.capitalize();

  #calculations
  if emppos == 'Manager':
    
    moneyearned = (mo + tu + we + th + fr) * 30 + (sa * 33) + (su * 34);
  else:
    moneyearned = (mo + tu + we + th + fr) * 23 + (sa * 26) + (su * 27);
  print(f'{empname} earned ${moneyearned} in their {emppos} position')
  print('-----')
#repeat
while True:
  payrollsoftware()
