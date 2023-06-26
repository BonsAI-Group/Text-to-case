

# Create the frontend webapp, pass in the App Service Plan ID and backend URL
resource "azurerm_linux_web_app" "frontend" {
  name                                    = "webapp-${local.resource_prefix}-frontend"
  location                                = azurerm_resource_group.rg.location
  resource_group_name                     = azurerm_resource_group.rg.name
  service_plan_id                         = azurerm_service_plan.appserviceplan.id
  https_only                              = true
  app_settings = {
    DOCKER_REGISTRY_SERVER_URL          = "https://index.docker.io"
    DOCKER_REGISTRY_SERVER_USERNAME     = ""
    DOCKER_REGISTRY_SERVER_PASSWORD     = ""
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
  }
  site_config {
    always_on                           = true
    minimum_tls_version                 = "1.2"
    application_stack {
      docker_image     = local.frontend_docker_image
      docker_image_tag = "latest"
    }
  }
}

# Create the backend webapp, pass in the App Service Plan ID and frontend URL
resource "azurerm_linux_web_app" "backend" {
  name                                    = "webapp-${local.resource_prefix}-backend"
  location                                = azurerm_resource_group.rg.location
  resource_group_name                     = azurerm_resource_group.rg.name
  service_plan_id                         = azurerm_service_plan.appserviceplan.id
  https_only                              = true
  app_settings = {
    DOCKER_REGISTRY_SERVER_URL          = "https://index.docker.io"
    DOCKER_REGISTRY_SERVER_USERNAME     = ""
    DOCKER_REGISTRY_SERVER_PASSWORD     = ""
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
  }
  site_config {
    always_on                           = true
    minimum_tls_version                 = "1.2"
    application_stack {
      docker_image     = local.backend_docker_image
      docker_image_tag = "latest"
    }
  }
}

# Create the models (hosting) webapp, pass in the App Service Plan ID
resource "azurerm_linux_web_app" "models" {
  name                                    = "webapp-${local.resource_prefix}-models"
  location                                = azurerm_resource_group.rg.location
  resource_group_name                     = azurerm_resource_group.rg.name
  service_plan_id                         = azurerm_service_plan.appserviceplan.id
  https_only                              = true
  app_settings = {
    DOCKER_REGISTRY_SERVER_URL          = "https://index.docker.io"
    DOCKER_REGISTRY_SERVER_USERNAME     = ""
    DOCKER_REGISTRY_SERVER_PASSWORD     = ""
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
  }
  site_config {
    always_on                           = true
    minimum_tls_version                 = "1.2"
    application_stack {
      docker_image     = local.models_docker_image
      docker_image_tag = "latest"
    }
  }
}
