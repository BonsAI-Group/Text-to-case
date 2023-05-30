# Create the frontend webapp, pass in the App Service Plan ID
resource "azurerm_linux_web_app" "frontend" {
    name                                    = "webapp-ml-text-to-case-frontend"
    location                                = azurerm_resource_group.rg.location
    resource_group_name                     = azurerm_resource_group.rg.name
    service_plan_id                         = azurerm_service_plan.appserviceplan.id
    https_only                              = true
    app_settings = {
        DOCKER_REGISTRY_SERVER_URL          = "https://registry.hub.docker.com/ericvdberge/infoland.frontend"
        DOCKER_REGISTRY_SERVER_USERNAME     = "ericvdberge"
        DOCKER_REGISTRY_SERVER_PASSWORD     = "LXBS3yQtxk85fP8@"
        WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
        WEBSITES_PORT                       = 8000
    }
    site_config {
        always_on                           = false
        minimum_tls_version                 = 1.2
    }
}

# Create the backend webapp, pass in the App Service Plan ID
resource "azurerm_linux_web_app" "backend" {
    name                                    = "webapp-ml-text-to-case-backend"
    location                                = azurerm_resource_group.rg.location
    resource_group_name                     = azurerm_resource_group.rg.name
    service_plan_id                         = azurerm_service_plan.appserviceplan.id
    https_only                              = true
    app_settings = {
        DOCKER_REGISTRY_SERVER_URL          = "https://registry.hub.docker.com/ericvdberge/infoland.backend"
        DOCKER_REGISTRY_SERVER_USERNAME     = "ericvdberge"
        DOCKER_REGISTRY_SERVER_PASSWORD     = "LXBS3yQtxk85fP8@"
        WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
        WEBSITES_PORT                       = 80
    }
    site_config {
        always_on                           = false
        minimum_tls_version                 = 1.2
    }
}

