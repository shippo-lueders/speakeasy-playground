<!-- Start SDK Example Usage [usage] -->
```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.ExampleWithOneOfArray(
    one_of_array=[
        904965,
    ],
)

res = s.example(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->