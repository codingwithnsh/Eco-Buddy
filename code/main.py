import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from random import choice
import csv
import os
from datetime import datetime

# Constants
DAILY_EMISSION_FACTORS = {
    "Car Usage (km)": 0.2,
    "Motorcycle Usage (km)": 0.1,
    "Public Bus (km)": 0.05,
    "Train/Subway (km)": 0.04,
    "Air Travel (short-haul, km)": 0.15,
    "Air Travel (long-haul, km)": 0.11,
    "Bicycle Manufacturing (unit)": 5,
    "Walking Shoes (pair)": 20,
    "Electricity Usage (kWh)": 0.5,
    "Natural Gas Usage (kWh)": 0.2,
    "Water Usage (liter)": 0.001,
    "Internet Usage (GB)": 0.01,
    "Meat Consumption (Chicken, meal)": 6,
    "Meat Consumption (Beef, meal)": 27,
    "Vegetarian Meal (meal)": 1.5,
    "Cooking (meal)": 0.5,
    "Plastic Bag (unit)": 0.01,
    "Streaming Video (hour)": 0.36,
    "Shower (10 minutes)": 0.9,
}

TIPS = [
    "Use public transportation to reduce emissions.",
    "Adopt a plant-based meal once a week.",
    "Switch to energy-efficient appliances.",
    "Carpool to save fuel and reduce emissions.",
    "Unplug devices when not in use.",
]

DATA_FILE = "carbon_footprint_data.csv"
selected_date = datetime.now().strftime("%Y-%m-%d")
current_activity = None  # Initialize selection variable


def calculate_footprint():
    try:
        if not table.get_children():
            messagebox.showwarning("No Data", "Please add activities to calculate the footprint.")
            return

        total_footprint = 0
        activities = []
        values = []

        for row in table.get_children():
            activity, value = table.item(row, "values")
            value = float(value)
            if activity not in DAILY_EMISSION_FACTORS:
                raise ValueError(f"Activity '{activity}' not found in emission factors.")
            total_value = value * DAILY_EMISSION_FACTORS[activity]
            total_footprint += total_value
            activities.append(activity)
            values.append(total_value)

        result_label.config(text=f"Your daily carbon footprint: {total_footprint:.2f} kg CO₂")
        update_pie_chart(activities, values)
        save_data(total_footprint)
        tip_label.config(text=f"Tip: {choice(TIPS)}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")


def update_pie_chart(activities, values):
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    ax.pie(values, labels=activities, autopct="%1.1f%%", colors=plt.cm.tab20.colors)
    ax.set_title("Carbon Footprint Distribution")

    for widget in bottom_frame.winfo_children():
        if widget not in (result_label, tip_label):  # Preserve result_label and tip_label
            widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=bottom_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def save_data(total_footprint):
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Activity", "Value", "Total Footprint (kg CO₂)"])
        for row in table.get_children():
            activity, value = table.item(row, "values")
            writer.writerow([selected_date, activity, value, total_footprint])


def update_listbox(*args):
    search_term = search_var.get().lower()
    listbox.delete(0, tk.END)
    for item in DAILY_EMISSION_FACTORS:
        if search_term in item.lower():
            listbox.insert(tk.END, item)


def on_listbox_select(event):
    global current_activity
    selection = event.widget.curselection()
    if selection:
        current_activity = event.widget.get(selection[0])
        selected_activity_label.config(text=f"Selected Activity: {current_activity}")


def add_value():
    global current_activity
    try:
        value = float(activity_value_entry.get())
        if current_activity:
            table.insert("", "end", values=(current_activity, value))
            activity_value_entry.delete(0, tk.END)
            calculate_footprint()
        else:
            messagebox.showerror("Error", "Select an activity first.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")


def show_data_for_date():
    global selected_date
    selected_date = cal.get_date()
    messagebox.showinfo("Date Selected", f"Showing data for {selected_date}")


root = tk.Tk()
root.title("Eco-Buddy")
root.geometry("1200x700")

left_frame = tk.Frame(root, width=400, bg="#f0f0f0")
left_frame.pack(side="left", fill="y")

search_var = tk.StringVar()
search_var.trace("w", update_listbox)  # Call update_listbox when search_var changes
search_entry = tk.Entry(left_frame, textvariable=search_var, font=("Arial", 12))
search_entry.pack(pady=10, padx=10, fill="x")

listbox = tk.Listbox(left_frame, font=("Arial", 10), height=15)
listbox.pack(padx=10, pady=10, fill="both", expand=True)
listbox.bind("<<ListboxSelect>>", on_listbox_select)

selected_activity_label = tk.Label(left_frame, text="Selected Activity: None", font=("Arial", 10))
selected_activity_label.pack(pady=5)

activity_value_entry = tk.Entry(left_frame, font=("Arial", 10))
activity_value_entry.pack(pady=5)

add_button = tk.Button(left_frame, text="Add Value", command=add_value, font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.pack(pady=10)

cal = Calendar(left_frame, selectmode="day", year=2025, month=5, day=10)
cal.pack(pady=10)

date_button = tk.Button(left_frame, text="Show Data", command=show_data_for_date)
date_button.pack(pady=5)

right_frame = tk.Frame(root, width=800, bg="#ffffff")
right_frame.pack(side="right", fill="both", expand=True)

top_frame = tk.Frame(right_frame, height=300, bg="#ffffff")
top_frame.pack(fill="x")

columns = ("Activity", "Value")
table = ttk.Treeview(top_frame, columns=columns, show="headings", height=15)
table.heading("Activity", text="Activity")
table.heading("Value", text="Value")
table.pack(fill="both", expand=True)

bottom_frame = tk.Frame(right_frame, height=400, bg="#ffffff")
bottom_frame.pack(fill="both", expand=True)

result_label = tk.Label(bottom_frame, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

tip_label = tk.Label(bottom_frame, text="", font=("Arial", 10, "italic"), wraplength=1000, justify="center")
tip_label.pack(pady=10)

update_listbox()  # Initialize Listbox values

root.mainloop()
