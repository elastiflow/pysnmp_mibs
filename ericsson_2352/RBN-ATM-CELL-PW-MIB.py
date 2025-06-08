# SNMP MIB module (RBN-ATM-CELL-PW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-ATM-CELL-PW-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:57 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle")

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

rbnAtmCellPWMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41)
)
if mibBuilder.loadTexts:
    rbnAtmCellPWMIB.setRevisions(
        ("2011-01-19 18:00",
         "2007-05-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnAtmCellPWObjects_ObjectIdentity = ObjectIdentity
rbnAtmCellPWObjects = _RbnAtmCellPWObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 1)
)
_RbnAtmCellPWStatTable_Object = MibTable
rbnAtmCellPWStatTable = _RbnAtmCellPWStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmCellPWStatTable.setStatus("current")
_RbnAtmCellPWStatEntry_Object = MibTableRow
rbnAtmCellPWStatEntry = _RbnAtmCellPWStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1)
)
rbnAtmCellPWStatEntry.setIndexNames(
    (0, "RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWCircuitHandle"),
)
if mibBuilder.loadTexts:
    rbnAtmCellPWStatEntry.setStatus("current")
_RbnAtmCellPWCircuitHandle_Type = RbnCircuitHandle
_RbnAtmCellPWCircuitHandle_Object = MibTableColumn
rbnAtmCellPWCircuitHandle = _RbnAtmCellPWCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 1),
    _RbnAtmCellPWCircuitHandle_Type()
)
rbnAtmCellPWCircuitHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmCellPWCircuitHandle.setStatus("current")
_RbnAtmCellPWOutOfSeqDrops_Type = Counter32
_RbnAtmCellPWOutOfSeqDrops_Object = MibTableColumn
rbnAtmCellPWOutOfSeqDrops = _RbnAtmCellPWOutOfSeqDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 2),
    _RbnAtmCellPWOutOfSeqDrops_Type()
)
rbnAtmCellPWOutOfSeqDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtmCellPWOutOfSeqDrops.setStatus("current")
_RbnAtmCellPWCellConcatDrops_Type = Counter32
_RbnAtmCellPWCellConcatDrops_Object = MibTableColumn
rbnAtmCellPWCellConcatDrops = _RbnAtmCellPWCellConcatDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 3),
    _RbnAtmCellPWCellConcatDrops_Type()
)
rbnAtmCellPWCellConcatDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtmCellPWCellConcatDrops.setStatus("current")
_RbnAtmCellPWMIBConformance_ObjectIdentity = ObjectIdentity
rbnAtmCellPWMIBConformance = _RbnAtmCellPWMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 2)
)
_RbnAtmCellPWMIBGroups_ObjectIdentity = ObjectIdentity
rbnAtmCellPWMIBGroups = _RbnAtmCellPWMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 1)
)
_RbnAtmCellPWMIBCompliances_ObjectIdentity = ObjectIdentity
rbnAtmCellPWMIBCompliances = _RbnAtmCellPWMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 2)
)

# Managed Objects groups

rbnAtmCellPWStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 1, 1)
)
rbnAtmCellPWStatGroup.setObjects(
      *(("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWOutOfSeqDrops"),
        ("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWCellConcatDrops"))
)
if mibBuilder.loadTexts:
    rbnAtmCellPWStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnAtmCellPWMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 2, 1)
)
rbnAtmCellPWMIBCompliance.setObjects(
    ("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWStatGroup")
)
if mibBuilder.loadTexts:
    rbnAtmCellPWMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ATM-CELL-PW-MIB",
    **{"rbnAtmCellPWMIB": rbnAtmCellPWMIB,
       "rbnAtmCellPWObjects": rbnAtmCellPWObjects,
       "rbnAtmCellPWStatTable": rbnAtmCellPWStatTable,
       "rbnAtmCellPWStatEntry": rbnAtmCellPWStatEntry,
       "rbnAtmCellPWCircuitHandle": rbnAtmCellPWCircuitHandle,
       "rbnAtmCellPWOutOfSeqDrops": rbnAtmCellPWOutOfSeqDrops,
       "rbnAtmCellPWCellConcatDrops": rbnAtmCellPWCellConcatDrops,
       "rbnAtmCellPWMIBConformance": rbnAtmCellPWMIBConformance,
       "rbnAtmCellPWMIBGroups": rbnAtmCellPWMIBGroups,
       "rbnAtmCellPWStatGroup": rbnAtmCellPWStatGroup,
       "rbnAtmCellPWMIBCompliances": rbnAtmCellPWMIBCompliances,
       "rbnAtmCellPWMIBCompliance": rbnAtmCellPWMIBCompliance}
)
