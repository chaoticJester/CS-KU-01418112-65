# 02 Python List Index

# index = ลำดับของข้อมูลเริ่มจาก 0 ถึง n-1

# 1. ประกาศ List ของจำนวนเฉพาะ ให้ชื่อตัวแปรว่า primes โดยมีข้อมูลเป็นจำนวนเฉพาะ 10 จำนวนแรก
# คำนวณหาผลรวมของจำนวนเฉพาะทั้ง 10 จำนวน โดยใช้ while loop เก็บผลรวมใส่ในตัวแปร total

primes = [2,3,5,7,11,13,17,19,23,29] #ใช้จากข้อแรก
i = 0
total = 0
while i < 10:
    total += primes[i] # การเรียนกใช้ข้อมูลต้องใส่ index เพื่อหาตำแหน่งข้อมูลที่ต้องการ 
    i += 1
print(total)

'''2. กำหนด List months และ days_in_month เป็น List ของตัวย่อชื่อเดือน และ List ของจำนวนวันในแต่ละเดือนตามลำดับ
ให้แสดง 12 บรรทัด ว่าแต่ละเดือนมีกี่วัน โดยใช้ while loop โดยแสดงชื่อเดือนและจำนวนวัน คั่นด้วยช่องว่าง'''

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i = 0
while i < 12:
    print(months[i], days_in_month[i])
    i += 1
