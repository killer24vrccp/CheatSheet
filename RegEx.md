## Python re (Regular Expression)

For use re you must be import module.

```python
import re
```


### RegEx Functions 
|Function|Description|
|-----|-----|
|findall|Returns a list containing all matches|
|search|Returns a Match object if there is a match anywhere in the string|
|split|Returns a list where the string has been split at each match| 
|sub|Replaces one or many matches with a string|


Exemple:

```python
import re 

split_term = "@"
email = "myemail@exemple.com"

print(re.split(split_term,email))
```