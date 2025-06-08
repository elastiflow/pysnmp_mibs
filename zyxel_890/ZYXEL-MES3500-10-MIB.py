# SNMP MIB module (ZYXEL-MES3500-10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZyXEL-MES3500-10-MIB.mib
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

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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


# MODULE-IDENTITY

faultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26)
)

faultTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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
_EsSeries_ObjectIdentity = ObjectIdentity
esSeries = _EsSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8)
)
_Mes3500_10_ObjectIdentity = ObjectIdentity
mes3500_10 = _Mes3500_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1)
)
_SysSwPlatformMajorVers_Type = Integer32
_SysSwPlatformMajorVers_Object = MibScalar
sysSwPlatformMajorVers = _SysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 1),
    _SysSwPlatformMajorVers_Type()
)
sysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setStatus("mandatory")
_SysSwPlatformMinorVers_Type = Integer32
_SysSwPlatformMinorVers_Object = MibScalar
sysSwPlatformMinorVers = _SysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 2),
    _SysSwPlatformMinorVers_Type()
)
sysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setStatus("mandatory")
_SysSwModelString_Type = DisplayString
_SysSwModelString_Object = MibScalar
sysSwModelString = _SysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 3),
    _SysSwModelString_Type()
)
sysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModelString.setStatus("mandatory")
_SysSwVersionControlNbr_Type = Integer32
_SysSwVersionControlNbr_Object = MibScalar
sysSwVersionControlNbr = _SysSwVersionControlNbr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 4),
    _SysSwVersionControlNbr_Type()
)
sysSwVersionControlNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionControlNbr.setStatus("mandatory")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 5),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("mandatory")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 6),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("mandatory")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 7),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("mandatory")
_SysHwMajorVers_Type = Integer32
_SysHwMajorVers_Object = MibScalar
sysHwMajorVers = _SysHwMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 8),
    _SysHwMajorVers_Type()
)
sysHwMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVers.setStatus("mandatory")
_SysHwMinorVers_Type = Integer32
_SysHwMinorVers_Object = MibScalar
sysHwMinorVers = _SysHwMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 9),
    _SysHwMinorVers_Type()
)
sysHwMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVers.setStatus("mandatory")
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 10),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 1, 11),
    _SysSwBootUpImage_Type()
)
sysSwBootUpImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwBootUpImage.setStatus("mandatory")
_RateLimitSetup_ObjectIdentity = ObjectIdentity
rateLimitSetup = _RateLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2)
)
_RateLimitState_Type = EnabledStatus
_RateLimitState_Object = MibScalar
rateLimitState = _RateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 1),
    _RateLimitState_Type()
)
rateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitState.setStatus("mandatory")
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("mandatory")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("mandatory")
_RateLimitPortState_Type = EnabledStatus
_RateLimitPortState_Object = MibTableColumn
rateLimitPortState = _RateLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 1),
    _RateLimitPortState_Type()
)
rateLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortState.setStatus("mandatory")
_RateLimitPortCommitRate_Type = Integer32
_RateLimitPortCommitRate_Object = MibTableColumn
rateLimitPortCommitRate = _RateLimitPortCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 2),
    _RateLimitPortCommitRate_Type()
)
rateLimitPortCommitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortCommitRate.setStatus("mandatory")
_RateLimitPortPeakRate_Type = Integer32
_RateLimitPortPeakRate_Object = MibTableColumn
rateLimitPortPeakRate = _RateLimitPortPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 3),
    _RateLimitPortPeakRate_Type()
)
rateLimitPortPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortPeakRate.setStatus("mandatory")
_RateLimitPortEgrRate_Type = Integer32
_RateLimitPortEgrRate_Object = MibTableColumn
rateLimitPortEgrRate = _RateLimitPortEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 4),
    _RateLimitPortEgrRate_Type()
)
rateLimitPortEgrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrRate.setStatus("mandatory")
_RateLimitPortPeakState_Type = EnabledStatus
_RateLimitPortPeakState_Object = MibTableColumn
rateLimitPortPeakState = _RateLimitPortPeakState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 5),
    _RateLimitPortPeakState_Type()
)
rateLimitPortPeakState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortPeakState.setStatus("mandatory")
_RateLimitPortEgrState_Type = EnabledStatus
_RateLimitPortEgrState_Object = MibTableColumn
rateLimitPortEgrState = _RateLimitPortEgrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 6),
    _RateLimitPortEgrState_Type()
)
rateLimitPortEgrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrState.setStatus("mandatory")
_RateLimitPortCommitState_Type = EnabledStatus
_RateLimitPortCommitState_Object = MibTableColumn
rateLimitPortCommitState = _RateLimitPortCommitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 2, 2, 1, 7),
    _RateLimitPortCommitState_Type()
)
rateLimitPortCommitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortCommitState.setStatus("mandatory")
_BrLimitSetup_ObjectIdentity = ObjectIdentity
brLimitSetup = _BrLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3)
)
_BrLimitState_Type = EnabledStatus
_BrLimitState_Object = MibScalar
brLimitState = _BrLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 1),
    _BrLimitState_Type()
)
brLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitState.setStatus("mandatory")
_BrLimitPortTable_Object = MibTable
brLimitPortTable = _BrLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2)
)
if mibBuilder.loadTexts:
    brLimitPortTable.setStatus("mandatory")
_BrLimitPortEntry_Object = MibTableRow
brLimitPortEntry = _BrLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1)
)
brLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    brLimitPortEntry.setStatus("mandatory")
_BrLimitPortBrState_Type = EnabledStatus
_BrLimitPortBrState_Object = MibTableColumn
brLimitPortBrState = _BrLimitPortBrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 1),
    _BrLimitPortBrState_Type()
)
brLimitPortBrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrState.setStatus("mandatory")
_BrLimitPortBrRate_Type = Integer32
_BrLimitPortBrRate_Object = MibTableColumn
brLimitPortBrRate = _BrLimitPortBrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 2),
    _BrLimitPortBrRate_Type()
)
brLimitPortBrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrRate.setStatus("mandatory")
_BrLimitPortMcState_Type = EnabledStatus
_BrLimitPortMcState_Object = MibTableColumn
brLimitPortMcState = _BrLimitPortMcState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 3),
    _BrLimitPortMcState_Type()
)
brLimitPortMcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcState.setStatus("mandatory")
_BrLimitPortMcRate_Type = Integer32
_BrLimitPortMcRate_Object = MibTableColumn
brLimitPortMcRate = _BrLimitPortMcRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 4),
    _BrLimitPortMcRate_Type()
)
brLimitPortMcRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcRate.setStatus("mandatory")
_BrLimitPortDlfState_Type = EnabledStatus
_BrLimitPortDlfState_Object = MibTableColumn
brLimitPortDlfState = _BrLimitPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 5),
    _BrLimitPortDlfState_Type()
)
brLimitPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfState.setStatus("mandatory")
_BrLimitPortDlfRate_Type = Integer32
_BrLimitPortDlfRate_Object = MibTableColumn
brLimitPortDlfRate = _BrLimitPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 6),
    _BrLimitPortDlfRate_Type()
)
brLimitPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfRate.setStatus("mandatory")
_BrLimitPortShutdown_Type = EnabledStatus
_BrLimitPortShutdown_Object = MibTableColumn
brLimitPortShutdown = _BrLimitPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 2, 1, 7),
    _BrLimitPortShutdown_Type()
)
brLimitPortShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortShutdown.setStatus("mandatory")
_BrLimitShutdown_Type = EnabledStatus
_BrLimitShutdown_Object = MibScalar
brLimitShutdown = _BrLimitShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 3, 3),
    _BrLimitShutdown_Type()
)
brLimitShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitShutdown.setStatus("mandatory")
_PortSecuritySetup_ObjectIdentity = ObjectIdentity
portSecuritySetup = _PortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4)
)
_PortSecurityState_Type = EnabledStatus
_PortSecurityState_Object = MibScalar
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 1),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("mandatory")
_PortSecurityPortTable_Object = MibTable
portSecurityPortTable = _PortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 2)
)
if mibBuilder.loadTexts:
    portSecurityPortTable.setStatus("mandatory")
_PortSecurityPortEntry_Object = MibTableRow
portSecurityPortEntry = _PortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 2, 1)
)
portSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portSecurityPortEntry.setStatus("mandatory")
_PortSecurityPortState_Type = EnabledStatus
_PortSecurityPortState_Object = MibTableColumn
portSecurityPortState = _PortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 2, 1, 1),
    _PortSecurityPortState_Type()
)
portSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortState.setStatus("mandatory")
_PortSecurityPortLearnState_Type = EnabledStatus
_PortSecurityPortLearnState_Object = MibTableColumn
portSecurityPortLearnState = _PortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 2, 1, 2),
    _PortSecurityPortLearnState_Type()
)
portSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setStatus("mandatory")
_PortSecurityPortCount_Type = Integer32
_PortSecurityPortCount_Object = MibTableColumn
portSecurityPortCount = _PortSecurityPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 2, 1, 3),
    _PortSecurityPortCount_Type()
)
portSecurityPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortCount.setStatus("mandatory")
_PortSecurityPortShutdown_Type = EnabledStatus
_PortSecurityPortShutdown_Object = MibTableColumn
portSecurityPortShutdown = _PortSecurityPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 2, 1, 4),
    _PortSecurityPortShutdown_Type()
)
portSecurityPortShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortShutdown.setStatus("mandatory")
_PortSecurityMacFreeze_Type = PortList
_PortSecurityMacFreeze_Object = MibScalar
portSecurityMacFreeze = _PortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 3),
    _PortSecurityMacFreeze_Type()
)
portSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacFreeze.setStatus("mandatory")
_PortSecurityShutdown_Type = EnabledStatus
_PortSecurityShutdown_Object = MibScalar
portSecurityShutdown = _PortSecurityShutdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 4, 6),
    _PortSecurityShutdown_Type()
)
portSecurityShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityShutdown.setStatus("mandatory")
_VlanTrunkSetup_ObjectIdentity = ObjectIdentity
vlanTrunkSetup = _VlanTrunkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 5)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("mandatory")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 5, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("mandatory")
_VlanTrunkPortState_Type = EnabledStatus
_VlanTrunkPortState_Object = MibTableColumn
vlanTrunkPortState = _VlanTrunkPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 5, 1, 1, 1),
    _VlanTrunkPortState_Type()
)
vlanTrunkPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setStatus("mandatory")
_VlanStackSetup_ObjectIdentity = ObjectIdentity
vlanStackSetup = _VlanStackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7)
)
_VlanStackState_Type = EnabledStatus
_VlanStackState_Object = MibScalar
vlanStackState = _VlanStackState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 1),
    _VlanStackState_Type()
)
vlanStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackState.setStatus("mandatory")
_VlanStackPortTable_Object = MibTable
vlanStackPortTable = _VlanStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 3)
)
if mibBuilder.loadTexts:
    vlanStackPortTable.setStatus("mandatory")
_VlanStackPortEntry_Object = MibTableRow
vlanStackPortEntry = _VlanStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 3, 1)
)
vlanStackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanStackPortEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 3, 1, 1),
    _VlanStackPortMode_Type()
)
vlanStackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortMode.setStatus("mandatory")
_VlanStackPortVid_Type = Integer32
_VlanStackPortVid_Object = MibTableColumn
vlanStackPortVid = _VlanStackPortVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 3, 1, 2),
    _VlanStackPortVid_Type()
)
vlanStackPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortVid.setStatus("mandatory")


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
        *(("prioriry-0", 0),
          ("prioriry-1", 1),
          ("prioriry-2", 2),
          ("prioriry-3", 3),
          ("prioriry-4", 4),
          ("prioriry-5", 5),
          ("prioriry-6", 6),
          ("prioriry-7", 7))
    )


_VlanStackPortPrio_Type.__name__ = "Integer32"
_VlanStackPortPrio_Object = MibTableColumn
vlanStackPortPrio = _VlanStackPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 3, 1, 3),
    _VlanStackPortPrio_Type()
)
vlanStackPortPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortPrio.setStatus("mandatory")
_VlanStackTunnelPortTpid_Type = Integer32
_VlanStackTunnelPortTpid_Object = MibTableColumn
vlanStackTunnelPortTpid = _VlanStackTunnelPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 3, 1, 4),
    _VlanStackTunnelPortTpid_Type()
)
vlanStackTunnelPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackTunnelPortTpid.setStatus("mandatory")
_SelectiveQinQTable_Object = MibTable
selectiveQinQTable = _SelectiveQinQTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4)
)
if mibBuilder.loadTexts:
    selectiveQinQTable.setStatus("mandatory")
_SelectiveQinQEntry_Object = MibTableRow
selectiveQinQEntry = _SelectiveQinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1)
)
selectiveQinQEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "selectiveQinQPort"),
    (0, "ZYXEL-MES3500-10-MIB", "selectiveQinQCvid"),
)
if mibBuilder.loadTexts:
    selectiveQinQEntry.setStatus("mandatory")
_SelectiveQinQName_Type = DisplayString
_SelectiveQinQName_Object = MibTableColumn
selectiveQinQName = _SelectiveQinQName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1, 1),
    _SelectiveQinQName_Type()
)
selectiveQinQName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQName.setStatus("mandatory")
_SelectiveQinQPort_Type = Integer32
_SelectiveQinQPort_Object = MibTableColumn
selectiveQinQPort = _SelectiveQinQPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1, 2),
    _SelectiveQinQPort_Type()
)
selectiveQinQPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectiveQinQPort.setStatus("mandatory")
_SelectiveQinQCvid_Type = Integer32
_SelectiveQinQCvid_Object = MibTableColumn
selectiveQinQCvid = _SelectiveQinQCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1, 3),
    _SelectiveQinQCvid_Type()
)
selectiveQinQCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selectiveQinQCvid.setStatus("mandatory")
_SelectiveQinQSpvid_Type = Integer32
_SelectiveQinQSpvid_Object = MibTableColumn
selectiveQinQSpvid = _SelectiveQinQSpvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1, 4),
    _SelectiveQinQSpvid_Type()
)
selectiveQinQSpvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQSpvid.setStatus("mandatory")


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
        *(("prioriry-0", 0),
          ("prioriry-1", 1),
          ("prioriry-2", 2),
          ("prioriry-3", 3),
          ("prioriry-4", 4),
          ("prioriry-5", 5),
          ("prioriry-6", 6),
          ("prioriry-7", 7))
    )


_SelectiveQinQPriority_Type.__name__ = "Integer32"
_SelectiveQinQPriority_Object = MibTableColumn
selectiveQinQPriority = _SelectiveQinQPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1, 5),
    _SelectiveQinQPriority_Type()
)
selectiveQinQPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectiveQinQPriority.setStatus("mandatory")
_SelectiveQinQRowStatus_Type = RowStatus
_SelectiveQinQRowStatus_Object = MibTableColumn
selectiveQinQRowStatus = _SelectiveQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 7, 4, 1, 6),
    _SelectiveQinQRowStatus_Type()
)
selectiveQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    selectiveQinQRowStatus.setStatus("mandatory")
_Dot1xSetup_ObjectIdentity = ObjectIdentity
dot1xSetup = _Dot1xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8)
)
_PortAuthState_Type = EnabledStatus
_PortAuthState_Object = MibScalar
portAuthState = _PortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 3),
    _PortAuthState_Type()
)
portAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthState.setStatus("mandatory")
_PortAuthTable_Object = MibTable
portAuthTable = _PortAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4)
)
if mibBuilder.loadTexts:
    portAuthTable.setStatus("mandatory")
_PortAuthEntry_Object = MibTableRow
portAuthEntry = _PortAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1)
)
portAuthEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portAuthEntry.setStatus("mandatory")
_PortAuthEntryState_Type = EnabledStatus
_PortAuthEntryState_Object = MibTableColumn
portAuthEntryState = _PortAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 1),
    _PortAuthEntryState_Type()
)
portAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthEntryState.setStatus("mandatory")
_PortReAuthEntryState_Type = EnabledStatus
_PortReAuthEntryState_Object = MibTableColumn
portReAuthEntryState = _PortReAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 2),
    _PortReAuthEntryState_Type()
)
portReAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryState.setStatus("mandatory")
_PortReAuthEntryTimer_Type = Integer32
_PortReAuthEntryTimer_Object = MibTableColumn
portReAuthEntryTimer = _PortReAuthEntryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 3),
    _PortReAuthEntryTimer_Type()
)
portReAuthEntryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryTimer.setStatus("mandatory")
_PortAuthQuietPeriod_Type = Integer32
_PortAuthQuietPeriod_Object = MibTableColumn
portAuthQuietPeriod = _PortAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 4),
    _PortAuthQuietPeriod_Type()
)
portAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthQuietPeriod.setStatus("mandatory")
_PortAuthTxPeriod_Type = Integer32
_PortAuthTxPeriod_Object = MibTableColumn
portAuthTxPeriod = _PortAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 5),
    _PortAuthTxPeriod_Type()
)
portAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthTxPeriod.setStatus("mandatory")
_PortAuthSupplicantTimeout_Type = Integer32
_PortAuthSupplicantTimeout_Object = MibTableColumn
portAuthSupplicantTimeout = _PortAuthSupplicantTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 6),
    _PortAuthSupplicantTimeout_Type()
)
portAuthSupplicantTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthSupplicantTimeout.setStatus("mandatory")
_PortAuthMaxRequest_Type = Integer32
_PortAuthMaxRequest_Object = MibTableColumn
portAuthMaxRequest = _PortAuthMaxRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 7),
    _PortAuthMaxRequest_Type()
)
portAuthMaxRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthMaxRequest.setStatus("mandatory")
_PortAuthGuestVlanState_Type = EnabledStatus
_PortAuthGuestVlanState_Object = MibTableColumn
portAuthGuestVlanState = _PortAuthGuestVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 8),
    _PortAuthGuestVlanState_Type()
)
portAuthGuestVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthGuestVlanState.setStatus("mandatory")
_PortAuthGuestVlan_Type = Integer32
_PortAuthGuestVlan_Object = MibTableColumn
portAuthGuestVlan = _PortAuthGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 9),
    _PortAuthGuestVlan_Type()
)
portAuthGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthGuestVlan.setStatus("mandatory")
_PortAuthGuestVlanHostMode_Type = Integer32
_PortAuthGuestVlanHostMode_Object = MibTableColumn
portAuthGuestVlanHostMode = _PortAuthGuestVlanHostMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 10),
    _PortAuthGuestVlanHostMode_Type()
)
portAuthGuestVlanHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthGuestVlanHostMode.setStatus("mandatory")
_PortAuthGuestVlanHostModeMultiSecureNumber_Type = Integer32
_PortAuthGuestVlanHostModeMultiSecureNumber_Object = MibTableColumn
portAuthGuestVlanHostModeMultiSecureNumber = _PortAuthGuestVlanHostModeMultiSecureNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 8, 4, 1, 11),
    _PortAuthGuestVlanHostModeMultiSecureNumber_Type()
)
portAuthGuestVlanHostModeMultiSecureNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthGuestVlanHostModeMultiSecureNumber.setStatus("mandatory")
_HwMonitorInfo_ObjectIdentity = ObjectIdentity
hwMonitorInfo = _HwMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9)
)
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1)
)
tempEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "tempIndex"),
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
        *(("mac", 1),
          ("cpu", 2),
          ("phy", 3))
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
_TempCurValue_Type = Integer32
_TempCurValue_Object = MibTableColumn
tempCurValue = _TempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1, 2),
    _TempCurValue_Type()
)
tempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurValue.setStatus("current")
_TempMaxValue_Type = Integer32
_TempMaxValue_Object = MibTableColumn
tempMaxValue = _TempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1, 3),
    _TempMaxValue_Type()
)
tempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxValue.setStatus("current")
_TempMinValue_Type = Integer32
_TempMinValue_Object = MibTableColumn
tempMinValue = _TempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1, 4),
    _TempMinValue_Type()
)
tempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinValue.setStatus("current")
_TempHighThresh_Type = Integer32
_TempHighThresh_Object = MibTableColumn
tempHighThresh = _TempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1, 5),
    _TempHighThresh_Type()
)
tempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighThresh.setStatus("current")
_TempDescr_Type = DisplayString
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 2, 1, 6),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1)
)
voltageEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 2),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 3),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 4),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 5),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
_VoltageLowThresh_Type = Integer32
_VoltageLowThresh_Object = MibTableColumn
voltageLowThresh = _VoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 6),
    _VoltageLowThresh_Type()
)
voltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowThresh.setStatus("current")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 9, 3, 1, 7),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10)
)
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 1),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("mandatory")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 2),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("mandatory")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 3),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("mandatory")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("mandatory")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4, 1, 1),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("mandatory")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4, 1, 2),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("mandatory")
_SnmpTrapDestPort_Type = Integer32
_SnmpTrapDestPort_Object = MibTableColumn
snmpTrapDestPort = _SnmpTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4, 1, 3),
    _SnmpTrapDestPort_Type()
)
snmpTrapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestPort.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4, 1, 4),
    _SnmpTrapVersion_Type()
)
snmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVersion.setStatus("mandatory")
_SnmpTrapUserName_Type = DisplayString
_SnmpTrapUserName_Object = MibTableColumn
snmpTrapUserName = _SnmpTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 4, 1, 5),
    _SnmpTrapUserName_Type()
)
snmpTrapUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapUserName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 5),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("mandatory")
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6, 1)
)
snmpUserEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "snmpUserName"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")
_SnmpUserName_Type = DisplayString
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6, 1, 1),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6, 1, 2),
    _SnmpUserSecurityLevel_Type()
)
snmpUserSecurityLevel.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6, 1, 3),
    _SnmpUserAuthProtocol_Type()
)
snmpUserAuthProtocol.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6, 1, 4),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")
_SnmpUserGroup_Type = DisplayString
_SnmpUserGroup_Object = MibTableColumn
snmpUserGroup = _SnmpUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 6, 1, 5),
    _SnmpUserGroup_Type()
)
snmpUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserGroup.setStatus("current")
_SnmpTrapGroupTable_Object = MibTable
snmpTrapGroupTable = _SnmpTrapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7)
)
if mibBuilder.loadTexts:
    snmpTrapGroupTable.setStatus("mandatory")
_SnmpTrapGroupEntry_Object = MibTableRow
snmpTrapGroupEntry = _SnmpTrapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7, 1)
)
snmpTrapGroupEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapGroupEntry.setStatus("mandatory")


class _SnmpTrapSystemGroup_Type(Bits):
    """Custom type snmpTrapSystemGroup based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 0),
          ("warmStart", 1),
          ("temperature", 3),
          ("voltage", 4),
          ("reset", 5),
          ("timeSync", 6),
          ("intrusionlock", 7),
          ("externalalarm", 10),
          ("loopGuard", 13),
          ("errdisable", 14),
          ("dyinggasp", 15))
    )

_SnmpTrapSystemGroup_Type.__name__ = "Bits"
_SnmpTrapSystemGroup_Object = MibTableColumn
snmpTrapSystemGroup = _SnmpTrapSystemGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7, 1, 1),
    _SnmpTrapSystemGroup_Type()
)
snmpTrapSystemGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSystemGroup.setStatus("mandatory")


class _SnmpTrapInterfaceGroup_Type(Bits):
    """Custom type snmpTrapInterfaceGroup based on Bits"""
    namedValues = NamedValues(
        *(("linkup", 0),
          ("linkdown", 1),
          ("lldp", 3),
          ("transceiver-ddm", 4))
    )

_SnmpTrapInterfaceGroup_Type.__name__ = "Bits"
_SnmpTrapInterfaceGroup_Object = MibTableColumn
snmpTrapInterfaceGroup = _SnmpTrapInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7, 1, 2),
    _SnmpTrapInterfaceGroup_Type()
)
snmpTrapInterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapInterfaceGroup.setStatus("mandatory")


class _SnmpTrapAAAGroup_Type(Bits):
    """Custom type snmpTrapAAAGroup based on Bits"""
    namedValues = NamedValues(
        *(("authentication", 0),
          ("accounting", 1))
    )

_SnmpTrapAAAGroup_Type.__name__ = "Bits"
_SnmpTrapAAAGroup_Object = MibTableColumn
snmpTrapAAAGroup = _SnmpTrapAAAGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7, 1, 3),
    _SnmpTrapAAAGroup_Type()
)
snmpTrapAAAGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapAAAGroup.setStatus("mandatory")


class _SnmpTrapIPGroup_Type(Bits):
    """Custom type snmpTrapIPGroup based on Bits"""
    namedValues = NamedValues(
        *(("ping", 0),
          ("traceroute", 1))
    )

_SnmpTrapIPGroup_Type.__name__ = "Bits"
_SnmpTrapIPGroup_Object = MibTableColumn
snmpTrapIPGroup = _SnmpTrapIPGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7, 1, 4),
    _SnmpTrapIPGroup_Type()
)
snmpTrapIPGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapIPGroup.setStatus("mandatory")


class _SnmpTrapSwitchGroup_Type(Bits):
    """Custom type snmpTrapSwitchGroup based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("mactable", 1),
          ("rmon", 2),
          ("cfm", 3))
    )

_SnmpTrapSwitchGroup_Type.__name__ = "Bits"
_SnmpTrapSwitchGroup_Object = MibTableColumn
snmpTrapSwitchGroup = _SnmpTrapSwitchGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 10, 7, 1, 5),
    _SnmpTrapSwitchGroup_Type()
)
snmpTrapSwitchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSwitchGroup.setStatus("mandatory")
_DateTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeSetup = _DateTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 1),
    _DateTimeServerType_Type()
)
dateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerType.setStatus("mandatory")
_DateTimeServerIP_Type = IpAddress
_DateTimeServerIP_Object = MibScalar
dateTimeServerIP = _DateTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 2),
    _DateTimeServerIP_Type()
)
dateTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIP.setStatus("mandatory")
_DateTimeZone_Type = Integer32
_DateTimeZone_Object = MibScalar
dateTimeZone = _DateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 3),
    _DateTimeZone_Type()
)
dateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeZone.setStatus("mandatory")
_DateTimeNewDateYear_Type = Integer32
_DateTimeNewDateYear_Object = MibScalar
dateTimeNewDateYear = _DateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 4),
    _DateTimeNewDateYear_Type()
)
dateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setStatus("mandatory")
_DateTimeNewDateMonth_Type = Integer32
_DateTimeNewDateMonth_Object = MibScalar
dateTimeNewDateMonth = _DateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 5),
    _DateTimeNewDateMonth_Type()
)
dateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setStatus("mandatory")
_DateTimeNewDateDay_Type = Integer32
_DateTimeNewDateDay_Object = MibScalar
dateTimeNewDateDay = _DateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 6),
    _DateTimeNewDateDay_Type()
)
dateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setStatus("mandatory")
_DateTimeNewTimeHour_Type = Integer32
_DateTimeNewTimeHour_Object = MibScalar
dateTimeNewTimeHour = _DateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 7),
    _DateTimeNewTimeHour_Type()
)
dateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setStatus("mandatory")
_DateTimeNewTimeMinute_Type = Integer32
_DateTimeNewTimeMinute_Object = MibScalar
dateTimeNewTimeMinute = _DateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 8),
    _DateTimeNewTimeMinute_Type()
)
dateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setStatus("mandatory")
_DateTimeNewTimeSecond_Type = Integer32
_DateTimeNewTimeSecond_Object = MibScalar
dateTimeNewTimeSecond = _DateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 9),
    _DateTimeNewTimeSecond_Type()
)
dateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setStatus("mandatory")
_DateTimeDaylightSavingTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeDaylightSavingTimeSetup = _DateTimeDaylightSavingTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10)
)
_DaylightSavingTimeState_Type = EnabledStatus
_DaylightSavingTimeState_Object = MibScalar
daylightSavingTimeState = _DaylightSavingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 1),
    _DaylightSavingTimeState_Type()
)
daylightSavingTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 2),
    _DaylightSavingTimeStartDateWeek_Type()
)
daylightSavingTimeStartDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateWeek.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 3),
    _DaylightSavingTimeStartDateDay_Type()
)
daylightSavingTimeStartDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateDay.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 4),
    _DaylightSavingTimeStartDateMonth_Type()
)
daylightSavingTimeStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateMonth.setStatus("mandatory")
_DaylightSavingTimeStartDateHour_Type = Integer32
_DaylightSavingTimeStartDateHour_Object = MibScalar
daylightSavingTimeStartDateHour = _DaylightSavingTimeStartDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 5),
    _DaylightSavingTimeStartDateHour_Type()
)
daylightSavingTimeStartDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateHour.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 6),
    _DaylightSavingTimeEndDateWeek_Type()
)
daylightSavingTimeEndDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateWeek.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 7),
    _DaylightSavingTimeEndDateDay_Type()
)
daylightSavingTimeEndDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateDay.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 8),
    _DaylightSavingTimeEndDateMonth_Type()
)
daylightSavingTimeEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateMonth.setStatus("mandatory")
_DaylightSavingTimeEndDateHour_Type = Integer32
_DaylightSavingTimeEndDateHour_Object = MibScalar
daylightSavingTimeEndDateHour = _DaylightSavingTimeEndDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 10, 9),
    _DaylightSavingTimeEndDateHour_Type()
)
daylightSavingTimeEndDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateHour.setStatus("mandatory")
_DateTimeServerAddr1_Type = DisplayString
_DateTimeServerAddr1_Object = MibScalar
dateTimeServerAddr1 = _DateTimeServerAddr1_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 11),
    _DateTimeServerAddr1_Type()
)
dateTimeServerAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerAddr1.setStatus("mandatory")
_DateTimeServerAddr2_Type = DisplayString
_DateTimeServerAddr2_Object = MibScalar
dateTimeServerAddr2 = _DateTimeServerAddr2_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 12),
    _DateTimeServerAddr2_Type()
)
dateTimeServerAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerAddr2.setStatus("mandatory")
_DateTimeServerAddr3_Type = DisplayString
_DateTimeServerAddr3_Object = MibScalar
dateTimeServerAddr3 = _DateTimeServerAddr3_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 11, 13),
    _DateTimeServerAddr3_Type()
)
dateTimeServerAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerAddr3.setStatus("mandatory")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 1),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 2),
    _SysMgmtBootupConfig_Type()
)
sysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupConfig.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 3),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("mandatory")


class _SysMgmtDefaultConfig_Type(Integer32):
    """Custom type sysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reset-to-default", 1))
    )


_SysMgmtDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtDefaultConfig_Object = MibScalar
sysMgmtDefaultConfig = _SysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 4),
    _SysMgmtDefaultConfig_Type()
)
sysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfig.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 5),
    _SysMgmtLastActionStatus_Type()
)
sysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 6),
    _SysMgmtSystemStatus_Type()
)
sysMgmtSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtSystemStatus.setStatus("mandatory")
_SysMgmtCPUUsage_Type = Integer32
_SysMgmtCPUUsage_Object = MibScalar
sysMgmtCPUUsage = _SysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 7),
    _SysMgmtCPUUsage_Type()
)
sysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 8),
    _SysMgmtBootupImage_Type()
)
sysMgmtBootupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupImage.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 9),
    _SysMgmtCounterReset_Type()
)
sysMgmtCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtCounterReset.setStatus("mandatory")
_SysMgmtTftpServiceSetup_ObjectIdentity = ObjectIdentity
sysMgmtTftpServiceSetup = _SysMgmtTftpServiceSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10)
)
_SysMgmtTftpServerIp_Type = IpAddress
_SysMgmtTftpServerIp_Object = MibScalar
sysMgmtTftpServerIp = _SysMgmtTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10, 1),
    _SysMgmtTftpServerIp_Type()
)
sysMgmtTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpServerIp.setStatus("mandatory")
_SysMgmtTftpRemoteFileName_Type = DisplayString
_SysMgmtTftpRemoteFileName_Object = MibScalar
sysMgmtTftpRemoteFileName = _SysMgmtTftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10, 2),
    _SysMgmtTftpRemoteFileName_Type()
)
sysMgmtTftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpRemoteFileName.setStatus("mandatory")


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
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtTftpConfigIndex_Type.__name__ = "Integer32"
_SysMgmtTftpConfigIndex_Object = MibScalar
sysMgmtTftpConfigIndex = _SysMgmtTftpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10, 3),
    _SysMgmtTftpConfigIndex_Type()
)
sysMgmtTftpConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpConfigIndex.setStatus("mandatory")


class _SysMgmtTftpAction_Type(Integer32):
    """Custom type sysMgmtTftpAction based on Integer32"""
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
          ("backup-config", 1),
          ("restore-config", 2),
          ("merge-config", 3))
    )


_SysMgmtTftpAction_Type.__name__ = "Integer32"
_SysMgmtTftpAction_Object = MibScalar
sysMgmtTftpAction = _SysMgmtTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10, 4),
    _SysMgmtTftpAction_Type()
)
sysMgmtTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpAction.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10, 5),
    _SysMgmtTftpActionStatus_Type()
)
sysMgmtTftpActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtTftpActionStatus.setStatus("mandatory")


class _SysMgmtTftpActionPrivilege13_Type(Integer32):
    """Custom type sysMgmtTftpActionPrivilege13 based on Integer32"""
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
          ("backup-config", 1),
          ("restore-config", 2),
          ("merge-config", 3))
    )


_SysMgmtTftpActionPrivilege13_Type.__name__ = "Integer32"
_SysMgmtTftpActionPrivilege13_Object = MibScalar
sysMgmtTftpActionPrivilege13 = _SysMgmtTftpActionPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 10, 113),
    _SysMgmtTftpActionPrivilege13_Type()
)
sysMgmtTftpActionPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtTftpActionPrivilege13.setStatus("mandatory")


class _SysMgmtConfigSavePrivilege13_Type(Integer32):
    """Custom type sysMgmtConfigSavePrivilege13 based on Integer32"""
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


_SysMgmtConfigSavePrivilege13_Type.__name__ = "Integer32"
_SysMgmtConfigSavePrivilege13_Object = MibScalar
sysMgmtConfigSavePrivilege13 = _SysMgmtConfigSavePrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 113),
    _SysMgmtConfigSavePrivilege13_Type()
)
sysMgmtConfigSavePrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSavePrivilege13.setStatus("mandatory")


class _SysMgmtDefaultConfigPrivilege13_Type(Integer32):
    """Custom type sysMgmtDefaultConfigPrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reset-to-default", 1))
    )


_SysMgmtDefaultConfigPrivilege13_Type.__name__ = "Integer32"
_SysMgmtDefaultConfigPrivilege13_Object = MibScalar
sysMgmtDefaultConfigPrivilege13 = _SysMgmtDefaultConfigPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 12, 213),
    _SysMgmtDefaultConfigPrivilege13_Type()
)
sysMgmtDefaultConfigPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfigPrivilege13.setStatus("mandatory")
_Layer2Setup_ObjectIdentity = ObjectIdentity
layer2Setup = _Layer2Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 1),
    _VlanTypeSetup_Type()
)
vlanTypeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTypeSetup.setStatus("mandatory")
_IgmpSnoopingStateSetup_Type = EnabledStatus
_IgmpSnoopingStateSetup_Object = MibScalar
igmpSnoopingStateSetup = _IgmpSnoopingStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 2),
    _IgmpSnoopingStateSetup_Type()
)
igmpSnoopingStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingStateSetup.setStatus("mandatory")
_TagVlanPortIsolationState_Type = EnabledStatus
_TagVlanPortIsolationState_Object = MibScalar
tagVlanPortIsolationState = _TagVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 3),
    _TagVlanPortIsolationState_Type()
)
tagVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanPortIsolationState.setStatus("mandatory")
_StpState_Type = EnabledStatus
_StpState_Object = MibScalar
stpState = _StpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 4),
    _StpState_Type()
)
stpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpState.setStatus("mandatory")
_IgmpFilteringStateSetup_Type = EnabledStatus
_IgmpFilteringStateSetup_Object = MibScalar
igmpFilteringStateSetup = _IgmpFilteringStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 6),
    _IgmpFilteringStateSetup_Type()
)
igmpFilteringStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpFilteringStateSetup.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 7),
    _UnknownMulticastFrameForwarding_Type()
)
unknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastFrameForwarding.setStatus("mandatory")
_MulticastGrpHostTimeout_Type = Integer32
_MulticastGrpHostTimeout_Object = MibScalar
multicastGrpHostTimeout = _MulticastGrpHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 8),
    _MulticastGrpHostTimeout_Type()
)
multicastGrpHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastGrpHostTimeout.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 9),
    _ReservedMulticastFrameForwarding_Type()
)
reservedMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reservedMulticastFrameForwarding.setStatus("mandatory")
_Igmpsnp8021pPriority_Type = Integer32
_Igmpsnp8021pPriority_Object = MibScalar
igmpsnp8021pPriority = _Igmpsnp8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 10),
    _Igmpsnp8021pPriority_Type()
)
igmpsnp8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnp8021pPriority.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 11),
    _IgmpsnpVlanMode_Type()
)
igmpsnpVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanMode.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 12),
    _StpMode_Type()
)
stpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMode.setStatus("mandatory")
_IgmpsnpVlanTable_Object = MibTable
igmpsnpVlanTable = _IgmpsnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 13)
)
if mibBuilder.loadTexts:
    igmpsnpVlanTable.setStatus("mandatory")
_IgmpsnpVlanEntry_Object = MibTableRow
igmpsnpVlanEntry = _IgmpsnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 13, 1)
)
igmpsnpVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "igmpsnpVid"),
)
if mibBuilder.loadTexts:
    igmpsnpVlanEntry.setStatus("mandatory")
_IgmpsnpVid_Type = Integer32
_IgmpsnpVid_Object = MibTableColumn
igmpsnpVid = _IgmpsnpVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 13, 1, 1),
    _IgmpsnpVid_Type()
)
igmpsnpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsnpVid.setStatus("mandatory")
_IgmpsnpVlanName_Type = DisplayString
_IgmpsnpVlanName_Object = MibTableColumn
igmpsnpVlanName = _IgmpsnpVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 13, 1, 2),
    _IgmpsnpVlanName_Type()
)
igmpsnpVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanName.setStatus("mandatory")
_IgmpsnpVlanRowStatus_Type = RowStatus
_IgmpsnpVlanRowStatus_Object = MibTableColumn
igmpsnpVlanRowStatus = _IgmpsnpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 13, 1, 3),
    _IgmpsnpVlanRowStatus_Type()
)
igmpsnpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpsnpVlanRowStatus.setStatus("mandatory")
_IgmpsnpQuerierMode_Type = EnabledStatus
_IgmpsnpQuerierMode_Object = MibScalar
igmpsnpQuerierMode = _IgmpsnpQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 14),
    _IgmpsnpQuerierMode_Type()
)
igmpsnpQuerierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpQuerierMode.setStatus("mandatory")
_EthernetCfmStateSetup_Type = EnabledStatus
_EthernetCfmStateSetup_Object = MibScalar
ethernetCfmStateSetup = _EthernetCfmStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 15),
    _EthernetCfmStateSetup_Type()
)
ethernetCfmStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetCfmStateSetup.setStatus("mandatory")
_LldpStateSetup_Type = EnabledStatus
_LldpStateSetup_Object = MibScalar
lldpStateSetup = _LldpStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 16),
    _LldpStateSetup_Type()
)
lldpStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStateSetup.setStatus("mandatory")
_IgmpSnpReportProxySetup_Type = EnabledStatus
_IgmpSnpReportProxySetup_Object = MibScalar
igmpSnpReportProxySetup = _IgmpSnpReportProxySetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 17),
    _IgmpSnpReportProxySetup_Type()
)
igmpSnpReportProxySetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnpReportProxySetup.setStatus("mandatory")
_SmartIsolationState_Type = EnabledStatus
_SmartIsolationState_Object = MibScalar
smartIsolationState = _SmartIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 13, 18),
    _SmartIsolationState_Type()
)
smartIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIsolationState.setStatus("mandatory")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14)
)
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibScalar
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("mandatory")
_InbandIpSetup_ObjectIdentity = ObjectIdentity
inbandIpSetup = _InbandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 3)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 3, 1),
    _InbandIpType_Type()
)
inbandIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpType.setStatus("mandatory")
_InbandVid_Type = Integer32
_InbandVid_Object = MibScalar
inbandVid = _InbandVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 3, 2),
    _InbandVid_Type()
)
inbandVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandVid.setStatus("mandatory")
_InbandStaticIp_Type = IpAddress
_InbandStaticIp_Object = MibScalar
inbandStaticIp = _InbandStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 3, 3),
    _InbandStaticIp_Type()
)
inbandStaticIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticIp.setStatus("mandatory")
_InbandStaticSubnetMask_Type = IpAddress
_InbandStaticSubnetMask_Object = MibScalar
inbandStaticSubnetMask = _InbandStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 3, 4),
    _InbandStaticSubnetMask_Type()
)
inbandStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticSubnetMask.setStatus("mandatory")
_InbandStaticGateway_Type = IpAddress
_InbandStaticGateway_Object = MibScalar
inbandStaticGateway = _InbandStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 3, 5),
    _InbandStaticGateway_Type()
)
inbandStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticGateway.setStatus("mandatory")
_MaxNumOfInbandIp_Type = Integer32
_MaxNumOfInbandIp_Object = MibScalar
maxNumOfInbandIp = _MaxNumOfInbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 4),
    _MaxNumOfInbandIp_Type()
)
maxNumOfInbandIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfInbandIp.setStatus("mandatory")
_InbandIpTable_Object = MibTable
inbandIpTable = _InbandIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5)
)
if mibBuilder.loadTexts:
    inbandIpTable.setStatus("mandatory")
_InbandIpEntry_Object = MibTableRow
inbandIpEntry = _InbandIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1)
)
inbandIpEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "inbandEntryIp"),
    (0, "ZYXEL-MES3500-10-MIB", "inbandEntryVid"),
)
if mibBuilder.loadTexts:
    inbandIpEntry.setStatus("mandatory")
_InbandEntryIp_Type = IpAddress
_InbandEntryIp_Object = MibTableColumn
inbandEntryIp = _InbandEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1, 1),
    _InbandEntryIp_Type()
)
inbandEntryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbandEntryIp.setStatus("mandatory")
_InbandEntrySubnetMask_Type = IpAddress
_InbandEntrySubnetMask_Object = MibTableColumn
inbandEntrySubnetMask = _InbandEntrySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1, 2),
    _InbandEntrySubnetMask_Type()
)
inbandEntrySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntrySubnetMask.setStatus("mandatory")
_InbandEntryGateway_Type = IpAddress
_InbandEntryGateway_Object = MibTableColumn
inbandEntryGateway = _InbandEntryGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1, 3),
    _InbandEntryGateway_Type()
)
inbandEntryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryGateway.setStatus("mandatory")
_InbandEntryVid_Type = Integer32
_InbandEntryVid_Object = MibTableColumn
inbandEntryVid = _InbandEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1, 4),
    _InbandEntryVid_Type()
)
inbandEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbandEntryVid.setStatus("mandatory")
_InbandEntryManageable_Type = EnabledStatus
_InbandEntryManageable_Object = MibTableColumn
inbandEntryManageable = _InbandEntryManageable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1, 5),
    _InbandEntryManageable_Type()
)
inbandEntryManageable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryManageable.setStatus("mandatory")
_InbandEntryRowStatus_Type = RowStatus
_InbandEntryRowStatus_Object = MibTableColumn
inbandEntryRowStatus = _InbandEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 14, 5, 1, 6),
    _InbandEntryRowStatus_Type()
)
inbandEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inbandEntryRowStatus.setStatus("mandatory")
_FilterSetup_ObjectIdentity = ObjectIdentity
filterSetup = _FilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "filterMacAddr"),
    (0, "ZYXEL-MES3500-10-MIB", "filterVid"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterName_Type = DisplayString
_FilterName_Object = MibTableColumn
filterName = _FilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1, 1, 1),
    _FilterName_Type()
)
filterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1, 1, 2),
    _FilterActionState_Type()
)
filterActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActionState.setStatus("mandatory")
_FilterMacAddr_Type = MacAddress
_FilterMacAddr_Object = MibTableColumn
filterMacAddr = _FilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1, 1, 3),
    _FilterMacAddr_Type()
)
filterMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMacAddr.setStatus("mandatory")
_FilterVid_Type = Integer32
_FilterVid_Object = MibTableColumn
filterVid = _FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1, 1, 4),
    _FilterVid_Type()
)
filterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterVid.setStatus("mandatory")
_FilterRowStatus_Type = RowStatus
_FilterRowStatus_Object = MibTableColumn
filterRowStatus = _FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 15, 1, 1, 5),
    _FilterRowStatus_Type()
)
filterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRowStatus.setStatus("mandatory")
_MirrorSetup_ObjectIdentity = ObjectIdentity
mirrorSetup = _MirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16)
)
_MirrorState_Type = EnabledStatus
_MirrorState_Object = MibScalar
mirrorState = _MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16, 1),
    _MirrorState_Type()
)
mirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorState.setStatus("mandatory")
_MirrorMonitorPort_Type = Integer32
_MirrorMonitorPort_Object = MibScalar
mirrorMonitorPort = _MirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16, 2),
    _MirrorMonitorPort_Type()
)
mirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMonitorPort.setStatus("mandatory")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16, 3)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("mandatory")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16, 3, 1)
)
mirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("mandatory")
_MirrorMirroredState_Type = EnabledStatus
_MirrorMirroredState_Object = MibTableColumn
mirrorMirroredState = _MirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16, 3, 1, 1),
    _MirrorMirroredState_Type()
)
mirrorMirroredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroredState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 16, 3, 1, 2),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("mandatory")
_AggrSetup_ObjectIdentity = ObjectIdentity
aggrSetup = _AggrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17)
)
_AggrState_Type = EnabledStatus
_AggrState_Object = MibScalar
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 1),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrState.setStatus("mandatory")
_AggrSystemPriority_Type = Integer32
_AggrSystemPriority_Object = MibScalar
aggrSystemPriority = _AggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 2),
    _AggrSystemPriority_Type()
)
aggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrSystemPriority.setStatus("mandatory")
_AggrGroupTable_Object = MibTable
aggrGroupTable = _AggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 3)
)
if mibBuilder.loadTexts:
    aggrGroupTable.setStatus("mandatory")
_AggrGroupEntry_Object = MibTableRow
aggrGroupEntry = _AggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 3, 1)
)
aggrGroupEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrGroupEntry.setStatus("mandatory")
_AggrGroupIndex_Type = Integer32
_AggrGroupIndex_Object = MibTableColumn
aggrGroupIndex = _AggrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 3, 1, 1),
    _AggrGroupIndex_Type()
)
aggrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrGroupIndex.setStatus("mandatory")
_AggrGroupState_Type = EnabledStatus
_AggrGroupState_Object = MibTableColumn
aggrGroupState = _AggrGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 3, 1, 2),
    _AggrGroupState_Type()
)
aggrGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupState.setStatus("mandatory")
_AggrGroupDynamicState_Type = EnabledStatus
_AggrGroupDynamicState_Object = MibTableColumn
aggrGroupDynamicState = _AggrGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 3, 1, 3),
    _AggrGroupDynamicState_Type()
)
aggrGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupDynamicState.setStatus("mandatory")


class _AggrGroupCriteria_Type(Integer32):
    """Custom type aggrGroupCriteria based on Integer32"""
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
        *(("src-mac", 1),
          ("dst-mac", 2),
          ("src-dst-mac", 3),
          ("src-ip", 4),
          ("dst-ip", 5),
          ("src-dst-ip", 6))
    )


_AggrGroupCriteria_Type.__name__ = "Integer32"
_AggrGroupCriteria_Object = MibTableColumn
aggrGroupCriteria = _AggrGroupCriteria_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 3, 1, 4),
    _AggrGroupCriteria_Type()
)
aggrGroupCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupCriteria.setStatus("mandatory")
_AggrPortTable_Object = MibTable
aggrPortTable = _AggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 4)
)
if mibBuilder.loadTexts:
    aggrPortTable.setStatus("mandatory")
_AggrPortEntry_Object = MibTableRow
aggrPortEntry = _AggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 4, 1)
)
aggrPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    aggrPortEntry.setStatus("mandatory")


class _AggrPortGroup_Type(Integer32):
    """Custom type aggrPortGroup based on Integer32"""
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
          ("t1", 1),
          ("t2", 2),
          ("t3", 3),
          ("t4", 4),
          ("t5", 5),
          ("t6", 6),
          ("t7", 7),
          ("t8", 8))
    )


_AggrPortGroup_Type.__name__ = "Integer32"
_AggrPortGroup_Object = MibTableColumn
aggrPortGroup = _AggrPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 4, 1, 1),
    _AggrPortGroup_Type()
)
aggrPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortGroup.setStatus("mandatory")
_AggrPortDynamicStateTimeout_Type = Integer32
_AggrPortDynamicStateTimeout_Object = MibTableColumn
aggrPortDynamicStateTimeout = _AggrPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 17, 4, 1, 2),
    _AggrPortDynamicStateTimeout_Type()
)
aggrPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortDynamicStateTimeout.setStatus("mandatory")
_AccessCtlSetup_ObjectIdentity = ObjectIdentity
accessCtlSetup = _AccessCtlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18)
)
_AccessCtlTable_Object = MibTable
accessCtlTable = _AccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 1)
)
if mibBuilder.loadTexts:
    accessCtlTable.setStatus("mandatory")
_AccessCtlEntry_Object = MibTableRow
accessCtlEntry = _AccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 1, 1)
)
accessCtlEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "accessCtlService"),
)
if mibBuilder.loadTexts:
    accessCtlEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 1, 1, 1),
    _AccessCtlService_Type()
)
accessCtlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtlService.setStatus("mandatory")
_AccessCtlEnable_Type = EnabledStatus
_AccessCtlEnable_Object = MibTableColumn
accessCtlEnable = _AccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 1, 1, 2),
    _AccessCtlEnable_Type()
)
accessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlEnable.setStatus("mandatory")
_AccessCtlServicePort_Type = Integer32
_AccessCtlServicePort_Object = MibTableColumn
accessCtlServicePort = _AccessCtlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 1, 1, 3),
    _AccessCtlServicePort_Type()
)
accessCtlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlServicePort.setStatus("mandatory")
_AccessCtlTimeout_Type = Integer32
_AccessCtlTimeout_Object = MibTableColumn
accessCtlTimeout = _AccessCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 1, 1, 4),
    _AccessCtlTimeout_Type()
)
accessCtlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlTimeout.setStatus("mandatory")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("mandatory")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("mandatory")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("mandatory")
_SecuredClientEnable_Type = EnabledStatus
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2, 1, 2),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("mandatory")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2, 1, 3),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("mandatory")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2, 1, 4),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 18, 2, 1, 5),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("mandatory")
_QueuingMethodSetup_ObjectIdentity = ObjectIdentity
queuingMethodSetup = _QueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19)
)
_PortQueuingMethodTable_Object = MibTable
portQueuingMethodTable = _PortQueuingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 1)
)
if mibBuilder.loadTexts:
    portQueuingMethodTable.setStatus("mandatory")
_PortQueuingMethodEntry_Object = MibTableRow
portQueuingMethodEntry = _PortQueuingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 1, 1)
)
portQueuingMethodEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-MES3500-10-MIB", "portQueuingMethodQueue"),
)
if mibBuilder.loadTexts:
    portQueuingMethodEntry.setStatus("mandatory")
_PortQueuingMethodQueue_Type = Integer32
_PortQueuingMethodQueue_Object = MibTableColumn
portQueuingMethodQueue = _PortQueuingMethodQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 1, 1, 1),
    _PortQueuingMethodQueue_Type()
)
portQueuingMethodQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portQueuingMethodQueue.setStatus("mandatory")
_PortQueuingMethodWeight_Type = Integer32
_PortQueuingMethodWeight_Object = MibTableColumn
portQueuingMethodWeight = _PortQueuingMethodWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 1, 1, 2),
    _PortQueuingMethodWeight_Type()
)
portQueuingMethodWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodWeight.setStatus("mandatory")


class _PortQueuingMethodMode_Type(Integer32):
    """Custom type portQueuingMethodMode based on Integer32"""
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


_PortQueuingMethodMode_Type.__name__ = "Integer32"
_PortQueuingMethodMode_Object = MibTableColumn
portQueuingMethodMode = _PortQueuingMethodMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 1, 1, 3),
    _PortQueuingMethodMode_Type()
)
portQueuingMethodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodMode.setStatus("mandatory")
_PortQueuingMethodHybridSpqTable_Object = MibTable
portQueuingMethodHybridSpqTable = _PortQueuingMethodHybridSpqTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 2)
)
if mibBuilder.loadTexts:
    portQueuingMethodHybridSpqTable.setStatus("mandatory")
_PortQueuingMethodHybridSpqEntry_Object = MibTableRow
portQueuingMethodHybridSpqEntry = _PortQueuingMethodHybridSpqEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 2, 1)
)
portQueuingMethodHybridSpqEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portQueuingMethodHybridSpqEntry.setStatus("mandatory")


class _PortQueuingMethodHybridSpq_Type(Integer32):
    """Custom type portQueuingMethodHybridSpq based on Integer32"""
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


_PortQueuingMethodHybridSpq_Type.__name__ = "Integer32"
_PortQueuingMethodHybridSpq_Object = MibTableColumn
portQueuingMethodHybridSpq = _PortQueuingMethodHybridSpq_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 19, 2, 1, 1),
    _PortQueuingMethodHybridSpq_Type()
)
portQueuingMethodHybridSpq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodHybridSpq.setStatus("mandatory")
_DhcpSetup_ObjectIdentity = ObjectIdentity
dhcpSetup = _DhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20)
)
_GlobalDhcpRelay_ObjectIdentity = ObjectIdentity
globalDhcpRelay = _GlobalDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1)
)
_GlobalDhcpRelayEnable_Type = EnabledStatus
_GlobalDhcpRelayEnable_Object = MibScalar
globalDhcpRelayEnable = _GlobalDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 1),
    _GlobalDhcpRelayEnable_Type()
)
globalDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayEnable.setStatus("mandatory")
_MaxNumberOfGlobalDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfGlobalDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfGlobalDhcpRelayRemoteServer = _MaxNumberOfGlobalDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 5),
    _MaxNumberOfGlobalDhcpRelayRemoteServer_Type()
)
maxNumberOfGlobalDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfGlobalDhcpRelayRemoteServer.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerTable_Object = MibTable
globalDhcpRelayRemoteServerTable = _GlobalDhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 6)
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerTable.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerEntry_Object = MibTableRow
globalDhcpRelayRemoteServerEntry = _GlobalDhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 6, 1)
)
globalDhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "globalDhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerEntry.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerIp_Type = IpAddress
_GlobalDhcpRelayRemoteServerIp_Object = MibTableColumn
globalDhcpRelayRemoteServerIp = _GlobalDhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 6, 1, 1),
    _GlobalDhcpRelayRemoteServerIp_Type()
)
globalDhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerIp.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerRowStatus_Type = RowStatus
_GlobalDhcpRelayRemoteServerRowStatus_Object = MibTableColumn
globalDhcpRelayRemoteServerRowStatus = _GlobalDhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 6, 1, 2),
    _GlobalDhcpRelayRemoteServerRowStatus_Type()
)
globalDhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerRowStatus.setStatus("mandatory")
_GlobalDhcpRelayOption82Profile_Type = DisplayString
_GlobalDhcpRelayOption82Profile_Object = MibScalar
globalDhcpRelayOption82Profile = _GlobalDhcpRelayOption82Profile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 7),
    _GlobalDhcpRelayOption82Profile_Type()
)
globalDhcpRelayOption82Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayOption82Profile.setStatus("mandatory")
_GlobalDhcpRelayOption82PortTable_Object = MibTable
globalDhcpRelayOption82PortTable = _GlobalDhcpRelayOption82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 8)
)
if mibBuilder.loadTexts:
    globalDhcpRelayOption82PortTable.setStatus("current")
_GlobalDhcpRelayOption82PortEntry_Object = MibTableRow
globalDhcpRelayOption82PortEntry = _GlobalDhcpRelayOption82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 8, 1)
)
globalDhcpRelayOption82PortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    globalDhcpRelayOption82PortEntry.setStatus("current")
_GlobalDhcpRelayOption82PortProfile_Type = DisplayString
_GlobalDhcpRelayOption82PortProfile_Object = MibTableColumn
globalDhcpRelayOption82PortProfile = _GlobalDhcpRelayOption82PortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 1, 8, 1, 1),
    _GlobalDhcpRelayOption82PortProfile_Type()
)
globalDhcpRelayOption82PortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    globalDhcpRelayOption82PortProfile.setStatus("current")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2)
)
_DhcpRelayInfoData_Type = DisplayString
_DhcpRelayInfoData_Object = MibScalar
dhcpRelayInfoData = _DhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 1),
    _DhcpRelayInfoData_Type()
)
dhcpRelayInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayInfoData.setStatus("mandatory")
_MaxNumberOfDhcpRelay_Type = Integer32
_MaxNumberOfDhcpRelay_Object = MibScalar
maxNumberOfDhcpRelay = _MaxNumberOfDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 2),
    _MaxNumberOfDhcpRelay_Type()
)
maxNumberOfDhcpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelay.setStatus("mandatory")
_MaxNumberOfDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfDhcpRelayRemoteServer = _MaxNumberOfDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 3),
    _MaxNumberOfDhcpRelayRemoteServer_Type()
)
maxNumberOfDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelayRemoteServer.setStatus("mandatory")
_DhcpRelayTable_Object = MibTable
dhcpRelayTable = _DhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayTable.setStatus("mandatory")
_DhcpRelayEntry_Object = MibTableRow
dhcpRelayEntry = _DhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 4, 1)
)
dhcpRelayEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpRelayVid"),
)
if mibBuilder.loadTexts:
    dhcpRelayEntry.setStatus("mandatory")
_DhcpRelayOption82Profile_Type = DisplayString
_DhcpRelayOption82Profile_Object = MibTableColumn
dhcpRelayOption82Profile = _DhcpRelayOption82Profile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 4, 1, 3),
    _DhcpRelayOption82Profile_Type()
)
dhcpRelayOption82Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Profile.setStatus("mandatory")
_DhcpRelayRemoteServerTable_Object = MibTable
dhcpRelayRemoteServerTable = _DhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 5)
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerTable.setStatus("mandatory")
_DhcpRelayRemoteServerEntry_Object = MibTableRow
dhcpRelayRemoteServerEntry = _DhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 5, 1)
)
dhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpRelayVid"),
    (0, "ZYXEL-MES3500-10-MIB", "dhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerEntry.setStatus("mandatory")
_DhcpRelayVid_Type = Integer32
_DhcpRelayVid_Object = MibTableColumn
dhcpRelayVid = _DhcpRelayVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 5, 1, 1),
    _DhcpRelayVid_Type()
)
dhcpRelayVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVid.setStatus("mandatory")
_DhcpRelayRemoteServerIp_Type = IpAddress
_DhcpRelayRemoteServerIp_Object = MibTableColumn
dhcpRelayRemoteServerIp = _DhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 5, 1, 2),
    _DhcpRelayRemoteServerIp_Type()
)
dhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerIp.setStatus("mandatory")
_DhcpRelayRemoteServerRowStatus_Type = RowStatus
_DhcpRelayRemoteServerRowStatus_Object = MibTableColumn
dhcpRelayRemoteServerRowStatus = _DhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 5, 1, 3),
    _DhcpRelayRemoteServerRowStatus_Type()
)
dhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerRowStatus.setStatus("mandatory")
_DhcpRelayOption82VlanPortTable_Object = MibTable
dhcpRelayOption82VlanPortTable = _DhcpRelayOption82VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 6)
)
if mibBuilder.loadTexts:
    dhcpRelayOption82VlanPortTable.setStatus("current")
_DhcpRelayOption82VlanPortEntry_Object = MibTableRow
dhcpRelayOption82VlanPortEntry = _DhcpRelayOption82VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 6, 1)
)
dhcpRelayOption82VlanPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpRelayVid"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dhcpRelayOption82VlanPortEntry.setStatus("current")
_DhcpRelayOption82VlanPortProfile_Type = DisplayString
_DhcpRelayOption82VlanPortProfile_Object = MibTableColumn
dhcpRelayOption82VlanPortProfile = _DhcpRelayOption82VlanPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 2, 6, 1, 1),
    _DhcpRelayOption82VlanPortProfile_Type()
)
dhcpRelayOption82VlanPortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayOption82VlanPortProfile.setStatus("current")
_DhcpOption82ProfileTable_Object = MibTable
dhcpOption82ProfileTable = _DhcpOption82ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4)
)
if mibBuilder.loadTexts:
    dhcpOption82ProfileTable.setStatus("mandatory")
_DhcpOption82ProfileEntry_Object = MibTableRow
dhcpOption82ProfileEntry = _DhcpOption82ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1)
)
dhcpOption82ProfileEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpOption82ProfileName"),
)
if mibBuilder.loadTexts:
    dhcpOption82ProfileEntry.setStatus("mandatory")
_DhcpOption82ProfileName_Type = DisplayString
_DhcpOption82ProfileName_Object = MibTableColumn
dhcpOption82ProfileName = _DhcpOption82ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 1),
    _DhcpOption82ProfileName_Type()
)
dhcpOption82ProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOption82ProfileName.setStatus("mandatory")
_DhcpOption82ProfileCircuitIDEnable_Type = EnabledStatus
_DhcpOption82ProfileCircuitIDEnable_Object = MibTableColumn
dhcpOption82ProfileCircuitIDEnable = _DhcpOption82ProfileCircuitIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 2),
    _DhcpOption82ProfileCircuitIDEnable_Type()
)
dhcpOption82ProfileCircuitIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileCircuitIDEnable.setStatus("mandatory")
_DhcpOption82ProfileCircuitIDSlotPort_Type = EnabledStatus
_DhcpOption82ProfileCircuitIDSlotPort_Object = MibTableColumn
dhcpOption82ProfileCircuitIDSlotPort = _DhcpOption82ProfileCircuitIDSlotPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 3),
    _DhcpOption82ProfileCircuitIDSlotPort_Type()
)
dhcpOption82ProfileCircuitIDSlotPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileCircuitIDSlotPort.setStatus("mandatory")
_DhcpOption82ProfileCircuitIDVlan_Type = EnabledStatus
_DhcpOption82ProfileCircuitIDVlan_Object = MibTableColumn
dhcpOption82ProfileCircuitIDVlan = _DhcpOption82ProfileCircuitIDVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 4),
    _DhcpOption82ProfileCircuitIDVlan_Type()
)
dhcpOption82ProfileCircuitIDVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileCircuitIDVlan.setStatus("mandatory")
_DhcpOption82ProfileCircuitIDHostname_Type = EnabledStatus
_DhcpOption82ProfileCircuitIDHostname_Object = MibTableColumn
dhcpOption82ProfileCircuitIDHostname = _DhcpOption82ProfileCircuitIDHostname_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 5),
    _DhcpOption82ProfileCircuitIDHostname_Type()
)
dhcpOption82ProfileCircuitIDHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileCircuitIDHostname.setStatus("mandatory")
_DhcpOption82ProfileCircuitIDString_Type = DisplayString
_DhcpOption82ProfileCircuitIDString_Object = MibTableColumn
dhcpOption82ProfileCircuitIDString = _DhcpOption82ProfileCircuitIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 6),
    _DhcpOption82ProfileCircuitIDString_Type()
)
dhcpOption82ProfileCircuitIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileCircuitIDString.setStatus("mandatory")
_DhcpOption82ProfileRemoteIDEnable_Type = EnabledStatus
_DhcpOption82ProfileRemoteIDEnable_Object = MibTableColumn
dhcpOption82ProfileRemoteIDEnable = _DhcpOption82ProfileRemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 7),
    _DhcpOption82ProfileRemoteIDEnable_Type()
)
dhcpOption82ProfileRemoteIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileRemoteIDEnable.setStatus("mandatory")
_DhcpOption82ProfileRemoteIDMAC_Type = EnabledStatus
_DhcpOption82ProfileRemoteIDMAC_Object = MibTableColumn
dhcpOption82ProfileRemoteIDMAC = _DhcpOption82ProfileRemoteIDMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 8),
    _DhcpOption82ProfileRemoteIDMAC_Type()
)
dhcpOption82ProfileRemoteIDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileRemoteIDMAC.setStatus("mandatory")
_DhcpOption82ProfileRemoteIDString_Type = DisplayString
_DhcpOption82ProfileRemoteIDString_Object = MibTableColumn
dhcpOption82ProfileRemoteIDString = _DhcpOption82ProfileRemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 9),
    _DhcpOption82ProfileRemoteIDString_Type()
)
dhcpOption82ProfileRemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82ProfileRemoteIDString.setStatus("mandatory")
_DhcpOption82ProfileRowstatus_Type = RowStatus
_DhcpOption82ProfileRowstatus_Object = MibTableColumn
dhcpOption82ProfileRowstatus = _DhcpOption82ProfileRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 20, 4, 1, 10),
    _DhcpOption82ProfileRowstatus_Type()
)
dhcpOption82ProfileRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpOption82ProfileRowstatus.setStatus("mandatory")
_StaticRouteSetup_ObjectIdentity = ObjectIdentity
staticRouteSetup = _StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21)
)
_MaxNumberOfStaticRoutes_Type = Integer32
_MaxNumberOfStaticRoutes_Object = MibScalar
maxNumberOfStaticRoutes = _MaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 1),
    _MaxNumberOfStaticRoutes_Type()
)
maxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfStaticRoutes.setStatus("mandatory")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("mandatory")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "staticRouteIp"),
    (0, "ZYXEL-MES3500-10-MIB", "staticRouteMask"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("mandatory")
_StaticRouteName_Type = DisplayString
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("mandatory")
_StaticRouteIp_Type = IpAddress
_StaticRouteIp_Object = MibTableColumn
staticRouteIp = _StaticRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1, 2),
    _StaticRouteIp_Type()
)
staticRouteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteIp.setStatus("mandatory")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("mandatory")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("mandatory")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("mandatory")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 21, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("mandatory")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("mandatory")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1, 1)
)
arpEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "arpIpAddr"),
    (0, "ZYXEL-MES3500-10-MIB", "arpMacVid"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("mandatory")
_ArpIndex_Type = Integer32
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("mandatory")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("mandatory")
_ArpMacAddr_Type = MacAddress
_ArpMacAddr_Object = MibTableColumn
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1, 1, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("mandatory")
_ArpMacVid_Type = Integer32
_ArpMacVid_Object = MibTableColumn
arpMacVid = _ArpMacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1, 1, 4),
    _ArpMacVid_Type()
)
arpMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacVid.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 22, 1, 1, 5),
    _ArpType_Type()
)
arpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpType.setStatus("mandatory")
_PortOpModeSetup_ObjectIdentity = ObjectIdentity
portOpModeSetup = _PortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24)
)
_PortOpModePortTable_Object = MibTable
portOpModePortTable = _PortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1)
)
if mibBuilder.loadTexts:
    portOpModePortTable.setStatus("mandatory")
_PortOpModePortEntry_Object = MibTableRow
portOpModePortEntry = _PortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1)
)
portOpModePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortEntry.setStatus("mandatory")


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
              5,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed-10-half", 1),
          ("speed-10-full", 2),
          ("speed-100-half", 3),
          ("speed-100-full", 4),
          ("speed-1000-full", 5),
          ("speed-10-half-neg", 8),
          ("speed-10-full-neg", 9),
          ("speed-10-auto-neg", 10),
          ("speed-10-100-half-neg", 11),
          ("speed-10-100-full-neg", 12),
          ("speed-10-100-auto-neg", 13),
          ("speed-10-100-1000-full-neg", 14))
    )


_PortOpModePortSpeedDuplex_Type.__name__ = "Integer32"
_PortOpModePortSpeedDuplex_Object = MibTableColumn
portOpModePortSpeedDuplex = _PortOpModePortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 1),
    _PortOpModePortSpeedDuplex_Type()
)
portOpModePortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortSpeedDuplex.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 2),
    _PortOpModePortFlowCntl_Type()
)
portOpModePortFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortFlowCntl.setStatus("mandatory")
_PortOpModePortName_Type = DisplayString
_PortOpModePortName_Object = MibTableColumn
portOpModePortName = _PortOpModePortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 3),
    _PortOpModePortName_Type()
)
portOpModePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 4),
    _PortOpModePortModuleType_Type()
)
portOpModePortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortModuleType.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 5),
    _PortOpModePortLinkUpType_Type()
)
portOpModePortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLinkUpType.setStatus("mandatory")
_PortOpModePortIntrusionLock_Type = EnabledStatus
_PortOpModePortIntrusionLock_Object = MibTableColumn
portOpModePortIntrusionLock = _PortOpModePortIntrusionLock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 6),
    _PortOpModePortIntrusionLock_Type()
)
portOpModePortIntrusionLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortIntrusionLock.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 7),
    _PortOpModePortLBTestStatus_Type()
)
portOpModePortLBTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBTestStatus.setStatus("mandatory")


class _PortOpModePortCounterReset_Type(Integer32):
    """Custom type portOpModePortCounterReset based on Integer32"""
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


_PortOpModePortCounterReset_Type.__name__ = "Integer32"
_PortOpModePortCounterReset_Object = MibTableColumn
portOpModePortCounterReset = _PortOpModePortCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 24, 1, 1, 8),
    _PortOpModePortCounterReset_Type()
)
portOpModePortCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortCounterReset.setStatus("mandatory")
_PortBasedVlanSetup_ObjectIdentity = ObjectIdentity
portBasedVlanSetup = _PortBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 25)
)
_PortBasedVlanPortListTable_Object = MibTable
portBasedVlanPortListTable = _PortBasedVlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 25, 1)
)
if mibBuilder.loadTexts:
    portBasedVlanPortListTable.setStatus("mandatory")
_PortBasedVlanPortListEntry_Object = MibTableRow
portBasedVlanPortListEntry = _PortBasedVlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 25, 1, 1)
)
portBasedVlanPortListEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBasedVlanPortListEntry.setStatus("mandatory")
_PortBasedVlanPortListMembers_Type = PortList
_PortBasedVlanPortListMembers_Object = MibTableColumn
portBasedVlanPortListMembers = _PortBasedVlanPortListMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 25, 1, 1, 1),
    _PortBasedVlanPortListMembers_Type()
)
portBasedVlanPortListMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedVlanPortListMembers.setStatus("mandatory")
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventSeqNum_Type = Integer32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventEventId_Type = EventIdNumber
_EventEventId_Object = MibTableColumn
eventEventId = _EventEventId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventInstanceType_Type = InstanceType
_EventInstanceType_Object = MibTableColumn
eventInstanceType = _EventInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 4),
    _EventInstanceType_Type()
)
eventInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceType.setStatus("current")
_EventInstanceId_Type = DisplayString
_EventInstanceId_Object = MibTableColumn
eventInstanceId = _EventInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 5),
    _EventInstanceId_Type()
)
eventInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceId.setStatus("current")
_EventInstanceName_Type = DisplayString
_EventInstanceName_Object = MibTableColumn
eventInstanceName = _EventInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 6),
    _EventInstanceName_Type()
)
eventInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceName.setStatus("current")
_EventSeverity_Type = EventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventSetTime_Type = UtcTimeStamp
_EventSetTime_Object = MibTableColumn
eventSetTime = _EventSetTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 9),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_EventServAffective_Type = EventServiceAffective
_EventServAffective_Object = MibTableColumn
eventServAffective = _EventServAffective_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 10),
    _EventServAffective_Type()
)
eventServAffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventServAffective.setStatus("current")
_EventInstanceIdNumber_Type = Integer32
_EventInstanceIdNumber_Object = MibTableColumn
eventInstanceIdNumber = _EventInstanceIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 26, 1, 1, 1, 11),
    _EventInstanceIdNumber_Type()
)
eventInstanceIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceIdNumber.setStatus("current")
_TrapInfoObjects_ObjectIdentity = ObjectIdentity
trapInfoObjects = _TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 1)
)
_TrapRefSeqNum_Type = Integer32
_TrapRefSeqNum_Object = MibScalar
trapRefSeqNum = _TrapRefSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 1, 1),
    _TrapRefSeqNum_Type()
)
trapRefSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRefSeqNum.setStatus("current")
_TrapPersistence_Type = EventPersistence
_TrapPersistence_Object = MibScalar
trapPersistence = _TrapPersistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 1, 2),
    _TrapPersistence_Type()
)
trapPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPersistence.setStatus("current")
_TrapSenderNodeId_Type = Integer32
_TrapSenderNodeId_Object = MibScalar
trapSenderNodeId = _TrapSenderNodeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 1, 3),
    _TrapSenderNodeId_Type()
)
trapSenderNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderNodeId.setStatus("current")
_TrapSenderStatus_Type = Integer32
_TrapSenderStatus_Object = MibScalar
trapSenderStatus = _TrapSenderStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 1, 4),
    _TrapSenderStatus_Type()
)
trapSenderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderStatus.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 2)
)
_MulticastPortSetup_ObjectIdentity = ObjectIdentity
multicastPortSetup = _MulticastPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28)
)
_MulticastPortTable_Object = MibTable
multicastPortTable = _MulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1)
)
if mibBuilder.loadTexts:
    multicastPortTable.setStatus("mandatory")
_MulticastPortEntry_Object = MibTableRow
multicastPortEntry = _MulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1)
)
multicastPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    multicastPortEntry.setStatus("mandatory")
_MulticastPortMaxGroupLimited_Type = EnabledStatus
_MulticastPortMaxGroupLimited_Object = MibTableColumn
multicastPortMaxGroupLimited = _MulticastPortMaxGroupLimited_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 2),
    _MulticastPortMaxGroupLimited_Type()
)
multicastPortMaxGroupLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxGroupLimited.setStatus("mandatory")
_MulticastPortMaxOfGroup_Type = Integer32
_MulticastPortMaxOfGroup_Object = MibTableColumn
multicastPortMaxOfGroup = _MulticastPortMaxOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 3),
    _MulticastPortMaxOfGroup_Type()
)
multicastPortMaxOfGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxOfGroup.setStatus("mandatory")
_MulticastPortIgmpFilteringProfile_Type = DisplayString
_MulticastPortIgmpFilteringProfile_Object = MibTableColumn
multicastPortIgmpFilteringProfile = _MulticastPortIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 4),
    _MulticastPortIgmpFilteringProfile_Type()
)
multicastPortIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortIgmpFilteringProfile.setStatus("mandatory")


class _MulticastPortQuerierMode_Type(Integer32):
    """Custom type multicastPortQuerierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2),
          ("edge", 3))
    )


_MulticastPortQuerierMode_Type.__name__ = "Integer32"
_MulticastPortQuerierMode_Object = MibTableColumn
multicastPortQuerierMode = _MulticastPortQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 5),
    _MulticastPortQuerierMode_Type()
)
multicastPortQuerierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortQuerierMode.setStatus("mandatory")


class _MulticastPortThrottlingAction_Type(Integer32):
    """Custom type multicastPortThrottlingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("replace", 2))
    )


_MulticastPortThrottlingAction_Type.__name__ = "Integer32"
_MulticastPortThrottlingAction_Object = MibTableColumn
multicastPortThrottlingAction = _MulticastPortThrottlingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 6),
    _MulticastPortThrottlingAction_Type()
)
multicastPortThrottlingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortThrottlingAction.setStatus("mandatory")


class _MulticastPortLeaveMode_Type(Integer32):
    """Custom type multicastPortLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("immediate", 1),
          ("fast", 2))
    )


_MulticastPortLeaveMode_Type.__name__ = "Integer32"
_MulticastPortLeaveMode_Object = MibTableColumn
multicastPortLeaveMode = _MulticastPortLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 7),
    _MulticastPortLeaveMode_Type()
)
multicastPortLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortLeaveMode.setStatus("mandatory")
_MulticastPortLeaveTimeout_Type = Integer32
_MulticastPortLeaveTimeout_Object = MibTableColumn
multicastPortLeaveTimeout = _MulticastPortLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 8),
    _MulticastPortLeaveTimeout_Type()
)
multicastPortLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortLeaveTimeout.setStatus("mandatory")
_MulticastPortFastLeaveTimeout_Type = Integer32
_MulticastPortFastLeaveTimeout_Object = MibTableColumn
multicastPortFastLeaveTimeout = _MulticastPortFastLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 28, 1, 1, 9),
    _MulticastPortFastLeaveTimeout_Type()
)
multicastPortFastLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortFastLeaveTimeout.setStatus("mandatory")
_MulticastStatus_ObjectIdentity = ObjectIdentity
multicastStatus = _MulticastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29)
)
_MulticastStatusTable_Object = MibTable
multicastStatusTable = _MulticastStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 1)
)
if mibBuilder.loadTexts:
    multicastStatusTable.setStatus("mandatory")
_MulticastStatusEntry_Object = MibTableRow
multicastStatusEntry = _MulticastStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 1, 1)
)
multicastStatusEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-MES3500-10-MIB", "multicastStatusPort"),
    (0, "ZYXEL-MES3500-10-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastStatusEntry.setStatus("mandatory")
_MulticastStatusIndex_Type = Integer32
_MulticastStatusIndex_Object = MibTableColumn
multicastStatusIndex = _MulticastStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 1, 1, 1),
    _MulticastStatusIndex_Type()
)
multicastStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusIndex.setStatus("mandatory")
_MulticastStatusVlanID_Type = Integer32
_MulticastStatusVlanID_Object = MibTableColumn
multicastStatusVlanID = _MulticastStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 1, 1, 2),
    _MulticastStatusVlanID_Type()
)
multicastStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusVlanID.setStatus("mandatory")
_MulticastStatusPort_Type = Integer32
_MulticastStatusPort_Object = MibTableColumn
multicastStatusPort = _MulticastStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 1, 1, 3),
    _MulticastStatusPort_Type()
)
multicastStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusPort.setStatus("mandatory")
_MulticastStatusGroup_Type = IpAddress
_MulticastStatusGroup_Object = MibTableColumn
multicastStatusGroup = _MulticastStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 1, 1, 4),
    _MulticastStatusGroup_Type()
)
multicastStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusGroup.setStatus("mandatory")
_IgmpSnpCountTable_Object = MibTable
igmpSnpCountTable = _IgmpSnpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2)
)
if mibBuilder.loadTexts:
    igmpSnpCountTable.setStatus("mandatory")
_IgmpSnpCountEntry_Object = MibTableRow
igmpSnpCountEntry = _IgmpSnpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1)
)
igmpSnpCountEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "igmpSnpCountIndex"),
)
if mibBuilder.loadTexts:
    igmpSnpCountEntry.setStatus("mandatory")
_IgmpSnpCountIndex_Type = Integer32
_IgmpSnpCountIndex_Object = MibTableColumn
igmpSnpCountIndex = _IgmpSnpCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 1),
    _IgmpSnpCountIndex_Type()
)
igmpSnpCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpCountIndex.setStatus("mandatory")
_IgmpSnpV2CountQueryRx_Type = Integer32
_IgmpSnpV2CountQueryRx_Object = MibTableColumn
igmpSnpV2CountQueryRx = _IgmpSnpV2CountQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 2),
    _IgmpSnpV2CountQueryRx_Type()
)
igmpSnpV2CountQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountQueryRx.setStatus("mandatory")
_IgmpSnpV2CountReportRx_Type = Integer32
_IgmpSnpV2CountReportRx_Object = MibTableColumn
igmpSnpV2CountReportRx = _IgmpSnpV2CountReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 3),
    _IgmpSnpV2CountReportRx_Type()
)
igmpSnpV2CountReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountReportRx.setStatus("mandatory")
_IgmpSnpV2CountLeaveRx_Type = Integer32
_IgmpSnpV2CountLeaveRx_Object = MibTableColumn
igmpSnpV2CountLeaveRx = _IgmpSnpV2CountLeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 4),
    _IgmpSnpV2CountLeaveRx_Type()
)
igmpSnpV2CountLeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountLeaveRx.setStatus("mandatory")
_IgmpSnpV2CountQueryRxDrop_Type = Integer32
_IgmpSnpV2CountQueryRxDrop_Object = MibTableColumn
igmpSnpV2CountQueryRxDrop = _IgmpSnpV2CountQueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 5),
    _IgmpSnpV2CountQueryRxDrop_Type()
)
igmpSnpV2CountQueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountQueryRxDrop.setStatus("mandatory")
_IgmpSnpV2CountReportRxDrop_Type = Integer32
_IgmpSnpV2CountReportRxDrop_Object = MibTableColumn
igmpSnpV2CountReportRxDrop = _IgmpSnpV2CountReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 6),
    _IgmpSnpV2CountReportRxDrop_Type()
)
igmpSnpV2CountReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountReportRxDrop.setStatus("mandatory")
_IgmpSnpV2CountLeaveRxDrop_Type = Integer32
_IgmpSnpV2CountLeaveRxDrop_Object = MibTableColumn
igmpSnpV2CountLeaveRxDrop = _IgmpSnpV2CountLeaveRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 7),
    _IgmpSnpV2CountLeaveRxDrop_Type()
)
igmpSnpV2CountLeaveRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountLeaveRxDrop.setStatus("mandatory")
_IgmpSnpV2CountQueryTx_Type = Integer32
_IgmpSnpV2CountQueryTx_Object = MibTableColumn
igmpSnpV2CountQueryTx = _IgmpSnpV2CountQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 8),
    _IgmpSnpV2CountQueryTx_Type()
)
igmpSnpV2CountQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountQueryTx.setStatus("mandatory")
_IgmpSnpV2CountReportTx_Type = Integer32
_IgmpSnpV2CountReportTx_Object = MibTableColumn
igmpSnpV2CountReportTx = _IgmpSnpV2CountReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 9),
    _IgmpSnpV2CountReportTx_Type()
)
igmpSnpV2CountReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountReportTx.setStatus("mandatory")
_IgmpSnpV2CountLeaveTx_Type = Integer32
_IgmpSnpV2CountLeaveTx_Object = MibTableColumn
igmpSnpV2CountLeaveTx = _IgmpSnpV2CountLeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 10),
    _IgmpSnpV2CountLeaveTx_Type()
)
igmpSnpV2CountLeaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountLeaveTx.setStatus("mandatory")
_IgmpSnpV3CountQueryRx_Type = Integer32
_IgmpSnpV3CountQueryRx_Object = MibTableColumn
igmpSnpV3CountQueryRx = _IgmpSnpV3CountQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 11),
    _IgmpSnpV3CountQueryRx_Type()
)
igmpSnpV3CountQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountQueryRx.setStatus("mandatory")
_IgmpSnpV3CountReportRx_Type = Integer32
_IgmpSnpV3CountReportRx_Object = MibTableColumn
igmpSnpV3CountReportRx = _IgmpSnpV3CountReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 12),
    _IgmpSnpV3CountReportRx_Type()
)
igmpSnpV3CountReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountReportRx.setStatus("mandatory")
_IgmpSnpV3CountQueryRxDrop_Type = Integer32
_IgmpSnpV3CountQueryRxDrop_Object = MibTableColumn
igmpSnpV3CountQueryRxDrop = _IgmpSnpV3CountQueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 13),
    _IgmpSnpV3CountQueryRxDrop_Type()
)
igmpSnpV3CountQueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountQueryRxDrop.setStatus("mandatory")
_IgmpSnpV3CountReportRxDrop_Type = Integer32
_IgmpSnpV3CountReportRxDrop_Object = MibTableColumn
igmpSnpV3CountReportRxDrop = _IgmpSnpV3CountReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 14),
    _IgmpSnpV3CountReportRxDrop_Type()
)
igmpSnpV3CountReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountReportRxDrop.setStatus("mandatory")
_IgmpSnpV3CountQueryTx_Type = Integer32
_IgmpSnpV3CountQueryTx_Object = MibTableColumn
igmpSnpV3CountQueryTx = _IgmpSnpV3CountQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 15),
    _IgmpSnpV3CountQueryTx_Type()
)
igmpSnpV3CountQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountQueryTx.setStatus("mandatory")
_IgmpSnpV3CountReportTx_Type = Integer32
_IgmpSnpV3CountReportTx_Object = MibTableColumn
igmpSnpV3CountReportTx = _IgmpSnpV3CountReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 2, 1, 16),
    _IgmpSnpV3CountReportTx_Type()
)
igmpSnpV3CountReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountReportTx.setStatus("mandatory")
_MulticastVlanStatusTable_Object = MibTable
multicastVlanStatusTable = _MulticastVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 3)
)
if mibBuilder.loadTexts:
    multicastVlanStatusTable.setStatus("mandatory")
_MulticastVlanStatusEntry_Object = MibTableRow
multicastVlanStatusEntry = _MulticastVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 3, 1)
)
multicastVlanStatusEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "multicastVlanStatusVlanID"),
)
if mibBuilder.loadTexts:
    multicastVlanStatusEntry.setStatus("mandatory")
_MulticastVlanStatusVlanID_Type = Integer32
_MulticastVlanStatusVlanID_Object = MibTableColumn
multicastVlanStatusVlanID = _MulticastVlanStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 3, 1, 1),
    _MulticastVlanStatusVlanID_Type()
)
multicastVlanStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusVlanID.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 3, 1, 2),
    _MulticastVlanStatusType_Type()
)
multicastVlanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusType.setStatus("mandatory")
_MulticastVlanQueryPort_Type = PortList
_MulticastVlanQueryPort_Object = MibTableColumn
multicastVlanQueryPort = _MulticastVlanQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 3, 1, 3),
    _MulticastVlanQueryPort_Type()
)
multicastVlanQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanQueryPort.setStatus("mandatory")
_IgmpSnpCountVlanTable_Object = MibTable
igmpSnpCountVlanTable = _IgmpSnpCountVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4)
)
if mibBuilder.loadTexts:
    igmpSnpCountVlanTable.setStatus("mandatory")
_IgmpSnpCountVlanEntry_Object = MibTableRow
igmpSnpCountVlanEntry = _IgmpSnpCountVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1)
)
igmpSnpCountVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "igmpSnpCountVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnpCountVlanEntry.setStatus("mandatory")
_IgmpSnpCountVlanIndex_Type = Integer32
_IgmpSnpCountVlanIndex_Object = MibTableColumn
igmpSnpCountVlanIndex = _IgmpSnpCountVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 1),
    _IgmpSnpCountVlanIndex_Type()
)
igmpSnpCountVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpCountVlanIndex.setStatus("mandatory")
_IgmpSnpV2CountVlanQueryRx_Type = Integer32
_IgmpSnpV2CountVlanQueryRx_Object = MibTableColumn
igmpSnpV2CountVlanQueryRx = _IgmpSnpV2CountVlanQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 2),
    _IgmpSnpV2CountVlanQueryRx_Type()
)
igmpSnpV2CountVlanQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanQueryRx.setStatus("mandatory")
_IgmpSnpV2CountVlanReportRx_Type = Integer32
_IgmpSnpV2CountVlanReportRx_Object = MibTableColumn
igmpSnpV2CountVlanReportRx = _IgmpSnpV2CountVlanReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 3),
    _IgmpSnpV2CountVlanReportRx_Type()
)
igmpSnpV2CountVlanReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanReportRx.setStatus("mandatory")
_IgmpSnpV2CountVlanLeaveRx_Type = Integer32
_IgmpSnpV2CountVlanLeaveRx_Object = MibTableColumn
igmpSnpV2CountVlanLeaveRx = _IgmpSnpV2CountVlanLeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 4),
    _IgmpSnpV2CountVlanLeaveRx_Type()
)
igmpSnpV2CountVlanLeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanLeaveRx.setStatus("mandatory")
_IgmpSnpV2CountVlanQueryRxDrop_Type = Integer32
_IgmpSnpV2CountVlanQueryRxDrop_Object = MibTableColumn
igmpSnpV2CountVlanQueryRxDrop = _IgmpSnpV2CountVlanQueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 5),
    _IgmpSnpV2CountVlanQueryRxDrop_Type()
)
igmpSnpV2CountVlanQueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanQueryRxDrop.setStatus("mandatory")
_IgmpSnpV2CountVlanReportRxDrop_Type = Integer32
_IgmpSnpV2CountVlanReportRxDrop_Object = MibTableColumn
igmpSnpV2CountVlanReportRxDrop = _IgmpSnpV2CountVlanReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 6),
    _IgmpSnpV2CountVlanReportRxDrop_Type()
)
igmpSnpV2CountVlanReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanReportRxDrop.setStatus("mandatory")
_IgmpSnpV2CountVlanLeaveRxDrop_Type = Integer32
_IgmpSnpV2CountVlanLeaveRxDrop_Object = MibTableColumn
igmpSnpV2CountVlanLeaveRxDrop = _IgmpSnpV2CountVlanLeaveRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 7),
    _IgmpSnpV2CountVlanLeaveRxDrop_Type()
)
igmpSnpV2CountVlanLeaveRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanLeaveRxDrop.setStatus("mandatory")
_IgmpSnpV2CountVlanQueryTx_Type = Integer32
_IgmpSnpV2CountVlanQueryTx_Object = MibTableColumn
igmpSnpV2CountVlanQueryTx = _IgmpSnpV2CountVlanQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 8),
    _IgmpSnpV2CountVlanQueryTx_Type()
)
igmpSnpV2CountVlanQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanQueryTx.setStatus("mandatory")
_IgmpSnpV2CountVlanReportTx_Type = Integer32
_IgmpSnpV2CountVlanReportTx_Object = MibTableColumn
igmpSnpV2CountVlanReportTx = _IgmpSnpV2CountVlanReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 9),
    _IgmpSnpV2CountVlanReportTx_Type()
)
igmpSnpV2CountVlanReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanReportTx.setStatus("mandatory")
_IgmpSnpV2CountVlanLeaveTx_Type = Integer32
_IgmpSnpV2CountVlanLeaveTx_Object = MibTableColumn
igmpSnpV2CountVlanLeaveTx = _IgmpSnpV2CountVlanLeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 10),
    _IgmpSnpV2CountVlanLeaveTx_Type()
)
igmpSnpV2CountVlanLeaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountVlanLeaveTx.setStatus("mandatory")
_IgmpSnpV3CountVlanQueryRx_Type = Integer32
_IgmpSnpV3CountVlanQueryRx_Object = MibTableColumn
igmpSnpV3CountVlanQueryRx = _IgmpSnpV3CountVlanQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 11),
    _IgmpSnpV3CountVlanQueryRx_Type()
)
igmpSnpV3CountVlanQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountVlanQueryRx.setStatus("mandatory")
_IgmpSnpV3CountVlanReportRx_Type = Integer32
_IgmpSnpV3CountVlanReportRx_Object = MibTableColumn
igmpSnpV3CountVlanReportRx = _IgmpSnpV3CountVlanReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 12),
    _IgmpSnpV3CountVlanReportRx_Type()
)
igmpSnpV3CountVlanReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountVlanReportRx.setStatus("mandatory")
_IgmpSnpV3CountVlanQueryRxDrop_Type = Integer32
_IgmpSnpV3CountVlanQueryRxDrop_Object = MibTableColumn
igmpSnpV3CountVlanQueryRxDrop = _IgmpSnpV3CountVlanQueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 13),
    _IgmpSnpV3CountVlanQueryRxDrop_Type()
)
igmpSnpV3CountVlanQueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountVlanQueryRxDrop.setStatus("mandatory")
_IgmpSnpV3CountVlanReportRxDrop_Type = Integer32
_IgmpSnpV3CountVlanReportRxDrop_Object = MibTableColumn
igmpSnpV3CountVlanReportRxDrop = _IgmpSnpV3CountVlanReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 14),
    _IgmpSnpV3CountVlanReportRxDrop_Type()
)
igmpSnpV3CountVlanReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountVlanReportRxDrop.setStatus("mandatory")
_IgmpSnpV3CountVlanQueryTx_Type = Integer32
_IgmpSnpV3CountVlanQueryTx_Object = MibTableColumn
igmpSnpV3CountVlanQueryTx = _IgmpSnpV3CountVlanQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 15),
    _IgmpSnpV3CountVlanQueryTx_Type()
)
igmpSnpV3CountVlanQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountVlanQueryTx.setStatus("mandatory")
_IgmpSnpV3CountVlanReportTx_Type = Integer32
_IgmpSnpV3CountVlanReportTx_Object = MibTableColumn
igmpSnpV3CountVlanReportTx = _IgmpSnpV3CountVlanReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 4, 1, 16),
    _IgmpSnpV3CountVlanReportTx_Type()
)
igmpSnpV3CountVlanReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountVlanReportTx.setStatus("mandatory")
_IgmpSnpCountPortTable_Object = MibTable
igmpSnpCountPortTable = _IgmpSnpCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5)
)
if mibBuilder.loadTexts:
    igmpSnpCountPortTable.setStatus("mandatory")
_IgmpSnpCountPortEntry_Object = MibTableRow
igmpSnpCountPortEntry = _IgmpSnpCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1)
)
igmpSnpCountPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    igmpSnpCountPortEntry.setStatus("mandatory")
_IgmpSnpV2CountPortQueryRx_Type = Integer32
_IgmpSnpV2CountPortQueryRx_Object = MibTableColumn
igmpSnpV2CountPortQueryRx = _IgmpSnpV2CountPortQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 1),
    _IgmpSnpV2CountPortQueryRx_Type()
)
igmpSnpV2CountPortQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortQueryRx.setStatus("mandatory")
_IgmpSnpV2CountPortReportRx_Type = Integer32
_IgmpSnpV2CountPortReportRx_Object = MibTableColumn
igmpSnpV2CountPortReportRx = _IgmpSnpV2CountPortReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 2),
    _IgmpSnpV2CountPortReportRx_Type()
)
igmpSnpV2CountPortReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortReportRx.setStatus("mandatory")
_IgmpSnpV2CountPortLeaveRx_Type = Integer32
_IgmpSnpV2CountPortLeaveRx_Object = MibTableColumn
igmpSnpV2CountPortLeaveRx = _IgmpSnpV2CountPortLeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 3),
    _IgmpSnpV2CountPortLeaveRx_Type()
)
igmpSnpV2CountPortLeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortLeaveRx.setStatus("mandatory")
_IgmpSnpV2CountPortReportRxDrop_Type = Integer32
_IgmpSnpV2CountPortReportRxDrop_Object = MibTableColumn
igmpSnpV2CountPortReportRxDrop = _IgmpSnpV2CountPortReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 4),
    _IgmpSnpV2CountPortReportRxDrop_Type()
)
igmpSnpV2CountPortReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortReportRxDrop.setStatus("mandatory")
_IgmpSnpV2CountPortLeaveRxDrop_Type = Integer32
_IgmpSnpV2CountPortLeaveRxDrop_Object = MibTableColumn
igmpSnpV2CountPortLeaveRxDrop = _IgmpSnpV2CountPortLeaveRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 5),
    _IgmpSnpV2CountPortLeaveRxDrop_Type()
)
igmpSnpV2CountPortLeaveRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortLeaveRxDrop.setStatus("mandatory")
_IgmpSnpV2CountPortReportTx_Type = Integer32
_IgmpSnpV2CountPortReportTx_Object = MibTableColumn
igmpSnpV2CountPortReportTx = _IgmpSnpV2CountPortReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 6),
    _IgmpSnpV2CountPortReportTx_Type()
)
igmpSnpV2CountPortReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortReportTx.setStatus("mandatory")
_IgmpSnpV2CountPortLeaveTx_Type = Integer32
_IgmpSnpV2CountPortLeaveTx_Object = MibTableColumn
igmpSnpV2CountPortLeaveTx = _IgmpSnpV2CountPortLeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 7),
    _IgmpSnpV2CountPortLeaveTx_Type()
)
igmpSnpV2CountPortLeaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV2CountPortLeaveTx.setStatus("mandatory")
_IgmpSnpV3CountPortQueryRx_Type = Integer32
_IgmpSnpV3CountPortQueryRx_Object = MibTableColumn
igmpSnpV3CountPortQueryRx = _IgmpSnpV3CountPortQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 8),
    _IgmpSnpV3CountPortQueryRx_Type()
)
igmpSnpV3CountPortQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountPortQueryRx.setStatus("mandatory")
_IgmpSnpV3CountPortReportRx_Type = Integer32
_IgmpSnpV3CountPortReportRx_Object = MibTableColumn
igmpSnpV3CountPortReportRx = _IgmpSnpV3CountPortReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 9),
    _IgmpSnpV3CountPortReportRx_Type()
)
igmpSnpV3CountPortReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountPortReportRx.setStatus("mandatory")
_IgmpSnpV3CountPortReportRxDrop_Type = Integer32
_IgmpSnpV3CountPortReportRxDrop_Object = MibTableColumn
igmpSnpV3CountPortReportRxDrop = _IgmpSnpV3CountPortReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 10),
    _IgmpSnpV3CountPortReportRxDrop_Type()
)
igmpSnpV3CountPortReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountPortReportRxDrop.setStatus("mandatory")
_IgmpSnpV3CountPortReportTx_Type = Integer32
_IgmpSnpV3CountPortReportTx_Object = MibTableColumn
igmpSnpV3CountPortReportTx = _IgmpSnpV3CountPortReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 5, 1, 11),
    _IgmpSnpV3CountPortReportTx_Type()
)
igmpSnpV3CountPortReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpV3CountPortReportTx.setStatus("mandatory")
_IgmpSnpGroupCountStatus_ObjectIdentity = ObjectIdentity
igmpSnpGroupCountStatus = _IgmpSnpGroupCountStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6)
)
_IgmpSnpGroupCountNum_Type = Integer32
_IgmpSnpGroupCountNum_Object = MibScalar
igmpSnpGroupCountNum = _IgmpSnpGroupCountNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 1),
    _IgmpSnpGroupCountNum_Type()
)
igmpSnpGroupCountNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpGroupCountNum.setStatus("mandatory")
_IgmpSnpGroupCountVlanTable_Object = MibTable
igmpSnpGroupCountVlanTable = _IgmpSnpGroupCountVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 2)
)
if mibBuilder.loadTexts:
    igmpSnpGroupCountVlanTable.setStatus("mandatory")
_IgmpSnpGroupCountVlanEntry_Object = MibTableRow
igmpSnpGroupCountVlanEntry = _IgmpSnpGroupCountVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 2, 1)
)
igmpSnpGroupCountVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "igmpSnpGroupCountVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnpGroupCountVlanEntry.setStatus("mandatory")
_IgmpSnpGroupCountVlanIndex_Type = Integer32
_IgmpSnpGroupCountVlanIndex_Object = MibTableColumn
igmpSnpGroupCountVlanIndex = _IgmpSnpGroupCountVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 2, 1, 1),
    _IgmpSnpGroupCountVlanIndex_Type()
)
igmpSnpGroupCountVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpGroupCountVlanIndex.setStatus("mandatory")
_IgmpSnpGroupCountVlanNum_Type = Integer32
_IgmpSnpGroupCountVlanNum_Object = MibTableColumn
igmpSnpGroupCountVlanNum = _IgmpSnpGroupCountVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 2, 1, 2),
    _IgmpSnpGroupCountVlanNum_Type()
)
igmpSnpGroupCountVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpGroupCountVlanNum.setStatus("mandatory")
_IgmpSnpGroupCountPortTable_Object = MibTable
igmpSnpGroupCountPortTable = _IgmpSnpGroupCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 3)
)
if mibBuilder.loadTexts:
    igmpSnpGroupCountPortTable.setStatus("mandatory")
_IgmpSnpGroupCountPortEntry_Object = MibTableRow
igmpSnpGroupCountPortEntry = _IgmpSnpGroupCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 3, 1)
)
igmpSnpGroupCountPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    igmpSnpGroupCountPortEntry.setStatus("mandatory")
_IgmpSnpGroupCountPortNum_Type = Integer32
_IgmpSnpGroupCountPortNum_Object = MibTableColumn
igmpSnpGroupCountPortNum = _IgmpSnpGroupCountPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 29, 6, 3, 1, 1),
    _IgmpSnpGroupCountPortNum_Type()
)
igmpSnpGroupCountPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnpGroupCountPortNum.setStatus("mandatory")
_IgmpFilteringProfileSetup_ObjectIdentity = ObjectIdentity
igmpFilteringProfileSetup = _IgmpFilteringProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30)
)
_IgmpFilteringMaxNumberOfProfile_Type = Integer32
_IgmpFilteringMaxNumberOfProfile_Object = MibScalar
igmpFilteringMaxNumberOfProfile = _IgmpFilteringMaxNumberOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 1),
    _IgmpFilteringMaxNumberOfProfile_Type()
)
igmpFilteringMaxNumberOfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringMaxNumberOfProfile.setStatus("mandatory")
_IgmpFilteringProfileTable_Object = MibTable
igmpFilteringProfileTable = _IgmpFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 2)
)
if mibBuilder.loadTexts:
    igmpFilteringProfileTable.setStatus("mandatory")
_IgmpFilteringProfileEntry_Object = MibTableRow
igmpFilteringProfileEntry = _IgmpFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 2, 1)
)
igmpFilteringProfileEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "igmpFilteringProfileName"),
    (0, "ZYXEL-MES3500-10-MIB", "igmpFilteringProfileStartAddress"),
    (0, "ZYXEL-MES3500-10-MIB", "igmpFilteringProfileEndAddress"),
)
if mibBuilder.loadTexts:
    igmpFilteringProfileEntry.setStatus("mandatory")
_IgmpFilteringProfileName_Type = DisplayString
_IgmpFilteringProfileName_Object = MibTableColumn
igmpFilteringProfileName = _IgmpFilteringProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 2, 1, 1),
    _IgmpFilteringProfileName_Type()
)
igmpFilteringProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileName.setStatus("mandatory")
_IgmpFilteringProfileStartAddress_Type = IpAddress
_IgmpFilteringProfileStartAddress_Object = MibTableColumn
igmpFilteringProfileStartAddress = _IgmpFilteringProfileStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 2, 1, 2),
    _IgmpFilteringProfileStartAddress_Type()
)
igmpFilteringProfileStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileStartAddress.setStatus("mandatory")
_IgmpFilteringProfileEndAddress_Type = IpAddress
_IgmpFilteringProfileEndAddress_Object = MibTableColumn
igmpFilteringProfileEndAddress = _IgmpFilteringProfileEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 2, 1, 3),
    _IgmpFilteringProfileEndAddress_Type()
)
igmpFilteringProfileEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileEndAddress.setStatus("mandatory")
_IgmpFilteringProfileRowStatus_Type = RowStatus
_IgmpFilteringProfileRowStatus_Object = MibTableColumn
igmpFilteringProfileRowStatus = _IgmpFilteringProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 30, 2, 1, 4),
    _IgmpFilteringProfileRowStatus_Type()
)
igmpFilteringProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilteringProfileRowStatus.setStatus("mandatory")
_MvrSetup_ObjectIdentity = ObjectIdentity
mvrSetup = _MvrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31)
)
_MaxNumberOfMVR_Type = Integer32
_MaxNumberOfMVR_Object = MibScalar
maxNumberOfMVR = _MaxNumberOfMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 1),
    _MaxNumberOfMVR_Type()
)
maxNumberOfMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMVR.setStatus("mandatory")
_MvrTable_Object = MibTable
mvrTable = _MvrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2)
)
if mibBuilder.loadTexts:
    mvrTable.setStatus("mandatory")
_MvrEntry_Object = MibTableRow
mvrEntry = _MvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2, 1)
)
mvrEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mvrVlanID"),
)
if mibBuilder.loadTexts:
    mvrEntry.setStatus("mandatory")
_MvrVlanID_Type = Integer32
_MvrVlanID_Object = MibTableColumn
mvrVlanID = _MvrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2, 1, 1),
    _MvrVlanID_Type()
)
mvrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanID.setStatus("mandatory")
_MvrName_Type = DisplayString
_MvrName_Object = MibTableColumn
mvrName = _MvrName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2, 1, 2),
    _MvrName_Type()
)
mvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2, 1, 3),
    _MvrMode_Type()
)
mvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMode.setStatus("mandatory")
_MvrRowStatus_Type = RowStatus
_MvrRowStatus_Object = MibTableColumn
mvrRowStatus = _MvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2, 1, 4),
    _MvrRowStatus_Type()
)
mvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrRowStatus.setStatus("mandatory")
_Mvr8021pPriority_Type = Integer32
_Mvr8021pPriority_Object = MibTableColumn
mvr8021pPriority = _Mvr8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 2, 1, 5),
    _Mvr8021pPriority_Type()
)
mvr8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvr8021pPriority.setStatus("mandatory")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 3)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("mandatory")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 3, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mvrVlanID"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 3, 1, 1),
    _MvrPortRole_Type()
)
mvrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortRole.setStatus("mandatory")
_MvrPortTagging_Type = EnabledStatus
_MvrPortTagging_Object = MibTableColumn
mvrPortTagging = _MvrPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 3, 1, 2),
    _MvrPortTagging_Type()
)
mvrPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortTagging.setStatus("mandatory")
_MaxNumberOfMvrGroup_Type = Integer32
_MaxNumberOfMvrGroup_Object = MibScalar
maxNumberOfMvrGroup = _MaxNumberOfMvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 4),
    _MaxNumberOfMvrGroup_Type()
)
maxNumberOfMvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMvrGroup.setStatus("mandatory")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 5)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("mandatory")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 5, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mvrVlanID"),
    (0, "ZYXEL-MES3500-10-MIB", "mvrGroupName"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("mandatory")
_MvrGroupName_Type = DisplayString
_MvrGroupName_Object = MibTableColumn
mvrGroupName = _MvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 5, 1, 1),
    _MvrGroupName_Type()
)
mvrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupName.setStatus("mandatory")
_MvrGroupStartAddress_Type = IpAddress
_MvrGroupStartAddress_Object = MibTableColumn
mvrGroupStartAddress = _MvrGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 5, 1, 2),
    _MvrGroupStartAddress_Type()
)
mvrGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStartAddress.setStatus("mandatory")
_MvrGroupEndAddress_Type = IpAddress
_MvrGroupEndAddress_Object = MibTableColumn
mvrGroupEndAddress = _MvrGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 5, 1, 3),
    _MvrGroupEndAddress_Type()
)
mvrGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupEndAddress.setStatus("mandatory")
_MvrGroupRowStatus_Type = RowStatus
_MvrGroupRowStatus_Object = MibTableColumn
mvrGroupRowStatus = _MvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 31, 5, 1, 4),
    _MvrGroupRowStatus_Type()
)
mvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupRowStatus.setStatus("mandatory")
_ClusterSetup_ObjectIdentity = ObjectIdentity
clusterSetup = _ClusterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32)
)
_ClusterManager_ObjectIdentity = ObjectIdentity
clusterManager = _ClusterManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1)
)
_ClusterMaxNumOfManager_Type = Integer32
_ClusterMaxNumOfManager_Object = MibScalar
clusterMaxNumOfManager = _ClusterMaxNumOfManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1, 1),
    _ClusterMaxNumOfManager_Type()
)
clusterMaxNumOfManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMaxNumOfManager.setStatus("mandatory")
_ClusterManagerTable_Object = MibTable
clusterManagerTable = _ClusterManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1, 2)
)
if mibBuilder.loadTexts:
    clusterManagerTable.setStatus("mandatory")
_ClusterManagerEntry_Object = MibTableRow
clusterManagerEntry = _ClusterManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1, 2, 1)
)
clusterManagerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "clusterManagerVid"),
)
if mibBuilder.loadTexts:
    clusterManagerEntry.setStatus("mandatory")
_ClusterManagerVid_Type = Integer32
_ClusterManagerVid_Object = MibTableColumn
clusterManagerVid = _ClusterManagerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1, 2, 1, 1),
    _ClusterManagerVid_Type()
)
clusterManagerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterManagerVid.setStatus("mandatory")
_ClusterManagerName_Type = DisplayString
_ClusterManagerName_Object = MibTableColumn
clusterManagerName = _ClusterManagerName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1, 2, 1, 2),
    _ClusterManagerName_Type()
)
clusterManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterManagerName.setStatus("mandatory")
_ClusterManagerRowStatus_Type = RowStatus
_ClusterManagerRowStatus_Object = MibTableColumn
clusterManagerRowStatus = _ClusterManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 1, 2, 1, 3),
    _ClusterManagerRowStatus_Type()
)
clusterManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusterManagerRowStatus.setStatus("mandatory")
_ClusterMembers_ObjectIdentity = ObjectIdentity
clusterMembers = _ClusterMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2)
)
_ClusterMaxNumOfMember_Type = Integer32
_ClusterMaxNumOfMember_Object = MibScalar
clusterMaxNumOfMember = _ClusterMaxNumOfMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 1),
    _ClusterMaxNumOfMember_Type()
)
clusterMaxNumOfMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMaxNumOfMember.setStatus("mandatory")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("mandatory")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "clusterMemberMac"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("mandatory")
_ClusterMemberMac_Type = MacAddress
_ClusterMemberMac_Object = MibTableColumn
clusterMemberMac = _ClusterMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2, 1, 1),
    _ClusterMemberMac_Type()
)
clusterMemberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberMac.setStatus("mandatory")
_ClusterMemberName_Type = DisplayString
_ClusterMemberName_Object = MibTableColumn
clusterMemberName = _ClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2, 1, 2),
    _ClusterMemberName_Type()
)
clusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberName.setStatus("mandatory")
_ClusterMemberModel_Type = DisplayString
_ClusterMemberModel_Object = MibTableColumn
clusterMemberModel = _ClusterMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2, 1, 3),
    _ClusterMemberModel_Type()
)
clusterMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberModel.setStatus("mandatory")
_ClusterMemberPassword_Type = DisplayString
_ClusterMemberPassword_Object = MibTableColumn
clusterMemberPassword = _ClusterMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2, 1, 4),
    _ClusterMemberPassword_Type()
)
clusterMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberPassword.setStatus("mandatory")
_ClusterMemberRowStatus_Type = RowStatus
_ClusterMemberRowStatus_Object = MibTableColumn
clusterMemberRowStatus = _ClusterMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 2, 2, 1, 5),
    _ClusterMemberRowStatus_Type()
)
clusterMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusterMemberRowStatus.setStatus("mandatory")
_ClusterCandidates_ObjectIdentity = ObjectIdentity
clusterCandidates = _ClusterCandidates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 3)
)
_ClusterCandidateTable_Object = MibTable
clusterCandidateTable = _ClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 3, 1)
)
if mibBuilder.loadTexts:
    clusterCandidateTable.setStatus("mandatory")
_ClusterCandidateEntry_Object = MibTableRow
clusterCandidateEntry = _ClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 3, 1, 1)
)
clusterCandidateEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "clusterCandidateMac"),
)
if mibBuilder.loadTexts:
    clusterCandidateEntry.setStatus("mandatory")
_ClusterCandidateMac_Type = MacAddress
_ClusterCandidateMac_Object = MibTableColumn
clusterCandidateMac = _ClusterCandidateMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 3, 1, 1, 1),
    _ClusterCandidateMac_Type()
)
clusterCandidateMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateMac.setStatus("mandatory")
_ClusterCandidateName_Type = DisplayString
_ClusterCandidateName_Object = MibTableColumn
clusterCandidateName = _ClusterCandidateName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 3, 1, 1, 2),
    _ClusterCandidateName_Type()
)
clusterCandidateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateName.setStatus("mandatory")
_ClusterCandidateModel_Type = DisplayString
_ClusterCandidateModel_Object = MibTableColumn
clusterCandidateModel = _ClusterCandidateModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 3, 1, 1, 3),
    _ClusterCandidateModel_Type()
)
clusterCandidateModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateModel.setStatus("mandatory")
_ClusterStatus_ObjectIdentity = ObjectIdentity
clusterStatus = _ClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4)
)


class _ClusterStatusRole_Type(Integer32):
    """Custom type clusterStatusRole based on Integer32"""
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
          ("manager", 1),
          ("member", 2))
    )


_ClusterStatusRole_Type.__name__ = "Integer32"
_ClusterStatusRole_Object = MibScalar
clusterStatusRole = _ClusterStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 1),
    _ClusterStatusRole_Type()
)
clusterStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusRole.setStatus("mandatory")
_ClusterStatusManager_Type = DisplayString
_ClusterStatusManager_Object = MibScalar
clusterStatusManager = _ClusterStatusManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 2),
    _ClusterStatusManager_Type()
)
clusterStatusManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusManager.setStatus("mandatory")
_ClsuterStatusMaxNumOfMember_Type = Integer32
_ClsuterStatusMaxNumOfMember_Object = MibScalar
clsuterStatusMaxNumOfMember = _ClsuterStatusMaxNumOfMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 3),
    _ClsuterStatusMaxNumOfMember_Type()
)
clsuterStatusMaxNumOfMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsuterStatusMaxNumOfMember.setStatus("mandatory")
_ClusterStatusMemberTable_Object = MibTable
clusterStatusMemberTable = _ClusterStatusMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 4)
)
if mibBuilder.loadTexts:
    clusterStatusMemberTable.setStatus("mandatory")
_ClusterStatusMemberEntry_Object = MibTableRow
clusterStatusMemberEntry = _ClusterStatusMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 4, 1)
)
clusterStatusMemberEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "clusterStatusMemberMac"),
)
if mibBuilder.loadTexts:
    clusterStatusMemberEntry.setStatus("mandatory")
_ClusterStatusMemberMac_Type = MacAddress
_ClusterStatusMemberMac_Object = MibTableColumn
clusterStatusMemberMac = _ClusterStatusMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 4, 1, 1),
    _ClusterStatusMemberMac_Type()
)
clusterStatusMemberMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberMac.setStatus("mandatory")
_ClusterStatusMemberName_Type = DisplayString
_ClusterStatusMemberName_Object = MibTableColumn
clusterStatusMemberName = _ClusterStatusMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 4, 1, 2),
    _ClusterStatusMemberName_Type()
)
clusterStatusMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberName.setStatus("mandatory")
_ClusterStatusMemberModel_Type = DisplayString
_ClusterStatusMemberModel_Object = MibTableColumn
clusterStatusMemberModel = _ClusterStatusMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 4, 1, 3),
    _ClusterStatusMemberModel_Type()
)
clusterStatusMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberModel.setStatus("mandatory")


class _ClusterStatusMemberStatus_Type(Integer32):
    """Custom type clusterStatusMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("online", 1),
          ("offline", 2))
    )


_ClusterStatusMemberStatus_Type.__name__ = "Integer32"
_ClusterStatusMemberStatus_Object = MibTableColumn
clusterStatusMemberStatus = _ClusterStatusMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 32, 4, 4, 1, 4),
    _ClusterStatusMemberStatus_Type()
)
clusterStatusMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberStatus.setStatus("mandatory")
_SysLogSetup_ObjectIdentity = ObjectIdentity
sysLogSetup = _SysLogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33)
)
_SysLogState_Type = EnabledStatus
_SysLogState_Object = MibScalar
sysLogState = _SysLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 1),
    _SysLogState_Type()
)
sysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogState.setStatus("mandatory")
_SysLogTypeTable_Object = MibTable
sysLogTypeTable = _SysLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2)
)
if mibBuilder.loadTexts:
    sysLogTypeTable.setStatus("mandatory")
_SysLogTypeEntry_Object = MibTableRow
sysLogTypeEntry = _SysLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2, 1)
)
sysLogTypeEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "sysLogTypeIndex"),
)
if mibBuilder.loadTexts:
    sysLogTypeEntry.setStatus("mandatory")
_SysLogTypeIndex_Type = Integer32
_SysLogTypeIndex_Object = MibTableColumn
sysLogTypeIndex = _SysLogTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2, 1, 1),
    _SysLogTypeIndex_Type()
)
sysLogTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogTypeIndex.setStatus("mandatory")
_SysLogTypeName_Type = DisplayString
_SysLogTypeName_Object = MibTableColumn
sysLogTypeName = _SysLogTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2, 1, 2),
    _SysLogTypeName_Type()
)
sysLogTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogTypeName.setStatus("mandatory")
_SysLogTypeState_Type = EnabledStatus
_SysLogTypeState_Object = MibTableColumn
sysLogTypeState = _SysLogTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2, 1, 3),
    _SysLogTypeState_Type()
)
sysLogTypeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2, 1, 4),
    _SysLogTypeFacility_Type()
)
sysLogTypeFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeFacility.setStatus("mandatory")


class _SysLogTypePrivilege_Type(Integer32):
    """Custom type sysLogTypePrivilege based on Integer32"""
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


_SysLogTypePrivilege_Type.__name__ = "Integer32"
_SysLogTypePrivilege_Object = MibTableColumn
sysLogTypePrivilege = _SysLogTypePrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 2, 1, 5),
    _SysLogTypePrivilege_Type()
)
sysLogTypePrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypePrivilege.setStatus("mandatory")
_SysLogServerTable_Object = MibTable
sysLogServerTable = _SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 3)
)
if mibBuilder.loadTexts:
    sysLogServerTable.setStatus("mandatory")
_SysLogServerEntry_Object = MibTableRow
sysLogServerEntry = _SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 3, 1)
)
sysLogServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "sysLogServerAddress"),
)
if mibBuilder.loadTexts:
    sysLogServerEntry.setStatus("mandatory")
_SysLogServerAddress_Type = IpAddress
_SysLogServerAddress_Object = MibTableColumn
sysLogServerAddress = _SysLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 3, 1, 1),
    _SysLogServerAddress_Type()
)
sysLogServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogServerAddress.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 3, 1, 2),
    _SysLogServerLogLevel_Type()
)
sysLogServerLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerLogLevel.setStatus("mandatory")
_SysLogServerRowStatus_Type = RowStatus
_SysLogServerRowStatus_Object = MibTableColumn
sysLogServerRowStatus = _SysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 33, 3, 1, 3),
    _SysLogServerRowStatus_Type()
)
sysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLogServerRowStatus.setStatus("mandatory")
_DiffservSetup_ObjectIdentity = ObjectIdentity
diffservSetup = _DiffservSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34)
)
_DiffservState_Type = EnabledStatus
_DiffservState_Object = MibScalar
diffservState = _DiffservState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 1),
    _DiffservState_Type()
)
diffservState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservState.setStatus("mandatory")
_DiffservMapTable_Object = MibTable
diffservMapTable = _DiffservMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 2)
)
if mibBuilder.loadTexts:
    diffservMapTable.setStatus("mandatory")
_DiffservMapEntry_Object = MibTableRow
diffservMapEntry = _DiffservMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 2, 1)
)
diffservMapEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "diffservMapDscp"),
)
if mibBuilder.loadTexts:
    diffservMapEntry.setStatus("mandatory")
_DiffservMapDscp_Type = Integer32
_DiffservMapDscp_Object = MibTableColumn
diffservMapDscp = _DiffservMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 2, 1, 1),
    _DiffservMapDscp_Type()
)
diffservMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffservMapDscp.setStatus("mandatory")
_DiffservMapPriority_Type = Integer32
_DiffservMapPriority_Object = MibTableColumn
diffservMapPriority = _DiffservMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 2, 1, 2),
    _DiffservMapPriority_Type()
)
diffservMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservMapPriority.setStatus("mandatory")
_DiffservPortTable_Object = MibTable
diffservPortTable = _DiffservPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 3)
)
if mibBuilder.loadTexts:
    diffservPortTable.setStatus("mandatory")
_DiffservPortEntry_Object = MibTableRow
diffservPortEntry = _DiffservPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 3, 1)
)
diffservPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    diffservPortEntry.setStatus("mandatory")
_DiffservPortState_Type = EnabledStatus
_DiffservPortState_Object = MibTableColumn
diffservPortState = _DiffservPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 34, 3, 1, 1),
    _DiffservPortState_Type()
)
diffservPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservPortState.setStatus("mandatory")
_ProtoBasedVlanSetup_ObjectIdentity = ObjectIdentity
protoBasedVlanSetup = _ProtoBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35)
)
_ProtoBasedVlanTable_Object = MibTable
protoBasedVlanTable = _ProtoBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1)
)
if mibBuilder.loadTexts:
    protoBasedVlanTable.setStatus("mandatory")
_ProtoBasedVlanEntry_Object = MibTableRow
protoBasedVlanEntry = _ProtoBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1)
)
protoBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "protoBasedVlanPort"),
    (0, "ZYXEL-MES3500-10-MIB", "protoBasedVlanPacketType"),
    (0, "ZYXEL-MES3500-10-MIB", "protoBasedVlanEtherType"),
)
if mibBuilder.loadTexts:
    protoBasedVlanEntry.setStatus("mandatory")
_ProtoBasedVlanPort_Type = Integer32
_ProtoBasedVlanPort_Object = MibTableColumn
protoBasedVlanPort = _ProtoBasedVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 1),
    _ProtoBasedVlanPort_Type()
)
protoBasedVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanPort.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 2),
    _ProtoBasedVlanPacketType_Type()
)
protoBasedVlanPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanPacketType.setStatus("mandatory")
_ProtoBasedVlanEtherType_Type = Integer32
_ProtoBasedVlanEtherType_Object = MibTableColumn
protoBasedVlanEtherType = _ProtoBasedVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 3),
    _ProtoBasedVlanEtherType_Type()
)
protoBasedVlanEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protoBasedVlanEtherType.setStatus("mandatory")


class _ProtoBasedVlanName_Type(DisplayString):
    """Custom type protoBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtoBasedVlanName_Type.__name__ = "DisplayString"
_ProtoBasedVlanName_Object = MibTableColumn
protoBasedVlanName = _ProtoBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 4),
    _ProtoBasedVlanName_Type()
)
protoBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanName.setStatus("mandatory")


class _ProtoBasedVlanVid_Type(Integer32):
    """Custom type protoBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ProtoBasedVlanVid_Type.__name__ = "Integer32"
_ProtoBasedVlanVid_Object = MibTableColumn
protoBasedVlanVid = _ProtoBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 5),
    _ProtoBasedVlanVid_Type()
)
protoBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanVid.setStatus("mandatory")


class _ProtoBasedVlanPriority_Type(Integer32):
    """Custom type protoBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ProtoBasedVlanPriority_Type.__name__ = "Integer32"
_ProtoBasedVlanPriority_Object = MibTableColumn
protoBasedVlanPriority = _ProtoBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 6),
    _ProtoBasedVlanPriority_Type()
)
protoBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protoBasedVlanPriority.setStatus("mandatory")
_ProtoBasedVlanState_Type = RowStatus
_ProtoBasedVlanState_Object = MibTableColumn
protoBasedVlanState = _ProtoBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 35, 1, 1, 7),
    _ProtoBasedVlanState_Type()
)
protoBasedVlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protoBasedVlanState.setStatus("mandatory")
_Mrstp_ObjectIdentity = ObjectIdentity
mrstp = _Mrstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36)
)
_MrstpSetup_ObjectIdentity = ObjectIdentity
mrstpSetup = _MrstpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1)
)
_MrstpBridgeTable_Object = MibTable
mrstpBridgeTable = _MrstpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1)
)
if mibBuilder.loadTexts:
    mrstpBridgeTable.setStatus("mandatory")
_MrstpBridgeEntry_Object = MibTableRow
mrstpBridgeEntry = _MrstpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1)
)
mrstpBridgeEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mrstpBridgeIndex"),
)
if mibBuilder.loadTexts:
    mrstpBridgeEntry.setStatus("mandatory")
_MrstpBridgeIndex_Type = Integer32
_MrstpBridgeIndex_Object = MibTableColumn
mrstpBridgeIndex = _MrstpBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 1),
    _MrstpBridgeIndex_Type()
)
mrstpBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpBridgeIndex.setStatus("mandatory")
_MrstpState_Type = EnabledStatus
_MrstpState_Object = MibTableColumn
mrstpState = _MrstpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 2),
    _MrstpState_Type()
)
mrstpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 3),
    _MrstpProtocolSpecification_Type()
)
mrstpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpProtocolSpecification.setStatus("mandatory")


class _MrstpPriority_Type(Integer32):
    """Custom type mrstpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MrstpPriority_Type.__name__ = "Integer32"
_MrstpPriority_Object = MibTableColumn
mrstpPriority = _MrstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 4),
    _MrstpPriority_Type()
)
mrstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPriority.setStatus("mandatory")
_MrstpTimeSinceTopologyChange_Type = TimeTicks
_MrstpTimeSinceTopologyChange_Object = MibTableColumn
mrstpTimeSinceTopologyChange = _MrstpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 5),
    _MrstpTimeSinceTopologyChange_Type()
)
mrstpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpTimeSinceTopologyChange.setStatus("mandatory")
_MrstpTopChanges_Type = Counter32
_MrstpTopChanges_Object = MibTableColumn
mrstpTopChanges = _MrstpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 6),
    _MrstpTopChanges_Type()
)
mrstpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpTopChanges.setStatus("mandatory")
_MrstpDesignatedRoot_Type = BridgeId
_MrstpDesignatedRoot_Object = MibTableColumn
mrstpDesignatedRoot = _MrstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 7),
    _MrstpDesignatedRoot_Type()
)
mrstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpDesignatedRoot.setStatus("mandatory")
_MrstpRootCost_Type = Integer32
_MrstpRootCost_Object = MibTableColumn
mrstpRootCost = _MrstpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 8),
    _MrstpRootCost_Type()
)
mrstpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpRootCost.setStatus("mandatory")
_MrstpRootPort_Type = Integer32
_MrstpRootPort_Object = MibTableColumn
mrstpRootPort = _MrstpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 9),
    _MrstpRootPort_Type()
)
mrstpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpRootPort.setStatus("mandatory")
_MrstpMaxAge_Type = Timeout
_MrstpMaxAge_Object = MibTableColumn
mrstpMaxAge = _MrstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 10),
    _MrstpMaxAge_Type()
)
mrstpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpMaxAge.setStatus("mandatory")
_MrstpHelloTime_Type = Timeout
_MrstpHelloTime_Object = MibTableColumn
mrstpHelloTime = _MrstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 11),
    _MrstpHelloTime_Type()
)
mrstpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpHelloTime.setStatus("mandatory")
_MrstpHoldTime_Type = Integer32
_MrstpHoldTime_Object = MibTableColumn
mrstpHoldTime = _MrstpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 12),
    _MrstpHoldTime_Type()
)
mrstpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpHoldTime.setStatus("mandatory")
_MrstpForwardDelay_Type = Timeout
_MrstpForwardDelay_Object = MibTableColumn
mrstpForwardDelay = _MrstpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 13),
    _MrstpForwardDelay_Type()
)
mrstpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpForwardDelay.setStatus("mandatory")


class _MrstpBridgeMaxAge_Type(Timeout):
    """Custom type mrstpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MrstpBridgeMaxAge_Type.__name__ = "Timeout"
_MrstpBridgeMaxAge_Object = MibTableColumn
mrstpBridgeMaxAge = _MrstpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 14),
    _MrstpBridgeMaxAge_Type()
)
mrstpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpBridgeMaxAge.setStatus("mandatory")


class _MrstpBridgeHelloTime_Type(Timeout):
    """Custom type mrstpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MrstpBridgeHelloTime_Type.__name__ = "Timeout"
_MrstpBridgeHelloTime_Object = MibTableColumn
mrstpBridgeHelloTime = _MrstpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 15),
    _MrstpBridgeHelloTime_Type()
)
mrstpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpBridgeHelloTime.setStatus("mandatory")


class _MrstpBridgeForwardDelay_Type(Timeout):
    """Custom type mrstpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MrstpBridgeForwardDelay_Type.__name__ = "Timeout"
_MrstpBridgeForwardDelay_Object = MibTableColumn
mrstpBridgeForwardDelay = _MrstpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 1, 1, 16),
    _MrstpBridgeForwardDelay_Type()
)
mrstpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpBridgeForwardDelay.setStatus("mandatory")
_MrstpPortTable_Object = MibTable
mrstpPortTable = _MrstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2)
)
if mibBuilder.loadTexts:
    mrstpPortTable.setStatus("mandatory")
_MrstpPortEntry_Object = MibTableRow
mrstpPortEntry = _MrstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1)
)
mrstpPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mrstpPort"),
)
if mibBuilder.loadTexts:
    mrstpPortEntry.setStatus("mandatory")


class _MrstpPort_Type(Integer32):
    """Custom type mrstpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MrstpPort_Type.__name__ = "Integer32"
_MrstpPort_Object = MibTableColumn
mrstpPort = _MrstpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 1),
    _MrstpPort_Type()
)
mrstpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPort.setStatus("mandatory")


class _MrstpPortPriority_Type(Integer32):
    """Custom type mrstpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MrstpPortPriority_Type.__name__ = "Integer32"
_MrstpPortPriority_Object = MibTableColumn
mrstpPortPriority = _MrstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 2),
    _MrstpPortPriority_Type()
)
mrstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortPriority.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 3),
    _MrstpPortState_Type()
)
mrstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 4),
    _MrstpPortEnable_Type()
)
mrstpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortEnable.setStatus("mandatory")


class _MrstpPortPathCost_Type(Integer32):
    """Custom type mrstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MrstpPortPathCost_Type.__name__ = "Integer32"
_MrstpPortPathCost_Object = MibTableColumn
mrstpPortPathCost = _MrstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 5),
    _MrstpPortPathCost_Type()
)
mrstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortPathCost.setStatus("mandatory")
_MrstpPortDesignatedRoot_Type = BridgeId
_MrstpPortDesignatedRoot_Object = MibTableColumn
mrstpPortDesignatedRoot = _MrstpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 6),
    _MrstpPortDesignatedRoot_Type()
)
mrstpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedRoot.setStatus("mandatory")
_MrstpPortDesignatedCost_Type = Integer32
_MrstpPortDesignatedCost_Object = MibTableColumn
mrstpPortDesignatedCost = _MrstpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 7),
    _MrstpPortDesignatedCost_Type()
)
mrstpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedCost.setStatus("mandatory")
_MrstpPortDesignatedBridge_Type = BridgeId
_MrstpPortDesignatedBridge_Object = MibTableColumn
mrstpPortDesignatedBridge = _MrstpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 8),
    _MrstpPortDesignatedBridge_Type()
)
mrstpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedBridge.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 9),
    _MrstpPortDesignatedPort_Type()
)
mrstpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortDesignatedPort.setStatus("mandatory")
_MrstpPortForwardTransitions_Type = Counter32
_MrstpPortForwardTransitions_Object = MibTableColumn
mrstpPortForwardTransitions = _MrstpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 10),
    _MrstpPortForwardTransitions_Type()
)
mrstpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortForwardTransitions.setStatus("mandatory")
_MrstpPortOnBridgeIndex_Type = Integer32
_MrstpPortOnBridgeIndex_Object = MibTableColumn
mrstpPortOnBridgeIndex = _MrstpPortOnBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 11),
    _MrstpPortOnBridgeIndex_Type()
)
mrstpPortOnBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortOnBridgeIndex.setStatus("mandatory")


class _MrstpPortAdminEdgePort_Type(Integer32):
    """Custom type mrstpPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MrstpPortAdminEdgePort_Type.__name__ = "Integer32"
_MrstpPortAdminEdgePort_Object = MibTableColumn
mrstpPortAdminEdgePort = _MrstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 12),
    _MrstpPortAdminEdgePort_Type()
)
mrstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrstpPortAdminEdgePort.setStatus("mandatory")


class _MrstpPortOperEdgePort_Type(Integer32):
    """Custom type mrstpPortOperEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MrstpPortOperEdgePort_Type.__name__ = "Integer32"
_MrstpPortOperEdgePort_Object = MibTableColumn
mrstpPortOperEdgePort = _MrstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 1, 2, 1, 13),
    _MrstpPortOperEdgePort_Type()
)
mrstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrstpPortOperEdgePort.setStatus("mandatory")
_MrstpNotifications_ObjectIdentity = ObjectIdentity
mrstpNotifications = _MrstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 2)
)
_DhcpSnp_ObjectIdentity = ObjectIdentity
dhcpSnp = _DhcpSnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100)
)
_DhcpSnpVlanTable_Object = MibTable
dhcpSnpVlanTable = _DhcpSnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 1)
)
if mibBuilder.loadTexts:
    dhcpSnpVlanTable.setStatus("mandatory")
_DhcpSnpVlanEntry_Object = MibTableRow
dhcpSnpVlanEntry = _DhcpSnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 1, 1)
)
dhcpSnpVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpSnpVlanEntryVid"),
)
if mibBuilder.loadTexts:
    dhcpSnpVlanEntry.setStatus("mandatory")


class _DhcpSnpVlanEntryVid_Type(Integer32):
    """Custom type dhcpSnpVlanEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnpVlanEntryVid_Type.__name__ = "Integer32"
_DhcpSnpVlanEntryVid_Object = MibTableColumn
dhcpSnpVlanEntryVid = _DhcpSnpVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 1, 1, 1),
    _DhcpSnpVlanEntryVid_Type()
)
dhcpSnpVlanEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryVid.setStatus("mandatory")
_DhcpSnpVlanEntryEnable_Type = EnabledStatus
_DhcpSnpVlanEntryEnable_Object = MibTableColumn
dhcpSnpVlanEntryEnable = _DhcpSnpVlanEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 1, 1, 2),
    _DhcpSnpVlanEntryEnable_Type()
)
dhcpSnpVlanEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryEnable.setStatus("mandatory")
_DhcpSnpVlanEntryOption82Enable_Type = EnabledStatus
_DhcpSnpVlanEntryOption82Enable_Object = MibTableColumn
dhcpSnpVlanEntryOption82Enable = _DhcpSnpVlanEntryOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 1, 1, 3),
    _DhcpSnpVlanEntryOption82Enable_Type()
)
dhcpSnpVlanEntryOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryOption82Enable.setStatus("mandatory")
_DhcpSnpVlanEntryInfo_Type = EnabledStatus
_DhcpSnpVlanEntryInfo_Object = MibTableColumn
dhcpSnpVlanEntryInfo = _DhcpSnpVlanEntryInfo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 1, 1, 4),
    _DhcpSnpVlanEntryInfo_Type()
)
dhcpSnpVlanEntryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpVlanEntryInfo.setStatus("mandatory")
_DhcpSnpPortTable_Object = MibTable
dhcpSnpPortTable = _DhcpSnpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 2)
)
if mibBuilder.loadTexts:
    dhcpSnpPortTable.setStatus("mandatory")
_DhcpSnpPortEntry_Object = MibTableRow
dhcpSnpPortEntry = _DhcpSnpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 2, 1)
)
dhcpSnpPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpSnpPortEntryPort"),
)
if mibBuilder.loadTexts:
    dhcpSnpPortEntry.setStatus("mandatory")
_DhcpSnpPortEntryPort_Type = Integer32
_DhcpSnpPortEntryPort_Object = MibTableColumn
dhcpSnpPortEntryPort = _DhcpSnpPortEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 2, 1, 1),
    _DhcpSnpPortEntryPort_Type()
)
dhcpSnpPortEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryPort.setStatus("mandatory")
_DhcpSnpPortEntryTrust_Type = EnabledStatus
_DhcpSnpPortEntryTrust_Object = MibTableColumn
dhcpSnpPortEntryTrust = _DhcpSnpPortEntryTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 2, 1, 2),
    _DhcpSnpPortEntryTrust_Type()
)
dhcpSnpPortEntryTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryTrust.setStatus("mandatory")


class _DhcpSnpPortEntryRate_Type(Integer32):
    """Custom type dhcpSnpPortEntryRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_DhcpSnpPortEntryRate_Type.__name__ = "Integer32"
_DhcpSnpPortEntryRate_Object = MibTableColumn
dhcpSnpPortEntryRate = _DhcpSnpPortEntryRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 2, 1, 3),
    _DhcpSnpPortEntryRate_Type()
)
dhcpSnpPortEntryRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpPortEntryRate.setStatus("mandatory")
_DhcpSnpBindTable_Object = MibTable
dhcpSnpBindTable = _DhcpSnpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3)
)
if mibBuilder.loadTexts:
    dhcpSnpBindTable.setStatus("mandatory")
_DhcpSnpBindEntry_Object = MibTableRow
dhcpSnpBindEntry = _DhcpSnpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1)
)
dhcpSnpBindEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpSnpBindEntryMac"),
    (0, "ZYXEL-MES3500-10-MIB", "dhcpSnpBindEntryVid"),
)
if mibBuilder.loadTexts:
    dhcpSnpBindEntry.setStatus("mandatory")
_DhcpSnpBindEntryMac_Type = MacAddress
_DhcpSnpBindEntryMac_Object = MibTableColumn
dhcpSnpBindEntryMac = _DhcpSnpBindEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1, 1),
    _DhcpSnpBindEntryMac_Type()
)
dhcpSnpBindEntryMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryMac.setStatus("mandatory")
_DhcpSnpBindEntryVid_Type = Integer32
_DhcpSnpBindEntryVid_Object = MibTableColumn
dhcpSnpBindEntryVid = _DhcpSnpBindEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1, 2),
    _DhcpSnpBindEntryVid_Type()
)
dhcpSnpBindEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryVid.setStatus("mandatory")
_DhcpSnpBindEntryIP_Type = IpAddress
_DhcpSnpBindEntryIP_Object = MibTableColumn
dhcpSnpBindEntryIP = _DhcpSnpBindEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1, 3),
    _DhcpSnpBindEntryIP_Type()
)
dhcpSnpBindEntryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryIP.setStatus("mandatory")
_DhcpSnpBindEntryLease_Type = Integer32
_DhcpSnpBindEntryLease_Object = MibTableColumn
dhcpSnpBindEntryLease = _DhcpSnpBindEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1, 4),
    _DhcpSnpBindEntryLease_Type()
)
dhcpSnpBindEntryLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryLease.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1, 5),
    _DhcpSnpBindEntryType_Type()
)
dhcpSnpBindEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryType.setStatus("mandatory")
_DhcpSnpBindEntryPort_Type = Integer32
_DhcpSnpBindEntryPort_Object = MibTableColumn
dhcpSnpBindEntryPort = _DhcpSnpBindEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 3, 1, 6),
    _DhcpSnpBindEntryPort_Type()
)
dhcpSnpBindEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpBindEntryPort.setStatus("mandatory")
_DhcpSnpEnable_Type = EnabledStatus
_DhcpSnpEnable_Object = MibScalar
dhcpSnpEnable = _DhcpSnpEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 4),
    _DhcpSnpEnable_Type()
)
dhcpSnpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpEnable.setStatus("mandatory")
_DhcpSnpDb_ObjectIdentity = ObjectIdentity
dhcpSnpDb = _DhcpSnpDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 1),
    _DhcpSnpDbAbort_Type()
)
dhcpSnpDbAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbAbort.setStatus("mandatory")


class _DhcpSnpDbWriteDelay_Type(Integer32):
    """Custom type dhcpSnpDbWriteDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcpSnpDbWriteDelay_Type.__name__ = "Integer32"
_DhcpSnpDbWriteDelay_Object = MibScalar
dhcpSnpDbWriteDelay = _DhcpSnpDbWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 2),
    _DhcpSnpDbWriteDelay_Type()
)
dhcpSnpDbWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbWriteDelay.setStatus("mandatory")


class _DhcpSnpDbUrl_Type(DisplayString):
    """Custom type dhcpSnpDbUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnpDbUrl_Type.__name__ = "DisplayString"
_DhcpSnpDbUrl_Object = MibScalar
dhcpSnpDbUrl = _DhcpSnpDbUrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 3),
    _DhcpSnpDbUrl_Type()
)
dhcpSnpDbUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbUrl.setStatus("mandatory")


class _DhcpSnpDbUrlRenew_Type(DisplayString):
    """Custom type dhcpSnpDbUrlRenew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnpDbUrlRenew_Type.__name__ = "DisplayString"
_DhcpSnpDbUrlRenew_Object = MibScalar
dhcpSnpDbUrlRenew = _DhcpSnpDbUrlRenew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 4),
    _DhcpSnpDbUrlRenew_Type()
)
dhcpSnpDbUrlRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbUrlRenew.setStatus("mandatory")
_DhcpSnpDbStat_ObjectIdentity = ObjectIdentity
dhcpSnpDbStat = _DhcpSnpDbStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5)
)
_DhcpSnpDbStatClear_Type = EnabledStatus
_DhcpSnpDbStatClear_Object = MibScalar
dhcpSnpDbStatClear = _DhcpSnpDbStatClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 1),
    _DhcpSnpDbStatClear_Type()
)
dhcpSnpDbStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDbStatClear.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 2),
    _DhcpSnpDbStatAgentRunning_Type()
)
dhcpSnpDbStatAgentRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatAgentRunning.setStatus("mandatory")
_DhcpSnpDbStatDelayExpiry_Type = Integer32
_DhcpSnpDbStatDelayExpiry_Object = MibScalar
dhcpSnpDbStatDelayExpiry = _DhcpSnpDbStatDelayExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 3),
    _DhcpSnpDbStatDelayExpiry_Type()
)
dhcpSnpDbStatDelayExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatDelayExpiry.setStatus("mandatory")
_DhcpSnpDbStatAbortExpiry_Type = Integer32
_DhcpSnpDbStatAbortExpiry_Object = MibScalar
dhcpSnpDbStatAbortExpiry = _DhcpSnpDbStatAbortExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 4),
    _DhcpSnpDbStatAbortExpiry_Type()
)
dhcpSnpDbStatAbortExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatAbortExpiry.setStatus("mandatory")
_DhcpSnpDbStatLastSuccTime_Type = DisplayString
_DhcpSnpDbStatLastSuccTime_Object = MibScalar
dhcpSnpDbStatLastSuccTime = _DhcpSnpDbStatLastSuccTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 5),
    _DhcpSnpDbStatLastSuccTime_Type()
)
dhcpSnpDbStatLastSuccTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastSuccTime.setStatus("mandatory")
_DhcpSnpDbStatLastFailTime_Type = DisplayString
_DhcpSnpDbStatLastFailTime_Object = MibScalar
dhcpSnpDbStatLastFailTime = _DhcpSnpDbStatLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 6),
    _DhcpSnpDbStatLastFailTime_Type()
)
dhcpSnpDbStatLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastFailTime.setStatus("mandatory")
_DhcpSnpDbStatLastFailReason_Type = DisplayString
_DhcpSnpDbStatLastFailReason_Object = MibScalar
dhcpSnpDbStatLastFailReason = _DhcpSnpDbStatLastFailReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 7),
    _DhcpSnpDbStatLastFailReason_Type()
)
dhcpSnpDbStatLastFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastFailReason.setStatus("mandatory")
_DhcpSnpDbStatTotalAttempt_Type = Integer32
_DhcpSnpDbStatTotalAttempt_Object = MibScalar
dhcpSnpDbStatTotalAttempt = _DhcpSnpDbStatTotalAttempt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 8),
    _DhcpSnpDbStatTotalAttempt_Type()
)
dhcpSnpDbStatTotalAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalAttempt.setStatus("mandatory")
_DhcpSnpDbStatStartupFail_Type = Integer32
_DhcpSnpDbStatStartupFail_Object = MibScalar
dhcpSnpDbStatStartupFail = _DhcpSnpDbStatStartupFail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 9),
    _DhcpSnpDbStatStartupFail_Type()
)
dhcpSnpDbStatStartupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatStartupFail.setStatus("mandatory")
_DhcpSnpDbStatSuccTrans_Type = Integer32
_DhcpSnpDbStatSuccTrans_Object = MibScalar
dhcpSnpDbStatSuccTrans = _DhcpSnpDbStatSuccTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 10),
    _DhcpSnpDbStatSuccTrans_Type()
)
dhcpSnpDbStatSuccTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccTrans.setStatus("mandatory")
_DhcpSnpDbStatFailTrans_Type = Integer32
_DhcpSnpDbStatFailTrans_Object = MibScalar
dhcpSnpDbStatFailTrans = _DhcpSnpDbStatFailTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 11),
    _DhcpSnpDbStatFailTrans_Type()
)
dhcpSnpDbStatFailTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailTrans.setStatus("mandatory")
_DhcpSnpDbStatSuccRead_Type = Integer32
_DhcpSnpDbStatSuccRead_Object = MibScalar
dhcpSnpDbStatSuccRead = _DhcpSnpDbStatSuccRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 12),
    _DhcpSnpDbStatSuccRead_Type()
)
dhcpSnpDbStatSuccRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccRead.setStatus("mandatory")
_DhcpSnpDbStatFailRead_Type = Integer32
_DhcpSnpDbStatFailRead_Object = MibScalar
dhcpSnpDbStatFailRead = _DhcpSnpDbStatFailRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 13),
    _DhcpSnpDbStatFailRead_Type()
)
dhcpSnpDbStatFailRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailRead.setStatus("mandatory")
_DhcpSnpDbStatSuccWrite_Type = Integer32
_DhcpSnpDbStatSuccWrite_Object = MibScalar
dhcpSnpDbStatSuccWrite = _DhcpSnpDbStatSuccWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 14),
    _DhcpSnpDbStatSuccWrite_Type()
)
dhcpSnpDbStatSuccWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatSuccWrite.setStatus("mandatory")
_DhcpSnpDbStatFailWrite_Type = Integer32
_DhcpSnpDbStatFailWrite_Object = MibScalar
dhcpSnpDbStatFailWrite = _DhcpSnpDbStatFailWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 15),
    _DhcpSnpDbStatFailWrite_Type()
)
dhcpSnpDbStatFailWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFailWrite.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 16),
    _DhcpSnpDbStatFirstSuccAccess_Type()
)
dhcpSnpDbStatFirstSuccAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFirstSuccAccess.setStatus("mandatory")
_DhcpSnpDbStatLastIgnoreBindCol_Type = Integer32
_DhcpSnpDbStatLastIgnoreBindCol_Object = MibScalar
dhcpSnpDbStatLastIgnoreBindCol = _DhcpSnpDbStatLastIgnoreBindCol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 17),
    _DhcpSnpDbStatLastIgnoreBindCol_Type()
)
dhcpSnpDbStatLastIgnoreBindCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreBindCol.setStatus("mandatory")
_DhcpSnpDbStatLastIgnoreExpireLease_Type = Integer32
_DhcpSnpDbStatLastIgnoreExpireLease_Object = MibScalar
dhcpSnpDbStatLastIgnoreExpireLease = _DhcpSnpDbStatLastIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 18),
    _DhcpSnpDbStatLastIgnoreExpireLease_Type()
)
dhcpSnpDbStatLastIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreExpireLease.setStatus("mandatory")
_DhcpSnpDbStatLastIgnoreInvalidIntf_Type = Integer32
_DhcpSnpDbStatLastIgnoreInvalidIntf_Object = MibScalar
dhcpSnpDbStatLastIgnoreInvalidIntf = _DhcpSnpDbStatLastIgnoreInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 19),
    _DhcpSnpDbStatLastIgnoreInvalidIntf_Type()
)
dhcpSnpDbStatLastIgnoreInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreInvalidIntf.setStatus("mandatory")
_DhcpSnpDbStatLastIgnoreUnsuppVlan_Type = Integer32
_DhcpSnpDbStatLastIgnoreUnsuppVlan_Object = MibScalar
dhcpSnpDbStatLastIgnoreUnsuppVlan = _DhcpSnpDbStatLastIgnoreUnsuppVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 20),
    _DhcpSnpDbStatLastIgnoreUnsuppVlan_Type()
)
dhcpSnpDbStatLastIgnoreUnsuppVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreUnsuppVlan.setStatus("mandatory")
_DhcpSnpDbStatLastIgnoreParse_Type = Integer32
_DhcpSnpDbStatLastIgnoreParse_Object = MibScalar
dhcpSnpDbStatLastIgnoreParse = _DhcpSnpDbStatLastIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 21),
    _DhcpSnpDbStatLastIgnoreParse_Type()
)
dhcpSnpDbStatLastIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatLastIgnoreParse.setStatus("mandatory")
_DhcpSnpDbStatTotalIgnoreBindCol_Type = Integer32
_DhcpSnpDbStatTotalIgnoreBindCol_Object = MibScalar
dhcpSnpDbStatTotalIgnoreBindCol = _DhcpSnpDbStatTotalIgnoreBindCol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 22),
    _DhcpSnpDbStatTotalIgnoreBindCol_Type()
)
dhcpSnpDbStatTotalIgnoreBindCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreBindCol.setStatus("mandatory")
_DhcpSnpDbStatTotalIgnoreExpireLease_Type = Integer32
_DhcpSnpDbStatTotalIgnoreExpireLease_Object = MibScalar
dhcpSnpDbStatTotalIgnoreExpireLease = _DhcpSnpDbStatTotalIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 23),
    _DhcpSnpDbStatTotalIgnoreExpireLease_Type()
)
dhcpSnpDbStatTotalIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreExpireLease.setStatus("mandatory")
_DhcpSnpDbStatTotalIgnoreInvalidIntf_Type = Integer32
_DhcpSnpDbStatTotalIgnoreInvalidIntf_Object = MibScalar
dhcpSnpDbStatTotalIgnoreInvalidIntf = _DhcpSnpDbStatTotalIgnoreInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 24),
    _DhcpSnpDbStatTotalIgnoreInvalidIntf_Type()
)
dhcpSnpDbStatTotalIgnoreInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreInvalidIntf.setStatus("mandatory")
_DhcpSnpDbStatTotalIgnoreUnsuppVlan_Type = Integer32
_DhcpSnpDbStatTotalIgnoreUnsuppVlan_Object = MibScalar
dhcpSnpDbStatTotalIgnoreUnsuppVlan = _DhcpSnpDbStatTotalIgnoreUnsuppVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 25),
    _DhcpSnpDbStatTotalIgnoreUnsuppVlan_Type()
)
dhcpSnpDbStatTotalIgnoreUnsuppVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreUnsuppVlan.setStatus("mandatory")
_DhcpSnpDbStatTotalIgnoreParse_Type = Integer32
_DhcpSnpDbStatTotalIgnoreParse_Object = MibScalar
dhcpSnpDbStatTotalIgnoreParse = _DhcpSnpDbStatTotalIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 26),
    _DhcpSnpDbStatTotalIgnoreParse_Type()
)
dhcpSnpDbStatTotalIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatTotalIgnoreParse.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 5, 5, 27),
    _DhcpSnpDbStatFirstSuccessAccess_Type()
)
dhcpSnpDbStatFirstSuccessAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnpDbStatFirstSuccessAccess.setStatus("mandatory")
_DhcpSnpDhcpVlan_ObjectIdentity = ObjectIdentity
dhcpSnpDhcpVlan = _DhcpSnpDhcpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 6)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 6, 1),
    _DhcpSnpDhcpVlanVid_Type()
)
dhcpSnpDhcpVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnpDhcpVlanVid.setStatus("mandatory")
_DhcpSnpOption82VlanPortTable_Object = MibTable
dhcpSnpOption82VlanPortTable = _DhcpSnpOption82VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 7)
)
if mibBuilder.loadTexts:
    dhcpSnpOption82VlanPortTable.setStatus("current")
_DhcpSnpOption82VlanPortEntry_Object = MibTableRow
dhcpSnpOption82VlanPortEntry = _DhcpSnpOption82VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 7, 1)
)
dhcpSnpOption82VlanPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "dhcpSnpVlanEntryVid"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dhcpSnpOption82VlanPortEntry.setStatus("current")
_DhcpSnpOption82VlanPortProfile_Type = DisplayString
_DhcpSnpOption82VlanPortProfile_Object = MibTableColumn
dhcpSnpOption82VlanPortProfile = _DhcpSnpOption82VlanPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 100, 7, 1, 1),
    _DhcpSnpOption82VlanPortProfile_Type()
)
dhcpSnpOption82VlanPortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnpOption82VlanPortProfile.setStatus("current")
_Ipsg_ObjectIdentity = ObjectIdentity
ipsg = _Ipsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101)
)
_IpsgTable_Object = MibTable
ipsgTable = _IpsgTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1)
)
if mibBuilder.loadTexts:
    ipsgTable.setStatus("mandatory")
_IpsgEntry_Object = MibTableRow
ipsgEntry = _IpsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1)
)
ipsgEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "ipsgEntryMac"),
    (0, "ZYXEL-MES3500-10-MIB", "ipsgEntryVid"),
)
if mibBuilder.loadTexts:
    ipsgEntry.setStatus("mandatory")
_IpsgEntryMac_Type = MacAddress
_IpsgEntryMac_Object = MibTableColumn
ipsgEntryMac = _IpsgEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 1),
    _IpsgEntryMac_Type()
)
ipsgEntryMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryMac.setStatus("mandatory")


class _IpsgEntryVid_Type(Integer32):
    """Custom type ipsgEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IpsgEntryVid_Type.__name__ = "Integer32"
_IpsgEntryVid_Object = MibTableColumn
ipsgEntryVid = _IpsgEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 2),
    _IpsgEntryVid_Type()
)
ipsgEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryVid.setStatus("mandatory")
_IpsgEntryIp_Type = IpAddress
_IpsgEntryIp_Object = MibTableColumn
ipsgEntryIp = _IpsgEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 3),
    _IpsgEntryIp_Type()
)
ipsgEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryIp.setStatus("mandatory")
_IpsgEntryLease_Type = Integer32
_IpsgEntryLease_Object = MibTableColumn
ipsgEntryLease = _IpsgEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 4),
    _IpsgEntryLease_Type()
)
ipsgEntryLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryLease.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 5),
    _IpsgEntryType_Type()
)
ipsgEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryType.setStatus("mandatory")
_IpsgEntryPort_Type = Integer32
_IpsgEntryPort_Object = MibTableColumn
ipsgEntryPort = _IpsgEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 6),
    _IpsgEntryPort_Type()
)
ipsgEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryPort.setStatus("mandatory")
_IpsgEntryState_Type = RowStatus
_IpsgEntryState_Object = MibTableColumn
ipsgEntryState = _IpsgEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 101, 1, 1, 7),
    _IpsgEntryState_Type()
)
ipsgEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsgEntryState.setStatus("mandatory")
_ArpInspect_ObjectIdentity = ObjectIdentity
arpInspect = _ArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102)
)
_ArpInspectSetup_ObjectIdentity = ObjectIdentity
arpInspectSetup = _ArpInspectSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1)
)
_ArpInspectState_Type = EnabledStatus
_ArpInspectState_Object = MibScalar
arpInspectState = _ArpInspectState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 1),
    _ArpInspectState_Type()
)
arpInspectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectState.setStatus("mandatory")


class _ArpInspectFilterAgingTime_Type(Integer32):
    """Custom type arpInspectFilterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArpInspectFilterAgingTime_Type.__name__ = "Integer32"
_ArpInspectFilterAgingTime_Object = MibScalar
arpInspectFilterAgingTime = _ArpInspectFilterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 2),
    _ArpInspectFilterAgingTime_Type()
)
arpInspectFilterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterAgingTime.setStatus("mandatory")
_ArpInspectLog_ObjectIdentity = ObjectIdentity
arpInspectLog = _ArpInspectLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 3, 1),
    _ArpInspectLogEntries_Type()
)
arpInspectLogEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogEntries.setStatus("mandatory")


class _ArpInspectLogRate_Type(Integer32):
    """Custom type arpInspectLogRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ArpInspectLogRate_Type.__name__ = "Integer32"
_ArpInspectLogRate_Object = MibScalar
arpInspectLogRate = _ArpInspectLogRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 3, 2),
    _ArpInspectLogRate_Type()
)
arpInspectLogRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogRate.setStatus("mandatory")


class _ArpInspectLogInterval_Type(Integer32):
    """Custom type arpInspectLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArpInspectLogInterval_Type.__name__ = "Integer32"
_ArpInspectLogInterval_Object = MibScalar
arpInspectLogInterval = _ArpInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 3, 3),
    _ArpInspectLogInterval_Type()
)
arpInspectLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogInterval.setStatus("mandatory")
_ArpInspectVlanTable_Object = MibTable
arpInspectVlanTable = _ArpInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 4)
)
if mibBuilder.loadTexts:
    arpInspectVlanTable.setStatus("mandatory")
_ArpInspectVlanEntry_Object = MibTableRow
arpInspectVlanEntry = _ArpInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 4, 1)
)
arpInspectVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectVlanVid"),
)
if mibBuilder.loadTexts:
    arpInspectVlanEntry.setStatus("mandatory")


class _ArpInspectVlanVid_Type(Integer32):
    """Custom type arpInspectVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectVlanVid_Type.__name__ = "Integer32"
_ArpInspectVlanVid_Object = MibTableColumn
arpInspectVlanVid = _ArpInspectVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 4, 1, 1),
    _ArpInspectVlanVid_Type()
)
arpInspectVlanVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectVlanVid.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 4, 1, 2),
    _ArpInspectVlanLog_Type()
)
arpInspectVlanLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanLog.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 4, 1, 3),
    _ArpInspectVlanStatus_Type()
)
arpInspectVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanStatus.setStatus("mandatory")
_ArpInspectPortTable_Object = MibTable
arpInspectPortTable = _ArpInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 5)
)
if mibBuilder.loadTexts:
    arpInspectPortTable.setStatus("mandatory")
_ArpInspectPortEntry_Object = MibTableRow
arpInspectPortEntry = _ArpInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 5, 1)
)
arpInspectPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectPortIndex"),
)
if mibBuilder.loadTexts:
    arpInspectPortEntry.setStatus("mandatory")
_ArpInspectPortIndex_Type = Integer32
_ArpInspectPortIndex_Object = MibTableColumn
arpInspectPortIndex = _ArpInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 5, 1, 1),
    _ArpInspectPortIndex_Type()
)
arpInspectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectPortIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 5, 1, 2),
    _ArpInspectPortTrust_Type()
)
arpInspectPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortTrust.setStatus("mandatory")


class _ArpInspectPortRate_Type(Integer32):
    """Custom type arpInspectPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ArpInspectPortRate_Type.__name__ = "Integer32"
_ArpInspectPortRate_Object = MibTableColumn
arpInspectPortRate = _ArpInspectPortRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 5, 1, 3),
    _ArpInspectPortRate_Type()
)
arpInspectPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortRate.setStatus("mandatory")


class _ArpInspectPortInterval_Type(Integer32):
    """Custom type arpInspectPortInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ArpInspectPortInterval_Type.__name__ = "Integer32"
_ArpInspectPortInterval_Object = MibTableColumn
arpInspectPortInterval = _ArpInspectPortInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 1, 5, 1, 4),
    _ArpInspectPortInterval_Type()
)
arpInspectPortInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortInterval.setStatus("mandatory")
_ArpInspectStatus_ObjectIdentity = ObjectIdentity
arpInspectStatus = _ArpInspectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2)
)
_ArpInspectFilterClear_Type = EnabledStatus
_ArpInspectFilterClear_Object = MibScalar
arpInspectFilterClear = _ArpInspectFilterClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 1),
    _ArpInspectFilterClear_Type()
)
arpInspectFilterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterClear.setStatus("mandatory")
_ArpInspectLogClear_Type = EnabledStatus
_ArpInspectLogClear_Object = MibScalar
arpInspectLogClear = _ArpInspectLogClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 2),
    _ArpInspectLogClear_Type()
)
arpInspectLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogClear.setStatus("mandatory")
_ArpInspectFilterTable_Object = MibTable
arpInspectFilterTable = _ArpInspectFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3)
)
if mibBuilder.loadTexts:
    arpInspectFilterTable.setStatus("mandatory")
_ArpInspectFilterEntry_Object = MibTableRow
arpInspectFilterEntry = _ArpInspectFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1)
)
arpInspectFilterEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectFilterMac"),
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectFilterVid"),
)
if mibBuilder.loadTexts:
    arpInspectFilterEntry.setStatus("mandatory")
_ArpInspectFilterMac_Type = MacAddress
_ArpInspectFilterMac_Object = MibTableColumn
arpInspectFilterMac = _ArpInspectFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1, 1),
    _ArpInspectFilterMac_Type()
)
arpInspectFilterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterMac.setStatus("mandatory")


class _ArpInspectFilterVid_Type(Integer32):
    """Custom type arpInspectFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectFilterVid_Type.__name__ = "Integer32"
_ArpInspectFilterVid_Object = MibTableColumn
arpInspectFilterVid = _ArpInspectFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1, 2),
    _ArpInspectFilterVid_Type()
)
arpInspectFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterVid.setStatus("mandatory")
_ArpInspectFilterPort_Type = Integer32
_ArpInspectFilterPort_Object = MibTableColumn
arpInspectFilterPort = _ArpInspectFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1, 3),
    _ArpInspectFilterPort_Type()
)
arpInspectFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterPort.setStatus("mandatory")
_ArpInspectFilterExpiry_Type = Integer32
_ArpInspectFilterExpiry_Object = MibTableColumn
arpInspectFilterExpiry = _ArpInspectFilterExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1, 4),
    _ArpInspectFilterExpiry_Type()
)
arpInspectFilterExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterExpiry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1, 5),
    _ArpInspectFilterReason_Type()
)
arpInspectFilterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterReason.setStatus("mandatory")
_ArpInspectFilterRowStatus_Type = RowStatus
_ArpInspectFilterRowStatus_Object = MibTableColumn
arpInspectFilterRowStatus = _ArpInspectFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 3, 1, 6),
    _ArpInspectFilterRowStatus_Type()
)
arpInspectFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arpInspectFilterRowStatus.setStatus("mandatory")
_ArpInspectLogTable_Object = MibTable
arpInspectLogTable = _ArpInspectLogTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4)
)
if mibBuilder.loadTexts:
    arpInspectLogTable.setStatus("mandatory")
_ArpInspectLogEntry_Object = MibTableRow
arpInspectLogEntry = _ArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1)
)
arpInspectLogEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectLogMac"),
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectLogVid"),
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectLogPort"),
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectLogIp"),
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectLogReason"),
)
if mibBuilder.loadTexts:
    arpInspectLogEntry.setStatus("mandatory")
_ArpInspectLogMac_Type = MacAddress
_ArpInspectLogMac_Object = MibTableColumn
arpInspectLogMac = _ArpInspectLogMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 1),
    _ArpInspectLogMac_Type()
)
arpInspectLogMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogMac.setStatus("mandatory")


class _ArpInspectLogVid_Type(Integer32):
    """Custom type arpInspectLogVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ArpInspectLogVid_Type.__name__ = "Integer32"
_ArpInspectLogVid_Object = MibTableColumn
arpInspectLogVid = _ArpInspectLogVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 2),
    _ArpInspectLogVid_Type()
)
arpInspectLogVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogVid.setStatus("mandatory")
_ArpInspectLogPort_Type = Integer32
_ArpInspectLogPort_Object = MibTableColumn
arpInspectLogPort = _ArpInspectLogPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 3),
    _ArpInspectLogPort_Type()
)
arpInspectLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogPort.setStatus("mandatory")
_ArpInspectLogIp_Type = IpAddress
_ArpInspectLogIp_Object = MibTableColumn
arpInspectLogIp = _ArpInspectLogIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 4),
    _ArpInspectLogIp_Type()
)
arpInspectLogIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogIp.setStatus("mandatory")
_ArpInspectLogNumPkt_Type = Integer32
_ArpInspectLogNumPkt_Object = MibTableColumn
arpInspectLogNumPkt = _ArpInspectLogNumPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 5),
    _ArpInspectLogNumPkt_Type()
)
arpInspectLogNumPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogNumPkt.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 6),
    _ArpInspectLogReason_Type()
)
arpInspectLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogReason.setStatus("mandatory")
_ArpInspectLogTime_Type = DateAndTime
_ArpInspectLogTime_Object = MibTableColumn
arpInspectLogTime = _ArpInspectLogTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 4, 1, 7),
    _ArpInspectLogTime_Type()
)
arpInspectLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogTime.setStatus("mandatory")
_ArpInspectStatisticsTable_Object = MibTable
arpInspectStatisticsTable = _ArpInspectStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5)
)
if mibBuilder.loadTexts:
    arpInspectStatisticsTable.setStatus("mandatory")
_ArpInspectStatisticsEntry_Object = MibTableRow
arpInspectStatisticsEntry = _ArpInspectStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1)
)
arpInspectStatisticsEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "arpInspectStatisticsVid"),
)
if mibBuilder.loadTexts:
    arpInspectStatisticsEntry.setStatus("mandatory")
_ArpInspectStatisticsVid_Type = Integer32
_ArpInspectStatisticsVid_Object = MibTableColumn
arpInspectStatisticsVid = _ArpInspectStatisticsVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 1),
    _ArpInspectStatisticsVid_Type()
)
arpInspectStatisticsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsVid.setStatus("mandatory")
_ArpInspectStatisticsReceived_Type = Counter32
_ArpInspectStatisticsReceived_Object = MibTableColumn
arpInspectStatisticsReceived = _ArpInspectStatisticsReceived_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 2),
    _ArpInspectStatisticsReceived_Type()
)
arpInspectStatisticsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsReceived.setStatus("mandatory")
_ArpInspectStatisticsRequest_Type = Counter32
_ArpInspectStatisticsRequest_Object = MibTableColumn
arpInspectStatisticsRequest = _ArpInspectStatisticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 3),
    _ArpInspectStatisticsRequest_Type()
)
arpInspectStatisticsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsRequest.setStatus("mandatory")
_ArpInspectStatisticsReply_Type = Counter32
_ArpInspectStatisticsReply_Object = MibTableColumn
arpInspectStatisticsReply = _ArpInspectStatisticsReply_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 4),
    _ArpInspectStatisticsReply_Type()
)
arpInspectStatisticsReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsReply.setStatus("mandatory")
_ArpInspectStatisticsForward_Type = Counter32
_ArpInspectStatisticsForward_Object = MibTableColumn
arpInspectStatisticsForward = _ArpInspectStatisticsForward_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 5),
    _ArpInspectStatisticsForward_Type()
)
arpInspectStatisticsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsForward.setStatus("mandatory")
_ArpInspectStatisticsDrop_Type = Counter32
_ArpInspectStatisticsDrop_Object = MibTableColumn
arpInspectStatisticsDrop = _ArpInspectStatisticsDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 6),
    _ArpInspectStatisticsDrop_Type()
)
arpInspectStatisticsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectStatisticsDrop.setStatus("mandatory")
_ArpInspectStatisticsClear_Type = EnabledStatus
_ArpInspectStatisticsClear_Object = MibTableColumn
arpInspectStatisticsClear = _ArpInspectStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 102, 2, 5, 1, 7),
    _ArpInspectStatisticsClear_Type()
)
arpInspectStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectStatisticsClear.setStatus("mandatory")
_TrTCMSetup_ObjectIdentity = ObjectIdentity
trTCMSetup = _TrTCMSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103)
)
_TrTCMState_Type = EnabledStatus
_TrTCMState_Object = MibScalar
trTCMState = _TrTCMState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 1),
    _TrTCMState_Type()
)
trTCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 2),
    _TrTCMMode_Type()
)
trTCMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMMode.setStatus("mandatory")
_TrTCMPortTable_Object = MibTable
trTCMPortTable = _TrTCMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 3)
)
if mibBuilder.loadTexts:
    trTCMPortTable.setStatus("mandatory")
_TrTCMPortEntry_Object = MibTableRow
trTCMPortEntry = _TrTCMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 3, 1)
)
trTCMPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    trTCMPortEntry.setStatus("mandatory")
_TrTCMPortState_Type = EnabledStatus
_TrTCMPortState_Object = MibTableColumn
trTCMPortState = _TrTCMPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 3, 1, 1),
    _TrTCMPortState_Type()
)
trTCMPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trTCMPortState.setStatus("mandatory")
_TrTCMPortCIR_Type = Integer32
_TrTCMPortCIR_Object = MibTableColumn
trTCMPortCIR = _TrTCMPortCIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 3, 1, 2),
    _TrTCMPortCIR_Type()
)
trTCMPortCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortCIR.setStatus("mandatory")
_TrTCMPortPIR_Type = Integer32
_TrTCMPortPIR_Object = MibTableColumn
trTCMPortPIR = _TrTCMPortPIR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 3, 1, 3),
    _TrTCMPortPIR_Type()
)
trTCMPortPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortPIR.setStatus("mandatory")
_TrTCMPortDscpProfile_Type = DisplayString
_TrTCMPortDscpProfile_Object = MibTableColumn
trTCMPortDscpProfile = _TrTCMPortDscpProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 3, 1, 7),
    _TrTCMPortDscpProfile_Type()
)
trTCMPortDscpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMPortDscpProfile.setStatus("mandatory")
_TrTCMDscpProfileTable_Object = MibTable
trTCMDscpProfileTable = _TrTCMDscpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4)
)
if mibBuilder.loadTexts:
    trTCMDscpProfileTable.setStatus("mandatory")
_TrTCMDscpProfileEntry_Object = MibTableRow
trTCMDscpProfileEntry = _TrTCMDscpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4, 1)
)
trTCMDscpProfileEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "trTCMDscpProfileDscpName"),
)
if mibBuilder.loadTexts:
    trTCMDscpProfileEntry.setStatus("mandatory")
_TrTCMDscpProfileDscpName_Type = DisplayString
_TrTCMDscpProfileDscpName_Object = MibTableColumn
trTCMDscpProfileDscpName = _TrTCMDscpProfileDscpName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4, 1, 1),
    _TrTCMDscpProfileDscpName_Type()
)
trTCMDscpProfileDscpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trTCMDscpProfileDscpName.setStatus("mandatory")
_TrTCMDscpProfileDscpGreen_Type = Integer32
_TrTCMDscpProfileDscpGreen_Object = MibTableColumn
trTCMDscpProfileDscpGreen = _TrTCMDscpProfileDscpGreen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4, 1, 2),
    _TrTCMDscpProfileDscpGreen_Type()
)
trTCMDscpProfileDscpGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMDscpProfileDscpGreen.setStatus("mandatory")
_TrTCMDscpProfileDscpYellow_Type = Integer32
_TrTCMDscpProfileDscpYellow_Object = MibTableColumn
trTCMDscpProfileDscpYellow = _TrTCMDscpProfileDscpYellow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4, 1, 3),
    _TrTCMDscpProfileDscpYellow_Type()
)
trTCMDscpProfileDscpYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMDscpProfileDscpYellow.setStatus("mandatory")
_TrTCMDscpProfileDscpRed_Type = Integer32
_TrTCMDscpProfileDscpRed_Object = MibTableColumn
trTCMDscpProfileDscpRed = _TrTCMDscpProfileDscpRed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4, 1, 4),
    _TrTCMDscpProfileDscpRed_Type()
)
trTCMDscpProfileDscpRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trTCMDscpProfileDscpRed.setStatus("mandatory")
_TrTCMDscpProfileDscpRowstatus_Type = RowStatus
_TrTCMDscpProfileDscpRowstatus_Object = MibTableColumn
trTCMDscpProfileDscpRowstatus = _TrTCMDscpProfileDscpRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 103, 4, 1, 5),
    _TrTCMDscpProfileDscpRowstatus_Type()
)
trTCMDscpProfileDscpRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trTCMDscpProfileDscpRowstatus.setStatus("mandatory")
_LoopGuardSetup_ObjectIdentity = ObjectIdentity
loopGuardSetup = _LoopGuardSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 104)
)
_LoopGuardState_Type = EnabledStatus
_LoopGuardState_Object = MibScalar
loopGuardState = _LoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 104, 1),
    _LoopGuardState_Type()
)
loopGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardState.setStatus("mandatory")
_LoopGuardPortTable_Object = MibTable
loopGuardPortTable = _LoopGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 104, 2)
)
if mibBuilder.loadTexts:
    loopGuardPortTable.setStatus("mandatory")
_LoopGuardPortEntry_Object = MibTableRow
loopGuardPortEntry = _LoopGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 104, 2, 1)
)
loopGuardPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    loopGuardPortEntry.setStatus("mandatory")
_LoopGuardPortState_Type = EnabledStatus
_LoopGuardPortState_Object = MibTableColumn
loopGuardPortState = _LoopGuardPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 104, 2, 1, 1),
    _LoopGuardPortState_Type()
)
loopGuardPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardPortState.setStatus("mandatory")
_SubnetBasedVlanSetup_ObjectIdentity = ObjectIdentity
subnetBasedVlanSetup = _SubnetBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105)
)
_SubnetBasedVlanState_Type = EnabledStatus
_SubnetBasedVlanState_Object = MibScalar
subnetBasedVlanState = _SubnetBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 1),
    _SubnetBasedVlanState_Type()
)
subnetBasedVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanState.setStatus("mandatory")
_DhcpVlanOverrideState_Type = EnabledStatus
_DhcpVlanOverrideState_Object = MibScalar
dhcpVlanOverrideState = _DhcpVlanOverrideState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 2),
    _DhcpVlanOverrideState_Type()
)
dhcpVlanOverrideState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpVlanOverrideState.setStatus("mandatory")
_SubnetBasedVlanTable_Object = MibTable
subnetBasedVlanTable = _SubnetBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3)
)
if mibBuilder.loadTexts:
    subnetBasedVlanTable.setStatus("mandatory")
_SubnetBasedVlanEntry_Object = MibTableRow
subnetBasedVlanEntry = _SubnetBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1)
)
subnetBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "subnetBasedVlanSrcIp"),
    (0, "ZYXEL-MES3500-10-MIB", "subnetBasedVlanSrcMaskBit"),
)
if mibBuilder.loadTexts:
    subnetBasedVlanEntry.setStatus("mandatory")
_SubnetBasedVlanSrcIp_Type = IpAddress
_SubnetBasedVlanSrcIp_Object = MibTableColumn
subnetBasedVlanSrcIp = _SubnetBasedVlanSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1, 1),
    _SubnetBasedVlanSrcIp_Type()
)
subnetBasedVlanSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanSrcIp.setStatus("mandatory")


class _SubnetBasedVlanSrcMaskBit_Type(Integer32):
    """Custom type subnetBasedVlanSrcMaskBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SubnetBasedVlanSrcMaskBit_Type.__name__ = "Integer32"
_SubnetBasedVlanSrcMaskBit_Object = MibTableColumn
subnetBasedVlanSrcMaskBit = _SubnetBasedVlanSrcMaskBit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1, 2),
    _SubnetBasedVlanSrcMaskBit_Type()
)
subnetBasedVlanSrcMaskBit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetBasedVlanSrcMaskBit.setStatus("mandatory")


class _SubnetBasedVlanName_Type(DisplayString):
    """Custom type subnetBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubnetBasedVlanName_Type.__name__ = "DisplayString"
_SubnetBasedVlanName_Object = MibTableColumn
subnetBasedVlanName = _SubnetBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1, 3),
    _SubnetBasedVlanName_Type()
)
subnetBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanName.setStatus("mandatory")


class _SubnetBasedVlanVid_Type(Integer32):
    """Custom type subnetBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SubnetBasedVlanVid_Type.__name__ = "Integer32"
_SubnetBasedVlanVid_Object = MibTableColumn
subnetBasedVlanVid = _SubnetBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1, 4),
    _SubnetBasedVlanVid_Type()
)
subnetBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanVid.setStatus("mandatory")


class _SubnetBasedVlanPriority_Type(Integer32):
    """Custom type subnetBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SubnetBasedVlanPriority_Type.__name__ = "Integer32"
_SubnetBasedVlanPriority_Object = MibTableColumn
subnetBasedVlanPriority = _SubnetBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1, 5),
    _SubnetBasedVlanPriority_Type()
)
subnetBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetBasedVlanPriority.setStatus("mandatory")
_SubnetBasedVlanEntryState_Type = RowStatus
_SubnetBasedVlanEntryState_Object = MibTableColumn
subnetBasedVlanEntryState = _SubnetBasedVlanEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 105, 3, 1, 6),
    _SubnetBasedVlanEntryState_Type()
)
subnetBasedVlanEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetBasedVlanEntryState.setStatus("mandatory")
_MacAuthenticationSetup_ObjectIdentity = ObjectIdentity
macAuthenticationSetup = _MacAuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106)
)
_MacAuthenticationState_Type = EnabledStatus
_MacAuthenticationState_Object = MibScalar
macAuthenticationState = _MacAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 1),
    _MacAuthenticationState_Type()
)
macAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationState.setStatus("mandatory")
_MacAuthenticationNamePrefix_Type = DisplayString
_MacAuthenticationNamePrefix_Object = MibScalar
macAuthenticationNamePrefix = _MacAuthenticationNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 2),
    _MacAuthenticationNamePrefix_Type()
)
macAuthenticationNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationNamePrefix.setStatus("mandatory")
_MacAuthenticationPassword_Type = DisplayString
_MacAuthenticationPassword_Object = MibScalar
macAuthenticationPassword = _MacAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 3),
    _MacAuthenticationPassword_Type()
)
macAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationPassword.setStatus("mandatory")
_MacAuthenticationTimeout_Type = Integer32
_MacAuthenticationTimeout_Object = MibScalar
macAuthenticationTimeout = _MacAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 4),
    _MacAuthenticationTimeout_Type()
)
macAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationTimeout.setStatus("mandatory")
_MacAuthenticationPortTable_Object = MibTable
macAuthenticationPortTable = _MacAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 5)
)
if mibBuilder.loadTexts:
    macAuthenticationPortTable.setStatus("mandatory")
_MacAuthenticationPortEntry_Object = MibTableRow
macAuthenticationPortEntry = _MacAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 5, 1)
)
macAuthenticationPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    macAuthenticationPortEntry.setStatus("mandatory")
_MacAuthenticationPortState_Type = EnabledStatus
_MacAuthenticationPortState_Object = MibTableColumn
macAuthenticationPortState = _MacAuthenticationPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 106, 5, 1, 1),
    _MacAuthenticationPortState_Type()
)
macAuthenticationPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthenticationPortState.setStatus("mandatory")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107)
)
_MstpGen_ObjectIdentity = ObjectIdentity
mstpGen = _MstpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1)
)
_MstpGenState_Type = EnabledStatus
_MstpGenState_Object = MibScalar
mstpGenState = _MstpGenState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 1),
    _MstpGenState_Type()
)
mstpGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenState.setStatus("mandatory")
_MstpGenCfgIdName_Type = DisplayString
_MstpGenCfgIdName_Object = MibScalar
mstpGenCfgIdName = _MstpGenCfgIdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 2),
    _MstpGenCfgIdName_Type()
)
mstpGenCfgIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdName.setStatus("mandatory")
_MstpGenCfgIdRevLevel_Type = Integer32
_MstpGenCfgIdRevLevel_Object = MibScalar
mstpGenCfgIdRevLevel = _MstpGenCfgIdRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 3),
    _MstpGenCfgIdRevLevel_Type()
)
mstpGenCfgIdRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdRevLevel.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 4),
    _MstpGenCfgIdCfgDigest_Type()
)
mstpGenCfgIdCfgDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCfgIdCfgDigest.setStatus("mandatory")


class _MstpGenHelloTime_Type(Timeout):
    """Custom type mstpGenHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MstpGenHelloTime_Type.__name__ = "Timeout"
_MstpGenHelloTime_Object = MibScalar
mstpGenHelloTime = _MstpGenHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 5),
    _MstpGenHelloTime_Type()
)
mstpGenHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenHelloTime.setStatus("mandatory")


class _MstpGenMaxAge_Type(Timeout):
    """Custom type mstpGenMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_MstpGenMaxAge_Type.__name__ = "Timeout"
_MstpGenMaxAge_Object = MibScalar
mstpGenMaxAge = _MstpGenMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 6),
    _MstpGenMaxAge_Type()
)
mstpGenMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxAge.setStatus("mandatory")


class _MstpGenForwardDelay_Type(Timeout):
    """Custom type mstpGenForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstpGenForwardDelay_Type.__name__ = "Timeout"
_MstpGenForwardDelay_Object = MibScalar
mstpGenForwardDelay = _MstpGenForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 7),
    _MstpGenForwardDelay_Type()
)
mstpGenForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenForwardDelay.setStatus("mandatory")


class _MstpGenMaxHops_Type(Integer32):
    """Custom type mstpGenMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MstpGenMaxHops_Type.__name__ = "Integer32"
_MstpGenMaxHops_Object = MibScalar
mstpGenMaxHops = _MstpGenMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 8),
    _MstpGenMaxHops_Type()
)
mstpGenMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxHops.setStatus("mandatory")
_MstpGenCistRootPathCost_Type = Integer32
_MstpGenCistRootPathCost_Object = MibScalar
mstpGenCistRootPathCost = _MstpGenCistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 9),
    _MstpGenCistRootPathCost_Type()
)
mstpGenCistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootPathCost.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 1, 10),
    _MstpGenCistRootBrid_Type()
)
mstpGenCistRootBrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootBrid.setStatus("mandatory")
_MstMapTable_Object = MibTable
mstMapTable = _MstMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20)
)
if mibBuilder.loadTexts:
    mstMapTable.setStatus("mandatory")
_MstMapEntry_Object = MibTableRow
mstMapEntry = _MstMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1)
)
mstMapEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mstMapIndex"),
)
if mibBuilder.loadTexts:
    mstMapEntry.setStatus("mandatory")
_MstMapIndex_Type = MstiOrCistInstanceIndex
_MstMapIndex_Object = MibTableColumn
mstMapIndex = _MstMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1, 1),
    _MstMapIndex_Type()
)
mstMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstMapIndex.setStatus("mandatory")


class _MstMapVlans1k_Type(OctetString):
    """Custom type mstMapVlans1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans1k_Type.__name__ = "OctetString"
_MstMapVlans1k_Object = MibTableColumn
mstMapVlans1k = _MstMapVlans1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1, 2),
    _MstMapVlans1k_Type()
)
mstMapVlans1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans1k.setStatus("mandatory")


class _MstMapVlans2k_Type(OctetString):
    """Custom type mstMapVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans2k_Type.__name__ = "OctetString"
_MstMapVlans2k_Object = MibTableColumn
mstMapVlans2k = _MstMapVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1, 3),
    _MstMapVlans2k_Type()
)
mstMapVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans2k.setStatus("mandatory")


class _MstMapVlans3k_Type(OctetString):
    """Custom type mstMapVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstMapVlans3k_Type.__name__ = "OctetString"
_MstMapVlans3k_Object = MibTableColumn
mstMapVlans3k = _MstMapVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1, 5),
    _MstMapVlans4k_Type()
)
mstMapVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans4k.setStatus("current")
_MstMapRowStatus_Type = RowStatus
_MstMapRowStatus_Object = MibTableColumn
mstMapRowStatus = _MstMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 20, 1, 6),
    _MstMapRowStatus_Type()
)
mstMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstMapRowStatus.setStatus("mandatory")
_MstVlanTable_Object = MibTable
mstVlanTable = _MstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 30)
)
if mibBuilder.loadTexts:
    mstVlanTable.setStatus("mandatory")
_MstVlanEntry_Object = MibTableRow
mstVlanEntry = _MstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 30, 1)
)
mstVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mstVlanIndex"),
)
if mibBuilder.loadTexts:
    mstVlanEntry.setStatus("mandatory")


class _MstVlanIndex_Type(Integer32):
    """Custom type mstVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MstVlanIndex_Type.__name__ = "Integer32"
_MstVlanIndex_Object = MibTableColumn
mstVlanIndex = _MstVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 30, 1, 1),
    _MstVlanIndex_Type()
)
mstVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstVlanIndex.setStatus("mandatory")
_MstVlanMstIndex_Type = MstiOrCistInstanceIndex
_MstVlanMstIndex_Object = MibTableColumn
mstVlanMstIndex = _MstVlanMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 30, 1, 2),
    _MstVlanMstIndex_Type()
)
mstVlanMstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstVlanMstIndex.setStatus("mandatory")
_MstpPortTable_Object = MibTable
mstpPortTable = _MstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 40)
)
if mibBuilder.loadTexts:
    mstpPortTable.setStatus("mandatory")
_MstpPortEntry_Object = MibTableRow
mstpPortEntry = _MstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 40, 1)
)
mstpPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mstpPortIndex"),
)
if mibBuilder.loadTexts:
    mstpPortEntry.setStatus("mandatory")


class _MstpPortIndex_Type(Integer32):
    """Custom type mstpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpPortIndex_Type.__name__ = "Integer32"
_MstpPortIndex_Object = MibTableColumn
mstpPortIndex = _MstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 40, 1, 1),
    _MstpPortIndex_Type()
)
mstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpPortIndex.setStatus("mandatory")
_MstpPortOperEdgePort_Type = TruthValue
_MstpPortOperEdgePort_Object = MibTableColumn
mstpPortOperEdgePort = _MstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 40, 1, 2),
    _MstpPortOperEdgePort_Type()
)
mstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperEdgePort.setStatus("mandatory")
_MstpPortOperPointToPointMAC_Type = TruthValue
_MstpPortOperPointToPointMAC_Object = MibTableColumn
mstpPortOperPointToPointMAC = _MstpPortOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 40, 1, 3),
    _MstpPortOperPointToPointMAC_Type()
)
mstpPortOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperPointToPointMAC.setStatus("mandatory")


class _MstpPortAdminEdgePort_Type(Integer32):
    """Custom type mstpPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MstpPortAdminEdgePort_Type.__name__ = "Integer32"
_MstpPortAdminEdgePort_Object = MibTableColumn
mstpPortAdminEdgePort = _MstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 40, 1, 4),
    _MstpPortAdminEdgePort_Type()
)
mstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminEdgePort.setStatus("mandatory")
_MstpXstTable_Object = MibTable
mstpXstTable = _MstpXstTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50)
)
if mibBuilder.loadTexts:
    mstpXstTable.setStatus("mandatory")
_MstpXstEntry_Object = MibTableRow
mstpXstEntry = _MstpXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1)
)
mstpXstEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mstpXstId"),
)
if mibBuilder.loadTexts:
    mstpXstEntry.setStatus("mandatory")
_MstpXstId_Type = MstiOrCistInstanceIndex
_MstpXstId_Object = MibTableColumn
mstpXstId = _MstpXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 1),
    _MstpXstId_Type()
)
mstpXstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstId.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 2),
    _MstpXstBridgePriority_Type()
)
mstpXstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstBridgePriority.setStatus("mandatory")
_MstpXstBridgeId_Type = BridgeId
_MstpXstBridgeId_Object = MibTableColumn
mstpXstBridgeId = _MstpXstBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 3),
    _MstpXstBridgeId_Type()
)
mstpXstBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstBridgeId.setStatus("mandatory")
_MstpXstInternalRootCost_Type = Integer32
_MstpXstInternalRootCost_Object = MibTableColumn
mstpXstInternalRootCost = _MstpXstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 4),
    _MstpXstInternalRootCost_Type()
)
mstpXstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstInternalRootCost.setStatus("mandatory")
_MstpXstRootPort_Type = Integer32
_MstpXstRootPort_Object = MibTableColumn
mstpXstRootPort = _MstpXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 5),
    _MstpXstRootPort_Type()
)
mstpXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstRootPort.setStatus("mandatory")
_MstpXstTimeSinceTopologyChange_Type = TimeTicks
_MstpXstTimeSinceTopologyChange_Object = MibTableColumn
mstpXstTimeSinceTopologyChange = _MstpXstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 6),
    _MstpXstTimeSinceTopologyChange_Type()
)
mstpXstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTimeSinceTopologyChange.setStatus("mandatory")
_MstpXstTopologyChangesCount_Type = Counter32
_MstpXstTopologyChangesCount_Object = MibTableColumn
mstpXstTopologyChangesCount = _MstpXstTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 50, 1, 7),
    _MstpXstTopologyChangesCount_Type()
)
mstpXstTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTopologyChangesCount.setStatus("mandatory")
_MstpXstPortTable_Object = MibTable
mstpXstPortTable = _MstpXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60)
)
if mibBuilder.loadTexts:
    mstpXstPortTable.setStatus("mandatory")
_MstpXstPortEntry_Object = MibTableRow
mstpXstPortEntry = _MstpXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1)
)
mstpXstPortEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "mstpXstPortXstId"),
    (0, "ZYXEL-MES3500-10-MIB", "mstpXstPortIndex"),
)
if mibBuilder.loadTexts:
    mstpXstPortEntry.setStatus("mandatory")
_MstpXstPortXstId_Type = MstiOrCistInstanceIndex
_MstpXstPortXstId_Object = MibTableColumn
mstpXstPortXstId = _MstpXstPortXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 1),
    _MstpXstPortXstId_Type()
)
mstpXstPortXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpXstPortXstId.setStatus("mandatory")


class _MstpXstPortIndex_Type(Integer32):
    """Custom type mstpXstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpXstPortIndex_Type.__name__ = "Integer32"
_MstpXstPortIndex_Object = MibTableColumn
mstpXstPortIndex = _MstpXstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 2),
    _MstpXstPortIndex_Type()
)
mstpXstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortIndex.setStatus("mandatory")
_MstpXstPortEnable_Type = EnabledStatus
_MstpXstPortEnable_Object = MibTableColumn
mstpXstPortEnable = _MstpXstPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 3),
    _MstpXstPortEnable_Type()
)
mstpXstPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortEnable.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 4),
    _MstpXstPortPriority_Type()
)
mstpXstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPriority.setStatus("mandatory")


class _MstpXstPortPathCost_Type(Integer32):
    """Custom type mstpXstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MstpXstPortPathCost_Type.__name__ = "Integer32"
_MstpXstPortPathCost_Object = MibTableColumn
mstpXstPortPathCost = _MstpXstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 5),
    _MstpXstPortPathCost_Type()
)
mstpXstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPathCost.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 6),
    _MstpXstPortState_Type()
)
mstpXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortState.setStatus("mandatory")
_MstpXstPortDesignatedRoot_Type = BridgeId
_MstpXstPortDesignatedRoot_Object = MibTableColumn
mstpXstPortDesignatedRoot = _MstpXstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 7),
    _MstpXstPortDesignatedRoot_Type()
)
mstpXstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedRoot.setStatus("mandatory")
_MstpXstPortDesignatedCost_Type = Integer32
_MstpXstPortDesignatedCost_Object = MibTableColumn
mstpXstPortDesignatedCost = _MstpXstPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 8),
    _MstpXstPortDesignatedCost_Type()
)
mstpXstPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedCost.setStatus("mandatory")
_MstpXstPortDesignatedBridge_Type = BridgeId
_MstpXstPortDesignatedBridge_Object = MibTableColumn
mstpXstPortDesignatedBridge = _MstpXstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 9),
    _MstpXstPortDesignatedBridge_Type()
)
mstpXstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedBridge.setStatus("mandatory")
_MstpXstPortDesignatedPort_Type = Integer32
_MstpXstPortDesignatedPort_Object = MibTableColumn
mstpXstPortDesignatedPort = _MstpXstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 60, 1, 10),
    _MstpXstPortDesignatedPort_Type()
)
mstpXstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedPort.setStatus("mandatory")
_MstpNotifications_ObjectIdentity = ObjectIdentity
mstpNotifications = _MstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 70)
)
_RadiusServerSetup_ObjectIdentity = ObjectIdentity
radiusServerSetup = _RadiusServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108)
)
_RadiusAuthServerSetup_ObjectIdentity = ObjectIdentity
radiusAuthServerSetup = _RadiusAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 1),
    _RadiusAuthServerMode_Type()
)
radiusAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerMode.setStatus("mandatory")
_RadiusAuthServerTimeout_Type = Integer32
_RadiusAuthServerTimeout_Object = MibScalar
radiusAuthServerTimeout = _RadiusAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 2),
    _RadiusAuthServerTimeout_Type()
)
radiusAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerTimeout.setStatus("mandatory")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("mandatory")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("mandatory")
_RadiusAuthServerIndex_Type = Integer32
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("mandatory")
_RadiusAuthServerIpAddr_Type = IpAddress
_RadiusAuthServerIpAddr_Object = MibTableColumn
radiusAuthServerIpAddr = _RadiusAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 3, 1, 2),
    _RadiusAuthServerIpAddr_Type()
)
radiusAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerIpAddr.setStatus("mandatory")
_RadiusAuthServerUdpPort_Type = Integer32
_RadiusAuthServerUdpPort_Object = MibTableColumn
radiusAuthServerUdpPort = _RadiusAuthServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 3, 1, 3),
    _RadiusAuthServerUdpPort_Type()
)
radiusAuthServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerUdpPort.setStatus("mandatory")
_RadiusAuthServerSharedSecret_Type = DisplayString
_RadiusAuthServerSharedSecret_Object = MibTableColumn
radiusAuthServerSharedSecret = _RadiusAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 1, 3, 1, 4),
    _RadiusAuthServerSharedSecret_Type()
)
radiusAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerSharedSecret.setStatus("mandatory")
_RadiusAcctServerSetup_ObjectIdentity = ObjectIdentity
radiusAcctServerSetup = _RadiusAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2)
)
_RadiusAcctServerTimeout_Type = Integer32
_RadiusAcctServerTimeout_Object = MibScalar
radiusAcctServerTimeout = _RadiusAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 1),
    _RadiusAcctServerTimeout_Type()
)
radiusAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerTimeout.setStatus("mandatory")
_RadiusAcctServerTable_Object = MibTable
radiusAcctServerTable = _RadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 2)
)
if mibBuilder.loadTexts:
    radiusAcctServerTable.setStatus("mandatory")
_RadiusAcctServerEntry_Object = MibTableRow
radiusAcctServerEntry = _RadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 2, 1)
)
radiusAcctServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "radiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAcctServerEntry.setStatus("mandatory")
_RadiusAcctServerIndex_Type = Integer32
_RadiusAcctServerIndex_Object = MibTableColumn
radiusAcctServerIndex = _RadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 2, 1, 1),
    _RadiusAcctServerIndex_Type()
)
radiusAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAcctServerIndex.setStatus("mandatory")
_RadiusAcctServerIpAddr_Type = IpAddress
_RadiusAcctServerIpAddr_Object = MibTableColumn
radiusAcctServerIpAddr = _RadiusAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 2, 1, 2),
    _RadiusAcctServerIpAddr_Type()
)
radiusAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerIpAddr.setStatus("mandatory")
_RadiusAcctServerUdpPort_Type = Integer32
_RadiusAcctServerUdpPort_Object = MibTableColumn
radiusAcctServerUdpPort = _RadiusAcctServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 2, 1, 3),
    _RadiusAcctServerUdpPort_Type()
)
radiusAcctServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerUdpPort.setStatus("mandatory")
_RadiusAcctServerSharedSecret_Type = DisplayString
_RadiusAcctServerSharedSecret_Object = MibTableColumn
radiusAcctServerSharedSecret = _RadiusAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 108, 2, 2, 1, 4),
    _RadiusAcctServerSharedSecret_Type()
)
radiusAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerSharedSecret.setStatus("mandatory")
_TacacsServerSetup_ObjectIdentity = ObjectIdentity
tacacsServerSetup = _TacacsServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109)
)
_TacacsAuthServerSetup_ObjectIdentity = ObjectIdentity
tacacsAuthServerSetup = _TacacsAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 1),
    _TacacsAuthServerMode_Type()
)
tacacsAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerMode.setStatus("mandatory")
_TacacsAuthServerTimeout_Type = Integer32
_TacacsAuthServerTimeout_Object = MibScalar
tacacsAuthServerTimeout = _TacacsAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 2),
    _TacacsAuthServerTimeout_Type()
)
tacacsAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTimeout.setStatus("mandatory")
_TacacsAuthServerTable_Object = MibTable
tacacsAuthServerTable = _TacacsAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 3)
)
if mibBuilder.loadTexts:
    tacacsAuthServerTable.setStatus("mandatory")
_TacacsAuthServerEntry_Object = MibTableRow
tacacsAuthServerEntry = _TacacsAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 3, 1)
)
tacacsAuthServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "tacacsAuthServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAuthServerEntry.setStatus("mandatory")
_TacacsAuthServerIndex_Type = Integer32
_TacacsAuthServerIndex_Object = MibTableColumn
tacacsAuthServerIndex = _TacacsAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 3, 1, 1),
    _TacacsAuthServerIndex_Type()
)
tacacsAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAuthServerIndex.setStatus("mandatory")
_TacacsAuthServerIpAddr_Type = IpAddress
_TacacsAuthServerIpAddr_Object = MibTableColumn
tacacsAuthServerIpAddr = _TacacsAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 3, 1, 2),
    _TacacsAuthServerIpAddr_Type()
)
tacacsAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerIpAddr.setStatus("mandatory")
_TacacsAuthServerTcpPort_Type = Integer32
_TacacsAuthServerTcpPort_Object = MibTableColumn
tacacsAuthServerTcpPort = _TacacsAuthServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 3, 1, 3),
    _TacacsAuthServerTcpPort_Type()
)
tacacsAuthServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTcpPort.setStatus("mandatory")
_TacacsAuthServerSharedSecret_Type = DisplayString
_TacacsAuthServerSharedSecret_Object = MibTableColumn
tacacsAuthServerSharedSecret = _TacacsAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 1, 3, 1, 4),
    _TacacsAuthServerSharedSecret_Type()
)
tacacsAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerSharedSecret.setStatus("mandatory")
_TacacsAcctServerSetup_ObjectIdentity = ObjectIdentity
tacacsAcctServerSetup = _TacacsAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2)
)
_TacacsAcctServerTimeout_Type = Integer32
_TacacsAcctServerTimeout_Object = MibScalar
tacacsAcctServerTimeout = _TacacsAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 1),
    _TacacsAcctServerTimeout_Type()
)
tacacsAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTimeout.setStatus("mandatory")
_TacacsAcctServerTable_Object = MibTable
tacacsAcctServerTable = _TacacsAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 2)
)
if mibBuilder.loadTexts:
    tacacsAcctServerTable.setStatus("mandatory")
_TacacsAcctServerEntry_Object = MibTableRow
tacacsAcctServerEntry = _TacacsAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 2, 1)
)
tacacsAcctServerEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "tacacsAcctServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAcctServerEntry.setStatus("mandatory")
_TacacsAcctServerIndex_Type = Integer32
_TacacsAcctServerIndex_Object = MibTableColumn
tacacsAcctServerIndex = _TacacsAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 2, 1, 1),
    _TacacsAcctServerIndex_Type()
)
tacacsAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAcctServerIndex.setStatus("mandatory")
_TacacsAcctServerIpAddr_Type = IpAddress
_TacacsAcctServerIpAddr_Object = MibTableColumn
tacacsAcctServerIpAddr = _TacacsAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 2, 1, 2),
    _TacacsAcctServerIpAddr_Type()
)
tacacsAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerIpAddr.setStatus("mandatory")
_TacacsAcctServerTcpPort_Type = Integer32
_TacacsAcctServerTcpPort_Object = MibTableColumn
tacacsAcctServerTcpPort = _TacacsAcctServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 2, 1, 3),
    _TacacsAcctServerTcpPort_Type()
)
tacacsAcctServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTcpPort.setStatus("mandatory")
_TacacsAcctServerSharedSecret_Type = DisplayString
_TacacsAcctServerSharedSecret_Object = MibTableColumn
tacacsAcctServerSharedSecret = _TacacsAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 109, 2, 2, 1, 4),
    _TacacsAcctServerSharedSecret_Type()
)
tacacsAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerSharedSecret.setStatus("mandatory")
_AaaSetup_ObjectIdentity = ObjectIdentity
aaaSetup = _AaaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110)
)
_AuthenticationSetup_ObjectIdentity = ObjectIdentity
authenticationSetup = _AuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 1)
)
_AuthenticationTypeTable_Object = MibTable
authenticationTypeTable = _AuthenticationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 1, 1)
)
if mibBuilder.loadTexts:
    authenticationTypeTable.setStatus("mandatory")
_AuthenticationTypeEntry_Object = MibTableRow
authenticationTypeEntry = _AuthenticationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 1, 1, 1)
)
authenticationTypeEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "authenticationTypeName"),
)
if mibBuilder.loadTexts:
    authenticationTypeEntry.setStatus("mandatory")
_AuthenticationTypeName_Type = DisplayString
_AuthenticationTypeName_Object = MibTableColumn
authenticationTypeName = _AuthenticationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 1, 1, 1, 1),
    _AuthenticationTypeName_Type()
)
authenticationTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationTypeName.setStatus("mandatory")
_AuthenticationTypeMethodList_Type = OctetString
_AuthenticationTypeMethodList_Object = MibTableColumn
authenticationTypeMethodList = _AuthenticationTypeMethodList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 1, 1, 1, 2),
    _AuthenticationTypeMethodList_Type()
)
authenticationTypeMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationTypeMethodList.setStatus("mandatory")
_AccountingSetup_ObjectIdentity = ObjectIdentity
accountingSetup = _AccountingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2)
)
_AccountingUpdatePeriod_Type = Integer32
_AccountingUpdatePeriod_Object = MibScalar
accountingUpdatePeriod = _AccountingUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 1),
    _AccountingUpdatePeriod_Type()
)
accountingUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingUpdatePeriod.setStatus("mandatory")
_AccountingTypeTable_Object = MibTable
accountingTypeTable = _AccountingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2)
)
if mibBuilder.loadTexts:
    accountingTypeTable.setStatus("mandatory")
_AccountingTypeEntry_Object = MibTableRow
accountingTypeEntry = _AccountingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1)
)
accountingTypeEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "accountingTypeName"),
)
if mibBuilder.loadTexts:
    accountingTypeEntry.setStatus("mandatory")
_AccountingTypeName_Type = DisplayString
_AccountingTypeName_Object = MibTableColumn
accountingTypeName = _AccountingTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1, 1),
    _AccountingTypeName_Type()
)
accountingTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingTypeName.setStatus("mandatory")
_AccountingTypeActive_Type = EnabledStatus
_AccountingTypeActive_Object = MibTableColumn
accountingTypeActive = _AccountingTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1, 2),
    _AccountingTypeActive_Type()
)
accountingTypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeActive.setStatus("mandatory")
_AccountingTypeBroadcast_Type = EnabledStatus
_AccountingTypeBroadcast_Object = MibTableColumn
accountingTypeBroadcast = _AccountingTypeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1, 3),
    _AccountingTypeBroadcast_Type()
)
accountingTypeBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeBroadcast.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1, 4),
    _AccountingTypeMode_Type()
)
accountingTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeMode.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1, 5),
    _AccountingTypeMethod_Type()
)
accountingTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeMethod.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 2, 2, 1, 6),
    _AccountingTypePrivilege_Type()
)
accountingTypePrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypePrivilege.setStatus("mandatory")
_AuthorizationSetup_ObjectIdentity = ObjectIdentity
authorizationSetup = _AuthorizationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 3)
)
_AuthorizationTypeTable_Object = MibTable
authorizationTypeTable = _AuthorizationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 3, 1)
)
if mibBuilder.loadTexts:
    authorizationTypeTable.setStatus("mandatory")
_AuthorizationTypeEntry_Object = MibTableRow
authorizationTypeEntry = _AuthorizationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 3, 1, 1)
)
authorizationTypeEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "authorizationTypeName"),
)
if mibBuilder.loadTexts:
    authorizationTypeEntry.setStatus("mandatory")
_AuthorizationTypeName_Type = DisplayString
_AuthorizationTypeName_Object = MibTableColumn
authorizationTypeName = _AuthorizationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 3, 1, 1, 1),
    _AuthorizationTypeName_Type()
)
authorizationTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizationTypeName.setStatus("mandatory")
_AuthorizationTypeActive_Type = EnabledStatus
_AuthorizationTypeActive_Object = MibTableColumn
authorizationTypeActive = _AuthorizationTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 3, 1, 1, 2),
    _AuthorizationTypeActive_Type()
)
authorizationTypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizationTypeActive.setStatus("mandatory")


class _AuthorizationTypeMethod_Type(Integer32):
    """Custom type authorizationTypeMethod based on Integer32"""
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


_AuthorizationTypeMethod_Type.__name__ = "Integer32"
_AuthorizationTypeMethod_Object = MibTableColumn
authorizationTypeMethod = _AuthorizationTypeMethod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 110, 3, 1, 1, 3),
    _AuthorizationTypeMethod_Type()
)
authorizationTypeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizationTypeMethod.setStatus("mandatory")
_PortIsolationSetup_ObjectIdentity = ObjectIdentity
portIsolationSetup = _PortIsolationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 112)
)
_PortIsolationTable_Object = MibTable
portIsolationTable = _PortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 112, 1)
)
if mibBuilder.loadTexts:
    portIsolationTable.setStatus("mandatory")
_PortIsolationEntry_Object = MibTableRow
portIsolationEntry = _PortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 112, 1, 1)
)
portIsolationEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portIsolationEntry.setStatus("mandatory")
_PortIsolationState_Type = EnabledStatus
_PortIsolationState_Object = MibTableColumn
portIsolationState = _PortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 112, 1, 1, 1),
    _PortIsolationState_Type()
)
portIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIsolationState.setStatus("mandatory")
_L2ptSetup_ObjectIdentity = ObjectIdentity
l2ptSetup = _L2ptSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115)
)
_L2ptState_Type = EnabledStatus
_L2ptState_Object = MibScalar
l2ptState = _L2ptState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 1),
    _L2ptState_Type()
)
l2ptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptState.setStatus("mandatory")
_L2ptMacAddr_Type = MacAddress
_L2ptMacAddr_Object = MibScalar
l2ptMacAddr = _L2ptMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 2),
    _L2ptMacAddr_Type()
)
l2ptMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptMacAddr.setStatus("mandatory")
_L2ptTable_Object = MibTable
l2ptTable = _L2ptTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 3)
)
if mibBuilder.loadTexts:
    l2ptTable.setStatus("mandatory")
_L2ptEntry_Object = MibTableRow
l2ptEntry = _L2ptEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 3, 1)
)
l2ptEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    l2ptEntry.setStatus("mandatory")


class _L2ptProtocolGroup_Type(Bits):
    """Custom type l2ptProtocolGroup based on Bits"""
    namedValues = NamedValues(
        *(("cdp", 0),
          ("stp", 1),
          ("vtp", 2))
    )

_L2ptProtocolGroup_Type.__name__ = "Bits"
_L2ptProtocolGroup_Object = MibTableColumn
l2ptProtocolGroup = _L2ptProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 3, 1, 1),
    _L2ptProtocolGroup_Type()
)
l2ptProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptProtocolGroup.setStatus("mandatory")


class _L2ptPointToPointProtocolGroup_Type(Bits):
    """Custom type l2ptPointToPointProtocolGroup based on Bits"""
    namedValues = NamedValues(
        *(("pagp", 0),
          ("lacp", 1),
          ("udld", 2))
    )

_L2ptPointToPointProtocolGroup_Type.__name__ = "Bits"
_L2ptPointToPointProtocolGroup_Object = MibTableColumn
l2ptPointToPointProtocolGroup = _L2ptPointToPointProtocolGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 3, 1, 2),
    _L2ptPointToPointProtocolGroup_Type()
)
l2ptPointToPointProtocolGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptPointToPointProtocolGroup.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 115, 3, 1, 3),
    _L2ptMode_Type()
)
l2ptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2ptMode.setStatus("mandatory")
_VlanMappingSetup_ObjectIdentity = ObjectIdentity
vlanMappingSetup = _VlanMappingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116)
)
_VlanMappingState_Type = EnabledStatus
_VlanMappingState_Object = MibScalar
vlanMappingState = _VlanMappingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 1),
    _VlanMappingState_Type()
)
vlanMappingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingState.setStatus("mandatory")
_VlanMappingPortTable_Object = MibTable
vlanMappingPortTable = _VlanMappingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 2)
)
if mibBuilder.loadTexts:
    vlanMappingPortTable.setStatus("mandatory")
_VlanMappingPortEntry_Object = MibTableRow
vlanMappingPortEntry = _VlanMappingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 2, 1)
)
vlanMappingPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanMappingPortEntry.setStatus("mandatory")
_VlanMappingPortState_Type = EnabledStatus
_VlanMappingPortState_Object = MibTableColumn
vlanMappingPortState = _VlanMappingPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 2, 1, 1),
    _VlanMappingPortState_Type()
)
vlanMappingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingPortState.setStatus("mandatory")
_VlanMappingRuleTable_Object = MibTable
vlanMappingRuleTable = _VlanMappingRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3)
)
if mibBuilder.loadTexts:
    vlanMappingRuleTable.setStatus("mandatory")
_VlanMappingRuleEntry_Object = MibTableRow
vlanMappingRuleEntry = _VlanMappingRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1)
)
vlanMappingRuleEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "vlanMappingRulePort"),
    (0, "ZYXEL-MES3500-10-MIB", "vlanMappingRuleVid"),
)
if mibBuilder.loadTexts:
    vlanMappingRuleEntry.setStatus("mandatory")
_VlanMappingRuleName_Type = DisplayString
_VlanMappingRuleName_Object = MibTableColumn
vlanMappingRuleName = _VlanMappingRuleName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 1),
    _VlanMappingRuleName_Type()
)
vlanMappingRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRuleName.setStatus("mandatory")
_VlanMappingRulePort_Type = Integer32
_VlanMappingRulePort_Object = MibTableColumn
vlanMappingRulePort = _VlanMappingRulePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 2),
    _VlanMappingRulePort_Type()
)
vlanMappingRulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMappingRulePort.setStatus("mandatory")
_VlanMappingRuleVid_Type = Integer32
_VlanMappingRuleVid_Object = MibTableColumn
vlanMappingRuleVid = _VlanMappingRuleVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 3),
    _VlanMappingRuleVid_Type()
)
vlanMappingRuleVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanMappingRuleVid.setStatus("mandatory")
_VlanMappingRuleTransVid_Type = Integer32
_VlanMappingRuleTransVid_Object = MibTableColumn
vlanMappingRuleTransVid = _VlanMappingRuleTransVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 4),
    _VlanMappingRuleTransVid_Type()
)
vlanMappingRuleTransVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRuleTransVid.setStatus("mandatory")


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
        *(("prioriry-0", 0),
          ("prioriry-1", 1),
          ("prioriry-2", 2),
          ("prioriry-3", 3),
          ("prioriry-4", 4),
          ("prioriry-5", 5),
          ("prioriry-6", 6),
          ("prioriry-7", 7))
    )


_VlanMappingRulePriority_Type.__name__ = "Integer32"
_VlanMappingRulePriority_Object = MibTableColumn
vlanMappingRulePriority = _VlanMappingRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 5),
    _VlanMappingRulePriority_Type()
)
vlanMappingRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRulePriority.setStatus("mandatory")
_VlanMappingRuleRowStatus_Type = RowStatus
_VlanMappingRuleRowStatus_Object = MibTableColumn
vlanMappingRuleRowStatus = _VlanMappingRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 6),
    _VlanMappingRuleRowStatus_Type()
)
vlanMappingRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMappingRuleRowStatus.setStatus("mandatory")


class _VlanMappingRuleDirection_Type(Integer32):
    """Custom type vlanMappingRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("ingress", 1),
          ("egress", 2))
    )


_VlanMappingRuleDirection_Type.__name__ = "Integer32"
_VlanMappingRuleDirection_Object = MibTableColumn
vlanMappingRuleDirection = _VlanMappingRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 116, 3, 1, 7),
    _VlanMappingRuleDirection_Type()
)
vlanMappingRuleDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMappingRuleDirection.setStatus("mandatory")
_TransceiverInfo_ObjectIdentity = ObjectIdentity
transceiverInfo = _TransceiverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117)
)
_TransceiverSerialInfoTable_Object = MibTable
transceiverSerialInfoTable = _TransceiverSerialInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1)
)
if mibBuilder.loadTexts:
    transceiverSerialInfoTable.setStatus("current")
_TransceiverSerialInfoEntry_Object = MibTableRow
transceiverSerialInfoEntry = _TransceiverSerialInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1)
)
transceiverSerialInfoEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "transceiverSerialInfoEntryPort"),
)
if mibBuilder.loadTexts:
    transceiverSerialInfoEntry.setStatus("current")
_TransceiverSerialInfoEntryPort_Type = Integer32
_TransceiverSerialInfoEntryPort_Object = MibTableColumn
transceiverSerialInfoEntryPort = _TransceiverSerialInfoEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 2),
    _TransceiverSerialInfoEntryStatus_Type()
)
transceiverSerialInfoEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryStatus.setStatus("current")
_TransceiverSerialInfoEntryVendor_Type = DisplayString
_TransceiverSerialInfoEntryVendor_Object = MibTableColumn
transceiverSerialInfoEntryVendor = _TransceiverSerialInfoEntryVendor_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 3),
    _TransceiverSerialInfoEntryVendor_Type()
)
transceiverSerialInfoEntryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryVendor.setStatus("current")
_TransceiverSerialInfoEntryPartNo_Type = DisplayString
_TransceiverSerialInfoEntryPartNo_Object = MibTableColumn
transceiverSerialInfoEntryPartNo = _TransceiverSerialInfoEntryPartNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 4),
    _TransceiverSerialInfoEntryPartNo_Type()
)
transceiverSerialInfoEntryPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryPartNo.setStatus("current")
_TransceiverSerialInfoEntrySerialNo_Type = DisplayString
_TransceiverSerialInfoEntrySerialNo_Object = MibTableColumn
transceiverSerialInfoEntrySerialNo = _TransceiverSerialInfoEntrySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 5),
    _TransceiverSerialInfoEntrySerialNo_Type()
)
transceiverSerialInfoEntrySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntrySerialNo.setStatus("current")
_TransceiverSerialInfoEntryRevision_Type = DisplayString
_TransceiverSerialInfoEntryRevision_Object = MibTableColumn
transceiverSerialInfoEntryRevision = _TransceiverSerialInfoEntryRevision_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 6),
    _TransceiverSerialInfoEntryRevision_Type()
)
transceiverSerialInfoEntryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryRevision.setStatus("current")
_TransceiverSerialInfoEntryDateCode_Type = DisplayString
_TransceiverSerialInfoEntryDateCode_Object = MibTableColumn
transceiverSerialInfoEntryDateCode = _TransceiverSerialInfoEntryDateCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 7),
    _TransceiverSerialInfoEntryDateCode_Type()
)
transceiverSerialInfoEntryDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryDateCode.setStatus("current")
_TransceiverSerialInfoEntryTransceiver_Type = DisplayString
_TransceiverSerialInfoEntryTransceiver_Object = MibTableColumn
transceiverSerialInfoEntryTransceiver = _TransceiverSerialInfoEntryTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 1, 1, 8),
    _TransceiverSerialInfoEntryTransceiver_Type()
)
transceiverSerialInfoEntryTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverSerialInfoEntryTransceiver.setStatus("current")
_TransceiverDdmInfoTable_Object = MibTable
transceiverDdmInfoTable = _TransceiverDdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2)
)
if mibBuilder.loadTexts:
    transceiverDdmInfoTable.setStatus("current")
_TransceiverDdmInfoEntry_Object = MibTableRow
transceiverDdmInfoEntry = _TransceiverDdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1)
)
transceiverDdmInfoEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "transceiverDdmInfoEntryPort"),
    (0, "ZYXEL-MES3500-10-MIB", "transceiverDdmInfoEntryType"),
)
if mibBuilder.loadTexts:
    transceiverDdmInfoEntry.setStatus("current")
_TransceiverDdmInfoEntryPort_Type = Integer32
_TransceiverDdmInfoEntryPort_Object = MibTableColumn
transceiverDdmInfoEntryPort = _TransceiverDdmInfoEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 1),
    _TransceiverDdmInfoEntryPort_Type()
)
transceiverDdmInfoEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryPort.setStatus("current")
_TransceiverDdmInfoEntryType_Type = Integer32
_TransceiverDdmInfoEntryType_Object = MibTableColumn
transceiverDdmInfoEntryType = _TransceiverDdmInfoEntryType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 2),
    _TransceiverDdmInfoEntryType_Type()
)
transceiverDdmInfoEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryType.setStatus("current")
_TransceiverDdmInfoEntryAlarmMax_Type = Integer32
_TransceiverDdmInfoEntryAlarmMax_Object = MibTableColumn
transceiverDdmInfoEntryAlarmMax = _TransceiverDdmInfoEntryAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 3),
    _TransceiverDdmInfoEntryAlarmMax_Type()
)
transceiverDdmInfoEntryAlarmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMax.setStatus("current")
_TransceiverDdmInfoEntryAlarmMin_Type = Integer32
_TransceiverDdmInfoEntryAlarmMin_Object = MibTableColumn
transceiverDdmInfoEntryAlarmMin = _TransceiverDdmInfoEntryAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 4),
    _TransceiverDdmInfoEntryAlarmMin_Type()
)
transceiverDdmInfoEntryAlarmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryAlarmMin.setStatus("current")
_TransceiverDdmInfoEntryWarnMax_Type = Integer32
_TransceiverDdmInfoEntryWarnMax_Object = MibTableColumn
transceiverDdmInfoEntryWarnMax = _TransceiverDdmInfoEntryWarnMax_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 5),
    _TransceiverDdmInfoEntryWarnMax_Type()
)
transceiverDdmInfoEntryWarnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMax.setStatus("current")
_TransceiverDdmInfoEntryWarnMin_Type = Integer32
_TransceiverDdmInfoEntryWarnMin_Object = MibTableColumn
transceiverDdmInfoEntryWarnMin = _TransceiverDdmInfoEntryWarnMin_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 6),
    _TransceiverDdmInfoEntryWarnMin_Type()
)
transceiverDdmInfoEntryWarnMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryWarnMin.setStatus("current")
_TransceiverDdmInfoEntryCurrent_Type = Integer32
_TransceiverDdmInfoEntryCurrent_Object = MibTableColumn
transceiverDdmInfoEntryCurrent = _TransceiverDdmInfoEntryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 7),
    _TransceiverDdmInfoEntryCurrent_Type()
)
transceiverDdmInfoEntryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryCurrent.setStatus("current")
_TransceiverDdmInfoEntryDescription_Type = DisplayString
_TransceiverDdmInfoEntryDescription_Object = MibTableColumn
transceiverDdmInfoEntryDescription = _TransceiverDdmInfoEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 117, 2, 1, 8),
    _TransceiverDdmInfoEntryDescription_Type()
)
transceiverDdmInfoEntryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmInfoEntryDescription.setStatus("current")
_Dot3OamOuld_ObjectIdentity = ObjectIdentity
dot3OamOuld = _Dot3OamOuld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118)
)
_Dot3OamSetup_ObjectIdentity = ObjectIdentity
dot3OamSetup = _Dot3OamSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 1)
)
_Dot3OamState_Type = EnabledStatus
_Dot3OamState_Object = MibScalar
dot3OamState = _Dot3OamState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 1, 1),
    _Dot3OamState_Type()
)
dot3OamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamState.setStatus("current")
_Dot3OamPortTable_Object = MibTable
dot3OamPortTable = _Dot3OamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 1, 2)
)
if mibBuilder.loadTexts:
    dot3OamPortTable.setStatus("current")
_Dot3OamPortEntry_Object = MibTableRow
dot3OamPortEntry = _Dot3OamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 1, 2, 1)
)
dot3OamPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamPortEntry.setStatus("current")
_Dot3OamPortState_Type = EnabledStatus
_Dot3OamPortState_Object = MibTableColumn
dot3OamPortState = _Dot3OamPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 1, 2, 1, 1),
    _Dot3OamPortState_Type()
)
dot3OamPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamPortState.setStatus("current")


class _Dot3OamFunctionsSupported_Type(Bits):
    """Custom type dot3OamFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_Dot3OamFunctionsSupported_Type.__name__ = "Bits"
_Dot3OamFunctionsSupported_Object = MibTableColumn
dot3OamFunctionsSupported = _Dot3OamFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 1, 2, 1, 2),
    _Dot3OamFunctionsSupported_Type()
)
dot3OamFunctionsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamFunctionsSupported.setStatus("current")
_Dot3OamOuldSetup_ObjectIdentity = ObjectIdentity
dot3OamOuldSetup = _Dot3OamOuldSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2)
)


class _Dot3OamOuldDiscoveryTimer_Type(Integer32):
    """Custom type dot3OamOuldDiscoveryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Dot3OamOuldDiscoveryTimer_Type.__name__ = "Integer32"
_Dot3OamOuldDiscoveryTimer_Object = MibScalar
dot3OamOuldDiscoveryTimer = _Dot3OamOuldDiscoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2, 1),
    _Dot3OamOuldDiscoveryTimer_Type()
)
dot3OamOuldDiscoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamOuldDiscoveryTimer.setStatus("current")


class _Dot3OamOuldRecoveryTimer_Type(Integer32):
    """Custom type dot3OamOuldRecoveryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_Dot3OamOuldRecoveryTimer_Type.__name__ = "Integer32"
_Dot3OamOuldRecoveryTimer_Object = MibScalar
dot3OamOuldRecoveryTimer = _Dot3OamOuldRecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2, 2),
    _Dot3OamOuldRecoveryTimer_Type()
)
dot3OamOuldRecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamOuldRecoveryTimer.setStatus("current")
_Dot3OamOuldSetupPortTable_Object = MibTable
dot3OamOuldSetupPortTable = _Dot3OamOuldSetupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2, 3)
)
if mibBuilder.loadTexts:
    dot3OamOuldSetupPortTable.setStatus("current")
_Dot3OamOuldSetupPortEntry_Object = MibTableRow
dot3OamOuldSetupPortEntry = _Dot3OamOuldSetupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2, 3, 1)
)
dot3OamOuldSetupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamOuldSetupPortEntry.setStatus("current")
_Dot3OamOuldState_Type = EnabledStatus
_Dot3OamOuldState_Object = MibTableColumn
dot3OamOuldState = _Dot3OamOuldState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2, 3, 1, 1),
    _Dot3OamOuldState_Type()
)
dot3OamOuldState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamOuldState.setStatus("current")
_Dot3OamOuldAggressiveMode_Type = EnabledStatus
_Dot3OamOuldAggressiveMode_Object = MibTableColumn
dot3OamOuldAggressiveMode = _Dot3OamOuldAggressiveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 2, 3, 1, 2),
    _Dot3OamOuldAggressiveMode_Type()
)
dot3OamOuldAggressiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3OamOuldAggressiveMode.setStatus("current")
_Dot3OamOuldStatus_ObjectIdentity = ObjectIdentity
dot3OamOuldStatus = _Dot3OamOuldStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 3)
)
_Dot3OamOuldStatusPortTable_Object = MibTable
dot3OamOuldStatusPortTable = _Dot3OamOuldStatusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 3, 1)
)
if mibBuilder.loadTexts:
    dot3OamOuldStatusPortTable.setStatus("current")
_Dot3OamOuldStatusPortEntry_Object = MibTableRow
dot3OamOuldStatusPortEntry = _Dot3OamOuldStatusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 3, 1, 1)
)
dot3OamOuldStatusPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot3OamOuldStatusPortEntry.setStatus("current")
_Dot3OamOuldResult_Type = DisplayString
_Dot3OamOuldResult_Object = MibTableColumn
dot3OamOuldResult = _Dot3OamOuldResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 3, 1, 1, 1),
    _Dot3OamOuldResult_Type()
)
dot3OamOuldResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamOuldResult.setStatus("current")
_Dot3OamOuldLinkStatus_Type = DisplayString
_Dot3OamOuldLinkStatus_Object = MibTableColumn
dot3OamOuldLinkStatus = _Dot3OamOuldLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 3, 1, 1, 2),
    _Dot3OamOuldLinkStatus_Type()
)
dot3OamOuldLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamOuldLinkStatus.setStatus("current")
_Dot3OamOuldCountdown_Type = DisplayString
_Dot3OamOuldCountdown_Object = MibTableColumn
dot3OamOuldCountdown = _Dot3OamOuldCountdown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 118, 3, 1, 1, 3),
    _Dot3OamOuldCountdown_Type()
)
dot3OamOuldCountdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3OamOuldCountdown.setStatus("current")
_Dot1agCfmSetup_ObjectIdentity = ObjectIdentity
dot1agCfmSetup = _Dot1agCfmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 119)
)
_Dot1agCfmMIBObjects_ObjectIdentity = ObjectIdentity
dot1agCfmMIBObjects = _Dot1agCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 119, 1)
)
_Dot1agCfmMep_ObjectIdentity = ObjectIdentity
dot1agCfmMep = _Dot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 119, 1, 7)
)
_Zyswdot1agCfmMepTable_Object = MibTable
zyswdot1agCfmMepTable = _Zyswdot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 119, 1, 7, 1)
)
if mibBuilder.loadTexts:
    zyswdot1agCfmMepTable.setStatus("mandatory")
_Zyswdot1agCfmMepEntry_Object = MibTableRow
zyswdot1agCfmMepEntry = _Zyswdot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 119, 1, 7, 1, 1)
)
zyswdot1agCfmMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    zyswdot1agCfmMepEntry.setStatus("mandatory")


class _Zyswdot1agCfmMepTransmitLbmDataTlvSize_Type(Unsigned32):
    """Custom type zyswdot1agCfmMepTransmitLbmDataTlvSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_Zyswdot1agCfmMepTransmitLbmDataTlvSize_Type.__name__ = "Unsigned32"
_Zyswdot1agCfmMepTransmitLbmDataTlvSize_Object = MibTableColumn
zyswdot1agCfmMepTransmitLbmDataTlvSize = _Zyswdot1agCfmMepTransmitLbmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 119, 1, 7, 1, 1, 1),
    _Zyswdot1agCfmMepTransmitLbmDataTlvSize_Type()
)
zyswdot1agCfmMepTransmitLbmDataTlvSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyswdot1agCfmMepTransmitLbmDataTlvSize.setStatus("mandatory")
_SFlowSetup_ObjectIdentity = ObjectIdentity
sFlowSetup = _SFlowSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123)
)
_SFlowState_Type = EnabledStatus
_SFlowState_Object = MibScalar
sFlowState = _SFlowState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 1),
    _SFlowState_Type()
)
sFlowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowState.setStatus("mandatory")
_SFlowCollectorTable_Object = MibTable
sFlowCollectorTable = _SFlowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 2)
)
if mibBuilder.loadTexts:
    sFlowCollectorTable.setStatus("current")
_SFlowCollectorEntry_Object = MibTableRow
sFlowCollectorEntry = _SFlowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 2, 1)
)
sFlowCollectorEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "sFlowCollectorAddressType"),
    (0, "ZYXEL-MES3500-10-MIB", "sFlowCollectorAddress"),
)
if mibBuilder.loadTexts:
    sFlowCollectorEntry.setStatus("current")
_SFlowCollectorAddressType_Type = InetAddressType
_SFlowCollectorAddressType_Object = MibTableColumn
sFlowCollectorAddressType = _SFlowCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 2, 1, 1),
    _SFlowCollectorAddressType_Type()
)
sFlowCollectorAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowCollectorAddressType.setStatus("current")
_SFlowCollectorAddress_Type = InetAddress
_SFlowCollectorAddress_Object = MibTableColumn
sFlowCollectorAddress = _SFlowCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 2, 1, 2),
    _SFlowCollectorAddress_Type()
)
sFlowCollectorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowCollectorAddress.setStatus("current")


class _SFlowCollectorUdpPort_Type(Unsigned32):
    """Custom type sFlowCollectorUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SFlowCollectorUdpPort_Type.__name__ = "Unsigned32"
_SFlowCollectorUdpPort_Object = MibTableColumn
sFlowCollectorUdpPort = _SFlowCollectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 2, 1, 3),
    _SFlowCollectorUdpPort_Type()
)
sFlowCollectorUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCollectorUdpPort.setStatus("current")
_SFlowCollectorRowStatus_Type = RowStatus
_SFlowCollectorRowStatus_Object = MibTableColumn
sFlowCollectorRowStatus = _SFlowCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 2, 1, 4),
    _SFlowCollectorRowStatus_Type()
)
sFlowCollectorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowCollectorRowStatus.setStatus("current")
_SFlowPortTable_Object = MibTable
sFlowPortTable = _SFlowPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 3)
)
if mibBuilder.loadTexts:
    sFlowPortTable.setStatus("current")
_SFlowPortEntry_Object = MibTableRow
sFlowPortEntry = _SFlowPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 3, 1)
)
sFlowPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    sFlowPortEntry.setStatus("current")
_SFlowPortState_Type = EnabledStatus
_SFlowPortState_Object = MibTableColumn
sFlowPortState = _SFlowPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 3, 1, 1),
    _SFlowPortState_Type()
)
sFlowPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowPortState.setStatus("mandatory")
_SFlowPortCollectorTable_Object = MibTable
sFlowPortCollectorTable = _SFlowPortCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4)
)
if mibBuilder.loadTexts:
    sFlowPortCollectorTable.setStatus("current")
_SFlowPortCollectorEntry_Object = MibTableRow
sFlowPortCollectorEntry = _SFlowPortCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4, 1)
)
sFlowPortCollectorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-MES3500-10-MIB", "sFlowPortCollectorAddressType"),
    (0, "ZYXEL-MES3500-10-MIB", "sFlowPortCollectorAddress"),
)
if mibBuilder.loadTexts:
    sFlowPortCollectorEntry.setStatus("current")
_SFlowPortCollectorAddressType_Type = InetAddressType
_SFlowPortCollectorAddressType_Object = MibTableColumn
sFlowPortCollectorAddressType = _SFlowPortCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4, 1, 1),
    _SFlowPortCollectorAddressType_Type()
)
sFlowPortCollectorAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowPortCollectorAddressType.setStatus("current")
_SFlowPortCollectorAddress_Type = InetAddress
_SFlowPortCollectorAddress_Object = MibTableColumn
sFlowPortCollectorAddress = _SFlowPortCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4, 1, 2),
    _SFlowPortCollectorAddress_Type()
)
sFlowPortCollectorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFlowPortCollectorAddress.setStatus("current")


class _SFlowPortCollectorSampleRate_Type(Unsigned32):
    """Custom type sFlowPortCollectorSampleRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_SFlowPortCollectorSampleRate_Type.__name__ = "Unsigned32"
_SFlowPortCollectorSampleRate_Object = MibTableColumn
sFlowPortCollectorSampleRate = _SFlowPortCollectorSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4, 1, 3),
    _SFlowPortCollectorSampleRate_Type()
)
sFlowPortCollectorSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowPortCollectorSampleRate.setStatus("current")


class _SFlowPortCollectorPollInterval_Type(Unsigned32):
    """Custom type sFlowPortCollectorPollInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 120),
    )


_SFlowPortCollectorPollInterval_Type.__name__ = "Unsigned32"
_SFlowPortCollectorPollInterval_Object = MibTableColumn
sFlowPortCollectorPollInterval = _SFlowPortCollectorPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4, 1, 4),
    _SFlowPortCollectorPollInterval_Type()
)
sFlowPortCollectorPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowPortCollectorPollInterval.setStatus("current")
_SFlowPortCollectorRowStatus_Type = RowStatus
_SFlowPortCollectorRowStatus_Object = MibTableColumn
sFlowPortCollectorRowStatus = _SFlowPortCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 123, 4, 1, 5),
    _SFlowPortCollectorRowStatus_Type()
)
sFlowPortCollectorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowPortCollectorRowStatus.setStatus("current")
_SysMemoryPool_ObjectIdentity = ObjectIdentity
sysMemoryPool = _SysMemoryPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124)
)
_SysMemoryPoolTable_Object = MibTable
sysMemoryPoolTable = _SysMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1)
)
if mibBuilder.loadTexts:
    sysMemoryPoolTable.setStatus("current")
_SysMemoryPoolEntry_Object = MibTableRow
sysMemoryPoolEntry = _SysMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1, 1)
)
sysMemoryPoolEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "sysMemoryPoolId"),
)
if mibBuilder.loadTexts:
    sysMemoryPoolEntry.setStatus("current")
_SysMemoryPoolId_Type = Unsigned32
_SysMemoryPoolId_Object = MibTableColumn
sysMemoryPoolId = _SysMemoryPoolId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1, 1, 1),
    _SysMemoryPoolId_Type()
)
sysMemoryPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolId.setStatus("current")


class _SysMemoryPoolName_Type(OctetString):
    """Custom type sysMemoryPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysMemoryPoolName_Type.__name__ = "OctetString"
_SysMemoryPoolName_Object = MibTableColumn
sysMemoryPoolName = _SysMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1, 1, 2),
    _SysMemoryPoolName_Type()
)
sysMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolName.setStatus("current")
_SysMemoryPoolTotal_Type = Unsigned32
_SysMemoryPoolTotal_Object = MibTableColumn
sysMemoryPoolTotal = _SysMemoryPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1, 1, 3),
    _SysMemoryPoolTotal_Type()
)
sysMemoryPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolTotal.setStatus("current")
_SysMemoryPoolUsed_Type = Unsigned32
_SysMemoryPoolUsed_Object = MibTableColumn
sysMemoryPoolUsed = _SysMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1, 1, 4),
    _SysMemoryPoolUsed_Type()
)
sysMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolUsed.setStatus("current")


class _SysMemoryPoolUtil_Type(Unsigned32):
    """Custom type sysMemoryPoolUtil based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMemoryPoolUtil_Type.__name__ = "Unsigned32"
_SysMemoryPoolUtil_Object = MibTableColumn
sysMemoryPoolUtil = _SysMemoryPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 124, 1, 1, 5),
    _SysMemoryPoolUtil_Type()
)
sysMemoryPoolUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemoryPoolUtil.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125)
)
_PppoeIaSetup_ObjectIdentity = ObjectIdentity
pppoeIaSetup = _PppoeIaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1)
)
_PppoeIaState_Type = EnabledStatus
_PppoeIaState_Object = MibScalar
pppoeIaState = _PppoeIaState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 1),
    _PppoeIaState_Type()
)
pppoeIaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaState.setStatus("mandatory")
_PppoeIaAccessNodeIdentifierString_Type = DisplayString
_PppoeIaAccessNodeIdentifierString_Object = MibScalar
pppoeIaAccessNodeIdentifierString = _PppoeIaAccessNodeIdentifierString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 2),
    _PppoeIaAccessNodeIdentifierString_Type()
)
pppoeIaAccessNodeIdentifierString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaAccessNodeIdentifierString.setStatus("mandatory")
_PppoeIaFlexibleCircuitIDSyntaxActive_Type = EnabledStatus
_PppoeIaFlexibleCircuitIDSyntaxActive_Object = MibScalar
pppoeIaFlexibleCircuitIDSyntaxActive = _PppoeIaFlexibleCircuitIDSyntaxActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 3),
    _PppoeIaFlexibleCircuitIDSyntaxActive_Type()
)
pppoeIaFlexibleCircuitIDSyntaxActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaFlexibleCircuitIDSyntaxActive.setStatus("mandatory")
_PppoeIaFlexibleCircuitIDSyntaxIdentifierString_Type = DisplayString
_PppoeIaFlexibleCircuitIDSyntaxIdentifierString_Object = MibScalar
pppoeIaFlexibleCircuitIDSyntaxIdentifierString = _PppoeIaFlexibleCircuitIDSyntaxIdentifierString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 4),
    _PppoeIaFlexibleCircuitIDSyntaxIdentifierString_Type()
)
pppoeIaFlexibleCircuitIDSyntaxIdentifierString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaFlexibleCircuitIDSyntaxIdentifierString.setStatus("mandatory")


class _PppoeIaFlexibleCircuitIDSyntaxOption_Type(Integer32):
    """Custom type pppoeIaFlexibleCircuitIDSyntaxOption based on Integer32"""
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
        *(("s", 1),
          ("p", 2),
          ("v", 3),
          ("sp", 4),
          ("sv", 5),
          ("pv", 6),
          ("spv", 7))
    )


_PppoeIaFlexibleCircuitIDSyntaxOption_Type.__name__ = "Integer32"
_PppoeIaFlexibleCircuitIDSyntaxOption_Object = MibScalar
pppoeIaFlexibleCircuitIDSyntaxOption = _PppoeIaFlexibleCircuitIDSyntaxOption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 5),
    _PppoeIaFlexibleCircuitIDSyntaxOption_Type()
)
pppoeIaFlexibleCircuitIDSyntaxOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaFlexibleCircuitIDSyntaxOption.setStatus("mandatory")


class _PppoeIaFlexibleCircuitIDSyntaxDelimiter_Type(Integer32):
    """Custom type pppoeIaFlexibleCircuitIDSyntaxDelimiter based on Integer32"""
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
        *(("pound-sign", 1),
          ("dot", 2),
          ("comma", 3),
          ("semicolon", 4),
          ("slash", 5),
          ("space", 6))
    )


_PppoeIaFlexibleCircuitIDSyntaxDelimiter_Type.__name__ = "Integer32"
_PppoeIaFlexibleCircuitIDSyntaxDelimiter_Object = MibScalar
pppoeIaFlexibleCircuitIDSyntaxDelimiter = _PppoeIaFlexibleCircuitIDSyntaxDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 6),
    _PppoeIaFlexibleCircuitIDSyntaxDelimiter_Type()
)
pppoeIaFlexibleCircuitIDSyntaxDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaFlexibleCircuitIDSyntaxDelimiter.setStatus("mandatory")
_PppoeIaPortTable_Object = MibTable
pppoeIaPortTable = _PppoeIaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 7)
)
if mibBuilder.loadTexts:
    pppoeIaPortTable.setStatus("mandatory")
_PppoeIaPortEntry_Object = MibTableRow
pppoeIaPortEntry = _PppoeIaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 7, 1)
)
pppoeIaPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    pppoeIaPortEntry.setStatus("mandatory")
_PppoeIaPortEntryPort_Type = Integer32
_PppoeIaPortEntryPort_Object = MibTableColumn
pppoeIaPortEntryPort = _PppoeIaPortEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 7, 1, 1),
    _PppoeIaPortEntryPort_Type()
)
pppoeIaPortEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaPortEntryPort.setStatus("mandatory")
_PppoeIaPortEntryTrust_Type = EnabledStatus
_PppoeIaPortEntryTrust_Object = MibTableColumn
pppoeIaPortEntryTrust = _PppoeIaPortEntryTrust_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 7, 1, 2),
    _PppoeIaPortEntryTrust_Type()
)
pppoeIaPortEntryTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaPortEntryTrust.setStatus("mandatory")
_PppoeIaPortEntryCircuitIDString_Type = DisplayString
_PppoeIaPortEntryCircuitIDString_Object = MibTableColumn
pppoeIaPortEntryCircuitIDString = _PppoeIaPortEntryCircuitIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 7, 1, 3),
    _PppoeIaPortEntryCircuitIDString_Type()
)
pppoeIaPortEntryCircuitIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaPortEntryCircuitIDString.setStatus("mandatory")
_PppoeIaPortEntryRemoteIDString_Type = DisplayString
_PppoeIaPortEntryRemoteIDString_Object = MibTableColumn
pppoeIaPortEntryRemoteIDString = _PppoeIaPortEntryRemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 7, 1, 4),
    _PppoeIaPortEntryRemoteIDString_Type()
)
pppoeIaPortEntryRemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaPortEntryRemoteIDString.setStatus("mandatory")
_PppoeIaVlanTable_Object = MibTable
pppoeIaVlanTable = _PppoeIaVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 8)
)
if mibBuilder.loadTexts:
    pppoeIaVlanTable.setStatus("mandatory")
_PppoeIaVlanEntry_Object = MibTableRow
pppoeIaVlanEntry = _PppoeIaVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 8, 1)
)
pppoeIaVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "pppoeIaVlanEntryVid"),
)
if mibBuilder.loadTexts:
    pppoeIaVlanEntry.setStatus("mandatory")


class _PppoeIaVlanEntryVid_Type(Integer32):
    """Custom type pppoeIaVlanEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PppoeIaVlanEntryVid_Type.__name__ = "Integer32"
_PppoeIaVlanEntryVid_Object = MibTableColumn
pppoeIaVlanEntryVid = _PppoeIaVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 8, 1, 1),
    _PppoeIaVlanEntryVid_Type()
)
pppoeIaVlanEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryVid.setStatus("mandatory")
_PppoeIaVlanEntryCircuitID_Type = EnabledStatus
_PppoeIaVlanEntryCircuitID_Object = MibTableColumn
pppoeIaVlanEntryCircuitID = _PppoeIaVlanEntryCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 8, 1, 2),
    _PppoeIaVlanEntryCircuitID_Type()
)
pppoeIaVlanEntryCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryCircuitID.setStatus("mandatory")
_PppoeIaVlanEntryRemoteID_Type = EnabledStatus
_PppoeIaVlanEntryRemoteID_Object = MibTableColumn
pppoeIaVlanEntryRemoteID = _PppoeIaVlanEntryRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 8, 1, 3),
    _PppoeIaVlanEntryRemoteID_Type()
)
pppoeIaVlanEntryRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryRemoteID.setStatus("mandatory")
_PppoeIaVlanEntryRowStatus_Type = RowStatus
_PppoeIaVlanEntryRowStatus_Object = MibTableColumn
pppoeIaVlanEntryRowStatus = _PppoeIaVlanEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 8, 1, 4),
    _PppoeIaVlanEntryRowStatus_Type()
)
pppoeIaVlanEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeIaVlanEntryRowStatus.setStatus("mandatory")
_PppoeIaPortVlanTable_Object = MibTable
pppoeIaPortVlanTable = _PppoeIaPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9)
)
if mibBuilder.loadTexts:
    pppoeIaPortVlanTable.setStatus("mandatory")
_PppoeIaPortVlanEntry_Object = MibTableRow
pppoeIaPortVlanEntry = _PppoeIaPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9, 1)
)
pppoeIaPortVlanEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "pppoeIaPortVlanEntryPort"),
    (0, "ZYXEL-MES3500-10-MIB", "pppoeIaPortVlanEntryVid"),
)
if mibBuilder.loadTexts:
    pppoeIaPortVlanEntry.setStatus("mandatory")
_PppoeIaPortVlanEntryPort_Type = Integer32
_PppoeIaPortVlanEntryPort_Object = MibTableColumn
pppoeIaPortVlanEntryPort = _PppoeIaPortVlanEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9, 1, 1),
    _PppoeIaPortVlanEntryPort_Type()
)
pppoeIaPortVlanEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaPortVlanEntryPort.setStatus("mandatory")
_PppoeIaPortVlanEntryVid_Type = Integer32
_PppoeIaPortVlanEntryVid_Object = MibTableColumn
pppoeIaPortVlanEntryVid = _PppoeIaPortVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9, 1, 2),
    _PppoeIaPortVlanEntryVid_Type()
)
pppoeIaPortVlanEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIaPortVlanEntryVid.setStatus("mandatory")
_PppoeIaPortVlanEntryCircuitIDString_Type = DisplayString
_PppoeIaPortVlanEntryCircuitIDString_Object = MibTableColumn
pppoeIaPortVlanEntryCircuitIDString = _PppoeIaPortVlanEntryCircuitIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9, 1, 3),
    _PppoeIaPortVlanEntryCircuitIDString_Type()
)
pppoeIaPortVlanEntryCircuitIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaPortVlanEntryCircuitIDString.setStatus("mandatory")
_PppoeIaPortVlanEntryRemoteIDString_Type = DisplayString
_PppoeIaPortVlanEntryRemoteIDString_Object = MibTableColumn
pppoeIaPortVlanEntryRemoteIDString = _PppoeIaPortVlanEntryRemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9, 1, 4),
    _PppoeIaPortVlanEntryRemoteIDString_Type()
)
pppoeIaPortVlanEntryRemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaPortVlanEntryRemoteIDString.setStatus("mandatory")
_PppoeIaPortVlanEntryRowStatus_Type = RowStatus
_PppoeIaPortVlanEntryRowStatus_Object = MibTableColumn
pppoeIaPortVlanEntryRowStatus = _PppoeIaPortVlanEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 9, 1, 5),
    _PppoeIaPortVlanEntryRowStatus_Type()
)
pppoeIaPortVlanEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppoeIaPortVlanEntryRowStatus.setStatus("mandatory")
_PppoeIaFlexibleCircuitIDSyntaxIdentifierStringType_Type = EnabledStatus
_PppoeIaFlexibleCircuitIDSyntaxIdentifierStringType_Object = MibScalar
pppoeIaFlexibleCircuitIDSyntaxIdentifierStringType = _PppoeIaFlexibleCircuitIDSyntaxIdentifierStringType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 125, 1, 10),
    _PppoeIaFlexibleCircuitIDSyntaxIdentifierStringType_Type()
)
pppoeIaFlexibleCircuitIDSyntaxIdentifierStringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeIaFlexibleCircuitIDSyntaxIdentifierStringType.setStatus("mandatory")
_Errdisable_ObjectIdentity = ObjectIdentity
errdisable = _Errdisable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130)
)
_Recovery_ObjectIdentity = ObjectIdentity
recovery = _Recovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1)
)
_ErrdisableRecoverySetup_ObjectIdentity = ObjectIdentity
errdisableRecoverySetup = _ErrdisableRecoverySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1)
)
_ErrdisableRecoveryState_Type = EnabledStatus
_ErrdisableRecoveryState_Object = MibScalar
errdisableRecoveryState = _ErrdisableRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 1),
    _ErrdisableRecoveryState_Type()
)
errdisableRecoveryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableRecoveryState.setStatus("mandatory")
_ErrdisableRecoveryReasonTable_Object = MibTable
errdisableRecoveryReasonTable = _ErrdisableRecoveryReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 2)
)
if mibBuilder.loadTexts:
    errdisableRecoveryReasonTable.setStatus("mandatory")
_ErrdisableRecoveryReasonEntry_Object = MibTableRow
errdisableRecoveryReasonEntry = _ErrdisableRecoveryReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 2, 1)
)
errdisableRecoveryReasonEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "errdisableRecoveryReason"),
)
if mibBuilder.loadTexts:
    errdisableRecoveryReasonEntry.setStatus("mandatory")


class _ErrdisableRecoveryReason_Type(Integer32):
    """Custom type errdisableRecoveryReason based on Integer32"""
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
        *(("loopguard", 0),
          ("arp", 1),
          ("bpdu", 2),
          ("igmp", 3))
    )


_ErrdisableRecoveryReason_Type.__name__ = "Integer32"
_ErrdisableRecoveryReason_Object = MibTableColumn
errdisableRecoveryReason = _ErrdisableRecoveryReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 2, 1, 1),
    _ErrdisableRecoveryReason_Type()
)
errdisableRecoveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryReason.setStatus("mandatory")


class _ErrdisableRecoveryReasonActive_Type(Integer32):
    """Custom type errdisableRecoveryReasonActive based on Integer32"""
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


_ErrdisableRecoveryReasonActive_Type.__name__ = "Integer32"
_ErrdisableRecoveryReasonActive_Object = MibTableColumn
errdisableRecoveryReasonActive = _ErrdisableRecoveryReasonActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 2, 1, 2),
    _ErrdisableRecoveryReasonActive_Type()
)
errdisableRecoveryReasonActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableRecoveryReasonActive.setStatus("mandatory")


class _ErrdisableRecoveryReasonInterval_Type(Integer32):
    """Custom type errdisableRecoveryReasonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2592000),
    )


_ErrdisableRecoveryReasonInterval_Type.__name__ = "Integer32"
_ErrdisableRecoveryReasonInterval_Object = MibTableColumn
errdisableRecoveryReasonInterval = _ErrdisableRecoveryReasonInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 2, 1, 3),
    _ErrdisableRecoveryReasonInterval_Type()
)
errdisableRecoveryReasonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableRecoveryReasonInterval.setStatus("mandatory")
_ErrdisableRecoveryIfStatusTable_Object = MibTable
errdisableRecoveryIfStatusTable = _ErrdisableRecoveryIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 3)
)
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusTable.setStatus("mandatory")
_ErrdisableRecoveryIfStatusEntry_Object = MibTableRow
errdisableRecoveryIfStatusEntry = _ErrdisableRecoveryIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 3, 1)
)
errdisableRecoveryIfStatusEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "errdisableRecoveryIfStatusReason"),
    (0, "ZYXEL-MES3500-10-MIB", "errdisableRecoveryIfStatusPort"),
)
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusEntry.setStatus("mandatory")


class _ErrdisableRecoveryIfStatusReason_Type(Integer32):
    """Custom type errdisableRecoveryIfStatusReason based on Integer32"""
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
        *(("loopguard", 0),
          ("arp", 1),
          ("bpdu", 2),
          ("igmp", 3))
    )


_ErrdisableRecoveryIfStatusReason_Type.__name__ = "Integer32"
_ErrdisableRecoveryIfStatusReason_Object = MibTableColumn
errdisableRecoveryIfStatusReason = _ErrdisableRecoveryIfStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 3, 1, 1),
    _ErrdisableRecoveryIfStatusReason_Type()
)
errdisableRecoveryIfStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusReason.setStatus("mandatory")
_ErrdisableRecoveryIfStatusPort_Type = Integer32
_ErrdisableRecoveryIfStatusPort_Object = MibTableColumn
errdisableRecoveryIfStatusPort = _ErrdisableRecoveryIfStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 3, 1, 2),
    _ErrdisableRecoveryIfStatusPort_Type()
)
errdisableRecoveryIfStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusPort.setStatus("mandatory")


class _ErrdisableRecoveryIfStatusTimeToRecover_Type(Integer32):
    """Custom type errdisableRecoveryIfStatusTimeToRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 2592000),
    )


_ErrdisableRecoveryIfStatusTimeToRecover_Type.__name__ = "Integer32"
_ErrdisableRecoveryIfStatusTimeToRecover_Object = MibTableColumn
errdisableRecoveryIfStatusTimeToRecover = _ErrdisableRecoveryIfStatusTimeToRecover_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 1, 1, 3, 1, 3),
    _ErrdisableRecoveryIfStatusTimeToRecover_Type()
)
errdisableRecoveryIfStatusTimeToRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableRecoveryIfStatusTimeToRecover.setStatus("mandatory")
_Detect_ObjectIdentity = ObjectIdentity
detect = _Detect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 2)
)
_ErrdisableDetectReasonTable_Object = MibTable
errdisableDetectReasonTable = _ErrdisableDetectReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 2, 1)
)
if mibBuilder.loadTexts:
    errdisableDetectReasonTable.setStatus("mandatory")
_ErrdisableDetectReasonEntry_Object = MibTableRow
errdisableDetectReasonEntry = _ErrdisableDetectReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 2, 1, 1)
)
errdisableDetectReasonEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "errdisableDetectReason"),
)
if mibBuilder.loadTexts:
    errdisableDetectReasonEntry.setStatus("mandatory")


class _ErrdisableDetectReason_Type(Integer32):
    """Custom type errdisableDetectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3))
    )


_ErrdisableDetectReason_Type.__name__ = "Integer32"
_ErrdisableDetectReason_Object = MibTableColumn
errdisableDetectReason = _ErrdisableDetectReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 2, 1, 1, 1),
    _ErrdisableDetectReason_Type()
)
errdisableDetectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableDetectReason.setStatus("mandatory")
_ErrdisableDetectReasonEnable_Type = EnabledStatus
_ErrdisableDetectReasonEnable_Object = MibTableColumn
errdisableDetectReasonEnable = _ErrdisableDetectReasonEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 2, 1, 1, 2),
    _ErrdisableDetectReasonEnable_Type()
)
errdisableDetectReasonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableDetectReasonEnable.setStatus("mandatory")


class _ErrdisableDetectReasonMode_Type(Integer32):
    """Custom type errdisableDetectReasonMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive-port", 1),
          ("inactive-reason", 2),
          ("rate-limitation", 3))
    )


_ErrdisableDetectReasonMode_Type.__name__ = "Integer32"
_ErrdisableDetectReasonMode_Object = MibTableColumn
errdisableDetectReasonMode = _ErrdisableDetectReasonMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 2, 1, 1, 3),
    _ErrdisableDetectReasonMode_Type()
)
errdisableDetectReasonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errdisableDetectReasonMode.setStatus("mandatory")
_ErrdisableTrapInfoObject_ObjectIdentity = ObjectIdentity
errdisableTrapInfoObject = _ErrdisableTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 3)
)
_ErrdisableTrapPort_Type = Integer32
_ErrdisableTrapPort_Object = MibScalar
errdisableTrapPort = _ErrdisableTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 3, 1),
    _ErrdisableTrapPort_Type()
)
errdisableTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableTrapPort.setStatus("mandatory")


class _ErrdisableTrapReason_Type(Integer32):
    """Custom type errdisableTrapReason based on Integer32"""
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
        *(("loopguard", 0),
          ("arp", 1),
          ("bpdu", 2),
          ("igmp", 3),
          ("stormcontrol", 4),
          ("portsecurity", 5))
    )


_ErrdisableTrapReason_Type.__name__ = "Integer32"
_ErrdisableTrapReason_Object = MibScalar
errdisableTrapReason = _ErrdisableTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 3, 2),
    _ErrdisableTrapReason_Type()
)
errdisableTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableTrapReason.setStatus("mandatory")


class _ErrdisableTrapMode_Type(Integer32):
    """Custom type errdisableTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive-port", 0),
          ("inactive-reason", 1),
          ("rate-limitation", 2))
    )


_ErrdisableTrapMode_Type.__name__ = "Integer32"
_ErrdisableTrapMode_Object = MibScalar
errdisableTrapMode = _ErrdisableTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 3, 3),
    _ErrdisableTrapMode_Type()
)
errdisableTrapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errdisableTrapMode.setStatus("mandatory")
_ErrdisableTrapNotifications_ObjectIdentity = ObjectIdentity
errdisableTrapNotifications = _ErrdisableTrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 4)
)
_CpuProtectionSetup_ObjectIdentity = ObjectIdentity
cpuProtectionSetup = _CpuProtectionSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 131)
)
_CpuProtectionTable_Object = MibTable
cpuProtectionTable = _CpuProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 131, 1)
)
if mibBuilder.loadTexts:
    cpuProtectionTable.setStatus("mandatory")
_CpuProtectionEntry_Object = MibTableRow
cpuProtectionEntry = _CpuProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 131, 1, 1)
)
cpuProtectionEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "cpuProtectionPort"),
    (0, "ZYXEL-MES3500-10-MIB", "cpuProtectionReason"),
)
if mibBuilder.loadTexts:
    cpuProtectionEntry.setStatus("mandatory")
_CpuProtectionPort_Type = Integer32
_CpuProtectionPort_Object = MibTableColumn
cpuProtectionPort = _CpuProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 131, 1, 1, 1),
    _CpuProtectionPort_Type()
)
cpuProtectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuProtectionPort.setStatus("mandatory")


class _CpuProtectionReason_Type(Integer32):
    """Custom type cpuProtectionReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("igmp", 3))
    )


_CpuProtectionReason_Type.__name__ = "Integer32"
_CpuProtectionReason_Object = MibTableColumn
cpuProtectionReason = _CpuProtectionReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 131, 1, 1, 2),
    _CpuProtectionReason_Type()
)
cpuProtectionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuProtectionReason.setStatus("mandatory")


class _CpuProtectionRateLimitSet_Type(Integer32):
    """Custom type cpuProtectionRateLimitSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CpuProtectionRateLimitSet_Type.__name__ = "Integer32"
_CpuProtectionRateLimitSet_Object = MibTableColumn
cpuProtectionRateLimitSet = _CpuProtectionRateLimitSet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 131, 1, 1, 3),
    _CpuProtectionRateLimitSet_Type()
)
cpuProtectionRateLimitSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuProtectionRateLimitSet.setStatus("mandatory")
_PrivateVLANSetup_ObjectIdentity = ObjectIdentity
privateVLANSetup = _PrivateVLANSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 133)
)
_PrivateVLANTable_Object = MibTable
privateVLANTable = _PrivateVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 133, 1)
)
if mibBuilder.loadTexts:
    privateVLANTable.setStatus("mandatory")
_PrivateVLANEntry_Object = MibTableRow
privateVLANEntry = _PrivateVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 133, 1, 1)
)
privateVLANEntry.setIndexNames(
    (0, "ZYXEL-MES3500-10-MIB", "privateVLANVid"),
)
if mibBuilder.loadTexts:
    privateVLANEntry.setStatus("mandatory")
_PrivateVLANName_Type = DisplayString
_PrivateVLANName_Object = MibTableColumn
privateVLANName = _PrivateVLANName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 133, 1, 1, 1),
    _PrivateVLANName_Type()
)
privateVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVLANName.setStatus("mandatory")


class _PrivateVLANVid_Type(Integer32):
    """Custom type privateVLANVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PrivateVLANVid_Type.__name__ = "Integer32"
_PrivateVLANVid_Object = MibTableColumn
privateVLANVid = _PrivateVLANVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 133, 1, 1, 2),
    _PrivateVLANVid_Type()
)
privateVLANVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVLANVid.setStatus("mandatory")
_PrivateVLANRowStatus_Type = RowStatus
_PrivateVLANRowStatus_Object = MibTableColumn
privateVLANRowStatus = _PrivateVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 133, 1, 1, 4),
    _PrivateVLANRowStatus_Type()
)
privateVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVLANRowStatus.setStatus("mandatory")
_ZyxelCableDiagnostics_ObjectIdentity = ObjectIdentity
zyxelCableDiagnostics = _ZyxelCableDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151)
)
_ZyxelCableDiagnosticsStatus_ObjectIdentity = ObjectIdentity
zyxelCableDiagnosticsStatus = _ZyxelCableDiagnosticsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1)
)
_ZyxelCableDiagnosticsPortTable_Object = MibTable
zyxelCableDiagnosticsPortTable = _ZyxelCableDiagnosticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsPortTable.setStatus("current")
_ZyxelCableDiagnosticsPortEntry_Object = MibTableRow
zyxelCableDiagnosticsPortEntry = _ZyxelCableDiagnosticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 1, 1)
)
zyxelCableDiagnosticsPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsPortEntry.setStatus("current")


class _ZyCableDiagnosticsPortAction_Type(Integer32):
    """Custom type zyCableDiagnosticsPortAction based on Integer32"""
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
          ("start", 1),
          ("clear", 2))
    )


_ZyCableDiagnosticsPortAction_Type.__name__ = "Integer32"
_ZyCableDiagnosticsPortAction_Object = MibTableColumn
zyCableDiagnosticsPortAction = _ZyCableDiagnosticsPortAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 1, 1, 1),
    _ZyCableDiagnosticsPortAction_Type()
)
zyCableDiagnosticsPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCableDiagnosticsPortAction.setStatus("current")


class _ZyCableDiagnosticsPortActionStatus_Type(Integer32):
    """Custom type zyCableDiagnosticsPortActionStatus based on Integer32"""
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


_ZyCableDiagnosticsPortActionStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticsPortActionStatus_Object = MibTableColumn
zyCableDiagnosticsPortActionStatus = _ZyCableDiagnosticsPortActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 1, 1, 2),
    _ZyCableDiagnosticsPortActionStatus_Type()
)
zyCableDiagnosticsPortActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsPortActionStatus.setStatus("current")
_ZyxelCableDiagnosticsResultPortTable_Object = MibTable
zyxelCableDiagnosticsResultPortTable = _ZyxelCableDiagnosticsResultPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsResultPortTable.setStatus("current")
_ZyxelCableDiagnosticsResultPortEntry_Object = MibTableRow
zyxelCableDiagnosticsResultPortEntry = _ZyxelCableDiagnosticsResultPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 2, 1)
)
zyxelCableDiagnosticsResultPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-MES3500-10-MIB", "zyCableDiagnosticsResultPortPairIndex"),
)
if mibBuilder.loadTexts:
    zyxelCableDiagnosticsResultPortEntry.setStatus("current")


class _ZyCableDiagnosticsResultPortPairIndex_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairIndex based on Integer32"""
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
        *(("pairA", 0),
          ("pairB", 1),
          ("pairC", 2),
          ("pairD", 3))
    )


_ZyCableDiagnosticsResultPortPairIndex_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairIndex_Object = MibTableColumn
zyCableDiagnosticsResultPortPairIndex = _ZyCableDiagnosticsResultPortPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 2, 1, 1),
    _ZyCableDiagnosticsResultPortPairIndex_Type()
)
zyCableDiagnosticsResultPortPairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairIndex.setStatus("current")


class _ZyCableDiagnosticsResultPortPairStatus_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairStatus based on Integer32"""
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
        *(("ok", 1),
          ("open", 2),
          ("short", 3),
          ("open-short", 4),
          ("crosstalk", 5),
          ("unknown", 6),
          ("unsupported", 7))
    )


_ZyCableDiagnosticsResultPortPairStatus_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairStatus_Object = MibTableColumn
zyCableDiagnosticsResultPortPairStatus = _ZyCableDiagnosticsResultPortPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 2, 1, 2),
    _ZyCableDiagnosticsResultPortPairStatus_Type()
)
zyCableDiagnosticsResultPortPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairStatus.setStatus("current")


class _ZyCableDiagnosticsResultPortPairLength_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupport", -2),
          ("not-available", -1))
    )


_ZyCableDiagnosticsResultPortPairLength_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairLength_Object = MibTableColumn
zyCableDiagnosticsResultPortPairLength = _ZyCableDiagnosticsResultPortPairLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 2, 1, 3),
    _ZyCableDiagnosticsResultPortPairLength_Type()
)
zyCableDiagnosticsResultPortPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairLength.setStatus("current")


class _ZyCableDiagnosticsResultPortPairDistanceToFault_Type(Integer32):
    """Custom type zyCableDiagnosticsResultPortPairDistanceToFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("unsupport", -2),
          ("not-available", -1))
    )


_ZyCableDiagnosticsResultPortPairDistanceToFault_Type.__name__ = "Integer32"
_ZyCableDiagnosticsResultPortPairDistanceToFault_Object = MibTableColumn
zyCableDiagnosticsResultPortPairDistanceToFault = _ZyCableDiagnosticsResultPortPairDistanceToFault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 151, 1, 2, 1, 4),
    _ZyCableDiagnosticsResultPortPairDistanceToFault_Type()
)
zyCableDiagnosticsResultPortPairDistanceToFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyCableDiagnosticsResultPortPairDistanceToFault.setStatus("current")

# Managed Objects groups


# Notification objects

eventOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 2, 1)
)
eventOnTrap.setObjects(
      *(("ZYXEL-MES3500-10-MIB", "eventSeqNum"),
        ("ZYXEL-MES3500-10-MIB", "eventEventId"),
        ("ZYXEL-MES3500-10-MIB", "eventName"),
        ("ZYXEL-MES3500-10-MIB", "eventSetTime"),
        ("ZYXEL-MES3500-10-MIB", "eventSeverity"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceType"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceId"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceName"),
        ("ZYXEL-MES3500-10-MIB", "eventServAffective"),
        ("ZYXEL-MES3500-10-MIB", "eventDescription"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceIdNumber"),
        ("ZYXEL-MES3500-10-MIB", "trapPersistence"),
        ("ZYXEL-MES3500-10-MIB", "trapSenderNodeId"),
        ("ZYXEL-MES3500-10-MIB", "trapSenderStatus"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventOnTrap.setStatus(
        "current"
    )

eventClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 27, 2, 2)
)
eventClearedTrap.setObjects(
      *(("ZYXEL-MES3500-10-MIB", "eventSeqNum"),
        ("ZYXEL-MES3500-10-MIB", "eventEventId"),
        ("ZYXEL-MES3500-10-MIB", "eventSetTime"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceType"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceId"),
        ("ZYXEL-MES3500-10-MIB", "eventInstanceIdNumber"),
        ("ZYXEL-MES3500-10-MIB", "trapRefSeqNum"),
        ("ZYXEL-MES3500-10-MIB", "trapSenderNodeId"),
        ("ZYXEL-MES3500-10-MIB", "trapSenderStatus"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventClearedTrap.setStatus(
        "current"
    )

mrstpRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 2, 1)
)
mrstpRoot.setObjects(
    ("ZYXEL-MES3500-10-MIB", "mrstpBridgeIndex")
)
if mibBuilder.loadTexts:
    mrstpRoot.setStatus(
        "current"
    )

mrstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 36, 2, 2)
)
mrstpTopologyChange.setObjects(
    ("ZYXEL-MES3500-10-MIB", "mrstpBridgeIndex")
)
if mibBuilder.loadTexts:
    mrstpTopologyChange.setStatus(
        "current"
    )

mstpRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 70, 1)
)
mstpRoot.setObjects(
    ("ZYXEL-MES3500-10-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpRoot.setStatus(
        "current"
    )

mstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 107, 70, 2)
)
mstpTopologyChange.setObjects(
    ("ZYXEL-MES3500-10-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpTopologyChange.setStatus(
        "current"
    )

errdisableDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 4, 1)
)
errdisableDetectTrap.setObjects(
      *(("ZYXEL-MES3500-10-MIB", "errdisableTrapPort"),
        ("ZYXEL-MES3500-10-MIB", "errdisableTrapReason"),
        ("ZYXEL-MES3500-10-MIB", "errdisableTrapMode"))
)
if mibBuilder.loadTexts:
    errdisableDetectTrap.setStatus(
        "current"
    )

errdisableRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 4, 2)
)
errdisableRecoveryTrap.setObjects(
      *(("ZYXEL-MES3500-10-MIB", "errdisableTrapPort"),
        ("ZYXEL-MES3500-10-MIB", "errdisableTrapReason"),
        ("ZYXEL-MES3500-10-MIB", "errdisableTrapMode"))
)
if mibBuilder.loadTexts:
    errdisableRecoveryTrap.setStatus(
        "current"
    )

errdisableDetectModeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 80, 130, 4, 3)
)
errdisableDetectModeChangeTrap.setObjects(
      *(("ZYXEL-MES3500-10-MIB", "errdisableTrapPort"),
        ("ZYXEL-MES3500-10-MIB", "errdisableTrapReason"),
        ("ZYXEL-MES3500-10-MIB", "errdisableTrapMode"))
)
if mibBuilder.loadTexts:
    errdisableDetectModeChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MES3500-10-MIB",
    **{"UtcTimeStamp": UtcTimeStamp,
       "EventIdNumber": EventIdNumber,
       "EventSeverity": EventSeverity,
       "EventServiceAffective": EventServiceAffective,
       "InstanceType": InstanceType,
       "EventPersistence": EventPersistence,
       "MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "esSeries": esSeries,
       "mes3500-10": mes3500_10,
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
       "sysSwBootUpImage": sysSwBootUpImage,
       "rateLimitSetup": rateLimitSetup,
       "rateLimitState": rateLimitState,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rateLimitPortState": rateLimitPortState,
       "rateLimitPortCommitRate": rateLimitPortCommitRate,
       "rateLimitPortPeakRate": rateLimitPortPeakRate,
       "rateLimitPortEgrRate": rateLimitPortEgrRate,
       "rateLimitPortPeakState": rateLimitPortPeakState,
       "rateLimitPortEgrState": rateLimitPortEgrState,
       "rateLimitPortCommitState": rateLimitPortCommitState,
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
       "brLimitPortShutdown": brLimitPortShutdown,
       "brLimitShutdown": brLimitShutdown,
       "portSecuritySetup": portSecuritySetup,
       "portSecurityState": portSecurityState,
       "portSecurityPortTable": portSecurityPortTable,
       "portSecurityPortEntry": portSecurityPortEntry,
       "portSecurityPortState": portSecurityPortState,
       "portSecurityPortLearnState": portSecurityPortLearnState,
       "portSecurityPortCount": portSecurityPortCount,
       "portSecurityPortShutdown": portSecurityPortShutdown,
       "portSecurityMacFreeze": portSecurityMacFreeze,
       "portSecurityShutdown": portSecurityShutdown,
       "vlanTrunkSetup": vlanTrunkSetup,
       "vlanTrunkPortTable": vlanTrunkPortTable,
       "vlanTrunkPortEntry": vlanTrunkPortEntry,
       "vlanTrunkPortState": vlanTrunkPortState,
       "vlanStackSetup": vlanStackSetup,
       "vlanStackState": vlanStackState,
       "vlanStackPortTable": vlanStackPortTable,
       "vlanStackPortEntry": vlanStackPortEntry,
       "vlanStackPortMode": vlanStackPortMode,
       "vlanStackPortVid": vlanStackPortVid,
       "vlanStackPortPrio": vlanStackPortPrio,
       "vlanStackTunnelPortTpid": vlanStackTunnelPortTpid,
       "selectiveQinQTable": selectiveQinQTable,
       "selectiveQinQEntry": selectiveQinQEntry,
       "selectiveQinQName": selectiveQinQName,
       "selectiveQinQPort": selectiveQinQPort,
       "selectiveQinQCvid": selectiveQinQCvid,
       "selectiveQinQSpvid": selectiveQinQSpvid,
       "selectiveQinQPriority": selectiveQinQPriority,
       "selectiveQinQRowStatus": selectiveQinQRowStatus,
       "dot1xSetup": dot1xSetup,
       "portAuthState": portAuthState,
       "portAuthTable": portAuthTable,
       "portAuthEntry": portAuthEntry,
       "portAuthEntryState": portAuthEntryState,
       "portReAuthEntryState": portReAuthEntryState,
       "portReAuthEntryTimer": portReAuthEntryTimer,
       "portAuthQuietPeriod": portAuthQuietPeriod,
       "portAuthTxPeriod": portAuthTxPeriod,
       "portAuthSupplicantTimeout": portAuthSupplicantTimeout,
       "portAuthMaxRequest": portAuthMaxRequest,
       "portAuthGuestVlanState": portAuthGuestVlanState,
       "portAuthGuestVlan": portAuthGuestVlan,
       "portAuthGuestVlanHostMode": portAuthGuestVlanHostMode,
       "portAuthGuestVlanHostModeMultiSecureNumber": portAuthGuestVlanHostModeMultiSecureNumber,
       "hwMonitorInfo": hwMonitorInfo,
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
       "snmpVersion": snmpVersion,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserName": snmpUserName,
       "snmpUserSecurityLevel": snmpUserSecurityLevel,
       "snmpUserAuthProtocol": snmpUserAuthProtocol,
       "snmpUserPrivProtocol": snmpUserPrivProtocol,
       "snmpUserGroup": snmpUserGroup,
       "snmpTrapGroupTable": snmpTrapGroupTable,
       "snmpTrapGroupEntry": snmpTrapGroupEntry,
       "snmpTrapSystemGroup": snmpTrapSystemGroup,
       "snmpTrapInterfaceGroup": snmpTrapInterfaceGroup,
       "snmpTrapAAAGroup": snmpTrapAAAGroup,
       "snmpTrapIPGroup": snmpTrapIPGroup,
       "snmpTrapSwitchGroup": snmpTrapSwitchGroup,
       "dateTimeSetup": dateTimeSetup,
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
       "dateTimeServerAddr1": dateTimeServerAddr1,
       "dateTimeServerAddr2": dateTimeServerAddr2,
       "dateTimeServerAddr3": dateTimeServerAddr3,
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
       "sysMgmtTftpActionPrivilege13": sysMgmtTftpActionPrivilege13,
       "sysMgmtConfigSavePrivilege13": sysMgmtConfigSavePrivilege13,
       "sysMgmtDefaultConfigPrivilege13": sysMgmtDefaultConfigPrivilege13,
       "layer2Setup": layer2Setup,
       "vlanTypeSetup": vlanTypeSetup,
       "igmpSnoopingStateSetup": igmpSnoopingStateSetup,
       "tagVlanPortIsolationState": tagVlanPortIsolationState,
       "stpState": stpState,
       "igmpFilteringStateSetup": igmpFilteringStateSetup,
       "unknownMulticastFrameForwarding": unknownMulticastFrameForwarding,
       "multicastGrpHostTimeout": multicastGrpHostTimeout,
       "reservedMulticastFrameForwarding": reservedMulticastFrameForwarding,
       "igmpsnp8021pPriority": igmpsnp8021pPriority,
       "igmpsnpVlanMode": igmpsnpVlanMode,
       "stpMode": stpMode,
       "igmpsnpVlanTable": igmpsnpVlanTable,
       "igmpsnpVlanEntry": igmpsnpVlanEntry,
       "igmpsnpVid": igmpsnpVid,
       "igmpsnpVlanName": igmpsnpVlanName,
       "igmpsnpVlanRowStatus": igmpsnpVlanRowStatus,
       "igmpsnpQuerierMode": igmpsnpQuerierMode,
       "ethernetCfmStateSetup": ethernetCfmStateSetup,
       "lldpStateSetup": lldpStateSetup,
       "igmpSnpReportProxySetup": igmpSnpReportProxySetup,
       "smartIsolationState": smartIsolationState,
       "ipSetup": ipSetup,
       "dnsIpAddress": dnsIpAddress,
       "inbandIpSetup": inbandIpSetup,
       "inbandIpType": inbandIpType,
       "inbandVid": inbandVid,
       "inbandStaticIp": inbandStaticIp,
       "inbandStaticSubnetMask": inbandStaticSubnetMask,
       "inbandStaticGateway": inbandStaticGateway,
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
       "aggrSetup": aggrSetup,
       "aggrState": aggrState,
       "aggrSystemPriority": aggrSystemPriority,
       "aggrGroupTable": aggrGroupTable,
       "aggrGroupEntry": aggrGroupEntry,
       "aggrGroupIndex": aggrGroupIndex,
       "aggrGroupState": aggrGroupState,
       "aggrGroupDynamicState": aggrGroupDynamicState,
       "aggrGroupCriteria": aggrGroupCriteria,
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
       "queuingMethodSetup": queuingMethodSetup,
       "portQueuingMethodTable": portQueuingMethodTable,
       "portQueuingMethodEntry": portQueuingMethodEntry,
       "portQueuingMethodQueue": portQueuingMethodQueue,
       "portQueuingMethodWeight": portQueuingMethodWeight,
       "portQueuingMethodMode": portQueuingMethodMode,
       "portQueuingMethodHybridSpqTable": portQueuingMethodHybridSpqTable,
       "portQueuingMethodHybridSpqEntry": portQueuingMethodHybridSpqEntry,
       "portQueuingMethodHybridSpq": portQueuingMethodHybridSpq,
       "dhcpSetup": dhcpSetup,
       "globalDhcpRelay": globalDhcpRelay,
       "globalDhcpRelayEnable": globalDhcpRelayEnable,
       "maxNumberOfGlobalDhcpRelayRemoteServer": maxNumberOfGlobalDhcpRelayRemoteServer,
       "globalDhcpRelayRemoteServerTable": globalDhcpRelayRemoteServerTable,
       "globalDhcpRelayRemoteServerEntry": globalDhcpRelayRemoteServerEntry,
       "globalDhcpRelayRemoteServerIp": globalDhcpRelayRemoteServerIp,
       "globalDhcpRelayRemoteServerRowStatus": globalDhcpRelayRemoteServerRowStatus,
       "globalDhcpRelayOption82Profile": globalDhcpRelayOption82Profile,
       "globalDhcpRelayOption82PortTable": globalDhcpRelayOption82PortTable,
       "globalDhcpRelayOption82PortEntry": globalDhcpRelayOption82PortEntry,
       "globalDhcpRelayOption82PortProfile": globalDhcpRelayOption82PortProfile,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayInfoData": dhcpRelayInfoData,
       "maxNumberOfDhcpRelay": maxNumberOfDhcpRelay,
       "maxNumberOfDhcpRelayRemoteServer": maxNumberOfDhcpRelayRemoteServer,
       "dhcpRelayTable": dhcpRelayTable,
       "dhcpRelayEntry": dhcpRelayEntry,
       "dhcpRelayOption82Profile": dhcpRelayOption82Profile,
       "dhcpRelayRemoteServerTable": dhcpRelayRemoteServerTable,
       "dhcpRelayRemoteServerEntry": dhcpRelayRemoteServerEntry,
       "dhcpRelayVid": dhcpRelayVid,
       "dhcpRelayRemoteServerIp": dhcpRelayRemoteServerIp,
       "dhcpRelayRemoteServerRowStatus": dhcpRelayRemoteServerRowStatus,
       "dhcpRelayOption82VlanPortTable": dhcpRelayOption82VlanPortTable,
       "dhcpRelayOption82VlanPortEntry": dhcpRelayOption82VlanPortEntry,
       "dhcpRelayOption82VlanPortProfile": dhcpRelayOption82VlanPortProfile,
       "dhcpOption82ProfileTable": dhcpOption82ProfileTable,
       "dhcpOption82ProfileEntry": dhcpOption82ProfileEntry,
       "dhcpOption82ProfileName": dhcpOption82ProfileName,
       "dhcpOption82ProfileCircuitIDEnable": dhcpOption82ProfileCircuitIDEnable,
       "dhcpOption82ProfileCircuitIDSlotPort": dhcpOption82ProfileCircuitIDSlotPort,
       "dhcpOption82ProfileCircuitIDVlan": dhcpOption82ProfileCircuitIDVlan,
       "dhcpOption82ProfileCircuitIDHostname": dhcpOption82ProfileCircuitIDHostname,
       "dhcpOption82ProfileCircuitIDString": dhcpOption82ProfileCircuitIDString,
       "dhcpOption82ProfileRemoteIDEnable": dhcpOption82ProfileRemoteIDEnable,
       "dhcpOption82ProfileRemoteIDMAC": dhcpOption82ProfileRemoteIDMAC,
       "dhcpOption82ProfileRemoteIDString": dhcpOption82ProfileRemoteIDString,
       "dhcpOption82ProfileRowstatus": dhcpOption82ProfileRowstatus,
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
       "portOpModePortLBTestStatus": portOpModePortLBTestStatus,
       "portOpModePortCounterReset": portOpModePortCounterReset,
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
       "multicastPortMaxGroupLimited": multicastPortMaxGroupLimited,
       "multicastPortMaxOfGroup": multicastPortMaxOfGroup,
       "multicastPortIgmpFilteringProfile": multicastPortIgmpFilteringProfile,
       "multicastPortQuerierMode": multicastPortQuerierMode,
       "multicastPortThrottlingAction": multicastPortThrottlingAction,
       "multicastPortLeaveMode": multicastPortLeaveMode,
       "multicastPortLeaveTimeout": multicastPortLeaveTimeout,
       "multicastPortFastLeaveTimeout": multicastPortFastLeaveTimeout,
       "multicastStatus": multicastStatus,
       "multicastStatusTable": multicastStatusTable,
       "multicastStatusEntry": multicastStatusEntry,
       "multicastStatusIndex": multicastStatusIndex,
       "multicastStatusVlanID": multicastStatusVlanID,
       "multicastStatusPort": multicastStatusPort,
       "multicastStatusGroup": multicastStatusGroup,
       "igmpSnpCountTable": igmpSnpCountTable,
       "igmpSnpCountEntry": igmpSnpCountEntry,
       "igmpSnpCountIndex": igmpSnpCountIndex,
       "igmpSnpV2CountQueryRx": igmpSnpV2CountQueryRx,
       "igmpSnpV2CountReportRx": igmpSnpV2CountReportRx,
       "igmpSnpV2CountLeaveRx": igmpSnpV2CountLeaveRx,
       "igmpSnpV2CountQueryRxDrop": igmpSnpV2CountQueryRxDrop,
       "igmpSnpV2CountReportRxDrop": igmpSnpV2CountReportRxDrop,
       "igmpSnpV2CountLeaveRxDrop": igmpSnpV2CountLeaveRxDrop,
       "igmpSnpV2CountQueryTx": igmpSnpV2CountQueryTx,
       "igmpSnpV2CountReportTx": igmpSnpV2CountReportTx,
       "igmpSnpV2CountLeaveTx": igmpSnpV2CountLeaveTx,
       "igmpSnpV3CountQueryRx": igmpSnpV3CountQueryRx,
       "igmpSnpV3CountReportRx": igmpSnpV3CountReportRx,
       "igmpSnpV3CountQueryRxDrop": igmpSnpV3CountQueryRxDrop,
       "igmpSnpV3CountReportRxDrop": igmpSnpV3CountReportRxDrop,
       "igmpSnpV3CountQueryTx": igmpSnpV3CountQueryTx,
       "igmpSnpV3CountReportTx": igmpSnpV3CountReportTx,
       "multicastVlanStatusTable": multicastVlanStatusTable,
       "multicastVlanStatusEntry": multicastVlanStatusEntry,
       "multicastVlanStatusVlanID": multicastVlanStatusVlanID,
       "multicastVlanStatusType": multicastVlanStatusType,
       "multicastVlanQueryPort": multicastVlanQueryPort,
       "igmpSnpCountVlanTable": igmpSnpCountVlanTable,
       "igmpSnpCountVlanEntry": igmpSnpCountVlanEntry,
       "igmpSnpCountVlanIndex": igmpSnpCountVlanIndex,
       "igmpSnpV2CountVlanQueryRx": igmpSnpV2CountVlanQueryRx,
       "igmpSnpV2CountVlanReportRx": igmpSnpV2CountVlanReportRx,
       "igmpSnpV2CountVlanLeaveRx": igmpSnpV2CountVlanLeaveRx,
       "igmpSnpV2CountVlanQueryRxDrop": igmpSnpV2CountVlanQueryRxDrop,
       "igmpSnpV2CountVlanReportRxDrop": igmpSnpV2CountVlanReportRxDrop,
       "igmpSnpV2CountVlanLeaveRxDrop": igmpSnpV2CountVlanLeaveRxDrop,
       "igmpSnpV2CountVlanQueryTx": igmpSnpV2CountVlanQueryTx,
       "igmpSnpV2CountVlanReportTx": igmpSnpV2CountVlanReportTx,
       "igmpSnpV2CountVlanLeaveTx": igmpSnpV2CountVlanLeaveTx,
       "igmpSnpV3CountVlanQueryRx": igmpSnpV3CountVlanQueryRx,
       "igmpSnpV3CountVlanReportRx": igmpSnpV3CountVlanReportRx,
       "igmpSnpV3CountVlanQueryRxDrop": igmpSnpV3CountVlanQueryRxDrop,
       "igmpSnpV3CountVlanReportRxDrop": igmpSnpV3CountVlanReportRxDrop,
       "igmpSnpV3CountVlanQueryTx": igmpSnpV3CountVlanQueryTx,
       "igmpSnpV3CountVlanReportTx": igmpSnpV3CountVlanReportTx,
       "igmpSnpCountPortTable": igmpSnpCountPortTable,
       "igmpSnpCountPortEntry": igmpSnpCountPortEntry,
       "igmpSnpV2CountPortQueryRx": igmpSnpV2CountPortQueryRx,
       "igmpSnpV2CountPortReportRx": igmpSnpV2CountPortReportRx,
       "igmpSnpV2CountPortLeaveRx": igmpSnpV2CountPortLeaveRx,
       "igmpSnpV2CountPortReportRxDrop": igmpSnpV2CountPortReportRxDrop,
       "igmpSnpV2CountPortLeaveRxDrop": igmpSnpV2CountPortLeaveRxDrop,
       "igmpSnpV2CountPortReportTx": igmpSnpV2CountPortReportTx,
       "igmpSnpV2CountPortLeaveTx": igmpSnpV2CountPortLeaveTx,
       "igmpSnpV3CountPortQueryRx": igmpSnpV3CountPortQueryRx,
       "igmpSnpV3CountPortReportRx": igmpSnpV3CountPortReportRx,
       "igmpSnpV3CountPortReportRxDrop": igmpSnpV3CountPortReportRxDrop,
       "igmpSnpV3CountPortReportTx": igmpSnpV3CountPortReportTx,
       "igmpSnpGroupCountStatus": igmpSnpGroupCountStatus,
       "igmpSnpGroupCountNum": igmpSnpGroupCountNum,
       "igmpSnpGroupCountVlanTable": igmpSnpGroupCountVlanTable,
       "igmpSnpGroupCountVlanEntry": igmpSnpGroupCountVlanEntry,
       "igmpSnpGroupCountVlanIndex": igmpSnpGroupCountVlanIndex,
       "igmpSnpGroupCountVlanNum": igmpSnpGroupCountVlanNum,
       "igmpSnpGroupCountPortTable": igmpSnpGroupCountPortTable,
       "igmpSnpGroupCountPortEntry": igmpSnpGroupCountPortEntry,
       "igmpSnpGroupCountPortNum": igmpSnpGroupCountPortNum,
       "igmpFilteringProfileSetup": igmpFilteringProfileSetup,
       "igmpFilteringMaxNumberOfProfile": igmpFilteringMaxNumberOfProfile,
       "igmpFilteringProfileTable": igmpFilteringProfileTable,
       "igmpFilteringProfileEntry": igmpFilteringProfileEntry,
       "igmpFilteringProfileName": igmpFilteringProfileName,
       "igmpFilteringProfileStartAddress": igmpFilteringProfileStartAddress,
       "igmpFilteringProfileEndAddress": igmpFilteringProfileEndAddress,
       "igmpFilteringProfileRowStatus": igmpFilteringProfileRowStatus,
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
       "clusterSetup": clusterSetup,
       "clusterManager": clusterManager,
       "clusterMaxNumOfManager": clusterMaxNumOfManager,
       "clusterManagerTable": clusterManagerTable,
       "clusterManagerEntry": clusterManagerEntry,
       "clusterManagerVid": clusterManagerVid,
       "clusterManagerName": clusterManagerName,
       "clusterManagerRowStatus": clusterManagerRowStatus,
       "clusterMembers": clusterMembers,
       "clusterMaxNumOfMember": clusterMaxNumOfMember,
       "clusterMemberTable": clusterMemberTable,
       "clusterMemberEntry": clusterMemberEntry,
       "clusterMemberMac": clusterMemberMac,
       "clusterMemberName": clusterMemberName,
       "clusterMemberModel": clusterMemberModel,
       "clusterMemberPassword": clusterMemberPassword,
       "clusterMemberRowStatus": clusterMemberRowStatus,
       "clusterCandidates": clusterCandidates,
       "clusterCandidateTable": clusterCandidateTable,
       "clusterCandidateEntry": clusterCandidateEntry,
       "clusterCandidateMac": clusterCandidateMac,
       "clusterCandidateName": clusterCandidateName,
       "clusterCandidateModel": clusterCandidateModel,
       "clusterStatus": clusterStatus,
       "clusterStatusRole": clusterStatusRole,
       "clusterStatusManager": clusterStatusManager,
       "clsuterStatusMaxNumOfMember": clsuterStatusMaxNumOfMember,
       "clusterStatusMemberTable": clusterStatusMemberTable,
       "clusterStatusMemberEntry": clusterStatusMemberEntry,
       "clusterStatusMemberMac": clusterStatusMemberMac,
       "clusterStatusMemberName": clusterStatusMemberName,
       "clusterStatusMemberModel": clusterStatusMemberModel,
       "clusterStatusMemberStatus": clusterStatusMemberStatus,
       "sysLogSetup": sysLogSetup,
       "sysLogState": sysLogState,
       "sysLogTypeTable": sysLogTypeTable,
       "sysLogTypeEntry": sysLogTypeEntry,
       "sysLogTypeIndex": sysLogTypeIndex,
       "sysLogTypeName": sysLogTypeName,
       "sysLogTypeState": sysLogTypeState,
       "sysLogTypeFacility": sysLogTypeFacility,
       "sysLogTypePrivilege": sysLogTypePrivilege,
       "sysLogServerTable": sysLogServerTable,
       "sysLogServerEntry": sysLogServerEntry,
       "sysLogServerAddress": sysLogServerAddress,
       "sysLogServerLogLevel": sysLogServerLogLevel,
       "sysLogServerRowStatus": sysLogServerRowStatus,
       "diffservSetup": diffservSetup,
       "diffservState": diffservState,
       "diffservMapTable": diffservMapTable,
       "diffservMapEntry": diffservMapEntry,
       "diffservMapDscp": diffservMapDscp,
       "diffservMapPriority": diffservMapPriority,
       "diffservPortTable": diffservPortTable,
       "diffservPortEntry": diffservPortEntry,
       "diffservPortState": diffservPortState,
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
       "mrstpPortAdminEdgePort": mrstpPortAdminEdgePort,
       "mrstpPortOperEdgePort": mrstpPortOperEdgePort,
       "mrstpNotifications": mrstpNotifications,
       "mrstpRoot": mrstpRoot,
       "mrstpTopologyChange": mrstpTopologyChange,
       "dhcpSnp": dhcpSnp,
       "dhcpSnpVlanTable": dhcpSnpVlanTable,
       "dhcpSnpVlanEntry": dhcpSnpVlanEntry,
       "dhcpSnpVlanEntryVid": dhcpSnpVlanEntryVid,
       "dhcpSnpVlanEntryEnable": dhcpSnpVlanEntryEnable,
       "dhcpSnpVlanEntryOption82Enable": dhcpSnpVlanEntryOption82Enable,
       "dhcpSnpVlanEntryInfo": dhcpSnpVlanEntryInfo,
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
       "dhcpSnpOption82VlanPortTable": dhcpSnpOption82VlanPortTable,
       "dhcpSnpOption82VlanPortEntry": dhcpSnpOption82VlanPortEntry,
       "dhcpSnpOption82VlanPortProfile": dhcpSnpOption82VlanPortProfile,
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
       "trTCMPortDscpProfile": trTCMPortDscpProfile,
       "trTCMDscpProfileTable": trTCMDscpProfileTable,
       "trTCMDscpProfileEntry": trTCMDscpProfileEntry,
       "trTCMDscpProfileDscpName": trTCMDscpProfileDscpName,
       "trTCMDscpProfileDscpGreen": trTCMDscpProfileDscpGreen,
       "trTCMDscpProfileDscpYellow": trTCMDscpProfileDscpYellow,
       "trTCMDscpProfileDscpRed": trTCMDscpProfileDscpRed,
       "trTCMDscpProfileDscpRowstatus": trTCMDscpProfileDscpRowstatus,
       "loopGuardSetup": loopGuardSetup,
       "loopGuardState": loopGuardState,
       "loopGuardPortTable": loopGuardPortTable,
       "loopGuardPortEntry": loopGuardPortEntry,
       "loopGuardPortState": loopGuardPortState,
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
       "mstpPortAdminEdgePort": mstpPortAdminEdgePort,
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
       "mstpRoot": mstpRoot,
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
       "radiusAcctServerSetup": radiusAcctServerSetup,
       "radiusAcctServerTimeout": radiusAcctServerTimeout,
       "radiusAcctServerTable": radiusAcctServerTable,
       "radiusAcctServerEntry": radiusAcctServerEntry,
       "radiusAcctServerIndex": radiusAcctServerIndex,
       "radiusAcctServerIpAddr": radiusAcctServerIpAddr,
       "radiusAcctServerUdpPort": radiusAcctServerUdpPort,
       "radiusAcctServerSharedSecret": radiusAcctServerSharedSecret,
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
       "tacacsAcctServerSetup": tacacsAcctServerSetup,
       "tacacsAcctServerTimeout": tacacsAcctServerTimeout,
       "tacacsAcctServerTable": tacacsAcctServerTable,
       "tacacsAcctServerEntry": tacacsAcctServerEntry,
       "tacacsAcctServerIndex": tacacsAcctServerIndex,
       "tacacsAcctServerIpAddr": tacacsAcctServerIpAddr,
       "tacacsAcctServerTcpPort": tacacsAcctServerTcpPort,
       "tacacsAcctServerSharedSecret": tacacsAcctServerSharedSecret,
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
       "authorizationSetup": authorizationSetup,
       "authorizationTypeTable": authorizationTypeTable,
       "authorizationTypeEntry": authorizationTypeEntry,
       "authorizationTypeName": authorizationTypeName,
       "authorizationTypeActive": authorizationTypeActive,
       "authorizationTypeMethod": authorizationTypeMethod,
       "portIsolationSetup": portIsolationSetup,
       "portIsolationTable": portIsolationTable,
       "portIsolationEntry": portIsolationEntry,
       "portIsolationState": portIsolationState,
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
       "vlanMappingRuleTable": vlanMappingRuleTable,
       "vlanMappingRuleEntry": vlanMappingRuleEntry,
       "vlanMappingRuleName": vlanMappingRuleName,
       "vlanMappingRulePort": vlanMappingRulePort,
       "vlanMappingRuleVid": vlanMappingRuleVid,
       "vlanMappingRuleTransVid": vlanMappingRuleTransVid,
       "vlanMappingRulePriority": vlanMappingRulePriority,
       "vlanMappingRuleRowStatus": vlanMappingRuleRowStatus,
       "vlanMappingRuleDirection": vlanMappingRuleDirection,
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
       "dot3OamOuld": dot3OamOuld,
       "dot3OamSetup": dot3OamSetup,
       "dot3OamState": dot3OamState,
       "dot3OamPortTable": dot3OamPortTable,
       "dot3OamPortEntry": dot3OamPortEntry,
       "dot3OamPortState": dot3OamPortState,
       "dot3OamFunctionsSupported": dot3OamFunctionsSupported,
       "dot3OamOuldSetup": dot3OamOuldSetup,
       "dot3OamOuldDiscoveryTimer": dot3OamOuldDiscoveryTimer,
       "dot3OamOuldRecoveryTimer": dot3OamOuldRecoveryTimer,
       "dot3OamOuldSetupPortTable": dot3OamOuldSetupPortTable,
       "dot3OamOuldSetupPortEntry": dot3OamOuldSetupPortEntry,
       "dot3OamOuldState": dot3OamOuldState,
       "dot3OamOuldAggressiveMode": dot3OamOuldAggressiveMode,
       "dot3OamOuldStatus": dot3OamOuldStatus,
       "dot3OamOuldStatusPortTable": dot3OamOuldStatusPortTable,
       "dot3OamOuldStatusPortEntry": dot3OamOuldStatusPortEntry,
       "dot3OamOuldResult": dot3OamOuldResult,
       "dot3OamOuldLinkStatus": dot3OamOuldLinkStatus,
       "dot3OamOuldCountdown": dot3OamOuldCountdown,
       "dot1agCfmSetup": dot1agCfmSetup,
       "dot1agCfmMIBObjects": dot1agCfmMIBObjects,
       "dot1agCfmMep": dot1agCfmMep,
       "zyswdot1agCfmMepTable": zyswdot1agCfmMepTable,
       "zyswdot1agCfmMepEntry": zyswdot1agCfmMepEntry,
       "zyswdot1agCfmMepTransmitLbmDataTlvSize": zyswdot1agCfmMepTransmitLbmDataTlvSize,
       "sFlowSetup": sFlowSetup,
       "sFlowState": sFlowState,
       "sFlowCollectorTable": sFlowCollectorTable,
       "sFlowCollectorEntry": sFlowCollectorEntry,
       "sFlowCollectorAddressType": sFlowCollectorAddressType,
       "sFlowCollectorAddress": sFlowCollectorAddress,
       "sFlowCollectorUdpPort": sFlowCollectorUdpPort,
       "sFlowCollectorRowStatus": sFlowCollectorRowStatus,
       "sFlowPortTable": sFlowPortTable,
       "sFlowPortEntry": sFlowPortEntry,
       "sFlowPortState": sFlowPortState,
       "sFlowPortCollectorTable": sFlowPortCollectorTable,
       "sFlowPortCollectorEntry": sFlowPortCollectorEntry,
       "sFlowPortCollectorAddressType": sFlowPortCollectorAddressType,
       "sFlowPortCollectorAddress": sFlowPortCollectorAddress,
       "sFlowPortCollectorSampleRate": sFlowPortCollectorSampleRate,
       "sFlowPortCollectorPollInterval": sFlowPortCollectorPollInterval,
       "sFlowPortCollectorRowStatus": sFlowPortCollectorRowStatus,
       "sysMemoryPool": sysMemoryPool,
       "sysMemoryPoolTable": sysMemoryPoolTable,
       "sysMemoryPoolEntry": sysMemoryPoolEntry,
       "sysMemoryPoolId": sysMemoryPoolId,
       "sysMemoryPoolName": sysMemoryPoolName,
       "sysMemoryPoolTotal": sysMemoryPoolTotal,
       "sysMemoryPoolUsed": sysMemoryPoolUsed,
       "sysMemoryPoolUtil": sysMemoryPoolUtil,
       "pppoe": pppoe,
       "pppoeIaSetup": pppoeIaSetup,
       "pppoeIaState": pppoeIaState,
       "pppoeIaAccessNodeIdentifierString": pppoeIaAccessNodeIdentifierString,
       "pppoeIaFlexibleCircuitIDSyntaxActive": pppoeIaFlexibleCircuitIDSyntaxActive,
       "pppoeIaFlexibleCircuitIDSyntaxIdentifierString": pppoeIaFlexibleCircuitIDSyntaxIdentifierString,
       "pppoeIaFlexibleCircuitIDSyntaxOption": pppoeIaFlexibleCircuitIDSyntaxOption,
       "pppoeIaFlexibleCircuitIDSyntaxDelimiter": pppoeIaFlexibleCircuitIDSyntaxDelimiter,
       "pppoeIaPortTable": pppoeIaPortTable,
       "pppoeIaPortEntry": pppoeIaPortEntry,
       "pppoeIaPortEntryPort": pppoeIaPortEntryPort,
       "pppoeIaPortEntryTrust": pppoeIaPortEntryTrust,
       "pppoeIaPortEntryCircuitIDString": pppoeIaPortEntryCircuitIDString,
       "pppoeIaPortEntryRemoteIDString": pppoeIaPortEntryRemoteIDString,
       "pppoeIaVlanTable": pppoeIaVlanTable,
       "pppoeIaVlanEntry": pppoeIaVlanEntry,
       "pppoeIaVlanEntryVid": pppoeIaVlanEntryVid,
       "pppoeIaVlanEntryCircuitID": pppoeIaVlanEntryCircuitID,
       "pppoeIaVlanEntryRemoteID": pppoeIaVlanEntryRemoteID,
       "pppoeIaVlanEntryRowStatus": pppoeIaVlanEntryRowStatus,
       "pppoeIaPortVlanTable": pppoeIaPortVlanTable,
       "pppoeIaPortVlanEntry": pppoeIaPortVlanEntry,
       "pppoeIaPortVlanEntryPort": pppoeIaPortVlanEntryPort,
       "pppoeIaPortVlanEntryVid": pppoeIaPortVlanEntryVid,
       "pppoeIaPortVlanEntryCircuitIDString": pppoeIaPortVlanEntryCircuitIDString,
       "pppoeIaPortVlanEntryRemoteIDString": pppoeIaPortVlanEntryRemoteIDString,
       "pppoeIaPortVlanEntryRowStatus": pppoeIaPortVlanEntryRowStatus,
       "pppoeIaFlexibleCircuitIDSyntaxIdentifierStringType": pppoeIaFlexibleCircuitIDSyntaxIdentifierStringType,
       "errdisable": errdisable,
       "recovery": recovery,
       "errdisableRecoverySetup": errdisableRecoverySetup,
       "errdisableRecoveryState": errdisableRecoveryState,
       "errdisableRecoveryReasonTable": errdisableRecoveryReasonTable,
       "errdisableRecoveryReasonEntry": errdisableRecoveryReasonEntry,
       "errdisableRecoveryReason": errdisableRecoveryReason,
       "errdisableRecoveryReasonActive": errdisableRecoveryReasonActive,
       "errdisableRecoveryReasonInterval": errdisableRecoveryReasonInterval,
       "errdisableRecoveryIfStatusTable": errdisableRecoveryIfStatusTable,
       "errdisableRecoveryIfStatusEntry": errdisableRecoveryIfStatusEntry,
       "errdisableRecoveryIfStatusReason": errdisableRecoveryIfStatusReason,
       "errdisableRecoveryIfStatusPort": errdisableRecoveryIfStatusPort,
       "errdisableRecoveryIfStatusTimeToRecover": errdisableRecoveryIfStatusTimeToRecover,
       "detect": detect,
       "errdisableDetectReasonTable": errdisableDetectReasonTable,
       "errdisableDetectReasonEntry": errdisableDetectReasonEntry,
       "errdisableDetectReason": errdisableDetectReason,
       "errdisableDetectReasonEnable": errdisableDetectReasonEnable,
       "errdisableDetectReasonMode": errdisableDetectReasonMode,
       "errdisableTrapInfoObject": errdisableTrapInfoObject,
       "errdisableTrapPort": errdisableTrapPort,
       "errdisableTrapReason": errdisableTrapReason,
       "errdisableTrapMode": errdisableTrapMode,
       "errdisableTrapNotifications": errdisableTrapNotifications,
       "errdisableDetectTrap": errdisableDetectTrap,
       "errdisableRecoveryTrap": errdisableRecoveryTrap,
       "errdisableDetectModeChangeTrap": errdisableDetectModeChangeTrap,
       "cpuProtectionSetup": cpuProtectionSetup,
       "cpuProtectionTable": cpuProtectionTable,
       "cpuProtectionEntry": cpuProtectionEntry,
       "cpuProtectionPort": cpuProtectionPort,
       "cpuProtectionReason": cpuProtectionReason,
       "cpuProtectionRateLimitSet": cpuProtectionRateLimitSet,
       "privateVLANSetup": privateVLANSetup,
       "privateVLANTable": privateVLANTable,
       "privateVLANEntry": privateVLANEntry,
       "privateVLANName": privateVLANName,
       "privateVLANVid": privateVLANVid,
       "privateVLANRowStatus": privateVLANRowStatus,
       "zyxelCableDiagnostics": zyxelCableDiagnostics,
       "zyxelCableDiagnosticsStatus": zyxelCableDiagnosticsStatus,
       "zyxelCableDiagnosticsPortTable": zyxelCableDiagnosticsPortTable,
       "zyxelCableDiagnosticsPortEntry": zyxelCableDiagnosticsPortEntry,
       "zyCableDiagnosticsPortAction": zyCableDiagnosticsPortAction,
       "zyCableDiagnosticsPortActionStatus": zyCableDiagnosticsPortActionStatus,
       "zyxelCableDiagnosticsResultPortTable": zyxelCableDiagnosticsResultPortTable,
       "zyxelCableDiagnosticsResultPortEntry": zyxelCableDiagnosticsResultPortEntry,
       "zyCableDiagnosticsResultPortPairIndex": zyCableDiagnosticsResultPortPairIndex,
       "zyCableDiagnosticsResultPortPairStatus": zyCableDiagnosticsResultPortPairStatus,
       "zyCableDiagnosticsResultPortPairLength": zyCableDiagnosticsResultPortPairLength,
       "zyCableDiagnosticsResultPortPairDistanceToFault": zyCableDiagnosticsResultPortPairDistanceToFault}
)
