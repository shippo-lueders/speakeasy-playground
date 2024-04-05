<!-- Start SDK Example Usage [usage] -->
```python
import shippo
from shippo.models import components

s = shippo.Shippo()


res = s.example(header_param='<value>', shippo_api_version='2018-02-08T00:00:00Z', example_body=components.ExampleBody())

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->