# Shippo SDK


## Overview

### Available Operations

* [example](#example)

## example

### Example Usage

```python
import shippo

s = shippo.Shippo()


res = s.example(results_per_page=904965)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `results_per_page`                                 | *Optional[int]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |


### Response

**[operations.ExampleResponse](../../models/operations/exampleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
