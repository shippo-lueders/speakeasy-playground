import {describe, it} from "mocha";
import {WebhookBody$} from "../models/components";
import {expect} from "chai";

describe('TestWebhook', function() {
    this.timeout(10000);

    it('should serialize webhook body to model', async () => {
        const payload = "some content";
        const data = `{"payload": "${payload}"}`;
        const json = JSON.parse(data);

        const webhookBody = WebhookBody$.inboundSchema.parse(json);

        expect(webhookBody.payload).to.be.equal(payload);
    })
});
