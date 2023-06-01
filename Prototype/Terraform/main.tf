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
    sku_name            = "F1"
}