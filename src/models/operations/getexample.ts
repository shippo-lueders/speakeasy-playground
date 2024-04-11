/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type GetExampleRequest = {
    exampleId: string;
    /**
     * The number of results to return per page (max 100)
     */
    headerParam?: string | undefined;
};

export type GetExampleResponse = {
    httpMeta: components.HTTPMetadata;
    exampleBody?: components.ExampleBody | undefined;
};

/** @internal */
export namespace GetExampleRequest$ {
    export type Inbound = {
        ExampleId: string;
        header_param?: string | undefined;
    };

    export const inboundSchema: z.ZodType<GetExampleRequest, z.ZodTypeDef, Inbound> = z
        .object({
            ExampleId: z.string(),
            header_param: z.string().optional(),
        })
        .transform((v) => {
            return {
                exampleId: v.ExampleId,
                ...(v.header_param === undefined ? null : { headerParam: v.header_param }),
            };
        });

    export type Outbound = {
        ExampleId: string;
        header_param?: string | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, GetExampleRequest> = z
        .object({
            exampleId: z.string(),
            headerParam: z.string().optional(),
        })
        .transform((v) => {
            return {
                ExampleId: v.exampleId,
                ...(v.headerParam === undefined ? null : { header_param: v.headerParam }),
            };
        });
}

/** @internal */
export namespace GetExampleResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
        ExampleBody?: components.ExampleBody$.Inbound | undefined;
    };

    export const inboundSchema: z.ZodType<GetExampleResponse, z.ZodTypeDef, Inbound> = z
        .object({
            HttpMeta: components.HTTPMetadata$.inboundSchema,
            ExampleBody: components.ExampleBody$.inboundSchema.optional(),
        })
        .transform((v) => {
            return {
                httpMeta: v.HttpMeta,
                ...(v.ExampleBody === undefined ? null : { exampleBody: v.ExampleBody }),
            };
        });

    export type Outbound = {
        HttpMeta: components.HTTPMetadata$.Outbound;
        ExampleBody?: components.ExampleBody$.Outbound | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, GetExampleResponse> = z
        .object({
            httpMeta: components.HTTPMetadata$.outboundSchema,
            exampleBody: components.ExampleBody$.outboundSchema.optional(),
        })
        .transform((v) => {
            return {
                HttpMeta: v.httpMeta,
                ...(v.exampleBody === undefined ? null : { ExampleBody: v.exampleBody }),
            };
        });
}
