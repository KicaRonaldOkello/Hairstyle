# Hairstyle



### Sign in
`api/v1/auth/signin_stylist`
`api/v1/auth/signin`

```
{
    "email":"asdfgh",
    "password":"sdfghfd"
}
```
### Sign up
#### stylist
`api/v1/auth/signup_stylist`
#### user
`api/v1/auth/signup`

```
{
    "email":"asdfgh@gmail.com",
    "lastname":"sdfghfd",
    "firstname":"ddff",
    "password":"sdfgds"
}
```

#### Add Hair Style

URL `/api/v1/stylist/hairstyles` 

METHOD `POST`

SAMPLE DATA
```
{
    "hairstyle_name":"kicky",
	"hairstyle_description":"sdfgdsx",
    "price_range":20000,
    "staff_id":1
	
}
```
### Stylist search 
add parameters to query 

`/api/v1/search?location=kikoni&hairstyle_name=kicky&price_range=40000`

METHOD `GET`

PARAMETERS
```
location            str
style               str                 
price_range         int
```
