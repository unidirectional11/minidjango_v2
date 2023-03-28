### how to open django shell?

`python manage.py shell`    # ORM

### TO GET ALL THE OBJECTS IN TABLE

```python
for obj in Portal.objects.all():
    print(obj)
    
# 1 portal - Naukri.com
# 4 portal - glassdoor.com
# 5 portal - findjob.com
# 6 portal - somenewportal.com

```

### HOW TO FILTER OBJECTS BASED ON CERTAIN COLUMN

```python

Portal.objects.get(name="Naukri.com")
```


### HOW TO CREATE NEW RECORD
```python
Portal.objects.create(name="randomwebsite.com", description="very random")
```


