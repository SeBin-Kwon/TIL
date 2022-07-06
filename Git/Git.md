# 📕 Git

> 분산 버전 관리 시스템



## 기본 명령어



### init

- `git init`으로 저장소 생성

  - (master)라는 표기를 확인 할 수 있음

- git 으로 버전관리를 하겠다.

- 모든 버전을 지우고 싶다면 `.git` 폴더 삭제하기(주의!)

  

  

#### 기본 흐름

1.  Working directory에서 작업하면
2. `git add`를 통해 Stagting Area에 모아서
3. `git commit`으로 Repository에 버전을 기록한다.

여러가지 파일 중에 버전 기록할 파일들만 `git add`를 통해 Stagting Area(임시공간)에 모은다!



### add

- `git add 파일명`

  Working directory상의 변경 내용을 Stagting Area에 추가하기 위해 사용

- `git add .`

  모든 변경 내용 추가



### commit

- `git commit -m '커밋 메시지'` 

  staged 상태의 파일들을 커밋을 통해 버전으로 기록

- SHA-1 해시를 사용하여 40자 길이의 체크섬을 생성하고, 이를 통해 고유한 커밋을 표기

- **커밋 메시지는 변경 사항을 나타낼 수 있도록 명확하게 작성해야 함**

  

#### commit message

> 의미있는 저장 ( SW가 반드시 작동 가능한 상태)

- **의미를 담아서 커밋 메시지 작성해야함**

- 원격 저장소에 보내면 오류를 발견했을 시 수정하기 복잡함



#### 기본 흐름

- Git은 파일을 modified, staged, committed로 관리

  - `modified` : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)

  - `staged` : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)

  - `committed` : 커밋이 된 상태

    

### log

- `git log`

  현재 저장소에 기록된 커밋을 조회

- 다양한 옵션을 통해 로그를 조회할 수 있음

  - `git log -1` : 가장 최근 1개를 보여줘
  - `git log --oneline` : 한 줄로 보여줘
  - `git log -2 --oneline` : 최근 2개를 한 줄로 보여줘

  

### status

- `git status`

  Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용

  - Untracked files

  - Changes not staged for commit

  - Changes to be committed

  - `Nothing to commit` : 커밋할 것이 없다, staging area가 비어있다.

  - `working tree clean` : 지금 새로 작업한 것도 없다, Working directory가 비어있다.

    

#### 파일 라이프 사이클

- `Untracked` : 한번도 커밋x -> `git add`를 통해 ` Staged`로 한번에 감
- `Unmodified` : 커밋이 되었음, 수정 X -> 수정하면 `Modified`

- `Modified` : `Unmodified`를 수정한것, `git add`하면 `Staged` 됨

- `Staged` : 임시공간에 있는 파일, 커밋하면 `Unmodified` 됨



> `status`를 통해 확인 가능하다.

- 초록 : `staged`

- 빨강 : `Untracked`, `Modified` (add 해야할 것)



## 추가 명령어

- `git reset HEAD^`

  가장 최근의 커밋 내역 한개 삭제

- `git reset HEAD~2`

  최근 2개의 커밋 내역 삭제 (숫자 변경 가능)

- `git log -p`

  로그 상세히 보기



## .gitkeep

> 빈 데이터 파일

1. 빈 폴더는 status에 나타나지 않는다.
2. 빈 데이터 파일을 관용적으로 사용하고 싶을 때, .gitkeep 파일을 생성한다



## 기타

- `head -> master`는 해당 커밋이 master 브랜치의 마지막 커밋이라는 뜻
- `git log` 후 end 나오면 `q`누르면 된다.



## 주의 사항

1. **(master) 있는 곳에서는 git init을 하지 않는다.**
2. **git 명령어를 입력할 때에는 항상 경로를 잘 보자. ex)~/Desktop/…**
3. **git init을 잘못했을 경우, 해당 경로에서 .git 파일을 삭제하자**

