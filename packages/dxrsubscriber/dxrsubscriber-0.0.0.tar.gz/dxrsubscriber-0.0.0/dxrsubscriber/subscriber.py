#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 8:54
# @Author  : wangqinggang
# @Email   : wqg1993@qq.com
# @File    : subscriber.py
import cv2
import zmq
import av
import os
import sys

class DxrSubscriber:
    def __init__(self, zmq_url, codec='h264', mode='r', result=True):
        self.zmq_url = zmq_url
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.RCVHWM, 1000)  # High Water Mark
        self.socket.connect(self.zmq_url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages
        self.decoder = av.codec.CodecContext.create(codec, mode)
        self.decoder.options = {'strict': 'experimental'}
        self.null_fd = os.open(os.devnull, os.O_WRONLY)
        self.old_stderr = os.dup(sys.stderr.fileno())
        self.result = result
        os.dup2(self.null_fd, sys.stderr.fileno())

    def pull(self):
        try:
            if self.result:
                topic, data = self.socket.recv_multipart()
            else:
                topic, data = self.socket.recv()
            packet = av.packet.Packet(data)
            if packet.size < 1000:
                return None, None
            try:
                frames = self.decoder.decode(packet)
            except Exception:
                frames = []
            for frame in frames:
                img = frame.to_ndarray(format='bgr24')
                return img, topic
        except zmq.ZMQError:
            pass
        except Exception:
            pass
        return None, None

    def close(self):
        self.socket.close()
        os.dup2(self.old_stderr, sys.stderr.fileno())
        os.close(self.null_fd)
        os.close(self.old_stderr)

    def show(self, img, port):
        cv2.namedWindow(f'received {port}', cv2.WINDOW_NORMAL)
        cv2.imshow(f'received {port}', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()
