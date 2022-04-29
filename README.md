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
This is the principal class of the library.

## Obtaining information

After setting up the class in your virtual enviorement, you should want to obtain the information.
For this we have two methods:

```python
user.sections()
```

```python
user.nrcs()
```

### Methods

The `sections` method; it returns a dictionary of **strings** where every course taken by the student in the actual semester is a **Key** and his respective section where the student is is his **Value**.

```python
courses_sections_dict = user.sections()
print(courses_sections_dict)

>>> {
"COURSE_0": "SECTION NUMBER",
"COURSE_1": "SECTION NUMBER",
...
}
```

Meanwhile, the `nrcs` method it returns a dictionary of **strings** where every course taken by the student in the actual semester is a **Key** and his respective NRC is his **Value**.

```python
courses_nrcs_dict = user.nrcs()
print(courses_nrcs_dict)

>>> {
"COURSE_0": "NRC_0",
"COURSE_1": "NRC_1",
...
}
```

### Auxiliary Function

This library possesses an extra function not related to extracting information from "Seguimiento Curricular" but "BuscaCursos". This is the `CourseSchedule` function; requires a NCR from a course in the form of a string and it returns a dictionary of **strings** with the schedule of every activity of the course.

```python
from ucurriculum_student import CourseSchedule

schedule = CourseSchedule("EXAMPLE_NRC")
print(schedule)

>>> {
    "CLAS": "L-W-J:3",
    "AYU": "M:3",
    ...
}
```