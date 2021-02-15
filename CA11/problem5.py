# Problem5

# Write a function ext_sort(filelist) which sorts and returns a list of filenames based on their extensions.

# Input: filelist = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'] and call ext_sort(filelist)
# Return: ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']

def ext_sort(filelist):
    x=sorted(filelist,key=lambda x: x[x.find('.'):])     #substring from . to end
    print(x)        


filelist = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
ext_sort(filelist)  