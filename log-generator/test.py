import re
log = "10.137.0.2 - - [22/Aug/2019:15:44:01 +0700] \"GET /api/mapan/binaan_list/?page=1 HTTP/1.1\" 500 98 0.041 \"-\" \"okhttp/3.12.1\" \"183.91.84.82\""
pat = r"GET.*HTTP|POST.*HTTP"
res = re.findall(pat,log)
print(res[0].split(" ")[1])