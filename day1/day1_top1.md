![Alt text](image-1.png)
So basically ended up as rank 1 but let me review other codes

Many ended up making code like my first attempt...
then this struck me

```
L = []
for i in range(input()):
    line = raw_input().split()
    if len(line) == 3:
        arg = 'L.' + line[0] + '(' + line[1] + ', ' + line[2] + ')'
    elif len(line) == 1:
        if line[0] == 'print':
            arg = 'print L'
        else:
            arg = 'L.' + line[0] + '()'
    elif len(line) == 2:
        arg = 'L.' + line[0] + '(' + line[1] + ')'
    
    exec(arg)
```
close to my second approach and uses exec

The short answer, or TL;DR
Basically, eval is used to evaluate a single dynamically generated Python expression, and exec is used to execute dynamically generated Python code only for its side effects.

I couldn't find anything else better...