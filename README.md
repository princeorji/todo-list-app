# todo-list-app
This is a todo-list app that allow users to set reminders on tasks and deadlines.

## Installation for backend
  * Create a virtual enviroment
  
  ```
    py -m venv <enviroment_name>
  ```
  * Activate it
  
  ```
    source <enviroment_name>/scripts/activate
  ```
  * Install the packages in the 'requirements.text' file
  
  ```
    pip install -r requirements.txt
  ```

## API Reference

#### Get a list of all tasks 

```
  http://127.0.0.1:8000/src/todo-list/
```
#### Create a task

```
  http://127.0.0.1:8000/src/create-todo/
```
#### Update a task

```
  http://127.0.0.1:8000/src/update-todo/id/
```
#### Delete a task

```
  http://127.0.0.1:8000/src/delete-todo/id/
```

## Heroku server url

```
  https://guarded-eyrie-62525.herokuapp.com/
```

