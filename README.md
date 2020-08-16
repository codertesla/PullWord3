# PullWord3

A Python 3 Client for PullWord

![Python 3.5](https://img.shields.io/badge/python-v3.7-blue)![Python 3.5](https://img.shields.io/badge/python-v3.6-blue)![Python 3.7](https://img.shields.io/badge/python-v3.7-blue)![Python 3.8](https://img.shields.io/badge/python-v3.8-blue)


## What's PullWord

> PullWord:永久免费的基于深度学习的中文在线抽词

[PullWord Website](http://pullword.com/)

## PullWord API

<http://api.pullword.com/>



## What's PullWord3 (Python)

> A Python3 Client for PullWord


## How to use PullWord3 (Python)

```
from pullword3 import pullword
sentence = '这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。'
print(pullword(sentence,))
```

## Output

```
[{'t': '这是', 'p': '0.821296'}, {'t': '一个', 'p': '1'}, {'t': '伸手不见五指', 'p': '0.976794'}, {'t': '不见', 'p': '0.831597'}, {'t': '五指', 'p': '0.976527'}, {'t': '黑夜', 'p': '1'}, {'t': '我叫', 'p': '0.895989'}, {'t': '孙悟空', 'p': '0.801972'}, {'t': '我爱北京', 'p': '0.968947'}, {'t': '北京', 'p': '0.856976'}, {'t': '我爱', 'p': '1'}, {'t': 'python', 'p': '1'}]
```

## Similar Projects
* pullword Golang <https://github.com/tiantour/pw>
* pullword Python2 <https://github.com/binhe22/pullword>

## Author
PullWord3 @[CoderTesla](https://github.com/codertesla) , Released under the MIT License.