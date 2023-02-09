# db-hack
The project is designed to edit data in the school database

## Installation
First you need to launch a website with an electronic diary. You can install and run the site by following the [instructions](https://github.com/devmanorg/e-diary#readme)
Then copy `scripts.py` from this repository and put it in website project folder

## How to run
For a correct work of scripts you should copy imports from the top of `scripts.py` file and paste them in your `shell`
In `sripts.py` we have three main functions:

- fix_marks()
This function corrects bad marks of a student for fives.
By default it corrects marks for `Фролов Иван`. If you want to change a student, just enter needed students name as `Last name First name`

```shell
fix_marks('Голубев Феофан')
```

- remove_chastisements()
This function remove chastisements of a student.
By default it remove chastisements for `Фролов Иван`. If you want to change a student, just enter needed students name as `Last name First name`

```shell
remove_chastisements('Голубев Феофан')
```

- create_commendation()
This function creates commendation for a student.
By default it creates commendation for `Фролов Иван` and for subject `Математика`. If you want to change a student or a subject, just enter needed students name as `Last name First name` and needed subject as `Георафия`

```shell
remove_chastisements('Голубев Феофан', 'География')
```
