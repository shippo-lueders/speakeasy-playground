<!-- Start SDK Example Usage [usage] -->
```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    header_param='<value>',
)

res = s.list(request=operations.ListRequest())

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->