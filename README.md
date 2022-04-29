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
For this exists the `courses` method; it returns a dictionary of **strings** where every course taken by the student in the actual semester is a **Key** and his respective section where the student is is his **Value**.

```python
courses_taken_dict = user.actual_courses()
print(courses_taken_dict)

>>> {
"COURSE_0": "SECTION NUMBER",
"COURSE_1": "SECTION NUMBER",
...
}
```

As well, we have the `nrcs` method; it returns a dictionary of **strings** where every course taken by the student in the actual semester is a **Key** and his respective NRC is his **Value**.

```python
nrcs_list = user.nrcs()
print(nrcs_list)

>>> {
"COURSE_0": "NRC_0",
"COURSE_1": "NRC_1",
...
}
```

### Extra Function

This library possesses a extra function not related to extracting information from "Seguimiento Curricular" but "BuscaCursos". This is the `CourseSchedule` function; requires a NCR from a course in the form of a string and it returns a list of **strings** with the schedule of the course.


