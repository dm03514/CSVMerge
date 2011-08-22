from csv import DictReader, writer
from datetime import date
from tempfile import TemporaryFile


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
  with TemporaryFile() as temp_file:
    csv_writer = writer(temp_file)
    for reader in dict_reader_list:
      csv_writer.writerows(line_dict.values() for line_dict in reader)

    #import ipdb; ipdb.set_trace() 
    temp_file.seek(0)
    perm_file = open('combined_%s.csv' % (date.today()), 'w')
    perm_file.write('%s\r\n' % (','.join(headings)))
    perm_file.writelines(line for line in temp_file)
    perm_file.close()


merge_csvs(['test.csv', 'test1.csv'])

