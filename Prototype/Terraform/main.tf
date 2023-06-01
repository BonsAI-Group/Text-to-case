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
  subscription_id = "f76a9885-d2db-43ee-85dd-267a6228a9bf"
  tenant_id = "c66b6765-b794-4a2b-84ed-845b341c086a"
  features {}
}

# Create the resource group
resource "azurerm_resource_group" "rg" {
  name     = "Infoland-text-to-case"
  location = "West Europe"
}

# Create the Linux App Service Plan
resource "azurerm_service_plan" "appserviceplan" {
    name                = "webapp-ml-text-to-case"
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    os_type             = "Linux"
    sku_name            = "B1"
}