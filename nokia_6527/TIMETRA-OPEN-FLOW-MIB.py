# SNMP MIB module (TIMETRA-OPEN-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-OPEN-FLOW-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:39 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TLNamedItemOrEmpty,
 TNamedItem,
 TmnxAdminState,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxPortID")


# MODULE-IDENTITY

timetraOpenFlowMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 93)
)
if mibBuilder.loadTexts:
    timetraOpenFlowMIBModule.setRevisions(
        ("2014-01-01 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOFDatapathIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxOFPktType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("hello", 1),
          ("error", 2),
          ("echoRequest", 3),
          ("echoReply", 4),
          ("experimenter", 5),
          ("featureRequest", 6),
          ("featureReply", 7),
          ("getConfigRequest", 8),
          ("getConfigReply", 9),
          ("setConfig", 10),
          ("packetIn", 11),
          ("flowRemoved", 12),
          ("portStatus", 13),
          ("packetOut", 14),
          ("flowMod", 15),
          ("groupMod", 16),
          ("portMod", 17),
          ("tableMod", 18),
          ("multipartRequest", 19),
          ("multipartReply", 20),
          ("barrierRequest", 21),
          ("barrierReply", 22),
          ("getQueueConfigRequest", 23),
          ("getQueueConfigReply", 24),
          ("roleRequest", 25),
          ("roleReply", 26),
          ("getAsyncRequest", 27),
          ("getAsyncReply", 28),
          ("setAsync", 29),
          ("meterMod", 30))
    )



class TmnxOFAsyncFltrPacketIn(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tableMiss", 0),
          ("applyAction", 1),
          ("invalidTTL", 2))
    )


class TmnxOFAsyncFltrPortStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("portAdd", 0),
          ("portDelete", 1),
          ("portModify", 2))
    )


class TmnxOFAsyncFltrFlowRemoved(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("idleTimeOut", 0),
          ("hardTimeOut", 1),
          ("flowModDelete", 2),
          ("groupDelete", 3))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxOpenFlowConformance_ObjectIdentity = ObjectIdentity
tmnxOpenFlowConformance = _TmnxOpenFlowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93)
)
_TmnxOpenFlowCompliances_ObjectIdentity = ObjectIdentity
tmnxOpenFlowCompliances = _TmnxOpenFlowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1)
)
_TmnxOpenFlowGroups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowGroups = _TmnxOpenFlowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2)
)
_TmnxOpenFlowV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowV12v0Groups = _TmnxOpenFlowV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1)
)
_TmnxOpenFlowNotifGroups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotifGroups = _TmnxOpenFlowNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 3)
)
_TmnxOpenFlow_ObjectIdentity = ObjectIdentity
tmnxOpenFlow = _TmnxOpenFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93)
)
_TmnxOpenFlowObjs_ObjectIdentity = ObjectIdentity
tmnxOpenFlowObjs = _TmnxOpenFlowObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1)
)
_TmnxOFSwitchTableLastChanged_Type = TimeStamp
_TmnxOFSwitchTableLastChanged_Object = MibScalar
tmnxOFSwitchTableLastChanged = _TmnxOFSwitchTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 1),
    _TmnxOFSwitchTableLastChanged_Type()
)
tmnxOFSwitchTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchTableLastChanged.setStatus("current")
_TmnxOFSwitchTable_Object = MibTable
tmnxOFSwitchTable = _TmnxOFSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxOFSwitchTable.setStatus("current")
_TmnxOFSwitchEntry_Object = MibTableRow
tmnxOFSwitchEntry = _TmnxOFSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1)
)
tmnxOFSwitchEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
)
if mibBuilder.loadTexts:
    tmnxOFSwitchEntry.setStatus("current")
_TmnxOFSwitchName_Type = TNamedItem
_TmnxOFSwitchName_Object = MibTableColumn
tmnxOFSwitchName = _TmnxOFSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 1),
    _TmnxOFSwitchName_Type()
)
tmnxOFSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFSwitchName.setStatus("current")
_TmnxOFSwitchRowStatus_Type = RowStatus
_TmnxOFSwitchRowStatus_Object = MibTableColumn
tmnxOFSwitchRowStatus = _TmnxOFSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 2),
    _TmnxOFSwitchRowStatus_Type()
)
tmnxOFSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchRowStatus.setStatus("current")
_TmnxOFSwitchLastChanged_Type = TimeStamp
_TmnxOFSwitchLastChanged_Object = MibTableColumn
tmnxOFSwitchLastChanged = _TmnxOFSwitchLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 3),
    _TmnxOFSwitchLastChanged_Type()
)
tmnxOFSwitchLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchLastChanged.setStatus("current")


class _TmnxOFSwitchEchoInterval_Type(Unsigned32):
    """Custom type tmnxOFSwitchEchoInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxOFSwitchEchoInterval_Type.__name__ = "Unsigned32"
_TmnxOFSwitchEchoInterval_Object = MibTableColumn
tmnxOFSwitchEchoInterval = _TmnxOFSwitchEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 4),
    _TmnxOFSwitchEchoInterval_Type()
)
tmnxOFSwitchEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFSwitchEchoInterval.setUnits("seconds")


class _TmnxOFSwitchEchoMultiple_Type(Unsigned32):
    """Custom type tmnxOFSwitchEchoMultiple based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxOFSwitchEchoMultiple_Type.__name__ = "Unsigned32"
_TmnxOFSwitchEchoMultiple_Object = MibTableColumn
tmnxOFSwitchEchoMultiple = _TmnxOFSwitchEchoMultiple_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 5),
    _TmnxOFSwitchEchoMultiple_Type()
)
tmnxOFSwitchEchoMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchEchoMultiple.setStatus("current")


class _TmnxOFSwitchLogicalPortStatus_Type(Bits):
    """Custom type tmnxOFSwitchLogicalPortStatus based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("rsvp-te", 0),
          ("mpls-tp", 1))
    )

_TmnxOFSwitchLogicalPortStatus_Type.__name__ = "Bits"
_TmnxOFSwitchLogicalPortStatus_Object = MibTableColumn
tmnxOFSwitchLogicalPortStatus = _TmnxOFSwitchLogicalPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 6),
    _TmnxOFSwitchLogicalPortStatus_Type()
)
tmnxOFSwitchLogicalPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchLogicalPortStatus.setStatus("current")


class _TmnxOFSwitchAdminState_Type(TmnxAdminState):
    """Custom type tmnxOFSwitchAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOFSwitchAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOFSwitchAdminState_Object = MibTableColumn
tmnxOFSwitchAdminState = _TmnxOFSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 7),
    _TmnxOFSwitchAdminState_Type()
)
tmnxOFSwitchAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchAdminState.setStatus("current")


class _TmnxOFSwitchDescription_Type(DisplayString):
    """Custom type tmnxOFSwitchDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxOFSwitchDescription_Type.__name__ = "DisplayString"
_TmnxOFSwitchDescription_Object = MibTableColumn
tmnxOFSwitchDescription = _TmnxOFSwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 8),
    _TmnxOFSwitchDescription_Type()
)
tmnxOFSwitchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchDescription.setStatus("current")
_TmnxOFSwitchDataPathID_Type = TmnxOFDatapathIdentifier
_TmnxOFSwitchDataPathID_Object = MibTableColumn
tmnxOFSwitchDataPathID = _TmnxOFSwitchDataPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 9),
    _TmnxOFSwitchDataPathID_Type()
)
tmnxOFSwitchDataPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchDataPathID.setStatus("current")
_TmnxOFSwitchFeaturesBufferSize_Type = Unsigned32
_TmnxOFSwitchFeaturesBufferSize_Object = MibTableColumn
tmnxOFSwitchFeaturesBufferSize = _TmnxOFSwitchFeaturesBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 10),
    _TmnxOFSwitchFeaturesBufferSize_Type()
)
tmnxOFSwitchFeaturesBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchFeaturesBufferSize.setStatus("current")
_TmnxOFSwitchFeaturesNumTables_Type = Unsigned32
_TmnxOFSwitchFeaturesNumTables_Object = MibTableColumn
tmnxOFSwitchFeaturesNumTables = _TmnxOFSwitchFeaturesNumTables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 11),
    _TmnxOFSwitchFeaturesNumTables_Type()
)
tmnxOFSwitchFeaturesNumTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchFeaturesNumTables.setStatus("current")


class _TmnxOFSwitchFeaturesCapability_Type(Bits):
    """Custom type tmnxOFSwitchFeaturesCapability based on Bits"""
    namedValues = NamedValues(
        *(("flow-stats", 0),
          ("table-stats", 1),
          ("port-stats", 2))
    )

_TmnxOFSwitchFeaturesCapability_Type.__name__ = "Bits"
_TmnxOFSwitchFeaturesCapability_Object = MibTableColumn
tmnxOFSwitchFeaturesCapability = _TmnxOFSwitchFeaturesCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 12),
    _TmnxOFSwitchFeaturesCapability_Type()
)
tmnxOFSwitchFeaturesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchFeaturesCapability.setStatus("current")
_TmnxOFControllerTableLastChanged_Type = TimeStamp
_TmnxOFControllerTableLastChanged_Object = MibScalar
tmnxOFControllerTableLastChanged = _TmnxOFControllerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 3),
    _TmnxOFControllerTableLastChanged_Type()
)
tmnxOFControllerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerTableLastChanged.setStatus("current")
_TmnxOFControllerTable_Object = MibTable
tmnxOFControllerTable = _TmnxOFControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOFControllerTable.setStatus("current")
_TmnxOFControllerEntry_Object = MibTableRow
tmnxOFControllerEntry = _TmnxOFControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1)
)
tmnxOFControllerEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddressType"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddress"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTCPPort"),
)
if mibBuilder.loadTexts:
    tmnxOFControllerEntry.setStatus("current")
_TmnxOFControllerAddressType_Type = InetAddressType
_TmnxOFControllerAddressType_Object = MibTableColumn
tmnxOFControllerAddressType = _TmnxOFControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 1),
    _TmnxOFControllerAddressType_Type()
)
tmnxOFControllerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFControllerAddressType.setStatus("current")


class _TmnxOFControllerAddress_Type(InetAddress):
    """Custom type tmnxOFControllerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFControllerAddress_Type.__name__ = "InetAddress"
_TmnxOFControllerAddress_Object = MibTableColumn
tmnxOFControllerAddress = _TmnxOFControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 2),
    _TmnxOFControllerAddress_Type()
)
tmnxOFControllerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFControllerAddress.setStatus("current")


class _TmnxOFControllerTCPPort_Type(InetPortNumber):
    """Custom type tmnxOFControllerTCPPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOFControllerTCPPort_Type.__name__ = "InetPortNumber"
_TmnxOFControllerTCPPort_Object = MibTableColumn
tmnxOFControllerTCPPort = _TmnxOFControllerTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 3),
    _TmnxOFControllerTCPPort_Type()
)
tmnxOFControllerTCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFControllerTCPPort.setStatus("current")
_TmnxOFControllerRowStatus_Type = RowStatus
_TmnxOFControllerRowStatus_Object = MibTableColumn
tmnxOFControllerRowStatus = _TmnxOFControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 4),
    _TmnxOFControllerRowStatus_Type()
)
tmnxOFControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerRowStatus.setStatus("current")
_TmnxOFControllerLastChanged_Type = TimeStamp
_TmnxOFControllerLastChanged_Object = MibTableColumn
tmnxOFControllerLastChanged = _TmnxOFControllerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 5),
    _TmnxOFControllerLastChanged_Type()
)
tmnxOFControllerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerLastChanged.setStatus("current")


class _TmnxOFControllerRole_Type(Integer32):
    """Custom type tmnxOFControllerRole based on Integer32"""
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
        *(("noChange", 0),
          ("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_TmnxOFControllerRole_Type.__name__ = "Integer32"
_TmnxOFControllerRole_Object = MibTableColumn
tmnxOFControllerRole = _TmnxOFControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 6),
    _TmnxOFControllerRole_Type()
)
tmnxOFControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerRole.setStatus("current")
_TmnxOFControllerGenID_Type = Counter64
_TmnxOFControllerGenID_Object = MibTableColumn
tmnxOFControllerGenID = _TmnxOFControllerGenID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 7),
    _TmnxOFControllerGenID_Type()
)
tmnxOFControllerGenID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerGenID.setStatus("current")
_TmnxOFFlowTableTableLastChanged_Type = TimeStamp
_TmnxOFFlowTableTableLastChanged_Object = MibScalar
tmnxOFFlowTableTableLastChanged = _TmnxOFFlowTableTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 5),
    _TmnxOFFlowTableTableLastChanged_Type()
)
tmnxOFFlowTableTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableTableLastChanged.setStatus("current")
_TmnxOFFlowTableTable_Object = MibTable
tmnxOFFlowTableTable = _TmnxOFFlowTableTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOFFlowTableTable.setStatus("current")
_TmnxOFFlowTableEntry_Object = MibTableRow
tmnxOFFlowTableEntry = _TmnxOFFlowTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1)
)
tmnxOFFlowTableEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableId"),
)
if mibBuilder.loadTexts:
    tmnxOFFlowTableEntry.setStatus("current")
_TmnxOFFlowTableId_Type = Unsigned32
_TmnxOFFlowTableId_Object = MibTableColumn
tmnxOFFlowTableId = _TmnxOFFlowTableId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 1),
    _TmnxOFFlowTableId_Type()
)
tmnxOFFlowTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFFlowTableId.setStatus("current")
_TmnxOFFlowTableRowStatus_Type = RowStatus
_TmnxOFFlowTableRowStatus_Object = MibTableColumn
tmnxOFFlowTableRowStatus = _TmnxOFFlowTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 2),
    _TmnxOFFlowTableRowStatus_Type()
)
tmnxOFFlowTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableRowStatus.setStatus("current")
_TmnxOFFlowTableLastChanged_Type = TimeStamp
_TmnxOFFlowTableLastChanged_Object = MibTableColumn
tmnxOFFlowTableLastChanged = _TmnxOFFlowTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 3),
    _TmnxOFFlowTableLastChanged_Type()
)
tmnxOFFlowTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableLastChanged.setStatus("current")


class _TmnxOFFlowTableMaxSize_Type(Unsigned32):
    """Custom type tmnxOFFlowTableMaxSize based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16000),
    )


_TmnxOFFlowTableMaxSize_Type.__name__ = "Unsigned32"
_TmnxOFFlowTableMaxSize_Object = MibTableColumn
tmnxOFFlowTableMaxSize = _TmnxOFFlowTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 4),
    _TmnxOFFlowTableMaxSize_Type()
)
tmnxOFFlowTableMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableMaxSize.setStatus("current")


class _TmnxOFFlowTableNoMatchAction_Type(Integer32):
    """Custom type tmnxOFFlowTableNoMatchAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("fall-through", 2))
    )


_TmnxOFFlowTableNoMatchAction_Type.__name__ = "Integer32"
_TmnxOFFlowTableNoMatchAction_Object = MibTableColumn
tmnxOFFlowTableNoMatchAction = _TmnxOFFlowTableNoMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 5),
    _TmnxOFFlowTableNoMatchAction_Type()
)
tmnxOFFlowTableNoMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableNoMatchAction.setStatus("current")
_TmnxOFFlowTableNumEntries_Type = Unsigned32
_TmnxOFFlowTableNumEntries_Object = MibTableColumn
tmnxOFFlowTableNumEntries = _TmnxOFFlowTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 6),
    _TmnxOFFlowTableNumEntries_Type()
)
tmnxOFFlowTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableNumEntries.setStatus("current")
_TmnxOFFlowTableOperStatus_Type = TmnxOperState
_TmnxOFFlowTableOperStatus_Object = MibTableColumn
tmnxOFFlowTableOperStatus = _TmnxOFFlowTableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 7),
    _TmnxOFFlowTableOperStatus_Type()
)
tmnxOFFlowTableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableOperStatus.setStatus("current")
_TmnxOFChannelInfoTable_Object = MibTable
tmnxOFChannelInfoTable = _TmnxOFChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxOFChannelInfoTable.setStatus("current")
_TmnxOFChannelInfoEntry_Object = MibTableRow
tmnxOFChannelInfoEntry = _TmnxOFChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1)
)
tmnxOFChannelInfoEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddressType"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddress"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTCPPort"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelID"),
)
if mibBuilder.loadTexts:
    tmnxOFChannelInfoEntry.setStatus("current")
_TmnxOFChannelID_Type = Unsigned32
_TmnxOFChannelID_Object = MibTableColumn
tmnxOFChannelID = _TmnxOFChannelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 1),
    _TmnxOFChannelID_Type()
)
tmnxOFChannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFChannelID.setStatus("current")
_TmnxOFChannelVersion_Type = Unsigned32
_TmnxOFChannelVersion_Object = MibTableColumn
tmnxOFChannelVersion = _TmnxOFChannelVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 2),
    _TmnxOFChannelVersion_Type()
)
tmnxOFChannelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelVersion.setStatus("current")


class _TmnxOFChannelType_Type(Integer32):
    """Custom type tmnxOFChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("auxiliary", 2))
    )


_TmnxOFChannelType_Type.__name__ = "Integer32"
_TmnxOFChannelType_Object = MibTableColumn
tmnxOFChannelType = _TmnxOFChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 3),
    _TmnxOFChannelType_Type()
)
tmnxOFChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelType.setStatus("current")
_TmnxOFChannelOperStatus_Type = TmnxOperState
_TmnxOFChannelOperStatus_Object = MibTableColumn
tmnxOFChannelOperStatus = _TmnxOFChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 4),
    _TmnxOFChannelOperStatus_Type()
)
tmnxOFChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelOperStatus.setStatus("current")


class _TmnxOFChannelOperFlags_Type(Bits):
    """Custom type tmnxOFChannelOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("socketStateDisable", 0),
          ("socketStateListen", 1),
          ("socketStateConnecting", 2),
          ("socketStateEstablished", 3),
          ("helloReceived", 4),
          ("helloTransmitted", 5),
          ("handshake", 6))
    )

_TmnxOFChannelOperFlags_Type.__name__ = "Bits"
_TmnxOFChannelOperFlags_Object = MibTableColumn
tmnxOFChannelOperFlags = _TmnxOFChannelOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 5),
    _TmnxOFChannelOperFlags_Type()
)
tmnxOFChannelOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelOperFlags.setStatus("current")
_TmnxOFChannelEchoTimeExpiry_Type = Unsigned32
_TmnxOFChannelEchoTimeExpiry_Object = MibTableColumn
tmnxOFChannelEchoTimeExpiry = _TmnxOFChannelEchoTimeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 6),
    _TmnxOFChannelEchoTimeExpiry_Type()
)
tmnxOFChannelEchoTimeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelEchoTimeExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelEchoTimeExpiry.setUnits("seconds")
_TmnxOFChannelHoldTimeExpiry_Type = Unsigned32
_TmnxOFChannelHoldTimeExpiry_Object = MibTableColumn
tmnxOFChannelHoldTimeExpiry = _TmnxOFChannelHoldTimeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 7),
    _TmnxOFChannelHoldTimeExpiry_Type()
)
tmnxOFChannelHoldTimeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelHoldTimeExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelHoldTimeExpiry.setUnits("seconds")
_TmnxOFChannelConnRetryExpiry_Type = Unsigned32
_TmnxOFChannelConnRetryExpiry_Object = MibTableColumn
tmnxOFChannelConnRetryExpiry = _TmnxOFChannelConnRetryExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 8),
    _TmnxOFChannelConnRetryExpiry_Type()
)
tmnxOFChannelConnRetryExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelConnRetryExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelConnRetryExpiry.setUnits("seconds")
_TmnxOFChannelConnUpTime_Type = Unsigned32
_TmnxOFChannelConnUpTime_Object = MibTableColumn
tmnxOFChannelConnUpTime = _TmnxOFChannelConnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 9),
    _TmnxOFChannelConnUpTime_Type()
)
tmnxOFChannelConnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelConnUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelConnUpTime.setUnits("seconds")
_TmnxOFChannelMEAsyncFltrPacketIn_Type = TmnxOFAsyncFltrPacketIn
_TmnxOFChannelMEAsyncFltrPacketIn_Object = MibTableColumn
tmnxOFChannelMEAsyncFltrPacketIn = _TmnxOFChannelMEAsyncFltrPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 10),
    _TmnxOFChannelMEAsyncFltrPacketIn_Type()
)
tmnxOFChannelMEAsyncFltrPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelMEAsyncFltrPacketIn.setStatus("current")
_TmnxOFChannelSlAsyncFltrPacketIn_Type = TmnxOFAsyncFltrPacketIn
_TmnxOFChannelSlAsyncFltrPacketIn_Object = MibTableColumn
tmnxOFChannelSlAsyncFltrPacketIn = _TmnxOFChannelSlAsyncFltrPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 11),
    _TmnxOFChannelSlAsyncFltrPacketIn_Type()
)
tmnxOFChannelSlAsyncFltrPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSlAsyncFltrPacketIn.setStatus("current")
_TmnxOFChannelMEAsyncFltrPortSts_Type = TmnxOFAsyncFltrPortStatus
_TmnxOFChannelMEAsyncFltrPortSts_Object = MibTableColumn
tmnxOFChannelMEAsyncFltrPortSts = _TmnxOFChannelMEAsyncFltrPortSts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 12),
    _TmnxOFChannelMEAsyncFltrPortSts_Type()
)
tmnxOFChannelMEAsyncFltrPortSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelMEAsyncFltrPortSts.setStatus("current")
_TmnxOFChannelSlAsyncFltrPortSts_Type = TmnxOFAsyncFltrPortStatus
_TmnxOFChannelSlAsyncFltrPortSts_Object = MibTableColumn
tmnxOFChannelSlAsyncFltrPortSts = _TmnxOFChannelSlAsyncFltrPortSts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 13),
    _TmnxOFChannelSlAsyncFltrPortSts_Type()
)
tmnxOFChannelSlAsyncFltrPortSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSlAsyncFltrPortSts.setStatus("current")
_TmnxOFChannelMEAsyncFltrFlowRem_Type = TmnxOFAsyncFltrFlowRemoved
_TmnxOFChannelMEAsyncFltrFlowRem_Object = MibTableColumn
tmnxOFChannelMEAsyncFltrFlowRem = _TmnxOFChannelMEAsyncFltrFlowRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 14),
    _TmnxOFChannelMEAsyncFltrFlowRem_Type()
)
tmnxOFChannelMEAsyncFltrFlowRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelMEAsyncFltrFlowRem.setStatus("current")
_TmnxOFChannelSlAsyncFltrFlowRem_Type = TmnxOFAsyncFltrFlowRemoved
_TmnxOFChannelSlAsyncFltrFlowRem_Object = MibTableColumn
tmnxOFChannelSlAsyncFltrFlowRem = _TmnxOFChannelSlAsyncFltrFlowRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 15),
    _TmnxOFChannelSlAsyncFltrFlowRem_Type()
)
tmnxOFChannelSlAsyncFltrFlowRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSlAsyncFltrFlowRem.setStatus("current")
_TmnxOFChannelStatsTable_Object = MibTable
tmnxOFChannelStatsTable = _TmnxOFChannelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxOFChannelStatsTable.setStatus("current")
_TmnxOFChannelStatsEntry_Object = MibTableRow
tmnxOFChannelStatsEntry = _TmnxOFChannelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1)
)
tmnxOFChannelStatsEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddressType"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddress"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTCPPort"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelID"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketType"),
)
if mibBuilder.loadTexts:
    tmnxOFChannelStatsEntry.setStatus("current")
_TmnxOFChannelPacketType_Type = TmnxOFPktType
_TmnxOFChannelPacketType_Object = MibTableColumn
tmnxOFChannelPacketType = _TmnxOFChannelPacketType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 1),
    _TmnxOFChannelPacketType_Type()
)
tmnxOFChannelPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketType.setStatus("current")
_TmnxOFChannelPacketTx_Type = Counter64
_TmnxOFChannelPacketTx_Object = MibTableColumn
tmnxOFChannelPacketTx = _TmnxOFChannelPacketTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 2),
    _TmnxOFChannelPacketTx_Type()
)
tmnxOFChannelPacketTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketTx.setStatus("current")
_TmnxOFChannelPacketRx_Type = Counter64
_TmnxOFChannelPacketRx_Object = MibTableColumn
tmnxOFChannelPacketRx = _TmnxOFChannelPacketRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 3),
    _TmnxOFChannelPacketRx_Type()
)
tmnxOFChannelPacketRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketRx.setStatus("current")
_TmnxOFChannelPacketErr_Type = Counter64
_TmnxOFChannelPacketErr_Object = MibTableColumn
tmnxOFChannelPacketErr = _TmnxOFChannelPacketErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 4),
    _TmnxOFChannelPacketErr_Type()
)
tmnxOFChannelPacketErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketErr.setStatus("current")
_TmnxOFPortStatsTable_Object = MibTable
tmnxOFPortStatsTable = _TmnxOFPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxOFPortStatsTable.setStatus("current")
_TmnxOFPortStatsEntry_Object = MibTableRow
tmnxOFPortStatsEntry = _TmnxOFPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1)
)
tmnxOFPortStatsEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortID"),
)
if mibBuilder.loadTexts:
    tmnxOFPortStatsEntry.setStatus("current")
_TmnxOFPortID_Type = TmnxPortID
_TmnxOFPortID_Object = MibTableColumn
tmnxOFPortID = _TmnxOFPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 1),
    _TmnxOFPortID_Type()
)
tmnxOFPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFPortID.setStatus("current")
_TmnxOFPortName_Type = TLNamedItemOrEmpty
_TmnxOFPortName_Object = MibTableColumn
tmnxOFPortName = _TmnxOFPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 2),
    _TmnxOFPortName_Type()
)
tmnxOFPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortName.setStatus("current")


class _TmnxOFPortType_Type(Integer32):
    """Custom type tmnxOFPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openFlowPhysicalPort", 0),
          ("openFlowLogicalPort", 1),
          ("openFlowReservedPort", 2))
    )


_TmnxOFPortType_Type.__name__ = "Integer32"
_TmnxOFPortType_Object = MibTableColumn
tmnxOFPortType = _TmnxOFPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 3),
    _TmnxOFPortType_Type()
)
tmnxOFPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortType.setStatus("current")
_TmnxOFPortTxPackets_Type = Counter64
_TmnxOFPortTxPackets_Object = MibTableColumn
tmnxOFPortTxPackets = _TmnxOFPortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 4),
    _TmnxOFPortTxPackets_Type()
)
tmnxOFPortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortTxPackets.setStatus("current")
_TmnxOFPortTxBytes_Type = Counter64
_TmnxOFPortTxBytes_Object = MibTableColumn
tmnxOFPortTxBytes = _TmnxOFPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 5),
    _TmnxOFPortTxBytes_Type()
)
tmnxOFPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortTxBytes.setStatus("current")
_TmnxOpenFlowNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotificationObjs = _TmnxOpenFlowNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 2)
)
_TmnxOFNotifyDescription_Type = DisplayString
_TmnxOFNotifyDescription_Object = MibScalar
tmnxOFNotifyDescription = _TmnxOFNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 2, 1),
    _TmnxOFNotifyDescription_Type()
)
tmnxOFNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOFNotifyDescription.setStatus("current")
_TmnxOpenFlowNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotifyPrefix = _TmnxOpenFlowNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 93)
)
_TmnxOpenFlowNotification_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotification = _TmnxOpenFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 93, 0)
)

# Managed Objects groups

tmnxOpenFlowConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1, 1)
)
tmnxOpenFlowConfigGroup.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchEchoInterval"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchEchoMultiple"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchLogicalPortStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchAdminState"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchDescription"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchDataPathID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchFeaturesBufferSize"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchFeaturesNumTables"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchFeaturesCapability"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerRole"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerGenID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableMaxSize"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableNoMatchAction"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableNumEntries"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableOperStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelVersion"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelOperStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelOperFlags"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelEchoTimeExpiry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelHoldTimeExpiry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelConnRetryExpiry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelConnUpTime"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelMEAsyncFltrPacketIn"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSlAsyncFltrPacketIn"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelMEAsyncFltrPortSts"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSlAsyncFltrPortSts"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelMEAsyncFltrFlowRem"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSlAsyncFltrFlowRem"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketTx"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketRx"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketErr"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortName"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortTxPackets"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortTxBytes"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowConfigGroup.setStatus("current")

tmnxOpenFlowNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1, 2)
)
tmnxOpenFlowNotifyObjsGroup.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxOFFlowEntryInsertFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 93, 0, 1)
)
tmnxOFFlowEntryInsertFailed.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableNoMatchAction"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableOperStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOFFlowEntryInsertFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxOpenFlowNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1, 3)
)
tmnxOpenFlowNotificationGroup.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowEntryInsertFailed")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOpenFlowComplianceV12v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 1)
)
tmnxOpenFlowComplianceV12v0.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowConfigGroup"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowNotifyObjsGroup"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV12v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OPEN-FLOW-MIB",
    **{"TmnxOFDatapathIdentifier": TmnxOFDatapathIdentifier,
       "TmnxOFPktType": TmnxOFPktType,
       "TmnxOFAsyncFltrPacketIn": TmnxOFAsyncFltrPacketIn,
       "TmnxOFAsyncFltrPortStatus": TmnxOFAsyncFltrPortStatus,
       "TmnxOFAsyncFltrFlowRemoved": TmnxOFAsyncFltrFlowRemoved,
       "timetraOpenFlowMIBModule": timetraOpenFlowMIBModule,
       "tmnxOpenFlowConformance": tmnxOpenFlowConformance,
       "tmnxOpenFlowCompliances": tmnxOpenFlowCompliances,
       "tmnxOpenFlowComplianceV12v0": tmnxOpenFlowComplianceV12v0,
       "tmnxOpenFlowGroups": tmnxOpenFlowGroups,
       "tmnxOpenFlowV12v0Groups": tmnxOpenFlowV12v0Groups,
       "tmnxOpenFlowConfigGroup": tmnxOpenFlowConfigGroup,
       "tmnxOpenFlowNotifyObjsGroup": tmnxOpenFlowNotifyObjsGroup,
       "tmnxOpenFlowNotificationGroup": tmnxOpenFlowNotificationGroup,
       "tmnxOpenFlowNotifGroups": tmnxOpenFlowNotifGroups,
       "tmnxOpenFlow": tmnxOpenFlow,
       "tmnxOpenFlowObjs": tmnxOpenFlowObjs,
       "tmnxOFSwitchTableLastChanged": tmnxOFSwitchTableLastChanged,
       "tmnxOFSwitchTable": tmnxOFSwitchTable,
       "tmnxOFSwitchEntry": tmnxOFSwitchEntry,
       "tmnxOFSwitchName": tmnxOFSwitchName,
       "tmnxOFSwitchRowStatus": tmnxOFSwitchRowStatus,
       "tmnxOFSwitchLastChanged": tmnxOFSwitchLastChanged,
       "tmnxOFSwitchEchoInterval": tmnxOFSwitchEchoInterval,
       "tmnxOFSwitchEchoMultiple": tmnxOFSwitchEchoMultiple,
       "tmnxOFSwitchLogicalPortStatus": tmnxOFSwitchLogicalPortStatus,
       "tmnxOFSwitchAdminState": tmnxOFSwitchAdminState,
       "tmnxOFSwitchDescription": tmnxOFSwitchDescription,
       "tmnxOFSwitchDataPathID": tmnxOFSwitchDataPathID,
       "tmnxOFSwitchFeaturesBufferSize": tmnxOFSwitchFeaturesBufferSize,
       "tmnxOFSwitchFeaturesNumTables": tmnxOFSwitchFeaturesNumTables,
       "tmnxOFSwitchFeaturesCapability": tmnxOFSwitchFeaturesCapability,
       "tmnxOFControllerTableLastChanged": tmnxOFControllerTableLastChanged,
       "tmnxOFControllerTable": tmnxOFControllerTable,
       "tmnxOFControllerEntry": tmnxOFControllerEntry,
       "tmnxOFControllerAddressType": tmnxOFControllerAddressType,
       "tmnxOFControllerAddress": tmnxOFControllerAddress,
       "tmnxOFControllerTCPPort": tmnxOFControllerTCPPort,
       "tmnxOFControllerRowStatus": tmnxOFControllerRowStatus,
       "tmnxOFControllerLastChanged": tmnxOFControllerLastChanged,
       "tmnxOFControllerRole": tmnxOFControllerRole,
       "tmnxOFControllerGenID": tmnxOFControllerGenID,
       "tmnxOFFlowTableTableLastChanged": tmnxOFFlowTableTableLastChanged,
       "tmnxOFFlowTableTable": tmnxOFFlowTableTable,
       "tmnxOFFlowTableEntry": tmnxOFFlowTableEntry,
       "tmnxOFFlowTableId": tmnxOFFlowTableId,
       "tmnxOFFlowTableRowStatus": tmnxOFFlowTableRowStatus,
       "tmnxOFFlowTableLastChanged": tmnxOFFlowTableLastChanged,
       "tmnxOFFlowTableMaxSize": tmnxOFFlowTableMaxSize,
       "tmnxOFFlowTableNoMatchAction": tmnxOFFlowTableNoMatchAction,
       "tmnxOFFlowTableNumEntries": tmnxOFFlowTableNumEntries,
       "tmnxOFFlowTableOperStatus": tmnxOFFlowTableOperStatus,
       "tmnxOFChannelInfoTable": tmnxOFChannelInfoTable,
       "tmnxOFChannelInfoEntry": tmnxOFChannelInfoEntry,
       "tmnxOFChannelID": tmnxOFChannelID,
       "tmnxOFChannelVersion": tmnxOFChannelVersion,
       "tmnxOFChannelType": tmnxOFChannelType,
       "tmnxOFChannelOperStatus": tmnxOFChannelOperStatus,
       "tmnxOFChannelOperFlags": tmnxOFChannelOperFlags,
       "tmnxOFChannelEchoTimeExpiry": tmnxOFChannelEchoTimeExpiry,
       "tmnxOFChannelHoldTimeExpiry": tmnxOFChannelHoldTimeExpiry,
       "tmnxOFChannelConnRetryExpiry": tmnxOFChannelConnRetryExpiry,
       "tmnxOFChannelConnUpTime": tmnxOFChannelConnUpTime,
       "tmnxOFChannelMEAsyncFltrPacketIn": tmnxOFChannelMEAsyncFltrPacketIn,
       "tmnxOFChannelSlAsyncFltrPacketIn": tmnxOFChannelSlAsyncFltrPacketIn,
       "tmnxOFChannelMEAsyncFltrPortSts": tmnxOFChannelMEAsyncFltrPortSts,
       "tmnxOFChannelSlAsyncFltrPortSts": tmnxOFChannelSlAsyncFltrPortSts,
       "tmnxOFChannelMEAsyncFltrFlowRem": tmnxOFChannelMEAsyncFltrFlowRem,
       "tmnxOFChannelSlAsyncFltrFlowRem": tmnxOFChannelSlAsyncFltrFlowRem,
       "tmnxOFChannelStatsTable": tmnxOFChannelStatsTable,
       "tmnxOFChannelStatsEntry": tmnxOFChannelStatsEntry,
       "tmnxOFChannelPacketType": tmnxOFChannelPacketType,
       "tmnxOFChannelPacketTx": tmnxOFChannelPacketTx,
       "tmnxOFChannelPacketRx": tmnxOFChannelPacketRx,
       "tmnxOFChannelPacketErr": tmnxOFChannelPacketErr,
       "tmnxOFPortStatsTable": tmnxOFPortStatsTable,
       "tmnxOFPortStatsEntry": tmnxOFPortStatsEntry,
       "tmnxOFPortID": tmnxOFPortID,
       "tmnxOFPortName": tmnxOFPortName,
       "tmnxOFPortType": tmnxOFPortType,
       "tmnxOFPortTxPackets": tmnxOFPortTxPackets,
       "tmnxOFPortTxBytes": tmnxOFPortTxBytes,
       "tmnxOpenFlowNotificationObjs": tmnxOpenFlowNotificationObjs,
       "tmnxOFNotifyDescription": tmnxOFNotifyDescription,
       "tmnxOpenFlowNotifyPrefix": tmnxOpenFlowNotifyPrefix,
       "tmnxOpenFlowNotification": tmnxOpenFlowNotification,
       "tmnxOFFlowEntryInsertFailed": tmnxOFFlowEntryInsertFailed}
)
