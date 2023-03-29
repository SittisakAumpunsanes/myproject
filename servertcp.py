#ตัวอย่างการเขียน Server TCP เพื่อทดสอบการรับบริการจากลูกค้า
import socket
# from datetime import datetime
import time
s = socket.socket() # Create Obj Socket
print("Socket Success Created")
port = 12345 # Create port Number

s.bind(('',port))
print("Socket Binded To :: %s"%(port))
s.listen(5) # สร้าง listen เชื่อมต่อ
print("Socket is listening")

#สร่าง loop เพื่อรอการเชื่อมต่อจากลูกข่าย
while True:
    c,addr = s.accept()
    f=open('log1.txt','a+') # ทำการเปิดไฟล์เพื่อเขียนlog
    print('got connect from',addr)
    # Sand thank msg to the client
    d=time.ctime()
    # time=d.strftime("%H:%M.%S")
    waddr=str(addr) # แปลงหมายเลขไอพี เป็น String
    time1=str(d)
    f.write(time1+'\n')
    c.send(b'Thank You For Connecting')
    print("Time",d)
    c.close() # ปิดการเชื่อมต่อ
 
