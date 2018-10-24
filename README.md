# ClippyBackEnd
This is the backend for clippy


# Current Endpoints:

### `/copydata/`
### `['GET']`

Description:

This endpoint is where most of the clipboard data for diffrent users can be found

**Headers**
<br/>

```json
{
    "Authorization": "Token [token]"
}
```
<br/>


Example Response:
```json
[
    {
        "content": "Clipboardcontent1",
        "date": "date_when_created1",
        "user": 1
    },
    {
        "content": "Clipboardcontent2",
        "date": "date_when_created2",
        "user": 1
    }
]
```
***

### `/copydata/`
### `['POST']`

Description:

This endpoint is how data is submitted to the copydata database

**Headers**
<br/>

```json
{
    "Authorization": "Token [token]"
}
```
<br/>

**Parameters:**<br/>
```json
{
  "content": "[content_to_submit]",
  "date": "[data_content_was_created]"
}
```


Example Response:
```json
[
    {
    "content": "clipboard_content",
    "date": "date",
    "user": 1
    }
]
```
***

### `/copydata/token`
### `['GET']`

Description:

This is how authentication tokens are aquired

**Headers**
<br/>

**None**
<br/>

**Parameters:**<br/>
**None**


Example Response:
```json
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "auth_token": "3db10d6fa452d894cdf57e121e995fb034c56733"
}
```
***

## Todo

- [x] Have a copydata list per user

- [ ] Probably switch from creating a new token to `Token.get_or_create` to create a new token when <br/> the end point is requested

- [x] Figure out why login in with TokenAuthentication is a problem

      // SessionAuthentication must be included in the authentication classes function


- [x] Have tokens generate automatically per new user
