print('โปรแกรมคำนวนเกรด')
a = int(input('โปีดใส่คะแนน : '))
if a < 0 or a > 100 :
    print('กรอกดีๆ')
elif a >= 80 :
    print('เกรด4')
elif a >= 70 :
    print('เกรด3')
elif a >= 60 :
    print('เกรด2')
elif a >= 50 :
    print('เกรด1')
else :
    print('ตกไปเหอะ')
    print('เราจะให้โอกาสคุณแก้ โปรดเลือก 1 หากไม่ต้องการเลือก 2')
    c = int(input('เลือก : '))
    if c == 1:
        d = 50 - a 
        print(f'คุณจะขาดคะแนน{d}')
    elif c == 2:
        print('ตกไปเถอะค่ะ')
    else:
        print('1 หรือ 2 อย่ากวนตีน')