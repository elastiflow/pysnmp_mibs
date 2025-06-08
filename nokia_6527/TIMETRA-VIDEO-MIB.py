# SNMP MIB module (TIMETRA-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-VIDEO-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:31:50 2025
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
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TIPFilterID,
 TMACFilterID) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TIPFilterID",
    "TMACFilterID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxMcPathVdoBufferSize,
 TmnxMcPathVdoChlType) = mibBuilder.importSymbols(
    "TIMETRA-MCAST-PATH-MGMT-MIB",
    "TmnxMcPathVdoBufferSize",
    "TmnxMcPathVdoChlType")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(InterfaceIndex,
 TCpmProtPolicyID,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TSapEgressPolicyID,
 TSapIngressPolicyID,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxServId,
 TmnxStrSapId,
 TmnxVdoAnalyzerAlarm,
 TmnxVdoAnalyzerAlarmStates,
 TmnxVdoFccServerMode,
 TmnxVdoGrpId,
 TmnxVdoGrpIdIndex,
 TmnxVdoIfName,
 TmnxVdoOutputFormat,
 TmnxVdoStatInt) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "InterfaceIndex",
    "TCpmProtPolicyID",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TSapEgressPolicyID",
    "TSapIngressPolicyID",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxServId",
    "TmnxStrSapId",
    "TmnxVdoAnalyzerAlarm",
    "TmnxVdoAnalyzerAlarmStates",
    "TmnxVdoFccServerMode",
    "TmnxVdoGrpId",
    "TmnxVdoGrpIdIndex",
    "TmnxVdoIfName",
    "TmnxVdoOutputFormat",
    "TmnxVdoStatInt")


# MODULE-IDENTITY

timetraVideoMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 61)
)
if mibBuilder.loadTexts:
    timetraVideoMIBModule.setRevisions(
        ("1911-02-01 00:00",
         "1909-02-28 00:00",
         "1908-07-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxVdoPIDType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("audio", 1),
          ("video", 2),
          ("data", 3),
          ("ca", 4),
          ("scte35", 5),
          ("pat", 6),
          ("pcr", 7),
          ("pmt", 8))
    )



class TmnxVdoPTS(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class TmnxMDILossRate(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



# MIB Managed Objects in the order of their OIDs

_TmnxVdoConformance_ObjectIdentity = ObjectIdentity
tmnxVdoConformance = _TmnxVdoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61)
)
_TmnxVdoCompliances_ObjectIdentity = ObjectIdentity
tmnxVdoCompliances = _TmnxVdoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 1)
)
_TmnxVdoGroups_ObjectIdentity = ObjectIdentity
tmnxVdoGroups = _TmnxVdoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2)
)
_TmnxVdo_ObjectIdentity = ObjectIdentity
tmnxVdo = _TmnxVdo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61)
)
_TmnxVdoObjs_ObjectIdentity = ObjectIdentity
tmnxVdoObjs = _TmnxVdoObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1)
)
_TmnxVdoIfTable_Object = MibTable
tmnxVdoIfTable = _TmnxVdoIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoIfTable.setStatus("current")
_TmnxVdoIfEntry_Object = MibTableRow
tmnxVdoIfEntry = _TmnxVdoIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1)
)
tmnxVdoIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
)
if mibBuilder.loadTexts:
    tmnxVdoIfEntry.setStatus("current")
_TmnxVdoIfName_Type = TmnxVdoIfName
_TmnxVdoIfName_Object = MibTableColumn
tmnxVdoIfName = _TmnxVdoIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 1),
    _TmnxVdoIfName_Type()
)
tmnxVdoIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoIfName.setStatus("current")
_TmnxVdoIfRowStatus_Type = RowStatus
_TmnxVdoIfRowStatus_Object = MibTableColumn
tmnxVdoIfRowStatus = _TmnxVdoIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 2),
    _TmnxVdoIfRowStatus_Type()
)
tmnxVdoIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRowStatus.setStatus("current")
_TmnxVdoIfLastChanged_Type = TimeStamp
_TmnxVdoIfLastChanged_Object = MibTableColumn
tmnxVdoIfLastChanged = _TmnxVdoIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 3),
    _TmnxVdoIfLastChanged_Type()
)
tmnxVdoIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfLastChanged.setStatus("current")


class _TmnxVdoIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxVdoIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxVdoIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxVdoIfAdminState_Object = MibTableColumn
tmnxVdoIfAdminState = _TmnxVdoIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 4),
    _TmnxVdoIfAdminState_Type()
)
tmnxVdoIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfAdminState.setStatus("current")
_TmnxVdoIfOperState_Type = TmnxOperState
_TmnxVdoIfOperState_Object = MibTableColumn
tmnxVdoIfOperState = _TmnxVdoIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 5),
    _TmnxVdoIfOperState_Type()
)
tmnxVdoIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfOperState.setStatus("current")
_TmnxVdoIfVrtrIfIndex_Type = InterfaceIndex
_TmnxVdoIfVrtrIfIndex_Object = MibTableColumn
tmnxVdoIfVrtrIfIndex = _TmnxVdoIfVrtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 6),
    _TmnxVdoIfVrtrIfIndex_Type()
)
tmnxVdoIfVrtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfVrtrIfIndex.setStatus("current")


class _TmnxVdoIfDescription_Type(TItemDescription):
    """Custom type tmnxVdoIfDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxVdoIfDescription_Type.__name__ = "TItemDescription"
_TmnxVdoIfDescription_Object = MibTableColumn
tmnxVdoIfDescription = _TmnxVdoIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 7),
    _TmnxVdoIfDescription_Type()
)
tmnxVdoIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfDescription.setStatus("current")


class _TmnxVdoIfVdoGrpId_Type(TmnxVdoGrpId):
    """Custom type tmnxVdoIfVdoGrpId based on TmnxVdoGrpId"""
    defaultValue = 0


_TmnxVdoIfVdoGrpId_Type.__name__ = "TmnxVdoGrpId"
_TmnxVdoIfVdoGrpId_Object = MibTableColumn
tmnxVdoIfVdoGrpId = _TmnxVdoIfVdoGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 8),
    _TmnxVdoIfVdoGrpId_Type()
)
tmnxVdoIfVdoGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfVdoGrpId.setStatus("current")


class _TmnxVdoIfIngressQosPolicyId_Type(TSapIngressPolicyID):
    """Custom type tmnxVdoIfIngressQosPolicyId based on TSapIngressPolicyID"""
    defaultValue = 1


_TmnxVdoIfIngressQosPolicyId_Type.__name__ = "TSapIngressPolicyID"
_TmnxVdoIfIngressQosPolicyId_Object = MibTableColumn
tmnxVdoIfIngressQosPolicyId = _TmnxVdoIfIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 9),
    _TmnxVdoIfIngressQosPolicyId_Type()
)
tmnxVdoIfIngressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfIngressQosPolicyId.setStatus("current")


class _TmnxVdoIfEgressQosPolicyId_Type(TSapEgressPolicyID):
    """Custom type tmnxVdoIfEgressQosPolicyId based on TSapEgressPolicyID"""
    defaultValue = 1


_TmnxVdoIfEgressQosPolicyId_Type.__name__ = "TSapEgressPolicyID"
_TmnxVdoIfEgressQosPolicyId_Object = MibTableColumn
tmnxVdoIfEgressQosPolicyId = _TmnxVdoIfEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 10),
    _TmnxVdoIfEgressQosPolicyId_Type()
)
tmnxVdoIfEgressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfEgressQosPolicyId.setStatus("current")


class _TmnxVdoIfAdi_Type(TruthValue):
    """Custom type tmnxVdoIfAdi based on TruthValue"""
    defaultValue = 2


_TmnxVdoIfAdi_Type.__name__ = "TruthValue"
_TmnxVdoIfAdi_Object = MibTableColumn
tmnxVdoIfAdi = _TmnxVdoIfAdi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 11),
    _TmnxVdoIfAdi_Type()
)
tmnxVdoIfAdi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfAdi.setStatus("current")


class _TmnxVdoIfRTClientAddrType_Type(InetAddressType):
    """Custom type tmnxVdoIfRTClientAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVdoIfRTClientAddrType_Type.__name__ = "InetAddressType"
_TmnxVdoIfRTClientAddrType_Object = MibTableColumn
tmnxVdoIfRTClientAddrType = _TmnxVdoIfRTClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 12),
    _TmnxVdoIfRTClientAddrType_Type()
)
tmnxVdoIfRTClientAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRTClientAddrType.setStatus("current")


class _TmnxVdoIfRTClientAddr_Type(InetAddress):
    """Custom type tmnxVdoIfRTClientAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoIfRTClientAddr_Type.__name__ = "InetAddress"
_TmnxVdoIfRTClientAddr_Object = MibTableColumn
tmnxVdoIfRTClientAddr = _TmnxVdoIfRTClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 13),
    _TmnxVdoIfRTClientAddr_Type()
)
tmnxVdoIfRTClientAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRTClientAddr.setStatus("current")


class _TmnxVdoIfGatewayAddrType_Type(InetAddressType):
    """Custom type tmnxVdoIfGatewayAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVdoIfGatewayAddrType_Type.__name__ = "InetAddressType"
_TmnxVdoIfGatewayAddrType_Object = MibTableColumn
tmnxVdoIfGatewayAddrType = _TmnxVdoIfGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 14),
    _TmnxVdoIfGatewayAddrType_Type()
)
tmnxVdoIfGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfGatewayAddrType.setStatus("current")


class _TmnxVdoIfGatewayAddr_Type(InetAddress):
    """Custom type tmnxVdoIfGatewayAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoIfGatewayAddr_Type.__name__ = "InetAddress"
_TmnxVdoIfGatewayAddr_Object = MibTableColumn
tmnxVdoIfGatewayAddr = _TmnxVdoIfGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 15),
    _TmnxVdoIfGatewayAddr_Type()
)
tmnxVdoIfGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfGatewayAddr.setStatus("current")
_TmnxVdoIfMcastSvcId_Type = TmnxServId
_TmnxVdoIfMcastSvcId_Object = MibTableColumn
tmnxVdoIfMcastSvcId = _TmnxVdoIfMcastSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 16),
    _TmnxVdoIfMcastSvcId_Type()
)
tmnxVdoIfMcastSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfMcastSvcId.setStatus("current")


class _TmnxVdoIfIngressIpFilterId_Type(TIPFilterID):
    """Custom type tmnxVdoIfIngressIpFilterId based on TIPFilterID"""
    defaultValue = 0


_TmnxVdoIfIngressIpFilterId_Type.__name__ = "TIPFilterID"
_TmnxVdoIfIngressIpFilterId_Object = MibTableColumn
tmnxVdoIfIngressIpFilterId = _TmnxVdoIfIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 17),
    _TmnxVdoIfIngressIpFilterId_Type()
)
tmnxVdoIfIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfIngressIpFilterId.setStatus("current")


class _TmnxVdoIfIngressMacFilterId_Type(TMACFilterID):
    """Custom type tmnxVdoIfIngressMacFilterId based on TMACFilterID"""
    defaultValue = 0


_TmnxVdoIfIngressMacFilterId_Type.__name__ = "TMACFilterID"
_TmnxVdoIfIngressMacFilterId_Object = MibTableColumn
tmnxVdoIfIngressMacFilterId = _TmnxVdoIfIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 18),
    _TmnxVdoIfIngressMacFilterId_Type()
)
tmnxVdoIfIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfIngressMacFilterId.setStatus("current")


class _TmnxVdoIfEgressIpFilterId_Type(TIPFilterID):
    """Custom type tmnxVdoIfEgressIpFilterId based on TIPFilterID"""
    defaultValue = 0


_TmnxVdoIfEgressIpFilterId_Type.__name__ = "TIPFilterID"
_TmnxVdoIfEgressIpFilterId_Object = MibTableColumn
tmnxVdoIfEgressIpFilterId = _TmnxVdoIfEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 19),
    _TmnxVdoIfEgressIpFilterId_Type()
)
tmnxVdoIfEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfEgressIpFilterId.setStatus("current")


class _TmnxVdoIfEgressMacFilterId_Type(TMACFilterID):
    """Custom type tmnxVdoIfEgressMacFilterId based on TMACFilterID"""
    defaultValue = 0


_TmnxVdoIfEgressMacFilterId_Type.__name__ = "TMACFilterID"
_TmnxVdoIfEgressMacFilterId_Object = MibTableColumn
tmnxVdoIfEgressMacFilterId = _TmnxVdoIfEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 20),
    _TmnxVdoIfEgressMacFilterId_Type()
)
tmnxVdoIfEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfEgressMacFilterId.setStatus("current")


class _TmnxVdoIfScte30ControlAddrType_Type(InetAddressType):
    """Custom type tmnxVdoIfScte30ControlAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVdoIfScte30ControlAddrType_Type.__name__ = "InetAddressType"
_TmnxVdoIfScte30ControlAddrType_Object = MibTableColumn
tmnxVdoIfScte30ControlAddrType = _TmnxVdoIfScte30ControlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 21),
    _TmnxVdoIfScte30ControlAddrType_Type()
)
tmnxVdoIfScte30ControlAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30ControlAddrType.setStatus("current")


class _TmnxVdoIfScte30ControlAddr_Type(InetAddress):
    """Custom type tmnxVdoIfScte30ControlAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoIfScte30ControlAddr_Type.__name__ = "InetAddress"
_TmnxVdoIfScte30ControlAddr_Object = MibTableColumn
tmnxVdoIfScte30ControlAddr = _TmnxVdoIfScte30ControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 22),
    _TmnxVdoIfScte30ControlAddr_Type()
)
tmnxVdoIfScte30ControlAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30ControlAddr.setStatus("current")


class _TmnxVdoIfScte30DataAddrType_Type(InetAddressType):
    """Custom type tmnxVdoIfScte30DataAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxVdoIfScte30DataAddrType_Type.__name__ = "InetAddressType"
_TmnxVdoIfScte30DataAddrType_Object = MibTableColumn
tmnxVdoIfScte30DataAddrType = _TmnxVdoIfScte30DataAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 23),
    _TmnxVdoIfScte30DataAddrType_Type()
)
tmnxVdoIfScte30DataAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30DataAddrType.setStatus("current")


class _TmnxVdoIfScte30DataAddr_Type(InetAddress):
    """Custom type tmnxVdoIfScte30DataAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoIfScte30DataAddr_Type.__name__ = "InetAddress"
_TmnxVdoIfScte30DataAddr_Object = MibTableColumn
tmnxVdoIfScte30DataAddr = _TmnxVdoIfScte30DataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 24),
    _TmnxVdoIfScte30DataAddr_Type()
)
tmnxVdoIfScte30DataAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30DataAddr.setStatus("current")
_TmnxVdoIfSapId_Type = TmnxStrSapId
_TmnxVdoIfSapId_Object = MibTableColumn
tmnxVdoIfSapId = _TmnxVdoIfSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 25),
    _TmnxVdoIfSapId_Type()
)
tmnxVdoIfSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfSapId.setStatus("current")


class _TmnxVdoIfMcastProtocol_Type(Integer32):
    """Custom type tmnxVdoIfMcastProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pim", 2),
          ("igmpSnooping", 3))
    )


_TmnxVdoIfMcastProtocol_Type.__name__ = "Integer32"
_TmnxVdoIfMcastProtocol_Object = MibTableColumn
tmnxVdoIfMcastProtocol = _TmnxVdoIfMcastProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 26),
    _TmnxVdoIfMcastProtocol_Type()
)
tmnxVdoIfMcastProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfMcastProtocol.setStatus("current")
_TmnxVdoIfSessions_Type = Unsigned32
_TmnxVdoIfSessions_Object = MibTableColumn
tmnxVdoIfSessions = _TmnxVdoIfSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 27),
    _TmnxVdoIfSessions_Type()
)
tmnxVdoIfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfSessions.setStatus("current")


class _TmnxVdoIfCpmProtectPolicyId_Type(TCpmProtPolicyID):
    """Custom type tmnxVdoIfCpmProtectPolicyId based on TCpmProtPolicyID"""
    defaultValue = 0


_TmnxVdoIfCpmProtectPolicyId_Type.__name__ = "TCpmProtPolicyID"
_TmnxVdoIfCpmProtectPolicyId_Object = MibTableColumn
tmnxVdoIfCpmProtectPolicyId = _TmnxVdoIfCpmProtectPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 28),
    _TmnxVdoIfCpmProtectPolicyId_Type()
)
tmnxVdoIfCpmProtectPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfCpmProtectPolicyId.setStatus("current")


class _TmnxVdoIfRTMcastReply_Type(TmnxEnabledDisabled):
    """Custom type tmnxVdoIfRTMcastReply based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxVdoIfRTMcastReply_Type.__name__ = "TmnxEnabledDisabled"
_TmnxVdoIfRTMcastReply_Object = MibTableColumn
tmnxVdoIfRTMcastReply = _TmnxVdoIfRTMcastReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 29),
    _TmnxVdoIfRTMcastReply_Type()
)
tmnxVdoIfRTMcastReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRTMcastReply.setStatus("current")


class _TmnxVdoIfRTCount_Type(Unsigned32):
    """Custom type tmnxVdoIfRTCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_TmnxVdoIfRTCount_Type.__name__ = "Unsigned32"
_TmnxVdoIfRTCount_Object = MibTableColumn
tmnxVdoIfRTCount = _TmnxVdoIfRTCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 30),
    _TmnxVdoIfRTCount_Type()
)
tmnxVdoIfRTCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRTCount.setStatus("current")


class _TmnxVdoIfRTInterval_Type(Unsigned32):
    """Custom type tmnxVdoIfRTInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8000),
    )


_TmnxVdoIfRTInterval_Type.__name__ = "Unsigned32"
_TmnxVdoIfRTInterval_Object = MibTableColumn
tmnxVdoIfRTInterval = _TmnxVdoIfRTInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 31),
    _TmnxVdoIfRTInterval_Type()
)
tmnxVdoIfRTInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRTInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoIfRTInterval.setUnits("milliseconds")


class _TmnxVdoIfRTHoldTime_Type(Unsigned32):
    """Custom type tmnxVdoIfRTHoldTime based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxVdoIfRTHoldTime_Type.__name__ = "Unsigned32"
_TmnxVdoIfRTHoldTime_Object = MibTableColumn
tmnxVdoIfRTHoldTime = _TmnxVdoIfRTHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 32),
    _TmnxVdoIfRTHoldTime_Type()
)
tmnxVdoIfRTHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfRTHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoIfRTHoldTime.setUnits("milliseconds")


class _TmnxVdoIfAcctPolicyId_Type(Unsigned32):
    """Custom type tmnxVdoIfAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_TmnxVdoIfAcctPolicyId_Type.__name__ = "Unsigned32"
_TmnxVdoIfAcctPolicyId_Object = MibTableColumn
tmnxVdoIfAcctPolicyId = _TmnxVdoIfAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 33),
    _TmnxVdoIfAcctPolicyId_Type()
)
tmnxVdoIfAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfAcctPolicyId.setStatus("current")


class _TmnxVdoIfOutputFormat_Type(TmnxVdoOutputFormat):
    """Custom type tmnxVdoIfOutputFormat based on TmnxVdoOutputFormat"""
    defaultValue = 2


_TmnxVdoIfOutputFormat_Type.__name__ = "TmnxVdoOutputFormat"
_TmnxVdoIfOutputFormat_Object = MibTableColumn
tmnxVdoIfOutputFormat = _TmnxVdoIfOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 1, 1, 34),
    _TmnxVdoIfOutputFormat_Type()
)
tmnxVdoIfOutputFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfOutputFormat.setStatus("current")
_TmnxVdoIfAddrTable_Object = MibTable
tmnxVdoIfAddrTable = _TmnxVdoIfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxVdoIfAddrTable.setStatus("current")
_TmnxVdoIfAddrEntry_Object = MibTableRow
tmnxVdoIfAddrEntry = _TmnxVdoIfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 2, 1)
)
tmnxVdoIfAddrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfAddrIpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfAddrIpAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxVdoIfAddrEntry.setStatus("current")
_TmnxVdoIfAddrIpAddrType_Type = InetAddressType
_TmnxVdoIfAddrIpAddrType_Object = MibTableColumn
tmnxVdoIfAddrIpAddrType = _TmnxVdoIfAddrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 2, 1, 1),
    _TmnxVdoIfAddrIpAddrType_Type()
)
tmnxVdoIfAddrIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoIfAddrIpAddrType.setStatus("current")


class _TmnxVdoIfAddrIpAddress_Type(InetAddress):
    """Custom type tmnxVdoIfAddrIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoIfAddrIpAddress_Type.__name__ = "InetAddress"
_TmnxVdoIfAddrIpAddress_Object = MibTableColumn
tmnxVdoIfAddrIpAddress = _TmnxVdoIfAddrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 2, 1, 2),
    _TmnxVdoIfAddrIpAddress_Type()
)
tmnxVdoIfAddrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoIfAddrIpAddress.setStatus("current")
_TmnxVdoIfAddrPrefixLen_Type = InetAddressPrefixLength
_TmnxVdoIfAddrPrefixLen_Object = MibTableColumn
tmnxVdoIfAddrPrefixLen = _TmnxVdoIfAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 2, 1, 3),
    _TmnxVdoIfAddrPrefixLen_Type()
)
tmnxVdoIfAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoIfAddrPrefixLen.setStatus("current")
_TmnxVdoIfAddrRowStatus_Type = RowStatus
_TmnxVdoIfAddrRowStatus_Object = MibTableColumn
tmnxVdoIfAddrRowStatus = _TmnxVdoIfAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 2, 1, 4),
    _TmnxVdoIfAddrRowStatus_Type()
)
tmnxVdoIfAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfAddrRowStatus.setStatus("current")
_TmnxVdoGrpTable_Object = MibTable
tmnxVdoGrpTable = _TmnxVdoGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpTable.setStatus("current")
_TmnxVdoGrpEntry_Object = MibTableRow
tmnxVdoGrpEntry = _TmnxVdoGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1)
)
tmnxVdoGrpEntry.setIndexNames(
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpId"),
)
if mibBuilder.loadTexts:
    tmnxVdoGrpEntry.setStatus("current")
_TmnxVdoGrpId_Type = TmnxVdoGrpIdIndex
_TmnxVdoGrpId_Object = MibTableColumn
tmnxVdoGrpId = _TmnxVdoGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 1),
    _TmnxVdoGrpId_Type()
)
tmnxVdoGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpId.setStatus("current")
_TmnxVdoGrpRowStatus_Type = RowStatus
_TmnxVdoGrpRowStatus_Object = MibTableColumn
tmnxVdoGrpRowStatus = _TmnxVdoGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 2),
    _TmnxVdoGrpRowStatus_Type()
)
tmnxVdoGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpRowStatus.setStatus("current")
_TmnxVdoGrpLastChanged_Type = TimeStamp
_TmnxVdoGrpLastChanged_Object = MibTableColumn
tmnxVdoGrpLastChanged = _TmnxVdoGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 3),
    _TmnxVdoGrpLastChanged_Type()
)
tmnxVdoGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpLastChanged.setStatus("current")


class _TmnxVdoGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxVdoGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxVdoGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxVdoGrpAdminState_Object = MibTableColumn
tmnxVdoGrpAdminState = _TmnxVdoGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 4),
    _TmnxVdoGrpAdminState_Type()
)
tmnxVdoGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpAdminState.setStatus("current")
_TmnxVdoGrpOperState_Type = TmnxOperState
_TmnxVdoGrpOperState_Object = MibTableColumn
tmnxVdoGrpOperState = _TmnxVdoGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 5),
    _TmnxVdoGrpOperState_Type()
)
tmnxVdoGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpOperState.setStatus("current")


class _TmnxVdoGrpDescription_Type(TItemDescription):
    """Custom type tmnxVdoGrpDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxVdoGrpDescription_Type.__name__ = "TItemDescription"
_TmnxVdoGrpDescription_Object = MibTableColumn
tmnxVdoGrpDescription = _TmnxVdoGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 6),
    _TmnxVdoGrpDescription_Type()
)
tmnxVdoGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpDescription.setStatus("current")


class _TmnxVdoGrpLocalRTServerState_Type(TruthValue):
    """Custom type tmnxVdoGrpLocalRTServerState based on TruthValue"""
    defaultValue = 2


_TmnxVdoGrpLocalRTServerState_Type.__name__ = "TruthValue"
_TmnxVdoGrpLocalRTServerState_Object = MibTableColumn
tmnxVdoGrpLocalRTServerState = _TmnxVdoGrpLocalRTServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 7),
    _TmnxVdoGrpLocalRTServerState_Type()
)
tmnxVdoGrpLocalRTServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpLocalRTServerState.setStatus("current")


class _TmnxVdoGrpFCCServerState_Type(TruthValue):
    """Custom type tmnxVdoGrpFCCServerState based on TruthValue"""
    defaultValue = 2


_TmnxVdoGrpFCCServerState_Type.__name__ = "TruthValue"
_TmnxVdoGrpFCCServerState_Object = MibTableColumn
tmnxVdoGrpFCCServerState = _TmnxVdoGrpFCCServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 8),
    _TmnxVdoGrpFCCServerState_Type()
)
tmnxVdoGrpFCCServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpFCCServerState.setStatus("current")


class _TmnxVdoGrpADIServerState_Type(TruthValue):
    """Custom type tmnxVdoGrpADIServerState based on TruthValue"""
    defaultValue = 2


_TmnxVdoGrpADIServerState_Type.__name__ = "TruthValue"
_TmnxVdoGrpADIServerState_Object = MibTableColumn
tmnxVdoGrpADIServerState = _TmnxVdoGrpADIServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 9),
    _TmnxVdoGrpADIServerState_Type()
)
tmnxVdoGrpADIServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpADIServerState.setStatus("current")


class _TmnxVdoGrpResvRet_Type(Unsigned32):
    """Custom type tmnxVdoGrpResvRet based on Unsigned32"""
    defaultValue = 0


_TmnxVdoGrpResvRet_Type.__name__ = "Unsigned32"
_TmnxVdoGrpResvRet_Object = MibTableColumn
tmnxVdoGrpResvRet = _TmnxVdoGrpResvRet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 10),
    _TmnxVdoGrpResvRet_Type()
)
tmnxVdoGrpResvRet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpResvRet.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpResvRet.setUnits("mbps")


class _TmnxVdoGrpAnalyzerState_Type(TruthValue):
    """Custom type tmnxVdoGrpAnalyzerState based on TruthValue"""
    defaultValue = 2


_TmnxVdoGrpAnalyzerState_Type.__name__ = "TruthValue"
_TmnxVdoGrpAnalyzerState_Object = MibTableColumn
tmnxVdoGrpAnalyzerState = _TmnxVdoGrpAnalyzerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 11),
    _TmnxVdoGrpAnalyzerState_Type()
)
tmnxVdoGrpAnalyzerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpAnalyzerState.setStatus("current")


class _TmnxVdoGrpStreamSelectionState_Type(TruthValue):
    """Custom type tmnxVdoGrpStreamSelectionState based on TruthValue"""
    defaultValue = 2


_TmnxVdoGrpStreamSelectionState_Type.__name__ = "TruthValue"
_TmnxVdoGrpStreamSelectionState_Object = MibTableColumn
tmnxVdoGrpStreamSelectionState = _TmnxVdoGrpStreamSelectionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 3, 1, 12),
    _TmnxVdoGrpStreamSelectionState_Type()
)
tmnxVdoGrpStreamSelectionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpStreamSelectionState.setStatus("current")
_TmnxVdoGrpMDATable_Object = MibTable
tmnxVdoGrpMDATable = _TmnxVdoGrpMDATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpMDATable.setStatus("current")
_TmnxVdoGrpMDAEntry_Object = MibTableRow
tmnxVdoGrpMDAEntry = _TmnxVdoGrpMDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1)
)
tmnxVdoGrpMDAEntry.setIndexNames(
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxVdoGrpMDAEntry.setStatus("current")
_TmnxVdoGrpMdaRowStatus_Type = RowStatus
_TmnxVdoGrpMdaRowStatus_Object = MibTableColumn
tmnxVdoGrpMdaRowStatus = _TmnxVdoGrpMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 1),
    _TmnxVdoGrpMdaRowStatus_Type()
)
tmnxVdoGrpMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRowStatus.setStatus("current")
_TmnxVdoGrpMdaAdminState_Type = TmnxAdminState
_TmnxVdoGrpMdaAdminState_Object = MibTableColumn
tmnxVdoGrpMdaAdminState = _TmnxVdoGrpMdaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 2),
    _TmnxVdoGrpMdaAdminState_Type()
)
tmnxVdoGrpMdaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaAdminState.setStatus("current")
_TmnxVdoGrpMdaOperState_Type = TmnxOperState
_TmnxVdoGrpMdaOperState_Object = MibTableColumn
tmnxVdoGrpMdaOperState = _TmnxVdoGrpMdaOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 3),
    _TmnxVdoGrpMdaOperState_Type()
)
tmnxVdoGrpMdaOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaOperState.setStatus("current")
_TmnxVdoGrpMdaUsedMemory_Type = Gauge32
_TmnxVdoGrpMdaUsedMemory_Object = MibTableColumn
tmnxVdoGrpMdaUsedMemory = _TmnxVdoGrpMdaUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 4),
    _TmnxVdoGrpMdaUsedMemory_Type()
)
tmnxVdoGrpMdaUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaUsedMemory.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaUsedMemory.setUnits("Bytes")
_TmnxVdoGrpMdaAvailableMemory_Type = Gauge32
_TmnxVdoGrpMdaAvailableMemory_Object = MibTableColumn
tmnxVdoGrpMdaAvailableMemory = _TmnxVdoGrpMdaAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 5),
    _TmnxVdoGrpMdaAvailableMemory_Type()
)
tmnxVdoGrpMdaAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaAvailableMemory.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaAvailableMemory.setUnits("Bytes")
_TmnxVdoGrpMdaChannels_Type = Gauge32
_TmnxVdoGrpMdaChannels_Object = MibTableColumn
tmnxVdoGrpMdaChannels = _TmnxVdoGrpMdaChannels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 6),
    _TmnxVdoGrpMdaChannels_Type()
)
tmnxVdoGrpMdaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaChannels.setStatus("current")
_TmnxVdoGrpMdaChannelAllocFails_Type = Counter32
_TmnxVdoGrpMdaChannelAllocFails_Object = MibTableColumn
tmnxVdoGrpMdaChannelAllocFails = _TmnxVdoGrpMdaChannelAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 7),
    _TmnxVdoGrpMdaChannelAllocFails_Type()
)
tmnxVdoGrpMdaChannelAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaChannelAllocFails.setStatus("current")
_TmnxVdoGrpMdaMaxBwExceeded_Type = Counter32
_TmnxVdoGrpMdaMaxBwExceeded_Object = MibTableColumn
tmnxVdoGrpMdaMaxBwExceeded = _TmnxVdoGrpMdaMaxBwExceeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 8),
    _TmnxVdoGrpMdaMaxBwExceeded_Type()
)
tmnxVdoGrpMdaMaxBwExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMaxBwExceeded.setStatus("current")
_TmnxVdoGrpMdaBwInUse_Type = Gauge32
_TmnxVdoGrpMdaBwInUse_Object = MibTableColumn
tmnxVdoGrpMdaBwInUse = _TmnxVdoGrpMdaBwInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 9),
    _TmnxVdoGrpMdaBwInUse_Type()
)
tmnxVdoGrpMdaBwInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaBwInUse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaBwInUse.setUnits("kbps")
_TmnxVdoGrpMdaActiveRtcpSessions_Type = Gauge32
_TmnxVdoGrpMdaActiveRtcpSessions_Object = MibTableColumn
tmnxVdoGrpMdaActiveRtcpSessions = _TmnxVdoGrpMdaActiveRtcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 10),
    _TmnxVdoGrpMdaActiveRtcpSessions_Type()
)
tmnxVdoGrpMdaActiveRtcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaActiveRtcpSessions.setStatus("current")
_TmnxVdoGrpMdaEgressStreamResets_Type = Counter32
_TmnxVdoGrpMdaEgressStreamResets_Object = MibTableColumn
tmnxVdoGrpMdaEgressStreamResets = _TmnxVdoGrpMdaEgressStreamResets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 11),
    _TmnxVdoGrpMdaEgressStreamResets_Type()
)
tmnxVdoGrpMdaEgressStreamResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaEgressStreamResets.setStatus("current")
_TmnxVdoGrpMdaIngressStreamResets_Type = Counter32
_TmnxVdoGrpMdaIngressStreamResets_Object = MibTableColumn
tmnxVdoGrpMdaIngressStreamResets = _TmnxVdoGrpMdaIngressStreamResets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 12),
    _TmnxVdoGrpMdaIngressStreamResets_Type()
)
tmnxVdoGrpMdaIngressStreamResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaIngressStreamResets.setStatus("current")
_TmnxVdoGrpMdaAdStreamResets_Type = Counter32
_TmnxVdoGrpMdaAdStreamResets_Object = MibTableColumn
tmnxVdoGrpMdaAdStreamResets = _TmnxVdoGrpMdaAdStreamResets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 13),
    _TmnxVdoGrpMdaAdStreamResets_Type()
)
tmnxVdoGrpMdaAdStreamResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaAdStreamResets.setStatus("current")
_TmnxVdoGrpMdaAdStreamAborts_Type = Counter32
_TmnxVdoGrpMdaAdStreamAborts_Object = MibTableColumn
tmnxVdoGrpMdaAdStreamAborts = _TmnxVdoGrpMdaAdStreamAborts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 14),
    _TmnxVdoGrpMdaAdStreamAborts_Type()
)
tmnxVdoGrpMdaAdStreamAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaAdStreamAborts.setStatus("current")
_TmnxVdoGrpMdaSsrcCollisions_Type = Counter32
_TmnxVdoGrpMdaSsrcCollisions_Object = MibTableColumn
tmnxVdoGrpMdaSsrcCollisions = _TmnxVdoGrpMdaSsrcCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 15),
    _TmnxVdoGrpMdaSsrcCollisions_Type()
)
tmnxVdoGrpMdaSsrcCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaSsrcCollisions.setStatus("current")
_TmnxVdoGrpMdaRxDataPackets_Type = Counter64
_TmnxVdoGrpMdaRxDataPackets_Object = MibTableColumn
tmnxVdoGrpMdaRxDataPackets = _TmnxVdoGrpMdaRxDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 16),
    _TmnxVdoGrpMdaRxDataPackets_Type()
)
tmnxVdoGrpMdaRxDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataPackets.setStatus("current")
_TmnxVdoGrpMdaRxDataPacketsLow32_Type = Counter32
_TmnxVdoGrpMdaRxDataPacketsLow32_Object = MibTableColumn
tmnxVdoGrpMdaRxDataPacketsLow32 = _TmnxVdoGrpMdaRxDataPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 17),
    _TmnxVdoGrpMdaRxDataPacketsLow32_Type()
)
tmnxVdoGrpMdaRxDataPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataPacketsLow32.setStatus("current")
_TmnxVdoGrpMdaRxDataPacketsHigh32_Type = Counter32
_TmnxVdoGrpMdaRxDataPacketsHigh32_Object = MibTableColumn
tmnxVdoGrpMdaRxDataPacketsHigh32 = _TmnxVdoGrpMdaRxDataPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 18),
    _TmnxVdoGrpMdaRxDataPacketsHigh32_Type()
)
tmnxVdoGrpMdaRxDataPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataPacketsHigh32.setStatus("current")
_TmnxVdoGrpMdaRxDataOctets_Type = Counter64
_TmnxVdoGrpMdaRxDataOctets_Object = MibTableColumn
tmnxVdoGrpMdaRxDataOctets = _TmnxVdoGrpMdaRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 19),
    _TmnxVdoGrpMdaRxDataOctets_Type()
)
tmnxVdoGrpMdaRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataOctets.setStatus("current")
_TmnxVdoGrpMdaRxDataOctetsLow32_Type = Counter32
_TmnxVdoGrpMdaRxDataOctetsLow32_Object = MibTableColumn
tmnxVdoGrpMdaRxDataOctetsLow32 = _TmnxVdoGrpMdaRxDataOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 20),
    _TmnxVdoGrpMdaRxDataOctetsLow32_Type()
)
tmnxVdoGrpMdaRxDataOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataOctetsLow32.setStatus("current")
_TmnxVdoGrpMdaRxDataOctetsHigh32_Type = Counter32
_TmnxVdoGrpMdaRxDataOctetsHigh32_Object = MibTableColumn
tmnxVdoGrpMdaRxDataOctetsHigh32 = _TmnxVdoGrpMdaRxDataOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 21),
    _TmnxVdoGrpMdaRxDataOctetsHigh32_Type()
)
tmnxVdoGrpMdaRxDataOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataOctetsHigh32.setStatus("current")
_TmnxVdoGrpMdaRxDataPacketErrors_Type = Counter64
_TmnxVdoGrpMdaRxDataPacketErrors_Object = MibTableColumn
tmnxVdoGrpMdaRxDataPacketErrors = _TmnxVdoGrpMdaRxDataPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 22),
    _TmnxVdoGrpMdaRxDataPacketErrors_Type()
)
tmnxVdoGrpMdaRxDataPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataPacketErrors.setStatus("current")
_TmnxVdoGrpMdaRxDataPktErrsLow32_Type = Counter32
_TmnxVdoGrpMdaRxDataPktErrsLow32_Object = MibTableColumn
tmnxVdoGrpMdaRxDataPktErrsLow32 = _TmnxVdoGrpMdaRxDataPktErrsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 23),
    _TmnxVdoGrpMdaRxDataPktErrsLow32_Type()
)
tmnxVdoGrpMdaRxDataPktErrsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataPktErrsLow32.setStatus("current")
_TmnxVdoGrpMdaRxDataPktErrsHigh32_Type = Counter32
_TmnxVdoGrpMdaRxDataPktErrsHigh32_Object = MibTableColumn
tmnxVdoGrpMdaRxDataPktErrsHigh32 = _TmnxVdoGrpMdaRxDataPktErrsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 24),
    _TmnxVdoGrpMdaRxDataPktErrsHigh32_Type()
)
tmnxVdoGrpMdaRxDataPktErrsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRxDataPktErrsHigh32.setStatus("current")
_TmnxVdoGrpMdaTxDataPackets_Type = Counter64
_TmnxVdoGrpMdaTxDataPackets_Object = MibTableColumn
tmnxVdoGrpMdaTxDataPackets = _TmnxVdoGrpMdaTxDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 25),
    _TmnxVdoGrpMdaTxDataPackets_Type()
)
tmnxVdoGrpMdaTxDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataPackets.setStatus("current")
_TmnxVdoGrpMdaTxDataPacketsLow32_Type = Counter32
_TmnxVdoGrpMdaTxDataPacketsLow32_Object = MibTableColumn
tmnxVdoGrpMdaTxDataPacketsLow32 = _TmnxVdoGrpMdaTxDataPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 26),
    _TmnxVdoGrpMdaTxDataPacketsLow32_Type()
)
tmnxVdoGrpMdaTxDataPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataPacketsLow32.setStatus("current")
_TmnxVdoGrpMdaTxDataPacketsHigh32_Type = Counter32
_TmnxVdoGrpMdaTxDataPacketsHigh32_Object = MibTableColumn
tmnxVdoGrpMdaTxDataPacketsHigh32 = _TmnxVdoGrpMdaTxDataPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 27),
    _TmnxVdoGrpMdaTxDataPacketsHigh32_Type()
)
tmnxVdoGrpMdaTxDataPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataPacketsHigh32.setStatus("current")
_TmnxVdoGrpMdaTxDataOctets_Type = Counter64
_TmnxVdoGrpMdaTxDataOctets_Object = MibTableColumn
tmnxVdoGrpMdaTxDataOctets = _TmnxVdoGrpMdaTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 28),
    _TmnxVdoGrpMdaTxDataOctets_Type()
)
tmnxVdoGrpMdaTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataOctets.setStatus("current")
_TmnxVdoGrpMdaTxDataOctetsLow32_Type = Counter32
_TmnxVdoGrpMdaTxDataOctetsLow32_Object = MibTableColumn
tmnxVdoGrpMdaTxDataOctetsLow32 = _TmnxVdoGrpMdaTxDataOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 29),
    _TmnxVdoGrpMdaTxDataOctetsLow32_Type()
)
tmnxVdoGrpMdaTxDataOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataOctetsLow32.setStatus("current")
_TmnxVdoGrpMdaTxDataOctetsHigh32_Type = Counter32
_TmnxVdoGrpMdaTxDataOctetsHigh32_Object = MibTableColumn
tmnxVdoGrpMdaTxDataOctetsHigh32 = _TmnxVdoGrpMdaTxDataOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 30),
    _TmnxVdoGrpMdaTxDataOctetsHigh32_Type()
)
tmnxVdoGrpMdaTxDataOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataOctetsHigh32.setStatus("current")
_TmnxVdoGrpMdaTxDataPacketErrors_Type = Counter64
_TmnxVdoGrpMdaTxDataPacketErrors_Object = MibTableColumn
tmnxVdoGrpMdaTxDataPacketErrors = _TmnxVdoGrpMdaTxDataPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 31),
    _TmnxVdoGrpMdaTxDataPacketErrors_Type()
)
tmnxVdoGrpMdaTxDataPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataPacketErrors.setStatus("current")
_TmnxVdoGrpMdaTxDataPktErrsLow32_Type = Counter32
_TmnxVdoGrpMdaTxDataPktErrsLow32_Object = MibTableColumn
tmnxVdoGrpMdaTxDataPktErrsLow32 = _TmnxVdoGrpMdaTxDataPktErrsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 32),
    _TmnxVdoGrpMdaTxDataPktErrsLow32_Type()
)
tmnxVdoGrpMdaTxDataPktErrsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataPktErrsLow32.setStatus("current")
_TmnxVdoGrpMdaTxDataPktErrsHigh32_Type = Counter32
_TmnxVdoGrpMdaTxDataPktErrsHigh32_Object = MibTableColumn
tmnxVdoGrpMdaTxDataPktErrsHigh32 = _TmnxVdoGrpMdaTxDataPktErrsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 33),
    _TmnxVdoGrpMdaTxDataPktErrsHigh32_Type()
)
tmnxVdoGrpMdaTxDataPktErrsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxDataPktErrsHigh32.setStatus("current")
_TmnxVdoGrpMdaRtcpParseErrors_Type = Counter32
_TmnxVdoGrpMdaRtcpParseErrors_Object = MibTableColumn
tmnxVdoGrpMdaRtcpParseErrors = _TmnxVdoGrpMdaRtcpParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 34),
    _TmnxVdoGrpMdaRtcpParseErrors_Type()
)
tmnxVdoGrpMdaRtcpParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRtcpParseErrors.setStatus("current")
_TmnxVdoGrpMdaRtcpConfigErrors_Type = Counter32
_TmnxVdoGrpMdaRtcpConfigErrors_Object = MibTableColumn
tmnxVdoGrpMdaRtcpConfigErrors = _TmnxVdoGrpMdaRtcpConfigErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 35),
    _TmnxVdoGrpMdaRtcpConfigErrors_Type()
)
tmnxVdoGrpMdaRtcpConfigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRtcpConfigErrors.setStatus("current")
_TmnxVdoGrpMdaRtcpIpcErrors_Type = Counter32
_TmnxVdoGrpMdaRtcpIpcErrors_Object = MibTableColumn
tmnxVdoGrpMdaRtcpIpcErrors = _TmnxVdoGrpMdaRtcpIpcErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 36),
    _TmnxVdoGrpMdaRtcpIpcErrors_Type()
)
tmnxVdoGrpMdaRtcpIpcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRtcpIpcErrors.setStatus("current")
_TmnxVdoGrpMdaRtcpSgErrors_Type = Counter32
_TmnxVdoGrpMdaRtcpSgErrors_Object = MibTableColumn
tmnxVdoGrpMdaRtcpSgErrors = _TmnxVdoGrpMdaRtcpSgErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 37),
    _TmnxVdoGrpMdaRtcpSgErrors_Type()
)
tmnxVdoGrpMdaRtcpSgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRtcpSgErrors.setStatus("current")
_TmnxVdoGrpMdaRtcpSubErrors_Type = Counter32
_TmnxVdoGrpMdaRtcpSubErrors_Object = MibTableColumn
tmnxVdoGrpMdaRtcpSubErrors = _TmnxVdoGrpMdaRtcpSubErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 38),
    _TmnxVdoGrpMdaRtcpSubErrors_Type()
)
tmnxVdoGrpMdaRtcpSubErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRtcpSubErrors.setStatus("current")
_TmnxVdoGrpMdaRtcpIntErrors_Type = Counter32
_TmnxVdoGrpMdaRtcpIntErrors_Object = MibTableColumn
tmnxVdoGrpMdaRtcpIntErrors = _TmnxVdoGrpMdaRtcpIntErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 39),
    _TmnxVdoGrpMdaRtcpIntErrors_Type()
)
tmnxVdoGrpMdaRtcpIntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRtcpIntErrors.setStatus("current")
_TmnxVdoGrpMdaTxLostPackets_Type = Counter32
_TmnxVdoGrpMdaTxLostPackets_Object = MibTableColumn
tmnxVdoGrpMdaTxLostPackets = _TmnxVdoGrpMdaTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 40),
    _TmnxVdoGrpMdaTxLostPackets_Type()
)
tmnxVdoGrpMdaTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaTxLostPackets.setStatus("current")
_TmnxVdoGrpMdaRequestedRtpPkts_Type = Counter32
_TmnxVdoGrpMdaRequestedRtpPkts_Object = MibTableColumn
tmnxVdoGrpMdaRequestedRtpPkts = _TmnxVdoGrpMdaRequestedRtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 41),
    _TmnxVdoGrpMdaRequestedRtpPkts_Type()
)
tmnxVdoGrpMdaRequestedRtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRequestedRtpPkts.setStatus("current")
_TmnxVdoGrpMdaHighPktPoolLimitHit_Type = Counter32
_TmnxVdoGrpMdaHighPktPoolLimitHit_Object = MibTableColumn
tmnxVdoGrpMdaHighPktPoolLimitHit = _TmnxVdoGrpMdaHighPktPoolLimitHit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 42),
    _TmnxVdoGrpMdaHighPktPoolLimitHit_Type()
)
tmnxVdoGrpMdaHighPktPoolLimitHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaHighPktPoolLimitHit.setStatus("current")
_TmnxVdoGrpMdaMallocFailures_Type = Counter32
_TmnxVdoGrpMdaMallocFailures_Object = MibTableColumn
tmnxVdoGrpMdaMallocFailures = _TmnxVdoGrpMdaMallocFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 43),
    _TmnxVdoGrpMdaMallocFailures_Type()
)
tmnxVdoGrpMdaMallocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMallocFailures.setStatus("current")
_TmnxVdoGrpMdaDentDroppedPkts_Type = Counter32
_TmnxVdoGrpMdaDentDroppedPkts_Object = MibTableColumn
tmnxVdoGrpMdaDentDroppedPkts = _TmnxVdoGrpMdaDentDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 44),
    _TmnxVdoGrpMdaDentDroppedPkts_Type()
)
tmnxVdoGrpMdaDentDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaDentDroppedPkts.setStatus("current")
_TmnxVdoGrpMdaBwPeak_Type = Gauge32
_TmnxVdoGrpMdaBwPeak_Object = MibTableColumn
tmnxVdoGrpMdaBwPeak = _TmnxVdoGrpMdaBwPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 45),
    _TmnxVdoGrpMdaBwPeak_Type()
)
tmnxVdoGrpMdaBwPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaBwPeak.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaBwPeak.setUnits("kbps")
_TmnxVdoGrpMdaCurTotalRetBw_Type = Gauge32
_TmnxVdoGrpMdaCurTotalRetBw_Object = MibTableColumn
tmnxVdoGrpMdaCurTotalRetBw = _TmnxVdoGrpMdaCurTotalRetBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 46),
    _TmnxVdoGrpMdaCurTotalRetBw_Type()
)
tmnxVdoGrpMdaCurTotalRetBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaCurTotalRetBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaCurTotalRetBw.setUnits("kbps")
_TmnxVdoGrpMdaPeakRetBw_Type = Gauge32
_TmnxVdoGrpMdaPeakRetBw_Object = MibTableColumn
tmnxVdoGrpMdaPeakRetBw = _TmnxVdoGrpMdaPeakRetBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 47),
    _TmnxVdoGrpMdaPeakRetBw_Type()
)
tmnxVdoGrpMdaPeakRetBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPeakRetBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPeakRetBw.setUnits("kbps")
_TmnxVdoGrpMdaCurFccBw_Type = Gauge32
_TmnxVdoGrpMdaCurFccBw_Object = MibTableColumn
tmnxVdoGrpMdaCurFccBw = _TmnxVdoGrpMdaCurFccBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 48),
    _TmnxVdoGrpMdaCurFccBw_Type()
)
tmnxVdoGrpMdaCurFccBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaCurFccBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaCurFccBw.setUnits("kbps")
_TmnxVdoGrpMdaFccDropCntReq_Type = Gauge32
_TmnxVdoGrpMdaFccDropCntReq_Object = MibTableColumn
tmnxVdoGrpMdaFccDropCntReq = _TmnxVdoGrpMdaFccDropCntReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 49),
    _TmnxVdoGrpMdaFccDropCntReq_Type()
)
tmnxVdoGrpMdaFccDropCntReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaFccDropCntReq.setStatus("current")
_TmnxVdoGrpMdaMcRtcp_Type = Counter64
_TmnxVdoGrpMdaMcRtcp_Object = MibTableColumn
tmnxVdoGrpMdaMcRtcp = _TmnxVdoGrpMdaMcRtcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 50),
    _TmnxVdoGrpMdaMcRtcp_Type()
)
tmnxVdoGrpMdaMcRtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRtcp.setStatus("current")
_TmnxVdoGrpMdaMcRtcpLow32_Type = Counter32
_TmnxVdoGrpMdaMcRtcpLow32_Object = MibTableColumn
tmnxVdoGrpMdaMcRtcpLow32 = _TmnxVdoGrpMdaMcRtcpLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 51),
    _TmnxVdoGrpMdaMcRtcpLow32_Type()
)
tmnxVdoGrpMdaMcRtcpLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRtcpLow32.setStatus("current")
_TmnxVdoGrpMdaMcRtcpHigh32_Type = Counter32
_TmnxVdoGrpMdaMcRtcpHigh32_Object = MibTableColumn
tmnxVdoGrpMdaMcRtcpHigh32 = _TmnxVdoGrpMdaMcRtcpHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 52),
    _TmnxVdoGrpMdaMcRtcpHigh32_Type()
)
tmnxVdoGrpMdaMcRtcpHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRtcpHigh32.setStatus("current")
_TmnxVdoGrpMdaMcRudp_Type = Counter64
_TmnxVdoGrpMdaMcRudp_Object = MibTableColumn
tmnxVdoGrpMdaMcRudp = _TmnxVdoGrpMdaMcRudp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 53),
    _TmnxVdoGrpMdaMcRudp_Type()
)
tmnxVdoGrpMdaMcRudp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRudp.setStatus("current")
_TmnxVdoGrpMdaMcRudpLow32_Type = Counter32
_TmnxVdoGrpMdaMcRudpLow32_Object = MibTableColumn
tmnxVdoGrpMdaMcRudpLow32 = _TmnxVdoGrpMdaMcRudpLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 54),
    _TmnxVdoGrpMdaMcRudpLow32_Type()
)
tmnxVdoGrpMdaMcRudpLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRudpLow32.setStatus("current")
_TmnxVdoGrpMdaMcRudpHigh32_Type = Counter32
_TmnxVdoGrpMdaMcRudpHigh32_Object = MibTableColumn
tmnxVdoGrpMdaMcRudpHigh32 = _TmnxVdoGrpMdaMcRudpHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 55),
    _TmnxVdoGrpMdaMcRudpHigh32_Type()
)
tmnxVdoGrpMdaMcRudpHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRudpHigh32.setStatus("current")
_TmnxVdoGrpMdaMcRetReqCrt_Type = Counter64
_TmnxVdoGrpMdaMcRetReqCrt_Object = MibTableColumn
tmnxVdoGrpMdaMcRetReqCrt = _TmnxVdoGrpMdaMcRetReqCrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 56),
    _TmnxVdoGrpMdaMcRetReqCrt_Type()
)
tmnxVdoGrpMdaMcRetReqCrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRetReqCrt.setStatus("current")
_TmnxVdoGrpMdaMcRetReqCrtLow32_Type = Counter32
_TmnxVdoGrpMdaMcRetReqCrtLow32_Object = MibTableColumn
tmnxVdoGrpMdaMcRetReqCrtLow32 = _TmnxVdoGrpMdaMcRetReqCrtLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 57),
    _TmnxVdoGrpMdaMcRetReqCrtLow32_Type()
)
tmnxVdoGrpMdaMcRetReqCrtLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRetReqCrtLow32.setStatus("current")
_TmnxVdoGrpMdaMcRetReqCrtHigh32_Type = Counter32
_TmnxVdoGrpMdaMcRetReqCrtHigh32_Object = MibTableColumn
tmnxVdoGrpMdaMcRetReqCrtHigh32 = _TmnxVdoGrpMdaMcRetReqCrtHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 58),
    _TmnxVdoGrpMdaMcRetReqCrtHigh32_Type()
)
tmnxVdoGrpMdaMcRetReqCrtHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaMcRetReqCrtHigh32.setStatus("current")
_TmnxVdoGrpMdaRetReqQnc_Type = Counter64
_TmnxVdoGrpMdaRetReqQnc_Object = MibTableColumn
tmnxVdoGrpMdaRetReqQnc = _TmnxVdoGrpMdaRetReqQnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 59),
    _TmnxVdoGrpMdaRetReqQnc_Type()
)
tmnxVdoGrpMdaRetReqQnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRetReqQnc.setStatus("current")
_TmnxVdoGrpMdaRetReqQncLow32_Type = Counter32
_TmnxVdoGrpMdaRetReqQncLow32_Object = MibTableColumn
tmnxVdoGrpMdaRetReqQncLow32 = _TmnxVdoGrpMdaRetReqQncLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 60),
    _TmnxVdoGrpMdaRetReqQncLow32_Type()
)
tmnxVdoGrpMdaRetReqQncLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRetReqQncLow32.setStatus("current")
_TmnxVdoGrpMdaRetReqQncHigh32_Type = Counter32
_TmnxVdoGrpMdaRetReqQncHigh32_Object = MibTableColumn
tmnxVdoGrpMdaRetReqQncHigh32 = _TmnxVdoGrpMdaRetReqQncHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 61),
    _TmnxVdoGrpMdaRetReqQncHigh32_Type()
)
tmnxVdoGrpMdaRetReqQncHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaRetReqQncHigh32.setStatus("current")
_TmnxVdoGrpMdaPktsLostInSeq10_Type = Counter32
_TmnxVdoGrpMdaPktsLostInSeq10_Object = MibTableColumn
tmnxVdoGrpMdaPktsLostInSeq10 = _TmnxVdoGrpMdaPktsLostInSeq10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 62),
    _TmnxVdoGrpMdaPktsLostInSeq10_Type()
)
tmnxVdoGrpMdaPktsLostInSeq10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPktsLostInSeq10.setStatus("current")
_TmnxVdoGrpMdaPktsLostInSeq20_Type = Counter32
_TmnxVdoGrpMdaPktsLostInSeq20_Object = MibTableColumn
tmnxVdoGrpMdaPktsLostInSeq20 = _TmnxVdoGrpMdaPktsLostInSeq20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 63),
    _TmnxVdoGrpMdaPktsLostInSeq20_Type()
)
tmnxVdoGrpMdaPktsLostInSeq20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPktsLostInSeq20.setStatus("current")
_TmnxVdoGrpMdaPktsLostInSeq30_Type = Counter32
_TmnxVdoGrpMdaPktsLostInSeq30_Object = MibTableColumn
tmnxVdoGrpMdaPktsLostInSeq30 = _TmnxVdoGrpMdaPktsLostInSeq30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 64),
    _TmnxVdoGrpMdaPktsLostInSeq30_Type()
)
tmnxVdoGrpMdaPktsLostInSeq30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPktsLostInSeq30.setStatus("current")
_TmnxVdoGrpMdaPktsLostInSeq40_Type = Counter32
_TmnxVdoGrpMdaPktsLostInSeq40_Object = MibTableColumn
tmnxVdoGrpMdaPktsLostInSeq40 = _TmnxVdoGrpMdaPktsLostInSeq40_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 65),
    _TmnxVdoGrpMdaPktsLostInSeq40_Type()
)
tmnxVdoGrpMdaPktsLostInSeq40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPktsLostInSeq40.setStatus("current")
_TmnxVdoGrpMdaPktsLostInSeqMore_Type = Counter32
_TmnxVdoGrpMdaPktsLostInSeqMore_Object = MibTableColumn
tmnxVdoGrpMdaPktsLostInSeqMore = _TmnxVdoGrpMdaPktsLostInSeqMore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 4, 1, 66),
    _TmnxVdoGrpMdaPktsLostInSeqMore_Type()
)
tmnxVdoGrpMdaPktsLostInSeqMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMdaPktsLostInSeqMore.setStatus("current")
_TmnxVdoAdiChlTable_Object = MibTable
tmnxVdoAdiChlTable = _TmnxVdoAdiChlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxVdoAdiChlTable.setStatus("current")
_TmnxVdoAdiChlEntry_Object = MibTableRow
tmnxVdoAdiChlEntry = _TmnxVdoAdiChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1)
)
tmnxVdoAdiChlEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlGrpAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlSrcAddress"),
)
if mibBuilder.loadTexts:
    tmnxVdoAdiChlEntry.setStatus("current")
_TmnxVdoAdiChlGrpAddrType_Type = InetAddressType
_TmnxVdoAdiChlGrpAddrType_Object = MibTableColumn
tmnxVdoAdiChlGrpAddrType = _TmnxVdoAdiChlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 1),
    _TmnxVdoAdiChlGrpAddrType_Type()
)
tmnxVdoAdiChlGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlGrpAddrType.setStatus("current")


class _TmnxVdoAdiChlGrpAddress_Type(InetAddress):
    """Custom type tmnxVdoAdiChlGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoAdiChlGrpAddress_Type.__name__ = "InetAddress"
_TmnxVdoAdiChlGrpAddress_Object = MibTableColumn
tmnxVdoAdiChlGrpAddress = _TmnxVdoAdiChlGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 2),
    _TmnxVdoAdiChlGrpAddress_Type()
)
tmnxVdoAdiChlGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlGrpAddress.setStatus("current")
_TmnxVdoAdiChlSrcAddrType_Type = InetAddressType
_TmnxVdoAdiChlSrcAddrType_Object = MibTableColumn
tmnxVdoAdiChlSrcAddrType = _TmnxVdoAdiChlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 3),
    _TmnxVdoAdiChlSrcAddrType_Type()
)
tmnxVdoAdiChlSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlSrcAddrType.setStatus("current")


class _TmnxVdoAdiChlSrcAddress_Type(InetAddress):
    """Custom type tmnxVdoAdiChlSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoAdiChlSrcAddress_Type.__name__ = "InetAddress"
_TmnxVdoAdiChlSrcAddress_Object = MibTableColumn
tmnxVdoAdiChlSrcAddress = _TmnxVdoAdiChlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 4),
    _TmnxVdoAdiChlSrcAddress_Type()
)
tmnxVdoAdiChlSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlSrcAddress.setStatus("current")
_TmnxVdoAdiChlRowStatus_Type = RowStatus
_TmnxVdoAdiChlRowStatus_Object = MibTableColumn
tmnxVdoAdiChlRowStatus = _TmnxVdoAdiChlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 5),
    _TmnxVdoAdiChlRowStatus_Type()
)
tmnxVdoAdiChlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlRowStatus.setStatus("current")


class _TmnxVdoAdiChlName_Type(TNamedItem):
    """Custom type tmnxVdoAdiChlName based on TNamedItem"""
    subtypeSpec = TNamedItem.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TmnxVdoAdiChlName_Type.__name__ = "TNamedItem"
_TmnxVdoAdiChlName_Object = MibTableColumn
tmnxVdoAdiChlName = _TmnxVdoAdiChlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 6),
    _TmnxVdoAdiChlName_Type()
)
tmnxVdoAdiChlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlName.setStatus("current")


class _TmnxVdoAdiChlDescription_Type(TItemDescription):
    """Custom type tmnxVdoAdiChlDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxVdoAdiChlDescription_Type.__name__ = "TItemDescription"
_TmnxVdoAdiChlDescription_Object = MibTableColumn
tmnxVdoAdiChlDescription = _TmnxVdoAdiChlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 7),
    _TmnxVdoAdiChlDescription_Type()
)
tmnxVdoAdiChlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlDescription.setStatus("current")


class _TmnxVdoAdiChlForwardScte35_Type(TruthValue):
    """Custom type tmnxVdoAdiChlForwardScte35 based on TruthValue"""
    defaultValue = 1


_TmnxVdoAdiChlForwardScte35_Type.__name__ = "TruthValue"
_TmnxVdoAdiChlForwardScte35_Object = MibTableColumn
tmnxVdoAdiChlForwardScte35 = _TmnxVdoAdiChlForwardScte35_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 5, 1, 8),
    _TmnxVdoAdiChlForwardScte35_Type()
)
tmnxVdoAdiChlForwardScte35.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlForwardScte35.setStatus("current")
_TmnxVdoAdiZoneChlTable_Object = MibTable
tmnxVdoAdiZoneChlTable = _TmnxVdoAdiZoneChlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlTable.setStatus("current")
_TmnxVdoAdiZoneChlEntry_Object = MibTableRow
tmnxVdoAdiZoneChlEntry = _TmnxVdoAdiZoneChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1)
)
tmnxVdoAdiZoneChlEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlGrpAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlSrcAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlGrpAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlSrcAddress"),
)
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlEntry.setStatus("current")
_TmnxVdoAdiZoneChlGrpAddrType_Type = InetAddressType
_TmnxVdoAdiZoneChlGrpAddrType_Object = MibTableColumn
tmnxVdoAdiZoneChlGrpAddrType = _TmnxVdoAdiZoneChlGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1, 1),
    _TmnxVdoAdiZoneChlGrpAddrType_Type()
)
tmnxVdoAdiZoneChlGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlGrpAddrType.setStatus("current")


class _TmnxVdoAdiZoneChlGrpAddress_Type(InetAddress):
    """Custom type tmnxVdoAdiZoneChlGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoAdiZoneChlGrpAddress_Type.__name__ = "InetAddress"
_TmnxVdoAdiZoneChlGrpAddress_Object = MibTableColumn
tmnxVdoAdiZoneChlGrpAddress = _TmnxVdoAdiZoneChlGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1, 2),
    _TmnxVdoAdiZoneChlGrpAddress_Type()
)
tmnxVdoAdiZoneChlGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlGrpAddress.setStatus("current")
_TmnxVdoAdiZoneChlSrcAddrType_Type = InetAddressType
_TmnxVdoAdiZoneChlSrcAddrType_Object = MibTableColumn
tmnxVdoAdiZoneChlSrcAddrType = _TmnxVdoAdiZoneChlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1, 3),
    _TmnxVdoAdiZoneChlSrcAddrType_Type()
)
tmnxVdoAdiZoneChlSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlSrcAddrType.setStatus("current")


class _TmnxVdoAdiZoneChlSrcAddress_Type(InetAddress):
    """Custom type tmnxVdoAdiZoneChlSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoAdiZoneChlSrcAddress_Type.__name__ = "InetAddress"
_TmnxVdoAdiZoneChlSrcAddress_Object = MibTableColumn
tmnxVdoAdiZoneChlSrcAddress = _TmnxVdoAdiZoneChlSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1, 4),
    _TmnxVdoAdiZoneChlSrcAddress_Type()
)
tmnxVdoAdiZoneChlSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlSrcAddress.setStatus("current")
_TmnxVdoAdiZoneChlRowStatus_Type = RowStatus
_TmnxVdoAdiZoneChlRowStatus_Object = MibTableColumn
tmnxVdoAdiZoneChlRowStatus = _TmnxVdoAdiZoneChlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1, 5),
    _TmnxVdoAdiZoneChlRowStatus_Type()
)
tmnxVdoAdiZoneChlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlRowStatus.setStatus("current")


class _TmnxVdoAdiZoneChlName_Type(TNamedItem):
    """Custom type tmnxVdoAdiZoneChlName based on TNamedItem"""
    subtypeSpec = TNamedItem.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TmnxVdoAdiZoneChlName_Type.__name__ = "TNamedItem"
_TmnxVdoAdiZoneChlName_Object = MibTableColumn
tmnxVdoAdiZoneChlName = _TmnxVdoAdiZoneChlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 6, 1, 6),
    _TmnxVdoAdiZoneChlName_Type()
)
tmnxVdoAdiZoneChlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlName.setStatus("current")
_TmnxVdoGrpSrcStatTable_Object = MibTable
tmnxVdoGrpSrcStatTable = _TmnxVdoGrpSrcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStatTable.setStatus("current")
_TmnxVdoGrpSrcStatEntry_Object = MibTableRow
tmnxVdoGrpSrcStatEntry = _TmnxVdoGrpSrcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1)
)
tmnxVdoGrpSrcStatEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGroupAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStatEntry.setStatus("current")
_TmnxVdoGrpSrcGrpAddrType_Type = InetAddressType
_TmnxVdoGrpSrcGrpAddrType_Object = MibTableColumn
tmnxVdoGrpSrcGrpAddrType = _TmnxVdoGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 1),
    _TmnxVdoGrpSrcGrpAddrType_Type()
)
tmnxVdoGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcGrpAddrType.setStatus("current")


class _TmnxVdoGrpSrcGroupAddress_Type(InetAddress):
    """Custom type tmnxVdoGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_TmnxVdoGrpSrcGroupAddress_Object = MibTableColumn
tmnxVdoGrpSrcGroupAddress = _TmnxVdoGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 2),
    _TmnxVdoGrpSrcGroupAddress_Type()
)
tmnxVdoGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcGroupAddress.setStatus("current")
_TmnxVdoGrpSrcSrcAddrType_Type = InetAddressType
_TmnxVdoGrpSrcSrcAddrType_Object = MibTableColumn
tmnxVdoGrpSrcSrcAddrType = _TmnxVdoGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 3),
    _TmnxVdoGrpSrcSrcAddrType_Type()
)
tmnxVdoGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcSrcAddrType.setStatus("current")


class _TmnxVdoGrpSrcSourceAddress_Type(InetAddress):
    """Custom type tmnxVdoGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_TmnxVdoGrpSrcSourceAddress_Object = MibTableColumn
tmnxVdoGrpSrcSourceAddress = _TmnxVdoGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 4),
    _TmnxVdoGrpSrcSourceAddress_Type()
)
tmnxVdoGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcSourceAddress.setStatus("current")


class _TmnxVdoGrpSrcStreamType_Type(Integer32):
    """Custom type tmnxVdoGrpSrcStreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network", 0),
          ("zone", 1))
    )


_TmnxVdoGrpSrcStreamType_Type.__name__ = "Integer32"
_TmnxVdoGrpSrcStreamType_Object = MibTableColumn
tmnxVdoGrpSrcStreamType = _TmnxVdoGrpSrcStreamType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 5),
    _TmnxVdoGrpSrcStreamType_Type()
)
tmnxVdoGrpSrcStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStreamType.setStatus("current")
_TmnxVdoGrpSrcVdoGrpId_Type = TmnxVdoGrpId
_TmnxVdoGrpSrcVdoGrpId_Object = MibTableColumn
tmnxVdoGrpSrcVdoGrpId = _TmnxVdoGrpSrcVdoGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 6),
    _TmnxVdoGrpSrcVdoGrpId_Type()
)
tmnxVdoGrpSrcVdoGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVdoGrpId.setStatus("current")
_TmnxVdoGrpSrcAdminRTBufferSize_Type = TmnxMcPathVdoBufferSize
_TmnxVdoGrpSrcAdminRTBufferSize_Object = MibTableColumn
tmnxVdoGrpSrcAdminRTBufferSize = _TmnxVdoGrpSrcAdminRTBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 7),
    _TmnxVdoGrpSrcAdminRTBufferSize_Type()
)
tmnxVdoGrpSrcAdminRTBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAdminRTBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAdminRTBufferSize.setUnits("milliseconds")
_TmnxVdoGrpSrcSSRCId_Type = Unsigned32
_TmnxVdoGrpSrcSSRCId_Object = MibTableColumn
tmnxVdoGrpSrcSSRCId = _TmnxVdoGrpSrcSSRCId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 8),
    _TmnxVdoGrpSrcSSRCId_Type()
)
tmnxVdoGrpSrcSSRCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcSSRCId.setStatus("current")
_TmnxVdoGrpSrcUDPSrcPort_Type = InetPortNumber
_TmnxVdoGrpSrcUDPSrcPort_Object = MibTableColumn
tmnxVdoGrpSrcUDPSrcPort = _TmnxVdoGrpSrcUDPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 9),
    _TmnxVdoGrpSrcUDPSrcPort_Type()
)
tmnxVdoGrpSrcUDPSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcUDPSrcPort.setStatus("current")
_TmnxVdoGrpSrcUDPDestPort_Type = InetPortNumber
_TmnxVdoGrpSrcUDPDestPort_Object = MibTableColumn
tmnxVdoGrpSrcUDPDestPort = _TmnxVdoGrpSrcUDPDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 10),
    _TmnxVdoGrpSrcUDPDestPort_Type()
)
tmnxVdoGrpSrcUDPDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcUDPDestPort.setStatus("current")
_TmnxVdoGrpSrcUptime_Type = Unsigned32
_TmnxVdoGrpSrcUptime_Object = MibTableColumn
tmnxVdoGrpSrcUptime = _TmnxVdoGrpSrcUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 11),
    _TmnxVdoGrpSrcUptime_Type()
)
tmnxVdoGrpSrcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcUptime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcUptime.setUnits("seconds")
_TmnxVdoGrpSrcAdminBW_Type = Unsigned32
_TmnxVdoGrpSrcAdminBW_Object = MibTableColumn
tmnxVdoGrpSrcAdminBW = _TmnxVdoGrpSrcAdminBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 12),
    _TmnxVdoGrpSrcAdminBW_Type()
)
tmnxVdoGrpSrcAdminBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAdminBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAdminBW.setUnits("kbps")
_TmnxVdoGrpSrcBufferSize_Type = Gauge32
_TmnxVdoGrpSrcBufferSize_Object = MibTableColumn
tmnxVdoGrpSrcBufferSize = _TmnxVdoGrpSrcBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 13),
    _TmnxVdoGrpSrcBufferSize_Type()
)
tmnxVdoGrpSrcBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcBufferSize.setUnits("milliseconds")
_TmnxVdoGrpSrcRxBytes_Type = Counter64
_TmnxVdoGrpSrcRxBytes_Object = MibTableColumn
tmnxVdoGrpSrcRxBytes = _TmnxVdoGrpSrcRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 14),
    _TmnxVdoGrpSrcRxBytes_Type()
)
tmnxVdoGrpSrcRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxBytes.setStatus("current")
_TmnxVdoGrpSrcRxPackets_Type = Counter64
_TmnxVdoGrpSrcRxPackets_Object = MibTableColumn
tmnxVdoGrpSrcRxPackets = _TmnxVdoGrpSrcRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 15),
    _TmnxVdoGrpSrcRxPackets_Type()
)
tmnxVdoGrpSrcRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxPackets.setStatus("current")
_TmnxVdoGrpSrcRxInvalidPackets_Type = Counter64
_TmnxVdoGrpSrcRxInvalidPackets_Object = MibTableColumn
tmnxVdoGrpSrcRxInvalidPackets = _TmnxVdoGrpSrcRxInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 16),
    _TmnxVdoGrpSrcRxInvalidPackets_Type()
)
tmnxVdoGrpSrcRxInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxInvalidPackets.setStatus("current")
_TmnxVdoGrpSrcTxBytes_Type = Counter64
_TmnxVdoGrpSrcTxBytes_Object = MibTableColumn
tmnxVdoGrpSrcTxBytes = _TmnxVdoGrpSrcTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 17),
    _TmnxVdoGrpSrcTxBytes_Type()
)
tmnxVdoGrpSrcTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcTxBytes.setStatus("current")
_TmnxVdoGrpSrcTxPackets_Type = Counter64
_TmnxVdoGrpSrcTxPackets_Object = MibTableColumn
tmnxVdoGrpSrcTxPackets = _TmnxVdoGrpSrcTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 18),
    _TmnxVdoGrpSrcTxPackets_Type()
)
tmnxVdoGrpSrcTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcTxPackets.setStatus("current")
_TmnxVdoGrpSrcTxFailedPackets_Type = Counter64
_TmnxVdoGrpSrcTxFailedPackets_Object = MibTableColumn
tmnxVdoGrpSrcTxFailedPackets = _TmnxVdoGrpSrcTxFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 19),
    _TmnxVdoGrpSrcTxFailedPackets_Type()
)
tmnxVdoGrpSrcTxFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcTxFailedPackets.setStatus("current")
_TmnxVdoGrpSrcRTClientAdminState_Type = TmnxAdminState
_TmnxVdoGrpSrcRTClientAdminState_Object = MibTableColumn
tmnxVdoGrpSrcRTClientAdminState = _TmnxVdoGrpSrcRTClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 20),
    _TmnxVdoGrpSrcRTClientAdminState_Type()
)
tmnxVdoGrpSrcRTClientAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientAdminState.setStatus("current")
_TmnxVdoGrpSrcRTClntRTSvrAddrType_Type = InetAddressType
_TmnxVdoGrpSrcRTClntRTSvrAddrType_Object = MibTableColumn
tmnxVdoGrpSrcRTClntRTSvrAddrType = _TmnxVdoGrpSrcRTClntRTSvrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 21),
    _TmnxVdoGrpSrcRTClntRTSvrAddrType_Type()
)
tmnxVdoGrpSrcRTClntRTSvrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClntRTSvrAddrType.setStatus("current")


class _TmnxVdoGrpSrcRTClntRTSvrAddr_Type(InetAddress):
    """Custom type tmnxVdoGrpSrcRTClntRTSvrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoGrpSrcRTClntRTSvrAddr_Type.__name__ = "InetAddress"
_TmnxVdoGrpSrcRTClntRTSvrAddr_Object = MibTableColumn
tmnxVdoGrpSrcRTClntRTSvrAddr = _TmnxVdoGrpSrcRTClntRTSvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 22),
    _TmnxVdoGrpSrcRTClntRTSvrAddr_Type()
)
tmnxVdoGrpSrcRTClntRTSvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClntRTSvrAddr.setStatus("current")
_TmnxVdoGrpSrcRTClientRTSrvrPort_Type = InetPortNumber
_TmnxVdoGrpSrcRTClientRTSrvrPort_Object = MibTableColumn
tmnxVdoGrpSrcRTClientRTSrvrPort = _TmnxVdoGrpSrcRTClientRTSrvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 23),
    _TmnxVdoGrpSrcRTClientRTSrvrPort_Type()
)
tmnxVdoGrpSrcRTClientRTSrvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientRTSrvrPort.setStatus("current")
_TmnxVdoGrpSrcRTClientRxReTxBytes_Type = Counter64
_TmnxVdoGrpSrcRTClientRxReTxBytes_Object = MibTableColumn
tmnxVdoGrpSrcRTClientRxReTxBytes = _TmnxVdoGrpSrcRTClientRxReTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 24),
    _TmnxVdoGrpSrcRTClientRxReTxBytes_Type()
)
tmnxVdoGrpSrcRTClientRxReTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientRxReTxBytes.setStatus("current")
_TmnxVdoGrpSrcRTClientRxReTxPkts_Type = Counter64
_TmnxVdoGrpSrcRTClientRxReTxPkts_Object = MibTableColumn
tmnxVdoGrpSrcRTClientRxReTxPkts = _TmnxVdoGrpSrcRTClientRxReTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 25),
    _TmnxVdoGrpSrcRTClientRxReTxPkts_Type()
)
tmnxVdoGrpSrcRTClientRxReTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientRxReTxPkts.setStatus("current")
_TmnxVdoGrpSrcRTClientTxRTReq_Type = Counter32
_TmnxVdoGrpSrcRTClientTxRTReq_Object = MibTableColumn
tmnxVdoGrpSrcRTClientTxRTReq = _TmnxVdoGrpSrcRTClientTxRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 26),
    _TmnxVdoGrpSrcRTClientTxRTReq_Type()
)
tmnxVdoGrpSrcRTClientTxRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientTxRTReq.setStatus("current")
_TmnxVdoGrpSrcRTClientTxRTReqReTx_Type = Counter32
_TmnxVdoGrpSrcRTClientTxRTReqReTx_Object = MibTableColumn
tmnxVdoGrpSrcRTClientTxRTReqReTx = _TmnxVdoGrpSrcRTClientTxRTReqReTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 27),
    _TmnxVdoGrpSrcRTClientTxRTReqReTx_Type()
)
tmnxVdoGrpSrcRTClientTxRTReqReTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientTxRTReqReTx.setStatus("current")
_TmnxVdoGrpSrcRTClientGapsDetectd_Type = Counter32
_TmnxVdoGrpSrcRTClientGapsDetectd_Object = MibTableColumn
tmnxVdoGrpSrcRTClientGapsDetectd = _TmnxVdoGrpSrcRTClientGapsDetectd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 28),
    _TmnxVdoGrpSrcRTClientGapsDetectd_Type()
)
tmnxVdoGrpSrcRTClientGapsDetectd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientGapsDetectd.setStatus("current")
_TmnxVdoGrpSrcRTClientFailedReq_Type = Counter32
_TmnxVdoGrpSrcRTClientFailedReq_Object = MibTableColumn
tmnxVdoGrpSrcRTClientFailedReq = _TmnxVdoGrpSrcRTClientFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 29),
    _TmnxVdoGrpSrcRTClientFailedReq_Type()
)
tmnxVdoGrpSrcRTClientFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientFailedReq.setStatus("current")
_TmnxVdoGrpSrcRTSrvrAdminState_Type = TmnxAdminState
_TmnxVdoGrpSrcRTSrvrAdminState_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrAdminState = _TmnxVdoGrpSrcRTSrvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 30),
    _TmnxVdoGrpSrcRTSrvrAdminState_Type()
)
tmnxVdoGrpSrcRTSrvrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrAdminState.setStatus("current")
_TmnxVdoGrpSrcRTSrvrRtpPktsReq_Type = Counter32
_TmnxVdoGrpSrcRTSrvrRtpPktsReq_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrRtpPktsReq = _TmnxVdoGrpSrcRTSrvrRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 31),
    _TmnxVdoGrpSrcRTSrvrRtpPktsReq_Type()
)
tmnxVdoGrpSrcRTSrvrRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrRtpPktsReq.setStatus("current")
_TmnxVdoGrpSrcRTSrvrRxRTReq_Type = Counter32
_TmnxVdoGrpSrcRTSrvrRxRTReq_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrRxRTReq = _TmnxVdoGrpSrcRTSrvrRxRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 32),
    _TmnxVdoGrpSrcRTSrvrRxRTReq_Type()
)
tmnxVdoGrpSrcRTSrvrRxRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrRxRTReq.setStatus("current")
_TmnxVdoGrpSrcRTSrvrRxFailedReq_Type = Counter32
_TmnxVdoGrpSrcRTSrvrRxFailedReq_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrRxFailedReq = _TmnxVdoGrpSrcRTSrvrRxFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 33),
    _TmnxVdoGrpSrcRTSrvrRxFailedReq_Type()
)
tmnxVdoGrpSrcRTSrvrRxFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrRxFailedReq.setStatus("current")
_TmnxVdoGrpSrcRTSrvrTxRTReplies_Type = Counter32
_TmnxVdoGrpSrcRTSrvrTxRTReplies_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrTxRTReplies = _TmnxVdoGrpSrcRTSrvrTxRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 34),
    _TmnxVdoGrpSrcRTSrvrTxRTReplies_Type()
)
tmnxVdoGrpSrcRTSrvrTxRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrTxRTReplies.setStatus("current")
_TmnxVdoGrpSrcRTSrvrTxBytes_Type = Counter64
_TmnxVdoGrpSrcRTSrvrTxBytes_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrTxBytes = _TmnxVdoGrpSrcRTSrvrTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 35),
    _TmnxVdoGrpSrcRTSrvrTxBytes_Type()
)
tmnxVdoGrpSrcRTSrvrTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrTxBytes.setStatus("current")
_TmnxVdoGrpSrcRTSrvrTxPackets_Type = Counter64
_TmnxVdoGrpSrcRTSrvrTxPackets_Object = MibTableColumn
tmnxVdoGrpSrcRTSrvrTxPackets = _TmnxVdoGrpSrcRTSrvrTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 36),
    _TmnxVdoGrpSrcRTSrvrTxPackets_Type()
)
tmnxVdoGrpSrcRTSrvrTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSrvrTxPackets.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrAdminState_Type = TmnxAdminState
_TmnxVdoGrpSrcFCCSrvrAdminState_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrAdminState = _TmnxVdoGrpSrcFCCSrvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 37),
    _TmnxVdoGrpSrcFCCSrvrAdminState_Type()
)
tmnxVdoGrpSrcFCCSrvrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrAdminState.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrChnlType_Type = TmnxMcPathVdoChlType
_TmnxVdoGrpSrcFCCSrvrChnlType_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrChnlType = _TmnxVdoGrpSrcFCCSrvrChnlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 38),
    _TmnxVdoGrpSrcFCCSrvrChnlType_Type()
)
tmnxVdoGrpSrcFCCSrvrChnlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrChnlType.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrRxFCCReq_Type = Counter32
_TmnxVdoGrpSrcFCCSrvrRxFCCReq_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrRxFCCReq = _TmnxVdoGrpSrcFCCSrvrRxFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 39),
    _TmnxVdoGrpSrcFCCSrvrRxFCCReq_Type()
)
tmnxVdoGrpSrcFCCSrvrRxFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrRxFCCReq.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrRxFailedReq_Type = Counter32
_TmnxVdoGrpSrcFCCSrvrRxFailedReq_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrRxFailedReq = _TmnxVdoGrpSrcFCCSrvrRxFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 40),
    _TmnxVdoGrpSrcFCCSrvrRxFailedReq_Type()
)
tmnxVdoGrpSrcFCCSrvrRxFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrRxFailedReq.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrTxFCCReplies_Type = Counter32
_TmnxVdoGrpSrcFCCSrvrTxFCCReplies_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrTxFCCReplies = _TmnxVdoGrpSrcFCCSrvrTxFCCReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 41),
    _TmnxVdoGrpSrcFCCSrvrTxFCCReplies_Type()
)
tmnxVdoGrpSrcFCCSrvrTxFCCReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrTxFCCReplies.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrTxBytes_Type = Counter64
_TmnxVdoGrpSrcFCCSrvrTxBytes_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrTxBytes = _TmnxVdoGrpSrcFCCSrvrTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 42),
    _TmnxVdoGrpSrcFCCSrvrTxBytes_Type()
)
tmnxVdoGrpSrcFCCSrvrTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrTxBytes.setStatus("current")
_TmnxVdoGrpSrcFCCSrvrTxPackets_Type = Counter64
_TmnxVdoGrpSrcFCCSrvrTxPackets_Object = MibTableColumn
tmnxVdoGrpSrcFCCSrvrTxPackets = _TmnxVdoGrpSrcFCCSrvrTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 43),
    _TmnxVdoGrpSrcFCCSrvrTxPackets_Type()
)
tmnxVdoGrpSrcFCCSrvrTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFCCSrvrTxPackets.setStatus("current")
_TmnxVdoGrpSrcADIAdminState_Type = TmnxAdminState
_TmnxVdoGrpSrcADIAdminState_Object = MibTableColumn
tmnxVdoGrpSrcADIAdminState = _TmnxVdoGrpSrcADIAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 44),
    _TmnxVdoGrpSrcADIAdminState_Type()
)
tmnxVdoGrpSrcADIAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIAdminState.setStatus("current")


class _TmnxVdoGrpSrcADICurrentState_Type(Integer32):
    """Custom type tmnxVdoGrpSrcADICurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network", 0),
          ("ad", 1))
    )


_TmnxVdoGrpSrcADICurrentState_Type.__name__ = "Integer32"
_TmnxVdoGrpSrcADICurrentState_Object = MibTableColumn
tmnxVdoGrpSrcADICurrentState = _TmnxVdoGrpSrcADICurrentState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 45),
    _TmnxVdoGrpSrcADICurrentState_Type()
)
tmnxVdoGrpSrcADICurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADICurrentState.setStatus("current")
_TmnxVdoGrpSrcADIPATVersion_Type = Unsigned32
_TmnxVdoGrpSrcADIPATVersion_Object = MibTableColumn
tmnxVdoGrpSrcADIPATVersion = _TmnxVdoGrpSrcADIPATVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 46),
    _TmnxVdoGrpSrcADIPATVersion_Type()
)
tmnxVdoGrpSrcADIPATVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIPATVersion.setStatus("current")
_TmnxVdoGrpSrcADIPMTVersion_Type = Unsigned32
_TmnxVdoGrpSrcADIPMTVersion_Object = MibTableColumn
tmnxVdoGrpSrcADIPMTVersion = _TmnxVdoGrpSrcADIPMTVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 47),
    _TmnxVdoGrpSrcADIPMTVersion_Type()
)
tmnxVdoGrpSrcADIPMTVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIPMTVersion.setStatus("current")
_TmnxVdoGrpSrcADIPATChanges_Type = Counter32
_TmnxVdoGrpSrcADIPATChanges_Object = MibTableColumn
tmnxVdoGrpSrcADIPATChanges = _TmnxVdoGrpSrcADIPATChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 48),
    _TmnxVdoGrpSrcADIPATChanges_Type()
)
tmnxVdoGrpSrcADIPATChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIPATChanges.setStatus("current")
_TmnxVdoGrpSrcADIPMTChanges_Type = Counter32
_TmnxVdoGrpSrcADIPMTChanges_Object = MibTableColumn
tmnxVdoGrpSrcADIPMTChanges = _TmnxVdoGrpSrcADIPMTChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 49),
    _TmnxVdoGrpSrcADIPMTChanges_Type()
)
tmnxVdoGrpSrcADIPMTChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIPMTChanges.setStatus("current")
_TmnxVdoGrpSrcADIRxPackets_Type = Counter64
_TmnxVdoGrpSrcADIRxPackets_Object = MibTableColumn
tmnxVdoGrpSrcADIRxPackets = _TmnxVdoGrpSrcADIRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 50),
    _TmnxVdoGrpSrcADIRxPackets_Type()
)
tmnxVdoGrpSrcADIRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIRxPackets.setStatus("current")
_TmnxVdoGrpSrcADITxPackets_Type = Counter64
_TmnxVdoGrpSrcADITxPackets_Object = MibTableColumn
tmnxVdoGrpSrcADITxPackets = _TmnxVdoGrpSrcADITxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 51),
    _TmnxVdoGrpSrcADITxPackets_Type()
)
tmnxVdoGrpSrcADITxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADITxPackets.setStatus("current")
_TmnxVdoGrpSrcADIRxSCTE35Msgs_Type = Counter32
_TmnxVdoGrpSrcADIRxSCTE35Msgs_Object = MibTableColumn
tmnxVdoGrpSrcADIRxSCTE35Msgs = _TmnxVdoGrpSrcADIRxSCTE35Msgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 52),
    _TmnxVdoGrpSrcADIRxSCTE35Msgs_Type()
)
tmnxVdoGrpSrcADIRxSCTE35Msgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIRxSCTE35Msgs.setStatus("current")
_TmnxVdoGrpSrcADIRxSCTE35MsgEnc_Type = Counter32
_TmnxVdoGrpSrcADIRxSCTE35MsgEnc_Object = MibTableColumn
tmnxVdoGrpSrcADIRxSCTE35MsgEnc = _TmnxVdoGrpSrcADIRxSCTE35MsgEnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 53),
    _TmnxVdoGrpSrcADIRxSCTE35MsgEnc_Type()
)
tmnxVdoGrpSrcADIRxSCTE35MsgEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIRxSCTE35MsgEnc.setStatus("current")
_TmnxVdoGrpSrcADIRxSCTE35MsgUnsup_Type = Counter32
_TmnxVdoGrpSrcADIRxSCTE35MsgUnsup_Object = MibTableColumn
tmnxVdoGrpSrcADIRxSCTE35MsgUnsup = _TmnxVdoGrpSrcADIRxSCTE35MsgUnsup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 54),
    _TmnxVdoGrpSrcADIRxSCTE35MsgUnsup_Type()
)
tmnxVdoGrpSrcADIRxSCTE35MsgUnsup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIRxSCTE35MsgUnsup.setStatus("current")
_TmnxVdoGrpSrcADIRxSCTE35MsgDisc_Type = Counter32
_TmnxVdoGrpSrcADIRxSCTE35MsgDisc_Object = MibTableColumn
tmnxVdoGrpSrcADIRxSCTE35MsgDisc = _TmnxVdoGrpSrcADIRxSCTE35MsgDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 55),
    _TmnxVdoGrpSrcADIRxSCTE35MsgDisc_Type()
)
tmnxVdoGrpSrcADIRxSCTE35MsgDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIRxSCTE35MsgDisc.setStatus("current")
_TmnxVdoGrpSrcADIUnsuppTSLenPkts_Type = Counter32
_TmnxVdoGrpSrcADIUnsuppTSLenPkts_Object = MibTableColumn
tmnxVdoGrpSrcADIUnsuppTSLenPkts = _TmnxVdoGrpSrcADIUnsuppTSLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 56),
    _TmnxVdoGrpSrcADIUnsuppTSLenPkts_Type()
)
tmnxVdoGrpSrcADIUnsuppTSLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcADIUnsuppTSLenPkts.setStatus("current")


class _TmnxVdoGrpSrcRTClientPort_Type(Unsigned32):
    """Custom type tmnxVdoGrpSrcRTClientPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6000, 7000),
    )


_TmnxVdoGrpSrcRTClientPort_Type.__name__ = "Unsigned32"
_TmnxVdoGrpSrcRTClientPort_Object = MibTableColumn
tmnxVdoGrpSrcRTClientPort = _TmnxVdoGrpSrcRTClientPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 57),
    _TmnxVdoGrpSrcRTClientPort_Type()
)
tmnxVdoGrpSrcRTClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTClientPort.setStatus("current")
_TmnxVdoGrpSrcDupSeqNumber_Type = Counter32
_TmnxVdoGrpSrcDupSeqNumber_Object = MibTableColumn
tmnxVdoGrpSrcDupSeqNumber = _TmnxVdoGrpSrcDupSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 58),
    _TmnxVdoGrpSrcDupSeqNumber_Type()
)
tmnxVdoGrpSrcDupSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcDupSeqNumber.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetPkts_Type = Counter64
_TmnxVdoGrpSrcRTSTxMcRetPkts_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetPkts = _TmnxVdoGrpSrcRTSTxMcRetPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 59),
    _TmnxVdoGrpSrcRTSTxMcRetPkts_Type()
)
tmnxVdoGrpSrcRTSTxMcRetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetPkts.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetPktsL32_Type = Counter32
_TmnxVdoGrpSrcRTSTxMcRetPktsL32_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetPktsL32 = _TmnxVdoGrpSrcRTSTxMcRetPktsL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 60),
    _TmnxVdoGrpSrcRTSTxMcRetPktsL32_Type()
)
tmnxVdoGrpSrcRTSTxMcRetPktsL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetPktsL32.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetPktsH32_Type = Counter32
_TmnxVdoGrpSrcRTSTxMcRetPktsH32_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetPktsH32 = _TmnxVdoGrpSrcRTSTxMcRetPktsH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 61),
    _TmnxVdoGrpSrcRTSTxMcRetPktsH32_Type()
)
tmnxVdoGrpSrcRTSTxMcRetPktsH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetPktsH32.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetBytes_Type = Counter64
_TmnxVdoGrpSrcRTSTxMcRetBytes_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetBytes = _TmnxVdoGrpSrcRTSTxMcRetBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 62),
    _TmnxVdoGrpSrcRTSTxMcRetBytes_Type()
)
tmnxVdoGrpSrcRTSTxMcRetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetBytes.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetBytesL32_Type = Counter32
_TmnxVdoGrpSrcRTSTxMcRetBytesL32_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetBytesL32 = _TmnxVdoGrpSrcRTSTxMcRetBytesL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 63),
    _TmnxVdoGrpSrcRTSTxMcRetBytesL32_Type()
)
tmnxVdoGrpSrcRTSTxMcRetBytesL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetBytesL32.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetBytesH32_Type = Counter32
_TmnxVdoGrpSrcRTSTxMcRetBytesH32_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetBytesH32 = _TmnxVdoGrpSrcRTSTxMcRetBytesH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 64),
    _TmnxVdoGrpSrcRTSTxMcRetBytesH32_Type()
)
tmnxVdoGrpSrcRTSTxMcRetBytesH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetBytesH32.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetErrs_Type = Counter64
_TmnxVdoGrpSrcRTSTxMcRetErrs_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetErrs = _TmnxVdoGrpSrcRTSTxMcRetErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 65),
    _TmnxVdoGrpSrcRTSTxMcRetErrs_Type()
)
tmnxVdoGrpSrcRTSTxMcRetErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetErrs.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetErrsL32_Type = Counter32
_TmnxVdoGrpSrcRTSTxMcRetErrsL32_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetErrsL32 = _TmnxVdoGrpSrcRTSTxMcRetErrsL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 66),
    _TmnxVdoGrpSrcRTSTxMcRetErrsL32_Type()
)
tmnxVdoGrpSrcRTSTxMcRetErrsL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetErrsL32.setStatus("current")
_TmnxVdoGrpSrcRTSTxMcRetErrsH32_Type = Counter32
_TmnxVdoGrpSrcRTSTxMcRetErrsH32_Object = MibTableColumn
tmnxVdoGrpSrcRTSTxMcRetErrsH32 = _TmnxVdoGrpSrcRTSTxMcRetErrsH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 67),
    _TmnxVdoGrpSrcRTSTxMcRetErrsH32_Type()
)
tmnxVdoGrpSrcRTSTxMcRetErrsH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSTxMcRetErrsH32.setStatus("current")
_TmnxVdoGrpSrcRTSRetReqQnc_Type = Counter64
_TmnxVdoGrpSrcRTSRetReqQnc_Object = MibTableColumn
tmnxVdoGrpSrcRTSRetReqQnc = _TmnxVdoGrpSrcRTSRetReqQnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 68),
    _TmnxVdoGrpSrcRTSRetReqQnc_Type()
)
tmnxVdoGrpSrcRTSRetReqQnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSRetReqQnc.setStatus("current")
_TmnxVdoGrpSrcRTSRetReqQncL32_Type = Counter32
_TmnxVdoGrpSrcRTSRetReqQncL32_Object = MibTableColumn
tmnxVdoGrpSrcRTSRetReqQncL32 = _TmnxVdoGrpSrcRTSRetReqQncL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 69),
    _TmnxVdoGrpSrcRTSRetReqQncL32_Type()
)
tmnxVdoGrpSrcRTSRetReqQncL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSRetReqQncL32.setStatus("current")
_TmnxVdoGrpSrcRTSRetReqQncH32_Type = Counter32
_TmnxVdoGrpSrcRTSRetReqQncH32_Object = MibTableColumn
tmnxVdoGrpSrcRTSRetReqQncH32 = _TmnxVdoGrpSrcRTSRetReqQncH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 70),
    _TmnxVdoGrpSrcRTSRetReqQncH32_Type()
)
tmnxVdoGrpSrcRTSRetReqQncH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSRetReqQncH32.setStatus("current")
_TmnxVdoGrpSrcRTSRetReqCrt_Type = Counter64
_TmnxVdoGrpSrcRTSRetReqCrt_Object = MibTableColumn
tmnxVdoGrpSrcRTSRetReqCrt = _TmnxVdoGrpSrcRTSRetReqCrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 71),
    _TmnxVdoGrpSrcRTSRetReqCrt_Type()
)
tmnxVdoGrpSrcRTSRetReqCrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSRetReqCrt.setStatus("current")
_TmnxVdoGrpSrcRTSRetReqCrtL32_Type = Counter32
_TmnxVdoGrpSrcRTSRetReqCrtL32_Object = MibTableColumn
tmnxVdoGrpSrcRTSRetReqCrtL32 = _TmnxVdoGrpSrcRTSRetReqCrtL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 72),
    _TmnxVdoGrpSrcRTSRetReqCrtL32_Type()
)
tmnxVdoGrpSrcRTSRetReqCrtL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSRetReqCrtL32.setStatus("current")
_TmnxVdoGrpSrcRTSRetReqCrtH32_Type = Counter32
_TmnxVdoGrpSrcRTSRetReqCrtH32_Object = MibTableColumn
tmnxVdoGrpSrcRTSRetReqCrtH32 = _TmnxVdoGrpSrcRTSRetReqCrtH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 73),
    _TmnxVdoGrpSrcRTSRetReqCrtH32_Type()
)
tmnxVdoGrpSrcRTSRetReqCrtH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRTSRetReqCrtH32.setStatus("current")
_TmnxVdoGrpSrcRxDupSsrcDrops_Type = Counter32
_TmnxVdoGrpSrcRxDupSsrcDrops_Object = MibTableColumn
tmnxVdoGrpSrcRxDupSsrcDrops = _TmnxVdoGrpSrcRxDupSsrcDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 74),
    _TmnxVdoGrpSrcRxDupSsrcDrops_Type()
)
tmnxVdoGrpSrcRxDupSsrcDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxDupSsrcDrops.setStatus("current")
_TmnxVdoGrpSrcDupSsrc_Type = Counter32
_TmnxVdoGrpSrcDupSsrc_Object = MibTableColumn
tmnxVdoGrpSrcDupSsrc = _TmnxVdoGrpSrcDupSsrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 75),
    _TmnxVdoGrpSrcDupSsrc_Type()
)
tmnxVdoGrpSrcDupSsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcDupSsrc.setStatus("current")


class _TmnxVdoGrpSrcFccMinDuration_Type(Unsigned32):
    """Custom type tmnxVdoGrpSrcFccMinDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxVdoGrpSrcFccMinDuration_Type.__name__ = "Unsigned32"
_TmnxVdoGrpSrcFccMinDuration_Object = MibTableColumn
tmnxVdoGrpSrcFccMinDuration = _TmnxVdoGrpSrcFccMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 76),
    _TmnxVdoGrpSrcFccMinDuration_Type()
)
tmnxVdoGrpSrcFccMinDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFccMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcFccMinDuration.setUnits("milliseconds")


class _TmnxVdoGrpSrcAudioReorder_Type(Unsigned32):
    """Custom type tmnxVdoGrpSrcAudioReorder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxVdoGrpSrcAudioReorder_Type.__name__ = "Unsigned32"
_TmnxVdoGrpSrcAudioReorder_Object = MibTableColumn
tmnxVdoGrpSrcAudioReorder = _TmnxVdoGrpSrcAudioReorder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 77),
    _TmnxVdoGrpSrcAudioReorder_Type()
)
tmnxVdoGrpSrcAudioReorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAudioReorder.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAudioReorder.setUnits("milliseconds")
_TmnxVdoGrpSrcRxBytesSaved_Type = Counter64
_TmnxVdoGrpSrcRxBytesSaved_Object = MibTableColumn
tmnxVdoGrpSrcRxBytesSaved = _TmnxVdoGrpSrcRxBytesSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 78),
    _TmnxVdoGrpSrcRxBytesSaved_Type()
)
tmnxVdoGrpSrcRxBytesSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxBytesSaved.setStatus("current")
_TmnxVdoGrpSrcRxBytesSavedL32_Type = Counter32
_TmnxVdoGrpSrcRxBytesSavedL32_Object = MibTableColumn
tmnxVdoGrpSrcRxBytesSavedL32 = _TmnxVdoGrpSrcRxBytesSavedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 79),
    _TmnxVdoGrpSrcRxBytesSavedL32_Type()
)
tmnxVdoGrpSrcRxBytesSavedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxBytesSavedL32.setStatus("current")
_TmnxVdoGrpSrcRxBytesSavedH32_Type = Counter32
_TmnxVdoGrpSrcRxBytesSavedH32_Object = MibTableColumn
tmnxVdoGrpSrcRxBytesSavedH32 = _TmnxVdoGrpSrcRxBytesSavedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 80),
    _TmnxVdoGrpSrcRxBytesSavedH32_Type()
)
tmnxVdoGrpSrcRxBytesSavedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxBytesSavedH32.setStatus("current")
_TmnxVdoGrpSrcRxPacketsSaved_Type = Counter64
_TmnxVdoGrpSrcRxPacketsSaved_Object = MibTableColumn
tmnxVdoGrpSrcRxPacketsSaved = _TmnxVdoGrpSrcRxPacketsSaved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 81),
    _TmnxVdoGrpSrcRxPacketsSaved_Type()
)
tmnxVdoGrpSrcRxPacketsSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxPacketsSaved.setStatus("current")
_TmnxVdoGrpSrcRxPacketsSavedL32_Type = Counter32
_TmnxVdoGrpSrcRxPacketsSavedL32_Object = MibTableColumn
tmnxVdoGrpSrcRxPacketsSavedL32 = _TmnxVdoGrpSrcRxPacketsSavedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 82),
    _TmnxVdoGrpSrcRxPacketsSavedL32_Type()
)
tmnxVdoGrpSrcRxPacketsSavedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxPacketsSavedL32.setStatus("current")
_TmnxVdoGrpSrcRxPacketsSavedH32_Type = Counter32
_TmnxVdoGrpSrcRxPacketsSavedH32_Object = MibTableColumn
tmnxVdoGrpSrcRxPacketsSavedH32 = _TmnxVdoGrpSrcRxPacketsSavedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 83),
    _TmnxVdoGrpSrcRxPacketsSavedH32_Type()
)
tmnxVdoGrpSrcRxPacketsSavedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRxPacketsSavedH32.setStatus("current")
_TmnxVdoGrpSrcStatOperBW_Type = Unsigned32
_TmnxVdoGrpSrcStatOperBW_Object = MibTableColumn
tmnxVdoGrpSrcStatOperBW = _TmnxVdoGrpSrcStatOperBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 84),
    _TmnxVdoGrpSrcStatOperBW_Type()
)
tmnxVdoGrpSrcStatOperBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStatOperBW.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStatOperBW.setUnits("kbps")
_TmnxVdoGrpSrcRouterIfName_Type = TNamedItemOrEmpty
_TmnxVdoGrpSrcRouterIfName_Object = MibTableColumn
tmnxVdoGrpSrcRouterIfName = _TmnxVdoGrpSrcRouterIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 85),
    _TmnxVdoGrpSrcRouterIfName_Type()
)
tmnxVdoGrpSrcRouterIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcRouterIfName.setStatus("current")
_TmnxVdoGrpSrcNumFccDentedPkts_Type = Counter32
_TmnxVdoGrpSrcNumFccDentedPkts_Object = MibTableColumn
tmnxVdoGrpSrcNumFccDentedPkts = _TmnxVdoGrpSrcNumFccDentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 7, 1, 86),
    _TmnxVdoGrpSrcNumFccDentedPkts_Type()
)
tmnxVdoGrpSrcNumFccDentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcNumFccDentedPkts.setStatus("current")
_TmnxVdoSGStatV1Table_Object = MibTable
tmnxVdoSGStatV1Table = _TmnxVdoSGStatV1Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxVdoSGStatV1Table.setStatus("current")
_TmnxVdoSGStatV1Entry_Object = MibTableRow
tmnxVdoSGStatV1Entry = _TmnxVdoSGStatV1Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoSGStatV1Entry.setStatus("current")
_TmnxVdoSGV1RxBytesLow32_Type = Counter32
_TmnxVdoSGV1RxBytesLow32_Object = MibTableColumn
tmnxVdoSGV1RxBytesLow32 = _TmnxVdoSGV1RxBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 1),
    _TmnxVdoSGV1RxBytesLow32_Type()
)
tmnxVdoSGV1RxBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RxBytesLow32.setStatus("current")
_TmnxVdoSGV1RxBytesHigh32_Type = Counter32
_TmnxVdoSGV1RxBytesHigh32_Object = MibTableColumn
tmnxVdoSGV1RxBytesHigh32 = _TmnxVdoSGV1RxBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 2),
    _TmnxVdoSGV1RxBytesHigh32_Type()
)
tmnxVdoSGV1RxBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RxBytesHigh32.setStatus("current")
_TmnxVdoSGV1RxPacketsLow32_Type = Counter32
_TmnxVdoSGV1RxPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1RxPacketsLow32 = _TmnxVdoSGV1RxPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 3),
    _TmnxVdoSGV1RxPacketsLow32_Type()
)
tmnxVdoSGV1RxPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RxPacketsLow32.setStatus("current")
_TmnxVdoSGV1RxPacketsHigh32_Type = Counter32
_TmnxVdoSGV1RxPacketsHigh32_Object = MibTableColumn
tmnxVdoSGV1RxPacketsHigh32 = _TmnxVdoSGV1RxPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 4),
    _TmnxVdoSGV1RxPacketsHigh32_Type()
)
tmnxVdoSGV1RxPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RxPacketsHigh32.setStatus("current")
_TmnxVdoSGV1RxInvalidPacketsLow32_Type = Counter32
_TmnxVdoSGV1RxInvalidPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1RxInvalidPacketsLow32 = _TmnxVdoSGV1RxInvalidPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 5),
    _TmnxVdoSGV1RxInvalidPacketsLow32_Type()
)
tmnxVdoSGV1RxInvalidPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RxInvalidPacketsLow32.setStatus("current")
_TmnxVdoSGV1RxInvalidPacketsHgh32_Type = Counter32
_TmnxVdoSGV1RxInvalidPacketsHgh32_Object = MibTableColumn
tmnxVdoSGV1RxInvalidPacketsHgh32 = _TmnxVdoSGV1RxInvalidPacketsHgh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 6),
    _TmnxVdoSGV1RxInvalidPacketsHgh32_Type()
)
tmnxVdoSGV1RxInvalidPacketsHgh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RxInvalidPacketsHgh32.setStatus("current")
_TmnxVdoSGV1TxBytesLow32_Type = Counter32
_TmnxVdoSGV1TxBytesLow32_Object = MibTableColumn
tmnxVdoSGV1TxBytesLow32 = _TmnxVdoSGV1TxBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 7),
    _TmnxVdoSGV1TxBytesLow32_Type()
)
tmnxVdoSGV1TxBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1TxBytesLow32.setStatus("current")
_TmnxVdoSGV1TxBytesHigh32_Type = Counter32
_TmnxVdoSGV1TxBytesHigh32_Object = MibTableColumn
tmnxVdoSGV1TxBytesHigh32 = _TmnxVdoSGV1TxBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 8),
    _TmnxVdoSGV1TxBytesHigh32_Type()
)
tmnxVdoSGV1TxBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1TxBytesHigh32.setStatus("current")
_TmnxVdoSGV1TxPacketsLow32_Type = Counter32
_TmnxVdoSGV1TxPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1TxPacketsLow32 = _TmnxVdoSGV1TxPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 9),
    _TmnxVdoSGV1TxPacketsLow32_Type()
)
tmnxVdoSGV1TxPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1TxPacketsLow32.setStatus("current")
_TmnxVdoSGV1TxPacketsHigh32_Type = Counter32
_TmnxVdoSGV1TxPacketsHigh32_Object = MibTableColumn
tmnxVdoSGV1TxPacketsHigh32 = _TmnxVdoSGV1TxPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 10),
    _TmnxVdoSGV1TxPacketsHigh32_Type()
)
tmnxVdoSGV1TxPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1TxPacketsHigh32.setStatus("current")
_TmnxVdoSGV1TxFailedPacketsLow32_Type = Counter32
_TmnxVdoSGV1TxFailedPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1TxFailedPacketsLow32 = _TmnxVdoSGV1TxFailedPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 11),
    _TmnxVdoSGV1TxFailedPacketsLow32_Type()
)
tmnxVdoSGV1TxFailedPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1TxFailedPacketsLow32.setStatus("current")
_TmnxVdoSGV1TxFailedPacketsHigh32_Type = Counter32
_TmnxVdoSGV1TxFailedPacketsHigh32_Object = MibTableColumn
tmnxVdoSGV1TxFailedPacketsHigh32 = _TmnxVdoSGV1TxFailedPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 12),
    _TmnxVdoSGV1TxFailedPacketsHigh32_Type()
)
tmnxVdoSGV1TxFailedPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1TxFailedPacketsHigh32.setStatus("current")
_TmnxVdoSGV1RTClntRxReTxBytsLow32_Type = Counter32
_TmnxVdoSGV1RTClntRxReTxBytsLow32_Object = MibTableColumn
tmnxVdoSGV1RTClntRxReTxBytsLow32 = _TmnxVdoSGV1RTClntRxReTxBytsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 13),
    _TmnxVdoSGV1RTClntRxReTxBytsLow32_Type()
)
tmnxVdoSGV1RTClntRxReTxBytsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTClntRxReTxBytsLow32.setStatus("current")
_TmnxVdoSGV1RTClntRxReTxBytsHgh32_Type = Counter32
_TmnxVdoSGV1RTClntRxReTxBytsHgh32_Object = MibTableColumn
tmnxVdoSGV1RTClntRxReTxBytsHgh32 = _TmnxVdoSGV1RTClntRxReTxBytsHgh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 14),
    _TmnxVdoSGV1RTClntRxReTxBytsHgh32_Type()
)
tmnxVdoSGV1RTClntRxReTxBytsHgh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTClntRxReTxBytsHgh32.setStatus("current")
_TmnxVdoSGV1RTClntRxReTxPktsLow32_Type = Counter32
_TmnxVdoSGV1RTClntRxReTxPktsLow32_Object = MibTableColumn
tmnxVdoSGV1RTClntRxReTxPktsLow32 = _TmnxVdoSGV1RTClntRxReTxPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 15),
    _TmnxVdoSGV1RTClntRxReTxPktsLow32_Type()
)
tmnxVdoSGV1RTClntRxReTxPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTClntRxReTxPktsLow32.setStatus("current")
_TmnxVdoSGV1RTClntRxReTxPktsHgh32_Type = Counter32
_TmnxVdoSGV1RTClntRxReTxPktsHgh32_Object = MibTableColumn
tmnxVdoSGV1RTClntRxReTxPktsHgh32 = _TmnxVdoSGV1RTClntRxReTxPktsHgh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 16),
    _TmnxVdoSGV1RTClntRxReTxPktsHgh32_Type()
)
tmnxVdoSGV1RTClntRxReTxPktsHgh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTClntRxReTxPktsHgh32.setStatus("current")
_TmnxVdoSGV1RTSrvrTxBytesLow32_Type = Counter32
_TmnxVdoSGV1RTSrvrTxBytesLow32_Object = MibTableColumn
tmnxVdoSGV1RTSrvrTxBytesLow32 = _TmnxVdoSGV1RTSrvrTxBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 17),
    _TmnxVdoSGV1RTSrvrTxBytesLow32_Type()
)
tmnxVdoSGV1RTSrvrTxBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTSrvrTxBytesLow32.setStatus("current")
_TmnxVdoSGV1RTSrvrTxBytesHigh32_Type = Counter32
_TmnxVdoSGV1RTSrvrTxBytesHigh32_Object = MibTableColumn
tmnxVdoSGV1RTSrvrTxBytesHigh32 = _TmnxVdoSGV1RTSrvrTxBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 18),
    _TmnxVdoSGV1RTSrvrTxBytesHigh32_Type()
)
tmnxVdoSGV1RTSrvrTxBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTSrvrTxBytesHigh32.setStatus("current")
_TmnxVdoSGV1RTSrvrTxPacketsLow32_Type = Counter32
_TmnxVdoSGV1RTSrvrTxPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1RTSrvrTxPacketsLow32 = _TmnxVdoSGV1RTSrvrTxPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 19),
    _TmnxVdoSGV1RTSrvrTxPacketsLow32_Type()
)
tmnxVdoSGV1RTSrvrTxPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTSrvrTxPacketsLow32.setStatus("current")
_TmnxVdoSGV1RTSrvrTxPacketsHigh32_Type = Counter32
_TmnxVdoSGV1RTSrvrTxPacketsHigh32_Object = MibTableColumn
tmnxVdoSGV1RTSrvrTxPacketsHigh32 = _TmnxVdoSGV1RTSrvrTxPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 20),
    _TmnxVdoSGV1RTSrvrTxPacketsHigh32_Type()
)
tmnxVdoSGV1RTSrvrTxPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1RTSrvrTxPacketsHigh32.setStatus("current")
_TmnxVdoSGV1FCCSrvrTxBytesLow32_Type = Counter32
_TmnxVdoSGV1FCCSrvrTxBytesLow32_Object = MibTableColumn
tmnxVdoSGV1FCCSrvrTxBytesLow32 = _TmnxVdoSGV1FCCSrvrTxBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 21),
    _TmnxVdoSGV1FCCSrvrTxBytesLow32_Type()
)
tmnxVdoSGV1FCCSrvrTxBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1FCCSrvrTxBytesLow32.setStatus("current")
_TmnxVdoSGV1FCCSrvrTxBytesHigh32_Type = Counter32
_TmnxVdoSGV1FCCSrvrTxBytesHigh32_Object = MibTableColumn
tmnxVdoSGV1FCCSrvrTxBytesHigh32 = _TmnxVdoSGV1FCCSrvrTxBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 22),
    _TmnxVdoSGV1FCCSrvrTxBytesHigh32_Type()
)
tmnxVdoSGV1FCCSrvrTxBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1FCCSrvrTxBytesHigh32.setStatus("current")
_TmnxVdoSGV1FCCSrvrTxPacketsLow32_Type = Counter32
_TmnxVdoSGV1FCCSrvrTxPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1FCCSrvrTxPacketsLow32 = _TmnxVdoSGV1FCCSrvrTxPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 23),
    _TmnxVdoSGV1FCCSrvrTxPacketsLow32_Type()
)
tmnxVdoSGV1FCCSrvrTxPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1FCCSrvrTxPacketsLow32.setStatus("current")
_TmnxVdoSGV1FCCSrvrTxPacketsHgh32_Type = Counter32
_TmnxVdoSGV1FCCSrvrTxPacketsHgh32_Object = MibTableColumn
tmnxVdoSGV1FCCSrvrTxPacketsHgh32 = _TmnxVdoSGV1FCCSrvrTxPacketsHgh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 24),
    _TmnxVdoSGV1FCCSrvrTxPacketsHgh32_Type()
)
tmnxVdoSGV1FCCSrvrTxPacketsHgh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1FCCSrvrTxPacketsHgh32.setStatus("current")
_TmnxVdoSGV1ADIRxPacketsLow32_Type = Counter32
_TmnxVdoSGV1ADIRxPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1ADIRxPacketsLow32 = _TmnxVdoSGV1ADIRxPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 25),
    _TmnxVdoSGV1ADIRxPacketsLow32_Type()
)
tmnxVdoSGV1ADIRxPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1ADIRxPacketsLow32.setStatus("current")
_TmnxVdoSGV1ADIRxPacketsHigh32_Type = Counter32
_TmnxVdoSGV1ADIRxPacketsHigh32_Object = MibTableColumn
tmnxVdoSGV1ADIRxPacketsHigh32 = _TmnxVdoSGV1ADIRxPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 26),
    _TmnxVdoSGV1ADIRxPacketsHigh32_Type()
)
tmnxVdoSGV1ADIRxPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1ADIRxPacketsHigh32.setStatus("current")
_TmnxVdoSGV1ADITxPacketsLow32_Type = Counter32
_TmnxVdoSGV1ADITxPacketsLow32_Object = MibTableColumn
tmnxVdoSGV1ADITxPacketsLow32 = _TmnxVdoSGV1ADITxPacketsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 27),
    _TmnxVdoSGV1ADITxPacketsLow32_Type()
)
tmnxVdoSGV1ADITxPacketsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1ADITxPacketsLow32.setStatus("current")
_TmnxVdoSGV1ADITxPacketsHigh32_Type = Counter32
_TmnxVdoSGV1ADITxPacketsHigh32_Object = MibTableColumn
tmnxVdoSGV1ADITxPacketsHigh32 = _TmnxVdoSGV1ADITxPacketsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 8, 1, 28),
    _TmnxVdoSGV1ADITxPacketsHigh32_Type()
)
tmnxVdoSGV1ADITxPacketsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGV1ADITxPacketsHigh32.setStatus("current")
_TmnxVdoSessionTable_Object = MibTable
tmnxVdoSessionTable = _TmnxVdoSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxVdoSessionTable.setStatus("current")
_TmnxVdoSessionEntry_Object = MibTableRow
tmnxVdoSessionEntry = _TmnxVdoSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1)
)
tmnxVdoSessionEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoSessionSourceAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoSessionSourceAddr"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoSessionSourcePort"),
)
if mibBuilder.loadTexts:
    tmnxVdoSessionEntry.setStatus("current")
_TmnxVdoSessionSourceAddrType_Type = InetAddressType
_TmnxVdoSessionSourceAddrType_Object = MibTableColumn
tmnxVdoSessionSourceAddrType = _TmnxVdoSessionSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 1),
    _TmnxVdoSessionSourceAddrType_Type()
)
tmnxVdoSessionSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoSessionSourceAddrType.setStatus("current")


class _TmnxVdoSessionSourceAddr_Type(InetAddress):
    """Custom type tmnxVdoSessionSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoSessionSourceAddr_Type.__name__ = "InetAddress"
_TmnxVdoSessionSourceAddr_Object = MibTableColumn
tmnxVdoSessionSourceAddr = _TmnxVdoSessionSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 2),
    _TmnxVdoSessionSourceAddr_Type()
)
tmnxVdoSessionSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoSessionSourceAddr.setStatus("current")
_TmnxVdoSessionSourcePort_Type = InetPortNumber
_TmnxVdoSessionSourcePort_Object = MibTableColumn
tmnxVdoSessionSourcePort = _TmnxVdoSessionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 3),
    _TmnxVdoSessionSourcePort_Type()
)
tmnxVdoSessionSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoSessionSourcePort.setStatus("current")
_TmnxVdoSessionSSRCId_Type = Counter32
_TmnxVdoSessionSSRCId_Object = MibTableColumn
tmnxVdoSessionSSRCId = _TmnxVdoSessionSSRCId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 4),
    _TmnxVdoSessionSSRCId_Type()
)
tmnxVdoSessionSSRCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionSSRCId.setStatus("current")
_TmnxVdoSessionUpTime_Type = Unsigned32
_TmnxVdoSessionUpTime_Object = MibTableColumn
tmnxVdoSessionUpTime = _TmnxVdoSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 5),
    _TmnxVdoSessionUpTime_Type()
)
tmnxVdoSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSessionUpTime.setUnits("seconds")
_TmnxVdoSessionExpireTime_Type = Unsigned32
_TmnxVdoSessionExpireTime_Object = MibTableColumn
tmnxVdoSessionExpireTime = _TmnxVdoSessionExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 6),
    _TmnxVdoSessionExpireTime_Type()
)
tmnxVdoSessionExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSessionExpireTime.setUnits("seconds")
_TmnxVdoSessionCName_Type = TNamedItem
_TmnxVdoSessionCName_Object = MibTableColumn
tmnxVdoSessionCName = _TmnxVdoSessionCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 7),
    _TmnxVdoSessionCName_Type()
)
tmnxVdoSessionCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionCName.setStatus("current")
_TmnxVdoSessionDestAddrType_Type = InetAddressType
_TmnxVdoSessionDestAddrType_Object = MibTableColumn
tmnxVdoSessionDestAddrType = _TmnxVdoSessionDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 8),
    _TmnxVdoSessionDestAddrType_Type()
)
tmnxVdoSessionDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionDestAddrType.setStatus("current")


class _TmnxVdoSessionDestAddr_Type(InetAddress):
    """Custom type tmnxVdoSessionDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoSessionDestAddr_Type.__name__ = "InetAddress"
_TmnxVdoSessionDestAddr_Object = MibTableColumn
tmnxVdoSessionDestAddr = _TmnxVdoSessionDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 9),
    _TmnxVdoSessionDestAddr_Type()
)
tmnxVdoSessionDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionDestAddr.setStatus("current")
_TmnxVdoSessionRxFCCRequests_Type = Counter32
_TmnxVdoSessionRxFCCRequests_Object = MibTableColumn
tmnxVdoSessionRxFCCRequests = _TmnxVdoSessionRxFCCRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 10),
    _TmnxVdoSessionRxFCCRequests_Type()
)
tmnxVdoSessionRxFCCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionRxFCCRequests.setStatus("current")
_TmnxVdoSessionTxFCCReplies_Type = Counter32
_TmnxVdoSessionTxFCCReplies_Object = MibTableColumn
tmnxVdoSessionTxFCCReplies = _TmnxVdoSessionTxFCCReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 11),
    _TmnxVdoSessionTxFCCReplies_Type()
)
tmnxVdoSessionTxFCCReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxFCCReplies.setStatus("current")
_TmnxVdoSessionTxFCCPackets_Type = Counter32
_TmnxVdoSessionTxFCCPackets_Object = MibTableColumn
tmnxVdoSessionTxFCCPackets = _TmnxVdoSessionTxFCCPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 12),
    _TmnxVdoSessionTxFCCPackets_Type()
)
tmnxVdoSessionTxFCCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxFCCPackets.setStatus("current")
_TmnxVdoSessionTxFCCOctets_Type = Counter32
_TmnxVdoSessionTxFCCOctets_Object = MibTableColumn
tmnxVdoSessionTxFCCOctets = _TmnxVdoSessionTxFCCOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 13),
    _TmnxVdoSessionTxFCCOctets_Type()
)
tmnxVdoSessionTxFCCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxFCCOctets.setStatus("current")
_TmnxVdoSessionTxFCCFailedPackets_Type = Counter32
_TmnxVdoSessionTxFCCFailedPackets_Object = MibTableColumn
tmnxVdoSessionTxFCCFailedPackets = _TmnxVdoSessionTxFCCFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 14),
    _TmnxVdoSessionTxFCCFailedPackets_Type()
)
tmnxVdoSessionTxFCCFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxFCCFailedPackets.setStatus("current")
_TmnxVdoSessionRxRTRequests_Type = Counter32
_TmnxVdoSessionRxRTRequests_Object = MibTableColumn
tmnxVdoSessionRxRTRequests = _TmnxVdoSessionRxRTRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 15),
    _TmnxVdoSessionRxRTRequests_Type()
)
tmnxVdoSessionRxRTRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionRxRTRequests.setStatus("current")
_TmnxVdoSessionTxRTReplies_Type = Counter32
_TmnxVdoSessionTxRTReplies_Object = MibTableColumn
tmnxVdoSessionTxRTReplies = _TmnxVdoSessionTxRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 16),
    _TmnxVdoSessionTxRTReplies_Type()
)
tmnxVdoSessionTxRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxRTReplies.setStatus("current")
_TmnxVdoSessionTxRTPackets_Type = Counter32
_TmnxVdoSessionTxRTPackets_Object = MibTableColumn
tmnxVdoSessionTxRTPackets = _TmnxVdoSessionTxRTPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 17),
    _TmnxVdoSessionTxRTPackets_Type()
)
tmnxVdoSessionTxRTPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxRTPackets.setStatus("current")
_TmnxVdoSessionTxRTOctets_Type = Counter32
_TmnxVdoSessionTxRTOctets_Object = MibTableColumn
tmnxVdoSessionTxRTOctets = _TmnxVdoSessionTxRTOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 18),
    _TmnxVdoSessionTxRTOctets_Type()
)
tmnxVdoSessionTxRTOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxRTOctets.setStatus("current")
_TmnxVdoSessionTxRTFailedPackets_Type = Counter32
_TmnxVdoSessionTxRTFailedPackets_Object = MibTableColumn
tmnxVdoSessionTxRTFailedPackets = _TmnxVdoSessionTxRTFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 19),
    _TmnxVdoSessionTxRTFailedPackets_Type()
)
tmnxVdoSessionTxRTFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionTxRTFailedPackets.setStatus("current")
_TmnxVdoSessionRequestedRtpPkts_Type = Counter32
_TmnxVdoSessionRequestedRtpPkts_Object = MibTableColumn
tmnxVdoSessionRequestedRtpPkts = _TmnxVdoSessionRequestedRtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 20),
    _TmnxVdoSessionRequestedRtpPkts_Type()
)
tmnxVdoSessionRequestedRtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionRequestedRtpPkts.setStatus("current")
_TmnxVdoSessionRTReqQuenched_Type = Counter32
_TmnxVdoSessionRTReqQuenched_Object = MibTableColumn
tmnxVdoSessionRTReqQuenched = _TmnxVdoSessionRTReqQuenched_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 21),
    _TmnxVdoSessionRTReqQuenched_Type()
)
tmnxVdoSessionRTReqQuenched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionRTReqQuenched.setStatus("current")
_TmnxVdoSessionRTMcastReqCreated_Type = Counter32
_TmnxVdoSessionRTMcastReqCreated_Object = MibTableColumn
tmnxVdoSessionRTMcastReqCreated = _TmnxVdoSessionRTMcastReqCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 22),
    _TmnxVdoSessionRTMcastReqCreated_Type()
)
tmnxVdoSessionRTMcastReqCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionRTMcastReqCreated.setStatus("current")
_TmnxVdoSessionPktsLostInSeq10_Type = Counter32
_TmnxVdoSessionPktsLostInSeq10_Object = MibTableColumn
tmnxVdoSessionPktsLostInSeq10 = _TmnxVdoSessionPktsLostInSeq10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 23),
    _TmnxVdoSessionPktsLostInSeq10_Type()
)
tmnxVdoSessionPktsLostInSeq10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionPktsLostInSeq10.setStatus("current")
_TmnxVdoSessionPktsLostInSeq20_Type = Counter32
_TmnxVdoSessionPktsLostInSeq20_Object = MibTableColumn
tmnxVdoSessionPktsLostInSeq20 = _TmnxVdoSessionPktsLostInSeq20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 24),
    _TmnxVdoSessionPktsLostInSeq20_Type()
)
tmnxVdoSessionPktsLostInSeq20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionPktsLostInSeq20.setStatus("current")
_TmnxVdoSessionPktsLostInSeq30_Type = Counter32
_TmnxVdoSessionPktsLostInSeq30_Object = MibTableColumn
tmnxVdoSessionPktsLostInSeq30 = _TmnxVdoSessionPktsLostInSeq30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 25),
    _TmnxVdoSessionPktsLostInSeq30_Type()
)
tmnxVdoSessionPktsLostInSeq30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionPktsLostInSeq30.setStatus("current")
_TmnxVdoSessionPktsLostInSeq40_Type = Counter32
_TmnxVdoSessionPktsLostInSeq40_Object = MibTableColumn
tmnxVdoSessionPktsLostInSeq40 = _TmnxVdoSessionPktsLostInSeq40_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 26),
    _TmnxVdoSessionPktsLostInSeq40_Type()
)
tmnxVdoSessionPktsLostInSeq40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionPktsLostInSeq40.setStatus("current")
_TmnxVdoSessionPktsLostInSeqMore_Type = Counter32
_TmnxVdoSessionPktsLostInSeqMore_Object = MibTableColumn
tmnxVdoSessionPktsLostInSeqMore = _TmnxVdoSessionPktsLostInSeqMore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 9, 1, 27),
    _TmnxVdoSessionPktsLostInSeqMore_Type()
)
tmnxVdoSessionPktsLostInSeqMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSessionPktsLostInSeqMore.setStatus("current")
_TmnxVdoIfStatTable_Object = MibTable
tmnxVdoIfStatTable = _TmnxVdoIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStatTable.setStatus("current")
_TmnxVdoIfStatEntry_Object = MibTableRow
tmnxVdoIfStatEntry = _TmnxVdoIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStatEntry.setStatus("current")
_TmnxVdoIfStatHdRTServerState_Type = TruthValue
_TmnxVdoIfStatHdRTServerState_Object = MibTableColumn
tmnxVdoIfStatHdRTServerState = _TmnxVdoIfStatHdRTServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 1),
    _TmnxVdoIfStatHdRTServerState_Type()
)
tmnxVdoIfStatHdRTServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHdRTServerState.setStatus("current")
_TmnxVdoIfStatSdRTServerState_Type = TruthValue
_TmnxVdoIfStatSdRTServerState_Object = MibTableColumn
tmnxVdoIfStatSdRTServerState = _TmnxVdoIfStatSdRTServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 2),
    _TmnxVdoIfStatSdRTServerState_Type()
)
tmnxVdoIfStatSdRTServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSdRTServerState.setStatus("current")
_TmnxVdoIfStatPipRTServerState_Type = TruthValue
_TmnxVdoIfStatPipRTServerState_Object = MibTableColumn
tmnxVdoIfStatPipRTServerState = _TmnxVdoIfStatPipRTServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 3),
    _TmnxVdoIfStatPipRTServerState_Type()
)
tmnxVdoIfStatPipRTServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipRTServerState.setStatus("current")
_TmnxVdoIfStatRTSvrSdRtpPktsReq_Type = Counter64
_TmnxVdoIfStatRTSvrSdRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrSdRtpPktsReq = _TmnxVdoIfStatRTSvrSdRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 4),
    _TmnxVdoIfStatRTSvrSdRtpPktsReq_Type()
)
tmnxVdoIfStatRTSvrSdRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrSdRtpPktsReq.setStatus("current")
_TmnxVdoIfStatRTSvrHdRtpPktsReq_Type = Counter64
_TmnxVdoIfStatRTSvrHdRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrHdRtpPktsReq = _TmnxVdoIfStatRTSvrHdRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 5),
    _TmnxVdoIfStatRTSvrHdRtpPktsReq_Type()
)
tmnxVdoIfStatRTSvrHdRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrHdRtpPktsReq.setStatus("current")
_TmnxVdoIfStatRTSvrPipRtpPktsReq_Type = Counter64
_TmnxVdoIfStatRTSvrPipRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrPipRtpPktsReq = _TmnxVdoIfStatRTSvrPipRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 6),
    _TmnxVdoIfStatRTSvrPipRtpPktsReq_Type()
)
tmnxVdoIfStatRTSvrPipRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrPipRtpPktsReq.setStatus("current")
_TmnxVdoIfStatRTSvrRxSdRTReq_Type = Counter64
_TmnxVdoIfStatRTSvrRxSdRTReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrRxSdRTReq = _TmnxVdoIfStatRTSvrRxSdRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 7),
    _TmnxVdoIfStatRTSvrRxSdRTReq_Type()
)
tmnxVdoIfStatRTSvrRxSdRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrRxSdRTReq.setStatus("current")
_TmnxVdoIfStatRTSvrRxSdFailedReq_Type = Counter64
_TmnxVdoIfStatRTSvrRxSdFailedReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrRxSdFailedReq = _TmnxVdoIfStatRTSvrRxSdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 8),
    _TmnxVdoIfStatRTSvrRxSdFailedReq_Type()
)
tmnxVdoIfStatRTSvrRxSdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrRxSdFailedReq.setStatus("current")
_TmnxVdoIfStatRTSvrRxHdRTReq_Type = Counter64
_TmnxVdoIfStatRTSvrRxHdRTReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrRxHdRTReq = _TmnxVdoIfStatRTSvrRxHdRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 9),
    _TmnxVdoIfStatRTSvrRxHdRTReq_Type()
)
tmnxVdoIfStatRTSvrRxHdRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrRxHdRTReq.setStatus("current")
_TmnxVdoIfStatRTSvrRxHdFailedReq_Type = Counter64
_TmnxVdoIfStatRTSvrRxHdFailedReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrRxHdFailedReq = _TmnxVdoIfStatRTSvrRxHdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 10),
    _TmnxVdoIfStatRTSvrRxHdFailedReq_Type()
)
tmnxVdoIfStatRTSvrRxHdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrRxHdFailedReq.setStatus("current")
_TmnxVdoIfStatRTSvrRxPipRTReq_Type = Counter64
_TmnxVdoIfStatRTSvrRxPipRTReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrRxPipRTReq = _TmnxVdoIfStatRTSvrRxPipRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 11),
    _TmnxVdoIfStatRTSvrRxPipRTReq_Type()
)
tmnxVdoIfStatRTSvrRxPipRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrRxPipRTReq.setStatus("current")
_TmnxVdoIfStatRTSvrRxPipFailedReq_Type = Counter64
_TmnxVdoIfStatRTSvrRxPipFailedReq_Object = MibTableColumn
tmnxVdoIfStatRTSvrRxPipFailedReq = _TmnxVdoIfStatRTSvrRxPipFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 12),
    _TmnxVdoIfStatRTSvrRxPipFailedReq_Type()
)
tmnxVdoIfStatRTSvrRxPipFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrRxPipFailedReq.setStatus("current")
_TmnxVdoIfStatRTSvrTxSdRTReplies_Type = Counter64
_TmnxVdoIfStatRTSvrTxSdRTReplies_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxSdRTReplies = _TmnxVdoIfStatRTSvrTxSdRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 13),
    _TmnxVdoIfStatRTSvrTxSdRTReplies_Type()
)
tmnxVdoIfStatRTSvrTxSdRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxSdRTReplies.setStatus("current")
_TmnxVdoIfStatRTSvrTxSdBytes_Type = Counter64
_TmnxVdoIfStatRTSvrTxSdBytes_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxSdBytes = _TmnxVdoIfStatRTSvrTxSdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 14),
    _TmnxVdoIfStatRTSvrTxSdBytes_Type()
)
tmnxVdoIfStatRTSvrTxSdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxSdBytes.setStatus("current")
_TmnxVdoIfStatRTSvrTxSdPackets_Type = Counter64
_TmnxVdoIfStatRTSvrTxSdPackets_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxSdPackets = _TmnxVdoIfStatRTSvrTxSdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 15),
    _TmnxVdoIfStatRTSvrTxSdPackets_Type()
)
tmnxVdoIfStatRTSvrTxSdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxSdPackets.setStatus("current")
_TmnxVdoIfStatRTSvrTxHdRTReplies_Type = Counter64
_TmnxVdoIfStatRTSvrTxHdRTReplies_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxHdRTReplies = _TmnxVdoIfStatRTSvrTxHdRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 16),
    _TmnxVdoIfStatRTSvrTxHdRTReplies_Type()
)
tmnxVdoIfStatRTSvrTxHdRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxHdRTReplies.setStatus("current")
_TmnxVdoIfStatRTSvrTxHdBytes_Type = Counter64
_TmnxVdoIfStatRTSvrTxHdBytes_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxHdBytes = _TmnxVdoIfStatRTSvrTxHdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 17),
    _TmnxVdoIfStatRTSvrTxHdBytes_Type()
)
tmnxVdoIfStatRTSvrTxHdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxHdBytes.setStatus("current")
_TmnxVdoIfStatRTSvrTxHdPackets_Type = Counter64
_TmnxVdoIfStatRTSvrTxHdPackets_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxHdPackets = _TmnxVdoIfStatRTSvrTxHdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 18),
    _TmnxVdoIfStatRTSvrTxHdPackets_Type()
)
tmnxVdoIfStatRTSvrTxHdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxHdPackets.setStatus("current")
_TmnxVdoIfStatRTSvrTxPipRTReplies_Type = Counter64
_TmnxVdoIfStatRTSvrTxPipRTReplies_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxPipRTReplies = _TmnxVdoIfStatRTSvrTxPipRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 19),
    _TmnxVdoIfStatRTSvrTxPipRTReplies_Type()
)
tmnxVdoIfStatRTSvrTxPipRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxPipRTReplies.setStatus("current")
_TmnxVdoIfStatRTSvrTxPipBytes_Type = Counter64
_TmnxVdoIfStatRTSvrTxPipBytes_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxPipBytes = _TmnxVdoIfStatRTSvrTxPipBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 20),
    _TmnxVdoIfStatRTSvrTxPipBytes_Type()
)
tmnxVdoIfStatRTSvrTxPipBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxPipBytes.setStatus("current")
_TmnxVdoIfStatRTSvrTxPipPackets_Type = Counter64
_TmnxVdoIfStatRTSvrTxPipPackets_Object = MibTableColumn
tmnxVdoIfStatRTSvrTxPipPackets = _TmnxVdoIfStatRTSvrTxPipPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 21),
    _TmnxVdoIfStatRTSvrTxPipPackets_Type()
)
tmnxVdoIfStatRTSvrTxPipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSvrTxPipPackets.setStatus("current")
_TmnxVdoIfStatHdFCCServerMode_Type = TmnxVdoFccServerMode
_TmnxVdoIfStatHdFCCServerMode_Object = MibTableColumn
tmnxVdoIfStatHdFCCServerMode = _TmnxVdoIfStatHdFCCServerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 22),
    _TmnxVdoIfStatHdFCCServerMode_Type()
)
tmnxVdoIfStatHdFCCServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHdFCCServerMode.setStatus("current")
_TmnxVdoIfStatSdFCCServerMode_Type = TmnxVdoFccServerMode
_TmnxVdoIfStatSdFCCServerMode_Object = MibTableColumn
tmnxVdoIfStatSdFCCServerMode = _TmnxVdoIfStatSdFCCServerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 23),
    _TmnxVdoIfStatSdFCCServerMode_Type()
)
tmnxVdoIfStatSdFCCServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSdFCCServerMode.setStatus("current")
_TmnxVdoIfStatPipFCCServerMode_Type = TmnxVdoFccServerMode
_TmnxVdoIfStatPipFCCServerMode_Object = MibTableColumn
tmnxVdoIfStatPipFCCServerMode = _TmnxVdoIfStatPipFCCServerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 24),
    _TmnxVdoIfStatPipFCCServerMode_Type()
)
tmnxVdoIfStatPipFCCServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipFCCServerMode.setStatus("current")
_TmnxVdoIfStatFCCSrRxSdFCCReq_Type = Counter64
_TmnxVdoIfStatFCCSrRxSdFCCReq_Object = MibTableColumn
tmnxVdoIfStatFCCSrRxSdFCCReq = _TmnxVdoIfStatFCCSrRxSdFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 25),
    _TmnxVdoIfStatFCCSrRxSdFCCReq_Type()
)
tmnxVdoIfStatFCCSrRxSdFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrRxSdFCCReq.setStatus("current")
_TmnxVdoIfStatFCCSrRxSdFailedReq_Type = Counter64
_TmnxVdoIfStatFCCSrRxSdFailedReq_Object = MibTableColumn
tmnxVdoIfStatFCCSrRxSdFailedReq = _TmnxVdoIfStatFCCSrRxSdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 26),
    _TmnxVdoIfStatFCCSrRxSdFailedReq_Type()
)
tmnxVdoIfStatFCCSrRxSdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrRxSdFailedReq.setStatus("current")
_TmnxVdoIfStatFCCSrRxHdFCCReq_Type = Counter64
_TmnxVdoIfStatFCCSrRxHdFCCReq_Object = MibTableColumn
tmnxVdoIfStatFCCSrRxHdFCCReq = _TmnxVdoIfStatFCCSrRxHdFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 27),
    _TmnxVdoIfStatFCCSrRxHdFCCReq_Type()
)
tmnxVdoIfStatFCCSrRxHdFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrRxHdFCCReq.setStatus("current")
_TmnxVdoIfStatFCCSrRxHdFailedReq_Type = Counter64
_TmnxVdoIfStatFCCSrRxHdFailedReq_Object = MibTableColumn
tmnxVdoIfStatFCCSrRxHdFailedReq = _TmnxVdoIfStatFCCSrRxHdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 28),
    _TmnxVdoIfStatFCCSrRxHdFailedReq_Type()
)
tmnxVdoIfStatFCCSrRxHdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrRxHdFailedReq.setStatus("current")
_TmnxVdoIfStatFCCSrRxPipFCCReq_Type = Counter64
_TmnxVdoIfStatFCCSrRxPipFCCReq_Object = MibTableColumn
tmnxVdoIfStatFCCSrRxPipFCCReq = _TmnxVdoIfStatFCCSrRxPipFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 29),
    _TmnxVdoIfStatFCCSrRxPipFCCReq_Type()
)
tmnxVdoIfStatFCCSrRxPipFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrRxPipFCCReq.setStatus("current")
_TmnxVdoIfStatFCCSrRxPipFailedReq_Type = Counter64
_TmnxVdoIfStatFCCSrRxPipFailedReq_Object = MibTableColumn
tmnxVdoIfStatFCCSrRxPipFailedReq = _TmnxVdoIfStatFCCSrRxPipFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 30),
    _TmnxVdoIfStatFCCSrRxPipFailedReq_Type()
)
tmnxVdoIfStatFCCSrRxPipFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrRxPipFailedReq.setStatus("current")
_TmnxVdoIfStatFCCSrTxSdFCCReplies_Type = Counter64
_TmnxVdoIfStatFCCSrTxSdFCCReplies_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxSdFCCReplies = _TmnxVdoIfStatFCCSrTxSdFCCReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 31),
    _TmnxVdoIfStatFCCSrTxSdFCCReplies_Type()
)
tmnxVdoIfStatFCCSrTxSdFCCReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxSdFCCReplies.setStatus("current")
_TmnxVdoIfStatFCCSrTxSdBytes_Type = Counter64
_TmnxVdoIfStatFCCSrTxSdBytes_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxSdBytes = _TmnxVdoIfStatFCCSrTxSdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 32),
    _TmnxVdoIfStatFCCSrTxSdBytes_Type()
)
tmnxVdoIfStatFCCSrTxSdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxSdBytes.setStatus("current")
_TmnxVdoIfStatFCCSrTxSdPackets_Type = Counter64
_TmnxVdoIfStatFCCSrTxSdPackets_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxSdPackets = _TmnxVdoIfStatFCCSrTxSdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 33),
    _TmnxVdoIfStatFCCSrTxSdPackets_Type()
)
tmnxVdoIfStatFCCSrTxSdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxSdPackets.setStatus("current")
_TmnxVdoIfStatFCCSrTxHdFCCReplies_Type = Counter64
_TmnxVdoIfStatFCCSrTxHdFCCReplies_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxHdFCCReplies = _TmnxVdoIfStatFCCSrTxHdFCCReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 34),
    _TmnxVdoIfStatFCCSrTxHdFCCReplies_Type()
)
tmnxVdoIfStatFCCSrTxHdFCCReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxHdFCCReplies.setStatus("current")
_TmnxVdoIfStatFCCSrTxHdBytes_Type = Counter64
_TmnxVdoIfStatFCCSrTxHdBytes_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxHdBytes = _TmnxVdoIfStatFCCSrTxHdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 35),
    _TmnxVdoIfStatFCCSrTxHdBytes_Type()
)
tmnxVdoIfStatFCCSrTxHdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxHdBytes.setStatus("current")
_TmnxVdoIfStatFCCSrTxHdPackets_Type = Counter64
_TmnxVdoIfStatFCCSrTxHdPackets_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxHdPackets = _TmnxVdoIfStatFCCSrTxHdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 36),
    _TmnxVdoIfStatFCCSrTxHdPackets_Type()
)
tmnxVdoIfStatFCCSrTxHdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxHdPackets.setStatus("current")
_TmnxVdoIfStatFCCSrTxPipFCCRplies_Type = Counter64
_TmnxVdoIfStatFCCSrTxPipFCCRplies_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxPipFCCRplies = _TmnxVdoIfStatFCCSrTxPipFCCRplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 37),
    _TmnxVdoIfStatFCCSrTxPipFCCRplies_Type()
)
tmnxVdoIfStatFCCSrTxPipFCCRplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxPipFCCRplies.setStatus("current")
_TmnxVdoIfStatFCCSrTxPipBytes_Type = Counter64
_TmnxVdoIfStatFCCSrTxPipBytes_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxPipBytes = _TmnxVdoIfStatFCCSrTxPipBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 38),
    _TmnxVdoIfStatFCCSrTxPipBytes_Type()
)
tmnxVdoIfStatFCCSrTxPipBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxPipBytes.setStatus("current")
_TmnxVdoIfStatFCCSrTxPipPackets_Type = Counter64
_TmnxVdoIfStatFCCSrTxPipPackets_Object = MibTableColumn
tmnxVdoIfStatFCCSrTxPipPackets = _TmnxVdoIfStatFCCSrTxPipPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 39),
    _TmnxVdoIfStatFCCSrTxPipPackets_Type()
)
tmnxVdoIfStatFCCSrTxPipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatFCCSrTxPipPackets.setStatus("current")
_TmnxVdoIfStatTxFailedPackets_Type = Counter64
_TmnxVdoIfStatTxFailedPackets_Object = MibTableColumn
tmnxVdoIfStatTxFailedPackets = _TmnxVdoIfStatTxFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 40),
    _TmnxVdoIfStatTxFailedPackets_Type()
)
tmnxVdoIfStatTxFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatTxFailedPackets.setStatus("current")
_TmnxVdoIfScte30TcpSessions_Type = Counter32
_TmnxVdoIfScte30TcpSessions_Object = MibTableColumn
tmnxVdoIfScte30TcpSessions = _TmnxVdoIfScte30TcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 41),
    _TmnxVdoIfScte30TcpSessions_Type()
)
tmnxVdoIfScte30TcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30TcpSessions.setStatus("current")
_TmnxVdoIfScte30InitSessions_Type = Counter32
_TmnxVdoIfScte30InitSessions_Object = MibTableColumn
tmnxVdoIfScte30InitSessions = _TmnxVdoIfScte30InitSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 42),
    _TmnxVdoIfScte30InitSessions_Type()
)
tmnxVdoIfScte30InitSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30InitSessions.setStatus("current")
_TmnxVdoIfStatRTSSdMcRdPktsReq_Type = Counter64
_TmnxVdoIfStatRTSSdMcRdPktsReq_Object = MibTableColumn
tmnxVdoIfStatRTSSdMcRdPktsReq = _TmnxVdoIfStatRTSSdMcRdPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 43),
    _TmnxVdoIfStatRTSSdMcRdPktsReq_Type()
)
tmnxVdoIfStatRTSSdMcRdPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSSdMcRdPktsReq.setStatus("current")
_TmnxVdoIfStatRTSSdMcRdPktsReqL32_Type = Counter32
_TmnxVdoIfStatRTSSdMcRdPktsReqL32_Object = MibTableColumn
tmnxVdoIfStatRTSSdMcRdPktsReqL32 = _TmnxVdoIfStatRTSSdMcRdPktsReqL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 44),
    _TmnxVdoIfStatRTSSdMcRdPktsReqL32_Type()
)
tmnxVdoIfStatRTSSdMcRdPktsReqL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSSdMcRdPktsReqL32.setStatus("current")
_TmnxVdoIfStatRTSSdMcRdPktsReqH32_Type = Counter32
_TmnxVdoIfStatRTSSdMcRdPktsReqH32_Object = MibTableColumn
tmnxVdoIfStatRTSSdMcRdPktsReqH32 = _TmnxVdoIfStatRTSSdMcRdPktsReqH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 45),
    _TmnxVdoIfStatRTSSdMcRdPktsReqH32_Type()
)
tmnxVdoIfStatRTSSdMcRdPktsReqH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSSdMcRdPktsReqH32.setStatus("current")
_TmnxVdoIfStatRTSHDMcRdPktsReq_Type = Counter64
_TmnxVdoIfStatRTSHDMcRdPktsReq_Object = MibTableColumn
tmnxVdoIfStatRTSHDMcRdPktsReq = _TmnxVdoIfStatRTSHDMcRdPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 46),
    _TmnxVdoIfStatRTSHDMcRdPktsReq_Type()
)
tmnxVdoIfStatRTSHDMcRdPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSHDMcRdPktsReq.setStatus("current")
_TmnxVdoIfStatRTSHDMcRdPktsReqL32_Type = Counter32
_TmnxVdoIfStatRTSHDMcRdPktsReqL32_Object = MibTableColumn
tmnxVdoIfStatRTSHDMcRdPktsReqL32 = _TmnxVdoIfStatRTSHDMcRdPktsReqL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 47),
    _TmnxVdoIfStatRTSHDMcRdPktsReqL32_Type()
)
tmnxVdoIfStatRTSHDMcRdPktsReqL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSHDMcRdPktsReqL32.setStatus("current")
_TmnxVdoIfStatRTSHDMcRdPktsReqH32_Type = Counter32
_TmnxVdoIfStatRTSHDMcRdPktsReqH32_Object = MibTableColumn
tmnxVdoIfStatRTSHDMcRdPktsReqH32 = _TmnxVdoIfStatRTSHDMcRdPktsReqH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 48),
    _TmnxVdoIfStatRTSHDMcRdPktsReqH32_Type()
)
tmnxVdoIfStatRTSHDMcRdPktsReqH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSHDMcRdPktsReqH32.setStatus("current")
_TmnxVdoIfStatRTSPipMcRdPktReq_Type = Counter64
_TmnxVdoIfStatRTSPipMcRdPktReq_Object = MibTableColumn
tmnxVdoIfStatRTSPipMcRdPktReq = _TmnxVdoIfStatRTSPipMcRdPktReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 49),
    _TmnxVdoIfStatRTSPipMcRdPktReq_Type()
)
tmnxVdoIfStatRTSPipMcRdPktReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSPipMcRdPktReq.setStatus("current")
_TmnxVdoIfStatRTSPipMcRdPktReqL32_Type = Counter32
_TmnxVdoIfStatRTSPipMcRdPktReqL32_Object = MibTableColumn
tmnxVdoIfStatRTSPipMcRdPktReqL32 = _TmnxVdoIfStatRTSPipMcRdPktReqL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 50),
    _TmnxVdoIfStatRTSPipMcRdPktReqL32_Type()
)
tmnxVdoIfStatRTSPipMcRdPktReqL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSPipMcRdPktReqL32.setStatus("current")
_TmnxVdoIfStatRTSPipMcRdPktReqH32_Type = Counter32
_TmnxVdoIfStatRTSPipMcRdPktReqH32_Object = MibTableColumn
tmnxVdoIfStatRTSPipMcRdPktReqH32 = _TmnxVdoIfStatRTSPipMcRdPktReqH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 51),
    _TmnxVdoIfStatRTSPipMcRdPktReqH32_Type()
)
tmnxVdoIfStatRTSPipMcRdPktReqH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatRTSPipMcRdPktReqH32.setStatus("current")
_TmnxVdoIfStatSDPktLostInSeq10_Type = Counter32
_TmnxVdoIfStatSDPktLostInSeq10_Object = MibTableColumn
tmnxVdoIfStatSDPktLostInSeq10 = _TmnxVdoIfStatSDPktLostInSeq10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 52),
    _TmnxVdoIfStatSDPktLostInSeq10_Type()
)
tmnxVdoIfStatSDPktLostInSeq10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSDPktLostInSeq10.setStatus("current")
_TmnxVdoIfStatSDPktLostInSeq20_Type = Counter32
_TmnxVdoIfStatSDPktLostInSeq20_Object = MibTableColumn
tmnxVdoIfStatSDPktLostInSeq20 = _TmnxVdoIfStatSDPktLostInSeq20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 53),
    _TmnxVdoIfStatSDPktLostInSeq20_Type()
)
tmnxVdoIfStatSDPktLostInSeq20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSDPktLostInSeq20.setStatus("current")
_TmnxVdoIfStatSDPktLostInSeq30_Type = Counter32
_TmnxVdoIfStatSDPktLostInSeq30_Object = MibTableColumn
tmnxVdoIfStatSDPktLostInSeq30 = _TmnxVdoIfStatSDPktLostInSeq30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 54),
    _TmnxVdoIfStatSDPktLostInSeq30_Type()
)
tmnxVdoIfStatSDPktLostInSeq30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSDPktLostInSeq30.setStatus("current")
_TmnxVdoIfStatSDPktLostInSeq40_Type = Counter32
_TmnxVdoIfStatSDPktLostInSeq40_Object = MibTableColumn
tmnxVdoIfStatSDPktLostInSeq40 = _TmnxVdoIfStatSDPktLostInSeq40_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 55),
    _TmnxVdoIfStatSDPktLostInSeq40_Type()
)
tmnxVdoIfStatSDPktLostInSeq40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSDPktLostInSeq40.setStatus("current")
_TmnxVdoIfStatSDPktLostInSeqMore_Type = Counter32
_TmnxVdoIfStatSDPktLostInSeqMore_Object = MibTableColumn
tmnxVdoIfStatSDPktLostInSeqMore = _TmnxVdoIfStatSDPktLostInSeqMore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 56),
    _TmnxVdoIfStatSDPktLostInSeqMore_Type()
)
tmnxVdoIfStatSDPktLostInSeqMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatSDPktLostInSeqMore.setStatus("current")
_TmnxVdoIfStatHDPktLostInSeq10_Type = Counter32
_TmnxVdoIfStatHDPktLostInSeq10_Object = MibTableColumn
tmnxVdoIfStatHDPktLostInSeq10 = _TmnxVdoIfStatHDPktLostInSeq10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 57),
    _TmnxVdoIfStatHDPktLostInSeq10_Type()
)
tmnxVdoIfStatHDPktLostInSeq10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHDPktLostInSeq10.setStatus("current")
_TmnxVdoIfStatHDPktLostInSeq20_Type = Counter32
_TmnxVdoIfStatHDPktLostInSeq20_Object = MibTableColumn
tmnxVdoIfStatHDPktLostInSeq20 = _TmnxVdoIfStatHDPktLostInSeq20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 58),
    _TmnxVdoIfStatHDPktLostInSeq20_Type()
)
tmnxVdoIfStatHDPktLostInSeq20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHDPktLostInSeq20.setStatus("current")
_TmnxVdoIfStatHDPktLostInSeq30_Type = Counter32
_TmnxVdoIfStatHDPktLostInSeq30_Object = MibTableColumn
tmnxVdoIfStatHDPktLostInSeq30 = _TmnxVdoIfStatHDPktLostInSeq30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 59),
    _TmnxVdoIfStatHDPktLostInSeq30_Type()
)
tmnxVdoIfStatHDPktLostInSeq30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHDPktLostInSeq30.setStatus("current")
_TmnxVdoIfStatHDPktLostInSeq40_Type = Counter32
_TmnxVdoIfStatHDPktLostInSeq40_Object = MibTableColumn
tmnxVdoIfStatHDPktLostInSeq40 = _TmnxVdoIfStatHDPktLostInSeq40_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 60),
    _TmnxVdoIfStatHDPktLostInSeq40_Type()
)
tmnxVdoIfStatHDPktLostInSeq40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHDPktLostInSeq40.setStatus("current")
_TmnxVdoIfStatHDPktLostInSeqMore_Type = Counter32
_TmnxVdoIfStatHDPktLostInSeqMore_Object = MibTableColumn
tmnxVdoIfStatHDPktLostInSeqMore = _TmnxVdoIfStatHDPktLostInSeqMore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 61),
    _TmnxVdoIfStatHDPktLostInSeqMore_Type()
)
tmnxVdoIfStatHDPktLostInSeqMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatHDPktLostInSeqMore.setStatus("current")
_TmnxVdoIfStatPipPktLostInSeq10_Type = Counter32
_TmnxVdoIfStatPipPktLostInSeq10_Object = MibTableColumn
tmnxVdoIfStatPipPktLostInSeq10 = _TmnxVdoIfStatPipPktLostInSeq10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 62),
    _TmnxVdoIfStatPipPktLostInSeq10_Type()
)
tmnxVdoIfStatPipPktLostInSeq10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipPktLostInSeq10.setStatus("current")
_TmnxVdoIfStatPipPktLostInSeq20_Type = Counter32
_TmnxVdoIfStatPipPktLostInSeq20_Object = MibTableColumn
tmnxVdoIfStatPipPktLostInSeq20 = _TmnxVdoIfStatPipPktLostInSeq20_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 63),
    _TmnxVdoIfStatPipPktLostInSeq20_Type()
)
tmnxVdoIfStatPipPktLostInSeq20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipPktLostInSeq20.setStatus("current")
_TmnxVdoIfStatPipPktLostInSeq30_Type = Counter32
_TmnxVdoIfStatPipPktLostInSeq30_Object = MibTableColumn
tmnxVdoIfStatPipPktLostInSeq30 = _TmnxVdoIfStatPipPktLostInSeq30_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 64),
    _TmnxVdoIfStatPipPktLostInSeq30_Type()
)
tmnxVdoIfStatPipPktLostInSeq30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipPktLostInSeq30.setStatus("current")
_TmnxVdoIfStatPipPktLostInSeq40_Type = Counter32
_TmnxVdoIfStatPipPktLostInSeq40_Object = MibTableColumn
tmnxVdoIfStatPipPktLostInSeq40 = _TmnxVdoIfStatPipPktLostInSeq40_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 65),
    _TmnxVdoIfStatPipPktLostInSeq40_Type()
)
tmnxVdoIfStatPipPktLostInSeq40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipPktLostInSeq40.setStatus("current")
_TmnxVdoIfStatPipPktLostInSeqMore_Type = Counter32
_TmnxVdoIfStatPipPktLostInSeqMore_Object = MibTableColumn
tmnxVdoIfStatPipPktLostInSeqMore = _TmnxVdoIfStatPipPktLostInSeqMore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 10, 1, 66),
    _TmnxVdoIfStatPipPktLostInSeqMore_Type()
)
tmnxVdoIfStatPipPktLostInSeqMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatPipPktLostInSeqMore.setStatus("current")
_TmnxVdoIfStLowTable_Object = MibTable
tmnxVdoIfStLowTable = _TmnxVdoIfStLowTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStLowTable.setStatus("current")
_TmnxVdoIfStLowEntry_Object = MibTableRow
tmnxVdoIfStLowEntry = _TmnxVdoIfStLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStLowEntry.setStatus("current")
_TmnxVdoIfStLowRTSvrSdRtpPktsReq_Type = Counter32
_TmnxVdoIfStLowRTSvrSdRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrSdRtpPktsReq = _TmnxVdoIfStLowRTSvrSdRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 1),
    _TmnxVdoIfStLowRTSvrSdRtpPktsReq_Type()
)
tmnxVdoIfStLowRTSvrSdRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrSdRtpPktsReq.setStatus("current")
_TmnxVdoIfStLowRTSvrHdRtpPktsReq_Type = Counter32
_TmnxVdoIfStLowRTSvrHdRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrHdRtpPktsReq = _TmnxVdoIfStLowRTSvrHdRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 2),
    _TmnxVdoIfStLowRTSvrHdRtpPktsReq_Type()
)
tmnxVdoIfStLowRTSvrHdRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrHdRtpPktsReq.setStatus("current")
_TmnxVdoIfStLowRTSvrPipRtpPktsReq_Type = Counter32
_TmnxVdoIfStLowRTSvrPipRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrPipRtpPktsReq = _TmnxVdoIfStLowRTSvrPipRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 3),
    _TmnxVdoIfStLowRTSvrPipRtpPktsReq_Type()
)
tmnxVdoIfStLowRTSvrPipRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrPipRtpPktsReq.setStatus("current")
_TmnxVdoIfStLowRTSvrRxSdRTReq_Type = Counter32
_TmnxVdoIfStLowRTSvrRxSdRTReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrRxSdRTReq = _TmnxVdoIfStLowRTSvrRxSdRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 4),
    _TmnxVdoIfStLowRTSvrRxSdRTReq_Type()
)
tmnxVdoIfStLowRTSvrRxSdRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrRxSdRTReq.setStatus("current")
_TmnxVdoIfStLowRTSvrRxSdFailedReq_Type = Counter32
_TmnxVdoIfStLowRTSvrRxSdFailedReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrRxSdFailedReq = _TmnxVdoIfStLowRTSvrRxSdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 5),
    _TmnxVdoIfStLowRTSvrRxSdFailedReq_Type()
)
tmnxVdoIfStLowRTSvrRxSdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrRxSdFailedReq.setStatus("current")
_TmnxVdoIfStLowRTSvrRxHdRTReq_Type = Counter32
_TmnxVdoIfStLowRTSvrRxHdRTReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrRxHdRTReq = _TmnxVdoIfStLowRTSvrRxHdRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 6),
    _TmnxVdoIfStLowRTSvrRxHdRTReq_Type()
)
tmnxVdoIfStLowRTSvrRxHdRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrRxHdRTReq.setStatus("current")
_TmnxVdoIfStLowRTSvrRxHdFailedReq_Type = Counter32
_TmnxVdoIfStLowRTSvrRxHdFailedReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrRxHdFailedReq = _TmnxVdoIfStLowRTSvrRxHdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 7),
    _TmnxVdoIfStLowRTSvrRxHdFailedReq_Type()
)
tmnxVdoIfStLowRTSvrRxHdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrRxHdFailedReq.setStatus("current")
_TmnxVdoIfStLowRTSvrRxPipRTReq_Type = Counter32
_TmnxVdoIfStLowRTSvrRxPipRTReq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrRxPipRTReq = _TmnxVdoIfStLowRTSvrRxPipRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 8),
    _TmnxVdoIfStLowRTSvrRxPipRTReq_Type()
)
tmnxVdoIfStLowRTSvrRxPipRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrRxPipRTReq.setStatus("current")
_TmnxVdoIfStLowRTSvrRxPipFailedRq_Type = Counter32
_TmnxVdoIfStLowRTSvrRxPipFailedRq_Object = MibTableColumn
tmnxVdoIfStLowRTSvrRxPipFailedRq = _TmnxVdoIfStLowRTSvrRxPipFailedRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 9),
    _TmnxVdoIfStLowRTSvrRxPipFailedRq_Type()
)
tmnxVdoIfStLowRTSvrRxPipFailedRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrRxPipFailedRq.setStatus("current")
_TmnxVdoIfStLowRTSvrTxSdRTReplies_Type = Counter32
_TmnxVdoIfStLowRTSvrTxSdRTReplies_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxSdRTReplies = _TmnxVdoIfStLowRTSvrTxSdRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 10),
    _TmnxVdoIfStLowRTSvrTxSdRTReplies_Type()
)
tmnxVdoIfStLowRTSvrTxSdRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxSdRTReplies.setStatus("current")
_TmnxVdoIfStLowRTSvrTxSdBytes_Type = Counter32
_TmnxVdoIfStLowRTSvrTxSdBytes_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxSdBytes = _TmnxVdoIfStLowRTSvrTxSdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 11),
    _TmnxVdoIfStLowRTSvrTxSdBytes_Type()
)
tmnxVdoIfStLowRTSvrTxSdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxSdBytes.setStatus("current")
_TmnxVdoIfStLowRTSvrTxSdPackets_Type = Counter32
_TmnxVdoIfStLowRTSvrTxSdPackets_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxSdPackets = _TmnxVdoIfStLowRTSvrTxSdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 12),
    _TmnxVdoIfStLowRTSvrTxSdPackets_Type()
)
tmnxVdoIfStLowRTSvrTxSdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxSdPackets.setStatus("current")
_TmnxVdoIfStLowRTSvrTxHdRTReplies_Type = Counter32
_TmnxVdoIfStLowRTSvrTxHdRTReplies_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxHdRTReplies = _TmnxVdoIfStLowRTSvrTxHdRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 13),
    _TmnxVdoIfStLowRTSvrTxHdRTReplies_Type()
)
tmnxVdoIfStLowRTSvrTxHdRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxHdRTReplies.setStatus("current")
_TmnxVdoIfStLowRTSvrTxHdBytes_Type = Counter32
_TmnxVdoIfStLowRTSvrTxHdBytes_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxHdBytes = _TmnxVdoIfStLowRTSvrTxHdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 14),
    _TmnxVdoIfStLowRTSvrTxHdBytes_Type()
)
tmnxVdoIfStLowRTSvrTxHdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxHdBytes.setStatus("current")
_TmnxVdoIfStLowRTSvrTxHdPackets_Type = Counter32
_TmnxVdoIfStLowRTSvrTxHdPackets_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxHdPackets = _TmnxVdoIfStLowRTSvrTxHdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 15),
    _TmnxVdoIfStLowRTSvrTxHdPackets_Type()
)
tmnxVdoIfStLowRTSvrTxHdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxHdPackets.setStatus("current")
_TmnxVdoIfStLowRTSvrTxPipRTReplis_Type = Counter32
_TmnxVdoIfStLowRTSvrTxPipRTReplis_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxPipRTReplis = _TmnxVdoIfStLowRTSvrTxPipRTReplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 16),
    _TmnxVdoIfStLowRTSvrTxPipRTReplis_Type()
)
tmnxVdoIfStLowRTSvrTxPipRTReplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxPipRTReplis.setStatus("current")
_TmnxVdoIfStLowRTSvrTxPipBytes_Type = Counter32
_TmnxVdoIfStLowRTSvrTxPipBytes_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxPipBytes = _TmnxVdoIfStLowRTSvrTxPipBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 17),
    _TmnxVdoIfStLowRTSvrTxPipBytes_Type()
)
tmnxVdoIfStLowRTSvrTxPipBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxPipBytes.setStatus("current")
_TmnxVdoIfStLowRTSvrTxPipPackets_Type = Counter32
_TmnxVdoIfStLowRTSvrTxPipPackets_Object = MibTableColumn
tmnxVdoIfStLowRTSvrTxPipPackets = _TmnxVdoIfStLowRTSvrTxPipPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 18),
    _TmnxVdoIfStLowRTSvrTxPipPackets_Type()
)
tmnxVdoIfStLowRTSvrTxPipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowRTSvrTxPipPackets.setStatus("current")
_TmnxVdoIfStLowFCCSrRxSdFCCReq_Type = Counter32
_TmnxVdoIfStLowFCCSrRxSdFCCReq_Object = MibTableColumn
tmnxVdoIfStLowFCCSrRxSdFCCReq = _TmnxVdoIfStLowFCCSrRxSdFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 19),
    _TmnxVdoIfStLowFCCSrRxSdFCCReq_Type()
)
tmnxVdoIfStLowFCCSrRxSdFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrRxSdFCCReq.setStatus("current")
_TmnxVdoIfStLowFCCSrRxSdFailedReq_Type = Counter32
_TmnxVdoIfStLowFCCSrRxSdFailedReq_Object = MibTableColumn
tmnxVdoIfStLowFCCSrRxSdFailedReq = _TmnxVdoIfStLowFCCSrRxSdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 20),
    _TmnxVdoIfStLowFCCSrRxSdFailedReq_Type()
)
tmnxVdoIfStLowFCCSrRxSdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrRxSdFailedReq.setStatus("current")
_TmnxVdoIfStLowFCCSrRxHdFCCReq_Type = Counter32
_TmnxVdoIfStLowFCCSrRxHdFCCReq_Object = MibTableColumn
tmnxVdoIfStLowFCCSrRxHdFCCReq = _TmnxVdoIfStLowFCCSrRxHdFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 21),
    _TmnxVdoIfStLowFCCSrRxHdFCCReq_Type()
)
tmnxVdoIfStLowFCCSrRxHdFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrRxHdFCCReq.setStatus("current")
_TmnxVdoIfStLowFCCSrRxHdFailedReq_Type = Counter32
_TmnxVdoIfStLowFCCSrRxHdFailedReq_Object = MibTableColumn
tmnxVdoIfStLowFCCSrRxHdFailedReq = _TmnxVdoIfStLowFCCSrRxHdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 22),
    _TmnxVdoIfStLowFCCSrRxHdFailedReq_Type()
)
tmnxVdoIfStLowFCCSrRxHdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrRxHdFailedReq.setStatus("current")
_TmnxVdoIfStLowFCCSrRxPipFCCReq_Type = Counter32
_TmnxVdoIfStLowFCCSrRxPipFCCReq_Object = MibTableColumn
tmnxVdoIfStLowFCCSrRxPipFCCReq = _TmnxVdoIfStLowFCCSrRxPipFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 23),
    _TmnxVdoIfStLowFCCSrRxPipFCCReq_Type()
)
tmnxVdoIfStLowFCCSrRxPipFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrRxPipFCCReq.setStatus("current")
_TmnxVdoIfStLowFCCSrRxPipFailedRq_Type = Counter32
_TmnxVdoIfStLowFCCSrRxPipFailedRq_Object = MibTableColumn
tmnxVdoIfStLowFCCSrRxPipFailedRq = _TmnxVdoIfStLowFCCSrRxPipFailedRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 24),
    _TmnxVdoIfStLowFCCSrRxPipFailedRq_Type()
)
tmnxVdoIfStLowFCCSrRxPipFailedRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrRxPipFailedRq.setStatus("current")
_TmnxVdoIfStLowFCCSrTxSdFCCReplis_Type = Counter32
_TmnxVdoIfStLowFCCSrTxSdFCCReplis_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxSdFCCReplis = _TmnxVdoIfStLowFCCSrTxSdFCCReplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 25),
    _TmnxVdoIfStLowFCCSrTxSdFCCReplis_Type()
)
tmnxVdoIfStLowFCCSrTxSdFCCReplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxSdFCCReplis.setStatus("current")
_TmnxVdoIfStLowFCCSrTxSdBytes_Type = Counter32
_TmnxVdoIfStLowFCCSrTxSdBytes_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxSdBytes = _TmnxVdoIfStLowFCCSrTxSdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 26),
    _TmnxVdoIfStLowFCCSrTxSdBytes_Type()
)
tmnxVdoIfStLowFCCSrTxSdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxSdBytes.setStatus("current")
_TmnxVdoIfStLowFCCSrTxSdPackets_Type = Counter32
_TmnxVdoIfStLowFCCSrTxSdPackets_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxSdPackets = _TmnxVdoIfStLowFCCSrTxSdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 27),
    _TmnxVdoIfStLowFCCSrTxSdPackets_Type()
)
tmnxVdoIfStLowFCCSrTxSdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxSdPackets.setStatus("current")
_TmnxVdoIfStLowFCCSrTxHdFCCReplis_Type = Counter32
_TmnxVdoIfStLowFCCSrTxHdFCCReplis_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxHdFCCReplis = _TmnxVdoIfStLowFCCSrTxHdFCCReplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 28),
    _TmnxVdoIfStLowFCCSrTxHdFCCReplis_Type()
)
tmnxVdoIfStLowFCCSrTxHdFCCReplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxHdFCCReplis.setStatus("current")
_TmnxVdoIfStLowFCCSrTxHdBytes_Type = Counter32
_TmnxVdoIfStLowFCCSrTxHdBytes_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxHdBytes = _TmnxVdoIfStLowFCCSrTxHdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 29),
    _TmnxVdoIfStLowFCCSrTxHdBytes_Type()
)
tmnxVdoIfStLowFCCSrTxHdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxHdBytes.setStatus("current")
_TmnxVdoIfStLowFCCSrTxHdPackets_Type = Counter32
_TmnxVdoIfStLowFCCSrTxHdPackets_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxHdPackets = _TmnxVdoIfStLowFCCSrTxHdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 30),
    _TmnxVdoIfStLowFCCSrTxHdPackets_Type()
)
tmnxVdoIfStLowFCCSrTxHdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxHdPackets.setStatus("current")
_TmnxVdoIfStLowFCCSrTxPipFCCRplis_Type = Counter32
_TmnxVdoIfStLowFCCSrTxPipFCCRplis_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxPipFCCRplis = _TmnxVdoIfStLowFCCSrTxPipFCCRplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 31),
    _TmnxVdoIfStLowFCCSrTxPipFCCRplis_Type()
)
tmnxVdoIfStLowFCCSrTxPipFCCRplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxPipFCCRplis.setStatus("current")
_TmnxVdoIfStLowFCCSrTxPipBytes_Type = Counter32
_TmnxVdoIfStLowFCCSrTxPipBytes_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxPipBytes = _TmnxVdoIfStLowFCCSrTxPipBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 32),
    _TmnxVdoIfStLowFCCSrTxPipBytes_Type()
)
tmnxVdoIfStLowFCCSrTxPipBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxPipBytes.setStatus("current")
_TmnxVdoIfStLowFCCSrTxPipPackets_Type = Counter32
_TmnxVdoIfStLowFCCSrTxPipPackets_Object = MibTableColumn
tmnxVdoIfStLowFCCSrTxPipPackets = _TmnxVdoIfStLowFCCSrTxPipPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 33),
    _TmnxVdoIfStLowFCCSrTxPipPackets_Type()
)
tmnxVdoIfStLowFCCSrTxPipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowFCCSrTxPipPackets.setStatus("current")
_TmnxVdoIfStLowTxFailedPackets_Type = Counter32
_TmnxVdoIfStLowTxFailedPackets_Object = MibTableColumn
tmnxVdoIfStLowTxFailedPackets = _TmnxVdoIfStLowTxFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 11, 1, 34),
    _TmnxVdoIfStLowTxFailedPackets_Type()
)
tmnxVdoIfStLowTxFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStLowTxFailedPackets.setStatus("current")
_TmnxVdoIfStHghTable_Object = MibTable
tmnxVdoIfStHghTable = _TmnxVdoIfStHghTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStHghTable.setStatus("current")
_TmnxVdoIfStHghEntry_Object = MibTableRow
tmnxVdoIfStHghEntry = _TmnxVdoIfStHghEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStHghEntry.setStatus("current")
_TmnxVdoIfStHghRTSvrSdRtpPktsReq_Type = Counter32
_TmnxVdoIfStHghRTSvrSdRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrSdRtpPktsReq = _TmnxVdoIfStHghRTSvrSdRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 1),
    _TmnxVdoIfStHghRTSvrSdRtpPktsReq_Type()
)
tmnxVdoIfStHghRTSvrSdRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrSdRtpPktsReq.setStatus("current")
_TmnxVdoIfStHghRTSvrHdRtpPktsReq_Type = Counter32
_TmnxVdoIfStHghRTSvrHdRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrHdRtpPktsReq = _TmnxVdoIfStHghRTSvrHdRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 2),
    _TmnxVdoIfStHghRTSvrHdRtpPktsReq_Type()
)
tmnxVdoIfStHghRTSvrHdRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrHdRtpPktsReq.setStatus("current")
_TmnxVdoIfStHghRTSvrPipRtpPktsReq_Type = Counter32
_TmnxVdoIfStHghRTSvrPipRtpPktsReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrPipRtpPktsReq = _TmnxVdoIfStHghRTSvrPipRtpPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 3),
    _TmnxVdoIfStHghRTSvrPipRtpPktsReq_Type()
)
tmnxVdoIfStHghRTSvrPipRtpPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrPipRtpPktsReq.setStatus("current")
_TmnxVdoIfStHghRTSvrRxSdRTReq_Type = Counter32
_TmnxVdoIfStHghRTSvrRxSdRTReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrRxSdRTReq = _TmnxVdoIfStHghRTSvrRxSdRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 4),
    _TmnxVdoIfStHghRTSvrRxSdRTReq_Type()
)
tmnxVdoIfStHghRTSvrRxSdRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrRxSdRTReq.setStatus("current")
_TmnxVdoIfStHghRTSvrRxSdFailedReq_Type = Counter32
_TmnxVdoIfStHghRTSvrRxSdFailedReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrRxSdFailedReq = _TmnxVdoIfStHghRTSvrRxSdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 5),
    _TmnxVdoIfStHghRTSvrRxSdFailedReq_Type()
)
tmnxVdoIfStHghRTSvrRxSdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrRxSdFailedReq.setStatus("current")
_TmnxVdoIfStHghRTSvrRxHdRTReq_Type = Counter32
_TmnxVdoIfStHghRTSvrRxHdRTReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrRxHdRTReq = _TmnxVdoIfStHghRTSvrRxHdRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 6),
    _TmnxVdoIfStHghRTSvrRxHdRTReq_Type()
)
tmnxVdoIfStHghRTSvrRxHdRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrRxHdRTReq.setStatus("current")
_TmnxVdoIfStHghRTSvrRxHdFailedReq_Type = Counter32
_TmnxVdoIfStHghRTSvrRxHdFailedReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrRxHdFailedReq = _TmnxVdoIfStHghRTSvrRxHdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 7),
    _TmnxVdoIfStHghRTSvrRxHdFailedReq_Type()
)
tmnxVdoIfStHghRTSvrRxHdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrRxHdFailedReq.setStatus("current")
_TmnxVdoIfStHghRTSvrRxPipRTReq_Type = Counter32
_TmnxVdoIfStHghRTSvrRxPipRTReq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrRxPipRTReq = _TmnxVdoIfStHghRTSvrRxPipRTReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 8),
    _TmnxVdoIfStHghRTSvrRxPipRTReq_Type()
)
tmnxVdoIfStHghRTSvrRxPipRTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrRxPipRTReq.setStatus("current")
_TmnxVdoIfStHghRTSvrRxPipFailedRq_Type = Counter32
_TmnxVdoIfStHghRTSvrRxPipFailedRq_Object = MibTableColumn
tmnxVdoIfStHghRTSvrRxPipFailedRq = _TmnxVdoIfStHghRTSvrRxPipFailedRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 9),
    _TmnxVdoIfStHghRTSvrRxPipFailedRq_Type()
)
tmnxVdoIfStHghRTSvrRxPipFailedRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrRxPipFailedRq.setStatus("current")
_TmnxVdoIfStHghRTSvrTxSdRTReplies_Type = Counter32
_TmnxVdoIfStHghRTSvrTxSdRTReplies_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxSdRTReplies = _TmnxVdoIfStHghRTSvrTxSdRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 10),
    _TmnxVdoIfStHghRTSvrTxSdRTReplies_Type()
)
tmnxVdoIfStHghRTSvrTxSdRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxSdRTReplies.setStatus("current")
_TmnxVdoIfStHghRTSvrTxSdBytes_Type = Counter32
_TmnxVdoIfStHghRTSvrTxSdBytes_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxSdBytes = _TmnxVdoIfStHghRTSvrTxSdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 11),
    _TmnxVdoIfStHghRTSvrTxSdBytes_Type()
)
tmnxVdoIfStHghRTSvrTxSdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxSdBytes.setStatus("current")
_TmnxVdoIfStHghRTSvrTxSdPackets_Type = Counter32
_TmnxVdoIfStHghRTSvrTxSdPackets_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxSdPackets = _TmnxVdoIfStHghRTSvrTxSdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 12),
    _TmnxVdoIfStHghRTSvrTxSdPackets_Type()
)
tmnxVdoIfStHghRTSvrTxSdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxSdPackets.setStatus("current")
_TmnxVdoIfStHghRTSvrTxHdRTReplies_Type = Counter32
_TmnxVdoIfStHghRTSvrTxHdRTReplies_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxHdRTReplies = _TmnxVdoIfStHghRTSvrTxHdRTReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 13),
    _TmnxVdoIfStHghRTSvrTxHdRTReplies_Type()
)
tmnxVdoIfStHghRTSvrTxHdRTReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxHdRTReplies.setStatus("current")
_TmnxVdoIfStHghRTSvrTxHdBytes_Type = Counter32
_TmnxVdoIfStHghRTSvrTxHdBytes_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxHdBytes = _TmnxVdoIfStHghRTSvrTxHdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 14),
    _TmnxVdoIfStHghRTSvrTxHdBytes_Type()
)
tmnxVdoIfStHghRTSvrTxHdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxHdBytes.setStatus("current")
_TmnxVdoIfStHghRTSvrTxHdPackets_Type = Counter32
_TmnxVdoIfStHghRTSvrTxHdPackets_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxHdPackets = _TmnxVdoIfStHghRTSvrTxHdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 15),
    _TmnxVdoIfStHghRTSvrTxHdPackets_Type()
)
tmnxVdoIfStHghRTSvrTxHdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxHdPackets.setStatus("current")
_TmnxVdoIfStHghRTSvrTxPipRTReplis_Type = Counter32
_TmnxVdoIfStHghRTSvrTxPipRTReplis_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxPipRTReplis = _TmnxVdoIfStHghRTSvrTxPipRTReplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 16),
    _TmnxVdoIfStHghRTSvrTxPipRTReplis_Type()
)
tmnxVdoIfStHghRTSvrTxPipRTReplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxPipRTReplis.setStatus("current")
_TmnxVdoIfStHghRTSvrTxPipBytes_Type = Counter32
_TmnxVdoIfStHghRTSvrTxPipBytes_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxPipBytes = _TmnxVdoIfStHghRTSvrTxPipBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 17),
    _TmnxVdoIfStHghRTSvrTxPipBytes_Type()
)
tmnxVdoIfStHghRTSvrTxPipBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxPipBytes.setStatus("current")
_TmnxVdoIfStHghRTSvrTxPipPackets_Type = Counter32
_TmnxVdoIfStHghRTSvrTxPipPackets_Object = MibTableColumn
tmnxVdoIfStHghRTSvrTxPipPackets = _TmnxVdoIfStHghRTSvrTxPipPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 18),
    _TmnxVdoIfStHghRTSvrTxPipPackets_Type()
)
tmnxVdoIfStHghRTSvrTxPipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghRTSvrTxPipPackets.setStatus("current")
_TmnxVdoIfStHghFCCSrRxSdFCCReq_Type = Counter32
_TmnxVdoIfStHghFCCSrRxSdFCCReq_Object = MibTableColumn
tmnxVdoIfStHghFCCSrRxSdFCCReq = _TmnxVdoIfStHghFCCSrRxSdFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 19),
    _TmnxVdoIfStHghFCCSrRxSdFCCReq_Type()
)
tmnxVdoIfStHghFCCSrRxSdFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrRxSdFCCReq.setStatus("current")
_TmnxVdoIfStHghFCCSrRxSdFailedReq_Type = Counter32
_TmnxVdoIfStHghFCCSrRxSdFailedReq_Object = MibTableColumn
tmnxVdoIfStHghFCCSrRxSdFailedReq = _TmnxVdoIfStHghFCCSrRxSdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 20),
    _TmnxVdoIfStHghFCCSrRxSdFailedReq_Type()
)
tmnxVdoIfStHghFCCSrRxSdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrRxSdFailedReq.setStatus("current")
_TmnxVdoIfStHghFCCSrRxHdFCCReq_Type = Counter32
_TmnxVdoIfStHghFCCSrRxHdFCCReq_Object = MibTableColumn
tmnxVdoIfStHghFCCSrRxHdFCCReq = _TmnxVdoIfStHghFCCSrRxHdFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 21),
    _TmnxVdoIfStHghFCCSrRxHdFCCReq_Type()
)
tmnxVdoIfStHghFCCSrRxHdFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrRxHdFCCReq.setStatus("current")
_TmnxVdoIfStHghFCCSrRxHdFailedReq_Type = Counter32
_TmnxVdoIfStHghFCCSrRxHdFailedReq_Object = MibTableColumn
tmnxVdoIfStHghFCCSrRxHdFailedReq = _TmnxVdoIfStHghFCCSrRxHdFailedReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 22),
    _TmnxVdoIfStHghFCCSrRxHdFailedReq_Type()
)
tmnxVdoIfStHghFCCSrRxHdFailedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrRxHdFailedReq.setStatus("current")
_TmnxVdoIfStHghFCCSrRxPipFCCReq_Type = Counter32
_TmnxVdoIfStHghFCCSrRxPipFCCReq_Object = MibTableColumn
tmnxVdoIfStHghFCCSrRxPipFCCReq = _TmnxVdoIfStHghFCCSrRxPipFCCReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 23),
    _TmnxVdoIfStHghFCCSrRxPipFCCReq_Type()
)
tmnxVdoIfStHghFCCSrRxPipFCCReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrRxPipFCCReq.setStatus("current")
_TmnxVdoIfStHghFCCSrRxPipFailedRq_Type = Counter32
_TmnxVdoIfStHghFCCSrRxPipFailedRq_Object = MibTableColumn
tmnxVdoIfStHghFCCSrRxPipFailedRq = _TmnxVdoIfStHghFCCSrRxPipFailedRq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 24),
    _TmnxVdoIfStHghFCCSrRxPipFailedRq_Type()
)
tmnxVdoIfStHghFCCSrRxPipFailedRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrRxPipFailedRq.setStatus("current")
_TmnxVdoIfStHghFCCSrTxSdFCCReplis_Type = Counter32
_TmnxVdoIfStHghFCCSrTxSdFCCReplis_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxSdFCCReplis = _TmnxVdoIfStHghFCCSrTxSdFCCReplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 25),
    _TmnxVdoIfStHghFCCSrTxSdFCCReplis_Type()
)
tmnxVdoIfStHghFCCSrTxSdFCCReplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxSdFCCReplis.setStatus("current")
_TmnxVdoIfStHghFCCSrTxSdBytes_Type = Counter32
_TmnxVdoIfStHghFCCSrTxSdBytes_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxSdBytes = _TmnxVdoIfStHghFCCSrTxSdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 26),
    _TmnxVdoIfStHghFCCSrTxSdBytes_Type()
)
tmnxVdoIfStHghFCCSrTxSdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxSdBytes.setStatus("current")
_TmnxVdoIfStHghFCCSrTxSdPackets_Type = Counter32
_TmnxVdoIfStHghFCCSrTxSdPackets_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxSdPackets = _TmnxVdoIfStHghFCCSrTxSdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 27),
    _TmnxVdoIfStHghFCCSrTxSdPackets_Type()
)
tmnxVdoIfStHghFCCSrTxSdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxSdPackets.setStatus("current")
_TmnxVdoIfStHghFCCSrTxHdFCCReplis_Type = Counter32
_TmnxVdoIfStHghFCCSrTxHdFCCReplis_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxHdFCCReplis = _TmnxVdoIfStHghFCCSrTxHdFCCReplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 28),
    _TmnxVdoIfStHghFCCSrTxHdFCCReplis_Type()
)
tmnxVdoIfStHghFCCSrTxHdFCCReplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxHdFCCReplis.setStatus("current")
_TmnxVdoIfStHghFCCSrTxHdBytes_Type = Counter32
_TmnxVdoIfStHghFCCSrTxHdBytes_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxHdBytes = _TmnxVdoIfStHghFCCSrTxHdBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 29),
    _TmnxVdoIfStHghFCCSrTxHdBytes_Type()
)
tmnxVdoIfStHghFCCSrTxHdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxHdBytes.setStatus("current")
_TmnxVdoIfStHghFCCSrTxHdPackets_Type = Counter32
_TmnxVdoIfStHghFCCSrTxHdPackets_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxHdPackets = _TmnxVdoIfStHghFCCSrTxHdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 30),
    _TmnxVdoIfStHghFCCSrTxHdPackets_Type()
)
tmnxVdoIfStHghFCCSrTxHdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxHdPackets.setStatus("current")
_TmnxVdoIfStHghFCCSrTxPipFCCRplis_Type = Counter32
_TmnxVdoIfStHghFCCSrTxPipFCCRplis_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxPipFCCRplis = _TmnxVdoIfStHghFCCSrTxPipFCCRplis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 31),
    _TmnxVdoIfStHghFCCSrTxPipFCCRplis_Type()
)
tmnxVdoIfStHghFCCSrTxPipFCCRplis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxPipFCCRplis.setStatus("current")
_TmnxVdoIfStHghFCCSrTxPipBytes_Type = Counter32
_TmnxVdoIfStHghFCCSrTxPipBytes_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxPipBytes = _TmnxVdoIfStHghFCCSrTxPipBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 32),
    _TmnxVdoIfStHghFCCSrTxPipBytes_Type()
)
tmnxVdoIfStHghFCCSrTxPipBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxPipBytes.setStatus("current")
_TmnxVdoIfStHghFCCSrTxPipPackets_Type = Counter32
_TmnxVdoIfStHghFCCSrTxPipPackets_Object = MibTableColumn
tmnxVdoIfStHghFCCSrTxPipPackets = _TmnxVdoIfStHghFCCSrTxPipPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 33),
    _TmnxVdoIfStHghFCCSrTxPipPackets_Type()
)
tmnxVdoIfStHghFCCSrTxPipPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghFCCSrTxPipPackets.setStatus("current")
_TmnxVdoIfStHghTxFailedPackets_Type = Counter32
_TmnxVdoIfStHghTxFailedPackets_Object = MibTableColumn
tmnxVdoIfStHghTxFailedPackets = _TmnxVdoIfStHghTxFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 12, 1, 34),
    _TmnxVdoIfStHghTxFailedPackets_Type()
)
tmnxVdoIfStHghTxFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStHghTxFailedPackets.setStatus("current")
_TmnxVdoPIDTable_Object = MibTable
tmnxVdoPIDTable = _TmnxVdoPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxVdoPIDTable.setStatus("current")
_TmnxVdoPIDEntry_Object = MibTableRow
tmnxVdoPIDEntry = _TmnxVdoPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1)
)
tmnxVdoPIDEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGroupAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSourceAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoPID"),
)
if mibBuilder.loadTexts:
    tmnxVdoPIDEntry.setStatus("current")


class _TmnxVdoPID_Type(Unsigned32):
    """Custom type tmnxVdoPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_TmnxVdoPID_Type.__name__ = "Unsigned32"
_TmnxVdoPID_Object = MibTableColumn
tmnxVdoPID = _TmnxVdoPID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 1),
    _TmnxVdoPID_Type()
)
tmnxVdoPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoPID.setStatus("current")
_TmnxVdoPIDType_Type = TmnxVdoPIDType
_TmnxVdoPIDType_Object = MibTableColumn
tmnxVdoPIDType = _TmnxVdoPIDType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 2),
    _TmnxVdoPIDType_Type()
)
tmnxVdoPIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDType.setStatus("current")
_TmnxVdoPIDMpegStreamType_Type = Unsigned32
_TmnxVdoPIDMpegStreamType_Object = MibTableColumn
tmnxVdoPIDMpegStreamType = _TmnxVdoPIDMpegStreamType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 3),
    _TmnxVdoPIDMpegStreamType_Type()
)
tmnxVdoPIDMpegStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDMpegStreamType.setStatus("current")
_TmnxVdoPIDLanguage_Type = TNamedItem
_TmnxVdoPIDLanguage_Object = MibTableColumn
tmnxVdoPIDLanguage = _TmnxVdoPIDLanguage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 4),
    _TmnxVdoPIDLanguage_Type()
)
tmnxVdoPIDLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDLanguage.setStatus("current")
_TmnxVdoPIDCcErrSecs_Type = Unsigned32
_TmnxVdoPIDCcErrSecs_Object = MibTableColumn
tmnxVdoPIDCcErrSecs = _TmnxVdoPIDCcErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 5),
    _TmnxVdoPIDCcErrSecs_Type()
)
tmnxVdoPIDCcErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDCcErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoPIDCcErrSecs.setUnits("seconds")
_TmnxVdoPIDTeiErrSecs_Type = Unsigned32
_TmnxVdoPIDTeiErrSecs_Object = MibTableColumn
tmnxVdoPIDTeiErrSecs = _TmnxVdoPIDTeiErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 6),
    _TmnxVdoPIDTeiErrSecs_Type()
)
tmnxVdoPIDTeiErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDTeiErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoPIDTeiErrSecs.setUnits("seconds")
_TmnxVdoPIDAbsentErrSecs_Type = Unsigned32
_TmnxVdoPIDAbsentErrSecs_Object = MibTableColumn
tmnxVdoPIDAbsentErrSecs = _TmnxVdoPIDAbsentErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 7),
    _TmnxVdoPIDAbsentErrSecs_Type()
)
tmnxVdoPIDAbsentErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDAbsentErrSecs.setStatus("current")
_TmnxVdoPIDBitrate_Type = Unsigned32
_TmnxVdoPIDBitrate_Object = MibTableColumn
tmnxVdoPIDBitrate = _TmnxVdoPIDBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 8),
    _TmnxVdoPIDBitrate_Type()
)
tmnxVdoPIDBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDBitrate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoPIDBitrate.setUnits("kbps")
_TmnxVdoPIDIsPCR_Type = TruthValue
_TmnxVdoPIDIsPCR_Object = MibTableColumn
tmnxVdoPIDIsPCR = _TmnxVdoPIDIsPCR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 13, 1, 9),
    _TmnxVdoPIDIsPCR_Type()
)
tmnxVdoPIDIsPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoPIDIsPCR.setStatus("current")
_TmnxVdoIfScte30AdSrvrTable_Object = MibTable
tmnxVdoIfScte30AdSrvrTable = _TmnxVdoIfScte30AdSrvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxVdoIfScte30AdSrvrTable.setStatus("current")
_TmnxVdoIfScte30AdSrvrEntry_Object = MibTableRow
tmnxVdoIfScte30AdSrvrEntry = _TmnxVdoIfScte30AdSrvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 14, 1)
)
tmnxVdoIfScte30AdSrvrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30AdSrvrAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30AdSrvrAddr"),
)
if mibBuilder.loadTexts:
    tmnxVdoIfScte30AdSrvrEntry.setStatus("current")
_TmnxVdoIfScte30AdSrvrAddrType_Type = InetAddressType
_TmnxVdoIfScte30AdSrvrAddrType_Object = MibTableColumn
tmnxVdoIfScte30AdSrvrAddrType = _TmnxVdoIfScte30AdSrvrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 14, 1, 1),
    _TmnxVdoIfScte30AdSrvrAddrType_Type()
)
tmnxVdoIfScte30AdSrvrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30AdSrvrAddrType.setStatus("current")


class _TmnxVdoIfScte30AdSrvrAddr_Type(InetAddress):
    """Custom type tmnxVdoIfScte30AdSrvrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoIfScte30AdSrvrAddr_Type.__name__ = "InetAddress"
_TmnxVdoIfScte30AdSrvrAddr_Object = MibTableColumn
tmnxVdoIfScte30AdSrvrAddr = _TmnxVdoIfScte30AdSrvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 14, 1, 2),
    _TmnxVdoIfScte30AdSrvrAddr_Type()
)
tmnxVdoIfScte30AdSrvrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30AdSrvrAddr.setStatus("current")
_TmnxVdoIfScte30AdSrvrRowStatus_Type = RowStatus
_TmnxVdoIfScte30AdSrvrRowStatus_Object = MibTableColumn
tmnxVdoIfScte30AdSrvrRowStatus = _TmnxVdoIfScte30AdSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 14, 1, 3),
    _TmnxVdoIfScte30AdSrvrRowStatus_Type()
)
tmnxVdoIfScte30AdSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30AdSrvrRowStatus.setStatus("current")
_TmnxVdoSGAdiStatTable_Object = MibTable
tmnxVdoSGAdiStatTable = _TmnxVdoSGAdiStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxVdoSGAdiStatTable.setStatus("current")
_TmnxVdoSGAdiStatEntry_Object = MibTableRow
tmnxVdoSGAdiStatEntry = _TmnxVdoSGAdiStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1)
)
tmnxVdoSGAdiStatEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGroupAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSourceAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiServerAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiServerAddr"),
)
if mibBuilder.loadTexts:
    tmnxVdoSGAdiStatEntry.setStatus("current")
_TmnxVdoSGAdiServerAddrType_Type = InetAddressType
_TmnxVdoSGAdiServerAddrType_Object = MibTableColumn
tmnxVdoSGAdiServerAddrType = _TmnxVdoSGAdiServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 1),
    _TmnxVdoSGAdiServerAddrType_Type()
)
tmnxVdoSGAdiServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiServerAddrType.setStatus("current")


class _TmnxVdoSGAdiServerAddr_Type(InetAddress):
    """Custom type tmnxVdoSGAdiServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoSGAdiServerAddr_Type.__name__ = "InetAddress"
_TmnxVdoSGAdiServerAddr_Object = MibTableColumn
tmnxVdoSGAdiServerAddr = _TmnxVdoSGAdiServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 2),
    _TmnxVdoSGAdiServerAddr_Type()
)
tmnxVdoSGAdiServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiServerAddr.setStatus("current")
_TmnxVdoSGAdiServerUptime_Type = Unsigned32
_TmnxVdoSGAdiServerUptime_Object = MibTableColumn
tmnxVdoSGAdiServerUptime = _TmnxVdoSGAdiServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 3),
    _TmnxVdoSGAdiServerUptime_Type()
)
tmnxVdoSGAdiServerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiServerUptime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiServerUptime.setUnits("seconds")
_TmnxVdoSGAdiInitReq_Type = Counter32
_TmnxVdoSGAdiInitReq_Object = MibTableColumn
tmnxVdoSGAdiInitReq = _TmnxVdoSGAdiInitReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 4),
    _TmnxVdoSGAdiInitReq_Type()
)
tmnxVdoSGAdiInitReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiInitReq.setStatus("current")
_TmnxVdoSGAdiSucInitResp_Type = Counter32
_TmnxVdoSGAdiSucInitResp_Object = MibTableColumn
tmnxVdoSGAdiSucInitResp = _TmnxVdoSGAdiSucInitResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 5),
    _TmnxVdoSGAdiSucInitResp_Type()
)
tmnxVdoSGAdiSucInitResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucInitResp.setStatus("current")
_TmnxVdoSGAdiUnsucInitResp_Type = Counter32
_TmnxVdoSGAdiUnsucInitResp_Object = MibTableColumn
tmnxVdoSGAdiUnsucInitResp = _TmnxVdoSGAdiUnsucInitResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 6),
    _TmnxVdoSGAdiUnsucInitResp_Type()
)
tmnxVdoSGAdiUnsucInitResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnsucInitResp.setStatus("current")
_TmnxVdoSGAdiAliveReq_Type = Counter32
_TmnxVdoSGAdiAliveReq_Object = MibTableColumn
tmnxVdoSGAdiAliveReq = _TmnxVdoSGAdiAliveReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 7),
    _TmnxVdoSGAdiAliveReq_Type()
)
tmnxVdoSGAdiAliveReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiAliveReq.setStatus("current")
_TmnxVdoSGAdiSucAliveResp_Type = Counter32
_TmnxVdoSGAdiSucAliveResp_Object = MibTableColumn
tmnxVdoSGAdiSucAliveResp = _TmnxVdoSGAdiSucAliveResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 8),
    _TmnxVdoSGAdiSucAliveResp_Type()
)
tmnxVdoSGAdiSucAliveResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucAliveResp.setStatus("current")
_TmnxVdoSGAdiUnSucAliveResp_Type = Counter32
_TmnxVdoSGAdiUnSucAliveResp_Object = MibTableColumn
tmnxVdoSGAdiUnSucAliveResp = _TmnxVdoSGAdiUnSucAliveResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 9),
    _TmnxVdoSGAdiUnSucAliveResp_Type()
)
tmnxVdoSGAdiUnSucAliveResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnSucAliveResp.setStatus("current")
_TmnxVdoSGAdiCueReq_Type = Counter32
_TmnxVdoSGAdiCueReq_Object = MibTableColumn
tmnxVdoSGAdiCueReq = _TmnxVdoSGAdiCueReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 10),
    _TmnxVdoSGAdiCueReq_Type()
)
tmnxVdoSGAdiCueReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiCueReq.setStatus("current")
_TmnxVdoSGAdiSucCueResp_Type = Counter32
_TmnxVdoSGAdiSucCueResp_Object = MibTableColumn
tmnxVdoSGAdiSucCueResp = _TmnxVdoSGAdiSucCueResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 11),
    _TmnxVdoSGAdiSucCueResp_Type()
)
tmnxVdoSGAdiSucCueResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucCueResp.setStatus("current")
_TmnxVdoSGAdiUnsucCueResp_Type = Counter32
_TmnxVdoSGAdiUnsucCueResp_Object = MibTableColumn
tmnxVdoSGAdiUnsucCueResp = _TmnxVdoSGAdiUnsucCueResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 12),
    _TmnxVdoSGAdiUnsucCueResp_Type()
)
tmnxVdoSGAdiUnsucCueResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnsucCueResp.setStatus("current")
_TmnxVdoSGAdiAbortReq_Type = Counter32
_TmnxVdoSGAdiAbortReq_Object = MibTableColumn
tmnxVdoSGAdiAbortReq = _TmnxVdoSGAdiAbortReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 13),
    _TmnxVdoSGAdiAbortReq_Type()
)
tmnxVdoSGAdiAbortReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiAbortReq.setStatus("current")
_TmnxVdoSGAdiSucAbortResp_Type = Counter32
_TmnxVdoSGAdiSucAbortResp_Object = MibTableColumn
tmnxVdoSGAdiSucAbortResp = _TmnxVdoSGAdiSucAbortResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 14),
    _TmnxVdoSGAdiSucAbortResp_Type()
)
tmnxVdoSGAdiSucAbortResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucAbortResp.setStatus("current")
_TmnxVdoSGAdiUnsucAbortResp_Type = Counter32
_TmnxVdoSGAdiUnsucAbortResp_Object = MibTableColumn
tmnxVdoSGAdiUnsucAbortResp = _TmnxVdoSGAdiUnsucAbortResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 15),
    _TmnxVdoSGAdiUnsucAbortResp_Type()
)
tmnxVdoSGAdiUnsucAbortResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnsucAbortResp.setStatus("current")
_TmnxVdoSGAdiUnknownSCTE30Req_Type = Counter32
_TmnxVdoSGAdiUnknownSCTE30Req_Object = MibTableColumn
tmnxVdoSGAdiUnknownSCTE30Req = _TmnxVdoSGAdiUnknownSCTE30Req_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 16),
    _TmnxVdoSGAdiUnknownSCTE30Req_Type()
)
tmnxVdoSGAdiUnknownSCTE30Req.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnknownSCTE30Req.setStatus("current")
_TmnxVdoSGAdiSpliceReq_Type = Counter32
_TmnxVdoSGAdiSpliceReq_Object = MibTableColumn
tmnxVdoSGAdiSpliceReq = _TmnxVdoSGAdiSpliceReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 17),
    _TmnxVdoSGAdiSpliceReq_Type()
)
tmnxVdoSGAdiSpliceReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSpliceReq.setStatus("current")
_TmnxVdoSGAdiSucSpliceResp_Type = Counter32
_TmnxVdoSGAdiSucSpliceResp_Object = MibTableColumn
tmnxVdoSGAdiSucSpliceResp = _TmnxVdoSGAdiSucSpliceResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 18),
    _TmnxVdoSGAdiSucSpliceResp_Type()
)
tmnxVdoSGAdiSucSpliceResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucSpliceResp.setStatus("current")
_TmnxVdoSGAdiUnsucSpliceResp_Type = Counter32
_TmnxVdoSGAdiUnsucSpliceResp_Object = MibTableColumn
tmnxVdoSGAdiUnsucSpliceResp = _TmnxVdoSGAdiUnsucSpliceResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 19),
    _TmnxVdoSGAdiUnsucSpliceResp_Type()
)
tmnxVdoSGAdiUnsucSpliceResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnsucSpliceResp.setStatus("current")
_TmnxVdoSGAdiSucSpliceInCompResp_Type = Counter32
_TmnxVdoSGAdiSucSpliceInCompResp_Object = MibTableColumn
tmnxVdoSGAdiSucSpliceInCompResp = _TmnxVdoSGAdiSucSpliceInCompResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 20),
    _TmnxVdoSGAdiSucSpliceInCompResp_Type()
)
tmnxVdoSGAdiSucSpliceInCompResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucSpliceInCompResp.setStatus("current")
_TmnxVdoSGAdiSucSpliceOutCompResp_Type = Counter32
_TmnxVdoSGAdiSucSpliceOutCompResp_Object = MibTableColumn
tmnxVdoSGAdiSucSpliceOutCompResp = _TmnxVdoSGAdiSucSpliceOutCompResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 21),
    _TmnxVdoSGAdiSucSpliceOutCompResp_Type()
)
tmnxVdoSGAdiSucSpliceOutCompResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiSucSpliceOutCompResp.setStatus("current")
_TmnxVdoSGAdiUnsucSpliceOutComRes_Type = Counter32
_TmnxVdoSGAdiUnsucSpliceOutComRes_Object = MibTableColumn
tmnxVdoSGAdiUnsucSpliceOutComRes = _TmnxVdoSGAdiUnsucSpliceOutComRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 22),
    _TmnxVdoSGAdiUnsucSpliceOutComRes_Type()
)
tmnxVdoSGAdiUnsucSpliceOutComRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiUnsucSpliceOutComRes.setStatus("current")
_TmnxVdoSGAdiMinPort_Type = Counter32
_TmnxVdoSGAdiMinPort_Object = MibTableColumn
tmnxVdoSGAdiMinPort = _TmnxVdoSGAdiMinPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 23),
    _TmnxVdoSGAdiMinPort_Type()
)
tmnxVdoSGAdiMinPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiMinPort.setStatus("current")
_TmnxVdoSGAdiMaxPort_Type = Counter32
_TmnxVdoSGAdiMaxPort_Object = MibTableColumn
tmnxVdoSGAdiMaxPort = _TmnxVdoSGAdiMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 24),
    _TmnxVdoSGAdiMaxPort_Type()
)
tmnxVdoSGAdiMaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiMaxPort.setStatus("current")
_TmnxVdoSGAdiChlName_Type = TNamedItem
_TmnxVdoSGAdiChlName_Object = MibTableColumn
tmnxVdoSGAdiChlName = _TmnxVdoSGAdiChlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 15, 1, 25),
    _TmnxVdoSGAdiChlName_Type()
)
tmnxVdoSGAdiChlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGAdiChlName.setStatus("current")
_TmnxVdoSGSpliceStatusTable_Object = MibTable
tmnxVdoSGSpliceStatusTable = _TmnxVdoSGSpliceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceStatusTable.setStatus("current")
_TmnxVdoSGSpliceStatusEntry_Object = MibTableRow
tmnxVdoSGSpliceStatusEntry = _TmnxVdoSGSpliceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1)
)
tmnxVdoSGSpliceStatusEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGroupAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSourceAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceStartTime"),
)
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceStatusEntry.setStatus("current")
_TmnxVdoSGSpliceStartTime_Type = Unsigned32
_TmnxVdoSGSpliceStartTime_Object = MibTableColumn
tmnxVdoSGSpliceStartTime = _TmnxVdoSGSpliceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 1),
    _TmnxVdoSGSpliceStartTime_Type()
)
tmnxVdoSGSpliceStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceStartTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceStartTime.setUnits("seconds")
_TmnxVdoSGSpliceAdServerAddrType_Type = InetAddressType
_TmnxVdoSGSpliceAdServerAddrType_Object = MibTableColumn
tmnxVdoSGSpliceAdServerAddrType = _TmnxVdoSGSpliceAdServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 2),
    _TmnxVdoSGSpliceAdServerAddrType_Type()
)
tmnxVdoSGSpliceAdServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceAdServerAddrType.setStatus("current")


class _TmnxVdoSGSpliceAdServerAddr_Type(InetAddress):
    """Custom type tmnxVdoSGSpliceAdServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxVdoSGSpliceAdServerAddr_Type.__name__ = "InetAddress"
_TmnxVdoSGSpliceAdServerAddr_Object = MibTableColumn
tmnxVdoSGSpliceAdServerAddr = _TmnxVdoSGSpliceAdServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 3),
    _TmnxVdoSGSpliceAdServerAddr_Type()
)
tmnxVdoSGSpliceAdServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceAdServerAddr.setStatus("current")


class _TmnxVdoSGSpliceStatus_Type(Integer32):
    """Custom type tmnxVdoSGSpliceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("pending", 2),
          ("inProgress", 3),
          ("complete", 4))
    )


_TmnxVdoSGSpliceStatus_Type.__name__ = "Integer32"
_TmnxVdoSGSpliceStatus_Object = MibTableColumn
tmnxVdoSGSpliceStatus = _TmnxVdoSGSpliceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 4),
    _TmnxVdoSGSpliceStatus_Type()
)
tmnxVdoSGSpliceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceStatus.setStatus("current")
_TmnxVdoSGSpliceDurationReq_Type = Unsigned32
_TmnxVdoSGSpliceDurationReq_Object = MibTableColumn
tmnxVdoSGSpliceDurationReq = _TmnxVdoSGSpliceDurationReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 5),
    _TmnxVdoSGSpliceDurationReq_Type()
)
tmnxVdoSGSpliceDurationReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceDurationReq.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceDurationReq.setUnits("seconds")
_TmnxVdoSGSpliceDurationPlayed_Type = Unsigned32
_TmnxVdoSGSpliceDurationPlayed_Object = MibTableColumn
tmnxVdoSGSpliceDurationPlayed = _TmnxVdoSGSpliceDurationPlayed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 6),
    _TmnxVdoSGSpliceDurationPlayed_Type()
)
tmnxVdoSGSpliceDurationPlayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceDurationPlayed.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceDurationPlayed.setUnits("seconds")
_TmnxVdoSGSpliceRate_Type = Unsigned32
_TmnxVdoSGSpliceRate_Object = MibTableColumn
tmnxVdoSGSpliceRate = _TmnxVdoSGSpliceRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 7),
    _TmnxVdoSGSpliceRate_Type()
)
tmnxVdoSGSpliceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceRate.setUnits("kbps")
_TmnxVdoSGSpliceSessionId_Type = Unsigned32
_TmnxVdoSGSpliceSessionId_Object = MibTableColumn
tmnxVdoSGSpliceSessionId = _TmnxVdoSGSpliceSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 8),
    _TmnxVdoSGSpliceSessionId_Type()
)
tmnxVdoSGSpliceSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceSessionId.setStatus("current")
_TmnxVdoSGSplicePriorSessionId_Type = Unsigned32
_TmnxVdoSGSplicePriorSessionId_Object = MibTableColumn
tmnxVdoSGSplicePriorSessionId = _TmnxVdoSGSplicePriorSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 9),
    _TmnxVdoSGSplicePriorSessionId_Type()
)
tmnxVdoSGSplicePriorSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSplicePriorSessionId.setStatus("current")


class _TmnxVdoSGSpliceAbortReason_Type(Integer32):
    """Custom type tmnxVdoSGSpliceAbortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unknown", 1),
          ("adSrvrReq", 2),
          ("spliceNotFound", 3),
          ("noPrimaryChannel", 4),
          ("noInsertChannel", 5),
          ("tooEarly", 6),
          ("spliceFailed", 7),
          ("spliceCollision", 8),
          ("spliceTooLate", 9),
          ("spliceQueueFull", 10),
          ("invalidSessionId", 11),
          ("sessionIncomplete", 12))
    )


_TmnxVdoSGSpliceAbortReason_Type.__name__ = "Integer32"
_TmnxVdoSGSpliceAbortReason_Object = MibTableColumn
tmnxVdoSGSpliceAbortReason = _TmnxVdoSGSpliceAbortReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 10),
    _TmnxVdoSGSpliceAbortReason_Type()
)
tmnxVdoSGSpliceAbortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceAbortReason.setStatus("current")
_TmnxVdoSGSpliceSpliceInSeqNum_Type = Unsigned32
_TmnxVdoSGSpliceSpliceInSeqNum_Object = MibTableColumn
tmnxVdoSGSpliceSpliceInSeqNum = _TmnxVdoSGSpliceSpliceInSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 11),
    _TmnxVdoSGSpliceSpliceInSeqNum_Type()
)
tmnxVdoSGSpliceSpliceInSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceSpliceInSeqNum.setStatus("current")
_TmnxVdoSGSpliceSpliceOutSeqNum_Type = Unsigned32
_TmnxVdoSGSpliceSpliceOutSeqNum_Object = MibTableColumn
tmnxVdoSGSpliceSpliceOutSeqNum = _TmnxVdoSGSpliceSpliceOutSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 12),
    _TmnxVdoSGSpliceSpliceOutSeqNum_Type()
)
tmnxVdoSGSpliceSpliceOutSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceSpliceOutSeqNum.setStatus("current")
_TmnxVdoSGSpliceNumBlkFrames_Type = Unsigned32
_TmnxVdoSGSpliceNumBlkFrames_Object = MibTableColumn
tmnxVdoSGSpliceNumBlkFrames = _TmnxVdoSGSpliceNumBlkFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 13),
    _TmnxVdoSGSpliceNumBlkFrames_Type()
)
tmnxVdoSGSpliceNumBlkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceNumBlkFrames.setStatus("current")
_TmnxVdoSGSpliceBlkFramePTS_Type = TmnxVdoPTS
_TmnxVdoSGSpliceBlkFramePTS_Object = MibTableColumn
tmnxVdoSGSpliceBlkFramePTS = _TmnxVdoSGSpliceBlkFramePTS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 14),
    _TmnxVdoSGSpliceBlkFramePTS_Type()
)
tmnxVdoSGSpliceBlkFramePTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceBlkFramePTS.setStatus("current")
_TmnxVdoSGSpliceMaxAdPTS_Type = TmnxVdoPTS
_TmnxVdoSGSpliceMaxAdPTS_Object = MibTableColumn
tmnxVdoSGSpliceMaxAdPTS = _TmnxVdoSGSpliceMaxAdPTS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 15),
    _TmnxVdoSGSpliceMaxAdPTS_Type()
)
tmnxVdoSGSpliceMaxAdPTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceMaxAdPTS.setStatus("current")
_TmnxVdoSGSpliceMinNwPTS_Type = TmnxVdoPTS
_TmnxVdoSGSpliceMinNwPTS_Object = MibTableColumn
tmnxVdoSGSpliceMinNwPTS = _TmnxVdoSGSpliceMinNwPTS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 16, 1, 16),
    _TmnxVdoSGSpliceMinNwPTS_Type()
)
tmnxVdoSGSpliceMinNwPTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoSGSpliceMinNwPTS.setStatus("current")
_TmnxVdoIfStatExtTable_Object = MibTable
tmnxVdoIfStatExtTable = _TmnxVdoIfStatExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTable.setStatus("current")
_TmnxVdoIfStatExtEntry_Object = MibTableRow
tmnxVdoIfStatExtEntry = _TmnxVdoIfStatExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtEntry.setStatus("current")
_TmnxVdoIfStatExtRxRtcpAppRepSum_Type = Counter64
_TmnxVdoIfStatExtRxRtcpAppRepSum_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpAppRepSum = _TmnxVdoIfStatExtRxRtcpAppRepSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 1),
    _TmnxVdoIfStatExtRxRtcpAppRepSum_Type()
)
tmnxVdoIfStatExtRxRtcpAppRepSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpAppRepSum.setStatus("current")
_TmnxVdoIfStatExtRxRtcpAppRepSumL_Type = Counter32
_TmnxVdoIfStatExtRxRtcpAppRepSumL_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpAppRepSumL = _TmnxVdoIfStatExtRxRtcpAppRepSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 2),
    _TmnxVdoIfStatExtRxRtcpAppRepSumL_Type()
)
tmnxVdoIfStatExtRxRtcpAppRepSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpAppRepSumL.setStatus("current")
_TmnxVdoIfStatExtRxRtcpAppRepSumH_Type = Counter32
_TmnxVdoIfStatExtRxRtcpAppRepSumH_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpAppRepSumH = _TmnxVdoIfStatExtRxRtcpAppRepSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 3),
    _TmnxVdoIfStatExtRxRtcpAppRepSumH_Type()
)
tmnxVdoIfStatExtRxRtcpAppRepSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpAppRepSumH.setStatus("current")
_TmnxVdoIfStatExtRxRtcpAppReqSum_Type = Counter64
_TmnxVdoIfStatExtRxRtcpAppReqSum_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpAppReqSum = _TmnxVdoIfStatExtRxRtcpAppReqSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 4),
    _TmnxVdoIfStatExtRxRtcpAppReqSum_Type()
)
tmnxVdoIfStatExtRxRtcpAppReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpAppReqSum.setStatus("current")
_TmnxVdoIfStatExtRxRtcpAppReqSumL_Type = Counter32
_TmnxVdoIfStatExtRxRtcpAppReqSumL_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpAppReqSumL = _TmnxVdoIfStatExtRxRtcpAppReqSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 5),
    _TmnxVdoIfStatExtRxRtcpAppReqSumL_Type()
)
tmnxVdoIfStatExtRxRtcpAppReqSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpAppReqSumL.setStatus("current")
_TmnxVdoIfStatExtRxRtcpAppReqSumH_Type = Counter32
_TmnxVdoIfStatExtRxRtcpAppReqSumH_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpAppReqSumH = _TmnxVdoIfStatExtRxRtcpAppReqSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 6),
    _TmnxVdoIfStatExtRxRtcpAppReqSumH_Type()
)
tmnxVdoIfStatExtRxRtcpAppReqSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpAppReqSumH.setStatus("current")
_TmnxVdoIfStatExtRxRtcpFbRepSum_Type = Counter64
_TmnxVdoIfStatExtRxRtcpFbRepSum_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpFbRepSum = _TmnxVdoIfStatExtRxRtcpFbRepSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 7),
    _TmnxVdoIfStatExtRxRtcpFbRepSum_Type()
)
tmnxVdoIfStatExtRxRtcpFbRepSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpFbRepSum.setStatus("current")
_TmnxVdoIfStatExtRxRtcpFbRepSumL_Type = Counter32
_TmnxVdoIfStatExtRxRtcpFbRepSumL_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpFbRepSumL = _TmnxVdoIfStatExtRxRtcpFbRepSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 8),
    _TmnxVdoIfStatExtRxRtcpFbRepSumL_Type()
)
tmnxVdoIfStatExtRxRtcpFbRepSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpFbRepSumL.setStatus("current")
_TmnxVdoIfStatExtRxRtcpFbRepSumH_Type = Counter32
_TmnxVdoIfStatExtRxRtcpFbRepSumH_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpFbRepSumH = _TmnxVdoIfStatExtRxRtcpFbRepSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 9),
    _TmnxVdoIfStatExtRxRtcpFbRepSumH_Type()
)
tmnxVdoIfStatExtRxRtcpFbRepSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpFbRepSumH.setStatus("current")
_TmnxVdoIfStatExtRxRtcpFbReqSum_Type = Counter64
_TmnxVdoIfStatExtRxRtcpFbReqSum_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpFbReqSum = _TmnxVdoIfStatExtRxRtcpFbReqSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 10),
    _TmnxVdoIfStatExtRxRtcpFbReqSum_Type()
)
tmnxVdoIfStatExtRxRtcpFbReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpFbReqSum.setStatus("current")
_TmnxVdoIfStatExtRxRtcpFbReqSumL_Type = Counter32
_TmnxVdoIfStatExtRxRtcpFbReqSumL_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpFbReqSumL = _TmnxVdoIfStatExtRxRtcpFbReqSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 11),
    _TmnxVdoIfStatExtRxRtcpFbReqSumL_Type()
)
tmnxVdoIfStatExtRxRtcpFbReqSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpFbReqSumL.setStatus("current")
_TmnxVdoIfStatExtRxRtcpFbReqSumH_Type = Counter32
_TmnxVdoIfStatExtRxRtcpFbReqSumH_Object = MibTableColumn
tmnxVdoIfStatExtRxRtcpFbReqSumH = _TmnxVdoIfStatExtRxRtcpFbReqSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 12),
    _TmnxVdoIfStatExtRxRtcpFbReqSumH_Type()
)
tmnxVdoIfStatExtRxRtcpFbReqSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRtcpFbReqSumH.setStatus("current")
_TmnxVdoIfStatExtRxRudpFbRepSum_Type = Counter64
_TmnxVdoIfStatExtRxRudpFbRepSum_Object = MibTableColumn
tmnxVdoIfStatExtRxRudpFbRepSum = _TmnxVdoIfStatExtRxRudpFbRepSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 13),
    _TmnxVdoIfStatExtRxRudpFbRepSum_Type()
)
tmnxVdoIfStatExtRxRudpFbRepSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRudpFbRepSum.setStatus("current")
_TmnxVdoIfStatExtRxRudpFbRepSumL_Type = Counter32
_TmnxVdoIfStatExtRxRudpFbRepSumL_Object = MibTableColumn
tmnxVdoIfStatExtRxRudpFbRepSumL = _TmnxVdoIfStatExtRxRudpFbRepSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 14),
    _TmnxVdoIfStatExtRxRudpFbRepSumL_Type()
)
tmnxVdoIfStatExtRxRudpFbRepSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRudpFbRepSumL.setStatus("current")
_TmnxVdoIfStatExtRxRudpFbRepSumH_Type = Counter32
_TmnxVdoIfStatExtRxRudpFbRepSumH_Object = MibTableColumn
tmnxVdoIfStatExtRxRudpFbRepSumH = _TmnxVdoIfStatExtRxRudpFbRepSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 15),
    _TmnxVdoIfStatExtRxRudpFbRepSumH_Type()
)
tmnxVdoIfStatExtRxRudpFbRepSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtRxRudpFbRepSumH.setStatus("current")
_TmnxVdoIfStatExtTxFccPktsSum_Type = Counter64
_TmnxVdoIfStatExtTxFccPktsSum_Object = MibTableColumn
tmnxVdoIfStatExtTxFccPktsSum = _TmnxVdoIfStatExtTxFccPktsSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 16),
    _TmnxVdoIfStatExtTxFccPktsSum_Type()
)
tmnxVdoIfStatExtTxFccPktsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxFccPktsSum.setStatus("current")
_TmnxVdoIfStatExtTxFccPktsSumL_Type = Counter32
_TmnxVdoIfStatExtTxFccPktsSumL_Object = MibTableColumn
tmnxVdoIfStatExtTxFccPktsSumL = _TmnxVdoIfStatExtTxFccPktsSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 17),
    _TmnxVdoIfStatExtTxFccPktsSumL_Type()
)
tmnxVdoIfStatExtTxFccPktsSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxFccPktsSumL.setStatus("current")
_TmnxVdoIfStatExtTxFccPktsSumH_Type = Counter32
_TmnxVdoIfStatExtTxFccPktsSumH_Object = MibTableColumn
tmnxVdoIfStatExtTxFccPktsSumH = _TmnxVdoIfStatExtTxFccPktsSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 18),
    _TmnxVdoIfStatExtTxFccPktsSumH_Type()
)
tmnxVdoIfStatExtTxFccPktsSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxFccPktsSumH.setStatus("current")
_TmnxVdoIfStatExtTxFccOctetsSum_Type = Counter64
_TmnxVdoIfStatExtTxFccOctetsSum_Object = MibTableColumn
tmnxVdoIfStatExtTxFccOctetsSum = _TmnxVdoIfStatExtTxFccOctetsSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 19),
    _TmnxVdoIfStatExtTxFccOctetsSum_Type()
)
tmnxVdoIfStatExtTxFccOctetsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxFccOctetsSum.setStatus("current")
_TmnxVdoIfStatExtTxFccOctetsSumL_Type = Counter32
_TmnxVdoIfStatExtTxFccOctetsSumL_Object = MibTableColumn
tmnxVdoIfStatExtTxFccOctetsSumL = _TmnxVdoIfStatExtTxFccOctetsSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 20),
    _TmnxVdoIfStatExtTxFccOctetsSumL_Type()
)
tmnxVdoIfStatExtTxFccOctetsSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxFccOctetsSumL.setStatus("current")
_TmnxVdoIfStatExtTxFccOctetsSumH_Type = Counter32
_TmnxVdoIfStatExtTxFccOctetsSumH_Object = MibTableColumn
tmnxVdoIfStatExtTxFccOctetsSumH = _TmnxVdoIfStatExtTxFccOctetsSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 21),
    _TmnxVdoIfStatExtTxFccOctetsSumH_Type()
)
tmnxVdoIfStatExtTxFccOctetsSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxFccOctetsSumH.setStatus("current")
_TmnxVdoIfStatExtTxRetPktsSum_Type = Counter64
_TmnxVdoIfStatExtTxRetPktsSum_Object = MibTableColumn
tmnxVdoIfStatExtTxRetPktsSum = _TmnxVdoIfStatExtTxRetPktsSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 22),
    _TmnxVdoIfStatExtTxRetPktsSum_Type()
)
tmnxVdoIfStatExtTxRetPktsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRetPktsSum.setStatus("current")
_TmnxVdoIfStatExtTxRetPktsSumL_Type = Counter32
_TmnxVdoIfStatExtTxRetPktsSumL_Object = MibTableColumn
tmnxVdoIfStatExtTxRetPktsSumL = _TmnxVdoIfStatExtTxRetPktsSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 23),
    _TmnxVdoIfStatExtTxRetPktsSumL_Type()
)
tmnxVdoIfStatExtTxRetPktsSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRetPktsSumL.setStatus("current")
_TmnxVdoIfStatExtTxRetPktsSumH_Type = Counter32
_TmnxVdoIfStatExtTxRetPktsSumH_Object = MibTableColumn
tmnxVdoIfStatExtTxRetPktsSumH = _TmnxVdoIfStatExtTxRetPktsSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 24),
    _TmnxVdoIfStatExtTxRetPktsSumH_Type()
)
tmnxVdoIfStatExtTxRetPktsSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRetPktsSumH.setStatus("current")
_TmnxVdoIfStatExtTxRetOctetsSum_Type = Counter64
_TmnxVdoIfStatExtTxRetOctetsSum_Object = MibTableColumn
tmnxVdoIfStatExtTxRetOctetsSum = _TmnxVdoIfStatExtTxRetOctetsSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 25),
    _TmnxVdoIfStatExtTxRetOctetsSum_Type()
)
tmnxVdoIfStatExtTxRetOctetsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRetOctetsSum.setStatus("current")
_TmnxVdoIfStatExtTxRetOctetsSumL_Type = Counter32
_TmnxVdoIfStatExtTxRetOctetsSumL_Object = MibTableColumn
tmnxVdoIfStatExtTxRetOctetsSumL = _TmnxVdoIfStatExtTxRetOctetsSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 26),
    _TmnxVdoIfStatExtTxRetOctetsSumL_Type()
)
tmnxVdoIfStatExtTxRetOctetsSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRetOctetsSumL.setStatus("current")
_TmnxVdoIfStatExtTxRetOctetsSumH_Type = Counter32
_TmnxVdoIfStatExtTxRetOctetsSumH_Object = MibTableColumn
tmnxVdoIfStatExtTxRetOctetsSumH = _TmnxVdoIfStatExtTxRetOctetsSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 27),
    _TmnxVdoIfStatExtTxRetOctetsSumH_Type()
)
tmnxVdoIfStatExtTxRetOctetsSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRetOctetsSumH.setStatus("current")
_TmnxVdoIfStatExtTxRudpPktsSum_Type = Counter64
_TmnxVdoIfStatExtTxRudpPktsSum_Object = MibTableColumn
tmnxVdoIfStatExtTxRudpPktsSum = _TmnxVdoIfStatExtTxRudpPktsSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 28),
    _TmnxVdoIfStatExtTxRudpPktsSum_Type()
)
tmnxVdoIfStatExtTxRudpPktsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRudpPktsSum.setStatus("current")
_TmnxVdoIfStatExtTxRudpPktsSumL_Type = Counter32
_TmnxVdoIfStatExtTxRudpPktsSumL_Object = MibTableColumn
tmnxVdoIfStatExtTxRudpPktsSumL = _TmnxVdoIfStatExtTxRudpPktsSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 29),
    _TmnxVdoIfStatExtTxRudpPktsSumL_Type()
)
tmnxVdoIfStatExtTxRudpPktsSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRudpPktsSumL.setStatus("current")
_TmnxVdoIfStatExtTxRudpPktsSumH_Type = Counter32
_TmnxVdoIfStatExtTxRudpPktsSumH_Object = MibTableColumn
tmnxVdoIfStatExtTxRudpPktsSumH = _TmnxVdoIfStatExtTxRudpPktsSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 30),
    _TmnxVdoIfStatExtTxRudpPktsSumH_Type()
)
tmnxVdoIfStatExtTxRudpPktsSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRudpPktsSumH.setStatus("current")
_TmnxVdoIfStatExtTxRudpByteSum_Type = Counter64
_TmnxVdoIfStatExtTxRudpByteSum_Object = MibTableColumn
tmnxVdoIfStatExtTxRudpByteSum = _TmnxVdoIfStatExtTxRudpByteSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 31),
    _TmnxVdoIfStatExtTxRudpByteSum_Type()
)
tmnxVdoIfStatExtTxRudpByteSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRudpByteSum.setStatus("current")
_TmnxVdoIfStatExtTxRudpByteSumL_Type = Counter32
_TmnxVdoIfStatExtTxRudpByteSumL_Object = MibTableColumn
tmnxVdoIfStatExtTxRudpByteSumL = _TmnxVdoIfStatExtTxRudpByteSumL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 32),
    _TmnxVdoIfStatExtTxRudpByteSumL_Type()
)
tmnxVdoIfStatExtTxRudpByteSumL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRudpByteSumL.setStatus("current")
_TmnxVdoIfStatExtTxRudpByteSumH_Type = Counter32
_TmnxVdoIfStatExtTxRudpByteSumH_Object = MibTableColumn
tmnxVdoIfStatExtTxRudpByteSumH = _TmnxVdoIfStatExtTxRudpByteSumH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 17, 1, 33),
    _TmnxVdoIfStatExtTxRudpByteSumH_Type()
)
tmnxVdoIfStatExtTxRudpByteSumH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfStatExtTxRudpByteSumH.setStatus("current")
_TmnxVdoGrpSrcVqmStatTable_Object = MibTable
tmnxVdoGrpSrcVqmStatTable = _TmnxVdoGrpSrcVqmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmStatTable.setStatus("current")
_TmnxVdoGrpSrcVqmStatEntry_Object = MibTableRow
tmnxVdoGrpSrcVqmStatEntry = _TmnxVdoGrpSrcVqmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1)
)
tmnxVdoGrpSrcVqmStatEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGroupAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSourceAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmStatsPeriod"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmStatsTime"),
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmStatEntry.setStatus("current")
_TmnxVdoGrpSrcVqmStatsPeriod_Type = TmnxVdoStatInt
_TmnxVdoGrpSrcVqmStatsPeriod_Object = MibTableColumn
tmnxVdoGrpSrcVqmStatsPeriod = _TmnxVdoGrpSrcVqmStatsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 1),
    _TmnxVdoGrpSrcVqmStatsPeriod_Type()
)
tmnxVdoGrpSrcVqmStatsPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmStatsPeriod.setStatus("current")
_TmnxVdoGrpSrcVqmStatsTime_Type = Unsigned32
_TmnxVdoGrpSrcVqmStatsTime_Object = MibTableColumn
tmnxVdoGrpSrcVqmStatsTime = _TmnxVdoGrpSrcVqmStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 2),
    _TmnxVdoGrpSrcVqmStatsTime_Type()
)
tmnxVdoGrpSrcVqmStatsTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmStatsTime.setStatus("current")
_TmnxVdoGrpSrcVqmGoodSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmGoodSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmGoodSecs = _TmnxVdoGrpSrcVqmGoodSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 3),
    _TmnxVdoGrpSrcVqmGoodSecs_Type()
)
tmnxVdoGrpSrcVqmGoodSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmGoodSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmGoodSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmErrSecs = _TmnxVdoGrpSrcVqmErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 4),
    _TmnxVdoGrpSrcVqmErrSecs_Type()
)
tmnxVdoGrpSrcVqmErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmDegrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmDegrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmDegrSecs = _TmnxVdoGrpSrcVqmDegrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 5),
    _TmnxVdoGrpSrcVqmDegrSecs_Type()
)
tmnxVdoGrpSrcVqmDegrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmDegrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmDegrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmImpairSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmImpairSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmImpairSecs = _TmnxVdoGrpSrcVqmImpairSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 6),
    _TmnxVdoGrpSrcVqmImpairSecs_Type()
)
tmnxVdoGrpSrcVqmImpairSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmImpairSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmImpairSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPmtRepErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPmtRepErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPmtRepErrSecs = _TmnxVdoGrpSrcVqmPmtRepErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 7),
    _TmnxVdoGrpSrcVqmPmtRepErrSecs_Type()
)
tmnxVdoGrpSrcVqmPmtRepErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtRepErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtRepErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPmtRepDegSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPmtRepDegSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPmtRepDegSecs = _TmnxVdoGrpSrcVqmPmtRepDegSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 8),
    _TmnxVdoGrpSrcVqmPmtRepDegSecs_Type()
)
tmnxVdoGrpSrcVqmPmtRepDegSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtRepDegSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtRepDegSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPmtRepImpSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPmtRepImpSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPmtRepImpSecs = _TmnxVdoGrpSrcVqmPmtRepImpSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 9),
    _TmnxVdoGrpSrcVqmPmtRepImpSecs_Type()
)
tmnxVdoGrpSrcVqmPmtRepImpSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtRepImpSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtRepImpSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPmtSyntxErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPmtSyntxErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPmtSyntxErrSecs = _TmnxVdoGrpSrcVqmPmtSyntxErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 10),
    _TmnxVdoGrpSrcVqmPmtSyntxErrSecs_Type()
)
tmnxVdoGrpSrcVqmPmtSyntxErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtSyntxErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPmtSyntxErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPatRepErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPatRepErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPatRepErrSecs = _TmnxVdoGrpSrcVqmPatRepErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 11),
    _TmnxVdoGrpSrcVqmPatRepErrSecs_Type()
)
tmnxVdoGrpSrcVqmPatRepErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatRepErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatRepErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPatRepDegSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPatRepDegSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPatRepDegSecs = _TmnxVdoGrpSrcVqmPatRepDegSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 12),
    _TmnxVdoGrpSrcVqmPatRepDegSecs_Type()
)
tmnxVdoGrpSrcVqmPatRepDegSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatRepDegSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatRepDegSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPatRepImpSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPatRepImpSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPatRepImpSecs = _TmnxVdoGrpSrcVqmPatRepImpSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 13),
    _TmnxVdoGrpSrcVqmPatRepImpSecs_Type()
)
tmnxVdoGrpSrcVqmPatRepImpSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatRepImpSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatRepImpSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPatSyntxErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPatSyntxErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPatSyntxErrSecs = _TmnxVdoGrpSrcVqmPatSyntxErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 14),
    _TmnxVdoGrpSrcVqmPatSyntxErrSecs_Type()
)
tmnxVdoGrpSrcVqmPatSyntxErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatSyntxErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPatSyntxErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPcrRepErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPcrRepErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPcrRepErrSecs = _TmnxVdoGrpSrcVqmPcrRepErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 15),
    _TmnxVdoGrpSrcVqmPcrRepErrSecs_Type()
)
tmnxVdoGrpSrcVqmPcrRepErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPcrRepErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPcrRepErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPcrRepDegSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPcrRepDegSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPcrRepDegSecs = _TmnxVdoGrpSrcVqmPcrRepDegSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 16),
    _TmnxVdoGrpSrcVqmPcrRepDegSecs_Type()
)
tmnxVdoGrpSrcVqmPcrRepDegSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPcrRepDegSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPcrRepDegSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmPcrRepImpSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmPcrRepImpSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmPcrRepImpSecs = _TmnxVdoGrpSrcVqmPcrRepImpSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 17),
    _TmnxVdoGrpSrcVqmPcrRepImpSecs_Type()
)
tmnxVdoGrpSrcVqmPcrRepImpSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPcrRepImpSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmPcrRepImpSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmSyncByteErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmSyncByteErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmSyncByteErrSecs = _TmnxVdoGrpSrcVqmSyncByteErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 18),
    _TmnxVdoGrpSrcVqmSyncByteErrSecs_Type()
)
tmnxVdoGrpSrcVqmSyncByteErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmSyncByteErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmSyncByteErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmSyncLossSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmSyncLossSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmSyncLossSecs = _TmnxVdoGrpSrcVqmSyncLossSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 19),
    _TmnxVdoGrpSrcVqmSyncLossSecs_Type()
)
tmnxVdoGrpSrcVqmSyncLossSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmSyncLossSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmSyncLossSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmCatErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmCatErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmCatErrSecs = _TmnxVdoGrpSrcVqmCatErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 20),
    _TmnxVdoGrpSrcVqmCatErrSecs_Type()
)
tmnxVdoGrpSrcVqmCatErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmCatErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmCatErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmUnrefPidErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmUnrefPidErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmUnrefPidErrSecs = _TmnxVdoGrpSrcVqmUnrefPidErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 21),
    _TmnxVdoGrpSrcVqmUnrefPidErrSecs_Type()
)
tmnxVdoGrpSrcVqmUnrefPidErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmUnrefPidErrSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmUnrefPidErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmMDIDelayFactor_Type = Unsigned32
_TmnxVdoGrpSrcVqmMDIDelayFactor_Object = MibTableColumn
tmnxVdoGrpSrcVqmMDIDelayFactor = _TmnxVdoGrpSrcVqmMDIDelayFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 22),
    _TmnxVdoGrpSrcVqmMDIDelayFactor_Type()
)
tmnxVdoGrpSrcVqmMDIDelayFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMDIDelayFactor.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMDIDelayFactor.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmMDILossRate_Type = TmnxMDILossRate
_TmnxVdoGrpSrcVqmMDILossRate_Object = MibTableColumn
tmnxVdoGrpSrcVqmMDILossRate = _TmnxVdoGrpSrcVqmMDILossRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 23),
    _TmnxVdoGrpSrcVqmMDILossRate_Type()
)
tmnxVdoGrpSrcVqmMDILossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMDILossRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMDILossRate.setUnits("TS/sec")
_TmnxVdoGrpSrcVqmMinGOPLength_Type = Unsigned32
_TmnxVdoGrpSrcVqmMinGOPLength_Object = MibTableColumn
tmnxVdoGrpSrcVqmMinGOPLength = _TmnxVdoGrpSrcVqmMinGOPLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 24),
    _TmnxVdoGrpSrcVqmMinGOPLength_Type()
)
tmnxVdoGrpSrcVqmMinGOPLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMinGOPLength.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMinGOPLength.setUnits("pictures")
_TmnxVdoGrpSrcVqmMinFrmPerSec_Type = Unsigned32
_TmnxVdoGrpSrcVqmMinFrmPerSec_Object = MibTableColumn
tmnxVdoGrpSrcVqmMinFrmPerSec = _TmnxVdoGrpSrcVqmMinFrmPerSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 25),
    _TmnxVdoGrpSrcVqmMinFrmPerSec_Type()
)
tmnxVdoGrpSrcVqmMinFrmPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMinFrmPerSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMinFrmPerSec.setUnits("fps")
_TmnxVdoGrpSrcVqmAvgGOPLength_Type = Unsigned32
_TmnxVdoGrpSrcVqmAvgGOPLength_Object = MibTableColumn
tmnxVdoGrpSrcVqmAvgGOPLength = _TmnxVdoGrpSrcVqmAvgGOPLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 26),
    _TmnxVdoGrpSrcVqmAvgGOPLength_Type()
)
tmnxVdoGrpSrcVqmAvgGOPLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmAvgGOPLength.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmAvgGOPLength.setUnits("pictures")
_TmnxVdoGrpSrcVqmAvgFrmPerSec_Type = Unsigned32
_TmnxVdoGrpSrcVqmAvgFrmPerSec_Object = MibTableColumn
tmnxVdoGrpSrcVqmAvgFrmPerSec = _TmnxVdoGrpSrcVqmAvgFrmPerSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 27),
    _TmnxVdoGrpSrcVqmAvgFrmPerSec_Type()
)
tmnxVdoGrpSrcVqmAvgFrmPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmAvgFrmPerSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmAvgFrmPerSec.setUnits("fps")
_TmnxVdoGrpSrcVqmMaxGOPLength_Type = Unsigned32
_TmnxVdoGrpSrcVqmMaxGOPLength_Object = MibTableColumn
tmnxVdoGrpSrcVqmMaxGOPLength = _TmnxVdoGrpSrcVqmMaxGOPLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 28),
    _TmnxVdoGrpSrcVqmMaxGOPLength_Type()
)
tmnxVdoGrpSrcVqmMaxGOPLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMaxGOPLength.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMaxGOPLength.setUnits("pictures")
_TmnxVdoGrpSrcVqmMaxFrmPerSec_Type = Unsigned32
_TmnxVdoGrpSrcVqmMaxFrmPerSec_Object = MibTableColumn
tmnxVdoGrpSrcVqmMaxFrmPerSec = _TmnxVdoGrpSrcVqmMaxFrmPerSec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 29),
    _TmnxVdoGrpSrcVqmMaxFrmPerSec_Type()
)
tmnxVdoGrpSrcVqmMaxFrmPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMaxFrmPerSec.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmMaxFrmPerSec.setUnits("fps")
_TmnxVdoGrpSrcVqmGoodIFrames_Type = Unsigned32
_TmnxVdoGrpSrcVqmGoodIFrames_Object = MibTableColumn
tmnxVdoGrpSrcVqmGoodIFrames = _TmnxVdoGrpSrcVqmGoodIFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 30),
    _TmnxVdoGrpSrcVqmGoodIFrames_Type()
)
tmnxVdoGrpSrcVqmGoodIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmGoodIFrames.setStatus("current")
_TmnxVdoGrpSrcVqmBadIFrames_Type = Unsigned32
_TmnxVdoGrpSrcVqmBadIFrames_Object = MibTableColumn
tmnxVdoGrpSrcVqmBadIFrames = _TmnxVdoGrpSrcVqmBadIFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 31),
    _TmnxVdoGrpSrcVqmBadIFrames_Type()
)
tmnxVdoGrpSrcVqmBadIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmBadIFrames.setStatus("current")
_TmnxVdoGrpSrcVqmGoodPFrames_Type = Unsigned32
_TmnxVdoGrpSrcVqmGoodPFrames_Object = MibTableColumn
tmnxVdoGrpSrcVqmGoodPFrames = _TmnxVdoGrpSrcVqmGoodPFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 32),
    _TmnxVdoGrpSrcVqmGoodPFrames_Type()
)
tmnxVdoGrpSrcVqmGoodPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmGoodPFrames.setStatus("current")
_TmnxVdoGrpSrcVqmBadPFrames_Type = Unsigned32
_TmnxVdoGrpSrcVqmBadPFrames_Object = MibTableColumn
tmnxVdoGrpSrcVqmBadPFrames = _TmnxVdoGrpSrcVqmBadPFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 33),
    _TmnxVdoGrpSrcVqmBadPFrames_Type()
)
tmnxVdoGrpSrcVqmBadPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmBadPFrames.setStatus("current")
_TmnxVdoGrpSrcVqmGoodBFrames_Type = Unsigned32
_TmnxVdoGrpSrcVqmGoodBFrames_Object = MibTableColumn
tmnxVdoGrpSrcVqmGoodBFrames = _TmnxVdoGrpSrcVqmGoodBFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 34),
    _TmnxVdoGrpSrcVqmGoodBFrames_Type()
)
tmnxVdoGrpSrcVqmGoodBFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmGoodBFrames.setStatus("current")
_TmnxVdoGrpSrcVqmBadBFrames_Type = Unsigned32
_TmnxVdoGrpSrcVqmBadBFrames_Object = MibTableColumn
tmnxVdoGrpSrcVqmBadBFrames = _TmnxVdoGrpSrcVqmBadBFrames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 35),
    _TmnxVdoGrpSrcVqmBadBFrames_Type()
)
tmnxVdoGrpSrcVqmBadBFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmBadBFrames.setStatus("current")
_TmnxVdoGrpSrcVqmTrafficLossSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmTrafficLossSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmTrafficLossSecs = _TmnxVdoGrpSrcVqmTrafficLossSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 36),
    _TmnxVdoGrpSrcVqmTrafficLossSecs_Type()
)
tmnxVdoGrpSrcVqmTrafficLossSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmTrafficLossSecs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmTrafficLossSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmSCTE35ErrSecs_Type = Unsigned32
_TmnxVdoGrpSrcVqmSCTE35ErrSecs_Object = MibTableColumn
tmnxVdoGrpSrcVqmSCTE35ErrSecs = _TmnxVdoGrpSrcVqmSCTE35ErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 18, 1, 37),
    _TmnxVdoGrpSrcVqmSCTE35ErrSecs_Type()
)
tmnxVdoGrpSrcVqmSCTE35ErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmSCTE35ErrSecs.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmSCTE35ErrSecs.setUnits("seconds")
_TmnxVdoGrpSrcVqmTable_Object = MibTable
tmnxVdoGrpSrcVqmTable = _TmnxVdoGrpSrcVqmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmTable.setStatus("current")
_TmnxVdoGrpSrcVqmEntry_Object = MibTableRow
tmnxVdoGrpSrcVqmEntry = _TmnxVdoGrpSrcVqmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1)
)
tmnxVdoGrpSrcVqmEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoIfName"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGrpAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcGroupAddress"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSrcAddrType"),
    (0, "TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmEntry.setStatus("current")
_TmnxVdoGrpSrcVqmOperAnalyzerSt_Type = TruthValue
_TmnxVdoGrpSrcVqmOperAnalyzerSt_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperAnalyzerSt = _TmnxVdoGrpSrcVqmOperAnalyzerSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 1),
    _TmnxVdoGrpSrcVqmOperAnalyzerSt_Type()
)
tmnxVdoGrpSrcVqmOperAnalyzerSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperAnalyzerSt.setStatus("current")
_TmnxVdoGrpSrcVqmOperCcError_Type = TruthValue
_TmnxVdoGrpSrcVqmOperCcError_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperCcError = _TmnxVdoGrpSrcVqmOperCcError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 2),
    _TmnxVdoGrpSrcVqmOperCcError_Type()
)
tmnxVdoGrpSrcVqmOperCcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperCcError.setStatus("current")
_TmnxVdoGrpSrcVqmOperPatRepError_Type = TruthValue
_TmnxVdoGrpSrcVqmOperPatRepError_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPatRepError = _TmnxVdoGrpSrcVqmOperPatRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 3),
    _TmnxVdoGrpSrcVqmOperPatRepError_Type()
)
tmnxVdoGrpSrcVqmOperPatRepError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPatRepError.setStatus("current")
_TmnxVdoGrpSrcVqmOperTncPatRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperTncPatRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperTncPatRep = _TmnxVdoGrpSrcVqmOperTncPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 4),
    _TmnxVdoGrpSrcVqmOperTncPatRep_Type()
)
tmnxVdoGrpSrcVqmOperTncPatRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTncPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTncPatRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperQosPatRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperQosPatRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperQosPatRep = _TmnxVdoGrpSrcVqmOperQosPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 5),
    _TmnxVdoGrpSrcVqmOperQosPatRep_Type()
)
tmnxVdoGrpSrcVqmOperQosPatRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperQosPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperQosPatRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperPoaPatRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperPoaPatRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPoaPatRep = _TmnxVdoGrpSrcVqmOperPoaPatRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 6),
    _TmnxVdoGrpSrcVqmOperPoaPatRep_Type()
)
tmnxVdoGrpSrcVqmOperPoaPatRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPoaPatRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPoaPatRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperPatSyntax_Type = TruthValue
_TmnxVdoGrpSrcVqmOperPatSyntax_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPatSyntax = _TmnxVdoGrpSrcVqmOperPatSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 7),
    _TmnxVdoGrpSrcVqmOperPatSyntax_Type()
)
tmnxVdoGrpSrcVqmOperPatSyntax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPatSyntax.setStatus("current")
_TmnxVdoGrpSrcVqmOperPcrRepError_Type = TruthValue
_TmnxVdoGrpSrcVqmOperPcrRepError_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPcrRepError = _TmnxVdoGrpSrcVqmOperPcrRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 8),
    _TmnxVdoGrpSrcVqmOperPcrRepError_Type()
)
tmnxVdoGrpSrcVqmOperPcrRepError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPcrRepError.setStatus("current")
_TmnxVdoGrpSrcVqmOperTncPcrRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperTncPcrRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperTncPcrRep = _TmnxVdoGrpSrcVqmOperTncPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 9),
    _TmnxVdoGrpSrcVqmOperTncPcrRep_Type()
)
tmnxVdoGrpSrcVqmOperTncPcrRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTncPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTncPcrRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperQosPcrRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperQosPcrRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperQosPcrRep = _TmnxVdoGrpSrcVqmOperQosPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 10),
    _TmnxVdoGrpSrcVqmOperQosPcrRep_Type()
)
tmnxVdoGrpSrcVqmOperQosPcrRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperQosPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperQosPcrRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperPoaPcrRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperPoaPcrRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPoaPcrRep = _TmnxVdoGrpSrcVqmOperPoaPcrRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 11),
    _TmnxVdoGrpSrcVqmOperPoaPcrRep_Type()
)
tmnxVdoGrpSrcVqmOperPoaPcrRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPoaPcrRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPoaPcrRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperVidPIDAbs_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperVidPIDAbs_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperVidPIDAbs = _TmnxVdoGrpSrcVqmOperVidPIDAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 12),
    _TmnxVdoGrpSrcVqmOperVidPIDAbs_Type()
)
tmnxVdoGrpSrcVqmOperVidPIDAbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperVidPIDAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperVidPIDAbs.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperPIDPmtUnref_Type = TruthValue
_TmnxVdoGrpSrcVqmOperPIDPmtUnref_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPIDPmtUnref = _TmnxVdoGrpSrcVqmOperPIDPmtUnref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 13),
    _TmnxVdoGrpSrcVqmOperPIDPmtUnref_Type()
)
tmnxVdoGrpSrcVqmOperPIDPmtUnref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPIDPmtUnref.setStatus("current")
_TmnxVdoGrpSrcVqmOperPmtRepError_Type = TruthValue
_TmnxVdoGrpSrcVqmOperPmtRepError_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPmtRepError = _TmnxVdoGrpSrcVqmOperPmtRepError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 14),
    _TmnxVdoGrpSrcVqmOperPmtRepError_Type()
)
tmnxVdoGrpSrcVqmOperPmtRepError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPmtRepError.setStatus("current")
_TmnxVdoGrpSrcVqmOperTncPmtRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperTncPmtRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperTncPmtRep = _TmnxVdoGrpSrcVqmOperTncPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 15),
    _TmnxVdoGrpSrcVqmOperTncPmtRep_Type()
)
tmnxVdoGrpSrcVqmOperTncPmtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTncPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTncPmtRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperQosPmtRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperQosPmtRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperQosPmtRep = _TmnxVdoGrpSrcVqmOperQosPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 16),
    _TmnxVdoGrpSrcVqmOperQosPmtRep_Type()
)
tmnxVdoGrpSrcVqmOperQosPmtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperQosPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperQosPmtRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperPoaPmtRep_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperPoaPmtRep_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPoaPmtRep = _TmnxVdoGrpSrcVqmOperPoaPmtRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 17),
    _TmnxVdoGrpSrcVqmOperPoaPmtRep_Type()
)
tmnxVdoGrpSrcVqmOperPoaPmtRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPoaPmtRep.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPoaPmtRep.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperPmtSyntax_Type = TruthValue
_TmnxVdoGrpSrcVqmOperPmtSyntax_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperPmtSyntax = _TmnxVdoGrpSrcVqmOperPmtSyntax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 18),
    _TmnxVdoGrpSrcVqmOperPmtSyntax_Type()
)
tmnxVdoGrpSrcVqmOperPmtSyntax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperPmtSyntax.setStatus("current")
_TmnxVdoGrpSrcVqmOperSCTE35Error_Type = TruthValue
_TmnxVdoGrpSrcVqmOperSCTE35Error_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperSCTE35Error = _TmnxVdoGrpSrcVqmOperSCTE35Error_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 19),
    _TmnxVdoGrpSrcVqmOperSCTE35Error_Type()
)
tmnxVdoGrpSrcVqmOperSCTE35Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperSCTE35Error.setStatus("current")
_TmnxVdoGrpSrcVqmOperTeiError_Type = TruthValue
_TmnxVdoGrpSrcVqmOperTeiError_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperTeiError = _TmnxVdoGrpSrcVqmOperTeiError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 20),
    _TmnxVdoGrpSrcVqmOperTeiError_Type()
)
tmnxVdoGrpSrcVqmOperTeiError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTeiError.setStatus("current")
_TmnxVdoGrpSrcVqmOperTsSyncLoss_Type = TruthValue
_TmnxVdoGrpSrcVqmOperTsSyncLoss_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperTsSyncLoss = _TmnxVdoGrpSrcVqmOperTsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 21),
    _TmnxVdoGrpSrcVqmOperTsSyncLoss_Type()
)
tmnxVdoGrpSrcVqmOperTsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperTsSyncLoss.setStatus("current")
_TmnxVdoGrpSrcVqmOperNonVidPIDAbs_Type = Unsigned32
_TmnxVdoGrpSrcVqmOperNonVidPIDAbs_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperNonVidPIDAbs = _TmnxVdoGrpSrcVqmOperNonVidPIDAbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 22),
    _TmnxVdoGrpSrcVqmOperNonVidPIDAbs_Type()
)
tmnxVdoGrpSrcVqmOperNonVidPIDAbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperNonVidPIDAbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperNonVidPIDAbs.setUnits("milliseconds")
_TmnxVdoGrpSrcVqmOperReportAlarm_Type = TmnxVdoAnalyzerAlarm
_TmnxVdoGrpSrcVqmOperReportAlarm_Object = MibTableColumn
tmnxVdoGrpSrcVqmOperReportAlarm = _TmnxVdoGrpSrcVqmOperReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 19, 1, 23),
    _TmnxVdoGrpSrcVqmOperReportAlarm_Type()
)
tmnxVdoGrpSrcVqmOperReportAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcVqmOperReportAlarm.setStatus("current")
_TmnxVdoGrpSrcStatExtTable_Object = MibTable
tmnxVdoGrpSrcStatExtTable = _TmnxVdoGrpSrcStatExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStatExtTable.setStatus("current")
_TmnxVdoGrpSrcStatExtEntry_Object = MibTableRow
tmnxVdoGrpSrcStatExtEntry = _TmnxVdoGrpSrcStatExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcStatExtEntry.setStatus("current")
_TmnxVdoGrpSrcExtMaxRtpTsDelta_Type = Counter32
_TmnxVdoGrpSrcExtMaxRtpTsDelta_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxRtpTsDelta = _TmnxVdoGrpSrcExtMaxRtpTsDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 1),
    _TmnxVdoGrpSrcExtMaxRtpTsDelta_Type()
)
tmnxVdoGrpSrcExtMaxRtpTsDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxRtpTsDelta.setStatus("current")
_TmnxVdoGrpSrcExtMaxTicksDelta_Type = Counter64
_TmnxVdoGrpSrcExtMaxTicksDelta_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxTicksDelta = _TmnxVdoGrpSrcExtMaxTicksDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 2),
    _TmnxVdoGrpSrcExtMaxTicksDelta_Type()
)
tmnxVdoGrpSrcExtMaxTicksDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxTicksDelta.setStatus("current")
_TmnxVdoGrpSrcExtMaxTicksDeltaL32_Type = Counter32
_TmnxVdoGrpSrcExtMaxTicksDeltaL32_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxTicksDeltaL32 = _TmnxVdoGrpSrcExtMaxTicksDeltaL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 3),
    _TmnxVdoGrpSrcExtMaxTicksDeltaL32_Type()
)
tmnxVdoGrpSrcExtMaxTicksDeltaL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxTicksDeltaL32.setStatus("current")
_TmnxVdoGrpSrcExtMaxTicksDeltaH32_Type = Counter32
_TmnxVdoGrpSrcExtMaxTicksDeltaH32_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxTicksDeltaH32 = _TmnxVdoGrpSrcExtMaxTicksDeltaH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 4),
    _TmnxVdoGrpSrcExtMaxTicksDeltaH32_Type()
)
tmnxVdoGrpSrcExtMaxTicksDeltaH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxTicksDeltaH32.setStatus("current")
_TmnxVdoGrpSrcExtCurTsJitter_Type = Counter64
_TmnxVdoGrpSrcExtCurTsJitter_Object = MibTableColumn
tmnxVdoGrpSrcExtCurTsJitter = _TmnxVdoGrpSrcExtCurTsJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 5),
    _TmnxVdoGrpSrcExtCurTsJitter_Type()
)
tmnxVdoGrpSrcExtCurTsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtCurTsJitter.setStatus("current")
_TmnxVdoGrpSrcExtCurTsJitterL32_Type = Counter32
_TmnxVdoGrpSrcExtCurTsJitterL32_Object = MibTableColumn
tmnxVdoGrpSrcExtCurTsJitterL32 = _TmnxVdoGrpSrcExtCurTsJitterL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 6),
    _TmnxVdoGrpSrcExtCurTsJitterL32_Type()
)
tmnxVdoGrpSrcExtCurTsJitterL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtCurTsJitterL32.setStatus("current")
_TmnxVdoGrpSrcExtCurTsJitterH32_Type = Counter32
_TmnxVdoGrpSrcExtCurTsJitterH32_Object = MibTableColumn
tmnxVdoGrpSrcExtCurTsJitterH32 = _TmnxVdoGrpSrcExtCurTsJitterH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 7),
    _TmnxVdoGrpSrcExtCurTsJitterH32_Type()
)
tmnxVdoGrpSrcExtCurTsJitterH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtCurTsJitterH32.setStatus("current")
_TmnxVdoGrpSrcExtMaxTsJitter_Type = Counter64
_TmnxVdoGrpSrcExtMaxTsJitter_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxTsJitter = _TmnxVdoGrpSrcExtMaxTsJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 8),
    _TmnxVdoGrpSrcExtMaxTsJitter_Type()
)
tmnxVdoGrpSrcExtMaxTsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxTsJitter.setStatus("current")
_TmnxVdoGrpSrcExtMaxTsJitterL32_Type = Counter32
_TmnxVdoGrpSrcExtMaxTsJitterL32_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxTsJitterL32 = _TmnxVdoGrpSrcExtMaxTsJitterL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 9),
    _TmnxVdoGrpSrcExtMaxTsJitterL32_Type()
)
tmnxVdoGrpSrcExtMaxTsJitterL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxTsJitterL32.setStatus("current")
_TmnxVdoGrpSrcExtMaxTsJitterH32_Type = Counter32
_TmnxVdoGrpSrcExtMaxTsJitterH32_Object = MibTableColumn
tmnxVdoGrpSrcExtMaxTsJitterH32 = _TmnxVdoGrpSrcExtMaxTsJitterH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 1, 20, 1, 10),
    _TmnxVdoGrpSrcExtMaxTsJitterH32_Type()
)
tmnxVdoGrpSrcExtMaxTsJitterH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcExtMaxTsJitterH32.setStatus("current")
_TmnxVdoGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxVdoGlobalObjs = _TmnxVdoGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2)
)
_TmnxVdoIfTableLastChanged_Type = TimeStamp
_TmnxVdoIfTableLastChanged_Object = MibScalar
tmnxVdoIfTableLastChanged = _TmnxVdoIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 1),
    _TmnxVdoIfTableLastChanged_Type()
)
tmnxVdoIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfTableLastChanged.setStatus("current")
_TmnxVdoIfAddrTableLastChanged_Type = TimeStamp
_TmnxVdoIfAddrTableLastChanged_Object = MibScalar
tmnxVdoIfAddrTableLastChanged = _TmnxVdoIfAddrTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 2),
    _TmnxVdoIfAddrTableLastChanged_Type()
)
tmnxVdoIfAddrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfAddrTableLastChanged.setStatus("current")
_TmnxVdoGrpTableLastChanged_Type = TimeStamp
_TmnxVdoGrpTableLastChanged_Object = MibScalar
tmnxVdoGrpTableLastChanged = _TmnxVdoGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 3),
    _TmnxVdoGrpTableLastChanged_Type()
)
tmnxVdoGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpTableLastChanged.setStatus("current")
_TmnxVdoGrpMDATableLastChanged_Type = TimeStamp
_TmnxVdoGrpMDATableLastChanged_Object = MibScalar
tmnxVdoGrpMDATableLastChanged = _TmnxVdoGrpMDATableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 4),
    _TmnxVdoGrpMDATableLastChanged_Type()
)
tmnxVdoGrpMDATableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoGrpMDATableLastChanged.setStatus("current")
_TmnxVdoAdiChlTableLastChanged_Type = TimeStamp
_TmnxVdoAdiChlTableLastChanged_Object = MibScalar
tmnxVdoAdiChlTableLastChanged = _TmnxVdoAdiChlTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 5),
    _TmnxVdoAdiChlTableLastChanged_Type()
)
tmnxVdoAdiChlTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoAdiChlTableLastChanged.setStatus("current")
_TmnxVdoAdiZoneChlTableLastChngd_Type = TimeStamp
_TmnxVdoAdiZoneChlTableLastChngd_Object = MibScalar
tmnxVdoAdiZoneChlTableLastChngd = _TmnxVdoAdiZoneChlTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 6),
    _TmnxVdoAdiZoneChlTableLastChngd_Type()
)
tmnxVdoAdiZoneChlTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoAdiZoneChlTableLastChngd.setStatus("current")
_TmnxVdoIfScte30AdSrvrTblLstChngd_Type = TimeStamp
_TmnxVdoIfScte30AdSrvrTblLstChngd_Object = MibScalar
tmnxVdoIfScte30AdSrvrTblLstChngd = _TmnxVdoIfScte30AdSrvrTblLstChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 2, 7),
    _TmnxVdoIfScte30AdSrvrTblLstChngd_Type()
)
tmnxVdoIfScte30AdSrvrTblLstChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVdoIfScte30AdSrvrTblLstChngd.setStatus("current")
_TmnxVdoNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxVdoNotificationObjs = _TmnxVdoNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3)
)
_TmnxVdoNotifysvcId_Type = TmnxServId
_TmnxVdoNotifysvcId_Object = MibScalar
tmnxVdoNotifysvcId = _TmnxVdoNotifysvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 1),
    _TmnxVdoNotifysvcId_Type()
)
tmnxVdoNotifysvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifysvcId.setStatus("current")
_TmnxVdoNotifyIfName_Type = TmnxVdoIfName
_TmnxVdoNotifyIfName_Object = MibScalar
tmnxVdoNotifyIfName = _TmnxVdoNotifyIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 2),
    _TmnxVdoNotifyIfName_Type()
)
tmnxVdoNotifyIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyIfName.setStatus("current")
_TmnxVdoNotifyGrpAddrType_Type = InetAddressType
_TmnxVdoNotifyGrpAddrType_Object = MibScalar
tmnxVdoNotifyGrpAddrType = _TmnxVdoNotifyGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 3),
    _TmnxVdoNotifyGrpAddrType_Type()
)
tmnxVdoNotifyGrpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyGrpAddrType.setStatus("current")
_TmnxVdoNotifyGroupAddress_Type = InetAddress
_TmnxVdoNotifyGroupAddress_Object = MibScalar
tmnxVdoNotifyGroupAddress = _TmnxVdoNotifyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 4),
    _TmnxVdoNotifyGroupAddress_Type()
)
tmnxVdoNotifyGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyGroupAddress.setStatus("current")
_TmnxVdoNotifySrcAddrType_Type = InetAddressType
_TmnxVdoNotifySrcAddrType_Object = MibScalar
tmnxVdoNotifySrcAddrType = _TmnxVdoNotifySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 5),
    _TmnxVdoNotifySrcAddrType_Type()
)
tmnxVdoNotifySrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifySrcAddrType.setStatus("current")
_TmnxVdoNotifySourceAddress_Type = InetAddress
_TmnxVdoNotifySourceAddress_Object = MibScalar
tmnxVdoNotifySourceAddress = _TmnxVdoNotifySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 6),
    _TmnxVdoNotifySourceAddress_Type()
)
tmnxVdoNotifySourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifySourceAddress.setStatus("current")
_TmnxVdoNotifyAdSpliceSessionId_Type = Unsigned32
_TmnxVdoNotifyAdSpliceSessionId_Object = MibScalar
tmnxVdoNotifyAdSpliceSessionId = _TmnxVdoNotifyAdSpliceSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 7),
    _TmnxVdoNotifyAdSpliceSessionId_Type()
)
tmnxVdoNotifyAdSpliceSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyAdSpliceSessionId.setStatus("current")


class _TmnxVdoNotifyAdSpliceAbortTime_Type(DateAndTime):
    """Custom type tmnxVdoNotifyAdSpliceAbortTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxVdoNotifyAdSpliceAbortTime_Type.__name__ = "DateAndTime"
_TmnxVdoNotifyAdSpliceAbortTime_Object = MibScalar
tmnxVdoNotifyAdSpliceAbortTime = _TmnxVdoNotifyAdSpliceAbortTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 8),
    _TmnxVdoNotifyAdSpliceAbortTime_Type()
)
tmnxVdoNotifyAdSpliceAbortTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyAdSpliceAbortTime.setStatus("current")
_TmnxVdoNotifyAdSpliceDuration_Type = Unsigned32
_TmnxVdoNotifyAdSpliceDuration_Object = MibScalar
tmnxVdoNotifyAdSpliceDuration = _TmnxVdoNotifyAdSpliceDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 9),
    _TmnxVdoNotifyAdSpliceDuration_Type()
)
tmnxVdoNotifyAdSpliceDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyAdSpliceDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxVdoNotifyAdSpliceDuration.setUnits("seconds")
_TmnxVdoNotifyClientAddrType_Type = InetAddressType
_TmnxVdoNotifyClientAddrType_Object = MibScalar
tmnxVdoNotifyClientAddrType = _TmnxVdoNotifyClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 10),
    _TmnxVdoNotifyClientAddrType_Type()
)
tmnxVdoNotifyClientAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyClientAddrType.setStatus("current")
_TmnxVdoNotifyClientAddress_Type = InetAddress
_TmnxVdoNotifyClientAddress_Object = MibScalar
tmnxVdoNotifyClientAddress = _TmnxVdoNotifyClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 11),
    _TmnxVdoNotifyClientAddress_Type()
)
tmnxVdoNotifyClientAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyClientAddress.setStatus("current")
_TmnxVdoNotifyAnalyzerState_Type = TmnxVdoAnalyzerAlarmStates
_TmnxVdoNotifyAnalyzerState_Object = MibScalar
tmnxVdoNotifyAnalyzerState = _TmnxVdoNotifyAnalyzerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 61, 3, 12),
    _TmnxVdoNotifyAnalyzerState_Type()
)
tmnxVdoNotifyAnalyzerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxVdoNotifyAnalyzerState.setStatus("current")
_TmnxVdoNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxVdoNotifyPrefix = _TmnxVdoNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61)
)
_TmnxVdoNotifications_ObjectIdentity = ObjectIdentity
tmnxVdoNotifications = _TmnxVdoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0)
)
tmnxVdoGrpSrcStatEntry.registerAugmentions(
    ("TIMETRA-VIDEO-MIB",
     "tmnxVdoSGStatV1Entry")
)
tmnxVdoSGStatV1Entry.setIndexNames(*tmnxVdoGrpSrcStatEntry.getIndexNames())
tmnxVdoIfAddrEntry.registerAugmentions(
    ("TIMETRA-VIDEO-MIB",
     "tmnxVdoIfStatEntry")
)
tmnxVdoIfStatEntry.setIndexNames(*tmnxVdoIfAddrEntry.getIndexNames())
tmnxVdoIfAddrEntry.registerAugmentions(
    ("TIMETRA-VIDEO-MIB",
     "tmnxVdoIfStLowEntry")
)
tmnxVdoIfStLowEntry.setIndexNames(*tmnxVdoIfAddrEntry.getIndexNames())
tmnxVdoIfAddrEntry.registerAugmentions(
    ("TIMETRA-VIDEO-MIB",
     "tmnxVdoIfStHghEntry")
)
tmnxVdoIfStHghEntry.setIndexNames(*tmnxVdoIfAddrEntry.getIndexNames())
tmnxVdoIfAddrEntry.registerAugmentions(
    ("TIMETRA-VIDEO-MIB",
     "tmnxVdoIfStatExtEntry")
)
tmnxVdoIfStatExtEntry.setIndexNames(*tmnxVdoIfAddrEntry.getIndexNames())
tmnxVdoGrpSrcStatEntry.registerAugmentions(
    ("TIMETRA-VIDEO-MIB",
     "tmnxVdoGrpSrcStatExtEntry")
)
tmnxVdoGrpSrcStatExtEntry.setIndexNames(*tmnxVdoGrpSrcStatEntry.getIndexNames())

# Managed Objects groups

tmnxVdoGlobalV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 1)
)
tmnxVdoGlobalV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoIfTableLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpTableLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMDATableLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfAddrTableLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlTableLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlTableLastChngd"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30AdSrvrTblLstChngd"))
)
if mibBuilder.loadTexts:
    tmnxVdoGlobalV7v0Group.setStatus("current")

tmnxVdoIfV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 2)
)
tmnxVdoIfV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoIfRowStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfOperState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfDescription"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfVdoGrpId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfVrtrIfIndex"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfIngressQosPolicyId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfEgressQosPolicyId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfAddrRowStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfAdi"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfRTClientAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfRTClientAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfGatewayAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfGatewayAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfMcastSvcId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfIngressIpFilterId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfIngressMacFilterId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfEgressIpFilterId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfEgressMacFilterId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30ControlAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30ControlAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30DataAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30DataAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfSapId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfMcastProtocol"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfSessions"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfCpmProtectPolicyId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30AdSrvrRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxVdoIfV7v0Group.setStatus("current")

tmnxVdoGrpV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 3)
)
tmnxVdoGrpV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpDescription"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpOperState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpLocalRTServerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpFCCServerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpADIServerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpRowStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpLastChanged"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRowStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaOperState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaUsedMemory"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaAvailableMemory"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaChannels"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaChannelAllocFails"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMaxBwExceeded"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaBwInUse"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaActiveRtcpSessions"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaEgressStreamResets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaIngressStreamResets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaAdStreamResets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaAdStreamAborts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaSsrcCollisions"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataOctets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataOctetsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataOctetsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataPacketErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataPktErrsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRxDataPktErrsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataOctets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataOctetsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataOctetsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataPacketErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataPktErrsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxDataPktErrsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRtcpParseErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRtcpConfigErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRtcpIpcErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRtcpSgErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRtcpSubErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRtcpIntErrors"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaTxLostPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRequestedRtpPkts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaHighPktPoolLimitHit"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMallocFailures"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaDentDroppedPkts"))
)
if mibBuilder.loadTexts:
    tmnxVdoGrpV7v0Group.setStatus("current")

tmnxVdoAdiV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 4)
)
tmnxVdoAdiV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlRowStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlDescription"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlRowStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiZoneChlName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiChlForwardScte35"))
)
if mibBuilder.loadTexts:
    tmnxVdoAdiV7v0Group.setStatus("current")

tmnxVdoStatsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 5)
)
tmnxVdoStatsV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcStreamType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVdoGrpId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcAdminRTBufferSize"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSSRCId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcUDPSrcPort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcUDPDestPort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcUptime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcAdminBW"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcBufferSize"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxInvalidPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcTxBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcTxPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcTxFailedPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClntRTSvrAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClntRTSvrAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientRTSrvrPort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientRxReTxBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientRxReTxPkts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientTxRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientTxRTReqReTx"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientGapsDetectd"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrRxRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrRxFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrTxRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrTxBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSrvrTxPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrChnlType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrRxFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrRxFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrTxFCCReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrTxBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFCCSrvrTxPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIAdminState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADICurrentState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIPATVersion"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIPMTVersion"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIPATChanges"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIPMTChanges"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIRxPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADITxPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIRxSCTE35Msgs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIRxSCTE35MsgEnc"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIRxSCTE35MsgUnsup"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIRxSCTE35MsgDisc"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcADIUnsuppTSLenPkts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTClientPort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcDupSeqNumber"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RxBytesLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RxBytesHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RxPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RxPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RxInvalidPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RxInvalidPacketsHgh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1TxBytesLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1TxBytesHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1TxPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1TxPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1TxFailedPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1TxFailedPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTClntRxReTxBytsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTClntRxReTxBytsHgh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTClntRxReTxPktsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTClntRxReTxPktsHgh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTSrvrTxBytesLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTSrvrTxBytesHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTSrvrTxPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1RTSrvrTxPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1FCCSrvrTxBytesLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1FCCSrvrTxBytesHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1FCCSrvrTxPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1FCCSrvrTxPacketsHgh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1ADIRxPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1ADIRxPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1ADITxPacketsLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGV1ADITxPacketsHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionSSRCId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionUpTime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionExpireTime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionCName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionDestAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionDestAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRxFCCRequests"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxFCCReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxFCCPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxFCCOctets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxFCCFailedPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRxRTRequests"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxRTPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxRTOctets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionTxRTFailedPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRequestedRtpPkts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHdRTServerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSdRTServerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipRTServerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrSdRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrHdRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrPipRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrRxSdRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrRxSdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrRxHdRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrRxHdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrRxPipRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrRxPipFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxSdRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxSdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxSdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxHdRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxHdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxHdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxPipRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxPipBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSvrTxPipPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHdFCCServerMode"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSdFCCServerMode"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipFCCServerMode"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrRxSdFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrRxSdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrRxHdFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrRxHdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrRxPipFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrRxPipFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxSdFCCReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxSdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxSdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxHdFCCReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxHdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxHdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxPipFCCRplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxPipBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatFCCSrTxPipPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatTxFailedPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30TcpSessions"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfScte30InitSessions"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrSdRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrHdRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrPipRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrRxSdRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrRxSdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrRxHdRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrRxHdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrRxPipRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrRxPipFailedRq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxSdRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxSdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxSdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxHdRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxHdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxHdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxPipRTReplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxPipBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowRTSvrTxPipPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrRxSdFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrRxSdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrRxHdFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrRxHdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrRxPipFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrRxPipFailedRq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxSdFCCReplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxSdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxSdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxHdFCCReplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxHdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxHdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxPipFCCRplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxPipBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowFCCSrTxPipPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStLowTxFailedPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrSdRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrHdRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrPipRtpPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrRxSdRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrRxSdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrRxHdRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrRxHdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrRxPipRTReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrRxPipFailedRq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxSdRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxSdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxSdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxHdRTReplies"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxHdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxHdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxPipRTReplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxPipBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghRTSvrTxPipPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrRxSdFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrRxSdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrRxHdFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrRxHdFailedReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrRxPipFCCReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrRxPipFailedRq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxSdFCCReplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxSdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxSdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxHdFCCReplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxHdBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxHdPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxPipFCCRplis"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxPipBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghFCCSrTxPipPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStHghTxFailedPackets"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDMpegStreamType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDLanguage"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiServerUptime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiInitReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucInitResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnsucInitResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiAliveReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucAliveResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnSucAliveResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiCueReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucCueResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnsucCueResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiAbortReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucAbortResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnsucAbortResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnknownSCTE30Req"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSpliceReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucSpliceResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnsucSpliceResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucSpliceInCompResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiSucSpliceOutCompResp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiUnsucSpliceOutComRes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceAdServerAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceAdServerAddr"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceStatus"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceDurationReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceDurationPlayed"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceRate"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceSessionId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSplicePriorSessionId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceAbortReason"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceSpliceInSeqNum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceSpliceOutSeqNum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceNumBlkFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceBlkFramePTS"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceMaxAdPTS"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGSpliceMinNwPTS"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiMinPort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiMaxPort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSGAdiChlName"))
)
if mibBuilder.loadTexts:
    tmnxVdoStatsV7v0Group.setStatus("current")

tmnxVdoNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 6)
)
tmnxVdoNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoNotifysvcId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyIfName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGrpAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGroupAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySrcAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySourceAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAdSpliceSessionId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAdSpliceAbortTime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAdSpliceDuration"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyClientAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyClientAddress"))
)
if mibBuilder.loadTexts:
    tmnxVdoNotifyObjsV7v0Group.setStatus("current")

tmnxVdoGrpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 8)
)
tmnxVdoGrpV8v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaBwPeak"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpResvRet"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpAnalyzerState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpStreamSelectionState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaCurTotalRetBw"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaPeakRetBw"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaCurFccBw"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaFccDropCntReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRtcp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRtcpLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRtcpHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRudp"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRudpLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRudpHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRetReqCrt"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRetReqCrtLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaMcRetReqCrtHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRetReqQnc"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRetReqQncLow32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaRetReqQncHigh32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaPktsLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaPktsLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaPktsLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaPktsLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaPktsLostInSeqMore"))
)
if mibBuilder.loadTexts:
    tmnxVdoGrpV8v0Group.setStatus("current")

tmnxVdoIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 9)
)
tmnxVdoIfV8v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoIfRTMcastReply"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfRTCount"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfRTInterval"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfRTHoldTime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfAcctPolicyId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfOutputFormat"))
)
if mibBuilder.loadTexts:
    tmnxVdoIfV8v0Group.setStatus("current")

tmnxVdoStatsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 10)
)
tmnxVdoStatsV8v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetPkts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetPktsL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetPktsH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetBytesL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetBytesH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetErrs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetErrsL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetErrsH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqQnc"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqQncL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqQncH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqCrt"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqCrtL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqCrtH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFccMinDuration"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcAudioReorder"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytesSaved"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytesSavedL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytesSavedH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPacketsSaved"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPacketsSavedL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPacketsSavedH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcStatOperBW"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRouterIfName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSSdMcRdPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSSdMcRdPktsReqL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSSdMcRdPktsReqH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSHDMcRdPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSHDMcRdPktsReqL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSHDMcRdPktsReqH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSPipMcRdPktReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSPipMcRdPktReqL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSPipMcRdPktReqH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRTReqQuenched"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRTMcastReqCreated"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppRepSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppRepSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppRepSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppReqSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppReqSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppReqSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbRepSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbRepSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbRepSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbReqSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbReqSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbReqSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRudpFbRepSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRudpFbRepSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRudpFbRepSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccPktsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccPktsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccPktsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccOctetsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccOctetsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccOctetsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetPktsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetPktsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetPktsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetOctetsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetOctetsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetOctetsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpPktsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpPktsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpPktsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpByteSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpByteSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpByteSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmDegrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmImpairSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtRepErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtRepDegSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtRepImpSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtSyntxErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatRepErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatRepDegSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatRepImpSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatSyntxErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPcrRepErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPcrRepDegSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPcrRepImpSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmSyncByteErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmSyncLossSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmCatErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmUnrefPidErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMDIDelayFactor"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMDILossRate"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMinGOPLength"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMinFrmPerSec"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmAvgGOPLength"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmAvgFrmPerSec"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMaxGOPLength"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMaxFrmPerSec"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodIFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmBadIFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodPFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmBadPFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodBFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmBadBFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmTrafficLossSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmSCTE35ErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperAnalyzerSt"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperCcError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPatRepError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTncPatRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperQosPatRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPoaPatRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPatSyntax"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPcrRepError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTncPcrRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperQosPcrRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPoaPcrRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperVidPIDAbs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPIDPmtUnref"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPmtRepError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTncPmtRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperQosPmtRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPoaPmtRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPmtSyntax"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperSCTE35Error"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTeiError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTsSyncLoss"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperNonVidPIDAbs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperReportAlarm"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDCcErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDTeiErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDAbsentErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDBitrate"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDIsPCR"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxRtpTsDelta"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTicksDelta"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTicksDeltaL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTicksDeltaH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtCurTsJitter"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtCurTsJitterL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtCurTsJitterH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTsJitter"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTsJitterL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTsJitterH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcNumFccDentedPkts"))
)
if mibBuilder.loadTexts:
    tmnxVdoStatsV8v0Group.setStatus("obsolete")

tmnxVdoGrpSrcV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 11)
)
tmnxVdoGrpSrcV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxDupSsrcDrops"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcDupSsrc"))
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcV7v0Group.setStatus("current")

tmnxVdoNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 12)
)
tmnxVdoNotifyObjsV8v0Group.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAnalyzerState")
)
if mibBuilder.loadTexts:
    tmnxVdoNotifyObjsV8v0Group.setStatus("current")

tmnxVdoStatsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 14)
)
tmnxVdoStatsV9v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetPkts"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetPktsL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetPktsH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetBytes"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetBytesL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetBytesH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetErrs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetErrsL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSTxMcRetErrsH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqQnc"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqQncL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqQncH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqCrt"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqCrtL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRTSRetReqCrtH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcFccMinDuration"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcAudioReorder"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytesSaved"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytesSavedL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxBytesSavedH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPacketsSaved"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPacketsSavedL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRxPacketsSavedH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcStatOperBW"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcRouterIfName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSSdMcRdPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSSdMcRdPktsReqL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSSdMcRdPktsReqH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSHDMcRdPktsReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSHDMcRdPktsReqL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSHDMcRdPktsReqH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSPipMcRdPktReq"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSPipMcRdPktReqL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatRTSPipMcRdPktReqH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRTReqQuenched"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionRTMcastReqCreated"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoSessionPktsLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatSDPktLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatHDPktLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq10"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq20"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq30"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeq40"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatPipPktLostInSeqMore"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppRepSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppRepSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppRepSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppReqSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppReqSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpAppReqSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbRepSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbRepSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbRepSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbReqSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbReqSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRtcpFbReqSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRudpFbRepSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRudpFbRepSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtRxRudpFbRepSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccPktsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccPktsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccPktsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccOctetsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccOctetsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxFccOctetsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetPktsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetPktsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetPktsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetOctetsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetOctetsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRetOctetsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpPktsSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpPktsSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpPktsSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpByteSum"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpByteSumL"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfStatExtTxRudpByteSumH"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmDegrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmImpairSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtRepErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtRepDegSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtRepImpSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPmtSyntxErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatRepErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatRepDegSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatRepImpSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPatSyntxErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPcrRepErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPcrRepDegSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmPcrRepImpSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmSyncByteErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmSyncLossSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmCatErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmUnrefPidErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMDIDelayFactor"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMDILossRate"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMinGOPLength"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMinFrmPerSec"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmAvgGOPLength"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmAvgFrmPerSec"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMaxGOPLength"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmMaxFrmPerSec"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodIFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmBadIFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodPFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmBadPFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmGoodBFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmBadBFrames"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmTrafficLossSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperAnalyzerSt"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperCcError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPatRepError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTncPatRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperQosPatRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPoaPatRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPatSyntax"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPcrRepError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTncPcrRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperQosPcrRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPoaPcrRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperVidPIDAbs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPIDPmtUnref"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPmtRepError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTncPmtRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperQosPmtRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPoaPmtRep"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperPmtSyntax"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperSCTE35Error"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTeiError"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperTsSyncLoss"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperNonVidPIDAbs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmOperReportAlarm"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDCcErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDTeiErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDAbsentErrSecs"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDBitrate"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoPIDIsPCR"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxRtpTsDelta"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTicksDelta"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTicksDeltaL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTicksDeltaH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtCurTsJitter"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtCurTsJitterL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtCurTsJitterH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTsJitter"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTsJitterL32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcExtMaxTsJitterH32"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcNumFccDentedPkts"))
)
if mibBuilder.loadTexts:
    tmnxVdoStatsV9v0Group.setStatus("current")

tmnxVdoObsoletedV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 15)
)
tmnxVdoObsoletedV9v0Group.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcVqmSCTE35ErrSecs")
)
if mibBuilder.loadTexts:
    tmnxVdoObsoletedV9v0Group.setStatus("current")


# Notification objects

tmnxVdoDuplicateSsrcId = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 1)
)
tmnxVdoDuplicateSsrcId.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcSSRCId")
)
if mibBuilder.loadTexts:
    tmnxVdoDuplicateSsrcId.setStatus(
        "current"
    )

tmnxVdoMdaSessionsLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 2)
)
tmnxVdoMdaSessionsLimitExceeded.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaActiveRtcpSessions")
)
if mibBuilder.loadTexts:
    tmnxVdoMdaSessionsLimitExceeded.setStatus(
        "current"
    )

tmnxVdoMdaSGLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 3)
)
tmnxVdoMdaSGLimitExceeded.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaChannels")
)
if mibBuilder.loadTexts:
    tmnxVdoMdaSGLimitExceeded.setStatus(
        "current"
    )

tmnxVdoMdaSessionsLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 4)
)
tmnxVdoMdaSessionsLimitCleared.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaActiveRtcpSessions")
)
if mibBuilder.loadTexts:
    tmnxVdoMdaSessionsLimitCleared.setStatus(
        "current"
    )

tmnxVdoMdaSGLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 5)
)
tmnxVdoMdaSGLimitCleared.setObjects(
    ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpMdaChannels")
)
if mibBuilder.loadTexts:
    tmnxVdoMdaSGLimitCleared.setStatus(
        "current"
    )

tmnxVdoAdSpliceAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 6)
)
tmnxVdoAdSpliceAbort.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoNotifysvcId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyIfName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGrpAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGroupAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySrcAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySourceAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAdSpliceSessionId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAdSpliceAbortTime"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAdSpliceDuration"))
)
if mibBuilder.loadTexts:
    tmnxVdoAdSpliceAbort.setStatus(
        "current"
    )

tmnxVdoClientSessionsLmtExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 7)
)
tmnxVdoClientSessionsLmtExceeded.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyClientAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyClientAddress"))
)
if mibBuilder.loadTexts:
    tmnxVdoClientSessionsLmtExceeded.setStatus(
        "current"
    )

tmnxVdoClientSessionsLmtCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 8)
)
tmnxVdoClientSessionsLmtCleared.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyClientAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyClientAddress"))
)
if mibBuilder.loadTexts:
    tmnxVdoClientSessionsLmtCleared.setStatus(
        "current"
    )

tmnxVdoGrpSrcAnlyzrErrState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 9)
)
tmnxVdoGrpSrcAnlyzrErrState.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoNotifysvcId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyIfName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGrpAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGroupAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySrcAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySourceAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyAnalyzerState"))
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAnlyzrErrState.setStatus(
        "current"
    )

tmnxVdoGrpSrcAnlyzrStClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 61, 0, 10)
)
tmnxVdoGrpSrcAnlyzrStClear.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoNotifysvcId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyIfName"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGrpAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifyGroupAddress"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySrcAddrType"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotifySourceAddress"))
)
if mibBuilder.loadTexts:
    tmnxVdoGrpSrcAnlyzrStClear.setStatus(
        "current"
    )


# Notifications groups

tmnxVdoNotificationsV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 7)
)
tmnxVdoNotificationsV7v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoDuplicateSsrcId"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoMdaSessionsLimitExceeded"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoMdaSGLimitExceeded"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoMdaSessionsLimitCleared"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoMdaSGLimitCleared"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdSpliceAbort"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoClientSessionsLmtExceeded"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoClientSessionsLmtCleared"))
)
if mibBuilder.loadTexts:
    tmnxVdoNotificationsV7v0Group.setStatus(
        "current"
    )

tmnxVdoNotificationsV8v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 2, 13)
)
tmnxVdoNotificationsV8v0Group.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcAnlyzrErrState"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcAnlyzrStClear"))
)
if mibBuilder.loadTexts:
    tmnxVdoNotificationsV8v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxVdoV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 1, 1)
)
tmnxVdoV7v0Compliance.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGlobalV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoStatsV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotificationsV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxVdoV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxVdoV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 1, 2)
)
tmnxVdoV8v0Compliance.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGlobalV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoStatsV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoStatsV8v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotificationsV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpV8v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfV8v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotificationsV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxVdoV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxVdoV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 61, 1, 3)
)
tmnxVdoV9v0Compliance.setObjects(
      *(("TIMETRA-VIDEO-MIB", "tmnxVdoGlobalV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoAdiV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoStatsV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoStatsV9v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotificationsV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpSrcV7v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoGrpV8v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoIfV8v0Group"),
        ("TIMETRA-VIDEO-MIB", "tmnxVdoNotificationsV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxVdoV9v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-VIDEO-MIB",
    **{"TmnxVdoPIDType": TmnxVdoPIDType,
       "TmnxVdoPTS": TmnxVdoPTS,
       "TmnxMDILossRate": TmnxMDILossRate,
       "timetraVideoMIBModule": timetraVideoMIBModule,
       "tmnxVdoConformance": tmnxVdoConformance,
       "tmnxVdoCompliances": tmnxVdoCompliances,
       "tmnxVdoV7v0Compliance": tmnxVdoV7v0Compliance,
       "tmnxVdoV8v0Compliance": tmnxVdoV8v0Compliance,
       "tmnxVdoV9v0Compliance": tmnxVdoV9v0Compliance,
       "tmnxVdoGroups": tmnxVdoGroups,
       "tmnxVdoGlobalV7v0Group": tmnxVdoGlobalV7v0Group,
       "tmnxVdoIfV7v0Group": tmnxVdoIfV7v0Group,
       "tmnxVdoGrpV7v0Group": tmnxVdoGrpV7v0Group,
       "tmnxVdoAdiV7v0Group": tmnxVdoAdiV7v0Group,
       "tmnxVdoStatsV7v0Group": tmnxVdoStatsV7v0Group,
       "tmnxVdoNotifyObjsV7v0Group": tmnxVdoNotifyObjsV7v0Group,
       "tmnxVdoNotificationsV7v0Group": tmnxVdoNotificationsV7v0Group,
       "tmnxVdoGrpV8v0Group": tmnxVdoGrpV8v0Group,
       "tmnxVdoIfV8v0Group": tmnxVdoIfV8v0Group,
       "tmnxVdoStatsV8v0Group": tmnxVdoStatsV8v0Group,
       "tmnxVdoGrpSrcV7v0Group": tmnxVdoGrpSrcV7v0Group,
       "tmnxVdoNotifyObjsV8v0Group": tmnxVdoNotifyObjsV8v0Group,
       "tmnxVdoNotificationsV8v0Group": tmnxVdoNotificationsV8v0Group,
       "tmnxVdoStatsV9v0Group": tmnxVdoStatsV9v0Group,
       "tmnxVdoObsoletedV9v0Group": tmnxVdoObsoletedV9v0Group,
       "tmnxVdo": tmnxVdo,
       "tmnxVdoObjs": tmnxVdoObjs,
       "tmnxVdoIfTable": tmnxVdoIfTable,
       "tmnxVdoIfEntry": tmnxVdoIfEntry,
       "tmnxVdoIfName": tmnxVdoIfName,
       "tmnxVdoIfRowStatus": tmnxVdoIfRowStatus,
       "tmnxVdoIfLastChanged": tmnxVdoIfLastChanged,
       "tmnxVdoIfAdminState": tmnxVdoIfAdminState,
       "tmnxVdoIfOperState": tmnxVdoIfOperState,
       "tmnxVdoIfVrtrIfIndex": tmnxVdoIfVrtrIfIndex,
       "tmnxVdoIfDescription": tmnxVdoIfDescription,
       "tmnxVdoIfVdoGrpId": tmnxVdoIfVdoGrpId,
       "tmnxVdoIfIngressQosPolicyId": tmnxVdoIfIngressQosPolicyId,
       "tmnxVdoIfEgressQosPolicyId": tmnxVdoIfEgressQosPolicyId,
       "tmnxVdoIfAdi": tmnxVdoIfAdi,
       "tmnxVdoIfRTClientAddrType": tmnxVdoIfRTClientAddrType,
       "tmnxVdoIfRTClientAddr": tmnxVdoIfRTClientAddr,
       "tmnxVdoIfGatewayAddrType": tmnxVdoIfGatewayAddrType,
       "tmnxVdoIfGatewayAddr": tmnxVdoIfGatewayAddr,
       "tmnxVdoIfMcastSvcId": tmnxVdoIfMcastSvcId,
       "tmnxVdoIfIngressIpFilterId": tmnxVdoIfIngressIpFilterId,
       "tmnxVdoIfIngressMacFilterId": tmnxVdoIfIngressMacFilterId,
       "tmnxVdoIfEgressIpFilterId": tmnxVdoIfEgressIpFilterId,
       "tmnxVdoIfEgressMacFilterId": tmnxVdoIfEgressMacFilterId,
       "tmnxVdoIfScte30ControlAddrType": tmnxVdoIfScte30ControlAddrType,
       "tmnxVdoIfScte30ControlAddr": tmnxVdoIfScte30ControlAddr,
       "tmnxVdoIfScte30DataAddrType": tmnxVdoIfScte30DataAddrType,
       "tmnxVdoIfScte30DataAddr": tmnxVdoIfScte30DataAddr,
       "tmnxVdoIfSapId": tmnxVdoIfSapId,
       "tmnxVdoIfMcastProtocol": tmnxVdoIfMcastProtocol,
       "tmnxVdoIfSessions": tmnxVdoIfSessions,
       "tmnxVdoIfCpmProtectPolicyId": tmnxVdoIfCpmProtectPolicyId,
       "tmnxVdoIfRTMcastReply": tmnxVdoIfRTMcastReply,
       "tmnxVdoIfRTCount": tmnxVdoIfRTCount,
       "tmnxVdoIfRTInterval": tmnxVdoIfRTInterval,
       "tmnxVdoIfRTHoldTime": tmnxVdoIfRTHoldTime,
       "tmnxVdoIfAcctPolicyId": tmnxVdoIfAcctPolicyId,
       "tmnxVdoIfOutputFormat": tmnxVdoIfOutputFormat,
       "tmnxVdoIfAddrTable": tmnxVdoIfAddrTable,
       "tmnxVdoIfAddrEntry": tmnxVdoIfAddrEntry,
       "tmnxVdoIfAddrIpAddrType": tmnxVdoIfAddrIpAddrType,
       "tmnxVdoIfAddrIpAddress": tmnxVdoIfAddrIpAddress,
       "tmnxVdoIfAddrPrefixLen": tmnxVdoIfAddrPrefixLen,
       "tmnxVdoIfAddrRowStatus": tmnxVdoIfAddrRowStatus,
       "tmnxVdoGrpTable": tmnxVdoGrpTable,
       "tmnxVdoGrpEntry": tmnxVdoGrpEntry,
       "tmnxVdoGrpId": tmnxVdoGrpId,
       "tmnxVdoGrpRowStatus": tmnxVdoGrpRowStatus,
       "tmnxVdoGrpLastChanged": tmnxVdoGrpLastChanged,
       "tmnxVdoGrpAdminState": tmnxVdoGrpAdminState,
       "tmnxVdoGrpOperState": tmnxVdoGrpOperState,
       "tmnxVdoGrpDescription": tmnxVdoGrpDescription,
       "tmnxVdoGrpLocalRTServerState": tmnxVdoGrpLocalRTServerState,
       "tmnxVdoGrpFCCServerState": tmnxVdoGrpFCCServerState,
       "tmnxVdoGrpADIServerState": tmnxVdoGrpADIServerState,
       "tmnxVdoGrpResvRet": tmnxVdoGrpResvRet,
       "tmnxVdoGrpAnalyzerState": tmnxVdoGrpAnalyzerState,
       "tmnxVdoGrpStreamSelectionState": tmnxVdoGrpStreamSelectionState,
       "tmnxVdoGrpMDATable": tmnxVdoGrpMDATable,
       "tmnxVdoGrpMDAEntry": tmnxVdoGrpMDAEntry,
       "tmnxVdoGrpMdaRowStatus": tmnxVdoGrpMdaRowStatus,
       "tmnxVdoGrpMdaAdminState": tmnxVdoGrpMdaAdminState,
       "tmnxVdoGrpMdaOperState": tmnxVdoGrpMdaOperState,
       "tmnxVdoGrpMdaUsedMemory": tmnxVdoGrpMdaUsedMemory,
       "tmnxVdoGrpMdaAvailableMemory": tmnxVdoGrpMdaAvailableMemory,
       "tmnxVdoGrpMdaChannels": tmnxVdoGrpMdaChannels,
       "tmnxVdoGrpMdaChannelAllocFails": tmnxVdoGrpMdaChannelAllocFails,
       "tmnxVdoGrpMdaMaxBwExceeded": tmnxVdoGrpMdaMaxBwExceeded,
       "tmnxVdoGrpMdaBwInUse": tmnxVdoGrpMdaBwInUse,
       "tmnxVdoGrpMdaActiveRtcpSessions": tmnxVdoGrpMdaActiveRtcpSessions,
       "tmnxVdoGrpMdaEgressStreamResets": tmnxVdoGrpMdaEgressStreamResets,
       "tmnxVdoGrpMdaIngressStreamResets": tmnxVdoGrpMdaIngressStreamResets,
       "tmnxVdoGrpMdaAdStreamResets": tmnxVdoGrpMdaAdStreamResets,
       "tmnxVdoGrpMdaAdStreamAborts": tmnxVdoGrpMdaAdStreamAborts,
       "tmnxVdoGrpMdaSsrcCollisions": tmnxVdoGrpMdaSsrcCollisions,
       "tmnxVdoGrpMdaRxDataPackets": tmnxVdoGrpMdaRxDataPackets,
       "tmnxVdoGrpMdaRxDataPacketsLow32": tmnxVdoGrpMdaRxDataPacketsLow32,
       "tmnxVdoGrpMdaRxDataPacketsHigh32": tmnxVdoGrpMdaRxDataPacketsHigh32,
       "tmnxVdoGrpMdaRxDataOctets": tmnxVdoGrpMdaRxDataOctets,
       "tmnxVdoGrpMdaRxDataOctetsLow32": tmnxVdoGrpMdaRxDataOctetsLow32,
       "tmnxVdoGrpMdaRxDataOctetsHigh32": tmnxVdoGrpMdaRxDataOctetsHigh32,
       "tmnxVdoGrpMdaRxDataPacketErrors": tmnxVdoGrpMdaRxDataPacketErrors,
       "tmnxVdoGrpMdaRxDataPktErrsLow32": tmnxVdoGrpMdaRxDataPktErrsLow32,
       "tmnxVdoGrpMdaRxDataPktErrsHigh32": tmnxVdoGrpMdaRxDataPktErrsHigh32,
       "tmnxVdoGrpMdaTxDataPackets": tmnxVdoGrpMdaTxDataPackets,
       "tmnxVdoGrpMdaTxDataPacketsLow32": tmnxVdoGrpMdaTxDataPacketsLow32,
       "tmnxVdoGrpMdaTxDataPacketsHigh32": tmnxVdoGrpMdaTxDataPacketsHigh32,
       "tmnxVdoGrpMdaTxDataOctets": tmnxVdoGrpMdaTxDataOctets,
       "tmnxVdoGrpMdaTxDataOctetsLow32": tmnxVdoGrpMdaTxDataOctetsLow32,
       "tmnxVdoGrpMdaTxDataOctetsHigh32": tmnxVdoGrpMdaTxDataOctetsHigh32,
       "tmnxVdoGrpMdaTxDataPacketErrors": tmnxVdoGrpMdaTxDataPacketErrors,
       "tmnxVdoGrpMdaTxDataPktErrsLow32": tmnxVdoGrpMdaTxDataPktErrsLow32,
       "tmnxVdoGrpMdaTxDataPktErrsHigh32": tmnxVdoGrpMdaTxDataPktErrsHigh32,
       "tmnxVdoGrpMdaRtcpParseErrors": tmnxVdoGrpMdaRtcpParseErrors,
       "tmnxVdoGrpMdaRtcpConfigErrors": tmnxVdoGrpMdaRtcpConfigErrors,
       "tmnxVdoGrpMdaRtcpIpcErrors": tmnxVdoGrpMdaRtcpIpcErrors,
       "tmnxVdoGrpMdaRtcpSgErrors": tmnxVdoGrpMdaRtcpSgErrors,
       "tmnxVdoGrpMdaRtcpSubErrors": tmnxVdoGrpMdaRtcpSubErrors,
       "tmnxVdoGrpMdaRtcpIntErrors": tmnxVdoGrpMdaRtcpIntErrors,
       "tmnxVdoGrpMdaTxLostPackets": tmnxVdoGrpMdaTxLostPackets,
       "tmnxVdoGrpMdaRequestedRtpPkts": tmnxVdoGrpMdaRequestedRtpPkts,
       "tmnxVdoGrpMdaHighPktPoolLimitHit": tmnxVdoGrpMdaHighPktPoolLimitHit,
       "tmnxVdoGrpMdaMallocFailures": tmnxVdoGrpMdaMallocFailures,
       "tmnxVdoGrpMdaDentDroppedPkts": tmnxVdoGrpMdaDentDroppedPkts,
       "tmnxVdoGrpMdaBwPeak": tmnxVdoGrpMdaBwPeak,
       "tmnxVdoGrpMdaCurTotalRetBw": tmnxVdoGrpMdaCurTotalRetBw,
       "tmnxVdoGrpMdaPeakRetBw": tmnxVdoGrpMdaPeakRetBw,
       "tmnxVdoGrpMdaCurFccBw": tmnxVdoGrpMdaCurFccBw,
       "tmnxVdoGrpMdaFccDropCntReq": tmnxVdoGrpMdaFccDropCntReq,
       "tmnxVdoGrpMdaMcRtcp": tmnxVdoGrpMdaMcRtcp,
       "tmnxVdoGrpMdaMcRtcpLow32": tmnxVdoGrpMdaMcRtcpLow32,
       "tmnxVdoGrpMdaMcRtcpHigh32": tmnxVdoGrpMdaMcRtcpHigh32,
       "tmnxVdoGrpMdaMcRudp": tmnxVdoGrpMdaMcRudp,
       "tmnxVdoGrpMdaMcRudpLow32": tmnxVdoGrpMdaMcRudpLow32,
       "tmnxVdoGrpMdaMcRudpHigh32": tmnxVdoGrpMdaMcRudpHigh32,
       "tmnxVdoGrpMdaMcRetReqCrt": tmnxVdoGrpMdaMcRetReqCrt,
       "tmnxVdoGrpMdaMcRetReqCrtLow32": tmnxVdoGrpMdaMcRetReqCrtLow32,
       "tmnxVdoGrpMdaMcRetReqCrtHigh32": tmnxVdoGrpMdaMcRetReqCrtHigh32,
       "tmnxVdoGrpMdaRetReqQnc": tmnxVdoGrpMdaRetReqQnc,
       "tmnxVdoGrpMdaRetReqQncLow32": tmnxVdoGrpMdaRetReqQncLow32,
       "tmnxVdoGrpMdaRetReqQncHigh32": tmnxVdoGrpMdaRetReqQncHigh32,
       "tmnxVdoGrpMdaPktsLostInSeq10": tmnxVdoGrpMdaPktsLostInSeq10,
       "tmnxVdoGrpMdaPktsLostInSeq20": tmnxVdoGrpMdaPktsLostInSeq20,
       "tmnxVdoGrpMdaPktsLostInSeq30": tmnxVdoGrpMdaPktsLostInSeq30,
       "tmnxVdoGrpMdaPktsLostInSeq40": tmnxVdoGrpMdaPktsLostInSeq40,
       "tmnxVdoGrpMdaPktsLostInSeqMore": tmnxVdoGrpMdaPktsLostInSeqMore,
       "tmnxVdoAdiChlTable": tmnxVdoAdiChlTable,
       "tmnxVdoAdiChlEntry": tmnxVdoAdiChlEntry,
       "tmnxVdoAdiChlGrpAddrType": tmnxVdoAdiChlGrpAddrType,
       "tmnxVdoAdiChlGrpAddress": tmnxVdoAdiChlGrpAddress,
       "tmnxVdoAdiChlSrcAddrType": tmnxVdoAdiChlSrcAddrType,
       "tmnxVdoAdiChlSrcAddress": tmnxVdoAdiChlSrcAddress,
       "tmnxVdoAdiChlRowStatus": tmnxVdoAdiChlRowStatus,
       "tmnxVdoAdiChlName": tmnxVdoAdiChlName,
       "tmnxVdoAdiChlDescription": tmnxVdoAdiChlDescription,
       "tmnxVdoAdiChlForwardScte35": tmnxVdoAdiChlForwardScte35,
       "tmnxVdoAdiZoneChlTable": tmnxVdoAdiZoneChlTable,
       "tmnxVdoAdiZoneChlEntry": tmnxVdoAdiZoneChlEntry,
       "tmnxVdoAdiZoneChlGrpAddrType": tmnxVdoAdiZoneChlGrpAddrType,
       "tmnxVdoAdiZoneChlGrpAddress": tmnxVdoAdiZoneChlGrpAddress,
       "tmnxVdoAdiZoneChlSrcAddrType": tmnxVdoAdiZoneChlSrcAddrType,
       "tmnxVdoAdiZoneChlSrcAddress": tmnxVdoAdiZoneChlSrcAddress,
       "tmnxVdoAdiZoneChlRowStatus": tmnxVdoAdiZoneChlRowStatus,
       "tmnxVdoAdiZoneChlName": tmnxVdoAdiZoneChlName,
       "tmnxVdoGrpSrcStatTable": tmnxVdoGrpSrcStatTable,
       "tmnxVdoGrpSrcStatEntry": tmnxVdoGrpSrcStatEntry,
       "tmnxVdoGrpSrcGrpAddrType": tmnxVdoGrpSrcGrpAddrType,
       "tmnxVdoGrpSrcGroupAddress": tmnxVdoGrpSrcGroupAddress,
       "tmnxVdoGrpSrcSrcAddrType": tmnxVdoGrpSrcSrcAddrType,
       "tmnxVdoGrpSrcSourceAddress": tmnxVdoGrpSrcSourceAddress,
       "tmnxVdoGrpSrcStreamType": tmnxVdoGrpSrcStreamType,
       "tmnxVdoGrpSrcVdoGrpId": tmnxVdoGrpSrcVdoGrpId,
       "tmnxVdoGrpSrcAdminRTBufferSize": tmnxVdoGrpSrcAdminRTBufferSize,
       "tmnxVdoGrpSrcSSRCId": tmnxVdoGrpSrcSSRCId,
       "tmnxVdoGrpSrcUDPSrcPort": tmnxVdoGrpSrcUDPSrcPort,
       "tmnxVdoGrpSrcUDPDestPort": tmnxVdoGrpSrcUDPDestPort,
       "tmnxVdoGrpSrcUptime": tmnxVdoGrpSrcUptime,
       "tmnxVdoGrpSrcAdminBW": tmnxVdoGrpSrcAdminBW,
       "tmnxVdoGrpSrcBufferSize": tmnxVdoGrpSrcBufferSize,
       "tmnxVdoGrpSrcRxBytes": tmnxVdoGrpSrcRxBytes,
       "tmnxVdoGrpSrcRxPackets": tmnxVdoGrpSrcRxPackets,
       "tmnxVdoGrpSrcRxInvalidPackets": tmnxVdoGrpSrcRxInvalidPackets,
       "tmnxVdoGrpSrcTxBytes": tmnxVdoGrpSrcTxBytes,
       "tmnxVdoGrpSrcTxPackets": tmnxVdoGrpSrcTxPackets,
       "tmnxVdoGrpSrcTxFailedPackets": tmnxVdoGrpSrcTxFailedPackets,
       "tmnxVdoGrpSrcRTClientAdminState": tmnxVdoGrpSrcRTClientAdminState,
       "tmnxVdoGrpSrcRTClntRTSvrAddrType": tmnxVdoGrpSrcRTClntRTSvrAddrType,
       "tmnxVdoGrpSrcRTClntRTSvrAddr": tmnxVdoGrpSrcRTClntRTSvrAddr,
       "tmnxVdoGrpSrcRTClientRTSrvrPort": tmnxVdoGrpSrcRTClientRTSrvrPort,
       "tmnxVdoGrpSrcRTClientRxReTxBytes": tmnxVdoGrpSrcRTClientRxReTxBytes,
       "tmnxVdoGrpSrcRTClientRxReTxPkts": tmnxVdoGrpSrcRTClientRxReTxPkts,
       "tmnxVdoGrpSrcRTClientTxRTReq": tmnxVdoGrpSrcRTClientTxRTReq,
       "tmnxVdoGrpSrcRTClientTxRTReqReTx": tmnxVdoGrpSrcRTClientTxRTReqReTx,
       "tmnxVdoGrpSrcRTClientGapsDetectd": tmnxVdoGrpSrcRTClientGapsDetectd,
       "tmnxVdoGrpSrcRTClientFailedReq": tmnxVdoGrpSrcRTClientFailedReq,
       "tmnxVdoGrpSrcRTSrvrAdminState": tmnxVdoGrpSrcRTSrvrAdminState,
       "tmnxVdoGrpSrcRTSrvrRtpPktsReq": tmnxVdoGrpSrcRTSrvrRtpPktsReq,
       "tmnxVdoGrpSrcRTSrvrRxRTReq": tmnxVdoGrpSrcRTSrvrRxRTReq,
       "tmnxVdoGrpSrcRTSrvrRxFailedReq": tmnxVdoGrpSrcRTSrvrRxFailedReq,
       "tmnxVdoGrpSrcRTSrvrTxRTReplies": tmnxVdoGrpSrcRTSrvrTxRTReplies,
       "tmnxVdoGrpSrcRTSrvrTxBytes": tmnxVdoGrpSrcRTSrvrTxBytes,
       "tmnxVdoGrpSrcRTSrvrTxPackets": tmnxVdoGrpSrcRTSrvrTxPackets,
       "tmnxVdoGrpSrcFCCSrvrAdminState": tmnxVdoGrpSrcFCCSrvrAdminState,
       "tmnxVdoGrpSrcFCCSrvrChnlType": tmnxVdoGrpSrcFCCSrvrChnlType,
       "tmnxVdoGrpSrcFCCSrvrRxFCCReq": tmnxVdoGrpSrcFCCSrvrRxFCCReq,
       "tmnxVdoGrpSrcFCCSrvrRxFailedReq": tmnxVdoGrpSrcFCCSrvrRxFailedReq,
       "tmnxVdoGrpSrcFCCSrvrTxFCCReplies": tmnxVdoGrpSrcFCCSrvrTxFCCReplies,
       "tmnxVdoGrpSrcFCCSrvrTxBytes": tmnxVdoGrpSrcFCCSrvrTxBytes,
       "tmnxVdoGrpSrcFCCSrvrTxPackets": tmnxVdoGrpSrcFCCSrvrTxPackets,
       "tmnxVdoGrpSrcADIAdminState": tmnxVdoGrpSrcADIAdminState,
       "tmnxVdoGrpSrcADICurrentState": tmnxVdoGrpSrcADICurrentState,
       "tmnxVdoGrpSrcADIPATVersion": tmnxVdoGrpSrcADIPATVersion,
       "tmnxVdoGrpSrcADIPMTVersion": tmnxVdoGrpSrcADIPMTVersion,
       "tmnxVdoGrpSrcADIPATChanges": tmnxVdoGrpSrcADIPATChanges,
       "tmnxVdoGrpSrcADIPMTChanges": tmnxVdoGrpSrcADIPMTChanges,
       "tmnxVdoGrpSrcADIRxPackets": tmnxVdoGrpSrcADIRxPackets,
       "tmnxVdoGrpSrcADITxPackets": tmnxVdoGrpSrcADITxPackets,
       "tmnxVdoGrpSrcADIRxSCTE35Msgs": tmnxVdoGrpSrcADIRxSCTE35Msgs,
       "tmnxVdoGrpSrcADIRxSCTE35MsgEnc": tmnxVdoGrpSrcADIRxSCTE35MsgEnc,
       "tmnxVdoGrpSrcADIRxSCTE35MsgUnsup": tmnxVdoGrpSrcADIRxSCTE35MsgUnsup,
       "tmnxVdoGrpSrcADIRxSCTE35MsgDisc": tmnxVdoGrpSrcADIRxSCTE35MsgDisc,
       "tmnxVdoGrpSrcADIUnsuppTSLenPkts": tmnxVdoGrpSrcADIUnsuppTSLenPkts,
       "tmnxVdoGrpSrcRTClientPort": tmnxVdoGrpSrcRTClientPort,
       "tmnxVdoGrpSrcDupSeqNumber": tmnxVdoGrpSrcDupSeqNumber,
       "tmnxVdoGrpSrcRTSTxMcRetPkts": tmnxVdoGrpSrcRTSTxMcRetPkts,
       "tmnxVdoGrpSrcRTSTxMcRetPktsL32": tmnxVdoGrpSrcRTSTxMcRetPktsL32,
       "tmnxVdoGrpSrcRTSTxMcRetPktsH32": tmnxVdoGrpSrcRTSTxMcRetPktsH32,
       "tmnxVdoGrpSrcRTSTxMcRetBytes": tmnxVdoGrpSrcRTSTxMcRetBytes,
       "tmnxVdoGrpSrcRTSTxMcRetBytesL32": tmnxVdoGrpSrcRTSTxMcRetBytesL32,
       "tmnxVdoGrpSrcRTSTxMcRetBytesH32": tmnxVdoGrpSrcRTSTxMcRetBytesH32,
       "tmnxVdoGrpSrcRTSTxMcRetErrs": tmnxVdoGrpSrcRTSTxMcRetErrs,
       "tmnxVdoGrpSrcRTSTxMcRetErrsL32": tmnxVdoGrpSrcRTSTxMcRetErrsL32,
       "tmnxVdoGrpSrcRTSTxMcRetErrsH32": tmnxVdoGrpSrcRTSTxMcRetErrsH32,
       "tmnxVdoGrpSrcRTSRetReqQnc": tmnxVdoGrpSrcRTSRetReqQnc,
       "tmnxVdoGrpSrcRTSRetReqQncL32": tmnxVdoGrpSrcRTSRetReqQncL32,
       "tmnxVdoGrpSrcRTSRetReqQncH32": tmnxVdoGrpSrcRTSRetReqQncH32,
       "tmnxVdoGrpSrcRTSRetReqCrt": tmnxVdoGrpSrcRTSRetReqCrt,
       "tmnxVdoGrpSrcRTSRetReqCrtL32": tmnxVdoGrpSrcRTSRetReqCrtL32,
       "tmnxVdoGrpSrcRTSRetReqCrtH32": tmnxVdoGrpSrcRTSRetReqCrtH32,
       "tmnxVdoGrpSrcRxDupSsrcDrops": tmnxVdoGrpSrcRxDupSsrcDrops,
       "tmnxVdoGrpSrcDupSsrc": tmnxVdoGrpSrcDupSsrc,
       "tmnxVdoGrpSrcFccMinDuration": tmnxVdoGrpSrcFccMinDuration,
       "tmnxVdoGrpSrcAudioReorder": tmnxVdoGrpSrcAudioReorder,
       "tmnxVdoGrpSrcRxBytesSaved": tmnxVdoGrpSrcRxBytesSaved,
       "tmnxVdoGrpSrcRxBytesSavedL32": tmnxVdoGrpSrcRxBytesSavedL32,
       "tmnxVdoGrpSrcRxBytesSavedH32": tmnxVdoGrpSrcRxBytesSavedH32,
       "tmnxVdoGrpSrcRxPacketsSaved": tmnxVdoGrpSrcRxPacketsSaved,
       "tmnxVdoGrpSrcRxPacketsSavedL32": tmnxVdoGrpSrcRxPacketsSavedL32,
       "tmnxVdoGrpSrcRxPacketsSavedH32": tmnxVdoGrpSrcRxPacketsSavedH32,
       "tmnxVdoGrpSrcStatOperBW": tmnxVdoGrpSrcStatOperBW,
       "tmnxVdoGrpSrcRouterIfName": tmnxVdoGrpSrcRouterIfName,
       "tmnxVdoGrpSrcNumFccDentedPkts": tmnxVdoGrpSrcNumFccDentedPkts,
       "tmnxVdoSGStatV1Table": tmnxVdoSGStatV1Table,
       "tmnxVdoSGStatV1Entry": tmnxVdoSGStatV1Entry,
       "tmnxVdoSGV1RxBytesLow32": tmnxVdoSGV1RxBytesLow32,
       "tmnxVdoSGV1RxBytesHigh32": tmnxVdoSGV1RxBytesHigh32,
       "tmnxVdoSGV1RxPacketsLow32": tmnxVdoSGV1RxPacketsLow32,
       "tmnxVdoSGV1RxPacketsHigh32": tmnxVdoSGV1RxPacketsHigh32,
       "tmnxVdoSGV1RxInvalidPacketsLow32": tmnxVdoSGV1RxInvalidPacketsLow32,
       "tmnxVdoSGV1RxInvalidPacketsHgh32": tmnxVdoSGV1RxInvalidPacketsHgh32,
       "tmnxVdoSGV1TxBytesLow32": tmnxVdoSGV1TxBytesLow32,
       "tmnxVdoSGV1TxBytesHigh32": tmnxVdoSGV1TxBytesHigh32,
       "tmnxVdoSGV1TxPacketsLow32": tmnxVdoSGV1TxPacketsLow32,
       "tmnxVdoSGV1TxPacketsHigh32": tmnxVdoSGV1TxPacketsHigh32,
       "tmnxVdoSGV1TxFailedPacketsLow32": tmnxVdoSGV1TxFailedPacketsLow32,
       "tmnxVdoSGV1TxFailedPacketsHigh32": tmnxVdoSGV1TxFailedPacketsHigh32,
       "tmnxVdoSGV1RTClntRxReTxBytsLow32": tmnxVdoSGV1RTClntRxReTxBytsLow32,
       "tmnxVdoSGV1RTClntRxReTxBytsHgh32": tmnxVdoSGV1RTClntRxReTxBytsHgh32,
       "tmnxVdoSGV1RTClntRxReTxPktsLow32": tmnxVdoSGV1RTClntRxReTxPktsLow32,
       "tmnxVdoSGV1RTClntRxReTxPktsHgh32": tmnxVdoSGV1RTClntRxReTxPktsHgh32,
       "tmnxVdoSGV1RTSrvrTxBytesLow32": tmnxVdoSGV1RTSrvrTxBytesLow32,
       "tmnxVdoSGV1RTSrvrTxBytesHigh32": tmnxVdoSGV1RTSrvrTxBytesHigh32,
       "tmnxVdoSGV1RTSrvrTxPacketsLow32": tmnxVdoSGV1RTSrvrTxPacketsLow32,
       "tmnxVdoSGV1RTSrvrTxPacketsHigh32": tmnxVdoSGV1RTSrvrTxPacketsHigh32,
       "tmnxVdoSGV1FCCSrvrTxBytesLow32": tmnxVdoSGV1FCCSrvrTxBytesLow32,
       "tmnxVdoSGV1FCCSrvrTxBytesHigh32": tmnxVdoSGV1FCCSrvrTxBytesHigh32,
       "tmnxVdoSGV1FCCSrvrTxPacketsLow32": tmnxVdoSGV1FCCSrvrTxPacketsLow32,
       "tmnxVdoSGV1FCCSrvrTxPacketsHgh32": tmnxVdoSGV1FCCSrvrTxPacketsHgh32,
       "tmnxVdoSGV1ADIRxPacketsLow32": tmnxVdoSGV1ADIRxPacketsLow32,
       "tmnxVdoSGV1ADIRxPacketsHigh32": tmnxVdoSGV1ADIRxPacketsHigh32,
       "tmnxVdoSGV1ADITxPacketsLow32": tmnxVdoSGV1ADITxPacketsLow32,
       "tmnxVdoSGV1ADITxPacketsHigh32": tmnxVdoSGV1ADITxPacketsHigh32,
       "tmnxVdoSessionTable": tmnxVdoSessionTable,
       "tmnxVdoSessionEntry": tmnxVdoSessionEntry,
       "tmnxVdoSessionSourceAddrType": tmnxVdoSessionSourceAddrType,
       "tmnxVdoSessionSourceAddr": tmnxVdoSessionSourceAddr,
       "tmnxVdoSessionSourcePort": tmnxVdoSessionSourcePort,
       "tmnxVdoSessionSSRCId": tmnxVdoSessionSSRCId,
       "tmnxVdoSessionUpTime": tmnxVdoSessionUpTime,
       "tmnxVdoSessionExpireTime": tmnxVdoSessionExpireTime,
       "tmnxVdoSessionCName": tmnxVdoSessionCName,
       "tmnxVdoSessionDestAddrType": tmnxVdoSessionDestAddrType,
       "tmnxVdoSessionDestAddr": tmnxVdoSessionDestAddr,
       "tmnxVdoSessionRxFCCRequests": tmnxVdoSessionRxFCCRequests,
       "tmnxVdoSessionTxFCCReplies": tmnxVdoSessionTxFCCReplies,
       "tmnxVdoSessionTxFCCPackets": tmnxVdoSessionTxFCCPackets,
       "tmnxVdoSessionTxFCCOctets": tmnxVdoSessionTxFCCOctets,
       "tmnxVdoSessionTxFCCFailedPackets": tmnxVdoSessionTxFCCFailedPackets,
       "tmnxVdoSessionRxRTRequests": tmnxVdoSessionRxRTRequests,
       "tmnxVdoSessionTxRTReplies": tmnxVdoSessionTxRTReplies,
       "tmnxVdoSessionTxRTPackets": tmnxVdoSessionTxRTPackets,
       "tmnxVdoSessionTxRTOctets": tmnxVdoSessionTxRTOctets,
       "tmnxVdoSessionTxRTFailedPackets": tmnxVdoSessionTxRTFailedPackets,
       "tmnxVdoSessionRequestedRtpPkts": tmnxVdoSessionRequestedRtpPkts,
       "tmnxVdoSessionRTReqQuenched": tmnxVdoSessionRTReqQuenched,
       "tmnxVdoSessionRTMcastReqCreated": tmnxVdoSessionRTMcastReqCreated,
       "tmnxVdoSessionPktsLostInSeq10": tmnxVdoSessionPktsLostInSeq10,
       "tmnxVdoSessionPktsLostInSeq20": tmnxVdoSessionPktsLostInSeq20,
       "tmnxVdoSessionPktsLostInSeq30": tmnxVdoSessionPktsLostInSeq30,
       "tmnxVdoSessionPktsLostInSeq40": tmnxVdoSessionPktsLostInSeq40,
       "tmnxVdoSessionPktsLostInSeqMore": tmnxVdoSessionPktsLostInSeqMore,
       "tmnxVdoIfStatTable": tmnxVdoIfStatTable,
       "tmnxVdoIfStatEntry": tmnxVdoIfStatEntry,
       "tmnxVdoIfStatHdRTServerState": tmnxVdoIfStatHdRTServerState,
       "tmnxVdoIfStatSdRTServerState": tmnxVdoIfStatSdRTServerState,
       "tmnxVdoIfStatPipRTServerState": tmnxVdoIfStatPipRTServerState,
       "tmnxVdoIfStatRTSvrSdRtpPktsReq": tmnxVdoIfStatRTSvrSdRtpPktsReq,
       "tmnxVdoIfStatRTSvrHdRtpPktsReq": tmnxVdoIfStatRTSvrHdRtpPktsReq,
       "tmnxVdoIfStatRTSvrPipRtpPktsReq": tmnxVdoIfStatRTSvrPipRtpPktsReq,
       "tmnxVdoIfStatRTSvrRxSdRTReq": tmnxVdoIfStatRTSvrRxSdRTReq,
       "tmnxVdoIfStatRTSvrRxSdFailedReq": tmnxVdoIfStatRTSvrRxSdFailedReq,
       "tmnxVdoIfStatRTSvrRxHdRTReq": tmnxVdoIfStatRTSvrRxHdRTReq,
       "tmnxVdoIfStatRTSvrRxHdFailedReq": tmnxVdoIfStatRTSvrRxHdFailedReq,
       "tmnxVdoIfStatRTSvrRxPipRTReq": tmnxVdoIfStatRTSvrRxPipRTReq,
       "tmnxVdoIfStatRTSvrRxPipFailedReq": tmnxVdoIfStatRTSvrRxPipFailedReq,
       "tmnxVdoIfStatRTSvrTxSdRTReplies": tmnxVdoIfStatRTSvrTxSdRTReplies,
       "tmnxVdoIfStatRTSvrTxSdBytes": tmnxVdoIfStatRTSvrTxSdBytes,
       "tmnxVdoIfStatRTSvrTxSdPackets": tmnxVdoIfStatRTSvrTxSdPackets,
       "tmnxVdoIfStatRTSvrTxHdRTReplies": tmnxVdoIfStatRTSvrTxHdRTReplies,
       "tmnxVdoIfStatRTSvrTxHdBytes": tmnxVdoIfStatRTSvrTxHdBytes,
       "tmnxVdoIfStatRTSvrTxHdPackets": tmnxVdoIfStatRTSvrTxHdPackets,
       "tmnxVdoIfStatRTSvrTxPipRTReplies": tmnxVdoIfStatRTSvrTxPipRTReplies,
       "tmnxVdoIfStatRTSvrTxPipBytes": tmnxVdoIfStatRTSvrTxPipBytes,
       "tmnxVdoIfStatRTSvrTxPipPackets": tmnxVdoIfStatRTSvrTxPipPackets,
       "tmnxVdoIfStatHdFCCServerMode": tmnxVdoIfStatHdFCCServerMode,
       "tmnxVdoIfStatSdFCCServerMode": tmnxVdoIfStatSdFCCServerMode,
       "tmnxVdoIfStatPipFCCServerMode": tmnxVdoIfStatPipFCCServerMode,
       "tmnxVdoIfStatFCCSrRxSdFCCReq": tmnxVdoIfStatFCCSrRxSdFCCReq,
       "tmnxVdoIfStatFCCSrRxSdFailedReq": tmnxVdoIfStatFCCSrRxSdFailedReq,
       "tmnxVdoIfStatFCCSrRxHdFCCReq": tmnxVdoIfStatFCCSrRxHdFCCReq,
       "tmnxVdoIfStatFCCSrRxHdFailedReq": tmnxVdoIfStatFCCSrRxHdFailedReq,
       "tmnxVdoIfStatFCCSrRxPipFCCReq": tmnxVdoIfStatFCCSrRxPipFCCReq,
       "tmnxVdoIfStatFCCSrRxPipFailedReq": tmnxVdoIfStatFCCSrRxPipFailedReq,
       "tmnxVdoIfStatFCCSrTxSdFCCReplies": tmnxVdoIfStatFCCSrTxSdFCCReplies,
       "tmnxVdoIfStatFCCSrTxSdBytes": tmnxVdoIfStatFCCSrTxSdBytes,
       "tmnxVdoIfStatFCCSrTxSdPackets": tmnxVdoIfStatFCCSrTxSdPackets,
       "tmnxVdoIfStatFCCSrTxHdFCCReplies": tmnxVdoIfStatFCCSrTxHdFCCReplies,
       "tmnxVdoIfStatFCCSrTxHdBytes": tmnxVdoIfStatFCCSrTxHdBytes,
       "tmnxVdoIfStatFCCSrTxHdPackets": tmnxVdoIfStatFCCSrTxHdPackets,
       "tmnxVdoIfStatFCCSrTxPipFCCRplies": tmnxVdoIfStatFCCSrTxPipFCCRplies,
       "tmnxVdoIfStatFCCSrTxPipBytes": tmnxVdoIfStatFCCSrTxPipBytes,
       "tmnxVdoIfStatFCCSrTxPipPackets": tmnxVdoIfStatFCCSrTxPipPackets,
       "tmnxVdoIfStatTxFailedPackets": tmnxVdoIfStatTxFailedPackets,
       "tmnxVdoIfScte30TcpSessions": tmnxVdoIfScte30TcpSessions,
       "tmnxVdoIfScte30InitSessions": tmnxVdoIfScte30InitSessions,
       "tmnxVdoIfStatRTSSdMcRdPktsReq": tmnxVdoIfStatRTSSdMcRdPktsReq,
       "tmnxVdoIfStatRTSSdMcRdPktsReqL32": tmnxVdoIfStatRTSSdMcRdPktsReqL32,
       "tmnxVdoIfStatRTSSdMcRdPktsReqH32": tmnxVdoIfStatRTSSdMcRdPktsReqH32,
       "tmnxVdoIfStatRTSHDMcRdPktsReq": tmnxVdoIfStatRTSHDMcRdPktsReq,
       "tmnxVdoIfStatRTSHDMcRdPktsReqL32": tmnxVdoIfStatRTSHDMcRdPktsReqL32,
       "tmnxVdoIfStatRTSHDMcRdPktsReqH32": tmnxVdoIfStatRTSHDMcRdPktsReqH32,
       "tmnxVdoIfStatRTSPipMcRdPktReq": tmnxVdoIfStatRTSPipMcRdPktReq,
       "tmnxVdoIfStatRTSPipMcRdPktReqL32": tmnxVdoIfStatRTSPipMcRdPktReqL32,
       "tmnxVdoIfStatRTSPipMcRdPktReqH32": tmnxVdoIfStatRTSPipMcRdPktReqH32,
       "tmnxVdoIfStatSDPktLostInSeq10": tmnxVdoIfStatSDPktLostInSeq10,
       "tmnxVdoIfStatSDPktLostInSeq20": tmnxVdoIfStatSDPktLostInSeq20,
       "tmnxVdoIfStatSDPktLostInSeq30": tmnxVdoIfStatSDPktLostInSeq30,
       "tmnxVdoIfStatSDPktLostInSeq40": tmnxVdoIfStatSDPktLostInSeq40,
       "tmnxVdoIfStatSDPktLostInSeqMore": tmnxVdoIfStatSDPktLostInSeqMore,
       "tmnxVdoIfStatHDPktLostInSeq10": tmnxVdoIfStatHDPktLostInSeq10,
       "tmnxVdoIfStatHDPktLostInSeq20": tmnxVdoIfStatHDPktLostInSeq20,
       "tmnxVdoIfStatHDPktLostInSeq30": tmnxVdoIfStatHDPktLostInSeq30,
       "tmnxVdoIfStatHDPktLostInSeq40": tmnxVdoIfStatHDPktLostInSeq40,
       "tmnxVdoIfStatHDPktLostInSeqMore": tmnxVdoIfStatHDPktLostInSeqMore,
       "tmnxVdoIfStatPipPktLostInSeq10": tmnxVdoIfStatPipPktLostInSeq10,
       "tmnxVdoIfStatPipPktLostInSeq20": tmnxVdoIfStatPipPktLostInSeq20,
       "tmnxVdoIfStatPipPktLostInSeq30": tmnxVdoIfStatPipPktLostInSeq30,
       "tmnxVdoIfStatPipPktLostInSeq40": tmnxVdoIfStatPipPktLostInSeq40,
       "tmnxVdoIfStatPipPktLostInSeqMore": tmnxVdoIfStatPipPktLostInSeqMore,
       "tmnxVdoIfStLowTable": tmnxVdoIfStLowTable,
       "tmnxVdoIfStLowEntry": tmnxVdoIfStLowEntry,
       "tmnxVdoIfStLowRTSvrSdRtpPktsReq": tmnxVdoIfStLowRTSvrSdRtpPktsReq,
       "tmnxVdoIfStLowRTSvrHdRtpPktsReq": tmnxVdoIfStLowRTSvrHdRtpPktsReq,
       "tmnxVdoIfStLowRTSvrPipRtpPktsReq": tmnxVdoIfStLowRTSvrPipRtpPktsReq,
       "tmnxVdoIfStLowRTSvrRxSdRTReq": tmnxVdoIfStLowRTSvrRxSdRTReq,
       "tmnxVdoIfStLowRTSvrRxSdFailedReq": tmnxVdoIfStLowRTSvrRxSdFailedReq,
       "tmnxVdoIfStLowRTSvrRxHdRTReq": tmnxVdoIfStLowRTSvrRxHdRTReq,
       "tmnxVdoIfStLowRTSvrRxHdFailedReq": tmnxVdoIfStLowRTSvrRxHdFailedReq,
       "tmnxVdoIfStLowRTSvrRxPipRTReq": tmnxVdoIfStLowRTSvrRxPipRTReq,
       "tmnxVdoIfStLowRTSvrRxPipFailedRq": tmnxVdoIfStLowRTSvrRxPipFailedRq,
       "tmnxVdoIfStLowRTSvrTxSdRTReplies": tmnxVdoIfStLowRTSvrTxSdRTReplies,
       "tmnxVdoIfStLowRTSvrTxSdBytes": tmnxVdoIfStLowRTSvrTxSdBytes,
       "tmnxVdoIfStLowRTSvrTxSdPackets": tmnxVdoIfStLowRTSvrTxSdPackets,
       "tmnxVdoIfStLowRTSvrTxHdRTReplies": tmnxVdoIfStLowRTSvrTxHdRTReplies,
       "tmnxVdoIfStLowRTSvrTxHdBytes": tmnxVdoIfStLowRTSvrTxHdBytes,
       "tmnxVdoIfStLowRTSvrTxHdPackets": tmnxVdoIfStLowRTSvrTxHdPackets,
       "tmnxVdoIfStLowRTSvrTxPipRTReplis": tmnxVdoIfStLowRTSvrTxPipRTReplis,
       "tmnxVdoIfStLowRTSvrTxPipBytes": tmnxVdoIfStLowRTSvrTxPipBytes,
       "tmnxVdoIfStLowRTSvrTxPipPackets": tmnxVdoIfStLowRTSvrTxPipPackets,
       "tmnxVdoIfStLowFCCSrRxSdFCCReq": tmnxVdoIfStLowFCCSrRxSdFCCReq,
       "tmnxVdoIfStLowFCCSrRxSdFailedReq": tmnxVdoIfStLowFCCSrRxSdFailedReq,
       "tmnxVdoIfStLowFCCSrRxHdFCCReq": tmnxVdoIfStLowFCCSrRxHdFCCReq,
       "tmnxVdoIfStLowFCCSrRxHdFailedReq": tmnxVdoIfStLowFCCSrRxHdFailedReq,
       "tmnxVdoIfStLowFCCSrRxPipFCCReq": tmnxVdoIfStLowFCCSrRxPipFCCReq,
       "tmnxVdoIfStLowFCCSrRxPipFailedRq": tmnxVdoIfStLowFCCSrRxPipFailedRq,
       "tmnxVdoIfStLowFCCSrTxSdFCCReplis": tmnxVdoIfStLowFCCSrTxSdFCCReplis,
       "tmnxVdoIfStLowFCCSrTxSdBytes": tmnxVdoIfStLowFCCSrTxSdBytes,
       "tmnxVdoIfStLowFCCSrTxSdPackets": tmnxVdoIfStLowFCCSrTxSdPackets,
       "tmnxVdoIfStLowFCCSrTxHdFCCReplis": tmnxVdoIfStLowFCCSrTxHdFCCReplis,
       "tmnxVdoIfStLowFCCSrTxHdBytes": tmnxVdoIfStLowFCCSrTxHdBytes,
       "tmnxVdoIfStLowFCCSrTxHdPackets": tmnxVdoIfStLowFCCSrTxHdPackets,
       "tmnxVdoIfStLowFCCSrTxPipFCCRplis": tmnxVdoIfStLowFCCSrTxPipFCCRplis,
       "tmnxVdoIfStLowFCCSrTxPipBytes": tmnxVdoIfStLowFCCSrTxPipBytes,
       "tmnxVdoIfStLowFCCSrTxPipPackets": tmnxVdoIfStLowFCCSrTxPipPackets,
       "tmnxVdoIfStLowTxFailedPackets": tmnxVdoIfStLowTxFailedPackets,
       "tmnxVdoIfStHghTable": tmnxVdoIfStHghTable,
       "tmnxVdoIfStHghEntry": tmnxVdoIfStHghEntry,
       "tmnxVdoIfStHghRTSvrSdRtpPktsReq": tmnxVdoIfStHghRTSvrSdRtpPktsReq,
       "tmnxVdoIfStHghRTSvrHdRtpPktsReq": tmnxVdoIfStHghRTSvrHdRtpPktsReq,
       "tmnxVdoIfStHghRTSvrPipRtpPktsReq": tmnxVdoIfStHghRTSvrPipRtpPktsReq,
       "tmnxVdoIfStHghRTSvrRxSdRTReq": tmnxVdoIfStHghRTSvrRxSdRTReq,
       "tmnxVdoIfStHghRTSvrRxSdFailedReq": tmnxVdoIfStHghRTSvrRxSdFailedReq,
       "tmnxVdoIfStHghRTSvrRxHdRTReq": tmnxVdoIfStHghRTSvrRxHdRTReq,
       "tmnxVdoIfStHghRTSvrRxHdFailedReq": tmnxVdoIfStHghRTSvrRxHdFailedReq,
       "tmnxVdoIfStHghRTSvrRxPipRTReq": tmnxVdoIfStHghRTSvrRxPipRTReq,
       "tmnxVdoIfStHghRTSvrRxPipFailedRq": tmnxVdoIfStHghRTSvrRxPipFailedRq,
       "tmnxVdoIfStHghRTSvrTxSdRTReplies": tmnxVdoIfStHghRTSvrTxSdRTReplies,
       "tmnxVdoIfStHghRTSvrTxSdBytes": tmnxVdoIfStHghRTSvrTxSdBytes,
       "tmnxVdoIfStHghRTSvrTxSdPackets": tmnxVdoIfStHghRTSvrTxSdPackets,
       "tmnxVdoIfStHghRTSvrTxHdRTReplies": tmnxVdoIfStHghRTSvrTxHdRTReplies,
       "tmnxVdoIfStHghRTSvrTxHdBytes": tmnxVdoIfStHghRTSvrTxHdBytes,
       "tmnxVdoIfStHghRTSvrTxHdPackets": tmnxVdoIfStHghRTSvrTxHdPackets,
       "tmnxVdoIfStHghRTSvrTxPipRTReplis": tmnxVdoIfStHghRTSvrTxPipRTReplis,
       "tmnxVdoIfStHghRTSvrTxPipBytes": tmnxVdoIfStHghRTSvrTxPipBytes,
       "tmnxVdoIfStHghRTSvrTxPipPackets": tmnxVdoIfStHghRTSvrTxPipPackets,
       "tmnxVdoIfStHghFCCSrRxSdFCCReq": tmnxVdoIfStHghFCCSrRxSdFCCReq,
       "tmnxVdoIfStHghFCCSrRxSdFailedReq": tmnxVdoIfStHghFCCSrRxSdFailedReq,
       "tmnxVdoIfStHghFCCSrRxHdFCCReq": tmnxVdoIfStHghFCCSrRxHdFCCReq,
       "tmnxVdoIfStHghFCCSrRxHdFailedReq": tmnxVdoIfStHghFCCSrRxHdFailedReq,
       "tmnxVdoIfStHghFCCSrRxPipFCCReq": tmnxVdoIfStHghFCCSrRxPipFCCReq,
       "tmnxVdoIfStHghFCCSrRxPipFailedRq": tmnxVdoIfStHghFCCSrRxPipFailedRq,
       "tmnxVdoIfStHghFCCSrTxSdFCCReplis": tmnxVdoIfStHghFCCSrTxSdFCCReplis,
       "tmnxVdoIfStHghFCCSrTxSdBytes": tmnxVdoIfStHghFCCSrTxSdBytes,
       "tmnxVdoIfStHghFCCSrTxSdPackets": tmnxVdoIfStHghFCCSrTxSdPackets,
       "tmnxVdoIfStHghFCCSrTxHdFCCReplis": tmnxVdoIfStHghFCCSrTxHdFCCReplis,
       "tmnxVdoIfStHghFCCSrTxHdBytes": tmnxVdoIfStHghFCCSrTxHdBytes,
       "tmnxVdoIfStHghFCCSrTxHdPackets": tmnxVdoIfStHghFCCSrTxHdPackets,
       "tmnxVdoIfStHghFCCSrTxPipFCCRplis": tmnxVdoIfStHghFCCSrTxPipFCCRplis,
       "tmnxVdoIfStHghFCCSrTxPipBytes": tmnxVdoIfStHghFCCSrTxPipBytes,
       "tmnxVdoIfStHghFCCSrTxPipPackets": tmnxVdoIfStHghFCCSrTxPipPackets,
       "tmnxVdoIfStHghTxFailedPackets": tmnxVdoIfStHghTxFailedPackets,
       "tmnxVdoPIDTable": tmnxVdoPIDTable,
       "tmnxVdoPIDEntry": tmnxVdoPIDEntry,
       "tmnxVdoPID": tmnxVdoPID,
       "tmnxVdoPIDType": tmnxVdoPIDType,
       "tmnxVdoPIDMpegStreamType": tmnxVdoPIDMpegStreamType,
       "tmnxVdoPIDLanguage": tmnxVdoPIDLanguage,
       "tmnxVdoPIDCcErrSecs": tmnxVdoPIDCcErrSecs,
       "tmnxVdoPIDTeiErrSecs": tmnxVdoPIDTeiErrSecs,
       "tmnxVdoPIDAbsentErrSecs": tmnxVdoPIDAbsentErrSecs,
       "tmnxVdoPIDBitrate": tmnxVdoPIDBitrate,
       "tmnxVdoPIDIsPCR": tmnxVdoPIDIsPCR,
       "tmnxVdoIfScte30AdSrvrTable": tmnxVdoIfScte30AdSrvrTable,
       "tmnxVdoIfScte30AdSrvrEntry": tmnxVdoIfScte30AdSrvrEntry,
       "tmnxVdoIfScte30AdSrvrAddrType": tmnxVdoIfScte30AdSrvrAddrType,
       "tmnxVdoIfScte30AdSrvrAddr": tmnxVdoIfScte30AdSrvrAddr,
       "tmnxVdoIfScte30AdSrvrRowStatus": tmnxVdoIfScte30AdSrvrRowStatus,
       "tmnxVdoSGAdiStatTable": tmnxVdoSGAdiStatTable,
       "tmnxVdoSGAdiStatEntry": tmnxVdoSGAdiStatEntry,
       "tmnxVdoSGAdiServerAddrType": tmnxVdoSGAdiServerAddrType,
       "tmnxVdoSGAdiServerAddr": tmnxVdoSGAdiServerAddr,
       "tmnxVdoSGAdiServerUptime": tmnxVdoSGAdiServerUptime,
       "tmnxVdoSGAdiInitReq": tmnxVdoSGAdiInitReq,
       "tmnxVdoSGAdiSucInitResp": tmnxVdoSGAdiSucInitResp,
       "tmnxVdoSGAdiUnsucInitResp": tmnxVdoSGAdiUnsucInitResp,
       "tmnxVdoSGAdiAliveReq": tmnxVdoSGAdiAliveReq,
       "tmnxVdoSGAdiSucAliveResp": tmnxVdoSGAdiSucAliveResp,
       "tmnxVdoSGAdiUnSucAliveResp": tmnxVdoSGAdiUnSucAliveResp,
       "tmnxVdoSGAdiCueReq": tmnxVdoSGAdiCueReq,
       "tmnxVdoSGAdiSucCueResp": tmnxVdoSGAdiSucCueResp,
       "tmnxVdoSGAdiUnsucCueResp": tmnxVdoSGAdiUnsucCueResp,
       "tmnxVdoSGAdiAbortReq": tmnxVdoSGAdiAbortReq,
       "tmnxVdoSGAdiSucAbortResp": tmnxVdoSGAdiSucAbortResp,
       "tmnxVdoSGAdiUnsucAbortResp": tmnxVdoSGAdiUnsucAbortResp,
       "tmnxVdoSGAdiUnknownSCTE30Req": tmnxVdoSGAdiUnknownSCTE30Req,
       "tmnxVdoSGAdiSpliceReq": tmnxVdoSGAdiSpliceReq,
       "tmnxVdoSGAdiSucSpliceResp": tmnxVdoSGAdiSucSpliceResp,
       "tmnxVdoSGAdiUnsucSpliceResp": tmnxVdoSGAdiUnsucSpliceResp,
       "tmnxVdoSGAdiSucSpliceInCompResp": tmnxVdoSGAdiSucSpliceInCompResp,
       "tmnxVdoSGAdiSucSpliceOutCompResp": tmnxVdoSGAdiSucSpliceOutCompResp,
       "tmnxVdoSGAdiUnsucSpliceOutComRes": tmnxVdoSGAdiUnsucSpliceOutComRes,
       "tmnxVdoSGAdiMinPort": tmnxVdoSGAdiMinPort,
       "tmnxVdoSGAdiMaxPort": tmnxVdoSGAdiMaxPort,
       "tmnxVdoSGAdiChlName": tmnxVdoSGAdiChlName,
       "tmnxVdoSGSpliceStatusTable": tmnxVdoSGSpliceStatusTable,
       "tmnxVdoSGSpliceStatusEntry": tmnxVdoSGSpliceStatusEntry,
       "tmnxVdoSGSpliceStartTime": tmnxVdoSGSpliceStartTime,
       "tmnxVdoSGSpliceAdServerAddrType": tmnxVdoSGSpliceAdServerAddrType,
       "tmnxVdoSGSpliceAdServerAddr": tmnxVdoSGSpliceAdServerAddr,
       "tmnxVdoSGSpliceStatus": tmnxVdoSGSpliceStatus,
       "tmnxVdoSGSpliceDurationReq": tmnxVdoSGSpliceDurationReq,
       "tmnxVdoSGSpliceDurationPlayed": tmnxVdoSGSpliceDurationPlayed,
       "tmnxVdoSGSpliceRate": tmnxVdoSGSpliceRate,
       "tmnxVdoSGSpliceSessionId": tmnxVdoSGSpliceSessionId,
       "tmnxVdoSGSplicePriorSessionId": tmnxVdoSGSplicePriorSessionId,
       "tmnxVdoSGSpliceAbortReason": tmnxVdoSGSpliceAbortReason,
       "tmnxVdoSGSpliceSpliceInSeqNum": tmnxVdoSGSpliceSpliceInSeqNum,
       "tmnxVdoSGSpliceSpliceOutSeqNum": tmnxVdoSGSpliceSpliceOutSeqNum,
       "tmnxVdoSGSpliceNumBlkFrames": tmnxVdoSGSpliceNumBlkFrames,
       "tmnxVdoSGSpliceBlkFramePTS": tmnxVdoSGSpliceBlkFramePTS,
       "tmnxVdoSGSpliceMaxAdPTS": tmnxVdoSGSpliceMaxAdPTS,
       "tmnxVdoSGSpliceMinNwPTS": tmnxVdoSGSpliceMinNwPTS,
       "tmnxVdoIfStatExtTable": tmnxVdoIfStatExtTable,
       "tmnxVdoIfStatExtEntry": tmnxVdoIfStatExtEntry,
       "tmnxVdoIfStatExtRxRtcpAppRepSum": tmnxVdoIfStatExtRxRtcpAppRepSum,
       "tmnxVdoIfStatExtRxRtcpAppRepSumL": tmnxVdoIfStatExtRxRtcpAppRepSumL,
       "tmnxVdoIfStatExtRxRtcpAppRepSumH": tmnxVdoIfStatExtRxRtcpAppRepSumH,
       "tmnxVdoIfStatExtRxRtcpAppReqSum": tmnxVdoIfStatExtRxRtcpAppReqSum,
       "tmnxVdoIfStatExtRxRtcpAppReqSumL": tmnxVdoIfStatExtRxRtcpAppReqSumL,
       "tmnxVdoIfStatExtRxRtcpAppReqSumH": tmnxVdoIfStatExtRxRtcpAppReqSumH,
       "tmnxVdoIfStatExtRxRtcpFbRepSum": tmnxVdoIfStatExtRxRtcpFbRepSum,
       "tmnxVdoIfStatExtRxRtcpFbRepSumL": tmnxVdoIfStatExtRxRtcpFbRepSumL,
       "tmnxVdoIfStatExtRxRtcpFbRepSumH": tmnxVdoIfStatExtRxRtcpFbRepSumH,
       "tmnxVdoIfStatExtRxRtcpFbReqSum": tmnxVdoIfStatExtRxRtcpFbReqSum,
       "tmnxVdoIfStatExtRxRtcpFbReqSumL": tmnxVdoIfStatExtRxRtcpFbReqSumL,
       "tmnxVdoIfStatExtRxRtcpFbReqSumH": tmnxVdoIfStatExtRxRtcpFbReqSumH,
       "tmnxVdoIfStatExtRxRudpFbRepSum": tmnxVdoIfStatExtRxRudpFbRepSum,
       "tmnxVdoIfStatExtRxRudpFbRepSumL": tmnxVdoIfStatExtRxRudpFbRepSumL,
       "tmnxVdoIfStatExtRxRudpFbRepSumH": tmnxVdoIfStatExtRxRudpFbRepSumH,
       "tmnxVdoIfStatExtTxFccPktsSum": tmnxVdoIfStatExtTxFccPktsSum,
       "tmnxVdoIfStatExtTxFccPktsSumL": tmnxVdoIfStatExtTxFccPktsSumL,
       "tmnxVdoIfStatExtTxFccPktsSumH": tmnxVdoIfStatExtTxFccPktsSumH,
       "tmnxVdoIfStatExtTxFccOctetsSum": tmnxVdoIfStatExtTxFccOctetsSum,
       "tmnxVdoIfStatExtTxFccOctetsSumL": tmnxVdoIfStatExtTxFccOctetsSumL,
       "tmnxVdoIfStatExtTxFccOctetsSumH": tmnxVdoIfStatExtTxFccOctetsSumH,
       "tmnxVdoIfStatExtTxRetPktsSum": tmnxVdoIfStatExtTxRetPktsSum,
       "tmnxVdoIfStatExtTxRetPktsSumL": tmnxVdoIfStatExtTxRetPktsSumL,
       "tmnxVdoIfStatExtTxRetPktsSumH": tmnxVdoIfStatExtTxRetPktsSumH,
       "tmnxVdoIfStatExtTxRetOctetsSum": tmnxVdoIfStatExtTxRetOctetsSum,
       "tmnxVdoIfStatExtTxRetOctetsSumL": tmnxVdoIfStatExtTxRetOctetsSumL,
       "tmnxVdoIfStatExtTxRetOctetsSumH": tmnxVdoIfStatExtTxRetOctetsSumH,
       "tmnxVdoIfStatExtTxRudpPktsSum": tmnxVdoIfStatExtTxRudpPktsSum,
       "tmnxVdoIfStatExtTxRudpPktsSumL": tmnxVdoIfStatExtTxRudpPktsSumL,
       "tmnxVdoIfStatExtTxRudpPktsSumH": tmnxVdoIfStatExtTxRudpPktsSumH,
       "tmnxVdoIfStatExtTxRudpByteSum": tmnxVdoIfStatExtTxRudpByteSum,
       "tmnxVdoIfStatExtTxRudpByteSumL": tmnxVdoIfStatExtTxRudpByteSumL,
       "tmnxVdoIfStatExtTxRudpByteSumH": tmnxVdoIfStatExtTxRudpByteSumH,
       "tmnxVdoGrpSrcVqmStatTable": tmnxVdoGrpSrcVqmStatTable,
       "tmnxVdoGrpSrcVqmStatEntry": tmnxVdoGrpSrcVqmStatEntry,
       "tmnxVdoGrpSrcVqmStatsPeriod": tmnxVdoGrpSrcVqmStatsPeriod,
       "tmnxVdoGrpSrcVqmStatsTime": tmnxVdoGrpSrcVqmStatsTime,
       "tmnxVdoGrpSrcVqmGoodSecs": tmnxVdoGrpSrcVqmGoodSecs,
       "tmnxVdoGrpSrcVqmErrSecs": tmnxVdoGrpSrcVqmErrSecs,
       "tmnxVdoGrpSrcVqmDegrSecs": tmnxVdoGrpSrcVqmDegrSecs,
       "tmnxVdoGrpSrcVqmImpairSecs": tmnxVdoGrpSrcVqmImpairSecs,
       "tmnxVdoGrpSrcVqmPmtRepErrSecs": tmnxVdoGrpSrcVqmPmtRepErrSecs,
       "tmnxVdoGrpSrcVqmPmtRepDegSecs": tmnxVdoGrpSrcVqmPmtRepDegSecs,
       "tmnxVdoGrpSrcVqmPmtRepImpSecs": tmnxVdoGrpSrcVqmPmtRepImpSecs,
       "tmnxVdoGrpSrcVqmPmtSyntxErrSecs": tmnxVdoGrpSrcVqmPmtSyntxErrSecs,
       "tmnxVdoGrpSrcVqmPatRepErrSecs": tmnxVdoGrpSrcVqmPatRepErrSecs,
       "tmnxVdoGrpSrcVqmPatRepDegSecs": tmnxVdoGrpSrcVqmPatRepDegSecs,
       "tmnxVdoGrpSrcVqmPatRepImpSecs": tmnxVdoGrpSrcVqmPatRepImpSecs,
       "tmnxVdoGrpSrcVqmPatSyntxErrSecs": tmnxVdoGrpSrcVqmPatSyntxErrSecs,
       "tmnxVdoGrpSrcVqmPcrRepErrSecs": tmnxVdoGrpSrcVqmPcrRepErrSecs,
       "tmnxVdoGrpSrcVqmPcrRepDegSecs": tmnxVdoGrpSrcVqmPcrRepDegSecs,
       "tmnxVdoGrpSrcVqmPcrRepImpSecs": tmnxVdoGrpSrcVqmPcrRepImpSecs,
       "tmnxVdoGrpSrcVqmSyncByteErrSecs": tmnxVdoGrpSrcVqmSyncByteErrSecs,
       "tmnxVdoGrpSrcVqmSyncLossSecs": tmnxVdoGrpSrcVqmSyncLossSecs,
       "tmnxVdoGrpSrcVqmCatErrSecs": tmnxVdoGrpSrcVqmCatErrSecs,
       "tmnxVdoGrpSrcVqmUnrefPidErrSecs": tmnxVdoGrpSrcVqmUnrefPidErrSecs,
       "tmnxVdoGrpSrcVqmMDIDelayFactor": tmnxVdoGrpSrcVqmMDIDelayFactor,
       "tmnxVdoGrpSrcVqmMDILossRate": tmnxVdoGrpSrcVqmMDILossRate,
       "tmnxVdoGrpSrcVqmMinGOPLength": tmnxVdoGrpSrcVqmMinGOPLength,
       "tmnxVdoGrpSrcVqmMinFrmPerSec": tmnxVdoGrpSrcVqmMinFrmPerSec,
       "tmnxVdoGrpSrcVqmAvgGOPLength": tmnxVdoGrpSrcVqmAvgGOPLength,
       "tmnxVdoGrpSrcVqmAvgFrmPerSec": tmnxVdoGrpSrcVqmAvgFrmPerSec,
       "tmnxVdoGrpSrcVqmMaxGOPLength": tmnxVdoGrpSrcVqmMaxGOPLength,
       "tmnxVdoGrpSrcVqmMaxFrmPerSec": tmnxVdoGrpSrcVqmMaxFrmPerSec,
       "tmnxVdoGrpSrcVqmGoodIFrames": tmnxVdoGrpSrcVqmGoodIFrames,
       "tmnxVdoGrpSrcVqmBadIFrames": tmnxVdoGrpSrcVqmBadIFrames,
       "tmnxVdoGrpSrcVqmGoodPFrames": tmnxVdoGrpSrcVqmGoodPFrames,
       "tmnxVdoGrpSrcVqmBadPFrames": tmnxVdoGrpSrcVqmBadPFrames,
       "tmnxVdoGrpSrcVqmGoodBFrames": tmnxVdoGrpSrcVqmGoodBFrames,
       "tmnxVdoGrpSrcVqmBadBFrames": tmnxVdoGrpSrcVqmBadBFrames,
       "tmnxVdoGrpSrcVqmTrafficLossSecs": tmnxVdoGrpSrcVqmTrafficLossSecs,
       "tmnxVdoGrpSrcVqmSCTE35ErrSecs": tmnxVdoGrpSrcVqmSCTE35ErrSecs,
       "tmnxVdoGrpSrcVqmTable": tmnxVdoGrpSrcVqmTable,
       "tmnxVdoGrpSrcVqmEntry": tmnxVdoGrpSrcVqmEntry,
       "tmnxVdoGrpSrcVqmOperAnalyzerSt": tmnxVdoGrpSrcVqmOperAnalyzerSt,
       "tmnxVdoGrpSrcVqmOperCcError": tmnxVdoGrpSrcVqmOperCcError,
       "tmnxVdoGrpSrcVqmOperPatRepError": tmnxVdoGrpSrcVqmOperPatRepError,
       "tmnxVdoGrpSrcVqmOperTncPatRep": tmnxVdoGrpSrcVqmOperTncPatRep,
       "tmnxVdoGrpSrcVqmOperQosPatRep": tmnxVdoGrpSrcVqmOperQosPatRep,
       "tmnxVdoGrpSrcVqmOperPoaPatRep": tmnxVdoGrpSrcVqmOperPoaPatRep,
       "tmnxVdoGrpSrcVqmOperPatSyntax": tmnxVdoGrpSrcVqmOperPatSyntax,
       "tmnxVdoGrpSrcVqmOperPcrRepError": tmnxVdoGrpSrcVqmOperPcrRepError,
       "tmnxVdoGrpSrcVqmOperTncPcrRep": tmnxVdoGrpSrcVqmOperTncPcrRep,
       "tmnxVdoGrpSrcVqmOperQosPcrRep": tmnxVdoGrpSrcVqmOperQosPcrRep,
       "tmnxVdoGrpSrcVqmOperPoaPcrRep": tmnxVdoGrpSrcVqmOperPoaPcrRep,
       "tmnxVdoGrpSrcVqmOperVidPIDAbs": tmnxVdoGrpSrcVqmOperVidPIDAbs,
       "tmnxVdoGrpSrcVqmOperPIDPmtUnref": tmnxVdoGrpSrcVqmOperPIDPmtUnref,
       "tmnxVdoGrpSrcVqmOperPmtRepError": tmnxVdoGrpSrcVqmOperPmtRepError,
       "tmnxVdoGrpSrcVqmOperTncPmtRep": tmnxVdoGrpSrcVqmOperTncPmtRep,
       "tmnxVdoGrpSrcVqmOperQosPmtRep": tmnxVdoGrpSrcVqmOperQosPmtRep,
       "tmnxVdoGrpSrcVqmOperPoaPmtRep": tmnxVdoGrpSrcVqmOperPoaPmtRep,
       "tmnxVdoGrpSrcVqmOperPmtSyntax": tmnxVdoGrpSrcVqmOperPmtSyntax,
       "tmnxVdoGrpSrcVqmOperSCTE35Error": tmnxVdoGrpSrcVqmOperSCTE35Error,
       "tmnxVdoGrpSrcVqmOperTeiError": tmnxVdoGrpSrcVqmOperTeiError,
       "tmnxVdoGrpSrcVqmOperTsSyncLoss": tmnxVdoGrpSrcVqmOperTsSyncLoss,
       "tmnxVdoGrpSrcVqmOperNonVidPIDAbs": tmnxVdoGrpSrcVqmOperNonVidPIDAbs,
       "tmnxVdoGrpSrcVqmOperReportAlarm": tmnxVdoGrpSrcVqmOperReportAlarm,
       "tmnxVdoGrpSrcStatExtTable": tmnxVdoGrpSrcStatExtTable,
       "tmnxVdoGrpSrcStatExtEntry": tmnxVdoGrpSrcStatExtEntry,
       "tmnxVdoGrpSrcExtMaxRtpTsDelta": tmnxVdoGrpSrcExtMaxRtpTsDelta,
       "tmnxVdoGrpSrcExtMaxTicksDelta": tmnxVdoGrpSrcExtMaxTicksDelta,
       "tmnxVdoGrpSrcExtMaxTicksDeltaL32": tmnxVdoGrpSrcExtMaxTicksDeltaL32,
       "tmnxVdoGrpSrcExtMaxTicksDeltaH32": tmnxVdoGrpSrcExtMaxTicksDeltaH32,
       "tmnxVdoGrpSrcExtCurTsJitter": tmnxVdoGrpSrcExtCurTsJitter,
       "tmnxVdoGrpSrcExtCurTsJitterL32": tmnxVdoGrpSrcExtCurTsJitterL32,
       "tmnxVdoGrpSrcExtCurTsJitterH32": tmnxVdoGrpSrcExtCurTsJitterH32,
       "tmnxVdoGrpSrcExtMaxTsJitter": tmnxVdoGrpSrcExtMaxTsJitter,
       "tmnxVdoGrpSrcExtMaxTsJitterL32": tmnxVdoGrpSrcExtMaxTsJitterL32,
       "tmnxVdoGrpSrcExtMaxTsJitterH32": tmnxVdoGrpSrcExtMaxTsJitterH32,
       "tmnxVdoGlobalObjs": tmnxVdoGlobalObjs,
       "tmnxVdoIfTableLastChanged": tmnxVdoIfTableLastChanged,
       "tmnxVdoIfAddrTableLastChanged": tmnxVdoIfAddrTableLastChanged,
       "tmnxVdoGrpTableLastChanged": tmnxVdoGrpTableLastChanged,
       "tmnxVdoGrpMDATableLastChanged": tmnxVdoGrpMDATableLastChanged,
       "tmnxVdoAdiChlTableLastChanged": tmnxVdoAdiChlTableLastChanged,
       "tmnxVdoAdiZoneChlTableLastChngd": tmnxVdoAdiZoneChlTableLastChngd,
       "tmnxVdoIfScte30AdSrvrTblLstChngd": tmnxVdoIfScte30AdSrvrTblLstChngd,
       "tmnxVdoNotificationObjs": tmnxVdoNotificationObjs,
       "tmnxVdoNotifysvcId": tmnxVdoNotifysvcId,
       "tmnxVdoNotifyIfName": tmnxVdoNotifyIfName,
       "tmnxVdoNotifyGrpAddrType": tmnxVdoNotifyGrpAddrType,
       "tmnxVdoNotifyGroupAddress": tmnxVdoNotifyGroupAddress,
       "tmnxVdoNotifySrcAddrType": tmnxVdoNotifySrcAddrType,
       "tmnxVdoNotifySourceAddress": tmnxVdoNotifySourceAddress,
       "tmnxVdoNotifyAdSpliceSessionId": tmnxVdoNotifyAdSpliceSessionId,
       "tmnxVdoNotifyAdSpliceAbortTime": tmnxVdoNotifyAdSpliceAbortTime,
       "tmnxVdoNotifyAdSpliceDuration": tmnxVdoNotifyAdSpliceDuration,
       "tmnxVdoNotifyClientAddrType": tmnxVdoNotifyClientAddrType,
       "tmnxVdoNotifyClientAddress": tmnxVdoNotifyClientAddress,
       "tmnxVdoNotifyAnalyzerState": tmnxVdoNotifyAnalyzerState,
       "tmnxVdoNotifyPrefix": tmnxVdoNotifyPrefix,
       "tmnxVdoNotifications": tmnxVdoNotifications,
       "tmnxVdoDuplicateSsrcId": tmnxVdoDuplicateSsrcId,
       "tmnxVdoMdaSessionsLimitExceeded": tmnxVdoMdaSessionsLimitExceeded,
       "tmnxVdoMdaSGLimitExceeded": tmnxVdoMdaSGLimitExceeded,
       "tmnxVdoMdaSessionsLimitCleared": tmnxVdoMdaSessionsLimitCleared,
       "tmnxVdoMdaSGLimitCleared": tmnxVdoMdaSGLimitCleared,
       "tmnxVdoAdSpliceAbort": tmnxVdoAdSpliceAbort,
       "tmnxVdoClientSessionsLmtExceeded": tmnxVdoClientSessionsLmtExceeded,
       "tmnxVdoClientSessionsLmtCleared": tmnxVdoClientSessionsLmtCleared,
       "tmnxVdoGrpSrcAnlyzrErrState": tmnxVdoGrpSrcAnlyzrErrState,
       "tmnxVdoGrpSrcAnlyzrStClear": tmnxVdoGrpSrcAnlyzrStClear}
)
