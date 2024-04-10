import fetchMock from 'fetch-mock';
import { describe, it } from 'mocha';
import { expect } from 'chai';
import { Shippo } from '../sdk';
import {GetExampleResponse} from "../models/operations";

// TODO: figure out why this is required
Object.assign(fetchMock.config, { Headers, Request, Response, fetch })
globalThis.fetch = fetchMock.sandbox();

describe('TestExample', function() {
    this.timeout(10000);

    beforeEach(() => {
        fetchMock.reset()
    })

    it('test_example_with_optional', async () => {
        fetchMock.get('http://localhost:8080/example', {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
            body: {
                requiredField: 'Hello, world!',
            }
        });

        const sdk = new Shippo({serverURL: "http://localhost:8080"})

        try {
            const result: GetExampleResponse = await sdk.getExample()
            console.log(result.exampleBody)
        } catch (err) {
            expect.fail(`Method threw an exception: ${err}`)
        }
    })

    it('test_example_with_optional_null', async () => {
        fetchMock.get('http://localhost:8080/example', {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
            body: {
                requiredField: 'Hello, world!',
                optionalField: null
            }
        });

        const sdk = new Shippo({serverURL: "http://localhost:8080"})

        try {
            const result: GetExampleResponse = await sdk.getExample()
            console.log(result.exampleBody)
        } catch (err) {
            expect.fail(`Method threw an exception: ${err}`)
        }
    })
});
