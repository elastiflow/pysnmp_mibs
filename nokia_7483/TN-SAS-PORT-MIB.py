# SNMP MIB module (TN-SAS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-SAS-PORT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:36 2025
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnPortEntry,
 tnPortEtherEntry,
 tnPortPortID) = mibBuilder.importSymbols(
    "TN-PORT-MIB",
    "tnPortEntry",
    "tnPortEtherEntry",
    "tnPortPortID")

(ServObjDesc,
 TNamedItem,
 TNamedItemOrEmpty,
 TQueueId,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "ServObjDesc",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TQueueId",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId")

(tnSASModules,
 tnSASObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnSASPortMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tnSASPortMIBModule.setRevisions(
        ("1912-09-01 00:00",
         "1908-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSASPortObjs_ObjectIdentity = ObjectIdentity
tnSASPortObjs = _TnSASPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2)
)
_TnSASPortExtnTable_Object = MibTable
tnSASPortExtnTable = _TnSASPortExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSASPortExtnTable.setStatus("current")
_TnSASPortExtnEntry_Object = MibTableRow
tnSASPortExtnEntry = _TnSASPortExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSASPortExtnEntry.setStatus("current")
_TnPortUplinkMode_Type = TruthValue
_TnPortUplinkMode_Object = MibTableColumn
tnPortUplinkMode = _TnPortUplinkMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 2, 1, 1),
    _TnPortUplinkMode_Type()
)
tnPortUplinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortUplinkMode.setStatus("current")


class _TnPortAccessEgressQoSPolicyId_Type(Unsigned32):
    """Custom type tnPortAccessEgressQoSPolicyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnPortAccessEgressQoSPolicyId_Type.__name__ = "Unsigned32"
_TnPortAccessEgressQoSPolicyId_Object = MibTableColumn
tnPortAccessEgressQoSPolicyId = _TnPortAccessEgressQoSPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 2, 1, 2),
    _TnPortAccessEgressQoSPolicyId_Type()
)
tnPortAccessEgressQoSPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortAccessEgressQoSPolicyId.setStatus("current")


class _TnPortNetworkQoSPolicyId_Type(Unsigned32):
    """Custom type tnPortNetworkQoSPolicyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnPortNetworkQoSPolicyId_Type.__name__ = "Unsigned32"
_TnPortNetworkQoSPolicyId_Object = MibTableColumn
tnPortNetworkQoSPolicyId = _TnPortNetworkQoSPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 2, 1, 3),
    _TnPortNetworkQoSPolicyId_Type()
)
tnPortNetworkQoSPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortNetworkQoSPolicyId.setStatus("current")
_TnPortShgGroupName_Type = TNamedItemOrEmpty
_TnPortShgGroupName_Object = MibTableColumn
tnPortShgGroupName = _TnPortShgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 2, 1, 4),
    _TnPortShgGroupName_Type()
)
tnPortShgGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortShgGroupName.setStatus("current")
_TnSASPortEtherExtnTable_Object = MibTable
tnSASPortEtherExtnTable = _TnSASPortEtherExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnSASPortEtherExtnTable.setStatus("current")
_TnSASPortEtherExtnEntry_Object = MibTableRow
tnSASPortEtherExtnEntry = _TnSASPortEtherExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnSASPortEtherExtnEntry.setStatus("current")


class _TnPortEtherEgressMaxBurst_Type(Integer32):
    """Custom type tnPortEtherEgressMaxBurst based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(32, 16384),
    )


_TnPortEtherEgressMaxBurst_Type.__name__ = "Integer32"
_TnPortEtherEgressMaxBurst_Object = MibTableColumn
tnPortEtherEgressMaxBurst = _TnPortEtherEgressMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 1),
    _TnPortEtherEgressMaxBurst_Type()
)
tnPortEtherEgressMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherEgressMaxBurst.setStatus("current")
_TnPortStatsQueue1PktsFwd_Type = TruthValue
_TnPortStatsQueue1PktsFwd_Object = MibTableColumn
tnPortStatsQueue1PktsFwd = _TnPortStatsQueue1PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 2),
    _TnPortStatsQueue1PktsFwd_Type()
)
tnPortStatsQueue1PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue1PktsFwd.setStatus("current")
_TnPortStatsQueue2PktsFwd_Type = TruthValue
_TnPortStatsQueue2PktsFwd_Object = MibTableColumn
tnPortStatsQueue2PktsFwd = _TnPortStatsQueue2PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 3),
    _TnPortStatsQueue2PktsFwd_Type()
)
tnPortStatsQueue2PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue2PktsFwd.setStatus("current")
_TnPortStatsQueue3PktsFwd_Type = TruthValue
_TnPortStatsQueue3PktsFwd_Object = MibTableColumn
tnPortStatsQueue3PktsFwd = _TnPortStatsQueue3PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 4),
    _TnPortStatsQueue3PktsFwd_Type()
)
tnPortStatsQueue3PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue3PktsFwd.setStatus("current")
_TnPortStatsQueue4PktsFwd_Type = TruthValue
_TnPortStatsQueue4PktsFwd_Object = MibTableColumn
tnPortStatsQueue4PktsFwd = _TnPortStatsQueue4PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 5),
    _TnPortStatsQueue4PktsFwd_Type()
)
tnPortStatsQueue4PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue4PktsFwd.setStatus("current")
_TnPortStatsQueue5PktsFwd_Type = TruthValue
_TnPortStatsQueue5PktsFwd_Object = MibTableColumn
tnPortStatsQueue5PktsFwd = _TnPortStatsQueue5PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 6),
    _TnPortStatsQueue5PktsFwd_Type()
)
tnPortStatsQueue5PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue5PktsFwd.setStatus("current")
_TnPortStatsQueue6PktsFwd_Type = TruthValue
_TnPortStatsQueue6PktsFwd_Object = MibTableColumn
tnPortStatsQueue6PktsFwd = _TnPortStatsQueue6PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 7),
    _TnPortStatsQueue6PktsFwd_Type()
)
tnPortStatsQueue6PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue6PktsFwd.setStatus("current")
_TnPortStatsQueue7PktsFwd_Type = TruthValue
_TnPortStatsQueue7PktsFwd_Object = MibTableColumn
tnPortStatsQueue7PktsFwd = _TnPortStatsQueue7PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 8),
    _TnPortStatsQueue7PktsFwd_Type()
)
tnPortStatsQueue7PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue7PktsFwd.setStatus("current")
_TnPortStatsQueue8PktsFwd_Type = TruthValue
_TnPortStatsQueue8PktsFwd_Object = MibTableColumn
tnPortStatsQueue8PktsFwd = _TnPortStatsQueue8PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 9),
    _TnPortStatsQueue8PktsFwd_Type()
)
tnPortStatsQueue8PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortStatsQueue8PktsFwd.setStatus("current")


class _TnPortEtherEgrSchedMode_Type(Integer32):
    """Custom type tnPortEtherEgrSchedMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fc-based", 1),
          ("sap-based", 2))
    )


_TnPortEtherEgrSchedMode_Type.__name__ = "Integer32"
_TnPortEtherEgrSchedMode_Object = MibTableColumn
tnPortEtherEgrSchedMode = _TnPortEtherEgrSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 10),
    _TnPortEtherEgrSchedMode_Type()
)
tnPortEtherEgrSchedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherEgrSchedMode.setStatus("current")


class _TnPortEtherLoopback_Type(Integer32):
    """Custom type tnPortEtherLoopback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("internal", 2))
    )


_TnPortEtherLoopback_Type.__name__ = "Integer32"
_TnPortEtherLoopback_Object = MibTableColumn
tnPortEtherLoopback = _TnPortEtherLoopback_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 11),
    _TnPortEtherLoopback_Type()
)
tnPortEtherLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherLoopback.setStatus("current")


class _TnPortEtherIpMTU_Type(Unsigned32):
    """Custom type tnPortEtherIpMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TnPortEtherIpMTU_Type.__name__ = "Unsigned32"
_TnPortEtherIpMTU_Object = MibTableColumn
tnPortEtherIpMTU = _TnPortEtherIpMTU_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 12),
    _TnPortEtherIpMTU_Type()
)
tnPortEtherIpMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherIpMTU.setStatus("current")
if mibBuilder.loadTexts:
    tnPortEtherIpMTU.setUnits("bytes")


class _TnPortEtherClockConfig_Type(Integer32):
    """Custom type tnPortEtherClockConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("automatic", 1),
          ("manual-master", 2),
          ("manual-slave", 3))
    )


_TnPortEtherClockConfig_Type.__name__ = "Integer32"
_TnPortEtherClockConfig_Object = MibTableColumn
tnPortEtherClockConfig = _TnPortEtherClockConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 13),
    _TnPortEtherClockConfig_Type()
)
tnPortEtherClockConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortEtherClockConfig.setStatus("current")
_TnPortLoopbckServId_Type = TmnxServId
_TnPortLoopbckServId_Object = MibTableColumn
tnPortLoopbckServId = _TnPortLoopbckServId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 14),
    _TnPortLoopbckServId_Type()
)
tnPortLoopbckServId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLoopbckServId.setStatus("current")
_TnPortLoopbckSapPortId_Type = TmnxPortID
_TnPortLoopbckSapPortId_Object = MibTableColumn
tnPortLoopbckSapPortId = _TnPortLoopbckSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 15),
    _TnPortLoopbckSapPortId_Type()
)
tnPortLoopbckSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLoopbckSapPortId.setStatus("current")
_TnPortLoopbckSapEncapVal_Type = TmnxEncapVal
_TnPortLoopbckSapEncapVal_Object = MibTableColumn
tnPortLoopbckSapEncapVal = _TnPortLoopbckSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 16),
    _TnPortLoopbckSapEncapVal_Type()
)
tnPortLoopbckSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLoopbckSapEncapVal.setStatus("current")
_TnPortLoopbckSrcMacAddr_Type = MacAddress
_TnPortLoopbckSrcMacAddr_Object = MibTableColumn
tnPortLoopbckSrcMacAddr = _TnPortLoopbckSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 17),
    _TnPortLoopbckSrcMacAddr_Type()
)
tnPortLoopbckSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLoopbckSrcMacAddr.setStatus("current")
_TnPortLoopbckDstMacAddr_Type = MacAddress
_TnPortLoopbckDstMacAddr_Object = MibTableColumn
tnPortLoopbckDstMacAddr = _TnPortLoopbckDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 18),
    _TnPortLoopbckDstMacAddr_Type()
)
tnPortLoopbckDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortLoopbckDstMacAddr.setStatus("current")


class _TnPortAccEgrSapQosMarking_Type(Integer32):
    """Custom type tnPortAccEgrSapQosMarking based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnPortAccEgrSapQosMarking_Type.__name__ = "Integer32"
_TnPortAccEgrSapQosMarking_Object = MibTableColumn
tnPortAccEgrSapQosMarking = _TnPortAccEgrSapQosMarking_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 4, 1, 19),
    _TnPortAccEgrSapQosMarking_Type()
)
tnPortAccEgrSapQosMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPortAccEgrSapQosMarking.setStatus("current")
_TnPortShgInfoTable_Object = MibTable
tnPortShgInfoTable = _TnPortShgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tnPortShgInfoTable.setStatus("current")
_TnPortShgInfoEntry_Object = MibTableRow
tnPortShgInfoEntry = _TnPortShgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6, 1)
)
tnPortShgInfoEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (1, "TN-SAS-PORT-MIB", "tnPortShgName"),
)
if mibBuilder.loadTexts:
    tnPortShgInfoEntry.setStatus("current")
_TnPortShgName_Type = TNamedItem
_TnPortShgName_Object = MibTableColumn
tnPortShgName = _TnPortShgName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6, 1, 1),
    _TnPortShgName_Type()
)
tnPortShgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortShgName.setStatus("current")
_TnPortShgRowStatus_Type = RowStatus
_TnPortShgRowStatus_Object = MibTableColumn
tnPortShgRowStatus = _TnPortShgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6, 1, 2),
    _TnPortShgRowStatus_Type()
)
tnPortShgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortShgRowStatus.setStatus("current")
_TnPortShgInstanceId_Type = Unsigned32
_TnPortShgInstanceId_Object = MibTableColumn
tnPortShgInstanceId = _TnPortShgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6, 1, 3),
    _TnPortShgInstanceId_Type()
)
tnPortShgInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortShgInstanceId.setStatus("current")


class _TnPortShgDescription_Type(ServObjDesc):
    """Custom type tnPortShgDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_TnPortShgDescription_Type.__name__ = "ServObjDesc"
_TnPortShgDescription_Object = MibTableColumn
tnPortShgDescription = _TnPortShgDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6, 1, 4),
    _TnPortShgDescription_Type()
)
tnPortShgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPortShgDescription.setStatus("current")
_TnPortShgLastMgmtChange_Type = TimeStamp
_TnPortShgLastMgmtChange_Object = MibTableColumn
tnPortShgLastMgmtChange = _TnPortShgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 6, 1, 5),
    _TnPortShgLastMgmtChange_Type()
)
tnPortShgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortShgLastMgmtChange.setStatus("current")
_TnPortNetEgressQueueStatsTable_Object = MibTable
tnPortNetEgressQueueStatsTable = _TnPortNetEgressQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsTable.setStatus("current")
_TnPortNetEgressQueueStatsEntry_Object = MibTableRow
tnPortNetEgressQueueStatsEntry = _TnPortNetEgressQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1)
)
tnPortNetEgressQueueStatsEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-SAS-PORT-MIB", "tnPortNetEgressQueueStatsIndex"),
)
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsEntry.setStatus("current")


class _TnPortNetEgressQueueStatsIndex_Type(TQueueId):
    """Custom type tnPortNetEgressQueueStatsIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnPortNetEgressQueueStatsIndex_Type.__name__ = "TQueueId"
_TnPortNetEgressQueueStatsIndex_Object = MibTableColumn
tnPortNetEgressQueueStatsIndex = _TnPortNetEgressQueueStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 1),
    _TnPortNetEgressQueueStatsIndex_Type()
)
tnPortNetEgressQueueStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsIndex.setStatus("current")
_TnPortNetEgressQueueStatsFwdPkts_Type = Counter64
_TnPortNetEgressQueueStatsFwdPkts_Object = MibTableColumn
tnPortNetEgressQueueStatsFwdPkts = _TnPortNetEgressQueueStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 2),
    _TnPortNetEgressQueueStatsFwdPkts_Type()
)
tnPortNetEgressQueueStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsFwdPkts.setStatus("current")
_TnPortNetEgressQueueStatsFwdOcts_Type = Counter64
_TnPortNetEgressQueueStatsFwdOcts_Object = MibTableColumn
tnPortNetEgressQueueStatsFwdOcts = _TnPortNetEgressQueueStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 3),
    _TnPortNetEgressQueueStatsFwdOcts_Type()
)
tnPortNetEgressQueueStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsFwdOcts.setStatus("current")
_TnPortNetEgressQueueStatsDroPkts_Type = Counter64
_TnPortNetEgressQueueStatsDroPkts_Object = MibTableColumn
tnPortNetEgressQueueStatsDroPkts = _TnPortNetEgressQueueStatsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 4),
    _TnPortNetEgressQueueStatsDroPkts_Type()
)
tnPortNetEgressQueueStatsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsDroPkts.setStatus("current")
_TnPortNetEgressQueueStatsDroOcts_Type = Counter64
_TnPortNetEgressQueueStatsDroOcts_Object = MibTableColumn
tnPortNetEgressQueueStatsDroOcts = _TnPortNetEgressQueueStatsDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 5),
    _TnPortNetEgressQueueStatsDroOcts_Type()
)
tnPortNetEgressQueueStatsDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsDroOcts.setStatus("current")
_TnPortNetEgressQueueStatsInProfDroPkts_Type = Counter64
_TnPortNetEgressQueueStatsInProfDroPkts_Object = MibTableColumn
tnPortNetEgressQueueStatsInProfDroPkts = _TnPortNetEgressQueueStatsInProfDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 6),
    _TnPortNetEgressQueueStatsInProfDroPkts_Type()
)
tnPortNetEgressQueueStatsInProfDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsInProfDroPkts.setStatus("current")
_TnPortNetEgressQueueStatsInProfDroOcts_Type = Counter64
_TnPortNetEgressQueueStatsInProfDroOcts_Object = MibTableColumn
tnPortNetEgressQueueStatsInProfDroOcts = _TnPortNetEgressQueueStatsInProfDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 7),
    _TnPortNetEgressQueueStatsInProfDroOcts_Type()
)
tnPortNetEgressQueueStatsInProfDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsInProfDroOcts.setStatus("current")
_TnPortNetEgressQueueStatsOutProfDroPkts_Type = Counter64
_TnPortNetEgressQueueStatsOutProfDroPkts_Object = MibTableColumn
tnPortNetEgressQueueStatsOutProfDroPkts = _TnPortNetEgressQueueStatsOutProfDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 8),
    _TnPortNetEgressQueueStatsOutProfDroPkts_Type()
)
tnPortNetEgressQueueStatsOutProfDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsOutProfDroPkts.setStatus("current")
_TnPortNetEgressQueueStatsOutProfDroOcts_Type = Counter64
_TnPortNetEgressQueueStatsOutProfDroOcts_Object = MibTableColumn
tnPortNetEgressQueueStatsOutProfDroOcts = _TnPortNetEgressQueueStatsOutProfDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 8, 1, 9),
    _TnPortNetEgressQueueStatsOutProfDroOcts_Type()
)
tnPortNetEgressQueueStatsOutProfDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPortNetEgressQueueStatsOutProfDroOcts.setStatus("current")
_TnSASPortScalar1_Type = Unsigned32
_TnSASPortScalar1_Object = MibScalar
tnSASPortScalar1 = _TnSASPortScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 101),
    _TnSASPortScalar1_Type()
)
tnSASPortScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASPortScalar1.setStatus("current")
_TnSASPortScalar2_Type = Unsigned32
_TnSASPortScalar2_Object = MibScalar
tnSASPortScalar2 = _TnSASPortScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 2, 102),
    _TnSASPortScalar2_Type()
)
tnSASPortScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSASPortScalar2.setStatus("current")
tnPortEntry.registerAugmentions(
    ("TN-SAS-PORT-MIB",
     "tnSASPortExtnEntry")
)
tnSASPortExtnEntry.setIndexNames(*tnPortEntry.getIndexNames())
tnPortEtherEntry.registerAugmentions(
    ("TN-SAS-PORT-MIB",
     "tnSASPortEtherExtnEntry")
)
tnSASPortEtherExtnEntry.setIndexNames(*tnPortEtherEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-PORT-MIB",
    **{"tnSASPortMIBModule": tnSASPortMIBModule,
       "tnSASPortObjs": tnSASPortObjs,
       "tnSASPortExtnTable": tnSASPortExtnTable,
       "tnSASPortExtnEntry": tnSASPortExtnEntry,
       "tnPortUplinkMode": tnPortUplinkMode,
       "tnPortAccessEgressQoSPolicyId": tnPortAccessEgressQoSPolicyId,
       "tnPortNetworkQoSPolicyId": tnPortNetworkQoSPolicyId,
       "tnPortShgGroupName": tnPortShgGroupName,
       "tnSASPortEtherExtnTable": tnSASPortEtherExtnTable,
       "tnSASPortEtherExtnEntry": tnSASPortEtherExtnEntry,
       "tnPortEtherEgressMaxBurst": tnPortEtherEgressMaxBurst,
       "tnPortStatsQueue1PktsFwd": tnPortStatsQueue1PktsFwd,
       "tnPortStatsQueue2PktsFwd": tnPortStatsQueue2PktsFwd,
       "tnPortStatsQueue3PktsFwd": tnPortStatsQueue3PktsFwd,
       "tnPortStatsQueue4PktsFwd": tnPortStatsQueue4PktsFwd,
       "tnPortStatsQueue5PktsFwd": tnPortStatsQueue5PktsFwd,
       "tnPortStatsQueue6PktsFwd": tnPortStatsQueue6PktsFwd,
       "tnPortStatsQueue7PktsFwd": tnPortStatsQueue7PktsFwd,
       "tnPortStatsQueue8PktsFwd": tnPortStatsQueue8PktsFwd,
       "tnPortEtherEgrSchedMode": tnPortEtherEgrSchedMode,
       "tnPortEtherLoopback": tnPortEtherLoopback,
       "tnPortEtherIpMTU": tnPortEtherIpMTU,
       "tnPortEtherClockConfig": tnPortEtherClockConfig,
       "tnPortLoopbckServId": tnPortLoopbckServId,
       "tnPortLoopbckSapPortId": tnPortLoopbckSapPortId,
       "tnPortLoopbckSapEncapVal": tnPortLoopbckSapEncapVal,
       "tnPortLoopbckSrcMacAddr": tnPortLoopbckSrcMacAddr,
       "tnPortLoopbckDstMacAddr": tnPortLoopbckDstMacAddr,
       "tnPortAccEgrSapQosMarking": tnPortAccEgrSapQosMarking,
       "tnPortShgInfoTable": tnPortShgInfoTable,
       "tnPortShgInfoEntry": tnPortShgInfoEntry,
       "tnPortShgName": tnPortShgName,
       "tnPortShgRowStatus": tnPortShgRowStatus,
       "tnPortShgInstanceId": tnPortShgInstanceId,
       "tnPortShgDescription": tnPortShgDescription,
       "tnPortShgLastMgmtChange": tnPortShgLastMgmtChange,
       "tnPortNetEgressQueueStatsTable": tnPortNetEgressQueueStatsTable,
       "tnPortNetEgressQueueStatsEntry": tnPortNetEgressQueueStatsEntry,
       "tnPortNetEgressQueueStatsIndex": tnPortNetEgressQueueStatsIndex,
       "tnPortNetEgressQueueStatsFwdPkts": tnPortNetEgressQueueStatsFwdPkts,
       "tnPortNetEgressQueueStatsFwdOcts": tnPortNetEgressQueueStatsFwdOcts,
       "tnPortNetEgressQueueStatsDroPkts": tnPortNetEgressQueueStatsDroPkts,
       "tnPortNetEgressQueueStatsDroOcts": tnPortNetEgressQueueStatsDroOcts,
       "tnPortNetEgressQueueStatsInProfDroPkts": tnPortNetEgressQueueStatsInProfDroPkts,
       "tnPortNetEgressQueueStatsInProfDroOcts": tnPortNetEgressQueueStatsInProfDroOcts,
       "tnPortNetEgressQueueStatsOutProfDroPkts": tnPortNetEgressQueueStatsOutProfDroPkts,
       "tnPortNetEgressQueueStatsOutProfDroOcts": tnPortNetEgressQueueStatsOutProfDroOcts,
       "tnSASPortScalar1": tnSASPortScalar1,
       "tnSASPortScalar2": tnSASPortScalar2}
)
