/* 
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

package org.openapis.openapi.models.operations;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.core.type.TypeReference;
import java.io.InputStream;
import java.lang.Deprecated;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Optional;
import org.openapis.openapi.utils.SpeakeasyMetadata;
import org.openapis.openapi.utils.Utils;

public class CreateExampleRequest {

    /**
     * The number of results to return per page (max 100)
     */
    @SpeakeasyMetadata("header:style=simple,explode=false,name=header_param")
    private Optional<? extends String> headerParam;

    @SpeakeasyMetadata("request:mediaType=application/json")
    private org.openapis.openapi.models.components.ExampleBody exampleBody;

    @JsonCreator
    public CreateExampleRequest(
            Optional<? extends String> headerParam,
            org.openapis.openapi.models.components.ExampleBody exampleBody) {
        Utils.checkNotNull(headerParam, "headerParam");
        Utils.checkNotNull(exampleBody, "exampleBody");
        this.headerParam = headerParam;
        this.exampleBody = exampleBody;
    }
    
    public CreateExampleRequest(
            org.openapis.openapi.models.components.ExampleBody exampleBody) {
        this(Optional.empty(), exampleBody);
    }

    /**
     * The number of results to return per page (max 100)
     */
    @SuppressWarnings("unchecked")
    @JsonIgnore
    public Optional<String> headerParam() {
        return (Optional<String>) headerParam;
    }

    @JsonIgnore
    public org.openapis.openapi.models.components.ExampleBody exampleBody() {
        return exampleBody;
    }

    public final static Builder builder() {
        return new Builder();
    }

    /**
     * The number of results to return per page (max 100)
     */
    public CreateExampleRequest withHeaderParam(String headerParam) {
        Utils.checkNotNull(headerParam, "headerParam");
        this.headerParam = Optional.ofNullable(headerParam);
        return this;
    }

    /**
     * The number of results to return per page (max 100)
     */
    public CreateExampleRequest withHeaderParam(Optional<? extends String> headerParam) {
        Utils.checkNotNull(headerParam, "headerParam");
        this.headerParam = headerParam;
        return this;
    }

    public CreateExampleRequest withExampleBody(org.openapis.openapi.models.components.ExampleBody exampleBody) {
        Utils.checkNotNull(exampleBody, "exampleBody");
        this.exampleBody = exampleBody;
        return this;
    }
    
    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CreateExampleRequest other = (CreateExampleRequest) o;
        return 
            java.util.Objects.deepEquals(this.headerParam, other.headerParam) &&
            java.util.Objects.deepEquals(this.exampleBody, other.exampleBody);
    }
    
    @Override
    public int hashCode() {
        return java.util.Objects.hash(
            headerParam,
            exampleBody);
    }
    
    @Override
    public String toString() {
        return Utils.toString(CreateExampleRequest.class,
                "headerParam", headerParam,
                "exampleBody", exampleBody);
    }
    
    public final static class Builder {
 
        private Optional<? extends String> headerParam = Optional.empty();
 
        private org.openapis.openapi.models.components.ExampleBody exampleBody;  
        
        private Builder() {
          // force use of static builder() method
        }

        /**
         * The number of results to return per page (max 100)
         */
        public Builder headerParam(String headerParam) {
            Utils.checkNotNull(headerParam, "headerParam");
            this.headerParam = Optional.ofNullable(headerParam);
            return this;
        }

        /**
         * The number of results to return per page (max 100)
         */
        public Builder headerParam(Optional<? extends String> headerParam) {
            Utils.checkNotNull(headerParam, "headerParam");
            this.headerParam = headerParam;
            return this;
        }

        public Builder exampleBody(org.openapis.openapi.models.components.ExampleBody exampleBody) {
            Utils.checkNotNull(exampleBody, "exampleBody");
            this.exampleBody = exampleBody;
            return this;
        }
        
        public CreateExampleRequest build() {
            return new CreateExampleRequest(
                headerParam,
                exampleBody);
        }
    }
}

