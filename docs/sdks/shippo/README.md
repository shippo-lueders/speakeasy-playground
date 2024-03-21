# Shippo SDK


## Overview

### Available Operations

* [example](#example)

## example

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.ExampleWithOneOfArray(
    one_of_array=[
        904965,
    ],
)

res = s.example(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.ExampleWithOneOfArray](../../models/components/examplewithoneofarray.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ExampleResponse](../../models/operations/exampleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
