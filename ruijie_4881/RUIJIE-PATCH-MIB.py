# SNMP MIB module (RUIJIE-PATCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PATCH-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

ruijiePatchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151)
)
if mibBuilder.loadTexts:
    ruijiePatchMIB.setRevisions(
        ("2016-09-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiePatchMIBObjects_ObjectIdentity = ObjectIdentity
ruijiePatchMIBObjects = _RuijiePatchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1)
)
_RuijiePatchTable_Object = MibTable
ruijiePatchTable = _RuijiePatchTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiePatchTable.setStatus("current")
_RuijiePatchEntry_Object = MibTableRow
ruijiePatchEntry = _RuijiePatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1)
)
ruijiePatchEntry.setIndexNames(
    (0, "RUIJIE-PATCH-MIB", "ruijiePatchDevIndex"),
    (0, "RUIJIE-PATCH-MIB", "ruijiePatchCmpntIndex"),
)
if mibBuilder.loadTexts:
    ruijiePatchEntry.setStatus("current")
_RuijiePatchDevIndex_Type = Integer32
_RuijiePatchDevIndex_Object = MibTableColumn
ruijiePatchDevIndex = _RuijiePatchDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 1),
    _RuijiePatchDevIndex_Type()
)
ruijiePatchDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchDevIndex.setStatus("current")
_RuijiePatchCmpntIndex_Type = Integer32
_RuijiePatchCmpntIndex_Object = MibTableColumn
ruijiePatchCmpntIndex = _RuijiePatchCmpntIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 2),
    _RuijiePatchCmpntIndex_Type()
)
ruijiePatchCmpntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchCmpntIndex.setStatus("current")
_RuijiePatchDevId_Type = Integer32
_RuijiePatchDevId_Object = MibTableColumn
ruijiePatchDevId = _RuijiePatchDevId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 3),
    _RuijiePatchDevId_Type()
)
ruijiePatchDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchDevId.setStatus("current")
_RuijiePatchSlotId_Type = Integer32
_RuijiePatchSlotId_Object = MibTableColumn
ruijiePatchSlotId = _RuijiePatchSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 4),
    _RuijiePatchSlotId_Type()
)
ruijiePatchSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchSlotId.setStatus("current")
_RuijiePatchCpuId_Type = Integer32
_RuijiePatchCpuId_Object = MibTableColumn
ruijiePatchCpuId = _RuijiePatchCpuId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 5),
    _RuijiePatchCpuId_Type()
)
ruijiePatchCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchCpuId.setStatus("current")
_RuijiePatchExist_Type = DisplayString
_RuijiePatchExist_Object = MibTableColumn
ruijiePatchExist = _RuijiePatchExist_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 6),
    _RuijiePatchExist_Type()
)
ruijiePatchExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchExist.setStatus("current")
_RuijiePatchName_Type = DisplayString
_RuijiePatchName_Object = MibTableColumn
ruijiePatchName = _RuijiePatchName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 7),
    _RuijiePatchName_Type()
)
ruijiePatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchName.setStatus("current")
_RuijiePatchBranch_Type = DisplayString
_RuijiePatchBranch_Object = MibTableColumn
ruijiePatchBranch = _RuijiePatchBranch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 8),
    _RuijiePatchBranch_Type()
)
ruijiePatchBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchBranch.setStatus("current")
_RuijiePatchCmpntName_Type = DisplayString
_RuijiePatchCmpntName_Object = MibTableColumn
ruijiePatchCmpntName = _RuijiePatchCmpntName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 9),
    _RuijiePatchCmpntName_Type()
)
ruijiePatchCmpntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchCmpntName.setStatus("current")
_RuijiePatchSize_Type = Counter64
_RuijiePatchSize_Object = MibTableColumn
ruijiePatchSize = _RuijiePatchSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 10),
    _RuijiePatchSize_Type()
)
ruijiePatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchSize.setStatus("current")
_RuijiePatchStatus_Type = DisplayString
_RuijiePatchStatus_Object = MibTableColumn
ruijiePatchStatus = _RuijiePatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 11),
    _RuijiePatchStatus_Type()
)
ruijiePatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchStatus.setStatus("current")
_RuijiePatchVersion_Type = DisplayString
_RuijiePatchVersion_Object = MibTableColumn
ruijiePatchVersion = _RuijiePatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 12),
    _RuijiePatchVersion_Type()
)
ruijiePatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchVersion.setStatus("current")
_RuijiePatchInstallTime_Type = DisplayString
_RuijiePatchInstallTime_Object = MibTableColumn
ruijiePatchInstallTime = _RuijiePatchInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 13),
    _RuijiePatchInstallTime_Type()
)
ruijiePatchInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchInstallTime.setStatus("current")
_RuijiePatchDescription_Type = DisplayString
_RuijiePatchDescription_Object = MibTableColumn
ruijiePatchDescription = _RuijiePatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 151, 1, 1, 1, 14),
    _RuijiePatchDescription_Type()
)
ruijiePatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePatchDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PATCH-MIB",
    **{"ruijiePatchMIB": ruijiePatchMIB,
       "ruijiePatchMIBObjects": ruijiePatchMIBObjects,
       "ruijiePatchTable": ruijiePatchTable,
       "ruijiePatchEntry": ruijiePatchEntry,
       "ruijiePatchDevIndex": ruijiePatchDevIndex,
       "ruijiePatchCmpntIndex": ruijiePatchCmpntIndex,
       "ruijiePatchDevId": ruijiePatchDevId,
       "ruijiePatchSlotId": ruijiePatchSlotId,
       "ruijiePatchCpuId": ruijiePatchCpuId,
       "ruijiePatchExist": ruijiePatchExist,
       "ruijiePatchName": ruijiePatchName,
       "ruijiePatchBranch": ruijiePatchBranch,
       "ruijiePatchCmpntName": ruijiePatchCmpntName,
       "ruijiePatchSize": ruijiePatchSize,
       "ruijiePatchStatus": ruijiePatchStatus,
       "ruijiePatchVersion": ruijiePatchVersion,
       "ruijiePatchInstallTime": ruijiePatchInstallTime,
       "ruijiePatchDescription": ruijiePatchDescription}
)
