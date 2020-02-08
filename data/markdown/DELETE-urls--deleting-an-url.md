## Deleting an url

### DELETE /apiv1/urls/:id

### Url Parameters

Name | Example
--- | ---
id | 1

### CURL

```bash
curl -X DELETE -- "$URL/apiv1/urls/1?"
```

### Response: 200 OK

#### Body

Content-Type: application/json

```json
{
    "id":1,
    "limit":10,
    "pattern":"\/foo"
}
```

---

## WHEN: Pattern is not found

### DELETE /apiv1/urls/:id

### Url Parameters

Name | Example
--- | ---
id | 0

### CURL

```bash
curl -X DELETE -- "$URL/apiv1/urls/0?"
```

### Response: 404 Not Found

#### Headers

* ContentType: application/json

