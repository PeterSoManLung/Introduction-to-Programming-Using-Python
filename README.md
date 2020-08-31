## Review
#### 內置數據類型 (Python)
1. Text Type (str) <code>e.g. "Hello", 'a'</code>
2. Numeric Type (int, float, complex) <code>e.g. 1, 1.2, 0.008</code>
3. Boolean Type (bool) <code>True, False</code>
##### 內置數據類型--尚未講
4. Sequence Type 
5. Mapping
6. Set 
7. Binary 

#### 如何輸出東西至顯示屏

<strong>輸出文字</strong>
```python
print("你好")
```
<strong>輸出數字--整數/浮點數</strong>
```python
print(10)
```
<strong>顯示數據類型</strong>
```python
print(type("Hello"))
print(type(1))
```

#### 如何輸入數據

<strong>獲取輸入數據步驟</strong>
1. 先創建一個常數 e.g. <code>input</code>
2. 利用 <code>input</code> (你所創建的常數)來儲存你輸入的值 e.g. <code>input = input("Message")</code>

```python
input = input("Message show on screen")
```

#### 如何轉換輸入值為數字類
<strong>方法 1 -- eval()</strong>
<br/>
```python
input = eval(input("Integer"))
```
<strong>方法 2 -- int()</strong>
<br/>
```python
input = input("Integer")
convert_int = int(input)
```

#### if..else
```python
if 條件:
  # 做仼何東西，當符合條件時
else:
  # 做仼何東西，當不符合條件時
```

#### if..elif..else
```python
if 條件1:
  # 做仼何東西，當符合條件1時
elif 條件2:
  # 做仼何東西，當符合條件2時
else:
  # 做仼何東西，當不符合條件1,2時
```
> <code>elif</code> 可以使用多次 e.g. <code>if..elif..elif..elif..else</code>

## Practice question from Introduction to Programming Using Python
標題係主要練嘅嘢**但**有啲題目有機練幾樣嘢<br/>
&#x1F534; Ching唔好睇答案做完run到program無error先睇


#### CH1 Question File
* 練Input & Output (輸入輸出)
  1. CH1.1
  2. CH1.2 (有機用到 ***for loop***)
  3. CH1.8 (要用到 ***運算***)
  4. CH1.9 (要用到 ***運算***)

* 練 for loop (for 迴圈)
  1. CH1.3 (要用到 ***Output***, 有機用到 ***if..else..***)
  2. CH1.4 (要用到 ***Output***, 有機用到 ***if..else..***)

* 練運算
  1. CH1.5 (要用到 ***Output***)
  2. CH1.7 (有機用到 ***for loop***)

* 練 if..elif..else (判定)
  1. CH1.6 (要用到 ***Output***, ***運算***, ***for loop***)
  
