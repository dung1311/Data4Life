from tkinter import *
from tkinter import filedialog
import os
import PIL
from PIL import Image, ImageTk
import count
import cv2


def getPath():
    file_path = filedialog.askopenfilename(title="Chọn một hình ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path == '':
        #print('chua lay duoc file_path')
        pass
    else:
        #print('da lay duoc file_path' + str(file_path))
        count.result(file_path)

def show_boxes():
    file_path = filedialog.askopenfilename(title="Chọn một hình ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path == '':
        #print('chua lay duoc file_path')
        pass
    else:
        #print('da lay duoc file_path' + str(file_path))
        count.result_without_label(file_path)


def main():
    root = Tk()
    root.geometry("")
    root.title("Đếm số phương tiện")
    root.configure(background = '#9F2B68')

    img = ImageTk.PhotoImage(Image.open("../imgs/background1.png"))
    label = Label(root, image = img)
    label.pack()
    btn1 = Button(root, text= "Image", background = '#34e8eb', foreground= 'black', command=getPath, width=10, height=4)
    btn1.place(x = 10, y = 10)
    btn2 = Button(root, text='Boxes', bg= '#34e8eb', fg= 'black', command=show_boxes, width=10, height=4)
    btn2.place(x = 200, y = 10)
    
    
    root.mainloop()

if __name__ == '__main__':
    main()

