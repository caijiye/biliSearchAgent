import get_data
from pprint import pprint
key="神经网络"
page=1
datas=get_data.get(key,page)
pprint(datas)
