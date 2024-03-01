<!-- Start SDK Example Usage [usage] -->
```python
import shippo
from shippo.models import components

s = shippo.Shippo()

req = components.LiveRateCreateRequest()

res = s.example(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->