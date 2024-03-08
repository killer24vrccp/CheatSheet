## Python re (Regular Expression)
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern. <br>
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

----------------------------------------
### Metacharacters


| Character |Description|    Example     |    Context     |       Output       |
|:---------:|-----|:--------------:|:--------------:|:------------------:|
|    [ ]    |A set of characters|    "Hello"     |    "[h-o]"     | `['l', 'l', 'o']`  |
|     \     |Signals a special sequence (can also be used to escape special characters)|   "Hello56"    |      "\d"      |    `['5', '6']`    |
|     .     |Any character (except newline character)| "hello planet" |    "he..o"     |    `['hello']`     |
|     ^     |Starts with| "hello planet" |     "^hel"     |       `True`       |
|     $     |Ends with| "hello planet" |     "net$"     |       `True`       |
|     *     |Zero or more occurrences| "hello planet" |    "he.*o"     |    `['hello']`     |
|     +     |One or more occurrences| "hello planet" |    "he.+o"     |    `['hello']`     |
|     ?     |Zero or one occurrences| "hello planet" |    "he.?o"     |        `[]`        |
|    {}     |Exactly the specified number of occurrences| "hello planet" |   "he.{2}o"    |    `['hello']`     |
|    \|     |Either or| "The rain in Spain falls mainly in the plain!" | "falls\|stays" |`['falls']`|
|    ()     |Capture and group|   "he.{2}o"    |


-------------------------------------------
### Special Sequences

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

| Character |Description| Example             |  Context  | Output |
|:---------:|-----|---------------------|:---------:|:------:|
|    \A     |  Returns a match if the specified characters are at the beginning of the string   | "The rain"          | r"\AThe"  |   `['The']`   |
|    \b     |   Returns a match where the specified characters are at the beginning or at the end of a word  | "The rain in Spain" | r"ain\b"  |`['ain', 'ain']`|
|    \B     |   Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word  | "The brain of aint" | r"\Bain"  |`['ain']`|
|    \d     |   Returns a match where the string contains digits (numbers from 0-9)  |"The rain in Spain of 1970"|   "\d"    |`['1', '9', '7', '0']`|
|    \D     |   Returns a match where the string DOES NOT contain digits  |"Colt 44"|   "\D"    |`['C', 'o', 'l', 't', ' ']`|
|    \s     |   Returns a match where the string contains a white space character  |"The rain in Spain"|   "\s"    |`[' ', ' ', ' ']`|
|    \w     |   Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)  |"My colt 44"|   "\w"    |`['M', 'y', 'c', 'o', 'l', 't', '4', '4']`|
|    \W     |   Returns a match where the string DOES NOT contain any word characters  |"My IP 127.0.0.1"|   "\W"    |`[' ', ' ', '.', '.', '.']`|
|    \Z     |   Returns a match if the specified characters are at the end of the string  |"The rain in Spain"| "Spain\Z" |`['Spain']`|

> [!NOTE]  
> The "r" in the beginning is making sure that the string is being treated as a "raw string"