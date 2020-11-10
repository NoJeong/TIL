# Field lookups

* 구글링 키워드 : `django queryset` -> `field lookups`
* 필드명__필드룩업
* exact : 대소문자 일치해야함.
* iexact : 대소문자 상관없이 일치하면 됨.
* contains : 해당 글자가 포함되어 있으면 됨.
* startswith : 해당글자로 시작하는 것만
* endswith : 해당글자로 끝나는 것만
* gt / gte / lt / lte : 비교연산자 



## 실습

* 제목이 first이고 한개만 가져와라. (여러개의 데이터가 있는데 하나만 가져오고 싶을때)

  ```
  Article.objects.filter(title='third').first()
  ```

  * 해당 모델 클래스로 값이 리턴



* 정렬을 하고 싶을 때(오름차순 & 내림차순)

  ```
  # 오름차순
  Article.objects.order_by('pk')
  # 내림차순
  Article.objects.order_by('-pk')
  ```

* QuerySet 으로 리턴을 받았을 때

  * QuerySet은 list와 유사함

  * indexing & slicing

    ```
    #indexing
    Article.objects.all()[1]
    
    Article.objects.all()[-1] # 지원하지 않음
    
    #slicing
    Article.objects.all()[:2]
    ```

    

## Template 확장 사용하기

1. base.html을 생성하고 원하는 위치에 templates 폴더안에 위치 시킨다.
   * base.thml에는 기본 html DOM 트리를 구성한다
   * bootstrap CDN을 복붙해준다
   * block을 body안에 적절한 곳에 위치 시켜준다
2. setting.py에 base.html의 경로를 등록한다
   * TEMPLATES라는 곳에 있는 DIRS에 그 경로를 추가해 준다.
   * base.html이 있는 경로를 BASE_DIR로 부터 설정해주면 된다.
   * `DIRS : [BASE_DIR/'workshop_sol'/'templates']`

3. 확장하고 사용한다. 
   * 제일 첫번째 줄에 `{% extends 'base.html' %}`
   * 그 다음 block을 위치시키고 block 안에 적절히 꾸며주면 된다.





# CRUD

### READ

* DB에서 전체 글 목록을 가져와서  page에 보여주자
* Article.objects.all() 의 QuerySet을 그대로 context에 담아서 template 파일에 전달
* template은 for 문으로 하나씩 db값을 접근 가능하고 `.`연산자를 이용해서 값에 접근도 가능



### CREATE

* form 태그에서 데이터를 전달하고 
* 그 데이터를 3가지 방법중 1개의 방법으로 DB에 저장하면 끝
* GET / POST
  * GET : 주소줄에 쿼리 스트링 형식으로 데이터가 전달. 전달하는데 길이가 한계가 있음 (255자)
    * 주로 데이터 정보를 가져올때 사용(즉, 데이터를 조회 할 때 이용)
  * POST :  패킷 바디안에 데이터가 전달
    * 주로 데이터의 정보를 생성, 수정, 삭제할 때 사용
  * GET/article/ : article의 정보를 조회
  * POST/article/ : article 을 생성.
  * POST/article/1/ : article을 수정.
  * REST API : 나중에 수업할 예정

* method를 POST로 변경 할 때 해야할일!
  * CSRF : Form tag 사이에 `{% csrf_token %}`
  * request.GET 을 request.POST로 변경



* CSRF
* Redirect() : 이미 만들어진 페이지로 경로 재설정.



----

### update

* 글 제목을 클릭 했을 때 해당 글만 보여지는 페이지.
* detail 페이지를 먼저 만들자!
  * 어떠한 글의 detail페이지 인지 해당글의 정보 (pk)가 필요함
  * 글의 정보를 동적 라우팅 방법으로 주소로 전달
  * 주소로 전달 받은 글의 pk 값을 가지고 DB에서 데이터를 가져옴
  * 가져온 데이터를 TEMPLATE 파일에서 보여주면 그것이 detail page!
* detail 페이지 하단에 수정하기 링크를 만들어 준다. 
  * 수정하기 링크는 edit하는 페이지를 보여주면 된다 
  * create 방법과 유사하게 form을 보여주는데
  * 차이점은 해당 글의 data를 같이 넘겨주고 그 데이터를 같이 보여주는게 차이점.
  * 수정하기 최종버튼을 눌렀으면 post 방식으로 DB에 적용을 시켜주면 끝
  * 이때 필요한 정보도 주소줄을 이용해서 전달한다. 
* DB에 적용시키는 방법은
  * 해당  pk를 가지는 데이터를 불러오고
  * 값을 수정하고
  * save한다
* 끝나면 detail page로 redirect 시키면 끝!!







------

### Delete

* 삭제하기 버튼을 누르면 삭제할 글의 pk가 같이 주소로 전달되고
* views.py에서 해당pk값의 정보를 가져온 다음에 delete 함수를 호출하면 끝!