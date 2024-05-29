import fetchMock from 'fetch-mock';
import {describe, it} from 'mocha';
import {Shippo} from '../sdk';
import {GetExampleResponse} from "../models/operations";
import {expect} from "chai";

// TODO: figure out why this is required
Object.assign(fetchMock.config, { Headers, Request, Response, fetch })
globalThis.fetch = fetchMock.sandbox();

describe('TestExample', function() {
    this.timeout(10000);

    beforeEach(() => {
        fetchMock.reset()
    })

    it('test example simple', async () => {
        fetchMock.get('http://localhost:8080/example', {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
            body: {
                field: 'value',
            }
        });

        const sdk = new Shippo({serverURL: "http://localhost:8080"})

        const result: GetExampleResponse = await sdk.getExample()
        expect(result.exampleBody.field).to.be.equal('value')
    })

    it('test example complex', async () => {

        fetchMock.get('http://localhost:8080/example', {
            status: 200,
            headers: { 'Content-Type': 'application/json' },
            body: {
                field: {
                    other_field: 'value'
                },
            }
        });

        const sdk = new Shippo({serverURL: "http://localhost:8080"})

        const result: GetExampleResponse = await sdk.getExample()
        expect(result.exampleBody.field.otherField).to.be.equal('value')
    })
});
