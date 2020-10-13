## 식별자 (identifier)

* 변수명은 식별자라고도 불림.

* 규칙

  1. 반드시 **문자, 달러($)** 또는 **밑줄(_)**로 시작해야한다!! (숫자, `-`로 시작할 수 없다.)

     ```javascript
     const hi-hello (X)
     const hi_hello (O)
     const _hi = 100 (O)
     const hi_hello = 100 (O)
     const 9hi = 100 (X)
     ```

     

  2. 대소문자를 구분한다. 

  3. 예약어는 사용할 수 없다. (const, function, class, )

* 스타일

  * 카멜케이스 (lowerCamelCase)
    * 객체, 변수, 함수
  * 파스칼 케이스 (UpperCamelCase)
    * 클래스, 생성자
  * 대문자 스네이크 케이스 (UPPER_CASE)
    * 상수 : 변수나 변수의 속성이 변하지 않는것.



## Hoisting

* var 로 선언된 변수는 선언이전에 참조할 수 있는 현상.



```javascript
console.log(name)
var name = '홍길동'

console.log(age)
let age = '홍길동'
```







## String

* JS 에서 문자열을 표현하는 방법



```javascript
const str1 ='홑 따옴표사용'
const str2 ='쌍 따옴표사용'

str1 + str2

const str3 = "줄바꿈은
허락되지않는다"

//excape squance
const str4 "줄바꿈은 \n 이렇게 해야합니다."

//template literal (ES6+) 백틱(` : ~쉬프트없이)
const str5 = `안녕하세요
이렇게 줄바꿈도 가능합니다`

const str6 = `${str1}`

const num = 100
const str7 = `${num} - ${str1}`
```

* 리터럴
  * 리터럴이라는단어는 값을 프로그램 안에서 직접 지정한다라는의미
  * 리터럴은 값을 만드는 방법



## Switch

```javascript
const name = '홍길동'

switch(name) {
    case 'admin': {
        console.log('관리자 모드')
        break
    }
    case 'manager': {
        console.log('매니저 모드')
        break
    }
    default: {
        console.log(`${name} 님 환영합니다.`)
    }
}
```





## for 문

```javascript
for (let i = 0 ; i < 6 ; i++) {
    console.log(i)
}

const numbers = [0, 1, 2, 3]
for (const number of numbers) {
    console.log(number)
}

const obj = {a : 'a', b : 'b'}
for (const o of obj) {
    console.log(o)
} // 에러 발생 

const obj = { a: 'apple', b : 'banana'}
for (const o in obj) {
    console.log(o)
    console.log(obj[o])
}
```



## 화살표 함수

```javascript
const arrow = function (name) {
    return `hello! ${name}!`
}

// 1. function 키워드를 삭제하고 화살표를 추가한다. 
const arrow = (name) => {
    return `hello ${name}!`
}

// 2. 매개변수가 하나일때는 괄호를 생략할 수 있다.
const arrow = name => {
    return `hello ${name}!`
}

// 3. {} & return 생략 ( body 에 표현식이 1개 인경우) 
const arrow = name => `hello! ${name}!`

//연습코드 
const exam = function () {
    return 'hello, world'
}

//1.
const exam = () => {
    return 'hello, world'
}

//2. skip (매개변수가 없으므로)

//3. 
const exam = () => 'hello, world'
```



## function 키워드 호이스팅

```javascript
// 선언식일때는 동작
add(2, 7)
function add (a, b) {
    return a + b
}

// 표현식일 때는?
sub(7, 2)
const sub = function (num1, num2) {
    return num1 - num2
}

const sub(7, 2)
var sub = function (num1,num2) {
    return num1 - num2
} // Error
```

---

## 함수의 Object 축약형

```javascript
let obj = {
    name : 'ssafy',
    sayHi : function () {
        console.log('hello')
    }
}

obj.sayHi() // 'hello'

// ES6+
let obj2 = {
    name : 'ssafy'
    // 함수의 object 축약형.
    sayHi () {
        console.log('hi!!')
    }
}

obj2.sayHi()


```

---

## JSON (JavaScript Object Notation)

JavaScript  Object 형태를 가지는 `문자열`

#### object -> JSON

```javascript
const objData = {
    coffee: 'Americano',
    icecream: 'Bravo corn',
}

const jsonData = JSON.stringify(objData)
console.log(typeof(jsonData))
```



#### JSON -> object

```javascript
const objData2 = JSON.parse(jsonData)
console.log(typeof(objData2))
```

---

## forEach

* exercise

  ```js
  // 배열 안에 있는 정보를 곱해서 그 넓이를 areas 배열에 저장
  const images = [
      { height : 10, width : 30},
      { height : 20, width : 90},
      { height : 54, width : 32}
  ]
  
  const areas = []
  ```

  * 풀이 코드

    ```js
    const images = [
        { height : 10, width : 30},
        { height : 20, width : 90},
        { height : 54, width : 32}
    ]
    
    images.forEach(function (img) {
        areas.push(img.height * img.width)
    })
    console.log(areas)
    ```

    

## map

* exercise

  ```js
  // 각 숫자들의 제곱근이 들어있는 새로운 배열을 만드세요.
  
  const newNumbers = [4, 9, 16]
  
  const dNums = newNumbers.map(function (num) {
      //return Math.sqrt(num)
      return num ** 0.5
  })
  ```

  

  ```js
  const areas2 = images.map(function (img) {
      return img.height * img.width
  })
  ```





## filter

```js
const products = [
    { name : 'cucumber', type : 'vegetable'},
    { name : 'banana', type : 'fruit'},
    { name : 'carrot', type : 'vegetable'},
    { name : 'apple', type : 'fruit'}
]

const fruits = products.filter (function (product) {
    return product.type === 'fruit'
})
console.log(fruits)
```

* exercise

  ```js
  //numbers 배열중 50보다 큰 값들만 모은 배열 filteredNumbers을 만드세요.
  const numbers = [15, 25, 35, 45, 55,65, 75, 85, 95]
  
  const filteredNumbers = numbers.filter (function (number) {
      return number > 50
  })
  console.log(filteredNumbers)
  ```

  

## find

```js
const products = [
    { name : 'cucumber', type : 'vegetable'},
    { name : 'banana', type : 'fruit'},
    { name : 'carrot', type : 'vegetable'},
    { name : 'apple', type : 'fruit'}
]

const select = products.find(function (product {
                                        return product.type === 'vegetable'
                                        }))
```



## some

```js
const products = [
    { name : 'cucumber', type : 'vegetable'},
    { name : 'banana', type : 'fruit'},
    { name : 'carrot', type : 'vegetable'},
    { name : 'apple', type : 'fruit'}
]

const someVegetable = products.some(function (product) {
    return product.type === 'vegetable'
})
console.log(someVegetable)

const someWater = products.some(function (product) {
    return product.type === 'water'
})
console.log(someWater)

const zerolist = []
const someZero = zeroList.some(function (zero) {
    return zero > 50
})
```

```js
// requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]
const someRequest = requests.some(function (request) {
    return request.status === 'pending'
})
```



## every

```js
// users 배열에서 모두가 submitted 인지 여부를 hasSubmitted에 저장하세요.
const users = [
    { id: 21, submitted: true },
    { id: 33, submitted: false },
    { id: 712, submitted: true},
]
const everyUser = users.every(function (user) {
    return user.submitted === true
})
```



## reduce

```js
const scores = [ 90, 90, 80, 77]

const totalScore = scores.reduce(function (sum, score) {
    return sum + score
})
```

```js
// 주어진 baseUrl 문자열 뒤에 필수 요청 변수인 api 의 key - value 값을 key=value 의 형태로 더하여 요청 url을 만드세요. URL에서 요청 변수는 & 문자로 구분합니다. 

const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
const api = {
  'key': 'API_KEY',
  'targetDt': '20200115'
}
const apiUrl = Object.entries(api).reduce(function (url, api) {
    return url + `${api[0]}=${api[1]}&`
}, baseUrl)


console.log(apiUrl)


```

