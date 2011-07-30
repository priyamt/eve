import shlex, subprocess
from subprocess import call


print 'Enter repository address :' 
repo = raw_input()
call("hg clone "+repo, shell=True)


print 'Enter filenames to copy :'
fnames = raw_input()
files_list=shlex.split(fnames)


print'Enter reponame'
reponame = raw_input()


print 'copying to repository'
for i in range(len(files_list)):
	call(["cp",files_list[i],reponame])

print'adding'
subprocess.Popen(["hg", "add"],cwd=reponame)

print'Enter Username of bitbucket'
username = raw_input()
print'Enter a  passphrase'
passphrase = raw_input()

print 'committing added files'
subprocess.Popen(["hg","commit","-u",username,"-Am",passphrase],cwd=reponame)

print'Pushing files to repository'
print'Enter username'
proc=subprocess.Popen(["hg","push"],cwd=reponame,stdout=subprocess.PIPE,)
stdout_value=proc.communicate()[0]

print' program finishing..'
