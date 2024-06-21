# Input/output file.txt in bash shell

Suppose input is in input.txt and you want output in output.txt. Make a python script and name it `sort.py` like this:

```python
l=map(int,raw_input("").strip().split())
l.sort() 
print l  # It will store it as a list

# or more precisely your answer can be
k=""
for i in l:
    k+=str(i)+" "
print k       #same output as you want
```

Run it in the terminal:

```bash
python sort.py < input.txt > output.txt
```
