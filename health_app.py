import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load ML model
model = joblib.load("model.pkl")

# Window
root = tk.Tk()
root.title("AI Health Risk Predictor")
root.geometry("700x500")
root.configure(bg="#121212")

# Title
title = tk.Label(root,
                 text="AI Health Risk Prediction System",
                 font=("Segoe UI",20,"bold"),
                 bg="#121212",
                 fg="#00E5FF")

title.pack(pady=20)


# Main Frame
frame = tk.Frame(root,bg="#1e1e1e",padx=20,pady=20)
frame.pack()


def create_input(label,row):

    tk.Label(frame,
             text=label,
             font=("Segoe UI",12),
             bg="#1e1e1e",
             fg="white").grid(row=row,column=0,padx=10,pady=10,sticky="w")

    entry = tk.Entry(frame,
                     font=("Segoe UI",12),
                     width=15)

    entry.grid(row=row,column=1,padx=10,pady=10)

    return entry


age = create_input("Age",0)
weight = create_input("Weight (kg)",1)
waist = create_input("Waist",2)
pulse = create_input("Pulse",3)
bp = create_input("Blood Pressure",4)
chol = create_input("Cholesterol",5)


# Result Label
result_label = tk.Label(root,
                        text="",
                        font=("Segoe UI",16,"bold"),
                        bg="#121212")

result_label.pack(pady=10)


def predict():

    try:

        values = np.array([[

        int(age.get()),
        int(weight.get()),
        int(waist.get()),
        int(pulse.get()),
        int(bp.get()),
        int(chol.get())

        ]])

        result = model.predict(values)[0]

        if result == 0:
            risk = "LOW RISK"
            color = "#00E676"
            tip = "Healthy lifestyle 👍"

        elif result == 1:
            risk = "MEDIUM RISK"
            color = "#FFC107"
            tip = "Exercise more and reduce fats"

        else:
            risk = "HIGH RISK"
            color = "#FF5252"
            tip = "Consult a doctor immediately"


        result_label.config(
            text=f"Health Risk: {risk}\nTip: {tip}",
            fg=color
        )


        # Graph
        labels = ["Age","Weight","Waist","Pulse","BP","Cholesterol"]

        plt.figure()
        plt.bar(labels,values[0])
        plt.title("Health Data Visualization")
        plt.ylabel("Values")
        plt.show()


    except:
        messagebox.showerror("Error","Please enter valid numbers")


def clear():

    age.delete(0,tk.END)
    weight.delete(0,tk.END)
    waist.delete(0,tk.END)
    pulse.delete(0,tk.END)
    bp.delete(0,tk.END)
    chol.delete(0,tk.END)

    result_label.config(text="")


# Buttons Frame
btn_frame = tk.Frame(root,bg="#121212")
btn_frame.pack(pady=20)

predict_btn = tk.Button(btn_frame,
                        text="Predict Risk",
                        command=predict,
                        font=("Segoe UI",12,"bold"),
                        bg="#00ADB5",
                        fg="white",
                        width=15)

predict_btn.grid(row=0,column=0,padx=10)


clear_btn = tk.Button(btn_frame,
                      text="Clear",
                      command=clear,
                      font=("Segoe UI",12,"bold"),
                      bg="#FF5252",
                      fg="white",
                      width=10)

clear_btn.grid(row=0,column=1,padx=10)


root.mainloop()