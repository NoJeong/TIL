# GIT CHEATSHEET

https://ssafyprj.github.io/git/?locale=ko 를 풀면서 정리한것

## git commit / merge



`git merge` : 

> 부모branch로 합치기

`git chechout bugfix; git merge master` : 

> `bugFix`가 `master`의 부모쪽에 있었기 때문에, git이 별다른 일을 할 필요가 없었습니다; 간단히 `bugFix`를 `master`가 붙어 있는 커밋으로 이동시켰습니다 



#### 실습

- `bugFix`라는 새 브랜치를 만듭니다

  ```
  git branch bugFix
  ```

- `git checkout bugFix`를 입력해 `bugFix` 브랜치로 이동(checkout)합니다.

  ```
  git checkout bugFix
  ```

- 커밋 한 번 하세요

  ```
  git commit
  ```

- `git checkout` 명령어를 이용해 `master`브랜치로 돌아갑니다

  ```
  git checkout master
  ```

- 커밋 또 하세요

  ```
  git commit
  ```

- `git merge` 명령어로 `bugFix`브랜치를 `master`에 합쳐 넣습니다.

  ```
  git merge bugFix
  ```





## git rebase

`bugFix` 브랜치에서의 작업을 `master` 브랜치 위로 직접 옮겨 놓으려고 합니다. 그렇게 하면, 실제로는 두 기능을 따로따로 개발했지만, 마치 순서대로 개발한 것처럼 보이게 됩니다.

```
git rebase master
```



![image-20210107145404583](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107145404583.png)

오! 이제 bugFix 브랜치의 작업 내용이 master의 바로 위에 깔끔한 한 줄의 커밋으로 보이게 됐습니다.

C3 커밋은 어딘가에 아직 남아있고(그림에서 흐려짐), C3'는 master 위에 올려 놓은 복사본입니다.

master가 아직 그대로라는 문제가 남아있는데요, 



우리는 지금 `master` 브랜치를 선택한 상태입니다. `bugFix` 브랜치쪽으로 리베이스 해보겠습니다

```
git rebase bugFix
```



![image-20210107145534589](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107145534589.png)

보세요! `master`가 `bugFix`의 부모쪽에 있었기 때문에, 단순히 그 브랜치를 더 앞쪽의 커밋을 가리키게 이동하는 것이 전부입니다

#### 실습

- `bugFix`라는 새 브랜치를 만들어 선택하세요

  `git branch bugFix;git checkout bugFix`

- 커밋 한 번 합니다

  `git commit`

- `master`로 돌아가서 또 커밋합니다

  `git checkout master; git commit`

- bugFix를 다시 선택하고 master에 리베이스 하세요

  `git checkout bugFix; git rebase master`

  

## git commit tree

### HEAD 분리하기

HEAD를 분리한다는 것은 HEAD를 브랜치 대신 커밋에 붙이는 것을 의미합니다. 명령을 사용하기 전의 모습은 다음과 같습니다:

HEAD -> master -> C1

![image-20210107150046098](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150046098.png)

`git chechout C1`

![image-20210107150113736](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150113736.png)

이제는 이렇게 되는군요

HEAD -> C1



#### 캐럿 연산자

`master^`는 "`master`의 부모"와 같은 의미 입니다.

`master^^` 는 "`master`의 조부모(부모의 부모)"를 의미합니다

![image-20210107150553192](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150553192.png)

`git checkout master^`

![image-20210107150614450](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150614450.png)

돌아가고 싶은 커밋의 갯수를 `~`뒤의 숫자로 명시해 줍시다.

![image-20210107150815809](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150815809.png)

`git checkout HEAD~4`

![image-20210107150825528](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150825528.png)

#### 브랜치 강제로 옮기기

![image-20210107150930662](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107150930662.png)

`git branch -f master HEAD~3`

![image-20210107151009558](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107151009558.png)

우리는 상대 참조를 통해 `C1`을 간결한 방법으로 참조할 수 있었고 브랜치 강제(`-f`)를 통해 브랜치를 저 위치로 빠르게 옮길 수 있었습니다.





## Git 리셋

![image-20210107152350628](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107152350628.png)

`git reset HEAD~1`

![image-20210107152419806](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107152419806.png)

그림에서처럼 `master` 브랜치가 가리키던 커밋을 `C1`로 다시 옮겼습니다; 이러면 로컬 저장소에는 마치 `C2`커밋이 아예 없었던 것과 마찬가지 상태가 됩니다.

 



## Git 리버트

각자의 컴퓨터에서 작업하는 로컬 브랜치의 경우 리셋(reset)을 잘 쓸 수 있습니다만, "히스토리를 고쳐쓴다"는 점 때문에 다른 사람이 작업하는 리모트 브랜치에는 쓸 수 없습니다.

변경분을 되돌리고, 이 되돌린 내용을 다른 사람들과 *공유하기* 위해서는, `git revert`를 써야합니다. 예제로 살펴볼게요.



![image-20210107153019677](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107153019677.png)

`git revert HEAD`

![image-20210107153106413](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107153106413.png)

어색하게도, 우리가 되돌리려고한 커밋의 아래에 새로운 커밋이 생겼습니다. `C2`라는 새로운 커밋에 *변경내용*이 기록되는데요, 이 변경내역이 정확히 `C2` 커밋 내용의 반대되는 내용입니다.

리버트를 하면 다른 사람들에게도 변경 내역을 밀어(push) 보낼 수 있습니다.



## 작업을 여기저기로 옮기기

#### Git 체리-픽

현재 위치(`HEAD`) 아래에 있는 일련의 커밋들에대한 복사본을 만들겠다는 것을 간단히 줄인 말입니다.

여기 repository가 있습니다. `master`와 master로 복사하고 싶은 작업이 있는 브랜치 `side`가 있습니다. 이것은 rebase를 통해서 할 수 있습니다(이미 배운), 하지만 체리-픽이 이 작업을 어떻게 수행하는지 확인해 봅시다.

![image-20210107153427040](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107153427040.png)

`git cherry-pick C2 C4`

![image-20210107153539386](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107153539386.png)

우리는 `C2`와 `C4` 커밋을 원했고 git이 우리가 원하는 곳 바로 밑에 톡 떨어뜨려 줬습니다. 아주 간단하죠!



#### Git 인터렉티브 리베이스

Git 체리-픽은 여러분이 원하는 커밋이 무엇인지 알때(각각의 해시값도) 아주 유용합니다 -- 체리-픽이 제공하는 간단함은 아주 매력적입니다.

하지만 원하는 커밋을 모르는 상황에는 어쩌죠? 고맙게도 git은 이런상황에 대한 대안이 있습니다. 우리는 이럴 때 인터렉티브 리베이스를 사용하면됩니다

인터렉티브 리베이스 대화창이 열리면, 3가지를 할 수 있습니다:

- 적용할 커밋들의 순서를 UI를 통해 바꿀수 있습니다(여기서는 마우스 드래그앤 드롭으로 가능합니다)
- 원하지 않는 커밋들을 뺄 수 있습니다. 이것은 `pick`을 이용해 지정할 수 있습니다(여기서는 `pick`토글 버튼을 끄는것으로 가능합니다)
- 마지막으로, 커밋을 스쿼시(squash)할 수 있습니다. 불행히도 저희 레벨은 몇개의 논리적 문제들 때문에 지원을 하지 않습니다. 이거에 대해서는 넘어가겠습니다. 요약하자면 커밋을 합칠 수 있습니다

![image-20210107154222495](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107154222495.png)

`git rebase -t HEAD~4`

![image-20210107154258107](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107154258107.png)

![image-20210107154319810](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210107154319810.png)



## 커밋 갖고놀기

#### REBASE 로 해보기

- `git rebase -i` 명령으로 우리가 바꿀 커밋을 가장 최근 순서로 바꾸어 놓습니다

  `git rebase -i HEAD~2`

- `git commit --amend` 명령으로 커밋 내용을 정정합니다

  `git commit --amend`

- 다시 `git rebase -i` 명령으로 이 전의 커밋 순서대로 되돌려 놓습니다

  `git rebase -i HEAD~2`

- 마지막으로, master를 지금 트리가 변경된 부분으로 이동합니다. (편하신 방법으로 하세요)

  `git rebase caption`

#### CHERRY_PICK으로 해보기

![image-20210109133725014](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109133725014.png)

 `git checkout master`

![image-20210109133737685](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109133737685.png)

` git cherry-pick C2`

![image-20210109133806249](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109133806249.png)

`git branch -f master HEAD~1`

![image-20210109133836977](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109133836977.png)

` git cherry-pick C2' C3`

C2'' - C3' 생성



## GIT 태그

여러분은 여러분의 프로젝트의 역사(작업 이력)에서 중요한 지점들에 *영구적으로* 표시를 할 방법이 없을까 궁금할것입니다. 주요 릴리즈나 큰 브랜치 병합(merge)이 있을때가 그런 상황이겠군요

Git 태그는 특정 커밋들을 브랜치로 참조하듯이 영구적인 "milestone(이정표)"으로 표시합니다.

중요한 점은, Git 태그는 커밋들이 추가적으로 생성되어도 절대 움직이지 않는다는 것입니다. 여러분은 태그를 "체크아웃"한 후에 그 태그에서 어떤 작업을 완료할 수 없습니다

![image-20210109134035230](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109134035230.png)

`git tag v1 C1`

![image-20210109134103494](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109134103494.png)

## GIt Describe 

커밋 트리에서 태그가 훌륭한 "닻"역할을 하기 때문에, git에는 여러분이 가장 가까운 "닻(태그)"에 비해 상대적으로 어디에 위치해있는지 *describe(묘사)*해주는 명령어가 있습니다. 이 명령어는 `git describe` 입니다!



Git describe는 커밋 히스토리에서 앞 뒤로 여러 커밋을 이동하고 나서 커밋 트리에서 방향감각을 다시 찾는데 도움을 줍니다; 이런 상황은 git bisect(문제가 되는 커밋을 찾는 명령어라고 간단히 생각하자)를 하고 나서라던가 휴가를 다녀온 동료의 컴퓨터에 앉는경우가 있습니다.



it describe 는 다음의 형태를 가지고 있습니다:

```
git describe <ref>
```

`<ref>`에는 commit을 의미하는 그 어떤것이던 쓸 수 있습니다. 만약 ref를 특정 지어주지 않으면, git은 그냥 지금 체크아웃된곳을 사용합니다 (`HEAD`).

명령어의 출력은 다음과 같은 형태로 나타납니다:

```
<tag>_<numCommits>_g<hash>
```

`tag`는 가장 가까운 부모 태그를 나타냅니다. `numCommits`은 그 태그가 몇 커밋 멀리있는지를 나타냅니다. `<hash>`는 묘사하고있는 커밋의 해시를 나타냅니다.



![image-20210109134834031](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109134834031.png)

```git
git tag v2 C3
```

![image-20210109134915015](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109134915015.png)

`git describe master` 명령은 다음을 출력합니다:

```
v1_2_gC2
```

`git describe side`는 다음을 출력합니다:

```
v2_1_gC4
```



## 여러 브랜치 리베이스 하기

![image-20210109145523369](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109145523369.png)

```
git rebase master bugFix
```

![image-20210109150102356](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150102356.png)

```
git rebase bugFix side
```

![image-20210109150224552](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150224552.png)

```
git rebase side another
```

![image-20210109150252229](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150252229.png)

* master 땡겨오기

```
git rebase another master
```



## 부모 선택하기

![image-20210109150717985](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150717985.png)

```
git checkout master^
```

* 첫 부모를따라간다

![image-20210109150746327](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150746327.png)

```
git checkout master^2
```

* 2번째 부모를 따라간다

![image-20210109150831342](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150831342.png)

#### 실습

![image-20210109150910767](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109150910767.png)

```
git checkout HEAD~; git checkout HEAD^2; git checkout HEAD~2
```

```
C6 -> C5 ->C3
```

* 이코드도 같은코드다

```
git checkout HEAD~^2~2
```

## 브랜치 스파게티

![image-20210109151820297](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109151820297.png)

```
git checkout one;git cherry-pick C4 C3 C2
```

![image-20210109151858591](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109151858591.png)

```
git checkout two
git cherry-pick C5 C4 C3 C2
```

![image-20210109151932277](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109151932277.png)

```
git branch -f three C2
```

![image-20210109152000355](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210109152000355.png)
