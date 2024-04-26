import tkinter as tk
import sqlite3 as sql
from tkinter import ttk, messagebox

class TodoListApp:
    def __init__(self, obj):
        self.root = obj
        # it is used to name the title
        self.root.title("To-Do List ----> BHANU CHAITANYA")
        self.root.geometry("500x400")   # it is used for todo list dimensions 
        self.root.resizable(0,0)        # here 0 means false, which is used to not allow further resizing to horizontal and vertical dimensions

        # The following commands for connecting to inbuilt database sqlite3
        self.connection = sql.connect('ToDoList.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('create table if not exists tasks (title text)')
        
        # created empty list to append tasks which will be added through database
        self.tasks = []

        self.header_frame = tk.Frame(self.root, bg="#000000")
        self.functions_frame = tk.Frame(self.root, bg="#EE82EE")
        self.listbox_frame = tk.Frame(self.root, bg="#800000")
        
        self.header_frame.pack(fill="both")
        self.functions_frame.pack(side="left", expand=True, fill="both")
        self.listbox_frame.pack(side="right", expand=1, fill="both")

        self.header_label = ttk.Label(
            self.header_frame,
            text="My To-Do List",
            font=("Times New Roman", "20"),
            background="#000000",
            foreground="#FFFF00"
        )
        self.header_label.pack(padx=20, pady=20)

        self.task_label = ttk.Label(
            self.functions_frame,
            text="Enter The Task:",
            font=("Times New Roman", "11", "bold"),
            background="#EE82EE",
            foreground="#000000"
        )
        self.task_label.place(x=85, y=50)

        self.task_field = ttk.Entry(
            self.functions_frame,
            font=("Times New Roman", "12"),
            width=25,
            background="#FFFF00",
            foreground="#A52A2A"
        )
        self.task_field.place(x=35, y=80)

        # The following is for adding GUI buttons to add,delete, and exit. 
        self.add_button = ttk.Button(
            self.functions_frame,
            text="Add",
            width=15,
            command=self.add_task
        )
        self.del_button = ttk.Button(
            self.functions_frame,
            text="Delete",
            width=10,
            command=self.delete_task
        )
        self.del_all_button = ttk.Button(
            self.functions_frame,
            text="Delete All",
            width=10,
            command=self.delete_all_tasks
        )
        self.exit_button = ttk.Button(
            self.functions_frame,
            text="Exit",
            width=15,
            command=self.close
        )

        # The following statements are for positions for buttons
        self.add_button.place(x=85, y=120)
        self.del_button.place(x=40, y=160)
        self.del_all_button.place(x=150, y=160)
        self.exit_button.place(x=85, y=200)

        self.task_listbox = tk.Listbox(
            self.listbox_frame,
            width=26,
            height=13,
            selectmode='SINGLE',
            background="#000000",
            foreground="#FFFF00",
            selectbackground="#000000",
            selectforeground="#FF0000",
            justify='center'
        )
        self.task_listbox.place(x=50, y=60)

        self.retrieve_database()
        self.list_update()

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.cursor.execute('insert into tasks values (?)', (task_string,))
            self.connection.commit()
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.list_update()
                self.cursor.execute('delete from tasks where title = ?', (the_value,))
                self.connection.commit()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            while(len(self.tasks) != 0):
                self.tasks.pop()
            self.cursor.execute('delete from tasks')
            self.list_update()
            self.connection.commit()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        print(self.tasks)
        self.root.destroy()

    def retrieve_database(self):
        while(len(self.tasks) != 0):
            self.tasks.pop()
        for row in self.cursor.execute('select title from tasks'):
            self.tasks.append(row[0])

# main program
obj = tk.Tk()
app = TodoListApp(obj)
obj.mainloop()
