from datetime import time

from snownlp import SnowNLP

s = SnowNLP(u"今天我很快樂。你怎么樣呀？");
print("[words]",s.words); # 分詞
time.sleep(1)
