from csv_merger import merge_csvs
import glob
import os
import Tkinter, Tkconstants, tkFileDialog


class CSVMerge(Tkinter.Frame):
  
  def __init__(self, root):

    Tkinter.Frame.__init__(self, root)

    self.directory = None

    button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

    Tkinter.Button(self, text='Choose Directory', command=self.ask_directory).pack(**button_opt)
    Tkinter.Button(self, text='Merge CSVs', command=self.merge_files_in_directory).pack(**button_opt)

    self.dir_opt = options = {}
    options['mustexist'] = True
    options['title'] = 'This is a title'
    options['parent'] = root


  def ask_directory(self):
    """Sets directory attribute as selected directoryname."""
    self.directory = tkFileDialog.askdirectory(**self.dir_opt)

  def merge_files_in_directory(self):
    """Merges all csv files in the specified directory"""
    if self.directory:
      input_list = [filename for filename in glob.glob(os.path.join(self.directory, '*.csv'))]
      merge_csvs(input_list, self.directory)

if __name__=='__main__':
  root = Tkinter.Tk()
  CSVMerge(root).pack()
  root.mainloop()
