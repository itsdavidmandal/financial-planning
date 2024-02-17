import tkinter as tk #importing the tkinter module for ceating gui interface

def calculate_eligibility(): #function to handle the core logic of determining phone eligibility based on user input.
  try:
    price_of_mobile = float(price_entry.get())
    """
Retrieving User Input:

- The `price_entry.get()` call retrieves the text currently displayed in the
  `price_entry` widget. This text represents the price of the mobile phone
  entered by the user.

Converting to Float:

- The `float(...)` part tries to convert the retrieved text (`price_entry.get()`)
  into a floating-point number. This conversion is necessary because the
  eligibility calculation in the larger code expects a numerical value for the
  phone price.

- If the conversion is successful, the converted number is stored in the
  `price_of_mobile` variable.
"""

    salary = float(salary_entry.get()) #same as the price of mobile
    emi_percent = float(emi_entry.get()) #same as the price of mobile
    emi_amount = 0.01 * emi_percent * price_of_mobile
    monthly_salary = salary / 12

    if price_of_mobile > 0.1 * salary:
      output_label.config(text="Nope, you are not eligible.") # Update output label to display "not eligible" message

    elif emi_amount > 0.15 * monthly_salary:
      output_label.config(text="Nope, you are not eligible.") # Update output label to display "not eligible" message

    else:
      output_label.config(text="Yep, you are eligible!")# Update output label to display "eligible" message

  except ValueError:
    output_label.config(text="Please enter valid numbers.")# Update output label to display "value error" message


root = tk.Tk() #creating the main tkinter window
root.title("Phone Eligibility Calculator") #naming the title of the wondow

# Labels and Input fields
price_label = tk.Label(root, text="Price of mobile:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

salary_label = tk.Label(root, text="Your salary:")
salary_label.pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

emi_label = tk.Label(root, text="EMI percentage:")
emi_label.pack()
emi_entry = tk.Entry(root)
emi_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_eligibility)
calculate_button.pack()

# Output label
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
