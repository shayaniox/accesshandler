**NOTE:** You can get more detailed from running `pytest` and looking for
`<path/to/accesshandler>/data/markdown` generated document from tests.

---

## Creating an rule

### CREATE /apiv1/rules

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
pattern | true | false | string | example.com/foo/bar
limit | true | false | string | 20/min

### CURL

```bash
curl -X CREATE --data '{"pattern": "example.com/foo/bar", "limit": "20/min"}' -- "$URL/apiv1/rules?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "id":1,
    "isExactUrl":true,
    "limit":"20\/min",
    "pattern":"example.com\/foo\/bar"
}
```

---

## Deleting an rule

### DELETE /apiv1/rules/:id

### Url Parameters

Name | Example
--- | ---
id | 1

### CURL

```bash
curl -X DELETE -- "$URL/apiv1/rules/1?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "limit":"10",
    "isExactUrl":false,
    "pattern":"\/foo",
    "id":1
}
```

---

## List of rule

### LIST /apiv1/rules

### CURL

```bash
curl -X LIST -- "$URL/apiv1/rules?"
```

### Response: 200 OK

#### Headers

* X-Pagination-Take: 100
* X-Pagination-Skip: 0
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "limit":"10",
        "isExactUrl":false,
        "pattern":"\/foo",
        "id":1
    },
    {
        "limit":"20",
        "isExactUrl":false,
        "pattern":"\/bar",
        "id":2
    },
    {
        "limit":"30",
        "isExactUrl":false,
        "pattern":"\/foo\/bar\/*",
        "id":3
    }
]
```

---
## Updating an rule

### UPDATE /apiv1/rules/:id

### Url Parameters

Name | Example
--- | ---
id | 1

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
pattern | true | ? | string | /foo/\d
limit | true | ? | string | 100/sec

### CURL

```bash
curl -X UPDATE --data '{"pattern": "/foo/\\d", "limit": "100/sec"}' -- "$URL/apiv1/rules/1?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "limit":"100\/sec",
    "isExactUrl":false,
    "pattern":"\/foo\/\\d",
    "id":1
}
```

---

## Post a log to check if passed the limit or not

### POST /apiv1/logs

### Form

Name | Required | Nullable | Type | Example
--- | --- | --- | --- | ---
url | true | ? | string | /foo/bar
IP | true | ? | string | 1.1.1.1

### CURL

```bash
curl -X POST --data '{"url": "/foo/bar", "IP": "1.1.1.1"}' -- "$URL/apiv1/logs?"
```

### Response: 200 OK

---

## Retrieving application's version

### GET /apiv1/version

### CURL

```bash
curl -- "$URL/apiv1/version?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "version":"0.1.0"
}
```
