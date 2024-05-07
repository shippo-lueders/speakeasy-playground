# Shippo SDK


## Overview

### Available Operations

* [list](#list)
* [create](#create)
* [get](#get)

## list

### Example Usage

```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    header_param='<value>',
)

res = s.list(request=operations.ListRequest())

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [operations.ListRequest](../../models/operations/listrequest.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[List[components.ExampleBody]](../../models/.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create

### Example Usage

```python
import shippo

s = shippo.Shippo(
    header_param='<value>',
)

res = s.create(field='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `field`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[components.ExampleBody](../../models/components/examplebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

### Example Usage

```python
import shippo

s = shippo.Shippo(
    header_param='<value>',
)

res = s.get(example_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                | Type                     | Required                 | Description              |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `example_id`             | *str*                    | :heavy_check_mark:       | Object ID of the example |


### Response

**[components.ExampleBody](../../models/components/examplebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
