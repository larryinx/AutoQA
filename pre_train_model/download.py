
from modelscope import snapshot_download

qwen = snapshot_download('qwen/Qwen-7B-Chat', local_dir='./pre_train_model/Qwen-7B-Chat')
m3e = snapshot_download('m3e-large', local_dir='./pre_train_model/m3e-large')
bge = snapshot_download('bge-reranker-large', local_dir='./pre_train_model/bge-reranker-large')
