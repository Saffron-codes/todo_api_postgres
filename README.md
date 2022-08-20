# REST API with Fastapi and Postgresql

## Create User
```
/register
```
> Pass the following json as body 

```json
{
    "name":"John",
    "email":"john@gmail.com",
    "passoword":"123456"
}
```
- The Password should not exceed 6 char

## Create Todo
```
/notes/create
```
> Pass the following json
```json
{
    "description":"Take Dogs for walk",
    "user_id":1
}
```
- The user_id is returned while creating the user


## Update Todo
```
/notes/update
```
> Pass the following json
```json
{
    "id":2
    "new_description":"Take Dogs for walk",
    "user_id":1
}
```
- The user_id is returned while creating the user
- The id aka note id is returned using get user todos

## Delete Todo
```
/notes/delete?id=1&user_id=2
```
> Pass the above with the parameters correctly

- The user_id is returned while creating the user
- The id aka note id is returned using get user todos

## Get User Todos
```
/notes/&user_id=2&password=123456
```
- returns a list of json 
```json
[
  {
    "id": 3,
    "description": "Take Dogs for walk"
  },
  {
    "id": 5,
    "description": "Buy milk & biscuit"
  }
]
```

