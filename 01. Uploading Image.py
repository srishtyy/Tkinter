# Uploading Image using Tkinter 

from tkinter import *
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk

root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[(("Picture File","*.jpg;*.png;*.gif"))])  #opens only JPG, PNG or GIF images
img=Image.open(file_path)
file_names=str(int(time.time()))
print(file_names)
img.save("path/image_name.png")
tkimage=ImageTk.PhotoImage(img)
root.mainloop()
root1 = Tk()
    
    file_path = filedialog.askopenfilename(filetypes=[(("Picture File", "*.jpg;*.png"))])
    img = Image.open(file_path)
    img.save("C:/Users/9911v/PycharmProjects/Facial Emotion Detector/abc.png")
    tkimage = ImageTk.PhotoImage(img)
    root1.mainloop()
