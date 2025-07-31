import tkinter as tk
from tkinter import ttk, messagebox

# Function to add a new employee
def add_employee():
    emp_id = emp_id_entry.get()
    emp_name = emp_name_entry.get()
    salary = salary_entry.get()

    if emp_id == "" or emp_name == "" or salary == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    tree.insert("", "end", values=(emp_id, emp_name, "N/A", salary))  # "mobile" is just placeholder
    clear_fields()

# Function to update selected employee
def update_employee():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to update.")
        return

    emp_id = emp_id_entry.get()
    emp_name = emp_name_entry.get()
    salary = salary_entry.get()

    tree.item(selected, values=(emp_id, emp_name, "N/A", salary))  # Update tree row
    clear_fields()

# Function to delete selected employee
def delete_employee():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to delete.")
        return
    tree.delete(selected)
    clear_fields()

# Function to clear entry fields
def clear_fields():
    emp_id_entry.delete(0, tk.END)
    emp_name_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)

# Function to populate form when row is selected
def on_row_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        emp_id_entry.delete(0, tk.END)
        emp_id_entry.insert(0, values[0])
        emp_name_entry.delete(0, tk.END)
        emp_name_entry.insert(0, values[1])
        salary_entry.delete(0, tk.END)
        salary_entry.insert(0, values[3])

# --- UI ---
root = tk.Tk()
root.title("Employee Registration")
root.geometry("800x500")
root.config(bg="white")

tk.Label(root, text="Employee Registration", fg='red', font=(None, 30), bg="white").place(x=250, y=10)

# Labels & Fields
tk.Label(root, text="Employee Id", bg="white", font=('Arial', 12)).place(x=50, y=80)
emp_id_entry = tk.Entry(root)
emp_id_entry.place(x=200, y=80)

tk.Label(root, text="Employee Name", bg="white", font=('Arial', 12)).place(x=50, y=120)
emp_name_entry = tk.Entry(root)
emp_name_entry.place(x=200, y=120)

tk.Label(root, text="Salary", bg="white", font=('Arial', 12)).place(x=50, y=160)
salary_entry = tk.Entry(root)
salary_entry.place(x=200, y=160)

# Buttons with functionality
tk.Button(root, text="Add", width=10, command=add_employee).place(x=200, y=200)
tk.Button(root, text="Update", width=10, command=update_employee).place(x=310, y=200)
tk.Button(root, text="Delete", width=10, command=delete_employee).place(x=420, y=200)

# Treeview table
tree = ttk.Treeview(root, columns=("id", "empname", "mobile", "salary"), show='headings')
tree.heading("id", text="ID")
tree.heading("empname", text="Employee Name")
tree.heading("mobile", text="Mobile")
tree.heading("salary", text="Salary")

tree.column("id", width=100)
tree.column("empname", width=200)
tree.column("mobile", width=150)
tree.column("salary", width=100)

tree.place(x=50, y=260, width=700, height=200)

# Bind row select
tree.bind("<ButtonRelease-1>", on_row_select)

root.mainloop()

