# SNMP MIB module (CISCO-TEMPERATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-TEMPERATURE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:55:06 2025
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

ciscoTempMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 870)
)
if mibBuilder.loadTexts:
    ciscoTempMIB.setRevisions(
        ("2020-05-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTempMIBInformation_ObjectIdentity = ObjectIdentity
ciscoTempMIBInformation = _CiscoTempMIBInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1)
)
_CiscoTempTable_Object = MibTable
ciscoTempTable = _CiscoTempTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTempTable.setStatus("current")
_CiscoTempEntry_Object = MibTableRow
ciscoTempEntry = _CiscoTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1)
)
ciscoTempEntry.setIndexNames(
    (0, "CISCO-TEMPERATURE-MIB", "ciscoTempIndex"),
)
if mibBuilder.loadTexts:
    ciscoTempEntry.setStatus("current")


class _CiscoTempIndex_Type(Integer32):
    """Custom type ciscoTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoTempIndex_Type.__name__ = "Integer32"
_CiscoTempIndex_Object = MibTableColumn
ciscoTempIndex = _CiscoTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 1),
    _CiscoTempIndex_Type()
)
ciscoTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoTempIndex.setStatus("current")
_CiscoTempValue_Type = Unsigned32
_CiscoTempValue_Object = MibTableColumn
ciscoTempValue = _CiscoTempValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 2),
    _CiscoTempValue_Type()
)
ciscoTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTempValue.setStatus("current")
if mibBuilder.loadTexts:
    ciscoTempValue.setUnits("degrees Celsius")
_CiscoTempHyst_Type = Unsigned32
_CiscoTempHyst_Object = MibTableColumn
ciscoTempHyst = _CiscoTempHyst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 3),
    _CiscoTempHyst_Type()
)
ciscoTempHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTempHyst.setStatus("current")
if mibBuilder.loadTexts:
    ciscoTempHyst.setUnits("degrees Celsius")
_CiscoTempOs_Type = Unsigned32
_CiscoTempOs_Object = MibTableColumn
ciscoTempOs = _CiscoTempOs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 1, 1, 1, 4),
    _CiscoTempOs_Type()
)
ciscoTempOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoTempOs.setStatus("current")
if mibBuilder.loadTexts:
    ciscoTempOs.setUnits("degrees Celsius")
_CiscoTempMIBConform_ObjectIdentity = ObjectIdentity
ciscoTempMIBConform = _CiscoTempMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 2)
)
_CiscoTempMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTempMIBCompliances = _CiscoTempMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1)
)
_CiscoTempMIBConformGroups_ObjectIdentity = ObjectIdentity
ciscoTempMIBConformGroups = _CiscoTempMIBConformGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2)
)

# Managed Objects groups

ciscoTempMIBGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 2, 1)
)
ciscoTempMIBGlobalGroup.setObjects(
      *(("CISCO-TEMPERATURE-MIB", "ciscoTempValue"),
        ("CISCO-TEMPERATURE-MIB", "ciscoTempHyst"),
        ("CISCO-TEMPERATURE-MIB", "ciscoTempOs"))
)
if mibBuilder.loadTexts:
    ciscoTempMIBGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTempMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 870, 2, 1, 1)
)
ciscoTempMIBCompliance.setObjects(
    ("CISCO-TEMPERATURE-MIB", "ciscoTempMIBGlobalGroup")
)
if mibBuilder.loadTexts:
    ciscoTempMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TEMPERATURE-MIB",
    **{"ciscoTempMIB": ciscoTempMIB,
       "ciscoTempMIBInformation": ciscoTempMIBInformation,
       "ciscoTempTable": ciscoTempTable,
       "ciscoTempEntry": ciscoTempEntry,
       "ciscoTempIndex": ciscoTempIndex,
       "ciscoTempValue": ciscoTempValue,
       "ciscoTempHyst": ciscoTempHyst,
       "ciscoTempOs": ciscoTempOs,
       "ciscoTempMIBConform": ciscoTempMIBConform,
       "ciscoTempMIBCompliances": ciscoTempMIBCompliances,
       "ciscoTempMIBCompliance": ciscoTempMIBCompliance,
       "ciscoTempMIBConformGroups": ciscoTempMIBConformGroups,
       "ciscoTempMIBGlobalGroup": ciscoTempMIBGlobalGroup}
)
