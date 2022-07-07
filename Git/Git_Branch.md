# 📘 Git branch

>독립적으로 작업을 진행하기 위한 개념. 필요에 의해 만들어지는 각각의 브랜치는 다른 브랜치의 영향을 받지 않기 때문에, 여러 작업을 동시에 진행할 수 있다.



## Git flow

> Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의미한다.

- `master (main)`

  - 배포 가능한 상태의 코드

- `develop (main)`

  - feature branch로 나뉘어지거나, 발생된 버그 수정 등 개발 진행

  - 개발 이후 release branch로 갈라짐.

- `feature branches (supporting)`

  - 기능별 개발 브랜치(topic branch)
  - 기능이 반영되거나 드랍되는 경우 브랜치 삭제

- `release branches (supporting)`

  - 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등 반영

- `hotfixes (supporting)`

  - 긴급하게 반영 해야하는 bug fix
  - release branch는 다음 버전을 위한 것 이라면, hotfix branch는 현재 버전을 위한 것




## branch 관련 명령어

> Git 브랜치를 위해 root-commit을 발생시키고 진행해야함.

```bash
$ git init
(master) $ touch README.md
(master) $ git add .
(master) $ git commit -m 'Init'
```

1. 브랜치 생성

   ```bash
   (master) $ git branch {브랜치명}
   ```

2. 브랜치 이동

   ```bash
   (master) $ git checkout {브랜치명}
   ```

3. 브랜치 생성 및 이동

   ```bash
   (master) $ git checkout -b {브랜치명}
   ```

4. 브랜치 삭제

   ```bash
   (master) $ git branch -d {브랜치명}
   ```

5. 브랜치 목록

   ```bash
   (master) $ git branch
   ```

6. 브랜치 병합

   ```bash
   (master) $ git merge {브랜치명}
   ```

   * master(HEAD) 브랜치에서 {브랜치명}을 병합
     * HEAD(머리) : 현재 내가 위치하고 있는 브랜치 정보



### merge

> 각 branch에서 작업을 한 이후 이력을 합치기 위해서는 일반적으로 merge 명령어를 사용한다.

- 병합을 진행할 때, 만약 서로 다른 이력(commit)에서 동일한 파일을 수정한 경우 충돌이 발생할 수 있다. 이 경우에는 반드시 직접 수정을 진행 해야 한다.
- 병합된 브랜치는 의미가 없으므로 삭제한다.



## branch 병합 시나리오

### 상황 1. fast-foward

> fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황



1. feature/home branch 생성 및 이동

   ```bash
   (master) $ git branch feature/home
   (master) $ git checkout feature/home
   ```

2. 작업 완료 후 commit

   ```bash
   (feature/home) $ touch home.txt
   (feature/home) $ git add .
   (feature/home) $ git commit -m 'Add home.txt'
   ```


3. master 이동

   ```bash
   (feature/home) $ git checkout master
   ```

4. master에 병합

   ```bash
   (master) $ git merge feature/home 
   ```

5. 결과 : fast-foward

   ```bash
   (master) $ git log --oneline
   b534a34 (HEAD -> master, feature/home) Complete Home!!!!
   e89616a Init
   ```

6. branch 삭제

   ```bash
   (master) $ git branch -d feature/home 
   ```

   

---

### 상황 2. merge commit

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 **다른 파일이 수정**되어 있는 상황
>
> git이 auto merging을 진행하고, **commit이 발생된다.**



1. feature/about branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/about
   ```

2. 작업 완료 후 commit

   ```bash
   (feature/about) $ touch about.txt
   (feature/about) $ git add .
   (feature/about) $ git commit -m 'Add about.txt'
   ```

3. master 이동

   ```bash
   (feature/about) $ git checkout master
   ```

4. master에 추가 commit을 발생시키기

   * **다른 파일을 수정 혹은 생성**

   ```bash
   (master) $ touch master.txt
   (master) $ git add .
   (master) $ git commit -m 'Add master.txt'
   ```

5. master에 병합

   ```bash
   (master) $ git merge feature/about
   ```

6. 결과 -> **자동으로 *merge commit 발생***

7. 커밋 및 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   582902d (HEAD -> master) Merge branch 'feature/about'
   |\
   | * 5e1f6de (feature/about) 자기소개 페이지 완료!
   * | 98c5528 마스터 작업....
   |/
   * b534a34 Complete Home!!!!
   * e89616a Init
   ```

8. branch 삭제

   ```bash
   $ git branch -d feature/about 
   ```

   

---

### 상황 3. merge commit 충돌

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 **같은 파일의 동일한 부분이 수정**되어 있는 상황
>
> git이 auto merging을 하지 못하고, 충돌 메시지가 뜬다.
>
> 해당 파일의 위치에 표준형식에 따라 표시 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 직접 commit을 발생 시켜야 한다.



1. feature/test branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/test
   ```

2. 작업 완료 후 commit

   ```bash
   # README.md 파일 열어서 수정
   (feature/test) $ touch test.txt
   (feature/test) $ git add .
   (feature/test) $ git commit -m 'Add test.txt'
   ```


3. master 이동

   ```bash
   $ git checkout master
   ```

4. master에 추가 commit을 발생시키기

   * **다른 파일을 수정 혹은 생성**

   ```bash
   # README.md 파일 열어서 수정
   (master) $ git add README.md
   (master) $ git commit -m 'Update README.md'
   ```

5. master에 병합

   ```bash
   (master) $ git merge feature/test 
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```

6. 결과 -> *merge conflict발생*

   > git status 명령어로 충돌 파일을 확인할 수 있음.

   ```bash
   (master|MERGING) $ git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")        
     (use "git merge --abort" to abort the merge)
   
   Changes to be committed:
           new file:   test-1.txt
           new file:   test-2.txt
           new file:   test.txt
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   README.md
   ```

7. 충돌 확인 및 해결

   ```
   <<<<<<< HEAD
   # 마스터에서 작업함...
   =======
   # 테스트에서 작성
   >>>>>>> feature/test
   ```

   - 내가 직접 수정 하기


8. merge commit 진행

   ```bash
   (master|MERGING) $ git add .
   (master|MERGING) $ git commit
   ```

   * vim 편집기 화면이 나타남

     * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료
     * `w` : write
     * `q` : quit

   * vs code 편집기에서 메시지보고 닫기

9. 커밋 및 확인하기

   ```bash
   (master) $ git log --oneline --graph
   *   bc1c0cd (HEAD -> master) Merge branch 'feature/test'
   |\  
   | * 95fad1c (feature/test) README 수정하고 test 작성하고
   * | 2ecad28 리드미 수정
   |/  
   *   582902d Merge branch 'feature/about'
   |\  
   | * 5e1f6de 자기소개 페이지 완료!
   * | 98c5528 마스터 작업....
   |/  
   * b534a34 Complete Home!!!!
   * e89616a Init
   ```


10. branch 삭제

    ```bash
    (master) $ git branch -d feature/test
    ```




## pull request

> 다른 사람의 원격 저장소를 받고 내가 작업한 commit을 push한 후 해당 원격 저장소의 소유자에게 pull할 것을 요청하는 것.
>
> 소유자가 수락하면 병합됨.



## fork

> 다른 사람의 원격 저장소를 내 원격 저장소로 가져오는 것



## Feature Branch Workflow

>Shared repository model (저장소의 소유권이 있는 경우)



1. 각 사용자는  원격 저장소의 소유권을 가져서 clone으로 로컬에 복제
2. branch 생성 및 기능 구현
3. 원격 저장소로 push
4. 원격 저장소에서 pull request로 병합함
5. 원격 저장소에서 병합 완료된 branch 삭제
6. master bransh로 switch
7. 병합된 master을 로컬로 pull
8. 병합된 로컬 branch 삭제



## Forking Workflow

> Fork & Pull model (저장소의 소유권이 없는 경우)



1. 소유권이 없는 원격 저장소를 fork를 통해 내 원격 저장소에 복제

2. clone으로 로컬에 복제

3. 로컬 저장소와 원본 원격 저장소 동기화를 위해 url 연결

   ``` bash
   git remote add upstream (원본 url)

4. branch 생성 및 기능 구현

5. 내 원격 저장소로 push

6. pull request

7. 원본 원격 저장소에서 pull request 수락 및 병합

8. 병합 완료된 branch 삭제

9. master bransh로 switch

10. 병합된 master을 로컬로 pull

    ```bash
     git pull upstream master
    ```

11. 병합된 로컬 branch 삭제