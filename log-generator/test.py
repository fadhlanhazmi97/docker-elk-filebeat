import re
log = "{address space usage: 264302592 bytes/252MB} {rss usage: 36761600 bytes/35MB} [pid: 25987|app: 0|req: 9445220/52610067] 10.99.0.48 () {34 vars in 686 bytes} [Tue Aug 13 13:01:05 2019] GET /agent/platform/rewards/history/?chairman_id=147353&limit=2&request_id=68fb3354-bdca-11e9-bf3c-0242ac120002 => generated 72 bytes in 17 msecs (HTTP/1.1 503) 4 headers in 138 bytes (1 switches on core 0)"
pat = r"GET\s\/.*=|POST\s\/.*="
res = re.findall(pat,log)
print(res[0].split(" ")[1])