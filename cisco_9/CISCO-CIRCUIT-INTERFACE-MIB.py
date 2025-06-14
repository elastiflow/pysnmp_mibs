# SNMP MIB module (CISCO-CIRCUIT-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CIRCUIT-INTERFACE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:55:31 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCircuitInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 160)
)
if mibBuilder.loadTexts:
    ciscoCircuitInterfaceMIB.setRevisions(
        ("2000-05-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCircuitInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCircuitInterfaceMIBObjects = _CiscoCircuitInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 1)
)
_CciDescription_ObjectIdentity = ObjectIdentity
cciDescription = _CciDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1)
)
_CciDescriptionTable_Object = MibTable
cciDescriptionTable = _CciDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cciDescriptionTable.setStatus("current")
_CciDescriptionEntry_Object = MibTableRow
cciDescriptionEntry = _CciDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1)
)
cciDescriptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cciDescriptionEntry.setStatus("current")


class _CciDescr_Type(SnmpAdminString):
    """Custom type cciDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CciDescr_Type.__name__ = "SnmpAdminString"
_CciDescr_Object = MibTableColumn
cciDescr = _CciDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 1),
    _CciDescr_Type()
)
cciDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cciDescr.setStatus("current")
_CciStatus_Type = RowStatus
_CciStatus_Object = MibTableColumn
cciStatus = _CciStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 2),
    _CciStatus_Type()
)
cciStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cciStatus.setStatus("current")
_CiscoCircuitInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCircuitInterfaceMIBConformance = _CiscoCircuitInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 3)
)
_CiscoCircuitInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCircuitInterfaceMIBCompliances = _CiscoCircuitInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1)
)
_CiscoCircuitInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCircuitInterfaceMIBGroups = _CiscoCircuitInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2)
)

# Managed Objects groups

ciscoCircuitInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2, 1)
)
ciscoCircuitInterfaceGroup.setObjects(
      *(("CISCO-CIRCUIT-INTERFACE-MIB", "cciDescr"),
        ("CISCO-CIRCUIT-INTERFACE-MIB", "cciStatus"))
)
if mibBuilder.loadTexts:
    ciscoCircuitInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCircuitInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1, 1)
)
ciscoCircuitInterfaceMIBCompliance.setObjects(
    ("CISCO-CIRCUIT-INTERFACE-MIB", "ciscoCircuitInterfaceGroup")
)
if mibBuilder.loadTexts:
    ciscoCircuitInterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIRCUIT-INTERFACE-MIB",
    **{"ciscoCircuitInterfaceMIB": ciscoCircuitInterfaceMIB,
       "ciscoCircuitInterfaceMIBObjects": ciscoCircuitInterfaceMIBObjects,
       "cciDescription": cciDescription,
       "cciDescriptionTable": cciDescriptionTable,
       "cciDescriptionEntry": cciDescriptionEntry,
       "cciDescr": cciDescr,
       "cciStatus": cciStatus,
       "ciscoCircuitInterfaceMIBConformance": ciscoCircuitInterfaceMIBConformance,
       "ciscoCircuitInterfaceMIBCompliances": ciscoCircuitInterfaceMIBCompliances,
       "ciscoCircuitInterfaceMIBCompliance": ciscoCircuitInterfaceMIBCompliance,
       "ciscoCircuitInterfaceMIBGroups": ciscoCircuitInterfaceMIBGroups,
       "ciscoCircuitInterfaceGroup": ciscoCircuitInterfaceGroup}
)
