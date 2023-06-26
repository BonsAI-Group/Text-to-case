terraform {
  required_version = ">= 0.12"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  subscription_id = local.subscription_id
  tenant_id = local.tenant_id
  features {}
}

# Create the resource group
resource "azurerm_resource_group" "rg" {
  name     = local.resource_group_name
  location = local.location
}

# Create the Linux App Service Plan
resource "azurerm_service_plan" "appserviceplan" {
    name                = "webapp-ml-text-to-case"
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    os_type             = "Linux"
    sku_name            = local.service_plan_sku
}
