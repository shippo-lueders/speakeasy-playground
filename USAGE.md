<!-- Start SDK Example Usage [usage] -->
```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.EntityCreateRequest(
    type=components.Type.FLAT_RATE,
)

res = s.create_example(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->