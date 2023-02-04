# Salary Calculator
print("S A L A R Y  C A L C U L A T O R")

name = str(input("Please enter the Name of Employee: "))
designation = str(input(
    '''Choose the designation of the employee:
Manager
Normal Employee
'''
))
mngr_gst = 18
norml_gst = 18
mngr_bonus = 5
norml_bonus = 3
error = "Error! Please Try Again."

if designation == 'Manager':
        mngr_basic = float(input("Enter Basic Salary of Manager: ₹"))
        mngr_bonus_sal = mngr_basic+(mngr_basic*((mngr_bonus/2)/100))
        mngr_gst_sal = mngr_bonus_sal-(mngr_bonus_sal*((mngr_gst/2)/100))
        mngr_finl_sal = mngr_gst_sal

elif designation == 'Normal Employee':
        norml_basic = float(input("Enter Basic Salary of Normal Employee: ₹"))
        norml_bonus_sal = norml_basic+(norml_basic*((norml_bonus/2)/100))
        norml_gst_sal = norml_bonus_sal-(norml_bonus_sal*((norml_gst/2)/100))
        norml_finl_sal = norml_gst_sal

else:
    print(error)

print("\n")
print("SALARY BREAKUP")
print("==============================================")
print(" NAME OF EMPLOYEE : ",name)
print(" DESIGNATION OF EMPLOYEE : ",designation)

if designation == 'Manager':
    print(" SALARY OF THE MANAGER : ₹", mngr_basic)
    print(" BONUS %: ", mngr_bonus, "%")
    print(" GST %: ", mngr_gst, "%")
    print(" FINAL SALARY: ₹", mngr_finl_sal)
elif designation == 'Normal Employee':
    print(" SALARY OF THE NORMAL EMPLOYEE : ₹", norml_basic)
    print(" BONUS %: ", norml_bonus, "%")
    print(" GST %: ", norml_gst, "%")
    print(" FINAL SALARY: ₹", norml_finl_sal)
else:
    print(error)

print("==============================================")




