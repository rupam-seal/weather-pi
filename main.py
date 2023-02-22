import git

repo = git.Repo()

# get all the commits from current repo
commits = list(repo.iter_commits("master"))

command = """"""

# name = input("Name: ")
# email = input("Email: ")

name = "rupam-seal"
email = "rupam.x.seal@gmail.com"


for i in range(len(commits)):
    command += '        ' + \
        f"""[{'"'+str(commits[i].hexsha)+'"'}]={'"'+str(commits[i].authored_datetime)+'" '}""" + '\n'

with open('command.sh', 'a', encoding='utf-8') as file:
    file.write(f"""git filter-branch -f --env-filter \\
'
    declare -A arr
    arr=(\n{command}    )

    for key in ${{!arr[@]}}; do
        if [ $GIT_COMMIT = ${{key}} ]
            then
                export GIT_AUTHOR_DATE=${{arr[${{key}}]}} 
                export GIT_COMMITTER_DATE=${{arr[${{key}}]}}
                export GIT_COMMITTER_NAME="{name}"
                export GIT_COMMITTER_EMAIL="{email}"
                export GIT_AUTHOR_NAME="{name}"
                export GIT_AUTHOR_EMAIL="{email}"
            fi
    done
    '
    """)
