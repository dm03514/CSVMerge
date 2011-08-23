from csv import DictReader, writer
from datetime import date


def merge_csvs(csv_to_merge_list):
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
  with open('combined_%s.csv' % (date.today()), 'w') as perm_file:
    csv_writer = writer(perm_file)
    csv_writer.writerow(headings)
    for reader in dict_reader_list:
      csv_writer.writerows(line_dict.values() for line_dict in reader)
    perm_file.close()
    #import ipdb; ipdb.set_trace() 

merge_csvs(['50onred.csv', 'Firstand10.csv', 'Commission Junction.csv', 'WorkingPlanet.csv', 'test.csv', 'test1.csv', 'test2.csv', 'test3.csv'])

