# SNMP MIB module (ZYXEL-ves1608FE57-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ves1608FE57-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:20:55 2025
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

(BridgeId,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus")

(HCPerfIntervalThreshold,
 HCPerfTimeElapsed) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalThreshold",
    "HCPerfTimeElapsed")

(Dot1agCfmMepId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qVlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(vdslLineAlarmConfProfileName,
 vdslLineConfProfileName,
 vdslPerf1DayIntervalNumber,
 vdslPerfIntervalNumber,
 vdslPhysSide) = mibBuilder.importSymbols(
    "VDSL-LINE-MIB",
    "vdslLineAlarmConfProfileName",
    "vdslLineConfProfileName",
    "vdslPerf1DayIntervalNumber",
    "vdslPerfIntervalNumber",
    "vdslPhysSide")

(xdsl2ChAlarmConfProfileName,
 xdsl2ChConfProfProfileName,
 xdsl2LAlarmConfTempTemplateName,
 xdsl2LConfProfProfileName,
 xdsl2LConfTempTemplateName,
 xdsl2LineAlarmConfProfileName,
 xdsl2LineBand,
 xdsl2LineSegment,
 xdsl2LineSegmentDirection,
 xdsl2PMChCurrUnit,
 xdsl2PMChHist15MInterval,
 xdsl2PMChHist15MUnit,
 xdsl2PMChHist1DInterval,
 xdsl2PMChHist1DUnit,
 xdsl2PMLCurrUnit,
 xdsl2PMLHist15MInterval,
 xdsl2PMLHist15MUnit,
 xdsl2PMLHist1DInterval,
 xdsl2PMLHist1DUnit,
 xdsl2SCStatusBand,
 xdsl2SCStatusDirection) = mibBuilder.importSymbols(
    "VDSL2-LINE-MIB",
    "xdsl2ChAlarmConfProfileName",
    "xdsl2ChConfProfProfileName",
    "xdsl2LAlarmConfTempTemplateName",
    "xdsl2LConfProfProfileName",
    "xdsl2LConfTempTemplateName",
    "xdsl2LineAlarmConfProfileName",
    "xdsl2LineBand",
    "xdsl2LineSegment",
    "xdsl2LineSegmentDirection",
    "xdsl2PMChCurrUnit",
    "xdsl2PMChHist15MInterval",
    "xdsl2PMChHist15MUnit",
    "xdsl2PMChHist1DInterval",
    "xdsl2PMChHist1DUnit",
    "xdsl2PMLCurrUnit",
    "xdsl2PMLHist15MInterval",
    "xdsl2PMLHist15MUnit",
    "xdsl2PMLHist1DInterval",
    "xdsl2PMLHist1DUnit",
    "xdsl2SCStatusBand",
    "xdsl2SCStatusDirection")

(Xdsl2LineLdsf,
 Xdsl2RaMode) = mibBuilder.importSymbols(
    "VDSL2-LINE-TC-MIB",
    "Xdsl2LineLdsf",
    "Xdsl2RaMode")


# MODULE-IDENTITY

ves1608FE57 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Vdsl2Band(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2),
          ("us0", 3),
          ("ds1", 4),
          ("us1", 5),
          ("ds2", 6),
          ("us2", 7),
          ("ds3", 8),
          ("us3", 9),
          ("ds4", 10),
          ("us4", 11))
    )



class UtcTimeStamp(TextualConvention, Unsigned32):
    status = "current"


class EventIdNumber(TextualConvention, Integer32):
    status = "current"


class EventSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("informational", 4))
    )



class EventServiceAffective(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noServiceAffected", 1),
          ("serviceAffected", 2))
    )



class InstanceType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("node", 2),
          ("shelf", 3),
          ("line", 4),
          ("switch", 5),
          ("lsp", 6),
          ("l2Interface", 7),
          ("l3Interface", 8),
          ("rowIndex", 9))
    )



class EventPersistence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("delta", 2))
    )



class MstiOrCistInstanceIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_VesSeries_ObjectIdentity = ObjectIdentity
vesSeries = _VesSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1)
)
_SysSwPlatformMajorVers_Type = Integer32
_SysSwPlatformMajorVers_Object = MibScalar
sysSwPlatformMajorVers = _SysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 1),
    _SysSwPlatformMajorVers_Type()
)
sysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setStatus("current")
_SysSwPlatformMinorVers_Type = Integer32
_SysSwPlatformMinorVers_Object = MibScalar
sysSwPlatformMinorVers = _SysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 2),
    _SysSwPlatformMinorVers_Type()
)
sysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setStatus("current")
_SysSwModelString_Type = DisplayString
_SysSwModelString_Object = MibScalar
sysSwModelString = _SysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 3),
    _SysSwModelString_Type()
)
sysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModelString.setStatus("current")
_SysSwVersionControlNbr_Type = Integer32
_SysSwVersionControlNbr_Object = MibScalar
sysSwVersionControlNbr = _SysSwVersionControlNbr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 4),
    _SysSwVersionControlNbr_Type()
)
sysSwVersionControlNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionControlNbr.setStatus("current")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 5),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("current")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 6),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("current")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 7),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("current")
_SysHwMajorVers_Type = Integer32
_SysHwMajorVers_Object = MibScalar
sysHwMajorVers = _SysHwMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 8),
    _SysHwMajorVers_Type()
)
sysHwMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVers.setStatus("current")
_SysHwMinorVers_Type = Integer32
_SysHwMinorVers_Object = MibScalar
sysHwMinorVers = _SysHwMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 9),
    _SysHwMinorVers_Type()
)
sysHwMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVers.setStatus("current")
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 10),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("current")
_SysFirmwareVersion_Type = DisplayString
_SysFirmwareVersion_Object = MibScalar
sysFirmwareVersion = _SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 11),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("current")
_SysModemCodeVersion_Type = DisplayString
_SysModemCodeVersion_Object = MibScalar
sysModemCodeVersion = _SysModemCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 12),
    _SysModemCodeVersion_Type()
)
sysModemCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModemCodeVersion.setStatus("current")
_SysPowerInfo_Type = DisplayString
_SysPowerInfo_Object = MibScalar
sysPowerInfo = _SysPowerInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 13),
    _SysPowerInfo_Type()
)
sysPowerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPowerInfo.setStatus("current")


class _SysSwBootUpImage_Type(Integer32):
    """Custom type sysSwBootUpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image-1", 1),
          ("image-2", 2))
    )


_SysSwBootUpImage_Type.__name__ = "Integer32"
_SysSwBootUpImage_Object = MibScalar
sysSwBootUpImage = _SysSwBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 14),
    _SysSwBootUpImage_Type()
)
sysSwBootUpImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwBootUpImage.setStatus("current")
_SysImage1FwVersion_Type = DisplayString
_SysImage1FwVersion_Object = MibScalar
sysImage1FwVersion = _SysImage1FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 15),
    _SysImage1FwVersion_Type()
)
sysImage1FwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImage1FwVersion.setStatus("current")
_SysImage2FwVersion_Type = DisplayString
_SysImage2FwVersion_Object = MibScalar
sysImage2FwVersion = _SysImage2FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 1, 16),
    _SysImage2FwVersion_Type()
)
sysImage2FwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImage2FwVersion.setStatus("current")
_BrLimitSetup_ObjectIdentity = ObjectIdentity
brLimitSetup = _BrLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3)
)
_BrLimitState_Type = EnabledStatus
_BrLimitState_Object = MibScalar
brLimitState = _BrLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 1),
    _BrLimitState_Type()
)
brLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitState.setStatus("current")
_BrLimitPortTable_Object = MibTable
brLimitPortTable = _BrLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2)
)
if mibBuilder.loadTexts:
    brLimitPortTable.setStatus("current")
_BrLimitPortEntry_Object = MibTableRow
brLimitPortEntry = _BrLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1)
)
brLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    brLimitPortEntry.setStatus("current")
_BrLimitPortBrState_Type = EnabledStatus
_BrLimitPortBrState_Object = MibTableColumn
brLimitPortBrState = _BrLimitPortBrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1, 1),
    _BrLimitPortBrState_Type()
)
brLimitPortBrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrState.setStatus("current")
_BrLimitPortBrRate_Type = Integer32
_BrLimitPortBrRate_Object = MibTableColumn
brLimitPortBrRate = _BrLimitPortBrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1, 2),
    _BrLimitPortBrRate_Type()
)
brLimitPortBrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrRate.setStatus("current")
_BrLimitPortMcState_Type = EnabledStatus
_BrLimitPortMcState_Object = MibTableColumn
brLimitPortMcState = _BrLimitPortMcState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1, 3),
    _BrLimitPortMcState_Type()
)
brLimitPortMcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcState.setStatus("current")
_BrLimitPortMcRate_Type = Integer32
_BrLimitPortMcRate_Object = MibTableColumn
brLimitPortMcRate = _BrLimitPortMcRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1, 4),
    _BrLimitPortMcRate_Type()
)
brLimitPortMcRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcRate.setStatus("current")
_BrLimitPortDlfState_Type = EnabledStatus
_BrLimitPortDlfState_Object = MibTableColumn
brLimitPortDlfState = _BrLimitPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1, 5),
    _BrLimitPortDlfState_Type()
)
brLimitPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfState.setStatus("current")
_BrLimitPortDlfRate_Type = Integer32
_BrLimitPortDlfRate_Object = MibTableColumn
brLimitPortDlfRate = _BrLimitPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 3, 2, 1, 6),
    _BrLimitPortDlfRate_Type()
)
brLimitPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfRate.setStatus("current")
_PortSecuritySetup_ObjectIdentity = ObjectIdentity
portSecuritySetup = _PortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4)
)
_PortSecurityState_Type = Integer32
_PortSecurityState_Object = MibScalar
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 1),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("current")
_PortSecurityPortTable_Object = MibTable
portSecurityPortTable = _PortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 2)
)
if mibBuilder.loadTexts:
    portSecurityPortTable.setStatus("current")
_PortSecurityPortEntry_Object = MibTableRow
portSecurityPortEntry = _PortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 2, 1)
)
portSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portSecurityPortEntry.setStatus("current")
_PortSecurityPortState_Type = EnabledStatus
_PortSecurityPortState_Object = MibTableColumn
portSecurityPortState = _PortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 2, 1, 1),
    _PortSecurityPortState_Type()
)
portSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortState.setStatus("current")
_PortSecurityPortLearnState_Type = EnabledStatus
_PortSecurityPortLearnState_Object = MibTableColumn
portSecurityPortLearnState = _PortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 2, 1, 2),
    _PortSecurityPortLearnState_Type()
)
portSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setStatus("current")
_PortSecurityPortCount_Type = Integer32
_PortSecurityPortCount_Object = MibTableColumn
portSecurityPortCount = _PortSecurityPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 2, 1, 3),
    _PortSecurityPortCount_Type()
)
portSecurityPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortCount.setStatus("current")
_PortSecurityMacFreeze_Type = PortList
_PortSecurityMacFreeze_Object = MibScalar
portSecurityMacFreeze = _PortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 4, 3),
    _PortSecurityMacFreeze_Type()
)
portSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacFreeze.setStatus("current")
_VlanTrunkSetup_ObjectIdentity = ObjectIdentity
vlanTrunkSetup = _VlanTrunkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 5)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("current")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 5, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("current")
_VlanTrunkPortState_Type = EnabledStatus
_VlanTrunkPortState_Object = MibTableColumn
vlanTrunkPortState = _VlanTrunkPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 5, 1, 1, 1),
    _VlanTrunkPortState_Type()
)
vlanTrunkPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setStatus("current")
_CtlProtTransSetup_ObjectIdentity = ObjectIdentity
ctlProtTransSetup = _CtlProtTransSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 6)
)
_CtlProtTransState_Type = EnabledStatus
_CtlProtTransState_Object = MibScalar
ctlProtTransState = _CtlProtTransState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 6, 1),
    _CtlProtTransState_Type()
)
ctlProtTransState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransState.setStatus("current")
_CtlProtTransTunnelPortTable_Object = MibTable
ctlProtTransTunnelPortTable = _CtlProtTransTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 6, 2)
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortTable.setStatus("current")
_CtlProtTransTunnelPortEntry_Object = MibTableRow
ctlProtTransTunnelPortEntry = _CtlProtTransTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 6, 2, 1)
)
ctlProtTransTunnelPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortEntry.setStatus("current")


class _CtlProtTransTunnelMode_Type(Integer32):
    """Custom type ctlProtTransTunnelMode based on Integer32"""
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
        *(("peer", 0),
          ("tunnel", 1),
          ("discard", 2),
          ("network", 3))
    )


_CtlProtTransTunnelMode_Type.__name__ = "Integer32"
_CtlProtTransTunnelMode_Object = MibTableColumn
ctlProtTransTunnelMode = _CtlProtTransTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 6, 2, 1, 1),
    _CtlProtTransTunnelMode_Type()
)
ctlProtTransTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransTunnelMode.setStatus("current")
_VlanStackSetup_ObjectIdentity = ObjectIdentity
vlanStackSetup = _VlanStackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7)
)
_VlanStackState_Type = EnabledStatus
_VlanStackState_Object = MibScalar
vlanStackState = _VlanStackState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 1),
    _VlanStackState_Type()
)
vlanStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackState.setStatus("current")
_VlanStackTpid_Type = Integer32
_VlanStackTpid_Object = MibScalar
vlanStackTpid = _VlanStackTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 2),
    _VlanStackTpid_Type()
)
vlanStackTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackTpid.setStatus("current")
_VlanStackPortTable_Object = MibTable
vlanStackPortTable = _VlanStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3)
)
if mibBuilder.loadTexts:
    vlanStackPortTable.setStatus("current")
_VlanStackPortEntry_Object = MibTableRow
vlanStackPortEntry = _VlanStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3, 1)
)
vlanStackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanStackPortEntry.setStatus("current")


class _VlanStackPortMode_Type(Integer32):
    """Custom type vlanStackPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("access", 2),
          ("tunnel", 3))
    )


_VlanStackPortMode_Type.__name__ = "Integer32"
_VlanStackPortMode_Object = MibTableColumn
vlanStackPortMode = _VlanStackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3, 1, 1),
    _VlanStackPortMode_Type()
)
vlanStackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortMode.setStatus("current")
_VlanStackPortVid_Type = Integer32
_VlanStackPortVid_Object = MibTableColumn
vlanStackPortVid = _VlanStackPortVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3, 1, 2),
    _VlanStackPortVid_Type()
)
vlanStackPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortVid.setStatus("current")


class _VlanStackPortPrio_Type(Integer32):
    """Custom type vlanStackPortPrio based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_VlanStackPortPrio_Type.__name__ = "Integer32"
_VlanStackPortPrio_Object = MibTableColumn
vlanStackPortPrio = _VlanStackPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3, 1, 3),
    _VlanStackPortPrio_Type()
)
vlanStackPortPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortPrio.setStatus("current")
_VlanStackTunnelPortTpid_Type = Integer32
_VlanStackTunnelPortTpid_Object = MibTableColumn
vlanStackTunnelPortTpid = _VlanStackTunnelPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3, 1, 4),
    _VlanStackTunnelPortTpid_Type()
)
vlanStackTunnelPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackTunnelPortTpid.setStatus("current")
_VlanStackPCopyCtagPrio_Type = EnabledStatus
_VlanStackPCopyCtagPrio_Object = MibTableColumn
vlanStackPCopyCtagPrio = _VlanStackPCopyCtagPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 3, 1, 5),
    _VlanStackPCopyCtagPrio_Type()
)
vlanStackPCopyCtagPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStackPCopyCtagPrio.setStatus("current")
_SelectiveQinQTable_Object = MibTable
selectiveQinQTable = _SelectiveQinQTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4)
)
if mibBuilder.loadTexts:
    selectiveQinQTable.setStatus("current")
_SelectiveQinQEntry_Object = MibTableRow
selectiveQinQEntry = _SelectiveQinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1)
)
selectiveQinQEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "selectiveQinQPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "selectiveQinQCvid"),
)
if mibBuilder.loadTexts:
    selectiveQinQEntry.setStatus("current")
_SelectiveQinQName_Type = DisplayString
_SelectiveQinQName_Object = MibTableColumn
selectiveQinQName = _SelectiveQinQName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 1),
    _SelectiveQinQName_Type()
)
selectiveQinQName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQName.setStatus("current")
_SelectiveQinQPort_Type = Integer32
_SelectiveQinQPort_Object = MibTableColumn
selectiveQinQPort = _SelectiveQinQPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 2),
    _SelectiveQinQPort_Type()
)
selectiveQinQPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectiveQinQPort.setStatus("current")
_SelectiveQinQCvid_Type = Integer32
_SelectiveQinQCvid_Object = MibTableColumn
selectiveQinQCvid = _SelectiveQinQCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 3),
    _SelectiveQinQCvid_Type()
)
selectiveQinQCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectiveQinQCvid.setStatus("current")
_SelectiveQinQSpvid_Type = Integer32
_SelectiveQinQSpvid_Object = MibTableColumn
selectiveQinQSpvid = _SelectiveQinQSpvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 4),
    _SelectiveQinQSpvid_Type()
)
selectiveQinQSpvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQSpvid.setStatus("current")


class _SelectiveQinQPriority_Type(Integer32):
    """Custom type selectiveQinQPriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_SelectiveQinQPriority_Type.__name__ = "Integer32"
_SelectiveQinQPriority_Object = MibTableColumn
selectiveQinQPriority = _SelectiveQinQPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 5),
    _SelectiveQinQPriority_Type()
)
selectiveQinQPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQPriority.setStatus("current")
_SelectiveQinQRowStatus_Type = RowStatus
_SelectiveQinQRowStatus_Object = MibTableColumn
selectiveQinQRowStatus = _SelectiveQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 6),
    _SelectiveQinQRowStatus_Type()
)
selectiveQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    selectiveQinQRowStatus.setStatus("current")
_SelectiveQinQACtivePrio_Type = EnabledStatus
_SelectiveQinQACtivePrio_Object = MibTableColumn
selectiveQinQACtivePrio = _SelectiveQinQACtivePrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 4, 1, 7),
    _SelectiveQinQACtivePrio_Type()
)
selectiveQinQACtivePrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQACtivePrio.setStatus("current")
_PortBasedInnerQTable_Object = MibTable
portBasedInnerQTable = _PortBasedInnerQTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 5)
)
if mibBuilder.loadTexts:
    portBasedInnerQTable.setStatus("current")
_PortBasedInnerQEntry_Object = MibTableRow
portBasedInnerQEntry = _PortBasedInnerQEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 5, 1)
)
portBasedInnerQEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBasedInnerQEntry.setStatus("current")
_PortBasedInnerQVid_Type = Integer32
_PortBasedInnerQVid_Object = MibTableColumn
portBasedInnerQVid = _PortBasedInnerQVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 5, 1, 1),
    _PortBasedInnerQVid_Type()
)
portBasedInnerQVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedInnerQVid.setStatus("current")


class _PortBasedInnerQPrio_Type(Integer32):
    """Custom type portBasedInnerQPrio based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_PortBasedInnerQPrio_Type.__name__ = "Integer32"
_PortBasedInnerQPrio_Object = MibTableColumn
portBasedInnerQPrio = _PortBasedInnerQPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 5, 1, 2),
    _PortBasedInnerQPrio_Type()
)
portBasedInnerQPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedInnerQPrio.setStatus("current")
_PortBasedInnerQActive_Type = EnabledStatus
_PortBasedInnerQActive_Object = MibTableColumn
portBasedInnerQActive = _PortBasedInnerQActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 5, 1, 3),
    _PortBasedInnerQActive_Type()
)
portBasedInnerQActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedInnerQActive.setStatus("current")
_PortBasedInnerQTxUntag_Type = EnabledStatus
_PortBasedInnerQTxUntag_Object = MibTableColumn
portBasedInnerQTxUntag = _PortBasedInnerQTxUntag_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 7, 5, 1, 4),
    _PortBasedInnerQTxUntag_Type()
)
portBasedInnerQTxUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedInnerQTxUntag.setStatus("current")
_Dot1xSetup_ObjectIdentity = ObjectIdentity
dot1xSetup = _Dot1xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8)
)
_PortAuthState_Type = EnabledStatus
_PortAuthState_Object = MibScalar
portAuthState = _PortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8, 3),
    _PortAuthState_Type()
)
portAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthState.setStatus("current")
_PortAuthTable_Object = MibTable
portAuthTable = _PortAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8, 4)
)
if mibBuilder.loadTexts:
    portAuthTable.setStatus("current")
_PortAuthEntry_Object = MibTableRow
portAuthEntry = _PortAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8, 4, 1)
)
portAuthEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portAuthEntry.setStatus("current")
_PortAuthEntryState_Type = EnabledStatus
_PortAuthEntryState_Object = MibTableColumn
portAuthEntryState = _PortAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8, 4, 1, 1),
    _PortAuthEntryState_Type()
)
portAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthEntryState.setStatus("current")
_PortReAuthEntryState_Type = EnabledStatus
_PortReAuthEntryState_Object = MibTableColumn
portReAuthEntryState = _PortReAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8, 4, 1, 2),
    _PortReAuthEntryState_Type()
)
portReAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryState.setStatus("current")
_PortReAuthEntryTimer_Type = Integer32
_PortReAuthEntryTimer_Object = MibTableColumn
portReAuthEntryTimer = _PortReAuthEntryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 8, 4, 1, 3),
    _PortReAuthEntryTimer_Type()
)
portReAuthEntryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryTimer.setStatus("current")
_HwMonitorInfo_ObjectIdentity = ObjectIdentity
hwMonitorInfo = _HwMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9)
)
_FanRpmTable_Object = MibTable
fanRpmTable = _FanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1)
)
if mibBuilder.loadTexts:
    fanRpmTable.setStatus("current")
_FanRpmEntry_Object = MibTableRow
fanRpmEntry = _FanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1)
)
fanRpmEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "fanRpmIndex"),
)
if mibBuilder.loadTexts:
    fanRpmEntry.setStatus("current")
_FanRpmIndex_Type = Integer32
_FanRpmIndex_Object = MibTableColumn
fanRpmIndex = _FanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1, 1),
    _FanRpmIndex_Type()
)
fanRpmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmIndex.setStatus("current")
_FanRpmCurValue_Type = Integer32
_FanRpmCurValue_Object = MibTableColumn
fanRpmCurValue = _FanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1, 2),
    _FanRpmCurValue_Type()
)
fanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmCurValue.setStatus("current")
_FanRpmMaxValue_Type = Integer32
_FanRpmMaxValue_Object = MibTableColumn
fanRpmMaxValue = _FanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1, 3),
    _FanRpmMaxValue_Type()
)
fanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMaxValue.setStatus("current")
_FanRpmMinValue_Type = Integer32
_FanRpmMinValue_Object = MibTableColumn
fanRpmMinValue = _FanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1, 4),
    _FanRpmMinValue_Type()
)
fanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMinValue.setStatus("current")
_FanRpmLowThresh_Type = Integer32
_FanRpmLowThresh_Object = MibTableColumn
fanRpmLowThresh = _FanRpmLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1, 5),
    _FanRpmLowThresh_Type()
)
fanRpmLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmLowThresh.setStatus("current")
_FanRpmDescr_Type = DisplayString
_FanRpmDescr_Object = MibTableColumn
fanRpmDescr = _FanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 1, 1, 6),
    _FanRpmDescr_Type()
)
fanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmDescr.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1)
)
tempEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 1),
          ("dsp", 2),
          ("hwMonitor", 3))
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
_TempCurValue_Type = Integer32
_TempCurValue_Object = MibTableColumn
tempCurValue = _TempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1, 2),
    _TempCurValue_Type()
)
tempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurValue.setStatus("current")
_TempMaxValue_Type = Integer32
_TempMaxValue_Object = MibTableColumn
tempMaxValue = _TempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1, 3),
    _TempMaxValue_Type()
)
tempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxValue.setStatus("current")
_TempMinValue_Type = Integer32
_TempMinValue_Object = MibTableColumn
tempMinValue = _TempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1, 4),
    _TempMinValue_Type()
)
tempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinValue.setStatus("current")
_TempHighThresh_Type = Integer32
_TempHighThresh_Object = MibTableColumn
tempHighThresh = _TempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1, 5),
    _TempHighThresh_Type()
)
tempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighThresh.setStatus("current")
_TempDescr_Type = DisplayString
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 2, 1, 6),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1)
)
voltageEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 2),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 3),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 4),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 5),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
_VoltageLowThresh_Type = Integer32
_VoltageLowThresh_Object = MibTableColumn
voltageLowThresh = _VoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 6),
    _VoltageLowThresh_Type()
)
voltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowThresh.setStatus("current")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 9, 3, 1, 7),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10)
)
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 1),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("current")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 2),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 3),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("current")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("current")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4, 1, 1),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("current")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4, 1, 2),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("current")
_SnmpTrapDestPort_Type = Integer32
_SnmpTrapDestPort_Object = MibTableColumn
snmpTrapDestPort = _SnmpTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4, 1, 3),
    _SnmpTrapDestPort_Type()
)
snmpTrapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestPort.setStatus("current")


class _SnmpTrapVersion_Type(Integer32):
    """Custom type snmpTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_SnmpTrapVersion_Type.__name__ = "Integer32"
_SnmpTrapVersion_Object = MibTableColumn
snmpTrapVersion = _SnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4, 1, 4),
    _SnmpTrapVersion_Type()
)
snmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVersion.setStatus("current")
_SnmpTrapUserName_Type = DisplayString
_SnmpTrapUserName_Object = MibTableColumn
snmpTrapUserName = _SnmpTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 4, 1, 5),
    _SnmpTrapUserName_Type()
)
snmpTrapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapUserName.setStatus("current")
_SnmpTrapGroupTable_Object = MibTable
snmpTrapGroupTable = _SnmpTrapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5)
)
if mibBuilder.loadTexts:
    snmpTrapGroupTable.setStatus("current")
_SnmpTrapGroupEntry_Object = MibTableRow
snmpTrapGroupEntry = _SnmpTrapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5, 1)
)
snmpTrapGroupEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapGroupEntry.setStatus("current")


class _SnmpTrapSystemGroup_Type(Bits):
    """Custom type snmpTrapSystemGroup based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 0),
          ("warmStart", 1),
          ("temperature", 3),
          ("voltage", 4),
          ("reset", 5),
          ("hwinformation", 7),
          ("loopguard", 9))
    )

_SnmpTrapSystemGroup_Type.__name__ = "Bits"
_SnmpTrapSystemGroup_Object = MibTableColumn
snmpTrapSystemGroup = _SnmpTrapSystemGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5, 1, 1),
    _SnmpTrapSystemGroup_Type()
)
snmpTrapSystemGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSystemGroup.setStatus("current")


class _SnmpTrapInterfaceGroup_Type(Bits):
    """Custom type snmpTrapInterfaceGroup based on Bits"""
    namedValues = NamedValues(
        *(("linkup", 0),
          ("linkdown", 1),
          ("autonegotiation", 2))
    )

_SnmpTrapInterfaceGroup_Type.__name__ = "Bits"
_SnmpTrapInterfaceGroup_Object = MibTableColumn
snmpTrapInterfaceGroup = _SnmpTrapInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5, 1, 2),
    _SnmpTrapInterfaceGroup_Type()
)
snmpTrapInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapInterfaceGroup.setStatus("current")


class _SnmpTrapAAAGroup_Type(Bits):
    """Custom type snmpTrapAAAGroup based on Bits"""
    namedValues = NamedValues(
        *(("authentication", 0),
          ("accounting", 1))
    )

_SnmpTrapAAAGroup_Type.__name__ = "Bits"
_SnmpTrapAAAGroup_Object = MibTableColumn
snmpTrapAAAGroup = _SnmpTrapAAAGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5, 1, 3),
    _SnmpTrapAAAGroup_Type()
)
snmpTrapAAAGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapAAAGroup.setStatus("current")


class _SnmpTrapSwitchGroup_Type(Bits):
    """Custom type snmpTrapSwitchGroup based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("mactable", 1),
          ("rmon", 2))
    )

_SnmpTrapSwitchGroup_Type.__name__ = "Bits"
_SnmpTrapSwitchGroup_Object = MibTableColumn
snmpTrapSwitchGroup = _SnmpTrapSwitchGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5, 1, 5),
    _SnmpTrapSwitchGroup_Type()
)
snmpTrapSwitchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSwitchGroup.setStatus("current")


class _SnmpTrapVdslGroup_Type(Bits):
    """Custom type snmpTrapVdslGroup based on Bits"""
    namedValues = NamedValues(
        *(("alarmprofile", 0),
          ("others", 1))
    )

_SnmpTrapVdslGroup_Type.__name__ = "Bits"
_SnmpTrapVdslGroup_Object = MibTableColumn
snmpTrapVdslGroup = _SnmpTrapVdslGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 5, 1, 6),
    _SnmpTrapVdslGroup_Type()
)
snmpTrapVdslGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVdslGroup.setStatus("current")


class _SnmpVersion_Type(Integer32):
    """Custom type snmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 0),
          ("v3", 1),
          ("v3v2c", 2))
    )


_SnmpVersion_Type.__name__ = "Integer32"
_SnmpVersion_Object = MibScalar
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 6),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 7)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 7, 1)
)
snmpUserEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "snmpUserName"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")
_SnmpUserName_Type = DisplayString
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 7, 1, 1),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserName.setStatus("current")


class _SnmpUserSecurityLevel_Type(Integer32):
    """Custom type snmpUserSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_SnmpUserSecurityLevel_Type.__name__ = "Integer32"
_SnmpUserSecurityLevel_Object = MibTableColumn
snmpUserSecurityLevel = _SnmpUserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 7, 1, 2),
    _SnmpUserSecurityLevel_Type()
)
snmpUserSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserSecurityLevel.setStatus("current")


class _SnmpUserAuthProtocol_Type(Integer32):
    """Custom type snmpUserAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )


_SnmpUserAuthProtocol_Type.__name__ = "Integer32"
_SnmpUserAuthProtocol_Object = MibTableColumn
snmpUserAuthProtocol = _SnmpUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 7, 1, 3),
    _SnmpUserAuthProtocol_Type()
)
snmpUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthProtocol.setStatus("current")


class _SnmpUserPrivProtocol_Type(Integer32):
    """Custom type snmpUserPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("aes", 1))
    )


_SnmpUserPrivProtocol_Type.__name__ = "Integer32"
_SnmpUserPrivProtocol_Object = MibTableColumn
snmpUserPrivProtocol = _SnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 7, 1, 4),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")
_SnmpTrapDestInfoTable_Object = MibTable
snmpTrapDestInfoTable = _SnmpTrapDestInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8)
)
if mibBuilder.loadTexts:
    snmpTrapDestInfoTable.setStatus("current")
_SnmpTrapDestInfoEntry_Object = MibTableRow
snmpTrapDestInfoEntry = _SnmpTrapDestInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1)
)
snmpTrapDestInfoEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "snmpTrapDestInfoIpAddrType"),
    (0, "ZYXEL-ves1608FE57-MIB", "snmpTrapDestInfoIpAddr"),
)
if mibBuilder.loadTexts:
    snmpTrapDestInfoEntry.setStatus("current")


class _SnmpTrapDestInfoIpAddrType_Type(InetAddressType):
    """Custom type snmpTrapDestInfoIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SnmpTrapDestInfoIpAddrType_Type.__name__ = "InetAddressType"
_SnmpTrapDestInfoIpAddrType_Object = MibTableColumn
snmpTrapDestInfoIpAddrType = _SnmpTrapDestInfoIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1, 1),
    _SnmpTrapDestInfoIpAddrType_Type()
)
snmpTrapDestInfoIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestInfoIpAddrType.setStatus("current")
_SnmpTrapDestInfoIpAddr_Type = InetAddress
_SnmpTrapDestInfoIpAddr_Object = MibTableColumn
snmpTrapDestInfoIpAddr = _SnmpTrapDestInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1, 2),
    _SnmpTrapDestInfoIpAddr_Type()
)
snmpTrapDestInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestInfoIpAddr.setStatus("current")
_SnmpTrapDestInfoRowStatus_Type = RowStatus
_SnmpTrapDestInfoRowStatus_Object = MibTableColumn
snmpTrapDestInfoRowStatus = _SnmpTrapDestInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1, 3),
    _SnmpTrapDestInfoRowStatus_Type()
)
snmpTrapDestInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestInfoRowStatus.setStatus("current")
_SnmpTrapDestInfoPort_Type = Integer32
_SnmpTrapDestInfoPort_Object = MibTableColumn
snmpTrapDestInfoPort = _SnmpTrapDestInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1, 4),
    _SnmpTrapDestInfoPort_Type()
)
snmpTrapDestInfoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestInfoPort.setStatus("current")


class _SnmpTrapDestInfoVersion_Type(Integer32):
    """Custom type snmpTrapDestInfoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_SnmpTrapDestInfoVersion_Type.__name__ = "Integer32"
_SnmpTrapDestInfoVersion_Object = MibTableColumn
snmpTrapDestInfoVersion = _SnmpTrapDestInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1, 5),
    _SnmpTrapDestInfoVersion_Type()
)
snmpTrapDestInfoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestInfoVersion.setStatus("current")
_SnmpTrapDestInfoUserName_Type = DisplayString
_SnmpTrapDestInfoUserName_Object = MibTableColumn
snmpTrapDestInfoUserName = _SnmpTrapDestInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 8, 1, 6),
    _SnmpTrapDestInfoUserName_Type()
)
snmpTrapDestInfoUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestInfoUserName.setStatus("current")
_SnmpTrapGroupInfoTable_Object = MibTable
snmpTrapGroupInfoTable = _SnmpTrapGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9)
)
if mibBuilder.loadTexts:
    snmpTrapGroupInfoTable.setStatus("current")
_SnmpTrapGroupInfoEntry_Object = MibTableRow
snmpTrapGroupInfoEntry = _SnmpTrapGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9, 1)
)
snmpTrapGroupInfoEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "snmpTrapDestInfoIpAddrType"),
    (0, "ZYXEL-ves1608FE57-MIB", "snmpTrapDestInfoIpAddr"),
)
if mibBuilder.loadTexts:
    snmpTrapGroupInfoEntry.setStatus("current")


class _SnmpTrapGroupInfoSystemGroup_Type(Bits):
    """Custom type snmpTrapGroupInfoSystemGroup based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 0),
          ("warmStart", 1),
          ("temperature", 3),
          ("voltage", 4),
          ("reset", 5),
          ("hwinformation", 7),
          ("loopguard", 9))
    )

_SnmpTrapGroupInfoSystemGroup_Type.__name__ = "Bits"
_SnmpTrapGroupInfoSystemGroup_Object = MibTableColumn
snmpTrapGroupInfoSystemGroup = _SnmpTrapGroupInfoSystemGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9, 1, 1),
    _SnmpTrapGroupInfoSystemGroup_Type()
)
snmpTrapGroupInfoSystemGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGroupInfoSystemGroup.setStatus("current")


class _SnmpTrapGroupInfoInterfaceGroup_Type(Bits):
    """Custom type snmpTrapGroupInfoInterfaceGroup based on Bits"""
    namedValues = NamedValues(
        *(("linkup", 0),
          ("linkdown", 1),
          ("autonegotiation", 2))
    )

_SnmpTrapGroupInfoInterfaceGroup_Type.__name__ = "Bits"
_SnmpTrapGroupInfoInterfaceGroup_Object = MibTableColumn
snmpTrapGroupInfoInterfaceGroup = _SnmpTrapGroupInfoInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9, 1, 2),
    _SnmpTrapGroupInfoInterfaceGroup_Type()
)
snmpTrapGroupInfoInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGroupInfoInterfaceGroup.setStatus("current")


class _SnmpTrapGroupInfoAAAGroup_Type(Bits):
    """Custom type snmpTrapGroupInfoAAAGroup based on Bits"""
    namedValues = NamedValues(
        *(("authentication", 0),
          ("accounting", 1))
    )

_SnmpTrapGroupInfoAAAGroup_Type.__name__ = "Bits"
_SnmpTrapGroupInfoAAAGroup_Object = MibTableColumn
snmpTrapGroupInfoAAAGroup = _SnmpTrapGroupInfoAAAGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9, 1, 3),
    _SnmpTrapGroupInfoAAAGroup_Type()
)
snmpTrapGroupInfoAAAGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGroupInfoAAAGroup.setStatus("current")


class _SnmpTrapGroupInfoSwitchGroup_Type(Bits):
    """Custom type snmpTrapGroupInfoSwitchGroup based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("mactable", 1),
          ("rmon", 2))
    )

_SnmpTrapGroupInfoSwitchGroup_Type.__name__ = "Bits"
_SnmpTrapGroupInfoSwitchGroup_Object = MibTableColumn
snmpTrapGroupInfoSwitchGroup = _SnmpTrapGroupInfoSwitchGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9, 1, 5),
    _SnmpTrapGroupInfoSwitchGroup_Type()
)
snmpTrapGroupInfoSwitchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGroupInfoSwitchGroup.setStatus("current")


class _SnmpTrapGroupInfoVdslGroup_Type(Bits):
    """Custom type snmpTrapGroupInfoVdslGroup based on Bits"""
    namedValues = NamedValues(
        *(("alarmprofile", 0),
          ("others", 1))
    )

_SnmpTrapGroupInfoVdslGroup_Type.__name__ = "Bits"
_SnmpTrapGroupInfoVdslGroup_Object = MibTableColumn
snmpTrapGroupInfoVdslGroup = _SnmpTrapGroupInfoVdslGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 10, 9, 1, 6),
    _SnmpTrapGroupInfoVdslGroup_Type()
)
snmpTrapGroupInfoVdslGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapGroupInfoVdslGroup.setStatus("current")
_DateTimeServerSetup_ObjectIdentity = ObjectIdentity
dateTimeServerSetup = _DateTimeServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11)
)


class _DateTimeServerType_Type(Integer32):
    """Custom type dateTimeServerType based on Integer32"""
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
        *(("none", 1),
          ("daytime", 2),
          ("time", 3),
          ("ntp", 4))
    )


_DateTimeServerType_Type.__name__ = "Integer32"
_DateTimeServerType_Object = MibScalar
dateTimeServerType = _DateTimeServerType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 1),
    _DateTimeServerType_Type()
)
dateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerType.setStatus("current")
_DateTimeServerIP_Type = IpAddress
_DateTimeServerIP_Object = MibScalar
dateTimeServerIP = _DateTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 2),
    _DateTimeServerIP_Type()
)
dateTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIP.setStatus("current")
_DateTimeZone_Type = Integer32
_DateTimeZone_Object = MibScalar
dateTimeZone = _DateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 3),
    _DateTimeZone_Type()
)
dateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeZone.setStatus("current")
_DateTimeNewDateYear_Type = Integer32
_DateTimeNewDateYear_Object = MibScalar
dateTimeNewDateYear = _DateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 4),
    _DateTimeNewDateYear_Type()
)
dateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setStatus("current")
_DateTimeNewDateMonth_Type = Integer32
_DateTimeNewDateMonth_Object = MibScalar
dateTimeNewDateMonth = _DateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 5),
    _DateTimeNewDateMonth_Type()
)
dateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setStatus("current")
_DateTimeNewDateDay_Type = Integer32
_DateTimeNewDateDay_Object = MibScalar
dateTimeNewDateDay = _DateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 6),
    _DateTimeNewDateDay_Type()
)
dateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setStatus("current")
_DateTimeNewTimeHour_Type = Integer32
_DateTimeNewTimeHour_Object = MibScalar
dateTimeNewTimeHour = _DateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 7),
    _DateTimeNewTimeHour_Type()
)
dateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setStatus("current")
_DateTimeNewTimeMinute_Type = Integer32
_DateTimeNewTimeMinute_Object = MibScalar
dateTimeNewTimeMinute = _DateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 8),
    _DateTimeNewTimeMinute_Type()
)
dateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setStatus("current")
_DateTimeNewTimeSecond_Type = Integer32
_DateTimeNewTimeSecond_Object = MibScalar
dateTimeNewTimeSecond = _DateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 9),
    _DateTimeNewTimeSecond_Type()
)
dateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setStatus("current")
_DateTimeDaylightSavingTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeDaylightSavingTimeSetup = _DateTimeDaylightSavingTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10)
)
_DaylightSavingTimeState_Type = EnabledStatus
_DaylightSavingTimeState_Object = MibScalar
daylightSavingTimeState = _DaylightSavingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 1),
    _DaylightSavingTimeState_Type()
)
daylightSavingTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeState.setStatus("current")


class _DaylightSavingTimeStartDateWeek_Type(Integer32):
    """Custom type daylightSavingTimeStartDateWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_DaylightSavingTimeStartDateWeek_Type.__name__ = "Integer32"
_DaylightSavingTimeStartDateWeek_Object = MibScalar
daylightSavingTimeStartDateWeek = _DaylightSavingTimeStartDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 2),
    _DaylightSavingTimeStartDateWeek_Type()
)
daylightSavingTimeStartDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateWeek.setStatus("current")


class _DaylightSavingTimeStartDateDay_Type(Integer32):
    """Custom type daylightSavingTimeStartDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_DaylightSavingTimeStartDateDay_Type.__name__ = "Integer32"
_DaylightSavingTimeStartDateDay_Object = MibScalar
daylightSavingTimeStartDateDay = _DaylightSavingTimeStartDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 3),
    _DaylightSavingTimeStartDateDay_Type()
)
daylightSavingTimeStartDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateDay.setStatus("current")


class _DaylightSavingTimeStartDateMonth_Type(Integer32):
    """Custom type daylightSavingTimeStartDateMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("january", 1),
          ("february", 2),
          ("march", 3),
          ("april", 4),
          ("may", 5),
          ("june", 6),
          ("july", 7),
          ("august", 8),
          ("september", 9),
          ("october", 10),
          ("november", 11),
          ("december", 12))
    )


_DaylightSavingTimeStartDateMonth_Type.__name__ = "Integer32"
_DaylightSavingTimeStartDateMonth_Object = MibScalar
daylightSavingTimeStartDateMonth = _DaylightSavingTimeStartDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 4),
    _DaylightSavingTimeStartDateMonth_Type()
)
daylightSavingTimeStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateMonth.setStatus("current")
_DaylightSavingTimeStartDateHour_Type = Integer32
_DaylightSavingTimeStartDateHour_Object = MibScalar
daylightSavingTimeStartDateHour = _DaylightSavingTimeStartDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 5),
    _DaylightSavingTimeStartDateHour_Type()
)
daylightSavingTimeStartDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateHour.setStatus("current")


class _DaylightSavingTimeEndDateWeek_Type(Integer32):
    """Custom type daylightSavingTimeEndDateWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_DaylightSavingTimeEndDateWeek_Type.__name__ = "Integer32"
_DaylightSavingTimeEndDateWeek_Object = MibScalar
daylightSavingTimeEndDateWeek = _DaylightSavingTimeEndDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 6),
    _DaylightSavingTimeEndDateWeek_Type()
)
daylightSavingTimeEndDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateWeek.setStatus("current")


class _DaylightSavingTimeEndDateDay_Type(Integer32):
    """Custom type daylightSavingTimeEndDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_DaylightSavingTimeEndDateDay_Type.__name__ = "Integer32"
_DaylightSavingTimeEndDateDay_Object = MibScalar
daylightSavingTimeEndDateDay = _DaylightSavingTimeEndDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 7),
    _DaylightSavingTimeEndDateDay_Type()
)
daylightSavingTimeEndDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateDay.setStatus("current")


class _DaylightSavingTimeEndDateMonth_Type(Integer32):
    """Custom type daylightSavingTimeEndDateMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("january", 1),
          ("february", 2),
          ("march", 3),
          ("april", 4),
          ("may", 5),
          ("june", 6),
          ("july", 7),
          ("august", 8),
          ("september", 9),
          ("october", 10),
          ("november", 11),
          ("december", 12))
    )


_DaylightSavingTimeEndDateMonth_Type.__name__ = "Integer32"
_DaylightSavingTimeEndDateMonth_Object = MibScalar
daylightSavingTimeEndDateMonth = _DaylightSavingTimeEndDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 8),
    _DaylightSavingTimeEndDateMonth_Type()
)
daylightSavingTimeEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateMonth.setStatus("current")
_DaylightSavingTimeEndDateHour_Type = Integer32
_DaylightSavingTimeEndDateHour_Object = MibScalar
daylightSavingTimeEndDateHour = _DaylightSavingTimeEndDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 10, 9),
    _DaylightSavingTimeEndDateHour_Type()
)
daylightSavingTimeEndDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateHour.setStatus("current")


class _DateTimeServerIPAddrType_Type(InetAddressType):
    """Custom type dateTimeServerIPAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_DateTimeServerIPAddrType_Type.__name__ = "InetAddressType"
_DateTimeServerIPAddrType_Object = MibScalar
dateTimeServerIPAddrType = _DateTimeServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 11),
    _DateTimeServerIPAddrType_Type()
)
dateTimeServerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIPAddrType.setStatus("current")
_DateTimeServerIPAddr_Type = InetAddress
_DateTimeServerIPAddr_Object = MibScalar
dateTimeServerIPAddr = _DateTimeServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 11, 12),
    _DateTimeServerIPAddr_Type()
)
dateTimeServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIPAddr.setStatus("current")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12)
)


class _SysMgmtConfigSave_Type(Integer32):
    """Custom type sysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtConfigSave_Type.__name__ = "Integer32"
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 1),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("current")


class _SysMgmtBootupConfig_Type(Integer32):
    """Custom type sysMgmtBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtBootupConfig_Type.__name__ = "Integer32"
_SysMgmtBootupConfig_Object = MibScalar
sysMgmtBootupConfig = _SysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 2),
    _SysMgmtBootupConfig_Type()
)
sysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupConfig.setStatus("current")


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 3),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("current")


class _SysMgmtDefaultConfig_Type(Integer32):
    """Custom type sysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reset-to-default", 1),
          ("reset-to-default-keep-ip", 2))
    )


_SysMgmtDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtDefaultConfig_Object = MibScalar
sysMgmtDefaultConfig = _SysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 4),
    _SysMgmtDefaultConfig_Type()
)
sysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfig.setStatus("current")


class _SysMgmtLastActionStatus_Type(Integer32):
    """Custom type sysMgmtLastActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("fail", 2))
    )


_SysMgmtLastActionStatus_Type.__name__ = "Integer32"
_SysMgmtLastActionStatus_Object = MibScalar
sysMgmtLastActionStatus = _SysMgmtLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 5),
    _SysMgmtLastActionStatus_Type()
)
sysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setStatus("current")


class _SysMgmtSystemStatus_Type(Bits):
    """Custom type sysMgmtSystemStatus based on Bits"""
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysTemperatureError", 1),
          ("sysFanRPMError", 2),
          ("sysVoltageRangeError", 3))
    )

_SysMgmtSystemStatus_Type.__name__ = "Bits"
_SysMgmtSystemStatus_Object = MibScalar
sysMgmtSystemStatus = _SysMgmtSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 6),
    _SysMgmtSystemStatus_Type()
)
sysMgmtSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtSystemStatus.setStatus("current")
_SysMgmtCPUUsage_Type = Integer32
_SysMgmtCPUUsage_Object = MibScalar
sysMgmtCPUUsage = _SysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 7),
    _SysMgmtCPUUsage_Type()
)
sysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setStatus("current")


class _SysMgmtBootupImage_Type(Integer32):
    """Custom type sysMgmtBootupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image-1", 1),
          ("image-2", 2))
    )


_SysMgmtBootupImage_Type.__name__ = "Integer32"
_SysMgmtBootupImage_Object = MibScalar
sysMgmtBootupImage = _SysMgmtBootupImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 8),
    _SysMgmtBootupImage_Type()
)
sysMgmtBootupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupImage.setStatus("current")


class _SysMgmtCounterReset_Type(Integer32):
    """Custom type sysMgmtCounterReset based on Integer32"""
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


_SysMgmtCounterReset_Type.__name__ = "Integer32"
_SysMgmtCounterReset_Object = MibScalar
sysMgmtCounterReset = _SysMgmtCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 9),
    _SysMgmtCounterReset_Type()
)
sysMgmtCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCounterReset.setStatus("current")
_SysMgmtTftpServiceSetup_ObjectIdentity = ObjectIdentity
sysMgmtTftpServiceSetup = _SysMgmtTftpServiceSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10)
)
_SysMgmtTftpServerIp_Type = IpAddress
_SysMgmtTftpServerIp_Object = MibScalar
sysMgmtTftpServerIp = _SysMgmtTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 1),
    _SysMgmtTftpServerIp_Type()
)
sysMgmtTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpServerIp.setStatus("current")
_SysMgmtTftpRemoteFileName_Type = DisplayString
_SysMgmtTftpRemoteFileName_Object = MibScalar
sysMgmtTftpRemoteFileName = _SysMgmtTftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 2),
    _SysMgmtTftpRemoteFileName_Type()
)
sysMgmtTftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpRemoteFileName.setStatus("current")


class _SysMgmtTftpConfigIndex_Type(Integer32):
    """Custom type sysMgmtTftpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_SysMgmtTftpConfigIndex_Type.__name__ = "Integer32"
_SysMgmtTftpConfigIndex_Object = MibScalar
sysMgmtTftpConfigIndex = _SysMgmtTftpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 3),
    _SysMgmtTftpConfigIndex_Type()
)
sysMgmtTftpConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpConfigIndex.setStatus("current")


class _SysMgmtTftpAction_Type(Integer32):
    """Custom type sysMgmtTftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("backup-config", 1),
          ("restore-config", 2))
    )


_SysMgmtTftpAction_Type.__name__ = "Integer32"
_SysMgmtTftpAction_Object = MibScalar
sysMgmtTftpAction = _SysMgmtTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 4),
    _SysMgmtTftpAction_Type()
)
sysMgmtTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpAction.setStatus("current")


class _SysMgmtTftpActionStatus_Type(Integer32):
    """Custom type sysMgmtTftpActionStatus based on Integer32"""
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
        *(("none", 0),
          ("success", 1),
          ("fail", 2),
          ("under-action", 3))
    )


_SysMgmtTftpActionStatus_Type.__name__ = "Integer32"
_SysMgmtTftpActionStatus_Object = MibScalar
sysMgmtTftpActionStatus = _SysMgmtTftpActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 5),
    _SysMgmtTftpActionStatus_Type()
)
sysMgmtTftpActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtTftpActionStatus.setStatus("current")
_SysMgmtTftpActionErrorInfo_Type = DisplayString
_SysMgmtTftpActionErrorInfo_Object = MibScalar
sysMgmtTftpActionErrorInfo = _SysMgmtTftpActionErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 6),
    _SysMgmtTftpActionErrorInfo_Type()
)
sysMgmtTftpActionErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtTftpActionErrorInfo.setStatus("current")


class _SysMgmtTftpServerAddressType_Type(InetAddressType):
    """Custom type sysMgmtTftpServerAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SysMgmtTftpServerAddressType_Type.__name__ = "InetAddressType"
_SysMgmtTftpServerAddressType_Object = MibScalar
sysMgmtTftpServerAddressType = _SysMgmtTftpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 7),
    _SysMgmtTftpServerAddressType_Type()
)
sysMgmtTftpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpServerAddressType.setStatus("current")


class _SysMgmtTftpServerAddress_Type(InetAddress):
    """Custom type sysMgmtTftpServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SysMgmtTftpServerAddress_Type.__name__ = "InetAddress"
_SysMgmtTftpServerAddress_Object = MibScalar
sysMgmtTftpServerAddress = _SysMgmtTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 10, 8),
    _SysMgmtTftpServerAddress_Type()
)
sysMgmtTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpServerAddress.setStatus("current")
_SysMgmtPacketBufferUsage_Type = Integer32
_SysMgmtPacketBufferUsage_Object = MibScalar
sysMgmtPacketBufferUsage = _SysMgmtPacketBufferUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 12),
    _SysMgmtPacketBufferUsage_Type()
)
sysMgmtPacketBufferUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtPacketBufferUsage.setStatus("current")
_SysMgmtMemoryUsage_Type = Integer32
_SysMgmtMemoryUsage_Object = MibScalar
sysMgmtMemoryUsage = _SysMgmtMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 13),
    _SysMgmtMemoryUsage_Type()
)
sysMgmtMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtMemoryUsage.setStatus("current")
_SysLoginSetup_ObjectIdentity = ObjectIdentity
sysLoginSetup = _SysLoginSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14)
)
_LoginLimitMaxNumberOfUser_Type = Integer32
_LoginLimitMaxNumberOfUser_Object = MibScalar
loginLimitMaxNumberOfUser = _LoginLimitMaxNumberOfUser_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 1),
    _LoginLimitMaxNumberOfUser_Type()
)
loginLimitMaxNumberOfUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginLimitMaxNumberOfUser.setStatus("current")
_SysLoginSetupTable_Object = MibTable
sysLoginSetupTable = _SysLoginSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 2)
)
if mibBuilder.loadTexts:
    sysLoginSetupTable.setStatus("current")
_SysLoginSetupEntry_Object = MibTableRow
sysLoginSetupEntry = _SysLoginSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 2, 1)
)
sysLoginSetupEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "sysLoginName"),
)
if mibBuilder.loadTexts:
    sysLoginSetupEntry.setStatus("current")
_SysLoginName_Type = DisplayString
_SysLoginName_Object = MibTableColumn
sysLoginName = _SysLoginName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 2, 1, 1),
    _SysLoginName_Type()
)
sysLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoginName.setStatus("current")
_SysLoginPassword_Type = DisplayString
_SysLoginPassword_Object = MibTableColumn
sysLoginPassword = _SysLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 2, 1, 2),
    _SysLoginPassword_Type()
)
sysLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginPassword.setStatus("current")
_SysLoginPrivilege_Type = Integer32
_SysLoginPrivilege_Object = MibTableColumn
sysLoginPrivilege = _SysLoginPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 2, 1, 3),
    _SysLoginPrivilege_Type()
)
sysLoginPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoginPrivilege.setStatus("current")
_SysLoginRowStatus_Type = RowStatus
_SysLoginRowStatus_Object = MibTableColumn
sysLoginRowStatus = _SysLoginRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 14, 2, 1, 4),
    _SysLoginRowStatus_Type()
)
sysLoginRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLoginRowStatus.setStatus("current")


class _SysMgmtMacFlush_Type(Integer32):
    """Custom type sysMgmtMacFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mac-flush", 1)
    )


_SysMgmtMacFlush_Type.__name__ = "Integer32"
_SysMgmtMacFlush_Object = MibScalar
sysMgmtMacFlush = _SysMgmtMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 16),
    _SysMgmtMacFlush_Type()
)
sysMgmtMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtMacFlush.setStatus("current")
_SysMgmtCPUUsageThreshold_Type = Integer32
_SysMgmtCPUUsageThreshold_Object = MibScalar
sysMgmtCPUUsageThreshold = _SysMgmtCPUUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 17),
    _SysMgmtCPUUsageThreshold_Type()
)
sysMgmtCPUUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCPUUsageThreshold.setStatus("current")
_SysMgmtPacketBufferThreshold_Type = Integer32
_SysMgmtPacketBufferThreshold_Object = MibScalar
sysMgmtPacketBufferThreshold = _SysMgmtPacketBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 18),
    _SysMgmtPacketBufferThreshold_Type()
)
sysMgmtPacketBufferThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtPacketBufferThreshold.setStatus("current")
_SysMgmtMemoryUsageThreshold_Type = Integer32
_SysMgmtMemoryUsageThreshold_Object = MibScalar
sysMgmtMemoryUsageThreshold = _SysMgmtMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 19),
    _SysMgmtMemoryUsageThreshold_Type()
)
sysMgmtMemoryUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtMemoryUsageThreshold.setStatus("current")
_SysMgmtPlusVersion_Type = Integer32
_SysMgmtPlusVersion_Object = MibScalar
sysMgmtPlusVersion = _SysMgmtPlusVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 12, 20),
    _SysMgmtPlusVersion_Type()
)
sysMgmtPlusVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtPlusVersion.setStatus("current")
_Layer2Setup_ObjectIdentity = ObjectIdentity
layer2Setup = _Layer2Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13)
)


class _VlanTypeSetup_Type(Integer32):
    """Custom type vlanTypeSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 1),
          ("port-based", 2))
    )


_VlanTypeSetup_Type.__name__ = "Integer32"
_VlanTypeSetup_Object = MibScalar
vlanTypeSetup = _VlanTypeSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 1),
    _VlanTypeSetup_Type()
)
vlanTypeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTypeSetup.setStatus("current")


class _IgmpSnoopingStateSetup_Type(Integer32):
    """Custom type igmpSnoopingStateSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enable-igmp-snooping", 2),
          ("enable-igmp-proxying", 3))
    )


_IgmpSnoopingStateSetup_Type.__name__ = "Integer32"
_IgmpSnoopingStateSetup_Object = MibScalar
igmpSnoopingStateSetup = _IgmpSnoopingStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 2),
    _IgmpSnoopingStateSetup_Type()
)
igmpSnoopingStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingStateSetup.setStatus("current")


class _TagVlanPortIsolationState_Type(Integer32):
    """Custom type tagVlanPortIsolationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("normal", 2),
          ("enhanced", 3))
    )


_TagVlanPortIsolationState_Type.__name__ = "Integer32"
_TagVlanPortIsolationState_Object = MibScalar
tagVlanPortIsolationState = _TagVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 3),
    _TagVlanPortIsolationState_Type()
)
tagVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanPortIsolationState.setStatus("current")
_StpState_Type = EnabledStatus
_StpState_Object = MibScalar
stpState = _StpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 4),
    _StpState_Type()
)
stpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpState.setStatus("current")
_IgmpFilteringStateSetup_Type = EnabledStatus
_IgmpFilteringStateSetup_Object = MibScalar
igmpFilteringStateSetup = _IgmpFilteringStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 5),
    _IgmpFilteringStateSetup_Type()
)
igmpFilteringStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpFilteringStateSetup.setStatus("current")


class _UnknownMulticastFrameForwarding_Type(Integer32):
    """Custom type unknownMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_UnknownMulticastFrameForwarding_Type.__name__ = "Integer32"
_UnknownMulticastFrameForwarding_Object = MibScalar
unknownMulticastFrameForwarding = _UnknownMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 6),
    _UnknownMulticastFrameForwarding_Type()
)
unknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastFrameForwarding.setStatus("current")
_MulticastGrpHostTimeout_Type = Integer32
_MulticastGrpHostTimeout_Object = MibScalar
multicastGrpHostTimeout = _MulticastGrpHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 7),
    _MulticastGrpHostTimeout_Type()
)
multicastGrpHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastGrpHostTimeout.setStatus("current")
_MulticastGrpLeaveTimeout_Type = Integer32
_MulticastGrpLeaveTimeout_Object = MibScalar
multicastGrpLeaveTimeout = _MulticastGrpLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 8),
    _MulticastGrpLeaveTimeout_Type()
)
multicastGrpLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastGrpLeaveTimeout.setStatus("current")


class _ReservedMulticastFrameForwarding_Type(Integer32):
    """Custom type reservedMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_ReservedMulticastFrameForwarding_Type.__name__ = "Integer32"
_ReservedMulticastFrameForwarding_Object = MibScalar
reservedMulticastFrameForwarding = _ReservedMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 9),
    _ReservedMulticastFrameForwarding_Type()
)
reservedMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reservedMulticastFrameForwarding.setStatus("current")
_Igmpsnp8021pPriority_Type = Integer32
_Igmpsnp8021pPriority_Object = MibScalar
igmpsnp8021pPriority = _Igmpsnp8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 10),
    _Igmpsnp8021pPriority_Type()
)
igmpsnp8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnp8021pPriority.setStatus("current")
_PortBasedVlanPortIsolationState_Type = Integer32
_PortBasedVlanPortIsolationState_Object = MibScalar
portBasedVlanPortIsolationState = _PortBasedVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 11),
    _PortBasedVlanPortIsolationState_Type()
)
portBasedVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedVlanPortIsolationState.setStatus("current")


class _IgmpsnpVlanMode_Type(Integer32):
    """Custom type igmpsnpVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_IgmpsnpVlanMode_Type.__name__ = "Integer32"
_IgmpsnpVlanMode_Object = MibScalar
igmpsnpVlanMode = _IgmpsnpVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 12),
    _IgmpsnpVlanMode_Type()
)
igmpsnpVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanMode.setStatus("current")


class _StpMode_Type(Integer32):
    """Custom type stpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("mrstp", 2),
          ("mstp", 3))
    )


_StpMode_Type.__name__ = "Integer32"
_StpMode_Object = MibScalar
stpMode = _StpMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 13),
    _StpMode_Type()
)
stpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMode.setStatus("current")
_IgmpsnpVlanTable_Object = MibTable
igmpsnpVlanTable = _IgmpsnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 14)
)
if mibBuilder.loadTexts:
    igmpsnpVlanTable.setStatus("current")
_IgmpsnpVlanEntry_Object = MibTableRow
igmpsnpVlanEntry = _IgmpsnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 14, 1)
)
igmpsnpVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "igmpsnpVid"),
)
if mibBuilder.loadTexts:
    igmpsnpVlanEntry.setStatus("current")
_IgmpsnpVid_Type = Integer32
_IgmpsnpVid_Object = MibTableColumn
igmpsnpVid = _IgmpsnpVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 14, 1, 1),
    _IgmpsnpVid_Type()
)
igmpsnpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsnpVid.setStatus("current")
_IgmpsnpVlanName_Type = DisplayString
_IgmpsnpVlanName_Object = MibTableColumn
igmpsnpVlanName = _IgmpsnpVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 14, 1, 2),
    _IgmpsnpVlanName_Type()
)
igmpsnpVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanName.setStatus("current")
_IgmpsnpVlanRowStatus_Type = RowStatus
_IgmpsnpVlanRowStatus_Object = MibTableColumn
igmpsnpVlanRowStatus = _IgmpsnpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 14, 1, 3),
    _IgmpsnpVlanRowStatus_Type()
)
igmpsnpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpsnpVlanRowStatus.setStatus("current")
_MgmdMLDsupport_Type = EnabledStatus
_MgmdMLDsupport_Object = MibScalar
mgmdMLDsupport = _MgmdMLDsupport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 13, 17),
    _MgmdMLDsupport_Type()
)
mgmdMLDsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmdMLDsupport.setStatus("current")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14)
)
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibScalar
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("current")


class _DefaultMgmt_Type(Integer32):
    """Custom type defaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-band", 0),
          ("out-of-band", 1))
    )


_DefaultMgmt_Type.__name__ = "Integer32"
_DefaultMgmt_Object = MibScalar
defaultMgmt = _DefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 2),
    _DefaultMgmt_Type()
)
defaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmt.setStatus("current")
_InbandIpSetup_ObjectIdentity = ObjectIdentity
inbandIpSetup = _InbandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 3)
)


class _InbandIpType_Type(Integer32):
    """Custom type inbandIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-client", 0),
          ("static-ip", 1))
    )


_InbandIpType_Type.__name__ = "Integer32"
_InbandIpType_Object = MibScalar
inbandIpType = _InbandIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 3, 1),
    _InbandIpType_Type()
)
inbandIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpType.setStatus("current")
_InbandVid_Type = Integer32
_InbandVid_Object = MibScalar
inbandVid = _InbandVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 3, 2),
    _InbandVid_Type()
)
inbandVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandVid.setStatus("current")
_InbandStaticIp_Type = IpAddress
_InbandStaticIp_Object = MibScalar
inbandStaticIp = _InbandStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 3, 3),
    _InbandStaticIp_Type()
)
inbandStaticIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticIp.setStatus("current")
_InbandStaticSubnetMask_Type = IpAddress
_InbandStaticSubnetMask_Object = MibScalar
inbandStaticSubnetMask = _InbandStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 3, 4),
    _InbandStaticSubnetMask_Type()
)
inbandStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticSubnetMask.setStatus("current")
_InbandStaticGateway_Type = IpAddress
_InbandStaticGateway_Object = MibScalar
inbandStaticGateway = _InbandStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 3, 5),
    _InbandStaticGateway_Type()
)
inbandStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticGateway.setStatus("current")
_OutOfBandIpSetup_ObjectIdentity = ObjectIdentity
outOfBandIpSetup = _OutOfBandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 4)
)
_OutOfBandIp_Type = IpAddress
_OutOfBandIp_Object = MibScalar
outOfBandIp = _OutOfBandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 4, 1),
    _OutOfBandIp_Type()
)
outOfBandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIp.setStatus("current")
_OutOfBandSubnetMask_Type = IpAddress
_OutOfBandSubnetMask_Object = MibScalar
outOfBandSubnetMask = _OutOfBandSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 4, 2),
    _OutOfBandSubnetMask_Type()
)
outOfBandSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandSubnetMask.setStatus("current")
_OutOfBandGateway_Type = IpAddress
_OutOfBandGateway_Object = MibScalar
outOfBandGateway = _OutOfBandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 4, 3),
    _OutOfBandGateway_Type()
)
outOfBandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandGateway.setStatus("current")
_MaxNumOfInbandIp_Type = Integer32
_MaxNumOfInbandIp_Object = MibScalar
maxNumOfInbandIp = _MaxNumOfInbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 5),
    _MaxNumOfInbandIp_Type()
)
maxNumOfInbandIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfInbandIp.setStatus("current")
_InbandIpTable_Object = MibTable
inbandIpTable = _InbandIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6)
)
if mibBuilder.loadTexts:
    inbandIpTable.setStatus("current")
_InbandIpEntry_Object = MibTableRow
inbandIpEntry = _InbandIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1)
)
inbandIpEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "inbandEntryIp"),
    (0, "ZYXEL-ves1608FE57-MIB", "inbandEntryVid"),
)
if mibBuilder.loadTexts:
    inbandIpEntry.setStatus("current")
_InbandEntryIp_Type = IpAddress
_InbandEntryIp_Object = MibTableColumn
inbandEntryIp = _InbandEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1, 1),
    _InbandEntryIp_Type()
)
inbandEntryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbandEntryIp.setStatus("current")
_InbandEntrySubnetMask_Type = IpAddress
_InbandEntrySubnetMask_Object = MibTableColumn
inbandEntrySubnetMask = _InbandEntrySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1, 2),
    _InbandEntrySubnetMask_Type()
)
inbandEntrySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntrySubnetMask.setStatus("current")
_InbandEntryGateway_Type = IpAddress
_InbandEntryGateway_Object = MibTableColumn
inbandEntryGateway = _InbandEntryGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1, 3),
    _InbandEntryGateway_Type()
)
inbandEntryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryGateway.setStatus("current")
_InbandEntryVid_Type = Integer32
_InbandEntryVid_Object = MibTableColumn
inbandEntryVid = _InbandEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1, 4),
    _InbandEntryVid_Type()
)
inbandEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbandEntryVid.setStatus("current")
_InbandEntryManageable_Type = EnabledStatus
_InbandEntryManageable_Object = MibTableColumn
inbandEntryManageable = _InbandEntryManageable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1, 5),
    _InbandEntryManageable_Type()
)
inbandEntryManageable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryManageable.setStatus("current")
_InbandEntryRowStatus_Type = RowStatus
_InbandEntryRowStatus_Object = MibTableColumn
inbandEntryRowStatus = _InbandEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 14, 6, 1, 6),
    _InbandEntryRowStatus_Type()
)
inbandEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inbandEntryRowStatus.setStatus("current")
_FilterSetup_ObjectIdentity = ObjectIdentity
filterSetup = _FilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("current")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "filterMacAddr"),
    (0, "ZYXEL-ves1608FE57-MIB", "filterVid"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("current")
_FilterName_Type = DisplayString
_FilterName_Object = MibTableColumn
filterName = _FilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1, 1, 1),
    _FilterName_Type()
)
filterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterName.setStatus("current")


class _FilterActionState_Type(Integer32):
    """Custom type filterActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard-source", 1),
          ("discard-destination", 2),
          ("both", 3))
    )


_FilterActionState_Type.__name__ = "Integer32"
_FilterActionState_Object = MibTableColumn
filterActionState = _FilterActionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1, 1, 2),
    _FilterActionState_Type()
)
filterActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActionState.setStatus("current")
_FilterMacAddr_Type = MacAddress
_FilterMacAddr_Object = MibTableColumn
filterMacAddr = _FilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1, 1, 3),
    _FilterMacAddr_Type()
)
filterMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMacAddr.setStatus("current")
_FilterVid_Type = Integer32
_FilterVid_Object = MibTableColumn
filterVid = _FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1, 1, 4),
    _FilterVid_Type()
)
filterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterVid.setStatus("current")
_FilterRowStatus_Type = RowStatus
_FilterRowStatus_Object = MibTableColumn
filterRowStatus = _FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 15, 1, 1, 5),
    _FilterRowStatus_Type()
)
filterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRowStatus.setStatus("current")
_MirrorSetup_ObjectIdentity = ObjectIdentity
mirrorSetup = _MirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16)
)
_MirrorState_Type = EnabledStatus
_MirrorState_Object = MibScalar
mirrorState = _MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 1),
    _MirrorState_Type()
)
mirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorState.setStatus("current")
_MirrorMonitorPort_Type = Integer32
_MirrorMonitorPort_Object = MibScalar
mirrorMonitorPort = _MirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 2),
    _MirrorMonitorPort_Type()
)
mirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMonitorPort.setStatus("current")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 3)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 3, 1)
)
mirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorMirroredState_Type = EnabledStatus
_MirrorMirroredState_Object = MibTableColumn
mirrorMirroredState = _MirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 3, 1, 1),
    _MirrorMirroredState_Type()
)
mirrorMirroredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroredState.setStatus("current")


class _MirrorDirection_Type(Integer32):
    """Custom type mirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1),
          ("both", 2))
    )


_MirrorDirection_Type.__name__ = "Integer32"
_MirrorDirection_Object = MibTableColumn
mirrorDirection = _MirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 3, 1, 2),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("current")
_MirrorRspanVid_Type = Integer32
_MirrorRspanVid_Object = MibScalar
mirrorRspanVid = _MirrorRspanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 16, 7),
    _MirrorRspanVid_Type()
)
mirrorRspanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorRspanVid.setStatus("current")
_AggrSetup_ObjectIdentity = ObjectIdentity
aggrSetup = _AggrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17)
)
_AggrState_Type = EnabledStatus
_AggrState_Object = MibScalar
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 1),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrState.setStatus("current")
_AggrSystemPriority_Type = Integer32
_AggrSystemPriority_Object = MibScalar
aggrSystemPriority = _AggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 2),
    _AggrSystemPriority_Type()
)
aggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrSystemPriority.setStatus("current")
_AggrGroupTable_Object = MibTable
aggrGroupTable = _AggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 3)
)
if mibBuilder.loadTexts:
    aggrGroupTable.setStatus("current")
_AggrGroupEntry_Object = MibTableRow
aggrGroupEntry = _AggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 3, 1)
)
aggrGroupEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrGroupEntry.setStatus("current")
_AggrGroupIndex_Type = Integer32
_AggrGroupIndex_Object = MibTableColumn
aggrGroupIndex = _AggrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 3, 1, 1),
    _AggrGroupIndex_Type()
)
aggrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrGroupIndex.setStatus("current")
_AggrGroupState_Type = EnabledStatus
_AggrGroupState_Object = MibTableColumn
aggrGroupState = _AggrGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 3, 1, 2),
    _AggrGroupState_Type()
)
aggrGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupState.setStatus("current")
_AggrGroupDynamicState_Type = EnabledStatus
_AggrGroupDynamicState_Object = MibTableColumn
aggrGroupDynamicState = _AggrGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 3, 1, 3),
    _AggrGroupDynamicState_Type()
)
aggrGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupDynamicState.setStatus("current")
_AggrPortTable_Object = MibTable
aggrPortTable = _AggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 4)
)
if mibBuilder.loadTexts:
    aggrPortTable.setStatus("current")
_AggrPortEntry_Object = MibTableRow
aggrPortEntry = _AggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 4, 1)
)
aggrPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    aggrPortEntry.setStatus("current")


class _AggrPortGroup_Type(Integer32):
    """Custom type aggrPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1", 1),
          ("t2", 2))
    )


_AggrPortGroup_Type.__name__ = "Integer32"
_AggrPortGroup_Object = MibTableColumn
aggrPortGroup = _AggrPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 4, 1, 1),
    _AggrPortGroup_Type()
)
aggrPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortGroup.setStatus("current")
_AggrPortDynamicStateTimeout_Type = Integer32
_AggrPortDynamicStateTimeout_Object = MibTableColumn
aggrPortDynamicStateTimeout = _AggrPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 17, 4, 1, 2),
    _AggrPortDynamicStateTimeout_Type()
)
aggrPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortDynamicStateTimeout.setStatus("current")
_AccessCtlSetup_ObjectIdentity = ObjectIdentity
accessCtlSetup = _AccessCtlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18)
)
_AccessCtlTable_Object = MibTable
accessCtlTable = _AccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 1)
)
if mibBuilder.loadTexts:
    accessCtlTable.setStatus("current")
_AccessCtlEntry_Object = MibTableRow
accessCtlEntry = _AccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 1, 1)
)
accessCtlEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "accessCtlService"),
)
if mibBuilder.loadTexts:
    accessCtlEntry.setStatus("current")


class _AccessCtlService_Type(Integer32):
    """Custom type accessCtlService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2),
          ("ftp", 3),
          ("http", 4),
          ("https", 5),
          ("icmp", 6),
          ("snmp", 7))
    )


_AccessCtlService_Type.__name__ = "Integer32"
_AccessCtlService_Object = MibTableColumn
accessCtlService = _AccessCtlService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 1, 1, 1),
    _AccessCtlService_Type()
)
accessCtlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtlService.setStatus("current")
_AccessCtlEnable_Type = EnabledStatus
_AccessCtlEnable_Object = MibTableColumn
accessCtlEnable = _AccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 1, 1, 2),
    _AccessCtlEnable_Type()
)
accessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlEnable.setStatus("current")
_AccessCtlServicePort_Type = Integer32
_AccessCtlServicePort_Object = MibTableColumn
accessCtlServicePort = _AccessCtlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 1, 1, 3),
    _AccessCtlServicePort_Type()
)
accessCtlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlServicePort.setStatus("current")
_AccessCtlTimeout_Type = Integer32
_AccessCtlTimeout_Object = MibTableColumn
accessCtlTimeout = _AccessCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 1, 1, 4),
    _AccessCtlTimeout_Type()
)
accessCtlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlTimeout.setStatus("current")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("current")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("current")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("current")
_SecuredClientEnable_Type = EnabledStatus
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 2),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("current")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 3),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("current")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 4),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("current")


class _SecuredClientService_Type(Bits):
    """Custom type securedClientService based on Bits"""
    namedValues = NamedValues(
        *(("telnet", 0),
          ("ftp", 1),
          ("http", 2),
          ("icmp", 3),
          ("snmp", 4),
          ("ssh", 5),
          ("https", 6))
    )

_SecuredClientService_Type.__name__ = "Bits"
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 5),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("current")


class _SecuredClientIpAddrType_Type(InetAddressType):
    """Custom type securedClientIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SecuredClientIpAddrType_Type.__name__ = "InetAddressType"
_SecuredClientIpAddrType_Object = MibTableColumn
securedClientIpAddrType = _SecuredClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 6),
    _SecuredClientIpAddrType_Type()
)
securedClientIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientIpAddrType.setStatus("current")
_SecuredClientStartIpAddr_Type = InetAddress
_SecuredClientStartIpAddr_Object = MibTableColumn
securedClientStartIpAddr = _SecuredClientStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 7),
    _SecuredClientStartIpAddr_Type()
)
securedClientStartIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIpAddr.setStatus("current")
_SecuredClientEndIpAddr_Type = InetAddress
_SecuredClientEndIpAddr_Object = MibTableColumn
securedClientEndIpAddr = _SecuredClientEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 18, 2, 1, 8),
    _SecuredClientEndIpAddr_Type()
)
securedClientEndIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIpAddr.setStatus("current")
_QueuingMethodSetup_ObjectIdentity = ObjectIdentity
queuingMethodSetup = _QueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19)
)


class _QueuingMethodType_Type(Integer32):
    """Custom type queuingMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictly-priority", 0),
          ("weighted-fair-scheduling", 1),
          ("weighted-round-robin", 2))
    )


_QueuingMethodType_Type.__name__ = "Integer32"
_QueuingMethodType_Object = MibScalar
queuingMethodType = _QueuingMethodType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 1),
    _QueuingMethodType_Type()
)
queuingMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMethodType.setStatus("current")
_PortQueuingMethodTable_Object = MibTable
portQueuingMethodTable = _PortQueuingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 2)
)
if mibBuilder.loadTexts:
    portQueuingMethodTable.setStatus("current")
_PortQueuingMethodEntry_Object = MibTableRow
portQueuingMethodEntry = _PortQueuingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 2, 1)
)
portQueuingMethodEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-ves1608FE57-MIB", "portQueuingMethodQueue"),
)
if mibBuilder.loadTexts:
    portQueuingMethodEntry.setStatus("current")
_PortQueuingMethodQueue_Type = Integer32
_PortQueuingMethodQueue_Object = MibTableColumn
portQueuingMethodQueue = _PortQueuingMethodQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 2, 1, 1),
    _PortQueuingMethodQueue_Type()
)
portQueuingMethodQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portQueuingMethodQueue.setStatus("current")
_PortQueuingMethodWeight_Type = Integer32
_PortQueuingMethodWeight_Object = MibTableColumn
portQueuingMethodWeight = _PortQueuingMethodWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 2, 1, 2),
    _PortQueuingMethodWeight_Type()
)
portQueuingMethodWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodWeight.setStatus("current")


class _QueuingMethodFeSpq_Type(Integer32):
    """Custom type queuingMethodFeSpq based on Integer32"""
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
        *(("none", 0),
          ("q0", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("q5", 6),
          ("q6", 7),
          ("q7", 8))
    )


_QueuingMethodFeSpq_Type.__name__ = "Integer32"
_QueuingMethodFeSpq_Object = MibScalar
queuingMethodFeSpq = _QueuingMethodFeSpq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 3),
    _QueuingMethodFeSpq_Type()
)
queuingMethodFeSpq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMethodFeSpq.setStatus("current")
_PortQueuingMethodGeSpqTable_Object = MibTable
portQueuingMethodGeSpqTable = _PortQueuingMethodGeSpqTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 4)
)
if mibBuilder.loadTexts:
    portQueuingMethodGeSpqTable.setStatus("current")
_PortQueuingMethodGeSpqEntry_Object = MibTableRow
portQueuingMethodGeSpqEntry = _PortQueuingMethodGeSpqEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 4, 1)
)
portQueuingMethodGeSpqEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portQueuingMethodGeSpqEntry.setStatus("current")


class _PortQueuingMethodGeSpq_Type(Integer32):
    """Custom type portQueuingMethodGeSpq based on Integer32"""
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
        *(("none", 0),
          ("q0", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("q5", 6),
          ("q6", 7),
          ("q7", 8))
    )


_PortQueuingMethodGeSpq_Type.__name__ = "Integer32"
_PortQueuingMethodGeSpq_Object = MibTableColumn
portQueuingMethodGeSpq = _PortQueuingMethodGeSpq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 19, 4, 1, 1),
    _PortQueuingMethodGeSpq_Type()
)
portQueuingMethodGeSpq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodGeSpq.setStatus("current")
_DhcpSetup_ObjectIdentity = ObjectIdentity
dhcpSetup = _DhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20)
)
_GlobalDhcpRelay_ObjectIdentity = ObjectIdentity
globalDhcpRelay = _GlobalDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1)
)
_GlobalDhcpRelayEnable_Type = EnabledStatus
_GlobalDhcpRelayEnable_Object = MibScalar
globalDhcpRelayEnable = _GlobalDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 1),
    _GlobalDhcpRelayEnable_Type()
)
globalDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayEnable.setStatus("current")
_GlobalDhcpRelayOption82Enable_Type = EnabledStatus
_GlobalDhcpRelayOption82Enable_Object = MibScalar
globalDhcpRelayOption82Enable = _GlobalDhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 2),
    _GlobalDhcpRelayOption82Enable_Type()
)
globalDhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayOption82Enable.setStatus("current")
_GlobalDhcpRelayInfoData_Type = DisplayString
_GlobalDhcpRelayInfoData_Object = MibScalar
globalDhcpRelayInfoData = _GlobalDhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 4),
    _GlobalDhcpRelayInfoData_Type()
)
globalDhcpRelayInfoData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayInfoData.setStatus("current")
_MaxNumberOfGlobalDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfGlobalDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfGlobalDhcpRelayRemoteServer = _MaxNumberOfGlobalDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 5),
    _MaxNumberOfGlobalDhcpRelayRemoteServer_Type()
)
maxNumberOfGlobalDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfGlobalDhcpRelayRemoteServer.setStatus("current")
_GlobalDhcpRelayRemoteServerTable_Object = MibTable
globalDhcpRelayRemoteServerTable = _GlobalDhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 6)
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerTable.setStatus("current")
_GlobalDhcpRelayRemoteServerEntry_Object = MibTableRow
globalDhcpRelayRemoteServerEntry = _GlobalDhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 6, 1)
)
globalDhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "globalDhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerEntry.setStatus("current")
_GlobalDhcpRelayRemoteServerIp_Type = IpAddress
_GlobalDhcpRelayRemoteServerIp_Object = MibTableColumn
globalDhcpRelayRemoteServerIp = _GlobalDhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 6, 1, 1),
    _GlobalDhcpRelayRemoteServerIp_Type()
)
globalDhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerIp.setStatus("current")
_GlobalDhcpRelayRemoteServerRowStatus_Type = RowStatus
_GlobalDhcpRelayRemoteServerRowStatus_Object = MibTableColumn
globalDhcpRelayRemoteServerRowStatus = _GlobalDhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 6, 1, 2),
    _GlobalDhcpRelayRemoteServerRowStatus_Type()
)
globalDhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerRowStatus.setStatus("current")
_GlobalDhcpRelayRemoteIDEnable_Type = EnabledStatus
_GlobalDhcpRelayRemoteIDEnable_Object = MibScalar
globalDhcpRelayRemoteIDEnable = _GlobalDhcpRelayRemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 7),
    _GlobalDhcpRelayRemoteIDEnable_Type()
)
globalDhcpRelayRemoteIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteIDEnable.setStatus("current")
_GlobalDhcpRelayRemoteIDData_Type = DisplayString
_GlobalDhcpRelayRemoteIDData_Object = MibScalar
globalDhcpRelayRemoteIDData = _GlobalDhcpRelayRemoteIDData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 8),
    _GlobalDhcpRelayRemoteIDData_Type()
)
globalDhcpRelayRemoteIDData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteIDData.setStatus("current")


class _GlobalDhcpRelayInfoType_Type(Integer32):
    """Custom type globalDhcpRelayInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("hostname", 2))
    )


_GlobalDhcpRelayInfoType_Type.__name__ = "Integer32"
_GlobalDhcpRelayInfoType_Object = MibScalar
globalDhcpRelayInfoType = _GlobalDhcpRelayInfoType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 9),
    _GlobalDhcpRelayInfoType_Type()
)
globalDhcpRelayInfoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayInfoType.setStatus("current")


class _GlobalDhcpRelayRemoteIDType_Type(Integer32):
    """Custom type globalDhcpRelayRemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("portname", 2))
    )


_GlobalDhcpRelayRemoteIDType_Type.__name__ = "Integer32"
_GlobalDhcpRelayRemoteIDType_Object = MibScalar
globalDhcpRelayRemoteIDType = _GlobalDhcpRelayRemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 1, 10),
    _GlobalDhcpRelayRemoteIDType_Type()
)
globalDhcpRelayRemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteIDType.setStatus("current")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3)
)
_MaxNumberOfDhcpRelay_Type = Integer32
_MaxNumberOfDhcpRelay_Object = MibScalar
maxNumberOfDhcpRelay = _MaxNumberOfDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 1),
    _MaxNumberOfDhcpRelay_Type()
)
maxNumberOfDhcpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelay.setStatus("current")
_MaxNumberOfDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfDhcpRelayRemoteServer = _MaxNumberOfDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 2),
    _MaxNumberOfDhcpRelayRemoteServer_Type()
)
maxNumberOfDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelayRemoteServer.setStatus("current")
_DhcpRelayTable_Object = MibTable
dhcpRelayTable = _DhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3)
)
if mibBuilder.loadTexts:
    dhcpRelayTable.setStatus("current")
_DhcpRelayEntry_Object = MibTableRow
dhcpRelayEntry = _DhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1)
)
dhcpRelayEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpRelayVid"),
)
if mibBuilder.loadTexts:
    dhcpRelayEntry.setStatus("current")
_DhcpRelayOption82Enable_Type = EnabledStatus
_DhcpRelayOption82Enable_Object = MibTableColumn
dhcpRelayOption82Enable = _DhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1, 1),
    _DhcpRelayOption82Enable_Type()
)
dhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Enable.setStatus("current")
_DhcpRelayInfoData_Type = DisplayString
_DhcpRelayInfoData_Object = MibTableColumn
dhcpRelayInfoData = _DhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1, 3),
    _DhcpRelayInfoData_Type()
)
dhcpRelayInfoData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoData.setStatus("current")
_DhcpRelayRemoteIDEnable_Type = EnabledStatus
_DhcpRelayRemoteIDEnable_Object = MibTableColumn
dhcpRelayRemoteIDEnable = _DhcpRelayRemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1, 4),
    _DhcpRelayRemoteIDEnable_Type()
)
dhcpRelayRemoteIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRemoteIDEnable.setStatus("current")
_DhcpRelayRemoteIDData_Type = DisplayString
_DhcpRelayRemoteIDData_Object = MibTableColumn
dhcpRelayRemoteIDData = _DhcpRelayRemoteIDData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1, 5),
    _DhcpRelayRemoteIDData_Type()
)
dhcpRelayRemoteIDData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRemoteIDData.setStatus("current")


class _DhcpRelayInfoType_Type(Integer32):
    """Custom type dhcpRelayInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("hostname", 2))
    )


_DhcpRelayInfoType_Type.__name__ = "Integer32"
_DhcpRelayInfoType_Object = MibTableColumn
dhcpRelayInfoType = _DhcpRelayInfoType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1, 6),
    _DhcpRelayInfoType_Type()
)
dhcpRelayInfoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoType.setStatus("current")


class _DhcpRelayRemoteIDType_Type(Integer32):
    """Custom type dhcpRelayRemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("portname", 2))
    )


_DhcpRelayRemoteIDType_Type.__name__ = "Integer32"
_DhcpRelayRemoteIDType_Object = MibTableColumn
dhcpRelayRemoteIDType = _DhcpRelayRemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 3, 1, 7),
    _DhcpRelayRemoteIDType_Type()
)
dhcpRelayRemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRemoteIDType.setStatus("current")
_DhcpRelayRemoteServerTable_Object = MibTable
dhcpRelayRemoteServerTable = _DhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerTable.setStatus("current")
_DhcpRelayRemoteServerEntry_Object = MibTableRow
dhcpRelayRemoteServerEntry = _DhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 4, 1)
)
dhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpRelayVid"),
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerEntry.setStatus("current")
_DhcpRelayVid_Type = Integer32
_DhcpRelayVid_Object = MibTableColumn
dhcpRelayVid = _DhcpRelayVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 4, 1, 1),
    _DhcpRelayVid_Type()
)
dhcpRelayVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVid.setStatus("current")
_DhcpRelayRemoteServerIp_Type = IpAddress
_DhcpRelayRemoteServerIp_Object = MibTableColumn
dhcpRelayRemoteServerIp = _DhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 4, 1, 2),
    _DhcpRelayRemoteServerIp_Type()
)
dhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerIp.setStatus("current")
_DhcpRelayRemoteServerRowStatus_Type = RowStatus
_DhcpRelayRemoteServerRowStatus_Object = MibTableColumn
dhcpRelayRemoteServerRowStatus = _DhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 20, 3, 4, 1, 3),
    _DhcpRelayRemoteServerRowStatus_Type()
)
dhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerRowStatus.setStatus("current")
_StaticRouteSetup_ObjectIdentity = ObjectIdentity
staticRouteSetup = _StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21)
)
_MaxNumberOfStaticRoutes_Type = Integer32
_MaxNumberOfStaticRoutes_Object = MibScalar
maxNumberOfStaticRoutes = _MaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 1),
    _MaxNumberOfStaticRoutes_Type()
)
maxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfStaticRoutes.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "staticRouteIp"),
    (0, "ZYXEL-ves1608FE57-MIB", "staticRouteMask"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")
_StaticRouteName_Type = DisplayString
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("current")
_StaticRouteIp_Type = IpAddress
_StaticRouteIp_Object = MibTableColumn
staticRouteIp = _StaticRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1, 2),
    _StaticRouteIp_Type()
)
staticRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteIp.setStatus("current")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("current")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("current")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("current")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 21, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("current")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1, 1)
)
arpEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "arpIpAddr"),
    (0, "ZYXEL-ves1608FE57-MIB", "arpMacVid"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("current")
_ArpIndex_Type = Integer32
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("current")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("current")
_ArpMacAddr_Type = MacAddress
_ArpMacAddr_Object = MibTableColumn
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1, 1, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("current")
_ArpMacVid_Type = Integer32
_ArpMacVid_Object = MibTableColumn
arpMacVid = _ArpMacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1, 1, 4),
    _ArpMacVid_Type()
)
arpMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacVid.setStatus("current")


class _ArpType_Type(Integer32):
    """Custom type arpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_ArpType_Type.__name__ = "Integer32"
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 22, 1, 1, 5),
    _ArpType_Type()
)
arpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpType.setStatus("current")
_PortOpModeSetup_ObjectIdentity = ObjectIdentity
portOpModeSetup = _PortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24)
)
_PortOpModePortTable_Object = MibTable
portOpModePortTable = _PortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1)
)
if mibBuilder.loadTexts:
    portOpModePortTable.setStatus("current")
_PortOpModePortEntry_Object = MibTableRow
portOpModePortEntry = _PortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1)
)
portOpModePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortEntry.setStatus("current")


class _PortOpModePortSpeedDuplex_Type(Integer32):
    """Custom type portOpModePortSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed-10-half", 1),
          ("speed-10-full", 2),
          ("speed-100-half", 3),
          ("speed-100-full", 4),
          ("speed-1000-full", 5))
    )


_PortOpModePortSpeedDuplex_Type.__name__ = "Integer32"
_PortOpModePortSpeedDuplex_Object = MibTableColumn
portOpModePortSpeedDuplex = _PortOpModePortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 1),
    _PortOpModePortSpeedDuplex_Type()
)
portOpModePortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortSpeedDuplex.setStatus("current")


class _PortOpModePortFlowCntl_Type(Integer32):
    """Custom type portOpModePortFlowCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PortOpModePortFlowCntl_Type.__name__ = "Integer32"
_PortOpModePortFlowCntl_Object = MibTableColumn
portOpModePortFlowCntl = _PortOpModePortFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 2),
    _PortOpModePortFlowCntl_Type()
)
portOpModePortFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortFlowCntl.setStatus("current")


class _PortOpModePortName_Type(OctetString):
    """Custom type portOpModePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_PortOpModePortName_Type.__name__ = "OctetString"
_PortOpModePortName_Object = MibTableColumn
portOpModePortName = _PortOpModePortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 3),
    _PortOpModePortName_Type()
)
portOpModePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortName.setStatus("current")


class _PortOpModePortModuleType_Type(Integer32):
    """Custom type portOpModePortModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet-10-100", 0),
          ("gigabit-ethernet-100-1000", 1))
    )


_PortOpModePortModuleType_Type.__name__ = "Integer32"
_PortOpModePortModuleType_Object = MibTableColumn
portOpModePortModuleType = _PortOpModePortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 4),
    _PortOpModePortModuleType_Type()
)
portOpModePortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortModuleType.setStatus("current")


class _PortOpModePortLinkUpType_Type(Integer32):
    """Custom type portOpModePortLinkUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("copper", 1),
          ("fiber", 2))
    )


_PortOpModePortLinkUpType_Type.__name__ = "Integer32"
_PortOpModePortLinkUpType_Object = MibTableColumn
portOpModePortLinkUpType = _PortOpModePortLinkUpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 5),
    _PortOpModePortLinkUpType_Type()
)
portOpModePortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLinkUpType.setStatus("current")
_PortOpModePortIntrusionLock_Type = EnabledStatus
_PortOpModePortIntrusionLock_Object = MibTableColumn
portOpModePortIntrusionLock = _PortOpModePortIntrusionLock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 6),
    _PortOpModePortIntrusionLock_Type()
)
portOpModePortIntrusionLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortIntrusionLock.setStatus("current")


class _PortOpModePortLBTestSetup_Type(Integer32):
    """Custom type portOpModePortLBTestSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("internal-loopback-test", 1)
    )


_PortOpModePortLBTestSetup_Type.__name__ = "Integer32"
_PortOpModePortLBTestSetup_Object = MibTableColumn
portOpModePortLBTestSetup = _PortOpModePortLBTestSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 7),
    _PortOpModePortLBTestSetup_Type()
)
portOpModePortLBTestSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortLBTestSetup.setStatus("current")


class _PortOpModePortLBTestStatus_Type(Integer32):
    """Custom type portOpModePortLBTestStatus based on Integer32"""
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
        *(("none", 0),
          ("under-testing", 1),
          ("success", 2),
          ("fail", 3))
    )


_PortOpModePortLBTestStatus_Type.__name__ = "Integer32"
_PortOpModePortLBTestStatus_Object = MibTableColumn
portOpModePortLBTestStatus = _PortOpModePortLBTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 8),
    _PortOpModePortLBTestStatus_Type()
)
portOpModePortLBTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBTestStatus.setStatus("current")


class _PortOpModePortSwCounterReset_Type(Integer32):
    """Custom type portOpModePortSwCounterReset based on Integer32"""
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


_PortOpModePortSwCounterReset_Type.__name__ = "Integer32"
_PortOpModePortSwCounterReset_Object = MibTableColumn
portOpModePortSwCounterReset = _PortOpModePortSwCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 9),
    _PortOpModePortSwCounterReset_Type()
)
portOpModePortSwCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortSwCounterReset.setStatus("current")


class _PortOpModePortVdslCounterReset_Type(Integer32):
    """Custom type portOpModePortVdslCounterReset based on Integer32"""
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


_PortOpModePortVdslCounterReset_Type.__name__ = "Integer32"
_PortOpModePortVdslCounterReset_Object = MibTableColumn
portOpModePortVdslCounterReset = _PortOpModePortVdslCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 10),
    _PortOpModePortVdslCounterReset_Type()
)
portOpModePortVdslCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortVdslCounterReset.setStatus("current")


class _PortOpModePortVdslStatus_Type(Integer32):
    """Custom type portOpModePortVdslStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("standby", 2),
          ("showtime", 3))
    )


_PortOpModePortVdslStatus_Type.__name__ = "Integer32"
_PortOpModePortVdslStatus_Object = MibTableColumn
portOpModePortVdslStatus = _PortOpModePortVdslStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 11),
    _PortOpModePortVdslStatus_Type()
)
portOpModePortVdslStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortVdslStatus.setStatus("current")
_PortOpModePortVdslUptime_Type = OctetString
_PortOpModePortVdslUptime_Object = MibTableColumn
portOpModePortVdslUptime = _PortOpModePortVdslUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 1, 1, 12),
    _PortOpModePortVdslUptime_Type()
)
portOpModePortVdslUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortVdslUptime.setStatus("current")
_PortOpModePortLBTable_Object = MibTable
portOpModePortLBTable = _PortOpModePortLBTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 2)
)
if mibBuilder.loadTexts:
    portOpModePortLBTable.setStatus("current")
_PortOpModePortLBEntry_Object = MibTableRow
portOpModePortLBEntry = _PortOpModePortLBEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 2, 1)
)
portOpModePortLBEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortLBEntry.setStatus("current")


class _PortOpModePortLBActive_Type(Integer32):
    """Custom type portOpModePortLBActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_PortOpModePortLBActive_Type.__name__ = "Integer32"
_PortOpModePortLBActive_Object = MibTableColumn
portOpModePortLBActive = _PortOpModePortLBActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 2, 1, 1),
    _PortOpModePortLBActive_Type()
)
portOpModePortLBActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortLBActive.setStatus("current")
_PortOpModePortLBNumber_Type = Integer32
_PortOpModePortLBNumber_Object = MibTableColumn
portOpModePortLBNumber = _PortOpModePortLBNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 2, 1, 2),
    _PortOpModePortLBNumber_Type()
)
portOpModePortLBNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortLBNumber.setStatus("current")
_PortOpModePortLBCount_Type = Integer32
_PortOpModePortLBCount_Object = MibTableColumn
portOpModePortLBCount = _PortOpModePortLBCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 2, 1, 3),
    _PortOpModePortLBCount_Type()
)
portOpModePortLBCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortLBCount.setStatus("current")
_PortOpModePortLBPktSize_Type = Integer32
_PortOpModePortLBPktSize_Object = MibTableColumn
portOpModePortLBPktSize = _PortOpModePortLBPktSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 2, 1, 4),
    _PortOpModePortLBPktSize_Type()
)
portOpModePortLBPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortLBPktSize.setStatus("current")
_PortOpModePortLBResultTable_Object = MibTable
portOpModePortLBResultTable = _PortOpModePortLBResultTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3)
)
if mibBuilder.loadTexts:
    portOpModePortLBResultTable.setStatus("current")
_PortOpModePortLBResultEntry_Object = MibTableRow
portOpModePortLBResultEntry = _PortOpModePortLBResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3, 1)
)
portOpModePortLBResultEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortLBResultEntry.setStatus("current")
_PortOpModePortLBMaxRTT_Type = Integer32
_PortOpModePortLBMaxRTT_Object = MibTableColumn
portOpModePortLBMaxRTT = _PortOpModePortLBMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3, 1, 1),
    _PortOpModePortLBMaxRTT_Type()
)
portOpModePortLBMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBMaxRTT.setStatus("current")
_PortOpModePortLBMinRTT_Type = Integer32
_PortOpModePortLBMinRTT_Object = MibTableColumn
portOpModePortLBMinRTT = _PortOpModePortLBMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3, 1, 2),
    _PortOpModePortLBMinRTT_Type()
)
portOpModePortLBMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBMinRTT.setStatus("current")
_PortOpModePortLBAvgRTT_Type = Integer32
_PortOpModePortLBAvgRTT_Object = MibTableColumn
portOpModePortLBAvgRTT = _PortOpModePortLBAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3, 1, 3),
    _PortOpModePortLBAvgRTT_Type()
)
portOpModePortLBAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBAvgRTT.setStatus("current")
_PortOpModePortLBPktLossRate_Type = Integer32
_PortOpModePortLBPktLossRate_Object = MibTableColumn
portOpModePortLBPktLossRate = _PortOpModePortLBPktLossRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3, 1, 4),
    _PortOpModePortLBPktLossRate_Type()
)
portOpModePortLBPktLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBPktLossRate.setStatus("current")


class _PortOpModePortLBStatus_Type(Integer32):
    """Custom type portOpModePortLBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("in-progress", 1),
          ("complete", 2))
    )


_PortOpModePortLBStatus_Type.__name__ = "Integer32"
_PortOpModePortLBStatus_Object = MibTableColumn
portOpModePortLBStatus = _PortOpModePortLBStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 24, 3, 1, 5),
    _PortOpModePortLBStatus_Type()
)
portOpModePortLBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBStatus.setStatus("current")
_PortBasedVlanSetup_ObjectIdentity = ObjectIdentity
portBasedVlanSetup = _PortBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 25)
)
_PortBasedVlanPortListTable_Object = MibTable
portBasedVlanPortListTable = _PortBasedVlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 25, 1)
)
if mibBuilder.loadTexts:
    portBasedVlanPortListTable.setStatus("current")
_PortBasedVlanPortListEntry_Object = MibTableRow
portBasedVlanPortListEntry = _PortBasedVlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 25, 1, 1)
)
portBasedVlanPortListEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBasedVlanPortListEntry.setStatus("current")
_PortBasedVlanPortListMembers_Type = PortList
_PortBasedVlanPortListMembers_Object = MibTableColumn
portBasedVlanPortListMembers = _PortBasedVlanPortListMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 25, 1, 1, 1),
    _PortBasedVlanPortListMembers_Type()
)
portBasedVlanPortListMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedVlanPortListMembers.setStatus("current")
_FaultMIB_ObjectIdentity = ObjectIdentity
faultMIB = _FaultMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26)
)
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventSeqNum_Type = Integer32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventEventId_Type = EventIdNumber
_EventEventId_Object = MibTableColumn
eventEventId = _EventEventId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 2),
    _EventEventId_Type()
)
eventEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventEventId.setStatus("current")


class _EventName_Type(DisplayString):
    """Custom type eventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EventName_Type.__name__ = "DisplayString"
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventInstanceType_Type = InstanceType
_EventInstanceType_Object = MibTableColumn
eventInstanceType = _EventInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 4),
    _EventInstanceType_Type()
)
eventInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceType.setStatus("current")
_EventInstanceId_Type = DisplayString
_EventInstanceId_Object = MibTableColumn
eventInstanceId = _EventInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 5),
    _EventInstanceId_Type()
)
eventInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceId.setStatus("current")
_EventInstanceName_Type = DisplayString
_EventInstanceName_Object = MibTableColumn
eventInstanceName = _EventInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 6),
    _EventInstanceName_Type()
)
eventInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceName.setStatus("current")
_EventSeverity_Type = EventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventSetTime_Type = UtcTimeStamp
_EventSetTime_Object = MibTableColumn
eventSetTime = _EventSetTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 8),
    _EventSetTime_Type()
)
eventSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSetTime.setStatus("current")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 9),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_EventServAffective_Type = EventServiceAffective
_EventServAffective_Object = MibTableColumn
eventServAffective = _EventServAffective_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 10),
    _EventServAffective_Type()
)
eventServAffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventServAffective.setStatus("current")
_EventInstanceIdNumber_Type = Integer32
_EventInstanceIdNumber_Object = MibTableColumn
eventInstanceIdNumber = _EventInstanceIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 26, 1, 1, 1, 11),
    _EventInstanceIdNumber_Type()
)
eventInstanceIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceIdNumber.setStatus("current")
_FaultTrapsMIB_ObjectIdentity = ObjectIdentity
faultTrapsMIB = _FaultTrapsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27)
)
_TrapInfoObjects_ObjectIdentity = ObjectIdentity
trapInfoObjects = _TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 1)
)
_TrapRefSeqNum_Type = Integer32
_TrapRefSeqNum_Object = MibScalar
trapRefSeqNum = _TrapRefSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 1, 1),
    _TrapRefSeqNum_Type()
)
trapRefSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRefSeqNum.setStatus("current")
_TrapPersistence_Type = EventPersistence
_TrapPersistence_Object = MibScalar
trapPersistence = _TrapPersistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 1, 2),
    _TrapPersistence_Type()
)
trapPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPersistence.setStatus("current")
_TrapSenderNodeId_Type = Integer32
_TrapSenderNodeId_Object = MibScalar
trapSenderNodeId = _TrapSenderNodeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 1, 3),
    _TrapSenderNodeId_Type()
)
trapSenderNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderNodeId.setStatus("current")
_TrapSenderStatus_Type = Integer32
_TrapSenderStatus_Object = MibScalar
trapSenderStatus = _TrapSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 1, 4),
    _TrapSenderStatus_Type()
)
trapSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderStatus.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 2)
)
_MulticastPortSetup_ObjectIdentity = ObjectIdentity
multicastPortSetup = _MulticastPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28)
)
_MulticastPortTable_Object = MibTable
multicastPortTable = _MulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1)
)
if mibBuilder.loadTexts:
    multicastPortTable.setStatus("current")
_MulticastPortEntry_Object = MibTableRow
multicastPortEntry = _MulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1)
)
multicastPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    multicastPortEntry.setStatus("current")
_MulticastPortImmediateLeave_Type = EnabledStatus
_MulticastPortImmediateLeave_Object = MibTableColumn
multicastPortImmediateLeave = _MulticastPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 1),
    _MulticastPortImmediateLeave_Type()
)
multicastPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortImmediateLeave.setStatus("current")
_MulticastPortMaxGroupLimited_Type = EnabledStatus
_MulticastPortMaxGroupLimited_Object = MibTableColumn
multicastPortMaxGroupLimited = _MulticastPortMaxGroupLimited_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 2),
    _MulticastPortMaxGroupLimited_Type()
)
multicastPortMaxGroupLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxGroupLimited.setStatus("current")
_MulticastPortMaxOfGroup_Type = Integer32
_MulticastPortMaxOfGroup_Object = MibTableColumn
multicastPortMaxOfGroup = _MulticastPortMaxOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 3),
    _MulticastPortMaxOfGroup_Type()
)
multicastPortMaxOfGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxOfGroup.setStatus("current")
_MulticastPortIgmpFilteringProfile_Type = DisplayString
_MulticastPortIgmpFilteringProfile_Object = MibTableColumn
multicastPortIgmpFilteringProfile = _MulticastPortIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 4),
    _MulticastPortIgmpFilteringProfile_Type()
)
multicastPortIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortIgmpFilteringProfile.setStatus("current")


class _MulticastPortQueryMode_Type(Integer32):
    """Custom type multicastPortQueryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-mode", 1),
          ("fix-mode", 2),
          ("edge-mode", 3))
    )


_MulticastPortQueryMode_Type.__name__ = "Integer32"
_MulticastPortQueryMode_Object = MibTableColumn
multicastPortQueryMode = _MulticastPortQueryMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 5),
    _MulticastPortQueryMode_Type()
)
multicastPortQueryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortQueryMode.setStatus("current")
_IgmpMsgMaxLimited_Type = EnabledStatus
_IgmpMsgMaxLimited_Object = MibTableColumn
igmpMsgMaxLimited = _IgmpMsgMaxLimited_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 6),
    _IgmpMsgMaxLimited_Type()
)
igmpMsgMaxLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMsgMaxLimited.setStatus("current")
_IgmpMsgLimit_Type = Integer32
_IgmpMsgLimit_Object = MibTableColumn
igmpMsgLimit = _IgmpMsgLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 28, 1, 1, 7),
    _IgmpMsgLimit_Type()
)
igmpMsgLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMsgLimit.setStatus("current")
_MulticastStatus_ObjectIdentity = ObjectIdentity
multicastStatus = _MulticastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29)
)
_MulticastStatusTable_Object = MibTable
multicastStatusTable = _MulticastStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1)
)
if mibBuilder.loadTexts:
    multicastStatusTable.setStatus("current")
_MulticastStatusEntry_Object = MibTableRow
multicastStatusEntry = _MulticastStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1)
)
multicastStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastStatusEntry.setStatus("current")
_MulticastStatusIndex_Type = Integer32
_MulticastStatusIndex_Object = MibTableColumn
multicastStatusIndex = _MulticastStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1, 1),
    _MulticastStatusIndex_Type()
)
multicastStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusIndex.setStatus("current")
_MulticastStatusVlanID_Type = Integer32
_MulticastStatusVlanID_Object = MibTableColumn
multicastStatusVlanID = _MulticastStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1, 2),
    _MulticastStatusVlanID_Type()
)
multicastStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusVlanID.setStatus("current")
_MulticastStatusPort_Type = Integer32
_MulticastStatusPort_Object = MibTableColumn
multicastStatusPort = _MulticastStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1, 3),
    _MulticastStatusPort_Type()
)
multicastStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusPort.setStatus("current")
_MulticastStatusGroup_Type = IpAddress
_MulticastStatusGroup_Object = MibTableColumn
multicastStatusGroup = _MulticastStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1, 4),
    _MulticastStatusGroup_Type()
)
multicastStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusGroup.setStatus("current")
_MulticastStatusJoinCounter_Type = Integer32
_MulticastStatusJoinCounter_Object = MibTableColumn
multicastStatusJoinCounter = _MulticastStatusJoinCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1, 5),
    _MulticastStatusJoinCounter_Type()
)
multicastStatusJoinCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusJoinCounter.setStatus("current")
_MulticastStatusLeaveCounter_Type = Integer32
_MulticastStatusLeaveCounter_Object = MibTableColumn
multicastStatusLeaveCounter = _MulticastStatusLeaveCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 1, 1, 6),
    _MulticastStatusLeaveCounter_Type()
)
multicastStatusLeaveCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusLeaveCounter.setStatus("current")
_IgmpCountTable_Object = MibTable
igmpCountTable = _IgmpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2)
)
if mibBuilder.loadTexts:
    igmpCountTable.setStatus("current")
_IgmpCountEntry_Object = MibTableRow
igmpCountEntry = _IgmpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1)
)
igmpCountEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "igmpCountIndex"),
)
if mibBuilder.loadTexts:
    igmpCountEntry.setStatus("current")
_IgmpCountIndex_Type = Integer32
_IgmpCountIndex_Object = MibTableColumn
igmpCountIndex = _IgmpCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 1),
    _IgmpCountIndex_Type()
)
igmpCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountIndex.setStatus("current")
_IgmpCountInQuery_Type = Integer32
_IgmpCountInQuery_Object = MibTableColumn
igmpCountInQuery = _IgmpCountInQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 2),
    _IgmpCountInQuery_Type()
)
igmpCountInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInQuery.setStatus("current")
_IgmpCountInReport_Type = Integer32
_IgmpCountInReport_Object = MibTableColumn
igmpCountInReport = _IgmpCountInReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 3),
    _IgmpCountInReport_Type()
)
igmpCountInReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInReport.setStatus("current")
_IgmpCountInLeave_Type = Integer32
_IgmpCountInLeave_Object = MibTableColumn
igmpCountInLeave = _IgmpCountInLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 4),
    _IgmpCountInLeave_Type()
)
igmpCountInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInLeave.setStatus("current")
_IgmpCountInQueryDrop_Type = Integer32
_IgmpCountInQueryDrop_Object = MibTableColumn
igmpCountInQueryDrop = _IgmpCountInQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 5),
    _IgmpCountInQueryDrop_Type()
)
igmpCountInQueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInQueryDrop.setStatus("current")
_IgmpCountInReportDrop_Type = Integer32
_IgmpCountInReportDrop_Object = MibTableColumn
igmpCountInReportDrop = _IgmpCountInReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 6),
    _IgmpCountInReportDrop_Type()
)
igmpCountInReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInReportDrop.setStatus("current")
_IgmpCountInLeaveDrop_Type = Integer32
_IgmpCountInLeaveDrop_Object = MibTableColumn
igmpCountInLeaveDrop = _IgmpCountInLeaveDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 7),
    _IgmpCountInLeaveDrop_Type()
)
igmpCountInLeaveDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInLeaveDrop.setStatus("current")
_IgmpCountOutQuery_Type = Integer32
_IgmpCountOutQuery_Object = MibTableColumn
igmpCountOutQuery = _IgmpCountOutQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 8),
    _IgmpCountOutQuery_Type()
)
igmpCountOutQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutQuery.setStatus("current")
_IgmpCountOutReport_Type = Integer32
_IgmpCountOutReport_Object = MibTableColumn
igmpCountOutReport = _IgmpCountOutReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 9),
    _IgmpCountOutReport_Type()
)
igmpCountOutReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutReport.setStatus("current")
_IgmpCountOutLeave_Type = Integer32
_IgmpCountOutLeave_Object = MibTableColumn
igmpCountOutLeave = _IgmpCountOutLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 2, 1, 10),
    _IgmpCountOutLeave_Type()
)
igmpCountOutLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutLeave.setStatus("current")
_MulticastVlanStatusTable_Object = MibTable
multicastVlanStatusTable = _MulticastVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 3)
)
if mibBuilder.loadTexts:
    multicastVlanStatusTable.setStatus("current")
_MulticastVlanStatusEntry_Object = MibTableRow
multicastVlanStatusEntry = _MulticastVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 3, 1)
)
multicastVlanStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "multicastVlanStatusVlanID"),
)
if mibBuilder.loadTexts:
    multicastVlanStatusEntry.setStatus("current")
_MulticastVlanStatusVlanID_Type = Integer32
_MulticastVlanStatusVlanID_Object = MibTableColumn
multicastVlanStatusVlanID = _MulticastVlanStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 3, 1, 1),
    _MulticastVlanStatusVlanID_Type()
)
multicastVlanStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusVlanID.setStatus("current")


class _MulticastVlanStatusType_Type(Integer32):
    """Custom type multicastVlanStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("mvr", 2),
          ("static", 3))
    )


_MulticastVlanStatusType_Type.__name__ = "Integer32"
_MulticastVlanStatusType_Object = MibTableColumn
multicastVlanStatusType = _MulticastVlanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 3, 1, 2),
    _MulticastVlanStatusType_Type()
)
multicastVlanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusType.setStatus("current")
_MulticastVlanQueryPort_Type = PortList
_MulticastVlanQueryPort_Object = MibTableColumn
multicastVlanQueryPort = _MulticastVlanQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 3, 1, 3),
    _MulticastVlanQueryPort_Type()
)
multicastVlanQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanQueryPort.setStatus("current")
_MulticastVlanQuerySrcIp_Type = IpAddress
_MulticastVlanQuerySrcIp_Object = MibTableColumn
multicastVlanQuerySrcIp = _MulticastVlanQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 3, 1, 4),
    _MulticastVlanQuerySrcIp_Type()
)
multicastVlanQuerySrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanQuerySrcIp.setStatus("current")
_IgmpCounterPortTable_Object = MibTable
igmpCounterPortTable = _IgmpCounterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 4)
)
if mibBuilder.loadTexts:
    igmpCounterPortTable.setStatus("current")
_IgmpCounterPortEntry_Object = MibTableRow
igmpCounterPortEntry = _IgmpCounterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 4, 1)
)
igmpCounterPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    igmpCounterPortEntry.setStatus("current")
_IgmpCounterPortJoin_Type = Counter32
_IgmpCounterPortJoin_Object = MibTableColumn
igmpCounterPortJoin = _IgmpCounterPortJoin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 4, 1, 1),
    _IgmpCounterPortJoin_Type()
)
igmpCounterPortJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortJoin.setStatus("current")
_IgmpCounterPortLeave_Type = Counter32
_IgmpCounterPortLeave_Object = MibTableColumn
igmpCounterPortLeave = _IgmpCounterPortLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 4, 1, 2),
    _IgmpCounterPortLeave_Type()
)
igmpCounterPortLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortLeave.setStatus("current")
_IgmpCounterPortActiveGroup_Type = Integer32
_IgmpCounterPortActiveGroup_Object = MibTableColumn
igmpCounterPortActiveGroup = _IgmpCounterPortActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 4, 1, 3),
    _IgmpCounterPortActiveGroup_Type()
)
igmpCounterPortActiveGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortActiveGroup.setStatus("current")
_IgmpCounterPortQuery_Type = Counter32
_IgmpCounterPortQuery_Object = MibTableColumn
igmpCounterPortQuery = _IgmpCounterPortQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 4, 1, 4),
    _IgmpCounterPortQuery_Type()
)
igmpCounterPortQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterPortQuery.setStatus("current")
_IgmpCounterVlanTable_Object = MibTable
igmpCounterVlanTable = _IgmpCounterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 5)
)
if mibBuilder.loadTexts:
    igmpCounterVlanTable.setStatus("current")
_IgmpCounterVlanEntry_Object = MibTableRow
igmpCounterVlanEntry = _IgmpCounterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 5, 1)
)
igmpCounterVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpCounterVlanEntry.setStatus("current")
_IgmpCounterVlanJoin_Type = Counter32
_IgmpCounterVlanJoin_Object = MibTableColumn
igmpCounterVlanJoin = _IgmpCounterVlanJoin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 5, 1, 1),
    _IgmpCounterVlanJoin_Type()
)
igmpCounterVlanJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanJoin.setStatus("current")
_IgmpCounterVlanLeave_Type = Counter32
_IgmpCounterVlanLeave_Object = MibTableColumn
igmpCounterVlanLeave = _IgmpCounterVlanLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 5, 1, 2),
    _IgmpCounterVlanLeave_Type()
)
igmpCounterVlanLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanLeave.setStatus("current")
_IgmpCounterVlanActiveGroup_Type = Integer32
_IgmpCounterVlanActiveGroup_Object = MibTableColumn
igmpCounterVlanActiveGroup = _IgmpCounterVlanActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 5, 1, 3),
    _IgmpCounterVlanActiveGroup_Type()
)
igmpCounterVlanActiveGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanActiveGroup.setStatus("current")
_IgmpCounterVlanQuery_Type = Counter32
_IgmpCounterVlanQuery_Object = MibTableColumn
igmpCounterVlanQuery = _IgmpCounterVlanQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 5, 1, 4),
    _IgmpCounterVlanQuery_Type()
)
igmpCounterVlanQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCounterVlanQuery.setStatus("current")
_MulticastCurrentGroupStatusTable_Object = MibTable
multicastCurrentGroupStatusTable = _MulticastCurrentGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 6)
)
if mibBuilder.loadTexts:
    multicastCurrentGroupStatusTable.setStatus("current")
_MulticastCurrentGroupStatusEntry_Object = MibTableRow
multicastCurrentGroupStatusEntry = _MulticastCurrentGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 6, 1)
)
multicastCurrentGroupStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastCurrentGroupStatusEntry.setStatus("current")
_MulticastCurrentNumberOfActivePort_Type = Integer32
_MulticastCurrentNumberOfActivePort_Object = MibTableColumn
multicastCurrentNumberOfActivePort = _MulticastCurrentNumberOfActivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 6, 1, 1),
    _MulticastCurrentNumberOfActivePort_Type()
)
multicastCurrentNumberOfActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastCurrentNumberOfActivePort.setStatus("current")
_MulticastClientSrcIpTable_Object = MibTable
multicastClientSrcIpTable = _MulticastClientSrcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 7)
)
if mibBuilder.loadTexts:
    multicastClientSrcIpTable.setStatus("current")
_MulticastClientSrcIpEntry_Object = MibTableRow
multicastClientSrcIpEntry = _MulticastClientSrcIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 7, 1)
)
multicastClientSrcIpEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "multicastStatusGroup"),
    (0, "ZYXEL-ves1608FE57-MIB", "multicastClientSrcIpIndex"),
)
if mibBuilder.loadTexts:
    multicastClientSrcIpEntry.setStatus("current")
_MulticastClientSrcIpIndex_Type = Integer32
_MulticastClientSrcIpIndex_Object = MibTableColumn
multicastClientSrcIpIndex = _MulticastClientSrcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 7, 1, 1),
    _MulticastClientSrcIpIndex_Type()
)
multicastClientSrcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastClientSrcIpIndex.setStatus("current")
_MulticastClientSrcIpAddress_Type = IpAddress
_MulticastClientSrcIpAddress_Object = MibTableColumn
multicastClientSrcIpAddress = _MulticastClientSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 7, 1, 2),
    _MulticastClientSrcIpAddress_Type()
)
multicastClientSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastClientSrcIpAddress.setStatus("current")
_MgmdStatusTable_Object = MibTable
mgmdStatusTable = _MgmdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8)
)
if mibBuilder.loadTexts:
    mgmdStatusTable.setStatus("current")
_MgmdStatusEntry_Object = MibTableRow
mgmdStatusEntry = _MgmdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1)
)
mgmdStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusGroupAddressType"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusGroupAddress"),
)
if mibBuilder.loadTexts:
    mgmdStatusEntry.setStatus("current")
_MgmdStatusIndex_Type = Integer32
_MgmdStatusIndex_Object = MibTableColumn
mgmdStatusIndex = _MgmdStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1, 1),
    _MgmdStatusIndex_Type()
)
mgmdStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusIndex.setStatus("current")
_MgmdStatusVlanID_Type = Integer32
_MgmdStatusVlanID_Object = MibTableColumn
mgmdStatusVlanID = _MgmdStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1, 2),
    _MgmdStatusVlanID_Type()
)
mgmdStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusVlanID.setStatus("current")
_MgmdStatusPort_Type = Integer32
_MgmdStatusPort_Object = MibTableColumn
mgmdStatusPort = _MgmdStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1, 3),
    _MgmdStatusPort_Type()
)
mgmdStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusPort.setStatus("current")


class _MgmdStatusGroupAddressType_Type(InetAddressType):
    """Custom type mgmdStatusGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdStatusGroupAddressType_Type.__name__ = "InetAddressType"
_MgmdStatusGroupAddressType_Object = MibTableColumn
mgmdStatusGroupAddressType = _MgmdStatusGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1, 4),
    _MgmdStatusGroupAddressType_Type()
)
mgmdStatusGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupAddressType.setStatus("current")


class _MgmdStatusGroupAddress_Type(InetAddress):
    """Custom type mgmdStatusGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdStatusGroupAddress_Type.__name__ = "InetAddress"
_MgmdStatusGroupAddress_Object = MibTableColumn
mgmdStatusGroupAddress = _MgmdStatusGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1, 5),
    _MgmdStatusGroupAddress_Type()
)
mgmdStatusGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupAddress.setStatus("current")


class _MgmdStatusGroupFilterMode_Type(Integer32):
    """Custom type mgmdStatusGroupFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_MgmdStatusGroupFilterMode_Type.__name__ = "Integer32"
_MgmdStatusGroupFilterMode_Object = MibTableColumn
mgmdStatusGroupFilterMode = _MgmdStatusGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 8, 1, 6),
    _MgmdStatusGroupFilterMode_Type()
)
mgmdStatusGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdStatusGroupFilterMode.setStatus("current")
_MgmdCountTable_Object = MibTable
mgmdCountTable = _MgmdCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9)
)
if mibBuilder.loadTexts:
    mgmdCountTable.setStatus("current")
_MgmdCountEntry_Object = MibTableRow
mgmdCountEntry = _MgmdCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1)
)
mgmdCountEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdCountIndex"),
)
if mibBuilder.loadTexts:
    mgmdCountEntry.setStatus("current")
_MgmdCountIndex_Type = Integer32
_MgmdCountIndex_Object = MibTableColumn
mgmdCountIndex = _MgmdCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 1),
    _MgmdCountIndex_Type()
)
mgmdCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountIndex.setStatus("current")
_MgmdCountInQuery_Type = Integer32
_MgmdCountInQuery_Object = MibTableColumn
mgmdCountInQuery = _MgmdCountInQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 2),
    _MgmdCountInQuery_Type()
)
mgmdCountInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInQuery.setStatus("current")
_MgmdCountInReport_Type = Integer32
_MgmdCountInReport_Object = MibTableColumn
mgmdCountInReport = _MgmdCountInReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 3),
    _MgmdCountInReport_Type()
)
mgmdCountInReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInReport.setStatus("current")
_MgmdCountInLeave_Type = Integer32
_MgmdCountInLeave_Object = MibTableColumn
mgmdCountInLeave = _MgmdCountInLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 4),
    _MgmdCountInLeave_Type()
)
mgmdCountInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInLeave.setStatus("current")
_MgmdCountInQueryDrop_Type = Integer32
_MgmdCountInQueryDrop_Object = MibTableColumn
mgmdCountInQueryDrop = _MgmdCountInQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 5),
    _MgmdCountInQueryDrop_Type()
)
mgmdCountInQueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInQueryDrop.setStatus("current")
_MgmdCountInReportDrop_Type = Integer32
_MgmdCountInReportDrop_Object = MibTableColumn
mgmdCountInReportDrop = _MgmdCountInReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 6),
    _MgmdCountInReportDrop_Type()
)
mgmdCountInReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInReportDrop.setStatus("current")
_MgmdCountInLeaveDrop_Type = Integer32
_MgmdCountInLeaveDrop_Object = MibTableColumn
mgmdCountInLeaveDrop = _MgmdCountInLeaveDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 7),
    _MgmdCountInLeaveDrop_Type()
)
mgmdCountInLeaveDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountInLeaveDrop.setStatus("current")
_MgmdCountOutQuery_Type = Integer32
_MgmdCountOutQuery_Object = MibTableColumn
mgmdCountOutQuery = _MgmdCountOutQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 8),
    _MgmdCountOutQuery_Type()
)
mgmdCountOutQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountOutQuery.setStatus("current")
_MgmdCountOutReport_Type = Integer32
_MgmdCountOutReport_Object = MibTableColumn
mgmdCountOutReport = _MgmdCountOutReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 9),
    _MgmdCountOutReport_Type()
)
mgmdCountOutReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountOutReport.setStatus("current")
_MgmdCountOutLeave_Type = Integer32
_MgmdCountOutLeave_Object = MibTableColumn
mgmdCountOutLeave = _MgmdCountOutLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 9, 1, 10),
    _MgmdCountOutLeave_Type()
)
mgmdCountOutLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCountOutLeave.setStatus("current")
_MgmdVlanStatusTable_Object = MibTable
mgmdVlanStatusTable = _MgmdVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10)
)
if mibBuilder.loadTexts:
    mgmdVlanStatusTable.setStatus("current")
_MgmdVlanStatusEntry_Object = MibTableRow
mgmdVlanStatusEntry = _MgmdVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10, 1)
)
mgmdVlanStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdVlanStatusVlanID"),
)
if mibBuilder.loadTexts:
    mgmdVlanStatusEntry.setStatus("current")
_MgmdVlanStatusVlanID_Type = Integer32
_MgmdVlanStatusVlanID_Object = MibTableColumn
mgmdVlanStatusVlanID = _MgmdVlanStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10, 1, 1),
    _MgmdVlanStatusVlanID_Type()
)
mgmdVlanStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanStatusVlanID.setStatus("current")


class _MgmdVlanStatusType_Type(Integer32):
    """Custom type mgmdVlanStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("mvr", 2),
          ("static", 3))
    )


_MgmdVlanStatusType_Type.__name__ = "Integer32"
_MgmdVlanStatusType_Object = MibTableColumn
mgmdVlanStatusType = _MgmdVlanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10, 1, 2),
    _MgmdVlanStatusType_Type()
)
mgmdVlanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanStatusType.setStatus("current")
_MgmdVlanQueryPort_Type = PortList
_MgmdVlanQueryPort_Object = MibTableColumn
mgmdVlanQueryPort = _MgmdVlanQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10, 1, 3),
    _MgmdVlanQueryPort_Type()
)
mgmdVlanQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanQueryPort.setStatus("current")


class _MgmdVlanQuerySrcIpType_Type(InetAddressType):
    """Custom type mgmdVlanQuerySrcIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdVlanQuerySrcIpType_Type.__name__ = "InetAddressType"
_MgmdVlanQuerySrcIpType_Object = MibTableColumn
mgmdVlanQuerySrcIpType = _MgmdVlanQuerySrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10, 1, 4),
    _MgmdVlanQuerySrcIpType_Type()
)
mgmdVlanQuerySrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanQuerySrcIpType.setStatus("current")


class _MgmdVlanQuerySrcIp_Type(InetAddress):
    """Custom type mgmdVlanQuerySrcIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdVlanQuerySrcIp_Type.__name__ = "InetAddress"
_MgmdVlanQuerySrcIp_Object = MibTableColumn
mgmdVlanQuerySrcIp = _MgmdVlanQuerySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 10, 1, 5),
    _MgmdVlanQuerySrcIp_Type()
)
mgmdVlanQuerySrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdVlanQuerySrcIp.setStatus("current")
_MgmdCounterPortTable_Object = MibTable
mgmdCounterPortTable = _MgmdCounterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 11)
)
if mibBuilder.loadTexts:
    mgmdCounterPortTable.setStatus("current")
_MgmdCounterPortEntry_Object = MibTableRow
mgmdCounterPortEntry = _MgmdCounterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 11, 1)
)
mgmdCounterPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mgmdCounterPortEntry.setStatus("current")
_MgmdCounterPortReport_Type = Counter32
_MgmdCounterPortReport_Object = MibTableColumn
mgmdCounterPortReport = _MgmdCounterPortReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 11, 1, 1),
    _MgmdCounterPortReport_Type()
)
mgmdCounterPortReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortReport.setStatus("current")
_MgmdCounterPortLeave_Type = Counter32
_MgmdCounterPortLeave_Object = MibTableColumn
mgmdCounterPortLeave = _MgmdCounterPortLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 11, 1, 2),
    _MgmdCounterPortLeave_Type()
)
mgmdCounterPortLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortLeave.setStatus("current")
_MgmdCounterPortActiveGroup_Type = Integer32
_MgmdCounterPortActiveGroup_Object = MibTableColumn
mgmdCounterPortActiveGroup = _MgmdCounterPortActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 11, 1, 3),
    _MgmdCounterPortActiveGroup_Type()
)
mgmdCounterPortActiveGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortActiveGroup.setStatus("current")
_MgmdCounterPortQuery_Type = Counter32
_MgmdCounterPortQuery_Object = MibTableColumn
mgmdCounterPortQuery = _MgmdCounterPortQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 11, 1, 4),
    _MgmdCounterPortQuery_Type()
)
mgmdCounterPortQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterPortQuery.setStatus("current")
_MgmdCounterVlanTable_Object = MibTable
mgmdCounterVlanTable = _MgmdCounterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 12)
)
if mibBuilder.loadTexts:
    mgmdCounterVlanTable.setStatus("current")
_MgmdCounterVlanEntry_Object = MibTableRow
mgmdCounterVlanEntry = _MgmdCounterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 12, 1)
)
mgmdCounterVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    mgmdCounterVlanEntry.setStatus("current")
_MgmdCounterVlanReport_Type = Counter32
_MgmdCounterVlanReport_Object = MibTableColumn
mgmdCounterVlanReport = _MgmdCounterVlanReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 12, 1, 1),
    _MgmdCounterVlanReport_Type()
)
mgmdCounterVlanReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanReport.setStatus("current")
_MgmdCounterVlanLeave_Type = Counter32
_MgmdCounterVlanLeave_Object = MibTableColumn
mgmdCounterVlanLeave = _MgmdCounterVlanLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 12, 1, 2),
    _MgmdCounterVlanLeave_Type()
)
mgmdCounterVlanLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanLeave.setStatus("current")
_MgmdCounterVlanActiveGroup_Type = Integer32
_MgmdCounterVlanActiveGroup_Object = MibTableColumn
mgmdCounterVlanActiveGroup = _MgmdCounterVlanActiveGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 12, 1, 3),
    _MgmdCounterVlanActiveGroup_Type()
)
mgmdCounterVlanActiveGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanActiveGroup.setStatus("current")
_MgmdCounterVlanQuery_Type = Counter32
_MgmdCounterVlanQuery_Object = MibTableColumn
mgmdCounterVlanQuery = _MgmdCounterVlanQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 12, 1, 4),
    _MgmdCounterVlanQuery_Type()
)
mgmdCounterVlanQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCounterVlanQuery.setStatus("current")
_MgmdCurrentGroupStatusTable_Object = MibTable
mgmdCurrentGroupStatusTable = _MgmdCurrentGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 13)
)
if mibBuilder.loadTexts:
    mgmdCurrentGroupStatusTable.setStatus("current")
_MgmdCurrentGroupStatusEntry_Object = MibTableRow
mgmdCurrentGroupStatusEntry = _MgmdCurrentGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 13, 1)
)
mgmdCurrentGroupStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusGroupAddressType"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusGroupAddress"),
)
if mibBuilder.loadTexts:
    mgmdCurrentGroupStatusEntry.setStatus("current")
_MgmdCurrentNumberOfActivePort_Type = Integer32
_MgmdCurrentNumberOfActivePort_Object = MibTableColumn
mgmdCurrentNumberOfActivePort = _MgmdCurrentNumberOfActivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 13, 1, 1),
    _MgmdCurrentNumberOfActivePort_Type()
)
mgmdCurrentNumberOfActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdCurrentNumberOfActivePort.setStatus("current")
_MgmdClientSrcIpTable_Object = MibTable
mgmdClientSrcIpTable = _MgmdClientSrcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 14)
)
if mibBuilder.loadTexts:
    mgmdClientSrcIpTable.setStatus("current")
_MgmdClientSrcIpEntry_Object = MibTableRow
mgmdClientSrcIpEntry = _MgmdClientSrcIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 14, 1)
)
mgmdClientSrcIpEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdClientSrcIpAddressType"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdClientSrcIpIndex"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusGroupAddress"),
)
if mibBuilder.loadTexts:
    mgmdClientSrcIpEntry.setStatus("current")
_MgmdClientSrcIpIndex_Type = Integer32
_MgmdClientSrcIpIndex_Object = MibTableColumn
mgmdClientSrcIpIndex = _MgmdClientSrcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 14, 1, 1),
    _MgmdClientSrcIpIndex_Type()
)
mgmdClientSrcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdClientSrcIpIndex.setStatus("current")


class _MgmdClientSrcIpAddressType_Type(InetAddressType):
    """Custom type mgmdClientSrcIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdClientSrcIpAddressType_Type.__name__ = "InetAddressType"
_MgmdClientSrcIpAddressType_Object = MibTableColumn
mgmdClientSrcIpAddressType = _MgmdClientSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 14, 1, 2),
    _MgmdClientSrcIpAddressType_Type()
)
mgmdClientSrcIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdClientSrcIpAddressType.setStatus("current")


class _MgmdClientSrcIpAddress_Type(InetAddress):
    """Custom type mgmdClientSrcIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdClientSrcIpAddress_Type.__name__ = "InetAddress"
_MgmdClientSrcIpAddress_Object = MibTableColumn
mgmdClientSrcIpAddress = _MgmdClientSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 14, 1, 3),
    _MgmdClientSrcIpAddress_Type()
)
mgmdClientSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdClientSrcIpAddress.setStatus("current")
_MgmdSrcListTable_Object = MibTable
mgmdSrcListTable = _MgmdSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 15)
)
if mibBuilder.loadTexts:
    mgmdSrcListTable.setStatus("current")
_MgmdSrcListEntry_Object = MibTableRow
mgmdSrcListEntry = _MgmdSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 15, 1)
)
mgmdSrcListEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdSrcListAddressType"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdStatusGroupAddress"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdSrcListAddress"),
)
if mibBuilder.loadTexts:
    mgmdSrcListEntry.setStatus("current")


class _MgmdSrcListAddressType_Type(InetAddressType):
    """Custom type mgmdSrcListAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_MgmdSrcListAddressType_Type.__name__ = "InetAddressType"
_MgmdSrcListAddressType_Object = MibTableColumn
mgmdSrcListAddressType = _MgmdSrcListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 15, 1, 1),
    _MgmdSrcListAddressType_Type()
)
mgmdSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdSrcListAddressType.setStatus("current")


class _MgmdSrcListAddress_Type(InetAddress):
    """Custom type mgmdSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_MgmdSrcListAddress_Type.__name__ = "InetAddress"
_MgmdSrcListAddress_Object = MibTableColumn
mgmdSrcListAddress = _MgmdSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 29, 15, 1, 2),
    _MgmdSrcListAddress_Type()
)
mgmdSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdSrcListAddress.setStatus("current")
_IgmpFilteringProfileSetup_ObjectIdentity = ObjectIdentity
igmpFilteringProfileSetup = _IgmpFilteringProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30)
)
_IgmpFilteringMaxNumberOfProfile_Type = Integer32
_IgmpFilteringMaxNumberOfProfile_Object = MibScalar
igmpFilteringMaxNumberOfProfile = _IgmpFilteringMaxNumberOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 1),
    _IgmpFilteringMaxNumberOfProfile_Type()
)
igmpFilteringMaxNumberOfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringMaxNumberOfProfile.setStatus("current")
_IgmpFilteringProfileTable_Object = MibTable
igmpFilteringProfileTable = _IgmpFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 2)
)
if mibBuilder.loadTexts:
    igmpFilteringProfileTable.setStatus("current")
_IgmpFilteringProfileEntry_Object = MibTableRow
igmpFilteringProfileEntry = _IgmpFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 2, 1)
)
igmpFilteringProfileEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "igmpFilteringProfileName"),
    (0, "ZYXEL-ves1608FE57-MIB", "igmpFilteringProfileStartAddress"),
    (0, "ZYXEL-ves1608FE57-MIB", "igmpFilteringProfileEndAddress"),
)
if mibBuilder.loadTexts:
    igmpFilteringProfileEntry.setStatus("current")
_IgmpFilteringProfileName_Type = DisplayString
_IgmpFilteringProfileName_Object = MibTableColumn
igmpFilteringProfileName = _IgmpFilteringProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 2, 1, 1),
    _IgmpFilteringProfileName_Type()
)
igmpFilteringProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileName.setStatus("current")
_IgmpFilteringProfileStartAddress_Type = IpAddress
_IgmpFilteringProfileStartAddress_Object = MibTableColumn
igmpFilteringProfileStartAddress = _IgmpFilteringProfileStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 2, 1, 2),
    _IgmpFilteringProfileStartAddress_Type()
)
igmpFilteringProfileStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileStartAddress.setStatus("current")
_IgmpFilteringProfileEndAddress_Type = IpAddress
_IgmpFilteringProfileEndAddress_Object = MibTableColumn
igmpFilteringProfileEndAddress = _IgmpFilteringProfileEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 2, 1, 3),
    _IgmpFilteringProfileEndAddress_Type()
)
igmpFilteringProfileEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileEndAddress.setStatus("current")
_IgmpFilteringProfileRowStatus_Type = RowStatus
_IgmpFilteringProfileRowStatus_Object = MibTableColumn
igmpFilteringProfileRowStatus = _IgmpFilteringProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 2, 1, 4),
    _IgmpFilteringProfileRowStatus_Type()
)
igmpFilteringProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilteringProfileRowStatus.setStatus("current")
_MgmdFilterProfileTable_Object = MibTable
mgmdFilterProfileTable = _MgmdFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3)
)
if mibBuilder.loadTexts:
    mgmdFilterProfileTable.setStatus("current")
_MgmdFilterProfileEntry_Object = MibTableRow
mgmdFilterProfileEntry = _MgmdFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3, 1)
)
mgmdFilterProfileEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdFilterProfileName"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdFilterProfileAddressType"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdFilterProfileStartAddress"),
    (0, "ZYXEL-ves1608FE57-MIB", "mgmdFilterProfileEndAddress"),
)
if mibBuilder.loadTexts:
    mgmdFilterProfileEntry.setStatus("current")
_MgmdFilterProfileName_Type = DisplayString
_MgmdFilterProfileName_Object = MibTableColumn
mgmdFilterProfileName = _MgmdFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3, 1, 1),
    _MgmdFilterProfileName_Type()
)
mgmdFilterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdFilterProfileName.setStatus("current")
_MgmdFilterProfileAddressType_Type = InetAddressType
_MgmdFilterProfileAddressType_Object = MibTableColumn
mgmdFilterProfileAddressType = _MgmdFilterProfileAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3, 1, 2),
    _MgmdFilterProfileAddressType_Type()
)
mgmdFilterProfileAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdFilterProfileAddressType.setStatus("current")
_MgmdFilterProfileStartAddress_Type = InetAddress
_MgmdFilterProfileStartAddress_Object = MibTableColumn
mgmdFilterProfileStartAddress = _MgmdFilterProfileStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3, 1, 3),
    _MgmdFilterProfileStartAddress_Type()
)
mgmdFilterProfileStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdFilterProfileStartAddress.setStatus("current")
_MgmdFilterProfileEndAddress_Type = InetAddress
_MgmdFilterProfileEndAddress_Object = MibTableColumn
mgmdFilterProfileEndAddress = _MgmdFilterProfileEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3, 1, 4),
    _MgmdFilterProfileEndAddress_Type()
)
mgmdFilterProfileEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdFilterProfileEndAddress.setStatus("current")
_MgmdFilterProfileRowStatus_Type = RowStatus
_MgmdFilterProfileRowStatus_Object = MibTableColumn
mgmdFilterProfileRowStatus = _MgmdFilterProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 30, 3, 1, 5),
    _MgmdFilterProfileRowStatus_Type()
)
mgmdFilterProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdFilterProfileRowStatus.setStatus("current")
_MvrSetup_ObjectIdentity = ObjectIdentity
mvrSetup = _MvrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31)
)
_MaxNumberOfMVR_Type = Integer32
_MaxNumberOfMVR_Object = MibScalar
maxNumberOfMVR = _MaxNumberOfMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 1),
    _MaxNumberOfMVR_Type()
)
maxNumberOfMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMVR.setStatus("current")
_MvrTable_Object = MibTable
mvrTable = _MvrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2)
)
if mibBuilder.loadTexts:
    mvrTable.setStatus("current")
_MvrEntry_Object = MibTableRow
mvrEntry = _MvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2, 1)
)
mvrEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mvrVlanID"),
)
if mibBuilder.loadTexts:
    mvrEntry.setStatus("current")
_MvrVlanID_Type = Integer32
_MvrVlanID_Object = MibTableColumn
mvrVlanID = _MvrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2, 1, 1),
    _MvrVlanID_Type()
)
mvrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanID.setStatus("current")
_MvrName_Type = DisplayString
_MvrName_Object = MibTableColumn
mvrName = _MvrName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2, 1, 2),
    _MvrName_Type()
)
mvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrName.setStatus("current")


class _MvrMode_Type(Integer32):
    """Custom type mvrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("compatible", 1))
    )


_MvrMode_Type.__name__ = "Integer32"
_MvrMode_Object = MibTableColumn
mvrMode = _MvrMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2, 1, 3),
    _MvrMode_Type()
)
mvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMode.setStatus("current")
_MvrRowStatus_Type = RowStatus
_MvrRowStatus_Object = MibTableColumn
mvrRowStatus = _MvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2, 1, 4),
    _MvrRowStatus_Type()
)
mvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrRowStatus.setStatus("current")
_Mvr8021pPriority_Type = Integer32
_Mvr8021pPriority_Object = MibTableColumn
mvr8021pPriority = _Mvr8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 2, 1, 5),
    _Mvr8021pPriority_Type()
)
mvr8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvr8021pPriority.setStatus("current")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 3)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("current")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 3, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mvrVlanID"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("current")


class _MvrPortRole_Type(Integer32):
    """Custom type mvrPortRole based on Integer32"""
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
          ("source-port", 2),
          ("receiver-port", 3))
    )


_MvrPortRole_Type.__name__ = "Integer32"
_MvrPortRole_Object = MibTableColumn
mvrPortRole = _MvrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 3, 1, 1),
    _MvrPortRole_Type()
)
mvrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortRole.setStatus("current")
_MvrPortTagging_Type = EnabledStatus
_MvrPortTagging_Object = MibTableColumn
mvrPortTagging = _MvrPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 3, 1, 2),
    _MvrPortTagging_Type()
)
mvrPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortTagging.setStatus("current")
_MaxNumberOfMvrGroup_Type = Integer32
_MaxNumberOfMvrGroup_Object = MibScalar
maxNumberOfMvrGroup = _MaxNumberOfMvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 4),
    _MaxNumberOfMvrGroup_Type()
)
maxNumberOfMvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMvrGroup.setStatus("current")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 5)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("current")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 5, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mvrVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "mvrGroupName"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("current")
_MvrGroupName_Type = DisplayString
_MvrGroupName_Object = MibTableColumn
mvrGroupName = _MvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 5, 1, 1),
    _MvrGroupName_Type()
)
mvrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupName.setStatus("current")
_MvrGroupStartAddress_Type = IpAddress
_MvrGroupStartAddress_Object = MibTableColumn
mvrGroupStartAddress = _MvrGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 5, 1, 2),
    _MvrGroupStartAddress_Type()
)
mvrGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStartAddress.setStatus("current")
_MvrGroupEndAddress_Type = IpAddress
_MvrGroupEndAddress_Object = MibTableColumn
mvrGroupEndAddress = _MvrGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 5, 1, 3),
    _MvrGroupEndAddress_Type()
)
mvrGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupEndAddress.setStatus("current")
_MvrGroupRowStatus_Type = RowStatus
_MvrGroupRowStatus_Object = MibTableColumn
mvrGroupRowStatus = _MvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 5, 1, 4),
    _MvrGroupRowStatus_Type()
)
mvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupRowStatus.setStatus("current")


class _MvrBehavior_Type(Integer32):
    """Custom type mvrBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmp-snooping", 1),
          ("igmp-proxy", 2))
    )


_MvrBehavior_Type.__name__ = "Integer32"
_MvrBehavior_Object = MibScalar
mvrBehavior = _MvrBehavior_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 6),
    _MvrBehavior_Type()
)
mvrBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrBehavior.setStatus("current")
_MvrMgmdGroupTable_Object = MibTable
mvrMgmdGroupTable = _MvrMgmdGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7)
)
if mibBuilder.loadTexts:
    mvrMgmdGroupTable.setStatus("current")
_MvrMgmdGroupEntry_Object = MibTableRow
mvrMgmdGroupEntry = _MvrMgmdGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7, 1)
)
mvrMgmdGroupEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mvrVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "mvrMgmdGroupName"),
)
if mibBuilder.loadTexts:
    mvrMgmdGroupEntry.setStatus("current")
_MvrMgmdGroupName_Type = DisplayString
_MvrMgmdGroupName_Object = MibTableColumn
mvrMgmdGroupName = _MvrMgmdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7, 1, 1),
    _MvrMgmdGroupName_Type()
)
mvrMgmdGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMgmdGroupName.setStatus("current")
_MvrMgmdGroupAddressType_Type = InetAddressType
_MvrMgmdGroupAddressType_Object = MibTableColumn
mvrMgmdGroupAddressType = _MvrMgmdGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7, 1, 2),
    _MvrMgmdGroupAddressType_Type()
)
mvrMgmdGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMgmdGroupAddressType.setStatus("current")
_MvrMgmdGroupStartAddress_Type = InetAddress
_MvrMgmdGroupStartAddress_Object = MibTableColumn
mvrMgmdGroupStartAddress = _MvrMgmdGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7, 1, 3),
    _MvrMgmdGroupStartAddress_Type()
)
mvrMgmdGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMgmdGroupStartAddress.setStatus("current")
_MvrMgmdGroupEndAddress_Type = InetAddress
_MvrMgmdGroupEndAddress_Object = MibTableColumn
mvrMgmdGroupEndAddress = _MvrMgmdGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7, 1, 4),
    _MvrMgmdGroupEndAddress_Type()
)
mvrMgmdGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMgmdGroupEndAddress.setStatus("current")
_MvrMgmdGroupRowStatus_Type = RowStatus
_MvrMgmdGroupRowStatus_Object = MibTableColumn
mvrMgmdGroupRowStatus = _MvrMgmdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 31, 7, 1, 5),
    _MvrMgmdGroupRowStatus_Type()
)
mvrMgmdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrMgmdGroupRowStatus.setStatus("current")
_SysLogSetup_ObjectIdentity = ObjectIdentity
sysLogSetup = _SysLogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33)
)
_SysLogState_Type = EnabledStatus
_SysLogState_Object = MibScalar
sysLogState = _SysLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 1),
    _SysLogState_Type()
)
sysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogState.setStatus("current")
_SysLogTypeTable_Object = MibTable
sysLogTypeTable = _SysLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 2)
)
if mibBuilder.loadTexts:
    sysLogTypeTable.setStatus("current")
_SysLogTypeEntry_Object = MibTableRow
sysLogTypeEntry = _SysLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 2, 1)
)
sysLogTypeEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "sysLogTypeIndex"),
)
if mibBuilder.loadTexts:
    sysLogTypeEntry.setStatus("current")
_SysLogTypeIndex_Type = Integer32
_SysLogTypeIndex_Object = MibTableColumn
sysLogTypeIndex = _SysLogTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 2, 1, 1),
    _SysLogTypeIndex_Type()
)
sysLogTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogTypeIndex.setStatus("current")
_SysLogTypeName_Type = DisplayString
_SysLogTypeName_Object = MibTableColumn
sysLogTypeName = _SysLogTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 2, 1, 2),
    _SysLogTypeName_Type()
)
sysLogTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogTypeName.setStatus("current")
_SysLogTypeState_Type = EnabledStatus
_SysLogTypeState_Object = MibTableColumn
sysLogTypeState = _SysLogTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 2, 1, 3),
    _SysLogTypeState_Type()
)
sysLogTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeState.setStatus("current")


class _SysLogTypeFacility_Type(Integer32):
    """Custom type sysLogTypeFacility based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("local-user0", 0),
          ("local-user1", 1),
          ("local-user2", 2),
          ("local-user3", 3),
          ("local-user4", 4),
          ("local-user5", 5),
          ("local-user6", 6),
          ("local-user7", 7))
    )


_SysLogTypeFacility_Type.__name__ = "Integer32"
_SysLogTypeFacility_Object = MibTableColumn
sysLogTypeFacility = _SysLogTypeFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 2, 1, 4),
    _SysLogTypeFacility_Type()
)
sysLogTypeFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeFacility.setStatus("current")
_SysLogServerTable_Object = MibTable
sysLogServerTable = _SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 3)
)
if mibBuilder.loadTexts:
    sysLogServerTable.setStatus("current")
_SysLogServerEntry_Object = MibTableRow
sysLogServerEntry = _SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 3, 1)
)
sysLogServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "sysLogServerAddress"),
)
if mibBuilder.loadTexts:
    sysLogServerEntry.setStatus("current")
_SysLogServerAddress_Type = IpAddress
_SysLogServerAddress_Object = MibTableColumn
sysLogServerAddress = _SysLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 3, 1, 1),
    _SysLogServerAddress_Type()
)
sysLogServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogServerAddress.setStatus("current")


class _SysLogServerLogLevel_Type(Integer32):
    """Custom type sysLogServerLogLevel based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level0-1", 1),
          ("level0-2", 2),
          ("level0-3", 3),
          ("level0-4", 4),
          ("level0-5", 5),
          ("level0-6", 6),
          ("level0-7", 7))
    )


_SysLogServerLogLevel_Type.__name__ = "Integer32"
_SysLogServerLogLevel_Object = MibTableColumn
sysLogServerLogLevel = _SysLogServerLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 3, 1, 2),
    _SysLogServerLogLevel_Type()
)
sysLogServerLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerLogLevel.setStatus("current")
_SysLogServerRowStatus_Type = RowStatus
_SysLogServerRowStatus_Object = MibTableColumn
sysLogServerRowStatus = _SysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 3, 1, 3),
    _SysLogServerRowStatus_Type()
)
sysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLogServerRowStatus.setStatus("current")
_SysLogServerInfoTable_Object = MibTable
sysLogServerInfoTable = _SysLogServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 4)
)
if mibBuilder.loadTexts:
    sysLogServerInfoTable.setStatus("current")
_SysLogServerInfoEntry_Object = MibTableRow
sysLogServerInfoEntry = _SysLogServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 4, 1)
)
sysLogServerInfoEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "sysLogServerInfoIpAddrType"),
    (0, "ZYXEL-ves1608FE57-MIB", "sysLogServerInfoIpAddr"),
)
if mibBuilder.loadTexts:
    sysLogServerInfoEntry.setStatus("current")


class _SysLogServerInfoIpAddrType_Type(InetAddressType):
    """Custom type sysLogServerInfoIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SysLogServerInfoIpAddrType_Type.__name__ = "InetAddressType"
_SysLogServerInfoIpAddrType_Object = MibTableColumn
sysLogServerInfoIpAddrType = _SysLogServerInfoIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 4, 1, 1),
    _SysLogServerInfoIpAddrType_Type()
)
sysLogServerInfoIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogServerInfoIpAddrType.setStatus("current")
_SysLogServerInfoIpAddr_Type = InetAddress
_SysLogServerInfoIpAddr_Object = MibTableColumn
sysLogServerInfoIpAddr = _SysLogServerInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 4, 1, 2),
    _SysLogServerInfoIpAddr_Type()
)
sysLogServerInfoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogServerInfoIpAddr.setStatus("current")


class _SysLogServerInfoLogLevel_Type(Integer32):
    """Custom type sysLogServerInfoLogLevel based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level0-1", 1),
          ("level0-2", 2),
          ("level0-3", 3),
          ("level0-4", 4),
          ("level0-5", 5),
          ("level0-6", 6),
          ("level0-7", 7))
    )


_SysLogServerInfoLogLevel_Type.__name__ = "Integer32"
_SysLogServerInfoLogLevel_Object = MibTableColumn
sysLogServerInfoLogLevel = _SysLogServerInfoLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 4, 1, 3),
    _SysLogServerInfoLogLevel_Type()
)
sysLogServerInfoLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerInfoLogLevel.setStatus("current")
_SysLogServerInfoRowStatus_Type = RowStatus
_SysLogServerInfoRowStatus_Object = MibTableColumn
sysLogServerInfoRowStatus = _SysLogServerInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 33, 4, 1, 4),
    _SysLogServerInfoRowStatus_Type()
)
sysLogServerInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLogServerInfoRowStatus.setStatus("current")
_DiffservSetup_ObjectIdentity = ObjectIdentity
diffservSetup = _DiffservSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34)
)
_DiffservState_Type = EnabledStatus
_DiffservState_Object = MibScalar
diffservState = _DiffservState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 1),
    _DiffservState_Type()
)
diffservState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservState.setStatus("current")
_DiffservMapTable_Object = MibTable
diffservMapTable = _DiffservMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 2)
)
if mibBuilder.loadTexts:
    diffservMapTable.setStatus("current")
_DiffservMapEntry_Object = MibTableRow
diffservMapEntry = _DiffservMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 2, 1)
)
diffservMapEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "diffservMapDscp"),
)
if mibBuilder.loadTexts:
    diffservMapEntry.setStatus("current")
_DiffservMapDscp_Type = Integer32
_DiffservMapDscp_Object = MibTableColumn
diffservMapDscp = _DiffservMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 2, 1, 1),
    _DiffservMapDscp_Type()
)
diffservMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffservMapDscp.setStatus("current")
_DiffservMapPriority_Type = Integer32
_DiffservMapPriority_Object = MibTableColumn
diffservMapPriority = _DiffservMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 2, 1, 2),
    _DiffservMapPriority_Type()
)
diffservMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservMapPriority.setStatus("current")
_DiffservPortTable_Object = MibTable
diffservPortTable = _DiffservPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 3)
)
if mibBuilder.loadTexts:
    diffservPortTable.setStatus("current")
_DiffservPortEntry_Object = MibTableRow
diffservPortEntry = _DiffservPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 3, 1)
)
diffservPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    diffservPortEntry.setStatus("current")
_DiffservPortState_Type = EnabledStatus
_DiffservPortState_Object = MibTableColumn
diffservPortState = _DiffservPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 34, 3, 1, 1),
    _DiffservPortState_Type()
)
diffservPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservPortState.setStatus("current")
_VturInfo_ObjectIdentity = ObjectIdentity
vturInfo = _VturInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 37)
)
_VturInfoTable_Object = MibTable
vturInfoTable = _VturInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 37, 1)
)
if mibBuilder.loadTexts:
    vturInfoTable.setStatus("current")
_VturInfoEntry_Object = MibTableRow
vturInfoEntry = _VturInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 37, 1, 1)
)
vturInfoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vturInfoEntry.setStatus("current")
_VturName_Type = DisplayString
_VturName_Object = MibTableColumn
vturName = _VturName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 37, 1, 1, 1),
    _VturName_Type()
)
vturName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vturName.setStatus("current")
_VturSysVersion_Type = DisplayString
_VturSysVersion_Object = MibTableColumn
vturSysVersion = _VturSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 37, 1, 1, 2),
    _VturSysVersion_Type()
)
vturSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vturSysVersion.setStatus("current")
_VturModemCodeVersion_Type = DisplayString
_VturModemCodeVersion_Object = MibTableColumn
vturModemCodeVersion = _VturModemCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 37, 1, 1, 3),
    _VturModemCodeVersion_Type()
)
vturModemCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vturModemCodeVersion.setStatus("current")
_ProtoBasedVlanSetup_ObjectIdentity = ObjectIdentity
protoBasedVlanSetup = _ProtoBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38)
)
_ProtoBasedVlanTable_Object = MibTable
protoBasedVlanTable = _ProtoBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1)
)
if mibBuilder.loadTexts:
    protoBasedVlanTable.setStatus("current")
_ProtoBasedVlanEntry_Object = MibTableRow
protoBasedVlanEntry = _ProtoBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1)
)
protoBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "protoBasedVlanPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "protoBasedVlanPacketType"),
    (0, "ZYXEL-ves1608FE57-MIB", "protoBasedVlanEtherType"),
)
if mibBuilder.loadTexts:
    protoBasedVlanEntry.setStatus("current")
_ProtoBasedVlanPort_Type = Integer32
_ProtoBasedVlanPort_Object = MibTableColumn
protoBasedVlanPort = _ProtoBasedVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 1),
    _ProtoBasedVlanPort_Type()
)
protoBasedVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanPort.setStatus("current")


class _ProtoBasedVlanPacketType_Type(Integer32):
    """Custom type protoBasedVlanPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etherII", 1),
          ("snap", 2),
          ("llc", 3))
    )


_ProtoBasedVlanPacketType_Type.__name__ = "Integer32"
_ProtoBasedVlanPacketType_Object = MibTableColumn
protoBasedVlanPacketType = _ProtoBasedVlanPacketType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 2),
    _ProtoBasedVlanPacketType_Type()
)
protoBasedVlanPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanPacketType.setStatus("current")
_ProtoBasedVlanEtherType_Type = Integer32
_ProtoBasedVlanEtherType_Object = MibTableColumn
protoBasedVlanEtherType = _ProtoBasedVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 3),
    _ProtoBasedVlanEtherType_Type()
)
protoBasedVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanEtherType.setStatus("current")


class _ProtoBasedVlanName_Type(DisplayString):
    """Custom type protoBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtoBasedVlanName_Type.__name__ = "DisplayString"
_ProtoBasedVlanName_Object = MibTableColumn
protoBasedVlanName = _ProtoBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 4),
    _ProtoBasedVlanName_Type()
)
protoBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanName.setStatus("current")


class _ProtoBasedVlanVid_Type(Integer32):
    """Custom type protoBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ProtoBasedVlanVid_Type.__name__ = "Integer32"
_ProtoBasedVlanVid_Object = MibTableColumn
protoBasedVlanVid = _ProtoBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 5),
    _ProtoBasedVlanVid_Type()
)
protoBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanVid.setStatus("current")


class _ProtoBasedVlanPriority_Type(Integer32):
    """Custom type protoBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ProtoBasedVlanPriority_Type.__name__ = "Integer32"
_ProtoBasedVlanPriority_Object = MibTableColumn
protoBasedVlanPriority = _ProtoBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 6),
    _ProtoBasedVlanPriority_Type()
)
protoBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanPriority.setStatus("current")
_ProtoBasedVlanState_Type = RowStatus
_ProtoBasedVlanState_Object = MibTableColumn
protoBasedVlanState = _ProtoBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 38, 1, 1, 7),
    _ProtoBasedVlanState_Type()
)
protoBasedVlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protoBasedVlanState.setStatus("current")
_ClassifierSetup_ObjectIdentity = ObjectIdentity
classifierSetup = _ClassifierSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39)
)
_ClassifierRuleTable_Object = MibTable
classifierRuleTable = _ClassifierRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1)
)
if mibBuilder.loadTexts:
    classifierRuleTable.setStatus("current")
_ClassifierRuleEntry_Object = MibTableRow
classifierRuleEntry = _ClassifierRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1)
)
classifierRuleEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "classifierName"),
)
if mibBuilder.loadTexts:
    classifierRuleEntry.setStatus("current")
_ClassifierName_Type = DisplayString
_ClassifierName_Object = MibTableColumn
classifierName = _ClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 1),
    _ClassifierName_Type()
)
classifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classifierName.setStatus("current")
_ClassifierEnable_Type = EnabledStatus
_ClassifierEnable_Object = MibTableColumn
classifierEnable = _ClassifierEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 2),
    _ClassifierEnable_Type()
)
classifierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierEnable.setStatus("current")


class _ClassifierPacketFormat_Type(Integer32):
    """Custom type classifierPacketFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ethernetII-untagged", 2),
          ("ethernetII-tagged", 3),
          ("ethernet802-3-untagged", 4),
          ("ethernet802-3-tagged", 5))
    )


_ClassifierPacketFormat_Type.__name__ = "Integer32"
_ClassifierPacketFormat_Object = MibTableColumn
classifierPacketFormat = _ClassifierPacketFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 3),
    _ClassifierPacketFormat_Type()
)
classifierPacketFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierPacketFormat.setStatus("current")
_ClassifierVlanId_Type = Integer32
_ClassifierVlanId_Object = MibTableColumn
classifierVlanId = _ClassifierVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 4),
    _ClassifierVlanId_Type()
)
classifierVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierVlanId.setStatus("current")
_Classifier8021pPriority_Type = Integer32
_Classifier8021pPriority_Object = MibTableColumn
classifier8021pPriority = _Classifier8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 5),
    _Classifier8021pPriority_Type()
)
classifier8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifier8021pPriority.setStatus("current")
_ClassifierEtherType_Type = Integer32
_ClassifierEtherType_Object = MibTableColumn
classifierEtherType = _ClassifierEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 6),
    _ClassifierEtherType_Type()
)
classifierEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierEtherType.setStatus("current")
_ClassifierSrcMAC_Type = MacAddress
_ClassifierSrcMAC_Object = MibTableColumn
classifierSrcMAC = _ClassifierSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 7),
    _ClassifierSrcMAC_Type()
)
classifierSrcMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcMAC.setStatus("current")
_ClassifierIncomingPort_Type = Integer32
_ClassifierIncomingPort_Object = MibTableColumn
classifierIncomingPort = _ClassifierIncomingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 8),
    _ClassifierIncomingPort_Type()
)
classifierIncomingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIncomingPort.setStatus("current")
_ClassifierDstMAC_Type = MacAddress
_ClassifierDstMAC_Object = MibTableColumn
classifierDstMAC = _ClassifierDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 9),
    _ClassifierDstMAC_Type()
)
classifierDstMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstMAC.setStatus("current")
_ClassifierDSCP_Type = Integer32
_ClassifierDSCP_Object = MibTableColumn
classifierDSCP = _ClassifierDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 10),
    _ClassifierDSCP_Type()
)
classifierDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDSCP.setStatus("current")
_ClassifierIpProtocol_Type = Integer32
_ClassifierIpProtocol_Object = MibTableColumn
classifierIpProtocol = _ClassifierIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 11),
    _ClassifierIpProtocol_Type()
)
classifierIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierIpProtocol.setStatus("current")
_ClassifierEstablishOnly_Type = EnabledStatus
_ClassifierEstablishOnly_Object = MibTableColumn
classifierEstablishOnly = _ClassifierEstablishOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 12),
    _ClassifierEstablishOnly_Type()
)
classifierEstablishOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierEstablishOnly.setStatus("current")
_ClassifierSrcIp_Type = IpAddress
_ClassifierSrcIp_Object = MibTableColumn
classifierSrcIp = _ClassifierSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 13),
    _ClassifierSrcIp_Type()
)
classifierSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIp.setStatus("current")
_ClassifierSrcIpMask_Type = Integer32
_ClassifierSrcIpMask_Object = MibTableColumn
classifierSrcIpMask = _ClassifierSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 14),
    _ClassifierSrcIpMask_Type()
)
classifierSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIpMask.setStatus("current")
_ClassifierSrcSocket_Type = Integer32
_ClassifierSrcSocket_Object = MibTableColumn
classifierSrcSocket = _ClassifierSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 15),
    _ClassifierSrcSocket_Type()
)
classifierSrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcSocket.setStatus("current")
_ClassifierDstIp_Type = IpAddress
_ClassifierDstIp_Object = MibTableColumn
classifierDstIp = _ClassifierDstIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 16),
    _ClassifierDstIp_Type()
)
classifierDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIp.setStatus("current")
_ClassifierDstIpMask_Type = Integer32
_ClassifierDstIpMask_Object = MibTableColumn
classifierDstIpMask = _ClassifierDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 17),
    _ClassifierDstIpMask_Type()
)
classifierDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIpMask.setStatus("current")
_ClassifierDstSocket_Type = Integer32
_ClassifierDstSocket_Object = MibTableColumn
classifierDstSocket = _ClassifierDstSocket_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 18),
    _ClassifierDstSocket_Type()
)
classifierDstSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstSocket.setStatus("current")
_ClassifierRowstatus_Type = RowStatus
_ClassifierRowstatus_Object = MibTableColumn
classifierRowstatus = _ClassifierRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 19),
    _ClassifierRowstatus_Type()
)
classifierRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierRowstatus.setStatus("current")
_ClassifierSrcIpv6_Type = Ipv6Address
_ClassifierSrcIpv6_Object = MibTableColumn
classifierSrcIpv6 = _ClassifierSrcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 20),
    _ClassifierSrcIpv6_Type()
)
classifierSrcIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIpv6.setStatus("current")
_ClassifierSrcIpv6Mask_Type = Integer32
_ClassifierSrcIpv6Mask_Object = MibTableColumn
classifierSrcIpv6Mask = _ClassifierSrcIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 21),
    _ClassifierSrcIpv6Mask_Type()
)
classifierSrcIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierSrcIpv6Mask.setStatus("current")
_ClassifierDstIpv6_Type = Ipv6Address
_ClassifierDstIpv6_Object = MibTableColumn
classifierDstIpv6 = _ClassifierDstIpv6_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 22),
    _ClassifierDstIpv6_Type()
)
classifierDstIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIpv6.setStatus("current")
_ClassifierDstIpv6Mask_Type = Integer32
_ClassifierDstIpv6Mask_Object = MibTableColumn
classifierDstIpv6Mask = _ClassifierDstIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 1, 1, 23),
    _ClassifierDstIpv6Mask_Type()
)
classifierDstIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierDstIpv6Mask.setStatus("current")
_ClassifierRuleSet_Type = DisplayString
_ClassifierRuleSet_Object = MibScalar
classifierRuleSet = _ClassifierRuleSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 39, 2),
    _ClassifierRuleSet_Type()
)
classifierRuleSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classifierRuleSet.setStatus("current")
_PolicySetup_ObjectIdentity = ObjectIdentity
policySetup = _PolicySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40)
)
_PolicyTable_Object = MibTable
policyTable = _PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1)
)
if mibBuilder.loadTexts:
    policyTable.setStatus("current")
_PolicyEntry_Object = MibTableRow
policyEntry = _PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1)
)
policyEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "policyName"),
)
if mibBuilder.loadTexts:
    policyEntry.setStatus("current")
_PolicyName_Type = DisplayString
_PolicyName_Object = MibTableColumn
policyName = _PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 1),
    _PolicyName_Type()
)
policyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyName.setStatus("current")
_PolicyEnable_Type = EnabledStatus
_PolicyEnable_Object = MibTableColumn
policyEnable = _PolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 2),
    _PolicyEnable_Type()
)
policyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyEnable.setStatus("current")
_PolicyClassifier_Type = DisplayString
_PolicyClassifier_Object = MibTableColumn
policyClassifier = _PolicyClassifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 3),
    _PolicyClassifier_Type()
)
policyClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyClassifier.setStatus("current")
_PolicyVlanId_Type = Integer32
_PolicyVlanId_Object = MibTableColumn
policyVlanId = _PolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 4),
    _PolicyVlanId_Type()
)
policyVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyVlanId.setStatus("current")
_PolicyEgressPort_Type = Integer32
_PolicyEgressPort_Object = MibTableColumn
policyEgressPort = _PolicyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 5),
    _PolicyEgressPort_Type()
)
policyEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyEgressPort.setStatus("current")


class _PolicyOutPktFormat_Type(Integer32):
    """Custom type policyOutPktFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_PolicyOutPktFormat_Type.__name__ = "Integer32"
_PolicyOutPktFormat_Object = MibTableColumn
policyOutPktFormat = _PolicyOutPktFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 6),
    _PolicyOutPktFormat_Type()
)
policyOutPktFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyOutPktFormat.setStatus("current")
_Policy8021pPriority_Type = Integer32
_Policy8021pPriority_Object = MibTableColumn
policy8021pPriority = _Policy8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 7),
    _Policy8021pPriority_Type()
)
policy8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policy8021pPriority.setStatus("current")
_PolicyDSCP_Type = Integer32
_PolicyDSCP_Object = MibTableColumn
policyDSCP = _PolicyDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 8),
    _PolicyDSCP_Type()
)
policyDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyDSCP.setStatus("current")
_PolicyTOS_Type = Integer32
_PolicyTOS_Object = MibTableColumn
policyTOS = _PolicyTOS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 9),
    _PolicyTOS_Type()
)
policyTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyTOS.setStatus("current")
_PolicyBandwidth_Type = Integer32
_PolicyBandwidth_Object = MibTableColumn
policyBandwidth = _PolicyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 10),
    _PolicyBandwidth_Type()
)
policyBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyBandwidth.setStatus("current")
_PolicyOutOfProfileDSCP_Type = Integer32
_PolicyOutOfProfileDSCP_Object = MibTableColumn
policyOutOfProfileDSCP = _PolicyOutOfProfileDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 11),
    _PolicyOutOfProfileDSCP_Type()
)
policyOutOfProfileDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyOutOfProfileDSCP.setStatus("current")


class _PolicyForwardingAction_Type(Integer32):
    """Custom type policyForwardingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-change", 1),
          ("discard-the-packet", 2),
          ("do-not-drop-the-matching-frame-previously-marked-for-dopping", 3))
    )


_PolicyForwardingAction_Type.__name__ = "Integer32"
_PolicyForwardingAction_Object = MibTableColumn
policyForwardingAction = _PolicyForwardingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 12),
    _PolicyForwardingAction_Type()
)
policyForwardingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyForwardingAction.setStatus("current")


class _PolicyPriorityAction_Type(Integer32):
    """Custom type policyPriorityAction based on Integer32"""
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
        *(("no-change", 1),
          ("set-the-packets-802-1-priority", 2),
          ("send-the-packet-to-priority-queue", 3),
          ("replace-the-802-1-priority-field-with-the-IP-TOS-value", 4))
    )


_PolicyPriorityAction_Type.__name__ = "Integer32"
_PolicyPriorityAction_Object = MibTableColumn
policyPriorityAction = _PolicyPriorityAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 13),
    _PolicyPriorityAction_Type()
)
policyPriorityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPriorityAction.setStatus("current")


class _PolicyDiffServAction_Type(Integer32):
    """Custom type policyDiffServAction based on Integer32"""
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
        *(("no-change", 1),
          ("set-the-packets-TOS-field", 2),
          ("replace-the-IP-TOS-field-with-the-802-1-priority-value", 3),
          ("set-the-Diffserv-Codepoint-field-in-the-frame", 4))
    )


_PolicyDiffServAction_Type.__name__ = "Integer32"
_PolicyDiffServAction_Object = MibTableColumn
policyDiffServAction = _PolicyDiffServAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 14),
    _PolicyDiffServAction_Type()
)
policyDiffServAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyDiffServAction.setStatus("current")


class _PolicyOutgoingAction_Type(Bits):
    """Custom type policyOutgoingAction based on Bits"""
    namedValues = NamedValues(
        *(("send-the-packet-to-the-mirror-port", 1),
          ("send-the-packet-to-the-egress-port", 2),
          ("send-the-matching-frames-to-the-egress-port", 3),
          ("set-the-packets-VLAN-ID", 4))
    )

_PolicyOutgoingAction_Type.__name__ = "Bits"
_PolicyOutgoingAction_Object = MibTableColumn
policyOutgoingAction = _PolicyOutgoingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 15),
    _PolicyOutgoingAction_Type()
)
policyOutgoingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyOutgoingAction.setStatus("current")
_PolicyMeteringEnable_Type = Integer32
_PolicyMeteringEnable_Object = MibTableColumn
policyMeteringEnable = _PolicyMeteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 16),
    _PolicyMeteringEnable_Type()
)
policyMeteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyMeteringEnable.setStatus("current")


class _PolicyOutOfProfileAction_Type(Bits):
    """Custom type policyOutOfProfileAction based on Bits"""
    namedValues = NamedValues(
        *(("drop-the-packet", 1),
          ("change-the-DSCP-value", 2),
          ("set-Out-Drop-Precedence", 3),
          ("do-not-drop-the-matching-frame-previously-marked-for-dropping", 4))
    )

_PolicyOutOfProfileAction_Type.__name__ = "Bits"
_PolicyOutOfProfileAction_Object = MibTableColumn
policyOutOfProfileAction = _PolicyOutOfProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 17),
    _PolicyOutOfProfileAction_Type()
)
policyOutOfProfileAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyOutOfProfileAction.setStatus("current")
_PolicyRowstatus_Type = RowStatus
_PolicyRowstatus_Object = MibTableColumn
policyRowstatus = _PolicyRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 1, 1, 18),
    _PolicyRowstatus_Type()
)
policyRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyRowstatus.setStatus("current")
_PolicyRuleSet_Type = DisplayString
_PolicyRuleSet_Object = MibScalar
policyRuleSet = _PolicyRuleSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 40, 2),
    _PolicyRuleSet_Type()
)
policyRuleSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyRuleSet.setStatus("current")
_SwitchCounterStatus_ObjectIdentity = ObjectIdentity
switchCounterStatus = _SwitchCounterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42)
)
_VlanCounterTable_Object = MibTable
vlanCounterTable = _VlanCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 1)
)
if mibBuilder.loadTexts:
    vlanCounterTable.setStatus("current")
_VlanCounterEntry_Object = MibTableRow
vlanCounterEntry = _VlanCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 1, 1)
)
vlanCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanCounterEntry.setStatus("current")
_VlanCounterTxPkts_Type = Counter32
_VlanCounterTxPkts_Object = MibTableColumn
vlanCounterTxPkts = _VlanCounterTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 1, 1, 1),
    _VlanCounterTxPkts_Type()
)
vlanCounterTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCounterTxPkts.setStatus("current")
_VlanCounterRxPkts_Type = Counter32
_VlanCounterRxPkts_Object = MibTableColumn
vlanCounterRxPkts = _VlanCounterRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 1, 1, 2),
    _VlanCounterRxPkts_Type()
)
vlanCounterRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCounterRxPkts.setStatus("current")
_SwitchCounterTable_Object = MibTable
switchCounterTable = _SwitchCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 2)
)
if mibBuilder.loadTexts:
    switchCounterTable.setStatus("current")
_SwitchCounterEntry_Object = MibTableRow
switchCounterEntry = _SwitchCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 2, 1)
)
switchCounterEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    switchCounterEntry.setStatus("current")
_SwitchUnknownUnicastCounter_Type = Counter32
_SwitchUnknownUnicastCounter_Object = MibTableColumn
switchUnknownUnicastCounter = _SwitchUnknownUnicastCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 2, 1, 1),
    _SwitchUnknownUnicastCounter_Type()
)
switchUnknownUnicastCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchUnknownUnicastCounter.setStatus("current")
_VlanCounterResetTable_Object = MibTable
vlanCounterResetTable = _VlanCounterResetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 3)
)
if mibBuilder.loadTexts:
    vlanCounterResetTable.setStatus("current")
_VlanCounterResetEntry_Object = MibTableRow
vlanCounterResetEntry = _VlanCounterResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 3, 1)
)
vlanCounterResetEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanCounterResetEntry.setStatus("current")


class _VlanCounterReset_Type(Integer32):
    """Custom type vlanCounterReset based on Integer32"""
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


_VlanCounterReset_Type.__name__ = "Integer32"
_VlanCounterReset_Object = MibTableColumn
vlanCounterReset = _VlanCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 3, 1, 1),
    _VlanCounterReset_Type()
)
vlanCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCounterReset.setStatus("current")
_VlanCounterSwitchSetup_ObjectIdentity = ObjectIdentity
vlanCounterSwitchSetup = _VlanCounterSwitchSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 4)
)


class _VlanCounterSwitch_Type(Integer32):
    """Custom type vlanCounterSwitch based on Integer32"""
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


_VlanCounterSwitch_Type.__name__ = "Integer32"
_VlanCounterSwitch_Object = MibScalar
vlanCounterSwitch = _VlanCounterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 4, 1),
    _VlanCounterSwitch_Type()
)
vlanCounterSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCounterSwitch.setStatus("current")
_VlanCounterVlan_Type = Integer32
_VlanCounterVlan_Object = MibScalar
vlanCounterVlan = _VlanCounterVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 4, 2),
    _VlanCounterVlan_Type()
)
vlanCounterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCounterVlan.setStatus("current")
_VlanCounterPort_Type = Integer32
_VlanCounterPort_Object = MibScalar
vlanCounterPort = _VlanCounterPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 4, 3),
    _VlanCounterPort_Type()
)
vlanCounterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCounterPort.setStatus("current")


class _VlanCounterDirection_Type(Integer32):
    """Custom type vlanCounterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2))
    )


_VlanCounterDirection_Type.__name__ = "Integer32"
_VlanCounterDirection_Object = MibScalar
vlanCounterDirection = _VlanCounterDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 42, 4, 4),
    _VlanCounterDirection_Type()
)
vlanCounterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanCounterDirection.setStatus("current")
_RateLimitProfilePortSetup_ObjectIdentity = ObjectIdentity
rateLimitProfilePortSetup = _RateLimitProfilePortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43)
)
_RateLimitProfilePortTable_Object = MibTable
rateLimitProfilePortTable = _RateLimitProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43, 1)
)
if mibBuilder.loadTexts:
    rateLimitProfilePortTable.setStatus("current")
_RateLimitProfilePortEntry_Object = MibTableRow
rateLimitProfilePortEntry = _RateLimitProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43, 1, 1)
)
rateLimitProfilePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateLimitProfilePortEntry.setStatus("current")
_RateLimitPortProfile_Type = DisplayString
_RateLimitPortProfile_Object = MibTableColumn
rateLimitPortProfile = _RateLimitPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43, 1, 1, 1),
    _RateLimitPortProfile_Type()
)
rateLimitPortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortProfile.setStatus("current")
_PerQueueProfilePortTable_Object = MibTable
perQueueProfilePortTable = _PerQueueProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43, 2)
)
if mibBuilder.loadTexts:
    perQueueProfilePortTable.setStatus("current")
_PerQueueProfilePortEntry_Object = MibTableRow
perQueueProfilePortEntry = _PerQueueProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43, 2, 1)
)
perQueueProfilePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    perQueueProfilePortEntry.setStatus("current")
_PerQueuePortProfile_Type = DisplayString
_PerQueuePortProfile_Object = MibTableColumn
perQueuePortProfile = _PerQueuePortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 43, 2, 1, 1),
    _PerQueuePortProfile_Type()
)
perQueuePortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueuePortProfile.setStatus("current")
_RateLimitProfileSetup_ObjectIdentity = ObjectIdentity
rateLimitProfileSetup = _RateLimitProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44)
)
_RateLimitMaxNumberOfProfile_Type = Integer32
_RateLimitMaxNumberOfProfile_Object = MibScalar
rateLimitMaxNumberOfProfile = _RateLimitMaxNumberOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 1),
    _RateLimitMaxNumberOfProfile_Type()
)
rateLimitMaxNumberOfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitMaxNumberOfProfile.setStatus("current")
_RateLimitProfileTable_Object = MibTable
rateLimitProfileTable = _RateLimitProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2)
)
if mibBuilder.loadTexts:
    rateLimitProfileTable.setStatus("current")
_RateLimitProfileEntry_Object = MibTableRow
rateLimitProfileEntry = _RateLimitProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1)
)
rateLimitProfileEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "rateLimitProfileName"),
)
if mibBuilder.loadTexts:
    rateLimitProfileEntry.setStatus("current")
_RateLimitProfileName_Type = DisplayString
_RateLimitProfileName_Object = MibTableColumn
rateLimitProfileName = _RateLimitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 1),
    _RateLimitProfileName_Type()
)
rateLimitProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitProfileName.setStatus("current")
_RateLimitProfilePeakRate_Type = Integer32
_RateLimitProfilePeakRate_Object = MibTableColumn
rateLimitProfilePeakRate = _RateLimitProfilePeakRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 2),
    _RateLimitProfilePeakRate_Type()
)
rateLimitProfilePeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitProfilePeakRate.setStatus("current")
_RateLimitProfileEgrRate_Type = Integer32
_RateLimitProfileEgrRate_Object = MibTableColumn
rateLimitProfileEgrRate = _RateLimitProfileEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 3),
    _RateLimitProfileEgrRate_Type()
)
rateLimitProfileEgrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitProfileEgrRate.setStatus("current")
_RateLimitProfileCommitRate_Type = Integer32
_RateLimitProfileCommitRate_Object = MibTableColumn
rateLimitProfileCommitRate = _RateLimitProfileCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 4),
    _RateLimitProfileCommitRate_Type()
)
rateLimitProfileCommitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitProfileCommitRate.setStatus("current")
_RateLimitProfilePeakState_Type = EnabledStatus
_RateLimitProfilePeakState_Object = MibTableColumn
rateLimitProfilePeakState = _RateLimitProfilePeakState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 5),
    _RateLimitProfilePeakState_Type()
)
rateLimitProfilePeakState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitProfilePeakState.setStatus("current")
_RateLimitProfileEgrState_Type = EnabledStatus
_RateLimitProfileEgrState_Object = MibTableColumn
rateLimitProfileEgrState = _RateLimitProfileEgrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 6),
    _RateLimitProfileEgrState_Type()
)
rateLimitProfileEgrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitProfileEgrState.setStatus("current")
_RateLimitProfileCommitState_Type = EnabledStatus
_RateLimitProfileCommitState_Object = MibTableColumn
rateLimitProfileCommitState = _RateLimitProfileCommitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 7),
    _RateLimitProfileCommitState_Type()
)
rateLimitProfileCommitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitProfileCommitState.setStatus("current")
_RateLimitProfileRowStatus_Type = RowStatus
_RateLimitProfileRowStatus_Object = MibTableColumn
rateLimitProfileRowStatus = _RateLimitProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 2, 1, 8),
    _RateLimitProfileRowStatus_Type()
)
rateLimitProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rateLimitProfileRowStatus.setStatus("current")
_PerQueueMaxNumberOfProfile_Type = Integer32
_PerQueueMaxNumberOfProfile_Object = MibScalar
perQueueMaxNumberOfProfile = _PerQueueMaxNumberOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 3),
    _PerQueueMaxNumberOfProfile_Type()
)
perQueueMaxNumberOfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perQueueMaxNumberOfProfile.setStatus("current")
_PerQueueProfileTable_Object = MibTable
perQueueProfileTable = _PerQueueProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4)
)
if mibBuilder.loadTexts:
    perQueueProfileTable.setStatus("current")
_PerQueueProfileEntry_Object = MibTableRow
perQueueProfileEntry = _PerQueueProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1)
)
perQueueProfileEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "perQueueProfileName"),
)
if mibBuilder.loadTexts:
    perQueueProfileEntry.setStatus("current")
_PerQueueProfileName_Type = DisplayString
_PerQueueProfileName_Object = MibTableColumn
perQueueProfileName = _PerQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 1),
    _PerQueueProfileName_Type()
)
perQueueProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perQueueProfileName.setStatus("current")
_PerQueueProfileQ0CIR_Type = Integer32
_PerQueueProfileQ0CIR_Object = MibTableColumn
perQueueProfileQ0CIR = _PerQueueProfileQ0CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 2),
    _PerQueueProfileQ0CIR_Type()
)
perQueueProfileQ0CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ0CIR.setStatus("current")
_PerQueueProfileQ0PIR_Type = Integer32
_PerQueueProfileQ0PIR_Object = MibTableColumn
perQueueProfileQ0PIR = _PerQueueProfileQ0PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 3),
    _PerQueueProfileQ0PIR_Type()
)
perQueueProfileQ0PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ0PIR.setStatus("current")
_PerQueueProfileQ1CIR_Type = Integer32
_PerQueueProfileQ1CIR_Object = MibTableColumn
perQueueProfileQ1CIR = _PerQueueProfileQ1CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 4),
    _PerQueueProfileQ1CIR_Type()
)
perQueueProfileQ1CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ1CIR.setStatus("current")
_PerQueueProfileQ1PIR_Type = Integer32
_PerQueueProfileQ1PIR_Object = MibTableColumn
perQueueProfileQ1PIR = _PerQueueProfileQ1PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 5),
    _PerQueueProfileQ1PIR_Type()
)
perQueueProfileQ1PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ1PIR.setStatus("current")
_PerQueueProfileQ2CIR_Type = Integer32
_PerQueueProfileQ2CIR_Object = MibTableColumn
perQueueProfileQ2CIR = _PerQueueProfileQ2CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 6),
    _PerQueueProfileQ2CIR_Type()
)
perQueueProfileQ2CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ2CIR.setStatus("current")
_PerQueueProfileQ2PIR_Type = Integer32
_PerQueueProfileQ2PIR_Object = MibTableColumn
perQueueProfileQ2PIR = _PerQueueProfileQ2PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 7),
    _PerQueueProfileQ2PIR_Type()
)
perQueueProfileQ2PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ2PIR.setStatus("current")
_PerQueueProfileQ3CIR_Type = Integer32
_PerQueueProfileQ3CIR_Object = MibTableColumn
perQueueProfileQ3CIR = _PerQueueProfileQ3CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 8),
    _PerQueueProfileQ3CIR_Type()
)
perQueueProfileQ3CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ3CIR.setStatus("current")
_PerQueueProfileQ3PIR_Type = Integer32
_PerQueueProfileQ3PIR_Object = MibTableColumn
perQueueProfileQ3PIR = _PerQueueProfileQ3PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 9),
    _PerQueueProfileQ3PIR_Type()
)
perQueueProfileQ3PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ3PIR.setStatus("current")
_PerQueueProfileQ4CIR_Type = Integer32
_PerQueueProfileQ4CIR_Object = MibTableColumn
perQueueProfileQ4CIR = _PerQueueProfileQ4CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 10),
    _PerQueueProfileQ4CIR_Type()
)
perQueueProfileQ4CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ4CIR.setStatus("current")
_PerQueueProfileQ4PIR_Type = Integer32
_PerQueueProfileQ4PIR_Object = MibTableColumn
perQueueProfileQ4PIR = _PerQueueProfileQ4PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 11),
    _PerQueueProfileQ4PIR_Type()
)
perQueueProfileQ4PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ4PIR.setStatus("current")
_PerQueueProfileQ5CIR_Type = Integer32
_PerQueueProfileQ5CIR_Object = MibTableColumn
perQueueProfileQ5CIR = _PerQueueProfileQ5CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 12),
    _PerQueueProfileQ5CIR_Type()
)
perQueueProfileQ5CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ5CIR.setStatus("current")
_PerQueueProfileQ5PIR_Type = Integer32
_PerQueueProfileQ5PIR_Object = MibTableColumn
perQueueProfileQ5PIR = _PerQueueProfileQ5PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 13),
    _PerQueueProfileQ5PIR_Type()
)
perQueueProfileQ5PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ5PIR.setStatus("current")
_PerQueueProfileQ6CIR_Type = Integer32
_PerQueueProfileQ6CIR_Object = MibTableColumn
perQueueProfileQ6CIR = _PerQueueProfileQ6CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 14),
    _PerQueueProfileQ6CIR_Type()
)
perQueueProfileQ6CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ6CIR.setStatus("current")
_PerQueueProfileQ6PIR_Type = Integer32
_PerQueueProfileQ6PIR_Object = MibTableColumn
perQueueProfileQ6PIR = _PerQueueProfileQ6PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 15),
    _PerQueueProfileQ6PIR_Type()
)
perQueueProfileQ6PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ6PIR.setStatus("current")
_PerQueueProfileQ7CIR_Type = Integer32
_PerQueueProfileQ7CIR_Object = MibTableColumn
perQueueProfileQ7CIR = _PerQueueProfileQ7CIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 16),
    _PerQueueProfileQ7CIR_Type()
)
perQueueProfileQ7CIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ7CIR.setStatus("current")
_PerQueueProfileQ7PIR_Type = Integer32
_PerQueueProfileQ7PIR_Object = MibTableColumn
perQueueProfileQ7PIR = _PerQueueProfileQ7PIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 17),
    _PerQueueProfileQ7PIR_Type()
)
perQueueProfileQ7PIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perQueueProfileQ7PIR.setStatus("current")
_PerQueueProfileRowStatus_Type = RowStatus
_PerQueueProfileRowStatus_Object = MibTableColumn
perQueueProfileRowStatus = _PerQueueProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 44, 4, 1, 18),
    _PerQueueProfileRowStatus_Type()
)
perQueueProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perQueueProfileRowStatus.setStatus("current")
_VlanSecuritySetup_ObjectIdentity = ObjectIdentity
vlanSecuritySetup = _VlanSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 45)
)
_VlanSecurityTable_Object = MibTable
vlanSecurityTable = _VlanSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 45, 1)
)
if mibBuilder.loadTexts:
    vlanSecurityTable.setStatus("current")
_VlanSecurityEntry_Object = MibTableRow
vlanSecurityEntry = _VlanSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 45, 1, 1)
)
vlanSecurityEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanSecurityEntry.setStatus("current")
_VlanSecurityCount_Type = Integer32
_VlanSecurityCount_Object = MibTableColumn
vlanSecurityCount = _VlanSecurityCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 45, 1, 1, 1),
    _VlanSecurityCount_Type()
)
vlanSecurityCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSecurityCount.setStatus("current")
_CfmSetup_ObjectIdentity = ObjectIdentity
cfmSetup = _CfmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46)
)
_CfmLoopbackPortTable_Object = MibTable
cfmLoopbackPortTable = _CfmLoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 1)
)
if mibBuilder.loadTexts:
    cfmLoopbackPortTable.setStatus("current")
_CfmLoopbackPortEntry_Object = MibTableRow
cfmLoopbackPortEntry = _CfmLoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 1, 1)
)
cfmLoopbackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    cfmLoopbackPortEntry.setStatus("current")
_CfmLoopbackPortState_Type = EnabledStatus
_CfmLoopbackPortState_Object = MibTableColumn
cfmLoopbackPortState = _CfmLoopbackPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 1, 1, 1),
    _CfmLoopbackPortState_Type()
)
cfmLoopbackPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmLoopbackPortState.setStatus("current")
_CfmMIPTable_Object = MibTable
cfmMIPTable = _CfmMIPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 2)
)
if mibBuilder.loadTexts:
    cfmMIPTable.setStatus("current")
_CfmMIPEntry_Object = MibTableRow
cfmMIPEntry = _CfmMIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 2, 1)
)
cfmMIPEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "cfmLevel"),
    (0, "ZYXEL-ves1608FE57-MIB", "cfmVlanID"),
    (0, "ZYXEL-ves1608FE57-MIB", "cfmPort"),
)
if mibBuilder.loadTexts:
    cfmMIPEntry.setStatus("current")
_CfmPort_Type = Integer32
_CfmPort_Object = MibTableColumn
cfmPort = _CfmPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 2, 1, 1),
    _CfmPort_Type()
)
cfmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmPort.setStatus("current")
_CfmVlanID_Type = Integer32
_CfmVlanID_Object = MibTableColumn
cfmVlanID = _CfmVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 2, 1, 2),
    _CfmVlanID_Type()
)
cfmVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmVlanID.setStatus("current")
_CfmLevel_Type = Integer32
_CfmLevel_Object = MibTableColumn
cfmLevel = _CfmLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 2, 1, 3),
    _CfmLevel_Type()
)
cfmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmLevel.setStatus("current")
_CfmMIPRowStatus_Type = RowStatus
_CfmMIPRowStatus_Object = MibTableColumn
cfmMIPRowStatus = _CfmMIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 2, 1, 4),
    _CfmMIPRowStatus_Type()
)
cfmMIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMIPRowStatus.setStatus("current")
_CfmActionEnableStatus_Type = EnabledStatus
_CfmActionEnableStatus_Object = MibScalar
cfmActionEnableStatus = _CfmActionEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 46, 3),
    _CfmActionEnableStatus_Type()
)
cfmActionEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmActionEnableStatus.setStatus("current")
_Mrstp_ObjectIdentity = ObjectIdentity
mrstp = _Mrstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48)
)
_MrstpSetup_ObjectIdentity = ObjectIdentity
mrstpSetup = _MrstpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1)
)
_MrstpBridgeTable_Object = MibTable
mrstpBridgeTable = _MrstpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1)
)
if mibBuilder.loadTexts:
    mrstpBridgeTable.setStatus("current")
_MrstpBridgeEntry_Object = MibTableRow
mrstpBridgeEntry = _MrstpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1)
)
mrstpBridgeEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mrstpBridgeIndex"),
)
if mibBuilder.loadTexts:
    mrstpBridgeEntry.setStatus("current")
_MrstpBridgeIndex_Type = Integer32
_MrstpBridgeIndex_Object = MibTableColumn
mrstpBridgeIndex = _MrstpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 1),
    _MrstpBridgeIndex_Type()
)
mrstpBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpBridgeIndex.setStatus("current")
_MrstpState_Type = EnabledStatus
_MrstpState_Object = MibTableColumn
mrstpState = _MrstpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 2),
    _MrstpState_Type()
)
mrstpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpState.setStatus("current")


class _MrstpProtocolSpecification_Type(Integer32):
    """Custom type mrstpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("decLb100", 2),
          ("ieee8021d", 3))
    )


_MrstpProtocolSpecification_Type.__name__ = "Integer32"
_MrstpProtocolSpecification_Object = MibTableColumn
mrstpProtocolSpecification = _MrstpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 3),
    _MrstpProtocolSpecification_Type()
)
mrstpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpProtocolSpecification.setStatus("current")


class _MrstpPriority_Type(Integer32):
    """Custom type mrstpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MrstpPriority_Type.__name__ = "Integer32"
_MrstpPriority_Object = MibTableColumn
mrstpPriority = _MrstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 4),
    _MrstpPriority_Type()
)
mrstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPriority.setStatus("current")
_MrstpTimeSinceTopologyChange_Type = TimeTicks
_MrstpTimeSinceTopologyChange_Object = MibTableColumn
mrstpTimeSinceTopologyChange = _MrstpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 5),
    _MrstpTimeSinceTopologyChange_Type()
)
mrstpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpTimeSinceTopologyChange.setStatus("current")
_MrstpTopChanges_Type = Counter32
_MrstpTopChanges_Object = MibTableColumn
mrstpTopChanges = _MrstpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 6),
    _MrstpTopChanges_Type()
)
mrstpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpTopChanges.setStatus("current")
_MrstpDesignatedRoot_Type = BridgeId
_MrstpDesignatedRoot_Object = MibTableColumn
mrstpDesignatedRoot = _MrstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 7),
    _MrstpDesignatedRoot_Type()
)
mrstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpDesignatedRoot.setStatus("current")
_MrstpRootCost_Type = Integer32
_MrstpRootCost_Object = MibTableColumn
mrstpRootCost = _MrstpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 8),
    _MrstpRootCost_Type()
)
mrstpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpRootCost.setStatus("current")
_MrstpRootPort_Type = Integer32
_MrstpRootPort_Object = MibTableColumn
mrstpRootPort = _MrstpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 9),
    _MrstpRootPort_Type()
)
mrstpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpRootPort.setStatus("current")
_MrstpMaxAge_Type = Timeout
_MrstpMaxAge_Object = MibTableColumn
mrstpMaxAge = _MrstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 10),
    _MrstpMaxAge_Type()
)
mrstpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpMaxAge.setStatus("current")
_MrstpHelloTime_Type = Timeout
_MrstpHelloTime_Object = MibTableColumn
mrstpHelloTime = _MrstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 11),
    _MrstpHelloTime_Type()
)
mrstpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpHelloTime.setStatus("current")
_MrstpHoldTime_Type = Integer32
_MrstpHoldTime_Object = MibTableColumn
mrstpHoldTime = _MrstpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 12),
    _MrstpHoldTime_Type()
)
mrstpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpHoldTime.setStatus("current")
_MrstpForwardDelay_Type = Timeout
_MrstpForwardDelay_Object = MibTableColumn
mrstpForwardDelay = _MrstpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 13),
    _MrstpForwardDelay_Type()
)
mrstpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpForwardDelay.setStatus("current")


class _MrstpBridgeMaxAge_Type(Timeout):
    """Custom type mrstpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MrstpBridgeMaxAge_Type.__name__ = "Timeout"
_MrstpBridgeMaxAge_Object = MibTableColumn
mrstpBridgeMaxAge = _MrstpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 14),
    _MrstpBridgeMaxAge_Type()
)
mrstpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpBridgeMaxAge.setStatus("current")


class _MrstpBridgeHelloTime_Type(Timeout):
    """Custom type mrstpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MrstpBridgeHelloTime_Type.__name__ = "Timeout"
_MrstpBridgeHelloTime_Object = MibTableColumn
mrstpBridgeHelloTime = _MrstpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 15),
    _MrstpBridgeHelloTime_Type()
)
mrstpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpBridgeHelloTime.setStatus("current")


class _MrstpBridgeForwardDelay_Type(Timeout):
    """Custom type mrstpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MrstpBridgeForwardDelay_Type.__name__ = "Timeout"
_MrstpBridgeForwardDelay_Object = MibTableColumn
mrstpBridgeForwardDelay = _MrstpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 1, 1, 16),
    _MrstpBridgeForwardDelay_Type()
)
mrstpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpBridgeForwardDelay.setStatus("current")
_MrstpPortTable_Object = MibTable
mrstpPortTable = _MrstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2)
)
if mibBuilder.loadTexts:
    mrstpPortTable.setStatus("current")
_MrstpPortEntry_Object = MibTableRow
mrstpPortEntry = _MrstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1)
)
mrstpPortEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mrstpPort"),
)
if mibBuilder.loadTexts:
    mrstpPortEntry.setStatus("current")


class _MrstpPort_Type(Integer32):
    """Custom type mrstpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MrstpPort_Type.__name__ = "Integer32"
_MrstpPort_Object = MibTableColumn
mrstpPort = _MrstpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 1),
    _MrstpPort_Type()
)
mrstpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPort.setStatus("current")


class _MrstpPortPriority_Type(Integer32):
    """Custom type mrstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MrstpPortPriority_Type.__name__ = "Integer32"
_MrstpPortPriority_Object = MibTableColumn
mrstpPortPriority = _MrstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 2),
    _MrstpPortPriority_Type()
)
mrstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortPriority.setStatus("current")


class _MrstpPortState_Type(Integer32):
    """Custom type mrstpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_MrstpPortState_Type.__name__ = "Integer32"
_MrstpPortState_Object = MibTableColumn
mrstpPortState = _MrstpPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 3),
    _MrstpPortState_Type()
)
mrstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortState.setStatus("current")


class _MrstpPortEnable_Type(Integer32):
    """Custom type mrstpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_MrstpPortEnable_Type.__name__ = "Integer32"
_MrstpPortEnable_Object = MibTableColumn
mrstpPortEnable = _MrstpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 4),
    _MrstpPortEnable_Type()
)
mrstpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortEnable.setStatus("current")


class _MrstpPortPathCost_Type(Integer32):
    """Custom type mrstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MrstpPortPathCost_Type.__name__ = "Integer32"
_MrstpPortPathCost_Object = MibTableColumn
mrstpPortPathCost = _MrstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 5),
    _MrstpPortPathCost_Type()
)
mrstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortPathCost.setStatus("current")
_MrstpPortDesignatedRoot_Type = BridgeId
_MrstpPortDesignatedRoot_Object = MibTableColumn
mrstpPortDesignatedRoot = _MrstpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 6),
    _MrstpPortDesignatedRoot_Type()
)
mrstpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedRoot.setStatus("current")
_MrstpPortDesignatedCost_Type = Integer32
_MrstpPortDesignatedCost_Object = MibTableColumn
mrstpPortDesignatedCost = _MrstpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 7),
    _MrstpPortDesignatedCost_Type()
)
mrstpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedCost.setStatus("current")
_MrstpPortDesignatedBridge_Type = BridgeId
_MrstpPortDesignatedBridge_Object = MibTableColumn
mrstpPortDesignatedBridge = _MrstpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 8),
    _MrstpPortDesignatedBridge_Type()
)
mrstpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedBridge.setStatus("current")


class _MrstpPortDesignatedPort_Type(OctetString):
    """Custom type mrstpPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MrstpPortDesignatedPort_Type.__name__ = "OctetString"
_MrstpPortDesignatedPort_Object = MibTableColumn
mrstpPortDesignatedPort = _MrstpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 9),
    _MrstpPortDesignatedPort_Type()
)
mrstpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedPort.setStatus("current")
_MrstpPortForwardTransitions_Type = Counter32
_MrstpPortForwardTransitions_Object = MibTableColumn
mrstpPortForwardTransitions = _MrstpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 10),
    _MrstpPortForwardTransitions_Type()
)
mrstpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortForwardTransitions.setStatus("current")
_MrstpPortOnBridgeIndex_Type = Integer32
_MrstpPortOnBridgeIndex_Object = MibTableColumn
mrstpPortOnBridgeIndex = _MrstpPortOnBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 1, 2, 1, 11),
    _MrstpPortOnBridgeIndex_Type()
)
mrstpPortOnBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortOnBridgeIndex.setStatus("current")
_MrstpNotifications_ObjectIdentity = ObjectIdentity
mrstpNotifications = _MrstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 2)
)
_DhcpSnp_ObjectIdentity = ObjectIdentity
dhcpSnp = _DhcpSnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49)
)
_DhcpSnpVlanTable_Object = MibTable
dhcpSnpVlanTable = _DhcpSnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1)
)
if mibBuilder.loadTexts:
    dhcpSnpVlanTable.setStatus("current")
_DhcpSnpVlanEntry_Object = MibTableRow
dhcpSnpVlanEntry = _DhcpSnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1, 1)
)
dhcpSnpVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpSnpVlanEntryVid"),
)
if mibBuilder.loadTexts:
    dhcpSnpVlanEntry.setStatus("current")


class _DhcpSnpVlanEntryVid_Type(Integer32):
    """Custom type dhcpSnpVlanEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnpVlanEntryVid_Type.__name__ = "Integer32"
_DhcpSnpVlanEntryVid_Object = MibTableColumn
dhcpSnpVlanEntryVid = _DhcpSnpVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1, 1, 1),
    _DhcpSnpVlanEntryVid_Type()
)
dhcpSnpVlanEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryVid.setStatus("current")
_DhcpSnpVlanEntryEnable_Type = EnabledStatus
_DhcpSnpVlanEntryEnable_Object = MibTableColumn
dhcpSnpVlanEntryEnable = _DhcpSnpVlanEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1, 1, 2),
    _DhcpSnpVlanEntryEnable_Type()
)
dhcpSnpVlanEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryEnable.setStatus("current")
_DhcpSnpVlanEntryOption82Enable_Type = EnabledStatus
_DhcpSnpVlanEntryOption82Enable_Object = MibTableColumn
dhcpSnpVlanEntryOption82Enable = _DhcpSnpVlanEntryOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1, 1, 3),
    _DhcpSnpVlanEntryOption82Enable_Type()
)
dhcpSnpVlanEntryOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryOption82Enable.setStatus("current")
_DhcpSnpVlanEntryInfo_Type = EnabledStatus
_DhcpSnpVlanEntryInfo_Object = MibTableColumn
dhcpSnpVlanEntryInfo = _DhcpSnpVlanEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1, 1, 4),
    _DhcpSnpVlanEntryInfo_Type()
)
dhcpSnpVlanEntryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryInfo.setStatus("current")
_DhcpSnpVlanEntryRemoteID_Type = EnabledStatus
_DhcpSnpVlanEntryRemoteID_Object = MibTableColumn
dhcpSnpVlanEntryRemoteID = _DhcpSnpVlanEntryRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 1, 1, 5),
    _DhcpSnpVlanEntryRemoteID_Type()
)
dhcpSnpVlanEntryRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryRemoteID.setStatus("current")
_DhcpSnpPortTable_Object = MibTable
dhcpSnpPortTable = _DhcpSnpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 2)
)
if mibBuilder.loadTexts:
    dhcpSnpPortTable.setStatus("current")
_DhcpSnpPortEntry_Object = MibTableRow
dhcpSnpPortEntry = _DhcpSnpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 2, 1)
)
dhcpSnpPortEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpSnpPortEntryPort"),
)
if mibBuilder.loadTexts:
    dhcpSnpPortEntry.setStatus("current")
_DhcpSnpPortEntryPort_Type = Integer32
_DhcpSnpPortEntryPort_Object = MibTableColumn
dhcpSnpPortEntryPort = _DhcpSnpPortEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 2, 1, 1),
    _DhcpSnpPortEntryPort_Type()
)
dhcpSnpPortEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryPort.setStatus("current")
_DhcpSnpPortEntryTrust_Type = EnabledStatus
_DhcpSnpPortEntryTrust_Object = MibTableColumn
dhcpSnpPortEntryTrust = _DhcpSnpPortEntryTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 2, 1, 2),
    _DhcpSnpPortEntryTrust_Type()
)
dhcpSnpPortEntryTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryTrust.setStatus("current")


class _DhcpSnpPortEntryRate_Type(Integer32):
    """Custom type dhcpSnpPortEntryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_DhcpSnpPortEntryRate_Type.__name__ = "Integer32"
_DhcpSnpPortEntryRate_Object = MibTableColumn
dhcpSnpPortEntryRate = _DhcpSnpPortEntryRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 2, 1, 3),
    _DhcpSnpPortEntryRate_Type()
)
dhcpSnpPortEntryRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryRate.setStatus("current")
_DhcpSnpBindTable_Object = MibTable
dhcpSnpBindTable = _DhcpSnpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3)
)
if mibBuilder.loadTexts:
    dhcpSnpBindTable.setStatus("current")
_DhcpSnpBindEntry_Object = MibTableRow
dhcpSnpBindEntry = _DhcpSnpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1)
)
dhcpSnpBindEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpSnpBindEntryMac"),
    (0, "ZYXEL-ves1608FE57-MIB", "dhcpSnpBindEntryVid"),
)
if mibBuilder.loadTexts:
    dhcpSnpBindEntry.setStatus("current")
_DhcpSnpBindEntryMac_Type = MacAddress
_DhcpSnpBindEntryMac_Object = MibTableColumn
dhcpSnpBindEntryMac = _DhcpSnpBindEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1, 1),
    _DhcpSnpBindEntryMac_Type()
)
dhcpSnpBindEntryMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryMac.setStatus("current")
_DhcpSnpBindEntryVid_Type = Integer32
_DhcpSnpBindEntryVid_Object = MibTableColumn
dhcpSnpBindEntryVid = _DhcpSnpBindEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1, 2),
    _DhcpSnpBindEntryVid_Type()
)
dhcpSnpBindEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryVid.setStatus("current")
_DhcpSnpBindEntryIP_Type = IpAddress
_DhcpSnpBindEntryIP_Object = MibTableColumn
dhcpSnpBindEntryIP = _DhcpSnpBindEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1, 3),
    _DhcpSnpBindEntryIP_Type()
)
dhcpSnpBindEntryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryIP.setStatus("current")
_DhcpSnpBindEntryLease_Type = Integer32
_DhcpSnpBindEntryLease_Object = MibTableColumn
dhcpSnpBindEntryLease = _DhcpSnpBindEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1, 4),
    _DhcpSnpBindEntryLease_Type()
)
dhcpSnpBindEntryLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryLease.setStatus("current")


class _DhcpSnpBindEntryType_Type(Integer32):
    """Custom type dhcpSnpBindEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dynamic", 2)
    )


_DhcpSnpBindEntryType_Type.__name__ = "Integer32"
_DhcpSnpBindEntryType_Object = MibTableColumn
dhcpSnpBindEntryType = _DhcpSnpBindEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1, 5),
    _DhcpSnpBindEntryType_Type()
)
dhcpSnpBindEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryType.setStatus("current")
_DhcpSnpBindEntryPort_Type = Integer32
_DhcpSnpBindEntryPort_Object = MibTableColumn
dhcpSnpBindEntryPort = _DhcpSnpBindEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 3, 1, 6),
    _DhcpSnpBindEntryPort_Type()
)
dhcpSnpBindEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryPort.setStatus("current")
_DhcpSnpEnable_Type = EnabledStatus
_DhcpSnpEnable_Object = MibScalar
dhcpSnpEnable = _DhcpSnpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 4),
    _DhcpSnpEnable_Type()
)
dhcpSnpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpEnable.setStatus("current")
_DhcpSnpDb_ObjectIdentity = ObjectIdentity
dhcpSnpDb = _DhcpSnpDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5)
)


class _DhcpSnpDbAbort_Type(Integer32):
    """Custom type dhcpSnpDbAbort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcpSnpDbAbort_Type.__name__ = "Integer32"
_DhcpSnpDbAbort_Object = MibScalar
dhcpSnpDbAbort = _DhcpSnpDbAbort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 1),
    _DhcpSnpDbAbort_Type()
)
dhcpSnpDbAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbAbort.setStatus("current")


class _DhcpSnpDbWriteDelay_Type(Integer32):
    """Custom type dhcpSnpDbWriteDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcpSnpDbWriteDelay_Type.__name__ = "Integer32"
_DhcpSnpDbWriteDelay_Object = MibScalar
dhcpSnpDbWriteDelay = _DhcpSnpDbWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 2),
    _DhcpSnpDbWriteDelay_Type()
)
dhcpSnpDbWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbWriteDelay.setStatus("current")


class _DhcpSnpDbUrl_Type(DisplayString):
    """Custom type dhcpSnpDbUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnpDbUrl_Type.__name__ = "DisplayString"
_DhcpSnpDbUrl_Object = MibScalar
dhcpSnpDbUrl = _DhcpSnpDbUrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 3),
    _DhcpSnpDbUrl_Type()
)
dhcpSnpDbUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbUrl.setStatus("current")


class _DhcpSnpDbUrlRenew_Type(DisplayString):
    """Custom type dhcpSnpDbUrlRenew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnpDbUrlRenew_Type.__name__ = "DisplayString"
_DhcpSnpDbUrlRenew_Object = MibScalar
dhcpSnpDbUrlRenew = _DhcpSnpDbUrlRenew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 4),
    _DhcpSnpDbUrlRenew_Type()
)
dhcpSnpDbUrlRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbUrlRenew.setStatus("current")
_DhcpSnpDbStat_ObjectIdentity = ObjectIdentity
dhcpSnpDbStat = _DhcpSnpDbStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5)
)
_DhcpSnpDbStatClear_Type = EnabledStatus
_DhcpSnpDbStatClear_Object = MibScalar
dhcpSnpDbStatClear = _DhcpSnpDbStatClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 1),
    _DhcpSnpDbStatClear_Type()
)
dhcpSnpDbStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbStatClear.setStatus("current")


class _DhcpSnpDbStatAgentRunning_Type(Integer32):
    """Custom type dhcpSnpDbStatAgentRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_DhcpSnpDbStatAgentRunning_Type.__name__ = "Integer32"
_DhcpSnpDbStatAgentRunning_Object = MibScalar
dhcpSnpDbStatAgentRunning = _DhcpSnpDbStatAgentRunning_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 2),
    _DhcpSnpDbStatAgentRunning_Type()
)
dhcpSnpDbStatAgentRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatAgentRunning.setStatus("current")
_DhcpSnpDbStatDelayExpiry_Type = Integer32
_DhcpSnpDbStatDelayExpiry_Object = MibScalar
dhcpSnpDbStatDelayExpiry = _DhcpSnpDbStatDelayExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 3),
    _DhcpSnpDbStatDelayExpiry_Type()
)
dhcpSnpDbStatDelayExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatDelayExpiry.setStatus("current")
_DhcpSnpDbStatAbortExpiry_Type = Integer32
_DhcpSnpDbStatAbortExpiry_Object = MibScalar
dhcpSnpDbStatAbortExpiry = _DhcpSnpDbStatAbortExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 4),
    _DhcpSnpDbStatAbortExpiry_Type()
)
dhcpSnpDbStatAbortExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatAbortExpiry.setStatus("current")
_DhcpSnpDbStatLastSuccTime_Type = DisplayString
_DhcpSnpDbStatLastSuccTime_Object = MibScalar
dhcpSnpDbStatLastSuccTime = _DhcpSnpDbStatLastSuccTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 5),
    _DhcpSnpDbStatLastSuccTime_Type()
)
dhcpSnpDbStatLastSuccTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastSuccTime.setStatus("current")
_DhcpSnpDbStatLastFailTime_Type = DisplayString
_DhcpSnpDbStatLastFailTime_Object = MibScalar
dhcpSnpDbStatLastFailTime = _DhcpSnpDbStatLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 6),
    _DhcpSnpDbStatLastFailTime_Type()
)
dhcpSnpDbStatLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastFailTime.setStatus("current")
_DhcpSnpDbStatLastFailReason_Type = DisplayString
_DhcpSnpDbStatLastFailReason_Object = MibScalar
dhcpSnpDbStatLastFailReason = _DhcpSnpDbStatLastFailReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 7),
    _DhcpSnpDbStatLastFailReason_Type()
)
dhcpSnpDbStatLastFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastFailReason.setStatus("current")
_DhcpSnpDbStatTotalAttempt_Type = Integer32
_DhcpSnpDbStatTotalAttempt_Object = MibScalar
dhcpSnpDbStatTotalAttempt = _DhcpSnpDbStatTotalAttempt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 8),
    _DhcpSnpDbStatTotalAttempt_Type()
)
dhcpSnpDbStatTotalAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalAttempt.setStatus("current")
_DhcpSnpDbStatStartupFail_Type = Integer32
_DhcpSnpDbStatStartupFail_Object = MibScalar
dhcpSnpDbStatStartupFail = _DhcpSnpDbStatStartupFail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 9),
    _DhcpSnpDbStatStartupFail_Type()
)
dhcpSnpDbStatStartupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatStartupFail.setStatus("current")
_DhcpSnpDbStatSuccTrans_Type = Integer32
_DhcpSnpDbStatSuccTrans_Object = MibScalar
dhcpSnpDbStatSuccTrans = _DhcpSnpDbStatSuccTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 10),
    _DhcpSnpDbStatSuccTrans_Type()
)
dhcpSnpDbStatSuccTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccTrans.setStatus("current")
_DhcpSnpDbStatFailTrans_Type = Integer32
_DhcpSnpDbStatFailTrans_Object = MibScalar
dhcpSnpDbStatFailTrans = _DhcpSnpDbStatFailTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 11),
    _DhcpSnpDbStatFailTrans_Type()
)
dhcpSnpDbStatFailTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailTrans.setStatus("current")
_DhcpSnpDbStatSuccRead_Type = Integer32
_DhcpSnpDbStatSuccRead_Object = MibScalar
dhcpSnpDbStatSuccRead = _DhcpSnpDbStatSuccRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 12),
    _DhcpSnpDbStatSuccRead_Type()
)
dhcpSnpDbStatSuccRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccRead.setStatus("current")
_DhcpSnpDbStatFailRead_Type = Integer32
_DhcpSnpDbStatFailRead_Object = MibScalar
dhcpSnpDbStatFailRead = _DhcpSnpDbStatFailRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 13),
    _DhcpSnpDbStatFailRead_Type()
)
dhcpSnpDbStatFailRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailRead.setStatus("current")
_DhcpSnpDbStatSuccWrite_Type = Integer32
_DhcpSnpDbStatSuccWrite_Object = MibScalar
dhcpSnpDbStatSuccWrite = _DhcpSnpDbStatSuccWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 14),
    _DhcpSnpDbStatSuccWrite_Type()
)
dhcpSnpDbStatSuccWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccWrite.setStatus("current")
_DhcpSnpDbStatFailWrite_Type = Integer32
_DhcpSnpDbStatFailWrite_Object = MibScalar
dhcpSnpDbStatFailWrite = _DhcpSnpDbStatFailWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 15),
    _DhcpSnpDbStatFailWrite_Type()
)
dhcpSnpDbStatFailWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailWrite.setStatus("current")


class _DhcpSnpDbStatFirstSuccAccess_Type(Integer32):
    """Custom type dhcpSnpDbStatFirstSuccAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_DhcpSnpDbStatFirstSuccAccess_Type.__name__ = "Integer32"
_DhcpSnpDbStatFirstSuccAccess_Object = MibScalar
dhcpSnpDbStatFirstSuccAccess = _DhcpSnpDbStatFirstSuccAccess_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 16),
    _DhcpSnpDbStatFirstSuccAccess_Type()
)
dhcpSnpDbStatFirstSuccAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFirstSuccAccess.setStatus("current")
_DhcpSnpDbStatLastIgnoreBindCol_Type = Integer32
_DhcpSnpDbStatLastIgnoreBindCol_Object = MibScalar
dhcpSnpDbStatLastIgnoreBindCol = _DhcpSnpDbStatLastIgnoreBindCol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 17),
    _DhcpSnpDbStatLastIgnoreBindCol_Type()
)
dhcpSnpDbStatLastIgnoreBindCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreBindCol.setStatus("current")
_DhcpSnpDbStatLastIgnoreExpireLease_Type = Integer32
_DhcpSnpDbStatLastIgnoreExpireLease_Object = MibScalar
dhcpSnpDbStatLastIgnoreExpireLease = _DhcpSnpDbStatLastIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 18),
    _DhcpSnpDbStatLastIgnoreExpireLease_Type()
)
dhcpSnpDbStatLastIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreExpireLease.setStatus("current")
_DhcpSnpDbStatLastIgnoreInvalidIntf_Type = Integer32
_DhcpSnpDbStatLastIgnoreInvalidIntf_Object = MibScalar
dhcpSnpDbStatLastIgnoreInvalidIntf = _DhcpSnpDbStatLastIgnoreInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 19),
    _DhcpSnpDbStatLastIgnoreInvalidIntf_Type()
)
dhcpSnpDbStatLastIgnoreInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreInvalidIntf.setStatus("current")
_DhcpSnpDbStatLastIgnoreUnsuppVlan_Type = Integer32
_DhcpSnpDbStatLastIgnoreUnsuppVlan_Object = MibScalar
dhcpSnpDbStatLastIgnoreUnsuppVlan = _DhcpSnpDbStatLastIgnoreUnsuppVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 20),
    _DhcpSnpDbStatLastIgnoreUnsuppVlan_Type()
)
dhcpSnpDbStatLastIgnoreUnsuppVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreUnsuppVlan.setStatus("current")
_DhcpSnpDbStatLastIgnoreParse_Type = Integer32
_DhcpSnpDbStatLastIgnoreParse_Object = MibScalar
dhcpSnpDbStatLastIgnoreParse = _DhcpSnpDbStatLastIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 21),
    _DhcpSnpDbStatLastIgnoreParse_Type()
)
dhcpSnpDbStatLastIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreParse.setStatus("current")
_DhcpSnpDbStatTotalIgnoreBindCol_Type = Integer32
_DhcpSnpDbStatTotalIgnoreBindCol_Object = MibScalar
dhcpSnpDbStatTotalIgnoreBindCol = _DhcpSnpDbStatTotalIgnoreBindCol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 22),
    _DhcpSnpDbStatTotalIgnoreBindCol_Type()
)
dhcpSnpDbStatTotalIgnoreBindCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreBindCol.setStatus("current")
_DhcpSnpDbStatTotalIgnoreExpireLease_Type = Integer32
_DhcpSnpDbStatTotalIgnoreExpireLease_Object = MibScalar
dhcpSnpDbStatTotalIgnoreExpireLease = _DhcpSnpDbStatTotalIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 23),
    _DhcpSnpDbStatTotalIgnoreExpireLease_Type()
)
dhcpSnpDbStatTotalIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreExpireLease.setStatus("current")
_DhcpSnpDbStatTotalIgnoreInvalidIntf_Type = Integer32
_DhcpSnpDbStatTotalIgnoreInvalidIntf_Object = MibScalar
dhcpSnpDbStatTotalIgnoreInvalidIntf = _DhcpSnpDbStatTotalIgnoreInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 24),
    _DhcpSnpDbStatTotalIgnoreInvalidIntf_Type()
)
dhcpSnpDbStatTotalIgnoreInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreInvalidIntf.setStatus("current")
_DhcpSnpDbStatTotalIgnoreUnsuppVlan_Type = Integer32
_DhcpSnpDbStatTotalIgnoreUnsuppVlan_Object = MibScalar
dhcpSnpDbStatTotalIgnoreUnsuppVlan = _DhcpSnpDbStatTotalIgnoreUnsuppVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 25),
    _DhcpSnpDbStatTotalIgnoreUnsuppVlan_Type()
)
dhcpSnpDbStatTotalIgnoreUnsuppVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreUnsuppVlan.setStatus("current")
_DhcpSnpDbStatTotalIgnoreParse_Type = Integer32
_DhcpSnpDbStatTotalIgnoreParse_Object = MibScalar
dhcpSnpDbStatTotalIgnoreParse = _DhcpSnpDbStatTotalIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 26),
    _DhcpSnpDbStatTotalIgnoreParse_Type()
)
dhcpSnpDbStatTotalIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreParse.setStatus("current")


class _DhcpSnpDbStatFirstSuccessAccess_Type(Integer32):
    """Custom type dhcpSnpDbStatFirstSuccessAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_DhcpSnpDbStatFirstSuccessAccess_Type.__name__ = "Integer32"
_DhcpSnpDbStatFirstSuccessAccess_Object = MibScalar
dhcpSnpDbStatFirstSuccessAccess = _DhcpSnpDbStatFirstSuccessAccess_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 5, 5, 27),
    _DhcpSnpDbStatFirstSuccessAccess_Type()
)
dhcpSnpDbStatFirstSuccessAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFirstSuccessAccess.setStatus("current")
_DhcpSnpDhcpVlan_ObjectIdentity = ObjectIdentity
dhcpSnpDhcpVlan = _DhcpSnpDhcpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 6)
)


class _DhcpSnpDhcpVlanVid_Type(Integer32):
    """Custom type dhcpSnpDhcpVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DhcpSnpDhcpVlanVid_Type.__name__ = "Integer32"
_DhcpSnpDhcpVlanVid_Object = MibScalar
dhcpSnpDhcpVlanVid = _DhcpSnpDhcpVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 49, 6, 1),
    _DhcpSnpDhcpVlanVid_Type()
)
dhcpSnpDhcpVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDhcpVlanVid.setStatus("current")
_Ipsg_ObjectIdentity = ObjectIdentity
ipsg = _Ipsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50)
)
_IpsgTable_Object = MibTable
ipsgTable = _IpsgTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1)
)
if mibBuilder.loadTexts:
    ipsgTable.setStatus("current")
_IpsgEntry_Object = MibTableRow
ipsgEntry = _IpsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1)
)
ipsgEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "ipsgEntryMac"),
    (0, "ZYXEL-ves1608FE57-MIB", "ipsgEntryVid"),
)
if mibBuilder.loadTexts:
    ipsgEntry.setStatus("current")
_IpsgEntryMac_Type = MacAddress
_IpsgEntryMac_Object = MibTableColumn
ipsgEntryMac = _IpsgEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 1),
    _IpsgEntryMac_Type()
)
ipsgEntryMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryMac.setStatus("current")


class _IpsgEntryVid_Type(Integer32):
    """Custom type ipsgEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpsgEntryVid_Type.__name__ = "Integer32"
_IpsgEntryVid_Object = MibTableColumn
ipsgEntryVid = _IpsgEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 2),
    _IpsgEntryVid_Type()
)
ipsgEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryVid.setStatus("current")
_IpsgEntryIp_Type = IpAddress
_IpsgEntryIp_Object = MibTableColumn
ipsgEntryIp = _IpsgEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 3),
    _IpsgEntryIp_Type()
)
ipsgEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryIp.setStatus("current")
_IpsgEntryLease_Type = Integer32
_IpsgEntryLease_Object = MibTableColumn
ipsgEntryLease = _IpsgEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 4),
    _IpsgEntryLease_Type()
)
ipsgEntryLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryLease.setStatus("current")


class _IpsgEntryType_Type(Integer32):
    """Custom type ipsgEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_IpsgEntryType_Type.__name__ = "Integer32"
_IpsgEntryType_Object = MibTableColumn
ipsgEntryType = _IpsgEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 5),
    _IpsgEntryType_Type()
)
ipsgEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryType.setStatus("current")
_IpsgEntryPort_Type = Integer32
_IpsgEntryPort_Object = MibTableColumn
ipsgEntryPort = _IpsgEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 6),
    _IpsgEntryPort_Type()
)
ipsgEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryPort.setStatus("current")
_IpsgEntryState_Type = RowStatus
_IpsgEntryState_Object = MibTableColumn
ipsgEntryState = _IpsgEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 50, 1, 1, 7),
    _IpsgEntryState_Type()
)
ipsgEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsgEntryState.setStatus("current")
_ArpInspect_ObjectIdentity = ObjectIdentity
arpInspect = _ArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51)
)
_ArpInspectSetup_ObjectIdentity = ObjectIdentity
arpInspectSetup = _ArpInspectSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1)
)
_ArpInspectState_Type = EnabledStatus
_ArpInspectState_Object = MibScalar
arpInspectState = _ArpInspectState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 1),
    _ArpInspectState_Type()
)
arpInspectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectState.setStatus("current")


class _ArpInspectFilterAgingTime_Type(Integer32):
    """Custom type arpInspectFilterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArpInspectFilterAgingTime_Type.__name__ = "Integer32"
_ArpInspectFilterAgingTime_Object = MibScalar
arpInspectFilterAgingTime = _ArpInspectFilterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 2),
    _ArpInspectFilterAgingTime_Type()
)
arpInspectFilterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterAgingTime.setStatus("current")
_ArpInspectLog_ObjectIdentity = ObjectIdentity
arpInspectLog = _ArpInspectLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 3)
)


class _ArpInspectLogEntries_Type(Integer32):
    """Custom type arpInspectLogEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ArpInspectLogEntries_Type.__name__ = "Integer32"
_ArpInspectLogEntries_Object = MibScalar
arpInspectLogEntries = _ArpInspectLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 3, 1),
    _ArpInspectLogEntries_Type()
)
arpInspectLogEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogEntries.setStatus("current")


class _ArpInspectLogRate_Type(Integer32):
    """Custom type arpInspectLogRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ArpInspectLogRate_Type.__name__ = "Integer32"
_ArpInspectLogRate_Object = MibScalar
arpInspectLogRate = _ArpInspectLogRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 3, 2),
    _ArpInspectLogRate_Type()
)
arpInspectLogRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogRate.setStatus("current")


class _ArpInspectLogInterval_Type(Integer32):
    """Custom type arpInspectLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArpInspectLogInterval_Type.__name__ = "Integer32"
_ArpInspectLogInterval_Object = MibScalar
arpInspectLogInterval = _ArpInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 3, 3),
    _ArpInspectLogInterval_Type()
)
arpInspectLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogInterval.setStatus("current")
_ArpInspectVlanTable_Object = MibTable
arpInspectVlanTable = _ArpInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 4)
)
if mibBuilder.loadTexts:
    arpInspectVlanTable.setStatus("current")
_ArpInspectVlanEntry_Object = MibTableRow
arpInspectVlanEntry = _ArpInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 4, 1)
)
arpInspectVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectVlanVid"),
)
if mibBuilder.loadTexts:
    arpInspectVlanEntry.setStatus("current")


class _ArpInspectVlanVid_Type(Integer32):
    """Custom type arpInspectVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectVlanVid_Type.__name__ = "Integer32"
_ArpInspectVlanVid_Object = MibTableColumn
arpInspectVlanVid = _ArpInspectVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 4, 1, 1),
    _ArpInspectVlanVid_Type()
)
arpInspectVlanVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectVlanVid.setStatus("current")


class _ArpInspectVlanLog_Type(Integer32):
    """Custom type arpInspectVlanLog based on Integer32"""
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
        *(("all", 1),
          ("none", 2),
          ("permit", 3),
          ("deny", 4))
    )


_ArpInspectVlanLog_Type.__name__ = "Integer32"
_ArpInspectVlanLog_Object = MibTableColumn
arpInspectVlanLog = _ArpInspectVlanLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 4, 1, 2),
    _ArpInspectVlanLog_Type()
)
arpInspectVlanLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanLog.setStatus("current")


class _ArpInspectVlanStatus_Type(Integer32):
    """Custom type arpInspectVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ArpInspectVlanStatus_Type.__name__ = "Integer32"
_ArpInspectVlanStatus_Object = MibTableColumn
arpInspectVlanStatus = _ArpInspectVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 4, 1, 3),
    _ArpInspectVlanStatus_Type()
)
arpInspectVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanStatus.setStatus("current")
_ArpInspectPortTable_Object = MibTable
arpInspectPortTable = _ArpInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 5)
)
if mibBuilder.loadTexts:
    arpInspectPortTable.setStatus("current")
_ArpInspectPortEntry_Object = MibTableRow
arpInspectPortEntry = _ArpInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 5, 1)
)
arpInspectPortEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectPortIndex"),
)
if mibBuilder.loadTexts:
    arpInspectPortEntry.setStatus("current")
_ArpInspectPortIndex_Type = Integer32
_ArpInspectPortIndex_Object = MibTableColumn
arpInspectPortIndex = _ArpInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 5, 1, 1),
    _ArpInspectPortIndex_Type()
)
arpInspectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectPortIndex.setStatus("current")


class _ArpInspectPortTrust_Type(Integer32):
    """Custom type arpInspectPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_ArpInspectPortTrust_Type.__name__ = "Integer32"
_ArpInspectPortTrust_Object = MibTableColumn
arpInspectPortTrust = _ArpInspectPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 5, 1, 2),
    _ArpInspectPortTrust_Type()
)
arpInspectPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortTrust.setStatus("current")


class _ArpInspectPortRate_Type(Integer32):
    """Custom type arpInspectPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ArpInspectPortRate_Type.__name__ = "Integer32"
_ArpInspectPortRate_Object = MibTableColumn
arpInspectPortRate = _ArpInspectPortRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 5, 1, 3),
    _ArpInspectPortRate_Type()
)
arpInspectPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortRate.setStatus("current")


class _ArpInspectPortInterval_Type(Integer32):
    """Custom type arpInspectPortInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ArpInspectPortInterval_Type.__name__ = "Integer32"
_ArpInspectPortInterval_Object = MibTableColumn
arpInspectPortInterval = _ArpInspectPortInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 1, 5, 1, 4),
    _ArpInspectPortInterval_Type()
)
arpInspectPortInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortInterval.setStatus("current")
_ArpInspectStatus_ObjectIdentity = ObjectIdentity
arpInspectStatus = _ArpInspectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2)
)
_ArpInspectFilterClear_Type = EnabledStatus
_ArpInspectFilterClear_Object = MibScalar
arpInspectFilterClear = _ArpInspectFilterClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 1),
    _ArpInspectFilterClear_Type()
)
arpInspectFilterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterClear.setStatus("current")
_ArpInspectLogClear_Type = EnabledStatus
_ArpInspectLogClear_Object = MibScalar
arpInspectLogClear = _ArpInspectLogClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 2),
    _ArpInspectLogClear_Type()
)
arpInspectLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogClear.setStatus("current")
_ArpInspectFilterTable_Object = MibTable
arpInspectFilterTable = _ArpInspectFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3)
)
if mibBuilder.loadTexts:
    arpInspectFilterTable.setStatus("current")
_ArpInspectFilterEntry_Object = MibTableRow
arpInspectFilterEntry = _ArpInspectFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1)
)
arpInspectFilterEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectFilterMac"),
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectFilterVid"),
)
if mibBuilder.loadTexts:
    arpInspectFilterEntry.setStatus("current")
_ArpInspectFilterMac_Type = MacAddress
_ArpInspectFilterMac_Object = MibTableColumn
arpInspectFilterMac = _ArpInspectFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1, 1),
    _ArpInspectFilterMac_Type()
)
arpInspectFilterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterMac.setStatus("current")


class _ArpInspectFilterVid_Type(Integer32):
    """Custom type arpInspectFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectFilterVid_Type.__name__ = "Integer32"
_ArpInspectFilterVid_Object = MibTableColumn
arpInspectFilterVid = _ArpInspectFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1, 2),
    _ArpInspectFilterVid_Type()
)
arpInspectFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterVid.setStatus("current")
_ArpInspectFilterPort_Type = Integer32
_ArpInspectFilterPort_Object = MibTableColumn
arpInspectFilterPort = _ArpInspectFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1, 3),
    _ArpInspectFilterPort_Type()
)
arpInspectFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterPort.setStatus("current")
_ArpInspectFilterExpiry_Type = Integer32
_ArpInspectFilterExpiry_Object = MibTableColumn
arpInspectFilterExpiry = _ArpInspectFilterExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1, 4),
    _ArpInspectFilterExpiry_Type()
)
arpInspectFilterExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterExpiry.setStatus("current")


class _ArpInspectFilterReason_Type(Integer32):
    """Custom type arpInspectFilterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macVid", 1),
          ("port", 2),
          ("ip", 3))
    )


_ArpInspectFilterReason_Type.__name__ = "Integer32"
_ArpInspectFilterReason_Object = MibTableColumn
arpInspectFilterReason = _ArpInspectFilterReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1, 5),
    _ArpInspectFilterReason_Type()
)
arpInspectFilterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterReason.setStatus("current")
_ArpInspectFilterRowStatus_Type = RowStatus
_ArpInspectFilterRowStatus_Object = MibTableColumn
arpInspectFilterRowStatus = _ArpInspectFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 3, 1, 6),
    _ArpInspectFilterRowStatus_Type()
)
arpInspectFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arpInspectFilterRowStatus.setStatus("current")
_ArpInspectLogTable_Object = MibTable
arpInspectLogTable = _ArpInspectLogTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4)
)
if mibBuilder.loadTexts:
    arpInspectLogTable.setStatus("current")
_ArpInspectLogEntry_Object = MibTableRow
arpInspectLogEntry = _ArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1)
)
arpInspectLogEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectLogMac"),
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectLogVid"),
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectLogPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectLogIp"),
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectLogReason"),
)
if mibBuilder.loadTexts:
    arpInspectLogEntry.setStatus("current")
_ArpInspectLogMac_Type = MacAddress
_ArpInspectLogMac_Object = MibTableColumn
arpInspectLogMac = _ArpInspectLogMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 1),
    _ArpInspectLogMac_Type()
)
arpInspectLogMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogMac.setStatus("current")


class _ArpInspectLogVid_Type(Integer32):
    """Custom type arpInspectLogVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectLogVid_Type.__name__ = "Integer32"
_ArpInspectLogVid_Object = MibTableColumn
arpInspectLogVid = _ArpInspectLogVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 2),
    _ArpInspectLogVid_Type()
)
arpInspectLogVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogVid.setStatus("current")
_ArpInspectLogPort_Type = Integer32
_ArpInspectLogPort_Object = MibTableColumn
arpInspectLogPort = _ArpInspectLogPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 3),
    _ArpInspectLogPort_Type()
)
arpInspectLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogPort.setStatus("current")
_ArpInspectLogIp_Type = IpAddress
_ArpInspectLogIp_Object = MibTableColumn
arpInspectLogIp = _ArpInspectLogIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 4),
    _ArpInspectLogIp_Type()
)
arpInspectLogIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogIp.setStatus("current")
_ArpInspectLogNumPkt_Type = Integer32
_ArpInspectLogNumPkt_Object = MibTableColumn
arpInspectLogNumPkt = _ArpInspectLogNumPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 5),
    _ArpInspectLogNumPkt_Type()
)
arpInspectLogNumPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogNumPkt.setStatus("current")


class _ArpInspectLogReason_Type(Integer32):
    """Custom type arpInspectLogReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("denyStatic", 2),
          ("denyDHCP", 3),
          ("permitStatic", 4),
          ("permitDHCP", 5))
    )


_ArpInspectLogReason_Type.__name__ = "Integer32"
_ArpInspectLogReason_Object = MibTableColumn
arpInspectLogReason = _ArpInspectLogReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 6),
    _ArpInspectLogReason_Type()
)
arpInspectLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogReason.setStatus("current")
_ArpInspectLogTime_Type = DateAndTime
_ArpInspectLogTime_Object = MibTableColumn
arpInspectLogTime = _ArpInspectLogTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 4, 1, 7),
    _ArpInspectLogTime_Type()
)
arpInspectLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogTime.setStatus("current")
_ArpInspectStatisticsTable_Object = MibTable
arpInspectStatisticsTable = _ArpInspectStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5)
)
if mibBuilder.loadTexts:
    arpInspectStatisticsTable.setStatus("current")
_ArpInspectStatisticsEntry_Object = MibTableRow
arpInspectStatisticsEntry = _ArpInspectStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1)
)
arpInspectStatisticsEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "arpInspectStatisticsVid"),
)
if mibBuilder.loadTexts:
    arpInspectStatisticsEntry.setStatus("current")
_ArpInspectStatisticsVid_Type = Integer32
_ArpInspectStatisticsVid_Object = MibTableColumn
arpInspectStatisticsVid = _ArpInspectStatisticsVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 1),
    _ArpInspectStatisticsVid_Type()
)
arpInspectStatisticsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsVid.setStatus("current")
_ArpInspectStatisticsReceived_Type = Counter32
_ArpInspectStatisticsReceived_Object = MibTableColumn
arpInspectStatisticsReceived = _ArpInspectStatisticsReceived_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 2),
    _ArpInspectStatisticsReceived_Type()
)
arpInspectStatisticsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsReceived.setStatus("current")
_ArpInspectStatisticsRequest_Type = Counter32
_ArpInspectStatisticsRequest_Object = MibTableColumn
arpInspectStatisticsRequest = _ArpInspectStatisticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 3),
    _ArpInspectStatisticsRequest_Type()
)
arpInspectStatisticsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsRequest.setStatus("current")
_ArpInspectStatisticsReply_Type = Counter32
_ArpInspectStatisticsReply_Object = MibTableColumn
arpInspectStatisticsReply = _ArpInspectStatisticsReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 4),
    _ArpInspectStatisticsReply_Type()
)
arpInspectStatisticsReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsReply.setStatus("current")
_ArpInspectStatisticsForward_Type = Counter32
_ArpInspectStatisticsForward_Object = MibTableColumn
arpInspectStatisticsForward = _ArpInspectStatisticsForward_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 5),
    _ArpInspectStatisticsForward_Type()
)
arpInspectStatisticsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsForward.setStatus("current")
_ArpInspectStatisticsDrop_Type = Counter32
_ArpInspectStatisticsDrop_Object = MibTableColumn
arpInspectStatisticsDrop = _ArpInspectStatisticsDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 6),
    _ArpInspectStatisticsDrop_Type()
)
arpInspectStatisticsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsDrop.setStatus("current")
_ArpInspectStatisticsClear_Type = EnabledStatus
_ArpInspectStatisticsClear_Object = MibTableColumn
arpInspectStatisticsClear = _ArpInspectStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 51, 2, 5, 1, 7),
    _ArpInspectStatisticsClear_Type()
)
arpInspectStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectStatisticsClear.setStatus("current")
_TrTCMSetup_ObjectIdentity = ObjectIdentity
trTCMSetup = _TrTCMSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52)
)
_TrTCMState_Type = EnabledStatus
_TrTCMState_Object = MibScalar
trTCMState = _TrTCMState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 1),
    _TrTCMState_Type()
)
trTCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMState.setStatus("current")


class _TrTCMMode_Type(Integer32):
    """Custom type trTCMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 0),
          ("color-blind", 1))
    )


_TrTCMMode_Type.__name__ = "Integer32"
_TrTCMMode_Object = MibScalar
trTCMMode = _TrTCMMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 2),
    _TrTCMMode_Type()
)
trTCMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMMode.setStatus("current")
_TrTCMPortTable_Object = MibTable
trTCMPortTable = _TrTCMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3)
)
if mibBuilder.loadTexts:
    trTCMPortTable.setStatus("current")
_TrTCMPortEntry_Object = MibTableRow
trTCMPortEntry = _TrTCMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1)
)
trTCMPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    trTCMPortEntry.setStatus("current")
_TrTCMPortState_Type = EnabledStatus
_TrTCMPortState_Object = MibTableColumn
trTCMPortState = _TrTCMPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1, 1),
    _TrTCMPortState_Type()
)
trTCMPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trTCMPortState.setStatus("current")
_TrTCMPortCIR_Type = Integer32
_TrTCMPortCIR_Object = MibTableColumn
trTCMPortCIR = _TrTCMPortCIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1, 2),
    _TrTCMPortCIR_Type()
)
trTCMPortCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortCIR.setStatus("current")
_TrTCMPortPIR_Type = Integer32
_TrTCMPortPIR_Object = MibTableColumn
trTCMPortPIR = _TrTCMPortPIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1, 3),
    _TrTCMPortPIR_Type()
)
trTCMPortPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortPIR.setStatus("current")
_TrTCMPortDscpGreen_Type = Integer32
_TrTCMPortDscpGreen_Object = MibTableColumn
trTCMPortDscpGreen = _TrTCMPortDscpGreen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1, 4),
    _TrTCMPortDscpGreen_Type()
)
trTCMPortDscpGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpGreen.setStatus("current")
_TrTCMPortDscpYellow_Type = Integer32
_TrTCMPortDscpYellow_Object = MibTableColumn
trTCMPortDscpYellow = _TrTCMPortDscpYellow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1, 5),
    _TrTCMPortDscpYellow_Type()
)
trTCMPortDscpYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpYellow.setStatus("current")
_TrTCMPortDscpRed_Type = Integer32
_TrTCMPortDscpRed_Object = MibTableColumn
trTCMPortDscpRed = _TrTCMPortDscpRed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 52, 3, 1, 6),
    _TrTCMPortDscpRed_Type()
)
trTCMPortDscpRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpRed.setStatus("current")
_LoopGuardSetup_ObjectIdentity = ObjectIdentity
loopGuardSetup = _LoopGuardSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53)
)
_LoopGuardState_Type = EnabledStatus
_LoopGuardState_Object = MibScalar
loopGuardState = _LoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53, 1),
    _LoopGuardState_Type()
)
loopGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardState.setStatus("current")
_LoopGuardPortTable_Object = MibTable
loopGuardPortTable = _LoopGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53, 2)
)
if mibBuilder.loadTexts:
    loopGuardPortTable.setStatus("current")
_LoopGuardPortEntry_Object = MibTableRow
loopGuardPortEntry = _LoopGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53, 2, 1)
)
loopGuardPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    loopGuardPortEntry.setStatus("current")
_LoopGuardPortState_Type = EnabledStatus
_LoopGuardPortState_Object = MibTableColumn
loopGuardPortState = _LoopGuardPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53, 2, 1, 1),
    _LoopGuardPortState_Type()
)
loopGuardPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardPortState.setStatus("current")


class _LoopGuardPortMode_Type(Integer32):
    """Custom type loopGuardPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix", 1),
          ("dynamic", 2))
    )


_LoopGuardPortMode_Type.__name__ = "Integer32"
_LoopGuardPortMode_Object = MibTableColumn
loopGuardPortMode = _LoopGuardPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53, 2, 1, 2),
    _LoopGuardPortMode_Type()
)
loopGuardPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardPortMode.setStatus("current")
_LoopGuardPortRecoverTime_Type = Integer32
_LoopGuardPortRecoverTime_Object = MibTableColumn
loopGuardPortRecoverTime = _LoopGuardPortRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 53, 2, 1, 3),
    _LoopGuardPortRecoverTime_Type()
)
loopGuardPortRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardPortRecoverTime.setStatus("current")
_SubnetBasedVlanSetup_ObjectIdentity = ObjectIdentity
subnetBasedVlanSetup = _SubnetBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54)
)
_SubnetBasedVlanState_Type = EnabledStatus
_SubnetBasedVlanState_Object = MibScalar
subnetBasedVlanState = _SubnetBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 1),
    _SubnetBasedVlanState_Type()
)
subnetBasedVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanState.setStatus("current")
_DhcpVlanOverrideState_Type = EnabledStatus
_DhcpVlanOverrideState_Object = MibScalar
dhcpVlanOverrideState = _DhcpVlanOverrideState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 2),
    _DhcpVlanOverrideState_Type()
)
dhcpVlanOverrideState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpVlanOverrideState.setStatus("current")
_SubnetBasedVlanTable_Object = MibTable
subnetBasedVlanTable = _SubnetBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3)
)
if mibBuilder.loadTexts:
    subnetBasedVlanTable.setStatus("current")
_SubnetBasedVlanEntry_Object = MibTableRow
subnetBasedVlanEntry = _SubnetBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1)
)
subnetBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "subnetBasedVlanSrcIp"),
    (0, "ZYXEL-ves1608FE57-MIB", "subnetBasedVlanSrcMaskBit"),
)
if mibBuilder.loadTexts:
    subnetBasedVlanEntry.setStatus("current")
_SubnetBasedVlanSrcIp_Type = IpAddress
_SubnetBasedVlanSrcIp_Object = MibTableColumn
subnetBasedVlanSrcIp = _SubnetBasedVlanSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1, 1),
    _SubnetBasedVlanSrcIp_Type()
)
subnetBasedVlanSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanSrcIp.setStatus("current")


class _SubnetBasedVlanSrcMaskBit_Type(Integer32):
    """Custom type subnetBasedVlanSrcMaskBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SubnetBasedVlanSrcMaskBit_Type.__name__ = "Integer32"
_SubnetBasedVlanSrcMaskBit_Object = MibTableColumn
subnetBasedVlanSrcMaskBit = _SubnetBasedVlanSrcMaskBit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1, 2),
    _SubnetBasedVlanSrcMaskBit_Type()
)
subnetBasedVlanSrcMaskBit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanSrcMaskBit.setStatus("current")


class _SubnetBasedVlanName_Type(DisplayString):
    """Custom type subnetBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubnetBasedVlanName_Type.__name__ = "DisplayString"
_SubnetBasedVlanName_Object = MibTableColumn
subnetBasedVlanName = _SubnetBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1, 3),
    _SubnetBasedVlanName_Type()
)
subnetBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanName.setStatus("current")


class _SubnetBasedVlanVid_Type(Integer32):
    """Custom type subnetBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SubnetBasedVlanVid_Type.__name__ = "Integer32"
_SubnetBasedVlanVid_Object = MibTableColumn
subnetBasedVlanVid = _SubnetBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1, 4),
    _SubnetBasedVlanVid_Type()
)
subnetBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanVid.setStatus("current")


class _SubnetBasedVlanPriority_Type(Integer32):
    """Custom type subnetBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SubnetBasedVlanPriority_Type.__name__ = "Integer32"
_SubnetBasedVlanPriority_Object = MibTableColumn
subnetBasedVlanPriority = _SubnetBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1, 5),
    _SubnetBasedVlanPriority_Type()
)
subnetBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanPriority.setStatus("current")
_SubnetBasedVlanEntryState_Type = RowStatus
_SubnetBasedVlanEntryState_Object = MibTableColumn
subnetBasedVlanEntryState = _SubnetBasedVlanEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 3, 1, 6),
    _SubnetBasedVlanEntryState_Type()
)
subnetBasedVlanEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetBasedVlanEntryState.setStatus("current")
_SubnetBasedVlanInfoTable_Object = MibTable
subnetBasedVlanInfoTable = _SubnetBasedVlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4)
)
if mibBuilder.loadTexts:
    subnetBasedVlanInfoTable.setStatus("current")
_SubnetBasedVlanInfoEntry_Object = MibTableRow
subnetBasedVlanInfoEntry = _SubnetBasedVlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1)
)
subnetBasedVlanInfoEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "subnetBasedVlanInfoSrcIpType"),
    (0, "ZYXEL-ves1608FE57-MIB", "subnetBasedVlanInfoSrcIp"),
    (0, "ZYXEL-ves1608FE57-MIB", "subnetBasedVlanInfoSrcMaskBit"),
)
if mibBuilder.loadTexts:
    subnetBasedVlanInfoEntry.setStatus("current")


class _SubnetBasedVlanInfoSrcIpType_Type(InetAddressType):
    """Custom type subnetBasedVlanInfoSrcIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SubnetBasedVlanInfoSrcIpType_Type.__name__ = "InetAddressType"
_SubnetBasedVlanInfoSrcIpType_Object = MibTableColumn
subnetBasedVlanInfoSrcIpType = _SubnetBasedVlanInfoSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 1),
    _SubnetBasedVlanInfoSrcIpType_Type()
)
subnetBasedVlanInfoSrcIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoSrcIpType.setStatus("current")
_SubnetBasedVlanInfoSrcIp_Type = InetAddress
_SubnetBasedVlanInfoSrcIp_Object = MibTableColumn
subnetBasedVlanInfoSrcIp = _SubnetBasedVlanInfoSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 2),
    _SubnetBasedVlanInfoSrcIp_Type()
)
subnetBasedVlanInfoSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoSrcIp.setStatus("current")


class _SubnetBasedVlanInfoSrcMaskBit_Type(Integer32):
    """Custom type subnetBasedVlanInfoSrcMaskBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SubnetBasedVlanInfoSrcMaskBit_Type.__name__ = "Integer32"
_SubnetBasedVlanInfoSrcMaskBit_Object = MibTableColumn
subnetBasedVlanInfoSrcMaskBit = _SubnetBasedVlanInfoSrcMaskBit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 3),
    _SubnetBasedVlanInfoSrcMaskBit_Type()
)
subnetBasedVlanInfoSrcMaskBit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoSrcMaskBit.setStatus("current")


class _SubnetBasedVlanInfoName_Type(DisplayString):
    """Custom type subnetBasedVlanInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubnetBasedVlanInfoName_Type.__name__ = "DisplayString"
_SubnetBasedVlanInfoName_Object = MibTableColumn
subnetBasedVlanInfoName = _SubnetBasedVlanInfoName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 4),
    _SubnetBasedVlanInfoName_Type()
)
subnetBasedVlanInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoName.setStatus("current")


class _SubnetBasedVlanInfoVid_Type(Integer32):
    """Custom type subnetBasedVlanInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SubnetBasedVlanInfoVid_Type.__name__ = "Integer32"
_SubnetBasedVlanInfoVid_Object = MibTableColumn
subnetBasedVlanInfoVid = _SubnetBasedVlanInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 5),
    _SubnetBasedVlanInfoVid_Type()
)
subnetBasedVlanInfoVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoVid.setStatus("current")


class _SubnetBasedVlanInfoPriority_Type(Integer32):
    """Custom type subnetBasedVlanInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SubnetBasedVlanInfoPriority_Type.__name__ = "Integer32"
_SubnetBasedVlanInfoPriority_Object = MibTableColumn
subnetBasedVlanInfoPriority = _SubnetBasedVlanInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 6),
    _SubnetBasedVlanInfoPriority_Type()
)
subnetBasedVlanInfoPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoPriority.setStatus("current")
_SubnetBasedVlanInfoEntryState_Type = RowStatus
_SubnetBasedVlanInfoEntryState_Object = MibTableColumn
subnetBasedVlanInfoEntryState = _SubnetBasedVlanInfoEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 54, 4, 1, 7),
    _SubnetBasedVlanInfoEntryState_Type()
)
subnetBasedVlanInfoEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetBasedVlanInfoEntryState.setStatus("current")
_MacAuthenticationSetup_ObjectIdentity = ObjectIdentity
macAuthenticationSetup = _MacAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55)
)
_MacAuthenticationState_Type = EnabledStatus
_MacAuthenticationState_Object = MibScalar
macAuthenticationState = _MacAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 1),
    _MacAuthenticationState_Type()
)
macAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationState.setStatus("current")
_MacAuthenticationNamePrefix_Type = DisplayString
_MacAuthenticationNamePrefix_Object = MibScalar
macAuthenticationNamePrefix = _MacAuthenticationNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 2),
    _MacAuthenticationNamePrefix_Type()
)
macAuthenticationNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationNamePrefix.setStatus("current")
_MacAuthenticationPassword_Type = DisplayString
_MacAuthenticationPassword_Object = MibScalar
macAuthenticationPassword = _MacAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 3),
    _MacAuthenticationPassword_Type()
)
macAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationPassword.setStatus("current")
_MacAuthenticationTimeout_Type = Integer32
_MacAuthenticationTimeout_Object = MibScalar
macAuthenticationTimeout = _MacAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 4),
    _MacAuthenticationTimeout_Type()
)
macAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationTimeout.setStatus("current")
_MacAuthenticationPortTable_Object = MibTable
macAuthenticationPortTable = _MacAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 5)
)
if mibBuilder.loadTexts:
    macAuthenticationPortTable.setStatus("current")
_MacAuthenticationPortEntry_Object = MibTableRow
macAuthenticationPortEntry = _MacAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 5, 1)
)
macAuthenticationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    macAuthenticationPortEntry.setStatus("current")
_MacAuthenticationPortState_Type = EnabledStatus
_MacAuthenticationPortState_Object = MibTableColumn
macAuthenticationPortState = _MacAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 55, 5, 1, 1),
    _MacAuthenticationPortState_Type()
)
macAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationPortState.setStatus("current")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56)
)
_MstpGen_ObjectIdentity = ObjectIdentity
mstpGen = _MstpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1)
)
_MstpGenState_Type = EnabledStatus
_MstpGenState_Object = MibScalar
mstpGenState = _MstpGenState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 1),
    _MstpGenState_Type()
)
mstpGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenState.setStatus("current")
_MstpGenCfgIdName_Type = DisplayString
_MstpGenCfgIdName_Object = MibScalar
mstpGenCfgIdName = _MstpGenCfgIdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 2),
    _MstpGenCfgIdName_Type()
)
mstpGenCfgIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdName.setStatus("current")
_MstpGenCfgIdRevLevel_Type = Integer32
_MstpGenCfgIdRevLevel_Object = MibScalar
mstpGenCfgIdRevLevel = _MstpGenCfgIdRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 3),
    _MstpGenCfgIdRevLevel_Type()
)
mstpGenCfgIdRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdRevLevel.setStatus("current")


class _MstpGenCfgIdCfgDigest_Type(OctetString):
    """Custom type mstpGenCfgIdCfgDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_MstpGenCfgIdCfgDigest_Type.__name__ = "OctetString"
_MstpGenCfgIdCfgDigest_Object = MibScalar
mstpGenCfgIdCfgDigest = _MstpGenCfgIdCfgDigest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 4),
    _MstpGenCfgIdCfgDigest_Type()
)
mstpGenCfgIdCfgDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCfgIdCfgDigest.setStatus("current")


class _MstpGenHelloTime_Type(Timeout):
    """Custom type mstpGenHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MstpGenHelloTime_Type.__name__ = "Timeout"
_MstpGenHelloTime_Object = MibScalar
mstpGenHelloTime = _MstpGenHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 5),
    _MstpGenHelloTime_Type()
)
mstpGenHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenHelloTime.setStatus("current")


class _MstpGenMaxAge_Type(Timeout):
    """Custom type mstpGenMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_MstpGenMaxAge_Type.__name__ = "Timeout"
_MstpGenMaxAge_Object = MibScalar
mstpGenMaxAge = _MstpGenMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 6),
    _MstpGenMaxAge_Type()
)
mstpGenMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxAge.setStatus("current")


class _MstpGenForwardDelay_Type(Timeout):
    """Custom type mstpGenForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstpGenForwardDelay_Type.__name__ = "Timeout"
_MstpGenForwardDelay_Object = MibScalar
mstpGenForwardDelay = _MstpGenForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 7),
    _MstpGenForwardDelay_Type()
)
mstpGenForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenForwardDelay.setStatus("current")


class _MstpGenMaxHops_Type(Integer32):
    """Custom type mstpGenMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MstpGenMaxHops_Type.__name__ = "Integer32"
_MstpGenMaxHops_Object = MibScalar
mstpGenMaxHops = _MstpGenMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 8),
    _MstpGenMaxHops_Type()
)
mstpGenMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxHops.setStatus("current")
_MstpGenCistRootPathCost_Type = Integer32
_MstpGenCistRootPathCost_Object = MibScalar
mstpGenCistRootPathCost = _MstpGenCistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 9),
    _MstpGenCistRootPathCost_Type()
)
mstpGenCistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootPathCost.setStatus("current")


class _MstpGenCistRootBrid_Type(OctetString):
    """Custom type mstpGenCistRootBrid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_MstpGenCistRootBrid_Type.__name__ = "OctetString"
_MstpGenCistRootBrid_Object = MibScalar
mstpGenCistRootBrid = _MstpGenCistRootBrid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 1, 10),
    _MstpGenCistRootBrid_Type()
)
mstpGenCistRootBrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootBrid.setStatus("current")
_MstMapTable_Object = MibTable
mstMapTable = _MstMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20)
)
if mibBuilder.loadTexts:
    mstMapTable.setStatus("current")
_MstMapEntry_Object = MibTableRow
mstMapEntry = _MstMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1)
)
mstMapEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mstMapIndex"),
)
if mibBuilder.loadTexts:
    mstMapEntry.setStatus("current")
_MstMapIndex_Type = MstiOrCistInstanceIndex
_MstMapIndex_Object = MibTableColumn
mstMapIndex = _MstMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1, 1),
    _MstMapIndex_Type()
)
mstMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstMapIndex.setStatus("current")


class _MstMapVlans1k_Type(OctetString):
    """Custom type mstMapVlans1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans1k_Type.__name__ = "OctetString"
_MstMapVlans1k_Object = MibTableColumn
mstMapVlans1k = _MstMapVlans1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1, 2),
    _MstMapVlans1k_Type()
)
mstMapVlans1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans1k.setStatus("current")


class _MstMapVlans2k_Type(OctetString):
    """Custom type mstMapVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans2k_Type.__name__ = "OctetString"
_MstMapVlans2k_Object = MibTableColumn
mstMapVlans2k = _MstMapVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1, 3),
    _MstMapVlans2k_Type()
)
mstMapVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans2k.setStatus("current")


class _MstMapVlans3k_Type(OctetString):
    """Custom type mstMapVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans3k_Type.__name__ = "OctetString"
_MstMapVlans3k_Object = MibTableColumn
mstMapVlans3k = _MstMapVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1, 4),
    _MstMapVlans3k_Type()
)
mstMapVlans3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans3k.setStatus("current")


class _MstMapVlans4k_Type(OctetString):
    """Custom type mstMapVlans4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans4k_Type.__name__ = "OctetString"
_MstMapVlans4k_Object = MibTableColumn
mstMapVlans4k = _MstMapVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1, 5),
    _MstMapVlans4k_Type()
)
mstMapVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans4k.setStatus("current")
_MstMapRowStatus_Type = RowStatus
_MstMapRowStatus_Object = MibTableColumn
mstMapRowStatus = _MstMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 20, 1, 6),
    _MstMapRowStatus_Type()
)
mstMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstMapRowStatus.setStatus("current")
_MstVlanTable_Object = MibTable
mstVlanTable = _MstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 30)
)
if mibBuilder.loadTexts:
    mstVlanTable.setStatus("current")
_MstVlanEntry_Object = MibTableRow
mstVlanEntry = _MstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 30, 1)
)
mstVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mstVlanIndex"),
)
if mibBuilder.loadTexts:
    mstVlanEntry.setStatus("current")


class _MstVlanIndex_Type(Integer32):
    """Custom type mstVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MstVlanIndex_Type.__name__ = "Integer32"
_MstVlanIndex_Object = MibTableColumn
mstVlanIndex = _MstVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 30, 1, 1),
    _MstVlanIndex_Type()
)
mstVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstVlanIndex.setStatus("current")
_MstVlanMstIndex_Type = MstiOrCistInstanceIndex
_MstVlanMstIndex_Object = MibTableColumn
mstVlanMstIndex = _MstVlanMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 30, 1, 2),
    _MstVlanMstIndex_Type()
)
mstVlanMstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstVlanMstIndex.setStatus("current")
_MstpPortTable_Object = MibTable
mstpPortTable = _MstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 40)
)
if mibBuilder.loadTexts:
    mstpPortTable.setStatus("current")
_MstpPortEntry_Object = MibTableRow
mstpPortEntry = _MstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 40, 1)
)
mstpPortEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mstpPortIndex"),
)
if mibBuilder.loadTexts:
    mstpPortEntry.setStatus("current")


class _MstpPortIndex_Type(Integer32):
    """Custom type mstpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpPortIndex_Type.__name__ = "Integer32"
_MstpPortIndex_Object = MibTableColumn
mstpPortIndex = _MstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 40, 1, 1),
    _MstpPortIndex_Type()
)
mstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpPortIndex.setStatus("current")
_MstpPortOperEdgePort_Type = TruthValue
_MstpPortOperEdgePort_Object = MibTableColumn
mstpPortOperEdgePort = _MstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 40, 1, 2),
    _MstpPortOperEdgePort_Type()
)
mstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperEdgePort.setStatus("current")
_MstpPortOperPointToPointMAC_Type = TruthValue
_MstpPortOperPointToPointMAC_Object = MibTableColumn
mstpPortOperPointToPointMAC = _MstpPortOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 40, 1, 3),
    _MstpPortOperPointToPointMAC_Type()
)
mstpPortOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperPointToPointMAC.setStatus("current")
_MstpXstTable_Object = MibTable
mstpXstTable = _MstpXstTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50)
)
if mibBuilder.loadTexts:
    mstpXstTable.setStatus("current")
_MstpXstEntry_Object = MibTableRow
mstpXstEntry = _MstpXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1)
)
mstpXstEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mstpXstId"),
)
if mibBuilder.loadTexts:
    mstpXstEntry.setStatus("current")
_MstpXstId_Type = MstiOrCistInstanceIndex
_MstpXstId_Object = MibTableColumn
mstpXstId = _MstpXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 1),
    _MstpXstId_Type()
)
mstpXstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstId.setStatus("current")


class _MstpXstBridgePriority_Type(Integer32):
    """Custom type mstpXstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstpXstBridgePriority_Type.__name__ = "Integer32"
_MstpXstBridgePriority_Object = MibTableColumn
mstpXstBridgePriority = _MstpXstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 2),
    _MstpXstBridgePriority_Type()
)
mstpXstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstBridgePriority.setStatus("current")
_MstpXstBridgeId_Type = BridgeId
_MstpXstBridgeId_Object = MibTableColumn
mstpXstBridgeId = _MstpXstBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 3),
    _MstpXstBridgeId_Type()
)
mstpXstBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstBridgeId.setStatus("current")
_MstpXstInternalRootCost_Type = Integer32
_MstpXstInternalRootCost_Object = MibTableColumn
mstpXstInternalRootCost = _MstpXstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 4),
    _MstpXstInternalRootCost_Type()
)
mstpXstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstInternalRootCost.setStatus("current")
_MstpXstRootPort_Type = Integer32
_MstpXstRootPort_Object = MibTableColumn
mstpXstRootPort = _MstpXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 5),
    _MstpXstRootPort_Type()
)
mstpXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstRootPort.setStatus("current")
_MstpXstTimeSinceTopologyChange_Type = TimeTicks
_MstpXstTimeSinceTopologyChange_Object = MibTableColumn
mstpXstTimeSinceTopologyChange = _MstpXstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 6),
    _MstpXstTimeSinceTopologyChange_Type()
)
mstpXstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTimeSinceTopologyChange.setStatus("current")
_MstpXstTopologyChangesCount_Type = Counter32
_MstpXstTopologyChangesCount_Object = MibTableColumn
mstpXstTopologyChangesCount = _MstpXstTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 50, 1, 7),
    _MstpXstTopologyChangesCount_Type()
)
mstpXstTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTopologyChangesCount.setStatus("current")
_MstpXstPortTable_Object = MibTable
mstpXstPortTable = _MstpXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60)
)
if mibBuilder.loadTexts:
    mstpXstPortTable.setStatus("current")
_MstpXstPortEntry_Object = MibTableRow
mstpXstPortEntry = _MstpXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1)
)
mstpXstPortEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "mstpXstPortXstId"),
    (0, "ZYXEL-ves1608FE57-MIB", "mstpXstPortIndex"),
)
if mibBuilder.loadTexts:
    mstpXstPortEntry.setStatus("current")
_MstpXstPortXstId_Type = MstiOrCistInstanceIndex
_MstpXstPortXstId_Object = MibTableColumn
mstpXstPortXstId = _MstpXstPortXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 1),
    _MstpXstPortXstId_Type()
)
mstpXstPortXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpXstPortXstId.setStatus("current")


class _MstpXstPortIndex_Type(Integer32):
    """Custom type mstpXstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpXstPortIndex_Type.__name__ = "Integer32"
_MstpXstPortIndex_Object = MibTableColumn
mstpXstPortIndex = _MstpXstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 2),
    _MstpXstPortIndex_Type()
)
mstpXstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortIndex.setStatus("current")
_MstpXstPortEnable_Type = EnabledStatus
_MstpXstPortEnable_Object = MibTableColumn
mstpXstPortEnable = _MstpXstPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 3),
    _MstpXstPortEnable_Type()
)
mstpXstPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortEnable.setStatus("current")


class _MstpXstPortPriority_Type(Integer32):
    """Custom type mstpXstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MstpXstPortPriority_Type.__name__ = "Integer32"
_MstpXstPortPriority_Object = MibTableColumn
mstpXstPortPriority = _MstpXstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 4),
    _MstpXstPortPriority_Type()
)
mstpXstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPriority.setStatus("current")


class _MstpXstPortPathCost_Type(Integer32):
    """Custom type mstpXstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpXstPortPathCost_Type.__name__ = "Integer32"
_MstpXstPortPathCost_Object = MibTableColumn
mstpXstPortPathCost = _MstpXstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 5),
    _MstpXstPortPathCost_Type()
)
mstpXstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPathCost.setStatus("current")


class _MstpXstPortState_Type(Integer32):
    """Custom type mstpXstPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("unknown", 4))
    )


_MstpXstPortState_Type.__name__ = "Integer32"
_MstpXstPortState_Object = MibTableColumn
mstpXstPortState = _MstpXstPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 6),
    _MstpXstPortState_Type()
)
mstpXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortState.setStatus("current")
_MstpXstPortDesignatedRoot_Type = BridgeId
_MstpXstPortDesignatedRoot_Object = MibTableColumn
mstpXstPortDesignatedRoot = _MstpXstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 7),
    _MstpXstPortDesignatedRoot_Type()
)
mstpXstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedRoot.setStatus("current")
_MstpXstPortDesignatedCost_Type = Integer32
_MstpXstPortDesignatedCost_Object = MibTableColumn
mstpXstPortDesignatedCost = _MstpXstPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 8),
    _MstpXstPortDesignatedCost_Type()
)
mstpXstPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedCost.setStatus("current")
_MstpXstPortDesignatedBridge_Type = BridgeId
_MstpXstPortDesignatedBridge_Object = MibTableColumn
mstpXstPortDesignatedBridge = _MstpXstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 9),
    _MstpXstPortDesignatedBridge_Type()
)
mstpXstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedBridge.setStatus("current")
_MstpXstPortDesignatedPort_Type = Integer32
_MstpXstPortDesignatedPort_Object = MibTableColumn
mstpXstPortDesignatedPort = _MstpXstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 60, 1, 10),
    _MstpXstPortDesignatedPort_Type()
)
mstpXstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedPort.setStatus("current")
_MstpNotifications_ObjectIdentity = ObjectIdentity
mstpNotifications = _MstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 70)
)
_RadiusServerSetup_ObjectIdentity = ObjectIdentity
radiusServerSetup = _RadiusServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57)
)
_RadiusAuthServerSetup_ObjectIdentity = ObjectIdentity
radiusAuthServerSetup = _RadiusAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1)
)


class _RadiusAuthServerMode_Type(Integer32):
    """Custom type radiusAuthServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-priority", 1),
          ("round-robin", 2))
    )


_RadiusAuthServerMode_Type.__name__ = "Integer32"
_RadiusAuthServerMode_Object = MibScalar
radiusAuthServerMode = _RadiusAuthServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 1),
    _RadiusAuthServerMode_Type()
)
radiusAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerMode.setStatus("current")
_RadiusAuthServerTimeout_Type = Integer32
_RadiusAuthServerTimeout_Object = MibScalar
radiusAuthServerTimeout = _RadiusAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 2),
    _RadiusAuthServerTimeout_Type()
)
radiusAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerTimeout.setStatus("current")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("current")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("current")
_RadiusAuthServerIndex_Type = Integer32
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("current")
_RadiusAuthServerIpAddr_Type = IpAddress
_RadiusAuthServerIpAddr_Object = MibTableColumn
radiusAuthServerIpAddr = _RadiusAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1, 2),
    _RadiusAuthServerIpAddr_Type()
)
radiusAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerIpAddr.setStatus("current")
_RadiusAuthServerUdpPort_Type = Integer32
_RadiusAuthServerUdpPort_Object = MibTableColumn
radiusAuthServerUdpPort = _RadiusAuthServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1, 3),
    _RadiusAuthServerUdpPort_Type()
)
radiusAuthServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerUdpPort.setStatus("current")
_RadiusAuthServerSharedSecret_Type = DisplayString
_RadiusAuthServerSharedSecret_Object = MibTableColumn
radiusAuthServerSharedSecret = _RadiusAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1, 4),
    _RadiusAuthServerSharedSecret_Type()
)
radiusAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerSharedSecret.setStatus("current")


class _RadiusAuthServerIpAddressType_Type(InetAddressType):
    """Custom type radiusAuthServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RadiusAuthServerIpAddressType_Type.__name__ = "InetAddressType"
_RadiusAuthServerIpAddressType_Object = MibTableColumn
radiusAuthServerIpAddressType = _RadiusAuthServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1, 5),
    _RadiusAuthServerIpAddressType_Type()
)
radiusAuthServerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServerIpAddressType.setStatus("current")
_RadiusAuthServerIpAddress_Type = InetAddress
_RadiusAuthServerIpAddress_Object = MibTableColumn
radiusAuthServerIpAddress = _RadiusAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 1, 3, 1, 6),
    _RadiusAuthServerIpAddress_Type()
)
radiusAuthServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerIpAddress.setStatus("current")
_RadiusAcctServerSetup_ObjectIdentity = ObjectIdentity
radiusAcctServerSetup = _RadiusAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2)
)
_RadiusAcctServerTimeout_Type = Integer32
_RadiusAcctServerTimeout_Object = MibScalar
radiusAcctServerTimeout = _RadiusAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 1),
    _RadiusAcctServerTimeout_Type()
)
radiusAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerTimeout.setStatus("current")
_RadiusAcctServerTable_Object = MibTable
radiusAcctServerTable = _RadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2)
)
if mibBuilder.loadTexts:
    radiusAcctServerTable.setStatus("current")
_RadiusAcctServerEntry_Object = MibTableRow
radiusAcctServerEntry = _RadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1)
)
radiusAcctServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "radiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAcctServerEntry.setStatus("current")
_RadiusAcctServerIndex_Type = Integer32
_RadiusAcctServerIndex_Object = MibTableColumn
radiusAcctServerIndex = _RadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1, 1),
    _RadiusAcctServerIndex_Type()
)
radiusAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAcctServerIndex.setStatus("current")
_RadiusAcctServerIpAddr_Type = IpAddress
_RadiusAcctServerIpAddr_Object = MibTableColumn
radiusAcctServerIpAddr = _RadiusAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1, 2),
    _RadiusAcctServerIpAddr_Type()
)
radiusAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerIpAddr.setStatus("current")
_RadiusAcctServerUdpPort_Type = Integer32
_RadiusAcctServerUdpPort_Object = MibTableColumn
radiusAcctServerUdpPort = _RadiusAcctServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1, 3),
    _RadiusAcctServerUdpPort_Type()
)
radiusAcctServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerUdpPort.setStatus("current")
_RadiusAcctServerSharedSecret_Type = DisplayString
_RadiusAcctServerSharedSecret_Object = MibTableColumn
radiusAcctServerSharedSecret = _RadiusAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1, 4),
    _RadiusAcctServerSharedSecret_Type()
)
radiusAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerSharedSecret.setStatus("current")


class _RadiusAcctServerIpAddressType_Type(InetAddressType):
    """Custom type radiusAcctServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RadiusAcctServerIpAddressType_Type.__name__ = "InetAddressType"
_RadiusAcctServerIpAddressType_Object = MibTableColumn
radiusAcctServerIpAddressType = _RadiusAcctServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1, 5),
    _RadiusAcctServerIpAddressType_Type()
)
radiusAcctServerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctServerIpAddressType.setStatus("current")
_RadiusAcctServerIpAddress_Type = InetAddress
_RadiusAcctServerIpAddress_Object = MibTableColumn
radiusAcctServerIpAddress = _RadiusAcctServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 57, 2, 2, 1, 6),
    _RadiusAcctServerIpAddress_Type()
)
radiusAcctServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerIpAddress.setStatus("current")
_TacacsServerSetup_ObjectIdentity = ObjectIdentity
tacacsServerSetup = _TacacsServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58)
)
_TacacsAuthServerSetup_ObjectIdentity = ObjectIdentity
tacacsAuthServerSetup = _TacacsAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1)
)


class _TacacsAuthServerMode_Type(Integer32):
    """Custom type tacacsAuthServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-priority", 1),
          ("round-robin", 2))
    )


_TacacsAuthServerMode_Type.__name__ = "Integer32"
_TacacsAuthServerMode_Object = MibScalar
tacacsAuthServerMode = _TacacsAuthServerMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 1),
    _TacacsAuthServerMode_Type()
)
tacacsAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerMode.setStatus("current")
_TacacsAuthServerTimeout_Type = Integer32
_TacacsAuthServerTimeout_Object = MibScalar
tacacsAuthServerTimeout = _TacacsAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 2),
    _TacacsAuthServerTimeout_Type()
)
tacacsAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTimeout.setStatus("current")
_TacacsAuthServerTable_Object = MibTable
tacacsAuthServerTable = _TacacsAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3)
)
if mibBuilder.loadTexts:
    tacacsAuthServerTable.setStatus("current")
_TacacsAuthServerEntry_Object = MibTableRow
tacacsAuthServerEntry = _TacacsAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1)
)
tacacsAuthServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "tacacsAuthServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAuthServerEntry.setStatus("current")
_TacacsAuthServerIndex_Type = Integer32
_TacacsAuthServerIndex_Object = MibTableColumn
tacacsAuthServerIndex = _TacacsAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1, 1),
    _TacacsAuthServerIndex_Type()
)
tacacsAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAuthServerIndex.setStatus("current")
_TacacsAuthServerIpAddr_Type = IpAddress
_TacacsAuthServerIpAddr_Object = MibTableColumn
tacacsAuthServerIpAddr = _TacacsAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1, 2),
    _TacacsAuthServerIpAddr_Type()
)
tacacsAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerIpAddr.setStatus("current")
_TacacsAuthServerTcpPort_Type = Integer32
_TacacsAuthServerTcpPort_Object = MibTableColumn
tacacsAuthServerTcpPort = _TacacsAuthServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1, 3),
    _TacacsAuthServerTcpPort_Type()
)
tacacsAuthServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTcpPort.setStatus("current")
_TacacsAuthServerSharedSecret_Type = DisplayString
_TacacsAuthServerSharedSecret_Object = MibTableColumn
tacacsAuthServerSharedSecret = _TacacsAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1, 4),
    _TacacsAuthServerSharedSecret_Type()
)
tacacsAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerSharedSecret.setStatus("current")


class _TacacsAuthServerIpAddressType_Type(InetAddressType):
    """Custom type tacacsAuthServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_TacacsAuthServerIpAddressType_Type.__name__ = "InetAddressType"
_TacacsAuthServerIpAddressType_Object = MibTableColumn
tacacsAuthServerIpAddressType = _TacacsAuthServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1, 5),
    _TacacsAuthServerIpAddressType_Type()
)
tacacsAuthServerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsAuthServerIpAddressType.setStatus("current")
_TacacsAuthServerIpAddress_Type = InetAddress
_TacacsAuthServerIpAddress_Object = MibTableColumn
tacacsAuthServerIpAddress = _TacacsAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 1, 3, 1, 6),
    _TacacsAuthServerIpAddress_Type()
)
tacacsAuthServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerIpAddress.setStatus("current")
_TacacsAcctServerSetup_ObjectIdentity = ObjectIdentity
tacacsAcctServerSetup = _TacacsAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2)
)
_TacacsAcctServerTimeout_Type = Integer32
_TacacsAcctServerTimeout_Object = MibScalar
tacacsAcctServerTimeout = _TacacsAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 1),
    _TacacsAcctServerTimeout_Type()
)
tacacsAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTimeout.setStatus("current")
_TacacsAcctServerTable_Object = MibTable
tacacsAcctServerTable = _TacacsAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2)
)
if mibBuilder.loadTexts:
    tacacsAcctServerTable.setStatus("current")
_TacacsAcctServerEntry_Object = MibTableRow
tacacsAcctServerEntry = _TacacsAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1)
)
tacacsAcctServerEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "tacacsAcctServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAcctServerEntry.setStatus("current")
_TacacsAcctServerIndex_Type = Integer32
_TacacsAcctServerIndex_Object = MibTableColumn
tacacsAcctServerIndex = _TacacsAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1, 1),
    _TacacsAcctServerIndex_Type()
)
tacacsAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAcctServerIndex.setStatus("current")
_TacacsAcctServerIpAddr_Type = IpAddress
_TacacsAcctServerIpAddr_Object = MibTableColumn
tacacsAcctServerIpAddr = _TacacsAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1, 2),
    _TacacsAcctServerIpAddr_Type()
)
tacacsAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerIpAddr.setStatus("current")
_TacacsAcctServerTcpPort_Type = Integer32
_TacacsAcctServerTcpPort_Object = MibTableColumn
tacacsAcctServerTcpPort = _TacacsAcctServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1, 3),
    _TacacsAcctServerTcpPort_Type()
)
tacacsAcctServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTcpPort.setStatus("current")
_TacacsAcctServerSharedSecret_Type = DisplayString
_TacacsAcctServerSharedSecret_Object = MibTableColumn
tacacsAcctServerSharedSecret = _TacacsAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1, 4),
    _TacacsAcctServerSharedSecret_Type()
)
tacacsAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerSharedSecret.setStatus("current")


class _TacacsAcctServerIpAddressType_Type(InetAddressType):
    """Custom type tacacsAcctServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_TacacsAcctServerIpAddressType_Type.__name__ = "InetAddressType"
_TacacsAcctServerIpAddressType_Object = MibTableColumn
tacacsAcctServerIpAddressType = _TacacsAcctServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1, 5),
    _TacacsAcctServerIpAddressType_Type()
)
tacacsAcctServerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsAcctServerIpAddressType.setStatus("current")
_TacacsAcctServerIpAddress_Type = InetAddress
_TacacsAcctServerIpAddress_Object = MibTableColumn
tacacsAcctServerIpAddress = _TacacsAcctServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 58, 2, 2, 1, 6),
    _TacacsAcctServerIpAddress_Type()
)
tacacsAcctServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerIpAddress.setStatus("current")
_AaaSetup_ObjectIdentity = ObjectIdentity
aaaSetup = _AaaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59)
)
_AuthenticationSetup_ObjectIdentity = ObjectIdentity
authenticationSetup = _AuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 1)
)
_AuthenticationTypeTable_Object = MibTable
authenticationTypeTable = _AuthenticationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 1, 1)
)
if mibBuilder.loadTexts:
    authenticationTypeTable.setStatus("current")
_AuthenticationTypeEntry_Object = MibTableRow
authenticationTypeEntry = _AuthenticationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 1, 1, 1)
)
authenticationTypeEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "authenticationTypeName"),
)
if mibBuilder.loadTexts:
    authenticationTypeEntry.setStatus("current")
_AuthenticationTypeName_Type = DisplayString
_AuthenticationTypeName_Object = MibTableColumn
authenticationTypeName = _AuthenticationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 1, 1, 1, 1),
    _AuthenticationTypeName_Type()
)
authenticationTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationTypeName.setStatus("current")
_AuthenticationTypeMethodList_Type = OctetString
_AuthenticationTypeMethodList_Object = MibTableColumn
authenticationTypeMethodList = _AuthenticationTypeMethodList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 1, 1, 1, 2),
    _AuthenticationTypeMethodList_Type()
)
authenticationTypeMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationTypeMethodList.setStatus("current")
_AccountingSetup_ObjectIdentity = ObjectIdentity
accountingSetup = _AccountingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2)
)
_AccountingUpdatePeriod_Type = Integer32
_AccountingUpdatePeriod_Object = MibScalar
accountingUpdatePeriod = _AccountingUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 1),
    _AccountingUpdatePeriod_Type()
)
accountingUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingUpdatePeriod.setStatus("current")
_AccountingTypeTable_Object = MibTable
accountingTypeTable = _AccountingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2)
)
if mibBuilder.loadTexts:
    accountingTypeTable.setStatus("current")
_AccountingTypeEntry_Object = MibTableRow
accountingTypeEntry = _AccountingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1)
)
accountingTypeEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "accountingTypeName"),
)
if mibBuilder.loadTexts:
    accountingTypeEntry.setStatus("current")
_AccountingTypeName_Type = DisplayString
_AccountingTypeName_Object = MibTableColumn
accountingTypeName = _AccountingTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1, 1),
    _AccountingTypeName_Type()
)
accountingTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingTypeName.setStatus("current")
_AccountingTypeActive_Type = EnabledStatus
_AccountingTypeActive_Object = MibTableColumn
accountingTypeActive = _AccountingTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1, 2),
    _AccountingTypeActive_Type()
)
accountingTypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeActive.setStatus("current")
_AccountingTypeBroadcast_Type = EnabledStatus
_AccountingTypeBroadcast_Object = MibTableColumn
accountingTypeBroadcast = _AccountingTypeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1, 3),
    _AccountingTypeBroadcast_Type()
)
accountingTypeBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeBroadcast.setStatus("current")


class _AccountingTypeMode_Type(Integer32):
    """Custom type accountingTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("start-stop", 1),
          ("stop-only", 2),
          ("not-available", 255))
    )


_AccountingTypeMode_Type.__name__ = "Integer32"
_AccountingTypeMode_Object = MibTableColumn
accountingTypeMode = _AccountingTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1, 4),
    _AccountingTypeMode_Type()
)
accountingTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeMode.setStatus("current")


class _AccountingTypeMethod_Type(Integer32):
    """Custom type accountingTypeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_AccountingTypeMethod_Type.__name__ = "Integer32"
_AccountingTypeMethod_Object = MibTableColumn
accountingTypeMethod = _AccountingTypeMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1, 5),
    _AccountingTypeMethod_Type()
)
accountingTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeMethod.setStatus("current")


class _AccountingTypePrivilege_Type(Integer32):
    """Custom type accountingTypePrivilege based on Integer32"""
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
              12,
              13,
              14,
              255)
        )
    )
    namedValues = NamedValues(
        *(("privilege-0", 0),
          ("privilege-1", 1),
          ("privilege-2", 2),
          ("privilege-3", 3),
          ("privilege-4", 4),
          ("privilege-5", 5),
          ("privilege-6", 6),
          ("privilege-7", 7),
          ("privilege-8", 8),
          ("privilege-9", 9),
          ("privilege-10", 10),
          ("privilege-11", 11),
          ("privilege-12", 12),
          ("privilege-13", 13),
          ("privilege-14", 14),
          ("not-available", 255))
    )


_AccountingTypePrivilege_Type.__name__ = "Integer32"
_AccountingTypePrivilege_Object = MibTableColumn
accountingTypePrivilege = _AccountingTypePrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 59, 2, 2, 1, 6),
    _AccountingTypePrivilege_Type()
)
accountingTypePrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypePrivilege.setStatus("current")
_Vdsl2Ext_ObjectIdentity = ObjectIdentity
vdsl2Ext = _Vdsl2Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60)
)
_Xdsl2ExtNotifications_ObjectIdentity = ObjectIdentity
xdsl2ExtNotifications = _Xdsl2ExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 0)
)
_Xdsl2ExtLine_ObjectIdentity = ObjectIdentity
xdsl2ExtLine = _Xdsl2ExtLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1)
)
_Xdsl2ExtLineTable_Object = MibTable
xdsl2ExtLineTable = _Xdsl2ExtLineTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineTable.setStatus("current")
_Xdsl2ExtLineEntry_Object = MibTableRow
xdsl2ExtLineEntry = _Xdsl2ExtLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 1, 1)
)
xdsl2ExtLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineEntry.setStatus("current")


class _Xdsl2LineCmndConfSelt_Type(Xdsl2LineLdsf):
    """Custom type xdsl2LineCmndConfSelt based on Xdsl2LineLdsf"""
    defaultValue = 0


_Xdsl2LineCmndConfSelt_Type.__name__ = "Xdsl2LineLdsf"
_Xdsl2LineCmndConfSelt_Object = MibTableColumn
xdsl2LineCmndConfSelt = _Xdsl2LineCmndConfSelt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 1, 1, 1),
    _Xdsl2LineCmndConfSelt_Type()
)
xdsl2LineCmndConfSelt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfSelt.setStatus("current")
_Xdsl2ExtLineBandTable_Object = MibTable
xdsl2ExtLineBandTable = _Xdsl2ExtLineBandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineBandTable.setStatus("current")
_Xdsl2ExtLineBandEntry_Object = MibTableRow
xdsl2ExtLineBandEntry = _Xdsl2ExtLineBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 2, 1)
)
xdsl2ExtLineBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineBand"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineBandEntry.setStatus("current")


class _Xdsl2LineBandStatusActAtp_Type(Integer32):
    """Custom type xdsl2LineBandStatusActAtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusActAtp_Type.__name__ = "Integer32"
_Xdsl2LineBandStatusActAtp_Object = MibTableColumn
xdsl2LineBandStatusActAtp = _Xdsl2LineBandStatusActAtp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 2, 1, 1),
    _Xdsl2LineBandStatusActAtp_Type()
)
xdsl2LineBandStatusActAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusActAtp.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusActAtp.setUnits("0.1 dBm")


class _Xdsl2LineBandStatusActRxPwr_Type(Integer32):
    """Custom type xdsl2LineBandStatusActRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusActRxPwr_Type.__name__ = "Integer32"
_Xdsl2LineBandStatusActRxPwr_Object = MibTableColumn
xdsl2LineBandStatusActRxPwr = _Xdsl2LineBandStatusActRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 1, 2, 1, 2),
    _Xdsl2LineBandStatusActRxPwr_Type()
)
xdsl2LineBandStatusActRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusActRxPwr.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusActRxPwr.setUnits("0.1 dBm")
_Xdsl2ExtStatus_ObjectIdentity = ObjectIdentity
xdsl2ExtStatus = _Xdsl2ExtStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2)
)
_Xdsl2ExtLineSegmentTable_Object = MibTable
xdsl2ExtLineSegmentTable = _Xdsl2ExtLineSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineSegmentTable.setStatus("current")
_Xdsl2ExtLineSegmentEntry_Object = MibTableRow
xdsl2ExtLineSegmentEntry = _Xdsl2ExtLineSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1)
)
xdsl2ExtLineSegmentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineSegmentDirection"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineSegment"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineSegmentEntry.setStatus("current")


class _Xdsl2LineSegmentLog_Type(OctetString):
    """Custom type xdsl2LineSegmentLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2LineSegmentLog_Type.__name__ = "OctetString"
_Xdsl2LineSegmentLog_Object = MibTableColumn
xdsl2LineSegmentLog = _Xdsl2LineSegmentLog_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 1),
    _Xdsl2LineSegmentLog_Type()
)
xdsl2LineSegmentLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentLog.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineSegmentLog.setUnits("dB")


class _Xdsl2LineSegmentQln_Type(OctetString):
    """Custom type xdsl2LineSegmentQln based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Xdsl2LineSegmentQln_Type.__name__ = "OctetString"
_Xdsl2LineSegmentQln_Object = MibTableColumn
xdsl2LineSegmentQln = _Xdsl2LineSegmentQln_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 2),
    _Xdsl2LineSegmentQln_Type()
)
xdsl2LineSegmentQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentQln.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineSegmentQln.setUnits("dBm/Hz")


class _Xdsl2LineSegmentSnr_Type(OctetString):
    """Custom type xdsl2LineSegmentSnr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Xdsl2LineSegmentSnr_Type.__name__ = "OctetString"
_Xdsl2LineSegmentSnr_Object = MibTableColumn
xdsl2LineSegmentSnr = _Xdsl2LineSegmentSnr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 3),
    _Xdsl2LineSegmentSnr_Type()
)
xdsl2LineSegmentSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentSnr.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineSegmentSnr.setUnits("0.5 dB")


class _Xdsl2LineSegmentStatus_Type(Bits):
    """Custom type xdsl2LineSegmentStatus based on Bits"""
    namedValues = NamedValues(
        *(("hlogReady", 0),
          ("qlnReady", 1),
          ("snrReady", 2))
    )

_Xdsl2LineSegmentStatus_Type.__name__ = "Bits"
_Xdsl2LineSegmentStatus_Object = MibTableColumn
xdsl2LineSegmentStatus = _Xdsl2LineSegmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 4),
    _Xdsl2LineSegmentStatus_Type()
)
xdsl2LineSegmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentStatus.setStatus("current")


class _Xdsl2LineSegmentLogScGroupSize_Type(Unsigned32):
    """Custom type xdsl2LineSegmentLogScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2LineSegmentLogScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2LineSegmentLogScGroupSize_Object = MibTableColumn
xdsl2LineSegmentLogScGroupSize = _Xdsl2LineSegmentLogScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 5),
    _Xdsl2LineSegmentLogScGroupSize_Type()
)
xdsl2LineSegmentLogScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentLogScGroupSize.setStatus("current")


class _Xdsl2LineSegmentQlnScGroupSize_Type(Unsigned32):
    """Custom type xdsl2LineSegmentQlnScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2LineSegmentQlnScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2LineSegmentQlnScGroupSize_Object = MibTableColumn
xdsl2LineSegmentQlnScGroupSize = _Xdsl2LineSegmentQlnScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 6),
    _Xdsl2LineSegmentQlnScGroupSize_Type()
)
xdsl2LineSegmentQlnScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentQlnScGroupSize.setStatus("current")


class _Xdsl2LineSegmentSnrScGroupSize_Type(Unsigned32):
    """Custom type xdsl2LineSegmentSnrScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2LineSegmentSnrScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2LineSegmentSnrScGroupSize_Object = MibTableColumn
xdsl2LineSegmentSnrScGroupSize = _Xdsl2LineSegmentSnrScGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 1, 1, 7),
    _Xdsl2LineSegmentSnrScGroupSize_Type()
)
xdsl2LineSegmentSnrScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentSnrScGroupSize.setStatus("current")
_Xdsl2ExtSCStatusTable_Object = MibTable
xdsl2ExtSCStatusTable = _Xdsl2ExtSCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2ExtSCStatusTable.setStatus("current")
_Xdsl2ExtSCStatusEntry_Object = MibTableRow
xdsl2ExtSCStatusEntry = _Xdsl2ExtSCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 3, 1)
)
xdsl2ExtSCStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusDirection"),
)
if mibBuilder.loadTexts:
    xdsl2ExtSCStatusEntry.setStatus("current")


class _Xdsl2SCStatusActAtp_Type(Integer32):
    """Custom type xdsl2SCStatusActAtp based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusActAtp_Type.__name__ = "Integer32"
_Xdsl2SCStatusActAtp_Object = MibTableColumn
xdsl2SCStatusActAtp = _Xdsl2SCStatusActAtp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 3, 1, 1),
    _Xdsl2SCStatusActAtp_Type()
)
xdsl2SCStatusActAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusActAtp.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusActAtp.setUnits("0.1 dBm")
_Xdsl2ExtSCStatusBandTable_Object = MibTable
xdsl2ExtSCStatusBandTable = _Xdsl2ExtSCStatusBandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 4)
)
if mibBuilder.loadTexts:
    xdsl2ExtSCStatusBandTable.setStatus("current")
_Xdsl2ExtSCStatusBandEntry_Object = MibTableRow
xdsl2ExtSCStatusBandEntry = _Xdsl2ExtSCStatusBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 4, 1)
)
xdsl2ExtSCStatusBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusBand"),
)
if mibBuilder.loadTexts:
    xdsl2ExtSCStatusBandEntry.setStatus("current")


class _Xdsl2SCStatusBandSnrMargin_Type(Integer32):
    """Custom type xdsl2SCStatusBandSnrMargin based on Integer32"""
    defaultValue = 2147483646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusBandSnrMargin_Type.__name__ = "Integer32"
_Xdsl2SCStatusBandSnrMargin_Object = MibTableColumn
xdsl2SCStatusBandSnrMargin = _Xdsl2SCStatusBandSnrMargin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 4, 1, 1),
    _Xdsl2SCStatusBandSnrMargin_Type()
)
xdsl2SCStatusBandSnrMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSnrMargin.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSnrMargin.setUnits("0.1 dB")
_Xdsl2ExtSeltStatusTable_Object = MibTable
xdsl2ExtSeltStatusTable = _Xdsl2ExtSeltStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 6)
)
if mibBuilder.loadTexts:
    xdsl2ExtSeltStatusTable.setStatus("current")
_Xdsl2ExtSeltStatusEntry_Object = MibTableRow
xdsl2ExtSeltStatusEntry = _Xdsl2ExtSeltStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 6, 1)
)
xdsl2ExtSeltStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2ExtSeltStatusEntry.setStatus("current")


class _Xdsl2SeltStatus_Type(Integer32):
    """Custom type xdsl2SeltStatus based on Integer32"""
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
        *(("idle", 0),
          ("inProgress", 1),
          ("failed", 2),
          ("done", 3))
    )


_Xdsl2SeltStatus_Type.__name__ = "Integer32"
_Xdsl2SeltStatus_Object = MibTableColumn
xdsl2SeltStatus = _Xdsl2SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 6, 1, 1),
    _Xdsl2SeltStatus_Type()
)
xdsl2SeltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltStatus.setStatus("current")
_Xdsl2SeltStatusLineType_Type = DisplayString
_Xdsl2SeltStatusLineType_Object = MibTableColumn
xdsl2SeltStatusLineType = _Xdsl2SeltStatusLineType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 6, 1, 2),
    _Xdsl2SeltStatusLineType_Type()
)
xdsl2SeltStatusLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltStatusLineType.setStatus("current")
_Xdsl2SeltStatusLineLength_Type = Integer32
_Xdsl2SeltStatusLineLength_Object = MibTableColumn
xdsl2SeltStatusLineLength = _Xdsl2SeltStatusLineLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 6, 1, 3),
    _Xdsl2SeltStatusLineLength_Type()
)
xdsl2SeltStatusLineLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltStatusLineLength.setStatus("current")
_Xdsl2ExtSeltReflectionStatusTable_Object = MibTable
xdsl2ExtSeltReflectionStatusTable = _Xdsl2ExtSeltReflectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7)
)
if mibBuilder.loadTexts:
    xdsl2ExtSeltReflectionStatusTable.setStatus("current")
_Xdsl2ExtSeltReflectionStatusEntry_Object = MibTableRow
xdsl2ExtSeltReflectionStatusEntry = _Xdsl2ExtSeltReflectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1)
)
xdsl2ExtSeltReflectionStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-ves1608FE57-MIB", "xdsl2SeltReflection"),
)
if mibBuilder.loadTexts:
    xdsl2ExtSeltReflectionStatusEntry.setStatus("current")
_Xdsl2SeltReflection_Type = Unsigned32
_Xdsl2SeltReflection_Object = MibTableColumn
xdsl2SeltReflection = _Xdsl2SeltReflection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 1),
    _Xdsl2SeltReflection_Type()
)
xdsl2SeltReflection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SeltReflection.setStatus("current")
_Xdsl2SeltDelay_Type = Integer32
_Xdsl2SeltDelay_Object = MibTableColumn
xdsl2SeltDelay = _Xdsl2SeltDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 2),
    _Xdsl2SeltDelay_Type()
)
xdsl2SeltDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltDelay.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SeltDelay.setUnits("0.1")
_Xdsl2SeltError_Type = Integer32
_Xdsl2SeltError_Object = MibTableColumn
xdsl2SeltError = _Xdsl2SeltError_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 3),
    _Xdsl2SeltError_Type()
)
xdsl2SeltError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltError.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SeltError.setUnits("0.1")
_Xdsl2SeltAtn180kHz_Type = Integer32
_Xdsl2SeltAtn180kHz_Object = MibTableColumn
xdsl2SeltAtn180kHz = _Xdsl2SeltAtn180kHz_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 4),
    _Xdsl2SeltAtn180kHz_Type()
)
xdsl2SeltAtn180kHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltAtn180kHz.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SeltAtn180kHz.setUnits("0.1")
_Xdsl2SeltAtn300kHz_Type = Integer32
_Xdsl2SeltAtn300kHz_Object = MibTableColumn
xdsl2SeltAtn300kHz = _Xdsl2SeltAtn300kHz_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 5),
    _Xdsl2SeltAtn300kHz_Type()
)
xdsl2SeltAtn300kHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltAtn300kHz.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SeltAtn300kHz.setUnits("0.1")
_Xdsl2SeltFitError_Type = Integer32
_Xdsl2SeltFitError_Object = MibTableColumn
xdsl2SeltFitError = _Xdsl2SeltFitError_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 6),
    _Xdsl2SeltFitError_Type()
)
xdsl2SeltFitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltFitError.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SeltFitError.setUnits("0.1")
_Xdsl2SeltFitTermination_Type = Integer32
_Xdsl2SeltFitTermination_Object = MibTableColumn
xdsl2SeltFitTermination = _Xdsl2SeltFitTermination_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 2, 7, 1, 7),
    _Xdsl2SeltFitTermination_Type()
)
xdsl2SeltFitTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SeltFitTermination.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SeltFitTermination.setUnits("0.2")
_Xdsl2ExtPM_ObjectIdentity = ObjectIdentity
xdsl2ExtPM = _Xdsl2ExtPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4)
)
_Xdsl2ExtPMLine_ObjectIdentity = ObjectIdentity
xdsl2ExtPMLine = _Xdsl2ExtPMLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1)
)
_Xdsl2ExtPMLineCurrTable_Object = MibTable
xdsl2ExtPMLineCurrTable = _Xdsl2ExtPMLineCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtPMLineCurrTable.setStatus("current")
_Xdsl2ExtPMLineCurrEntry_Object = MibTableRow
xdsl2ExtPMLineCurrEntry = _Xdsl2ExtPMLineCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1)
)
xdsl2ExtPMLineCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2ExtPMLineCurrEntry.setStatus("current")
_Xdsl2PMLSinceLinkFecs_Type = Counter32
_Xdsl2PMLSinceLinkFecs_Object = MibTableColumn
xdsl2PMLSinceLinkFecs = _Xdsl2PMLSinceLinkFecs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 1),
    _Xdsl2PMLSinceLinkFecs_Type()
)
xdsl2PMLSinceLinkFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkFecs.setUnits("seconds")
_Xdsl2PMLSinceLinkEs_Type = Counter32
_Xdsl2PMLSinceLinkEs_Object = MibTableColumn
xdsl2PMLSinceLinkEs = _Xdsl2PMLSinceLinkEs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 2),
    _Xdsl2PMLSinceLinkEs_Type()
)
xdsl2PMLSinceLinkEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkEs.setUnits("seconds")
_Xdsl2PMLSinceLinkSes_Type = Counter32
_Xdsl2PMLSinceLinkSes_Object = MibTableColumn
xdsl2PMLSinceLinkSes = _Xdsl2PMLSinceLinkSes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 3),
    _Xdsl2PMLSinceLinkSes_Type()
)
xdsl2PMLSinceLinkSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkSes.setUnits("seconds")
_Xdsl2PMLSinceLinkLoss_Type = Counter32
_Xdsl2PMLSinceLinkLoss_Object = MibTableColumn
xdsl2PMLSinceLinkLoss = _Xdsl2PMLSinceLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 4),
    _Xdsl2PMLSinceLinkLoss_Type()
)
xdsl2PMLSinceLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLoss.setUnits("seconds")
_Xdsl2PMLSinceLinkUas_Type = Counter32
_Xdsl2PMLSinceLinkUas_Object = MibTableColumn
xdsl2PMLSinceLinkUas = _Xdsl2PMLSinceLinkUas_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 5),
    _Xdsl2PMLSinceLinkUas_Type()
)
xdsl2PMLSinceLinkUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkUas.setUnits("seconds")
_Xdsl2PMLSinceLinkLofs_Type = Counter32
_Xdsl2PMLSinceLinkLofs_Object = MibTableColumn
xdsl2PMLSinceLinkLofs = _Xdsl2PMLSinceLinkLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 6),
    _Xdsl2PMLSinceLinkLofs_Type()
)
xdsl2PMLSinceLinkLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLofs.setUnits("seconds")
_Xdsl2PMLSinceLinkLol_Type = Counter32
_Xdsl2PMLSinceLinkLol_Object = MibTableColumn
xdsl2PMLSinceLinkLol = _Xdsl2PMLSinceLinkLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 7),
    _Xdsl2PMLSinceLinkLol_Type()
)
xdsl2PMLSinceLinkLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLol.setStatus("current")
_Xdsl2PMLSinceLinkLols_Type = Counter32
_Xdsl2PMLSinceLinkLols_Object = MibTableColumn
xdsl2PMLSinceLinkLols = _Xdsl2PMLSinceLinkLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 8),
    _Xdsl2PMLSinceLinkLols_Type()
)
xdsl2PMLSinceLinkLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLols.setUnits("seconds")
_Xdsl2PMLSinceLinkLpr_Type = Counter32
_Xdsl2PMLSinceLinkLpr_Object = MibTableColumn
xdsl2PMLSinceLinkLpr = _Xdsl2PMLSinceLinkLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 9),
    _Xdsl2PMLSinceLinkLpr_Type()
)
xdsl2PMLSinceLinkLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLpr.setStatus("current")
_Xdsl2PMLSinceLinkLprs_Type = Counter32
_Xdsl2PMLSinceLinkLprs_Object = MibTableColumn
xdsl2PMLSinceLinkLprs = _Xdsl2PMLSinceLinkLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 10),
    _Xdsl2PMLSinceLinkLprs_Type()
)
xdsl2PMLSinceLinkLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkLprs.setUnits("seconds")
_Xdsl2PMLCurr15MLofs_Type = Counter32
_Xdsl2PMLCurr15MLofs_Object = MibTableColumn
xdsl2PMLCurr15MLofs = _Xdsl2PMLCurr15MLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 11),
    _Xdsl2PMLCurr15MLofs_Type()
)
xdsl2PMLCurr15MLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLofs.setUnits("seconds")
_Xdsl2PMLCurr15MLol_Type = Counter32
_Xdsl2PMLCurr15MLol_Object = MibTableColumn
xdsl2PMLCurr15MLol = _Xdsl2PMLCurr15MLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 12),
    _Xdsl2PMLCurr15MLol_Type()
)
xdsl2PMLCurr15MLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLol.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLol.setUnits("seconds")
_Xdsl2PMLCurr15MLols_Type = Counter32
_Xdsl2PMLCurr15MLols_Object = MibTableColumn
xdsl2PMLCurr15MLols = _Xdsl2PMLCurr15MLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 13),
    _Xdsl2PMLCurr15MLols_Type()
)
xdsl2PMLCurr15MLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLols.setUnits("seconds")
_Xdsl2PMLCurr15MLpr_Type = Counter32
_Xdsl2PMLCurr15MLpr_Object = MibTableColumn
xdsl2PMLCurr15MLpr = _Xdsl2PMLCurr15MLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 14),
    _Xdsl2PMLCurr15MLpr_Type()
)
xdsl2PMLCurr15MLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLpr.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLpr.setUnits("seconds")
_Xdsl2PMLCurr15MLprs_Type = Counter32
_Xdsl2PMLCurr15MLprs_Object = MibTableColumn
xdsl2PMLCurr15MLprs = _Xdsl2PMLCurr15MLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 15),
    _Xdsl2PMLCurr15MLprs_Type()
)
xdsl2PMLCurr15MLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLprs.setUnits("seconds")
_Xdsl2PMLCurr1DayLofs_Type = Counter32
_Xdsl2PMLCurr1DayLofs_Object = MibTableColumn
xdsl2PMLCurr1DayLofs = _Xdsl2PMLCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 16),
    _Xdsl2PMLCurr1DayLofs_Type()
)
xdsl2PMLCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLofs.setUnits("seconds")
_Xdsl2PMLCurr1DayLol_Type = Counter32
_Xdsl2PMLCurr1DayLol_Object = MibTableColumn
xdsl2PMLCurr1DayLol = _Xdsl2PMLCurr1DayLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 17),
    _Xdsl2PMLCurr1DayLol_Type()
)
xdsl2PMLCurr1DayLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLol.setStatus("current")
_Xdsl2PMLCurr1DayLols_Type = Counter32
_Xdsl2PMLCurr1DayLols_Object = MibTableColumn
xdsl2PMLCurr1DayLols = _Xdsl2PMLCurr1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 18),
    _Xdsl2PMLCurr1DayLols_Type()
)
xdsl2PMLCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLols.setUnits("seconds")
_Xdsl2PMLCurr1DayLpr_Type = Counter32
_Xdsl2PMLCurr1DayLpr_Object = MibTableColumn
xdsl2PMLCurr1DayLpr = _Xdsl2PMLCurr1DayLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 19),
    _Xdsl2PMLCurr1DayLpr_Type()
)
xdsl2PMLCurr1DayLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLpr.setStatus("current")
_Xdsl2PMLCurr1DayLprs_Type = Counter32
_Xdsl2PMLCurr1DayLprs_Object = MibTableColumn
xdsl2PMLCurr1DayLprs = _Xdsl2PMLCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 20),
    _Xdsl2PMLCurr1DayLprs_Type()
)
xdsl2PMLCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLprs.setUnits("seconds")
_Xdsl2PMLSinceLinkInmEqInp_Type = Counter32
_Xdsl2PMLSinceLinkInmEqInp_Object = MibTableColumn
xdsl2PMLSinceLinkInmEqInp = _Xdsl2PMLSinceLinkInmEqInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 21),
    _Xdsl2PMLSinceLinkInmEqInp_Type()
)
xdsl2PMLSinceLinkInmEqInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkInmEqInp.setStatus("current")
_Xdsl2PMLSinceLinkInmIAT_Type = Counter32
_Xdsl2PMLSinceLinkInmIAT_Object = MibTableColumn
xdsl2PMLSinceLinkInmIAT = _Xdsl2PMLSinceLinkInmIAT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 22),
    _Xdsl2PMLSinceLinkInmIAT_Type()
)
xdsl2PMLSinceLinkInmIAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkInmIAT.setStatus("current")
_Xdsl2PMLSinceLinkInmME_Type = Counter32
_Xdsl2PMLSinceLinkInmME_Object = MibTableColumn
xdsl2PMLSinceLinkInmME = _Xdsl2PMLSinceLinkInmME_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 23),
    _Xdsl2PMLSinceLinkInmME_Type()
)
xdsl2PMLSinceLinkInmME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkInmME.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLSinceLinkInmME.setUnits("symbols")
_Xdsl2PMLCurr15MInmEqInp_Type = Counter32
_Xdsl2PMLCurr15MInmEqInp_Object = MibTableColumn
xdsl2PMLCurr15MInmEqInp = _Xdsl2PMLCurr15MInmEqInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 24),
    _Xdsl2PMLCurr15MInmEqInp_Type()
)
xdsl2PMLCurr15MInmEqInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MInmEqInp.setStatus("current")
_Xdsl2PMLCurr15MInmIAT_Type = Counter32
_Xdsl2PMLCurr15MInmIAT_Object = MibTableColumn
xdsl2PMLCurr15MInmIAT = _Xdsl2PMLCurr15MInmIAT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 25),
    _Xdsl2PMLCurr15MInmIAT_Type()
)
xdsl2PMLCurr15MInmIAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MInmIAT.setStatus("current")
_Xdsl2PMLCurr15MInmME_Type = Counter32
_Xdsl2PMLCurr15MInmME_Object = MibTableColumn
xdsl2PMLCurr15MInmME = _Xdsl2PMLCurr15MInmME_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 26),
    _Xdsl2PMLCurr15MInmME_Type()
)
xdsl2PMLCurr15MInmME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MInmME.setStatus("current")
_Xdsl2PMLCurr1DayInmEqInp_Type = Counter32
_Xdsl2PMLCurr1DayInmEqInp_Object = MibTableColumn
xdsl2PMLCurr1DayInmEqInp = _Xdsl2PMLCurr1DayInmEqInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 27),
    _Xdsl2PMLCurr1DayInmEqInp_Type()
)
xdsl2PMLCurr1DayInmEqInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayInmEqInp.setStatus("current")
_Xdsl2PMLCurr1DayInmIAT_Type = Counter32
_Xdsl2PMLCurr1DayInmIAT_Object = MibTableColumn
xdsl2PMLCurr1DayInmIAT = _Xdsl2PMLCurr1DayInmIAT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 28),
    _Xdsl2PMLCurr1DayInmIAT_Type()
)
xdsl2PMLCurr1DayInmIAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayInmIAT.setStatus("current")
_Xdsl2PMLCurr1DayInmME_Type = Counter32
_Xdsl2PMLCurr1DayInmME_Object = MibTableColumn
xdsl2PMLCurr1DayInmME = _Xdsl2PMLCurr1DayInmME_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 1, 1, 29),
    _Xdsl2PMLCurr1DayInmME_Type()
)
xdsl2PMLCurr1DayInmME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayInmME.setStatus("current")
_Xdsl2ExtPMLineHist15MinTable_Object = MibTable
xdsl2ExtPMLineHist15MinTable = _Xdsl2ExtPMLineHist15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3)
)
if mibBuilder.loadTexts:
    xdsl2ExtPMLineHist15MinTable.setStatus("current")
_Xdsl2ExtPMLineHist15MinEntry_Object = MibTableRow
xdsl2ExtPMLineHist15MinEntry = _Xdsl2ExtPMLineHist15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1)
)
xdsl2ExtPMLineHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist15MUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2ExtPMLineHist15MinEntry.setStatus("current")
_Xdsl2PMLHist15MLofs_Type = Counter32
_Xdsl2PMLHist15MLofs_Object = MibTableColumn
xdsl2PMLHist15MLofs = _Xdsl2PMLHist15MLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 1),
    _Xdsl2PMLHist15MLofs_Type()
)
xdsl2PMLHist15MLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLofs.setUnits("seconds")
_Xdsl2PMLHist15MLol_Type = Counter32
_Xdsl2PMLHist15MLol_Object = MibTableColumn
xdsl2PMLHist15MLol = _Xdsl2PMLHist15MLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 2),
    _Xdsl2PMLHist15MLol_Type()
)
xdsl2PMLHist15MLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLol.setStatus("current")
_Xdsl2PMLHist15MLols_Type = Counter32
_Xdsl2PMLHist15MLols_Object = MibTableColumn
xdsl2PMLHist15MLols = _Xdsl2PMLHist15MLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 3),
    _Xdsl2PMLHist15MLols_Type()
)
xdsl2PMLHist15MLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLols.setUnits("seconds")
_Xdsl2PMLHist15MLpr_Type = Counter32
_Xdsl2PMLHist15MLpr_Object = MibTableColumn
xdsl2PMLHist15MLpr = _Xdsl2PMLHist15MLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 4),
    _Xdsl2PMLHist15MLpr_Type()
)
xdsl2PMLHist15MLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLpr.setStatus("current")
_Xdsl2PMLHist15MLprs_Type = Counter32
_Xdsl2PMLHist15MLprs_Object = MibTableColumn
xdsl2PMLHist15MLprs = _Xdsl2PMLHist15MLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 5),
    _Xdsl2PMLHist15MLprs_Type()
)
xdsl2PMLHist15MLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLprs.setUnits("seconds")
_Xdsl2PMLHist15MInmEqInp_Type = Counter32
_Xdsl2PMLHist15MInmEqInp_Object = MibTableColumn
xdsl2PMLHist15MInmEqInp = _Xdsl2PMLHist15MInmEqInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 6),
    _Xdsl2PMLHist15MInmEqInp_Type()
)
xdsl2PMLHist15MInmEqInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MInmEqInp.setStatus("current")
_Xdsl2PMLHist15MInmIAT_Type = Counter32
_Xdsl2PMLHist15MInmIAT_Object = MibTableColumn
xdsl2PMLHist15MInmIAT = _Xdsl2PMLHist15MInmIAT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 7),
    _Xdsl2PMLHist15MInmIAT_Type()
)
xdsl2PMLHist15MInmIAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MInmIAT.setStatus("current")
_Xdsl2PMLHist15MInmME_Type = Counter32
_Xdsl2PMLHist15MInmME_Object = MibTableColumn
xdsl2PMLHist15MInmME = _Xdsl2PMLHist15MInmME_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 3, 1, 8),
    _Xdsl2PMLHist15MInmME_Type()
)
xdsl2PMLHist15MInmME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MInmME.setStatus("current")
_Xdsl2ExtPMLineHist1DayTable_Object = MibTable
xdsl2ExtPMLineHist1DayTable = _Xdsl2ExtPMLineHist1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4)
)
if mibBuilder.loadTexts:
    xdsl2ExtPMLineHist1DayTable.setStatus("current")
_Xdsl2ExtPMLineHist1DayEntry_Object = MibTableRow
xdsl2ExtPMLineHist1DayEntry = _Xdsl2ExtPMLineHist1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1)
)
xdsl2ExtPMLineHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist1DUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2ExtPMLineHist1DayEntry.setStatus("current")
_Xdsl2PMLHist1DLofs_Type = Counter32
_Xdsl2PMLHist1DLofs_Object = MibTableColumn
xdsl2PMLHist1DLofs = _Xdsl2PMLHist1DLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 1),
    _Xdsl2PMLHist1DLofs_Type()
)
xdsl2PMLHist1DLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLofs.setUnits("seconds")
_Xdsl2PMLHist1DLol_Type = Counter32
_Xdsl2PMLHist1DLol_Object = MibTableColumn
xdsl2PMLHist1DLol = _Xdsl2PMLHist1DLol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 2),
    _Xdsl2PMLHist1DLol_Type()
)
xdsl2PMLHist1DLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLol.setStatus("current")
_Xdsl2PMLHist1DLols_Type = Counter32
_Xdsl2PMLHist1DLols_Object = MibTableColumn
xdsl2PMLHist1DLols = _Xdsl2PMLHist1DLols_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 3),
    _Xdsl2PMLHist1DLols_Type()
)
xdsl2PMLHist1DLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLols.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLols.setUnits("seconds")
_Xdsl2PMLHist1DLpr_Type = Counter32
_Xdsl2PMLHist1DLpr_Object = MibTableColumn
xdsl2PMLHist1DLpr = _Xdsl2PMLHist1DLpr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 4),
    _Xdsl2PMLHist1DLpr_Type()
)
xdsl2PMLHist1DLpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLpr.setStatus("current")
_Xdsl2PMLHist1DLprs_Type = Counter32
_Xdsl2PMLHist1DLprs_Object = MibTableColumn
xdsl2PMLHist1DLprs = _Xdsl2PMLHist1DLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 5),
    _Xdsl2PMLHist1DLprs_Type()
)
xdsl2PMLHist1DLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLprs.setUnits("seconds")
_Xdsl2PMLHist1DInmEqInp_Type = Counter32
_Xdsl2PMLHist1DInmEqInp_Object = MibTableColumn
xdsl2PMLHist1DInmEqInp = _Xdsl2PMLHist1DInmEqInp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 6),
    _Xdsl2PMLHist1DInmEqInp_Type()
)
xdsl2PMLHist1DInmEqInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DInmEqInp.setStatus("current")
_Xdsl2PMLHist1DInmIAT_Type = Counter32
_Xdsl2PMLHist1DInmIAT_Object = MibTableColumn
xdsl2PMLHist1DInmIAT = _Xdsl2PMLHist1DInmIAT_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 7),
    _Xdsl2PMLHist1DInmIAT_Type()
)
xdsl2PMLHist1DInmIAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DInmIAT.setStatus("current")
_Xdsl2PMLHist1DInmME_Type = Counter32
_Xdsl2PMLHist1DInmME_Object = MibTableColumn
xdsl2PMLHist1DInmME = _Xdsl2PMLHist1DInmME_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 1, 4, 1, 8),
    _Xdsl2PMLHist1DInmME_Type()
)
xdsl2PMLHist1DInmME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DInmME.setStatus("current")
_Xdsl2ExtPMChannel_ObjectIdentity = ObjectIdentity
xdsl2ExtPMChannel = _Xdsl2ExtPMChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2)
)
_Xdsl2ExtPMChCurrTable_Object = MibTable
xdsl2ExtPMChCurrTable = _Xdsl2ExtPMChCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtPMChCurrTable.setStatus("current")
_Xdsl2ExtPMChCurrEntry_Object = MibTableRow
xdsl2ExtPMChCurrEntry = _Xdsl2ExtPMChCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1, 1)
)
xdsl2ExtPMChCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2ExtPMChCurrEntry.setStatus("current")
_Xdsl2PMChSinceLinkUncorrectedCWs_Type = Unsigned32
_Xdsl2PMChSinceLinkUncorrectedCWs_Object = MibTableColumn
xdsl2PMChSinceLinkUncorrectedCWs = _Xdsl2PMChSinceLinkUncorrectedCWs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1, 1, 1),
    _Xdsl2PMChSinceLinkUncorrectedCWs_Type()
)
xdsl2PMChSinceLinkUncorrectedCWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChSinceLinkUncorrectedCWs.setStatus("current")
_Xdsl2PMChCurr15MUncorrectedCWs_Type = Unsigned32
_Xdsl2PMChCurr15MUncorrectedCWs_Object = MibTableColumn
xdsl2PMChCurr15MUncorrectedCWs = _Xdsl2PMChCurr15MUncorrectedCWs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1, 1, 2),
    _Xdsl2PMChCurr15MUncorrectedCWs_Type()
)
xdsl2PMChCurr15MUncorrectedCWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MUncorrectedCWs.setStatus("current")
_Xdsl2PMChCurr1DayUncorrectedCWs_Type = Unsigned32
_Xdsl2PMChCurr1DayUncorrectedCWs_Object = MibTableColumn
xdsl2PMChCurr1DayUncorrectedCWs = _Xdsl2PMChCurr1DayUncorrectedCWs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1, 1, 3),
    _Xdsl2PMChCurr1DayUncorrectedCWs_Type()
)
xdsl2PMChCurr1DayUncorrectedCWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayUncorrectedCWs.setStatus("current")
_Xdsl2PMChSinceLinkCodingViolations_Type = Unsigned32
_Xdsl2PMChSinceLinkCodingViolations_Object = MibTableColumn
xdsl2PMChSinceLinkCodingViolations = _Xdsl2PMChSinceLinkCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1, 1, 4),
    _Xdsl2PMChSinceLinkCodingViolations_Type()
)
xdsl2PMChSinceLinkCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChSinceLinkCodingViolations.setStatus("current")
_Xdsl2PMChSinceLinkCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChSinceLinkCorrectedBlocks_Object = MibTableColumn
xdsl2PMChSinceLinkCorrectedBlocks = _Xdsl2PMChSinceLinkCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 1, 1, 5),
    _Xdsl2PMChSinceLinkCorrectedBlocks_Type()
)
xdsl2PMChSinceLinkCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChSinceLinkCorrectedBlocks.setStatus("current")
_Xdsl2ExtPMChHist15MinTable_Object = MibTable
xdsl2ExtPMChHist15MinTable = _Xdsl2ExtPMChHist15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 2)
)
if mibBuilder.loadTexts:
    xdsl2ExtPMChHist15MinTable.setStatus("current")
_Xdsl2ExtPMChHist15MinEntry_Object = MibTableRow
xdsl2ExtPMChHist15MinEntry = _Xdsl2ExtPMChHist15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 2, 1)
)
xdsl2ExtPMChHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist15MUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2ExtPMChHist15MinEntry.setStatus("current")
_Xdsl2PMChHist15MUncorrectedCWs_Type = Unsigned32
_Xdsl2PMChHist15MUncorrectedCWs_Object = MibTableColumn
xdsl2PMChHist15MUncorrectedCWs = _Xdsl2PMChHist15MUncorrectedCWs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 2, 1, 1),
    _Xdsl2PMChHist15MUncorrectedCWs_Type()
)
xdsl2PMChHist15MUncorrectedCWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MUncorrectedCWs.setStatus("current")
_Xdsl2ExtPMChHist1DTable_Object = MibTable
xdsl2ExtPMChHist1DTable = _Xdsl2ExtPMChHist1DTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2ExtPMChHist1DTable.setStatus("current")
_Xdsl2ExtPMChHist1DEntry_Object = MibTableRow
xdsl2ExtPMChHist1DEntry = _Xdsl2ExtPMChHist1DEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 3, 1)
)
xdsl2ExtPMChHist1DEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist1DUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2ExtPMChHist1DEntry.setStatus("current")
_Xdsl2PMChHist1DayUncorrectedCWs_Type = Unsigned32
_Xdsl2PMChHist1DayUncorrectedCWs_Object = MibTableColumn
xdsl2PMChHist1DayUncorrectedCWs = _Xdsl2PMChHist1DayUncorrectedCWs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 4, 2, 3, 1, 1),
    _Xdsl2PMChHist1DayUncorrectedCWs_Type()
)
xdsl2PMChHist1DayUncorrectedCWs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DayUncorrectedCWs.setStatus("current")
_Xdsl2ExtProfile_ObjectIdentity = ObjectIdentity
xdsl2ExtProfile = _Xdsl2ExtProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5)
)
_Xdsl2ExtProfileLine_ObjectIdentity = ObjectIdentity
xdsl2ExtProfileLine = _Xdsl2ExtProfileLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1)
)
_Xdsl2ExtLineConfTemplateTable_Object = MibTable
xdsl2ExtLineConfTemplateTable = _Xdsl2ExtLineConfTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineConfTemplateTable.setStatus("current")
_Xdsl2ExtLineConfTemplateEntry_Object = MibTableRow
xdsl2ExtLineConfTemplateEntry = _Xdsl2ExtLineConfTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 1, 1)
)
xdsl2ExtLineConfTemplateEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfTempTemplateName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineConfTemplateEntry.setStatus("current")
_Xdsl2LConfTempPortList_Type = PortList
_Xdsl2LConfTempPortList_Object = MibTableColumn
xdsl2LConfTempPortList = _Xdsl2LConfTempPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 1, 1, 1),
    _Xdsl2LConfTempPortList_Type()
)
xdsl2LConfTempPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LConfTempPortList.setStatus("current")


class _Xdsl2LConfTempInmConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempInmConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LConfTempInmConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempInmConfProfile_Object = MibTableColumn
xdsl2LConfTempInmConfProfile = _Xdsl2LConfTempInmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 1, 1, 2),
    _Xdsl2LConfTempInmConfProfile_Type()
)
xdsl2LConfTempInmConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempInmConfProfile.setStatus("current")
_Xdsl2ExtLineConfProfTable_Object = MibTable
xdsl2ExtLineConfProfTable = _Xdsl2ExtLineConfProfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineConfProfTable.setStatus("current")
_Xdsl2ExtLineConfProfEntry_Object = MibTableRow
xdsl2ExtLineConfProfEntry = _Xdsl2ExtLineConfProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 2, 1)
)
xdsl2ExtLineConfProfEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineConfProfEntry.setStatus("current")
_Xdsl2LConfProfBitSwapDs_Type = Unsigned32
_Xdsl2LConfProfBitSwapDs_Object = MibTableColumn
xdsl2LConfProfBitSwapDs = _Xdsl2LConfProfBitSwapDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 2, 1, 1),
    _Xdsl2LConfProfBitSwapDs_Type()
)
xdsl2LConfProfBitSwapDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LConfProfBitSwapDs.setStatus("current")
_Xdsl2LConfProfBitSwapUs_Type = Unsigned32
_Xdsl2LConfProfBitSwapUs_Object = MibTableColumn
xdsl2LConfProfBitSwapUs = _Xdsl2LConfProfBitSwapUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 2, 1, 2),
    _Xdsl2LConfProfBitSwapUs_Type()
)
xdsl2LConfProfBitSwapUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LConfProfBitSwapUs.setStatus("current")
_Xdsl2LConfProfPortList_Type = PortList
_Xdsl2LConfProfPortList_Object = MibTableColumn
xdsl2LConfProfPortList = _Xdsl2LConfProfPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 2, 1, 3),
    _Xdsl2LConfProfPortList_Type()
)
xdsl2LConfProfPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LConfProfPortList.setStatus("current")
_Xdsl2MaxNumLineConfTemplate_Type = Unsigned32
_Xdsl2MaxNumLineConfTemplate_Object = MibScalar
xdsl2MaxNumLineConfTemplate = _Xdsl2MaxNumLineConfTemplate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 5),
    _Xdsl2MaxNumLineConfTemplate_Type()
)
xdsl2MaxNumLineConfTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumLineConfTemplate.setStatus("current")
_Xdsl2MaxNumLineConfProfile_Type = Unsigned32
_Xdsl2MaxNumLineConfProfile_Object = MibScalar
xdsl2MaxNumLineConfProfile = _Xdsl2MaxNumLineConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 6),
    _Xdsl2MaxNumLineConfProfile_Type()
)
xdsl2MaxNumLineConfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumLineConfProfile.setStatus("current")
_Xdsl2ExtInmConfProfTable_Object = MibTable
xdsl2ExtInmConfProfTable = _Xdsl2ExtInmConfProfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7)
)
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfTable.setStatus("current")
_Xdsl2ExtInmConfProfEntry_Object = MibTableRow
xdsl2ExtInmConfProfEntry = _Xdsl2ExtInmConfProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1)
)
xdsl2ExtInmConfProfEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "xdsl2ExtInmConfProfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfEntry.setStatus("current")


class _Xdsl2ExtInmConfProfProfileName_Type(SnmpAdminString):
    """Custom type xdsl2ExtInmConfProfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2ExtInmConfProfProfileName_Type.__name__ = "SnmpAdminString"
_Xdsl2ExtInmConfProfProfileName_Object = MibTableColumn
xdsl2ExtInmConfProfProfileName = _Xdsl2ExtInmConfProfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 1),
    _Xdsl2ExtInmConfProfProfileName_Type()
)
xdsl2ExtInmConfProfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfProfileName.setStatus("current")


class _Xdsl2ExtInmConfProfVtucInpEq_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVtucInpEq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xdsl2ExtInmConfProfVtucInpEq_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVtucInpEq_Object = MibTableColumn
xdsl2ExtInmConfProfVtucInpEq = _Xdsl2ExtInmConfProfVtucInpEq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 2),
    _Xdsl2ExtInmConfProfVtucInpEq_Type()
)
xdsl2ExtInmConfProfVtucInpEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVtucInpEq.setStatus("current")


class _Xdsl2ExtInmConfProfVturInpEq_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVturInpEq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xdsl2ExtInmConfProfVturInpEq_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVturInpEq_Object = MibTableColumn
xdsl2ExtInmConfProfVturInpEq = _Xdsl2ExtInmConfProfVturInpEq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 3),
    _Xdsl2ExtInmConfProfVturInpEq_Type()
)
xdsl2ExtInmConfProfVturInpEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVturInpEq.setStatus("current")


class _Xdsl2ExtInmConfProfVtucCC_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVtucCC based on Unsigned32"""
    defaultValue = 0


_Xdsl2ExtInmConfProfVtucCC_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVtucCC_Object = MibTableColumn
xdsl2ExtInmConfProfVtucCC = _Xdsl2ExtInmConfProfVtucCC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 4),
    _Xdsl2ExtInmConfProfVtucCC_Type()
)
xdsl2ExtInmConfProfVtucCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVtucCC.setStatus("current")


class _Xdsl2ExtInmConfProfVturCC_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVturCC based on Unsigned32"""
    defaultValue = 0


_Xdsl2ExtInmConfProfVturCC_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVturCC_Object = MibTableColumn
xdsl2ExtInmConfProfVturCC = _Xdsl2ExtInmConfProfVturCC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 5),
    _Xdsl2ExtInmConfProfVturCC_Type()
)
xdsl2ExtInmConfProfVturCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVturCC.setStatus("current")


class _Xdsl2ExtInmConfProfVtucIATO_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVtucIATO based on Unsigned32"""
    defaultValue = 3


_Xdsl2ExtInmConfProfVtucIATO_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVtucIATO_Object = MibTableColumn
xdsl2ExtInmConfProfVtucIATO = _Xdsl2ExtInmConfProfVtucIATO_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 6),
    _Xdsl2ExtInmConfProfVtucIATO_Type()
)
xdsl2ExtInmConfProfVtucIATO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVtucIATO.setStatus("current")


class _Xdsl2ExtInmConfProfVturIATO_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVturIATO based on Unsigned32"""
    defaultValue = 3


_Xdsl2ExtInmConfProfVturIATO_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVturIATO_Object = MibTableColumn
xdsl2ExtInmConfProfVturIATO = _Xdsl2ExtInmConfProfVturIATO_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 7),
    _Xdsl2ExtInmConfProfVturIATO_Type()
)
xdsl2ExtInmConfProfVturIATO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVturIATO.setStatus("current")


class _Xdsl2ExtInmConfProfVtucIATS_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVtucIATS based on Unsigned32"""
    defaultValue = 0


_Xdsl2ExtInmConfProfVtucIATS_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVtucIATS_Object = MibTableColumn
xdsl2ExtInmConfProfVtucIATS = _Xdsl2ExtInmConfProfVtucIATS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 8),
    _Xdsl2ExtInmConfProfVtucIATS_Type()
)
xdsl2ExtInmConfProfVtucIATS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVtucIATS.setStatus("current")


class _Xdsl2ExtInmConfProfVturIATS_Type(Unsigned32):
    """Custom type xdsl2ExtInmConfProfVturIATS based on Unsigned32"""
    defaultValue = 0


_Xdsl2ExtInmConfProfVturIATS_Type.__name__ = "Unsigned32"
_Xdsl2ExtInmConfProfVturIATS_Object = MibTableColumn
xdsl2ExtInmConfProfVturIATS = _Xdsl2ExtInmConfProfVturIATS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 9),
    _Xdsl2ExtInmConfProfVturIATS_Type()
)
xdsl2ExtInmConfProfVturIATS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfVturIATS.setStatus("current")
_Xdsl2ExtInmConfProfRowStatus_Type = RowStatus
_Xdsl2ExtInmConfProfRowStatus_Object = MibTableColumn
xdsl2ExtInmConfProfRowStatus = _Xdsl2ExtInmConfProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 14),
    _Xdsl2ExtInmConfProfRowStatus_Type()
)
xdsl2ExtInmConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfRowStatus.setStatus("current")
_Xdsl2ExtInmConfProfPortList_Type = PortList
_Xdsl2ExtInmConfProfPortList_Object = MibTableColumn
xdsl2ExtInmConfProfPortList = _Xdsl2ExtInmConfProfPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 7, 1, 15),
    _Xdsl2ExtInmConfProfPortList_Type()
)
xdsl2ExtInmConfProfPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ExtInmConfProfPortList.setStatus("current")
_Xdsl2MaxNumInmConfProfile_Type = Unsigned32
_Xdsl2MaxNumInmConfProfile_Object = MibScalar
xdsl2MaxNumInmConfProfile = _Xdsl2MaxNumInmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 1, 8),
    _Xdsl2MaxNumInmConfProfile_Type()
)
xdsl2MaxNumInmConfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumInmConfProfile.setStatus("current")
_Xdsl2ExtProfileChannel_ObjectIdentity = ObjectIdentity
xdsl2ExtProfileChannel = _Xdsl2ExtProfileChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2)
)
_Xdsl2ExtChConfProfileTable_Object = MibTable
xdsl2ExtChConfProfileTable = _Xdsl2ExtChConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtChConfProfileTable.setStatus("current")
_Xdsl2ExtChConfProfileEntry_Object = MibTableRow
xdsl2ExtChConfProfileEntry = _Xdsl2ExtChConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2, 1, 1)
)
xdsl2ExtChConfProfileEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2ChConfProfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtChConfProfileEntry.setStatus("current")
_Xdsl2ChConfProfPhyRDs_Type = Unsigned32
_Xdsl2ChConfProfPhyRDs_Object = MibTableColumn
xdsl2ChConfProfPhyRDs = _Xdsl2ChConfProfPhyRDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2, 1, 1, 1),
    _Xdsl2ChConfProfPhyRDs_Type()
)
xdsl2ChConfProfPhyRDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfPhyRDs.setStatus("current")
_Xdsl2ChConfProfPhyRUs_Type = Unsigned32
_Xdsl2ChConfProfPhyRUs_Object = MibTableColumn
xdsl2ChConfProfPhyRUs = _Xdsl2ChConfProfPhyRUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2, 1, 1, 2),
    _Xdsl2ChConfProfPhyRUs_Type()
)
xdsl2ChConfProfPhyRUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfPhyRUs.setStatus("current")
_Xdsl2ChConfProfPortList_Type = PortList
_Xdsl2ChConfProfPortList_Object = MibTableColumn
xdsl2ChConfProfPortList = _Xdsl2ChConfProfPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2, 1, 1, 3),
    _Xdsl2ChConfProfPortList_Type()
)
xdsl2ChConfProfPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChConfProfPortList.setStatus("current")
_Xdsl2MaxNumChConfProfile_Type = Unsigned32
_Xdsl2MaxNumChConfProfile_Object = MibScalar
xdsl2MaxNumChConfProfile = _Xdsl2MaxNumChConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 2, 2),
    _Xdsl2MaxNumChConfProfile_Type()
)
xdsl2MaxNumChConfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumChConfProfile.setStatus("current")
_Xdsl2ExtProfileAlarmConf_ObjectIdentity = ObjectIdentity
xdsl2ExtProfileAlarmConf = _Xdsl2ExtProfileAlarmConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3)
)
_Xdsl2ExtLineAlarmConfTemplateTable_Object = MibTable
xdsl2ExtLineAlarmConfTemplateTable = _Xdsl2ExtLineAlarmConfTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 1)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineAlarmConfTemplateTable.setStatus("current")
_Xdsl2ExtLineAlarmConfTemplateEntry_Object = MibTableRow
xdsl2ExtLineAlarmConfTemplateEntry = _Xdsl2ExtLineAlarmConfTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 1, 1)
)
xdsl2ExtLineAlarmConfTemplateEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LAlarmConfTempTemplateName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineAlarmConfTemplateEntry.setStatus("current")
_Xdsl2LAlarmConfTempPortList_Type = PortList
_Xdsl2LAlarmConfTempPortList_Object = MibTableColumn
xdsl2LAlarmConfTempPortList = _Xdsl2LAlarmConfTempPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 1, 1, 3),
    _Xdsl2LAlarmConfTempPortList_Type()
)
xdsl2LAlarmConfTempPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempPortList.setStatus("current")
_Xdsl2ExtLineAlarmConfProfileTable_Object = MibTable
xdsl2ExtLineAlarmConfProfileTable = _Xdsl2ExtLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 2)
)
if mibBuilder.loadTexts:
    xdsl2ExtLineAlarmConfProfileTable.setStatus("current")
_Xdsl2ExtLineAlarmConfProfileEntry_Object = MibTableRow
xdsl2ExtLineAlarmConfProfileEntry = _Xdsl2ExtLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 2, 1)
)
xdsl2ExtLineAlarmConfProfileEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtLineAlarmConfProfileEntry.setStatus("current")


class _Xdsl2LineAlarmConfProfileXtucThresh15MinLofs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXtucThresh15MinLofs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXtucThresh15MinLofs_Type.__name__ = "HCPerfIntervalThreshold"
_Xdsl2LineAlarmConfProfileXtucThresh15MinLofs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXtucThresh15MinLofs = _Xdsl2LineAlarmConfProfileXtucThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 2, 1, 1),
    _Xdsl2LineAlarmConfProfileXtucThresh15MinLofs_Type()
)
xdsl2LineAlarmConfProfileXtucThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinLofs.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXturThresh15MinLofs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinLofs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinLofs_Type.__name__ = "HCPerfIntervalThreshold"
_Xdsl2LineAlarmConfProfileXturThresh15MinLofs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinLofs = _Xdsl2LineAlarmConfProfileXturThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 2, 1, 2),
    _Xdsl2LineAlarmConfProfileXturThresh15MinLofs_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinLofs.setUnits("seconds")
_Xdsl2LAlarmConfProfilePortList_Type = PortList
_Xdsl2LAlarmConfProfilePortList_Object = MibTableColumn
xdsl2LAlarmConfProfilePortList = _Xdsl2LAlarmConfProfilePortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 2, 1, 3),
    _Xdsl2LAlarmConfProfilePortList_Type()
)
xdsl2LAlarmConfProfilePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfProfilePortList.setStatus("current")


class _Xdsl2LineAlarmConfProfileXturThresh15MinLprs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinLprs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinLprs_Type.__name__ = "HCPerfIntervalThreshold"
_Xdsl2LineAlarmConfProfileXturThresh15MinLprs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinLprs = _Xdsl2LineAlarmConfProfileXturThresh15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 2, 1, 4),
    _Xdsl2LineAlarmConfProfileXturThresh15MinLprs_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinLprs.setUnits("seconds")
_Xdsl2ExtChAlarmConfProfileTable_Object = MibTable
xdsl2ExtChAlarmConfProfileTable = _Xdsl2ExtChAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 3)
)
if mibBuilder.loadTexts:
    xdsl2ExtChAlarmConfProfileTable.setStatus("current")
_Xdsl2ExtChAlarmConfProfileEntry_Object = MibTableRow
xdsl2ExtChAlarmConfProfileEntry = _Xdsl2ExtChAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 3, 1)
)
xdsl2ExtChAlarmConfProfileEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ExtChAlarmConfProfileEntry.setStatus("current")
_Xdsl2ChAlarmConfProfilePortList_Type = PortList
_Xdsl2ChAlarmConfProfilePortList_Object = MibTableColumn
xdsl2ChAlarmConfProfilePortList = _Xdsl2ChAlarmConfProfilePortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 3, 1, 3),
    _Xdsl2ChAlarmConfProfilePortList_Type()
)
xdsl2ChAlarmConfProfilePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfilePortList.setStatus("current")
_Xdsl2MaxNumLineAlarmConfTemplate_Type = Unsigned32
_Xdsl2MaxNumLineAlarmConfTemplate_Object = MibScalar
xdsl2MaxNumLineAlarmConfTemplate = _Xdsl2MaxNumLineAlarmConfTemplate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 4),
    _Xdsl2MaxNumLineAlarmConfTemplate_Type()
)
xdsl2MaxNumLineAlarmConfTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumLineAlarmConfTemplate.setStatus("current")
_Xdsl2MaxNumLineAlarmConfProfile_Type = Unsigned32
_Xdsl2MaxNumLineAlarmConfProfile_Object = MibScalar
xdsl2MaxNumLineAlarmConfProfile = _Xdsl2MaxNumLineAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 5),
    _Xdsl2MaxNumLineAlarmConfProfile_Type()
)
xdsl2MaxNumLineAlarmConfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumLineAlarmConfProfile.setStatus("current")
_Xdsl2MaxNumChAlarmConfProfile_Type = Unsigned32
_Xdsl2MaxNumChAlarmConfProfile_Object = MibScalar
xdsl2MaxNumChAlarmConfProfile = _Xdsl2MaxNumChAlarmConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 5, 3, 6),
    _Xdsl2MaxNumChAlarmConfProfile_Type()
)
xdsl2MaxNumChAlarmConfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2MaxNumChAlarmConfProfile.setStatus("current")
_MacBasedVlanSetup_ObjectIdentity = ObjectIdentity
macBasedVlanSetup = _MacBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61)
)
_MacBasedVlanTable_Object = MibTable
macBasedVlanTable = _MacBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1)
)
if mibBuilder.loadTexts:
    macBasedVlanTable.setStatus("current")
_MacBasedVlanEntry_Object = MibTableRow
macBasedVlanEntry = _MacBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1, 1)
)
macBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "macBasedVlanMAC"),
)
if mibBuilder.loadTexts:
    macBasedVlanEntry.setStatus("current")
_MacBasedVlanName_Type = DisplayString
_MacBasedVlanName_Object = MibTableColumn
macBasedVlanName = _MacBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1, 1, 1),
    _MacBasedVlanName_Type()
)
macBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macBasedVlanName.setStatus("current")
_MacBasedVlanMAC_Type = MacAddress
_MacBasedVlanMAC_Object = MibTableColumn
macBasedVlanMAC = _MacBasedVlanMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1, 1, 2),
    _MacBasedVlanMAC_Type()
)
macBasedVlanMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macBasedVlanMAC.setStatus("current")
_MacBasedVlanVlanId_Type = Integer32
_MacBasedVlanVlanId_Object = MibTableColumn
macBasedVlanVlanId = _MacBasedVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1, 1, 3),
    _MacBasedVlanVlanId_Type()
)
macBasedVlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macBasedVlanVlanId.setStatus("current")
_MacBasedVlan8021pPriority_Type = Integer32
_MacBasedVlan8021pPriority_Object = MibTableColumn
macBasedVlan8021pPriority = _MacBasedVlan8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1, 1, 4),
    _MacBasedVlan8021pPriority_Type()
)
macBasedVlan8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macBasedVlan8021pPriority.setStatus("current")
_MacBasedVlanRowstatus_Type = RowStatus
_MacBasedVlanRowstatus_Object = MibTableColumn
macBasedVlanRowstatus = _MacBasedVlanRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 61, 1, 1, 5),
    _MacBasedVlanRowstatus_Type()
)
macBasedVlanRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macBasedVlanRowstatus.setStatus("current")
_VlanProfileSetup_ObjectIdentity = ObjectIdentity
vlanProfileSetup = _VlanProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62)
)
_VlanProfileTable_Object = MibTable
vlanProfileTable = _VlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 1)
)
if mibBuilder.loadTexts:
    vlanProfileTable.setStatus("current")
_VlanProfileEntry_Object = MibTableRow
vlanProfileEntry = _VlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 1, 1)
)
vlanProfileEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "vlanProfileName"),
)
if mibBuilder.loadTexts:
    vlanProfileEntry.setStatus("current")
_VlanProfileName_Type = DisplayString
_VlanProfileName_Object = MibTableColumn
vlanProfileName = _VlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 1, 1, 1),
    _VlanProfileName_Type()
)
vlanProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanProfileName.setStatus("current")


class _VlanProfileMacLearning_Type(Integer32):
    """Custom type vlanProfileMacLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VlanProfileMacLearning_Type.__name__ = "Integer32"
_VlanProfileMacLearning_Object = MibTableColumn
vlanProfileMacLearning = _VlanProfileMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 1, 1, 2),
    _VlanProfileMacLearning_Type()
)
vlanProfileMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanProfileMacLearning.setStatus("current")


class _VlanProfileUnknownMulticastDrop_Type(Integer32):
    """Custom type vlanProfileUnknownMulticastDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VlanProfileUnknownMulticastDrop_Type.__name__ = "Integer32"
_VlanProfileUnknownMulticastDrop_Object = MibTableColumn
vlanProfileUnknownMulticastDrop = _VlanProfileUnknownMulticastDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 1, 1, 3),
    _VlanProfileUnknownMulticastDrop_Type()
)
vlanProfileUnknownMulticastDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanProfileUnknownMulticastDrop.setStatus("current")
_VlanProfileRowStatus_Type = RowStatus
_VlanProfileRowStatus_Object = MibTableColumn
vlanProfileRowStatus = _VlanProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 1, 1, 4),
    _VlanProfileRowStatus_Type()
)
vlanProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanProfileRowStatus.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 2)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 2, 1)
)
vlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_ProfileName_Type = DisplayString
_ProfileName_Object = MibTableColumn
profileName = _ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 62, 2, 1, 1),
    _ProfileName_Type()
)
profileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileName.setStatus("current")
_DosPreventionSetup_ObjectIdentity = ObjectIdentity
dosPreventionSetup = _DosPreventionSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63)
)


class _DosPreventionActive_Type(Integer32):
    """Custom type dosPreventionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionActive_Type.__name__ = "Integer32"
_DosPreventionActive_Object = MibScalar
dosPreventionActive = _DosPreventionActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 1),
    _DosPreventionActive_Type()
)
dosPreventionActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionActive.setStatus("current")


class _DosPreventionMacChecking_Type(Integer32):
    """Custom type dosPreventionMacChecking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionMacChecking_Type.__name__ = "Integer32"
_DosPreventionMacChecking_Object = MibScalar
dosPreventionMacChecking = _DosPreventionMacChecking_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 4),
    _DosPreventionMacChecking_Type()
)
dosPreventionMacChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionMacChecking.setStatus("current")


class _DosPreventionIPChecking_Type(Integer32):
    """Custom type dosPreventionIPChecking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionIPChecking_Type.__name__ = "Integer32"
_DosPreventionIPChecking_Object = MibScalar
dosPreventionIPChecking = _DosPreventionIPChecking_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 5),
    _DosPreventionIPChecking_Type()
)
dosPreventionIPChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionIPChecking.setStatus("current")


class _DosPreventionICMPFragment_Type(Integer32):
    """Custom type dosPreventionICMPFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionICMPFragment_Type.__name__ = "Integer32"
_DosPreventionICMPFragment_Object = MibScalar
dosPreventionICMPFragment = _DosPreventionICMPFragment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 9),
    _DosPreventionICMPFragment_Type()
)
dosPreventionICMPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionICMPFragment.setStatus("current")


class _DosPreventionTCPSYN_Type(Integer32):
    """Custom type dosPreventionTCPSYN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionTCPSYN_Type.__name__ = "Integer32"
_DosPreventionTCPSYN_Object = MibScalar
dosPreventionTCPSYN = _DosPreventionTCPSYN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 11),
    _DosPreventionTCPSYN_Type()
)
dosPreventionTCPSYN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionTCPSYN.setStatus("current")


class _DosPreventionTCPFragment_Type(Integer32):
    """Custom type dosPreventionTCPFragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionTCPFragment_Type.__name__ = "Integer32"
_DosPreventionTCPFragment_Object = MibScalar
dosPreventionTCPFragment = _DosPreventionTCPFragment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 13),
    _DosPreventionTCPFragment_Type()
)
dosPreventionTCPFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionTCPFragment.setStatus("current")


class _DosPreventionTCPControlSN_Type(Integer32):
    """Custom type dosPreventionTCPControlSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionTCPControlSN_Type.__name__ = "Integer32"
_DosPreventionTCPControlSN_Object = MibScalar
dosPreventionTCPControlSN = _DosPreventionTCPControlSN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 14),
    _DosPreventionTCPControlSN_Type()
)
dosPreventionTCPControlSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionTCPControlSN.setStatus("current")


class _DosPreventionTCPPort_Type(Integer32):
    """Custom type dosPreventionTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionTCPPort_Type.__name__ = "Integer32"
_DosPreventionTCPPort_Object = MibScalar
dosPreventionTCPPort = _DosPreventionTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 15),
    _DosPreventionTCPPort_Type()
)
dosPreventionTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionTCPPort.setStatus("current")


class _DosPreventionTCPSF_Type(Integer32):
    """Custom type dosPreventionTCPSF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionTCPSF_Type.__name__ = "Integer32"
_DosPreventionTCPSF_Object = MibScalar
dosPreventionTCPSF = _DosPreventionTCPSF_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 16),
    _DosPreventionTCPSF_Type()
)
dosPreventionTCPSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionTCPSF.setStatus("current")


class _DosPreventionTCPFUP_Type(Integer32):
    """Custom type dosPreventionTCPFUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionTCPFUP_Type.__name__ = "Integer32"
_DosPreventionTCPFUP_Object = MibScalar
dosPreventionTCPFUP = _DosPreventionTCPFUP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 17),
    _DosPreventionTCPFUP_Type()
)
dosPreventionTCPFUP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionTCPFUP.setStatus("current")


class _DosPreventionUDPPort_Type(Integer32):
    """Custom type dosPreventionUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DosPreventionUDPPort_Type.__name__ = "Integer32"
_DosPreventionUDPPort_Object = MibScalar
dosPreventionUDPPort = _DosPreventionUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 63, 18),
    _DosPreventionUDPPort_Type()
)
dosPreventionUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosPreventionUDPPort.setStatus("current")
_Ipv6Setup_ObjectIdentity = ObjectIdentity
ipv6Setup = _Ipv6Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65)
)


class _Ipv6DefaultMgmt_Type(Integer32):
    """Custom type ipv6DefaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-band", 0),
          ("out-of-band", 1))
    )


_Ipv6DefaultMgmt_Type.__name__ = "Integer32"
_Ipv6DefaultMgmt_Object = MibScalar
ipv6DefaultMgmt = _Ipv6DefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 2),
    _Ipv6DefaultMgmt_Type()
)
ipv6DefaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultMgmt.setStatus("current")
_InbandIpv6Setup_ObjectIdentity = ObjectIdentity
inbandIpv6Setup = _InbandIpv6Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 3)
)
_InbandIpv6Vid_Type = Integer32
_InbandIpv6Vid_Object = MibScalar
inbandIpv6Vid = _InbandIpv6Vid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 3, 2),
    _InbandIpv6Vid_Type()
)
inbandIpv6Vid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpv6Vid.setStatus("current")
_InbandIpv6StaticIp_Type = Ipv6Address
_InbandIpv6StaticIp_Object = MibScalar
inbandIpv6StaticIp = _InbandIpv6StaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 3, 3),
    _InbandIpv6StaticIp_Type()
)
inbandIpv6StaticIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpv6StaticIp.setStatus("current")
_InbandIpv6StaticSubnetMask_Type = Ipv6Address
_InbandIpv6StaticSubnetMask_Object = MibScalar
inbandIpv6StaticSubnetMask = _InbandIpv6StaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 3, 4),
    _InbandIpv6StaticSubnetMask_Type()
)
inbandIpv6StaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpv6StaticSubnetMask.setStatus("current")
_InbandIpv6StaticGateway_Type = Ipv6Address
_InbandIpv6StaticGateway_Object = MibScalar
inbandIpv6StaticGateway = _InbandIpv6StaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 3, 5),
    _InbandIpv6StaticGateway_Type()
)
inbandIpv6StaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpv6StaticGateway.setStatus("current")
_OutOfBandIpv6Setup_ObjectIdentity = ObjectIdentity
outOfBandIpv6Setup = _OutOfBandIpv6Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 4)
)
_OutOfBandIpv6Ip_Type = Ipv6Address
_OutOfBandIpv6Ip_Object = MibScalar
outOfBandIpv6Ip = _OutOfBandIpv6Ip_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 4, 1),
    _OutOfBandIpv6Ip_Type()
)
outOfBandIpv6Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIpv6Ip.setStatus("current")
_OutOfBandIpv6SubnetMask_Type = Ipv6Address
_OutOfBandIpv6SubnetMask_Object = MibScalar
outOfBandIpv6SubnetMask = _OutOfBandIpv6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 4, 2),
    _OutOfBandIpv6SubnetMask_Type()
)
outOfBandIpv6SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIpv6SubnetMask.setStatus("current")
_OutOfBandIpv6Gateway_Type = Ipv6Address
_OutOfBandIpv6Gateway_Object = MibScalar
outOfBandIpv6Gateway = _OutOfBandIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 65, 4, 3),
    _OutOfBandIpv6Gateway_Type()
)
outOfBandIpv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIpv6Gateway.setStatus("current")
_L2ptSetup_ObjectIdentity = ObjectIdentity
l2ptSetup = _L2ptSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115)
)
_L2ptState_Type = EnabledStatus
_L2ptState_Object = MibScalar
l2ptState = _L2ptState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 1),
    _L2ptState_Type()
)
l2ptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptState.setStatus("current")
_L2ptMacAddr_Type = MacAddress
_L2ptMacAddr_Object = MibScalar
l2ptMacAddr = _L2ptMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 2),
    _L2ptMacAddr_Type()
)
l2ptMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptMacAddr.setStatus("current")
_L2ptTable_Object = MibTable
l2ptTable = _L2ptTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 3)
)
if mibBuilder.loadTexts:
    l2ptTable.setStatus("current")
_L2ptEntry_Object = MibTableRow
l2ptEntry = _L2ptEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 3, 1)
)
l2ptEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    l2ptEntry.setStatus("current")


class _L2ptProtocolGroup_Type(Bits):
    """Custom type l2ptProtocolGroup based on Bits"""
    namedValues = NamedValues(
        *(("cDP", 0),
          ("sTP", 1),
          ("vTP", 2))
    )

_L2ptProtocolGroup_Type.__name__ = "Bits"
_L2ptProtocolGroup_Object = MibTableColumn
l2ptProtocolGroup = _L2ptProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 3, 1, 1),
    _L2ptProtocolGroup_Type()
)
l2ptProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptProtocolGroup.setStatus("current")


class _L2ptPointToPointProtocolGroup_Type(Bits):
    """Custom type l2ptPointToPointProtocolGroup based on Bits"""
    namedValues = NamedValues(
        *(("pAGP", 0),
          ("lACP", 1),
          ("uDLD", 2))
    )

_L2ptPointToPointProtocolGroup_Type.__name__ = "Bits"
_L2ptPointToPointProtocolGroup_Object = MibTableColumn
l2ptPointToPointProtocolGroup = _L2ptPointToPointProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 3, 1, 2),
    _L2ptPointToPointProtocolGroup_Type()
)
l2ptPointToPointProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptPointToPointProtocolGroup.setStatus("current")


class _L2ptMode_Type(Integer32):
    """Custom type l2ptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("tunnel", 2))
    )


_L2ptMode_Type.__name__ = "Integer32"
_L2ptMode_Object = MibTableColumn
l2ptMode = _L2ptMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 115, 3, 1, 3),
    _L2ptMode_Type()
)
l2ptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptMode.setStatus("current")
_VlanMappingSetup_ObjectIdentity = ObjectIdentity
vlanMappingSetup = _VlanMappingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116)
)
_VlanMappingState_Type = EnabledStatus
_VlanMappingState_Object = MibScalar
vlanMappingState = _VlanMappingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 1),
    _VlanMappingState_Type()
)
vlanMappingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingState.setStatus("current")
_VlanMappingPortTable_Object = MibTable
vlanMappingPortTable = _VlanMappingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 2)
)
if mibBuilder.loadTexts:
    vlanMappingPortTable.setStatus("current")
_VlanMappingPortEntry_Object = MibTableRow
vlanMappingPortEntry = _VlanMappingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 2, 1)
)
vlanMappingPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanMappingPortEntry.setStatus("current")
_VlanMappingPortState_Type = EnabledStatus
_VlanMappingPortState_Object = MibTableColumn
vlanMappingPortState = _VlanMappingPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 2, 1, 1),
    _VlanMappingPortState_Type()
)
vlanMappingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingPortState.setStatus("current")
_VlanMappingPortDropMiss_Type = EnabledStatus
_VlanMappingPortDropMiss_Object = MibTableColumn
vlanMappingPortDropMiss = _VlanMappingPortDropMiss_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 2, 1, 2),
    _VlanMappingPortDropMiss_Type()
)
vlanMappingPortDropMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingPortDropMiss.setStatus("current")
_VlanMappingRuleTable_Object = MibTable
vlanMappingRuleTable = _VlanMappingRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3)
)
if mibBuilder.loadTexts:
    vlanMappingRuleTable.setStatus("current")
_VlanMappingRuleEntry_Object = MibTableRow
vlanMappingRuleEntry = _VlanMappingRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1)
)
vlanMappingRuleEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "vlanMappingRulePort"),
    (0, "ZYXEL-ves1608FE57-MIB", "vlanMappingRuleVid"),
)
if mibBuilder.loadTexts:
    vlanMappingRuleEntry.setStatus("current")
_VlanMappingRuleName_Type = DisplayString
_VlanMappingRuleName_Object = MibTableColumn
vlanMappingRuleName = _VlanMappingRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 1),
    _VlanMappingRuleName_Type()
)
vlanMappingRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRuleName.setStatus("current")
_VlanMappingRulePort_Type = Integer32
_VlanMappingRulePort_Object = MibTableColumn
vlanMappingRulePort = _VlanMappingRulePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 2),
    _VlanMappingRulePort_Type()
)
vlanMappingRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMappingRulePort.setStatus("current")
_VlanMappingRuleVid_Type = Integer32
_VlanMappingRuleVid_Object = MibTableColumn
vlanMappingRuleVid = _VlanMappingRuleVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 3),
    _VlanMappingRuleVid_Type()
)
vlanMappingRuleVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMappingRuleVid.setStatus("current")
_VlanMappingRuleTransVid_Type = Integer32
_VlanMappingRuleTransVid_Object = MibTableColumn
vlanMappingRuleTransVid = _VlanMappingRuleTransVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 4),
    _VlanMappingRuleTransVid_Type()
)
vlanMappingRuleTransVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRuleTransVid.setStatus("current")


class _VlanMappingRulePriority_Type(Integer32):
    """Custom type vlanMappingRulePriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_VlanMappingRulePriority_Type.__name__ = "Integer32"
_VlanMappingRulePriority_Object = MibTableColumn
vlanMappingRulePriority = _VlanMappingRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 5),
    _VlanMappingRulePriority_Type()
)
vlanMappingRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRulePriority.setStatus("current")
_VlanMappingRuleRowStatus_Type = RowStatus
_VlanMappingRuleRowStatus_Object = MibTableColumn
vlanMappingRuleRowStatus = _VlanMappingRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 6),
    _VlanMappingRuleRowStatus_Type()
)
vlanMappingRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMappingRuleRowStatus.setStatus("current")
_VlanMappingRuleReplacePrio_Type = EnabledStatus
_VlanMappingRuleReplacePrio_Object = MibTableColumn
vlanMappingRuleReplacePrio = _VlanMappingRuleReplacePrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 116, 3, 1, 7),
    _VlanMappingRuleReplacePrio_Type()
)
vlanMappingRuleReplacePrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRuleReplacePrio.setStatus("current")
_TransceiverInfo_ObjectIdentity = ObjectIdentity
transceiverInfo = _TransceiverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117)
)
_TransceiverSerialInfoTable_Object = MibTable
transceiverSerialInfoTable = _TransceiverSerialInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1)
)
if mibBuilder.loadTexts:
    transceiverSerialInfoTable.setStatus("current")
_TransceiverSerialInfoEntry_Object = MibTableRow
transceiverSerialInfoEntry = _TransceiverSerialInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1)
)
transceiverSerialInfoEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "transceiverSerialInfoEntryPort"),
)
if mibBuilder.loadTexts:
    transceiverSerialInfoEntry.setStatus("current")
_TransceiverSerialInfoEntryPort_Type = Integer32
_TransceiverSerialInfoEntryPort_Object = MibTableColumn
transceiverSerialInfoEntryPort = _TransceiverSerialInfoEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 1),
    _TransceiverSerialInfoEntryPort_Type()
)
transceiverSerialInfoEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryPort.setStatus("current")


class _TransceiverSerialInfoEntryStatus_Type(Integer32):
    """Custom type transceiverSerialInfoEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok-with-DDM", 1),
          ("ok-without-DDM", 2),
          ("nonoperational", 3))
    )


_TransceiverSerialInfoEntryStatus_Type.__name__ = "Integer32"
_TransceiverSerialInfoEntryStatus_Object = MibTableColumn
transceiverSerialInfoEntryStatus = _TransceiverSerialInfoEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 2),
    _TransceiverSerialInfoEntryStatus_Type()
)
transceiverSerialInfoEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryStatus.setStatus("current")
_TransceiverSerialInfoEntryVendor_Type = DisplayString
_TransceiverSerialInfoEntryVendor_Object = MibTableColumn
transceiverSerialInfoEntryVendor = _TransceiverSerialInfoEntryVendor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 3),
    _TransceiverSerialInfoEntryVendor_Type()
)
transceiverSerialInfoEntryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryVendor.setStatus("current")
_TransceiverSerialInfoEntryPartNo_Type = DisplayString
_TransceiverSerialInfoEntryPartNo_Object = MibTableColumn
transceiverSerialInfoEntryPartNo = _TransceiverSerialInfoEntryPartNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 4),
    _TransceiverSerialInfoEntryPartNo_Type()
)
transceiverSerialInfoEntryPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryPartNo.setStatus("current")
_TransceiverSerialInfoEntrySerialNo_Type = DisplayString
_TransceiverSerialInfoEntrySerialNo_Object = MibTableColumn
transceiverSerialInfoEntrySerialNo = _TransceiverSerialInfoEntrySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 5),
    _TransceiverSerialInfoEntrySerialNo_Type()
)
transceiverSerialInfoEntrySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntrySerialNo.setStatus("current")
_TransceiverSerialInfoEntryRevision_Type = DisplayString
_TransceiverSerialInfoEntryRevision_Object = MibTableColumn
transceiverSerialInfoEntryRevision = _TransceiverSerialInfoEntryRevision_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 6),
    _TransceiverSerialInfoEntryRevision_Type()
)
transceiverSerialInfoEntryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryRevision.setStatus("current")
_TransceiverSerialInfoEntryDateCode_Type = DisplayString
_TransceiverSerialInfoEntryDateCode_Object = MibTableColumn
transceiverSerialInfoEntryDateCode = _TransceiverSerialInfoEntryDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 7),
    _TransceiverSerialInfoEntryDateCode_Type()
)
transceiverSerialInfoEntryDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryDateCode.setStatus("current")
_TransceiverSerialInfoEntryTransceiver_Type = DisplayString
_TransceiverSerialInfoEntryTransceiver_Object = MibTableColumn
transceiverSerialInfoEntryTransceiver = _TransceiverSerialInfoEntryTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 1, 1, 8),
    _TransceiverSerialInfoEntryTransceiver_Type()
)
transceiverSerialInfoEntryTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryTransceiver.setStatus("current")
_TransceiverDdmInfoTable_Object = MibTable
transceiverDdmInfoTable = _TransceiverDdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2)
)
if mibBuilder.loadTexts:
    transceiverDdmInfoTable.setStatus("current")
_TransceiverDdmInfoEntry_Object = MibTableRow
transceiverDdmInfoEntry = _TransceiverDdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1)
)
transceiverDdmInfoEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "transceiverDdmInfoEntryPort"),
    (0, "ZYXEL-ves1608FE57-MIB", "transceiverDdmInfoEntryType"),
)
if mibBuilder.loadTexts:
    transceiverDdmInfoEntry.setStatus("current")
_TransceiverDdmInfoEntryPort_Type = Integer32
_TransceiverDdmInfoEntryPort_Object = MibTableColumn
transceiverDdmInfoEntryPort = _TransceiverDdmInfoEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 1),
    _TransceiverDdmInfoEntryPort_Type()
)
transceiverDdmInfoEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryPort.setStatus("current")


class _TransceiverDdmInfoEntryType_Type(Integer32):
    """Custom type transceiverDdmInfoEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("voltage", 2),
          ("bias", 3),
          ("txPower", 4),
          ("rxPower", 5))
    )


_TransceiverDdmInfoEntryType_Type.__name__ = "Integer32"
_TransceiverDdmInfoEntryType_Object = MibTableColumn
transceiverDdmInfoEntryType = _TransceiverDdmInfoEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 2),
    _TransceiverDdmInfoEntryType_Type()
)
transceiverDdmInfoEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryType.setStatus("current")
_TransceiverDdmInfoEntryAlarmMax_Type = Integer32
_TransceiverDdmInfoEntryAlarmMax_Object = MibTableColumn
transceiverDdmInfoEntryAlarmMax = _TransceiverDdmInfoEntryAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 3),
    _TransceiverDdmInfoEntryAlarmMax_Type()
)
transceiverDdmInfoEntryAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMax.setStatus("current")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMax.setUnits("0.01")
_TransceiverDdmInfoEntryAlarmMin_Type = Integer32
_TransceiverDdmInfoEntryAlarmMin_Object = MibTableColumn
transceiverDdmInfoEntryAlarmMin = _TransceiverDdmInfoEntryAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 4),
    _TransceiverDdmInfoEntryAlarmMin_Type()
)
transceiverDdmInfoEntryAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMin.setStatus("current")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMin.setUnits("0.01")
_TransceiverDdmInfoEntryWarnMax_Type = Integer32
_TransceiverDdmInfoEntryWarnMax_Object = MibTableColumn
transceiverDdmInfoEntryWarnMax = _TransceiverDdmInfoEntryWarnMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 5),
    _TransceiverDdmInfoEntryWarnMax_Type()
)
transceiverDdmInfoEntryWarnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMax.setStatus("current")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMax.setUnits("0.01")
_TransceiverDdmInfoEntryWarnMin_Type = Integer32
_TransceiverDdmInfoEntryWarnMin_Object = MibTableColumn
transceiverDdmInfoEntryWarnMin = _TransceiverDdmInfoEntryWarnMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 6),
    _TransceiverDdmInfoEntryWarnMin_Type()
)
transceiverDdmInfoEntryWarnMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMin.setStatus("current")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMin.setUnits("0.01")
_TransceiverDdmInfoEntryCurrent_Type = Integer32
_TransceiverDdmInfoEntryCurrent_Object = MibTableColumn
transceiverDdmInfoEntryCurrent = _TransceiverDdmInfoEntryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 7),
    _TransceiverDdmInfoEntryCurrent_Type()
)
transceiverDdmInfoEntryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryCurrent.setUnits("0.01")
_TransceiverDdmInfoEntryDescription_Type = DisplayString
_TransceiverDdmInfoEntryDescription_Object = MibTableColumn
transceiverDdmInfoEntryDescription = _TransceiverDdmInfoEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 117, 2, 1, 8),
    _TransceiverDdmInfoEntryDescription_Type()
)
transceiverDdmInfoEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryDescription.setStatus("current")
_PppoeIASetup_ObjectIdentity = ObjectIdentity
pppoeIASetup = _PppoeIASetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119)
)
_GlobalPPPoEIA_ObjectIdentity = ObjectIdentity
globalPPPoEIA = _GlobalPPPoEIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1)
)
_GlobalPPPoEIAEnable_Type = EnabledStatus
_GlobalPPPoEIAEnable_Object = MibScalar
globalPPPoEIAEnable = _GlobalPPPoEIAEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 1),
    _GlobalPPPoEIAEnable_Type()
)
globalPPPoEIAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIAEnable.setStatus("current")
_GlobalPPPoEIACircuitIDInfoEnable_Type = EnabledStatus
_GlobalPPPoEIACircuitIDInfoEnable_Object = MibScalar
globalPPPoEIACircuitIDInfoEnable = _GlobalPPPoEIACircuitIDInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 2),
    _GlobalPPPoEIACircuitIDInfoEnable_Type()
)
globalPPPoEIACircuitIDInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIACircuitIDInfoEnable.setStatus("current")
_GlobalPPPoEIACircuitIDInfoData_Type = DisplayString
_GlobalPPPoEIACircuitIDInfoData_Object = MibScalar
globalPPPoEIACircuitIDInfoData = _GlobalPPPoEIACircuitIDInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 3),
    _GlobalPPPoEIACircuitIDInfoData_Type()
)
globalPPPoEIACircuitIDInfoData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIACircuitIDInfoData.setStatus("current")
_GlobalPPPoEIARemoteIDEnable_Type = EnabledStatus
_GlobalPPPoEIARemoteIDEnable_Object = MibScalar
globalPPPoEIARemoteIDEnable = _GlobalPPPoEIARemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 4),
    _GlobalPPPoEIARemoteIDEnable_Type()
)
globalPPPoEIARemoteIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIARemoteIDEnable.setStatus("current")
_GlobalPPPoEIARemoteIDData_Type = DisplayString
_GlobalPPPoEIARemoteIDData_Object = MibScalar
globalPPPoEIARemoteIDData = _GlobalPPPoEIARemoteIDData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 5),
    _GlobalPPPoEIARemoteIDData_Type()
)
globalPPPoEIARemoteIDData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIARemoteIDData.setStatus("current")


class _GlobalPPPoEIARemoteIDType_Type(Integer32):
    """Custom type globalPPPoEIARemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("system", 2))
    )


_GlobalPPPoEIARemoteIDType_Type.__name__ = "Integer32"
_GlobalPPPoEIARemoteIDType_Object = MibScalar
globalPPPoEIARemoteIDType = _GlobalPPPoEIARemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 6),
    _GlobalPPPoEIARemoteIDType_Type()
)
globalPPPoEIARemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIARemoteIDType.setStatus("current")


class _GlobalPPPoEIACircuitIDType_Type(Integer32):
    """Custom type globalPPPoEIACircuitIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostname", 1),
          ("system", 2))
    )


_GlobalPPPoEIACircuitIDType_Type.__name__ = "Integer32"
_GlobalPPPoEIACircuitIDType_Object = MibScalar
globalPPPoEIACircuitIDType = _GlobalPPPoEIACircuitIDType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 1, 7),
    _GlobalPPPoEIACircuitIDType_Type()
)
globalPPPoEIACircuitIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPPPoEIACircuitIDType.setStatus("current")
_PppoeIA_ObjectIdentity = ObjectIdentity
pppoeIA = _PppoeIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2)
)
_MaxNumberOfPPPoEIA_Type = Integer32
_MaxNumberOfPPPoEIA_Object = MibScalar
maxNumberOfPPPoEIA = _MaxNumberOfPPPoEIA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 1),
    _MaxNumberOfPPPoEIA_Type()
)
maxNumberOfPPPoEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfPPPoEIA.setStatus("current")
_PppoeIATable_Object = MibTable
pppoeIATable = _PppoeIATable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2)
)
if mibBuilder.loadTexts:
    pppoeIATable.setStatus("current")
_PppoeIAEntry_Object = MibTableRow
pppoeIAEntry = _PppoeIAEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1)
)
pppoeIAEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "pppoeIAVID"),
)
if mibBuilder.loadTexts:
    pppoeIAEntry.setStatus("current")
_PppoeIAVID_Type = Integer32
_PppoeIAVID_Object = MibTableColumn
pppoeIAVID = _PppoeIAVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 1),
    _PppoeIAVID_Type()
)
pppoeIAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIAVID.setStatus("current")
_PppoeIACircuitIDInfoEnable_Type = EnabledStatus
_PppoeIACircuitIDInfoEnable_Object = MibTableColumn
pppoeIACircuitIDInfoEnable = _PppoeIACircuitIDInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 2),
    _PppoeIACircuitIDInfoEnable_Type()
)
pppoeIACircuitIDInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIACircuitIDInfoEnable.setStatus("current")
_PppoeIACircuitIDInfoData_Type = DisplayString
_PppoeIACircuitIDInfoData_Object = MibTableColumn
pppoeIACircuitIDInfoData = _PppoeIACircuitIDInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 3),
    _PppoeIACircuitIDInfoData_Type()
)
pppoeIACircuitIDInfoData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIACircuitIDInfoData.setStatus("current")
_PppoeIARemoteIDEnable_Type = EnabledStatus
_PppoeIARemoteIDEnable_Object = MibTableColumn
pppoeIARemoteIDEnable = _PppoeIARemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 4),
    _PppoeIARemoteIDEnable_Type()
)
pppoeIARemoteIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIARemoteIDEnable.setStatus("current")
_PppoeIARemoteIDData_Type = DisplayString
_PppoeIARemoteIDData_Object = MibTableColumn
pppoeIARemoteIDData = _PppoeIARemoteIDData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 5),
    _PppoeIARemoteIDData_Type()
)
pppoeIARemoteIDData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIARemoteIDData.setStatus("current")
_PppoeIARowStatus_Type = RowStatus
_PppoeIARowStatus_Object = MibTableColumn
pppoeIARowStatus = _PppoeIARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 6),
    _PppoeIARowStatus_Type()
)
pppoeIARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeIARowStatus.setStatus("current")


class _PppoeIARemoteIDType_Type(Integer32):
    """Custom type pppoeIARemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("system", 2))
    )


_PppoeIARemoteIDType_Type.__name__ = "Integer32"
_PppoeIARemoteIDType_Object = MibTableColumn
pppoeIARemoteIDType = _PppoeIARemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 7),
    _PppoeIARemoteIDType_Type()
)
pppoeIARemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIARemoteIDType.setStatus("current")


class _PppoeIACircuitIDType_Type(Integer32):
    """Custom type pppoeIACircuitIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostname", 1),
          ("system", 2))
    )


_PppoeIACircuitIDType_Type.__name__ = "Integer32"
_PppoeIACircuitIDType_Object = MibTableColumn
pppoeIACircuitIDType = _PppoeIACircuitIDType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 119, 2, 2, 1, 8),
    _PppoeIACircuitIDType_Type()
)
pppoeIACircuitIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIACircuitIDType.setStatus("current")
_IwfSetup_ObjectIdentity = ObjectIdentity
iwfSetup = _IwfSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120)
)
_PvcRuleTable_Object = MibTable
pvcRuleTable = _PvcRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1)
)
if mibBuilder.loadTexts:
    pvcRuleTable.setStatus("current")
_PvcRuleEntry_Object = MibTableRow
pvcRuleEntry = _PvcRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1)
)
pvcRuleEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "pvcRulePort"),
    (0, "ZYXEL-ves1608FE57-MIB", "pvcRuleVpi"),
    (0, "ZYXEL-ves1608FE57-MIB", "pvcRuleVci"),
)
if mibBuilder.loadTexts:
    pvcRuleEntry.setStatus("current")
_PvcRulePort_Type = Integer32
_PvcRulePort_Object = MibTableColumn
pvcRulePort = _PvcRulePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 1),
    _PvcRulePort_Type()
)
pvcRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcRulePort.setStatus("current")
_PvcRuleVpi_Type = Integer32
_PvcRuleVpi_Object = MibTableColumn
pvcRuleVpi = _PvcRuleVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 2),
    _PvcRuleVpi_Type()
)
pvcRuleVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcRuleVpi.setStatus("current")
_PvcRuleVci_Type = Integer32
_PvcRuleVci_Object = MibTableColumn
pvcRuleVci = _PvcRuleVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 3),
    _PvcRuleVci_Type()
)
pvcRuleVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcRuleVci.setStatus("current")
_PvcRulePvid_Type = Integer32
_PvcRulePvid_Object = MibTableColumn
pvcRulePvid = _PvcRulePvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 4),
    _PvcRulePvid_Type()
)
pvcRulePvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRulePvid.setStatus("current")


class _PvcRuleEncap_Type(Integer32):
    """Custom type pvcRuleEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("llc", 0),
          ("vc", 1))
    )


_PvcRuleEncap_Type.__name__ = "Integer32"
_PvcRuleEncap_Object = MibTableColumn
pvcRuleEncap = _PvcRuleEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 5),
    _PvcRuleEncap_Type()
)
pvcRuleEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRuleEncap.setStatus("current")


class _PvcRulePriority_Type(Integer32):
    """Custom type pvcRulePriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_PvcRulePriority_Type.__name__ = "Integer32"
_PvcRulePriority_Object = MibTableColumn
pvcRulePriority = _PvcRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 6),
    _PvcRulePriority_Type()
)
pvcRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRulePriority.setStatus("current")


class _PvcRuleFCS_Type(Integer32):
    """Custom type pvcRuleFCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fcs", 0),
          ("no-fcs", 1))
    )


_PvcRuleFCS_Type.__name__ = "Integer32"
_PvcRuleFCS_Object = MibTableColumn
pvcRuleFCS = _PvcRuleFCS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 7),
    _PvcRuleFCS_Type()
)
pvcRuleFCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRuleFCS.setStatus("current")
_PvcRuleMVlan_Type = EnabledStatus
_PvcRuleMVlan_Object = MibTableColumn
pvcRuleMVlan = _PvcRuleMVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 8),
    _PvcRuleMVlan_Type()
)
pvcRuleMVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRuleMVlan.setStatus("current")
_PvcRuleRowStatus_Type = RowStatus
_PvcRuleRowStatus_Object = MibTableColumn
pvcRuleRowStatus = _PvcRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 1, 1, 9),
    _PvcRuleRowStatus_Type()
)
pvcRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pvcRuleRowStatus.setStatus("current")
_IppvcRuleTable_Object = MibTable
ippvcRuleTable = _IppvcRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2)
)
if mibBuilder.loadTexts:
    ippvcRuleTable.setStatus("current")
_IppvcRuleEntry_Object = MibTableRow
ippvcRuleEntry = _IppvcRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1)
)
ippvcRuleEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "ippvcRulePort"),
    (0, "ZYXEL-ves1608FE57-MIB", "ippvcRuleVpi"),
    (0, "ZYXEL-ves1608FE57-MIB", "ippvcRuleVci"),
)
if mibBuilder.loadTexts:
    ippvcRuleEntry.setStatus("current")
_IppvcRulePort_Type = Integer32
_IppvcRulePort_Object = MibTableColumn
ippvcRulePort = _IppvcRulePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 1),
    _IppvcRulePort_Type()
)
ippvcRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ippvcRulePort.setStatus("current")
_IppvcRuleVpi_Type = Integer32
_IppvcRuleVpi_Object = MibTableColumn
ippvcRuleVpi = _IppvcRuleVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 2),
    _IppvcRuleVpi_Type()
)
ippvcRuleVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ippvcRuleVpi.setStatus("current")
_IppvcRuleVci_Type = Integer32
_IppvcRuleVci_Object = MibTableColumn
ippvcRuleVci = _IppvcRuleVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 3),
    _IppvcRuleVci_Type()
)
ippvcRuleVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ippvcRuleVci.setStatus("current")
_IppvcRulePvid_Type = Integer32
_IppvcRulePvid_Object = MibTableColumn
ippvcRulePvid = _IppvcRulePvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 4),
    _IppvcRulePvid_Type()
)
ippvcRulePvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ippvcRulePvid.setStatus("current")


class _IppvcRuleEncap_Type(Integer32):
    """Custom type ippvcRuleEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("llc", 0),
          ("vc", 1))
    )


_IppvcRuleEncap_Type.__name__ = "Integer32"
_IppvcRuleEncap_Object = MibTableColumn
ippvcRuleEncap = _IppvcRuleEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 5),
    _IppvcRuleEncap_Type()
)
ippvcRuleEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ippvcRuleEncap.setStatus("current")


class _IppvcRulePriority_Type(Integer32):
    """Custom type ippvcRulePriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_IppvcRulePriority_Type.__name__ = "Integer32"
_IppvcRulePriority_Object = MibTableColumn
ippvcRulePriority = _IppvcRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 6),
    _IppvcRulePriority_Type()
)
ippvcRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ippvcRulePriority.setStatus("current")
_IppvcRuleSubnetIp_Type = IpAddress
_IppvcRuleSubnetIp_Object = MibTableColumn
ippvcRuleSubnetIp = _IppvcRuleSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 7),
    _IppvcRuleSubnetIp_Type()
)
ippvcRuleSubnetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ippvcRuleSubnetIp.setStatus("current")
_IppvcRuleSubnetMask_Type = IpAddress
_IppvcRuleSubnetMask_Object = MibTableColumn
ippvcRuleSubnetMask = _IppvcRuleSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 8),
    _IppvcRuleSubnetMask_Type()
)
ippvcRuleSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ippvcRuleSubnetMask.setStatus("current")
_IppvcRuleDefaultRoute_Type = IpAddress
_IppvcRuleDefaultRoute_Object = MibTableColumn
ippvcRuleDefaultRoute = _IppvcRuleDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 9),
    _IppvcRuleDefaultRoute_Type()
)
ippvcRuleDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ippvcRuleDefaultRoute.setStatus("current")
_IppvcRuleRowStatus_Type = RowStatus
_IppvcRuleRowStatus_Object = MibTableColumn
ippvcRuleRowStatus = _IppvcRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 2, 1, 10),
    _IppvcRuleRowStatus_Type()
)
ippvcRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ippvcRuleRowStatus.setStatus("current")
_PaepvcRuleTable_Object = MibTable
paepvcRuleTable = _PaepvcRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3)
)
if mibBuilder.loadTexts:
    paepvcRuleTable.setStatus("current")
_PaepvcRuleEntry_Object = MibTableRow
paepvcRuleEntry = _PaepvcRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1)
)
paepvcRuleEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "paepvcRulePort"),
    (0, "ZYXEL-ves1608FE57-MIB", "paepvcRuleVpi"),
    (0, "ZYXEL-ves1608FE57-MIB", "paepvcRuleVci"),
)
if mibBuilder.loadTexts:
    paepvcRuleEntry.setStatus("current")
_PaepvcRulePort_Type = Integer32
_PaepvcRulePort_Object = MibTableColumn
paepvcRulePort = _PaepvcRulePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 1),
    _PaepvcRulePort_Type()
)
paepvcRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcRulePort.setStatus("current")
_PaepvcRuleVpi_Type = Integer32
_PaepvcRuleVpi_Object = MibTableColumn
paepvcRuleVpi = _PaepvcRuleVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 2),
    _PaepvcRuleVpi_Type()
)
paepvcRuleVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcRuleVpi.setStatus("current")
_PaepvcRuleVci_Type = Integer32
_PaepvcRuleVci_Object = MibTableColumn
paepvcRuleVci = _PaepvcRuleVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 3),
    _PaepvcRuleVci_Type()
)
paepvcRuleVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paepvcRuleVci.setStatus("current")
_PaepvcRulePvid_Type = Integer32
_PaepvcRulePvid_Object = MibTableColumn
paepvcRulePvid = _PaepvcRulePvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 4),
    _PaepvcRulePvid_Type()
)
paepvcRulePvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paepvcRulePvid.setStatus("current")


class _PaepvcRuleEncap_Type(Integer32):
    """Custom type paepvcRuleEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("llc", 0),
          ("vc", 1))
    )


_PaepvcRuleEncap_Type.__name__ = "Integer32"
_PaepvcRuleEncap_Object = MibTableColumn
paepvcRuleEncap = _PaepvcRuleEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 5),
    _PaepvcRuleEncap_Type()
)
paepvcRuleEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paepvcRuleEncap.setStatus("current")


class _PaepvcRulePriority_Type(Integer32):
    """Custom type paepvcRulePriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-1", 1),
          ("priority-2", 2),
          ("priority-3", 3),
          ("priority-4", 4),
          ("priority-5", 5),
          ("priority-6", 6),
          ("priority-7", 7))
    )


_PaepvcRulePriority_Type.__name__ = "Integer32"
_PaepvcRulePriority_Object = MibTableColumn
paepvcRulePriority = _PaepvcRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 6),
    _PaepvcRulePriority_Type()
)
paepvcRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paepvcRulePriority.setStatus("current")
_PaepvcRuleRowStatus_Type = RowStatus
_PaepvcRuleRowStatus_Object = MibTableColumn
paepvcRuleRowStatus = _PaepvcRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 120, 3, 1, 7),
    _PaepvcRuleRowStatus_Type()
)
paepvcRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    paepvcRuleRowStatus.setStatus("current")
_XdslBondingSetup_ObjectIdentity = ObjectIdentity
xdslBondingSetup = _XdslBondingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121)
)
_XdslBondingConfigTable_Object = MibTable
xdslBondingConfigTable = _XdslBondingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 1)
)
if mibBuilder.loadTexts:
    xdslBondingConfigTable.setStatus("current")
_XdslBondingConfigEntry_Object = MibTableRow
xdslBondingConfigEntry = _XdslBondingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 1, 1)
)
xdslBondingConfigEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "xdslBondingConfigName"),
)
if mibBuilder.loadTexts:
    xdslBondingConfigEntry.setStatus("current")
_XdslBondingConfigName_Type = DisplayString
_XdslBondingConfigName_Object = MibTableColumn
xdslBondingConfigName = _XdslBondingConfigName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 1, 1, 1),
    _XdslBondingConfigName_Type()
)
xdslBondingConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingConfigName.setStatus("current")
_XdslBondingConfigMemberPort_Type = PortList
_XdslBondingConfigMemberPort_Object = MibTableColumn
xdslBondingConfigMemberPort = _XdslBondingConfigMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 1, 1, 2),
    _XdslBondingConfigMemberPort_Type()
)
xdslBondingConfigMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslBondingConfigMemberPort.setStatus("current")
_XdslBondingConfigRowStatus_Type = RowStatus
_XdslBondingConfigRowStatus_Object = MibTableColumn
xdslBondingConfigRowStatus = _XdslBondingConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 1, 1, 3),
    _XdslBondingConfigRowStatus_Type()
)
xdslBondingConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdslBondingConfigRowStatus.setStatus("current")
_XdslBondingStatusTable_Object = MibTable
xdslBondingStatusTable = _XdslBondingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2)
)
if mibBuilder.loadTexts:
    xdslBondingStatusTable.setStatus("current")
_XdslBondingStatusEntry_Object = MibTableRow
xdslBondingStatusEntry = _XdslBondingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1)
)
xdslBondingStatusEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "xdslBondingConfigName"),
)
if mibBuilder.loadTexts:
    xdslBondingStatusEntry.setStatus("current")
_XdslBondingStatusActive_Type = Unsigned32
_XdslBondingStatusActive_Object = MibTableColumn
xdslBondingStatusActive = _XdslBondingStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 1),
    _XdslBondingStatusActive_Type()
)
xdslBondingStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusActive.setStatus("current")
_XdslBondingStatusMemberPort_Type = PortList
_XdslBondingStatusMemberPort_Object = MibTableColumn
xdslBondingStatusMemberPort = _XdslBondingStatusMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 2),
    _XdslBondingStatusMemberPort_Type()
)
xdslBondingStatusMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusMemberPort.setStatus("current")
_XdslBondingStatusActivePort_Type = PortList
_XdslBondingStatusActivePort_Object = MibTableColumn
xdslBondingStatusActivePort = _XdslBondingStatusActivePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 3),
    _XdslBondingStatusActivePort_Type()
)
xdslBondingStatusActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusActivePort.setStatus("current")
_XdslBondingStatusMainPort_Type = Unsigned32
_XdslBondingStatusMainPort_Object = MibTableColumn
xdslBondingStatusMainPort = _XdslBondingStatusMainPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 4),
    _XdslBondingStatusMainPort_Type()
)
xdslBondingStatusMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusMainPort.setStatus("current")
_XdslBondingStatusFlagType_Type = Unsigned32
_XdslBondingStatusFlagType_Object = MibTableColumn
xdslBondingStatusFlagType = _XdslBondingStatusFlagType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 5),
    _XdslBondingStatusFlagType_Type()
)
xdslBondingStatusFlagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusFlagType.setStatus("current")
_XdslBondingStatusRateUs_Type = Unsigned32
_XdslBondingStatusRateUs_Object = MibTableColumn
xdslBondingStatusRateUs = _XdslBondingStatusRateUs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 6),
    _XdslBondingStatusRateUs_Type()
)
xdslBondingStatusRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusRateUs.setStatus("current")
_XdslBondingStatusRateDs_Type = Unsigned32
_XdslBondingStatusRateDs_Object = MibTableColumn
xdslBondingStatusRateDs = _XdslBondingStatusRateDs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 121, 2, 1, 7),
    _XdslBondingStatusRateDs_Type()
)
xdslBondingStatusRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslBondingStatusRateDs.setStatus("current")
_MacFlush_ObjectIdentity = ObjectIdentity
macFlush = _MacFlush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 122)
)
_MacFlushTable_Object = MibTable
macFlushTable = _MacFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 122, 1)
)
if mibBuilder.loadTexts:
    macFlushTable.setStatus("current")
_MacFlushEntry_Object = MibTableRow
macFlushEntry = _MacFlushEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 122, 1, 1)
)
macFlushEntry.setIndexNames(
    (0, "ZYXEL-ves1608FE57-MIB", "macFlushPortIndex"),
)
if mibBuilder.loadTexts:
    macFlushEntry.setStatus("current")
_MacFlushPortIndex_Type = Integer32
_MacFlushPortIndex_Object = MibTableColumn
macFlushPortIndex = _MacFlushPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 122, 1, 1, 1),
    _MacFlushPortIndex_Type()
)
macFlushPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFlushPortIndex.setStatus("current")
_MacFlushPortConfig_Type = Integer32
_MacFlushPortConfig_Object = MibTableColumn
macFlushPortConfig = _MacFlushPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 122, 1, 1, 2),
    _MacFlushPortConfig_Type()
)
macFlushPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFlushPortConfig.setStatus("current")

# Managed Objects groups


# Notification objects

eventOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 2, 1)
)
eventOnTrap.setObjects(
      *(("ZYXEL-ves1608FE57-MIB", "eventSeqNum"),
        ("ZYXEL-ves1608FE57-MIB", "eventEventId"),
        ("ZYXEL-ves1608FE57-MIB", "eventName"),
        ("ZYXEL-ves1608FE57-MIB", "eventSetTime"),
        ("ZYXEL-ves1608FE57-MIB", "eventSeverity"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceType"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceId"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceName"),
        ("ZYXEL-ves1608FE57-MIB", "eventServAffective"),
        ("ZYXEL-ves1608FE57-MIB", "eventDescription"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceIdNumber"),
        ("ZYXEL-ves1608FE57-MIB", "trapPersistence"),
        ("ZYXEL-ves1608FE57-MIB", "trapSenderNodeId"),
        ("ZYXEL-ves1608FE57-MIB", "trapSenderStatus"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventOnTrap.setStatus(
        "current"
    )

eventClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 27, 2, 2)
)
eventClearedTrap.setObjects(
      *(("ZYXEL-ves1608FE57-MIB", "eventSeqNum"),
        ("ZYXEL-ves1608FE57-MIB", "eventEventId"),
        ("ZYXEL-ves1608FE57-MIB", "eventSetTime"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceType"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceId"),
        ("ZYXEL-ves1608FE57-MIB", "eventInstanceIdNumber"),
        ("ZYXEL-ves1608FE57-MIB", "trapRefSeqNum"),
        ("ZYXEL-ves1608FE57-MIB", "trapSenderNodeId"),
        ("ZYXEL-ves1608FE57-MIB", "trapSenderStatus"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventClearedTrap.setStatus(
        "current"
    )

newRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 2, 1)
)
newRoot.setObjects(
    ("ZYXEL-ves1608FE57-MIB", "mrstpBridgeIndex")
)
if mibBuilder.loadTexts:
    newRoot.setStatus(
        "current"
    )

topologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 48, 2, 2)
)
topologyChange.setObjects(
    ("ZYXEL-ves1608FE57-MIB", "mrstpBridgeIndex")
)
if mibBuilder.loadTexts:
    topologyChange.setStatus(
        "current"
    )

mstpNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 70, 1)
)
mstpNewRoot.setObjects(
    ("ZYXEL-ves1608FE57-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpNewRoot.setStatus(
        "current"
    )

mstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 56, 70, 2)
)
mstpTopologyChange.setObjects(
    ("ZYXEL-ves1608FE57-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpTopologyChange.setStatus(
        "current"
    )

xdsl2LinePerfLOFSThreshXtuc = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 0, 1)
)
xdsl2LinePerfLOFSThreshXtuc.setObjects(
      *(("ZYXEL-ves1608FE57-MIB", "xdsl2PMLCurr15MLofs"),
        ("ZYXEL-ves1608FE57-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfLOFSThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfLOFSThreshXtur = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 0, 2)
)
xdsl2LinePerfLOFSThreshXtur.setObjects(
      *(("ZYXEL-ves1608FE57-MIB", "xdsl2PMLCurr15MLofs"),
        ("ZYXEL-ves1608FE57-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfLOFSThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfLPRSThreshXtur = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 43, 60, 0, 3)
)
xdsl2LinePerfLPRSThreshXtur.setObjects(
      *(("ZYXEL-ves1608FE57-MIB", "xdsl2PMLCurr15MLprs"),
        ("ZYXEL-ves1608FE57-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfLPRSThreshXtur.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ves1608FE57-MIB",
    **{"Vdsl2Band": Vdsl2Band,
       "UtcTimeStamp": UtcTimeStamp,
       "EventIdNumber": EventIdNumber,
       "EventSeverity": EventSeverity,
       "EventServiceAffective": EventServiceAffective,
       "InstanceType": InstanceType,
       "EventPersistence": EventPersistence,
       "MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "vesSeries": vesSeries,
       "ves1608FE57": ves1608FE57,
       "sysInfo": sysInfo,
       "sysSwPlatformMajorVers": sysSwPlatformMajorVers,
       "sysSwPlatformMinorVers": sysSwPlatformMinorVers,
       "sysSwModelString": sysSwModelString,
       "sysSwVersionControlNbr": sysSwVersionControlNbr,
       "sysSwDay": sysSwDay,
       "sysSwMonth": sysSwMonth,
       "sysSwYear": sysSwYear,
       "sysHwMajorVers": sysHwMajorVers,
       "sysHwMinorVers": sysHwMinorVers,
       "sysSerialNumber": sysSerialNumber,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysModemCodeVersion": sysModemCodeVersion,
       "sysPowerInfo": sysPowerInfo,
       "sysSwBootUpImage": sysSwBootUpImage,
       "sysImage1FwVersion": sysImage1FwVersion,
       "sysImage2FwVersion": sysImage2FwVersion,
       "brLimitSetup": brLimitSetup,
       "brLimitState": brLimitState,
       "brLimitPortTable": brLimitPortTable,
       "brLimitPortEntry": brLimitPortEntry,
       "brLimitPortBrState": brLimitPortBrState,
       "brLimitPortBrRate": brLimitPortBrRate,
       "brLimitPortMcState": brLimitPortMcState,
       "brLimitPortMcRate": brLimitPortMcRate,
       "brLimitPortDlfState": brLimitPortDlfState,
       "brLimitPortDlfRate": brLimitPortDlfRate,
       "portSecuritySetup": portSecuritySetup,
       "portSecurityState": portSecurityState,
       "portSecurityPortTable": portSecurityPortTable,
       "portSecurityPortEntry": portSecurityPortEntry,
       "portSecurityPortState": portSecurityPortState,
       "portSecurityPortLearnState": portSecurityPortLearnState,
       "portSecurityPortCount": portSecurityPortCount,
       "portSecurityMacFreeze": portSecurityMacFreeze,
       "vlanTrunkSetup": vlanTrunkSetup,
       "vlanTrunkPortTable": vlanTrunkPortTable,
       "vlanTrunkPortEntry": vlanTrunkPortEntry,
       "vlanTrunkPortState": vlanTrunkPortState,
       "ctlProtTransSetup": ctlProtTransSetup,
       "ctlProtTransState": ctlProtTransState,
       "ctlProtTransTunnelPortTable": ctlProtTransTunnelPortTable,
       "ctlProtTransTunnelPortEntry": ctlProtTransTunnelPortEntry,
       "ctlProtTransTunnelMode": ctlProtTransTunnelMode,
       "vlanStackSetup": vlanStackSetup,
       "vlanStackState": vlanStackState,
       "vlanStackTpid": vlanStackTpid,
       "vlanStackPortTable": vlanStackPortTable,
       "vlanStackPortEntry": vlanStackPortEntry,
       "vlanStackPortMode": vlanStackPortMode,
       "vlanStackPortVid": vlanStackPortVid,
       "vlanStackPortPrio": vlanStackPortPrio,
       "vlanStackTunnelPortTpid": vlanStackTunnelPortTpid,
       "vlanStackPCopyCtagPrio": vlanStackPCopyCtagPrio,
       "selectiveQinQTable": selectiveQinQTable,
       "selectiveQinQEntry": selectiveQinQEntry,
       "selectiveQinQName": selectiveQinQName,
       "selectiveQinQPort": selectiveQinQPort,
       "selectiveQinQCvid": selectiveQinQCvid,
       "selectiveQinQSpvid": selectiveQinQSpvid,
       "selectiveQinQPriority": selectiveQinQPriority,
       "selectiveQinQRowStatus": selectiveQinQRowStatus,
       "selectiveQinQACtivePrio": selectiveQinQACtivePrio,
       "portBasedInnerQTable": portBasedInnerQTable,
       "portBasedInnerQEntry": portBasedInnerQEntry,
       "portBasedInnerQVid": portBasedInnerQVid,
       "portBasedInnerQPrio": portBasedInnerQPrio,
       "portBasedInnerQActive": portBasedInnerQActive,
       "portBasedInnerQTxUntag": portBasedInnerQTxUntag,
       "dot1xSetup": dot1xSetup,
       "portAuthState": portAuthState,
       "portAuthTable": portAuthTable,
       "portAuthEntry": portAuthEntry,
       "portAuthEntryState": portAuthEntryState,
       "portReAuthEntryState": portReAuthEntryState,
       "portReAuthEntryTimer": portReAuthEntryTimer,
       "hwMonitorInfo": hwMonitorInfo,
       "fanRpmTable": fanRpmTable,
       "fanRpmEntry": fanRpmEntry,
       "fanRpmIndex": fanRpmIndex,
       "fanRpmCurValue": fanRpmCurValue,
       "fanRpmMaxValue": fanRpmMaxValue,
       "fanRpmMinValue": fanRpmMinValue,
       "fanRpmLowThresh": fanRpmLowThresh,
       "fanRpmDescr": fanRpmDescr,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempCurValue": tempCurValue,
       "tempMaxValue": tempMaxValue,
       "tempMinValue": tempMinValue,
       "tempHighThresh": tempHighThresh,
       "tempDescr": tempDescr,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageCurValue": voltageCurValue,
       "voltageMaxValue": voltageMaxValue,
       "voltageMinValue": voltageMinValue,
       "voltageNominalValue": voltageNominalValue,
       "voltageLowThresh": voltageLowThresh,
       "voltageDescr": voltageDescr,
       "snmpSetup": snmpSetup,
       "snmpGetCommunity": snmpGetCommunity,
       "snmpSetCommunity": snmpSetCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestEntry": snmpTrapDestEntry,
       "snmpTrapDestIP": snmpTrapDestIP,
       "snmpTrapDestRowStatus": snmpTrapDestRowStatus,
       "snmpTrapDestPort": snmpTrapDestPort,
       "snmpTrapVersion": snmpTrapVersion,
       "snmpTrapUserName": snmpTrapUserName,
       "snmpTrapGroupTable": snmpTrapGroupTable,
       "snmpTrapGroupEntry": snmpTrapGroupEntry,
       "snmpTrapSystemGroup": snmpTrapSystemGroup,
       "snmpTrapInterfaceGroup": snmpTrapInterfaceGroup,
       "snmpTrapAAAGroup": snmpTrapAAAGroup,
       "snmpTrapSwitchGroup": snmpTrapSwitchGroup,
       "snmpTrapVdslGroup": snmpTrapVdslGroup,
       "snmpVersion": snmpVersion,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserName": snmpUserName,
       "snmpUserSecurityLevel": snmpUserSecurityLevel,
       "snmpUserAuthProtocol": snmpUserAuthProtocol,
       "snmpUserPrivProtocol": snmpUserPrivProtocol,
       "snmpTrapDestInfoTable": snmpTrapDestInfoTable,
       "snmpTrapDestInfoEntry": snmpTrapDestInfoEntry,
       "snmpTrapDestInfoIpAddrType": snmpTrapDestInfoIpAddrType,
       "snmpTrapDestInfoIpAddr": snmpTrapDestInfoIpAddr,
       "snmpTrapDestInfoRowStatus": snmpTrapDestInfoRowStatus,
       "snmpTrapDestInfoPort": snmpTrapDestInfoPort,
       "snmpTrapDestInfoVersion": snmpTrapDestInfoVersion,
       "snmpTrapDestInfoUserName": snmpTrapDestInfoUserName,
       "snmpTrapGroupInfoTable": snmpTrapGroupInfoTable,
       "snmpTrapGroupInfoEntry": snmpTrapGroupInfoEntry,
       "snmpTrapGroupInfoSystemGroup": snmpTrapGroupInfoSystemGroup,
       "snmpTrapGroupInfoInterfaceGroup": snmpTrapGroupInfoInterfaceGroup,
       "snmpTrapGroupInfoAAAGroup": snmpTrapGroupInfoAAAGroup,
       "snmpTrapGroupInfoSwitchGroup": snmpTrapGroupInfoSwitchGroup,
       "snmpTrapGroupInfoVdslGroup": snmpTrapGroupInfoVdslGroup,
       "dateTimeServerSetup": dateTimeServerSetup,
       "dateTimeServerType": dateTimeServerType,
       "dateTimeServerIP": dateTimeServerIP,
       "dateTimeZone": dateTimeZone,
       "dateTimeNewDateYear": dateTimeNewDateYear,
       "dateTimeNewDateMonth": dateTimeNewDateMonth,
       "dateTimeNewDateDay": dateTimeNewDateDay,
       "dateTimeNewTimeHour": dateTimeNewTimeHour,
       "dateTimeNewTimeMinute": dateTimeNewTimeMinute,
       "dateTimeNewTimeSecond": dateTimeNewTimeSecond,
       "dateTimeDaylightSavingTimeSetup": dateTimeDaylightSavingTimeSetup,
       "daylightSavingTimeState": daylightSavingTimeState,
       "daylightSavingTimeStartDateWeek": daylightSavingTimeStartDateWeek,
       "daylightSavingTimeStartDateDay": daylightSavingTimeStartDateDay,
       "daylightSavingTimeStartDateMonth": daylightSavingTimeStartDateMonth,
       "daylightSavingTimeStartDateHour": daylightSavingTimeStartDateHour,
       "daylightSavingTimeEndDateWeek": daylightSavingTimeEndDateWeek,
       "daylightSavingTimeEndDateDay": daylightSavingTimeEndDateDay,
       "daylightSavingTimeEndDateMonth": daylightSavingTimeEndDateMonth,
       "daylightSavingTimeEndDateHour": daylightSavingTimeEndDateHour,
       "dateTimeServerIPAddrType": dateTimeServerIPAddrType,
       "dateTimeServerIPAddr": dateTimeServerIPAddr,
       "sysMgmt": sysMgmt,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtBootupConfig": sysMgmtBootupConfig,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtDefaultConfig": sysMgmtDefaultConfig,
       "sysMgmtLastActionStatus": sysMgmtLastActionStatus,
       "sysMgmtSystemStatus": sysMgmtSystemStatus,
       "sysMgmtCPUUsage": sysMgmtCPUUsage,
       "sysMgmtBootupImage": sysMgmtBootupImage,
       "sysMgmtCounterReset": sysMgmtCounterReset,
       "sysMgmtTftpServiceSetup": sysMgmtTftpServiceSetup,
       "sysMgmtTftpServerIp": sysMgmtTftpServerIp,
       "sysMgmtTftpRemoteFileName": sysMgmtTftpRemoteFileName,
       "sysMgmtTftpConfigIndex": sysMgmtTftpConfigIndex,
       "sysMgmtTftpAction": sysMgmtTftpAction,
       "sysMgmtTftpActionStatus": sysMgmtTftpActionStatus,
       "sysMgmtTftpActionErrorInfo": sysMgmtTftpActionErrorInfo,
       "sysMgmtTftpServerAddressType": sysMgmtTftpServerAddressType,
       "sysMgmtTftpServerAddress": sysMgmtTftpServerAddress,
       "sysMgmtPacketBufferUsage": sysMgmtPacketBufferUsage,
       "sysMgmtMemoryUsage": sysMgmtMemoryUsage,
       "sysLoginSetup": sysLoginSetup,
       "loginLimitMaxNumberOfUser": loginLimitMaxNumberOfUser,
       "sysLoginSetupTable": sysLoginSetupTable,
       "sysLoginSetupEntry": sysLoginSetupEntry,
       "sysLoginName": sysLoginName,
       "sysLoginPassword": sysLoginPassword,
       "sysLoginPrivilege": sysLoginPrivilege,
       "sysLoginRowStatus": sysLoginRowStatus,
       "sysMgmtMacFlush": sysMgmtMacFlush,
       "sysMgmtCPUUsageThreshold": sysMgmtCPUUsageThreshold,
       "sysMgmtPacketBufferThreshold": sysMgmtPacketBufferThreshold,
       "sysMgmtMemoryUsageThreshold": sysMgmtMemoryUsageThreshold,
       "sysMgmtPlusVersion": sysMgmtPlusVersion,
       "layer2Setup": layer2Setup,
       "vlanTypeSetup": vlanTypeSetup,
       "igmpSnoopingStateSetup": igmpSnoopingStateSetup,
       "tagVlanPortIsolationState": tagVlanPortIsolationState,
       "stpState": stpState,
       "igmpFilteringStateSetup": igmpFilteringStateSetup,
       "unknownMulticastFrameForwarding": unknownMulticastFrameForwarding,
       "multicastGrpHostTimeout": multicastGrpHostTimeout,
       "multicastGrpLeaveTimeout": multicastGrpLeaveTimeout,
       "reservedMulticastFrameForwarding": reservedMulticastFrameForwarding,
       "igmpsnp8021pPriority": igmpsnp8021pPriority,
       "portBasedVlanPortIsolationState": portBasedVlanPortIsolationState,
       "igmpsnpVlanMode": igmpsnpVlanMode,
       "stpMode": stpMode,
       "igmpsnpVlanTable": igmpsnpVlanTable,
       "igmpsnpVlanEntry": igmpsnpVlanEntry,
       "igmpsnpVid": igmpsnpVid,
       "igmpsnpVlanName": igmpsnpVlanName,
       "igmpsnpVlanRowStatus": igmpsnpVlanRowStatus,
       "mgmdMLDsupport": mgmdMLDsupport,
       "ipSetup": ipSetup,
       "dnsIpAddress": dnsIpAddress,
       "defaultMgmt": defaultMgmt,
       "inbandIpSetup": inbandIpSetup,
       "inbandIpType": inbandIpType,
       "inbandVid": inbandVid,
       "inbandStaticIp": inbandStaticIp,
       "inbandStaticSubnetMask": inbandStaticSubnetMask,
       "inbandStaticGateway": inbandStaticGateway,
       "outOfBandIpSetup": outOfBandIpSetup,
       "outOfBandIp": outOfBandIp,
       "outOfBandSubnetMask": outOfBandSubnetMask,
       "outOfBandGateway": outOfBandGateway,
       "maxNumOfInbandIp": maxNumOfInbandIp,
       "inbandIpTable": inbandIpTable,
       "inbandIpEntry": inbandIpEntry,
       "inbandEntryIp": inbandEntryIp,
       "inbandEntrySubnetMask": inbandEntrySubnetMask,
       "inbandEntryGateway": inbandEntryGateway,
       "inbandEntryVid": inbandEntryVid,
       "inbandEntryManageable": inbandEntryManageable,
       "inbandEntryRowStatus": inbandEntryRowStatus,
       "filterSetup": filterSetup,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterName": filterName,
       "filterActionState": filterActionState,
       "filterMacAddr": filterMacAddr,
       "filterVid": filterVid,
       "filterRowStatus": filterRowStatus,
       "mirrorSetup": mirrorSetup,
       "mirrorState": mirrorState,
       "mirrorMonitorPort": mirrorMonitorPort,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorMirroredState": mirrorMirroredState,
       "mirrorDirection": mirrorDirection,
       "mirrorRspanVid": mirrorRspanVid,
       "aggrSetup": aggrSetup,
       "aggrState": aggrState,
       "aggrSystemPriority": aggrSystemPriority,
       "aggrGroupTable": aggrGroupTable,
       "aggrGroupEntry": aggrGroupEntry,
       "aggrGroupIndex": aggrGroupIndex,
       "aggrGroupState": aggrGroupState,
       "aggrGroupDynamicState": aggrGroupDynamicState,
       "aggrPortTable": aggrPortTable,
       "aggrPortEntry": aggrPortEntry,
       "aggrPortGroup": aggrPortGroup,
       "aggrPortDynamicStateTimeout": aggrPortDynamicStateTimeout,
       "accessCtlSetup": accessCtlSetup,
       "accessCtlTable": accessCtlTable,
       "accessCtlEntry": accessCtlEntry,
       "accessCtlService": accessCtlService,
       "accessCtlEnable": accessCtlEnable,
       "accessCtlServicePort": accessCtlServicePort,
       "accessCtlTimeout": accessCtlTimeout,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientEnable": securedClientEnable,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "securedClientIpAddrType": securedClientIpAddrType,
       "securedClientStartIpAddr": securedClientStartIpAddr,
       "securedClientEndIpAddr": securedClientEndIpAddr,
       "queuingMethodSetup": queuingMethodSetup,
       "queuingMethodType": queuingMethodType,
       "portQueuingMethodTable": portQueuingMethodTable,
       "portQueuingMethodEntry": portQueuingMethodEntry,
       "portQueuingMethodQueue": portQueuingMethodQueue,
       "portQueuingMethodWeight": portQueuingMethodWeight,
       "queuingMethodFeSpq": queuingMethodFeSpq,
       "portQueuingMethodGeSpqTable": portQueuingMethodGeSpqTable,
       "portQueuingMethodGeSpqEntry": portQueuingMethodGeSpqEntry,
       "portQueuingMethodGeSpq": portQueuingMethodGeSpq,
       "dhcpSetup": dhcpSetup,
       "globalDhcpRelay": globalDhcpRelay,
       "globalDhcpRelayEnable": globalDhcpRelayEnable,
       "globalDhcpRelayOption82Enable": globalDhcpRelayOption82Enable,
       "globalDhcpRelayInfoData": globalDhcpRelayInfoData,
       "maxNumberOfGlobalDhcpRelayRemoteServer": maxNumberOfGlobalDhcpRelayRemoteServer,
       "globalDhcpRelayRemoteServerTable": globalDhcpRelayRemoteServerTable,
       "globalDhcpRelayRemoteServerEntry": globalDhcpRelayRemoteServerEntry,
       "globalDhcpRelayRemoteServerIp": globalDhcpRelayRemoteServerIp,
       "globalDhcpRelayRemoteServerRowStatus": globalDhcpRelayRemoteServerRowStatus,
       "globalDhcpRelayRemoteIDEnable": globalDhcpRelayRemoteIDEnable,
       "globalDhcpRelayRemoteIDData": globalDhcpRelayRemoteIDData,
       "globalDhcpRelayInfoType": globalDhcpRelayInfoType,
       "globalDhcpRelayRemoteIDType": globalDhcpRelayRemoteIDType,
       "dhcpRelay": dhcpRelay,
       "maxNumberOfDhcpRelay": maxNumberOfDhcpRelay,
       "maxNumberOfDhcpRelayRemoteServer": maxNumberOfDhcpRelayRemoteServer,
       "dhcpRelayTable": dhcpRelayTable,
       "dhcpRelayEntry": dhcpRelayEntry,
       "dhcpRelayOption82Enable": dhcpRelayOption82Enable,
       "dhcpRelayInfoData": dhcpRelayInfoData,
       "dhcpRelayRemoteIDEnable": dhcpRelayRemoteIDEnable,
       "dhcpRelayRemoteIDData": dhcpRelayRemoteIDData,
       "dhcpRelayInfoType": dhcpRelayInfoType,
       "dhcpRelayRemoteIDType": dhcpRelayRemoteIDType,
       "dhcpRelayRemoteServerTable": dhcpRelayRemoteServerTable,
       "dhcpRelayRemoteServerEntry": dhcpRelayRemoteServerEntry,
       "dhcpRelayVid": dhcpRelayVid,
       "dhcpRelayRemoteServerIp": dhcpRelayRemoteServerIp,
       "dhcpRelayRemoteServerRowStatus": dhcpRelayRemoteServerRowStatus,
       "staticRouteSetup": staticRouteSetup,
       "maxNumberOfStaticRoutes": maxNumberOfStaticRoutes,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteName": staticRouteName,
       "staticRouteIp": staticRouteIp,
       "staticRouteMask": staticRouteMask,
       "staticRouteGateway": staticRouteGateway,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteRowStatus": staticRouteRowStatus,
       "arpInfo": arpInfo,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpIndex": arpIndex,
       "arpIpAddr": arpIpAddr,
       "arpMacAddr": arpMacAddr,
       "arpMacVid": arpMacVid,
       "arpType": arpType,
       "portOpModeSetup": portOpModeSetup,
       "portOpModePortTable": portOpModePortTable,
       "portOpModePortEntry": portOpModePortEntry,
       "portOpModePortSpeedDuplex": portOpModePortSpeedDuplex,
       "portOpModePortFlowCntl": portOpModePortFlowCntl,
       "portOpModePortName": portOpModePortName,
       "portOpModePortModuleType": portOpModePortModuleType,
       "portOpModePortLinkUpType": portOpModePortLinkUpType,
       "portOpModePortIntrusionLock": portOpModePortIntrusionLock,
       "portOpModePortLBTestSetup": portOpModePortLBTestSetup,
       "portOpModePortLBTestStatus": portOpModePortLBTestStatus,
       "portOpModePortSwCounterReset": portOpModePortSwCounterReset,
       "portOpModePortVdslCounterReset": portOpModePortVdslCounterReset,
       "portOpModePortVdslStatus": portOpModePortVdslStatus,
       "portOpModePortVdslUptime": portOpModePortVdslUptime,
       "portOpModePortLBTable": portOpModePortLBTable,
       "portOpModePortLBEntry": portOpModePortLBEntry,
       "portOpModePortLBActive": portOpModePortLBActive,
       "portOpModePortLBNumber": portOpModePortLBNumber,
       "portOpModePortLBCount": portOpModePortLBCount,
       "portOpModePortLBPktSize": portOpModePortLBPktSize,
       "portOpModePortLBResultTable": portOpModePortLBResultTable,
       "portOpModePortLBResultEntry": portOpModePortLBResultEntry,
       "portOpModePortLBMaxRTT": portOpModePortLBMaxRTT,
       "portOpModePortLBMinRTT": portOpModePortLBMinRTT,
       "portOpModePortLBAvgRTT": portOpModePortLBAvgRTT,
       "portOpModePortLBPktLossRate": portOpModePortLBPktLossRate,
       "portOpModePortLBStatus": portOpModePortLBStatus,
       "portBasedVlanSetup": portBasedVlanSetup,
       "portBasedVlanPortListTable": portBasedVlanPortListTable,
       "portBasedVlanPortListEntry": portBasedVlanPortListEntry,
       "portBasedVlanPortListMembers": portBasedVlanPortListMembers,
       "faultMIB": faultMIB,
       "eventObjects": eventObjects,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventSeqNum": eventSeqNum,
       "eventEventId": eventEventId,
       "eventName": eventName,
       "eventInstanceType": eventInstanceType,
       "eventInstanceId": eventInstanceId,
       "eventInstanceName": eventInstanceName,
       "eventSeverity": eventSeverity,
       "eventSetTime": eventSetTime,
       "eventDescription": eventDescription,
       "eventServAffective": eventServAffective,
       "eventInstanceIdNumber": eventInstanceIdNumber,
       "faultTrapsMIB": faultTrapsMIB,
       "trapInfoObjects": trapInfoObjects,
       "trapRefSeqNum": trapRefSeqNum,
       "trapPersistence": trapPersistence,
       "trapSenderNodeId": trapSenderNodeId,
       "trapSenderStatus": trapSenderStatus,
       "trapNotifications": trapNotifications,
       "eventOnTrap": eventOnTrap,
       "eventClearedTrap": eventClearedTrap,
       "multicastPortSetup": multicastPortSetup,
       "multicastPortTable": multicastPortTable,
       "multicastPortEntry": multicastPortEntry,
       "multicastPortImmediateLeave": multicastPortImmediateLeave,
       "multicastPortMaxGroupLimited": multicastPortMaxGroupLimited,
       "multicastPortMaxOfGroup": multicastPortMaxOfGroup,
       "multicastPortIgmpFilteringProfile": multicastPortIgmpFilteringProfile,
       "multicastPortQueryMode": multicastPortQueryMode,
       "igmpMsgMaxLimited": igmpMsgMaxLimited,
       "igmpMsgLimit": igmpMsgLimit,
       "multicastStatus": multicastStatus,
       "multicastStatusTable": multicastStatusTable,
       "multicastStatusEntry": multicastStatusEntry,
       "multicastStatusIndex": multicastStatusIndex,
       "multicastStatusVlanID": multicastStatusVlanID,
       "multicastStatusPort": multicastStatusPort,
       "multicastStatusGroup": multicastStatusGroup,
       "multicastStatusJoinCounter": multicastStatusJoinCounter,
       "multicastStatusLeaveCounter": multicastStatusLeaveCounter,
       "igmpCountTable": igmpCountTable,
       "igmpCountEntry": igmpCountEntry,
       "igmpCountIndex": igmpCountIndex,
       "igmpCountInQuery": igmpCountInQuery,
       "igmpCountInReport": igmpCountInReport,
       "igmpCountInLeave": igmpCountInLeave,
       "igmpCountInQueryDrop": igmpCountInQueryDrop,
       "igmpCountInReportDrop": igmpCountInReportDrop,
       "igmpCountInLeaveDrop": igmpCountInLeaveDrop,
       "igmpCountOutQuery": igmpCountOutQuery,
       "igmpCountOutReport": igmpCountOutReport,
       "igmpCountOutLeave": igmpCountOutLeave,
       "multicastVlanStatusTable": multicastVlanStatusTable,
       "multicastVlanStatusEntry": multicastVlanStatusEntry,
       "multicastVlanStatusVlanID": multicastVlanStatusVlanID,
       "multicastVlanStatusType": multicastVlanStatusType,
       "multicastVlanQueryPort": multicastVlanQueryPort,
       "multicastVlanQuerySrcIp": multicastVlanQuerySrcIp,
       "igmpCounterPortTable": igmpCounterPortTable,
       "igmpCounterPortEntry": igmpCounterPortEntry,
       "igmpCounterPortJoin": igmpCounterPortJoin,
       "igmpCounterPortLeave": igmpCounterPortLeave,
       "igmpCounterPortActiveGroup": igmpCounterPortActiveGroup,
       "igmpCounterPortQuery": igmpCounterPortQuery,
       "igmpCounterVlanTable": igmpCounterVlanTable,
       "igmpCounterVlanEntry": igmpCounterVlanEntry,
       "igmpCounterVlanJoin": igmpCounterVlanJoin,
       "igmpCounterVlanLeave": igmpCounterVlanLeave,
       "igmpCounterVlanActiveGroup": igmpCounterVlanActiveGroup,
       "igmpCounterVlanQuery": igmpCounterVlanQuery,
       "multicastCurrentGroupStatusTable": multicastCurrentGroupStatusTable,
       "multicastCurrentGroupStatusEntry": multicastCurrentGroupStatusEntry,
       "multicastCurrentNumberOfActivePort": multicastCurrentNumberOfActivePort,
       "multicastClientSrcIpTable": multicastClientSrcIpTable,
       "multicastClientSrcIpEntry": multicastClientSrcIpEntry,
       "multicastClientSrcIpIndex": multicastClientSrcIpIndex,
       "multicastClientSrcIpAddress": multicastClientSrcIpAddress,
       "mgmdStatusTable": mgmdStatusTable,
       "mgmdStatusEntry": mgmdStatusEntry,
       "mgmdStatusIndex": mgmdStatusIndex,
       "mgmdStatusVlanID": mgmdStatusVlanID,
       "mgmdStatusPort": mgmdStatusPort,
       "mgmdStatusGroupAddressType": mgmdStatusGroupAddressType,
       "mgmdStatusGroupAddress": mgmdStatusGroupAddress,
       "mgmdStatusGroupFilterMode": mgmdStatusGroupFilterMode,
       "mgmdCountTable": mgmdCountTable,
       "mgmdCountEntry": mgmdCountEntry,
       "mgmdCountIndex": mgmdCountIndex,
       "mgmdCountInQuery": mgmdCountInQuery,
       "mgmdCountInReport": mgmdCountInReport,
       "mgmdCountInLeave": mgmdCountInLeave,
       "mgmdCountInQueryDrop": mgmdCountInQueryDrop,
       "mgmdCountInReportDrop": mgmdCountInReportDrop,
       "mgmdCountInLeaveDrop": mgmdCountInLeaveDrop,
       "mgmdCountOutQuery": mgmdCountOutQuery,
       "mgmdCountOutReport": mgmdCountOutReport,
       "mgmdCountOutLeave": mgmdCountOutLeave,
       "mgmdVlanStatusTable": mgmdVlanStatusTable,
       "mgmdVlanStatusEntry": mgmdVlanStatusEntry,
       "mgmdVlanStatusVlanID": mgmdVlanStatusVlanID,
       "mgmdVlanStatusType": mgmdVlanStatusType,
       "mgmdVlanQueryPort": mgmdVlanQueryPort,
       "mgmdVlanQuerySrcIpType": mgmdVlanQuerySrcIpType,
       "mgmdVlanQuerySrcIp": mgmdVlanQuerySrcIp,
       "mgmdCounterPortTable": mgmdCounterPortTable,
       "mgmdCounterPortEntry": mgmdCounterPortEntry,
       "mgmdCounterPortReport": mgmdCounterPortReport,
       "mgmdCounterPortLeave": mgmdCounterPortLeave,
       "mgmdCounterPortActiveGroup": mgmdCounterPortActiveGroup,
       "mgmdCounterPortQuery": mgmdCounterPortQuery,
       "mgmdCounterVlanTable": mgmdCounterVlanTable,
       "mgmdCounterVlanEntry": mgmdCounterVlanEntry,
       "mgmdCounterVlanReport": mgmdCounterVlanReport,
       "mgmdCounterVlanLeave": mgmdCounterVlanLeave,
       "mgmdCounterVlanActiveGroup": mgmdCounterVlanActiveGroup,
       "mgmdCounterVlanQuery": mgmdCounterVlanQuery,
       "mgmdCurrentGroupStatusTable": mgmdCurrentGroupStatusTable,
       "mgmdCurrentGroupStatusEntry": mgmdCurrentGroupStatusEntry,
       "mgmdCurrentNumberOfActivePort": mgmdCurrentNumberOfActivePort,
       "mgmdClientSrcIpTable": mgmdClientSrcIpTable,
       "mgmdClientSrcIpEntry": mgmdClientSrcIpEntry,
       "mgmdClientSrcIpIndex": mgmdClientSrcIpIndex,
       "mgmdClientSrcIpAddressType": mgmdClientSrcIpAddressType,
       "mgmdClientSrcIpAddress": mgmdClientSrcIpAddress,
       "mgmdSrcListTable": mgmdSrcListTable,
       "mgmdSrcListEntry": mgmdSrcListEntry,
       "mgmdSrcListAddressType": mgmdSrcListAddressType,
       "mgmdSrcListAddress": mgmdSrcListAddress,
       "igmpFilteringProfileSetup": igmpFilteringProfileSetup,
       "igmpFilteringMaxNumberOfProfile": igmpFilteringMaxNumberOfProfile,
       "igmpFilteringProfileTable": igmpFilteringProfileTable,
       "igmpFilteringProfileEntry": igmpFilteringProfileEntry,
       "igmpFilteringProfileName": igmpFilteringProfileName,
       "igmpFilteringProfileStartAddress": igmpFilteringProfileStartAddress,
       "igmpFilteringProfileEndAddress": igmpFilteringProfileEndAddress,
       "igmpFilteringProfileRowStatus": igmpFilteringProfileRowStatus,
       "mgmdFilterProfileTable": mgmdFilterProfileTable,
       "mgmdFilterProfileEntry": mgmdFilterProfileEntry,
       "mgmdFilterProfileName": mgmdFilterProfileName,
       "mgmdFilterProfileAddressType": mgmdFilterProfileAddressType,
       "mgmdFilterProfileStartAddress": mgmdFilterProfileStartAddress,
       "mgmdFilterProfileEndAddress": mgmdFilterProfileEndAddress,
       "mgmdFilterProfileRowStatus": mgmdFilterProfileRowStatus,
       "mvrSetup": mvrSetup,
       "maxNumberOfMVR": maxNumberOfMVR,
       "mvrTable": mvrTable,
       "mvrEntry": mvrEntry,
       "mvrVlanID": mvrVlanID,
       "mvrName": mvrName,
       "mvrMode": mvrMode,
       "mvrRowStatus": mvrRowStatus,
       "mvr8021pPriority": mvr8021pPriority,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrPortRole": mvrPortRole,
       "mvrPortTagging": mvrPortTagging,
       "maxNumberOfMvrGroup": maxNumberOfMvrGroup,
       "mvrGroupTable": mvrGroupTable,
       "mvrGroupEntry": mvrGroupEntry,
       "mvrGroupName": mvrGroupName,
       "mvrGroupStartAddress": mvrGroupStartAddress,
       "mvrGroupEndAddress": mvrGroupEndAddress,
       "mvrGroupRowStatus": mvrGroupRowStatus,
       "mvrBehavior": mvrBehavior,
       "mvrMgmdGroupTable": mvrMgmdGroupTable,
       "mvrMgmdGroupEntry": mvrMgmdGroupEntry,
       "mvrMgmdGroupName": mvrMgmdGroupName,
       "mvrMgmdGroupAddressType": mvrMgmdGroupAddressType,
       "mvrMgmdGroupStartAddress": mvrMgmdGroupStartAddress,
       "mvrMgmdGroupEndAddress": mvrMgmdGroupEndAddress,
       "mvrMgmdGroupRowStatus": mvrMgmdGroupRowStatus,
       "sysLogSetup": sysLogSetup,
       "sysLogState": sysLogState,
       "sysLogTypeTable": sysLogTypeTable,
       "sysLogTypeEntry": sysLogTypeEntry,
       "sysLogTypeIndex": sysLogTypeIndex,
       "sysLogTypeName": sysLogTypeName,
       "sysLogTypeState": sysLogTypeState,
       "sysLogTypeFacility": sysLogTypeFacility,
       "sysLogServerTable": sysLogServerTable,
       "sysLogServerEntry": sysLogServerEntry,
       "sysLogServerAddress": sysLogServerAddress,
       "sysLogServerLogLevel": sysLogServerLogLevel,
       "sysLogServerRowStatus": sysLogServerRowStatus,
       "sysLogServerInfoTable": sysLogServerInfoTable,
       "sysLogServerInfoEntry": sysLogServerInfoEntry,
       "sysLogServerInfoIpAddrType": sysLogServerInfoIpAddrType,
       "sysLogServerInfoIpAddr": sysLogServerInfoIpAddr,
       "sysLogServerInfoLogLevel": sysLogServerInfoLogLevel,
       "sysLogServerInfoRowStatus": sysLogServerInfoRowStatus,
       "diffservSetup": diffservSetup,
       "diffservState": diffservState,
       "diffservMapTable": diffservMapTable,
       "diffservMapEntry": diffservMapEntry,
       "diffservMapDscp": diffservMapDscp,
       "diffservMapPriority": diffservMapPriority,
       "diffservPortTable": diffservPortTable,
       "diffservPortEntry": diffservPortEntry,
       "diffservPortState": diffservPortState,
       "vturInfo": vturInfo,
       "vturInfoTable": vturInfoTable,
       "vturInfoEntry": vturInfoEntry,
       "vturName": vturName,
       "vturSysVersion": vturSysVersion,
       "vturModemCodeVersion": vturModemCodeVersion,
       "protoBasedVlanSetup": protoBasedVlanSetup,
       "protoBasedVlanTable": protoBasedVlanTable,
       "protoBasedVlanEntry": protoBasedVlanEntry,
       "protoBasedVlanPort": protoBasedVlanPort,
       "protoBasedVlanPacketType": protoBasedVlanPacketType,
       "protoBasedVlanEtherType": protoBasedVlanEtherType,
       "protoBasedVlanName": protoBasedVlanName,
       "protoBasedVlanVid": protoBasedVlanVid,
       "protoBasedVlanPriority": protoBasedVlanPriority,
       "protoBasedVlanState": protoBasedVlanState,
       "classifierSetup": classifierSetup,
       "classifierRuleTable": classifierRuleTable,
       "classifierRuleEntry": classifierRuleEntry,
       "classifierName": classifierName,
       "classifierEnable": classifierEnable,
       "classifierPacketFormat": classifierPacketFormat,
       "classifierVlanId": classifierVlanId,
       "classifier8021pPriority": classifier8021pPriority,
       "classifierEtherType": classifierEtherType,
       "classifierSrcMAC": classifierSrcMAC,
       "classifierIncomingPort": classifierIncomingPort,
       "classifierDstMAC": classifierDstMAC,
       "classifierDSCP": classifierDSCP,
       "classifierIpProtocol": classifierIpProtocol,
       "classifierEstablishOnly": classifierEstablishOnly,
       "classifierSrcIp": classifierSrcIp,
       "classifierSrcIpMask": classifierSrcIpMask,
       "classifierSrcSocket": classifierSrcSocket,
       "classifierDstIp": classifierDstIp,
       "classifierDstIpMask": classifierDstIpMask,
       "classifierDstSocket": classifierDstSocket,
       "classifierRowstatus": classifierRowstatus,
       "classifierSrcIpv6": classifierSrcIpv6,
       "classifierSrcIpv6Mask": classifierSrcIpv6Mask,
       "classifierDstIpv6": classifierDstIpv6,
       "classifierDstIpv6Mask": classifierDstIpv6Mask,
       "classifierRuleSet": classifierRuleSet,
       "policySetup": policySetup,
       "policyTable": policyTable,
       "policyEntry": policyEntry,
       "policyName": policyName,
       "policyEnable": policyEnable,
       "policyClassifier": policyClassifier,
       "policyVlanId": policyVlanId,
       "policyEgressPort": policyEgressPort,
       "policyOutPktFormat": policyOutPktFormat,
       "policy8021pPriority": policy8021pPriority,
       "policyDSCP": policyDSCP,
       "policyTOS": policyTOS,
       "policyBandwidth": policyBandwidth,
       "policyOutOfProfileDSCP": policyOutOfProfileDSCP,
       "policyForwardingAction": policyForwardingAction,
       "policyPriorityAction": policyPriorityAction,
       "policyDiffServAction": policyDiffServAction,
       "policyOutgoingAction": policyOutgoingAction,
       "policyMeteringEnable": policyMeteringEnable,
       "policyOutOfProfileAction": policyOutOfProfileAction,
       "policyRowstatus": policyRowstatus,
       "policyRuleSet": policyRuleSet,
       "switchCounterStatus": switchCounterStatus,
       "vlanCounterTable": vlanCounterTable,
       "vlanCounterEntry": vlanCounterEntry,
       "vlanCounterTxPkts": vlanCounterTxPkts,
       "vlanCounterRxPkts": vlanCounterRxPkts,
       "switchCounterTable": switchCounterTable,
       "switchCounterEntry": switchCounterEntry,
       "switchUnknownUnicastCounter": switchUnknownUnicastCounter,
       "vlanCounterResetTable": vlanCounterResetTable,
       "vlanCounterResetEntry": vlanCounterResetEntry,
       "vlanCounterReset": vlanCounterReset,
       "vlanCounterSwitchSetup": vlanCounterSwitchSetup,
       "vlanCounterSwitch": vlanCounterSwitch,
       "vlanCounterVlan": vlanCounterVlan,
       "vlanCounterPort": vlanCounterPort,
       "vlanCounterDirection": vlanCounterDirection,
       "rateLimitProfilePortSetup": rateLimitProfilePortSetup,
       "rateLimitProfilePortTable": rateLimitProfilePortTable,
       "rateLimitProfilePortEntry": rateLimitProfilePortEntry,
       "rateLimitPortProfile": rateLimitPortProfile,
       "perQueueProfilePortTable": perQueueProfilePortTable,
       "perQueueProfilePortEntry": perQueueProfilePortEntry,
       "perQueuePortProfile": perQueuePortProfile,
       "rateLimitProfileSetup": rateLimitProfileSetup,
       "rateLimitMaxNumberOfProfile": rateLimitMaxNumberOfProfile,
       "rateLimitProfileTable": rateLimitProfileTable,
       "rateLimitProfileEntry": rateLimitProfileEntry,
       "rateLimitProfileName": rateLimitProfileName,
       "rateLimitProfilePeakRate": rateLimitProfilePeakRate,
       "rateLimitProfileEgrRate": rateLimitProfileEgrRate,
       "rateLimitProfileCommitRate": rateLimitProfileCommitRate,
       "rateLimitProfilePeakState": rateLimitProfilePeakState,
       "rateLimitProfileEgrState": rateLimitProfileEgrState,
       "rateLimitProfileCommitState": rateLimitProfileCommitState,
       "rateLimitProfileRowStatus": rateLimitProfileRowStatus,
       "perQueueMaxNumberOfProfile": perQueueMaxNumberOfProfile,
       "perQueueProfileTable": perQueueProfileTable,
       "perQueueProfileEntry": perQueueProfileEntry,
       "perQueueProfileName": perQueueProfileName,
       "perQueueProfileQ0CIR": perQueueProfileQ0CIR,
       "perQueueProfileQ0PIR": perQueueProfileQ0PIR,
       "perQueueProfileQ1CIR": perQueueProfileQ1CIR,
       "perQueueProfileQ1PIR": perQueueProfileQ1PIR,
       "perQueueProfileQ2CIR": perQueueProfileQ2CIR,
       "perQueueProfileQ2PIR": perQueueProfileQ2PIR,
       "perQueueProfileQ3CIR": perQueueProfileQ3CIR,
       "perQueueProfileQ3PIR": perQueueProfileQ3PIR,
       "perQueueProfileQ4CIR": perQueueProfileQ4CIR,
       "perQueueProfileQ4PIR": perQueueProfileQ4PIR,
       "perQueueProfileQ5CIR": perQueueProfileQ5CIR,
       "perQueueProfileQ5PIR": perQueueProfileQ5PIR,
       "perQueueProfileQ6CIR": perQueueProfileQ6CIR,
       "perQueueProfileQ6PIR": perQueueProfileQ6PIR,
       "perQueueProfileQ7CIR": perQueueProfileQ7CIR,
       "perQueueProfileQ7PIR": perQueueProfileQ7PIR,
       "perQueueProfileRowStatus": perQueueProfileRowStatus,
       "vlanSecuritySetup": vlanSecuritySetup,
       "vlanSecurityTable": vlanSecurityTable,
       "vlanSecurityEntry": vlanSecurityEntry,
       "vlanSecurityCount": vlanSecurityCount,
       "cfmSetup": cfmSetup,
       "cfmLoopbackPortTable": cfmLoopbackPortTable,
       "cfmLoopbackPortEntry": cfmLoopbackPortEntry,
       "cfmLoopbackPortState": cfmLoopbackPortState,
       "cfmMIPTable": cfmMIPTable,
       "cfmMIPEntry": cfmMIPEntry,
       "cfmPort": cfmPort,
       "cfmVlanID": cfmVlanID,
       "cfmLevel": cfmLevel,
       "cfmMIPRowStatus": cfmMIPRowStatus,
       "cfmActionEnableStatus": cfmActionEnableStatus,
       "mrstp": mrstp,
       "mrstpSetup": mrstpSetup,
       "mrstpBridgeTable": mrstpBridgeTable,
       "mrstpBridgeEntry": mrstpBridgeEntry,
       "mrstpBridgeIndex": mrstpBridgeIndex,
       "mrstpState": mrstpState,
       "mrstpProtocolSpecification": mrstpProtocolSpecification,
       "mrstpPriority": mrstpPriority,
       "mrstpTimeSinceTopologyChange": mrstpTimeSinceTopologyChange,
       "mrstpTopChanges": mrstpTopChanges,
       "mrstpDesignatedRoot": mrstpDesignatedRoot,
       "mrstpRootCost": mrstpRootCost,
       "mrstpRootPort": mrstpRootPort,
       "mrstpMaxAge": mrstpMaxAge,
       "mrstpHelloTime": mrstpHelloTime,
       "mrstpHoldTime": mrstpHoldTime,
       "mrstpForwardDelay": mrstpForwardDelay,
       "mrstpBridgeMaxAge": mrstpBridgeMaxAge,
       "mrstpBridgeHelloTime": mrstpBridgeHelloTime,
       "mrstpBridgeForwardDelay": mrstpBridgeForwardDelay,
       "mrstpPortTable": mrstpPortTable,
       "mrstpPortEntry": mrstpPortEntry,
       "mrstpPort": mrstpPort,
       "mrstpPortPriority": mrstpPortPriority,
       "mrstpPortState": mrstpPortState,
       "mrstpPortEnable": mrstpPortEnable,
       "mrstpPortPathCost": mrstpPortPathCost,
       "mrstpPortDesignatedRoot": mrstpPortDesignatedRoot,
       "mrstpPortDesignatedCost": mrstpPortDesignatedCost,
       "mrstpPortDesignatedBridge": mrstpPortDesignatedBridge,
       "mrstpPortDesignatedPort": mrstpPortDesignatedPort,
       "mrstpPortForwardTransitions": mrstpPortForwardTransitions,
       "mrstpPortOnBridgeIndex": mrstpPortOnBridgeIndex,
       "mrstpNotifications": mrstpNotifications,
       "newRoot": newRoot,
       "topologyChange": topologyChange,
       "dhcpSnp": dhcpSnp,
       "dhcpSnpVlanTable": dhcpSnpVlanTable,
       "dhcpSnpVlanEntry": dhcpSnpVlanEntry,
       "dhcpSnpVlanEntryVid": dhcpSnpVlanEntryVid,
       "dhcpSnpVlanEntryEnable": dhcpSnpVlanEntryEnable,
       "dhcpSnpVlanEntryOption82Enable": dhcpSnpVlanEntryOption82Enable,
       "dhcpSnpVlanEntryInfo": dhcpSnpVlanEntryInfo,
       "dhcpSnpVlanEntryRemoteID": dhcpSnpVlanEntryRemoteID,
       "dhcpSnpPortTable": dhcpSnpPortTable,
       "dhcpSnpPortEntry": dhcpSnpPortEntry,
       "dhcpSnpPortEntryPort": dhcpSnpPortEntryPort,
       "dhcpSnpPortEntryTrust": dhcpSnpPortEntryTrust,
       "dhcpSnpPortEntryRate": dhcpSnpPortEntryRate,
       "dhcpSnpBindTable": dhcpSnpBindTable,
       "dhcpSnpBindEntry": dhcpSnpBindEntry,
       "dhcpSnpBindEntryMac": dhcpSnpBindEntryMac,
       "dhcpSnpBindEntryVid": dhcpSnpBindEntryVid,
       "dhcpSnpBindEntryIP": dhcpSnpBindEntryIP,
       "dhcpSnpBindEntryLease": dhcpSnpBindEntryLease,
       "dhcpSnpBindEntryType": dhcpSnpBindEntryType,
       "dhcpSnpBindEntryPort": dhcpSnpBindEntryPort,
       "dhcpSnpEnable": dhcpSnpEnable,
       "dhcpSnpDb": dhcpSnpDb,
       "dhcpSnpDbAbort": dhcpSnpDbAbort,
       "dhcpSnpDbWriteDelay": dhcpSnpDbWriteDelay,
       "dhcpSnpDbUrl": dhcpSnpDbUrl,
       "dhcpSnpDbUrlRenew": dhcpSnpDbUrlRenew,
       "dhcpSnpDbStat": dhcpSnpDbStat,
       "dhcpSnpDbStatClear": dhcpSnpDbStatClear,
       "dhcpSnpDbStatAgentRunning": dhcpSnpDbStatAgentRunning,
       "dhcpSnpDbStatDelayExpiry": dhcpSnpDbStatDelayExpiry,
       "dhcpSnpDbStatAbortExpiry": dhcpSnpDbStatAbortExpiry,
       "dhcpSnpDbStatLastSuccTime": dhcpSnpDbStatLastSuccTime,
       "dhcpSnpDbStatLastFailTime": dhcpSnpDbStatLastFailTime,
       "dhcpSnpDbStatLastFailReason": dhcpSnpDbStatLastFailReason,
       "dhcpSnpDbStatTotalAttempt": dhcpSnpDbStatTotalAttempt,
       "dhcpSnpDbStatStartupFail": dhcpSnpDbStatStartupFail,
       "dhcpSnpDbStatSuccTrans": dhcpSnpDbStatSuccTrans,
       "dhcpSnpDbStatFailTrans": dhcpSnpDbStatFailTrans,
       "dhcpSnpDbStatSuccRead": dhcpSnpDbStatSuccRead,
       "dhcpSnpDbStatFailRead": dhcpSnpDbStatFailRead,
       "dhcpSnpDbStatSuccWrite": dhcpSnpDbStatSuccWrite,
       "dhcpSnpDbStatFailWrite": dhcpSnpDbStatFailWrite,
       "dhcpSnpDbStatFirstSuccAccess": dhcpSnpDbStatFirstSuccAccess,
       "dhcpSnpDbStatLastIgnoreBindCol": dhcpSnpDbStatLastIgnoreBindCol,
       "dhcpSnpDbStatLastIgnoreExpireLease": dhcpSnpDbStatLastIgnoreExpireLease,
       "dhcpSnpDbStatLastIgnoreInvalidIntf": dhcpSnpDbStatLastIgnoreInvalidIntf,
       "dhcpSnpDbStatLastIgnoreUnsuppVlan": dhcpSnpDbStatLastIgnoreUnsuppVlan,
       "dhcpSnpDbStatLastIgnoreParse": dhcpSnpDbStatLastIgnoreParse,
       "dhcpSnpDbStatTotalIgnoreBindCol": dhcpSnpDbStatTotalIgnoreBindCol,
       "dhcpSnpDbStatTotalIgnoreExpireLease": dhcpSnpDbStatTotalIgnoreExpireLease,
       "dhcpSnpDbStatTotalIgnoreInvalidIntf": dhcpSnpDbStatTotalIgnoreInvalidIntf,
       "dhcpSnpDbStatTotalIgnoreUnsuppVlan": dhcpSnpDbStatTotalIgnoreUnsuppVlan,
       "dhcpSnpDbStatTotalIgnoreParse": dhcpSnpDbStatTotalIgnoreParse,
       "dhcpSnpDbStatFirstSuccessAccess": dhcpSnpDbStatFirstSuccessAccess,
       "dhcpSnpDhcpVlan": dhcpSnpDhcpVlan,
       "dhcpSnpDhcpVlanVid": dhcpSnpDhcpVlanVid,
       "ipsg": ipsg,
       "ipsgTable": ipsgTable,
       "ipsgEntry": ipsgEntry,
       "ipsgEntryMac": ipsgEntryMac,
       "ipsgEntryVid": ipsgEntryVid,
       "ipsgEntryIp": ipsgEntryIp,
       "ipsgEntryLease": ipsgEntryLease,
       "ipsgEntryType": ipsgEntryType,
       "ipsgEntryPort": ipsgEntryPort,
       "ipsgEntryState": ipsgEntryState,
       "arpInspect": arpInspect,
       "arpInspectSetup": arpInspectSetup,
       "arpInspectState": arpInspectState,
       "arpInspectFilterAgingTime": arpInspectFilterAgingTime,
       "arpInspectLog": arpInspectLog,
       "arpInspectLogEntries": arpInspectLogEntries,
       "arpInspectLogRate": arpInspectLogRate,
       "arpInspectLogInterval": arpInspectLogInterval,
       "arpInspectVlanTable": arpInspectVlanTable,
       "arpInspectVlanEntry": arpInspectVlanEntry,
       "arpInspectVlanVid": arpInspectVlanVid,
       "arpInspectVlanLog": arpInspectVlanLog,
       "arpInspectVlanStatus": arpInspectVlanStatus,
       "arpInspectPortTable": arpInspectPortTable,
       "arpInspectPortEntry": arpInspectPortEntry,
       "arpInspectPortIndex": arpInspectPortIndex,
       "arpInspectPortTrust": arpInspectPortTrust,
       "arpInspectPortRate": arpInspectPortRate,
       "arpInspectPortInterval": arpInspectPortInterval,
       "arpInspectStatus": arpInspectStatus,
       "arpInspectFilterClear": arpInspectFilterClear,
       "arpInspectLogClear": arpInspectLogClear,
       "arpInspectFilterTable": arpInspectFilterTable,
       "arpInspectFilterEntry": arpInspectFilterEntry,
       "arpInspectFilterMac": arpInspectFilterMac,
       "arpInspectFilterVid": arpInspectFilterVid,
       "arpInspectFilterPort": arpInspectFilterPort,
       "arpInspectFilterExpiry": arpInspectFilterExpiry,
       "arpInspectFilterReason": arpInspectFilterReason,
       "arpInspectFilterRowStatus": arpInspectFilterRowStatus,
       "arpInspectLogTable": arpInspectLogTable,
       "arpInspectLogEntry": arpInspectLogEntry,
       "arpInspectLogMac": arpInspectLogMac,
       "arpInspectLogVid": arpInspectLogVid,
       "arpInspectLogPort": arpInspectLogPort,
       "arpInspectLogIp": arpInspectLogIp,
       "arpInspectLogNumPkt": arpInspectLogNumPkt,
       "arpInspectLogReason": arpInspectLogReason,
       "arpInspectLogTime": arpInspectLogTime,
       "arpInspectStatisticsTable": arpInspectStatisticsTable,
       "arpInspectStatisticsEntry": arpInspectStatisticsEntry,
       "arpInspectStatisticsVid": arpInspectStatisticsVid,
       "arpInspectStatisticsReceived": arpInspectStatisticsReceived,
       "arpInspectStatisticsRequest": arpInspectStatisticsRequest,
       "arpInspectStatisticsReply": arpInspectStatisticsReply,
       "arpInspectStatisticsForward": arpInspectStatisticsForward,
       "arpInspectStatisticsDrop": arpInspectStatisticsDrop,
       "arpInspectStatisticsClear": arpInspectStatisticsClear,
       "trTCMSetup": trTCMSetup,
       "trTCMState": trTCMState,
       "trTCMMode": trTCMMode,
       "trTCMPortTable": trTCMPortTable,
       "trTCMPortEntry": trTCMPortEntry,
       "trTCMPortState": trTCMPortState,
       "trTCMPortCIR": trTCMPortCIR,
       "trTCMPortPIR": trTCMPortPIR,
       "trTCMPortDscpGreen": trTCMPortDscpGreen,
       "trTCMPortDscpYellow": trTCMPortDscpYellow,
       "trTCMPortDscpRed": trTCMPortDscpRed,
       "loopGuardSetup": loopGuardSetup,
       "loopGuardState": loopGuardState,
       "loopGuardPortTable": loopGuardPortTable,
       "loopGuardPortEntry": loopGuardPortEntry,
       "loopGuardPortState": loopGuardPortState,
       "loopGuardPortMode": loopGuardPortMode,
       "loopGuardPortRecoverTime": loopGuardPortRecoverTime,
       "subnetBasedVlanSetup": subnetBasedVlanSetup,
       "subnetBasedVlanState": subnetBasedVlanState,
       "dhcpVlanOverrideState": dhcpVlanOverrideState,
       "subnetBasedVlanTable": subnetBasedVlanTable,
       "subnetBasedVlanEntry": subnetBasedVlanEntry,
       "subnetBasedVlanSrcIp": subnetBasedVlanSrcIp,
       "subnetBasedVlanSrcMaskBit": subnetBasedVlanSrcMaskBit,
       "subnetBasedVlanName": subnetBasedVlanName,
       "subnetBasedVlanVid": subnetBasedVlanVid,
       "subnetBasedVlanPriority": subnetBasedVlanPriority,
       "subnetBasedVlanEntryState": subnetBasedVlanEntryState,
       "subnetBasedVlanInfoTable": subnetBasedVlanInfoTable,
       "subnetBasedVlanInfoEntry": subnetBasedVlanInfoEntry,
       "subnetBasedVlanInfoSrcIpType": subnetBasedVlanInfoSrcIpType,
       "subnetBasedVlanInfoSrcIp": subnetBasedVlanInfoSrcIp,
       "subnetBasedVlanInfoSrcMaskBit": subnetBasedVlanInfoSrcMaskBit,
       "subnetBasedVlanInfoName": subnetBasedVlanInfoName,
       "subnetBasedVlanInfoVid": subnetBasedVlanInfoVid,
       "subnetBasedVlanInfoPriority": subnetBasedVlanInfoPriority,
       "subnetBasedVlanInfoEntryState": subnetBasedVlanInfoEntryState,
       "macAuthenticationSetup": macAuthenticationSetup,
       "macAuthenticationState": macAuthenticationState,
       "macAuthenticationNamePrefix": macAuthenticationNamePrefix,
       "macAuthenticationPassword": macAuthenticationPassword,
       "macAuthenticationTimeout": macAuthenticationTimeout,
       "macAuthenticationPortTable": macAuthenticationPortTable,
       "macAuthenticationPortEntry": macAuthenticationPortEntry,
       "macAuthenticationPortState": macAuthenticationPortState,
       "mstp": mstp,
       "mstpGen": mstpGen,
       "mstpGenState": mstpGenState,
       "mstpGenCfgIdName": mstpGenCfgIdName,
       "mstpGenCfgIdRevLevel": mstpGenCfgIdRevLevel,
       "mstpGenCfgIdCfgDigest": mstpGenCfgIdCfgDigest,
       "mstpGenHelloTime": mstpGenHelloTime,
       "mstpGenMaxAge": mstpGenMaxAge,
       "mstpGenForwardDelay": mstpGenForwardDelay,
       "mstpGenMaxHops": mstpGenMaxHops,
       "mstpGenCistRootPathCost": mstpGenCistRootPathCost,
       "mstpGenCistRootBrid": mstpGenCistRootBrid,
       "mstMapTable": mstMapTable,
       "mstMapEntry": mstMapEntry,
       "mstMapIndex": mstMapIndex,
       "mstMapVlans1k": mstMapVlans1k,
       "mstMapVlans2k": mstMapVlans2k,
       "mstMapVlans3k": mstMapVlans3k,
       "mstMapVlans4k": mstMapVlans4k,
       "mstMapRowStatus": mstMapRowStatus,
       "mstVlanTable": mstVlanTable,
       "mstVlanEntry": mstVlanEntry,
       "mstVlanIndex": mstVlanIndex,
       "mstVlanMstIndex": mstVlanMstIndex,
       "mstpPortTable": mstpPortTable,
       "mstpPortEntry": mstpPortEntry,
       "mstpPortIndex": mstpPortIndex,
       "mstpPortOperEdgePort": mstpPortOperEdgePort,
       "mstpPortOperPointToPointMAC": mstpPortOperPointToPointMAC,
       "mstpXstTable": mstpXstTable,
       "mstpXstEntry": mstpXstEntry,
       "mstpXstId": mstpXstId,
       "mstpXstBridgePriority": mstpXstBridgePriority,
       "mstpXstBridgeId": mstpXstBridgeId,
       "mstpXstInternalRootCost": mstpXstInternalRootCost,
       "mstpXstRootPort": mstpXstRootPort,
       "mstpXstTimeSinceTopologyChange": mstpXstTimeSinceTopologyChange,
       "mstpXstTopologyChangesCount": mstpXstTopologyChangesCount,
       "mstpXstPortTable": mstpXstPortTable,
       "mstpXstPortEntry": mstpXstPortEntry,
       "mstpXstPortXstId": mstpXstPortXstId,
       "mstpXstPortIndex": mstpXstPortIndex,
       "mstpXstPortEnable": mstpXstPortEnable,
       "mstpXstPortPriority": mstpXstPortPriority,
       "mstpXstPortPathCost": mstpXstPortPathCost,
       "mstpXstPortState": mstpXstPortState,
       "mstpXstPortDesignatedRoot": mstpXstPortDesignatedRoot,
       "mstpXstPortDesignatedCost": mstpXstPortDesignatedCost,
       "mstpXstPortDesignatedBridge": mstpXstPortDesignatedBridge,
       "mstpXstPortDesignatedPort": mstpXstPortDesignatedPort,
       "mstpNotifications": mstpNotifications,
       "mstpNewRoot": mstpNewRoot,
       "mstpTopologyChange": mstpTopologyChange,
       "radiusServerSetup": radiusServerSetup,
       "radiusAuthServerSetup": radiusAuthServerSetup,
       "radiusAuthServerMode": radiusAuthServerMode,
       "radiusAuthServerTimeout": radiusAuthServerTimeout,
       "radiusAuthServerTable": radiusAuthServerTable,
       "radiusAuthServerEntry": radiusAuthServerEntry,
       "radiusAuthServerIndex": radiusAuthServerIndex,
       "radiusAuthServerIpAddr": radiusAuthServerIpAddr,
       "radiusAuthServerUdpPort": radiusAuthServerUdpPort,
       "radiusAuthServerSharedSecret": radiusAuthServerSharedSecret,
       "radiusAuthServerIpAddressType": radiusAuthServerIpAddressType,
       "radiusAuthServerIpAddress": radiusAuthServerIpAddress,
       "radiusAcctServerSetup": radiusAcctServerSetup,
       "radiusAcctServerTimeout": radiusAcctServerTimeout,
       "radiusAcctServerTable": radiusAcctServerTable,
       "radiusAcctServerEntry": radiusAcctServerEntry,
       "radiusAcctServerIndex": radiusAcctServerIndex,
       "radiusAcctServerIpAddr": radiusAcctServerIpAddr,
       "radiusAcctServerUdpPort": radiusAcctServerUdpPort,
       "radiusAcctServerSharedSecret": radiusAcctServerSharedSecret,
       "radiusAcctServerIpAddressType": radiusAcctServerIpAddressType,
       "radiusAcctServerIpAddress": radiusAcctServerIpAddress,
       "tacacsServerSetup": tacacsServerSetup,
       "tacacsAuthServerSetup": tacacsAuthServerSetup,
       "tacacsAuthServerMode": tacacsAuthServerMode,
       "tacacsAuthServerTimeout": tacacsAuthServerTimeout,
       "tacacsAuthServerTable": tacacsAuthServerTable,
       "tacacsAuthServerEntry": tacacsAuthServerEntry,
       "tacacsAuthServerIndex": tacacsAuthServerIndex,
       "tacacsAuthServerIpAddr": tacacsAuthServerIpAddr,
       "tacacsAuthServerTcpPort": tacacsAuthServerTcpPort,
       "tacacsAuthServerSharedSecret": tacacsAuthServerSharedSecret,
       "tacacsAuthServerIpAddressType": tacacsAuthServerIpAddressType,
       "tacacsAuthServerIpAddress": tacacsAuthServerIpAddress,
       "tacacsAcctServerSetup": tacacsAcctServerSetup,
       "tacacsAcctServerTimeout": tacacsAcctServerTimeout,
       "tacacsAcctServerTable": tacacsAcctServerTable,
       "tacacsAcctServerEntry": tacacsAcctServerEntry,
       "tacacsAcctServerIndex": tacacsAcctServerIndex,
       "tacacsAcctServerIpAddr": tacacsAcctServerIpAddr,
       "tacacsAcctServerTcpPort": tacacsAcctServerTcpPort,
       "tacacsAcctServerSharedSecret": tacacsAcctServerSharedSecret,
       "tacacsAcctServerIpAddressType": tacacsAcctServerIpAddressType,
       "tacacsAcctServerIpAddress": tacacsAcctServerIpAddress,
       "aaaSetup": aaaSetup,
       "authenticationSetup": authenticationSetup,
       "authenticationTypeTable": authenticationTypeTable,
       "authenticationTypeEntry": authenticationTypeEntry,
       "authenticationTypeName": authenticationTypeName,
       "authenticationTypeMethodList": authenticationTypeMethodList,
       "accountingSetup": accountingSetup,
       "accountingUpdatePeriod": accountingUpdatePeriod,
       "accountingTypeTable": accountingTypeTable,
       "accountingTypeEntry": accountingTypeEntry,
       "accountingTypeName": accountingTypeName,
       "accountingTypeActive": accountingTypeActive,
       "accountingTypeBroadcast": accountingTypeBroadcast,
       "accountingTypeMode": accountingTypeMode,
       "accountingTypeMethod": accountingTypeMethod,
       "accountingTypePrivilege": accountingTypePrivilege,
       "vdsl2Ext": vdsl2Ext,
       "xdsl2ExtNotifications": xdsl2ExtNotifications,
       "xdsl2LinePerfLOFSThreshXtuc": xdsl2LinePerfLOFSThreshXtuc,
       "xdsl2LinePerfLOFSThreshXtur": xdsl2LinePerfLOFSThreshXtur,
       "xdsl2LinePerfLPRSThreshXtur": xdsl2LinePerfLPRSThreshXtur,
       "xdsl2ExtLine": xdsl2ExtLine,
       "xdsl2ExtLineTable": xdsl2ExtLineTable,
       "xdsl2ExtLineEntry": xdsl2ExtLineEntry,
       "xdsl2LineCmndConfSelt": xdsl2LineCmndConfSelt,
       "xdsl2ExtLineBandTable": xdsl2ExtLineBandTable,
       "xdsl2ExtLineBandEntry": xdsl2ExtLineBandEntry,
       "xdsl2LineBandStatusActAtp": xdsl2LineBandStatusActAtp,
       "xdsl2LineBandStatusActRxPwr": xdsl2LineBandStatusActRxPwr,
       "xdsl2ExtStatus": xdsl2ExtStatus,
       "xdsl2ExtLineSegmentTable": xdsl2ExtLineSegmentTable,
       "xdsl2ExtLineSegmentEntry": xdsl2ExtLineSegmentEntry,
       "xdsl2LineSegmentLog": xdsl2LineSegmentLog,
       "xdsl2LineSegmentQln": xdsl2LineSegmentQln,
       "xdsl2LineSegmentSnr": xdsl2LineSegmentSnr,
       "xdsl2LineSegmentStatus": xdsl2LineSegmentStatus,
       "xdsl2LineSegmentLogScGroupSize": xdsl2LineSegmentLogScGroupSize,
       "xdsl2LineSegmentQlnScGroupSize": xdsl2LineSegmentQlnScGroupSize,
       "xdsl2LineSegmentSnrScGroupSize": xdsl2LineSegmentSnrScGroupSize,
       "xdsl2ExtSCStatusTable": xdsl2ExtSCStatusTable,
       "xdsl2ExtSCStatusEntry": xdsl2ExtSCStatusEntry,
       "xdsl2SCStatusActAtp": xdsl2SCStatusActAtp,
       "xdsl2ExtSCStatusBandTable": xdsl2ExtSCStatusBandTable,
       "xdsl2ExtSCStatusBandEntry": xdsl2ExtSCStatusBandEntry,
       "xdsl2SCStatusBandSnrMargin": xdsl2SCStatusBandSnrMargin,
       "xdsl2ExtSeltStatusTable": xdsl2ExtSeltStatusTable,
       "xdsl2ExtSeltStatusEntry": xdsl2ExtSeltStatusEntry,
       "xdsl2SeltStatus": xdsl2SeltStatus,
       "xdsl2SeltStatusLineType": xdsl2SeltStatusLineType,
       "xdsl2SeltStatusLineLength": xdsl2SeltStatusLineLength,
       "xdsl2ExtSeltReflectionStatusTable": xdsl2ExtSeltReflectionStatusTable,
       "xdsl2ExtSeltReflectionStatusEntry": xdsl2ExtSeltReflectionStatusEntry,
       "xdsl2SeltReflection": xdsl2SeltReflection,
       "xdsl2SeltDelay": xdsl2SeltDelay,
       "xdsl2SeltError": xdsl2SeltError,
       "xdsl2SeltAtn180kHz": xdsl2SeltAtn180kHz,
       "xdsl2SeltAtn300kHz": xdsl2SeltAtn300kHz,
       "xdsl2SeltFitError": xdsl2SeltFitError,
       "xdsl2SeltFitTermination": xdsl2SeltFitTermination,
       "xdsl2ExtPM": xdsl2ExtPM,
       "xdsl2ExtPMLine": xdsl2ExtPMLine,
       "xdsl2ExtPMLineCurrTable": xdsl2ExtPMLineCurrTable,
       "xdsl2ExtPMLineCurrEntry": xdsl2ExtPMLineCurrEntry,
       "xdsl2PMLSinceLinkFecs": xdsl2PMLSinceLinkFecs,
       "xdsl2PMLSinceLinkEs": xdsl2PMLSinceLinkEs,
       "xdsl2PMLSinceLinkSes": xdsl2PMLSinceLinkSes,
       "xdsl2PMLSinceLinkLoss": xdsl2PMLSinceLinkLoss,
       "xdsl2PMLSinceLinkUas": xdsl2PMLSinceLinkUas,
       "xdsl2PMLSinceLinkLofs": xdsl2PMLSinceLinkLofs,
       "xdsl2PMLSinceLinkLol": xdsl2PMLSinceLinkLol,
       "xdsl2PMLSinceLinkLols": xdsl2PMLSinceLinkLols,
       "xdsl2PMLSinceLinkLpr": xdsl2PMLSinceLinkLpr,
       "xdsl2PMLSinceLinkLprs": xdsl2PMLSinceLinkLprs,
       "xdsl2PMLCurr15MLofs": xdsl2PMLCurr15MLofs,
       "xdsl2PMLCurr15MLol": xdsl2PMLCurr15MLol,
       "xdsl2PMLCurr15MLols": xdsl2PMLCurr15MLols,
       "xdsl2PMLCurr15MLpr": xdsl2PMLCurr15MLpr,
       "xdsl2PMLCurr15MLprs": xdsl2PMLCurr15MLprs,
       "xdsl2PMLCurr1DayLofs": xdsl2PMLCurr1DayLofs,
       "xdsl2PMLCurr1DayLol": xdsl2PMLCurr1DayLol,
       "xdsl2PMLCurr1DayLols": xdsl2PMLCurr1DayLols,
       "xdsl2PMLCurr1DayLpr": xdsl2PMLCurr1DayLpr,
       "xdsl2PMLCurr1DayLprs": xdsl2PMLCurr1DayLprs,
       "xdsl2PMLSinceLinkInmEqInp": xdsl2PMLSinceLinkInmEqInp,
       "xdsl2PMLSinceLinkInmIAT": xdsl2PMLSinceLinkInmIAT,
       "xdsl2PMLSinceLinkInmME": xdsl2PMLSinceLinkInmME,
       "xdsl2PMLCurr15MInmEqInp": xdsl2PMLCurr15MInmEqInp,
       "xdsl2PMLCurr15MInmIAT": xdsl2PMLCurr15MInmIAT,
       "xdsl2PMLCurr15MInmME": xdsl2PMLCurr15MInmME,
       "xdsl2PMLCurr1DayInmEqInp": xdsl2PMLCurr1DayInmEqInp,
       "xdsl2PMLCurr1DayInmIAT": xdsl2PMLCurr1DayInmIAT,
       "xdsl2PMLCurr1DayInmME": xdsl2PMLCurr1DayInmME,
       "xdsl2ExtPMLineHist15MinTable": xdsl2ExtPMLineHist15MinTable,
       "xdsl2ExtPMLineHist15MinEntry": xdsl2ExtPMLineHist15MinEntry,
       "xdsl2PMLHist15MLofs": xdsl2PMLHist15MLofs,
       "xdsl2PMLHist15MLol": xdsl2PMLHist15MLol,
       "xdsl2PMLHist15MLols": xdsl2PMLHist15MLols,
       "xdsl2PMLHist15MLpr": xdsl2PMLHist15MLpr,
       "xdsl2PMLHist15MLprs": xdsl2PMLHist15MLprs,
       "xdsl2PMLHist15MInmEqInp": xdsl2PMLHist15MInmEqInp,
       "xdsl2PMLHist15MInmIAT": xdsl2PMLHist15MInmIAT,
       "xdsl2PMLHist15MInmME": xdsl2PMLHist15MInmME,
       "xdsl2ExtPMLineHist1DayTable": xdsl2ExtPMLineHist1DayTable,
       "xdsl2ExtPMLineHist1DayEntry": xdsl2ExtPMLineHist1DayEntry,
       "xdsl2PMLHist1DLofs": xdsl2PMLHist1DLofs,
       "xdsl2PMLHist1DLol": xdsl2PMLHist1DLol,
       "xdsl2PMLHist1DLols": xdsl2PMLHist1DLols,
       "xdsl2PMLHist1DLpr": xdsl2PMLHist1DLpr,
       "xdsl2PMLHist1DLprs": xdsl2PMLHist1DLprs,
       "xdsl2PMLHist1DInmEqInp": xdsl2PMLHist1DInmEqInp,
       "xdsl2PMLHist1DInmIAT": xdsl2PMLHist1DInmIAT,
       "xdsl2PMLHist1DInmME": xdsl2PMLHist1DInmME,
       "xdsl2ExtPMChannel": xdsl2ExtPMChannel,
       "xdsl2ExtPMChCurrTable": xdsl2ExtPMChCurrTable,
       "xdsl2ExtPMChCurrEntry": xdsl2ExtPMChCurrEntry,
       "xdsl2PMChSinceLinkUncorrectedCWs": xdsl2PMChSinceLinkUncorrectedCWs,
       "xdsl2PMChCurr15MUncorrectedCWs": xdsl2PMChCurr15MUncorrectedCWs,
       "xdsl2PMChCurr1DayUncorrectedCWs": xdsl2PMChCurr1DayUncorrectedCWs,
       "xdsl2PMChSinceLinkCodingViolations": xdsl2PMChSinceLinkCodingViolations,
       "xdsl2PMChSinceLinkCorrectedBlocks": xdsl2PMChSinceLinkCorrectedBlocks,
       "xdsl2ExtPMChHist15MinTable": xdsl2ExtPMChHist15MinTable,
       "xdsl2ExtPMChHist15MinEntry": xdsl2ExtPMChHist15MinEntry,
       "xdsl2PMChHist15MUncorrectedCWs": xdsl2PMChHist15MUncorrectedCWs,
       "xdsl2ExtPMChHist1DTable": xdsl2ExtPMChHist1DTable,
       "xdsl2ExtPMChHist1DEntry": xdsl2ExtPMChHist1DEntry,
       "xdsl2PMChHist1DayUncorrectedCWs": xdsl2PMChHist1DayUncorrectedCWs,
       "xdsl2ExtProfile": xdsl2ExtProfile,
       "xdsl2ExtProfileLine": xdsl2ExtProfileLine,
       "xdsl2ExtLineConfTemplateTable": xdsl2ExtLineConfTemplateTable,
       "xdsl2ExtLineConfTemplateEntry": xdsl2ExtLineConfTemplateEntry,
       "xdsl2LConfTempPortList": xdsl2LConfTempPortList,
       "xdsl2LConfTempInmConfProfile": xdsl2LConfTempInmConfProfile,
       "xdsl2ExtLineConfProfTable": xdsl2ExtLineConfProfTable,
       "xdsl2ExtLineConfProfEntry": xdsl2ExtLineConfProfEntry,
       "xdsl2LConfProfBitSwapDs": xdsl2LConfProfBitSwapDs,
       "xdsl2LConfProfBitSwapUs": xdsl2LConfProfBitSwapUs,
       "xdsl2LConfProfPortList": xdsl2LConfProfPortList,
       "xdsl2MaxNumLineConfTemplate": xdsl2MaxNumLineConfTemplate,
       "xdsl2MaxNumLineConfProfile": xdsl2MaxNumLineConfProfile,
       "xdsl2ExtInmConfProfTable": xdsl2ExtInmConfProfTable,
       "xdsl2ExtInmConfProfEntry": xdsl2ExtInmConfProfEntry,
       "xdsl2ExtInmConfProfProfileName": xdsl2ExtInmConfProfProfileName,
       "xdsl2ExtInmConfProfVtucInpEq": xdsl2ExtInmConfProfVtucInpEq,
       "xdsl2ExtInmConfProfVturInpEq": xdsl2ExtInmConfProfVturInpEq,
       "xdsl2ExtInmConfProfVtucCC": xdsl2ExtInmConfProfVtucCC,
       "xdsl2ExtInmConfProfVturCC": xdsl2ExtInmConfProfVturCC,
       "xdsl2ExtInmConfProfVtucIATO": xdsl2ExtInmConfProfVtucIATO,
       "xdsl2ExtInmConfProfVturIATO": xdsl2ExtInmConfProfVturIATO,
       "xdsl2ExtInmConfProfVtucIATS": xdsl2ExtInmConfProfVtucIATS,
       "xdsl2ExtInmConfProfVturIATS": xdsl2ExtInmConfProfVturIATS,
       "xdsl2ExtInmConfProfRowStatus": xdsl2ExtInmConfProfRowStatus,
       "xdsl2ExtInmConfProfPortList": xdsl2ExtInmConfProfPortList,
       "xdsl2MaxNumInmConfProfile": xdsl2MaxNumInmConfProfile,
       "xdsl2ExtProfileChannel": xdsl2ExtProfileChannel,
       "xdsl2ExtChConfProfileTable": xdsl2ExtChConfProfileTable,
       "xdsl2ExtChConfProfileEntry": xdsl2ExtChConfProfileEntry,
       "xdsl2ChConfProfPhyRDs": xdsl2ChConfProfPhyRDs,
       "xdsl2ChConfProfPhyRUs": xdsl2ChConfProfPhyRUs,
       "xdsl2ChConfProfPortList": xdsl2ChConfProfPortList,
       "xdsl2MaxNumChConfProfile": xdsl2MaxNumChConfProfile,
       "xdsl2ExtProfileAlarmConf": xdsl2ExtProfileAlarmConf,
       "xdsl2ExtLineAlarmConfTemplateTable": xdsl2ExtLineAlarmConfTemplateTable,
       "xdsl2ExtLineAlarmConfTemplateEntry": xdsl2ExtLineAlarmConfTemplateEntry,
       "xdsl2LAlarmConfTempPortList": xdsl2LAlarmConfTempPortList,
       "xdsl2ExtLineAlarmConfProfileTable": xdsl2ExtLineAlarmConfProfileTable,
       "xdsl2ExtLineAlarmConfProfileEntry": xdsl2ExtLineAlarmConfProfileEntry,
       "xdsl2LineAlarmConfProfileXtucThresh15MinLofs": xdsl2LineAlarmConfProfileXtucThresh15MinLofs,
       "xdsl2LineAlarmConfProfileXturThresh15MinLofs": xdsl2LineAlarmConfProfileXturThresh15MinLofs,
       "xdsl2LAlarmConfProfilePortList": xdsl2LAlarmConfProfilePortList,
       "xdsl2LineAlarmConfProfileXturThresh15MinLprs": xdsl2LineAlarmConfProfileXturThresh15MinLprs,
       "xdsl2ExtChAlarmConfProfileTable": xdsl2ExtChAlarmConfProfileTable,
       "xdsl2ExtChAlarmConfProfileEntry": xdsl2ExtChAlarmConfProfileEntry,
       "xdsl2ChAlarmConfProfilePortList": xdsl2ChAlarmConfProfilePortList,
       "xdsl2MaxNumLineAlarmConfTemplate": xdsl2MaxNumLineAlarmConfTemplate,
       "xdsl2MaxNumLineAlarmConfProfile": xdsl2MaxNumLineAlarmConfProfile,
       "xdsl2MaxNumChAlarmConfProfile": xdsl2MaxNumChAlarmConfProfile,
       "macBasedVlanSetup": macBasedVlanSetup,
       "macBasedVlanTable": macBasedVlanTable,
       "macBasedVlanEntry": macBasedVlanEntry,
       "macBasedVlanName": macBasedVlanName,
       "macBasedVlanMAC": macBasedVlanMAC,
       "macBasedVlanVlanId": macBasedVlanVlanId,
       "macBasedVlan8021pPriority": macBasedVlan8021pPriority,
       "macBasedVlanRowstatus": macBasedVlanRowstatus,
       "vlanProfileSetup": vlanProfileSetup,
       "vlanProfileTable": vlanProfileTable,
       "vlanProfileEntry": vlanProfileEntry,
       "vlanProfileName": vlanProfileName,
       "vlanProfileMacLearning": vlanProfileMacLearning,
       "vlanProfileUnknownMulticastDrop": vlanProfileUnknownMulticastDrop,
       "vlanProfileRowStatus": vlanProfileRowStatus,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "profileName": profileName,
       "dosPreventionSetup": dosPreventionSetup,
       "dosPreventionActive": dosPreventionActive,
       "dosPreventionMacChecking": dosPreventionMacChecking,
       "dosPreventionIPChecking": dosPreventionIPChecking,
       "dosPreventionICMPFragment": dosPreventionICMPFragment,
       "dosPreventionTCPSYN": dosPreventionTCPSYN,
       "dosPreventionTCPFragment": dosPreventionTCPFragment,
       "dosPreventionTCPControlSN": dosPreventionTCPControlSN,
       "dosPreventionTCPPort": dosPreventionTCPPort,
       "dosPreventionTCPSF": dosPreventionTCPSF,
       "dosPreventionTCPFUP": dosPreventionTCPFUP,
       "dosPreventionUDPPort": dosPreventionUDPPort,
       "ipv6Setup": ipv6Setup,
       "ipv6DefaultMgmt": ipv6DefaultMgmt,
       "inbandIpv6Setup": inbandIpv6Setup,
       "inbandIpv6Vid": inbandIpv6Vid,
       "inbandIpv6StaticIp": inbandIpv6StaticIp,
       "inbandIpv6StaticSubnetMask": inbandIpv6StaticSubnetMask,
       "inbandIpv6StaticGateway": inbandIpv6StaticGateway,
       "outOfBandIpv6Setup": outOfBandIpv6Setup,
       "outOfBandIpv6Ip": outOfBandIpv6Ip,
       "outOfBandIpv6SubnetMask": outOfBandIpv6SubnetMask,
       "outOfBandIpv6Gateway": outOfBandIpv6Gateway,
       "l2ptSetup": l2ptSetup,
       "l2ptState": l2ptState,
       "l2ptMacAddr": l2ptMacAddr,
       "l2ptTable": l2ptTable,
       "l2ptEntry": l2ptEntry,
       "l2ptProtocolGroup": l2ptProtocolGroup,
       "l2ptPointToPointProtocolGroup": l2ptPointToPointProtocolGroup,
       "l2ptMode": l2ptMode,
       "vlanMappingSetup": vlanMappingSetup,
       "vlanMappingState": vlanMappingState,
       "vlanMappingPortTable": vlanMappingPortTable,
       "vlanMappingPortEntry": vlanMappingPortEntry,
       "vlanMappingPortState": vlanMappingPortState,
       "vlanMappingPortDropMiss": vlanMappingPortDropMiss,
       "vlanMappingRuleTable": vlanMappingRuleTable,
       "vlanMappingRuleEntry": vlanMappingRuleEntry,
       "vlanMappingRuleName": vlanMappingRuleName,
       "vlanMappingRulePort": vlanMappingRulePort,
       "vlanMappingRuleVid": vlanMappingRuleVid,
       "vlanMappingRuleTransVid": vlanMappingRuleTransVid,
       "vlanMappingRulePriority": vlanMappingRulePriority,
       "vlanMappingRuleRowStatus": vlanMappingRuleRowStatus,
       "vlanMappingRuleReplacePrio": vlanMappingRuleReplacePrio,
       "transceiverInfo": transceiverInfo,
       "transceiverSerialInfoTable": transceiverSerialInfoTable,
       "transceiverSerialInfoEntry": transceiverSerialInfoEntry,
       "transceiverSerialInfoEntryPort": transceiverSerialInfoEntryPort,
       "transceiverSerialInfoEntryStatus": transceiverSerialInfoEntryStatus,
       "transceiverSerialInfoEntryVendor": transceiverSerialInfoEntryVendor,
       "transceiverSerialInfoEntryPartNo": transceiverSerialInfoEntryPartNo,
       "transceiverSerialInfoEntrySerialNo": transceiverSerialInfoEntrySerialNo,
       "transceiverSerialInfoEntryRevision": transceiverSerialInfoEntryRevision,
       "transceiverSerialInfoEntryDateCode": transceiverSerialInfoEntryDateCode,
       "transceiverSerialInfoEntryTransceiver": transceiverSerialInfoEntryTransceiver,
       "transceiverDdmInfoTable": transceiverDdmInfoTable,
       "transceiverDdmInfoEntry": transceiverDdmInfoEntry,
       "transceiverDdmInfoEntryPort": transceiverDdmInfoEntryPort,
       "transceiverDdmInfoEntryType": transceiverDdmInfoEntryType,
       "transceiverDdmInfoEntryAlarmMax": transceiverDdmInfoEntryAlarmMax,
       "transceiverDdmInfoEntryAlarmMin": transceiverDdmInfoEntryAlarmMin,
       "transceiverDdmInfoEntryWarnMax": transceiverDdmInfoEntryWarnMax,
       "transceiverDdmInfoEntryWarnMin": transceiverDdmInfoEntryWarnMin,
       "transceiverDdmInfoEntryCurrent": transceiverDdmInfoEntryCurrent,
       "transceiverDdmInfoEntryDescription": transceiverDdmInfoEntryDescription,
       "pppoeIASetup": pppoeIASetup,
       "globalPPPoEIA": globalPPPoEIA,
       "globalPPPoEIAEnable": globalPPPoEIAEnable,
       "globalPPPoEIACircuitIDInfoEnable": globalPPPoEIACircuitIDInfoEnable,
       "globalPPPoEIACircuitIDInfoData": globalPPPoEIACircuitIDInfoData,
       "globalPPPoEIARemoteIDEnable": globalPPPoEIARemoteIDEnable,
       "globalPPPoEIARemoteIDData": globalPPPoEIARemoteIDData,
       "globalPPPoEIARemoteIDType": globalPPPoEIARemoteIDType,
       "globalPPPoEIACircuitIDType": globalPPPoEIACircuitIDType,
       "pppoeIA": pppoeIA,
       "maxNumberOfPPPoEIA": maxNumberOfPPPoEIA,
       "pppoeIATable": pppoeIATable,
       "pppoeIAEntry": pppoeIAEntry,
       "pppoeIAVID": pppoeIAVID,
       "pppoeIACircuitIDInfoEnable": pppoeIACircuitIDInfoEnable,
       "pppoeIACircuitIDInfoData": pppoeIACircuitIDInfoData,
       "pppoeIARemoteIDEnable": pppoeIARemoteIDEnable,
       "pppoeIARemoteIDData": pppoeIARemoteIDData,
       "pppoeIARowStatus": pppoeIARowStatus,
       "pppoeIARemoteIDType": pppoeIARemoteIDType,
       "pppoeIACircuitIDType": pppoeIACircuitIDType,
       "iwfSetup": iwfSetup,
       "pvcRuleTable": pvcRuleTable,
       "pvcRuleEntry": pvcRuleEntry,
       "pvcRulePort": pvcRulePort,
       "pvcRuleVpi": pvcRuleVpi,
       "pvcRuleVci": pvcRuleVci,
       "pvcRulePvid": pvcRulePvid,
       "pvcRuleEncap": pvcRuleEncap,
       "pvcRulePriority": pvcRulePriority,
       "pvcRuleFCS": pvcRuleFCS,
       "pvcRuleMVlan": pvcRuleMVlan,
       "pvcRuleRowStatus": pvcRuleRowStatus,
       "ippvcRuleTable": ippvcRuleTable,
       "ippvcRuleEntry": ippvcRuleEntry,
       "ippvcRulePort": ippvcRulePort,
       "ippvcRuleVpi": ippvcRuleVpi,
       "ippvcRuleVci": ippvcRuleVci,
       "ippvcRulePvid": ippvcRulePvid,
       "ippvcRuleEncap": ippvcRuleEncap,
       "ippvcRulePriority": ippvcRulePriority,
       "ippvcRuleSubnetIp": ippvcRuleSubnetIp,
       "ippvcRuleSubnetMask": ippvcRuleSubnetMask,
       "ippvcRuleDefaultRoute": ippvcRuleDefaultRoute,
       "ippvcRuleRowStatus": ippvcRuleRowStatus,
       "paepvcRuleTable": paepvcRuleTable,
       "paepvcRuleEntry": paepvcRuleEntry,
       "paepvcRulePort": paepvcRulePort,
       "paepvcRuleVpi": paepvcRuleVpi,
       "paepvcRuleVci": paepvcRuleVci,
       "paepvcRulePvid": paepvcRulePvid,
       "paepvcRuleEncap": paepvcRuleEncap,
       "paepvcRulePriority": paepvcRulePriority,
       "paepvcRuleRowStatus": paepvcRuleRowStatus,
       "xdslBondingSetup": xdslBondingSetup,
       "xdslBondingConfigTable": xdslBondingConfigTable,
       "xdslBondingConfigEntry": xdslBondingConfigEntry,
       "xdslBondingConfigName": xdslBondingConfigName,
       "xdslBondingConfigMemberPort": xdslBondingConfigMemberPort,
       "xdslBondingConfigRowStatus": xdslBondingConfigRowStatus,
       "xdslBondingStatusTable": xdslBondingStatusTable,
       "xdslBondingStatusEntry": xdslBondingStatusEntry,
       "xdslBondingStatusActive": xdslBondingStatusActive,
       "xdslBondingStatusMemberPort": xdslBondingStatusMemberPort,
       "xdslBondingStatusActivePort": xdslBondingStatusActivePort,
       "xdslBondingStatusMainPort": xdslBondingStatusMainPort,
       "xdslBondingStatusFlagType": xdslBondingStatusFlagType,
       "xdslBondingStatusRateUs": xdslBondingStatusRateUs,
       "xdslBondingStatusRateDs": xdslBondingStatusRateDs,
       "macFlush": macFlush,
       "macFlushTable": macFlushTable,
       "macFlushEntry": macFlushEntry,
       "macFlushPortIndex": macFlushPortIndex,
       "macFlushPortConfig": macFlushPortConfig}
)
