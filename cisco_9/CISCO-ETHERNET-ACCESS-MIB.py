# SNMP MIB module (CISCO-ETHERNET-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ETHERNET-ACCESS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:14:07 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(managementDomainIndex,
 vtpVlanIndex) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "managementDomainIndex",
    "vtpVlanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoEthernetAccessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466)
)
if mibBuilder.loadTexts:
    ciscoEthernetAccessMIB.setRevisions(
        ("2007-09-14 00:00",
         "2005-01-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CeaVlanUNIType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("isolated", 2),
          ("community", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEthernetAccessMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEthernetAccessMIBObjects = _CiscoEthernetAccessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1)
)
_CeaGlobals_ObjectIdentity = ObjectIdentity
ceaGlobals = _CeaGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1)
)


class _CeaMaxNNIPorts_Type(Integer32):
    """Custom type ceaMaxNNIPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CeaMaxNNIPorts_Type.__name__ = "Integer32"
_CeaMaxNNIPorts_Object = MibScalar
ceaMaxNNIPorts = _CeaMaxNNIPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 1),
    _CeaMaxNNIPorts_Type()
)
ceaMaxNNIPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceaMaxNNIPorts.setStatus("current")


class _CeaMaxUNIVlanCommunityPorts_Type(Integer32):
    """Custom type ceaMaxUNIVlanCommunityPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CeaMaxUNIVlanCommunityPorts_Type.__name__ = "Integer32"
_CeaMaxUNIVlanCommunityPorts_Object = MibScalar
ceaMaxUNIVlanCommunityPorts = _CeaMaxUNIVlanCommunityPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 2),
    _CeaMaxUNIVlanCommunityPorts_Type()
)
ceaMaxUNIVlanCommunityPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceaMaxUNIVlanCommunityPorts.setStatus("current")
_CeaConfig_ObjectIdentity = ObjectIdentity
ceaConfig = _CeaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2)
)
_CeaPortTable_Object = MibTable
ceaPortTable = _CeaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ceaPortTable.setStatus("current")
_CeaPortEntry_Object = MibTableRow
ceaPortEntry = _CeaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1)
)
ceaPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ceaPortEntry.setStatus("current")


class _CeaPortType_Type(Integer32):
    """Custom type ceaPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("uni", 2),
          ("nni", 3),
          ("eni", 4))
    )


_CeaPortType_Type.__name__ = "Integer32"
_CeaPortType_Object = MibTableColumn
ceaPortType = _CeaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 1),
    _CeaPortType_Type()
)
ceaPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceaPortType.setStatus("current")


class _CeaPortCapability_Type(Bits):
    """Custom type ceaPortCapability based on Bits"""
    namedValues = NamedValues(
        *(("nni", 0),
          ("uni", 1),
          ("eni", 2))
    )

_CeaPortCapability_Type.__name__ = "Bits"
_CeaPortCapability_Object = MibTableColumn
ceaPortCapability = _CeaPortCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 2),
    _CeaPortCapability_Type()
)
ceaPortCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceaPortCapability.setStatus("current")
_CeaUNIVlanTable_Object = MibTable
ceaUNIVlanTable = _CeaUNIVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ceaUNIVlanTable.setStatus("current")
_CeaUNIVlanEntry_Object = MibTableRow
ceaUNIVlanEntry = _CeaUNIVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1)
)
ceaUNIVlanEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanIndex"),
)
if mibBuilder.loadTexts:
    ceaUNIVlanEntry.setStatus("current")
_CeaUNIVlanType_Type = CeaVlanUNIType
_CeaUNIVlanType_Object = MibTableColumn
ceaUNIVlanType = _CeaUNIVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1, 1),
    _CeaUNIVlanType_Type()
)
ceaUNIVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceaUNIVlanType.setStatus("current")
_CiscoEthernetAccessMIBConform_ObjectIdentity = ObjectIdentity
ciscoEthernetAccessMIBConform = _CiscoEthernetAccessMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 2)
)
_CEthernetAccessMIBCompliances_ObjectIdentity = ObjectIdentity
cEthernetAccessMIBCompliances = _CEthernetAccessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1)
)
_CEthernetAccessMIBGroups_ObjectIdentity = ObjectIdentity
cEthernetAccessMIBGroups = _CEthernetAccessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2)
)

# Managed Objects groups

ceaPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 1)
)
ceaPortGroup.setObjects(
      *(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxNNIPorts"),
        ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortType"),
        ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortCapability"))
)
if mibBuilder.loadTexts:
    ceaPortGroup.setStatus("current")

ceaVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 2)
)
ceaVlanGroup.setObjects(
      *(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxUNIVlanCommunityPorts"),
        ("CISCO-ETHERNET-ACCESS-MIB", "ceaUNIVlanType"))
)
if mibBuilder.loadTexts:
    ceaVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cEthernetAccessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1, 1)
)
cEthernetAccessMIBCompliance.setObjects(
      *(("CISCO-ETHERNET-ACCESS-MIB", "ceaPortGroup"),
        ("CISCO-ETHERNET-ACCESS-MIB", "ceaVlanGroup"))
)
if mibBuilder.loadTexts:
    cEthernetAccessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ETHERNET-ACCESS-MIB",
    **{"CeaVlanUNIType": CeaVlanUNIType,
       "ciscoEthernetAccessMIB": ciscoEthernetAccessMIB,
       "ciscoEthernetAccessMIBObjects": ciscoEthernetAccessMIBObjects,
       "ceaGlobals": ceaGlobals,
       "ceaMaxNNIPorts": ceaMaxNNIPorts,
       "ceaMaxUNIVlanCommunityPorts": ceaMaxUNIVlanCommunityPorts,
       "ceaConfig": ceaConfig,
       "ceaPortTable": ceaPortTable,
       "ceaPortEntry": ceaPortEntry,
       "ceaPortType": ceaPortType,
       "ceaPortCapability": ceaPortCapability,
       "ceaUNIVlanTable": ceaUNIVlanTable,
       "ceaUNIVlanEntry": ceaUNIVlanEntry,
       "ceaUNIVlanType": ceaUNIVlanType,
       "ciscoEthernetAccessMIBConform": ciscoEthernetAccessMIBConform,
       "cEthernetAccessMIBCompliances": cEthernetAccessMIBCompliances,
       "cEthernetAccessMIBCompliance": cEthernetAccessMIBCompliance,
       "cEthernetAccessMIBGroups": cEthernetAccessMIBGroups,
       "ceaPortGroup": ceaPortGroup,
       "ceaVlanGroup": ceaVlanGroup}
)
