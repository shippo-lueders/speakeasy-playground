package org.openapis.openapi

import com.github.tomakehurst.wiremock.WireMockServer
import spock.lang.Shared
import spock.lang.Specification

import static com.github.tomakehurst.wiremock.client.WireMock.*
import static com.github.tomakehurst.wiremock.core.WireMockConfiguration.options


class ExampleSpec extends Specification {
    @Shared
    WireMockServer wiremockServer

    def setupSpec() {
        wiremockServer = new WireMockServer(options().dynamicPort())
        wiremockServer.start()
    }

    def cleanupSpec() {
        wiremockServer.stop()
    }

    def cleanup() {
        wiremockServer.resetAll()
    }

    def "should do something"() {
        given:
        SDK sdk = SDK.builder()
                .serverURL(wiremockServer.baseUrl())
                .build()

        wiremockServer.stubFor(get("/example").willReturn(
                ok('{"field": "value"}').withHeader("Content-Type", "application/json")
        ))

        when:
        def response = sdk.getExample().call()

        then:
        def body = response.exampleBody().get()
        assert body.field().get() == "value"
    }
    
}
