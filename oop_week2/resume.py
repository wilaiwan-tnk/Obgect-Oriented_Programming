a = input("โปรดกรอกชื่อ \n")
b = input("โปรดกรอกอายุ \n")
c = input("โปรดกรอกรหัสบัตรประจำตัวนักเรียน\n")
d = input("โปรดกรอกชั้นปี \n")
e = input("โปรดกรอกชื่อเล่น \n")
f = float(input("โปรดกรอกส่วนสูง \n"))
g = float(input("โปรดกรอกน้ำหนัก \n"))
s = f+g
print('ชื่อ' +a+ 'อายุ' +str(b)+'ปี')
print('รหัสประจำตัวนักเรียน'+c+'ชั้นปี'+(d)+'')
print('ชื่อเล่น'+e)
print('ส่วนสูง: '+str(f)+'เซนติเมรต' 'น้ำหนัก:'+str(g)+'กิโลกรัม')
print('ส่วนสูง+น้ำหนัก='+str(s))