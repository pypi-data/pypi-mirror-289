
from gxl_ai_utils.utils import utils_file

from datasets import load_dataset

for partiton in ['train', 'validation', 'test']:
    print(partiton)
    ds = load_dataset("speechcolab/gigaspeech2", split=partiton)
    save_dir = '/home/work_nfs10/xlgeng/data/gigaspeech2/' + partiton
    utils_file.makedir(save_dir)
    ds.save_to_disk(save_dir)

