## git 사용법

*  새파일 추가

  ```  bash
  $ git add . #현재 디렉토리의 모든 파일 
  $ git add python/ #특정 폴더
  $ git add 정리.md #특정 파일
  ```

* 저장소 초기화

  `$ git init`

* 파일 없애기

  `$ git reset or $ git restore --statged 파일이름` 

* commit 버전의 이력을 확정짓는 명령어, 해당시점을 스냅샷으로 만들어 기록

`$ git commit -m`

`$ git commit --amend` : 제일 마지막 커밋기록 수정가능 #저장후에 :wq



`$ git commit만 쳤을때` : esc : q 로 나가기





```bash
$ git conㅐfig --global user.name Nojeong #이름설정
$ git config --global user.email op032@naver.com #이메일 설정
```

* 파일 상태 확인하기

`$ git status`  

*  log 정보 파악하기

`$ git log` 

*  완성된 메모장에   
  * 정말 중요하거나 필요없는것, 퍼블릭에 올리지말것(블랙리스트) 파일이름 적기ex) d.txt, 폴더이름

`$ git log --oneline` 

* 간단하게 커밋을 볼 수 있음

`$ git diff`

* 파일들의 수정된 점을 알려줌

`$ echo > .gitignore`

gitignore.io

`git reset HEAD^` 이전 커밋 지우기

복사는 시프트 + 인서트 

tensorflow







## 원격저장소



#### 0. repository 생성

####  1. 원격저장소 local에 등록

``` bash
$ git remote add origin '깃 레파지토리 주소'
$ git remote -ㅍ #현재 등록된 remote 정보를 확인 가능
```

#### 2. push

* 원격 저장소로 업로드

  ```bash
  $ git push origin master
  ```

  ---

  #### 우리의 루틴

  * 싸피에서 한 것이 최신 버전이고 집에서 작업을 하는경우

    `pull -> add -> commit -> push`

    ```bash
    $ git pull origin master
    ```

    해당 루틴으로 진행하면 끝!

  * 집에서 한것이 최신버전이고 집에서 작업을 하는경우

    `add -> commit -> push`

  * 집에서 한것이 최신버전이고 싸피에서 git작업을 한번도 하지 않은 경우

    1. `git clone '원격 저장소 주소(레파지토리 주소)'`
       * 원격저장소를 기준으로 최신 버전의 파일이 다운로드 받아짐
       * .git 폴더도 자동 생성되어짐.(git DB가 들어가있기 때문)

  * add, commit,push 루틴은 아래와 같음