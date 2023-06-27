locals {
    //Configure login
    subscription_id = "eb825cf1-d2c0-44b0-a557-66cee2f3a2e6"
    tenant_id = "0172c9f5-f568-42ac-9eb8-24ef84881faa"

    //Configure the prefix for all resources that are going to be created
    resource_prefix = "infolandttc"

    //Configure resource group names
    //with location of resources and sku (how much resources)
    resource_group_name = "Infoland-text-to-case"
    service_plan_sku = "P2v2"
    location = "West Europe"

    //Configure docker images
    frontend_docker_image = "ericvdberge/infoland.frontend"
    backend_docker_image = "ericvdberge/infoland.backend"
    models_docker_image = "ericvdberge/infoland.models"

}