# 🗂 Git 사용법

> 변경 및 추가 사항 : 
>
> 1. 브랜치 master -> main
> 2. checkout -> switch
> 3. reset, revert 추가

### Git 사용하는 방법 두 가지

> - **터미널에 명령어를 이용하는 CLI 방식**
> - 소스트리 등의 프로그램을 사용하는 GUI 방식
### 프로젝트 생성
1. 프로젝트 폴더 생성 후 VS Code로 열람
2. VS Code 터미널에 명령어 입력 시작 `^⌥₩`

✅해당 폴더 내에 숨김파일인 `.git폴더`가 Git 관리내역들이 저장됨

---

## Git 관리 시작

- `git init`
새로운 Git 저장소(repository)를 생성할 때 사용하는 명령어, Git 설치 및 초기화

- `git status`
저장소(repository)의 상태를 보여주는 명령어, 변경사항 확인 가능
✅추적하지 않는(untracked) 파일: Git의 관리에 들어간 적 없는 파일

- `git add (파일경로)`
해당 Working directory의 파일을 staging area로 옮기는 명령어.

- `git add .`
추가되지 않은 모든 파일을 staging area로 옮기는 명령어.

- `git commit`
Staging 영역에 있는 파일을 repository에 저장하는 명령어.

- `git commit -m "(커밋 메시지)"`
커밋 메시지까지 함께 작성

- `git commit -am "(커밋 메시지)"`
add와 commit을 한번에 할 수 있음
✅ 단 새로 추가된(untracked) 파일이 없을 때 한정

- `git log`
repository에 있는 commit 이력을 조회하는 명령어.
위치한 브랜치에서의 내역만 볼 수 있음.
종료는 `:q`


### Vi 입력 모드 진입시

- `i`	
입력 시작 (명령어 입력 모드에서 텍스트 입력 모드로 전환)
- `ESC`
입력 종료 (텍스트 입력 모드에서 명령어 입력 모드로 전환)
- `:q`
저장 없이 종료
- `:q!`
저장 없이 강제 종료 (입력한 것이 있을 때 사용)
- `:wq`
저장하고 종료 (입력한 것이 있을 때 사용)
- `k`
위로 스크롤 (git log등에서 내역이 길 때 사용)
- `j`
아래로 스크롤	(git log등에서 내역이 길 때 사용)

---

## Git에서 커밋한 내용 되돌리는 방법 두 가지
> - **reset** : 원하는 커밋으로 되돌린 뒤 이후 내역을 지움
> - **revert** : 원하는 커밋으로 되돌린 커밋을 새로 추가함
### reset 사용하기
- `git reset --hard (돌아갈 커밋 해시)`
현 커밋 상태로 초기화

### revert 사용하기
- `git revert (되돌릴 커밋 해시)`
`:wq`로 커밋 메시지 저장

- `git revert --no-commit (되돌릴  커밋 해시)`
커밋하지 않고 revert하기
✅ 원하는 다른 작업을 추가한 다음 함께 커밋
취소하려면 `git reset --hard`

---

## Git의 관리에서 특정 파일/폴더를 배제해야 할 경우
> - 자동으로 생성 또는 다운로드되는 파일들 (빌드 결과물, 라이브러리)
> - 보안상 민감한 정보를 담은 파일
`.gitignore 파일`을 사용해서 배제할 요소들을 지정할 수 있다.
1. .gitignore 파일 생성
2. 배제할 파일/폴더 작성 후 저장 

### .gitignore 형식

- `file.c`
모든 file.c

- `/file.c`
최상위 폴더의 file.c

- `*.c`
모든 .c 확장자 파일

- `!not_ignore_this.c`
.c 확장자지만 무시하지 않을 파일

- `logs`
logs란 이름의 파일 또는 폴더와 그 내용들

- `logs/`
logs란 이름의 폴더와 그 내용들

- `logs/debug.log`
- `logs/*.c`
logs 폴더 바로 안의 debug.log와 .c 파일들

- `logs/**/debug.log`
logs 폴더 바로 안, 또는 그 안의 다른 폴더(들) 안의 debug.log

---

## Branch

> #### Branch: 분기된 가지
> 프로젝트를 하나 이상의 모습으로 관리해야 할 때, 모든 작업을 하나의 프로젝트 폴더에서 진행할 수 있도록 함.

ex) 실배포용, 테스트서버용, 새로운 시도용
여러 작업들이 각각 독립되어 진행될 때

ex) 신기능 1, 신기능 2, 코드개선, 긴급수정 등
각각 작업한 뒤 확정된 것을 메인에 통합

### 브랜치 생성 / 이동 / 삭제하기

- `git branch (브랜치명)`
브랜치 생성하는 명령어

- `git branch`
브랜치 목록 조회

- `git branch -a`
로컬과 원격의 브랜치들 조회

- `git switch (브랜치명)`
해당 브랜치로 이동

- `git switch -c (브랜치명)`
브랜치 생성과 동시에 이동

- `git branch -d (삭제할 브랜치명)`
브랜치 삭제

- `git branch -D (강제 삭제할 브랜치명)`
브랜치 강제 삭제
✅ 다른 브랜치로 가져오지 않은 내용이 있는 브랜치를 지울 경우에 강제 삭제 해야 함

- `git branch -m (기존 브랜치명) (새 브랜치명)`
브랜치 이름 바꾸기

- `git log --all --decorate --oneline --graph`
여러 브랜치의 내역 편리하게 보기

---
## 서로 다른 브랜치를 합치는 방법 두 가지
> - **merge** : 두 브랜치를 한 커밋에 이어붙임. 브랜치 사용내역을 남길 필요가 있을 때 적합한 방식
> - **rebase** : 브랜치를 다른 브랜치에 이어붙임. 한 줄로 깔끔히 정리된 내역을 유지하기 원할 때 적합함.
>   ✅ 이미 팀원과 공유된 커밋들에 대해서는 사용하지 않는 것이 좋음
### merge로 합치기
- `git merge (브랜치명)`
1. main 브랜치로 이동
2. 위의 명령어로 병합
3. `:wq`로 자동입력된 커밋 메시지 저장하여 마무리
✅ merge도 reset으로 되돌리기 가능함

- `git branch -d (브랜치명)`
병합된 브랜치 삭제

### rebase로 합치기
- `git rebase (브랜치명)`
1. 합쳐질 브랜치로 이동
✅ merge때와 반대
2. 위의 명령어로 병합 / main 브랜치는 뒤쳐져 있음
3. main 브랜치로 이동 후 merge로 현재 상황 맞추기
4. 병합된 브랜치 삭제

---

## 브랜치간 충돌 해결

### merge 충돌 해결하기
1. 오류 메시지와 `git status` 확인
2. VS Code에서 해당 부분 확인
3. 충돌 부분을 수정한 뒤 `git add .`, `git commit`으로 병합 완료
4. 당장 해결하기 어려우면 중단하기

- `git merge --abort`
merge 중단

### rebase 충돌 해결하기
1. 오류 메시지와 `git status` 확인
2. VS Code에서 해당 부분 확인
3. 충돌 부분을 수정한 뒤 `git add .`
- `git rebase --continue`
rebase 계속 진행하기

4. main에서 merge로 병합 완료
5. 당장 해결하기 어려우면 중단하기

- `git rebase --abort`
rebase 중단

---
## 원격 저장소 사용하기

### GitHub 레포지토리 생성 후 명령어

- `git remote add (origin) (원격 저장소 주소) `
로컬의 Git 저장소에 원격 저장소로 연결 추가
원격 저장소 이름에 흔히 origin 사용. 다른 것으로 수정 가능

- `git branch -M main`
기본 브랜치명을 main으로 바꿈

- `git push -u (origin) (main) `
현재 브랜치와 명시된 원격 브랜치 기본 연결, 커밋 업로드
`-u` 또는 `--set-upstream`

- `git switch -t (origin)/(원격 브랜치명)`
로컬에 같은 이름의 브랜치를 생성 후 연결하고 switch함

- `git remote`
원격 목록 보기

- `git remote -v`
원격 목록 자세히 보기

- `git remote remove (origin 등 원격 이름)`
원격 지우기
✅ 로컬 프로젝트와의 연결만 없애는 것. GitHub의 레포지토리는 지워지지 않음

- `git fetch`
원격의 변경사항 확인

- `git push (원격 이름) --delete (원격의 브랜치명)`
원격의 브랜치 삭제

### GitHub에서 프로젝트 다운받기
> - Download ZIP: 파일들만 다운받음, Git 관리내역 제외
- **Git clone**: Git 관리내역 포함 다운로드

- `git clone (원격 저장소 주소)`
원격 저장소에서 다운로드를 하는 명령어.

---

## 원격으로 커밋 업로드 / 다운로드 하기

- `git push`
로컬 저장소의 내용을 원격 저장소로 업로드 하는 명령어.
✅ `git push -u (origin) (main)`으로 대상 원격 브랜치가 지정되었을 때 가능

- `git push --force`
원격 저장소에 강제 적용

- `git pull`
로컬 저장소의 내용을 원격 저장소로 다운로드 하는 명령어.

> ✅ 원격에 먼저 적용된 새 버전이 있을 경우 push 불가능함.
> pull 해서 원격의 버전을 받아온 다음 push 가능함

### push 할 것이 있을 때 pull 하는 두 가지 방법

- `git pull --no-rebase` - merge 방식

- `git pull --rebase` - rebase 방식
✅ 협업시 사용해도 됨


---
[git & github 강의](https://www.youtube.com/watch?v=1I3hMwQU6GU&t=319s)
[출처 사이트](https://www.yalco.kr/lectures/git-github/)