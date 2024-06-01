# SDK


## Overview

### Available Operations

* [getExample](#getexample)
* [createExample](#createexample)

## getExample

### Example Usage

```java
package hello.world;

import java.math.BigDecimal;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.Optional;
import org.openapis.openapi.SDK;
import org.openapis.openapi.models.components.*;
import org.openapis.openapi.models.operations.*;
import org.openapis.openapi.utils.EventStream;
import org.openapitools.jackson.nullable.JsonNullable;
import static java.util.Map.entry;

public class Application {

    public static void main(String[] args) throws Exception {
        try {
            SDK sdk = SDK.builder()
                .shippoApiVersion("2018-02-08")
                .build();

            GetExampleResponse res = sdk.getExample()
                .headerParam("<value>")
                .shippoApiVersion("2018-02-08")
                .call();

            if (res.exampleBody().isPresent()) {
                // handle response
            }
        } catch (org.openapis.openapi.models.errors.SDKError e) {
            // handle exception
            throw e;
        } catch (Exception e) {
            // handle exception
            throw e;
        }
    }
}
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `headerParam`                                        | *Optional<? extends String>*                         | :heavy_minus_sign:                                   | The number of results to return per page (max 100)   |                                                      |
| `shippoApiVersion`                                   | *Optional<? extends String>*                         | :heavy_minus_sign:                                   | String used to pick a non-default API version to use | 2018-02-08                                           |


### Response

**[Optional<? extends org.openapis.openapi.models.operations.GetExampleResponse>](../../models/operations/GetExampleResponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models/errors/SDKError | 4xx-5xx                | */*                    |

## createExample

### Example Usage

```java
package hello.world;

import java.math.BigDecimal;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.Optional;
import org.openapis.openapi.SDK;
import org.openapis.openapi.models.components.*;
import org.openapis.openapi.models.operations.*;
import org.openapis.openapi.utils.EventStream;
import org.openapitools.jackson.nullable.JsonNullable;
import static java.util.Map.entry;

public class Application {

    public static void main(String[] args) throws Exception {
        try {
            SDK sdk = SDK.builder()
                .shippoApiVersion("2018-02-08")
                .build();

            CreateExampleResponse res = sdk.createExample()
                .headerParam("<value>")
                .exampleBody(ExampleBody.builder()
                    .build())
                .call();

            // handle response
        } catch (org.openapis.openapi.models.errors.SDKError e) {
            // handle exception
            throw e;
        } catch (Exception e) {
            // handle exception
            throw e;
        }
    }
}
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `headerParam`                                                                                                    | *Optional<? extends String>*                                                                                     | :heavy_minus_sign:                                                                                               | The number of results to return per page (max 100)                                                               |
| `exampleBody`                                                                                                    | [Optional<? extends org.openapis.openapi.models.components.ExampleBody>](../../models/components/ExampleBody.md) | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |


### Response

**[Optional<? extends org.openapis.openapi.models.operations.CreateExampleResponse>](../../models/operations/CreateExampleResponse.md)**
### Errors

| Error Object           | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| models/errors/SDKError | 4xx-5xx                | */*                    |
