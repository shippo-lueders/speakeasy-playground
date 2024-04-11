<!-- Start SDK Example Usage [usage] -->
```typescript
import { Shippo } from "shippo";

async function run() {
    const sdk = new Shippo();

    const headerParam = "<value>";

    const result = await sdk.listExamples(headerParam);

    // Handle the result
    console.log(result);
}

run();

```
<!-- End SDK Example Usage [usage] -->