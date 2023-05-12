---
title: System Surveyor API v2.0.0
language_tabs:
  - shell: cURL
  - python: Python
  - ruby: Ruby
  - go: Go
  - http: HTTP
  - javascript: JavaScript
  - javascript--nodejs: Node.JS
language_clients:
  - shell: ""
  - python: ""
  - ruby: ""
  - go: ""
  - http: ""
  - javascript: ""
  - javascript--nodejs: ""
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="system-surveyor-api">System Surveyor API v2.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# How to Use Our REST APIs

            System Surveyor's APIs enable bi-directional communication with it's platform.             These APIs provide a software layer connecting and optimizing the network to allow your users to             create / edit / retrieve sites & surveys, along with all of the associated data.

## Domain Name

            The domain name for our API is https://openapi.systemsurveyor.com.             This needs to be prefixed to all requests.

## Prerequisites

            In order to utilize these APIs, you must have an Enterprise account, with a valid             plan. Your account administrator must create an `access_token` for you, which is required for each request.

# Authentication

- HTTP Authentication, scheme: bearer 

Once the account administrator creates your API `access_token`         ([link](https://app.systemsurveyor.com/v2/account/#api_management)), you must include that with each request.         These tokens are valid for 1 year, and can be revoked at any time by the account administrator.         You will find examples for each request with each endpoint below.

<h1 id="system-surveyor-api-folders">Folders</h1>

## Creates a new site/survey folder or updates an existing one if found.

<a id="opIdcreate_or_update_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /v3/folder/{folder_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.put('/v3/folder/{folder_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.put '/v3/folder/{folder_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/v3/folder/{folder_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PUT /v3/folder/{folder_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "string",
  "site_external_id": "string",
  "team_id": 0,
  "label": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/folder/{folder_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "name": "string",
  "site_external_id": "string",
  "team_id": 0,
  "label": "string"
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/folder/{folder_id}',
{
  method: 'PUT',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PUT /v3/folder/{folder_id}`

To create/update a site folder, pass a value for `team_id` field in the request payload, to create/update a survey folder
pass a value for `site_id` field.

> Body parameter

```json
{
  "name": "string",
  "site_external_id": "string",
  "team_id": 0,
  "label": "string"
}
```

<h3 id="creates-a-new-site/survey-folder-or-updates-an-existing-one-if-found.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|
|body|body|[FolderSchema](#schemafolderschema)|true|none|
|» name|body|string|true|none|
|» site_id|body|integer|false|none|
|» site_external_id|body|string|false|none|
|» id|body|string|false|none|
|» team_id|body|integer|false|none|
|» label|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "name": "string",
  "site_id": 0,
  "id": "string",
  "team_id": 0,
  "label": "string"
}
```

<h3 id="creates-a-new-site/survey-folder-or-updates-an-existing-one-if-found.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Folder updated|[FolderSchema](#schemafolderschema)|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Folder created|[FolderSchema](#schemafolderschema)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Soft deletes a site folder or a survey folder.

<a id="opIddelete_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/folder/{folder_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/folder/{folder_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/folder/{folder_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/v3/folder/{folder_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/folder/{folder_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/folder/{folder_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/folder/{folder_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /v3/folder/{folder_id}`

Folder must be empty in order to be deleted.

Only account admins, team admins, and team members can delete folders. Only team members with write access can delete survey
folders.

<h3 id="soft-deletes-a-site-folder-or-a-survey-folder.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|

<h3 id="soft-deletes-a-site-folder-or-a-survey-folder.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Creates a new folder that can hold sites

<a id="opIdcreate_site_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/site_folder \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v3/site_folder', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/v3/site_folder',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/v3/site_folder", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /v3/site_folder HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "My Folder",
  "label": "S0124",
  "team_id": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_folder',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "name": "My Folder",
  "label": "S0124",
  "team_id": 0
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_folder',
{
  method: 'POST',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /v3/site_folder`

> Body parameter

```json
{
  "name": "My Folder",
  "label": "S0124",
  "team_id": 0
}
```

<h3 id="creates-a-new-folder-that-can-hold-sites-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» name|body|string|false|Folder name. Does not need to be unique|
|» label|body|string|false|none|
|» team_id|body|integer|false|none|

> Example responses

> 201 Response

```json
{
  "name": "string",
  "site_id": 0,
  "id": "string",
  "team_id": 0,
  "label": "string"
}
```

<h3 id="creates-a-new-folder-that-can-hold-sites-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|OK|[FolderSchema](#schemafolderschema)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Update all fields of a folder

<a id="opIdupdate_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/site_folder/{folder_external_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.patch('/v3/site_folder/{folder_external_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.patch '/v3/site_folder/{folder_external_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/v3/site_folder/{folder_external_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PATCH /v3/site_folder/{folder_external_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "My Folder",
  "label": "ER-1233"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_folder/{folder_external_id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "name": "My Folder",
  "label": "ER-1233"
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_folder/{folder_external_id}',
{
  method: 'PATCH',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PATCH /v3/site_folder/{folder_external_id}`

> Body parameter

```json
{
  "name": "My Folder",
  "label": "ER-1233"
}
```

<h3 id="update-all-fields-of-a-folder-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|Folder ID|
|body|body|object|true|none|
|» name|body|string|false|Folder name. Does not need to be unique|
|» label|body|string|false|none|

> Example responses

> 201 Response

```json
{
  "name": "string",
  "site_id": 0,
  "id": "string",
  "team_id": 0,
  "label": "string"
}
```

<h3 id="update-all-fields-of-a-folder-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|OK|[FolderSchema](#schemafolderschema)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Allows creating folders inside a site, which can store and organize surveys

<a id="opIdcreate_survey_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/{site_id}/folder \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v3/{site_id}/folder', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/v3/{site_id}/folder',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/v3/{site_id}/folder", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /v3/{site_id}/folder HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "My Folder",
  "label": "LS1-34"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/{site_id}/folder',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "name": "My Folder",
  "label": "LS1-34"
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/{site_id}/folder',
{
  method: 'POST',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /v3/{site_id}/folder`

> Body parameter

```json
{
  "name": "My Folder",
  "label": "LS1-34"
}
```

<h3 id="allows-creating-folders-inside-a-site,-which-can-store-and-organize-surveys-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site external ID|
|body|body|object|true|none|
|» name|body|string|false|Folder name. Does not need to be unique|
|» label|body|string|false|Folder label|

> Example responses

> 201 Response

```json
{
  "name": "string",
  "site_id": 0,
  "id": "string",
  "team_id": 0,
  "label": "string"
}
```

<h3 id="allows-creating-folders-inside-a-site,-which-can-store-and-organize-surveys-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|OK|[FolderSchema](#schemafolderschema)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Deletes a survey folder in a site.

<a id="opIddelete_survey_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/survey_folder/{folder_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/survey_folder/{folder_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/survey_folder/{folder_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/v3/survey_folder/{folder_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/survey_folder/{folder_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey_folder/{folder_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey_folder/{folder_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /v3/survey_folder/{folder_id}`

Folders that already contain surveys are not allowed to be deleted.

Only team members with write access can delete survey folders.

<h3 id="deletes-a-survey-folder-in-a-site.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|

<h3 id="deletes-a-survey-folder-in-a-site.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Soft deletes a folder that can contain sites.

<a id="opIddelete_site_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/site_folder/{folder_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/site_folder/{folder_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/site_folder/{folder_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/v3/site_folder/{folder_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/site_folder/{folder_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_folder/{folder_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_folder/{folder_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /v3/site_folder/{folder_id}`

Folder must be empty in order to be deleted. Only account admins, team admins, and team members can delete folders.

<h3 id="soft-deletes-a-folder-that-can-contain-sites.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|

<h3 id="soft-deletes-a-folder-that-can-contain-sites.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-reports">Reports</h1>

## Queues a message for creating reports for sites or surveys

<a id="opIdcreate_report"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/report \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v3/report', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/v3/report',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/v3/report", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /v3/report HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "site_id": "string",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "paper_size": "string",
  "is_site_report": false,
  "name": "string",
  "options": [
    {
      "value": true,
      "template_name": "string",
      "scope": "template",
      "inputs": [
        {
          "value": "string",
          "field_id": "string"
        }
      ],
      "id": "string"
    }
  ],
  "is_excel": false,
  "output": "pdf",
  "filters": [
    {}
  ],
  "custom_data": {},
  "survey_ids": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/report',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "site_id": "string",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "paper_size": "string",
  "is_site_report": false,
  "name": "string",
  "options": [
    {
      "value": true,
      "template_name": "string",
      "scope": "template",
      "inputs": [
        {
          "value": "string",
          "field_id": "string"
        }
      ],
      "id": "string"
    }
  ],
  "is_excel": false,
  "output": "pdf",
  "filters": [
    {}
  ],
  "custom_data": {},
  "survey_ids": [
    "string"
  ]
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/report',
{
  method: 'POST',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /v3/report`

Reports are created by an external PHP service by picking up messages from the queue.

> Body parameter

```json
{
  "site_id": "string",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "paper_size": "string",
  "is_site_report": false,
  "name": "string",
  "options": [
    {
      "value": true,
      "template_name": "string",
      "scope": "template",
      "inputs": [
        {
          "value": "string",
          "field_id": "string"
        }
      ],
      "id": "string"
    }
  ],
  "is_excel": false,
  "output": "pdf",
  "filters": [
    {}
  ],
  "custom_data": {},
  "survey_ids": [
    "string"
  ]
}
```

<h3 id="queues-a-message-for-creating-reports-for-sites-or-surveys-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SurveyReportRequestSchema](#schemasurveyreportrequestschema)|true|none|
|» site_id|body|string|true|none|
|» report_id|body|string(uuid)|true|none|
|» paper_size|body|string|false|none|
|» is_site_report|body|boolean|false|none|
|» name|body|string|true|none|
|» options|body|[[SurveyOptions](#schemasurveyoptions)]|false|none|
|»» value|body|boolean|true|none|
|»» template_name|body|string|false|none|
|»» scope|body|string|true|none|
|»» inputs|body|[[SurveyFields](#schemasurveyfields)]|false|none|
|»»» value|body|string|true|none|
|»»» field_id|body|string|true|none|
|»» id|body|string|true|none|
|» is_excel|body|boolean|false|none|
|» output|body|string|true|none|
|» filters|body|[object]|false|none|
|» custom_data|body|object|false|none|
|» survey_ids|body|[string]|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» scope|template|
|»» scope|model|
|»» scope|content|
|» output|pdf|
|» output|html|
|» output|xls|

> Example responses

> 202 Response

```json
{
  "report_id": 2545
}
```

<h3 id="queues-a-message-for-creating-reports-for-sites-or-surveys-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Report scheduled successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<h3 id="queues-a-message-for-creating-reports-for-sites-or-surveys-responseschema">Response Schema</h3>

Status Code **202**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» report_id|integer|false|none|Unique ID of the scheduled report|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-sites">Sites</h1>

## Get site information

<a id="opIdget_site"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/site/{site_id} \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/site/{site_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v3/site/{site_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/site/{site_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /v3/site/{site_id}`

<h3 id="get-site-information-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "46787da3-1e6e-4d9b-a858-ac9e12dc3efb",
  "team_id": 1992,
  "name": "John's site",
  "label": "BATS",
  "survey_count": 0,
  "city": "Los Angeles",
  "state": "California",
  "street": "1300 S SAN PEDRO ST",
  "zip_code": 38129,
  "is_active": true,
  "version": 1674845520,
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "creator": {
    "user_id": 9313,
    "first_name": "John",
    "last_name": "Smith"
  },
  "modifier": {
    "user_id": 9313,
    "first_name": "John",
    "last_name": "Smith"
  },
  "created_at": 1452384000,
  "modified_at": 1673557029
}
```

<h3 id="get-site-information-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<h3 id="get-site-information-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|false|none|ID for the site|
|» team_id|integer|false|none|ID of the team associated with the site.|
|» name|string|false|none|Name of the Site|
|» label|string|false|none|Label attached to the site|
|» survey_count|integer|false|none|none|
|» city|string|false|none|City that the site is in|
|» state|string|false|none|State that the Site is in|
|» street|string|false|none|Street address of the site|
|» zip_code|string|false|none|Zip code of where the website is|
|» is_active|boolean|false|none|none|
|» version|integer|false|none|none|
|» reference_id|string|false|none|none|
|» tags|[string]|false|none|none|
|» creator|object|false|none|Information about the creator of the Site.|
|»» user_id|integer|false|none|ID of the user who created the site.|
|»» first_name|string|false|none|First name of the user who created the site.|
|»» last_name|string|false|none|Last name of the user who created the site.|
|» modifier|object|false|none|Information about the latest user to modify the Site.|
|»» user_id|integer|false|none|ID of the user who last modified the site.|
|»» first_name|string|false|none|First name of the user who last modified the site.|
|»» last_name|string|false|none|Last name of the user who last modified the site.|
|» created_at|integer|false|none|Unix timestamp of when the site was created.|
|» modified_at|integer|false|none|Unix time stamp for when the site was last modified.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Creates a new site with a specific `site_id` or updates the site if it already exists

<a id="opIdcreate_or_update_site"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /v3/site/{site_id} \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.put('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.put '/v3/site/{site_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/v3/site/{site_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PUT /v3/site/{site_id} HTTP/1.1

Content-Type: application/json

```

```javascript
const inputBody = '{
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "label": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "label": "string"
};
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'PUT',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PUT /v3/site/{site_id}`

To create a site, pass a new UUID for the `site_id`.
To update a site, pass the existing UUID for the `site_id`.
You may pass a `folder_external_id` field in the payload to create the site inside that folder.

> Body parameter

```json
{
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "label": "string"
}
```

<h3 id="creates-a-new-site-with-a-specific-`site_id`-or-updates-the-site-if-it-already-exists-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|body|body|[SiteSchema](#schemasiteschema)|true|none|
|» legacy_site_id|body|integer|false|none|
|» creator|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» reference_id|body|string|false|none|
|» street|body|string|false|none|
|» team_id|body|integer|true|none|
|» name|body|string|true|none|
|» site_id|body|string|false|none|
|» created_at|body|null|false|none|
|» modifier|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» modified_at|body|null|false|none|
|» state|body|string|false|none|
|» zip_code|body|string|false|none|
|» is_archived|body|any|false|none|
|» tags|body|[string]|false|none|
|» city|body|string|false|none|
|» version|body|integer|false|none|
|» label|body|string|false|none|

<h3 id="creates-a-new-site-with-a-specific-`site_id`-or-updates-the-site-if-it-already-exists-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful update|None|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful create|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Update specific fields of a site

<a id="opIdpatch_site"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/site/{site_id} \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.patch('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.patch '/v3/site/{site_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/v3/site/{site_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PATCH /v3/site/{site_id} HTTP/1.1

Content-Type: application/json

```

```javascript
const inputBody = '{
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "label": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "label": "string"
};
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'PATCH',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PATCH /v3/site/{site_id}`

> Body parameter

```json
{
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "label": "string"
}
```

<h3 id="update-specific-fields-of-a-site-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|body|body|[SiteSchema](#schemasiteschema)|true|none|
|» legacy_site_id|body|integer|false|none|
|» creator|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» reference_id|body|string|false|none|
|» street|body|string|false|none|
|» team_id|body|integer|true|none|
|» name|body|string|true|none|
|» site_id|body|string|false|none|
|» created_at|body|null|false|none|
|» modifier|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» modified_at|body|null|false|none|
|» state|body|string|false|none|
|» zip_code|body|string|false|none|
|» is_archived|body|any|false|none|
|» tags|body|[string]|false|none|
|» city|body|string|false|none|
|» version|body|integer|false|none|
|» label|body|string|false|none|

<h3 id="update-specific-fields-of-a-site-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful update|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Hard deletes a site and all related objects.

<a id="opIddelete_site"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/site/{site_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/site/{site_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/v3/site/{site_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/site/{site_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /v3/site/{site_id}`

<h3 id="hard-deletes-a-site-and-all-related-objects.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|

<h3 id="hard-deletes-a-site-and-all-related-objects.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Returns all archived/unarchived sites and folders across all teams of a user.

<a id="opIdget_user_sites_and_folders"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/sites \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/sites', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/sites',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v3/sites", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/sites HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/sites',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/sites',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /v3/sites`

Explanation of usage of filters:

Filtered by favorites:
  - All sites that are in workbench but not in a folder
  - All folders that have a site under them that is in the workbench
  - Don't return sites that are in workbench but also in a folder

Filtered by folder and favorites:
  - All sites in the folder that are in the workbench

Filtered by folder:
  - All sites in folder

<h3 id="returns-all-archived/unarchived-sites-and-folders-across-all-teams-of-a-user.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page[number]|query|integer|false|Page to retrieve from the entire result set|
|page[size]|query|integer|false|Max amount of objects to return per page in the response|
|filter[modified_after]|query|integer|false|Return only sites that have been created, modified, or favorited (added to workbench) after an specific datetime (in UTC Epoch format).|
|filter[deleted_after]|query|integer|false|Return only sites that were deleted after an specified timestamp. Limited site data is returned using this filter.|
|filter[favorites_only]|query|integer|false|Filters results to only include sites the user has added to their workbench|
|filter[folder_id]|query|string|false|Returns only sites that belong to a specific folder|

> Example responses

> 200 Response

```json
{
  "sites": [
    {
      "id": "46787da3-1e6e-4d9b-a858-ac9e12dc3efb",
      "name": "Union Square",
      "survey_count": 12,
      "type": "site",
      "version": 45479945,
      "favorite_timestamp": 12034903409,
      "has_favorite_sites": true,
      "permissions": {
        "is_site_guest": true,
        "user_can_edit_site": true,
        "user_can_change_site_access": true,
        "user_can_invite_guests": true,
        "user_can_delete_surveys": true,
        "user_can_create_surveys": true,
        "user_can_modify_surveys": true,
        "user_can_revoke_survey_edit": true,
        "user_can_edit_contacts": true,
        "user_can_view_site_access": true
      },
      "owner": {
        "user_id": 12390,
        "first_name": "John",
        "last_name": "Doe"
      },
      "modified_at": 1644374426,
      "modifier": "string",
      "team": {
        "team_id": 1049,
        "name": "string"
      }
    }
  ]
}
```

<h3 id="returns-all-archived/unarchived-sites-and-folders-across-all-teams-of-a-user.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<h3 id="returns-all-archived/unarchived-sites-and-folders-across-all-teams-of-a-user.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» sites|[object]|false|none|Result list of sites or folders|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» survey_count|integer|false|none|none|
|»» type|string|false|none|If the result item is a site or a folder|
|»» version|integer|false|none|none|
|»» favorite_timestamp|integer|false|none|Unix Timestamp of when the site was added to favorites|
|»» has_favorite_sites|boolean|false|none|Indicates if a folder has sites that are in the user's workbench|
|»» permissions|object|false|none|none|
|»»» is_site_guest|boolean|false|none|none|
|»»» user_can_edit_site|boolean|false|none|none|
|»»» user_can_change_site_access|boolean|false|none|none|
|»»» user_can_invite_guests|boolean|false|none|none|
|»»» user_can_delete_surveys|boolean|false|none|none|
|»»» user_can_create_surveys|boolean|false|none|none|
|»»» user_can_modify_surveys|boolean|false|none|none|
|»»» user_can_revoke_survey_edit|boolean|false|none|none|
|»»» user_can_edit_contacts|boolean|false|none|none|
|»»» user_can_view_site_access|boolean|false|none|none|
|»» owner|object|false|none|none|
|»»» user_id|integer|false|none|none|
|»»» first_name|string|false|none|none|
|»»» last_name|string|false|none|none|
|»» modified_at|integer|false|none|Unix Timestamp of the most recently modified survey in the site. If the site has no surveys, falls back to the<br>site's own `modified_at` datetime.|
|»» modifier|string|false|none|User who modified the site or folder|
|»» team|object|false|none|none|
|»»» team_id|integer|false|none|none|
|»»» name|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|site|
|type|folder|
|is_site_guest|true|
|is_site_guest|false|
|user_can_edit_site|true|
|user_can_edit_site|false|
|user_can_change_site_access|true|
|user_can_change_site_access|false|
|user_can_invite_guests|true|
|user_can_invite_guests|false|
|user_can_delete_surveys|true|
|user_can_delete_surveys|false|
|user_can_create_surveys|true|
|user_can_create_surveys|false|
|user_can_modify_surveys|true|
|user_can_modify_surveys|false|
|user_can_revoke_survey_edit|true|
|user_can_revoke_survey_edit|false|
|user_can_edit_contacts|true|
|user_can_edit_contacts|false|
|user_can_view_site_access|true|
|user_can_view_site_access|false|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Allows for batch deleting of sites (and all related data).

<a id="opIddelete_sites"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/sites \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/sites', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/sites',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/v3/sites", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/sites HTTP/1.1

Content-Type: application/json

```

```javascript
const inputBody = '[
  "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb"
]';
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/sites',
{
  method: 'DELETE',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = [
  "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb"
];
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/sites',
{
  method: 'DELETE',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /v3/sites`

Users must be team members and have write access on all sites to be deleted, otherwise the entire operation will fail.
Guest users are not allowed to batch delete sites.

> Body parameter

```json
[
  "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb"
]
```

<h3 id="allows-for-batch-deleting-of-sites-(and-all-related-data).-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|

<h3 id="allows-for-batch-deleting-of-sites-(and-all-related-data).-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-surveys">Surveys</h1>

## Returns all surveys and folders for a specific site. These are shown in the site overview page.

<a id="opIdget_site_surveys_and_folders"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/site/{site_id}/surveys \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/site/{site_id}/surveys', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/site/{site_id}/surveys',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v3/site/{site_id}/surveys", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/site/{site_id}/surveys HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}/surveys',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}/surveys',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /v3/site/{site_id}/surveys`

Surveys that belong to folders will not be included in the response, unless
a search is being made.

Results are ordered by `title` ascending by default if no sorting is specified.

Query Parameters:

- q: Search surveys and folders.

- filter[status]: Return only surveys in a specific status (`archived` or `open`). Folders will also be returned in the response.
- filter[external_folder_id]: Filter surveys by folder using string of external_id (UUID). Only surveys will be returned.
- filter[modified_after]: Return surveys and folders that have been created or modified after a timestamp (in UTC Epoch format).
- filter[deleted_after]: Return surveys and folders that have been deleted after the specified timestamp.

- page[number]: Page to retrieve from the entire result set.
- page[size]: Max amount of objects to return per page in the response. Defaults to 100.

- sort: Sort by fields (comma separated). Use `-` prefix on field name to sort descending.

<h3 id="returns-all-surveys-and-folders-for-a-specific-site.-these-are-shown-in-the-site-overview-page.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|filter[status]|query|string|false|Return only surveys in a specific status (`archived` or `open`).|
|filter[external_folder_id]|query|string|false|Filter surveys by folder using string of external_id (UUID)|
|filter[modified_after]|query|number|false|Return only surveys and folders that have been created or modified after a timestamp (in UTC Epoch format).|
|filter[deleted_after]|query|number|false|Return surveys and folders that have been deleted after the specified timestamp.|
|sort|query|string|false|Sort by column names (comma separated). Use `-` prefix on column name to sort descending|
|q|query|string|false|Apply search to query|
|page[number]|query|integer|false|Page to retrieve from the entire result set|
|page[size]|query|integer|false|Max amount of objects to return per page in the response|

#### Enumerated Values

|Parameter|Value|
|---|---|
|filter[status]|archived|
|filter[status]|open|
|sort|id|
|sort|title|
|sort|document_image_url|
|sort|preview_image|
|sort|editor_id|
|sort|editor_first_name|
|sort|editor_last_name|
|sort|label|
|sort|element_count|
|sort|is_folder|
|sort|is_archived|
|sort|created_at|
|sort|modified_at|
|sort|status|
|sort|survey_count|

> Example responses

> 200 Response

```json
{
  "surveys": [
    {
      "id": "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb",
      "title": "New Folder Name",
      "label": "TGS-123",
      "is_folder": true,
      "preview_image": "https://app.systemsurveyor.com/media/2023/01/28/d9a8cf3a-728e-4eae-b290-1f2d1bc35a0e.png",
      "element_count": 90,
      "survey_count": 2,
      "is_archived": false,
      "modified_at": 1674952923,
      "created_at": 1674952923,
      "editor": {
        "user_id": 9313,
        "first_name": "John",
        "last_name": "Doe"
      }
    }
  ]
}
```

<h3 id="returns-all-surveys-and-folders-for-a-specific-site.-these-are-shown-in-the-site-overview-page.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<h3 id="returns-all-surveys-and-folders-for-a-specific-site.-these-are-shown-in-the-site-overview-page.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» surveys|[object]|false|none|none|
|»» id|string|false|none|Survey or folder id|
|»» title|string|false|none|Title given to the folder at the time of creation.|
|»» label|string|false|none|Label attached to this folder|
|»» is_folder|boolean|false|none|Is this object a folder or a survey|
|»» preview_image|string|false|none|URL to the folder's preview image|
|»» element_count|integer|false|none|Count of elements in this folder|
|»» survey_count|integer|false|none|Count for the survey|
|»» is_archived|boolean|false|none|If the folder is archived or not|
|»» modified_at|integer|false|none|Unix timestamp of when the survey was last modified|
|»» created_at|integer|false|none|Unix timestamp of when this folder was created.|
|»» editor|object|false|none|none|
|»»» user_id|integer|false|none|ID of the user who last edited this object.|
|»»» first_name|string|false|none|First Name of the person who edited this folder|
|»»» last_name|string|false|none|Last Name of the person who last edited this folder|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Allows creating a new survey with a unique identifier generated by the client, or updates the existing survey with that identifier if it exists.

<a id="opIdcreate_or_update_survey"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /v3/site/{site_id}/survey/{survey_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.put('/v3/site/{site_id}/survey/{survey_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.put '/v3/site/{site_id}/survey/{survey_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/v3/site/{site_id}/survey/{survey_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PUT /v3/site/{site_id}/survey/{survey_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "label": "string",
  "reference_id": "string",
  "description": "string",
  "summary": "string",
  "location": "string",
  "status": null,
  "icon_size": 0,
  "unit": null,
  "margin_range": 0,
  "floorplan_scale": 0,
  "elements": [
    {
      "id": "string",
      "name": "string",
      "element_id": 0,
      "element_index": 0,
      "element_profile_id": 0,
      "systemtype_id": 0,
      "variant": null,
      "z_order": 0,
      "position": null,
      "attributes": [
        {
          "value": "string",
          "name": "string",
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "description": "string",
          "model": "string",
          "price": null,
          "labor_hours": 0,
          "row_index": 0,
          "quantity": null,
          "manufacturer": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "a_side": null,
          "z_side": null,
          "id": "string",
          "type": "string"
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "id": "string",
          "entry": "string",
          "date": null
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "size": "string",
      "stroke_width": "string",
      "text": "string",
      "end_point": null,
      "opacity": 1,
      "stroke_color": "string",
      "location": null,
      "category": null,
      "font_size": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}/survey/{survey_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "title": "string",
  "label": "string",
  "reference_id": "string",
  "description": "string",
  "summary": "string",
  "location": "string",
  "status": null,
  "icon_size": 0,
  "unit": null,
  "margin_range": 0,
  "floorplan_scale": 0,
  "elements": [
    {
      "id": "string",
      "name": "string",
      "element_id": 0,
      "element_index": 0,
      "element_profile_id": 0,
      "systemtype_id": 0,
      "variant": null,
      "z_order": 0,
      "position": null,
      "attributes": [
        {
          "value": "string",
          "name": "string",
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "description": "string",
          "model": "string",
          "price": null,
          "labor_hours": 0,
          "row_index": 0,
          "quantity": null,
          "manufacturer": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "a_side": null,
          "z_side": null,
          "id": "string",
          "type": "string"
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "id": "string",
          "entry": "string",
          "date": null
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "size": "string",
      "stroke_width": "string",
      "text": "string",
      "end_point": null,
      "opacity": 1,
      "stroke_color": "string",
      "location": null,
      "category": null,
      "font_size": "string"
    }
  ]
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site/{site_id}/survey/{survey_id}',
{
  method: 'PUT',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PUT /v3/site/{site_id}/survey/{survey_id}`

Also allows creating/updating surveys with elements, comments, and annotations.

> Body parameter

```json
{
  "title": "string",
  "label": "string",
  "reference_id": "string",
  "description": "string",
  "summary": "string",
  "location": "string",
  "status": null,
  "icon_size": 0,
  "unit": null,
  "margin_range": 0,
  "floorplan_scale": 0,
  "elements": [
    {
      "id": "string",
      "name": "string",
      "element_id": 0,
      "element_index": 0,
      "element_profile_id": 0,
      "systemtype_id": 0,
      "variant": null,
      "z_order": 0,
      "position": null,
      "attributes": [
        {
          "value": "string",
          "name": "string",
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "description": "string",
          "model": "string",
          "price": null,
          "labor_hours": 0,
          "row_index": 0,
          "quantity": null,
          "manufacturer": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "a_side": null,
          "z_side": null,
          "id": "string",
          "type": "string"
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "id": "string",
          "entry": "string",
          "date": null
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "size": "string",
      "stroke_width": "string",
      "text": "string",
      "end_point": null,
      "opacity": 1,
      "stroke_color": "string",
      "location": null,
      "category": null,
      "font_size": "string"
    }
  ]
}
```

<h3 id="allows-creating-a-new-survey-with-a-unique-identifier-generated-by-the-client,-or-updates-the-existing-survey-with-that-identifier-if-it-exists.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site external ID|
|survey_id|path|string|true|Survey external ID|
|body|body|[SurveySchema](#schemasurveyschema)|true|none|
|» id|body|string|false|none|
|» title|body|string|true|none|
|» label|body|string|false|none|
|» reference_id|body|string|false|none|
|» description|body|string|false|none|
|» summary|body|string|false|none|
|» location|body|string|false|none|
|» status|body|any|false|none|
|» site|body|any|false|none|
|» icon_size|body|integer|true|none|
|» is_archived|body|boolean|false|none|
|» unit|body|any|true|none|
|» version|body|integer|false|none|
|» margin_range|body|number|true|none|
|» type|body|any|false|none|
|» floorplan_scale|body|number|false|none|
|» preview_image|body|string|false|none|
|» floorplan_url|body|string|false|none|
|» sync_status|body|any|false|none|
|» creator|body|integer|false|none|
|» editor|body|[RelatedUser](#schemarelateduser)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|any|false|none|
|» modifier|body|integer|false|none|
|» created_at|body|any|false|none|
|» modified_at|body|any|false|none|
|» elements|body|[[SurveyElement](#schemasurveyelement)]|false|none|
|»» id|body|string|true|none|
|»» name|body|string|true|none|
|»» element_id|body|integer|true|none|
|»» element_index|body|integer|false|none|
|»» element_profile_id|body|integer|false|none|
|»» systemtype_id|body|integer|true|none|
|»» variant|body|any|false|none|
|»» z_order|body|integer|false|none|
|»» position|body|any|true|none|
|»» photo_urls|body|[string]|false|none|
|»» pdf_urls|body|any|false|none|
|»» sync_status|body|any|false|none|
|»» attributes|body|[[SurveyAttribute](#schemasurveyattribute)]|false|none|
|»»» value|body|string|true|none|
|»»» name|body|string|true|none|
|»»» id|body|integer|false|none|
|»»» attribute_id|body|integer|true|none|
|»» accessories|body|[[SurveyElementAccessory](#schemasurveyelementaccessory)]|false|none|
|»»» description|body|string|false|none|
|»»» model|body|string|true|none|
|»»» price|body|any|false|none|
|»»» labor_hours|body|number|false|none|
|»»» id|body|string|false|none|
|»»» row_index|body|integer|true|none|
|»»» quantity|body|any|false|none|
|»»» manufacturer|body|string|true|none|
|»» children|body|[[SurveyElement](#schemasurveyelement)]|false|none|
|»» cables|body|[[CablePath](#schemacablepath)]|false|none|
|»»» a_side|body|any|true|none|
|»»» z_side|body|any|true|none|
|»»» id|body|string|true|none|
|»»» type|body|string|false|none|
|»» connections|body|[PathConnection](#schemapathconnection)|false|none|
|»»» start|body|any|false|none|
|»»» end|body|any|false|none|
|»» activity_log|body|[[SurveyElementActivityLog](#schemasurveyelementactivitylog)]|false|none|
|»»» creator|body|integer|false|none|
|»»» id|body|string|false|none|
|»»» modifier|body|integer|false|none|
|»»» entry|body|string|false|none|
|»»» created_at|body|any|false|none|
|»»» modified_at|body|any|false|none|
|»»» date|body|any|false|none|
|» annotations|body|[[SurveyAnnotation](#schemasurveyannotation)]|false|none|
|»» start_point|body|any|false|none|
|»» fill|body|any|false|none|
|»» size|body|string|false|none|
|»» stroke_width|body|string|true|none|
|»» text|body|string|false|none|
|»» end_point|body|any|false|none|
|»» coordinates|body|any|false|none|
|»» opacity|body|number|false|none|
|»» stroke_color|body|string|true|none|
|»» location|body|any|true|none|
|»» category|body|any|true|none|
|»» id|body|string|false|none|
|»» font_size|body|string|false|none|
|» users|body|any|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» sync_status|synced|
|» sync_status|pending|
|» sync_status|errored|
|»» sync_status|synced|
|»» sync_status|pending|
|»» sync_status|errored|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "title": "string",
  "label": "string",
  "reference_id": "string",
  "description": "string",
  "summary": "string",
  "location": "string",
  "site": null,
  "icon_size": 0,
  "is_archived": true,
  "unit": null,
  "version": 0,
  "margin_range": 0,
  "type": null,
  "floorplan_scale": 0,
  "preview_image": "string",
  "floorplan_url": "string",
  "sync_status": "synced",
  "creator": 0,
  "editor": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "modifier": 0,
  "created_at": null,
  "modified_at": null,
  "elements": [
    {
      "id": "string",
      "name": "string",
      "element_id": 0,
      "element_index": 0,
      "element_profile_id": 0,
      "systemtype_id": 0,
      "variant": null,
      "z_order": 0,
      "position": null,
      "photo_urls": [
        "string"
      ],
      "pdf_urls": null,
      "sync_status": "synced",
      "attributes": [
        {
          "value": "string",
          "name": "string",
          "id": 0,
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "description": "string",
          "model": "string",
          "price": null,
          "labor_hours": 0,
          "id": "string",
          "row_index": 0,
          "quantity": null,
          "manufacturer": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "a_side": null,
          "z_side": null,
          "id": "string",
          "type": "string"
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "creator": 0,
          "id": "string",
          "modifier": 0,
          "entry": "string",
          "created_at": null,
          "modified_at": null,
          "date": null
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "fill": null,
      "size": "string",
      "stroke_width": "string",
      "text": "string",
      "end_point": null,
      "coordinates": null,
      "opacity": 1,
      "stroke_color": "string",
      "location": null,
      "category": null,
      "id": "string",
      "font_size": "string"
    }
  ],
  "users": null
}
```

<h3 id="allows-creating-a-new-survey-with-a-unique-identifier-generated-by-the-client,-or-updates-the-existing-survey-with-that-identifier-if-it-exists.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Survey updated successfully|[SurveySchema](#schemasurveyschema)|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Survey created successfully|[SurveySchema](#schemasurveyschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Deletes a survey and all its related objects

<a id="opIddelete_survey"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/survey/{survey_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/survey/{survey_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/survey/{survey_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/v3/survey/{survey_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/survey/{survey_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`DELETE /v3/survey/{survey_id}`

Also expires any shares of the survey.

<h3 id="deletes-a-survey-and-all-its-related-objects-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|string|true|Survey ID|

<h3 id="deletes-a-survey-and-all-its-related-objects-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-teams">Teams</h1>

## Returns all the teams the current user is a member of

<a id="opIdget_user_teams"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/teams \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/teams', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/teams',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v3/teams", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/teams HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/teams',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/teams',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /v3/teams`

Returns the information related to a user. This endpoint returns which teams a user is a part of, plan
subscriptions, features access for the user as well as who owns the Team as the lead.

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "type": null
    }
  ]
}
```

<h3 id="returns-all-the-teams-the-current-user-is-a-member-of-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<h3 id="returns-all-the-teams-the-current-user-is-a-member-of-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[object]|false|none|none|
|»» type|any|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-users">Users</h1>

## Get data for the current authenticated user at a granular level.

<a id="opIdget_current_user_data"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/user \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/user', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/user',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v3/user", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/user HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/user',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/user',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`GET /v3/user`

The returned information includes information about the user that they provided at sign up as well as informationa about the teams they are a part of, company they are with and subscription they have with System Surveyor.

> Example responses

> 200 Response

```json
{
  "id": 12094,
  "user_name": "john_smith",
  "first_name": "John",
  "last_name": "Doe",
  "title": "CEO",
  "email": "foobar@gmail.com",
  "company": "System Surveyor",
  "mobile": "910-423-345",
  "country": "United States of America (USA)",
  "state": "Pennsylvania",
  "city": "Los Angeles",
  "avatar_url": "https://app.systemsurveyor.com/media/common/avatar.png",
  "created_at": 1594652482,
  "teams": [
    {
      "id": 11,
      "name": "John's Team",
      "account_id": 995,
      "role": "team_member",
      "unit": "metric",
      "labor_rate": 15,
      "budget_status": 0,
      "margin_range": 20,
      "logo_url": "https://app.systemsurveyor.com/media/common/team-logo.png"
    }
  ],
  "accounts": [
    {
      "id": 450495,
      "company": "System Surveyor",
      "is_trial": true,
      "is_free": true,
      "cancel_requested": true,
      "trial_expiration": "string",
      "subscription": {
        "id": 123,
        "quantity": 10,
        "plan": {
          "id": 0,
          "name": "Enterprise",
          "max_seats": 0,
          "max_attachments_per_element": 0
        }
      },
      "features": {
        "comments": true,
        "site_tagging": true,
        "report_custom_watermark": true,
        "exclude_powered_by": true,
        "sso": true,
        "hidden_attributes": true,
        "site_access_permissions": true,
        "multiple_teams": true,
        "report_include_ssv_logo": true,
        "report_include_company_logo": true,
        "guest_user": true,
        "add_folder": true,
        "export_survey": true,
        "report_export_excel": true,
        "report_require_ssv_watermark": true,
        "v2_survey": true,
        "public_api": true
      }
    }
  ]
}
```

<h3 id="get-data-for-the-current-authenticated-user-at-a-granular-level.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<h3 id="get-data-for-the-current-authenticated-user-at-a-granular-level.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer|false|none|none|
|» user_name|string|false|none|none|
|» first_name|string|false|none|none|
|» last_name|string|false|none|none|
|» title|string|false|none|none|
|» email|string|false|none|none|
|» company|string|false|none|none|
|» mobile|string|false|none|none|
|» country|string|false|none|none|
|» state|string|false|none|none|
|» city|string|false|none|none|
|» avatar_url|string|false|none|none|
|» created_at|integer|false|none|Unix timestamp when this user was created.|
|» teams|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» name|string|false|none|Name of the team|
|»» account_id|integer|false|none|none|
|»» role|string|false|none|none|
|»» unit|string|false|none|none|
|»» labor_rate|float|false|none|The labor rate is the hourly rate charged by the installation contractor|
|»» budget_status|integer|false|none|Value is either 0 or 1. If 0, then budget estimator calculations are disbaled, but if set to 1 then estimator is enabled.<br>Recommended value is setting it to 0|
|»» margin_range|float|false|none|none|
|»» logo_url|string|false|none|none|
|» accounts|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» company|string|false|none|none|
|»» is_trial|boolean|false|none|none|
|»» is_free|boolean|false|none|none|
|»» cancel_requested|boolean|false|none|none|
|»» trial_expiration|string|false|none|date mm-dd-yyyy of when the trial will expire.|
|»» subscription|object|false|none|none|
|»»» id|integer|false|none|none|
|»»» quantity|integer|false|none|none|
|»»» plan|object|false|none|none|
|»»»» id|integer|false|none|none|
|»»»» name|string|false|none|none|
|»»»» max_seats|integer|false|none|none|
|»»»» max_attachments_per_element|integer|false|none|none|
|»» features|object|false|none|none|
|»»» comments|boolean|false|none|none|
|»»» site_tagging|boolean|false|none|none|
|»»» report_custom_watermark|boolean|false|none|none|
|»»» exclude_powered_by|boolean|false|none|none|
|»»» sso|boolean|false|none|none|
|»»» hidden_attributes|boolean|false|none|none|
|»»» site_access_permissions|boolean|false|none|none|
|»»» multiple_teams|boolean|false|none|none|
|»»» report_include_ssv_logo|boolean|false|none|none|
|»»» report_include_company_logo|boolean|false|none|none|
|»»» guest_user|boolean|false|none|none|
|»»» add_folder|boolean|false|none|none|
|»»» export_survey|boolean|false|none|none|
|»»» report_export_excel|boolean|false|none|none|
|»»» report_require_ssv_watermark|boolean|false|none|none|
|»»» v2_survey|boolean|false|none|none|
|»»» public_api|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|unit|metric|
|unit|imperial|
|budget_status|0|
|budget_status|1|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Update user information associated with the linked account

<a id="opIdupdate_user"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/user \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.patch('/v3/user', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.patch '/v3/user',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/v3/user", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PATCH /v3/user HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "first_name": "string",
  "last_name": "string",
  "user_name": "string",
  "company": "string",
  "mobile": "string",
  "title": "string",
  "country": "string",
  "state": "string",
  "city": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/user',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```javascript--nodejs
const fetch = require('node-fetch');
const inputBody = {
  "first_name": "string",
  "last_name": "string",
  "user_name": "string",
  "company": "string",
  "mobile": "string",
  "title": "string",
  "country": "string",
  "state": "string",
  "city": "string"
};
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/user',
{
  method: 'PATCH',
  body: JSON.stringify(inputBody),
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`PATCH /v3/user`

You can change the values for a user by supplying the new values for first_name, last_name,
user_name, company, mobile, title, country, state, city

> Body parameter

```json
{
  "first_name": "string",
  "last_name": "string",
  "user_name": "string",
  "company": "string",
  "mobile": "string",
  "title": "string",
  "country": "string",
  "state": "string",
  "city": "string"
}
```

<h3 id="update-user-information-associated-with-the-linked-account-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» first_name|body|string|false|none|
|» last_name|body|string|false|none|
|» user_name|body|string|false|none|
|» company|body|string|false|none|
|» mobile|body|string|false|none|
|» title|body|string|false|none|
|» country|body|string|false|none|
|» state|body|string|false|none|
|» city|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "id": 12094,
  "user_name": "foobar",
  "first_name": "John",
  "last_name": "Doe",
  "title": "CEO",
  "email": "foobar@gmail.com",
  "company": "System Surveyor",
  "mobile": "910-423-345",
  "country": "Netherlands",
  "state": "Pennsylvania",
  "city": "Philadelphia",
  "avatar_url": "https://app.systemsurveyor.com/media/common/avatar.png",
  "created_at": 1594652482,
  "teams": [
    {
      "id": 112,
      "name": "John's Team",
      "account_id": 995,
      "role": "team_member",
      "unit": "metric",
      "labor_rate": 10,
      "budget_status": 0,
      "margin_range": 20,
      "logo_url": "https://app.systemsurveyor.com/media/common/team-logo.png"
    }
  ],
  "accounts": [
    {
      "id": 450495,
      "company": "System Surveyor",
      "is_trial": true,
      "is_free": true,
      "cancel_requested": true,
      "trial_expiration": "string",
      "subscription": {
        "id": 123,
        "quantity": 10,
        "plan": {
          "id": 0,
          "name": "Enterprise",
          "max_seats": 0,
          "max_attachments_per_element": 0
        }
      },
      "features": {
        "comments": true,
        "site_tagging": true,
        "report_custom_watermark": true,
        "exclude_powered_by": true,
        "sso": true,
        "hidden_attributes": true,
        "site_access_permissions": true,
        "multiple_teams": true,
        "report_include_ssv_logo": true,
        "report_include_company_logo": true,
        "guest_user": true,
        "add_folder": true,
        "export_survey": true,
        "report_export_excel": true,
        "report_require_ssv_watermark": true,
        "v2_survey": true,
        "public_api": true
      }
    }
  ]
}
```

<h3 id="update-user-information-associated-with-the-linked-account-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<h3 id="update-user-information-associated-with-the-linked-account-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer|false|none|ID for the user.|
|» user_name|string|false|none|User Name given to this user at the time of creation of the account.|
|» first_name|string|false|none|First Name of the User|
|» last_name|string|false|none|Last Name of the User.|
|» title|string|false|none|Title that the user holds in the company.|
|» email|string|false|none|Email for the user.|
|» company|string|false|none|Name of the company that this user is associated|
|» mobile|string|false|none|Mobile number of the User|
|» country|string|false|none|Name of the Country where this user is based|
|» state|string|false|none|State that the user is based in.|
|» city|string|false|none|City that the user is based in.|
|» avatar_url|string|false|none|URL link to a publicly accessible image.|
|» created_at|integer|false|none|Unix timestamp of when the user was created.|
|» teams|[object]|false|none|none|
|»» id|integer|false|none|ID of the team that is associated with this user.|
|»» name|string|false|none|Team Name that this user is associated with|
|»» account_id|integer|false|none|Account id of the user.|
|»» role|string|false|none|Role for the User in the team he is in.|
|»» unit|string|false|none|none|
|»» labor_rate|float|false|none|the hourly rate charged by the installation contractor|
|»» budget_status|integer|false|none|Value is either 0 or 1. If 0, then budget estimator calculations are disbaled, but if set to 1 then estimator is enabled.<br>Recommended value is setting it to 0|
|»» margin_range|float|false|none|none|
|»» logo_url|string|false|none|URL link to a publicly accessible image|
|» accounts|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» company|string|false|none|none|
|»» is_trial|boolean|false|none|none|
|»» is_free|boolean|false|none|none|
|»» cancel_requested|boolean|false|none|none|
|»» trial_expiration|string|false|none|date mm-dd-yyyy of when the trial will expire.|
|»» subscription|object|false|none|none|
|»»» id|integer|false|none|none|
|»»» quantity|integer|false|none|none|
|»»» plan|object|false|none|none|
|»»»» id|integer|false|none|none|
|»»»» name|string|false|none|none|
|»»»» max_seats|integer|false|none|none|
|»»»» max_attachments_per_element|integer|false|none|none|
|»» features|object|false|none|none|
|»»» comments|boolean|false|none|none|
|»»» site_tagging|boolean|false|none|none|
|»»» report_custom_watermark|boolean|false|none|none|
|»»» exclude_powered_by|boolean|false|none|none|
|»»» sso|boolean|false|none|none|
|»»» hidden_attributes|boolean|false|none|none|
|»»» site_access_permissions|boolean|false|none|none|
|»»» multiple_teams|boolean|false|none|none|
|»»» report_include_ssv_logo|boolean|false|none|none|
|»»» report_include_company_logo|boolean|false|none|none|
|»»» guest_user|boolean|false|none|none|
|»»» add_folder|boolean|false|none|none|
|»»» export_survey|boolean|false|none|none|
|»»» report_export_excel|boolean|false|none|none|
|»»» report_require_ssv_watermark|boolean|false|none|none|
|»»» v2_survey|boolean|false|none|none|
|»»» public_api|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|unit|metric|
|unit|imperial|
|budget_status|0|
|budget_status|1|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

# Schemas

<h2 id="tocS_UserResponse">UserResponse</h2>
<!-- backwards compatibility -->
<a id="schemauserresponse"></a>
<a id="schema_UserResponse"></a>
<a id="tocSuserresponse"></a>
<a id="tocsuserresponse"></a>

```json
{
  "first_name": "string",
  "last_name": "string",
  "user_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|first_name|string|false|none|none|
|last_name|string|false|none|none|
|user_id|integer|true|none|none|

<h2 id="tocS_SiteSchema">SiteSchema</h2>
<!-- backwards compatibility -->
<a id="schemasiteschema"></a>
<a id="schema_SiteSchema"></a>
<a id="tocSsiteschema"></a>
<a id="tocssiteschema"></a>

```json
{
  "legacy_site_id": 0,
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": 0
  },
  "reference_id": "string",
  "street": "string",
  "team_id": 0,
  "name": "string",
  "site_id": "string",
  "created_at": null,
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": 0
  },
  "modified_at": null,
  "state": "string",
  "zip_code": "string",
  "is_archived": null,
  "tags": [
    "string"
  ],
  "city": "string",
  "version": 0,
  "label": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|legacy_site_id|integer|false|read-only|none|
|creator|[UserResponse](#schemauserresponse)|false|read-only|none|
|reference_id|string|false|none|none|
|street|string|false|none|none|
|team_id|integer|true|none|none|
|name|string|true|none|none|
|site_id|string|false|none|none|
|created_at|null|false|read-only|none|
|modifier|[UserResponse](#schemauserresponse)|false|read-only|none|
|modified_at|null|false|read-only|none|
|state|string|false|none|none|
|zip_code|string|false|none|none|
|is_archived|any|false|none|none|
|tags|[string]|false|none|none|
|city|string|false|none|none|
|version|integer|false|read-only|none|
|label|string|false|none|none|

<h2 id="tocS_ShareSiteOrSurveyRequestSchema">ShareSiteOrSurveyRequestSchema</h2>
<!-- backwards compatibility -->
<a id="schemasharesiteorsurveyrequestschema"></a>
<a id="schema_ShareSiteOrSurveyRequestSchema"></a>
<a id="tocSsharesiteorsurveyrequestschema"></a>
<a id="tocssharesiteorsurveyrequestschema"></a>

```json
{
  "message": "string",
  "emails": [
    "user@example.com"
  ],
  "expiration_date": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|none|
|emails|[string]|true|none|none|
|expiration_date|any|true|none|none|

<h2 id="tocS_SurveyFields">SurveyFields</h2>
<!-- backwards compatibility -->
<a id="schemasurveyfields"></a>
<a id="schema_SurveyFields"></a>
<a id="tocSsurveyfields"></a>
<a id="tocssurveyfields"></a>

```json
{
  "value": "string",
  "field_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|string|true|none|none|
|field_id|string|true|none|none|

<h2 id="tocS_SurveyOptions">SurveyOptions</h2>
<!-- backwards compatibility -->
<a id="schemasurveyoptions"></a>
<a id="schema_SurveyOptions"></a>
<a id="tocSsurveyoptions"></a>
<a id="tocssurveyoptions"></a>

```json
{
  "value": true,
  "template_name": "string",
  "scope": "template",
  "inputs": [
    {
      "value": "string",
      "field_id": "string"
    }
  ],
  "id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|boolean|true|none|none|
|template_name|string|false|none|none|
|scope|string|true|none|none|
|inputs|[[SurveyFields](#schemasurveyfields)]|false|none|none|
|id|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|scope|template|
|scope|model|
|scope|content|

<h2 id="tocS_SurveyReportRequestSchema">SurveyReportRequestSchema</h2>
<!-- backwards compatibility -->
<a id="schemasurveyreportrequestschema"></a>
<a id="schema_SurveyReportRequestSchema"></a>
<a id="tocSsurveyreportrequestschema"></a>
<a id="tocssurveyreportrequestschema"></a>

```json
{
  "site_id": "string",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "paper_size": "string",
  "is_site_report": false,
  "name": "string",
  "options": [
    {
      "value": true,
      "template_name": "string",
      "scope": "template",
      "inputs": [
        {
          "value": "string",
          "field_id": "string"
        }
      ],
      "id": "string"
    }
  ],
  "is_excel": false,
  "output": "pdf",
  "filters": [
    {}
  ],
  "custom_data": {},
  "survey_ids": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|site_id|string|true|none|none|
|report_id|string(uuid)|true|none|none|
|paper_size|string|false|none|none|
|is_site_report|boolean|false|none|none|
|name|string|true|none|none|
|options|[[SurveyOptions](#schemasurveyoptions)]|false|none|none|
|is_excel|boolean|false|none|none|
|output|string|true|none|none|
|filters|[object]|false|none|none|
|custom_data|object|false|none|none|
|survey_ids|[string]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|output|pdf|
|output|html|
|output|xls|

<h2 id="tocS_SurveyReportRequestSchemaDeprecated">SurveyReportRequestSchemaDeprecated</h2>
<!-- backwards compatibility -->
<a id="schemasurveyreportrequestschemadeprecated"></a>
<a id="schema_SurveyReportRequestSchemaDeprecated"></a>
<a id="tocSsurveyreportrequestschemadeprecated"></a>
<a id="tocssurveyreportrequestschemadeprecated"></a>

```json
{
  "site_id": "string",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "paper_size": "string",
  "is_site_report": false,
  "name": "string",
  "ids": [
    "string"
  ],
  "options": [
    {
      "value": true,
      "template_name": "string",
      "scope": "template",
      "inputs": [
        {
          "value": "string",
          "field_id": "string"
        }
      ],
      "id": "string"
    }
  ],
  "output": "pdf",
  "filters": [
    {}
  ],
  "is_excel": false,
  "custom_data": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|site_id|string|true|none|none|
|report_id|string(uuid)|true|none|none|
|paper_size|string|false|none|none|
|is_site_report|boolean|false|none|none|
|name|string|true|none|none|
|ids|[string]|false|none|none|
|options|[[SurveyOptions](#schemasurveyoptions)]|false|none|none|
|output|string|true|none|none|
|filters|[object]|false|none|none|
|is_excel|boolean|false|none|none|
|custom_data|object|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|output|pdf|
|output|html|
|output|xls|

<h2 id="tocS_EPAccessory">EPAccessory</h2>
<!-- backwards compatibility -->
<a id="schemaepaccessory"></a>
<a id="schema_EPAccessory"></a>
<a id="tocSepaccessory"></a>
<a id="tocsepaccessory"></a>

```json
{
  "description": "string",
  "model": "",
  "labor_hours": [
    0
  ],
  "price": [
    0
  ],
  "created_at": null,
  "manufacturer": "",
  "id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|true|none|none|
|model|string|false|none|none|
|labor_hours|number,null|false|none|none|
|price|number,null|false|none|none|
|created_at|any|false|read-only|none|
|manufacturer|string|false|none|none|
|id|integer|false|read-only|none|

<h2 id="tocS_Attribute">Attribute</h2>
<!-- backwards compatibility -->
<a id="schemaattribute"></a>
<a id="schema_Attribute"></a>
<a id="tocSattribute"></a>
<a id="tocsattribute"></a>

```json
{
  "value": "string",
  "attribute_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|string|true|none|none|
|attribute_id|integer|true|none|none|

<h2 id="tocS_SubElement">SubElement</h2>
<!-- backwards compatibility -->
<a id="schemasubelement"></a>
<a id="schema_SubElement"></a>
<a id="tocSsubelement"></a>
<a id="tocssubelement"></a>

```json
{
  "systemtype_id": "string",
  "element_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemtype_id|string|true|none|none|
|element_id|string|true|none|none|

<h2 id="tocS_Link">Link</h2>
<!-- backwards compatibility -->
<a id="schemalink"></a>
<a id="schema_Link"></a>
<a id="tocSlink"></a>
<a id="tocslink"></a>

```json
{
  "link_type": 0,
  "name": "string",
  "url": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|link_type|integer|true|none|none|
|name|string|true|none|none|
|url|string(url)|true|none|none|

<h2 id="tocS_EPContent">EPContent</h2>
<!-- backwards compatibility -->
<a id="schemaepcontent"></a>
<a id="schema_EPContent"></a>
<a id="tocSepcontent"></a>
<a id="tocsepcontent"></a>

```json
{
  "attribute": [],
  "child": [],
  "pdf_url": []
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|attribute|[[Attribute](#schemaattribute)]|false|none|none|
|child|[[SubElement](#schemasubelement)]|false|none|none|
|pdf_url|[[Link](#schemalink)]|false|none|none|

<h2 id="tocS_ElementProfileSchema">ElementProfileSchema</h2>
<!-- backwards compatibility -->
<a id="schemaelementprofileschema"></a>
<a id="schema_ElementProfileSchema"></a>
<a id="tocSelementprofileschema"></a>
<a id="tocselementprofileschema"></a>

```json
{
  "created_by": 0,
  "is_default": true,
  "team_id": 0,
  "name": "string",
  "accessories": [
    {
      "description": "string",
      "model": "",
      "labor_hours": [
        0
      ],
      "price": [
        0
      ],
      "created_at": null,
      "manufacturer": "",
      "id": 0
    }
  ],
  "created_at": null,
  "modified_at": null,
  "sort": 0,
  "content": {
    "attribute": [],
    "child": [],
    "pdf_url": []
  },
  "id": 0,
  "element_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|created_by|integer|false|read-only|none|
|is_default|boolean|false|none|none|
|team_id|integer|true|none|none|
|name|string|true|none|none|
|accessories|[[EPAccessory](#schemaepaccessory)]|false|none|none|
|created_at|any|false|read-only|none|
|modified_at|any|false|read-only|none|
|sort|integer|false|none|none|
|content|[EPContent](#schemaepcontent)|true|none|none|
|id|integer|false|read-only|none|
|element_id|integer|true|none|none|

<h2 id="tocS_FolderSchema">FolderSchema</h2>
<!-- backwards compatibility -->
<a id="schemafolderschema"></a>
<a id="schema_FolderSchema"></a>
<a id="tocSfolderschema"></a>
<a id="tocsfolderschema"></a>

```json
{
  "name": "string",
  "site_id": 0,
  "site_external_id": "string",
  "id": "string",
  "team_id": 0,
  "label": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|site_id|integer|false|read-only|none|
|site_external_id|string|false|write-only|none|
|id|string|false|read-only|none|
|team_id|integer|false|none|none|
|label|string|false|none|none|

<h2 id="tocS_RelatedUser">RelatedUser</h2>
<!-- backwards compatibility -->
<a id="schemarelateduser"></a>
<a id="schema_RelatedUser"></a>
<a id="tocSrelateduser"></a>
<a id="tocsrelateduser"></a>

```json
{
  "first_name": "string",
  "last_name": "string",
  "user_id": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|first_name|string|false|none|none|
|last_name|string|false|none|none|
|user_id|any|false|none|none|

<h2 id="tocS_SurveyAttribute">SurveyAttribute</h2>
<!-- backwards compatibility -->
<a id="schemasurveyattribute"></a>
<a id="schema_SurveyAttribute"></a>
<a id="tocSsurveyattribute"></a>
<a id="tocssurveyattribute"></a>

```json
{
  "value": "string",
  "name": "string",
  "id": 0,
  "attribute_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|string|true|none|none|
|name|string|true|none|none|
|id|integer|false|read-only|none|
|attribute_id|integer|true|none|none|

<h2 id="tocS_SurveyElementAccessory">SurveyElementAccessory</h2>
<!-- backwards compatibility -->
<a id="schemasurveyelementaccessory"></a>
<a id="schema_SurveyElementAccessory"></a>
<a id="tocSsurveyelementaccessory"></a>
<a id="tocssurveyelementaccessory"></a>

```json
{
  "description": "string",
  "model": "string",
  "price": null,
  "labor_hours": 0,
  "id": "string",
  "row_index": 0,
  "quantity": null,
  "manufacturer": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|false|none|none|
|model|string|true|none|none|
|price|any|false|none|none|
|labor_hours|number|false|none|none|
|id|string|false|read-only|none|
|row_index|integer|true|none|none|
|quantity|any|false|none|none|
|manufacturer|string|true|none|none|

<h2 id="tocS_CablePath">CablePath</h2>
<!-- backwards compatibility -->
<a id="schemacablepath"></a>
<a id="schema_CablePath"></a>
<a id="tocScablepath"></a>
<a id="tocscablepath"></a>

```json
{
  "a_side": null,
  "z_side": null,
  "id": "string",
  "type": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|a_side|any|true|none|none|
|z_side|any|true|none|none|
|id|string|true|none|none|
|type|string|false|none|none|

<h2 id="tocS_PathConnection">PathConnection</h2>
<!-- backwards compatibility -->
<a id="schemapathconnection"></a>
<a id="schema_PathConnection"></a>
<a id="tocSpathconnection"></a>
<a id="tocspathconnection"></a>

```json
{
  "start": null,
  "end": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start|any|false|none|none|
|end|any|false|none|none|

<h2 id="tocS_SurveyElementActivityLog">SurveyElementActivityLog</h2>
<!-- backwards compatibility -->
<a id="schemasurveyelementactivitylog"></a>
<a id="schema_SurveyElementActivityLog"></a>
<a id="tocSsurveyelementactivitylog"></a>
<a id="tocssurveyelementactivitylog"></a>

```json
{
  "creator": 0,
  "id": "string",
  "modifier": 0,
  "entry": "string",
  "created_at": null,
  "modified_at": null,
  "date": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|creator|integer|false|read-only|none|
|id|string|false|none|none|
|modifier|integer|false|read-only|none|
|entry|string|false|none|none|
|created_at|any|false|read-only|none|
|modified_at|any|false|read-only|none|
|date|any|false|none|none|

<h2 id="tocS_SurveyElement">SurveyElement</h2>
<!-- backwards compatibility -->
<a id="schemasurveyelement"></a>
<a id="schema_SurveyElement"></a>
<a id="tocSsurveyelement"></a>
<a id="tocssurveyelement"></a>

```json
{
  "id": "string",
  "name": "string",
  "element_id": 0,
  "element_index": 0,
  "element_profile_id": 0,
  "systemtype_id": 0,
  "variant": null,
  "z_order": 0,
  "position": null,
  "photo_urls": [
    "string"
  ],
  "pdf_urls": null,
  "sync_status": "synced",
  "attributes": [
    {
      "value": "string",
      "name": "string",
      "id": 0,
      "attribute_id": 0
    }
  ],
  "accessories": [
    {
      "description": "string",
      "model": "string",
      "price": null,
      "labor_hours": 0,
      "id": "string",
      "row_index": 0,
      "quantity": null,
      "manufacturer": "string"
    }
  ],
  "children": [
    {
      "id": "string",
      "name": "string",
      "element_id": 0,
      "element_index": 0,
      "element_profile_id": 0,
      "systemtype_id": 0,
      "variant": null,
      "z_order": 0,
      "position": null,
      "photo_urls": [
        "string"
      ],
      "pdf_urls": null,
      "sync_status": "synced",
      "attributes": [
        {
          "value": "string",
          "name": "string",
          "id": 0,
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "description": "string",
          "model": "string",
          "price": null,
          "labor_hours": 0,
          "id": "string",
          "row_index": 0,
          "quantity": null,
          "manufacturer": "string"
        }
      ],
      "children": [],
      "cables": [
        {
          "a_side": null,
          "z_side": null,
          "id": "string",
          "type": "string"
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "creator": 0,
          "id": "string",
          "modifier": 0,
          "entry": "string",
          "created_at": null,
          "modified_at": null,
          "date": null
        }
      ]
    }
  ],
  "cables": [
    {
      "a_side": null,
      "z_side": null,
      "id": "string",
      "type": "string"
    }
  ],
  "connections": {
    "start": null,
    "end": null
  },
  "activity_log": [
    {
      "creator": 0,
      "id": "string",
      "modifier": 0,
      "entry": "string",
      "created_at": null,
      "modified_at": null,
      "date": null
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|none|
|name|string|true|none|none|
|element_id|integer|true|none|none|
|element_index|integer|false|none|none|
|element_profile_id|integer|false|none|none|
|systemtype_id|integer|true|none|none|
|variant|any|false|none|none|
|z_order|integer|false|none|none|
|position|any|true|none|none|
|photo_urls|[string]|false|read-only|none|
|pdf_urls|any|false|read-only|none|
|sync_status|any|false|read-only|none|
|attributes|[[SurveyAttribute](#schemasurveyattribute)]|false|none|none|
|accessories|[[SurveyElementAccessory](#schemasurveyelementaccessory)]|false|none|none|
|children|[[SurveyElement](#schemasurveyelement)]|false|none|none|
|cables|[[CablePath](#schemacablepath)]|false|none|none|
|connections|[PathConnection](#schemapathconnection)|false|none|none|
|activity_log|[[SurveyElementActivityLog](#schemasurveyelementactivitylog)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sync_status|synced|
|sync_status|pending|
|sync_status|errored|

<h2 id="tocS_SurveyAnnotation">SurveyAnnotation</h2>
<!-- backwards compatibility -->
<a id="schemasurveyannotation"></a>
<a id="schema_SurveyAnnotation"></a>
<a id="tocSsurveyannotation"></a>
<a id="tocssurveyannotation"></a>

```json
{
  "start_point": null,
  "fill": null,
  "size": "string",
  "stroke_width": "string",
  "text": "string",
  "end_point": null,
  "coordinates": null,
  "opacity": 1,
  "stroke_color": "string",
  "location": null,
  "category": null,
  "id": "string",
  "font_size": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start_point|any|false|none|none|
|fill|any|false|read-only|none|
|size|string|false|none|none|
|stroke_width|string|true|none|none|
|text|string|false|none|none|
|end_point|any|false|none|none|
|coordinates|any|false|read-only|none|
|opacity|number|false|none|none|
|stroke_color|string|true|none|none|
|location|any|true|none|none|
|category|any|true|none|none|
|id|string|false|read-only|none|
|font_size|string|false|none|none|

<h2 id="tocS_SurveySchema">SurveySchema</h2>
<!-- backwards compatibility -->
<a id="schemasurveyschema"></a>
<a id="schema_SurveySchema"></a>
<a id="tocSsurveyschema"></a>
<a id="tocssurveyschema"></a>

```json
{
  "id": "string",
  "title": "string",
  "label": "string",
  "reference_id": "string",
  "description": "string",
  "summary": "string",
  "location": "string",
  "status": null,
  "site": null,
  "icon_size": 0,
  "is_archived": true,
  "unit": null,
  "version": 0,
  "margin_range": 0,
  "type": null,
  "floorplan_scale": 0,
  "preview_image": "string",
  "floorplan_url": "string",
  "sync_status": "synced",
  "creator": 0,
  "editor": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "modifier": 0,
  "created_at": null,
  "modified_at": null,
  "elements": [
    {
      "id": "string",
      "name": "string",
      "element_id": 0,
      "element_index": 0,
      "element_profile_id": 0,
      "systemtype_id": 0,
      "variant": null,
      "z_order": 0,
      "position": null,
      "photo_urls": [
        "string"
      ],
      "pdf_urls": null,
      "sync_status": "synced",
      "attributes": [
        {
          "value": "string",
          "name": "string",
          "id": 0,
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "description": "string",
          "model": "string",
          "price": null,
          "labor_hours": 0,
          "id": "string",
          "row_index": 0,
          "quantity": null,
          "manufacturer": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "a_side": null,
          "z_side": null,
          "id": "string",
          "type": "string"
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "creator": 0,
          "id": "string",
          "modifier": 0,
          "entry": "string",
          "created_at": null,
          "modified_at": null,
          "date": null
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "fill": null,
      "size": "string",
      "stroke_width": "string",
      "text": "string",
      "end_point": null,
      "coordinates": null,
      "opacity": 1,
      "stroke_color": "string",
      "location": null,
      "category": null,
      "id": "string",
      "font_size": "string"
    }
  ],
  "users": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|read-only|none|
|title|string|true|none|none|
|label|string|false|none|none|
|reference_id|string|false|none|none|
|description|string|false|none|none|
|summary|string|false|none|none|
|location|string|false|none|none|
|status|any|false|write-only|none|
|site|any|false|read-only|none|
|icon_size|integer|true|none|none|
|is_archived|boolean|false|read-only|none|
|unit|any|true|none|none|
|version|integer|false|read-only|none|
|margin_range|number|true|none|none|
|type|any|false|read-only|none|
|floorplan_scale|number|false|none|none|
|preview_image|string|false|read-only|none|
|floorplan_url|string|false|read-only|none|
|sync_status|any|false|read-only|none|
|creator|integer|false|read-only|none|
|editor|[RelatedUser](#schemarelateduser)|false|read-only|none|
|modifier|integer|false|read-only|none|
|created_at|any|false|read-only|none|
|modified_at|any|false|read-only|none|
|elements|[[SurveyElement](#schemasurveyelement)]|false|none|none|
|annotations|[[SurveyAnnotation](#schemasurveyannotation)]|false|none|none|
|users|any|false|read-only|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sync_status|synced|
|sync_status|pending|
|sync_status|errored|

