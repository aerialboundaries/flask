from werkzeug.utils import secure_filename
import os, pathlib

p_file = 'ryoko.jpg'
print(p_file)

securefile = secure_filename(p_file)
print(securefile)