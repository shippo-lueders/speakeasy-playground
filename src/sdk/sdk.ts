/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import { SDKHooks } from "../hooks";
import { SDK_METADATA, SDKOptions, serverURLFromOptions } from "../lib/config";
import * as enc$ from "../lib/encodings";
import { HTTPClient } from "../lib/http";
import * as schemas$ from "../lib/schemas";
import { ClientSDK, RequestOptions } from "../lib/sdks";
import * as components from "../models/components";
import * as operations from "../models/operations";

export class Shippo extends ClientSDK {
    private readonly options$: SDKOptions & { hooks?: SDKHooks };

    constructor(options: SDKOptions = {}) {
        const opt = options as unknown;
        let hooks: SDKHooks;
        if (
            typeof opt === "object" &&
            opt != null &&
            "hooks" in opt &&
            opt.hooks instanceof SDKHooks
        ) {
            hooks = opt.hooks;
        } else {
            hooks = new SDKHooks();
        }

        super({
            client: options.httpClient || new HTTPClient(),
            baseURL: serverURLFromOptions(options),
            hooks,
        });

        this.options$ = { ...options, hooks };
        void this.options$;
    }

    async getExample(
        headerParam?: string | undefined,
        options?: RequestOptions
    ): Promise<operations.GetExampleResponse> {
        const input$: operations.GetExampleRequest = {
            headerParam: headerParam,
        };
        const headers$ = new Headers();
        headers$.set("user-agent", SDK_METADATA.userAgent);
        headers$.set("Accept", "application/json");

        const payload$ = schemas$.parse(
            input$,
            (value$) => operations.GetExampleRequest$.outboundSchema.parse(value$),
            "Input validation failed"
        );
        const body$ = null;

        const path$ = this.templateURLComponent("/example")();

        const query$ = "";

        headers$.set(
            "header_param",
            enc$.encodeSimple("header_param", payload$.header_param, {
                explode: false,
                charEncoding: "none",
            })
        );
        const context = { operationID: "GetExample", oAuth2Scopes: [], securitySource: null };

        const doOptions = { context, errorCodes: ["4XX", "5XX"] };
        const request$ = this.createRequest$(
            context,
            { method: "GET", path: path$, headers: headers$, query: query$, body: body$ },
            options
        );

        const response = await this.do$(request$, doOptions);

        const responseFields$ = {
            HttpMeta: { Response: response, Request: request$ },
        };

        const [result$] = await this.matcher<operations.GetExampleResponse>()
            .json(200, operations.GetExampleResponse$, { key: "ExampleBody" })
            .fail(["4XX", "5XX"])
            .match(response, request$, { extraFields: responseFields$ });

        return result$;
    }

    async createExample(
        headerParam?: string | undefined,
        exampleBody?: components.ExampleBody | undefined,
        options?: RequestOptions
    ): Promise<operations.CreateExampleResponse> {
        const input$: operations.CreateExampleRequest = {
            headerParam: headerParam,
            exampleBody: exampleBody,
        };
        const headers$ = new Headers();
        headers$.set("user-agent", SDK_METADATA.userAgent);
        headers$.set("Content-Type", "application/json");
        headers$.set("Accept", "application/json");

        const payload$ = schemas$.parse(
            input$,
            (value$) => operations.CreateExampleRequest$.outboundSchema.parse(value$),
            "Input validation failed"
        );
        const body$ = enc$.encodeJSON("body", payload$.ExampleBody, { explode: true });

        const path$ = this.templateURLComponent("/example")();

        const query$ = "";

        headers$.set(
            "header_param",
            enc$.encodeSimple("header_param", payload$.header_param, {
                explode: false,
                charEncoding: "none",
            })
        );
        const context = { operationID: "CreateExample", oAuth2Scopes: [], securitySource: null };

        const doOptions = { context, errorCodes: ["4XX", "5XX"] };
        const request$ = this.createRequest$(
            context,
            { method: "POST", path: path$, headers: headers$, query: query$, body: body$ },
            options
        );

        const response = await this.do$(request$, doOptions);

        const responseFields$ = {
            HttpMeta: { Response: response, Request: request$ },
        };

        const [result$] = await this.matcher<operations.CreateExampleResponse>()
            .json(201, operations.CreateExampleResponse$, { key: "ExampleBody" })
            .fail(["4XX", "5XX"])
            .match(response, request$, { extraFields: responseFields$ });

        return result$;
    }
}
