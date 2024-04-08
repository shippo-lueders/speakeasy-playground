<!-- Start SDK Example Usage [usage] -->
```python
import shippo
from shippo.models import components

s = shippo.Shippo()


res = s.example(header_param='<value>', example_body=components.ExampleBody())

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->