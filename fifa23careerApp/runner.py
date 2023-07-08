from tkinter import *
import os
import constants
from PIL import Image, ImageTk

'''
PUT THIS ON GIT
'''


class ImageApp:
    global index_image

    def __init__(self):
        self.label_image = None
        self.index_image = 0

    def create_list_images(self):
        os.chdir(constants.path_players)
        list_images = []
        # create images
        fifa_team_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\fifa23.png"))
        donarumma_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\Donarumma.jpg"))
        t_hernandez_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\theo hernandez.jpg"))
        e_militao_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\eder_militao.jpg"))
        d_upamecano_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\upamecano.jpg"))
        n_mendes_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\nuno_mendes.jpg"))
        m_rashford_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\rashford.jpg"))
        j_bellingham_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\bellingham.jpg"))
        pedri_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\pedri.jpg"))
        kvaraskelia_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\kvaraskelia.jpg"))
        k_mbappe_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\mbappe.jpg"))
        e_haaland_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\haaland.jpg"))
        vinicius_image = ImageTk.PhotoImage(Image.open(constants.path_players + r"\vinicius.webp"))
        list_images.append(fifa_team_image)
        list_images.append(donarumma_image)
        list_images.append(t_hernandez_image)
        list_images.append(e_militao_image)
        list_images.append(d_upamecano_image)
        list_images.append(n_mendes_image)
        list_images.append(m_rashford_image)
        list_images.append(j_bellingham_image)
        list_images.append(pedri_image)
        list_images.append(kvaraskelia_image)
        list_images.append(k_mbappe_image)
        list_images.append(e_haaland_image)
        list_images.append(vinicius_image)
        return list_images

    def forward(self, window_place, list_images):
        # make global variables
        global button_forward
        global button_back
        global status_label

        print(self.index_image)
        print(len(list_images))

        # delete previous image

        button_back = Button(window_place, text="Back", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                             command=lambda: self.back(window_place, list_images))

        button_exit = Button(window_place, text="Exit", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                             command=window_place.quit)
        # put buttons on grid now

        # put status bar

        # se va intinde de la vest la est
        self.index_image += 1
        if self.index_image == len(list_images) - 1:
            button_forward = Button(window_place, text="Next", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                                    command=lambda: self.forward(window_place, list_images),
                                    state="disabled")
            self.label_image.grid_forget()
            self.label_image = Label(window_place, image=list_images[self.index_image])
            status_label = Label(window_place, text=constants.name_players[self.index_image], bd=3, fg='#70CF83',
                                 relief=SUNKEN,
                                 anchor=E,
                                 bg="#936554")
        else:
            button_forward = Button(window_place, text="Next", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                                    command=lambda: self.forward(window_place, list_images))
            self.label_image.grid_forget()
            # put now next image with buttons
            self.label_image = Label(window_place, image=list_images[self.index_image])
            status_label = Label(window_place, text=constants.name_players[self.index_image], bd=3, fg='#70CF83',
                                 relief=SUNKEN,
                                 anchor=E,
                                 bg="#936554")
        self.label_image.grid(row=0, column=0, columnspan=3)  # want the image to include all buttons
        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        button_exit.grid(row=1, column=1)
        status_label.grid(row=2, column=0, columnspan=3, sticky=W + E)

    def back(self, window_place, list_images):
        global button_forward
        global button_back
        global status_label
        print(self.index_image)
        # global label_image
        # delete previous image
        button_forward = Button(window_place, text="Next", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                                command=lambda: self.forward(window_place, list_images))

        button_exit = Button(window_place, text="Exit", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                             command=window_place.quit)

        # put buttons on grid now

        # put status bar

        self.index_image -= 1
        if self.index_image == 0:
            self.label_image.grid_forget()
            button_back = Button(window_place, text="Back", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                                 command=lambda: self.forward(window_place, list_images),
                                 state="disabled")
            status_label = Label(window_place, text=constants.name_players[self.index_image], bd=3, fg='#70CF83',
                                 relief=SUNKEN, anchor=E, bg="#936554")
            self.label_image = Label(window_place, image=list_images[self.index_image])
            status_label = Label(window_place, text=constants.name_players[self.index_image], bd=3, fg='#70CF83',
                                 relief=SUNKEN, anchor=E, bg="#936554")
        else:
            button_back = Button(window_place, text="Back", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                                 command=lambda: self.back(window_place, list_images))
            self.label_image.grid_forget()
            # put now next image with buttons
            self.label_image = Label(window_place, image=list_images[self.index_image])
            status_label = Label(window_place, text=constants.name_players[self.index_image], bd=3, fg='#70CF83',
                                 relief=SUNKEN, anchor=E, bg="#936554")  # se va intinde de la vest la est
        self.label_image.grid(row=0, column=0, columnspan=3)  # want the image to include all buttons
        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        button_exit.grid(row=1, column=1)
        status_label.grid(row=2, column=0, columnspan=3, sticky=W + E)

    def create_commands(self, window_place):  # window place is root
        # create the buttons
        # global index_image
        # index_image = 0
        images_list = self.create_list_images()
        button_forward = Button(window_place, text="Next", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                                command=lambda: self.forward(window_place, images_list))
        button_back = Button(window_place, text="Back", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                             command=lambda: self.back(window_place, images_list), state="disabled")
        button_exit = Button(window_place, text="Exit", foreground="#3EA8B9", bg="#ddd", padx=10, pady=10,
                             command=window_place.quit)

        # create labels to put image
        self.label_image = Label(image=images_list[0])

        # put these on the grid
        self.label_image.grid(row=0, column=0, columnspan=3)  # want the image to include all buttons
        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        button_exit.grid(row=1, column=1)

        # create label for name(status bar)
        status_label = Label(window_place, text=constants.name_players[0], bd=3, fg='#70CF83', relief=SUNKEN, anchor=E,
                             bg="#936554")
        status_label.grid(row=2, column=0, columnspan=3, sticky=W + E)  # se va intinde de la vest la est
        # return label_image

    def run_application(self):
        root = Tk()
        root.title("Fifa 23 best career team")
        root.iconbitmap(r"G:\pycharm\pythonProject\TkinterBasic\fifa23careerApp\Icons-Land-Sport-Soccer-Ball.ico")
        self.create_commands(root)
        root.mainloop()
