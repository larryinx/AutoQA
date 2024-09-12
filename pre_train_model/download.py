
from modelscope import snapshot_download

qwen = snapshot_download('qwen/Qwen-7B-Chat', local_dir='./pre_train_model/Qwen-7B-Chat')
m3e = snapshot_download('AI-ModelScope/m3e-large', revision='master', local_dir='./pre_train_model/m3e-large')
bge = snapshot_download('AI-ModelScope/bge-large-zh-v1.5', local_dir='./pre_train_model/bge-reranker-large')
