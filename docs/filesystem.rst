filesystem
========

find_ext_files
--------
::

def find_ext_files(dir_name, ext):
  """ Find all file with specific extension under designated directory.

  """

  **Arguments**

  dir_name: path of the designated directory

  ext: specific file extension


overwrite_dir
--------
::

def overwrite_dir(dir_name):
  """ Create a directory, and delete it first if exist.

  """

  **Arguments**

  dir_name: path of the directory


check_mkdir
--------
::

def check_mkdir(dir_name):
  """ if directory not exist, create the directory

  """

  **Arguments**

  dir_name: path of the directory


batch_rename_files
--------
::

def batch_rename_files(input_dir, save_dir, ext='.png', start_num=0, filename_len=5):
  """ Rename all files with specific extention in an input directory to another directory with ordering numbers.

  """

  **Arguments**

  input_dir: directory that interested files in

  save_dir: directory to save renamed files

  ext: interested file extension

  start_num: start number for first file

  filename_len: length of renamed filename



batch_uuid_rename
--------
::

def batch_uuid_rename(input_dir, save_dir, ext=".png"):
  """ Rename all files with specific extension in an input directory to another directory with uuid string as filename.

  """

  **Arguments**

  input_dir: directory that interested files in

  save_dir: directory to save renamed files

  ext: interested file extension


is_image_file
--------
::

def is_image_file(filename):
  """ Check given filename is an image or not. Extensions of image file include: ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP', 'tif', 'TIF', 'tiff', 'TIFF',]

  """

  **Arguments**

  filename: name or path of given file
