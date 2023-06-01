locals {
    //Configure login
    subscription_id = "f76a9885-d2db-43ee-85dd-267a6228a9bf"
    tenant_id = "c66b6765-b794-4a2b-84ed-845b341c086a"

    //Configure the prefix for all resources that are going to be created
    resource_prefix = "infolandttc"

    //Configure resource group names
    //with location of resources and sku (how much resources)
    resource_group_name = "Infoland-text-to-case"
    service_plan_sku = "B1"
    location = "West Europe"

    //Configure docker images
    frontend_docker_image = "ericvdberge/infoland.frontend"
    backend_docker_image = "ericvdberge/infoland.backend"
}