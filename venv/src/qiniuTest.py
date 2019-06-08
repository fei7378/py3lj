from qiniu import Auth, put_file, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
# 七牛云：
# AccessKey：SacmOCm2cAQ2w_ajo-3qRfVsBNyPHrZ8qtDZaU2i
# SecretKey：F1laHwEwAzGXbcgvb2-MLgtRauIP45xoP4cg0T5G
#
# 阿里云
# AccessKey：LTAIjCIpztP4nnKf
# SecretKey：acNkXT5ZDvVp9aFRYuvaNkhIcbYMjD
access_key = 'SacmOCm2cAQ2w_ajo-3qRfVsBNyPHrZ8qtDZaU2i'
secret_key = 'F1laHwEwAzGXbcgvb2-MLgtRauIP45xoP4cg0T5G'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'hrxx2019'
#上传后保存的文件名
key = 'SOTTR_Wallpaper_3840x2160.jpg'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
localfile = '/home/feiyc/SOTTR_Wallpaper_3840x2160.jpg'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)