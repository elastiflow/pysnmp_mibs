# SNMP MIB module (CISCO-FIREPOWER-AP-ETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-ETHER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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

(CfprApConditionRemoteInvRslt,
 CfprApEquipmentChassisConfigState,
 CfprApEquipmentXcvrType,
 CfprApEtherCIoEpIfType,
 CfprApEtherCloudType,
 CfprApEtherErrStatsHistThresholded,
 CfprApEtherErrStatsThresholded,
 CfprApEtherExternalEpAdminState,
 CfprApEtherExternalEpLocale,
 CfprApEtherExternalPcAdminState,
 CfprApEtherExternalPcLocale,
 CfprApEtherFcoeInterfaceStatsHistThresholded,
 CfprApEtherFcoeInterfaceStatsThresholded,
 CfprApEtherFtwOperMode,
 CfprApEtherFtwPortPairFsmCurrentFsm,
 CfprApEtherFtwPortPairFsmStageName,
 CfprApEtherFtwPortPairFsmTaskItem,
 CfprApEtherFtwPortPairMode,
 CfprApEtherFtwPortPairWdtState,
 CfprApEtherIntFIoEpType,
 CfprApEtherInternalPcLocale,
 CfprApEtherLossStatsHistThresholded,
 CfprApEtherLossStatsThresholded,
 CfprApEtherNiErrStatsHistThresholded,
 CfprApEtherNiErrStatsThresholded,
 CfprApEtherPIoEpIfType,
 CfprApEtherPIoFsmCurrentFsm,
 CfprApEtherPIoFsmStageName,
 CfprApEtherPauseStatsHistThresholded,
 CfprApEtherPauseStatsThresholded,
 CfprApEtherRxStatsHistThresholded,
 CfprApEtherRxStatsThresholded,
 CfprApEtherSatelliteConnectionDisc,
 CfprApEtherServerIntFIoAdminState,
 CfprApEtherServerIntFIoFsmCurrentFsm,
 CfprApEtherServerIntFIoFsmStageName,
 CfprApEtherServerIntFIoFsmTaskItem,
 CfprApEtherServerIntFIoIfRole,
 CfprApEtherServerIntFIoLocale,
 CfprApEtherServerIntFIoPcEpIfRole,
 CfprApEtherServerIntFIoPcEpPortId,
 CfprApEtherServerIntFIoPcIfRole,
 CfprApEtherServerIntFIoPcPortId,
 CfprApEtherServerIntFIoPcTransport,
 CfprApEtherServerIntFIoPcType,
 CfprApEtherServerIntFIoTransport,
 CfprApEtherServerIntFIoType,
 CfprApEtherSwitchIntFIoAck,
 CfprApEtherSwitchIntFIoIfRole,
 CfprApEtherSwitchIntFIoLocale,
 CfprApEtherSwitchIntFIoPcEpIfRole,
 CfprApEtherSwitchIntFIoPcEpPortId,
 CfprApEtherSwitchIntFIoPcIfRole,
 CfprApEtherSwitchIntFIoPcPortId,
 CfprApEtherSwitchIntFIoPcTransport,
 CfprApEtherSwitchIntFIoPcType,
 CfprApEtherSwitchIntFIoTransport,
 CfprApEtherSwitchIntFIoType,
 CfprApEtherTxStatsHistThresholded,
 CfprApEtherTxStatsThresholded,
 CfprApFabricAdminState,
 CfprApFabricMembershipStatus,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApFsmLifecycle,
 CfprApLicenseState,
 CfprApNetworkConnectionType,
 CfprApNetworkLocale,
 CfprApNetworkPhysEpIfType,
 CfprApNetworkPortOperState,
 CfprApNetworkPortRole,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApPortDuplex,
 CfprApPortEncap,
 CfprApPortEthSpeed,
 CfprApPortMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApEquipmentChassisConfigState",
    "CfprApEquipmentXcvrType",
    "CfprApEtherCIoEpIfType",
    "CfprApEtherCloudType",
    "CfprApEtherErrStatsHistThresholded",
    "CfprApEtherErrStatsThresholded",
    "CfprApEtherExternalEpAdminState",
    "CfprApEtherExternalEpLocale",
    "CfprApEtherExternalPcAdminState",
    "CfprApEtherExternalPcLocale",
    "CfprApEtherFcoeInterfaceStatsHistThresholded",
    "CfprApEtherFcoeInterfaceStatsThresholded",
    "CfprApEtherFtwOperMode",
    "CfprApEtherFtwPortPairFsmCurrentFsm",
    "CfprApEtherFtwPortPairFsmStageName",
    "CfprApEtherFtwPortPairFsmTaskItem",
    "CfprApEtherFtwPortPairMode",
    "CfprApEtherFtwPortPairWdtState",
    "CfprApEtherIntFIoEpType",
    "CfprApEtherInternalPcLocale",
    "CfprApEtherLossStatsHistThresholded",
    "CfprApEtherLossStatsThresholded",
    "CfprApEtherNiErrStatsHistThresholded",
    "CfprApEtherNiErrStatsThresholded",
    "CfprApEtherPIoEpIfType",
    "CfprApEtherPIoFsmCurrentFsm",
    "CfprApEtherPIoFsmStageName",
    "CfprApEtherPauseStatsHistThresholded",
    "CfprApEtherPauseStatsThresholded",
    "CfprApEtherRxStatsHistThresholded",
    "CfprApEtherRxStatsThresholded",
    "CfprApEtherSatelliteConnectionDisc",
    "CfprApEtherServerIntFIoAdminState",
    "CfprApEtherServerIntFIoFsmCurrentFsm",
    "CfprApEtherServerIntFIoFsmStageName",
    "CfprApEtherServerIntFIoFsmTaskItem",
    "CfprApEtherServerIntFIoIfRole",
    "CfprApEtherServerIntFIoLocale",
    "CfprApEtherServerIntFIoPcEpIfRole",
    "CfprApEtherServerIntFIoPcEpPortId",
    "CfprApEtherServerIntFIoPcIfRole",
    "CfprApEtherServerIntFIoPcPortId",
    "CfprApEtherServerIntFIoPcTransport",
    "CfprApEtherServerIntFIoPcType",
    "CfprApEtherServerIntFIoTransport",
    "CfprApEtherServerIntFIoType",
    "CfprApEtherSwitchIntFIoAck",
    "CfprApEtherSwitchIntFIoIfRole",
    "CfprApEtherSwitchIntFIoLocale",
    "CfprApEtherSwitchIntFIoPcEpIfRole",
    "CfprApEtherSwitchIntFIoPcEpPortId",
    "CfprApEtherSwitchIntFIoPcIfRole",
    "CfprApEtherSwitchIntFIoPcPortId",
    "CfprApEtherSwitchIntFIoPcTransport",
    "CfprApEtherSwitchIntFIoPcType",
    "CfprApEtherSwitchIntFIoTransport",
    "CfprApEtherSwitchIntFIoType",
    "CfprApEtherTxStatsHistThresholded",
    "CfprApEtherTxStatsThresholded",
    "CfprApFabricAdminState",
    "CfprApFabricMembershipStatus",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApFsmLifecycle",
    "CfprApLicenseState",
    "CfprApNetworkConnectionType",
    "CfprApNetworkLocale",
    "CfprApNetworkPhysEpIfType",
    "CfprApNetworkPortOperState",
    "CfprApNetworkPortRole",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
    "CfprApPortDuplex",
    "CfprApPortEncap",
    "CfprApPortEthSpeed",
    "CfprApPortMode")

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

cfprApEtherObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApEtherErrStatsTable_Object = MibTable
cfprApEtherErrStatsTable = _CfprApEtherErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    cfprApEtherErrStatsTable.setStatus("current")
_CfprApEtherErrStatsEntry_Object = MibTableRow
cfprApEtherErrStatsEntry = _CfprApEtherErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1)
)
cfprApEtherErrStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherErrStatsEntry.setStatus("current")
_CfprApEtherErrStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherErrStatsInstanceId_Object = MibTableColumn
cfprApEtherErrStatsInstanceId = _CfprApEtherErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 1),
    _CfprApEtherErrStatsInstanceId_Type()
)
cfprApEtherErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsInstanceId.setStatus("current")
_CfprApEtherErrStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherErrStatsDn_Object = MibTableColumn
cfprApEtherErrStatsDn = _CfprApEtherErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 2),
    _CfprApEtherErrStatsDn_Type()
)
cfprApEtherErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsDn.setStatus("current")
_CfprApEtherErrStatsRn_Type = SnmpAdminString
_CfprApEtherErrStatsRn_Object = MibTableColumn
cfprApEtherErrStatsRn = _CfprApEtherErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 3),
    _CfprApEtherErrStatsRn_Type()
)
cfprApEtherErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsRn.setStatus("current")
_CfprApEtherErrStatsAlign_Type = Unsigned64
_CfprApEtherErrStatsAlign_Object = MibTableColumn
cfprApEtherErrStatsAlign = _CfprApEtherErrStatsAlign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 4),
    _CfprApEtherErrStatsAlign_Type()
)
cfprApEtherErrStatsAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsAlign.setStatus("current")
_CfprApEtherErrStatsAlignDelta_Type = Counter64
_CfprApEtherErrStatsAlignDelta_Object = MibTableColumn
cfprApEtherErrStatsAlignDelta = _CfprApEtherErrStatsAlignDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 5),
    _CfprApEtherErrStatsAlignDelta_Type()
)
cfprApEtherErrStatsAlignDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsAlignDelta.setStatus("current")
_CfprApEtherErrStatsAlignDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsAlignDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsAlignDeltaAvg = _CfprApEtherErrStatsAlignDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 6),
    _CfprApEtherErrStatsAlignDeltaAvg_Type()
)
cfprApEtherErrStatsAlignDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsAlignDeltaAvg.setStatus("current")
_CfprApEtherErrStatsAlignDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsAlignDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsAlignDeltaMax = _CfprApEtherErrStatsAlignDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 7),
    _CfprApEtherErrStatsAlignDeltaMax_Type()
)
cfprApEtherErrStatsAlignDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsAlignDeltaMax.setStatus("current")
_CfprApEtherErrStatsAlignDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsAlignDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsAlignDeltaMin = _CfprApEtherErrStatsAlignDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 8),
    _CfprApEtherErrStatsAlignDeltaMin_Type()
)
cfprApEtherErrStatsAlignDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsAlignDeltaMin.setStatus("current")
_CfprApEtherErrStatsDeferredTx_Type = Unsigned64
_CfprApEtherErrStatsDeferredTx_Object = MibTableColumn
cfprApEtherErrStatsDeferredTx = _CfprApEtherErrStatsDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 9),
    _CfprApEtherErrStatsDeferredTx_Type()
)
cfprApEtherErrStatsDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsDeferredTx.setStatus("current")
_CfprApEtherErrStatsDeferredTxDelta_Type = Counter64
_CfprApEtherErrStatsDeferredTxDelta_Object = MibTableColumn
cfprApEtherErrStatsDeferredTxDelta = _CfprApEtherErrStatsDeferredTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 10),
    _CfprApEtherErrStatsDeferredTxDelta_Type()
)
cfprApEtherErrStatsDeferredTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsDeferredTxDelta.setStatus("current")
_CfprApEtherErrStatsDeferredTxDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsDeferredTxDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsDeferredTxDeltaAvg = _CfprApEtherErrStatsDeferredTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 11),
    _CfprApEtherErrStatsDeferredTxDeltaAvg_Type()
)
cfprApEtherErrStatsDeferredTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsDeferredTxDeltaAvg.setStatus("current")
_CfprApEtherErrStatsDeferredTxDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsDeferredTxDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsDeferredTxDeltaMax = _CfprApEtherErrStatsDeferredTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 12),
    _CfprApEtherErrStatsDeferredTxDeltaMax_Type()
)
cfprApEtherErrStatsDeferredTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsDeferredTxDeltaMax.setStatus("current")
_CfprApEtherErrStatsDeferredTxDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsDeferredTxDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsDeferredTxDeltaMin = _CfprApEtherErrStatsDeferredTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 13),
    _CfprApEtherErrStatsDeferredTxDeltaMin_Type()
)
cfprApEtherErrStatsDeferredTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsDeferredTxDeltaMin.setStatus("current")
_CfprApEtherErrStatsFcs_Type = Unsigned64
_CfprApEtherErrStatsFcs_Object = MibTableColumn
cfprApEtherErrStatsFcs = _CfprApEtherErrStatsFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 14),
    _CfprApEtherErrStatsFcs_Type()
)
cfprApEtherErrStatsFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsFcs.setStatus("current")
_CfprApEtherErrStatsFcsDelta_Type = Counter64
_CfprApEtherErrStatsFcsDelta_Object = MibTableColumn
cfprApEtherErrStatsFcsDelta = _CfprApEtherErrStatsFcsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 15),
    _CfprApEtherErrStatsFcsDelta_Type()
)
cfprApEtherErrStatsFcsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsFcsDelta.setStatus("current")
_CfprApEtherErrStatsFcsDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsFcsDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsFcsDeltaAvg = _CfprApEtherErrStatsFcsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 16),
    _CfprApEtherErrStatsFcsDeltaAvg_Type()
)
cfprApEtherErrStatsFcsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsFcsDeltaAvg.setStatus("current")
_CfprApEtherErrStatsFcsDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsFcsDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsFcsDeltaMax = _CfprApEtherErrStatsFcsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 17),
    _CfprApEtherErrStatsFcsDeltaMax_Type()
)
cfprApEtherErrStatsFcsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsFcsDeltaMax.setStatus("current")
_CfprApEtherErrStatsFcsDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsFcsDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsFcsDeltaMin = _CfprApEtherErrStatsFcsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 18),
    _CfprApEtherErrStatsFcsDeltaMin_Type()
)
cfprApEtherErrStatsFcsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsFcsDeltaMin.setStatus("current")
_CfprApEtherErrStatsIntMacRx_Type = Unsigned64
_CfprApEtherErrStatsIntMacRx_Object = MibTableColumn
cfprApEtherErrStatsIntMacRx = _CfprApEtherErrStatsIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 19),
    _CfprApEtherErrStatsIntMacRx_Type()
)
cfprApEtherErrStatsIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacRx.setStatus("current")
_CfprApEtherErrStatsIntMacRxDelta_Type = Counter64
_CfprApEtherErrStatsIntMacRxDelta_Object = MibTableColumn
cfprApEtherErrStatsIntMacRxDelta = _CfprApEtherErrStatsIntMacRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 20),
    _CfprApEtherErrStatsIntMacRxDelta_Type()
)
cfprApEtherErrStatsIntMacRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacRxDelta.setStatus("current")
_CfprApEtherErrStatsIntMacRxDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsIntMacRxDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsIntMacRxDeltaAvg = _CfprApEtherErrStatsIntMacRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 21),
    _CfprApEtherErrStatsIntMacRxDeltaAvg_Type()
)
cfprApEtherErrStatsIntMacRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacRxDeltaAvg.setStatus("current")
_CfprApEtherErrStatsIntMacRxDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsIntMacRxDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsIntMacRxDeltaMax = _CfprApEtherErrStatsIntMacRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 22),
    _CfprApEtherErrStatsIntMacRxDeltaMax_Type()
)
cfprApEtherErrStatsIntMacRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacRxDeltaMax.setStatus("current")
_CfprApEtherErrStatsIntMacRxDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsIntMacRxDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsIntMacRxDeltaMin = _CfprApEtherErrStatsIntMacRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 23),
    _CfprApEtherErrStatsIntMacRxDeltaMin_Type()
)
cfprApEtherErrStatsIntMacRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacRxDeltaMin.setStatus("current")
_CfprApEtherErrStatsIntMacTx_Type = Unsigned64
_CfprApEtherErrStatsIntMacTx_Object = MibTableColumn
cfprApEtherErrStatsIntMacTx = _CfprApEtherErrStatsIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 24),
    _CfprApEtherErrStatsIntMacTx_Type()
)
cfprApEtherErrStatsIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacTx.setStatus("current")
_CfprApEtherErrStatsIntMacTxDelta_Type = Counter64
_CfprApEtherErrStatsIntMacTxDelta_Object = MibTableColumn
cfprApEtherErrStatsIntMacTxDelta = _CfprApEtherErrStatsIntMacTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 25),
    _CfprApEtherErrStatsIntMacTxDelta_Type()
)
cfprApEtherErrStatsIntMacTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacTxDelta.setStatus("current")
_CfprApEtherErrStatsIntMacTxDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsIntMacTxDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsIntMacTxDeltaAvg = _CfprApEtherErrStatsIntMacTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 26),
    _CfprApEtherErrStatsIntMacTxDeltaAvg_Type()
)
cfprApEtherErrStatsIntMacTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacTxDeltaAvg.setStatus("current")
_CfprApEtherErrStatsIntMacTxDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsIntMacTxDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsIntMacTxDeltaMax = _CfprApEtherErrStatsIntMacTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 27),
    _CfprApEtherErrStatsIntMacTxDeltaMax_Type()
)
cfprApEtherErrStatsIntMacTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacTxDeltaMax.setStatus("current")
_CfprApEtherErrStatsIntMacTxDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsIntMacTxDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsIntMacTxDeltaMin = _CfprApEtherErrStatsIntMacTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 28),
    _CfprApEtherErrStatsIntMacTxDeltaMin_Type()
)
cfprApEtherErrStatsIntMacTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntMacTxDeltaMin.setStatus("current")
_CfprApEtherErrStatsIntervals_Type = Gauge32
_CfprApEtherErrStatsIntervals_Object = MibTableColumn
cfprApEtherErrStatsIntervals = _CfprApEtherErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 29),
    _CfprApEtherErrStatsIntervals_Type()
)
cfprApEtherErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsIntervals.setStatus("current")
_CfprApEtherErrStatsOutDiscard_Type = Unsigned64
_CfprApEtherErrStatsOutDiscard_Object = MibTableColumn
cfprApEtherErrStatsOutDiscard = _CfprApEtherErrStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 30),
    _CfprApEtherErrStatsOutDiscard_Type()
)
cfprApEtherErrStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsOutDiscard.setStatus("current")
_CfprApEtherErrStatsOutDiscardDelta_Type = Counter64
_CfprApEtherErrStatsOutDiscardDelta_Object = MibTableColumn
cfprApEtherErrStatsOutDiscardDelta = _CfprApEtherErrStatsOutDiscardDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 31),
    _CfprApEtherErrStatsOutDiscardDelta_Type()
)
cfprApEtherErrStatsOutDiscardDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsOutDiscardDelta.setStatus("current")
_CfprApEtherErrStatsOutDiscardDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsOutDiscardDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsOutDiscardDeltaAvg = _CfprApEtherErrStatsOutDiscardDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 32),
    _CfprApEtherErrStatsOutDiscardDeltaAvg_Type()
)
cfprApEtherErrStatsOutDiscardDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsOutDiscardDeltaAvg.setStatus("current")
_CfprApEtherErrStatsOutDiscardDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsOutDiscardDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsOutDiscardDeltaMax = _CfprApEtherErrStatsOutDiscardDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 33),
    _CfprApEtherErrStatsOutDiscardDeltaMax_Type()
)
cfprApEtherErrStatsOutDiscardDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsOutDiscardDeltaMax.setStatus("current")
_CfprApEtherErrStatsOutDiscardDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsOutDiscardDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsOutDiscardDeltaMin = _CfprApEtherErrStatsOutDiscardDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 34),
    _CfprApEtherErrStatsOutDiscardDeltaMin_Type()
)
cfprApEtherErrStatsOutDiscardDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsOutDiscardDeltaMin.setStatus("current")
_CfprApEtherErrStatsRcv_Type = Unsigned64
_CfprApEtherErrStatsRcv_Object = MibTableColumn
cfprApEtherErrStatsRcv = _CfprApEtherErrStatsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 35),
    _CfprApEtherErrStatsRcv_Type()
)
cfprApEtherErrStatsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsRcv.setStatus("current")
_CfprApEtherErrStatsRcvDelta_Type = Counter64
_CfprApEtherErrStatsRcvDelta_Object = MibTableColumn
cfprApEtherErrStatsRcvDelta = _CfprApEtherErrStatsRcvDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 36),
    _CfprApEtherErrStatsRcvDelta_Type()
)
cfprApEtherErrStatsRcvDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsRcvDelta.setStatus("current")
_CfprApEtherErrStatsRcvDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsRcvDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsRcvDeltaAvg = _CfprApEtherErrStatsRcvDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 37),
    _CfprApEtherErrStatsRcvDeltaAvg_Type()
)
cfprApEtherErrStatsRcvDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsRcvDeltaAvg.setStatus("current")
_CfprApEtherErrStatsRcvDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsRcvDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsRcvDeltaMax = _CfprApEtherErrStatsRcvDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 38),
    _CfprApEtherErrStatsRcvDeltaMax_Type()
)
cfprApEtherErrStatsRcvDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsRcvDeltaMax.setStatus("current")
_CfprApEtherErrStatsRcvDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsRcvDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsRcvDeltaMin = _CfprApEtherErrStatsRcvDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 39),
    _CfprApEtherErrStatsRcvDeltaMin_Type()
)
cfprApEtherErrStatsRcvDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsRcvDeltaMin.setStatus("current")
_CfprApEtherErrStatsSuspect_Type = TruthValue
_CfprApEtherErrStatsSuspect_Object = MibTableColumn
cfprApEtherErrStatsSuspect = _CfprApEtherErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 40),
    _CfprApEtherErrStatsSuspect_Type()
)
cfprApEtherErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsSuspect.setStatus("current")
_CfprApEtherErrStatsThresholded_Type = CfprApEtherErrStatsThresholded
_CfprApEtherErrStatsThresholded_Object = MibTableColumn
cfprApEtherErrStatsThresholded = _CfprApEtherErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 41),
    _CfprApEtherErrStatsThresholded_Type()
)
cfprApEtherErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsThresholded.setStatus("current")
_CfprApEtherErrStatsTimeCollected_Type = DateAndTime
_CfprApEtherErrStatsTimeCollected_Object = MibTableColumn
cfprApEtherErrStatsTimeCollected = _CfprApEtherErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 42),
    _CfprApEtherErrStatsTimeCollected_Type()
)
cfprApEtherErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsTimeCollected.setStatus("current")
_CfprApEtherErrStatsUnderSize_Type = Unsigned64
_CfprApEtherErrStatsUnderSize_Object = MibTableColumn
cfprApEtherErrStatsUnderSize = _CfprApEtherErrStatsUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 43),
    _CfprApEtherErrStatsUnderSize_Type()
)
cfprApEtherErrStatsUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsUnderSize.setStatus("current")
_CfprApEtherErrStatsUnderSizeDelta_Type = Counter64
_CfprApEtherErrStatsUnderSizeDelta_Object = MibTableColumn
cfprApEtherErrStatsUnderSizeDelta = _CfprApEtherErrStatsUnderSizeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 44),
    _CfprApEtherErrStatsUnderSizeDelta_Type()
)
cfprApEtherErrStatsUnderSizeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsUnderSizeDelta.setStatus("current")
_CfprApEtherErrStatsUnderSizeDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsUnderSizeDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsUnderSizeDeltaAvg = _CfprApEtherErrStatsUnderSizeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 45),
    _CfprApEtherErrStatsUnderSizeDeltaAvg_Type()
)
cfprApEtherErrStatsUnderSizeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsUnderSizeDeltaAvg.setStatus("current")
_CfprApEtherErrStatsUnderSizeDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsUnderSizeDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsUnderSizeDeltaMax = _CfprApEtherErrStatsUnderSizeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 46),
    _CfprApEtherErrStatsUnderSizeDeltaMax_Type()
)
cfprApEtherErrStatsUnderSizeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsUnderSizeDeltaMax.setStatus("current")
_CfprApEtherErrStatsUnderSizeDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsUnderSizeDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsUnderSizeDeltaMin = _CfprApEtherErrStatsUnderSizeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 47),
    _CfprApEtherErrStatsUnderSizeDeltaMin_Type()
)
cfprApEtherErrStatsUnderSizeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsUnderSizeDeltaMin.setStatus("current")
_CfprApEtherErrStatsUpdate_Type = Gauge32
_CfprApEtherErrStatsUpdate_Object = MibTableColumn
cfprApEtherErrStatsUpdate = _CfprApEtherErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 48),
    _CfprApEtherErrStatsUpdate_Type()
)
cfprApEtherErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsUpdate.setStatus("current")
_CfprApEtherErrStatsXmit_Type = Unsigned64
_CfprApEtherErrStatsXmit_Object = MibTableColumn
cfprApEtherErrStatsXmit = _CfprApEtherErrStatsXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 49),
    _CfprApEtherErrStatsXmit_Type()
)
cfprApEtherErrStatsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsXmit.setStatus("current")
_CfprApEtherErrStatsXmitDelta_Type = Counter64
_CfprApEtherErrStatsXmitDelta_Object = MibTableColumn
cfprApEtherErrStatsXmitDelta = _CfprApEtherErrStatsXmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 50),
    _CfprApEtherErrStatsXmitDelta_Type()
)
cfprApEtherErrStatsXmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsXmitDelta.setStatus("current")
_CfprApEtherErrStatsXmitDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsXmitDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsXmitDeltaAvg = _CfprApEtherErrStatsXmitDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 51),
    _CfprApEtherErrStatsXmitDeltaAvg_Type()
)
cfprApEtherErrStatsXmitDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsXmitDeltaAvg.setStatus("current")
_CfprApEtherErrStatsXmitDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsXmitDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsXmitDeltaMax = _CfprApEtherErrStatsXmitDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 52),
    _CfprApEtherErrStatsXmitDeltaMax_Type()
)
cfprApEtherErrStatsXmitDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsXmitDeltaMax.setStatus("current")
_CfprApEtherErrStatsXmitDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsXmitDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsXmitDeltaMin = _CfprApEtherErrStatsXmitDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 1, 1, 53),
    _CfprApEtherErrStatsXmitDeltaMin_Type()
)
cfprApEtherErrStatsXmitDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsXmitDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistTable_Object = MibTable
cfprApEtherErrStatsHistTable = _CfprApEtherErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistTable.setStatus("current")
_CfprApEtherErrStatsHistEntry_Object = MibTableRow
cfprApEtherErrStatsHistEntry = _CfprApEtherErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1)
)
cfprApEtherErrStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistEntry.setStatus("current")
_CfprApEtherErrStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherErrStatsHistInstanceId_Object = MibTableColumn
cfprApEtherErrStatsHistInstanceId = _CfprApEtherErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 1),
    _CfprApEtherErrStatsHistInstanceId_Type()
)
cfprApEtherErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistInstanceId.setStatus("current")
_CfprApEtherErrStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherErrStatsHistDn_Object = MibTableColumn
cfprApEtherErrStatsHistDn = _CfprApEtherErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 2),
    _CfprApEtherErrStatsHistDn_Type()
)
cfprApEtherErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistDn.setStatus("current")
_CfprApEtherErrStatsHistRn_Type = SnmpAdminString
_CfprApEtherErrStatsHistRn_Object = MibTableColumn
cfprApEtherErrStatsHistRn = _CfprApEtherErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 3),
    _CfprApEtherErrStatsHistRn_Type()
)
cfprApEtherErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistRn.setStatus("current")
_CfprApEtherErrStatsHistAlign_Type = Unsigned64
_CfprApEtherErrStatsHistAlign_Object = MibTableColumn
cfprApEtherErrStatsHistAlign = _CfprApEtherErrStatsHistAlign_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 4),
    _CfprApEtherErrStatsHistAlign_Type()
)
cfprApEtherErrStatsHistAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistAlign.setStatus("current")
_CfprApEtherErrStatsHistAlignDelta_Type = Unsigned64
_CfprApEtherErrStatsHistAlignDelta_Object = MibTableColumn
cfprApEtherErrStatsHistAlignDelta = _CfprApEtherErrStatsHistAlignDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 5),
    _CfprApEtherErrStatsHistAlignDelta_Type()
)
cfprApEtherErrStatsHistAlignDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistAlignDelta.setStatus("current")
_CfprApEtherErrStatsHistAlignDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistAlignDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistAlignDeltaAvg = _CfprApEtherErrStatsHistAlignDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 6),
    _CfprApEtherErrStatsHistAlignDeltaAvg_Type()
)
cfprApEtherErrStatsHistAlignDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistAlignDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistAlignDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistAlignDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistAlignDeltaMax = _CfprApEtherErrStatsHistAlignDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 7),
    _CfprApEtherErrStatsHistAlignDeltaMax_Type()
)
cfprApEtherErrStatsHistAlignDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistAlignDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistAlignDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistAlignDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistAlignDeltaMin = _CfprApEtherErrStatsHistAlignDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 8),
    _CfprApEtherErrStatsHistAlignDeltaMin_Type()
)
cfprApEtherErrStatsHistAlignDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistAlignDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistDeferredTx_Type = Unsigned64
_CfprApEtherErrStatsHistDeferredTx_Object = MibTableColumn
cfprApEtherErrStatsHistDeferredTx = _CfprApEtherErrStatsHistDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 9),
    _CfprApEtherErrStatsHistDeferredTx_Type()
)
cfprApEtherErrStatsHistDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistDeferredTx.setStatus("current")
_CfprApEtherErrStatsHistDeferredTxDelta_Type = Unsigned64
_CfprApEtherErrStatsHistDeferredTxDelta_Object = MibTableColumn
cfprApEtherErrStatsHistDeferredTxDelta = _CfprApEtherErrStatsHistDeferredTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 10),
    _CfprApEtherErrStatsHistDeferredTxDelta_Type()
)
cfprApEtherErrStatsHistDeferredTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistDeferredTxDelta.setStatus("current")
_CfprApEtherErrStatsHistDeferredTxDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistDeferredTxDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistDeferredTxDeltaAvg = _CfprApEtherErrStatsHistDeferredTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 11),
    _CfprApEtherErrStatsHistDeferredTxDeltaAvg_Type()
)
cfprApEtherErrStatsHistDeferredTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistDeferredTxDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistDeferredTxDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistDeferredTxDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistDeferredTxDeltaMax = _CfprApEtherErrStatsHistDeferredTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 12),
    _CfprApEtherErrStatsHistDeferredTxDeltaMax_Type()
)
cfprApEtherErrStatsHistDeferredTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistDeferredTxDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistDeferredTxDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistDeferredTxDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistDeferredTxDeltaMin = _CfprApEtherErrStatsHistDeferredTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 13),
    _CfprApEtherErrStatsHistDeferredTxDeltaMin_Type()
)
cfprApEtherErrStatsHistDeferredTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistDeferredTxDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistFcs_Type = Unsigned64
_CfprApEtherErrStatsHistFcs_Object = MibTableColumn
cfprApEtherErrStatsHistFcs = _CfprApEtherErrStatsHistFcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 14),
    _CfprApEtherErrStatsHistFcs_Type()
)
cfprApEtherErrStatsHistFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistFcs.setStatus("current")
_CfprApEtherErrStatsHistFcsDelta_Type = Unsigned64
_CfprApEtherErrStatsHistFcsDelta_Object = MibTableColumn
cfprApEtherErrStatsHistFcsDelta = _CfprApEtherErrStatsHistFcsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 15),
    _CfprApEtherErrStatsHistFcsDelta_Type()
)
cfprApEtherErrStatsHistFcsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistFcsDelta.setStatus("current")
_CfprApEtherErrStatsHistFcsDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistFcsDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistFcsDeltaAvg = _CfprApEtherErrStatsHistFcsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 16),
    _CfprApEtherErrStatsHistFcsDeltaAvg_Type()
)
cfprApEtherErrStatsHistFcsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistFcsDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistFcsDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistFcsDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistFcsDeltaMax = _CfprApEtherErrStatsHistFcsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 17),
    _CfprApEtherErrStatsHistFcsDeltaMax_Type()
)
cfprApEtherErrStatsHistFcsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistFcsDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistFcsDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistFcsDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistFcsDeltaMin = _CfprApEtherErrStatsHistFcsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 18),
    _CfprApEtherErrStatsHistFcsDeltaMin_Type()
)
cfprApEtherErrStatsHistFcsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistFcsDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistId_Type = Unsigned64
_CfprApEtherErrStatsHistId_Object = MibTableColumn
cfprApEtherErrStatsHistId = _CfprApEtherErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 19),
    _CfprApEtherErrStatsHistId_Type()
)
cfprApEtherErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistId.setStatus("current")
_CfprApEtherErrStatsHistIntMacRx_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacRx_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacRx = _CfprApEtherErrStatsHistIntMacRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 20),
    _CfprApEtherErrStatsHistIntMacRx_Type()
)
cfprApEtherErrStatsHistIntMacRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacRx.setStatus("current")
_CfprApEtherErrStatsHistIntMacRxDelta_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacRxDelta_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacRxDelta = _CfprApEtherErrStatsHistIntMacRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 21),
    _CfprApEtherErrStatsHistIntMacRxDelta_Type()
)
cfprApEtherErrStatsHistIntMacRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacRxDelta.setStatus("current")
_CfprApEtherErrStatsHistIntMacRxDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacRxDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacRxDeltaAvg = _CfprApEtherErrStatsHistIntMacRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 22),
    _CfprApEtherErrStatsHistIntMacRxDeltaAvg_Type()
)
cfprApEtherErrStatsHistIntMacRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacRxDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistIntMacRxDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacRxDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacRxDeltaMax = _CfprApEtherErrStatsHistIntMacRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 23),
    _CfprApEtherErrStatsHistIntMacRxDeltaMax_Type()
)
cfprApEtherErrStatsHistIntMacRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacRxDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistIntMacRxDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacRxDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacRxDeltaMin = _CfprApEtherErrStatsHistIntMacRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 24),
    _CfprApEtherErrStatsHistIntMacRxDeltaMin_Type()
)
cfprApEtherErrStatsHistIntMacRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacRxDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistIntMacTx_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacTx_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacTx = _CfprApEtherErrStatsHistIntMacTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 25),
    _CfprApEtherErrStatsHistIntMacTx_Type()
)
cfprApEtherErrStatsHistIntMacTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacTx.setStatus("current")
_CfprApEtherErrStatsHistIntMacTxDelta_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacTxDelta_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacTxDelta = _CfprApEtherErrStatsHistIntMacTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 26),
    _CfprApEtherErrStatsHistIntMacTxDelta_Type()
)
cfprApEtherErrStatsHistIntMacTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacTxDelta.setStatus("current")
_CfprApEtherErrStatsHistIntMacTxDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacTxDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacTxDeltaAvg = _CfprApEtherErrStatsHistIntMacTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 27),
    _CfprApEtherErrStatsHistIntMacTxDeltaAvg_Type()
)
cfprApEtherErrStatsHistIntMacTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacTxDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistIntMacTxDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacTxDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacTxDeltaMax = _CfprApEtherErrStatsHistIntMacTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 28),
    _CfprApEtherErrStatsHistIntMacTxDeltaMax_Type()
)
cfprApEtherErrStatsHistIntMacTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacTxDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistIntMacTxDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistIntMacTxDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistIntMacTxDeltaMin = _CfprApEtherErrStatsHistIntMacTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 29),
    _CfprApEtherErrStatsHistIntMacTxDeltaMin_Type()
)
cfprApEtherErrStatsHistIntMacTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistIntMacTxDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistMostRecent_Type = TruthValue
_CfprApEtherErrStatsHistMostRecent_Object = MibTableColumn
cfprApEtherErrStatsHistMostRecent = _CfprApEtherErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 30),
    _CfprApEtherErrStatsHistMostRecent_Type()
)
cfprApEtherErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistMostRecent.setStatus("current")
_CfprApEtherErrStatsHistOutDiscard_Type = Unsigned64
_CfprApEtherErrStatsHistOutDiscard_Object = MibTableColumn
cfprApEtherErrStatsHistOutDiscard = _CfprApEtherErrStatsHistOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 31),
    _CfprApEtherErrStatsHistOutDiscard_Type()
)
cfprApEtherErrStatsHistOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistOutDiscard.setStatus("current")
_CfprApEtherErrStatsHistOutDiscardDelta_Type = Unsigned64
_CfprApEtherErrStatsHistOutDiscardDelta_Object = MibTableColumn
cfprApEtherErrStatsHistOutDiscardDelta = _CfprApEtherErrStatsHistOutDiscardDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 32),
    _CfprApEtherErrStatsHistOutDiscardDelta_Type()
)
cfprApEtherErrStatsHistOutDiscardDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistOutDiscardDelta.setStatus("current")
_CfprApEtherErrStatsHistOutDiscardDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistOutDiscardDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistOutDiscardDeltaAvg = _CfprApEtherErrStatsHistOutDiscardDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 33),
    _CfprApEtherErrStatsHistOutDiscardDeltaAvg_Type()
)
cfprApEtherErrStatsHistOutDiscardDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistOutDiscardDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistOutDiscardDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistOutDiscardDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistOutDiscardDeltaMax = _CfprApEtherErrStatsHistOutDiscardDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 34),
    _CfprApEtherErrStatsHistOutDiscardDeltaMax_Type()
)
cfprApEtherErrStatsHistOutDiscardDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistOutDiscardDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistOutDiscardDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistOutDiscardDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistOutDiscardDeltaMin = _CfprApEtherErrStatsHistOutDiscardDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 35),
    _CfprApEtherErrStatsHistOutDiscardDeltaMin_Type()
)
cfprApEtherErrStatsHistOutDiscardDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistOutDiscardDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistRcv_Type = Unsigned64
_CfprApEtherErrStatsHistRcv_Object = MibTableColumn
cfprApEtherErrStatsHistRcv = _CfprApEtherErrStatsHistRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 36),
    _CfprApEtherErrStatsHistRcv_Type()
)
cfprApEtherErrStatsHistRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistRcv.setStatus("current")
_CfprApEtherErrStatsHistRcvDelta_Type = Unsigned64
_CfprApEtherErrStatsHistRcvDelta_Object = MibTableColumn
cfprApEtherErrStatsHistRcvDelta = _CfprApEtherErrStatsHistRcvDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 37),
    _CfprApEtherErrStatsHistRcvDelta_Type()
)
cfprApEtherErrStatsHistRcvDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistRcvDelta.setStatus("current")
_CfprApEtherErrStatsHistRcvDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistRcvDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistRcvDeltaAvg = _CfprApEtherErrStatsHistRcvDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 38),
    _CfprApEtherErrStatsHistRcvDeltaAvg_Type()
)
cfprApEtherErrStatsHistRcvDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistRcvDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistRcvDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistRcvDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistRcvDeltaMax = _CfprApEtherErrStatsHistRcvDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 39),
    _CfprApEtherErrStatsHistRcvDeltaMax_Type()
)
cfprApEtherErrStatsHistRcvDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistRcvDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistRcvDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistRcvDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistRcvDeltaMin = _CfprApEtherErrStatsHistRcvDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 40),
    _CfprApEtherErrStatsHistRcvDeltaMin_Type()
)
cfprApEtherErrStatsHistRcvDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistRcvDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistSuspect_Type = TruthValue
_CfprApEtherErrStatsHistSuspect_Object = MibTableColumn
cfprApEtherErrStatsHistSuspect = _CfprApEtherErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 41),
    _CfprApEtherErrStatsHistSuspect_Type()
)
cfprApEtherErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistSuspect.setStatus("current")
_CfprApEtherErrStatsHistThresholded_Type = CfprApEtherErrStatsHistThresholded
_CfprApEtherErrStatsHistThresholded_Object = MibTableColumn
cfprApEtherErrStatsHistThresholded = _CfprApEtherErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 42),
    _CfprApEtherErrStatsHistThresholded_Type()
)
cfprApEtherErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistThresholded.setStatus("current")
_CfprApEtherErrStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherErrStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherErrStatsHistTimeCollected = _CfprApEtherErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 43),
    _CfprApEtherErrStatsHistTimeCollected_Type()
)
cfprApEtherErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistTimeCollected.setStatus("current")
_CfprApEtherErrStatsHistUnderSize_Type = Unsigned64
_CfprApEtherErrStatsHistUnderSize_Object = MibTableColumn
cfprApEtherErrStatsHistUnderSize = _CfprApEtherErrStatsHistUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 44),
    _CfprApEtherErrStatsHistUnderSize_Type()
)
cfprApEtherErrStatsHistUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistUnderSize.setStatus("current")
_CfprApEtherErrStatsHistUnderSizeDelta_Type = Unsigned64
_CfprApEtherErrStatsHistUnderSizeDelta_Object = MibTableColumn
cfprApEtherErrStatsHistUnderSizeDelta = _CfprApEtherErrStatsHistUnderSizeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 45),
    _CfprApEtherErrStatsHistUnderSizeDelta_Type()
)
cfprApEtherErrStatsHistUnderSizeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistUnderSizeDelta.setStatus("current")
_CfprApEtherErrStatsHistUnderSizeDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistUnderSizeDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistUnderSizeDeltaAvg = _CfprApEtherErrStatsHistUnderSizeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 46),
    _CfprApEtherErrStatsHistUnderSizeDeltaAvg_Type()
)
cfprApEtherErrStatsHistUnderSizeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistUnderSizeDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistUnderSizeDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistUnderSizeDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistUnderSizeDeltaMax = _CfprApEtherErrStatsHistUnderSizeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 47),
    _CfprApEtherErrStatsHistUnderSizeDeltaMax_Type()
)
cfprApEtherErrStatsHistUnderSizeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistUnderSizeDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistUnderSizeDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistUnderSizeDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistUnderSizeDeltaMin = _CfprApEtherErrStatsHistUnderSizeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 48),
    _CfprApEtherErrStatsHistUnderSizeDeltaMin_Type()
)
cfprApEtherErrStatsHistUnderSizeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistUnderSizeDeltaMin.setStatus("current")
_CfprApEtherErrStatsHistXmit_Type = Unsigned64
_CfprApEtherErrStatsHistXmit_Object = MibTableColumn
cfprApEtherErrStatsHistXmit = _CfprApEtherErrStatsHistXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 49),
    _CfprApEtherErrStatsHistXmit_Type()
)
cfprApEtherErrStatsHistXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistXmit.setStatus("current")
_CfprApEtherErrStatsHistXmitDelta_Type = Unsigned64
_CfprApEtherErrStatsHistXmitDelta_Object = MibTableColumn
cfprApEtherErrStatsHistXmitDelta = _CfprApEtherErrStatsHistXmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 50),
    _CfprApEtherErrStatsHistXmitDelta_Type()
)
cfprApEtherErrStatsHistXmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistXmitDelta.setStatus("current")
_CfprApEtherErrStatsHistXmitDeltaAvg_Type = Unsigned64
_CfprApEtherErrStatsHistXmitDeltaAvg_Object = MibTableColumn
cfprApEtherErrStatsHistXmitDeltaAvg = _CfprApEtherErrStatsHistXmitDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 51),
    _CfprApEtherErrStatsHistXmitDeltaAvg_Type()
)
cfprApEtherErrStatsHistXmitDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistXmitDeltaAvg.setStatus("current")
_CfprApEtherErrStatsHistXmitDeltaMax_Type = Unsigned64
_CfprApEtherErrStatsHistXmitDeltaMax_Object = MibTableColumn
cfprApEtherErrStatsHistXmitDeltaMax = _CfprApEtherErrStatsHistXmitDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 52),
    _CfprApEtherErrStatsHistXmitDeltaMax_Type()
)
cfprApEtherErrStatsHistXmitDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistXmitDeltaMax.setStatus("current")
_CfprApEtherErrStatsHistXmitDeltaMin_Type = Unsigned64
_CfprApEtherErrStatsHistXmitDeltaMin_Object = MibTableColumn
cfprApEtherErrStatsHistXmitDeltaMin = _CfprApEtherErrStatsHistXmitDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 2, 1, 53),
    _CfprApEtherErrStatsHistXmitDeltaMin_Type()
)
cfprApEtherErrStatsHistXmitDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherErrStatsHistXmitDeltaMin.setStatus("current")
_CfprApEtherFailToWireTable_Object = MibTable
cfprApEtherFailToWireTable = _CfprApEtherFailToWireTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3)
)
if mibBuilder.loadTexts:
    cfprApEtherFailToWireTable.setStatus("current")
_CfprApEtherFailToWireEntry_Object = MibTableRow
cfprApEtherFailToWireEntry = _CfprApEtherFailToWireEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1)
)
cfprApEtherFailToWireEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFailToWireInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFailToWireEntry.setStatus("current")
_CfprApEtherFailToWireInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFailToWireInstanceId_Object = MibTableColumn
cfprApEtherFailToWireInstanceId = _CfprApEtherFailToWireInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 1),
    _CfprApEtherFailToWireInstanceId_Type()
)
cfprApEtherFailToWireInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireInstanceId.setStatus("current")
_CfprApEtherFailToWireDn_Type = CfprApManagedObjectDn
_CfprApEtherFailToWireDn_Object = MibTableColumn
cfprApEtherFailToWireDn = _CfprApEtherFailToWireDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 2),
    _CfprApEtherFailToWireDn_Type()
)
cfprApEtherFailToWireDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireDn.setStatus("current")
_CfprApEtherFailToWireRn_Type = SnmpAdminString
_CfprApEtherFailToWireRn_Object = MibTableColumn
cfprApEtherFailToWireRn = _CfprApEtherFailToWireRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 3),
    _CfprApEtherFailToWireRn_Type()
)
cfprApEtherFailToWireRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireRn.setStatus("current")
_CfprApEtherFailToWireLocale_Type = CfprApNetworkLocale
_CfprApEtherFailToWireLocale_Object = MibTableColumn
cfprApEtherFailToWireLocale = _CfprApEtherFailToWireLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 4),
    _CfprApEtherFailToWireLocale_Type()
)
cfprApEtherFailToWireLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireLocale.setStatus("current")
_CfprApEtherFailToWireName_Type = SnmpAdminString
_CfprApEtherFailToWireName_Object = MibTableColumn
cfprApEtherFailToWireName = _CfprApEtherFailToWireName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 5),
    _CfprApEtherFailToWireName_Type()
)
cfprApEtherFailToWireName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireName.setStatus("current")
_CfprApEtherFailToWireTransport_Type = CfprApNetworkTransport
_CfprApEtherFailToWireTransport_Object = MibTableColumn
cfprApEtherFailToWireTransport = _CfprApEtherFailToWireTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 6),
    _CfprApEtherFailToWireTransport_Type()
)
cfprApEtherFailToWireTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireTransport.setStatus("current")
_CfprApEtherFailToWireType_Type = CfprApNetworkConnectionType
_CfprApEtherFailToWireType_Object = MibTableColumn
cfprApEtherFailToWireType = _CfprApEtherFailToWireType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 3, 1, 7),
    _CfprApEtherFailToWireType_Type()
)
cfprApEtherFailToWireType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFailToWireType.setStatus("current")
_CfprApEtherFcoeInterfaceStatsTable_Object = MibTable
cfprApEtherFcoeInterfaceStatsTable = _CfprApEtherFcoeInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4)
)
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsTable.setStatus("current")
_CfprApEtherFcoeInterfaceStatsEntry_Object = MibTableRow
cfprApEtherFcoeInterfaceStatsEntry = _CfprApEtherFcoeInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1)
)
cfprApEtherFcoeInterfaceStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFcoeInterfaceStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsEntry.setStatus("current")
_CfprApEtherFcoeInterfaceStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFcoeInterfaceStatsInstanceId_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsInstanceId = _CfprApEtherFcoeInterfaceStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 1),
    _CfprApEtherFcoeInterfaceStatsInstanceId_Type()
)
cfprApEtherFcoeInterfaceStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsInstanceId.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherFcoeInterfaceStatsDn_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDn = _CfprApEtherFcoeInterfaceStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 2),
    _CfprApEtherFcoeInterfaceStatsDn_Type()
)
cfprApEtherFcoeInterfaceStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDn.setStatus("current")
_CfprApEtherFcoeInterfaceStatsRn_Type = SnmpAdminString
_CfprApEtherFcoeInterfaceStatsRn_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsRn = _CfprApEtherFcoeInterfaceStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 3),
    _CfprApEtherFcoeInterfaceStatsRn_Type()
)
cfprApEtherFcoeInterfaceStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsRn.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesRx = _CfprApEtherFcoeInterfaceStatsBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 4),
    _CfprApEtherFcoeInterfaceStatsBytesRx_Type()
)
cfprApEtherFcoeInterfaceStatsBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesRxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsBytesRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesRxDelta = _CfprApEtherFcoeInterfaceStatsBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 5),
    _CfprApEtherFcoeInterfaceStatsBytesRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 6),
    _CfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesRxDeltaMax = _CfprApEtherFcoeInterfaceStatsBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 7),
    _CfprApEtherFcoeInterfaceStatsBytesRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesRxDeltaMin = _CfprApEtherFcoeInterfaceStatsBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 8),
    _CfprApEtherFcoeInterfaceStatsBytesRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesTx = _CfprApEtherFcoeInterfaceStatsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 9),
    _CfprApEtherFcoeInterfaceStatsBytesTx_Type()
)
cfprApEtherFcoeInterfaceStatsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesTxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsBytesTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesTxDelta = _CfprApEtherFcoeInterfaceStatsBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 10),
    _CfprApEtherFcoeInterfaceStatsBytesTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 11),
    _CfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesTxDeltaMax = _CfprApEtherFcoeInterfaceStatsBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 12),
    _CfprApEtherFcoeInterfaceStatsBytesTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsBytesTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsBytesTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsBytesTxDeltaMin = _CfprApEtherFcoeInterfaceStatsBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 13),
    _CfprApEtherFcoeInterfaceStatsBytesTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsBytesTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedRx = _CfprApEtherFcoeInterfaceStatsDroppedRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 14),
    _CfprApEtherFcoeInterfaceStatsDroppedRx_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedRxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsDroppedRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedRxDelta = _CfprApEtherFcoeInterfaceStatsDroppedRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 15),
    _CfprApEtherFcoeInterfaceStatsDroppedRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 16),
    _CfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax = _CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 17),
    _CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin = _CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 18),
    _CfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedTx = _CfprApEtherFcoeInterfaceStatsDroppedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 19),
    _CfprApEtherFcoeInterfaceStatsDroppedTx_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedTxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsDroppedTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedTxDelta = _CfprApEtherFcoeInterfaceStatsDroppedTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 20),
    _CfprApEtherFcoeInterfaceStatsDroppedTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 21),
    _CfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax = _CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 22),
    _CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin = _CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 23),
    _CfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsRx = _CfprApEtherFcoeInterfaceStatsErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 24),
    _CfprApEtherFcoeInterfaceStatsErrorsRx_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsRxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsErrorsRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsRxDelta = _CfprApEtherFcoeInterfaceStatsErrorsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 25),
    _CfprApEtherFcoeInterfaceStatsErrorsRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 26),
    _CfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax = _CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 27),
    _CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin = _CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 28),
    _CfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsTx = _CfprApEtherFcoeInterfaceStatsErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 29),
    _CfprApEtherFcoeInterfaceStatsErrorsTx_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsTxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsErrorsTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsTxDelta = _CfprApEtherFcoeInterfaceStatsErrorsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 30),
    _CfprApEtherFcoeInterfaceStatsErrorsTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 31),
    _CfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax = _CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 32),
    _CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin = _CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 33),
    _CfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsIntervals_Type = Gauge32
_CfprApEtherFcoeInterfaceStatsIntervals_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsIntervals = _CfprApEtherFcoeInterfaceStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 34),
    _CfprApEtherFcoeInterfaceStatsIntervals_Type()
)
cfprApEtherFcoeInterfaceStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsIntervals.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsRx = _CfprApEtherFcoeInterfaceStatsPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 35),
    _CfprApEtherFcoeInterfaceStatsPacketsRx_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsRxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsPacketsRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsRxDelta = _CfprApEtherFcoeInterfaceStatsPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 36),
    _CfprApEtherFcoeInterfaceStatsPacketsRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 37),
    _CfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax = _CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 38),
    _CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin = _CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 39),
    _CfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsTx = _CfprApEtherFcoeInterfaceStatsPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 40),
    _CfprApEtherFcoeInterfaceStatsPacketsTx_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsTxDelta_Type = Counter64
_CfprApEtherFcoeInterfaceStatsPacketsTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsTxDelta = _CfprApEtherFcoeInterfaceStatsPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 41),
    _CfprApEtherFcoeInterfaceStatsPacketsTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 42),
    _CfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax = _CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 43),
    _CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin = _CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 44),
    _CfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsSuspect_Type = TruthValue
_CfprApEtherFcoeInterfaceStatsSuspect_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsSuspect = _CfprApEtherFcoeInterfaceStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 45),
    _CfprApEtherFcoeInterfaceStatsSuspect_Type()
)
cfprApEtherFcoeInterfaceStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsSuspect.setStatus("current")
_CfprApEtherFcoeInterfaceStatsThresholded_Type = CfprApEtherFcoeInterfaceStatsThresholded
_CfprApEtherFcoeInterfaceStatsThresholded_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsThresholded = _CfprApEtherFcoeInterfaceStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 46),
    _CfprApEtherFcoeInterfaceStatsThresholded_Type()
)
cfprApEtherFcoeInterfaceStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsThresholded.setStatus("current")
_CfprApEtherFcoeInterfaceStatsTimeCollected_Type = DateAndTime
_CfprApEtherFcoeInterfaceStatsTimeCollected_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsTimeCollected = _CfprApEtherFcoeInterfaceStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 47),
    _CfprApEtherFcoeInterfaceStatsTimeCollected_Type()
)
cfprApEtherFcoeInterfaceStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsTimeCollected.setStatus("current")
_CfprApEtherFcoeInterfaceStatsUpdate_Type = Gauge32
_CfprApEtherFcoeInterfaceStatsUpdate_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsUpdate = _CfprApEtherFcoeInterfaceStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 4, 1, 48),
    _CfprApEtherFcoeInterfaceStatsUpdate_Type()
)
cfprApEtherFcoeInterfaceStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsUpdate.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistTable_Object = MibTable
cfprApEtherFcoeInterfaceStatsHistTable = _CfprApEtherFcoeInterfaceStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5)
)
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistTable.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistEntry_Object = MibTableRow
cfprApEtherFcoeInterfaceStatsHistEntry = _CfprApEtherFcoeInterfaceStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1)
)
cfprApEtherFcoeInterfaceStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFcoeInterfaceStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistEntry.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFcoeInterfaceStatsHistInstanceId_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistInstanceId = _CfprApEtherFcoeInterfaceStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 1),
    _CfprApEtherFcoeInterfaceStatsHistInstanceId_Type()
)
cfprApEtherFcoeInterfaceStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistInstanceId.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherFcoeInterfaceStatsHistDn_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDn = _CfprApEtherFcoeInterfaceStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 2),
    _CfprApEtherFcoeInterfaceStatsHistDn_Type()
)
cfprApEtherFcoeInterfaceStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDn.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistRn_Type = SnmpAdminString
_CfprApEtherFcoeInterfaceStatsHistRn_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistRn = _CfprApEtherFcoeInterfaceStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 3),
    _CfprApEtherFcoeInterfaceStatsHistRn_Type()
)
cfprApEtherFcoeInterfaceStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistRn.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesRx = _CfprApEtherFcoeInterfaceStatsHistBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 4),
    _CfprApEtherFcoeInterfaceStatsHistBytesRx_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesRxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesRxDelta = _CfprApEtherFcoeInterfaceStatsHistBytesRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 5),
    _CfprApEtherFcoeInterfaceStatsHistBytesRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 6),
    _CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 7),
    _CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 8),
    _CfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesTx = _CfprApEtherFcoeInterfaceStatsHistBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 9),
    _CfprApEtherFcoeInterfaceStatsHistBytesTx_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesTxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesTxDelta = _CfprApEtherFcoeInterfaceStatsHistBytesTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 10),
    _CfprApEtherFcoeInterfaceStatsHistBytesTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 11),
    _CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 12),
    _CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 13),
    _CfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedRx = _CfprApEtherFcoeInterfaceStatsHistDroppedRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 14),
    _CfprApEtherFcoeInterfaceStatsHistDroppedRx_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedRxDelta = _CfprApEtherFcoeInterfaceStatsHistDroppedRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 15),
    _CfprApEtherFcoeInterfaceStatsHistDroppedRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 16),
    _CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 17),
    _CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 18),
    _CfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedTx = _CfprApEtherFcoeInterfaceStatsHistDroppedTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 19),
    _CfprApEtherFcoeInterfaceStatsHistDroppedTx_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedTxDelta = _CfprApEtherFcoeInterfaceStatsHistDroppedTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 20),
    _CfprApEtherFcoeInterfaceStatsHistDroppedTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 21),
    _CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 22),
    _CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 23),
    _CfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsRx = _CfprApEtherFcoeInterfaceStatsHistErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 24),
    _CfprApEtherFcoeInterfaceStatsHistErrorsRx_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsRxDelta = _CfprApEtherFcoeInterfaceStatsHistErrorsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 25),
    _CfprApEtherFcoeInterfaceStatsHistErrorsRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 26),
    _CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 27),
    _CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 28),
    _CfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsTx = _CfprApEtherFcoeInterfaceStatsHistErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 29),
    _CfprApEtherFcoeInterfaceStatsHistErrorsTx_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsTxDelta = _CfprApEtherFcoeInterfaceStatsHistErrorsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 30),
    _CfprApEtherFcoeInterfaceStatsHistErrorsTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 31),
    _CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 32),
    _CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 33),
    _CfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistId_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistId_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistId = _CfprApEtherFcoeInterfaceStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 34),
    _CfprApEtherFcoeInterfaceStatsHistId_Type()
)
cfprApEtherFcoeInterfaceStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistId.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistMostRecent_Type = TruthValue
_CfprApEtherFcoeInterfaceStatsHistMostRecent_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistMostRecent = _CfprApEtherFcoeInterfaceStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 35),
    _CfprApEtherFcoeInterfaceStatsHistMostRecent_Type()
)
cfprApEtherFcoeInterfaceStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistMostRecent.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsRx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsRx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsRx = _CfprApEtherFcoeInterfaceStatsHistPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 36),
    _CfprApEtherFcoeInterfaceStatsHistPacketsRx_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsRx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsRxDelta = _CfprApEtherFcoeInterfaceStatsHistPacketsRxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 37),
    _CfprApEtherFcoeInterfaceStatsHistPacketsRxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsRxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsRxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 38),
    _CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 39),
    _CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 40),
    _CfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsTx_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsTx_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsTx = _CfprApEtherFcoeInterfaceStatsHistPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 41),
    _CfprApEtherFcoeInterfaceStatsHistPacketsTx_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsTx.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDelta_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDelta_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsTxDelta = _CfprApEtherFcoeInterfaceStatsHistPacketsTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 42),
    _CfprApEtherFcoeInterfaceStatsHistPacketsTxDelta_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsTxDelta.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg = _CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 43),
    _CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax = _CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 44),
    _CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type = Unsigned64
_CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin = _CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 45),
    _CfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin_Type()
)
cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistSuspect_Type = TruthValue
_CfprApEtherFcoeInterfaceStatsHistSuspect_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistSuspect = _CfprApEtherFcoeInterfaceStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 46),
    _CfprApEtherFcoeInterfaceStatsHistSuspect_Type()
)
cfprApEtherFcoeInterfaceStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistSuspect.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistThresholded_Type = CfprApEtherFcoeInterfaceStatsHistThresholded
_CfprApEtherFcoeInterfaceStatsHistThresholded_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistThresholded = _CfprApEtherFcoeInterfaceStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 47),
    _CfprApEtherFcoeInterfaceStatsHistThresholded_Type()
)
cfprApEtherFcoeInterfaceStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistThresholded.setStatus("current")
_CfprApEtherFcoeInterfaceStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherFcoeInterfaceStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherFcoeInterfaceStatsHistTimeCollected = _CfprApEtherFcoeInterfaceStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 5, 1, 48),
    _CfprApEtherFcoeInterfaceStatsHistTimeCollected_Type()
)
cfprApEtherFcoeInterfaceStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFcoeInterfaceStatsHistTimeCollected.setStatus("current")
_CfprApEtherFtwPortPairTable_Object = MibTable
cfprApEtherFtwPortPairTable = _CfprApEtherFtwPortPairTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6)
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairTable.setStatus("current")
_CfprApEtherFtwPortPairEntry_Object = MibTableRow
cfprApEtherFtwPortPairEntry = _CfprApEtherFtwPortPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1)
)
cfprApEtherFtwPortPairEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFtwPortPairInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairEntry.setStatus("current")
_CfprApEtherFtwPortPairInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFtwPortPairInstanceId_Object = MibTableColumn
cfprApEtherFtwPortPairInstanceId = _CfprApEtherFtwPortPairInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 1),
    _CfprApEtherFtwPortPairInstanceId_Type()
)
cfprApEtherFtwPortPairInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairInstanceId.setStatus("current")
_CfprApEtherFtwPortPairDn_Type = CfprApManagedObjectDn
_CfprApEtherFtwPortPairDn_Object = MibTableColumn
cfprApEtherFtwPortPairDn = _CfprApEtherFtwPortPairDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 2),
    _CfprApEtherFtwPortPairDn_Type()
)
cfprApEtherFtwPortPairDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairDn.setStatus("current")
_CfprApEtherFtwPortPairRn_Type = SnmpAdminString
_CfprApEtherFtwPortPairRn_Object = MibTableColumn
cfprApEtherFtwPortPairRn = _CfprApEtherFtwPortPairRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 3),
    _CfprApEtherFtwPortPairRn_Type()
)
cfprApEtherFtwPortPairRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairRn.setStatus("current")
_CfprApEtherFtwPortPairAggrPortId_Type = Gauge32
_CfprApEtherFtwPortPairAggrPortId_Object = MibTableColumn
cfprApEtherFtwPortPairAggrPortId = _CfprApEtherFtwPortPairAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 4),
    _CfprApEtherFtwPortPairAggrPortId_Type()
)
cfprApEtherFtwPortPairAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairAggrPortId.setStatus("current")
_CfprApEtherFtwPortPairChassisId_Type = Gauge32
_CfprApEtherFtwPortPairChassisId_Object = MibTableColumn
cfprApEtherFtwPortPairChassisId = _CfprApEtherFtwPortPairChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 5),
    _CfprApEtherFtwPortPairChassisId_Type()
)
cfprApEtherFtwPortPairChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairChassisId.setStatus("current")
_CfprApEtherFtwPortPairEpDn_Type = SnmpAdminString
_CfprApEtherFtwPortPairEpDn_Object = MibTableColumn
cfprApEtherFtwPortPairEpDn = _CfprApEtherFtwPortPairEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 6),
    _CfprApEtherFtwPortPairEpDn_Type()
)
cfprApEtherFtwPortPairEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairEpDn.setStatus("current")
_CfprApEtherFtwPortPairFsmDescr_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmDescr_Object = MibTableColumn
cfprApEtherFtwPortPairFsmDescr = _CfprApEtherFtwPortPairFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 7),
    _CfprApEtherFtwPortPairFsmDescr_Type()
)
cfprApEtherFtwPortPairFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmDescr.setStatus("current")
_CfprApEtherFtwPortPairFsmPrev_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmPrev_Object = MibTableColumn
cfprApEtherFtwPortPairFsmPrev = _CfprApEtherFtwPortPairFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 8),
    _CfprApEtherFtwPortPairFsmPrev_Type()
)
cfprApEtherFtwPortPairFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmPrev.setStatus("current")
_CfprApEtherFtwPortPairFsmProgr_Type = Gauge32
_CfprApEtherFtwPortPairFsmProgr_Object = MibTableColumn
cfprApEtherFtwPortPairFsmProgr = _CfprApEtherFtwPortPairFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 9),
    _CfprApEtherFtwPortPairFsmProgr_Type()
)
cfprApEtherFtwPortPairFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmProgr.setStatus("current")
_CfprApEtherFtwPortPairFsmRmtInvErrCode_Type = Gauge32
_CfprApEtherFtwPortPairFsmRmtInvErrCode_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRmtInvErrCode = _CfprApEtherFtwPortPairFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 10),
    _CfprApEtherFtwPortPairFsmRmtInvErrCode_Type()
)
cfprApEtherFtwPortPairFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRmtInvErrCode.setStatus("current")
_CfprApEtherFtwPortPairFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmRmtInvErrDescr_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRmtInvErrDescr = _CfprApEtherFtwPortPairFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 11),
    _CfprApEtherFtwPortPairFsmRmtInvErrDescr_Type()
)
cfprApEtherFtwPortPairFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRmtInvErrDescr.setStatus("current")
_CfprApEtherFtwPortPairFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEtherFtwPortPairFsmRmtInvRslt_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRmtInvRslt = _CfprApEtherFtwPortPairFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 12),
    _CfprApEtherFtwPortPairFsmRmtInvRslt_Type()
)
cfprApEtherFtwPortPairFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRmtInvRslt.setStatus("current")
_CfprApEtherFtwPortPairFsmStageDescr_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmStageDescr_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageDescr = _CfprApEtherFtwPortPairFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 13),
    _CfprApEtherFtwPortPairFsmStageDescr_Type()
)
cfprApEtherFtwPortPairFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageDescr.setStatus("current")
_CfprApEtherFtwPortPairFsmStamp_Type = DateAndTime
_CfprApEtherFtwPortPairFsmStamp_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStamp = _CfprApEtherFtwPortPairFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 14),
    _CfprApEtherFtwPortPairFsmStamp_Type()
)
cfprApEtherFtwPortPairFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStamp.setStatus("current")
_CfprApEtherFtwPortPairFsmStatus_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmStatus_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStatus = _CfprApEtherFtwPortPairFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 15),
    _CfprApEtherFtwPortPairFsmStatus_Type()
)
cfprApEtherFtwPortPairFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStatus.setStatus("current")
_CfprApEtherFtwPortPairFsmTry_Type = Gauge32
_CfprApEtherFtwPortPairFsmTry_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTry = _CfprApEtherFtwPortPairFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 16),
    _CfprApEtherFtwPortPairFsmTry_Type()
)
cfprApEtherFtwPortPairFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTry.setStatus("current")
_CfprApEtherFtwPortPairIfRole_Type = CfprApNetworkPortRole
_CfprApEtherFtwPortPairIfRole_Object = MibTableColumn
cfprApEtherFtwPortPairIfRole = _CfprApEtherFtwPortPairIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 17),
    _CfprApEtherFtwPortPairIfRole_Type()
)
cfprApEtherFtwPortPairIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairIfRole.setStatus("current")
_CfprApEtherFtwPortPairIfType_Type = CfprApNetworkPhysEpIfType
_CfprApEtherFtwPortPairIfType_Object = MibTableColumn
cfprApEtherFtwPortPairIfType = _CfprApEtherFtwPortPairIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 18),
    _CfprApEtherFtwPortPairIfType_Type()
)
cfprApEtherFtwPortPairIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairIfType.setStatus("current")
_CfprApEtherFtwPortPairLocale_Type = CfprApNetworkLocale
_CfprApEtherFtwPortPairLocale_Object = MibTableColumn
cfprApEtherFtwPortPairLocale = _CfprApEtherFtwPortPairLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 19),
    _CfprApEtherFtwPortPairLocale_Type()
)
cfprApEtherFtwPortPairLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairLocale.setStatus("current")
_CfprApEtherFtwPortPairMode_Type = CfprApEtherFtwPortPairMode
_CfprApEtherFtwPortPairMode_Object = MibTableColumn
cfprApEtherFtwPortPairMode = _CfprApEtherFtwPortPairMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 20),
    _CfprApEtherFtwPortPairMode_Type()
)
cfprApEtherFtwPortPairMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairMode.setStatus("current")
_CfprApEtherFtwPortPairName_Type = SnmpAdminString
_CfprApEtherFtwPortPairName_Object = MibTableColumn
cfprApEtherFtwPortPairName = _CfprApEtherFtwPortPairName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 21),
    _CfprApEtherFtwPortPairName_Type()
)
cfprApEtherFtwPortPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairName.setStatus("current")
_CfprApEtherFtwPortPairOperMode_Type = CfprApEtherFtwOperMode
_CfprApEtherFtwPortPairOperMode_Object = MibTableColumn
cfprApEtherFtwPortPairOperMode = _CfprApEtherFtwPortPairOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 22),
    _CfprApEtherFtwPortPairOperMode_Type()
)
cfprApEtherFtwPortPairOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairOperMode.setStatus("current")
_CfprApEtherFtwPortPairPeerAggrPortId_Type = Gauge32
_CfprApEtherFtwPortPairPeerAggrPortId_Object = MibTableColumn
cfprApEtherFtwPortPairPeerAggrPortId = _CfprApEtherFtwPortPairPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 23),
    _CfprApEtherFtwPortPairPeerAggrPortId_Type()
)
cfprApEtherFtwPortPairPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPeerAggrPortId.setStatus("current")
_CfprApEtherFtwPortPairPeerChassisId_Type = Gauge32
_CfprApEtherFtwPortPairPeerChassisId_Object = MibTableColumn
cfprApEtherFtwPortPairPeerChassisId = _CfprApEtherFtwPortPairPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 24),
    _CfprApEtherFtwPortPairPeerChassisId_Type()
)
cfprApEtherFtwPortPairPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPeerChassisId.setStatus("current")
_CfprApEtherFtwPortPairPeerDn_Type = SnmpAdminString
_CfprApEtherFtwPortPairPeerDn_Object = MibTableColumn
cfprApEtherFtwPortPairPeerDn = _CfprApEtherFtwPortPairPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 25),
    _CfprApEtherFtwPortPairPeerDn_Type()
)
cfprApEtherFtwPortPairPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPeerDn.setStatus("current")
_CfprApEtherFtwPortPairPeerPortId_Type = Gauge32
_CfprApEtherFtwPortPairPeerPortId_Object = MibTableColumn
cfprApEtherFtwPortPairPeerPortId = _CfprApEtherFtwPortPairPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 26),
    _CfprApEtherFtwPortPairPeerPortId_Type()
)
cfprApEtherFtwPortPairPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPeerPortId.setStatus("current")
_CfprApEtherFtwPortPairPeerPortName_Type = SnmpAdminString
_CfprApEtherFtwPortPairPeerPortName_Object = MibTableColumn
cfprApEtherFtwPortPairPeerPortName = _CfprApEtherFtwPortPairPeerPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 27),
    _CfprApEtherFtwPortPairPeerPortName_Type()
)
cfprApEtherFtwPortPairPeerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPeerPortName.setStatus("current")
_CfprApEtherFtwPortPairPeerSlotId_Type = Gauge32
_CfprApEtherFtwPortPairPeerSlotId_Object = MibTableColumn
cfprApEtherFtwPortPairPeerSlotId = _CfprApEtherFtwPortPairPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 28),
    _CfprApEtherFtwPortPairPeerSlotId_Type()
)
cfprApEtherFtwPortPairPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPeerSlotId.setStatus("current")
_CfprApEtherFtwPortPairPortId_Type = Gauge32
_CfprApEtherFtwPortPairPortId_Object = MibTableColumn
cfprApEtherFtwPortPairPortId = _CfprApEtherFtwPortPairPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 29),
    _CfprApEtherFtwPortPairPortId_Type()
)
cfprApEtherFtwPortPairPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPortId.setStatus("current")
_CfprApEtherFtwPortPairPortName_Type = SnmpAdminString
_CfprApEtherFtwPortPairPortName_Object = MibTableColumn
cfprApEtherFtwPortPairPortName = _CfprApEtherFtwPortPairPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 30),
    _CfprApEtherFtwPortPairPortName_Type()
)
cfprApEtherFtwPortPairPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairPortName.setStatus("current")
_CfprApEtherFtwPortPairSlotId_Type = Gauge32
_CfprApEtherFtwPortPairSlotId_Object = MibTableColumn
cfprApEtherFtwPortPairSlotId = _CfprApEtherFtwPortPairSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 31),
    _CfprApEtherFtwPortPairSlotId_Type()
)
cfprApEtherFtwPortPairSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairSlotId.setStatus("current")
_CfprApEtherFtwPortPairSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherFtwPortPairSwitchId_Object = MibTableColumn
cfprApEtherFtwPortPairSwitchId = _CfprApEtherFtwPortPairSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 32),
    _CfprApEtherFtwPortPairSwitchId_Type()
)
cfprApEtherFtwPortPairSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairSwitchId.setStatus("current")
_CfprApEtherFtwPortPairTransport_Type = CfprApNetworkTransport
_CfprApEtherFtwPortPairTransport_Object = MibTableColumn
cfprApEtherFtwPortPairTransport = _CfprApEtherFtwPortPairTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 33),
    _CfprApEtherFtwPortPairTransport_Type()
)
cfprApEtherFtwPortPairTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairTransport.setStatus("current")
_CfprApEtherFtwPortPairType_Type = CfprApNetworkConnectionType
_CfprApEtherFtwPortPairType_Object = MibTableColumn
cfprApEtherFtwPortPairType = _CfprApEtherFtwPortPairType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 34),
    _CfprApEtherFtwPortPairType_Type()
)
cfprApEtherFtwPortPairType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairType.setStatus("current")
_CfprApEtherFtwPortPairWdtStart_Type = Gauge32
_CfprApEtherFtwPortPairWdtStart_Object = MibTableColumn
cfprApEtherFtwPortPairWdtStart = _CfprApEtherFtwPortPairWdtStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 35),
    _CfprApEtherFtwPortPairWdtStart_Type()
)
cfprApEtherFtwPortPairWdtStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairWdtStart.setStatus("current")
_CfprApEtherFtwPortPairWdtState_Type = CfprApEtherFtwPortPairWdtState
_CfprApEtherFtwPortPairWdtState_Object = MibTableColumn
cfprApEtherFtwPortPairWdtState = _CfprApEtherFtwPortPairWdtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 6, 1, 36),
    _CfprApEtherFtwPortPairWdtState_Type()
)
cfprApEtherFtwPortPairWdtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairWdtState.setStatus("current")
_CfprApEtherFtwPortPairFsmTable_Object = MibTable
cfprApEtherFtwPortPairFsmTable = _CfprApEtherFtwPortPairFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7)
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTable.setStatus("current")
_CfprApEtherFtwPortPairFsmEntry_Object = MibTableRow
cfprApEtherFtwPortPairFsmEntry = _CfprApEtherFtwPortPairFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1)
)
cfprApEtherFtwPortPairFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFtwPortPairFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmEntry.setStatus("current")
_CfprApEtherFtwPortPairFsmInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFtwPortPairFsmInstanceId_Object = MibTableColumn
cfprApEtherFtwPortPairFsmInstanceId = _CfprApEtherFtwPortPairFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 1),
    _CfprApEtherFtwPortPairFsmInstanceId_Type()
)
cfprApEtherFtwPortPairFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmInstanceId.setStatus("current")
_CfprApEtherFtwPortPairFsmDn_Type = CfprApManagedObjectDn
_CfprApEtherFtwPortPairFsmDn_Object = MibTableColumn
cfprApEtherFtwPortPairFsmDn = _CfprApEtherFtwPortPairFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 2),
    _CfprApEtherFtwPortPairFsmDn_Type()
)
cfprApEtherFtwPortPairFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmDn.setStatus("current")
_CfprApEtherFtwPortPairFsmRn_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmRn_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRn = _CfprApEtherFtwPortPairFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 3),
    _CfprApEtherFtwPortPairFsmRn_Type()
)
cfprApEtherFtwPortPairFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRn.setStatus("current")
_CfprApEtherFtwPortPairFsmCompletionTime_Type = DateAndTime
_CfprApEtherFtwPortPairFsmCompletionTime_Object = MibTableColumn
cfprApEtherFtwPortPairFsmCompletionTime = _CfprApEtherFtwPortPairFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 4),
    _CfprApEtherFtwPortPairFsmCompletionTime_Type()
)
cfprApEtherFtwPortPairFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmCompletionTime.setStatus("current")
_CfprApEtherFtwPortPairFsmCurrentFsm_Type = CfprApEtherFtwPortPairFsmCurrentFsm
_CfprApEtherFtwPortPairFsmCurrentFsm_Object = MibTableColumn
cfprApEtherFtwPortPairFsmCurrentFsm = _CfprApEtherFtwPortPairFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 5),
    _CfprApEtherFtwPortPairFsmCurrentFsm_Type()
)
cfprApEtherFtwPortPairFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmCurrentFsm.setStatus("current")
_CfprApEtherFtwPortPairFsmDescrData_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmDescrData_Object = MibTableColumn
cfprApEtherFtwPortPairFsmDescrData = _CfprApEtherFtwPortPairFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 6),
    _CfprApEtherFtwPortPairFsmDescrData_Type()
)
cfprApEtherFtwPortPairFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmDescrData.setStatus("current")
_CfprApEtherFtwPortPairFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApEtherFtwPortPairFsmFsmStatus_Object = MibTableColumn
cfprApEtherFtwPortPairFsmFsmStatus = _CfprApEtherFtwPortPairFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 7),
    _CfprApEtherFtwPortPairFsmFsmStatus_Type()
)
cfprApEtherFtwPortPairFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmFsmStatus.setStatus("current")
_CfprApEtherFtwPortPairFsmProgress_Type = Gauge32
_CfprApEtherFtwPortPairFsmProgress_Object = MibTableColumn
cfprApEtherFtwPortPairFsmProgress = _CfprApEtherFtwPortPairFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 8),
    _CfprApEtherFtwPortPairFsmProgress_Type()
)
cfprApEtherFtwPortPairFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmProgress.setStatus("current")
_CfprApEtherFtwPortPairFsmRmtErrCode_Type = Gauge32
_CfprApEtherFtwPortPairFsmRmtErrCode_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRmtErrCode = _CfprApEtherFtwPortPairFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 9),
    _CfprApEtherFtwPortPairFsmRmtErrCode_Type()
)
cfprApEtherFtwPortPairFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRmtErrCode.setStatus("current")
_CfprApEtherFtwPortPairFsmRmtErrDescr_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmRmtErrDescr_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRmtErrDescr = _CfprApEtherFtwPortPairFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 10),
    _CfprApEtherFtwPortPairFsmRmtErrDescr_Type()
)
cfprApEtherFtwPortPairFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRmtErrDescr.setStatus("current")
_CfprApEtherFtwPortPairFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEtherFtwPortPairFsmRmtRslt_Object = MibTableColumn
cfprApEtherFtwPortPairFsmRmtRslt = _CfprApEtherFtwPortPairFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 7, 1, 11),
    _CfprApEtherFtwPortPairFsmRmtRslt_Type()
)
cfprApEtherFtwPortPairFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmRmtRslt.setStatus("current")
_CfprApEtherFtwPortPairFsmStageTable_Object = MibTable
cfprApEtherFtwPortPairFsmStageTable = _CfprApEtherFtwPortPairFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8)
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageTable.setStatus("current")
_CfprApEtherFtwPortPairFsmStageEntry_Object = MibTableRow
cfprApEtherFtwPortPairFsmStageEntry = _CfprApEtherFtwPortPairFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1)
)
cfprApEtherFtwPortPairFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFtwPortPairFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageEntry.setStatus("current")
_CfprApEtherFtwPortPairFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFtwPortPairFsmStageInstanceId_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageInstanceId = _CfprApEtherFtwPortPairFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 1),
    _CfprApEtherFtwPortPairFsmStageInstanceId_Type()
)
cfprApEtherFtwPortPairFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageInstanceId.setStatus("current")
_CfprApEtherFtwPortPairFsmStageDn_Type = CfprApManagedObjectDn
_CfprApEtherFtwPortPairFsmStageDn_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageDn = _CfprApEtherFtwPortPairFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 2),
    _CfprApEtherFtwPortPairFsmStageDn_Type()
)
cfprApEtherFtwPortPairFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageDn.setStatus("current")
_CfprApEtherFtwPortPairFsmStageRn_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmStageRn_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageRn = _CfprApEtherFtwPortPairFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 3),
    _CfprApEtherFtwPortPairFsmStageRn_Type()
)
cfprApEtherFtwPortPairFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageRn.setStatus("current")
_CfprApEtherFtwPortPairFsmStageDescrData_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmStageDescrData_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageDescrData = _CfprApEtherFtwPortPairFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 4),
    _CfprApEtherFtwPortPairFsmStageDescrData_Type()
)
cfprApEtherFtwPortPairFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageDescrData.setStatus("current")
_CfprApEtherFtwPortPairFsmStageLastUpdateTime_Type = DateAndTime
_CfprApEtherFtwPortPairFsmStageLastUpdateTime_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageLastUpdateTime = _CfprApEtherFtwPortPairFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 5),
    _CfprApEtherFtwPortPairFsmStageLastUpdateTime_Type()
)
cfprApEtherFtwPortPairFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageLastUpdateTime.setStatus("current")
_CfprApEtherFtwPortPairFsmStageName_Type = CfprApEtherFtwPortPairFsmStageName
_CfprApEtherFtwPortPairFsmStageName_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageName = _CfprApEtherFtwPortPairFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 6),
    _CfprApEtherFtwPortPairFsmStageName_Type()
)
cfprApEtherFtwPortPairFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageName.setStatus("current")
_CfprApEtherFtwPortPairFsmStageOrder_Type = Gauge32
_CfprApEtherFtwPortPairFsmStageOrder_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageOrder = _CfprApEtherFtwPortPairFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 7),
    _CfprApEtherFtwPortPairFsmStageOrder_Type()
)
cfprApEtherFtwPortPairFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageOrder.setStatus("current")
_CfprApEtherFtwPortPairFsmStageRetry_Type = Gauge32
_CfprApEtherFtwPortPairFsmStageRetry_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageRetry = _CfprApEtherFtwPortPairFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 8),
    _CfprApEtherFtwPortPairFsmStageRetry_Type()
)
cfprApEtherFtwPortPairFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageRetry.setStatus("current")
_CfprApEtherFtwPortPairFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApEtherFtwPortPairFsmStageStageStatus_Object = MibTableColumn
cfprApEtherFtwPortPairFsmStageStageStatus = _CfprApEtherFtwPortPairFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 8, 1, 9),
    _CfprApEtherFtwPortPairFsmStageStageStatus_Type()
)
cfprApEtherFtwPortPairFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmStageStageStatus.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskTable_Object = MibTable
cfprApEtherFtwPortPairFsmTaskTable = _CfprApEtherFtwPortPairFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9)
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskTable.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskEntry_Object = MibTableRow
cfprApEtherFtwPortPairFsmTaskEntry = _CfprApEtherFtwPortPairFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1)
)
cfprApEtherFtwPortPairFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherFtwPortPairFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskEntry.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApEtherFtwPortPairFsmTaskInstanceId_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskInstanceId = _CfprApEtherFtwPortPairFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 1),
    _CfprApEtherFtwPortPairFsmTaskInstanceId_Type()
)
cfprApEtherFtwPortPairFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskInstanceId.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApEtherFtwPortPairFsmTaskDn_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskDn = _CfprApEtherFtwPortPairFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 2),
    _CfprApEtherFtwPortPairFsmTaskDn_Type()
)
cfprApEtherFtwPortPairFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskDn.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskRn_Type = SnmpAdminString
_CfprApEtherFtwPortPairFsmTaskRn_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskRn = _CfprApEtherFtwPortPairFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 3),
    _CfprApEtherFtwPortPairFsmTaskRn_Type()
)
cfprApEtherFtwPortPairFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskRn.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApEtherFtwPortPairFsmTaskCompletion_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskCompletion = _CfprApEtherFtwPortPairFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 4),
    _CfprApEtherFtwPortPairFsmTaskCompletion_Type()
)
cfprApEtherFtwPortPairFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskCompletion.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskFlags_Type = CfprApFsmFlags
_CfprApEtherFtwPortPairFsmTaskFlags_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskFlags = _CfprApEtherFtwPortPairFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 5),
    _CfprApEtherFtwPortPairFsmTaskFlags_Type()
)
cfprApEtherFtwPortPairFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskFlags.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskItem_Type = CfprApEtherFtwPortPairFsmTaskItem
_CfprApEtherFtwPortPairFsmTaskItem_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskItem = _CfprApEtherFtwPortPairFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 6),
    _CfprApEtherFtwPortPairFsmTaskItem_Type()
)
cfprApEtherFtwPortPairFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskItem.setStatus("current")
_CfprApEtherFtwPortPairFsmTaskSeqId_Type = Gauge32
_CfprApEtherFtwPortPairFsmTaskSeqId_Object = MibTableColumn
cfprApEtherFtwPortPairFsmTaskSeqId = _CfprApEtherFtwPortPairFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 9, 1, 7),
    _CfprApEtherFtwPortPairFsmTaskSeqId_Type()
)
cfprApEtherFtwPortPairFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherFtwPortPairFsmTaskSeqId.setStatus("current")
_CfprApEtherLossStatsTable_Object = MibTable
cfprApEtherLossStatsTable = _CfprApEtherLossStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10)
)
if mibBuilder.loadTexts:
    cfprApEtherLossStatsTable.setStatus("current")
_CfprApEtherLossStatsEntry_Object = MibTableRow
cfprApEtherLossStatsEntry = _CfprApEtherLossStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1)
)
cfprApEtherLossStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherLossStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherLossStatsEntry.setStatus("current")
_CfprApEtherLossStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherLossStatsInstanceId_Object = MibTableColumn
cfprApEtherLossStatsInstanceId = _CfprApEtherLossStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 1),
    _CfprApEtherLossStatsInstanceId_Type()
)
cfprApEtherLossStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsInstanceId.setStatus("current")
_CfprApEtherLossStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherLossStatsDn_Object = MibTableColumn
cfprApEtherLossStatsDn = _CfprApEtherLossStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 2),
    _CfprApEtherLossStatsDn_Type()
)
cfprApEtherLossStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsDn.setStatus("current")
_CfprApEtherLossStatsRn_Type = SnmpAdminString
_CfprApEtherLossStatsRn_Object = MibTableColumn
cfprApEtherLossStatsRn = _CfprApEtherLossStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 3),
    _CfprApEtherLossStatsRn_Type()
)
cfprApEtherLossStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsRn.setStatus("current")
_CfprApEtherLossStatsSQETest_Type = Unsigned64
_CfprApEtherLossStatsSQETest_Object = MibTableColumn
cfprApEtherLossStatsSQETest = _CfprApEtherLossStatsSQETest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 4),
    _CfprApEtherLossStatsSQETest_Type()
)
cfprApEtherLossStatsSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSQETest.setStatus("current")
_CfprApEtherLossStatsSQETestDelta_Type = Counter64
_CfprApEtherLossStatsSQETestDelta_Object = MibTableColumn
cfprApEtherLossStatsSQETestDelta = _CfprApEtherLossStatsSQETestDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 5),
    _CfprApEtherLossStatsSQETestDelta_Type()
)
cfprApEtherLossStatsSQETestDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSQETestDelta.setStatus("current")
_CfprApEtherLossStatsSQETestDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsSQETestDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsSQETestDeltaAvg = _CfprApEtherLossStatsSQETestDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 6),
    _CfprApEtherLossStatsSQETestDeltaAvg_Type()
)
cfprApEtherLossStatsSQETestDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSQETestDeltaAvg.setStatus("current")
_CfprApEtherLossStatsSQETestDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsSQETestDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsSQETestDeltaMax = _CfprApEtherLossStatsSQETestDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 7),
    _CfprApEtherLossStatsSQETestDeltaMax_Type()
)
cfprApEtherLossStatsSQETestDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSQETestDeltaMax.setStatus("current")
_CfprApEtherLossStatsSQETestDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsSQETestDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsSQETestDeltaMin = _CfprApEtherLossStatsSQETestDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 8),
    _CfprApEtherLossStatsSQETestDeltaMin_Type()
)
cfprApEtherLossStatsSQETestDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSQETestDeltaMin.setStatus("current")
_CfprApEtherLossStatsCarrierSense_Type = Unsigned64
_CfprApEtherLossStatsCarrierSense_Object = MibTableColumn
cfprApEtherLossStatsCarrierSense = _CfprApEtherLossStatsCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 9),
    _CfprApEtherLossStatsCarrierSense_Type()
)
cfprApEtherLossStatsCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsCarrierSense.setStatus("current")
_CfprApEtherLossStatsCarrierSenseDelta_Type = Counter64
_CfprApEtherLossStatsCarrierSenseDelta_Object = MibTableColumn
cfprApEtherLossStatsCarrierSenseDelta = _CfprApEtherLossStatsCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 10),
    _CfprApEtherLossStatsCarrierSenseDelta_Type()
)
cfprApEtherLossStatsCarrierSenseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsCarrierSenseDelta.setStatus("current")
_CfprApEtherLossStatsCarrierSenseDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsCarrierSenseDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsCarrierSenseDeltaAvg = _CfprApEtherLossStatsCarrierSenseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 11),
    _CfprApEtherLossStatsCarrierSenseDeltaAvg_Type()
)
cfprApEtherLossStatsCarrierSenseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsCarrierSenseDeltaAvg.setStatus("current")
_CfprApEtherLossStatsCarrierSenseDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsCarrierSenseDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsCarrierSenseDeltaMax = _CfprApEtherLossStatsCarrierSenseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 12),
    _CfprApEtherLossStatsCarrierSenseDeltaMax_Type()
)
cfprApEtherLossStatsCarrierSenseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsCarrierSenseDeltaMax.setStatus("current")
_CfprApEtherLossStatsCarrierSenseDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsCarrierSenseDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsCarrierSenseDeltaMin = _CfprApEtherLossStatsCarrierSenseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 13),
    _CfprApEtherLossStatsCarrierSenseDeltaMin_Type()
)
cfprApEtherLossStatsCarrierSenseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsCarrierSenseDeltaMin.setStatus("current")
_CfprApEtherLossStatsExcessCollision_Type = Unsigned64
_CfprApEtherLossStatsExcessCollision_Object = MibTableColumn
cfprApEtherLossStatsExcessCollision = _CfprApEtherLossStatsExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 14),
    _CfprApEtherLossStatsExcessCollision_Type()
)
cfprApEtherLossStatsExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsExcessCollision.setStatus("current")
_CfprApEtherLossStatsExcessCollisionDelta_Type = Counter64
_CfprApEtherLossStatsExcessCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsExcessCollisionDelta = _CfprApEtherLossStatsExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 15),
    _CfprApEtherLossStatsExcessCollisionDelta_Type()
)
cfprApEtherLossStatsExcessCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsExcessCollisionDelta.setStatus("current")
_CfprApEtherLossStatsExcessCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsExcessCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsExcessCollisionDeltaAvg = _CfprApEtherLossStatsExcessCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 16),
    _CfprApEtherLossStatsExcessCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsExcessCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsExcessCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsExcessCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsExcessCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsExcessCollisionDeltaMax = _CfprApEtherLossStatsExcessCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 17),
    _CfprApEtherLossStatsExcessCollisionDeltaMax_Type()
)
cfprApEtherLossStatsExcessCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsExcessCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsExcessCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsExcessCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsExcessCollisionDeltaMin = _CfprApEtherLossStatsExcessCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 18),
    _CfprApEtherLossStatsExcessCollisionDeltaMin_Type()
)
cfprApEtherLossStatsExcessCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsExcessCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsGiants_Type = Unsigned64
_CfprApEtherLossStatsGiants_Object = MibTableColumn
cfprApEtherLossStatsGiants = _CfprApEtherLossStatsGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 19),
    _CfprApEtherLossStatsGiants_Type()
)
cfprApEtherLossStatsGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsGiants.setStatus("current")
_CfprApEtherLossStatsGiantsDelta_Type = Counter64
_CfprApEtherLossStatsGiantsDelta_Object = MibTableColumn
cfprApEtherLossStatsGiantsDelta = _CfprApEtherLossStatsGiantsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 20),
    _CfprApEtherLossStatsGiantsDelta_Type()
)
cfprApEtherLossStatsGiantsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsGiantsDelta.setStatus("current")
_CfprApEtherLossStatsGiantsDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsGiantsDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsGiantsDeltaAvg = _CfprApEtherLossStatsGiantsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 21),
    _CfprApEtherLossStatsGiantsDeltaAvg_Type()
)
cfprApEtherLossStatsGiantsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsGiantsDeltaAvg.setStatus("current")
_CfprApEtherLossStatsGiantsDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsGiantsDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsGiantsDeltaMax = _CfprApEtherLossStatsGiantsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 22),
    _CfprApEtherLossStatsGiantsDeltaMax_Type()
)
cfprApEtherLossStatsGiantsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsGiantsDeltaMax.setStatus("current")
_CfprApEtherLossStatsGiantsDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsGiantsDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsGiantsDeltaMin = _CfprApEtherLossStatsGiantsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 23),
    _CfprApEtherLossStatsGiantsDeltaMin_Type()
)
cfprApEtherLossStatsGiantsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsGiantsDeltaMin.setStatus("current")
_CfprApEtherLossStatsIntervals_Type = Gauge32
_CfprApEtherLossStatsIntervals_Object = MibTableColumn
cfprApEtherLossStatsIntervals = _CfprApEtherLossStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 24),
    _CfprApEtherLossStatsIntervals_Type()
)
cfprApEtherLossStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsIntervals.setStatus("current")
_CfprApEtherLossStatsLateCollision_Type = Unsigned64
_CfprApEtherLossStatsLateCollision_Object = MibTableColumn
cfprApEtherLossStatsLateCollision = _CfprApEtherLossStatsLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 25),
    _CfprApEtherLossStatsLateCollision_Type()
)
cfprApEtherLossStatsLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsLateCollision.setStatus("current")
_CfprApEtherLossStatsLateCollisionDelta_Type = Counter64
_CfprApEtherLossStatsLateCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsLateCollisionDelta = _CfprApEtherLossStatsLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 26),
    _CfprApEtherLossStatsLateCollisionDelta_Type()
)
cfprApEtherLossStatsLateCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsLateCollisionDelta.setStatus("current")
_CfprApEtherLossStatsLateCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsLateCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsLateCollisionDeltaAvg = _CfprApEtherLossStatsLateCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 27),
    _CfprApEtherLossStatsLateCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsLateCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsLateCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsLateCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsLateCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsLateCollisionDeltaMax = _CfprApEtherLossStatsLateCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 28),
    _CfprApEtherLossStatsLateCollisionDeltaMax_Type()
)
cfprApEtherLossStatsLateCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsLateCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsLateCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsLateCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsLateCollisionDeltaMin = _CfprApEtherLossStatsLateCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 29),
    _CfprApEtherLossStatsLateCollisionDeltaMin_Type()
)
cfprApEtherLossStatsLateCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsLateCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsMultiCollision_Type = Unsigned64
_CfprApEtherLossStatsMultiCollision_Object = MibTableColumn
cfprApEtherLossStatsMultiCollision = _CfprApEtherLossStatsMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 30),
    _CfprApEtherLossStatsMultiCollision_Type()
)
cfprApEtherLossStatsMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsMultiCollision.setStatus("current")
_CfprApEtherLossStatsMultiCollisionDelta_Type = Counter64
_CfprApEtherLossStatsMultiCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsMultiCollisionDelta = _CfprApEtherLossStatsMultiCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 31),
    _CfprApEtherLossStatsMultiCollisionDelta_Type()
)
cfprApEtherLossStatsMultiCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsMultiCollisionDelta.setStatus("current")
_CfprApEtherLossStatsMultiCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsMultiCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsMultiCollisionDeltaAvg = _CfprApEtherLossStatsMultiCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 32),
    _CfprApEtherLossStatsMultiCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsMultiCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsMultiCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsMultiCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsMultiCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsMultiCollisionDeltaMax = _CfprApEtherLossStatsMultiCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 33),
    _CfprApEtherLossStatsMultiCollisionDeltaMax_Type()
)
cfprApEtherLossStatsMultiCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsMultiCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsMultiCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsMultiCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsMultiCollisionDeltaMin = _CfprApEtherLossStatsMultiCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 34),
    _CfprApEtherLossStatsMultiCollisionDeltaMin_Type()
)
cfprApEtherLossStatsMultiCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsMultiCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsSingleCollision_Type = Unsigned64
_CfprApEtherLossStatsSingleCollision_Object = MibTableColumn
cfprApEtherLossStatsSingleCollision = _CfprApEtherLossStatsSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 35),
    _CfprApEtherLossStatsSingleCollision_Type()
)
cfprApEtherLossStatsSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSingleCollision.setStatus("current")
_CfprApEtherLossStatsSingleCollisionDelta_Type = Counter64
_CfprApEtherLossStatsSingleCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsSingleCollisionDelta = _CfprApEtherLossStatsSingleCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 36),
    _CfprApEtherLossStatsSingleCollisionDelta_Type()
)
cfprApEtherLossStatsSingleCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSingleCollisionDelta.setStatus("current")
_CfprApEtherLossStatsSingleCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsSingleCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsSingleCollisionDeltaAvg = _CfprApEtherLossStatsSingleCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 37),
    _CfprApEtherLossStatsSingleCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsSingleCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSingleCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsSingleCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsSingleCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsSingleCollisionDeltaMax = _CfprApEtherLossStatsSingleCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 38),
    _CfprApEtherLossStatsSingleCollisionDeltaMax_Type()
)
cfprApEtherLossStatsSingleCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSingleCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsSingleCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsSingleCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsSingleCollisionDeltaMin = _CfprApEtherLossStatsSingleCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 39),
    _CfprApEtherLossStatsSingleCollisionDeltaMin_Type()
)
cfprApEtherLossStatsSingleCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSingleCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsSuspect_Type = TruthValue
_CfprApEtherLossStatsSuspect_Object = MibTableColumn
cfprApEtherLossStatsSuspect = _CfprApEtherLossStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 40),
    _CfprApEtherLossStatsSuspect_Type()
)
cfprApEtherLossStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSuspect.setStatus("current")
_CfprApEtherLossStatsSymbol_Type = Unsigned64
_CfprApEtherLossStatsSymbol_Object = MibTableColumn
cfprApEtherLossStatsSymbol = _CfprApEtherLossStatsSymbol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 41),
    _CfprApEtherLossStatsSymbol_Type()
)
cfprApEtherLossStatsSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSymbol.setStatus("current")
_CfprApEtherLossStatsSymbolDelta_Type = Counter64
_CfprApEtherLossStatsSymbolDelta_Object = MibTableColumn
cfprApEtherLossStatsSymbolDelta = _CfprApEtherLossStatsSymbolDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 42),
    _CfprApEtherLossStatsSymbolDelta_Type()
)
cfprApEtherLossStatsSymbolDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSymbolDelta.setStatus("current")
_CfprApEtherLossStatsSymbolDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsSymbolDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsSymbolDeltaAvg = _CfprApEtherLossStatsSymbolDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 43),
    _CfprApEtherLossStatsSymbolDeltaAvg_Type()
)
cfprApEtherLossStatsSymbolDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSymbolDeltaAvg.setStatus("current")
_CfprApEtherLossStatsSymbolDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsSymbolDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsSymbolDeltaMax = _CfprApEtherLossStatsSymbolDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 44),
    _CfprApEtherLossStatsSymbolDeltaMax_Type()
)
cfprApEtherLossStatsSymbolDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSymbolDeltaMax.setStatus("current")
_CfprApEtherLossStatsSymbolDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsSymbolDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsSymbolDeltaMin = _CfprApEtherLossStatsSymbolDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 45),
    _CfprApEtherLossStatsSymbolDeltaMin_Type()
)
cfprApEtherLossStatsSymbolDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsSymbolDeltaMin.setStatus("current")
_CfprApEtherLossStatsThresholded_Type = CfprApEtherLossStatsThresholded
_CfprApEtherLossStatsThresholded_Object = MibTableColumn
cfprApEtherLossStatsThresholded = _CfprApEtherLossStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 46),
    _CfprApEtherLossStatsThresholded_Type()
)
cfprApEtherLossStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsThresholded.setStatus("current")
_CfprApEtherLossStatsTimeCollected_Type = DateAndTime
_CfprApEtherLossStatsTimeCollected_Object = MibTableColumn
cfprApEtherLossStatsTimeCollected = _CfprApEtherLossStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 47),
    _CfprApEtherLossStatsTimeCollected_Type()
)
cfprApEtherLossStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsTimeCollected.setStatus("current")
_CfprApEtherLossStatsUpdate_Type = Gauge32
_CfprApEtherLossStatsUpdate_Object = MibTableColumn
cfprApEtherLossStatsUpdate = _CfprApEtherLossStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 10, 1, 48),
    _CfprApEtherLossStatsUpdate_Type()
)
cfprApEtherLossStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsUpdate.setStatus("current")
_CfprApEtherLossStatsHistTable_Object = MibTable
cfprApEtherLossStatsHistTable = _CfprApEtherLossStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11)
)
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistTable.setStatus("current")
_CfprApEtherLossStatsHistEntry_Object = MibTableRow
cfprApEtherLossStatsHistEntry = _CfprApEtherLossStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1)
)
cfprApEtherLossStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherLossStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistEntry.setStatus("current")
_CfprApEtherLossStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherLossStatsHistInstanceId_Object = MibTableColumn
cfprApEtherLossStatsHistInstanceId = _CfprApEtherLossStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 1),
    _CfprApEtherLossStatsHistInstanceId_Type()
)
cfprApEtherLossStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistInstanceId.setStatus("current")
_CfprApEtherLossStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherLossStatsHistDn_Object = MibTableColumn
cfprApEtherLossStatsHistDn = _CfprApEtherLossStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 2),
    _CfprApEtherLossStatsHistDn_Type()
)
cfprApEtherLossStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistDn.setStatus("current")
_CfprApEtherLossStatsHistRn_Type = SnmpAdminString
_CfprApEtherLossStatsHistRn_Object = MibTableColumn
cfprApEtherLossStatsHistRn = _CfprApEtherLossStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 3),
    _CfprApEtherLossStatsHistRn_Type()
)
cfprApEtherLossStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistRn.setStatus("current")
_CfprApEtherLossStatsHistSQETest_Type = Unsigned64
_CfprApEtherLossStatsHistSQETest_Object = MibTableColumn
cfprApEtherLossStatsHistSQETest = _CfprApEtherLossStatsHistSQETest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 4),
    _CfprApEtherLossStatsHistSQETest_Type()
)
cfprApEtherLossStatsHistSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSQETest.setStatus("current")
_CfprApEtherLossStatsHistSQETestDelta_Type = Unsigned64
_CfprApEtherLossStatsHistSQETestDelta_Object = MibTableColumn
cfprApEtherLossStatsHistSQETestDelta = _CfprApEtherLossStatsHistSQETestDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 5),
    _CfprApEtherLossStatsHistSQETestDelta_Type()
)
cfprApEtherLossStatsHistSQETestDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSQETestDelta.setStatus("current")
_CfprApEtherLossStatsHistSQETestDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistSQETestDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistSQETestDeltaAvg = _CfprApEtherLossStatsHistSQETestDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 6),
    _CfprApEtherLossStatsHistSQETestDeltaAvg_Type()
)
cfprApEtherLossStatsHistSQETestDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSQETestDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistSQETestDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistSQETestDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistSQETestDeltaMax = _CfprApEtherLossStatsHistSQETestDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 7),
    _CfprApEtherLossStatsHistSQETestDeltaMax_Type()
)
cfprApEtherLossStatsHistSQETestDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSQETestDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistSQETestDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistSQETestDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistSQETestDeltaMin = _CfprApEtherLossStatsHistSQETestDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 8),
    _CfprApEtherLossStatsHistSQETestDeltaMin_Type()
)
cfprApEtherLossStatsHistSQETestDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSQETestDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistCarrierSense_Type = Unsigned64
_CfprApEtherLossStatsHistCarrierSense_Object = MibTableColumn
cfprApEtherLossStatsHistCarrierSense = _CfprApEtherLossStatsHistCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 9),
    _CfprApEtherLossStatsHistCarrierSense_Type()
)
cfprApEtherLossStatsHistCarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistCarrierSense.setStatus("current")
_CfprApEtherLossStatsHistCarrierSenseDelta_Type = Unsigned64
_CfprApEtherLossStatsHistCarrierSenseDelta_Object = MibTableColumn
cfprApEtherLossStatsHistCarrierSenseDelta = _CfprApEtherLossStatsHistCarrierSenseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 10),
    _CfprApEtherLossStatsHistCarrierSenseDelta_Type()
)
cfprApEtherLossStatsHistCarrierSenseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistCarrierSenseDelta.setStatus("current")
_CfprApEtherLossStatsHistCarrierSenseDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistCarrierSenseDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistCarrierSenseDeltaAvg = _CfprApEtherLossStatsHistCarrierSenseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 11),
    _CfprApEtherLossStatsHistCarrierSenseDeltaAvg_Type()
)
cfprApEtherLossStatsHistCarrierSenseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistCarrierSenseDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistCarrierSenseDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistCarrierSenseDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistCarrierSenseDeltaMax = _CfprApEtherLossStatsHistCarrierSenseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 12),
    _CfprApEtherLossStatsHistCarrierSenseDeltaMax_Type()
)
cfprApEtherLossStatsHistCarrierSenseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistCarrierSenseDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistCarrierSenseDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistCarrierSenseDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistCarrierSenseDeltaMin = _CfprApEtherLossStatsHistCarrierSenseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 13),
    _CfprApEtherLossStatsHistCarrierSenseDeltaMin_Type()
)
cfprApEtherLossStatsHistCarrierSenseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistCarrierSenseDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistExcessCollision_Type = Unsigned64
_CfprApEtherLossStatsHistExcessCollision_Object = MibTableColumn
cfprApEtherLossStatsHistExcessCollision = _CfprApEtherLossStatsHistExcessCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 14),
    _CfprApEtherLossStatsHistExcessCollision_Type()
)
cfprApEtherLossStatsHistExcessCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistExcessCollision.setStatus("current")
_CfprApEtherLossStatsHistExcessCollisionDelta_Type = Unsigned64
_CfprApEtherLossStatsHistExcessCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsHistExcessCollisionDelta = _CfprApEtherLossStatsHistExcessCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 15),
    _CfprApEtherLossStatsHistExcessCollisionDelta_Type()
)
cfprApEtherLossStatsHistExcessCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistExcessCollisionDelta.setStatus("current")
_CfprApEtherLossStatsHistExcessCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistExcessCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistExcessCollisionDeltaAvg = _CfprApEtherLossStatsHistExcessCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 16),
    _CfprApEtherLossStatsHistExcessCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsHistExcessCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistExcessCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistExcessCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistExcessCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistExcessCollisionDeltaMax = _CfprApEtherLossStatsHistExcessCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 17),
    _CfprApEtherLossStatsHistExcessCollisionDeltaMax_Type()
)
cfprApEtherLossStatsHistExcessCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistExcessCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistExcessCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistExcessCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistExcessCollisionDeltaMin = _CfprApEtherLossStatsHistExcessCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 18),
    _CfprApEtherLossStatsHistExcessCollisionDeltaMin_Type()
)
cfprApEtherLossStatsHistExcessCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistExcessCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistGiants_Type = Unsigned64
_CfprApEtherLossStatsHistGiants_Object = MibTableColumn
cfprApEtherLossStatsHistGiants = _CfprApEtherLossStatsHistGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 19),
    _CfprApEtherLossStatsHistGiants_Type()
)
cfprApEtherLossStatsHistGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistGiants.setStatus("current")
_CfprApEtherLossStatsHistGiantsDelta_Type = Unsigned64
_CfprApEtherLossStatsHistGiantsDelta_Object = MibTableColumn
cfprApEtherLossStatsHistGiantsDelta = _CfprApEtherLossStatsHistGiantsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 20),
    _CfprApEtherLossStatsHistGiantsDelta_Type()
)
cfprApEtherLossStatsHistGiantsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistGiantsDelta.setStatus("current")
_CfprApEtherLossStatsHistGiantsDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistGiantsDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistGiantsDeltaAvg = _CfprApEtherLossStatsHistGiantsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 21),
    _CfprApEtherLossStatsHistGiantsDeltaAvg_Type()
)
cfprApEtherLossStatsHistGiantsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistGiantsDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistGiantsDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistGiantsDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistGiantsDeltaMax = _CfprApEtherLossStatsHistGiantsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 22),
    _CfprApEtherLossStatsHistGiantsDeltaMax_Type()
)
cfprApEtherLossStatsHistGiantsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistGiantsDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistGiantsDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistGiantsDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistGiantsDeltaMin = _CfprApEtherLossStatsHistGiantsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 23),
    _CfprApEtherLossStatsHistGiantsDeltaMin_Type()
)
cfprApEtherLossStatsHistGiantsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistGiantsDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistId_Type = Unsigned64
_CfprApEtherLossStatsHistId_Object = MibTableColumn
cfprApEtherLossStatsHistId = _CfprApEtherLossStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 24),
    _CfprApEtherLossStatsHistId_Type()
)
cfprApEtherLossStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistId.setStatus("current")
_CfprApEtherLossStatsHistLateCollision_Type = Unsigned64
_CfprApEtherLossStatsHistLateCollision_Object = MibTableColumn
cfprApEtherLossStatsHistLateCollision = _CfprApEtherLossStatsHistLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 25),
    _CfprApEtherLossStatsHistLateCollision_Type()
)
cfprApEtherLossStatsHistLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistLateCollision.setStatus("current")
_CfprApEtherLossStatsHistLateCollisionDelta_Type = Unsigned64
_CfprApEtherLossStatsHistLateCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsHistLateCollisionDelta = _CfprApEtherLossStatsHistLateCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 26),
    _CfprApEtherLossStatsHistLateCollisionDelta_Type()
)
cfprApEtherLossStatsHistLateCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistLateCollisionDelta.setStatus("current")
_CfprApEtherLossStatsHistLateCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistLateCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistLateCollisionDeltaAvg = _CfprApEtherLossStatsHistLateCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 27),
    _CfprApEtherLossStatsHistLateCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsHistLateCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistLateCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistLateCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistLateCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistLateCollisionDeltaMax = _CfprApEtherLossStatsHistLateCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 28),
    _CfprApEtherLossStatsHistLateCollisionDeltaMax_Type()
)
cfprApEtherLossStatsHistLateCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistLateCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistLateCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistLateCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistLateCollisionDeltaMin = _CfprApEtherLossStatsHistLateCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 29),
    _CfprApEtherLossStatsHistLateCollisionDeltaMin_Type()
)
cfprApEtherLossStatsHistLateCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistLateCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistMostRecent_Type = TruthValue
_CfprApEtherLossStatsHistMostRecent_Object = MibTableColumn
cfprApEtherLossStatsHistMostRecent = _CfprApEtherLossStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 30),
    _CfprApEtherLossStatsHistMostRecent_Type()
)
cfprApEtherLossStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistMostRecent.setStatus("current")
_CfprApEtherLossStatsHistMultiCollision_Type = Unsigned64
_CfprApEtherLossStatsHistMultiCollision_Object = MibTableColumn
cfprApEtherLossStatsHistMultiCollision = _CfprApEtherLossStatsHistMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 31),
    _CfprApEtherLossStatsHistMultiCollision_Type()
)
cfprApEtherLossStatsHistMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistMultiCollision.setStatus("current")
_CfprApEtherLossStatsHistMultiCollisionDelta_Type = Unsigned64
_CfprApEtherLossStatsHistMultiCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsHistMultiCollisionDelta = _CfprApEtherLossStatsHistMultiCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 32),
    _CfprApEtherLossStatsHistMultiCollisionDelta_Type()
)
cfprApEtherLossStatsHistMultiCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistMultiCollisionDelta.setStatus("current")
_CfprApEtherLossStatsHistMultiCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistMultiCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistMultiCollisionDeltaAvg = _CfprApEtherLossStatsHistMultiCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 33),
    _CfprApEtherLossStatsHistMultiCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsHistMultiCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistMultiCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistMultiCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistMultiCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistMultiCollisionDeltaMax = _CfprApEtherLossStatsHistMultiCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 34),
    _CfprApEtherLossStatsHistMultiCollisionDeltaMax_Type()
)
cfprApEtherLossStatsHistMultiCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistMultiCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistMultiCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistMultiCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistMultiCollisionDeltaMin = _CfprApEtherLossStatsHistMultiCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 35),
    _CfprApEtherLossStatsHistMultiCollisionDeltaMin_Type()
)
cfprApEtherLossStatsHistMultiCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistMultiCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistSingleCollision_Type = Unsigned64
_CfprApEtherLossStatsHistSingleCollision_Object = MibTableColumn
cfprApEtherLossStatsHistSingleCollision = _CfprApEtherLossStatsHistSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 36),
    _CfprApEtherLossStatsHistSingleCollision_Type()
)
cfprApEtherLossStatsHistSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSingleCollision.setStatus("current")
_CfprApEtherLossStatsHistSingleCollisionDelta_Type = Unsigned64
_CfprApEtherLossStatsHistSingleCollisionDelta_Object = MibTableColumn
cfprApEtherLossStatsHistSingleCollisionDelta = _CfprApEtherLossStatsHistSingleCollisionDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 37),
    _CfprApEtherLossStatsHistSingleCollisionDelta_Type()
)
cfprApEtherLossStatsHistSingleCollisionDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSingleCollisionDelta.setStatus("current")
_CfprApEtherLossStatsHistSingleCollisionDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistSingleCollisionDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistSingleCollisionDeltaAvg = _CfprApEtherLossStatsHistSingleCollisionDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 38),
    _CfprApEtherLossStatsHistSingleCollisionDeltaAvg_Type()
)
cfprApEtherLossStatsHistSingleCollisionDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSingleCollisionDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistSingleCollisionDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistSingleCollisionDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistSingleCollisionDeltaMax = _CfprApEtherLossStatsHistSingleCollisionDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 39),
    _CfprApEtherLossStatsHistSingleCollisionDeltaMax_Type()
)
cfprApEtherLossStatsHistSingleCollisionDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSingleCollisionDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistSingleCollisionDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistSingleCollisionDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistSingleCollisionDeltaMin = _CfprApEtherLossStatsHistSingleCollisionDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 40),
    _CfprApEtherLossStatsHistSingleCollisionDeltaMin_Type()
)
cfprApEtherLossStatsHistSingleCollisionDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSingleCollisionDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistSuspect_Type = TruthValue
_CfprApEtherLossStatsHistSuspect_Object = MibTableColumn
cfprApEtherLossStatsHistSuspect = _CfprApEtherLossStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 41),
    _CfprApEtherLossStatsHistSuspect_Type()
)
cfprApEtherLossStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSuspect.setStatus("current")
_CfprApEtherLossStatsHistSymbol_Type = Unsigned64
_CfprApEtherLossStatsHistSymbol_Object = MibTableColumn
cfprApEtherLossStatsHistSymbol = _CfprApEtherLossStatsHistSymbol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 42),
    _CfprApEtherLossStatsHistSymbol_Type()
)
cfprApEtherLossStatsHistSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSymbol.setStatus("current")
_CfprApEtherLossStatsHistSymbolDelta_Type = Unsigned64
_CfprApEtherLossStatsHistSymbolDelta_Object = MibTableColumn
cfprApEtherLossStatsHistSymbolDelta = _CfprApEtherLossStatsHistSymbolDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 43),
    _CfprApEtherLossStatsHistSymbolDelta_Type()
)
cfprApEtherLossStatsHistSymbolDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSymbolDelta.setStatus("current")
_CfprApEtherLossStatsHistSymbolDeltaAvg_Type = Unsigned64
_CfprApEtherLossStatsHistSymbolDeltaAvg_Object = MibTableColumn
cfprApEtherLossStatsHistSymbolDeltaAvg = _CfprApEtherLossStatsHistSymbolDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 44),
    _CfprApEtherLossStatsHistSymbolDeltaAvg_Type()
)
cfprApEtherLossStatsHistSymbolDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSymbolDeltaAvg.setStatus("current")
_CfprApEtherLossStatsHistSymbolDeltaMax_Type = Unsigned64
_CfprApEtherLossStatsHistSymbolDeltaMax_Object = MibTableColumn
cfprApEtherLossStatsHistSymbolDeltaMax = _CfprApEtherLossStatsHistSymbolDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 45),
    _CfprApEtherLossStatsHistSymbolDeltaMax_Type()
)
cfprApEtherLossStatsHistSymbolDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSymbolDeltaMax.setStatus("current")
_CfprApEtherLossStatsHistSymbolDeltaMin_Type = Unsigned64
_CfprApEtherLossStatsHistSymbolDeltaMin_Object = MibTableColumn
cfprApEtherLossStatsHistSymbolDeltaMin = _CfprApEtherLossStatsHistSymbolDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 46),
    _CfprApEtherLossStatsHistSymbolDeltaMin_Type()
)
cfprApEtherLossStatsHistSymbolDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistSymbolDeltaMin.setStatus("current")
_CfprApEtherLossStatsHistThresholded_Type = CfprApEtherLossStatsHistThresholded
_CfprApEtherLossStatsHistThresholded_Object = MibTableColumn
cfprApEtherLossStatsHistThresholded = _CfprApEtherLossStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 47),
    _CfprApEtherLossStatsHistThresholded_Type()
)
cfprApEtherLossStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistThresholded.setStatus("current")
_CfprApEtherLossStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherLossStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherLossStatsHistTimeCollected = _CfprApEtherLossStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 11, 1, 48),
    _CfprApEtherLossStatsHistTimeCollected_Type()
)
cfprApEtherLossStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherLossStatsHistTimeCollected.setStatus("current")
_CfprApEtherNiErrStatsTable_Object = MibTable
cfprApEtherNiErrStatsTable = _CfprApEtherNiErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12)
)
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTable.setStatus("current")
_CfprApEtherNiErrStatsEntry_Object = MibTableRow
cfprApEtherNiErrStatsEntry = _CfprApEtherNiErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1)
)
cfprApEtherNiErrStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherNiErrStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsEntry.setStatus("current")
_CfprApEtherNiErrStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherNiErrStatsInstanceId_Object = MibTableColumn
cfprApEtherNiErrStatsInstanceId = _CfprApEtherNiErrStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 1),
    _CfprApEtherNiErrStatsInstanceId_Type()
)
cfprApEtherNiErrStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsInstanceId.setStatus("current")
_CfprApEtherNiErrStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherNiErrStatsDn_Object = MibTableColumn
cfprApEtherNiErrStatsDn = _CfprApEtherNiErrStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 2),
    _CfprApEtherNiErrStatsDn_Type()
)
cfprApEtherNiErrStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsDn.setStatus("current")
_CfprApEtherNiErrStatsRn_Type = SnmpAdminString
_CfprApEtherNiErrStatsRn_Object = MibTableColumn
cfprApEtherNiErrStatsRn = _CfprApEtherNiErrStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 3),
    _CfprApEtherNiErrStatsRn_Type()
)
cfprApEtherNiErrStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsRn.setStatus("current")
_CfprApEtherNiErrStatsCrc_Type = Unsigned64
_CfprApEtherNiErrStatsCrc_Object = MibTableColumn
cfprApEtherNiErrStatsCrc = _CfprApEtherNiErrStatsCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 4),
    _CfprApEtherNiErrStatsCrc_Type()
)
cfprApEtherNiErrStatsCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsCrc.setStatus("current")
_CfprApEtherNiErrStatsCrcDelta_Type = Counter64
_CfprApEtherNiErrStatsCrcDelta_Object = MibTableColumn
cfprApEtherNiErrStatsCrcDelta = _CfprApEtherNiErrStatsCrcDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 5),
    _CfprApEtherNiErrStatsCrcDelta_Type()
)
cfprApEtherNiErrStatsCrcDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsCrcDelta.setStatus("current")
_CfprApEtherNiErrStatsCrcDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsCrcDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsCrcDeltaAvg = _CfprApEtherNiErrStatsCrcDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 6),
    _CfprApEtherNiErrStatsCrcDeltaAvg_Type()
)
cfprApEtherNiErrStatsCrcDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsCrcDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsCrcDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsCrcDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsCrcDeltaMax = _CfprApEtherNiErrStatsCrcDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 7),
    _CfprApEtherNiErrStatsCrcDeltaMax_Type()
)
cfprApEtherNiErrStatsCrcDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsCrcDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsCrcDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsCrcDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsCrcDeltaMin = _CfprApEtherNiErrStatsCrcDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 8),
    _CfprApEtherNiErrStatsCrcDeltaMin_Type()
)
cfprApEtherNiErrStatsCrcDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsCrcDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsFrameTx_Type = Unsigned64
_CfprApEtherNiErrStatsFrameTx_Object = MibTableColumn
cfprApEtherNiErrStatsFrameTx = _CfprApEtherNiErrStatsFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 9),
    _CfprApEtherNiErrStatsFrameTx_Type()
)
cfprApEtherNiErrStatsFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsFrameTx.setStatus("current")
_CfprApEtherNiErrStatsFrameTxDelta_Type = Counter64
_CfprApEtherNiErrStatsFrameTxDelta_Object = MibTableColumn
cfprApEtherNiErrStatsFrameTxDelta = _CfprApEtherNiErrStatsFrameTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 10),
    _CfprApEtherNiErrStatsFrameTxDelta_Type()
)
cfprApEtherNiErrStatsFrameTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsFrameTxDelta.setStatus("current")
_CfprApEtherNiErrStatsFrameTxDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsFrameTxDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsFrameTxDeltaAvg = _CfprApEtherNiErrStatsFrameTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 11),
    _CfprApEtherNiErrStatsFrameTxDeltaAvg_Type()
)
cfprApEtherNiErrStatsFrameTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsFrameTxDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsFrameTxDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsFrameTxDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsFrameTxDeltaMax = _CfprApEtherNiErrStatsFrameTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 12),
    _CfprApEtherNiErrStatsFrameTxDeltaMax_Type()
)
cfprApEtherNiErrStatsFrameTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsFrameTxDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsFrameTxDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsFrameTxDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsFrameTxDeltaMin = _CfprApEtherNiErrStatsFrameTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 13),
    _CfprApEtherNiErrStatsFrameTxDeltaMin_Type()
)
cfprApEtherNiErrStatsFrameTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsFrameTxDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsInRange_Type = Unsigned64
_CfprApEtherNiErrStatsInRange_Object = MibTableColumn
cfprApEtherNiErrStatsInRange = _CfprApEtherNiErrStatsInRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 14),
    _CfprApEtherNiErrStatsInRange_Type()
)
cfprApEtherNiErrStatsInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsInRange.setStatus("current")
_CfprApEtherNiErrStatsInRangeDelta_Type = Counter64
_CfprApEtherNiErrStatsInRangeDelta_Object = MibTableColumn
cfprApEtherNiErrStatsInRangeDelta = _CfprApEtherNiErrStatsInRangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 15),
    _CfprApEtherNiErrStatsInRangeDelta_Type()
)
cfprApEtherNiErrStatsInRangeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsInRangeDelta.setStatus("current")
_CfprApEtherNiErrStatsInRangeDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsInRangeDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsInRangeDeltaAvg = _CfprApEtherNiErrStatsInRangeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 16),
    _CfprApEtherNiErrStatsInRangeDeltaAvg_Type()
)
cfprApEtherNiErrStatsInRangeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsInRangeDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsInRangeDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsInRangeDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsInRangeDeltaMax = _CfprApEtherNiErrStatsInRangeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 17),
    _CfprApEtherNiErrStatsInRangeDeltaMax_Type()
)
cfprApEtherNiErrStatsInRangeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsInRangeDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsInRangeDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsInRangeDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsInRangeDeltaMin = _CfprApEtherNiErrStatsInRangeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 18),
    _CfprApEtherNiErrStatsInRangeDeltaMin_Type()
)
cfprApEtherNiErrStatsInRangeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsInRangeDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsIntervals_Type = Gauge32
_CfprApEtherNiErrStatsIntervals_Object = MibTableColumn
cfprApEtherNiErrStatsIntervals = _CfprApEtherNiErrStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 19),
    _CfprApEtherNiErrStatsIntervals_Type()
)
cfprApEtherNiErrStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsIntervals.setStatus("current")
_CfprApEtherNiErrStatsSuspect_Type = TruthValue
_CfprApEtherNiErrStatsSuspect_Object = MibTableColumn
cfprApEtherNiErrStatsSuspect = _CfprApEtherNiErrStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 20),
    _CfprApEtherNiErrStatsSuspect_Type()
)
cfprApEtherNiErrStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsSuspect.setStatus("current")
_CfprApEtherNiErrStatsThresholded_Type = CfprApEtherNiErrStatsThresholded
_CfprApEtherNiErrStatsThresholded_Object = MibTableColumn
cfprApEtherNiErrStatsThresholded = _CfprApEtherNiErrStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 21),
    _CfprApEtherNiErrStatsThresholded_Type()
)
cfprApEtherNiErrStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsThresholded.setStatus("current")
_CfprApEtherNiErrStatsTimeCollected_Type = DateAndTime
_CfprApEtherNiErrStatsTimeCollected_Object = MibTableColumn
cfprApEtherNiErrStatsTimeCollected = _CfprApEtherNiErrStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 22),
    _CfprApEtherNiErrStatsTimeCollected_Type()
)
cfprApEtherNiErrStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTimeCollected.setStatus("current")
_CfprApEtherNiErrStatsTooLong_Type = Unsigned64
_CfprApEtherNiErrStatsTooLong_Object = MibTableColumn
cfprApEtherNiErrStatsTooLong = _CfprApEtherNiErrStatsTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 23),
    _CfprApEtherNiErrStatsTooLong_Type()
)
cfprApEtherNiErrStatsTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooLong.setStatus("current")
_CfprApEtherNiErrStatsTooLongDelta_Type = Counter64
_CfprApEtherNiErrStatsTooLongDelta_Object = MibTableColumn
cfprApEtherNiErrStatsTooLongDelta = _CfprApEtherNiErrStatsTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 24),
    _CfprApEtherNiErrStatsTooLongDelta_Type()
)
cfprApEtherNiErrStatsTooLongDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooLongDelta.setStatus("current")
_CfprApEtherNiErrStatsTooLongDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsTooLongDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsTooLongDeltaAvg = _CfprApEtherNiErrStatsTooLongDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 25),
    _CfprApEtherNiErrStatsTooLongDeltaAvg_Type()
)
cfprApEtherNiErrStatsTooLongDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooLongDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsTooLongDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsTooLongDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsTooLongDeltaMax = _CfprApEtherNiErrStatsTooLongDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 26),
    _CfprApEtherNiErrStatsTooLongDeltaMax_Type()
)
cfprApEtherNiErrStatsTooLongDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooLongDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsTooLongDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsTooLongDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsTooLongDeltaMin = _CfprApEtherNiErrStatsTooLongDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 27),
    _CfprApEtherNiErrStatsTooLongDeltaMin_Type()
)
cfprApEtherNiErrStatsTooLongDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooLongDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsTooShort_Type = Unsigned64
_CfprApEtherNiErrStatsTooShort_Object = MibTableColumn
cfprApEtherNiErrStatsTooShort = _CfprApEtherNiErrStatsTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 28),
    _CfprApEtherNiErrStatsTooShort_Type()
)
cfprApEtherNiErrStatsTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooShort.setStatus("current")
_CfprApEtherNiErrStatsTooShortDelta_Type = Counter64
_CfprApEtherNiErrStatsTooShortDelta_Object = MibTableColumn
cfprApEtherNiErrStatsTooShortDelta = _CfprApEtherNiErrStatsTooShortDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 29),
    _CfprApEtherNiErrStatsTooShortDelta_Type()
)
cfprApEtherNiErrStatsTooShortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooShortDelta.setStatus("current")
_CfprApEtherNiErrStatsTooShortDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsTooShortDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsTooShortDeltaAvg = _CfprApEtherNiErrStatsTooShortDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 30),
    _CfprApEtherNiErrStatsTooShortDeltaAvg_Type()
)
cfprApEtherNiErrStatsTooShortDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooShortDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsTooShortDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsTooShortDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsTooShortDeltaMax = _CfprApEtherNiErrStatsTooShortDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 31),
    _CfprApEtherNiErrStatsTooShortDeltaMax_Type()
)
cfprApEtherNiErrStatsTooShortDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooShortDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsTooShortDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsTooShortDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsTooShortDeltaMin = _CfprApEtherNiErrStatsTooShortDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 32),
    _CfprApEtherNiErrStatsTooShortDeltaMin_Type()
)
cfprApEtherNiErrStatsTooShortDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsTooShortDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsUpdate_Type = Gauge32
_CfprApEtherNiErrStatsUpdate_Object = MibTableColumn
cfprApEtherNiErrStatsUpdate = _CfprApEtherNiErrStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 12, 1, 33),
    _CfprApEtherNiErrStatsUpdate_Type()
)
cfprApEtherNiErrStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsUpdate.setStatus("current")
_CfprApEtherNiErrStatsHistTable_Object = MibTable
cfprApEtherNiErrStatsHistTable = _CfprApEtherNiErrStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13)
)
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTable.setStatus("current")
_CfprApEtherNiErrStatsHistEntry_Object = MibTableRow
cfprApEtherNiErrStatsHistEntry = _CfprApEtherNiErrStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1)
)
cfprApEtherNiErrStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherNiErrStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistEntry.setStatus("current")
_CfprApEtherNiErrStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherNiErrStatsHistInstanceId_Object = MibTableColumn
cfprApEtherNiErrStatsHistInstanceId = _CfprApEtherNiErrStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 1),
    _CfprApEtherNiErrStatsHistInstanceId_Type()
)
cfprApEtherNiErrStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistInstanceId.setStatus("current")
_CfprApEtherNiErrStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherNiErrStatsHistDn_Object = MibTableColumn
cfprApEtherNiErrStatsHistDn = _CfprApEtherNiErrStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 2),
    _CfprApEtherNiErrStatsHistDn_Type()
)
cfprApEtherNiErrStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistDn.setStatus("current")
_CfprApEtherNiErrStatsHistRn_Type = SnmpAdminString
_CfprApEtherNiErrStatsHistRn_Object = MibTableColumn
cfprApEtherNiErrStatsHistRn = _CfprApEtherNiErrStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 3),
    _CfprApEtherNiErrStatsHistRn_Type()
)
cfprApEtherNiErrStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistRn.setStatus("current")
_CfprApEtherNiErrStatsHistCrc_Type = Unsigned64
_CfprApEtherNiErrStatsHistCrc_Object = MibTableColumn
cfprApEtherNiErrStatsHistCrc = _CfprApEtherNiErrStatsHistCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 4),
    _CfprApEtherNiErrStatsHistCrc_Type()
)
cfprApEtherNiErrStatsHistCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistCrc.setStatus("current")
_CfprApEtherNiErrStatsHistCrcDelta_Type = Unsigned64
_CfprApEtherNiErrStatsHistCrcDelta_Object = MibTableColumn
cfprApEtherNiErrStatsHistCrcDelta = _CfprApEtherNiErrStatsHistCrcDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 5),
    _CfprApEtherNiErrStatsHistCrcDelta_Type()
)
cfprApEtherNiErrStatsHistCrcDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistCrcDelta.setStatus("current")
_CfprApEtherNiErrStatsHistCrcDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsHistCrcDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsHistCrcDeltaAvg = _CfprApEtherNiErrStatsHistCrcDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 6),
    _CfprApEtherNiErrStatsHistCrcDeltaAvg_Type()
)
cfprApEtherNiErrStatsHistCrcDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistCrcDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsHistCrcDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsHistCrcDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsHistCrcDeltaMax = _CfprApEtherNiErrStatsHistCrcDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 7),
    _CfprApEtherNiErrStatsHistCrcDeltaMax_Type()
)
cfprApEtherNiErrStatsHistCrcDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistCrcDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsHistCrcDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsHistCrcDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsHistCrcDeltaMin = _CfprApEtherNiErrStatsHistCrcDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 8),
    _CfprApEtherNiErrStatsHistCrcDeltaMin_Type()
)
cfprApEtherNiErrStatsHistCrcDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistCrcDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsHistFrameTx_Type = Unsigned64
_CfprApEtherNiErrStatsHistFrameTx_Object = MibTableColumn
cfprApEtherNiErrStatsHistFrameTx = _CfprApEtherNiErrStatsHistFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 9),
    _CfprApEtherNiErrStatsHistFrameTx_Type()
)
cfprApEtherNiErrStatsHistFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistFrameTx.setStatus("current")
_CfprApEtherNiErrStatsHistFrameTxDelta_Type = Unsigned64
_CfprApEtherNiErrStatsHistFrameTxDelta_Object = MibTableColumn
cfprApEtherNiErrStatsHistFrameTxDelta = _CfprApEtherNiErrStatsHistFrameTxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 10),
    _CfprApEtherNiErrStatsHistFrameTxDelta_Type()
)
cfprApEtherNiErrStatsHistFrameTxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistFrameTxDelta.setStatus("current")
_CfprApEtherNiErrStatsHistFrameTxDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsHistFrameTxDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsHistFrameTxDeltaAvg = _CfprApEtherNiErrStatsHistFrameTxDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 11),
    _CfprApEtherNiErrStatsHistFrameTxDeltaAvg_Type()
)
cfprApEtherNiErrStatsHistFrameTxDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistFrameTxDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsHistFrameTxDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsHistFrameTxDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsHistFrameTxDeltaMax = _CfprApEtherNiErrStatsHistFrameTxDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 12),
    _CfprApEtherNiErrStatsHistFrameTxDeltaMax_Type()
)
cfprApEtherNiErrStatsHistFrameTxDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistFrameTxDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsHistFrameTxDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsHistFrameTxDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsHistFrameTxDeltaMin = _CfprApEtherNiErrStatsHistFrameTxDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 13),
    _CfprApEtherNiErrStatsHistFrameTxDeltaMin_Type()
)
cfprApEtherNiErrStatsHistFrameTxDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistFrameTxDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsHistId_Type = Unsigned64
_CfprApEtherNiErrStatsHistId_Object = MibTableColumn
cfprApEtherNiErrStatsHistId = _CfprApEtherNiErrStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 14),
    _CfprApEtherNiErrStatsHistId_Type()
)
cfprApEtherNiErrStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistId.setStatus("current")
_CfprApEtherNiErrStatsHistInRange_Type = Unsigned64
_CfprApEtherNiErrStatsHistInRange_Object = MibTableColumn
cfprApEtherNiErrStatsHistInRange = _CfprApEtherNiErrStatsHistInRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 15),
    _CfprApEtherNiErrStatsHistInRange_Type()
)
cfprApEtherNiErrStatsHistInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistInRange.setStatus("current")
_CfprApEtherNiErrStatsHistInRangeDelta_Type = Unsigned64
_CfprApEtherNiErrStatsHistInRangeDelta_Object = MibTableColumn
cfprApEtherNiErrStatsHistInRangeDelta = _CfprApEtherNiErrStatsHistInRangeDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 16),
    _CfprApEtherNiErrStatsHistInRangeDelta_Type()
)
cfprApEtherNiErrStatsHistInRangeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistInRangeDelta.setStatus("current")
_CfprApEtherNiErrStatsHistInRangeDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsHistInRangeDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsHistInRangeDeltaAvg = _CfprApEtherNiErrStatsHistInRangeDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 17),
    _CfprApEtherNiErrStatsHistInRangeDeltaAvg_Type()
)
cfprApEtherNiErrStatsHistInRangeDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistInRangeDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsHistInRangeDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsHistInRangeDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsHistInRangeDeltaMax = _CfprApEtherNiErrStatsHistInRangeDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 18),
    _CfprApEtherNiErrStatsHistInRangeDeltaMax_Type()
)
cfprApEtherNiErrStatsHistInRangeDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistInRangeDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsHistInRangeDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsHistInRangeDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsHistInRangeDeltaMin = _CfprApEtherNiErrStatsHistInRangeDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 19),
    _CfprApEtherNiErrStatsHistInRangeDeltaMin_Type()
)
cfprApEtherNiErrStatsHistInRangeDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistInRangeDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsHistMostRecent_Type = TruthValue
_CfprApEtherNiErrStatsHistMostRecent_Object = MibTableColumn
cfprApEtherNiErrStatsHistMostRecent = _CfprApEtherNiErrStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 20),
    _CfprApEtherNiErrStatsHistMostRecent_Type()
)
cfprApEtherNiErrStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistMostRecent.setStatus("current")
_CfprApEtherNiErrStatsHistSuspect_Type = TruthValue
_CfprApEtherNiErrStatsHistSuspect_Object = MibTableColumn
cfprApEtherNiErrStatsHistSuspect = _CfprApEtherNiErrStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 21),
    _CfprApEtherNiErrStatsHistSuspect_Type()
)
cfprApEtherNiErrStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistSuspect.setStatus("current")
_CfprApEtherNiErrStatsHistThresholded_Type = CfprApEtherNiErrStatsHistThresholded
_CfprApEtherNiErrStatsHistThresholded_Object = MibTableColumn
cfprApEtherNiErrStatsHistThresholded = _CfprApEtherNiErrStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 22),
    _CfprApEtherNiErrStatsHistThresholded_Type()
)
cfprApEtherNiErrStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistThresholded.setStatus("current")
_CfprApEtherNiErrStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherNiErrStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherNiErrStatsHistTimeCollected = _CfprApEtherNiErrStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 23),
    _CfprApEtherNiErrStatsHistTimeCollected_Type()
)
cfprApEtherNiErrStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTimeCollected.setStatus("current")
_CfprApEtherNiErrStatsHistTooLong_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooLong_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooLong = _CfprApEtherNiErrStatsHistTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 24),
    _CfprApEtherNiErrStatsHistTooLong_Type()
)
cfprApEtherNiErrStatsHistTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooLong.setStatus("current")
_CfprApEtherNiErrStatsHistTooLongDelta_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooLongDelta_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooLongDelta = _CfprApEtherNiErrStatsHistTooLongDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 25),
    _CfprApEtherNiErrStatsHistTooLongDelta_Type()
)
cfprApEtherNiErrStatsHistTooLongDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooLongDelta.setStatus("current")
_CfprApEtherNiErrStatsHistTooLongDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooLongDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooLongDeltaAvg = _CfprApEtherNiErrStatsHistTooLongDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 26),
    _CfprApEtherNiErrStatsHistTooLongDeltaAvg_Type()
)
cfprApEtherNiErrStatsHistTooLongDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooLongDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsHistTooLongDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooLongDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooLongDeltaMax = _CfprApEtherNiErrStatsHistTooLongDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 27),
    _CfprApEtherNiErrStatsHistTooLongDeltaMax_Type()
)
cfprApEtherNiErrStatsHistTooLongDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooLongDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsHistTooLongDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooLongDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooLongDeltaMin = _CfprApEtherNiErrStatsHistTooLongDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 28),
    _CfprApEtherNiErrStatsHistTooLongDeltaMin_Type()
)
cfprApEtherNiErrStatsHistTooLongDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooLongDeltaMin.setStatus("current")
_CfprApEtherNiErrStatsHistTooShort_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooShort_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooShort = _CfprApEtherNiErrStatsHistTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 29),
    _CfprApEtherNiErrStatsHistTooShort_Type()
)
cfprApEtherNiErrStatsHistTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooShort.setStatus("current")
_CfprApEtherNiErrStatsHistTooShortDelta_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooShortDelta_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooShortDelta = _CfprApEtherNiErrStatsHistTooShortDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 30),
    _CfprApEtherNiErrStatsHistTooShortDelta_Type()
)
cfprApEtherNiErrStatsHistTooShortDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooShortDelta.setStatus("current")
_CfprApEtherNiErrStatsHistTooShortDeltaAvg_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooShortDeltaAvg_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooShortDeltaAvg = _CfprApEtherNiErrStatsHistTooShortDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 31),
    _CfprApEtherNiErrStatsHistTooShortDeltaAvg_Type()
)
cfprApEtherNiErrStatsHistTooShortDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooShortDeltaAvg.setStatus("current")
_CfprApEtherNiErrStatsHistTooShortDeltaMax_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooShortDeltaMax_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooShortDeltaMax = _CfprApEtherNiErrStatsHistTooShortDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 32),
    _CfprApEtherNiErrStatsHistTooShortDeltaMax_Type()
)
cfprApEtherNiErrStatsHistTooShortDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooShortDeltaMax.setStatus("current")
_CfprApEtherNiErrStatsHistTooShortDeltaMin_Type = Unsigned64
_CfprApEtherNiErrStatsHistTooShortDeltaMin_Object = MibTableColumn
cfprApEtherNiErrStatsHistTooShortDeltaMin = _CfprApEtherNiErrStatsHistTooShortDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 13, 1, 33),
    _CfprApEtherNiErrStatsHistTooShortDeltaMin_Type()
)
cfprApEtherNiErrStatsHistTooShortDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNiErrStatsHistTooShortDeltaMin.setStatus("current")
_CfprApEtherNicIfConfigTable_Object = MibTable
cfprApEtherNicIfConfigTable = _CfprApEtherNicIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 14)
)
if mibBuilder.loadTexts:
    cfprApEtherNicIfConfigTable.setStatus("current")
_CfprApEtherNicIfConfigEntry_Object = MibTableRow
cfprApEtherNicIfConfigEntry = _CfprApEtherNicIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 14, 1)
)
cfprApEtherNicIfConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherNicIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherNicIfConfigEntry.setStatus("current")
_CfprApEtherNicIfConfigInstanceId_Type = CfprApManagedObjectId
_CfprApEtherNicIfConfigInstanceId_Object = MibTableColumn
cfprApEtherNicIfConfigInstanceId = _CfprApEtherNicIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 14, 1, 1),
    _CfprApEtherNicIfConfigInstanceId_Type()
)
cfprApEtherNicIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherNicIfConfigInstanceId.setStatus("current")
_CfprApEtherNicIfConfigDn_Type = CfprApManagedObjectDn
_CfprApEtherNicIfConfigDn_Object = MibTableColumn
cfprApEtherNicIfConfigDn = _CfprApEtherNicIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 14, 1, 2),
    _CfprApEtherNicIfConfigDn_Type()
)
cfprApEtherNicIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNicIfConfigDn.setStatus("current")
_CfprApEtherNicIfConfigRn_Type = SnmpAdminString
_CfprApEtherNicIfConfigRn_Object = MibTableColumn
cfprApEtherNicIfConfigRn = _CfprApEtherNicIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 14, 1, 3),
    _CfprApEtherNicIfConfigRn_Type()
)
cfprApEtherNicIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherNicIfConfigRn.setStatus("current")
_CfprApEtherPIoTable_Object = MibTable
cfprApEtherPIoTable = _CfprApEtherPIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15)
)
if mibBuilder.loadTexts:
    cfprApEtherPIoTable.setStatus("current")
_CfprApEtherPIoEntry_Object = MibTableRow
cfprApEtherPIoEntry = _CfprApEtherPIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1)
)
cfprApEtherPIoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPIoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPIoEntry.setStatus("current")
_CfprApEtherPIoInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPIoInstanceId_Object = MibTableColumn
cfprApEtherPIoInstanceId = _CfprApEtherPIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 1),
    _CfprApEtherPIoInstanceId_Type()
)
cfprApEtherPIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPIoInstanceId.setStatus("current")
_CfprApEtherPIoDn_Type = CfprApManagedObjectDn
_CfprApEtherPIoDn_Object = MibTableColumn
cfprApEtherPIoDn = _CfprApEtherPIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 2),
    _CfprApEtherPIoDn_Type()
)
cfprApEtherPIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoDn.setStatus("current")
_CfprApEtherPIoRn_Type = SnmpAdminString
_CfprApEtherPIoRn_Object = MibTableColumn
cfprApEtherPIoRn = _CfprApEtherPIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 3),
    _CfprApEtherPIoRn_Type()
)
cfprApEtherPIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoRn.setStatus("current")
_CfprApEtherPIoAdminState_Type = CfprApFabricAdminState
_CfprApEtherPIoAdminState_Object = MibTableColumn
cfprApEtherPIoAdminState = _CfprApEtherPIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 4),
    _CfprApEtherPIoAdminState_Type()
)
cfprApEtherPIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoAdminState.setStatus("current")
_CfprApEtherPIoAdminTransport_Type = CfprApNetworkTransport
_CfprApEtherPIoAdminTransport_Object = MibTableColumn
cfprApEtherPIoAdminTransport = _CfprApEtherPIoAdminTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 5),
    _CfprApEtherPIoAdminTransport_Type()
)
cfprApEtherPIoAdminTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoAdminTransport.setStatus("current")
_CfprApEtherPIoAggrPortId_Type = Gauge32
_CfprApEtherPIoAggrPortId_Object = MibTableColumn
cfprApEtherPIoAggrPortId = _CfprApEtherPIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 6),
    _CfprApEtherPIoAggrPortId_Type()
)
cfprApEtherPIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoAggrPortId.setStatus("current")
_CfprApEtherPIoChassisId_Type = Gauge32
_CfprApEtherPIoChassisId_Object = MibTableColumn
cfprApEtherPIoChassisId = _CfprApEtherPIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 7),
    _CfprApEtherPIoChassisId_Type()
)
cfprApEtherPIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoChassisId.setStatus("current")
_CfprApEtherPIoEncap_Type = CfprApPortEncap
_CfprApEtherPIoEncap_Object = MibTableColumn
cfprApEtherPIoEncap = _CfprApEtherPIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 8),
    _CfprApEtherPIoEncap_Type()
)
cfprApEtherPIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEncap.setStatus("current")
_CfprApEtherPIoEpDn_Type = SnmpAdminString
_CfprApEtherPIoEpDn_Object = MibTableColumn
cfprApEtherPIoEpDn = _CfprApEtherPIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 9),
    _CfprApEtherPIoEpDn_Type()
)
cfprApEtherPIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEpDn.setStatus("current")
_CfprApEtherPIoFltAggr_Type = Unsigned64
_CfprApEtherPIoFltAggr_Object = MibTableColumn
cfprApEtherPIoFltAggr = _CfprApEtherPIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 10),
    _CfprApEtherPIoFltAggr_Type()
)
cfprApEtherPIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFltAggr.setStatus("current")
_CfprApEtherPIoFsmDescr_Type = SnmpAdminString
_CfprApEtherPIoFsmDescr_Object = MibTableColumn
cfprApEtherPIoFsmDescr = _CfprApEtherPIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 11),
    _CfprApEtherPIoFsmDescr_Type()
)
cfprApEtherPIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmDescr.setStatus("current")
_CfprApEtherPIoFsmPrev_Type = SnmpAdminString
_CfprApEtherPIoFsmPrev_Object = MibTableColumn
cfprApEtherPIoFsmPrev = _CfprApEtherPIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 12),
    _CfprApEtherPIoFsmPrev_Type()
)
cfprApEtherPIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmPrev.setStatus("current")
_CfprApEtherPIoFsmProgr_Type = Gauge32
_CfprApEtherPIoFsmProgr_Object = MibTableColumn
cfprApEtherPIoFsmProgr = _CfprApEtherPIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 13),
    _CfprApEtherPIoFsmProgr_Type()
)
cfprApEtherPIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmProgr.setStatus("current")
_CfprApEtherPIoFsmRmtInvErrCode_Type = Gauge32
_CfprApEtherPIoFsmRmtInvErrCode_Object = MibTableColumn
cfprApEtherPIoFsmRmtInvErrCode = _CfprApEtherPIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 14),
    _CfprApEtherPIoFsmRmtInvErrCode_Type()
)
cfprApEtherPIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRmtInvErrCode.setStatus("current")
_CfprApEtherPIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApEtherPIoFsmRmtInvErrDescr_Object = MibTableColumn
cfprApEtherPIoFsmRmtInvErrDescr = _CfprApEtherPIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 15),
    _CfprApEtherPIoFsmRmtInvErrDescr_Type()
)
cfprApEtherPIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRmtInvErrDescr.setStatus("current")
_CfprApEtherPIoFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEtherPIoFsmRmtInvRslt_Object = MibTableColumn
cfprApEtherPIoFsmRmtInvRslt = _CfprApEtherPIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 16),
    _CfprApEtherPIoFsmRmtInvRslt_Type()
)
cfprApEtherPIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRmtInvRslt.setStatus("current")
_CfprApEtherPIoFsmStageDescr_Type = SnmpAdminString
_CfprApEtherPIoFsmStageDescr_Object = MibTableColumn
cfprApEtherPIoFsmStageDescr = _CfprApEtherPIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 17),
    _CfprApEtherPIoFsmStageDescr_Type()
)
cfprApEtherPIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageDescr.setStatus("current")
_CfprApEtherPIoFsmStamp_Type = DateAndTime
_CfprApEtherPIoFsmStamp_Object = MibTableColumn
cfprApEtherPIoFsmStamp = _CfprApEtherPIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 18),
    _CfprApEtherPIoFsmStamp_Type()
)
cfprApEtherPIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStamp.setStatus("current")
_CfprApEtherPIoFsmStatus_Type = SnmpAdminString
_CfprApEtherPIoFsmStatus_Object = MibTableColumn
cfprApEtherPIoFsmStatus = _CfprApEtherPIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 19),
    _CfprApEtherPIoFsmStatus_Type()
)
cfprApEtherPIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStatus.setStatus("current")
_CfprApEtherPIoFsmTry_Type = Gauge32
_CfprApEtherPIoFsmTry_Object = MibTableColumn
cfprApEtherPIoFsmTry = _CfprApEtherPIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 20),
    _CfprApEtherPIoFsmTry_Type()
)
cfprApEtherPIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmTry.setStatus("current")
_CfprApEtherPIoFtwPhyDn_Type = SnmpAdminString
_CfprApEtherPIoFtwPhyDn_Object = MibTableColumn
cfprApEtherPIoFtwPhyDn = _CfprApEtherPIoFtwPhyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 21),
    _CfprApEtherPIoFtwPhyDn_Type()
)
cfprApEtherPIoFtwPhyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFtwPhyDn.setStatus("current")
_CfprApEtherPIoIfRole_Type = CfprApNetworkPortRole
_CfprApEtherPIoIfRole_Object = MibTableColumn
cfprApEtherPIoIfRole = _CfprApEtherPIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 22),
    _CfprApEtherPIoIfRole_Type()
)
cfprApEtherPIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoIfRole.setStatus("current")
_CfprApEtherPIoIfType_Type = CfprApNetworkPhysEpIfType
_CfprApEtherPIoIfType_Object = MibTableColumn
cfprApEtherPIoIfType = _CfprApEtherPIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 23),
    _CfprApEtherPIoIfType_Type()
)
cfprApEtherPIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoIfType.setStatus("current")
_CfprApEtherPIoIsPortChannelMember_Type = TruthValue
_CfprApEtherPIoIsPortChannelMember_Object = MibTableColumn
cfprApEtherPIoIsPortChannelMember = _CfprApEtherPIoIsPortChannelMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 24),
    _CfprApEtherPIoIsPortChannelMember_Type()
)
cfprApEtherPIoIsPortChannelMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoIsPortChannelMember.setStatus("current")
_CfprApEtherPIoLc_Type = CfprApFsmLifecycle
_CfprApEtherPIoLc_Object = MibTableColumn
cfprApEtherPIoLc = _CfprApEtherPIoLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 25),
    _CfprApEtherPIoLc_Type()
)
cfprApEtherPIoLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoLc.setStatus("current")
_CfprApEtherPIoLicGP_Type = Unsigned64
_CfprApEtherPIoLicGP_Object = MibTableColumn
cfprApEtherPIoLicGP = _CfprApEtherPIoLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 26),
    _CfprApEtherPIoLicGP_Type()
)
cfprApEtherPIoLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoLicGP.setStatus("current")
_CfprApEtherPIoLicState_Type = CfprApLicenseState
_CfprApEtherPIoLicState_Object = MibTableColumn
cfprApEtherPIoLicState = _CfprApEtherPIoLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 27),
    _CfprApEtherPIoLicState_Type()
)
cfprApEtherPIoLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoLicState.setStatus("current")
_CfprApEtherPIoLocale_Type = CfprApNetworkLocale
_CfprApEtherPIoLocale_Object = MibTableColumn
cfprApEtherPIoLocale = _CfprApEtherPIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 28),
    _CfprApEtherPIoLocale_Type()
)
cfprApEtherPIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoLocale.setStatus("current")
_CfprApEtherPIoMac_Type = MacAddress
_CfprApEtherPIoMac_Object = MibTableColumn
cfprApEtherPIoMac = _CfprApEtherPIoMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 29),
    _CfprApEtherPIoMac_Type()
)
cfprApEtherPIoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoMac.setStatus("current")
_CfprApEtherPIoMode_Type = CfprApPortMode
_CfprApEtherPIoMode_Object = MibTableColumn
cfprApEtherPIoMode = _CfprApEtherPIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 30),
    _CfprApEtherPIoMode_Type()
)
cfprApEtherPIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoMode.setStatus("current")
_CfprApEtherPIoModel_Type = SnmpAdminString
_CfprApEtherPIoModel_Object = MibTableColumn
cfprApEtherPIoModel = _CfprApEtherPIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 31),
    _CfprApEtherPIoModel_Type()
)
cfprApEtherPIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoModel.setStatus("current")
_CfprApEtherPIoName_Type = SnmpAdminString
_CfprApEtherPIoName_Object = MibTableColumn
cfprApEtherPIoName = _CfprApEtherPIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 32),
    _CfprApEtherPIoName_Type()
)
cfprApEtherPIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoName.setStatus("current")
_CfprApEtherPIoOperDuplex_Type = CfprApPortDuplex
_CfprApEtherPIoOperDuplex_Object = MibTableColumn
cfprApEtherPIoOperDuplex = _CfprApEtherPIoOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 33),
    _CfprApEtherPIoOperDuplex_Type()
)
cfprApEtherPIoOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoOperDuplex.setStatus("current")
_CfprApEtherPIoOperSpeed_Type = CfprApPortEthSpeed
_CfprApEtherPIoOperSpeed_Object = MibTableColumn
cfprApEtherPIoOperSpeed = _CfprApEtherPIoOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 34),
    _CfprApEtherPIoOperSpeed_Type()
)
cfprApEtherPIoOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoOperSpeed.setStatus("current")
_CfprApEtherPIoOperState_Type = CfprApNetworkPortOperState
_CfprApEtherPIoOperState_Object = MibTableColumn
cfprApEtherPIoOperState = _CfprApEtherPIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 35),
    _CfprApEtherPIoOperState_Type()
)
cfprApEtherPIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoOperState.setStatus("current")
_CfprApEtherPIoPeerAggrPortId_Type = Gauge32
_CfprApEtherPIoPeerAggrPortId_Object = MibTableColumn
cfprApEtherPIoPeerAggrPortId = _CfprApEtherPIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 36),
    _CfprApEtherPIoPeerAggrPortId_Type()
)
cfprApEtherPIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoPeerAggrPortId.setStatus("current")
_CfprApEtherPIoPeerChassisId_Type = Gauge32
_CfprApEtherPIoPeerChassisId_Object = MibTableColumn
cfprApEtherPIoPeerChassisId = _CfprApEtherPIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 37),
    _CfprApEtherPIoPeerChassisId_Type()
)
cfprApEtherPIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoPeerChassisId.setStatus("current")
_CfprApEtherPIoPeerDn_Type = SnmpAdminString
_CfprApEtherPIoPeerDn_Object = MibTableColumn
cfprApEtherPIoPeerDn = _CfprApEtherPIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 38),
    _CfprApEtherPIoPeerDn_Type()
)
cfprApEtherPIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoPeerDn.setStatus("current")
_CfprApEtherPIoPeerPortId_Type = Gauge32
_CfprApEtherPIoPeerPortId_Object = MibTableColumn
cfprApEtherPIoPeerPortId = _CfprApEtherPIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 39),
    _CfprApEtherPIoPeerPortId_Type()
)
cfprApEtherPIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoPeerPortId.setStatus("current")
_CfprApEtherPIoPeerSlotId_Type = Gauge32
_CfprApEtherPIoPeerSlotId_Object = MibTableColumn
cfprApEtherPIoPeerSlotId = _CfprApEtherPIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 40),
    _CfprApEtherPIoPeerSlotId_Type()
)
cfprApEtherPIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoPeerSlotId.setStatus("current")
_CfprApEtherPIoPortId_Type = Gauge32
_CfprApEtherPIoPortId_Object = MibTableColumn
cfprApEtherPIoPortId = _CfprApEtherPIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 41),
    _CfprApEtherPIoPortId_Type()
)
cfprApEtherPIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoPortId.setStatus("current")
_CfprApEtherPIoRevision_Type = SnmpAdminString
_CfprApEtherPIoRevision_Object = MibTableColumn
cfprApEtherPIoRevision = _CfprApEtherPIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 42),
    _CfprApEtherPIoRevision_Type()
)
cfprApEtherPIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoRevision.setStatus("current")
_CfprApEtherPIoSerial_Type = SnmpAdminString
_CfprApEtherPIoSerial_Object = MibTableColumn
cfprApEtherPIoSerial = _CfprApEtherPIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 43),
    _CfprApEtherPIoSerial_Type()
)
cfprApEtherPIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoSerial.setStatus("current")
_CfprApEtherPIoSlotId_Type = Gauge32
_CfprApEtherPIoSlotId_Object = MibTableColumn
cfprApEtherPIoSlotId = _CfprApEtherPIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 44),
    _CfprApEtherPIoSlotId_Type()
)
cfprApEtherPIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoSlotId.setStatus("current")
_CfprApEtherPIoStateQual_Type = SnmpAdminString
_CfprApEtherPIoStateQual_Object = MibTableColumn
cfprApEtherPIoStateQual = _CfprApEtherPIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 45),
    _CfprApEtherPIoStateQual_Type()
)
cfprApEtherPIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoStateQual.setStatus("current")
_CfprApEtherPIoSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherPIoSwitchId_Object = MibTableColumn
cfprApEtherPIoSwitchId = _CfprApEtherPIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 46),
    _CfprApEtherPIoSwitchId_Type()
)
cfprApEtherPIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoSwitchId.setStatus("current")
_CfprApEtherPIoTransport_Type = CfprApNetworkTransport
_CfprApEtherPIoTransport_Object = MibTableColumn
cfprApEtherPIoTransport = _CfprApEtherPIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 47),
    _CfprApEtherPIoTransport_Type()
)
cfprApEtherPIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoTransport.setStatus("current")
_CfprApEtherPIoTs_Type = DateAndTime
_CfprApEtherPIoTs_Object = MibTableColumn
cfprApEtherPIoTs = _CfprApEtherPIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 48),
    _CfprApEtherPIoTs_Type()
)
cfprApEtherPIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoTs.setStatus("current")
_CfprApEtherPIoType_Type = CfprApNetworkConnectionType
_CfprApEtherPIoType_Object = MibTableColumn
cfprApEtherPIoType = _CfprApEtherPIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 49),
    _CfprApEtherPIoType_Type()
)
cfprApEtherPIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoType.setStatus("current")
_CfprApEtherPIoUnifiedPort_Type = TruthValue
_CfprApEtherPIoUnifiedPort_Object = MibTableColumn
cfprApEtherPIoUnifiedPort = _CfprApEtherPIoUnifiedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 50),
    _CfprApEtherPIoUnifiedPort_Type()
)
cfprApEtherPIoUnifiedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoUnifiedPort.setStatus("current")
_CfprApEtherPIoUsrLbl_Type = SnmpAdminString
_CfprApEtherPIoUsrLbl_Object = MibTableColumn
cfprApEtherPIoUsrLbl = _CfprApEtherPIoUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 51),
    _CfprApEtherPIoUsrLbl_Type()
)
cfprApEtherPIoUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoUsrLbl.setStatus("current")
_CfprApEtherPIoVendor_Type = SnmpAdminString
_CfprApEtherPIoVendor_Object = MibTableColumn
cfprApEtherPIoVendor = _CfprApEtherPIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 52),
    _CfprApEtherPIoVendor_Type()
)
cfprApEtherPIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoVendor.setStatus("current")
_CfprApEtherPIoXcvrType_Type = CfprApEquipmentXcvrType
_CfprApEtherPIoXcvrType_Object = MibTableColumn
cfprApEtherPIoXcvrType = _CfprApEtherPIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 15, 1, 53),
    _CfprApEtherPIoXcvrType_Type()
)
cfprApEtherPIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoXcvrType.setStatus("current")
_CfprApEtherPIoEndPointTable_Object = MibTable
cfprApEtherPIoEndPointTable = _CfprApEtherPIoEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16)
)
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointTable.setStatus("current")
_CfprApEtherPIoEndPointEntry_Object = MibTableRow
cfprApEtherPIoEndPointEntry = _CfprApEtherPIoEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1)
)
cfprApEtherPIoEndPointEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPIoEndPointInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointEntry.setStatus("current")
_CfprApEtherPIoEndPointInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPIoEndPointInstanceId_Object = MibTableColumn
cfprApEtherPIoEndPointInstanceId = _CfprApEtherPIoEndPointInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1, 1),
    _CfprApEtherPIoEndPointInstanceId_Type()
)
cfprApEtherPIoEndPointInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointInstanceId.setStatus("current")
_CfprApEtherPIoEndPointDn_Type = CfprApManagedObjectDn
_CfprApEtherPIoEndPointDn_Object = MibTableColumn
cfprApEtherPIoEndPointDn = _CfprApEtherPIoEndPointDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1, 2),
    _CfprApEtherPIoEndPointDn_Type()
)
cfprApEtherPIoEndPointDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointDn.setStatus("current")
_CfprApEtherPIoEndPointRn_Type = SnmpAdminString
_CfprApEtherPIoEndPointRn_Object = MibTableColumn
cfprApEtherPIoEndPointRn = _CfprApEtherPIoEndPointRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1, 3),
    _CfprApEtherPIoEndPointRn_Type()
)
cfprApEtherPIoEndPointRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointRn.setStatus("current")
_CfprApEtherPIoEndPointEndPointDn_Type = SnmpAdminString
_CfprApEtherPIoEndPointEndPointDn_Object = MibTableColumn
cfprApEtherPIoEndPointEndPointDn = _CfprApEtherPIoEndPointEndPointDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1, 4),
    _CfprApEtherPIoEndPointEndPointDn_Type()
)
cfprApEtherPIoEndPointEndPointDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointEndPointDn.setStatus("current")
_CfprApEtherPIoEndPointEpCloudType_Type = CfprApEtherCloudType
_CfprApEtherPIoEndPointEpCloudType_Object = MibTableColumn
cfprApEtherPIoEndPointEpCloudType = _CfprApEtherPIoEndPointEpCloudType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1, 5),
    _CfprApEtherPIoEndPointEpCloudType_Type()
)
cfprApEtherPIoEndPointEpCloudType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointEpCloudType.setStatus("current")
_CfprApEtherPIoEndPointUsrLbl_Type = SnmpAdminString
_CfprApEtherPIoEndPointUsrLbl_Object = MibTableColumn
cfprApEtherPIoEndPointUsrLbl = _CfprApEtherPIoEndPointUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 16, 1, 6),
    _CfprApEtherPIoEndPointUsrLbl_Type()
)
cfprApEtherPIoEndPointUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoEndPointUsrLbl.setStatus("current")
_CfprApEtherPIoFsmTable_Object = MibTable
cfprApEtherPIoFsmTable = _CfprApEtherPIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17)
)
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmTable.setStatus("current")
_CfprApEtherPIoFsmEntry_Object = MibTableRow
cfprApEtherPIoFsmEntry = _CfprApEtherPIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1)
)
cfprApEtherPIoFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmEntry.setStatus("current")
_CfprApEtherPIoFsmInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPIoFsmInstanceId_Object = MibTableColumn
cfprApEtherPIoFsmInstanceId = _CfprApEtherPIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 1),
    _CfprApEtherPIoFsmInstanceId_Type()
)
cfprApEtherPIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmInstanceId.setStatus("current")
_CfprApEtherPIoFsmDn_Type = CfprApManagedObjectDn
_CfprApEtherPIoFsmDn_Object = MibTableColumn
cfprApEtherPIoFsmDn = _CfprApEtherPIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 2),
    _CfprApEtherPIoFsmDn_Type()
)
cfprApEtherPIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmDn.setStatus("current")
_CfprApEtherPIoFsmRn_Type = SnmpAdminString
_CfprApEtherPIoFsmRn_Object = MibTableColumn
cfprApEtherPIoFsmRn = _CfprApEtherPIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 3),
    _CfprApEtherPIoFsmRn_Type()
)
cfprApEtherPIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRn.setStatus("current")
_CfprApEtherPIoFsmCompletionTime_Type = DateAndTime
_CfprApEtherPIoFsmCompletionTime_Object = MibTableColumn
cfprApEtherPIoFsmCompletionTime = _CfprApEtherPIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 4),
    _CfprApEtherPIoFsmCompletionTime_Type()
)
cfprApEtherPIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmCompletionTime.setStatus("current")
_CfprApEtherPIoFsmCurrentFsm_Type = CfprApEtherPIoFsmCurrentFsm
_CfprApEtherPIoFsmCurrentFsm_Object = MibTableColumn
cfprApEtherPIoFsmCurrentFsm = _CfprApEtherPIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 5),
    _CfprApEtherPIoFsmCurrentFsm_Type()
)
cfprApEtherPIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmCurrentFsm.setStatus("current")
_CfprApEtherPIoFsmDescrData_Type = SnmpAdminString
_CfprApEtherPIoFsmDescrData_Object = MibTableColumn
cfprApEtherPIoFsmDescrData = _CfprApEtherPIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 6),
    _CfprApEtherPIoFsmDescrData_Type()
)
cfprApEtherPIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmDescrData.setStatus("current")
_CfprApEtherPIoFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApEtherPIoFsmFsmStatus_Object = MibTableColumn
cfprApEtherPIoFsmFsmStatus = _CfprApEtherPIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 7),
    _CfprApEtherPIoFsmFsmStatus_Type()
)
cfprApEtherPIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmFsmStatus.setStatus("current")
_CfprApEtherPIoFsmProgress_Type = Gauge32
_CfprApEtherPIoFsmProgress_Object = MibTableColumn
cfprApEtherPIoFsmProgress = _CfprApEtherPIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 8),
    _CfprApEtherPIoFsmProgress_Type()
)
cfprApEtherPIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmProgress.setStatus("current")
_CfprApEtherPIoFsmRmtErrCode_Type = Gauge32
_CfprApEtherPIoFsmRmtErrCode_Object = MibTableColumn
cfprApEtherPIoFsmRmtErrCode = _CfprApEtherPIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 9),
    _CfprApEtherPIoFsmRmtErrCode_Type()
)
cfprApEtherPIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRmtErrCode.setStatus("current")
_CfprApEtherPIoFsmRmtErrDescr_Type = SnmpAdminString
_CfprApEtherPIoFsmRmtErrDescr_Object = MibTableColumn
cfprApEtherPIoFsmRmtErrDescr = _CfprApEtherPIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 10),
    _CfprApEtherPIoFsmRmtErrDescr_Type()
)
cfprApEtherPIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRmtErrDescr.setStatus("current")
_CfprApEtherPIoFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEtherPIoFsmRmtRslt_Object = MibTableColumn
cfprApEtherPIoFsmRmtRslt = _CfprApEtherPIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 17, 1, 11),
    _CfprApEtherPIoFsmRmtRslt_Type()
)
cfprApEtherPIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmRmtRslt.setStatus("current")
_CfprApEtherPIoFsmStageTable_Object = MibTable
cfprApEtherPIoFsmStageTable = _CfprApEtherPIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18)
)
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageTable.setStatus("current")
_CfprApEtherPIoFsmStageEntry_Object = MibTableRow
cfprApEtherPIoFsmStageEntry = _CfprApEtherPIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1)
)
cfprApEtherPIoFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageEntry.setStatus("current")
_CfprApEtherPIoFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPIoFsmStageInstanceId_Object = MibTableColumn
cfprApEtherPIoFsmStageInstanceId = _CfprApEtherPIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 1),
    _CfprApEtherPIoFsmStageInstanceId_Type()
)
cfprApEtherPIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageInstanceId.setStatus("current")
_CfprApEtherPIoFsmStageDn_Type = CfprApManagedObjectDn
_CfprApEtherPIoFsmStageDn_Object = MibTableColumn
cfprApEtherPIoFsmStageDn = _CfprApEtherPIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 2),
    _CfprApEtherPIoFsmStageDn_Type()
)
cfprApEtherPIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageDn.setStatus("current")
_CfprApEtherPIoFsmStageRn_Type = SnmpAdminString
_CfprApEtherPIoFsmStageRn_Object = MibTableColumn
cfprApEtherPIoFsmStageRn = _CfprApEtherPIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 3),
    _CfprApEtherPIoFsmStageRn_Type()
)
cfprApEtherPIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageRn.setStatus("current")
_CfprApEtherPIoFsmStageDescrData_Type = SnmpAdminString
_CfprApEtherPIoFsmStageDescrData_Object = MibTableColumn
cfprApEtherPIoFsmStageDescrData = _CfprApEtherPIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 4),
    _CfprApEtherPIoFsmStageDescrData_Type()
)
cfprApEtherPIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageDescrData.setStatus("current")
_CfprApEtherPIoFsmStageLastUpdateTime_Type = DateAndTime
_CfprApEtherPIoFsmStageLastUpdateTime_Object = MibTableColumn
cfprApEtherPIoFsmStageLastUpdateTime = _CfprApEtherPIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 5),
    _CfprApEtherPIoFsmStageLastUpdateTime_Type()
)
cfprApEtherPIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageLastUpdateTime.setStatus("current")
_CfprApEtherPIoFsmStageName_Type = CfprApEtherPIoFsmStageName
_CfprApEtherPIoFsmStageName_Object = MibTableColumn
cfprApEtherPIoFsmStageName = _CfprApEtherPIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 6),
    _CfprApEtherPIoFsmStageName_Type()
)
cfprApEtherPIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageName.setStatus("current")
_CfprApEtherPIoFsmStageOrder_Type = Gauge32
_CfprApEtherPIoFsmStageOrder_Object = MibTableColumn
cfprApEtherPIoFsmStageOrder = _CfprApEtherPIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 7),
    _CfprApEtherPIoFsmStageOrder_Type()
)
cfprApEtherPIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageOrder.setStatus("current")
_CfprApEtherPIoFsmStageRetry_Type = Gauge32
_CfprApEtherPIoFsmStageRetry_Object = MibTableColumn
cfprApEtherPIoFsmStageRetry = _CfprApEtherPIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 8),
    _CfprApEtherPIoFsmStageRetry_Type()
)
cfprApEtherPIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageRetry.setStatus("current")
_CfprApEtherPIoFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApEtherPIoFsmStageStageStatus_Object = MibTableColumn
cfprApEtherPIoFsmStageStageStatus = _CfprApEtherPIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 18, 1, 9),
    _CfprApEtherPIoFsmStageStageStatus_Type()
)
cfprApEtherPIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPIoFsmStageStageStatus.setStatus("current")
_CfprApEtherPauseStatsTable_Object = MibTable
cfprApEtherPauseStatsTable = _CfprApEtherPauseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19)
)
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsTable.setStatus("current")
_CfprApEtherPauseStatsEntry_Object = MibTableRow
cfprApEtherPauseStatsEntry = _CfprApEtherPauseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1)
)
cfprApEtherPauseStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPauseStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsEntry.setStatus("current")
_CfprApEtherPauseStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPauseStatsInstanceId_Object = MibTableColumn
cfprApEtherPauseStatsInstanceId = _CfprApEtherPauseStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 1),
    _CfprApEtherPauseStatsInstanceId_Type()
)
cfprApEtherPauseStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsInstanceId.setStatus("current")
_CfprApEtherPauseStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherPauseStatsDn_Object = MibTableColumn
cfprApEtherPauseStatsDn = _CfprApEtherPauseStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 2),
    _CfprApEtherPauseStatsDn_Type()
)
cfprApEtherPauseStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsDn.setStatus("current")
_CfprApEtherPauseStatsRn_Type = SnmpAdminString
_CfprApEtherPauseStatsRn_Object = MibTableColumn
cfprApEtherPauseStatsRn = _CfprApEtherPauseStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 3),
    _CfprApEtherPauseStatsRn_Type()
)
cfprApEtherPauseStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsRn.setStatus("current")
_CfprApEtherPauseStatsIntervals_Type = Gauge32
_CfprApEtherPauseStatsIntervals_Object = MibTableColumn
cfprApEtherPauseStatsIntervals = _CfprApEtherPauseStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 4),
    _CfprApEtherPauseStatsIntervals_Type()
)
cfprApEtherPauseStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsIntervals.setStatus("current")
_CfprApEtherPauseStatsRecvPause_Type = Unsigned64
_CfprApEtherPauseStatsRecvPause_Object = MibTableColumn
cfprApEtherPauseStatsRecvPause = _CfprApEtherPauseStatsRecvPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 5),
    _CfprApEtherPauseStatsRecvPause_Type()
)
cfprApEtherPauseStatsRecvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsRecvPause.setStatus("current")
_CfprApEtherPauseStatsRecvPauseDelta_Type = Counter64
_CfprApEtherPauseStatsRecvPauseDelta_Object = MibTableColumn
cfprApEtherPauseStatsRecvPauseDelta = _CfprApEtherPauseStatsRecvPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 6),
    _CfprApEtherPauseStatsRecvPauseDelta_Type()
)
cfprApEtherPauseStatsRecvPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsRecvPauseDelta.setStatus("current")
_CfprApEtherPauseStatsRecvPauseDeltaAvg_Type = Unsigned64
_CfprApEtherPauseStatsRecvPauseDeltaAvg_Object = MibTableColumn
cfprApEtherPauseStatsRecvPauseDeltaAvg = _CfprApEtherPauseStatsRecvPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 7),
    _CfprApEtherPauseStatsRecvPauseDeltaAvg_Type()
)
cfprApEtherPauseStatsRecvPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsRecvPauseDeltaAvg.setStatus("current")
_CfprApEtherPauseStatsRecvPauseDeltaMax_Type = Unsigned64
_CfprApEtherPauseStatsRecvPauseDeltaMax_Object = MibTableColumn
cfprApEtherPauseStatsRecvPauseDeltaMax = _CfprApEtherPauseStatsRecvPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 8),
    _CfprApEtherPauseStatsRecvPauseDeltaMax_Type()
)
cfprApEtherPauseStatsRecvPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsRecvPauseDeltaMax.setStatus("current")
_CfprApEtherPauseStatsRecvPauseDeltaMin_Type = Unsigned64
_CfprApEtherPauseStatsRecvPauseDeltaMin_Object = MibTableColumn
cfprApEtherPauseStatsRecvPauseDeltaMin = _CfprApEtherPauseStatsRecvPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 9),
    _CfprApEtherPauseStatsRecvPauseDeltaMin_Type()
)
cfprApEtherPauseStatsRecvPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsRecvPauseDeltaMin.setStatus("current")
_CfprApEtherPauseStatsResets_Type = Unsigned64
_CfprApEtherPauseStatsResets_Object = MibTableColumn
cfprApEtherPauseStatsResets = _CfprApEtherPauseStatsResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 10),
    _CfprApEtherPauseStatsResets_Type()
)
cfprApEtherPauseStatsResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsResets.setStatus("current")
_CfprApEtherPauseStatsResetsDelta_Type = Counter64
_CfprApEtherPauseStatsResetsDelta_Object = MibTableColumn
cfprApEtherPauseStatsResetsDelta = _CfprApEtherPauseStatsResetsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 11),
    _CfprApEtherPauseStatsResetsDelta_Type()
)
cfprApEtherPauseStatsResetsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsResetsDelta.setStatus("current")
_CfprApEtherPauseStatsResetsDeltaAvg_Type = Unsigned64
_CfprApEtherPauseStatsResetsDeltaAvg_Object = MibTableColumn
cfprApEtherPauseStatsResetsDeltaAvg = _CfprApEtherPauseStatsResetsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 12),
    _CfprApEtherPauseStatsResetsDeltaAvg_Type()
)
cfprApEtherPauseStatsResetsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsResetsDeltaAvg.setStatus("current")
_CfprApEtherPauseStatsResetsDeltaMax_Type = Unsigned64
_CfprApEtherPauseStatsResetsDeltaMax_Object = MibTableColumn
cfprApEtherPauseStatsResetsDeltaMax = _CfprApEtherPauseStatsResetsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 13),
    _CfprApEtherPauseStatsResetsDeltaMax_Type()
)
cfprApEtherPauseStatsResetsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsResetsDeltaMax.setStatus("current")
_CfprApEtherPauseStatsResetsDeltaMin_Type = Unsigned64
_CfprApEtherPauseStatsResetsDeltaMin_Object = MibTableColumn
cfprApEtherPauseStatsResetsDeltaMin = _CfprApEtherPauseStatsResetsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 14),
    _CfprApEtherPauseStatsResetsDeltaMin_Type()
)
cfprApEtherPauseStatsResetsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsResetsDeltaMin.setStatus("current")
_CfprApEtherPauseStatsSuspect_Type = TruthValue
_CfprApEtherPauseStatsSuspect_Object = MibTableColumn
cfprApEtherPauseStatsSuspect = _CfprApEtherPauseStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 15),
    _CfprApEtherPauseStatsSuspect_Type()
)
cfprApEtherPauseStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsSuspect.setStatus("current")
_CfprApEtherPauseStatsThresholded_Type = CfprApEtherPauseStatsThresholded
_CfprApEtherPauseStatsThresholded_Object = MibTableColumn
cfprApEtherPauseStatsThresholded = _CfprApEtherPauseStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 16),
    _CfprApEtherPauseStatsThresholded_Type()
)
cfprApEtherPauseStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsThresholded.setStatus("current")
_CfprApEtherPauseStatsTimeCollected_Type = DateAndTime
_CfprApEtherPauseStatsTimeCollected_Object = MibTableColumn
cfprApEtherPauseStatsTimeCollected = _CfprApEtherPauseStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 17),
    _CfprApEtherPauseStatsTimeCollected_Type()
)
cfprApEtherPauseStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsTimeCollected.setStatus("current")
_CfprApEtherPauseStatsUpdate_Type = Gauge32
_CfprApEtherPauseStatsUpdate_Object = MibTableColumn
cfprApEtherPauseStatsUpdate = _CfprApEtherPauseStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 18),
    _CfprApEtherPauseStatsUpdate_Type()
)
cfprApEtherPauseStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsUpdate.setStatus("current")
_CfprApEtherPauseStatsXmitPause_Type = Unsigned64
_CfprApEtherPauseStatsXmitPause_Object = MibTableColumn
cfprApEtherPauseStatsXmitPause = _CfprApEtherPauseStatsXmitPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 19),
    _CfprApEtherPauseStatsXmitPause_Type()
)
cfprApEtherPauseStatsXmitPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsXmitPause.setStatus("current")
_CfprApEtherPauseStatsXmitPauseDelta_Type = Counter64
_CfprApEtherPauseStatsXmitPauseDelta_Object = MibTableColumn
cfprApEtherPauseStatsXmitPauseDelta = _CfprApEtherPauseStatsXmitPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 20),
    _CfprApEtherPauseStatsXmitPauseDelta_Type()
)
cfprApEtherPauseStatsXmitPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsXmitPauseDelta.setStatus("current")
_CfprApEtherPauseStatsXmitPauseDeltaAvg_Type = Unsigned64
_CfprApEtherPauseStatsXmitPauseDeltaAvg_Object = MibTableColumn
cfprApEtherPauseStatsXmitPauseDeltaAvg = _CfprApEtherPauseStatsXmitPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 21),
    _CfprApEtherPauseStatsXmitPauseDeltaAvg_Type()
)
cfprApEtherPauseStatsXmitPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsXmitPauseDeltaAvg.setStatus("current")
_CfprApEtherPauseStatsXmitPauseDeltaMax_Type = Unsigned64
_CfprApEtherPauseStatsXmitPauseDeltaMax_Object = MibTableColumn
cfprApEtherPauseStatsXmitPauseDeltaMax = _CfprApEtherPauseStatsXmitPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 22),
    _CfprApEtherPauseStatsXmitPauseDeltaMax_Type()
)
cfprApEtherPauseStatsXmitPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsXmitPauseDeltaMax.setStatus("current")
_CfprApEtherPauseStatsXmitPauseDeltaMin_Type = Unsigned64
_CfprApEtherPauseStatsXmitPauseDeltaMin_Object = MibTableColumn
cfprApEtherPauseStatsXmitPauseDeltaMin = _CfprApEtherPauseStatsXmitPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 19, 1, 23),
    _CfprApEtherPauseStatsXmitPauseDeltaMin_Type()
)
cfprApEtherPauseStatsXmitPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsXmitPauseDeltaMin.setStatus("current")
_CfprApEtherPauseStatsHistTable_Object = MibTable
cfprApEtherPauseStatsHistTable = _CfprApEtherPauseStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20)
)
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistTable.setStatus("current")
_CfprApEtherPauseStatsHistEntry_Object = MibTableRow
cfprApEtherPauseStatsHistEntry = _CfprApEtherPauseStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1)
)
cfprApEtherPauseStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPauseStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistEntry.setStatus("current")
_CfprApEtherPauseStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPauseStatsHistInstanceId_Object = MibTableColumn
cfprApEtherPauseStatsHistInstanceId = _CfprApEtherPauseStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 1),
    _CfprApEtherPauseStatsHistInstanceId_Type()
)
cfprApEtherPauseStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistInstanceId.setStatus("current")
_CfprApEtherPauseStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherPauseStatsHistDn_Object = MibTableColumn
cfprApEtherPauseStatsHistDn = _CfprApEtherPauseStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 2),
    _CfprApEtherPauseStatsHistDn_Type()
)
cfprApEtherPauseStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistDn.setStatus("current")
_CfprApEtherPauseStatsHistRn_Type = SnmpAdminString
_CfprApEtherPauseStatsHistRn_Object = MibTableColumn
cfprApEtherPauseStatsHistRn = _CfprApEtherPauseStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 3),
    _CfprApEtherPauseStatsHistRn_Type()
)
cfprApEtherPauseStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistRn.setStatus("current")
_CfprApEtherPauseStatsHistId_Type = Unsigned64
_CfprApEtherPauseStatsHistId_Object = MibTableColumn
cfprApEtherPauseStatsHistId = _CfprApEtherPauseStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 4),
    _CfprApEtherPauseStatsHistId_Type()
)
cfprApEtherPauseStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistId.setStatus("current")
_CfprApEtherPauseStatsHistMostRecent_Type = TruthValue
_CfprApEtherPauseStatsHistMostRecent_Object = MibTableColumn
cfprApEtherPauseStatsHistMostRecent = _CfprApEtherPauseStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 5),
    _CfprApEtherPauseStatsHistMostRecent_Type()
)
cfprApEtherPauseStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistMostRecent.setStatus("current")
_CfprApEtherPauseStatsHistRecvPause_Type = Unsigned64
_CfprApEtherPauseStatsHistRecvPause_Object = MibTableColumn
cfprApEtherPauseStatsHistRecvPause = _CfprApEtherPauseStatsHistRecvPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 6),
    _CfprApEtherPauseStatsHistRecvPause_Type()
)
cfprApEtherPauseStatsHistRecvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistRecvPause.setStatus("current")
_CfprApEtherPauseStatsHistRecvPauseDelta_Type = Unsigned64
_CfprApEtherPauseStatsHistRecvPauseDelta_Object = MibTableColumn
cfprApEtherPauseStatsHistRecvPauseDelta = _CfprApEtherPauseStatsHistRecvPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 7),
    _CfprApEtherPauseStatsHistRecvPauseDelta_Type()
)
cfprApEtherPauseStatsHistRecvPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistRecvPauseDelta.setStatus("current")
_CfprApEtherPauseStatsHistRecvPauseDeltaAvg_Type = Unsigned64
_CfprApEtherPauseStatsHistRecvPauseDeltaAvg_Object = MibTableColumn
cfprApEtherPauseStatsHistRecvPauseDeltaAvg = _CfprApEtherPauseStatsHistRecvPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 8),
    _CfprApEtherPauseStatsHistRecvPauseDeltaAvg_Type()
)
cfprApEtherPauseStatsHistRecvPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistRecvPauseDeltaAvg.setStatus("current")
_CfprApEtherPauseStatsHistRecvPauseDeltaMax_Type = Unsigned64
_CfprApEtherPauseStatsHistRecvPauseDeltaMax_Object = MibTableColumn
cfprApEtherPauseStatsHistRecvPauseDeltaMax = _CfprApEtherPauseStatsHistRecvPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 9),
    _CfprApEtherPauseStatsHistRecvPauseDeltaMax_Type()
)
cfprApEtherPauseStatsHistRecvPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistRecvPauseDeltaMax.setStatus("current")
_CfprApEtherPauseStatsHistRecvPauseDeltaMin_Type = Unsigned64
_CfprApEtherPauseStatsHistRecvPauseDeltaMin_Object = MibTableColumn
cfprApEtherPauseStatsHistRecvPauseDeltaMin = _CfprApEtherPauseStatsHistRecvPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 10),
    _CfprApEtherPauseStatsHistRecvPauseDeltaMin_Type()
)
cfprApEtherPauseStatsHistRecvPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistRecvPauseDeltaMin.setStatus("current")
_CfprApEtherPauseStatsHistResets_Type = Unsigned64
_CfprApEtherPauseStatsHistResets_Object = MibTableColumn
cfprApEtherPauseStatsHistResets = _CfprApEtherPauseStatsHistResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 11),
    _CfprApEtherPauseStatsHistResets_Type()
)
cfprApEtherPauseStatsHistResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistResets.setStatus("current")
_CfprApEtherPauseStatsHistResetsDelta_Type = Unsigned64
_CfprApEtherPauseStatsHistResetsDelta_Object = MibTableColumn
cfprApEtherPauseStatsHistResetsDelta = _CfprApEtherPauseStatsHistResetsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 12),
    _CfprApEtherPauseStatsHistResetsDelta_Type()
)
cfprApEtherPauseStatsHistResetsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistResetsDelta.setStatus("current")
_CfprApEtherPauseStatsHistResetsDeltaAvg_Type = Unsigned64
_CfprApEtherPauseStatsHistResetsDeltaAvg_Object = MibTableColumn
cfprApEtherPauseStatsHistResetsDeltaAvg = _CfprApEtherPauseStatsHistResetsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 13),
    _CfprApEtherPauseStatsHistResetsDeltaAvg_Type()
)
cfprApEtherPauseStatsHistResetsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistResetsDeltaAvg.setStatus("current")
_CfprApEtherPauseStatsHistResetsDeltaMax_Type = Unsigned64
_CfprApEtherPauseStatsHistResetsDeltaMax_Object = MibTableColumn
cfprApEtherPauseStatsHistResetsDeltaMax = _CfprApEtherPauseStatsHistResetsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 14),
    _CfprApEtherPauseStatsHistResetsDeltaMax_Type()
)
cfprApEtherPauseStatsHistResetsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistResetsDeltaMax.setStatus("current")
_CfprApEtherPauseStatsHistResetsDeltaMin_Type = Unsigned64
_CfprApEtherPauseStatsHistResetsDeltaMin_Object = MibTableColumn
cfprApEtherPauseStatsHistResetsDeltaMin = _CfprApEtherPauseStatsHistResetsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 15),
    _CfprApEtherPauseStatsHistResetsDeltaMin_Type()
)
cfprApEtherPauseStatsHistResetsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistResetsDeltaMin.setStatus("current")
_CfprApEtherPauseStatsHistSuspect_Type = TruthValue
_CfprApEtherPauseStatsHistSuspect_Object = MibTableColumn
cfprApEtherPauseStatsHistSuspect = _CfprApEtherPauseStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 16),
    _CfprApEtherPauseStatsHistSuspect_Type()
)
cfprApEtherPauseStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistSuspect.setStatus("current")
_CfprApEtherPauseStatsHistThresholded_Type = CfprApEtherPauseStatsHistThresholded
_CfprApEtherPauseStatsHistThresholded_Object = MibTableColumn
cfprApEtherPauseStatsHistThresholded = _CfprApEtherPauseStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 17),
    _CfprApEtherPauseStatsHistThresholded_Type()
)
cfprApEtherPauseStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistThresholded.setStatus("current")
_CfprApEtherPauseStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherPauseStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherPauseStatsHistTimeCollected = _CfprApEtherPauseStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 18),
    _CfprApEtherPauseStatsHistTimeCollected_Type()
)
cfprApEtherPauseStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistTimeCollected.setStatus("current")
_CfprApEtherPauseStatsHistXmitPause_Type = Unsigned64
_CfprApEtherPauseStatsHistXmitPause_Object = MibTableColumn
cfprApEtherPauseStatsHistXmitPause = _CfprApEtherPauseStatsHistXmitPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 19),
    _CfprApEtherPauseStatsHistXmitPause_Type()
)
cfprApEtherPauseStatsHistXmitPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistXmitPause.setStatus("current")
_CfprApEtherPauseStatsHistXmitPauseDelta_Type = Unsigned64
_CfprApEtherPauseStatsHistXmitPauseDelta_Object = MibTableColumn
cfprApEtherPauseStatsHistXmitPauseDelta = _CfprApEtherPauseStatsHistXmitPauseDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 20),
    _CfprApEtherPauseStatsHistXmitPauseDelta_Type()
)
cfprApEtherPauseStatsHistXmitPauseDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistXmitPauseDelta.setStatus("current")
_CfprApEtherPauseStatsHistXmitPauseDeltaAvg_Type = Unsigned64
_CfprApEtherPauseStatsHistXmitPauseDeltaAvg_Object = MibTableColumn
cfprApEtherPauseStatsHistXmitPauseDeltaAvg = _CfprApEtherPauseStatsHistXmitPauseDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 21),
    _CfprApEtherPauseStatsHistXmitPauseDeltaAvg_Type()
)
cfprApEtherPauseStatsHistXmitPauseDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistXmitPauseDeltaAvg.setStatus("current")
_CfprApEtherPauseStatsHistXmitPauseDeltaMax_Type = Unsigned64
_CfprApEtherPauseStatsHistXmitPauseDeltaMax_Object = MibTableColumn
cfprApEtherPauseStatsHistXmitPauseDeltaMax = _CfprApEtherPauseStatsHistXmitPauseDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 22),
    _CfprApEtherPauseStatsHistXmitPauseDeltaMax_Type()
)
cfprApEtherPauseStatsHistXmitPauseDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistXmitPauseDeltaMax.setStatus("current")
_CfprApEtherPauseStatsHistXmitPauseDeltaMin_Type = Unsigned64
_CfprApEtherPauseStatsHistXmitPauseDeltaMin_Object = MibTableColumn
cfprApEtherPauseStatsHistXmitPauseDeltaMin = _CfprApEtherPauseStatsHistXmitPauseDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 20, 1, 23),
    _CfprApEtherPauseStatsHistXmitPauseDeltaMin_Type()
)
cfprApEtherPauseStatsHistXmitPauseDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPauseStatsHistXmitPauseDeltaMin.setStatus("current")
_CfprApEtherPortChanIdElemTable_Object = MibTable
cfprApEtherPortChanIdElemTable = _CfprApEtherPortChanIdElemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 21)
)
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdElemTable.setStatus("current")
_CfprApEtherPortChanIdElemEntry_Object = MibTableRow
cfprApEtherPortChanIdElemEntry = _CfprApEtherPortChanIdElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 21, 1)
)
cfprApEtherPortChanIdElemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPortChanIdElemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdElemEntry.setStatus("current")
_CfprApEtherPortChanIdElemInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPortChanIdElemInstanceId_Object = MibTableColumn
cfprApEtherPortChanIdElemInstanceId = _CfprApEtherPortChanIdElemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 21, 1, 1),
    _CfprApEtherPortChanIdElemInstanceId_Type()
)
cfprApEtherPortChanIdElemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdElemInstanceId.setStatus("current")
_CfprApEtherPortChanIdElemDn_Type = CfprApManagedObjectDn
_CfprApEtherPortChanIdElemDn_Object = MibTableColumn
cfprApEtherPortChanIdElemDn = _CfprApEtherPortChanIdElemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 21, 1, 2),
    _CfprApEtherPortChanIdElemDn_Type()
)
cfprApEtherPortChanIdElemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdElemDn.setStatus("current")
_CfprApEtherPortChanIdElemRn_Type = SnmpAdminString
_CfprApEtherPortChanIdElemRn_Object = MibTableColumn
cfprApEtherPortChanIdElemRn = _CfprApEtherPortChanIdElemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 21, 1, 3),
    _CfprApEtherPortChanIdElemRn_Type()
)
cfprApEtherPortChanIdElemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdElemRn.setStatus("current")
_CfprApEtherPortChanIdElemId_Type = Gauge32
_CfprApEtherPortChanIdElemId_Object = MibTableColumn
cfprApEtherPortChanIdElemId = _CfprApEtherPortChanIdElemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 21, 1, 4),
    _CfprApEtherPortChanIdElemId_Type()
)
cfprApEtherPortChanIdElemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdElemId.setStatus("current")
_CfprApEtherPortChanIdUniverseTable_Object = MibTable
cfprApEtherPortChanIdUniverseTable = _CfprApEtherPortChanIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 22)
)
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdUniverseTable.setStatus("current")
_CfprApEtherPortChanIdUniverseEntry_Object = MibTableRow
cfprApEtherPortChanIdUniverseEntry = _CfprApEtherPortChanIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 22, 1)
)
cfprApEtherPortChanIdUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherPortChanIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdUniverseEntry.setStatus("current")
_CfprApEtherPortChanIdUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApEtherPortChanIdUniverseInstanceId_Object = MibTableColumn
cfprApEtherPortChanIdUniverseInstanceId = _CfprApEtherPortChanIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 22, 1, 1),
    _CfprApEtherPortChanIdUniverseInstanceId_Type()
)
cfprApEtherPortChanIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdUniverseInstanceId.setStatus("current")
_CfprApEtherPortChanIdUniverseDn_Type = CfprApManagedObjectDn
_CfprApEtherPortChanIdUniverseDn_Object = MibTableColumn
cfprApEtherPortChanIdUniverseDn = _CfprApEtherPortChanIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 22, 1, 2),
    _CfprApEtherPortChanIdUniverseDn_Type()
)
cfprApEtherPortChanIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdUniverseDn.setStatus("current")
_CfprApEtherPortChanIdUniverseRn_Type = SnmpAdminString
_CfprApEtherPortChanIdUniverseRn_Object = MibTableColumn
cfprApEtherPortChanIdUniverseRn = _CfprApEtherPortChanIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 22, 1, 3),
    _CfprApEtherPortChanIdUniverseRn_Type()
)
cfprApEtherPortChanIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherPortChanIdUniverseRn.setStatus("current")
_CfprApEtherRxStatsTable_Object = MibTable
cfprApEtherRxStatsTable = _CfprApEtherRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23)
)
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTable.setStatus("current")
_CfprApEtherRxStatsEntry_Object = MibTableRow
cfprApEtherRxStatsEntry = _CfprApEtherRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1)
)
cfprApEtherRxStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherRxStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherRxStatsEntry.setStatus("current")
_CfprApEtherRxStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherRxStatsInstanceId_Object = MibTableColumn
cfprApEtherRxStatsInstanceId = _CfprApEtherRxStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 1),
    _CfprApEtherRxStatsInstanceId_Type()
)
cfprApEtherRxStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsInstanceId.setStatus("current")
_CfprApEtherRxStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherRxStatsDn_Object = MibTableColumn
cfprApEtherRxStatsDn = _CfprApEtherRxStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 2),
    _CfprApEtherRxStatsDn_Type()
)
cfprApEtherRxStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsDn.setStatus("current")
_CfprApEtherRxStatsRn_Type = SnmpAdminString
_CfprApEtherRxStatsRn_Object = MibTableColumn
cfprApEtherRxStatsRn = _CfprApEtherRxStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 3),
    _CfprApEtherRxStatsRn_Type()
)
cfprApEtherRxStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsRn.setStatus("current")
_CfprApEtherRxStatsBroadcastPackets_Type = Unsigned64
_CfprApEtherRxStatsBroadcastPackets_Object = MibTableColumn
cfprApEtherRxStatsBroadcastPackets = _CfprApEtherRxStatsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 4),
    _CfprApEtherRxStatsBroadcastPackets_Type()
)
cfprApEtherRxStatsBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsBroadcastPackets.setStatus("current")
_CfprApEtherRxStatsBroadcastPacketsDelta_Type = Counter64
_CfprApEtherRxStatsBroadcastPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsBroadcastPacketsDelta = _CfprApEtherRxStatsBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 5),
    _CfprApEtherRxStatsBroadcastPacketsDelta_Type()
)
cfprApEtherRxStatsBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsBroadcastPacketsDelta.setStatus("current")
_CfprApEtherRxStatsBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsBroadcastPacketsDeltaAvg = _CfprApEtherRxStatsBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 6),
    _CfprApEtherRxStatsBroadcastPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsBroadcastPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsBroadcastPacketsDeltaMax = _CfprApEtherRxStatsBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 7),
    _CfprApEtherRxStatsBroadcastPacketsDeltaMax_Type()
)
cfprApEtherRxStatsBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsBroadcastPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsBroadcastPacketsDeltaMin = _CfprApEtherRxStatsBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 8),
    _CfprApEtherRxStatsBroadcastPacketsDeltaMin_Type()
)
cfprApEtherRxStatsBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsBroadcastPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsIntervals_Type = Gauge32
_CfprApEtherRxStatsIntervals_Object = MibTableColumn
cfprApEtherRxStatsIntervals = _CfprApEtherRxStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 9),
    _CfprApEtherRxStatsIntervals_Type()
)
cfprApEtherRxStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsIntervals.setStatus("current")
_CfprApEtherRxStatsJumboPackets_Type = Unsigned64
_CfprApEtherRxStatsJumboPackets_Object = MibTableColumn
cfprApEtherRxStatsJumboPackets = _CfprApEtherRxStatsJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 10),
    _CfprApEtherRxStatsJumboPackets_Type()
)
cfprApEtherRxStatsJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsJumboPackets.setStatus("current")
_CfprApEtherRxStatsJumboPacketsDelta_Type = Counter64
_CfprApEtherRxStatsJumboPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsJumboPacketsDelta = _CfprApEtherRxStatsJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 11),
    _CfprApEtherRxStatsJumboPacketsDelta_Type()
)
cfprApEtherRxStatsJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsJumboPacketsDelta.setStatus("current")
_CfprApEtherRxStatsJumboPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsJumboPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsJumboPacketsDeltaAvg = _CfprApEtherRxStatsJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 12),
    _CfprApEtherRxStatsJumboPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsJumboPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsJumboPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsJumboPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsJumboPacketsDeltaMax = _CfprApEtherRxStatsJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 13),
    _CfprApEtherRxStatsJumboPacketsDeltaMax_Type()
)
cfprApEtherRxStatsJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsJumboPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsJumboPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsJumboPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsJumboPacketsDeltaMin = _CfprApEtherRxStatsJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 14),
    _CfprApEtherRxStatsJumboPacketsDeltaMin_Type()
)
cfprApEtherRxStatsJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsJumboPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsMulticastPackets_Type = Unsigned64
_CfprApEtherRxStatsMulticastPackets_Object = MibTableColumn
cfprApEtherRxStatsMulticastPackets = _CfprApEtherRxStatsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 15),
    _CfprApEtherRxStatsMulticastPackets_Type()
)
cfprApEtherRxStatsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsMulticastPackets.setStatus("current")
_CfprApEtherRxStatsMulticastPacketsDelta_Type = Counter64
_CfprApEtherRxStatsMulticastPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsMulticastPacketsDelta = _CfprApEtherRxStatsMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 16),
    _CfprApEtherRxStatsMulticastPacketsDelta_Type()
)
cfprApEtherRxStatsMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsMulticastPacketsDelta.setStatus("current")
_CfprApEtherRxStatsMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsMulticastPacketsDeltaAvg = _CfprApEtherRxStatsMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 17),
    _CfprApEtherRxStatsMulticastPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsMulticastPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsMulticastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsMulticastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsMulticastPacketsDeltaMax = _CfprApEtherRxStatsMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 18),
    _CfprApEtherRxStatsMulticastPacketsDeltaMax_Type()
)
cfprApEtherRxStatsMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsMulticastPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsMulticastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsMulticastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsMulticastPacketsDeltaMin = _CfprApEtherRxStatsMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 19),
    _CfprApEtherRxStatsMulticastPacketsDeltaMin_Type()
)
cfprApEtherRxStatsMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsMulticastPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsSuspect_Type = TruthValue
_CfprApEtherRxStatsSuspect_Object = MibTableColumn
cfprApEtherRxStatsSuspect = _CfprApEtherRxStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 20),
    _CfprApEtherRxStatsSuspect_Type()
)
cfprApEtherRxStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsSuspect.setStatus("current")
_CfprApEtherRxStatsThresholded_Type = CfprApEtherRxStatsThresholded
_CfprApEtherRxStatsThresholded_Object = MibTableColumn
cfprApEtherRxStatsThresholded = _CfprApEtherRxStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 21),
    _CfprApEtherRxStatsThresholded_Type()
)
cfprApEtherRxStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsThresholded.setStatus("current")
_CfprApEtherRxStatsTimeCollected_Type = DateAndTime
_CfprApEtherRxStatsTimeCollected_Object = MibTableColumn
cfprApEtherRxStatsTimeCollected = _CfprApEtherRxStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 22),
    _CfprApEtherRxStatsTimeCollected_Type()
)
cfprApEtherRxStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTimeCollected.setStatus("current")
_CfprApEtherRxStatsTotalBytes_Type = Unsigned64
_CfprApEtherRxStatsTotalBytes_Object = MibTableColumn
cfprApEtherRxStatsTotalBytes = _CfprApEtherRxStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 23),
    _CfprApEtherRxStatsTotalBytes_Type()
)
cfprApEtherRxStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalBytes.setStatus("current")
_CfprApEtherRxStatsTotalBytesDelta_Type = Counter64
_CfprApEtherRxStatsTotalBytesDelta_Object = MibTableColumn
cfprApEtherRxStatsTotalBytesDelta = _CfprApEtherRxStatsTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 24),
    _CfprApEtherRxStatsTotalBytesDelta_Type()
)
cfprApEtherRxStatsTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalBytesDelta.setStatus("current")
_CfprApEtherRxStatsTotalBytesDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsTotalBytesDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsTotalBytesDeltaAvg = _CfprApEtherRxStatsTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 25),
    _CfprApEtherRxStatsTotalBytesDeltaAvg_Type()
)
cfprApEtherRxStatsTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalBytesDeltaAvg.setStatus("current")
_CfprApEtherRxStatsTotalBytesDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsTotalBytesDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsTotalBytesDeltaMax = _CfprApEtherRxStatsTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 26),
    _CfprApEtherRxStatsTotalBytesDeltaMax_Type()
)
cfprApEtherRxStatsTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalBytesDeltaMax.setStatus("current")
_CfprApEtherRxStatsTotalBytesDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsTotalBytesDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsTotalBytesDeltaMin = _CfprApEtherRxStatsTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 27),
    _CfprApEtherRxStatsTotalBytesDeltaMin_Type()
)
cfprApEtherRxStatsTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalBytesDeltaMin.setStatus("current")
_CfprApEtherRxStatsTotalPackets_Type = Unsigned64
_CfprApEtherRxStatsTotalPackets_Object = MibTableColumn
cfprApEtherRxStatsTotalPackets = _CfprApEtherRxStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 28),
    _CfprApEtherRxStatsTotalPackets_Type()
)
cfprApEtherRxStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalPackets.setStatus("current")
_CfprApEtherRxStatsTotalPacketsDelta_Type = Counter64
_CfprApEtherRxStatsTotalPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsTotalPacketsDelta = _CfprApEtherRxStatsTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 29),
    _CfprApEtherRxStatsTotalPacketsDelta_Type()
)
cfprApEtherRxStatsTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalPacketsDelta.setStatus("current")
_CfprApEtherRxStatsTotalPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsTotalPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsTotalPacketsDeltaAvg = _CfprApEtherRxStatsTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 30),
    _CfprApEtherRxStatsTotalPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsTotalPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsTotalPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsTotalPacketsDeltaMax = _CfprApEtherRxStatsTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 31),
    _CfprApEtherRxStatsTotalPacketsDeltaMax_Type()
)
cfprApEtherRxStatsTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsTotalPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsTotalPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsTotalPacketsDeltaMin = _CfprApEtherRxStatsTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 32),
    _CfprApEtherRxStatsTotalPacketsDeltaMin_Type()
)
cfprApEtherRxStatsTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsTotalPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsUnicastPackets_Type = Unsigned64
_CfprApEtherRxStatsUnicastPackets_Object = MibTableColumn
cfprApEtherRxStatsUnicastPackets = _CfprApEtherRxStatsUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 33),
    _CfprApEtherRxStatsUnicastPackets_Type()
)
cfprApEtherRxStatsUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsUnicastPackets.setStatus("current")
_CfprApEtherRxStatsUnicastPacketsDelta_Type = Counter64
_CfprApEtherRxStatsUnicastPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsUnicastPacketsDelta = _CfprApEtherRxStatsUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 34),
    _CfprApEtherRxStatsUnicastPacketsDelta_Type()
)
cfprApEtherRxStatsUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsUnicastPacketsDelta.setStatus("current")
_CfprApEtherRxStatsUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsUnicastPacketsDeltaAvg = _CfprApEtherRxStatsUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 35),
    _CfprApEtherRxStatsUnicastPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsUnicastPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsUnicastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsUnicastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsUnicastPacketsDeltaMax = _CfprApEtherRxStatsUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 36),
    _CfprApEtherRxStatsUnicastPacketsDeltaMax_Type()
)
cfprApEtherRxStatsUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsUnicastPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsUnicastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsUnicastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsUnicastPacketsDeltaMin = _CfprApEtherRxStatsUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 37),
    _CfprApEtherRxStatsUnicastPacketsDeltaMin_Type()
)
cfprApEtherRxStatsUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsUnicastPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsUpdate_Type = Gauge32
_CfprApEtherRxStatsUpdate_Object = MibTableColumn
cfprApEtherRxStatsUpdate = _CfprApEtherRxStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 23, 1, 38),
    _CfprApEtherRxStatsUpdate_Type()
)
cfprApEtherRxStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsUpdate.setStatus("current")
_CfprApEtherRxStatsHistTable_Object = MibTable
cfprApEtherRxStatsHistTable = _CfprApEtherRxStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24)
)
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTable.setStatus("current")
_CfprApEtherRxStatsHistEntry_Object = MibTableRow
cfprApEtherRxStatsHistEntry = _CfprApEtherRxStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1)
)
cfprApEtherRxStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherRxStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistEntry.setStatus("current")
_CfprApEtherRxStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherRxStatsHistInstanceId_Object = MibTableColumn
cfprApEtherRxStatsHistInstanceId = _CfprApEtherRxStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 1),
    _CfprApEtherRxStatsHistInstanceId_Type()
)
cfprApEtherRxStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistInstanceId.setStatus("current")
_CfprApEtherRxStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherRxStatsHistDn_Object = MibTableColumn
cfprApEtherRxStatsHistDn = _CfprApEtherRxStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 2),
    _CfprApEtherRxStatsHistDn_Type()
)
cfprApEtherRxStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistDn.setStatus("current")
_CfprApEtherRxStatsHistRn_Type = SnmpAdminString
_CfprApEtherRxStatsHistRn_Object = MibTableColumn
cfprApEtherRxStatsHistRn = _CfprApEtherRxStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 3),
    _CfprApEtherRxStatsHistRn_Type()
)
cfprApEtherRxStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistRn.setStatus("current")
_CfprApEtherRxStatsHistBroadcastPackets_Type = Unsigned64
_CfprApEtherRxStatsHistBroadcastPackets_Object = MibTableColumn
cfprApEtherRxStatsHistBroadcastPackets = _CfprApEtherRxStatsHistBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 4),
    _CfprApEtherRxStatsHistBroadcastPackets_Type()
)
cfprApEtherRxStatsHistBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistBroadcastPackets.setStatus("current")
_CfprApEtherRxStatsHistBroadcastPacketsDelta_Type = Unsigned64
_CfprApEtherRxStatsHistBroadcastPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsHistBroadcastPacketsDelta = _CfprApEtherRxStatsHistBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 5),
    _CfprApEtherRxStatsHistBroadcastPacketsDelta_Type()
)
cfprApEtherRxStatsHistBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistBroadcastPacketsDelta.setStatus("current")
_CfprApEtherRxStatsHistBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsHistBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsHistBroadcastPacketsDeltaAvg = _CfprApEtherRxStatsHistBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 6),
    _CfprApEtherRxStatsHistBroadcastPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistBroadcastPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsHistBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsHistBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsHistBroadcastPacketsDeltaMax = _CfprApEtherRxStatsHistBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 7),
    _CfprApEtherRxStatsHistBroadcastPacketsDeltaMax_Type()
)
cfprApEtherRxStatsHistBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistBroadcastPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsHistBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsHistBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsHistBroadcastPacketsDeltaMin = _CfprApEtherRxStatsHistBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 8),
    _CfprApEtherRxStatsHistBroadcastPacketsDeltaMin_Type()
)
cfprApEtherRxStatsHistBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistBroadcastPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsHistId_Type = Unsigned64
_CfprApEtherRxStatsHistId_Object = MibTableColumn
cfprApEtherRxStatsHistId = _CfprApEtherRxStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 9),
    _CfprApEtherRxStatsHistId_Type()
)
cfprApEtherRxStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistId.setStatus("current")
_CfprApEtherRxStatsHistJumboPackets_Type = Unsigned64
_CfprApEtherRxStatsHistJumboPackets_Object = MibTableColumn
cfprApEtherRxStatsHistJumboPackets = _CfprApEtherRxStatsHistJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 10),
    _CfprApEtherRxStatsHistJumboPackets_Type()
)
cfprApEtherRxStatsHistJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistJumboPackets.setStatus("current")
_CfprApEtherRxStatsHistJumboPacketsDelta_Type = Unsigned64
_CfprApEtherRxStatsHistJumboPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsHistJumboPacketsDelta = _CfprApEtherRxStatsHistJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 11),
    _CfprApEtherRxStatsHistJumboPacketsDelta_Type()
)
cfprApEtherRxStatsHistJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistJumboPacketsDelta.setStatus("current")
_CfprApEtherRxStatsHistJumboPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsHistJumboPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsHistJumboPacketsDeltaAvg = _CfprApEtherRxStatsHistJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 12),
    _CfprApEtherRxStatsHistJumboPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsHistJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistJumboPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsHistJumboPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsHistJumboPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsHistJumboPacketsDeltaMax = _CfprApEtherRxStatsHistJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 13),
    _CfprApEtherRxStatsHistJumboPacketsDeltaMax_Type()
)
cfprApEtherRxStatsHistJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistJumboPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsHistJumboPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsHistJumboPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsHistJumboPacketsDeltaMin = _CfprApEtherRxStatsHistJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 14),
    _CfprApEtherRxStatsHistJumboPacketsDeltaMin_Type()
)
cfprApEtherRxStatsHistJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistJumboPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsHistMostRecent_Type = TruthValue
_CfprApEtherRxStatsHistMostRecent_Object = MibTableColumn
cfprApEtherRxStatsHistMostRecent = _CfprApEtherRxStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 15),
    _CfprApEtherRxStatsHistMostRecent_Type()
)
cfprApEtherRxStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistMostRecent.setStatus("current")
_CfprApEtherRxStatsHistMulticastPackets_Type = Unsigned64
_CfprApEtherRxStatsHistMulticastPackets_Object = MibTableColumn
cfprApEtherRxStatsHistMulticastPackets = _CfprApEtherRxStatsHistMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 16),
    _CfprApEtherRxStatsHistMulticastPackets_Type()
)
cfprApEtherRxStatsHistMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistMulticastPackets.setStatus("current")
_CfprApEtherRxStatsHistMulticastPacketsDelta_Type = Unsigned64
_CfprApEtherRxStatsHistMulticastPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsHistMulticastPacketsDelta = _CfprApEtherRxStatsHistMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 17),
    _CfprApEtherRxStatsHistMulticastPacketsDelta_Type()
)
cfprApEtherRxStatsHistMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistMulticastPacketsDelta.setStatus("current")
_CfprApEtherRxStatsHistMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsHistMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsHistMulticastPacketsDeltaAvg = _CfprApEtherRxStatsHistMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 18),
    _CfprApEtherRxStatsHistMulticastPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsHistMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistMulticastPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsHistMulticastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsHistMulticastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsHistMulticastPacketsDeltaMax = _CfprApEtherRxStatsHistMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 19),
    _CfprApEtherRxStatsHistMulticastPacketsDeltaMax_Type()
)
cfprApEtherRxStatsHistMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistMulticastPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsHistMulticastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsHistMulticastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsHistMulticastPacketsDeltaMin = _CfprApEtherRxStatsHistMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 20),
    _CfprApEtherRxStatsHistMulticastPacketsDeltaMin_Type()
)
cfprApEtherRxStatsHistMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistMulticastPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsHistSuspect_Type = TruthValue
_CfprApEtherRxStatsHistSuspect_Object = MibTableColumn
cfprApEtherRxStatsHistSuspect = _CfprApEtherRxStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 21),
    _CfprApEtherRxStatsHistSuspect_Type()
)
cfprApEtherRxStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistSuspect.setStatus("current")
_CfprApEtherRxStatsHistThresholded_Type = CfprApEtherRxStatsHistThresholded
_CfprApEtherRxStatsHistThresholded_Object = MibTableColumn
cfprApEtherRxStatsHistThresholded = _CfprApEtherRxStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 22),
    _CfprApEtherRxStatsHistThresholded_Type()
)
cfprApEtherRxStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistThresholded.setStatus("current")
_CfprApEtherRxStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherRxStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherRxStatsHistTimeCollected = _CfprApEtherRxStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 23),
    _CfprApEtherRxStatsHistTimeCollected_Type()
)
cfprApEtherRxStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTimeCollected.setStatus("current")
_CfprApEtherRxStatsHistTotalBytes_Type = Unsigned64
_CfprApEtherRxStatsHistTotalBytes_Object = MibTableColumn
cfprApEtherRxStatsHistTotalBytes = _CfprApEtherRxStatsHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 24),
    _CfprApEtherRxStatsHistTotalBytes_Type()
)
cfprApEtherRxStatsHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalBytes.setStatus("current")
_CfprApEtherRxStatsHistTotalBytesDelta_Type = Unsigned64
_CfprApEtherRxStatsHistTotalBytesDelta_Object = MibTableColumn
cfprApEtherRxStatsHistTotalBytesDelta = _CfprApEtherRxStatsHistTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 25),
    _CfprApEtherRxStatsHistTotalBytesDelta_Type()
)
cfprApEtherRxStatsHistTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalBytesDelta.setStatus("current")
_CfprApEtherRxStatsHistTotalBytesDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsHistTotalBytesDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsHistTotalBytesDeltaAvg = _CfprApEtherRxStatsHistTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 26),
    _CfprApEtherRxStatsHistTotalBytesDeltaAvg_Type()
)
cfprApEtherRxStatsHistTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalBytesDeltaAvg.setStatus("current")
_CfprApEtherRxStatsHistTotalBytesDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsHistTotalBytesDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsHistTotalBytesDeltaMax = _CfprApEtherRxStatsHistTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 27),
    _CfprApEtherRxStatsHistTotalBytesDeltaMax_Type()
)
cfprApEtherRxStatsHistTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalBytesDeltaMax.setStatus("current")
_CfprApEtherRxStatsHistTotalBytesDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsHistTotalBytesDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsHistTotalBytesDeltaMin = _CfprApEtherRxStatsHistTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 28),
    _CfprApEtherRxStatsHistTotalBytesDeltaMin_Type()
)
cfprApEtherRxStatsHistTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalBytesDeltaMin.setStatus("current")
_CfprApEtherRxStatsHistTotalPackets_Type = Unsigned64
_CfprApEtherRxStatsHistTotalPackets_Object = MibTableColumn
cfprApEtherRxStatsHistTotalPackets = _CfprApEtherRxStatsHistTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 29),
    _CfprApEtherRxStatsHistTotalPackets_Type()
)
cfprApEtherRxStatsHistTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalPackets.setStatus("current")
_CfprApEtherRxStatsHistTotalPacketsDelta_Type = Unsigned64
_CfprApEtherRxStatsHistTotalPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsHistTotalPacketsDelta = _CfprApEtherRxStatsHistTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 30),
    _CfprApEtherRxStatsHistTotalPacketsDelta_Type()
)
cfprApEtherRxStatsHistTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalPacketsDelta.setStatus("current")
_CfprApEtherRxStatsHistTotalPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsHistTotalPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsHistTotalPacketsDeltaAvg = _CfprApEtherRxStatsHistTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 31),
    _CfprApEtherRxStatsHistTotalPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsHistTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsHistTotalPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsHistTotalPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsHistTotalPacketsDeltaMax = _CfprApEtherRxStatsHistTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 32),
    _CfprApEtherRxStatsHistTotalPacketsDeltaMax_Type()
)
cfprApEtherRxStatsHistTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsHistTotalPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsHistTotalPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsHistTotalPacketsDeltaMin = _CfprApEtherRxStatsHistTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 33),
    _CfprApEtherRxStatsHistTotalPacketsDeltaMin_Type()
)
cfprApEtherRxStatsHistTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistTotalPacketsDeltaMin.setStatus("current")
_CfprApEtherRxStatsHistUnicastPackets_Type = Unsigned64
_CfprApEtherRxStatsHistUnicastPackets_Object = MibTableColumn
cfprApEtherRxStatsHistUnicastPackets = _CfprApEtherRxStatsHistUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 34),
    _CfprApEtherRxStatsHistUnicastPackets_Type()
)
cfprApEtherRxStatsHistUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistUnicastPackets.setStatus("current")
_CfprApEtherRxStatsHistUnicastPacketsDelta_Type = Unsigned64
_CfprApEtherRxStatsHistUnicastPacketsDelta_Object = MibTableColumn
cfprApEtherRxStatsHistUnicastPacketsDelta = _CfprApEtherRxStatsHistUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 35),
    _CfprApEtherRxStatsHistUnicastPacketsDelta_Type()
)
cfprApEtherRxStatsHistUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistUnicastPacketsDelta.setStatus("current")
_CfprApEtherRxStatsHistUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherRxStatsHistUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherRxStatsHistUnicastPacketsDeltaAvg = _CfprApEtherRxStatsHistUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 36),
    _CfprApEtherRxStatsHistUnicastPacketsDeltaAvg_Type()
)
cfprApEtherRxStatsHistUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistUnicastPacketsDeltaAvg.setStatus("current")
_CfprApEtherRxStatsHistUnicastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherRxStatsHistUnicastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherRxStatsHistUnicastPacketsDeltaMax = _CfprApEtherRxStatsHistUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 37),
    _CfprApEtherRxStatsHistUnicastPacketsDeltaMax_Type()
)
cfprApEtherRxStatsHistUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistUnicastPacketsDeltaMax.setStatus("current")
_CfprApEtherRxStatsHistUnicastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherRxStatsHistUnicastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherRxStatsHistUnicastPacketsDeltaMin = _CfprApEtherRxStatsHistUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 24, 1, 38),
    _CfprApEtherRxStatsHistUnicastPacketsDeltaMin_Type()
)
cfprApEtherRxStatsHistUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherRxStatsHistUnicastPacketsDeltaMin.setStatus("current")
_CfprApEtherServerIntFIoTable_Object = MibTable
cfprApEtherServerIntFIoTable = _CfprApEtherServerIntFIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25)
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoTable.setStatus("current")
_CfprApEtherServerIntFIoEntry_Object = MibTableRow
cfprApEtherServerIntFIoEntry = _CfprApEtherServerIntFIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1)
)
cfprApEtherServerIntFIoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherServerIntFIoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoEntry.setStatus("current")
_CfprApEtherServerIntFIoInstanceId_Type = CfprApManagedObjectId
_CfprApEtherServerIntFIoInstanceId_Object = MibTableColumn
cfprApEtherServerIntFIoInstanceId = _CfprApEtherServerIntFIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 1),
    _CfprApEtherServerIntFIoInstanceId_Type()
)
cfprApEtherServerIntFIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoInstanceId.setStatus("current")
_CfprApEtherServerIntFIoDn_Type = CfprApManagedObjectDn
_CfprApEtherServerIntFIoDn_Object = MibTableColumn
cfprApEtherServerIntFIoDn = _CfprApEtherServerIntFIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 2),
    _CfprApEtherServerIntFIoDn_Type()
)
cfprApEtherServerIntFIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoDn.setStatus("current")
_CfprApEtherServerIntFIoRn_Type = SnmpAdminString
_CfprApEtherServerIntFIoRn_Object = MibTableColumn
cfprApEtherServerIntFIoRn = _CfprApEtherServerIntFIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 3),
    _CfprApEtherServerIntFIoRn_Type()
)
cfprApEtherServerIntFIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoRn.setStatus("current")
_CfprApEtherServerIntFIoAdminSpeed_Type = CfprApPortEthSpeed
_CfprApEtherServerIntFIoAdminSpeed_Object = MibTableColumn
cfprApEtherServerIntFIoAdminSpeed = _CfprApEtherServerIntFIoAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 4),
    _CfprApEtherServerIntFIoAdminSpeed_Type()
)
cfprApEtherServerIntFIoAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoAdminSpeed.setStatus("current")
_CfprApEtherServerIntFIoAdminState_Type = CfprApEtherServerIntFIoAdminState
_CfprApEtherServerIntFIoAdminState_Object = MibTableColumn
cfprApEtherServerIntFIoAdminState = _CfprApEtherServerIntFIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 5),
    _CfprApEtherServerIntFIoAdminState_Type()
)
cfprApEtherServerIntFIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoAdminState.setStatus("current")
_CfprApEtherServerIntFIoAggrPortId_Type = Gauge32
_CfprApEtherServerIntFIoAggrPortId_Object = MibTableColumn
cfprApEtherServerIntFIoAggrPortId = _CfprApEtherServerIntFIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 6),
    _CfprApEtherServerIntFIoAggrPortId_Type()
)
cfprApEtherServerIntFIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoAggrPortId.setStatus("current")
_CfprApEtherServerIntFIoChassisId_Type = Gauge32
_CfprApEtherServerIntFIoChassisId_Object = MibTableColumn
cfprApEtherServerIntFIoChassisId = _CfprApEtherServerIntFIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 7),
    _CfprApEtherServerIntFIoChassisId_Type()
)
cfprApEtherServerIntFIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoChassisId.setStatus("current")
_CfprApEtherServerIntFIoEncap_Type = CfprApPortEncap
_CfprApEtherServerIntFIoEncap_Object = MibTableColumn
cfprApEtherServerIntFIoEncap = _CfprApEtherServerIntFIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 8),
    _CfprApEtherServerIntFIoEncap_Type()
)
cfprApEtherServerIntFIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoEncap.setStatus("current")
_CfprApEtherServerIntFIoEpDn_Type = SnmpAdminString
_CfprApEtherServerIntFIoEpDn_Object = MibTableColumn
cfprApEtherServerIntFIoEpDn = _CfprApEtherServerIntFIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 9),
    _CfprApEtherServerIntFIoEpDn_Type()
)
cfprApEtherServerIntFIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoEpDn.setStatus("current")
_CfprApEtherServerIntFIoFltAggr_Type = Unsigned64
_CfprApEtherServerIntFIoFltAggr_Object = MibTableColumn
cfprApEtherServerIntFIoFltAggr = _CfprApEtherServerIntFIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 10),
    _CfprApEtherServerIntFIoFltAggr_Type()
)
cfprApEtherServerIntFIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFltAggr.setStatus("current")
_CfprApEtherServerIntFIoFsmDescr_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmDescr_Object = MibTableColumn
cfprApEtherServerIntFIoFsmDescr = _CfprApEtherServerIntFIoFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 11),
    _CfprApEtherServerIntFIoFsmDescr_Type()
)
cfprApEtherServerIntFIoFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmDescr.setStatus("current")
_CfprApEtherServerIntFIoFsmPrev_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmPrev_Object = MibTableColumn
cfprApEtherServerIntFIoFsmPrev = _CfprApEtherServerIntFIoFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 12),
    _CfprApEtherServerIntFIoFsmPrev_Type()
)
cfprApEtherServerIntFIoFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmPrev.setStatus("current")
_CfprApEtherServerIntFIoFsmProgr_Type = Gauge32
_CfprApEtherServerIntFIoFsmProgr_Object = MibTableColumn
cfprApEtherServerIntFIoFsmProgr = _CfprApEtherServerIntFIoFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 13),
    _CfprApEtherServerIntFIoFsmProgr_Type()
)
cfprApEtherServerIntFIoFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmProgr.setStatus("current")
_CfprApEtherServerIntFIoFsmRmtInvErrCode_Type = Gauge32
_CfprApEtherServerIntFIoFsmRmtInvErrCode_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRmtInvErrCode = _CfprApEtherServerIntFIoFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 14),
    _CfprApEtherServerIntFIoFsmRmtInvErrCode_Type()
)
cfprApEtherServerIntFIoFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRmtInvErrCode.setStatus("current")
_CfprApEtherServerIntFIoFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmRmtInvErrDescr_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRmtInvErrDescr = _CfprApEtherServerIntFIoFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 15),
    _CfprApEtherServerIntFIoFsmRmtInvErrDescr_Type()
)
cfprApEtherServerIntFIoFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRmtInvErrDescr.setStatus("current")
_CfprApEtherServerIntFIoFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEtherServerIntFIoFsmRmtInvRslt_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRmtInvRslt = _CfprApEtherServerIntFIoFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 16),
    _CfprApEtherServerIntFIoFsmRmtInvRslt_Type()
)
cfprApEtherServerIntFIoFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRmtInvRslt.setStatus("current")
_CfprApEtherServerIntFIoFsmStageDescr_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmStageDescr_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageDescr = _CfprApEtherServerIntFIoFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 17),
    _CfprApEtherServerIntFIoFsmStageDescr_Type()
)
cfprApEtherServerIntFIoFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageDescr.setStatus("current")
_CfprApEtherServerIntFIoFsmStamp_Type = DateAndTime
_CfprApEtherServerIntFIoFsmStamp_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStamp = _CfprApEtherServerIntFIoFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 18),
    _CfprApEtherServerIntFIoFsmStamp_Type()
)
cfprApEtherServerIntFIoFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStamp.setStatus("current")
_CfprApEtherServerIntFIoFsmStatus_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmStatus_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStatus = _CfprApEtherServerIntFIoFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 19),
    _CfprApEtherServerIntFIoFsmStatus_Type()
)
cfprApEtherServerIntFIoFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStatus.setStatus("current")
_CfprApEtherServerIntFIoFsmTry_Type = Gauge32
_CfprApEtherServerIntFIoFsmTry_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTry = _CfprApEtherServerIntFIoFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 20),
    _CfprApEtherServerIntFIoFsmTry_Type()
)
cfprApEtherServerIntFIoFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTry.setStatus("current")
_CfprApEtherServerIntFIoIfRole_Type = CfprApEtherServerIntFIoIfRole
_CfprApEtherServerIntFIoIfRole_Object = MibTableColumn
cfprApEtherServerIntFIoIfRole = _CfprApEtherServerIntFIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 21),
    _CfprApEtherServerIntFIoIfRole_Type()
)
cfprApEtherServerIntFIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoIfRole.setStatus("current")
_CfprApEtherServerIntFIoIfType_Type = CfprApNetworkPhysEpIfType
_CfprApEtherServerIntFIoIfType_Object = MibTableColumn
cfprApEtherServerIntFIoIfType = _CfprApEtherServerIntFIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 22),
    _CfprApEtherServerIntFIoIfType_Type()
)
cfprApEtherServerIntFIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoIfType.setStatus("current")
_CfprApEtherServerIntFIoLocale_Type = CfprApEtherServerIntFIoLocale
_CfprApEtherServerIntFIoLocale_Object = MibTableColumn
cfprApEtherServerIntFIoLocale = _CfprApEtherServerIntFIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 23),
    _CfprApEtherServerIntFIoLocale_Type()
)
cfprApEtherServerIntFIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoLocale.setStatus("current")
_CfprApEtherServerIntFIoMac_Type = MacAddress
_CfprApEtherServerIntFIoMac_Object = MibTableColumn
cfprApEtherServerIntFIoMac = _CfprApEtherServerIntFIoMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 24),
    _CfprApEtherServerIntFIoMac_Type()
)
cfprApEtherServerIntFIoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoMac.setStatus("current")
_CfprApEtherServerIntFIoMode_Type = CfprApPortMode
_CfprApEtherServerIntFIoMode_Object = MibTableColumn
cfprApEtherServerIntFIoMode = _CfprApEtherServerIntFIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 25),
    _CfprApEtherServerIntFIoMode_Type()
)
cfprApEtherServerIntFIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoMode.setStatus("current")
_CfprApEtherServerIntFIoModel_Type = SnmpAdminString
_CfprApEtherServerIntFIoModel_Object = MibTableColumn
cfprApEtherServerIntFIoModel = _CfprApEtherServerIntFIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 26),
    _CfprApEtherServerIntFIoModel_Type()
)
cfprApEtherServerIntFIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoModel.setStatus("current")
_CfprApEtherServerIntFIoName_Type = SnmpAdminString
_CfprApEtherServerIntFIoName_Object = MibTableColumn
cfprApEtherServerIntFIoName = _CfprApEtherServerIntFIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 27),
    _CfprApEtherServerIntFIoName_Type()
)
cfprApEtherServerIntFIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoName.setStatus("current")
_CfprApEtherServerIntFIoNsSize_Type = Gauge32
_CfprApEtherServerIntFIoNsSize_Object = MibTableColumn
cfprApEtherServerIntFIoNsSize = _CfprApEtherServerIntFIoNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 28),
    _CfprApEtherServerIntFIoNsSize_Type()
)
cfprApEtherServerIntFIoNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoNsSize.setStatus("current")
_CfprApEtherServerIntFIoOperBorderAggrPortId_Type = Gauge32
_CfprApEtherServerIntFIoOperBorderAggrPortId_Object = MibTableColumn
cfprApEtherServerIntFIoOperBorderAggrPortId = _CfprApEtherServerIntFIoOperBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 29),
    _CfprApEtherServerIntFIoOperBorderAggrPortId_Type()
)
cfprApEtherServerIntFIoOperBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoOperBorderAggrPortId.setStatus("current")
_CfprApEtherServerIntFIoOperBorderPortId_Type = Gauge32
_CfprApEtherServerIntFIoOperBorderPortId_Object = MibTableColumn
cfprApEtherServerIntFIoOperBorderPortId = _CfprApEtherServerIntFIoOperBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 30),
    _CfprApEtherServerIntFIoOperBorderPortId_Type()
)
cfprApEtherServerIntFIoOperBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoOperBorderPortId.setStatus("current")
_CfprApEtherServerIntFIoOperBorderSlotId_Type = Gauge32
_CfprApEtherServerIntFIoOperBorderSlotId_Object = MibTableColumn
cfprApEtherServerIntFIoOperBorderSlotId = _CfprApEtherServerIntFIoOperBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 31),
    _CfprApEtherServerIntFIoOperBorderSlotId_Type()
)
cfprApEtherServerIntFIoOperBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoOperBorderSlotId.setStatus("current")
_CfprApEtherServerIntFIoOperState_Type = CfprApNetworkPortOperState
_CfprApEtherServerIntFIoOperState_Object = MibTableColumn
cfprApEtherServerIntFIoOperState = _CfprApEtherServerIntFIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 32),
    _CfprApEtherServerIntFIoOperState_Type()
)
cfprApEtherServerIntFIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoOperState.setStatus("current")
_CfprApEtherServerIntFIoPeerAggrPortId_Type = Gauge32
_CfprApEtherServerIntFIoPeerAggrPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPeerAggrPortId = _CfprApEtherServerIntFIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 33),
    _CfprApEtherServerIntFIoPeerAggrPortId_Type()
)
cfprApEtherServerIntFIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPeerAggrPortId.setStatus("current")
_CfprApEtherServerIntFIoPeerChassisId_Type = Gauge32
_CfprApEtherServerIntFIoPeerChassisId_Object = MibTableColumn
cfprApEtherServerIntFIoPeerChassisId = _CfprApEtherServerIntFIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 34),
    _CfprApEtherServerIntFIoPeerChassisId_Type()
)
cfprApEtherServerIntFIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPeerChassisId.setStatus("current")
_CfprApEtherServerIntFIoPeerDn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPeerDn_Object = MibTableColumn
cfprApEtherServerIntFIoPeerDn = _CfprApEtherServerIntFIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 35),
    _CfprApEtherServerIntFIoPeerDn_Type()
)
cfprApEtherServerIntFIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPeerDn.setStatus("current")
_CfprApEtherServerIntFIoPeerEncap_Type = Gauge32
_CfprApEtherServerIntFIoPeerEncap_Object = MibTableColumn
cfprApEtherServerIntFIoPeerEncap = _CfprApEtherServerIntFIoPeerEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 36),
    _CfprApEtherServerIntFIoPeerEncap_Type()
)
cfprApEtherServerIntFIoPeerEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPeerEncap.setStatus("current")
_CfprApEtherServerIntFIoPeerPortId_Type = Gauge32
_CfprApEtherServerIntFIoPeerPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPeerPortId = _CfprApEtherServerIntFIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 37),
    _CfprApEtherServerIntFIoPeerPortId_Type()
)
cfprApEtherServerIntFIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPeerPortId.setStatus("current")
_CfprApEtherServerIntFIoPeerSlotId_Type = Gauge32
_CfprApEtherServerIntFIoPeerSlotId_Object = MibTableColumn
cfprApEtherServerIntFIoPeerSlotId = _CfprApEtherServerIntFIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 38),
    _CfprApEtherServerIntFIoPeerSlotId_Type()
)
cfprApEtherServerIntFIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPeerSlotId.setStatus("current")
_CfprApEtherServerIntFIoPortId_Type = Gauge32
_CfprApEtherServerIntFIoPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPortId = _CfprApEtherServerIntFIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 39),
    _CfprApEtherServerIntFIoPortId_Type()
)
cfprApEtherServerIntFIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPortId.setStatus("current")
_CfprApEtherServerIntFIoRevision_Type = SnmpAdminString
_CfprApEtherServerIntFIoRevision_Object = MibTableColumn
cfprApEtherServerIntFIoRevision = _CfprApEtherServerIntFIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 40),
    _CfprApEtherServerIntFIoRevision_Type()
)
cfprApEtherServerIntFIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoRevision.setStatus("current")
_CfprApEtherServerIntFIoSerial_Type = SnmpAdminString
_CfprApEtherServerIntFIoSerial_Object = MibTableColumn
cfprApEtherServerIntFIoSerial = _CfprApEtherServerIntFIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 41),
    _CfprApEtherServerIntFIoSerial_Type()
)
cfprApEtherServerIntFIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoSerial.setStatus("current")
_CfprApEtherServerIntFIoSlotId_Type = Gauge32
_CfprApEtherServerIntFIoSlotId_Object = MibTableColumn
cfprApEtherServerIntFIoSlotId = _CfprApEtherServerIntFIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 42),
    _CfprApEtherServerIntFIoSlotId_Type()
)
cfprApEtherServerIntFIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoSlotId.setStatus("current")
_CfprApEtherServerIntFIoStateQual_Type = SnmpAdminString
_CfprApEtherServerIntFIoStateQual_Object = MibTableColumn
cfprApEtherServerIntFIoStateQual = _CfprApEtherServerIntFIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 43),
    _CfprApEtherServerIntFIoStateQual_Type()
)
cfprApEtherServerIntFIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoStateQual.setStatus("current")
_CfprApEtherServerIntFIoSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherServerIntFIoSwitchId_Object = MibTableColumn
cfprApEtherServerIntFIoSwitchId = _CfprApEtherServerIntFIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 44),
    _CfprApEtherServerIntFIoSwitchId_Type()
)
cfprApEtherServerIntFIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoSwitchId.setStatus("current")
_CfprApEtherServerIntFIoTransport_Type = CfprApEtherServerIntFIoTransport
_CfprApEtherServerIntFIoTransport_Object = MibTableColumn
cfprApEtherServerIntFIoTransport = _CfprApEtherServerIntFIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 45),
    _CfprApEtherServerIntFIoTransport_Type()
)
cfprApEtherServerIntFIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoTransport.setStatus("current")
_CfprApEtherServerIntFIoTs_Type = DateAndTime
_CfprApEtherServerIntFIoTs_Object = MibTableColumn
cfprApEtherServerIntFIoTs = _CfprApEtherServerIntFIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 46),
    _CfprApEtherServerIntFIoTs_Type()
)
cfprApEtherServerIntFIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoTs.setStatus("current")
_CfprApEtherServerIntFIoType_Type = CfprApEtherServerIntFIoType
_CfprApEtherServerIntFIoType_Object = MibTableColumn
cfprApEtherServerIntFIoType = _CfprApEtherServerIntFIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 47),
    _CfprApEtherServerIntFIoType_Type()
)
cfprApEtherServerIntFIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoType.setStatus("current")
_CfprApEtherServerIntFIoVendor_Type = SnmpAdminString
_CfprApEtherServerIntFIoVendor_Object = MibTableColumn
cfprApEtherServerIntFIoVendor = _CfprApEtherServerIntFIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 48),
    _CfprApEtherServerIntFIoVendor_Type()
)
cfprApEtherServerIntFIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoVendor.setStatus("current")
_CfprApEtherServerIntFIoXcvrType_Type = CfprApEquipmentXcvrType
_CfprApEtherServerIntFIoXcvrType_Object = MibTableColumn
cfprApEtherServerIntFIoXcvrType = _CfprApEtherServerIntFIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 25, 1, 49),
    _CfprApEtherServerIntFIoXcvrType_Type()
)
cfprApEtherServerIntFIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoXcvrType.setStatus("current")
_CfprApEtherServerIntFIoFsmTable_Object = MibTable
cfprApEtherServerIntFIoFsmTable = _CfprApEtherServerIntFIoFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26)
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTable.setStatus("current")
_CfprApEtherServerIntFIoFsmEntry_Object = MibTableRow
cfprApEtherServerIntFIoFsmEntry = _CfprApEtherServerIntFIoFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1)
)
cfprApEtherServerIntFIoFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherServerIntFIoFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmEntry.setStatus("current")
_CfprApEtherServerIntFIoFsmInstanceId_Type = CfprApManagedObjectId
_CfprApEtherServerIntFIoFsmInstanceId_Object = MibTableColumn
cfprApEtherServerIntFIoFsmInstanceId = _CfprApEtherServerIntFIoFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 1),
    _CfprApEtherServerIntFIoFsmInstanceId_Type()
)
cfprApEtherServerIntFIoFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmInstanceId.setStatus("current")
_CfprApEtherServerIntFIoFsmDn_Type = CfprApManagedObjectDn
_CfprApEtherServerIntFIoFsmDn_Object = MibTableColumn
cfprApEtherServerIntFIoFsmDn = _CfprApEtherServerIntFIoFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 2),
    _CfprApEtherServerIntFIoFsmDn_Type()
)
cfprApEtherServerIntFIoFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmDn.setStatus("current")
_CfprApEtherServerIntFIoFsmRn_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmRn_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRn = _CfprApEtherServerIntFIoFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 3),
    _CfprApEtherServerIntFIoFsmRn_Type()
)
cfprApEtherServerIntFIoFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRn.setStatus("current")
_CfprApEtherServerIntFIoFsmCompletionTime_Type = DateAndTime
_CfprApEtherServerIntFIoFsmCompletionTime_Object = MibTableColumn
cfprApEtherServerIntFIoFsmCompletionTime = _CfprApEtherServerIntFIoFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 4),
    _CfprApEtherServerIntFIoFsmCompletionTime_Type()
)
cfprApEtherServerIntFIoFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmCompletionTime.setStatus("current")
_CfprApEtherServerIntFIoFsmCurrentFsm_Type = CfprApEtherServerIntFIoFsmCurrentFsm
_CfprApEtherServerIntFIoFsmCurrentFsm_Object = MibTableColumn
cfprApEtherServerIntFIoFsmCurrentFsm = _CfprApEtherServerIntFIoFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 5),
    _CfprApEtherServerIntFIoFsmCurrentFsm_Type()
)
cfprApEtherServerIntFIoFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmCurrentFsm.setStatus("current")
_CfprApEtherServerIntFIoFsmDescrData_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmDescrData_Object = MibTableColumn
cfprApEtherServerIntFIoFsmDescrData = _CfprApEtherServerIntFIoFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 6),
    _CfprApEtherServerIntFIoFsmDescrData_Type()
)
cfprApEtherServerIntFIoFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmDescrData.setStatus("current")
_CfprApEtherServerIntFIoFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApEtherServerIntFIoFsmFsmStatus_Object = MibTableColumn
cfprApEtherServerIntFIoFsmFsmStatus = _CfprApEtherServerIntFIoFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 7),
    _CfprApEtherServerIntFIoFsmFsmStatus_Type()
)
cfprApEtherServerIntFIoFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmFsmStatus.setStatus("current")
_CfprApEtherServerIntFIoFsmProgress_Type = Gauge32
_CfprApEtherServerIntFIoFsmProgress_Object = MibTableColumn
cfprApEtherServerIntFIoFsmProgress = _CfprApEtherServerIntFIoFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 8),
    _CfprApEtherServerIntFIoFsmProgress_Type()
)
cfprApEtherServerIntFIoFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmProgress.setStatus("current")
_CfprApEtherServerIntFIoFsmRmtErrCode_Type = Gauge32
_CfprApEtherServerIntFIoFsmRmtErrCode_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRmtErrCode = _CfprApEtherServerIntFIoFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 9),
    _CfprApEtherServerIntFIoFsmRmtErrCode_Type()
)
cfprApEtherServerIntFIoFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRmtErrCode.setStatus("current")
_CfprApEtherServerIntFIoFsmRmtErrDescr_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmRmtErrDescr_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRmtErrDescr = _CfprApEtherServerIntFIoFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 10),
    _CfprApEtherServerIntFIoFsmRmtErrDescr_Type()
)
cfprApEtherServerIntFIoFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRmtErrDescr.setStatus("current")
_CfprApEtherServerIntFIoFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEtherServerIntFIoFsmRmtRslt_Object = MibTableColumn
cfprApEtherServerIntFIoFsmRmtRslt = _CfprApEtherServerIntFIoFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 26, 1, 11),
    _CfprApEtherServerIntFIoFsmRmtRslt_Type()
)
cfprApEtherServerIntFIoFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmRmtRslt.setStatus("current")
_CfprApEtherServerIntFIoFsmStageTable_Object = MibTable
cfprApEtherServerIntFIoFsmStageTable = _CfprApEtherServerIntFIoFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27)
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageTable.setStatus("current")
_CfprApEtherServerIntFIoFsmStageEntry_Object = MibTableRow
cfprApEtherServerIntFIoFsmStageEntry = _CfprApEtherServerIntFIoFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1)
)
cfprApEtherServerIntFIoFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherServerIntFIoFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageEntry.setStatus("current")
_CfprApEtherServerIntFIoFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApEtherServerIntFIoFsmStageInstanceId_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageInstanceId = _CfprApEtherServerIntFIoFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 1),
    _CfprApEtherServerIntFIoFsmStageInstanceId_Type()
)
cfprApEtherServerIntFIoFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageInstanceId.setStatus("current")
_CfprApEtherServerIntFIoFsmStageDn_Type = CfprApManagedObjectDn
_CfprApEtherServerIntFIoFsmStageDn_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageDn = _CfprApEtherServerIntFIoFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 2),
    _CfprApEtherServerIntFIoFsmStageDn_Type()
)
cfprApEtherServerIntFIoFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageDn.setStatus("current")
_CfprApEtherServerIntFIoFsmStageRn_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmStageRn_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageRn = _CfprApEtherServerIntFIoFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 3),
    _CfprApEtherServerIntFIoFsmStageRn_Type()
)
cfprApEtherServerIntFIoFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageRn.setStatus("current")
_CfprApEtherServerIntFIoFsmStageDescrData_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmStageDescrData_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageDescrData = _CfprApEtherServerIntFIoFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 4),
    _CfprApEtherServerIntFIoFsmStageDescrData_Type()
)
cfprApEtherServerIntFIoFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageDescrData.setStatus("current")
_CfprApEtherServerIntFIoFsmStageLastUpdateTime_Type = DateAndTime
_CfprApEtherServerIntFIoFsmStageLastUpdateTime_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageLastUpdateTime = _CfprApEtherServerIntFIoFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 5),
    _CfprApEtherServerIntFIoFsmStageLastUpdateTime_Type()
)
cfprApEtherServerIntFIoFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageLastUpdateTime.setStatus("current")
_CfprApEtherServerIntFIoFsmStageName_Type = CfprApEtherServerIntFIoFsmStageName
_CfprApEtherServerIntFIoFsmStageName_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageName = _CfprApEtherServerIntFIoFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 6),
    _CfprApEtherServerIntFIoFsmStageName_Type()
)
cfprApEtherServerIntFIoFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageName.setStatus("current")
_CfprApEtherServerIntFIoFsmStageOrder_Type = Gauge32
_CfprApEtherServerIntFIoFsmStageOrder_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageOrder = _CfprApEtherServerIntFIoFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 7),
    _CfprApEtherServerIntFIoFsmStageOrder_Type()
)
cfprApEtherServerIntFIoFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageOrder.setStatus("current")
_CfprApEtherServerIntFIoFsmStageRetry_Type = Gauge32
_CfprApEtherServerIntFIoFsmStageRetry_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageRetry = _CfprApEtherServerIntFIoFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 8),
    _CfprApEtherServerIntFIoFsmStageRetry_Type()
)
cfprApEtherServerIntFIoFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageRetry.setStatus("current")
_CfprApEtherServerIntFIoFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApEtherServerIntFIoFsmStageStageStatus_Object = MibTableColumn
cfprApEtherServerIntFIoFsmStageStageStatus = _CfprApEtherServerIntFIoFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 27, 1, 9),
    _CfprApEtherServerIntFIoFsmStageStageStatus_Type()
)
cfprApEtherServerIntFIoFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmStageStageStatus.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskTable_Object = MibTable
cfprApEtherServerIntFIoFsmTaskTable = _CfprApEtherServerIntFIoFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28)
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskTable.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskEntry_Object = MibTableRow
cfprApEtherServerIntFIoFsmTaskEntry = _CfprApEtherServerIntFIoFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1)
)
cfprApEtherServerIntFIoFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherServerIntFIoFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskEntry.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApEtherServerIntFIoFsmTaskInstanceId_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskInstanceId = _CfprApEtherServerIntFIoFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 1),
    _CfprApEtherServerIntFIoFsmTaskInstanceId_Type()
)
cfprApEtherServerIntFIoFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskInstanceId.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApEtherServerIntFIoFsmTaskDn_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskDn = _CfprApEtherServerIntFIoFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 2),
    _CfprApEtherServerIntFIoFsmTaskDn_Type()
)
cfprApEtherServerIntFIoFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskDn.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskRn_Type = SnmpAdminString
_CfprApEtherServerIntFIoFsmTaskRn_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskRn = _CfprApEtherServerIntFIoFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 3),
    _CfprApEtherServerIntFIoFsmTaskRn_Type()
)
cfprApEtherServerIntFIoFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskRn.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApEtherServerIntFIoFsmTaskCompletion_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskCompletion = _CfprApEtherServerIntFIoFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 4),
    _CfprApEtherServerIntFIoFsmTaskCompletion_Type()
)
cfprApEtherServerIntFIoFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskCompletion.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskFlags_Type = CfprApFsmFlags
_CfprApEtherServerIntFIoFsmTaskFlags_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskFlags = _CfprApEtherServerIntFIoFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 5),
    _CfprApEtherServerIntFIoFsmTaskFlags_Type()
)
cfprApEtherServerIntFIoFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskFlags.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskItem_Type = CfprApEtherServerIntFIoFsmTaskItem
_CfprApEtherServerIntFIoFsmTaskItem_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskItem = _CfprApEtherServerIntFIoFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 6),
    _CfprApEtherServerIntFIoFsmTaskItem_Type()
)
cfprApEtherServerIntFIoFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskItem.setStatus("current")
_CfprApEtherServerIntFIoFsmTaskSeqId_Type = Gauge32
_CfprApEtherServerIntFIoFsmTaskSeqId_Object = MibTableColumn
cfprApEtherServerIntFIoFsmTaskSeqId = _CfprApEtherServerIntFIoFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 28, 1, 7),
    _CfprApEtherServerIntFIoFsmTaskSeqId_Type()
)
cfprApEtherServerIntFIoFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoFsmTaskSeqId.setStatus("current")
_CfprApEtherServerIntFIoPcTable_Object = MibTable
cfprApEtherServerIntFIoPcTable = _CfprApEtherServerIntFIoPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29)
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcTable.setStatus("current")
_CfprApEtherServerIntFIoPcEntry_Object = MibTableRow
cfprApEtherServerIntFIoPcEntry = _CfprApEtherServerIntFIoPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1)
)
cfprApEtherServerIntFIoPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherServerIntFIoPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEntry.setStatus("current")
_CfprApEtherServerIntFIoPcInstanceId_Type = CfprApManagedObjectId
_CfprApEtherServerIntFIoPcInstanceId_Object = MibTableColumn
cfprApEtherServerIntFIoPcInstanceId = _CfprApEtherServerIntFIoPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 1),
    _CfprApEtherServerIntFIoPcInstanceId_Type()
)
cfprApEtherServerIntFIoPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcInstanceId.setStatus("current")
_CfprApEtherServerIntFIoPcDn_Type = CfprApManagedObjectDn
_CfprApEtherServerIntFIoPcDn_Object = MibTableColumn
cfprApEtherServerIntFIoPcDn = _CfprApEtherServerIntFIoPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 2),
    _CfprApEtherServerIntFIoPcDn_Type()
)
cfprApEtherServerIntFIoPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcDn.setStatus("current")
_CfprApEtherServerIntFIoPcRn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcRn_Object = MibTableColumn
cfprApEtherServerIntFIoPcRn = _CfprApEtherServerIntFIoPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 3),
    _CfprApEtherServerIntFIoPcRn_Type()
)
cfprApEtherServerIntFIoPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcRn.setStatus("current")
_CfprApEtherServerIntFIoPcChassisId_Type = Gauge32
_CfprApEtherServerIntFIoPcChassisId_Object = MibTableColumn
cfprApEtherServerIntFIoPcChassisId = _CfprApEtherServerIntFIoPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 4),
    _CfprApEtherServerIntFIoPcChassisId_Type()
)
cfprApEtherServerIntFIoPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcChassisId.setStatus("current")
_CfprApEtherServerIntFIoPcEpDn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcEpDn_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpDn = _CfprApEtherServerIntFIoPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 5),
    _CfprApEtherServerIntFIoPcEpDn_Type()
)
cfprApEtherServerIntFIoPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpDn.setStatus("current")
_CfprApEtherServerIntFIoPcFltAggr_Type = Unsigned64
_CfprApEtherServerIntFIoPcFltAggr_Object = MibTableColumn
cfprApEtherServerIntFIoPcFltAggr = _CfprApEtherServerIntFIoPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 6),
    _CfprApEtherServerIntFIoPcFltAggr_Type()
)
cfprApEtherServerIntFIoPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcFltAggr.setStatus("current")
_CfprApEtherServerIntFIoPcIfRole_Type = CfprApEtherServerIntFIoPcIfRole
_CfprApEtherServerIntFIoPcIfRole_Object = MibTableColumn
cfprApEtherServerIntFIoPcIfRole = _CfprApEtherServerIntFIoPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 7),
    _CfprApEtherServerIntFIoPcIfRole_Type()
)
cfprApEtherServerIntFIoPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcIfRole.setStatus("current")
_CfprApEtherServerIntFIoPcIfType_Type = CfprApEtherCIoEpIfType
_CfprApEtherServerIntFIoPcIfType_Object = MibTableColumn
cfprApEtherServerIntFIoPcIfType = _CfprApEtherServerIntFIoPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 8),
    _CfprApEtherServerIntFIoPcIfType_Type()
)
cfprApEtherServerIntFIoPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcIfType.setStatus("current")
_CfprApEtherServerIntFIoPcLocale_Type = CfprApEtherInternalPcLocale
_CfprApEtherServerIntFIoPcLocale_Object = MibTableColumn
cfprApEtherServerIntFIoPcLocale = _CfprApEtherServerIntFIoPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 9),
    _CfprApEtherServerIntFIoPcLocale_Type()
)
cfprApEtherServerIntFIoPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcLocale.setStatus("current")
_CfprApEtherServerIntFIoPcName_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcName_Object = MibTableColumn
cfprApEtherServerIntFIoPcName = _CfprApEtherServerIntFIoPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 10),
    _CfprApEtherServerIntFIoPcName_Type()
)
cfprApEtherServerIntFIoPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcName.setStatus("current")
_CfprApEtherServerIntFIoPcOperSpeed_Type = CfprApPortEthSpeed
_CfprApEtherServerIntFIoPcOperSpeed_Object = MibTableColumn
cfprApEtherServerIntFIoPcOperSpeed = _CfprApEtherServerIntFIoPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 11),
    _CfprApEtherServerIntFIoPcOperSpeed_Type()
)
cfprApEtherServerIntFIoPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcOperSpeed.setStatus("current")
_CfprApEtherServerIntFIoPcOperState_Type = CfprApNetworkPortOperState
_CfprApEtherServerIntFIoPcOperState_Object = MibTableColumn
cfprApEtherServerIntFIoPcOperState = _CfprApEtherServerIntFIoPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 12),
    _CfprApEtherServerIntFIoPcOperState_Type()
)
cfprApEtherServerIntFIoPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcOperState.setStatus("current")
_CfprApEtherServerIntFIoPcPeerDn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcPeerDn_Object = MibTableColumn
cfprApEtherServerIntFIoPcPeerDn = _CfprApEtherServerIntFIoPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 13),
    _CfprApEtherServerIntFIoPcPeerDn_Type()
)
cfprApEtherServerIntFIoPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcPeerDn.setStatus("current")
_CfprApEtherServerIntFIoPcPortId_Type = CfprApEtherServerIntFIoPcPortId
_CfprApEtherServerIntFIoPcPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPcPortId = _CfprApEtherServerIntFIoPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 14),
    _CfprApEtherServerIntFIoPcPortId_Type()
)
cfprApEtherServerIntFIoPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcPortId.setStatus("current")
_CfprApEtherServerIntFIoPcStateQual_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcStateQual_Object = MibTableColumn
cfprApEtherServerIntFIoPcStateQual = _CfprApEtherServerIntFIoPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 15),
    _CfprApEtherServerIntFIoPcStateQual_Type()
)
cfprApEtherServerIntFIoPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcStateQual.setStatus("current")
_CfprApEtherServerIntFIoPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherServerIntFIoPcSwitchId_Object = MibTableColumn
cfprApEtherServerIntFIoPcSwitchId = _CfprApEtherServerIntFIoPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 16),
    _CfprApEtherServerIntFIoPcSwitchId_Type()
)
cfprApEtherServerIntFIoPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcSwitchId.setStatus("current")
_CfprApEtherServerIntFIoPcTransport_Type = CfprApEtherServerIntFIoPcTransport
_CfprApEtherServerIntFIoPcTransport_Object = MibTableColumn
cfprApEtherServerIntFIoPcTransport = _CfprApEtherServerIntFIoPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 17),
    _CfprApEtherServerIntFIoPcTransport_Type()
)
cfprApEtherServerIntFIoPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcTransport.setStatus("current")
_CfprApEtherServerIntFIoPcType_Type = CfprApEtherServerIntFIoPcType
_CfprApEtherServerIntFIoPcType_Object = MibTableColumn
cfprApEtherServerIntFIoPcType = _CfprApEtherServerIntFIoPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 29, 1, 18),
    _CfprApEtherServerIntFIoPcType_Type()
)
cfprApEtherServerIntFIoPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcType.setStatus("current")
_CfprApEtherServerIntFIoPcEpTable_Object = MibTable
cfprApEtherServerIntFIoPcEpTable = _CfprApEtherServerIntFIoPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30)
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpTable.setStatus("current")
_CfprApEtherServerIntFIoPcEpEntry_Object = MibTableRow
cfprApEtherServerIntFIoPcEpEntry = _CfprApEtherServerIntFIoPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1)
)
cfprApEtherServerIntFIoPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherServerIntFIoPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpEntry.setStatus("current")
_CfprApEtherServerIntFIoPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApEtherServerIntFIoPcEpInstanceId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpInstanceId = _CfprApEtherServerIntFIoPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 1),
    _CfprApEtherServerIntFIoPcEpInstanceId_Type()
)
cfprApEtherServerIntFIoPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpInstanceId.setStatus("current")
_CfprApEtherServerIntFIoPcEpDnData_Type = CfprApManagedObjectDn
_CfprApEtherServerIntFIoPcEpDnData_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpDnData = _CfprApEtherServerIntFIoPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 2),
    _CfprApEtherServerIntFIoPcEpDnData_Type()
)
cfprApEtherServerIntFIoPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpDnData.setStatus("current")
_CfprApEtherServerIntFIoPcEpRn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcEpRn_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpRn = _CfprApEtherServerIntFIoPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 3),
    _CfprApEtherServerIntFIoPcEpRn_Type()
)
cfprApEtherServerIntFIoPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpRn.setStatus("current")
_CfprApEtherServerIntFIoPcEpAdminState_Type = CfprApEtherExternalEpAdminState
_CfprApEtherServerIntFIoPcEpAdminState_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpAdminState = _CfprApEtherServerIntFIoPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 4),
    _CfprApEtherServerIntFIoPcEpAdminState_Type()
)
cfprApEtherServerIntFIoPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpAdminState.setStatus("current")
_CfprApEtherServerIntFIoPcEpAggrPortId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpAggrPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpAggrPortId = _CfprApEtherServerIntFIoPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 5),
    _CfprApEtherServerIntFIoPcEpAggrPortId_Type()
)
cfprApEtherServerIntFIoPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpAggrPortId.setStatus("current")
_CfprApEtherServerIntFIoPcEpChassisId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpChassisId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpChassisId = _CfprApEtherServerIntFIoPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 6),
    _CfprApEtherServerIntFIoPcEpChassisId_Type()
)
cfprApEtherServerIntFIoPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpChassisId.setStatus("current")
_CfprApEtherServerIntFIoPcEpEpDn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcEpEpDn_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpEpDn = _CfprApEtherServerIntFIoPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 7),
    _CfprApEtherServerIntFIoPcEpEpDn_Type()
)
cfprApEtherServerIntFIoPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpEpDn.setStatus("current")
_CfprApEtherServerIntFIoPcEpIfRole_Type = CfprApEtherServerIntFIoPcEpIfRole
_CfprApEtherServerIntFIoPcEpIfRole_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpIfRole = _CfprApEtherServerIntFIoPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 8),
    _CfprApEtherServerIntFIoPcEpIfRole_Type()
)
cfprApEtherServerIntFIoPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpIfRole.setStatus("current")
_CfprApEtherServerIntFIoPcEpIfType_Type = CfprApEtherPIoEpIfType
_CfprApEtherServerIntFIoPcEpIfType_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpIfType = _CfprApEtherServerIntFIoPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 9),
    _CfprApEtherServerIntFIoPcEpIfType_Type()
)
cfprApEtherServerIntFIoPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpIfType.setStatus("current")
_CfprApEtherServerIntFIoPcEpLocale_Type = CfprApEtherExternalEpLocale
_CfprApEtherServerIntFIoPcEpLocale_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpLocale = _CfprApEtherServerIntFIoPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 10),
    _CfprApEtherServerIntFIoPcEpLocale_Type()
)
cfprApEtherServerIntFIoPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpLocale.setStatus("current")
_CfprApEtherServerIntFIoPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApEtherServerIntFIoPcEpMembership_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpMembership = _CfprApEtherServerIntFIoPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 11),
    _CfprApEtherServerIntFIoPcEpMembership_Type()
)
cfprApEtherServerIntFIoPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpMembership.setStatus("current")
_CfprApEtherServerIntFIoPcEpName_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcEpName_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpName = _CfprApEtherServerIntFIoPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 12),
    _CfprApEtherServerIntFIoPcEpName_Type()
)
cfprApEtherServerIntFIoPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpName.setStatus("current")
_CfprApEtherServerIntFIoPcEpPeerAggrPortId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpPeerAggrPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpPeerAggrPortId = _CfprApEtherServerIntFIoPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 13),
    _CfprApEtherServerIntFIoPcEpPeerAggrPortId_Type()
)
cfprApEtherServerIntFIoPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpPeerAggrPortId.setStatus("current")
_CfprApEtherServerIntFIoPcEpPeerChassisId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpPeerChassisId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpPeerChassisId = _CfprApEtherServerIntFIoPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 14),
    _CfprApEtherServerIntFIoPcEpPeerChassisId_Type()
)
cfprApEtherServerIntFIoPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpPeerChassisId.setStatus("current")
_CfprApEtherServerIntFIoPcEpPeerDn_Type = SnmpAdminString
_CfprApEtherServerIntFIoPcEpPeerDn_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpPeerDn = _CfprApEtherServerIntFIoPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 15),
    _CfprApEtherServerIntFIoPcEpPeerDn_Type()
)
cfprApEtherServerIntFIoPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpPeerDn.setStatus("current")
_CfprApEtherServerIntFIoPcEpPeerPortId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpPeerPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpPeerPortId = _CfprApEtherServerIntFIoPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 16),
    _CfprApEtherServerIntFIoPcEpPeerPortId_Type()
)
cfprApEtherServerIntFIoPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpPeerPortId.setStatus("current")
_CfprApEtherServerIntFIoPcEpPeerSlotId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpPeerSlotId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpPeerSlotId = _CfprApEtherServerIntFIoPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 17),
    _CfprApEtherServerIntFIoPcEpPeerSlotId_Type()
)
cfprApEtherServerIntFIoPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpPeerSlotId.setStatus("current")
_CfprApEtherServerIntFIoPcEpPortId_Type = CfprApEtherServerIntFIoPcEpPortId
_CfprApEtherServerIntFIoPcEpPortId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpPortId = _CfprApEtherServerIntFIoPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 18),
    _CfprApEtherServerIntFIoPcEpPortId_Type()
)
cfprApEtherServerIntFIoPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpPortId.setStatus("current")
_CfprApEtherServerIntFIoPcEpSlotId_Type = Gauge32
_CfprApEtherServerIntFIoPcEpSlotId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpSlotId = _CfprApEtherServerIntFIoPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 19),
    _CfprApEtherServerIntFIoPcEpSlotId_Type()
)
cfprApEtherServerIntFIoPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpSlotId.setStatus("current")
_CfprApEtherServerIntFIoPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherServerIntFIoPcEpSwitchId_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpSwitchId = _CfprApEtherServerIntFIoPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 20),
    _CfprApEtherServerIntFIoPcEpSwitchId_Type()
)
cfprApEtherServerIntFIoPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpSwitchId.setStatus("current")
_CfprApEtherServerIntFIoPcEpTransport_Type = CfprApNetworkTransport
_CfprApEtherServerIntFIoPcEpTransport_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpTransport = _CfprApEtherServerIntFIoPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 21),
    _CfprApEtherServerIntFIoPcEpTransport_Type()
)
cfprApEtherServerIntFIoPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpTransport.setStatus("current")
_CfprApEtherServerIntFIoPcEpType_Type = CfprApEtherIntFIoEpType
_CfprApEtherServerIntFIoPcEpType_Object = MibTableColumn
cfprApEtherServerIntFIoPcEpType = _CfprApEtherServerIntFIoPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 30, 1, 22),
    _CfprApEtherServerIntFIoPcEpType_Type()
)
cfprApEtherServerIntFIoPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherServerIntFIoPcEpType.setStatus("current")
_CfprApEtherSwIfConfigTable_Object = MibTable
cfprApEtherSwIfConfigTable = _CfprApEtherSwIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 31)
)
if mibBuilder.loadTexts:
    cfprApEtherSwIfConfigTable.setStatus("current")
_CfprApEtherSwIfConfigEntry_Object = MibTableRow
cfprApEtherSwIfConfigEntry = _CfprApEtherSwIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 31, 1)
)
cfprApEtherSwIfConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherSwIfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherSwIfConfigEntry.setStatus("current")
_CfprApEtherSwIfConfigInstanceId_Type = CfprApManagedObjectId
_CfprApEtherSwIfConfigInstanceId_Object = MibTableColumn
cfprApEtherSwIfConfigInstanceId = _CfprApEtherSwIfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 31, 1, 1),
    _CfprApEtherSwIfConfigInstanceId_Type()
)
cfprApEtherSwIfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherSwIfConfigInstanceId.setStatus("current")
_CfprApEtherSwIfConfigDn_Type = CfprApManagedObjectDn
_CfprApEtherSwIfConfigDn_Object = MibTableColumn
cfprApEtherSwIfConfigDn = _CfprApEtherSwIfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 31, 1, 2),
    _CfprApEtherSwIfConfigDn_Type()
)
cfprApEtherSwIfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwIfConfigDn.setStatus("current")
_CfprApEtherSwIfConfigRn_Type = SnmpAdminString
_CfprApEtherSwIfConfigRn_Object = MibTableColumn
cfprApEtherSwIfConfigRn = _CfprApEtherSwIfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 31, 1, 3),
    _CfprApEtherSwIfConfigRn_Type()
)
cfprApEtherSwIfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwIfConfigRn.setStatus("current")
_CfprApEtherSwitchIntFIoTable_Object = MibTable
cfprApEtherSwitchIntFIoTable = _CfprApEtherSwitchIntFIoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32)
)
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoTable.setStatus("current")
_CfprApEtherSwitchIntFIoEntry_Object = MibTableRow
cfprApEtherSwitchIntFIoEntry = _CfprApEtherSwitchIntFIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1)
)
cfprApEtherSwitchIntFIoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherSwitchIntFIoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoEntry.setStatus("current")
_CfprApEtherSwitchIntFIoInstanceId_Type = CfprApManagedObjectId
_CfprApEtherSwitchIntFIoInstanceId_Object = MibTableColumn
cfprApEtherSwitchIntFIoInstanceId = _CfprApEtherSwitchIntFIoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 1),
    _CfprApEtherSwitchIntFIoInstanceId_Type()
)
cfprApEtherSwitchIntFIoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoInstanceId.setStatus("current")
_CfprApEtherSwitchIntFIoDn_Type = CfprApManagedObjectDn
_CfprApEtherSwitchIntFIoDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoDn = _CfprApEtherSwitchIntFIoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 2),
    _CfprApEtherSwitchIntFIoDn_Type()
)
cfprApEtherSwitchIntFIoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoDn.setStatus("current")
_CfprApEtherSwitchIntFIoRn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoRn_Object = MibTableColumn
cfprApEtherSwitchIntFIoRn = _CfprApEtherSwitchIntFIoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 3),
    _CfprApEtherSwitchIntFIoRn_Type()
)
cfprApEtherSwitchIntFIoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoRn.setStatus("current")
_CfprApEtherSwitchIntFIoAck_Type = CfprApEtherSwitchIntFIoAck
_CfprApEtherSwitchIntFIoAck_Object = MibTableColumn
cfprApEtherSwitchIntFIoAck = _CfprApEtherSwitchIntFIoAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 4),
    _CfprApEtherSwitchIntFIoAck_Type()
)
cfprApEtherSwitchIntFIoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoAck.setStatus("current")
_CfprApEtherSwitchIntFIoAdminState_Type = CfprApFabricAdminState
_CfprApEtherSwitchIntFIoAdminState_Object = MibTableColumn
cfprApEtherSwitchIntFIoAdminState = _CfprApEtherSwitchIntFIoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 5),
    _CfprApEtherSwitchIntFIoAdminState_Type()
)
cfprApEtherSwitchIntFIoAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoAdminState.setStatus("current")
_CfprApEtherSwitchIntFIoAggrPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoAggrPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoAggrPortId = _CfprApEtherSwitchIntFIoAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 6),
    _CfprApEtherSwitchIntFIoAggrPortId_Type()
)
cfprApEtherSwitchIntFIoAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoAggrPortId.setStatus("current")
_CfprApEtherSwitchIntFIoChassisId_Type = Gauge32
_CfprApEtherSwitchIntFIoChassisId_Object = MibTableColumn
cfprApEtherSwitchIntFIoChassisId = _CfprApEtherSwitchIntFIoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 7),
    _CfprApEtherSwitchIntFIoChassisId_Type()
)
cfprApEtherSwitchIntFIoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoChassisId.setStatus("current")
_CfprApEtherSwitchIntFIoDelFeTs_Type = Unsigned64
_CfprApEtherSwitchIntFIoDelFeTs_Object = MibTableColumn
cfprApEtherSwitchIntFIoDelFeTs = _CfprApEtherSwitchIntFIoDelFeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 8),
    _CfprApEtherSwitchIntFIoDelFeTs_Type()
)
cfprApEtherSwitchIntFIoDelFeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoDelFeTs.setStatus("current")
_CfprApEtherSwitchIntFIoDiscovery_Type = CfprApEtherSatelliteConnectionDisc
_CfprApEtherSwitchIntFIoDiscovery_Object = MibTableColumn
cfprApEtherSwitchIntFIoDiscovery = _CfprApEtherSwitchIntFIoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 9),
    _CfprApEtherSwitchIntFIoDiscovery_Type()
)
cfprApEtherSwitchIntFIoDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoDiscovery.setStatus("current")
_CfprApEtherSwitchIntFIoEncap_Type = CfprApPortEncap
_CfprApEtherSwitchIntFIoEncap_Object = MibTableColumn
cfprApEtherSwitchIntFIoEncap = _CfprApEtherSwitchIntFIoEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 10),
    _CfprApEtherSwitchIntFIoEncap_Type()
)
cfprApEtherSwitchIntFIoEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoEncap.setStatus("current")
_CfprApEtherSwitchIntFIoEpDn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoEpDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoEpDn = _CfprApEtherSwitchIntFIoEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 11),
    _CfprApEtherSwitchIntFIoEpDn_Type()
)
cfprApEtherSwitchIntFIoEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoEpDn.setStatus("current")
_CfprApEtherSwitchIntFIoFltAggr_Type = Unsigned64
_CfprApEtherSwitchIntFIoFltAggr_Object = MibTableColumn
cfprApEtherSwitchIntFIoFltAggr = _CfprApEtherSwitchIntFIoFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 12),
    _CfprApEtherSwitchIntFIoFltAggr_Type()
)
cfprApEtherSwitchIntFIoFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoFltAggr.setStatus("current")
_CfprApEtherSwitchIntFIoIfRole_Type = CfprApEtherSwitchIntFIoIfRole
_CfprApEtherSwitchIntFIoIfRole_Object = MibTableColumn
cfprApEtherSwitchIntFIoIfRole = _CfprApEtherSwitchIntFIoIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 13),
    _CfprApEtherSwitchIntFIoIfRole_Type()
)
cfprApEtherSwitchIntFIoIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoIfRole.setStatus("current")
_CfprApEtherSwitchIntFIoIfType_Type = CfprApNetworkPhysEpIfType
_CfprApEtherSwitchIntFIoIfType_Object = MibTableColumn
cfprApEtherSwitchIntFIoIfType = _CfprApEtherSwitchIntFIoIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 14),
    _CfprApEtherSwitchIntFIoIfType_Type()
)
cfprApEtherSwitchIntFIoIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoIfType.setStatus("current")
_CfprApEtherSwitchIntFIoLocale_Type = CfprApEtherSwitchIntFIoLocale
_CfprApEtherSwitchIntFIoLocale_Object = MibTableColumn
cfprApEtherSwitchIntFIoLocale = _CfprApEtherSwitchIntFIoLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 15),
    _CfprApEtherSwitchIntFIoLocale_Type()
)
cfprApEtherSwitchIntFIoLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoLocale.setStatus("current")
_CfprApEtherSwitchIntFIoMode_Type = CfprApPortMode
_CfprApEtherSwitchIntFIoMode_Object = MibTableColumn
cfprApEtherSwitchIntFIoMode = _CfprApEtherSwitchIntFIoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 16),
    _CfprApEtherSwitchIntFIoMode_Type()
)
cfprApEtherSwitchIntFIoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoMode.setStatus("current")
_CfprApEtherSwitchIntFIoModel_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoModel_Object = MibTableColumn
cfprApEtherSwitchIntFIoModel = _CfprApEtherSwitchIntFIoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 17),
    _CfprApEtherSwitchIntFIoModel_Type()
)
cfprApEtherSwitchIntFIoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoModel.setStatus("current")
_CfprApEtherSwitchIntFIoName_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoName_Object = MibTableColumn
cfprApEtherSwitchIntFIoName = _CfprApEtherSwitchIntFIoName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 18),
    _CfprApEtherSwitchIntFIoName_Type()
)
cfprApEtherSwitchIntFIoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoName.setStatus("current")
_CfprApEtherSwitchIntFIoNewFeTs_Type = Unsigned64
_CfprApEtherSwitchIntFIoNewFeTs_Object = MibTableColumn
cfprApEtherSwitchIntFIoNewFeTs = _CfprApEtherSwitchIntFIoNewFeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 19),
    _CfprApEtherSwitchIntFIoNewFeTs_Type()
)
cfprApEtherSwitchIntFIoNewFeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoNewFeTs.setStatus("current")
_CfprApEtherSwitchIntFIoOperState_Type = CfprApNetworkPortOperState
_CfprApEtherSwitchIntFIoOperState_Object = MibTableColumn
cfprApEtherSwitchIntFIoOperState = _CfprApEtherSwitchIntFIoOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 20),
    _CfprApEtherSwitchIntFIoOperState_Type()
)
cfprApEtherSwitchIntFIoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoOperState.setStatus("current")
_CfprApEtherSwitchIntFIoPeerAggrPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoPeerAggrPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPeerAggrPortId = _CfprApEtherSwitchIntFIoPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 21),
    _CfprApEtherSwitchIntFIoPeerAggrPortId_Type()
)
cfprApEtherSwitchIntFIoPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPeerAggrPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPeerChassisId_Type = Gauge32
_CfprApEtherSwitchIntFIoPeerChassisId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPeerChassisId = _CfprApEtherSwitchIntFIoPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 22),
    _CfprApEtherSwitchIntFIoPeerChassisId_Type()
)
cfprApEtherSwitchIntFIoPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPeerChassisId.setStatus("current")
_CfprApEtherSwitchIntFIoPeerDn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPeerDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPeerDn = _CfprApEtherSwitchIntFIoPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 23),
    _CfprApEtherSwitchIntFIoPeerDn_Type()
)
cfprApEtherSwitchIntFIoPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPeerDn.setStatus("current")
_CfprApEtherSwitchIntFIoPeerPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoPeerPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPeerPortId = _CfprApEtherSwitchIntFIoPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 24),
    _CfprApEtherSwitchIntFIoPeerPortId_Type()
)
cfprApEtherSwitchIntFIoPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPeerPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPeerSlotId_Type = Gauge32
_CfprApEtherSwitchIntFIoPeerSlotId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPeerSlotId = _CfprApEtherSwitchIntFIoPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 25),
    _CfprApEtherSwitchIntFIoPeerSlotId_Type()
)
cfprApEtherSwitchIntFIoPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPeerSlotId.setStatus("current")
_CfprApEtherSwitchIntFIoPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPortId = _CfprApEtherSwitchIntFIoPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 26),
    _CfprApEtherSwitchIntFIoPortId_Type()
)
cfprApEtherSwitchIntFIoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPortId.setStatus("current")
_CfprApEtherSwitchIntFIoRevision_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoRevision_Object = MibTableColumn
cfprApEtherSwitchIntFIoRevision = _CfprApEtherSwitchIntFIoRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 27),
    _CfprApEtherSwitchIntFIoRevision_Type()
)
cfprApEtherSwitchIntFIoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoRevision.setStatus("current")
_CfprApEtherSwitchIntFIoSerial_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoSerial_Object = MibTableColumn
cfprApEtherSwitchIntFIoSerial = _CfprApEtherSwitchIntFIoSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 28),
    _CfprApEtherSwitchIntFIoSerial_Type()
)
cfprApEtherSwitchIntFIoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoSerial.setStatus("current")
_CfprApEtherSwitchIntFIoSlotId_Type = Gauge32
_CfprApEtherSwitchIntFIoSlotId_Object = MibTableColumn
cfprApEtherSwitchIntFIoSlotId = _CfprApEtherSwitchIntFIoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 29),
    _CfprApEtherSwitchIntFIoSlotId_Type()
)
cfprApEtherSwitchIntFIoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoSlotId.setStatus("current")
_CfprApEtherSwitchIntFIoStateQual_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoStateQual_Object = MibTableColumn
cfprApEtherSwitchIntFIoStateQual = _CfprApEtherSwitchIntFIoStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 30),
    _CfprApEtherSwitchIntFIoStateQual_Type()
)
cfprApEtherSwitchIntFIoStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoStateQual.setStatus("current")
_CfprApEtherSwitchIntFIoSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherSwitchIntFIoSwitchId_Object = MibTableColumn
cfprApEtherSwitchIntFIoSwitchId = _CfprApEtherSwitchIntFIoSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 31),
    _CfprApEtherSwitchIntFIoSwitchId_Type()
)
cfprApEtherSwitchIntFIoSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoSwitchId.setStatus("current")
_CfprApEtherSwitchIntFIoTransport_Type = CfprApEtherSwitchIntFIoTransport
_CfprApEtherSwitchIntFIoTransport_Object = MibTableColumn
cfprApEtherSwitchIntFIoTransport = _CfprApEtherSwitchIntFIoTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 32),
    _CfprApEtherSwitchIntFIoTransport_Type()
)
cfprApEtherSwitchIntFIoTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoTransport.setStatus("current")
_CfprApEtherSwitchIntFIoTs_Type = DateAndTime
_CfprApEtherSwitchIntFIoTs_Object = MibTableColumn
cfprApEtherSwitchIntFIoTs = _CfprApEtherSwitchIntFIoTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 33),
    _CfprApEtherSwitchIntFIoTs_Type()
)
cfprApEtherSwitchIntFIoTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoTs.setStatus("current")
_CfprApEtherSwitchIntFIoType_Type = CfprApEtherSwitchIntFIoType
_CfprApEtherSwitchIntFIoType_Object = MibTableColumn
cfprApEtherSwitchIntFIoType = _CfprApEtherSwitchIntFIoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 34),
    _CfprApEtherSwitchIntFIoType_Type()
)
cfprApEtherSwitchIntFIoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoType.setStatus("current")
_CfprApEtherSwitchIntFIoVendor_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoVendor_Object = MibTableColumn
cfprApEtherSwitchIntFIoVendor = _CfprApEtherSwitchIntFIoVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 35),
    _CfprApEtherSwitchIntFIoVendor_Type()
)
cfprApEtherSwitchIntFIoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoVendor.setStatus("current")
_CfprApEtherSwitchIntFIoXcvrType_Type = CfprApEquipmentXcvrType
_CfprApEtherSwitchIntFIoXcvrType_Object = MibTableColumn
cfprApEtherSwitchIntFIoXcvrType = _CfprApEtherSwitchIntFIoXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 32, 1, 36),
    _CfprApEtherSwitchIntFIoXcvrType_Type()
)
cfprApEtherSwitchIntFIoXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoXcvrType.setStatus("current")
_CfprApEtherSwitchIntFIoPcTable_Object = MibTable
cfprApEtherSwitchIntFIoPcTable = _CfprApEtherSwitchIntFIoPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33)
)
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcTable.setStatus("current")
_CfprApEtherSwitchIntFIoPcEntry_Object = MibTableRow
cfprApEtherSwitchIntFIoPcEntry = _CfprApEtherSwitchIntFIoPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1)
)
cfprApEtherSwitchIntFIoPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherSwitchIntFIoPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEntry.setStatus("current")
_CfprApEtherSwitchIntFIoPcInstanceId_Type = CfprApManagedObjectId
_CfprApEtherSwitchIntFIoPcInstanceId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcInstanceId = _CfprApEtherSwitchIntFIoPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 1),
    _CfprApEtherSwitchIntFIoPcInstanceId_Type()
)
cfprApEtherSwitchIntFIoPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcInstanceId.setStatus("current")
_CfprApEtherSwitchIntFIoPcDn_Type = CfprApManagedObjectDn
_CfprApEtherSwitchIntFIoPcDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcDn = _CfprApEtherSwitchIntFIoPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 2),
    _CfprApEtherSwitchIntFIoPcDn_Type()
)
cfprApEtherSwitchIntFIoPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcDn.setStatus("current")
_CfprApEtherSwitchIntFIoPcRn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcRn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcRn = _CfprApEtherSwitchIntFIoPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 3),
    _CfprApEtherSwitchIntFIoPcRn_Type()
)
cfprApEtherSwitchIntFIoPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcRn.setStatus("current")
_CfprApEtherSwitchIntFIoPcAdminState_Type = CfprApEtherExternalPcAdminState
_CfprApEtherSwitchIntFIoPcAdminState_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcAdminState = _CfprApEtherSwitchIntFIoPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 4),
    _CfprApEtherSwitchIntFIoPcAdminState_Type()
)
cfprApEtherSwitchIntFIoPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcAdminState.setStatus("current")
_CfprApEtherSwitchIntFIoPcChassisId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcChassisId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcChassisId = _CfprApEtherSwitchIntFIoPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 5),
    _CfprApEtherSwitchIntFIoPcChassisId_Type()
)
cfprApEtherSwitchIntFIoPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcChassisId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpDn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcEpDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpDn = _CfprApEtherSwitchIntFIoPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 6),
    _CfprApEtherSwitchIntFIoPcEpDn_Type()
)
cfprApEtherSwitchIntFIoPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpDn.setStatus("current")
_CfprApEtherSwitchIntFIoPcFltAggr_Type = Unsigned64
_CfprApEtherSwitchIntFIoPcFltAggr_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcFltAggr = _CfprApEtherSwitchIntFIoPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 7),
    _CfprApEtherSwitchIntFIoPcFltAggr_Type()
)
cfprApEtherSwitchIntFIoPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcFltAggr.setStatus("current")
_CfprApEtherSwitchIntFIoPcIfRole_Type = CfprApEtherSwitchIntFIoPcIfRole
_CfprApEtherSwitchIntFIoPcIfRole_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcIfRole = _CfprApEtherSwitchIntFIoPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 8),
    _CfprApEtherSwitchIntFIoPcIfRole_Type()
)
cfprApEtherSwitchIntFIoPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcIfRole.setStatus("current")
_CfprApEtherSwitchIntFIoPcIfType_Type = CfprApEtherCIoEpIfType
_CfprApEtherSwitchIntFIoPcIfType_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcIfType = _CfprApEtherSwitchIntFIoPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 9),
    _CfprApEtherSwitchIntFIoPcIfType_Type()
)
cfprApEtherSwitchIntFIoPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcIfType.setStatus("current")
_CfprApEtherSwitchIntFIoPcLocale_Type = CfprApEtherExternalPcLocale
_CfprApEtherSwitchIntFIoPcLocale_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcLocale = _CfprApEtherSwitchIntFIoPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 10),
    _CfprApEtherSwitchIntFIoPcLocale_Type()
)
cfprApEtherSwitchIntFIoPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcLocale.setStatus("current")
_CfprApEtherSwitchIntFIoPcName_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcName_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcName = _CfprApEtherSwitchIntFIoPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 11),
    _CfprApEtherSwitchIntFIoPcName_Type()
)
cfprApEtherSwitchIntFIoPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcName.setStatus("current")
_CfprApEtherSwitchIntFIoPcOperSpeed_Type = CfprApPortEthSpeed
_CfprApEtherSwitchIntFIoPcOperSpeed_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcOperSpeed = _CfprApEtherSwitchIntFIoPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 12),
    _CfprApEtherSwitchIntFIoPcOperSpeed_Type()
)
cfprApEtherSwitchIntFIoPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcOperSpeed.setStatus("current")
_CfprApEtherSwitchIntFIoPcOperState_Type = CfprApNetworkPortOperState
_CfprApEtherSwitchIntFIoPcOperState_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcOperState = _CfprApEtherSwitchIntFIoPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 13),
    _CfprApEtherSwitchIntFIoPcOperState_Type()
)
cfprApEtherSwitchIntFIoPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcOperState.setStatus("current")
_CfprApEtherSwitchIntFIoPcPeerDn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcPeerDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcPeerDn = _CfprApEtherSwitchIntFIoPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 14),
    _CfprApEtherSwitchIntFIoPcPeerDn_Type()
)
cfprApEtherSwitchIntFIoPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcPeerDn.setStatus("current")
_CfprApEtherSwitchIntFIoPcPortId_Type = CfprApEtherSwitchIntFIoPcPortId
_CfprApEtherSwitchIntFIoPcPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcPortId = _CfprApEtherSwitchIntFIoPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 15),
    _CfprApEtherSwitchIntFIoPcPortId_Type()
)
cfprApEtherSwitchIntFIoPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPcStateQual_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcStateQual_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcStateQual = _CfprApEtherSwitchIntFIoPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 16),
    _CfprApEtherSwitchIntFIoPcStateQual_Type()
)
cfprApEtherSwitchIntFIoPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcStateQual.setStatus("current")
_CfprApEtherSwitchIntFIoPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherSwitchIntFIoPcSwitchId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcSwitchId = _CfprApEtherSwitchIntFIoPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 17),
    _CfprApEtherSwitchIntFIoPcSwitchId_Type()
)
cfprApEtherSwitchIntFIoPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcSwitchId.setStatus("current")
_CfprApEtherSwitchIntFIoPcTransport_Type = CfprApEtherSwitchIntFIoPcTransport
_CfprApEtherSwitchIntFIoPcTransport_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcTransport = _CfprApEtherSwitchIntFIoPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 18),
    _CfprApEtherSwitchIntFIoPcTransport_Type()
)
cfprApEtherSwitchIntFIoPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcTransport.setStatus("current")
_CfprApEtherSwitchIntFIoPcType_Type = CfprApEtherSwitchIntFIoPcType
_CfprApEtherSwitchIntFIoPcType_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcType = _CfprApEtherSwitchIntFIoPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 33, 1, 19),
    _CfprApEtherSwitchIntFIoPcType_Type()
)
cfprApEtherSwitchIntFIoPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcType.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpTable_Object = MibTable
cfprApEtherSwitchIntFIoPcEpTable = _CfprApEtherSwitchIntFIoPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34)
)
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpTable.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpEntry_Object = MibTableRow
cfprApEtherSwitchIntFIoPcEpEntry = _CfprApEtherSwitchIntFIoPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1)
)
cfprApEtherSwitchIntFIoPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherSwitchIntFIoPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpEntry.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApEtherSwitchIntFIoPcEpInstanceId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpInstanceId = _CfprApEtherSwitchIntFIoPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 1),
    _CfprApEtherSwitchIntFIoPcEpInstanceId_Type()
)
cfprApEtherSwitchIntFIoPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpInstanceId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpDnData_Type = CfprApManagedObjectDn
_CfprApEtherSwitchIntFIoPcEpDnData_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpDnData = _CfprApEtherSwitchIntFIoPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 2),
    _CfprApEtherSwitchIntFIoPcEpDnData_Type()
)
cfprApEtherSwitchIntFIoPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpDnData.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpRn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcEpRn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpRn = _CfprApEtherSwitchIntFIoPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 3),
    _CfprApEtherSwitchIntFIoPcEpRn_Type()
)
cfprApEtherSwitchIntFIoPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpRn.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpAckState_Type = CfprApEquipmentChassisConfigState
_CfprApEtherSwitchIntFIoPcEpAckState_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpAckState = _CfprApEtherSwitchIntFIoPcEpAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 4),
    _CfprApEtherSwitchIntFIoPcEpAckState_Type()
)
cfprApEtherSwitchIntFIoPcEpAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpAckState.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpAdminState_Type = CfprApEtherExternalEpAdminState
_CfprApEtherSwitchIntFIoPcEpAdminState_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpAdminState = _CfprApEtherSwitchIntFIoPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 5),
    _CfprApEtherSwitchIntFIoPcEpAdminState_Type()
)
cfprApEtherSwitchIntFIoPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpAdminState.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpAggrPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpAggrPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpAggrPortId = _CfprApEtherSwitchIntFIoPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 6),
    _CfprApEtherSwitchIntFIoPcEpAggrPortId_Type()
)
cfprApEtherSwitchIntFIoPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpAggrPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpChassisId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpChassisId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpChassisId = _CfprApEtherSwitchIntFIoPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 7),
    _CfprApEtherSwitchIntFIoPcEpChassisId_Type()
)
cfprApEtherSwitchIntFIoPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpChassisId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpEpDn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcEpEpDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpEpDn = _CfprApEtherSwitchIntFIoPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 8),
    _CfprApEtherSwitchIntFIoPcEpEpDn_Type()
)
cfprApEtherSwitchIntFIoPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpEpDn.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpIfRole_Type = CfprApEtherSwitchIntFIoPcEpIfRole
_CfprApEtherSwitchIntFIoPcEpIfRole_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpIfRole = _CfprApEtherSwitchIntFIoPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 9),
    _CfprApEtherSwitchIntFIoPcEpIfRole_Type()
)
cfprApEtherSwitchIntFIoPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpIfRole.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpIfType_Type = CfprApEtherPIoEpIfType
_CfprApEtherSwitchIntFIoPcEpIfType_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpIfType = _CfprApEtherSwitchIntFIoPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 10),
    _CfprApEtherSwitchIntFIoPcEpIfType_Type()
)
cfprApEtherSwitchIntFIoPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpIfType.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpLocale_Type = CfprApEtherExternalEpLocale
_CfprApEtherSwitchIntFIoPcEpLocale_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpLocale = _CfprApEtherSwitchIntFIoPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 11),
    _CfprApEtherSwitchIntFIoPcEpLocale_Type()
)
cfprApEtherSwitchIntFIoPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpLocale.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApEtherSwitchIntFIoPcEpMembership_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpMembership = _CfprApEtherSwitchIntFIoPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 12),
    _CfprApEtherSwitchIntFIoPcEpMembership_Type()
)
cfprApEtherSwitchIntFIoPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpMembership.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpName_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcEpName_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpName = _CfprApEtherSwitchIntFIoPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 13),
    _CfprApEtherSwitchIntFIoPcEpName_Type()
)
cfprApEtherSwitchIntFIoPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpName.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpPeerAggrPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpPeerAggrPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpPeerAggrPortId = _CfprApEtherSwitchIntFIoPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 14),
    _CfprApEtherSwitchIntFIoPcEpPeerAggrPortId_Type()
)
cfprApEtherSwitchIntFIoPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpPeerAggrPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpPeerChassisId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpPeerChassisId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpPeerChassisId = _CfprApEtherSwitchIntFIoPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 15),
    _CfprApEtherSwitchIntFIoPcEpPeerChassisId_Type()
)
cfprApEtherSwitchIntFIoPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpPeerChassisId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpPeerDn_Type = SnmpAdminString
_CfprApEtherSwitchIntFIoPcEpPeerDn_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpPeerDn = _CfprApEtherSwitchIntFIoPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 16),
    _CfprApEtherSwitchIntFIoPcEpPeerDn_Type()
)
cfprApEtherSwitchIntFIoPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpPeerDn.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpPeerPortId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpPeerPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpPeerPortId = _CfprApEtherSwitchIntFIoPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 17),
    _CfprApEtherSwitchIntFIoPcEpPeerPortId_Type()
)
cfprApEtherSwitchIntFIoPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpPeerPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpPeerSlotId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpPeerSlotId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpPeerSlotId = _CfprApEtherSwitchIntFIoPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 18),
    _CfprApEtherSwitchIntFIoPcEpPeerSlotId_Type()
)
cfprApEtherSwitchIntFIoPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpPeerSlotId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpPortId_Type = CfprApEtherSwitchIntFIoPcEpPortId
_CfprApEtherSwitchIntFIoPcEpPortId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpPortId = _CfprApEtherSwitchIntFIoPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 19),
    _CfprApEtherSwitchIntFIoPcEpPortId_Type()
)
cfprApEtherSwitchIntFIoPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpPortId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpSlotId_Type = Gauge32
_CfprApEtherSwitchIntFIoPcEpSlotId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpSlotId = _CfprApEtherSwitchIntFIoPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 20),
    _CfprApEtherSwitchIntFIoPcEpSlotId_Type()
)
cfprApEtherSwitchIntFIoPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpSlotId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpStatusChangeTs_Type = DateAndTime
_CfprApEtherSwitchIntFIoPcEpStatusChangeTs_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpStatusChangeTs = _CfprApEtherSwitchIntFIoPcEpStatusChangeTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 21),
    _CfprApEtherSwitchIntFIoPcEpStatusChangeTs_Type()
)
cfprApEtherSwitchIntFIoPcEpStatusChangeTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpStatusChangeTs.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApEtherSwitchIntFIoPcEpSwitchId_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpSwitchId = _CfprApEtherSwitchIntFIoPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 22),
    _CfprApEtherSwitchIntFIoPcEpSwitchId_Type()
)
cfprApEtherSwitchIntFIoPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpSwitchId.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpTransport_Type = CfprApNetworkTransport
_CfprApEtherSwitchIntFIoPcEpTransport_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpTransport = _CfprApEtherSwitchIntFIoPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 23),
    _CfprApEtherSwitchIntFIoPcEpTransport_Type()
)
cfprApEtherSwitchIntFIoPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpTransport.setStatus("current")
_CfprApEtherSwitchIntFIoPcEpType_Type = CfprApEtherIntFIoEpType
_CfprApEtherSwitchIntFIoPcEpType_Object = MibTableColumn
cfprApEtherSwitchIntFIoPcEpType = _CfprApEtherSwitchIntFIoPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 34, 1, 24),
    _CfprApEtherSwitchIntFIoPcEpType_Type()
)
cfprApEtherSwitchIntFIoPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherSwitchIntFIoPcEpType.setStatus("current")
_CfprApEtherTxStatsTable_Object = MibTable
cfprApEtherTxStatsTable = _CfprApEtherTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35)
)
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTable.setStatus("current")
_CfprApEtherTxStatsEntry_Object = MibTableRow
cfprApEtherTxStatsEntry = _CfprApEtherTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1)
)
cfprApEtherTxStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherTxStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherTxStatsEntry.setStatus("current")
_CfprApEtherTxStatsInstanceId_Type = CfprApManagedObjectId
_CfprApEtherTxStatsInstanceId_Object = MibTableColumn
cfprApEtherTxStatsInstanceId = _CfprApEtherTxStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 1),
    _CfprApEtherTxStatsInstanceId_Type()
)
cfprApEtherTxStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsInstanceId.setStatus("current")
_CfprApEtherTxStatsDn_Type = CfprApManagedObjectDn
_CfprApEtherTxStatsDn_Object = MibTableColumn
cfprApEtherTxStatsDn = _CfprApEtherTxStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 2),
    _CfprApEtherTxStatsDn_Type()
)
cfprApEtherTxStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsDn.setStatus("current")
_CfprApEtherTxStatsRn_Type = SnmpAdminString
_CfprApEtherTxStatsRn_Object = MibTableColumn
cfprApEtherTxStatsRn = _CfprApEtherTxStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 3),
    _CfprApEtherTxStatsRn_Type()
)
cfprApEtherTxStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsRn.setStatus("current")
_CfprApEtherTxStatsBroadcastPackets_Type = Unsigned64
_CfprApEtherTxStatsBroadcastPackets_Object = MibTableColumn
cfprApEtherTxStatsBroadcastPackets = _CfprApEtherTxStatsBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 4),
    _CfprApEtherTxStatsBroadcastPackets_Type()
)
cfprApEtherTxStatsBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsBroadcastPackets.setStatus("current")
_CfprApEtherTxStatsBroadcastPacketsDelta_Type = Counter64
_CfprApEtherTxStatsBroadcastPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsBroadcastPacketsDelta = _CfprApEtherTxStatsBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 5),
    _CfprApEtherTxStatsBroadcastPacketsDelta_Type()
)
cfprApEtherTxStatsBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsBroadcastPacketsDelta.setStatus("current")
_CfprApEtherTxStatsBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsBroadcastPacketsDeltaAvg = _CfprApEtherTxStatsBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 6),
    _CfprApEtherTxStatsBroadcastPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsBroadcastPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsBroadcastPacketsDeltaMax = _CfprApEtherTxStatsBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 7),
    _CfprApEtherTxStatsBroadcastPacketsDeltaMax_Type()
)
cfprApEtherTxStatsBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsBroadcastPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsBroadcastPacketsDeltaMin = _CfprApEtherTxStatsBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 8),
    _CfprApEtherTxStatsBroadcastPacketsDeltaMin_Type()
)
cfprApEtherTxStatsBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsBroadcastPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsIntervals_Type = Gauge32
_CfprApEtherTxStatsIntervals_Object = MibTableColumn
cfprApEtherTxStatsIntervals = _CfprApEtherTxStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 9),
    _CfprApEtherTxStatsIntervals_Type()
)
cfprApEtherTxStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsIntervals.setStatus("current")
_CfprApEtherTxStatsJumboPackets_Type = Unsigned64
_CfprApEtherTxStatsJumboPackets_Object = MibTableColumn
cfprApEtherTxStatsJumboPackets = _CfprApEtherTxStatsJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 10),
    _CfprApEtherTxStatsJumboPackets_Type()
)
cfprApEtherTxStatsJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsJumboPackets.setStatus("current")
_CfprApEtherTxStatsJumboPacketsDelta_Type = Counter64
_CfprApEtherTxStatsJumboPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsJumboPacketsDelta = _CfprApEtherTxStatsJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 11),
    _CfprApEtherTxStatsJumboPacketsDelta_Type()
)
cfprApEtherTxStatsJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsJumboPacketsDelta.setStatus("current")
_CfprApEtherTxStatsJumboPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsJumboPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsJumboPacketsDeltaAvg = _CfprApEtherTxStatsJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 12),
    _CfprApEtherTxStatsJumboPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsJumboPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsJumboPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsJumboPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsJumboPacketsDeltaMax = _CfprApEtherTxStatsJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 13),
    _CfprApEtherTxStatsJumboPacketsDeltaMax_Type()
)
cfprApEtherTxStatsJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsJumboPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsJumboPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsJumboPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsJumboPacketsDeltaMin = _CfprApEtherTxStatsJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 14),
    _CfprApEtherTxStatsJumboPacketsDeltaMin_Type()
)
cfprApEtherTxStatsJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsJumboPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsMulticastPackets_Type = Unsigned64
_CfprApEtherTxStatsMulticastPackets_Object = MibTableColumn
cfprApEtherTxStatsMulticastPackets = _CfprApEtherTxStatsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 15),
    _CfprApEtherTxStatsMulticastPackets_Type()
)
cfprApEtherTxStatsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsMulticastPackets.setStatus("current")
_CfprApEtherTxStatsMulticastPacketsDelta_Type = Counter64
_CfprApEtherTxStatsMulticastPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsMulticastPacketsDelta = _CfprApEtherTxStatsMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 16),
    _CfprApEtherTxStatsMulticastPacketsDelta_Type()
)
cfprApEtherTxStatsMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsMulticastPacketsDelta.setStatus("current")
_CfprApEtherTxStatsMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsMulticastPacketsDeltaAvg = _CfprApEtherTxStatsMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 17),
    _CfprApEtherTxStatsMulticastPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsMulticastPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsMulticastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsMulticastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsMulticastPacketsDeltaMax = _CfprApEtherTxStatsMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 18),
    _CfprApEtherTxStatsMulticastPacketsDeltaMax_Type()
)
cfprApEtherTxStatsMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsMulticastPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsMulticastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsMulticastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsMulticastPacketsDeltaMin = _CfprApEtherTxStatsMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 19),
    _CfprApEtherTxStatsMulticastPacketsDeltaMin_Type()
)
cfprApEtherTxStatsMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsMulticastPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsSuspect_Type = TruthValue
_CfprApEtherTxStatsSuspect_Object = MibTableColumn
cfprApEtherTxStatsSuspect = _CfprApEtherTxStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 20),
    _CfprApEtherTxStatsSuspect_Type()
)
cfprApEtherTxStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsSuspect.setStatus("current")
_CfprApEtherTxStatsThresholded_Type = CfprApEtherTxStatsThresholded
_CfprApEtherTxStatsThresholded_Object = MibTableColumn
cfprApEtherTxStatsThresholded = _CfprApEtherTxStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 21),
    _CfprApEtherTxStatsThresholded_Type()
)
cfprApEtherTxStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsThresholded.setStatus("current")
_CfprApEtherTxStatsTimeCollected_Type = DateAndTime
_CfprApEtherTxStatsTimeCollected_Object = MibTableColumn
cfprApEtherTxStatsTimeCollected = _CfprApEtherTxStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 22),
    _CfprApEtherTxStatsTimeCollected_Type()
)
cfprApEtherTxStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTimeCollected.setStatus("current")
_CfprApEtherTxStatsTotalBytes_Type = Unsigned64
_CfprApEtherTxStatsTotalBytes_Object = MibTableColumn
cfprApEtherTxStatsTotalBytes = _CfprApEtherTxStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 23),
    _CfprApEtherTxStatsTotalBytes_Type()
)
cfprApEtherTxStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalBytes.setStatus("current")
_CfprApEtherTxStatsTotalBytesDelta_Type = Counter64
_CfprApEtherTxStatsTotalBytesDelta_Object = MibTableColumn
cfprApEtherTxStatsTotalBytesDelta = _CfprApEtherTxStatsTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 24),
    _CfprApEtherTxStatsTotalBytesDelta_Type()
)
cfprApEtherTxStatsTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalBytesDelta.setStatus("current")
_CfprApEtherTxStatsTotalBytesDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsTotalBytesDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsTotalBytesDeltaAvg = _CfprApEtherTxStatsTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 25),
    _CfprApEtherTxStatsTotalBytesDeltaAvg_Type()
)
cfprApEtherTxStatsTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalBytesDeltaAvg.setStatus("current")
_CfprApEtherTxStatsTotalBytesDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsTotalBytesDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsTotalBytesDeltaMax = _CfprApEtherTxStatsTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 26),
    _CfprApEtherTxStatsTotalBytesDeltaMax_Type()
)
cfprApEtherTxStatsTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalBytesDeltaMax.setStatus("current")
_CfprApEtherTxStatsTotalBytesDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsTotalBytesDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsTotalBytesDeltaMin = _CfprApEtherTxStatsTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 27),
    _CfprApEtherTxStatsTotalBytesDeltaMin_Type()
)
cfprApEtherTxStatsTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalBytesDeltaMin.setStatus("current")
_CfprApEtherTxStatsTotalPackets_Type = Unsigned64
_CfprApEtherTxStatsTotalPackets_Object = MibTableColumn
cfprApEtherTxStatsTotalPackets = _CfprApEtherTxStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 28),
    _CfprApEtherTxStatsTotalPackets_Type()
)
cfprApEtherTxStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalPackets.setStatus("current")
_CfprApEtherTxStatsTotalPacketsDelta_Type = Counter64
_CfprApEtherTxStatsTotalPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsTotalPacketsDelta = _CfprApEtherTxStatsTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 29),
    _CfprApEtherTxStatsTotalPacketsDelta_Type()
)
cfprApEtherTxStatsTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalPacketsDelta.setStatus("current")
_CfprApEtherTxStatsTotalPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsTotalPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsTotalPacketsDeltaAvg = _CfprApEtherTxStatsTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 30),
    _CfprApEtherTxStatsTotalPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsTotalPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsTotalPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsTotalPacketsDeltaMax = _CfprApEtherTxStatsTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 31),
    _CfprApEtherTxStatsTotalPacketsDeltaMax_Type()
)
cfprApEtherTxStatsTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsTotalPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsTotalPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsTotalPacketsDeltaMin = _CfprApEtherTxStatsTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 32),
    _CfprApEtherTxStatsTotalPacketsDeltaMin_Type()
)
cfprApEtherTxStatsTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsTotalPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsUnicastPackets_Type = Unsigned64
_CfprApEtherTxStatsUnicastPackets_Object = MibTableColumn
cfprApEtherTxStatsUnicastPackets = _CfprApEtherTxStatsUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 33),
    _CfprApEtherTxStatsUnicastPackets_Type()
)
cfprApEtherTxStatsUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsUnicastPackets.setStatus("current")
_CfprApEtherTxStatsUnicastPacketsDelta_Type = Counter64
_CfprApEtherTxStatsUnicastPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsUnicastPacketsDelta = _CfprApEtherTxStatsUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 34),
    _CfprApEtherTxStatsUnicastPacketsDelta_Type()
)
cfprApEtherTxStatsUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsUnicastPacketsDelta.setStatus("current")
_CfprApEtherTxStatsUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsUnicastPacketsDeltaAvg = _CfprApEtherTxStatsUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 35),
    _CfprApEtherTxStatsUnicastPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsUnicastPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsUnicastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsUnicastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsUnicastPacketsDeltaMax = _CfprApEtherTxStatsUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 36),
    _CfprApEtherTxStatsUnicastPacketsDeltaMax_Type()
)
cfprApEtherTxStatsUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsUnicastPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsUnicastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsUnicastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsUnicastPacketsDeltaMin = _CfprApEtherTxStatsUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 37),
    _CfprApEtherTxStatsUnicastPacketsDeltaMin_Type()
)
cfprApEtherTxStatsUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsUnicastPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsUpdate_Type = Gauge32
_CfprApEtherTxStatsUpdate_Object = MibTableColumn
cfprApEtherTxStatsUpdate = _CfprApEtherTxStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 35, 1, 38),
    _CfprApEtherTxStatsUpdate_Type()
)
cfprApEtherTxStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsUpdate.setStatus("current")
_CfprApEtherTxStatsHistTable_Object = MibTable
cfprApEtherTxStatsHistTable = _CfprApEtherTxStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36)
)
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTable.setStatus("current")
_CfprApEtherTxStatsHistEntry_Object = MibTableRow
cfprApEtherTxStatsHistEntry = _CfprApEtherTxStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1)
)
cfprApEtherTxStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-ETHER-MIB", "cfprApEtherTxStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistEntry.setStatus("current")
_CfprApEtherTxStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApEtherTxStatsHistInstanceId_Object = MibTableColumn
cfprApEtherTxStatsHistInstanceId = _CfprApEtherTxStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 1),
    _CfprApEtherTxStatsHistInstanceId_Type()
)
cfprApEtherTxStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistInstanceId.setStatus("current")
_CfprApEtherTxStatsHistDn_Type = CfprApManagedObjectDn
_CfprApEtherTxStatsHistDn_Object = MibTableColumn
cfprApEtherTxStatsHistDn = _CfprApEtherTxStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 2),
    _CfprApEtherTxStatsHistDn_Type()
)
cfprApEtherTxStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistDn.setStatus("current")
_CfprApEtherTxStatsHistRn_Type = SnmpAdminString
_CfprApEtherTxStatsHistRn_Object = MibTableColumn
cfprApEtherTxStatsHistRn = _CfprApEtherTxStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 3),
    _CfprApEtherTxStatsHistRn_Type()
)
cfprApEtherTxStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistRn.setStatus("current")
_CfprApEtherTxStatsHistBroadcastPackets_Type = Unsigned64
_CfprApEtherTxStatsHistBroadcastPackets_Object = MibTableColumn
cfprApEtherTxStatsHistBroadcastPackets = _CfprApEtherTxStatsHistBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 4),
    _CfprApEtherTxStatsHistBroadcastPackets_Type()
)
cfprApEtherTxStatsHistBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistBroadcastPackets.setStatus("current")
_CfprApEtherTxStatsHistBroadcastPacketsDelta_Type = Unsigned64
_CfprApEtherTxStatsHistBroadcastPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsHistBroadcastPacketsDelta = _CfprApEtherTxStatsHistBroadcastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 5),
    _CfprApEtherTxStatsHistBroadcastPacketsDelta_Type()
)
cfprApEtherTxStatsHistBroadcastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistBroadcastPacketsDelta.setStatus("current")
_CfprApEtherTxStatsHistBroadcastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsHistBroadcastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsHistBroadcastPacketsDeltaAvg = _CfprApEtherTxStatsHistBroadcastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 6),
    _CfprApEtherTxStatsHistBroadcastPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsHistBroadcastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistBroadcastPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsHistBroadcastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsHistBroadcastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsHistBroadcastPacketsDeltaMax = _CfprApEtherTxStatsHistBroadcastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 7),
    _CfprApEtherTxStatsHistBroadcastPacketsDeltaMax_Type()
)
cfprApEtherTxStatsHistBroadcastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistBroadcastPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsHistBroadcastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsHistBroadcastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsHistBroadcastPacketsDeltaMin = _CfprApEtherTxStatsHistBroadcastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 8),
    _CfprApEtherTxStatsHistBroadcastPacketsDeltaMin_Type()
)
cfprApEtherTxStatsHistBroadcastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistBroadcastPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsHistId_Type = Unsigned64
_CfprApEtherTxStatsHistId_Object = MibTableColumn
cfprApEtherTxStatsHistId = _CfprApEtherTxStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 9),
    _CfprApEtherTxStatsHistId_Type()
)
cfprApEtherTxStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistId.setStatus("current")
_CfprApEtherTxStatsHistJumboPackets_Type = Unsigned64
_CfprApEtherTxStatsHistJumboPackets_Object = MibTableColumn
cfprApEtherTxStatsHistJumboPackets = _CfprApEtherTxStatsHistJumboPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 10),
    _CfprApEtherTxStatsHistJumboPackets_Type()
)
cfprApEtherTxStatsHistJumboPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistJumboPackets.setStatus("current")
_CfprApEtherTxStatsHistJumboPacketsDelta_Type = Unsigned64
_CfprApEtherTxStatsHistJumboPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsHistJumboPacketsDelta = _CfprApEtherTxStatsHistJumboPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 11),
    _CfprApEtherTxStatsHistJumboPacketsDelta_Type()
)
cfprApEtherTxStatsHistJumboPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistJumboPacketsDelta.setStatus("current")
_CfprApEtherTxStatsHistJumboPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsHistJumboPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsHistJumboPacketsDeltaAvg = _CfprApEtherTxStatsHistJumboPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 12),
    _CfprApEtherTxStatsHistJumboPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsHistJumboPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistJumboPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsHistJumboPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsHistJumboPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsHistJumboPacketsDeltaMax = _CfprApEtherTxStatsHistJumboPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 13),
    _CfprApEtherTxStatsHistJumboPacketsDeltaMax_Type()
)
cfprApEtherTxStatsHistJumboPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistJumboPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsHistJumboPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsHistJumboPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsHistJumboPacketsDeltaMin = _CfprApEtherTxStatsHistJumboPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 14),
    _CfprApEtherTxStatsHistJumboPacketsDeltaMin_Type()
)
cfprApEtherTxStatsHistJumboPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistJumboPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsHistMostRecent_Type = TruthValue
_CfprApEtherTxStatsHistMostRecent_Object = MibTableColumn
cfprApEtherTxStatsHistMostRecent = _CfprApEtherTxStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 15),
    _CfprApEtherTxStatsHistMostRecent_Type()
)
cfprApEtherTxStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistMostRecent.setStatus("current")
_CfprApEtherTxStatsHistMulticastPackets_Type = Unsigned64
_CfprApEtherTxStatsHistMulticastPackets_Object = MibTableColumn
cfprApEtherTxStatsHistMulticastPackets = _CfprApEtherTxStatsHistMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 16),
    _CfprApEtherTxStatsHistMulticastPackets_Type()
)
cfprApEtherTxStatsHistMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistMulticastPackets.setStatus("current")
_CfprApEtherTxStatsHistMulticastPacketsDelta_Type = Unsigned64
_CfprApEtherTxStatsHistMulticastPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsHistMulticastPacketsDelta = _CfprApEtherTxStatsHistMulticastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 17),
    _CfprApEtherTxStatsHistMulticastPacketsDelta_Type()
)
cfprApEtherTxStatsHistMulticastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistMulticastPacketsDelta.setStatus("current")
_CfprApEtherTxStatsHistMulticastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsHistMulticastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsHistMulticastPacketsDeltaAvg = _CfprApEtherTxStatsHistMulticastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 18),
    _CfprApEtherTxStatsHistMulticastPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsHistMulticastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistMulticastPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsHistMulticastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsHistMulticastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsHistMulticastPacketsDeltaMax = _CfprApEtherTxStatsHistMulticastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 19),
    _CfprApEtherTxStatsHistMulticastPacketsDeltaMax_Type()
)
cfprApEtherTxStatsHistMulticastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistMulticastPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsHistMulticastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsHistMulticastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsHistMulticastPacketsDeltaMin = _CfprApEtherTxStatsHistMulticastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 20),
    _CfprApEtherTxStatsHistMulticastPacketsDeltaMin_Type()
)
cfprApEtherTxStatsHistMulticastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistMulticastPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsHistSuspect_Type = TruthValue
_CfprApEtherTxStatsHistSuspect_Object = MibTableColumn
cfprApEtherTxStatsHistSuspect = _CfprApEtherTxStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 21),
    _CfprApEtherTxStatsHistSuspect_Type()
)
cfprApEtherTxStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistSuspect.setStatus("current")
_CfprApEtherTxStatsHistThresholded_Type = CfprApEtherTxStatsHistThresholded
_CfprApEtherTxStatsHistThresholded_Object = MibTableColumn
cfprApEtherTxStatsHistThresholded = _CfprApEtherTxStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 22),
    _CfprApEtherTxStatsHistThresholded_Type()
)
cfprApEtherTxStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistThresholded.setStatus("current")
_CfprApEtherTxStatsHistTimeCollected_Type = DateAndTime
_CfprApEtherTxStatsHistTimeCollected_Object = MibTableColumn
cfprApEtherTxStatsHistTimeCollected = _CfprApEtherTxStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 23),
    _CfprApEtherTxStatsHistTimeCollected_Type()
)
cfprApEtherTxStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTimeCollected.setStatus("current")
_CfprApEtherTxStatsHistTotalBytes_Type = Unsigned64
_CfprApEtherTxStatsHistTotalBytes_Object = MibTableColumn
cfprApEtherTxStatsHistTotalBytes = _CfprApEtherTxStatsHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 24),
    _CfprApEtherTxStatsHistTotalBytes_Type()
)
cfprApEtherTxStatsHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalBytes.setStatus("current")
_CfprApEtherTxStatsHistTotalBytesDelta_Type = Unsigned64
_CfprApEtherTxStatsHistTotalBytesDelta_Object = MibTableColumn
cfprApEtherTxStatsHistTotalBytesDelta = _CfprApEtherTxStatsHistTotalBytesDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 25),
    _CfprApEtherTxStatsHistTotalBytesDelta_Type()
)
cfprApEtherTxStatsHistTotalBytesDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalBytesDelta.setStatus("current")
_CfprApEtherTxStatsHistTotalBytesDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsHistTotalBytesDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsHistTotalBytesDeltaAvg = _CfprApEtherTxStatsHistTotalBytesDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 26),
    _CfprApEtherTxStatsHistTotalBytesDeltaAvg_Type()
)
cfprApEtherTxStatsHistTotalBytesDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalBytesDeltaAvg.setStatus("current")
_CfprApEtherTxStatsHistTotalBytesDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsHistTotalBytesDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsHistTotalBytesDeltaMax = _CfprApEtherTxStatsHistTotalBytesDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 27),
    _CfprApEtherTxStatsHistTotalBytesDeltaMax_Type()
)
cfprApEtherTxStatsHistTotalBytesDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalBytesDeltaMax.setStatus("current")
_CfprApEtherTxStatsHistTotalBytesDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsHistTotalBytesDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsHistTotalBytesDeltaMin = _CfprApEtherTxStatsHistTotalBytesDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 28),
    _CfprApEtherTxStatsHistTotalBytesDeltaMin_Type()
)
cfprApEtherTxStatsHistTotalBytesDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalBytesDeltaMin.setStatus("current")
_CfprApEtherTxStatsHistTotalPackets_Type = Unsigned64
_CfprApEtherTxStatsHistTotalPackets_Object = MibTableColumn
cfprApEtherTxStatsHistTotalPackets = _CfprApEtherTxStatsHistTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 29),
    _CfprApEtherTxStatsHistTotalPackets_Type()
)
cfprApEtherTxStatsHistTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalPackets.setStatus("current")
_CfprApEtherTxStatsHistTotalPacketsDelta_Type = Unsigned64
_CfprApEtherTxStatsHistTotalPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsHistTotalPacketsDelta = _CfprApEtherTxStatsHistTotalPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 30),
    _CfprApEtherTxStatsHistTotalPacketsDelta_Type()
)
cfprApEtherTxStatsHistTotalPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalPacketsDelta.setStatus("current")
_CfprApEtherTxStatsHistTotalPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsHistTotalPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsHistTotalPacketsDeltaAvg = _CfprApEtherTxStatsHistTotalPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 31),
    _CfprApEtherTxStatsHistTotalPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsHistTotalPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsHistTotalPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsHistTotalPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsHistTotalPacketsDeltaMax = _CfprApEtherTxStatsHistTotalPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 32),
    _CfprApEtherTxStatsHistTotalPacketsDeltaMax_Type()
)
cfprApEtherTxStatsHistTotalPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsHistTotalPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsHistTotalPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsHistTotalPacketsDeltaMin = _CfprApEtherTxStatsHistTotalPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 33),
    _CfprApEtherTxStatsHistTotalPacketsDeltaMin_Type()
)
cfprApEtherTxStatsHistTotalPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistTotalPacketsDeltaMin.setStatus("current")
_CfprApEtherTxStatsHistUnicastPackets_Type = Unsigned64
_CfprApEtherTxStatsHistUnicastPackets_Object = MibTableColumn
cfprApEtherTxStatsHistUnicastPackets = _CfprApEtherTxStatsHistUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 34),
    _CfprApEtherTxStatsHistUnicastPackets_Type()
)
cfprApEtherTxStatsHistUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistUnicastPackets.setStatus("current")
_CfprApEtherTxStatsHistUnicastPacketsDelta_Type = Unsigned64
_CfprApEtherTxStatsHistUnicastPacketsDelta_Object = MibTableColumn
cfprApEtherTxStatsHistUnicastPacketsDelta = _CfprApEtherTxStatsHistUnicastPacketsDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 35),
    _CfprApEtherTxStatsHistUnicastPacketsDelta_Type()
)
cfprApEtherTxStatsHistUnicastPacketsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistUnicastPacketsDelta.setStatus("current")
_CfprApEtherTxStatsHistUnicastPacketsDeltaAvg_Type = Unsigned64
_CfprApEtherTxStatsHistUnicastPacketsDeltaAvg_Object = MibTableColumn
cfprApEtherTxStatsHistUnicastPacketsDeltaAvg = _CfprApEtherTxStatsHistUnicastPacketsDeltaAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 36),
    _CfprApEtherTxStatsHistUnicastPacketsDeltaAvg_Type()
)
cfprApEtherTxStatsHistUnicastPacketsDeltaAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistUnicastPacketsDeltaAvg.setStatus("current")
_CfprApEtherTxStatsHistUnicastPacketsDeltaMax_Type = Unsigned64
_CfprApEtherTxStatsHistUnicastPacketsDeltaMax_Object = MibTableColumn
cfprApEtherTxStatsHistUnicastPacketsDeltaMax = _CfprApEtherTxStatsHistUnicastPacketsDeltaMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 37),
    _CfprApEtherTxStatsHistUnicastPacketsDeltaMax_Type()
)
cfprApEtherTxStatsHistUnicastPacketsDeltaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistUnicastPacketsDeltaMax.setStatus("current")
_CfprApEtherTxStatsHistUnicastPacketsDeltaMin_Type = Unsigned64
_CfprApEtherTxStatsHistUnicastPacketsDeltaMin_Object = MibTableColumn
cfprApEtherTxStatsHistUnicastPacketsDeltaMin = _CfprApEtherTxStatsHistUnicastPacketsDeltaMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 21, 36, 1, 38),
    _CfprApEtherTxStatsHistUnicastPacketsDeltaMin_Type()
)
cfprApEtherTxStatsHistUnicastPacketsDeltaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEtherTxStatsHistUnicastPacketsDeltaMin.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-ETHER-MIB",
    **{"cfprApEtherObjects": cfprApEtherObjects,
       "cfprApEtherErrStatsTable": cfprApEtherErrStatsTable,
       "cfprApEtherErrStatsEntry": cfprApEtherErrStatsEntry,
       "cfprApEtherErrStatsInstanceId": cfprApEtherErrStatsInstanceId,
       "cfprApEtherErrStatsDn": cfprApEtherErrStatsDn,
       "cfprApEtherErrStatsRn": cfprApEtherErrStatsRn,
       "cfprApEtherErrStatsAlign": cfprApEtherErrStatsAlign,
       "cfprApEtherErrStatsAlignDelta": cfprApEtherErrStatsAlignDelta,
       "cfprApEtherErrStatsAlignDeltaAvg": cfprApEtherErrStatsAlignDeltaAvg,
       "cfprApEtherErrStatsAlignDeltaMax": cfprApEtherErrStatsAlignDeltaMax,
       "cfprApEtherErrStatsAlignDeltaMin": cfprApEtherErrStatsAlignDeltaMin,
       "cfprApEtherErrStatsDeferredTx": cfprApEtherErrStatsDeferredTx,
       "cfprApEtherErrStatsDeferredTxDelta": cfprApEtherErrStatsDeferredTxDelta,
       "cfprApEtherErrStatsDeferredTxDeltaAvg": cfprApEtherErrStatsDeferredTxDeltaAvg,
       "cfprApEtherErrStatsDeferredTxDeltaMax": cfprApEtherErrStatsDeferredTxDeltaMax,
       "cfprApEtherErrStatsDeferredTxDeltaMin": cfprApEtherErrStatsDeferredTxDeltaMin,
       "cfprApEtherErrStatsFcs": cfprApEtherErrStatsFcs,
       "cfprApEtherErrStatsFcsDelta": cfprApEtherErrStatsFcsDelta,
       "cfprApEtherErrStatsFcsDeltaAvg": cfprApEtherErrStatsFcsDeltaAvg,
       "cfprApEtherErrStatsFcsDeltaMax": cfprApEtherErrStatsFcsDeltaMax,
       "cfprApEtherErrStatsFcsDeltaMin": cfprApEtherErrStatsFcsDeltaMin,
       "cfprApEtherErrStatsIntMacRx": cfprApEtherErrStatsIntMacRx,
       "cfprApEtherErrStatsIntMacRxDelta": cfprApEtherErrStatsIntMacRxDelta,
       "cfprApEtherErrStatsIntMacRxDeltaAvg": cfprApEtherErrStatsIntMacRxDeltaAvg,
       "cfprApEtherErrStatsIntMacRxDeltaMax": cfprApEtherErrStatsIntMacRxDeltaMax,
       "cfprApEtherErrStatsIntMacRxDeltaMin": cfprApEtherErrStatsIntMacRxDeltaMin,
       "cfprApEtherErrStatsIntMacTx": cfprApEtherErrStatsIntMacTx,
       "cfprApEtherErrStatsIntMacTxDelta": cfprApEtherErrStatsIntMacTxDelta,
       "cfprApEtherErrStatsIntMacTxDeltaAvg": cfprApEtherErrStatsIntMacTxDeltaAvg,
       "cfprApEtherErrStatsIntMacTxDeltaMax": cfprApEtherErrStatsIntMacTxDeltaMax,
       "cfprApEtherErrStatsIntMacTxDeltaMin": cfprApEtherErrStatsIntMacTxDeltaMin,
       "cfprApEtherErrStatsIntervals": cfprApEtherErrStatsIntervals,
       "cfprApEtherErrStatsOutDiscard": cfprApEtherErrStatsOutDiscard,
       "cfprApEtherErrStatsOutDiscardDelta": cfprApEtherErrStatsOutDiscardDelta,
       "cfprApEtherErrStatsOutDiscardDeltaAvg": cfprApEtherErrStatsOutDiscardDeltaAvg,
       "cfprApEtherErrStatsOutDiscardDeltaMax": cfprApEtherErrStatsOutDiscardDeltaMax,
       "cfprApEtherErrStatsOutDiscardDeltaMin": cfprApEtherErrStatsOutDiscardDeltaMin,
       "cfprApEtherErrStatsRcv": cfprApEtherErrStatsRcv,
       "cfprApEtherErrStatsRcvDelta": cfprApEtherErrStatsRcvDelta,
       "cfprApEtherErrStatsRcvDeltaAvg": cfprApEtherErrStatsRcvDeltaAvg,
       "cfprApEtherErrStatsRcvDeltaMax": cfprApEtherErrStatsRcvDeltaMax,
       "cfprApEtherErrStatsRcvDeltaMin": cfprApEtherErrStatsRcvDeltaMin,
       "cfprApEtherErrStatsSuspect": cfprApEtherErrStatsSuspect,
       "cfprApEtherErrStatsThresholded": cfprApEtherErrStatsThresholded,
       "cfprApEtherErrStatsTimeCollected": cfprApEtherErrStatsTimeCollected,
       "cfprApEtherErrStatsUnderSize": cfprApEtherErrStatsUnderSize,
       "cfprApEtherErrStatsUnderSizeDelta": cfprApEtherErrStatsUnderSizeDelta,
       "cfprApEtherErrStatsUnderSizeDeltaAvg": cfprApEtherErrStatsUnderSizeDeltaAvg,
       "cfprApEtherErrStatsUnderSizeDeltaMax": cfprApEtherErrStatsUnderSizeDeltaMax,
       "cfprApEtherErrStatsUnderSizeDeltaMin": cfprApEtherErrStatsUnderSizeDeltaMin,
       "cfprApEtherErrStatsUpdate": cfprApEtherErrStatsUpdate,
       "cfprApEtherErrStatsXmit": cfprApEtherErrStatsXmit,
       "cfprApEtherErrStatsXmitDelta": cfprApEtherErrStatsXmitDelta,
       "cfprApEtherErrStatsXmitDeltaAvg": cfprApEtherErrStatsXmitDeltaAvg,
       "cfprApEtherErrStatsXmitDeltaMax": cfprApEtherErrStatsXmitDeltaMax,
       "cfprApEtherErrStatsXmitDeltaMin": cfprApEtherErrStatsXmitDeltaMin,
       "cfprApEtherErrStatsHistTable": cfprApEtherErrStatsHistTable,
       "cfprApEtherErrStatsHistEntry": cfprApEtherErrStatsHistEntry,
       "cfprApEtherErrStatsHistInstanceId": cfprApEtherErrStatsHistInstanceId,
       "cfprApEtherErrStatsHistDn": cfprApEtherErrStatsHistDn,
       "cfprApEtherErrStatsHistRn": cfprApEtherErrStatsHistRn,
       "cfprApEtherErrStatsHistAlign": cfprApEtherErrStatsHistAlign,
       "cfprApEtherErrStatsHistAlignDelta": cfprApEtherErrStatsHistAlignDelta,
       "cfprApEtherErrStatsHistAlignDeltaAvg": cfprApEtherErrStatsHistAlignDeltaAvg,
       "cfprApEtherErrStatsHistAlignDeltaMax": cfprApEtherErrStatsHistAlignDeltaMax,
       "cfprApEtherErrStatsHistAlignDeltaMin": cfprApEtherErrStatsHistAlignDeltaMin,
       "cfprApEtherErrStatsHistDeferredTx": cfprApEtherErrStatsHistDeferredTx,
       "cfprApEtherErrStatsHistDeferredTxDelta": cfprApEtherErrStatsHistDeferredTxDelta,
       "cfprApEtherErrStatsHistDeferredTxDeltaAvg": cfprApEtherErrStatsHistDeferredTxDeltaAvg,
       "cfprApEtherErrStatsHistDeferredTxDeltaMax": cfprApEtherErrStatsHistDeferredTxDeltaMax,
       "cfprApEtherErrStatsHistDeferredTxDeltaMin": cfprApEtherErrStatsHistDeferredTxDeltaMin,
       "cfprApEtherErrStatsHistFcs": cfprApEtherErrStatsHistFcs,
       "cfprApEtherErrStatsHistFcsDelta": cfprApEtherErrStatsHistFcsDelta,
       "cfprApEtherErrStatsHistFcsDeltaAvg": cfprApEtherErrStatsHistFcsDeltaAvg,
       "cfprApEtherErrStatsHistFcsDeltaMax": cfprApEtherErrStatsHistFcsDeltaMax,
       "cfprApEtherErrStatsHistFcsDeltaMin": cfprApEtherErrStatsHistFcsDeltaMin,
       "cfprApEtherErrStatsHistId": cfprApEtherErrStatsHistId,
       "cfprApEtherErrStatsHistIntMacRx": cfprApEtherErrStatsHistIntMacRx,
       "cfprApEtherErrStatsHistIntMacRxDelta": cfprApEtherErrStatsHistIntMacRxDelta,
       "cfprApEtherErrStatsHistIntMacRxDeltaAvg": cfprApEtherErrStatsHistIntMacRxDeltaAvg,
       "cfprApEtherErrStatsHistIntMacRxDeltaMax": cfprApEtherErrStatsHistIntMacRxDeltaMax,
       "cfprApEtherErrStatsHistIntMacRxDeltaMin": cfprApEtherErrStatsHistIntMacRxDeltaMin,
       "cfprApEtherErrStatsHistIntMacTx": cfprApEtherErrStatsHistIntMacTx,
       "cfprApEtherErrStatsHistIntMacTxDelta": cfprApEtherErrStatsHistIntMacTxDelta,
       "cfprApEtherErrStatsHistIntMacTxDeltaAvg": cfprApEtherErrStatsHistIntMacTxDeltaAvg,
       "cfprApEtherErrStatsHistIntMacTxDeltaMax": cfprApEtherErrStatsHistIntMacTxDeltaMax,
       "cfprApEtherErrStatsHistIntMacTxDeltaMin": cfprApEtherErrStatsHistIntMacTxDeltaMin,
       "cfprApEtherErrStatsHistMostRecent": cfprApEtherErrStatsHistMostRecent,
       "cfprApEtherErrStatsHistOutDiscard": cfprApEtherErrStatsHistOutDiscard,
       "cfprApEtherErrStatsHistOutDiscardDelta": cfprApEtherErrStatsHistOutDiscardDelta,
       "cfprApEtherErrStatsHistOutDiscardDeltaAvg": cfprApEtherErrStatsHistOutDiscardDeltaAvg,
       "cfprApEtherErrStatsHistOutDiscardDeltaMax": cfprApEtherErrStatsHistOutDiscardDeltaMax,
       "cfprApEtherErrStatsHistOutDiscardDeltaMin": cfprApEtherErrStatsHistOutDiscardDeltaMin,
       "cfprApEtherErrStatsHistRcv": cfprApEtherErrStatsHistRcv,
       "cfprApEtherErrStatsHistRcvDelta": cfprApEtherErrStatsHistRcvDelta,
       "cfprApEtherErrStatsHistRcvDeltaAvg": cfprApEtherErrStatsHistRcvDeltaAvg,
       "cfprApEtherErrStatsHistRcvDeltaMax": cfprApEtherErrStatsHistRcvDeltaMax,
       "cfprApEtherErrStatsHistRcvDeltaMin": cfprApEtherErrStatsHistRcvDeltaMin,
       "cfprApEtherErrStatsHistSuspect": cfprApEtherErrStatsHistSuspect,
       "cfprApEtherErrStatsHistThresholded": cfprApEtherErrStatsHistThresholded,
       "cfprApEtherErrStatsHistTimeCollected": cfprApEtherErrStatsHistTimeCollected,
       "cfprApEtherErrStatsHistUnderSize": cfprApEtherErrStatsHistUnderSize,
       "cfprApEtherErrStatsHistUnderSizeDelta": cfprApEtherErrStatsHistUnderSizeDelta,
       "cfprApEtherErrStatsHistUnderSizeDeltaAvg": cfprApEtherErrStatsHistUnderSizeDeltaAvg,
       "cfprApEtherErrStatsHistUnderSizeDeltaMax": cfprApEtherErrStatsHistUnderSizeDeltaMax,
       "cfprApEtherErrStatsHistUnderSizeDeltaMin": cfprApEtherErrStatsHistUnderSizeDeltaMin,
       "cfprApEtherErrStatsHistXmit": cfprApEtherErrStatsHistXmit,
       "cfprApEtherErrStatsHistXmitDelta": cfprApEtherErrStatsHistXmitDelta,
       "cfprApEtherErrStatsHistXmitDeltaAvg": cfprApEtherErrStatsHistXmitDeltaAvg,
       "cfprApEtherErrStatsHistXmitDeltaMax": cfprApEtherErrStatsHistXmitDeltaMax,
       "cfprApEtherErrStatsHistXmitDeltaMin": cfprApEtherErrStatsHistXmitDeltaMin,
       "cfprApEtherFailToWireTable": cfprApEtherFailToWireTable,
       "cfprApEtherFailToWireEntry": cfprApEtherFailToWireEntry,
       "cfprApEtherFailToWireInstanceId": cfprApEtherFailToWireInstanceId,
       "cfprApEtherFailToWireDn": cfprApEtherFailToWireDn,
       "cfprApEtherFailToWireRn": cfprApEtherFailToWireRn,
       "cfprApEtherFailToWireLocale": cfprApEtherFailToWireLocale,
       "cfprApEtherFailToWireName": cfprApEtherFailToWireName,
       "cfprApEtherFailToWireTransport": cfprApEtherFailToWireTransport,
       "cfprApEtherFailToWireType": cfprApEtherFailToWireType,
       "cfprApEtherFcoeInterfaceStatsTable": cfprApEtherFcoeInterfaceStatsTable,
       "cfprApEtherFcoeInterfaceStatsEntry": cfprApEtherFcoeInterfaceStatsEntry,
       "cfprApEtherFcoeInterfaceStatsInstanceId": cfprApEtherFcoeInterfaceStatsInstanceId,
       "cfprApEtherFcoeInterfaceStatsDn": cfprApEtherFcoeInterfaceStatsDn,
       "cfprApEtherFcoeInterfaceStatsRn": cfprApEtherFcoeInterfaceStatsRn,
       "cfprApEtherFcoeInterfaceStatsBytesRx": cfprApEtherFcoeInterfaceStatsBytesRx,
       "cfprApEtherFcoeInterfaceStatsBytesRxDelta": cfprApEtherFcoeInterfaceStatsBytesRxDelta,
       "cfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg": cfprApEtherFcoeInterfaceStatsBytesRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsBytesRxDeltaMax": cfprApEtherFcoeInterfaceStatsBytesRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsBytesRxDeltaMin": cfprApEtherFcoeInterfaceStatsBytesRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsBytesTx": cfprApEtherFcoeInterfaceStatsBytesTx,
       "cfprApEtherFcoeInterfaceStatsBytesTxDelta": cfprApEtherFcoeInterfaceStatsBytesTxDelta,
       "cfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg": cfprApEtherFcoeInterfaceStatsBytesTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsBytesTxDeltaMax": cfprApEtherFcoeInterfaceStatsBytesTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsBytesTxDeltaMin": cfprApEtherFcoeInterfaceStatsBytesTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsDroppedRx": cfprApEtherFcoeInterfaceStatsDroppedRx,
       "cfprApEtherFcoeInterfaceStatsDroppedRxDelta": cfprApEtherFcoeInterfaceStatsDroppedRxDelta,
       "cfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg": cfprApEtherFcoeInterfaceStatsDroppedRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax": cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin": cfprApEtherFcoeInterfaceStatsDroppedRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsDroppedTx": cfprApEtherFcoeInterfaceStatsDroppedTx,
       "cfprApEtherFcoeInterfaceStatsDroppedTxDelta": cfprApEtherFcoeInterfaceStatsDroppedTxDelta,
       "cfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg": cfprApEtherFcoeInterfaceStatsDroppedTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax": cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin": cfprApEtherFcoeInterfaceStatsDroppedTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsErrorsRx": cfprApEtherFcoeInterfaceStatsErrorsRx,
       "cfprApEtherFcoeInterfaceStatsErrorsRxDelta": cfprApEtherFcoeInterfaceStatsErrorsRxDelta,
       "cfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg": cfprApEtherFcoeInterfaceStatsErrorsRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax": cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin": cfprApEtherFcoeInterfaceStatsErrorsRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsErrorsTx": cfprApEtherFcoeInterfaceStatsErrorsTx,
       "cfprApEtherFcoeInterfaceStatsErrorsTxDelta": cfprApEtherFcoeInterfaceStatsErrorsTxDelta,
       "cfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg": cfprApEtherFcoeInterfaceStatsErrorsTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax": cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin": cfprApEtherFcoeInterfaceStatsErrorsTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsIntervals": cfprApEtherFcoeInterfaceStatsIntervals,
       "cfprApEtherFcoeInterfaceStatsPacketsRx": cfprApEtherFcoeInterfaceStatsPacketsRx,
       "cfprApEtherFcoeInterfaceStatsPacketsRxDelta": cfprApEtherFcoeInterfaceStatsPacketsRxDelta,
       "cfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg": cfprApEtherFcoeInterfaceStatsPacketsRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax": cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin": cfprApEtherFcoeInterfaceStatsPacketsRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsPacketsTx": cfprApEtherFcoeInterfaceStatsPacketsTx,
       "cfprApEtherFcoeInterfaceStatsPacketsTxDelta": cfprApEtherFcoeInterfaceStatsPacketsTxDelta,
       "cfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg": cfprApEtherFcoeInterfaceStatsPacketsTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax": cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin": cfprApEtherFcoeInterfaceStatsPacketsTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsSuspect": cfprApEtherFcoeInterfaceStatsSuspect,
       "cfprApEtherFcoeInterfaceStatsThresholded": cfprApEtherFcoeInterfaceStatsThresholded,
       "cfprApEtherFcoeInterfaceStatsTimeCollected": cfprApEtherFcoeInterfaceStatsTimeCollected,
       "cfprApEtherFcoeInterfaceStatsUpdate": cfprApEtherFcoeInterfaceStatsUpdate,
       "cfprApEtherFcoeInterfaceStatsHistTable": cfprApEtherFcoeInterfaceStatsHistTable,
       "cfprApEtherFcoeInterfaceStatsHistEntry": cfprApEtherFcoeInterfaceStatsHistEntry,
       "cfprApEtherFcoeInterfaceStatsHistInstanceId": cfprApEtherFcoeInterfaceStatsHistInstanceId,
       "cfprApEtherFcoeInterfaceStatsHistDn": cfprApEtherFcoeInterfaceStatsHistDn,
       "cfprApEtherFcoeInterfaceStatsHistRn": cfprApEtherFcoeInterfaceStatsHistRn,
       "cfprApEtherFcoeInterfaceStatsHistBytesRx": cfprApEtherFcoeInterfaceStatsHistBytesRx,
       "cfprApEtherFcoeInterfaceStatsHistBytesRxDelta": cfprApEtherFcoeInterfaceStatsHistBytesRxDelta,
       "cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax": cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin": cfprApEtherFcoeInterfaceStatsHistBytesRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistBytesTx": cfprApEtherFcoeInterfaceStatsHistBytesTx,
       "cfprApEtherFcoeInterfaceStatsHistBytesTxDelta": cfprApEtherFcoeInterfaceStatsHistBytesTxDelta,
       "cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax": cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin": cfprApEtherFcoeInterfaceStatsHistBytesTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistDroppedRx": cfprApEtherFcoeInterfaceStatsHistDroppedRx,
       "cfprApEtherFcoeInterfaceStatsHistDroppedRxDelta": cfprApEtherFcoeInterfaceStatsHistDroppedRxDelta,
       "cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax": cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin": cfprApEtherFcoeInterfaceStatsHistDroppedRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistDroppedTx": cfprApEtherFcoeInterfaceStatsHistDroppedTx,
       "cfprApEtherFcoeInterfaceStatsHistDroppedTxDelta": cfprApEtherFcoeInterfaceStatsHistDroppedTxDelta,
       "cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax": cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin": cfprApEtherFcoeInterfaceStatsHistDroppedTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistErrorsRx": cfprApEtherFcoeInterfaceStatsHistErrorsRx,
       "cfprApEtherFcoeInterfaceStatsHistErrorsRxDelta": cfprApEtherFcoeInterfaceStatsHistErrorsRxDelta,
       "cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax": cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin": cfprApEtherFcoeInterfaceStatsHistErrorsRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistErrorsTx": cfprApEtherFcoeInterfaceStatsHistErrorsTx,
       "cfprApEtherFcoeInterfaceStatsHistErrorsTxDelta": cfprApEtherFcoeInterfaceStatsHistErrorsTxDelta,
       "cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax": cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin": cfprApEtherFcoeInterfaceStatsHistErrorsTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistId": cfprApEtherFcoeInterfaceStatsHistId,
       "cfprApEtherFcoeInterfaceStatsHistMostRecent": cfprApEtherFcoeInterfaceStatsHistMostRecent,
       "cfprApEtherFcoeInterfaceStatsHistPacketsRx": cfprApEtherFcoeInterfaceStatsHistPacketsRx,
       "cfprApEtherFcoeInterfaceStatsHistPacketsRxDelta": cfprApEtherFcoeInterfaceStatsHistPacketsRxDelta,
       "cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax": cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin": cfprApEtherFcoeInterfaceStatsHistPacketsRxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistPacketsTx": cfprApEtherFcoeInterfaceStatsHistPacketsTx,
       "cfprApEtherFcoeInterfaceStatsHistPacketsTxDelta": cfprApEtherFcoeInterfaceStatsHistPacketsTxDelta,
       "cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg": cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaAvg,
       "cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax": cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMax,
       "cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin": cfprApEtherFcoeInterfaceStatsHistPacketsTxDeltaMin,
       "cfprApEtherFcoeInterfaceStatsHistSuspect": cfprApEtherFcoeInterfaceStatsHistSuspect,
       "cfprApEtherFcoeInterfaceStatsHistThresholded": cfprApEtherFcoeInterfaceStatsHistThresholded,
       "cfprApEtherFcoeInterfaceStatsHistTimeCollected": cfprApEtherFcoeInterfaceStatsHistTimeCollected,
       "cfprApEtherFtwPortPairTable": cfprApEtherFtwPortPairTable,
       "cfprApEtherFtwPortPairEntry": cfprApEtherFtwPortPairEntry,
       "cfprApEtherFtwPortPairInstanceId": cfprApEtherFtwPortPairInstanceId,
       "cfprApEtherFtwPortPairDn": cfprApEtherFtwPortPairDn,
       "cfprApEtherFtwPortPairRn": cfprApEtherFtwPortPairRn,
       "cfprApEtherFtwPortPairAggrPortId": cfprApEtherFtwPortPairAggrPortId,
       "cfprApEtherFtwPortPairChassisId": cfprApEtherFtwPortPairChassisId,
       "cfprApEtherFtwPortPairEpDn": cfprApEtherFtwPortPairEpDn,
       "cfprApEtherFtwPortPairFsmDescr": cfprApEtherFtwPortPairFsmDescr,
       "cfprApEtherFtwPortPairFsmPrev": cfprApEtherFtwPortPairFsmPrev,
       "cfprApEtherFtwPortPairFsmProgr": cfprApEtherFtwPortPairFsmProgr,
       "cfprApEtherFtwPortPairFsmRmtInvErrCode": cfprApEtherFtwPortPairFsmRmtInvErrCode,
       "cfprApEtherFtwPortPairFsmRmtInvErrDescr": cfprApEtherFtwPortPairFsmRmtInvErrDescr,
       "cfprApEtherFtwPortPairFsmRmtInvRslt": cfprApEtherFtwPortPairFsmRmtInvRslt,
       "cfprApEtherFtwPortPairFsmStageDescr": cfprApEtherFtwPortPairFsmStageDescr,
       "cfprApEtherFtwPortPairFsmStamp": cfprApEtherFtwPortPairFsmStamp,
       "cfprApEtherFtwPortPairFsmStatus": cfprApEtherFtwPortPairFsmStatus,
       "cfprApEtherFtwPortPairFsmTry": cfprApEtherFtwPortPairFsmTry,
       "cfprApEtherFtwPortPairIfRole": cfprApEtherFtwPortPairIfRole,
       "cfprApEtherFtwPortPairIfType": cfprApEtherFtwPortPairIfType,
       "cfprApEtherFtwPortPairLocale": cfprApEtherFtwPortPairLocale,
       "cfprApEtherFtwPortPairMode": cfprApEtherFtwPortPairMode,
       "cfprApEtherFtwPortPairName": cfprApEtherFtwPortPairName,
       "cfprApEtherFtwPortPairOperMode": cfprApEtherFtwPortPairOperMode,
       "cfprApEtherFtwPortPairPeerAggrPortId": cfprApEtherFtwPortPairPeerAggrPortId,
       "cfprApEtherFtwPortPairPeerChassisId": cfprApEtherFtwPortPairPeerChassisId,
       "cfprApEtherFtwPortPairPeerDn": cfprApEtherFtwPortPairPeerDn,
       "cfprApEtherFtwPortPairPeerPortId": cfprApEtherFtwPortPairPeerPortId,
       "cfprApEtherFtwPortPairPeerPortName": cfprApEtherFtwPortPairPeerPortName,
       "cfprApEtherFtwPortPairPeerSlotId": cfprApEtherFtwPortPairPeerSlotId,
       "cfprApEtherFtwPortPairPortId": cfprApEtherFtwPortPairPortId,
       "cfprApEtherFtwPortPairPortName": cfprApEtherFtwPortPairPortName,
       "cfprApEtherFtwPortPairSlotId": cfprApEtherFtwPortPairSlotId,
       "cfprApEtherFtwPortPairSwitchId": cfprApEtherFtwPortPairSwitchId,
       "cfprApEtherFtwPortPairTransport": cfprApEtherFtwPortPairTransport,
       "cfprApEtherFtwPortPairType": cfprApEtherFtwPortPairType,
       "cfprApEtherFtwPortPairWdtStart": cfprApEtherFtwPortPairWdtStart,
       "cfprApEtherFtwPortPairWdtState": cfprApEtherFtwPortPairWdtState,
       "cfprApEtherFtwPortPairFsmTable": cfprApEtherFtwPortPairFsmTable,
       "cfprApEtherFtwPortPairFsmEntry": cfprApEtherFtwPortPairFsmEntry,
       "cfprApEtherFtwPortPairFsmInstanceId": cfprApEtherFtwPortPairFsmInstanceId,
       "cfprApEtherFtwPortPairFsmDn": cfprApEtherFtwPortPairFsmDn,
       "cfprApEtherFtwPortPairFsmRn": cfprApEtherFtwPortPairFsmRn,
       "cfprApEtherFtwPortPairFsmCompletionTime": cfprApEtherFtwPortPairFsmCompletionTime,
       "cfprApEtherFtwPortPairFsmCurrentFsm": cfprApEtherFtwPortPairFsmCurrentFsm,
       "cfprApEtherFtwPortPairFsmDescrData": cfprApEtherFtwPortPairFsmDescrData,
       "cfprApEtherFtwPortPairFsmFsmStatus": cfprApEtherFtwPortPairFsmFsmStatus,
       "cfprApEtherFtwPortPairFsmProgress": cfprApEtherFtwPortPairFsmProgress,
       "cfprApEtherFtwPortPairFsmRmtErrCode": cfprApEtherFtwPortPairFsmRmtErrCode,
       "cfprApEtherFtwPortPairFsmRmtErrDescr": cfprApEtherFtwPortPairFsmRmtErrDescr,
       "cfprApEtherFtwPortPairFsmRmtRslt": cfprApEtherFtwPortPairFsmRmtRslt,
       "cfprApEtherFtwPortPairFsmStageTable": cfprApEtherFtwPortPairFsmStageTable,
       "cfprApEtherFtwPortPairFsmStageEntry": cfprApEtherFtwPortPairFsmStageEntry,
       "cfprApEtherFtwPortPairFsmStageInstanceId": cfprApEtherFtwPortPairFsmStageInstanceId,
       "cfprApEtherFtwPortPairFsmStageDn": cfprApEtherFtwPortPairFsmStageDn,
       "cfprApEtherFtwPortPairFsmStageRn": cfprApEtherFtwPortPairFsmStageRn,
       "cfprApEtherFtwPortPairFsmStageDescrData": cfprApEtherFtwPortPairFsmStageDescrData,
       "cfprApEtherFtwPortPairFsmStageLastUpdateTime": cfprApEtherFtwPortPairFsmStageLastUpdateTime,
       "cfprApEtherFtwPortPairFsmStageName": cfprApEtherFtwPortPairFsmStageName,
       "cfprApEtherFtwPortPairFsmStageOrder": cfprApEtherFtwPortPairFsmStageOrder,
       "cfprApEtherFtwPortPairFsmStageRetry": cfprApEtherFtwPortPairFsmStageRetry,
       "cfprApEtherFtwPortPairFsmStageStageStatus": cfprApEtherFtwPortPairFsmStageStageStatus,
       "cfprApEtherFtwPortPairFsmTaskTable": cfprApEtherFtwPortPairFsmTaskTable,
       "cfprApEtherFtwPortPairFsmTaskEntry": cfprApEtherFtwPortPairFsmTaskEntry,
       "cfprApEtherFtwPortPairFsmTaskInstanceId": cfprApEtherFtwPortPairFsmTaskInstanceId,
       "cfprApEtherFtwPortPairFsmTaskDn": cfprApEtherFtwPortPairFsmTaskDn,
       "cfprApEtherFtwPortPairFsmTaskRn": cfprApEtherFtwPortPairFsmTaskRn,
       "cfprApEtherFtwPortPairFsmTaskCompletion": cfprApEtherFtwPortPairFsmTaskCompletion,
       "cfprApEtherFtwPortPairFsmTaskFlags": cfprApEtherFtwPortPairFsmTaskFlags,
       "cfprApEtherFtwPortPairFsmTaskItem": cfprApEtherFtwPortPairFsmTaskItem,
       "cfprApEtherFtwPortPairFsmTaskSeqId": cfprApEtherFtwPortPairFsmTaskSeqId,
       "cfprApEtherLossStatsTable": cfprApEtherLossStatsTable,
       "cfprApEtherLossStatsEntry": cfprApEtherLossStatsEntry,
       "cfprApEtherLossStatsInstanceId": cfprApEtherLossStatsInstanceId,
       "cfprApEtherLossStatsDn": cfprApEtherLossStatsDn,
       "cfprApEtherLossStatsRn": cfprApEtherLossStatsRn,
       "cfprApEtherLossStatsSQETest": cfprApEtherLossStatsSQETest,
       "cfprApEtherLossStatsSQETestDelta": cfprApEtherLossStatsSQETestDelta,
       "cfprApEtherLossStatsSQETestDeltaAvg": cfprApEtherLossStatsSQETestDeltaAvg,
       "cfprApEtherLossStatsSQETestDeltaMax": cfprApEtherLossStatsSQETestDeltaMax,
       "cfprApEtherLossStatsSQETestDeltaMin": cfprApEtherLossStatsSQETestDeltaMin,
       "cfprApEtherLossStatsCarrierSense": cfprApEtherLossStatsCarrierSense,
       "cfprApEtherLossStatsCarrierSenseDelta": cfprApEtherLossStatsCarrierSenseDelta,
       "cfprApEtherLossStatsCarrierSenseDeltaAvg": cfprApEtherLossStatsCarrierSenseDeltaAvg,
       "cfprApEtherLossStatsCarrierSenseDeltaMax": cfprApEtherLossStatsCarrierSenseDeltaMax,
       "cfprApEtherLossStatsCarrierSenseDeltaMin": cfprApEtherLossStatsCarrierSenseDeltaMin,
       "cfprApEtherLossStatsExcessCollision": cfprApEtherLossStatsExcessCollision,
       "cfprApEtherLossStatsExcessCollisionDelta": cfprApEtherLossStatsExcessCollisionDelta,
       "cfprApEtherLossStatsExcessCollisionDeltaAvg": cfprApEtherLossStatsExcessCollisionDeltaAvg,
       "cfprApEtherLossStatsExcessCollisionDeltaMax": cfprApEtherLossStatsExcessCollisionDeltaMax,
       "cfprApEtherLossStatsExcessCollisionDeltaMin": cfprApEtherLossStatsExcessCollisionDeltaMin,
       "cfprApEtherLossStatsGiants": cfprApEtherLossStatsGiants,
       "cfprApEtherLossStatsGiantsDelta": cfprApEtherLossStatsGiantsDelta,
       "cfprApEtherLossStatsGiantsDeltaAvg": cfprApEtherLossStatsGiantsDeltaAvg,
       "cfprApEtherLossStatsGiantsDeltaMax": cfprApEtherLossStatsGiantsDeltaMax,
       "cfprApEtherLossStatsGiantsDeltaMin": cfprApEtherLossStatsGiantsDeltaMin,
       "cfprApEtherLossStatsIntervals": cfprApEtherLossStatsIntervals,
       "cfprApEtherLossStatsLateCollision": cfprApEtherLossStatsLateCollision,
       "cfprApEtherLossStatsLateCollisionDelta": cfprApEtherLossStatsLateCollisionDelta,
       "cfprApEtherLossStatsLateCollisionDeltaAvg": cfprApEtherLossStatsLateCollisionDeltaAvg,
       "cfprApEtherLossStatsLateCollisionDeltaMax": cfprApEtherLossStatsLateCollisionDeltaMax,
       "cfprApEtherLossStatsLateCollisionDeltaMin": cfprApEtherLossStatsLateCollisionDeltaMin,
       "cfprApEtherLossStatsMultiCollision": cfprApEtherLossStatsMultiCollision,
       "cfprApEtherLossStatsMultiCollisionDelta": cfprApEtherLossStatsMultiCollisionDelta,
       "cfprApEtherLossStatsMultiCollisionDeltaAvg": cfprApEtherLossStatsMultiCollisionDeltaAvg,
       "cfprApEtherLossStatsMultiCollisionDeltaMax": cfprApEtherLossStatsMultiCollisionDeltaMax,
       "cfprApEtherLossStatsMultiCollisionDeltaMin": cfprApEtherLossStatsMultiCollisionDeltaMin,
       "cfprApEtherLossStatsSingleCollision": cfprApEtherLossStatsSingleCollision,
       "cfprApEtherLossStatsSingleCollisionDelta": cfprApEtherLossStatsSingleCollisionDelta,
       "cfprApEtherLossStatsSingleCollisionDeltaAvg": cfprApEtherLossStatsSingleCollisionDeltaAvg,
       "cfprApEtherLossStatsSingleCollisionDeltaMax": cfprApEtherLossStatsSingleCollisionDeltaMax,
       "cfprApEtherLossStatsSingleCollisionDeltaMin": cfprApEtherLossStatsSingleCollisionDeltaMin,
       "cfprApEtherLossStatsSuspect": cfprApEtherLossStatsSuspect,
       "cfprApEtherLossStatsSymbol": cfprApEtherLossStatsSymbol,
       "cfprApEtherLossStatsSymbolDelta": cfprApEtherLossStatsSymbolDelta,
       "cfprApEtherLossStatsSymbolDeltaAvg": cfprApEtherLossStatsSymbolDeltaAvg,
       "cfprApEtherLossStatsSymbolDeltaMax": cfprApEtherLossStatsSymbolDeltaMax,
       "cfprApEtherLossStatsSymbolDeltaMin": cfprApEtherLossStatsSymbolDeltaMin,
       "cfprApEtherLossStatsThresholded": cfprApEtherLossStatsThresholded,
       "cfprApEtherLossStatsTimeCollected": cfprApEtherLossStatsTimeCollected,
       "cfprApEtherLossStatsUpdate": cfprApEtherLossStatsUpdate,
       "cfprApEtherLossStatsHistTable": cfprApEtherLossStatsHistTable,
       "cfprApEtherLossStatsHistEntry": cfprApEtherLossStatsHistEntry,
       "cfprApEtherLossStatsHistInstanceId": cfprApEtherLossStatsHistInstanceId,
       "cfprApEtherLossStatsHistDn": cfprApEtherLossStatsHistDn,
       "cfprApEtherLossStatsHistRn": cfprApEtherLossStatsHistRn,
       "cfprApEtherLossStatsHistSQETest": cfprApEtherLossStatsHistSQETest,
       "cfprApEtherLossStatsHistSQETestDelta": cfprApEtherLossStatsHistSQETestDelta,
       "cfprApEtherLossStatsHistSQETestDeltaAvg": cfprApEtherLossStatsHistSQETestDeltaAvg,
       "cfprApEtherLossStatsHistSQETestDeltaMax": cfprApEtherLossStatsHistSQETestDeltaMax,
       "cfprApEtherLossStatsHistSQETestDeltaMin": cfprApEtherLossStatsHistSQETestDeltaMin,
       "cfprApEtherLossStatsHistCarrierSense": cfprApEtherLossStatsHistCarrierSense,
       "cfprApEtherLossStatsHistCarrierSenseDelta": cfprApEtherLossStatsHistCarrierSenseDelta,
       "cfprApEtherLossStatsHistCarrierSenseDeltaAvg": cfprApEtherLossStatsHistCarrierSenseDeltaAvg,
       "cfprApEtherLossStatsHistCarrierSenseDeltaMax": cfprApEtherLossStatsHistCarrierSenseDeltaMax,
       "cfprApEtherLossStatsHistCarrierSenseDeltaMin": cfprApEtherLossStatsHistCarrierSenseDeltaMin,
       "cfprApEtherLossStatsHistExcessCollision": cfprApEtherLossStatsHistExcessCollision,
       "cfprApEtherLossStatsHistExcessCollisionDelta": cfprApEtherLossStatsHistExcessCollisionDelta,
       "cfprApEtherLossStatsHistExcessCollisionDeltaAvg": cfprApEtherLossStatsHistExcessCollisionDeltaAvg,
       "cfprApEtherLossStatsHistExcessCollisionDeltaMax": cfprApEtherLossStatsHistExcessCollisionDeltaMax,
       "cfprApEtherLossStatsHistExcessCollisionDeltaMin": cfprApEtherLossStatsHistExcessCollisionDeltaMin,
       "cfprApEtherLossStatsHistGiants": cfprApEtherLossStatsHistGiants,
       "cfprApEtherLossStatsHistGiantsDelta": cfprApEtherLossStatsHistGiantsDelta,
       "cfprApEtherLossStatsHistGiantsDeltaAvg": cfprApEtherLossStatsHistGiantsDeltaAvg,
       "cfprApEtherLossStatsHistGiantsDeltaMax": cfprApEtherLossStatsHistGiantsDeltaMax,
       "cfprApEtherLossStatsHistGiantsDeltaMin": cfprApEtherLossStatsHistGiantsDeltaMin,
       "cfprApEtherLossStatsHistId": cfprApEtherLossStatsHistId,
       "cfprApEtherLossStatsHistLateCollision": cfprApEtherLossStatsHistLateCollision,
       "cfprApEtherLossStatsHistLateCollisionDelta": cfprApEtherLossStatsHistLateCollisionDelta,
       "cfprApEtherLossStatsHistLateCollisionDeltaAvg": cfprApEtherLossStatsHistLateCollisionDeltaAvg,
       "cfprApEtherLossStatsHistLateCollisionDeltaMax": cfprApEtherLossStatsHistLateCollisionDeltaMax,
       "cfprApEtherLossStatsHistLateCollisionDeltaMin": cfprApEtherLossStatsHistLateCollisionDeltaMin,
       "cfprApEtherLossStatsHistMostRecent": cfprApEtherLossStatsHistMostRecent,
       "cfprApEtherLossStatsHistMultiCollision": cfprApEtherLossStatsHistMultiCollision,
       "cfprApEtherLossStatsHistMultiCollisionDelta": cfprApEtherLossStatsHistMultiCollisionDelta,
       "cfprApEtherLossStatsHistMultiCollisionDeltaAvg": cfprApEtherLossStatsHistMultiCollisionDeltaAvg,
       "cfprApEtherLossStatsHistMultiCollisionDeltaMax": cfprApEtherLossStatsHistMultiCollisionDeltaMax,
       "cfprApEtherLossStatsHistMultiCollisionDeltaMin": cfprApEtherLossStatsHistMultiCollisionDeltaMin,
       "cfprApEtherLossStatsHistSingleCollision": cfprApEtherLossStatsHistSingleCollision,
       "cfprApEtherLossStatsHistSingleCollisionDelta": cfprApEtherLossStatsHistSingleCollisionDelta,
       "cfprApEtherLossStatsHistSingleCollisionDeltaAvg": cfprApEtherLossStatsHistSingleCollisionDeltaAvg,
       "cfprApEtherLossStatsHistSingleCollisionDeltaMax": cfprApEtherLossStatsHistSingleCollisionDeltaMax,
       "cfprApEtherLossStatsHistSingleCollisionDeltaMin": cfprApEtherLossStatsHistSingleCollisionDeltaMin,
       "cfprApEtherLossStatsHistSuspect": cfprApEtherLossStatsHistSuspect,
       "cfprApEtherLossStatsHistSymbol": cfprApEtherLossStatsHistSymbol,
       "cfprApEtherLossStatsHistSymbolDelta": cfprApEtherLossStatsHistSymbolDelta,
       "cfprApEtherLossStatsHistSymbolDeltaAvg": cfprApEtherLossStatsHistSymbolDeltaAvg,
       "cfprApEtherLossStatsHistSymbolDeltaMax": cfprApEtherLossStatsHistSymbolDeltaMax,
       "cfprApEtherLossStatsHistSymbolDeltaMin": cfprApEtherLossStatsHistSymbolDeltaMin,
       "cfprApEtherLossStatsHistThresholded": cfprApEtherLossStatsHistThresholded,
       "cfprApEtherLossStatsHistTimeCollected": cfprApEtherLossStatsHistTimeCollected,
       "cfprApEtherNiErrStatsTable": cfprApEtherNiErrStatsTable,
       "cfprApEtherNiErrStatsEntry": cfprApEtherNiErrStatsEntry,
       "cfprApEtherNiErrStatsInstanceId": cfprApEtherNiErrStatsInstanceId,
       "cfprApEtherNiErrStatsDn": cfprApEtherNiErrStatsDn,
       "cfprApEtherNiErrStatsRn": cfprApEtherNiErrStatsRn,
       "cfprApEtherNiErrStatsCrc": cfprApEtherNiErrStatsCrc,
       "cfprApEtherNiErrStatsCrcDelta": cfprApEtherNiErrStatsCrcDelta,
       "cfprApEtherNiErrStatsCrcDeltaAvg": cfprApEtherNiErrStatsCrcDeltaAvg,
       "cfprApEtherNiErrStatsCrcDeltaMax": cfprApEtherNiErrStatsCrcDeltaMax,
       "cfprApEtherNiErrStatsCrcDeltaMin": cfprApEtherNiErrStatsCrcDeltaMin,
       "cfprApEtherNiErrStatsFrameTx": cfprApEtherNiErrStatsFrameTx,
       "cfprApEtherNiErrStatsFrameTxDelta": cfprApEtherNiErrStatsFrameTxDelta,
       "cfprApEtherNiErrStatsFrameTxDeltaAvg": cfprApEtherNiErrStatsFrameTxDeltaAvg,
       "cfprApEtherNiErrStatsFrameTxDeltaMax": cfprApEtherNiErrStatsFrameTxDeltaMax,
       "cfprApEtherNiErrStatsFrameTxDeltaMin": cfprApEtherNiErrStatsFrameTxDeltaMin,
       "cfprApEtherNiErrStatsInRange": cfprApEtherNiErrStatsInRange,
       "cfprApEtherNiErrStatsInRangeDelta": cfprApEtherNiErrStatsInRangeDelta,
       "cfprApEtherNiErrStatsInRangeDeltaAvg": cfprApEtherNiErrStatsInRangeDeltaAvg,
       "cfprApEtherNiErrStatsInRangeDeltaMax": cfprApEtherNiErrStatsInRangeDeltaMax,
       "cfprApEtherNiErrStatsInRangeDeltaMin": cfprApEtherNiErrStatsInRangeDeltaMin,
       "cfprApEtherNiErrStatsIntervals": cfprApEtherNiErrStatsIntervals,
       "cfprApEtherNiErrStatsSuspect": cfprApEtherNiErrStatsSuspect,
       "cfprApEtherNiErrStatsThresholded": cfprApEtherNiErrStatsThresholded,
       "cfprApEtherNiErrStatsTimeCollected": cfprApEtherNiErrStatsTimeCollected,
       "cfprApEtherNiErrStatsTooLong": cfprApEtherNiErrStatsTooLong,
       "cfprApEtherNiErrStatsTooLongDelta": cfprApEtherNiErrStatsTooLongDelta,
       "cfprApEtherNiErrStatsTooLongDeltaAvg": cfprApEtherNiErrStatsTooLongDeltaAvg,
       "cfprApEtherNiErrStatsTooLongDeltaMax": cfprApEtherNiErrStatsTooLongDeltaMax,
       "cfprApEtherNiErrStatsTooLongDeltaMin": cfprApEtherNiErrStatsTooLongDeltaMin,
       "cfprApEtherNiErrStatsTooShort": cfprApEtherNiErrStatsTooShort,
       "cfprApEtherNiErrStatsTooShortDelta": cfprApEtherNiErrStatsTooShortDelta,
       "cfprApEtherNiErrStatsTooShortDeltaAvg": cfprApEtherNiErrStatsTooShortDeltaAvg,
       "cfprApEtherNiErrStatsTooShortDeltaMax": cfprApEtherNiErrStatsTooShortDeltaMax,
       "cfprApEtherNiErrStatsTooShortDeltaMin": cfprApEtherNiErrStatsTooShortDeltaMin,
       "cfprApEtherNiErrStatsUpdate": cfprApEtherNiErrStatsUpdate,
       "cfprApEtherNiErrStatsHistTable": cfprApEtherNiErrStatsHistTable,
       "cfprApEtherNiErrStatsHistEntry": cfprApEtherNiErrStatsHistEntry,
       "cfprApEtherNiErrStatsHistInstanceId": cfprApEtherNiErrStatsHistInstanceId,
       "cfprApEtherNiErrStatsHistDn": cfprApEtherNiErrStatsHistDn,
       "cfprApEtherNiErrStatsHistRn": cfprApEtherNiErrStatsHistRn,
       "cfprApEtherNiErrStatsHistCrc": cfprApEtherNiErrStatsHistCrc,
       "cfprApEtherNiErrStatsHistCrcDelta": cfprApEtherNiErrStatsHistCrcDelta,
       "cfprApEtherNiErrStatsHistCrcDeltaAvg": cfprApEtherNiErrStatsHistCrcDeltaAvg,
       "cfprApEtherNiErrStatsHistCrcDeltaMax": cfprApEtherNiErrStatsHistCrcDeltaMax,
       "cfprApEtherNiErrStatsHistCrcDeltaMin": cfprApEtherNiErrStatsHistCrcDeltaMin,
       "cfprApEtherNiErrStatsHistFrameTx": cfprApEtherNiErrStatsHistFrameTx,
       "cfprApEtherNiErrStatsHistFrameTxDelta": cfprApEtherNiErrStatsHistFrameTxDelta,
       "cfprApEtherNiErrStatsHistFrameTxDeltaAvg": cfprApEtherNiErrStatsHistFrameTxDeltaAvg,
       "cfprApEtherNiErrStatsHistFrameTxDeltaMax": cfprApEtherNiErrStatsHistFrameTxDeltaMax,
       "cfprApEtherNiErrStatsHistFrameTxDeltaMin": cfprApEtherNiErrStatsHistFrameTxDeltaMin,
       "cfprApEtherNiErrStatsHistId": cfprApEtherNiErrStatsHistId,
       "cfprApEtherNiErrStatsHistInRange": cfprApEtherNiErrStatsHistInRange,
       "cfprApEtherNiErrStatsHistInRangeDelta": cfprApEtherNiErrStatsHistInRangeDelta,
       "cfprApEtherNiErrStatsHistInRangeDeltaAvg": cfprApEtherNiErrStatsHistInRangeDeltaAvg,
       "cfprApEtherNiErrStatsHistInRangeDeltaMax": cfprApEtherNiErrStatsHistInRangeDeltaMax,
       "cfprApEtherNiErrStatsHistInRangeDeltaMin": cfprApEtherNiErrStatsHistInRangeDeltaMin,
       "cfprApEtherNiErrStatsHistMostRecent": cfprApEtherNiErrStatsHistMostRecent,
       "cfprApEtherNiErrStatsHistSuspect": cfprApEtherNiErrStatsHistSuspect,
       "cfprApEtherNiErrStatsHistThresholded": cfprApEtherNiErrStatsHistThresholded,
       "cfprApEtherNiErrStatsHistTimeCollected": cfprApEtherNiErrStatsHistTimeCollected,
       "cfprApEtherNiErrStatsHistTooLong": cfprApEtherNiErrStatsHistTooLong,
       "cfprApEtherNiErrStatsHistTooLongDelta": cfprApEtherNiErrStatsHistTooLongDelta,
       "cfprApEtherNiErrStatsHistTooLongDeltaAvg": cfprApEtherNiErrStatsHistTooLongDeltaAvg,
       "cfprApEtherNiErrStatsHistTooLongDeltaMax": cfprApEtherNiErrStatsHistTooLongDeltaMax,
       "cfprApEtherNiErrStatsHistTooLongDeltaMin": cfprApEtherNiErrStatsHistTooLongDeltaMin,
       "cfprApEtherNiErrStatsHistTooShort": cfprApEtherNiErrStatsHistTooShort,
       "cfprApEtherNiErrStatsHistTooShortDelta": cfprApEtherNiErrStatsHistTooShortDelta,
       "cfprApEtherNiErrStatsHistTooShortDeltaAvg": cfprApEtherNiErrStatsHistTooShortDeltaAvg,
       "cfprApEtherNiErrStatsHistTooShortDeltaMax": cfprApEtherNiErrStatsHistTooShortDeltaMax,
       "cfprApEtherNiErrStatsHistTooShortDeltaMin": cfprApEtherNiErrStatsHistTooShortDeltaMin,
       "cfprApEtherNicIfConfigTable": cfprApEtherNicIfConfigTable,
       "cfprApEtherNicIfConfigEntry": cfprApEtherNicIfConfigEntry,
       "cfprApEtherNicIfConfigInstanceId": cfprApEtherNicIfConfigInstanceId,
       "cfprApEtherNicIfConfigDn": cfprApEtherNicIfConfigDn,
       "cfprApEtherNicIfConfigRn": cfprApEtherNicIfConfigRn,
       "cfprApEtherPIoTable": cfprApEtherPIoTable,
       "cfprApEtherPIoEntry": cfprApEtherPIoEntry,
       "cfprApEtherPIoInstanceId": cfprApEtherPIoInstanceId,
       "cfprApEtherPIoDn": cfprApEtherPIoDn,
       "cfprApEtherPIoRn": cfprApEtherPIoRn,
       "cfprApEtherPIoAdminState": cfprApEtherPIoAdminState,
       "cfprApEtherPIoAdminTransport": cfprApEtherPIoAdminTransport,
       "cfprApEtherPIoAggrPortId": cfprApEtherPIoAggrPortId,
       "cfprApEtherPIoChassisId": cfprApEtherPIoChassisId,
       "cfprApEtherPIoEncap": cfprApEtherPIoEncap,
       "cfprApEtherPIoEpDn": cfprApEtherPIoEpDn,
       "cfprApEtherPIoFltAggr": cfprApEtherPIoFltAggr,
       "cfprApEtherPIoFsmDescr": cfprApEtherPIoFsmDescr,
       "cfprApEtherPIoFsmPrev": cfprApEtherPIoFsmPrev,
       "cfprApEtherPIoFsmProgr": cfprApEtherPIoFsmProgr,
       "cfprApEtherPIoFsmRmtInvErrCode": cfprApEtherPIoFsmRmtInvErrCode,
       "cfprApEtherPIoFsmRmtInvErrDescr": cfprApEtherPIoFsmRmtInvErrDescr,
       "cfprApEtherPIoFsmRmtInvRslt": cfprApEtherPIoFsmRmtInvRslt,
       "cfprApEtherPIoFsmStageDescr": cfprApEtherPIoFsmStageDescr,
       "cfprApEtherPIoFsmStamp": cfprApEtherPIoFsmStamp,
       "cfprApEtherPIoFsmStatus": cfprApEtherPIoFsmStatus,
       "cfprApEtherPIoFsmTry": cfprApEtherPIoFsmTry,
       "cfprApEtherPIoFtwPhyDn": cfprApEtherPIoFtwPhyDn,
       "cfprApEtherPIoIfRole": cfprApEtherPIoIfRole,
       "cfprApEtherPIoIfType": cfprApEtherPIoIfType,
       "cfprApEtherPIoIsPortChannelMember": cfprApEtherPIoIsPortChannelMember,
       "cfprApEtherPIoLc": cfprApEtherPIoLc,
       "cfprApEtherPIoLicGP": cfprApEtherPIoLicGP,
       "cfprApEtherPIoLicState": cfprApEtherPIoLicState,
       "cfprApEtherPIoLocale": cfprApEtherPIoLocale,
       "cfprApEtherPIoMac": cfprApEtherPIoMac,
       "cfprApEtherPIoMode": cfprApEtherPIoMode,
       "cfprApEtherPIoModel": cfprApEtherPIoModel,
       "cfprApEtherPIoName": cfprApEtherPIoName,
       "cfprApEtherPIoOperDuplex": cfprApEtherPIoOperDuplex,
       "cfprApEtherPIoOperSpeed": cfprApEtherPIoOperSpeed,
       "cfprApEtherPIoOperState": cfprApEtherPIoOperState,
       "cfprApEtherPIoPeerAggrPortId": cfprApEtherPIoPeerAggrPortId,
       "cfprApEtherPIoPeerChassisId": cfprApEtherPIoPeerChassisId,
       "cfprApEtherPIoPeerDn": cfprApEtherPIoPeerDn,
       "cfprApEtherPIoPeerPortId": cfprApEtherPIoPeerPortId,
       "cfprApEtherPIoPeerSlotId": cfprApEtherPIoPeerSlotId,
       "cfprApEtherPIoPortId": cfprApEtherPIoPortId,
       "cfprApEtherPIoRevision": cfprApEtherPIoRevision,
       "cfprApEtherPIoSerial": cfprApEtherPIoSerial,
       "cfprApEtherPIoSlotId": cfprApEtherPIoSlotId,
       "cfprApEtherPIoStateQual": cfprApEtherPIoStateQual,
       "cfprApEtherPIoSwitchId": cfprApEtherPIoSwitchId,
       "cfprApEtherPIoTransport": cfprApEtherPIoTransport,
       "cfprApEtherPIoTs": cfprApEtherPIoTs,
       "cfprApEtherPIoType": cfprApEtherPIoType,
       "cfprApEtherPIoUnifiedPort": cfprApEtherPIoUnifiedPort,
       "cfprApEtherPIoUsrLbl": cfprApEtherPIoUsrLbl,
       "cfprApEtherPIoVendor": cfprApEtherPIoVendor,
       "cfprApEtherPIoXcvrType": cfprApEtherPIoXcvrType,
       "cfprApEtherPIoEndPointTable": cfprApEtherPIoEndPointTable,
       "cfprApEtherPIoEndPointEntry": cfprApEtherPIoEndPointEntry,
       "cfprApEtherPIoEndPointInstanceId": cfprApEtherPIoEndPointInstanceId,
       "cfprApEtherPIoEndPointDn": cfprApEtherPIoEndPointDn,
       "cfprApEtherPIoEndPointRn": cfprApEtherPIoEndPointRn,
       "cfprApEtherPIoEndPointEndPointDn": cfprApEtherPIoEndPointEndPointDn,
       "cfprApEtherPIoEndPointEpCloudType": cfprApEtherPIoEndPointEpCloudType,
       "cfprApEtherPIoEndPointUsrLbl": cfprApEtherPIoEndPointUsrLbl,
       "cfprApEtherPIoFsmTable": cfprApEtherPIoFsmTable,
       "cfprApEtherPIoFsmEntry": cfprApEtherPIoFsmEntry,
       "cfprApEtherPIoFsmInstanceId": cfprApEtherPIoFsmInstanceId,
       "cfprApEtherPIoFsmDn": cfprApEtherPIoFsmDn,
       "cfprApEtherPIoFsmRn": cfprApEtherPIoFsmRn,
       "cfprApEtherPIoFsmCompletionTime": cfprApEtherPIoFsmCompletionTime,
       "cfprApEtherPIoFsmCurrentFsm": cfprApEtherPIoFsmCurrentFsm,
       "cfprApEtherPIoFsmDescrData": cfprApEtherPIoFsmDescrData,
       "cfprApEtherPIoFsmFsmStatus": cfprApEtherPIoFsmFsmStatus,
       "cfprApEtherPIoFsmProgress": cfprApEtherPIoFsmProgress,
       "cfprApEtherPIoFsmRmtErrCode": cfprApEtherPIoFsmRmtErrCode,
       "cfprApEtherPIoFsmRmtErrDescr": cfprApEtherPIoFsmRmtErrDescr,
       "cfprApEtherPIoFsmRmtRslt": cfprApEtherPIoFsmRmtRslt,
       "cfprApEtherPIoFsmStageTable": cfprApEtherPIoFsmStageTable,
       "cfprApEtherPIoFsmStageEntry": cfprApEtherPIoFsmStageEntry,
       "cfprApEtherPIoFsmStageInstanceId": cfprApEtherPIoFsmStageInstanceId,
       "cfprApEtherPIoFsmStageDn": cfprApEtherPIoFsmStageDn,
       "cfprApEtherPIoFsmStageRn": cfprApEtherPIoFsmStageRn,
       "cfprApEtherPIoFsmStageDescrData": cfprApEtherPIoFsmStageDescrData,
       "cfprApEtherPIoFsmStageLastUpdateTime": cfprApEtherPIoFsmStageLastUpdateTime,
       "cfprApEtherPIoFsmStageName": cfprApEtherPIoFsmStageName,
       "cfprApEtherPIoFsmStageOrder": cfprApEtherPIoFsmStageOrder,
       "cfprApEtherPIoFsmStageRetry": cfprApEtherPIoFsmStageRetry,
       "cfprApEtherPIoFsmStageStageStatus": cfprApEtherPIoFsmStageStageStatus,
       "cfprApEtherPauseStatsTable": cfprApEtherPauseStatsTable,
       "cfprApEtherPauseStatsEntry": cfprApEtherPauseStatsEntry,
       "cfprApEtherPauseStatsInstanceId": cfprApEtherPauseStatsInstanceId,
       "cfprApEtherPauseStatsDn": cfprApEtherPauseStatsDn,
       "cfprApEtherPauseStatsRn": cfprApEtherPauseStatsRn,
       "cfprApEtherPauseStatsIntervals": cfprApEtherPauseStatsIntervals,
       "cfprApEtherPauseStatsRecvPause": cfprApEtherPauseStatsRecvPause,
       "cfprApEtherPauseStatsRecvPauseDelta": cfprApEtherPauseStatsRecvPauseDelta,
       "cfprApEtherPauseStatsRecvPauseDeltaAvg": cfprApEtherPauseStatsRecvPauseDeltaAvg,
       "cfprApEtherPauseStatsRecvPauseDeltaMax": cfprApEtherPauseStatsRecvPauseDeltaMax,
       "cfprApEtherPauseStatsRecvPauseDeltaMin": cfprApEtherPauseStatsRecvPauseDeltaMin,
       "cfprApEtherPauseStatsResets": cfprApEtherPauseStatsResets,
       "cfprApEtherPauseStatsResetsDelta": cfprApEtherPauseStatsResetsDelta,
       "cfprApEtherPauseStatsResetsDeltaAvg": cfprApEtherPauseStatsResetsDeltaAvg,
       "cfprApEtherPauseStatsResetsDeltaMax": cfprApEtherPauseStatsResetsDeltaMax,
       "cfprApEtherPauseStatsResetsDeltaMin": cfprApEtherPauseStatsResetsDeltaMin,
       "cfprApEtherPauseStatsSuspect": cfprApEtherPauseStatsSuspect,
       "cfprApEtherPauseStatsThresholded": cfprApEtherPauseStatsThresholded,
       "cfprApEtherPauseStatsTimeCollected": cfprApEtherPauseStatsTimeCollected,
       "cfprApEtherPauseStatsUpdate": cfprApEtherPauseStatsUpdate,
       "cfprApEtherPauseStatsXmitPause": cfprApEtherPauseStatsXmitPause,
       "cfprApEtherPauseStatsXmitPauseDelta": cfprApEtherPauseStatsXmitPauseDelta,
       "cfprApEtherPauseStatsXmitPauseDeltaAvg": cfprApEtherPauseStatsXmitPauseDeltaAvg,
       "cfprApEtherPauseStatsXmitPauseDeltaMax": cfprApEtherPauseStatsXmitPauseDeltaMax,
       "cfprApEtherPauseStatsXmitPauseDeltaMin": cfprApEtherPauseStatsXmitPauseDeltaMin,
       "cfprApEtherPauseStatsHistTable": cfprApEtherPauseStatsHistTable,
       "cfprApEtherPauseStatsHistEntry": cfprApEtherPauseStatsHistEntry,
       "cfprApEtherPauseStatsHistInstanceId": cfprApEtherPauseStatsHistInstanceId,
       "cfprApEtherPauseStatsHistDn": cfprApEtherPauseStatsHistDn,
       "cfprApEtherPauseStatsHistRn": cfprApEtherPauseStatsHistRn,
       "cfprApEtherPauseStatsHistId": cfprApEtherPauseStatsHistId,
       "cfprApEtherPauseStatsHistMostRecent": cfprApEtherPauseStatsHistMostRecent,
       "cfprApEtherPauseStatsHistRecvPause": cfprApEtherPauseStatsHistRecvPause,
       "cfprApEtherPauseStatsHistRecvPauseDelta": cfprApEtherPauseStatsHistRecvPauseDelta,
       "cfprApEtherPauseStatsHistRecvPauseDeltaAvg": cfprApEtherPauseStatsHistRecvPauseDeltaAvg,
       "cfprApEtherPauseStatsHistRecvPauseDeltaMax": cfprApEtherPauseStatsHistRecvPauseDeltaMax,
       "cfprApEtherPauseStatsHistRecvPauseDeltaMin": cfprApEtherPauseStatsHistRecvPauseDeltaMin,
       "cfprApEtherPauseStatsHistResets": cfprApEtherPauseStatsHistResets,
       "cfprApEtherPauseStatsHistResetsDelta": cfprApEtherPauseStatsHistResetsDelta,
       "cfprApEtherPauseStatsHistResetsDeltaAvg": cfprApEtherPauseStatsHistResetsDeltaAvg,
       "cfprApEtherPauseStatsHistResetsDeltaMax": cfprApEtherPauseStatsHistResetsDeltaMax,
       "cfprApEtherPauseStatsHistResetsDeltaMin": cfprApEtherPauseStatsHistResetsDeltaMin,
       "cfprApEtherPauseStatsHistSuspect": cfprApEtherPauseStatsHistSuspect,
       "cfprApEtherPauseStatsHistThresholded": cfprApEtherPauseStatsHistThresholded,
       "cfprApEtherPauseStatsHistTimeCollected": cfprApEtherPauseStatsHistTimeCollected,
       "cfprApEtherPauseStatsHistXmitPause": cfprApEtherPauseStatsHistXmitPause,
       "cfprApEtherPauseStatsHistXmitPauseDelta": cfprApEtherPauseStatsHistXmitPauseDelta,
       "cfprApEtherPauseStatsHistXmitPauseDeltaAvg": cfprApEtherPauseStatsHistXmitPauseDeltaAvg,
       "cfprApEtherPauseStatsHistXmitPauseDeltaMax": cfprApEtherPauseStatsHistXmitPauseDeltaMax,
       "cfprApEtherPauseStatsHistXmitPauseDeltaMin": cfprApEtherPauseStatsHistXmitPauseDeltaMin,
       "cfprApEtherPortChanIdElemTable": cfprApEtherPortChanIdElemTable,
       "cfprApEtherPortChanIdElemEntry": cfprApEtherPortChanIdElemEntry,
       "cfprApEtherPortChanIdElemInstanceId": cfprApEtherPortChanIdElemInstanceId,
       "cfprApEtherPortChanIdElemDn": cfprApEtherPortChanIdElemDn,
       "cfprApEtherPortChanIdElemRn": cfprApEtherPortChanIdElemRn,
       "cfprApEtherPortChanIdElemId": cfprApEtherPortChanIdElemId,
       "cfprApEtherPortChanIdUniverseTable": cfprApEtherPortChanIdUniverseTable,
       "cfprApEtherPortChanIdUniverseEntry": cfprApEtherPortChanIdUniverseEntry,
       "cfprApEtherPortChanIdUniverseInstanceId": cfprApEtherPortChanIdUniverseInstanceId,
       "cfprApEtherPortChanIdUniverseDn": cfprApEtherPortChanIdUniverseDn,
       "cfprApEtherPortChanIdUniverseRn": cfprApEtherPortChanIdUniverseRn,
       "cfprApEtherRxStatsTable": cfprApEtherRxStatsTable,
       "cfprApEtherRxStatsEntry": cfprApEtherRxStatsEntry,
       "cfprApEtherRxStatsInstanceId": cfprApEtherRxStatsInstanceId,
       "cfprApEtherRxStatsDn": cfprApEtherRxStatsDn,
       "cfprApEtherRxStatsRn": cfprApEtherRxStatsRn,
       "cfprApEtherRxStatsBroadcastPackets": cfprApEtherRxStatsBroadcastPackets,
       "cfprApEtherRxStatsBroadcastPacketsDelta": cfprApEtherRxStatsBroadcastPacketsDelta,
       "cfprApEtherRxStatsBroadcastPacketsDeltaAvg": cfprApEtherRxStatsBroadcastPacketsDeltaAvg,
       "cfprApEtherRxStatsBroadcastPacketsDeltaMax": cfprApEtherRxStatsBroadcastPacketsDeltaMax,
       "cfprApEtherRxStatsBroadcastPacketsDeltaMin": cfprApEtherRxStatsBroadcastPacketsDeltaMin,
       "cfprApEtherRxStatsIntervals": cfprApEtherRxStatsIntervals,
       "cfprApEtherRxStatsJumboPackets": cfprApEtherRxStatsJumboPackets,
       "cfprApEtherRxStatsJumboPacketsDelta": cfprApEtherRxStatsJumboPacketsDelta,
       "cfprApEtherRxStatsJumboPacketsDeltaAvg": cfprApEtherRxStatsJumboPacketsDeltaAvg,
       "cfprApEtherRxStatsJumboPacketsDeltaMax": cfprApEtherRxStatsJumboPacketsDeltaMax,
       "cfprApEtherRxStatsJumboPacketsDeltaMin": cfprApEtherRxStatsJumboPacketsDeltaMin,
       "cfprApEtherRxStatsMulticastPackets": cfprApEtherRxStatsMulticastPackets,
       "cfprApEtherRxStatsMulticastPacketsDelta": cfprApEtherRxStatsMulticastPacketsDelta,
       "cfprApEtherRxStatsMulticastPacketsDeltaAvg": cfprApEtherRxStatsMulticastPacketsDeltaAvg,
       "cfprApEtherRxStatsMulticastPacketsDeltaMax": cfprApEtherRxStatsMulticastPacketsDeltaMax,
       "cfprApEtherRxStatsMulticastPacketsDeltaMin": cfprApEtherRxStatsMulticastPacketsDeltaMin,
       "cfprApEtherRxStatsSuspect": cfprApEtherRxStatsSuspect,
       "cfprApEtherRxStatsThresholded": cfprApEtherRxStatsThresholded,
       "cfprApEtherRxStatsTimeCollected": cfprApEtherRxStatsTimeCollected,
       "cfprApEtherRxStatsTotalBytes": cfprApEtherRxStatsTotalBytes,
       "cfprApEtherRxStatsTotalBytesDelta": cfprApEtherRxStatsTotalBytesDelta,
       "cfprApEtherRxStatsTotalBytesDeltaAvg": cfprApEtherRxStatsTotalBytesDeltaAvg,
       "cfprApEtherRxStatsTotalBytesDeltaMax": cfprApEtherRxStatsTotalBytesDeltaMax,
       "cfprApEtherRxStatsTotalBytesDeltaMin": cfprApEtherRxStatsTotalBytesDeltaMin,
       "cfprApEtherRxStatsTotalPackets": cfprApEtherRxStatsTotalPackets,
       "cfprApEtherRxStatsTotalPacketsDelta": cfprApEtherRxStatsTotalPacketsDelta,
       "cfprApEtherRxStatsTotalPacketsDeltaAvg": cfprApEtherRxStatsTotalPacketsDeltaAvg,
       "cfprApEtherRxStatsTotalPacketsDeltaMax": cfprApEtherRxStatsTotalPacketsDeltaMax,
       "cfprApEtherRxStatsTotalPacketsDeltaMin": cfprApEtherRxStatsTotalPacketsDeltaMin,
       "cfprApEtherRxStatsUnicastPackets": cfprApEtherRxStatsUnicastPackets,
       "cfprApEtherRxStatsUnicastPacketsDelta": cfprApEtherRxStatsUnicastPacketsDelta,
       "cfprApEtherRxStatsUnicastPacketsDeltaAvg": cfprApEtherRxStatsUnicastPacketsDeltaAvg,
       "cfprApEtherRxStatsUnicastPacketsDeltaMax": cfprApEtherRxStatsUnicastPacketsDeltaMax,
       "cfprApEtherRxStatsUnicastPacketsDeltaMin": cfprApEtherRxStatsUnicastPacketsDeltaMin,
       "cfprApEtherRxStatsUpdate": cfprApEtherRxStatsUpdate,
       "cfprApEtherRxStatsHistTable": cfprApEtherRxStatsHistTable,
       "cfprApEtherRxStatsHistEntry": cfprApEtherRxStatsHistEntry,
       "cfprApEtherRxStatsHistInstanceId": cfprApEtherRxStatsHistInstanceId,
       "cfprApEtherRxStatsHistDn": cfprApEtherRxStatsHistDn,
       "cfprApEtherRxStatsHistRn": cfprApEtherRxStatsHistRn,
       "cfprApEtherRxStatsHistBroadcastPackets": cfprApEtherRxStatsHistBroadcastPackets,
       "cfprApEtherRxStatsHistBroadcastPacketsDelta": cfprApEtherRxStatsHistBroadcastPacketsDelta,
       "cfprApEtherRxStatsHistBroadcastPacketsDeltaAvg": cfprApEtherRxStatsHistBroadcastPacketsDeltaAvg,
       "cfprApEtherRxStatsHistBroadcastPacketsDeltaMax": cfprApEtherRxStatsHistBroadcastPacketsDeltaMax,
       "cfprApEtherRxStatsHistBroadcastPacketsDeltaMin": cfprApEtherRxStatsHistBroadcastPacketsDeltaMin,
       "cfprApEtherRxStatsHistId": cfprApEtherRxStatsHistId,
       "cfprApEtherRxStatsHistJumboPackets": cfprApEtherRxStatsHistJumboPackets,
       "cfprApEtherRxStatsHistJumboPacketsDelta": cfprApEtherRxStatsHistJumboPacketsDelta,
       "cfprApEtherRxStatsHistJumboPacketsDeltaAvg": cfprApEtherRxStatsHistJumboPacketsDeltaAvg,
       "cfprApEtherRxStatsHistJumboPacketsDeltaMax": cfprApEtherRxStatsHistJumboPacketsDeltaMax,
       "cfprApEtherRxStatsHistJumboPacketsDeltaMin": cfprApEtherRxStatsHistJumboPacketsDeltaMin,
       "cfprApEtherRxStatsHistMostRecent": cfprApEtherRxStatsHistMostRecent,
       "cfprApEtherRxStatsHistMulticastPackets": cfprApEtherRxStatsHistMulticastPackets,
       "cfprApEtherRxStatsHistMulticastPacketsDelta": cfprApEtherRxStatsHistMulticastPacketsDelta,
       "cfprApEtherRxStatsHistMulticastPacketsDeltaAvg": cfprApEtherRxStatsHistMulticastPacketsDeltaAvg,
       "cfprApEtherRxStatsHistMulticastPacketsDeltaMax": cfprApEtherRxStatsHistMulticastPacketsDeltaMax,
       "cfprApEtherRxStatsHistMulticastPacketsDeltaMin": cfprApEtherRxStatsHistMulticastPacketsDeltaMin,
       "cfprApEtherRxStatsHistSuspect": cfprApEtherRxStatsHistSuspect,
       "cfprApEtherRxStatsHistThresholded": cfprApEtherRxStatsHistThresholded,
       "cfprApEtherRxStatsHistTimeCollected": cfprApEtherRxStatsHistTimeCollected,
       "cfprApEtherRxStatsHistTotalBytes": cfprApEtherRxStatsHistTotalBytes,
       "cfprApEtherRxStatsHistTotalBytesDelta": cfprApEtherRxStatsHistTotalBytesDelta,
       "cfprApEtherRxStatsHistTotalBytesDeltaAvg": cfprApEtherRxStatsHistTotalBytesDeltaAvg,
       "cfprApEtherRxStatsHistTotalBytesDeltaMax": cfprApEtherRxStatsHistTotalBytesDeltaMax,
       "cfprApEtherRxStatsHistTotalBytesDeltaMin": cfprApEtherRxStatsHistTotalBytesDeltaMin,
       "cfprApEtherRxStatsHistTotalPackets": cfprApEtherRxStatsHistTotalPackets,
       "cfprApEtherRxStatsHistTotalPacketsDelta": cfprApEtherRxStatsHistTotalPacketsDelta,
       "cfprApEtherRxStatsHistTotalPacketsDeltaAvg": cfprApEtherRxStatsHistTotalPacketsDeltaAvg,
       "cfprApEtherRxStatsHistTotalPacketsDeltaMax": cfprApEtherRxStatsHistTotalPacketsDeltaMax,
       "cfprApEtherRxStatsHistTotalPacketsDeltaMin": cfprApEtherRxStatsHistTotalPacketsDeltaMin,
       "cfprApEtherRxStatsHistUnicastPackets": cfprApEtherRxStatsHistUnicastPackets,
       "cfprApEtherRxStatsHistUnicastPacketsDelta": cfprApEtherRxStatsHistUnicastPacketsDelta,
       "cfprApEtherRxStatsHistUnicastPacketsDeltaAvg": cfprApEtherRxStatsHistUnicastPacketsDeltaAvg,
       "cfprApEtherRxStatsHistUnicastPacketsDeltaMax": cfprApEtherRxStatsHistUnicastPacketsDeltaMax,
       "cfprApEtherRxStatsHistUnicastPacketsDeltaMin": cfprApEtherRxStatsHistUnicastPacketsDeltaMin,
       "cfprApEtherServerIntFIoTable": cfprApEtherServerIntFIoTable,
       "cfprApEtherServerIntFIoEntry": cfprApEtherServerIntFIoEntry,
       "cfprApEtherServerIntFIoInstanceId": cfprApEtherServerIntFIoInstanceId,
       "cfprApEtherServerIntFIoDn": cfprApEtherServerIntFIoDn,
       "cfprApEtherServerIntFIoRn": cfprApEtherServerIntFIoRn,
       "cfprApEtherServerIntFIoAdminSpeed": cfprApEtherServerIntFIoAdminSpeed,
       "cfprApEtherServerIntFIoAdminState": cfprApEtherServerIntFIoAdminState,
       "cfprApEtherServerIntFIoAggrPortId": cfprApEtherServerIntFIoAggrPortId,
       "cfprApEtherServerIntFIoChassisId": cfprApEtherServerIntFIoChassisId,
       "cfprApEtherServerIntFIoEncap": cfprApEtherServerIntFIoEncap,
       "cfprApEtherServerIntFIoEpDn": cfprApEtherServerIntFIoEpDn,
       "cfprApEtherServerIntFIoFltAggr": cfprApEtherServerIntFIoFltAggr,
       "cfprApEtherServerIntFIoFsmDescr": cfprApEtherServerIntFIoFsmDescr,
       "cfprApEtherServerIntFIoFsmPrev": cfprApEtherServerIntFIoFsmPrev,
       "cfprApEtherServerIntFIoFsmProgr": cfprApEtherServerIntFIoFsmProgr,
       "cfprApEtherServerIntFIoFsmRmtInvErrCode": cfprApEtherServerIntFIoFsmRmtInvErrCode,
       "cfprApEtherServerIntFIoFsmRmtInvErrDescr": cfprApEtherServerIntFIoFsmRmtInvErrDescr,
       "cfprApEtherServerIntFIoFsmRmtInvRslt": cfprApEtherServerIntFIoFsmRmtInvRslt,
       "cfprApEtherServerIntFIoFsmStageDescr": cfprApEtherServerIntFIoFsmStageDescr,
       "cfprApEtherServerIntFIoFsmStamp": cfprApEtherServerIntFIoFsmStamp,
       "cfprApEtherServerIntFIoFsmStatus": cfprApEtherServerIntFIoFsmStatus,
       "cfprApEtherServerIntFIoFsmTry": cfprApEtherServerIntFIoFsmTry,
       "cfprApEtherServerIntFIoIfRole": cfprApEtherServerIntFIoIfRole,
       "cfprApEtherServerIntFIoIfType": cfprApEtherServerIntFIoIfType,
       "cfprApEtherServerIntFIoLocale": cfprApEtherServerIntFIoLocale,
       "cfprApEtherServerIntFIoMac": cfprApEtherServerIntFIoMac,
       "cfprApEtherServerIntFIoMode": cfprApEtherServerIntFIoMode,
       "cfprApEtherServerIntFIoModel": cfprApEtherServerIntFIoModel,
       "cfprApEtherServerIntFIoName": cfprApEtherServerIntFIoName,
       "cfprApEtherServerIntFIoNsSize": cfprApEtherServerIntFIoNsSize,
       "cfprApEtherServerIntFIoOperBorderAggrPortId": cfprApEtherServerIntFIoOperBorderAggrPortId,
       "cfprApEtherServerIntFIoOperBorderPortId": cfprApEtherServerIntFIoOperBorderPortId,
       "cfprApEtherServerIntFIoOperBorderSlotId": cfprApEtherServerIntFIoOperBorderSlotId,
       "cfprApEtherServerIntFIoOperState": cfprApEtherServerIntFIoOperState,
       "cfprApEtherServerIntFIoPeerAggrPortId": cfprApEtherServerIntFIoPeerAggrPortId,
       "cfprApEtherServerIntFIoPeerChassisId": cfprApEtherServerIntFIoPeerChassisId,
       "cfprApEtherServerIntFIoPeerDn": cfprApEtherServerIntFIoPeerDn,
       "cfprApEtherServerIntFIoPeerEncap": cfprApEtherServerIntFIoPeerEncap,
       "cfprApEtherServerIntFIoPeerPortId": cfprApEtherServerIntFIoPeerPortId,
       "cfprApEtherServerIntFIoPeerSlotId": cfprApEtherServerIntFIoPeerSlotId,
       "cfprApEtherServerIntFIoPortId": cfprApEtherServerIntFIoPortId,
       "cfprApEtherServerIntFIoRevision": cfprApEtherServerIntFIoRevision,
       "cfprApEtherServerIntFIoSerial": cfprApEtherServerIntFIoSerial,
       "cfprApEtherServerIntFIoSlotId": cfprApEtherServerIntFIoSlotId,
       "cfprApEtherServerIntFIoStateQual": cfprApEtherServerIntFIoStateQual,
       "cfprApEtherServerIntFIoSwitchId": cfprApEtherServerIntFIoSwitchId,
       "cfprApEtherServerIntFIoTransport": cfprApEtherServerIntFIoTransport,
       "cfprApEtherServerIntFIoTs": cfprApEtherServerIntFIoTs,
       "cfprApEtherServerIntFIoType": cfprApEtherServerIntFIoType,
       "cfprApEtherServerIntFIoVendor": cfprApEtherServerIntFIoVendor,
       "cfprApEtherServerIntFIoXcvrType": cfprApEtherServerIntFIoXcvrType,
       "cfprApEtherServerIntFIoFsmTable": cfprApEtherServerIntFIoFsmTable,
       "cfprApEtherServerIntFIoFsmEntry": cfprApEtherServerIntFIoFsmEntry,
       "cfprApEtherServerIntFIoFsmInstanceId": cfprApEtherServerIntFIoFsmInstanceId,
       "cfprApEtherServerIntFIoFsmDn": cfprApEtherServerIntFIoFsmDn,
       "cfprApEtherServerIntFIoFsmRn": cfprApEtherServerIntFIoFsmRn,
       "cfprApEtherServerIntFIoFsmCompletionTime": cfprApEtherServerIntFIoFsmCompletionTime,
       "cfprApEtherServerIntFIoFsmCurrentFsm": cfprApEtherServerIntFIoFsmCurrentFsm,
       "cfprApEtherServerIntFIoFsmDescrData": cfprApEtherServerIntFIoFsmDescrData,
       "cfprApEtherServerIntFIoFsmFsmStatus": cfprApEtherServerIntFIoFsmFsmStatus,
       "cfprApEtherServerIntFIoFsmProgress": cfprApEtherServerIntFIoFsmProgress,
       "cfprApEtherServerIntFIoFsmRmtErrCode": cfprApEtherServerIntFIoFsmRmtErrCode,
       "cfprApEtherServerIntFIoFsmRmtErrDescr": cfprApEtherServerIntFIoFsmRmtErrDescr,
       "cfprApEtherServerIntFIoFsmRmtRslt": cfprApEtherServerIntFIoFsmRmtRslt,
       "cfprApEtherServerIntFIoFsmStageTable": cfprApEtherServerIntFIoFsmStageTable,
       "cfprApEtherServerIntFIoFsmStageEntry": cfprApEtherServerIntFIoFsmStageEntry,
       "cfprApEtherServerIntFIoFsmStageInstanceId": cfprApEtherServerIntFIoFsmStageInstanceId,
       "cfprApEtherServerIntFIoFsmStageDn": cfprApEtherServerIntFIoFsmStageDn,
       "cfprApEtherServerIntFIoFsmStageRn": cfprApEtherServerIntFIoFsmStageRn,
       "cfprApEtherServerIntFIoFsmStageDescrData": cfprApEtherServerIntFIoFsmStageDescrData,
       "cfprApEtherServerIntFIoFsmStageLastUpdateTime": cfprApEtherServerIntFIoFsmStageLastUpdateTime,
       "cfprApEtherServerIntFIoFsmStageName": cfprApEtherServerIntFIoFsmStageName,
       "cfprApEtherServerIntFIoFsmStageOrder": cfprApEtherServerIntFIoFsmStageOrder,
       "cfprApEtherServerIntFIoFsmStageRetry": cfprApEtherServerIntFIoFsmStageRetry,
       "cfprApEtherServerIntFIoFsmStageStageStatus": cfprApEtherServerIntFIoFsmStageStageStatus,
       "cfprApEtherServerIntFIoFsmTaskTable": cfprApEtherServerIntFIoFsmTaskTable,
       "cfprApEtherServerIntFIoFsmTaskEntry": cfprApEtherServerIntFIoFsmTaskEntry,
       "cfprApEtherServerIntFIoFsmTaskInstanceId": cfprApEtherServerIntFIoFsmTaskInstanceId,
       "cfprApEtherServerIntFIoFsmTaskDn": cfprApEtherServerIntFIoFsmTaskDn,
       "cfprApEtherServerIntFIoFsmTaskRn": cfprApEtherServerIntFIoFsmTaskRn,
       "cfprApEtherServerIntFIoFsmTaskCompletion": cfprApEtherServerIntFIoFsmTaskCompletion,
       "cfprApEtherServerIntFIoFsmTaskFlags": cfprApEtherServerIntFIoFsmTaskFlags,
       "cfprApEtherServerIntFIoFsmTaskItem": cfprApEtherServerIntFIoFsmTaskItem,
       "cfprApEtherServerIntFIoFsmTaskSeqId": cfprApEtherServerIntFIoFsmTaskSeqId,
       "cfprApEtherServerIntFIoPcTable": cfprApEtherServerIntFIoPcTable,
       "cfprApEtherServerIntFIoPcEntry": cfprApEtherServerIntFIoPcEntry,
       "cfprApEtherServerIntFIoPcInstanceId": cfprApEtherServerIntFIoPcInstanceId,
       "cfprApEtherServerIntFIoPcDn": cfprApEtherServerIntFIoPcDn,
       "cfprApEtherServerIntFIoPcRn": cfprApEtherServerIntFIoPcRn,
       "cfprApEtherServerIntFIoPcChassisId": cfprApEtherServerIntFIoPcChassisId,
       "cfprApEtherServerIntFIoPcEpDn": cfprApEtherServerIntFIoPcEpDn,
       "cfprApEtherServerIntFIoPcFltAggr": cfprApEtherServerIntFIoPcFltAggr,
       "cfprApEtherServerIntFIoPcIfRole": cfprApEtherServerIntFIoPcIfRole,
       "cfprApEtherServerIntFIoPcIfType": cfprApEtherServerIntFIoPcIfType,
       "cfprApEtherServerIntFIoPcLocale": cfprApEtherServerIntFIoPcLocale,
       "cfprApEtherServerIntFIoPcName": cfprApEtherServerIntFIoPcName,
       "cfprApEtherServerIntFIoPcOperSpeed": cfprApEtherServerIntFIoPcOperSpeed,
       "cfprApEtherServerIntFIoPcOperState": cfprApEtherServerIntFIoPcOperState,
       "cfprApEtherServerIntFIoPcPeerDn": cfprApEtherServerIntFIoPcPeerDn,
       "cfprApEtherServerIntFIoPcPortId": cfprApEtherServerIntFIoPcPortId,
       "cfprApEtherServerIntFIoPcStateQual": cfprApEtherServerIntFIoPcStateQual,
       "cfprApEtherServerIntFIoPcSwitchId": cfprApEtherServerIntFIoPcSwitchId,
       "cfprApEtherServerIntFIoPcTransport": cfprApEtherServerIntFIoPcTransport,
       "cfprApEtherServerIntFIoPcType": cfprApEtherServerIntFIoPcType,
       "cfprApEtherServerIntFIoPcEpTable": cfprApEtherServerIntFIoPcEpTable,
       "cfprApEtherServerIntFIoPcEpEntry": cfprApEtherServerIntFIoPcEpEntry,
       "cfprApEtherServerIntFIoPcEpInstanceId": cfprApEtherServerIntFIoPcEpInstanceId,
       "cfprApEtherServerIntFIoPcEpDnData": cfprApEtherServerIntFIoPcEpDnData,
       "cfprApEtherServerIntFIoPcEpRn": cfprApEtherServerIntFIoPcEpRn,
       "cfprApEtherServerIntFIoPcEpAdminState": cfprApEtherServerIntFIoPcEpAdminState,
       "cfprApEtherServerIntFIoPcEpAggrPortId": cfprApEtherServerIntFIoPcEpAggrPortId,
       "cfprApEtherServerIntFIoPcEpChassisId": cfprApEtherServerIntFIoPcEpChassisId,
       "cfprApEtherServerIntFIoPcEpEpDn": cfprApEtherServerIntFIoPcEpEpDn,
       "cfprApEtherServerIntFIoPcEpIfRole": cfprApEtherServerIntFIoPcEpIfRole,
       "cfprApEtherServerIntFIoPcEpIfType": cfprApEtherServerIntFIoPcEpIfType,
       "cfprApEtherServerIntFIoPcEpLocale": cfprApEtherServerIntFIoPcEpLocale,
       "cfprApEtherServerIntFIoPcEpMembership": cfprApEtherServerIntFIoPcEpMembership,
       "cfprApEtherServerIntFIoPcEpName": cfprApEtherServerIntFIoPcEpName,
       "cfprApEtherServerIntFIoPcEpPeerAggrPortId": cfprApEtherServerIntFIoPcEpPeerAggrPortId,
       "cfprApEtherServerIntFIoPcEpPeerChassisId": cfprApEtherServerIntFIoPcEpPeerChassisId,
       "cfprApEtherServerIntFIoPcEpPeerDn": cfprApEtherServerIntFIoPcEpPeerDn,
       "cfprApEtherServerIntFIoPcEpPeerPortId": cfprApEtherServerIntFIoPcEpPeerPortId,
       "cfprApEtherServerIntFIoPcEpPeerSlotId": cfprApEtherServerIntFIoPcEpPeerSlotId,
       "cfprApEtherServerIntFIoPcEpPortId": cfprApEtherServerIntFIoPcEpPortId,
       "cfprApEtherServerIntFIoPcEpSlotId": cfprApEtherServerIntFIoPcEpSlotId,
       "cfprApEtherServerIntFIoPcEpSwitchId": cfprApEtherServerIntFIoPcEpSwitchId,
       "cfprApEtherServerIntFIoPcEpTransport": cfprApEtherServerIntFIoPcEpTransport,
       "cfprApEtherServerIntFIoPcEpType": cfprApEtherServerIntFIoPcEpType,
       "cfprApEtherSwIfConfigTable": cfprApEtherSwIfConfigTable,
       "cfprApEtherSwIfConfigEntry": cfprApEtherSwIfConfigEntry,
       "cfprApEtherSwIfConfigInstanceId": cfprApEtherSwIfConfigInstanceId,
       "cfprApEtherSwIfConfigDn": cfprApEtherSwIfConfigDn,
       "cfprApEtherSwIfConfigRn": cfprApEtherSwIfConfigRn,
       "cfprApEtherSwitchIntFIoTable": cfprApEtherSwitchIntFIoTable,
       "cfprApEtherSwitchIntFIoEntry": cfprApEtherSwitchIntFIoEntry,
       "cfprApEtherSwitchIntFIoInstanceId": cfprApEtherSwitchIntFIoInstanceId,
       "cfprApEtherSwitchIntFIoDn": cfprApEtherSwitchIntFIoDn,
       "cfprApEtherSwitchIntFIoRn": cfprApEtherSwitchIntFIoRn,
       "cfprApEtherSwitchIntFIoAck": cfprApEtherSwitchIntFIoAck,
       "cfprApEtherSwitchIntFIoAdminState": cfprApEtherSwitchIntFIoAdminState,
       "cfprApEtherSwitchIntFIoAggrPortId": cfprApEtherSwitchIntFIoAggrPortId,
       "cfprApEtherSwitchIntFIoChassisId": cfprApEtherSwitchIntFIoChassisId,
       "cfprApEtherSwitchIntFIoDelFeTs": cfprApEtherSwitchIntFIoDelFeTs,
       "cfprApEtherSwitchIntFIoDiscovery": cfprApEtherSwitchIntFIoDiscovery,
       "cfprApEtherSwitchIntFIoEncap": cfprApEtherSwitchIntFIoEncap,
       "cfprApEtherSwitchIntFIoEpDn": cfprApEtherSwitchIntFIoEpDn,
       "cfprApEtherSwitchIntFIoFltAggr": cfprApEtherSwitchIntFIoFltAggr,
       "cfprApEtherSwitchIntFIoIfRole": cfprApEtherSwitchIntFIoIfRole,
       "cfprApEtherSwitchIntFIoIfType": cfprApEtherSwitchIntFIoIfType,
       "cfprApEtherSwitchIntFIoLocale": cfprApEtherSwitchIntFIoLocale,
       "cfprApEtherSwitchIntFIoMode": cfprApEtherSwitchIntFIoMode,
       "cfprApEtherSwitchIntFIoModel": cfprApEtherSwitchIntFIoModel,
       "cfprApEtherSwitchIntFIoName": cfprApEtherSwitchIntFIoName,
       "cfprApEtherSwitchIntFIoNewFeTs": cfprApEtherSwitchIntFIoNewFeTs,
       "cfprApEtherSwitchIntFIoOperState": cfprApEtherSwitchIntFIoOperState,
       "cfprApEtherSwitchIntFIoPeerAggrPortId": cfprApEtherSwitchIntFIoPeerAggrPortId,
       "cfprApEtherSwitchIntFIoPeerChassisId": cfprApEtherSwitchIntFIoPeerChassisId,
       "cfprApEtherSwitchIntFIoPeerDn": cfprApEtherSwitchIntFIoPeerDn,
       "cfprApEtherSwitchIntFIoPeerPortId": cfprApEtherSwitchIntFIoPeerPortId,
       "cfprApEtherSwitchIntFIoPeerSlotId": cfprApEtherSwitchIntFIoPeerSlotId,
       "cfprApEtherSwitchIntFIoPortId": cfprApEtherSwitchIntFIoPortId,
       "cfprApEtherSwitchIntFIoRevision": cfprApEtherSwitchIntFIoRevision,
       "cfprApEtherSwitchIntFIoSerial": cfprApEtherSwitchIntFIoSerial,
       "cfprApEtherSwitchIntFIoSlotId": cfprApEtherSwitchIntFIoSlotId,
       "cfprApEtherSwitchIntFIoStateQual": cfprApEtherSwitchIntFIoStateQual,
       "cfprApEtherSwitchIntFIoSwitchId": cfprApEtherSwitchIntFIoSwitchId,
       "cfprApEtherSwitchIntFIoTransport": cfprApEtherSwitchIntFIoTransport,
       "cfprApEtherSwitchIntFIoTs": cfprApEtherSwitchIntFIoTs,
       "cfprApEtherSwitchIntFIoType": cfprApEtherSwitchIntFIoType,
       "cfprApEtherSwitchIntFIoVendor": cfprApEtherSwitchIntFIoVendor,
       "cfprApEtherSwitchIntFIoXcvrType": cfprApEtherSwitchIntFIoXcvrType,
       "cfprApEtherSwitchIntFIoPcTable": cfprApEtherSwitchIntFIoPcTable,
       "cfprApEtherSwitchIntFIoPcEntry": cfprApEtherSwitchIntFIoPcEntry,
       "cfprApEtherSwitchIntFIoPcInstanceId": cfprApEtherSwitchIntFIoPcInstanceId,
       "cfprApEtherSwitchIntFIoPcDn": cfprApEtherSwitchIntFIoPcDn,
       "cfprApEtherSwitchIntFIoPcRn": cfprApEtherSwitchIntFIoPcRn,
       "cfprApEtherSwitchIntFIoPcAdminState": cfprApEtherSwitchIntFIoPcAdminState,
       "cfprApEtherSwitchIntFIoPcChassisId": cfprApEtherSwitchIntFIoPcChassisId,
       "cfprApEtherSwitchIntFIoPcEpDn": cfprApEtherSwitchIntFIoPcEpDn,
       "cfprApEtherSwitchIntFIoPcFltAggr": cfprApEtherSwitchIntFIoPcFltAggr,
       "cfprApEtherSwitchIntFIoPcIfRole": cfprApEtherSwitchIntFIoPcIfRole,
       "cfprApEtherSwitchIntFIoPcIfType": cfprApEtherSwitchIntFIoPcIfType,
       "cfprApEtherSwitchIntFIoPcLocale": cfprApEtherSwitchIntFIoPcLocale,
       "cfprApEtherSwitchIntFIoPcName": cfprApEtherSwitchIntFIoPcName,
       "cfprApEtherSwitchIntFIoPcOperSpeed": cfprApEtherSwitchIntFIoPcOperSpeed,
       "cfprApEtherSwitchIntFIoPcOperState": cfprApEtherSwitchIntFIoPcOperState,
       "cfprApEtherSwitchIntFIoPcPeerDn": cfprApEtherSwitchIntFIoPcPeerDn,
       "cfprApEtherSwitchIntFIoPcPortId": cfprApEtherSwitchIntFIoPcPortId,
       "cfprApEtherSwitchIntFIoPcStateQual": cfprApEtherSwitchIntFIoPcStateQual,
       "cfprApEtherSwitchIntFIoPcSwitchId": cfprApEtherSwitchIntFIoPcSwitchId,
       "cfprApEtherSwitchIntFIoPcTransport": cfprApEtherSwitchIntFIoPcTransport,
       "cfprApEtherSwitchIntFIoPcType": cfprApEtherSwitchIntFIoPcType,
       "cfprApEtherSwitchIntFIoPcEpTable": cfprApEtherSwitchIntFIoPcEpTable,
       "cfprApEtherSwitchIntFIoPcEpEntry": cfprApEtherSwitchIntFIoPcEpEntry,
       "cfprApEtherSwitchIntFIoPcEpInstanceId": cfprApEtherSwitchIntFIoPcEpInstanceId,
       "cfprApEtherSwitchIntFIoPcEpDnData": cfprApEtherSwitchIntFIoPcEpDnData,
       "cfprApEtherSwitchIntFIoPcEpRn": cfprApEtherSwitchIntFIoPcEpRn,
       "cfprApEtherSwitchIntFIoPcEpAckState": cfprApEtherSwitchIntFIoPcEpAckState,
       "cfprApEtherSwitchIntFIoPcEpAdminState": cfprApEtherSwitchIntFIoPcEpAdminState,
       "cfprApEtherSwitchIntFIoPcEpAggrPortId": cfprApEtherSwitchIntFIoPcEpAggrPortId,
       "cfprApEtherSwitchIntFIoPcEpChassisId": cfprApEtherSwitchIntFIoPcEpChassisId,
       "cfprApEtherSwitchIntFIoPcEpEpDn": cfprApEtherSwitchIntFIoPcEpEpDn,
       "cfprApEtherSwitchIntFIoPcEpIfRole": cfprApEtherSwitchIntFIoPcEpIfRole,
       "cfprApEtherSwitchIntFIoPcEpIfType": cfprApEtherSwitchIntFIoPcEpIfType,
       "cfprApEtherSwitchIntFIoPcEpLocale": cfprApEtherSwitchIntFIoPcEpLocale,
       "cfprApEtherSwitchIntFIoPcEpMembership": cfprApEtherSwitchIntFIoPcEpMembership,
       "cfprApEtherSwitchIntFIoPcEpName": cfprApEtherSwitchIntFIoPcEpName,
       "cfprApEtherSwitchIntFIoPcEpPeerAggrPortId": cfprApEtherSwitchIntFIoPcEpPeerAggrPortId,
       "cfprApEtherSwitchIntFIoPcEpPeerChassisId": cfprApEtherSwitchIntFIoPcEpPeerChassisId,
       "cfprApEtherSwitchIntFIoPcEpPeerDn": cfprApEtherSwitchIntFIoPcEpPeerDn,
       "cfprApEtherSwitchIntFIoPcEpPeerPortId": cfprApEtherSwitchIntFIoPcEpPeerPortId,
       "cfprApEtherSwitchIntFIoPcEpPeerSlotId": cfprApEtherSwitchIntFIoPcEpPeerSlotId,
       "cfprApEtherSwitchIntFIoPcEpPortId": cfprApEtherSwitchIntFIoPcEpPortId,
       "cfprApEtherSwitchIntFIoPcEpSlotId": cfprApEtherSwitchIntFIoPcEpSlotId,
       "cfprApEtherSwitchIntFIoPcEpStatusChangeTs": cfprApEtherSwitchIntFIoPcEpStatusChangeTs,
       "cfprApEtherSwitchIntFIoPcEpSwitchId": cfprApEtherSwitchIntFIoPcEpSwitchId,
       "cfprApEtherSwitchIntFIoPcEpTransport": cfprApEtherSwitchIntFIoPcEpTransport,
       "cfprApEtherSwitchIntFIoPcEpType": cfprApEtherSwitchIntFIoPcEpType,
       "cfprApEtherTxStatsTable": cfprApEtherTxStatsTable,
       "cfprApEtherTxStatsEntry": cfprApEtherTxStatsEntry,
       "cfprApEtherTxStatsInstanceId": cfprApEtherTxStatsInstanceId,
       "cfprApEtherTxStatsDn": cfprApEtherTxStatsDn,
       "cfprApEtherTxStatsRn": cfprApEtherTxStatsRn,
       "cfprApEtherTxStatsBroadcastPackets": cfprApEtherTxStatsBroadcastPackets,
       "cfprApEtherTxStatsBroadcastPacketsDelta": cfprApEtherTxStatsBroadcastPacketsDelta,
       "cfprApEtherTxStatsBroadcastPacketsDeltaAvg": cfprApEtherTxStatsBroadcastPacketsDeltaAvg,
       "cfprApEtherTxStatsBroadcastPacketsDeltaMax": cfprApEtherTxStatsBroadcastPacketsDeltaMax,
       "cfprApEtherTxStatsBroadcastPacketsDeltaMin": cfprApEtherTxStatsBroadcastPacketsDeltaMin,
       "cfprApEtherTxStatsIntervals": cfprApEtherTxStatsIntervals,
       "cfprApEtherTxStatsJumboPackets": cfprApEtherTxStatsJumboPackets,
       "cfprApEtherTxStatsJumboPacketsDelta": cfprApEtherTxStatsJumboPacketsDelta,
       "cfprApEtherTxStatsJumboPacketsDeltaAvg": cfprApEtherTxStatsJumboPacketsDeltaAvg,
       "cfprApEtherTxStatsJumboPacketsDeltaMax": cfprApEtherTxStatsJumboPacketsDeltaMax,
       "cfprApEtherTxStatsJumboPacketsDeltaMin": cfprApEtherTxStatsJumboPacketsDeltaMin,
       "cfprApEtherTxStatsMulticastPackets": cfprApEtherTxStatsMulticastPackets,
       "cfprApEtherTxStatsMulticastPacketsDelta": cfprApEtherTxStatsMulticastPacketsDelta,
       "cfprApEtherTxStatsMulticastPacketsDeltaAvg": cfprApEtherTxStatsMulticastPacketsDeltaAvg,
       "cfprApEtherTxStatsMulticastPacketsDeltaMax": cfprApEtherTxStatsMulticastPacketsDeltaMax,
       "cfprApEtherTxStatsMulticastPacketsDeltaMin": cfprApEtherTxStatsMulticastPacketsDeltaMin,
       "cfprApEtherTxStatsSuspect": cfprApEtherTxStatsSuspect,
       "cfprApEtherTxStatsThresholded": cfprApEtherTxStatsThresholded,
       "cfprApEtherTxStatsTimeCollected": cfprApEtherTxStatsTimeCollected,
       "cfprApEtherTxStatsTotalBytes": cfprApEtherTxStatsTotalBytes,
       "cfprApEtherTxStatsTotalBytesDelta": cfprApEtherTxStatsTotalBytesDelta,
       "cfprApEtherTxStatsTotalBytesDeltaAvg": cfprApEtherTxStatsTotalBytesDeltaAvg,
       "cfprApEtherTxStatsTotalBytesDeltaMax": cfprApEtherTxStatsTotalBytesDeltaMax,
       "cfprApEtherTxStatsTotalBytesDeltaMin": cfprApEtherTxStatsTotalBytesDeltaMin,
       "cfprApEtherTxStatsTotalPackets": cfprApEtherTxStatsTotalPackets,
       "cfprApEtherTxStatsTotalPacketsDelta": cfprApEtherTxStatsTotalPacketsDelta,
       "cfprApEtherTxStatsTotalPacketsDeltaAvg": cfprApEtherTxStatsTotalPacketsDeltaAvg,
       "cfprApEtherTxStatsTotalPacketsDeltaMax": cfprApEtherTxStatsTotalPacketsDeltaMax,
       "cfprApEtherTxStatsTotalPacketsDeltaMin": cfprApEtherTxStatsTotalPacketsDeltaMin,
       "cfprApEtherTxStatsUnicastPackets": cfprApEtherTxStatsUnicastPackets,
       "cfprApEtherTxStatsUnicastPacketsDelta": cfprApEtherTxStatsUnicastPacketsDelta,
       "cfprApEtherTxStatsUnicastPacketsDeltaAvg": cfprApEtherTxStatsUnicastPacketsDeltaAvg,
       "cfprApEtherTxStatsUnicastPacketsDeltaMax": cfprApEtherTxStatsUnicastPacketsDeltaMax,
       "cfprApEtherTxStatsUnicastPacketsDeltaMin": cfprApEtherTxStatsUnicastPacketsDeltaMin,
       "cfprApEtherTxStatsUpdate": cfprApEtherTxStatsUpdate,
       "cfprApEtherTxStatsHistTable": cfprApEtherTxStatsHistTable,
       "cfprApEtherTxStatsHistEntry": cfprApEtherTxStatsHistEntry,
       "cfprApEtherTxStatsHistInstanceId": cfprApEtherTxStatsHistInstanceId,
       "cfprApEtherTxStatsHistDn": cfprApEtherTxStatsHistDn,
       "cfprApEtherTxStatsHistRn": cfprApEtherTxStatsHistRn,
       "cfprApEtherTxStatsHistBroadcastPackets": cfprApEtherTxStatsHistBroadcastPackets,
       "cfprApEtherTxStatsHistBroadcastPacketsDelta": cfprApEtherTxStatsHistBroadcastPacketsDelta,
       "cfprApEtherTxStatsHistBroadcastPacketsDeltaAvg": cfprApEtherTxStatsHistBroadcastPacketsDeltaAvg,
       "cfprApEtherTxStatsHistBroadcastPacketsDeltaMax": cfprApEtherTxStatsHistBroadcastPacketsDeltaMax,
       "cfprApEtherTxStatsHistBroadcastPacketsDeltaMin": cfprApEtherTxStatsHistBroadcastPacketsDeltaMin,
       "cfprApEtherTxStatsHistId": cfprApEtherTxStatsHistId,
       "cfprApEtherTxStatsHistJumboPackets": cfprApEtherTxStatsHistJumboPackets,
       "cfprApEtherTxStatsHistJumboPacketsDelta": cfprApEtherTxStatsHistJumboPacketsDelta,
       "cfprApEtherTxStatsHistJumboPacketsDeltaAvg": cfprApEtherTxStatsHistJumboPacketsDeltaAvg,
       "cfprApEtherTxStatsHistJumboPacketsDeltaMax": cfprApEtherTxStatsHistJumboPacketsDeltaMax,
       "cfprApEtherTxStatsHistJumboPacketsDeltaMin": cfprApEtherTxStatsHistJumboPacketsDeltaMin,
       "cfprApEtherTxStatsHistMostRecent": cfprApEtherTxStatsHistMostRecent,
       "cfprApEtherTxStatsHistMulticastPackets": cfprApEtherTxStatsHistMulticastPackets,
       "cfprApEtherTxStatsHistMulticastPacketsDelta": cfprApEtherTxStatsHistMulticastPacketsDelta,
       "cfprApEtherTxStatsHistMulticastPacketsDeltaAvg": cfprApEtherTxStatsHistMulticastPacketsDeltaAvg,
       "cfprApEtherTxStatsHistMulticastPacketsDeltaMax": cfprApEtherTxStatsHistMulticastPacketsDeltaMax,
       "cfprApEtherTxStatsHistMulticastPacketsDeltaMin": cfprApEtherTxStatsHistMulticastPacketsDeltaMin,
       "cfprApEtherTxStatsHistSuspect": cfprApEtherTxStatsHistSuspect,
       "cfprApEtherTxStatsHistThresholded": cfprApEtherTxStatsHistThresholded,
       "cfprApEtherTxStatsHistTimeCollected": cfprApEtherTxStatsHistTimeCollected,
       "cfprApEtherTxStatsHistTotalBytes": cfprApEtherTxStatsHistTotalBytes,
       "cfprApEtherTxStatsHistTotalBytesDelta": cfprApEtherTxStatsHistTotalBytesDelta,
       "cfprApEtherTxStatsHistTotalBytesDeltaAvg": cfprApEtherTxStatsHistTotalBytesDeltaAvg,
       "cfprApEtherTxStatsHistTotalBytesDeltaMax": cfprApEtherTxStatsHistTotalBytesDeltaMax,
       "cfprApEtherTxStatsHistTotalBytesDeltaMin": cfprApEtherTxStatsHistTotalBytesDeltaMin,
       "cfprApEtherTxStatsHistTotalPackets": cfprApEtherTxStatsHistTotalPackets,
       "cfprApEtherTxStatsHistTotalPacketsDelta": cfprApEtherTxStatsHistTotalPacketsDelta,
       "cfprApEtherTxStatsHistTotalPacketsDeltaAvg": cfprApEtherTxStatsHistTotalPacketsDeltaAvg,
       "cfprApEtherTxStatsHistTotalPacketsDeltaMax": cfprApEtherTxStatsHistTotalPacketsDeltaMax,
       "cfprApEtherTxStatsHistTotalPacketsDeltaMin": cfprApEtherTxStatsHistTotalPacketsDeltaMin,
       "cfprApEtherTxStatsHistUnicastPackets": cfprApEtherTxStatsHistUnicastPackets,
       "cfprApEtherTxStatsHistUnicastPacketsDelta": cfprApEtherTxStatsHistUnicastPacketsDelta,
       "cfprApEtherTxStatsHistUnicastPacketsDeltaAvg": cfprApEtherTxStatsHistUnicastPacketsDeltaAvg,
       "cfprApEtherTxStatsHistUnicastPacketsDeltaMax": cfprApEtherTxStatsHistUnicastPacketsDeltaMax,
       "cfprApEtherTxStatsHistUnicastPacketsDeltaMin": cfprApEtherTxStatsHistUnicastPacketsDeltaMin}
)
