# -*- coding: utf-8 -*-
"""
todo: Documentation

    Project name: _Studi_
    File name: tkinter_base64_image-ico

    Date created: 30/12/2019
    Date last modified: 22/1/2020
    Status: Stable

    Python version: 3.8
    Modules required: pillow
"""
__author__ = 'Ariel Montes Nogueira'
__website__ = 'http://www.montes.ml'
__email__ = 'arielmontes1989@gmail.com'

__copyright__ = 'Copyright © 2020-present Ariel Montes Nogueira'
__credits__ = []
__license__ = '''
                Licensed under the Apache License, Version 2.0 (the "License");
                you may not use this file except in compliance with the License.
                You may obtain a copy of the License at

                    http://www.apache.org/licenses/LICENSE-2.0

                Unless required by applicable law or agreed to in writing, software
                distributed under the License is distributed on an "AS IS" BASIS,
                WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
                See the License for the specific language governing permissions and
                limitations under the License.'''
__recovery__ = 'https://github.com/Ariel-MN/Tkinter_base64_Images'
__version__ = '1.0'

from base64 import b64decode
from PIL import Image, ImageTk
from tkinter import Tk, PhotoImage, Label
from os import system, remove


# Binary encode image:
ico_b = b'R0lGODlhMAAwAHAAACH5BAEAAAEALAAAAAAwADAAgQAAAAAAAAAAAAAAAAK6jI+py+0Po5y0Wgny\n3Sh7wG2fF1ojWU4nmkKr1rpvLK/08' \
        b'4JpDuch/zH4REDU0FQ0zpDJ3hIWaSptgWCtKXyOcFTrYbhc\nhFlZanmrMJc7YTb6e0pDwfK3Gq4D6xK2O/yMRuYGxJCnBcUX54cXVyXIyL' \
        b'Ko9+j4BohY2WgJiXnp\n1OXF2cnp+dnZJjalKcgTZbhYGuoKKjXqMCnFtJqrG8jb61VUcnSTCltcityAqjxI2XwJffssXW19\nLV0AADs=\n'

# String encode image:
ico_s = """R0lGODlhMAAwAHAAACH5BAEAAAEALAAAAAAwADAAgQAAAAAAAAAAAAAAAAK6jI+py+0Po5y0Wgny3Sh7wG2fF1ojWU4nmkKr1rpvLK/084JpD
        uch/zH4REDU0FQ0zpDJ3hIWaSptgWCtKXyOcFTrYbhchFlZanmrMJc7YTb6e0pDwfK3Gq4D6xK2O/yMRuYGxJCnBcUX54cXVyXIyLKo9+j4BohY2
        WgJiXnp1OXF2cnp+dnZJjalKcgTZbhYGuoKKjXqMCnFtJqrG8jb61VUcnSTCltcityAqjxI2XwJffssXW19LV0AADs="""

# Tkinter program:
root = Tk()
root.title("Encoded Images")
root.geometry("260x50+605+160")  # window size and position

# Config and set icon:
tempfile = '$$_temp.ico'
icondata = b64decode(ico_s)

iconfile = open(tempfile, 'wb')  # create the file
iconfile.write(icondata)  # create the icon
iconfile.close()
icon = PhotoImage(file=tempfile)
root.tk.call('wm', 'iconphoto', root, icon)
remove(tempfile)  # delete the tempfile

# Config Image:
""" From Binary """
pic_bytes = b64decode(ico_b)  # trasform into bytes with Base64
image_1 = ImageTk.BytesIO(pic_bytes)  # create a pillow ImageTk from bytes

""" From String """
pic_bytes = b64decode(ico_s.encode())  # trasform into bytes with Base64
image_2 = ImageTk.BytesIO(pic_bytes)  # create a pillow ImageTk from bytes

""" Configuration """
pil_photo = Image.open(image_1)  # get the image with PIL Image
tk_photo = ImageTk.PhotoImage(pil_photo)  # convert to an image Tkinter can handle
label = Label(root, image=tk_photo).pack()  # display the image into tkinter interface

# Keep the program open:
root.mainloop()
