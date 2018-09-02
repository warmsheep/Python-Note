## web框架本质
HTTP:
 无状态，短连接
TCP：
  不断开

WEB应用（网站）：
HTTP协议：
发送
  请求头+请求体
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: PSTM=1481910936; BIDUPSID=35D7F6F2472C8B3B84F6DE652D51F573; FP_UID=2f4c6d6c09cb7acba2f6ef5c75d78b1d; BDUSS=dEd25IbUZDRW9ZaDZvSXRrT0hjMEpBSGZRRWZhZW1Cfm41NGJLZVpVZ1dLYWhaSVFBQUFBJCQAAAAAAAAAAAEAAADWcAALztLDx7XE0MTUvLaoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABacgFkWnIBZbG; IK_CID_74=15; IK_CID_1031=2; IK_D6B1263EDC4E7A98BDCF3D6F233F6A9A=29; IK_CID_1=1; BAIDUID=989BA05982934B9E567A14872EB99CF4:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=2; H_PS_PSSID=1460_21085_26350_26924_20927; BDSFRCVID=FTIsJeCCxG3w24377nuqMSPzErBTF9vvRq-x3J; H_BDCLCKID_SF=tJPfoC-KfCP3fP36q6--jtLOMqOybD62aKDs3lRp-hcqEIL45Ic2MfLgjpQxLxDL-6nfQKjMy66AqxbSj4Qz2-KY5UuOJ4rNLKn2Bh7H5l5nhMJeb67JDMP0-xKH0-6y523ion6vQpn-HxtuDj0MDTJBjGDsK43tHJID3-bOHJOoDDv1Kfb5y4LdjG5zWjcAbHPf_Kblt4bRjM3ehj3z0xFH3-Aq5xc8bejZ2qR5XhubSJc_b-rEQfbQ0hQPqP-jW5ILKqOzKb7JOpkxhfnxybKV0aCHJ58qJnAe_Kv5b-0_JRnYK-r_q4tehHRlLUceWDTm5-nTt-0KMK86jPThKfu90h64bfjn3J5qLfohH4P5OCcnK4-Xj5O0DaJP; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1535460168,1535593317,1535594526,1535594544; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1535594588
Host: zhidao.baidu.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
  （get和post的区别）
响应
  响应头+响应体
  Access-Control-Allow-Headers: X-ik-ssl,X-ik-token,X-ik-utdata
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html
Date: Thu, 30 Aug 2018 02:03:30 GMT
Server: Apache
Transfer-Encoding: chunked
Vary: Accept-Encoding
Wait: 2

浏览器（socket客户端）
 2.www.cnblogs.com(42.121.252.58,80)
   sk.connect()
   sk.send('打开')
 5.接收
 6.连接断开
博客园（socket服务端）
1.监听ip和端口(42.121.252.58,80)
while True:
  用户=等待用户连接
  3.收到"打开"
  4.响应：’好‘


str(data,encoding='utf-8')
bytes('ads',encoding='utf-8')
