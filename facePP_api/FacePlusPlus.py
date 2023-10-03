# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import time
import os

MAX_RETRY = 5

http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "Fill in your key"
secret = "Fill in your secret key"
filepath = "./datasetForTesting"

for root, dirs, files in os.walk(filepath):
    for file in files:
        path = os.path.join(root, file)
        boundary = '----------%s' % hex(int(time.time() * 1000))
        data = []
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
        data.append(key)
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
        data.append(secret)
        data.append('--%s' % boundary)
        fr = open(path, "rb")
        data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
        data.append('Content-Type: %s\r\n' % 'application/octet-stream')
        data.append(fr.read())
        fr.close()
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
        data.append('0')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
        data.append(
            "gender,age,ethnicity")
        data.append('--%s--\r\n' % boundary)

        for i, d in enumerate(data):
            if isinstance(d, str):
                data[i] = d.encode('utf-8')

        http_body = b'\r\n'.join(data)

        # build http request
        req = urllib.request.Request(url=http_url, data=http_body)

        # header
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

        # try to send request for MAX_RETRY times
        for i in range(MAX_RETRY):
            try:
                # post data to server
                resp = urllib.request.urlopen(req, timeout=5)
                # get response
                qrcont = resp.read()
                # if you want to load as json, you should decode first,
                # for example: json.loads(qrount.decode('utf-8'))
                with open('result.txt', 'a+') as f:
                    f.write(path + "\n")
                    f.write(qrcont.decode('utf-8') + '\n')
                print(qrcont.decode('utf-8'))
            except urllib.error.HTTPError as e:
                print(e.read().decode('utf-8'))
                time.sleep(1)
                continue
            else:
                break