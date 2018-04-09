# My Git cheatsheet

List branches:

``` shell
git branch
git branch -av
```

Switch HEAD to <branch>:

``` shell
git checkout <branch>
```

Create a new branch based on current HEAD:

``` shell
git branch <new_branch> 
```

Create a new tracking branch based on a remote branch:

``` shell
git checkout --track <remote/branch>
```

Push to remote:

``` shell
git push origin <branch_name>
```

Delete local branch:

``` shell
git branch -d feature/login
```

Delete remote branch:

``` shell
git push origin --delete feature/login
```

Rename a file:

``` shell
git mv old_filename new_filename
```

