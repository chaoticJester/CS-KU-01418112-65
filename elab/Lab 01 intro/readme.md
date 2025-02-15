# Lab 01 intro

### ยินดีตอนรับสู่ CS39 *นรก* 🔥 ขุมแรกของการเรียน CS

โดย lab 00 intro คือ lab ที่จะอธิการใช้ elab และ วิธีการเขียน python นิดหน่อย แบบนิดหน่อยจริงๆอะนะ
 
#### โดยมันจะมีห้วข้อ 5 หัวข้อ
1.  [อธิบายระบบตรวจคำตอบอัตโนมัติ](#1-อธิบายระบบตรวจคำตอบอัตโนมัติ)
2.  [อธิบายระบบคำตอบแบบตรวจเองและกึ่งอัตโนมัติ](#2-อธิบายระบบคำตอบแบบตรวจเองและกึ่งอัตโนมัติ)
3.  [วิธีที่ดู Submit และ Result ของ sumit นั้นๆ](#3-วิธีที่ดู-Submit-และ-Result-ของ-sumitนั้นๆ)
4.  [การเขียน Python แบบขนมเบื้องต้น : Variable and Basic Output](#4-การเขียน-Python-แบบขนมเบื้องต้น-Variable-and-Basic-Output)
5.  [การเขียน Python แบบขนมเบื้องต้น : Expression](#5-การเขียน-Python-แบบขนมเบื้องต้น-Expression)

## 1. อธิบายระบบตรวจคำตอบอัตโนมัติ

### elab คืออะไร
E-Labsheet หรือ elab คือ เว็บไซต์สำหรับทำแบบฝึกหัดและข้อสอบ เว็บไซต์มีการเฉลยคำตอบให้ผู้สอนทราบผลทันที หรือ ส่งคำตอบแล้วจารเอาไปตรวจเอง

### โดยระบบที่เราจะใช้หลักๆคือ 
#### กล่องเหลือง (ตรวจauto) และ กล่องฟ้า (ตรวจกึ่งauto/ตรวจมือ) 

###### แต่เราจะมาพูดถึงกล่องเหลืองก่อน

### กล่องเหลือง 🟨 คือกล่องรับคำตอบ auto โดย ถ้าเราใส่ตัวอักษรแล้วกด summit มันจะตรวจคำตอบพร้อมบอกคะแนนให้เลย
![กล่องเหลือง](./image%20folder/yellow.png)

#### วิธีดู Result
 โดยวิธีการดู Result คือ ชื่อหัวข้อนั้นจะมี คำว่า `Result` ตามด้วยสภาพนะว่าผ่านหรือติดปัญหาอะไรบ้าง ส่วนตัวของ `[p]` หากมีหลายข้อหรือหลาย test case ในelabนั้น สามารถกดได้ว่าเราผิดส่วนไหนผิดเพราะอะไร
![Result](./image%20folder/Result.png)

## 2. อธิบายระบบคำตอบแบบตรวจเองและกึ่งอัตโนมัติ

### กล่องฟ้า 🟦 คือ มี 2 แบบ  
1. รับคำตอบแบบตรวจเอง : จารไปตรวจเอง  
2. รับคำตอบกึ่งอัตโนมัติ : สามารถดูได้ว่าถูกแบบตรงเป็ะไหมถ้าไม่จารจะมาดูเอง

สามารถดูตามรูปเรียงลำดับลงมาได้เลย

<br>
![กล่องฟ้า](./image%20folder/blue.png)

## 3. วิธีที่ดู Submit และ Result ของ summit นั้นๆ

### Submit Result
#### ข้อมูลทดสอบ (test case) ในแต่ละ elab จะมี test case มากกว่า 1 ข้อเราสามารถตรวจว่าถูกได้หรือป่าว โดยการกดที่ icon ตรงนั้น 

![Explain results](./image%20folder/Explain%20results.png)

แล้วจะขึ้นว่าเราผิดอะไรบ้าง

![Explain results2](./image%20folder/Explain%20results%202.png)

#### รายละเอียดดังนี้
- P = Pass 
- F = Fail 
- S = Incorrect Spacing เว้นไม่ตรงเช่น hello world เป็น helloworld
- C = Incorrect case คำถูกแต่ตัวอักษรที่มีตัวใหญ่หรือตัวเล็กไม่ตรงกัน

## 4.การเขียน Python แบบขนมเบื้องต้น : Variable and Basic Output

### เรามาเรียน python 101 กันนนน 🍕

### Basic Output
#### โดนเราคงต้องอธิบายอะไรมากกนะ 


```python
x = "Hello World"
print(x)

# output : Hello World
```

ตัวแปรในภาษา python สามารถสร้างจากการ พิม `ชื่อตัวแปร = ข้อมูล`
ส่วนการนำค่าพวกนี้ออก สามารถทำโดยการ พิม `print(ชื่อตัวแปร)`

แค่นี้แหละทุกคนก็ไม่ยากได้อย่างที่คิดหรือป่าว 

### Data types

#### เรื่องนี้จะยากขึ้นมาหน่อย <br> Data type คือ ประเภทของข้อมูล เช่น ตัว C ก็จะเป็นตัวอักษร 14 เป็นตัวเลขจำนวนเต็ม 2.5 เป็นตัวเลยทศนิยม

#### โดยหลักๆที่เราควรรู้ :
1. integers(int) : ตัวเลขจำนวนเต็ม
2. float(float) : ตัวเลยทศนิยม
3. characters(str) : ตัวอักษรหรือช่วงตัวอักษรที่มารวมกัน

สามารถใช้ `type(ข้อมูล)` เพื่อหา type ของข้อมูลนั้นได้ ป.ล. ถ้าใช้ผ่านตัวย python สามารถเขียนได้เลย แต่ถ้าเขียนใน file ต้องใช้ `print(type(ข้อมูล))` ด้วยนะ

```python
>>> type("Hello")  # check the type of the literal "Hello"
<class 'str'>
>>> type(10)       # check the type of the literal 10
<class 'int'>
>>> type(10.0)     # check the type of the literal 10.0
<class 'float'>
>>> 
```

#### Variables

####  Variables ตัวแปร : ทำได้หลายอย่าง เช่น เขียนสมการลงตัวแปร เขียน function ลง ตัวแปร หรือ การสลับข้อมูลในตัวแปร

```python
#สามารถเขียนสมการได้ 
>>> total = 3+5+10    # variable 'total' is assigned to the value of the expression 3+5+10
>>> total             # 'total' is now an expression, which can be displayed using print()
18
>>> total/3           # or be part of another expression
6.0

#สามารถกำหนดหลายตัวได้พร้อมกัน
>>> x,y = 10,20       # x is assigned to 10, y is assigned to 20
>>> x
10
>>> y
20

#สามารถสลับตัวแปรได้
>>> x = y             # x points to the same object pointed by y, which is 20
>>> y = x             # y points to the same object pointed by x, which is now 20
>>> x
20
>>> y
20
>>> 
```

## 5. การเขียน Python แบบขนมเบื้องต้น : Expression

#### จากนี้อาจจะงงหน่อยๆ 

### data หรือ var ที่มี data นั้นสามารถถูกเครื่องหมายทางคณิตศาสตร์มาได้แม้ว่าจะเป็น char ก็ตาม

```python
#ตัวเลขก็ทำได้ แต่หากหารจะเปลี่ยนเป็น float แทน
>>> 3+5+10   # 3+5+10 forms a new expression with value 10 and type 'int' 
18
>>> type(3+5+10)
<class 'int'>
>>> 3+5+10/3    # this expression equals 3+5+(10/3) because '/' has precedence over '+' 
11.333333333333334
>>> (3+5+10)/3  # to compute the correct average, parentheses must be used 
6.0

#char ก็ทำได้
>>> "Hello" + "World"  # use '+' with strings to join them together 
'HelloWorld'
>>> "Hello" * 3  # use '*' with a string to repeat the same string multiple times 
'HelloHelloHello'
>>> "Hello" + 3  # ถ้าทำข้ามdata typeจะมีแค่ * กัย in เท่านั้นนะ 

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    "Hello" + 3
TypeError: must be str, not int
>>> 
```

### เรื่องผิดบ่อย ควรระวัง ขโมยมาค่อนข้างดีถ้าว่างอะ แต่แม่งยาวไม่ต้องอ่านเถอะ
- จำลำดับการทำงานของตัวดำเนินการทางคณิตศาสตร์ผิด (** ทำก่อน * / // % - ทำก่อน + -) ⚠️
- ลืมใส่ * สำหรับการคูณ
- ลืมว่าการดำเนินการระหว่างจำนวนเต็มกับจำนวนจริง - จะได้ผลลัพธ์เป็นจำนวนจริง ⚠️
- เข้าใจผิดเรื่องการบวก การบวกของจำนวน ไม่เหมือนกับ การบวกของสตริง ⚠️
- นำข้อมูลที่ไม่ใช่สตริงมาบวกกับสตริง ⚠️
- ลืมความแตกต่างของ / กับ // กับ % ⚠️
- 1e3 ไม่ใช่จำนวนเต็ม 1000 และเป็นจำนวนจริง 1000.0 
- k++ หรือ k-- ทำใน python ไม่ได้ ให้ใช้ k += 1 หรือ k -= 1
- ++k หรือ --k ไม่ทำให้ k เปลี่ยนค่าไป
- ลืม import math เมื่อใช้ฟังก์ชันของ math
- ใส่วงเล็บเปิดหรือวงเล็บปิด ไม่ครบคู่ ⚠️
- สะกดชื่อตัวแปรผิด หรือผิดเรื่องการใช้ตัวเล็กกับตัวใหญ่ ⚠️
- ตั้งชื่อตัวแปรซ้ำกับคำสงวน ⚠️

