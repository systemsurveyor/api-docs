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

<h1 id="system-surveyor-api-resources">Resources</h1>

## Gets the corresponding floorplan image for a survey.

<a id="opIdget_survey_floorplan"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /survey/{survey_external_id}/floorplan \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/survey/{survey_external_id}/floorplan', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/octet-stream',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/survey/{survey_external_id}/floorplan',
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
        "Accept": []string{"application/octet-stream"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/survey/{survey_external_id}/floorplan", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /survey/{survey_external_id}/floorplan HTTP/1.1

Accept: application/octet-stream

```

```javascript

const headers = {
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/survey/{survey_external_id}/floorplan',
{
  method: 'POST',

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
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/survey/{survey_external_id}/floorplan',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /survey/{survey_external_id}/floorplan`

User must have at least read access on the survey's site in order to access the floorplan.

<h3 id="gets-the-corresponding-floorplan-image-for-a-survey.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|undefined|true|Survey external ID|

> Example responses

> 200 Response

<h3 id="gets-the-corresponding-floorplan-image-for-a-survey.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Floorplan image binary file|string|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Replaces a survey element's photo at a given path with a new photo.

<a id="opIdupdate_survey_element_photo"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /surveyelement/{survey_element_external_id}/photo \
  -H 'Content-Type: image/png' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'image/png',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/surveyelement/{survey_element_external_id}/photo', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'image/png',
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/surveyelement/{survey_element_external_id}/photo',
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
        "Content-Type": []string{"image/png"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/surveyelement/{survey_element_external_id}/photo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /surveyelement/{survey_element_external_id}/photo HTTP/1.1

Content-Type: image/png
Accept: application/json

```

```javascript
const inputBody = '/tmp/path-to-photo.png';
const headers = {
  'Content-Type':'image/png',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/surveyelement/{survey_element_external_id}/photo',
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
const inputBody = /tmp/path-to-photo.png;
const headers = {
  'Content-Type':'image/png',
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/surveyelement/{survey_element_external_id}/photo',
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

`POST /surveyelement/{survey_element_external_id}/photo`

> Body parameter

<h3 id="replaces-a-survey-element's-photo-at-a-given-path-with-a-new-photo.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_element_id|path|undefined|true|Survey Element external ID|
|body|body|string(binary)|false|none|

> Example responses

> 200 Response

```json
{
  "photo_path": "2022/11/01/39dace0d-4oo5d-47c7-9bff-9c87fbe2c00b.pdf"
}
```

<h3 id="replaces-a-survey-element's-photo-at-a-given-path-with-a-new-photo.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<h3 id="replaces-a-survey-element's-photo-at-a-given-path-with-a-new-photo.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» photo_path|string|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Retrieves a photo image that belongs to a survey element.

<a id="opIdget_survey_element_photo"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /surveyelement/{survey_element_external_id}/photo \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/surveyelement/{survey_element_external_id}/photo', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/octet-stream',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/surveyelement/{survey_element_external_id}/photo',
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
        "Accept": []string{"application/octet-stream"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/surveyelement/{survey_element_external_id}/photo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /surveyelement/{survey_element_external_id}/photo HTTP/1.1

Accept: application/octet-stream

```

```javascript

const headers = {
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/surveyelement/{survey_element_external_id}/photo',
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
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/surveyelement/{survey_element_external_id}/photo',
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

`GET /surveyelement/{survey_element_external_id}/photo`

User must have at least read access on the survey's site in order to access the survey element's photos.

<h3 id="retrieves-a-photo-image-that-belongs-to-a-survey-element.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_element_id|path|undefined|true|Survey Element external ID|
|path|path|undefined|true|Photo relative path|

> Example responses

> 200 Response

<h3 id="retrieves-a-photo-image-that-belongs-to-a-survey-element.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Photo image binary file|string|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Deletes a photo from a survey element's list of photos.

<a id="opIddelete_survey_element_photo"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /surveyelement/{survey_element_external_id}/photo \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/surveyelement/{survey_element_external_id}/photo', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/octet-stream',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/surveyelement/{survey_element_external_id}/photo',
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
        "Accept": []string{"application/octet-stream"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/surveyelement/{survey_element_external_id}/photo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /surveyelement/{survey_element_external_id}/photo HTTP/1.1

Accept: application/octet-stream

```

```javascript

const headers = {
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/surveyelement/{survey_element_external_id}/photo',
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
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/surveyelement/{survey_element_external_id}/photo',
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

`DELETE /surveyelement/{survey_element_external_id}/photo`

<h3 id="deletes-a-photo-from-a-survey-element's-list-of-photos.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_element_id|path|undefined|true|Survey Element external ID|
|path|path|undefined|true|Photo relative path|

> Example responses

> 200 Response

<h3 id="deletes-a-photo-from-a-survey-element's-list-of-photos.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Photo image binary file|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

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
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string"
  },
  "site_external_id": "string",
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
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
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string"
  },
  "site_external_id": "string",
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
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
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string"
  },
  "site_external_id": "string",
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
}
```

<h3 id="creates-a-new-site/survey-folder-or-updates-an-existing-one-if-found.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|
|body|body|[FolderSchema](#schemafolderschema)|true|none|
|» id|body|string|false|none|
|» modified_at|body|any|false|none|
|» team_id|body|integer|false|none|
|» team|body|[Team](#schemateam)|false|none|
|»» name|body|string|false|none|
|»» id|body|string|false|none|
|» site_external_id|body|string|false|none|
|» site_id|body|integer|false|none|
|» label|body|string|false|none|
|» creator|body|[RelatedUser](#schemarelateduser)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|any|false|none|
|» name|body|string|true|none|
|» modifier|body|[RelatedUser](#schemarelateduser)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string",
    "id": "string"
  },
  "site_id": 0,
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
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

<a id="opIdget_folder_sites"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/folder/{folder_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/folder/{folder_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/folder/{folder_id}',
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
    req, err := http.NewRequest("GET", "/v3/folder/{folder_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/folder/{folder_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/folder/{folder_id}',
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
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/folder/{folder_id}',
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

`GET /v3/folder/{folder_id}`

Returns the sites within a folder that the current user has access to.

Query Parameters:
    - `filter[sites_modified_after]`: Return only sites that have sites which have been created, modified, or given access
                                    to after the specified timestamp.

<h3 id="soft-deletes-a-site-folder-or-a-survey-folder.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|

<h3 id="soft-deletes-a-site-folder-or-a-survey-folder.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

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
  "id": "string",
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string",
    "id": "string"
  },
  "site_id": 0,
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
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
  "id": "string",
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string",
    "id": "string"
  },
  "site_id": 0,
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
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
  "id": "string",
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string",
    "id": "string"
  },
  "site_id": 0,
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
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

## Retrieves a report result file after it has been generated.

<a id="opIdget_report_file"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/report?path=%2Fwww%2Fdata%2Fexport%2Fpdf%2F12398%2F2024%2F1%2Fb5d05d5a-d665-4adc-b5b9-60d1c296c695.pdf \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/report', params={
  'path': '/www/data/export/pdf/12398/2024/1/b5d05d5a-d665-4adc-b5b9-60d1c296c695.pdf'
}, headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/octet-stream',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/report',
  params: {
  'path' => 'string'
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
        "Accept": []string{"application/octet-stream"},
        "Authorization": []string{"Bearer {access-token}"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v3/report", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/report?path=%2Fwww%2Fdata%2Fexport%2Fpdf%2F12398%2F2024%2F1%2Fb5d05d5a-d665-4adc-b5b9-60d1c296c695.pdf HTTP/1.1

Accept: application/octet-stream

```

```javascript

const headers = {
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/report?path=%2Fwww%2Fdata%2Fexport%2Fpdf%2F12398%2F2024%2F1%2Fb5d05d5a-d665-4adc-b5b9-60d1c296c695.pdf',
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
  'Accept':'application/octet-stream',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/report?path=%2Fwww%2Fdata%2Fexport%2Fpdf%2F12398%2F2024%2F1%2Fb5d05d5a-d665-4adc-b5b9-60d1c296c695.pdf',
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

`GET /v3/report`

The user must have read access on the site the report was generated for

<h3 id="retrieves-a-report-result-file-after-it-has-been-generated.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|path|query|string|true|none|

> Example responses

> 200 Response

<h3 id="retrieves-a-report-result-file-after-it-has-been-generated.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Report in progress|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unable to process the contained instructions|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Allows scheduling Excel or JSON reports.

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
  "site_id": "de6e23c1-68e8-47eb-a2ef-78b472ec090d",
  "survey_ids": [
    "de6e23c1-68e8-47eb-a2ef-78b472ec090d",
    "f89b13b6-52cc-49de-90a2-cccda01bb0aa"
  ],
  "output": "xls",
  "scope": "site",
  "report_name": "My Bill of Materials report",
  "report_definition_id": "f89b13b6-52cc-49de-90a2-cccda01bb0aa"
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
  "site_id": "de6e23c1-68e8-47eb-a2ef-78b472ec090d",
  "survey_ids": [
    "de6e23c1-68e8-47eb-a2ef-78b472ec090d",
    "f89b13b6-52cc-49de-90a2-cccda01bb0aa"
  ],
  "output": "xls",
  "scope": "site",
  "report_name": "My Bill of Materials report",
  "report_definition_id": "f89b13b6-52cc-49de-90a2-cccda01bb0aa"
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

Legacy Excel reports (reports that are processed by https://github.com/systemsurveyor/ssv-reporting) cannot be scheduled
using this endpoint. They need to be scheduled using `POST /v2/report`.

> Body parameter

```json
{
  "site_id": "de6e23c1-68e8-47eb-a2ef-78b472ec090d",
  "survey_ids": [
    "de6e23c1-68e8-47eb-a2ef-78b472ec090d",
    "f89b13b6-52cc-49de-90a2-cccda01bb0aa"
  ],
  "output": "xls",
  "scope": "site",
  "report_name": "My Bill of Materials report",
  "report_definition_id": "f89b13b6-52cc-49de-90a2-cccda01bb0aa"
}
```

<h3 id="allows-scheduling-excel-or-json-reports.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» site_id|body|string|false|External ID of the report's site|
|» survey_ids|body|[string]|false|List of external IDs of surveys in the report|
|» output|body|string|false|Output format for the report|
|» scope|body|string|false|Whether the report is a site report or survey report|
|» report_name|body|string|false|Name given to the new report|
|» report_definition_id|body|string|false|External ID of the report definition the new report belongs to|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» output|xls|
|» output|json|
|» scope|site|
|» scope|survey|

> Example responses

> 202 Response

```json
{
  "report_id": 2545
}
```

<h3 id="allows-scheduling-excel-or-json-reports.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Report scheduled successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Unable to process the contained instructions|None|

<h3 id="allows-scheduling-excel-or-json-reports.-responseschema">Response Schema</h3>

Status Code **202**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» report_id|integer|false|none|Unique ID of the scheduled report|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Returns all reports that have been created by the current user.

<a id="opIdget_current_user_reports"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/reports \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/reports', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/reports',
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
    req, err := http.NewRequest("GET", "/v3/reports", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/reports HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/reports',
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

fetch('/v3/reports',
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

`GET /v3/reports`

> Example responses

> 200 Response

```json
{
  "survey_id": 0,
  "expires_at": null,
  "token": "string",
  "status": null,
  "id": 0,
  "site_id": 0,
  "type": null,
  "name": "string",
  "file_path": "string"
}
```

<h3 id="returns-all-reports-that-have-been-created-by-the-current-user.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ReportSchema](#schemareportschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

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
  "site_id": "string",
  "label": "string",
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string"
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
  "site_id": "string",
  "label": "string",
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string"
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
  "site_id": "string",
  "label": "string",
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string"
}
```

<h3 id="creates-a-new-site-with-a-specific-`site_id`-or-updates-the-site-if-it-already-exists-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|body|body|[SiteSchema](#schemasiteschema)|true|none|
|» site_id|body|string|false|none|
|» legacy_site_id|body|integer|false|none|
|» version|body|integer|false|none|
|» label|body|string|false|none|
|» modified_at|body|null|false|none|
|» is_archived|body|any|false|none|
|» team_id|body|integer|true|none|
|» state|body|string|false|none|
|» reference_id|body|string|false|none|
|» modifier|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» creator|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» tags|body|[string]|false|none|
|» street|body|string|false|none|
|» name|body|string|true|none|
|» zip_code|body|string|false|none|
|» city|body|string|false|none|
|» created_at|body|null|false|none|

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
  "site_id": "string",
  "label": "string",
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string"
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
  "site_id": "string",
  "label": "string",
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string"
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
  "site_id": "string",
  "label": "string",
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string"
}
```

<h3 id="update-specific-fields-of-a-site-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|body|body|[SiteSchema](#schemasiteschema)|true|none|
|» site_id|body|string|false|none|
|» legacy_site_id|body|integer|false|none|
|» version|body|integer|false|none|
|» label|body|string|false|none|
|» modified_at|body|null|false|none|
|» is_archived|body|any|false|none|
|» team_id|body|integer|true|none|
|» state|body|string|false|none|
|» reference_id|body|string|false|none|
|» modifier|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» creator|body|[UserResponse](#schemauserresponse)|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|»» user_id|body|integer|true|none|
|» tags|body|[string]|false|none|
|» street|body|string|false|none|
|» name|body|string|true|none|
|» zip_code|body|string|false|none|
|» city|body|string|false|none|
|» created_at|body|null|false|none|

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

<a id="opIdget_user_sites_and_site_folders"></a>

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
|q|query|string|false|Apply search to query|
|page[number]|query|integer|false|Page to retrieve from the entire result set|
|page[size]|query|integer|false|Max amount of objects to return per page in the response|
|filter[modified_after]|query|integer|false|Return only sites that have been created, modified, or favorited (added to workbench) after an specific datetime (in UTC Epoch format).|
|filter[deleted_after]|query|integer|false|(DEPRECATED) Return only sites that were deleted after an specified timestamp. Limited site data is returned using this filter.|
|filter[favorites_only]|query|integer|false|Filters results to only include sites the user has added to their workbench|
|filter[folder_id]|query|string|false|Returns only sites that belong to a specific folder|
|filter[accessible_after]|query|integer|false|Returns only sites and folders where the user has been granted access to after a specified time|

> Example responses

> 200 Response

```json
{
  "sites": [
    {
      "id": "46787da3-1e6e-4d9b-a858-ac9e12dc3efb",
      "name": "Union Square",
      "site_count": 5,
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
|»» site_count|integer|false|none|For folders, returns the number of sites within the folder accessible by the user|
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

## Adds a list of sites to the user's workbench.

<a id="opIdadd_sites_to_favorites"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/site_favorites \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v3/site_favorites', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/v3/site_favorites',
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
    req, err := http.NewRequest("POST", "/v3/site_favorites", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /v3/site_favorites HTTP/1.1

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

fetch('/v3/site_favorites',
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
const inputBody = [
  "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb"
];
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/site_favorites',
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

`POST /v3/site_favorites`

Sites that are already in the workbench will be ignored.

> Body parameter

```json
[
  "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb"
]
```

<h3 id="adds-a-list-of-sites-to-the-user's-workbench.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|

<h3 id="adds-a-list-of-sites-to-the-user's-workbench.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Removes sites from the current user's workbench.

<a id="opIdremove_sites_from_favorites"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/site_favorites \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/site_favorites', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/site_favorites',
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
    req, err := http.NewRequest("DELETE", "/v3/site_favorites", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/site_favorites HTTP/1.1

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

fetch('/v3/site_favorites',
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

fetch('/v3/site_favorites',
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

`DELETE /v3/site_favorites`

Sites that are not in the users workbench and are requested for removal will be ignored.

> Body parameter

```json
[
  "b14663f6-9ad1-40c0-8a1a-32f2e19b1ccb"
]
```

<h3 id="removes-sites-from-the-current-user's-workbench.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|

<h3 id="removes-sites-from-the-current-user's-workbench.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Returns all of the current user's favorite sites across all teams.

<a id="opIdget_user_favorite_sites"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/favorite_sites \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/favorite_sites', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/favorite_sites',
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
    req, err := http.NewRequest("GET", "/v3/favorite_sites", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/favorite_sites HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/favorite_sites',
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

fetch('/v3/favorite_sites',
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

`GET /v3/favorite_sites`

Results are ordered by most recently favorited.

Query Parameters:

  - filter[modified_after]: Return only sites that have been added or removed from favorites after the specified timestamp.

<h3 id="returns-all-of-the-current-user's-favorite-sites-across-all-teams.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page[number]|query|integer|false|Page to retrieve from the entire result set|
|page[size]|query|integer|false|Max amount of objects to return per page in the response|
|filter[modified_after]|query|integer|false|Return only sites that have been added or removed from favorites after the specified timestamp.|

> Example responses

> 200 Response

```json
{
  "favorite_sites": [
    {
      "id": "46787da3-1e6e-4d9b-a858-ac9e12dc3efb",
      "name": "Union Square",
      "favorited_at": 1645157198
    }
  ],
  "unfavorited_sites": [
    {
      "id": "46787da3-1e6e-4d9b-a858-ac9e12dc3efb",
      "name": "Union Square",
      "unfavorited_at": 1645157198
    }
  ]
}
```

<h3 id="returns-all-of-the-current-user's-favorite-sites-across-all-teams.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<h3 id="returns-all-of-the-current-user's-favorite-sites-across-all-teams.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» favorite_sites|[object]|false|none|List of user's favorited sites|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» favorited_at|number|false|none|Unix Timestamp indicating when the site was added to favorites.|
|» unfavorited_sites|[object]|false|none|Result list of sites unfavorited after the specified timestamp|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» unfavorited_at|number|false|none|Unix Timestamp indicating when the site was removed from favorites.|

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

## Sets an editor lock on a survey so that other users cannot edit it

<a id="opIdlock_survey"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/survey/{survey_id}/lock \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v3/survey/{survey_id}/lock', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/v3/survey/{survey_id}/lock',
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
    req, err := http.NewRequest("POST", "/v3/survey/{survey_id}/lock", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /v3/survey/{survey_id}/lock HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/lock',
{
  method: 'POST',

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

fetch('/v3/survey/{survey_id}/lock',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

`POST /v3/survey/{survey_id}/lock`

If the survey already has an editor lock from another user, the user requesting the lock will need to request the
current editor to release the lock.

<h3 id="sets-an-editor-lock-on-a-survey-so-that-other-users-cannot-edit-it-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|string|true|Survey ID|

<h3 id="sets-an-editor-lock-on-a-survey-so-that-other-users-cannot-edit-it-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Email has been sent to current survey editor to release lock|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Removes a survey's current editor

<a id="opIdremove_survey_editor_lock"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/survey/{survey_id}/lock \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/survey/{survey_id}/lock', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/survey/{survey_id}/lock',
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
    req, err := http.NewRequest("DELETE", "/v3/survey/{survey_id}/lock", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/survey/{survey_id}/lock HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/lock',
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

fetch('/v3/survey/{survey_id}/lock',
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

`DELETE /v3/survey/{survey_id}/lock`

<h3 id="removes-a-survey's-current-editor-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|string|true|Survey ID|

<h3 id="removes-a-survey's-current-editor-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-comments">Comments</h1>

## Adds a new comment to a survey.

<a id="opIdadd_survey_comment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/survey/{survey_id}/comment \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/v3/survey/{survey_id}/comment', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.post '/v3/survey/{survey_id}/comment',
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
    req, err := http.NewRequest("POST", "/v3/survey/{survey_id}/comment", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
POST /v3/survey/{survey_id}/comment HTTP/1.1

Content-Type: application/json

```

```javascript
const inputBody = '{
  "corpus": "Lorem ipsum",
  "parent_id": 2334
}';
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comment',
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
  "corpus": "Lorem ipsum",
  "parent_id": 2334
};
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comment',
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

`POST /v3/survey/{survey_id}/comment`

> Body parameter

```json
{
  "corpus": "Lorem ipsum",
  "parent_id": 2334
}
```

<h3 id="adds-a-new-comment-to-a-survey.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» corpus|body|string|false|none|
|» parent_id|body|number|false|none|

<h3 id="adds-a-new-comment-to-a-survey.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Get all comments from a survey

<a id="opIdget_survey_comments"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/survey/{survey_id}/comments \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/survey/{survey_id}/comments', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/survey/{survey_id}/comments',
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
    req, err := http.NewRequest("GET", "/v3/survey/{survey_id}/comments", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/survey/{survey_id}/comments HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comments',
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
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comments',
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

`GET /v3/survey/{survey_id}/comments`

<h3 id="get-all-comments-from-a-survey-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|string|true|Survey ID|

<h3 id="get-all-comments-from-a-survey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Deletes a comment in a survey.

<a id="opIddelete_survey_comment"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/survey/{survey_id}/comment/{comment_id} \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Authorization': 'Bearer {access-token}'
}

r = requests.delete('/v3/survey/{survey_id}/comment/{comment_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.delete '/v3/survey/{survey_id}/comment/{comment_id}',
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
    req, err := http.NewRequest("DELETE", "/v3/survey/{survey_id}/comment/{comment_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
DELETE /v3/survey/{survey_id}/comment/{comment_id} HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comment/{comment_id}',
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

fetch('/v3/survey/{survey_id}/comment/{comment_id}',
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

`DELETE /v3/survey/{survey_id}/comment/{comment_id}`

Users are only allowed to delete their own comments.

<h3 id="deletes-a-comment-in-a-survey.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|string|true|Survey external ID|
|comment_id|path|number|true|Comment ID|

<h3 id="deletes-a-comment-in-a-survey.-responses">Responses</h3>

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

## Allows editing a comment in a survey.

<a id="opIdedit_survey_comment"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/survey/{survey_id}/comment/{comment_id} \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.patch('/v3/survey/{survey_id}/comment/{comment_id}', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.patch '/v3/survey/{survey_id}/comment/{comment_id}',
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
    req, err := http.NewRequest("PATCH", "/v3/survey/{survey_id}/comment/{comment_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
PATCH /v3/survey/{survey_id}/comment/{comment_id} HTTP/1.1

Content-Type: application/json

```

```javascript
const inputBody = '{
  "corpus": "Lorem ipsum",
  "is_open": true
}';
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comment/{comment_id}',
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
  "corpus": "Lorem ipsum",
  "is_open": true
};
const headers = {
  'Content-Type':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/survey/{survey_id}/comment/{comment_id}',
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

`PATCH /v3/survey/{survey_id}/comment/{comment_id}`

Editing/deleting and closing/re-opening comments will only be allowed for comment creators.

Team/Account admins can close and reopen all comments on the survey.

> Body parameter

```json
{
  "corpus": "Lorem ipsum",
  "is_open": true
}
```

<h3 id="allows-editing-a-comment-in-a-survey.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_id|path|string|true|Survey external ID|
|comment_id|path|number|true|Comment ID|
|body|body|object|true|none|
|» corpus|body|string|false|none|
|» is_open|body|boolean|false|none|

<h3 id="allows-editing-a-comment-in-a-survey.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

<h1 id="system-surveyor-api-systemtypes">SystemTypes</h1>

## Returns a team's selected system types.

<a id="opIdget_team_selected_system_types"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/team/{team_id}/system_types \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/team/{team_id}/system_types', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/team/{team_id}/system_types',
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
    req, err := http.NewRequest("GET", "/v3/team/{team_id}/system_types", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/team/{team_id}/system_types HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/team/{team_id}/system_types',
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

fetch('/v3/team/{team_id}/system_types',
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

`GET /v3/team/{team_id}/system_types`

<h3 id="returns-a-team's-selected-system-types.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|team_id|path|number|true|none|

> Example responses

> 200 Response

```json
{
  "elements": [
    {
      "abbreviation": "string",
      "category": {
        "name": "string",
        "abbreviation": "string",
        "id": 0
      },
      "icon": null,
      "name": "string",
      "id": 0,
      "sort_order": 0
    }
  ],
  "abbreviation": "string",
  "id": 0,
  "element_color": "string",
  "name": "string",
  "sort": 0
}
```

<h3 id="returns-a-team's-selected-system-types.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[SystemTypeSchema](#schemasystemtypeschema)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

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

## Returns information about all members of a team.d

<a id="opIdget_team_members"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/team/{team_id}/membership \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/team/{team_id}/membership', headers = headers)

print(r.json())

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'Bearer {access-token}'
}

result = RestClient.get '/v3/team/{team_id}/membership',
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
    req, err := http.NewRequest("GET", "/v3/team/{team_id}/membership", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

```http
GET /v3/team/{team_id}/membership HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'Bearer {access-token}'
};

fetch('/v3/team/{team_id}/membership',
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

fetch('/v3/team/{team_id}/membership',
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

`GET /v3/team/{team_id}/membership`

> Example responses

> 200 Response

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "company": "System Surveyor",
  "email": "jdoe@gmail.com",
  "avatar_url": "string",
  "user_id": 140956,
  "role": "admin",
  "is_enable": true
}
```

<h3 id="returns-information-about-all-members-of-a-team.d-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<h3 id="returns-information-about-all-members-of-a-team.d-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» first_name|string|false|none|none|
|» last_name|string|false|none|none|
|» company|string|false|none|none|
|» email|string|false|none|none|
|» avatar_url|string|false|none|none|
|» user_id|number|false|none|none|
|» role|string|false|none|none|
|» is_enable|boolean|false|none|none|

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
          "max_elements_per_survey": 0,
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
        "public_api": true,
        "v2_report": true
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
|»»»» max_elements_per_survey|integer|false|none|none|
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
|»»» v2_report|boolean|false|none|none|

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
          "max_elements_per_survey": 0,
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
        "public_api": true,
        "v2_report": true
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
|»»»» max_elements_per_survey|integer|false|none|none|
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
|»»» v2_report|boolean|false|none|none|

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

<h2 id="tocS_ElementCategory">ElementCategory</h2>
<!-- backwards compatibility -->
<a id="schemaelementcategory"></a>
<a id="schema_ElementCategory"></a>
<a id="tocSelementcategory"></a>
<a id="tocselementcategory"></a>

```json
{
  "name": "string",
  "abbreviation": "string",
  "id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|abbreviation|string|true|none|none|
|id|integer|false|read-only|none|

<h2 id="tocS_ElementSchema">ElementSchema</h2>
<!-- backwards compatibility -->
<a id="schemaelementschema"></a>
<a id="schema_ElementSchema"></a>
<a id="tocSelementschema"></a>
<a id="tocselementschema"></a>

```json
{
  "abbreviation": "string",
  "category": {
    "name": "string",
    "abbreviation": "string",
    "id": 0
  },
  "icon": null,
  "name": "string",
  "id": 0,
  "sort_order": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|abbreviation|string|false|none|none|
|category|[ElementCategory](#schemaelementcategory)|false|none|none|
|icon|any|false|read-only|none|
|name|string|false|none|none|
|id|integer|false|read-only|none|
|sort_order|integer|false|none|none|

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
  "site_id": "string",
  "legacy_site_id": 0,
  "version": 0,
  "label": "string",
  "modified_at": null,
  "is_archived": null,
  "team_id": 0,
  "state": "string",
  "reference_id": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": 0
  },
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": 0
  },
  "tags": [
    "string"
  ],
  "street": "string",
  "name": "string",
  "zip_code": "string",
  "city": "string",
  "created_at": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|site_id|string|false|none|none|
|legacy_site_id|integer|false|read-only|none|
|version|integer|false|read-only|none|
|label|string|false|none|none|
|modified_at|null|false|read-only|none|
|is_archived|any|false|none|none|
|team_id|integer|true|none|none|
|state|string|false|none|none|
|reference_id|string|false|none|none|
|modifier|[UserResponse](#schemauserresponse)|false|read-only|none|
|creator|[UserResponse](#schemauserresponse)|false|read-only|none|
|tags|[string]|false|none|none|
|street|string|false|none|none|
|name|string|true|none|none|
|zip_code|string|false|none|none|
|city|string|false|none|none|
|created_at|null|false|read-only|none|

<h2 id="tocS_ShareSiteOrSurveyRequestSchema">ShareSiteOrSurveyRequestSchema</h2>
<!-- backwards compatibility -->
<a id="schemasharesiteorsurveyrequestschema"></a>
<a id="schema_ShareSiteOrSurveyRequestSchema"></a>
<a id="tocSsharesiteorsurveyrequestschema"></a>
<a id="tocssharesiteorsurveyrequestschema"></a>

```json
{
  "emails": [
    "user@example.com"
  ],
  "expiration_date": null,
  "message": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emails|[string]|true|none|none|
|expiration_date|any|true|none|none|
|message|string|false|none|none|

<h2 id="tocS_SurveyFields">SurveyFields</h2>
<!-- backwards compatibility -->
<a id="schemasurveyfields"></a>
<a id="schema_SurveyFields"></a>
<a id="tocSsurveyfields"></a>
<a id="tocssurveyfields"></a>

```json
{
  "field_id": "string",
  "value": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|field_id|string|true|none|none|
|value|string|true|none|none|

<h2 id="tocS_SurveyOptions">SurveyOptions</h2>
<!-- backwards compatibility -->
<a id="schemasurveyoptions"></a>
<a id="schema_SurveyOptions"></a>
<a id="tocSsurveyoptions"></a>
<a id="tocssurveyoptions"></a>

```json
{
  "inputs": [
    {
      "field_id": "string",
      "value": "string"
    }
  ],
  "value": true,
  "id": "string",
  "scope": "template",
  "template_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|inputs|[[SurveyFields](#schemasurveyfields)]|false|none|none|
|value|boolean|true|none|none|
|id|string|true|none|none|
|scope|string|true|none|none|
|template_name|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|scope|template|
|scope|model|
|scope|content|

<h2 id="tocS_SurveyReportRequestSchemaDeprecated">SurveyReportRequestSchemaDeprecated</h2>
<!-- backwards compatibility -->
<a id="schemasurveyreportrequestschemadeprecated"></a>
<a id="schema_SurveyReportRequestSchemaDeprecated"></a>
<a id="tocSsurveyreportrequestschemadeprecated"></a>
<a id="tocssurveyreportrequestschemadeprecated"></a>

```json
{
  "name": "string",
  "is_site_report": false,
  "paper_size": "string",
  "is_excel": false,
  "options": [
    {
      "inputs": [
        {
          "field_id": "string",
          "value": "string"
        }
      ],
      "value": true,
      "id": "string",
      "scope": "template",
      "template_name": "string"
    }
  ],
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "output": "pdf",
  "site_id": "string",
  "filters": [
    {}
  ],
  "custom_data": {},
  "ids": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|is_site_report|boolean|false|none|none|
|paper_size|string|false|none|none|
|is_excel|boolean|false|none|none|
|options|[[SurveyOptions](#schemasurveyoptions)]|false|none|none|
|report_id|string(uuid)|true|none|none|
|output|string|true|none|none|
|site_id|string|true|none|none|
|filters|[object]|false|none|none|
|custom_data|object|false|none|none|
|ids|[string]|false|none|none|

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
  "model": "",
  "manufacturer": "",
  "id": 0,
  "price": [
    0
  ],
  "labor_hours": [
    0
  ],
  "description": "string",
  "created_at": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|model|string|false|none|none|
|manufacturer|string|false|none|none|
|id|integer|false|read-only|none|
|price|number,null|false|none|none|
|labor_hours|number,null|false|none|none|
|description|string|true|none|none|
|created_at|any|false|read-only|none|

<h2 id="tocS_Link">Link</h2>
<!-- backwards compatibility -->
<a id="schemalink"></a>
<a id="schema_Link"></a>
<a id="tocSlink"></a>
<a id="tocslink"></a>

```json
{
  "name": "string",
  "url": "string",
  "link_type": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|url|string(url)|true|none|none|
|link_type|integer|true|none|none|

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

<h2 id="tocS_EPContent">EPContent</h2>
<!-- backwards compatibility -->
<a id="schemaepcontent"></a>
<a id="schema_EPContent"></a>
<a id="tocSepcontent"></a>
<a id="tocsepcontent"></a>

```json
{
  "pdf_url": [],
  "attribute": [],
  "child": []
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pdf_url|[[Link](#schemalink)]|false|none|none|
|attribute|[[Attribute](#schemaattribute)]|false|none|none|
|child|[[SubElement](#schemasubelement)]|false|none|none|

<h2 id="tocS_ElementProfileSchema">ElementProfileSchema</h2>
<!-- backwards compatibility -->
<a id="schemaelementprofileschema"></a>
<a id="schema_ElementProfileSchema"></a>
<a id="tocSelementprofileschema"></a>
<a id="tocselementprofileschema"></a>

```json
{
  "element_id": 0,
  "created_by": 0,
  "modified_at": null,
  "id": 0,
  "created_at": null,
  "accessories": [
    {
      "model": "",
      "manufacturer": "",
      "id": 0,
      "price": [
        0
      ],
      "labor_hours": [
        0
      ],
      "description": "string",
      "created_at": null
    }
  ],
  "is_default": true,
  "name": "string",
  "content": {
    "pdf_url": [],
    "attribute": [],
    "child": []
  },
  "sort": 0,
  "team_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|element_id|integer|true|none|none|
|created_by|integer|false|read-only|none|
|modified_at|any|false|read-only|none|
|id|integer|false|read-only|none|
|created_at|any|false|read-only|none|
|accessories|[[EPAccessory](#schemaepaccessory)]|false|none|none|
|is_default|boolean|false|none|none|
|name|string|true|none|none|
|content|[EPContent](#schemaepcontent)|true|none|none|
|sort|integer|false|none|none|
|team_id|integer|true|none|none|

<h2 id="tocS_Team">Team</h2>
<!-- backwards compatibility -->
<a id="schemateam"></a>
<a id="schema_Team"></a>
<a id="tocSteam"></a>
<a id="tocsteam"></a>

```json
{
  "name": "string",
  "id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|id|string|false|read-only|none|

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

<h2 id="tocS_FolderSchema">FolderSchema</h2>
<!-- backwards compatibility -->
<a id="schemafolderschema"></a>
<a id="schema_FolderSchema"></a>
<a id="tocSfolderschema"></a>
<a id="tocsfolderschema"></a>

```json
{
  "id": "string",
  "modified_at": null,
  "team_id": 0,
  "team": {
    "name": "string",
    "id": "string"
  },
  "site_external_id": "string",
  "site_id": 0,
  "label": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "name": "string",
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|read-only|none|
|modified_at|any|false|none|none|
|team_id|integer|false|none|none|
|team|[Team](#schemateam)|false|none|none|
|site_external_id|string|false|write-only|none|
|site_id|integer|false|read-only|none|
|label|string|false|none|none|
|creator|[RelatedUser](#schemarelateduser)|false|none|none|
|name|string|true|none|none|
|modifier|[RelatedUser](#schemarelateduser)|false|none|none|

<h2 id="tocS_ReportSchema">ReportSchema</h2>
<!-- backwards compatibility -->
<a id="schemareportschema"></a>
<a id="schema_ReportSchema"></a>
<a id="tocSreportschema"></a>
<a id="tocsreportschema"></a>

```json
{
  "survey_id": 0,
  "expires_at": null,
  "token": "string",
  "status": null,
  "id": 0,
  "site_id": 0,
  "type": null,
  "name": "string",
  "file_path": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|survey_id|integer|false|none|none|
|expires_at|any|false|none|none|
|token|string|false|none|none|
|status|any|false|none|none|
|id|integer|false|none|none|
|site_id|integer|false|none|none|
|type|any|false|none|none|
|name|string|false|none|none|
|file_path|string|false|none|none|

<h2 id="tocS_SurveyAttribute">SurveyAttribute</h2>
<!-- backwards compatibility -->
<a id="schemasurveyattribute"></a>
<a id="schema_SurveyAttribute"></a>
<a id="tocSsurveyattribute"></a>
<a id="tocssurveyattribute"></a>

```json
{
  "name": "string",
  "value": "string",
  "id": 0,
  "attribute_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|value|string|true|none|none|
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
  "model": "string",
  "quantity": null,
  "manufacturer": "string",
  "id": "string",
  "row_index": 0,
  "price": null,
  "labor_hours": 0,
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|model|string|true|none|none|
|quantity|any|false|none|none|
|manufacturer|string|true|none|none|
|id|string|false|read-only|none|
|row_index|integer|true|none|none|
|price|any|false|none|none|
|labor_hours|number|false|none|none|
|description|string|false|none|none|

<h2 id="tocS_CablePath">CablePath</h2>
<!-- backwards compatibility -->
<a id="schemacablepath"></a>
<a id="schema_CablePath"></a>
<a id="tocScablepath"></a>
<a id="tocscablepath"></a>

```json
{
  "external_id": "string",
  "a_side": null,
  "z_side": null,
  "id": "string",
  "type": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|external_id|string|true|none|none|
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
  "id": "string",
  "modified_at": null,
  "date": null,
  "entry": "string",
  "creator": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "modifier": {
    "first_name": "string",
    "last_name": "string",
    "user_id": null
  },
  "created_at": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|modified_at|any|false|read-only|none|
|date|any|false|none|none|
|entry|string|false|none|none|
|creator|[RelatedUser](#schemarelateduser)|false|read-only|none|
|modifier|[RelatedUser](#schemarelateduser)|false|read-only|none|
|created_at|any|false|read-only|none|

<h2 id="tocS_WebLink">WebLink</h2>
<!-- backwards compatibility -->
<a id="schemaweblink"></a>
<a id="schema_WebLink"></a>
<a id="tocSweblink"></a>
<a id="tocsweblink"></a>

```json
{
  "name": "string",
  "url": "string",
  "link_type": 2
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|url|string|true|none|none|
|link_type|any|false|write-only|none|

<h2 id="tocS_PDFLink">PDFLink</h2>
<!-- backwards compatibility -->
<a id="schemapdflink"></a>
<a id="schema_PDFLink"></a>
<a id="tocSpdflink"></a>
<a id="tocspdflink"></a>

```json
{
  "name": "string",
  "url": "string",
  "link_type": 1
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|url|string|true|none|none|
|link_type|any|false|none|none|

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
  "sync_status": "synced",
  "attributes": [
    {
      "name": "string",
      "value": "string",
      "id": 0,
      "attribute_id": 0
    }
  ],
  "accessories": [
    {
      "model": "string",
      "quantity": null,
      "manufacturer": "string",
      "id": "string",
      "row_index": 0,
      "price": null,
      "labor_hours": 0,
      "description": "string"
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
      "sync_status": "synced",
      "attributes": [
        {
          "name": "string",
          "value": "string",
          "id": 0,
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "model": "string",
          "quantity": null,
          "manufacturer": "string",
          "id": "string",
          "row_index": 0,
          "price": null,
          "labor_hours": 0,
          "description": "string"
        }
      ],
      "children": [],
      "cables": [
        {
          "external_id": "string",
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
          "modified_at": null,
          "date": null,
          "entry": "string",
          "creator": {
            "first_name": "string",
            "last_name": "string",
            "user_id": null
          },
          "modifier": {
            "first_name": "string",
            "last_name": "string",
            "user_id": null
          },
          "created_at": null
        }
      ],
      "pdf_urls": null,
      "web_links": [
        {
          "name": "string",
          "url": "string",
          "link_type": 2
        }
      ],
      "photos": [
        "string"
      ],
      "pdfs": [
        {
          "name": "string",
          "url": "string",
          "link_type": 1
        }
      ]
    }
  ],
  "cables": [
    {
      "external_id": "string",
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
      "modified_at": null,
      "date": null,
      "entry": "string",
      "creator": {
        "first_name": "string",
        "last_name": "string",
        "user_id": null
      },
      "modifier": {
        "first_name": "string",
        "last_name": "string",
        "user_id": null
      },
      "created_at": null
    }
  ],
  "pdf_urls": null,
  "web_links": [
    {
      "name": "string",
      "url": "string",
      "link_type": 2
    }
  ],
  "photos": [
    "string"
  ],
  "pdfs": [
    {
      "name": "string",
      "url": "string",
      "link_type": 1
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
|sync_status|any|false|read-only|none|
|attributes|[[SurveyAttribute](#schemasurveyattribute)]|false|none|none|
|accessories|[[SurveyElementAccessory](#schemasurveyelementaccessory)]|false|none|none|
|children|[[SurveyElement](#schemasurveyelement)]|false|none|none|
|cables|[[CablePath](#schemacablepath)]|false|none|none|
|connections|[PathConnection](#schemapathconnection)|false|none|none|
|activity_log|[[SurveyElementActivityLog](#schemasurveyelementactivitylog)]|false|none|none|
|pdf_urls|any|false|read-only|none|
|web_links|[[WebLink](#schemaweblink)]|false|none|none|
|photos|[string]|false|write-only|none|
|pdfs|[[PDFLink](#schemapdflink)]|false|write-only|none|

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
  "font_size": "string",
  "text": "string",
  "category": null,
  "id": "string",
  "stroke_width": "string",
  "coordinates": null,
  "stroke_color": "string",
  "fill": null,
  "size": "string",
  "location": null,
  "end_point": null,
  "opacity": 1,
  "start_point": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|font_size|string|false|none|none|
|text|string|false|none|none|
|category|any|true|none|none|
|id|string|false|read-only|none|
|stroke_width|string|true|none|none|
|coordinates|any|false|none|none|
|stroke_color|string|true|none|none|
|fill|any|false|none|none|
|size|string|false|none|none|
|location|any|true|none|none|
|end_point|any|false|none|none|
|opacity|number|false|none|none|
|start_point|any|false|none|none|

<h2 id="tocS_BoundaryPoint">BoundaryPoint</h2>
<!-- backwards compatibility -->
<a id="schemaboundarypoint"></a>
<a id="schema_BoundaryPoint"></a>
<a id="tocSboundarypoint"></a>
<a id="tocsboundarypoint"></a>

```json
{
  "y": 0,
  "x": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|y|number|true|none|none|
|x|number|true|none|none|

<h2 id="tocS_SurveyBoundary">SurveyBoundary</h2>
<!-- backwards compatibility -->
<a id="schemasurveyboundary"></a>
<a id="schema_SurveyBoundary"></a>
<a id="tocSsurveyboundary"></a>
<a id="tocssurveyboundary"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "points": [
    {
      "y": 0,
      "x": 0
    }
  ],
  "modified_at": null,
  "created_at": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|points|[[BoundaryPoint](#schemaboundarypoint)]|true|none|none|
|modified_at|any|false|read-only|none|
|created_at|any|false|read-only|none|

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
  "customer_external_id": null,
  "custom_site_id": null,
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
      "sync_status": "synced",
      "attributes": [
        {
          "name": "string",
          "value": "string",
          "id": 0,
          "attribute_id": 0
        }
      ],
      "accessories": [
        {
          "model": "string",
          "quantity": null,
          "manufacturer": "string",
          "id": "string",
          "row_index": 0,
          "price": null,
          "labor_hours": 0,
          "description": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "external_id": "string",
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
          "modified_at": null,
          "date": null,
          "entry": "string",
          "creator": {
            "first_name": "string",
            "last_name": "string",
            "user_id": null
          },
          "modifier": {
            "first_name": "string",
            "last_name": "string",
            "user_id": null
          },
          "created_at": null
        }
      ],
      "pdf_urls": null,
      "web_links": [
        {
          "name": "string",
          "url": "string",
          "link_type": 2
        }
      ],
      "photos": [
        "string"
      ],
      "pdfs": [
        {
          "name": "string",
          "url": "string",
          "link_type": 1
        }
      ]
    }
  ],
  "annotations": [
    {
      "font_size": "string",
      "text": "string",
      "category": null,
      "id": "string",
      "stroke_width": "string",
      "coordinates": null,
      "stroke_color": "string",
      "fill": null,
      "size": "string",
      "location": null,
      "end_point": null,
      "opacity": 1,
      "start_point": null
    }
  ],
  "boundaries": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "points": [
        {
          "y": 0,
          "x": 0
        }
      ],
      "modified_at": null,
      "created_at": null
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
|customer_external_id|any|false|read-only|none|
|custom_site_id|any|false|read-only|none|
|icon_size|integer|true|none|none|
|is_archived|boolean|false|read-only|none|
|unit|any|true|none|none|
|version|integer|false|read-only|none|
|margin_range|number|true|none|none|
|type|any|false|read-only|none|
|floorplan_scale|number|false|none|none|
|preview_image|string|false|read-only|none|
|floorplan_url|string|false|none|none|
|sync_status|any|false|read-only|none|
|creator|integer|false|read-only|none|
|editor|[RelatedUser](#schemarelateduser)|false|read-only|none|
|modifier|integer|false|read-only|none|
|created_at|any|false|read-only|none|
|modified_at|any|false|read-only|none|
|elements|[[SurveyElement](#schemasurveyelement)]|false|none|none|
|annotations|[[SurveyAnnotation](#schemasurveyannotation)]|false|none|none|
|boundaries|[[SurveyBoundary](#schemasurveyboundary)]|false|none|none|
|users|any|false|read-only|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sync_status|synced|
|sync_status|pending|
|sync_status|errored|

<h2 id="tocS_SystemTypeSchema">SystemTypeSchema</h2>
<!-- backwards compatibility -->
<a id="schemasystemtypeschema"></a>
<a id="schema_SystemTypeSchema"></a>
<a id="tocSsystemtypeschema"></a>
<a id="tocssystemtypeschema"></a>

```json
{
  "elements": [
    {
      "abbreviation": "string",
      "category": {
        "name": "string",
        "abbreviation": "string",
        "id": 0
      },
      "icon": null,
      "name": "string",
      "id": 0,
      "sort_order": 0
    }
  ],
  "abbreviation": "string",
  "id": 0,
  "element_color": "string",
  "name": "string",
  "sort": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|elements|[[ElementSchema](#schemaelementschema)]|false|none|none|
|abbreviation|string|true|none|none|
|id|integer|false|read-only|none|
|element_color|string|true|none|none|
|name|string|true|none|none|
|sort|integer|false|none|none|

<h2 id="tocS_UserPreferencesSchema">UserPreferencesSchema</h2>
<!-- backwards compatibility -->
<a id="schemauserpreferencesschema"></a>
<a id="schema_UserPreferencesSchema"></a>
<a id="tocSuserpreferencesschema"></a>
<a id="tocsuserpreferencesschema"></a>

```json
{
  "comment_notification_mentions_only": true,
  "report_2_enabled": true,
  "auto_sync": true,
  "comment_notification_time": "string",
  "timezone": "string",
  "comment_notification_editor_only": true,
  "comment_notification_enabled": true,
  "web_2_enabled": true,
  "comment_notification_daily_batch": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comment_notification_mentions_only|boolean|false|none|none|
|report_2_enabled|boolean|false|none|none|
|auto_sync|boolean|false|none|none|
|comment_notification_time|string|false|none|none|
|timezone|string|false|none|none|
|comment_notification_editor_only|boolean|false|none|none|
|comment_notification_enabled|boolean|false|none|none|
|web_2_enabled|boolean|false|none|none|
|comment_notification_daily_batch|boolean|false|none|none|

