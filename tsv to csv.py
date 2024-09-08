import os
import csv
import pandas as pd

def convert_all_tsv_to_csv(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.tsv'):
            tsv_file = os.path.join(folder_path, filename)
            csv_file = os.path.join(folder_path, filename.replace('.tsv', '.csv'))

            with open(tsv_file, 'r') as tsv_in, open(csv_file, 'w', newline='') as csv_out:
                tsv_reader = csv.reader(tsv_in, delimiter='\t')
                csv_writer = csv.writer(csv_out)

                for row in tsv_reader:
                    if row and not row[0].startswith(('#')):
                        csv_writer.writerow(row)

            print(f"converted: {filename} -> {filename.replace('.tsv', '.csv')}")

folder_path = '/Users/saumyamishra/Desktop/intern/cytometry/CytoDataset/MarburgData/02BM_vs_leukemia/Target'
convert_all_tsv_to_csv(folder_path)


