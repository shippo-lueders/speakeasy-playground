/* 
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

package org.openapis.openapi.models.operations;

import com.fasterxml.jackson.core.type.TypeReference;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.Optional;
import java.util.stream.Stream;
import org.openapis.openapi.models.errors.SDKError;
import org.openapis.openapi.utils.LazySingletonValue;
import org.openapis.openapi.utils.Utils;
import org.openapitools.jackson.nullable.JsonNullable;


public class GetExampleRequestBuilder {

    private Optional<? extends String> headerParam = Optional.empty();
    private final SDKMethodInterfaces.MethodCallGetExample sdk;

    public GetExampleRequestBuilder(SDKMethodInterfaces.MethodCallGetExample sdk) {
        this.sdk = sdk;
    }
                
    public GetExampleRequestBuilder headerParam(String headerParam) {
        Utils.checkNotNull(headerParam, "headerParam");
        this.headerParam = Optional.of(headerParam);
        return this;
    }

    public GetExampleRequestBuilder headerParam(Optional<? extends String> headerParam) {
        Utils.checkNotNull(headerParam, "headerParam");
        this.headerParam = headerParam;
        return this;
    }

    public GetExampleResponse call() throws Exception {

        return sdk.getExample(
            headerParam);
    }
}
