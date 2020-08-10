# 0727 review

## 예외처리

* 문법 에러:문법적 오류가 있을때

* exception

  * NameError
  * TypeError
  * ValueError : `int('3.5')`
  * ZeroDivisionError
  * IndexError
  * KeyError
  * ModuleError
  * ImportError

* 예외 처리

  * try & except

    ```python
    try:
        <코드블럭 1>
    except 예외1: 
        <코드블럭 2>
    except 예외2, 예외3:
        <코드블럭 3>
    except 예외4 as err:
        print(f'{err}로 에러 메세지를 프린트 할 수 있다.')
    else: #코드블럭 1에서 에러가 발생하지 않았을때만 실행.
        <코드블럭 4>
    finally: #반드시 실행
        <코드블럭 5>
    ```

* 예외 발생

  * raise: 예외를 강제로 발생 `raise ValueError('숫자를 입력해주세요.')

  * assert: 예외를 강제로 발생

    * 상태를 주로 검증하기 위해서 `assert Boolean expression, error message`

      ```python
      assert type(x) == int,'숫자형이 아닙니다.'
      ```

      

## 데이터 구조

* 데이터 구조 : 데이터에 편리하게 접근을 하고, 그 값을 변경하기위해 데이터를 저장하거나 조작하는 방법
* 순서가 있는 구조(ordered)
  * 문자열, 리스트
* 순서가 없는 구조(unordered)
  * set, Dictionary



### 문자열



* 변경할수없다(immutable) / 순서가 있다 (ordered) / 순회 가능하다 (iterable)

* String Method

  * 값을 변경하는 method

    * replace(ord str, new str[,count]) 

      ```python
      'yay!'.replace('a','-')  #'y-y!'
      'wooooooo'.replace('o','!',3) #w!!!oooo
      ```

      

    * strip([char]) #[]안의 값은 optional한 값이다

      * 특정 문자를 지정하면 해당문자를 양쪽에서 찾아 제거한다.
      * lstrip: 해당문자를 왼쪽에서 찾아서 제거 / rstrip : 해당문자를 오른쪽에서 찾아서 제거

    * split([char])

      * 문자열을 특정 단위로 나누어서 `리스트로 반환`

        ```python
        input = ('1 2 3 4 5')
        
        li_input = input.split() # ['1', '2', '3', '4', '5']
        
        a = 'a_b_c'
        print(a.split('_')) #['a', 'b', 'c']
        print(a.split('b')) #['a_', '_c']
        
        ```

    * join(iterable)

      * 특정 문자열로 만들어서 반환 

      ```python
      word = '배고파'
      '!'.join(word) = '배!고!파'
      words = ['a', 'b', 'c']
      '_'.join(words) ='a_b_c'
      ```

  * 문자 변경

    * `capitalize()` : 앞글자만 대문자로
    * `title()`: 공백이나 따옴표 뒷글자를 대문자로 `New York Times`
    * `upper()` : 모두 대문자
    * `lower()`: 모두 소문자
    * `swapcase()` : 대소문자 change

  * 문자열 관련 검증

    * `istitle()`
    * `isalpha()` : 알파벳 구성인지 검증
    * `isspace()` : 공백인지 아닌지
    * `isupper()` / `islower()`
    * `isdecimal()` : 순수 int로 형변환이 가능한 문자열인지
    * `isdigit()` : 윗첨자도 숫자로 인식
    * `isnumeric()` : 분수의 특수기호, 특수 로마자도 숫자로 인식
      * 주의: 해당 decimal, digit, numeric은 float 형태의 문자열은 False로 반환

  * 기타 문자열 관련 메소드

    * `dir('string')`



### 리스트	



* 변경가능(mutable), 순서가 있고, 순회가 가능하다(iterable)

* List Method

  * 값을 추가 및 삭제

    * `append(x)`
    * `extend(iterable)`
    * `insert(index,x)`
    * `remove(x)`: 지우려는 값이 없으면 error 발생
    * `pop(i)`: 정해진 위치에 있는 값을 삭제하고 그값을 반환, i 에 값이 없으면 마지막 항목 
    * `clear()`: 모든 요소 삭제

    

  * 탐색 및 정렬

    * `index(x)`: 제일 처음 있는 x값의 index값 반환 / 값 없으면 에러
    * `count(x)`: 리스트에서 x의 갯수를 count 후 반환
    * `sort()`: None을 반환, 원본을 변경 `sort(reverse = True)`는 오름차순 `sort(reverse = False)` 는 내림차순
      * `sorted(iterable[, reverse=True])`: 정렬된 값을 반환, 그리고 원본 유지
    * `reverse()`: 정렬없이 앞뒤를 뒤집어줌
      * `reversed()`: 정렬없이 앞뒤를 뒤집어줌 `list_reverseiterator object` 반환.

  * 리스트 복사 

    ```python
    a = [1, 2, 3]
    b = a
    b[0] =10
    print(a) #[10, 2, 3]
    ```

    1. `slicing()`을 활용해서 복사

       ```python
       a = [[1, 2],[3, 4]]
       b = a[:]
       
       a[0] = [4,5]
       print(b)
       ```

       

    2. `list()` 메서드를 활용해서 복사

       ```python
       a = [1, 2, 3]
       b = list(a)
       
       b[1] = 200
       print(a) #[1,2,3]
       ```

    3. copy 모듈을 활용

       ```python
       import copy
       
       a = [1, 2, [3, 4]]
       b = copy.copy(a)
       
       ```

       ​	

   * `deepcopy`	

     ```python
     import copy
     
     a = [1, 2, [3, 4]]
     b = copy.deepcopy(a)
     
     ```



* 데이터 분류
  * * immutable
      * number, string, bool, range, tuple, frozenset
    * mutable
      * list, set dictionary

---

* Buit-in Function

  * map(funtion, iterable)

    * iterable 한 데이터를 인자로 받아 모든 요소에 function을 적용한 후 결과를 `map object`로 반환

      ```python
      def square(num):
          return num**2
      
      numbers =[1, 2, 3, 4, 5]
      double_li = list(map(square, numbers))
      print(double_li) #[1, 4, 9, 16, 25]
      
      
      input = '1 2 3 4 5'
      
      numbers = input.split()
      new_numbers = list(map(int, numbers))
      
      ```

  * filter(function, iterable)

    * function의 return값이 `True`인 값만 추출, `filter object`값을 반환

      ```python
      def pos_num(num):
          if num > 0:
              return num
          else:
              return False
          
      
      numbers = list(range(-10, 11))
      pos = list(filter(pos_num, numbers)) # [1, 2, 3, 4, ....... , 9]
      ```

   * zip(*iterable)

      * 복수의 iterable한 객체를 모아준다. tuple 모음으로 구성된 zip object를 반환.

        ```python
        girls = ['jane', 'iu', 'mary']
        boys = ['justin', 'david', 'kim']
        ranking = [1, 2, 3]
        
        cuples = list(zip(girls, boys, ranking)) 
        # [('jane', 'justin', 1), ('iu','david', 2), ('mary', 'kim', 3)]
        ```

     * 되도록이면 길이가 같은 객체를 사용하는 것이 좋다.

     * 길이가 다르다면 짧은 객체를 기준으로 합쳐주고 나머지는 무시된다.

     * `itertools`내장 모듈안에 `zip_longest`함수를 사용하면 긴것을 기준으로 합쳐준다.

       ```python
       from itertools import zip_longest
       num1 = [1, 2]
       num2 = [3, 4, 5]
       zip(num1, num2) #[(1, 3), (2, 4)]
       zip_longest(num1, num2, fillvalue=0) #[(1, 3),(2, 4), (0, 5)]
       ```



---

## 데이터 구조



### 세트(set)



* 변경 가능하고, 순서가 없고, 순회는 가능

* 집합의 요소는 유니크 하다. 중복이 불가능

* 집합의 요소는 immutable 값만 가능. mutable 객체를 넣으면 `TypeError`발생

* Set Methods

  * 추가 및 삭제
    * add(elem): 값을 하나 추가 시킬때 사용
    * update(*others): 여러개의 값을 넣을때 사용
    * remove(elem): 값을 삭제를 하고 만약 값이 없으면 `KeyError `발생
    * discard(elem):값을 삭제를 하고 만약 값이 없어도 에러가 발생하지 않는다
    * pop(): 임의의 요소를 제거한 후 반환해준다.

  

### 딕셔너리



* 변경 가능하고, 순서가 없고, 순회가 가능하다

* Dictionary Methods

  * get(key)

    *  key를 통해서 해당 value를 가져온다

      ```python
      dic['key']: 키값을 직접 넣어서 값을 가졍ㄹ 때 키가 없으면 keyError 발생 
      ```

    * key가 없어도 에러를 발생하지 않음. None을 반환

  * pop()

    * key가 있으면 dictionary에서 제거하고, 키가 없으면 default값을 반환
    * default가 없으면 keyerror 발생.

  * update()

    * 1개 이상의 값을 `key = value`의 형식으로 값을 추가 할 수 있다.
    * key가 존재하면 그 값을 수정
    * key가 존재하지 않으면 새로 생성

  * keys()

    * 해당 dictionary의 키를 리스트로 반환(`dict_key object`)

  * values()

    * 해당 dictionary의 값을 리스트로 반환(`dict_value object`)

  * items()

    * 해당 dictionary의 키와 값을 리스트로 반환(`dict_items object`)



* Dictionary 순회

```python
# 1. dictionary를 for로 순회했을때
for dic in dicts:
	print(dic) #dicts의 키값이 들어있다.
    
# 2. keys로 순회 했을때
for dic in dict.keys():
    print(dic) #dicts의 키값이 들어있다.
    
# 3. values로 순회 했을때
for val in dicts.values():
    print(val) #dicts의 value값이 들어있다.
    
# 4.items로 순회 했을때
for dic in dicts.items():
    print(dic) #dic에는 (key, value)형태의 tuple 값이 들어있다.

for key, value in dicts.items():
print(key) 
print(value)
```





### List Comprehension

* 간결함
* python만의 특징을 가지고 있음
* 속도도 빠르다
* 무분별하게 사용하게되면 가독성이 떨어진다.

```python
#기본 형태
li_comp = [for 임시변수 in iterable]
li_comp2 = list(식 for 임시변수 in iterable)

#기본 형태 + 조건식
li_comp3 = [식 for 임시변수 in iterable if 조건식]
li_comp4 = [식1 if 조건식 else 식2 for 임시변수 in iterable]

li_comp5 = [식1 if 조건식 else 식2 if 조건식 else 식3 for 임시변수 in iterable]
```



```python
def only_square_area(list1, list2):
	area = [i*j for i in list1 for j in list2 if i == j]
    return area
```

