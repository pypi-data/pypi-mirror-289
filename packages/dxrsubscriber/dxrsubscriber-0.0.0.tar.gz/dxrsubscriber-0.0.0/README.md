# ZMQ Subscriber

A ZMQ subscriber for receiving and decoding video streams.

## Installation

```sh
pip install zmq_subscriber

from zmq_subscriber import ZmqSubscriber

subscriber = ZmqSubscriber("tcp://localhost:5555")
img, topic = subscriber.pull()
if img is not None:
    subscriber.show(img, "5555")
subscriber.close()


### 6. 生成分发包

在项目根目录下运行以下命令生成分发包：

```sh
python setup.py sdist bdist_wheel
