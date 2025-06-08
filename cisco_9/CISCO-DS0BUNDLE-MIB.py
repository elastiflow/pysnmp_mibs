# SNMP MIB module (CISCO-DS0BUNDLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DS0BUNDLE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:11:57 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

ds0Bundle = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx0BundleNextIndex_Type = TestAndIncr
_Dsx0BundleNextIndex_Object = MibScalar
dsx0BundleNextIndex = _Dsx0BundleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 2),
    _Dsx0BundleNextIndex_Type()
)
dsx0BundleNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0BundleNextIndex.setStatus("current")
_Dsx0BundleTable_Object = MibTable
dsx0BundleTable = _Dsx0BundleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 3)
)
if mibBuilder.loadTexts:
    dsx0BundleTable.setStatus("current")
_Dsx0BundleEntry_Object = MibTableRow
dsx0BundleEntry = _Dsx0BundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1)
)
dsx0BundleEntry.setIndexNames(
    (0, "CISCO-DS0BUNDLE-MIB", "dsx0BundleIndex"),
)
if mibBuilder.loadTexts:
    dsx0BundleEntry.setStatus("current")


class _Dsx0BundleIndex_Type(Integer32):
    """Custom type dsx0BundleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dsx0BundleIndex_Type.__name__ = "Integer32"
_Dsx0BundleIndex_Object = MibTableColumn
dsx0BundleIndex = _Dsx0BundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 1),
    _Dsx0BundleIndex_Type()
)
dsx0BundleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx0BundleIndex.setStatus("current")
_Dsx0BundleIfIndex_Type = InterfaceIndex
_Dsx0BundleIfIndex_Object = MibTableColumn
dsx0BundleIfIndex = _Dsx0BundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 2),
    _Dsx0BundleIfIndex_Type()
)
dsx0BundleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0BundleIfIndex.setStatus("current")
_Dsx0BundleRowStatus_Type = RowStatus
_Dsx0BundleRowStatus_Object = MibTableColumn
dsx0BundleRowStatus = _Dsx0BundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 3),
    _Dsx0BundleRowStatus_Type()
)
dsx0BundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsx0BundleRowStatus.setStatus("current")
_Ds0BundleConformance_ObjectIdentity = ObjectIdentity
ds0BundleConformance = _Ds0BundleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 4)
)
_Ds0BundleGroups_ObjectIdentity = ObjectIdentity
ds0BundleGroups = _Ds0BundleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1)
)
_Ds0BundleCompliances_ObjectIdentity = ObjectIdentity
ds0BundleCompliances = _Ds0BundleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2)
)

# Managed Objects groups

ds0BundleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1, 2)
)
ds0BundleConfigGroup.setObjects(
      *(("CISCO-DS0BUNDLE-MIB", "dsx0BundleNextIndex"),
        ("CISCO-DS0BUNDLE-MIB", "dsx0BundleIfIndex"),
        ("CISCO-DS0BUNDLE-MIB", "dsx0BundleRowStatus"))
)
if mibBuilder.loadTexts:
    ds0BundleConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ds0BundleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2, 1)
)
ds0BundleCompliance.setObjects(
    ("CISCO-DS0BUNDLE-MIB", "ds0BundleConfigGroup")
)
if mibBuilder.loadTexts:
    ds0BundleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS0BUNDLE-MIB",
    **{"ds0Bundle": ds0Bundle,
       "dsx0BundleNextIndex": dsx0BundleNextIndex,
       "dsx0BundleTable": dsx0BundleTable,
       "dsx0BundleEntry": dsx0BundleEntry,
       "dsx0BundleIndex": dsx0BundleIndex,
       "dsx0BundleIfIndex": dsx0BundleIfIndex,
       "dsx0BundleRowStatus": dsx0BundleRowStatus,
       "ds0BundleConformance": ds0BundleConformance,
       "ds0BundleGroups": ds0BundleGroups,
       "ds0BundleConfigGroup": ds0BundleConfigGroup,
       "ds0BundleCompliances": ds0BundleCompliances,
       "ds0BundleCompliance": ds0BundleCompliance}
)
