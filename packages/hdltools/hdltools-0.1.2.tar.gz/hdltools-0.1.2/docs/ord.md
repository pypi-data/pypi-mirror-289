# ORDSupport

Supporting the creation of an ORD Document for Data Products. 

Main resource: [Open Resource Discovery](https://sap.github.io/open-resource-discovery/)


# Introduction

Open Resource Discovery (ORD) is a documentation of an application/service exposure to the external world. For a **data product** it consists in particular of the description of all the **APIs**.These resources are embedded into a taxonomy like **products**, **packages**, **vendor**, **consumption bundles** etc. with additional information of who is the owner, validity, ...

# Building Blocks

## API Description

The most basic building block of a data product is the API. Although the delta sharing is not the only supported protocol for a data product it might be the most used one. For this we need: 

1. ORD Document
   1. openResourceDiscovery (str), "1.8"
   2. policyLevel (enum: none, sap:core:v1, custom
   3. products [Array]
      1. ordId (str)
      2. title (str)
      3. shortDescription (str)
      4. vendor (str), e.g. "sap:vendor:SAP:"
   4. packages[Array]
      1. ordId (str)
      2. title (str)
      3. shortDescription (str)
      4. description (str)
      5. version (str)
      6. vendor (str), e.g. "sap:vendor:SAP:"
   5. IntegrationDependency
      1. ordId (str)
      2. title (str)
      3. partOfPackage (str)
      4. version (str)
      5. visibility (enum: public, internal, private)
      6. releaseStatus (Enum: active, beta, deprecated)
      7. mandatory (bool)
   6. dataProducts
      1. ordId (str)
      2. title (str)
      3. partOfPackage (str)
      4. version (str), e.g 
      5. lastUpdate (str), "1.2.3"
      6. visibility (enum: public, internal, private)
      7. releaseStatus (Enum: active, beta, deprecated)
      8.  type (enum: base, derived)
      9.  category (enum: business-object, analytical, other)
      10. outputPorts (Array\<Data Product Output Port\>)
      11. responsible (str), e.g. "sap:ach:CIC-DP-CO")
   7. Data Product Output Port
       1.  ordId (str), e.g. sap.cic:apiResource:RetailTransactionOData:v1
   8. apiResources [Array]: 
      1. ordId, e.g. "sap.s4:apiResource:API_BILL_OF_MATERIAL_SRV:v1"
      2. title (1-255chars)
      3. shortDescription (1-255chars)
      4. description
      5. partOfPackage
      6. version
      7. visibility (Enum: public, internal, private)
      8. releaseStatus (Enum: active, beta, deprecated)
      9. entry Points: URL
      10. api Protocol: (Enum: "delta-sharing")
      11. partOfConsumptionBundle (Array\<Consumption Bundle\>)
   9.  consumptionBundles [Array]
       1.  ordId - "sap.{provider}:apiResource:{share}:v{version}"
       2.  title - "Delta Sharing {share} for {recipient}"
       3.  credentialExchangeStrategies (Array of Credential Exchange Strategy)


