# SNMP MIB module (CISCO-FIREPOWER-AP-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-POWER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApPolicyPolicyOwner,
 CfprApPowerCapAction,
 CfprApPowerChThrAction,
 CfprApPowerGroupState,
 CfprApPowerGroupStatsHistThresholded,
 CfprApPowerGroupStatsThresholded,
 CfprApPowerLockState,
 CfprApPowerMemberState,
 CfprApPowerMgmtStyle,
 CfprApPowerOperState,
 CfprApPowerPrioritySharing,
 CfprApPowerProfilingMethod,
 CfprApPowerPsuLineMode,
 CfprApPowerPsuState,
 CfprApPowerReallocation,
 CfprApPowerReqConflict) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApPolicyPolicyOwner",
    "CfprApPowerCapAction",
    "CfprApPowerChThrAction",
    "CfprApPowerGroupState",
    "CfprApPowerGroupStatsHistThresholded",
    "CfprApPowerGroupStatsThresholded",
    "CfprApPowerLockState",
    "CfprApPowerMemberState",
    "CfprApPowerMgmtStyle",
    "CfprApPowerOperState",
    "CfprApPowerPrioritySharing",
    "CfprApPowerProfilingMethod",
    "CfprApPowerPsuLineMode",
    "CfprApPowerPsuState",
    "CfprApPowerReallocation",
    "CfprApPowerReqConflict")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprApPowerObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApPowerBudgetTable_Object = MibTable
cfprApPowerBudgetTable = _CfprApPowerBudgetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1)
)
if mibBuilder.loadTexts:
    cfprApPowerBudgetTable.setStatus("current")
_CfprApPowerBudgetEntry_Object = MibTableRow
cfprApPowerBudgetEntry = _CfprApPowerBudgetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1)
)
cfprApPowerBudgetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerBudgetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerBudgetEntry.setStatus("current")
_CfprApPowerBudgetInstanceId_Type = CfprApManagedObjectId
_CfprApPowerBudgetInstanceId_Object = MibTableColumn
cfprApPowerBudgetInstanceId = _CfprApPowerBudgetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 1),
    _CfprApPowerBudgetInstanceId_Type()
)
cfprApPowerBudgetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerBudgetInstanceId.setStatus("current")
_CfprApPowerBudgetDn_Type = CfprApManagedObjectDn
_CfprApPowerBudgetDn_Object = MibTableColumn
cfprApPowerBudgetDn = _CfprApPowerBudgetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 2),
    _CfprApPowerBudgetDn_Type()
)
cfprApPowerBudgetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetDn.setStatus("current")
_CfprApPowerBudgetRn_Type = SnmpAdminString
_CfprApPowerBudgetRn_Object = MibTableColumn
cfprApPowerBudgetRn = _CfprApPowerBudgetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 3),
    _CfprApPowerBudgetRn_Type()
)
cfprApPowerBudgetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetRn.setStatus("current")
_CfprApPowerBudgetAdminCommitted_Type = Gauge32
_CfprApPowerBudgetAdminCommitted_Object = MibTableColumn
cfprApPowerBudgetAdminCommitted = _CfprApPowerBudgetAdminCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 4),
    _CfprApPowerBudgetAdminCommitted_Type()
)
cfprApPowerBudgetAdminCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetAdminCommitted.setStatus("current")
_CfprApPowerBudgetAdminFPLockState_Type = CfprApPowerLockState
_CfprApPowerBudgetAdminFPLockState_Object = MibTableColumn
cfprApPowerBudgetAdminFPLockState = _CfprApPowerBudgetAdminFPLockState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 5),
    _CfprApPowerBudgetAdminFPLockState_Type()
)
cfprApPowerBudgetAdminFPLockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetAdminFPLockState.setStatus("current")
_CfprApPowerBudgetAdminPeak_Type = Gauge32
_CfprApPowerBudgetAdminPeak_Object = MibTableColumn
cfprApPowerBudgetAdminPeak = _CfprApPowerBudgetAdminPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 6),
    _CfprApPowerBudgetAdminPeak_Type()
)
cfprApPowerBudgetAdminPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetAdminPeak.setStatus("current")
_CfprApPowerBudgetAdminPeakNew_Type = Gauge32
_CfprApPowerBudgetAdminPeakNew_Object = MibTableColumn
cfprApPowerBudgetAdminPeakNew = _CfprApPowerBudgetAdminPeakNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 7),
    _CfprApPowerBudgetAdminPeakNew_Type()
)
cfprApPowerBudgetAdminPeakNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetAdminPeakNew.setStatus("current")
_CfprApPowerBudgetBootPower_Type = Gauge32
_CfprApPowerBudgetBootPower_Object = MibTableColumn
cfprApPowerBudgetBootPower = _CfprApPowerBudgetBootPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 8),
    _CfprApPowerBudgetBootPower_Type()
)
cfprApPowerBudgetBootPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetBootPower.setStatus("current")
_CfprApPowerBudgetCapAction_Type = CfprApPowerCapAction
_CfprApPowerBudgetCapAction_Object = MibTableColumn
cfprApPowerBudgetCapAction = _CfprApPowerBudgetCapAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 9),
    _CfprApPowerBudgetCapAction_Type()
)
cfprApPowerBudgetCapAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetCapAction.setStatus("current")
_CfprApPowerBudgetCatalogPower_Type = Gauge32
_CfprApPowerBudgetCatalogPower_Object = MibTableColumn
cfprApPowerBudgetCatalogPower = _CfprApPowerBudgetCatalogPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 10),
    _CfprApPowerBudgetCatalogPower_Type()
)
cfprApPowerBudgetCatalogPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetCatalogPower.setStatus("current")
_CfprApPowerBudgetChRsrvdPower_Type = Gauge32
_CfprApPowerBudgetChRsrvdPower_Object = MibTableColumn
cfprApPowerBudgetChRsrvdPower = _CfprApPowerBudgetChRsrvdPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 11),
    _CfprApPowerBudgetChRsrvdPower_Type()
)
cfprApPowerBudgetChRsrvdPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetChRsrvdPower.setStatus("current")
_CfprApPowerBudgetCurrentPower_Type = Gauge32
_CfprApPowerBudgetCurrentPower_Object = MibTableColumn
cfprApPowerBudgetCurrentPower = _CfprApPowerBudgetCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 12),
    _CfprApPowerBudgetCurrentPower_Type()
)
cfprApPowerBudgetCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetCurrentPower.setStatus("current")
_CfprApPowerBudgetDynRealloc_Type = CfprApPowerReallocation
_CfprApPowerBudgetDynRealloc_Object = MibTableColumn
cfprApPowerBudgetDynRealloc = _CfprApPowerBudgetDynRealloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 13),
    _CfprApPowerBudgetDynRealloc_Type()
)
cfprApPowerBudgetDynRealloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetDynRealloc.setStatus("current")
_CfprApPowerBudgetGroupName_Type = SnmpAdminString
_CfprApPowerBudgetGroupName_Object = MibTableColumn
cfprApPowerBudgetGroupName = _CfprApPowerBudgetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 14),
    _CfprApPowerBudgetGroupName_Type()
)
cfprApPowerBudgetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetGroupName.setStatus("current")
_CfprApPowerBudgetIdlePower_Type = Gauge32
_CfprApPowerBudgetIdlePower_Object = MibTableColumn
cfprApPowerBudgetIdlePower = _CfprApPowerBudgetIdlePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 15),
    _CfprApPowerBudgetIdlePower_Type()
)
cfprApPowerBudgetIdlePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetIdlePower.setStatus("current")
_CfprApPowerBudgetMaxPower_Type = Gauge32
_CfprApPowerBudgetMaxPower_Object = MibTableColumn
cfprApPowerBudgetMaxPower = _CfprApPowerBudgetMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 16),
    _CfprApPowerBudgetMaxPower_Type()
)
cfprApPowerBudgetMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetMaxPower.setStatus("current")
_CfprApPowerBudgetMinPower_Type = Gauge32
_CfprApPowerBudgetMinPower_Object = MibTableColumn
cfprApPowerBudgetMinPower = _CfprApPowerBudgetMinPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 17),
    _CfprApPowerBudgetMinPower_Type()
)
cfprApPowerBudgetMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetMinPower.setStatus("current")
_CfprApPowerBudgetOperCommitted_Type = Gauge32
_CfprApPowerBudgetOperCommitted_Object = MibTableColumn
cfprApPowerBudgetOperCommitted = _CfprApPowerBudgetOperCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 18),
    _CfprApPowerBudgetOperCommitted_Type()
)
cfprApPowerBudgetOperCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetOperCommitted.setStatus("current")
_CfprApPowerBudgetOperFPLockState_Type = CfprApPowerLockState
_CfprApPowerBudgetOperFPLockState_Object = MibTableColumn
cfprApPowerBudgetOperFPLockState = _CfprApPowerBudgetOperFPLockState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 19),
    _CfprApPowerBudgetOperFPLockState_Type()
)
cfprApPowerBudgetOperFPLockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetOperFPLockState.setStatus("current")
_CfprApPowerBudgetOperMin_Type = Gauge32
_CfprApPowerBudgetOperMin_Object = MibTableColumn
cfprApPowerBudgetOperMin = _CfprApPowerBudgetOperMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 20),
    _CfprApPowerBudgetOperMin_Type()
)
cfprApPowerBudgetOperMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetOperMin.setStatus("current")
_CfprApPowerBudgetOperPeak_Type = Gauge32
_CfprApPowerBudgetOperPeak_Object = MibTableColumn
cfprApPowerBudgetOperPeak = _CfprApPowerBudgetOperPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 21),
    _CfprApPowerBudgetOperPeak_Type()
)
cfprApPowerBudgetOperPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetOperPeak.setStatus("current")
_CfprApPowerBudgetOperProfMethod_Type = CfprApPowerProfilingMethod
_CfprApPowerBudgetOperProfMethod_Object = MibTableColumn
cfprApPowerBudgetOperProfMethod = _CfprApPowerBudgetOperProfMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 22),
    _CfprApPowerBudgetOperProfMethod_Type()
)
cfprApPowerBudgetOperProfMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetOperProfMethod.setStatus("current")
_CfprApPowerBudgetOperState_Type = CfprApPowerOperState
_CfprApPowerBudgetOperState_Object = MibTableColumn
cfprApPowerBudgetOperState = _CfprApPowerBudgetOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 23),
    _CfprApPowerBudgetOperState_Type()
)
cfprApPowerBudgetOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetOperState.setStatus("current")
_CfprApPowerBudgetPrio_Type = Gauge32
_CfprApPowerBudgetPrio_Object = MibTableColumn
cfprApPowerBudgetPrio = _CfprApPowerBudgetPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 24),
    _CfprApPowerBudgetPrio_Type()
)
cfprApPowerBudgetPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetPrio.setStatus("current")
_CfprApPowerBudgetProfMethod_Type = CfprApPowerProfilingMethod
_CfprApPowerBudgetProfMethod_Object = MibTableColumn
cfprApPowerBudgetProfMethod = _CfprApPowerBudgetProfMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 25),
    _CfprApPowerBudgetProfMethod_Type()
)
cfprApPowerBudgetProfMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetProfMethod.setStatus("current")
_CfprApPowerBudgetProfiling_Type = TruthValue
_CfprApPowerBudgetProfiling_Object = MibTableColumn
cfprApPowerBudgetProfiling = _CfprApPowerBudgetProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 26),
    _CfprApPowerBudgetProfiling_Type()
)
cfprApPowerBudgetProfiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetProfiling.setStatus("current")
_CfprApPowerBudgetPsuCapacity_Type = Gauge32
_CfprApPowerBudgetPsuCapacity_Object = MibTableColumn
cfprApPowerBudgetPsuCapacity = _CfprApPowerBudgetPsuCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 27),
    _CfprApPowerBudgetPsuCapacity_Type()
)
cfprApPowerBudgetPsuCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetPsuCapacity.setStatus("current")
_CfprApPowerBudgetPsuLineMode_Type = CfprApPowerPsuLineMode
_CfprApPowerBudgetPsuLineMode_Object = MibTableColumn
cfprApPowerBudgetPsuLineMode = _CfprApPowerBudgetPsuLineMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 28),
    _CfprApPowerBudgetPsuLineMode_Type()
)
cfprApPowerBudgetPsuLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetPsuLineMode.setStatus("current")
_CfprApPowerBudgetPsuState_Type = CfprApPowerPsuState
_CfprApPowerBudgetPsuState_Object = MibTableColumn
cfprApPowerBudgetPsuState = _CfprApPowerBudgetPsuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 29),
    _CfprApPowerBudgetPsuState_Type()
)
cfprApPowerBudgetPsuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetPsuState.setStatus("current")
_CfprApPowerBudgetScaledWt_Type = Gauge32
_CfprApPowerBudgetScaledWt_Object = MibTableColumn
cfprApPowerBudgetScaledWt = _CfprApPowerBudgetScaledWt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 30),
    _CfprApPowerBudgetScaledWt_Type()
)
cfprApPowerBudgetScaledWt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetScaledWt.setStatus("current")
_CfprApPowerBudgetStyle_Type = CfprApPowerMgmtStyle
_CfprApPowerBudgetStyle_Object = MibTableColumn
cfprApPowerBudgetStyle = _CfprApPowerBudgetStyle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 31),
    _CfprApPowerBudgetStyle_Type()
)
cfprApPowerBudgetStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetStyle.setStatus("current")
_CfprApPowerBudgetUpdateTime_Type = DateAndTime
_CfprApPowerBudgetUpdateTime_Object = MibTableColumn
cfprApPowerBudgetUpdateTime = _CfprApPowerBudgetUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 32),
    _CfprApPowerBudgetUpdateTime_Type()
)
cfprApPowerBudgetUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetUpdateTime.setStatus("current")
_CfprApPowerBudgetWeight_Type = Gauge32
_CfprApPowerBudgetWeight_Object = MibTableColumn
cfprApPowerBudgetWeight = _CfprApPowerBudgetWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 1, 1, 33),
    _CfprApPowerBudgetWeight_Type()
)
cfprApPowerBudgetWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerBudgetWeight.setStatus("current")
_CfprApPowerChassisMemberTable_Object = MibTable
cfprApPowerChassisMemberTable = _CfprApPowerChassisMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2)
)
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberTable.setStatus("current")
_CfprApPowerChassisMemberEntry_Object = MibTableRow
cfprApPowerChassisMemberEntry = _CfprApPowerChassisMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2, 1)
)
cfprApPowerChassisMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerChassisMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberEntry.setStatus("current")
_CfprApPowerChassisMemberInstanceId_Type = CfprApManagedObjectId
_CfprApPowerChassisMemberInstanceId_Object = MibTableColumn
cfprApPowerChassisMemberInstanceId = _CfprApPowerChassisMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2, 1, 1),
    _CfprApPowerChassisMemberInstanceId_Type()
)
cfprApPowerChassisMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberInstanceId.setStatus("current")
_CfprApPowerChassisMemberDn_Type = CfprApManagedObjectDn
_CfprApPowerChassisMemberDn_Object = MibTableColumn
cfprApPowerChassisMemberDn = _CfprApPowerChassisMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2, 1, 2),
    _CfprApPowerChassisMemberDn_Type()
)
cfprApPowerChassisMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberDn.setStatus("current")
_CfprApPowerChassisMemberRn_Type = SnmpAdminString
_CfprApPowerChassisMemberRn_Object = MibTableColumn
cfprApPowerChassisMemberRn = _CfprApPowerChassisMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2, 1, 3),
    _CfprApPowerChassisMemberRn_Type()
)
cfprApPowerChassisMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberRn.setStatus("current")
_CfprApPowerChassisMemberId_Type = Gauge32
_CfprApPowerChassisMemberId_Object = MibTableColumn
cfprApPowerChassisMemberId = _CfprApPowerChassisMemberId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2, 1, 4),
    _CfprApPowerChassisMemberId_Type()
)
cfprApPowerChassisMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberId.setStatus("current")
_CfprApPowerChassisMemberOperState_Type = CfprApPowerMemberState
_CfprApPowerChassisMemberOperState_Object = MibTableColumn
cfprApPowerChassisMemberOperState = _CfprApPowerChassisMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 2, 1, 5),
    _CfprApPowerChassisMemberOperState_Type()
)
cfprApPowerChassisMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerChassisMemberOperState.setStatus("current")
_CfprApPowerEpTable_Object = MibTable
cfprApPowerEpTable = _CfprApPowerEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 3)
)
if mibBuilder.loadTexts:
    cfprApPowerEpTable.setStatus("current")
_CfprApPowerEpEntry_Object = MibTableRow
cfprApPowerEpEntry = _CfprApPowerEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 3, 1)
)
cfprApPowerEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerEpEntry.setStatus("current")
_CfprApPowerEpInstanceId_Type = CfprApManagedObjectId
_CfprApPowerEpInstanceId_Object = MibTableColumn
cfprApPowerEpInstanceId = _CfprApPowerEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 3, 1, 1),
    _CfprApPowerEpInstanceId_Type()
)
cfprApPowerEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerEpInstanceId.setStatus("current")
_CfprApPowerEpDn_Type = CfprApManagedObjectDn
_CfprApPowerEpDn_Object = MibTableColumn
cfprApPowerEpDn = _CfprApPowerEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 3, 1, 2),
    _CfprApPowerEpDn_Type()
)
cfprApPowerEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerEpDn.setStatus("current")
_CfprApPowerEpRn_Type = SnmpAdminString
_CfprApPowerEpRn_Object = MibTableColumn
cfprApPowerEpRn = _CfprApPowerEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 3, 1, 3),
    _CfprApPowerEpRn_Type()
)
cfprApPowerEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerEpRn.setStatus("current")
_CfprApPowerGroupTable_Object = MibTable
cfprApPowerGroupTable = _CfprApPowerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4)
)
if mibBuilder.loadTexts:
    cfprApPowerGroupTable.setStatus("current")
_CfprApPowerGroupEntry_Object = MibTableRow
cfprApPowerGroupEntry = _CfprApPowerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1)
)
cfprApPowerGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerGroupEntry.setStatus("current")
_CfprApPowerGroupInstanceId_Type = CfprApManagedObjectId
_CfprApPowerGroupInstanceId_Object = MibTableColumn
cfprApPowerGroupInstanceId = _CfprApPowerGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 1),
    _CfprApPowerGroupInstanceId_Type()
)
cfprApPowerGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerGroupInstanceId.setStatus("current")
_CfprApPowerGroupDn_Type = CfprApManagedObjectDn
_CfprApPowerGroupDn_Object = MibTableColumn
cfprApPowerGroupDn = _CfprApPowerGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 2),
    _CfprApPowerGroupDn_Type()
)
cfprApPowerGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupDn.setStatus("current")
_CfprApPowerGroupRn_Type = SnmpAdminString
_CfprApPowerGroupRn_Object = MibTableColumn
cfprApPowerGroupRn = _CfprApPowerGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 3),
    _CfprApPowerGroupRn_Type()
)
cfprApPowerGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupRn.setStatus("current")
_CfprApPowerGroupAdminCommitted_Type = Gauge32
_CfprApPowerGroupAdminCommitted_Object = MibTableColumn
cfprApPowerGroupAdminCommitted = _CfprApPowerGroupAdminCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 4),
    _CfprApPowerGroupAdminCommitted_Type()
)
cfprApPowerGroupAdminCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdminCommitted.setStatus("current")
_CfprApPowerGroupAdminPeak_Type = Gauge32
_CfprApPowerGroupAdminPeak_Object = MibTableColumn
cfprApPowerGroupAdminPeak = _CfprApPowerGroupAdminPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 5),
    _CfprApPowerGroupAdminPeak_Type()
)
cfprApPowerGroupAdminPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdminPeak.setStatus("current")
_CfprApPowerGroupCurReqPower_Type = Gauge32
_CfprApPowerGroupCurReqPower_Object = MibTableColumn
cfprApPowerGroupCurReqPower = _CfprApPowerGroupCurReqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 6),
    _CfprApPowerGroupCurReqPower_Type()
)
cfprApPowerGroupCurReqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupCurReqPower.setStatus("current")
_CfprApPowerGroupCurrentPower_Type = Gauge32
_CfprApPowerGroupCurrentPower_Object = MibTableColumn
cfprApPowerGroupCurrentPower = _CfprApPowerGroupCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 7),
    _CfprApPowerGroupCurrentPower_Type()
)
cfprApPowerGroupCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupCurrentPower.setStatus("current")
_CfprApPowerGroupDescr_Type = SnmpAdminString
_CfprApPowerGroupDescr_Object = MibTableColumn
cfprApPowerGroupDescr = _CfprApPowerGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 8),
    _CfprApPowerGroupDescr_Type()
)
cfprApPowerGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupDescr.setStatus("current")
_CfprApPowerGroupFltAggr_Type = Unsigned64
_CfprApPowerGroupFltAggr_Object = MibTableColumn
cfprApPowerGroupFltAggr = _CfprApPowerGroupFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 9),
    _CfprApPowerGroupFltAggr_Type()
)
cfprApPowerGroupFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupFltAggr.setStatus("current")
_CfprApPowerGroupIntId_Type = SnmpAdminString
_CfprApPowerGroupIntId_Object = MibTableColumn
cfprApPowerGroupIntId = _CfprApPowerGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 10),
    _CfprApPowerGroupIntId_Type()
)
cfprApPowerGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupIntId.setStatus("current")
_CfprApPowerGroupMinReqPower_Type = Gauge32
_CfprApPowerGroupMinReqPower_Object = MibTableColumn
cfprApPowerGroupMinReqPower = _CfprApPowerGroupMinReqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 11),
    _CfprApPowerGroupMinReqPower_Type()
)
cfprApPowerGroupMinReqPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupMinReqPower.setStatus("current")
_CfprApPowerGroupName_Type = SnmpAdminString
_CfprApPowerGroupName_Object = MibTableColumn
cfprApPowerGroupName = _CfprApPowerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 12),
    _CfprApPowerGroupName_Type()
)
cfprApPowerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupName.setStatus("current")
_CfprApPowerGroupOperCommitted_Type = Gauge32
_CfprApPowerGroupOperCommitted_Object = MibTableColumn
cfprApPowerGroupOperCommitted = _CfprApPowerGroupOperCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 13),
    _CfprApPowerGroupOperCommitted_Type()
)
cfprApPowerGroupOperCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupOperCommitted.setStatus("current")
_CfprApPowerGroupOperPeak_Type = Gauge32
_CfprApPowerGroupOperPeak_Object = MibTableColumn
cfprApPowerGroupOperPeak = _CfprApPowerGroupOperPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 14),
    _CfprApPowerGroupOperPeak_Type()
)
cfprApPowerGroupOperPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupOperPeak.setStatus("current")
_CfprApPowerGroupOperState_Type = CfprApPowerGroupState
_CfprApPowerGroupOperState_Object = MibTableColumn
cfprApPowerGroupOperState = _CfprApPowerGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 15),
    _CfprApPowerGroupOperState_Type()
)
cfprApPowerGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupOperState.setStatus("current")
_CfprApPowerGroupPolicyLevel_Type = Gauge32
_CfprApPowerGroupPolicyLevel_Object = MibTableColumn
cfprApPowerGroupPolicyLevel = _CfprApPowerGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 16),
    _CfprApPowerGroupPolicyLevel_Type()
)
cfprApPowerGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupPolicyLevel.setStatus("current")
_CfprApPowerGroupPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPowerGroupPolicyOwner_Object = MibTableColumn
cfprApPowerGroupPolicyOwner = _CfprApPowerGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 17),
    _CfprApPowerGroupPolicyOwner_Type()
)
cfprApPowerGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupPolicyOwner.setStatus("current")
_CfprApPowerGroupQualifier_Type = SnmpAdminString
_CfprApPowerGroupQualifier_Object = MibTableColumn
cfprApPowerGroupQualifier = _CfprApPowerGroupQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 18),
    _CfprApPowerGroupQualifier_Type()
)
cfprApPowerGroupQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupQualifier.setStatus("current")
_CfprApPowerGroupRealloc_Type = CfprApPowerReallocation
_CfprApPowerGroupRealloc_Object = MibTableColumn
cfprApPowerGroupRealloc = _CfprApPowerGroupRealloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 4, 1, 19),
    _CfprApPowerGroupRealloc_Type()
)
cfprApPowerGroupRealloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupRealloc.setStatus("current")
_CfprApPowerGroupAdditionPolicyTable_Object = MibTable
cfprApPowerGroupAdditionPolicyTable = _CfprApPowerGroupAdditionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5)
)
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyTable.setStatus("current")
_CfprApPowerGroupAdditionPolicyEntry_Object = MibTableRow
cfprApPowerGroupAdditionPolicyEntry = _CfprApPowerGroupAdditionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1)
)
cfprApPowerGroupAdditionPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerGroupAdditionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyEntry.setStatus("current")
_CfprApPowerGroupAdditionPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApPowerGroupAdditionPolicyInstanceId_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyInstanceId = _CfprApPowerGroupAdditionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 1),
    _CfprApPowerGroupAdditionPolicyInstanceId_Type()
)
cfprApPowerGroupAdditionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyInstanceId.setStatus("current")
_CfprApPowerGroupAdditionPolicyDn_Type = CfprApManagedObjectDn
_CfprApPowerGroupAdditionPolicyDn_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyDn = _CfprApPowerGroupAdditionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 2),
    _CfprApPowerGroupAdditionPolicyDn_Type()
)
cfprApPowerGroupAdditionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyDn.setStatus("current")
_CfprApPowerGroupAdditionPolicyRn_Type = SnmpAdminString
_CfprApPowerGroupAdditionPolicyRn_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyRn = _CfprApPowerGroupAdditionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 3),
    _CfprApPowerGroupAdditionPolicyRn_Type()
)
cfprApPowerGroupAdditionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyRn.setStatus("current")
_CfprApPowerGroupAdditionPolicyAction_Type = CfprApPowerChThrAction
_CfprApPowerGroupAdditionPolicyAction_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyAction = _CfprApPowerGroupAdditionPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 4),
    _CfprApPowerGroupAdditionPolicyAction_Type()
)
cfprApPowerGroupAdditionPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyAction.setStatus("current")
_CfprApPowerGroupAdditionPolicyDescr_Type = SnmpAdminString
_CfprApPowerGroupAdditionPolicyDescr_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyDescr = _CfprApPowerGroupAdditionPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 5),
    _CfprApPowerGroupAdditionPolicyDescr_Type()
)
cfprApPowerGroupAdditionPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyDescr.setStatus("current")
_CfprApPowerGroupAdditionPolicyIntId_Type = SnmpAdminString
_CfprApPowerGroupAdditionPolicyIntId_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyIntId = _CfprApPowerGroupAdditionPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 6),
    _CfprApPowerGroupAdditionPolicyIntId_Type()
)
cfprApPowerGroupAdditionPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyIntId.setStatus("current")
_CfprApPowerGroupAdditionPolicyName_Type = SnmpAdminString
_CfprApPowerGroupAdditionPolicyName_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyName = _CfprApPowerGroupAdditionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 7),
    _CfprApPowerGroupAdditionPolicyName_Type()
)
cfprApPowerGroupAdditionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyName.setStatus("current")
_CfprApPowerGroupAdditionPolicyPolicyLevel_Type = Gauge32
_CfprApPowerGroupAdditionPolicyPolicyLevel_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyPolicyLevel = _CfprApPowerGroupAdditionPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 8),
    _CfprApPowerGroupAdditionPolicyPolicyLevel_Type()
)
cfprApPowerGroupAdditionPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyPolicyLevel.setStatus("current")
_CfprApPowerGroupAdditionPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPowerGroupAdditionPolicyPolicyOwner_Object = MibTableColumn
cfprApPowerGroupAdditionPolicyPolicyOwner = _CfprApPowerGroupAdditionPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 5, 1, 9),
    _CfprApPowerGroupAdditionPolicyPolicyOwner_Type()
)
cfprApPowerGroupAdditionPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupAdditionPolicyPolicyOwner.setStatus("current")
_CfprApPowerGroupQualTable_Object = MibTable
cfprApPowerGroupQualTable = _CfprApPowerGroupQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 6)
)
if mibBuilder.loadTexts:
    cfprApPowerGroupQualTable.setStatus("current")
_CfprApPowerGroupQualEntry_Object = MibTableRow
cfprApPowerGroupQualEntry = _CfprApPowerGroupQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 6, 1)
)
cfprApPowerGroupQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerGroupQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerGroupQualEntry.setStatus("current")
_CfprApPowerGroupQualInstanceId_Type = CfprApManagedObjectId
_CfprApPowerGroupQualInstanceId_Object = MibTableColumn
cfprApPowerGroupQualInstanceId = _CfprApPowerGroupQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 6, 1, 1),
    _CfprApPowerGroupQualInstanceId_Type()
)
cfprApPowerGroupQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerGroupQualInstanceId.setStatus("current")
_CfprApPowerGroupQualDn_Type = CfprApManagedObjectDn
_CfprApPowerGroupQualDn_Object = MibTableColumn
cfprApPowerGroupQualDn = _CfprApPowerGroupQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 6, 1, 2),
    _CfprApPowerGroupQualDn_Type()
)
cfprApPowerGroupQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupQualDn.setStatus("current")
_CfprApPowerGroupQualRn_Type = SnmpAdminString
_CfprApPowerGroupQualRn_Object = MibTableColumn
cfprApPowerGroupQualRn = _CfprApPowerGroupQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 6, 1, 3),
    _CfprApPowerGroupQualRn_Type()
)
cfprApPowerGroupQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupQualRn.setStatus("current")
_CfprApPowerGroupQualGroupName_Type = SnmpAdminString
_CfprApPowerGroupQualGroupName_Object = MibTableColumn
cfprApPowerGroupQualGroupName = _CfprApPowerGroupQualGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 6, 1, 4),
    _CfprApPowerGroupQualGroupName_Type()
)
cfprApPowerGroupQualGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupQualGroupName.setStatus("current")
_CfprApPowerGroupStatsTable_Object = MibTable
cfprApPowerGroupStatsTable = _CfprApPowerGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7)
)
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsTable.setStatus("current")
_CfprApPowerGroupStatsEntry_Object = MibTableRow
cfprApPowerGroupStatsEntry = _CfprApPowerGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1)
)
cfprApPowerGroupStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerGroupStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsEntry.setStatus("current")
_CfprApPowerGroupStatsInstanceId_Type = CfprApManagedObjectId
_CfprApPowerGroupStatsInstanceId_Object = MibTableColumn
cfprApPowerGroupStatsInstanceId = _CfprApPowerGroupStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 1),
    _CfprApPowerGroupStatsInstanceId_Type()
)
cfprApPowerGroupStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsInstanceId.setStatus("current")
_CfprApPowerGroupStatsDn_Type = CfprApManagedObjectDn
_CfprApPowerGroupStatsDn_Object = MibTableColumn
cfprApPowerGroupStatsDn = _CfprApPowerGroupStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 2),
    _CfprApPowerGroupStatsDn_Type()
)
cfprApPowerGroupStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsDn.setStatus("current")
_CfprApPowerGroupStatsRn_Type = SnmpAdminString
_CfprApPowerGroupStatsRn_Object = MibTableColumn
cfprApPowerGroupStatsRn = _CfprApPowerGroupStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 3),
    _CfprApPowerGroupStatsRn_Type()
)
cfprApPowerGroupStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsRn.setStatus("current")
_CfprApPowerGroupStatsIntervals_Type = Gauge32
_CfprApPowerGroupStatsIntervals_Object = MibTableColumn
cfprApPowerGroupStatsIntervals = _CfprApPowerGroupStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 4),
    _CfprApPowerGroupStatsIntervals_Type()
)
cfprApPowerGroupStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsIntervals.setStatus("current")
_CfprApPowerGroupStatsPower_Type = Integer32
_CfprApPowerGroupStatsPower_Object = MibTableColumn
cfprApPowerGroupStatsPower = _CfprApPowerGroupStatsPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 5),
    _CfprApPowerGroupStatsPower_Type()
)
cfprApPowerGroupStatsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsPower.setStatus("current")
_CfprApPowerGroupStatsPowerAvg_Type = Integer32
_CfprApPowerGroupStatsPowerAvg_Object = MibTableColumn
cfprApPowerGroupStatsPowerAvg = _CfprApPowerGroupStatsPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 6),
    _CfprApPowerGroupStatsPowerAvg_Type()
)
cfprApPowerGroupStatsPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsPowerAvg.setStatus("current")
_CfprApPowerGroupStatsPowerMax_Type = Integer32
_CfprApPowerGroupStatsPowerMax_Object = MibTableColumn
cfprApPowerGroupStatsPowerMax = _CfprApPowerGroupStatsPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 7),
    _CfprApPowerGroupStatsPowerMax_Type()
)
cfprApPowerGroupStatsPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsPowerMax.setStatus("current")
_CfprApPowerGroupStatsPowerMin_Type = Integer32
_CfprApPowerGroupStatsPowerMin_Object = MibTableColumn
cfprApPowerGroupStatsPowerMin = _CfprApPowerGroupStatsPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 8),
    _CfprApPowerGroupStatsPowerMin_Type()
)
cfprApPowerGroupStatsPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsPowerMin.setStatus("current")
_CfprApPowerGroupStatsSuspect_Type = TruthValue
_CfprApPowerGroupStatsSuspect_Object = MibTableColumn
cfprApPowerGroupStatsSuspect = _CfprApPowerGroupStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 9),
    _CfprApPowerGroupStatsSuspect_Type()
)
cfprApPowerGroupStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsSuspect.setStatus("current")
_CfprApPowerGroupStatsThresholded_Type = CfprApPowerGroupStatsThresholded
_CfprApPowerGroupStatsThresholded_Object = MibTableColumn
cfprApPowerGroupStatsThresholded = _CfprApPowerGroupStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 10),
    _CfprApPowerGroupStatsThresholded_Type()
)
cfprApPowerGroupStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsThresholded.setStatus("current")
_CfprApPowerGroupStatsTimeCollected_Type = DateAndTime
_CfprApPowerGroupStatsTimeCollected_Object = MibTableColumn
cfprApPowerGroupStatsTimeCollected = _CfprApPowerGroupStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 11),
    _CfprApPowerGroupStatsTimeCollected_Type()
)
cfprApPowerGroupStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsTimeCollected.setStatus("current")
_CfprApPowerGroupStatsUpdate_Type = Gauge32
_CfprApPowerGroupStatsUpdate_Object = MibTableColumn
cfprApPowerGroupStatsUpdate = _CfprApPowerGroupStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 7, 1, 12),
    _CfprApPowerGroupStatsUpdate_Type()
)
cfprApPowerGroupStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsUpdate.setStatus("current")
_CfprApPowerGroupStatsHistTable_Object = MibTable
cfprApPowerGroupStatsHistTable = _CfprApPowerGroupStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8)
)
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistTable.setStatus("current")
_CfprApPowerGroupStatsHistEntry_Object = MibTableRow
cfprApPowerGroupStatsHistEntry = _CfprApPowerGroupStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1)
)
cfprApPowerGroupStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerGroupStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistEntry.setStatus("current")
_CfprApPowerGroupStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApPowerGroupStatsHistInstanceId_Object = MibTableColumn
cfprApPowerGroupStatsHistInstanceId = _CfprApPowerGroupStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 1),
    _CfprApPowerGroupStatsHistInstanceId_Type()
)
cfprApPowerGroupStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistInstanceId.setStatus("current")
_CfprApPowerGroupStatsHistDn_Type = CfprApManagedObjectDn
_CfprApPowerGroupStatsHistDn_Object = MibTableColumn
cfprApPowerGroupStatsHistDn = _CfprApPowerGroupStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 2),
    _CfprApPowerGroupStatsHistDn_Type()
)
cfprApPowerGroupStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistDn.setStatus("current")
_CfprApPowerGroupStatsHistRn_Type = SnmpAdminString
_CfprApPowerGroupStatsHistRn_Object = MibTableColumn
cfprApPowerGroupStatsHistRn = _CfprApPowerGroupStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 3),
    _CfprApPowerGroupStatsHistRn_Type()
)
cfprApPowerGroupStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistRn.setStatus("current")
_CfprApPowerGroupStatsHistId_Type = Unsigned64
_CfprApPowerGroupStatsHistId_Object = MibTableColumn
cfprApPowerGroupStatsHistId = _CfprApPowerGroupStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 4),
    _CfprApPowerGroupStatsHistId_Type()
)
cfprApPowerGroupStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistId.setStatus("current")
_CfprApPowerGroupStatsHistMostRecent_Type = TruthValue
_CfprApPowerGroupStatsHistMostRecent_Object = MibTableColumn
cfprApPowerGroupStatsHistMostRecent = _CfprApPowerGroupStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 5),
    _CfprApPowerGroupStatsHistMostRecent_Type()
)
cfprApPowerGroupStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistMostRecent.setStatus("current")
_CfprApPowerGroupStatsHistPower_Type = Integer32
_CfprApPowerGroupStatsHistPower_Object = MibTableColumn
cfprApPowerGroupStatsHistPower = _CfprApPowerGroupStatsHistPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 6),
    _CfprApPowerGroupStatsHistPower_Type()
)
cfprApPowerGroupStatsHistPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistPower.setStatus("current")
_CfprApPowerGroupStatsHistPowerAvg_Type = Integer32
_CfprApPowerGroupStatsHistPowerAvg_Object = MibTableColumn
cfprApPowerGroupStatsHistPowerAvg = _CfprApPowerGroupStatsHistPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 7),
    _CfprApPowerGroupStatsHistPowerAvg_Type()
)
cfprApPowerGroupStatsHistPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistPowerAvg.setStatus("current")
_CfprApPowerGroupStatsHistPowerMax_Type = Integer32
_CfprApPowerGroupStatsHistPowerMax_Object = MibTableColumn
cfprApPowerGroupStatsHistPowerMax = _CfprApPowerGroupStatsHistPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 8),
    _CfprApPowerGroupStatsHistPowerMax_Type()
)
cfprApPowerGroupStatsHistPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistPowerMax.setStatus("current")
_CfprApPowerGroupStatsHistPowerMin_Type = Integer32
_CfprApPowerGroupStatsHistPowerMin_Object = MibTableColumn
cfprApPowerGroupStatsHistPowerMin = _CfprApPowerGroupStatsHistPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 9),
    _CfprApPowerGroupStatsHistPowerMin_Type()
)
cfprApPowerGroupStatsHistPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistPowerMin.setStatus("current")
_CfprApPowerGroupStatsHistSuspect_Type = TruthValue
_CfprApPowerGroupStatsHistSuspect_Object = MibTableColumn
cfprApPowerGroupStatsHistSuspect = _CfprApPowerGroupStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 10),
    _CfprApPowerGroupStatsHistSuspect_Type()
)
cfprApPowerGroupStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistSuspect.setStatus("current")
_CfprApPowerGroupStatsHistThresholded_Type = CfprApPowerGroupStatsHistThresholded
_CfprApPowerGroupStatsHistThresholded_Object = MibTableColumn
cfprApPowerGroupStatsHistThresholded = _CfprApPowerGroupStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 11),
    _CfprApPowerGroupStatsHistThresholded_Type()
)
cfprApPowerGroupStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistThresholded.setStatus("current")
_CfprApPowerGroupStatsHistTimeCollected_Type = DateAndTime
_CfprApPowerGroupStatsHistTimeCollected_Object = MibTableColumn
cfprApPowerGroupStatsHistTimeCollected = _CfprApPowerGroupStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 8, 1, 12),
    _CfprApPowerGroupStatsHistTimeCollected_Type()
)
cfprApPowerGroupStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerGroupStatsHistTimeCollected.setStatus("current")
_CfprApPowerMgmtPolicyTable_Object = MibTable
cfprApPowerMgmtPolicyTable = _CfprApPowerMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9)
)
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyTable.setStatus("current")
_CfprApPowerMgmtPolicyEntry_Object = MibTableRow
cfprApPowerMgmtPolicyEntry = _CfprApPowerMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1)
)
cfprApPowerMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyEntry.setStatus("current")
_CfprApPowerMgmtPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApPowerMgmtPolicyInstanceId_Object = MibTableColumn
cfprApPowerMgmtPolicyInstanceId = _CfprApPowerMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 1),
    _CfprApPowerMgmtPolicyInstanceId_Type()
)
cfprApPowerMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyInstanceId.setStatus("current")
_CfprApPowerMgmtPolicyDn_Type = CfprApManagedObjectDn
_CfprApPowerMgmtPolicyDn_Object = MibTableColumn
cfprApPowerMgmtPolicyDn = _CfprApPowerMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 2),
    _CfprApPowerMgmtPolicyDn_Type()
)
cfprApPowerMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyDn.setStatus("current")
_CfprApPowerMgmtPolicyRn_Type = SnmpAdminString
_CfprApPowerMgmtPolicyRn_Object = MibTableColumn
cfprApPowerMgmtPolicyRn = _CfprApPowerMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 3),
    _CfprApPowerMgmtPolicyRn_Type()
)
cfprApPowerMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyRn.setStatus("current")
_CfprApPowerMgmtPolicyDescr_Type = SnmpAdminString
_CfprApPowerMgmtPolicyDescr_Object = MibTableColumn
cfprApPowerMgmtPolicyDescr = _CfprApPowerMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 4),
    _CfprApPowerMgmtPolicyDescr_Type()
)
cfprApPowerMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyDescr.setStatus("current")
_CfprApPowerMgmtPolicyIntId_Type = SnmpAdminString
_CfprApPowerMgmtPolicyIntId_Object = MibTableColumn
cfprApPowerMgmtPolicyIntId = _CfprApPowerMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 5),
    _CfprApPowerMgmtPolicyIntId_Type()
)
cfprApPowerMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyIntId.setStatus("current")
_CfprApPowerMgmtPolicyName_Type = SnmpAdminString
_CfprApPowerMgmtPolicyName_Object = MibTableColumn
cfprApPowerMgmtPolicyName = _CfprApPowerMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 6),
    _CfprApPowerMgmtPolicyName_Type()
)
cfprApPowerMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyName.setStatus("current")
_CfprApPowerMgmtPolicyPolicyLevel_Type = Gauge32
_CfprApPowerMgmtPolicyPolicyLevel_Object = MibTableColumn
cfprApPowerMgmtPolicyPolicyLevel = _CfprApPowerMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 7),
    _CfprApPowerMgmtPolicyPolicyLevel_Type()
)
cfprApPowerMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyPolicyLevel.setStatus("current")
_CfprApPowerMgmtPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPowerMgmtPolicyPolicyOwner_Object = MibTableColumn
cfprApPowerMgmtPolicyPolicyOwner = _CfprApPowerMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 8),
    _CfprApPowerMgmtPolicyPolicyOwner_Type()
)
cfprApPowerMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyPolicyOwner.setStatus("current")
_CfprApPowerMgmtPolicyProfiling_Type = TruthValue
_CfprApPowerMgmtPolicyProfiling_Object = MibTableColumn
cfprApPowerMgmtPolicyProfiling = _CfprApPowerMgmtPolicyProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 9),
    _CfprApPowerMgmtPolicyProfiling_Type()
)
cfprApPowerMgmtPolicyProfiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyProfiling.setStatus("current")
_CfprApPowerMgmtPolicyStyle_Type = CfprApPowerMgmtStyle
_CfprApPowerMgmtPolicyStyle_Object = MibTableColumn
cfprApPowerMgmtPolicyStyle = _CfprApPowerMgmtPolicyStyle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 9, 1, 10),
    _CfprApPowerMgmtPolicyStyle_Type()
)
cfprApPowerMgmtPolicyStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerMgmtPolicyStyle.setStatus("current")
_CfprApPowerPlacementTable_Object = MibTable
cfprApPowerPlacementTable = _CfprApPowerPlacementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10)
)
if mibBuilder.loadTexts:
    cfprApPowerPlacementTable.setStatus("current")
_CfprApPowerPlacementEntry_Object = MibTableRow
cfprApPowerPlacementEntry = _CfprApPowerPlacementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1)
)
cfprApPowerPlacementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerPlacementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerPlacementEntry.setStatus("current")
_CfprApPowerPlacementInstanceId_Type = CfprApManagedObjectId
_CfprApPowerPlacementInstanceId_Object = MibTableColumn
cfprApPowerPlacementInstanceId = _CfprApPowerPlacementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 1),
    _CfprApPowerPlacementInstanceId_Type()
)
cfprApPowerPlacementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerPlacementInstanceId.setStatus("current")
_CfprApPowerPlacementDn_Type = CfprApManagedObjectDn
_CfprApPowerPlacementDn_Object = MibTableColumn
cfprApPowerPlacementDn = _CfprApPowerPlacementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 2),
    _CfprApPowerPlacementDn_Type()
)
cfprApPowerPlacementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementDn.setStatus("current")
_CfprApPowerPlacementRn_Type = SnmpAdminString
_CfprApPowerPlacementRn_Object = MibTableColumn
cfprApPowerPlacementRn = _CfprApPowerPlacementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 3),
    _CfprApPowerPlacementRn_Type()
)
cfprApPowerPlacementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementRn.setStatus("current")
_CfprApPowerPlacementDescr_Type = SnmpAdminString
_CfprApPowerPlacementDescr_Object = MibTableColumn
cfprApPowerPlacementDescr = _CfprApPowerPlacementDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 4),
    _CfprApPowerPlacementDescr_Type()
)
cfprApPowerPlacementDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementDescr.setStatus("current")
_CfprApPowerPlacementIntId_Type = SnmpAdminString
_CfprApPowerPlacementIntId_Object = MibTableColumn
cfprApPowerPlacementIntId = _CfprApPowerPlacementIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 5),
    _CfprApPowerPlacementIntId_Type()
)
cfprApPowerPlacementIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementIntId.setStatus("current")
_CfprApPowerPlacementName_Type = SnmpAdminString
_CfprApPowerPlacementName_Object = MibTableColumn
cfprApPowerPlacementName = _CfprApPowerPlacementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 6),
    _CfprApPowerPlacementName_Type()
)
cfprApPowerPlacementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementName.setStatus("current")
_CfprApPowerPlacementPeerReqConflict_Type = CfprApPowerReqConflict
_CfprApPowerPlacementPeerReqConflict_Object = MibTableColumn
cfprApPowerPlacementPeerReqConflict = _CfprApPowerPlacementPeerReqConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 7),
    _CfprApPowerPlacementPeerReqConflict_Type()
)
cfprApPowerPlacementPeerReqConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementPeerReqConflict.setStatus("current")
_CfprApPowerPlacementPgName_Type = SnmpAdminString
_CfprApPowerPlacementPgName_Object = MibTableColumn
cfprApPowerPlacementPgName = _CfprApPowerPlacementPgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 8),
    _CfprApPowerPlacementPgName_Type()
)
cfprApPowerPlacementPgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementPgName.setStatus("current")
_CfprApPowerPlacementPolicyLevel_Type = Gauge32
_CfprApPowerPlacementPolicyLevel_Object = MibTableColumn
cfprApPowerPlacementPolicyLevel = _CfprApPowerPlacementPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 9),
    _CfprApPowerPlacementPolicyLevel_Type()
)
cfprApPowerPlacementPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementPolicyLevel.setStatus("current")
_CfprApPowerPlacementPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPowerPlacementPolicyOwner_Object = MibTableColumn
cfprApPowerPlacementPolicyOwner = _CfprApPowerPlacementPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 10),
    _CfprApPowerPlacementPolicyOwner_Type()
)
cfprApPowerPlacementPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementPolicyOwner.setStatus("current")
_CfprApPowerPlacementPrioShare_Type = CfprApPowerPrioritySharing
_CfprApPowerPlacementPrioShare_Object = MibTableColumn
cfprApPowerPlacementPrioShare = _CfprApPowerPlacementPrioShare_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 11),
    _CfprApPowerPlacementPrioShare_Type()
)
cfprApPowerPlacementPrioShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementPrioShare.setStatus("current")
_CfprApPowerPlacementSelfReqConflict_Type = CfprApPowerReqConflict
_CfprApPowerPlacementSelfReqConflict_Object = MibTableColumn
cfprApPowerPlacementSelfReqConflict = _CfprApPowerPlacementSelfReqConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 10, 1, 12),
    _CfprApPowerPlacementSelfReqConflict_Type()
)
cfprApPowerPlacementSelfReqConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPlacementSelfReqConflict.setStatus("current")
_CfprApPowerPolicyTable_Object = MibTable
cfprApPowerPolicyTable = _CfprApPowerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11)
)
if mibBuilder.loadTexts:
    cfprApPowerPolicyTable.setStatus("current")
_CfprApPowerPolicyEntry_Object = MibTableRow
cfprApPowerPolicyEntry = _CfprApPowerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1)
)
cfprApPowerPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerPolicyEntry.setStatus("current")
_CfprApPowerPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApPowerPolicyInstanceId_Object = MibTableColumn
cfprApPowerPolicyInstanceId = _CfprApPowerPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 1),
    _CfprApPowerPolicyInstanceId_Type()
)
cfprApPowerPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerPolicyInstanceId.setStatus("current")
_CfprApPowerPolicyDn_Type = CfprApManagedObjectDn
_CfprApPowerPolicyDn_Object = MibTableColumn
cfprApPowerPolicyDn = _CfprApPowerPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 2),
    _CfprApPowerPolicyDn_Type()
)
cfprApPowerPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyDn.setStatus("current")
_CfprApPowerPolicyRn_Type = SnmpAdminString
_CfprApPowerPolicyRn_Object = MibTableColumn
cfprApPowerPolicyRn = _CfprApPowerPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 3),
    _CfprApPowerPolicyRn_Type()
)
cfprApPowerPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyRn.setStatus("current")
_CfprApPowerPolicyDescr_Type = SnmpAdminString
_CfprApPowerPolicyDescr_Object = MibTableColumn
cfprApPowerPolicyDescr = _CfprApPowerPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 4),
    _CfprApPowerPolicyDescr_Type()
)
cfprApPowerPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyDescr.setStatus("current")
_CfprApPowerPolicyIntId_Type = SnmpAdminString
_CfprApPowerPolicyIntId_Object = MibTableColumn
cfprApPowerPolicyIntId = _CfprApPowerPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 5),
    _CfprApPowerPolicyIntId_Type()
)
cfprApPowerPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyIntId.setStatus("current")
_CfprApPowerPolicyName_Type = SnmpAdminString
_CfprApPowerPolicyName_Object = MibTableColumn
cfprApPowerPolicyName = _CfprApPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 6),
    _CfprApPowerPolicyName_Type()
)
cfprApPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyName.setStatus("current")
_CfprApPowerPolicyOperPrio_Type = Gauge32
_CfprApPowerPolicyOperPrio_Object = MibTableColumn
cfprApPowerPolicyOperPrio = _CfprApPowerPolicyOperPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 7),
    _CfprApPowerPolicyOperPrio_Type()
)
cfprApPowerPolicyOperPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyOperPrio.setStatus("current")
_CfprApPowerPolicyPolicyLevel_Type = Gauge32
_CfprApPowerPolicyPolicyLevel_Object = MibTableColumn
cfprApPowerPolicyPolicyLevel = _CfprApPowerPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 8),
    _CfprApPowerPolicyPolicyLevel_Type()
)
cfprApPowerPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyPolicyLevel.setStatus("current")
_CfprApPowerPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPowerPolicyPolicyOwner_Object = MibTableColumn
cfprApPowerPolicyPolicyOwner = _CfprApPowerPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 9),
    _CfprApPowerPolicyPolicyOwner_Type()
)
cfprApPowerPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyPolicyOwner.setStatus("current")
_CfprApPowerPolicyPrio_Type = Gauge32
_CfprApPowerPolicyPrio_Object = MibTableColumn
cfprApPowerPolicyPrio = _CfprApPowerPolicyPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 11, 1, 10),
    _CfprApPowerPolicyPrio_Type()
)
cfprApPowerPolicyPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPolicyPrio.setStatus("current")
_CfprApPowerPrioWghtTable_Object = MibTable
cfprApPowerPrioWghtTable = _CfprApPowerPrioWghtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12)
)
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtTable.setStatus("current")
_CfprApPowerPrioWghtEntry_Object = MibTableRow
cfprApPowerPrioWghtEntry = _CfprApPowerPrioWghtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12, 1)
)
cfprApPowerPrioWghtEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerPrioWghtInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtEntry.setStatus("current")
_CfprApPowerPrioWghtInstanceId_Type = CfprApManagedObjectId
_CfprApPowerPrioWghtInstanceId_Object = MibTableColumn
cfprApPowerPrioWghtInstanceId = _CfprApPowerPrioWghtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12, 1, 1),
    _CfprApPowerPrioWghtInstanceId_Type()
)
cfprApPowerPrioWghtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtInstanceId.setStatus("current")
_CfprApPowerPrioWghtDn_Type = CfprApManagedObjectDn
_CfprApPowerPrioWghtDn_Object = MibTableColumn
cfprApPowerPrioWghtDn = _CfprApPowerPrioWghtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12, 1, 2),
    _CfprApPowerPrioWghtDn_Type()
)
cfprApPowerPrioWghtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtDn.setStatus("current")
_CfprApPowerPrioWghtRn_Type = SnmpAdminString
_CfprApPowerPrioWghtRn_Object = MibTableColumn
cfprApPowerPrioWghtRn = _CfprApPowerPrioWghtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12, 1, 3),
    _CfprApPowerPrioWghtRn_Type()
)
cfprApPowerPrioWghtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtRn.setStatus("current")
_CfprApPowerPrioWghtPrio_Type = Gauge32
_CfprApPowerPrioWghtPrio_Object = MibTableColumn
cfprApPowerPrioWghtPrio = _CfprApPowerPrioWghtPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12, 1, 4),
    _CfprApPowerPrioWghtPrio_Type()
)
cfprApPowerPrioWghtPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtPrio.setStatus("current")
_CfprApPowerPrioWghtWeight_Type = Gauge32
_CfprApPowerPrioWghtWeight_Object = MibTableColumn
cfprApPowerPrioWghtWeight = _CfprApPowerPrioWghtWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 12, 1, 5),
    _CfprApPowerPrioWghtWeight_Type()
)
cfprApPowerPrioWghtWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerPrioWghtWeight.setStatus("current")
_CfprApPowerProfiledPowerTable_Object = MibTable
cfprApPowerProfiledPowerTable = _CfprApPowerProfiledPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13)
)
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerTable.setStatus("current")
_CfprApPowerProfiledPowerEntry_Object = MibTableRow
cfprApPowerProfiledPowerEntry = _CfprApPowerProfiledPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1)
)
cfprApPowerProfiledPowerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerProfiledPowerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerEntry.setStatus("current")
_CfprApPowerProfiledPowerInstanceId_Type = CfprApManagedObjectId
_CfprApPowerProfiledPowerInstanceId_Object = MibTableColumn
cfprApPowerProfiledPowerInstanceId = _CfprApPowerProfiledPowerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 1),
    _CfprApPowerProfiledPowerInstanceId_Type()
)
cfprApPowerProfiledPowerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerInstanceId.setStatus("current")
_CfprApPowerProfiledPowerDn_Type = CfprApManagedObjectDn
_CfprApPowerProfiledPowerDn_Object = MibTableColumn
cfprApPowerProfiledPowerDn = _CfprApPowerProfiledPowerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 2),
    _CfprApPowerProfiledPowerDn_Type()
)
cfprApPowerProfiledPowerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerDn.setStatus("current")
_CfprApPowerProfiledPowerRn_Type = SnmpAdminString
_CfprApPowerProfiledPowerRn_Object = MibTableColumn
cfprApPowerProfiledPowerRn = _CfprApPowerProfiledPowerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 3),
    _CfprApPowerProfiledPowerRn_Type()
)
cfprApPowerProfiledPowerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerRn.setStatus("current")
_CfprApPowerProfiledPowerAbsMinPostPower_Type = Gauge32
_CfprApPowerProfiledPowerAbsMinPostPower_Object = MibTableColumn
cfprApPowerProfiledPowerAbsMinPostPower = _CfprApPowerProfiledPowerAbsMinPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 4),
    _CfprApPowerProfiledPowerAbsMinPostPower_Type()
)
cfprApPowerProfiledPowerAbsMinPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerAbsMinPostPower.setStatus("current")
_CfprApPowerProfiledPowerMaxAppPower_Type = Gauge32
_CfprApPowerProfiledPowerMaxAppPower_Object = MibTableColumn
cfprApPowerProfiledPowerMaxAppPower = _CfprApPowerProfiledPowerMaxAppPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 5),
    _CfprApPowerProfiledPowerMaxAppPower_Type()
)
cfprApPowerProfiledPowerMaxAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerMaxAppPower.setStatus("current")
_CfprApPowerProfiledPowerMaxPostPower_Type = Gauge32
_CfprApPowerProfiledPowerMaxPostPower_Object = MibTableColumn
cfprApPowerProfiledPowerMaxPostPower = _CfprApPowerProfiledPowerMaxPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 6),
    _CfprApPowerProfiledPowerMaxPostPower_Type()
)
cfprApPowerProfiledPowerMaxPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerMaxPostPower.setStatus("current")
_CfprApPowerProfiledPowerMinAppPower_Type = Gauge32
_CfprApPowerProfiledPowerMinAppPower_Object = MibTableColumn
cfprApPowerProfiledPowerMinAppPower = _CfprApPowerProfiledPowerMinAppPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 7),
    _CfprApPowerProfiledPowerMinAppPower_Type()
)
cfprApPowerProfiledPowerMinAppPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerMinAppPower.setStatus("current")
_CfprApPowerProfiledPowerMinNormPostPower_Type = Gauge32
_CfprApPowerProfiledPowerMinNormPostPower_Object = MibTableColumn
cfprApPowerProfiledPowerMinNormPostPower = _CfprApPowerProfiledPowerMinNormPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 8),
    _CfprApPowerProfiledPowerMinNormPostPower_Type()
)
cfprApPowerProfiledPowerMinNormPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerMinNormPostPower.setStatus("current")
_CfprApPowerProfiledPowerMinPostPower_Type = Gauge32
_CfprApPowerProfiledPowerMinPostPower_Object = MibTableColumn
cfprApPowerProfiledPowerMinPostPower = _CfprApPowerProfiledPowerMinPostPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 9),
    _CfprApPowerProfiledPowerMinPostPower_Type()
)
cfprApPowerProfiledPowerMinPostPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerMinPostPower.setStatus("current")
_CfprApPowerProfiledPowerPreDiscoveryPower_Type = Gauge32
_CfprApPowerProfiledPowerPreDiscoveryPower_Object = MibTableColumn
cfprApPowerProfiledPowerPreDiscoveryPower = _CfprApPowerProfiledPowerPreDiscoveryPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 10),
    _CfprApPowerProfiledPowerPreDiscoveryPower_Type()
)
cfprApPowerProfiledPowerPreDiscoveryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerPreDiscoveryPower.setStatus("current")
_CfprApPowerProfiledPowerProfileRunTime_Type = Gauge32
_CfprApPowerProfiledPowerProfileRunTime_Object = MibTableColumn
cfprApPowerProfiledPowerProfileRunTime = _CfprApPowerProfiledPowerProfileRunTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 11),
    _CfprApPowerProfiledPowerProfileRunTime_Type()
)
cfprApPowerProfiledPowerProfileRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerProfileRunTime.setStatus("current")
_CfprApPowerProfiledPowerProfiledBoot_Type = Gauge32
_CfprApPowerProfiledPowerProfiledBoot_Object = MibTableColumn
cfprApPowerProfiledPowerProfiledBoot = _CfprApPowerProfiledPowerProfiledBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 12),
    _CfprApPowerProfiledPowerProfiledBoot_Type()
)
cfprApPowerProfiledPowerProfiledBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerProfiledBoot.setStatus("current")
_CfprApPowerProfiledPowerProfiledMax_Type = Gauge32
_CfprApPowerProfiledPowerProfiledMax_Object = MibTableColumn
cfprApPowerProfiledPowerProfiledMax = _CfprApPowerProfiledPowerProfiledMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 13),
    _CfprApPowerProfiledPowerProfiledMax_Type()
)
cfprApPowerProfiledPowerProfiledMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerProfiledMax.setStatus("current")
_CfprApPowerProfiledPowerProfiledMin_Type = Gauge32
_CfprApPowerProfiledPowerProfiledMin_Object = MibTableColumn
cfprApPowerProfiledPowerProfiledMin = _CfprApPowerProfiledPowerProfiledMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 14),
    _CfprApPowerProfiledPowerProfiledMin_Type()
)
cfprApPowerProfiledPowerProfiledMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerProfiledMin.setStatus("current")
_CfprApPowerProfiledPowerSkipProfiling_Type = TruthValue
_CfprApPowerProfiledPowerSkipProfiling_Object = MibTableColumn
cfprApPowerProfiledPowerSkipProfiling = _CfprApPowerProfiledPowerSkipProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 13, 1, 15),
    _CfprApPowerProfiledPowerSkipProfiling_Type()
)
cfprApPowerProfiledPowerSkipProfiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerProfiledPowerSkipProfiling.setStatus("current")
_CfprApPowerRackUnitMemberTable_Object = MibTable
cfprApPowerRackUnitMemberTable = _CfprApPowerRackUnitMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14)
)
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberTable.setStatus("current")
_CfprApPowerRackUnitMemberEntry_Object = MibTableRow
cfprApPowerRackUnitMemberEntry = _CfprApPowerRackUnitMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14, 1)
)
cfprApPowerRackUnitMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POWER-MIB", "cfprApPowerRackUnitMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberEntry.setStatus("current")
_CfprApPowerRackUnitMemberInstanceId_Type = CfprApManagedObjectId
_CfprApPowerRackUnitMemberInstanceId_Object = MibTableColumn
cfprApPowerRackUnitMemberInstanceId = _CfprApPowerRackUnitMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14, 1, 1),
    _CfprApPowerRackUnitMemberInstanceId_Type()
)
cfprApPowerRackUnitMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberInstanceId.setStatus("current")
_CfprApPowerRackUnitMemberDn_Type = CfprApManagedObjectDn
_CfprApPowerRackUnitMemberDn_Object = MibTableColumn
cfprApPowerRackUnitMemberDn = _CfprApPowerRackUnitMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14, 1, 2),
    _CfprApPowerRackUnitMemberDn_Type()
)
cfprApPowerRackUnitMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberDn.setStatus("current")
_CfprApPowerRackUnitMemberRn_Type = SnmpAdminString
_CfprApPowerRackUnitMemberRn_Object = MibTableColumn
cfprApPowerRackUnitMemberRn = _CfprApPowerRackUnitMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14, 1, 3),
    _CfprApPowerRackUnitMemberRn_Type()
)
cfprApPowerRackUnitMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberRn.setStatus("current")
_CfprApPowerRackUnitMemberId_Type = Gauge32
_CfprApPowerRackUnitMemberId_Object = MibTableColumn
cfprApPowerRackUnitMemberId = _CfprApPowerRackUnitMemberId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14, 1, 4),
    _CfprApPowerRackUnitMemberId_Type()
)
cfprApPowerRackUnitMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberId.setStatus("current")
_CfprApPowerRackUnitMemberOperState_Type = CfprApPowerMemberState
_CfprApPowerRackUnitMemberOperState_Object = MibTableColumn
cfprApPowerRackUnitMemberOperState = _CfprApPowerRackUnitMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 64, 14, 1, 5),
    _CfprApPowerRackUnitMemberOperState_Type()
)
cfprApPowerRackUnitMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPowerRackUnitMemberOperState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-POWER-MIB",
    **{"cfprApPowerObjects": cfprApPowerObjects,
       "cfprApPowerBudgetTable": cfprApPowerBudgetTable,
       "cfprApPowerBudgetEntry": cfprApPowerBudgetEntry,
       "cfprApPowerBudgetInstanceId": cfprApPowerBudgetInstanceId,
       "cfprApPowerBudgetDn": cfprApPowerBudgetDn,
       "cfprApPowerBudgetRn": cfprApPowerBudgetRn,
       "cfprApPowerBudgetAdminCommitted": cfprApPowerBudgetAdminCommitted,
       "cfprApPowerBudgetAdminFPLockState": cfprApPowerBudgetAdminFPLockState,
       "cfprApPowerBudgetAdminPeak": cfprApPowerBudgetAdminPeak,
       "cfprApPowerBudgetAdminPeakNew": cfprApPowerBudgetAdminPeakNew,
       "cfprApPowerBudgetBootPower": cfprApPowerBudgetBootPower,
       "cfprApPowerBudgetCapAction": cfprApPowerBudgetCapAction,
       "cfprApPowerBudgetCatalogPower": cfprApPowerBudgetCatalogPower,
       "cfprApPowerBudgetChRsrvdPower": cfprApPowerBudgetChRsrvdPower,
       "cfprApPowerBudgetCurrentPower": cfprApPowerBudgetCurrentPower,
       "cfprApPowerBudgetDynRealloc": cfprApPowerBudgetDynRealloc,
       "cfprApPowerBudgetGroupName": cfprApPowerBudgetGroupName,
       "cfprApPowerBudgetIdlePower": cfprApPowerBudgetIdlePower,
       "cfprApPowerBudgetMaxPower": cfprApPowerBudgetMaxPower,
       "cfprApPowerBudgetMinPower": cfprApPowerBudgetMinPower,
       "cfprApPowerBudgetOperCommitted": cfprApPowerBudgetOperCommitted,
       "cfprApPowerBudgetOperFPLockState": cfprApPowerBudgetOperFPLockState,
       "cfprApPowerBudgetOperMin": cfprApPowerBudgetOperMin,
       "cfprApPowerBudgetOperPeak": cfprApPowerBudgetOperPeak,
       "cfprApPowerBudgetOperProfMethod": cfprApPowerBudgetOperProfMethod,
       "cfprApPowerBudgetOperState": cfprApPowerBudgetOperState,
       "cfprApPowerBudgetPrio": cfprApPowerBudgetPrio,
       "cfprApPowerBudgetProfMethod": cfprApPowerBudgetProfMethod,
       "cfprApPowerBudgetProfiling": cfprApPowerBudgetProfiling,
       "cfprApPowerBudgetPsuCapacity": cfprApPowerBudgetPsuCapacity,
       "cfprApPowerBudgetPsuLineMode": cfprApPowerBudgetPsuLineMode,
       "cfprApPowerBudgetPsuState": cfprApPowerBudgetPsuState,
       "cfprApPowerBudgetScaledWt": cfprApPowerBudgetScaledWt,
       "cfprApPowerBudgetStyle": cfprApPowerBudgetStyle,
       "cfprApPowerBudgetUpdateTime": cfprApPowerBudgetUpdateTime,
       "cfprApPowerBudgetWeight": cfprApPowerBudgetWeight,
       "cfprApPowerChassisMemberTable": cfprApPowerChassisMemberTable,
       "cfprApPowerChassisMemberEntry": cfprApPowerChassisMemberEntry,
       "cfprApPowerChassisMemberInstanceId": cfprApPowerChassisMemberInstanceId,
       "cfprApPowerChassisMemberDn": cfprApPowerChassisMemberDn,
       "cfprApPowerChassisMemberRn": cfprApPowerChassisMemberRn,
       "cfprApPowerChassisMemberId": cfprApPowerChassisMemberId,
       "cfprApPowerChassisMemberOperState": cfprApPowerChassisMemberOperState,
       "cfprApPowerEpTable": cfprApPowerEpTable,
       "cfprApPowerEpEntry": cfprApPowerEpEntry,
       "cfprApPowerEpInstanceId": cfprApPowerEpInstanceId,
       "cfprApPowerEpDn": cfprApPowerEpDn,
       "cfprApPowerEpRn": cfprApPowerEpRn,
       "cfprApPowerGroupTable": cfprApPowerGroupTable,
       "cfprApPowerGroupEntry": cfprApPowerGroupEntry,
       "cfprApPowerGroupInstanceId": cfprApPowerGroupInstanceId,
       "cfprApPowerGroupDn": cfprApPowerGroupDn,
       "cfprApPowerGroupRn": cfprApPowerGroupRn,
       "cfprApPowerGroupAdminCommitted": cfprApPowerGroupAdminCommitted,
       "cfprApPowerGroupAdminPeak": cfprApPowerGroupAdminPeak,
       "cfprApPowerGroupCurReqPower": cfprApPowerGroupCurReqPower,
       "cfprApPowerGroupCurrentPower": cfprApPowerGroupCurrentPower,
       "cfprApPowerGroupDescr": cfprApPowerGroupDescr,
       "cfprApPowerGroupFltAggr": cfprApPowerGroupFltAggr,
       "cfprApPowerGroupIntId": cfprApPowerGroupIntId,
       "cfprApPowerGroupMinReqPower": cfprApPowerGroupMinReqPower,
       "cfprApPowerGroupName": cfprApPowerGroupName,
       "cfprApPowerGroupOperCommitted": cfprApPowerGroupOperCommitted,
       "cfprApPowerGroupOperPeak": cfprApPowerGroupOperPeak,
       "cfprApPowerGroupOperState": cfprApPowerGroupOperState,
       "cfprApPowerGroupPolicyLevel": cfprApPowerGroupPolicyLevel,
       "cfprApPowerGroupPolicyOwner": cfprApPowerGroupPolicyOwner,
       "cfprApPowerGroupQualifier": cfprApPowerGroupQualifier,
       "cfprApPowerGroupRealloc": cfprApPowerGroupRealloc,
       "cfprApPowerGroupAdditionPolicyTable": cfprApPowerGroupAdditionPolicyTable,
       "cfprApPowerGroupAdditionPolicyEntry": cfprApPowerGroupAdditionPolicyEntry,
       "cfprApPowerGroupAdditionPolicyInstanceId": cfprApPowerGroupAdditionPolicyInstanceId,
       "cfprApPowerGroupAdditionPolicyDn": cfprApPowerGroupAdditionPolicyDn,
       "cfprApPowerGroupAdditionPolicyRn": cfprApPowerGroupAdditionPolicyRn,
       "cfprApPowerGroupAdditionPolicyAction": cfprApPowerGroupAdditionPolicyAction,
       "cfprApPowerGroupAdditionPolicyDescr": cfprApPowerGroupAdditionPolicyDescr,
       "cfprApPowerGroupAdditionPolicyIntId": cfprApPowerGroupAdditionPolicyIntId,
       "cfprApPowerGroupAdditionPolicyName": cfprApPowerGroupAdditionPolicyName,
       "cfprApPowerGroupAdditionPolicyPolicyLevel": cfprApPowerGroupAdditionPolicyPolicyLevel,
       "cfprApPowerGroupAdditionPolicyPolicyOwner": cfprApPowerGroupAdditionPolicyPolicyOwner,
       "cfprApPowerGroupQualTable": cfprApPowerGroupQualTable,
       "cfprApPowerGroupQualEntry": cfprApPowerGroupQualEntry,
       "cfprApPowerGroupQualInstanceId": cfprApPowerGroupQualInstanceId,
       "cfprApPowerGroupQualDn": cfprApPowerGroupQualDn,
       "cfprApPowerGroupQualRn": cfprApPowerGroupQualRn,
       "cfprApPowerGroupQualGroupName": cfprApPowerGroupQualGroupName,
       "cfprApPowerGroupStatsTable": cfprApPowerGroupStatsTable,
       "cfprApPowerGroupStatsEntry": cfprApPowerGroupStatsEntry,
       "cfprApPowerGroupStatsInstanceId": cfprApPowerGroupStatsInstanceId,
       "cfprApPowerGroupStatsDn": cfprApPowerGroupStatsDn,
       "cfprApPowerGroupStatsRn": cfprApPowerGroupStatsRn,
       "cfprApPowerGroupStatsIntervals": cfprApPowerGroupStatsIntervals,
       "cfprApPowerGroupStatsPower": cfprApPowerGroupStatsPower,
       "cfprApPowerGroupStatsPowerAvg": cfprApPowerGroupStatsPowerAvg,
       "cfprApPowerGroupStatsPowerMax": cfprApPowerGroupStatsPowerMax,
       "cfprApPowerGroupStatsPowerMin": cfprApPowerGroupStatsPowerMin,
       "cfprApPowerGroupStatsSuspect": cfprApPowerGroupStatsSuspect,
       "cfprApPowerGroupStatsThresholded": cfprApPowerGroupStatsThresholded,
       "cfprApPowerGroupStatsTimeCollected": cfprApPowerGroupStatsTimeCollected,
       "cfprApPowerGroupStatsUpdate": cfprApPowerGroupStatsUpdate,
       "cfprApPowerGroupStatsHistTable": cfprApPowerGroupStatsHistTable,
       "cfprApPowerGroupStatsHistEntry": cfprApPowerGroupStatsHistEntry,
       "cfprApPowerGroupStatsHistInstanceId": cfprApPowerGroupStatsHistInstanceId,
       "cfprApPowerGroupStatsHistDn": cfprApPowerGroupStatsHistDn,
       "cfprApPowerGroupStatsHistRn": cfprApPowerGroupStatsHistRn,
       "cfprApPowerGroupStatsHistId": cfprApPowerGroupStatsHistId,
       "cfprApPowerGroupStatsHistMostRecent": cfprApPowerGroupStatsHistMostRecent,
       "cfprApPowerGroupStatsHistPower": cfprApPowerGroupStatsHistPower,
       "cfprApPowerGroupStatsHistPowerAvg": cfprApPowerGroupStatsHistPowerAvg,
       "cfprApPowerGroupStatsHistPowerMax": cfprApPowerGroupStatsHistPowerMax,
       "cfprApPowerGroupStatsHistPowerMin": cfprApPowerGroupStatsHistPowerMin,
       "cfprApPowerGroupStatsHistSuspect": cfprApPowerGroupStatsHistSuspect,
       "cfprApPowerGroupStatsHistThresholded": cfprApPowerGroupStatsHistThresholded,
       "cfprApPowerGroupStatsHistTimeCollected": cfprApPowerGroupStatsHistTimeCollected,
       "cfprApPowerMgmtPolicyTable": cfprApPowerMgmtPolicyTable,
       "cfprApPowerMgmtPolicyEntry": cfprApPowerMgmtPolicyEntry,
       "cfprApPowerMgmtPolicyInstanceId": cfprApPowerMgmtPolicyInstanceId,
       "cfprApPowerMgmtPolicyDn": cfprApPowerMgmtPolicyDn,
       "cfprApPowerMgmtPolicyRn": cfprApPowerMgmtPolicyRn,
       "cfprApPowerMgmtPolicyDescr": cfprApPowerMgmtPolicyDescr,
       "cfprApPowerMgmtPolicyIntId": cfprApPowerMgmtPolicyIntId,
       "cfprApPowerMgmtPolicyName": cfprApPowerMgmtPolicyName,
       "cfprApPowerMgmtPolicyPolicyLevel": cfprApPowerMgmtPolicyPolicyLevel,
       "cfprApPowerMgmtPolicyPolicyOwner": cfprApPowerMgmtPolicyPolicyOwner,
       "cfprApPowerMgmtPolicyProfiling": cfprApPowerMgmtPolicyProfiling,
       "cfprApPowerMgmtPolicyStyle": cfprApPowerMgmtPolicyStyle,
       "cfprApPowerPlacementTable": cfprApPowerPlacementTable,
       "cfprApPowerPlacementEntry": cfprApPowerPlacementEntry,
       "cfprApPowerPlacementInstanceId": cfprApPowerPlacementInstanceId,
       "cfprApPowerPlacementDn": cfprApPowerPlacementDn,
       "cfprApPowerPlacementRn": cfprApPowerPlacementRn,
       "cfprApPowerPlacementDescr": cfprApPowerPlacementDescr,
       "cfprApPowerPlacementIntId": cfprApPowerPlacementIntId,
       "cfprApPowerPlacementName": cfprApPowerPlacementName,
       "cfprApPowerPlacementPeerReqConflict": cfprApPowerPlacementPeerReqConflict,
       "cfprApPowerPlacementPgName": cfprApPowerPlacementPgName,
       "cfprApPowerPlacementPolicyLevel": cfprApPowerPlacementPolicyLevel,
       "cfprApPowerPlacementPolicyOwner": cfprApPowerPlacementPolicyOwner,
       "cfprApPowerPlacementPrioShare": cfprApPowerPlacementPrioShare,
       "cfprApPowerPlacementSelfReqConflict": cfprApPowerPlacementSelfReqConflict,
       "cfprApPowerPolicyTable": cfprApPowerPolicyTable,
       "cfprApPowerPolicyEntry": cfprApPowerPolicyEntry,
       "cfprApPowerPolicyInstanceId": cfprApPowerPolicyInstanceId,
       "cfprApPowerPolicyDn": cfprApPowerPolicyDn,
       "cfprApPowerPolicyRn": cfprApPowerPolicyRn,
       "cfprApPowerPolicyDescr": cfprApPowerPolicyDescr,
       "cfprApPowerPolicyIntId": cfprApPowerPolicyIntId,
       "cfprApPowerPolicyName": cfprApPowerPolicyName,
       "cfprApPowerPolicyOperPrio": cfprApPowerPolicyOperPrio,
       "cfprApPowerPolicyPolicyLevel": cfprApPowerPolicyPolicyLevel,
       "cfprApPowerPolicyPolicyOwner": cfprApPowerPolicyPolicyOwner,
       "cfprApPowerPolicyPrio": cfprApPowerPolicyPrio,
       "cfprApPowerPrioWghtTable": cfprApPowerPrioWghtTable,
       "cfprApPowerPrioWghtEntry": cfprApPowerPrioWghtEntry,
       "cfprApPowerPrioWghtInstanceId": cfprApPowerPrioWghtInstanceId,
       "cfprApPowerPrioWghtDn": cfprApPowerPrioWghtDn,
       "cfprApPowerPrioWghtRn": cfprApPowerPrioWghtRn,
       "cfprApPowerPrioWghtPrio": cfprApPowerPrioWghtPrio,
       "cfprApPowerPrioWghtWeight": cfprApPowerPrioWghtWeight,
       "cfprApPowerProfiledPowerTable": cfprApPowerProfiledPowerTable,
       "cfprApPowerProfiledPowerEntry": cfprApPowerProfiledPowerEntry,
       "cfprApPowerProfiledPowerInstanceId": cfprApPowerProfiledPowerInstanceId,
       "cfprApPowerProfiledPowerDn": cfprApPowerProfiledPowerDn,
       "cfprApPowerProfiledPowerRn": cfprApPowerProfiledPowerRn,
       "cfprApPowerProfiledPowerAbsMinPostPower": cfprApPowerProfiledPowerAbsMinPostPower,
       "cfprApPowerProfiledPowerMaxAppPower": cfprApPowerProfiledPowerMaxAppPower,
       "cfprApPowerProfiledPowerMaxPostPower": cfprApPowerProfiledPowerMaxPostPower,
       "cfprApPowerProfiledPowerMinAppPower": cfprApPowerProfiledPowerMinAppPower,
       "cfprApPowerProfiledPowerMinNormPostPower": cfprApPowerProfiledPowerMinNormPostPower,
       "cfprApPowerProfiledPowerMinPostPower": cfprApPowerProfiledPowerMinPostPower,
       "cfprApPowerProfiledPowerPreDiscoveryPower": cfprApPowerProfiledPowerPreDiscoveryPower,
       "cfprApPowerProfiledPowerProfileRunTime": cfprApPowerProfiledPowerProfileRunTime,
       "cfprApPowerProfiledPowerProfiledBoot": cfprApPowerProfiledPowerProfiledBoot,
       "cfprApPowerProfiledPowerProfiledMax": cfprApPowerProfiledPowerProfiledMax,
       "cfprApPowerProfiledPowerProfiledMin": cfprApPowerProfiledPowerProfiledMin,
       "cfprApPowerProfiledPowerSkipProfiling": cfprApPowerProfiledPowerSkipProfiling,
       "cfprApPowerRackUnitMemberTable": cfprApPowerRackUnitMemberTable,
       "cfprApPowerRackUnitMemberEntry": cfprApPowerRackUnitMemberEntry,
       "cfprApPowerRackUnitMemberInstanceId": cfprApPowerRackUnitMemberInstanceId,
       "cfprApPowerRackUnitMemberDn": cfprApPowerRackUnitMemberDn,
       "cfprApPowerRackUnitMemberRn": cfprApPowerRackUnitMemberRn,
       "cfprApPowerRackUnitMemberId": cfprApPowerRackUnitMemberId,
       "cfprApPowerRackUnitMemberOperState": cfprApPowerRackUnitMemberOperState}
)
