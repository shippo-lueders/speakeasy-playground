/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type CreateExampleRequest = {
    /**
     * The number of results to return per page (max 100)
     */
    headerParam?: string | undefined;
    exampleBody?: components.ExampleBody | undefined;
};

export type CreateExampleResponse = {
    httpMeta: components.HTTPMetadata;
};

/** @internal */
export namespace CreateExampleRequest$ {
    export type Inbound = {
        header_param?: string | undefined;
        ExampleBody?: components.ExampleBody$.Inbound | undefined;
    };

    export const inboundSchema: z.ZodType<CreateExampleRequest, z.ZodTypeDef, Inbound> = z
        .object({
            header_param: z.string().optional(),
            ExampleBody: components.ExampleBody$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                ...(v.header_param === undefined ? null : { headerParam: v.header_param }),
                ...(v.ExampleBody === undefined ? null : { exampleBody: v.ExampleBody }),
            };
        });

    export type Outbound = {
        header_param?: string | undefined;
        ExampleBody?: components.ExampleBody$.Outbound | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, CreateExampleRequest> = z
        .object({
            headerParam: z.string().optional(),
            exampleBody: components.ExampleBody$.outboundSchema.optional(),
        })
        .transform((v) => {
            return {
                ...(v.headerParam === undefined ? null : { header_param: v.headerParam }),
                ...(v.exampleBody === undefined ? null : { ExampleBody: v.exampleBody }),
            };
        });
}

/** @internal */
export namespace CreateExampleResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
    };

    export const inboundSchema: z.ZodType<CreateExampleResponse, z.ZodTypeDef, Inbound> = z
        .object({
            HttpMeta: components.HTTPMetadata$.inboundSchema,
        })
        .transform((v) => {
            return {
                httpMeta: v.HttpMeta,
            };
        });

    export type Outbound = {
        HttpMeta: components.HTTPMetadata$.Outbound;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, CreateExampleResponse> = z
        .object({
            httpMeta: components.HTTPMetadata$.outboundSchema,
        })
        .transform((v) => {
            return {
                HttpMeta: v.httpMeta,
            };
        });
}