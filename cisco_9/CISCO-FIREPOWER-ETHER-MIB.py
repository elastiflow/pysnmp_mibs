# SNMP MIB module (CISCO-FIREPOWER-ETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-ETHER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprConditionRemoteInvRslt,
 CfprEquipmentChassisConfigState,
 CfprEquipmentXcvrType,
 CfprEtherCIoEpIfType,
 CfprEtherCloudType,
 CfprEtherErrStatsHistThresholded,
 CfprEtherErrStatsThresholded,
 CfprEtherExternalEpAdminState,
 CfprEtherExternalEpLocale,
 CfprEtherExternalPcAdminState,
 CfprEtherExternalPcLocale,
 CfprEtherFcoeInterfaceStatsHistThresholded,
 CfprEtherFcoeInterfaceStatsThresholded,
 CfprEtherFtwOperMode,
 CfprEtherFtwPortPairFsmCurrentFsm,
 CfprEtherFtwPortPairFsmStageName,
 CfprEtherFtwPortPairFsmTaskItem,
 CfprEtherFtwPortPairMode,
 CfprEtherFtwPortPairWdtState,
 CfprEtherIntFIoEpType,
 CfprEtherInternalPcLocale,
 CfprEtherLossStatsHistThresholded,
 CfprEtherLossStatsThresholded,
 CfprEtherNiErrStatsHistThresholded,
 CfprEtherNiErrStatsThresholded,
 CfprEtherPIoEpIfType,
 CfprEtherPIoFsmCurrentFsm,
 CfprEtherPIoFsmStageName,
 CfprEtherPauseStatsHistThresholded,
 CfprEtherPauseStatsThresholded,
 CfprEtherRxStatsHistThresholded,
 CfprEtherRxStatsThresholded,
 CfprEtherSatelliteConnectionDisc,
 CfprEtherServerIntFIoAdminState,
 CfprEtherServerIntFIoFsmCurrentFsm,
 CfprEtherServerIntFIoFsmStageName,
 CfprEtherServerIntFIoFsmTaskItem,
 CfprEtherServerIntFIoIfRole,
 CfprEtherServerIntFIoLocale,
 CfprEtherServerIntFIoPcEpIfRole,
 CfprEtherServerIntFIoPcEpPortId,
 CfprEtherServerIntFIoPcIfRole,
 CfprEtherServerIntFIoPcPortId,
 CfprEtherServerIntFIoPcTransport,
 CfprEtherServerIntFIoPcType,
 CfprEtherServerIntFIoTransport,
 CfprEtherServerIntFIoType,
 CfprEtherSwitchIntFIoAck,
 CfprEtherSwitchIntFIoIfRole,
 CfprEtherSwitchIntFIoLocale,
 CfprEtherSwitchIntFIoPcEpIfRole,
 CfprEtherSwitchIntFIoPcEpPortId,
 CfprEtherSwitchIntFIoPcIfRole,
 CfprEtherSwitchIntFIoPcPortId,
 CfprEtherSwitchIntFIoPcTransport,
 CfprEtherSwitchIntFIoPcType,
 CfprEtherSwitchIntFIoTransport,
 CfprEtherSwitchIntFIoType,
 CfprEtherTxStatsHistThresholded,
 CfprEtherTxStatsThresholded,
 CfprFabricAdminState,
 CfprFabricMembershipStatus,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprFsmLifecycle,
 CfprLicenseState,
 CfprNetworkConnectionType,
 CfprNetworkLocale,
 CfprNetworkPhysEpIfType,
 CfprNetworkPortOperState,
 CfprNetworkPortRole,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprPortDuplex,
 CfprPortEncap,
 CfprPortEthSpeed,
 CfprPortMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprEquipmentChassisConfigState",
    "CfprEquipmentXcvrType",
    "CfprEtherCIoEpIfType",
    "CfprEtherCloudType",
    "CfprEtherErrStatsHistThresholded",
    "CfprEtherErrStatsThresholded",
    "CfprEtherExternalEpAdminState",
    "CfprEtherExternalEpLocale",
    "CfprEtherExternalPcAdminState",
    "CfprEtherExternalPcLocale",
    "CfprEtherFcoeInterfaceStatsHistThresholded",
    "CfprEtherFcoeInterfaceStatsThresholded",
    "CfprEtherFtwOperMode",
    "CfprEtherFtwPortPairFsmCurrentFsm",
    "CfprEtherFtwPortPairFsmStageName",
    "CfprEtherFtwPortPairFsmTaskItem",
    "CfprEtherFtwPortPairMode",
    "CfprEtherFtwPortPairWdtState",
    "CfprEtherIntFIoEpType",
    "CfprEtherInternalPcLocale",
    "CfprEtherLossStatsHistThresholded",
    "CfprEtherLossStatsThresholded",
    "CfprEtherNiErrStatsHistThresholded",
    "CfprEtherNiErrStatsThresholded",
    "CfprEtherPIoEpIfType",
    "CfprEtherPIoFsmCurrentFsm",
    "CfprEtherPIoFsmStageName",
    "CfprEtherPauseStatsHistThresholded",
    "CfprEtherPauseStatsThresholded",
    "CfprEtherRxStatsHistThresholded",
    "CfprEtherRxStatsThresholded",
    "CfprEtherSatelliteConnectionDisc",
    "CfprEtherServerIntFIoAdminState",
    "CfprEtherServerIntFIoFsmCurrentFsm",
    "CfprEtherServerIntFIoFsmStageName",
    "CfprEtherServerIntFIoFsmTaskItem",
    "CfprEtherServerIntFIoIfRole",
    "CfprEtherServerIntFIoLocale",
    "CfprEtherServerIntFIoPcEpIfRole",
    "CfprEtherServerIntFIoPcEpPortId",
    "CfprEtherServerIntFIoPcIfRole",
    "CfprEtherServerIntFIoPcPortId",
    "CfprEtherServerIntFIoPcTransport",
    "CfprEtherServerIntFIoPcType",
    "CfprEtherServerIntFIoTransport",
    "CfprEtherServerIntFIoType",
    "CfprEtherSwitchIntFIoAck",
    "CfprEtherSwitchIntFIoIfRole",
    "CfprEtherSwitchIntFIoLocale",
    "CfprEtherSwitchIntFIoPcEpIfRole",
    "CfprEtherSwitchIntFIoPcEpPortId",
    "CfprEtherSwitchIntFIoPcIfRole",
    "CfprEtherSwitchIntFIoPcPortId",
    "CfprEtherSwitchIntFIoPcTransport",
    "CfprEtherSwitchIntFIoPcType",
    "CfprEtherSwitchIntFIoTransport",
    "CfprEtherSwitchIntFIoType",
    "CfprEtherTxStatsHistThresholded",
    "CfprEtherTxStatsThresholded",
    "CfprFabricAdminState",
    "CfprFabricMembershipStatus",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprFsmLifecycle",
    "CfprLicenseState",
    "CfprNetworkConnectionType",
    "CfprNetworkLocale",
    "CfprNetworkPhysEpIfType",
    "CfprNetworkPortOperState",
    "CfprNetworkPortRole",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
    "CfprPortDuplex",
    "CfprPortEncap",
    "CfprPortEthSpeed",
    "CfprPortMode")

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

cfprEtherObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprEtherErrStatsTable_Object = MibTable
cfprEtherErrStatsTable = _CfprEtherErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1)
)
if mibBuilder.loadTexts:
    cfprEtherErrStatsTable.setStatus("current")
_CfprEtherErrStatsEntry_Object = MibTableRow
cfprEtherErrStatsEntry = _CfprEtherErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1)
)
cfprEtherErrStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherErrStatsEntry.setStatus("current")
_CfprEtherErrStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherErrStatsInstanceId_Object = MibTableColumn
cfprEtherErrStatsInstanceId = _CfprEtherErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 1),
    _CfprEtherErrStatsInstanceId_Type()
)
cfprEtherErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherErrStatsInstanceId.setStatus("current")
_CfprEtherErrStatsDn_Type = CfprManagedObjectDn
_CfprEtherErrStatsDn_Object = MibTableColumn
cfprEtherErrStatsDn = _CfprEtherErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 2),
    _CfprEtherErrStatsDn_Type()
)
cfprEtherErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsDn.setStatus("current")
_CfprEtherErrStatsRn_Type = SnmpAdminString
_CfprEtherErrStatsRn_Object = MibTableColumn
cfprEtherErrStatsRn = _CfprEtherErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 3),
    _CfprEtherErrStatsRn_Type()
)
cfprEtherErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsRn.setStatus("current")
_CfprEtherErrStatsAlign_Type = Unsigned64
_CfprEtherErrStatsAlign_Object = MibTableColumn
cfprEtherErrStatsAlign = _CfprEtherErrStatsAlign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 4),
    _CfprEtherErrStatsAlign_Type()
)
cfprEtherErrStatsAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsAlign.setStatus("current")
_CfprEtherErrStatsAlignDelta_Type = Counter64
_CfprEtherErrStatsAlignDelta_Object = MibTableColumn
cfprEtherErrStatsAlignDelta = _CfprEtherErrStatsAlignDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 5),
    _CfprEtherErrStatsAlignDelta_Type()
)
cfprEtherErrStatsAlignDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsAlignDelta.setStatus("current")
_CfprEtherErrStatsAlignDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsAlignDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsAlignDeltaAvg = _CfprEtherErrStatsAlignDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 6),
    _CfprEtherErrStatsAlignDeltaAvg_Type()
)
cfprEtherErrStatsAlignDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsAlignDeltaAvg.setStatus("current")
_CfprEtherErrStatsAlignDeltaMax_Type = Unsigned64
_CfprEtherErrStatsAlignDeltaMax_Object = MibTableColumn
cfprEtherErrStatsAlignDeltaMax = _CfprEtherErrStatsAlignDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 7),
    _CfprEtherErrStatsAlignDeltaMax_Type()
)
cfprEtherErrStatsAlignDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsAlignDeltaMax.setStatus("current")
_CfprEtherErrStatsAlignDeltaMin_Type = Unsigned64
_CfprEtherErrStatsAlignDeltaMin_Object = MibTableColumn
cfprEtherErrStatsAlignDeltaMin = _CfprEtherErrStatsAlignDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 8),
    _CfprEtherErrStatsAlignDeltaMin_Type()
)
cfprEtherErrStatsAlignDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsAlignDeltaMin.setStatus("current")
_CfprEtherErrStatsDeferredTx_Type = Unsigned64
_CfprEtherErrStatsDeferredTx_Object = MibTableColumn
cfprEtherErrStatsDeferredTx = _CfprEtherErrStatsDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 9),
    _CfprEtherErrStatsDeferredTx_Type()
)
cfprEtherErrStatsDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsDeferredTx.setStatus("current")
_CfprEtherErrStatsDeferredTxDelta_Type = Counter64
_CfprEtherErrStatsDeferredTxDelta_Object = MibTableColumn
cfprEtherErrStatsDeferredTxDelta = _CfprEtherErrStatsDeferredTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 10),
    _CfprEtherErrStatsDeferredTxDelta_Type()
)
cfprEtherErrStatsDeferredTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsDeferredTxDelta.setStatus("current")
_CfprEtherErrStatsDeferredTxDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsDeferredTxDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsDeferredTxDeltaAvg = _CfprEtherErrStatsDeferredTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 11),
    _CfprEtherErrStatsDeferredTxDeltaAvg_Type()
)
cfprEtherErrStatsDeferredTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsDeferredTxDeltaAvg.setStatus("current")
_CfprEtherErrStatsDeferredTxDeltaMax_Type = Unsigned64
_CfprEtherErrStatsDeferredTxDeltaMax_Object = MibTableColumn
cfprEtherErrStatsDeferredTxDeltaMax = _CfprEtherErrStatsDeferredTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 12),
    _CfprEtherErrStatsDeferredTxDeltaMax_Type()
)
cfprEtherErrStatsDeferredTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsDeferredTxDeltaMax.setStatus("current")
_CfprEtherErrStatsDeferredTxDeltaMin_Type = Unsigned64
_CfprEtherErrStatsDeferredTxDeltaMin_Object = MibTableColumn
cfprEtherErrStatsDeferredTxDeltaMin = _CfprEtherErrStatsDeferredTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 13),
    _CfprEtherErrStatsDeferredTxDeltaMin_Type()
)
cfprEtherErrStatsDeferredTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsDeferredTxDeltaMin.setStatus("current")
_CfprEtherErrStatsFcs_Type = Unsigned64
_CfprEtherErrStatsFcs_Object = MibTableColumn
cfprEtherErrStatsFcs = _CfprEtherErrStatsFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 14),
    _CfprEtherErrStatsFcs_Type()
)
cfprEtherErrStatsFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsFcs.setStatus("current")
_CfprEtherErrStatsFcsDelta_Type = Counter64
_CfprEtherErrStatsFcsDelta_Object = MibTableColumn
cfprEtherErrStatsFcsDelta = _CfprEtherErrStatsFcsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 15),
    _CfprEtherErrStatsFcsDelta_Type()
)
cfprEtherErrStatsFcsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsFcsDelta.setStatus("current")
_CfprEtherErrStatsFcsDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsFcsDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsFcsDeltaAvg = _CfprEtherErrStatsFcsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 16),
    _CfprEtherErrStatsFcsDeltaAvg_Type()
)
cfprEtherErrStatsFcsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsFcsDeltaAvg.setStatus("current")
_CfprEtherErrStatsFcsDeltaMax_Type = Unsigned64
_CfprEtherErrStatsFcsDeltaMax_Object = MibTableColumn
cfprEtherErrStatsFcsDeltaMax = _CfprEtherErrStatsFcsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 17),
    _CfprEtherErrStatsFcsDeltaMax_Type()
)
cfprEtherErrStatsFcsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsFcsDeltaMax.setStatus("current")
_CfprEtherErrStatsFcsDeltaMin_Type = Unsigned64
_CfprEtherErrStatsFcsDeltaMin_Object = MibTableColumn
cfprEtherErrStatsFcsDeltaMin = _CfprEtherErrStatsFcsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 18),
    _CfprEtherErrStatsFcsDeltaMin_Type()
)
cfprEtherErrStatsFcsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsFcsDeltaMin.setStatus("current")
_CfprEtherErrStatsIntMacRx_Type = Unsigned64
_CfprEtherErrStatsIntMacRx_Object = MibTableColumn
cfprEtherErrStatsIntMacRx = _CfprEtherErrStatsIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 19),
    _CfprEtherErrStatsIntMacRx_Type()
)
cfprEtherErrStatsIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacRx.setStatus("current")
_CfprEtherErrStatsIntMacRxDelta_Type = Counter64
_CfprEtherErrStatsIntMacRxDelta_Object = MibTableColumn
cfprEtherErrStatsIntMacRxDelta = _CfprEtherErrStatsIntMacRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 20),
    _CfprEtherErrStatsIntMacRxDelta_Type()
)
cfprEtherErrStatsIntMacRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacRxDelta.setStatus("current")
_CfprEtherErrStatsIntMacRxDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsIntMacRxDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsIntMacRxDeltaAvg = _CfprEtherErrStatsIntMacRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 21),
    _CfprEtherErrStatsIntMacRxDeltaAvg_Type()
)
cfprEtherErrStatsIntMacRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacRxDeltaAvg.setStatus("current")
_CfprEtherErrStatsIntMacRxDeltaMax_Type = Unsigned64
_CfprEtherErrStatsIntMacRxDeltaMax_Object = MibTableColumn
cfprEtherErrStatsIntMacRxDeltaMax = _CfprEtherErrStatsIntMacRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 22),
    _CfprEtherErrStatsIntMacRxDeltaMax_Type()
)
cfprEtherErrStatsIntMacRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacRxDeltaMax.setStatus("current")
_CfprEtherErrStatsIntMacRxDeltaMin_Type = Unsigned64
_CfprEtherErrStatsIntMacRxDeltaMin_Object = MibTableColumn
cfprEtherErrStatsIntMacRxDeltaMin = _CfprEtherErrStatsIntMacRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 23),
    _CfprEtherErrStatsIntMacRxDeltaMin_Type()
)
cfprEtherErrStatsIntMacRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacRxDeltaMin.setStatus("current")
_CfprEtherErrStatsIntMacTx_Type = Unsigned64
_CfprEtherErrStatsIntMacTx_Object = MibTableColumn
cfprEtherErrStatsIntMacTx = _CfprEtherErrStatsIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 24),
    _CfprEtherErrStatsIntMacTx_Type()
)
cfprEtherErrStatsIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacTx.setStatus("current")
_CfprEtherErrStatsIntMacTxDelta_Type = Counter64
_CfprEtherErrStatsIntMacTxDelta_Object = MibTableColumn
cfprEtherErrStatsIntMacTxDelta = _CfprEtherErrStatsIntMacTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 25),
    _CfprEtherErrStatsIntMacTxDelta_Type()
)
cfprEtherErrStatsIntMacTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacTxDelta.setStatus("current")
_CfprEtherErrStatsIntMacTxDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsIntMacTxDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsIntMacTxDeltaAvg = _CfprEtherErrStatsIntMacTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 26),
    _CfprEtherErrStatsIntMacTxDeltaAvg_Type()
)
cfprEtherErrStatsIntMacTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacTxDeltaAvg.setStatus("current")
_CfprEtherErrStatsIntMacTxDeltaMax_Type = Unsigned64
_CfprEtherErrStatsIntMacTxDeltaMax_Object = MibTableColumn
cfprEtherErrStatsIntMacTxDeltaMax = _CfprEtherErrStatsIntMacTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 27),
    _CfprEtherErrStatsIntMacTxDeltaMax_Type()
)
cfprEtherErrStatsIntMacTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacTxDeltaMax.setStatus("current")
_CfprEtherErrStatsIntMacTxDeltaMin_Type = Unsigned64
_CfprEtherErrStatsIntMacTxDeltaMin_Object = MibTableColumn
cfprEtherErrStatsIntMacTxDeltaMin = _CfprEtherErrStatsIntMacTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 28),
    _CfprEtherErrStatsIntMacTxDeltaMin_Type()
)
cfprEtherErrStatsIntMacTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntMacTxDeltaMin.setStatus("current")
_CfprEtherErrStatsIntervals_Type = Gauge32
_CfprEtherErrStatsIntervals_Object = MibTableColumn
cfprEtherErrStatsIntervals = _CfprEtherErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 29),
    _CfprEtherErrStatsIntervals_Type()
)
cfprEtherErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsIntervals.setStatus("current")
_CfprEtherErrStatsOutDiscard_Type = Unsigned64
_CfprEtherErrStatsOutDiscard_Object = MibTableColumn
cfprEtherErrStatsOutDiscard = _CfprEtherErrStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 30),
    _CfprEtherErrStatsOutDiscard_Type()
)
cfprEtherErrStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsOutDiscard.setStatus("current")
_CfprEtherErrStatsOutDiscardDelta_Type = Counter64
_CfprEtherErrStatsOutDiscardDelta_Object = MibTableColumn
cfprEtherErrStatsOutDiscardDelta = _CfprEtherErrStatsOutDiscardDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 31),
    _CfprEtherErrStatsOutDiscardDelta_Type()
)
cfprEtherErrStatsOutDiscardDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsOutDiscardDelta.setStatus("current")
_CfprEtherErrStatsOutDiscardDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsOutDiscardDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsOutDiscardDeltaAvg = _CfprEtherErrStatsOutDiscardDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 32),
    _CfprEtherErrStatsOutDiscardDeltaAvg_Type()
)
cfprEtherErrStatsOutDiscardDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsOutDiscardDeltaAvg.setStatus("current")
_CfprEtherErrStatsOutDiscardDeltaMax_Type = Unsigned64
_CfprEtherErrStatsOutDiscardDeltaMax_Object = MibTableColumn
cfprEtherErrStatsOutDiscardDeltaMax = _CfprEtherErrStatsOutDiscardDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 33),
    _CfprEtherErrStatsOutDiscardDeltaMax_Type()
)
cfprEtherErrStatsOutDiscardDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsOutDiscardDeltaMax.setStatus("current")
_CfprEtherErrStatsOutDiscardDeltaMin_Type = Unsigned64
_CfprEtherErrStatsOutDiscardDeltaMin_Object = MibTableColumn
cfprEtherErrStatsOutDiscardDeltaMin = _CfprEtherErrStatsOutDiscardDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 34),
    _CfprEtherErrStatsOutDiscardDeltaMin_Type()
)
cfprEtherErrStatsOutDiscardDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsOutDiscardDeltaMin.setStatus("current")
_CfprEtherErrStatsRcv_Type = Unsigned64
_CfprEtherErrStatsRcv_Object = MibTableColumn
cfprEtherErrStatsRcv = _CfprEtherErrStatsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 35),
    _CfprEtherErrStatsRcv_Type()
)
cfprEtherErrStatsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsRcv.setStatus("current")
_CfprEtherErrStatsRcvDelta_Type = Counter64
_CfprEtherErrStatsRcvDelta_Object = MibTableColumn
cfprEtherErrStatsRcvDelta = _CfprEtherErrStatsRcvDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 36),
    _CfprEtherErrStatsRcvDelta_Type()
)
cfprEtherErrStatsRcvDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsRcvDelta.setStatus("current")
_CfprEtherErrStatsRcvDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsRcvDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsRcvDeltaAvg = _CfprEtherErrStatsRcvDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 37),
    _CfprEtherErrStatsRcvDeltaAvg_Type()
)
cfprEtherErrStatsRcvDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsRcvDeltaAvg.setStatus("current")
_CfprEtherErrStatsRcvDeltaMax_Type = Unsigned64
_CfprEtherErrStatsRcvDeltaMax_Object = MibTableColumn
cfprEtherErrStatsRcvDeltaMax = _CfprEtherErrStatsRcvDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 38),
    _CfprEtherErrStatsRcvDeltaMax_Type()
)
cfprEtherErrStatsRcvDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsRcvDeltaMax.setStatus("current")
_CfprEtherErrStatsRcvDeltaMin_Type = Unsigned64
_CfprEtherErrStatsRcvDeltaMin_Object = MibTableColumn
cfprEtherErrStatsRcvDeltaMin = _CfprEtherErrStatsRcvDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 39),
    _CfprEtherErrStatsRcvDeltaMin_Type()
)
cfprEtherErrStatsRcvDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsRcvDeltaMin.setStatus("current")
_CfprEtherErrStatsSuspect_Type = TruthValue
_CfprEtherErrStatsSuspect_Object = MibTableColumn
cfprEtherErrStatsSuspect = _CfprEtherErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 40),
    _CfprEtherErrStatsSuspect_Type()
)
cfprEtherErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsSuspect.setStatus("current")
_CfprEtherErrStatsThresholded_Type = CfprEtherErrStatsThresholded
_CfprEtherErrStatsThresholded_Object = MibTableColumn
cfprEtherErrStatsThresholded = _CfprEtherErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 41),
    _CfprEtherErrStatsThresholded_Type()
)
cfprEtherErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsThresholded.setStatus("current")
_CfprEtherErrStatsTimeCollected_Type = DateAndTime
_CfprEtherErrStatsTimeCollected_Object = MibTableColumn
cfprEtherErrStatsTimeCollected = _CfprEtherErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 42),
    _CfprEtherErrStatsTimeCollected_Type()
)
cfprEtherErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsTimeCollected.setStatus("current")
_CfprEtherErrStatsUnderSize_Type = Unsigned64
_CfprEtherErrStatsUnderSize_Object = MibTableColumn
cfprEtherErrStatsUnderSize = _CfprEtherErrStatsUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 43),
    _CfprEtherErrStatsUnderSize_Type()
)
cfprEtherErrStatsUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsUnderSize.setStatus("current")
_CfprEtherErrStatsUnderSizeDelta_Type = Counter64
_CfprEtherErrStatsUnderSizeDelta_Object = MibTableColumn
cfprEtherErrStatsUnderSizeDelta = _CfprEtherErrStatsUnderSizeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 44),
    _CfprEtherErrStatsUnderSizeDelta_Type()
)
cfprEtherErrStatsUnderSizeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsUnderSizeDelta.setStatus("current")
_CfprEtherErrStatsUnderSizeDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsUnderSizeDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsUnderSizeDeltaAvg = _CfprEtherErrStatsUnderSizeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 45),
    _CfprEtherErrStatsUnderSizeDeltaAvg_Type()
)
cfprEtherErrStatsUnderSizeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsUnderSizeDeltaAvg.setStatus("current")
_CfprEtherErrStatsUnderSizeDeltaMax_Type = Unsigned64
_CfprEtherErrStatsUnderSizeDeltaMax_Object = MibTableColumn
cfprEtherErrStatsUnderSizeDeltaMax = _CfprEtherErrStatsUnderSizeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 46),
    _CfprEtherErrStatsUnderSizeDeltaMax_Type()
)
cfprEtherErrStatsUnderSizeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsUnderSizeDeltaMax.setStatus("current")
_CfprEtherErrStatsUnderSizeDeltaMin_Type = Unsigned64
_CfprEtherErrStatsUnderSizeDeltaMin_Object = MibTableColumn
cfprEtherErrStatsUnderSizeDeltaMin = _CfprEtherErrStatsUnderSizeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 47),
    _CfprEtherErrStatsUnderSizeDeltaMin_Type()
)
cfprEtherErrStatsUnderSizeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsUnderSizeDeltaMin.setStatus("current")
_CfprEtherErrStatsUpdate_Type = Gauge32
_CfprEtherErrStatsUpdate_Object = MibTableColumn
cfprEtherErrStatsUpdate = _CfprEtherErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 48),
    _CfprEtherErrStatsUpdate_Type()
)
cfprEtherErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsUpdate.setStatus("current")
_CfprEtherErrStatsXmit_Type = Unsigned64
_CfprEtherErrStatsXmit_Object = MibTableColumn
cfprEtherErrStatsXmit = _CfprEtherErrStatsXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 49),
    _CfprEtherErrStatsXmit_Type()
)
cfprEtherErrStatsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsXmit.setStatus("current")
_CfprEtherErrStatsXmitDelta_Type = Counter64
_CfprEtherErrStatsXmitDelta_Object = MibTableColumn
cfprEtherErrStatsXmitDelta = _CfprEtherErrStatsXmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 50),
    _CfprEtherErrStatsXmitDelta_Type()
)
cfprEtherErrStatsXmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsXmitDelta.setStatus("current")
_CfprEtherErrStatsXmitDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsXmitDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsXmitDeltaAvg = _CfprEtherErrStatsXmitDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 51),
    _CfprEtherErrStatsXmitDeltaAvg_Type()
)
cfprEtherErrStatsXmitDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsXmitDeltaAvg.setStatus("current")
_CfprEtherErrStatsXmitDeltaMax_Type = Unsigned64
_CfprEtherErrStatsXmitDeltaMax_Object = MibTableColumn
cfprEtherErrStatsXmitDeltaMax = _CfprEtherErrStatsXmitDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 52),
    _CfprEtherErrStatsXmitDeltaMax_Type()
)
cfprEtherErrStatsXmitDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsXmitDeltaMax.setStatus("current")
_CfprEtherErrStatsXmitDeltaMin_Type = Unsigned64
_CfprEtherErrStatsXmitDeltaMin_Object = MibTableColumn
cfprEtherErrStatsXmitDeltaMin = _CfprEtherErrStatsXmitDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 1, 1, 53),
    _CfprEtherErrStatsXmitDeltaMin_Type()
)
cfprEtherErrStatsXmitDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsXmitDeltaMin.setStatus("current")
_CfprEtherErrStatsHistTable_Object = MibTable
cfprEtherErrStatsHistTable = _CfprEtherErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2)
)
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistTable.setStatus("current")
_CfprEtherErrStatsHistEntry_Object = MibTableRow
cfprEtherErrStatsHistEntry = _CfprEtherErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1)
)
cfprEtherErrStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistEntry.setStatus("current")
_CfprEtherErrStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherErrStatsHistInstanceId_Object = MibTableColumn
cfprEtherErrStatsHistInstanceId = _CfprEtherErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 1),
    _CfprEtherErrStatsHistInstanceId_Type()
)
cfprEtherErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistInstanceId.setStatus("current")
_CfprEtherErrStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherErrStatsHistDn_Object = MibTableColumn
cfprEtherErrStatsHistDn = _CfprEtherErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 2),
    _CfprEtherErrStatsHistDn_Type()
)
cfprEtherErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistDn.setStatus("current")
_CfprEtherErrStatsHistRn_Type = SnmpAdminString
_CfprEtherErrStatsHistRn_Object = MibTableColumn
cfprEtherErrStatsHistRn = _CfprEtherErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 3),
    _CfprEtherErrStatsHistRn_Type()
)
cfprEtherErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistRn.setStatus("current")
_CfprEtherErrStatsHistAlign_Type = Unsigned64
_CfprEtherErrStatsHistAlign_Object = MibTableColumn
cfprEtherErrStatsHistAlign = _CfprEtherErrStatsHistAlign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 4),
    _CfprEtherErrStatsHistAlign_Type()
)
cfprEtherErrStatsHistAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistAlign.setStatus("current")
_CfprEtherErrStatsHistAlignDelta_Type = Unsigned64
_CfprEtherErrStatsHistAlignDelta_Object = MibTableColumn
cfprEtherErrStatsHistAlignDelta = _CfprEtherErrStatsHistAlignDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 5),
    _CfprEtherErrStatsHistAlignDelta_Type()
)
cfprEtherErrStatsHistAlignDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistAlignDelta.setStatus("current")
_CfprEtherErrStatsHistAlignDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistAlignDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistAlignDeltaAvg = _CfprEtherErrStatsHistAlignDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 6),
    _CfprEtherErrStatsHistAlignDeltaAvg_Type()
)
cfprEtherErrStatsHistAlignDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistAlignDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistAlignDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistAlignDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistAlignDeltaMax = _CfprEtherErrStatsHistAlignDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 7),
    _CfprEtherErrStatsHistAlignDeltaMax_Type()
)
cfprEtherErrStatsHistAlignDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistAlignDeltaMax.setStatus("current")
_CfprEtherErrStatsHistAlignDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistAlignDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistAlignDeltaMin = _CfprEtherErrStatsHistAlignDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 8),
    _CfprEtherErrStatsHistAlignDeltaMin_Type()
)
cfprEtherErrStatsHistAlignDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistAlignDeltaMin.setStatus("current")
_CfprEtherErrStatsHistDeferredTx_Type = Unsigned64
_CfprEtherErrStatsHistDeferredTx_Object = MibTableColumn
cfprEtherErrStatsHistDeferredTx = _CfprEtherErrStatsHistDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 9),
    _CfprEtherErrStatsHistDeferredTx_Type()
)
cfprEtherErrStatsHistDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistDeferredTx.setStatus("current")
_CfprEtherErrStatsHistDeferredTxDelta_Type = Unsigned64
_CfprEtherErrStatsHistDeferredTxDelta_Object = MibTableColumn
cfprEtherErrStatsHistDeferredTxDelta = _CfprEtherErrStatsHistDeferredTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 10),
    _CfprEtherErrStatsHistDeferredTxDelta_Type()
)
cfprEtherErrStatsHistDeferredTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistDeferredTxDelta.setStatus("current")
_CfprEtherErrStatsHistDeferredTxDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistDeferredTxDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistDeferredTxDeltaAvg = _CfprEtherErrStatsHistDeferredTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 11),
    _CfprEtherErrStatsHistDeferredTxDeltaAvg_Type()
)
cfprEtherErrStatsHistDeferredTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistDeferredTxDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistDeferredTxDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistDeferredTxDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistDeferredTxDeltaMax = _CfprEtherErrStatsHistDeferredTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 12),
    _CfprEtherErrStatsHistDeferredTxDeltaMax_Type()
)
cfprEtherErrStatsHistDeferredTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistDeferredTxDeltaMax.setStatus("current")
_CfprEtherErrStatsHistDeferredTxDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistDeferredTxDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistDeferredTxDeltaMin = _CfprEtherErrStatsHistDeferredTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 13),
    _CfprEtherErrStatsHistDeferredTxDeltaMin_Type()
)
cfprEtherErrStatsHistDeferredTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistDeferredTxDeltaMin.setStatus("current")
_CfprEtherErrStatsHistFcs_Type = Unsigned64
_CfprEtherErrStatsHistFcs_Object = MibTableColumn
cfprEtherErrStatsHistFcs = _CfprEtherErrStatsHistFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 14),
    _CfprEtherErrStatsHistFcs_Type()
)
cfprEtherErrStatsHistFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistFcs.setStatus("current")
_CfprEtherErrStatsHistFcsDelta_Type = Unsigned64
_CfprEtherErrStatsHistFcsDelta_Object = MibTableColumn
cfprEtherErrStatsHistFcsDelta = _CfprEtherErrStatsHistFcsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 15),
    _CfprEtherErrStatsHistFcsDelta_Type()
)
cfprEtherErrStatsHistFcsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistFcsDelta.setStatus("current")
_CfprEtherErrStatsHistFcsDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistFcsDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistFcsDeltaAvg = _CfprEtherErrStatsHistFcsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 16),
    _CfprEtherErrStatsHistFcsDeltaAvg_Type()
)
cfprEtherErrStatsHistFcsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistFcsDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistFcsDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistFcsDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistFcsDeltaMax = _CfprEtherErrStatsHistFcsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 17),
    _CfprEtherErrStatsHistFcsDeltaMax_Type()
)
cfprEtherErrStatsHistFcsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistFcsDeltaMax.setStatus("current")
_CfprEtherErrStatsHistFcsDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistFcsDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistFcsDeltaMin = _CfprEtherErrStatsHistFcsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 18),
    _CfprEtherErrStatsHistFcsDeltaMin_Type()
)
cfprEtherErrStatsHistFcsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistFcsDeltaMin.setStatus("current")
_CfprEtherErrStatsHistId_Type = Unsigned64
_CfprEtherErrStatsHistId_Object = MibTableColumn
cfprEtherErrStatsHistId = _CfprEtherErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 19),
    _CfprEtherErrStatsHistId_Type()
)
cfprEtherErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistId.setStatus("current")
_CfprEtherErrStatsHistIntMacRx_Type = Unsigned64
_CfprEtherErrStatsHistIntMacRx_Object = MibTableColumn
cfprEtherErrStatsHistIntMacRx = _CfprEtherErrStatsHistIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 20),
    _CfprEtherErrStatsHistIntMacRx_Type()
)
cfprEtherErrStatsHistIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacRx.setStatus("current")
_CfprEtherErrStatsHistIntMacRxDelta_Type = Unsigned64
_CfprEtherErrStatsHistIntMacRxDelta_Object = MibTableColumn
cfprEtherErrStatsHistIntMacRxDelta = _CfprEtherErrStatsHistIntMacRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 21),
    _CfprEtherErrStatsHistIntMacRxDelta_Type()
)
cfprEtherErrStatsHistIntMacRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacRxDelta.setStatus("current")
_CfprEtherErrStatsHistIntMacRxDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistIntMacRxDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistIntMacRxDeltaAvg = _CfprEtherErrStatsHistIntMacRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 22),
    _CfprEtherErrStatsHistIntMacRxDeltaAvg_Type()
)
cfprEtherErrStatsHistIntMacRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacRxDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistIntMacRxDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistIntMacRxDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistIntMacRxDeltaMax = _CfprEtherErrStatsHistIntMacRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 23),
    _CfprEtherErrStatsHistIntMacRxDeltaMax_Type()
)
cfprEtherErrStatsHistIntMacRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacRxDeltaMax.setStatus("current")
_CfprEtherErrStatsHistIntMacRxDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistIntMacRxDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistIntMacRxDeltaMin = _CfprEtherErrStatsHistIntMacRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 24),
    _CfprEtherErrStatsHistIntMacRxDeltaMin_Type()
)
cfprEtherErrStatsHistIntMacRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacRxDeltaMin.setStatus("current")
_CfprEtherErrStatsHistIntMacTx_Type = Unsigned64
_CfprEtherErrStatsHistIntMacTx_Object = MibTableColumn
cfprEtherErrStatsHistIntMacTx = _CfprEtherErrStatsHistIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 25),
    _CfprEtherErrStatsHistIntMacTx_Type()
)
cfprEtherErrStatsHistIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacTx.setStatus("current")
_CfprEtherErrStatsHistIntMacTxDelta_Type = Unsigned64
_CfprEtherErrStatsHistIntMacTxDelta_Object = MibTableColumn
cfprEtherErrStatsHistIntMacTxDelta = _CfprEtherErrStatsHistIntMacTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 26),
    _CfprEtherErrStatsHistIntMacTxDelta_Type()
)
cfprEtherErrStatsHistIntMacTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacTxDelta.setStatus("current")
_CfprEtherErrStatsHistIntMacTxDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistIntMacTxDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistIntMacTxDeltaAvg = _CfprEtherErrStatsHistIntMacTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 27),
    _CfprEtherErrStatsHistIntMacTxDeltaAvg_Type()
)
cfprEtherErrStatsHistIntMacTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacTxDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistIntMacTxDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistIntMacTxDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistIntMacTxDeltaMax = _CfprEtherErrStatsHistIntMacTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 28),
    _CfprEtherErrStatsHistIntMacTxDeltaMax_Type()
)
cfprEtherErrStatsHistIntMacTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacTxDeltaMax.setStatus("current")
_CfprEtherErrStatsHistIntMacTxDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistIntMacTxDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistIntMacTxDeltaMin = _CfprEtherErrStatsHistIntMacTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 29),
    _CfprEtherErrStatsHistIntMacTxDeltaMin_Type()
)
cfprEtherErrStatsHistIntMacTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistIntMacTxDeltaMin.setStatus("current")
_CfprEtherErrStatsHistMostRecent_Type = TruthValue
_CfprEtherErrStatsHistMostRecent_Object = MibTableColumn
cfprEtherErrStatsHistMostRecent = _CfprEtherErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 30),
    _CfprEtherErrStatsHistMostRecent_Type()
)
cfprEtherErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistMostRecent.setStatus("current")
_CfprEtherErrStatsHistOutDiscard_Type = Unsigned64
_CfprEtherErrStatsHistOutDiscard_Object = MibTableColumn
cfprEtherErrStatsHistOutDiscard = _CfprEtherErrStatsHistOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 31),
    _CfprEtherErrStatsHistOutDiscard_Type()
)
cfprEtherErrStatsHistOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistOutDiscard.setStatus("current")
_CfprEtherErrStatsHistOutDiscardDelta_Type = Unsigned64
_CfprEtherErrStatsHistOutDiscardDelta_Object = MibTableColumn
cfprEtherErrStatsHistOutDiscardDelta = _CfprEtherErrStatsHistOutDiscardDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 32),
    _CfprEtherErrStatsHistOutDiscardDelta_Type()
)
cfprEtherErrStatsHistOutDiscardDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistOutDiscardDelta.setStatus("current")
_CfprEtherErrStatsHistOutDiscardDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistOutDiscardDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistOutDiscardDeltaAvg = _CfprEtherErrStatsHistOutDiscardDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 33),
    _CfprEtherErrStatsHistOutDiscardDeltaAvg_Type()
)
cfprEtherErrStatsHistOutDiscardDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistOutDiscardDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistOutDiscardDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistOutDiscardDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistOutDiscardDeltaMax = _CfprEtherErrStatsHistOutDiscardDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 34),
    _CfprEtherErrStatsHistOutDiscardDeltaMax_Type()
)
cfprEtherErrStatsHistOutDiscardDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistOutDiscardDeltaMax.setStatus("current")
_CfprEtherErrStatsHistOutDiscardDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistOutDiscardDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistOutDiscardDeltaMin = _CfprEtherErrStatsHistOutDiscardDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 35),
    _CfprEtherErrStatsHistOutDiscardDeltaMin_Type()
)
cfprEtherErrStatsHistOutDiscardDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistOutDiscardDeltaMin.setStatus("current")
_CfprEtherErrStatsHistRcv_Type = Unsigned64
_CfprEtherErrStatsHistRcv_Object = MibTableColumn
cfprEtherErrStatsHistRcv = _CfprEtherErrStatsHistRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 36),
    _CfprEtherErrStatsHistRcv_Type()
)
cfprEtherErrStatsHistRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistRcv.setStatus("current")
_CfprEtherErrStatsHistRcvDelta_Type = Unsigned64
_CfprEtherErrStatsHistRcvDelta_Object = MibTableColumn
cfprEtherErrStatsHistRcvDelta = _CfprEtherErrStatsHistRcvDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 37),
    _CfprEtherErrStatsHistRcvDelta_Type()
)
cfprEtherErrStatsHistRcvDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistRcvDelta.setStatus("current")
_CfprEtherErrStatsHistRcvDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistRcvDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistRcvDeltaAvg = _CfprEtherErrStatsHistRcvDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 38),
    _CfprEtherErrStatsHistRcvDeltaAvg_Type()
)
cfprEtherErrStatsHistRcvDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistRcvDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistRcvDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistRcvDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistRcvDeltaMax = _CfprEtherErrStatsHistRcvDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 39),
    _CfprEtherErrStatsHistRcvDeltaMax_Type()
)
cfprEtherErrStatsHistRcvDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistRcvDeltaMax.setStatus("current")
_CfprEtherErrStatsHistRcvDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistRcvDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistRcvDeltaMin = _CfprEtherErrStatsHistRcvDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 40),
    _CfprEtherErrStatsHistRcvDeltaMin_Type()
)
cfprEtherErrStatsHistRcvDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistRcvDeltaMin.setStatus("current")
_CfprEtherErrStatsHistSuspect_Type = TruthValue
_CfprEtherErrStatsHistSuspect_Object = MibTableColumn
cfprEtherErrStatsHistSuspect = _CfprEtherErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 41),
    _CfprEtherErrStatsHistSuspect_Type()
)
cfprEtherErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistSuspect.setStatus("current")
_CfprEtherErrStatsHistThresholded_Type = CfprEtherErrStatsHistThresholded
_CfprEtherErrStatsHistThresholded_Object = MibTableColumn
cfprEtherErrStatsHistThresholded = _CfprEtherErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 42),
    _CfprEtherErrStatsHistThresholded_Type()
)
cfprEtherErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistThresholded.setStatus("current")
_CfprEtherErrStatsHistTimeCollected_Type = DateAndTime
_CfprEtherErrStatsHistTimeCollected_Object = MibTableColumn
cfprEtherErrStatsHistTimeCollected = _CfprEtherErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 43),
    _CfprEtherErrStatsHistTimeCollected_Type()
)
cfprEtherErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistTimeCollected.setStatus("current")
_CfprEtherErrStatsHistUnderSize_Type = Unsigned64
_CfprEtherErrStatsHistUnderSize_Object = MibTableColumn
cfprEtherErrStatsHistUnderSize = _CfprEtherErrStatsHistUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 44),
    _CfprEtherErrStatsHistUnderSize_Type()
)
cfprEtherErrStatsHistUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistUnderSize.setStatus("current")
_CfprEtherErrStatsHistUnderSizeDelta_Type = Unsigned64
_CfprEtherErrStatsHistUnderSizeDelta_Object = MibTableColumn
cfprEtherErrStatsHistUnderSizeDelta = _CfprEtherErrStatsHistUnderSizeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 45),
    _CfprEtherErrStatsHistUnderSizeDelta_Type()
)
cfprEtherErrStatsHistUnderSizeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistUnderSizeDelta.setStatus("current")
_CfprEtherErrStatsHistUnderSizeDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistUnderSizeDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistUnderSizeDeltaAvg = _CfprEtherErrStatsHistUnderSizeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 46),
    _CfprEtherErrStatsHistUnderSizeDeltaAvg_Type()
)
cfprEtherErrStatsHistUnderSizeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistUnderSizeDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistUnderSizeDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistUnderSizeDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistUnderSizeDeltaMax = _CfprEtherErrStatsHistUnderSizeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 47),
    _CfprEtherErrStatsHistUnderSizeDeltaMax_Type()
)
cfprEtherErrStatsHistUnderSizeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistUnderSizeDeltaMax.setStatus("current")
_CfprEtherErrStatsHistUnderSizeDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistUnderSizeDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistUnderSizeDeltaMin = _CfprEtherErrStatsHistUnderSizeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 48),
    _CfprEtherErrStatsHistUnderSizeDeltaMin_Type()
)
cfprEtherErrStatsHistUnderSizeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistUnderSizeDeltaMin.setStatus("current")
_CfprEtherErrStatsHistXmit_Type = Unsigned64
_CfprEtherErrStatsHistXmit_Object = MibTableColumn
cfprEtherErrStatsHistXmit = _CfprEtherErrStatsHistXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 49),
    _CfprEtherErrStatsHistXmit_Type()
)
cfprEtherErrStatsHistXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistXmit.setStatus("current")
_CfprEtherErrStatsHistXmitDelta_Type = Unsigned64
_CfprEtherErrStatsHistXmitDelta_Object = MibTableColumn
cfprEtherErrStatsHistXmitDelta = _CfprEtherErrStatsHistXmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 50),
    _CfprEtherErrStatsHistXmitDelta_Type()
)
cfprEtherErrStatsHistXmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistXmitDelta.setStatus("current")
_CfprEtherErrStatsHistXmitDeltaAvg_Type = Unsigned64
_CfprEtherErrStatsHistXmitDeltaAvg_Object = MibTableColumn
cfprEtherErrStatsHistXmitDeltaAvg = _CfprEtherErrStatsHistXmitDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 51),
    _CfprEtherErrStatsHistXmitDeltaAvg_Type()
)
cfprEtherErrStatsHistXmitDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistXmitDeltaAvg.setStatus("current")
_CfprEtherErrStatsHistXmitDeltaMax_Type = Unsigned64
_CfprEtherErrStatsHistXmitDeltaMax_Object = MibTableColumn
cfprEtherErrStatsHistXmitDeltaMax = _CfprEtherErrStatsHistXmitDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 52),
    _CfprEtherErrStatsHistXmitDeltaMax_Type()
)
cfprEtherErrStatsHistXmitDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistXmitDeltaMax.setStatus("current")
_CfprEtherErrStatsHistXmitDeltaMin_Type = Unsigned64
_CfprEtherErrStatsHistXmitDeltaMin_Object = MibTableColumn
cfprEtherErrStatsHistXmitDeltaMin = _CfprEtherErrStatsHistXmitDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 2, 1, 53),
    _CfprEtherErrStatsHistXmitDeltaMin_Type()
)
cfprEtherErrStatsHistXmitDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherErrStatsHistXmitDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsTable_Object = MibTable
cfprEtherFcoeInterfaceStatsTable = _CfprEtherFcoeInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3)
)
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsTable.setStatus("current")
_CfprEtherFcoeInterfaceStatsEntry_Object = MibTableRow
cfprEtherFcoeInterfaceStatsEntry = _CfprEtherFcoeInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1)
)
cfprEtherFcoeInterfaceStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFcoeInterfaceStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsEntry.setStatus("current")
_CfprEtherFcoeInterfaceStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherFcoeInterfaceStatsInstanceId_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsInstanceId = _CfprEtherFcoeInterfaceStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 1),
    _CfprEtherFcoeInterfaceStatsInstanceId_Type()
)
cfprEtherFcoeInterfaceStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsInstanceId.setStatus("current")
_CfprEtherFcoeInterfaceStatsDn_Type = CfprManagedObjectDn
_CfprEtherFcoeInterfaceStatsDn_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDn = _CfprEtherFcoeInterfaceStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 2),
    _CfprEtherFcoeInterfaceStatsDn_Type()
)
cfprEtherFcoeInterfaceStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDn.setStatus("current")
_CfprEtherFcoeInterfaceStatsRn_Type = SnmpAdminString
_CfprEtherFcoeInterfaceStatsRn_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsRn = _CfprEtherFcoeInterfaceStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 3),
    _CfprEtherFcoeInterfaceStatsRn_Type()
)
cfprEtherFcoeInterfaceStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsRn.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRx = _CfprEtherFcoeInterfaceStatsBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 4),
    _CfprEtherFcoeInterfaceStatsBytesRx_Type()
)
cfprEtherFcoeInterfaceStatsBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesRxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsBytesRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDelta = _CfprEtherFcoeInterfaceStatsBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 5),
    _CfprEtherFcoeInterfaceStatsBytesRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg = _CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 6),
    _CfprEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDeltaMax = _CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 7),
    _CfprEtherFcoeInterfaceStatsBytesRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesRxDeltaMin = _CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 8),
    _CfprEtherFcoeInterfaceStatsBytesRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTx = _CfprEtherFcoeInterfaceStatsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 9),
    _CfprEtherFcoeInterfaceStatsBytesTx_Type()
)
cfprEtherFcoeInterfaceStatsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesTxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsBytesTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDelta = _CfprEtherFcoeInterfaceStatsBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 10),
    _CfprEtherFcoeInterfaceStatsBytesTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg = _CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 11),
    _CfprEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDeltaMax = _CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 12),
    _CfprEtherFcoeInterfaceStatsBytesTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsBytesTxDeltaMin = _CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 13),
    _CfprEtherFcoeInterfaceStatsBytesTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsBytesTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRx = _CfprEtherFcoeInterfaceStatsDroppedRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 14),
    _CfprEtherFcoeInterfaceStatsDroppedRx_Type()
)
cfprEtherFcoeInterfaceStatsDroppedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedRxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsDroppedRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDelta = _CfprEtherFcoeInterfaceStatsDroppedRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 15),
    _CfprEtherFcoeInterfaceStatsDroppedRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsDroppedRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg = _CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 16),
    _CfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax = _CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 17),
    _CfprEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin = _CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 18),
    _CfprEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTx = _CfprEtherFcoeInterfaceStatsDroppedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 19),
    _CfprEtherFcoeInterfaceStatsDroppedTx_Type()
)
cfprEtherFcoeInterfaceStatsDroppedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedTxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsDroppedTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDelta = _CfprEtherFcoeInterfaceStatsDroppedTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 20),
    _CfprEtherFcoeInterfaceStatsDroppedTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsDroppedTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg = _CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 21),
    _CfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax = _CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 22),
    _CfprEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin = _CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 23),
    _CfprEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRx = _CfprEtherFcoeInterfaceStatsErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 24),
    _CfprEtherFcoeInterfaceStatsErrorsRx_Type()
)
cfprEtherFcoeInterfaceStatsErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsRxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsErrorsRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDelta = _CfprEtherFcoeInterfaceStatsErrorsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 25),
    _CfprEtherFcoeInterfaceStatsErrorsRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsErrorsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg = _CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 26),
    _CfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax = _CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 27),
    _CfprEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin = _CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 28),
    _CfprEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTx = _CfprEtherFcoeInterfaceStatsErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 29),
    _CfprEtherFcoeInterfaceStatsErrorsTx_Type()
)
cfprEtherFcoeInterfaceStatsErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsTxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsErrorsTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDelta = _CfprEtherFcoeInterfaceStatsErrorsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 30),
    _CfprEtherFcoeInterfaceStatsErrorsTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsErrorsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg = _CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 31),
    _CfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax = _CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 32),
    _CfprEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin = _CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 33),
    _CfprEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsIntervals_Type = Gauge32
_CfprEtherFcoeInterfaceStatsIntervals_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsIntervals = _CfprEtherFcoeInterfaceStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 34),
    _CfprEtherFcoeInterfaceStatsIntervals_Type()
)
cfprEtherFcoeInterfaceStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsIntervals.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRx = _CfprEtherFcoeInterfaceStatsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 35),
    _CfprEtherFcoeInterfaceStatsPacketsRx_Type()
)
cfprEtherFcoeInterfaceStatsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsRxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsPacketsRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDelta = _CfprEtherFcoeInterfaceStatsPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 36),
    _CfprEtherFcoeInterfaceStatsPacketsRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg = _CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 37),
    _CfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax = _CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 38),
    _CfprEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin = _CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 39),
    _CfprEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTx = _CfprEtherFcoeInterfaceStatsPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 40),
    _CfprEtherFcoeInterfaceStatsPacketsTx_Type()
)
cfprEtherFcoeInterfaceStatsPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsTxDelta_Type = Counter64
_CfprEtherFcoeInterfaceStatsPacketsTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDelta = _CfprEtherFcoeInterfaceStatsPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 41),
    _CfprEtherFcoeInterfaceStatsPacketsTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg = _CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 42),
    _CfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax = _CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 43),
    _CfprEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin = _CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 44),
    _CfprEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsSuspect_Type = TruthValue
_CfprEtherFcoeInterfaceStatsSuspect_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsSuspect = _CfprEtherFcoeInterfaceStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 45),
    _CfprEtherFcoeInterfaceStatsSuspect_Type()
)
cfprEtherFcoeInterfaceStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsSuspect.setStatus("current")
_CfprEtherFcoeInterfaceStatsThresholded_Type = CfprEtherFcoeInterfaceStatsThresholded
_CfprEtherFcoeInterfaceStatsThresholded_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsThresholded = _CfprEtherFcoeInterfaceStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 46),
    _CfprEtherFcoeInterfaceStatsThresholded_Type()
)
cfprEtherFcoeInterfaceStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsThresholded.setStatus("current")
_CfprEtherFcoeInterfaceStatsTimeCollected_Type = DateAndTime
_CfprEtherFcoeInterfaceStatsTimeCollected_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsTimeCollected = _CfprEtherFcoeInterfaceStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 47),
    _CfprEtherFcoeInterfaceStatsTimeCollected_Type()
)
cfprEtherFcoeInterfaceStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsTimeCollected.setStatus("current")
_CfprEtherFcoeInterfaceStatsUpdate_Type = Gauge32
_CfprEtherFcoeInterfaceStatsUpdate_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsUpdate = _CfprEtherFcoeInterfaceStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 3, 1, 48),
    _CfprEtherFcoeInterfaceStatsUpdate_Type()
)
cfprEtherFcoeInterfaceStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsUpdate.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistTable_Object = MibTable
cfprEtherFcoeInterfaceStatsHistTable = _CfprEtherFcoeInterfaceStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4)
)
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistTable.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistEntry_Object = MibTableRow
cfprEtherFcoeInterfaceStatsHistEntry = _CfprEtherFcoeInterfaceStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1)
)
cfprEtherFcoeInterfaceStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFcoeInterfaceStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistEntry.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherFcoeInterfaceStatsHistInstanceId_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistInstanceId = _CfprEtherFcoeInterfaceStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 1),
    _CfprEtherFcoeInterfaceStatsHistInstanceId_Type()
)
cfprEtherFcoeInterfaceStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistInstanceId.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherFcoeInterfaceStatsHistDn_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDn = _CfprEtherFcoeInterfaceStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 2),
    _CfprEtherFcoeInterfaceStatsHistDn_Type()
)
cfprEtherFcoeInterfaceStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDn.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistRn_Type = SnmpAdminString
_CfprEtherFcoeInterfaceStatsHistRn_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistRn = _CfprEtherFcoeInterfaceStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 3),
    _CfprEtherFcoeInterfaceStatsHistRn_Type()
)
cfprEtherFcoeInterfaceStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistRn.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRx = _CfprEtherFcoeInterfaceStatsHistBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 4),
    _CfprEtherFcoeInterfaceStatsHistBytesRx_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDelta = _CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 5),
    _CfprEtherFcoeInterfaceStatsHistBytesRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 6),
    _CfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax = _CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 7),
    _CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin = _CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 8),
    _CfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTx = _CfprEtherFcoeInterfaceStatsHistBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 9),
    _CfprEtherFcoeInterfaceStatsHistBytesTx_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDelta = _CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 10),
    _CfprEtherFcoeInterfaceStatsHistBytesTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 11),
    _CfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax = _CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 12),
    _CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin = _CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 13),
    _CfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRx = _CfprEtherFcoeInterfaceStatsHistDroppedRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 14),
    _CfprEtherFcoeInterfaceStatsHistDroppedRx_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDelta = _CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 15),
    _CfprEtherFcoeInterfaceStatsHistDroppedRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 16),
    _CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax = _CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 17),
    _CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin = _CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 18),
    _CfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTx = _CfprEtherFcoeInterfaceStatsHistDroppedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 19),
    _CfprEtherFcoeInterfaceStatsHistDroppedTx_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDelta = _CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 20),
    _CfprEtherFcoeInterfaceStatsHistDroppedTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 21),
    _CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax = _CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 22),
    _CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin = _CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 23),
    _CfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRx = _CfprEtherFcoeInterfaceStatsHistErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 24),
    _CfprEtherFcoeInterfaceStatsHistErrorsRx_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDelta = _CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 25),
    _CfprEtherFcoeInterfaceStatsHistErrorsRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 26),
    _CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax = _CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 27),
    _CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin = _CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 28),
    _CfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTx = _CfprEtherFcoeInterfaceStatsHistErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 29),
    _CfprEtherFcoeInterfaceStatsHistErrorsTx_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDelta = _CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 30),
    _CfprEtherFcoeInterfaceStatsHistErrorsTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 31),
    _CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax = _CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 32),
    _CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin = _CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 33),
    _CfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistId_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistId_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistId = _CfprEtherFcoeInterfaceStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 34),
    _CfprEtherFcoeInterfaceStatsHistId_Type()
)
cfprEtherFcoeInterfaceStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistId.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistMostRecent_Type = TruthValue
_CfprEtherFcoeInterfaceStatsHistMostRecent_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistMostRecent = _CfprEtherFcoeInterfaceStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 35),
    _CfprEtherFcoeInterfaceStatsHistMostRecent_Type()
)
cfprEtherFcoeInterfaceStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistMostRecent.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsRx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRx = _CfprEtherFcoeInterfaceStatsHistPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 36),
    _CfprEtherFcoeInterfaceStatsHistPacketsRx_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsRx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDelta = _CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 37),
    _CfprEtherFcoeInterfaceStatsHistPacketsRxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsRxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 38),
    _CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax = _CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 39),
    _CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin = _CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 40),
    _CfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsTx_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTx_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTx = _CfprEtherFcoeInterfaceStatsHistPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 41),
    _CfprEtherFcoeInterfaceStatsHistPacketsTx_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsTx.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDelta = _CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 42),
    _CfprEtherFcoeInterfaceStatsHistPacketsTxDelta_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsTxDelta.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg = _CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 43),
    _CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax = _CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 44),
    _CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type = Unsigned64
_CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin = _CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 45),
    _CfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type()
)
cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistSuspect_Type = TruthValue
_CfprEtherFcoeInterfaceStatsHistSuspect_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistSuspect = _CfprEtherFcoeInterfaceStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 46),
    _CfprEtherFcoeInterfaceStatsHistSuspect_Type()
)
cfprEtherFcoeInterfaceStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistSuspect.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistThresholded_Type = CfprEtherFcoeInterfaceStatsHistThresholded
_CfprEtherFcoeInterfaceStatsHistThresholded_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistThresholded = _CfprEtherFcoeInterfaceStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 47),
    _CfprEtherFcoeInterfaceStatsHistThresholded_Type()
)
cfprEtherFcoeInterfaceStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistThresholded.setStatus("current")
_CfprEtherFcoeInterfaceStatsHistTimeCollected_Type = DateAndTime
_CfprEtherFcoeInterfaceStatsHistTimeCollected_Object = MibTableColumn
cfprEtherFcoeInterfaceStatsHistTimeCollected = _CfprEtherFcoeInterfaceStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 4, 1, 48),
    _CfprEtherFcoeInterfaceStatsHistTimeCollected_Type()
)
cfprEtherFcoeInterfaceStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFcoeInterfaceStatsHistTimeCollected.setStatus("current")
_CfprEtherLossStatsTable_Object = MibTable
cfprEtherLossStatsTable = _CfprEtherLossStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5)
)
if mibBuilder.loadTexts:
    cfprEtherLossStatsTable.setStatus("current")
_CfprEtherLossStatsEntry_Object = MibTableRow
cfprEtherLossStatsEntry = _CfprEtherLossStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1)
)
cfprEtherLossStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherLossStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherLossStatsEntry.setStatus("current")
_CfprEtherLossStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherLossStatsInstanceId_Object = MibTableColumn
cfprEtherLossStatsInstanceId = _CfprEtherLossStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 1),
    _CfprEtherLossStatsInstanceId_Type()
)
cfprEtherLossStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherLossStatsInstanceId.setStatus("current")
_CfprEtherLossStatsDn_Type = CfprManagedObjectDn
_CfprEtherLossStatsDn_Object = MibTableColumn
cfprEtherLossStatsDn = _CfprEtherLossStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 2),
    _CfprEtherLossStatsDn_Type()
)
cfprEtherLossStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsDn.setStatus("current")
_CfprEtherLossStatsRn_Type = SnmpAdminString
_CfprEtherLossStatsRn_Object = MibTableColumn
cfprEtherLossStatsRn = _CfprEtherLossStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 3),
    _CfprEtherLossStatsRn_Type()
)
cfprEtherLossStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsRn.setStatus("current")
_CfprEtherLossStatsSQETest_Type = Unsigned64
_CfprEtherLossStatsSQETest_Object = MibTableColumn
cfprEtherLossStatsSQETest = _CfprEtherLossStatsSQETest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 4),
    _CfprEtherLossStatsSQETest_Type()
)
cfprEtherLossStatsSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSQETest.setStatus("current")
_CfprEtherLossStatsSQETestDelta_Type = Counter64
_CfprEtherLossStatsSQETestDelta_Object = MibTableColumn
cfprEtherLossStatsSQETestDelta = _CfprEtherLossStatsSQETestDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 5),
    _CfprEtherLossStatsSQETestDelta_Type()
)
cfprEtherLossStatsSQETestDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSQETestDelta.setStatus("current")
_CfprEtherLossStatsSQETestDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsSQETestDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsSQETestDeltaAvg = _CfprEtherLossStatsSQETestDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 6),
    _CfprEtherLossStatsSQETestDeltaAvg_Type()
)
cfprEtherLossStatsSQETestDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSQETestDeltaAvg.setStatus("current")
_CfprEtherLossStatsSQETestDeltaMax_Type = Unsigned64
_CfprEtherLossStatsSQETestDeltaMax_Object = MibTableColumn
cfprEtherLossStatsSQETestDeltaMax = _CfprEtherLossStatsSQETestDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 7),
    _CfprEtherLossStatsSQETestDeltaMax_Type()
)
cfprEtherLossStatsSQETestDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSQETestDeltaMax.setStatus("current")
_CfprEtherLossStatsSQETestDeltaMin_Type = Unsigned64
_CfprEtherLossStatsSQETestDeltaMin_Object = MibTableColumn
cfprEtherLossStatsSQETestDeltaMin = _CfprEtherLossStatsSQETestDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 8),
    _CfprEtherLossStatsSQETestDeltaMin_Type()
)
cfprEtherLossStatsSQETestDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSQETestDeltaMin.setStatus("current")
_CfprEtherLossStatsCarrierSense_Type = Unsigned64
_CfprEtherLossStatsCarrierSense_Object = MibTableColumn
cfprEtherLossStatsCarrierSense = _CfprEtherLossStatsCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 9),
    _CfprEtherLossStatsCarrierSense_Type()
)
cfprEtherLossStatsCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsCarrierSense.setStatus("current")
_CfprEtherLossStatsCarrierSenseDelta_Type = Counter64
_CfprEtherLossStatsCarrierSenseDelta_Object = MibTableColumn
cfprEtherLossStatsCarrierSenseDelta = _CfprEtherLossStatsCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 10),
    _CfprEtherLossStatsCarrierSenseDelta_Type()
)
cfprEtherLossStatsCarrierSenseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsCarrierSenseDelta.setStatus("current")
_CfprEtherLossStatsCarrierSenseDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsCarrierSenseDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsCarrierSenseDeltaAvg = _CfprEtherLossStatsCarrierSenseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 11),
    _CfprEtherLossStatsCarrierSenseDeltaAvg_Type()
)
cfprEtherLossStatsCarrierSenseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsCarrierSenseDeltaAvg.setStatus("current")
_CfprEtherLossStatsCarrierSenseDeltaMax_Type = Unsigned64
_CfprEtherLossStatsCarrierSenseDeltaMax_Object = MibTableColumn
cfprEtherLossStatsCarrierSenseDeltaMax = _CfprEtherLossStatsCarrierSenseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 12),
    _CfprEtherLossStatsCarrierSenseDeltaMax_Type()
)
cfprEtherLossStatsCarrierSenseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsCarrierSenseDeltaMax.setStatus("current")
_CfprEtherLossStatsCarrierSenseDeltaMin_Type = Unsigned64
_CfprEtherLossStatsCarrierSenseDeltaMin_Object = MibTableColumn
cfprEtherLossStatsCarrierSenseDeltaMin = _CfprEtherLossStatsCarrierSenseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 13),
    _CfprEtherLossStatsCarrierSenseDeltaMin_Type()
)
cfprEtherLossStatsCarrierSenseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsCarrierSenseDeltaMin.setStatus("current")
_CfprEtherLossStatsExcessCollision_Type = Unsigned64
_CfprEtherLossStatsExcessCollision_Object = MibTableColumn
cfprEtherLossStatsExcessCollision = _CfprEtherLossStatsExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 14),
    _CfprEtherLossStatsExcessCollision_Type()
)
cfprEtherLossStatsExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsExcessCollision.setStatus("current")
_CfprEtherLossStatsExcessCollisionDelta_Type = Counter64
_CfprEtherLossStatsExcessCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsExcessCollisionDelta = _CfprEtherLossStatsExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 15),
    _CfprEtherLossStatsExcessCollisionDelta_Type()
)
cfprEtherLossStatsExcessCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsExcessCollisionDelta.setStatus("current")
_CfprEtherLossStatsExcessCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsExcessCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsExcessCollisionDeltaAvg = _CfprEtherLossStatsExcessCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 16),
    _CfprEtherLossStatsExcessCollisionDeltaAvg_Type()
)
cfprEtherLossStatsExcessCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsExcessCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsExcessCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsExcessCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsExcessCollisionDeltaMax = _CfprEtherLossStatsExcessCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 17),
    _CfprEtherLossStatsExcessCollisionDeltaMax_Type()
)
cfprEtherLossStatsExcessCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsExcessCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsExcessCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsExcessCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsExcessCollisionDeltaMin = _CfprEtherLossStatsExcessCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 18),
    _CfprEtherLossStatsExcessCollisionDeltaMin_Type()
)
cfprEtherLossStatsExcessCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsExcessCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsGiants_Type = Unsigned64
_CfprEtherLossStatsGiants_Object = MibTableColumn
cfprEtherLossStatsGiants = _CfprEtherLossStatsGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 19),
    _CfprEtherLossStatsGiants_Type()
)
cfprEtherLossStatsGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsGiants.setStatus("current")
_CfprEtherLossStatsGiantsDelta_Type = Counter64
_CfprEtherLossStatsGiantsDelta_Object = MibTableColumn
cfprEtherLossStatsGiantsDelta = _CfprEtherLossStatsGiantsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 20),
    _CfprEtherLossStatsGiantsDelta_Type()
)
cfprEtherLossStatsGiantsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsGiantsDelta.setStatus("current")
_CfprEtherLossStatsGiantsDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsGiantsDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsGiantsDeltaAvg = _CfprEtherLossStatsGiantsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 21),
    _CfprEtherLossStatsGiantsDeltaAvg_Type()
)
cfprEtherLossStatsGiantsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsGiantsDeltaAvg.setStatus("current")
_CfprEtherLossStatsGiantsDeltaMax_Type = Unsigned64
_CfprEtherLossStatsGiantsDeltaMax_Object = MibTableColumn
cfprEtherLossStatsGiantsDeltaMax = _CfprEtherLossStatsGiantsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 22),
    _CfprEtherLossStatsGiantsDeltaMax_Type()
)
cfprEtherLossStatsGiantsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsGiantsDeltaMax.setStatus("current")
_CfprEtherLossStatsGiantsDeltaMin_Type = Unsigned64
_CfprEtherLossStatsGiantsDeltaMin_Object = MibTableColumn
cfprEtherLossStatsGiantsDeltaMin = _CfprEtherLossStatsGiantsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 23),
    _CfprEtherLossStatsGiantsDeltaMin_Type()
)
cfprEtherLossStatsGiantsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsGiantsDeltaMin.setStatus("current")
_CfprEtherLossStatsIntervals_Type = Gauge32
_CfprEtherLossStatsIntervals_Object = MibTableColumn
cfprEtherLossStatsIntervals = _CfprEtherLossStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 24),
    _CfprEtherLossStatsIntervals_Type()
)
cfprEtherLossStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsIntervals.setStatus("current")
_CfprEtherLossStatsLateCollision_Type = Unsigned64
_CfprEtherLossStatsLateCollision_Object = MibTableColumn
cfprEtherLossStatsLateCollision = _CfprEtherLossStatsLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 25),
    _CfprEtherLossStatsLateCollision_Type()
)
cfprEtherLossStatsLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsLateCollision.setStatus("current")
_CfprEtherLossStatsLateCollisionDelta_Type = Counter64
_CfprEtherLossStatsLateCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsLateCollisionDelta = _CfprEtherLossStatsLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 26),
    _CfprEtherLossStatsLateCollisionDelta_Type()
)
cfprEtherLossStatsLateCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsLateCollisionDelta.setStatus("current")
_CfprEtherLossStatsLateCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsLateCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsLateCollisionDeltaAvg = _CfprEtherLossStatsLateCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 27),
    _CfprEtherLossStatsLateCollisionDeltaAvg_Type()
)
cfprEtherLossStatsLateCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsLateCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsLateCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsLateCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsLateCollisionDeltaMax = _CfprEtherLossStatsLateCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 28),
    _CfprEtherLossStatsLateCollisionDeltaMax_Type()
)
cfprEtherLossStatsLateCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsLateCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsLateCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsLateCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsLateCollisionDeltaMin = _CfprEtherLossStatsLateCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 29),
    _CfprEtherLossStatsLateCollisionDeltaMin_Type()
)
cfprEtherLossStatsLateCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsLateCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsMultiCollision_Type = Unsigned64
_CfprEtherLossStatsMultiCollision_Object = MibTableColumn
cfprEtherLossStatsMultiCollision = _CfprEtherLossStatsMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 30),
    _CfprEtherLossStatsMultiCollision_Type()
)
cfprEtherLossStatsMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsMultiCollision.setStatus("current")
_CfprEtherLossStatsMultiCollisionDelta_Type = Counter64
_CfprEtherLossStatsMultiCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsMultiCollisionDelta = _CfprEtherLossStatsMultiCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 31),
    _CfprEtherLossStatsMultiCollisionDelta_Type()
)
cfprEtherLossStatsMultiCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsMultiCollisionDelta.setStatus("current")
_CfprEtherLossStatsMultiCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsMultiCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsMultiCollisionDeltaAvg = _CfprEtherLossStatsMultiCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 32),
    _CfprEtherLossStatsMultiCollisionDeltaAvg_Type()
)
cfprEtherLossStatsMultiCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsMultiCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsMultiCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsMultiCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsMultiCollisionDeltaMax = _CfprEtherLossStatsMultiCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 33),
    _CfprEtherLossStatsMultiCollisionDeltaMax_Type()
)
cfprEtherLossStatsMultiCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsMultiCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsMultiCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsMultiCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsMultiCollisionDeltaMin = _CfprEtherLossStatsMultiCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 34),
    _CfprEtherLossStatsMultiCollisionDeltaMin_Type()
)
cfprEtherLossStatsMultiCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsMultiCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsSingleCollision_Type = Unsigned64
_CfprEtherLossStatsSingleCollision_Object = MibTableColumn
cfprEtherLossStatsSingleCollision = _CfprEtherLossStatsSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 35),
    _CfprEtherLossStatsSingleCollision_Type()
)
cfprEtherLossStatsSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSingleCollision.setStatus("current")
_CfprEtherLossStatsSingleCollisionDelta_Type = Counter64
_CfprEtherLossStatsSingleCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsSingleCollisionDelta = _CfprEtherLossStatsSingleCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 36),
    _CfprEtherLossStatsSingleCollisionDelta_Type()
)
cfprEtherLossStatsSingleCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSingleCollisionDelta.setStatus("current")
_CfprEtherLossStatsSingleCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsSingleCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsSingleCollisionDeltaAvg = _CfprEtherLossStatsSingleCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 37),
    _CfprEtherLossStatsSingleCollisionDeltaAvg_Type()
)
cfprEtherLossStatsSingleCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSingleCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsSingleCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsSingleCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsSingleCollisionDeltaMax = _CfprEtherLossStatsSingleCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 38),
    _CfprEtherLossStatsSingleCollisionDeltaMax_Type()
)
cfprEtherLossStatsSingleCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSingleCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsSingleCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsSingleCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsSingleCollisionDeltaMin = _CfprEtherLossStatsSingleCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 39),
    _CfprEtherLossStatsSingleCollisionDeltaMin_Type()
)
cfprEtherLossStatsSingleCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSingleCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsSuspect_Type = TruthValue
_CfprEtherLossStatsSuspect_Object = MibTableColumn
cfprEtherLossStatsSuspect = _CfprEtherLossStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 40),
    _CfprEtherLossStatsSuspect_Type()
)
cfprEtherLossStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSuspect.setStatus("current")
_CfprEtherLossStatsSymbol_Type = Unsigned64
_CfprEtherLossStatsSymbol_Object = MibTableColumn
cfprEtherLossStatsSymbol = _CfprEtherLossStatsSymbol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 41),
    _CfprEtherLossStatsSymbol_Type()
)
cfprEtherLossStatsSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSymbol.setStatus("current")
_CfprEtherLossStatsSymbolDelta_Type = Counter64
_CfprEtherLossStatsSymbolDelta_Object = MibTableColumn
cfprEtherLossStatsSymbolDelta = _CfprEtherLossStatsSymbolDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 42),
    _CfprEtherLossStatsSymbolDelta_Type()
)
cfprEtherLossStatsSymbolDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSymbolDelta.setStatus("current")
_CfprEtherLossStatsSymbolDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsSymbolDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsSymbolDeltaAvg = _CfprEtherLossStatsSymbolDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 43),
    _CfprEtherLossStatsSymbolDeltaAvg_Type()
)
cfprEtherLossStatsSymbolDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSymbolDeltaAvg.setStatus("current")
_CfprEtherLossStatsSymbolDeltaMax_Type = Unsigned64
_CfprEtherLossStatsSymbolDeltaMax_Object = MibTableColumn
cfprEtherLossStatsSymbolDeltaMax = _CfprEtherLossStatsSymbolDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 44),
    _CfprEtherLossStatsSymbolDeltaMax_Type()
)
cfprEtherLossStatsSymbolDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSymbolDeltaMax.setStatus("current")
_CfprEtherLossStatsSymbolDeltaMin_Type = Unsigned64
_CfprEtherLossStatsSymbolDeltaMin_Object = MibTableColumn
cfprEtherLossStatsSymbolDeltaMin = _CfprEtherLossStatsSymbolDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 45),
    _CfprEtherLossStatsSymbolDeltaMin_Type()
)
cfprEtherLossStatsSymbolDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsSymbolDeltaMin.setStatus("current")
_CfprEtherLossStatsThresholded_Type = CfprEtherLossStatsThresholded
_CfprEtherLossStatsThresholded_Object = MibTableColumn
cfprEtherLossStatsThresholded = _CfprEtherLossStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 46),
    _CfprEtherLossStatsThresholded_Type()
)
cfprEtherLossStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsThresholded.setStatus("current")
_CfprEtherLossStatsTimeCollected_Type = DateAndTime
_CfprEtherLossStatsTimeCollected_Object = MibTableColumn
cfprEtherLossStatsTimeCollected = _CfprEtherLossStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 47),
    _CfprEtherLossStatsTimeCollected_Type()
)
cfprEtherLossStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsTimeCollected.setStatus("current")
_CfprEtherLossStatsUpdate_Type = Gauge32
_CfprEtherLossStatsUpdate_Object = MibTableColumn
cfprEtherLossStatsUpdate = _CfprEtherLossStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 5, 1, 48),
    _CfprEtherLossStatsUpdate_Type()
)
cfprEtherLossStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsUpdate.setStatus("current")
_CfprEtherLossStatsHistTable_Object = MibTable
cfprEtherLossStatsHistTable = _CfprEtherLossStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6)
)
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistTable.setStatus("current")
_CfprEtherLossStatsHistEntry_Object = MibTableRow
cfprEtherLossStatsHistEntry = _CfprEtherLossStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1)
)
cfprEtherLossStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherLossStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistEntry.setStatus("current")
_CfprEtherLossStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherLossStatsHistInstanceId_Object = MibTableColumn
cfprEtherLossStatsHistInstanceId = _CfprEtherLossStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 1),
    _CfprEtherLossStatsHistInstanceId_Type()
)
cfprEtherLossStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistInstanceId.setStatus("current")
_CfprEtherLossStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherLossStatsHistDn_Object = MibTableColumn
cfprEtherLossStatsHistDn = _CfprEtherLossStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 2),
    _CfprEtherLossStatsHistDn_Type()
)
cfprEtherLossStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistDn.setStatus("current")
_CfprEtherLossStatsHistRn_Type = SnmpAdminString
_CfprEtherLossStatsHistRn_Object = MibTableColumn
cfprEtherLossStatsHistRn = _CfprEtherLossStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 3),
    _CfprEtherLossStatsHistRn_Type()
)
cfprEtherLossStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistRn.setStatus("current")
_CfprEtherLossStatsHistSQETest_Type = Unsigned64
_CfprEtherLossStatsHistSQETest_Object = MibTableColumn
cfprEtherLossStatsHistSQETest = _CfprEtherLossStatsHistSQETest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 4),
    _CfprEtherLossStatsHistSQETest_Type()
)
cfprEtherLossStatsHistSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSQETest.setStatus("current")
_CfprEtherLossStatsHistSQETestDelta_Type = Unsigned64
_CfprEtherLossStatsHistSQETestDelta_Object = MibTableColumn
cfprEtherLossStatsHistSQETestDelta = _CfprEtherLossStatsHistSQETestDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 5),
    _CfprEtherLossStatsHistSQETestDelta_Type()
)
cfprEtherLossStatsHistSQETestDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSQETestDelta.setStatus("current")
_CfprEtherLossStatsHistSQETestDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistSQETestDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistSQETestDeltaAvg = _CfprEtherLossStatsHistSQETestDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 6),
    _CfprEtherLossStatsHistSQETestDeltaAvg_Type()
)
cfprEtherLossStatsHistSQETestDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSQETestDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistSQETestDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistSQETestDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistSQETestDeltaMax = _CfprEtherLossStatsHistSQETestDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 7),
    _CfprEtherLossStatsHistSQETestDeltaMax_Type()
)
cfprEtherLossStatsHistSQETestDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSQETestDeltaMax.setStatus("current")
_CfprEtherLossStatsHistSQETestDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistSQETestDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistSQETestDeltaMin = _CfprEtherLossStatsHistSQETestDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 8),
    _CfprEtherLossStatsHistSQETestDeltaMin_Type()
)
cfprEtherLossStatsHistSQETestDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSQETestDeltaMin.setStatus("current")
_CfprEtherLossStatsHistCarrierSense_Type = Unsigned64
_CfprEtherLossStatsHistCarrierSense_Object = MibTableColumn
cfprEtherLossStatsHistCarrierSense = _CfprEtherLossStatsHistCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 9),
    _CfprEtherLossStatsHistCarrierSense_Type()
)
cfprEtherLossStatsHistCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistCarrierSense.setStatus("current")
_CfprEtherLossStatsHistCarrierSenseDelta_Type = Unsigned64
_CfprEtherLossStatsHistCarrierSenseDelta_Object = MibTableColumn
cfprEtherLossStatsHistCarrierSenseDelta = _CfprEtherLossStatsHistCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 10),
    _CfprEtherLossStatsHistCarrierSenseDelta_Type()
)
cfprEtherLossStatsHistCarrierSenseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistCarrierSenseDelta.setStatus("current")
_CfprEtherLossStatsHistCarrierSenseDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistCarrierSenseDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistCarrierSenseDeltaAvg = _CfprEtherLossStatsHistCarrierSenseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 11),
    _CfprEtherLossStatsHistCarrierSenseDeltaAvg_Type()
)
cfprEtherLossStatsHistCarrierSenseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistCarrierSenseDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistCarrierSenseDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistCarrierSenseDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistCarrierSenseDeltaMax = _CfprEtherLossStatsHistCarrierSenseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 12),
    _CfprEtherLossStatsHistCarrierSenseDeltaMax_Type()
)
cfprEtherLossStatsHistCarrierSenseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistCarrierSenseDeltaMax.setStatus("current")
_CfprEtherLossStatsHistCarrierSenseDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistCarrierSenseDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistCarrierSenseDeltaMin = _CfprEtherLossStatsHistCarrierSenseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 13),
    _CfprEtherLossStatsHistCarrierSenseDeltaMin_Type()
)
cfprEtherLossStatsHistCarrierSenseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistCarrierSenseDeltaMin.setStatus("current")
_CfprEtherLossStatsHistExcessCollision_Type = Unsigned64
_CfprEtherLossStatsHistExcessCollision_Object = MibTableColumn
cfprEtherLossStatsHistExcessCollision = _CfprEtherLossStatsHistExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 14),
    _CfprEtherLossStatsHistExcessCollision_Type()
)
cfprEtherLossStatsHistExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistExcessCollision.setStatus("current")
_CfprEtherLossStatsHistExcessCollisionDelta_Type = Unsigned64
_CfprEtherLossStatsHistExcessCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsHistExcessCollisionDelta = _CfprEtherLossStatsHistExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 15),
    _CfprEtherLossStatsHistExcessCollisionDelta_Type()
)
cfprEtherLossStatsHistExcessCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistExcessCollisionDelta.setStatus("current")
_CfprEtherLossStatsHistExcessCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistExcessCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistExcessCollisionDeltaAvg = _CfprEtherLossStatsHistExcessCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 16),
    _CfprEtherLossStatsHistExcessCollisionDeltaAvg_Type()
)
cfprEtherLossStatsHistExcessCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistExcessCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistExcessCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistExcessCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistExcessCollisionDeltaMax = _CfprEtherLossStatsHistExcessCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 17),
    _CfprEtherLossStatsHistExcessCollisionDeltaMax_Type()
)
cfprEtherLossStatsHistExcessCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistExcessCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsHistExcessCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistExcessCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistExcessCollisionDeltaMin = _CfprEtherLossStatsHistExcessCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 18),
    _CfprEtherLossStatsHistExcessCollisionDeltaMin_Type()
)
cfprEtherLossStatsHistExcessCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistExcessCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsHistGiants_Type = Unsigned64
_CfprEtherLossStatsHistGiants_Object = MibTableColumn
cfprEtherLossStatsHistGiants = _CfprEtherLossStatsHistGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 19),
    _CfprEtherLossStatsHistGiants_Type()
)
cfprEtherLossStatsHistGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistGiants.setStatus("current")
_CfprEtherLossStatsHistGiantsDelta_Type = Unsigned64
_CfprEtherLossStatsHistGiantsDelta_Object = MibTableColumn
cfprEtherLossStatsHistGiantsDelta = _CfprEtherLossStatsHistGiantsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 20),
    _CfprEtherLossStatsHistGiantsDelta_Type()
)
cfprEtherLossStatsHistGiantsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistGiantsDelta.setStatus("current")
_CfprEtherLossStatsHistGiantsDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistGiantsDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistGiantsDeltaAvg = _CfprEtherLossStatsHistGiantsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 21),
    _CfprEtherLossStatsHistGiantsDeltaAvg_Type()
)
cfprEtherLossStatsHistGiantsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistGiantsDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistGiantsDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistGiantsDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistGiantsDeltaMax = _CfprEtherLossStatsHistGiantsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 22),
    _CfprEtherLossStatsHistGiantsDeltaMax_Type()
)
cfprEtherLossStatsHistGiantsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistGiantsDeltaMax.setStatus("current")
_CfprEtherLossStatsHistGiantsDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistGiantsDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistGiantsDeltaMin = _CfprEtherLossStatsHistGiantsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 23),
    _CfprEtherLossStatsHistGiantsDeltaMin_Type()
)
cfprEtherLossStatsHistGiantsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistGiantsDeltaMin.setStatus("current")
_CfprEtherLossStatsHistId_Type = Unsigned64
_CfprEtherLossStatsHistId_Object = MibTableColumn
cfprEtherLossStatsHistId = _CfprEtherLossStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 24),
    _CfprEtherLossStatsHistId_Type()
)
cfprEtherLossStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistId.setStatus("current")
_CfprEtherLossStatsHistLateCollision_Type = Unsigned64
_CfprEtherLossStatsHistLateCollision_Object = MibTableColumn
cfprEtherLossStatsHistLateCollision = _CfprEtherLossStatsHistLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 25),
    _CfprEtherLossStatsHistLateCollision_Type()
)
cfprEtherLossStatsHistLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistLateCollision.setStatus("current")
_CfprEtherLossStatsHistLateCollisionDelta_Type = Unsigned64
_CfprEtherLossStatsHistLateCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsHistLateCollisionDelta = _CfprEtherLossStatsHistLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 26),
    _CfprEtherLossStatsHistLateCollisionDelta_Type()
)
cfprEtherLossStatsHistLateCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistLateCollisionDelta.setStatus("current")
_CfprEtherLossStatsHistLateCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistLateCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistLateCollisionDeltaAvg = _CfprEtherLossStatsHistLateCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 27),
    _CfprEtherLossStatsHistLateCollisionDeltaAvg_Type()
)
cfprEtherLossStatsHistLateCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistLateCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistLateCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistLateCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistLateCollisionDeltaMax = _CfprEtherLossStatsHistLateCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 28),
    _CfprEtherLossStatsHistLateCollisionDeltaMax_Type()
)
cfprEtherLossStatsHistLateCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistLateCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsHistLateCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistLateCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistLateCollisionDeltaMin = _CfprEtherLossStatsHistLateCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 29),
    _CfprEtherLossStatsHistLateCollisionDeltaMin_Type()
)
cfprEtherLossStatsHistLateCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistLateCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsHistMostRecent_Type = TruthValue
_CfprEtherLossStatsHistMostRecent_Object = MibTableColumn
cfprEtherLossStatsHistMostRecent = _CfprEtherLossStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 30),
    _CfprEtherLossStatsHistMostRecent_Type()
)
cfprEtherLossStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistMostRecent.setStatus("current")
_CfprEtherLossStatsHistMultiCollision_Type = Unsigned64
_CfprEtherLossStatsHistMultiCollision_Object = MibTableColumn
cfprEtherLossStatsHistMultiCollision = _CfprEtherLossStatsHistMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 31),
    _CfprEtherLossStatsHistMultiCollision_Type()
)
cfprEtherLossStatsHistMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistMultiCollision.setStatus("current")
_CfprEtherLossStatsHistMultiCollisionDelta_Type = Unsigned64
_CfprEtherLossStatsHistMultiCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsHistMultiCollisionDelta = _CfprEtherLossStatsHistMultiCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 32),
    _CfprEtherLossStatsHistMultiCollisionDelta_Type()
)
cfprEtherLossStatsHistMultiCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistMultiCollisionDelta.setStatus("current")
_CfprEtherLossStatsHistMultiCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistMultiCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistMultiCollisionDeltaAvg = _CfprEtherLossStatsHistMultiCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 33),
    _CfprEtherLossStatsHistMultiCollisionDeltaAvg_Type()
)
cfprEtherLossStatsHistMultiCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistMultiCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistMultiCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistMultiCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistMultiCollisionDeltaMax = _CfprEtherLossStatsHistMultiCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 34),
    _CfprEtherLossStatsHistMultiCollisionDeltaMax_Type()
)
cfprEtherLossStatsHistMultiCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistMultiCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsHistMultiCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistMultiCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistMultiCollisionDeltaMin = _CfprEtherLossStatsHistMultiCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 35),
    _CfprEtherLossStatsHistMultiCollisionDeltaMin_Type()
)
cfprEtherLossStatsHistMultiCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistMultiCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsHistSingleCollision_Type = Unsigned64
_CfprEtherLossStatsHistSingleCollision_Object = MibTableColumn
cfprEtherLossStatsHistSingleCollision = _CfprEtherLossStatsHistSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 36),
    _CfprEtherLossStatsHistSingleCollision_Type()
)
cfprEtherLossStatsHistSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSingleCollision.setStatus("current")
_CfprEtherLossStatsHistSingleCollisionDelta_Type = Unsigned64
_CfprEtherLossStatsHistSingleCollisionDelta_Object = MibTableColumn
cfprEtherLossStatsHistSingleCollisionDelta = _CfprEtherLossStatsHistSingleCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 37),
    _CfprEtherLossStatsHistSingleCollisionDelta_Type()
)
cfprEtherLossStatsHistSingleCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSingleCollisionDelta.setStatus("current")
_CfprEtherLossStatsHistSingleCollisionDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistSingleCollisionDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistSingleCollisionDeltaAvg = _CfprEtherLossStatsHistSingleCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 38),
    _CfprEtherLossStatsHistSingleCollisionDeltaAvg_Type()
)
cfprEtherLossStatsHistSingleCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSingleCollisionDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistSingleCollisionDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistSingleCollisionDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistSingleCollisionDeltaMax = _CfprEtherLossStatsHistSingleCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 39),
    _CfprEtherLossStatsHistSingleCollisionDeltaMax_Type()
)
cfprEtherLossStatsHistSingleCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSingleCollisionDeltaMax.setStatus("current")
_CfprEtherLossStatsHistSingleCollisionDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistSingleCollisionDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistSingleCollisionDeltaMin = _CfprEtherLossStatsHistSingleCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 40),
    _CfprEtherLossStatsHistSingleCollisionDeltaMin_Type()
)
cfprEtherLossStatsHistSingleCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSingleCollisionDeltaMin.setStatus("current")
_CfprEtherLossStatsHistSuspect_Type = TruthValue
_CfprEtherLossStatsHistSuspect_Object = MibTableColumn
cfprEtherLossStatsHistSuspect = _CfprEtherLossStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 41),
    _CfprEtherLossStatsHistSuspect_Type()
)
cfprEtherLossStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSuspect.setStatus("current")
_CfprEtherLossStatsHistSymbol_Type = Unsigned64
_CfprEtherLossStatsHistSymbol_Object = MibTableColumn
cfprEtherLossStatsHistSymbol = _CfprEtherLossStatsHistSymbol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 42),
    _CfprEtherLossStatsHistSymbol_Type()
)
cfprEtherLossStatsHistSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSymbol.setStatus("current")
_CfprEtherLossStatsHistSymbolDelta_Type = Unsigned64
_CfprEtherLossStatsHistSymbolDelta_Object = MibTableColumn
cfprEtherLossStatsHistSymbolDelta = _CfprEtherLossStatsHistSymbolDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 43),
    _CfprEtherLossStatsHistSymbolDelta_Type()
)
cfprEtherLossStatsHistSymbolDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSymbolDelta.setStatus("current")
_CfprEtherLossStatsHistSymbolDeltaAvg_Type = Unsigned64
_CfprEtherLossStatsHistSymbolDeltaAvg_Object = MibTableColumn
cfprEtherLossStatsHistSymbolDeltaAvg = _CfprEtherLossStatsHistSymbolDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 44),
    _CfprEtherLossStatsHistSymbolDeltaAvg_Type()
)
cfprEtherLossStatsHistSymbolDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSymbolDeltaAvg.setStatus("current")
_CfprEtherLossStatsHistSymbolDeltaMax_Type = Unsigned64
_CfprEtherLossStatsHistSymbolDeltaMax_Object = MibTableColumn
cfprEtherLossStatsHistSymbolDeltaMax = _CfprEtherLossStatsHistSymbolDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 45),
    _CfprEtherLossStatsHistSymbolDeltaMax_Type()
)
cfprEtherLossStatsHistSymbolDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSymbolDeltaMax.setStatus("current")
_CfprEtherLossStatsHistSymbolDeltaMin_Type = Unsigned64
_CfprEtherLossStatsHistSymbolDeltaMin_Object = MibTableColumn
cfprEtherLossStatsHistSymbolDeltaMin = _CfprEtherLossStatsHistSymbolDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 46),
    _CfprEtherLossStatsHistSymbolDeltaMin_Type()
)
cfprEtherLossStatsHistSymbolDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistSymbolDeltaMin.setStatus("current")
_CfprEtherLossStatsHistThresholded_Type = CfprEtherLossStatsHistThresholded
_CfprEtherLossStatsHistThresholded_Object = MibTableColumn
cfprEtherLossStatsHistThresholded = _CfprEtherLossStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 47),
    _CfprEtherLossStatsHistThresholded_Type()
)
cfprEtherLossStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistThresholded.setStatus("current")
_CfprEtherLossStatsHistTimeCollected_Type = DateAndTime
_CfprEtherLossStatsHistTimeCollected_Object = MibTableColumn
cfprEtherLossStatsHistTimeCollected = _CfprEtherLossStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 6, 1, 48),
    _CfprEtherLossStatsHistTimeCollected_Type()
)
cfprEtherLossStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherLossStatsHistTimeCollected.setStatus("current")
_CfprEtherNiErrStatsTable_Object = MibTable
cfprEtherNiErrStatsTable = _CfprEtherNiErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7)
)
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTable.setStatus("current")
_CfprEtherNiErrStatsEntry_Object = MibTableRow
cfprEtherNiErrStatsEntry = _CfprEtherNiErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1)
)
cfprEtherNiErrStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherNiErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsEntry.setStatus("current")
_CfprEtherNiErrStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherNiErrStatsInstanceId_Object = MibTableColumn
cfprEtherNiErrStatsInstanceId = _CfprEtherNiErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 1),
    _CfprEtherNiErrStatsInstanceId_Type()
)
cfprEtherNiErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsInstanceId.setStatus("current")
_CfprEtherNiErrStatsDn_Type = CfprManagedObjectDn
_CfprEtherNiErrStatsDn_Object = MibTableColumn
cfprEtherNiErrStatsDn = _CfprEtherNiErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 2),
    _CfprEtherNiErrStatsDn_Type()
)
cfprEtherNiErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsDn.setStatus("current")
_CfprEtherNiErrStatsRn_Type = SnmpAdminString
_CfprEtherNiErrStatsRn_Object = MibTableColumn
cfprEtherNiErrStatsRn = _CfprEtherNiErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 3),
    _CfprEtherNiErrStatsRn_Type()
)
cfprEtherNiErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsRn.setStatus("current")
_CfprEtherNiErrStatsCrc_Type = Unsigned64
_CfprEtherNiErrStatsCrc_Object = MibTableColumn
cfprEtherNiErrStatsCrc = _CfprEtherNiErrStatsCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 4),
    _CfprEtherNiErrStatsCrc_Type()
)
cfprEtherNiErrStatsCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsCrc.setStatus("current")
_CfprEtherNiErrStatsCrcDelta_Type = Counter64
_CfprEtherNiErrStatsCrcDelta_Object = MibTableColumn
cfprEtherNiErrStatsCrcDelta = _CfprEtherNiErrStatsCrcDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 5),
    _CfprEtherNiErrStatsCrcDelta_Type()
)
cfprEtherNiErrStatsCrcDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsCrcDelta.setStatus("current")
_CfprEtherNiErrStatsCrcDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsCrcDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsCrcDeltaAvg = _CfprEtherNiErrStatsCrcDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 6),
    _CfprEtherNiErrStatsCrcDeltaAvg_Type()
)
cfprEtherNiErrStatsCrcDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsCrcDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsCrcDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsCrcDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsCrcDeltaMax = _CfprEtherNiErrStatsCrcDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 7),
    _CfprEtherNiErrStatsCrcDeltaMax_Type()
)
cfprEtherNiErrStatsCrcDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsCrcDeltaMax.setStatus("current")
_CfprEtherNiErrStatsCrcDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsCrcDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsCrcDeltaMin = _CfprEtherNiErrStatsCrcDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 8),
    _CfprEtherNiErrStatsCrcDeltaMin_Type()
)
cfprEtherNiErrStatsCrcDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsCrcDeltaMin.setStatus("current")
_CfprEtherNiErrStatsFrameTx_Type = Unsigned64
_CfprEtherNiErrStatsFrameTx_Object = MibTableColumn
cfprEtherNiErrStatsFrameTx = _CfprEtherNiErrStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 9),
    _CfprEtherNiErrStatsFrameTx_Type()
)
cfprEtherNiErrStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsFrameTx.setStatus("current")
_CfprEtherNiErrStatsFrameTxDelta_Type = Counter64
_CfprEtherNiErrStatsFrameTxDelta_Object = MibTableColumn
cfprEtherNiErrStatsFrameTxDelta = _CfprEtherNiErrStatsFrameTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 10),
    _CfprEtherNiErrStatsFrameTxDelta_Type()
)
cfprEtherNiErrStatsFrameTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsFrameTxDelta.setStatus("current")
_CfprEtherNiErrStatsFrameTxDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsFrameTxDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsFrameTxDeltaAvg = _CfprEtherNiErrStatsFrameTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 11),
    _CfprEtherNiErrStatsFrameTxDeltaAvg_Type()
)
cfprEtherNiErrStatsFrameTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsFrameTxDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsFrameTxDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsFrameTxDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsFrameTxDeltaMax = _CfprEtherNiErrStatsFrameTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 12),
    _CfprEtherNiErrStatsFrameTxDeltaMax_Type()
)
cfprEtherNiErrStatsFrameTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsFrameTxDeltaMax.setStatus("current")
_CfprEtherNiErrStatsFrameTxDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsFrameTxDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsFrameTxDeltaMin = _CfprEtherNiErrStatsFrameTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 13),
    _CfprEtherNiErrStatsFrameTxDeltaMin_Type()
)
cfprEtherNiErrStatsFrameTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsFrameTxDeltaMin.setStatus("current")
_CfprEtherNiErrStatsInRange_Type = Unsigned64
_CfprEtherNiErrStatsInRange_Object = MibTableColumn
cfprEtherNiErrStatsInRange = _CfprEtherNiErrStatsInRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 14),
    _CfprEtherNiErrStatsInRange_Type()
)
cfprEtherNiErrStatsInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsInRange.setStatus("current")
_CfprEtherNiErrStatsInRangeDelta_Type = Counter64
_CfprEtherNiErrStatsInRangeDelta_Object = MibTableColumn
cfprEtherNiErrStatsInRangeDelta = _CfprEtherNiErrStatsInRangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 15),
    _CfprEtherNiErrStatsInRangeDelta_Type()
)
cfprEtherNiErrStatsInRangeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsInRangeDelta.setStatus("current")
_CfprEtherNiErrStatsInRangeDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsInRangeDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsInRangeDeltaAvg = _CfprEtherNiErrStatsInRangeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 16),
    _CfprEtherNiErrStatsInRangeDeltaAvg_Type()
)
cfprEtherNiErrStatsInRangeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsInRangeDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsInRangeDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsInRangeDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsInRangeDeltaMax = _CfprEtherNiErrStatsInRangeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 17),
    _CfprEtherNiErrStatsInRangeDeltaMax_Type()
)
cfprEtherNiErrStatsInRangeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsInRangeDeltaMax.setStatus("current")
_CfprEtherNiErrStatsInRangeDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsInRangeDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsInRangeDeltaMin = _CfprEtherNiErrStatsInRangeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 18),
    _CfprEtherNiErrStatsInRangeDeltaMin_Type()
)
cfprEtherNiErrStatsInRangeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsInRangeDeltaMin.setStatus("current")
_CfprEtherNiErrStatsIntervals_Type = Gauge32
_CfprEtherNiErrStatsIntervals_Object = MibTableColumn
cfprEtherNiErrStatsIntervals = _CfprEtherNiErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 19),
    _CfprEtherNiErrStatsIntervals_Type()
)
cfprEtherNiErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsIntervals.setStatus("current")
_CfprEtherNiErrStatsSuspect_Type = TruthValue
_CfprEtherNiErrStatsSuspect_Object = MibTableColumn
cfprEtherNiErrStatsSuspect = _CfprEtherNiErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 20),
    _CfprEtherNiErrStatsSuspect_Type()
)
cfprEtherNiErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsSuspect.setStatus("current")
_CfprEtherNiErrStatsThresholded_Type = CfprEtherNiErrStatsThresholded
_CfprEtherNiErrStatsThresholded_Object = MibTableColumn
cfprEtherNiErrStatsThresholded = _CfprEtherNiErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 21),
    _CfprEtherNiErrStatsThresholded_Type()
)
cfprEtherNiErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsThresholded.setStatus("current")
_CfprEtherNiErrStatsTimeCollected_Type = DateAndTime
_CfprEtherNiErrStatsTimeCollected_Object = MibTableColumn
cfprEtherNiErrStatsTimeCollected = _CfprEtherNiErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 22),
    _CfprEtherNiErrStatsTimeCollected_Type()
)
cfprEtherNiErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTimeCollected.setStatus("current")
_CfprEtherNiErrStatsTooLong_Type = Unsigned64
_CfprEtherNiErrStatsTooLong_Object = MibTableColumn
cfprEtherNiErrStatsTooLong = _CfprEtherNiErrStatsTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 23),
    _CfprEtherNiErrStatsTooLong_Type()
)
cfprEtherNiErrStatsTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooLong.setStatus("current")
_CfprEtherNiErrStatsTooLongDelta_Type = Counter64
_CfprEtherNiErrStatsTooLongDelta_Object = MibTableColumn
cfprEtherNiErrStatsTooLongDelta = _CfprEtherNiErrStatsTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 24),
    _CfprEtherNiErrStatsTooLongDelta_Type()
)
cfprEtherNiErrStatsTooLongDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooLongDelta.setStatus("current")
_CfprEtherNiErrStatsTooLongDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsTooLongDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsTooLongDeltaAvg = _CfprEtherNiErrStatsTooLongDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 25),
    _CfprEtherNiErrStatsTooLongDeltaAvg_Type()
)
cfprEtherNiErrStatsTooLongDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooLongDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsTooLongDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsTooLongDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsTooLongDeltaMax = _CfprEtherNiErrStatsTooLongDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 26),
    _CfprEtherNiErrStatsTooLongDeltaMax_Type()
)
cfprEtherNiErrStatsTooLongDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooLongDeltaMax.setStatus("current")
_CfprEtherNiErrStatsTooLongDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsTooLongDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsTooLongDeltaMin = _CfprEtherNiErrStatsTooLongDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 27),
    _CfprEtherNiErrStatsTooLongDeltaMin_Type()
)
cfprEtherNiErrStatsTooLongDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooLongDeltaMin.setStatus("current")
_CfprEtherNiErrStatsTooShort_Type = Unsigned64
_CfprEtherNiErrStatsTooShort_Object = MibTableColumn
cfprEtherNiErrStatsTooShort = _CfprEtherNiErrStatsTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 28),
    _CfprEtherNiErrStatsTooShort_Type()
)
cfprEtherNiErrStatsTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooShort.setStatus("current")
_CfprEtherNiErrStatsTooShortDelta_Type = Counter64
_CfprEtherNiErrStatsTooShortDelta_Object = MibTableColumn
cfprEtherNiErrStatsTooShortDelta = _CfprEtherNiErrStatsTooShortDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 29),
    _CfprEtherNiErrStatsTooShortDelta_Type()
)
cfprEtherNiErrStatsTooShortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooShortDelta.setStatus("current")
_CfprEtherNiErrStatsTooShortDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsTooShortDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsTooShortDeltaAvg = _CfprEtherNiErrStatsTooShortDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 30),
    _CfprEtherNiErrStatsTooShortDeltaAvg_Type()
)
cfprEtherNiErrStatsTooShortDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooShortDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsTooShortDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsTooShortDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsTooShortDeltaMax = _CfprEtherNiErrStatsTooShortDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 31),
    _CfprEtherNiErrStatsTooShortDeltaMax_Type()
)
cfprEtherNiErrStatsTooShortDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooShortDeltaMax.setStatus("current")
_CfprEtherNiErrStatsTooShortDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsTooShortDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsTooShortDeltaMin = _CfprEtherNiErrStatsTooShortDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 32),
    _CfprEtherNiErrStatsTooShortDeltaMin_Type()
)
cfprEtherNiErrStatsTooShortDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsTooShortDeltaMin.setStatus("current")
_CfprEtherNiErrStatsUpdate_Type = Gauge32
_CfprEtherNiErrStatsUpdate_Object = MibTableColumn
cfprEtherNiErrStatsUpdate = _CfprEtherNiErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 7, 1, 33),
    _CfprEtherNiErrStatsUpdate_Type()
)
cfprEtherNiErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsUpdate.setStatus("current")
_CfprEtherNiErrStatsHistTable_Object = MibTable
cfprEtherNiErrStatsHistTable = _CfprEtherNiErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8)
)
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTable.setStatus("current")
_CfprEtherNiErrStatsHistEntry_Object = MibTableRow
cfprEtherNiErrStatsHistEntry = _CfprEtherNiErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1)
)
cfprEtherNiErrStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherNiErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistEntry.setStatus("current")
_CfprEtherNiErrStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherNiErrStatsHistInstanceId_Object = MibTableColumn
cfprEtherNiErrStatsHistInstanceId = _CfprEtherNiErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 1),
    _CfprEtherNiErrStatsHistInstanceId_Type()
)
cfprEtherNiErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistInstanceId.setStatus("current")
_CfprEtherNiErrStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherNiErrStatsHistDn_Object = MibTableColumn
cfprEtherNiErrStatsHistDn = _CfprEtherNiErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 2),
    _CfprEtherNiErrStatsHistDn_Type()
)
cfprEtherNiErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistDn.setStatus("current")
_CfprEtherNiErrStatsHistRn_Type = SnmpAdminString
_CfprEtherNiErrStatsHistRn_Object = MibTableColumn
cfprEtherNiErrStatsHistRn = _CfprEtherNiErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 3),
    _CfprEtherNiErrStatsHistRn_Type()
)
cfprEtherNiErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistRn.setStatus("current")
_CfprEtherNiErrStatsHistCrc_Type = Unsigned64
_CfprEtherNiErrStatsHistCrc_Object = MibTableColumn
cfprEtherNiErrStatsHistCrc = _CfprEtherNiErrStatsHistCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 4),
    _CfprEtherNiErrStatsHistCrc_Type()
)
cfprEtherNiErrStatsHistCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistCrc.setStatus("current")
_CfprEtherNiErrStatsHistCrcDelta_Type = Unsigned64
_CfprEtherNiErrStatsHistCrcDelta_Object = MibTableColumn
cfprEtherNiErrStatsHistCrcDelta = _CfprEtherNiErrStatsHistCrcDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 5),
    _CfprEtherNiErrStatsHistCrcDelta_Type()
)
cfprEtherNiErrStatsHistCrcDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistCrcDelta.setStatus("current")
_CfprEtherNiErrStatsHistCrcDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsHistCrcDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsHistCrcDeltaAvg = _CfprEtherNiErrStatsHistCrcDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 6),
    _CfprEtherNiErrStatsHistCrcDeltaAvg_Type()
)
cfprEtherNiErrStatsHistCrcDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistCrcDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsHistCrcDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsHistCrcDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsHistCrcDeltaMax = _CfprEtherNiErrStatsHistCrcDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 7),
    _CfprEtherNiErrStatsHistCrcDeltaMax_Type()
)
cfprEtherNiErrStatsHistCrcDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistCrcDeltaMax.setStatus("current")
_CfprEtherNiErrStatsHistCrcDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsHistCrcDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsHistCrcDeltaMin = _CfprEtherNiErrStatsHistCrcDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 8),
    _CfprEtherNiErrStatsHistCrcDeltaMin_Type()
)
cfprEtherNiErrStatsHistCrcDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistCrcDeltaMin.setStatus("current")
_CfprEtherNiErrStatsHistFrameTx_Type = Unsigned64
_CfprEtherNiErrStatsHistFrameTx_Object = MibTableColumn
cfprEtherNiErrStatsHistFrameTx = _CfprEtherNiErrStatsHistFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 9),
    _CfprEtherNiErrStatsHistFrameTx_Type()
)
cfprEtherNiErrStatsHistFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistFrameTx.setStatus("current")
_CfprEtherNiErrStatsHistFrameTxDelta_Type = Unsigned64
_CfprEtherNiErrStatsHistFrameTxDelta_Object = MibTableColumn
cfprEtherNiErrStatsHistFrameTxDelta = _CfprEtherNiErrStatsHistFrameTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 10),
    _CfprEtherNiErrStatsHistFrameTxDelta_Type()
)
cfprEtherNiErrStatsHistFrameTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistFrameTxDelta.setStatus("current")
_CfprEtherNiErrStatsHistFrameTxDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsHistFrameTxDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsHistFrameTxDeltaAvg = _CfprEtherNiErrStatsHistFrameTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 11),
    _CfprEtherNiErrStatsHistFrameTxDeltaAvg_Type()
)
cfprEtherNiErrStatsHistFrameTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistFrameTxDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsHistFrameTxDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsHistFrameTxDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsHistFrameTxDeltaMax = _CfprEtherNiErrStatsHistFrameTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 12),
    _CfprEtherNiErrStatsHistFrameTxDeltaMax_Type()
)
cfprEtherNiErrStatsHistFrameTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistFrameTxDeltaMax.setStatus("current")
_CfprEtherNiErrStatsHistFrameTxDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsHistFrameTxDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsHistFrameTxDeltaMin = _CfprEtherNiErrStatsHistFrameTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 13),
    _CfprEtherNiErrStatsHistFrameTxDeltaMin_Type()
)
cfprEtherNiErrStatsHistFrameTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistFrameTxDeltaMin.setStatus("current")
_CfprEtherNiErrStatsHistId_Type = Unsigned64
_CfprEtherNiErrStatsHistId_Object = MibTableColumn
cfprEtherNiErrStatsHistId = _CfprEtherNiErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 14),
    _CfprEtherNiErrStatsHistId_Type()
)
cfprEtherNiErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistId.setStatus("current")
_CfprEtherNiErrStatsHistInRange_Type = Unsigned64
_CfprEtherNiErrStatsHistInRange_Object = MibTableColumn
cfprEtherNiErrStatsHistInRange = _CfprEtherNiErrStatsHistInRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 15),
    _CfprEtherNiErrStatsHistInRange_Type()
)
cfprEtherNiErrStatsHistInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistInRange.setStatus("current")
_CfprEtherNiErrStatsHistInRangeDelta_Type = Unsigned64
_CfprEtherNiErrStatsHistInRangeDelta_Object = MibTableColumn
cfprEtherNiErrStatsHistInRangeDelta = _CfprEtherNiErrStatsHistInRangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 16),
    _CfprEtherNiErrStatsHistInRangeDelta_Type()
)
cfprEtherNiErrStatsHistInRangeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistInRangeDelta.setStatus("current")
_CfprEtherNiErrStatsHistInRangeDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsHistInRangeDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsHistInRangeDeltaAvg = _CfprEtherNiErrStatsHistInRangeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 17),
    _CfprEtherNiErrStatsHistInRangeDeltaAvg_Type()
)
cfprEtherNiErrStatsHistInRangeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistInRangeDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsHistInRangeDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsHistInRangeDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsHistInRangeDeltaMax = _CfprEtherNiErrStatsHistInRangeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 18),
    _CfprEtherNiErrStatsHistInRangeDeltaMax_Type()
)
cfprEtherNiErrStatsHistInRangeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistInRangeDeltaMax.setStatus("current")
_CfprEtherNiErrStatsHistInRangeDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsHistInRangeDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsHistInRangeDeltaMin = _CfprEtherNiErrStatsHistInRangeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 19),
    _CfprEtherNiErrStatsHistInRangeDeltaMin_Type()
)
cfprEtherNiErrStatsHistInRangeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistInRangeDeltaMin.setStatus("current")
_CfprEtherNiErrStatsHistMostRecent_Type = TruthValue
_CfprEtherNiErrStatsHistMostRecent_Object = MibTableColumn
cfprEtherNiErrStatsHistMostRecent = _CfprEtherNiErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 20),
    _CfprEtherNiErrStatsHistMostRecent_Type()
)
cfprEtherNiErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistMostRecent.setStatus("current")
_CfprEtherNiErrStatsHistSuspect_Type = TruthValue
_CfprEtherNiErrStatsHistSuspect_Object = MibTableColumn
cfprEtherNiErrStatsHistSuspect = _CfprEtherNiErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 21),
    _CfprEtherNiErrStatsHistSuspect_Type()
)
cfprEtherNiErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistSuspect.setStatus("current")
_CfprEtherNiErrStatsHistThresholded_Type = CfprEtherNiErrStatsHistThresholded
_CfprEtherNiErrStatsHistThresholded_Object = MibTableColumn
cfprEtherNiErrStatsHistThresholded = _CfprEtherNiErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 22),
    _CfprEtherNiErrStatsHistThresholded_Type()
)
cfprEtherNiErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistThresholded.setStatus("current")
_CfprEtherNiErrStatsHistTimeCollected_Type = DateAndTime
_CfprEtherNiErrStatsHistTimeCollected_Object = MibTableColumn
cfprEtherNiErrStatsHistTimeCollected = _CfprEtherNiErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 23),
    _CfprEtherNiErrStatsHistTimeCollected_Type()
)
cfprEtherNiErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTimeCollected.setStatus("current")
_CfprEtherNiErrStatsHistTooLong_Type = Unsigned64
_CfprEtherNiErrStatsHistTooLong_Object = MibTableColumn
cfprEtherNiErrStatsHistTooLong = _CfprEtherNiErrStatsHistTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 24),
    _CfprEtherNiErrStatsHistTooLong_Type()
)
cfprEtherNiErrStatsHistTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooLong.setStatus("current")
_CfprEtherNiErrStatsHistTooLongDelta_Type = Unsigned64
_CfprEtherNiErrStatsHistTooLongDelta_Object = MibTableColumn
cfprEtherNiErrStatsHistTooLongDelta = _CfprEtherNiErrStatsHistTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 25),
    _CfprEtherNiErrStatsHistTooLongDelta_Type()
)
cfprEtherNiErrStatsHistTooLongDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooLongDelta.setStatus("current")
_CfprEtherNiErrStatsHistTooLongDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsHistTooLongDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsHistTooLongDeltaAvg = _CfprEtherNiErrStatsHistTooLongDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 26),
    _CfprEtherNiErrStatsHistTooLongDeltaAvg_Type()
)
cfprEtherNiErrStatsHistTooLongDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooLongDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsHistTooLongDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsHistTooLongDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsHistTooLongDeltaMax = _CfprEtherNiErrStatsHistTooLongDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 27),
    _CfprEtherNiErrStatsHistTooLongDeltaMax_Type()
)
cfprEtherNiErrStatsHistTooLongDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooLongDeltaMax.setStatus("current")
_CfprEtherNiErrStatsHistTooLongDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsHistTooLongDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsHistTooLongDeltaMin = _CfprEtherNiErrStatsHistTooLongDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 28),
    _CfprEtherNiErrStatsHistTooLongDeltaMin_Type()
)
cfprEtherNiErrStatsHistTooLongDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooLongDeltaMin.setStatus("current")
_CfprEtherNiErrStatsHistTooShort_Type = Unsigned64
_CfprEtherNiErrStatsHistTooShort_Object = MibTableColumn
cfprEtherNiErrStatsHistTooShort = _CfprEtherNiErrStatsHistTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 29),
    _CfprEtherNiErrStatsHistTooShort_Type()
)
cfprEtherNiErrStatsHistTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooShort.setStatus("current")
_CfprEtherNiErrStatsHistTooShortDelta_Type = Unsigned64
_CfprEtherNiErrStatsHistTooShortDelta_Object = MibTableColumn
cfprEtherNiErrStatsHistTooShortDelta = _CfprEtherNiErrStatsHistTooShortDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 30),
    _CfprEtherNiErrStatsHistTooShortDelta_Type()
)
cfprEtherNiErrStatsHistTooShortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooShortDelta.setStatus("current")
_CfprEtherNiErrStatsHistTooShortDeltaAvg_Type = Unsigned64
_CfprEtherNiErrStatsHistTooShortDeltaAvg_Object = MibTableColumn
cfprEtherNiErrStatsHistTooShortDeltaAvg = _CfprEtherNiErrStatsHistTooShortDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 31),
    _CfprEtherNiErrStatsHistTooShortDeltaAvg_Type()
)
cfprEtherNiErrStatsHistTooShortDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooShortDeltaAvg.setStatus("current")
_CfprEtherNiErrStatsHistTooShortDeltaMax_Type = Unsigned64
_CfprEtherNiErrStatsHistTooShortDeltaMax_Object = MibTableColumn
cfprEtherNiErrStatsHistTooShortDeltaMax = _CfprEtherNiErrStatsHistTooShortDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 32),
    _CfprEtherNiErrStatsHistTooShortDeltaMax_Type()
)
cfprEtherNiErrStatsHistTooShortDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooShortDeltaMax.setStatus("current")
_CfprEtherNiErrStatsHistTooShortDeltaMin_Type = Unsigned64
_CfprEtherNiErrStatsHistTooShortDeltaMin_Object = MibTableColumn
cfprEtherNiErrStatsHistTooShortDeltaMin = _CfprEtherNiErrStatsHistTooShortDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 8, 1, 33),
    _CfprEtherNiErrStatsHistTooShortDeltaMin_Type()
)
cfprEtherNiErrStatsHistTooShortDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNiErrStatsHistTooShortDeltaMin.setStatus("current")
_CfprEtherNicIfConfigTable_Object = MibTable
cfprEtherNicIfConfigTable = _CfprEtherNicIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 9)
)
if mibBuilder.loadTexts:
    cfprEtherNicIfConfigTable.setStatus("current")
_CfprEtherNicIfConfigEntry_Object = MibTableRow
cfprEtherNicIfConfigEntry = _CfprEtherNicIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 9, 1)
)
cfprEtherNicIfConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherNicIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherNicIfConfigEntry.setStatus("current")
_CfprEtherNicIfConfigInstanceId_Type = CfprManagedObjectId
_CfprEtherNicIfConfigInstanceId_Object = MibTableColumn
cfprEtherNicIfConfigInstanceId = _CfprEtherNicIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 9, 1, 1),
    _CfprEtherNicIfConfigInstanceId_Type()
)
cfprEtherNicIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherNicIfConfigInstanceId.setStatus("current")
_CfprEtherNicIfConfigDn_Type = CfprManagedObjectDn
_CfprEtherNicIfConfigDn_Object = MibTableColumn
cfprEtherNicIfConfigDn = _CfprEtherNicIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 9, 1, 2),
    _CfprEtherNicIfConfigDn_Type()
)
cfprEtherNicIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNicIfConfigDn.setStatus("current")
_CfprEtherNicIfConfigRn_Type = SnmpAdminString
_CfprEtherNicIfConfigRn_Object = MibTableColumn
cfprEtherNicIfConfigRn = _CfprEtherNicIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 9, 1, 3),
    _CfprEtherNicIfConfigRn_Type()
)
cfprEtherNicIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherNicIfConfigRn.setStatus("current")
_CfprEtherPIoTable_Object = MibTable
cfprEtherPIoTable = _CfprEtherPIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10)
)
if mibBuilder.loadTexts:
    cfprEtherPIoTable.setStatus("current")
_CfprEtherPIoEntry_Object = MibTableRow
cfprEtherPIoEntry = _CfprEtherPIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1)
)
cfprEtherPIoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPIoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPIoEntry.setStatus("current")
_CfprEtherPIoInstanceId_Type = CfprManagedObjectId
_CfprEtherPIoInstanceId_Object = MibTableColumn
cfprEtherPIoInstanceId = _CfprEtherPIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 1),
    _CfprEtherPIoInstanceId_Type()
)
cfprEtherPIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPIoInstanceId.setStatus("current")
_CfprEtherPIoDn_Type = CfprManagedObjectDn
_CfprEtherPIoDn_Object = MibTableColumn
cfprEtherPIoDn = _CfprEtherPIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 2),
    _CfprEtherPIoDn_Type()
)
cfprEtherPIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoDn.setStatus("current")
_CfprEtherPIoRn_Type = SnmpAdminString
_CfprEtherPIoRn_Object = MibTableColumn
cfprEtherPIoRn = _CfprEtherPIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 3),
    _CfprEtherPIoRn_Type()
)
cfprEtherPIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoRn.setStatus("current")
_CfprEtherPIoAdminState_Type = CfprFabricAdminState
_CfprEtherPIoAdminState_Object = MibTableColumn
cfprEtherPIoAdminState = _CfprEtherPIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 4),
    _CfprEtherPIoAdminState_Type()
)
cfprEtherPIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoAdminState.setStatus("current")
_CfprEtherPIoAdminTransport_Type = CfprNetworkTransport
_CfprEtherPIoAdminTransport_Object = MibTableColumn
cfprEtherPIoAdminTransport = _CfprEtherPIoAdminTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 5),
    _CfprEtherPIoAdminTransport_Type()
)
cfprEtherPIoAdminTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoAdminTransport.setStatus("current")
_CfprEtherPIoAggrPortId_Type = Gauge32
_CfprEtherPIoAggrPortId_Object = MibTableColumn
cfprEtherPIoAggrPortId = _CfprEtherPIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 6),
    _CfprEtherPIoAggrPortId_Type()
)
cfprEtherPIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoAggrPortId.setStatus("current")
_CfprEtherPIoChassisId_Type = Gauge32
_CfprEtherPIoChassisId_Object = MibTableColumn
cfprEtherPIoChassisId = _CfprEtherPIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 7),
    _CfprEtherPIoChassisId_Type()
)
cfprEtherPIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoChassisId.setStatus("current")
_CfprEtherPIoEncap_Type = CfprPortEncap
_CfprEtherPIoEncap_Object = MibTableColumn
cfprEtherPIoEncap = _CfprEtherPIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 8),
    _CfprEtherPIoEncap_Type()
)
cfprEtherPIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEncap.setStatus("current")
_CfprEtherPIoEpDn_Type = SnmpAdminString
_CfprEtherPIoEpDn_Object = MibTableColumn
cfprEtherPIoEpDn = _CfprEtherPIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 9),
    _CfprEtherPIoEpDn_Type()
)
cfprEtherPIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEpDn.setStatus("current")
_CfprEtherPIoFltAggr_Type = Unsigned64
_CfprEtherPIoFltAggr_Object = MibTableColumn
cfprEtherPIoFltAggr = _CfprEtherPIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 10),
    _CfprEtherPIoFltAggr_Type()
)
cfprEtherPIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFltAggr.setStatus("current")
_CfprEtherPIoFsmDescr_Type = SnmpAdminString
_CfprEtherPIoFsmDescr_Object = MibTableColumn
cfprEtherPIoFsmDescr = _CfprEtherPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 11),
    _CfprEtherPIoFsmDescr_Type()
)
cfprEtherPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmDescr.setStatus("current")
_CfprEtherPIoFsmPrev_Type = SnmpAdminString
_CfprEtherPIoFsmPrev_Object = MibTableColumn
cfprEtherPIoFsmPrev = _CfprEtherPIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 12),
    _CfprEtherPIoFsmPrev_Type()
)
cfprEtherPIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmPrev.setStatus("current")
_CfprEtherPIoFsmProgr_Type = Gauge32
_CfprEtherPIoFsmProgr_Object = MibTableColumn
cfprEtherPIoFsmProgr = _CfprEtherPIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 13),
    _CfprEtherPIoFsmProgr_Type()
)
cfprEtherPIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmProgr.setStatus("current")
_CfprEtherPIoFsmRmtInvErrCode_Type = Gauge32
_CfprEtherPIoFsmRmtInvErrCode_Object = MibTableColumn
cfprEtherPIoFsmRmtInvErrCode = _CfprEtherPIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 14),
    _CfprEtherPIoFsmRmtInvErrCode_Type()
)
cfprEtherPIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRmtInvErrCode.setStatus("current")
_CfprEtherPIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprEtherPIoFsmRmtInvErrDescr_Object = MibTableColumn
cfprEtherPIoFsmRmtInvErrDescr = _CfprEtherPIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 15),
    _CfprEtherPIoFsmRmtInvErrDescr_Type()
)
cfprEtherPIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRmtInvErrDescr.setStatus("current")
_CfprEtherPIoFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprEtherPIoFsmRmtInvRslt_Object = MibTableColumn
cfprEtherPIoFsmRmtInvRslt = _CfprEtherPIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 16),
    _CfprEtherPIoFsmRmtInvRslt_Type()
)
cfprEtherPIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRmtInvRslt.setStatus("current")
_CfprEtherPIoFsmStageDescr_Type = SnmpAdminString
_CfprEtherPIoFsmStageDescr_Object = MibTableColumn
cfprEtherPIoFsmStageDescr = _CfprEtherPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 17),
    _CfprEtherPIoFsmStageDescr_Type()
)
cfprEtherPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageDescr.setStatus("current")
_CfprEtherPIoFsmStamp_Type = DateAndTime
_CfprEtherPIoFsmStamp_Object = MibTableColumn
cfprEtherPIoFsmStamp = _CfprEtherPIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 18),
    _CfprEtherPIoFsmStamp_Type()
)
cfprEtherPIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStamp.setStatus("current")
_CfprEtherPIoFsmStatus_Type = SnmpAdminString
_CfprEtherPIoFsmStatus_Object = MibTableColumn
cfprEtherPIoFsmStatus = _CfprEtherPIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 19),
    _CfprEtherPIoFsmStatus_Type()
)
cfprEtherPIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStatus.setStatus("current")
_CfprEtherPIoFsmTry_Type = Gauge32
_CfprEtherPIoFsmTry_Object = MibTableColumn
cfprEtherPIoFsmTry = _CfprEtherPIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 20),
    _CfprEtherPIoFsmTry_Type()
)
cfprEtherPIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmTry.setStatus("current")
_CfprEtherPIoIfRole_Type = CfprNetworkPortRole
_CfprEtherPIoIfRole_Object = MibTableColumn
cfprEtherPIoIfRole = _CfprEtherPIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 21),
    _CfprEtherPIoIfRole_Type()
)
cfprEtherPIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoIfRole.setStatus("current")
_CfprEtherPIoIfType_Type = CfprNetworkPhysEpIfType
_CfprEtherPIoIfType_Object = MibTableColumn
cfprEtherPIoIfType = _CfprEtherPIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 22),
    _CfprEtherPIoIfType_Type()
)
cfprEtherPIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoIfType.setStatus("current")
_CfprEtherPIoIsPortChannelMember_Type = TruthValue
_CfprEtherPIoIsPortChannelMember_Object = MibTableColumn
cfprEtherPIoIsPortChannelMember = _CfprEtherPIoIsPortChannelMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 23),
    _CfprEtherPIoIsPortChannelMember_Type()
)
cfprEtherPIoIsPortChannelMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoIsPortChannelMember.setStatus("current")
_CfprEtherPIoLc_Type = CfprFsmLifecycle
_CfprEtherPIoLc_Object = MibTableColumn
cfprEtherPIoLc = _CfprEtherPIoLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 24),
    _CfprEtherPIoLc_Type()
)
cfprEtherPIoLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoLc.setStatus("current")
_CfprEtherPIoLicGP_Type = Unsigned64
_CfprEtherPIoLicGP_Object = MibTableColumn
cfprEtherPIoLicGP = _CfprEtherPIoLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 25),
    _CfprEtherPIoLicGP_Type()
)
cfprEtherPIoLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoLicGP.setStatus("current")
_CfprEtherPIoLicState_Type = CfprLicenseState
_CfprEtherPIoLicState_Object = MibTableColumn
cfprEtherPIoLicState = _CfprEtherPIoLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 26),
    _CfprEtherPIoLicState_Type()
)
cfprEtherPIoLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoLicState.setStatus("current")
_CfprEtherPIoLocale_Type = CfprNetworkLocale
_CfprEtherPIoLocale_Object = MibTableColumn
cfprEtherPIoLocale = _CfprEtherPIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 27),
    _CfprEtherPIoLocale_Type()
)
cfprEtherPIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoLocale.setStatus("current")
_CfprEtherPIoMac_Type = MacAddress
_CfprEtherPIoMac_Object = MibTableColumn
cfprEtherPIoMac = _CfprEtherPIoMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 28),
    _CfprEtherPIoMac_Type()
)
cfprEtherPIoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoMac.setStatus("current")
_CfprEtherPIoMode_Type = CfprPortMode
_CfprEtherPIoMode_Object = MibTableColumn
cfprEtherPIoMode = _CfprEtherPIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 29),
    _CfprEtherPIoMode_Type()
)
cfprEtherPIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoMode.setStatus("current")
_CfprEtherPIoModel_Type = SnmpAdminString
_CfprEtherPIoModel_Object = MibTableColumn
cfprEtherPIoModel = _CfprEtherPIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 30),
    _CfprEtherPIoModel_Type()
)
cfprEtherPIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoModel.setStatus("current")
_CfprEtherPIoName_Type = SnmpAdminString
_CfprEtherPIoName_Object = MibTableColumn
cfprEtherPIoName = _CfprEtherPIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 31),
    _CfprEtherPIoName_Type()
)
cfprEtherPIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoName.setStatus("current")
_CfprEtherPIoOperSpeed_Type = CfprPortEthSpeed
_CfprEtherPIoOperSpeed_Object = MibTableColumn
cfprEtherPIoOperSpeed = _CfprEtherPIoOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 32),
    _CfprEtherPIoOperSpeed_Type()
)
cfprEtherPIoOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoOperSpeed.setStatus("current")
_CfprEtherPIoOperState_Type = CfprNetworkPortOperState
_CfprEtherPIoOperState_Object = MibTableColumn
cfprEtherPIoOperState = _CfprEtherPIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 33),
    _CfprEtherPIoOperState_Type()
)
cfprEtherPIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoOperState.setStatus("current")
_CfprEtherPIoPeerAggrPortId_Type = Gauge32
_CfprEtherPIoPeerAggrPortId_Object = MibTableColumn
cfprEtherPIoPeerAggrPortId = _CfprEtherPIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 34),
    _CfprEtherPIoPeerAggrPortId_Type()
)
cfprEtherPIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoPeerAggrPortId.setStatus("current")
_CfprEtherPIoPeerChassisId_Type = Gauge32
_CfprEtherPIoPeerChassisId_Object = MibTableColumn
cfprEtherPIoPeerChassisId = _CfprEtherPIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 35),
    _CfprEtherPIoPeerChassisId_Type()
)
cfprEtherPIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoPeerChassisId.setStatus("current")
_CfprEtherPIoPeerDn_Type = SnmpAdminString
_CfprEtherPIoPeerDn_Object = MibTableColumn
cfprEtherPIoPeerDn = _CfprEtherPIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 36),
    _CfprEtherPIoPeerDn_Type()
)
cfprEtherPIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoPeerDn.setStatus("current")
_CfprEtherPIoPeerPortId_Type = Gauge32
_CfprEtherPIoPeerPortId_Object = MibTableColumn
cfprEtherPIoPeerPortId = _CfprEtherPIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 37),
    _CfprEtherPIoPeerPortId_Type()
)
cfprEtherPIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoPeerPortId.setStatus("current")
_CfprEtherPIoPeerSlotId_Type = Gauge32
_CfprEtherPIoPeerSlotId_Object = MibTableColumn
cfprEtherPIoPeerSlotId = _CfprEtherPIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 38),
    _CfprEtherPIoPeerSlotId_Type()
)
cfprEtherPIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoPeerSlotId.setStatus("current")
_CfprEtherPIoPortId_Type = Gauge32
_CfprEtherPIoPortId_Object = MibTableColumn
cfprEtherPIoPortId = _CfprEtherPIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 39),
    _CfprEtherPIoPortId_Type()
)
cfprEtherPIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoPortId.setStatus("current")
_CfprEtherPIoRevision_Type = SnmpAdminString
_CfprEtherPIoRevision_Object = MibTableColumn
cfprEtherPIoRevision = _CfprEtherPIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 40),
    _CfprEtherPIoRevision_Type()
)
cfprEtherPIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoRevision.setStatus("current")
_CfprEtherPIoSerial_Type = SnmpAdminString
_CfprEtherPIoSerial_Object = MibTableColumn
cfprEtherPIoSerial = _CfprEtherPIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 41),
    _CfprEtherPIoSerial_Type()
)
cfprEtherPIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoSerial.setStatus("current")
_CfprEtherPIoSlotId_Type = Gauge32
_CfprEtherPIoSlotId_Object = MibTableColumn
cfprEtherPIoSlotId = _CfprEtherPIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 42),
    _CfprEtherPIoSlotId_Type()
)
cfprEtherPIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoSlotId.setStatus("current")
_CfprEtherPIoStateQual_Type = SnmpAdminString
_CfprEtherPIoStateQual_Object = MibTableColumn
cfprEtherPIoStateQual = _CfprEtherPIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 43),
    _CfprEtherPIoStateQual_Type()
)
cfprEtherPIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoStateQual.setStatus("current")
_CfprEtherPIoSwitchId_Type = CfprNetworkSwitchId
_CfprEtherPIoSwitchId_Object = MibTableColumn
cfprEtherPIoSwitchId = _CfprEtherPIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 44),
    _CfprEtherPIoSwitchId_Type()
)
cfprEtherPIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoSwitchId.setStatus("current")
_CfprEtherPIoTransport_Type = CfprNetworkTransport
_CfprEtherPIoTransport_Object = MibTableColumn
cfprEtherPIoTransport = _CfprEtherPIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 45),
    _CfprEtherPIoTransport_Type()
)
cfprEtherPIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoTransport.setStatus("current")
_CfprEtherPIoTs_Type = DateAndTime
_CfprEtherPIoTs_Object = MibTableColumn
cfprEtherPIoTs = _CfprEtherPIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 46),
    _CfprEtherPIoTs_Type()
)
cfprEtherPIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoTs.setStatus("current")
_CfprEtherPIoType_Type = CfprNetworkConnectionType
_CfprEtherPIoType_Object = MibTableColumn
cfprEtherPIoType = _CfprEtherPIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 47),
    _CfprEtherPIoType_Type()
)
cfprEtherPIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoType.setStatus("current")
_CfprEtherPIoUnifiedPort_Type = TruthValue
_CfprEtherPIoUnifiedPort_Object = MibTableColumn
cfprEtherPIoUnifiedPort = _CfprEtherPIoUnifiedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 48),
    _CfprEtherPIoUnifiedPort_Type()
)
cfprEtherPIoUnifiedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoUnifiedPort.setStatus("current")
_CfprEtherPIoUsrLbl_Type = SnmpAdminString
_CfprEtherPIoUsrLbl_Object = MibTableColumn
cfprEtherPIoUsrLbl = _CfprEtherPIoUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 49),
    _CfprEtherPIoUsrLbl_Type()
)
cfprEtherPIoUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoUsrLbl.setStatus("current")
_CfprEtherPIoVendor_Type = SnmpAdminString
_CfprEtherPIoVendor_Object = MibTableColumn
cfprEtherPIoVendor = _CfprEtherPIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 50),
    _CfprEtherPIoVendor_Type()
)
cfprEtherPIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoVendor.setStatus("current")
_CfprEtherPIoXcvrType_Type = CfprEquipmentXcvrType
_CfprEtherPIoXcvrType_Object = MibTableColumn
cfprEtherPIoXcvrType = _CfprEtherPIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 51),
    _CfprEtherPIoXcvrType_Type()
)
cfprEtherPIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoXcvrType.setStatus("current")
_CfprEtherPIoFtwPhyDn_Type = SnmpAdminString
_CfprEtherPIoFtwPhyDn_Object = MibTableColumn
cfprEtherPIoFtwPhyDn = _CfprEtherPIoFtwPhyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 52),
    _CfprEtherPIoFtwPhyDn_Type()
)
cfprEtherPIoFtwPhyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFtwPhyDn.setStatus("current")
_CfprEtherPIoOperDuplex_Type = CfprPortDuplex
_CfprEtherPIoOperDuplex_Object = MibTableColumn
cfprEtherPIoOperDuplex = _CfprEtherPIoOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 10, 1, 53),
    _CfprEtherPIoOperDuplex_Type()
)
cfprEtherPIoOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoOperDuplex.setStatus("current")
_CfprEtherPIoEndPointTable_Object = MibTable
cfprEtherPIoEndPointTable = _CfprEtherPIoEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11)
)
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointTable.setStatus("current")
_CfprEtherPIoEndPointEntry_Object = MibTableRow
cfprEtherPIoEndPointEntry = _CfprEtherPIoEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1)
)
cfprEtherPIoEndPointEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPIoEndPointInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointEntry.setStatus("current")
_CfprEtherPIoEndPointInstanceId_Type = CfprManagedObjectId
_CfprEtherPIoEndPointInstanceId_Object = MibTableColumn
cfprEtherPIoEndPointInstanceId = _CfprEtherPIoEndPointInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1, 1),
    _CfprEtherPIoEndPointInstanceId_Type()
)
cfprEtherPIoEndPointInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointInstanceId.setStatus("current")
_CfprEtherPIoEndPointDn_Type = CfprManagedObjectDn
_CfprEtherPIoEndPointDn_Object = MibTableColumn
cfprEtherPIoEndPointDn = _CfprEtherPIoEndPointDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1, 2),
    _CfprEtherPIoEndPointDn_Type()
)
cfprEtherPIoEndPointDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointDn.setStatus("current")
_CfprEtherPIoEndPointRn_Type = SnmpAdminString
_CfprEtherPIoEndPointRn_Object = MibTableColumn
cfprEtherPIoEndPointRn = _CfprEtherPIoEndPointRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1, 3),
    _CfprEtherPIoEndPointRn_Type()
)
cfprEtherPIoEndPointRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointRn.setStatus("current")
_CfprEtherPIoEndPointEndPointDn_Type = SnmpAdminString
_CfprEtherPIoEndPointEndPointDn_Object = MibTableColumn
cfprEtherPIoEndPointEndPointDn = _CfprEtherPIoEndPointEndPointDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1, 4),
    _CfprEtherPIoEndPointEndPointDn_Type()
)
cfprEtherPIoEndPointEndPointDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointEndPointDn.setStatus("current")
_CfprEtherPIoEndPointEpCloudType_Type = CfprEtherCloudType
_CfprEtherPIoEndPointEpCloudType_Object = MibTableColumn
cfprEtherPIoEndPointEpCloudType = _CfprEtherPIoEndPointEpCloudType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1, 5),
    _CfprEtherPIoEndPointEpCloudType_Type()
)
cfprEtherPIoEndPointEpCloudType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointEpCloudType.setStatus("current")
_CfprEtherPIoEndPointUsrLbl_Type = SnmpAdminString
_CfprEtherPIoEndPointUsrLbl_Object = MibTableColumn
cfprEtherPIoEndPointUsrLbl = _CfprEtherPIoEndPointUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 11, 1, 6),
    _CfprEtherPIoEndPointUsrLbl_Type()
)
cfprEtherPIoEndPointUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoEndPointUsrLbl.setStatus("current")
_CfprEtherPIoFsmTable_Object = MibTable
cfprEtherPIoFsmTable = _CfprEtherPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12)
)
if mibBuilder.loadTexts:
    cfprEtherPIoFsmTable.setStatus("current")
_CfprEtherPIoFsmEntry_Object = MibTableRow
cfprEtherPIoFsmEntry = _CfprEtherPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1)
)
cfprEtherPIoFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPIoFsmEntry.setStatus("current")
_CfprEtherPIoFsmInstanceId_Type = CfprManagedObjectId
_CfprEtherPIoFsmInstanceId_Object = MibTableColumn
cfprEtherPIoFsmInstanceId = _CfprEtherPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 1),
    _CfprEtherPIoFsmInstanceId_Type()
)
cfprEtherPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmInstanceId.setStatus("current")
_CfprEtherPIoFsmDn_Type = CfprManagedObjectDn
_CfprEtherPIoFsmDn_Object = MibTableColumn
cfprEtherPIoFsmDn = _CfprEtherPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 2),
    _CfprEtherPIoFsmDn_Type()
)
cfprEtherPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmDn.setStatus("current")
_CfprEtherPIoFsmRn_Type = SnmpAdminString
_CfprEtherPIoFsmRn_Object = MibTableColumn
cfprEtherPIoFsmRn = _CfprEtherPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 3),
    _CfprEtherPIoFsmRn_Type()
)
cfprEtherPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRn.setStatus("current")
_CfprEtherPIoFsmCompletionTime_Type = DateAndTime
_CfprEtherPIoFsmCompletionTime_Object = MibTableColumn
cfprEtherPIoFsmCompletionTime = _CfprEtherPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 4),
    _CfprEtherPIoFsmCompletionTime_Type()
)
cfprEtherPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmCompletionTime.setStatus("current")
_CfprEtherPIoFsmCurrentFsm_Type = CfprEtherPIoFsmCurrentFsm
_CfprEtherPIoFsmCurrentFsm_Object = MibTableColumn
cfprEtherPIoFsmCurrentFsm = _CfprEtherPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 5),
    _CfprEtherPIoFsmCurrentFsm_Type()
)
cfprEtherPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmCurrentFsm.setStatus("current")
_CfprEtherPIoFsmDescrData_Type = SnmpAdminString
_CfprEtherPIoFsmDescrData_Object = MibTableColumn
cfprEtherPIoFsmDescrData = _CfprEtherPIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 6),
    _CfprEtherPIoFsmDescrData_Type()
)
cfprEtherPIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmDescrData.setStatus("current")
_CfprEtherPIoFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprEtherPIoFsmFsmStatus_Object = MibTableColumn
cfprEtherPIoFsmFsmStatus = _CfprEtherPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 7),
    _CfprEtherPIoFsmFsmStatus_Type()
)
cfprEtherPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmFsmStatus.setStatus("current")
_CfprEtherPIoFsmProgress_Type = Gauge32
_CfprEtherPIoFsmProgress_Object = MibTableColumn
cfprEtherPIoFsmProgress = _CfprEtherPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 8),
    _CfprEtherPIoFsmProgress_Type()
)
cfprEtherPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmProgress.setStatus("current")
_CfprEtherPIoFsmRmtErrCode_Type = Gauge32
_CfprEtherPIoFsmRmtErrCode_Object = MibTableColumn
cfprEtherPIoFsmRmtErrCode = _CfprEtherPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 9),
    _CfprEtherPIoFsmRmtErrCode_Type()
)
cfprEtherPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRmtErrCode.setStatus("current")
_CfprEtherPIoFsmRmtErrDescr_Type = SnmpAdminString
_CfprEtherPIoFsmRmtErrDescr_Object = MibTableColumn
cfprEtherPIoFsmRmtErrDescr = _CfprEtherPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 10),
    _CfprEtherPIoFsmRmtErrDescr_Type()
)
cfprEtherPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRmtErrDescr.setStatus("current")
_CfprEtherPIoFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprEtherPIoFsmRmtRslt_Object = MibTableColumn
cfprEtherPIoFsmRmtRslt = _CfprEtherPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 12, 1, 11),
    _CfprEtherPIoFsmRmtRslt_Type()
)
cfprEtherPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmRmtRslt.setStatus("current")
_CfprEtherPIoFsmStageTable_Object = MibTable
cfprEtherPIoFsmStageTable = _CfprEtherPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13)
)
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageTable.setStatus("current")
_CfprEtherPIoFsmStageEntry_Object = MibTableRow
cfprEtherPIoFsmStageEntry = _CfprEtherPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1)
)
cfprEtherPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageEntry.setStatus("current")
_CfprEtherPIoFsmStageInstanceId_Type = CfprManagedObjectId
_CfprEtherPIoFsmStageInstanceId_Object = MibTableColumn
cfprEtherPIoFsmStageInstanceId = _CfprEtherPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 1),
    _CfprEtherPIoFsmStageInstanceId_Type()
)
cfprEtherPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageInstanceId.setStatus("current")
_CfprEtherPIoFsmStageDn_Type = CfprManagedObjectDn
_CfprEtherPIoFsmStageDn_Object = MibTableColumn
cfprEtherPIoFsmStageDn = _CfprEtherPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 2),
    _CfprEtherPIoFsmStageDn_Type()
)
cfprEtherPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageDn.setStatus("current")
_CfprEtherPIoFsmStageRn_Type = SnmpAdminString
_CfprEtherPIoFsmStageRn_Object = MibTableColumn
cfprEtherPIoFsmStageRn = _CfprEtherPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 3),
    _CfprEtherPIoFsmStageRn_Type()
)
cfprEtherPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageRn.setStatus("current")
_CfprEtherPIoFsmStageDescrData_Type = SnmpAdminString
_CfprEtherPIoFsmStageDescrData_Object = MibTableColumn
cfprEtherPIoFsmStageDescrData = _CfprEtherPIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 4),
    _CfprEtherPIoFsmStageDescrData_Type()
)
cfprEtherPIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageDescrData.setStatus("current")
_CfprEtherPIoFsmStageLastUpdateTime_Type = DateAndTime
_CfprEtherPIoFsmStageLastUpdateTime_Object = MibTableColumn
cfprEtherPIoFsmStageLastUpdateTime = _CfprEtherPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 5),
    _CfprEtherPIoFsmStageLastUpdateTime_Type()
)
cfprEtherPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageLastUpdateTime.setStatus("current")
_CfprEtherPIoFsmStageName_Type = CfprEtherPIoFsmStageName
_CfprEtherPIoFsmStageName_Object = MibTableColumn
cfprEtherPIoFsmStageName = _CfprEtherPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 6),
    _CfprEtherPIoFsmStageName_Type()
)
cfprEtherPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageName.setStatus("current")
_CfprEtherPIoFsmStageOrder_Type = Gauge32
_CfprEtherPIoFsmStageOrder_Object = MibTableColumn
cfprEtherPIoFsmStageOrder = _CfprEtherPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 7),
    _CfprEtherPIoFsmStageOrder_Type()
)
cfprEtherPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageOrder.setStatus("current")
_CfprEtherPIoFsmStageRetry_Type = Gauge32
_CfprEtherPIoFsmStageRetry_Object = MibTableColumn
cfprEtherPIoFsmStageRetry = _CfprEtherPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 8),
    _CfprEtherPIoFsmStageRetry_Type()
)
cfprEtherPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageRetry.setStatus("current")
_CfprEtherPIoFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprEtherPIoFsmStageStageStatus_Object = MibTableColumn
cfprEtherPIoFsmStageStageStatus = _CfprEtherPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 13, 1, 9),
    _CfprEtherPIoFsmStageStageStatus_Type()
)
cfprEtherPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPIoFsmStageStageStatus.setStatus("current")
_CfprEtherPauseStatsTable_Object = MibTable
cfprEtherPauseStatsTable = _CfprEtherPauseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14)
)
if mibBuilder.loadTexts:
    cfprEtherPauseStatsTable.setStatus("current")
_CfprEtherPauseStatsEntry_Object = MibTableRow
cfprEtherPauseStatsEntry = _CfprEtherPauseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1)
)
cfprEtherPauseStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPauseStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPauseStatsEntry.setStatus("current")
_CfprEtherPauseStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherPauseStatsInstanceId_Object = MibTableColumn
cfprEtherPauseStatsInstanceId = _CfprEtherPauseStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 1),
    _CfprEtherPauseStatsInstanceId_Type()
)
cfprEtherPauseStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsInstanceId.setStatus("current")
_CfprEtherPauseStatsDn_Type = CfprManagedObjectDn
_CfprEtherPauseStatsDn_Object = MibTableColumn
cfprEtherPauseStatsDn = _CfprEtherPauseStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 2),
    _CfprEtherPauseStatsDn_Type()
)
cfprEtherPauseStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsDn.setStatus("current")
_CfprEtherPauseStatsRn_Type = SnmpAdminString
_CfprEtherPauseStatsRn_Object = MibTableColumn
cfprEtherPauseStatsRn = _CfprEtherPauseStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 3),
    _CfprEtherPauseStatsRn_Type()
)
cfprEtherPauseStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsRn.setStatus("current")
_CfprEtherPauseStatsIntervals_Type = Gauge32
_CfprEtherPauseStatsIntervals_Object = MibTableColumn
cfprEtherPauseStatsIntervals = _CfprEtherPauseStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 4),
    _CfprEtherPauseStatsIntervals_Type()
)
cfprEtherPauseStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsIntervals.setStatus("current")
_CfprEtherPauseStatsRecvPause_Type = Unsigned64
_CfprEtherPauseStatsRecvPause_Object = MibTableColumn
cfprEtherPauseStatsRecvPause = _CfprEtherPauseStatsRecvPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 5),
    _CfprEtherPauseStatsRecvPause_Type()
)
cfprEtherPauseStatsRecvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsRecvPause.setStatus("current")
_CfprEtherPauseStatsRecvPauseDelta_Type = Counter64
_CfprEtherPauseStatsRecvPauseDelta_Object = MibTableColumn
cfprEtherPauseStatsRecvPauseDelta = _CfprEtherPauseStatsRecvPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 6),
    _CfprEtherPauseStatsRecvPauseDelta_Type()
)
cfprEtherPauseStatsRecvPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsRecvPauseDelta.setStatus("current")
_CfprEtherPauseStatsRecvPauseDeltaAvg_Type = Unsigned64
_CfprEtherPauseStatsRecvPauseDeltaAvg_Object = MibTableColumn
cfprEtherPauseStatsRecvPauseDeltaAvg = _CfprEtherPauseStatsRecvPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 7),
    _CfprEtherPauseStatsRecvPauseDeltaAvg_Type()
)
cfprEtherPauseStatsRecvPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsRecvPauseDeltaAvg.setStatus("current")
_CfprEtherPauseStatsRecvPauseDeltaMax_Type = Unsigned64
_CfprEtherPauseStatsRecvPauseDeltaMax_Object = MibTableColumn
cfprEtherPauseStatsRecvPauseDeltaMax = _CfprEtherPauseStatsRecvPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 8),
    _CfprEtherPauseStatsRecvPauseDeltaMax_Type()
)
cfprEtherPauseStatsRecvPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsRecvPauseDeltaMax.setStatus("current")
_CfprEtherPauseStatsRecvPauseDeltaMin_Type = Unsigned64
_CfprEtherPauseStatsRecvPauseDeltaMin_Object = MibTableColumn
cfprEtherPauseStatsRecvPauseDeltaMin = _CfprEtherPauseStatsRecvPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 9),
    _CfprEtherPauseStatsRecvPauseDeltaMin_Type()
)
cfprEtherPauseStatsRecvPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsRecvPauseDeltaMin.setStatus("current")
_CfprEtherPauseStatsResets_Type = Unsigned64
_CfprEtherPauseStatsResets_Object = MibTableColumn
cfprEtherPauseStatsResets = _CfprEtherPauseStatsResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 10),
    _CfprEtherPauseStatsResets_Type()
)
cfprEtherPauseStatsResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsResets.setStatus("current")
_CfprEtherPauseStatsResetsDelta_Type = Counter64
_CfprEtherPauseStatsResetsDelta_Object = MibTableColumn
cfprEtherPauseStatsResetsDelta = _CfprEtherPauseStatsResetsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 11),
    _CfprEtherPauseStatsResetsDelta_Type()
)
cfprEtherPauseStatsResetsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsResetsDelta.setStatus("current")
_CfprEtherPauseStatsResetsDeltaAvg_Type = Unsigned64
_CfprEtherPauseStatsResetsDeltaAvg_Object = MibTableColumn
cfprEtherPauseStatsResetsDeltaAvg = _CfprEtherPauseStatsResetsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 12),
    _CfprEtherPauseStatsResetsDeltaAvg_Type()
)
cfprEtherPauseStatsResetsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsResetsDeltaAvg.setStatus("current")
_CfprEtherPauseStatsResetsDeltaMax_Type = Unsigned64
_CfprEtherPauseStatsResetsDeltaMax_Object = MibTableColumn
cfprEtherPauseStatsResetsDeltaMax = _CfprEtherPauseStatsResetsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 13),
    _CfprEtherPauseStatsResetsDeltaMax_Type()
)
cfprEtherPauseStatsResetsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsResetsDeltaMax.setStatus("current")
_CfprEtherPauseStatsResetsDeltaMin_Type = Unsigned64
_CfprEtherPauseStatsResetsDeltaMin_Object = MibTableColumn
cfprEtherPauseStatsResetsDeltaMin = _CfprEtherPauseStatsResetsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 14),
    _CfprEtherPauseStatsResetsDeltaMin_Type()
)
cfprEtherPauseStatsResetsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsResetsDeltaMin.setStatus("current")
_CfprEtherPauseStatsSuspect_Type = TruthValue
_CfprEtherPauseStatsSuspect_Object = MibTableColumn
cfprEtherPauseStatsSuspect = _CfprEtherPauseStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 15),
    _CfprEtherPauseStatsSuspect_Type()
)
cfprEtherPauseStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsSuspect.setStatus("current")
_CfprEtherPauseStatsThresholded_Type = CfprEtherPauseStatsThresholded
_CfprEtherPauseStatsThresholded_Object = MibTableColumn
cfprEtherPauseStatsThresholded = _CfprEtherPauseStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 16),
    _CfprEtherPauseStatsThresholded_Type()
)
cfprEtherPauseStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsThresholded.setStatus("current")
_CfprEtherPauseStatsTimeCollected_Type = DateAndTime
_CfprEtherPauseStatsTimeCollected_Object = MibTableColumn
cfprEtherPauseStatsTimeCollected = _CfprEtherPauseStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 17),
    _CfprEtherPauseStatsTimeCollected_Type()
)
cfprEtherPauseStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsTimeCollected.setStatus("current")
_CfprEtherPauseStatsUpdate_Type = Gauge32
_CfprEtherPauseStatsUpdate_Object = MibTableColumn
cfprEtherPauseStatsUpdate = _CfprEtherPauseStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 18),
    _CfprEtherPauseStatsUpdate_Type()
)
cfprEtherPauseStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsUpdate.setStatus("current")
_CfprEtherPauseStatsXmitPause_Type = Unsigned64
_CfprEtherPauseStatsXmitPause_Object = MibTableColumn
cfprEtherPauseStatsXmitPause = _CfprEtherPauseStatsXmitPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 19),
    _CfprEtherPauseStatsXmitPause_Type()
)
cfprEtherPauseStatsXmitPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsXmitPause.setStatus("current")
_CfprEtherPauseStatsXmitPauseDelta_Type = Counter64
_CfprEtherPauseStatsXmitPauseDelta_Object = MibTableColumn
cfprEtherPauseStatsXmitPauseDelta = _CfprEtherPauseStatsXmitPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 20),
    _CfprEtherPauseStatsXmitPauseDelta_Type()
)
cfprEtherPauseStatsXmitPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsXmitPauseDelta.setStatus("current")
_CfprEtherPauseStatsXmitPauseDeltaAvg_Type = Unsigned64
_CfprEtherPauseStatsXmitPauseDeltaAvg_Object = MibTableColumn
cfprEtherPauseStatsXmitPauseDeltaAvg = _CfprEtherPauseStatsXmitPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 21),
    _CfprEtherPauseStatsXmitPauseDeltaAvg_Type()
)
cfprEtherPauseStatsXmitPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsXmitPauseDeltaAvg.setStatus("current")
_CfprEtherPauseStatsXmitPauseDeltaMax_Type = Unsigned64
_CfprEtherPauseStatsXmitPauseDeltaMax_Object = MibTableColumn
cfprEtherPauseStatsXmitPauseDeltaMax = _CfprEtherPauseStatsXmitPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 22),
    _CfprEtherPauseStatsXmitPauseDeltaMax_Type()
)
cfprEtherPauseStatsXmitPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsXmitPauseDeltaMax.setStatus("current")
_CfprEtherPauseStatsXmitPauseDeltaMin_Type = Unsigned64
_CfprEtherPauseStatsXmitPauseDeltaMin_Object = MibTableColumn
cfprEtherPauseStatsXmitPauseDeltaMin = _CfprEtherPauseStatsXmitPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 14, 1, 23),
    _CfprEtherPauseStatsXmitPauseDeltaMin_Type()
)
cfprEtherPauseStatsXmitPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsXmitPauseDeltaMin.setStatus("current")
_CfprEtherPauseStatsHistTable_Object = MibTable
cfprEtherPauseStatsHistTable = _CfprEtherPauseStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15)
)
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistTable.setStatus("current")
_CfprEtherPauseStatsHistEntry_Object = MibTableRow
cfprEtherPauseStatsHistEntry = _CfprEtherPauseStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1)
)
cfprEtherPauseStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPauseStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistEntry.setStatus("current")
_CfprEtherPauseStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherPauseStatsHistInstanceId_Object = MibTableColumn
cfprEtherPauseStatsHistInstanceId = _CfprEtherPauseStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 1),
    _CfprEtherPauseStatsHistInstanceId_Type()
)
cfprEtherPauseStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistInstanceId.setStatus("current")
_CfprEtherPauseStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherPauseStatsHistDn_Object = MibTableColumn
cfprEtherPauseStatsHistDn = _CfprEtherPauseStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 2),
    _CfprEtherPauseStatsHistDn_Type()
)
cfprEtherPauseStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistDn.setStatus("current")
_CfprEtherPauseStatsHistRn_Type = SnmpAdminString
_CfprEtherPauseStatsHistRn_Object = MibTableColumn
cfprEtherPauseStatsHistRn = _CfprEtherPauseStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 3),
    _CfprEtherPauseStatsHistRn_Type()
)
cfprEtherPauseStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistRn.setStatus("current")
_CfprEtherPauseStatsHistId_Type = Unsigned64
_CfprEtherPauseStatsHistId_Object = MibTableColumn
cfprEtherPauseStatsHistId = _CfprEtherPauseStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 4),
    _CfprEtherPauseStatsHistId_Type()
)
cfprEtherPauseStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistId.setStatus("current")
_CfprEtherPauseStatsHistMostRecent_Type = TruthValue
_CfprEtherPauseStatsHistMostRecent_Object = MibTableColumn
cfprEtherPauseStatsHistMostRecent = _CfprEtherPauseStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 5),
    _CfprEtherPauseStatsHistMostRecent_Type()
)
cfprEtherPauseStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistMostRecent.setStatus("current")
_CfprEtherPauseStatsHistRecvPause_Type = Unsigned64
_CfprEtherPauseStatsHistRecvPause_Object = MibTableColumn
cfprEtherPauseStatsHistRecvPause = _CfprEtherPauseStatsHistRecvPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 6),
    _CfprEtherPauseStatsHistRecvPause_Type()
)
cfprEtherPauseStatsHistRecvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistRecvPause.setStatus("current")
_CfprEtherPauseStatsHistRecvPauseDelta_Type = Unsigned64
_CfprEtherPauseStatsHistRecvPauseDelta_Object = MibTableColumn
cfprEtherPauseStatsHistRecvPauseDelta = _CfprEtherPauseStatsHistRecvPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 7),
    _CfprEtherPauseStatsHistRecvPauseDelta_Type()
)
cfprEtherPauseStatsHistRecvPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistRecvPauseDelta.setStatus("current")
_CfprEtherPauseStatsHistRecvPauseDeltaAvg_Type = Unsigned64
_CfprEtherPauseStatsHistRecvPauseDeltaAvg_Object = MibTableColumn
cfprEtherPauseStatsHistRecvPauseDeltaAvg = _CfprEtherPauseStatsHistRecvPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 8),
    _CfprEtherPauseStatsHistRecvPauseDeltaAvg_Type()
)
cfprEtherPauseStatsHistRecvPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistRecvPauseDeltaAvg.setStatus("current")
_CfprEtherPauseStatsHistRecvPauseDeltaMax_Type = Unsigned64
_CfprEtherPauseStatsHistRecvPauseDeltaMax_Object = MibTableColumn
cfprEtherPauseStatsHistRecvPauseDeltaMax = _CfprEtherPauseStatsHistRecvPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 9),
    _CfprEtherPauseStatsHistRecvPauseDeltaMax_Type()
)
cfprEtherPauseStatsHistRecvPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistRecvPauseDeltaMax.setStatus("current")
_CfprEtherPauseStatsHistRecvPauseDeltaMin_Type = Unsigned64
_CfprEtherPauseStatsHistRecvPauseDeltaMin_Object = MibTableColumn
cfprEtherPauseStatsHistRecvPauseDeltaMin = _CfprEtherPauseStatsHistRecvPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 10),
    _CfprEtherPauseStatsHistRecvPauseDeltaMin_Type()
)
cfprEtherPauseStatsHistRecvPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistRecvPauseDeltaMin.setStatus("current")
_CfprEtherPauseStatsHistResets_Type = Unsigned64
_CfprEtherPauseStatsHistResets_Object = MibTableColumn
cfprEtherPauseStatsHistResets = _CfprEtherPauseStatsHistResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 11),
    _CfprEtherPauseStatsHistResets_Type()
)
cfprEtherPauseStatsHistResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistResets.setStatus("current")
_CfprEtherPauseStatsHistResetsDelta_Type = Unsigned64
_CfprEtherPauseStatsHistResetsDelta_Object = MibTableColumn
cfprEtherPauseStatsHistResetsDelta = _CfprEtherPauseStatsHistResetsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 12),
    _CfprEtherPauseStatsHistResetsDelta_Type()
)
cfprEtherPauseStatsHistResetsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistResetsDelta.setStatus("current")
_CfprEtherPauseStatsHistResetsDeltaAvg_Type = Unsigned64
_CfprEtherPauseStatsHistResetsDeltaAvg_Object = MibTableColumn
cfprEtherPauseStatsHistResetsDeltaAvg = _CfprEtherPauseStatsHistResetsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 13),
    _CfprEtherPauseStatsHistResetsDeltaAvg_Type()
)
cfprEtherPauseStatsHistResetsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistResetsDeltaAvg.setStatus("current")
_CfprEtherPauseStatsHistResetsDeltaMax_Type = Unsigned64
_CfprEtherPauseStatsHistResetsDeltaMax_Object = MibTableColumn
cfprEtherPauseStatsHistResetsDeltaMax = _CfprEtherPauseStatsHistResetsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 14),
    _CfprEtherPauseStatsHistResetsDeltaMax_Type()
)
cfprEtherPauseStatsHistResetsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistResetsDeltaMax.setStatus("current")
_CfprEtherPauseStatsHistResetsDeltaMin_Type = Unsigned64
_CfprEtherPauseStatsHistResetsDeltaMin_Object = MibTableColumn
cfprEtherPauseStatsHistResetsDeltaMin = _CfprEtherPauseStatsHistResetsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 15),
    _CfprEtherPauseStatsHistResetsDeltaMin_Type()
)
cfprEtherPauseStatsHistResetsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistResetsDeltaMin.setStatus("current")
_CfprEtherPauseStatsHistSuspect_Type = TruthValue
_CfprEtherPauseStatsHistSuspect_Object = MibTableColumn
cfprEtherPauseStatsHistSuspect = _CfprEtherPauseStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 16),
    _CfprEtherPauseStatsHistSuspect_Type()
)
cfprEtherPauseStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistSuspect.setStatus("current")
_CfprEtherPauseStatsHistThresholded_Type = CfprEtherPauseStatsHistThresholded
_CfprEtherPauseStatsHistThresholded_Object = MibTableColumn
cfprEtherPauseStatsHistThresholded = _CfprEtherPauseStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 17),
    _CfprEtherPauseStatsHistThresholded_Type()
)
cfprEtherPauseStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistThresholded.setStatus("current")
_CfprEtherPauseStatsHistTimeCollected_Type = DateAndTime
_CfprEtherPauseStatsHistTimeCollected_Object = MibTableColumn
cfprEtherPauseStatsHistTimeCollected = _CfprEtherPauseStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 18),
    _CfprEtherPauseStatsHistTimeCollected_Type()
)
cfprEtherPauseStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistTimeCollected.setStatus("current")
_CfprEtherPauseStatsHistXmitPause_Type = Unsigned64
_CfprEtherPauseStatsHistXmitPause_Object = MibTableColumn
cfprEtherPauseStatsHistXmitPause = _CfprEtherPauseStatsHistXmitPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 19),
    _CfprEtherPauseStatsHistXmitPause_Type()
)
cfprEtherPauseStatsHistXmitPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistXmitPause.setStatus("current")
_CfprEtherPauseStatsHistXmitPauseDelta_Type = Unsigned64
_CfprEtherPauseStatsHistXmitPauseDelta_Object = MibTableColumn
cfprEtherPauseStatsHistXmitPauseDelta = _CfprEtherPauseStatsHistXmitPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 20),
    _CfprEtherPauseStatsHistXmitPauseDelta_Type()
)
cfprEtherPauseStatsHistXmitPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistXmitPauseDelta.setStatus("current")
_CfprEtherPauseStatsHistXmitPauseDeltaAvg_Type = Unsigned64
_CfprEtherPauseStatsHistXmitPauseDeltaAvg_Object = MibTableColumn
cfprEtherPauseStatsHistXmitPauseDeltaAvg = _CfprEtherPauseStatsHistXmitPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 21),
    _CfprEtherPauseStatsHistXmitPauseDeltaAvg_Type()
)
cfprEtherPauseStatsHistXmitPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistXmitPauseDeltaAvg.setStatus("current")
_CfprEtherPauseStatsHistXmitPauseDeltaMax_Type = Unsigned64
_CfprEtherPauseStatsHistXmitPauseDeltaMax_Object = MibTableColumn
cfprEtherPauseStatsHistXmitPauseDeltaMax = _CfprEtherPauseStatsHistXmitPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 22),
    _CfprEtherPauseStatsHistXmitPauseDeltaMax_Type()
)
cfprEtherPauseStatsHistXmitPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistXmitPauseDeltaMax.setStatus("current")
_CfprEtherPauseStatsHistXmitPauseDeltaMin_Type = Unsigned64
_CfprEtherPauseStatsHistXmitPauseDeltaMin_Object = MibTableColumn
cfprEtherPauseStatsHistXmitPauseDeltaMin = _CfprEtherPauseStatsHistXmitPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 15, 1, 23),
    _CfprEtherPauseStatsHistXmitPauseDeltaMin_Type()
)
cfprEtherPauseStatsHistXmitPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPauseStatsHistXmitPauseDeltaMin.setStatus("current")
_CfprEtherPortChanIdElemTable_Object = MibTable
cfprEtherPortChanIdElemTable = _CfprEtherPortChanIdElemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 16)
)
if mibBuilder.loadTexts:
    cfprEtherPortChanIdElemTable.setStatus("current")
_CfprEtherPortChanIdElemEntry_Object = MibTableRow
cfprEtherPortChanIdElemEntry = _CfprEtherPortChanIdElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 16, 1)
)
cfprEtherPortChanIdElemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPortChanIdElemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPortChanIdElemEntry.setStatus("current")
_CfprEtherPortChanIdElemInstanceId_Type = CfprManagedObjectId
_CfprEtherPortChanIdElemInstanceId_Object = MibTableColumn
cfprEtherPortChanIdElemInstanceId = _CfprEtherPortChanIdElemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 16, 1, 1),
    _CfprEtherPortChanIdElemInstanceId_Type()
)
cfprEtherPortChanIdElemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdElemInstanceId.setStatus("current")
_CfprEtherPortChanIdElemDn_Type = CfprManagedObjectDn
_CfprEtherPortChanIdElemDn_Object = MibTableColumn
cfprEtherPortChanIdElemDn = _CfprEtherPortChanIdElemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 16, 1, 2),
    _CfprEtherPortChanIdElemDn_Type()
)
cfprEtherPortChanIdElemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdElemDn.setStatus("current")
_CfprEtherPortChanIdElemRn_Type = SnmpAdminString
_CfprEtherPortChanIdElemRn_Object = MibTableColumn
cfprEtherPortChanIdElemRn = _CfprEtherPortChanIdElemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 16, 1, 3),
    _CfprEtherPortChanIdElemRn_Type()
)
cfprEtherPortChanIdElemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdElemRn.setStatus("current")
_CfprEtherPortChanIdElemId_Type = Gauge32
_CfprEtherPortChanIdElemId_Object = MibTableColumn
cfprEtherPortChanIdElemId = _CfprEtherPortChanIdElemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 16, 1, 4),
    _CfprEtherPortChanIdElemId_Type()
)
cfprEtherPortChanIdElemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdElemId.setStatus("current")
_CfprEtherPortChanIdUniverseTable_Object = MibTable
cfprEtherPortChanIdUniverseTable = _CfprEtherPortChanIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 17)
)
if mibBuilder.loadTexts:
    cfprEtherPortChanIdUniverseTable.setStatus("current")
_CfprEtherPortChanIdUniverseEntry_Object = MibTableRow
cfprEtherPortChanIdUniverseEntry = _CfprEtherPortChanIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 17, 1)
)
cfprEtherPortChanIdUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherPortChanIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherPortChanIdUniverseEntry.setStatus("current")
_CfprEtherPortChanIdUniverseInstanceId_Type = CfprManagedObjectId
_CfprEtherPortChanIdUniverseInstanceId_Object = MibTableColumn
cfprEtherPortChanIdUniverseInstanceId = _CfprEtherPortChanIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 17, 1, 1),
    _CfprEtherPortChanIdUniverseInstanceId_Type()
)
cfprEtherPortChanIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdUniverseInstanceId.setStatus("current")
_CfprEtherPortChanIdUniverseDn_Type = CfprManagedObjectDn
_CfprEtherPortChanIdUniverseDn_Object = MibTableColumn
cfprEtherPortChanIdUniverseDn = _CfprEtherPortChanIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 17, 1, 2),
    _CfprEtherPortChanIdUniverseDn_Type()
)
cfprEtherPortChanIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdUniverseDn.setStatus("current")
_CfprEtherPortChanIdUniverseRn_Type = SnmpAdminString
_CfprEtherPortChanIdUniverseRn_Object = MibTableColumn
cfprEtherPortChanIdUniverseRn = _CfprEtherPortChanIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 17, 1, 3),
    _CfprEtherPortChanIdUniverseRn_Type()
)
cfprEtherPortChanIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherPortChanIdUniverseRn.setStatus("current")
_CfprEtherRxStatsTable_Object = MibTable
cfprEtherRxStatsTable = _CfprEtherRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18)
)
if mibBuilder.loadTexts:
    cfprEtherRxStatsTable.setStatus("current")
_CfprEtherRxStatsEntry_Object = MibTableRow
cfprEtherRxStatsEntry = _CfprEtherRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1)
)
cfprEtherRxStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherRxStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherRxStatsEntry.setStatus("current")
_CfprEtherRxStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherRxStatsInstanceId_Object = MibTableColumn
cfprEtherRxStatsInstanceId = _CfprEtherRxStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 1),
    _CfprEtherRxStatsInstanceId_Type()
)
cfprEtherRxStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherRxStatsInstanceId.setStatus("current")
_CfprEtherRxStatsDn_Type = CfprManagedObjectDn
_CfprEtherRxStatsDn_Object = MibTableColumn
cfprEtherRxStatsDn = _CfprEtherRxStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 2),
    _CfprEtherRxStatsDn_Type()
)
cfprEtherRxStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsDn.setStatus("current")
_CfprEtherRxStatsRn_Type = SnmpAdminString
_CfprEtherRxStatsRn_Object = MibTableColumn
cfprEtherRxStatsRn = _CfprEtherRxStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 3),
    _CfprEtherRxStatsRn_Type()
)
cfprEtherRxStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsRn.setStatus("current")
_CfprEtherRxStatsBroadcastPackets_Type = Unsigned64
_CfprEtherRxStatsBroadcastPackets_Object = MibTableColumn
cfprEtherRxStatsBroadcastPackets = _CfprEtherRxStatsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 4),
    _CfprEtherRxStatsBroadcastPackets_Type()
)
cfprEtherRxStatsBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsBroadcastPackets.setStatus("current")
_CfprEtherRxStatsBroadcastPacketsDelta_Type = Counter64
_CfprEtherRxStatsBroadcastPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsBroadcastPacketsDelta = _CfprEtherRxStatsBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 5),
    _CfprEtherRxStatsBroadcastPacketsDelta_Type()
)
cfprEtherRxStatsBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsBroadcastPacketsDelta.setStatus("current")
_CfprEtherRxStatsBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsBroadcastPacketsDeltaAvg = _CfprEtherRxStatsBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 6),
    _CfprEtherRxStatsBroadcastPacketsDeltaAvg_Type()
)
cfprEtherRxStatsBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsBroadcastPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsBroadcastPacketsDeltaMax = _CfprEtherRxStatsBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 7),
    _CfprEtherRxStatsBroadcastPacketsDeltaMax_Type()
)
cfprEtherRxStatsBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsBroadcastPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsBroadcastPacketsDeltaMin = _CfprEtherRxStatsBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 8),
    _CfprEtherRxStatsBroadcastPacketsDeltaMin_Type()
)
cfprEtherRxStatsBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsBroadcastPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsIntervals_Type = Gauge32
_CfprEtherRxStatsIntervals_Object = MibTableColumn
cfprEtherRxStatsIntervals = _CfprEtherRxStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 9),
    _CfprEtherRxStatsIntervals_Type()
)
cfprEtherRxStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsIntervals.setStatus("current")
_CfprEtherRxStatsJumboPackets_Type = Unsigned64
_CfprEtherRxStatsJumboPackets_Object = MibTableColumn
cfprEtherRxStatsJumboPackets = _CfprEtherRxStatsJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 10),
    _CfprEtherRxStatsJumboPackets_Type()
)
cfprEtherRxStatsJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsJumboPackets.setStatus("current")
_CfprEtherRxStatsJumboPacketsDelta_Type = Counter64
_CfprEtherRxStatsJumboPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsJumboPacketsDelta = _CfprEtherRxStatsJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 11),
    _CfprEtherRxStatsJumboPacketsDelta_Type()
)
cfprEtherRxStatsJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsJumboPacketsDelta.setStatus("current")
_CfprEtherRxStatsJumboPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsJumboPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsJumboPacketsDeltaAvg = _CfprEtherRxStatsJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 12),
    _CfprEtherRxStatsJumboPacketsDeltaAvg_Type()
)
cfprEtherRxStatsJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsJumboPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsJumboPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsJumboPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsJumboPacketsDeltaMax = _CfprEtherRxStatsJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 13),
    _CfprEtherRxStatsJumboPacketsDeltaMax_Type()
)
cfprEtherRxStatsJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsJumboPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsJumboPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsJumboPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsJumboPacketsDeltaMin = _CfprEtherRxStatsJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 14),
    _CfprEtherRxStatsJumboPacketsDeltaMin_Type()
)
cfprEtherRxStatsJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsJumboPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsMulticastPackets_Type = Unsigned64
_CfprEtherRxStatsMulticastPackets_Object = MibTableColumn
cfprEtherRxStatsMulticastPackets = _CfprEtherRxStatsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 15),
    _CfprEtherRxStatsMulticastPackets_Type()
)
cfprEtherRxStatsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsMulticastPackets.setStatus("current")
_CfprEtherRxStatsMulticastPacketsDelta_Type = Counter64
_CfprEtherRxStatsMulticastPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsMulticastPacketsDelta = _CfprEtherRxStatsMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 16),
    _CfprEtherRxStatsMulticastPacketsDelta_Type()
)
cfprEtherRxStatsMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsMulticastPacketsDelta.setStatus("current")
_CfprEtherRxStatsMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsMulticastPacketsDeltaAvg = _CfprEtherRxStatsMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 17),
    _CfprEtherRxStatsMulticastPacketsDeltaAvg_Type()
)
cfprEtherRxStatsMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsMulticastPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsMulticastPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsMulticastPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsMulticastPacketsDeltaMax = _CfprEtherRxStatsMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 18),
    _CfprEtherRxStatsMulticastPacketsDeltaMax_Type()
)
cfprEtherRxStatsMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsMulticastPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsMulticastPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsMulticastPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsMulticastPacketsDeltaMin = _CfprEtherRxStatsMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 19),
    _CfprEtherRxStatsMulticastPacketsDeltaMin_Type()
)
cfprEtherRxStatsMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsMulticastPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsSuspect_Type = TruthValue
_CfprEtherRxStatsSuspect_Object = MibTableColumn
cfprEtherRxStatsSuspect = _CfprEtherRxStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 20),
    _CfprEtherRxStatsSuspect_Type()
)
cfprEtherRxStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsSuspect.setStatus("current")
_CfprEtherRxStatsThresholded_Type = CfprEtherRxStatsThresholded
_CfprEtherRxStatsThresholded_Object = MibTableColumn
cfprEtherRxStatsThresholded = _CfprEtherRxStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 21),
    _CfprEtherRxStatsThresholded_Type()
)
cfprEtherRxStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsThresholded.setStatus("current")
_CfprEtherRxStatsTimeCollected_Type = DateAndTime
_CfprEtherRxStatsTimeCollected_Object = MibTableColumn
cfprEtherRxStatsTimeCollected = _CfprEtherRxStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 22),
    _CfprEtherRxStatsTimeCollected_Type()
)
cfprEtherRxStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTimeCollected.setStatus("current")
_CfprEtherRxStatsTotalBytes_Type = Unsigned64
_CfprEtherRxStatsTotalBytes_Object = MibTableColumn
cfprEtherRxStatsTotalBytes = _CfprEtherRxStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 23),
    _CfprEtherRxStatsTotalBytes_Type()
)
cfprEtherRxStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalBytes.setStatus("current")
_CfprEtherRxStatsTotalBytesDelta_Type = Counter64
_CfprEtherRxStatsTotalBytesDelta_Object = MibTableColumn
cfprEtherRxStatsTotalBytesDelta = _CfprEtherRxStatsTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 24),
    _CfprEtherRxStatsTotalBytesDelta_Type()
)
cfprEtherRxStatsTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalBytesDelta.setStatus("current")
_CfprEtherRxStatsTotalBytesDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsTotalBytesDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsTotalBytesDeltaAvg = _CfprEtherRxStatsTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 25),
    _CfprEtherRxStatsTotalBytesDeltaAvg_Type()
)
cfprEtherRxStatsTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalBytesDeltaAvg.setStatus("current")
_CfprEtherRxStatsTotalBytesDeltaMax_Type = Unsigned64
_CfprEtherRxStatsTotalBytesDeltaMax_Object = MibTableColumn
cfprEtherRxStatsTotalBytesDeltaMax = _CfprEtherRxStatsTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 26),
    _CfprEtherRxStatsTotalBytesDeltaMax_Type()
)
cfprEtherRxStatsTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalBytesDeltaMax.setStatus("current")
_CfprEtherRxStatsTotalBytesDeltaMin_Type = Unsigned64
_CfprEtherRxStatsTotalBytesDeltaMin_Object = MibTableColumn
cfprEtherRxStatsTotalBytesDeltaMin = _CfprEtherRxStatsTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 27),
    _CfprEtherRxStatsTotalBytesDeltaMin_Type()
)
cfprEtherRxStatsTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalBytesDeltaMin.setStatus("current")
_CfprEtherRxStatsTotalPackets_Type = Unsigned64
_CfprEtherRxStatsTotalPackets_Object = MibTableColumn
cfprEtherRxStatsTotalPackets = _CfprEtherRxStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 28),
    _CfprEtherRxStatsTotalPackets_Type()
)
cfprEtherRxStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalPackets.setStatus("current")
_CfprEtherRxStatsTotalPacketsDelta_Type = Counter64
_CfprEtherRxStatsTotalPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsTotalPacketsDelta = _CfprEtherRxStatsTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 29),
    _CfprEtherRxStatsTotalPacketsDelta_Type()
)
cfprEtherRxStatsTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalPacketsDelta.setStatus("current")
_CfprEtherRxStatsTotalPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsTotalPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsTotalPacketsDeltaAvg = _CfprEtherRxStatsTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 30),
    _CfprEtherRxStatsTotalPacketsDeltaAvg_Type()
)
cfprEtherRxStatsTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsTotalPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsTotalPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsTotalPacketsDeltaMax = _CfprEtherRxStatsTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 31),
    _CfprEtherRxStatsTotalPacketsDeltaMax_Type()
)
cfprEtherRxStatsTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsTotalPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsTotalPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsTotalPacketsDeltaMin = _CfprEtherRxStatsTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 32),
    _CfprEtherRxStatsTotalPacketsDeltaMin_Type()
)
cfprEtherRxStatsTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsTotalPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsUnicastPackets_Type = Unsigned64
_CfprEtherRxStatsUnicastPackets_Object = MibTableColumn
cfprEtherRxStatsUnicastPackets = _CfprEtherRxStatsUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 33),
    _CfprEtherRxStatsUnicastPackets_Type()
)
cfprEtherRxStatsUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsUnicastPackets.setStatus("current")
_CfprEtherRxStatsUnicastPacketsDelta_Type = Counter64
_CfprEtherRxStatsUnicastPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsUnicastPacketsDelta = _CfprEtherRxStatsUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 34),
    _CfprEtherRxStatsUnicastPacketsDelta_Type()
)
cfprEtherRxStatsUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsUnicastPacketsDelta.setStatus("current")
_CfprEtherRxStatsUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsUnicastPacketsDeltaAvg = _CfprEtherRxStatsUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 35),
    _CfprEtherRxStatsUnicastPacketsDeltaAvg_Type()
)
cfprEtherRxStatsUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsUnicastPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsUnicastPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsUnicastPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsUnicastPacketsDeltaMax = _CfprEtherRxStatsUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 36),
    _CfprEtherRxStatsUnicastPacketsDeltaMax_Type()
)
cfprEtherRxStatsUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsUnicastPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsUnicastPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsUnicastPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsUnicastPacketsDeltaMin = _CfprEtherRxStatsUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 37),
    _CfprEtherRxStatsUnicastPacketsDeltaMin_Type()
)
cfprEtherRxStatsUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsUnicastPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsUpdate_Type = Gauge32
_CfprEtherRxStatsUpdate_Object = MibTableColumn
cfprEtherRxStatsUpdate = _CfprEtherRxStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 18, 1, 38),
    _CfprEtherRxStatsUpdate_Type()
)
cfprEtherRxStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsUpdate.setStatus("current")
_CfprEtherRxStatsHistTable_Object = MibTable
cfprEtherRxStatsHistTable = _CfprEtherRxStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19)
)
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTable.setStatus("current")
_CfprEtherRxStatsHistEntry_Object = MibTableRow
cfprEtherRxStatsHistEntry = _CfprEtherRxStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1)
)
cfprEtherRxStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherRxStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistEntry.setStatus("current")
_CfprEtherRxStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherRxStatsHistInstanceId_Object = MibTableColumn
cfprEtherRxStatsHistInstanceId = _CfprEtherRxStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 1),
    _CfprEtherRxStatsHistInstanceId_Type()
)
cfprEtherRxStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistInstanceId.setStatus("current")
_CfprEtherRxStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherRxStatsHistDn_Object = MibTableColumn
cfprEtherRxStatsHistDn = _CfprEtherRxStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 2),
    _CfprEtherRxStatsHistDn_Type()
)
cfprEtherRxStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistDn.setStatus("current")
_CfprEtherRxStatsHistRn_Type = SnmpAdminString
_CfprEtherRxStatsHistRn_Object = MibTableColumn
cfprEtherRxStatsHistRn = _CfprEtherRxStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 3),
    _CfprEtherRxStatsHistRn_Type()
)
cfprEtherRxStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistRn.setStatus("current")
_CfprEtherRxStatsHistBroadcastPackets_Type = Unsigned64
_CfprEtherRxStatsHistBroadcastPackets_Object = MibTableColumn
cfprEtherRxStatsHistBroadcastPackets = _CfprEtherRxStatsHistBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 4),
    _CfprEtherRxStatsHistBroadcastPackets_Type()
)
cfprEtherRxStatsHistBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistBroadcastPackets.setStatus("current")
_CfprEtherRxStatsHistBroadcastPacketsDelta_Type = Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDelta = _CfprEtherRxStatsHistBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 5),
    _CfprEtherRxStatsHistBroadcastPacketsDelta_Type()
)
cfprEtherRxStatsHistBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistBroadcastPacketsDelta.setStatus("current")
_CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDeltaAvg = _CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 6),
    _CfprEtherRxStatsHistBroadcastPacketsDeltaAvg_Type()
)
cfprEtherRxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistBroadcastPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDeltaMax = _CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 7),
    _CfprEtherRxStatsHistBroadcastPacketsDeltaMax_Type()
)
cfprEtherRxStatsHistBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistBroadcastPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsHistBroadcastPacketsDeltaMin = _CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 8),
    _CfprEtherRxStatsHistBroadcastPacketsDeltaMin_Type()
)
cfprEtherRxStatsHistBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistBroadcastPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsHistId_Type = Unsigned64
_CfprEtherRxStatsHistId_Object = MibTableColumn
cfprEtherRxStatsHistId = _CfprEtherRxStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 9),
    _CfprEtherRxStatsHistId_Type()
)
cfprEtherRxStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistId.setStatus("current")
_CfprEtherRxStatsHistJumboPackets_Type = Unsigned64
_CfprEtherRxStatsHistJumboPackets_Object = MibTableColumn
cfprEtherRxStatsHistJumboPackets = _CfprEtherRxStatsHistJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 10),
    _CfprEtherRxStatsHistJumboPackets_Type()
)
cfprEtherRxStatsHistJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistJumboPackets.setStatus("current")
_CfprEtherRxStatsHistJumboPacketsDelta_Type = Unsigned64
_CfprEtherRxStatsHistJumboPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsHistJumboPacketsDelta = _CfprEtherRxStatsHistJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 11),
    _CfprEtherRxStatsHistJumboPacketsDelta_Type()
)
cfprEtherRxStatsHistJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistJumboPacketsDelta.setStatus("current")
_CfprEtherRxStatsHistJumboPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsHistJumboPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsHistJumboPacketsDeltaAvg = _CfprEtherRxStatsHistJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 12),
    _CfprEtherRxStatsHistJumboPacketsDeltaAvg_Type()
)
cfprEtherRxStatsHistJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistJumboPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsHistJumboPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsHistJumboPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsHistJumboPacketsDeltaMax = _CfprEtherRxStatsHistJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 13),
    _CfprEtherRxStatsHistJumboPacketsDeltaMax_Type()
)
cfprEtherRxStatsHistJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistJumboPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsHistJumboPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsHistJumboPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsHistJumboPacketsDeltaMin = _CfprEtherRxStatsHistJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 14),
    _CfprEtherRxStatsHistJumboPacketsDeltaMin_Type()
)
cfprEtherRxStatsHistJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistJumboPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsHistMostRecent_Type = TruthValue
_CfprEtherRxStatsHistMostRecent_Object = MibTableColumn
cfprEtherRxStatsHistMostRecent = _CfprEtherRxStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 15),
    _CfprEtherRxStatsHistMostRecent_Type()
)
cfprEtherRxStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistMostRecent.setStatus("current")
_CfprEtherRxStatsHistMulticastPackets_Type = Unsigned64
_CfprEtherRxStatsHistMulticastPackets_Object = MibTableColumn
cfprEtherRxStatsHistMulticastPackets = _CfprEtherRxStatsHistMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 16),
    _CfprEtherRxStatsHistMulticastPackets_Type()
)
cfprEtherRxStatsHistMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistMulticastPackets.setStatus("current")
_CfprEtherRxStatsHistMulticastPacketsDelta_Type = Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDelta = _CfprEtherRxStatsHistMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 17),
    _CfprEtherRxStatsHistMulticastPacketsDelta_Type()
)
cfprEtherRxStatsHistMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistMulticastPacketsDelta.setStatus("current")
_CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDeltaAvg = _CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 18),
    _CfprEtherRxStatsHistMulticastPacketsDeltaAvg_Type()
)
cfprEtherRxStatsHistMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistMulticastPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsHistMulticastPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDeltaMax = _CfprEtherRxStatsHistMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 19),
    _CfprEtherRxStatsHistMulticastPacketsDeltaMax_Type()
)
cfprEtherRxStatsHistMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistMulticastPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsHistMulticastPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsHistMulticastPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsHistMulticastPacketsDeltaMin = _CfprEtherRxStatsHistMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 20),
    _CfprEtherRxStatsHistMulticastPacketsDeltaMin_Type()
)
cfprEtherRxStatsHistMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistMulticastPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsHistSuspect_Type = TruthValue
_CfprEtherRxStatsHistSuspect_Object = MibTableColumn
cfprEtherRxStatsHistSuspect = _CfprEtherRxStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 21),
    _CfprEtherRxStatsHistSuspect_Type()
)
cfprEtherRxStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistSuspect.setStatus("current")
_CfprEtherRxStatsHistThresholded_Type = CfprEtherRxStatsHistThresholded
_CfprEtherRxStatsHistThresholded_Object = MibTableColumn
cfprEtherRxStatsHistThresholded = _CfprEtherRxStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 22),
    _CfprEtherRxStatsHistThresholded_Type()
)
cfprEtherRxStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistThresholded.setStatus("current")
_CfprEtherRxStatsHistTimeCollected_Type = DateAndTime
_CfprEtherRxStatsHistTimeCollected_Object = MibTableColumn
cfprEtherRxStatsHistTimeCollected = _CfprEtherRxStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 23),
    _CfprEtherRxStatsHistTimeCollected_Type()
)
cfprEtherRxStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTimeCollected.setStatus("current")
_CfprEtherRxStatsHistTotalBytes_Type = Unsigned64
_CfprEtherRxStatsHistTotalBytes_Object = MibTableColumn
cfprEtherRxStatsHistTotalBytes = _CfprEtherRxStatsHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 24),
    _CfprEtherRxStatsHistTotalBytes_Type()
)
cfprEtherRxStatsHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalBytes.setStatus("current")
_CfprEtherRxStatsHistTotalBytesDelta_Type = Unsigned64
_CfprEtherRxStatsHistTotalBytesDelta_Object = MibTableColumn
cfprEtherRxStatsHistTotalBytesDelta = _CfprEtherRxStatsHistTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 25),
    _CfprEtherRxStatsHistTotalBytesDelta_Type()
)
cfprEtherRxStatsHistTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalBytesDelta.setStatus("current")
_CfprEtherRxStatsHistTotalBytesDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsHistTotalBytesDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsHistTotalBytesDeltaAvg = _CfprEtherRxStatsHistTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 26),
    _CfprEtherRxStatsHistTotalBytesDeltaAvg_Type()
)
cfprEtherRxStatsHistTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalBytesDeltaAvg.setStatus("current")
_CfprEtherRxStatsHistTotalBytesDeltaMax_Type = Unsigned64
_CfprEtherRxStatsHistTotalBytesDeltaMax_Object = MibTableColumn
cfprEtherRxStatsHistTotalBytesDeltaMax = _CfprEtherRxStatsHistTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 27),
    _CfprEtherRxStatsHistTotalBytesDeltaMax_Type()
)
cfprEtherRxStatsHistTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalBytesDeltaMax.setStatus("current")
_CfprEtherRxStatsHistTotalBytesDeltaMin_Type = Unsigned64
_CfprEtherRxStatsHistTotalBytesDeltaMin_Object = MibTableColumn
cfprEtherRxStatsHistTotalBytesDeltaMin = _CfprEtherRxStatsHistTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 28),
    _CfprEtherRxStatsHistTotalBytesDeltaMin_Type()
)
cfprEtherRxStatsHistTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalBytesDeltaMin.setStatus("current")
_CfprEtherRxStatsHistTotalPackets_Type = Unsigned64
_CfprEtherRxStatsHistTotalPackets_Object = MibTableColumn
cfprEtherRxStatsHistTotalPackets = _CfprEtherRxStatsHistTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 29),
    _CfprEtherRxStatsHistTotalPackets_Type()
)
cfprEtherRxStatsHistTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalPackets.setStatus("current")
_CfprEtherRxStatsHistTotalPacketsDelta_Type = Unsigned64
_CfprEtherRxStatsHistTotalPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsHistTotalPacketsDelta = _CfprEtherRxStatsHistTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 30),
    _CfprEtherRxStatsHistTotalPacketsDelta_Type()
)
cfprEtherRxStatsHistTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalPacketsDelta.setStatus("current")
_CfprEtherRxStatsHistTotalPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsHistTotalPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsHistTotalPacketsDeltaAvg = _CfprEtherRxStatsHistTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 31),
    _CfprEtherRxStatsHistTotalPacketsDeltaAvg_Type()
)
cfprEtherRxStatsHistTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsHistTotalPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsHistTotalPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsHistTotalPacketsDeltaMax = _CfprEtherRxStatsHistTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 32),
    _CfprEtherRxStatsHistTotalPacketsDeltaMax_Type()
)
cfprEtherRxStatsHistTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsHistTotalPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsHistTotalPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsHistTotalPacketsDeltaMin = _CfprEtherRxStatsHistTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 33),
    _CfprEtherRxStatsHistTotalPacketsDeltaMin_Type()
)
cfprEtherRxStatsHistTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistTotalPacketsDeltaMin.setStatus("current")
_CfprEtherRxStatsHistUnicastPackets_Type = Unsigned64
_CfprEtherRxStatsHistUnicastPackets_Object = MibTableColumn
cfprEtherRxStatsHistUnicastPackets = _CfprEtherRxStatsHistUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 34),
    _CfprEtherRxStatsHistUnicastPackets_Type()
)
cfprEtherRxStatsHistUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistUnicastPackets.setStatus("current")
_CfprEtherRxStatsHistUnicastPacketsDelta_Type = Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDelta_Object = MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDelta = _CfprEtherRxStatsHistUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 35),
    _CfprEtherRxStatsHistUnicastPacketsDelta_Type()
)
cfprEtherRxStatsHistUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistUnicastPacketsDelta.setStatus("current")
_CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDeltaAvg = _CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 36),
    _CfprEtherRxStatsHistUnicastPacketsDeltaAvg_Type()
)
cfprEtherRxStatsHistUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistUnicastPacketsDeltaAvg.setStatus("current")
_CfprEtherRxStatsHistUnicastPacketsDeltaMax_Type = Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDeltaMax_Object = MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDeltaMax = _CfprEtherRxStatsHistUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 37),
    _CfprEtherRxStatsHistUnicastPacketsDeltaMax_Type()
)
cfprEtherRxStatsHistUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistUnicastPacketsDeltaMax.setStatus("current")
_CfprEtherRxStatsHistUnicastPacketsDeltaMin_Type = Unsigned64
_CfprEtherRxStatsHistUnicastPacketsDeltaMin_Object = MibTableColumn
cfprEtherRxStatsHistUnicastPacketsDeltaMin = _CfprEtherRxStatsHistUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 19, 1, 38),
    _CfprEtherRxStatsHistUnicastPacketsDeltaMin_Type()
)
cfprEtherRxStatsHistUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherRxStatsHistUnicastPacketsDeltaMin.setStatus("current")
_CfprEtherServerIntFIoTable_Object = MibTable
cfprEtherServerIntFIoTable = _CfprEtherServerIntFIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20)
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoTable.setStatus("current")
_CfprEtherServerIntFIoEntry_Object = MibTableRow
cfprEtherServerIntFIoEntry = _CfprEtherServerIntFIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1)
)
cfprEtherServerIntFIoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherServerIntFIoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoEntry.setStatus("current")
_CfprEtherServerIntFIoInstanceId_Type = CfprManagedObjectId
_CfprEtherServerIntFIoInstanceId_Object = MibTableColumn
cfprEtherServerIntFIoInstanceId = _CfprEtherServerIntFIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 1),
    _CfprEtherServerIntFIoInstanceId_Type()
)
cfprEtherServerIntFIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoInstanceId.setStatus("current")
_CfprEtherServerIntFIoDn_Type = CfprManagedObjectDn
_CfprEtherServerIntFIoDn_Object = MibTableColumn
cfprEtherServerIntFIoDn = _CfprEtherServerIntFIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 2),
    _CfprEtherServerIntFIoDn_Type()
)
cfprEtherServerIntFIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoDn.setStatus("current")
_CfprEtherServerIntFIoRn_Type = SnmpAdminString
_CfprEtherServerIntFIoRn_Object = MibTableColumn
cfprEtherServerIntFIoRn = _CfprEtherServerIntFIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 3),
    _CfprEtherServerIntFIoRn_Type()
)
cfprEtherServerIntFIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoRn.setStatus("current")
_CfprEtherServerIntFIoAdminSpeed_Type = CfprPortEthSpeed
_CfprEtherServerIntFIoAdminSpeed_Object = MibTableColumn
cfprEtherServerIntFIoAdminSpeed = _CfprEtherServerIntFIoAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 4),
    _CfprEtherServerIntFIoAdminSpeed_Type()
)
cfprEtherServerIntFIoAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoAdminSpeed.setStatus("current")
_CfprEtherServerIntFIoAdminState_Type = CfprEtherServerIntFIoAdminState
_CfprEtherServerIntFIoAdminState_Object = MibTableColumn
cfprEtherServerIntFIoAdminState = _CfprEtherServerIntFIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 5),
    _CfprEtherServerIntFIoAdminState_Type()
)
cfprEtherServerIntFIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoAdminState.setStatus("current")
_CfprEtherServerIntFIoAggrPortId_Type = Gauge32
_CfprEtherServerIntFIoAggrPortId_Object = MibTableColumn
cfprEtherServerIntFIoAggrPortId = _CfprEtherServerIntFIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 6),
    _CfprEtherServerIntFIoAggrPortId_Type()
)
cfprEtherServerIntFIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoAggrPortId.setStatus("current")
_CfprEtherServerIntFIoChassisId_Type = Gauge32
_CfprEtherServerIntFIoChassisId_Object = MibTableColumn
cfprEtherServerIntFIoChassisId = _CfprEtherServerIntFIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 7),
    _CfprEtherServerIntFIoChassisId_Type()
)
cfprEtherServerIntFIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoChassisId.setStatus("current")
_CfprEtherServerIntFIoEncap_Type = CfprPortEncap
_CfprEtherServerIntFIoEncap_Object = MibTableColumn
cfprEtherServerIntFIoEncap = _CfprEtherServerIntFIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 8),
    _CfprEtherServerIntFIoEncap_Type()
)
cfprEtherServerIntFIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoEncap.setStatus("current")
_CfprEtherServerIntFIoEpDn_Type = SnmpAdminString
_CfprEtherServerIntFIoEpDn_Object = MibTableColumn
cfprEtherServerIntFIoEpDn = _CfprEtherServerIntFIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 9),
    _CfprEtherServerIntFIoEpDn_Type()
)
cfprEtherServerIntFIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoEpDn.setStatus("current")
_CfprEtherServerIntFIoFltAggr_Type = Unsigned64
_CfprEtherServerIntFIoFltAggr_Object = MibTableColumn
cfprEtherServerIntFIoFltAggr = _CfprEtherServerIntFIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 10),
    _CfprEtherServerIntFIoFltAggr_Type()
)
cfprEtherServerIntFIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFltAggr.setStatus("current")
_CfprEtherServerIntFIoFsmDescr_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmDescr_Object = MibTableColumn
cfprEtherServerIntFIoFsmDescr = _CfprEtherServerIntFIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 11),
    _CfprEtherServerIntFIoFsmDescr_Type()
)
cfprEtherServerIntFIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmDescr.setStatus("current")
_CfprEtherServerIntFIoFsmPrev_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmPrev_Object = MibTableColumn
cfprEtherServerIntFIoFsmPrev = _CfprEtherServerIntFIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 12),
    _CfprEtherServerIntFIoFsmPrev_Type()
)
cfprEtherServerIntFIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmPrev.setStatus("current")
_CfprEtherServerIntFIoFsmProgr_Type = Gauge32
_CfprEtherServerIntFIoFsmProgr_Object = MibTableColumn
cfprEtherServerIntFIoFsmProgr = _CfprEtherServerIntFIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 13),
    _CfprEtherServerIntFIoFsmProgr_Type()
)
cfprEtherServerIntFIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmProgr.setStatus("current")
_CfprEtherServerIntFIoFsmRmtInvErrCode_Type = Gauge32
_CfprEtherServerIntFIoFsmRmtInvErrCode_Object = MibTableColumn
cfprEtherServerIntFIoFsmRmtInvErrCode = _CfprEtherServerIntFIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 14),
    _CfprEtherServerIntFIoFsmRmtInvErrCode_Type()
)
cfprEtherServerIntFIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRmtInvErrCode.setStatus("current")
_CfprEtherServerIntFIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmRmtInvErrDescr_Object = MibTableColumn
cfprEtherServerIntFIoFsmRmtInvErrDescr = _CfprEtherServerIntFIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 15),
    _CfprEtherServerIntFIoFsmRmtInvErrDescr_Type()
)
cfprEtherServerIntFIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRmtInvErrDescr.setStatus("current")
_CfprEtherServerIntFIoFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprEtherServerIntFIoFsmRmtInvRslt_Object = MibTableColumn
cfprEtherServerIntFIoFsmRmtInvRslt = _CfprEtherServerIntFIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 16),
    _CfprEtherServerIntFIoFsmRmtInvRslt_Type()
)
cfprEtherServerIntFIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRmtInvRslt.setStatus("current")
_CfprEtherServerIntFIoFsmStageDescr_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmStageDescr_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageDescr = _CfprEtherServerIntFIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 17),
    _CfprEtherServerIntFIoFsmStageDescr_Type()
)
cfprEtherServerIntFIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageDescr.setStatus("current")
_CfprEtherServerIntFIoFsmStamp_Type = DateAndTime
_CfprEtherServerIntFIoFsmStamp_Object = MibTableColumn
cfprEtherServerIntFIoFsmStamp = _CfprEtherServerIntFIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 18),
    _CfprEtherServerIntFIoFsmStamp_Type()
)
cfprEtherServerIntFIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStamp.setStatus("current")
_CfprEtherServerIntFIoFsmStatus_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmStatus_Object = MibTableColumn
cfprEtherServerIntFIoFsmStatus = _CfprEtherServerIntFIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 19),
    _CfprEtherServerIntFIoFsmStatus_Type()
)
cfprEtherServerIntFIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStatus.setStatus("current")
_CfprEtherServerIntFIoFsmTry_Type = Gauge32
_CfprEtherServerIntFIoFsmTry_Object = MibTableColumn
cfprEtherServerIntFIoFsmTry = _CfprEtherServerIntFIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 20),
    _CfprEtherServerIntFIoFsmTry_Type()
)
cfprEtherServerIntFIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTry.setStatus("current")
_CfprEtherServerIntFIoIfRole_Type = CfprEtherServerIntFIoIfRole
_CfprEtherServerIntFIoIfRole_Object = MibTableColumn
cfprEtherServerIntFIoIfRole = _CfprEtherServerIntFIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 21),
    _CfprEtherServerIntFIoIfRole_Type()
)
cfprEtherServerIntFIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoIfRole.setStatus("current")
_CfprEtherServerIntFIoIfType_Type = CfprNetworkPhysEpIfType
_CfprEtherServerIntFIoIfType_Object = MibTableColumn
cfprEtherServerIntFIoIfType = _CfprEtherServerIntFIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 22),
    _CfprEtherServerIntFIoIfType_Type()
)
cfprEtherServerIntFIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoIfType.setStatus("current")
_CfprEtherServerIntFIoLocale_Type = CfprEtherServerIntFIoLocale
_CfprEtherServerIntFIoLocale_Object = MibTableColumn
cfprEtherServerIntFIoLocale = _CfprEtherServerIntFIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 23),
    _CfprEtherServerIntFIoLocale_Type()
)
cfprEtherServerIntFIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoLocale.setStatus("current")
_CfprEtherServerIntFIoMac_Type = MacAddress
_CfprEtherServerIntFIoMac_Object = MibTableColumn
cfprEtherServerIntFIoMac = _CfprEtherServerIntFIoMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 24),
    _CfprEtherServerIntFIoMac_Type()
)
cfprEtherServerIntFIoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoMac.setStatus("current")
_CfprEtherServerIntFIoMode_Type = CfprPortMode
_CfprEtherServerIntFIoMode_Object = MibTableColumn
cfprEtherServerIntFIoMode = _CfprEtherServerIntFIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 25),
    _CfprEtherServerIntFIoMode_Type()
)
cfprEtherServerIntFIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoMode.setStatus("current")
_CfprEtherServerIntFIoModel_Type = SnmpAdminString
_CfprEtherServerIntFIoModel_Object = MibTableColumn
cfprEtherServerIntFIoModel = _CfprEtherServerIntFIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 26),
    _CfprEtherServerIntFIoModel_Type()
)
cfprEtherServerIntFIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoModel.setStatus("current")
_CfprEtherServerIntFIoName_Type = SnmpAdminString
_CfprEtherServerIntFIoName_Object = MibTableColumn
cfprEtherServerIntFIoName = _CfprEtherServerIntFIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 27),
    _CfprEtherServerIntFIoName_Type()
)
cfprEtherServerIntFIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoName.setStatus("current")
_CfprEtherServerIntFIoNsSize_Type = Gauge32
_CfprEtherServerIntFIoNsSize_Object = MibTableColumn
cfprEtherServerIntFIoNsSize = _CfprEtherServerIntFIoNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 28),
    _CfprEtherServerIntFIoNsSize_Type()
)
cfprEtherServerIntFIoNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoNsSize.setStatus("current")
_CfprEtherServerIntFIoOperBorderAggrPortId_Type = Gauge32
_CfprEtherServerIntFIoOperBorderAggrPortId_Object = MibTableColumn
cfprEtherServerIntFIoOperBorderAggrPortId = _CfprEtherServerIntFIoOperBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 29),
    _CfprEtherServerIntFIoOperBorderAggrPortId_Type()
)
cfprEtherServerIntFIoOperBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoOperBorderAggrPortId.setStatus("current")
_CfprEtherServerIntFIoOperBorderPortId_Type = Gauge32
_CfprEtherServerIntFIoOperBorderPortId_Object = MibTableColumn
cfprEtherServerIntFIoOperBorderPortId = _CfprEtherServerIntFIoOperBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 30),
    _CfprEtherServerIntFIoOperBorderPortId_Type()
)
cfprEtherServerIntFIoOperBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoOperBorderPortId.setStatus("current")
_CfprEtherServerIntFIoOperBorderSlotId_Type = Gauge32
_CfprEtherServerIntFIoOperBorderSlotId_Object = MibTableColumn
cfprEtherServerIntFIoOperBorderSlotId = _CfprEtherServerIntFIoOperBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 31),
    _CfprEtherServerIntFIoOperBorderSlotId_Type()
)
cfprEtherServerIntFIoOperBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoOperBorderSlotId.setStatus("current")
_CfprEtherServerIntFIoOperState_Type = CfprNetworkPortOperState
_CfprEtherServerIntFIoOperState_Object = MibTableColumn
cfprEtherServerIntFIoOperState = _CfprEtherServerIntFIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 32),
    _CfprEtherServerIntFIoOperState_Type()
)
cfprEtherServerIntFIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoOperState.setStatus("current")
_CfprEtherServerIntFIoPeerAggrPortId_Type = Gauge32
_CfprEtherServerIntFIoPeerAggrPortId_Object = MibTableColumn
cfprEtherServerIntFIoPeerAggrPortId = _CfprEtherServerIntFIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 33),
    _CfprEtherServerIntFIoPeerAggrPortId_Type()
)
cfprEtherServerIntFIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPeerAggrPortId.setStatus("current")
_CfprEtherServerIntFIoPeerChassisId_Type = Gauge32
_CfprEtherServerIntFIoPeerChassisId_Object = MibTableColumn
cfprEtherServerIntFIoPeerChassisId = _CfprEtherServerIntFIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 34),
    _CfprEtherServerIntFIoPeerChassisId_Type()
)
cfprEtherServerIntFIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPeerChassisId.setStatus("current")
_CfprEtherServerIntFIoPeerDn_Type = SnmpAdminString
_CfprEtherServerIntFIoPeerDn_Object = MibTableColumn
cfprEtherServerIntFIoPeerDn = _CfprEtherServerIntFIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 35),
    _CfprEtherServerIntFIoPeerDn_Type()
)
cfprEtherServerIntFIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPeerDn.setStatus("current")
_CfprEtherServerIntFIoPeerEncap_Type = Gauge32
_CfprEtherServerIntFIoPeerEncap_Object = MibTableColumn
cfprEtherServerIntFIoPeerEncap = _CfprEtherServerIntFIoPeerEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 36),
    _CfprEtherServerIntFIoPeerEncap_Type()
)
cfprEtherServerIntFIoPeerEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPeerEncap.setStatus("current")
_CfprEtherServerIntFIoPeerPortId_Type = Gauge32
_CfprEtherServerIntFIoPeerPortId_Object = MibTableColumn
cfprEtherServerIntFIoPeerPortId = _CfprEtherServerIntFIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 37),
    _CfprEtherServerIntFIoPeerPortId_Type()
)
cfprEtherServerIntFIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPeerPortId.setStatus("current")
_CfprEtherServerIntFIoPeerSlotId_Type = Gauge32
_CfprEtherServerIntFIoPeerSlotId_Object = MibTableColumn
cfprEtherServerIntFIoPeerSlotId = _CfprEtherServerIntFIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 38),
    _CfprEtherServerIntFIoPeerSlotId_Type()
)
cfprEtherServerIntFIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPeerSlotId.setStatus("current")
_CfprEtherServerIntFIoPortId_Type = Gauge32
_CfprEtherServerIntFIoPortId_Object = MibTableColumn
cfprEtherServerIntFIoPortId = _CfprEtherServerIntFIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 39),
    _CfprEtherServerIntFIoPortId_Type()
)
cfprEtherServerIntFIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPortId.setStatus("current")
_CfprEtherServerIntFIoRevision_Type = SnmpAdminString
_CfprEtherServerIntFIoRevision_Object = MibTableColumn
cfprEtherServerIntFIoRevision = _CfprEtherServerIntFIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 40),
    _CfprEtherServerIntFIoRevision_Type()
)
cfprEtherServerIntFIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoRevision.setStatus("current")
_CfprEtherServerIntFIoSerial_Type = SnmpAdminString
_CfprEtherServerIntFIoSerial_Object = MibTableColumn
cfprEtherServerIntFIoSerial = _CfprEtherServerIntFIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 41),
    _CfprEtherServerIntFIoSerial_Type()
)
cfprEtherServerIntFIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoSerial.setStatus("current")
_CfprEtherServerIntFIoSlotId_Type = Gauge32
_CfprEtherServerIntFIoSlotId_Object = MibTableColumn
cfprEtherServerIntFIoSlotId = _CfprEtherServerIntFIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 42),
    _CfprEtherServerIntFIoSlotId_Type()
)
cfprEtherServerIntFIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoSlotId.setStatus("current")
_CfprEtherServerIntFIoStateQual_Type = SnmpAdminString
_CfprEtherServerIntFIoStateQual_Object = MibTableColumn
cfprEtherServerIntFIoStateQual = _CfprEtherServerIntFIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 43),
    _CfprEtherServerIntFIoStateQual_Type()
)
cfprEtherServerIntFIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoStateQual.setStatus("current")
_CfprEtherServerIntFIoSwitchId_Type = CfprNetworkSwitchId
_CfprEtherServerIntFIoSwitchId_Object = MibTableColumn
cfprEtherServerIntFIoSwitchId = _CfprEtherServerIntFIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 44),
    _CfprEtherServerIntFIoSwitchId_Type()
)
cfprEtherServerIntFIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoSwitchId.setStatus("current")
_CfprEtherServerIntFIoTransport_Type = CfprEtherServerIntFIoTransport
_CfprEtherServerIntFIoTransport_Object = MibTableColumn
cfprEtherServerIntFIoTransport = _CfprEtherServerIntFIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 45),
    _CfprEtherServerIntFIoTransport_Type()
)
cfprEtherServerIntFIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoTransport.setStatus("current")
_CfprEtherServerIntFIoTs_Type = DateAndTime
_CfprEtherServerIntFIoTs_Object = MibTableColumn
cfprEtherServerIntFIoTs = _CfprEtherServerIntFIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 46),
    _CfprEtherServerIntFIoTs_Type()
)
cfprEtherServerIntFIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoTs.setStatus("current")
_CfprEtherServerIntFIoType_Type = CfprEtherServerIntFIoType
_CfprEtherServerIntFIoType_Object = MibTableColumn
cfprEtherServerIntFIoType = _CfprEtherServerIntFIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 47),
    _CfprEtherServerIntFIoType_Type()
)
cfprEtherServerIntFIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoType.setStatus("current")
_CfprEtherServerIntFIoVendor_Type = SnmpAdminString
_CfprEtherServerIntFIoVendor_Object = MibTableColumn
cfprEtherServerIntFIoVendor = _CfprEtherServerIntFIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 48),
    _CfprEtherServerIntFIoVendor_Type()
)
cfprEtherServerIntFIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoVendor.setStatus("current")
_CfprEtherServerIntFIoXcvrType_Type = CfprEquipmentXcvrType
_CfprEtherServerIntFIoXcvrType_Object = MibTableColumn
cfprEtherServerIntFIoXcvrType = _CfprEtherServerIntFIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 20, 1, 49),
    _CfprEtherServerIntFIoXcvrType_Type()
)
cfprEtherServerIntFIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoXcvrType.setStatus("current")
_CfprEtherServerIntFIoFsmTable_Object = MibTable
cfprEtherServerIntFIoFsmTable = _CfprEtherServerIntFIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21)
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTable.setStatus("current")
_CfprEtherServerIntFIoFsmEntry_Object = MibTableRow
cfprEtherServerIntFIoFsmEntry = _CfprEtherServerIntFIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1)
)
cfprEtherServerIntFIoFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherServerIntFIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmEntry.setStatus("current")
_CfprEtherServerIntFIoFsmInstanceId_Type = CfprManagedObjectId
_CfprEtherServerIntFIoFsmInstanceId_Object = MibTableColumn
cfprEtherServerIntFIoFsmInstanceId = _CfprEtherServerIntFIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 1),
    _CfprEtherServerIntFIoFsmInstanceId_Type()
)
cfprEtherServerIntFIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmInstanceId.setStatus("current")
_CfprEtherServerIntFIoFsmDn_Type = CfprManagedObjectDn
_CfprEtherServerIntFIoFsmDn_Object = MibTableColumn
cfprEtherServerIntFIoFsmDn = _CfprEtherServerIntFIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 2),
    _CfprEtherServerIntFIoFsmDn_Type()
)
cfprEtherServerIntFIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmDn.setStatus("current")
_CfprEtherServerIntFIoFsmRn_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmRn_Object = MibTableColumn
cfprEtherServerIntFIoFsmRn = _CfprEtherServerIntFIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 3),
    _CfprEtherServerIntFIoFsmRn_Type()
)
cfprEtherServerIntFIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRn.setStatus("current")
_CfprEtherServerIntFIoFsmCompletionTime_Type = DateAndTime
_CfprEtherServerIntFIoFsmCompletionTime_Object = MibTableColumn
cfprEtherServerIntFIoFsmCompletionTime = _CfprEtherServerIntFIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 4),
    _CfprEtherServerIntFIoFsmCompletionTime_Type()
)
cfprEtherServerIntFIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmCompletionTime.setStatus("current")
_CfprEtherServerIntFIoFsmCurrentFsm_Type = CfprEtherServerIntFIoFsmCurrentFsm
_CfprEtherServerIntFIoFsmCurrentFsm_Object = MibTableColumn
cfprEtherServerIntFIoFsmCurrentFsm = _CfprEtherServerIntFIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 5),
    _CfprEtherServerIntFIoFsmCurrentFsm_Type()
)
cfprEtherServerIntFIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmCurrentFsm.setStatus("current")
_CfprEtherServerIntFIoFsmDescrData_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmDescrData_Object = MibTableColumn
cfprEtherServerIntFIoFsmDescrData = _CfprEtherServerIntFIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 6),
    _CfprEtherServerIntFIoFsmDescrData_Type()
)
cfprEtherServerIntFIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmDescrData.setStatus("current")
_CfprEtherServerIntFIoFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprEtherServerIntFIoFsmFsmStatus_Object = MibTableColumn
cfprEtherServerIntFIoFsmFsmStatus = _CfprEtherServerIntFIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 7),
    _CfprEtherServerIntFIoFsmFsmStatus_Type()
)
cfprEtherServerIntFIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmFsmStatus.setStatus("current")
_CfprEtherServerIntFIoFsmProgress_Type = Gauge32
_CfprEtherServerIntFIoFsmProgress_Object = MibTableColumn
cfprEtherServerIntFIoFsmProgress = _CfprEtherServerIntFIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 8),
    _CfprEtherServerIntFIoFsmProgress_Type()
)
cfprEtherServerIntFIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmProgress.setStatus("current")
_CfprEtherServerIntFIoFsmRmtErrCode_Type = Gauge32
_CfprEtherServerIntFIoFsmRmtErrCode_Object = MibTableColumn
cfprEtherServerIntFIoFsmRmtErrCode = _CfprEtherServerIntFIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 9),
    _CfprEtherServerIntFIoFsmRmtErrCode_Type()
)
cfprEtherServerIntFIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRmtErrCode.setStatus("current")
_CfprEtherServerIntFIoFsmRmtErrDescr_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmRmtErrDescr_Object = MibTableColumn
cfprEtherServerIntFIoFsmRmtErrDescr = _CfprEtherServerIntFIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 10),
    _CfprEtherServerIntFIoFsmRmtErrDescr_Type()
)
cfprEtherServerIntFIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRmtErrDescr.setStatus("current")
_CfprEtherServerIntFIoFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprEtherServerIntFIoFsmRmtRslt_Object = MibTableColumn
cfprEtherServerIntFIoFsmRmtRslt = _CfprEtherServerIntFIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 21, 1, 11),
    _CfprEtherServerIntFIoFsmRmtRslt_Type()
)
cfprEtherServerIntFIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmRmtRslt.setStatus("current")
_CfprEtherServerIntFIoFsmStageTable_Object = MibTable
cfprEtherServerIntFIoFsmStageTable = _CfprEtherServerIntFIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22)
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageTable.setStatus("current")
_CfprEtherServerIntFIoFsmStageEntry_Object = MibTableRow
cfprEtherServerIntFIoFsmStageEntry = _CfprEtherServerIntFIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1)
)
cfprEtherServerIntFIoFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherServerIntFIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageEntry.setStatus("current")
_CfprEtherServerIntFIoFsmStageInstanceId_Type = CfprManagedObjectId
_CfprEtherServerIntFIoFsmStageInstanceId_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageInstanceId = _CfprEtherServerIntFIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 1),
    _CfprEtherServerIntFIoFsmStageInstanceId_Type()
)
cfprEtherServerIntFIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageInstanceId.setStatus("current")
_CfprEtherServerIntFIoFsmStageDn_Type = CfprManagedObjectDn
_CfprEtherServerIntFIoFsmStageDn_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageDn = _CfprEtherServerIntFIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 2),
    _CfprEtherServerIntFIoFsmStageDn_Type()
)
cfprEtherServerIntFIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageDn.setStatus("current")
_CfprEtherServerIntFIoFsmStageRn_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmStageRn_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageRn = _CfprEtherServerIntFIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 3),
    _CfprEtherServerIntFIoFsmStageRn_Type()
)
cfprEtherServerIntFIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageRn.setStatus("current")
_CfprEtherServerIntFIoFsmStageDescrData_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmStageDescrData_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageDescrData = _CfprEtherServerIntFIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 4),
    _CfprEtherServerIntFIoFsmStageDescrData_Type()
)
cfprEtherServerIntFIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageDescrData.setStatus("current")
_CfprEtherServerIntFIoFsmStageLastUpdateTime_Type = DateAndTime
_CfprEtherServerIntFIoFsmStageLastUpdateTime_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageLastUpdateTime = _CfprEtherServerIntFIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 5),
    _CfprEtherServerIntFIoFsmStageLastUpdateTime_Type()
)
cfprEtherServerIntFIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageLastUpdateTime.setStatus("current")
_CfprEtherServerIntFIoFsmStageName_Type = CfprEtherServerIntFIoFsmStageName
_CfprEtherServerIntFIoFsmStageName_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageName = _CfprEtherServerIntFIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 6),
    _CfprEtherServerIntFIoFsmStageName_Type()
)
cfprEtherServerIntFIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageName.setStatus("current")
_CfprEtherServerIntFIoFsmStageOrder_Type = Gauge32
_CfprEtherServerIntFIoFsmStageOrder_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageOrder = _CfprEtherServerIntFIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 7),
    _CfprEtherServerIntFIoFsmStageOrder_Type()
)
cfprEtherServerIntFIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageOrder.setStatus("current")
_CfprEtherServerIntFIoFsmStageRetry_Type = Gauge32
_CfprEtherServerIntFIoFsmStageRetry_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageRetry = _CfprEtherServerIntFIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 8),
    _CfprEtherServerIntFIoFsmStageRetry_Type()
)
cfprEtherServerIntFIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageRetry.setStatus("current")
_CfprEtherServerIntFIoFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprEtherServerIntFIoFsmStageStageStatus_Object = MibTableColumn
cfprEtherServerIntFIoFsmStageStageStatus = _CfprEtherServerIntFIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 22, 1, 9),
    _CfprEtherServerIntFIoFsmStageStageStatus_Type()
)
cfprEtherServerIntFIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmStageStageStatus.setStatus("current")
_CfprEtherServerIntFIoFsmTaskTable_Object = MibTable
cfprEtherServerIntFIoFsmTaskTable = _CfprEtherServerIntFIoFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23)
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskTable.setStatus("current")
_CfprEtherServerIntFIoFsmTaskEntry_Object = MibTableRow
cfprEtherServerIntFIoFsmTaskEntry = _CfprEtherServerIntFIoFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1)
)
cfprEtherServerIntFIoFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherServerIntFIoFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskEntry.setStatus("current")
_CfprEtherServerIntFIoFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprEtherServerIntFIoFsmTaskInstanceId_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskInstanceId = _CfprEtherServerIntFIoFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 1),
    _CfprEtherServerIntFIoFsmTaskInstanceId_Type()
)
cfprEtherServerIntFIoFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskInstanceId.setStatus("current")
_CfprEtherServerIntFIoFsmTaskDn_Type = CfprManagedObjectDn
_CfprEtherServerIntFIoFsmTaskDn_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskDn = _CfprEtherServerIntFIoFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 2),
    _CfprEtherServerIntFIoFsmTaskDn_Type()
)
cfprEtherServerIntFIoFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskDn.setStatus("current")
_CfprEtherServerIntFIoFsmTaskRn_Type = SnmpAdminString
_CfprEtherServerIntFIoFsmTaskRn_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskRn = _CfprEtherServerIntFIoFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 3),
    _CfprEtherServerIntFIoFsmTaskRn_Type()
)
cfprEtherServerIntFIoFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskRn.setStatus("current")
_CfprEtherServerIntFIoFsmTaskCompletion_Type = CfprFsmCompletion
_CfprEtherServerIntFIoFsmTaskCompletion_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskCompletion = _CfprEtherServerIntFIoFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 4),
    _CfprEtherServerIntFIoFsmTaskCompletion_Type()
)
cfprEtherServerIntFIoFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskCompletion.setStatus("current")
_CfprEtherServerIntFIoFsmTaskFlags_Type = CfprFsmFlags
_CfprEtherServerIntFIoFsmTaskFlags_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskFlags = _CfprEtherServerIntFIoFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 5),
    _CfprEtherServerIntFIoFsmTaskFlags_Type()
)
cfprEtherServerIntFIoFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskFlags.setStatus("current")
_CfprEtherServerIntFIoFsmTaskItem_Type = CfprEtherServerIntFIoFsmTaskItem
_CfprEtherServerIntFIoFsmTaskItem_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskItem = _CfprEtherServerIntFIoFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 6),
    _CfprEtherServerIntFIoFsmTaskItem_Type()
)
cfprEtherServerIntFIoFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskItem.setStatus("current")
_CfprEtherServerIntFIoFsmTaskSeqId_Type = Gauge32
_CfprEtherServerIntFIoFsmTaskSeqId_Object = MibTableColumn
cfprEtherServerIntFIoFsmTaskSeqId = _CfprEtherServerIntFIoFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 23, 1, 7),
    _CfprEtherServerIntFIoFsmTaskSeqId_Type()
)
cfprEtherServerIntFIoFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoFsmTaskSeqId.setStatus("current")
_CfprEtherServerIntFIoPcTable_Object = MibTable
cfprEtherServerIntFIoPcTable = _CfprEtherServerIntFIoPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24)
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcTable.setStatus("current")
_CfprEtherServerIntFIoPcEntry_Object = MibTableRow
cfprEtherServerIntFIoPcEntry = _CfprEtherServerIntFIoPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1)
)
cfprEtherServerIntFIoPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherServerIntFIoPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEntry.setStatus("current")
_CfprEtherServerIntFIoPcInstanceId_Type = CfprManagedObjectId
_CfprEtherServerIntFIoPcInstanceId_Object = MibTableColumn
cfprEtherServerIntFIoPcInstanceId = _CfprEtherServerIntFIoPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 1),
    _CfprEtherServerIntFIoPcInstanceId_Type()
)
cfprEtherServerIntFIoPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcInstanceId.setStatus("current")
_CfprEtherServerIntFIoPcDn_Type = CfprManagedObjectDn
_CfprEtherServerIntFIoPcDn_Object = MibTableColumn
cfprEtherServerIntFIoPcDn = _CfprEtherServerIntFIoPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 2),
    _CfprEtherServerIntFIoPcDn_Type()
)
cfprEtherServerIntFIoPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcDn.setStatus("current")
_CfprEtherServerIntFIoPcRn_Type = SnmpAdminString
_CfprEtherServerIntFIoPcRn_Object = MibTableColumn
cfprEtherServerIntFIoPcRn = _CfprEtherServerIntFIoPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 3),
    _CfprEtherServerIntFIoPcRn_Type()
)
cfprEtherServerIntFIoPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcRn.setStatus("current")
_CfprEtherServerIntFIoPcChassisId_Type = Gauge32
_CfprEtherServerIntFIoPcChassisId_Object = MibTableColumn
cfprEtherServerIntFIoPcChassisId = _CfprEtherServerIntFIoPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 4),
    _CfprEtherServerIntFIoPcChassisId_Type()
)
cfprEtherServerIntFIoPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcChassisId.setStatus("current")
_CfprEtherServerIntFIoPcEpDn_Type = SnmpAdminString
_CfprEtherServerIntFIoPcEpDn_Object = MibTableColumn
cfprEtherServerIntFIoPcEpDn = _CfprEtherServerIntFIoPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 5),
    _CfprEtherServerIntFIoPcEpDn_Type()
)
cfprEtherServerIntFIoPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpDn.setStatus("current")
_CfprEtherServerIntFIoPcFltAggr_Type = Unsigned64
_CfprEtherServerIntFIoPcFltAggr_Object = MibTableColumn
cfprEtherServerIntFIoPcFltAggr = _CfprEtherServerIntFIoPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 6),
    _CfprEtherServerIntFIoPcFltAggr_Type()
)
cfprEtherServerIntFIoPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcFltAggr.setStatus("current")
_CfprEtherServerIntFIoPcIfRole_Type = CfprEtherServerIntFIoPcIfRole
_CfprEtherServerIntFIoPcIfRole_Object = MibTableColumn
cfprEtherServerIntFIoPcIfRole = _CfprEtherServerIntFIoPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 7),
    _CfprEtherServerIntFIoPcIfRole_Type()
)
cfprEtherServerIntFIoPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcIfRole.setStatus("current")
_CfprEtherServerIntFIoPcIfType_Type = CfprEtherCIoEpIfType
_CfprEtherServerIntFIoPcIfType_Object = MibTableColumn
cfprEtherServerIntFIoPcIfType = _CfprEtherServerIntFIoPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 8),
    _CfprEtherServerIntFIoPcIfType_Type()
)
cfprEtherServerIntFIoPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcIfType.setStatus("current")
_CfprEtherServerIntFIoPcLocale_Type = CfprEtherInternalPcLocale
_CfprEtherServerIntFIoPcLocale_Object = MibTableColumn
cfprEtherServerIntFIoPcLocale = _CfprEtherServerIntFIoPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 9),
    _CfprEtherServerIntFIoPcLocale_Type()
)
cfprEtherServerIntFIoPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcLocale.setStatus("current")
_CfprEtherServerIntFIoPcName_Type = SnmpAdminString
_CfprEtherServerIntFIoPcName_Object = MibTableColumn
cfprEtherServerIntFIoPcName = _CfprEtherServerIntFIoPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 10),
    _CfprEtherServerIntFIoPcName_Type()
)
cfprEtherServerIntFIoPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcName.setStatus("current")
_CfprEtherServerIntFIoPcOperSpeed_Type = CfprPortEthSpeed
_CfprEtherServerIntFIoPcOperSpeed_Object = MibTableColumn
cfprEtherServerIntFIoPcOperSpeed = _CfprEtherServerIntFIoPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 11),
    _CfprEtherServerIntFIoPcOperSpeed_Type()
)
cfprEtherServerIntFIoPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcOperSpeed.setStatus("current")
_CfprEtherServerIntFIoPcOperState_Type = CfprNetworkPortOperState
_CfprEtherServerIntFIoPcOperState_Object = MibTableColumn
cfprEtherServerIntFIoPcOperState = _CfprEtherServerIntFIoPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 12),
    _CfprEtherServerIntFIoPcOperState_Type()
)
cfprEtherServerIntFIoPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcOperState.setStatus("current")
_CfprEtherServerIntFIoPcPeerDn_Type = SnmpAdminString
_CfprEtherServerIntFIoPcPeerDn_Object = MibTableColumn
cfprEtherServerIntFIoPcPeerDn = _CfprEtherServerIntFIoPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 13),
    _CfprEtherServerIntFIoPcPeerDn_Type()
)
cfprEtherServerIntFIoPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcPeerDn.setStatus("current")
_CfprEtherServerIntFIoPcPortId_Type = CfprEtherServerIntFIoPcPortId
_CfprEtherServerIntFIoPcPortId_Object = MibTableColumn
cfprEtherServerIntFIoPcPortId = _CfprEtherServerIntFIoPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 14),
    _CfprEtherServerIntFIoPcPortId_Type()
)
cfprEtherServerIntFIoPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcPortId.setStatus("current")
_CfprEtherServerIntFIoPcStateQual_Type = SnmpAdminString
_CfprEtherServerIntFIoPcStateQual_Object = MibTableColumn
cfprEtherServerIntFIoPcStateQual = _CfprEtherServerIntFIoPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 15),
    _CfprEtherServerIntFIoPcStateQual_Type()
)
cfprEtherServerIntFIoPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcStateQual.setStatus("current")
_CfprEtherServerIntFIoPcSwitchId_Type = CfprNetworkSwitchId
_CfprEtherServerIntFIoPcSwitchId_Object = MibTableColumn
cfprEtherServerIntFIoPcSwitchId = _CfprEtherServerIntFIoPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 16),
    _CfprEtherServerIntFIoPcSwitchId_Type()
)
cfprEtherServerIntFIoPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcSwitchId.setStatus("current")
_CfprEtherServerIntFIoPcTransport_Type = CfprEtherServerIntFIoPcTransport
_CfprEtherServerIntFIoPcTransport_Object = MibTableColumn
cfprEtherServerIntFIoPcTransport = _CfprEtherServerIntFIoPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 17),
    _CfprEtherServerIntFIoPcTransport_Type()
)
cfprEtherServerIntFIoPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcTransport.setStatus("current")
_CfprEtherServerIntFIoPcType_Type = CfprEtherServerIntFIoPcType
_CfprEtherServerIntFIoPcType_Object = MibTableColumn
cfprEtherServerIntFIoPcType = _CfprEtherServerIntFIoPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 24, 1, 18),
    _CfprEtherServerIntFIoPcType_Type()
)
cfprEtherServerIntFIoPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcType.setStatus("current")
_CfprEtherServerIntFIoPcEpTable_Object = MibTable
cfprEtherServerIntFIoPcEpTable = _CfprEtherServerIntFIoPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25)
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpTable.setStatus("current")
_CfprEtherServerIntFIoPcEpEntry_Object = MibTableRow
cfprEtherServerIntFIoPcEpEntry = _CfprEtherServerIntFIoPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1)
)
cfprEtherServerIntFIoPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherServerIntFIoPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpEntry.setStatus("current")
_CfprEtherServerIntFIoPcEpInstanceId_Type = CfprManagedObjectId
_CfprEtherServerIntFIoPcEpInstanceId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpInstanceId = _CfprEtherServerIntFIoPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 1),
    _CfprEtherServerIntFIoPcEpInstanceId_Type()
)
cfprEtherServerIntFIoPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpInstanceId.setStatus("current")
_CfprEtherServerIntFIoPcEpDnData_Type = CfprManagedObjectDn
_CfprEtherServerIntFIoPcEpDnData_Object = MibTableColumn
cfprEtherServerIntFIoPcEpDnData = _CfprEtherServerIntFIoPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 2),
    _CfprEtherServerIntFIoPcEpDnData_Type()
)
cfprEtherServerIntFIoPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpDnData.setStatus("current")
_CfprEtherServerIntFIoPcEpRn_Type = SnmpAdminString
_CfprEtherServerIntFIoPcEpRn_Object = MibTableColumn
cfprEtherServerIntFIoPcEpRn = _CfprEtherServerIntFIoPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 3),
    _CfprEtherServerIntFIoPcEpRn_Type()
)
cfprEtherServerIntFIoPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpRn.setStatus("current")
_CfprEtherServerIntFIoPcEpAdminState_Type = CfprEtherExternalEpAdminState
_CfprEtherServerIntFIoPcEpAdminState_Object = MibTableColumn
cfprEtherServerIntFIoPcEpAdminState = _CfprEtherServerIntFIoPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 4),
    _CfprEtherServerIntFIoPcEpAdminState_Type()
)
cfprEtherServerIntFIoPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpAdminState.setStatus("current")
_CfprEtherServerIntFIoPcEpAggrPortId_Type = Gauge32
_CfprEtherServerIntFIoPcEpAggrPortId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpAggrPortId = _CfprEtherServerIntFIoPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 5),
    _CfprEtherServerIntFIoPcEpAggrPortId_Type()
)
cfprEtherServerIntFIoPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpAggrPortId.setStatus("current")
_CfprEtherServerIntFIoPcEpChassisId_Type = Gauge32
_CfprEtherServerIntFIoPcEpChassisId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpChassisId = _CfprEtherServerIntFIoPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 6),
    _CfprEtherServerIntFIoPcEpChassisId_Type()
)
cfprEtherServerIntFIoPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpChassisId.setStatus("current")
_CfprEtherServerIntFIoPcEpEpDn_Type = SnmpAdminString
_CfprEtherServerIntFIoPcEpEpDn_Object = MibTableColumn
cfprEtherServerIntFIoPcEpEpDn = _CfprEtherServerIntFIoPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 7),
    _CfprEtherServerIntFIoPcEpEpDn_Type()
)
cfprEtherServerIntFIoPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpEpDn.setStatus("current")
_CfprEtherServerIntFIoPcEpIfRole_Type = CfprEtherServerIntFIoPcEpIfRole
_CfprEtherServerIntFIoPcEpIfRole_Object = MibTableColumn
cfprEtherServerIntFIoPcEpIfRole = _CfprEtherServerIntFIoPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 8),
    _CfprEtherServerIntFIoPcEpIfRole_Type()
)
cfprEtherServerIntFIoPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpIfRole.setStatus("current")
_CfprEtherServerIntFIoPcEpIfType_Type = CfprEtherPIoEpIfType
_CfprEtherServerIntFIoPcEpIfType_Object = MibTableColumn
cfprEtherServerIntFIoPcEpIfType = _CfprEtherServerIntFIoPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 9),
    _CfprEtherServerIntFIoPcEpIfType_Type()
)
cfprEtherServerIntFIoPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpIfType.setStatus("current")
_CfprEtherServerIntFIoPcEpLocale_Type = CfprEtherExternalEpLocale
_CfprEtherServerIntFIoPcEpLocale_Object = MibTableColumn
cfprEtherServerIntFIoPcEpLocale = _CfprEtherServerIntFIoPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 10),
    _CfprEtherServerIntFIoPcEpLocale_Type()
)
cfprEtherServerIntFIoPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpLocale.setStatus("current")
_CfprEtherServerIntFIoPcEpMembership_Type = CfprFabricMembershipStatus
_CfprEtherServerIntFIoPcEpMembership_Object = MibTableColumn
cfprEtherServerIntFIoPcEpMembership = _CfprEtherServerIntFIoPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 11),
    _CfprEtherServerIntFIoPcEpMembership_Type()
)
cfprEtherServerIntFIoPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpMembership.setStatus("current")
_CfprEtherServerIntFIoPcEpName_Type = SnmpAdminString
_CfprEtherServerIntFIoPcEpName_Object = MibTableColumn
cfprEtherServerIntFIoPcEpName = _CfprEtherServerIntFIoPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 12),
    _CfprEtherServerIntFIoPcEpName_Type()
)
cfprEtherServerIntFIoPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpName.setStatus("current")
_CfprEtherServerIntFIoPcEpPeerAggrPortId_Type = Gauge32
_CfprEtherServerIntFIoPcEpPeerAggrPortId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpPeerAggrPortId = _CfprEtherServerIntFIoPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 13),
    _CfprEtherServerIntFIoPcEpPeerAggrPortId_Type()
)
cfprEtherServerIntFIoPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpPeerAggrPortId.setStatus("current")
_CfprEtherServerIntFIoPcEpPeerChassisId_Type = Gauge32
_CfprEtherServerIntFIoPcEpPeerChassisId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpPeerChassisId = _CfprEtherServerIntFIoPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 14),
    _CfprEtherServerIntFIoPcEpPeerChassisId_Type()
)
cfprEtherServerIntFIoPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpPeerChassisId.setStatus("current")
_CfprEtherServerIntFIoPcEpPeerDn_Type = SnmpAdminString
_CfprEtherServerIntFIoPcEpPeerDn_Object = MibTableColumn
cfprEtherServerIntFIoPcEpPeerDn = _CfprEtherServerIntFIoPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 15),
    _CfprEtherServerIntFIoPcEpPeerDn_Type()
)
cfprEtherServerIntFIoPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpPeerDn.setStatus("current")
_CfprEtherServerIntFIoPcEpPeerPortId_Type = Gauge32
_CfprEtherServerIntFIoPcEpPeerPortId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpPeerPortId = _CfprEtherServerIntFIoPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 16),
    _CfprEtherServerIntFIoPcEpPeerPortId_Type()
)
cfprEtherServerIntFIoPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpPeerPortId.setStatus("current")
_CfprEtherServerIntFIoPcEpPeerSlotId_Type = Gauge32
_CfprEtherServerIntFIoPcEpPeerSlotId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpPeerSlotId = _CfprEtherServerIntFIoPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 17),
    _CfprEtherServerIntFIoPcEpPeerSlotId_Type()
)
cfprEtherServerIntFIoPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpPeerSlotId.setStatus("current")
_CfprEtherServerIntFIoPcEpPortId_Type = CfprEtherServerIntFIoPcEpPortId
_CfprEtherServerIntFIoPcEpPortId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpPortId = _CfprEtherServerIntFIoPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 18),
    _CfprEtherServerIntFIoPcEpPortId_Type()
)
cfprEtherServerIntFIoPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpPortId.setStatus("current")
_CfprEtherServerIntFIoPcEpSlotId_Type = Gauge32
_CfprEtherServerIntFIoPcEpSlotId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpSlotId = _CfprEtherServerIntFIoPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 19),
    _CfprEtherServerIntFIoPcEpSlotId_Type()
)
cfprEtherServerIntFIoPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpSlotId.setStatus("current")
_CfprEtherServerIntFIoPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprEtherServerIntFIoPcEpSwitchId_Object = MibTableColumn
cfprEtherServerIntFIoPcEpSwitchId = _CfprEtherServerIntFIoPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 20),
    _CfprEtherServerIntFIoPcEpSwitchId_Type()
)
cfprEtherServerIntFIoPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpSwitchId.setStatus("current")
_CfprEtherServerIntFIoPcEpTransport_Type = CfprNetworkTransport
_CfprEtherServerIntFIoPcEpTransport_Object = MibTableColumn
cfprEtherServerIntFIoPcEpTransport = _CfprEtherServerIntFIoPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 21),
    _CfprEtherServerIntFIoPcEpTransport_Type()
)
cfprEtherServerIntFIoPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpTransport.setStatus("current")
_CfprEtherServerIntFIoPcEpType_Type = CfprEtherIntFIoEpType
_CfprEtherServerIntFIoPcEpType_Object = MibTableColumn
cfprEtherServerIntFIoPcEpType = _CfprEtherServerIntFIoPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 25, 1, 22),
    _CfprEtherServerIntFIoPcEpType_Type()
)
cfprEtherServerIntFIoPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherServerIntFIoPcEpType.setStatus("current")
_CfprEtherSwIfConfigTable_Object = MibTable
cfprEtherSwIfConfigTable = _CfprEtherSwIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 26)
)
if mibBuilder.loadTexts:
    cfprEtherSwIfConfigTable.setStatus("current")
_CfprEtherSwIfConfigEntry_Object = MibTableRow
cfprEtherSwIfConfigEntry = _CfprEtherSwIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 26, 1)
)
cfprEtherSwIfConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherSwIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherSwIfConfigEntry.setStatus("current")
_CfprEtherSwIfConfigInstanceId_Type = CfprManagedObjectId
_CfprEtherSwIfConfigInstanceId_Object = MibTableColumn
cfprEtherSwIfConfigInstanceId = _CfprEtherSwIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 26, 1, 1),
    _CfprEtherSwIfConfigInstanceId_Type()
)
cfprEtherSwIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherSwIfConfigInstanceId.setStatus("current")
_CfprEtherSwIfConfigDn_Type = CfprManagedObjectDn
_CfprEtherSwIfConfigDn_Object = MibTableColumn
cfprEtherSwIfConfigDn = _CfprEtherSwIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 26, 1, 2),
    _CfprEtherSwIfConfigDn_Type()
)
cfprEtherSwIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwIfConfigDn.setStatus("current")
_CfprEtherSwIfConfigRn_Type = SnmpAdminString
_CfprEtherSwIfConfigRn_Object = MibTableColumn
cfprEtherSwIfConfigRn = _CfprEtherSwIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 26, 1, 3),
    _CfprEtherSwIfConfigRn_Type()
)
cfprEtherSwIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwIfConfigRn.setStatus("current")
_CfprEtherSwitchIntFIoTable_Object = MibTable
cfprEtherSwitchIntFIoTable = _CfprEtherSwitchIntFIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27)
)
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoTable.setStatus("current")
_CfprEtherSwitchIntFIoEntry_Object = MibTableRow
cfprEtherSwitchIntFIoEntry = _CfprEtherSwitchIntFIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1)
)
cfprEtherSwitchIntFIoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherSwitchIntFIoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoEntry.setStatus("current")
_CfprEtherSwitchIntFIoInstanceId_Type = CfprManagedObjectId
_CfprEtherSwitchIntFIoInstanceId_Object = MibTableColumn
cfprEtherSwitchIntFIoInstanceId = _CfprEtherSwitchIntFIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 1),
    _CfprEtherSwitchIntFIoInstanceId_Type()
)
cfprEtherSwitchIntFIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoInstanceId.setStatus("current")
_CfprEtherSwitchIntFIoDn_Type = CfprManagedObjectDn
_CfprEtherSwitchIntFIoDn_Object = MibTableColumn
cfprEtherSwitchIntFIoDn = _CfprEtherSwitchIntFIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 2),
    _CfprEtherSwitchIntFIoDn_Type()
)
cfprEtherSwitchIntFIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoDn.setStatus("current")
_CfprEtherSwitchIntFIoRn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoRn_Object = MibTableColumn
cfprEtherSwitchIntFIoRn = _CfprEtherSwitchIntFIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 3),
    _CfprEtherSwitchIntFIoRn_Type()
)
cfprEtherSwitchIntFIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoRn.setStatus("current")
_CfprEtherSwitchIntFIoAck_Type = CfprEtherSwitchIntFIoAck
_CfprEtherSwitchIntFIoAck_Object = MibTableColumn
cfprEtherSwitchIntFIoAck = _CfprEtherSwitchIntFIoAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 4),
    _CfprEtherSwitchIntFIoAck_Type()
)
cfprEtherSwitchIntFIoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoAck.setStatus("current")
_CfprEtherSwitchIntFIoAdminState_Type = CfprFabricAdminState
_CfprEtherSwitchIntFIoAdminState_Object = MibTableColumn
cfprEtherSwitchIntFIoAdminState = _CfprEtherSwitchIntFIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 5),
    _CfprEtherSwitchIntFIoAdminState_Type()
)
cfprEtherSwitchIntFIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoAdminState.setStatus("current")
_CfprEtherSwitchIntFIoAggrPortId_Type = Gauge32
_CfprEtherSwitchIntFIoAggrPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoAggrPortId = _CfprEtherSwitchIntFIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 6),
    _CfprEtherSwitchIntFIoAggrPortId_Type()
)
cfprEtherSwitchIntFIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoAggrPortId.setStatus("current")
_CfprEtherSwitchIntFIoChassisId_Type = Gauge32
_CfprEtherSwitchIntFIoChassisId_Object = MibTableColumn
cfprEtherSwitchIntFIoChassisId = _CfprEtherSwitchIntFIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 7),
    _CfprEtherSwitchIntFIoChassisId_Type()
)
cfprEtherSwitchIntFIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoChassisId.setStatus("current")
_CfprEtherSwitchIntFIoDelFeTs_Type = Unsigned64
_CfprEtherSwitchIntFIoDelFeTs_Object = MibTableColumn
cfprEtherSwitchIntFIoDelFeTs = _CfprEtherSwitchIntFIoDelFeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 8),
    _CfprEtherSwitchIntFIoDelFeTs_Type()
)
cfprEtherSwitchIntFIoDelFeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoDelFeTs.setStatus("current")
_CfprEtherSwitchIntFIoDiscovery_Type = CfprEtherSatelliteConnectionDisc
_CfprEtherSwitchIntFIoDiscovery_Object = MibTableColumn
cfprEtherSwitchIntFIoDiscovery = _CfprEtherSwitchIntFIoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 9),
    _CfprEtherSwitchIntFIoDiscovery_Type()
)
cfprEtherSwitchIntFIoDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoDiscovery.setStatus("current")
_CfprEtherSwitchIntFIoEncap_Type = CfprPortEncap
_CfprEtherSwitchIntFIoEncap_Object = MibTableColumn
cfprEtherSwitchIntFIoEncap = _CfprEtherSwitchIntFIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 10),
    _CfprEtherSwitchIntFIoEncap_Type()
)
cfprEtherSwitchIntFIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoEncap.setStatus("current")
_CfprEtherSwitchIntFIoEpDn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoEpDn_Object = MibTableColumn
cfprEtherSwitchIntFIoEpDn = _CfprEtherSwitchIntFIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 11),
    _CfprEtherSwitchIntFIoEpDn_Type()
)
cfprEtherSwitchIntFIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoEpDn.setStatus("current")
_CfprEtherSwitchIntFIoFltAggr_Type = Unsigned64
_CfprEtherSwitchIntFIoFltAggr_Object = MibTableColumn
cfprEtherSwitchIntFIoFltAggr = _CfprEtherSwitchIntFIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 12),
    _CfprEtherSwitchIntFIoFltAggr_Type()
)
cfprEtherSwitchIntFIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoFltAggr.setStatus("current")
_CfprEtherSwitchIntFIoIfRole_Type = CfprEtherSwitchIntFIoIfRole
_CfprEtherSwitchIntFIoIfRole_Object = MibTableColumn
cfprEtherSwitchIntFIoIfRole = _CfprEtherSwitchIntFIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 13),
    _CfprEtherSwitchIntFIoIfRole_Type()
)
cfprEtherSwitchIntFIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoIfRole.setStatus("current")
_CfprEtherSwitchIntFIoIfType_Type = CfprNetworkPhysEpIfType
_CfprEtherSwitchIntFIoIfType_Object = MibTableColumn
cfprEtherSwitchIntFIoIfType = _CfprEtherSwitchIntFIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 14),
    _CfprEtherSwitchIntFIoIfType_Type()
)
cfprEtherSwitchIntFIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoIfType.setStatus("current")
_CfprEtherSwitchIntFIoLocale_Type = CfprEtherSwitchIntFIoLocale
_CfprEtherSwitchIntFIoLocale_Object = MibTableColumn
cfprEtherSwitchIntFIoLocale = _CfprEtherSwitchIntFIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 15),
    _CfprEtherSwitchIntFIoLocale_Type()
)
cfprEtherSwitchIntFIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoLocale.setStatus("current")
_CfprEtherSwitchIntFIoMode_Type = CfprPortMode
_CfprEtherSwitchIntFIoMode_Object = MibTableColumn
cfprEtherSwitchIntFIoMode = _CfprEtherSwitchIntFIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 16),
    _CfprEtherSwitchIntFIoMode_Type()
)
cfprEtherSwitchIntFIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoMode.setStatus("current")
_CfprEtherSwitchIntFIoModel_Type = SnmpAdminString
_CfprEtherSwitchIntFIoModel_Object = MibTableColumn
cfprEtherSwitchIntFIoModel = _CfprEtherSwitchIntFIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 17),
    _CfprEtherSwitchIntFIoModel_Type()
)
cfprEtherSwitchIntFIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoModel.setStatus("current")
_CfprEtherSwitchIntFIoName_Type = SnmpAdminString
_CfprEtherSwitchIntFIoName_Object = MibTableColumn
cfprEtherSwitchIntFIoName = _CfprEtherSwitchIntFIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 18),
    _CfprEtherSwitchIntFIoName_Type()
)
cfprEtherSwitchIntFIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoName.setStatus("current")
_CfprEtherSwitchIntFIoNewFeTs_Type = Unsigned64
_CfprEtherSwitchIntFIoNewFeTs_Object = MibTableColumn
cfprEtherSwitchIntFIoNewFeTs = _CfprEtherSwitchIntFIoNewFeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 19),
    _CfprEtherSwitchIntFIoNewFeTs_Type()
)
cfprEtherSwitchIntFIoNewFeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoNewFeTs.setStatus("current")
_CfprEtherSwitchIntFIoOperState_Type = CfprNetworkPortOperState
_CfprEtherSwitchIntFIoOperState_Object = MibTableColumn
cfprEtherSwitchIntFIoOperState = _CfprEtherSwitchIntFIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 20),
    _CfprEtherSwitchIntFIoOperState_Type()
)
cfprEtherSwitchIntFIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoOperState.setStatus("current")
_CfprEtherSwitchIntFIoPeerAggrPortId_Type = Gauge32
_CfprEtherSwitchIntFIoPeerAggrPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPeerAggrPortId = _CfprEtherSwitchIntFIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 21),
    _CfprEtherSwitchIntFIoPeerAggrPortId_Type()
)
cfprEtherSwitchIntFIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPeerAggrPortId.setStatus("current")
_CfprEtherSwitchIntFIoPeerChassisId_Type = Gauge32
_CfprEtherSwitchIntFIoPeerChassisId_Object = MibTableColumn
cfprEtherSwitchIntFIoPeerChassisId = _CfprEtherSwitchIntFIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 22),
    _CfprEtherSwitchIntFIoPeerChassisId_Type()
)
cfprEtherSwitchIntFIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPeerChassisId.setStatus("current")
_CfprEtherSwitchIntFIoPeerDn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPeerDn_Object = MibTableColumn
cfprEtherSwitchIntFIoPeerDn = _CfprEtherSwitchIntFIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 23),
    _CfprEtherSwitchIntFIoPeerDn_Type()
)
cfprEtherSwitchIntFIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPeerDn.setStatus("current")
_CfprEtherSwitchIntFIoPeerPortId_Type = Gauge32
_CfprEtherSwitchIntFIoPeerPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPeerPortId = _CfprEtherSwitchIntFIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 24),
    _CfprEtherSwitchIntFIoPeerPortId_Type()
)
cfprEtherSwitchIntFIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPeerPortId.setStatus("current")
_CfprEtherSwitchIntFIoPeerSlotId_Type = Gauge32
_CfprEtherSwitchIntFIoPeerSlotId_Object = MibTableColumn
cfprEtherSwitchIntFIoPeerSlotId = _CfprEtherSwitchIntFIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 25),
    _CfprEtherSwitchIntFIoPeerSlotId_Type()
)
cfprEtherSwitchIntFIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPeerSlotId.setStatus("current")
_CfprEtherSwitchIntFIoPortId_Type = Gauge32
_CfprEtherSwitchIntFIoPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPortId = _CfprEtherSwitchIntFIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 26),
    _CfprEtherSwitchIntFIoPortId_Type()
)
cfprEtherSwitchIntFIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPortId.setStatus("current")
_CfprEtherSwitchIntFIoRevision_Type = SnmpAdminString
_CfprEtherSwitchIntFIoRevision_Object = MibTableColumn
cfprEtherSwitchIntFIoRevision = _CfprEtherSwitchIntFIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 27),
    _CfprEtherSwitchIntFIoRevision_Type()
)
cfprEtherSwitchIntFIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoRevision.setStatus("current")
_CfprEtherSwitchIntFIoSerial_Type = SnmpAdminString
_CfprEtherSwitchIntFIoSerial_Object = MibTableColumn
cfprEtherSwitchIntFIoSerial = _CfprEtherSwitchIntFIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 28),
    _CfprEtherSwitchIntFIoSerial_Type()
)
cfprEtherSwitchIntFIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoSerial.setStatus("current")
_CfprEtherSwitchIntFIoSlotId_Type = Gauge32
_CfprEtherSwitchIntFIoSlotId_Object = MibTableColumn
cfprEtherSwitchIntFIoSlotId = _CfprEtherSwitchIntFIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 29),
    _CfprEtherSwitchIntFIoSlotId_Type()
)
cfprEtherSwitchIntFIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoSlotId.setStatus("current")
_CfprEtherSwitchIntFIoStateQual_Type = SnmpAdminString
_CfprEtherSwitchIntFIoStateQual_Object = MibTableColumn
cfprEtherSwitchIntFIoStateQual = _CfprEtherSwitchIntFIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 30),
    _CfprEtherSwitchIntFIoStateQual_Type()
)
cfprEtherSwitchIntFIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoStateQual.setStatus("current")
_CfprEtherSwitchIntFIoSwitchId_Type = CfprNetworkSwitchId
_CfprEtherSwitchIntFIoSwitchId_Object = MibTableColumn
cfprEtherSwitchIntFIoSwitchId = _CfprEtherSwitchIntFIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 31),
    _CfprEtherSwitchIntFIoSwitchId_Type()
)
cfprEtherSwitchIntFIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoSwitchId.setStatus("current")
_CfprEtherSwitchIntFIoTransport_Type = CfprEtherSwitchIntFIoTransport
_CfprEtherSwitchIntFIoTransport_Object = MibTableColumn
cfprEtherSwitchIntFIoTransport = _CfprEtherSwitchIntFIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 32),
    _CfprEtherSwitchIntFIoTransport_Type()
)
cfprEtherSwitchIntFIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoTransport.setStatus("current")
_CfprEtherSwitchIntFIoTs_Type = DateAndTime
_CfprEtherSwitchIntFIoTs_Object = MibTableColumn
cfprEtherSwitchIntFIoTs = _CfprEtherSwitchIntFIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 33),
    _CfprEtherSwitchIntFIoTs_Type()
)
cfprEtherSwitchIntFIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoTs.setStatus("current")
_CfprEtherSwitchIntFIoType_Type = CfprEtherSwitchIntFIoType
_CfprEtherSwitchIntFIoType_Object = MibTableColumn
cfprEtherSwitchIntFIoType = _CfprEtherSwitchIntFIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 34),
    _CfprEtherSwitchIntFIoType_Type()
)
cfprEtherSwitchIntFIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoType.setStatus("current")
_CfprEtherSwitchIntFIoVendor_Type = SnmpAdminString
_CfprEtherSwitchIntFIoVendor_Object = MibTableColumn
cfprEtherSwitchIntFIoVendor = _CfprEtherSwitchIntFIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 35),
    _CfprEtherSwitchIntFIoVendor_Type()
)
cfprEtherSwitchIntFIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoVendor.setStatus("current")
_CfprEtherSwitchIntFIoXcvrType_Type = CfprEquipmentXcvrType
_CfprEtherSwitchIntFIoXcvrType_Object = MibTableColumn
cfprEtherSwitchIntFIoXcvrType = _CfprEtherSwitchIntFIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 27, 1, 36),
    _CfprEtherSwitchIntFIoXcvrType_Type()
)
cfprEtherSwitchIntFIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoXcvrType.setStatus("current")
_CfprEtherSwitchIntFIoPcTable_Object = MibTable
cfprEtherSwitchIntFIoPcTable = _CfprEtherSwitchIntFIoPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28)
)
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcTable.setStatus("current")
_CfprEtherSwitchIntFIoPcEntry_Object = MibTableRow
cfprEtherSwitchIntFIoPcEntry = _CfprEtherSwitchIntFIoPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1)
)
cfprEtherSwitchIntFIoPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherSwitchIntFIoPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEntry.setStatus("current")
_CfprEtherSwitchIntFIoPcInstanceId_Type = CfprManagedObjectId
_CfprEtherSwitchIntFIoPcInstanceId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcInstanceId = _CfprEtherSwitchIntFIoPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 1),
    _CfprEtherSwitchIntFIoPcInstanceId_Type()
)
cfprEtherSwitchIntFIoPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcInstanceId.setStatus("current")
_CfprEtherSwitchIntFIoPcDn_Type = CfprManagedObjectDn
_CfprEtherSwitchIntFIoPcDn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcDn = _CfprEtherSwitchIntFIoPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 2),
    _CfprEtherSwitchIntFIoPcDn_Type()
)
cfprEtherSwitchIntFIoPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcDn.setStatus("current")
_CfprEtherSwitchIntFIoPcRn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcRn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcRn = _CfprEtherSwitchIntFIoPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 3),
    _CfprEtherSwitchIntFIoPcRn_Type()
)
cfprEtherSwitchIntFIoPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcRn.setStatus("current")
_CfprEtherSwitchIntFIoPcAdminState_Type = CfprEtherExternalPcAdminState
_CfprEtherSwitchIntFIoPcAdminState_Object = MibTableColumn
cfprEtherSwitchIntFIoPcAdminState = _CfprEtherSwitchIntFIoPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 4),
    _CfprEtherSwitchIntFIoPcAdminState_Type()
)
cfprEtherSwitchIntFIoPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcAdminState.setStatus("current")
_CfprEtherSwitchIntFIoPcChassisId_Type = Gauge32
_CfprEtherSwitchIntFIoPcChassisId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcChassisId = _CfprEtherSwitchIntFIoPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 5),
    _CfprEtherSwitchIntFIoPcChassisId_Type()
)
cfprEtherSwitchIntFIoPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcChassisId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpDn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcEpDn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpDn = _CfprEtherSwitchIntFIoPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 6),
    _CfprEtherSwitchIntFIoPcEpDn_Type()
)
cfprEtherSwitchIntFIoPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpDn.setStatus("current")
_CfprEtherSwitchIntFIoPcFltAggr_Type = Unsigned64
_CfprEtherSwitchIntFIoPcFltAggr_Object = MibTableColumn
cfprEtherSwitchIntFIoPcFltAggr = _CfprEtherSwitchIntFIoPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 7),
    _CfprEtherSwitchIntFIoPcFltAggr_Type()
)
cfprEtherSwitchIntFIoPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcFltAggr.setStatus("current")
_CfprEtherSwitchIntFIoPcIfRole_Type = CfprEtherSwitchIntFIoPcIfRole
_CfprEtherSwitchIntFIoPcIfRole_Object = MibTableColumn
cfprEtherSwitchIntFIoPcIfRole = _CfprEtherSwitchIntFIoPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 8),
    _CfprEtherSwitchIntFIoPcIfRole_Type()
)
cfprEtherSwitchIntFIoPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcIfRole.setStatus("current")
_CfprEtherSwitchIntFIoPcIfType_Type = CfprEtherCIoEpIfType
_CfprEtherSwitchIntFIoPcIfType_Object = MibTableColumn
cfprEtherSwitchIntFIoPcIfType = _CfprEtherSwitchIntFIoPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 9),
    _CfprEtherSwitchIntFIoPcIfType_Type()
)
cfprEtherSwitchIntFIoPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcIfType.setStatus("current")
_CfprEtherSwitchIntFIoPcLocale_Type = CfprEtherExternalPcLocale
_CfprEtherSwitchIntFIoPcLocale_Object = MibTableColumn
cfprEtherSwitchIntFIoPcLocale = _CfprEtherSwitchIntFIoPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 10),
    _CfprEtherSwitchIntFIoPcLocale_Type()
)
cfprEtherSwitchIntFIoPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcLocale.setStatus("current")
_CfprEtherSwitchIntFIoPcName_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcName_Object = MibTableColumn
cfprEtherSwitchIntFIoPcName = _CfprEtherSwitchIntFIoPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 11),
    _CfprEtherSwitchIntFIoPcName_Type()
)
cfprEtherSwitchIntFIoPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcName.setStatus("current")
_CfprEtherSwitchIntFIoPcOperSpeed_Type = CfprPortEthSpeed
_CfprEtherSwitchIntFIoPcOperSpeed_Object = MibTableColumn
cfprEtherSwitchIntFIoPcOperSpeed = _CfprEtherSwitchIntFIoPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 12),
    _CfprEtherSwitchIntFIoPcOperSpeed_Type()
)
cfprEtherSwitchIntFIoPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcOperSpeed.setStatus("current")
_CfprEtherSwitchIntFIoPcOperState_Type = CfprNetworkPortOperState
_CfprEtherSwitchIntFIoPcOperState_Object = MibTableColumn
cfprEtherSwitchIntFIoPcOperState = _CfprEtherSwitchIntFIoPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 13),
    _CfprEtherSwitchIntFIoPcOperState_Type()
)
cfprEtherSwitchIntFIoPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcOperState.setStatus("current")
_CfprEtherSwitchIntFIoPcPeerDn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcPeerDn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcPeerDn = _CfprEtherSwitchIntFIoPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 14),
    _CfprEtherSwitchIntFIoPcPeerDn_Type()
)
cfprEtherSwitchIntFIoPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcPeerDn.setStatus("current")
_CfprEtherSwitchIntFIoPcPortId_Type = CfprEtherSwitchIntFIoPcPortId
_CfprEtherSwitchIntFIoPcPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcPortId = _CfprEtherSwitchIntFIoPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 15),
    _CfprEtherSwitchIntFIoPcPortId_Type()
)
cfprEtherSwitchIntFIoPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcPortId.setStatus("current")
_CfprEtherSwitchIntFIoPcStateQual_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcStateQual_Object = MibTableColumn
cfprEtherSwitchIntFIoPcStateQual = _CfprEtherSwitchIntFIoPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 16),
    _CfprEtherSwitchIntFIoPcStateQual_Type()
)
cfprEtherSwitchIntFIoPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcStateQual.setStatus("current")
_CfprEtherSwitchIntFIoPcSwitchId_Type = CfprNetworkSwitchId
_CfprEtherSwitchIntFIoPcSwitchId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcSwitchId = _CfprEtherSwitchIntFIoPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 17),
    _CfprEtherSwitchIntFIoPcSwitchId_Type()
)
cfprEtherSwitchIntFIoPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcSwitchId.setStatus("current")
_CfprEtherSwitchIntFIoPcTransport_Type = CfprEtherSwitchIntFIoPcTransport
_CfprEtherSwitchIntFIoPcTransport_Object = MibTableColumn
cfprEtherSwitchIntFIoPcTransport = _CfprEtherSwitchIntFIoPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 18),
    _CfprEtherSwitchIntFIoPcTransport_Type()
)
cfprEtherSwitchIntFIoPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcTransport.setStatus("current")
_CfprEtherSwitchIntFIoPcType_Type = CfprEtherSwitchIntFIoPcType
_CfprEtherSwitchIntFIoPcType_Object = MibTableColumn
cfprEtherSwitchIntFIoPcType = _CfprEtherSwitchIntFIoPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 28, 1, 19),
    _CfprEtherSwitchIntFIoPcType_Type()
)
cfprEtherSwitchIntFIoPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcType.setStatus("current")
_CfprEtherSwitchIntFIoPcEpTable_Object = MibTable
cfprEtherSwitchIntFIoPcEpTable = _CfprEtherSwitchIntFIoPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29)
)
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpTable.setStatus("current")
_CfprEtherSwitchIntFIoPcEpEntry_Object = MibTableRow
cfprEtherSwitchIntFIoPcEpEntry = _CfprEtherSwitchIntFIoPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1)
)
cfprEtherSwitchIntFIoPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherSwitchIntFIoPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpEntry.setStatus("current")
_CfprEtherSwitchIntFIoPcEpInstanceId_Type = CfprManagedObjectId
_CfprEtherSwitchIntFIoPcEpInstanceId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpInstanceId = _CfprEtherSwitchIntFIoPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 1),
    _CfprEtherSwitchIntFIoPcEpInstanceId_Type()
)
cfprEtherSwitchIntFIoPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpInstanceId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpDnData_Type = CfprManagedObjectDn
_CfprEtherSwitchIntFIoPcEpDnData_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpDnData = _CfprEtherSwitchIntFIoPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 2),
    _CfprEtherSwitchIntFIoPcEpDnData_Type()
)
cfprEtherSwitchIntFIoPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpDnData.setStatus("current")
_CfprEtherSwitchIntFIoPcEpRn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcEpRn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpRn = _CfprEtherSwitchIntFIoPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 3),
    _CfprEtherSwitchIntFIoPcEpRn_Type()
)
cfprEtherSwitchIntFIoPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpRn.setStatus("current")
_CfprEtherSwitchIntFIoPcEpAckState_Type = CfprEquipmentChassisConfigState
_CfprEtherSwitchIntFIoPcEpAckState_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpAckState = _CfprEtherSwitchIntFIoPcEpAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 4),
    _CfprEtherSwitchIntFIoPcEpAckState_Type()
)
cfprEtherSwitchIntFIoPcEpAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpAckState.setStatus("current")
_CfprEtherSwitchIntFIoPcEpAdminState_Type = CfprEtherExternalEpAdminState
_CfprEtherSwitchIntFIoPcEpAdminState_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpAdminState = _CfprEtherSwitchIntFIoPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 5),
    _CfprEtherSwitchIntFIoPcEpAdminState_Type()
)
cfprEtherSwitchIntFIoPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpAdminState.setStatus("current")
_CfprEtherSwitchIntFIoPcEpAggrPortId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpAggrPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpAggrPortId = _CfprEtherSwitchIntFIoPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 6),
    _CfprEtherSwitchIntFIoPcEpAggrPortId_Type()
)
cfprEtherSwitchIntFIoPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpAggrPortId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpChassisId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpChassisId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpChassisId = _CfprEtherSwitchIntFIoPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 7),
    _CfprEtherSwitchIntFIoPcEpChassisId_Type()
)
cfprEtherSwitchIntFIoPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpChassisId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpEpDn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcEpEpDn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpEpDn = _CfprEtherSwitchIntFIoPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 8),
    _CfprEtherSwitchIntFIoPcEpEpDn_Type()
)
cfprEtherSwitchIntFIoPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpEpDn.setStatus("current")
_CfprEtherSwitchIntFIoPcEpIfRole_Type = CfprEtherSwitchIntFIoPcEpIfRole
_CfprEtherSwitchIntFIoPcEpIfRole_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpIfRole = _CfprEtherSwitchIntFIoPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 9),
    _CfprEtherSwitchIntFIoPcEpIfRole_Type()
)
cfprEtherSwitchIntFIoPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpIfRole.setStatus("current")
_CfprEtherSwitchIntFIoPcEpIfType_Type = CfprEtherPIoEpIfType
_CfprEtherSwitchIntFIoPcEpIfType_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpIfType = _CfprEtherSwitchIntFIoPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 10),
    _CfprEtherSwitchIntFIoPcEpIfType_Type()
)
cfprEtherSwitchIntFIoPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpIfType.setStatus("current")
_CfprEtherSwitchIntFIoPcEpLocale_Type = CfprEtherExternalEpLocale
_CfprEtherSwitchIntFIoPcEpLocale_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpLocale = _CfprEtherSwitchIntFIoPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 11),
    _CfprEtherSwitchIntFIoPcEpLocale_Type()
)
cfprEtherSwitchIntFIoPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpLocale.setStatus("current")
_CfprEtherSwitchIntFIoPcEpMembership_Type = CfprFabricMembershipStatus
_CfprEtherSwitchIntFIoPcEpMembership_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpMembership = _CfprEtherSwitchIntFIoPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 12),
    _CfprEtherSwitchIntFIoPcEpMembership_Type()
)
cfprEtherSwitchIntFIoPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpMembership.setStatus("current")
_CfprEtherSwitchIntFIoPcEpName_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcEpName_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpName = _CfprEtherSwitchIntFIoPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 13),
    _CfprEtherSwitchIntFIoPcEpName_Type()
)
cfprEtherSwitchIntFIoPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpName.setStatus("current")
_CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerAggrPortId = _CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 14),
    _CfprEtherSwitchIntFIoPcEpPeerAggrPortId_Type()
)
cfprEtherSwitchIntFIoPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpPeerAggrPortId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpPeerChassisId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpPeerChassisId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerChassisId = _CfprEtherSwitchIntFIoPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 15),
    _CfprEtherSwitchIntFIoPcEpPeerChassisId_Type()
)
cfprEtherSwitchIntFIoPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpPeerChassisId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpPeerDn_Type = SnmpAdminString
_CfprEtherSwitchIntFIoPcEpPeerDn_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerDn = _CfprEtherSwitchIntFIoPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 16),
    _CfprEtherSwitchIntFIoPcEpPeerDn_Type()
)
cfprEtherSwitchIntFIoPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpPeerDn.setStatus("current")
_CfprEtherSwitchIntFIoPcEpPeerPortId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpPeerPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerPortId = _CfprEtherSwitchIntFIoPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 17),
    _CfprEtherSwitchIntFIoPcEpPeerPortId_Type()
)
cfprEtherSwitchIntFIoPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpPeerPortId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpPeerSlotId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpPeerSlotId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpPeerSlotId = _CfprEtherSwitchIntFIoPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 18),
    _CfprEtherSwitchIntFIoPcEpPeerSlotId_Type()
)
cfprEtherSwitchIntFIoPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpPeerSlotId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpPortId_Type = CfprEtherSwitchIntFIoPcEpPortId
_CfprEtherSwitchIntFIoPcEpPortId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpPortId = _CfprEtherSwitchIntFIoPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 19),
    _CfprEtherSwitchIntFIoPcEpPortId_Type()
)
cfprEtherSwitchIntFIoPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpPortId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpSlotId_Type = Gauge32
_CfprEtherSwitchIntFIoPcEpSlotId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpSlotId = _CfprEtherSwitchIntFIoPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 20),
    _CfprEtherSwitchIntFIoPcEpSlotId_Type()
)
cfprEtherSwitchIntFIoPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpSlotId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpStatusChangeTs_Type = DateAndTime
_CfprEtherSwitchIntFIoPcEpStatusChangeTs_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpStatusChangeTs = _CfprEtherSwitchIntFIoPcEpStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 21),
    _CfprEtherSwitchIntFIoPcEpStatusChangeTs_Type()
)
cfprEtherSwitchIntFIoPcEpStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpStatusChangeTs.setStatus("current")
_CfprEtherSwitchIntFIoPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprEtherSwitchIntFIoPcEpSwitchId_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpSwitchId = _CfprEtherSwitchIntFIoPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 22),
    _CfprEtherSwitchIntFIoPcEpSwitchId_Type()
)
cfprEtherSwitchIntFIoPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpSwitchId.setStatus("current")
_CfprEtherSwitchIntFIoPcEpTransport_Type = CfprNetworkTransport
_CfprEtherSwitchIntFIoPcEpTransport_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpTransport = _CfprEtherSwitchIntFIoPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 23),
    _CfprEtherSwitchIntFIoPcEpTransport_Type()
)
cfprEtherSwitchIntFIoPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpTransport.setStatus("current")
_CfprEtherSwitchIntFIoPcEpType_Type = CfprEtherIntFIoEpType
_CfprEtherSwitchIntFIoPcEpType_Object = MibTableColumn
cfprEtherSwitchIntFIoPcEpType = _CfprEtherSwitchIntFIoPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 29, 1, 24),
    _CfprEtherSwitchIntFIoPcEpType_Type()
)
cfprEtherSwitchIntFIoPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherSwitchIntFIoPcEpType.setStatus("current")
_CfprEtherTxStatsTable_Object = MibTable
cfprEtherTxStatsTable = _CfprEtherTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30)
)
if mibBuilder.loadTexts:
    cfprEtherTxStatsTable.setStatus("current")
_CfprEtherTxStatsEntry_Object = MibTableRow
cfprEtherTxStatsEntry = _CfprEtherTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1)
)
cfprEtherTxStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherTxStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherTxStatsEntry.setStatus("current")
_CfprEtherTxStatsInstanceId_Type = CfprManagedObjectId
_CfprEtherTxStatsInstanceId_Object = MibTableColumn
cfprEtherTxStatsInstanceId = _CfprEtherTxStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 1),
    _CfprEtherTxStatsInstanceId_Type()
)
cfprEtherTxStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherTxStatsInstanceId.setStatus("current")
_CfprEtherTxStatsDn_Type = CfprManagedObjectDn
_CfprEtherTxStatsDn_Object = MibTableColumn
cfprEtherTxStatsDn = _CfprEtherTxStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 2),
    _CfprEtherTxStatsDn_Type()
)
cfprEtherTxStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsDn.setStatus("current")
_CfprEtherTxStatsRn_Type = SnmpAdminString
_CfprEtherTxStatsRn_Object = MibTableColumn
cfprEtherTxStatsRn = _CfprEtherTxStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 3),
    _CfprEtherTxStatsRn_Type()
)
cfprEtherTxStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsRn.setStatus("current")
_CfprEtherTxStatsBroadcastPackets_Type = Unsigned64
_CfprEtherTxStatsBroadcastPackets_Object = MibTableColumn
cfprEtherTxStatsBroadcastPackets = _CfprEtherTxStatsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 4),
    _CfprEtherTxStatsBroadcastPackets_Type()
)
cfprEtherTxStatsBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsBroadcastPackets.setStatus("current")
_CfprEtherTxStatsBroadcastPacketsDelta_Type = Counter64
_CfprEtherTxStatsBroadcastPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsBroadcastPacketsDelta = _CfprEtherTxStatsBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 5),
    _CfprEtherTxStatsBroadcastPacketsDelta_Type()
)
cfprEtherTxStatsBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsBroadcastPacketsDelta.setStatus("current")
_CfprEtherTxStatsBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsBroadcastPacketsDeltaAvg = _CfprEtherTxStatsBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 6),
    _CfprEtherTxStatsBroadcastPacketsDeltaAvg_Type()
)
cfprEtherTxStatsBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsBroadcastPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsBroadcastPacketsDeltaMax = _CfprEtherTxStatsBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 7),
    _CfprEtherTxStatsBroadcastPacketsDeltaMax_Type()
)
cfprEtherTxStatsBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsBroadcastPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsBroadcastPacketsDeltaMin = _CfprEtherTxStatsBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 8),
    _CfprEtherTxStatsBroadcastPacketsDeltaMin_Type()
)
cfprEtherTxStatsBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsBroadcastPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsIntervals_Type = Gauge32
_CfprEtherTxStatsIntervals_Object = MibTableColumn
cfprEtherTxStatsIntervals = _CfprEtherTxStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 9),
    _CfprEtherTxStatsIntervals_Type()
)
cfprEtherTxStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsIntervals.setStatus("current")
_CfprEtherTxStatsJumboPackets_Type = Unsigned64
_CfprEtherTxStatsJumboPackets_Object = MibTableColumn
cfprEtherTxStatsJumboPackets = _CfprEtherTxStatsJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 10),
    _CfprEtherTxStatsJumboPackets_Type()
)
cfprEtherTxStatsJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsJumboPackets.setStatus("current")
_CfprEtherTxStatsJumboPacketsDelta_Type = Counter64
_CfprEtherTxStatsJumboPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsJumboPacketsDelta = _CfprEtherTxStatsJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 11),
    _CfprEtherTxStatsJumboPacketsDelta_Type()
)
cfprEtherTxStatsJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsJumboPacketsDelta.setStatus("current")
_CfprEtherTxStatsJumboPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsJumboPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsJumboPacketsDeltaAvg = _CfprEtherTxStatsJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 12),
    _CfprEtherTxStatsJumboPacketsDeltaAvg_Type()
)
cfprEtherTxStatsJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsJumboPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsJumboPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsJumboPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsJumboPacketsDeltaMax = _CfprEtherTxStatsJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 13),
    _CfprEtherTxStatsJumboPacketsDeltaMax_Type()
)
cfprEtherTxStatsJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsJumboPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsJumboPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsJumboPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsJumboPacketsDeltaMin = _CfprEtherTxStatsJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 14),
    _CfprEtherTxStatsJumboPacketsDeltaMin_Type()
)
cfprEtherTxStatsJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsJumboPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsMulticastPackets_Type = Unsigned64
_CfprEtherTxStatsMulticastPackets_Object = MibTableColumn
cfprEtherTxStatsMulticastPackets = _CfprEtherTxStatsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 15),
    _CfprEtherTxStatsMulticastPackets_Type()
)
cfprEtherTxStatsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsMulticastPackets.setStatus("current")
_CfprEtherTxStatsMulticastPacketsDelta_Type = Counter64
_CfprEtherTxStatsMulticastPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsMulticastPacketsDelta = _CfprEtherTxStatsMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 16),
    _CfprEtherTxStatsMulticastPacketsDelta_Type()
)
cfprEtherTxStatsMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsMulticastPacketsDelta.setStatus("current")
_CfprEtherTxStatsMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsMulticastPacketsDeltaAvg = _CfprEtherTxStatsMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 17),
    _CfprEtherTxStatsMulticastPacketsDeltaAvg_Type()
)
cfprEtherTxStatsMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsMulticastPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsMulticastPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsMulticastPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsMulticastPacketsDeltaMax = _CfprEtherTxStatsMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 18),
    _CfprEtherTxStatsMulticastPacketsDeltaMax_Type()
)
cfprEtherTxStatsMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsMulticastPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsMulticastPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsMulticastPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsMulticastPacketsDeltaMin = _CfprEtherTxStatsMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 19),
    _CfprEtherTxStatsMulticastPacketsDeltaMin_Type()
)
cfprEtherTxStatsMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsMulticastPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsSuspect_Type = TruthValue
_CfprEtherTxStatsSuspect_Object = MibTableColumn
cfprEtherTxStatsSuspect = _CfprEtherTxStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 20),
    _CfprEtherTxStatsSuspect_Type()
)
cfprEtherTxStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsSuspect.setStatus("current")
_CfprEtherTxStatsThresholded_Type = CfprEtherTxStatsThresholded
_CfprEtherTxStatsThresholded_Object = MibTableColumn
cfprEtherTxStatsThresholded = _CfprEtherTxStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 21),
    _CfprEtherTxStatsThresholded_Type()
)
cfprEtherTxStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsThresholded.setStatus("current")
_CfprEtherTxStatsTimeCollected_Type = DateAndTime
_CfprEtherTxStatsTimeCollected_Object = MibTableColumn
cfprEtherTxStatsTimeCollected = _CfprEtherTxStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 22),
    _CfprEtherTxStatsTimeCollected_Type()
)
cfprEtherTxStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTimeCollected.setStatus("current")
_CfprEtherTxStatsTotalBytes_Type = Unsigned64
_CfprEtherTxStatsTotalBytes_Object = MibTableColumn
cfprEtherTxStatsTotalBytes = _CfprEtherTxStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 23),
    _CfprEtherTxStatsTotalBytes_Type()
)
cfprEtherTxStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalBytes.setStatus("current")
_CfprEtherTxStatsTotalBytesDelta_Type = Counter64
_CfprEtherTxStatsTotalBytesDelta_Object = MibTableColumn
cfprEtherTxStatsTotalBytesDelta = _CfprEtherTxStatsTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 24),
    _CfprEtherTxStatsTotalBytesDelta_Type()
)
cfprEtherTxStatsTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalBytesDelta.setStatus("current")
_CfprEtherTxStatsTotalBytesDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsTotalBytesDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsTotalBytesDeltaAvg = _CfprEtherTxStatsTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 25),
    _CfprEtherTxStatsTotalBytesDeltaAvg_Type()
)
cfprEtherTxStatsTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalBytesDeltaAvg.setStatus("current")
_CfprEtherTxStatsTotalBytesDeltaMax_Type = Unsigned64
_CfprEtherTxStatsTotalBytesDeltaMax_Object = MibTableColumn
cfprEtherTxStatsTotalBytesDeltaMax = _CfprEtherTxStatsTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 26),
    _CfprEtherTxStatsTotalBytesDeltaMax_Type()
)
cfprEtherTxStatsTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalBytesDeltaMax.setStatus("current")
_CfprEtherTxStatsTotalBytesDeltaMin_Type = Unsigned64
_CfprEtherTxStatsTotalBytesDeltaMin_Object = MibTableColumn
cfprEtherTxStatsTotalBytesDeltaMin = _CfprEtherTxStatsTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 27),
    _CfprEtherTxStatsTotalBytesDeltaMin_Type()
)
cfprEtherTxStatsTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalBytesDeltaMin.setStatus("current")
_CfprEtherTxStatsTotalPackets_Type = Unsigned64
_CfprEtherTxStatsTotalPackets_Object = MibTableColumn
cfprEtherTxStatsTotalPackets = _CfprEtherTxStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 28),
    _CfprEtherTxStatsTotalPackets_Type()
)
cfprEtherTxStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalPackets.setStatus("current")
_CfprEtherTxStatsTotalPacketsDelta_Type = Counter64
_CfprEtherTxStatsTotalPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsTotalPacketsDelta = _CfprEtherTxStatsTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 29),
    _CfprEtherTxStatsTotalPacketsDelta_Type()
)
cfprEtherTxStatsTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalPacketsDelta.setStatus("current")
_CfprEtherTxStatsTotalPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsTotalPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsTotalPacketsDeltaAvg = _CfprEtherTxStatsTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 30),
    _CfprEtherTxStatsTotalPacketsDeltaAvg_Type()
)
cfprEtherTxStatsTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsTotalPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsTotalPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsTotalPacketsDeltaMax = _CfprEtherTxStatsTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 31),
    _CfprEtherTxStatsTotalPacketsDeltaMax_Type()
)
cfprEtherTxStatsTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsTotalPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsTotalPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsTotalPacketsDeltaMin = _CfprEtherTxStatsTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 32),
    _CfprEtherTxStatsTotalPacketsDeltaMin_Type()
)
cfprEtherTxStatsTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsTotalPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsUnicastPackets_Type = Unsigned64
_CfprEtherTxStatsUnicastPackets_Object = MibTableColumn
cfprEtherTxStatsUnicastPackets = _CfprEtherTxStatsUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 33),
    _CfprEtherTxStatsUnicastPackets_Type()
)
cfprEtherTxStatsUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsUnicastPackets.setStatus("current")
_CfprEtherTxStatsUnicastPacketsDelta_Type = Counter64
_CfprEtherTxStatsUnicastPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsUnicastPacketsDelta = _CfprEtherTxStatsUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 34),
    _CfprEtherTxStatsUnicastPacketsDelta_Type()
)
cfprEtherTxStatsUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsUnicastPacketsDelta.setStatus("current")
_CfprEtherTxStatsUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsUnicastPacketsDeltaAvg = _CfprEtherTxStatsUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 35),
    _CfprEtherTxStatsUnicastPacketsDeltaAvg_Type()
)
cfprEtherTxStatsUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsUnicastPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsUnicastPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsUnicastPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsUnicastPacketsDeltaMax = _CfprEtherTxStatsUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 36),
    _CfprEtherTxStatsUnicastPacketsDeltaMax_Type()
)
cfprEtherTxStatsUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsUnicastPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsUnicastPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsUnicastPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsUnicastPacketsDeltaMin = _CfprEtherTxStatsUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 37),
    _CfprEtherTxStatsUnicastPacketsDeltaMin_Type()
)
cfprEtherTxStatsUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsUnicastPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsUpdate_Type = Gauge32
_CfprEtherTxStatsUpdate_Object = MibTableColumn
cfprEtherTxStatsUpdate = _CfprEtherTxStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 30, 1, 38),
    _CfprEtherTxStatsUpdate_Type()
)
cfprEtherTxStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsUpdate.setStatus("current")
_CfprEtherTxStatsHistTable_Object = MibTable
cfprEtherTxStatsHistTable = _CfprEtherTxStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31)
)
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTable.setStatus("current")
_CfprEtherTxStatsHistEntry_Object = MibTableRow
cfprEtherTxStatsHistEntry = _CfprEtherTxStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1)
)
cfprEtherTxStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherTxStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistEntry.setStatus("current")
_CfprEtherTxStatsHistInstanceId_Type = CfprManagedObjectId
_CfprEtherTxStatsHistInstanceId_Object = MibTableColumn
cfprEtherTxStatsHistInstanceId = _CfprEtherTxStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 1),
    _CfprEtherTxStatsHistInstanceId_Type()
)
cfprEtherTxStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistInstanceId.setStatus("current")
_CfprEtherTxStatsHistDn_Type = CfprManagedObjectDn
_CfprEtherTxStatsHistDn_Object = MibTableColumn
cfprEtherTxStatsHistDn = _CfprEtherTxStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 2),
    _CfprEtherTxStatsHistDn_Type()
)
cfprEtherTxStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistDn.setStatus("current")
_CfprEtherTxStatsHistRn_Type = SnmpAdminString
_CfprEtherTxStatsHistRn_Object = MibTableColumn
cfprEtherTxStatsHistRn = _CfprEtherTxStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 3),
    _CfprEtherTxStatsHistRn_Type()
)
cfprEtherTxStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistRn.setStatus("current")
_CfprEtherTxStatsHistBroadcastPackets_Type = Unsigned64
_CfprEtherTxStatsHistBroadcastPackets_Object = MibTableColumn
cfprEtherTxStatsHistBroadcastPackets = _CfprEtherTxStatsHistBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 4),
    _CfprEtherTxStatsHistBroadcastPackets_Type()
)
cfprEtherTxStatsHistBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistBroadcastPackets.setStatus("current")
_CfprEtherTxStatsHistBroadcastPacketsDelta_Type = Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDelta = _CfprEtherTxStatsHistBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 5),
    _CfprEtherTxStatsHistBroadcastPacketsDelta_Type()
)
cfprEtherTxStatsHistBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistBroadcastPacketsDelta.setStatus("current")
_CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDeltaAvg = _CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 6),
    _CfprEtherTxStatsHistBroadcastPacketsDeltaAvg_Type()
)
cfprEtherTxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistBroadcastPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDeltaMax = _CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 7),
    _CfprEtherTxStatsHistBroadcastPacketsDeltaMax_Type()
)
cfprEtherTxStatsHistBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistBroadcastPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsHistBroadcastPacketsDeltaMin = _CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 8),
    _CfprEtherTxStatsHistBroadcastPacketsDeltaMin_Type()
)
cfprEtherTxStatsHistBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistBroadcastPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsHistId_Type = Unsigned64
_CfprEtherTxStatsHistId_Object = MibTableColumn
cfprEtherTxStatsHistId = _CfprEtherTxStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 9),
    _CfprEtherTxStatsHistId_Type()
)
cfprEtherTxStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistId.setStatus("current")
_CfprEtherTxStatsHistJumboPackets_Type = Unsigned64
_CfprEtherTxStatsHistJumboPackets_Object = MibTableColumn
cfprEtherTxStatsHistJumboPackets = _CfprEtherTxStatsHistJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 10),
    _CfprEtherTxStatsHistJumboPackets_Type()
)
cfprEtherTxStatsHistJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistJumboPackets.setStatus("current")
_CfprEtherTxStatsHistJumboPacketsDelta_Type = Unsigned64
_CfprEtherTxStatsHistJumboPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsHistJumboPacketsDelta = _CfprEtherTxStatsHistJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 11),
    _CfprEtherTxStatsHistJumboPacketsDelta_Type()
)
cfprEtherTxStatsHistJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistJumboPacketsDelta.setStatus("current")
_CfprEtherTxStatsHistJumboPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsHistJumboPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsHistJumboPacketsDeltaAvg = _CfprEtherTxStatsHistJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 12),
    _CfprEtherTxStatsHistJumboPacketsDeltaAvg_Type()
)
cfprEtherTxStatsHistJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistJumboPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsHistJumboPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsHistJumboPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsHistJumboPacketsDeltaMax = _CfprEtherTxStatsHistJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 13),
    _CfprEtherTxStatsHistJumboPacketsDeltaMax_Type()
)
cfprEtherTxStatsHistJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistJumboPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsHistJumboPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsHistJumboPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsHistJumboPacketsDeltaMin = _CfprEtherTxStatsHistJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 14),
    _CfprEtherTxStatsHistJumboPacketsDeltaMin_Type()
)
cfprEtherTxStatsHistJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistJumboPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsHistMostRecent_Type = TruthValue
_CfprEtherTxStatsHistMostRecent_Object = MibTableColumn
cfprEtherTxStatsHistMostRecent = _CfprEtherTxStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 15),
    _CfprEtherTxStatsHistMostRecent_Type()
)
cfprEtherTxStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistMostRecent.setStatus("current")
_CfprEtherTxStatsHistMulticastPackets_Type = Unsigned64
_CfprEtherTxStatsHistMulticastPackets_Object = MibTableColumn
cfprEtherTxStatsHistMulticastPackets = _CfprEtherTxStatsHistMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 16),
    _CfprEtherTxStatsHistMulticastPackets_Type()
)
cfprEtherTxStatsHistMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistMulticastPackets.setStatus("current")
_CfprEtherTxStatsHistMulticastPacketsDelta_Type = Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDelta = _CfprEtherTxStatsHistMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 17),
    _CfprEtherTxStatsHistMulticastPacketsDelta_Type()
)
cfprEtherTxStatsHistMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistMulticastPacketsDelta.setStatus("current")
_CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDeltaAvg = _CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 18),
    _CfprEtherTxStatsHistMulticastPacketsDeltaAvg_Type()
)
cfprEtherTxStatsHistMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistMulticastPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsHistMulticastPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDeltaMax = _CfprEtherTxStatsHistMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 19),
    _CfprEtherTxStatsHistMulticastPacketsDeltaMax_Type()
)
cfprEtherTxStatsHistMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistMulticastPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsHistMulticastPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsHistMulticastPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsHistMulticastPacketsDeltaMin = _CfprEtherTxStatsHistMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 20),
    _CfprEtherTxStatsHistMulticastPacketsDeltaMin_Type()
)
cfprEtherTxStatsHistMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistMulticastPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsHistSuspect_Type = TruthValue
_CfprEtherTxStatsHistSuspect_Object = MibTableColumn
cfprEtherTxStatsHistSuspect = _CfprEtherTxStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 21),
    _CfprEtherTxStatsHistSuspect_Type()
)
cfprEtherTxStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistSuspect.setStatus("current")
_CfprEtherTxStatsHistThresholded_Type = CfprEtherTxStatsHistThresholded
_CfprEtherTxStatsHistThresholded_Object = MibTableColumn
cfprEtherTxStatsHistThresholded = _CfprEtherTxStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 22),
    _CfprEtherTxStatsHistThresholded_Type()
)
cfprEtherTxStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistThresholded.setStatus("current")
_CfprEtherTxStatsHistTimeCollected_Type = DateAndTime
_CfprEtherTxStatsHistTimeCollected_Object = MibTableColumn
cfprEtherTxStatsHistTimeCollected = _CfprEtherTxStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 23),
    _CfprEtherTxStatsHistTimeCollected_Type()
)
cfprEtherTxStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTimeCollected.setStatus("current")
_CfprEtherTxStatsHistTotalBytes_Type = Unsigned64
_CfprEtherTxStatsHistTotalBytes_Object = MibTableColumn
cfprEtherTxStatsHistTotalBytes = _CfprEtherTxStatsHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 24),
    _CfprEtherTxStatsHistTotalBytes_Type()
)
cfprEtherTxStatsHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalBytes.setStatus("current")
_CfprEtherTxStatsHistTotalBytesDelta_Type = Unsigned64
_CfprEtherTxStatsHistTotalBytesDelta_Object = MibTableColumn
cfprEtherTxStatsHistTotalBytesDelta = _CfprEtherTxStatsHistTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 25),
    _CfprEtherTxStatsHistTotalBytesDelta_Type()
)
cfprEtherTxStatsHistTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalBytesDelta.setStatus("current")
_CfprEtherTxStatsHistTotalBytesDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsHistTotalBytesDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsHistTotalBytesDeltaAvg = _CfprEtherTxStatsHistTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 26),
    _CfprEtherTxStatsHistTotalBytesDeltaAvg_Type()
)
cfprEtherTxStatsHistTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalBytesDeltaAvg.setStatus("current")
_CfprEtherTxStatsHistTotalBytesDeltaMax_Type = Unsigned64
_CfprEtherTxStatsHistTotalBytesDeltaMax_Object = MibTableColumn
cfprEtherTxStatsHistTotalBytesDeltaMax = _CfprEtherTxStatsHistTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 27),
    _CfprEtherTxStatsHistTotalBytesDeltaMax_Type()
)
cfprEtherTxStatsHistTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalBytesDeltaMax.setStatus("current")
_CfprEtherTxStatsHistTotalBytesDeltaMin_Type = Unsigned64
_CfprEtherTxStatsHistTotalBytesDeltaMin_Object = MibTableColumn
cfprEtherTxStatsHistTotalBytesDeltaMin = _CfprEtherTxStatsHistTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 28),
    _CfprEtherTxStatsHistTotalBytesDeltaMin_Type()
)
cfprEtherTxStatsHistTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalBytesDeltaMin.setStatus("current")
_CfprEtherTxStatsHistTotalPackets_Type = Unsigned64
_CfprEtherTxStatsHistTotalPackets_Object = MibTableColumn
cfprEtherTxStatsHistTotalPackets = _CfprEtherTxStatsHistTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 29),
    _CfprEtherTxStatsHistTotalPackets_Type()
)
cfprEtherTxStatsHistTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalPackets.setStatus("current")
_CfprEtherTxStatsHistTotalPacketsDelta_Type = Unsigned64
_CfprEtherTxStatsHistTotalPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsHistTotalPacketsDelta = _CfprEtherTxStatsHistTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 30),
    _CfprEtherTxStatsHistTotalPacketsDelta_Type()
)
cfprEtherTxStatsHistTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalPacketsDelta.setStatus("current")
_CfprEtherTxStatsHistTotalPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsHistTotalPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsHistTotalPacketsDeltaAvg = _CfprEtherTxStatsHistTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 31),
    _CfprEtherTxStatsHistTotalPacketsDeltaAvg_Type()
)
cfprEtherTxStatsHistTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsHistTotalPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsHistTotalPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsHistTotalPacketsDeltaMax = _CfprEtherTxStatsHistTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 32),
    _CfprEtherTxStatsHistTotalPacketsDeltaMax_Type()
)
cfprEtherTxStatsHistTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsHistTotalPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsHistTotalPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsHistTotalPacketsDeltaMin = _CfprEtherTxStatsHistTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 33),
    _CfprEtherTxStatsHistTotalPacketsDeltaMin_Type()
)
cfprEtherTxStatsHistTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistTotalPacketsDeltaMin.setStatus("current")
_CfprEtherTxStatsHistUnicastPackets_Type = Unsigned64
_CfprEtherTxStatsHistUnicastPackets_Object = MibTableColumn
cfprEtherTxStatsHistUnicastPackets = _CfprEtherTxStatsHistUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 34),
    _CfprEtherTxStatsHistUnicastPackets_Type()
)
cfprEtherTxStatsHistUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistUnicastPackets.setStatus("current")
_CfprEtherTxStatsHistUnicastPacketsDelta_Type = Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDelta_Object = MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDelta = _CfprEtherTxStatsHistUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 35),
    _CfprEtherTxStatsHistUnicastPacketsDelta_Type()
)
cfprEtherTxStatsHistUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistUnicastPacketsDelta.setStatus("current")
_CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDeltaAvg = _CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 36),
    _CfprEtherTxStatsHistUnicastPacketsDeltaAvg_Type()
)
cfprEtherTxStatsHistUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistUnicastPacketsDeltaAvg.setStatus("current")
_CfprEtherTxStatsHistUnicastPacketsDeltaMax_Type = Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDeltaMax_Object = MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDeltaMax = _CfprEtherTxStatsHistUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 37),
    _CfprEtherTxStatsHistUnicastPacketsDeltaMax_Type()
)
cfprEtherTxStatsHistUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistUnicastPacketsDeltaMax.setStatus("current")
_CfprEtherTxStatsHistUnicastPacketsDeltaMin_Type = Unsigned64
_CfprEtherTxStatsHistUnicastPacketsDeltaMin_Object = MibTableColumn
cfprEtherTxStatsHistUnicastPacketsDeltaMin = _CfprEtherTxStatsHistUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 31, 1, 38),
    _CfprEtherTxStatsHistUnicastPacketsDeltaMin_Type()
)
cfprEtherTxStatsHistUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherTxStatsHistUnicastPacketsDeltaMin.setStatus("current")
_CfprEtherFailToWireTable_Object = MibTable
cfprEtherFailToWireTable = _CfprEtherFailToWireTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32)
)
if mibBuilder.loadTexts:
    cfprEtherFailToWireTable.setStatus("current")
_CfprEtherFailToWireEntry_Object = MibTableRow
cfprEtherFailToWireEntry = _CfprEtherFailToWireEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1)
)
cfprEtherFailToWireEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFailToWireInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFailToWireEntry.setStatus("current")
_CfprEtherFailToWireInstanceId_Type = CfprManagedObjectId
_CfprEtherFailToWireInstanceId_Object = MibTableColumn
cfprEtherFailToWireInstanceId = _CfprEtherFailToWireInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 1),
    _CfprEtherFailToWireInstanceId_Type()
)
cfprEtherFailToWireInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFailToWireInstanceId.setStatus("current")
_CfprEtherFailToWireDn_Type = CfprManagedObjectDn
_CfprEtherFailToWireDn_Object = MibTableColumn
cfprEtherFailToWireDn = _CfprEtherFailToWireDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 2),
    _CfprEtherFailToWireDn_Type()
)
cfprEtherFailToWireDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFailToWireDn.setStatus("current")
_CfprEtherFailToWireRn_Type = SnmpAdminString
_CfprEtherFailToWireRn_Object = MibTableColumn
cfprEtherFailToWireRn = _CfprEtherFailToWireRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 3),
    _CfprEtherFailToWireRn_Type()
)
cfprEtherFailToWireRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFailToWireRn.setStatus("current")
_CfprEtherFailToWireLocale_Type = CfprNetworkLocale
_CfprEtherFailToWireLocale_Object = MibTableColumn
cfprEtherFailToWireLocale = _CfprEtherFailToWireLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 4),
    _CfprEtherFailToWireLocale_Type()
)
cfprEtherFailToWireLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFailToWireLocale.setStatus("current")
_CfprEtherFailToWireName_Type = SnmpAdminString
_CfprEtherFailToWireName_Object = MibTableColumn
cfprEtherFailToWireName = _CfprEtherFailToWireName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 5),
    _CfprEtherFailToWireName_Type()
)
cfprEtherFailToWireName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFailToWireName.setStatus("current")
_CfprEtherFailToWireTransport_Type = CfprNetworkTransport
_CfprEtherFailToWireTransport_Object = MibTableColumn
cfprEtherFailToWireTransport = _CfprEtherFailToWireTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 6),
    _CfprEtherFailToWireTransport_Type()
)
cfprEtherFailToWireTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFailToWireTransport.setStatus("current")
_CfprEtherFailToWireType_Type = CfprNetworkConnectionType
_CfprEtherFailToWireType_Object = MibTableColumn
cfprEtherFailToWireType = _CfprEtherFailToWireType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 32, 1, 7),
    _CfprEtherFailToWireType_Type()
)
cfprEtherFailToWireType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFailToWireType.setStatus("current")
_CfprEtherFtwPortPairTable_Object = MibTable
cfprEtherFtwPortPairTable = _CfprEtherFtwPortPairTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33)
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairTable.setStatus("current")
_CfprEtherFtwPortPairEntry_Object = MibTableRow
cfprEtherFtwPortPairEntry = _CfprEtherFtwPortPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1)
)
cfprEtherFtwPortPairEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFtwPortPairInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairEntry.setStatus("current")
_CfprEtherFtwPortPairInstanceId_Type = CfprManagedObjectId
_CfprEtherFtwPortPairInstanceId_Object = MibTableColumn
cfprEtherFtwPortPairInstanceId = _CfprEtherFtwPortPairInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 1),
    _CfprEtherFtwPortPairInstanceId_Type()
)
cfprEtherFtwPortPairInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairInstanceId.setStatus("current")
_CfprEtherFtwPortPairDn_Type = CfprManagedObjectDn
_CfprEtherFtwPortPairDn_Object = MibTableColumn
cfprEtherFtwPortPairDn = _CfprEtherFtwPortPairDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 2),
    _CfprEtherFtwPortPairDn_Type()
)
cfprEtherFtwPortPairDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairDn.setStatus("current")
_CfprEtherFtwPortPairRn_Type = SnmpAdminString
_CfprEtherFtwPortPairRn_Object = MibTableColumn
cfprEtherFtwPortPairRn = _CfprEtherFtwPortPairRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 3),
    _CfprEtherFtwPortPairRn_Type()
)
cfprEtherFtwPortPairRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairRn.setStatus("current")
_CfprEtherFtwPortPairAggrPortId_Type = Gauge32
_CfprEtherFtwPortPairAggrPortId_Object = MibTableColumn
cfprEtherFtwPortPairAggrPortId = _CfprEtherFtwPortPairAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 4),
    _CfprEtherFtwPortPairAggrPortId_Type()
)
cfprEtherFtwPortPairAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairAggrPortId.setStatus("current")
_CfprEtherFtwPortPairChassisId_Type = Gauge32
_CfprEtherFtwPortPairChassisId_Object = MibTableColumn
cfprEtherFtwPortPairChassisId = _CfprEtherFtwPortPairChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 5),
    _CfprEtherFtwPortPairChassisId_Type()
)
cfprEtherFtwPortPairChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairChassisId.setStatus("current")
_CfprEtherFtwPortPairEpDn_Type = SnmpAdminString
_CfprEtherFtwPortPairEpDn_Object = MibTableColumn
cfprEtherFtwPortPairEpDn = _CfprEtherFtwPortPairEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 6),
    _CfprEtherFtwPortPairEpDn_Type()
)
cfprEtherFtwPortPairEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairEpDn.setStatus("current")
_CfprEtherFtwPortPairFsmDescr_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmDescr_Object = MibTableColumn
cfprEtherFtwPortPairFsmDescr = _CfprEtherFtwPortPairFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 7),
    _CfprEtherFtwPortPairFsmDescr_Type()
)
cfprEtherFtwPortPairFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmDescr.setStatus("current")
_CfprEtherFtwPortPairFsmPrev_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmPrev_Object = MibTableColumn
cfprEtherFtwPortPairFsmPrev = _CfprEtherFtwPortPairFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 8),
    _CfprEtherFtwPortPairFsmPrev_Type()
)
cfprEtherFtwPortPairFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmPrev.setStatus("current")
_CfprEtherFtwPortPairFsmProgr_Type = Gauge32
_CfprEtherFtwPortPairFsmProgr_Object = MibTableColumn
cfprEtherFtwPortPairFsmProgr = _CfprEtherFtwPortPairFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 9),
    _CfprEtherFtwPortPairFsmProgr_Type()
)
cfprEtherFtwPortPairFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmProgr.setStatus("current")
_CfprEtherFtwPortPairFsmRmtInvErrCode_Type = Gauge32
_CfprEtherFtwPortPairFsmRmtInvErrCode_Object = MibTableColumn
cfprEtherFtwPortPairFsmRmtInvErrCode = _CfprEtherFtwPortPairFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 10),
    _CfprEtherFtwPortPairFsmRmtInvErrCode_Type()
)
cfprEtherFtwPortPairFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRmtInvErrCode.setStatus("current")
_CfprEtherFtwPortPairFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmRmtInvErrDescr_Object = MibTableColumn
cfprEtherFtwPortPairFsmRmtInvErrDescr = _CfprEtherFtwPortPairFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 11),
    _CfprEtherFtwPortPairFsmRmtInvErrDescr_Type()
)
cfprEtherFtwPortPairFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRmtInvErrDescr.setStatus("current")
_CfprEtherFtwPortPairFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprEtherFtwPortPairFsmRmtInvRslt_Object = MibTableColumn
cfprEtherFtwPortPairFsmRmtInvRslt = _CfprEtherFtwPortPairFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 12),
    _CfprEtherFtwPortPairFsmRmtInvRslt_Type()
)
cfprEtherFtwPortPairFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRmtInvRslt.setStatus("current")
_CfprEtherFtwPortPairFsmStageDescr_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmStageDescr_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageDescr = _CfprEtherFtwPortPairFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 13),
    _CfprEtherFtwPortPairFsmStageDescr_Type()
)
cfprEtherFtwPortPairFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageDescr.setStatus("current")
_CfprEtherFtwPortPairFsmStamp_Type = DateAndTime
_CfprEtherFtwPortPairFsmStamp_Object = MibTableColumn
cfprEtherFtwPortPairFsmStamp = _CfprEtherFtwPortPairFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 14),
    _CfprEtherFtwPortPairFsmStamp_Type()
)
cfprEtherFtwPortPairFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStamp.setStatus("current")
_CfprEtherFtwPortPairFsmStatus_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmStatus_Object = MibTableColumn
cfprEtherFtwPortPairFsmStatus = _CfprEtherFtwPortPairFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 15),
    _CfprEtherFtwPortPairFsmStatus_Type()
)
cfprEtherFtwPortPairFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStatus.setStatus("current")
_CfprEtherFtwPortPairFsmTry_Type = Gauge32
_CfprEtherFtwPortPairFsmTry_Object = MibTableColumn
cfprEtherFtwPortPairFsmTry = _CfprEtherFtwPortPairFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 16),
    _CfprEtherFtwPortPairFsmTry_Type()
)
cfprEtherFtwPortPairFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTry.setStatus("current")
_CfprEtherFtwPortPairIfRole_Type = CfprNetworkPortRole
_CfprEtherFtwPortPairIfRole_Object = MibTableColumn
cfprEtherFtwPortPairIfRole = _CfprEtherFtwPortPairIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 17),
    _CfprEtherFtwPortPairIfRole_Type()
)
cfprEtherFtwPortPairIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairIfRole.setStatus("current")
_CfprEtherFtwPortPairIfType_Type = CfprNetworkPhysEpIfType
_CfprEtherFtwPortPairIfType_Object = MibTableColumn
cfprEtherFtwPortPairIfType = _CfprEtherFtwPortPairIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 18),
    _CfprEtherFtwPortPairIfType_Type()
)
cfprEtherFtwPortPairIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairIfType.setStatus("current")
_CfprEtherFtwPortPairLocale_Type = CfprNetworkLocale
_CfprEtherFtwPortPairLocale_Object = MibTableColumn
cfprEtherFtwPortPairLocale = _CfprEtherFtwPortPairLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 19),
    _CfprEtherFtwPortPairLocale_Type()
)
cfprEtherFtwPortPairLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairLocale.setStatus("current")
_CfprEtherFtwPortPairMode_Type = CfprEtherFtwPortPairMode
_CfprEtherFtwPortPairMode_Object = MibTableColumn
cfprEtherFtwPortPairMode = _CfprEtherFtwPortPairMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 20),
    _CfprEtherFtwPortPairMode_Type()
)
cfprEtherFtwPortPairMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairMode.setStatus("current")
_CfprEtherFtwPortPairName_Type = SnmpAdminString
_CfprEtherFtwPortPairName_Object = MibTableColumn
cfprEtherFtwPortPairName = _CfprEtherFtwPortPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 21),
    _CfprEtherFtwPortPairName_Type()
)
cfprEtherFtwPortPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairName.setStatus("current")
_CfprEtherFtwPortPairOperMode_Type = CfprEtherFtwOperMode
_CfprEtherFtwPortPairOperMode_Object = MibTableColumn
cfprEtherFtwPortPairOperMode = _CfprEtherFtwPortPairOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 22),
    _CfprEtherFtwPortPairOperMode_Type()
)
cfprEtherFtwPortPairOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairOperMode.setStatus("current")
_CfprEtherFtwPortPairPeerAggrPortId_Type = Gauge32
_CfprEtherFtwPortPairPeerAggrPortId_Object = MibTableColumn
cfprEtherFtwPortPairPeerAggrPortId = _CfprEtherFtwPortPairPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 23),
    _CfprEtherFtwPortPairPeerAggrPortId_Type()
)
cfprEtherFtwPortPairPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPeerAggrPortId.setStatus("current")
_CfprEtherFtwPortPairPeerChassisId_Type = Gauge32
_CfprEtherFtwPortPairPeerChassisId_Object = MibTableColumn
cfprEtherFtwPortPairPeerChassisId = _CfprEtherFtwPortPairPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 24),
    _CfprEtherFtwPortPairPeerChassisId_Type()
)
cfprEtherFtwPortPairPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPeerChassisId.setStatus("current")
_CfprEtherFtwPortPairPeerDn_Type = SnmpAdminString
_CfprEtherFtwPortPairPeerDn_Object = MibTableColumn
cfprEtherFtwPortPairPeerDn = _CfprEtherFtwPortPairPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 25),
    _CfprEtherFtwPortPairPeerDn_Type()
)
cfprEtherFtwPortPairPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPeerDn.setStatus("current")
_CfprEtherFtwPortPairPeerPortId_Type = Gauge32
_CfprEtherFtwPortPairPeerPortId_Object = MibTableColumn
cfprEtherFtwPortPairPeerPortId = _CfprEtherFtwPortPairPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 26),
    _CfprEtherFtwPortPairPeerPortId_Type()
)
cfprEtherFtwPortPairPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPeerPortId.setStatus("current")
_CfprEtherFtwPortPairPeerPortName_Type = SnmpAdminString
_CfprEtherFtwPortPairPeerPortName_Object = MibTableColumn
cfprEtherFtwPortPairPeerPortName = _CfprEtherFtwPortPairPeerPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 27),
    _CfprEtherFtwPortPairPeerPortName_Type()
)
cfprEtherFtwPortPairPeerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPeerPortName.setStatus("current")
_CfprEtherFtwPortPairPeerSlotId_Type = Gauge32
_CfprEtherFtwPortPairPeerSlotId_Object = MibTableColumn
cfprEtherFtwPortPairPeerSlotId = _CfprEtherFtwPortPairPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 28),
    _CfprEtherFtwPortPairPeerSlotId_Type()
)
cfprEtherFtwPortPairPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPeerSlotId.setStatus("current")
_CfprEtherFtwPortPairPortId_Type = Gauge32
_CfprEtherFtwPortPairPortId_Object = MibTableColumn
cfprEtherFtwPortPairPortId = _CfprEtherFtwPortPairPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 29),
    _CfprEtherFtwPortPairPortId_Type()
)
cfprEtherFtwPortPairPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPortId.setStatus("current")
_CfprEtherFtwPortPairPortName_Type = SnmpAdminString
_CfprEtherFtwPortPairPortName_Object = MibTableColumn
cfprEtherFtwPortPairPortName = _CfprEtherFtwPortPairPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 30),
    _CfprEtherFtwPortPairPortName_Type()
)
cfprEtherFtwPortPairPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairPortName.setStatus("current")
_CfprEtherFtwPortPairSlotId_Type = Gauge32
_CfprEtherFtwPortPairSlotId_Object = MibTableColumn
cfprEtherFtwPortPairSlotId = _CfprEtherFtwPortPairSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 31),
    _CfprEtherFtwPortPairSlotId_Type()
)
cfprEtherFtwPortPairSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairSlotId.setStatus("current")
_CfprEtherFtwPortPairSwitchId_Type = CfprNetworkSwitchId
_CfprEtherFtwPortPairSwitchId_Object = MibTableColumn
cfprEtherFtwPortPairSwitchId = _CfprEtherFtwPortPairSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 32),
    _CfprEtherFtwPortPairSwitchId_Type()
)
cfprEtherFtwPortPairSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairSwitchId.setStatus("current")
_CfprEtherFtwPortPairTransport_Type = CfprNetworkTransport
_CfprEtherFtwPortPairTransport_Object = MibTableColumn
cfprEtherFtwPortPairTransport = _CfprEtherFtwPortPairTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 33),
    _CfprEtherFtwPortPairTransport_Type()
)
cfprEtherFtwPortPairTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairTransport.setStatus("current")
_CfprEtherFtwPortPairTs_Type = DateAndTime
_CfprEtherFtwPortPairTs_Object = MibTableColumn
cfprEtherFtwPortPairTs = _CfprEtherFtwPortPairTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 34),
    _CfprEtherFtwPortPairTs_Type()
)
cfprEtherFtwPortPairTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairTs.setStatus("current")
_CfprEtherFtwPortPairType_Type = CfprNetworkConnectionType
_CfprEtherFtwPortPairType_Object = MibTableColumn
cfprEtherFtwPortPairType = _CfprEtherFtwPortPairType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 35),
    _CfprEtherFtwPortPairType_Type()
)
cfprEtherFtwPortPairType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairType.setStatus("current")
_CfprEtherFtwPortPairWdtStart_Type = Gauge32
_CfprEtherFtwPortPairWdtStart_Object = MibTableColumn
cfprEtherFtwPortPairWdtStart = _CfprEtherFtwPortPairWdtStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 36),
    _CfprEtherFtwPortPairWdtStart_Type()
)
cfprEtherFtwPortPairWdtStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairWdtStart.setStatus("current")
_CfprEtherFtwPortPairWdtState_Type = CfprEtherFtwPortPairWdtState
_CfprEtherFtwPortPairWdtState_Object = MibTableColumn
cfprEtherFtwPortPairWdtState = _CfprEtherFtwPortPairWdtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 33, 1, 37),
    _CfprEtherFtwPortPairWdtState_Type()
)
cfprEtherFtwPortPairWdtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairWdtState.setStatus("current")
_CfprEtherFtwPortPairFsmTable_Object = MibTable
cfprEtherFtwPortPairFsmTable = _CfprEtherFtwPortPairFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34)
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTable.setStatus("current")
_CfprEtherFtwPortPairFsmEntry_Object = MibTableRow
cfprEtherFtwPortPairFsmEntry = _CfprEtherFtwPortPairFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1)
)
cfprEtherFtwPortPairFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFtwPortPairFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmEntry.setStatus("current")
_CfprEtherFtwPortPairFsmInstanceId_Type = CfprManagedObjectId
_CfprEtherFtwPortPairFsmInstanceId_Object = MibTableColumn
cfprEtherFtwPortPairFsmInstanceId = _CfprEtherFtwPortPairFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 1),
    _CfprEtherFtwPortPairFsmInstanceId_Type()
)
cfprEtherFtwPortPairFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmInstanceId.setStatus("current")
_CfprEtherFtwPortPairFsmDn_Type = CfprManagedObjectDn
_CfprEtherFtwPortPairFsmDn_Object = MibTableColumn
cfprEtherFtwPortPairFsmDn = _CfprEtherFtwPortPairFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 2),
    _CfprEtherFtwPortPairFsmDn_Type()
)
cfprEtherFtwPortPairFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmDn.setStatus("current")
_CfprEtherFtwPortPairFsmRn_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmRn_Object = MibTableColumn
cfprEtherFtwPortPairFsmRn = _CfprEtherFtwPortPairFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 3),
    _CfprEtherFtwPortPairFsmRn_Type()
)
cfprEtherFtwPortPairFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRn.setStatus("current")
_CfprEtherFtwPortPairFsmCompletionTime_Type = DateAndTime
_CfprEtherFtwPortPairFsmCompletionTime_Object = MibTableColumn
cfprEtherFtwPortPairFsmCompletionTime = _CfprEtherFtwPortPairFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 4),
    _CfprEtherFtwPortPairFsmCompletionTime_Type()
)
cfprEtherFtwPortPairFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmCompletionTime.setStatus("current")
_CfprEtherFtwPortPairFsmCurrentFsm_Type = CfprEtherFtwPortPairFsmCurrentFsm
_CfprEtherFtwPortPairFsmCurrentFsm_Object = MibTableColumn
cfprEtherFtwPortPairFsmCurrentFsm = _CfprEtherFtwPortPairFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 5),
    _CfprEtherFtwPortPairFsmCurrentFsm_Type()
)
cfprEtherFtwPortPairFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmCurrentFsm.setStatus("current")
_CfprEtherFtwPortPairFsmDescrData_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmDescrData_Object = MibTableColumn
cfprEtherFtwPortPairFsmDescrData = _CfprEtherFtwPortPairFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 6),
    _CfprEtherFtwPortPairFsmDescrData_Type()
)
cfprEtherFtwPortPairFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmDescrData.setStatus("current")
_CfprEtherFtwPortPairFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprEtherFtwPortPairFsmFsmStatus_Object = MibTableColumn
cfprEtherFtwPortPairFsmFsmStatus = _CfprEtherFtwPortPairFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 7),
    _CfprEtherFtwPortPairFsmFsmStatus_Type()
)
cfprEtherFtwPortPairFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmFsmStatus.setStatus("current")
_CfprEtherFtwPortPairFsmProgress_Type = Gauge32
_CfprEtherFtwPortPairFsmProgress_Object = MibTableColumn
cfprEtherFtwPortPairFsmProgress = _CfprEtherFtwPortPairFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 8),
    _CfprEtherFtwPortPairFsmProgress_Type()
)
cfprEtherFtwPortPairFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmProgress.setStatus("current")
_CfprEtherFtwPortPairFsmRmtErrCode_Type = Gauge32
_CfprEtherFtwPortPairFsmRmtErrCode_Object = MibTableColumn
cfprEtherFtwPortPairFsmRmtErrCode = _CfprEtherFtwPortPairFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 9),
    _CfprEtherFtwPortPairFsmRmtErrCode_Type()
)
cfprEtherFtwPortPairFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRmtErrCode.setStatus("current")
_CfprEtherFtwPortPairFsmRmtErrDescr_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmRmtErrDescr_Object = MibTableColumn
cfprEtherFtwPortPairFsmRmtErrDescr = _CfprEtherFtwPortPairFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 10),
    _CfprEtherFtwPortPairFsmRmtErrDescr_Type()
)
cfprEtherFtwPortPairFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRmtErrDescr.setStatus("current")
_CfprEtherFtwPortPairFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprEtherFtwPortPairFsmRmtRslt_Object = MibTableColumn
cfprEtherFtwPortPairFsmRmtRslt = _CfprEtherFtwPortPairFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 34, 1, 11),
    _CfprEtherFtwPortPairFsmRmtRslt_Type()
)
cfprEtherFtwPortPairFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmRmtRslt.setStatus("current")
_CfprEtherFtwPortPairFsmStageTable_Object = MibTable
cfprEtherFtwPortPairFsmStageTable = _CfprEtherFtwPortPairFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35)
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageTable.setStatus("current")
_CfprEtherFtwPortPairFsmStageEntry_Object = MibTableRow
cfprEtherFtwPortPairFsmStageEntry = _CfprEtherFtwPortPairFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1)
)
cfprEtherFtwPortPairFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFtwPortPairFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageEntry.setStatus("current")
_CfprEtherFtwPortPairFsmStageInstanceId_Type = CfprManagedObjectId
_CfprEtherFtwPortPairFsmStageInstanceId_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageInstanceId = _CfprEtherFtwPortPairFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 1),
    _CfprEtherFtwPortPairFsmStageInstanceId_Type()
)
cfprEtherFtwPortPairFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageInstanceId.setStatus("current")
_CfprEtherFtwPortPairFsmStageDn_Type = CfprManagedObjectDn
_CfprEtherFtwPortPairFsmStageDn_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageDn = _CfprEtherFtwPortPairFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 2),
    _CfprEtherFtwPortPairFsmStageDn_Type()
)
cfprEtherFtwPortPairFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageDn.setStatus("current")
_CfprEtherFtwPortPairFsmStageRn_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmStageRn_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageRn = _CfprEtherFtwPortPairFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 3),
    _CfprEtherFtwPortPairFsmStageRn_Type()
)
cfprEtherFtwPortPairFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageRn.setStatus("current")
_CfprEtherFtwPortPairFsmStageDescrData_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmStageDescrData_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageDescrData = _CfprEtherFtwPortPairFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 4),
    _CfprEtherFtwPortPairFsmStageDescrData_Type()
)
cfprEtherFtwPortPairFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageDescrData.setStatus("current")
_CfprEtherFtwPortPairFsmStageLastUpdateTime_Type = DateAndTime
_CfprEtherFtwPortPairFsmStageLastUpdateTime_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageLastUpdateTime = _CfprEtherFtwPortPairFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 5),
    _CfprEtherFtwPortPairFsmStageLastUpdateTime_Type()
)
cfprEtherFtwPortPairFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageLastUpdateTime.setStatus("current")
_CfprEtherFtwPortPairFsmStageName_Type = CfprEtherFtwPortPairFsmStageName
_CfprEtherFtwPortPairFsmStageName_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageName = _CfprEtherFtwPortPairFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 6),
    _CfprEtherFtwPortPairFsmStageName_Type()
)
cfprEtherFtwPortPairFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageName.setStatus("current")
_CfprEtherFtwPortPairFsmStageOrder_Type = Gauge32
_CfprEtherFtwPortPairFsmStageOrder_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageOrder = _CfprEtherFtwPortPairFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 7),
    _CfprEtherFtwPortPairFsmStageOrder_Type()
)
cfprEtherFtwPortPairFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageOrder.setStatus("current")
_CfprEtherFtwPortPairFsmStageRetry_Type = Gauge32
_CfprEtherFtwPortPairFsmStageRetry_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageRetry = _CfprEtherFtwPortPairFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 8),
    _CfprEtherFtwPortPairFsmStageRetry_Type()
)
cfprEtherFtwPortPairFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageRetry.setStatus("current")
_CfprEtherFtwPortPairFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprEtherFtwPortPairFsmStageStageStatus_Object = MibTableColumn
cfprEtherFtwPortPairFsmStageStageStatus = _CfprEtherFtwPortPairFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 35, 1, 9),
    _CfprEtherFtwPortPairFsmStageStageStatus_Type()
)
cfprEtherFtwPortPairFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmStageStageStatus.setStatus("current")
_CfprEtherFtwPortPairFsmTaskTable_Object = MibTable
cfprEtherFtwPortPairFsmTaskTable = _CfprEtherFtwPortPairFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36)
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskTable.setStatus("current")
_CfprEtherFtwPortPairFsmTaskEntry_Object = MibTableRow
cfprEtherFtwPortPairFsmTaskEntry = _CfprEtherFtwPortPairFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1)
)
cfprEtherFtwPortPairFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-ETHER-MIB", "cfprEtherFtwPortPairFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskEntry.setStatus("current")
_CfprEtherFtwPortPairFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprEtherFtwPortPairFsmTaskInstanceId_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskInstanceId = _CfprEtherFtwPortPairFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 1),
    _CfprEtherFtwPortPairFsmTaskInstanceId_Type()
)
cfprEtherFtwPortPairFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskInstanceId.setStatus("current")
_CfprEtherFtwPortPairFsmTaskDn_Type = CfprManagedObjectDn
_CfprEtherFtwPortPairFsmTaskDn_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskDn = _CfprEtherFtwPortPairFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 2),
    _CfprEtherFtwPortPairFsmTaskDn_Type()
)
cfprEtherFtwPortPairFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskDn.setStatus("current")
_CfprEtherFtwPortPairFsmTaskRn_Type = SnmpAdminString
_CfprEtherFtwPortPairFsmTaskRn_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskRn = _CfprEtherFtwPortPairFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 3),
    _CfprEtherFtwPortPairFsmTaskRn_Type()
)
cfprEtherFtwPortPairFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskRn.setStatus("current")
_CfprEtherFtwPortPairFsmTaskCompletion_Type = CfprFsmCompletion
_CfprEtherFtwPortPairFsmTaskCompletion_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskCompletion = _CfprEtherFtwPortPairFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 4),
    _CfprEtherFtwPortPairFsmTaskCompletion_Type()
)
cfprEtherFtwPortPairFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskCompletion.setStatus("current")
_CfprEtherFtwPortPairFsmTaskFlags_Type = CfprFsmFlags
_CfprEtherFtwPortPairFsmTaskFlags_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskFlags = _CfprEtherFtwPortPairFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 5),
    _CfprEtherFtwPortPairFsmTaskFlags_Type()
)
cfprEtherFtwPortPairFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskFlags.setStatus("current")
_CfprEtherFtwPortPairFsmTaskItem_Type = CfprEtherFtwPortPairFsmTaskItem
_CfprEtherFtwPortPairFsmTaskItem_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskItem = _CfprEtherFtwPortPairFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 6),
    _CfprEtherFtwPortPairFsmTaskItem_Type()
)
cfprEtherFtwPortPairFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskItem.setStatus("current")
_CfprEtherFtwPortPairFsmTaskSeqId_Type = Gauge32
_CfprEtherFtwPortPairFsmTaskSeqId_Object = MibTableColumn
cfprEtherFtwPortPairFsmTaskSeqId = _CfprEtherFtwPortPairFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 21, 36, 1, 7),
    _CfprEtherFtwPortPairFsmTaskSeqId_Type()
)
cfprEtherFtwPortPairFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEtherFtwPortPairFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-ETHER-MIB",
    **{"cfprEtherObjects": cfprEtherObjects,
       "cfprEtherErrStatsTable": cfprEtherErrStatsTable,
       "cfprEtherErrStatsEntry": cfprEtherErrStatsEntry,
       "cfprEtherErrStatsInstanceId": cfprEtherErrStatsInstanceId,
       "cfprEtherErrStatsDn": cfprEtherErrStatsDn,
       "cfprEtherErrStatsRn": cfprEtherErrStatsRn,
       "cfprEtherErrStatsAlign": cfprEtherErrStatsAlign,
       "cfprEtherErrStatsAlignDelta": cfprEtherErrStatsAlignDelta,
       "cfprEtherErrStatsAlignDeltaAvg": cfprEtherErrStatsAlignDeltaAvg,
       "cfprEtherErrStatsAlignDeltaMax": cfprEtherErrStatsAlignDeltaMax,
       "cfprEtherErrStatsAlignDeltaMin": cfprEtherErrStatsAlignDeltaMin,
       "cfprEtherErrStatsDeferredTx": cfprEtherErrStatsDeferredTx,
       "cfprEtherErrStatsDeferredTxDelta": cfprEtherErrStatsDeferredTxDelta,
       "cfprEtherErrStatsDeferredTxDeltaAvg": cfprEtherErrStatsDeferredTxDeltaAvg,
       "cfprEtherErrStatsDeferredTxDeltaMax": cfprEtherErrStatsDeferredTxDeltaMax,
       "cfprEtherErrStatsDeferredTxDeltaMin": cfprEtherErrStatsDeferredTxDeltaMin,
       "cfprEtherErrStatsFcs": cfprEtherErrStatsFcs,
       "cfprEtherErrStatsFcsDelta": cfprEtherErrStatsFcsDelta,
       "cfprEtherErrStatsFcsDeltaAvg": cfprEtherErrStatsFcsDeltaAvg,
       "cfprEtherErrStatsFcsDeltaMax": cfprEtherErrStatsFcsDeltaMax,
       "cfprEtherErrStatsFcsDeltaMin": cfprEtherErrStatsFcsDeltaMin,
       "cfprEtherErrStatsIntMacRx": cfprEtherErrStatsIntMacRx,
       "cfprEtherErrStatsIntMacRxDelta": cfprEtherErrStatsIntMacRxDelta,
       "cfprEtherErrStatsIntMacRxDeltaAvg": cfprEtherErrStatsIntMacRxDeltaAvg,
       "cfprEtherErrStatsIntMacRxDeltaMax": cfprEtherErrStatsIntMacRxDeltaMax,
       "cfprEtherErrStatsIntMacRxDeltaMin": cfprEtherErrStatsIntMacRxDeltaMin,
       "cfprEtherErrStatsIntMacTx": cfprEtherErrStatsIntMacTx,
       "cfprEtherErrStatsIntMacTxDelta": cfprEtherErrStatsIntMacTxDelta,
       "cfprEtherErrStatsIntMacTxDeltaAvg": cfprEtherErrStatsIntMacTxDeltaAvg,
       "cfprEtherErrStatsIntMacTxDeltaMax": cfprEtherErrStatsIntMacTxDeltaMax,
       "cfprEtherErrStatsIntMacTxDeltaMin": cfprEtherErrStatsIntMacTxDeltaMin,
       "cfprEtherErrStatsIntervals": cfprEtherErrStatsIntervals,
       "cfprEtherErrStatsOutDiscard": cfprEtherErrStatsOutDiscard,
       "cfprEtherErrStatsOutDiscardDelta": cfprEtherErrStatsOutDiscardDelta,
       "cfprEtherErrStatsOutDiscardDeltaAvg": cfprEtherErrStatsOutDiscardDeltaAvg,
       "cfprEtherErrStatsOutDiscardDeltaMax": cfprEtherErrStatsOutDiscardDeltaMax,
       "cfprEtherErrStatsOutDiscardDeltaMin": cfprEtherErrStatsOutDiscardDeltaMin,
       "cfprEtherErrStatsRcv": cfprEtherErrStatsRcv,
       "cfprEtherErrStatsRcvDelta": cfprEtherErrStatsRcvDelta,
       "cfprEtherErrStatsRcvDeltaAvg": cfprEtherErrStatsRcvDeltaAvg,
       "cfprEtherErrStatsRcvDeltaMax": cfprEtherErrStatsRcvDeltaMax,
       "cfprEtherErrStatsRcvDeltaMin": cfprEtherErrStatsRcvDeltaMin,
       "cfprEtherErrStatsSuspect": cfprEtherErrStatsSuspect,
       "cfprEtherErrStatsThresholded": cfprEtherErrStatsThresholded,
       "cfprEtherErrStatsTimeCollected": cfprEtherErrStatsTimeCollected,
       "cfprEtherErrStatsUnderSize": cfprEtherErrStatsUnderSize,
       "cfprEtherErrStatsUnderSizeDelta": cfprEtherErrStatsUnderSizeDelta,
       "cfprEtherErrStatsUnderSizeDeltaAvg": cfprEtherErrStatsUnderSizeDeltaAvg,
       "cfprEtherErrStatsUnderSizeDeltaMax": cfprEtherErrStatsUnderSizeDeltaMax,
       "cfprEtherErrStatsUnderSizeDeltaMin": cfprEtherErrStatsUnderSizeDeltaMin,
       "cfprEtherErrStatsUpdate": cfprEtherErrStatsUpdate,
       "cfprEtherErrStatsXmit": cfprEtherErrStatsXmit,
       "cfprEtherErrStatsXmitDelta": cfprEtherErrStatsXmitDelta,
       "cfprEtherErrStatsXmitDeltaAvg": cfprEtherErrStatsXmitDeltaAvg,
       "cfprEtherErrStatsXmitDeltaMax": cfprEtherErrStatsXmitDeltaMax,
       "cfprEtherErrStatsXmitDeltaMin": cfprEtherErrStatsXmitDeltaMin,
       "cfprEtherErrStatsHistTable": cfprEtherErrStatsHistTable,
       "cfprEtherErrStatsHistEntry": cfprEtherErrStatsHistEntry,
       "cfprEtherErrStatsHistInstanceId": cfprEtherErrStatsHistInstanceId,
       "cfprEtherErrStatsHistDn": cfprEtherErrStatsHistDn,
       "cfprEtherErrStatsHistRn": cfprEtherErrStatsHistRn,
       "cfprEtherErrStatsHistAlign": cfprEtherErrStatsHistAlign,
       "cfprEtherErrStatsHistAlignDelta": cfprEtherErrStatsHistAlignDelta,
       "cfprEtherErrStatsHistAlignDeltaAvg": cfprEtherErrStatsHistAlignDeltaAvg,
       "cfprEtherErrStatsHistAlignDeltaMax": cfprEtherErrStatsHistAlignDeltaMax,
       "cfprEtherErrStatsHistAlignDeltaMin": cfprEtherErrStatsHistAlignDeltaMin,
       "cfprEtherErrStatsHistDeferredTx": cfprEtherErrStatsHistDeferredTx,
       "cfprEtherErrStatsHistDeferredTxDelta": cfprEtherErrStatsHistDeferredTxDelta,
       "cfprEtherErrStatsHistDeferredTxDeltaAvg": cfprEtherErrStatsHistDeferredTxDeltaAvg,
       "cfprEtherErrStatsHistDeferredTxDeltaMax": cfprEtherErrStatsHistDeferredTxDeltaMax,
       "cfprEtherErrStatsHistDeferredTxDeltaMin": cfprEtherErrStatsHistDeferredTxDeltaMin,
       "cfprEtherErrStatsHistFcs": cfprEtherErrStatsHistFcs,
       "cfprEtherErrStatsHistFcsDelta": cfprEtherErrStatsHistFcsDelta,
       "cfprEtherErrStatsHistFcsDeltaAvg": cfprEtherErrStatsHistFcsDeltaAvg,
       "cfprEtherErrStatsHistFcsDeltaMax": cfprEtherErrStatsHistFcsDeltaMax,
       "cfprEtherErrStatsHistFcsDeltaMin": cfprEtherErrStatsHistFcsDeltaMin,
       "cfprEtherErrStatsHistId": cfprEtherErrStatsHistId,
       "cfprEtherErrStatsHistIntMacRx": cfprEtherErrStatsHistIntMacRx,
       "cfprEtherErrStatsHistIntMacRxDelta": cfprEtherErrStatsHistIntMacRxDelta,
       "cfprEtherErrStatsHistIntMacRxDeltaAvg": cfprEtherErrStatsHistIntMacRxDeltaAvg,
       "cfprEtherErrStatsHistIntMacRxDeltaMax": cfprEtherErrStatsHistIntMacRxDeltaMax,
       "cfprEtherErrStatsHistIntMacRxDeltaMin": cfprEtherErrStatsHistIntMacRxDeltaMin,
       "cfprEtherErrStatsHistIntMacTx": cfprEtherErrStatsHistIntMacTx,
       "cfprEtherErrStatsHistIntMacTxDelta": cfprEtherErrStatsHistIntMacTxDelta,
       "cfprEtherErrStatsHistIntMacTxDeltaAvg": cfprEtherErrStatsHistIntMacTxDeltaAvg,
       "cfprEtherErrStatsHistIntMacTxDeltaMax": cfprEtherErrStatsHistIntMacTxDeltaMax,
       "cfprEtherErrStatsHistIntMacTxDeltaMin": cfprEtherErrStatsHistIntMacTxDeltaMin,
       "cfprEtherErrStatsHistMostRecent": cfprEtherErrStatsHistMostRecent,
       "cfprEtherErrStatsHistOutDiscard": cfprEtherErrStatsHistOutDiscard,
       "cfprEtherErrStatsHistOutDiscardDelta": cfprEtherErrStatsHistOutDiscardDelta,
       "cfprEtherErrStatsHistOutDiscardDeltaAvg": cfprEtherErrStatsHistOutDiscardDeltaAvg,
       "cfprEtherErrStatsHistOutDiscardDeltaMax": cfprEtherErrStatsHistOutDiscardDeltaMax,
       "cfprEtherErrStatsHistOutDiscardDeltaMin": cfprEtherErrStatsHistOutDiscardDeltaMin,
       "cfprEtherErrStatsHistRcv": cfprEtherErrStatsHistRcv,
       "cfprEtherErrStatsHistRcvDelta": cfprEtherErrStatsHistRcvDelta,
       "cfprEtherErrStatsHistRcvDeltaAvg": cfprEtherErrStatsHistRcvDeltaAvg,
       "cfprEtherErrStatsHistRcvDeltaMax": cfprEtherErrStatsHistRcvDeltaMax,
       "cfprEtherErrStatsHistRcvDeltaMin": cfprEtherErrStatsHistRcvDeltaMin,
       "cfprEtherErrStatsHistSuspect": cfprEtherErrStatsHistSuspect,
       "cfprEtherErrStatsHistThresholded": cfprEtherErrStatsHistThresholded,
       "cfprEtherErrStatsHistTimeCollected": cfprEtherErrStatsHistTimeCollected,
       "cfprEtherErrStatsHistUnderSize": cfprEtherErrStatsHistUnderSize,
       "cfprEtherErrStatsHistUnderSizeDelta": cfprEtherErrStatsHistUnderSizeDelta,
       "cfprEtherErrStatsHistUnderSizeDeltaAvg": cfprEtherErrStatsHistUnderSizeDeltaAvg,
       "cfprEtherErrStatsHistUnderSizeDeltaMax": cfprEtherErrStatsHistUnderSizeDeltaMax,
       "cfprEtherErrStatsHistUnderSizeDeltaMin": cfprEtherErrStatsHistUnderSizeDeltaMin,
       "cfprEtherErrStatsHistXmit": cfprEtherErrStatsHistXmit,
       "cfprEtherErrStatsHistXmitDelta": cfprEtherErrStatsHistXmitDelta,
       "cfprEtherErrStatsHistXmitDeltaAvg": cfprEtherErrStatsHistXmitDeltaAvg,
       "cfprEtherErrStatsHistXmitDeltaMax": cfprEtherErrStatsHistXmitDeltaMax,
       "cfprEtherErrStatsHistXmitDeltaMin": cfprEtherErrStatsHistXmitDeltaMin,
       "cfprEtherFcoeInterfaceStatsTable": cfprEtherFcoeInterfaceStatsTable,
       "cfprEtherFcoeInterfaceStatsEntry": cfprEtherFcoeInterfaceStatsEntry,
       "cfprEtherFcoeInterfaceStatsInstanceId": cfprEtherFcoeInterfaceStatsInstanceId,
       "cfprEtherFcoeInterfaceStatsDn": cfprEtherFcoeInterfaceStatsDn,
       "cfprEtherFcoeInterfaceStatsRn": cfprEtherFcoeInterfaceStatsRn,
       "cfprEtherFcoeInterfaceStatsBytesRx": cfprEtherFcoeInterfaceStatsBytesRx,
       "cfprEtherFcoeInterfaceStatsBytesRxDelta": cfprEtherFcoeInterfaceStatsBytesRxDelta,
       "cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg": cfprEtherFcoeInterfaceStatsBytesRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsBytesRxDeltaMax": cfprEtherFcoeInterfaceStatsBytesRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsBytesRxDeltaMin": cfprEtherFcoeInterfaceStatsBytesRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsBytesTx": cfprEtherFcoeInterfaceStatsBytesTx,
       "cfprEtherFcoeInterfaceStatsBytesTxDelta": cfprEtherFcoeInterfaceStatsBytesTxDelta,
       "cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg": cfprEtherFcoeInterfaceStatsBytesTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsBytesTxDeltaMax": cfprEtherFcoeInterfaceStatsBytesTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsBytesTxDeltaMin": cfprEtherFcoeInterfaceStatsBytesTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsDroppedRx": cfprEtherFcoeInterfaceStatsDroppedRx,
       "cfprEtherFcoeInterfaceStatsDroppedRxDelta": cfprEtherFcoeInterfaceStatsDroppedRxDelta,
       "cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg": cfprEtherFcoeInterfaceStatsDroppedRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax": cfprEtherFcoeInterfaceStatsDroppedRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin": cfprEtherFcoeInterfaceStatsDroppedRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsDroppedTx": cfprEtherFcoeInterfaceStatsDroppedTx,
       "cfprEtherFcoeInterfaceStatsDroppedTxDelta": cfprEtherFcoeInterfaceStatsDroppedTxDelta,
       "cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg": cfprEtherFcoeInterfaceStatsDroppedTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax": cfprEtherFcoeInterfaceStatsDroppedTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin": cfprEtherFcoeInterfaceStatsDroppedTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsErrorsRx": cfprEtherFcoeInterfaceStatsErrorsRx,
       "cfprEtherFcoeInterfaceStatsErrorsRxDelta": cfprEtherFcoeInterfaceStatsErrorsRxDelta,
       "cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg": cfprEtherFcoeInterfaceStatsErrorsRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax": cfprEtherFcoeInterfaceStatsErrorsRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin": cfprEtherFcoeInterfaceStatsErrorsRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsErrorsTx": cfprEtherFcoeInterfaceStatsErrorsTx,
       "cfprEtherFcoeInterfaceStatsErrorsTxDelta": cfprEtherFcoeInterfaceStatsErrorsTxDelta,
       "cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg": cfprEtherFcoeInterfaceStatsErrorsTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax": cfprEtherFcoeInterfaceStatsErrorsTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin": cfprEtherFcoeInterfaceStatsErrorsTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsIntervals": cfprEtherFcoeInterfaceStatsIntervals,
       "cfprEtherFcoeInterfaceStatsPacketsRx": cfprEtherFcoeInterfaceStatsPacketsRx,
       "cfprEtherFcoeInterfaceStatsPacketsRxDelta": cfprEtherFcoeInterfaceStatsPacketsRxDelta,
       "cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg": cfprEtherFcoeInterfaceStatsPacketsRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax": cfprEtherFcoeInterfaceStatsPacketsRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin": cfprEtherFcoeInterfaceStatsPacketsRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsPacketsTx": cfprEtherFcoeInterfaceStatsPacketsTx,
       "cfprEtherFcoeInterfaceStatsPacketsTxDelta": cfprEtherFcoeInterfaceStatsPacketsTxDelta,
       "cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg": cfprEtherFcoeInterfaceStatsPacketsTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax": cfprEtherFcoeInterfaceStatsPacketsTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin": cfprEtherFcoeInterfaceStatsPacketsTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsSuspect": cfprEtherFcoeInterfaceStatsSuspect,
       "cfprEtherFcoeInterfaceStatsThresholded": cfprEtherFcoeInterfaceStatsThresholded,
       "cfprEtherFcoeInterfaceStatsTimeCollected": cfprEtherFcoeInterfaceStatsTimeCollected,
       "cfprEtherFcoeInterfaceStatsUpdate": cfprEtherFcoeInterfaceStatsUpdate,
       "cfprEtherFcoeInterfaceStatsHistTable": cfprEtherFcoeInterfaceStatsHistTable,
       "cfprEtherFcoeInterfaceStatsHistEntry": cfprEtherFcoeInterfaceStatsHistEntry,
       "cfprEtherFcoeInterfaceStatsHistInstanceId": cfprEtherFcoeInterfaceStatsHistInstanceId,
       "cfprEtherFcoeInterfaceStatsHistDn": cfprEtherFcoeInterfaceStatsHistDn,
       "cfprEtherFcoeInterfaceStatsHistRn": cfprEtherFcoeInterfaceStatsHistRn,
       "cfprEtherFcoeInterfaceStatsHistBytesRx": cfprEtherFcoeInterfaceStatsHistBytesRx,
       "cfprEtherFcoeInterfaceStatsHistBytesRxDelta": cfprEtherFcoeInterfaceStatsHistBytesRxDelta,
       "cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg": cfprEtherFcoeInterfaceStatsHistBytesRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax": cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin": cfprEtherFcoeInterfaceStatsHistBytesRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistBytesTx": cfprEtherFcoeInterfaceStatsHistBytesTx,
       "cfprEtherFcoeInterfaceStatsHistBytesTxDelta": cfprEtherFcoeInterfaceStatsHistBytesTxDelta,
       "cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg": cfprEtherFcoeInterfaceStatsHistBytesTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax": cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin": cfprEtherFcoeInterfaceStatsHistBytesTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistDroppedRx": cfprEtherFcoeInterfaceStatsHistDroppedRx,
       "cfprEtherFcoeInterfaceStatsHistDroppedRxDelta": cfprEtherFcoeInterfaceStatsHistDroppedRxDelta,
       "cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg": cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax": cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin": cfprEtherFcoeInterfaceStatsHistDroppedRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistDroppedTx": cfprEtherFcoeInterfaceStatsHistDroppedTx,
       "cfprEtherFcoeInterfaceStatsHistDroppedTxDelta": cfprEtherFcoeInterfaceStatsHistDroppedTxDelta,
       "cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg": cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax": cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin": cfprEtherFcoeInterfaceStatsHistDroppedTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistErrorsRx": cfprEtherFcoeInterfaceStatsHistErrorsRx,
       "cfprEtherFcoeInterfaceStatsHistErrorsRxDelta": cfprEtherFcoeInterfaceStatsHistErrorsRxDelta,
       "cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg": cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax": cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin": cfprEtherFcoeInterfaceStatsHistErrorsRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistErrorsTx": cfprEtherFcoeInterfaceStatsHistErrorsTx,
       "cfprEtherFcoeInterfaceStatsHistErrorsTxDelta": cfprEtherFcoeInterfaceStatsHistErrorsTxDelta,
       "cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg": cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax": cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin": cfprEtherFcoeInterfaceStatsHistErrorsTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistId": cfprEtherFcoeInterfaceStatsHistId,
       "cfprEtherFcoeInterfaceStatsHistMostRecent": cfprEtherFcoeInterfaceStatsHistMostRecent,
       "cfprEtherFcoeInterfaceStatsHistPacketsRx": cfprEtherFcoeInterfaceStatsHistPacketsRx,
       "cfprEtherFcoeInterfaceStatsHistPacketsRxDelta": cfprEtherFcoeInterfaceStatsHistPacketsRxDelta,
       "cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg": cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax": cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin": cfprEtherFcoeInterfaceStatsHistPacketsRxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistPacketsTx": cfprEtherFcoeInterfaceStatsHistPacketsTx,
       "cfprEtherFcoeInterfaceStatsHistPacketsTxDelta": cfprEtherFcoeInterfaceStatsHistPacketsTxDelta,
       "cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg": cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg,
       "cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax": cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMax,
       "cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin": cfprEtherFcoeInterfaceStatsHistPacketsTxDeltaMin,
       "cfprEtherFcoeInterfaceStatsHistSuspect": cfprEtherFcoeInterfaceStatsHistSuspect,
       "cfprEtherFcoeInterfaceStatsHistThresholded": cfprEtherFcoeInterfaceStatsHistThresholded,
       "cfprEtherFcoeInterfaceStatsHistTimeCollected": cfprEtherFcoeInterfaceStatsHistTimeCollected,
       "cfprEtherLossStatsTable": cfprEtherLossStatsTable,
       "cfprEtherLossStatsEntry": cfprEtherLossStatsEntry,
       "cfprEtherLossStatsInstanceId": cfprEtherLossStatsInstanceId,
       "cfprEtherLossStatsDn": cfprEtherLossStatsDn,
       "cfprEtherLossStatsRn": cfprEtherLossStatsRn,
       "cfprEtherLossStatsSQETest": cfprEtherLossStatsSQETest,
       "cfprEtherLossStatsSQETestDelta": cfprEtherLossStatsSQETestDelta,
       "cfprEtherLossStatsSQETestDeltaAvg": cfprEtherLossStatsSQETestDeltaAvg,
       "cfprEtherLossStatsSQETestDeltaMax": cfprEtherLossStatsSQETestDeltaMax,
       "cfprEtherLossStatsSQETestDeltaMin": cfprEtherLossStatsSQETestDeltaMin,
       "cfprEtherLossStatsCarrierSense": cfprEtherLossStatsCarrierSense,
       "cfprEtherLossStatsCarrierSenseDelta": cfprEtherLossStatsCarrierSenseDelta,
       "cfprEtherLossStatsCarrierSenseDeltaAvg": cfprEtherLossStatsCarrierSenseDeltaAvg,
       "cfprEtherLossStatsCarrierSenseDeltaMax": cfprEtherLossStatsCarrierSenseDeltaMax,
       "cfprEtherLossStatsCarrierSenseDeltaMin": cfprEtherLossStatsCarrierSenseDeltaMin,
       "cfprEtherLossStatsExcessCollision": cfprEtherLossStatsExcessCollision,
       "cfprEtherLossStatsExcessCollisionDelta": cfprEtherLossStatsExcessCollisionDelta,
       "cfprEtherLossStatsExcessCollisionDeltaAvg": cfprEtherLossStatsExcessCollisionDeltaAvg,
       "cfprEtherLossStatsExcessCollisionDeltaMax": cfprEtherLossStatsExcessCollisionDeltaMax,
       "cfprEtherLossStatsExcessCollisionDeltaMin": cfprEtherLossStatsExcessCollisionDeltaMin,
       "cfprEtherLossStatsGiants": cfprEtherLossStatsGiants,
       "cfprEtherLossStatsGiantsDelta": cfprEtherLossStatsGiantsDelta,
       "cfprEtherLossStatsGiantsDeltaAvg": cfprEtherLossStatsGiantsDeltaAvg,
       "cfprEtherLossStatsGiantsDeltaMax": cfprEtherLossStatsGiantsDeltaMax,
       "cfprEtherLossStatsGiantsDeltaMin": cfprEtherLossStatsGiantsDeltaMin,
       "cfprEtherLossStatsIntervals": cfprEtherLossStatsIntervals,
       "cfprEtherLossStatsLateCollision": cfprEtherLossStatsLateCollision,
       "cfprEtherLossStatsLateCollisionDelta": cfprEtherLossStatsLateCollisionDelta,
       "cfprEtherLossStatsLateCollisionDeltaAvg": cfprEtherLossStatsLateCollisionDeltaAvg,
       "cfprEtherLossStatsLateCollisionDeltaMax": cfprEtherLossStatsLateCollisionDeltaMax,
       "cfprEtherLossStatsLateCollisionDeltaMin": cfprEtherLossStatsLateCollisionDeltaMin,
       "cfprEtherLossStatsMultiCollision": cfprEtherLossStatsMultiCollision,
       "cfprEtherLossStatsMultiCollisionDelta": cfprEtherLossStatsMultiCollisionDelta,
       "cfprEtherLossStatsMultiCollisionDeltaAvg": cfprEtherLossStatsMultiCollisionDeltaAvg,
       "cfprEtherLossStatsMultiCollisionDeltaMax": cfprEtherLossStatsMultiCollisionDeltaMax,
       "cfprEtherLossStatsMultiCollisionDeltaMin": cfprEtherLossStatsMultiCollisionDeltaMin,
       "cfprEtherLossStatsSingleCollision": cfprEtherLossStatsSingleCollision,
       "cfprEtherLossStatsSingleCollisionDelta": cfprEtherLossStatsSingleCollisionDelta,
       "cfprEtherLossStatsSingleCollisionDeltaAvg": cfprEtherLossStatsSingleCollisionDeltaAvg,
       "cfprEtherLossStatsSingleCollisionDeltaMax": cfprEtherLossStatsSingleCollisionDeltaMax,
       "cfprEtherLossStatsSingleCollisionDeltaMin": cfprEtherLossStatsSingleCollisionDeltaMin,
       "cfprEtherLossStatsSuspect": cfprEtherLossStatsSuspect,
       "cfprEtherLossStatsSymbol": cfprEtherLossStatsSymbol,
       "cfprEtherLossStatsSymbolDelta": cfprEtherLossStatsSymbolDelta,
       "cfprEtherLossStatsSymbolDeltaAvg": cfprEtherLossStatsSymbolDeltaAvg,
       "cfprEtherLossStatsSymbolDeltaMax": cfprEtherLossStatsSymbolDeltaMax,
       "cfprEtherLossStatsSymbolDeltaMin": cfprEtherLossStatsSymbolDeltaMin,
       "cfprEtherLossStatsThresholded": cfprEtherLossStatsThresholded,
       "cfprEtherLossStatsTimeCollected": cfprEtherLossStatsTimeCollected,
       "cfprEtherLossStatsUpdate": cfprEtherLossStatsUpdate,
       "cfprEtherLossStatsHistTable": cfprEtherLossStatsHistTable,
       "cfprEtherLossStatsHistEntry": cfprEtherLossStatsHistEntry,
       "cfprEtherLossStatsHistInstanceId": cfprEtherLossStatsHistInstanceId,
       "cfprEtherLossStatsHistDn": cfprEtherLossStatsHistDn,
       "cfprEtherLossStatsHistRn": cfprEtherLossStatsHistRn,
       "cfprEtherLossStatsHistSQETest": cfprEtherLossStatsHistSQETest,
       "cfprEtherLossStatsHistSQETestDelta": cfprEtherLossStatsHistSQETestDelta,
       "cfprEtherLossStatsHistSQETestDeltaAvg": cfprEtherLossStatsHistSQETestDeltaAvg,
       "cfprEtherLossStatsHistSQETestDeltaMax": cfprEtherLossStatsHistSQETestDeltaMax,
       "cfprEtherLossStatsHistSQETestDeltaMin": cfprEtherLossStatsHistSQETestDeltaMin,
       "cfprEtherLossStatsHistCarrierSense": cfprEtherLossStatsHistCarrierSense,
       "cfprEtherLossStatsHistCarrierSenseDelta": cfprEtherLossStatsHistCarrierSenseDelta,
       "cfprEtherLossStatsHistCarrierSenseDeltaAvg": cfprEtherLossStatsHistCarrierSenseDeltaAvg,
       "cfprEtherLossStatsHistCarrierSenseDeltaMax": cfprEtherLossStatsHistCarrierSenseDeltaMax,
       "cfprEtherLossStatsHistCarrierSenseDeltaMin": cfprEtherLossStatsHistCarrierSenseDeltaMin,
       "cfprEtherLossStatsHistExcessCollision": cfprEtherLossStatsHistExcessCollision,
       "cfprEtherLossStatsHistExcessCollisionDelta": cfprEtherLossStatsHistExcessCollisionDelta,
       "cfprEtherLossStatsHistExcessCollisionDeltaAvg": cfprEtherLossStatsHistExcessCollisionDeltaAvg,
       "cfprEtherLossStatsHistExcessCollisionDeltaMax": cfprEtherLossStatsHistExcessCollisionDeltaMax,
       "cfprEtherLossStatsHistExcessCollisionDeltaMin": cfprEtherLossStatsHistExcessCollisionDeltaMin,
       "cfprEtherLossStatsHistGiants": cfprEtherLossStatsHistGiants,
       "cfprEtherLossStatsHistGiantsDelta": cfprEtherLossStatsHistGiantsDelta,
       "cfprEtherLossStatsHistGiantsDeltaAvg": cfprEtherLossStatsHistGiantsDeltaAvg,
       "cfprEtherLossStatsHistGiantsDeltaMax": cfprEtherLossStatsHistGiantsDeltaMax,
       "cfprEtherLossStatsHistGiantsDeltaMin": cfprEtherLossStatsHistGiantsDeltaMin,
       "cfprEtherLossStatsHistId": cfprEtherLossStatsHistId,
       "cfprEtherLossStatsHistLateCollision": cfprEtherLossStatsHistLateCollision,
       "cfprEtherLossStatsHistLateCollisionDelta": cfprEtherLossStatsHistLateCollisionDelta,
       "cfprEtherLossStatsHistLateCollisionDeltaAvg": cfprEtherLossStatsHistLateCollisionDeltaAvg,
       "cfprEtherLossStatsHistLateCollisionDeltaMax": cfprEtherLossStatsHistLateCollisionDeltaMax,
       "cfprEtherLossStatsHistLateCollisionDeltaMin": cfprEtherLossStatsHistLateCollisionDeltaMin,
       "cfprEtherLossStatsHistMostRecent": cfprEtherLossStatsHistMostRecent,
       "cfprEtherLossStatsHistMultiCollision": cfprEtherLossStatsHistMultiCollision,
       "cfprEtherLossStatsHistMultiCollisionDelta": cfprEtherLossStatsHistMultiCollisionDelta,
       "cfprEtherLossStatsHistMultiCollisionDeltaAvg": cfprEtherLossStatsHistMultiCollisionDeltaAvg,
       "cfprEtherLossStatsHistMultiCollisionDeltaMax": cfprEtherLossStatsHistMultiCollisionDeltaMax,
       "cfprEtherLossStatsHistMultiCollisionDeltaMin": cfprEtherLossStatsHistMultiCollisionDeltaMin,
       "cfprEtherLossStatsHistSingleCollision": cfprEtherLossStatsHistSingleCollision,
       "cfprEtherLossStatsHistSingleCollisionDelta": cfprEtherLossStatsHistSingleCollisionDelta,
       "cfprEtherLossStatsHistSingleCollisionDeltaAvg": cfprEtherLossStatsHistSingleCollisionDeltaAvg,
       "cfprEtherLossStatsHistSingleCollisionDeltaMax": cfprEtherLossStatsHistSingleCollisionDeltaMax,
       "cfprEtherLossStatsHistSingleCollisionDeltaMin": cfprEtherLossStatsHistSingleCollisionDeltaMin,
       "cfprEtherLossStatsHistSuspect": cfprEtherLossStatsHistSuspect,
       "cfprEtherLossStatsHistSymbol": cfprEtherLossStatsHistSymbol,
       "cfprEtherLossStatsHistSymbolDelta": cfprEtherLossStatsHistSymbolDelta,
       "cfprEtherLossStatsHistSymbolDeltaAvg": cfprEtherLossStatsHistSymbolDeltaAvg,
       "cfprEtherLossStatsHistSymbolDeltaMax": cfprEtherLossStatsHistSymbolDeltaMax,
       "cfprEtherLossStatsHistSymbolDeltaMin": cfprEtherLossStatsHistSymbolDeltaMin,
       "cfprEtherLossStatsHistThresholded": cfprEtherLossStatsHistThresholded,
       "cfprEtherLossStatsHistTimeCollected": cfprEtherLossStatsHistTimeCollected,
       "cfprEtherNiErrStatsTable": cfprEtherNiErrStatsTable,
       "cfprEtherNiErrStatsEntry": cfprEtherNiErrStatsEntry,
       "cfprEtherNiErrStatsInstanceId": cfprEtherNiErrStatsInstanceId,
       "cfprEtherNiErrStatsDn": cfprEtherNiErrStatsDn,
       "cfprEtherNiErrStatsRn": cfprEtherNiErrStatsRn,
       "cfprEtherNiErrStatsCrc": cfprEtherNiErrStatsCrc,
       "cfprEtherNiErrStatsCrcDelta": cfprEtherNiErrStatsCrcDelta,
       "cfprEtherNiErrStatsCrcDeltaAvg": cfprEtherNiErrStatsCrcDeltaAvg,
       "cfprEtherNiErrStatsCrcDeltaMax": cfprEtherNiErrStatsCrcDeltaMax,
       "cfprEtherNiErrStatsCrcDeltaMin": cfprEtherNiErrStatsCrcDeltaMin,
       "cfprEtherNiErrStatsFrameTx": cfprEtherNiErrStatsFrameTx,
       "cfprEtherNiErrStatsFrameTxDelta": cfprEtherNiErrStatsFrameTxDelta,
       "cfprEtherNiErrStatsFrameTxDeltaAvg": cfprEtherNiErrStatsFrameTxDeltaAvg,
       "cfprEtherNiErrStatsFrameTxDeltaMax": cfprEtherNiErrStatsFrameTxDeltaMax,
       "cfprEtherNiErrStatsFrameTxDeltaMin": cfprEtherNiErrStatsFrameTxDeltaMin,
       "cfprEtherNiErrStatsInRange": cfprEtherNiErrStatsInRange,
       "cfprEtherNiErrStatsInRangeDelta": cfprEtherNiErrStatsInRangeDelta,
       "cfprEtherNiErrStatsInRangeDeltaAvg": cfprEtherNiErrStatsInRangeDeltaAvg,
       "cfprEtherNiErrStatsInRangeDeltaMax": cfprEtherNiErrStatsInRangeDeltaMax,
       "cfprEtherNiErrStatsInRangeDeltaMin": cfprEtherNiErrStatsInRangeDeltaMin,
       "cfprEtherNiErrStatsIntervals": cfprEtherNiErrStatsIntervals,
       "cfprEtherNiErrStatsSuspect": cfprEtherNiErrStatsSuspect,
       "cfprEtherNiErrStatsThresholded": cfprEtherNiErrStatsThresholded,
       "cfprEtherNiErrStatsTimeCollected": cfprEtherNiErrStatsTimeCollected,
       "cfprEtherNiErrStatsTooLong": cfprEtherNiErrStatsTooLong,
       "cfprEtherNiErrStatsTooLongDelta": cfprEtherNiErrStatsTooLongDelta,
       "cfprEtherNiErrStatsTooLongDeltaAvg": cfprEtherNiErrStatsTooLongDeltaAvg,
       "cfprEtherNiErrStatsTooLongDeltaMax": cfprEtherNiErrStatsTooLongDeltaMax,
       "cfprEtherNiErrStatsTooLongDeltaMin": cfprEtherNiErrStatsTooLongDeltaMin,
       "cfprEtherNiErrStatsTooShort": cfprEtherNiErrStatsTooShort,
       "cfprEtherNiErrStatsTooShortDelta": cfprEtherNiErrStatsTooShortDelta,
       "cfprEtherNiErrStatsTooShortDeltaAvg": cfprEtherNiErrStatsTooShortDeltaAvg,
       "cfprEtherNiErrStatsTooShortDeltaMax": cfprEtherNiErrStatsTooShortDeltaMax,
       "cfprEtherNiErrStatsTooShortDeltaMin": cfprEtherNiErrStatsTooShortDeltaMin,
       "cfprEtherNiErrStatsUpdate": cfprEtherNiErrStatsUpdate,
       "cfprEtherNiErrStatsHistTable": cfprEtherNiErrStatsHistTable,
       "cfprEtherNiErrStatsHistEntry": cfprEtherNiErrStatsHistEntry,
       "cfprEtherNiErrStatsHistInstanceId": cfprEtherNiErrStatsHistInstanceId,
       "cfprEtherNiErrStatsHistDn": cfprEtherNiErrStatsHistDn,
       "cfprEtherNiErrStatsHistRn": cfprEtherNiErrStatsHistRn,
       "cfprEtherNiErrStatsHistCrc": cfprEtherNiErrStatsHistCrc,
       "cfprEtherNiErrStatsHistCrcDelta": cfprEtherNiErrStatsHistCrcDelta,
       "cfprEtherNiErrStatsHistCrcDeltaAvg": cfprEtherNiErrStatsHistCrcDeltaAvg,
       "cfprEtherNiErrStatsHistCrcDeltaMax": cfprEtherNiErrStatsHistCrcDeltaMax,
       "cfprEtherNiErrStatsHistCrcDeltaMin": cfprEtherNiErrStatsHistCrcDeltaMin,
       "cfprEtherNiErrStatsHistFrameTx": cfprEtherNiErrStatsHistFrameTx,
       "cfprEtherNiErrStatsHistFrameTxDelta": cfprEtherNiErrStatsHistFrameTxDelta,
       "cfprEtherNiErrStatsHistFrameTxDeltaAvg": cfprEtherNiErrStatsHistFrameTxDeltaAvg,
       "cfprEtherNiErrStatsHistFrameTxDeltaMax": cfprEtherNiErrStatsHistFrameTxDeltaMax,
       "cfprEtherNiErrStatsHistFrameTxDeltaMin": cfprEtherNiErrStatsHistFrameTxDeltaMin,
       "cfprEtherNiErrStatsHistId": cfprEtherNiErrStatsHistId,
       "cfprEtherNiErrStatsHistInRange": cfprEtherNiErrStatsHistInRange,
       "cfprEtherNiErrStatsHistInRangeDelta": cfprEtherNiErrStatsHistInRangeDelta,
       "cfprEtherNiErrStatsHistInRangeDeltaAvg": cfprEtherNiErrStatsHistInRangeDeltaAvg,
       "cfprEtherNiErrStatsHistInRangeDeltaMax": cfprEtherNiErrStatsHistInRangeDeltaMax,
       "cfprEtherNiErrStatsHistInRangeDeltaMin": cfprEtherNiErrStatsHistInRangeDeltaMin,
       "cfprEtherNiErrStatsHistMostRecent": cfprEtherNiErrStatsHistMostRecent,
       "cfprEtherNiErrStatsHistSuspect": cfprEtherNiErrStatsHistSuspect,
       "cfprEtherNiErrStatsHistThresholded": cfprEtherNiErrStatsHistThresholded,
       "cfprEtherNiErrStatsHistTimeCollected": cfprEtherNiErrStatsHistTimeCollected,
       "cfprEtherNiErrStatsHistTooLong": cfprEtherNiErrStatsHistTooLong,
       "cfprEtherNiErrStatsHistTooLongDelta": cfprEtherNiErrStatsHistTooLongDelta,
       "cfprEtherNiErrStatsHistTooLongDeltaAvg": cfprEtherNiErrStatsHistTooLongDeltaAvg,
       "cfprEtherNiErrStatsHistTooLongDeltaMax": cfprEtherNiErrStatsHistTooLongDeltaMax,
       "cfprEtherNiErrStatsHistTooLongDeltaMin": cfprEtherNiErrStatsHistTooLongDeltaMin,
       "cfprEtherNiErrStatsHistTooShort": cfprEtherNiErrStatsHistTooShort,
       "cfprEtherNiErrStatsHistTooShortDelta": cfprEtherNiErrStatsHistTooShortDelta,
       "cfprEtherNiErrStatsHistTooShortDeltaAvg": cfprEtherNiErrStatsHistTooShortDeltaAvg,
       "cfprEtherNiErrStatsHistTooShortDeltaMax": cfprEtherNiErrStatsHistTooShortDeltaMax,
       "cfprEtherNiErrStatsHistTooShortDeltaMin": cfprEtherNiErrStatsHistTooShortDeltaMin,
       "cfprEtherNicIfConfigTable": cfprEtherNicIfConfigTable,
       "cfprEtherNicIfConfigEntry": cfprEtherNicIfConfigEntry,
       "cfprEtherNicIfConfigInstanceId": cfprEtherNicIfConfigInstanceId,
       "cfprEtherNicIfConfigDn": cfprEtherNicIfConfigDn,
       "cfprEtherNicIfConfigRn": cfprEtherNicIfConfigRn,
       "cfprEtherPIoTable": cfprEtherPIoTable,
       "cfprEtherPIoEntry": cfprEtherPIoEntry,
       "cfprEtherPIoInstanceId": cfprEtherPIoInstanceId,
       "cfprEtherPIoDn": cfprEtherPIoDn,
       "cfprEtherPIoRn": cfprEtherPIoRn,
       "cfprEtherPIoAdminState": cfprEtherPIoAdminState,
       "cfprEtherPIoAdminTransport": cfprEtherPIoAdminTransport,
       "cfprEtherPIoAggrPortId": cfprEtherPIoAggrPortId,
       "cfprEtherPIoChassisId": cfprEtherPIoChassisId,
       "cfprEtherPIoEncap": cfprEtherPIoEncap,
       "cfprEtherPIoEpDn": cfprEtherPIoEpDn,
       "cfprEtherPIoFltAggr": cfprEtherPIoFltAggr,
       "cfprEtherPIoFsmDescr": cfprEtherPIoFsmDescr,
       "cfprEtherPIoFsmPrev": cfprEtherPIoFsmPrev,
       "cfprEtherPIoFsmProgr": cfprEtherPIoFsmProgr,
       "cfprEtherPIoFsmRmtInvErrCode": cfprEtherPIoFsmRmtInvErrCode,
       "cfprEtherPIoFsmRmtInvErrDescr": cfprEtherPIoFsmRmtInvErrDescr,
       "cfprEtherPIoFsmRmtInvRslt": cfprEtherPIoFsmRmtInvRslt,
       "cfprEtherPIoFsmStageDescr": cfprEtherPIoFsmStageDescr,
       "cfprEtherPIoFsmStamp": cfprEtherPIoFsmStamp,
       "cfprEtherPIoFsmStatus": cfprEtherPIoFsmStatus,
       "cfprEtherPIoFsmTry": cfprEtherPIoFsmTry,
       "cfprEtherPIoIfRole": cfprEtherPIoIfRole,
       "cfprEtherPIoIfType": cfprEtherPIoIfType,
       "cfprEtherPIoIsPortChannelMember": cfprEtherPIoIsPortChannelMember,
       "cfprEtherPIoLc": cfprEtherPIoLc,
       "cfprEtherPIoLicGP": cfprEtherPIoLicGP,
       "cfprEtherPIoLicState": cfprEtherPIoLicState,
       "cfprEtherPIoLocale": cfprEtherPIoLocale,
       "cfprEtherPIoMac": cfprEtherPIoMac,
       "cfprEtherPIoMode": cfprEtherPIoMode,
       "cfprEtherPIoModel": cfprEtherPIoModel,
       "cfprEtherPIoName": cfprEtherPIoName,
       "cfprEtherPIoOperSpeed": cfprEtherPIoOperSpeed,
       "cfprEtherPIoOperState": cfprEtherPIoOperState,
       "cfprEtherPIoPeerAggrPortId": cfprEtherPIoPeerAggrPortId,
       "cfprEtherPIoPeerChassisId": cfprEtherPIoPeerChassisId,
       "cfprEtherPIoPeerDn": cfprEtherPIoPeerDn,
       "cfprEtherPIoPeerPortId": cfprEtherPIoPeerPortId,
       "cfprEtherPIoPeerSlotId": cfprEtherPIoPeerSlotId,
       "cfprEtherPIoPortId": cfprEtherPIoPortId,
       "cfprEtherPIoRevision": cfprEtherPIoRevision,
       "cfprEtherPIoSerial": cfprEtherPIoSerial,
       "cfprEtherPIoSlotId": cfprEtherPIoSlotId,
       "cfprEtherPIoStateQual": cfprEtherPIoStateQual,
       "cfprEtherPIoSwitchId": cfprEtherPIoSwitchId,
       "cfprEtherPIoTransport": cfprEtherPIoTransport,
       "cfprEtherPIoTs": cfprEtherPIoTs,
       "cfprEtherPIoType": cfprEtherPIoType,
       "cfprEtherPIoUnifiedPort": cfprEtherPIoUnifiedPort,
       "cfprEtherPIoUsrLbl": cfprEtherPIoUsrLbl,
       "cfprEtherPIoVendor": cfprEtherPIoVendor,
       "cfprEtherPIoXcvrType": cfprEtherPIoXcvrType,
       "cfprEtherPIoFtwPhyDn": cfprEtherPIoFtwPhyDn,
       "cfprEtherPIoOperDuplex": cfprEtherPIoOperDuplex,
       "cfprEtherPIoEndPointTable": cfprEtherPIoEndPointTable,
       "cfprEtherPIoEndPointEntry": cfprEtherPIoEndPointEntry,
       "cfprEtherPIoEndPointInstanceId": cfprEtherPIoEndPointInstanceId,
       "cfprEtherPIoEndPointDn": cfprEtherPIoEndPointDn,
       "cfprEtherPIoEndPointRn": cfprEtherPIoEndPointRn,
       "cfprEtherPIoEndPointEndPointDn": cfprEtherPIoEndPointEndPointDn,
       "cfprEtherPIoEndPointEpCloudType": cfprEtherPIoEndPointEpCloudType,
       "cfprEtherPIoEndPointUsrLbl": cfprEtherPIoEndPointUsrLbl,
       "cfprEtherPIoFsmTable": cfprEtherPIoFsmTable,
       "cfprEtherPIoFsmEntry": cfprEtherPIoFsmEntry,
       "cfprEtherPIoFsmInstanceId": cfprEtherPIoFsmInstanceId,
       "cfprEtherPIoFsmDn": cfprEtherPIoFsmDn,
       "cfprEtherPIoFsmRn": cfprEtherPIoFsmRn,
       "cfprEtherPIoFsmCompletionTime": cfprEtherPIoFsmCompletionTime,
       "cfprEtherPIoFsmCurrentFsm": cfprEtherPIoFsmCurrentFsm,
       "cfprEtherPIoFsmDescrData": cfprEtherPIoFsmDescrData,
       "cfprEtherPIoFsmFsmStatus": cfprEtherPIoFsmFsmStatus,
       "cfprEtherPIoFsmProgress": cfprEtherPIoFsmProgress,
       "cfprEtherPIoFsmRmtErrCode": cfprEtherPIoFsmRmtErrCode,
       "cfprEtherPIoFsmRmtErrDescr": cfprEtherPIoFsmRmtErrDescr,
       "cfprEtherPIoFsmRmtRslt": cfprEtherPIoFsmRmtRslt,
       "cfprEtherPIoFsmStageTable": cfprEtherPIoFsmStageTable,
       "cfprEtherPIoFsmStageEntry": cfprEtherPIoFsmStageEntry,
       "cfprEtherPIoFsmStageInstanceId": cfprEtherPIoFsmStageInstanceId,
       "cfprEtherPIoFsmStageDn": cfprEtherPIoFsmStageDn,
       "cfprEtherPIoFsmStageRn": cfprEtherPIoFsmStageRn,
       "cfprEtherPIoFsmStageDescrData": cfprEtherPIoFsmStageDescrData,
       "cfprEtherPIoFsmStageLastUpdateTime": cfprEtherPIoFsmStageLastUpdateTime,
       "cfprEtherPIoFsmStageName": cfprEtherPIoFsmStageName,
       "cfprEtherPIoFsmStageOrder": cfprEtherPIoFsmStageOrder,
       "cfprEtherPIoFsmStageRetry": cfprEtherPIoFsmStageRetry,
       "cfprEtherPIoFsmStageStageStatus": cfprEtherPIoFsmStageStageStatus,
       "cfprEtherPauseStatsTable": cfprEtherPauseStatsTable,
       "cfprEtherPauseStatsEntry": cfprEtherPauseStatsEntry,
       "cfprEtherPauseStatsInstanceId": cfprEtherPauseStatsInstanceId,
       "cfprEtherPauseStatsDn": cfprEtherPauseStatsDn,
       "cfprEtherPauseStatsRn": cfprEtherPauseStatsRn,
       "cfprEtherPauseStatsIntervals": cfprEtherPauseStatsIntervals,
       "cfprEtherPauseStatsRecvPause": cfprEtherPauseStatsRecvPause,
       "cfprEtherPauseStatsRecvPauseDelta": cfprEtherPauseStatsRecvPauseDelta,
       "cfprEtherPauseStatsRecvPauseDeltaAvg": cfprEtherPauseStatsRecvPauseDeltaAvg,
       "cfprEtherPauseStatsRecvPauseDeltaMax": cfprEtherPauseStatsRecvPauseDeltaMax,
       "cfprEtherPauseStatsRecvPauseDeltaMin": cfprEtherPauseStatsRecvPauseDeltaMin,
       "cfprEtherPauseStatsResets": cfprEtherPauseStatsResets,
       "cfprEtherPauseStatsResetsDelta": cfprEtherPauseStatsResetsDelta,
       "cfprEtherPauseStatsResetsDeltaAvg": cfprEtherPauseStatsResetsDeltaAvg,
       "cfprEtherPauseStatsResetsDeltaMax": cfprEtherPauseStatsResetsDeltaMax,
       "cfprEtherPauseStatsResetsDeltaMin": cfprEtherPauseStatsResetsDeltaMin,
       "cfprEtherPauseStatsSuspect": cfprEtherPauseStatsSuspect,
       "cfprEtherPauseStatsThresholded": cfprEtherPauseStatsThresholded,
       "cfprEtherPauseStatsTimeCollected": cfprEtherPauseStatsTimeCollected,
       "cfprEtherPauseStatsUpdate": cfprEtherPauseStatsUpdate,
       "cfprEtherPauseStatsXmitPause": cfprEtherPauseStatsXmitPause,
       "cfprEtherPauseStatsXmitPauseDelta": cfprEtherPauseStatsXmitPauseDelta,
       "cfprEtherPauseStatsXmitPauseDeltaAvg": cfprEtherPauseStatsXmitPauseDeltaAvg,
       "cfprEtherPauseStatsXmitPauseDeltaMax": cfprEtherPauseStatsXmitPauseDeltaMax,
       "cfprEtherPauseStatsXmitPauseDeltaMin": cfprEtherPauseStatsXmitPauseDeltaMin,
       "cfprEtherPauseStatsHistTable": cfprEtherPauseStatsHistTable,
       "cfprEtherPauseStatsHistEntry": cfprEtherPauseStatsHistEntry,
       "cfprEtherPauseStatsHistInstanceId": cfprEtherPauseStatsHistInstanceId,
       "cfprEtherPauseStatsHistDn": cfprEtherPauseStatsHistDn,
       "cfprEtherPauseStatsHistRn": cfprEtherPauseStatsHistRn,
       "cfprEtherPauseStatsHistId": cfprEtherPauseStatsHistId,
       "cfprEtherPauseStatsHistMostRecent": cfprEtherPauseStatsHistMostRecent,
       "cfprEtherPauseStatsHistRecvPause": cfprEtherPauseStatsHistRecvPause,
       "cfprEtherPauseStatsHistRecvPauseDelta": cfprEtherPauseStatsHistRecvPauseDelta,
       "cfprEtherPauseStatsHistRecvPauseDeltaAvg": cfprEtherPauseStatsHistRecvPauseDeltaAvg,
       "cfprEtherPauseStatsHistRecvPauseDeltaMax": cfprEtherPauseStatsHistRecvPauseDeltaMax,
       "cfprEtherPauseStatsHistRecvPauseDeltaMin": cfprEtherPauseStatsHistRecvPauseDeltaMin,
       "cfprEtherPauseStatsHistResets": cfprEtherPauseStatsHistResets,
       "cfprEtherPauseStatsHistResetsDelta": cfprEtherPauseStatsHistResetsDelta,
       "cfprEtherPauseStatsHistResetsDeltaAvg": cfprEtherPauseStatsHistResetsDeltaAvg,
       "cfprEtherPauseStatsHistResetsDeltaMax": cfprEtherPauseStatsHistResetsDeltaMax,
       "cfprEtherPauseStatsHistResetsDeltaMin": cfprEtherPauseStatsHistResetsDeltaMin,
       "cfprEtherPauseStatsHistSuspect": cfprEtherPauseStatsHistSuspect,
       "cfprEtherPauseStatsHistThresholded": cfprEtherPauseStatsHistThresholded,
       "cfprEtherPauseStatsHistTimeCollected": cfprEtherPauseStatsHistTimeCollected,
       "cfprEtherPauseStatsHistXmitPause": cfprEtherPauseStatsHistXmitPause,
       "cfprEtherPauseStatsHistXmitPauseDelta": cfprEtherPauseStatsHistXmitPauseDelta,
       "cfprEtherPauseStatsHistXmitPauseDeltaAvg": cfprEtherPauseStatsHistXmitPauseDeltaAvg,
       "cfprEtherPauseStatsHistXmitPauseDeltaMax": cfprEtherPauseStatsHistXmitPauseDeltaMax,
       "cfprEtherPauseStatsHistXmitPauseDeltaMin": cfprEtherPauseStatsHistXmitPauseDeltaMin,
       "cfprEtherPortChanIdElemTable": cfprEtherPortChanIdElemTable,
       "cfprEtherPortChanIdElemEntry": cfprEtherPortChanIdElemEntry,
       "cfprEtherPortChanIdElemInstanceId": cfprEtherPortChanIdElemInstanceId,
       "cfprEtherPortChanIdElemDn": cfprEtherPortChanIdElemDn,
       "cfprEtherPortChanIdElemRn": cfprEtherPortChanIdElemRn,
       "cfprEtherPortChanIdElemId": cfprEtherPortChanIdElemId,
       "cfprEtherPortChanIdUniverseTable": cfprEtherPortChanIdUniverseTable,
       "cfprEtherPortChanIdUniverseEntry": cfprEtherPortChanIdUniverseEntry,
       "cfprEtherPortChanIdUniverseInstanceId": cfprEtherPortChanIdUniverseInstanceId,
       "cfprEtherPortChanIdUniverseDn": cfprEtherPortChanIdUniverseDn,
       "cfprEtherPortChanIdUniverseRn": cfprEtherPortChanIdUniverseRn,
       "cfprEtherRxStatsTable": cfprEtherRxStatsTable,
       "cfprEtherRxStatsEntry": cfprEtherRxStatsEntry,
       "cfprEtherRxStatsInstanceId": cfprEtherRxStatsInstanceId,
       "cfprEtherRxStatsDn": cfprEtherRxStatsDn,
       "cfprEtherRxStatsRn": cfprEtherRxStatsRn,
       "cfprEtherRxStatsBroadcastPackets": cfprEtherRxStatsBroadcastPackets,
       "cfprEtherRxStatsBroadcastPacketsDelta": cfprEtherRxStatsBroadcastPacketsDelta,
       "cfprEtherRxStatsBroadcastPacketsDeltaAvg": cfprEtherRxStatsBroadcastPacketsDeltaAvg,
       "cfprEtherRxStatsBroadcastPacketsDeltaMax": cfprEtherRxStatsBroadcastPacketsDeltaMax,
       "cfprEtherRxStatsBroadcastPacketsDeltaMin": cfprEtherRxStatsBroadcastPacketsDeltaMin,
       "cfprEtherRxStatsIntervals": cfprEtherRxStatsIntervals,
       "cfprEtherRxStatsJumboPackets": cfprEtherRxStatsJumboPackets,
       "cfprEtherRxStatsJumboPacketsDelta": cfprEtherRxStatsJumboPacketsDelta,
       "cfprEtherRxStatsJumboPacketsDeltaAvg": cfprEtherRxStatsJumboPacketsDeltaAvg,
       "cfprEtherRxStatsJumboPacketsDeltaMax": cfprEtherRxStatsJumboPacketsDeltaMax,
       "cfprEtherRxStatsJumboPacketsDeltaMin": cfprEtherRxStatsJumboPacketsDeltaMin,
       "cfprEtherRxStatsMulticastPackets": cfprEtherRxStatsMulticastPackets,
       "cfprEtherRxStatsMulticastPacketsDelta": cfprEtherRxStatsMulticastPacketsDelta,
       "cfprEtherRxStatsMulticastPacketsDeltaAvg": cfprEtherRxStatsMulticastPacketsDeltaAvg,
       "cfprEtherRxStatsMulticastPacketsDeltaMax": cfprEtherRxStatsMulticastPacketsDeltaMax,
       "cfprEtherRxStatsMulticastPacketsDeltaMin": cfprEtherRxStatsMulticastPacketsDeltaMin,
       "cfprEtherRxStatsSuspect": cfprEtherRxStatsSuspect,
       "cfprEtherRxStatsThresholded": cfprEtherRxStatsThresholded,
       "cfprEtherRxStatsTimeCollected": cfprEtherRxStatsTimeCollected,
       "cfprEtherRxStatsTotalBytes": cfprEtherRxStatsTotalBytes,
       "cfprEtherRxStatsTotalBytesDelta": cfprEtherRxStatsTotalBytesDelta,
       "cfprEtherRxStatsTotalBytesDeltaAvg": cfprEtherRxStatsTotalBytesDeltaAvg,
       "cfprEtherRxStatsTotalBytesDeltaMax": cfprEtherRxStatsTotalBytesDeltaMax,
       "cfprEtherRxStatsTotalBytesDeltaMin": cfprEtherRxStatsTotalBytesDeltaMin,
       "cfprEtherRxStatsTotalPackets": cfprEtherRxStatsTotalPackets,
       "cfprEtherRxStatsTotalPacketsDelta": cfprEtherRxStatsTotalPacketsDelta,
       "cfprEtherRxStatsTotalPacketsDeltaAvg": cfprEtherRxStatsTotalPacketsDeltaAvg,
       "cfprEtherRxStatsTotalPacketsDeltaMax": cfprEtherRxStatsTotalPacketsDeltaMax,
       "cfprEtherRxStatsTotalPacketsDeltaMin": cfprEtherRxStatsTotalPacketsDeltaMin,
       "cfprEtherRxStatsUnicastPackets": cfprEtherRxStatsUnicastPackets,
       "cfprEtherRxStatsUnicastPacketsDelta": cfprEtherRxStatsUnicastPacketsDelta,
       "cfprEtherRxStatsUnicastPacketsDeltaAvg": cfprEtherRxStatsUnicastPacketsDeltaAvg,
       "cfprEtherRxStatsUnicastPacketsDeltaMax": cfprEtherRxStatsUnicastPacketsDeltaMax,
       "cfprEtherRxStatsUnicastPacketsDeltaMin": cfprEtherRxStatsUnicastPacketsDeltaMin,
       "cfprEtherRxStatsUpdate": cfprEtherRxStatsUpdate,
       "cfprEtherRxStatsHistTable": cfprEtherRxStatsHistTable,
       "cfprEtherRxStatsHistEntry": cfprEtherRxStatsHistEntry,
       "cfprEtherRxStatsHistInstanceId": cfprEtherRxStatsHistInstanceId,
       "cfprEtherRxStatsHistDn": cfprEtherRxStatsHistDn,
       "cfprEtherRxStatsHistRn": cfprEtherRxStatsHistRn,
       "cfprEtherRxStatsHistBroadcastPackets": cfprEtherRxStatsHistBroadcastPackets,
       "cfprEtherRxStatsHistBroadcastPacketsDelta": cfprEtherRxStatsHistBroadcastPacketsDelta,
       "cfprEtherRxStatsHistBroadcastPacketsDeltaAvg": cfprEtherRxStatsHistBroadcastPacketsDeltaAvg,
       "cfprEtherRxStatsHistBroadcastPacketsDeltaMax": cfprEtherRxStatsHistBroadcastPacketsDeltaMax,
       "cfprEtherRxStatsHistBroadcastPacketsDeltaMin": cfprEtherRxStatsHistBroadcastPacketsDeltaMin,
       "cfprEtherRxStatsHistId": cfprEtherRxStatsHistId,
       "cfprEtherRxStatsHistJumboPackets": cfprEtherRxStatsHistJumboPackets,
       "cfprEtherRxStatsHistJumboPacketsDelta": cfprEtherRxStatsHistJumboPacketsDelta,
       "cfprEtherRxStatsHistJumboPacketsDeltaAvg": cfprEtherRxStatsHistJumboPacketsDeltaAvg,
       "cfprEtherRxStatsHistJumboPacketsDeltaMax": cfprEtherRxStatsHistJumboPacketsDeltaMax,
       "cfprEtherRxStatsHistJumboPacketsDeltaMin": cfprEtherRxStatsHistJumboPacketsDeltaMin,
       "cfprEtherRxStatsHistMostRecent": cfprEtherRxStatsHistMostRecent,
       "cfprEtherRxStatsHistMulticastPackets": cfprEtherRxStatsHistMulticastPackets,
       "cfprEtherRxStatsHistMulticastPacketsDelta": cfprEtherRxStatsHistMulticastPacketsDelta,
       "cfprEtherRxStatsHistMulticastPacketsDeltaAvg": cfprEtherRxStatsHistMulticastPacketsDeltaAvg,
       "cfprEtherRxStatsHistMulticastPacketsDeltaMax": cfprEtherRxStatsHistMulticastPacketsDeltaMax,
       "cfprEtherRxStatsHistMulticastPacketsDeltaMin": cfprEtherRxStatsHistMulticastPacketsDeltaMin,
       "cfprEtherRxStatsHistSuspect": cfprEtherRxStatsHistSuspect,
       "cfprEtherRxStatsHistThresholded": cfprEtherRxStatsHistThresholded,
       "cfprEtherRxStatsHistTimeCollected": cfprEtherRxStatsHistTimeCollected,
       "cfprEtherRxStatsHistTotalBytes": cfprEtherRxStatsHistTotalBytes,
       "cfprEtherRxStatsHistTotalBytesDelta": cfprEtherRxStatsHistTotalBytesDelta,
       "cfprEtherRxStatsHistTotalBytesDeltaAvg": cfprEtherRxStatsHistTotalBytesDeltaAvg,
       "cfprEtherRxStatsHistTotalBytesDeltaMax": cfprEtherRxStatsHistTotalBytesDeltaMax,
       "cfprEtherRxStatsHistTotalBytesDeltaMin": cfprEtherRxStatsHistTotalBytesDeltaMin,
       "cfprEtherRxStatsHistTotalPackets": cfprEtherRxStatsHistTotalPackets,
       "cfprEtherRxStatsHistTotalPacketsDelta": cfprEtherRxStatsHistTotalPacketsDelta,
       "cfprEtherRxStatsHistTotalPacketsDeltaAvg": cfprEtherRxStatsHistTotalPacketsDeltaAvg,
       "cfprEtherRxStatsHistTotalPacketsDeltaMax": cfprEtherRxStatsHistTotalPacketsDeltaMax,
       "cfprEtherRxStatsHistTotalPacketsDeltaMin": cfprEtherRxStatsHistTotalPacketsDeltaMin,
       "cfprEtherRxStatsHistUnicastPackets": cfprEtherRxStatsHistUnicastPackets,
       "cfprEtherRxStatsHistUnicastPacketsDelta": cfprEtherRxStatsHistUnicastPacketsDelta,
       "cfprEtherRxStatsHistUnicastPacketsDeltaAvg": cfprEtherRxStatsHistUnicastPacketsDeltaAvg,
       "cfprEtherRxStatsHistUnicastPacketsDeltaMax": cfprEtherRxStatsHistUnicastPacketsDeltaMax,
       "cfprEtherRxStatsHistUnicastPacketsDeltaMin": cfprEtherRxStatsHistUnicastPacketsDeltaMin,
       "cfprEtherServerIntFIoTable": cfprEtherServerIntFIoTable,
       "cfprEtherServerIntFIoEntry": cfprEtherServerIntFIoEntry,
       "cfprEtherServerIntFIoInstanceId": cfprEtherServerIntFIoInstanceId,
       "cfprEtherServerIntFIoDn": cfprEtherServerIntFIoDn,
       "cfprEtherServerIntFIoRn": cfprEtherServerIntFIoRn,
       "cfprEtherServerIntFIoAdminSpeed": cfprEtherServerIntFIoAdminSpeed,
       "cfprEtherServerIntFIoAdminState": cfprEtherServerIntFIoAdminState,
       "cfprEtherServerIntFIoAggrPortId": cfprEtherServerIntFIoAggrPortId,
       "cfprEtherServerIntFIoChassisId": cfprEtherServerIntFIoChassisId,
       "cfprEtherServerIntFIoEncap": cfprEtherServerIntFIoEncap,
       "cfprEtherServerIntFIoEpDn": cfprEtherServerIntFIoEpDn,
       "cfprEtherServerIntFIoFltAggr": cfprEtherServerIntFIoFltAggr,
       "cfprEtherServerIntFIoFsmDescr": cfprEtherServerIntFIoFsmDescr,
       "cfprEtherServerIntFIoFsmPrev": cfprEtherServerIntFIoFsmPrev,
       "cfprEtherServerIntFIoFsmProgr": cfprEtherServerIntFIoFsmProgr,
       "cfprEtherServerIntFIoFsmRmtInvErrCode": cfprEtherServerIntFIoFsmRmtInvErrCode,
       "cfprEtherServerIntFIoFsmRmtInvErrDescr": cfprEtherServerIntFIoFsmRmtInvErrDescr,
       "cfprEtherServerIntFIoFsmRmtInvRslt": cfprEtherServerIntFIoFsmRmtInvRslt,
       "cfprEtherServerIntFIoFsmStageDescr": cfprEtherServerIntFIoFsmStageDescr,
       "cfprEtherServerIntFIoFsmStamp": cfprEtherServerIntFIoFsmStamp,
       "cfprEtherServerIntFIoFsmStatus": cfprEtherServerIntFIoFsmStatus,
       "cfprEtherServerIntFIoFsmTry": cfprEtherServerIntFIoFsmTry,
       "cfprEtherServerIntFIoIfRole": cfprEtherServerIntFIoIfRole,
       "cfprEtherServerIntFIoIfType": cfprEtherServerIntFIoIfType,
       "cfprEtherServerIntFIoLocale": cfprEtherServerIntFIoLocale,
       "cfprEtherServerIntFIoMac": cfprEtherServerIntFIoMac,
       "cfprEtherServerIntFIoMode": cfprEtherServerIntFIoMode,
       "cfprEtherServerIntFIoModel": cfprEtherServerIntFIoModel,
       "cfprEtherServerIntFIoName": cfprEtherServerIntFIoName,
       "cfprEtherServerIntFIoNsSize": cfprEtherServerIntFIoNsSize,
       "cfprEtherServerIntFIoOperBorderAggrPortId": cfprEtherServerIntFIoOperBorderAggrPortId,
       "cfprEtherServerIntFIoOperBorderPortId": cfprEtherServerIntFIoOperBorderPortId,
       "cfprEtherServerIntFIoOperBorderSlotId": cfprEtherServerIntFIoOperBorderSlotId,
       "cfprEtherServerIntFIoOperState": cfprEtherServerIntFIoOperState,
       "cfprEtherServerIntFIoPeerAggrPortId": cfprEtherServerIntFIoPeerAggrPortId,
       "cfprEtherServerIntFIoPeerChassisId": cfprEtherServerIntFIoPeerChassisId,
       "cfprEtherServerIntFIoPeerDn": cfprEtherServerIntFIoPeerDn,
       "cfprEtherServerIntFIoPeerEncap": cfprEtherServerIntFIoPeerEncap,
       "cfprEtherServerIntFIoPeerPortId": cfprEtherServerIntFIoPeerPortId,
       "cfprEtherServerIntFIoPeerSlotId": cfprEtherServerIntFIoPeerSlotId,
       "cfprEtherServerIntFIoPortId": cfprEtherServerIntFIoPortId,
       "cfprEtherServerIntFIoRevision": cfprEtherServerIntFIoRevision,
       "cfprEtherServerIntFIoSerial": cfprEtherServerIntFIoSerial,
       "cfprEtherServerIntFIoSlotId": cfprEtherServerIntFIoSlotId,
       "cfprEtherServerIntFIoStateQual": cfprEtherServerIntFIoStateQual,
       "cfprEtherServerIntFIoSwitchId": cfprEtherServerIntFIoSwitchId,
       "cfprEtherServerIntFIoTransport": cfprEtherServerIntFIoTransport,
       "cfprEtherServerIntFIoTs": cfprEtherServerIntFIoTs,
       "cfprEtherServerIntFIoType": cfprEtherServerIntFIoType,
       "cfprEtherServerIntFIoVendor": cfprEtherServerIntFIoVendor,
       "cfprEtherServerIntFIoXcvrType": cfprEtherServerIntFIoXcvrType,
       "cfprEtherServerIntFIoFsmTable": cfprEtherServerIntFIoFsmTable,
       "cfprEtherServerIntFIoFsmEntry": cfprEtherServerIntFIoFsmEntry,
       "cfprEtherServerIntFIoFsmInstanceId": cfprEtherServerIntFIoFsmInstanceId,
       "cfprEtherServerIntFIoFsmDn": cfprEtherServerIntFIoFsmDn,
       "cfprEtherServerIntFIoFsmRn": cfprEtherServerIntFIoFsmRn,
       "cfprEtherServerIntFIoFsmCompletionTime": cfprEtherServerIntFIoFsmCompletionTime,
       "cfprEtherServerIntFIoFsmCurrentFsm": cfprEtherServerIntFIoFsmCurrentFsm,
       "cfprEtherServerIntFIoFsmDescrData": cfprEtherServerIntFIoFsmDescrData,
       "cfprEtherServerIntFIoFsmFsmStatus": cfprEtherServerIntFIoFsmFsmStatus,
       "cfprEtherServerIntFIoFsmProgress": cfprEtherServerIntFIoFsmProgress,
       "cfprEtherServerIntFIoFsmRmtErrCode": cfprEtherServerIntFIoFsmRmtErrCode,
       "cfprEtherServerIntFIoFsmRmtErrDescr": cfprEtherServerIntFIoFsmRmtErrDescr,
       "cfprEtherServerIntFIoFsmRmtRslt": cfprEtherServerIntFIoFsmRmtRslt,
       "cfprEtherServerIntFIoFsmStageTable": cfprEtherServerIntFIoFsmStageTable,
       "cfprEtherServerIntFIoFsmStageEntry": cfprEtherServerIntFIoFsmStageEntry,
       "cfprEtherServerIntFIoFsmStageInstanceId": cfprEtherServerIntFIoFsmStageInstanceId,
       "cfprEtherServerIntFIoFsmStageDn": cfprEtherServerIntFIoFsmStageDn,
       "cfprEtherServerIntFIoFsmStageRn": cfprEtherServerIntFIoFsmStageRn,
       "cfprEtherServerIntFIoFsmStageDescrData": cfprEtherServerIntFIoFsmStageDescrData,
       "cfprEtherServerIntFIoFsmStageLastUpdateTime": cfprEtherServerIntFIoFsmStageLastUpdateTime,
       "cfprEtherServerIntFIoFsmStageName": cfprEtherServerIntFIoFsmStageName,
       "cfprEtherServerIntFIoFsmStageOrder": cfprEtherServerIntFIoFsmStageOrder,
       "cfprEtherServerIntFIoFsmStageRetry": cfprEtherServerIntFIoFsmStageRetry,
       "cfprEtherServerIntFIoFsmStageStageStatus": cfprEtherServerIntFIoFsmStageStageStatus,
       "cfprEtherServerIntFIoFsmTaskTable": cfprEtherServerIntFIoFsmTaskTable,
       "cfprEtherServerIntFIoFsmTaskEntry": cfprEtherServerIntFIoFsmTaskEntry,
       "cfprEtherServerIntFIoFsmTaskInstanceId": cfprEtherServerIntFIoFsmTaskInstanceId,
       "cfprEtherServerIntFIoFsmTaskDn": cfprEtherServerIntFIoFsmTaskDn,
       "cfprEtherServerIntFIoFsmTaskRn": cfprEtherServerIntFIoFsmTaskRn,
       "cfprEtherServerIntFIoFsmTaskCompletion": cfprEtherServerIntFIoFsmTaskCompletion,
       "cfprEtherServerIntFIoFsmTaskFlags": cfprEtherServerIntFIoFsmTaskFlags,
       "cfprEtherServerIntFIoFsmTaskItem": cfprEtherServerIntFIoFsmTaskItem,
       "cfprEtherServerIntFIoFsmTaskSeqId": cfprEtherServerIntFIoFsmTaskSeqId,
       "cfprEtherServerIntFIoPcTable": cfprEtherServerIntFIoPcTable,
       "cfprEtherServerIntFIoPcEntry": cfprEtherServerIntFIoPcEntry,
       "cfprEtherServerIntFIoPcInstanceId": cfprEtherServerIntFIoPcInstanceId,
       "cfprEtherServerIntFIoPcDn": cfprEtherServerIntFIoPcDn,
       "cfprEtherServerIntFIoPcRn": cfprEtherServerIntFIoPcRn,
       "cfprEtherServerIntFIoPcChassisId": cfprEtherServerIntFIoPcChassisId,
       "cfprEtherServerIntFIoPcEpDn": cfprEtherServerIntFIoPcEpDn,
       "cfprEtherServerIntFIoPcFltAggr": cfprEtherServerIntFIoPcFltAggr,
       "cfprEtherServerIntFIoPcIfRole": cfprEtherServerIntFIoPcIfRole,
       "cfprEtherServerIntFIoPcIfType": cfprEtherServerIntFIoPcIfType,
       "cfprEtherServerIntFIoPcLocale": cfprEtherServerIntFIoPcLocale,
       "cfprEtherServerIntFIoPcName": cfprEtherServerIntFIoPcName,
       "cfprEtherServerIntFIoPcOperSpeed": cfprEtherServerIntFIoPcOperSpeed,
       "cfprEtherServerIntFIoPcOperState": cfprEtherServerIntFIoPcOperState,
       "cfprEtherServerIntFIoPcPeerDn": cfprEtherServerIntFIoPcPeerDn,
       "cfprEtherServerIntFIoPcPortId": cfprEtherServerIntFIoPcPortId,
       "cfprEtherServerIntFIoPcStateQual": cfprEtherServerIntFIoPcStateQual,
       "cfprEtherServerIntFIoPcSwitchId": cfprEtherServerIntFIoPcSwitchId,
       "cfprEtherServerIntFIoPcTransport": cfprEtherServerIntFIoPcTransport,
       "cfprEtherServerIntFIoPcType": cfprEtherServerIntFIoPcType,
       "cfprEtherServerIntFIoPcEpTable": cfprEtherServerIntFIoPcEpTable,
       "cfprEtherServerIntFIoPcEpEntry": cfprEtherServerIntFIoPcEpEntry,
       "cfprEtherServerIntFIoPcEpInstanceId": cfprEtherServerIntFIoPcEpInstanceId,
       "cfprEtherServerIntFIoPcEpDnData": cfprEtherServerIntFIoPcEpDnData,
       "cfprEtherServerIntFIoPcEpRn": cfprEtherServerIntFIoPcEpRn,
       "cfprEtherServerIntFIoPcEpAdminState": cfprEtherServerIntFIoPcEpAdminState,
       "cfprEtherServerIntFIoPcEpAggrPortId": cfprEtherServerIntFIoPcEpAggrPortId,
       "cfprEtherServerIntFIoPcEpChassisId": cfprEtherServerIntFIoPcEpChassisId,
       "cfprEtherServerIntFIoPcEpEpDn": cfprEtherServerIntFIoPcEpEpDn,
       "cfprEtherServerIntFIoPcEpIfRole": cfprEtherServerIntFIoPcEpIfRole,
       "cfprEtherServerIntFIoPcEpIfType": cfprEtherServerIntFIoPcEpIfType,
       "cfprEtherServerIntFIoPcEpLocale": cfprEtherServerIntFIoPcEpLocale,
       "cfprEtherServerIntFIoPcEpMembership": cfprEtherServerIntFIoPcEpMembership,
       "cfprEtherServerIntFIoPcEpName": cfprEtherServerIntFIoPcEpName,
       "cfprEtherServerIntFIoPcEpPeerAggrPortId": cfprEtherServerIntFIoPcEpPeerAggrPortId,
       "cfprEtherServerIntFIoPcEpPeerChassisId": cfprEtherServerIntFIoPcEpPeerChassisId,
       "cfprEtherServerIntFIoPcEpPeerDn": cfprEtherServerIntFIoPcEpPeerDn,
       "cfprEtherServerIntFIoPcEpPeerPortId": cfprEtherServerIntFIoPcEpPeerPortId,
       "cfprEtherServerIntFIoPcEpPeerSlotId": cfprEtherServerIntFIoPcEpPeerSlotId,
       "cfprEtherServerIntFIoPcEpPortId": cfprEtherServerIntFIoPcEpPortId,
       "cfprEtherServerIntFIoPcEpSlotId": cfprEtherServerIntFIoPcEpSlotId,
       "cfprEtherServerIntFIoPcEpSwitchId": cfprEtherServerIntFIoPcEpSwitchId,
       "cfprEtherServerIntFIoPcEpTransport": cfprEtherServerIntFIoPcEpTransport,
       "cfprEtherServerIntFIoPcEpType": cfprEtherServerIntFIoPcEpType,
       "cfprEtherSwIfConfigTable": cfprEtherSwIfConfigTable,
       "cfprEtherSwIfConfigEntry": cfprEtherSwIfConfigEntry,
       "cfprEtherSwIfConfigInstanceId": cfprEtherSwIfConfigInstanceId,
       "cfprEtherSwIfConfigDn": cfprEtherSwIfConfigDn,
       "cfprEtherSwIfConfigRn": cfprEtherSwIfConfigRn,
       "cfprEtherSwitchIntFIoTable": cfprEtherSwitchIntFIoTable,
       "cfprEtherSwitchIntFIoEntry": cfprEtherSwitchIntFIoEntry,
       "cfprEtherSwitchIntFIoInstanceId": cfprEtherSwitchIntFIoInstanceId,
       "cfprEtherSwitchIntFIoDn": cfprEtherSwitchIntFIoDn,
       "cfprEtherSwitchIntFIoRn": cfprEtherSwitchIntFIoRn,
       "cfprEtherSwitchIntFIoAck": cfprEtherSwitchIntFIoAck,
       "cfprEtherSwitchIntFIoAdminState": cfprEtherSwitchIntFIoAdminState,
       "cfprEtherSwitchIntFIoAggrPortId": cfprEtherSwitchIntFIoAggrPortId,
       "cfprEtherSwitchIntFIoChassisId": cfprEtherSwitchIntFIoChassisId,
       "cfprEtherSwitchIntFIoDelFeTs": cfprEtherSwitchIntFIoDelFeTs,
       "cfprEtherSwitchIntFIoDiscovery": cfprEtherSwitchIntFIoDiscovery,
       "cfprEtherSwitchIntFIoEncap": cfprEtherSwitchIntFIoEncap,
       "cfprEtherSwitchIntFIoEpDn": cfprEtherSwitchIntFIoEpDn,
       "cfprEtherSwitchIntFIoFltAggr": cfprEtherSwitchIntFIoFltAggr,
       "cfprEtherSwitchIntFIoIfRole": cfprEtherSwitchIntFIoIfRole,
       "cfprEtherSwitchIntFIoIfType": cfprEtherSwitchIntFIoIfType,
       "cfprEtherSwitchIntFIoLocale": cfprEtherSwitchIntFIoLocale,
       "cfprEtherSwitchIntFIoMode": cfprEtherSwitchIntFIoMode,
       "cfprEtherSwitchIntFIoModel": cfprEtherSwitchIntFIoModel,
       "cfprEtherSwitchIntFIoName": cfprEtherSwitchIntFIoName,
       "cfprEtherSwitchIntFIoNewFeTs": cfprEtherSwitchIntFIoNewFeTs,
       "cfprEtherSwitchIntFIoOperState": cfprEtherSwitchIntFIoOperState,
       "cfprEtherSwitchIntFIoPeerAggrPortId": cfprEtherSwitchIntFIoPeerAggrPortId,
       "cfprEtherSwitchIntFIoPeerChassisId": cfprEtherSwitchIntFIoPeerChassisId,
       "cfprEtherSwitchIntFIoPeerDn": cfprEtherSwitchIntFIoPeerDn,
       "cfprEtherSwitchIntFIoPeerPortId": cfprEtherSwitchIntFIoPeerPortId,
       "cfprEtherSwitchIntFIoPeerSlotId": cfprEtherSwitchIntFIoPeerSlotId,
       "cfprEtherSwitchIntFIoPortId": cfprEtherSwitchIntFIoPortId,
       "cfprEtherSwitchIntFIoRevision": cfprEtherSwitchIntFIoRevision,
       "cfprEtherSwitchIntFIoSerial": cfprEtherSwitchIntFIoSerial,
       "cfprEtherSwitchIntFIoSlotId": cfprEtherSwitchIntFIoSlotId,
       "cfprEtherSwitchIntFIoStateQual": cfprEtherSwitchIntFIoStateQual,
       "cfprEtherSwitchIntFIoSwitchId": cfprEtherSwitchIntFIoSwitchId,
       "cfprEtherSwitchIntFIoTransport": cfprEtherSwitchIntFIoTransport,
       "cfprEtherSwitchIntFIoTs": cfprEtherSwitchIntFIoTs,
       "cfprEtherSwitchIntFIoType": cfprEtherSwitchIntFIoType,
       "cfprEtherSwitchIntFIoVendor": cfprEtherSwitchIntFIoVendor,
       "cfprEtherSwitchIntFIoXcvrType": cfprEtherSwitchIntFIoXcvrType,
       "cfprEtherSwitchIntFIoPcTable": cfprEtherSwitchIntFIoPcTable,
       "cfprEtherSwitchIntFIoPcEntry": cfprEtherSwitchIntFIoPcEntry,
       "cfprEtherSwitchIntFIoPcInstanceId": cfprEtherSwitchIntFIoPcInstanceId,
       "cfprEtherSwitchIntFIoPcDn": cfprEtherSwitchIntFIoPcDn,
       "cfprEtherSwitchIntFIoPcRn": cfprEtherSwitchIntFIoPcRn,
       "cfprEtherSwitchIntFIoPcAdminState": cfprEtherSwitchIntFIoPcAdminState,
       "cfprEtherSwitchIntFIoPcChassisId": cfprEtherSwitchIntFIoPcChassisId,
       "cfprEtherSwitchIntFIoPcEpDn": cfprEtherSwitchIntFIoPcEpDn,
       "cfprEtherSwitchIntFIoPcFltAggr": cfprEtherSwitchIntFIoPcFltAggr,
       "cfprEtherSwitchIntFIoPcIfRole": cfprEtherSwitchIntFIoPcIfRole,
       "cfprEtherSwitchIntFIoPcIfType": cfprEtherSwitchIntFIoPcIfType,
       "cfprEtherSwitchIntFIoPcLocale": cfprEtherSwitchIntFIoPcLocale,
       "cfprEtherSwitchIntFIoPcName": cfprEtherSwitchIntFIoPcName,
       "cfprEtherSwitchIntFIoPcOperSpeed": cfprEtherSwitchIntFIoPcOperSpeed,
       "cfprEtherSwitchIntFIoPcOperState": cfprEtherSwitchIntFIoPcOperState,
       "cfprEtherSwitchIntFIoPcPeerDn": cfprEtherSwitchIntFIoPcPeerDn,
       "cfprEtherSwitchIntFIoPcPortId": cfprEtherSwitchIntFIoPcPortId,
       "cfprEtherSwitchIntFIoPcStateQual": cfprEtherSwitchIntFIoPcStateQual,
       "cfprEtherSwitchIntFIoPcSwitchId": cfprEtherSwitchIntFIoPcSwitchId,
       "cfprEtherSwitchIntFIoPcTransport": cfprEtherSwitchIntFIoPcTransport,
       "cfprEtherSwitchIntFIoPcType": cfprEtherSwitchIntFIoPcType,
       "cfprEtherSwitchIntFIoPcEpTable": cfprEtherSwitchIntFIoPcEpTable,
       "cfprEtherSwitchIntFIoPcEpEntry": cfprEtherSwitchIntFIoPcEpEntry,
       "cfprEtherSwitchIntFIoPcEpInstanceId": cfprEtherSwitchIntFIoPcEpInstanceId,
       "cfprEtherSwitchIntFIoPcEpDnData": cfprEtherSwitchIntFIoPcEpDnData,
       "cfprEtherSwitchIntFIoPcEpRn": cfprEtherSwitchIntFIoPcEpRn,
       "cfprEtherSwitchIntFIoPcEpAckState": cfprEtherSwitchIntFIoPcEpAckState,
       "cfprEtherSwitchIntFIoPcEpAdminState": cfprEtherSwitchIntFIoPcEpAdminState,
       "cfprEtherSwitchIntFIoPcEpAggrPortId": cfprEtherSwitchIntFIoPcEpAggrPortId,
       "cfprEtherSwitchIntFIoPcEpChassisId": cfprEtherSwitchIntFIoPcEpChassisId,
       "cfprEtherSwitchIntFIoPcEpEpDn": cfprEtherSwitchIntFIoPcEpEpDn,
       "cfprEtherSwitchIntFIoPcEpIfRole": cfprEtherSwitchIntFIoPcEpIfRole,
       "cfprEtherSwitchIntFIoPcEpIfType": cfprEtherSwitchIntFIoPcEpIfType,
       "cfprEtherSwitchIntFIoPcEpLocale": cfprEtherSwitchIntFIoPcEpLocale,
       "cfprEtherSwitchIntFIoPcEpMembership": cfprEtherSwitchIntFIoPcEpMembership,
       "cfprEtherSwitchIntFIoPcEpName": cfprEtherSwitchIntFIoPcEpName,
       "cfprEtherSwitchIntFIoPcEpPeerAggrPortId": cfprEtherSwitchIntFIoPcEpPeerAggrPortId,
       "cfprEtherSwitchIntFIoPcEpPeerChassisId": cfprEtherSwitchIntFIoPcEpPeerChassisId,
       "cfprEtherSwitchIntFIoPcEpPeerDn": cfprEtherSwitchIntFIoPcEpPeerDn,
       "cfprEtherSwitchIntFIoPcEpPeerPortId": cfprEtherSwitchIntFIoPcEpPeerPortId,
       "cfprEtherSwitchIntFIoPcEpPeerSlotId": cfprEtherSwitchIntFIoPcEpPeerSlotId,
       "cfprEtherSwitchIntFIoPcEpPortId": cfprEtherSwitchIntFIoPcEpPortId,
       "cfprEtherSwitchIntFIoPcEpSlotId": cfprEtherSwitchIntFIoPcEpSlotId,
       "cfprEtherSwitchIntFIoPcEpStatusChangeTs": cfprEtherSwitchIntFIoPcEpStatusChangeTs,
       "cfprEtherSwitchIntFIoPcEpSwitchId": cfprEtherSwitchIntFIoPcEpSwitchId,
       "cfprEtherSwitchIntFIoPcEpTransport": cfprEtherSwitchIntFIoPcEpTransport,
       "cfprEtherSwitchIntFIoPcEpType": cfprEtherSwitchIntFIoPcEpType,
       "cfprEtherTxStatsTable": cfprEtherTxStatsTable,
       "cfprEtherTxStatsEntry": cfprEtherTxStatsEntry,
       "cfprEtherTxStatsInstanceId": cfprEtherTxStatsInstanceId,
       "cfprEtherTxStatsDn": cfprEtherTxStatsDn,
       "cfprEtherTxStatsRn": cfprEtherTxStatsRn,
       "cfprEtherTxStatsBroadcastPackets": cfprEtherTxStatsBroadcastPackets,
       "cfprEtherTxStatsBroadcastPacketsDelta": cfprEtherTxStatsBroadcastPacketsDelta,
       "cfprEtherTxStatsBroadcastPacketsDeltaAvg": cfprEtherTxStatsBroadcastPacketsDeltaAvg,
       "cfprEtherTxStatsBroadcastPacketsDeltaMax": cfprEtherTxStatsBroadcastPacketsDeltaMax,
       "cfprEtherTxStatsBroadcastPacketsDeltaMin": cfprEtherTxStatsBroadcastPacketsDeltaMin,
       "cfprEtherTxStatsIntervals": cfprEtherTxStatsIntervals,
       "cfprEtherTxStatsJumboPackets": cfprEtherTxStatsJumboPackets,
       "cfprEtherTxStatsJumboPacketsDelta": cfprEtherTxStatsJumboPacketsDelta,
       "cfprEtherTxStatsJumboPacketsDeltaAvg": cfprEtherTxStatsJumboPacketsDeltaAvg,
       "cfprEtherTxStatsJumboPacketsDeltaMax": cfprEtherTxStatsJumboPacketsDeltaMax,
       "cfprEtherTxStatsJumboPacketsDeltaMin": cfprEtherTxStatsJumboPacketsDeltaMin,
       "cfprEtherTxStatsMulticastPackets": cfprEtherTxStatsMulticastPackets,
       "cfprEtherTxStatsMulticastPacketsDelta": cfprEtherTxStatsMulticastPacketsDelta,
       "cfprEtherTxStatsMulticastPacketsDeltaAvg": cfprEtherTxStatsMulticastPacketsDeltaAvg,
       "cfprEtherTxStatsMulticastPacketsDeltaMax": cfprEtherTxStatsMulticastPacketsDeltaMax,
       "cfprEtherTxStatsMulticastPacketsDeltaMin": cfprEtherTxStatsMulticastPacketsDeltaMin,
       "cfprEtherTxStatsSuspect": cfprEtherTxStatsSuspect,
       "cfprEtherTxStatsThresholded": cfprEtherTxStatsThresholded,
       "cfprEtherTxStatsTimeCollected": cfprEtherTxStatsTimeCollected,
       "cfprEtherTxStatsTotalBytes": cfprEtherTxStatsTotalBytes,
       "cfprEtherTxStatsTotalBytesDelta": cfprEtherTxStatsTotalBytesDelta,
       "cfprEtherTxStatsTotalBytesDeltaAvg": cfprEtherTxStatsTotalBytesDeltaAvg,
       "cfprEtherTxStatsTotalBytesDeltaMax": cfprEtherTxStatsTotalBytesDeltaMax,
       "cfprEtherTxStatsTotalBytesDeltaMin": cfprEtherTxStatsTotalBytesDeltaMin,
       "cfprEtherTxStatsTotalPackets": cfprEtherTxStatsTotalPackets,
       "cfprEtherTxStatsTotalPacketsDelta": cfprEtherTxStatsTotalPacketsDelta,
       "cfprEtherTxStatsTotalPacketsDeltaAvg": cfprEtherTxStatsTotalPacketsDeltaAvg,
       "cfprEtherTxStatsTotalPacketsDeltaMax": cfprEtherTxStatsTotalPacketsDeltaMax,
       "cfprEtherTxStatsTotalPacketsDeltaMin": cfprEtherTxStatsTotalPacketsDeltaMin,
       "cfprEtherTxStatsUnicastPackets": cfprEtherTxStatsUnicastPackets,
       "cfprEtherTxStatsUnicastPacketsDelta": cfprEtherTxStatsUnicastPacketsDelta,
       "cfprEtherTxStatsUnicastPacketsDeltaAvg": cfprEtherTxStatsUnicastPacketsDeltaAvg,
       "cfprEtherTxStatsUnicastPacketsDeltaMax": cfprEtherTxStatsUnicastPacketsDeltaMax,
       "cfprEtherTxStatsUnicastPacketsDeltaMin": cfprEtherTxStatsUnicastPacketsDeltaMin,
       "cfprEtherTxStatsUpdate": cfprEtherTxStatsUpdate,
       "cfprEtherTxStatsHistTable": cfprEtherTxStatsHistTable,
       "cfprEtherTxStatsHistEntry": cfprEtherTxStatsHistEntry,
       "cfprEtherTxStatsHistInstanceId": cfprEtherTxStatsHistInstanceId,
       "cfprEtherTxStatsHistDn": cfprEtherTxStatsHistDn,
       "cfprEtherTxStatsHistRn": cfprEtherTxStatsHistRn,
       "cfprEtherTxStatsHistBroadcastPackets": cfprEtherTxStatsHistBroadcastPackets,
       "cfprEtherTxStatsHistBroadcastPacketsDelta": cfprEtherTxStatsHistBroadcastPacketsDelta,
       "cfprEtherTxStatsHistBroadcastPacketsDeltaAvg": cfprEtherTxStatsHistBroadcastPacketsDeltaAvg,
       "cfprEtherTxStatsHistBroadcastPacketsDeltaMax": cfprEtherTxStatsHistBroadcastPacketsDeltaMax,
       "cfprEtherTxStatsHistBroadcastPacketsDeltaMin": cfprEtherTxStatsHistBroadcastPacketsDeltaMin,
       "cfprEtherTxStatsHistId": cfprEtherTxStatsHistId,
       "cfprEtherTxStatsHistJumboPackets": cfprEtherTxStatsHistJumboPackets,
       "cfprEtherTxStatsHistJumboPacketsDelta": cfprEtherTxStatsHistJumboPacketsDelta,
       "cfprEtherTxStatsHistJumboPacketsDeltaAvg": cfprEtherTxStatsHistJumboPacketsDeltaAvg,
       "cfprEtherTxStatsHistJumboPacketsDeltaMax": cfprEtherTxStatsHistJumboPacketsDeltaMax,
       "cfprEtherTxStatsHistJumboPacketsDeltaMin": cfprEtherTxStatsHistJumboPacketsDeltaMin,
       "cfprEtherTxStatsHistMostRecent": cfprEtherTxStatsHistMostRecent,
       "cfprEtherTxStatsHistMulticastPackets": cfprEtherTxStatsHistMulticastPackets,
       "cfprEtherTxStatsHistMulticastPacketsDelta": cfprEtherTxStatsHistMulticastPacketsDelta,
       "cfprEtherTxStatsHistMulticastPacketsDeltaAvg": cfprEtherTxStatsHistMulticastPacketsDeltaAvg,
       "cfprEtherTxStatsHistMulticastPacketsDeltaMax": cfprEtherTxStatsHistMulticastPacketsDeltaMax,
       "cfprEtherTxStatsHistMulticastPacketsDeltaMin": cfprEtherTxStatsHistMulticastPacketsDeltaMin,
       "cfprEtherTxStatsHistSuspect": cfprEtherTxStatsHistSuspect,
       "cfprEtherTxStatsHistThresholded": cfprEtherTxStatsHistThresholded,
       "cfprEtherTxStatsHistTimeCollected": cfprEtherTxStatsHistTimeCollected,
       "cfprEtherTxStatsHistTotalBytes": cfprEtherTxStatsHistTotalBytes,
       "cfprEtherTxStatsHistTotalBytesDelta": cfprEtherTxStatsHistTotalBytesDelta,
       "cfprEtherTxStatsHistTotalBytesDeltaAvg": cfprEtherTxStatsHistTotalBytesDeltaAvg,
       "cfprEtherTxStatsHistTotalBytesDeltaMax": cfprEtherTxStatsHistTotalBytesDeltaMax,
       "cfprEtherTxStatsHistTotalBytesDeltaMin": cfprEtherTxStatsHistTotalBytesDeltaMin,
       "cfprEtherTxStatsHistTotalPackets": cfprEtherTxStatsHistTotalPackets,
       "cfprEtherTxStatsHistTotalPacketsDelta": cfprEtherTxStatsHistTotalPacketsDelta,
       "cfprEtherTxStatsHistTotalPacketsDeltaAvg": cfprEtherTxStatsHistTotalPacketsDeltaAvg,
       "cfprEtherTxStatsHistTotalPacketsDeltaMax": cfprEtherTxStatsHistTotalPacketsDeltaMax,
       "cfprEtherTxStatsHistTotalPacketsDeltaMin": cfprEtherTxStatsHistTotalPacketsDeltaMin,
       "cfprEtherTxStatsHistUnicastPackets": cfprEtherTxStatsHistUnicastPackets,
       "cfprEtherTxStatsHistUnicastPacketsDelta": cfprEtherTxStatsHistUnicastPacketsDelta,
       "cfprEtherTxStatsHistUnicastPacketsDeltaAvg": cfprEtherTxStatsHistUnicastPacketsDeltaAvg,
       "cfprEtherTxStatsHistUnicastPacketsDeltaMax": cfprEtherTxStatsHistUnicastPacketsDeltaMax,
       "cfprEtherTxStatsHistUnicastPacketsDeltaMin": cfprEtherTxStatsHistUnicastPacketsDeltaMin,
       "cfprEtherFailToWireTable": cfprEtherFailToWireTable,
       "cfprEtherFailToWireEntry": cfprEtherFailToWireEntry,
       "cfprEtherFailToWireInstanceId": cfprEtherFailToWireInstanceId,
       "cfprEtherFailToWireDn": cfprEtherFailToWireDn,
       "cfprEtherFailToWireRn": cfprEtherFailToWireRn,
       "cfprEtherFailToWireLocale": cfprEtherFailToWireLocale,
       "cfprEtherFailToWireName": cfprEtherFailToWireName,
       "cfprEtherFailToWireTransport": cfprEtherFailToWireTransport,
       "cfprEtherFailToWireType": cfprEtherFailToWireType,
       "cfprEtherFtwPortPairTable": cfprEtherFtwPortPairTable,
       "cfprEtherFtwPortPairEntry": cfprEtherFtwPortPairEntry,
       "cfprEtherFtwPortPairInstanceId": cfprEtherFtwPortPairInstanceId,
       "cfprEtherFtwPortPairDn": cfprEtherFtwPortPairDn,
       "cfprEtherFtwPortPairRn": cfprEtherFtwPortPairRn,
       "cfprEtherFtwPortPairAggrPortId": cfprEtherFtwPortPairAggrPortId,
       "cfprEtherFtwPortPairChassisId": cfprEtherFtwPortPairChassisId,
       "cfprEtherFtwPortPairEpDn": cfprEtherFtwPortPairEpDn,
       "cfprEtherFtwPortPairFsmDescr": cfprEtherFtwPortPairFsmDescr,
       "cfprEtherFtwPortPairFsmPrev": cfprEtherFtwPortPairFsmPrev,
       "cfprEtherFtwPortPairFsmProgr": cfprEtherFtwPortPairFsmProgr,
       "cfprEtherFtwPortPairFsmRmtInvErrCode": cfprEtherFtwPortPairFsmRmtInvErrCode,
       "cfprEtherFtwPortPairFsmRmtInvErrDescr": cfprEtherFtwPortPairFsmRmtInvErrDescr,
       "cfprEtherFtwPortPairFsmRmtInvRslt": cfprEtherFtwPortPairFsmRmtInvRslt,
       "cfprEtherFtwPortPairFsmStageDescr": cfprEtherFtwPortPairFsmStageDescr,
       "cfprEtherFtwPortPairFsmStamp": cfprEtherFtwPortPairFsmStamp,
       "cfprEtherFtwPortPairFsmStatus": cfprEtherFtwPortPairFsmStatus,
       "cfprEtherFtwPortPairFsmTry": cfprEtherFtwPortPairFsmTry,
       "cfprEtherFtwPortPairIfRole": cfprEtherFtwPortPairIfRole,
       "cfprEtherFtwPortPairIfType": cfprEtherFtwPortPairIfType,
       "cfprEtherFtwPortPairLocale": cfprEtherFtwPortPairLocale,
       "cfprEtherFtwPortPairMode": cfprEtherFtwPortPairMode,
       "cfprEtherFtwPortPairName": cfprEtherFtwPortPairName,
       "cfprEtherFtwPortPairOperMode": cfprEtherFtwPortPairOperMode,
       "cfprEtherFtwPortPairPeerAggrPortId": cfprEtherFtwPortPairPeerAggrPortId,
       "cfprEtherFtwPortPairPeerChassisId": cfprEtherFtwPortPairPeerChassisId,
       "cfprEtherFtwPortPairPeerDn": cfprEtherFtwPortPairPeerDn,
       "cfprEtherFtwPortPairPeerPortId": cfprEtherFtwPortPairPeerPortId,
       "cfprEtherFtwPortPairPeerPortName": cfprEtherFtwPortPairPeerPortName,
       "cfprEtherFtwPortPairPeerSlotId": cfprEtherFtwPortPairPeerSlotId,
       "cfprEtherFtwPortPairPortId": cfprEtherFtwPortPairPortId,
       "cfprEtherFtwPortPairPortName": cfprEtherFtwPortPairPortName,
       "cfprEtherFtwPortPairSlotId": cfprEtherFtwPortPairSlotId,
       "cfprEtherFtwPortPairSwitchId": cfprEtherFtwPortPairSwitchId,
       "cfprEtherFtwPortPairTransport": cfprEtherFtwPortPairTransport,
       "cfprEtherFtwPortPairTs": cfprEtherFtwPortPairTs,
       "cfprEtherFtwPortPairType": cfprEtherFtwPortPairType,
       "cfprEtherFtwPortPairWdtStart": cfprEtherFtwPortPairWdtStart,
       "cfprEtherFtwPortPairWdtState": cfprEtherFtwPortPairWdtState,
       "cfprEtherFtwPortPairFsmTable": cfprEtherFtwPortPairFsmTable,
       "cfprEtherFtwPortPairFsmEntry": cfprEtherFtwPortPairFsmEntry,
       "cfprEtherFtwPortPairFsmInstanceId": cfprEtherFtwPortPairFsmInstanceId,
       "cfprEtherFtwPortPairFsmDn": cfprEtherFtwPortPairFsmDn,
       "cfprEtherFtwPortPairFsmRn": cfprEtherFtwPortPairFsmRn,
       "cfprEtherFtwPortPairFsmCompletionTime": cfprEtherFtwPortPairFsmCompletionTime,
       "cfprEtherFtwPortPairFsmCurrentFsm": cfprEtherFtwPortPairFsmCurrentFsm,
       "cfprEtherFtwPortPairFsmDescrData": cfprEtherFtwPortPairFsmDescrData,
       "cfprEtherFtwPortPairFsmFsmStatus": cfprEtherFtwPortPairFsmFsmStatus,
       "cfprEtherFtwPortPairFsmProgress": cfprEtherFtwPortPairFsmProgress,
       "cfprEtherFtwPortPairFsmRmtErrCode": cfprEtherFtwPortPairFsmRmtErrCode,
       "cfprEtherFtwPortPairFsmRmtErrDescr": cfprEtherFtwPortPairFsmRmtErrDescr,
       "cfprEtherFtwPortPairFsmRmtRslt": cfprEtherFtwPortPairFsmRmtRslt,
       "cfprEtherFtwPortPairFsmStageTable": cfprEtherFtwPortPairFsmStageTable,
       "cfprEtherFtwPortPairFsmStageEntry": cfprEtherFtwPortPairFsmStageEntry,
       "cfprEtherFtwPortPairFsmStageInstanceId": cfprEtherFtwPortPairFsmStageInstanceId,
       "cfprEtherFtwPortPairFsmStageDn": cfprEtherFtwPortPairFsmStageDn,
       "cfprEtherFtwPortPairFsmStageRn": cfprEtherFtwPortPairFsmStageRn,
       "cfprEtherFtwPortPairFsmStageDescrData": cfprEtherFtwPortPairFsmStageDescrData,
       "cfprEtherFtwPortPairFsmStageLastUpdateTime": cfprEtherFtwPortPairFsmStageLastUpdateTime,
       "cfprEtherFtwPortPairFsmStageName": cfprEtherFtwPortPairFsmStageName,
       "cfprEtherFtwPortPairFsmStageOrder": cfprEtherFtwPortPairFsmStageOrder,
       "cfprEtherFtwPortPairFsmStageRetry": cfprEtherFtwPortPairFsmStageRetry,
       "cfprEtherFtwPortPairFsmStageStageStatus": cfprEtherFtwPortPairFsmStageStageStatus,
       "cfprEtherFtwPortPairFsmTaskTable": cfprEtherFtwPortPairFsmTaskTable,
       "cfprEtherFtwPortPairFsmTaskEntry": cfprEtherFtwPortPairFsmTaskEntry,
       "cfprEtherFtwPortPairFsmTaskInstanceId": cfprEtherFtwPortPairFsmTaskInstanceId,
       "cfprEtherFtwPortPairFsmTaskDn": cfprEtherFtwPortPairFsmTaskDn,
       "cfprEtherFtwPortPairFsmTaskRn": cfprEtherFtwPortPairFsmTaskRn,
       "cfprEtherFtwPortPairFsmTaskCompletion": cfprEtherFtwPortPairFsmTaskCompletion,
       "cfprEtherFtwPortPairFsmTaskFlags": cfprEtherFtwPortPairFsmTaskFlags,
       "cfprEtherFtwPortPairFsmTaskItem": cfprEtherFtwPortPairFsmTaskItem,
       "cfprEtherFtwPortPairFsmTaskSeqId": cfprEtherFtwPortPairFsmTaskSeqId}
)
