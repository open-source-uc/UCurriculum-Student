# UCurriculum-Student🧍

Python library dedicated to extract the information from the "Seguimiento Curricular" page of the Pontifical Catholic University of Chile (UC); in particular, the actual courses taken by a student. *Note that this only works for the first degree that appears in "Seguimiento Curricular" dropdown menu.*

## Installation

For the installation of the library, use:

```shell
$ pip install ucurriculum-student
```

## Getting Started

After installing UCurriculum-Student, you can start using it from Python like this:

```python
from ucurriculum_student import Student

user = Student("USERNAME", "PASSWORD")
```
Were `USERNAME` and `PASSWORD` refers to the username and password, respectively, for accesing SSO-UC.

### Obtaining information

After setting up the class in your virtual enviorement, you should want to obtain the information. For now, the library possesses only one method.
This is the `courses` method; it returns a dictionary where every course taken by the student in the actual semester is a **Key** and his respective section where the student is is his **Value**.

```python
courses_taken_dict = user.actual_courses()
print(courses_taken_dict)

>>> {
"COURSE_0": "SECTION NUMBER",
"COURSE_1": "SECTION NUMBER",
...
}
```

As well, we have the `nrcs` method; it returns a list with every NRC that the student is right now.

```python
nrcs_list = user.nrcs()
print(nrcs_list)

>>> [
"NRC_0",
"NRC_1",
...
]
```







*
