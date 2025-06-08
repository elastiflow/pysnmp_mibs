# SNMP MIB module (ZYXEL-ES2108G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ES2108G-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:16:51 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26)
)

faultTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27)
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
    status = "mandatory"
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
_Es2108g_ObjectIdentity = ObjectIdentity
es2108g = _Es2108g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1)
)
_SysSwPlatformMajorVers_Type = Integer32
_SysSwPlatformMajorVers_Object = MibScalar
sysSwPlatformMajorVers = _SysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 1),
    _SysSwPlatformMajorVers_Type()
)
sysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setStatus("mandatory")
_SysSwPlatformMinorVers_Type = Integer32
_SysSwPlatformMinorVers_Object = MibScalar
sysSwPlatformMinorVers = _SysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 2),
    _SysSwPlatformMinorVers_Type()
)
sysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setStatus("mandatory")
_SysSwModelString_Type = DisplayString
_SysSwModelString_Object = MibScalar
sysSwModelString = _SysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 3),
    _SysSwModelString_Type()
)
sysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModelString.setStatus("mandatory")
_SysSwVersionControlNbr_Type = Integer32
_SysSwVersionControlNbr_Object = MibScalar
sysSwVersionControlNbr = _SysSwVersionControlNbr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 4),
    _SysSwVersionControlNbr_Type()
)
sysSwVersionControlNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionControlNbr.setStatus("mandatory")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 5),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("mandatory")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 6),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("mandatory")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 7),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("mandatory")
_SysHwMajorVers_Type = Integer32
_SysHwMajorVers_Object = MibScalar
sysHwMajorVers = _SysHwMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 8),
    _SysHwMajorVers_Type()
)
sysHwMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVers.setStatus("mandatory")
_SysHwMinorVers_Type = Integer32
_SysHwMinorVers_Object = MibScalar
sysHwMinorVers = _SysHwMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 9),
    _SysHwMinorVers_Type()
)
sysHwMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVers.setStatus("mandatory")
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 1, 10),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("mandatory")
_RateLimitSetup_ObjectIdentity = ObjectIdentity
rateLimitSetup = _RateLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2)
)
_RateLimitState_Type = EnabledStatus
_RateLimitState_Object = MibScalar
rateLimitState = _RateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 1),
    _RateLimitState_Type()
)
rateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitState.setStatus("mandatory")
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("mandatory")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("mandatory")
_RateLimitPortState_Type = EnabledStatus
_RateLimitPortState_Object = MibTableColumn
rateLimitPortState = _RateLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2, 1, 1),
    _RateLimitPortState_Type()
)
rateLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortState.setStatus("mandatory")
_RateLimitPortIngRate_Type = Integer32
_RateLimitPortIngRate_Object = MibTableColumn
rateLimitPortIngRate = _RateLimitPortIngRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2, 1, 2),
    _RateLimitPortIngRate_Type()
)
rateLimitPortIngRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortIngRate.setStatus("mandatory")
_RateLimitPortEgrRate_Type = Integer32
_RateLimitPortEgrRate_Object = MibTableColumn
rateLimitPortEgrRate = _RateLimitPortEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2, 1, 3),
    _RateLimitPortEgrRate_Type()
)
rateLimitPortEgrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrRate.setStatus("mandatory")
_RateLimitPortStateIngress_Type = EnabledStatus
_RateLimitPortStateIngress_Object = MibTableColumn
rateLimitPortStateIngress = _RateLimitPortStateIngress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2, 1, 5),
    _RateLimitPortStateIngress_Type()
)
rateLimitPortStateIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortStateIngress.setStatus("mandatory")
_RateLimitPortStateEgress_Type = EnabledStatus
_RateLimitPortStateEgress_Object = MibTableColumn
rateLimitPortStateEgress = _RateLimitPortStateEgress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 2, 2, 1, 6),
    _RateLimitPortStateEgress_Type()
)
rateLimitPortStateEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortStateEgress.setStatus("mandatory")
_BrLimitSetup_ObjectIdentity = ObjectIdentity
brLimitSetup = _BrLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 3)
)
_BrLimitState_Type = EnabledStatus
_BrLimitState_Object = MibScalar
brLimitState = _BrLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 3, 1),
    _BrLimitState_Type()
)
brLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitState.setStatus("mandatory")
_BrLimitPortTable_Object = MibTable
brLimitPortTable = _BrLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 3, 2)
)
if mibBuilder.loadTexts:
    brLimitPortTable.setStatus("mandatory")
_BrLimitPortEntry_Object = MibTableRow
brLimitPortEntry = _BrLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 3, 2, 1)
)
brLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    brLimitPortEntry.setStatus("mandatory")
_BrLimitPortState_Type = EnabledStatus
_BrLimitPortState_Object = MibTableColumn
brLimitPortState = _BrLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 3, 2, 1, 1),
    _BrLimitPortState_Type()
)
brLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortState.setStatus("mandatory")
_BrLimitPortRate_Type = Integer32
_BrLimitPortRate_Object = MibTableColumn
brLimitPortRate = _BrLimitPortRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 3, 2, 1, 2),
    _BrLimitPortRate_Type()
)
brLimitPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortRate.setStatus("mandatory")
_PortSecuritySetup_ObjectIdentity = ObjectIdentity
portSecuritySetup = _PortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4)
)
_PortSecurityState_Type = EnabledStatus
_PortSecurityState_Object = MibScalar
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 1),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("mandatory")
_PortSecurityPortTable_Object = MibTable
portSecurityPortTable = _PortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 2)
)
if mibBuilder.loadTexts:
    portSecurityPortTable.setStatus("mandatory")
_PortSecurityPortEntry_Object = MibTableRow
portSecurityPortEntry = _PortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 2, 1)
)
portSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portSecurityPortEntry.setStatus("mandatory")
_PortSecurityPortState_Type = EnabledStatus
_PortSecurityPortState_Object = MibTableColumn
portSecurityPortState = _PortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 2, 1, 1),
    _PortSecurityPortState_Type()
)
portSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortState.setStatus("mandatory")
_PortSecurityPortLearnState_Type = EnabledStatus
_PortSecurityPortLearnState_Object = MibTableColumn
portSecurityPortLearnState = _PortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 2, 1, 2),
    _PortSecurityPortLearnState_Type()
)
portSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setStatus("mandatory")
_PortSecurityPortCount_Type = Integer32
_PortSecurityPortCount_Object = MibTableColumn
portSecurityPortCount = _PortSecurityPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 2, 1, 3),
    _PortSecurityPortCount_Type()
)
portSecurityPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortCount.setStatus("mandatory")
_PortSecurityMacFreeze_Type = PortList
_PortSecurityMacFreeze_Object = MibScalar
portSecurityMacFreeze = _PortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 4, 3),
    _PortSecurityMacFreeze_Type()
)
portSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacFreeze.setStatus("mandatory")
_VlanTrunkSetup_ObjectIdentity = ObjectIdentity
vlanTrunkSetup = _VlanTrunkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 5)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("mandatory")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 5, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("mandatory")
_VlanTrunkPortState_Type = EnabledStatus
_VlanTrunkPortState_Object = MibTableColumn
vlanTrunkPortState = _VlanTrunkPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 5, 1, 1, 1),
    _VlanTrunkPortState_Type()
)
vlanTrunkPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setStatus("mandatory")
_Dot1xSetup_ObjectIdentity = ObjectIdentity
dot1xSetup = _Dot1xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6)
)
_PortAuthState_Type = EnabledStatus
_PortAuthState_Object = MibScalar
portAuthState = _PortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6, 3),
    _PortAuthState_Type()
)
portAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthState.setStatus("mandatory")
_PortAuthTable_Object = MibTable
portAuthTable = _PortAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6, 4)
)
if mibBuilder.loadTexts:
    portAuthTable.setStatus("mandatory")
_PortAuthEntry_Object = MibTableRow
portAuthEntry = _PortAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6, 4, 1)
)
portAuthEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portAuthEntry.setStatus("mandatory")
_PortAuthEntryState_Type = EnabledStatus
_PortAuthEntryState_Object = MibTableColumn
portAuthEntryState = _PortAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6, 4, 1, 1),
    _PortAuthEntryState_Type()
)
portAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthEntryState.setStatus("mandatory")
_PortReAuthEntryState_Type = EnabledStatus
_PortReAuthEntryState_Object = MibTableColumn
portReAuthEntryState = _PortReAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6, 4, 1, 2),
    _PortReAuthEntryState_Type()
)
portReAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryState.setStatus("mandatory")
_PortReAuthEntryTimer_Type = Integer32
_PortReAuthEntryTimer_Object = MibTableColumn
portReAuthEntryTimer = _PortReAuthEntryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 6, 4, 1, 3),
    _PortReAuthEntryTimer_Type()
)
portReAuthEntryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryTimer.setStatus("mandatory")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7)
)
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 1),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("mandatory")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 2),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("mandatory")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 3),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("mandatory")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("mandatory")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4, 1, 1),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("mandatory")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4, 1, 2),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("mandatory")
_SnmpTrapDestPort_Type = Integer32
_SnmpTrapDestPort_Object = MibTableColumn
snmpTrapDestPort = _SnmpTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4, 1, 4),
    _SnmpTrapVersion_Type()
)
snmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVersion.setStatus("mandatory")
_SnmpTrapUserName_Type = DisplayString
_SnmpTrapUserName_Object = MibTableColumn
snmpTrapUserName = _SnmpTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 5),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("mandatory")
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 6)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 6, 1)
)
snmpUserEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "snmpUserName"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")
_SnmpUserName_Type = DisplayString
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 6, 1, 4),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")
_SnmpTrapGroupTable_Object = MibTable
snmpTrapGroupTable = _SnmpTrapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7)
)
if mibBuilder.loadTexts:
    snmpTrapGroupTable.setStatus("mandatory")
_SnmpTrapGroupEntry_Object = MibTableRow
snmpTrapGroupEntry = _SnmpTrapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7, 1)
)
snmpTrapGroupEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapGroupEntry.setStatus("mandatory")


class _SnmpTrapSystemGroup_Type(Bits):
    """Custom type snmpTrapSystemGroup based on Bits"""
    namedValues = NamedValues(
        *(("coldStart", 0),
          ("warmStart", 1),
          ("reset", 5),
          ("timeSync", 6),
          ("intrusionlock", 7),
          ("loopGuard", 13))
    )

_SnmpTrapSystemGroup_Type.__name__ = "Bits"
_SnmpTrapSystemGroup_Object = MibTableColumn
snmpTrapSystemGroup = _SnmpTrapSystemGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7, 1, 1),
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
          ("autonegotiation", 2))
    )

_SnmpTrapInterfaceGroup_Type.__name__ = "Bits"
_SnmpTrapInterfaceGroup_Object = MibTableColumn
snmpTrapInterfaceGroup = _SnmpTrapInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7, 1, 4),
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
          ("rmon", 2))
    )

_SnmpTrapSwitchGroup_Type.__name__ = "Bits"
_SnmpTrapSwitchGroup_Object = MibTableColumn
snmpTrapSwitchGroup = _SnmpTrapSwitchGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 7, 7, 1, 5),
    _SnmpTrapSwitchGroup_Type()
)
snmpTrapSwitchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSwitchGroup.setStatus("mandatory")
_DateTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeSetup = _DateTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 1),
    _DateTimeServerType_Type()
)
dateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerType.setStatus("mandatory")
_DateTimeServerIP_Type = IpAddress
_DateTimeServerIP_Object = MibScalar
dateTimeServerIP = _DateTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 2),
    _DateTimeServerIP_Type()
)
dateTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIP.setStatus("mandatory")
_DateTimeZone_Type = Integer32
_DateTimeZone_Object = MibScalar
dateTimeZone = _DateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 3),
    _DateTimeZone_Type()
)
dateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeZone.setStatus("mandatory")
_DateTimeNewDateYear_Type = Integer32
_DateTimeNewDateYear_Object = MibScalar
dateTimeNewDateYear = _DateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 4),
    _DateTimeNewDateYear_Type()
)
dateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setStatus("mandatory")
_DateTimeNewDateMonth_Type = Integer32
_DateTimeNewDateMonth_Object = MibScalar
dateTimeNewDateMonth = _DateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 5),
    _DateTimeNewDateMonth_Type()
)
dateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setStatus("mandatory")
_DateTimeNewDateDay_Type = Integer32
_DateTimeNewDateDay_Object = MibScalar
dateTimeNewDateDay = _DateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 6),
    _DateTimeNewDateDay_Type()
)
dateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setStatus("mandatory")
_DateTimeNewTimeHour_Type = Integer32
_DateTimeNewTimeHour_Object = MibScalar
dateTimeNewTimeHour = _DateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 7),
    _DateTimeNewTimeHour_Type()
)
dateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setStatus("mandatory")
_DateTimeNewTimeMinute_Type = Integer32
_DateTimeNewTimeMinute_Object = MibScalar
dateTimeNewTimeMinute = _DateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 8),
    _DateTimeNewTimeMinute_Type()
)
dateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setStatus("mandatory")
_DateTimeNewTimeSecond_Type = Integer32
_DateTimeNewTimeSecond_Object = MibScalar
dateTimeNewTimeSecond = _DateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 9),
    _DateTimeNewTimeSecond_Type()
)
dateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setStatus("mandatory")
_DateTimeDaylightSavingTimeSetup_ObjectIdentity = ObjectIdentity
dateTimeDaylightSavingTimeSetup = _DateTimeDaylightSavingTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10)
)
_DaylightSavingTimeState_Type = EnabledStatus
_DaylightSavingTimeState_Object = MibScalar
daylightSavingTimeState = _DaylightSavingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 4),
    _DaylightSavingTimeStartDateMonth_Type()
)
daylightSavingTimeStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeStartDateMonth.setStatus("mandatory")
_DaylightSavingTimeStartDateHour_Type = Integer32
_DaylightSavingTimeStartDateHour_Object = MibScalar
daylightSavingTimeStartDateHour = _DaylightSavingTimeStartDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 7),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 8),
    _DaylightSavingTimeEndDateMonth_Type()
)
daylightSavingTimeEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateMonth.setStatus("mandatory")
_DaylightSavingTimeEndDateHour_Type = Integer32
_DaylightSavingTimeEndDateHour_Object = MibScalar
daylightSavingTimeEndDateHour = _DaylightSavingTimeEndDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 8, 10, 9),
    _DaylightSavingTimeEndDateHour_Type()
)
daylightSavingTimeEndDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingTimeEndDateHour.setStatus("mandatory")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 9)
)


class _SysMgmtConfigSave_Type(Integer32):
    """Custom type sysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("config", 1)
    )


_SysMgmtConfigSave_Type.__name__ = "Integer32"
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 9, 1),
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
            1
        )
    )
    namedValues = NamedValues(
        ("config", 1)
    )


_SysMgmtBootupConfig_Type.__name__ = "Integer32"
_SysMgmtBootupConfig_Object = MibScalar
sysMgmtBootupConfig = _SysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 9, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 9, 3),
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
          ("reset_to_default", 1))
    )


_SysMgmtDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtDefaultConfig_Object = MibScalar
sysMgmtDefaultConfig = _SysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 9, 5),
    _SysMgmtLastActionStatus_Type()
)
sysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setStatus("mandatory")
_Layer2Setup_ObjectIdentity = ObjectIdentity
layer2Setup = _Layer2Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10)
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
          ("port_based", 2))
    )


_VlanTypeSetup_Type.__name__ = "Integer32"
_VlanTypeSetup_Object = MibScalar
vlanTypeSetup = _VlanTypeSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 1),
    _VlanTypeSetup_Type()
)
vlanTypeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTypeSetup.setStatus("mandatory")
_IgmpSnoopingStateSetup_Type = EnabledStatus
_IgmpSnoopingStateSetup_Object = MibScalar
igmpSnoopingStateSetup = _IgmpSnoopingStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 2),
    _IgmpSnoopingStateSetup_Type()
)
igmpSnoopingStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingStateSetup.setStatus("mandatory")
_TagVlanPortIsolationState_Type = EnabledStatus
_TagVlanPortIsolationState_Object = MibScalar
tagVlanPortIsolationState = _TagVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 3),
    _TagVlanPortIsolationState_Type()
)
tagVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanPortIsolationState.setStatus("mandatory")
_StpState_Type = EnabledStatus
_StpState_Object = MibScalar
stpState = _StpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 4),
    _StpState_Type()
)
stpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpState.setStatus("mandatory")
_TagVlanIngressCheckState_Type = EnabledStatus
_TagVlanIngressCheckState_Object = MibScalar
tagVlanIngressCheckState = _TagVlanIngressCheckState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 5),
    _TagVlanIngressCheckState_Type()
)
tagVlanIngressCheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanIngressCheckState.setStatus("mandatory")
_IgmpFilteringStateSetup_Type = EnabledStatus
_IgmpFilteringStateSetup_Object = MibScalar
igmpFilteringStateSetup = _IgmpFilteringStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 7),
    _UnknownMulticastFrameForwarding_Type()
)
unknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownMulticastFrameForwarding.setStatus("mandatory")
_MulticastGrpHostTimeOut_Type = Integer32
_MulticastGrpHostTimeOut_Object = MibScalar
multicastGrpHostTimeOut = _MulticastGrpHostTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 8),
    _MulticastGrpHostTimeOut_Type()
)
multicastGrpHostTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastGrpHostTimeOut.setStatus("mandatory")
_MulticastGrpLeaveTimeOut_Type = Integer32
_MulticastGrpLeaveTimeOut_Object = MibScalar
multicastGrpLeaveTimeOut = _MulticastGrpLeaveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 9),
    _MulticastGrpLeaveTimeOut_Type()
)
multicastGrpLeaveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastGrpLeaveTimeOut.setStatus("mandatory")
_Igmpsnp8021pPriority_Type = Integer32
_Igmpsnp8021pPriority_Object = MibScalar
igmpsnp8021pPriority = _Igmpsnp8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 10),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 11),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("mstp", 3))
    )


_StpMode_Type.__name__ = "Integer32"
_StpMode_Object = MibScalar
stpMode = _StpMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 12),
    _StpMode_Type()
)
stpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMode.setStatus("mandatory")
_IgmpsnpVlanTable_Object = MibTable
igmpsnpVlanTable = _IgmpsnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 13)
)
if mibBuilder.loadTexts:
    igmpsnpVlanTable.setStatus("mandatory")
_IgmpsnpVlanEntry_Object = MibTableRow
igmpsnpVlanEntry = _IgmpsnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 13, 1)
)
igmpsnpVlanEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "igmpsnpVid"),
)
if mibBuilder.loadTexts:
    igmpsnpVlanEntry.setStatus("mandatory")
_IgmpsnpVid_Type = Integer32
_IgmpsnpVid_Object = MibTableColumn
igmpsnpVid = _IgmpsnpVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 13, 1, 1),
    _IgmpsnpVid_Type()
)
igmpsnpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpsnpVid.setStatus("mandatory")
_IgmpsnpVlanName_Type = DisplayString
_IgmpsnpVlanName_Object = MibTableColumn
igmpsnpVlanName = _IgmpsnpVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 13, 1, 2),
    _IgmpsnpVlanName_Type()
)
igmpsnpVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpVlanName.setStatus("mandatory")
_IgmpsnpVlanRowStatus_Type = RowStatus
_IgmpsnpVlanRowStatus_Object = MibTableColumn
igmpsnpVlanRowStatus = _IgmpsnpVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 13, 1, 3),
    _IgmpsnpVlanRowStatus_Type()
)
igmpsnpVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpsnpVlanRowStatus.setStatus("mandatory")
_IgmpsnpQuerierMode_Type = EnabledStatus
_IgmpsnpQuerierMode_Object = MibScalar
igmpsnpQuerierMode = _IgmpsnpQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 10, 14),
    _IgmpsnpQuerierMode_Type()
)
igmpsnpQuerierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpsnpQuerierMode.setStatus("mandatory")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11)
)
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibScalar
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("mandatory")
_DefaultMgmtIpSetup_ObjectIdentity = ObjectIdentity
defaultMgmtIpSetup = _DefaultMgmtIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 2)
)


class _DefaultMgmtIpType_Type(Integer32):
    """Custom type defaultMgmtIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp_client", 0),
          ("static_ip", 1))
    )


_DefaultMgmtIpType_Type.__name__ = "Integer32"
_DefaultMgmtIpType_Object = MibScalar
defaultMgmtIpType = _DefaultMgmtIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 2, 1),
    _DefaultMgmtIpType_Type()
)
defaultMgmtIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmtIpType.setStatus("mandatory")
_DefaultMgmtVid_Type = Integer32
_DefaultMgmtVid_Object = MibScalar
defaultMgmtVid = _DefaultMgmtVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 2, 2),
    _DefaultMgmtVid_Type()
)
defaultMgmtVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmtVid.setStatus("mandatory")
_DefaultMgmtStaticIp_Type = IpAddress
_DefaultMgmtStaticIp_Object = MibScalar
defaultMgmtStaticIp = _DefaultMgmtStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 2, 3),
    _DefaultMgmtStaticIp_Type()
)
defaultMgmtStaticIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmtStaticIp.setStatus("mandatory")
_DefaultMgmtStaticSubnetMask_Type = IpAddress
_DefaultMgmtStaticSubnetMask_Object = MibScalar
defaultMgmtStaticSubnetMask = _DefaultMgmtStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 2, 4),
    _DefaultMgmtStaticSubnetMask_Type()
)
defaultMgmtStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmtStaticSubnetMask.setStatus("mandatory")
_DefaultMgmtStaticGateway_Type = IpAddress
_DefaultMgmtStaticGateway_Object = MibScalar
defaultMgmtStaticGateway = _DefaultMgmtStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 2, 5),
    _DefaultMgmtStaticGateway_Type()
)
defaultMgmtStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmtStaticGateway.setStatus("mandatory")
_MaxNumOfMgmtIp_Type = Integer32
_MaxNumOfMgmtIp_Object = MibScalar
maxNumOfMgmtIp = _MaxNumOfMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 3),
    _MaxNumOfMgmtIp_Type()
)
maxNumOfMgmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfMgmtIp.setStatus("mandatory")
_MgmtIpTable_Object = MibTable
mgmtIpTable = _MgmtIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6)
)
if mibBuilder.loadTexts:
    mgmtIpTable.setStatus("mandatory")
_MgmtIpEntry_Object = MibTableRow
mgmtIpEntry = _MgmtIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1)
)
mgmtIpEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mgmtEntryIp"),
    (0, "ZYXEL-ES2108G-MIB", "mgmtEntryVid"),
)
if mibBuilder.loadTexts:
    mgmtIpEntry.setStatus("mandatory")
_MgmtEntryIp_Type = IpAddress
_MgmtEntryIp_Object = MibTableColumn
mgmtEntryIp = _MgmtEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1, 1),
    _MgmtEntryIp_Type()
)
mgmtEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtEntryIp.setStatus("mandatory")
_MgmtEntrySubnetMask_Type = IpAddress
_MgmtEntrySubnetMask_Object = MibTableColumn
mgmtEntrySubnetMask = _MgmtEntrySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1, 2),
    _MgmtEntrySubnetMask_Type()
)
mgmtEntrySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtEntrySubnetMask.setStatus("mandatory")
_MgmtEntryGateway_Type = IpAddress
_MgmtEntryGateway_Object = MibTableColumn
mgmtEntryGateway = _MgmtEntryGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1, 3),
    _MgmtEntryGateway_Type()
)
mgmtEntryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtEntryGateway.setStatus("mandatory")
_MgmtEntryVid_Type = Integer32
_MgmtEntryVid_Object = MibTableColumn
mgmtEntryVid = _MgmtEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1, 4),
    _MgmtEntryVid_Type()
)
mgmtEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtEntryVid.setStatus("mandatory")
_MgmtEntryManageable_Type = EnabledStatus
_MgmtEntryManageable_Object = MibTableColumn
mgmtEntryManageable = _MgmtEntryManageable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1, 5),
    _MgmtEntryManageable_Type()
)
mgmtEntryManageable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtEntryManageable.setStatus("mandatory")
_MgmtEntryRowStatus_Type = RowStatus
_MgmtEntryRowStatus_Object = MibTableColumn
mgmtEntryRowStatus = _MgmtEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 11, 6, 1, 6),
    _MgmtEntryRowStatus_Type()
)
mgmtEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmtEntryRowStatus.setStatus("mandatory")
_FilterSetup_ObjectIdentity = ObjectIdentity
filterSetup = _FilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "filterMacAddr"),
    (0, "ZYXEL-ES2108G-MIB", "filterVid"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterName_Type = DisplayString
_FilterName_Object = MibTableColumn
filterName = _FilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12, 1, 1, 1),
    _FilterName_Type()
)
filterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterName.setStatus("mandatory")
_FilterMacAddr_Type = MacAddress
_FilterMacAddr_Object = MibTableColumn
filterMacAddr = _FilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12, 1, 1, 2),
    _FilterMacAddr_Type()
)
filterMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterMacAddr.setStatus("mandatory")
_FilterVid_Type = Integer32
_FilterVid_Object = MibTableColumn
filterVid = _FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12, 1, 1, 3),
    _FilterVid_Type()
)
filterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterVid.setStatus("mandatory")
_FilterRowStatus_Type = RowStatus
_FilterRowStatus_Object = MibTableColumn
filterRowStatus = _FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 12, 1, 1, 4),
    _FilterRowStatus_Type()
)
filterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRowStatus.setStatus("mandatory")
_MirrorSetup_ObjectIdentity = ObjectIdentity
mirrorSetup = _MirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13)
)
_MirrorState_Type = EnabledStatus
_MirrorState_Object = MibScalar
mirrorState = _MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 1),
    _MirrorState_Type()
)
mirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorState.setStatus("mandatory")
_MirrorMonitorPort_Type = Integer32
_MirrorMonitorPort_Object = MibScalar
mirrorMonitorPort = _MirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 2),
    _MirrorMonitorPort_Type()
)
mirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMonitorPort.setStatus("mandatory")


class _MirrorIngActionState_Type(Integer32):
    """Custom type mirrorIngActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("destination_mac", 1),
          ("source_mac", 2))
    )


_MirrorIngActionState_Type.__name__ = "Integer32"
_MirrorIngActionState_Object = MibScalar
mirrorIngActionState = _MirrorIngActionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 3),
    _MirrorIngActionState_Type()
)
mirrorIngActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorIngActionState.setStatus("mandatory")
_MirrorIngMacAddr_Type = MacAddress
_MirrorIngMacAddr_Object = MibScalar
mirrorIngMacAddr = _MirrorIngMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 4),
    _MirrorIngMacAddr_Type()
)
mirrorIngMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorIngMacAddr.setStatus("mandatory")


class _MirrorEgrActionState_Type(Integer32):
    """Custom type mirrorEgrActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("destination_mac", 1),
          ("source_mac", 2))
    )


_MirrorEgrActionState_Type.__name__ = "Integer32"
_MirrorEgrActionState_Object = MibScalar
mirrorEgrActionState = _MirrorEgrActionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 5),
    _MirrorEgrActionState_Type()
)
mirrorEgrActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorEgrActionState.setStatus("mandatory")
_MirrorEgrMacAddr_Type = MacAddress
_MirrorEgrMacAddr_Object = MibScalar
mirrorEgrMacAddr = _MirrorEgrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 6),
    _MirrorEgrMacAddr_Type()
)
mirrorEgrMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorEgrMacAddr.setStatus("mandatory")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 7)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("mandatory")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 7, 1)
)
mirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("mandatory")
_MirrorMirroredState_Type = EnabledStatus
_MirrorMirroredState_Object = MibTableColumn
mirrorMirroredState = _MirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 13, 7, 1, 2),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("mandatory")
_AggrSetup_ObjectIdentity = ObjectIdentity
aggrSetup = _AggrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14)
)
_AggrState_Type = EnabledStatus
_AggrState_Object = MibScalar
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 1),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrState.setStatus("mandatory")
_AggrSystemPriority_Type = Integer32
_AggrSystemPriority_Object = MibScalar
aggrSystemPriority = _AggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 2),
    _AggrSystemPriority_Type()
)
aggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrSystemPriority.setStatus("mandatory")
_AggrGroupTable_Object = MibTable
aggrGroupTable = _AggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 3)
)
if mibBuilder.loadTexts:
    aggrGroupTable.setStatus("mandatory")
_AggrGroupEntry_Object = MibTableRow
aggrGroupEntry = _AggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 3, 1)
)
aggrGroupEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrGroupEntry.setStatus("mandatory")
_AggrGroupIndex_Type = Integer32
_AggrGroupIndex_Object = MibTableColumn
aggrGroupIndex = _AggrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 3, 1, 1),
    _AggrGroupIndex_Type()
)
aggrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrGroupIndex.setStatus("mandatory")
_AggrGroupState_Type = EnabledStatus
_AggrGroupState_Object = MibTableColumn
aggrGroupState = _AggrGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 3, 1, 2),
    _AggrGroupState_Type()
)
aggrGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupState.setStatus("mandatory")
_AggrGroupDynamicState_Type = EnabledStatus
_AggrGroupDynamicState_Object = MibTableColumn
aggrGroupDynamicState = _AggrGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 3, 1, 3),
    _AggrGroupDynamicState_Type()
)
aggrGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupDynamicState.setStatus("mandatory")
_AggrPortTable_Object = MibTable
aggrPortTable = _AggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 4)
)
if mibBuilder.loadTexts:
    aggrPortTable.setStatus("mandatory")
_AggrPortEntry_Object = MibTableRow
aggrPortEntry = _AggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 4, 1, 1),
    _AggrPortGroup_Type()
)
aggrPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortGroup.setStatus("mandatory")
_AggrPortDynamicStateTimeout_Type = Integer32
_AggrPortDynamicStateTimeout_Object = MibTableColumn
aggrPortDynamicStateTimeout = _AggrPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 14, 4, 1, 2),
    _AggrPortDynamicStateTimeout_Type()
)
aggrPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortDynamicStateTimeout.setStatus("mandatory")
_AccessCtlSetup_ObjectIdentity = ObjectIdentity
accessCtlSetup = _AccessCtlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15)
)
_AccessCtlTable_Object = MibTable
accessCtlTable = _AccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 1)
)
if mibBuilder.loadTexts:
    accessCtlTable.setStatus("mandatory")
_AccessCtlEntry_Object = MibTableRow
accessCtlEntry = _AccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 1, 1)
)
accessCtlEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "accessCtlService"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 1, 1, 1),
    _AccessCtlService_Type()
)
accessCtlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtlService.setStatus("mandatory")
_AccessCtlEnable_Type = EnabledStatus
_AccessCtlEnable_Object = MibTableColumn
accessCtlEnable = _AccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 1, 1, 2),
    _AccessCtlEnable_Type()
)
accessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlEnable.setStatus("mandatory")
_AccessCtlServicePort_Type = Integer32
_AccessCtlServicePort_Object = MibTableColumn
accessCtlServicePort = _AccessCtlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 1, 1, 3),
    _AccessCtlServicePort_Type()
)
accessCtlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlServicePort.setStatus("mandatory")
_AccessCtlTimeout_Type = Integer32
_AccessCtlTimeout_Object = MibTableColumn
accessCtlTimeout = _AccessCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 1, 1, 4),
    _AccessCtlTimeout_Type()
)
accessCtlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlTimeout.setStatus("mandatory")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("mandatory")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("mandatory")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("mandatory")
_SecuredClientEnable_Type = EnabledStatus
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2, 1, 2),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("mandatory")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2, 1, 3),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("mandatory")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 15, 2, 1, 5),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("mandatory")
_QueuingMethodSetup_ObjectIdentity = ObjectIdentity
queuingMethodSetup = _QueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 16)
)


class _QueuingMethodType_Type(Integer32):
    """Custom type queuingMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strictly_priority", 0),
          ("weighted_round_robin_scheduling", 1))
    )


_QueuingMethodType_Type.__name__ = "Integer32"
_QueuingMethodType_Object = MibScalar
queuingMethodType = _QueuingMethodType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 16, 1),
    _QueuingMethodType_Type()
)
queuingMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMethodType.setStatus("mandatory")
_QueuingMethodTable_Object = MibTable
queuingMethodTable = _QueuingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 16, 2)
)
if mibBuilder.loadTexts:
    queuingMethodTable.setStatus("mandatory")
_QueuingMethodEntry_Object = MibTableRow
queuingMethodEntry = _QueuingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 16, 2, 1)
)
queuingMethodEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "queuingMethodQueue"),
)
if mibBuilder.loadTexts:
    queuingMethodEntry.setStatus("mandatory")
_QueuingMethodQueue_Type = Integer32
_QueuingMethodQueue_Object = MibTableColumn
queuingMethodQueue = _QueuingMethodQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 16, 2, 1, 1),
    _QueuingMethodQueue_Type()
)
queuingMethodQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuingMethodQueue.setStatus("mandatory")
_QueuingMethodWeight_Type = Integer32
_QueuingMethodWeight_Object = MibTableColumn
queuingMethodWeight = _QueuingMethodWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 16, 2, 1, 2),
    _QueuingMethodWeight_Type()
)
queuingMethodWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMethodWeight.setStatus("mandatory")
_StaticRouteSetup_ObjectIdentity = ObjectIdentity
staticRouteSetup = _StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17)
)
_MaxNumberOfStaticRoutes_Type = Integer32
_MaxNumberOfStaticRoutes_Object = MibScalar
maxNumberOfStaticRoutes = _MaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 1),
    _MaxNumberOfStaticRoutes_Type()
)
maxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfStaticRoutes.setStatus("mandatory")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("mandatory")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "staticRouteIp"),
    (0, "ZYXEL-ES2108G-MIB", "staticRouteMask"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("mandatory")
_StaticRouteName_Type = DisplayString
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("mandatory")
_StaticRouteIp_Type = IpAddress
_StaticRouteIp_Object = MibTableColumn
staticRouteIp = _StaticRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1, 2),
    _StaticRouteIp_Type()
)
staticRouteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteIp.setStatus("mandatory")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("mandatory")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("mandatory")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("mandatory")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 17, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("mandatory")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("mandatory")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1, 1)
)
arpEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "arpIpAddr"),
    (0, "ZYXEL-ES2108G-MIB", "arpMacVid"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("mandatory")
_ArpIndex_Type = Integer32
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("mandatory")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("mandatory")
_ArpMacAddr_Type = MacAddress
_ArpMacAddr_Object = MibTableColumn
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1, 1, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("mandatory")
_ArpMacVid_Type = Integer32
_ArpMacVid_Object = MibTableColumn
arpMacVid = _ArpMacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1, 1, 4),
    _ArpMacVid_Type()
)
arpMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacVid.setStatus("mandatory")
_ArpType_Type = Integer32
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 18, 1, 1, 5),
    _ArpType_Type()
)
arpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpType.setStatus("mandatory")
_PortOpModeSetup_ObjectIdentity = ObjectIdentity
portOpModeSetup = _PortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19)
)
_PortOpModePortTable_Object = MibTable
portOpModePortTable = _PortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1)
)
if mibBuilder.loadTexts:
    portOpModePortTable.setStatus("mandatory")
_PortOpModePortEntry_Object = MibTableRow
portOpModePortEntry = _PortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1)
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed_10_half", 1),
          ("speed_10_full", 2),
          ("speed_100_half", 3),
          ("speed_100_full", 4),
          ("speed_1000_full", 5))
    )


_PortOpModePortSpeedDuplex_Type.__name__ = "Integer32"
_PortOpModePortSpeedDuplex_Object = MibTableColumn
portOpModePortSpeedDuplex = _PortOpModePortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 2),
    _PortOpModePortFlowCntl_Type()
)
portOpModePortFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortFlowCntl.setStatus("mandatory")


class _PortOpModePortName_Type(OctetString):
    """Custom type portOpModePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpModePortName_Type.__name__ = "OctetString"
_PortOpModePortName_Object = MibTableColumn
portOpModePortName = _PortOpModePortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 3),
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
        *(("fast_ethernet_10_100", 0),
          ("gigabit_ethernet_100_1000", 1))
    )


_PortOpModePortModuleType_Type.__name__ = "Integer32"
_PortOpModePortModuleType_Object = MibTableColumn
portOpModePortModuleType = _PortOpModePortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 5),
    _PortOpModePortLinkUpType_Type()
)
portOpModePortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLinkUpType.setStatus("mandatory")
_PortOpModePortIntrusionLock_Type = EnabledStatus
_PortOpModePortIntrusionLock_Object = MibTableColumn
portOpModePortIntrusionLock = _PortOpModePortIntrusionLock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 6),
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
          ("underTesting", 1),
          ("success", 2),
          ("fail", 3))
    )


_PortOpModePortLBTestStatus_Type.__name__ = "Integer32"
_PortOpModePortLBTestStatus_Object = MibTableColumn
portOpModePortLBTestStatus = _PortOpModePortLBTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 19, 1, 1, 7),
    _PortOpModePortLBTestStatus_Type()
)
portOpModePortLBTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBTestStatus.setStatus("mandatory")
_PortBasedVlanSetup_ObjectIdentity = ObjectIdentity
portBasedVlanSetup = _PortBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 20)
)
_PortBasedVlanPortListTable_Object = MibTable
portBasedVlanPortListTable = _PortBasedVlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 20, 1)
)
if mibBuilder.loadTexts:
    portBasedVlanPortListTable.setStatus("mandatory")
_PortBasedVlanPortListEntry_Object = MibTableRow
portBasedVlanPortListEntry = _PortBasedVlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 20, 1, 1)
)
portBasedVlanPortListEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBasedVlanPortListEntry.setStatus("mandatory")
_PortBasedVlanPortListMembers_Type = PortList
_PortBasedVlanPortListMembers_Object = MibTableColumn
portBasedVlanPortListMembers = _PortBasedVlanPortListMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 20, 1, 1, 1),
    _PortBasedVlanPortListMembers_Type()
)
portBasedVlanPortListMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedVlanPortListMembers.setStatus("mandatory")
_DiffservSetup_ObjectIdentity = ObjectIdentity
diffservSetup = _DiffservSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21)
)
_DiffservState_Type = EnabledStatus
_DiffservState_Object = MibScalar
diffservState = _DiffservState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 1),
    _DiffservState_Type()
)
diffservState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservState.setStatus("mandatory")
_DiffservMapTable_Object = MibTable
diffservMapTable = _DiffservMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 2)
)
if mibBuilder.loadTexts:
    diffservMapTable.setStatus("mandatory")
_DiffservMapEntry_Object = MibTableRow
diffservMapEntry = _DiffservMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 2, 1)
)
diffservMapEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "diffservMapDscp"),
)
if mibBuilder.loadTexts:
    diffservMapEntry.setStatus("mandatory")
_DiffservMapDscp_Type = Integer32
_DiffservMapDscp_Object = MibTableColumn
diffservMapDscp = _DiffservMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 2, 1, 1),
    _DiffservMapDscp_Type()
)
diffservMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffservMapDscp.setStatus("mandatory")
_DiffservMapPriority_Type = Integer32
_DiffservMapPriority_Object = MibTableColumn
diffservMapPriority = _DiffservMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 2, 1, 2),
    _DiffservMapPriority_Type()
)
diffservMapPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservMapPriority.setStatus("mandatory")
_DiffservPortTable_Object = MibTable
diffservPortTable = _DiffservPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 3)
)
if mibBuilder.loadTexts:
    diffservPortTable.setStatus("mandatory")
_DiffservPortEntry_Object = MibTableRow
diffservPortEntry = _DiffservPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 3, 1)
)
diffservPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    diffservPortEntry.setStatus("mandatory")
_DiffservPortState_Type = EnabledStatus
_DiffservPortState_Object = MibTableColumn
diffservPortState = _DiffservPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 21, 3, 1, 1),
    _DiffservPortState_Type()
)
diffservPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservPortState.setStatus("mandatory")
_ClusterSetup_ObjectIdentity = ObjectIdentity
clusterSetup = _ClusterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22)
)
_ClusterManager_ObjectIdentity = ObjectIdentity
clusterManager = _ClusterManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1)
)
_ClusterMaxNumOfManager_Type = Integer32
_ClusterMaxNumOfManager_Object = MibScalar
clusterMaxNumOfManager = _ClusterMaxNumOfManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1, 1),
    _ClusterMaxNumOfManager_Type()
)
clusterMaxNumOfManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMaxNumOfManager.setStatus("mandatory")
_ClusterManagerTable_Object = MibTable
clusterManagerTable = _ClusterManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1, 2)
)
if mibBuilder.loadTexts:
    clusterManagerTable.setStatus("mandatory")
_ClusterManagerEntry_Object = MibTableRow
clusterManagerEntry = _ClusterManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1, 2, 1)
)
clusterManagerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "clusterManagerVid"),
)
if mibBuilder.loadTexts:
    clusterManagerEntry.setStatus("mandatory")
_ClusterManagerVid_Type = Integer32
_ClusterManagerVid_Object = MibTableColumn
clusterManagerVid = _ClusterManagerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1, 2, 1, 1),
    _ClusterManagerVid_Type()
)
clusterManagerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterManagerVid.setStatus("mandatory")
_ClusterManagerName_Type = DisplayString
_ClusterManagerName_Object = MibTableColumn
clusterManagerName = _ClusterManagerName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1, 2, 1, 2),
    _ClusterManagerName_Type()
)
clusterManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterManagerName.setStatus("mandatory")
_ClusterManagerRowStatus_Type = RowStatus
_ClusterManagerRowStatus_Object = MibTableColumn
clusterManagerRowStatus = _ClusterManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 1, 2, 1, 3),
    _ClusterManagerRowStatus_Type()
)
clusterManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusterManagerRowStatus.setStatus("mandatory")
_ClusterMembers_ObjectIdentity = ObjectIdentity
clusterMembers = _ClusterMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2)
)
_ClusterMaxNumOfMember_Type = Integer32
_ClusterMaxNumOfMember_Object = MibScalar
clusterMaxNumOfMember = _ClusterMaxNumOfMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 1),
    _ClusterMaxNumOfMember_Type()
)
clusterMaxNumOfMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMaxNumOfMember.setStatus("mandatory")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("mandatory")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "clusterMemberMac"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("mandatory")
_ClusterMemberMac_Type = MacAddress
_ClusterMemberMac_Object = MibTableColumn
clusterMemberMac = _ClusterMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2, 1, 1),
    _ClusterMemberMac_Type()
)
clusterMemberMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberMac.setStatus("mandatory")
_ClusterMemberName_Type = DisplayString
_ClusterMemberName_Object = MibTableColumn
clusterMemberName = _ClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2, 1, 2),
    _ClusterMemberName_Type()
)
clusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberName.setStatus("mandatory")
_ClusterMemberModel_Type = DisplayString
_ClusterMemberModel_Object = MibTableColumn
clusterMemberModel = _ClusterMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2, 1, 3),
    _ClusterMemberModel_Type()
)
clusterMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberModel.setStatus("mandatory")
_ClusterMemberPassword_Type = DisplayString
_ClusterMemberPassword_Object = MibTableColumn
clusterMemberPassword = _ClusterMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2, 1, 4),
    _ClusterMemberPassword_Type()
)
clusterMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberPassword.setStatus("mandatory")
_ClusterMemberRowStatus_Type = RowStatus
_ClusterMemberRowStatus_Object = MibTableColumn
clusterMemberRowStatus = _ClusterMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 2, 2, 1, 5),
    _ClusterMemberRowStatus_Type()
)
clusterMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusterMemberRowStatus.setStatus("mandatory")
_ClusterCandidates_ObjectIdentity = ObjectIdentity
clusterCandidates = _ClusterCandidates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 3)
)
_ClusterCandidateTable_Object = MibTable
clusterCandidateTable = _ClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 3, 1)
)
if mibBuilder.loadTexts:
    clusterCandidateTable.setStatus("mandatory")
_ClusterCandidateEntry_Object = MibTableRow
clusterCandidateEntry = _ClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 3, 1, 1)
)
clusterCandidateEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "clusterCandidateMac"),
)
if mibBuilder.loadTexts:
    clusterCandidateEntry.setStatus("mandatory")
_ClusterCandidateMac_Type = MacAddress
_ClusterCandidateMac_Object = MibTableColumn
clusterCandidateMac = _ClusterCandidateMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 3, 1, 1, 1),
    _ClusterCandidateMac_Type()
)
clusterCandidateMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateMac.setStatus("mandatory")
_ClusterCandidateName_Type = DisplayString
_ClusterCandidateName_Object = MibTableColumn
clusterCandidateName = _ClusterCandidateName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 3, 1, 1, 2),
    _ClusterCandidateName_Type()
)
clusterCandidateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateName.setStatus("mandatory")
_ClusterCandidateModel_Type = DisplayString
_ClusterCandidateModel_Object = MibTableColumn
clusterCandidateModel = _ClusterCandidateModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 3, 1, 1, 3),
    _ClusterCandidateModel_Type()
)
clusterCandidateModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateModel.setStatus("mandatory")
_ClusterStatus_ObjectIdentity = ObjectIdentity
clusterStatus = _ClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 1),
    _ClusterStatusRole_Type()
)
clusterStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusRole.setStatus("mandatory")
_ClusterStatusManager_Type = DisplayString
_ClusterStatusManager_Object = MibScalar
clusterStatusManager = _ClusterStatusManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 2),
    _ClusterStatusManager_Type()
)
clusterStatusManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusManager.setStatus("mandatory")
_ClsuterStatusMaxNumOfMember_Type = Integer32
_ClsuterStatusMaxNumOfMember_Object = MibScalar
clsuterStatusMaxNumOfMember = _ClsuterStatusMaxNumOfMember_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 3),
    _ClsuterStatusMaxNumOfMember_Type()
)
clsuterStatusMaxNumOfMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsuterStatusMaxNumOfMember.setStatus("mandatory")
_ClusterStatusMemberTable_Object = MibTable
clusterStatusMemberTable = _ClusterStatusMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 4)
)
if mibBuilder.loadTexts:
    clusterStatusMemberTable.setStatus("mandatory")
_ClusterStatusMemberEntry_Object = MibTableRow
clusterStatusMemberEntry = _ClusterStatusMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 4, 1)
)
clusterStatusMemberEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "clusterStatusMemberMac"),
)
if mibBuilder.loadTexts:
    clusterStatusMemberEntry.setStatus("mandatory")
_ClusterStatusMemberMac_Type = MacAddress
_ClusterStatusMemberMac_Object = MibTableColumn
clusterStatusMemberMac = _ClusterStatusMemberMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 4, 1, 1),
    _ClusterStatusMemberMac_Type()
)
clusterStatusMemberMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberMac.setStatus("mandatory")
_ClusterStatusMemberName_Type = DisplayString
_ClusterStatusMemberName_Object = MibTableColumn
clusterStatusMemberName = _ClusterStatusMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 4, 1, 2),
    _ClusterStatusMemberName_Type()
)
clusterStatusMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberName.setStatus("mandatory")
_ClusterStatusMemberModel_Type = DisplayString
_ClusterStatusMemberModel_Object = MibTableColumn
clusterStatusMemberModel = _ClusterStatusMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 22, 4, 4, 1, 4),
    _ClusterStatusMemberStatus_Type()
)
clusterStatusMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatusMemberStatus.setStatus("mandatory")
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventSeqNum_Type = Integer32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventEventId_Type = EventIdNumber
_EventEventId_Object = MibTableColumn
eventEventId = _EventEventId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventInstanceType_Type = InstanceType
_EventInstanceType_Object = MibTableColumn
eventInstanceType = _EventInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 4),
    _EventInstanceType_Type()
)
eventInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceType.setStatus("current")
_EventInstanceId_Type = DisplayString
_EventInstanceId_Object = MibTableColumn
eventInstanceId = _EventInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 5),
    _EventInstanceId_Type()
)
eventInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceId.setStatus("current")
_EventInstanceName_Type = DisplayString
_EventInstanceName_Object = MibTableColumn
eventInstanceName = _EventInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 6),
    _EventInstanceName_Type()
)
eventInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceName.setStatus("current")
_EventSeverity_Type = EventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventSetTime_Type = UtcTimeStamp
_EventSetTime_Object = MibTableColumn
eventSetTime = _EventSetTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 9),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_EventServAffective_Type = EventServiceAffective
_EventServAffective_Object = MibTableColumn
eventServAffective = _EventServAffective_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 26, 1, 1, 1, 10),
    _EventServAffective_Type()
)
eventServAffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventServAffective.setStatus("current")
_TrapInfoObjects_ObjectIdentity = ObjectIdentity
trapInfoObjects = _TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 1)
)
_TrapRefSeqNum_Type = Integer32
_TrapRefSeqNum_Object = MibScalar
trapRefSeqNum = _TrapRefSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 1, 1),
    _TrapRefSeqNum_Type()
)
trapRefSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRefSeqNum.setStatus("current")
_TrapPersistence_Type = EventPersistence
_TrapPersistence_Object = MibScalar
trapPersistence = _TrapPersistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 1, 2),
    _TrapPersistence_Type()
)
trapPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPersistence.setStatus("current")
_TrapSenderNodeId_Type = Integer32
_TrapSenderNodeId_Object = MibScalar
trapSenderNodeId = _TrapSenderNodeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 1, 3),
    _TrapSenderNodeId_Type()
)
trapSenderNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderNodeId.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 2)
)
_MulticastPortSetup_ObjectIdentity = ObjectIdentity
multicastPortSetup = _MulticastPortSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28)
)
_MulticastPortTable_Object = MibTable
multicastPortTable = _MulticastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1)
)
if mibBuilder.loadTexts:
    multicastPortTable.setStatus("mandatory")
_MulticastPortEntry_Object = MibTableRow
multicastPortEntry = _MulticastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1, 1)
)
multicastPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    multicastPortEntry.setStatus("mandatory")
_MulticastPortImmediateLeave_Type = EnabledStatus
_MulticastPortImmediateLeave_Object = MibTableColumn
multicastPortImmediateLeave = _MulticastPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1, 1, 1),
    _MulticastPortImmediateLeave_Type()
)
multicastPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortImmediateLeave.setStatus("mandatory")
_MulticastPortMaxGroupLimited_Type = EnabledStatus
_MulticastPortMaxGroupLimited_Object = MibTableColumn
multicastPortMaxGroupLimited = _MulticastPortMaxGroupLimited_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1, 1, 2),
    _MulticastPortMaxGroupLimited_Type()
)
multicastPortMaxGroupLimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxGroupLimited.setStatus("mandatory")
_MulticastPortMaxOfGroup_Type = Integer32
_MulticastPortMaxOfGroup_Object = MibTableColumn
multicastPortMaxOfGroup = _MulticastPortMaxOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1, 1, 3),
    _MulticastPortMaxOfGroup_Type()
)
multicastPortMaxOfGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortMaxOfGroup.setStatus("mandatory")
_MulticastPortIgmpFilteringProfile_Type = DisplayString
_MulticastPortIgmpFilteringProfile_Object = MibTableColumn
multicastPortIgmpFilteringProfile = _MulticastPortIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1, 1, 4),
    _MulticastPortIgmpFilteringProfile_Type()
)
multicastPortIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortIgmpFilteringProfile.setStatus("mandatory")


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
        *(("auto_mode", 1),
          ("fix_mode", 2),
          ("edge_mode", 3))
    )


_MulticastPortQueryMode_Type.__name__ = "Integer32"
_MulticastPortQueryMode_Object = MibTableColumn
multicastPortQueryMode = _MulticastPortQueryMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 28, 1, 1, 5),
    _MulticastPortQueryMode_Type()
)
multicastPortQueryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastPortQueryMode.setStatus("mandatory")
_MulticastStatus_ObjectIdentity = ObjectIdentity
multicastStatus = _MulticastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29)
)
_MulticastStatusTable_Object = MibTable
multicastStatusTable = _MulticastStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 1)
)
if mibBuilder.loadTexts:
    multicastStatusTable.setStatus("mandatory")
_MulticastStatusEntry_Object = MibTableRow
multicastStatusEntry = _MulticastStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 1, 1)
)
multicastStatusEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "multicastStatusVlanID"),
    (0, "ZYXEL-ES2108G-MIB", "multicastStatusPort"),
    (0, "ZYXEL-ES2108G-MIB", "multicastStatusGroup"),
)
if mibBuilder.loadTexts:
    multicastStatusEntry.setStatus("mandatory")
_MulticastStatusIndex_Type = Integer32
_MulticastStatusIndex_Object = MibTableColumn
multicastStatusIndex = _MulticastStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 1, 1, 1),
    _MulticastStatusIndex_Type()
)
multicastStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusIndex.setStatus("mandatory")
_MulticastStatusVlanID_Type = Integer32
_MulticastStatusVlanID_Object = MibTableColumn
multicastStatusVlanID = _MulticastStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 1, 1, 2),
    _MulticastStatusVlanID_Type()
)
multicastStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusVlanID.setStatus("mandatory")
_MulticastStatusPort_Type = Integer32
_MulticastStatusPort_Object = MibTableColumn
multicastStatusPort = _MulticastStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 1, 1, 3),
    _MulticastStatusPort_Type()
)
multicastStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusPort.setStatus("mandatory")
_MulticastStatusGroup_Type = IpAddress
_MulticastStatusGroup_Object = MibTableColumn
multicastStatusGroup = _MulticastStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 1, 1, 4),
    _MulticastStatusGroup_Type()
)
multicastStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastStatusGroup.setStatus("mandatory")
_IgmpCountTable_Object = MibTable
igmpCountTable = _IgmpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2)
)
if mibBuilder.loadTexts:
    igmpCountTable.setStatus("mandatory")
_IgmpCountEntry_Object = MibTableRow
igmpCountEntry = _IgmpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1)
)
igmpCountEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "igmpCountIndex"),
)
if mibBuilder.loadTexts:
    igmpCountEntry.setStatus("mandatory")
_IgmpCountIndex_Type = Integer32
_IgmpCountIndex_Object = MibTableColumn
igmpCountIndex = _IgmpCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 1),
    _IgmpCountIndex_Type()
)
igmpCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountIndex.setStatus("mandatory")
_IgmpCountInQuery_Type = Integer32
_IgmpCountInQuery_Object = MibTableColumn
igmpCountInQuery = _IgmpCountInQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 2),
    _IgmpCountInQuery_Type()
)
igmpCountInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInQuery.setStatus("mandatory")
_IgmpCountInReport_Type = Integer32
_IgmpCountInReport_Object = MibTableColumn
igmpCountInReport = _IgmpCountInReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 3),
    _IgmpCountInReport_Type()
)
igmpCountInReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInReport.setStatus("mandatory")
_IgmpCountInLeave_Type = Integer32
_IgmpCountInLeave_Object = MibTableColumn
igmpCountInLeave = _IgmpCountInLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 4),
    _IgmpCountInLeave_Type()
)
igmpCountInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInLeave.setStatus("mandatory")
_IgmpCountInQueryDrop_Type = Integer32
_IgmpCountInQueryDrop_Object = MibTableColumn
igmpCountInQueryDrop = _IgmpCountInQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 5),
    _IgmpCountInQueryDrop_Type()
)
igmpCountInQueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInQueryDrop.setStatus("mandatory")
_IgmpCountInReportDrop_Type = Integer32
_IgmpCountInReportDrop_Object = MibTableColumn
igmpCountInReportDrop = _IgmpCountInReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 6),
    _IgmpCountInReportDrop_Type()
)
igmpCountInReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInReportDrop.setStatus("mandatory")
_IgmpCountInLeaveDrop_Type = Integer32
_IgmpCountInLeaveDrop_Object = MibTableColumn
igmpCountInLeaveDrop = _IgmpCountInLeaveDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 7),
    _IgmpCountInLeaveDrop_Type()
)
igmpCountInLeaveDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountInLeaveDrop.setStatus("mandatory")
_IgmpCountOutQuery_Type = Integer32
_IgmpCountOutQuery_Object = MibTableColumn
igmpCountOutQuery = _IgmpCountOutQuery_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 8),
    _IgmpCountOutQuery_Type()
)
igmpCountOutQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutQuery.setStatus("mandatory")
_IgmpCountOutReport_Type = Integer32
_IgmpCountOutReport_Object = MibTableColumn
igmpCountOutReport = _IgmpCountOutReport_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 9),
    _IgmpCountOutReport_Type()
)
igmpCountOutReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutReport.setStatus("mandatory")
_IgmpCountOutLeave_Type = Integer32
_IgmpCountOutLeave_Object = MibTableColumn
igmpCountOutLeave = _IgmpCountOutLeave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 2, 1, 10),
    _IgmpCountOutLeave_Type()
)
igmpCountOutLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCountOutLeave.setStatus("mandatory")
_MulticastVlanStatusTable_Object = MibTable
multicastVlanStatusTable = _MulticastVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 3)
)
if mibBuilder.loadTexts:
    multicastVlanStatusTable.setStatus("mandatory")
_MulticastVlanStatusEntry_Object = MibTableRow
multicastVlanStatusEntry = _MulticastVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 3, 1)
)
multicastVlanStatusEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "multicastVlanStatusVlanID"),
)
if mibBuilder.loadTexts:
    multicastVlanStatusEntry.setStatus("mandatory")
_MulticastVlanStatusVlanID_Type = Integer32
_MulticastVlanStatusVlanID_Object = MibTableColumn
multicastVlanStatusVlanID = _MulticastVlanStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 3, 1, 2),
    _MulticastVlanStatusType_Type()
)
multicastVlanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanStatusType.setStatus("mandatory")
_MulticastVlanQueryPort_Type = PortList
_MulticastVlanQueryPort_Object = MibTableColumn
multicastVlanQueryPort = _MulticastVlanQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 29, 3, 1, 3),
    _MulticastVlanQueryPort_Type()
)
multicastVlanQueryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastVlanQueryPort.setStatus("mandatory")
_IgmpFilteringProfileSetup_ObjectIdentity = ObjectIdentity
igmpFilteringProfileSetup = _IgmpFilteringProfileSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30)
)
_IgmpFilteringMaxNumberOfProfile_Type = Integer32
_IgmpFilteringMaxNumberOfProfile_Object = MibScalar
igmpFilteringMaxNumberOfProfile = _IgmpFilteringMaxNumberOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 1),
    _IgmpFilteringMaxNumberOfProfile_Type()
)
igmpFilteringMaxNumberOfProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringMaxNumberOfProfile.setStatus("mandatory")
_IgmpFilteringProfileTable_Object = MibTable
igmpFilteringProfileTable = _IgmpFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 2)
)
if mibBuilder.loadTexts:
    igmpFilteringProfileTable.setStatus("mandatory")
_IgmpFilteringProfileEntry_Object = MibTableRow
igmpFilteringProfileEntry = _IgmpFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 2, 1)
)
igmpFilteringProfileEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "igmpFilteringProfileName"),
    (0, "ZYXEL-ES2108G-MIB", "igmpFilteringProfileStartAddress"),
    (0, "ZYXEL-ES2108G-MIB", "igmpFilteringProfileEndAddress"),
)
if mibBuilder.loadTexts:
    igmpFilteringProfileEntry.setStatus("mandatory")
_IgmpFilteringProfileName_Type = DisplayString
_IgmpFilteringProfileName_Object = MibTableColumn
igmpFilteringProfileName = _IgmpFilteringProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 2, 1, 1),
    _IgmpFilteringProfileName_Type()
)
igmpFilteringProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileName.setStatus("mandatory")
_IgmpFilteringProfileStartAddress_Type = IpAddress
_IgmpFilteringProfileStartAddress_Object = MibTableColumn
igmpFilteringProfileStartAddress = _IgmpFilteringProfileStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 2, 1, 2),
    _IgmpFilteringProfileStartAddress_Type()
)
igmpFilteringProfileStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileStartAddress.setStatus("mandatory")
_IgmpFilteringProfileEndAddress_Type = IpAddress
_IgmpFilteringProfileEndAddress_Object = MibTableColumn
igmpFilteringProfileEndAddress = _IgmpFilteringProfileEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 2, 1, 3),
    _IgmpFilteringProfileEndAddress_Type()
)
igmpFilteringProfileEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpFilteringProfileEndAddress.setStatus("mandatory")
_IgmpFilteringProfileRowStatus_Type = RowStatus
_IgmpFilteringProfileRowStatus_Object = MibTableColumn
igmpFilteringProfileRowStatus = _IgmpFilteringProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 30, 2, 1, 4),
    _IgmpFilteringProfileRowStatus_Type()
)
igmpFilteringProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpFilteringProfileRowStatus.setStatus("mandatory")
_MvrSetup_ObjectIdentity = ObjectIdentity
mvrSetup = _MvrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31)
)
_MaxNumberOfMVR_Type = Integer32
_MaxNumberOfMVR_Object = MibScalar
maxNumberOfMVR = _MaxNumberOfMVR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 1),
    _MaxNumberOfMVR_Type()
)
maxNumberOfMVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMVR.setStatus("mandatory")
_MvrTable_Object = MibTable
mvrTable = _MvrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2)
)
if mibBuilder.loadTexts:
    mvrTable.setStatus("mandatory")
_MvrEntry_Object = MibTableRow
mvrEntry = _MvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2, 1)
)
mvrEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mvrVlanID"),
)
if mibBuilder.loadTexts:
    mvrEntry.setStatus("mandatory")
_MvrVlanID_Type = Integer32
_MvrVlanID_Object = MibTableColumn
mvrVlanID = _MvrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2, 1, 1),
    _MvrVlanID_Type()
)
mvrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanID.setStatus("mandatory")
_MvrName_Type = DisplayString
_MvrName_Object = MibTableColumn
mvrName = _MvrName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2, 1, 3),
    _MvrMode_Type()
)
mvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMode.setStatus("mandatory")
_MvrRowStatus_Type = RowStatus
_MvrRowStatus_Object = MibTableColumn
mvrRowStatus = _MvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2, 1, 4),
    _MvrRowStatus_Type()
)
mvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrRowStatus.setStatus("mandatory")
_Mvr8021pPriority_Type = Integer32
_Mvr8021pPriority_Object = MibTableColumn
mvr8021pPriority = _Mvr8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 2, 1, 5),
    _Mvr8021pPriority_Type()
)
mvr8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvr8021pPriority.setStatus("mandatory")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 3)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("mandatory")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 3, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mvrVlanID"),
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
          ("source_port", 2),
          ("receiver_port", 3))
    )


_MvrPortRole_Type.__name__ = "Integer32"
_MvrPortRole_Object = MibTableColumn
mvrPortRole = _MvrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 3, 1, 1),
    _MvrPortRole_Type()
)
mvrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortRole.setStatus("mandatory")
_MvrPortTagging_Type = EnabledStatus
_MvrPortTagging_Object = MibTableColumn
mvrPortTagging = _MvrPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 3, 1, 2),
    _MvrPortTagging_Type()
)
mvrPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortTagging.setStatus("mandatory")
_MaxNumberOfMvrGroup_Type = Integer32
_MaxNumberOfMvrGroup_Object = MibScalar
maxNumberOfMvrGroup = _MaxNumberOfMvrGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 4),
    _MaxNumberOfMvrGroup_Type()
)
maxNumberOfMvrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfMvrGroup.setStatus("mandatory")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 5)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("mandatory")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 5, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mvrVlanID"),
    (0, "ZYXEL-ES2108G-MIB", "mvrGroupName"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("mandatory")
_MvrGroupName_Type = DisplayString
_MvrGroupName_Object = MibTableColumn
mvrGroupName = _MvrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 5, 1, 1),
    _MvrGroupName_Type()
)
mvrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupName.setStatus("mandatory")
_MvrGroupStartAddress_Type = IpAddress
_MvrGroupStartAddress_Object = MibTableColumn
mvrGroupStartAddress = _MvrGroupStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 5, 1, 2),
    _MvrGroupStartAddress_Type()
)
mvrGroupStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStartAddress.setStatus("mandatory")
_MvrGroupEndAddress_Type = IpAddress
_MvrGroupEndAddress_Object = MibTableColumn
mvrGroupEndAddress = _MvrGroupEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 5, 1, 3),
    _MvrGroupEndAddress_Type()
)
mvrGroupEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupEndAddress.setStatus("mandatory")
_MvrGroupRowStatus_Type = RowStatus
_MvrGroupRowStatus_Object = MibTableColumn
mvrGroupRowStatus = _MvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 31, 5, 1, 4),
    _MvrGroupRowStatus_Type()
)
mvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupRowStatus.setStatus("mandatory")
_SysLogSetup_ObjectIdentity = ObjectIdentity
sysLogSetup = _SysLogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32)
)
_SysLogState_Type = EnabledStatus
_SysLogState_Object = MibScalar
sysLogState = _SysLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 1),
    _SysLogState_Type()
)
sysLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogState.setStatus("mandatory")
_SysLogTypeTable_Object = MibTable
sysLogTypeTable = _SysLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 2)
)
if mibBuilder.loadTexts:
    sysLogTypeTable.setStatus("mandatory")
_SysLogTypeEntry_Object = MibTableRow
sysLogTypeEntry = _SysLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 2, 1)
)
sysLogTypeEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "sysLogTypeIndex"),
)
if mibBuilder.loadTexts:
    sysLogTypeEntry.setStatus("mandatory")
_SysLogTypeIndex_Type = Integer32
_SysLogTypeIndex_Object = MibTableColumn
sysLogTypeIndex = _SysLogTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 2, 1, 1),
    _SysLogTypeIndex_Type()
)
sysLogTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysLogTypeIndex.setStatus("mandatory")
_SysLogTypeName_Type = DisplayString
_SysLogTypeName_Object = MibTableColumn
sysLogTypeName = _SysLogTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 2, 1, 2),
    _SysLogTypeName_Type()
)
sysLogTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogTypeName.setStatus("mandatory")
_SysLogTypeState_Type = EnabledStatus
_SysLogTypeState_Object = MibTableColumn
sysLogTypeState = _SysLogTypeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 2, 1, 3),
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
        *(("local_user0", 0),
          ("local_user1", 1),
          ("local_user2", 2),
          ("local_user3", 3),
          ("local_user4", 4),
          ("local_user5", 5),
          ("local_user6", 6),
          ("local_user7", 7))
    )


_SysLogTypeFacility_Type.__name__ = "Integer32"
_SysLogTypeFacility_Object = MibTableColumn
sysLogTypeFacility = _SysLogTypeFacility_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 2, 1, 4),
    _SysLogTypeFacility_Type()
)
sysLogTypeFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogTypeFacility.setStatus("mandatory")
_SysLogServerTable_Object = MibTable
sysLogServerTable = _SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 3)
)
if mibBuilder.loadTexts:
    sysLogServerTable.setStatus("mandatory")
_SysLogServerEntry_Object = MibTableRow
sysLogServerEntry = _SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 3, 1)
)
sysLogServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "sysLogServerAddress"),
)
if mibBuilder.loadTexts:
    sysLogServerEntry.setStatus("mandatory")
_SysLogServerAddress_Type = IpAddress
_SysLogServerAddress_Object = MibTableColumn
sysLogServerAddress = _SysLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 3, 1, 2),
    _SysLogServerLogLevel_Type()
)
sysLogServerLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerLogLevel.setStatus("mandatory")
_SysLogServerRowStatus_Type = RowStatus
_SysLogServerRowStatus_Object = MibTableColumn
sysLogServerRowStatus = _SysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 32, 3, 1, 3),
    _SysLogServerRowStatus_Type()
)
sysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysLogServerRowStatus.setStatus("mandatory")
_DhcpSetup_ObjectIdentity = ObjectIdentity
dhcpSetup = _DhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33)
)
_GlobalDhcpRelay_ObjectIdentity = ObjectIdentity
globalDhcpRelay = _GlobalDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1)
)
_GlobalDhcpRelayEnable_Type = EnabledStatus
_GlobalDhcpRelayEnable_Object = MibScalar
globalDhcpRelayEnable = _GlobalDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 1),
    _GlobalDhcpRelayEnable_Type()
)
globalDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayEnable.setStatus("mandatory")
_GlobalDhcpRelayOption82Enable_Type = EnabledStatus
_GlobalDhcpRelayOption82Enable_Object = MibScalar
globalDhcpRelayOption82Enable = _GlobalDhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 2),
    _GlobalDhcpRelayOption82Enable_Type()
)
globalDhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayOption82Enable.setStatus("mandatory")
_GlobalDhcpRelayInfoEnable_Type = EnabledStatus
_GlobalDhcpRelayInfoEnable_Object = MibScalar
globalDhcpRelayInfoEnable = _GlobalDhcpRelayInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 3),
    _GlobalDhcpRelayInfoEnable_Type()
)
globalDhcpRelayInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDhcpRelayInfoEnable.setStatus("mandatory")
_GlobalDhcpRelayInfoData_Type = DisplayString
_GlobalDhcpRelayInfoData_Object = MibScalar
globalDhcpRelayInfoData = _GlobalDhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 4),
    _GlobalDhcpRelayInfoData_Type()
)
globalDhcpRelayInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDhcpRelayInfoData.setStatus("mandatory")
_MaxNumberOfGlobalDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfGlobalDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfGlobalDhcpRelayRemoteServer = _MaxNumberOfGlobalDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 5),
    _MaxNumberOfGlobalDhcpRelayRemoteServer_Type()
)
maxNumberOfGlobalDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfGlobalDhcpRelayRemoteServer.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerTable_Object = MibTable
globalDhcpRelayRemoteServerTable = _GlobalDhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 6)
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerTable.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerEntry_Object = MibTableRow
globalDhcpRelayRemoteServerEntry = _GlobalDhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 6, 1)
)
globalDhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "globalDhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerEntry.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerIp_Type = IpAddress
_GlobalDhcpRelayRemoteServerIp_Object = MibTableColumn
globalDhcpRelayRemoteServerIp = _GlobalDhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 6, 1, 1),
    _GlobalDhcpRelayRemoteServerIp_Type()
)
globalDhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerIp.setStatus("mandatory")
_GlobalDhcpRelayRemoteServerRowStatus_Type = RowStatus
_GlobalDhcpRelayRemoteServerRowStatus_Object = MibTableColumn
globalDhcpRelayRemoteServerRowStatus = _GlobalDhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 1, 6, 1, 2),
    _GlobalDhcpRelayRemoteServerRowStatus_Type()
)
globalDhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    globalDhcpRelayRemoteServerRowStatus.setStatus("mandatory")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3)
)
_DhcpRelayInfoData_Type = DisplayString
_DhcpRelayInfoData_Object = MibScalar
dhcpRelayInfoData = _DhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 1),
    _DhcpRelayInfoData_Type()
)
dhcpRelayInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayInfoData.setStatus("mandatory")
_MaxNumberOfDhcpRelay_Type = Integer32
_MaxNumberOfDhcpRelay_Object = MibScalar
maxNumberOfDhcpRelay = _MaxNumberOfDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 2),
    _MaxNumberOfDhcpRelay_Type()
)
maxNumberOfDhcpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelay.setStatus("mandatory")
_MaxNumberOfDhcpRelayRemoteServer_Type = Integer32
_MaxNumberOfDhcpRelayRemoteServer_Object = MibScalar
maxNumberOfDhcpRelayRemoteServer = _MaxNumberOfDhcpRelayRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 3),
    _MaxNumberOfDhcpRelayRemoteServer_Type()
)
maxNumberOfDhcpRelayRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRelayRemoteServer.setStatus("mandatory")
_DhcpRelayRemoteServerTable_Object = MibTable
dhcpRelayRemoteServerTable = _DhcpRelayRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerTable.setStatus("mandatory")
_DhcpRelayRemoteServerEntry_Object = MibTableRow
dhcpRelayRemoteServerEntry = _DhcpRelayRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 4, 1)
)
dhcpRelayRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "dhcpRelayVid"),
    (0, "ZYXEL-ES2108G-MIB", "dhcpRelayRemoteServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerEntry.setStatus("mandatory")
_DhcpRelayVid_Type = Integer32
_DhcpRelayVid_Object = MibTableColumn
dhcpRelayVid = _DhcpRelayVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 4, 1, 1),
    _DhcpRelayVid_Type()
)
dhcpRelayVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVid.setStatus("mandatory")
_DhcpRelayRemoteServerIp_Type = IpAddress
_DhcpRelayRemoteServerIp_Object = MibTableColumn
dhcpRelayRemoteServerIp = _DhcpRelayRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 4, 1, 2),
    _DhcpRelayRemoteServerIp_Type()
)
dhcpRelayRemoteServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerIp.setStatus("mandatory")
_DhcpRelayRemoteServerRowStatus_Type = RowStatus
_DhcpRelayRemoteServerRowStatus_Object = MibTableColumn
dhcpRelayRemoteServerRowStatus = _DhcpRelayRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 4, 1, 3),
    _DhcpRelayRemoteServerRowStatus_Type()
)
dhcpRelayRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayRemoteServerRowStatus.setStatus("mandatory")
_DhcpRelayTable_Object = MibTable
dhcpRelayTable = _DhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 5)
)
if mibBuilder.loadTexts:
    dhcpRelayTable.setStatus("mandatory")
_DhcpRelayEntry_Object = MibTableRow
dhcpRelayEntry = _DhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 5, 1)
)
dhcpRelayEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "dhcpRelayVid"),
)
if mibBuilder.loadTexts:
    dhcpRelayEntry.setStatus("mandatory")
_DhcpRelayOption82Enable_Type = EnabledStatus
_DhcpRelayOption82Enable_Object = MibTableColumn
dhcpRelayOption82Enable = _DhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 5, 1, 1),
    _DhcpRelayOption82Enable_Type()
)
dhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Enable.setStatus("mandatory")
_DhcpRelayInfoEnable_Type = EnabledStatus
_DhcpRelayInfoEnable_Object = MibTableColumn
dhcpRelayInfoEnable = _DhcpRelayInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 33, 3, 5, 1, 2),
    _DhcpRelayInfoEnable_Type()
)
dhcpRelayInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoEnable.setStatus("mandatory")
_RadiusServerSetup_ObjectIdentity = ObjectIdentity
radiusServerSetup = _RadiusServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34)
)
_RadiusAuthServerSetup_ObjectIdentity = ObjectIdentity
radiusAuthServerSetup = _RadiusAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 1),
    _RadiusAuthServerMode_Type()
)
radiusAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerMode.setStatus("mandatory")
_RadiusAuthServerTimeout_Type = Integer32
_RadiusAuthServerTimeout_Object = MibScalar
radiusAuthServerTimeout = _RadiusAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 2),
    _RadiusAuthServerTimeout_Type()
)
radiusAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerTimeout.setStatus("mandatory")
_RadiusAuthServerTable_Object = MibTable
radiusAuthServerTable = _RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 3)
)
if mibBuilder.loadTexts:
    radiusAuthServerTable.setStatus("mandatory")
_RadiusAuthServerEntry_Object = MibTableRow
radiusAuthServerEntry = _RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 3, 1)
)
radiusAuthServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "radiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAuthServerEntry.setStatus("mandatory")
_RadiusAuthServerIndex_Type = Integer32
_RadiusAuthServerIndex_Object = MibTableColumn
radiusAuthServerIndex = _RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 3, 1, 1),
    _RadiusAuthServerIndex_Type()
)
radiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAuthServerIndex.setStatus("mandatory")
_RadiusAuthServerIpAddr_Type = IpAddress
_RadiusAuthServerIpAddr_Object = MibTableColumn
radiusAuthServerIpAddr = _RadiusAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 3, 1, 2),
    _RadiusAuthServerIpAddr_Type()
)
radiusAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerIpAddr.setStatus("mandatory")
_RadiusAuthServerUdpPort_Type = Integer32
_RadiusAuthServerUdpPort_Object = MibTableColumn
radiusAuthServerUdpPort = _RadiusAuthServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 3, 1, 3),
    _RadiusAuthServerUdpPort_Type()
)
radiusAuthServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerUdpPort.setStatus("mandatory")
_RadiusAuthServerSharedSecret_Type = DisplayString
_RadiusAuthServerSharedSecret_Object = MibTableColumn
radiusAuthServerSharedSecret = _RadiusAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 1, 3, 1, 4),
    _RadiusAuthServerSharedSecret_Type()
)
radiusAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthServerSharedSecret.setStatus("mandatory")
_RadiusAcctServerSetup_ObjectIdentity = ObjectIdentity
radiusAcctServerSetup = _RadiusAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2)
)
_RadiusAcctServerTimeout_Type = Integer32
_RadiusAcctServerTimeout_Object = MibScalar
radiusAcctServerTimeout = _RadiusAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 1),
    _RadiusAcctServerTimeout_Type()
)
radiusAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerTimeout.setStatus("mandatory")
_RadiusAcctServerTable_Object = MibTable
radiusAcctServerTable = _RadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 2)
)
if mibBuilder.loadTexts:
    radiusAcctServerTable.setStatus("mandatory")
_RadiusAcctServerEntry_Object = MibTableRow
radiusAcctServerEntry = _RadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 2, 1)
)
radiusAcctServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "radiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    radiusAcctServerEntry.setStatus("mandatory")
_RadiusAcctServerIndex_Type = Integer32
_RadiusAcctServerIndex_Object = MibTableColumn
radiusAcctServerIndex = _RadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 2, 1, 1),
    _RadiusAcctServerIndex_Type()
)
radiusAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusAcctServerIndex.setStatus("mandatory")
_RadiusAcctServerIpAddr_Type = IpAddress
_RadiusAcctServerIpAddr_Object = MibTableColumn
radiusAcctServerIpAddr = _RadiusAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 2, 1, 2),
    _RadiusAcctServerIpAddr_Type()
)
radiusAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerIpAddr.setStatus("mandatory")
_RadiusAcctServerUdpPort_Type = Integer32
_RadiusAcctServerUdpPort_Object = MibTableColumn
radiusAcctServerUdpPort = _RadiusAcctServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 2, 1, 3),
    _RadiusAcctServerUdpPort_Type()
)
radiusAcctServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerUdpPort.setStatus("mandatory")
_RadiusAcctServerSharedSecret_Type = DisplayString
_RadiusAcctServerSharedSecret_Object = MibTableColumn
radiusAcctServerSharedSecret = _RadiusAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 34, 2, 2, 1, 4),
    _RadiusAcctServerSharedSecret_Type()
)
radiusAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctServerSharedSecret.setStatus("mandatory")
_TacacsServerSetup_ObjectIdentity = ObjectIdentity
tacacsServerSetup = _TacacsServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35)
)
_TacacsAuthServerSetup_ObjectIdentity = ObjectIdentity
tacacsAuthServerSetup = _TacacsAuthServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 1),
    _TacacsAuthServerMode_Type()
)
tacacsAuthServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerMode.setStatus("mandatory")
_TacacsAuthServerTimeout_Type = Integer32
_TacacsAuthServerTimeout_Object = MibScalar
tacacsAuthServerTimeout = _TacacsAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 2),
    _TacacsAuthServerTimeout_Type()
)
tacacsAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTimeout.setStatus("mandatory")
_TacacsAuthServerTable_Object = MibTable
tacacsAuthServerTable = _TacacsAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 3)
)
if mibBuilder.loadTexts:
    tacacsAuthServerTable.setStatus("mandatory")
_TacacsAuthServerEntry_Object = MibTableRow
tacacsAuthServerEntry = _TacacsAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 3, 1)
)
tacacsAuthServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "tacacsAuthServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAuthServerEntry.setStatus("mandatory")
_TacacsAuthServerIndex_Type = Integer32
_TacacsAuthServerIndex_Object = MibTableColumn
tacacsAuthServerIndex = _TacacsAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 3, 1, 1),
    _TacacsAuthServerIndex_Type()
)
tacacsAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAuthServerIndex.setStatus("mandatory")
_TacacsAuthServerIpAddr_Type = IpAddress
_TacacsAuthServerIpAddr_Object = MibTableColumn
tacacsAuthServerIpAddr = _TacacsAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 3, 1, 2),
    _TacacsAuthServerIpAddr_Type()
)
tacacsAuthServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerIpAddr.setStatus("mandatory")
_TacacsAuthServerTcpPort_Type = Integer32
_TacacsAuthServerTcpPort_Object = MibTableColumn
tacacsAuthServerTcpPort = _TacacsAuthServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 3, 1, 3),
    _TacacsAuthServerTcpPort_Type()
)
tacacsAuthServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerTcpPort.setStatus("mandatory")
_TacacsAuthServerSharedSecret_Type = DisplayString
_TacacsAuthServerSharedSecret_Object = MibTableColumn
tacacsAuthServerSharedSecret = _TacacsAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 1, 3, 1, 4),
    _TacacsAuthServerSharedSecret_Type()
)
tacacsAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthServerSharedSecret.setStatus("mandatory")
_TacacsAcctServerSetup_ObjectIdentity = ObjectIdentity
tacacsAcctServerSetup = _TacacsAcctServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2)
)
_TacacsAcctServerTimeout_Type = Integer32
_TacacsAcctServerTimeout_Object = MibScalar
tacacsAcctServerTimeout = _TacacsAcctServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 1),
    _TacacsAcctServerTimeout_Type()
)
tacacsAcctServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTimeout.setStatus("mandatory")
_TacacsAcctServerTable_Object = MibTable
tacacsAcctServerTable = _TacacsAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 2)
)
if mibBuilder.loadTexts:
    tacacsAcctServerTable.setStatus("mandatory")
_TacacsAcctServerEntry_Object = MibTableRow
tacacsAcctServerEntry = _TacacsAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 2, 1)
)
tacacsAcctServerEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "tacacsAcctServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsAcctServerEntry.setStatus("mandatory")
_TacacsAcctServerIndex_Type = Integer32
_TacacsAcctServerIndex_Object = MibTableColumn
tacacsAcctServerIndex = _TacacsAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 2, 1, 1),
    _TacacsAcctServerIndex_Type()
)
tacacsAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsAcctServerIndex.setStatus("mandatory")
_TacacsAcctServerIpAddr_Type = IpAddress
_TacacsAcctServerIpAddr_Object = MibTableColumn
tacacsAcctServerIpAddr = _TacacsAcctServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 2, 1, 2),
    _TacacsAcctServerIpAddr_Type()
)
tacacsAcctServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerIpAddr.setStatus("mandatory")
_TacacsAcctServerTcpPort_Type = Integer32
_TacacsAcctServerTcpPort_Object = MibTableColumn
tacacsAcctServerTcpPort = _TacacsAcctServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 2, 1, 3),
    _TacacsAcctServerTcpPort_Type()
)
tacacsAcctServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerTcpPort.setStatus("mandatory")
_TacacsAcctServerSharedSecret_Type = DisplayString
_TacacsAcctServerSharedSecret_Object = MibTableColumn
tacacsAcctServerSharedSecret = _TacacsAcctServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 35, 2, 2, 1, 4),
    _TacacsAcctServerSharedSecret_Type()
)
tacacsAcctServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAcctServerSharedSecret.setStatus("mandatory")
_AaaSetup_ObjectIdentity = ObjectIdentity
aaaSetup = _AaaSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36)
)
_AuthenticationSetup_ObjectIdentity = ObjectIdentity
authenticationSetup = _AuthenticationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 1)
)
_AuthenticationTypeTable_Object = MibTable
authenticationTypeTable = _AuthenticationTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 1, 1)
)
if mibBuilder.loadTexts:
    authenticationTypeTable.setStatus("mandatory")
_AuthenticationTypeEntry_Object = MibTableRow
authenticationTypeEntry = _AuthenticationTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 1, 1, 1)
)
authenticationTypeEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "authenticationTypeName"),
)
if mibBuilder.loadTexts:
    authenticationTypeEntry.setStatus("mandatory")
_AuthenticationTypeName_Type = DisplayString
_AuthenticationTypeName_Object = MibTableColumn
authenticationTypeName = _AuthenticationTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 1, 1, 1, 1),
    _AuthenticationTypeName_Type()
)
authenticationTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationTypeName.setStatus("mandatory")
_AuthenticationTypeMethodList_Type = OctetString
_AuthenticationTypeMethodList_Object = MibTableColumn
authenticationTypeMethodList = _AuthenticationTypeMethodList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 1, 1, 1, 2),
    _AuthenticationTypeMethodList_Type()
)
authenticationTypeMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationTypeMethodList.setStatus("mandatory")
_AccountingSetup_ObjectIdentity = ObjectIdentity
accountingSetup = _AccountingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2)
)
_AccountingUpdatePeriod_Type = Integer32
_AccountingUpdatePeriod_Object = MibScalar
accountingUpdatePeriod = _AccountingUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 1),
    _AccountingUpdatePeriod_Type()
)
accountingUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingUpdatePeriod.setStatus("mandatory")
_AccountingTypeTable_Object = MibTable
accountingTypeTable = _AccountingTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2)
)
if mibBuilder.loadTexts:
    accountingTypeTable.setStatus("mandatory")
_AccountingTypeEntry_Object = MibTableRow
accountingTypeEntry = _AccountingTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1)
)
accountingTypeEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "accountingTypeName"),
)
if mibBuilder.loadTexts:
    accountingTypeEntry.setStatus("mandatory")
_AccountingTypeName_Type = DisplayString
_AccountingTypeName_Object = MibTableColumn
accountingTypeName = _AccountingTypeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1, 1),
    _AccountingTypeName_Type()
)
accountingTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountingTypeName.setStatus("mandatory")
_AccountingTypeActive_Type = EnabledStatus
_AccountingTypeActive_Object = MibTableColumn
accountingTypeActive = _AccountingTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1, 2),
    _AccountingTypeActive_Type()
)
accountingTypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypeActive.setStatus("mandatory")
_AccountingTypeBroadcast_Type = EnabledStatus
_AccountingTypeBroadcast_Object = MibTableColumn
accountingTypeBroadcast = _AccountingTypeBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 36, 2, 2, 1, 6),
    _AccountingTypePrivilege_Type()
)
accountingTypePrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingTypePrivilege.setStatus("mandatory")
_Ipsg_ObjectIdentity = ObjectIdentity
ipsg = _Ipsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101)
)
_IpsgTable_Object = MibTable
ipsgTable = _IpsgTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1)
)
if mibBuilder.loadTexts:
    ipsgTable.setStatus("mandatory")
_IpsgEntry_Object = MibTableRow
ipsgEntry = _IpsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1)
)
ipsgEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "ipsgEntryMac"),
    (0, "ZYXEL-ES2108G-MIB", "ipsgEntryVid"),
)
if mibBuilder.loadTexts:
    ipsgEntry.setStatus("mandatory")
_IpsgEntryMac_Type = MacAddress
_IpsgEntryMac_Object = MibTableColumn
ipsgEntryMac = _IpsgEntryMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 2),
    _IpsgEntryVid_Type()
)
ipsgEntryVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryVid.setStatus("mandatory")
_IpsgEntryIp_Type = IpAddress
_IpsgEntryIp_Object = MibTableColumn
ipsgEntryIp = _IpsgEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 3),
    _IpsgEntryIp_Type()
)
ipsgEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryIp.setStatus("mandatory")
_IpsgEntryLease_Type = Integer32
_IpsgEntryLease_Object = MibTableColumn
ipsgEntryLease = _IpsgEntryLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 5),
    _IpsgEntryType_Type()
)
ipsgEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsgEntryType.setStatus("mandatory")
_IpsgEntryPort_Type = Integer32
_IpsgEntryPort_Object = MibTableColumn
ipsgEntryPort = _IpsgEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 6),
    _IpsgEntryPort_Type()
)
ipsgEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsgEntryPort.setStatus("mandatory")
_IpsgEntryState_Type = RowStatus
_IpsgEntryState_Object = MibTableColumn
ipsgEntryState = _IpsgEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 101, 1, 1, 7),
    _IpsgEntryState_Type()
)
ipsgEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsgEntryState.setStatus("mandatory")
_ArpInspect_ObjectIdentity = ObjectIdentity
arpInspect = _ArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102)
)
_ArpInspectSetup_ObjectIdentity = ObjectIdentity
arpInspectSetup = _ArpInspectSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1)
)
_ArpInspectState_Type = EnabledStatus
_ArpInspectState_Object = MibScalar
arpInspectState = _ArpInspectState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 2),
    _ArpInspectFilterAgingTime_Type()
)
arpInspectFilterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterAgingTime.setStatus("mandatory")
_ArpInspectLog_ObjectIdentity = ObjectIdentity
arpInspectLog = _ArpInspectLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 3, 3),
    _ArpInspectLogInterval_Type()
)
arpInspectLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogInterval.setStatus("mandatory")
_ArpInspectVlanTable_Object = MibTable
arpInspectVlanTable = _ArpInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 4)
)
if mibBuilder.loadTexts:
    arpInspectVlanTable.setStatus("mandatory")
_ArpInspectVlanEntry_Object = MibTableRow
arpInspectVlanEntry = _ArpInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 4, 1)
)
arpInspectVlanEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "arpInspectVlanVid"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 4, 1, 3),
    _ArpInspectVlanStatus_Type()
)
arpInspectVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectVlanStatus.setStatus("mandatory")
_ArpInspectPortTable_Object = MibTable
arpInspectPortTable = _ArpInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 5)
)
if mibBuilder.loadTexts:
    arpInspectPortTable.setStatus("mandatory")
_ArpInspectPortEntry_Object = MibTableRow
arpInspectPortEntry = _ArpInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 5, 1)
)
arpInspectPortEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "arpInspectPortIndex"),
)
if mibBuilder.loadTexts:
    arpInspectPortEntry.setStatus("mandatory")
_ArpInspectPortIndex_Type = Integer32
_ArpInspectPortIndex_Object = MibTableColumn
arpInspectPortIndex = _ArpInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 1, 5, 1, 2),
    _ArpInspectPortTrust_Type()
)
arpInspectPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectPortTrust.setStatus("mandatory")
_ArpInspectStatus_ObjectIdentity = ObjectIdentity
arpInspectStatus = _ArpInspectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2)
)
_ArpInspectFilterClear_Type = EnabledStatus
_ArpInspectFilterClear_Object = MibScalar
arpInspectFilterClear = _ArpInspectFilterClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 1),
    _ArpInspectFilterClear_Type()
)
arpInspectFilterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectFilterClear.setStatus("mandatory")
_ArpInspectLogClear_Type = EnabledStatus
_ArpInspectLogClear_Object = MibScalar
arpInspectLogClear = _ArpInspectLogClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 2),
    _ArpInspectLogClear_Type()
)
arpInspectLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectLogClear.setStatus("mandatory")
_ArpInspectFilterTable_Object = MibTable
arpInspectFilterTable = _ArpInspectFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3)
)
if mibBuilder.loadTexts:
    arpInspectFilterTable.setStatus("mandatory")
_ArpInspectFilterEntry_Object = MibTableRow
arpInspectFilterEntry = _ArpInspectFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1)
)
arpInspectFilterEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "arpInspectFilterMac"),
    (0, "ZYXEL-ES2108G-MIB", "arpInspectFilterVid"),
)
if mibBuilder.loadTexts:
    arpInspectFilterEntry.setStatus("mandatory")
_ArpInspectFilterMac_Type = MacAddress
_ArpInspectFilterMac_Object = MibTableColumn
arpInspectFilterMac = _ArpInspectFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1, 2),
    _ArpInspectFilterVid_Type()
)
arpInspectFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterVid.setStatus("mandatory")
_ArpInspectFilterPort_Type = Integer32
_ArpInspectFilterPort_Object = MibTableColumn
arpInspectFilterPort = _ArpInspectFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1, 3),
    _ArpInspectFilterPort_Type()
)
arpInspectFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterPort.setStatus("mandatory")
_ArpInspectFilterExpiry_Type = Integer32
_ArpInspectFilterExpiry_Object = MibTableColumn
arpInspectFilterExpiry = _ArpInspectFilterExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1, 5),
    _ArpInspectFilterReason_Type()
)
arpInspectFilterReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectFilterReason.setStatus("mandatory")
_ArpInspectFilterRowStatus_Type = RowStatus
_ArpInspectFilterRowStatus_Object = MibTableColumn
arpInspectFilterRowStatus = _ArpInspectFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 3, 1, 6),
    _ArpInspectFilterRowStatus_Type()
)
arpInspectFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arpInspectFilterRowStatus.setStatus("mandatory")
_ArpInspectLogTable_Object = MibTable
arpInspectLogTable = _ArpInspectLogTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4)
)
if mibBuilder.loadTexts:
    arpInspectLogTable.setStatus("mandatory")
_ArpInspectLogEntry_Object = MibTableRow
arpInspectLogEntry = _ArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1)
)
arpInspectLogEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "arpInspectLogMac"),
    (0, "ZYXEL-ES2108G-MIB", "arpInspectLogVid"),
    (0, "ZYXEL-ES2108G-MIB", "arpInspectLogPort"),
    (0, "ZYXEL-ES2108G-MIB", "arpInspectLogIp"),
)
if mibBuilder.loadTexts:
    arpInspectLogEntry.setStatus("mandatory")
_ArpInspectLogMac_Type = MacAddress
_ArpInspectLogMac_Object = MibTableColumn
arpInspectLogMac = _ArpInspectLogMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 2),
    _ArpInspectLogVid_Type()
)
arpInspectLogVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogVid.setStatus("mandatory")
_ArpInspectLogPort_Type = Integer32
_ArpInspectLogPort_Object = MibTableColumn
arpInspectLogPort = _ArpInspectLogPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 3),
    _ArpInspectLogPort_Type()
)
arpInspectLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogPort.setStatus("mandatory")
_ArpInspectLogIp_Type = IpAddress
_ArpInspectLogIp_Object = MibTableColumn
arpInspectLogIp = _ArpInspectLogIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 4),
    _ArpInspectLogIp_Type()
)
arpInspectLogIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogIp.setStatus("mandatory")
_ArpInspectLogNumPkt_Type = Integer32
_ArpInspectLogNumPkt_Object = MibTableColumn
arpInspectLogNumPkt = _ArpInspectLogNumPkt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 6),
    _ArpInspectLogReason_Type()
)
arpInspectLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogReason.setStatus("mandatory")
_ArpInspectLogTime_Type = DateAndTime
_ArpInspectLogTime_Object = MibTableColumn
arpInspectLogTime = _ArpInspectLogTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 102, 2, 4, 1, 7),
    _ArpInspectLogTime_Type()
)
arpInspectLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInspectLogTime.setStatus("mandatory")
_LoopGuardSetup_ObjectIdentity = ObjectIdentity
loopGuardSetup = _LoopGuardSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 104)
)
_LoopGuardState_Type = EnabledStatus
_LoopGuardState_Object = MibScalar
loopGuardState = _LoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 104, 1),
    _LoopGuardState_Type()
)
loopGuardState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardState.setStatus("mandatory")
_LoopGuardPortTable_Object = MibTable
loopGuardPortTable = _LoopGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 104, 2)
)
if mibBuilder.loadTexts:
    loopGuardPortTable.setStatus("mandatory")
_LoopGuardPortEntry_Object = MibTableRow
loopGuardPortEntry = _LoopGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 104, 2, 1)
)
loopGuardPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    loopGuardPortEntry.setStatus("mandatory")
_LoopGuardPortState_Type = EnabledStatus
_LoopGuardPortState_Object = MibTableColumn
loopGuardPortState = _LoopGuardPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 104, 2, 1, 1),
    _LoopGuardPortState_Type()
)
loopGuardPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopGuardPortState.setStatus("mandatory")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107)
)
_MstpGen_ObjectIdentity = ObjectIdentity
mstpGen = _MstpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1)
)
_MstpGenState_Type = EnabledStatus
_MstpGenState_Object = MibScalar
mstpGenState = _MstpGenState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 1),
    _MstpGenState_Type()
)
mstpGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenState.setStatus("mandatory")
_MstpGenCfgIdName_Type = DisplayString
_MstpGenCfgIdName_Object = MibScalar
mstpGenCfgIdName = _MstpGenCfgIdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 2),
    _MstpGenCfgIdName_Type()
)
mstpGenCfgIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdName.setStatus("mandatory")
_MstpGenCfgIdRevLevel_Type = Integer32
_MstpGenCfgIdRevLevel_Object = MibScalar
mstpGenCfgIdRevLevel = _MstpGenCfgIdRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 4),
    _MstpGenCfgIdCfgDigest_Type()
)
mstpGenCfgIdCfgDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCfgIdCfgDigest.setStatus("mandatory")


class _MstpGenHelloTime_Type(Timeout):
    """Custom type mstpGenHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MstpGenHelloTime_Type.__name__ = "Timeout"
_MstpGenHelloTime_Object = MibScalar
mstpGenHelloTime = _MstpGenHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 5),
    _MstpGenHelloTime_Type()
)
mstpGenHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenHelloTime.setStatus("mandatory")


class _MstpGenMaxAge_Type(Timeout):
    """Custom type mstpGenMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MstpGenMaxAge_Type.__name__ = "Timeout"
_MstpGenMaxAge_Object = MibScalar
mstpGenMaxAge = _MstpGenMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 6),
    _MstpGenMaxAge_Type()
)
mstpGenMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxAge.setStatus("mandatory")


class _MstpGenForwardDelay_Type(Timeout):
    """Custom type mstpGenForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MstpGenForwardDelay_Type.__name__ = "Timeout"
_MstpGenForwardDelay_Object = MibScalar
mstpGenForwardDelay = _MstpGenForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 7),
    _MstpGenForwardDelay_Type()
)
mstpGenForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenForwardDelay.setStatus("mandatory")


class _MstpGenMaxHops_Type(Integer32):
    """Custom type mstpGenMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstpGenMaxHops_Type.__name__ = "Integer32"
_MstpGenMaxHops_Object = MibScalar
mstpGenMaxHops = _MstpGenMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 8),
    _MstpGenMaxHops_Type()
)
mstpGenMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxHops.setStatus("mandatory")
_MstpGenCistRootPathCost_Type = Integer32
_MstpGenCistRootPathCost_Object = MibScalar
mstpGenCistRootPathCost = _MstpGenCistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 9),
    _MstpGenCistRootPathCost_Type()
)
mstpGenCistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootPathCost.setStatus("mandatory")


class _MstpGenCistRootBrid_Type(OctetString):
    """Custom type mstpGenCistRootBrid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_MstpGenCistRootBrid_Type.__name__ = "OctetString"
_MstpGenCistRootBrid_Object = MibScalar
mstpGenCistRootBrid = _MstpGenCistRootBrid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 1, 10),
    _MstpGenCistRootBrid_Type()
)
mstpGenCistRootBrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCistRootBrid.setStatus("mandatory")
_MstMapTable_Object = MibTable
mstMapTable = _MstMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20)
)
if mibBuilder.loadTexts:
    mstMapTable.setStatus("mandatory")
_MstMapEntry_Object = MibTableRow
mstMapEntry = _MstMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1)
)
mstMapEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mstMapIndex"),
)
if mibBuilder.loadTexts:
    mstMapEntry.setStatus("mandatory")
_MstMapIndex_Type = MstiOrCistInstanceIndex
_MstMapIndex_Object = MibTableColumn
mstMapIndex = _MstMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1, 5),
    _MstMapVlans4k_Type()
)
mstMapVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMapVlans4k.setStatus("current")
_MstMapRowStatus_Type = RowStatus
_MstMapRowStatus_Object = MibTableColumn
mstMapRowStatus = _MstMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 20, 1, 6),
    _MstMapRowStatus_Type()
)
mstMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstMapRowStatus.setStatus("mandatory")
_MstVlanTable_Object = MibTable
mstVlanTable = _MstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 30)
)
if mibBuilder.loadTexts:
    mstVlanTable.setStatus("mandatory")
_MstVlanEntry_Object = MibTableRow
mstVlanEntry = _MstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 30, 1)
)
mstVlanEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mstVlanIndex"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 30, 1, 1),
    _MstVlanIndex_Type()
)
mstVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstVlanIndex.setStatus("mandatory")
_MstVlanMstIndex_Type = MstiOrCistInstanceIndex
_MstVlanMstIndex_Object = MibTableColumn
mstVlanMstIndex = _MstVlanMstIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 30, 1, 2),
    _MstVlanMstIndex_Type()
)
mstVlanMstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstVlanMstIndex.setStatus("mandatory")
_MstpPortTable_Object = MibTable
mstpPortTable = _MstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 40)
)
if mibBuilder.loadTexts:
    mstpPortTable.setStatus("mandatory")
_MstpPortEntry_Object = MibTableRow
mstpPortEntry = _MstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 40, 1)
)
mstpPortEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mstpPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 40, 1, 1),
    _MstpPortIndex_Type()
)
mstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpPortIndex.setStatus("mandatory")
_MstpPortOperEdgePort_Type = TruthValue
_MstpPortOperEdgePort_Object = MibTableColumn
mstpPortOperEdgePort = _MstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 40, 1, 2),
    _MstpPortOperEdgePort_Type()
)
mstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperEdgePort.setStatus("mandatory")
_MstpPortOperPointToPointMAC_Type = TruthValue
_MstpPortOperPointToPointMAC_Object = MibTableColumn
mstpPortOperPointToPointMAC = _MstpPortOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 40, 1, 3),
    _MstpPortOperPointToPointMAC_Type()
)
mstpPortOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperPointToPointMAC.setStatus("mandatory")
_MstpXstTable_Object = MibTable
mstpXstTable = _MstpXstTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50)
)
if mibBuilder.loadTexts:
    mstpXstTable.setStatus("mandatory")
_MstpXstEntry_Object = MibTableRow
mstpXstEntry = _MstpXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1)
)
mstpXstEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mstpXstId"),
)
if mibBuilder.loadTexts:
    mstpXstEntry.setStatus("mandatory")
_MstpXstId_Type = MstiOrCistInstanceIndex
_MstpXstId_Object = MibTableColumn
mstpXstId = _MstpXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 2),
    _MstpXstBridgePriority_Type()
)
mstpXstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstBridgePriority.setStatus("mandatory")
_MstpXstBridgeId_Type = BridgeId
_MstpXstBridgeId_Object = MibTableColumn
mstpXstBridgeId = _MstpXstBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 3),
    _MstpXstBridgeId_Type()
)
mstpXstBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstBridgeId.setStatus("mandatory")
_MstpXstInternalRootCost_Type = Integer32
_MstpXstInternalRootCost_Object = MibTableColumn
mstpXstInternalRootCost = _MstpXstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 4),
    _MstpXstInternalRootCost_Type()
)
mstpXstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstInternalRootCost.setStatus("mandatory")
_MstpXstRootPort_Type = Integer32
_MstpXstRootPort_Object = MibTableColumn
mstpXstRootPort = _MstpXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 5),
    _MstpXstRootPort_Type()
)
mstpXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstRootPort.setStatus("mandatory")
_MstpXstTimeSinceTopologyChange_Type = TimeTicks
_MstpXstTimeSinceTopologyChange_Object = MibTableColumn
mstpXstTimeSinceTopologyChange = _MstpXstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 6),
    _MstpXstTimeSinceTopologyChange_Type()
)
mstpXstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTimeSinceTopologyChange.setStatus("mandatory")
_MstpXstTopologyChangesCount_Type = Counter32
_MstpXstTopologyChangesCount_Object = MibTableColumn
mstpXstTopologyChangesCount = _MstpXstTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 50, 1, 7),
    _MstpXstTopologyChangesCount_Type()
)
mstpXstTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTopologyChangesCount.setStatus("mandatory")
_MstpXstPortTable_Object = MibTable
mstpXstPortTable = _MstpXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60)
)
if mibBuilder.loadTexts:
    mstpXstPortTable.setStatus("mandatory")
_MstpXstPortEntry_Object = MibTableRow
mstpXstPortEntry = _MstpXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1)
)
mstpXstPortEntry.setIndexNames(
    (0, "ZYXEL-ES2108G-MIB", "mstpXstPortXstId"),
    (0, "ZYXEL-ES2108G-MIB", "mstpXstPortIndex"),
)
if mibBuilder.loadTexts:
    mstpXstPortEntry.setStatus("mandatory")
_MstpXstPortXstId_Type = MstiOrCistInstanceIndex
_MstpXstPortXstId_Object = MibTableColumn
mstpXstPortXstId = _MstpXstPortXstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 2),
    _MstpXstPortIndex_Type()
)
mstpXstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortIndex.setStatus("mandatory")
_MstpXstPortEnable_Type = EnabledStatus
_MstpXstPortEnable_Object = MibTableColumn
mstpXstPortEnable = _MstpXstPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 6),
    _MstpXstPortState_Type()
)
mstpXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortState.setStatus("mandatory")
_MstpXstPortDesignatedRoot_Type = BridgeId
_MstpXstPortDesignatedRoot_Object = MibTableColumn
mstpXstPortDesignatedRoot = _MstpXstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 7),
    _MstpXstPortDesignatedRoot_Type()
)
mstpXstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedRoot.setStatus("mandatory")
_MstpXstPortDesignatedCost_Type = Integer32
_MstpXstPortDesignatedCost_Object = MibTableColumn
mstpXstPortDesignatedCost = _MstpXstPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 8),
    _MstpXstPortDesignatedCost_Type()
)
mstpXstPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedCost.setStatus("mandatory")
_MstpXstPortDesignatedBridge_Type = BridgeId
_MstpXstPortDesignatedBridge_Object = MibTableColumn
mstpXstPortDesignatedBridge = _MstpXstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 9),
    _MstpXstPortDesignatedBridge_Type()
)
mstpXstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedBridge.setStatus("mandatory")
_MstpXstPortDesignatedPort_Type = Integer32
_MstpXstPortDesignatedPort_Object = MibTableColumn
mstpXstPortDesignatedPort = _MstpXstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 60, 1, 10),
    _MstpXstPortDesignatedPort_Type()
)
mstpXstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedPort.setStatus("mandatory")
_MstpNotifications_ObjectIdentity = ObjectIdentity
mstpNotifications = _MstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 70)
)

# Managed Objects groups


# Notification objects

eventOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 2, 1)
)
eventOnTrap.setObjects(
      *(("ZYXEL-ES2108G-MIB", "eventSeqNum"),
        ("ZYXEL-ES2108G-MIB", "eventEventId"),
        ("ZYXEL-ES2108G-MIB", "eventName"),
        ("ZYXEL-ES2108G-MIB", "eventSetTime"),
        ("ZYXEL-ES2108G-MIB", "eventSeverity"),
        ("ZYXEL-ES2108G-MIB", "eventInstanceType"),
        ("ZYXEL-ES2108G-MIB", "eventInstanceId"),
        ("ZYXEL-ES2108G-MIB", "eventInstanceName"),
        ("ZYXEL-ES2108G-MIB", "eventServAffective"),
        ("ZYXEL-ES2108G-MIB", "eventDescription"),
        ("ZYXEL-ES2108G-MIB", "trapPersistence"),
        ("ZYXEL-ES2108G-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventOnTrap.setStatus(
        "current"
    )

eventClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 27, 2, 2)
)
eventClearedTrap.setObjects(
      *(("ZYXEL-ES2108G-MIB", "eventSeqNum"),
        ("ZYXEL-ES2108G-MIB", "eventEventId"),
        ("ZYXEL-ES2108G-MIB", "eventSetTime"),
        ("ZYXEL-ES2108G-MIB", "eventInstanceType"),
        ("ZYXEL-ES2108G-MIB", "eventInstanceId"),
        ("ZYXEL-ES2108G-MIB", "trapRefSeqNum"),
        ("ZYXEL-ES2108G-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventClearedTrap.setStatus(
        "current"
    )

mstpNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 70, 1)
)
mstpNewRoot.setObjects(
    ("ZYXEL-ES2108G-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpNewRoot.setStatus(
        "current"
    )

mstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 19, 107, 70, 2)
)
mstpTopologyChange.setObjects(
    ("ZYXEL-ES2108G-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES2108G-MIB",
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
       "es2108g": es2108g,
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
       "rateLimitSetup": rateLimitSetup,
       "rateLimitState": rateLimitState,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rateLimitPortState": rateLimitPortState,
       "rateLimitPortIngRate": rateLimitPortIngRate,
       "rateLimitPortEgrRate": rateLimitPortEgrRate,
       "rateLimitPortStateIngress": rateLimitPortStateIngress,
       "rateLimitPortStateEgress": rateLimitPortStateEgress,
       "brLimitSetup": brLimitSetup,
       "brLimitState": brLimitState,
       "brLimitPortTable": brLimitPortTable,
       "brLimitPortEntry": brLimitPortEntry,
       "brLimitPortState": brLimitPortState,
       "brLimitPortRate": brLimitPortRate,
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
       "dot1xSetup": dot1xSetup,
       "portAuthState": portAuthState,
       "portAuthTable": portAuthTable,
       "portAuthEntry": portAuthEntry,
       "portAuthEntryState": portAuthEntryState,
       "portReAuthEntryState": portReAuthEntryState,
       "portReAuthEntryTimer": portReAuthEntryTimer,
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
       "sysMgmt": sysMgmt,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtBootupConfig": sysMgmtBootupConfig,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtDefaultConfig": sysMgmtDefaultConfig,
       "sysMgmtLastActionStatus": sysMgmtLastActionStatus,
       "layer2Setup": layer2Setup,
       "vlanTypeSetup": vlanTypeSetup,
       "igmpSnoopingStateSetup": igmpSnoopingStateSetup,
       "tagVlanPortIsolationState": tagVlanPortIsolationState,
       "stpState": stpState,
       "tagVlanIngressCheckState": tagVlanIngressCheckState,
       "igmpFilteringStateSetup": igmpFilteringStateSetup,
       "unknownMulticastFrameForwarding": unknownMulticastFrameForwarding,
       "multicastGrpHostTimeOut": multicastGrpHostTimeOut,
       "multicastGrpLeaveTimeOut": multicastGrpLeaveTimeOut,
       "igmpsnp8021pPriority": igmpsnp8021pPriority,
       "igmpsnpVlanMode": igmpsnpVlanMode,
       "stpMode": stpMode,
       "igmpsnpVlanTable": igmpsnpVlanTable,
       "igmpsnpVlanEntry": igmpsnpVlanEntry,
       "igmpsnpVid": igmpsnpVid,
       "igmpsnpVlanName": igmpsnpVlanName,
       "igmpsnpVlanRowStatus": igmpsnpVlanRowStatus,
       "igmpsnpQuerierMode": igmpsnpQuerierMode,
       "ipSetup": ipSetup,
       "dnsIpAddress": dnsIpAddress,
       "defaultMgmtIpSetup": defaultMgmtIpSetup,
       "defaultMgmtIpType": defaultMgmtIpType,
       "defaultMgmtVid": defaultMgmtVid,
       "defaultMgmtStaticIp": defaultMgmtStaticIp,
       "defaultMgmtStaticSubnetMask": defaultMgmtStaticSubnetMask,
       "defaultMgmtStaticGateway": defaultMgmtStaticGateway,
       "maxNumOfMgmtIp": maxNumOfMgmtIp,
       "mgmtIpTable": mgmtIpTable,
       "mgmtIpEntry": mgmtIpEntry,
       "mgmtEntryIp": mgmtEntryIp,
       "mgmtEntrySubnetMask": mgmtEntrySubnetMask,
       "mgmtEntryGateway": mgmtEntryGateway,
       "mgmtEntryVid": mgmtEntryVid,
       "mgmtEntryManageable": mgmtEntryManageable,
       "mgmtEntryRowStatus": mgmtEntryRowStatus,
       "filterSetup": filterSetup,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterName": filterName,
       "filterMacAddr": filterMacAddr,
       "filterVid": filterVid,
       "filterRowStatus": filterRowStatus,
       "mirrorSetup": mirrorSetup,
       "mirrorState": mirrorState,
       "mirrorMonitorPort": mirrorMonitorPort,
       "mirrorIngActionState": mirrorIngActionState,
       "mirrorIngMacAddr": mirrorIngMacAddr,
       "mirrorEgrActionState": mirrorEgrActionState,
       "mirrorEgrMacAddr": mirrorEgrMacAddr,
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
       "queuingMethodType": queuingMethodType,
       "queuingMethodTable": queuingMethodTable,
       "queuingMethodEntry": queuingMethodEntry,
       "queuingMethodQueue": queuingMethodQueue,
       "queuingMethodWeight": queuingMethodWeight,
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
       "portBasedVlanSetup": portBasedVlanSetup,
       "portBasedVlanPortListTable": portBasedVlanPortListTable,
       "portBasedVlanPortListEntry": portBasedVlanPortListEntry,
       "portBasedVlanPortListMembers": portBasedVlanPortListMembers,
       "diffservSetup": diffservSetup,
       "diffservState": diffservState,
       "diffservMapTable": diffservMapTable,
       "diffservMapEntry": diffservMapEntry,
       "diffservMapDscp": diffservMapDscp,
       "diffservMapPriority": diffservMapPriority,
       "diffservPortTable": diffservPortTable,
       "diffservPortEntry": diffservPortEntry,
       "diffservPortState": diffservPortState,
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
       "faultTrapsMIB": faultTrapsMIB,
       "trapInfoObjects": trapInfoObjects,
       "trapRefSeqNum": trapRefSeqNum,
       "trapPersistence": trapPersistence,
       "trapSenderNodeId": trapSenderNodeId,
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
       "multicastStatus": multicastStatus,
       "multicastStatusTable": multicastStatusTable,
       "multicastStatusEntry": multicastStatusEntry,
       "multicastStatusIndex": multicastStatusIndex,
       "multicastStatusVlanID": multicastStatusVlanID,
       "multicastStatusPort": multicastStatusPort,
       "multicastStatusGroup": multicastStatusGroup,
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
       "dhcpSetup": dhcpSetup,
       "globalDhcpRelay": globalDhcpRelay,
       "globalDhcpRelayEnable": globalDhcpRelayEnable,
       "globalDhcpRelayOption82Enable": globalDhcpRelayOption82Enable,
       "globalDhcpRelayInfoEnable": globalDhcpRelayInfoEnable,
       "globalDhcpRelayInfoData": globalDhcpRelayInfoData,
       "maxNumberOfGlobalDhcpRelayRemoteServer": maxNumberOfGlobalDhcpRelayRemoteServer,
       "globalDhcpRelayRemoteServerTable": globalDhcpRelayRemoteServerTable,
       "globalDhcpRelayRemoteServerEntry": globalDhcpRelayRemoteServerEntry,
       "globalDhcpRelayRemoteServerIp": globalDhcpRelayRemoteServerIp,
       "globalDhcpRelayRemoteServerRowStatus": globalDhcpRelayRemoteServerRowStatus,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayInfoData": dhcpRelayInfoData,
       "maxNumberOfDhcpRelay": maxNumberOfDhcpRelay,
       "maxNumberOfDhcpRelayRemoteServer": maxNumberOfDhcpRelayRemoteServer,
       "dhcpRelayRemoteServerTable": dhcpRelayRemoteServerTable,
       "dhcpRelayRemoteServerEntry": dhcpRelayRemoteServerEntry,
       "dhcpRelayVid": dhcpRelayVid,
       "dhcpRelayRemoteServerIp": dhcpRelayRemoteServerIp,
       "dhcpRelayRemoteServerRowStatus": dhcpRelayRemoteServerRowStatus,
       "dhcpRelayTable": dhcpRelayTable,
       "dhcpRelayEntry": dhcpRelayEntry,
       "dhcpRelayOption82Enable": dhcpRelayOption82Enable,
       "dhcpRelayInfoEnable": dhcpRelayInfoEnable,
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
       "loopGuardSetup": loopGuardSetup,
       "loopGuardState": loopGuardState,
       "loopGuardPortTable": loopGuardPortTable,
       "loopGuardPortEntry": loopGuardPortEntry,
       "loopGuardPortState": loopGuardPortState,
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
       "mstpTopologyChange": mstpTopologyChange}
)
