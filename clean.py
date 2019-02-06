import os

os.system('color A')



dir_path = os.path.dirname(os.path.realpath(__file__))
rel_path = '\import'
import_path = dir_path + rel_path

for root, dirs, files in os.walk(import_path):
    for file in files:
        os.remove(os.path.join(root, file))
print('Cleanup completed')
print('')