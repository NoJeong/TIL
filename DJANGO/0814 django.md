# 0814 django



* 장고 프로젝트 만들기

```django
django-admin startproject 프로젝트이름
```

프로젝트 이름에는 

* 하이픈 X
* python, django에서 쓰는 기본 이름은 X

* 터미널에서 서버 끄기 `ctrl + c`

* 앱의 이름은 복수형으로 작성!





## 장고 할일

1. app 생성
2. app 등록



## view 함수

* 함수선언시 첫 인자로 반드시 request를 받아야한다.



## 코드작성순서 (데이터 흐름과 동일)

1. urls.py
2. views.py
3. templates



## 장고 코드 작성 순서



```django
#djang imports style guide
#1. standard library
#2. 3rd party 
#3. Django
#4. local django
```





## Django

Django 3.1

`pip list` 로 버전 확인 가능!

* 장고 설치하기

```
pip install Django

#특정버전으로 받을 시
pip install django==3.0.8
```

* 장고 시작django admin st





# Django template language (DTL)

* django template system에서 사용하는 built-in template system이다. 
* 조건, 반복, 치환, 필터, 변수 등의 기능을 제공 
* 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한것 
* 파이썬처럼if, for를 사용할 수 있지만 이것은 단순히 python code로 실행되는 것이 아닙니다.



syntax



* variable: `{{ variable }}`
* filter: **{{** **name|lower** **}}**
* tags: **{%** **tag** **%}**



----



# 템플릿 시스템 설계 철학

* 장고는 템플릿 시스템이 **표현**을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다. 
* 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다. 