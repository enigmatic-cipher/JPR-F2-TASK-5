"""
Modify the class ContactDetails in Task2. Create two constructors. The first one takes email address, mobile number and landline as input. The second constructor takes email address and mobile number as input. Also add a method printDetails in the class. In another class create objects of the class ContactDetails using both the constructors and print them.
"""

class contactDetails:
  def __init__(self, email_address, mobile_number, landline):
    self.email_address = email_address
    self.mobile_number = mobile_number
    self.landline = landline

  def __str__(self):
    return "Contact Detail: Email ID: {}, Mobile No: {}, & Landline: {}".format(self.email_address,self.mobile_number,self.landline)

e_id = input("Enter Email ID: ")
m_no = input("Enter Mobile Number: ")
llne = input("Enter Landline Number: ")

emp_1 = contactDetails(e_id,m_no,llne)
print(emp_1)
