# SNMP MIB module (TIMETRA-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SFLOW-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:35:22 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(sFlowCpDataSource,
 sFlowCpInstance,
 sFlowCpReceiver,
 sFlowRcvrEntry,
 sFlowRcvrIndex) = mibBuilder.importSymbols(
    "SFLOW-MIB",
    "sFlowCpDataSource",
    "sFlowCpInstance",
    "sFlowCpReceiver",
    "sFlowRcvrEntry",
    "sFlowRcvrIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TEgrPolicerId,
 TEgressQueueId,
 TIngPolicerId,
 TIngressQueueId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TEgrPolicerId",
    "TEgressQueueId",
    "TIngPolicerId",
    "TIngressQueueId")


# MODULE-IDENTITY

timetraSflowMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 95)
)
if mibBuilder.loadTexts:
    timetraSflowMIBModule.setRevisions(
        ("2013-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxSflowCounterMapTrafficType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSflowConformance_ObjectIdentity = ObjectIdentity
tmnxSflowConformance = _TmnxSflowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95)
)
_TmnxSflowCompliances_ObjectIdentity = ObjectIdentity
tmnxSflowCompliances = _TmnxSflowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 1)
)
_TmnxSflowGroups_ObjectIdentity = ObjectIdentity
tmnxSflowGroups = _TmnxSflowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2)
)
_TmnxSflowV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxSflowV12v0Groups = _TmnxSflowV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2, 1)
)
_TmnxSflowObjs_ObjectIdentity = ObjectIdentity
tmnxSflowObjs = _TmnxSflowObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95)
)
_TmnxSflowConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxSflowConfigTimeStamps = _TmnxSflowConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1)
)
_TmnxSflowRcvrTableLastChanged_Type = TimeStamp
_TmnxSflowRcvrTableLastChanged_Object = MibScalar
tmnxSflowRcvrTableLastChanged = _TmnxSflowRcvrTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1, 1),
    _TmnxSflowRcvrTableLastChanged_Type()
)
tmnxSflowRcvrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowRcvrTableLastChanged.setStatus("current")
_TmnxSflowCpTableLastChanged_Type = TimeStamp
_TmnxSflowCpTableLastChanged_Object = MibScalar
tmnxSflowCpTableLastChanged = _TmnxSflowCpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1, 2),
    _TmnxSflowCpTableLastChanged_Type()
)
tmnxSflowCpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowCpTableLastChanged.setStatus("current")
_TmnxSflowIngCMapPlcrTableLstCh_Type = TimeStamp
_TmnxSflowIngCMapPlcrTableLstCh_Object = MibScalar
tmnxSflowIngCMapPlcrTableLstCh = _TmnxSflowIngCMapPlcrTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1, 3),
    _TmnxSflowIngCMapPlcrTableLstCh_Type()
)
tmnxSflowIngCMapPlcrTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrTableLstCh.setStatus("current")
_TmnxSflowEgrCMapPlcrTableLstCh_Type = TimeStamp
_TmnxSflowEgrCMapPlcrTableLstCh_Object = MibScalar
tmnxSflowEgrCMapPlcrTableLstCh = _TmnxSflowEgrCMapPlcrTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1, 4),
    _TmnxSflowEgrCMapPlcrTableLstCh_Type()
)
tmnxSflowEgrCMapPlcrTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrTableLstCh.setStatus("current")
_TmnxSflowIngCMapQueueTableLstCh_Type = TimeStamp
_TmnxSflowIngCMapQueueTableLstCh_Object = MibScalar
tmnxSflowIngCMapQueueTableLstCh = _TmnxSflowIngCMapQueueTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1, 5),
    _TmnxSflowIngCMapQueueTableLstCh_Type()
)
tmnxSflowIngCMapQueueTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueTableLstCh.setStatus("current")
_TmnxSflowEgrCMapQueueTableLstCh_Type = TimeStamp
_TmnxSflowEgrCMapQueueTableLstCh_Object = MibScalar
tmnxSflowEgrCMapQueueTableLstCh = _TmnxSflowEgrCMapQueueTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 1, 6),
    _TmnxSflowEgrCMapQueueTableLstCh_Type()
)
tmnxSflowEgrCMapQueueTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueTableLstCh.setStatus("current")
_TmnxSflowConfigurations_ObjectIdentity = ObjectIdentity
tmnxSflowConfigurations = _TmnxSflowConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2)
)
_TmnxSflowRcvrTable_Object = MibTable
tmnxSflowRcvrTable = _TmnxSflowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxSflowRcvrTable.setStatus("current")
_TmnxSflowRcvrEntry_Object = MibTableRow
tmnxSflowRcvrEntry = _TmnxSflowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxSflowRcvrEntry.setStatus("current")
_TmnxSflowRcvrLastChanged_Type = TimeStamp
_TmnxSflowRcvrLastChanged_Object = MibTableColumn
tmnxSflowRcvrLastChanged = _TmnxSflowRcvrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 1, 1, 1),
    _TmnxSflowRcvrLastChanged_Type()
)
tmnxSflowRcvrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowRcvrLastChanged.setStatus("current")


class _TmnxSflowRcvrBackupAddressType_Type(InetAddressType):
    """Custom type tmnxSflowRcvrBackupAddressType based on InetAddressType"""
    defaultValue = 1


_TmnxSflowRcvrBackupAddressType_Type.__name__ = "InetAddressType"
_TmnxSflowRcvrBackupAddressType_Object = MibTableColumn
tmnxSflowRcvrBackupAddressType = _TmnxSflowRcvrBackupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 1, 1, 2),
    _TmnxSflowRcvrBackupAddressType_Type()
)
tmnxSflowRcvrBackupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSflowRcvrBackupAddressType.setStatus("current")


class _TmnxSflowRcvrBackupAddress_Type(InetAddress):
    """Custom type tmnxSflowRcvrBackupAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSflowRcvrBackupAddress_Type.__name__ = "InetAddress"
_TmnxSflowRcvrBackupAddress_Object = MibTableColumn
tmnxSflowRcvrBackupAddress = _TmnxSflowRcvrBackupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 1, 1, 3),
    _TmnxSflowRcvrBackupAddress_Type()
)
tmnxSflowRcvrBackupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSflowRcvrBackupAddress.setStatus("current")


class _TmnxSflowRcvrBackupDstPort_Type(Integer32):
    """Custom type tmnxSflowRcvrBackupDstPort based on Integer32"""
    defaultValue = 6343


_TmnxSflowRcvrBackupDstPort_Type.__name__ = "Integer32"
_TmnxSflowRcvrBackupDstPort_Object = MibTableColumn
tmnxSflowRcvrBackupDstPort = _TmnxSflowRcvrBackupDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 1, 1, 4),
    _TmnxSflowRcvrBackupDstPort_Type()
)
tmnxSflowRcvrBackupDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSflowRcvrBackupDstPort.setStatus("current")
_TmnxSflowCpTable_Object = MibTable
tmnxSflowCpTable = _TmnxSflowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxSflowCpTable.setStatus("current")
_TmnxSflowCpEntry_Object = MibTableRow
tmnxSflowCpEntry = _TmnxSflowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 2, 1)
)
tmnxSflowCpEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowCpDataSource"),
    (0, "SFLOW-MIB", "sFlowCpInstance"),
)
if mibBuilder.loadTexts:
    tmnxSflowCpEntry.setStatus("current")
_TmnxSflowCpRowStatus_Type = RowStatus
_TmnxSflowCpRowStatus_Object = MibTableColumn
tmnxSflowCpRowStatus = _TmnxSflowCpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 2, 1, 1),
    _TmnxSflowCpRowStatus_Type()
)
tmnxSflowCpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowCpRowStatus.setStatus("current")
_TmnxSflowCpLastChanged_Type = TimeStamp
_TmnxSflowCpLastChanged_Object = MibTableColumn
tmnxSflowCpLastChanged = _TmnxSflowCpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 2, 1, 2),
    _TmnxSflowCpLastChanged_Type()
)
tmnxSflowCpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowCpLastChanged.setStatus("current")
_TmnxSflowIngCMapPlcrTable_Object = MibTable
tmnxSflowIngCMapPlcrTable = _TmnxSflowIngCMapPlcrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrTable.setStatus("current")
_TmnxSflowIngCMapPlcrEntry_Object = MibTableRow
tmnxSflowIngCMapPlcrEntry = _TmnxSflowIngCMapPlcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 3, 1)
)
tmnxSflowIngCMapPlcrEntry.setIndexNames(
    (0, "TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapPlcrId"),
)
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrEntry.setStatus("current")
_TmnxSflowIngCMapPlcrId_Type = TIngPolicerId
_TmnxSflowIngCMapPlcrId_Object = MibTableColumn
tmnxSflowIngCMapPlcrId = _TmnxSflowIngCMapPlcrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 3, 1, 1),
    _TmnxSflowIngCMapPlcrId_Type()
)
tmnxSflowIngCMapPlcrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrId.setStatus("current")
_TmnxSflowIngCMapPlcrRowStatus_Type = RowStatus
_TmnxSflowIngCMapPlcrRowStatus_Object = MibTableColumn
tmnxSflowIngCMapPlcrRowStatus = _TmnxSflowIngCMapPlcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 3, 1, 2),
    _TmnxSflowIngCMapPlcrRowStatus_Type()
)
tmnxSflowIngCMapPlcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrRowStatus.setStatus("current")
_TmnxSflowIngCMapPlcrLastChange_Type = TimeStamp
_TmnxSflowIngCMapPlcrLastChange_Object = MibTableColumn
tmnxSflowIngCMapPlcrLastChange = _TmnxSflowIngCMapPlcrLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 3, 1, 3),
    _TmnxSflowIngCMapPlcrLastChange_Type()
)
tmnxSflowIngCMapPlcrLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrLastChange.setStatus("current")


class _TmnxSflowIngCMapPlcrTrafficType_Type(TmnxSflowCounterMapTrafficType):
    """Custom type tmnxSflowIngCMapPlcrTrafficType based on TmnxSflowCounterMapTrafficType"""
    defaultValue = 1


_TmnxSflowIngCMapPlcrTrafficType_Type.__name__ = "TmnxSflowCounterMapTrafficType"
_TmnxSflowIngCMapPlcrTrafficType_Object = MibTableColumn
tmnxSflowIngCMapPlcrTrafficType = _TmnxSflowIngCMapPlcrTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 3, 1, 4),
    _TmnxSflowIngCMapPlcrTrafficType_Type()
)
tmnxSflowIngCMapPlcrTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapPlcrTrafficType.setStatus("current")
_TmnxSflowEgrCMapPlcrTable_Object = MibTable
tmnxSflowEgrCMapPlcrTable = _TmnxSflowEgrCMapPlcrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrTable.setStatus("current")
_TmnxSflowEgrCMapPlcrEntry_Object = MibTableRow
tmnxSflowEgrCMapPlcrEntry = _TmnxSflowEgrCMapPlcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 4, 1)
)
tmnxSflowEgrCMapPlcrEntry.setIndexNames(
    (0, "TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapPlcrId"),
)
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrEntry.setStatus("current")
_TmnxSflowEgrCMapPlcrId_Type = TEgrPolicerId
_TmnxSflowEgrCMapPlcrId_Object = MibTableColumn
tmnxSflowEgrCMapPlcrId = _TmnxSflowEgrCMapPlcrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 4, 1, 1),
    _TmnxSflowEgrCMapPlcrId_Type()
)
tmnxSflowEgrCMapPlcrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrId.setStatus("current")
_TmnxSflowEgrCMapPlcrRowStatus_Type = RowStatus
_TmnxSflowEgrCMapPlcrRowStatus_Object = MibTableColumn
tmnxSflowEgrCMapPlcrRowStatus = _TmnxSflowEgrCMapPlcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 4, 1, 2),
    _TmnxSflowEgrCMapPlcrRowStatus_Type()
)
tmnxSflowEgrCMapPlcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrRowStatus.setStatus("current")
_TmnxSflowEgrCMapPlcrLastChange_Type = TimeStamp
_TmnxSflowEgrCMapPlcrLastChange_Object = MibTableColumn
tmnxSflowEgrCMapPlcrLastChange = _TmnxSflowEgrCMapPlcrLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 4, 1, 3),
    _TmnxSflowEgrCMapPlcrLastChange_Type()
)
tmnxSflowEgrCMapPlcrLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrLastChange.setStatus("current")


class _TmnxSflowEgrCMapPlcrTrafficType_Type(TmnxSflowCounterMapTrafficType):
    """Custom type tmnxSflowEgrCMapPlcrTrafficType based on TmnxSflowCounterMapTrafficType"""
    defaultValue = 1


_TmnxSflowEgrCMapPlcrTrafficType_Type.__name__ = "TmnxSflowCounterMapTrafficType"
_TmnxSflowEgrCMapPlcrTrafficType_Object = MibTableColumn
tmnxSflowEgrCMapPlcrTrafficType = _TmnxSflowEgrCMapPlcrTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 4, 1, 4),
    _TmnxSflowEgrCMapPlcrTrafficType_Type()
)
tmnxSflowEgrCMapPlcrTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapPlcrTrafficType.setStatus("current")
_TmnxSflowIngCMapQueueTable_Object = MibTable
tmnxSflowIngCMapQueueTable = _TmnxSflowIngCMapQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueTable.setStatus("current")
_TmnxSflowIngCMapQueueEntry_Object = MibTableRow
tmnxSflowIngCMapQueueEntry = _TmnxSflowIngCMapQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 5, 1)
)
tmnxSflowIngCMapQueueEntry.setIndexNames(
    (0, "TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapQueueId"),
)
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueEntry.setStatus("current")
_TmnxSflowIngCMapQueueId_Type = TIngressQueueId
_TmnxSflowIngCMapQueueId_Object = MibTableColumn
tmnxSflowIngCMapQueueId = _TmnxSflowIngCMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 5, 1, 1),
    _TmnxSflowIngCMapQueueId_Type()
)
tmnxSflowIngCMapQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueId.setStatus("current")
_TmnxSflowIngCMapQueueRowStatus_Type = RowStatus
_TmnxSflowIngCMapQueueRowStatus_Object = MibTableColumn
tmnxSflowIngCMapQueueRowStatus = _TmnxSflowIngCMapQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 5, 1, 2),
    _TmnxSflowIngCMapQueueRowStatus_Type()
)
tmnxSflowIngCMapQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueRowStatus.setStatus("current")
_TmnxSflowIngCMapQueueLastChange_Type = TimeStamp
_TmnxSflowIngCMapQueueLastChange_Object = MibTableColumn
tmnxSflowIngCMapQueueLastChange = _TmnxSflowIngCMapQueueLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 5, 1, 3),
    _TmnxSflowIngCMapQueueLastChange_Type()
)
tmnxSflowIngCMapQueueLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueLastChange.setStatus("current")


class _TmnxSflowIngCMapQueueTrafficType_Type(TmnxSflowCounterMapTrafficType):
    """Custom type tmnxSflowIngCMapQueueTrafficType based on TmnxSflowCounterMapTrafficType"""
    defaultValue = 1


_TmnxSflowIngCMapQueueTrafficType_Type.__name__ = "TmnxSflowCounterMapTrafficType"
_TmnxSflowIngCMapQueueTrafficType_Object = MibTableColumn
tmnxSflowIngCMapQueueTrafficType = _TmnxSflowIngCMapQueueTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 5, 1, 4),
    _TmnxSflowIngCMapQueueTrafficType_Type()
)
tmnxSflowIngCMapQueueTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowIngCMapQueueTrafficType.setStatus("current")
_TmnxSflowEgrCMapQueueTable_Object = MibTable
tmnxSflowEgrCMapQueueTable = _TmnxSflowEgrCMapQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueTable.setStatus("current")
_TmnxSflowEgrCMapQueueEntry_Object = MibTableRow
tmnxSflowEgrCMapQueueEntry = _TmnxSflowEgrCMapQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 6, 1)
)
tmnxSflowEgrCMapQueueEntry.setIndexNames(
    (0, "TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapQueueId"),
)
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueEntry.setStatus("current")
_TmnxSflowEgrCMapQueueId_Type = TEgressQueueId
_TmnxSflowEgrCMapQueueId_Object = MibTableColumn
tmnxSflowEgrCMapQueueId = _TmnxSflowEgrCMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 6, 1, 1),
    _TmnxSflowEgrCMapQueueId_Type()
)
tmnxSflowEgrCMapQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueId.setStatus("current")
_TmnxSflowEgrCMapQueueRowStatus_Type = RowStatus
_TmnxSflowEgrCMapQueueRowStatus_Object = MibTableColumn
tmnxSflowEgrCMapQueueRowStatus = _TmnxSflowEgrCMapQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 6, 1, 2),
    _TmnxSflowEgrCMapQueueRowStatus_Type()
)
tmnxSflowEgrCMapQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueRowStatus.setStatus("current")
_TmnxSflowEgrCMapQueueLastChange_Type = TimeStamp
_TmnxSflowEgrCMapQueueLastChange_Object = MibTableColumn
tmnxSflowEgrCMapQueueLastChange = _TmnxSflowEgrCMapQueueLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 6, 1, 3),
    _TmnxSflowEgrCMapQueueLastChange_Type()
)
tmnxSflowEgrCMapQueueLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueLastChange.setStatus("current")


class _TmnxSflowEgrCMapQueueTrafficType_Type(TmnxSflowCounterMapTrafficType):
    """Custom type tmnxSflowEgrCMapQueueTrafficType based on TmnxSflowCounterMapTrafficType"""
    defaultValue = 1


_TmnxSflowEgrCMapQueueTrafficType_Type.__name__ = "TmnxSflowCounterMapTrafficType"
_TmnxSflowEgrCMapQueueTrafficType_Object = MibTableColumn
tmnxSflowEgrCMapQueueTrafficType = _TmnxSflowEgrCMapQueueTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 2, 6, 1, 4),
    _TmnxSflowEgrCMapQueueTrafficType_Type()
)
tmnxSflowEgrCMapQueueTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSflowEgrCMapQueueTrafficType.setStatus("current")
_TmnxSflowStatistics_ObjectIdentity = ObjectIdentity
tmnxSflowStatistics = _TmnxSflowStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3)
)
_TmnxSflowRcvrStatsTable_Object = MibTable
tmnxSflowRcvrStatsTable = _TmnxSflowRcvrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxSflowRcvrStatsTable.setStatus("current")
_TmnxSflowRcvrStatsEntry_Object = MibTableRow
tmnxSflowRcvrStatsEntry = _TmnxSflowRcvrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3, 1, 1)
)
tmnxSflowRcvrStatsEntry.setIndexNames(
    (0, "SFLOW-MIB", "sFlowRcvrIndex"),
    (0, "TIMETRA-SFLOW-MIB", "tmnxSflowRcvrType"),
)
if mibBuilder.loadTexts:
    tmnxSflowRcvrStatsEntry.setStatus("current")


class _TmnxSflowRcvrType_Type(Integer32):
    """Custom type tmnxSflowRcvrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_TmnxSflowRcvrType_Type.__name__ = "Integer32"
_TmnxSflowRcvrType_Object = MibTableColumn
tmnxSflowRcvrType = _TmnxSflowRcvrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3, 1, 1, 1),
    _TmnxSflowRcvrType_Type()
)
tmnxSflowRcvrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSflowRcvrType.setStatus("current")
_TmnxSflowRcvrLastPacketSent_Type = TimeStamp
_TmnxSflowRcvrLastPacketSent_Object = MibTableColumn
tmnxSflowRcvrLastPacketSent = _TmnxSflowRcvrLastPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3, 1, 1, 2),
    _TmnxSflowRcvrLastPacketSent_Type()
)
tmnxSflowRcvrLastPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowRcvrLastPacketSent.setStatus("current")
_TmnxSflowRcvrPacketsSent_Type = Counter32
_TmnxSflowRcvrPacketsSent_Object = MibTableColumn
tmnxSflowRcvrPacketsSent = _TmnxSflowRcvrPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3, 1, 1, 3),
    _TmnxSflowRcvrPacketsSent_Type()
)
tmnxSflowRcvrPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowRcvrPacketsSent.setStatus("current")
_TmnxSflowRcvrPacketErrors_Type = Counter32
_TmnxSflowRcvrPacketErrors_Object = MibTableColumn
tmnxSflowRcvrPacketErrors = _TmnxSflowRcvrPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 3, 1, 1, 4),
    _TmnxSflowRcvrPacketErrors_Type()
)
tmnxSflowRcvrPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSflowRcvrPacketErrors.setStatus("current")
_TmnxSflowNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxSflowNotifyObjects = _TmnxSflowNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 4)
)


class _TmnxSflowNotifyRcvrIndex_Type(Integer32):
    """Custom type tmnxSflowNotifyRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxSflowNotifyRcvrIndex_Type.__name__ = "Integer32"
_TmnxSflowNotifyRcvrIndex_Object = MibScalar
tmnxSflowNotifyRcvrIndex = _TmnxSflowNotifyRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 4, 1),
    _TmnxSflowNotifyRcvrIndex_Type()
)
tmnxSflowNotifyRcvrIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSflowNotifyRcvrIndex.setStatus("current")


class _TmnxSflowNotifyFlowFailReason_Type(Integer32):
    """Custom type tmnxSflowNotifyFlowFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("udpSendFailure", 1),
          ("cpSequenceReset", 2),
          ("cpUnreachable", 3))
    )


_TmnxSflowNotifyFlowFailReason_Type.__name__ = "Integer32"
_TmnxSflowNotifyFlowFailReason_Object = MibScalar
tmnxSflowNotifyFlowFailReason = _TmnxSflowNotifyFlowFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 95, 4, 2),
    _TmnxSflowNotifyFlowFailReason_Type()
)
tmnxSflowNotifyFlowFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSflowNotifyFlowFailReason.setStatus("current")
_TmnxSflowNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSflowNotifyPrefix = _TmnxSflowNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 95)
)
_TmnxSflowNotifications_ObjectIdentity = ObjectIdentity
tmnxSflowNotifications = _TmnxSflowNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 95, 0)
)
sFlowRcvrEntry.registerAugmentions(
    ("TIMETRA-SFLOW-MIB",
     "tmnxSflowRcvrEntry")
)
tmnxSflowRcvrEntry.setIndexNames(*sFlowRcvrEntry.getIndexNames())

# Managed Objects groups

tmnxSflowTimeStampV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2, 1, 1)
)
tmnxSflowTimeStampV12v0Group.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrTableLastChanged"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowCpTableLastChanged"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapPlcrTableLstCh"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapPlcrTableLstCh"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapQueueTableLstCh"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapQueueTableLstCh"))
)
if mibBuilder.loadTexts:
    tmnxSflowTimeStampV12v0Group.setStatus("current")

tmnxSflowConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2, 1, 2)
)
tmnxSflowConfigV12v0Group.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrLastChanged"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrBackupAddressType"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrBackupAddress"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrBackupDstPort"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowCpRowStatus"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowCpLastChanged"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapPlcrRowStatus"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapPlcrRowStatus"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapPlcrLastChange"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapPlcrLastChange"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapPlcrTrafficType"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapPlcrTrafficType"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapQueueRowStatus"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapQueueRowStatus"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapQueueLastChange"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapQueueLastChange"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowIngCMapQueueTrafficType"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowEgrCMapQueueTrafficType"))
)
if mibBuilder.loadTexts:
    tmnxSflowConfigV12v0Group.setStatus("current")

tmnxSflowNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2, 1, 3)
)
tmnxSflowNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowNotifyRcvrIndex"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowNotifyFlowFailReason"))
)
if mibBuilder.loadTexts:
    tmnxSflowNotifyObjsV12v0Group.setStatus("current")

tmnxSflowRcvrStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2, 1, 5)
)
tmnxSflowRcvrStatsV12v0Group.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrLastPacketSent"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrPacketsSent"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrPacketErrors"))
)
if mibBuilder.loadTexts:
    tmnxSflowRcvrStatsV12v0Group.setStatus("current")


# Notification objects

tmnxSflowCpEntrySampling = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 95, 0, 1)
)
tmnxSflowCpEntrySampling.setObjects(
      *(("SFLOW-MIB", "sFlowCpReceiver"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowNotifyFlowFailReason"))
)
if mibBuilder.loadTexts:
    tmnxSflowCpEntrySampling.setStatus(
        "current"
    )

tmnxSflowPacketTxFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 95, 0, 2)
)
tmnxSflowPacketTxFailure.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowNotifyRcvrIndex"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowNotifyFlowFailReason"))
)
if mibBuilder.loadTexts:
    tmnxSflowPacketTxFailure.setStatus(
        "current"
    )


# Notifications groups

tmnxSflowNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 2, 1, 4)
)
tmnxSflowNotifV12v0Group.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowCpEntrySampling"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowPacketTxFailure"))
)
if mibBuilder.loadTexts:
    tmnxSflowNotifV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSflowV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 95, 1, 1)
)
tmnxSflowV12v0Compliance.setObjects(
      *(("TIMETRA-SFLOW-MIB", "tmnxSflowTimeStampV12v0Group"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowConfigV12v0Group"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowNotifyObjsV12v0Group"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowNotifV12v0Group"),
        ("TIMETRA-SFLOW-MIB", "tmnxSflowRcvrStatsV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSflowV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SFLOW-MIB",
    **{"TmnxSflowCounterMapTrafficType": TmnxSflowCounterMapTrafficType,
       "timetraSflowMIBModule": timetraSflowMIBModule,
       "tmnxSflowConformance": tmnxSflowConformance,
       "tmnxSflowCompliances": tmnxSflowCompliances,
       "tmnxSflowV12v0Compliance": tmnxSflowV12v0Compliance,
       "tmnxSflowGroups": tmnxSflowGroups,
       "tmnxSflowV12v0Groups": tmnxSflowV12v0Groups,
       "tmnxSflowTimeStampV12v0Group": tmnxSflowTimeStampV12v0Group,
       "tmnxSflowConfigV12v0Group": tmnxSflowConfigV12v0Group,
       "tmnxSflowNotifyObjsV12v0Group": tmnxSflowNotifyObjsV12v0Group,
       "tmnxSflowNotifV12v0Group": tmnxSflowNotifV12v0Group,
       "tmnxSflowRcvrStatsV12v0Group": tmnxSflowRcvrStatsV12v0Group,
       "tmnxSflowObjs": tmnxSflowObjs,
       "tmnxSflowConfigTimeStamps": tmnxSflowConfigTimeStamps,
       "tmnxSflowRcvrTableLastChanged": tmnxSflowRcvrTableLastChanged,
       "tmnxSflowCpTableLastChanged": tmnxSflowCpTableLastChanged,
       "tmnxSflowIngCMapPlcrTableLstCh": tmnxSflowIngCMapPlcrTableLstCh,
       "tmnxSflowEgrCMapPlcrTableLstCh": tmnxSflowEgrCMapPlcrTableLstCh,
       "tmnxSflowIngCMapQueueTableLstCh": tmnxSflowIngCMapQueueTableLstCh,
       "tmnxSflowEgrCMapQueueTableLstCh": tmnxSflowEgrCMapQueueTableLstCh,
       "tmnxSflowConfigurations": tmnxSflowConfigurations,
       "tmnxSflowRcvrTable": tmnxSflowRcvrTable,
       "tmnxSflowRcvrEntry": tmnxSflowRcvrEntry,
       "tmnxSflowRcvrLastChanged": tmnxSflowRcvrLastChanged,
       "tmnxSflowRcvrBackupAddressType": tmnxSflowRcvrBackupAddressType,
       "tmnxSflowRcvrBackupAddress": tmnxSflowRcvrBackupAddress,
       "tmnxSflowRcvrBackupDstPort": tmnxSflowRcvrBackupDstPort,
       "tmnxSflowCpTable": tmnxSflowCpTable,
       "tmnxSflowCpEntry": tmnxSflowCpEntry,
       "tmnxSflowCpRowStatus": tmnxSflowCpRowStatus,
       "tmnxSflowCpLastChanged": tmnxSflowCpLastChanged,
       "tmnxSflowIngCMapPlcrTable": tmnxSflowIngCMapPlcrTable,
       "tmnxSflowIngCMapPlcrEntry": tmnxSflowIngCMapPlcrEntry,
       "tmnxSflowIngCMapPlcrId": tmnxSflowIngCMapPlcrId,
       "tmnxSflowIngCMapPlcrRowStatus": tmnxSflowIngCMapPlcrRowStatus,
       "tmnxSflowIngCMapPlcrLastChange": tmnxSflowIngCMapPlcrLastChange,
       "tmnxSflowIngCMapPlcrTrafficType": tmnxSflowIngCMapPlcrTrafficType,
       "tmnxSflowEgrCMapPlcrTable": tmnxSflowEgrCMapPlcrTable,
       "tmnxSflowEgrCMapPlcrEntry": tmnxSflowEgrCMapPlcrEntry,
       "tmnxSflowEgrCMapPlcrId": tmnxSflowEgrCMapPlcrId,
       "tmnxSflowEgrCMapPlcrRowStatus": tmnxSflowEgrCMapPlcrRowStatus,
       "tmnxSflowEgrCMapPlcrLastChange": tmnxSflowEgrCMapPlcrLastChange,
       "tmnxSflowEgrCMapPlcrTrafficType": tmnxSflowEgrCMapPlcrTrafficType,
       "tmnxSflowIngCMapQueueTable": tmnxSflowIngCMapQueueTable,
       "tmnxSflowIngCMapQueueEntry": tmnxSflowIngCMapQueueEntry,
       "tmnxSflowIngCMapQueueId": tmnxSflowIngCMapQueueId,
       "tmnxSflowIngCMapQueueRowStatus": tmnxSflowIngCMapQueueRowStatus,
       "tmnxSflowIngCMapQueueLastChange": tmnxSflowIngCMapQueueLastChange,
       "tmnxSflowIngCMapQueueTrafficType": tmnxSflowIngCMapQueueTrafficType,
       "tmnxSflowEgrCMapQueueTable": tmnxSflowEgrCMapQueueTable,
       "tmnxSflowEgrCMapQueueEntry": tmnxSflowEgrCMapQueueEntry,
       "tmnxSflowEgrCMapQueueId": tmnxSflowEgrCMapQueueId,
       "tmnxSflowEgrCMapQueueRowStatus": tmnxSflowEgrCMapQueueRowStatus,
       "tmnxSflowEgrCMapQueueLastChange": tmnxSflowEgrCMapQueueLastChange,
       "tmnxSflowEgrCMapQueueTrafficType": tmnxSflowEgrCMapQueueTrafficType,
       "tmnxSflowStatistics": tmnxSflowStatistics,
       "tmnxSflowRcvrStatsTable": tmnxSflowRcvrStatsTable,
       "tmnxSflowRcvrStatsEntry": tmnxSflowRcvrStatsEntry,
       "tmnxSflowRcvrType": tmnxSflowRcvrType,
       "tmnxSflowRcvrLastPacketSent": tmnxSflowRcvrLastPacketSent,
       "tmnxSflowRcvrPacketsSent": tmnxSflowRcvrPacketsSent,
       "tmnxSflowRcvrPacketErrors": tmnxSflowRcvrPacketErrors,
       "tmnxSflowNotifyObjects": tmnxSflowNotifyObjects,
       "tmnxSflowNotifyRcvrIndex": tmnxSflowNotifyRcvrIndex,
       "tmnxSflowNotifyFlowFailReason": tmnxSflowNotifyFlowFailReason,
       "tmnxSflowNotifyPrefix": tmnxSflowNotifyPrefix,
       "tmnxSflowNotifications": tmnxSflowNotifications,
       "tmnxSflowCpEntrySampling": tmnxSflowCpEntrySampling,
       "tmnxSflowPacketTxFailure": tmnxSflowPacketTxFailure}
)
