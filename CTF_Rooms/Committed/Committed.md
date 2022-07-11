# Committed


1. Unzip the zip file provided. The folder has 3 items: `Readme.md`, `main.py`, and `.git/`.

2. `Readme.md`.
```
# Commited
---

## About the Project

Commited is our project created to manage our databases, Commited will bring help our database management team by simplfying database management by using our python scripts.

## Project Status

Completed.

## Team

Our development team consists of finest developers and we work simultaneously using our cool version control methodology. We are the BEST.
```

3. `main.py`. Simply manages mysql database. Maybe the username/password was accidentally committed previously?
```
import mysql.connector

def create_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="", # Username Goes Here
    password="" # Password Goes Here
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE commited")


def create_tables():
    mydb = mysql.connector.connect(
    host="localhost",
    user="", #username Goes here
    password="", #password Goes here
    database="commited"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


def populate_tables():
    mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="commited"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


create_db()
create_tables()
populate_tables()
```

4. `.git` contains these files/folders.
```
COMMIT_EDITMSG  HEAD  branches  config  description  hooks  index  info  logs  objects  refs
```

5. Use `git status` to find that there's nothing to commit.
```
ubuntu@thm-comitted:~/commited/commited$ git status
On branch master
nothing to commit, working tree clean
```

6. Using `git log` shows us these commits. None of the commit messages indicate that there was any confidential information leaked.
```
commit 28c36211be8187d4be04530e340206b856198a84 (HEAD -> master)
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:49:32 2022 -0800

    Finished

commit 9ecdc566de145f5c13da74673fa3432773692502
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:40:19 2022 -0800

    Database management features added.

commit 26bcf1aa99094bf2fb4c9685b528a55838698fbe
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:32:49 2022 -0800

    Create database logic added

commit b0eda7db60a1cb0aea86f053816a1bfb7e2d6c67
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:30:43 2022 -0800

    Connecting to db logic added

commit 441daaaa600aef8021f273c8c66404d5283ed83e
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:28:16 2022 -0800

    Initial Project.
```

7. Use `git branch` and find that there are two branches.
```
ubuntu@thm-comitted:~/commited/commited$ git branch
  dbint
* master
```

8. Switch to the `dbint` branch with `git checkout dbint`. There's a file called `Note` that indicates that a password might have been hardcoded.
```
# Branch DBint

This branch is being used to test the code with the mysql server.

## Reminder

Please don't hardcode password, use enviroment variables where possible.
```

9. Use `git log` and find that there's a commit message called `Oops`.
```
ubuntu@thm-comitted:~/commited/commited$ git log
commit 4e16af9349ed8eaa4a29decd82a7f1f9886a32db (HEAD -> dbint)
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:48:08 2022 -0800

    Reminder Added.

commit c56c470a2a9dfb5cfbd54cd614a9fdb1644412b5
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:46:39 2022 -0800

    Oops

commit 3a8cc16f919b8ac43651d68dceacbb28ebb9b625
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:45:14 2022 -0800

    DB check

commit 6e1ea88319ae84175bfe953b7791ec695e1ca004
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:43:34 2022 -0800

    Note added

commit 9ecdc566de145f5c13da74673fa3432773692502
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:40:19 2022 -0800

    Database management features added.

commit 26bcf1aa99094bf2fb4c9685b528a55838698fbe
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:32:49 2022 -0800

    Create database logic added

commit b0eda7db60a1cb0aea86f053816a1bfb7e2d6c67
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:30:43 2022 -0800

    Connecting to db logic added

commit 441daaaa600aef8021f273c8c66404d5283ed83e
Author: fumenoid <fumenoid@gmail.com>
Date:   Sun Feb 13 00:28:16 2022 -0800

    Initial Project.
```

10. Use `git reset --hard HEAD~1` twice or `git reset --hard HEAD~2` to undo the commits and view the code before the commit with the message `Oops`. Now when we check `main.py` we find the flag in the `password` section: `flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}`.
