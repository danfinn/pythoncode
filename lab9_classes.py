#!/usr/bin/python

class Payroll:
  def __init__(self,name,wage,hours):
    self.name = name
    self.wage = wage
    self.hours = hours
    self.overtimeWage = self.wage * 1.5

  def calculate_pay(self):
    pay_check = self.wage * self.hours
    print pay_check

  def check_overtime(self):
    if (self.hours > 40):
      print "%s worked overtime" %self.name

  def full_output(self):
    if (self.hours <= 40):
      print "%s worked %d hours this week at %d dollars per hour.  The total earned is %d" %(self.name,self.hours,self.wage,(self.hours * self.wage))
    elif (self.hours > 40):
      overtime_hours = self.hours - 40
      print "%s worked %d hours this week.  %d of those hours are at an overtime rate.  The total earned is %d." %(self.name,self.hours,overtime_hours,((40 * self.wage) + (overtime_hours * self.overtimeWage)))

employee_name = raw_input("Enter employees name: ")
employee_wage = int(raw_input("Enter employees hourly wage: "))
employee_hours_worked = int(raw_input("Enter employees hours for the week: "))

if type(employee_name) == str and type(employee_wage) == int and type(employee_hours_worked) == int:
  employee1 = Payroll(employee_name,employee_wage,employee_hours_worked)
  employee1.full_output()
  
#employee1 = Payroll('Bob',10,41)
#employee1.full_output()
