from tkinter import *
from operations import Operations


class CreateCalcButton:
    global result_value

    def __init__(self):
        self.operation = Operations()

    def clear_buttons(self, en1, en2, res):
        en1.delete(0, END)
        en2.delete(0, END)
        res.set(0)

    def click_button(self, windows_place, value, option_buton, entry1, entry2, result_value):
        if option_buton == 1:
            result_value.set(self.operation.calculate_sum(int(entry1.get()), int(entry2.get())))
        elif option_buton == 2:
            result_value.set(self.operation.calculate_difference(int(entry1.get()), int(entry2.get())))
        elif option_buton == 3:
            result_value.set(self.operation.calculate_multiplication(int(entry1.get()), int(entry2.get())))
        elif option_buton == 4:
            result_value.set(self.operation.calculate_division(int(entry1.get()), int(entry2.get())))
        elif option_buton == 5:
            result_value.set(self.operation.calculate_power(int(entry1.get()), int(entry2.get())))
        elif option_buton == 6:
            self.clear_buttons(entry1, entry2, result_value)

        result_value = Label(windows_place, text=value.get())
        result_value.grid(row=6, column=1)

    def create_gui(self):
        global radio_button1
        global radio_button2
        global radio_button3
        global radio_button4
        global radio_button5
        global radio_button6

        root = Tk()
        root.title = "Option calculator app"  # create 2 labels with 2 entries
        result_value = DoubleVar()  # just stocks the option which is selected
        label1 = Label(root, text="Number 1", padx=10, pady=5)
        label2 = Label(root, text="Number 2", padx=10, pady=5)
        label1.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        # create 2 entries
        entry1 = Entry(root, width=18, borderwidth=5, highlightbackground="#CBD35C", fg="#124E58", bd=5,
                       font=("Arial", 14, "bold"))
        entry2 = Entry(root, width=18, borderwidth=5, highlightbackground="#CBD35C", fg="#124E58", bd=5,
                       font=("Arial", 14, "bold"))
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        entry1.insert(0, str(0))
        entry2.insert(0, str(0))

        # create a frame
        frame_calc = LabelFrame(root, text="Option calculator", padx=10, pady=10, width=400, bd=10,
                                font=("Georgia", 10, "bold"), labelanchor="n")  # with ancho
        frame_calc.grid(row=2, columnspan=2, column=0, sticky="WE")
        # put the buttons in the frame
        label_result = Label(frame_calc, text="Result", padx=5, pady=2, font=("Georgia", 18, "bold"), anchor="ne")

        radio_button1 = Radiobutton(frame_calc, text="Addition", variable=result_value,
                                    value=result_value, pady=10,
                                    bd=15, font=("Georgia", 10, "bold"),
                                    bg="#b22222",
                                    command=lambda: self.click_button(frame_calc, result_value, 1, entry1, entry2,
                                                                      result_value),
                                    anchor="n")
        radio_button2 = Radiobutton(frame_calc, text="Difference", variable=result_value,
                                    value=result_value,
                                    padx=10,
                                    pady=10, bd=15,
                                    font=("Georgia", 10, "bold"),
                                    bg="#b22222",
                                    command=lambda: self.click_button(frame_calc, result_value, 2, entry1, entry2,
                                                                      result_value),
                                    anchor="n")
        radio_button3 = Radiobutton(frame_calc, text="Multiplication", variable=result_value,
                                    value=result_value,
                                    padx=10,
                                    pady=10, bd=15,
                                    font=("Georgia", 10, "bold"),
                                    bg="#b22222",
                                    command=lambda: self.click_button(frame_calc, result_value, 3, entry1, entry2,
                                                                      result_value),
                                    anchor="n")
        radio_button4 = Radiobutton(frame_calc, text="Division", variable=result_value,
                                    value=result_value,
                                    padx=10,
                                    pady=10, bd=15,
                                    font=("Georgia", 10, "bold"),
                                    bg="#b22222",
                                    command=lambda: self.click_button(frame_calc, result_value, 4, entry1, entry2,
                                                                      result_value),
                                    anchor="n")
        radio_button5 = Radiobutton(frame_calc, text="Power", variable=result_value,
                                    value=result_value, padx=10,
                                    pady=10, bd=15,
                                    font=("Georgia", 10, "bold"),
                                    bg="#b22222",
                                    command=lambda: self.click_button(frame_calc, result_value, 5, entry1, entry2,
                                                                      result_value),
                                    anchor="n")
        print(result_value.get())
        radio_button6 = Radiobutton(frame_calc, text="CLEAR", variable=result_value,
                                    value=result_value, padx=10,
                                    pady=10, bd=15,
                                    font=("Georgia", 10, "bold"),
                                    bg="#b22222",
                                    command=lambda: self.click_button(frame_calc, result_value, 6, entry1, entry2,
                                                                      result_value),
                                    anchor="n")

        result = Label(frame_calc, text=result_value.get(), padx=5, pady=10, font=("Georgia", 18, "bold"),
                       fg="#20B2AA", anchor="n")
        # put buttons on grid
        radio_button1.grid(row=0, column=0, sticky="WE")
        radio_button2.grid(row=1, column=0, sticky="WE")
        radio_button3.grid(row=2, column=0, sticky="WE")
        radio_button4.grid(row=3, column=0, sticky="WE")
        radio_button5.grid(row=4, column=0, sticky="WE")
        radio_button6.grid(row=5, column=0, sticky="WE")

        label_result.grid(row=6, column=0)
        result.grid(row=6, column=1)

        root.mainloop()
