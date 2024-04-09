/*
 * Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT.
 */

import * as components from "../components";
import * as z from "zod";

export type GetExampleRequest = {
    /**
     * The number of results to return per page (max 100)
     */
    headerParam?: string | undefined;
};

export type GetExampleResponse = {
    httpMeta: components.HTTPMetadata;
};

/** @internal */
export namespace GetExampleRequest$ {
    export type Inbound = {
        header_param?: string | undefined;
    };

    export const inboundSchema: z.ZodType<GetExampleRequest, z.ZodTypeDef, Inbound> = z
        .object({
            header_param: z.string().optional(),
        })
        .transform((v) => {
            return {
                ...(v.header_param === undefined ? null : { headerParam: v.header_param }),
            };
        });

    export type Outbound = {
        header_param?: string | undefined;
    };

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, GetExampleRequest> = z
        .object({
            headerParam: z.string().optional(),
        })
        .transform((v) => {
            return {
                ...(v.headerParam === undefined ? null : { header_param: v.headerParam }),
            };
        });
}

/** @internal */
export namespace GetExampleResponse$ {
    export type Inbound = {
        HttpMeta: components.HTTPMetadata$.Inbound;
    };

    export const inboundSchema: z.ZodType<GetExampleResponse, z.ZodTypeDef, Inbound> = z
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

    export const outboundSchema: z.ZodType<Outbound, z.ZodTypeDef, GetExampleResponse> = z
        .object({
            httpMeta: components.HTTPMetadata$.outboundSchema,
        })
        .transform((v) => {
            return {
                HttpMeta: v.httpMeta,
            };
        });
}
