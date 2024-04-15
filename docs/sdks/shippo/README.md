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


res = s.example(header_param='<value>', example_body=components.ExampleBody())

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `header_param`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The number of results to return per page (max 100)                         |
| `example_body`                                                             | [Optional[components.ExampleBody]](../../models/components/examplebody.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.ExampleResponse](../../models/operations/exampleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
