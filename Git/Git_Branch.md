# ๐ณ Git branch

>๋๋ฆฝ์ ์ผ๋ก ์์์ ์งํํ๊ธฐ ์ํ ๊ฐ๋. ํ์์ ์ํด ๋ง๋ค์ด์ง๋ ๊ฐ๊ฐ์ ๋ธ๋์น๋ ๋ค๋ฅธ ๋ธ๋์น์ ์ํฅ์ ๋ฐ์ง ์๊ธฐ ๋๋ฌธ์, ์ฌ๋ฌ ์์์ ๋์์ ์งํํ  ์ ์๋ค.



## Git flow

> Git์ ํ์ฉํ์ฌ ํ์ํ๋ ํ๋ฆ์ผ๋ก branch๋ฅผ ํ์ฉํ๋ ์ ๋ต์ ์๋ฏธํ๋ค.

- `master (main)`

  - ๋ฐฐํฌ ๊ฐ๋ฅํ ์ํ์ ์ฝ๋

- `develop (main)`

  - feature branch๋ก ๋๋์ด์ง๊ฑฐ๋, ๋ฐ์๋ ๋ฒ๊ทธ ์์  ๋ฑ ๊ฐ๋ฐ ์งํ

  - ๊ฐ๋ฐ ์ดํ release branch๋ก ๊ฐ๋ผ์ง.

- `feature branches (supporting)`

  - ๊ธฐ๋ฅ๋ณ ๊ฐ๋ฐ ๋ธ๋์น(topic branch)
  - ๊ธฐ๋ฅ์ด ๋ฐ์๋๊ฑฐ๋ ๋๋๋๋ ๊ฒฝ์ฐ ๋ธ๋์น ์ญ์ 

- `release branches (supporting)`

  - ๊ฐ๋ฐ ์๋ฃ ์ดํ QA/Test ๋ฑ์ ํตํด ์ป์ด์ง ๋ค์ ๋ฐฐํฌ ์  minor bug fix ๋ฑ ๋ฐ์

- `hotfixes (supporting)`

  - ๊ธด๊ธํ๊ฒ ๋ฐ์ ํด์ผํ๋ bug fix
  - release branch๋ ๋ค์ ๋ฒ์ ์ ์ํ ๊ฒ ์ด๋ผ๋ฉด, hotfix branch๋ ํ์ฌ ๋ฒ์ ์ ์ํ ๊ฒ




## branch ๊ด๋ จ ๋ช๋ น์ด

> Git ๋ธ๋์น๋ฅผ ์ํด root-commit์ ๋ฐ์์ํค๊ณ  ์งํํด์ผํจ.

```bash
$ git init
(master) $ touch README.md
(master) $ git add .
(master) $ git commit -m 'Init'
```

1. ๋ธ๋์น ์์ฑ

   ```bash
   (master) $ git branch {๋ธ๋์น๋ช}
   ```

2. ๋ธ๋์น ์ด๋

   ```bash
   (master) $ git checkout {๋ธ๋์น๋ช}
   ```

3. ๋ธ๋์น ์์ฑ ๋ฐ ์ด๋

   ```bash
   (master) $ git checkout -b {๋ธ๋์น๋ช}
   ```

4. ๋ธ๋์น ์ญ์ 

   ```bash
   (master) $ git branch -d {๋ธ๋์น๋ช}
   ```

5. ๋ธ๋์น ๋ชฉ๋ก

   ```bash
   (master) $ git branch
   ```

6. ๋ธ๋์น ๋ณํฉ

   ```bash
   (master) $ git merge {๋ธ๋์น๋ช}
   ```

   * master(HEAD) ๋ธ๋์น์์ {๋ธ๋์น๋ช}์ ๋ณํฉ
     * HEAD(๋จธ๋ฆฌ) : ํ์ฌ ๋ด๊ฐ ์์นํ๊ณ  ์๋ ๋ธ๋์น ์ ๋ณด



### merge

> ๊ฐ branch์์ ์์์ ํ ์ดํ ์ด๋ ฅ์ ํฉ์น๊ธฐ ์ํด์๋ ์ผ๋ฐ์ ์ผ๋ก merge ๋ช๋ น์ด๋ฅผ ์ฌ์ฉํ๋ค.

- ๋ณํฉ์ ์งํํ  ๋, ๋ง์ฝ ์๋ก ๋ค๋ฅธ ์ด๋ ฅ(commit)์์ ๋์ผํ ํ์ผ์ ์์ ํ ๊ฒฝ์ฐ ์ถฉ๋์ด ๋ฐ์ํ  ์ ์๋ค. ์ด ๊ฒฝ์ฐ์๋ ๋ฐ๋์ ์ง์  ์์ ์ ์งํ ํด์ผ ํ๋ค.
- ๋ณํฉ๋ ๋ธ๋์น๋ ์๋ฏธ๊ฐ ์์ผ๋ฏ๋ก ์ญ์ ํ๋ค.



## branch ๋ณํฉ ์ํฉ

### 1. fast-foward

> fast-foward๋ feature ๋ธ๋์น ์์ฑ๋ ์ดํ master ๋ธ๋์น์ ๋ณ๊ฒฝ ์ฌํญ์ด ์๋ ์ํฉ

1. feature branch ์์ฑ ๋ฐ ์ด๋

   ```bash
   (master) $ git branch feature
   (master) $ git checkout feature
   ```

2. ์์ ์๋ฃ ํ commit

   ```bash
   (feature) $ touch home.txt
   (feature) $ git add .
   (feature) $ git commit -m 'Add home.txt'
   ```


3. master ์ด๋

   ```bash
   (feature) $ git checkout master
   ```

4. master์ ๋ณํฉ

   ```bash
   (master) $ git merge feature
   ```

5. ๊ฒฐ๊ณผ : fast-foward

   ```bash
   (master) $ git log --oneline
   b534a34 (HEAD -> master, feature)
   ```
   
6. branch ์ญ์ 

   ```bash
   (master) $ git branch -d feature 
   ```

   

---

### 2. merge commit

> ์๋ก ๋ค๋ฅธ ์ด๋ ฅ(commit)์ ๋ณํฉ(merge)ํ๋ ๊ณผ์ ์์ **๋ค๋ฅธ ํ์ผ์ด ์์ **๋์ด ์๋ ์ํฉ
>
> git์ด auto merging์ ์งํํ๊ณ , **commit์ด ๋ฐ์๋๋ค.**

1. feature/a branch ์์ฑ ๋ฐ ์ด๋

   ```bash
   (master) $ git checkout -b feature/a
   ```

2. ์์ ์๋ฃ ํ commit

   ```bash
   (feature/a) $ touch about.txt
   (feature/a) $ git add .
   (feature/a) $ git commit -m 'Add about.txt'
   ```

3. master ์ด๋

   ```bash
   (feature/a) $ git checkout master
   ```

4. master์ ์ถ๊ฐ commit์ ๋ฐ์์ํค๊ธฐ

   * **๋ค๋ฅธ ํ์ผ์ ์์  ํน์ ์์ฑ**

   ```bash
   (master) $ touch master.txt
   (master) $ git add .
   (master) $ git commit -m 'Add master.txt'
   ```

5. master์ ๋ณํฉ

   ```bash
   (master) $ git merge feature/a
   ```

6. ๊ฒฐ๊ณผ -> **์๋์ผ๋ก *merge commit ๋ฐ์***

7. ์ปค๋ฐ ๋ฐ ๊ทธ๋ํ ํ์ธํ๊ธฐ

   ```bash
   $ git log --oneline --graph
   *   582902d (HEAD -> master) Merge branch 'feature/a'
   ```
   
8. branch ์ญ์ 

   ```bash
   $ git branch -d feature/a 
   ```

   

---

### 3. merge commit ์ถฉ๋

> ์๋ก ๋ค๋ฅธ ์ด๋ ฅ(commit)์ ๋ณํฉ(merge)ํ๋ ๊ณผ์ ์์ **๊ฐ์ ํ์ผ์ ๋์ผํ ๋ถ๋ถ์ด ์์ **๋์ด ์๋ ์ํฉ
>
> git์ด auto merging์ ํ์ง ๋ชปํ๊ณ , ์ถฉ๋ ๋ฉ์์ง๊ฐ ๋ฌ๋ค.
>
> ํด๋น ํ์ผ์ ์์น์ ํ์คํ์์ ๋ฐ๋ผ ํ์ ํด์ค๋ค.
>
> ์ํ๋ ํํ์ ์ฝ๋๋ก ์ง์  ์์ ์ ํ๊ณ  ์ง์  commit์ ๋ฐ์ ์์ผ์ผ ํ๋ค.

1. feature/test branch ์์ฑ ๋ฐ ์ด๋

   ```bash
   (master) $ git checkout -b feature/test
   ```

2. ์์ ์๋ฃ ํ commit

   ```bash
   # README.md ํ์ผ ์ด์ด์ ์์ 
   (feature/test) $ touch test.txt
   (feature/test) $ git add .
   (feature/test) $ git commit -m 'Add test.txt'
   ```


3. master ์ด๋

   ```bash
   $ git checkout master
   ```

4. master์ ์ถ๊ฐ commit์ ๋ฐ์์ํค๊ธฐ

   * **๋ค๋ฅธ ํ์ผ์ ์์  ํน์ ์์ฑ**

   ```bash
   # README.md ํ์ผ ์ด์ด์ ์์ 
   (master) $ git add README.md
   (master) $ git commit -m 'Update README.md'
   ```

5. master์ ๋ณํฉ

   ```bash
   (master) $ git merge feature/test 
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```

6. ๊ฒฐ๊ณผ -> *merge conflict๋ฐ์*

   > git status ๋ช๋ น์ด๋ก ์ถฉ๋ ํ์ผ์ ํ์ธํ  ์ ์์.

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

7. ์ถฉ๋ ํ์ธ ๋ฐ ํด๊ฒฐ

   ```
   <<<<<<< HEAD
   # ๋ง์คํฐ์์ ์์ํจ...
   =======
   # ํ์คํธ์์ ์์ฑ
   >>>>>>> feature/test
   ```

   - ๋ด๊ฐ ์ง์  ์์  ํ๊ธฐ


8. merge commit ์งํ

   ```bash
   (master|MERGING) $ git add .
   (master|MERGING) $ git commit
   ```

   * vim ํธ์ง๊ธฐ ํ๋ฉด์ด ๋ํ๋จ

     * ์๋์ผ๋ก ์์ฑ๋ ์ปค๋ฐ ๋ฉ์์ง๋ฅผ ํ์ธํ๊ณ , `esc`๋ฅผ ๋๋ฅธ ํ `:wq`๋ฅผ ์๋ ฅํ์ฌ ์ ์ฅ ๋ฐ ์ข๋ฃ
     * `w` : write
     * `q` : quit

   * vs code ํธ์ง๊ธฐ์์ ๋ฉ์์ง๋ณด๊ณ  ๋ซ๊ธฐ

9. ์ปค๋ฐ ๋ฐ ํ์ธํ๊ธฐ

   ```bash
   (master) $ git log --oneline --graph
   *   bc1c0cd (HEAD -> master) Merge branch 'feature/test'
   ```


10. branch ์ญ์ 

    ```bash
    (master) $ git branch -d feature/test
    ```




## pull request

> ๋ค๋ฅธ ์ฌ๋์ ์๊ฒฉ ์ ์ฅ์๋ฅผ ๋ฐ๊ณ  ๋ด๊ฐ ์์ํ commit์ pushํ ํ ํด๋น ์๊ฒฉ ์ ์ฅ์์ ์์ ์์๊ฒ pullํ  ๊ฒ์ ์์ฒญํ๋ ๊ฒ.
>
> ์์ ์๊ฐ ์๋ฝํ๋ฉด ๋ณํฉ๋จ.



## fork

> ๋ค๋ฅธ ์ฌ๋์ ์๊ฒฉ ์ ์ฅ์๋ฅผ ๋ด ์๊ฒฉ ์ ์ฅ์๋ก ๊ฐ์ ธ์ค๋ ๊ฒ



## Feature Branch Workflow

>Shared repository model (์ ์ฅ์์ ์์ ๊ถ์ด ์๋ ๊ฒฝ์ฐ)



1. ๊ฐ ์ฌ์ฉ์๋  ์๊ฒฉ ์ ์ฅ์์ ์์ ๊ถ์ ๊ฐ์ ธ์ clone์ผ๋ก ๋ก์ปฌ์ ๋ณต์ 
2. branch ์์ฑ ๋ฐ ๊ธฐ๋ฅ ๊ตฌํ
3. ์๊ฒฉ ์ ์ฅ์๋ก push
4. ์๊ฒฉ ์ ์ฅ์์์ pull request๋ก ๋ณํฉํจ
5. ์๊ฒฉ ์ ์ฅ์์์ ๋ณํฉ ์๋ฃ๋ branch ์ญ์ 
6. master bransh๋ก switch
7. ๋ณํฉ๋ master์ ๋ก์ปฌ๋ก pull
8. ๋ณํฉ๋ ๋ก์ปฌ branch ์ญ์ 



## Forking Workflow

> Fork & Pull model (์ ์ฅ์์ ์์ ๊ถ์ด ์๋ ๊ฒฝ์ฐ)



1. ์์ ๊ถ์ด ์๋ ์๊ฒฉ ์ ์ฅ์๋ฅผ fork๋ฅผ ํตํด ๋ด ์๊ฒฉ ์ ์ฅ์์ ๋ณต์ 

2. clone์ผ๋ก ๋ก์ปฌ์ ๋ณต์ 

3. ๋ก์ปฌ ์ ์ฅ์์ ์๋ณธ ์๊ฒฉ ์ ์ฅ์ ๋๊ธฐํ๋ฅผ ์ํด url ์ฐ๊ฒฐ

   ``` bash
   git remote add upstream (์๋ณธ url)

4. branch ์์ฑ ๋ฐ ๊ธฐ๋ฅ ๊ตฌํ

5. ๋ด ์๊ฒฉ ์ ์ฅ์๋ก push

6. pull request

7. ์๋ณธ ์๊ฒฉ ์ ์ฅ์์์ pull request ์๋ฝ ๋ฐ ๋ณํฉ

8. ๋ณํฉ ์๋ฃ๋ branch ์ญ์ 

9. master bransh๋ก switch

10. ๋ณํฉ๋ master์ ๋ก์ปฌ๋ก pull

    ```bash
     git pull upstream master
    ```

11. ๋ณํฉ๋ ๋ก์ปฌ branch ์ญ์ 