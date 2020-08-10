# 08_Module / Package

### 다양한 모듈 상용법

#### 모듈

```python
import module
from module import var, function, Class
from module import *
```

### 패키지

```python
from package import module
from package.module import var, function, Class
```

### `from` 모듈 `import` 데이터 `as` 별명

```python
from my_package.statistics.tools import satandard_deviation

sd = standard_deviation
sd([1, 2, 3,  4, 5])
```



# 09_OOP_I

* 객체지향프로그래밍

### 객체(object)

> Python에서 **모든것은 객체(object)**이다
>
> 모든 객체는 **타입(Type), 속성(attribute), 조작법(method)**을 가진다



#### 객체(object)의 특징

* **타입(type)**: 어떤 연산자와 조작이 가능한가?
* **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
* **조작법(method)**: 어떤 행위를 할 수 있는가?



### 타입(type)과 인스턴스(instance)

#### 타입

* 공통되니 속성과 조작법을 가진 객체들의 분류



#### 인스턴스

* 특정 타입(type)의 실제 데이터 예시
* 파이썬에서 모든것은 객체이고, **모든 객체는 특정 타입의 인스턴스**이다.

```python
a = int(10)
type(a) == int #True
isinstance(a, int) #True
```



### 속성(Attribute)과 메서드(Method)


| type      | attributes       | methods                                |
| --------- | ---------------- | -------------------------------------- |
| `complex` | `.real`, `.imag` |                                        |
| `str`     | _                | `.capitalize()`, `.join()`, `.split()` |
| `list`    | _                | `.append()`, `.reverse()`, `.sort()`   |
| `dict`    | _                | `.keys()`, `.values()`, `.items()`     |

```python
(3+4j).real #3
(3+4j).imag #4
```

```python
dir(list) #리스트타입의 객체가 가지고있는 메서드를 확인하기
```





# 객체지향프로그래밍 장점

* 코드의 **직관성**
* 활용의 **용이성**
* 변경의 **유연성**



### 클래스(Class) 생성

* 활용법

```python
Class <클래스이름>:
    <메소드>
    
Class ClassName:
    methods
```

* 예시

```python
Class Person:
    pass

print(type(Person)) #class'type'
```

