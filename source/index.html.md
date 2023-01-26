---
title: System Surveyor API v2.0.0
language_tabs:
  - shell: cURL
  - python: Python
  - csharp: C#
language_clients:
  - shell: ""
  - python: ""
  - csharp: ""
toc_footers: []
includes: []
search: false
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="system-surveyor-api">System Surveyor API v2.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

How to Use Our REST APIs

System Surveyor's APIs enable bi-directional communication with it's platform. These APIs provide a software layer connecting and optimizing the network to allow your users to create/edit/retrieve sites & surveys, along with all of the associated data.

##Prerequisites

In order to utilize these APIs, you must have an Enterprise account, with a valid plan. Your account administrator must create an `access_token` for you, which is required for each request.

# Authentication

- HTTP Authentication, scheme: bearer Once the account administrator creates your API `access_token` ([link](https://app.systemsurveyor.com/v2/account/#api_management)), you must include that with each request. These tokens are valid for 1 year, and can be revoked at any time by the account administrator. Here is a sample request:

```
curl --location --request GET 'https://openapi.systemsurveyor.com/v3/user' \  
--header 'Authorization: Bearer <<TOKEN>>'
```

<h1 id="system-surveyor-api-resources">Resources</h1>

## Fetches a binary resource and returns it as bytes.

<a id="opIdget_resource"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/resource \
  -H 'Accept: application/octet-stream' \
  -H 'Authorization: Bearer {access-token}'

```

```python
import requests
headers = {
  'Accept': 'application/octet-stream',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/v3/resource', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    /// Make a dummy request
    public async Task MakeGetRequest()
    {
      string url = "/v3/resource";
      var result = await GetAsync(url);
    }

    /// Performs a GET Request
    public async Task GetAsync(string url)
    {
        //Start the request
        HttpResponseMessage response = await Client.GetAsync(url);

        //Validate result
        response.EnsureSuccessStatusCode();

    }
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`GET /v3/resource`

Resource path is a relative URL to the binary resource in EFS, passed in a `path` query parameter.

Example path: `2022/08/05/207e7214-6792-4288-8820-438b1f3233be.png`

<h3 id="fetches-a-binary-resource-and-returns-it-as-bytes.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|path|path|string|true|Relative URL of the resource|

> Example responses

> 200 Response

<h3 id="fetches-a-binary-resource-and-returns-it-as-bytes.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A binary resource file|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
jwt
</aside>

## Sets an image to a survey element.

<a id="opIdadd_survey_element_resource"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/survey_element/{survey_element_id}/resource \
  -H 'Content-Type: application/pdf' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/pdf',
  'Accept': 'application/json'
}

r = requests.post('/v3/survey_element/{survey_element_id}/resource', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    /// Make a dummy request
    public async Task MakePostRequest()
    {
      string url = "/v3/survey_element/{survey_element_id}/resource";
      
      
      await PostAsync(null, url);
      
    }

    /// Performs a POST Request
    public async Task PostAsync(undefined content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute POST request
        HttpResponseMessage response = await Client.PostAsync(url, jsonContent);
    }
    
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(undefined content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`POST /v3/survey_element/{survey_element_id}/resource`

> Body parameter

<h3 id="sets-an-image-to-a-survey-element.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|survey_element_id|path|undefined|true|The external id of the surveyelement|
|body|body|string(binary)|false|none|

> Example responses

> 200 Response

```json
{
  "data": {
    "resource_url": "2022/11/01/39dace0d-7aa3-47c7-9bff-9c87fbe2c00b.png"
  }
}
```

<h3 id="sets-an-image-to-a-survey-element.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The path to the uploaded file|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|The specified resource was not found|None|

<h3 id="sets-an-image-to-a-survey-element.-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|false|none|none|
|»» resource_url|string|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

<h1 id="system-surveyor-api-folders">Folders</h1>

## Creates a new site/survey folder or updates an existing one if found.

<a id="opIdcreate_or_update_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /v3/folder/{folder_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/v3/folder/{folder_id}', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    /// Make a dummy request
    public async Task MakePutRequest()
    {
      int id = 1;
      string url = "/v3/folder/{folder_id}";

      
      string json = @"{
  ""site_external_id"": ""string"",
  ""label"": ""string"",
  ""name"": ""string"",
  ""team_id"": 0
}";
      FolderSchema content = JsonConvert.DeserializeObject(json);
      var result = await PutAsync(id, content, url);
      
          
    }

    /// Performs a PUT Request
    public async Task PutAsync(int id, FolderSchema content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute PUT request
        HttpResponseMessage response = await Client.PutAsync(url + $"/{id}", jsonContent);

        //Return response
        return await DeserializeObject(response);
    }
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(FolderSchema content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`PUT /v3/folder/{folder_id}`

To create/update a site folder, pass a value for `team_id` field in the request payload, to create/update a survey folder
pass a value for `site_id` field.

> Body parameter

```json
{
  "site_external_id": "string",
  "label": "string",
  "name": "string",
  "team_id": 0
}
```

<h3 id="creates-a-new-site/survey-folder-or-updates-an-existing-one-if-found.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|folder_id|path|string|true|Folder ID|
|body|body|[FolderSchema](#schemafolderschema)|true|none|
|» site_external_id|body|string|false|none|
|» label|body|string|false|none|
|» name|body|string|true|none|
|» id|body|string|false|none|
|» team_id|body|integer|false|none|
|» site_id|body|integer|false|none|

> Example responses

> 200 Response

```json
{
  "label": "string",
  "name": "string",
  "id": "string",
  "team_id": 0,
  "site_id": 0
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
None, None, None, None
</aside>

## Soft deletes a site folder or a survey folder.

<a id="opIddelete_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/folder/{folder_id}

```

```python
import requests

r = requests.delete('/v3/folder/{folder_id}')

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    /// Make a dummy request
    public async Task MakeDeleteRequest()
    {
      int id = 1;
      string url = "/v3/folder/{folder_id}";

      await DeleteAsync(id, url);
    }

    /// Performs a DELETE Request
    public async Task DeleteAsync(int id, string url)
    {
        //Execute DELETE request
        HttpResponseMessage response = await Client.DeleteAsync(url + $"/{id}");

        //Return response
        await DeserializeObject(response);
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
None, None, None, None
</aside>

## Creates a new folder that can hold sites

<a id="opIdcreate_site_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/site_folder \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/v3/site_folder', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    /// Make a dummy request
    public async Task MakePostRequest()
    {
      string url = "/v3/site_folder";
      
      
      await PostAsync(null, url);
      
    }

    /// Performs a POST Request
    public async Task PostAsync(undefined content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute POST request
        HttpResponseMessage response = await Client.PostAsync(url, jsonContent);
    }
    
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(undefined content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
  "label": "string",
  "name": "string",
  "id": "string",
  "team_id": 0,
  "site_id": 0
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
None, None, None, None
</aside>

## Update all fields of a folder

<a id="opIdupdate_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/site_folder/{folder_external_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/v3/site_folder/{folder_external_id}', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
  "label": "string",
  "name": "string",
  "id": "string",
  "team_id": 0,
  "site_id": 0
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
None, None, None, None
</aside>

## Allows creating folders inside a site, which can store and organize surveys

<a id="opIdcreate_survey_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/{site_id}/folder \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/v3/{site_id}/folder', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    /// Make a dummy request
    public async Task MakePostRequest()
    {
      string url = "/v3/{site_id}/folder";
      
      
      await PostAsync(null, url);
      
    }

    /// Performs a POST Request
    public async Task PostAsync(undefined content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute POST request
        HttpResponseMessage response = await Client.PostAsync(url, jsonContent);
    }
    
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(undefined content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
  "label": "string",
  "name": "string",
  "id": "string",
  "team_id": 0,
  "site_id": 0
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
None, None, None, None
</aside>

## Deletes a survey folder in a site.

<a id="opIddelete_survey_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/survey_folder/{folder_id}

```

```python
import requests

r = requests.delete('/v3/survey_folder/{folder_id}')

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    /// Make a dummy request
    public async Task MakeDeleteRequest()
    {
      int id = 1;
      string url = "/v3/survey_folder/{folder_id}";

      await DeleteAsync(id, url);
    }

    /// Performs a DELETE Request
    public async Task DeleteAsync(int id, string url)
    {
        //Execute DELETE request
        HttpResponseMessage response = await Client.DeleteAsync(url + $"/{id}");

        //Return response
        await DeserializeObject(response);
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
None, None, None, None
</aside>

## Soft deletes a folder that can contain sites.

<a id="opIddelete_site_folder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/site_folder/{folder_id}

```

```python
import requests

r = requests.delete('/v3/site_folder/{folder_id}')

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    /// Make a dummy request
    public async Task MakeDeleteRequest()
    {
      int id = 1;
      string url = "/v3/site_folder/{folder_id}";

      await DeleteAsync(id, url);
    }

    /// Performs a DELETE Request
    public async Task DeleteAsync(int id, string url)
    {
        //Execute DELETE request
        HttpResponseMessage response = await Client.DeleteAsync(url + $"/{id}");

        //Return response
        await DeserializeObject(response);
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
None, None, None, None
</aside>

<h1 id="system-surveyor-api-reports">Reports</h1>

## Queues a message for creating reports for sites or surveys

<a id="opIdcreate_report"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v3/report \
  -H 'Content-Type: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.post('/v3/report', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    /// Make a dummy request
    public async Task MakePostRequest()
    {
      string url = "/v3/report";
      
      string json = @"{
  ""name"": ""string"",
  ""paper_size"": ""string"",
  ""filters"": [
    {}
  ],
  ""is_excel"": false,
  ""is_site_report"": false,
  ""survey_ids"": [
    ""string""
  ],
  ""options"": [
    {
      ""value"": true,
      ""template_name"": ""string"",
      ""inputs"": [
        {
          ""field_id"": ""string"",
          ""value"": ""string""
        }
      ],
      ""scope"": ""template"",
      ""id"": ""string""
    }
  ],
  ""custom_data"": {},
  ""output"": ""pdf"",
  ""report_id"": ""5ed7905a-4735-4cf7-b1ab-521e066fb971"",
  ""site_id"": ""string""
}";
      SurveyReportRequestSchema content = JsonConvert.DeserializeObject(json);
      await PostAsync(content, url);
      
      
    }

    /// Performs a POST Request
    public async Task PostAsync(SurveyReportRequestSchema content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute POST request
        HttpResponseMessage response = await Client.PostAsync(url, jsonContent);
    }
    
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(SurveyReportRequestSchema content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`POST /v3/report`

Reports are created by an external PHP service by picking up messages from the queue.

> Body parameter

```json
{
  "name": "string",
  "paper_size": "string",
  "filters": [
    {}
  ],
  "is_excel": false,
  "is_site_report": false,
  "survey_ids": [
    "string"
  ],
  "options": [
    {
      "value": true,
      "template_name": "string",
      "inputs": [
        {
          "field_id": "string",
          "value": "string"
        }
      ],
      "scope": "template",
      "id": "string"
    }
  ],
  "custom_data": {},
  "output": "pdf",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "site_id": "string"
}
```

<h3 id="queues-a-message-for-creating-reports-for-sites-or-surveys-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SurveyReportRequestSchema](#schemasurveyreportrequestschema)|true|none|
|» name|body|string|true|none|
|» paper_size|body|string|false|none|
|» filters|body|[object]|false|none|
|» is_excel|body|boolean|false|none|
|» is_site_report|body|boolean|false|none|
|» survey_ids|body|[string]|false|none|
|» options|body|[[SurveyOptions](#schemasurveyoptions)]|false|none|
|»» value|body|boolean|true|none|
|»» template_name|body|string|false|none|
|»» inputs|body|[[SurveyFields](#schemasurveyfields)]|false|none|
|»»» field_id|body|string|true|none|
|»»» value|body|string|true|none|
|»» scope|body|string|true|none|
|»» id|body|string|true|none|
|» custom_data|body|object|false|none|
|» output|body|string|true|none|
|» report_id|body|string(uuid)|true|none|
|» site_id|body|string|true|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» scope|template|
|»» scope|model|
|»» scope|content|
|» output|pdf|
|» output|html|
|» output|xls|

<h3 id="queues-a-message-for-creating-reports-for-sites-or-surveys-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Report scheduled successfully|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

<h1 id="system-surveyor-api-sites">Sites</h1>

## Get site information

<a id="opIdget_site"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/site/{site_id} \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    /// Make a dummy request
    public async Task MakeGetRequest()
    {
      string url = "/v3/site/{site_id}";
      var result = await GetAsync(url);
    }

    /// Performs a GET Request
    public async Task GetAsync(string url)
    {
        //Start the request
        HttpResponseMessage response = await Client.GetAsync(url);

        //Validate result
        response.EnsureSuccessStatusCode();

    }
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
  "team_id": 0,
  "name": "string",
  "label": "string",
  "survey_count": 0,
  "city": "string",
  "state": "string",
  "street": "string",
  "zip_code": "string",
  "is_active": true,
  "version": 0,
  "reference_id": "string",
  "tags": [
    "string"
  ],
  "creator": {
    "user_id": 0,
    "first_name": "string",
    "last_name": "string"
  },
  "modifier": {
    "user_id": 0,
    "first_name": "string",
    "last_name": "string"
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
|» id|string|false|none|none|
|» team_id|integer|false|none|none|
|» name|string|false|none|none|
|» label|string|false|none|none|
|» survey_count|integer|false|none|none|
|» city|string|false|none|none|
|» state|string|false|none|none|
|» street|string|false|none|none|
|» zip_code|string|false|none|none|
|» is_active|boolean|false|none|none|
|» version|integer|false|none|none|
|» reference_id|string|false|none|none|
|» tags|[string]|false|none|none|
|» creator|object|false|none|none|
|»» user_id|integer|false|none|none|
|»» first_name|string|false|none|none|
|»» last_name|string|false|none|none|
|» modifier|object|false|none|none|
|»» user_id|integer|false|none|none|
|»» first_name|string|false|none|none|
|»» last_name|string|false|none|none|
|» created_at|integer|false|none|none|
|» modified_at|integer|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

## Creates a new site with a specific `external_id` or updates the site if it already exists

<a id="opIdcreate_or_update_site"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /v3/site/{site_id} \
  -H 'Content-Type: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.put('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    /// Make a dummy request
    public async Task MakePutRequest()
    {
      int id = 1;
      string url = "/v3/site/{site_id}";

      
      string json = @"{
  ""street"": ""string"",
  ""label"": ""string"",
  ""name"": ""string"",
  ""state"": ""string"",
  ""city"": ""string"",
  ""zip_code"": ""string"",
  ""tags"": [
    ""string""
  ],
  ""reference_id"": ""string"",
  ""team_id"": 0,
  ""is_archived"": null,
  ""site_id"": ""string""
}";
      SiteSchema content = JsonConvert.DeserializeObject(json);
      var result = await PutAsync(id, content, url);
      
          
    }

    /// Performs a PUT Request
    public async Task PutAsync(int id, SiteSchema content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute PUT request
        HttpResponseMessage response = await Client.PutAsync(url + $"/{id}", jsonContent);

        //Return response
        return await DeserializeObject(response);
    }
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(SiteSchema content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`PUT /v3/site/{site_id}`

Pass a folder external ID in a `folder_external_id` field in the payload to create the site inside that folder.

> Body parameter

```json
{
  "street": "string",
  "label": "string",
  "name": "string",
  "state": "string",
  "city": "string",
  "zip_code": "string",
  "tags": [
    "string"
  ],
  "reference_id": "string",
  "team_id": 0,
  "is_archived": null,
  "site_id": "string"
}
```

<h3 id="creates-a-new-site-with-a-specific-`external_id`-or-updates-the-site-if-it-already-exists-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|body|body|[SiteSchema](#schemasiteschema)|true|none|
|» street|body|string|false|none|
|» label|body|string|false|none|
|» name|body|string|true|none|
|» state|body|string|false|none|
|» city|body|string|false|none|
|» created_at|body|null|false|none|
|» zip_code|body|string|false|none|
|» tags|body|[string]|false|none|
|» legacy_site_id|body|integer|false|none|
|» modified_at|body|null|false|none|
|» reference_id|body|string|false|none|
|» version|body|integer|false|none|
|» team_id|body|integer|true|none|
|» creator|body|[UserResponse](#schemauserresponse)|false|none|
|»» user_id|body|integer|true|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|» is_archived|body|any|false|none|
|» site_id|body|string|false|none|
|» modifier|body|[UserResponse](#schemauserresponse)|false|none|
|»» user_id|body|integer|true|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|

<h3 id="creates-a-new-site-with-a-specific-`external_id`-or-updates-the-site-if-it-already-exists-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful update|None|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful create|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

## Update specific fields of a site

<a id="opIdpatch_site"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/site/{site_id} \
  -H 'Content-Type: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.patch('/v3/site/{site_id}', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`PATCH /v3/site/{site_id}`

> Body parameter

```json
{
  "street": "string",
  "label": "string",
  "name": "string",
  "state": "string",
  "city": "string",
  "zip_code": "string",
  "tags": [
    "string"
  ],
  "reference_id": "string",
  "team_id": 0,
  "is_archived": null,
  "site_id": "string"
}
```

<h3 id="update-specific-fields-of-a-site-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|site_id|path|string|true|Site ID|
|body|body|[SiteSchema](#schemasiteschema)|true|none|
|» street|body|string|false|none|
|» label|body|string|false|none|
|» name|body|string|true|none|
|» state|body|string|false|none|
|» city|body|string|false|none|
|» created_at|body|null|false|none|
|» zip_code|body|string|false|none|
|» tags|body|[string]|false|none|
|» legacy_site_id|body|integer|false|none|
|» modified_at|body|null|false|none|
|» reference_id|body|string|false|none|
|» version|body|integer|false|none|
|» team_id|body|integer|true|none|
|» creator|body|[UserResponse](#schemauserresponse)|false|none|
|»» user_id|body|integer|true|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
|» is_archived|body|any|false|none|
|» site_id|body|string|false|none|
|» modifier|body|[UserResponse](#schemauserresponse)|false|none|
|»» user_id|body|integer|true|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|

<h3 id="update-specific-fields-of-a-site-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful update|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid request sent to endpoint|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Invalid permissions to perform operation|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

## Hard deletes a site and all related objects.

<a id="opIddelete_site"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/site/{site_id}

```

```python
import requests

r = requests.delete('/v3/site/{site_id}')

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    /// Make a dummy request
    public async Task MakeDeleteRequest()
    {
      int id = 1;
      string url = "/v3/site/{site_id}";

      await DeleteAsync(id, url);
    }

    /// Performs a DELETE Request
    public async Task DeleteAsync(int id, string url)
    {
        //Execute DELETE request
        HttpResponseMessage response = await Client.DeleteAsync(url + $"/{id}");

        //Return response
        await DeserializeObject(response);
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
None, None, None, None
</aside>

## Returns all archived/unarchived sites and folders across all teams of a user.

<a id="opIdget_user_sites_and_folders"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/sites \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/v3/sites', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    /// Make a dummy request
    public async Task MakeGetRequest()
    {
      string url = "/v3/sites";
      var result = await GetAsync(url);
    }

    /// Performs a GET Request
    public async Task GetAsync(string url)
    {
        //Start the request
        HttpResponseMessage response = await Client.GetAsync(url);

        //Validate result
        response.EnsureSuccessStatusCode();

    }
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`GET /v3/sites`

Explanation of usage of filters:

Filtered by favorites:
  - All sites that are in workbench but not in a folder
  - All folders that have a site under them that is in the workbench
  - Don’t return sites that are in workbench but also in a folder

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
      "modified_at": 1644374426,
      "owner": {
        "user_id": 12390,
        "first_name": "John",
        "last_name": "Doe"
      },
      "modifier": {
        "user_id": 12390,
        "first_name": "John",
        "last_name": "Doe"
      },
      "team": {
        "team_id": 1049,
        "name": "string"
      },
      "type": "site",
      "version": 45479945,
      "favorite_timestamp": 12034903409,
      "has_favorite_sites": true
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
|»» modified_at|integer|false|none|Datetime of the most recently modified survey in the site. If the site has no surveys, falls back to the<br>site's own `modified_at` datetime.|
|»» owner|object|false|none|none|
|»»» user_id|integer|false|none|none|
|»»» first_name|string|false|none|none|
|»»» last_name|string|false|none|none|
|»» modifier|object|false|none|none|
|»»» user_id|integer|false|none|none|
|»»» first_name|string|false|none|none|
|»»» last_name|string|false|none|none|
|»» team|object|false|none|none|
|»»» team_id|integer|false|none|none|
|»»» name|string|false|none|none|
|»» type|string|false|none|If the result item is a site or a folder|
|»» version|integer|false|none|none|
|»» favorite_timestamp|integer|false|none|Timestamp of when the site was added to favorites|
|»» has_favorite_sites|boolean|false|none|Indicates if a folder has sites that are in the user's workbench|

#### Enumerated Values

|Property|Value|
|---|---|
|type|site|
|type|folder|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

## Allows for batch deleting of sites (and all related data).

<a id="opIddelete_sites"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/sites \
  -H 'Content-Type: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json'
}

r = requests.delete('/v3/sites', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    /// Make a dummy request
    public async Task MakeDeleteRequest()
    {
      int id = 1;
      string url = "/v3/sites";

      await DeleteAsync(id, url);
    }

    /// Performs a DELETE Request
    public async Task DeleteAsync(int id, string url)
    {
        //Execute DELETE request
        HttpResponseMessage response = await Client.DeleteAsync(url + $"/{id}");

        //Return response
        await DeserializeObject(response);
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
None, None, None, None
</aside>

<h1 id="system-surveyor-api-surveys">Surveys</h1>

## Returns all surveys and folders for a specific site. These are shown in the site overview page.

<a id="opIdget_site_surveys_and_folders"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/site/{site_id}/surveys \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/v3/site/{site_id}/surveys', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    /// Make a dummy request
    public async Task MakeGetRequest()
    {
      string url = "/v3/site/{site_id}/surveys";
      var result = await GetAsync(url);
    }

    /// Performs a GET Request
    public async Task GetAsync(string url)
    {
        //Start the request
        HttpResponseMessage response = await Client.GetAsync(url);

        //Validate result
        response.EnsureSuccessStatusCode();

    }
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
|sort|editor_id|
|sort|editor_first_name|
|sort|editor_last_name|
|sort|comments_count|
|sort|elements_count|
|sort|is_folder|
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
      "title": "My survey",
      "label": "TGS-123",
      "is_folder": false,
      "preview_image": "string",
      "elements_count": 90,
      "survey_count": 34,
      "is_archived": false
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
|»» id|string|false|none|none|
|»» title|string|false|none|none|
|»» label|string|false|none|none|
|»» is_folder|boolean|false|none|none|
|»» preview_image|string|false|none|URL to the survey's preview image|
|»» elements_count|integer|false|none|Element count for survey|
|»» survey_count|integer|false|none|Survey count for folder|
|»» is_archived|boolean|false|none|If the survey is archived or not|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

## Allows creating a new survey with a unique identifier generated by the client, or updates the existing survey with that identifier if it exists.

<a id="opIdcreate_or_update_survey"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /v3/site/{site_id}/survey/{survey_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/v3/site/{site_id}/survey/{survey_id}', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    /// Make a dummy request
    public async Task MakePutRequest()
    {
      int id = 1;
      string url = "/v3/site/{site_id}/survey/{survey_id}";

      
      string json = @"{
  ""title"": ""string"",
  ""label"": ""string"",
  ""reference_id"": ""string"",
  ""description"": ""string"",
  ""summary"": ""string"",
  ""location"": ""string"",
  ""status"": null,
  ""icon_size"": 0,
  ""unit"": null,
  ""margin_range"": 0,
  ""floorplan_scale"": 0,
  ""elements"": [
    {
      ""id"": ""string"",
      ""name"": ""string"",
      ""element_id"": 0,
      ""element_index"": 0,
      ""element_profile_id"": 0,
      ""systemtype_id"": 0,
      ""variant"": null,
      ""z_order"": 0,
      ""position"": null,
      ""photo_urls"": [
        ""string""
      ],
      ""pdf_urls"": [
        {}
      ],
      ""attributes"": [
        {
          ""attribute_id"": 0,
          ""value"": ""string"",
          ""name"": ""string""
        }
      ],
      ""accessories"": [
        {
          ""quantity"": null,
          ""model"": ""string"",
          ""description"": ""string"",
          ""labor_hours"": 0,
          ""manufacturer"": ""string"",
          ""price"": null,
          ""row_index"": 0
        }
      ],
      ""children"": [
        {}
      ],
      ""cables"": [
        {
          ""id"": ""string"",
          ""a_side"": null,
          ""type"": ""string"",
          ""z_side"": null
        }
      ],
      ""connections"": {
        ""start"": null,
        ""end"": null
      },
      ""activity_log"": [
        {
          ""entry"": ""string""
        }
      ]
    }
  ],
  ""annotations"": [
    {
      ""start_point"": null,
      ""end_point"": null,
      ""category"": null,
      ""text"": ""string"",
      ""stroke_width"": ""string"",
      ""stroke_color"": ""string"",
      ""location"": null,
      ""size"": ""string"",
      ""font_size"": ""string""
    }
  ]
}";
      SurveySchema content = JsonConvert.DeserializeObject(json);
      var result = await PutAsync(id, content, url);
      
          
    }

    /// Performs a PUT Request
    public async Task PutAsync(int id, SurveySchema content, string url)
    {
        //Serialize Object
        StringContent jsonContent = SerializeObject(content);

        //Execute PUT request
        HttpResponseMessage response = await Client.PutAsync(url + $"/{id}", jsonContent);

        //Return response
        return await DeserializeObject(response);
    }
    
    
    /// Serialize an object to Json
    private StringContent SerializeObject(SurveySchema content)
    {
        //Serialize Object
        string jsonObject = JsonConvert.SerializeObject(content);

        //Create Json UTF8 String Content
        return new StringContent(jsonObject, Encoding.UTF8, "application/json");
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
      "photo_urls": [
        "string"
      ],
      "pdf_urls": [
        {}
      ],
      "attributes": [
        {
          "attribute_id": 0,
          "value": "string",
          "name": "string"
        }
      ],
      "accessories": [
        {
          "quantity": null,
          "model": "string",
          "description": "string",
          "labor_hours": 0,
          "manufacturer": "string",
          "price": null,
          "row_index": 0
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "id": "string",
          "a_side": null,
          "type": "string",
          "z_side": null
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "entry": "string"
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "end_point": null,
      "category": null,
      "text": "string",
      "stroke_width": "string",
      "stroke_color": "string",
      "location": null,
      "size": "string",
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
|»» user_id|body|any|false|none|
|»» first_name|body|string|false|none|
|»» last_name|body|string|false|none|
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
|»» pdf_urls|body|[object]|false|none|
|»» attributes|body|[[SurveyAttribute](#schemasurveyattribute)]|false|none|
|»»» attribute_id|body|integer|true|none|
|»»» id|body|integer|false|none|
|»»» value|body|string|true|none|
|»»» name|body|string|true|none|
|»» accessories|body|[[SurveyElementAccessory](#schemasurveyelementaccessory)]|false|none|
|»»» quantity|body|any|false|none|
|»»» model|body|string|true|none|
|»»» description|body|string|false|none|
|»»» labor_hours|body|number|false|none|
|»»» manufacturer|body|string|true|none|
|»»» price|body|any|false|none|
|»»» row_index|body|integer|true|none|
|»»» id|body|string|false|none|
|»» children|body|[[SurveyElement](#schemasurveyelement)]|false|none|
|»» cables|body|[[CablePath](#schemacablepath)]|false|none|
|»»» id|body|string|true|none|
|»»» a_side|body|any|true|none|
|»»» type|body|string|false|none|
|»»» z_side|body|any|true|none|
|»» connections|body|[PathConnection](#schemapathconnection)|false|none|
|»»» start|body|any|false|none|
|»»» end|body|any|false|none|
|»» activity_log|body|[[SurveyElementActivityLog](#schemasurveyelementactivitylog)]|false|none|
|»»» date|body|any|false|none|
|»»» id|body|string|false|none|
|»»» entry|body|string|false|none|
|» annotations|body|[[SurveyAnnotation](#schemasurveyannotation)]|false|none|
|»» start_point|body|any|false|none|
|»» end_point|body|any|false|none|
|»» category|body|any|true|none|
|»» text|body|string|false|none|
|»» stroke_width|body|string|true|none|
|»» stroke_color|body|string|true|none|
|»» location|body|any|true|none|
|»» size|body|string|false|none|
|»» id|body|string|false|none|
|»» font_size|body|string|false|none|
|» users|body|any|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» sync_status|synced|
|» sync_status|pending|
|» sync_status|errored|

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
    "user_id": null,
    "first_name": "string",
    "last_name": "string"
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
      "pdf_urls": [
        {}
      ],
      "attributes": [
        {
          "attribute_id": 0,
          "id": 0,
          "value": "string",
          "name": "string"
        }
      ],
      "accessories": [
        {
          "quantity": null,
          "model": "string",
          "description": "string",
          "labor_hours": 0,
          "manufacturer": "string",
          "price": null,
          "row_index": 0,
          "id": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "id": "string",
          "a_side": null,
          "type": "string",
          "z_side": null
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "date": null,
          "id": "string",
          "entry": "string"
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "end_point": null,
      "category": null,
      "text": "string",
      "stroke_width": "string",
      "stroke_color": "string",
      "location": null,
      "size": "string",
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
None, None, None, None
</aside>

## Deletes a survey and all its related objects

<a id="opIddelete_survey"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /v3/survey/{survey_id}

```

```python
import requests

r = requests.delete('/v3/survey/{survey_id}')

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    /// Make a dummy request
    public async Task MakeDeleteRequest()
    {
      int id = 1;
      string url = "/v3/survey/{survey_id}";

      await DeleteAsync(id, url);
    }

    /// Performs a DELETE Request
    public async Task DeleteAsync(int id, string url)
    {
        //Execute DELETE request
        HttpResponseMessage response = await Client.DeleteAsync(url + $"/{id}");

        //Return response
        await DeserializeObject(response);
    }
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

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
None, None, None, None
</aside>

<h1 id="system-surveyor-api-teams">Teams</h1>

## Returns all the teams the current user is a member of

<a id="opIdget_user_teams"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/teams \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/v3/teams', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    /// Make a dummy request
    public async Task MakeGetRequest()
    {
      string url = "/v3/teams";
      var result = await GetAsync(url);
    }

    /// Performs a GET Request
    public async Task GetAsync(string url)
    {
        //Start the request
        HttpResponseMessage response = await Client.GetAsync(url);

        //Validate result
        response.EnsureSuccessStatusCode();

    }
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`GET /v3/teams`

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
None, None, None, None
</aside>

<h1 id="system-surveyor-api-users">Users</h1>

## Get data for the current authenticated user

<a id="opIdget_current_user_data"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v3/user \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/v3/user', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    /// Make a dummy request
    public async Task MakeGetRequest()
    {
      string url = "/v3/user";
      var result = await GetAsync(url);
    }

    /// Performs a GET Request
    public async Task GetAsync(string url)
    {
        //Start the request
        HttpResponseMessage response = await Client.GetAsync(url);

        //Validate result
        response.EnsureSuccessStatusCode();

    }
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`GET /v3/user`

This includes accounts and teams that the current user belongs to, either as a team member or a guest user.

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
  "country": "string",
  "state": "string",
  "last_login": 0,
  "avatar_url": "string",
  "is_complete_setup": true,
  "created_at": 0,
  "teams": [
    {
      "id": 112,
      "name": "John's Team",
      "account_id": 995,
      "role": "team_member",
      "unit": "metric",
      "labor_rate": null,
      "budget_status": 0,
      "margin_range": null
    }
  ],
  "accounts": [
    {
      "id": 450495,
      "company": "string",
      "is_trial": true,
      "is_free": true,
      "cancel_requested": true,
      "subscription": {
        "id": 0,
        "quantity": 0,
        "end_date": 0,
        "plan": {
          "id": 0,
          "name": "string",
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

<h3 id="get-data-for-the-current-authenticated-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Access token is missing or invalid|None|

<h3 id="get-data-for-the-current-authenticated-user-responseschema">Response Schema</h3>

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
|» last_login|number|false|none|none|
|» avatar_url|string|false|none|none|
|» is_complete_setup|boolean|false|none|none|
|» created_at|integer|false|none|none|
|» teams|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» name|string|false|none|none|
|»» account_id|integer|false|none|none|
|»» role|string|false|none|none|
|»» unit|string|false|none|none|
|»» labor_rate|float|false|none|none|
|»» budget_status|integer|false|none|none|
|»» margin_range|float|false|none|none|
|» accounts|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» company|string|false|none|none|
|»» is_trial|boolean|false|none|none|
|»» is_free|boolean|false|none|none|
|»» cancel_requested|boolean|false|none|none|
|»» subscription|object|false|none|none|
|»»» id|integer|false|none|none|
|»»» quantity|integer|false|none|none|
|»»» end_date|integer|false|none|none|
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

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
</aside>

## Update user information associated with the linked account

<a id="opIdupdate_user"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /v3/user \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/v3/user', headers = headers)

print(r.json())

```

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

/// <<summary>>
/// Example of Http Client
/// <</summary>>
public class HttpExample
{
    private HttpClient Client { get; set; }

    /// <<summary>>
    /// Setup http client
    /// <</summary>>
    public HttpExample()
    {
      Client = new HttpClient();
    }
    
    
    
    
    
    /// Deserialize object from request response
    private async Task DeserializeObject(HttpResponseMessage response)
    {
        //Read body 
        string responseBody = await response.Content.ReadAsStringAsync();

        //Deserialize Body to object
        var result = JsonConvert.DeserializeObject(responseBody);
    }
}

```

`PATCH /v3/user`

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
  "country": "string",
  "state": "string",
  "last_login": 0,
  "avatar_url": "string",
  "is_complete_setup": true,
  "created_at": 0,
  "teams": [
    {
      "id": 112,
      "name": "John's Team",
      "account_id": 995,
      "role": "team_member",
      "unit": "metric",
      "labor_rate": null,
      "budget_status": 0,
      "margin_range": null
    }
  ],
  "accounts": [
    {
      "id": 450495,
      "company": "string",
      "is_trial": true,
      "is_free": true,
      "cancel_requested": true,
      "features": {
        "comments": true,
        "site_tagging": true,
        "multiple_teams": true,
        "site_access_permissions": true
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
|» last_login|number|false|none|none|
|» avatar_url|string|false|none|none|
|» is_complete_setup|boolean|false|none|none|
|» created_at|integer|false|none|none|
|» teams|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» name|string|false|none|none|
|»» account_id|integer|false|none|none|
|»» role|string|false|none|none|
|»» unit|string|false|none|none|
|»» labor_rate|float|false|none|none|
|»» budget_status|integer|false|none|none|
|»» margin_range|float|false|none|none|
|» accounts|[object]|false|none|none|
|»» id|integer|false|none|none|
|»» company|string|false|none|none|
|»» is_trial|boolean|false|none|none|
|»» is_free|boolean|false|none|none|
|»» cancel_requested|boolean|false|none|none|
|»» features|object|false|none|none|
|»»» comments|boolean|false|none|none|
|»»» site_tagging|boolean|false|none|none|
|»»» multiple_teams|boolean|false|none|none|
|»»» site_access_permissions|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|unit|metric|
|unit|imperial|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, None, None, None
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
  "user_id": 0,
  "first_name": "string",
  "last_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_id|integer|true|none|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|

<h2 id="tocS_SiteSchema">SiteSchema</h2>
<!-- backwards compatibility -->
<a id="schemasiteschema"></a>
<a id="schema_SiteSchema"></a>
<a id="tocSsiteschema"></a>
<a id="tocssiteschema"></a>

```json
{
  "street": "string",
  "label": "string",
  "name": "string",
  "state": "string",
  "city": "string",
  "created_at": null,
  "zip_code": "string",
  "tags": [
    "string"
  ],
  "legacy_site_id": 0,
  "modified_at": null,
  "reference_id": "string",
  "version": 0,
  "team_id": 0,
  "creator": {
    "user_id": 0,
    "first_name": "string",
    "last_name": "string"
  },
  "is_archived": null,
  "site_id": "string",
  "modifier": {
    "user_id": 0,
    "first_name": "string",
    "last_name": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|street|string|false|none|none|
|label|string|false|none|none|
|name|string|true|none|none|
|state|string|false|none|none|
|city|string|false|none|none|
|created_at|null|false|read-only|none|
|zip_code|string|false|none|none|
|tags|[string]|false|none|none|
|legacy_site_id|integer|false|read-only|none|
|modified_at|null|false|read-only|none|
|reference_id|string|false|none|none|
|version|integer|false|read-only|none|
|team_id|integer|true|none|none|
|creator|[UserResponse](#schemauserresponse)|false|read-only|none|
|is_archived|any|false|none|none|
|site_id|string|false|none|none|
|modifier|[UserResponse](#schemauserresponse)|false|read-only|none|

<h2 id="tocS_ShareSiteOrSurveyRequestSchema">ShareSiteOrSurveyRequestSchema</h2>
<!-- backwards compatibility -->
<a id="schemasharesiteorsurveyrequestschema"></a>
<a id="schema_ShareSiteOrSurveyRequestSchema"></a>
<a id="tocSsharesiteorsurveyrequestschema"></a>
<a id="tocssharesiteorsurveyrequestschema"></a>

```json
{
  "message": "string",
  "created_at": null,
  "modified_at": null,
  "expiration_date": null,
  "emails": [
    "user@example.com"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|none|
|created_at|null|false|read-only|none|
|modified_at|null|false|read-only|none|
|expiration_date|any|true|none|none|
|emails|[string]|true|none|none|

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
  "value": true,
  "template_name": "string",
  "inputs": [
    {
      "field_id": "string",
      "value": "string"
    }
  ],
  "scope": "template",
  "id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|boolean|true|none|none|
|template_name|string|false|none|none|
|inputs|[[SurveyFields](#schemasurveyfields)]|false|none|none|
|scope|string|true|none|none|
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
  "name": "string",
  "paper_size": "string",
  "filters": [
    {}
  ],
  "is_excel": false,
  "is_site_report": false,
  "survey_ids": [
    "string"
  ],
  "options": [
    {
      "value": true,
      "template_name": "string",
      "inputs": [
        {
          "field_id": "string",
          "value": "string"
        }
      ],
      "scope": "template",
      "id": "string"
    }
  ],
  "custom_data": {},
  "output": "pdf",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "site_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|paper_size|string|false|none|none|
|filters|[object]|false|none|none|
|is_excel|boolean|false|none|none|
|is_site_report|boolean|false|none|none|
|survey_ids|[string]|false|none|none|
|options|[[SurveyOptions](#schemasurveyoptions)]|false|none|none|
|custom_data|object|false|none|none|
|output|string|true|none|none|
|report_id|string(uuid)|true|none|none|
|site_id|string|true|none|none|

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
  "ids": [
    "string"
  ],
  "name": "string",
  "paper_size": "string",
  "filters": [
    {}
  ],
  "is_excel": false,
  "is_site_report": false,
  "options": [
    {
      "value": true,
      "template_name": "string",
      "inputs": [
        {
          "field_id": "string",
          "value": "string"
        }
      ],
      "scope": "template",
      "id": "string"
    }
  ],
  "custom_data": {},
  "output": "pdf",
  "report_id": "5ed7905a-4735-4cf7-b1ab-521e066fb971",
  "site_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ids|[string]|false|none|none|
|name|string|true|none|none|
|paper_size|string|false|none|none|
|filters|[object]|false|none|none|
|is_excel|boolean|false|none|none|
|is_site_report|boolean|false|none|none|
|options|[[SurveyOptions](#schemasurveyoptions)]|false|none|none|
|custom_data|object|false|none|none|
|output|string|true|none|none|
|report_id|string(uuid)|true|none|none|
|site_id|string|true|none|none|

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
  "description": "string",
  "labor_hours": [
    0
  ],
  "price": [
    0
  ],
  "manufacturer": "",
  "created_at": null,
  "id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|model|string|false|none|none|
|description|string|true|none|none|
|labor_hours|number,null|false|none|none|
|price|number,null|false|none|none|
|manufacturer|string|false|none|none|
|created_at|any|false|read-only|none|
|id|integer|false|read-only|none|

<h2 id="tocS_Attribute">Attribute</h2>
<!-- backwards compatibility -->
<a id="schemaattribute"></a>
<a id="schema_Attribute"></a>
<a id="tocSattribute"></a>
<a id="tocsattribute"></a>

```json
{
  "attribute_id": 0,
  "value": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|attribute_id|integer|true|none|none|
|value|string|true|none|none|

<h2 id="tocS_Link">Link</h2>
<!-- backwards compatibility -->
<a id="schemalink"></a>
<a id="schema_Link"></a>
<a id="tocSlink"></a>
<a id="tocslink"></a>

```json
{
  "url": "string",
  "link_type": 0,
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|url|string(url)|true|none|none|
|link_type|integer|true|none|none|
|name|string|true|none|none|

<h2 id="tocS_SubElement">SubElement</h2>
<!-- backwards compatibility -->
<a id="schemasubelement"></a>
<a id="schema_SubElement"></a>
<a id="tocSsubelement"></a>
<a id="tocssubelement"></a>

```json
{
  "element_id": "string",
  "systemtype_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|element_id|string|true|none|none|
|systemtype_id|string|true|none|none|

<h2 id="tocS_EPContent">EPContent</h2>
<!-- backwards compatibility -->
<a id="schemaepcontent"></a>
<a id="schema_EPContent"></a>
<a id="tocSepcontent"></a>
<a id="tocsepcontent"></a>

```json
{
  "attribute": [],
  "pdf_url": [],
  "child": []
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|attribute|[[Attribute](#schemaattribute)]|false|none|none|
|pdf_url|[[Link](#schemalink)]|false|none|none|
|child|[[SubElement](#schemasubelement)]|false|none|none|

<h2 id="tocS_ElementProfileSchema">ElementProfileSchema</h2>
<!-- backwards compatibility -->
<a id="schemaelementprofileschema"></a>
<a id="schema_ElementProfileSchema"></a>
<a id="tocSelementprofileschema"></a>
<a id="tocselementprofileschema"></a>

```json
{
  "name": "string",
  "is_default": true,
  "accessories": [
    {
      "model": "",
      "description": "string",
      "labor_hours": [
        0
      ],
      "price": [
        0
      ],
      "manufacturer": "",
      "created_at": null,
      "id": 0
    }
  ],
  "content": {
    "attribute": [],
    "pdf_url": [],
    "child": []
  },
  "created_at": null,
  "modified_at": null,
  "team_id": 0,
  "created_by": 0,
  "sort": 0,
  "element_id": 0,
  "id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|is_default|boolean|false|none|none|
|accessories|[[EPAccessory](#schemaepaccessory)]|false|none|none|
|content|[EPContent](#schemaepcontent)|true|none|none|
|created_at|any|false|read-only|none|
|modified_at|any|false|read-only|none|
|team_id|integer|true|none|none|
|created_by|integer|false|read-only|none|
|sort|integer|false|none|none|
|element_id|integer|true|none|none|
|id|integer|false|read-only|none|

<h2 id="tocS_FolderSchema">FolderSchema</h2>
<!-- backwards compatibility -->
<a id="schemafolderschema"></a>
<a id="schema_FolderSchema"></a>
<a id="tocSfolderschema"></a>
<a id="tocsfolderschema"></a>

```json
{
  "site_external_id": "string",
  "label": "string",
  "name": "string",
  "id": "string",
  "team_id": 0,
  "site_id": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|site_external_id|string|false|write-only|none|
|label|string|false|none|none|
|name|string|true|none|none|
|id|string|false|read-only|none|
|team_id|integer|false|none|none|
|site_id|integer|false|read-only|none|

<h2 id="tocS_RelatedUser">RelatedUser</h2>
<!-- backwards compatibility -->
<a id="schemarelateduser"></a>
<a id="schema_RelatedUser"></a>
<a id="tocSrelateduser"></a>
<a id="tocsrelateduser"></a>

```json
{
  "user_id": null,
  "first_name": "string",
  "last_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_id|any|false|none|none|
|first_name|string|false|none|none|
|last_name|string|false|none|none|

<h2 id="tocS_SurveyAttribute">SurveyAttribute</h2>
<!-- backwards compatibility -->
<a id="schemasurveyattribute"></a>
<a id="schema_SurveyAttribute"></a>
<a id="tocSsurveyattribute"></a>
<a id="tocssurveyattribute"></a>

```json
{
  "attribute_id": 0,
  "id": 0,
  "value": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|attribute_id|integer|true|none|none|
|id|integer|false|read-only|none|
|value|string|true|none|none|
|name|string|true|none|none|

<h2 id="tocS_SurveyElementAccessory">SurveyElementAccessory</h2>
<!-- backwards compatibility -->
<a id="schemasurveyelementaccessory"></a>
<a id="schema_SurveyElementAccessory"></a>
<a id="tocSsurveyelementaccessory"></a>
<a id="tocssurveyelementaccessory"></a>

```json
{
  "quantity": null,
  "model": "string",
  "description": "string",
  "labor_hours": 0,
  "manufacturer": "string",
  "price": null,
  "row_index": 0,
  "id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|quantity|any|false|none|none|
|model|string|true|none|none|
|description|string|false|none|none|
|labor_hours|number|false|none|none|
|manufacturer|string|true|none|none|
|price|any|false|none|none|
|row_index|integer|true|none|none|
|id|string|false|read-only|none|

<h2 id="tocS_CablePath">CablePath</h2>
<!-- backwards compatibility -->
<a id="schemacablepath"></a>
<a id="schema_CablePath"></a>
<a id="tocScablepath"></a>
<a id="tocscablepath"></a>

```json
{
  "id": "string",
  "a_side": null,
  "type": "string",
  "z_side": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|none|
|a_side|any|true|none|none|
|type|string|false|none|none|
|z_side|any|true|none|none|

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
  "date": null,
  "id": "string",
  "entry": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|any|false|read-only|none|
|id|string|false|read-only|none|
|entry|string|false|none|none|

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
  "pdf_urls": [
    {}
  ],
  "attributes": [
    {
      "attribute_id": 0,
      "id": 0,
      "value": "string",
      "name": "string"
    }
  ],
  "accessories": [
    {
      "quantity": null,
      "model": "string",
      "description": "string",
      "labor_hours": 0,
      "manufacturer": "string",
      "price": null,
      "row_index": 0,
      "id": "string"
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
      "pdf_urls": [
        {}
      ],
      "attributes": [
        {
          "attribute_id": 0,
          "id": 0,
          "value": "string",
          "name": "string"
        }
      ],
      "accessories": [
        {
          "quantity": null,
          "model": "string",
          "description": "string",
          "labor_hours": 0,
          "manufacturer": "string",
          "price": null,
          "row_index": 0,
          "id": "string"
        }
      ],
      "children": [],
      "cables": [
        {
          "id": "string",
          "a_side": null,
          "type": "string",
          "z_side": null
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "date": null,
          "id": "string",
          "entry": "string"
        }
      ]
    }
  ],
  "cables": [
    {
      "id": "string",
      "a_side": null,
      "type": "string",
      "z_side": null
    }
  ],
  "connections": {
    "start": null,
    "end": null
  },
  "activity_log": [
    {
      "date": null,
      "id": "string",
      "entry": "string"
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
|photo_urls|[string]|false|none|none|
|pdf_urls|[object]|false|none|none|
|attributes|[[SurveyAttribute](#schemasurveyattribute)]|false|none|none|
|accessories|[[SurveyElementAccessory](#schemasurveyelementaccessory)]|false|none|none|
|children|[[SurveyElement](#schemasurveyelement)]|false|none|none|
|cables|[[CablePath](#schemacablepath)]|false|none|none|
|connections|[PathConnection](#schemapathconnection)|false|none|none|
|activity_log|[[SurveyElementActivityLog](#schemasurveyelementactivitylog)]|false|none|none|

<h2 id="tocS_SurveyAnnotation">SurveyAnnotation</h2>
<!-- backwards compatibility -->
<a id="schemasurveyannotation"></a>
<a id="schema_SurveyAnnotation"></a>
<a id="tocSsurveyannotation"></a>
<a id="tocssurveyannotation"></a>

```json
{
  "start_point": null,
  "end_point": null,
  "category": null,
  "text": "string",
  "stroke_width": "string",
  "stroke_color": "string",
  "location": null,
  "size": "string",
  "id": "string",
  "font_size": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|start_point|any|false|none|none|
|end_point|any|false|none|none|
|category|any|true|none|none|
|text|string|false|none|none|
|stroke_width|string|true|none|none|
|stroke_color|string|true|none|none|
|location|any|true|none|none|
|size|string|false|none|none|
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
    "user_id": null,
    "first_name": "string",
    "last_name": "string"
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
      "pdf_urls": [
        {}
      ],
      "attributes": [
        {
          "attribute_id": 0,
          "id": 0,
          "value": "string",
          "name": "string"
        }
      ],
      "accessories": [
        {
          "quantity": null,
          "model": "string",
          "description": "string",
          "labor_hours": 0,
          "manufacturer": "string",
          "price": null,
          "row_index": 0,
          "id": "string"
        }
      ],
      "children": [
        {}
      ],
      "cables": [
        {
          "id": "string",
          "a_side": null,
          "type": "string",
          "z_side": null
        }
      ],
      "connections": {
        "start": null,
        "end": null
      },
      "activity_log": [
        {
          "date": null,
          "id": "string",
          "entry": "string"
        }
      ]
    }
  ],
  "annotations": [
    {
      "start_point": null,
      "end_point": null,
      "category": null,
      "text": "string",
      "stroke_width": "string",
      "stroke_color": "string",
      "location": null,
      "size": "string",
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

