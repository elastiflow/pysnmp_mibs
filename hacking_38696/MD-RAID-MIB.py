# SNMP MIB module (MD-RAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hacking_38696/MD-RAID-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:21:09 2025
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

(hackingExperimental,) = mibBuilder.importSymbols(
    "HACKING-SNMP-MIB",
    "hackingExperimental")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mdRaidMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mdRaidMIB.setRevisions(
        ("2016-10-19 00:00",
         "2011-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MdRaid_ObjectIdentity = ObjectIdentity
mdRaid = _MdRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2)
)
_MdRaidTable_Object = MibTable
mdRaidTable = _MdRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mdRaidTable.setStatus("current")
_MdRaidArrayEntry_Object = MibTableRow
mdRaidArrayEntry = _MdRaidArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1)
)
mdRaidArrayEntry.setIndexNames(
    (0, "MD-RAID-MIB", "mdRaidArrayIndex"),
)
if mibBuilder.loadTexts:
    mdRaidArrayEntry.setStatus("current")


class _MdRaidArrayIndex_Type(Integer32):
    """Custom type mdRaidArrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdRaidArrayIndex_Type.__name__ = "Integer32"
_MdRaidArrayIndex_Object = MibTableColumn
mdRaidArrayIndex = _MdRaidArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 1),
    _MdRaidArrayIndex_Type()
)
mdRaidArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayIndex.setStatus("current")
_MdRaidArrayDev_Type = DisplayString
_MdRaidArrayDev_Object = MibTableColumn
mdRaidArrayDev = _MdRaidArrayDev_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 2),
    _MdRaidArrayDev_Type()
)
mdRaidArrayDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayDev.setStatus("current")
_MdRaidArrayVersion_Type = DisplayString
_MdRaidArrayVersion_Object = MibTableColumn
mdRaidArrayVersion = _MdRaidArrayVersion_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 3),
    _MdRaidArrayVersion_Type()
)
mdRaidArrayVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayVersion.setStatus("current")
_MdRaidArrayUUID_Type = DisplayString
_MdRaidArrayUUID_Object = MibTableColumn
mdRaidArrayUUID = _MdRaidArrayUUID_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 4),
    _MdRaidArrayUUID_Type()
)
mdRaidArrayUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayUUID.setStatus("current")
_MdRaidArrayLevel_Type = DisplayString
_MdRaidArrayLevel_Object = MibTableColumn
mdRaidArrayLevel = _MdRaidArrayLevel_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 5),
    _MdRaidArrayLevel_Type()
)
mdRaidArrayLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayLevel.setStatus("current")
_MdRaidArrayLayout_Type = DisplayString
_MdRaidArrayLayout_Object = MibTableColumn
mdRaidArrayLayout = _MdRaidArrayLayout_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 6),
    _MdRaidArrayLayout_Type()
)
mdRaidArrayLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayLayout.setStatus("current")
_MdRaidArrayChunkSize_Type = DisplayString
_MdRaidArrayChunkSize_Object = MibTableColumn
mdRaidArrayChunkSize = _MdRaidArrayChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 7),
    _MdRaidArrayChunkSize_Type()
)
mdRaidArrayChunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayChunkSize.setStatus("current")
_MdRaidArraySize_Type = DisplayString
_MdRaidArraySize_Object = MibTableColumn
mdRaidArraySize = _MdRaidArraySize_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 8),
    _MdRaidArraySize_Type()
)
mdRaidArraySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArraySize.setStatus("current")
_MdRaidArrayDeviceSize_Type = DisplayString
_MdRaidArrayDeviceSize_Object = MibTableColumn
mdRaidArrayDeviceSize = _MdRaidArrayDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 9),
    _MdRaidArrayDeviceSize_Type()
)
mdRaidArrayDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayDeviceSize.setStatus("current")
_MdRaidArrayHealthOK_Type = TruthValue
_MdRaidArrayHealthOK_Object = MibTableColumn
mdRaidArrayHealthOK = _MdRaidArrayHealthOK_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 10),
    _MdRaidArrayHealthOK_Type()
)
mdRaidArrayHealthOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayHealthOK.setStatus("current")
_MdRaidArrayHasFailedComponents_Type = TruthValue
_MdRaidArrayHasFailedComponents_Object = MibTableColumn
mdRaidArrayHasFailedComponents = _MdRaidArrayHasFailedComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 11),
    _MdRaidArrayHasFailedComponents_Type()
)
mdRaidArrayHasFailedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayHasFailedComponents.setStatus("current")
_MdRaidArrayHasAvailableSpares_Type = TruthValue
_MdRaidArrayHasAvailableSpares_Object = MibTableColumn
mdRaidArrayHasAvailableSpares = _MdRaidArrayHasAvailableSpares_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 12),
    _MdRaidArrayHasAvailableSpares_Type()
)
mdRaidArrayHasAvailableSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayHasAvailableSpares.setStatus("current")
_MdRaidArrayTotalComponents_Type = Gauge32
_MdRaidArrayTotalComponents_Object = MibTableColumn
mdRaidArrayTotalComponents = _MdRaidArrayTotalComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 13),
    _MdRaidArrayTotalComponents_Type()
)
mdRaidArrayTotalComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayTotalComponents.setStatus("current")
_MdRaidArrayActiveComponents_Type = Gauge32
_MdRaidArrayActiveComponents_Object = MibTableColumn
mdRaidArrayActiveComponents = _MdRaidArrayActiveComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 14),
    _MdRaidArrayActiveComponents_Type()
)
mdRaidArrayActiveComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayActiveComponents.setStatus("current")
_MdRaidArrayWorkingComponents_Type = Gauge32
_MdRaidArrayWorkingComponents_Object = MibTableColumn
mdRaidArrayWorkingComponents = _MdRaidArrayWorkingComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 15),
    _MdRaidArrayWorkingComponents_Type()
)
mdRaidArrayWorkingComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayWorkingComponents.setStatus("current")
_MdRaidArrayFailedComponents_Type = Gauge32
_MdRaidArrayFailedComponents_Object = MibTableColumn
mdRaidArrayFailedComponents = _MdRaidArrayFailedComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 16),
    _MdRaidArrayFailedComponents_Type()
)
mdRaidArrayFailedComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayFailedComponents.setStatus("current")
_MdRaidArraySpareComponents_Type = Gauge32
_MdRaidArraySpareComponents_Object = MibTableColumn
mdRaidArraySpareComponents = _MdRaidArraySpareComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 17),
    _MdRaidArraySpareComponents_Type()
)
mdRaidArraySpareComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArraySpareComponents.setStatus("current")
_MdRaidArrayRaidComponents_Type = Gauge32
_MdRaidArrayRaidComponents_Object = MibTableColumn
mdRaidArrayRaidComponents = _MdRaidArrayRaidComponents_Object(
    (1, 3, 6, 1, 4, 1, 38696, 2, 2, 2, 1, 18),
    _MdRaidArrayRaidComponents_Type()
)
mdRaidArrayRaidComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdRaidArrayRaidComponents.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MD-RAID-MIB",
    **{"mdRaid": mdRaid,
       "mdRaidMIB": mdRaidMIB,
       "mdRaidTable": mdRaidTable,
       "mdRaidArrayEntry": mdRaidArrayEntry,
       "mdRaidArrayIndex": mdRaidArrayIndex,
       "mdRaidArrayDev": mdRaidArrayDev,
       "mdRaidArrayVersion": mdRaidArrayVersion,
       "mdRaidArrayUUID": mdRaidArrayUUID,
       "mdRaidArrayLevel": mdRaidArrayLevel,
       "mdRaidArrayLayout": mdRaidArrayLayout,
       "mdRaidArrayChunkSize": mdRaidArrayChunkSize,
       "mdRaidArraySize": mdRaidArraySize,
       "mdRaidArrayDeviceSize": mdRaidArrayDeviceSize,
       "mdRaidArrayHealthOK": mdRaidArrayHealthOK,
       "mdRaidArrayHasFailedComponents": mdRaidArrayHasFailedComponents,
       "mdRaidArrayHasAvailableSpares": mdRaidArrayHasAvailableSpares,
       "mdRaidArrayTotalComponents": mdRaidArrayTotalComponents,
       "mdRaidArrayActiveComponents": mdRaidArrayActiveComponents,
       "mdRaidArrayWorkingComponents": mdRaidArrayWorkingComponents,
       "mdRaidArrayFailedComponents": mdRaidArrayFailedComponents,
       "mdRaidArraySpareComponents": mdRaidArraySpareComponents,
       "mdRaidArrayRaidComponents": mdRaidArrayRaidComponents}
)
