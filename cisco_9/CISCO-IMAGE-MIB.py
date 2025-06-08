# SNMP MIB module (CISCO-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IMAGE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:28 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DisplayString,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoImageMIB_ObjectIdentity = ObjectIdentity
ciscoImageMIB = _CiscoImageMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25)
)
_CiscoImageMIBObjects_ObjectIdentity = ObjectIdentity
ciscoImageMIBObjects = _CiscoImageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1)
)
_CiscoImageTable_Object = MibTable
ciscoImageTable = _CiscoImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoImageTable.setStatus("mandatory")
_CiscoImageEntry_Object = MibTableRow
ciscoImageEntry = _CiscoImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1)
)
ciscoImageEntry.setIndexNames(
    (0, "CISCO-IMAGE-MIB", "ciscoImageIndex"),
)
if mibBuilder.loadTexts:
    ciscoImageEntry.setStatus("mandatory")


class _CiscoImageIndex_Type(Integer32):
    """Custom type ciscoImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoImageIndex_Type.__name__ = "Integer32"
_CiscoImageIndex_Object = MibTableColumn
ciscoImageIndex = _CiscoImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1),
    _CiscoImageIndex_Type()
)
ciscoImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoImageIndex.setStatus("mandatory")
_CiscoImageString_Type = DisplayString
_CiscoImageString_Object = MibTableColumn
ciscoImageString = _CiscoImageString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2),
    _CiscoImageString_Type()
)
ciscoImageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImageString.setStatus("mandatory")
_CiscoImageMIBConformance_ObjectIdentity = ObjectIdentity
ciscoImageMIBConformance = _CiscoImageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2)
)
_CiscoImageMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoImageMIBCompliances = _CiscoImageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1)
)
_CiscoImageMIBCompliance_ObjectIdentity = ObjectIdentity
ciscoImageMIBCompliance = _CiscoImageMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)
)
_CiscoImageMIBGroups_ObjectIdentity = ObjectIdentity
ciscoImageMIBGroups = _CiscoImageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2)
)
_CiscoImageMIBGroup_ObjectIdentity = ObjectIdentity
ciscoImageMIBGroup = _CiscoImageMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMAGE-MIB",
    **{"ciscoImageMIB": ciscoImageMIB,
       "ciscoImageMIBObjects": ciscoImageMIBObjects,
       "ciscoImageTable": ciscoImageTable,
       "ciscoImageEntry": ciscoImageEntry,
       "ciscoImageIndex": ciscoImageIndex,
       "ciscoImageString": ciscoImageString,
       "ciscoImageMIBConformance": ciscoImageMIBConformance,
       "ciscoImageMIBCompliances": ciscoImageMIBCompliances,
       "ciscoImageMIBCompliance": ciscoImageMIBCompliance,
       "ciscoImageMIBGroups": ciscoImageMIBGroups,
       "ciscoImageMIBGroup": ciscoImageMIBGroup}
)
