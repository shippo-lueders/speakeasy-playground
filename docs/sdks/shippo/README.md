# Shippo SDK


## Overview

### Available Operations

* [GetExample](#getexample)
* [CreateExample](#createexample)

## GetExample

### Example Usage

```csharp
using Shippo;
using Shippo.Models.Requests;

var sdk = new ShippoSDK();

var res = await sdk.GetExampleAsync(headerParam: "<value>");

// handle response
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `HeaderParam`                                      | *string*                                           | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |


### Response

**[GetExampleResponse](../../Models/Requests/GetExampleResponse.md)**
### Errors

| Error Object                                | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Shippo.Models.Errors.GetExampleResponseBody | 400                                         | application/json                            |
| Shippo.Models.Errors.SDKException           | 4xx-5xx                                     | */*                                         |

## CreateExample

### Example Usage

```csharp
using Shippo;
using Shippo.Models.Requests;
using Shippo.Models.Components;

var sdk = new ShippoSDK();

var res = await sdk.CreateExampleAsync(
    headerParam: "<value>",
    exampleBody: new ExampleBody() {});

// handle response
```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `HeaderParam`                                         | *string*                                              | :heavy_minus_sign:                                    | The number of results to return per page (max 100)    |
| `ExampleBody`                                         | [ExampleBody](../../Models/Components/ExampleBody.md) | :heavy_minus_sign:                                    | N/A                                                   |


### Response

**[CreateExampleResponse](../../Models/Requests/CreateExampleResponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| Shippo.Models.Errors.SDKException | 4xx-5xx                           | */*                               |
