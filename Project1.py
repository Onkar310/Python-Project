# /*=======================================================================================================
#   Developed by: Onkar Sangale
#                 onkarsangale135@gmail.com
#                 'Python' Programming.
#                 Sem 2, 2022.Project
#                 Vishwakarma Institute of technology,pune
#                 Project on:-  image manipulation using pillow
#   =======================================================================================================
print("\n=======================================================================================================")

print("\n=============================IMAGE MANIPULATION USING PILLOW===========================================")

print("\n=======================================================================================================")

print("                             +-------------+-------------------------+")
print("                             |    Sr.No    |      Manipulation       |")
print("                             +-------------+-------------------------+")
print("                             |      1.     |        Compress image   |")
print("                             |      2.     |        Rotate image.    |")
print("                             |      3.     |        Apply filter     |")
print("                             |      4.     |        Crop Image       |")
print("                             |      5.     |        Exit             |")
print("                             +-------------+-------------------------+")
choice = int(input("                                     Choice:"))
match choice:
    case 1:
        import PIL
        from PIL import Image, ImageFilter
        from tkinter.filedialog import *
        file_path = askopenfilename()
        img = PIL.Image.open(file_path)
        myHeight, myWidth = img.size
        img = img.resize((myHeight, myWidth), Image.LANCZOS)
        save_path = asksaveasfilename()
        img.save(save_path + "compressed.jpg")
    case 2:
        import PIL
        from PIL import Image, ImageFilter
        from tkinter.filedialog import *
        file_path = askopenfilename()
        img = PIL.Image.open(file_path)
        img.rotate(180).show()
        save_path = asksaveasfilename()
        img.save(save_path + "compressed.jpg")
    case 3:
        import PIL
        from PIL import Image, ImageFilter
        from tkinter.filedialog import *
        file_path = askopenfilename()
        img = PIL.Image.open(file_path)
        img.filter(ImageFilter.EMBOSS).show()
        save_path = asksaveasfilename()
        img.save(save_path + "compressed.jpg")
    case 4:
        import PIL
        from PIL import Image, ImageFilter
        from tkinter.filedialog import *
        file_path = askopenfilename()
        img = PIL.Image.open(file_path)
        area = (200, 50, 420, 300)
        img.crop(area).show()
        save_path = asksaveasfilename()
        img.save(save_path + "compressed.jpg")
    case 5:
        exit
