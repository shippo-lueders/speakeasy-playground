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

s = shippo.Shippo()


res = s.list(header_param='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `header_param`                                     | *Optional[str]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |


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
from shippo.models import components

s = shippo.Shippo()


res = s.create(header_param='<value>', example_body=components.ExampleBody())

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

**[components.ExampleBody](../../models/components/examplebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

### Example Usage

```python
import shippo

s = shippo.Shippo()


res = s.get(example_id='<value>', header_param='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `example_id`                                       | *str*                                              | :heavy_check_mark:                                 | Object ID of the example                           |
| `header_param`                                     | *Optional[str]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |


### Response

**[components.ExampleBody](../../models/components/examplebody.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
