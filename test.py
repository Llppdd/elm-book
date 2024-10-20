import os.path

import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiTjhlSWlXclZfbnBYeTRrZFNpbUJhLS1URC1zZ2d5NjlzWXUwOFJUYWwtRkRvSmVQWEVuOGM3VVhzaVJfbHQ3NVRQcGVxemZMWGZVUXhkUkN0N1BWZlduaDNsUkZiViIsImlhdCI6MTcyNjMyNTAyNSwiZXhwIjoxNzI4MDUzMDI1fQ.DcFUZmbmHIJltsTBXT7pP1BAmqLtjTAd1WlmvOnCTXbCDcvIDw6GWxMGnXvbaxCg",
    "sentry-trace": "347da9f2190e46c397c71dd79aab0320-b5d60d647ea45a05-0",
    "baggage": "sentry-environment=production,sentry-release=2.17.11,sentry-public_key=49b9ad1a6201bfe027db296ab7c6d672,sentry-trace_id=347da9f2190e46c397c71dd79aab0320,sentry-sample_rate=0.1,sentry-sampled=false",
    "Origin": "http://192.168.22.38:15700",
    "Connection": "keep-alive",
    "Referer": "http://192.168.22.38:15700/crontab",
    "Priority": "u=0"
}
cookies = {
    "46a615ae9ebc07b6a0a447b19219eb70_ssl": "155b224e-f5c1-40e4-abd5-f3f7536649da.GB8WuSwckeCpA-w8BIRpcbzFZyA",
    "dbcc6c349d5db269c40588106d459af9_ssl": "6805cf35-baa6-403b-ad19-faa0c8a4b40c.8_u4yJvc-a5HjNDIqNqe9Xq7Zzw",
    "701f5481bb70da08d30d509d1dca385d_ssl": "2b4069f2-f5dc-4e43-a9f6-03dc1d2729da.AKXK2M9Miu_H637gCk-XOKN-wOg",
    "0eab8e5b14bd0c2bb36fa762b9c3c3be_ssl": "18b73303-9d92-42f3-904b-bd8b51a7a082.5qq9XtZnWKxCoBiRMtdGOrNZ0ZA",
    "458b9a540aa40cab289022a5246f507d_ssl": "48887ba9-a9b3-4648-9cd5-a6675513536e.NLNoknnLoz587RT1fJHZNUybdQ4",
    "35b0eb072b86d64de94d17c037ced679_ssl": "24bfade4-9146-43dd-b53f-ac89e77254d6.bo90a_QEik4Y7lH3O9oQ7h2kvfM",
    "_ga_KMJJCFZDKF": "GS1.1.1726320679.1.1.1726321010.0.0.0",
    "_ga": "GA1.1.1923831622.1726320680",
    "NMTID": "00OCfCIvJXEKrak20nZkTWUQuCRIY4AAAGR8LvsXg",
    "__csrf": "ff3d97275f9e1548d6ca1f2d38723b7c",
    "MUSIC_U": "00F8CD1360A155E678A1BE889FC5617A052BBECF34BCB4A48E333C94ED530796EAD797AA479CB71B917859B1D281555638E96AFE97ADE85E86BE552F3787712BD897207B1BD75CCF15252F945CDA502F15CB8B56F560EB3141BE4B91F3E7B6EC4FAD103768BF937A080A8EB098224E70608DCDF7D11E28E37D9138D410EAA790303AE113DA914DBC73FD42D563D31FDD678FD7EC519067D366D967564F7CDE1AF37AD832652EC661007015243758024B498EB86BFED167CE5AF5812E32820233DCA3948F3E16945A276362562F1C9D12EC74B211B49EBF11F5B6091851367CFB7F1CF6A181379D4A74B5FDFB6A8D56008AF1205BC1D3CAF54E96075131AD2E69A4D7AF43CFA1EBE2CF1D10CBD79EA4F8A7C15200C1EC187993CE691092367ED0DD567EDE1C8DB66CB1CD83DBEEC8521FED65FCB4BCFF25967C9E55EED34C3F1F848748CF3BB7E4587E676853C6F0608791"
}
url = "http://192.168.22.38:15700/api/crons"
params = {
    "t": "1726323134766"
}

# 获取当前路径文件
import random

wj = [i for i in os.listdir(os.getcwd()) if i.endswith("js") or i.endswith("py")]
print(wj)
for i in wj:

    data = {
        "name": f"饿了么_{i.replace(".js", "").replace(".py", "")}",
        "command": f"task {i}",
        "schedule": f"0 {random.randint(1, 59)} {random.randint(1, 23)} ? * *"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

    print(response.text)
    print(response)
