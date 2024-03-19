# Shippo SDK


## Overview

### Available Operations

* [create_example](#create_example)
* [update_example](#update_example)

## create_example

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.EntityCreateRequest(
    type=components.Type.FLAT_RATE,
)

res = s.create_example(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.EntityCreateRequest](../../models/components/entitycreaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateExampleResponse](../../models/operations/createexampleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_example

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.EntityUpdateRequest(
    type=components.EntityUpdateRequestType.FLAT_RATE,
    id='<id>',
)

res = s.update_example(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.EntityUpdateRequest](../../models/components/entityupdaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateExampleResponse](../../models/operations/updateexampleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
