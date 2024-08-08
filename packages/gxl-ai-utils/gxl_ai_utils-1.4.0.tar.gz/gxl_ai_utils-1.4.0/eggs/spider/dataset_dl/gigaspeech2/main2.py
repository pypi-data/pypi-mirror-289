import os
import webdataset as wds
from huggingface_hub import HfFileSystem, get_token, hf_hub_url
import subprocess

fs = HfFileSystem()
files = [fs.resolve_path(path) for path in fs.glob("hf://datasets/speechcolab/gigaspeech2/**/train/*.tar.gz")]
urls = [hf_hub_url(file.repo_id, file.path_in_repo, repo_type="dataset") for file in files]
local_dir = "./home/work_nfs10/xlgeng/data/gigaspeech2/train"
os.makedirs(local_dir, exist_ok=True)

for url in urls:
    filename = url.split("/")[-1]
    print(url)
