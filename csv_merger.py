from csv import DictReader, writer
from datetime import date
import os


def merge_csvs(csv_to_merge_list, save_to_path=os.path.dirname( __file__ )):
  """
  Takes a list of csv filepaths to merge.  Saves a combined file in the current directory.
  """
  dict_reader_list = []
  headings = None
  for csv_dir in csv_to_merge_list:
    try:
      f = open(csv_dir, 'r')
    except IOError:
      print 'Error opening up file %s' % (csv_dir)
      return

    reader = DictReader(f)

    if not headings:
      headings = reader.fieldnames
    else:
      # verify fieldnames match up.
      if headings != reader.fieldnames:
        print 'Fields do not match up' 
        return
    dict_reader_list.append(reader)

  # create a new file
  with open('%s/combined_%s.csv' % (save_to_path, date.today()), 'w') as perm_file:
    csv_writer = writer(perm_file)
    csv_writer.writerow(headings)
    for reader in dict_reader_list:
      # Make Sure that we retain the heading order, there has to be a better way to do this.
      for line_dict in reader:
        csv_writer.writerow([line_dict[heading] for heading in headings])

