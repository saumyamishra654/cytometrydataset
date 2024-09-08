import os

def rename_lrn_to_tsv(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.lrn'):
            new_filename = filename.replace('.lrn', '.tsv')
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")

folder_path = '/Users/saumyamishra/Desktop/intern/cytometry/CytoDataset/MarburgData/02BM_vs_leukemia/Target'
rename_lrn_to_tsv(folder_path)
