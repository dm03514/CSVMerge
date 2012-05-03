from csv import DictReader, writer
from datetime import date
import os


def merge_csvs(csv_to_merge_list, save_to_path=os.path.dirname( __file__ )):
  """
  Takes a list of csv filepaths to merge.  Saves a combined file 
  in the current directory.
  """
  file_handlers_list = []
  headings = None
  for csv_dir in csv_to_merge_list:
    try:
      f = open(csv_dir, 'r')
    except IOError:
      print 'Error opening up file %s' % (csv_dir)
      return

    reader = DictReader(f)

    if not headings:
      # should only be on the first run
      headings = reader.fieldnames

    # verify fieldnames match up.
    if headings != reader.fieldnames:
      print 'Fields do not match up' 
      return
    file_handlers_list.append(f)

  # create a new file
  with open('%s/combined_%s.csv' % (save_to_path, date.today()), 'w') as perm_file:
    csv_writer = writer(perm_file)
    csv_writer.writerow(headings)
    for file_handler in file_handlers_list:
      # write the headings using the csv_writer but after that just feed in
      # the lines.  Everything should match up.
      for line in file_handler:
        perm_file.write(line)
      #for line_dict in reader:
      #csv_writer.writerow([line_dict[heading] for heading in headings])

