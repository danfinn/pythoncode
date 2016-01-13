#!/usr/bin/python

#class Person:
#  def __init__(self,gender,name):
#    self.gender = gender
#    self.name = name
#
#  def display(self):
#    print("You're a ", self.gender ,", and your name is : ", self.name)
#
#people = Person('Male','Dan')
#people2 = Person('Female','Candice')
#people.display()
#people2.display()

class Example:
  def __init__(self, **kwargs):
    self.variables = kwargs
  def set_vars(self,k,v):
    self.variables[k] = v
  def get_vars(self,k):
    return self.variables.get(k, None)

var = Example(Age=36, Location='Utah')
var.set_vars('Name','Dan')
print(var.get_vars('Name'))
print(var.get_vars('Location'))
