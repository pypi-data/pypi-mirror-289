import dataclasses
from typing import Optional

from launchflow.gcp.cloud_run_container import CloudRunServiceContainer
from launchflow.gcp.resource import GCPResource
from launchflow.models.enums import ResourceProduct
from launchflow.models.flow_state import EnvironmentState
from launchflow.node import Outputs
from launchflow.resource import ResourceInputs


@dataclasses.dataclass
class CustomDomainMappingOutputs(Outputs):
    ip_address: str
    registered_domain: str
    ssl_certificate_id: str


@dataclasses.dataclass
class CustomDomainMappingInputs(ResourceInputs):
    domain: str
    cloud_run_service: str
    region: Optional[str]


class CustomDomainMapping(GCPResource[CustomDomainMappingOutputs]):
    """A resource for mapping a custom domain to a Cloud Run service.

    Like all [Resources](/docs/concepts/resources), this class configures itself across multiple [Environments](/docs/concepts/environments).

    ### Example Usage
    ```python
    import launchflow as lf

    custom_domain_mapping = lf.gcp.CustomDomainMapping("my-custom-domain-mapping", domain="my-domain.com", cloud_run=lf.gcp.CloudRunServiceContainer("my-cloud-run-service"))
    ```
    """

    product = ResourceProduct.GCP_CUSTOM_DOMAIN_MAPPING

    def __init__(
        self, name: str, *, domain: str, cloud_run: CloudRunServiceContainer
    ) -> None:
        """Create a new CustomDomainMapping resource.

        **Args:**
        - `name` (str): The name of the CustomDomainMapping resource. This must be globally unique.
        - `domain` (str): The domain to map to the Cloud Run service.
        - `cloud_run` (CloudRunServiceContainer): The Cloud Run service to map the domain to.
        """
        super().__init__(
            name=name,
        )
        self.domain = domain
        self.cloud_run = cloud_run

    def inputs(self, environment_state: EnvironmentState) -> CustomDomainMappingInputs:
        """Get the inputs for the Custom Domain Mapping resource.

        **Args:**
        - `environment_type` (EnvironmentType): The type of environment.

        **Returns:**
        - CustomDomainMappingInputs: The inputs for the Custom Domain Mapping resource.
        """
        return CustomDomainMappingInputs(
            resource_id=self.resource_id,
            domain=self.domain,
            cloud_run_service=self.cloud_run.resource_id,
            region=self.cloud_run.region,
        )
