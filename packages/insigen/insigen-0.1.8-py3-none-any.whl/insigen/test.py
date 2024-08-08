
import os
import pickle
this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl
data_path = os.path.join(this_dir, 'Data/')
data = pickle.load(open(data_path + 'embeds.pickle', 'rb'))