import fetchMock from 'fetch-mock';
import { describe, it } from 'mocha';
import { Shippo } from '../sdk';
import {GetExampleResponse} from "../models/operations";

// TODO: figure out why this is required
Object.assign(fetchMock.config, { Headers, Request, Response, fetch })
globalThis.fetch = fetchMock.sandbox();

describe('TestExample', function() {
    this.timeout(10000);

    it('test_example', async () => {
        fetchMock.get('http://localhost:8080/example', {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
            body: {
                field: 'Hello, world!',
            }
        });

        const sdk = new Shippo({serverURL: "http://localhost:8080"})

        try {
            const result: GetExampleResponse = await sdk.getExample()
            console.log(result.exampleBody)
        } catch (err) {
            console.log(err)
        }
    })
});
