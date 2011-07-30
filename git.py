import shlex, subprocess
from subprocess import call

print'Enter reponame'
reponame = raw_input()

print 'make the repo directory'
call(["mkdir",reponame])

print 'initialization'
call(["git","init"],cwd=reponame)


print 'Enter filenames to copy :'
fnames = raw_input()

print 'copying to repository'
call(["cp",fnames,reponame])
print'adding'
subprocess.Popen(["git","add ."],cwd=reponame)

print'Enter the  message'
message = raw_input()

print 'committing added files'
subprocess.Popen(["git","commit","-m"+message],cwd=reponame)
print 'repo url'
url=raw_input()
subprocess.Popen(["git","remote","add","origin"+url],cwd=reponame)

print'Pushing files to repository'

proc=subprocess.Popen(["git","push","origin","-u","master"],cwd=reponame,stdout=subprocess.PIPE,)
stdout_value=proc.communicate()[0]

print' program finishing..'
