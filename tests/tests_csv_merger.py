from csv import DictReader, writer
from csv_merger import merge_csvs
from datetime import date
from shutil import rmtree
import os
import unittest

class TestCSVMerger(unittest.TestCase):

  def setUp(self):
    self.temp_dir = 'tmp'
    os.mkdir(self.temp_dir)
    
  def test_merge_csvs_success(self):
    """Tests we can successfully merge 2 csv files"""
    # make 2 temp csv files so we have something to combine
    files_to_open_list = []
    for i in range(2):
      headings_list = ['Heading1', 'Heading2', 'Heading3', 'Heading4']
      files_to_open_list.append('%s/csv%s.csv' % (self.temp_dir, i))
      with open('%s/csv%s.csv' % (self.temp_dir, i), 'w') as f:
        csv_writer = writer(f)
        csv_writer.writerow(headings_list)
        csv_writer.writerow([i, i, i, i])
        csv_writer.writerow([i, i, i, i])
 
    merge_csvs(files_to_open_list)
    # open the outputted csv file and make sure it has the right headings
    f = open('combined_%s.csv' % (date.today()), 'r')
    dict_reader = DictReader(f)
    self.assertEqual(len(dict_reader.fieldnames), 4)
    lines_list = [line for line in dict_reader]
    self.assertEqual(len(lines_list), 4)

  def tearDown(self):
    rmtree(self.temp_dir)
    os.remove('combined_%s.csv' % (date.today()))

if __name__ == '__main__':
  unittest.main()
  
