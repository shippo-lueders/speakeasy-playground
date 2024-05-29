/* 
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

package org.openapis.openapi.utils;

import java.net.http.HttpRequest.BodyPublisher;

public class SerializedBody {
    
    private final String contentType;
    private final BodyPublisher body;
    
    public SerializedBody(String contentType, BodyPublisher body) {
        Utils.checkNotNull(contentType, "content");
        Utils.checkNotNull(body, "body");
        this.contentType = contentType;
        this.body = body;
    }
    
    public String contentType() {
        return contentType;
    }
    
    public BodyPublisher body() {
        return body;
    }
}
