# SNMP MIB module (RUIJIE-CMPNT-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CMPNT-UPGRADE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieCmpntPatchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162)
)
if mibBuilder.loadTexts:
    ruijieCmpntPatchMIB.setRevisions(
        ("2019-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCmpntPatchMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCmpntPatchMIBObjects = _RuijieCmpntPatchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1)
)
_RuijieCmpntPatchTable_Object = MibTable
ruijieCmpntPatchTable = _RuijieCmpntPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieCmpntPatchTable.setStatus("current")
_RuijieCmpntPatchEntry_Object = MibTableRow
ruijieCmpntPatchEntry = _RuijieCmpntPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1)
)
ruijieCmpntPatchEntry.setIndexNames(
    (0, "RUIJIE-CMPNT-UPGRADE-MIB", "ruijieCmpntDevIndex"),
    (0, "RUIJIE-CMPNT-UPGRADE-MIB", "ruijieCmpntPatchIndex"),
)
if mibBuilder.loadTexts:
    ruijieCmpntPatchEntry.setStatus("current")
_RuijieCmpntDevIndex_Type = Integer32
_RuijieCmpntDevIndex_Object = MibTableColumn
ruijieCmpntDevIndex = _RuijieCmpntDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 1),
    _RuijieCmpntDevIndex_Type()
)
ruijieCmpntDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntDevIndex.setStatus("current")
_RuijieCmpntPatchIndex_Type = Integer32
_RuijieCmpntPatchIndex_Object = MibTableColumn
ruijieCmpntPatchIndex = _RuijieCmpntPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 2),
    _RuijieCmpntPatchIndex_Type()
)
ruijieCmpntPatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchIndex.setStatus("current")
_RuijieCmpntPatchDevId_Type = Integer32
_RuijieCmpntPatchDevId_Object = MibTableColumn
ruijieCmpntPatchDevId = _RuijieCmpntPatchDevId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 3),
    _RuijieCmpntPatchDevId_Type()
)
ruijieCmpntPatchDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchDevId.setStatus("current")
_RuijieCmpntPatchSlotId_Type = Integer32
_RuijieCmpntPatchSlotId_Object = MibTableColumn
ruijieCmpntPatchSlotId = _RuijieCmpntPatchSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 4),
    _RuijieCmpntPatchSlotId_Type()
)
ruijieCmpntPatchSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchSlotId.setStatus("current")
_RuijieCmpntPatchCpuId_Type = Integer32
_RuijieCmpntPatchCpuId_Object = MibTableColumn
ruijieCmpntPatchCpuId = _RuijieCmpntPatchCpuId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 5),
    _RuijieCmpntPatchCpuId_Type()
)
ruijieCmpntPatchCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchCpuId.setStatus("current")
_RuijieCmpntPatchName_Type = DisplayString
_RuijieCmpntPatchName_Object = MibTableColumn
ruijieCmpntPatchName = _RuijieCmpntPatchName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 6),
    _RuijieCmpntPatchName_Type()
)
ruijieCmpntPatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchName.setStatus("current")
_RuijieCmpntPatchStatus_Type = DisplayString
_RuijieCmpntPatchStatus_Object = MibTableColumn
ruijieCmpntPatchStatus = _RuijieCmpntPatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 7),
    _RuijieCmpntPatchStatus_Type()
)
ruijieCmpntPatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchStatus.setStatus("current")
_RuijieCmpntPatchFlag_Type = DisplayString
_RuijieCmpntPatchFlag_Object = MibTableColumn
ruijieCmpntPatchFlag = _RuijieCmpntPatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 8),
    _RuijieCmpntPatchFlag_Type()
)
ruijieCmpntPatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchFlag.setStatus("current")
_RuijieCmpntPatchDesc_Type = DisplayString
_RuijieCmpntPatchDesc_Object = MibTableColumn
ruijieCmpntPatchDesc = _RuijieCmpntPatchDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 162, 1, 1, 1, 9),
    _RuijieCmpntPatchDesc_Type()
)
ruijieCmpntPatchDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCmpntPatchDesc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CMPNT-UPGRADE-MIB",
    **{"ruijieCmpntPatchMIB": ruijieCmpntPatchMIB,
       "ruijieCmpntPatchMIBObjects": ruijieCmpntPatchMIBObjects,
       "ruijieCmpntPatchTable": ruijieCmpntPatchTable,
       "ruijieCmpntPatchEntry": ruijieCmpntPatchEntry,
       "ruijieCmpntDevIndex": ruijieCmpntDevIndex,
       "ruijieCmpntPatchIndex": ruijieCmpntPatchIndex,
       "ruijieCmpntPatchDevId": ruijieCmpntPatchDevId,
       "ruijieCmpntPatchSlotId": ruijieCmpntPatchSlotId,
       "ruijieCmpntPatchCpuId": ruijieCmpntPatchCpuId,
       "ruijieCmpntPatchName": ruijieCmpntPatchName,
       "ruijieCmpntPatchStatus": ruijieCmpntPatchStatus,
       "ruijieCmpntPatchFlag": ruijieCmpntPatchFlag,
       "ruijieCmpntPatchDesc": ruijieCmpntPatchDesc}
)
