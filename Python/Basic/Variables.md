## Variable
Variable In Python is very easy to use and create.
Variable is for store specific data to use by the code.

### Integer
Integer variable is for manipulate number by exemple `198`.

```python
a = 123
a = int(123)  # same declaration
```

We can convert string number to integer.
But if the string have one letter the program raise one error because you
***can't convert letter to integer.***

```python
a = "24"
a = int(a)  # Convert 'a' variable to int
```

### String
String variable is for manipulate string by exemple `Hello World`.

```python
a = "Hello World"
a = str("Hello World")  # same declaration
```

### Boolean
Boolean variable is for manipulate boolean. Boolean it have two 
possibilities `True` or `False`.
>True is 1 False is 0.

```python
a = True
a = bool(True)  # same declaration
```

We can convert Boolean to Integer.

```python 
a = True
a = int(a)
```

### Float
Float variable is for manipulate number by exemple `198.01`.

```python
a = 198.01
a = float(198.01)  # same declaration
```

### List
List variable is for manipulation one list by exemple `['2', 'string']`
We can store all variable type in the list in same variable.

```pycon
a = [1, 'string', True, 1.15, [1,2,3], {"var":"1"}]
```

#### Manipulation

```python
a = [2,7,8]
print(a[2])

output: 8
```

### Dictionary
Dictionary variable is for manipulation one Dict by exemple `{'myvar':'My Texte'}`
We can store all variable type in the list in same variable.

```pycon
a = {
    'First_var':'Hello',
    'Second_Var':10,
    'Third_Var':1.72,
    'Four_Var':True,
    'Five_Var':[1,4,8,2.51,{
    'dev':'Ced',
    'version':'v.1.0.1'
    }]
}
```

#### Manipulation

```python
a = {
    'First_var':'Hello',
    'Five_Var':[1,4,8,2.51,{
    'dev':'Ced',
    'version':'v.1.0.1'
    }]
}

print(a['Five_Var'][0]['version'])
```
### Tuple