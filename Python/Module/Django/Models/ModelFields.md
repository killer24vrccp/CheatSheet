### Models Fields 

Make sure the models dependence is present in  your `models.py`.

```python 
from django.db import models
```

How create a new model exemple:

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_lenght=20)
```

### Relationships

#### OneToOneField 
Used for a "one-to-one" relationship, where an object can be linked to one (and only one) other object,
and this object can be linked to one (and only one) other object. For example, each user can
have a profile, and each profile is linked to one (and only one) user. This would be represented
like a OneToOneField.

#### ForeignKey
Used for a "many-to-one" relationship, where one object can be related to another object, but not vice versa. 
It's like a parent/child relationship. For example, each entry in a blog can be linked to an author, but an 
author can have multiple entries. This would be represented as a ForeignKey.

#### ManyToManyField 
Used for a "many-to-many" relationship, where one object can be linked to several other objects, and those 
objects can also be linked to several others. For example, in a blog application, an article could have 
multiple authors, and each author could write multiple articles. This would be represented as a ManyToManyField.

### No Relationships

#### Charfield
