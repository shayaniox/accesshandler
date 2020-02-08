## List of url

### LIST /apiv1/urls

### CURL

```bash
curl -X LIST -- "$URL/apiv1/urls?"
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
        "id":1,
        "limit":10,
        "pattern":"\/foo"
    },
    {
        "id":2,
        "limit":20,
        "pattern":"\/bar"
    },
    {
        "id":3,
        "limit":30,
        "pattern":"\/foo\/bar\/*"
    }
]
```

---

## WHEN: Trying to sorting response

### LIST /apiv1/urls

### Query Strings

Name | Example
--- | ---
sort | id

### CURL

```bash
curl -X LIST -- "$URL/apiv1/urls?sort=id"
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
        "id":1,
        "limit":10,
        "pattern":"\/foo"
    },
    {
        "id":2,
        "limit":20,
        "pattern":"\/bar"
    },
    {
        "id":3,
        "limit":30,
        "pattern":"\/foo\/bar\/*"
    }
]
```

---

## WHEN: Sorting the response descending

### LIST /apiv1/urls

### Query Strings

Name | Example
--- | ---
sort | -id

### CURL

```bash
curl -X LIST -- "$URL/apiv1/urls?sort=-id"
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
        "id":3,
        "limit":30,
        "pattern":"\/foo\/bar\/*"
    },
    {
        "id":2,
        "limit":20,
        "pattern":"\/bar"
    },
    {
        "id":1,
        "limit":10,
        "pattern":"\/foo"
    }
]
```

---

## WHEN: Trying pagination response

### LIST /apiv1/urls

### Query Strings

Name | Example
--- | ---
take | 1

### CURL

```bash
curl -X LIST -- "$URL/apiv1/urls?take=1"
```

### Response: 200 OK

#### Headers

* X-Pagination-Take: 1
* X-Pagination-Skip: 0
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "id":1,
        "limit":10,
        "pattern":"\/foo"
    }
]
```

---

## WHEN: Trying pagination with skip

### LIST /apiv1/urls

### Query Strings

Name | Example
--- | ---
take | 1
skip | 1

### CURL

```bash
curl -X LIST -- "$URL/apiv1/urls?take=1&skip=1"
```

### Response: 200 OK

#### Headers

* X-Pagination-Take: 1
* X-Pagination-Skip: 1
* X-Pagination-Count: 3

#### Body

Content-Type: application/json

```json
[
    {
        "id":2,
        "limit":20,
        "pattern":"\/bar"
    }
]
```

---

## WHEN: Trying filtering response

### LIST /apiv1/urls

### Query Strings

Name | Example
--- | ---
pattern | /foo

### CURL

```bash
curl -X LIST -- "$URL/apiv1/urls?pattern=/foo"
```

### Response: 200 OK

#### Headers

* X-Pagination-Take: 100
* X-Pagination-Skip: 0
* X-Pagination-Count: 1

#### Body

Content-Type: application/json

```json
[
    {
        "id":1,
        "limit":10,
        "pattern":"\/foo"
    }
]
```

