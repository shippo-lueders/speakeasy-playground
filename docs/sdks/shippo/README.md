# Shippo SDK


## Overview

### Available Operations

* [example](#example)
* [example_two](#example_two)

## example

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.LiveRateCreateRequest()

res = s.example(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.LiveRateCreateRequest](../../models/components/liveratecreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ExampleResponse](../../models/operations/exampleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## example_two

### Example Usage

```python
import shippo

s = shippo.Shippo()


res = s.example_two()

if res.shipment is not None:
    # handle response
    pass
```


### Response

**[operations.ExampleTwoResponse](../../models/operations/exampletworesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
