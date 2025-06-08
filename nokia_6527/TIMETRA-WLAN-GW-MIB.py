# SNMP MIB module (TIMETRA-WLAN-GW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-WLAN-GW-MIB.mib
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

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLabel")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxChassisIndexOrZero,
 TmnxSlotNumOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndexOrZero",
    "TmnxSlotNumOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex")

(TIPFilterID,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TIPFilterID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxMobProfKeepAliveInterval,
 TmnxMobProfKeepAliveResponse,
 TmnxMobProfKeepAliveRetryCount,
 TmnxMobProfKeepAliveTimeout,
 TmnxMobProfMsgReTxRetryCount,
 TmnxMobProfMsgReTxTimeout) = mibBuilder.importSymbols(
    "TIMETRA-MOBILE-PROFILE-MIB",
    "TmnxMobProfKeepAliveInterval",
    "TmnxMobProfKeepAliveResponse",
    "TmnxMobProfKeepAliveRetryCount",
    "TmnxMobProfKeepAliveTimeout",
    "TmnxMobProfMsgReTxRetryCount",
    "TmnxMobProfMsgReTxTimeout")

(iesIfIndex,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "iesIfIndex",
    "svcId")

(TmnxMobApn,
 TmnxMobApnDomainName,
 TmnxMobApnOrZero,
 TmnxMobArp,
 TmnxMobArpValue,
 TmnxMobBearerId,
 TmnxMobImsiStr,
 TmnxMobMccOrEmpty,
 TmnxMobMncOrEmpty,
 TmnxMobPathMgmtState,
 TmnxMobProfGbrRate,
 TmnxMobProfIpTtl,
 TmnxMobProfMbrRate,
 TmnxMobQci,
 TmnxMobService) = mibBuilder.importSymbols(
    "TIMETRA-TC-MG-MIB",
    "TmnxMobApn",
    "TmnxMobApnDomainName",
    "TmnxMobApnOrZero",
    "TmnxMobArp",
    "TmnxMobArpValue",
    "TmnxMobBearerId",
    "TmnxMobImsiStr",
    "TmnxMobMccOrEmpty",
    "TmnxMobMncOrEmpty",
    "TmnxMobPathMgmtState",
    "TmnxMobProfGbrRate",
    "TmnxMobProfIpTtl",
    "TmnxMobProfMbrRate",
    "TmnxMobQci",
    "TmnxMobService")

(QTagFullRange,
 QTagFullRangeOrNone,
 SvcISID,
 TAdaptationRule,
 TCIRRate,
 TIpProtocol,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TOperator,
 TPIRRate,
 TPolicyID,
 TPortSchedulerPIR,
 TmnxActionType,
 TmnxAdminState,
 TmnxBsxIsaAaGroupIndexOrZero,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxHttpRedirectUrl,
 TmnxMacSpecification,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrID,
 TmnxVRtrIDOrZero,
 TmnxWlanGwIsaGrpId,
 TmnxWlanGwIsaGrpIdOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "QTagFullRange",
    "QTagFullRangeOrNone",
    "SvcISID",
    "TAdaptationRule",
    "TCIRRate",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TOperator",
    "TPIRRate",
    "TPolicyID",
    "TPortSchedulerPIR",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxBsxIsaAaGroupIndexOrZero",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxHttpRedirectUrl",
    "TmnxMacSpecification",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero",
    "TmnxWlanGwIsaGrpId",
    "TmnxWlanGwIsaGrpIdOrZero")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraWlanGwMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 81)
)
if mibBuilder.loadTexts:
    timetraWlanGwMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-02-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxWlanGwBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )



class TmnxWlanGwIsaIomOperState(TextualConvention, Integer32):
    status = "current"
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
        *(("unavail", 0),
          ("primary", 1),
          ("backup", 2),
          ("busy", 3))
    )



class TmnxWlanGwMgwInterfaceType(TextualConvention, Integer32):
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
        *(("gn", 1),
          ("s2a", 2),
          ("s2b", 3))
    )



class TmnxWlanGwDsmFilterAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )



class TmnxWlanGwDsmFilterActionOrNone(TextualConvention, Integer32):
    status = "current"
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
          ("drop", 1),
          ("forward", 2))
    )



class TmnxWlanGwQoSOperState(TextualConvention, Integer32):
    status = "current"
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
        *(("adminDown", 0),
          ("active", 1),
          ("pending", 2),
          ("problem", 3))
    )



class TmnxWlanGwUeIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxWlanGwChargingCharBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bit0", 0),
          ("bit1", 1),
          ("bit2", 2),
          ("bit3", 3),
          ("bit4", 4),
          ("bit5", 5),
          ("bit6", 6),
          ("bit7", 7),
          ("bit8", 8),
          ("bit9", 9),
          ("bit10", 10),
          ("bit11", 11),
          ("bit12", 12),
          ("bit13", 13),
          ("bit14", 14),
          ("bit15", 15))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxWlanGwConformance_ObjectIdentity = ObjectIdentity
tmnxWlanGwConformance = _TmnxWlanGwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81)
)
_TmnxWlanGwCompliances_ObjectIdentity = ObjectIdentity
tmnxWlanGwCompliances = _TmnxWlanGwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1)
)
_TmnxWlanGwGroups_ObjectIdentity = ObjectIdentity
tmnxWlanGwGroups = _TmnxWlanGwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2)
)
_TmnxWlanGw_ObjectIdentity = ObjectIdentity
tmnxWlanGw = _TmnxWlanGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81)
)
_TmnxWlanGwObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwObjs = _TmnxWlanGwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1)
)
_TmnxWlanGwIsaObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwIsaObjs = _TmnxWlanGwIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1)
)
_TmnxWlanGwGrpTable_Object = MibTable
tmnxWlanGwGrpTable = _TmnxWlanGwGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpTable.setStatus("current")
_TmnxWlanGwGrpEntry_Object = MibTableRow
tmnxWlanGwGrpEntry = _TmnxWlanGwGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1)
)
tmnxWlanGwGrpEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpEntry.setStatus("current")
_TmnxWlanGwGrpId_Type = TmnxWlanGwIsaGrpId
_TmnxWlanGwGrpId_Object = MibTableColumn
tmnxWlanGwGrpId = _TmnxWlanGwGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 1),
    _TmnxWlanGwGrpId_Type()
)
tmnxWlanGwGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpId.setStatus("current")
_TmnxWlanGwGrpRowStatus_Type = RowStatus
_TmnxWlanGwGrpRowStatus_Object = MibTableColumn
tmnxWlanGwGrpRowStatus = _TmnxWlanGwGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 2),
    _TmnxWlanGwGrpRowStatus_Type()
)
tmnxWlanGwGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpRowStatus.setStatus("current")
_TmnxWlanGwGrpLastMgmtChange_Type = TimeStamp
_TmnxWlanGwGrpLastMgmtChange_Object = MibTableColumn
tmnxWlanGwGrpLastMgmtChange = _TmnxWlanGwGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 3),
    _TmnxWlanGwGrpLastMgmtChange_Type()
)
tmnxWlanGwGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpLastMgmtChange.setStatus("current")


class _TmnxWlanGwGrpDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwGrpDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwGrpDescription_Object = MibTableColumn
tmnxWlanGwGrpDescription = _TmnxWlanGwGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 4),
    _TmnxWlanGwGrpDescription_Type()
)
tmnxWlanGwGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpDescription.setStatus("current")


class _TmnxWlanGwGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanGwGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwGrpAdminState_Object = MibTableColumn
tmnxWlanGwGrpAdminState = _TmnxWlanGwGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 5),
    _TmnxWlanGwGrpAdminState_Type()
)
tmnxWlanGwGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpAdminState.setStatus("current")


class _TmnxWlanGwGrpActiveIomLimit_Type(Unsigned32):
    """Custom type tmnxWlanGwGrpActiveIomLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TmnxWlanGwGrpActiveIomLimit_Type.__name__ = "Unsigned32"
_TmnxWlanGwGrpActiveIomLimit_Object = MibTableColumn
tmnxWlanGwGrpActiveIomLimit = _TmnxWlanGwGrpActiveIomLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 6),
    _TmnxWlanGwGrpActiveIomLimit_Type()
)
tmnxWlanGwGrpActiveIomLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpActiveIomLimit.setStatus("current")


class _TmnxWlanGwGrpPortPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwGrpPortPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwGrpPortPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwGrpPortPlcy_Object = MibTableColumn
tmnxWlanGwGrpPortPlcy = _TmnxWlanGwGrpPortPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 7),
    _TmnxWlanGwGrpPortPlcy_Type()
)
tmnxWlanGwGrpPortPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpPortPlcy.setStatus("current")


class _TmnxWlanGwGrpTunnelPortPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwGrpTunnelPortPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwGrpTunnelPortPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwGrpTunnelPortPlcy_Object = MibTableColumn
tmnxWlanGwGrpTunnelPortPlcy = _TmnxWlanGwGrpTunnelPortPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 8),
    _TmnxWlanGwGrpTunnelPortPlcy_Type()
)
tmnxWlanGwGrpTunnelPortPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpTunnelPortPlcy.setStatus("current")


class _TmnxWlanGwGrpIsaAaGroup_Type(TmnxBsxIsaAaGroupIndexOrZero):
    """Custom type tmnxWlanGwGrpIsaAaGroup based on TmnxBsxIsaAaGroupIndexOrZero"""
    defaultValue = 0


_TmnxWlanGwGrpIsaAaGroup_Type.__name__ = "TmnxBsxIsaAaGroupIndexOrZero"
_TmnxWlanGwGrpIsaAaGroup_Object = MibTableColumn
tmnxWlanGwGrpIsaAaGroup = _TmnxWlanGwGrpIsaAaGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 9),
    _TmnxWlanGwGrpIsaAaGroup_Type()
)
tmnxWlanGwGrpIsaAaGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpIsaAaGroup.setStatus("current")
_TmnxWlanGwGrpOperState_Type = TmnxOperState
_TmnxWlanGwGrpOperState_Object = MibTableColumn
tmnxWlanGwGrpOperState = _TmnxWlanGwGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 50),
    _TmnxWlanGwGrpOperState_Type()
)
tmnxWlanGwGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpOperState.setStatus("current")
_TmnxWlanGwGrpDegraded_Type = TruthValue
_TmnxWlanGwGrpDegraded_Object = MibTableColumn
tmnxWlanGwGrpDegraded = _TmnxWlanGwGrpDegraded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 1, 1, 51),
    _TmnxWlanGwGrpDegraded_Type()
)
tmnxWlanGwGrpDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpDegraded.setStatus("current")
_TmnxWlanGwIomTable_Object = MibTable
tmnxWlanGwIomTable = _TmnxWlanGwIomTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIomTable.setStatus("current")
_TmnxWlanGwIomEntry_Object = MibTableRow
tmnxWlanGwIomEntry = _TmnxWlanGwIomEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1)
)
tmnxWlanGwIomEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIomEntry.setStatus("current")
_TmnxWlanGwIomRowStatus_Type = RowStatus
_TmnxWlanGwIomRowStatus_Object = MibTableColumn
tmnxWlanGwIomRowStatus = _TmnxWlanGwIomRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 1),
    _TmnxWlanGwIomRowStatus_Type()
)
tmnxWlanGwIomRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIomRowStatus.setStatus("current")
_TmnxWlanGwIomLastMgmtChange_Type = TimeStamp
_TmnxWlanGwIomLastMgmtChange_Object = MibTableColumn
tmnxWlanGwIomLastMgmtChange = _TmnxWlanGwIomLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 2),
    _TmnxWlanGwIomLastMgmtChange_Type()
)
tmnxWlanGwIomLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIomLastMgmtChange.setStatus("current")
_TmnxWlanGwIomOperState_Type = TmnxWlanGwIsaIomOperState
_TmnxWlanGwIomOperState_Object = MibTableColumn
tmnxWlanGwIomOperState = _TmnxWlanGwIomOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 2, 1, 3),
    _TmnxWlanGwIomOperState_Type()
)
tmnxWlanGwIomOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIomOperState.setStatus("current")
_TmnxWlanGwIsaMemberTable_Object = MibTable
tmnxWlanGwIsaMemberTable = _TmnxWlanGwIsaMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberTable.setStatus("current")
_TmnxWlanGwIsaMemberEntry_Object = MibTableRow
tmnxWlanGwIsaMemberEntry = _TmnxWlanGwIsaMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1)
)
tmnxWlanGwIsaMemberEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEntry.setStatus("current")
_TmnxWlanGwIsaMemberId_Type = Unsigned32
_TmnxWlanGwIsaMemberId_Object = MibTableColumn
tmnxWlanGwIsaMemberId = _TmnxWlanGwIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 1),
    _TmnxWlanGwIsaMemberId_Type()
)
tmnxWlanGwIsaMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberId.setStatus("current")
_TmnxWlanGwIsaMemberChassisIndex_Type = TmnxChassisIndexOrZero
_TmnxWlanGwIsaMemberChassisIndex_Object = MibTableColumn
tmnxWlanGwIsaMemberChassisIndex = _TmnxWlanGwIsaMemberChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 2),
    _TmnxWlanGwIsaMemberChassisIndex_Type()
)
tmnxWlanGwIsaMemberChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberChassisIndex.setStatus("current")
_TmnxWlanGwIsaMemberCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxWlanGwIsaMemberCardSlotNum_Object = MibTableColumn
tmnxWlanGwIsaMemberCardSlotNum = _TmnxWlanGwIsaMemberCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 3),
    _TmnxWlanGwIsaMemberCardSlotNum_Type()
)
tmnxWlanGwIsaMemberCardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberCardSlotNum.setStatus("current")
_TmnxWlanGwIsaMemberSlotNum_Type = Unsigned32
_TmnxWlanGwIsaMemberSlotNum_Object = MibTableColumn
tmnxWlanGwIsaMemberSlotNum = _TmnxWlanGwIsaMemberSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 4),
    _TmnxWlanGwIsaMemberSlotNum_Type()
)
tmnxWlanGwIsaMemberSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberSlotNum.setStatus("current")
_TmnxWlanGwIsaMemberNumSoftGreTu_Type = Gauge32
_TmnxWlanGwIsaMemberNumSoftGreTu_Object = MibTableColumn
tmnxWlanGwIsaMemberNumSoftGreTu = _TmnxWlanGwIsaMemberNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 5),
    _TmnxWlanGwIsaMemberNumSoftGreTu_Type()
)
tmnxWlanGwIsaMemberNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberNumSoftGreTu.setStatus("current")
_TmnxWlanGwIsaMemberNumUe_Type = Gauge32
_TmnxWlanGwIsaMemberNumUe_Object = MibTableColumn
tmnxWlanGwIsaMemberNumUe = _TmnxWlanGwIsaMemberNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 6),
    _TmnxWlanGwIsaMemberNumUe_Type()
)
tmnxWlanGwIsaMemberNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberNumUe.setStatus("current")
_TmnxWlanGwIsaMemberEegMemberAct_Type = Gauge32
_TmnxWlanGwIsaMemberEegMemberAct_Object = MibTableColumn
tmnxWlanGwIsaMemberEegMemberAct = _TmnxWlanGwIsaMemberEegMemberAct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 7),
    _TmnxWlanGwIsaMemberEegMemberAct_Type()
)
tmnxWlanGwIsaMemberEegMemberAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEegMemberAct.setStatus("current")
_TmnxWlanGwIsaMemberEegMemberPend_Type = Gauge32
_TmnxWlanGwIsaMemberEegMemberPend_Object = MibTableColumn
tmnxWlanGwIsaMemberEegMemberPend = _TmnxWlanGwIsaMemberEegMemberPend_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 8),
    _TmnxWlanGwIsaMemberEegMemberPend_Type()
)
tmnxWlanGwIsaMemberEegMemberPend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberEegMemberPend.setStatus("current")
_TmnxWlanGwIsaMemberTuQosProblem_Type = Gauge32
_TmnxWlanGwIsaMemberTuQosProblem_Object = MibTableColumn
tmnxWlanGwIsaMemberTuQosProblem = _TmnxWlanGwIsaMemberTuQosProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 3, 1, 9),
    _TmnxWlanGwIsaMemberTuQosProblem_Type()
)
tmnxWlanGwIsaMemberTuQosProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberTuQosProblem.setStatus("current")
_TmnxWlanGwIsaMemberStatsTable_Object = MibTable
tmnxWlanGwIsaMemberStatsTable = _TmnxWlanGwIsaMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsTable.setStatus("current")
_TmnxWlanGwIsaMemberStatsEntry_Object = MibTableRow
tmnxWlanGwIsaMemberStatsEntry = _TmnxWlanGwIsaMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1)
)
tmnxWlanGwIsaMemberStatsEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsType"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsEntry.setStatus("current")


class _TmnxWlanGwIsaMemberStatsType_Type(Unsigned32):
    """Custom type tmnxWlanGwIsaMemberStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxWlanGwIsaMemberStatsType_Type.__name__ = "Unsigned32"
_TmnxWlanGwIsaMemberStatsType_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsType = _TmnxWlanGwIsaMemberStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 1),
    _TmnxWlanGwIsaMemberStatsType_Type()
)
tmnxWlanGwIsaMemberStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsType.setStatus("current")


class _TmnxWlanGwIsaMemberStatsName_Type(DisplayString):
    """Custom type tmnxWlanGwIsaMemberStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWlanGwIsaMemberStatsName_Type.__name__ = "DisplayString"
_TmnxWlanGwIsaMemberStatsName_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsName = _TmnxWlanGwIsaMemberStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 2),
    _TmnxWlanGwIsaMemberStatsName_Type()
)
tmnxWlanGwIsaMemberStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsName.setStatus("current")
_TmnxWlanGwIsaMemberStatsVal_Type = Counter32
_TmnxWlanGwIsaMemberStatsVal_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsVal = _TmnxWlanGwIsaMemberStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 3),
    _TmnxWlanGwIsaMemberStatsVal_Type()
)
tmnxWlanGwIsaMemberStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsVal.setStatus("current")
_TmnxWlanGwIsaMemberStatsValHw_Type = Counter32
_TmnxWlanGwIsaMemberStatsValHw_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsValHw = _TmnxWlanGwIsaMemberStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 4),
    _TmnxWlanGwIsaMemberStatsValHw_Type()
)
tmnxWlanGwIsaMemberStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsValHw.setStatus("current")
_TmnxWlanGwIsaMemberStatsValue_Type = Counter64
_TmnxWlanGwIsaMemberStatsValue_Object = MibTableColumn
tmnxWlanGwIsaMemberStatsValue = _TmnxWlanGwIsaMemberStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 1, 4, 1, 5),
    _TmnxWlanGwIsaMemberStatsValue_Type()
)
tmnxWlanGwIsaMemberStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIsaMemberStatsValue.setStatus("current")
_TmnxWlanGwSoftGreObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwSoftGreObjs = _TmnxWlanGwSoftGreObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2)
)
_TmnxWlanGwSoftGreIfTable_Object = MibTable
tmnxWlanGwSoftGreIfTable = _TmnxWlanGwSoftGreIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTable.setStatus("current")
_TmnxWlanGwSoftGreIfEntry_Object = MibTableRow
tmnxWlanGwSoftGreIfEntry = _TmnxWlanGwSoftGreIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1)
)
tmnxWlanGwSoftGreIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEntry.setStatus("current")
_TmnxWlanGwSoftGreIfLastCh_Type = TimeStamp
_TmnxWlanGwSoftGreIfLastCh_Object = MibTableColumn
tmnxWlanGwSoftGreIfLastCh = _TmnxWlanGwSoftGreIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 1),
    _TmnxWlanGwSoftGreIfLastCh_Type()
)
tmnxWlanGwSoftGreIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfLastCh.setStatus("current")


class _TmnxWlanGwSoftGreIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxWlanGwSoftGreIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxWlanGwSoftGreIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxWlanGwSoftGreIfAdminState_Object = MibTableColumn
tmnxWlanGwSoftGreIfAdminState = _TmnxWlanGwSoftGreIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 2),
    _TmnxWlanGwSoftGreIfAdminState_Type()
)
tmnxWlanGwSoftGreIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAdminState.setStatus("current")


class _TmnxWlanGwSoftGreIfRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwSoftGreIfRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwSoftGreIfRouter_Object = MibTableColumn
tmnxWlanGwSoftGreIfRouter = _TmnxWlanGwSoftGreIfRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 3),
    _TmnxWlanGwSoftGreIfRouter_Type()
)
tmnxWlanGwSoftGreIfRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRouter.setStatus("current")


class _TmnxWlanGwSoftGreIfGwAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreIfGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfGwAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreIfGwAddrType_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwAddrType = _TmnxWlanGwSoftGreIfGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 4),
    _TmnxWlanGwSoftGreIfGwAddrType_Type()
)
tmnxWlanGwSoftGreIfGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwAddrType.setStatus("current")


class _TmnxWlanGwSoftGreIfGwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreIfGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreIfGwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreIfGwAddr_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwAddr = _TmnxWlanGwSoftGreIfGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 5),
    _TmnxWlanGwSoftGreIfGwAddr_Type()
)
tmnxWlanGwSoftGreIfGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwAddr.setStatus("current")


class _TmnxWlanGwSoftGreIfGrpId_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwSoftGreIfGrpId based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfGrpId_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwSoftGreIfGrpId_Object = MibTableColumn
tmnxWlanGwSoftGreIfGrpId = _TmnxWlanGwSoftGreIfGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 6),
    _TmnxWlanGwSoftGreIfGrpId_Type()
)
tmnxWlanGwSoftGreIfGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGrpId.setStatus("current")


class _TmnxWlanGwSoftGreIfShapingType_Type(Integer32):
    """Custom type tmnxWlanGwSoftGreIfShapingType based on Integer32"""
    defaultValue = 0

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
          ("perTunnel", 1),
          ("perRetailer", 2))
    )


_TmnxWlanGwSoftGreIfShapingType_Type.__name__ = "Integer32"
_TmnxWlanGwSoftGreIfShapingType_Object = MibTableColumn
tmnxWlanGwSoftGreIfShapingType = _TmnxWlanGwSoftGreIfShapingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 7),
    _TmnxWlanGwSoftGreIfShapingType_Type()
)
tmnxWlanGwSoftGreIfShapingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfShapingType.setStatus("current")


class _TmnxWlanGwSoftGreIfShapeMultiUe_Type(TruthValue):
    """Custom type tmnxWlanGwSoftGreIfShapeMultiUe based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfShapeMultiUe_Type.__name__ = "TruthValue"
_TmnxWlanGwSoftGreIfShapeMultiUe_Object = MibTableColumn
tmnxWlanGwSoftGreIfShapeMultiUe = _TmnxWlanGwSoftGreIfShapeMultiUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 8),
    _TmnxWlanGwSoftGreIfShapeMultiUe_Type()
)
tmnxWlanGwSoftGreIfShapeMultiUe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfShapeMultiUe.setStatus("current")


class _TmnxWlanGwSoftGreIfEQosPlcy_Type(TPolicyID):
    """Custom type tmnxWlanGwSoftGreIfEQosPlcy based on TPolicyID"""
    defaultValue = 1

    subtypeSpec = TPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxWlanGwSoftGreIfEQosPlcy_Type.__name__ = "TPolicyID"
_TmnxWlanGwSoftGreIfEQosPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreIfEQosPlcy = _TmnxWlanGwSoftGreIfEQosPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 9),
    _TmnxWlanGwSoftGreIfEQosPlcy_Type()
)
tmnxWlanGwSoftGreIfEQosPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEQosPlcy.setStatus("current")


class _TmnxWlanGwSoftGreIfESchedPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreIfESchedPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreIfESchedPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreIfESchedPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreIfESchedPlcy = _TmnxWlanGwSoftGreIfESchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 10),
    _TmnxWlanGwSoftGreIfESchedPlcy_Type()
)
tmnxWlanGwSoftGreIfESchedPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfESchedPlcy.setStatus("current")


class _TmnxWlanGwSoftGreIfEAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type tmnxWlanGwSoftGreIfEAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_TmnxWlanGwSoftGreIfEAggRateLimit_Type.__name__ = "TPortSchedulerPIR"
_TmnxWlanGwSoftGreIfEAggRateLimit_Object = MibTableColumn
tmnxWlanGwSoftGreIfEAggRateLimit = _TmnxWlanGwSoftGreIfEAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 11),
    _TmnxWlanGwSoftGreIfEAggRateLimit_Type()
)
tmnxWlanGwSoftGreIfEAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEAggRateLimit.setUnits("kbps")


class _TmnxWlanGwSoftGreIfMobTrigger_Type(Bits):
    """Custom type tmnxWlanGwSoftGreIfMobTrigger based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("data", 0),
          ("iapp", 1))
    )

_TmnxWlanGwSoftGreIfMobTrigger_Type.__name__ = "Bits"
_TmnxWlanGwSoftGreIfMobTrigger_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobTrigger = _TmnxWlanGwSoftGreIfMobTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 12),
    _TmnxWlanGwSoftGreIfMobTrigger_Type()
)
tmnxWlanGwSoftGreIfMobTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobTrigger.setStatus("current")


class _TmnxWlanGwSoftGreIfMobHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfMobHoldTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxWlanGwSoftGreIfMobHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfMobHoldTime_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobHoldTime = _TmnxWlanGwSoftGreIfMobHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 13),
    _TmnxWlanGwSoftGreIfMobHoldTime_Type()
)
tmnxWlanGwSoftGreIfMobHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobHoldTime.setUnits("seconds")


class _TmnxWlanGwSoftGreIfDefRetailSvc_Type(TmnxServId):
    """Custom type tmnxWlanGwSoftGreIfDefRetailSvc based on TmnxServId"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfDefRetailSvc_Type.__name__ = "TmnxServId"
_TmnxWlanGwSoftGreIfDefRetailSvc_Object = MibTableColumn
tmnxWlanGwSoftGreIfDefRetailSvc = _TmnxWlanGwSoftGreIfDefRetailSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 14),
    _TmnxWlanGwSoftGreIfDefRetailSvc_Type()
)
tmnxWlanGwSoftGreIfDefRetailSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfDefRetailSvc.setStatus("current")


class _TmnxWlanGwSoftGreIfTcpMssAdjust_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfTcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_TmnxWlanGwSoftGreIfTcpMssAdjust_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfTcpMssAdjust_Object = MibTableColumn
tmnxWlanGwSoftGreIfTcpMssAdjust = _TmnxWlanGwSoftGreIfTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 15),
    _TmnxWlanGwSoftGreIfTcpMssAdjust_Type()
)
tmnxWlanGwSoftGreIfTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTcpMssAdjust.setUnits("bytes")


class _TmnxWlanGwSoftGreIfEHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfEHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxWlanGwSoftGreIfEHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfEHoldTime_Object = MibTableColumn
tmnxWlanGwSoftGreIfEHoldTime = _TmnxWlanGwSoftGreIfEHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 16),
    _TmnxWlanGwSoftGreIfEHoldTime_Type()
)
tmnxWlanGwSoftGreIfEHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfEHoldTime.setUnits("seconds")


class _TmnxWlanGwSoftGreIfDataTrigg_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfDataTrigg based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfDataTrigg_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfDataTrigg_Object = MibTableColumn
tmnxWlanGwSoftGreIfDataTrigg = _TmnxWlanGwSoftGreIfDataTrigg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 18),
    _TmnxWlanGwSoftGreIfDataTrigg_Type()
)
tmnxWlanGwSoftGreIfDataTrigg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfDataTrigg.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfAuthPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreIfAuthPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreIfAuthPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreIfAuthPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreIfAuthPlcy = _TmnxWlanGwSoftGreIfAuthPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 19),
    _TmnxWlanGwSoftGreIfAuthPlcy_Type()
)
tmnxWlanGwSoftGreIfAuthPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAuthPlcy.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfAuthHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreIfAuthHoldTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxWlanGwSoftGreIfAuthHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreIfAuthHoldTime_Object = MibTableColumn
tmnxWlanGwSoftGreIfAuthHoldTime = _TmnxWlanGwSoftGreIfAuthHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 20),
    _TmnxWlanGwSoftGreIfAuthHoldTime_Type()
)
tmnxWlanGwSoftGreIfAuthHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAuthHoldTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfAuthHoldTime.setUnits("seconds")


class _TmnxWlanGwSoftGreIfRadProxVrtr_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwSoftGreIfRadProxVrtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfRadProxVrtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwSoftGreIfRadProxVrtr_Object = MibTableColumn
tmnxWlanGwSoftGreIfRadProxVrtr = _TmnxWlanGwSoftGreIfRadProxVrtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 21),
    _TmnxWlanGwSoftGreIfRadProxVrtr_Type()
)
tmnxWlanGwSoftGreIfRadProxVrtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRadProxVrtr.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfRadProxSrv_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreIfRadProxSrv based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreIfRadProxSrv_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreIfRadProxSrv_Object = MibTableColumn
tmnxWlanGwSoftGreIfRadProxSrv = _TmnxWlanGwSoftGreIfRadProxSrv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 22),
    _TmnxWlanGwSoftGreIfRadProxSrv_Type()
)
tmnxWlanGwSoftGreIfRadProxSrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRadProxSrv.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfRadProxMacFmt_Type(TmnxMacSpecification):
    """Custom type tmnxWlanGwSoftGreIfRadProxMacFmt based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxWlanGwSoftGreIfRadProxMacFmt_Type.__name__ = "TmnxMacSpecification"
_TmnxWlanGwSoftGreIfRadProxMacFmt_Object = MibTableColumn
tmnxWlanGwSoftGreIfRadProxMacFmt = _TmnxWlanGwSoftGreIfRadProxMacFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 23),
    _TmnxWlanGwSoftGreIfRadProxMacFmt_Type()
)
tmnxWlanGwSoftGreIfRadProxMacFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfRadProxMacFmt.setStatus("obsolete")


class _TmnxWlanGwSoftGreIfGwV6AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreIfGwV6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreIfGwV6AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreIfGwV6AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwV6AddrType = _TmnxWlanGwSoftGreIfGwV6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 29),
    _TmnxWlanGwSoftGreIfGwV6AddrType_Type()
)
tmnxWlanGwSoftGreIfGwV6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwV6AddrType.setStatus("current")


class _TmnxWlanGwSoftGreIfGwV6Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreIfGwV6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreIfGwV6Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreIfGwV6Addr_Object = MibTableColumn
tmnxWlanGwSoftGreIfGwV6Addr = _TmnxWlanGwSoftGreIfGwV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 30),
    _TmnxWlanGwSoftGreIfGwV6Addr_Type()
)
tmnxWlanGwSoftGreIfGwV6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfGwV6Addr.setStatus("current")


class _TmnxWlanGwSoftGreIfMobArpAp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreIfMobArpAp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfMobArpAp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreIfMobArpAp_Object = MibTableColumn
tmnxWlanGwSoftGreIfMobArpAp = _TmnxWlanGwSoftGreIfMobArpAp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 32),
    _TmnxWlanGwSoftGreIfMobArpAp_Type()
)
tmnxWlanGwSoftGreIfMobArpAp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfMobArpAp.setStatus("current")


class _TmnxWlanGwSoftGreIfDownIfGrpDeg_Type(TruthValue):
    """Custom type tmnxWlanGwSoftGreIfDownIfGrpDeg based on TruthValue"""
    defaultValue = 2


_TmnxWlanGwSoftGreIfDownIfGrpDeg_Type.__name__ = "TruthValue"
_TmnxWlanGwSoftGreIfDownIfGrpDeg_Object = MibTableColumn
tmnxWlanGwSoftGreIfDownIfGrpDeg = _TmnxWlanGwSoftGreIfDownIfGrpDeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 35),
    _TmnxWlanGwSoftGreIfDownIfGrpDeg_Type()
)
tmnxWlanGwSoftGreIfDownIfGrpDeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfDownIfGrpDeg.setStatus("current")
_TmnxWlanGwSoftGreIfNumSoftGreTu_Type = Gauge32
_TmnxWlanGwSoftGreIfNumSoftGreTu_Object = MibTableColumn
tmnxWlanGwSoftGreIfNumSoftGreTu = _TmnxWlanGwSoftGreIfNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 1, 1, 100),
    _TmnxWlanGwSoftGreIfNumSoftGreTu_Type()
)
tmnxWlanGwSoftGreIfNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfNumSoftGreTu.setStatus("current")
_TmnxWlanGwSoftGreTuTable_Object = MibTable
tmnxWlanGwSoftGreTuTable = _TmnxWlanGwSoftGreTuTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuTable.setStatus("current")
_TmnxWlanGwSoftGreTuEntry_Object = MibTableRow
tmnxWlanGwSoftGreTuEntry = _TmnxWlanGwSoftGreTuEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1)
)
tmnxWlanGwSoftGreTuEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEntry.setStatus("current")
_TmnxWlanGwSoftGreTuRemoteAddrTyp_Type = InetAddressType
_TmnxWlanGwSoftGreTuRemoteAddrTyp_Object = MibTableColumn
tmnxWlanGwSoftGreTuRemoteAddrTyp = _TmnxWlanGwSoftGreTuRemoteAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 1),
    _TmnxWlanGwSoftGreTuRemoteAddrTyp_Type()
)
tmnxWlanGwSoftGreTuRemoteAddrTyp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuRemoteAddrTyp.setStatus("current")


class _TmnxWlanGwSoftGreTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwSoftGreTuRemoteAddr = _TmnxWlanGwSoftGreTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 2),
    _TmnxWlanGwSoftGreTuRemoteAddr_Type()
)
tmnxWlanGwSoftGreTuRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuRemoteAddr.setStatus("current")
_TmnxWlanGwSoftGreTuLocalAddrType_Type = InetAddressType
_TmnxWlanGwSoftGreTuLocalAddrType_Object = MibTableColumn
tmnxWlanGwSoftGreTuLocalAddrType = _TmnxWlanGwSoftGreTuLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 3),
    _TmnxWlanGwSoftGreTuLocalAddrType_Type()
)
tmnxWlanGwSoftGreTuLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuLocalAddrType.setStatus("current")


class _TmnxWlanGwSoftGreTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreTuLocalAddr_Object = MibTableColumn
tmnxWlanGwSoftGreTuLocalAddr = _TmnxWlanGwSoftGreTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 4),
    _TmnxWlanGwSoftGreTuLocalAddr_Type()
)
tmnxWlanGwSoftGreTuLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuLocalAddr.setStatus("current")


class _TmnxWlanGwSoftGreTuEstabTime_Type(DateAndTime):
    """Custom type tmnxWlanGwSoftGreTuEstabTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwSoftGreTuEstabTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwSoftGreTuEstabTime_Object = MibTableColumn
tmnxWlanGwSoftGreTuEstabTime = _TmnxWlanGwSoftGreTuEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 5),
    _TmnxWlanGwSoftGreTuEstabTime_Type()
)
tmnxWlanGwSoftGreTuEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuEstabTime.setStatus("current")
_TmnxWlanGwSoftGreTuIsaGroup_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwSoftGreTuIsaGroup_Object = MibTableColumn
tmnxWlanGwSoftGreTuIsaGroup = _TmnxWlanGwSoftGreTuIsaGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 6),
    _TmnxWlanGwSoftGreTuIsaGroup_Type()
)
tmnxWlanGwSoftGreTuIsaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuIsaGroup.setStatus("current")
_TmnxWlanGwSoftGreTuIsaMember_Type = Unsigned32
_TmnxWlanGwSoftGreTuIsaMember_Object = MibTableColumn
tmnxWlanGwSoftGreTuIsaMember = _TmnxWlanGwSoftGreTuIsaMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 7),
    _TmnxWlanGwSoftGreTuIsaMember_Type()
)
tmnxWlanGwSoftGreTuIsaMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuIsaMember.setStatus("current")
_TmnxWlanGwSoftGreTuNumUe_Type = Gauge32
_TmnxWlanGwSoftGreTuNumUe_Object = MibTableColumn
tmnxWlanGwSoftGreTuNumUe = _TmnxWlanGwSoftGreTuNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 8),
    _TmnxWlanGwSoftGreTuNumUe_Type()
)
tmnxWlanGwSoftGreTuNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuNumUe.setStatus("current")
_TmnxWlanGwSoftGreTuApMacAddress_Type = MacAddress
_TmnxWlanGwSoftGreTuApMacAddress_Object = MibTableColumn
tmnxWlanGwSoftGreTuApMacAddress = _TmnxWlanGwSoftGreTuApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 10),
    _TmnxWlanGwSoftGreTuApMacAddress_Type()
)
tmnxWlanGwSoftGreTuApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuApMacAddress.setStatus("current")
_TmnxWlanGwSoftGreTuApLearnFailed_Type = TruthValue
_TmnxWlanGwSoftGreTuApLearnFailed_Object = MibTableColumn
tmnxWlanGwSoftGreTuApLearnFailed = _TmnxWlanGwSoftGreTuApLearnFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 2, 1, 11),
    _TmnxWlanGwSoftGreTuApLearnFailed_Type()
)
tmnxWlanGwSoftGreTuApLearnFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuApLearnFailed.setStatus("current")
_TmnxWlanGwTuQosTable_Object = MibTable
tmnxWlanGwTuQosTable = _TmnxWlanGwTuQosTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosTable.setStatus("current")
_TmnxWlanGwTuQosEntry_Object = MibTableRow
tmnxWlanGwTuQosEntry = _TmnxWlanGwTuQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1)
)
tmnxWlanGwTuQosEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRetailService"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEntry.setStatus("current")
_TmnxWlanGwTuQosRetailService_Type = TmnxServId
_TmnxWlanGwTuQosRetailService_Object = MibTableColumn
tmnxWlanGwTuQosRetailService = _TmnxWlanGwTuQosRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 1),
    _TmnxWlanGwTuQosRetailService_Type()
)
tmnxWlanGwTuQosRetailService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosRetailService.setStatus("current")
_TmnxWlanGwTuQosEegSvcId_Type = TmnxServId
_TmnxWlanGwTuQosEegSvcId_Object = MibTableColumn
tmnxWlanGwTuQosEegSvcId = _TmnxWlanGwTuQosEegSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 2),
    _TmnxWlanGwTuQosEegSvcId_Type()
)
tmnxWlanGwTuQosEegSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegSvcId.setStatus("current")
_TmnxWlanGwTuQosEegPortId_Type = TmnxPortID
_TmnxWlanGwTuQosEegPortId_Object = MibTableColumn
tmnxWlanGwTuQosEegPortId = _TmnxWlanGwTuQosEegPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 3),
    _TmnxWlanGwTuQosEegPortId_Type()
)
tmnxWlanGwTuQosEegPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegPortId.setStatus("current")
_TmnxWlanGwTuQosEegEncapValue_Type = TmnxEncapVal
_TmnxWlanGwTuQosEegEncapValue_Object = MibTableColumn
tmnxWlanGwTuQosEegEncapValue = _TmnxWlanGwTuQosEegEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 4),
    _TmnxWlanGwTuQosEegEncapValue_Type()
)
tmnxWlanGwTuQosEegEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegEncapValue.setStatus("current")
_TmnxWlanGwTuQosEegName_Type = TNamedItemOrEmpty
_TmnxWlanGwTuQosEegName_Object = MibTableColumn
tmnxWlanGwTuQosEegName = _TmnxWlanGwTuQosEegName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 5),
    _TmnxWlanGwTuQosEegName_Type()
)
tmnxWlanGwTuQosEegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegName.setStatus("current")
_TmnxWlanGwTuQosEegMember_Type = SvcISID
_TmnxWlanGwTuQosEegMember_Object = MibTableColumn
tmnxWlanGwTuQosEegMember = _TmnxWlanGwTuQosEegMember_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 6),
    _TmnxWlanGwTuQosEegMember_Type()
)
tmnxWlanGwTuQosEegMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosEegMember.setStatus("current")
_TmnxWlanGwTuQosState_Type = TmnxWlanGwQoSOperState
_TmnxWlanGwTuQosState_Object = MibTableColumn
tmnxWlanGwTuQosState = _TmnxWlanGwTuQosState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 7),
    _TmnxWlanGwTuQosState_Type()
)
tmnxWlanGwTuQosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosState.setStatus("current")
_TmnxWlanGwTuQosNumUe_Type = Gauge32
_TmnxWlanGwTuQosNumUe_Object = MibTableColumn
tmnxWlanGwTuQosNumUe = _TmnxWlanGwTuQosNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 8),
    _TmnxWlanGwTuQosNumUe_Type()
)
tmnxWlanGwTuQosNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosNumUe.setStatus("current")
_TmnxWlanGwTuQosRemainingHoldTime_Type = Gauge32
_TmnxWlanGwTuQosRemainingHoldTime_Object = MibTableColumn
tmnxWlanGwTuQosRemainingHoldTime = _TmnxWlanGwTuQosRemainingHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 3, 1, 9),
    _TmnxWlanGwTuQosRemainingHoldTime_Type()
)
tmnxWlanGwTuQosRemainingHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosRemainingHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosRemainingHoldTime.setUnits("seconds")
_TmnxWlanGwSoftGreTuUeTable_Object = MibTable
tmnxWlanGwSoftGreTuUeTable = _TmnxWlanGwSoftGreTuUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuUeTable.setStatus("current")
_TmnxWlanGwSoftGreTuUeEntry_Object = MibTableRow
tmnxWlanGwSoftGreTuUeEntry = _TmnxWlanGwSoftGreTuUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 4, 1)
)
tmnxWlanGwSoftGreTuUeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddrTyp"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuLocalAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuUeEntry.setStatus("current")
_TmnxWlanGwSoftGreTuUeSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwSoftGreTuUeSsid_Object = MibTableColumn
tmnxWlanGwSoftGreTuUeSsid = _TmnxWlanGwSoftGreTuUeSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 4, 1, 1),
    _TmnxWlanGwSoftGreTuUeSsid_Type()
)
tmnxWlanGwSoftGreTuUeSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreTuUeSsid.setStatus("current")
_TmnxWlanGwSoftGreXtTable_Object = MibTable
tmnxWlanGwSoftGreXtTable = _TmnxWlanGwSoftGreXtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtTable.setStatus("obsolete")
_TmnxWlanGwSoftGreXtEntry_Object = MibTableRow
tmnxWlanGwSoftGreXtEntry = _TmnxWlanGwSoftGreXtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtEntry.setStatus("obsolete")
_TmnxWlanGwSoftGreXtLastCh_Type = TimeStamp
_TmnxWlanGwSoftGreXtLastCh_Object = MibTableColumn
tmnxWlanGwSoftGreXtLastCh = _TmnxWlanGwSoftGreXtLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 1),
    _TmnxWlanGwSoftGreXtLastCh_Type()
)
tmnxWlanGwSoftGreXtLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtLastCh.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSoftGreXtDhcp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSoftGreXtDhcp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSoftGreXtDhcp_Object = MibTableColumn
tmnxWlanGwSoftGreXtDhcp = _TmnxWlanGwSoftGreXtDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 2),
    _TmnxWlanGwSoftGreXtDhcp_Type()
)
tmnxWlanGwSoftGreXtDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDhcp.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtAddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtAddrType = _TmnxWlanGwSoftGreXtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 3),
    _TmnxWlanGwSoftGreXtAddrType_Type()
)
tmnxWlanGwSoftGreXtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtAddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtAddr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtAddr_Object = MibTableColumn
tmnxWlanGwSoftGreXtAddr = _TmnxWlanGwSoftGreXtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 4),
    _TmnxWlanGwSoftGreXtAddr_Type()
)
tmnxWlanGwSoftGreXtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtAddr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreXtLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwSoftGreXtLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreXtLeaseTime_Object = MibTableColumn
tmnxWlanGwSoftGreXtLeaseTime = _TmnxWlanGwSoftGreXtLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 5),
    _TmnxWlanGwSoftGreXtLeaseTime_Type()
)
tmnxWlanGwSoftGreXtLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtLeaseTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtLeaseTime.setUnits("seconds")


class _TmnxWlanGwSoftGreXtActLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwSoftGreXtActLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwSoftGreXtActLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwSoftGreXtActLeaseTime_Object = MibTableColumn
tmnxWlanGwSoftGreXtActLeaseTime = _TmnxWlanGwSoftGreXtActLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 6),
    _TmnxWlanGwSoftGreXtActLeaseTime_Type()
)
tmnxWlanGwSoftGreXtActLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtActLeaseTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtActLeaseTime.setUnits("seconds")


class _TmnxWlanGwSoftGreXtDns1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtDns1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtDns1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtDns1AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns1AddrType = _TmnxWlanGwSoftGreXtDns1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 7),
    _TmnxWlanGwSoftGreXtDns1AddrType_Type()
)
tmnxWlanGwSoftGreXtDns1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns1AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDns1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtDns1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtDns1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtDns1Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns1Addr = _TmnxWlanGwSoftGreXtDns1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 8),
    _TmnxWlanGwSoftGreXtDns1Addr_Type()
)
tmnxWlanGwSoftGreXtDns1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns1Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDns2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtDns2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtDns2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtDns2AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns2AddrType = _TmnxWlanGwSoftGreXtDns2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 9),
    _TmnxWlanGwSoftGreXtDns2AddrType_Type()
)
tmnxWlanGwSoftGreXtDns2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns2AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtDns2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtDns2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtDns2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtDns2Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtDns2Addr = _TmnxWlanGwSoftGreXtDns2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 10),
    _TmnxWlanGwSoftGreXtDns2Addr_Type()
)
tmnxWlanGwSoftGreXtDns2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtDns2Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtNb1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtNb1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtNb1AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb1AddrType = _TmnxWlanGwSoftGreXtNb1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 11),
    _TmnxWlanGwSoftGreXtNb1AddrType_Type()
)
tmnxWlanGwSoftGreXtNb1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb1AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtNb1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtNb1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtNb1Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb1Addr = _TmnxWlanGwSoftGreXtNb1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 12),
    _TmnxWlanGwSoftGreXtNb1Addr_Type()
)
tmnxWlanGwSoftGreXtNb1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb1Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwSoftGreXtNb2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSoftGreXtNb2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSoftGreXtNb2AddrType_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb2AddrType = _TmnxWlanGwSoftGreXtNb2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 13),
    _TmnxWlanGwSoftGreXtNb2AddrType_Type()
)
tmnxWlanGwSoftGreXtNb2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb2AddrType.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNb2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwSoftGreXtNb2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSoftGreXtNb2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwSoftGreXtNb2Addr_Object = MibTableColumn
tmnxWlanGwSoftGreXtNb2Addr = _TmnxWlanGwSoftGreXtNb2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 14),
    _TmnxWlanGwSoftGreXtNb2Addr_Type()
)
tmnxWlanGwSoftGreXtNb2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNb2Addr.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtHttpRdrPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreXtHttpRdrPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreXtHttpRdrPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreXtHttpRdrPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreXtHttpRdrPlcy = _TmnxWlanGwSoftGreXtHttpRdrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 21),
    _TmnxWlanGwSoftGreXtHttpRdrPlcy_Type()
)
tmnxWlanGwSoftGreXtHttpRdrPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtHttpRdrPlcy.setStatus("obsolete")


class _TmnxWlanGwSoftGreXtNatPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwSoftGreXtNatPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwSoftGreXtNatPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwSoftGreXtNatPlcy_Object = MibTableColumn
tmnxWlanGwSoftGreXtNatPlcy = _TmnxWlanGwSoftGreXtNatPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 5, 1, 22),
    _TmnxWlanGwSoftGreXtNatPlcy_Type()
)
tmnxWlanGwSoftGreXtNatPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreXtNatPlcy.setStatus("obsolete")
_TmnxWlanGwVlanTable_Object = MibTable
tmnxWlanGwVlanTable = _TmnxWlanGwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTable.setStatus("current")
_TmnxWlanGwVlanEntry_Object = MibTableRow
tmnxWlanGwVlanEntry = _TmnxWlanGwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1)
)
tmnxWlanGwVlanEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTagStart"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTagEnd"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanEntry.setStatus("current")


class _TmnxWlanGwVlanTagStart_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanTagStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4096, 4096),
    )


_TmnxWlanGwVlanTagStart_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanTagStart_Object = MibTableColumn
tmnxWlanGwVlanTagStart = _TmnxWlanGwVlanTagStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 1),
    _TmnxWlanGwVlanTagStart_Type()
)
tmnxWlanGwVlanTagStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTagStart.setStatus("current")


class _TmnxWlanGwVlanTagEnd_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanTagEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4096, 4096),
    )


_TmnxWlanGwVlanTagEnd_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanTagEnd_Object = MibTableColumn
tmnxWlanGwVlanTagEnd = _TmnxWlanGwVlanTagEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 2),
    _TmnxWlanGwVlanTagEnd_Type()
)
tmnxWlanGwVlanTagEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTagEnd.setStatus("current")
_TmnxWlanGwVlanRowStatus_Type = RowStatus
_TmnxWlanGwVlanRowStatus_Object = MibTableColumn
tmnxWlanGwVlanRowStatus = _TmnxWlanGwVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 3),
    _TmnxWlanGwVlanRowStatus_Type()
)
tmnxWlanGwVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRowStatus.setStatus("current")
_TmnxWlanGwVlanLastCh_Type = TimeStamp
_TmnxWlanGwVlanLastCh_Object = MibTableColumn
tmnxWlanGwVlanLastCh = _TmnxWlanGwVlanLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 4),
    _TmnxWlanGwVlanLastCh_Type()
)
tmnxWlanGwVlanLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLastCh.setStatus("current")


class _TmnxWlanGwVlanRetailService_Type(TmnxServId):
    """Custom type tmnxWlanGwVlanRetailService based on TmnxServId"""
    defaultValue = 0


_TmnxWlanGwVlanRetailService_Type.__name__ = "TmnxServId"
_TmnxWlanGwVlanRetailService_Object = MibTableColumn
tmnxWlanGwVlanRetailService = _TmnxWlanGwVlanRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 5),
    _TmnxWlanGwVlanRetailService_Type()
)
tmnxWlanGwVlanRetailService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRetailService.setStatus("current")


class _TmnxWlanGwVlanDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDhcp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDhcp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDhcp_Object = MibTableColumn
tmnxWlanGwVlanDhcp = _TmnxWlanGwVlanDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 6),
    _TmnxWlanGwVlanDhcp_Type()
)
tmnxWlanGwVlanDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDhcp.setStatus("current")


class _TmnxWlanGwVlanAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanAddrType_Object = MibTableColumn
tmnxWlanGwVlanAddrType = _TmnxWlanGwVlanAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 7),
    _TmnxWlanGwVlanAddrType_Type()
)
tmnxWlanGwVlanAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAddrType.setStatus("current")


class _TmnxWlanGwVlanAddr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanAddr_Object = MibTableColumn
tmnxWlanGwVlanAddr = _TmnxWlanGwVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 8),
    _TmnxWlanGwVlanAddr_Type()
)
tmnxWlanGwVlanAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAddr.setStatus("current")


class _TmnxWlanGwVlanLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanLeaseTime_Object = MibTableColumn
tmnxWlanGwVlanLeaseTime = _TmnxWlanGwVlanLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 9),
    _TmnxWlanGwVlanLeaseTime_Type()
)
tmnxWlanGwVlanLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanLeaseTime.setUnits("seconds")


class _TmnxWlanGwVlanActLeaseTime_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanActLeaseTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_TmnxWlanGwVlanActLeaseTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanActLeaseTime_Object = MibTableColumn
tmnxWlanGwVlanActLeaseTime = _TmnxWlanGwVlanActLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 10),
    _TmnxWlanGwVlanActLeaseTime_Type()
)
tmnxWlanGwVlanActLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanActLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanActLeaseTime.setUnits("seconds")


class _TmnxWlanGwVlanDns1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanDns1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanDns1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanDns1AddrType_Object = MibTableColumn
tmnxWlanGwVlanDns1AddrType = _TmnxWlanGwVlanDns1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 11),
    _TmnxWlanGwVlanDns1AddrType_Type()
)
tmnxWlanGwVlanDns1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns1AddrType.setStatus("current")


class _TmnxWlanGwVlanDns1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanDns1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanDns1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanDns1Addr_Object = MibTableColumn
tmnxWlanGwVlanDns1Addr = _TmnxWlanGwVlanDns1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 12),
    _TmnxWlanGwVlanDns1Addr_Type()
)
tmnxWlanGwVlanDns1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns1Addr.setStatus("current")


class _TmnxWlanGwVlanDns2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanDns2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanDns2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanDns2AddrType_Object = MibTableColumn
tmnxWlanGwVlanDns2AddrType = _TmnxWlanGwVlanDns2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 13),
    _TmnxWlanGwVlanDns2AddrType_Type()
)
tmnxWlanGwVlanDns2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns2AddrType.setStatus("current")


class _TmnxWlanGwVlanDns2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanDns2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanDns2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanDns2Addr_Object = MibTableColumn
tmnxWlanGwVlanDns2Addr = _TmnxWlanGwVlanDns2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 14),
    _TmnxWlanGwVlanDns2Addr_Type()
)
tmnxWlanGwVlanDns2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDns2Addr.setStatus("current")


class _TmnxWlanGwVlanNb1AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanNb1AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanNb1AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanNb1AddrType_Object = MibTableColumn
tmnxWlanGwVlanNb1AddrType = _TmnxWlanGwVlanNb1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 15),
    _TmnxWlanGwVlanNb1AddrType_Type()
)
tmnxWlanGwVlanNb1AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb1AddrType.setStatus("current")


class _TmnxWlanGwVlanNb1Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanNb1Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanNb1Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanNb1Addr_Object = MibTableColumn
tmnxWlanGwVlanNb1Addr = _TmnxWlanGwVlanNb1Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 16),
    _TmnxWlanGwVlanNb1Addr_Type()
)
tmnxWlanGwVlanNb1Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb1Addr.setStatus("current")


class _TmnxWlanGwVlanNb2AddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwVlanNb2AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwVlanNb2AddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwVlanNb2AddrType_Object = MibTableColumn
tmnxWlanGwVlanNb2AddrType = _TmnxWlanGwVlanNb2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 17),
    _TmnxWlanGwVlanNb2AddrType_Type()
)
tmnxWlanGwVlanNb2AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb2AddrType.setStatus("current")


class _TmnxWlanGwVlanNb2Addr_Type(InetAddress):
    """Custom type tmnxWlanGwVlanNb2Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwVlanNb2Addr_Type.__name__ = "InetAddress"
_TmnxWlanGwVlanNb2Addr_Object = MibTableColumn
tmnxWlanGwVlanNb2Addr = _TmnxWlanGwVlanNb2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 18),
    _TmnxWlanGwVlanNb2Addr_Type()
)
tmnxWlanGwVlanNb2Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNb2Addr.setStatus("current")


class _TmnxWlanGwVlanHttpRdrPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanHttpRdrPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanHttpRdrPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanHttpRdrPlcy_Object = MibTableColumn
tmnxWlanGwVlanHttpRdrPlcy = _TmnxWlanGwVlanHttpRdrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 21),
    _TmnxWlanGwVlanHttpRdrPlcy_Type()
)
tmnxWlanGwVlanHttpRdrPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanHttpRdrPlcy.setStatus("current")


class _TmnxWlanGwVlanNatPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanNatPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanNatPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanNatPlcy_Object = MibTableColumn
tmnxWlanGwVlanNatPlcy = _TmnxWlanGwVlanNatPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 22),
    _TmnxWlanGwVlanNatPlcy_Type()
)
tmnxWlanGwVlanNatPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanNatPlcy.setStatus("current")


class _TmnxWlanGwVlanDataTrigg_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDataTrigg based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDataTrigg_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDataTrigg_Object = MibTableColumn
tmnxWlanGwVlanDataTrigg = _TmnxWlanGwVlanDataTrigg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 30),
    _TmnxWlanGwVlanDataTrigg_Type()
)
tmnxWlanGwVlanDataTrigg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDataTrigg.setStatus("current")


class _TmnxWlanGwVlanAuthPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanAuthPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanAuthPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanAuthPlcy_Object = MibTableColumn
tmnxWlanGwVlanAuthPlcy = _TmnxWlanGwVlanAuthPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 31),
    _TmnxWlanGwVlanAuthPlcy_Type()
)
tmnxWlanGwVlanAuthPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthPlcy.setStatus("current")


class _TmnxWlanGwVlanAuthHoldTime_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanAuthHoldTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxWlanGwVlanAuthHoldTime_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanAuthHoldTime_Object = MibTableColumn
tmnxWlanGwVlanAuthHoldTime = _TmnxWlanGwVlanAuthHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 32),
    _TmnxWlanGwVlanAuthHoldTime_Type()
)
tmnxWlanGwVlanAuthHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthHoldTime.setUnits("seconds")


class _TmnxWlanGwVlanRadProxVrtr_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwVlanRadProxVrtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwVlanRadProxVrtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwVlanRadProxVrtr_Object = MibTableColumn
tmnxWlanGwVlanRadProxVrtr = _TmnxWlanGwVlanRadProxVrtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 34),
    _TmnxWlanGwVlanRadProxVrtr_Type()
)
tmnxWlanGwVlanRadProxVrtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRadProxVrtr.setStatus("current")


class _TmnxWlanGwVlanRadProxSrv_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanRadProxSrv based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanRadProxSrv_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanRadProxSrv_Object = MibTableColumn
tmnxWlanGwVlanRadProxSrv = _TmnxWlanGwVlanRadProxSrv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 35),
    _TmnxWlanGwVlanRadProxSrv_Type()
)
tmnxWlanGwVlanRadProxSrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRadProxSrv.setStatus("current")


class _TmnxWlanGwVlanRadProxMacFmt_Type(TmnxMacSpecification):
    """Custom type tmnxWlanGwVlanRadProxMacFmt based on TmnxMacSpecification"""
    defaultValue = OctetString("aa:")

    subtypeSpec = TmnxMacSpecification.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_TmnxWlanGwVlanRadProxMacFmt_Type.__name__ = "TmnxMacSpecification"
_TmnxWlanGwVlanRadProxMacFmt_Object = MibTableColumn
tmnxWlanGwVlanRadProxMacFmt = _TmnxWlanGwVlanRadProxMacFmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 36),
    _TmnxWlanGwVlanRadProxMacFmt_Type()
)
tmnxWlanGwVlanRadProxMacFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanRadProxMacFmt.setStatus("current")


class _TmnxWlanGwVlanAuthOnDhcp_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanAuthOnDhcp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanAuthOnDhcp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanAuthOnDhcp_Object = MibTableColumn
tmnxWlanGwVlanAuthOnDhcp = _TmnxWlanGwVlanAuthOnDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 6, 1, 40),
    _TmnxWlanGwVlanAuthOnDhcp_Type()
)
tmnxWlanGwVlanAuthOnDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanAuthOnDhcp.setStatus("current")
_TmnxWlanGwSubIfTable_Object = MibTable
tmnxWlanGwSubIfTable = _TmnxWlanGwSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfTable.setStatus("current")
_TmnxWlanGwSubIfEntry_Object = MibTableRow
tmnxWlanGwSubIfEntry = _TmnxWlanGwSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1)
)
tmnxWlanGwSubIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfEntry.setStatus("current")
_TmnxWlanGwSubIfRowStatus_Type = RowStatus
_TmnxWlanGwSubIfRowStatus_Object = MibTableColumn
tmnxWlanGwSubIfRowStatus = _TmnxWlanGwSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 1),
    _TmnxWlanGwSubIfRowStatus_Type()
)
tmnxWlanGwSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRowStatus.setStatus("current")
_TmnxWlanGwSubIfLastCh_Type = TimeStamp
_TmnxWlanGwSubIfLastCh_Object = MibTableColumn
tmnxWlanGwSubIfLastCh = _TmnxWlanGwSubIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 2),
    _TmnxWlanGwSubIfLastCh_Type()
)
tmnxWlanGwSubIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfLastCh.setStatus("current")


class _TmnxWlanGwSubIfRedExpPrefixType_Type(InetAddressType):
    """Custom type tmnxWlanGwSubIfRedExpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSubIfRedExpPrefixType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSubIfRedExpPrefixType_Object = MibTableColumn
tmnxWlanGwSubIfRedExpPrefixType = _TmnxWlanGwSubIfRedExpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 3),
    _TmnxWlanGwSubIfRedExpPrefixType_Type()
)
tmnxWlanGwSubIfRedExpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedExpPrefixType.setStatus("current")


class _TmnxWlanGwSubIfRedExpPrefix_Type(InetAddress):
    """Custom type tmnxWlanGwSubIfRedExpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSubIfRedExpPrefix_Type.__name__ = "InetAddress"
_TmnxWlanGwSubIfRedExpPrefix_Object = MibTableColumn
tmnxWlanGwSubIfRedExpPrefix = _TmnxWlanGwSubIfRedExpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 4),
    _TmnxWlanGwSubIfRedExpPrefix_Type()
)
tmnxWlanGwSubIfRedExpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedExpPrefix.setStatus("current")


class _TmnxWlanGwSubIfRedExpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwSubIfRedExpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwSubIfRedExpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwSubIfRedExpPrefixLen_Object = MibTableColumn
tmnxWlanGwSubIfRedExpPrefixLen = _TmnxWlanGwSubIfRedExpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 5),
    _TmnxWlanGwSubIfRedExpPrefixLen_Type()
)
tmnxWlanGwSubIfRedExpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedExpPrefixLen.setStatus("current")


class _TmnxWlanGwSubIfRedMonPrefixType_Type(InetAddressType):
    """Custom type tmnxWlanGwSubIfRedMonPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwSubIfRedMonPrefixType_Type.__name__ = "InetAddressType"
_TmnxWlanGwSubIfRedMonPrefixType_Object = MibTableColumn
tmnxWlanGwSubIfRedMonPrefixType = _TmnxWlanGwSubIfRedMonPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 6),
    _TmnxWlanGwSubIfRedMonPrefixType_Type()
)
tmnxWlanGwSubIfRedMonPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedMonPrefixType.setStatus("current")


class _TmnxWlanGwSubIfRedMonPrefix_Type(InetAddress):
    """Custom type tmnxWlanGwSubIfRedMonPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwSubIfRedMonPrefix_Type.__name__ = "InetAddress"
_TmnxWlanGwSubIfRedMonPrefix_Object = MibTableColumn
tmnxWlanGwSubIfRedMonPrefix = _TmnxWlanGwSubIfRedMonPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 7),
    _TmnxWlanGwSubIfRedMonPrefix_Type()
)
tmnxWlanGwSubIfRedMonPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedMonPrefix.setStatus("current")


class _TmnxWlanGwSubIfRedMonPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwSubIfRedMonPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxWlanGwSubIfRedMonPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwSubIfRedMonPrefixLen_Object = MibTableColumn
tmnxWlanGwSubIfRedMonPrefixLen = _TmnxWlanGwSubIfRedMonPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 8),
    _TmnxWlanGwSubIfRedMonPrefixLen_Type()
)
tmnxWlanGwSubIfRedMonPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedMonPrefixLen.setStatus("current")


class _TmnxWlanGwSubIfRedAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwSubIfRedAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwSubIfRedAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwSubIfRedAdminState_Object = MibTableColumn
tmnxWlanGwSubIfRedAdminState = _TmnxWlanGwSubIfRedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 9),
    _TmnxWlanGwSubIfRedAdminState_Type()
)
tmnxWlanGwSubIfRedAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedAdminState.setStatus("current")
_TmnxWlanGwSubIfRedActive_Type = TruthValue
_TmnxWlanGwSubIfRedActive_Object = MibTableColumn
tmnxWlanGwSubIfRedActive = _TmnxWlanGwSubIfRedActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 10),
    _TmnxWlanGwSubIfRedActive_Type()
)
tmnxWlanGwSubIfRedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedActive.setStatus("current")


class _TmnxWlanGwSubIfRedSwitch_Type(TmnxActionType):
    """Custom type tmnxWlanGwSubIfRedSwitch based on TmnxActionType"""
    defaultValue = 2


_TmnxWlanGwSubIfRedSwitch_Type.__name__ = "TmnxActionType"
_TmnxWlanGwSubIfRedSwitch_Object = MibTableColumn
tmnxWlanGwSubIfRedSwitch = _TmnxWlanGwSubIfRedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 2, 7, 1, 11),
    _TmnxWlanGwSubIfRedSwitch_Type()
)
tmnxWlanGwSubIfRedSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedSwitch.setStatus("current")
_TmnxWlanGwIfRetailTable_Object = MibTable
tmnxWlanGwIfRetailTable = _TmnxWlanGwIfRetailTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTable.setStatus("obsolete")
_TmnxWlanGwIfRetailEntry_Object = MibTableRow
tmnxWlanGwIfRetailEntry = _TmnxWlanGwIfRetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1)
)
tmnxWlanGwIfRetailEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SERV-MIB", "iesIfIndex"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTagStart"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTagEnd"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailEntry.setStatus("obsolete")
_TmnxWlanGwIfRetailTagStart_Type = QTagFullRange
_TmnxWlanGwIfRetailTagStart_Object = MibTableColumn
tmnxWlanGwIfRetailTagStart = _TmnxWlanGwIfRetailTagStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 1),
    _TmnxWlanGwIfRetailTagStart_Type()
)
tmnxWlanGwIfRetailTagStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTagStart.setStatus("obsolete")
_TmnxWlanGwIfRetailTagEnd_Type = QTagFullRange
_TmnxWlanGwIfRetailTagEnd_Object = MibTableColumn
tmnxWlanGwIfRetailTagEnd = _TmnxWlanGwIfRetailTagEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 2),
    _TmnxWlanGwIfRetailTagEnd_Type()
)
tmnxWlanGwIfRetailTagEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTagEnd.setStatus("obsolete")
_TmnxWlanGwIfRetailRowStatus_Type = RowStatus
_TmnxWlanGwIfRetailRowStatus_Object = MibTableColumn
tmnxWlanGwIfRetailRowStatus = _TmnxWlanGwIfRetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 3),
    _TmnxWlanGwIfRetailRowStatus_Type()
)
tmnxWlanGwIfRetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailRowStatus.setStatus("obsolete")
_TmnxWlanGwIfRetailLastCh_Type = TimeStamp
_TmnxWlanGwIfRetailLastCh_Object = MibTableColumn
tmnxWlanGwIfRetailLastCh = _TmnxWlanGwIfRetailLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 4),
    _TmnxWlanGwIfRetailLastCh_Type()
)
tmnxWlanGwIfRetailLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailLastCh.setStatus("obsolete")
_TmnxWlanGwIfRetailService_Type = TmnxServId
_TmnxWlanGwIfRetailService_Object = MibTableColumn
tmnxWlanGwIfRetailService = _TmnxWlanGwIfRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 3, 1, 5),
    _TmnxWlanGwIfRetailService_Type()
)
tmnxWlanGwIfRetailService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailService.setStatus("obsolete")
_TmnxWlanGwUeTable_Object = MibTable
tmnxWlanGwUeTable = _TmnxWlanGwUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeTable.setStatus("current")
_TmnxWlanGwUeEntry_Object = MibTableRow
tmnxWlanGwUeEntry = _TmnxWlanGwUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1)
)
tmnxWlanGwUeEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeEntry.setStatus("current")
_TmnxWlanGwUeMacAddress_Type = MacAddress
_TmnxWlanGwUeMacAddress_Object = MibTableColumn
tmnxWlanGwUeMacAddress = _TmnxWlanGwUeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 1),
    _TmnxWlanGwUeMacAddress_Type()
)
tmnxWlanGwUeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwUeMacAddress.setStatus("current")
_TmnxWlanGwUeQTag_Type = QTagFullRangeOrNone
_TmnxWlanGwUeQTag_Object = MibTableColumn
tmnxWlanGwUeQTag = _TmnxWlanGwUeQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 3),
    _TmnxWlanGwUeQTag_Type()
)
tmnxWlanGwUeQTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQTag.setStatus("current")
_TmnxWlanGwUeMplsLabel_Type = MplsLabel
_TmnxWlanGwUeMplsLabel_Object = MibTableColumn
tmnxWlanGwUeMplsLabel = _TmnxWlanGwUeMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 4),
    _TmnxWlanGwUeMplsLabel_Type()
)
tmnxWlanGwUeMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeMplsLabel.setStatus("current")
_TmnxWlanGwUeTuRouter_Type = TmnxVRtrID
_TmnxWlanGwUeTuRouter_Object = MibTableColumn
tmnxWlanGwUeTuRouter = _TmnxWlanGwUeTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 5),
    _TmnxWlanGwUeTuRouter_Type()
)
tmnxWlanGwUeTuRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuRouter.setStatus("current")
_TmnxWlanGwUeTuAddrType_Type = InetAddressType
_TmnxWlanGwUeTuAddrType_Object = MibTableColumn
tmnxWlanGwUeTuAddrType = _TmnxWlanGwUeTuAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 6),
    _TmnxWlanGwUeTuAddrType_Type()
)
tmnxWlanGwUeTuAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuAddrType.setStatus("current")


class _TmnxWlanGwUeTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwUeTuRemoteAddr = _TmnxWlanGwUeTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 7),
    _TmnxWlanGwUeTuRemoteAddr_Type()
)
tmnxWlanGwUeTuRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuRemoteAddr.setStatus("current")


class _TmnxWlanGwUeTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeTuLocalAddr_Object = MibTableColumn
tmnxWlanGwUeTuLocalAddr = _TmnxWlanGwUeTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 8),
    _TmnxWlanGwUeTuLocalAddr_Type()
)
tmnxWlanGwUeTuLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuLocalAddr.setStatus("current")
_TmnxWlanGwUeTuQosRetailService_Type = TmnxServId
_TmnxWlanGwUeTuQosRetailService_Object = MibTableColumn
tmnxWlanGwUeTuQosRetailService = _TmnxWlanGwUeTuQosRetailService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 9),
    _TmnxWlanGwUeTuQosRetailService_Type()
)
tmnxWlanGwUeTuQosRetailService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeTuQosRetailService.setStatus("current")
_TmnxWlanGwUeSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwUeSsid_Object = MibTableColumn
tmnxWlanGwUeSsid = _TmnxWlanGwUeSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 10),
    _TmnxWlanGwUeSsid_Type()
)
tmnxWlanGwUeSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeSsid.setStatus("current")
_TmnxWlanGwUePrevApAddrType_Type = InetAddressType
_TmnxWlanGwUePrevApAddrType_Object = MibTableColumn
tmnxWlanGwUePrevApAddrType = _TmnxWlanGwUePrevApAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 11),
    _TmnxWlanGwUePrevApAddrType_Type()
)
tmnxWlanGwUePrevApAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUePrevApAddrType.setStatus("current")


class _TmnxWlanGwUePrevApAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUePrevApAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUePrevApAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUePrevApAddr_Object = MibTableColumn
tmnxWlanGwUePrevApAddr = _TmnxWlanGwUePrevApAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 12),
    _TmnxWlanGwUePrevApAddr_Type()
)
tmnxWlanGwUePrevApAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUePrevApAddr.setStatus("current")


class _TmnxWlanGwUeLastMoveTime_Type(DateAndTime):
    """Custom type tmnxWlanGwUeLastMoveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeLastMoveTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeLastMoveTime_Object = MibTableColumn
tmnxWlanGwUeLastMoveTime = _TmnxWlanGwUeLastMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 13),
    _TmnxWlanGwUeLastMoveTime_Type()
)
tmnxWlanGwUeLastMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeLastMoveTime.setStatus("current")
_TmnxWlanGwUeImsi_Type = TmnxMobImsiStr
_TmnxWlanGwUeImsi_Object = MibTableColumn
tmnxWlanGwUeImsi = _TmnxWlanGwUeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 4, 1, 15),
    _TmnxWlanGwUeImsi_Type()
)
tmnxWlanGwUeImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeImsi.setStatus("current")
_TmnxWlanGwSsidTable_Object = MibTable
tmnxWlanGwSsidTable = _TmnxWlanGwSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwSsidTable.setStatus("current")
_TmnxWlanGwSsidEntry_Object = MibTableRow
tmnxWlanGwSsidEntry = _TmnxWlanGwSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5, 1)
)
tmnxWlanGwSsidEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSsid"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwSsidEntry.setStatus("current")
_TmnxWlanGwSsid_Type = TNamedItem
_TmnxWlanGwSsid_Object = MibTableColumn
tmnxWlanGwSsid = _TmnxWlanGwSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5, 1, 1),
    _TmnxWlanGwSsid_Type()
)
tmnxWlanGwSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwSsid.setStatus("current")
_TmnxWlanGwSsidNumUe_Type = Gauge32
_TmnxWlanGwSsidNumUe_Object = MibTableColumn
tmnxWlanGwSsidNumUe = _TmnxWlanGwSsidNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 5, 1, 2),
    _TmnxWlanGwSsidNumUe_Type()
)
tmnxWlanGwSsidNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSsidNumUe.setStatus("current")
_TmnxWlanGwMgwObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwMgwObjs = _TmnxWlanGwMgwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6)
)
_TmnxWlanGwMgwProfTable_Object = MibTable
tmnxWlanGwMgwProfTable = _TmnxWlanGwMgwProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTable.setStatus("current")
_TmnxWlanGwMgwProfEntry_Object = MibTableRow
tmnxWlanGwMgwProfEntry = _TmnxWlanGwMgwProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1)
)
tmnxWlanGwMgwProfEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfEntry.setStatus("current")
_TmnxWlanGwMgwProfName_Type = TNamedItem
_TmnxWlanGwMgwProfName_Object = MibTableColumn
tmnxWlanGwMgwProfName = _TmnxWlanGwMgwProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 1),
    _TmnxWlanGwMgwProfName_Type()
)
tmnxWlanGwMgwProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfName.setStatus("current")
_TmnxWlanGwMgwProfRowStatus_Type = RowStatus
_TmnxWlanGwMgwProfRowStatus_Object = MibTableColumn
tmnxWlanGwMgwProfRowStatus = _TmnxWlanGwMgwProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 2),
    _TmnxWlanGwMgwProfRowStatus_Type()
)
tmnxWlanGwMgwProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfRowStatus.setStatus("current")
_TmnxWlanGwMgwProfLastChanged_Type = TimeStamp
_TmnxWlanGwMgwProfLastChanged_Object = MibTableColumn
tmnxWlanGwMgwProfLastChanged = _TmnxWlanGwMgwProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 3),
    _TmnxWlanGwMgwProfLastChanged_Type()
)
tmnxWlanGwMgwProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfLastChanged.setStatus("current")


class _TmnxWlanGwMgwProfDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwMgwProfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwMgwProfDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwMgwProfDescription_Object = MibTableColumn
tmnxWlanGwMgwProfDescription = _TmnxWlanGwMgwProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 4),
    _TmnxWlanGwMgwProfDescription_Type()
)
tmnxWlanGwMgwProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfDescription.setStatus("current")


class _TmnxWlanGwMgwProfMsgReTxTimeout_Type(TmnxMobProfMsgReTxTimeout):
    """Custom type tmnxWlanGwMgwProfMsgReTxTimeout based on TmnxMobProfMsgReTxTimeout"""
    defaultValue = 5


_TmnxWlanGwMgwProfMsgReTxTimeout_Type.__name__ = "TmnxMobProfMsgReTxTimeout"
_TmnxWlanGwMgwProfMsgReTxTimeout_Object = MibTableColumn
tmnxWlanGwMgwProfMsgReTxTimeout = _TmnxWlanGwMgwProfMsgReTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 5),
    _TmnxWlanGwMgwProfMsgReTxTimeout_Type()
)
tmnxWlanGwMgwProfMsgReTxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfMsgReTxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfMsgReTxTimeout.setUnits("seconds")


class _TmnxWlanGwMgwProfMsgReTxRetryCnt_Type(TmnxMobProfMsgReTxRetryCount):
    """Custom type tmnxWlanGwMgwProfMsgReTxRetryCnt based on TmnxMobProfMsgReTxRetryCount"""
    defaultValue = 3


_TmnxWlanGwMgwProfMsgReTxRetryCnt_Type.__name__ = "TmnxMobProfMsgReTxRetryCount"
_TmnxWlanGwMgwProfMsgReTxRetryCnt_Object = MibTableColumn
tmnxWlanGwMgwProfMsgReTxRetryCnt = _TmnxWlanGwMgwProfMsgReTxRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 6),
    _TmnxWlanGwMgwProfMsgReTxRetryCnt_Type()
)
tmnxWlanGwMgwProfMsgReTxRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfMsgReTxRetryCnt.setStatus("current")


class _TmnxWlanGwMgwProfKeepAlvTimeout_Type(TmnxMobProfKeepAliveTimeout):
    """Custom type tmnxWlanGwMgwProfKeepAlvTimeout based on TmnxMobProfKeepAliveTimeout"""
    defaultValue = 60


_TmnxWlanGwMgwProfKeepAlvTimeout_Type.__name__ = "TmnxMobProfKeepAliveTimeout"
_TmnxWlanGwMgwProfKeepAlvTimeout_Object = MibTableColumn
tmnxWlanGwMgwProfKeepAlvTimeout = _TmnxWlanGwMgwProfKeepAlvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 7),
    _TmnxWlanGwMgwProfKeepAlvTimeout_Type()
)
tmnxWlanGwMgwProfKeepAlvTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvTimeout.setUnits("seconds")


class _TmnxWlanGwMgwProfKeepAlvRetryCnt_Type(TmnxMobProfKeepAliveRetryCount):
    """Custom type tmnxWlanGwMgwProfKeepAlvRetryCnt based on TmnxMobProfKeepAliveRetryCount"""
    defaultValue = 4


_TmnxWlanGwMgwProfKeepAlvRetryCnt_Type.__name__ = "TmnxMobProfKeepAliveRetryCount"
_TmnxWlanGwMgwProfKeepAlvRetryCnt_Object = MibTableColumn
tmnxWlanGwMgwProfKeepAlvRetryCnt = _TmnxWlanGwMgwProfKeepAlvRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 8),
    _TmnxWlanGwMgwProfKeepAlvRetryCnt_Type()
)
tmnxWlanGwMgwProfKeepAlvRetryCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvRetryCnt.setStatus("current")


class _TmnxWlanGwMgwProfKeepAlvResp_Type(TmnxMobProfKeepAliveResponse):
    """Custom type tmnxWlanGwMgwProfKeepAlvResp based on TmnxMobProfKeepAliveResponse"""
    defaultValue = 5


_TmnxWlanGwMgwProfKeepAlvResp_Type.__name__ = "TmnxMobProfKeepAliveResponse"
_TmnxWlanGwMgwProfKeepAlvResp_Object = MibTableColumn
tmnxWlanGwMgwProfKeepAlvResp = _TmnxWlanGwMgwProfKeepAlvResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 9),
    _TmnxWlanGwMgwProfKeepAlvResp_Type()
)
tmnxWlanGwMgwProfKeepAlvResp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvResp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfKeepAlvResp.setUnits("seconds")


class _TmnxWlanGwMgwProfTtl_Type(TmnxMobProfIpTtl):
    """Custom type tmnxWlanGwMgwProfTtl based on TmnxMobProfIpTtl"""
    defaultValue = 255


_TmnxWlanGwMgwProfTtl_Type.__name__ = "TmnxMobProfIpTtl"
_TmnxWlanGwMgwProfTtl_Object = MibTableColumn
tmnxWlanGwMgwProfTtl = _TmnxWlanGwMgwProfTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 10),
    _TmnxWlanGwMgwProfTtl_Type()
)
tmnxWlanGwMgwProfTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTtl.setUnits("hops")


class _TmnxWlanGwMgwProfInterfaceType_Type(TmnxWlanGwMgwInterfaceType):
    """Custom type tmnxWlanGwMgwProfInterfaceType based on TmnxWlanGwMgwInterfaceType"""
    defaultValue = 2


_TmnxWlanGwMgwProfInterfaceType_Type.__name__ = "TmnxWlanGwMgwInterfaceType"
_TmnxWlanGwMgwProfInterfaceType_Object = MibTableColumn
tmnxWlanGwMgwProfInterfaceType = _TmnxWlanGwMgwProfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 12),
    _TmnxWlanGwMgwProfInterfaceType_Type()
)
tmnxWlanGwMgwProfInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfInterfaceType.setStatus("current")


class _TmnxWlanGwMgwProfChrgCharHome_Type(TmnxWlanGwChargingCharBits):
    """Custom type tmnxWlanGwMgwProfChrgCharHome based on TmnxWlanGwChargingCharBits"""
    defaultHexValue = "00"


_TmnxWlanGwMgwProfChrgCharHome_Type.__name__ = "TmnxWlanGwChargingCharBits"
_TmnxWlanGwMgwProfChrgCharHome_Object = MibTableColumn
tmnxWlanGwMgwProfChrgCharHome = _TmnxWlanGwMgwProfChrgCharHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 15),
    _TmnxWlanGwMgwProfChrgCharHome_Type()
)
tmnxWlanGwMgwProfChrgCharHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfChrgCharHome.setStatus("current")


class _TmnxWlanGwMgwProfChrgCharRoam_Type(TmnxWlanGwChargingCharBits):
    """Custom type tmnxWlanGwMgwProfChrgCharRoam based on TmnxWlanGwChargingCharBits"""
    defaultHexValue = "00"


_TmnxWlanGwMgwProfChrgCharRoam_Type.__name__ = "TmnxWlanGwChargingCharBits"
_TmnxWlanGwMgwProfChrgCharRoam_Object = MibTableColumn
tmnxWlanGwMgwProfChrgCharRoam = _TmnxWlanGwMgwProfChrgCharRoam_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 16),
    _TmnxWlanGwMgwProfChrgCharRoam_Type()
)
tmnxWlanGwMgwProfChrgCharRoam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfChrgCharRoam.setStatus("current")


class _TmnxWlanGwMgwProfSeHoldTime_Type(Integer32):
    """Custom type tmnxWlanGwMgwProfSeHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 3600),
    )


_TmnxWlanGwMgwProfSeHoldTime_Type.__name__ = "Integer32"
_TmnxWlanGwMgwProfSeHoldTime_Object = MibTableColumn
tmnxWlanGwMgwProfSeHoldTime = _TmnxWlanGwMgwProfSeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 20),
    _TmnxWlanGwMgwProfSeHoldTime_Type()
)
tmnxWlanGwMgwProfSeHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfSeHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfSeHoldTime.setUnits("seconds")


class _TmnxWlanGwMgwProfReportWlanLoc_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwMgwProfReportWlanLoc based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwMgwProfReportWlanLoc_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwMgwProfReportWlanLoc_Object = MibTableColumn
tmnxWlanGwMgwProfReportWlanLoc = _TmnxWlanGwMgwProfReportWlanLoc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 21),
    _TmnxWlanGwMgwProfReportWlanLoc_Type()
)
tmnxWlanGwMgwProfReportWlanLoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfReportWlanLoc.setStatus("current")


class _TmnxWlanGwMgwProfProtocolCfgOpt_Type(Integer32):
    """Custom type tmnxWlanGwMgwProfProtocolCfgOpt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pco", 1),
          ("apco", 2))
    )


_TmnxWlanGwMgwProfProtocolCfgOpt_Type.__name__ = "Integer32"
_TmnxWlanGwMgwProfProtocolCfgOpt_Object = MibTableColumn
tmnxWlanGwMgwProfProtocolCfgOpt = _TmnxWlanGwMgwProfProtocolCfgOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 1, 1, 22),
    _TmnxWlanGwMgwProfProtocolCfgOpt_Type()
)
tmnxWlanGwMgwProfProtocolCfgOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfProtocolCfgOpt.setStatus("current")
_TmnxWlanGwMgwAddrTable_Object = MibTable
tmnxWlanGwMgwAddrTable = _TmnxWlanGwMgwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrTable.setStatus("current")
_TmnxWlanGwMgwAddrEntry_Object = MibTableRow
tmnxWlanGwMgwAddrEntry = _TmnxWlanGwMgwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1)
)
tmnxWlanGwMgwAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrEntry.setStatus("current")
_TmnxWlanGwMgwAddrType_Type = InetAddressType
_TmnxWlanGwMgwAddrType_Object = MibTableColumn
tmnxWlanGwMgwAddrType = _TmnxWlanGwMgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 1),
    _TmnxWlanGwMgwAddrType_Type()
)
tmnxWlanGwMgwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrType.setStatus("current")


class _TmnxWlanGwMgwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwAddr_Object = MibTableColumn
tmnxWlanGwMgwAddr = _TmnxWlanGwMgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 2),
    _TmnxWlanGwMgwAddr_Type()
)
tmnxWlanGwMgwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddr.setStatus("current")


class _TmnxWlanGwMgwAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwMgwAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxWlanGwMgwAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwMgwAddrPrefixLen_Object = MibTableColumn
tmnxWlanGwMgwAddrPrefixLen = _TmnxWlanGwMgwAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 3),
    _TmnxWlanGwMgwAddrPrefixLen_Type()
)
tmnxWlanGwMgwAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrPrefixLen.setStatus("current")
_TmnxWlanGwMgwAddrRowStatus_Type = RowStatus
_TmnxWlanGwMgwAddrRowStatus_Object = MibTableColumn
tmnxWlanGwMgwAddrRowStatus = _TmnxWlanGwMgwAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 4),
    _TmnxWlanGwMgwAddrRowStatus_Type()
)
tmnxWlanGwMgwAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrRowStatus.setStatus("current")
_TmnxWlanGwMgwAddrLastMgmtChange_Type = TimeStamp
_TmnxWlanGwMgwAddrLastMgmtChange_Object = MibTableColumn
tmnxWlanGwMgwAddrLastMgmtChange = _TmnxWlanGwMgwAddrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 5),
    _TmnxWlanGwMgwAddrLastMgmtChange_Type()
)
tmnxWlanGwMgwAddrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrLastMgmtChange.setStatus("current")
_TmnxWlanGwMgwAddrProfile_Type = TNamedItem
_TmnxWlanGwMgwAddrProfile_Object = MibTableColumn
tmnxWlanGwMgwAddrProfile = _TmnxWlanGwMgwAddrProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 2, 1, 6),
    _TmnxWlanGwMgwAddrProfile_Type()
)
tmnxWlanGwMgwAddrProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrProfile.setStatus("current")
_TmnxWlanGwMgwTable_Object = MibTable
tmnxWlanGwMgwTable = _TmnxWlanGwMgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwTable.setStatus("current")
_TmnxWlanGwMgwEntry_Object = MibTableRow
tmnxWlanGwMgwEntry = _TmnxWlanGwMgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1)
)
tmnxWlanGwMgwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemotePort"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwEntry.setStatus("current")
_TmnxWlanGwMgwRemoteAddrType_Type = InetAddressType
_TmnxWlanGwMgwRemoteAddrType_Object = MibTableColumn
tmnxWlanGwMgwRemoteAddrType = _TmnxWlanGwMgwRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 1),
    _TmnxWlanGwMgwRemoteAddrType_Type()
)
tmnxWlanGwMgwRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRemoteAddrType.setStatus("current")


class _TmnxWlanGwMgwRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwRemoteAddr_Object = MibTableColumn
tmnxWlanGwMgwRemoteAddr = _TmnxWlanGwMgwRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 2),
    _TmnxWlanGwMgwRemoteAddr_Type()
)
tmnxWlanGwMgwRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRemoteAddr.setStatus("current")
_TmnxWlanGwMgwRemotePort_Type = InetPortNumber
_TmnxWlanGwMgwRemotePort_Object = MibTableColumn
tmnxWlanGwMgwRemotePort = _TmnxWlanGwMgwRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 3),
    _TmnxWlanGwMgwRemotePort_Type()
)
tmnxWlanGwMgwRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRemotePort.setStatus("current")
_TmnxWlanGwMgwLocalAddrType_Type = InetAddressType
_TmnxWlanGwMgwLocalAddrType_Object = MibTableColumn
tmnxWlanGwMgwLocalAddrType = _TmnxWlanGwMgwLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 4),
    _TmnxWlanGwMgwLocalAddrType_Type()
)
tmnxWlanGwMgwLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwLocalAddrType.setStatus("current")


class _TmnxWlanGwMgwLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwLocalAddr_Object = MibTableColumn
tmnxWlanGwMgwLocalAddr = _TmnxWlanGwMgwLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 5),
    _TmnxWlanGwMgwLocalAddr_Type()
)
tmnxWlanGwMgwLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwLocalAddr.setStatus("current")


class _TmnxWlanGwMgwTime_Type(DateAndTime):
    """Custom type tmnxWlanGwMgwTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwMgwTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwMgwTime_Object = MibTableColumn
tmnxWlanGwMgwTime = _TmnxWlanGwMgwTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 6),
    _TmnxWlanGwMgwTime_Type()
)
tmnxWlanGwMgwTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwTime.setStatus("current")
_TmnxWlanGwMgwProfile_Type = TNamedItemOrEmpty
_TmnxWlanGwMgwProfile_Object = MibTableColumn
tmnxWlanGwMgwProfile = _TmnxWlanGwMgwProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 7),
    _TmnxWlanGwMgwProfile_Type()
)
tmnxWlanGwMgwProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfile.setStatus("current")


class _TmnxWlanGwMgwControl_Type(Integer32):
    """Custom type tmnxWlanGwMgwControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gtpv1C", 1),
          ("gtpv2C", 2))
    )


_TmnxWlanGwMgwControl_Type.__name__ = "Integer32"
_TmnxWlanGwMgwControl_Object = MibTableColumn
tmnxWlanGwMgwControl = _TmnxWlanGwMgwControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 8),
    _TmnxWlanGwMgwControl_Type()
)
tmnxWlanGwMgwControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwControl.setStatus("current")
_TmnxWlanGwMgwRestartCnt_Type = Gauge32
_TmnxWlanGwMgwRestartCnt_Object = MibTableColumn
tmnxWlanGwMgwRestartCnt = _TmnxWlanGwMgwRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 9),
    _TmnxWlanGwMgwRestartCnt_Type()
)
tmnxWlanGwMgwRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRestartCnt.setStatus("current")
_TmnxWlanGwMgwState_Type = TmnxMobPathMgmtState
_TmnxWlanGwMgwState_Object = MibTableColumn
tmnxWlanGwMgwState = _TmnxWlanGwMgwState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 10),
    _TmnxWlanGwMgwState_Type()
)
tmnxWlanGwMgwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwState.setStatus("current")
_TmnxWlanGwMgwInterfaceType_Type = TmnxWlanGwMgwInterfaceType
_TmnxWlanGwMgwInterfaceType_Object = MibTableColumn
tmnxWlanGwMgwInterfaceType = _TmnxWlanGwMgwInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 3, 1, 11),
    _TmnxWlanGwMgwInterfaceType_Type()
)
tmnxWlanGwMgwInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwInterfaceType.setStatus("current")
_TmnxWlanMgwStatsTable_Object = MibTable
tmnxWlanMgwStatsTable = _TmnxWlanMgwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsTable.setStatus("current")
_TmnxWlanMgwStatsEntry_Object = MibTableRow
tmnxWlanMgwStatsEntry = _TmnxWlanMgwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1)
)
tmnxWlanMgwStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemoteAddr"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRemotePort"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsId"),
)
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsEntry.setStatus("current")


class _TmnxWlanMgwStatsId_Type(Unsigned32):
    """Custom type tmnxWlanMgwStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44),
    )


_TmnxWlanMgwStatsId_Type.__name__ = "Unsigned32"
_TmnxWlanMgwStatsId_Object = MibTableColumn
tmnxWlanMgwStatsId = _TmnxWlanMgwStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 1),
    _TmnxWlanMgwStatsId_Type()
)
tmnxWlanMgwStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsId.setStatus("current")


class _TmnxWlanMgwStatsName_Type(DisplayString):
    """Custom type tmnxWlanMgwStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxWlanMgwStatsName_Type.__name__ = "DisplayString"
_TmnxWlanMgwStatsName_Object = MibTableColumn
tmnxWlanMgwStatsName = _TmnxWlanMgwStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 2),
    _TmnxWlanMgwStatsName_Type()
)
tmnxWlanMgwStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsName.setStatus("current")
_TmnxWlanMgwStatsVal_Type = Counter64
_TmnxWlanMgwStatsVal_Object = MibTableColumn
tmnxWlanMgwStatsVal = _TmnxWlanMgwStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 3),
    _TmnxWlanMgwStatsVal_Type()
)
tmnxWlanMgwStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsVal.setStatus("current")
_TmnxWlanMgwStatsValLw_Type = Counter32
_TmnxWlanMgwStatsValLw_Object = MibTableColumn
tmnxWlanMgwStatsValLw = _TmnxWlanMgwStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 4),
    _TmnxWlanMgwStatsValLw_Type()
)
tmnxWlanMgwStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsValLw.setStatus("current")
_TmnxWlanMgwStatsValHw_Type = Counter32
_TmnxWlanMgwStatsValHw_Object = MibTableColumn
tmnxWlanMgwStatsValHw = _TmnxWlanMgwStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 4, 1, 5),
    _TmnxWlanMgwStatsValHw_Type()
)
tmnxWlanMgwStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanMgwStatsValHw.setStatus("current")
_TmnxWlanGwGtpSeTable_Object = MibTable
tmnxWlanGwGtpSeTable = _TmnxWlanGwGtpSeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeTable.setStatus("current")
_TmnxWlanGwGtpSeEntry_Object = MibTableRow
tmnxWlanGwGtpSeEntry = _TmnxWlanGwGtpSeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1)
)
tmnxWlanGwGtpSeEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeImsi"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeApn"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeEntry.setStatus("current")


class _TmnxWlanGwGtpSeImsi_Type(TmnxMobImsiStr):
    """Custom type tmnxWlanGwGtpSeImsi based on TmnxMobImsiStr"""
    subtypeSpec = TmnxMobImsiStr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 15),
    )


_TmnxWlanGwGtpSeImsi_Type.__name__ = "TmnxMobImsiStr"
_TmnxWlanGwGtpSeImsi_Object = MibTableColumn
tmnxWlanGwGtpSeImsi = _TmnxWlanGwGtpSeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 1),
    _TmnxWlanGwGtpSeImsi_Type()
)
tmnxWlanGwGtpSeImsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeImsi.setStatus("current")
_TmnxWlanGwGtpSeApn_Type = TmnxMobApn
_TmnxWlanGwGtpSeApn_Object = MibTableColumn
tmnxWlanGwGtpSeApn = _TmnxWlanGwGtpSeApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 2),
    _TmnxWlanGwGtpSeApn_Type()
)
tmnxWlanGwGtpSeApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeApn.setStatus("current")
_TmnxWlanGwGtpSeMgwRouter_Type = TmnxVRtrIDOrZero
_TmnxWlanGwGtpSeMgwRouter_Object = MibTableColumn
tmnxWlanGwGtpSeMgwRouter = _TmnxWlanGwGtpSeMgwRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 3),
    _TmnxWlanGwGtpSeMgwRouter_Type()
)
tmnxWlanGwGtpSeMgwRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeMgwRouter.setStatus("current")
_TmnxWlanGwGtpSeMgwAddrType_Type = InetAddressType
_TmnxWlanGwGtpSeMgwAddrType_Object = MibTableColumn
tmnxWlanGwGtpSeMgwAddrType = _TmnxWlanGwGtpSeMgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 4),
    _TmnxWlanGwGtpSeMgwAddrType_Type()
)
tmnxWlanGwGtpSeMgwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeMgwAddrType.setStatus("current")


class _TmnxWlanGwGtpSeMgwAddr_Type(InetAddress):
    """Custom type tmnxWlanGwGtpSeMgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwGtpSeMgwAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwGtpSeMgwAddr_Object = MibTableColumn
tmnxWlanGwGtpSeMgwAddr = _TmnxWlanGwGtpSeMgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 5),
    _TmnxWlanGwGtpSeMgwAddr_Type()
)
tmnxWlanGwGtpSeMgwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeMgwAddr.setStatus("current")
_TmnxWlanGwGtpSeRemoteCtrlTeid_Type = Unsigned32
_TmnxWlanGwGtpSeRemoteCtrlTeid_Object = MibTableColumn
tmnxWlanGwGtpSeRemoteCtrlTeid = _TmnxWlanGwGtpSeRemoteCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 6),
    _TmnxWlanGwGtpSeRemoteCtrlTeid_Type()
)
tmnxWlanGwGtpSeRemoteCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeRemoteCtrlTeid.setStatus("current")
_TmnxWlanGwGtpSeLocalCtrlTeid_Type = Unsigned32
_TmnxWlanGwGtpSeLocalCtrlTeid_Object = MibTableColumn
tmnxWlanGwGtpSeLocalCtrlTeid = _TmnxWlanGwGtpSeLocalCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 7),
    _TmnxWlanGwGtpSeLocalCtrlTeid_Type()
)
tmnxWlanGwGtpSeLocalCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeLocalCtrlTeid.setStatus("current")
_TmnxWlanGwGtpSeChrgChar_Type = TmnxWlanGwChargingCharBits
_TmnxWlanGwGtpSeChrgChar_Object = MibTableColumn
tmnxWlanGwGtpSeChrgChar = _TmnxWlanGwGtpSeChrgChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 5, 1, 10),
    _TmnxWlanGwGtpSeChrgChar_Type()
)
tmnxWlanGwGtpSeChrgChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpSeChrgChar.setStatus("current")
_TmnxWlanGwBcTable_Object = MibTable
tmnxWlanGwBcTable = _TmnxWlanGwBcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6)
)
if mibBuilder.loadTexts:
    tmnxWlanGwBcTable.setStatus("current")
_TmnxWlanGwBcEntry_Object = MibTableRow
tmnxWlanGwBcEntry = _TmnxWlanGwBcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1)
)
tmnxWlanGwBcEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeImsi"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwBcEntry.setStatus("current")
_TmnxWlanGwBcId_Type = TmnxMobBearerId
_TmnxWlanGwBcId_Object = MibTableColumn
tmnxWlanGwBcId = _TmnxWlanGwBcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 1),
    _TmnxWlanGwBcId_Type()
)
tmnxWlanGwBcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwBcId.setStatus("current")
_TmnxWlanGwBcRemoteTeid_Type = Unsigned32
_TmnxWlanGwBcRemoteTeid_Object = MibTableColumn
tmnxWlanGwBcRemoteTeid = _TmnxWlanGwBcRemoteTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 2),
    _TmnxWlanGwBcRemoteTeid_Type()
)
tmnxWlanGwBcRemoteTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcRemoteTeid.setStatus("current")
_TmnxWlanGwBcLocalTeid_Type = Unsigned32
_TmnxWlanGwBcLocalTeid_Object = MibTableColumn
tmnxWlanGwBcLocalTeid = _TmnxWlanGwBcLocalTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 3),
    _TmnxWlanGwBcLocalTeid_Type()
)
tmnxWlanGwBcLocalTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcLocalTeid.setStatus("current")
_TmnxWlanGwBcQosUlGbr_Type = Unsigned32
_TmnxWlanGwBcQosUlGbr_Object = MibTableColumn
tmnxWlanGwBcQosUlGbr = _TmnxWlanGwBcQosUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 10),
    _TmnxWlanGwBcQosUlGbr_Type()
)
tmnxWlanGwBcQosUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlGbr.setUnits("Kbps")
_TmnxWlanGwBcQosUlMbr_Type = Unsigned32
_TmnxWlanGwBcQosUlMbr_Object = MibTableColumn
tmnxWlanGwBcQosUlMbr = _TmnxWlanGwBcQosUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 11),
    _TmnxWlanGwBcQosUlMbr_Type()
)
tmnxWlanGwBcQosUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosUlMbr.setUnits("Kbps")
_TmnxWlanGwBcQosDlGbr_Type = Unsigned32
_TmnxWlanGwBcQosDlGbr_Object = MibTableColumn
tmnxWlanGwBcQosDlGbr = _TmnxWlanGwBcQosDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 12),
    _TmnxWlanGwBcQosDlGbr_Type()
)
tmnxWlanGwBcQosDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlGbr.setUnits("Kbps")
_TmnxWlanGwBcQosDlMbr_Type = Unsigned32
_TmnxWlanGwBcQosDlMbr_Object = MibTableColumn
tmnxWlanGwBcQosDlMbr = _TmnxWlanGwBcQosDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 13),
    _TmnxWlanGwBcQosDlMbr_Type()
)
tmnxWlanGwBcQosDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosDlMbr.setUnits("Kbps")
_TmnxWlanGwBcQosQci_Type = TmnxMobQci
_TmnxWlanGwBcQosQci_Object = MibTableColumn
tmnxWlanGwBcQosQci = _TmnxWlanGwBcQosQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 14),
    _TmnxWlanGwBcQosQci_Type()
)
tmnxWlanGwBcQosQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosQci.setStatus("current")
_TmnxWlanGwBcQosArp_Type = TmnxMobArp
_TmnxWlanGwBcQosArp_Object = MibTableColumn
tmnxWlanGwBcQosArp = _TmnxWlanGwBcQosArp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 6, 1, 15),
    _TmnxWlanGwBcQosArp_Type()
)
tmnxWlanGwBcQosArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwBcQosArp.setStatus("current")
_TmnxWlanGwMgwCacheTable_Object = MibTable
tmnxWlanGwMgwCacheTable = _TmnxWlanGwMgwCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheTable.setStatus("obsolete")
_TmnxWlanGwMgwCacheEntry_Object = MibTableRow
tmnxWlanGwMgwCacheEntry = _TmnxWlanGwMgwCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1)
)
tmnxWlanGwMgwCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheAddrType"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheAddr"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheEntry.setStatus("obsolete")
_TmnxWlanGwMgwCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwCacheApn_Object = MibTableColumn
tmnxWlanGwMgwCacheApn = _TmnxWlanGwMgwCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 1),
    _TmnxWlanGwMgwCacheApn_Type()
)
tmnxWlanGwMgwCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheApn.setStatus("obsolete")
_TmnxWlanGwMgwCacheAddrType_Type = InetAddressType
_TmnxWlanGwMgwCacheAddrType_Object = MibTableColumn
tmnxWlanGwMgwCacheAddrType = _TmnxWlanGwMgwCacheAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 2),
    _TmnxWlanGwMgwCacheAddrType_Type()
)
tmnxWlanGwMgwCacheAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheAddrType.setStatus("obsolete")


class _TmnxWlanGwMgwCacheAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwCacheAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwCacheAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwCacheAddr_Object = MibTableColumn
tmnxWlanGwMgwCacheAddr = _TmnxWlanGwMgwCacheAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 3),
    _TmnxWlanGwMgwCacheAddr_Type()
)
tmnxWlanGwMgwCacheAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheAddr.setStatus("obsolete")
_TmnxWlanGwMgwCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwCacheTtl = _TmnxWlanGwMgwCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 7, 1, 4),
    _TmnxWlanGwMgwCacheTtl_Type()
)
tmnxWlanGwMgwCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheTtl.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwCacheTtl.setUnits("seconds")
_TmnxWlanGwGtpStatsTable_Object = MibTable
tmnxWlanGwGtpStatsTable = _TmnxWlanGwGtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsTable.setStatus("current")
_TmnxWlanGwGtpStatsEntry_Object = MibTableRow
tmnxWlanGwGtpStatsEntry = _TmnxWlanGwGtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1)
)
tmnxWlanGwGtpStatsEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsEntry.setStatus("current")


class _TmnxWlanGwGtpStatsId_Type(Unsigned32):
    """Custom type tmnxWlanGwGtpStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 71),
    )


_TmnxWlanGwGtpStatsId_Type.__name__ = "Unsigned32"
_TmnxWlanGwGtpStatsId_Object = MibTableColumn
tmnxWlanGwGtpStatsId = _TmnxWlanGwGtpStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 1),
    _TmnxWlanGwGtpStatsId_Type()
)
tmnxWlanGwGtpStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsId.setStatus("current")


class _TmnxWlanGwGtpStatsName_Type(DisplayString):
    """Custom type tmnxWlanGwGtpStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 56),
    )


_TmnxWlanGwGtpStatsName_Type.__name__ = "DisplayString"
_TmnxWlanGwGtpStatsName_Object = MibTableColumn
tmnxWlanGwGtpStatsName = _TmnxWlanGwGtpStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 2),
    _TmnxWlanGwGtpStatsName_Type()
)
tmnxWlanGwGtpStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsName.setStatus("current")
_TmnxWlanGwGtpStatsVal_Type = Counter64
_TmnxWlanGwGtpStatsVal_Object = MibTableColumn
tmnxWlanGwGtpStatsVal = _TmnxWlanGwGtpStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 3),
    _TmnxWlanGwGtpStatsVal_Type()
)
tmnxWlanGwGtpStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsVal.setStatus("current")
_TmnxWlanGwGtpStatsValLw_Type = Counter32
_TmnxWlanGwGtpStatsValLw_Object = MibTableColumn
tmnxWlanGwGtpStatsValLw = _TmnxWlanGwGtpStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 4),
    _TmnxWlanGwGtpStatsValLw_Type()
)
tmnxWlanGwGtpStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsValLw.setStatus("current")
_TmnxWlanGwGtpStatsValHw_Type = Counter32
_TmnxWlanGwGtpStatsValHw_Object = MibTableColumn
tmnxWlanGwGtpStatsValHw = _TmnxWlanGwGtpStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 8, 1, 5),
    _TmnxWlanGwGtpStatsValHw_Type()
)
tmnxWlanGwGtpStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGtpStatsValHw.setStatus("current")
_TmnxWlanGwMgwArecCacheTable_Object = MibTable
tmnxWlanGwMgwArecCacheTable = _TmnxWlanGwMgwArecCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheTable.setStatus("current")
_TmnxWlanGwMgwArecCacheEntry_Object = MibTableRow
tmnxWlanGwMgwArecCacheEntry = _TmnxWlanGwMgwArecCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1)
)
tmnxWlanGwMgwArecCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheEntry.setStatus("current")
_TmnxWlanGwMgwArecCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwArecCacheApn_Object = MibTableColumn
tmnxWlanGwMgwArecCacheApn = _TmnxWlanGwMgwArecCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 1),
    _TmnxWlanGwMgwArecCacheApn_Type()
)
tmnxWlanGwMgwArecCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheApn.setStatus("current")
_TmnxWlanGwMgwArecCacheIndex_Type = Unsigned32
_TmnxWlanGwMgwArecCacheIndex_Object = MibTableColumn
tmnxWlanGwMgwArecCacheIndex = _TmnxWlanGwMgwArecCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 2),
    _TmnxWlanGwMgwArecCacheIndex_Type()
)
tmnxWlanGwMgwArecCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheIndex.setStatus("current")
_TmnxWlanGwMgwArecCacheAddrType_Type = InetAddressType
_TmnxWlanGwMgwArecCacheAddrType_Object = MibTableColumn
tmnxWlanGwMgwArecCacheAddrType = _TmnxWlanGwMgwArecCacheAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 3),
    _TmnxWlanGwMgwArecCacheAddrType_Type()
)
tmnxWlanGwMgwArecCacheAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheAddrType.setStatus("current")


class _TmnxWlanGwMgwArecCacheAddr_Type(InetAddress):
    """Custom type tmnxWlanGwMgwArecCacheAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwMgwArecCacheAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwMgwArecCacheAddr_Object = MibTableColumn
tmnxWlanGwMgwArecCacheAddr = _TmnxWlanGwMgwArecCacheAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 4),
    _TmnxWlanGwMgwArecCacheAddr_Type()
)
tmnxWlanGwMgwArecCacheAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheAddr.setStatus("current")
_TmnxWlanGwMgwArecCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwArecCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwArecCacheTtl = _TmnxWlanGwMgwArecCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 10, 1, 5),
    _TmnxWlanGwMgwArecCacheTtl_Type()
)
tmnxWlanGwMgwArecCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwArecCacheTtl.setUnits("seconds")
_TmnxWlanGwMgwSnaptrCacheTable_Object = MibTable
tmnxWlanGwMgwSnaptrCacheTable = _TmnxWlanGwMgwSnaptrCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheTable.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheEntry_Object = MibTableRow
tmnxWlanGwMgwSnaptrCacheEntry = _TmnxWlanGwMgwSnaptrCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1)
)
tmnxWlanGwMgwSnaptrCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheOrder"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheEntry.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSnaptrCacheApn_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheApn = _TmnxWlanGwMgwSnaptrCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 1),
    _TmnxWlanGwMgwSnaptrCacheApn_Type()
)
tmnxWlanGwMgwSnaptrCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheApn.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheOrder_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCacheOrder_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheOrder = _TmnxWlanGwMgwSnaptrCacheOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 2),
    _TmnxWlanGwMgwSnaptrCacheOrder_Type()
)
tmnxWlanGwMgwSnaptrCacheOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheOrder.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheIndex_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCacheIndex_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheIndex = _TmnxWlanGwMgwSnaptrCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 3),
    _TmnxWlanGwMgwSnaptrCacheIndex_Type()
)
tmnxWlanGwMgwSnaptrCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheIndex.setStatus("current")
_TmnxWlanGwMgwSnaptrCachePref_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCachePref_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCachePref = _TmnxWlanGwMgwSnaptrCachePref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 4),
    _TmnxWlanGwMgwSnaptrCachePref_Type()
)
tmnxWlanGwMgwSnaptrCachePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCachePref.setStatus("current")


class _TmnxWlanGwMgwSnaptrCacheService_Type(TmnxMobService):
    """Custom type tmnxWlanGwMgwSnaptrCacheService based on TmnxMobService"""
    subtypeSpec = TmnxMobService.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_TmnxWlanGwMgwSnaptrCacheService_Type.__name__ = "TmnxMobService"
_TmnxWlanGwMgwSnaptrCacheService_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheService = _TmnxWlanGwMgwSnaptrCacheService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 5),
    _TmnxWlanGwMgwSnaptrCacheService_Type()
)
tmnxWlanGwMgwSnaptrCacheService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheService.setStatus("current")


class _TmnxWlanGwMgwSnaptrCacheNext_Type(Integer32):
    """Custom type tmnxWlanGwMgwSnaptrCacheNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dnsSrv", 1),
          ("dnsA", 2),
          ("dnsNaptr", 3))
    )


_TmnxWlanGwMgwSnaptrCacheNext_Type.__name__ = "Integer32"
_TmnxWlanGwMgwSnaptrCacheNext_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheNext = _TmnxWlanGwMgwSnaptrCacheNext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 6),
    _TmnxWlanGwMgwSnaptrCacheNext_Type()
)
tmnxWlanGwMgwSnaptrCacheNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheNext.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheRepl_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSnaptrCacheRepl_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheRepl = _TmnxWlanGwMgwSnaptrCacheRepl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 7),
    _TmnxWlanGwMgwSnaptrCacheRepl_Type()
)
tmnxWlanGwMgwSnaptrCacheRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheRepl.setStatus("current")
_TmnxWlanGwMgwSnaptrCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwSnaptrCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwSnaptrCacheTtl = _TmnxWlanGwMgwSnaptrCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 11, 1, 8),
    _TmnxWlanGwMgwSnaptrCacheTtl_Type()
)
tmnxWlanGwMgwSnaptrCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSnaptrCacheTtl.setUnits("seconds")
_TmnxWlanGwMgwSrvCacheTable_Object = MibTable
tmnxWlanGwMgwSrvCacheTable = _TmnxWlanGwMgwSrvCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12)
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTable.setStatus("current")
_TmnxWlanGwMgwSrvCacheEntry_Object = MibTableRow
tmnxWlanGwMgwSrvCacheEntry = _TmnxWlanGwMgwSrvCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1)
)
tmnxWlanGwMgwSrvCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheApn"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCachePriority"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheIndex"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheEntry.setStatus("current")
_TmnxWlanGwMgwSrvCacheApn_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSrvCacheApn_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheApn = _TmnxWlanGwMgwSrvCacheApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 1),
    _TmnxWlanGwMgwSrvCacheApn_Type()
)
tmnxWlanGwMgwSrvCacheApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheApn.setStatus("current")


class _TmnxWlanGwMgwSrvCachePriority_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwSrvCachePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxWlanGwMgwSrvCachePriority_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwSrvCachePriority_Object = MibTableColumn
tmnxWlanGwMgwSrvCachePriority = _TmnxWlanGwMgwSrvCachePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 2),
    _TmnxWlanGwMgwSrvCachePriority_Type()
)
tmnxWlanGwMgwSrvCachePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCachePriority.setStatus("current")
_TmnxWlanGwMgwSrvCacheIndex_Type = Unsigned32
_TmnxWlanGwMgwSrvCacheIndex_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheIndex = _TmnxWlanGwMgwSrvCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 3),
    _TmnxWlanGwMgwSrvCacheIndex_Type()
)
tmnxWlanGwMgwSrvCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheIndex.setStatus("current")


class _TmnxWlanGwMgwSrvCacheWeight_Type(Unsigned32):
    """Custom type tmnxWlanGwMgwSrvCacheWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxWlanGwMgwSrvCacheWeight_Type.__name__ = "Unsigned32"
_TmnxWlanGwMgwSrvCacheWeight_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheWeight = _TmnxWlanGwMgwSrvCacheWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 4),
    _TmnxWlanGwMgwSrvCacheWeight_Type()
)
tmnxWlanGwMgwSrvCacheWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheWeight.setStatus("current")
_TmnxWlanGwMgwSrvCachePort_Type = InetPortNumber
_TmnxWlanGwMgwSrvCachePort_Object = MibTableColumn
tmnxWlanGwMgwSrvCachePort = _TmnxWlanGwMgwSrvCachePort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 5),
    _TmnxWlanGwMgwSrvCachePort_Type()
)
tmnxWlanGwMgwSrvCachePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCachePort.setStatus("current")
_TmnxWlanGwMgwSrvCacheTarget_Type = TmnxMobApnDomainName
_TmnxWlanGwMgwSrvCacheTarget_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheTarget = _TmnxWlanGwMgwSrvCacheTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 6),
    _TmnxWlanGwMgwSrvCacheTarget_Type()
)
tmnxWlanGwMgwSrvCacheTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTarget.setStatus("current")
_TmnxWlanGwMgwSrvCacheTtl_Type = Unsigned32
_TmnxWlanGwMgwSrvCacheTtl_Object = MibTableColumn
tmnxWlanGwMgwSrvCacheTtl = _TmnxWlanGwMgwSrvCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 12, 1, 7),
    _TmnxWlanGwMgwSrvCacheTtl_Type()
)
tmnxWlanGwMgwSrvCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSrvCacheTtl.setUnits("seconds")
_TmnxWlanGwPgwTable_Object = MibTable
tmnxWlanGwPgwTable = _TmnxWlanGwPgwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20)
)
if mibBuilder.loadTexts:
    tmnxWlanGwPgwTable.setStatus("current")
_TmnxWlanGwPgwEntry_Object = MibTableRow
tmnxWlanGwPgwEntry = _TmnxWlanGwPgwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwPgwEntry.setStatus("current")
_TmnxWlanGwPgwLastChanged_Type = TimeStamp
_TmnxWlanGwPgwLastChanged_Object = MibTableColumn
tmnxWlanGwPgwLastChanged = _TmnxWlanGwPgwLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 1),
    _TmnxWlanGwPgwLastChanged_Type()
)
tmnxWlanGwPgwLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwLastChanged.setStatus("current")


class _TmnxWlanGwPgwQosUplinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwPgwQosUplinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosUplinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwPgwQosUplinkGbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosUplinkGbrRate = _TmnxWlanGwPgwQosUplinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 2),
    _TmnxWlanGwPgwQosUplinkGbrRate_Type()
)
tmnxWlanGwPgwQosUplinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkGbrRate.setUnits("Kbps")


class _TmnxWlanGwPgwQosUplinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwPgwQosUplinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosUplinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwPgwQosUplinkMbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosUplinkMbrRate = _TmnxWlanGwPgwQosUplinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 3),
    _TmnxWlanGwPgwQosUplinkMbrRate_Type()
)
tmnxWlanGwPgwQosUplinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosUplinkMbrRate.setUnits("Kbps")


class _TmnxWlanGwPgwQosDwnlinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwPgwQosDwnlinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosDwnlinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwPgwQosDwnlinkGbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosDwnlinkGbrRate = _TmnxWlanGwPgwQosDwnlinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 4),
    _TmnxWlanGwPgwQosDwnlinkGbrRate_Type()
)
tmnxWlanGwPgwQosDwnlinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkGbrRate.setUnits("Kbps")


class _TmnxWlanGwPgwQosDwnlinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwPgwQosDwnlinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxWlanGwPgwQosDwnlinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwPgwQosDwnlinkMbrRate_Object = MibTableColumn
tmnxWlanGwPgwQosDwnlinkMbrRate = _TmnxWlanGwPgwQosDwnlinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 5),
    _TmnxWlanGwPgwQosDwnlinkMbrRate_Type()
)
tmnxWlanGwPgwQosDwnlinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosDwnlinkMbrRate.setUnits("Kbps")


class _TmnxWlanGwPgwQosArpValue_Type(TmnxMobArpValue):
    """Custom type tmnxWlanGwPgwQosArpValue based on TmnxMobArpValue"""
    defaultValue = 1


_TmnxWlanGwPgwQosArpValue_Type.__name__ = "TmnxMobArpValue"
_TmnxWlanGwPgwQosArpValue_Object = MibTableColumn
tmnxWlanGwPgwQosArpValue = _TmnxWlanGwPgwQosArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 6),
    _TmnxWlanGwPgwQosArpValue_Type()
)
tmnxWlanGwPgwQosArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosArpValue.setStatus("current")


class _TmnxWlanGwPgwQosQciValue_Type(TmnxMobQci):
    """Custom type tmnxWlanGwPgwQosQciValue based on TmnxMobQci"""
    defaultValue = 8


_TmnxWlanGwPgwQosQciValue_Type.__name__ = "TmnxMobQci"
_TmnxWlanGwPgwQosQciValue_Object = MibTableColumn
tmnxWlanGwPgwQosQciValue = _TmnxWlanGwPgwQosQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 20, 1, 7),
    _TmnxWlanGwPgwQosQciValue_Type()
)
tmnxWlanGwPgwQosQciValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwQosQciValue.setStatus("current")
_TmnxWlanGwGgsnTable_Object = MibTable
tmnxWlanGwGgsnTable = _TmnxWlanGwGgsnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnTable.setStatus("current")
_TmnxWlanGwGgsnEntry_Object = MibTableRow
tmnxWlanGwGgsnEntry = _TmnxWlanGwGgsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnEntry.setStatus("current")
_TmnxWlanGwGgsnLastChanged_Type = TimeStamp
_TmnxWlanGwGgsnLastChanged_Object = MibTableColumn
tmnxWlanGwGgsnLastChanged = _TmnxWlanGwGgsnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 1),
    _TmnxWlanGwGgsnLastChanged_Type()
)
tmnxWlanGwGgsnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnLastChanged.setStatus("current")


class _TmnxWlanGwGgsnQosUplinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwGgsnQosUplinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 5000


_TmnxWlanGwGgsnQosUplinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwGgsnQosUplinkGbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosUplinkGbrRate = _TmnxWlanGwGgsnQosUplinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 2),
    _TmnxWlanGwGgsnQosUplinkGbrRate_Type()
)
tmnxWlanGwGgsnQosUplinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkGbrRate.setUnits("Kbps")


class _TmnxWlanGwGgsnQosUplinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwGgsnQosUplinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 5000


_TmnxWlanGwGgsnQosUplinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwGgsnQosUplinkMbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosUplinkMbrRate = _TmnxWlanGwGgsnQosUplinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 3),
    _TmnxWlanGwGgsnQosUplinkMbrRate_Type()
)
tmnxWlanGwGgsnQosUplinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosUplinkMbrRate.setUnits("Kbps")


class _TmnxWlanGwGgsnQosDwnlinkGbrRate_Type(TmnxMobProfGbrRate):
    """Custom type tmnxWlanGwGgsnQosDwnlinkGbrRate based on TmnxMobProfGbrRate"""
    defaultValue = 2000


_TmnxWlanGwGgsnQosDwnlinkGbrRate_Type.__name__ = "TmnxMobProfGbrRate"
_TmnxWlanGwGgsnQosDwnlinkGbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosDwnlinkGbrRate = _TmnxWlanGwGgsnQosDwnlinkGbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 4),
    _TmnxWlanGwGgsnQosDwnlinkGbrRate_Type()
)
tmnxWlanGwGgsnQosDwnlinkGbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkGbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkGbrRate.setUnits("Kbps")


class _TmnxWlanGwGgsnQosDwnlinkMbrRate_Type(TmnxMobProfMbrRate):
    """Custom type tmnxWlanGwGgsnQosDwnlinkMbrRate based on TmnxMobProfMbrRate"""
    defaultValue = 2000


_TmnxWlanGwGgsnQosDwnlinkMbrRate_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxWlanGwGgsnQosDwnlinkMbrRate_Object = MibTableColumn
tmnxWlanGwGgsnQosDwnlinkMbrRate = _TmnxWlanGwGgsnQosDwnlinkMbrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 5),
    _TmnxWlanGwGgsnQosDwnlinkMbrRate_Type()
)
tmnxWlanGwGgsnQosDwnlinkMbrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkMbrRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosDwnlinkMbrRate.setUnits("Kbps")


class _TmnxWlanGwGgsnQosArpValue_Type(TmnxMobArpValue):
    """Custom type tmnxWlanGwGgsnQosArpValue based on TmnxMobArpValue"""
    defaultValue = 1

    subtypeSpec = TmnxMobArpValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TmnxWlanGwGgsnQosArpValue_Type.__name__ = "TmnxMobArpValue"
_TmnxWlanGwGgsnQosArpValue_Object = MibTableColumn
tmnxWlanGwGgsnQosArpValue = _TmnxWlanGwGgsnQosArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 6, 21, 1, 6),
    _TmnxWlanGwGgsnQosArpValue_Type()
)
tmnxWlanGwGgsnQosArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnQosArpValue.setStatus("current")
_TmnxWlanGwSysCfgObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwSysCfgObjs = _TmnxWlanGwSysCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7)
)


class _TmnxWlanGwSysCfgServingNwMcc_Type(TmnxMobMccOrEmpty):
    """Custom type tmnxWlanGwSysCfgServingNwMcc based on TmnxMobMccOrEmpty"""
    defaultHexValue = ""


_TmnxWlanGwSysCfgServingNwMcc_Type.__name__ = "TmnxMobMccOrEmpty"
_TmnxWlanGwSysCfgServingNwMcc_Object = MibScalar
tmnxWlanGwSysCfgServingNwMcc = _TmnxWlanGwSysCfgServingNwMcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 1),
    _TmnxWlanGwSysCfgServingNwMcc_Type()
)
tmnxWlanGwSysCfgServingNwMcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgServingNwMcc.setStatus("current")


class _TmnxWlanGwSysCfgServingNwMnc_Type(TmnxMobMncOrEmpty):
    """Custom type tmnxWlanGwSysCfgServingNwMnc based on TmnxMobMncOrEmpty"""
    defaultHexValue = ""


_TmnxWlanGwSysCfgServingNwMnc_Type.__name__ = "TmnxMobMncOrEmpty"
_TmnxWlanGwSysCfgServingNwMnc_Object = MibScalar
tmnxWlanGwSysCfgServingNwMnc = _TmnxWlanGwSysCfgServingNwMnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 2),
    _TmnxWlanGwSysCfgServingNwMnc_Type()
)
tmnxWlanGwSysCfgServingNwMnc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgServingNwMnc.setStatus("current")


class _TmnxWlanGwSysCfgMgwMaxHeldSe_Type(Unsigned32):
    """Custom type tmnxWlanGwSysCfgMgwMaxHeldSe based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_TmnxWlanGwSysCfgMgwMaxHeldSe_Type.__name__ = "Unsigned32"
_TmnxWlanGwSysCfgMgwMaxHeldSe_Object = MibScalar
tmnxWlanGwSysCfgMgwMaxHeldSe = _TmnxWlanGwSysCfgMgwMaxHeldSe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 7, 5),
    _TmnxWlanGwSysCfgMgwMaxHeldSe_Type()
)
tmnxWlanGwSysCfgMgwMaxHeldSe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxWlanGwSysCfgMgwMaxHeldSe.setStatus("current")
_TmnxWlanGwTable_Object = MibTable
tmnxWlanGwTable = _TmnxWlanGwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxWlanGwTable.setStatus("current")
_TmnxWlanGwEntry_Object = MibTableRow
tmnxWlanGwEntry = _TmnxWlanGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1)
)
tmnxWlanGwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwEntry.setStatus("current")
_TmnxWlanGwRowStatus_Type = RowStatus
_TmnxWlanGwRowStatus_Object = MibTableColumn
tmnxWlanGwRowStatus = _TmnxWlanGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 1),
    _TmnxWlanGwRowStatus_Type()
)
tmnxWlanGwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwRowStatus.setStatus("current")
_TmnxWlanGwLastCh_Type = TimeStamp
_TmnxWlanGwLastCh_Object = MibTableColumn
tmnxWlanGwLastCh = _TmnxWlanGwLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 2),
    _TmnxWlanGwLastCh_Type()
)
tmnxWlanGwLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwLastCh.setStatus("current")


class _TmnxWlanGwApn_Type(TmnxMobApnOrZero):
    """Custom type tmnxWlanGwApn based on TmnxMobApnOrZero"""
    defaultValue = OctetString("")

    subtypeSpec = TmnxMobApnOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxWlanGwApn_Type.__name__ = "TmnxMobApnOrZero"
_TmnxWlanGwApn_Object = MibTableColumn
tmnxWlanGwApn = _TmnxWlanGwApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 3),
    _TmnxWlanGwApn_Type()
)
tmnxWlanGwApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwApn.setStatus("current")


class _TmnxWlanGwMobAcctInterimUpdate_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwMobAcctInterimUpdate based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwMobAcctInterimUpdate_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwMobAcctInterimUpdate_Object = MibTableColumn
tmnxWlanGwMobAcctInterimUpdate = _TmnxWlanGwMobAcctInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 8, 1, 10),
    _TmnxWlanGwMobAcctInterimUpdate_Type()
)
tmnxWlanGwMobAcctInterimUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwMobAcctInterimUpdate.setStatus("current")
_TmnxWlanGwDsmSubObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwDsmSubObjs = _TmnxWlanGwDsmSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9)
)
_TmnxWlanGwVlanDsmTable_Object = MibTable
tmnxWlanGwVlanDsmTable = _TmnxWlanGwVlanDsmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmTable.setStatus("current")
_TmnxWlanGwVlanDsmEntry_Object = MibTableRow
tmnxWlanGwVlanDsmEntry = _TmnxWlanGwVlanDsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmEntry.setStatus("current")
_TmnxWlanGwVlanDsmLastCh_Type = TimeStamp
_TmnxWlanGwVlanDsmLastCh_Object = MibTableColumn
tmnxWlanGwVlanDsmLastCh = _TmnxWlanGwVlanDsmLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 1),
    _TmnxWlanGwVlanDsmLastCh_Type()
)
tmnxWlanGwVlanDsmLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmLastCh.setStatus("current")


class _TmnxWlanGwVlanDsmAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxWlanGwVlanDsmAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxWlanGwVlanDsmAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxWlanGwVlanDsmAdminState_Object = MibTableColumn
tmnxWlanGwVlanDsmAdminState = _TmnxWlanGwVlanDsmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 2),
    _TmnxWlanGwVlanDsmAdminState_Type()
)
tmnxWlanGwVlanDsmAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAdminState.setStatus("current")


class _TmnxWlanGwVlanDsmAcctPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmAcctPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmAcctPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmAcctPlcy_Object = MibTableColumn
tmnxWlanGwVlanDsmAcctPlcy = _TmnxWlanGwVlanDsmAcctPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 3),
    _TmnxWlanGwVlanDsmAcctPlcy_Type()
)
tmnxWlanGwVlanDsmAcctPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAcctPlcy.setStatus("current")


class _TmnxWlanGwVlanDsmEgressPolicer_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmEgressPolicer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmEgressPolicer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmEgressPolicer_Object = MibTableColumn
tmnxWlanGwVlanDsmEgressPolicer = _TmnxWlanGwVlanDsmEgressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 4),
    _TmnxWlanGwVlanDsmEgressPolicer_Type()
)
tmnxWlanGwVlanDsmEgressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmEgressPolicer.setStatus("current")


class _TmnxWlanGwVlanDsmIngressPolicer_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmIngressPolicer based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmIngressPolicer_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmIngressPolicer_Object = MibTableColumn
tmnxWlanGwVlanDsmIngressPolicer = _TmnxWlanGwVlanDsmIngressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 5),
    _TmnxWlanGwVlanDsmIngressPolicer_Type()
)
tmnxWlanGwVlanDsmIngressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmIngressPolicer.setStatus("current")


class _TmnxWlanGwVlanDsmIpFilter_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmIpFilter based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmIpFilter_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmIpFilter_Object = MibTableColumn
tmnxWlanGwVlanDsmIpFilter = _TmnxWlanGwVlanDsmIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 6),
    _TmnxWlanGwVlanDsmIpFilter_Type()
)
tmnxWlanGwVlanDsmIpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmIpFilter.setStatus("current")


class _TmnxWlanGwVlanDsmOneTimeRdrUrl_Type(TmnxHttpRedirectUrl):
    """Custom type tmnxWlanGwVlanDsmOneTimeRdrUrl based on TmnxHttpRedirectUrl"""
    defaultHexValue = ""


_TmnxWlanGwVlanDsmOneTimeRdrUrl_Type.__name__ = "TmnxHttpRedirectUrl"
_TmnxWlanGwVlanDsmOneTimeRdrUrl_Object = MibTableColumn
tmnxWlanGwVlanDsmOneTimeRdrUrl = _TmnxWlanGwVlanDsmOneTimeRdrUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 7),
    _TmnxWlanGwVlanDsmOneTimeRdrUrl_Type()
)
tmnxWlanGwVlanDsmOneTimeRdrUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmOneTimeRdrUrl.setStatus("current")


class _TmnxWlanGwVlanDsmOneTimeRdrPort_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDsmOneTimeRdrPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxWlanGwVlanDsmOneTimeRdrPort_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDsmOneTimeRdrPort_Object = MibTableColumn
tmnxWlanGwVlanDsmOneTimeRdrPort = _TmnxWlanGwVlanDsmOneTimeRdrPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 8),
    _TmnxWlanGwVlanDsmOneTimeRdrPort_Type()
)
tmnxWlanGwVlanDsmOneTimeRdrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmOneTimeRdrPort.setStatus("current")


class _TmnxWlanGwVlanDsmAcctUpdInterv_Type(Unsigned32):
    """Custom type tmnxWlanGwVlanDsmAcctUpdInterv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TmnxWlanGwVlanDsmAcctUpdInterv_Type.__name__ = "Unsigned32"
_TmnxWlanGwVlanDsmAcctUpdInterv_Object = MibTableColumn
tmnxWlanGwVlanDsmAcctUpdInterv = _TmnxWlanGwVlanDsmAcctUpdInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 9),
    _TmnxWlanGwVlanDsmAcctUpdInterv_Type()
)
tmnxWlanGwVlanDsmAcctUpdInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAcctUpdInterv.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmAcctUpdInterv.setUnits("minutes")


class _TmnxWlanGwVlanDsmDefAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxWlanGwVlanDsmDefAppProfile based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxWlanGwVlanDsmDefAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxWlanGwVlanDsmDefAppProfile_Object = MibTableColumn
tmnxWlanGwVlanDsmDefAppProfile = _TmnxWlanGwVlanDsmDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 1, 1, 10),
    _TmnxWlanGwVlanDsmDefAppProfile_Type()
)
tmnxWlanGwVlanDsmDefAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmDefAppProfile.setStatus("current")
_TmnxWlanGwDsmIpFilTable_Object = MibTable
tmnxWlanGwDsmIpFilTable = _TmnxWlanGwDsmIpFilTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilTable.setStatus("current")
_TmnxWlanGwDsmIpFilEntry_Object = MibTableRow
tmnxWlanGwDsmIpFilEntry = _TmnxWlanGwDsmIpFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1)
)
tmnxWlanGwDsmIpFilEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilEntry.setStatus("current")
_TmnxWlanGwDsmIpFilName_Type = TNamedItem
_TmnxWlanGwDsmIpFilName_Object = MibTableColumn
tmnxWlanGwDsmIpFilName = _TmnxWlanGwDsmIpFilName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 1),
    _TmnxWlanGwDsmIpFilName_Type()
)
tmnxWlanGwDsmIpFilName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilName.setStatus("current")
_TmnxWlanGwDsmIpFilRowStatus_Type = RowStatus
_TmnxWlanGwDsmIpFilRowStatus_Object = MibTableColumn
tmnxWlanGwDsmIpFilRowStatus = _TmnxWlanGwDsmIpFilRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 2),
    _TmnxWlanGwDsmIpFilRowStatus_Type()
)
tmnxWlanGwDsmIpFilRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilRowStatus.setStatus("current")
_TmnxWlanGwDsmIpFilLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilLastCh_Object = MibTableColumn
tmnxWlanGwDsmIpFilLastCh = _TmnxWlanGwDsmIpFilLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 3),
    _TmnxWlanGwDsmIpFilLastCh_Type()
)
tmnxWlanGwDsmIpFilLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilLastCh.setStatus("current")


class _TmnxWlanGwDsmIpFilDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwDsmIpFilDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwDsmIpFilDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwDsmIpFilDescription_Object = MibTableColumn
tmnxWlanGwDsmIpFilDescription = _TmnxWlanGwDsmIpFilDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 4),
    _TmnxWlanGwDsmIpFilDescription_Type()
)
tmnxWlanGwDsmIpFilDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilDescription.setStatus("current")


class _TmnxWlanGwDsmIpFilDefaultAction_Type(TmnxWlanGwDsmFilterAction):
    """Custom type tmnxWlanGwDsmIpFilDefaultAction based on TmnxWlanGwDsmFilterAction"""
    defaultValue = 1


_TmnxWlanGwDsmIpFilDefaultAction_Type.__name__ = "TmnxWlanGwDsmFilterAction"
_TmnxWlanGwDsmIpFilDefaultAction_Object = MibTableColumn
tmnxWlanGwDsmIpFilDefaultAction = _TmnxWlanGwDsmIpFilDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 2, 1, 5),
    _TmnxWlanGwDsmIpFilDefaultAction_Type()
)
tmnxWlanGwDsmIpFilDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilDefaultAction.setStatus("current")
_TmnxWlanGwDsmIpFilN3Table_Object = MibTable
tmnxWlanGwDsmIpFilN3Table = _TmnxWlanGwDsmIpFilN3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Table.setStatus("current")
_TmnxWlanGwDsmIpFilN3Entry_Object = MibTableRow
tmnxWlanGwDsmIpFilN3Entry = _TmnxWlanGwDsmIpFilN3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1)
)
tmnxWlanGwDsmIpFilN3Entry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilName"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Index"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Entry.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Index_Type(Unsigned32):
    """Custom type tmnxWlanGwDsmIpFilN3Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxWlanGwDsmIpFilN3Index_Type.__name__ = "Unsigned32"
_TmnxWlanGwDsmIpFilN3Index_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Index = _TmnxWlanGwDsmIpFilN3Index_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 1),
    _TmnxWlanGwDsmIpFilN3Index_Type()
)
tmnxWlanGwDsmIpFilN3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Index.setStatus("current")
_TmnxWlanGwDsmIpFilN3RowStatus_Type = RowStatus
_TmnxWlanGwDsmIpFilN3RowStatus_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3RowStatus = _TmnxWlanGwDsmIpFilN3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 2),
    _TmnxWlanGwDsmIpFilN3RowStatus_Type()
)
tmnxWlanGwDsmIpFilN3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3RowStatus.setStatus("current")
_TmnxWlanGwDsmIpFilN3LastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilN3LastCh_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3LastCh = _TmnxWlanGwDsmIpFilN3LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 3),
    _TmnxWlanGwDsmIpFilN3LastCh_Type()
)
tmnxWlanGwDsmIpFilN3LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3LastCh.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Description_Type(TItemDescription):
    """Custom type tmnxWlanGwDsmIpFilN3Description based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwDsmIpFilN3Description_Type.__name__ = "TItemDescription"
_TmnxWlanGwDsmIpFilN3Description_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Description = _TmnxWlanGwDsmIpFilN3Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 4),
    _TmnxWlanGwDsmIpFilN3Description_Type()
)
tmnxWlanGwDsmIpFilN3Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Description.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Action_Type(TmnxWlanGwDsmFilterActionOrNone):
    """Custom type tmnxWlanGwDsmIpFilN3Action based on TmnxWlanGwDsmFilterActionOrNone"""
    defaultValue = 0


_TmnxWlanGwDsmIpFilN3Action_Type.__name__ = "TmnxWlanGwDsmFilterActionOrNone"
_TmnxWlanGwDsmIpFilN3Action_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Action = _TmnxWlanGwDsmIpFilN3Action_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 5),
    _TmnxWlanGwDsmIpFilN3Action_Type()
)
tmnxWlanGwDsmIpFilN3Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Action.setStatus("current")


class _TmnxWlanGwDsmIpFilN3Protocol_Type(TIpProtocol):
    """Custom type tmnxWlanGwDsmIpFilN3Protocol based on TIpProtocol"""
    defaultValue = -1


_TmnxWlanGwDsmIpFilN3Protocol_Type.__name__ = "TIpProtocol"
_TmnxWlanGwDsmIpFilN3Protocol_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3Protocol = _TmnxWlanGwDsmIpFilN3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 6),
    _TmnxWlanGwDsmIpFilN3Protocol_Type()
)
tmnxWlanGwDsmIpFilN3Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3Protocol.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwDsmIpFilN3DestAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwDsmIpFilN3DestAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwDsmIpFilN3DestAddrType_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestAddrType = _TmnxWlanGwDsmIpFilN3DestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 7),
    _TmnxWlanGwDsmIpFilN3DestAddrType_Type()
)
tmnxWlanGwDsmIpFilN3DestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestAddrType.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestAddr_Type(InetAddress):
    """Custom type tmnxWlanGwDsmIpFilN3DestAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxWlanGwDsmIpFilN3DestAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwDsmIpFilN3DestAddr_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestAddr = _TmnxWlanGwDsmIpFilN3DestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 8),
    _TmnxWlanGwDsmIpFilN3DestAddr_Type()
)
tmnxWlanGwDsmIpFilN3DestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestAddr.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxWlanGwDsmIpFilN3DestPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxWlanGwDsmIpFilN3DestPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxWlanGwDsmIpFilN3DestPrefLen_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestPrefLen = _TmnxWlanGwDsmIpFilN3DestPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 9),
    _TmnxWlanGwDsmIpFilN3DestPrefLen_Type()
)
tmnxWlanGwDsmIpFilN3DestPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestPrefLen.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestPortOp_Type(Integer32):
    """Custom type tmnxWlanGwDsmIpFilN3DestPortOp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("eq", 1))
    )


_TmnxWlanGwDsmIpFilN3DestPortOp_Type.__name__ = "Integer32"
_TmnxWlanGwDsmIpFilN3DestPortOp_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestPortOp = _TmnxWlanGwDsmIpFilN3DestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 10),
    _TmnxWlanGwDsmIpFilN3DestPortOp_Type()
)
tmnxWlanGwDsmIpFilN3DestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestPortOp.setStatus("current")


class _TmnxWlanGwDsmIpFilN3DestPort1_Type(InetPortNumber):
    """Custom type tmnxWlanGwDsmIpFilN3DestPort1 based on InetPortNumber"""
    defaultValue = 0


_TmnxWlanGwDsmIpFilN3DestPort1_Type.__name__ = "InetPortNumber"
_TmnxWlanGwDsmIpFilN3DestPort1_Object = MibTableColumn
tmnxWlanGwDsmIpFilN3DestPort1 = _TmnxWlanGwDsmIpFilN3DestPort1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 3, 1, 11),
    _TmnxWlanGwDsmIpFilN3DestPort1_Type()
)
tmnxWlanGwDsmIpFilN3DestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3DestPort1.setStatus("current")
_TmnxWlanGwPolicerTable_Object = MibTable
tmnxWlanGwPolicerTable = _TmnxWlanGwPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerTable.setStatus("current")
_TmnxWlanGwPolicerEntry_Object = MibTableRow
tmnxWlanGwPolicerEntry = _TmnxWlanGwPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1)
)
tmnxWlanGwPolicerEntry.setIndexNames(
    (1, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerName"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerEntry.setStatus("current")
_TmnxWlanGwPolicerName_Type = TNamedItem
_TmnxWlanGwPolicerName_Object = MibTableColumn
tmnxWlanGwPolicerName = _TmnxWlanGwPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 1),
    _TmnxWlanGwPolicerName_Type()
)
tmnxWlanGwPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerName.setStatus("current")
_TmnxWlanGwPolicerRowLastChange_Type = TimeStamp
_TmnxWlanGwPolicerRowLastChange_Object = MibTableColumn
tmnxWlanGwPolicerRowLastChange = _TmnxWlanGwPolicerRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 2),
    _TmnxWlanGwPolicerRowLastChange_Type()
)
tmnxWlanGwPolicerRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerRowLastChange.setStatus("current")
_TmnxWlanGwPolicerRowStatus_Type = RowStatus
_TmnxWlanGwPolicerRowStatus_Object = MibTableColumn
tmnxWlanGwPolicerRowStatus = _TmnxWlanGwPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 3),
    _TmnxWlanGwPolicerRowStatus_Type()
)
tmnxWlanGwPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerRowStatus.setStatus("current")


class _TmnxWlanGwPolicerDescription_Type(TItemDescription):
    """Custom type tmnxWlanGwPolicerDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxWlanGwPolicerDescription_Type.__name__ = "TItemDescription"
_TmnxWlanGwPolicerDescription_Object = MibTableColumn
tmnxWlanGwPolicerDescription = _TmnxWlanGwPolicerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 4),
    _TmnxWlanGwPolicerDescription_Type()
)
tmnxWlanGwPolicerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerDescription.setStatus("current")


class _TmnxWlanGwPolicerType_Type(Integer32):
    """Custom type tmnxWlanGwPolicerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("singleBucketBandwidth", 0),
          ("dualBucketBandwidth", 1))
    )


_TmnxWlanGwPolicerType_Type.__name__ = "Integer32"
_TmnxWlanGwPolicerType_Object = MibTableColumn
tmnxWlanGwPolicerType = _TmnxWlanGwPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 5),
    _TmnxWlanGwPolicerType_Type()
)
tmnxWlanGwPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerType.setStatus("current")


class _TmnxWlanGwPolicerAction_Type(Integer32):
    """Custom type tmnxWlanGwPolicerAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permitDeny", 0),
          ("priorityMark", 1))
    )


_TmnxWlanGwPolicerAction_Type.__name__ = "Integer32"
_TmnxWlanGwPolicerAction_Object = MibTableColumn
tmnxWlanGwPolicerAction = _TmnxWlanGwPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 6),
    _TmnxWlanGwPolicerAction_Type()
)
tmnxWlanGwPolicerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAction.setStatus("current")


class _TmnxWlanGwPolicerAdminPIR_Type(TPIRRate):
    """Custom type tmnxWlanGwPolicerAdminPIR based on TPIRRate"""
    defaultValue = -1


_TmnxWlanGwPolicerAdminPIR_Type.__name__ = "TPIRRate"
_TmnxWlanGwPolicerAdminPIR_Object = MibTableColumn
tmnxWlanGwPolicerAdminPIR = _TmnxWlanGwPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 7),
    _TmnxWlanGwPolicerAdminPIR_Type()
)
tmnxWlanGwPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminPIR.setUnits("kbps")


class _TmnxWlanGwPolicerAdminCIR_Type(TCIRRate):
    """Custom type tmnxWlanGwPolicerAdminCIR based on TCIRRate"""
    defaultValue = 0


_TmnxWlanGwPolicerAdminCIR_Type.__name__ = "TCIRRate"
_TmnxWlanGwPolicerAdminCIR_Object = MibTableColumn
tmnxWlanGwPolicerAdminCIR = _TmnxWlanGwPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 8),
    _TmnxWlanGwPolicerAdminCIR_Type()
)
tmnxWlanGwPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerAdminCIR.setUnits("kbps")


class _TmnxWlanGwPolicerMBS_Type(TmnxWlanGwBurstSize):
    """Custom type tmnxWlanGwPolicerMBS based on TmnxWlanGwBurstSize"""
    defaultValue = 0


_TmnxWlanGwPolicerMBS_Type.__name__ = "TmnxWlanGwBurstSize"
_TmnxWlanGwPolicerMBS_Object = MibTableColumn
tmnxWlanGwPolicerMBS = _TmnxWlanGwPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 9),
    _TmnxWlanGwPolicerMBS_Type()
)
tmnxWlanGwPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerMBS.setUnits("kilobytes")


class _TmnxWlanGwPolicerCBS_Type(TmnxWlanGwBurstSize):
    """Custom type tmnxWlanGwPolicerCBS based on TmnxWlanGwBurstSize"""
    defaultValue = 0


_TmnxWlanGwPolicerCBS_Type.__name__ = "TmnxWlanGwBurstSize"
_TmnxWlanGwPolicerCBS_Object = MibTableColumn
tmnxWlanGwPolicerCBS = _TmnxWlanGwPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 10),
    _TmnxWlanGwPolicerCBS_Type()
)
tmnxWlanGwPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerCBS.setUnits("kilobytes")


class _TmnxWlanGwPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxWlanGwPolicerPIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TmnxWlanGwPolicerPIRAdaptation_Type.__name__ = "TAdaptationRule"
_TmnxWlanGwPolicerPIRAdaptation_Object = MibTableColumn
tmnxWlanGwPolicerPIRAdaptation = _TmnxWlanGwPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 11),
    _TmnxWlanGwPolicerPIRAdaptation_Type()
)
tmnxWlanGwPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerPIRAdaptation.setStatus("current")


class _TmnxWlanGwPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tmnxWlanGwPolicerCIRAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TmnxWlanGwPolicerCIRAdaptation_Type.__name__ = "TAdaptationRule"
_TmnxWlanGwPolicerCIRAdaptation_Object = MibTableColumn
tmnxWlanGwPolicerCIRAdaptation = _TmnxWlanGwPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 9, 4, 1, 12),
    _TmnxWlanGwPolicerCIRAdaptation_Type()
)
tmnxWlanGwPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerCIRAdaptation.setStatus("current")
_TmnxWlanGwUeObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwUeObjs = _TmnxWlanGwUeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11)
)
_TmnxWlanGwUeNextQryId_Type = Unsigned32
_TmnxWlanGwUeNextQryId_Object = MibScalar
tmnxWlanGwUeNextQryId = _TmnxWlanGwUeNextQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 1),
    _TmnxWlanGwUeNextQryId_Type()
)
tmnxWlanGwUeNextQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeNextQryId.setStatus("current")
_TmnxWlanGwUeMaxQryId_Type = Unsigned32
_TmnxWlanGwUeMaxQryId_Object = MibScalar
tmnxWlanGwUeMaxQryId = _TmnxWlanGwUeMaxQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 2),
    _TmnxWlanGwUeMaxQryId_Type()
)
tmnxWlanGwUeMaxQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeMaxQryId.setStatus("current")
_TmnxWlanGwUeQryTable_Object = MibTable
tmnxWlanGwUeQryTable = _TmnxWlanGwUeQryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3)
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryTable.setStatus("current")
_TmnxWlanGwUeQryEntry_Object = MibTableRow
tmnxWlanGwUeQryEntry = _TmnxWlanGwUeQryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1)
)
tmnxWlanGwUeQryEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryEntry.setStatus("current")
_TmnxWlanGwUeQryId_Type = Unsigned32
_TmnxWlanGwUeQryId_Object = MibTableColumn
tmnxWlanGwUeQryId = _TmnxWlanGwUeQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 1),
    _TmnxWlanGwUeQryId_Type()
)
tmnxWlanGwUeQryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryId.setStatus("current")
_TmnxWlanGwUeQryRowStatus_Type = RowStatus
_TmnxWlanGwUeQryRowStatus_Object = MibTableColumn
tmnxWlanGwUeQryRowStatus = _TmnxWlanGwUeQryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 2),
    _TmnxWlanGwUeQryRowStatus_Type()
)
tmnxWlanGwUeQryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryRowStatus.setStatus("current")


class _TmnxWlanGwUeQryWhereState_Type(Bits):
    """Custom type tmnxWlanGwUeQryWhereState based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("bDataTriggered", 0),
          ("bDhcpTriggered", 1),
          ("bIpAssigned", 2),
          ("bAuthorizedOnly", 3),
          ("bIpAssignedAuthorized", 4),
          ("bAlreadySignedIn", 5),
          ("bPortal", 6),
          ("bDistributedSubMgmt", 7),
          ("bEsmUser", 8))
    )

_TmnxWlanGwUeQryWhereState_Type.__name__ = "Bits"
_TmnxWlanGwUeQryWhereState_Object = MibTableColumn
tmnxWlanGwUeQryWhereState = _TmnxWlanGwUeQryWhereState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 3),
    _TmnxWlanGwUeQryWhereState_Type()
)
tmnxWlanGwUeQryWhereState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereState.setStatus("current")
_TmnxWlanGwUeQryWhereMacAddress_Type = MacAddress
_TmnxWlanGwUeQryWhereMacAddress_Object = MibTableColumn
tmnxWlanGwUeQryWhereMacAddress = _TmnxWlanGwUeQryWhereMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 4),
    _TmnxWlanGwUeQryWhereMacAddress_Type()
)
tmnxWlanGwUeQryWhereMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereMacAddress.setStatus("current")


class _TmnxWlanGwUeQryWhereAddrType_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereAddrType_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereAddrType_Object = MibTableColumn
tmnxWlanGwUeQryWhereAddrType = _TmnxWlanGwUeQryWhereAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 5),
    _TmnxWlanGwUeQryWhereAddrType_Type()
)
tmnxWlanGwUeQryWhereAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereAddrType.setStatus("current")


class _TmnxWlanGwUeQryWhereAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereAddr_Object = MibTableColumn
tmnxWlanGwUeQryWhereAddr = _TmnxWlanGwUeQryWhereAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 6),
    _TmnxWlanGwUeQryWhereAddr_Type()
)
tmnxWlanGwUeQryWhereAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereAddr.setStatus("current")


class _TmnxWlanGwUeQryWhereIsaGrp_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxWlanGwUeQryWhereIsaGrp based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereIsaGrp_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxWlanGwUeQryWhereIsaGrp_Object = MibTableColumn
tmnxWlanGwUeQryWhereIsaGrp = _TmnxWlanGwUeQryWhereIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 7),
    _TmnxWlanGwUeQryWhereIsaGrp_Type()
)
tmnxWlanGwUeQryWhereIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereIsaGrp.setStatus("current")


class _TmnxWlanGwUeQryWhereMemberId_Type(Unsigned32):
    """Custom type tmnxWlanGwUeQryWhereMemberId based on Unsigned32"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereMemberId_Type.__name__ = "Unsigned32"
_TmnxWlanGwUeQryWhereMemberId_Object = MibTableColumn
tmnxWlanGwUeQryWhereMemberId = _TmnxWlanGwUeQryWhereMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 8),
    _TmnxWlanGwUeQryWhereMemberId_Type()
)
tmnxWlanGwUeQryWhereMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereMemberId.setStatus("current")


class _TmnxWlanGwUeQryWhereQTag_Type(QTagFullRangeOrNone):
    """Custom type tmnxWlanGwUeQryWhereQTag based on QTagFullRangeOrNone"""
    defaultValue = -1


_TmnxWlanGwUeQryWhereQTag_Type.__name__ = "QTagFullRangeOrNone"
_TmnxWlanGwUeQryWhereQTag_Object = MibTableColumn
tmnxWlanGwUeQryWhereQTag = _TmnxWlanGwUeQryWhereQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 9),
    _TmnxWlanGwUeQryWhereQTag_Type()
)
tmnxWlanGwUeQryWhereQTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereQTag.setStatus("current")


class _TmnxWlanGwUeQryWhereTuRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxWlanGwUeQryWhereTuRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereTuRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxWlanGwUeQryWhereTuRouter_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuRouter = _TmnxWlanGwUeQryWhereTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 10),
    _TmnxWlanGwUeQryWhereTuRouter_Type()
)
tmnxWlanGwUeQryWhereTuRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuRouter.setStatus("current")


class _TmnxWlanGwUeQryWhereTuRemAddrTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereTuRemAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereTuRemAddrTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereTuRemAddrTyp_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuRemAddrTyp = _TmnxWlanGwUeQryWhereTuRemAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 11),
    _TmnxWlanGwUeQryWhereTuRemAddrTyp_Type()
)
tmnxWlanGwUeQryWhereTuRemAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuRemAddrTyp.setStatus("current")


class _TmnxWlanGwUeQryWhereTuRemAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereTuRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereTuRemAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereTuRemAddr_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuRemAddr = _TmnxWlanGwUeQryWhereTuRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 12),
    _TmnxWlanGwUeQryWhereTuRemAddr_Type()
)
tmnxWlanGwUeQryWhereTuRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuRemAddr.setStatus("current")


class _TmnxWlanGwUeQryWhereTuLocAddrTyp_Type(InetAddressType):
    """Custom type tmnxWlanGwUeQryWhereTuLocAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxWlanGwUeQryWhereTuLocAddrTyp_Type.__name__ = "InetAddressType"
_TmnxWlanGwUeQryWhereTuLocAddrTyp_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuLocAddrTyp = _TmnxWlanGwUeQryWhereTuLocAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 13),
    _TmnxWlanGwUeQryWhereTuLocAddrTyp_Type()
)
tmnxWlanGwUeQryWhereTuLocAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuLocAddrTyp.setStatus("current")


class _TmnxWlanGwUeQryWhereTuLocAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeQryWhereTuLocAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeQryWhereTuLocAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeQryWhereTuLocAddr_Object = MibTableColumn
tmnxWlanGwUeQryWhereTuLocAddr = _TmnxWlanGwUeQryWhereTuLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 14),
    _TmnxWlanGwUeQryWhereTuLocAddr_Type()
)
tmnxWlanGwUeQryWhereTuLocAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryWhereTuLocAddr.setStatus("current")
_TmnxWlanGwUeQryNumResults_Type = Gauge32
_TmnxWlanGwUeQryNumResults_Object = MibTableColumn
tmnxWlanGwUeQryNumResults = _TmnxWlanGwUeQryNumResults_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 3, 1, 200),
    _TmnxWlanGwUeQryNumResults_Type()
)
tmnxWlanGwUeQryNumResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryNumResults.setStatus("current")
_TmnxWlanGwUeResTable_Object = MibTable
tmnxWlanGwUeResTable = _TmnxWlanGwUeResTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4)
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTable.setStatus("current")
_TmnxWlanGwUeResEntry_Object = MibTableRow
tmnxWlanGwUeResEntry = _TmnxWlanGwUeResEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1)
)
tmnxWlanGwUeResEntry.setIndexNames(
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryId"),
    (0, "TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResId"),
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEntry.setStatus("current")
_TmnxWlanGwUeResId_Type = TmnxWlanGwUeIdentifier
_TmnxWlanGwUeResId_Object = MibTableColumn
tmnxWlanGwUeResId = _TmnxWlanGwUeResId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 1),
    _TmnxWlanGwUeResId_Type()
)
tmnxWlanGwUeResId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResId.setStatus("current")
_TmnxWlanGwUeResMacAddress_Type = MacAddress
_TmnxWlanGwUeResMacAddress_Object = MibTableColumn
tmnxWlanGwUeResMacAddress = _TmnxWlanGwUeResMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 2),
    _TmnxWlanGwUeResMacAddress_Type()
)
tmnxWlanGwUeResMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResMacAddress.setStatus("current")
_TmnxWlanGwUeResQTag_Type = QTagFullRangeOrNone
_TmnxWlanGwUeResQTag_Object = MibTableColumn
tmnxWlanGwUeResQTag = _TmnxWlanGwUeResQTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 3),
    _TmnxWlanGwUeResQTag_Type()
)
tmnxWlanGwUeResQTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResQTag.setStatus("current")
_TmnxWlanGwUeResAddrType_Type = InetAddressType
_TmnxWlanGwUeResAddrType_Object = MibTableColumn
tmnxWlanGwUeResAddrType = _TmnxWlanGwUeResAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 4),
    _TmnxWlanGwUeResAddrType_Type()
)
tmnxWlanGwUeResAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAddrType.setStatus("current")


class _TmnxWlanGwUeResAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResAddr_Object = MibTableColumn
tmnxWlanGwUeResAddr = _TmnxWlanGwUeResAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 5),
    _TmnxWlanGwUeResAddr_Type()
)
tmnxWlanGwUeResAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAddr.setStatus("current")


class _TmnxWlanGwUeResState_Type(Integer32):
    """Custom type tmnxWlanGwUeResState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("dataTriggered", 2),
          ("dhcpTriggered", 3),
          ("ipAssigned", 4),
          ("authorizedOnly", 5),
          ("ipAssignedAuthorized", 6),
          ("alreadySignedIn", 7),
          ("portal", 8),
          ("distributedSubMgmt", 9),
          ("esmUser", 10))
    )


_TmnxWlanGwUeResState_Type.__name__ = "Integer32"
_TmnxWlanGwUeResState_Object = MibTableColumn
tmnxWlanGwUeResState = _TmnxWlanGwUeResState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 6),
    _TmnxWlanGwUeResState_Type()
)
tmnxWlanGwUeResState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResState.setStatus("current")
_TmnxWlanGwUeResIsaGrp_Type = TmnxWlanGwIsaGrpIdOrZero
_TmnxWlanGwUeResIsaGrp_Object = MibTableColumn
tmnxWlanGwUeResIsaGrp = _TmnxWlanGwUeResIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 7),
    _TmnxWlanGwUeResIsaGrp_Type()
)
tmnxWlanGwUeResIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIsaGrp.setStatus("current")
_TmnxWlanGwUeResIsaMemberId_Type = Unsigned32
_TmnxWlanGwUeResIsaMemberId_Object = MibTableColumn
tmnxWlanGwUeResIsaMemberId = _TmnxWlanGwUeResIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 8),
    _TmnxWlanGwUeResIsaMemberId_Type()
)
tmnxWlanGwUeResIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIsaMemberId.setStatus("current")
_TmnxWlanGwUeResTuRouter_Type = TmnxVRtrIDOrZero
_TmnxWlanGwUeResTuRouter_Object = MibTableColumn
tmnxWlanGwUeResTuRouter = _TmnxWlanGwUeResTuRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 9),
    _TmnxWlanGwUeResTuRouter_Type()
)
tmnxWlanGwUeResTuRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuRouter.setStatus("current")
_TmnxWlanGwUeResTuAddrType_Type = InetAddressType
_TmnxWlanGwUeResTuAddrType_Object = MibTableColumn
tmnxWlanGwUeResTuAddrType = _TmnxWlanGwUeResTuAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 10),
    _TmnxWlanGwUeResTuAddrType_Type()
)
tmnxWlanGwUeResTuAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuAddrType.setStatus("current")


class _TmnxWlanGwUeResTuRemoteAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResTuRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResTuRemoteAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResTuRemoteAddr_Object = MibTableColumn
tmnxWlanGwUeResTuRemoteAddr = _TmnxWlanGwUeResTuRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 11),
    _TmnxWlanGwUeResTuRemoteAddr_Type()
)
tmnxWlanGwUeResTuRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuRemoteAddr.setStatus("current")


class _TmnxWlanGwUeResTuLocalAddr_Type(InetAddress):
    """Custom type tmnxWlanGwUeResTuLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxWlanGwUeResTuLocalAddr_Type.__name__ = "InetAddress"
_TmnxWlanGwUeResTuLocalAddr_Object = MibTableColumn
tmnxWlanGwUeResTuLocalAddr = _TmnxWlanGwUeResTuLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 12),
    _TmnxWlanGwUeResTuLocalAddr_Type()
)
tmnxWlanGwUeResTuLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTuLocalAddr.setStatus("current")
_TmnxWlanGwUeResApMacAddress_Type = MacAddress
_TmnxWlanGwUeResApMacAddress_Object = MibTableColumn
tmnxWlanGwUeResApMacAddress = _TmnxWlanGwUeResApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 100),
    _TmnxWlanGwUeResApMacAddress_Type()
)
tmnxWlanGwUeResApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResApMacAddress.setStatus("current")
_TmnxWlanGwUeResSsid_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResSsid_Object = MibTableColumn
tmnxWlanGwUeResSsid = _TmnxWlanGwUeResSsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 101),
    _TmnxWlanGwUeResSsid_Type()
)
tmnxWlanGwUeResSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSsid.setStatus("current")
_TmnxWlanGwUeResMplsLabel_Type = MplsLabel
_TmnxWlanGwUeResMplsLabel_Object = MibTableColumn
tmnxWlanGwUeResMplsLabel = _TmnxWlanGwUeResMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 102),
    _TmnxWlanGwUeResMplsLabel_Type()
)
tmnxWlanGwUeResMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResMplsLabel.setStatus("current")


class _TmnxWlanGwUeResLastMoveTime_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResLastMoveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResLastMoveTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResLastMoveTime_Object = MibTableColumn
tmnxWlanGwUeResLastMoveTime = _TmnxWlanGwUeResLastMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 103),
    _TmnxWlanGwUeResLastMoveTime_Type()
)
tmnxWlanGwUeResLastMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResLastMoveTime.setStatus("current")


class _TmnxWlanGwUeResExpirationTime_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResExpirationTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResExpirationTime_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResExpirationTime_Object = MibTableColumn
tmnxWlanGwUeResExpirationTime = _TmnxWlanGwUeResExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 104),
    _TmnxWlanGwUeResExpirationTime_Type()
)
tmnxWlanGwUeResExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResExpirationTime.setStatus("current")
_TmnxWlanGwUeResIdleTimeout_Type = Unsigned32
_TmnxWlanGwUeResIdleTimeout_Object = MibTableColumn
tmnxWlanGwUeResIdleTimeout = _TmnxWlanGwUeResIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 105),
    _TmnxWlanGwUeResIdleTimeout_Type()
)
tmnxWlanGwUeResIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIdleTimeout.setUnits("seconds")


class _TmnxWlanGwUeResSessionTimeout_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResSessionTimeout based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResSessionTimeout_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResSessionTimeout_Object = MibTableColumn
tmnxWlanGwUeResSessionTimeout = _TmnxWlanGwUeResSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 106),
    _TmnxWlanGwUeResSessionTimeout_Type()
)
tmnxWlanGwUeResSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResSessionTimeout.setStatus("current")
_TmnxWlanGwUeResNatPlcy_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResNatPlcy_Object = MibTableColumn
tmnxWlanGwUeResNatPlcy = _TmnxWlanGwUeResNatPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 107),
    _TmnxWlanGwUeResNatPlcy_Type()
)
tmnxWlanGwUeResNatPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResNatPlcy.setStatus("current")
_TmnxWlanGwUeResHttpRdrPlcy_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResHttpRdrPlcy_Object = MibTableColumn
tmnxWlanGwUeResHttpRdrPlcy = _TmnxWlanGwUeResHttpRdrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 108),
    _TmnxWlanGwUeResHttpRdrPlcy_Type()
)
tmnxWlanGwUeResHttpRdrPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResHttpRdrPlcy.setStatus("current")
_TmnxWlanGwUeResDsmIpFilter_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResDsmIpFilter_Object = MibTableColumn
tmnxWlanGwUeResDsmIpFilter = _TmnxWlanGwUeResDsmIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 109),
    _TmnxWlanGwUeResDsmIpFilter_Type()
)
tmnxWlanGwUeResDsmIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmIpFilter.setStatus("current")
_TmnxWlanGwUeResDsmAcctPlcy_Type = TNamedItemOrEmpty
_TmnxWlanGwUeResDsmAcctPlcy_Object = MibTableColumn
tmnxWlanGwUeResDsmAcctPlcy = _TmnxWlanGwUeResDsmAcctPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 110),
    _TmnxWlanGwUeResDsmAcctPlcy_Type()
)
tmnxWlanGwUeResDsmAcctPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAcctPlcy.setStatus("current")
_TmnxWlanGwUeResDsmAcctUpdInterv_Type = Unsigned32
_TmnxWlanGwUeResDsmAcctUpdInterv_Object = MibTableColumn
tmnxWlanGwUeResDsmAcctUpdInterv = _TmnxWlanGwUeResDsmAcctUpdInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 111),
    _TmnxWlanGwUeResDsmAcctUpdInterv_Type()
)
tmnxWlanGwUeResDsmAcctUpdInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAcctUpdInterv.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResDsmAcctUpdInterv.setUnits("seconds")


class _TmnxWlanGwUeResAcctUpdate_Type(DateAndTime):
    """Custom type tmnxWlanGwUeResAcctUpdate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxWlanGwUeResAcctUpdate_Type.__name__ = "DateAndTime"
_TmnxWlanGwUeResAcctUpdate_Object = MibTableColumn
tmnxWlanGwUeResAcctUpdate = _TmnxWlanGwUeResAcctUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 112),
    _TmnxWlanGwUeResAcctUpdate_Type()
)
tmnxWlanGwUeResAcctUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResAcctUpdate.setStatus("current")
_TmnxWlanGwUeResIngOperPir_Type = TPIRRate
_TmnxWlanGwUeResIngOperPir_Object = MibTableColumn
tmnxWlanGwUeResIngOperPir = _TmnxWlanGwUeResIngOperPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 113),
    _TmnxWlanGwUeResIngOperPir_Type()
)
tmnxWlanGwUeResIngOperPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperPir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperPir.setUnits("kbps")
_TmnxWlanGwUeResIngOperCir_Type = TCIRRate
_TmnxWlanGwUeResIngOperCir_Object = MibTableColumn
tmnxWlanGwUeResIngOperCir = _TmnxWlanGwUeResIngOperCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 114),
    _TmnxWlanGwUeResIngOperCir_Type()
)
tmnxWlanGwUeResIngOperCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperCir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResIngOperCir.setUnits("kbps")
_TmnxWlanGwUeResEgrOperPir_Type = TPIRRate
_TmnxWlanGwUeResEgrOperPir_Object = MibTableColumn
tmnxWlanGwUeResEgrOperPir = _TmnxWlanGwUeResEgrOperPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 115),
    _TmnxWlanGwUeResEgrOperPir_Type()
)
tmnxWlanGwUeResEgrOperPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperPir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperPir.setUnits("kbps")
_TmnxWlanGwUeResEgrOperCir_Type = TCIRRate
_TmnxWlanGwUeResEgrOperCir_Object = MibTableColumn
tmnxWlanGwUeResEgrOperCir = _TmnxWlanGwUeResEgrOperCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 116),
    _TmnxWlanGwUeResEgrOperCir_Type()
)
tmnxWlanGwUeResEgrOperCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperCir.setStatus("current")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResEgrOperCir.setUnits("kbps")
_TmnxWlanGwUeResRxPkts_Type = Counter64
_TmnxWlanGwUeResRxPkts_Object = MibTableColumn
tmnxWlanGwUeResRxPkts = _TmnxWlanGwUeResRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 200),
    _TmnxWlanGwUeResRxPkts_Type()
)
tmnxWlanGwUeResRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResRxPkts.setStatus("current")
_TmnxWlanGwUeResRxOctets_Type = Counter64
_TmnxWlanGwUeResRxOctets_Object = MibTableColumn
tmnxWlanGwUeResRxOctets = _TmnxWlanGwUeResRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 201),
    _TmnxWlanGwUeResRxOctets_Type()
)
tmnxWlanGwUeResRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResRxOctets.setStatus("current")
_TmnxWlanGwUeResTxPkts_Type = Counter64
_TmnxWlanGwUeResTxPkts_Object = MibTableColumn
tmnxWlanGwUeResTxPkts = _TmnxWlanGwUeResTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 202),
    _TmnxWlanGwUeResTxPkts_Type()
)
tmnxWlanGwUeResTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTxPkts.setStatus("current")
_TmnxWlanGwUeResTxOctets_Type = Counter64
_TmnxWlanGwUeResTxOctets_Object = MibTableColumn
tmnxWlanGwUeResTxOctets = _TmnxWlanGwUeResTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 11, 4, 1, 203),
    _TmnxWlanGwUeResTxOctets_Type()
)
tmnxWlanGwUeResTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwUeResTxOctets.setStatus("current")
_TmnxWlanGwGrpTableLastCh_Type = TimeStamp
_TmnxWlanGwGrpTableLastCh_Object = MibScalar
tmnxWlanGwGrpTableLastCh = _TmnxWlanGwGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 100),
    _TmnxWlanGwGrpTableLastCh_Type()
)
tmnxWlanGwGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGrpTableLastCh.setStatus("current")
_TmnxWlanGwIomTableLastCh_Type = TimeStamp
_TmnxWlanGwIomTableLastCh_Object = MibScalar
tmnxWlanGwIomTableLastCh = _TmnxWlanGwIomTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 101),
    _TmnxWlanGwIomTableLastCh_Type()
)
tmnxWlanGwIomTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIomTableLastCh.setStatus("current")
_TmnxWlanGwSoftGreIfTableLastCh_Type = TimeStamp
_TmnxWlanGwSoftGreIfTableLastCh_Object = MibScalar
tmnxWlanGwSoftGreIfTableLastCh = _TmnxWlanGwSoftGreIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 102),
    _TmnxWlanGwSoftGreIfTableLastCh_Type()
)
tmnxWlanGwSoftGreIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreIfTableLastCh.setStatus("current")
_TmnxWlanGwIfRetailTableLastCh_Type = TimeStamp
_TmnxWlanGwIfRetailTableLastCh_Object = MibScalar
tmnxWlanGwIfRetailTableLastCh = _TmnxWlanGwIfRetailTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 103),
    _TmnxWlanGwIfRetailTableLastCh_Type()
)
tmnxWlanGwIfRetailTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwIfRetailTableLastCh.setStatus("obsolete")
_TmnxWlanGwMgwProfTableLastCh_Type = TimeStamp
_TmnxWlanGwMgwProfTableLastCh_Object = MibScalar
tmnxWlanGwMgwProfTableLastCh = _TmnxWlanGwMgwProfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 104),
    _TmnxWlanGwMgwProfTableLastCh_Type()
)
tmnxWlanGwMgwProfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwProfTableLastCh.setStatus("current")
_TmnxWlanGwMgwAddrTableLastCh_Type = TimeStamp
_TmnxWlanGwMgwAddrTableLastCh_Object = MibScalar
tmnxWlanGwMgwAddrTableLastCh = _TmnxWlanGwMgwAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 105),
    _TmnxWlanGwMgwAddrTableLastCh_Type()
)
tmnxWlanGwMgwAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwAddrTableLastCh.setStatus("current")
_TmnxWlanGwTableLastCh_Type = TimeStamp
_TmnxWlanGwTableLastCh_Object = MibScalar
tmnxWlanGwTableLastCh = _TmnxWlanGwTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 106),
    _TmnxWlanGwTableLastCh_Type()
)
tmnxWlanGwTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwTableLastCh.setStatus("current")
_TmnxWlanGwVlanTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanTableLastCh_Object = MibScalar
tmnxWlanGwVlanTableLastCh = _TmnxWlanGwVlanTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 107),
    _TmnxWlanGwVlanTableLastCh_Type()
)
tmnxWlanGwVlanTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanTableLastCh.setStatus("current")
_TmnxWlanGwPgwTableLastCh_Type = TimeStamp
_TmnxWlanGwPgwTableLastCh_Object = MibScalar
tmnxWlanGwPgwTableLastCh = _TmnxWlanGwPgwTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 108),
    _TmnxWlanGwPgwTableLastCh_Type()
)
tmnxWlanGwPgwTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPgwTableLastCh.setStatus("current")
_TmnxWlanGwGgsnTableLastCh_Type = TimeStamp
_TmnxWlanGwGgsnTableLastCh_Object = MibScalar
tmnxWlanGwGgsnTableLastCh = _TmnxWlanGwGgsnTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 109),
    _TmnxWlanGwGgsnTableLastCh_Type()
)
tmnxWlanGwGgsnTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwGgsnTableLastCh.setStatus("current")
_TmnxWlanGwSubIfTableLastCh_Type = TimeStamp
_TmnxWlanGwSubIfTableLastCh_Object = MibScalar
tmnxWlanGwSubIfTableLastCh = _TmnxWlanGwSubIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 110),
    _TmnxWlanGwSubIfTableLastCh_Type()
)
tmnxWlanGwSubIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfTableLastCh.setStatus("current")
_TmnxWlanGwVlanDsmTableLastCh_Type = TimeStamp
_TmnxWlanGwVlanDsmTableLastCh_Object = MibScalar
tmnxWlanGwVlanDsmTableLastCh = _TmnxWlanGwVlanDsmTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 111),
    _TmnxWlanGwVlanDsmTableLastCh_Type()
)
tmnxWlanGwVlanDsmTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwVlanDsmTableLastCh.setStatus("current")
_TmnxWlanGwDsmIpFilTableLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilTableLastCh_Object = MibScalar
tmnxWlanGwDsmIpFilTableLastCh = _TmnxWlanGwDsmIpFilTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 112),
    _TmnxWlanGwDsmIpFilTableLastCh_Type()
)
tmnxWlanGwDsmIpFilTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilTableLastCh.setStatus("current")
_TmnxWlanGwDsmIpFilN3TableLastCh_Type = TimeStamp
_TmnxWlanGwDsmIpFilN3TableLastCh_Object = MibScalar
tmnxWlanGwDsmIpFilN3TableLastCh = _TmnxWlanGwDsmIpFilN3TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 113),
    _TmnxWlanGwDsmIpFilN3TableLastCh_Type()
)
tmnxWlanGwDsmIpFilN3TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwDsmIpFilN3TableLastCh.setStatus("current")
_TmnxWlanGwPolicerTableLastCh_Type = TimeStamp
_TmnxWlanGwPolicerTableLastCh_Object = MibScalar
tmnxWlanGwPolicerTableLastCh = _TmnxWlanGwPolicerTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 114),
    _TmnxWlanGwPolicerTableLastCh_Type()
)
tmnxWlanGwPolicerTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPolicerTableLastCh.setStatus("current")
_TmnxWlanGwResrcProblem_Type = TruthValue
_TmnxWlanGwResrcProblem_Object = MibScalar
tmnxWlanGwResrcProblem = _TmnxWlanGwResrcProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 200),
    _TmnxWlanGwResrcProblem_Type()
)
tmnxWlanGwResrcProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwResrcProblem.setStatus("current")
_TmnxWlanGwNumSoftGreTu_Type = Gauge32
_TmnxWlanGwNumSoftGreTu_Object = MibScalar
tmnxWlanGwNumSoftGreTu = _TmnxWlanGwNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 201),
    _TmnxWlanGwNumSoftGreTu_Type()
)
tmnxWlanGwNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwNumSoftGreTu.setStatus("current")
_TmnxWlanGwPeakNumSoftGreTu_Type = Gauge32
_TmnxWlanGwPeakNumSoftGreTu_Object = MibScalar
tmnxWlanGwPeakNumSoftGreTu = _TmnxWlanGwPeakNumSoftGreTu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 202),
    _TmnxWlanGwPeakNumSoftGreTu_Type()
)
tmnxWlanGwPeakNumSoftGreTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPeakNumSoftGreTu.setStatus("current")
_TmnxWlanGwNumUe_Type = Gauge32
_TmnxWlanGwNumUe_Object = MibScalar
tmnxWlanGwNumUe = _TmnxWlanGwNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 203),
    _TmnxWlanGwNumUe_Type()
)
tmnxWlanGwNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwNumUe.setStatus("current")
_TmnxWlanGwPeakNumUe_Type = Gauge32
_TmnxWlanGwPeakNumUe_Object = MibScalar
tmnxWlanGwPeakNumUe = _TmnxWlanGwPeakNumUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 204),
    _TmnxWlanGwPeakNumUe_Type()
)
tmnxWlanGwPeakNumUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwPeakNumUe.setStatus("current")
_TmnxWlanGwNumMgw_Type = Gauge32
_TmnxWlanGwNumMgw_Object = MibScalar
tmnxWlanGwNumMgw = _TmnxWlanGwNumMgw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 205),
    _TmnxWlanGwNumMgw_Type()
)
tmnxWlanGwNumMgw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwNumMgw.setStatus("current")
_TmnxWlanGwMgwNumHeldSe_Type = Gauge32
_TmnxWlanGwMgwNumHeldSe_Object = MibScalar
tmnxWlanGwMgwNumHeldSe = _TmnxWlanGwMgwNumHeldSe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 1, 210),
    _TmnxWlanGwMgwNumHeldSe_Type()
)
tmnxWlanGwMgwNumHeldSe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxWlanGwMgwNumHeldSe.setStatus("current")
_TmnxWlanGwNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxWlanGwNotificationObjs = _TmnxWlanGwNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2)
)


class _TmnxWlanGwNotifyDescription_Type(DisplayString):
    """Custom type tmnxWlanGwNotifyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxWlanGwNotifyDescription_Type.__name__ = "DisplayString"
_TmnxWlanGwNotifyDescription_Object = MibScalar
tmnxWlanGwNotifyDescription = _TmnxWlanGwNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 1),
    _TmnxWlanGwNotifyDescription_Type()
)
tmnxWlanGwNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyDescription.setStatus("current")
_TmnxWlanGwNotifyTrue_Type = TruthValue
_TmnxWlanGwNotifyTrue_Object = MibScalar
tmnxWlanGwNotifyTrue = _TmnxWlanGwNotifyTrue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 2),
    _TmnxWlanGwNotifyTrue_Type()
)
tmnxWlanGwNotifyTrue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyTrue.setStatus("current")


class _TmnxWlanGwNotify3gppRelease_Type(DisplayString):
    """Custom type tmnxWlanGwNotify3gppRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TmnxWlanGwNotify3gppRelease_Type.__name__ = "DisplayString"
_TmnxWlanGwNotify3gppRelease_Object = MibScalar
tmnxWlanGwNotify3gppRelease = _TmnxWlanGwNotify3gppRelease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 81, 2, 3),
    _TmnxWlanGwNotify3gppRelease_Type()
)
tmnxWlanGwNotify3gppRelease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxWlanGwNotify3gppRelease.setStatus("current")
_TmnxWlanGwNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxWlanGwNotifyPrefix = _TmnxWlanGwNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81)
)
_TmnxWlanGwNotifications_ObjectIdentity = ObjectIdentity
tmnxWlanGwNotifications = _TmnxWlanGwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0)
)
tmnxWlanGwSoftGreIfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwSoftGreXtEntry")
)
tmnxWlanGwSoftGreXtEntry.setIndexNames(*tmnxWlanGwSoftGreIfEntry.getIndexNames())
tmnxWlanGwMgwProfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwPgwEntry")
)
tmnxWlanGwPgwEntry.setIndexNames(*tmnxWlanGwMgwProfEntry.getIndexNames())
tmnxWlanGwMgwProfEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwGgsnEntry")
)
tmnxWlanGwGgsnEntry.setIndexNames(*tmnxWlanGwMgwProfEntry.getIndexNames())
tmnxWlanGwVlanEntry.registerAugmentions(
    ("TIMETRA-WLAN-GW-MIB",
     "tmnxWlanGwVlanDsmEntry")
)
tmnxWlanGwVlanDsmEntry.setIndexNames(*tmnxWlanGwVlanEntry.getIndexNames())

# Managed Objects groups

tmnxWlanGwIsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 1)
)
tmnxWlanGwIsaGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpActiveIomLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpPortPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpTunnelPortPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomOperState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberChassisIndex"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberCardSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberSlotNum"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEegMemberAct"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberEegMemberPend"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberTuQosProblem"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsValHw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberStatsValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblem"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwIsaGroup.setStatus("current")

tmnxWlanGwSoftGreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 2)
)
tmnxWlanGwSoftGreGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapingType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapeMultiUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEQosPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfESchedPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEAggRateLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobTrigger"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDefRetailSvc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTcpMssAdjust"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEstabTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegSvcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegEncapValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRemainingHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuUeSsid"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreGroup.setStatus("obsolete")

tmnxWlanGwObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 3)
)
tmnxWlanGwObjGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuQosRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSsidNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumUe"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwObjGroup.setStatus("obsolete")

tmnxWlanGwMgwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 4)
)
tmnxWlanGwMgwGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeImsi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfKeepAlvRetryCnt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfMsgReTxTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfMsgReTxRetryCnt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfKeepAlvTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfKeepAlvResp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfInterfaceType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwAddrProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwLocalAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwControl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRestartCnt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwInterfaceType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsValLw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanMgwStatsValHw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeMgwRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeMgwAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeMgwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeRemoteCtrlTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeLocalCtrlTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcRemoteTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcLocalTeid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgServingNwMcc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgServingNwMnc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwApn"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumMgw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsVal"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsValLw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpStatsValHw"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwGroup.setStatus("current")

tmnxWlanGwSoftGreV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 5)
)
tmnxWlanGwSoftGreV11v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxMacFmt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxMacFmt"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreV11v0Group.setStatus("obsolete")

tmnxWlanGwMgwV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 6)
)
tmnxWlanGwMgwV11v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwArecCacheTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCachePref"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheNext"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheRepl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSnaptrCacheTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheWeight"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCachePort"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheTarget"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSrvCacheTtl"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwV11v0Group.setStatus("current")

tmnxWlanGwMgwQosIeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 10)
)
tmnxWlanGwMgwQosIeGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosUplinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosUplinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosDwnlinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosDwnlinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosArpValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwQosQciValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnLastChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosUplinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosUplinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosDwnlinkGbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosDwnlinkMbrRate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnQosArpValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPgwTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGgsnTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosUlGbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosUlMbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosDlGbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosDlMbr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosArp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwBcQosQci"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwQosIeGroup.setStatus("current")

tmnxWlanGwMgwChargingCharGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 11)
)
tmnxWlanGwMgwChargingCharGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfChrgCharHome"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfChrgCharRoam"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGtpSeChrgChar"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwChargingCharGroup.setStatus("current")

tmnxWlanGwMobilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 15)
)
tmnxWlanGwMobilityGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobAcctInterimUpdate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobArpAp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuApMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuApLearnFailed"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMobilityGroup.setStatus("current")

tmnxWlanGwMgwSeHoldTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 16)
)
tmnxWlanGwMgwSeHoldTimeGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfSeHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSysCfgMgwMaxHeldSe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwNumHeldSe"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwSeHoldTimeGroup.setStatus("current")

tmnxWlanGwV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 17)
)
tmnxWlanGwV12v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpDegraded"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeTuQosRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUePrevApAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSsidNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPeakNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfReportWlanLoc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwProfProtocolCfgOpt"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV12v0Group.setStatus("current")

tmnxWlanGwSoftGreV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 18)
)
tmnxWlanGwSoftGreV12v0Group.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGrpId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapingType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfShapeMultiUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEQosPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfESchedPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEAggRateLimit"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobTrigger"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfMobHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDefRetailSvc"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTcpMssAdjust"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfEHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfNumSoftGreTu"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuEstabTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuIsaMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegSvcId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegPortId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegEncapValue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegName"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosEegMember"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosNumUe"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosRemainingHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreTuUeSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfGwV6Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanRadProxMacFmt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDownIfGrpDeg"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSoftGreV12v0Group.setStatus("current")

tmnxWlanGwRedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 19)
)
tmnxWlanGwRedGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedExpPrefixType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedExpPrefix"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedExpPrefixLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedMonPrefixType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedMonPrefix"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedMonPrefixLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedActive"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedSwitch"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwRedGroup.setStatus("current")

tmnxWlanGwDsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 20)
)
tmnxWlanGwDsmGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpIsaAaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanAuthOnDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAdminState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAcctPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmEgressPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmIngressPolicer"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmIpFilter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmOneTimeRdrUrl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmOneTimeRdrPort"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmAcctUpdInterv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmDefAppProfile"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwVlanDsmTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilDefaultAction"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3TableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3RowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3LastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Description"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Action"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3Protocol"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestPrefLen"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestPortOp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmIpFilN3DestPort1"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerRowLastChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerAction"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerAdminPIR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerAdminCIR"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerMBS"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerCBS"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerPIRAdaptation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerCIRAdaptation"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwPolicerTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwDsmGroup.setStatus("current")

tmnxWlanGwUeQryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 23)
)
tmnxWlanGwUeQryGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeNextQryId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeMaxQryId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereIsaGrp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuRemAddrTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuRemAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuLocAddrTyp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryWhereTuLocAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryNumResults"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResState"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIsaGrp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIsaMemberId"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResQTag"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuRouter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuLocalAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTuRemoteAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSsid"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResApMacAddress"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResMplsLabel"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResLastMoveTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResExpirationTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIdleTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResSessionTimeout"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResNatPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmIpFilter"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmAcctPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResDsmAcctUpdInterv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResAcctUpdate"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIngOperPir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResIngOperCir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResEgrOperPir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResEgrOperCir"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResRxPkts"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResRxOctets"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTxPkts"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeResTxOctets"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwUeQryGroup.setStatus("current")

tmnxWlanGwObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 98)
)
tmnxWlanGwObsoletedGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwCacheTtl"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailRowStatus"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailService"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIfRetailTableLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfDataTrigg"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfAuthHoldTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxVrtr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxSrv"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreIfRadProxMacFmt"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLastCh"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDhcp"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtAddr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtActLeaseTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtDns2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb1Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2AddrType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNb2Addr"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtHttpRdrPlcy"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreXtNatPlcy"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwObsoletedGroup.setStatus("current")

tmnxWlanGwNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 99)
)
tmnxWlanGwNotifyObjsGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotify3gppRelease"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxWlanGwResrcProblemDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 1)
)
tmnxWlanGwResrcProblemDetected.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblem")
)
if mibBuilder.loadTexts:
    tmnxWlanGwResrcProblemDetected.setStatus(
        "current"
    )

tmnxWlanGwResrcProblemCause = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 2)
)
tmnxWlanGwResrcProblemCause.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxWlanGwResrcProblemCause.setStatus(
        "current"
    )

tmnxWlanGwTuQosProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 3)
)
tmnxWlanGwTuQosProblem.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaMemberTuQosProblem")
)
if mibBuilder.loadTexts:
    tmnxWlanGwTuQosProblem.setStatus(
        "current"
    )

tmnxWlanGwGrpOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 4)
)
tmnxWlanGwGrpOperStateChanged.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperState")
)
if mibBuilder.loadTexts:
    tmnxWlanGwGrpOperStateChanged.setStatus(
        "current"
    )

tmnxWlanGwIomActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 5)
)
tmnxWlanGwIomActive.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomLastMgmtChange"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwIomActive.setStatus(
        "current"
    )

tmnxWlanGwMgwConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 10)
)
tmnxWlanGwMgwConnected.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwTime"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwConnected.setStatus(
        "current"
    )

tmnxWlanGwMgwRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 11)
)
tmnxWlanGwMgwRestarted.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRestartCnt")
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwRestarted.setStatus(
        "current"
    )

tmnxWlanGwNumMgwHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 12)
)
tmnxWlanGwNumMgwHi.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumMgw"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyTrue"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNumMgwHi.setStatus(
        "current"
    )

tmnxWlanGwMgwStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 13)
)
tmnxWlanGwMgwStateChanged.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwState")
)
if mibBuilder.loadTexts:
    tmnxWlanGwMgwStateChanged.setStatus(
        "current"
    )

tmnxWlanGwQosRadiusGtpMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 14)
)
tmnxWlanGwQosRadiusGtpMismatch.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwInterfaceType"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotify3gppRelease"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwQosRadiusGtpMismatch.setStatus(
        "current"
    )

tmnxWlanGwSubIfRedActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 81, 0, 15)
)
tmnxWlanGwSubIfRedActiveChanged.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedActive"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwSubIfRedActiveChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxWlanGwNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 2, 100)
)
tmnxWlanGwNotifyGroup.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblemDetected"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwResrcProblemCause"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwTuQosProblem"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwGrpOperStateChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIomActive"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwConnected"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwRestarted"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNumMgwHi"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwStateChanged"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwQosRadiusGtpMismatch"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSubIfRedActiveChanged"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxWlanGwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 1)
)
tmnxWlanGwCompliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObjGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwCompliance.setStatus(
        "obsolete"
    )

tmnxWlanGwNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 2)
)
tmnxWlanGwNotifyCompliance.setObjects(
    ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxWlanGwNotifyCompliance.setStatus(
        "current"
    )

tmnxWlanGwV10Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 3)
)
tmnxWlanGwV10Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObjGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV10Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV11Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 4)
)
tmnxWlanGwV11Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObjGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV11Compliance.setStatus(
        "obsolete"
    )

tmnxWlanGwV12Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 81, 1, 5)
)
tmnxWlanGwV12Compliance.setObjects(
      *(("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwIsaGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwSoftGreV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwRedGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwV12v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwV11v0Group"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwQosIeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwChargingCharGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMobilityGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwMgwSeHoldTimeGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwDsmGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwUeQryGroup"),
        ("TIMETRA-WLAN-GW-MIB", "tmnxWlanGwObsoletedGroup"))
)
if mibBuilder.loadTexts:
    tmnxWlanGwV12Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-WLAN-GW-MIB",
    **{"TmnxWlanGwBurstSize": TmnxWlanGwBurstSize,
       "TmnxWlanGwIsaIomOperState": TmnxWlanGwIsaIomOperState,
       "TmnxWlanGwMgwInterfaceType": TmnxWlanGwMgwInterfaceType,
       "TmnxWlanGwDsmFilterAction": TmnxWlanGwDsmFilterAction,
       "TmnxWlanGwDsmFilterActionOrNone": TmnxWlanGwDsmFilterActionOrNone,
       "TmnxWlanGwQoSOperState": TmnxWlanGwQoSOperState,
       "TmnxWlanGwUeIdentifier": TmnxWlanGwUeIdentifier,
       "TmnxWlanGwChargingCharBits": TmnxWlanGwChargingCharBits,
       "timetraWlanGwMIBModule": timetraWlanGwMIBModule,
       "tmnxWlanGwConformance": tmnxWlanGwConformance,
       "tmnxWlanGwCompliances": tmnxWlanGwCompliances,
       "tmnxWlanGwCompliance": tmnxWlanGwCompliance,
       "tmnxWlanGwNotifyCompliance": tmnxWlanGwNotifyCompliance,
       "tmnxWlanGwV10Compliance": tmnxWlanGwV10Compliance,
       "tmnxWlanGwV11Compliance": tmnxWlanGwV11Compliance,
       "tmnxWlanGwV12Compliance": tmnxWlanGwV12Compliance,
       "tmnxWlanGwGroups": tmnxWlanGwGroups,
       "tmnxWlanGwIsaGroup": tmnxWlanGwIsaGroup,
       "tmnxWlanGwSoftGreGroup": tmnxWlanGwSoftGreGroup,
       "tmnxWlanGwObjGroup": tmnxWlanGwObjGroup,
       "tmnxWlanGwMgwGroup": tmnxWlanGwMgwGroup,
       "tmnxWlanGwSoftGreV11v0Group": tmnxWlanGwSoftGreV11v0Group,
       "tmnxWlanGwMgwV11v0Group": tmnxWlanGwMgwV11v0Group,
       "tmnxWlanGwMgwQosIeGroup": tmnxWlanGwMgwQosIeGroup,
       "tmnxWlanGwMgwChargingCharGroup": tmnxWlanGwMgwChargingCharGroup,
       "tmnxWlanGwMobilityGroup": tmnxWlanGwMobilityGroup,
       "tmnxWlanGwMgwSeHoldTimeGroup": tmnxWlanGwMgwSeHoldTimeGroup,
       "tmnxWlanGwV12v0Group": tmnxWlanGwV12v0Group,
       "tmnxWlanGwSoftGreV12v0Group": tmnxWlanGwSoftGreV12v0Group,
       "tmnxWlanGwRedGroup": tmnxWlanGwRedGroup,
       "tmnxWlanGwDsmGroup": tmnxWlanGwDsmGroup,
       "tmnxWlanGwUeQryGroup": tmnxWlanGwUeQryGroup,
       "tmnxWlanGwObsoletedGroup": tmnxWlanGwObsoletedGroup,
       "tmnxWlanGwNotifyObjsGroup": tmnxWlanGwNotifyObjsGroup,
       "tmnxWlanGwNotifyGroup": tmnxWlanGwNotifyGroup,
       "tmnxWlanGw": tmnxWlanGw,
       "tmnxWlanGwObjs": tmnxWlanGwObjs,
       "tmnxWlanGwIsaObjs": tmnxWlanGwIsaObjs,
       "tmnxWlanGwGrpTable": tmnxWlanGwGrpTable,
       "tmnxWlanGwGrpEntry": tmnxWlanGwGrpEntry,
       "tmnxWlanGwGrpId": tmnxWlanGwGrpId,
       "tmnxWlanGwGrpRowStatus": tmnxWlanGwGrpRowStatus,
       "tmnxWlanGwGrpLastMgmtChange": tmnxWlanGwGrpLastMgmtChange,
       "tmnxWlanGwGrpDescription": tmnxWlanGwGrpDescription,
       "tmnxWlanGwGrpAdminState": tmnxWlanGwGrpAdminState,
       "tmnxWlanGwGrpActiveIomLimit": tmnxWlanGwGrpActiveIomLimit,
       "tmnxWlanGwGrpPortPlcy": tmnxWlanGwGrpPortPlcy,
       "tmnxWlanGwGrpTunnelPortPlcy": tmnxWlanGwGrpTunnelPortPlcy,
       "tmnxWlanGwGrpIsaAaGroup": tmnxWlanGwGrpIsaAaGroup,
       "tmnxWlanGwGrpOperState": tmnxWlanGwGrpOperState,
       "tmnxWlanGwGrpDegraded": tmnxWlanGwGrpDegraded,
       "tmnxWlanGwIomTable": tmnxWlanGwIomTable,
       "tmnxWlanGwIomEntry": tmnxWlanGwIomEntry,
       "tmnxWlanGwIomRowStatus": tmnxWlanGwIomRowStatus,
       "tmnxWlanGwIomLastMgmtChange": tmnxWlanGwIomLastMgmtChange,
       "tmnxWlanGwIomOperState": tmnxWlanGwIomOperState,
       "tmnxWlanGwIsaMemberTable": tmnxWlanGwIsaMemberTable,
       "tmnxWlanGwIsaMemberEntry": tmnxWlanGwIsaMemberEntry,
       "tmnxWlanGwIsaMemberId": tmnxWlanGwIsaMemberId,
       "tmnxWlanGwIsaMemberChassisIndex": tmnxWlanGwIsaMemberChassisIndex,
       "tmnxWlanGwIsaMemberCardSlotNum": tmnxWlanGwIsaMemberCardSlotNum,
       "tmnxWlanGwIsaMemberSlotNum": tmnxWlanGwIsaMemberSlotNum,
       "tmnxWlanGwIsaMemberNumSoftGreTu": tmnxWlanGwIsaMemberNumSoftGreTu,
       "tmnxWlanGwIsaMemberNumUe": tmnxWlanGwIsaMemberNumUe,
       "tmnxWlanGwIsaMemberEegMemberAct": tmnxWlanGwIsaMemberEegMemberAct,
       "tmnxWlanGwIsaMemberEegMemberPend": tmnxWlanGwIsaMemberEegMemberPend,
       "tmnxWlanGwIsaMemberTuQosProblem": tmnxWlanGwIsaMemberTuQosProblem,
       "tmnxWlanGwIsaMemberStatsTable": tmnxWlanGwIsaMemberStatsTable,
       "tmnxWlanGwIsaMemberStatsEntry": tmnxWlanGwIsaMemberStatsEntry,
       "tmnxWlanGwIsaMemberStatsType": tmnxWlanGwIsaMemberStatsType,
       "tmnxWlanGwIsaMemberStatsName": tmnxWlanGwIsaMemberStatsName,
       "tmnxWlanGwIsaMemberStatsVal": tmnxWlanGwIsaMemberStatsVal,
       "tmnxWlanGwIsaMemberStatsValHw": tmnxWlanGwIsaMemberStatsValHw,
       "tmnxWlanGwIsaMemberStatsValue": tmnxWlanGwIsaMemberStatsValue,
       "tmnxWlanGwSoftGreObjs": tmnxWlanGwSoftGreObjs,
       "tmnxWlanGwSoftGreIfTable": tmnxWlanGwSoftGreIfTable,
       "tmnxWlanGwSoftGreIfEntry": tmnxWlanGwSoftGreIfEntry,
       "tmnxWlanGwSoftGreIfLastCh": tmnxWlanGwSoftGreIfLastCh,
       "tmnxWlanGwSoftGreIfAdminState": tmnxWlanGwSoftGreIfAdminState,
       "tmnxWlanGwSoftGreIfRouter": tmnxWlanGwSoftGreIfRouter,
       "tmnxWlanGwSoftGreIfGwAddrType": tmnxWlanGwSoftGreIfGwAddrType,
       "tmnxWlanGwSoftGreIfGwAddr": tmnxWlanGwSoftGreIfGwAddr,
       "tmnxWlanGwSoftGreIfGrpId": tmnxWlanGwSoftGreIfGrpId,
       "tmnxWlanGwSoftGreIfShapingType": tmnxWlanGwSoftGreIfShapingType,
       "tmnxWlanGwSoftGreIfShapeMultiUe": tmnxWlanGwSoftGreIfShapeMultiUe,
       "tmnxWlanGwSoftGreIfEQosPlcy": tmnxWlanGwSoftGreIfEQosPlcy,
       "tmnxWlanGwSoftGreIfESchedPlcy": tmnxWlanGwSoftGreIfESchedPlcy,
       "tmnxWlanGwSoftGreIfEAggRateLimit": tmnxWlanGwSoftGreIfEAggRateLimit,
       "tmnxWlanGwSoftGreIfMobTrigger": tmnxWlanGwSoftGreIfMobTrigger,
       "tmnxWlanGwSoftGreIfMobHoldTime": tmnxWlanGwSoftGreIfMobHoldTime,
       "tmnxWlanGwSoftGreIfDefRetailSvc": tmnxWlanGwSoftGreIfDefRetailSvc,
       "tmnxWlanGwSoftGreIfTcpMssAdjust": tmnxWlanGwSoftGreIfTcpMssAdjust,
       "tmnxWlanGwSoftGreIfEHoldTime": tmnxWlanGwSoftGreIfEHoldTime,
       "tmnxWlanGwSoftGreIfDataTrigg": tmnxWlanGwSoftGreIfDataTrigg,
       "tmnxWlanGwSoftGreIfAuthPlcy": tmnxWlanGwSoftGreIfAuthPlcy,
       "tmnxWlanGwSoftGreIfAuthHoldTime": tmnxWlanGwSoftGreIfAuthHoldTime,
       "tmnxWlanGwSoftGreIfRadProxVrtr": tmnxWlanGwSoftGreIfRadProxVrtr,
       "tmnxWlanGwSoftGreIfRadProxSrv": tmnxWlanGwSoftGreIfRadProxSrv,
       "tmnxWlanGwSoftGreIfRadProxMacFmt": tmnxWlanGwSoftGreIfRadProxMacFmt,
       "tmnxWlanGwSoftGreIfGwV6AddrType": tmnxWlanGwSoftGreIfGwV6AddrType,
       "tmnxWlanGwSoftGreIfGwV6Addr": tmnxWlanGwSoftGreIfGwV6Addr,
       "tmnxWlanGwSoftGreIfMobArpAp": tmnxWlanGwSoftGreIfMobArpAp,
       "tmnxWlanGwSoftGreIfDownIfGrpDeg": tmnxWlanGwSoftGreIfDownIfGrpDeg,
       "tmnxWlanGwSoftGreIfNumSoftGreTu": tmnxWlanGwSoftGreIfNumSoftGreTu,
       "tmnxWlanGwSoftGreTuTable": tmnxWlanGwSoftGreTuTable,
       "tmnxWlanGwSoftGreTuEntry": tmnxWlanGwSoftGreTuEntry,
       "tmnxWlanGwSoftGreTuRemoteAddrTyp": tmnxWlanGwSoftGreTuRemoteAddrTyp,
       "tmnxWlanGwSoftGreTuRemoteAddr": tmnxWlanGwSoftGreTuRemoteAddr,
       "tmnxWlanGwSoftGreTuLocalAddrType": tmnxWlanGwSoftGreTuLocalAddrType,
       "tmnxWlanGwSoftGreTuLocalAddr": tmnxWlanGwSoftGreTuLocalAddr,
       "tmnxWlanGwSoftGreTuEstabTime": tmnxWlanGwSoftGreTuEstabTime,
       "tmnxWlanGwSoftGreTuIsaGroup": tmnxWlanGwSoftGreTuIsaGroup,
       "tmnxWlanGwSoftGreTuIsaMember": tmnxWlanGwSoftGreTuIsaMember,
       "tmnxWlanGwSoftGreTuNumUe": tmnxWlanGwSoftGreTuNumUe,
       "tmnxWlanGwSoftGreTuApMacAddress": tmnxWlanGwSoftGreTuApMacAddress,
       "tmnxWlanGwSoftGreTuApLearnFailed": tmnxWlanGwSoftGreTuApLearnFailed,
       "tmnxWlanGwTuQosTable": tmnxWlanGwTuQosTable,
       "tmnxWlanGwTuQosEntry": tmnxWlanGwTuQosEntry,
       "tmnxWlanGwTuQosRetailService": tmnxWlanGwTuQosRetailService,
       "tmnxWlanGwTuQosEegSvcId": tmnxWlanGwTuQosEegSvcId,
       "tmnxWlanGwTuQosEegPortId": tmnxWlanGwTuQosEegPortId,
       "tmnxWlanGwTuQosEegEncapValue": tmnxWlanGwTuQosEegEncapValue,
       "tmnxWlanGwTuQosEegName": tmnxWlanGwTuQosEegName,
       "tmnxWlanGwTuQosEegMember": tmnxWlanGwTuQosEegMember,
       "tmnxWlanGwTuQosState": tmnxWlanGwTuQosState,
       "tmnxWlanGwTuQosNumUe": tmnxWlanGwTuQosNumUe,
       "tmnxWlanGwTuQosRemainingHoldTime": tmnxWlanGwTuQosRemainingHoldTime,
       "tmnxWlanGwSoftGreTuUeTable": tmnxWlanGwSoftGreTuUeTable,
       "tmnxWlanGwSoftGreTuUeEntry": tmnxWlanGwSoftGreTuUeEntry,
       "tmnxWlanGwSoftGreTuUeSsid": tmnxWlanGwSoftGreTuUeSsid,
       "tmnxWlanGwSoftGreXtTable": tmnxWlanGwSoftGreXtTable,
       "tmnxWlanGwSoftGreXtEntry": tmnxWlanGwSoftGreXtEntry,
       "tmnxWlanGwSoftGreXtLastCh": tmnxWlanGwSoftGreXtLastCh,
       "tmnxWlanGwSoftGreXtDhcp": tmnxWlanGwSoftGreXtDhcp,
       "tmnxWlanGwSoftGreXtAddrType": tmnxWlanGwSoftGreXtAddrType,
       "tmnxWlanGwSoftGreXtAddr": tmnxWlanGwSoftGreXtAddr,
       "tmnxWlanGwSoftGreXtLeaseTime": tmnxWlanGwSoftGreXtLeaseTime,
       "tmnxWlanGwSoftGreXtActLeaseTime": tmnxWlanGwSoftGreXtActLeaseTime,
       "tmnxWlanGwSoftGreXtDns1AddrType": tmnxWlanGwSoftGreXtDns1AddrType,
       "tmnxWlanGwSoftGreXtDns1Addr": tmnxWlanGwSoftGreXtDns1Addr,
       "tmnxWlanGwSoftGreXtDns2AddrType": tmnxWlanGwSoftGreXtDns2AddrType,
       "tmnxWlanGwSoftGreXtDns2Addr": tmnxWlanGwSoftGreXtDns2Addr,
       "tmnxWlanGwSoftGreXtNb1AddrType": tmnxWlanGwSoftGreXtNb1AddrType,
       "tmnxWlanGwSoftGreXtNb1Addr": tmnxWlanGwSoftGreXtNb1Addr,
       "tmnxWlanGwSoftGreXtNb2AddrType": tmnxWlanGwSoftGreXtNb2AddrType,
       "tmnxWlanGwSoftGreXtNb2Addr": tmnxWlanGwSoftGreXtNb2Addr,
       "tmnxWlanGwSoftGreXtHttpRdrPlcy": tmnxWlanGwSoftGreXtHttpRdrPlcy,
       "tmnxWlanGwSoftGreXtNatPlcy": tmnxWlanGwSoftGreXtNatPlcy,
       "tmnxWlanGwVlanTable": tmnxWlanGwVlanTable,
       "tmnxWlanGwVlanEntry": tmnxWlanGwVlanEntry,
       "tmnxWlanGwVlanTagStart": tmnxWlanGwVlanTagStart,
       "tmnxWlanGwVlanTagEnd": tmnxWlanGwVlanTagEnd,
       "tmnxWlanGwVlanRowStatus": tmnxWlanGwVlanRowStatus,
       "tmnxWlanGwVlanLastCh": tmnxWlanGwVlanLastCh,
       "tmnxWlanGwVlanRetailService": tmnxWlanGwVlanRetailService,
       "tmnxWlanGwVlanDhcp": tmnxWlanGwVlanDhcp,
       "tmnxWlanGwVlanAddrType": tmnxWlanGwVlanAddrType,
       "tmnxWlanGwVlanAddr": tmnxWlanGwVlanAddr,
       "tmnxWlanGwVlanLeaseTime": tmnxWlanGwVlanLeaseTime,
       "tmnxWlanGwVlanActLeaseTime": tmnxWlanGwVlanActLeaseTime,
       "tmnxWlanGwVlanDns1AddrType": tmnxWlanGwVlanDns1AddrType,
       "tmnxWlanGwVlanDns1Addr": tmnxWlanGwVlanDns1Addr,
       "tmnxWlanGwVlanDns2AddrType": tmnxWlanGwVlanDns2AddrType,
       "tmnxWlanGwVlanDns2Addr": tmnxWlanGwVlanDns2Addr,
       "tmnxWlanGwVlanNb1AddrType": tmnxWlanGwVlanNb1AddrType,
       "tmnxWlanGwVlanNb1Addr": tmnxWlanGwVlanNb1Addr,
       "tmnxWlanGwVlanNb2AddrType": tmnxWlanGwVlanNb2AddrType,
       "tmnxWlanGwVlanNb2Addr": tmnxWlanGwVlanNb2Addr,
       "tmnxWlanGwVlanHttpRdrPlcy": tmnxWlanGwVlanHttpRdrPlcy,
       "tmnxWlanGwVlanNatPlcy": tmnxWlanGwVlanNatPlcy,
       "tmnxWlanGwVlanDataTrigg": tmnxWlanGwVlanDataTrigg,
       "tmnxWlanGwVlanAuthPlcy": tmnxWlanGwVlanAuthPlcy,
       "tmnxWlanGwVlanAuthHoldTime": tmnxWlanGwVlanAuthHoldTime,
       "tmnxWlanGwVlanRadProxVrtr": tmnxWlanGwVlanRadProxVrtr,
       "tmnxWlanGwVlanRadProxSrv": tmnxWlanGwVlanRadProxSrv,
       "tmnxWlanGwVlanRadProxMacFmt": tmnxWlanGwVlanRadProxMacFmt,
       "tmnxWlanGwVlanAuthOnDhcp": tmnxWlanGwVlanAuthOnDhcp,
       "tmnxWlanGwSubIfTable": tmnxWlanGwSubIfTable,
       "tmnxWlanGwSubIfEntry": tmnxWlanGwSubIfEntry,
       "tmnxWlanGwSubIfRowStatus": tmnxWlanGwSubIfRowStatus,
       "tmnxWlanGwSubIfLastCh": tmnxWlanGwSubIfLastCh,
       "tmnxWlanGwSubIfRedExpPrefixType": tmnxWlanGwSubIfRedExpPrefixType,
       "tmnxWlanGwSubIfRedExpPrefix": tmnxWlanGwSubIfRedExpPrefix,
       "tmnxWlanGwSubIfRedExpPrefixLen": tmnxWlanGwSubIfRedExpPrefixLen,
       "tmnxWlanGwSubIfRedMonPrefixType": tmnxWlanGwSubIfRedMonPrefixType,
       "tmnxWlanGwSubIfRedMonPrefix": tmnxWlanGwSubIfRedMonPrefix,
       "tmnxWlanGwSubIfRedMonPrefixLen": tmnxWlanGwSubIfRedMonPrefixLen,
       "tmnxWlanGwSubIfRedAdminState": tmnxWlanGwSubIfRedAdminState,
       "tmnxWlanGwSubIfRedActive": tmnxWlanGwSubIfRedActive,
       "tmnxWlanGwSubIfRedSwitch": tmnxWlanGwSubIfRedSwitch,
       "tmnxWlanGwIfRetailTable": tmnxWlanGwIfRetailTable,
       "tmnxWlanGwIfRetailEntry": tmnxWlanGwIfRetailEntry,
       "tmnxWlanGwIfRetailTagStart": tmnxWlanGwIfRetailTagStart,
       "tmnxWlanGwIfRetailTagEnd": tmnxWlanGwIfRetailTagEnd,
       "tmnxWlanGwIfRetailRowStatus": tmnxWlanGwIfRetailRowStatus,
       "tmnxWlanGwIfRetailLastCh": tmnxWlanGwIfRetailLastCh,
       "tmnxWlanGwIfRetailService": tmnxWlanGwIfRetailService,
       "tmnxWlanGwUeTable": tmnxWlanGwUeTable,
       "tmnxWlanGwUeEntry": tmnxWlanGwUeEntry,
       "tmnxWlanGwUeMacAddress": tmnxWlanGwUeMacAddress,
       "tmnxWlanGwUeQTag": tmnxWlanGwUeQTag,
       "tmnxWlanGwUeMplsLabel": tmnxWlanGwUeMplsLabel,
       "tmnxWlanGwUeTuRouter": tmnxWlanGwUeTuRouter,
       "tmnxWlanGwUeTuAddrType": tmnxWlanGwUeTuAddrType,
       "tmnxWlanGwUeTuRemoteAddr": tmnxWlanGwUeTuRemoteAddr,
       "tmnxWlanGwUeTuLocalAddr": tmnxWlanGwUeTuLocalAddr,
       "tmnxWlanGwUeTuQosRetailService": tmnxWlanGwUeTuQosRetailService,
       "tmnxWlanGwUeSsid": tmnxWlanGwUeSsid,
       "tmnxWlanGwUePrevApAddrType": tmnxWlanGwUePrevApAddrType,
       "tmnxWlanGwUePrevApAddr": tmnxWlanGwUePrevApAddr,
       "tmnxWlanGwUeLastMoveTime": tmnxWlanGwUeLastMoveTime,
       "tmnxWlanGwUeImsi": tmnxWlanGwUeImsi,
       "tmnxWlanGwSsidTable": tmnxWlanGwSsidTable,
       "tmnxWlanGwSsidEntry": tmnxWlanGwSsidEntry,
       "tmnxWlanGwSsid": tmnxWlanGwSsid,
       "tmnxWlanGwSsidNumUe": tmnxWlanGwSsidNumUe,
       "tmnxWlanGwMgwObjs": tmnxWlanGwMgwObjs,
       "tmnxWlanGwMgwProfTable": tmnxWlanGwMgwProfTable,
       "tmnxWlanGwMgwProfEntry": tmnxWlanGwMgwProfEntry,
       "tmnxWlanGwMgwProfName": tmnxWlanGwMgwProfName,
       "tmnxWlanGwMgwProfRowStatus": tmnxWlanGwMgwProfRowStatus,
       "tmnxWlanGwMgwProfLastChanged": tmnxWlanGwMgwProfLastChanged,
       "tmnxWlanGwMgwProfDescription": tmnxWlanGwMgwProfDescription,
       "tmnxWlanGwMgwProfMsgReTxTimeout": tmnxWlanGwMgwProfMsgReTxTimeout,
       "tmnxWlanGwMgwProfMsgReTxRetryCnt": tmnxWlanGwMgwProfMsgReTxRetryCnt,
       "tmnxWlanGwMgwProfKeepAlvTimeout": tmnxWlanGwMgwProfKeepAlvTimeout,
       "tmnxWlanGwMgwProfKeepAlvRetryCnt": tmnxWlanGwMgwProfKeepAlvRetryCnt,
       "tmnxWlanGwMgwProfKeepAlvResp": tmnxWlanGwMgwProfKeepAlvResp,
       "tmnxWlanGwMgwProfTtl": tmnxWlanGwMgwProfTtl,
       "tmnxWlanGwMgwProfInterfaceType": tmnxWlanGwMgwProfInterfaceType,
       "tmnxWlanGwMgwProfChrgCharHome": tmnxWlanGwMgwProfChrgCharHome,
       "tmnxWlanGwMgwProfChrgCharRoam": tmnxWlanGwMgwProfChrgCharRoam,
       "tmnxWlanGwMgwProfSeHoldTime": tmnxWlanGwMgwProfSeHoldTime,
       "tmnxWlanGwMgwProfReportWlanLoc": tmnxWlanGwMgwProfReportWlanLoc,
       "tmnxWlanGwMgwProfProtocolCfgOpt": tmnxWlanGwMgwProfProtocolCfgOpt,
       "tmnxWlanGwMgwAddrTable": tmnxWlanGwMgwAddrTable,
       "tmnxWlanGwMgwAddrEntry": tmnxWlanGwMgwAddrEntry,
       "tmnxWlanGwMgwAddrType": tmnxWlanGwMgwAddrType,
       "tmnxWlanGwMgwAddr": tmnxWlanGwMgwAddr,
       "tmnxWlanGwMgwAddrPrefixLen": tmnxWlanGwMgwAddrPrefixLen,
       "tmnxWlanGwMgwAddrRowStatus": tmnxWlanGwMgwAddrRowStatus,
       "tmnxWlanGwMgwAddrLastMgmtChange": tmnxWlanGwMgwAddrLastMgmtChange,
       "tmnxWlanGwMgwAddrProfile": tmnxWlanGwMgwAddrProfile,
       "tmnxWlanGwMgwTable": tmnxWlanGwMgwTable,
       "tmnxWlanGwMgwEntry": tmnxWlanGwMgwEntry,
       "tmnxWlanGwMgwRemoteAddrType": tmnxWlanGwMgwRemoteAddrType,
       "tmnxWlanGwMgwRemoteAddr": tmnxWlanGwMgwRemoteAddr,
       "tmnxWlanGwMgwRemotePort": tmnxWlanGwMgwRemotePort,
       "tmnxWlanGwMgwLocalAddrType": tmnxWlanGwMgwLocalAddrType,
       "tmnxWlanGwMgwLocalAddr": tmnxWlanGwMgwLocalAddr,
       "tmnxWlanGwMgwTime": tmnxWlanGwMgwTime,
       "tmnxWlanGwMgwProfile": tmnxWlanGwMgwProfile,
       "tmnxWlanGwMgwControl": tmnxWlanGwMgwControl,
       "tmnxWlanGwMgwRestartCnt": tmnxWlanGwMgwRestartCnt,
       "tmnxWlanGwMgwState": tmnxWlanGwMgwState,
       "tmnxWlanGwMgwInterfaceType": tmnxWlanGwMgwInterfaceType,
       "tmnxWlanMgwStatsTable": tmnxWlanMgwStatsTable,
       "tmnxWlanMgwStatsEntry": tmnxWlanMgwStatsEntry,
       "tmnxWlanMgwStatsId": tmnxWlanMgwStatsId,
       "tmnxWlanMgwStatsName": tmnxWlanMgwStatsName,
       "tmnxWlanMgwStatsVal": tmnxWlanMgwStatsVal,
       "tmnxWlanMgwStatsValLw": tmnxWlanMgwStatsValLw,
       "tmnxWlanMgwStatsValHw": tmnxWlanMgwStatsValHw,
       "tmnxWlanGwGtpSeTable": tmnxWlanGwGtpSeTable,
       "tmnxWlanGwGtpSeEntry": tmnxWlanGwGtpSeEntry,
       "tmnxWlanGwGtpSeImsi": tmnxWlanGwGtpSeImsi,
       "tmnxWlanGwGtpSeApn": tmnxWlanGwGtpSeApn,
       "tmnxWlanGwGtpSeMgwRouter": tmnxWlanGwGtpSeMgwRouter,
       "tmnxWlanGwGtpSeMgwAddrType": tmnxWlanGwGtpSeMgwAddrType,
       "tmnxWlanGwGtpSeMgwAddr": tmnxWlanGwGtpSeMgwAddr,
       "tmnxWlanGwGtpSeRemoteCtrlTeid": tmnxWlanGwGtpSeRemoteCtrlTeid,
       "tmnxWlanGwGtpSeLocalCtrlTeid": tmnxWlanGwGtpSeLocalCtrlTeid,
       "tmnxWlanGwGtpSeChrgChar": tmnxWlanGwGtpSeChrgChar,
       "tmnxWlanGwBcTable": tmnxWlanGwBcTable,
       "tmnxWlanGwBcEntry": tmnxWlanGwBcEntry,
       "tmnxWlanGwBcId": tmnxWlanGwBcId,
       "tmnxWlanGwBcRemoteTeid": tmnxWlanGwBcRemoteTeid,
       "tmnxWlanGwBcLocalTeid": tmnxWlanGwBcLocalTeid,
       "tmnxWlanGwBcQosUlGbr": tmnxWlanGwBcQosUlGbr,
       "tmnxWlanGwBcQosUlMbr": tmnxWlanGwBcQosUlMbr,
       "tmnxWlanGwBcQosDlGbr": tmnxWlanGwBcQosDlGbr,
       "tmnxWlanGwBcQosDlMbr": tmnxWlanGwBcQosDlMbr,
       "tmnxWlanGwBcQosQci": tmnxWlanGwBcQosQci,
       "tmnxWlanGwBcQosArp": tmnxWlanGwBcQosArp,
       "tmnxWlanGwMgwCacheTable": tmnxWlanGwMgwCacheTable,
       "tmnxWlanGwMgwCacheEntry": tmnxWlanGwMgwCacheEntry,
       "tmnxWlanGwMgwCacheApn": tmnxWlanGwMgwCacheApn,
       "tmnxWlanGwMgwCacheAddrType": tmnxWlanGwMgwCacheAddrType,
       "tmnxWlanGwMgwCacheAddr": tmnxWlanGwMgwCacheAddr,
       "tmnxWlanGwMgwCacheTtl": tmnxWlanGwMgwCacheTtl,
       "tmnxWlanGwGtpStatsTable": tmnxWlanGwGtpStatsTable,
       "tmnxWlanGwGtpStatsEntry": tmnxWlanGwGtpStatsEntry,
       "tmnxWlanGwGtpStatsId": tmnxWlanGwGtpStatsId,
       "tmnxWlanGwGtpStatsName": tmnxWlanGwGtpStatsName,
       "tmnxWlanGwGtpStatsVal": tmnxWlanGwGtpStatsVal,
       "tmnxWlanGwGtpStatsValLw": tmnxWlanGwGtpStatsValLw,
       "tmnxWlanGwGtpStatsValHw": tmnxWlanGwGtpStatsValHw,
       "tmnxWlanGwMgwArecCacheTable": tmnxWlanGwMgwArecCacheTable,
       "tmnxWlanGwMgwArecCacheEntry": tmnxWlanGwMgwArecCacheEntry,
       "tmnxWlanGwMgwArecCacheApn": tmnxWlanGwMgwArecCacheApn,
       "tmnxWlanGwMgwArecCacheIndex": tmnxWlanGwMgwArecCacheIndex,
       "tmnxWlanGwMgwArecCacheAddrType": tmnxWlanGwMgwArecCacheAddrType,
       "tmnxWlanGwMgwArecCacheAddr": tmnxWlanGwMgwArecCacheAddr,
       "tmnxWlanGwMgwArecCacheTtl": tmnxWlanGwMgwArecCacheTtl,
       "tmnxWlanGwMgwSnaptrCacheTable": tmnxWlanGwMgwSnaptrCacheTable,
       "tmnxWlanGwMgwSnaptrCacheEntry": tmnxWlanGwMgwSnaptrCacheEntry,
       "tmnxWlanGwMgwSnaptrCacheApn": tmnxWlanGwMgwSnaptrCacheApn,
       "tmnxWlanGwMgwSnaptrCacheOrder": tmnxWlanGwMgwSnaptrCacheOrder,
       "tmnxWlanGwMgwSnaptrCacheIndex": tmnxWlanGwMgwSnaptrCacheIndex,
       "tmnxWlanGwMgwSnaptrCachePref": tmnxWlanGwMgwSnaptrCachePref,
       "tmnxWlanGwMgwSnaptrCacheService": tmnxWlanGwMgwSnaptrCacheService,
       "tmnxWlanGwMgwSnaptrCacheNext": tmnxWlanGwMgwSnaptrCacheNext,
       "tmnxWlanGwMgwSnaptrCacheRepl": tmnxWlanGwMgwSnaptrCacheRepl,
       "tmnxWlanGwMgwSnaptrCacheTtl": tmnxWlanGwMgwSnaptrCacheTtl,
       "tmnxWlanGwMgwSrvCacheTable": tmnxWlanGwMgwSrvCacheTable,
       "tmnxWlanGwMgwSrvCacheEntry": tmnxWlanGwMgwSrvCacheEntry,
       "tmnxWlanGwMgwSrvCacheApn": tmnxWlanGwMgwSrvCacheApn,
       "tmnxWlanGwMgwSrvCachePriority": tmnxWlanGwMgwSrvCachePriority,
       "tmnxWlanGwMgwSrvCacheIndex": tmnxWlanGwMgwSrvCacheIndex,
       "tmnxWlanGwMgwSrvCacheWeight": tmnxWlanGwMgwSrvCacheWeight,
       "tmnxWlanGwMgwSrvCachePort": tmnxWlanGwMgwSrvCachePort,
       "tmnxWlanGwMgwSrvCacheTarget": tmnxWlanGwMgwSrvCacheTarget,
       "tmnxWlanGwMgwSrvCacheTtl": tmnxWlanGwMgwSrvCacheTtl,
       "tmnxWlanGwPgwTable": tmnxWlanGwPgwTable,
       "tmnxWlanGwPgwEntry": tmnxWlanGwPgwEntry,
       "tmnxWlanGwPgwLastChanged": tmnxWlanGwPgwLastChanged,
       "tmnxWlanGwPgwQosUplinkGbrRate": tmnxWlanGwPgwQosUplinkGbrRate,
       "tmnxWlanGwPgwQosUplinkMbrRate": tmnxWlanGwPgwQosUplinkMbrRate,
       "tmnxWlanGwPgwQosDwnlinkGbrRate": tmnxWlanGwPgwQosDwnlinkGbrRate,
       "tmnxWlanGwPgwQosDwnlinkMbrRate": tmnxWlanGwPgwQosDwnlinkMbrRate,
       "tmnxWlanGwPgwQosArpValue": tmnxWlanGwPgwQosArpValue,
       "tmnxWlanGwPgwQosQciValue": tmnxWlanGwPgwQosQciValue,
       "tmnxWlanGwGgsnTable": tmnxWlanGwGgsnTable,
       "tmnxWlanGwGgsnEntry": tmnxWlanGwGgsnEntry,
       "tmnxWlanGwGgsnLastChanged": tmnxWlanGwGgsnLastChanged,
       "tmnxWlanGwGgsnQosUplinkGbrRate": tmnxWlanGwGgsnQosUplinkGbrRate,
       "tmnxWlanGwGgsnQosUplinkMbrRate": tmnxWlanGwGgsnQosUplinkMbrRate,
       "tmnxWlanGwGgsnQosDwnlinkGbrRate": tmnxWlanGwGgsnQosDwnlinkGbrRate,
       "tmnxWlanGwGgsnQosDwnlinkMbrRate": tmnxWlanGwGgsnQosDwnlinkMbrRate,
       "tmnxWlanGwGgsnQosArpValue": tmnxWlanGwGgsnQosArpValue,
       "tmnxWlanGwSysCfgObjs": tmnxWlanGwSysCfgObjs,
       "tmnxWlanGwSysCfgServingNwMcc": tmnxWlanGwSysCfgServingNwMcc,
       "tmnxWlanGwSysCfgServingNwMnc": tmnxWlanGwSysCfgServingNwMnc,
       "tmnxWlanGwSysCfgMgwMaxHeldSe": tmnxWlanGwSysCfgMgwMaxHeldSe,
       "tmnxWlanGwTable": tmnxWlanGwTable,
       "tmnxWlanGwEntry": tmnxWlanGwEntry,
       "tmnxWlanGwRowStatus": tmnxWlanGwRowStatus,
       "tmnxWlanGwLastCh": tmnxWlanGwLastCh,
       "tmnxWlanGwApn": tmnxWlanGwApn,
       "tmnxWlanGwMobAcctInterimUpdate": tmnxWlanGwMobAcctInterimUpdate,
       "tmnxWlanGwDsmSubObjs": tmnxWlanGwDsmSubObjs,
       "tmnxWlanGwVlanDsmTable": tmnxWlanGwVlanDsmTable,
       "tmnxWlanGwVlanDsmEntry": tmnxWlanGwVlanDsmEntry,
       "tmnxWlanGwVlanDsmLastCh": tmnxWlanGwVlanDsmLastCh,
       "tmnxWlanGwVlanDsmAdminState": tmnxWlanGwVlanDsmAdminState,
       "tmnxWlanGwVlanDsmAcctPlcy": tmnxWlanGwVlanDsmAcctPlcy,
       "tmnxWlanGwVlanDsmEgressPolicer": tmnxWlanGwVlanDsmEgressPolicer,
       "tmnxWlanGwVlanDsmIngressPolicer": tmnxWlanGwVlanDsmIngressPolicer,
       "tmnxWlanGwVlanDsmIpFilter": tmnxWlanGwVlanDsmIpFilter,
       "tmnxWlanGwVlanDsmOneTimeRdrUrl": tmnxWlanGwVlanDsmOneTimeRdrUrl,
       "tmnxWlanGwVlanDsmOneTimeRdrPort": tmnxWlanGwVlanDsmOneTimeRdrPort,
       "tmnxWlanGwVlanDsmAcctUpdInterv": tmnxWlanGwVlanDsmAcctUpdInterv,
       "tmnxWlanGwVlanDsmDefAppProfile": tmnxWlanGwVlanDsmDefAppProfile,
       "tmnxWlanGwDsmIpFilTable": tmnxWlanGwDsmIpFilTable,
       "tmnxWlanGwDsmIpFilEntry": tmnxWlanGwDsmIpFilEntry,
       "tmnxWlanGwDsmIpFilName": tmnxWlanGwDsmIpFilName,
       "tmnxWlanGwDsmIpFilRowStatus": tmnxWlanGwDsmIpFilRowStatus,
       "tmnxWlanGwDsmIpFilLastCh": tmnxWlanGwDsmIpFilLastCh,
       "tmnxWlanGwDsmIpFilDescription": tmnxWlanGwDsmIpFilDescription,
       "tmnxWlanGwDsmIpFilDefaultAction": tmnxWlanGwDsmIpFilDefaultAction,
       "tmnxWlanGwDsmIpFilN3Table": tmnxWlanGwDsmIpFilN3Table,
       "tmnxWlanGwDsmIpFilN3Entry": tmnxWlanGwDsmIpFilN3Entry,
       "tmnxWlanGwDsmIpFilN3Index": tmnxWlanGwDsmIpFilN3Index,
       "tmnxWlanGwDsmIpFilN3RowStatus": tmnxWlanGwDsmIpFilN3RowStatus,
       "tmnxWlanGwDsmIpFilN3LastCh": tmnxWlanGwDsmIpFilN3LastCh,
       "tmnxWlanGwDsmIpFilN3Description": tmnxWlanGwDsmIpFilN3Description,
       "tmnxWlanGwDsmIpFilN3Action": tmnxWlanGwDsmIpFilN3Action,
       "tmnxWlanGwDsmIpFilN3Protocol": tmnxWlanGwDsmIpFilN3Protocol,
       "tmnxWlanGwDsmIpFilN3DestAddrType": tmnxWlanGwDsmIpFilN3DestAddrType,
       "tmnxWlanGwDsmIpFilN3DestAddr": tmnxWlanGwDsmIpFilN3DestAddr,
       "tmnxWlanGwDsmIpFilN3DestPrefLen": tmnxWlanGwDsmIpFilN3DestPrefLen,
       "tmnxWlanGwDsmIpFilN3DestPortOp": tmnxWlanGwDsmIpFilN3DestPortOp,
       "tmnxWlanGwDsmIpFilN3DestPort1": tmnxWlanGwDsmIpFilN3DestPort1,
       "tmnxWlanGwPolicerTable": tmnxWlanGwPolicerTable,
       "tmnxWlanGwPolicerEntry": tmnxWlanGwPolicerEntry,
       "tmnxWlanGwPolicerName": tmnxWlanGwPolicerName,
       "tmnxWlanGwPolicerRowLastChange": tmnxWlanGwPolicerRowLastChange,
       "tmnxWlanGwPolicerRowStatus": tmnxWlanGwPolicerRowStatus,
       "tmnxWlanGwPolicerDescription": tmnxWlanGwPolicerDescription,
       "tmnxWlanGwPolicerType": tmnxWlanGwPolicerType,
       "tmnxWlanGwPolicerAction": tmnxWlanGwPolicerAction,
       "tmnxWlanGwPolicerAdminPIR": tmnxWlanGwPolicerAdminPIR,
       "tmnxWlanGwPolicerAdminCIR": tmnxWlanGwPolicerAdminCIR,
       "tmnxWlanGwPolicerMBS": tmnxWlanGwPolicerMBS,
       "tmnxWlanGwPolicerCBS": tmnxWlanGwPolicerCBS,
       "tmnxWlanGwPolicerPIRAdaptation": tmnxWlanGwPolicerPIRAdaptation,
       "tmnxWlanGwPolicerCIRAdaptation": tmnxWlanGwPolicerCIRAdaptation,
       "tmnxWlanGwUeObjs": tmnxWlanGwUeObjs,
       "tmnxWlanGwUeNextQryId": tmnxWlanGwUeNextQryId,
       "tmnxWlanGwUeMaxQryId": tmnxWlanGwUeMaxQryId,
       "tmnxWlanGwUeQryTable": tmnxWlanGwUeQryTable,
       "tmnxWlanGwUeQryEntry": tmnxWlanGwUeQryEntry,
       "tmnxWlanGwUeQryId": tmnxWlanGwUeQryId,
       "tmnxWlanGwUeQryRowStatus": tmnxWlanGwUeQryRowStatus,
       "tmnxWlanGwUeQryWhereState": tmnxWlanGwUeQryWhereState,
       "tmnxWlanGwUeQryWhereMacAddress": tmnxWlanGwUeQryWhereMacAddress,
       "tmnxWlanGwUeQryWhereAddrType": tmnxWlanGwUeQryWhereAddrType,
       "tmnxWlanGwUeQryWhereAddr": tmnxWlanGwUeQryWhereAddr,
       "tmnxWlanGwUeQryWhereIsaGrp": tmnxWlanGwUeQryWhereIsaGrp,
       "tmnxWlanGwUeQryWhereMemberId": tmnxWlanGwUeQryWhereMemberId,
       "tmnxWlanGwUeQryWhereQTag": tmnxWlanGwUeQryWhereQTag,
       "tmnxWlanGwUeQryWhereTuRouter": tmnxWlanGwUeQryWhereTuRouter,
       "tmnxWlanGwUeQryWhereTuRemAddrTyp": tmnxWlanGwUeQryWhereTuRemAddrTyp,
       "tmnxWlanGwUeQryWhereTuRemAddr": tmnxWlanGwUeQryWhereTuRemAddr,
       "tmnxWlanGwUeQryWhereTuLocAddrTyp": tmnxWlanGwUeQryWhereTuLocAddrTyp,
       "tmnxWlanGwUeQryWhereTuLocAddr": tmnxWlanGwUeQryWhereTuLocAddr,
       "tmnxWlanGwUeQryNumResults": tmnxWlanGwUeQryNumResults,
       "tmnxWlanGwUeResTable": tmnxWlanGwUeResTable,
       "tmnxWlanGwUeResEntry": tmnxWlanGwUeResEntry,
       "tmnxWlanGwUeResId": tmnxWlanGwUeResId,
       "tmnxWlanGwUeResMacAddress": tmnxWlanGwUeResMacAddress,
       "tmnxWlanGwUeResQTag": tmnxWlanGwUeResQTag,
       "tmnxWlanGwUeResAddrType": tmnxWlanGwUeResAddrType,
       "tmnxWlanGwUeResAddr": tmnxWlanGwUeResAddr,
       "tmnxWlanGwUeResState": tmnxWlanGwUeResState,
       "tmnxWlanGwUeResIsaGrp": tmnxWlanGwUeResIsaGrp,
       "tmnxWlanGwUeResIsaMemberId": tmnxWlanGwUeResIsaMemberId,
       "tmnxWlanGwUeResTuRouter": tmnxWlanGwUeResTuRouter,
       "tmnxWlanGwUeResTuAddrType": tmnxWlanGwUeResTuAddrType,
       "tmnxWlanGwUeResTuRemoteAddr": tmnxWlanGwUeResTuRemoteAddr,
       "tmnxWlanGwUeResTuLocalAddr": tmnxWlanGwUeResTuLocalAddr,
       "tmnxWlanGwUeResApMacAddress": tmnxWlanGwUeResApMacAddress,
       "tmnxWlanGwUeResSsid": tmnxWlanGwUeResSsid,
       "tmnxWlanGwUeResMplsLabel": tmnxWlanGwUeResMplsLabel,
       "tmnxWlanGwUeResLastMoveTime": tmnxWlanGwUeResLastMoveTime,
       "tmnxWlanGwUeResExpirationTime": tmnxWlanGwUeResExpirationTime,
       "tmnxWlanGwUeResIdleTimeout": tmnxWlanGwUeResIdleTimeout,
       "tmnxWlanGwUeResSessionTimeout": tmnxWlanGwUeResSessionTimeout,
       "tmnxWlanGwUeResNatPlcy": tmnxWlanGwUeResNatPlcy,
       "tmnxWlanGwUeResHttpRdrPlcy": tmnxWlanGwUeResHttpRdrPlcy,
       "tmnxWlanGwUeResDsmIpFilter": tmnxWlanGwUeResDsmIpFilter,
       "tmnxWlanGwUeResDsmAcctPlcy": tmnxWlanGwUeResDsmAcctPlcy,
       "tmnxWlanGwUeResDsmAcctUpdInterv": tmnxWlanGwUeResDsmAcctUpdInterv,
       "tmnxWlanGwUeResAcctUpdate": tmnxWlanGwUeResAcctUpdate,
       "tmnxWlanGwUeResIngOperPir": tmnxWlanGwUeResIngOperPir,
       "tmnxWlanGwUeResIngOperCir": tmnxWlanGwUeResIngOperCir,
       "tmnxWlanGwUeResEgrOperPir": tmnxWlanGwUeResEgrOperPir,
       "tmnxWlanGwUeResEgrOperCir": tmnxWlanGwUeResEgrOperCir,
       "tmnxWlanGwUeResRxPkts": tmnxWlanGwUeResRxPkts,
       "tmnxWlanGwUeResRxOctets": tmnxWlanGwUeResRxOctets,
       "tmnxWlanGwUeResTxPkts": tmnxWlanGwUeResTxPkts,
       "tmnxWlanGwUeResTxOctets": tmnxWlanGwUeResTxOctets,
       "tmnxWlanGwGrpTableLastCh": tmnxWlanGwGrpTableLastCh,
       "tmnxWlanGwIomTableLastCh": tmnxWlanGwIomTableLastCh,
       "tmnxWlanGwSoftGreIfTableLastCh": tmnxWlanGwSoftGreIfTableLastCh,
       "tmnxWlanGwIfRetailTableLastCh": tmnxWlanGwIfRetailTableLastCh,
       "tmnxWlanGwMgwProfTableLastCh": tmnxWlanGwMgwProfTableLastCh,
       "tmnxWlanGwMgwAddrTableLastCh": tmnxWlanGwMgwAddrTableLastCh,
       "tmnxWlanGwTableLastCh": tmnxWlanGwTableLastCh,
       "tmnxWlanGwVlanTableLastCh": tmnxWlanGwVlanTableLastCh,
       "tmnxWlanGwPgwTableLastCh": tmnxWlanGwPgwTableLastCh,
       "tmnxWlanGwGgsnTableLastCh": tmnxWlanGwGgsnTableLastCh,
       "tmnxWlanGwSubIfTableLastCh": tmnxWlanGwSubIfTableLastCh,
       "tmnxWlanGwVlanDsmTableLastCh": tmnxWlanGwVlanDsmTableLastCh,
       "tmnxWlanGwDsmIpFilTableLastCh": tmnxWlanGwDsmIpFilTableLastCh,
       "tmnxWlanGwDsmIpFilN3TableLastCh": tmnxWlanGwDsmIpFilN3TableLastCh,
       "tmnxWlanGwPolicerTableLastCh": tmnxWlanGwPolicerTableLastCh,
       "tmnxWlanGwResrcProblem": tmnxWlanGwResrcProblem,
       "tmnxWlanGwNumSoftGreTu": tmnxWlanGwNumSoftGreTu,
       "tmnxWlanGwPeakNumSoftGreTu": tmnxWlanGwPeakNumSoftGreTu,
       "tmnxWlanGwNumUe": tmnxWlanGwNumUe,
       "tmnxWlanGwPeakNumUe": tmnxWlanGwPeakNumUe,
       "tmnxWlanGwNumMgw": tmnxWlanGwNumMgw,
       "tmnxWlanGwMgwNumHeldSe": tmnxWlanGwMgwNumHeldSe,
       "tmnxWlanGwNotificationObjs": tmnxWlanGwNotificationObjs,
       "tmnxWlanGwNotifyDescription": tmnxWlanGwNotifyDescription,
       "tmnxWlanGwNotifyTrue": tmnxWlanGwNotifyTrue,
       "tmnxWlanGwNotify3gppRelease": tmnxWlanGwNotify3gppRelease,
       "tmnxWlanGwNotifyPrefix": tmnxWlanGwNotifyPrefix,
       "tmnxWlanGwNotifications": tmnxWlanGwNotifications,
       "tmnxWlanGwResrcProblemDetected": tmnxWlanGwResrcProblemDetected,
       "tmnxWlanGwResrcProblemCause": tmnxWlanGwResrcProblemCause,
       "tmnxWlanGwTuQosProblem": tmnxWlanGwTuQosProblem,
       "tmnxWlanGwGrpOperStateChanged": tmnxWlanGwGrpOperStateChanged,
       "tmnxWlanGwIomActive": tmnxWlanGwIomActive,
       "tmnxWlanGwMgwConnected": tmnxWlanGwMgwConnected,
       "tmnxWlanGwMgwRestarted": tmnxWlanGwMgwRestarted,
       "tmnxWlanGwNumMgwHi": tmnxWlanGwNumMgwHi,
       "tmnxWlanGwMgwStateChanged": tmnxWlanGwMgwStateChanged,
       "tmnxWlanGwQosRadiusGtpMismatch": tmnxWlanGwQosRadiusGtpMismatch,
       "tmnxWlanGwSubIfRedActiveChanged": tmnxWlanGwSubIfRedActiveChanged}
)
