# SNMP MIB module (TIMETRA-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SECURITY-MIB.mib
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

(Dot1agCfmMDLevel,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevel")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(TmnxSlotNumOrZero,
 tmnxCpmFlashHwIndex,
 tmnxCpmFlashOperStatus) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxSlotNumOrZero",
    "tmnxCpmFlashHwIndex",
    "tmnxCpmFlashOperStatus")

(TEntryId,
 TFilterLogId,
 TFltrPortSelector,
 TItemMatch) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId",
    "TFilterLogId",
    "TFltrPortSelector",
    "TItemMatch")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortPortID,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortPortID")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(sdpBindId,) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindId")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(Dot1PPriority,
 Dot1PPriorityMask,
 IPv6FlowLabel,
 InterfaceIndex,
 IpAddressPrefixLength,
 ServiceAccessPoint,
 TBurstSize,
 TCIRRate,
 TCpmProtPolicyID,
 TDSCPNameOrEmpty,
 TIpOption,
 TIpProtocol,
 TItemDescription,
 TLDisplayString,
 TNamedItem,
 TNamedItemOrEmpty,
 TOperator,
 TPIRRate,
 TPIRRateOrZero,
 TTcpUdpPort,
 TmnxActionType,
 TmnxAdminState,
 TmnxDisplayStringURL,
 TmnxDistCpuProtAction,
 TmnxDistCpuProtActionDuration,
 TmnxDistCpuProtBurstSize,
 TmnxDistCpuProtEnforceType,
 TmnxDistCpuProtLogEventType,
 TmnxDistCpuProtPacketRateLimit,
 TmnxDistCpuProtProtocolId,
 TmnxDistCpuProtRate,
 TmnxDistCpuProtRateType,
 TmnxDistCpuProtState,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "Dot1PPriorityMask",
    "IPv6FlowLabel",
    "InterfaceIndex",
    "IpAddressPrefixLength",
    "ServiceAccessPoint",
    "TBurstSize",
    "TCIRRate",
    "TCpmProtPolicyID",
    "TDSCPNameOrEmpty",
    "TIpOption",
    "TIpProtocol",
    "TItemDescription",
    "TLDisplayString",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TOperator",
    "TPIRRate",
    "TPIRRateOrZero",
    "TTcpUdpPort",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxDisplayStringURL",
    "TmnxDistCpuProtAction",
    "TmnxDistCpuProtActionDuration",
    "TmnxDistCpuProtBurstSize",
    "TmnxDistCpuProtEnforceType",
    "TmnxDistCpuProtLogEventType",
    "TmnxDistCpuProtPacketRateLimit",
    "TmnxDistCpuProtProtocolId",
    "TmnxDistCpuProtRate",
    "TmnxDistCpuProtRateType",
    "TmnxDistCpuProtState",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfIndex,
 vRtrIfName) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex",
    "vRtrIfName")


# MODULE-IDENTITY

timetraSecurityMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 22)
)
if mibBuilder.loadTexts:
    timetraSecurityMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-08-01 00:00",
         "2011-11-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-02-28 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2003-01-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TProfileAction(TextualConvention, Integer32):
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
        *(("deny", 1),
          ("allow", 2),
          ("none", 3))
    )



class TmnxMafAction(TextualConvention, Integer32):
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
        *(("none", 0),
          ("permit", 1),
          ("deny", 2),
          ("denyHostUnreachable", 3))
    )



class TCpmFilterQueueId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(33, 2000),
    )



class TCpmFilterActionOrDefault(TextualConvention, Integer32):
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
        *(("drop", 1),
          ("forward", 2),
          ("queue", 3),
          ("default", 4))
    )



class TmnxKeyChainKeyDirection(TextualConvention, Integer32):
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
        *(("send", 1),
          ("receive", 2),
          ("send-receive", 3))
    )



class TmnxKeyChainKeyAlgorithm(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("nullKeyAlgo", 0),
          ("aes128Cmac96", 1),
          ("hmacSha196", 2),
          ("password", 3),
          ("message-digest", 4),
          ("hmacMd5", 5),
          ("hmacSha1", 6),
          ("hmacSha256", 7))
    )



class TmnxKeyChainKeyOption(TextualConvention, Integer32):
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
          ("basic", 1),
          ("isis-enhanced", 2))
    )



class TmnxKeyChainTcpOptionNum(TextualConvention, Integer32):
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
        *(("value253", 1),
          ("value254", 2),
          ("all", 3))
    )



class TmnxMafType(TextualConvention, Integer32):
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3))
    )



class TmnxCpmPacketRateLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )



class TmnxCpmPacketPolRateLimit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65534),
    )



class TmnxCpmPktPolRateLimitInclZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65534),
    )



class TmnxCpmPacketRate(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxCpmProtEthCfmOpCode(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxMafMacFltrFrameType(TextualConvention, Integer32):
    status = "current"
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
        *(("e802dot3", 0),
          ("e802dot2LLC", 1),
          ("e802dot2SNAP", 2),
          ("ethernetII", 3),
          ("e802dot1ag", 4))
    )



class TmnxCpmMacFltrFrameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("e802dot2LLC", 1),
          ("ethernetII", 3),
          ("e802dot1ag", 4))
    )



class TmnxSecRadiusServAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("round-robin", 2))
    )



class TCpmFilterPortOperator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mask", 0),
          ("range", 1))
    )



class TSSHCipherNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              6,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des", 2),
          ("threeDes", 3),
          ("blowfish", 6),
          ("threeDesCbc", 32),
          ("blowfishCbc", 33),
          ("cast128Cbc", 34),
          ("arcfour", 35),
          ("aes128Cbc", 36),
          ("aes192Cbc", 37),
          ("aes256Cbc", 38),
          ("rijndaelCbc", 39))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSecurityConformance_ObjectIdentity = ObjectIdentity
tmnxSecurityConformance = _TmnxSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22)
)
_TmnxSecurityCompliances_ObjectIdentity = ObjectIdentity
tmnxSecurityCompliances = _TmnxSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1)
)
_TmnxSecurityGroups_ObjectIdentity = ObjectIdentity
tmnxSecurityGroups = _TmnxSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2)
)
_TmnxSecurityObjects_ObjectIdentity = ObjectIdentity
tmnxSecurityObjects = _TmnxSecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22)
)
_TmnxUserProfileTable_Object = MibTable
tmnxUserProfileTable = _TmnxUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1)
)
if mibBuilder.loadTexts:
    tmnxUserProfileTable.setStatus("current")
_TmnxUserProfileEntry_Object = MibTableRow
tmnxUserProfileEntry = _TmnxUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1, 1)
)
tmnxUserProfileEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxUserProfile"),
)
if mibBuilder.loadTexts:
    tmnxUserProfileEntry.setStatus("current")
_TmnxUserProfile_Type = TNamedItem
_TmnxUserProfile_Object = MibTableColumn
tmnxUserProfile = _TmnxUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1, 1, 1),
    _TmnxUserProfile_Type()
)
tmnxUserProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxUserProfile.setStatus("current")
_TmnxUserProfileRowStatus_Type = RowStatus
_TmnxUserProfileRowStatus_Object = MibTableColumn
tmnxUserProfileRowStatus = _TmnxUserProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1, 1, 2),
    _TmnxUserProfileRowStatus_Type()
)
tmnxUserProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileRowStatus.setStatus("current")


class _TmnxUserProfileDefaultAction_Type(TProfileAction):
    """Custom type tmnxUserProfileDefaultAction based on TProfileAction"""
    defaultValue = 1


_TmnxUserProfileDefaultAction_Type.__name__ = "TProfileAction"
_TmnxUserProfileDefaultAction_Object = MibTableColumn
tmnxUserProfileDefaultAction = _TmnxUserProfileDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1, 1, 3),
    _TmnxUserProfileDefaultAction_Type()
)
tmnxUserProfileDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileDefaultAction.setStatus("current")


class _TmnxUserProfileLi_Type(TruthValue):
    """Custom type tmnxUserProfileLi based on TruthValue"""
    defaultValue = 2


_TmnxUserProfileLi_Type.__name__ = "TruthValue"
_TmnxUserProfileLi_Object = MibTableColumn
tmnxUserProfileLi = _TmnxUserProfileLi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1, 1, 4),
    _TmnxUserProfileLi_Type()
)
tmnxUserProfileLi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileLi.setStatus("current")


class _TmnxUserProfileNCKillSession_Type(TruthValue):
    """Custom type tmnxUserProfileNCKillSession based on TruthValue"""
    defaultValue = 2


_TmnxUserProfileNCKillSession_Type.__name__ = "TruthValue"
_TmnxUserProfileNCKillSession_Object = MibTableColumn
tmnxUserProfileNCKillSession = _TmnxUserProfileNCKillSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 1, 1, 5),
    _TmnxUserProfileNCKillSession_Type()
)
tmnxUserProfileNCKillSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileNCKillSession.setStatus("current")
_TmnxUserProfileMatchTable_Object = MibTable
tmnxUserProfileMatchTable = _TmnxUserProfileMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2)
)
if mibBuilder.loadTexts:
    tmnxUserProfileMatchTable.setStatus("current")
_TmnxUserProfileMatchEntry_Object = MibTableRow
tmnxUserProfileMatchEntry = _TmnxUserProfileMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2, 1)
)
tmnxUserProfileMatchEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxUserProfile"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchId"),
)
if mibBuilder.loadTexts:
    tmnxUserProfileMatchEntry.setStatus("current")


class _TmnxUserProfileMatchId_Type(Unsigned32):
    """Custom type tmnxUserProfileMatchId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TmnxUserProfileMatchId_Type.__name__ = "Unsigned32"
_TmnxUserProfileMatchId_Object = MibTableColumn
tmnxUserProfileMatchId = _TmnxUserProfileMatchId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2, 1, 1),
    _TmnxUserProfileMatchId_Type()
)
tmnxUserProfileMatchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxUserProfileMatchId.setStatus("current")
_TmnxUserProfileMatchRowStatus_Type = RowStatus
_TmnxUserProfileMatchRowStatus_Object = MibTableColumn
tmnxUserProfileMatchRowStatus = _TmnxUserProfileMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2, 1, 2),
    _TmnxUserProfileMatchRowStatus_Type()
)
tmnxUserProfileMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileMatchRowStatus.setStatus("current")


class _TmnxUserProfileMatchDescription_Type(TItemDescription):
    """Custom type tmnxUserProfileMatchDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxUserProfileMatchDescription_Type.__name__ = "TItemDescription"
_TmnxUserProfileMatchDescription_Object = MibTableColumn
tmnxUserProfileMatchDescription = _TmnxUserProfileMatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2, 1, 3),
    _TmnxUserProfileMatchDescription_Type()
)
tmnxUserProfileMatchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileMatchDescription.setStatus("current")
_TmnxUserProfileMatchAction_Type = TProfileAction
_TmnxUserProfileMatchAction_Object = MibTableColumn
tmnxUserProfileMatchAction = _TmnxUserProfileMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2, 1, 4),
    _TmnxUserProfileMatchAction_Type()
)
tmnxUserProfileMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileMatchAction.setStatus("current")
_TmnxUserProfileMatchString_Type = DisplayString
_TmnxUserProfileMatchString_Object = MibTableColumn
tmnxUserProfileMatchString = _TmnxUserProfileMatchString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 2, 1, 5),
    _TmnxUserProfileMatchString_Type()
)
tmnxUserProfileMatchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserProfileMatchString.setStatus("current")
_TmnxUserTable_Object = MibTable
tmnxUserTable = _TmnxUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3)
)
if mibBuilder.loadTexts:
    tmnxUserTable.setStatus("current")
_TmnxUserEntry_Object = MibTableRow
tmnxUserEntry = _TmnxUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1)
)
tmnxUserEntry.setIndexNames(
    (1, "TIMETRA-SECURITY-MIB", "tmnxUserName"),
)
if mibBuilder.loadTexts:
    tmnxUserEntry.setStatus("current")
_TmnxUserName_Type = TNamedItem
_TmnxUserName_Object = MibTableColumn
tmnxUserName = _TmnxUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 1),
    _TmnxUserName_Type()
)
tmnxUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxUserName.setStatus("current")
_TmnxUserRowStatus_Type = RowStatus
_TmnxUserRowStatus_Object = MibTableColumn
tmnxUserRowStatus = _TmnxUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 2),
    _TmnxUserRowStatus_Type()
)
tmnxUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserRowStatus.setStatus("current")


class _TmnxUserPassword_Type(DisplayString):
    """Custom type tmnxUserPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_TmnxUserPassword_Type.__name__ = "DisplayString"
_TmnxUserPassword_Object = MibTableColumn
tmnxUserPassword = _TmnxUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 3),
    _TmnxUserPassword_Type()
)
tmnxUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserPassword.setStatus("current")


class _TmnxUserPasswordEncrypted_Type(TruthValue):
    """Custom type tmnxUserPasswordEncrypted based on TruthValue"""
    defaultValue = 1


_TmnxUserPasswordEncrypted_Type.__name__ = "TruthValue"
_TmnxUserPasswordEncrypted_Object = MibTableColumn
tmnxUserPasswordEncrypted = _TmnxUserPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 4),
    _TmnxUserPasswordEncrypted_Type()
)
tmnxUserPasswordEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserPasswordEncrypted.setStatus("obsolete")


class _TmnxUserAccess_Type(Bits):
    """Custom type tmnxUserAccess based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("console", 0),
          ("ftp", 1),
          ("snmp", 2),
          ("li", 3),
          ("netconf", 4))
    )

_TmnxUserAccess_Type.__name__ = "Bits"
_TmnxUserAccess_Object = MibTableColumn
tmnxUserAccess = _TmnxUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 5),
    _TmnxUserAccess_Type()
)
tmnxUserAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserAccess.setStatus("current")


class _TmnxUserHomeDirectory_Type(DisplayString):
    """Custom type tmnxUserHomeDirectory based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TmnxUserHomeDirectory_Type.__name__ = "DisplayString"
_TmnxUserHomeDirectory_Object = MibTableColumn
tmnxUserHomeDirectory = _TmnxUserHomeDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 6),
    _TmnxUserHomeDirectory_Type()
)
tmnxUserHomeDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserHomeDirectory.setStatus("current")


class _TmnxUserRestrictedToHome_Type(TruthValue):
    """Custom type tmnxUserRestrictedToHome based on TruthValue"""
    defaultValue = 2


_TmnxUserRestrictedToHome_Type.__name__ = "TruthValue"
_TmnxUserRestrictedToHome_Object = MibTableColumn
tmnxUserRestrictedToHome = _TmnxUserRestrictedToHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 7),
    _TmnxUserRestrictedToHome_Type()
)
tmnxUserRestrictedToHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserRestrictedToHome.setStatus("current")


class _TmnxUserConsoleLoginExecFile_Type(DisplayString):
    """Custom type tmnxUserConsoleLoginExecFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TmnxUserConsoleLoginExecFile_Type.__name__ = "DisplayString"
_TmnxUserConsoleLoginExecFile_Object = MibTableColumn
tmnxUserConsoleLoginExecFile = _TmnxUserConsoleLoginExecFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 8),
    _TmnxUserConsoleLoginExecFile_Type()
)
tmnxUserConsoleLoginExecFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleLoginExecFile.setStatus("current")


class _TmnxUserConsoleCannotChangePswd_Type(TruthValue):
    """Custom type tmnxUserConsoleCannotChangePswd based on TruthValue"""
    defaultValue = 2


_TmnxUserConsoleCannotChangePswd_Type.__name__ = "TruthValue"
_TmnxUserConsoleCannotChangePswd_Object = MibTableColumn
tmnxUserConsoleCannotChangePswd = _TmnxUserConsoleCannotChangePswd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 9),
    _TmnxUserConsoleCannotChangePswd_Type()
)
tmnxUserConsoleCannotChangePswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleCannotChangePswd.setStatus("current")


class _TmnxUserConsoleNewPswdAtLogin_Type(TruthValue):
    """Custom type tmnxUserConsoleNewPswdAtLogin based on TruthValue"""
    defaultValue = 2


_TmnxUserConsoleNewPswdAtLogin_Type.__name__ = "TruthValue"
_TmnxUserConsoleNewPswdAtLogin_Object = MibTableColumn
tmnxUserConsoleNewPswdAtLogin = _TmnxUserConsoleNewPswdAtLogin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 10),
    _TmnxUserConsoleNewPswdAtLogin_Type()
)
tmnxUserConsoleNewPswdAtLogin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleNewPswdAtLogin.setStatus("current")


class _TmnxUserConsoleMemberProfile1_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile1_Object = MibTableColumn
tmnxUserConsoleMemberProfile1 = _TmnxUserConsoleMemberProfile1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 11),
    _TmnxUserConsoleMemberProfile1_Type()
)
tmnxUserConsoleMemberProfile1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile1.setStatus("current")


class _TmnxUserConsoleMemberProfile2_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile2_Object = MibTableColumn
tmnxUserConsoleMemberProfile2 = _TmnxUserConsoleMemberProfile2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 12),
    _TmnxUserConsoleMemberProfile2_Type()
)
tmnxUserConsoleMemberProfile2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile2.setStatus("current")


class _TmnxUserConsoleMemberProfile3_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile3_Object = MibTableColumn
tmnxUserConsoleMemberProfile3 = _TmnxUserConsoleMemberProfile3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 13),
    _TmnxUserConsoleMemberProfile3_Type()
)
tmnxUserConsoleMemberProfile3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile3.setStatus("current")


class _TmnxUserConsoleMemberProfile4_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile4_Object = MibTableColumn
tmnxUserConsoleMemberProfile4 = _TmnxUserConsoleMemberProfile4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 14),
    _TmnxUserConsoleMemberProfile4_Type()
)
tmnxUserConsoleMemberProfile4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile4.setStatus("current")


class _TmnxUserConsoleMemberProfile5_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile5_Object = MibTableColumn
tmnxUserConsoleMemberProfile5 = _TmnxUserConsoleMemberProfile5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 15),
    _TmnxUserConsoleMemberProfile5_Type()
)
tmnxUserConsoleMemberProfile5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile5.setStatus("current")


class _TmnxUserConsoleMemberProfile6_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile6 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile6_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile6_Object = MibTableColumn
tmnxUserConsoleMemberProfile6 = _TmnxUserConsoleMemberProfile6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 16),
    _TmnxUserConsoleMemberProfile6_Type()
)
tmnxUserConsoleMemberProfile6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile6.setStatus("current")


class _TmnxUserConsoleMemberProfile7_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile7 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile7_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile7_Object = MibTableColumn
tmnxUserConsoleMemberProfile7 = _TmnxUserConsoleMemberProfile7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 17),
    _TmnxUserConsoleMemberProfile7_Type()
)
tmnxUserConsoleMemberProfile7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile7.setStatus("current")


class _TmnxUserConsoleMemberProfile8_Type(TNamedItemOrEmpty):
    """Custom type tmnxUserConsoleMemberProfile8 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxUserConsoleMemberProfile8_Type.__name__ = "TNamedItemOrEmpty"
_TmnxUserConsoleMemberProfile8_Object = MibTableColumn
tmnxUserConsoleMemberProfile8 = _TmnxUserConsoleMemberProfile8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 18),
    _TmnxUserConsoleMemberProfile8_Type()
)
tmnxUserConsoleMemberProfile8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserConsoleMemberProfile8.setStatus("current")
_TmnxUserAttemptedLogins_Type = Counter32
_TmnxUserAttemptedLogins_Object = MibTableColumn
tmnxUserAttemptedLogins = _TmnxUserAttemptedLogins_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 19),
    _TmnxUserAttemptedLogins_Type()
)
tmnxUserAttemptedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxUserAttemptedLogins.setStatus("current")
_TmnxUserSuccessfulLogins_Type = Counter32
_TmnxUserSuccessfulLogins_Object = MibTableColumn
tmnxUserSuccessfulLogins = _TmnxUserSuccessfulLogins_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 20),
    _TmnxUserSuccessfulLogins_Type()
)
tmnxUserSuccessfulLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxUserSuccessfulLogins.setStatus("current")
_TmnxUserPasswordChanged_Type = TimeStamp
_TmnxUserPasswordChanged_Object = MibTableColumn
tmnxUserPasswordChanged = _TmnxUserPasswordChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 3, 1, 21),
    _TmnxUserPasswordChanged_Type()
)
tmnxUserPasswordChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxUserPasswordChanged.setStatus("current")
_TmnxMafObjs_ObjectIdentity = ObjectIdentity
tmnxMafObjs = _TmnxMafObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4)
)
_TmnxMafTable_Object = MibTable
tmnxMafTable = _TmnxMafTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxMafTable.setStatus("obsolete")
_TmnxMafEntry_Object = MibTableRow
tmnxMafEntry = _TmnxMafEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 1, 1)
)
tmnxMafEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxMafName"),
)
if mibBuilder.loadTexts:
    tmnxMafEntry.setStatus("obsolete")
_TmnxMafName_Type = TNamedItem
_TmnxMafName_Object = MibTableColumn
tmnxMafName = _TmnxMafName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 1, 1, 1),
    _TmnxMafName_Type()
)
tmnxMafName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMafName.setStatus("obsolete")
_TmnxMafRowStatus_Type = RowStatus
_TmnxMafRowStatus_Object = MibTableColumn
tmnxMafRowStatus = _TmnxMafRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 1, 1, 2),
    _TmnxMafRowStatus_Type()
)
tmnxMafRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafRowStatus.setStatus("obsolete")


class _TmnxMafDefaultAction_Type(TmnxMafAction):
    """Custom type tmnxMafDefaultAction based on TmnxMafAction"""
    defaultValue = 0


_TmnxMafDefaultAction_Type.__name__ = "TmnxMafAction"
_TmnxMafDefaultAction_Object = MibTableColumn
tmnxMafDefaultAction = _TmnxMafDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 1, 1, 3),
    _TmnxMafDefaultAction_Type()
)
tmnxMafDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafDefaultAction.setStatus("obsolete")


class _TmnxMafAdminState_Type(TmnxAdminState):
    """Custom type tmnxMafAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxMafAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMafAdminState_Object = MibTableColumn
tmnxMafAdminState = _TmnxMafAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 1, 1, 4),
    _TmnxMafAdminState_Type()
)
tmnxMafAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafAdminState.setStatus("obsolete")
_TmnxMafMatchTable_Object = MibTable
tmnxMafMatchTable = _TmnxMafMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxMafMatchTable.setStatus("obsolete")
_TmnxMafMatchEntry_Object = MibTableRow
tmnxMafMatchEntry = _TmnxMafMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1)
)
tmnxMafMatchEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxMafName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxMafMatchIndex"),
)
if mibBuilder.loadTexts:
    tmnxMafMatchEntry.setStatus("obsolete")


class _TmnxMafMatchIndex_Type(Unsigned32):
    """Custom type tmnxMafMatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TmnxMafMatchIndex_Type.__name__ = "Unsigned32"
_TmnxMafMatchIndex_Object = MibTableColumn
tmnxMafMatchIndex = _TmnxMafMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 1),
    _TmnxMafMatchIndex_Type()
)
tmnxMafMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMafMatchIndex.setStatus("obsolete")
_TmnxMafMatchRowStatus_Type = RowStatus
_TmnxMafMatchRowStatus_Object = MibTableColumn
tmnxMafMatchRowStatus = _TmnxMafMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 2),
    _TmnxMafMatchRowStatus_Type()
)
tmnxMafMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchRowStatus.setStatus("obsolete")
_TmnxMafMatchLastChanged_Type = TimeStamp
_TmnxMafMatchLastChanged_Object = MibTableColumn
tmnxMafMatchLastChanged = _TmnxMafMatchLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 3),
    _TmnxMafMatchLastChanged_Type()
)
tmnxMafMatchLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMafMatchLastChanged.setStatus("obsolete")


class _TmnxMafMatchAction_Type(TmnxMafAction):
    """Custom type tmnxMafMatchAction based on TmnxMafAction"""
    defaultValue = 0


_TmnxMafMatchAction_Type.__name__ = "TmnxMafAction"
_TmnxMafMatchAction_Object = MibTableColumn
tmnxMafMatchAction = _TmnxMafMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 4),
    _TmnxMafMatchAction_Type()
)
tmnxMafMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchAction.setStatus("obsolete")


class _TmnxMafMatchDescription_Type(TItemDescription):
    """Custom type tmnxMafMatchDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMafMatchDescription_Type.__name__ = "TItemDescription"
_TmnxMafMatchDescription_Object = MibTableColumn
tmnxMafMatchDescription = _TmnxMafMatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 5),
    _TmnxMafMatchDescription_Type()
)
tmnxMafMatchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchDescription.setStatus("obsolete")


class _TmnxMafMatchSrcIpAddr_Type(IpAddress):
    """Custom type tmnxMafMatchSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxMafMatchSrcIpAddr_Type.__name__ = "IpAddress"
_TmnxMafMatchSrcIpAddr_Object = MibTableColumn
tmnxMafMatchSrcIpAddr = _TmnxMafMatchSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 6),
    _TmnxMafMatchSrcIpAddr_Type()
)
tmnxMafMatchSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchSrcIpAddr.setStatus("obsolete")


class _TmnxMafMatchSrcIpMask_Type(IpAddressPrefixLength):
    """Custom type tmnxMafMatchSrcIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TmnxMafMatchSrcIpMask_Type.__name__ = "IpAddressPrefixLength"
_TmnxMafMatchSrcIpMask_Object = MibTableColumn
tmnxMafMatchSrcIpMask = _TmnxMafMatchSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 7),
    _TmnxMafMatchSrcIpMask_Type()
)
tmnxMafMatchSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchSrcIpMask.setStatus("obsolete")


class _TmnxMafMatchSrcPortType_Type(Integer32):
    """Custom type tmnxMafMatchSrcPortType based on Integer32"""
    defaultValue = 1

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
        *(("any", 1),
          ("cpm", 2),
          ("port", 3),
          ("lag", 4))
    )


_TmnxMafMatchSrcPortType_Type.__name__ = "Integer32"
_TmnxMafMatchSrcPortType_Object = MibTableColumn
tmnxMafMatchSrcPortType = _TmnxMafMatchSrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 8),
    _TmnxMafMatchSrcPortType_Type()
)
tmnxMafMatchSrcPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchSrcPortType.setStatus("obsolete")


class _TmnxMafMatchSrcPortId_Type(TmnxPortID):
    """Custom type tmnxMafMatchSrcPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxMafMatchSrcPortId_Type.__name__ = "TmnxPortID"
_TmnxMafMatchSrcPortId_Object = MibTableColumn
tmnxMafMatchSrcPortId = _TmnxMafMatchSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 9),
    _TmnxMafMatchSrcPortId_Type()
)
tmnxMafMatchSrcPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchSrcPortId.setStatus("obsolete")


class _TmnxMafMatchDestPort_Type(TTcpUdpPort):
    """Custom type tmnxMafMatchDestPort based on TTcpUdpPort"""
    defaultValue = 0


_TmnxMafMatchDestPort_Type.__name__ = "TTcpUdpPort"
_TmnxMafMatchDestPort_Object = MibTableColumn
tmnxMafMatchDestPort = _TmnxMafMatchDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 10),
    _TmnxMafMatchDestPort_Type()
)
tmnxMafMatchDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchDestPort.setStatus("obsolete")


class _TmnxMafMatchDestPortMask_Type(Unsigned32):
    """Custom type tmnxMafMatchDestPortMask based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxMafMatchDestPortMask_Type.__name__ = "Unsigned32"
_TmnxMafMatchDestPortMask_Object = MibTableColumn
tmnxMafMatchDestPortMask = _TmnxMafMatchDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 11),
    _TmnxMafMatchDestPortMask_Type()
)
tmnxMafMatchDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchDestPortMask.setStatus("obsolete")


class _TmnxMafMatchProtocol_Type(TIpProtocol):
    """Custom type tmnxMafMatchProtocol based on TIpProtocol"""
    defaultValue = -1


_TmnxMafMatchProtocol_Type.__name__ = "TIpProtocol"
_TmnxMafMatchProtocol_Object = MibTableColumn
tmnxMafMatchProtocol = _TmnxMafMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 12),
    _TmnxMafMatchProtocol_Type()
)
tmnxMafMatchProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchProtocol.setStatus("obsolete")
_TmnxMafMatchCount_Type = Counter64
_TmnxMafMatchCount_Object = MibTableColumn
tmnxMafMatchCount = _TmnxMafMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 13),
    _TmnxMafMatchCount_Type()
)
tmnxMafMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMafMatchCount.setStatus("obsolete")


class _TmnxMafMatchRouter_Type(TNamedItemOrEmpty):
    """Custom type tmnxMafMatchRouter based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMafMatchRouter_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMafMatchRouter_Object = MibTableColumn
tmnxMafMatchRouter = _TmnxMafMatchRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 14),
    _TmnxMafMatchRouter_Type()
)
tmnxMafMatchRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchRouter.setStatus("obsolete")


class _TmnxMafMatchLog_Type(TruthValue):
    """Custom type tmnxMafMatchLog based on TruthValue"""
    defaultValue = 2


_TmnxMafMatchLog_Type.__name__ = "TruthValue"
_TmnxMafMatchLog_Object = MibTableColumn
tmnxMafMatchLog = _TmnxMafMatchLog_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 2, 1, 15),
    _TmnxMafMatchLog_Type()
)
tmnxMafMatchLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMafMatchLog.setStatus("obsolete")
_TmnxGenMafTableLastChanged_Type = TimeStamp
_TmnxGenMafTableLastChanged_Object = MibScalar
tmnxGenMafTableLastChanged = _TmnxGenMafTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 3),
    _TmnxGenMafTableLastChanged_Type()
)
tmnxGenMafTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGenMafTableLastChanged.setStatus("current")
_TmnxGenMafTable_Object = MibTable
tmnxGenMafTable = _TmnxGenMafTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxGenMafTable.setStatus("current")
_TmnxGenMafEntry_Object = MibTableRow
tmnxGenMafEntry = _TmnxGenMafEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1)
)
tmnxGenMafEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxGenMafType"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxGenMafName"),
)
if mibBuilder.loadTexts:
    tmnxGenMafEntry.setStatus("current")
_TmnxGenMafType_Type = TmnxMafType
_TmnxGenMafType_Object = MibTableColumn
tmnxGenMafType = _TmnxGenMafType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1, 1),
    _TmnxGenMafType_Type()
)
tmnxGenMafType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGenMafType.setStatus("current")
_TmnxGenMafName_Type = TNamedItem
_TmnxGenMafName_Object = MibTableColumn
tmnxGenMafName = _TmnxGenMafName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1, 2),
    _TmnxGenMafName_Type()
)
tmnxGenMafName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGenMafName.setStatus("current")
_TmnxGenMafLastModified_Type = TimeStamp
_TmnxGenMafLastModified_Object = MibTableColumn
tmnxGenMafLastModified = _TmnxGenMafLastModified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1, 3),
    _TmnxGenMafLastModified_Type()
)
tmnxGenMafLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGenMafLastModified.setStatus("current")
_TmnxGenMafRowStatus_Type = RowStatus
_TmnxGenMafRowStatus_Object = MibTableColumn
tmnxGenMafRowStatus = _TmnxGenMafRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1, 4),
    _TmnxGenMafRowStatus_Type()
)
tmnxGenMafRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGenMafRowStatus.setStatus("current")


class _TmnxGenMafAdminState_Type(TmnxAdminState):
    """Custom type tmnxGenMafAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxGenMafAdminState_Type.__name__ = "TmnxAdminState"
_TmnxGenMafAdminState_Object = MibTableColumn
tmnxGenMafAdminState = _TmnxGenMafAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1, 5),
    _TmnxGenMafAdminState_Type()
)
tmnxGenMafAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGenMafAdminState.setStatus("current")


class _TmnxGenMafDefaultAction_Type(TmnxMafAction):
    """Custom type tmnxGenMafDefaultAction based on TmnxMafAction"""
    defaultValue = 0


_TmnxGenMafDefaultAction_Type.__name__ = "TmnxMafAction"
_TmnxGenMafDefaultAction_Object = MibTableColumn
tmnxGenMafDefaultAction = _TmnxGenMafDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 4, 1, 6),
    _TmnxGenMafDefaultAction_Type()
)
tmnxGenMafDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGenMafDefaultAction.setStatus("current")
_TmnxMafIPMatchTableLastChanged_Type = TimeStamp
_TmnxMafIPMatchTableLastChanged_Object = MibScalar
tmnxMafIPMatchTableLastChanged = _TmnxMafIPMatchTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 5),
    _TmnxMafIPMatchTableLastChanged_Type()
)
tmnxMafIPMatchTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMafIPMatchTableLastChanged.setStatus("current")
_TmnxIPMafMatchTable_Object = MibTable
tmnxIPMafMatchTable = _TmnxIPMafMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxIPMafMatchTable.setStatus("current")
_TmnxIPMafMatchEntry_Object = MibTableRow
tmnxIPMafMatchEntry = _TmnxIPMafMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1)
)
tmnxIPMafMatchEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxGenMafType"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxGenMafName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxIPMafMatchIndex"),
)
if mibBuilder.loadTexts:
    tmnxIPMafMatchEntry.setStatus("current")


class _TmnxIPMafMatchIndex_Type(Unsigned32):
    """Custom type tmnxIPMafMatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TmnxIPMafMatchIndex_Type.__name__ = "Unsigned32"
_TmnxIPMafMatchIndex_Object = MibTableColumn
tmnxIPMafMatchIndex = _TmnxIPMafMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 1),
    _TmnxIPMafMatchIndex_Type()
)
tmnxIPMafMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPMafMatchIndex.setStatus("current")
_TmnxIPMafMatchRowStatus_Type = RowStatus
_TmnxIPMafMatchRowStatus_Object = MibTableColumn
tmnxIPMafMatchRowStatus = _TmnxIPMafMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 2),
    _TmnxIPMafMatchRowStatus_Type()
)
tmnxIPMafMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchRowStatus.setStatus("current")
_TmnxIPMafMatchLastChanged_Type = TimeStamp
_TmnxIPMafMatchLastChanged_Object = MibTableColumn
tmnxIPMafMatchLastChanged = _TmnxIPMafMatchLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 3),
    _TmnxIPMafMatchLastChanged_Type()
)
tmnxIPMafMatchLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPMafMatchLastChanged.setStatus("current")


class _TmnxIPMafMatchAction_Type(TmnxMafAction):
    """Custom type tmnxIPMafMatchAction based on TmnxMafAction"""
    defaultValue = 0


_TmnxIPMafMatchAction_Type.__name__ = "TmnxMafAction"
_TmnxIPMafMatchAction_Object = MibTableColumn
tmnxIPMafMatchAction = _TmnxIPMafMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 4),
    _TmnxIPMafMatchAction_Type()
)
tmnxIPMafMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchAction.setStatus("current")


class _TmnxIPMafMatchDescription_Type(TItemDescription):
    """Custom type tmnxIPMafMatchDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxIPMafMatchDescription_Type.__name__ = "TItemDescription"
_TmnxIPMafMatchDescription_Object = MibTableColumn
tmnxIPMafMatchDescription = _TmnxIPMafMatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 5),
    _TmnxIPMafMatchDescription_Type()
)
tmnxIPMafMatchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchDescription.setStatus("current")


class _TmnxIPMafMatchSrcIpAddrType_Type(InetAddressType):
    """Custom type tmnxIPMafMatchSrcIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPMafMatchSrcIpAddrType_Type.__name__ = "InetAddressType"
_TmnxIPMafMatchSrcIpAddrType_Object = MibTableColumn
tmnxIPMafMatchSrcIpAddrType = _TmnxIPMafMatchSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 6),
    _TmnxIPMafMatchSrcIpAddrType_Type()
)
tmnxIPMafMatchSrcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchSrcIpAddrType.setStatus("current")


class _TmnxIPMafMatchSrcIpAddr_Type(InetAddress):
    """Custom type tmnxIPMafMatchSrcIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPMafMatchSrcIpAddr_Type.__name__ = "InetAddress"
_TmnxIPMafMatchSrcIpAddr_Object = MibTableColumn
tmnxIPMafMatchSrcIpAddr = _TmnxIPMafMatchSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 7),
    _TmnxIPMafMatchSrcIpAddr_Type()
)
tmnxIPMafMatchSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchSrcIpAddr.setStatus("current")


class _TmnxIPMafMatchSrcIpMask_Type(InetAddressPrefixLength):
    """Custom type tmnxIPMafMatchSrcIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxIPMafMatchSrcIpMask_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPMafMatchSrcIpMask_Object = MibTableColumn
tmnxIPMafMatchSrcIpMask = _TmnxIPMafMatchSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 8),
    _TmnxIPMafMatchSrcIpMask_Type()
)
tmnxIPMafMatchSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchSrcIpMask.setStatus("current")


class _TmnxIPMafMatchSrcPortType_Type(Integer32):
    """Custom type tmnxIPMafMatchSrcPortType based on Integer32"""
    defaultValue = 1

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
        *(("any", 1),
          ("cpm", 2),
          ("port", 3),
          ("lag", 4))
    )


_TmnxIPMafMatchSrcPortType_Type.__name__ = "Integer32"
_TmnxIPMafMatchSrcPortType_Object = MibTableColumn
tmnxIPMafMatchSrcPortType = _TmnxIPMafMatchSrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 9),
    _TmnxIPMafMatchSrcPortType_Type()
)
tmnxIPMafMatchSrcPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchSrcPortType.setStatus("current")


class _TmnxIPMafMatchSrcPortId_Type(TmnxPortID):
    """Custom type tmnxIPMafMatchSrcPortId based on TmnxPortID"""
    defaultValue = 503316480


_TmnxIPMafMatchSrcPortId_Type.__name__ = "TmnxPortID"
_TmnxIPMafMatchSrcPortId_Object = MibTableColumn
tmnxIPMafMatchSrcPortId = _TmnxIPMafMatchSrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 10),
    _TmnxIPMafMatchSrcPortId_Type()
)
tmnxIPMafMatchSrcPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchSrcPortId.setStatus("current")


class _TmnxIPMafMatchDestPort_Type(TTcpUdpPort):
    """Custom type tmnxIPMafMatchDestPort based on TTcpUdpPort"""
    defaultValue = 0


_TmnxIPMafMatchDestPort_Type.__name__ = "TTcpUdpPort"
_TmnxIPMafMatchDestPort_Object = MibTableColumn
tmnxIPMafMatchDestPort = _TmnxIPMafMatchDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 11),
    _TmnxIPMafMatchDestPort_Type()
)
tmnxIPMafMatchDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchDestPort.setStatus("current")


class _TmnxIPMafMatchDestPortMask_Type(Unsigned32):
    """Custom type tmnxIPMafMatchDestPortMask based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxIPMafMatchDestPortMask_Type.__name__ = "Unsigned32"
_TmnxIPMafMatchDestPortMask_Object = MibTableColumn
tmnxIPMafMatchDestPortMask = _TmnxIPMafMatchDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 12),
    _TmnxIPMafMatchDestPortMask_Type()
)
tmnxIPMafMatchDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchDestPortMask.setStatus("current")


class _TmnxIPMafMatchProtNxtHdr_Type(TIpProtocol):
    """Custom type tmnxIPMafMatchProtNxtHdr based on TIpProtocol"""
    defaultValue = -1


_TmnxIPMafMatchProtNxtHdr_Type.__name__ = "TIpProtocol"
_TmnxIPMafMatchProtNxtHdr_Object = MibTableColumn
tmnxIPMafMatchProtNxtHdr = _TmnxIPMafMatchProtNxtHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 13),
    _TmnxIPMafMatchProtNxtHdr_Type()
)
tmnxIPMafMatchProtNxtHdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchProtNxtHdr.setStatus("current")
_TmnxIPMafMatchCount_Type = Counter64
_TmnxIPMafMatchCount_Object = MibTableColumn
tmnxIPMafMatchCount = _TmnxIPMafMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 14),
    _TmnxIPMafMatchCount_Type()
)
tmnxIPMafMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPMafMatchCount.setStatus("current")


class _TmnxIPMafMatchRouter_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPMafMatchRouter based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPMafMatchRouter_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPMafMatchRouter_Object = MibTableColumn
tmnxIPMafMatchRouter = _TmnxIPMafMatchRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 15),
    _TmnxIPMafMatchRouter_Type()
)
tmnxIPMafMatchRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchRouter.setStatus("current")


class _TmnxIPMafMatchFlowLabel_Type(IPv6FlowLabel):
    """Custom type tmnxIPMafMatchFlowLabel based on IPv6FlowLabel"""
    defaultValue = -1


_TmnxIPMafMatchFlowLabel_Type.__name__ = "IPv6FlowLabel"
_TmnxIPMafMatchFlowLabel_Object = MibTableColumn
tmnxIPMafMatchFlowLabel = _TmnxIPMafMatchFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 16),
    _TmnxIPMafMatchFlowLabel_Type()
)
tmnxIPMafMatchFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchFlowLabel.setStatus("current")


class _TmnxIPMafMatchLog_Type(TruthValue):
    """Custom type tmnxIPMafMatchLog based on TruthValue"""
    defaultValue = 2


_TmnxIPMafMatchLog_Type.__name__ = "TruthValue"
_TmnxIPMafMatchLog_Object = MibTableColumn
tmnxIPMafMatchLog = _TmnxIPMafMatchLog_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 6, 1, 17),
    _TmnxIPMafMatchLog_Type()
)
tmnxIPMafMatchLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPMafMatchLog.setStatus("current")
_TmnxMafMacMatchTableLastChanged_Type = TimeStamp
_TmnxMafMacMatchTableLastChanged_Object = MibScalar
tmnxMafMacMatchTableLastChanged = _TmnxMafMacMatchTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 7),
    _TmnxMafMacMatchTableLastChanged_Type()
)
tmnxMafMacMatchTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMafMacMatchTableLastChanged.setStatus("current")
_TmnxMacMafMatchTable_Object = MibTable
tmnxMacMafMatchTable = _TmnxMacMafMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8)
)
if mibBuilder.loadTexts:
    tmnxMacMafMatchTable.setStatus("current")
_TmnxMacMafMatchEntry_Object = MibTableRow
tmnxMacMafMatchEntry = _TmnxMacMafMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1)
)
tmnxMacMafMatchEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxGenMafName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxMacMafMatchIndex"),
)
if mibBuilder.loadTexts:
    tmnxMacMafMatchEntry.setStatus("current")


class _TmnxMacMafMatchIndex_Type(Unsigned32):
    """Custom type tmnxMacMafMatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TmnxMacMafMatchIndex_Type.__name__ = "Unsigned32"
_TmnxMacMafMatchIndex_Object = MibTableColumn
tmnxMacMafMatchIndex = _TmnxMacMafMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 1),
    _TmnxMacMafMatchIndex_Type()
)
tmnxMacMafMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMacMafMatchIndex.setStatus("current")
_TmnxMacMafMatchRowStatus_Type = RowStatus
_TmnxMacMafMatchRowStatus_Object = MibTableColumn
tmnxMacMafMatchRowStatus = _TmnxMacMafMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 2),
    _TmnxMacMafMatchRowStatus_Type()
)
tmnxMacMafMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchRowStatus.setStatus("current")
_TmnxMacMafMatchLastChanged_Type = TimeStamp
_TmnxMacMafMatchLastChanged_Object = MibTableColumn
tmnxMacMafMatchLastChanged = _TmnxMacMafMatchLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 3),
    _TmnxMacMafMatchLastChanged_Type()
)
tmnxMacMafMatchLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacMafMatchLastChanged.setStatus("current")


class _TmnxMacMafMatchAction_Type(TmnxMafAction):
    """Custom type tmnxMacMafMatchAction based on TmnxMafAction"""
    defaultValue = 0


_TmnxMacMafMatchAction_Type.__name__ = "TmnxMafAction"
_TmnxMacMafMatchAction_Object = MibTableColumn
tmnxMacMafMatchAction = _TmnxMacMafMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 4),
    _TmnxMacMafMatchAction_Type()
)
tmnxMacMafMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchAction.setStatus("current")


class _TmnxMacMafMatchDescription_Type(TItemDescription):
    """Custom type tmnxMacMafMatchDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMacMafMatchDescription_Type.__name__ = "TItemDescription"
_TmnxMacMafMatchDescription_Object = MibTableColumn
tmnxMacMafMatchDescription = _TmnxMacMafMatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 5),
    _TmnxMacMafMatchDescription_Type()
)
tmnxMacMafMatchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDescription.setStatus("current")


class _TmnxMacMafMatchLog_Type(TruthValue):
    """Custom type tmnxMacMafMatchLog based on TruthValue"""
    defaultValue = 2


_TmnxMacMafMatchLog_Type.__name__ = "TruthValue"
_TmnxMacMafMatchLog_Object = MibTableColumn
tmnxMacMafMatchLog = _TmnxMacMafMatchLog_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 6),
    _TmnxMacMafMatchLog_Type()
)
tmnxMacMafMatchLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchLog.setStatus("current")


class _TmnxMacMafMatchFrameType_Type(TmnxMafMacFltrFrameType):
    """Custom type tmnxMacMafMatchFrameType based on TmnxMafMacFltrFrameType"""
    defaultValue = 0


_TmnxMacMafMatchFrameType_Type.__name__ = "TmnxMafMacFltrFrameType"
_TmnxMacMafMatchFrameType_Object = MibTableColumn
tmnxMacMafMatchFrameType = _TmnxMacMafMatchFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 7),
    _TmnxMacMafMatchFrameType_Type()
)
tmnxMacMafMatchFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchFrameType.setStatus("current")


class _TmnxMacMafMatchSvcId_Type(TmnxServId):
    """Custom type tmnxMacMafMatchSvcId based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxMacMafMatchSvcId_Type.__name__ = "TmnxServId"
_TmnxMacMafMatchSvcId_Object = MibTableColumn
tmnxMacMafMatchSvcId = _TmnxMacMafMatchSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 8),
    _TmnxMacMafMatchSvcId_Type()
)
tmnxMacMafMatchSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSvcId.setStatus("current")


class _TmnxMacMafMatchDot1pValue_Type(Dot1PPriority):
    """Custom type tmnxMacMafMatchDot1pValue based on Dot1PPriority"""
    defaultValue = -1


_TmnxMacMafMatchDot1pValue_Type.__name__ = "Dot1PPriority"
_TmnxMacMafMatchDot1pValue_Object = MibTableColumn
tmnxMacMafMatchDot1pValue = _TmnxMacMafMatchDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 9),
    _TmnxMacMafMatchDot1pValue_Type()
)
tmnxMacMafMatchDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDot1pValue.setStatus("current")


class _TmnxMacMafMatchDot1pMask_Type(Dot1PPriorityMask):
    """Custom type tmnxMacMafMatchDot1pMask based on Dot1PPriorityMask"""
    defaultValue = 0


_TmnxMacMafMatchDot1pMask_Type.__name__ = "Dot1PPriorityMask"
_TmnxMacMafMatchDot1pMask_Object = MibTableColumn
tmnxMacMafMatchDot1pMask = _TmnxMacMafMatchDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 10),
    _TmnxMacMafMatchDot1pMask_Type()
)
tmnxMacMafMatchDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDot1pMask.setStatus("current")


class _TmnxMacMafMatchDsap_Type(ServiceAccessPoint):
    """Custom type tmnxMacMafMatchDsap based on ServiceAccessPoint"""
    defaultValue = -1


_TmnxMacMafMatchDsap_Type.__name__ = "ServiceAccessPoint"
_TmnxMacMafMatchDsap_Object = MibTableColumn
tmnxMacMafMatchDsap = _TmnxMacMafMatchDsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 11),
    _TmnxMacMafMatchDsap_Type()
)
tmnxMacMafMatchDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDsap.setStatus("current")


class _TmnxMacMafMatchDsapMask_Type(ServiceAccessPoint):
    """Custom type tmnxMacMafMatchDsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TmnxMacMafMatchDsapMask_Type.__name__ = "ServiceAccessPoint"
_TmnxMacMafMatchDsapMask_Object = MibTableColumn
tmnxMacMafMatchDsapMask = _TmnxMacMafMatchDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 12),
    _TmnxMacMafMatchDsapMask_Type()
)
tmnxMacMafMatchDsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDsapMask.setStatus("current")


class _TmnxMacMafMatchSrcMAC_Type(MacAddress):
    """Custom type tmnxMacMafMatchSrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMacMafMatchSrcMAC_Type.__name__ = "MacAddress"
_TmnxMacMafMatchSrcMAC_Object = MibTableColumn
tmnxMacMafMatchSrcMAC = _TmnxMacMafMatchSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 13),
    _TmnxMacMafMatchSrcMAC_Type()
)
tmnxMacMafMatchSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSrcMAC.setStatus("current")


class _TmnxMacMafMatchSrcMACMask_Type(MacAddress):
    """Custom type tmnxMacMafMatchSrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMacMafMatchSrcMACMask_Type.__name__ = "MacAddress"
_TmnxMacMafMatchSrcMACMask_Object = MibTableColumn
tmnxMacMafMatchSrcMACMask = _TmnxMacMafMatchSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 14),
    _TmnxMacMafMatchSrcMACMask_Type()
)
tmnxMacMafMatchSrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSrcMACMask.setStatus("current")


class _TmnxMacMafMatchDstMAC_Type(MacAddress):
    """Custom type tmnxMacMafMatchDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMacMafMatchDstMAC_Type.__name__ = "MacAddress"
_TmnxMacMafMatchDstMAC_Object = MibTableColumn
tmnxMacMafMatchDstMAC = _TmnxMacMafMatchDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 15),
    _TmnxMacMafMatchDstMAC_Type()
)
tmnxMacMafMatchDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDstMAC.setStatus("current")


class _TmnxMacMafMatchDstMACMask_Type(MacAddress):
    """Custom type tmnxMacMafMatchDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMacMafMatchDstMACMask_Type.__name__ = "MacAddress"
_TmnxMacMafMatchDstMACMask_Object = MibTableColumn
tmnxMacMafMatchDstMACMask = _TmnxMacMafMatchDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 16),
    _TmnxMacMafMatchDstMACMask_Type()
)
tmnxMacMafMatchDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchDstMACMask.setStatus("current")


class _TmnxMacMafMatchEtherType_Type(Integer32):
    """Custom type tmnxMacMafMatchEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxMacMafMatchEtherType_Type.__name__ = "Integer32"
_TmnxMacMafMatchEtherType_Object = MibTableColumn
tmnxMacMafMatchEtherType = _TmnxMacMafMatchEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 17),
    _TmnxMacMafMatchEtherType_Type()
)
tmnxMacMafMatchEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchEtherType.setStatus("current")


class _TmnxMacMafMatchSnapOui_Type(Integer32):
    """Custom type tmnxMacMafMatchSnapOui based on Integer32"""
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
        *(("off", 1),
          ("zero", 2),
          ("nonZero", 3))
    )


_TmnxMacMafMatchSnapOui_Type.__name__ = "Integer32"
_TmnxMacMafMatchSnapOui_Object = MibTableColumn
tmnxMacMafMatchSnapOui = _TmnxMacMafMatchSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 18),
    _TmnxMacMafMatchSnapOui_Type()
)
tmnxMacMafMatchSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSnapOui.setStatus("current")


class _TmnxMacMafMatchSnapPid_Type(Integer32):
    """Custom type tmnxMacMafMatchSnapPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxMacMafMatchSnapPid_Type.__name__ = "Integer32"
_TmnxMacMafMatchSnapPid_Object = MibTableColumn
tmnxMacMafMatchSnapPid = _TmnxMacMafMatchSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 19),
    _TmnxMacMafMatchSnapPid_Type()
)
tmnxMacMafMatchSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSnapPid.setStatus("current")


class _TmnxMacMafMatchSsap_Type(ServiceAccessPoint):
    """Custom type tmnxMacMafMatchSsap based on ServiceAccessPoint"""
    defaultValue = -1


_TmnxMacMafMatchSsap_Type.__name__ = "ServiceAccessPoint"
_TmnxMacMafMatchSsap_Object = MibTableColumn
tmnxMacMafMatchSsap = _TmnxMacMafMatchSsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 20),
    _TmnxMacMafMatchSsap_Type()
)
tmnxMacMafMatchSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSsap.setStatus("current")


class _TmnxMacMafMatchSsapMask_Type(ServiceAccessPoint):
    """Custom type tmnxMacMafMatchSsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TmnxMacMafMatchSsapMask_Type.__name__ = "ServiceAccessPoint"
_TmnxMacMafMatchSsapMask_Object = MibTableColumn
tmnxMacMafMatchSsapMask = _TmnxMacMafMatchSsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 21),
    _TmnxMacMafMatchSsapMask_Type()
)
tmnxMacMafMatchSsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchSsapMask.setStatus("current")


class _TmnxMacMafMatchCfmOpCodeOper_Type(TOperator):
    """Custom type tmnxMacMafMatchCfmOpCodeOper based on TOperator"""
    defaultValue = 0


_TmnxMacMafMatchCfmOpCodeOper_Type.__name__ = "TOperator"
_TmnxMacMafMatchCfmOpCodeOper_Object = MibTableColumn
tmnxMacMafMatchCfmOpCodeOper = _TmnxMacMafMatchCfmOpCodeOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 22),
    _TmnxMacMafMatchCfmOpCodeOper_Type()
)
tmnxMacMafMatchCfmOpCodeOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchCfmOpCodeOper.setStatus("current")


class _TmnxMacMafMatchCfmOpCodeValue1_Type(Unsigned32):
    """Custom type tmnxMacMafMatchCfmOpCodeValue1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxMacMafMatchCfmOpCodeValue1_Type.__name__ = "Unsigned32"
_TmnxMacMafMatchCfmOpCodeValue1_Object = MibTableColumn
tmnxMacMafMatchCfmOpCodeValue1 = _TmnxMacMafMatchCfmOpCodeValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 23),
    _TmnxMacMafMatchCfmOpCodeValue1_Type()
)
tmnxMacMafMatchCfmOpCodeValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchCfmOpCodeValue1.setStatus("current")


class _TmnxMacMafMatchCfmOpCodeValue2_Type(Unsigned32):
    """Custom type tmnxMacMafMatchCfmOpCodeValue2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxMacMafMatchCfmOpCodeValue2_Type.__name__ = "Unsigned32"
_TmnxMacMafMatchCfmOpCodeValue2_Object = MibTableColumn
tmnxMacMafMatchCfmOpCodeValue2 = _TmnxMacMafMatchCfmOpCodeValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 24),
    _TmnxMacMafMatchCfmOpCodeValue2_Type()
)
tmnxMacMafMatchCfmOpCodeValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMacMafMatchCfmOpCodeValue2.setStatus("current")
_TmnxMacMafMatchCount_Type = Counter64
_TmnxMacMafMatchCount_Object = MibTableColumn
tmnxMacMafMatchCount = _TmnxMacMafMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 4, 8, 1, 25),
    _TmnxMacMafMatchCount_Type()
)
tmnxMacMafMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMacMafMatchCount.setStatus("current")
_TmnxPasswordInfo_ObjectIdentity = ObjectIdentity
tmnxPasswordInfo = _TmnxPasswordInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5)
)


class _TmnxPasswordAging_Type(Unsigned32):
    """Custom type tmnxPasswordAging based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
        ValueRangeConstraint(65535, 65535),
    )


_TmnxPasswordAging_Type.__name__ = "Unsigned32"
_TmnxPasswordAging_Object = MibScalar
tmnxPasswordAging = _TmnxPasswordAging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 1),
    _TmnxPasswordAging_Type()
)
tmnxPasswordAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAging.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPasswordAging.setUnits("Days")


class _TmnxPasswordMinLength_Type(Unsigned32):
    """Custom type tmnxPasswordMinLength based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 50),
    )


_TmnxPasswordMinLength_Type.__name__ = "Unsigned32"
_TmnxPasswordMinLength_Object = MibScalar
tmnxPasswordMinLength = _TmnxPasswordMinLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 2),
    _TmnxPasswordMinLength_Type()
)
tmnxPasswordMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordMinLength.setStatus("current")


class _TmnxPasswordComplexity_Type(Bits):
    """Custom type tmnxPasswordComplexity based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("alpha-numeric", 0),
          ("mixed-case", 1),
          ("special-character", 2))
    )

_TmnxPasswordComplexity_Type.__name__ = "Bits"
_TmnxPasswordComplexity_Object = MibScalar
tmnxPasswordComplexity = _TmnxPasswordComplexity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 3),
    _TmnxPasswordComplexity_Type()
)
tmnxPasswordComplexity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordComplexity.setStatus("obsolete")


class _TmnxPasswordAttemptsCount_Type(Unsigned32):
    """Custom type tmnxPasswordAttemptsCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxPasswordAttemptsCount_Type.__name__ = "Unsigned32"
_TmnxPasswordAttemptsCount_Object = MibScalar
tmnxPasswordAttemptsCount = _TmnxPasswordAttemptsCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 4),
    _TmnxPasswordAttemptsCount_Type()
)
tmnxPasswordAttemptsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAttemptsCount.setStatus("current")


class _TmnxPasswordAttemptsTime_Type(Unsigned32):
    """Custom type tmnxPasswordAttemptsTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TmnxPasswordAttemptsTime_Type.__name__ = "Unsigned32"
_TmnxPasswordAttemptsTime_Object = MibScalar
tmnxPasswordAttemptsTime = _TmnxPasswordAttemptsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 5),
    _TmnxPasswordAttemptsTime_Type()
)
tmnxPasswordAttemptsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAttemptsTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPasswordAttemptsTime.setUnits("Minutes")


class _TmnxPasswordAttemptsLockoutPeriod_Type(Unsigned32):
    """Custom type tmnxPasswordAttemptsLockoutPeriod based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TmnxPasswordAttemptsLockoutPeriod_Type.__name__ = "Unsigned32"
_TmnxPasswordAttemptsLockoutPeriod_Object = MibScalar
tmnxPasswordAttemptsLockoutPeriod = _TmnxPasswordAttemptsLockoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 6),
    _TmnxPasswordAttemptsLockoutPeriod_Type()
)
tmnxPasswordAttemptsLockoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAttemptsLockoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPasswordAttemptsLockoutPeriod.setUnits("Minutes")


class _TmnxPasswordAuthenOrder1_Type(Integer32):
    """Custom type tmnxPasswordAuthenOrder1 based on Integer32"""
    defaultValue = 2

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
          ("local", 1),
          ("radius", 2),
          ("tacplus", 3))
    )


_TmnxPasswordAuthenOrder1_Type.__name__ = "Integer32"
_TmnxPasswordAuthenOrder1_Object = MibScalar
tmnxPasswordAuthenOrder1 = _TmnxPasswordAuthenOrder1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 7),
    _TmnxPasswordAuthenOrder1_Type()
)
tmnxPasswordAuthenOrder1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAuthenOrder1.setStatus("current")


class _TmnxPasswordAuthenOrder2_Type(Integer32):
    """Custom type tmnxPasswordAuthenOrder2 based on Integer32"""
    defaultValue = 3

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
          ("local", 1),
          ("radius", 2),
          ("tacplus", 3))
    )


_TmnxPasswordAuthenOrder2_Type.__name__ = "Integer32"
_TmnxPasswordAuthenOrder2_Object = MibScalar
tmnxPasswordAuthenOrder2 = _TmnxPasswordAuthenOrder2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 8),
    _TmnxPasswordAuthenOrder2_Type()
)
tmnxPasswordAuthenOrder2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAuthenOrder2.setStatus("current")


class _TmnxPasswordAuthenOrder3_Type(Integer32):
    """Custom type tmnxPasswordAuthenOrder3 based on Integer32"""
    defaultValue = 1

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
          ("local", 1),
          ("radius", 2),
          ("tacplus", 3))
    )


_TmnxPasswordAuthenOrder3_Type.__name__ = "Integer32"
_TmnxPasswordAuthenOrder3_Object = MibScalar
tmnxPasswordAuthenOrder3 = _TmnxPasswordAuthenOrder3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 9),
    _TmnxPasswordAuthenOrder3_Type()
)
tmnxPasswordAuthenOrder3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAuthenOrder3.setStatus("current")


class _TmnxPasswordAuthenExitOnReject_Type(TruthValue):
    """Custom type tmnxPasswordAuthenExitOnReject based on TruthValue"""
    defaultValue = 2


_TmnxPasswordAuthenExitOnReject_Type.__name__ = "TruthValue"
_TmnxPasswordAuthenExitOnReject_Object = MibScalar
tmnxPasswordAuthenExitOnReject = _TmnxPasswordAuthenExitOnReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 10),
    _TmnxPasswordAuthenExitOnReject_Type()
)
tmnxPasswordAuthenExitOnReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAuthenExitOnReject.setStatus("current")


class _TmnxAdminPassword_Type(OctetString):
    """Custom type tmnxAdminPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_TmnxAdminPassword_Type.__name__ = "OctetString"
_TmnxAdminPassword_Object = MibScalar
tmnxAdminPassword = _TmnxAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 11),
    _TmnxAdminPassword_Type()
)
tmnxAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxAdminPassword.setStatus("current")


class _TmnxAdminPasswordEncrypted_Type(TruthValue):
    """Custom type tmnxAdminPasswordEncrypted based on TruthValue"""
    defaultValue = 1


_TmnxAdminPasswordEncrypted_Type.__name__ = "TruthValue"
_TmnxAdminPasswordEncrypted_Object = MibScalar
tmnxAdminPasswordEncrypted = _TmnxAdminPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 12),
    _TmnxAdminPasswordEncrypted_Type()
)
tmnxAdminPasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxAdminPasswordEncrypted.setStatus("current")


class _TmnxPasswordHealthCheck_Type(TruthValue):
    """Custom type tmnxPasswordHealthCheck based on TruthValue"""
    defaultValue = 1


_TmnxPasswordHealthCheck_Type.__name__ = "TruthValue"
_TmnxPasswordHealthCheck_Object = MibScalar
tmnxPasswordHealthCheck = _TmnxPasswordHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 13),
    _TmnxPasswordHealthCheck_Type()
)
tmnxPasswordHealthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordHealthCheck.setStatus("current")


class _TmnxPasswordHealthCheckInterval_Type(Unsigned32):
    """Custom type tmnxPasswordHealthCheckInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 1500),
    )


_TmnxPasswordHealthCheckInterval_Type.__name__ = "Unsigned32"
_TmnxPasswordHealthCheckInterval_Object = MibScalar
tmnxPasswordHealthCheckInterval = _TmnxPasswordHealthCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 14),
    _TmnxPasswordHealthCheckInterval_Type()
)
tmnxPasswordHealthCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordHealthCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPasswordHealthCheckInterval.setUnits("seconds")


class _TmnxDynSvcPassword_Type(DisplayString):
    """Custom type tmnxDynSvcPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_TmnxDynSvcPassword_Type.__name__ = "DisplayString"
_TmnxDynSvcPassword_Object = MibScalar
tmnxDynSvcPassword = _TmnxDynSvcPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 15),
    _TmnxDynSvcPassword_Type()
)
tmnxDynSvcPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcPassword.setStatus("current")


class _TmnxTacPlusEnableAdminPrivLvl_Type(Integer32):
    """Custom type tmnxTacPlusEnableAdminPrivLvl based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_TmnxTacPlusEnableAdminPrivLvl_Type.__name__ = "Integer32"
_TmnxTacPlusEnableAdminPrivLvl_Object = MibScalar
tmnxTacPlusEnableAdminPrivLvl = _TmnxTacPlusEnableAdminPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 16),
    _TmnxTacPlusEnableAdminPrivLvl_Type()
)
tmnxTacPlusEnableAdminPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusEnableAdminPrivLvl.setStatus("current")


class _TmnxPasswordHistory_Type(Unsigned32):
    """Custom type tmnxPasswordHistory based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TmnxPasswordHistory_Type.__name__ = "Unsigned32"
_TmnxPasswordHistory_Object = MibScalar
tmnxPasswordHistory = _TmnxPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 17),
    _TmnxPasswordHistory_Type()
)
tmnxPasswordHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordHistory.setStatus("current")


class _TmnxPasswordMinChange_Type(Unsigned32):
    """Custom type tmnxPasswordMinChange based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxPasswordMinChange_Type.__name__ = "Unsigned32"
_TmnxPasswordMinChange_Object = MibScalar
tmnxPasswordMinChange = _TmnxPasswordMinChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 18),
    _TmnxPasswordMinChange_Type()
)
tmnxPasswordMinChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordMinChange.setStatus("current")


class _TmnxPasswordMinAge_Type(Unsigned32):
    """Custom type tmnxPasswordMinAge based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxPasswordMinAge_Type.__name__ = "Unsigned32"
_TmnxPasswordMinAge_Object = MibScalar
tmnxPasswordMinAge = _TmnxPasswordMinAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 19),
    _TmnxPasswordMinAge_Type()
)
tmnxPasswordMinAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordMinAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPasswordMinAge.setUnits("Seconds")


class _TmnxPasswordAllowUserName_Type(TruthValue):
    """Custom type tmnxPasswordAllowUserName based on TruthValue"""
    defaultValue = 2


_TmnxPasswordAllowUserName_Type.__name__ = "TruthValue"
_TmnxPasswordAllowUserName_Object = MibScalar
tmnxPasswordAllowUserName = _TmnxPasswordAllowUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 20),
    _TmnxPasswordAllowUserName_Type()
)
tmnxPasswordAllowUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordAllowUserName.setStatus("current")


class _TmnxPasswordMaxRepeatedChars_Type(Unsigned32):
    """Custom type tmnxPasswordMaxRepeatedChars based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 8),
    )


_TmnxPasswordMaxRepeatedChars_Type.__name__ = "Unsigned32"
_TmnxPasswordMaxRepeatedChars_Object = MibScalar
tmnxPasswordMaxRepeatedChars = _TmnxPasswordMaxRepeatedChars_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 21),
    _TmnxPasswordMaxRepeatedChars_Type()
)
tmnxPasswordMaxRepeatedChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordMaxRepeatedChars.setStatus("current")


class _TmnxPasswordCreditsLowerCase_Type(Unsigned32):
    """Custom type tmnxPasswordCreditsLowerCase based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordCreditsLowerCase_Type.__name__ = "Unsigned32"
_TmnxPasswordCreditsLowerCase_Object = MibScalar
tmnxPasswordCreditsLowerCase = _TmnxPasswordCreditsLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 22),
    _TmnxPasswordCreditsLowerCase_Type()
)
tmnxPasswordCreditsLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordCreditsLowerCase.setStatus("current")


class _TmnxPasswordCreditsUpperCase_Type(Unsigned32):
    """Custom type tmnxPasswordCreditsUpperCase based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordCreditsUpperCase_Type.__name__ = "Unsigned32"
_TmnxPasswordCreditsUpperCase_Object = MibScalar
tmnxPasswordCreditsUpperCase = _TmnxPasswordCreditsUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 23),
    _TmnxPasswordCreditsUpperCase_Type()
)
tmnxPasswordCreditsUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordCreditsUpperCase.setStatus("current")


class _TmnxPasswordCreditsNumeric_Type(Unsigned32):
    """Custom type tmnxPasswordCreditsNumeric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordCreditsNumeric_Type.__name__ = "Unsigned32"
_TmnxPasswordCreditsNumeric_Object = MibScalar
tmnxPasswordCreditsNumeric = _TmnxPasswordCreditsNumeric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 24),
    _TmnxPasswordCreditsNumeric_Type()
)
tmnxPasswordCreditsNumeric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordCreditsNumeric.setStatus("current")


class _TmnxPasswordCreditsSpecialChar_Type(Unsigned32):
    """Custom type tmnxPasswordCreditsSpecialChar based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordCreditsSpecialChar_Type.__name__ = "Unsigned32"
_TmnxPasswordCreditsSpecialChar_Object = MibScalar
tmnxPasswordCreditsSpecialChar = _TmnxPasswordCreditsSpecialChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 25),
    _TmnxPasswordCreditsSpecialChar_Type()
)
tmnxPasswordCreditsSpecialChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordCreditsSpecialChar.setStatus("current")


class _TmnxPasswordReqLowerCase_Type(Unsigned32):
    """Custom type tmnxPasswordReqLowerCase based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordReqLowerCase_Type.__name__ = "Unsigned32"
_TmnxPasswordReqLowerCase_Object = MibScalar
tmnxPasswordReqLowerCase = _TmnxPasswordReqLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 26),
    _TmnxPasswordReqLowerCase_Type()
)
tmnxPasswordReqLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordReqLowerCase.setStatus("current")


class _TmnxPasswordReqUpperCase_Type(Unsigned32):
    """Custom type tmnxPasswordReqUpperCase based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordReqUpperCase_Type.__name__ = "Unsigned32"
_TmnxPasswordReqUpperCase_Object = MibScalar
tmnxPasswordReqUpperCase = _TmnxPasswordReqUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 27),
    _TmnxPasswordReqUpperCase_Type()
)
tmnxPasswordReqUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordReqUpperCase.setStatus("current")


class _TmnxPasswordReqNumeric_Type(Unsigned32):
    """Custom type tmnxPasswordReqNumeric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordReqNumeric_Type.__name__ = "Unsigned32"
_TmnxPasswordReqNumeric_Object = MibScalar
tmnxPasswordReqNumeric = _TmnxPasswordReqNumeric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 28),
    _TmnxPasswordReqNumeric_Type()
)
tmnxPasswordReqNumeric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordReqNumeric.setStatus("current")


class _TmnxPasswordReqSpecialChar_Type(Unsigned32):
    """Custom type tmnxPasswordReqSpecialChar based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPasswordReqSpecialChar_Type.__name__ = "Unsigned32"
_TmnxPasswordReqSpecialChar_Object = MibScalar
tmnxPasswordReqSpecialChar = _TmnxPasswordReqSpecialChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 29),
    _TmnxPasswordReqSpecialChar_Type()
)
tmnxPasswordReqSpecialChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordReqSpecialChar.setStatus("current")


class _TmnxPasswordReqNumCharClass_Type(Unsigned32):
    """Custom type tmnxPasswordReqNumCharClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_TmnxPasswordReqNumCharClass_Type.__name__ = "Unsigned32"
_TmnxPasswordReqNumCharClass_Object = MibScalar
tmnxPasswordReqNumCharClass = _TmnxPasswordReqNumCharClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 5, 30),
    _TmnxPasswordReqNumCharClass_Type()
)
tmnxPasswordReqNumCharClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPasswordReqNumCharClass.setStatus("current")
_TmnxRadiusInfo_ObjectIdentity = ObjectIdentity
tmnxRadiusInfo = _TmnxRadiusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6)
)


class _TmnxRadiusAdminStatus_Type(Integer32):
    """Custom type tmnxRadiusAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxRadiusAdminStatus_Type.__name__ = "Integer32"
_TmnxRadiusAdminStatus_Object = MibScalar
tmnxRadiusAdminStatus = _TmnxRadiusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 1),
    _TmnxRadiusAdminStatus_Type()
)
tmnxRadiusAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusAdminStatus.setStatus("current")


class _TmnxRadiusAccounting_Type(TruthValue):
    """Custom type tmnxRadiusAccounting based on TruthValue"""
    defaultValue = 2


_TmnxRadiusAccounting_Type.__name__ = "TruthValue"
_TmnxRadiusAccounting_Object = MibScalar
tmnxRadiusAccounting = _TmnxRadiusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 2),
    _TmnxRadiusAccounting_Type()
)
tmnxRadiusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusAccounting.setStatus("current")


class _TmnxRadiusAuthorization_Type(TruthValue):
    """Custom type tmnxRadiusAuthorization based on TruthValue"""
    defaultValue = 2


_TmnxRadiusAuthorization_Type.__name__ = "TruthValue"
_TmnxRadiusAuthorization_Object = MibScalar
tmnxRadiusAuthorization = _TmnxRadiusAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 3),
    _TmnxRadiusAuthorization_Type()
)
tmnxRadiusAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusAuthorization.setStatus("current")


class _TmnxRadiusRetryAttempts_Type(Unsigned32):
    """Custom type tmnxRadiusRetryAttempts based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxRadiusRetryAttempts_Type.__name__ = "Unsigned32"
_TmnxRadiusRetryAttempts_Object = MibScalar
tmnxRadiusRetryAttempts = _TmnxRadiusRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 4),
    _TmnxRadiusRetryAttempts_Type()
)
tmnxRadiusRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusRetryAttempts.setStatus("current")


class _TmnxRadiusTimeout_Type(Unsigned32):
    """Custom type tmnxRadiusTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxRadiusTimeout_Type.__name__ = "Unsigned32"
_TmnxRadiusTimeout_Object = MibScalar
tmnxRadiusTimeout = _TmnxRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 5),
    _TmnxRadiusTimeout_Type()
)
tmnxRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadiusTimeout.setUnits("Seconds")


class _TmnxRadiusPort_Type(Unsigned32):
    """Custom type tmnxRadiusPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadiusPort_Type.__name__ = "Unsigned32"
_TmnxRadiusPort_Object = MibScalar
tmnxRadiusPort = _TmnxRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 6),
    _TmnxRadiusPort_Type()
)
tmnxRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusPort.setStatus("current")
_TmnxRadiusServerTable_Object = MibTable
tmnxRadiusServerTable = _TmnxRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7)
)
if mibBuilder.loadTexts:
    tmnxRadiusServerTable.setStatus("current")
_TmnxRadiusServerEntry_Object = MibTableRow
tmnxRadiusServerEntry = _TmnxRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1)
)
tmnxRadiusServerEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    tmnxRadiusServerEntry.setStatus("current")


class _TmnxRadiusServerIndex_Type(Unsigned32):
    """Custom type tmnxRadiusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxRadiusServerIndex_Type.__name__ = "Unsigned32"
_TmnxRadiusServerIndex_Object = MibTableColumn
tmnxRadiusServerIndex = _TmnxRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 1),
    _TmnxRadiusServerIndex_Type()
)
tmnxRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadiusServerIndex.setStatus("current")
_TmnxRadiusServerAddress_Type = IpAddress
_TmnxRadiusServerAddress_Object = MibTableColumn
tmnxRadiusServerAddress = _TmnxRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 2),
    _TmnxRadiusServerAddress_Type()
)
tmnxRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadiusServerAddress.setStatus("obsolete")


class _TmnxRadiusServerSecret_Type(OctetString):
    """Custom type tmnxRadiusServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxRadiusServerSecret_Type.__name__ = "OctetString"
_TmnxRadiusServerSecret_Object = MibTableColumn
tmnxRadiusServerSecret = _TmnxRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 3),
    _TmnxRadiusServerSecret_Type()
)
tmnxRadiusServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadiusServerSecret.setStatus("current")


class _TmnxRadiusServerOperStatus_Type(Integer32):
    """Custom type tmnxRadiusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxRadiusServerOperStatus_Type.__name__ = "Integer32"
_TmnxRadiusServerOperStatus_Object = MibTableColumn
tmnxRadiusServerOperStatus = _TmnxRadiusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 4),
    _TmnxRadiusServerOperStatus_Type()
)
tmnxRadiusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusServerOperStatus.setStatus("current")
_TmnxRadiusServerRowStatus_Type = RowStatus
_TmnxRadiusServerRowStatus_Object = MibTableColumn
tmnxRadiusServerRowStatus = _TmnxRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 5),
    _TmnxRadiusServerRowStatus_Type()
)
tmnxRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadiusServerRowStatus.setStatus("current")
_TmnxRadiusServerInetAddressType_Type = InetAddressType
_TmnxRadiusServerInetAddressType_Object = MibTableColumn
tmnxRadiusServerInetAddressType = _TmnxRadiusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 6),
    _TmnxRadiusServerInetAddressType_Type()
)
tmnxRadiusServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadiusServerInetAddressType.setStatus("current")


class _TmnxRadiusServerInetAddress_Type(InetAddress):
    """Custom type tmnxRadiusServerInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxRadiusServerInetAddress_Type.__name__ = "InetAddress"
_TmnxRadiusServerInetAddress_Object = MibTableColumn
tmnxRadiusServerInetAddress = _TmnxRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 7, 1, 7),
    _TmnxRadiusServerInetAddress_Type()
)
tmnxRadiusServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadiusServerInetAddress.setStatus("current")


class _TmnxRadiusSourceAddress_Type(IpAddress):
    """Custom type tmnxRadiusSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxRadiusSourceAddress_Type.__name__ = "IpAddress"
_TmnxRadiusSourceAddress_Object = MibScalar
tmnxRadiusSourceAddress = _TmnxRadiusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 8),
    _TmnxRadiusSourceAddress_Type()
)
tmnxRadiusSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusSourceAddress.setStatus("obsolete")


class _TmnxRadiusConfigured_Type(TruthValue):
    """Custom type tmnxRadiusConfigured based on TruthValue"""
    defaultValue = 2


_TmnxRadiusConfigured_Type.__name__ = "TruthValue"
_TmnxRadiusConfigured_Object = MibScalar
tmnxRadiusConfigured = _TmnxRadiusConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 9),
    _TmnxRadiusConfigured_Type()
)
tmnxRadiusConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusConfigured.setStatus("current")


class _TmnxRadiusPEDiscovery_Type(TruthValue):
    """Custom type tmnxRadiusPEDiscovery based on TruthValue"""
    defaultValue = 2


_TmnxRadiusPEDiscovery_Type.__name__ = "TruthValue"
_TmnxRadiusPEDiscovery_Object = MibScalar
tmnxRadiusPEDiscovery = _TmnxRadiusPEDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 10),
    _TmnxRadiusPEDiscovery_Type()
)
tmnxRadiusPEDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusPEDiscovery.setStatus("obsolete")


class _TmnxRadiusPEDiscoveryPassword_Type(OctetString):
    """Custom type tmnxRadiusPEDiscoveryPassword based on OctetString"""
    defaultHexValue = ""


_TmnxRadiusPEDiscoveryPassword_Type.__name__ = "OctetString"
_TmnxRadiusPEDiscoveryPassword_Object = MibScalar
tmnxRadiusPEDiscoveryPassword = _TmnxRadiusPEDiscoveryPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 11),
    _TmnxRadiusPEDiscoveryPassword_Type()
)
tmnxRadiusPEDiscoveryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusPEDiscoveryPassword.setStatus("obsolete")


class _TmnxRadiusPEDiscoveryInterval_Type(Unsigned32):
    """Custom type tmnxRadiusPEDiscoveryInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TmnxRadiusPEDiscoveryInterval_Type.__name__ = "Unsigned32"
_TmnxRadiusPEDiscoveryInterval_Object = MibScalar
tmnxRadiusPEDiscoveryInterval = _TmnxRadiusPEDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 12),
    _TmnxRadiusPEDiscoveryInterval_Type()
)
tmnxRadiusPEDiscoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusPEDiscoveryInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxRadiusPEDiscoveryInterval.setUnits("minutes")


class _TmnxRadiusPEForceDiscovery_Type(TmnxActionType):
    """Custom type tmnxRadiusPEForceDiscovery based on TmnxActionType"""
    defaultValue = 2


_TmnxRadiusPEForceDiscovery_Type.__name__ = "TmnxActionType"
_TmnxRadiusPEForceDiscovery_Object = MibScalar
tmnxRadiusPEForceDiscovery = _TmnxRadiusPEForceDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 13),
    _TmnxRadiusPEForceDiscovery_Type()
)
tmnxRadiusPEForceDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusPEForceDiscovery.setStatus("current")


class _TmnxRadiusPEForceDiscoverySvcId_Type(Unsigned32):
    """Custom type tmnxRadiusPEForceDiscoverySvcId based on Unsigned32"""
    defaultValue = 0


_TmnxRadiusPEForceDiscoverySvcId_Type.__name__ = "Unsigned32"
_TmnxRadiusPEForceDiscoverySvcId_Object = MibScalar
tmnxRadiusPEForceDiscoverySvcId = _TmnxRadiusPEForceDiscoverySvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 14),
    _TmnxRadiusPEForceDiscoverySvcId_Type()
)
tmnxRadiusPEForceDiscoverySvcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusPEForceDiscoverySvcId.setStatus("current")


class _TmnxRadiusAccountingPort_Type(Unsigned32):
    """Custom type tmnxRadiusAccountingPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadiusAccountingPort_Type.__name__ = "Unsigned32"
_TmnxRadiusAccountingPort_Object = MibScalar
tmnxRadiusAccountingPort = _TmnxRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 15),
    _TmnxRadiusAccountingPort_Type()
)
tmnxRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusAccountingPort.setStatus("current")


class _TmnxRadiusUseTemplate_Type(TruthValue):
    """Custom type tmnxRadiusUseTemplate based on TruthValue"""
    defaultValue = 2


_TmnxRadiusUseTemplate_Type.__name__ = "TruthValue"
_TmnxRadiusUseTemplate_Object = MibScalar
tmnxRadiusUseTemplate = _TmnxRadiusUseTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 16),
    _TmnxRadiusUseTemplate_Type()
)
tmnxRadiusUseTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusUseTemplate.setStatus("current")


class _TmnxRadiusAuthAlgorithm_Type(TmnxSecRadiusServAlgorithm):
    """Custom type tmnxRadiusAuthAlgorithm based on TmnxSecRadiusServAlgorithm"""
    defaultValue = 1


_TmnxRadiusAuthAlgorithm_Type.__name__ = "TmnxSecRadiusServAlgorithm"
_TmnxRadiusAuthAlgorithm_Object = MibScalar
tmnxRadiusAuthAlgorithm = _TmnxRadiusAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 17),
    _TmnxRadiusAuthAlgorithm_Type()
)
tmnxRadiusAuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadiusAuthAlgorithm.setStatus("current")
_TmnxRadiusUserStatsTable_Object = MibTable
tmnxRadiusUserStatsTable = _TmnxRadiusUserStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18)
)
if mibBuilder.loadTexts:
    tmnxRadiusUserStatsTable.setStatus("current")
_TmnxRadiusUserStatsEntry_Object = MibTableRow
tmnxRadiusUserStatsEntry = _TmnxRadiusUserStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1)
)
tmnxRadiusUserStatsEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxUserName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxRadiusPolicyName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxRadiusUserServerIndex"),
)
if mibBuilder.loadTexts:
    tmnxRadiusUserStatsEntry.setStatus("current")
_TmnxRadiusPolicyName_Type = TNamedItem
_TmnxRadiusPolicyName_Object = MibTableColumn
tmnxRadiusPolicyName = _TmnxRadiusPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 1),
    _TmnxRadiusPolicyName_Type()
)
tmnxRadiusPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadiusPolicyName.setStatus("current")


class _TmnxRadiusUserServerIndex_Type(Unsigned32):
    """Custom type tmnxRadiusUserServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxRadiusUserServerIndex_Type.__name__ = "Unsigned32"
_TmnxRadiusUserServerIndex_Object = MibTableColumn
tmnxRadiusUserServerIndex = _TmnxRadiusUserServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 2),
    _TmnxRadiusUserServerIndex_Type()
)
tmnxRadiusUserServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadiusUserServerIndex.setStatus("current")
_TmnxRadiusUserReqTx_Type = Counter32
_TmnxRadiusUserReqTx_Object = MibTableColumn
tmnxRadiusUserReqTx = _TmnxRadiusUserReqTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 3),
    _TmnxRadiusUserReqTx_Type()
)
tmnxRadiusUserReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserReqTx.setStatus("current")
_TmnxRadiusUserReqRx_Type = Counter32
_TmnxRadiusUserReqRx_Object = MibTableColumn
tmnxRadiusUserReqRx = _TmnxRadiusUserReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 4),
    _TmnxRadiusUserReqRx_Type()
)
tmnxRadiusUserReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserReqRx.setStatus("current")
_TmnxRadiusUserOpenFail_Type = Counter32
_TmnxRadiusUserOpenFail_Object = MibTableColumn
tmnxRadiusUserOpenFail = _TmnxRadiusUserOpenFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 5),
    _TmnxRadiusUserOpenFail_Type()
)
tmnxRadiusUserOpenFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserOpenFail.setStatus("current")
_TmnxRadiusUserBindFail_Type = Counter32
_TmnxRadiusUserBindFail_Object = MibTableColumn
tmnxRadiusUserBindFail = _TmnxRadiusUserBindFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 6),
    _TmnxRadiusUserBindFail_Type()
)
tmnxRadiusUserBindFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserBindFail.setStatus("current")
_TmnxRadiusUserSendFail_Type = Counter32
_TmnxRadiusUserSendFail_Object = MibTableColumn
tmnxRadiusUserSendFail = _TmnxRadiusUserSendFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 7),
    _TmnxRadiusUserSendFail_Type()
)
tmnxRadiusUserSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserSendFail.setStatus("current")
_TmnxRadiusUserRecvFail_Type = Counter32
_TmnxRadiusUserRecvFail_Object = MibTableColumn
tmnxRadiusUserRecvFail = _TmnxRadiusUserRecvFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 8),
    _TmnxRadiusUserRecvFail_Type()
)
tmnxRadiusUserRecvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserRecvFail.setStatus("current")
_TmnxRadiusUserSendTimeout_Type = Counter32
_TmnxRadiusUserSendTimeout_Object = MibTableColumn
tmnxRadiusUserSendTimeout = _TmnxRadiusUserSendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 9),
    _TmnxRadiusUserSendTimeout_Type()
)
tmnxRadiusUserSendTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserSendTimeout.setStatus("current")
_TmnxRadiusUserLoginPass_Type = Counter32
_TmnxRadiusUserLoginPass_Object = MibTableColumn
tmnxRadiusUserLoginPass = _TmnxRadiusUserLoginPass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 10),
    _TmnxRadiusUserLoginPass_Type()
)
tmnxRadiusUserLoginPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserLoginPass.setStatus("current")
_TmnxRadiusUserLoginFail_Type = Counter32
_TmnxRadiusUserLoginFail_Object = MibTableColumn
tmnxRadiusUserLoginFail = _TmnxRadiusUserLoginFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 11),
    _TmnxRadiusUserLoginFail_Type()
)
tmnxRadiusUserLoginFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserLoginFail.setStatus("current")
_TmnxRadiusUserMd5Fail_Type = Counter32
_TmnxRadiusUserMd5Fail_Object = MibTableColumn
tmnxRadiusUserMd5Fail = _TmnxRadiusUserMd5Fail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 12),
    _TmnxRadiusUserMd5Fail_Type()
)
tmnxRadiusUserMd5Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserMd5Fail.setStatus("current")
_TmnxRadiusUserPending_Type = Counter32
_TmnxRadiusUserPending_Object = MibTableColumn
tmnxRadiusUserPending = _TmnxRadiusUserPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 13),
    _TmnxRadiusUserPending_Type()
)
tmnxRadiusUserPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserPending.setStatus("current")
_TmnxRadiusUserAcctReqTx_Type = Counter32
_TmnxRadiusUserAcctReqTx_Object = MibTableColumn
tmnxRadiusUserAcctReqTx = _TmnxRadiusUserAcctReqTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 14),
    _TmnxRadiusUserAcctReqTx_Type()
)
tmnxRadiusUserAcctReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserAcctReqTx.setStatus("current")
_TmnxRadiusUserAcctRejRx_Type = Counter32
_TmnxRadiusUserAcctRejRx_Object = MibTableColumn
tmnxRadiusUserAcctRejRx = _TmnxRadiusUserAcctRejRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 15),
    _TmnxRadiusUserAcctRejRx_Type()
)
tmnxRadiusUserAcctRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserAcctRejRx.setStatus("current")
_TmnxRadiusUserAcctConnError_Type = Counter32
_TmnxRadiusUserAcctConnError_Object = MibTableColumn
tmnxRadiusUserAcctConnError = _TmnxRadiusUserAcctConnError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 16),
    _TmnxRadiusUserAcctConnError_Type()
)
tmnxRadiusUserAcctConnError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserAcctConnError.setStatus("current")
_TmnxRadiusUserAccChallengePkt_Type = Counter32
_TmnxRadiusUserAccChallengePkt_Object = MibTableColumn
tmnxRadiusUserAccChallengePkt = _TmnxRadiusUserAccChallengePkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 17),
    _TmnxRadiusUserAccChallengePkt_Type()
)
tmnxRadiusUserAccChallengePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserAccChallengePkt.setStatus("current")
_TmnxRadiusUserAuthAvgDelay_Type = Gauge32
_TmnxRadiusUserAuthAvgDelay_Object = MibTableColumn
tmnxRadiusUserAuthAvgDelay = _TmnxRadiusUserAuthAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 18),
    _TmnxRadiusUserAuthAvgDelay_Type()
)
tmnxRadiusUserAuthAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserAuthAvgDelay.setStatus("current")
_TmnxRadiusUserAcctAvgDelay_Type = Gauge32
_TmnxRadiusUserAcctAvgDelay_Object = MibTableColumn
tmnxRadiusUserAcctAvgDelay = _TmnxRadiusUserAcctAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 6, 18, 1, 19),
    _TmnxRadiusUserAcctAvgDelay_Type()
)
tmnxRadiusUserAcctAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadiusUserAcctAvgDelay.setStatus("current")
_TmnxTacPlusInfo_ObjectIdentity = ObjectIdentity
tmnxTacPlusInfo = _TmnxTacPlusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7)
)


class _TmnxTacPlusAdminStatus_Type(Integer32):
    """Custom type tmnxTacPlusAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxTacPlusAdminStatus_Type.__name__ = "Integer32"
_TmnxTacPlusAdminStatus_Object = MibScalar
tmnxTacPlusAdminStatus = _TmnxTacPlusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 1),
    _TmnxTacPlusAdminStatus_Type()
)
tmnxTacPlusAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusAdminStatus.setStatus("current")


class _TmnxTacPlusTimeout_Type(Unsigned32):
    """Custom type tmnxTacPlusTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxTacPlusTimeout_Type.__name__ = "Unsigned32"
_TmnxTacPlusTimeout_Object = MibScalar
tmnxTacPlusTimeout = _TmnxTacPlusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 2),
    _TmnxTacPlusTimeout_Type()
)
tmnxTacPlusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTacPlusTimeout.setUnits("Seconds")
_TmnxTacPlusServerTable_Object = MibTable
tmnxTacPlusServerTable = _TmnxTacPlusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3)
)
if mibBuilder.loadTexts:
    tmnxTacPlusServerTable.setStatus("current")
_TmnxTacPlusServerEntry_Object = MibTableRow
tmnxTacPlusServerEntry = _TmnxTacPlusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1)
)
tmnxTacPlusServerEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxTacPlusServerIndex"),
)
if mibBuilder.loadTexts:
    tmnxTacPlusServerEntry.setStatus("current")


class _TmnxTacPlusServerIndex_Type(Unsigned32):
    """Custom type tmnxTacPlusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxTacPlusServerIndex_Type.__name__ = "Unsigned32"
_TmnxTacPlusServerIndex_Object = MibTableColumn
tmnxTacPlusServerIndex = _TmnxTacPlusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 1),
    _TmnxTacPlusServerIndex_Type()
)
tmnxTacPlusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTacPlusServerIndex.setStatus("current")
_TmnxTacPlusServerAddress_Type = IpAddress
_TmnxTacPlusServerAddress_Object = MibTableColumn
tmnxTacPlusServerAddress = _TmnxTacPlusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 2),
    _TmnxTacPlusServerAddress_Type()
)
tmnxTacPlusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusServerAddress.setStatus("obsolete")


class _TmnxTacPlusServerSecret_Type(OctetString):
    """Custom type tmnxTacPlusServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxTacPlusServerSecret_Type.__name__ = "OctetString"
_TmnxTacPlusServerSecret_Object = MibTableColumn
tmnxTacPlusServerSecret = _TmnxTacPlusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 3),
    _TmnxTacPlusServerSecret_Type()
)
tmnxTacPlusServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusServerSecret.setStatus("current")
_TmnxTacPlusServerRowStatus_Type = RowStatus
_TmnxTacPlusServerRowStatus_Object = MibTableColumn
tmnxTacPlusServerRowStatus = _TmnxTacPlusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 4),
    _TmnxTacPlusServerRowStatus_Type()
)
tmnxTacPlusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusServerRowStatus.setStatus("current")


class _TmnxTacPlusServerOperStatus_Type(Integer32):
    """Custom type tmnxTacPlusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxTacPlusServerOperStatus_Type.__name__ = "Integer32"
_TmnxTacPlusServerOperStatus_Object = MibTableColumn
tmnxTacPlusServerOperStatus = _TmnxTacPlusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 5),
    _TmnxTacPlusServerOperStatus_Type()
)
tmnxTacPlusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTacPlusServerOperStatus.setStatus("current")
_TmnxTacPlusServerInetAddressType_Type = InetAddressType
_TmnxTacPlusServerInetAddressType_Object = MibTableColumn
tmnxTacPlusServerInetAddressType = _TmnxTacPlusServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 6),
    _TmnxTacPlusServerInetAddressType_Type()
)
tmnxTacPlusServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusServerInetAddressType.setStatus("current")


class _TmnxTacPlusServerInetAddress_Type(InetAddress):
    """Custom type tmnxTacPlusServerInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxTacPlusServerInetAddress_Type.__name__ = "InetAddress"
_TmnxTacPlusServerInetAddress_Object = MibTableColumn
tmnxTacPlusServerInetAddress = _TmnxTacPlusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 7),
    _TmnxTacPlusServerInetAddress_Type()
)
tmnxTacPlusServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusServerInetAddress.setStatus("current")


class _TmnxTacPlusServerPort_Type(TTcpUdpPort):
    """Custom type tmnxTacPlusServerPort based on TTcpUdpPort"""
    defaultValue = 49


_TmnxTacPlusServerPort_Type.__name__ = "TTcpUdpPort"
_TmnxTacPlusServerPort_Object = MibTableColumn
tmnxTacPlusServerPort = _TmnxTacPlusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 3, 1, 8),
    _TmnxTacPlusServerPort_Type()
)
tmnxTacPlusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusServerPort.setStatus("current")


class _TmnxTacPlusAccounting_Type(TruthValue):
    """Custom type tmnxTacPlusAccounting based on TruthValue"""
    defaultValue = 2


_TmnxTacPlusAccounting_Type.__name__ = "TruthValue"
_TmnxTacPlusAccounting_Object = MibScalar
tmnxTacPlusAccounting = _TmnxTacPlusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 4),
    _TmnxTacPlusAccounting_Type()
)
tmnxTacPlusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusAccounting.setStatus("current")


class _TmnxTacPlusAcctRecType_Type(Integer32):
    """Custom type tmnxTacPlusAcctRecType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startStop", 1),
          ("stopOnly", 2))
    )


_TmnxTacPlusAcctRecType_Type.__name__ = "Integer32"
_TmnxTacPlusAcctRecType_Object = MibScalar
tmnxTacPlusAcctRecType = _TmnxTacPlusAcctRecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 5),
    _TmnxTacPlusAcctRecType_Type()
)
tmnxTacPlusAcctRecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusAcctRecType.setStatus("current")


class _TmnxTacPlusAuthorization_Type(TruthValue):
    """Custom type tmnxTacPlusAuthorization based on TruthValue"""
    defaultValue = 2


_TmnxTacPlusAuthorization_Type.__name__ = "TruthValue"
_TmnxTacPlusAuthorization_Object = MibScalar
tmnxTacPlusAuthorization = _TmnxTacPlusAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 6),
    _TmnxTacPlusAuthorization_Type()
)
tmnxTacPlusAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusAuthorization.setStatus("current")


class _TmnxTacPlusSingleConnection_Type(TruthValue):
    """Custom type tmnxTacPlusSingleConnection based on TruthValue"""
    defaultValue = 2


_TmnxTacPlusSingleConnection_Type.__name__ = "TruthValue"
_TmnxTacPlusSingleConnection_Object = MibScalar
tmnxTacPlusSingleConnection = _TmnxTacPlusSingleConnection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 7),
    _TmnxTacPlusSingleConnection_Type()
)
tmnxTacPlusSingleConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusSingleConnection.setStatus("obsolete")


class _TmnxTacPlusSourceAddress_Type(IpAddress):
    """Custom type tmnxTacPlusSourceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TmnxTacPlusSourceAddress_Type.__name__ = "IpAddress"
_TmnxTacPlusSourceAddress_Object = MibScalar
tmnxTacPlusSourceAddress = _TmnxTacPlusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 8),
    _TmnxTacPlusSourceAddress_Type()
)
tmnxTacPlusSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusSourceAddress.setStatus("obsolete")


class _TmnxTacPlusConfigured_Type(TruthValue):
    """Custom type tmnxTacPlusConfigured based on TruthValue"""
    defaultValue = 2


_TmnxTacPlusConfigured_Type.__name__ = "TruthValue"
_TmnxTacPlusConfigured_Object = MibScalar
tmnxTacPlusConfigured = _TmnxTacPlusConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 9),
    _TmnxTacPlusConfigured_Type()
)
tmnxTacPlusConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusConfigured.setStatus("current")


class _TmnxTacplusUseTemplate_Type(TruthValue):
    """Custom type tmnxTacplusUseTemplate based on TruthValue"""
    defaultValue = 1


_TmnxTacplusUseTemplate_Type.__name__ = "TruthValue"
_TmnxTacplusUseTemplate_Object = MibScalar
tmnxTacplusUseTemplate = _TmnxTacplusUseTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 10),
    _TmnxTacplusUseTemplate_Type()
)
tmnxTacplusUseTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacplusUseTemplate.setStatus("current")


class _TmnxTacPlusInteractiveAuthen_Type(TruthValue):
    """Custom type tmnxTacPlusInteractiveAuthen based on TruthValue"""
    defaultValue = 2


_TmnxTacPlusInteractiveAuthen_Type.__name__ = "TruthValue"
_TmnxTacPlusInteractiveAuthen_Object = MibScalar
tmnxTacPlusInteractiveAuthen = _TmnxTacPlusInteractiveAuthen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 11),
    _TmnxTacPlusInteractiveAuthen_Type()
)
tmnxTacPlusInteractiveAuthen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusInteractiveAuthen.setStatus("current")


class _TmnxTacPlusAuthorUsePrivLvl_Type(TruthValue):
    """Custom type tmnxTacPlusAuthorUsePrivLvl based on TruthValue"""
    defaultValue = 2


_TmnxTacPlusAuthorUsePrivLvl_Type.__name__ = "TruthValue"
_TmnxTacPlusAuthorUsePrivLvl_Object = MibScalar
tmnxTacPlusAuthorUsePrivLvl = _TmnxTacPlusAuthorUsePrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 7, 12),
    _TmnxTacPlusAuthorUsePrivLvl_Type()
)
tmnxTacPlusAuthorUsePrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTacPlusAuthorUsePrivLvl.setStatus("current")
_TmnxServerCtlObjs_ObjectIdentity = ObjectIdentity
tmnxServerCtlObjs = _TmnxServerCtlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 8)
)


class _TmnxEnableServers_Type(Bits):
    """Custom type tmnxEnableServers based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("telnet", 0),
          ("ssh", 1),
          ("ftp", 2),
          ("telnet6", 3))
    )

_TmnxEnableServers_Type.__name__ = "Bits"
_TmnxEnableServers_Object = MibScalar
tmnxEnableServers = _TmnxEnableServers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 8, 1),
    _TmnxEnableServers_Type()
)
tmnxEnableServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxEnableServers.setStatus("current")
_TmnxTelnetServerOperStatus_Type = TmnxOperState
_TmnxTelnetServerOperStatus_Object = MibScalar
tmnxTelnetServerOperStatus = _TmnxTelnetServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 8, 2),
    _TmnxTelnetServerOperStatus_Type()
)
tmnxTelnetServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTelnetServerOperStatus.setStatus("current")
_TmnxSSHServerOperStatus_Type = TmnxOperState
_TmnxSSHServerOperStatus_Object = MibScalar
tmnxSSHServerOperStatus = _TmnxSSHServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 8, 3),
    _TmnxSSHServerOperStatus_Type()
)
tmnxSSHServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSSHServerOperStatus.setStatus("current")
_TmnxFTPServerOperStatus_Type = TmnxOperState
_TmnxFTPServerOperStatus_Object = MibScalar
tmnxFTPServerOperStatus = _TmnxFTPServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 8, 4),
    _TmnxFTPServerOperStatus_Type()
)
tmnxFTPServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFTPServerOperStatus.setStatus("current")
_TmnxTelnet6ServerOperStatus_Type = TmnxOperState
_TmnxTelnet6ServerOperStatus_Object = MibScalar
tmnxTelnet6ServerOperStatus = _TmnxTelnet6ServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 8, 5),
    _TmnxTelnet6ServerOperStatus_Type()
)
tmnxTelnet6ServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTelnet6ServerOperStatus.setStatus("current")
_TmnxCpmSecurityObjs_ObjectIdentity = ObjectIdentity
tmnxCpmSecurityObjs = _TmnxCpmSecurityObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9)
)


class _TmnxCpmPerPeerQueuing_Type(TruthValue):
    """Custom type tmnxCpmPerPeerQueuing based on TruthValue"""
    defaultValue = 2


_TmnxCpmPerPeerQueuing_Type.__name__ = "TruthValue"
_TmnxCpmPerPeerQueuing_Object = MibScalar
tmnxCpmPerPeerQueuing = _TmnxCpmPerPeerQueuing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 1),
    _TmnxCpmPerPeerQueuing_Type()
)
tmnxCpmPerPeerQueuing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmPerPeerQueuing.setStatus("current")
_TmnxCpmQueuesTotal_Type = Gauge32
_TmnxCpmQueuesTotal_Object = MibScalar
tmnxCpmQueuesTotal = _TmnxCpmQueuesTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 2),
    _TmnxCpmQueuesTotal_Type()
)
tmnxCpmQueuesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmQueuesTotal.setStatus("current")
_TmnxCpmQueuesInUse_Type = Gauge32
_TmnxCpmQueuesInUse_Object = MibScalar
tmnxCpmQueuesInUse = _TmnxCpmQueuesInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 3),
    _TmnxCpmQueuesInUse_Type()
)
tmnxCpmQueuesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmQueuesInUse.setStatus("current")
_TCpmFilterQueueTable_Object = MibTable
tCpmFilterQueueTable = _TCpmFilterQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4)
)
if mibBuilder.loadTexts:
    tCpmFilterQueueTable.setStatus("current")
_TCpmFilterQueueEntry_Object = MibTableRow
tCpmFilterQueueEntry = _TCpmFilterQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1)
)
tCpmFilterQueueEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmFilterQueueId"),
)
if mibBuilder.loadTexts:
    tCpmFilterQueueEntry.setStatus("current")


class _TCpmFilterQueueId_Type(TCpmFilterQueueId):
    """Custom type tCpmFilterQueueId based on TCpmFilterQueueId"""
    subtypeSpec = TCpmFilterQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 2000),
    )


_TCpmFilterQueueId_Type.__name__ = "TCpmFilterQueueId"
_TCpmFilterQueueId_Object = MibTableColumn
tCpmFilterQueueId = _TCpmFilterQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 1),
    _TCpmFilterQueueId_Type()
)
tCpmFilterQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tCpmFilterQueueId.setStatus("current")
_TCpmFilterQueueRowStatus_Type = RowStatus
_TCpmFilterQueueRowStatus_Object = MibTableColumn
tCpmFilterQueueRowStatus = _TCpmFilterQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 2),
    _TCpmFilterQueueRowStatus_Type()
)
tCpmFilterQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmFilterQueueRowStatus.setStatus("current")
_TCpmFilterQueueLastChanged_Type = TimeStamp
_TCpmFilterQueueLastChanged_Object = MibTableColumn
tCpmFilterQueueLastChanged = _TCpmFilterQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 3),
    _TCpmFilterQueueLastChanged_Type()
)
tCpmFilterQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQueueLastChanged.setStatus("current")


class _TCpmFilterQueueAdminPIR_Type(TPIRRate):
    """Custom type tCpmFilterQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TCpmFilterQueueAdminPIR_Type.__name__ = "TPIRRate"
_TCpmFilterQueueAdminPIR_Object = MibTableColumn
tCpmFilterQueueAdminPIR = _TCpmFilterQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 4),
    _TCpmFilterQueueAdminPIR_Type()
)
tCpmFilterQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmFilterQueueAdminPIR.setStatus("current")


class _TCpmFilterQueueAdminCIR_Type(TCIRRate):
    """Custom type tCpmFilterQueueAdminCIR based on TCIRRate"""
    defaultValue = -1


_TCpmFilterQueueAdminCIR_Type.__name__ = "TCIRRate"
_TCpmFilterQueueAdminCIR_Object = MibTableColumn
tCpmFilterQueueAdminCIR = _TCpmFilterQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 5),
    _TCpmFilterQueueAdminCIR_Type()
)
tCpmFilterQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmFilterQueueAdminCIR.setStatus("current")


class _TCpmFilterQueueCBS_Type(TBurstSize):
    """Custom type tCpmFilterQueueCBS based on TBurstSize"""
    defaultValue = -1


_TCpmFilterQueueCBS_Type.__name__ = "TBurstSize"
_TCpmFilterQueueCBS_Object = MibTableColumn
tCpmFilterQueueCBS = _TCpmFilterQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 6),
    _TCpmFilterQueueCBS_Type()
)
tCpmFilterQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmFilterQueueCBS.setStatus("current")


class _TCpmFilterQueueMBS_Type(TBurstSize):
    """Custom type tCpmFilterQueueMBS based on TBurstSize"""
    defaultValue = -1


_TCpmFilterQueueMBS_Type.__name__ = "TBurstSize"
_TCpmFilterQueueMBS_Object = MibTableColumn
tCpmFilterQueueMBS = _TCpmFilterQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 7),
    _TCpmFilterQueueMBS_Type()
)
tCpmFilterQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmFilterQueueMBS.setStatus("current")
_TCpmFilterQueueReferences_Type = Unsigned32
_TCpmFilterQueueReferences_Object = MibTableColumn
tCpmFilterQueueReferences = _TCpmFilterQueueReferences_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 8),
    _TCpmFilterQueueReferences_Type()
)
tCpmFilterQueueReferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQueueReferences.setStatus("current")
_TCpmFilterQueueOperPIR_Type = TPIRRateOrZero
_TCpmFilterQueueOperPIR_Object = MibTableColumn
tCpmFilterQueueOperPIR = _TCpmFilterQueueOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 9),
    _TCpmFilterQueueOperPIR_Type()
)
tCpmFilterQueueOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQueueOperPIR.setStatus("current")
_TCpmFilterQueueOperCIR_Type = TCIRRate
_TCpmFilterQueueOperCIR_Object = MibTableColumn
tCpmFilterQueueOperCIR = _TCpmFilterQueueOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 4, 1, 10),
    _TCpmFilterQueueOperCIR_Type()
)
tCpmFilterQueueOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQueueOperCIR.setStatus("current")
_TmnxCpmHwFilterObjs_ObjectIdentity = ObjectIdentity
tmnxCpmHwFilterObjs = _TmnxCpmHwFilterObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 5)
)


class _TCpmFilterDefaultAction_Type(TCpmFilterActionOrDefault):
    """Custom type tCpmFilterDefaultAction based on TCpmFilterActionOrDefault"""
    defaultValue = 2

    subtypeSpec = TCpmFilterActionOrDefault.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TCpmFilterDefaultAction_Type.__name__ = "TCpmFilterActionOrDefault"
_TCpmFilterDefaultAction_Object = MibScalar
tCpmFilterDefaultAction = _TCpmFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 5, 1),
    _TCpmFilterDefaultAction_Type()
)
tCpmFilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCpmFilterDefaultAction.setStatus("current")


class _TCpmIpFilterAdminState_Type(TmnxAdminState):
    """Custom type tCpmIpFilterAdminState based on TmnxAdminState"""
    defaultValue = 3


_TCpmIpFilterAdminState_Type.__name__ = "TmnxAdminState"
_TCpmIpFilterAdminState_Object = MibScalar
tCpmIpFilterAdminState = _TCpmIpFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 5, 2),
    _TCpmIpFilterAdminState_Type()
)
tCpmIpFilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCpmIpFilterAdminState.setStatus("current")


class _TCpmIPv6FilterAdminState_Type(TmnxAdminState):
    """Custom type tCpmIPv6FilterAdminState based on TmnxAdminState"""
    defaultValue = 3


_TCpmIPv6FilterAdminState_Type.__name__ = "TmnxAdminState"
_TCpmIPv6FilterAdminState_Object = MibScalar
tCpmIPv6FilterAdminState = _TCpmIPv6FilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 5, 3),
    _TCpmIPv6FilterAdminState_Type()
)
tCpmIPv6FilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCpmIPv6FilterAdminState.setStatus("current")


class _TCpmMacFilterAdminState_Type(TmnxAdminState):
    """Custom type tCpmMacFilterAdminState based on TmnxAdminState"""
    defaultValue = 3


_TCpmMacFilterAdminState_Type.__name__ = "TmnxAdminState"
_TCpmMacFilterAdminState_Object = MibScalar
tCpmMacFilterAdminState = _TCpmMacFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 5, 4),
    _TCpmMacFilterAdminState_Type()
)
tCpmMacFilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCpmMacFilterAdminState.setStatus("current")
_TCpmIpFilterTable_Object = MibTable
tCpmIpFilterTable = _TCpmIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6)
)
if mibBuilder.loadTexts:
    tCpmIpFilterTable.setStatus("current")
_TCpmIpFilterEntry_Object = MibTableRow
tCpmIpFilterEntry = _TCpmIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1)
)
tCpmIpFilterEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryId"),
)
if mibBuilder.loadTexts:
    tCpmIpFilterEntry.setStatus("current")


class _TCpmIpFilterEntryId_Type(TEntryId):
    """Custom type tCpmIpFilterEntryId based on TEntryId"""
    subtypeSpec = TEntryId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TCpmIpFilterEntryId_Type.__name__ = "TEntryId"
_TCpmIpFilterEntryId_Object = MibTableColumn
tCpmIpFilterEntryId = _TCpmIpFilterEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 1),
    _TCpmIpFilterEntryId_Type()
)
tCpmIpFilterEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryId.setStatus("current")
_TCpmIpFilterEntryRowStatus_Type = RowStatus
_TCpmIpFilterEntryRowStatus_Object = MibTableColumn
tCpmIpFilterEntryRowStatus = _TCpmIpFilterEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 2),
    _TCpmIpFilterEntryRowStatus_Type()
)
tCpmIpFilterEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryRowStatus.setStatus("current")
_TCpmIpFilterEntryLastChanged_Type = TimeStamp
_TCpmIpFilterEntryLastChanged_Object = MibTableColumn
tCpmIpFilterEntryLastChanged = _TCpmIpFilterEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 3),
    _TCpmIpFilterEntryLastChanged_Type()
)
tCpmIpFilterEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryLastChanged.setStatus("current")


class _TCpmIpFilterEntryLogId_Type(TFilterLogId):
    """Custom type tCpmIpFilterEntryLogId based on TFilterLogId"""
    defaultValue = 0


_TCpmIpFilterEntryLogId_Type.__name__ = "TFilterLogId"
_TCpmIpFilterEntryLogId_Object = MibTableColumn
tCpmIpFilterEntryLogId = _TCpmIpFilterEntryLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 4),
    _TCpmIpFilterEntryLogId_Type()
)
tCpmIpFilterEntryLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryLogId.setStatus("current")


class _TCpmIpFilterEntryDescription_Type(TItemDescription):
    """Custom type tCpmIpFilterEntryDescription based on TItemDescription"""
    defaultHexValue = ""


_TCpmIpFilterEntryDescription_Type.__name__ = "TItemDescription"
_TCpmIpFilterEntryDescription_Object = MibTableColumn
tCpmIpFilterEntryDescription = _TCpmIpFilterEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 5),
    _TCpmIpFilterEntryDescription_Type()
)
tCpmIpFilterEntryDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDescription.setStatus("current")


class _TCpmIpFilterEntryAction_Type(TCpmFilterActionOrDefault):
    """Custom type tCpmIpFilterEntryAction based on TCpmFilterActionOrDefault"""
    defaultValue = 1


_TCpmIpFilterEntryAction_Type.__name__ = "TCpmFilterActionOrDefault"
_TCpmIpFilterEntryAction_Object = MibTableColumn
tCpmIpFilterEntryAction = _TCpmIpFilterEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 6),
    _TCpmIpFilterEntryAction_Type()
)
tCpmIpFilterEntryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryAction.setStatus("current")


class _TCpmIpFilterEntryQueueId_Type(TCpmFilterQueueId):
    """Custom type tCpmIpFilterEntryQueueId based on TCpmFilterQueueId"""
    defaultValue = 0


_TCpmIpFilterEntryQueueId_Type.__name__ = "TCpmFilterQueueId"
_TCpmIpFilterEntryQueueId_Object = MibTableColumn
tCpmIpFilterEntryQueueId = _TCpmIpFilterEntryQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 7),
    _TCpmIpFilterEntryQueueId_Type()
)
tCpmIpFilterEntryQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryQueueId.setStatus("current")


class _TCpmIpFilterEntrySrcIPAddr_Type(IpAddress):
    """Custom type tCpmIpFilterEntrySrcIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TCpmIpFilterEntrySrcIPAddr_Type.__name__ = "IpAddress"
_TCpmIpFilterEntrySrcIPAddr_Object = MibTableColumn
tCpmIpFilterEntrySrcIPAddr = _TCpmIpFilterEntrySrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 8),
    _TCpmIpFilterEntrySrcIPAddr_Type()
)
tCpmIpFilterEntrySrcIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcIPAddr.setStatus("current")


class _TCpmIpFilterEntrySrcIPMask_Type(IpAddressPrefixLength):
    """Custom type tCpmIpFilterEntrySrcIPMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TCpmIpFilterEntrySrcIPMask_Type.__name__ = "IpAddressPrefixLength"
_TCpmIpFilterEntrySrcIPMask_Object = MibTableColumn
tCpmIpFilterEntrySrcIPMask = _TCpmIpFilterEntrySrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 9),
    _TCpmIpFilterEntrySrcIPMask_Type()
)
tCpmIpFilterEntrySrcIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcIPMask.setStatus("current")


class _TCpmIpFilterEntryDestIPAddr_Type(IpAddress):
    """Custom type tCpmIpFilterEntryDestIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TCpmIpFilterEntryDestIPAddr_Type.__name__ = "IpAddress"
_TCpmIpFilterEntryDestIPAddr_Object = MibTableColumn
tCpmIpFilterEntryDestIPAddr = _TCpmIpFilterEntryDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 10),
    _TCpmIpFilterEntryDestIPAddr_Type()
)
tCpmIpFilterEntryDestIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDestIPAddr.setStatus("current")


class _TCpmIpFilterEntryDestIPMask_Type(IpAddressPrefixLength):
    """Custom type tCpmIpFilterEntryDestIPMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TCpmIpFilterEntryDestIPMask_Type.__name__ = "IpAddressPrefixLength"
_TCpmIpFilterEntryDestIPMask_Object = MibTableColumn
tCpmIpFilterEntryDestIPMask = _TCpmIpFilterEntryDestIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 11),
    _TCpmIpFilterEntryDestIPMask_Type()
)
tCpmIpFilterEntryDestIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDestIPMask.setStatus("current")


class _TCpmIpFilterEntryProtocol_Type(TIpProtocol):
    """Custom type tCpmIpFilterEntryProtocol based on TIpProtocol"""
    defaultValue = -1


_TCpmIpFilterEntryProtocol_Type.__name__ = "TIpProtocol"
_TCpmIpFilterEntryProtocol_Object = MibTableColumn
tCpmIpFilterEntryProtocol = _TCpmIpFilterEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 12),
    _TCpmIpFilterEntryProtocol_Type()
)
tCpmIpFilterEntryProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryProtocol.setStatus("current")


class _TCpmIpFilterEntrySrcPort_Type(TTcpUdpPort):
    """Custom type tCpmIpFilterEntrySrcPort based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIpFilterEntrySrcPort_Type.__name__ = "TTcpUdpPort"
_TCpmIpFilterEntrySrcPort_Object = MibTableColumn
tCpmIpFilterEntrySrcPort = _TCpmIpFilterEntrySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 13),
    _TCpmIpFilterEntrySrcPort_Type()
)
tCpmIpFilterEntrySrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcPort.setStatus("current")


class _TCpmIpFilterEntrySrcPortMask_Type(Integer32):
    """Custom type tCpmIpFilterEntrySrcPortMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TCpmIpFilterEntrySrcPortMask_Type.__name__ = "Integer32"
_TCpmIpFilterEntrySrcPortMask_Object = MibTableColumn
tCpmIpFilterEntrySrcPortMask = _TCpmIpFilterEntrySrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 14),
    _TCpmIpFilterEntrySrcPortMask_Type()
)
tCpmIpFilterEntrySrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcPortMask.setStatus("current")


class _TCpmIpFilterEntryDestPort_Type(TTcpUdpPort):
    """Custom type tCpmIpFilterEntryDestPort based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIpFilterEntryDestPort_Type.__name__ = "TTcpUdpPort"
_TCpmIpFilterEntryDestPort_Object = MibTableColumn
tCpmIpFilterEntryDestPort = _TCpmIpFilterEntryDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 15),
    _TCpmIpFilterEntryDestPort_Type()
)
tCpmIpFilterEntryDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDestPort.setStatus("current")


class _TCpmIpFilterEntryDestPortMask_Type(Integer32):
    """Custom type tCpmIpFilterEntryDestPortMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TCpmIpFilterEntryDestPortMask_Type.__name__ = "Integer32"
_TCpmIpFilterEntryDestPortMask_Object = MibTableColumn
tCpmIpFilterEntryDestPortMask = _TCpmIpFilterEntryDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 16),
    _TCpmIpFilterEntryDestPortMask_Type()
)
tCpmIpFilterEntryDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDestPortMask.setStatus("current")


class _TCpmIpFilterEntryDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tCpmIpFilterEntryDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TCpmIpFilterEntryDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TCpmIpFilterEntryDSCP_Object = MibTableColumn
tCpmIpFilterEntryDSCP = _TCpmIpFilterEntryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 17),
    _TCpmIpFilterEntryDSCP_Type()
)
tCpmIpFilterEntryDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDSCP.setStatus("current")


class _TCpmIpFilterEntryFragment_Type(TItemMatch):
    """Custom type tCpmIpFilterEntryFragment based on TItemMatch"""
    defaultValue = 1


_TCpmIpFilterEntryFragment_Type.__name__ = "TItemMatch"
_TCpmIpFilterEntryFragment_Object = MibTableColumn
tCpmIpFilterEntryFragment = _TCpmIpFilterEntryFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 18),
    _TCpmIpFilterEntryFragment_Type()
)
tCpmIpFilterEntryFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryFragment.setStatus("current")


class _TCpmIpFilterEntryOptionPresent_Type(TItemMatch):
    """Custom type tCpmIpFilterEntryOptionPresent based on TItemMatch"""
    defaultValue = 1


_TCpmIpFilterEntryOptionPresent_Type.__name__ = "TItemMatch"
_TCpmIpFilterEntryOptionPresent_Object = MibTableColumn
tCpmIpFilterEntryOptionPresent = _TCpmIpFilterEntryOptionPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 19),
    _TCpmIpFilterEntryOptionPresent_Type()
)
tCpmIpFilterEntryOptionPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryOptionPresent.setStatus("current")


class _TCpmIpFilterEntryIPOptionValue_Type(TIpOption):
    """Custom type tCpmIpFilterEntryIPOptionValue based on TIpOption"""
    defaultValue = 0


_TCpmIpFilterEntryIPOptionValue_Type.__name__ = "TIpOption"
_TCpmIpFilterEntryIPOptionValue_Object = MibTableColumn
tCpmIpFilterEntryIPOptionValue = _TCpmIpFilterEntryIPOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 20),
    _TCpmIpFilterEntryIPOptionValue_Type()
)
tCpmIpFilterEntryIPOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryIPOptionValue.setStatus("current")


class _TCpmIpFilterEntryIPOptionMask_Type(TIpOption):
    """Custom type tCpmIpFilterEntryIPOptionMask based on TIpOption"""
    defaultValue = 0


_TCpmIpFilterEntryIPOptionMask_Type.__name__ = "TIpOption"
_TCpmIpFilterEntryIPOptionMask_Object = MibTableColumn
tCpmIpFilterEntryIPOptionMask = _TCpmIpFilterEntryIPOptionMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 21),
    _TCpmIpFilterEntryIPOptionMask_Type()
)
tCpmIpFilterEntryIPOptionMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryIPOptionMask.setStatus("current")


class _TCpmIpFilterEntryMultipleOption_Type(TItemMatch):
    """Custom type tCpmIpFilterEntryMultipleOption based on TItemMatch"""
    defaultValue = 1


_TCpmIpFilterEntryMultipleOption_Type.__name__ = "TItemMatch"
_TCpmIpFilterEntryMultipleOption_Object = MibTableColumn
tCpmIpFilterEntryMultipleOption = _TCpmIpFilterEntryMultipleOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 22),
    _TCpmIpFilterEntryMultipleOption_Type()
)
tCpmIpFilterEntryMultipleOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryMultipleOption.setStatus("current")


class _TCpmIpFilterEntryTcpSyn_Type(TItemMatch):
    """Custom type tCpmIpFilterEntryTcpSyn based on TItemMatch"""
    defaultValue = 1


_TCpmIpFilterEntryTcpSyn_Type.__name__ = "TItemMatch"
_TCpmIpFilterEntryTcpSyn_Object = MibTableColumn
tCpmIpFilterEntryTcpSyn = _TCpmIpFilterEntryTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 23),
    _TCpmIpFilterEntryTcpSyn_Type()
)
tCpmIpFilterEntryTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryTcpSyn.setStatus("current")


class _TCpmIpFilterEntryTcpAck_Type(TItemMatch):
    """Custom type tCpmIpFilterEntryTcpAck based on TItemMatch"""
    defaultValue = 1


_TCpmIpFilterEntryTcpAck_Type.__name__ = "TItemMatch"
_TCpmIpFilterEntryTcpAck_Object = MibTableColumn
tCpmIpFilterEntryTcpAck = _TCpmIpFilterEntryTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 24),
    _TCpmIpFilterEntryTcpAck_Type()
)
tCpmIpFilterEntryTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryTcpAck.setStatus("current")


class _TCpmIpFilterEntryIcmpCode_Type(Integer32):
    """Custom type tCpmIpFilterEntryIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TCpmIpFilterEntryIcmpCode_Type.__name__ = "Integer32"
_TCpmIpFilterEntryIcmpCode_Object = MibTableColumn
tCpmIpFilterEntryIcmpCode = _TCpmIpFilterEntryIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 25),
    _TCpmIpFilterEntryIcmpCode_Type()
)
tCpmIpFilterEntryIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryIcmpCode.setStatus("current")


class _TCpmIpFilterEntryIcmpType_Type(Integer32):
    """Custom type tCpmIpFilterEntryIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TCpmIpFilterEntryIcmpType_Type.__name__ = "Integer32"
_TCpmIpFilterEntryIcmpType_Object = MibTableColumn
tCpmIpFilterEntryIcmpType = _TCpmIpFilterEntryIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 26),
    _TCpmIpFilterEntryIcmpType_Type()
)
tCpmIpFilterEntryIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryIcmpType.setStatus("current")


class _TCpmIpFilterEntryVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tCpmIpFilterEntryVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TCpmIpFilterEntryVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TCpmIpFilterEntryVRtrId_Object = MibTableColumn
tCpmIpFilterEntryVRtrId = _TCpmIpFilterEntryVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 27),
    _TCpmIpFilterEntryVRtrId_Type()
)
tCpmIpFilterEntryVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryVRtrId.setStatus("current")
_TCpmIpFilterEntryLogCreated_Type = TruthValue
_TCpmIpFilterEntryLogCreated_Object = MibTableColumn
tCpmIpFilterEntryLogCreated = _TCpmIpFilterEntryLogCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 28),
    _TCpmIpFilterEntryLogCreated_Type()
)
tCpmIpFilterEntryLogCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryLogCreated.setStatus("current")


class _TCpmIpFilterEntrySrcIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIpFilterEntrySrcIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIpFilterEntrySrcIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIpFilterEntrySrcIpPrefixList_Object = MibTableColumn
tCpmIpFilterEntrySrcIpPrefixList = _TCpmIpFilterEntrySrcIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 30),
    _TCpmIpFilterEntrySrcIpPrefixList_Type()
)
tCpmIpFilterEntrySrcIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcIpPrefixList.setStatus("current")


class _TCpmIpFilterEntryDstIpPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIpFilterEntryDstIpPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIpFilterEntryDstIpPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIpFilterEntryDstIpPrefixList_Object = MibTableColumn
tCpmIpFilterEntryDstIpPrefixList = _TCpmIpFilterEntryDstIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 31),
    _TCpmIpFilterEntryDstIpPrefixList_Type()
)
tCpmIpFilterEntryDstIpPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDstIpPrefixList.setStatus("current")


class _TCpmIpFilterEntrySrcPortHigh_Type(TTcpUdpPort):
    """Custom type tCpmIpFilterEntrySrcPortHigh based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIpFilterEntrySrcPortHigh_Type.__name__ = "TTcpUdpPort"
_TCpmIpFilterEntrySrcPortHigh_Object = MibTableColumn
tCpmIpFilterEntrySrcPortHigh = _TCpmIpFilterEntrySrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 32),
    _TCpmIpFilterEntrySrcPortHigh_Type()
)
tCpmIpFilterEntrySrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcPortHigh.setStatus("current")


class _TCpmIpFilterEntrySrcPortOper_Type(TCpmFilterPortOperator):
    """Custom type tCpmIpFilterEntrySrcPortOper based on TCpmFilterPortOperator"""
    defaultValue = 0


_TCpmIpFilterEntrySrcPortOper_Type.__name__ = "TCpmFilterPortOperator"
_TCpmIpFilterEntrySrcPortOper_Object = MibTableColumn
tCpmIpFilterEntrySrcPortOper = _TCpmIpFilterEntrySrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 33),
    _TCpmIpFilterEntrySrcPortOper_Type()
)
tCpmIpFilterEntrySrcPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcPortOper.setStatus("current")


class _TCpmIpFilterEntryDestPortHigh_Type(TTcpUdpPort):
    """Custom type tCpmIpFilterEntryDestPortHigh based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIpFilterEntryDestPortHigh_Type.__name__ = "TTcpUdpPort"
_TCpmIpFilterEntryDestPortHigh_Object = MibTableColumn
tCpmIpFilterEntryDestPortHigh = _TCpmIpFilterEntryDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 34),
    _TCpmIpFilterEntryDestPortHigh_Type()
)
tCpmIpFilterEntryDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDestPortHigh.setStatus("current")


class _TCpmIpFilterEntryDestPortOper_Type(TCpmFilterPortOperator):
    """Custom type tCpmIpFilterEntryDestPortOper based on TCpmFilterPortOperator"""
    defaultValue = 0


_TCpmIpFilterEntryDestPortOper_Type.__name__ = "TCpmFilterPortOperator"
_TCpmIpFilterEntryDestPortOper_Object = MibTableColumn
tCpmIpFilterEntryDestPortOper = _TCpmIpFilterEntryDestPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 35),
    _TCpmIpFilterEntryDestPortOper_Type()
)
tCpmIpFilterEntryDestPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDestPortOper.setStatus("current")


class _TCpmIpFilterEntrySrcPortList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIpFilterEntrySrcPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIpFilterEntrySrcPortList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIpFilterEntrySrcPortList_Object = MibTableColumn
tCpmIpFilterEntrySrcPortList = _TCpmIpFilterEntrySrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 36),
    _TCpmIpFilterEntrySrcPortList_Type()
)
tCpmIpFilterEntrySrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntrySrcPortList.setStatus("current")


class _TCpmIpFilterEntryDstPortList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIpFilterEntryDstPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIpFilterEntryDstPortList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIpFilterEntryDstPortList_Object = MibTableColumn
tCpmIpFilterEntryDstPortList = _TCpmIpFilterEntryDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 37),
    _TCpmIpFilterEntryDstPortList_Type()
)
tCpmIpFilterEntryDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryDstPortList.setStatus("current")


class _TCpmIpFilterEntryPortSelector_Type(TFltrPortSelector):
    """Custom type tCpmIpFilterEntryPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TCpmIpFilterEntryPortSelector_Type.__name__ = "TFltrPortSelector"
_TCpmIpFilterEntryPortSelector_Object = MibTableColumn
tCpmIpFilterEntryPortSelector = _TCpmIpFilterEntryPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 6, 1, 38),
    _TCpmIpFilterEntryPortSelector_Type()
)
tCpmIpFilterEntryPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIpFilterEntryPortSelector.setStatus("current")
_TCpmIpFilterStatsTable_Object = MibTable
tCpmIpFilterStatsTable = _TCpmIpFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 7)
)
if mibBuilder.loadTexts:
    tCpmIpFilterStatsTable.setStatus("current")
_TCpmIpFilterStatsEntry_Object = MibTableRow
tCpmIpFilterStatsEntry = _TCpmIpFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 7, 1)
)
tCpmIpFilterStatsEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryId"),
)
if mibBuilder.loadTexts:
    tCpmIpFilterStatsEntry.setStatus("current")
_TCpmIpFilterStatsDroppedPkts_Type = Counter64
_TCpmIpFilterStatsDroppedPkts_Object = MibTableColumn
tCpmIpFilterStatsDroppedPkts = _TCpmIpFilterStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 7, 1, 1),
    _TCpmIpFilterStatsDroppedPkts_Type()
)
tCpmIpFilterStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIpFilterStatsDroppedPkts.setStatus("current")
_TCpmIpFilterStatsForwardedPkts_Type = Counter64
_TCpmIpFilterStatsForwardedPkts_Object = MibTableColumn
tCpmIpFilterStatsForwardedPkts = _TCpmIpFilterStatsForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 7, 1, 2),
    _TCpmIpFilterStatsForwardedPkts_Type()
)
tCpmIpFilterStatsForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIpFilterStatsForwardedPkts.setStatus("current")
_TCpmFilterQueueStatsTable_Object = MibTable
tCpmFilterQueueStatsTable = _TCpmFilterQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8)
)
if mibBuilder.loadTexts:
    tCpmFilterQueueStatsTable.setStatus("current")
_TCpmFilterQueueStatsEntry_Object = MibTableRow
tCpmFilterQueueStatsEntry = _TCpmFilterQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1)
)
tCpmFilterQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmFilterQueueId"),
)
if mibBuilder.loadTexts:
    tCpmFilterQueueStatsEntry.setStatus("current")
_TCpmFilterQInProfileDropPkts_Type = Counter64
_TCpmFilterQInProfileDropPkts_Object = MibTableColumn
tCpmFilterQInProfileDropPkts = _TCpmFilterQInProfileDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 1),
    _TCpmFilterQInProfileDropPkts_Type()
)
tCpmFilterQInProfileDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQInProfileDropPkts.setStatus("current")
_TCpmFilterQInProfileFwdPkts_Type = Counter64
_TCpmFilterQInProfileFwdPkts_Object = MibTableColumn
tCpmFilterQInProfileFwdPkts = _TCpmFilterQInProfileFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 2),
    _TCpmFilterQInProfileFwdPkts_Type()
)
tCpmFilterQInProfileFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQInProfileFwdPkts.setStatus("current")
_TCpmFilterQInProfileDropOctets_Type = Counter64
_TCpmFilterQInProfileDropOctets_Object = MibTableColumn
tCpmFilterQInProfileDropOctets = _TCpmFilterQInProfileDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 3),
    _TCpmFilterQInProfileDropOctets_Type()
)
tCpmFilterQInProfileDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQInProfileDropOctets.setStatus("current")
_TCpmFilterQInProfileFwdOctets_Type = Counter64
_TCpmFilterQInProfileFwdOctets_Object = MibTableColumn
tCpmFilterQInProfileFwdOctets = _TCpmFilterQInProfileFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 4),
    _TCpmFilterQInProfileFwdOctets_Type()
)
tCpmFilterQInProfileFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQInProfileFwdOctets.setStatus("current")
_TCpmFilterQOutProfileDropPkts_Type = Counter64
_TCpmFilterQOutProfileDropPkts_Object = MibTableColumn
tCpmFilterQOutProfileDropPkts = _TCpmFilterQOutProfileDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 5),
    _TCpmFilterQOutProfileDropPkts_Type()
)
tCpmFilterQOutProfileDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQOutProfileDropPkts.setStatus("current")
_TCpmFilterQOutProfileFwdPkts_Type = Counter64
_TCpmFilterQOutProfileFwdPkts_Object = MibTableColumn
tCpmFilterQOutProfileFwdPkts = _TCpmFilterQOutProfileFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 6),
    _TCpmFilterQOutProfileFwdPkts_Type()
)
tCpmFilterQOutProfileFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQOutProfileFwdPkts.setStatus("current")
_TCpmFilterQOutProfileDropOctets_Type = Counter64
_TCpmFilterQOutProfileDropOctets_Object = MibTableColumn
tCpmFilterQOutProfileDropOctets = _TCpmFilterQOutProfileDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 7),
    _TCpmFilterQOutProfileDropOctets_Type()
)
tCpmFilterQOutProfileDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQOutProfileDropOctets.setStatus("current")
_TCpmFilterQOutProfileFwdOctets_Type = Counter64
_TCpmFilterQOutProfileFwdOctets_Object = MibTableColumn
tCpmFilterQOutProfileFwdOctets = _TCpmFilterQOutProfileFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 8, 1, 8),
    _TCpmFilterQOutProfileFwdOctets_Type()
)
tCpmFilterQOutProfileFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmFilterQOutProfileFwdOctets.setStatus("current")
_TCpmIPv6FilterTable_Object = MibTable
tCpmIPv6FilterTable = _TCpmIPv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9)
)
if mibBuilder.loadTexts:
    tCpmIPv6FilterTable.setStatus("current")
_TCpmIPv6FilterEntry_Object = MibTableRow
tCpmIPv6FilterEntry = _TCpmIPv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1)
)
tCpmIPv6FilterEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryId"),
)
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntry.setStatus("current")


class _TCpmIPv6FilterEntryId_Type(TEntryId):
    """Custom type tCpmIPv6FilterEntryId based on TEntryId"""
    subtypeSpec = TEntryId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TCpmIPv6FilterEntryId_Type.__name__ = "TEntryId"
_TCpmIPv6FilterEntryId_Object = MibTableColumn
tCpmIPv6FilterEntryId = _TCpmIPv6FilterEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 1),
    _TCpmIPv6FilterEntryId_Type()
)
tCpmIPv6FilterEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryId.setStatus("current")
_TCpmIPv6FilterEntryRowStatus_Type = RowStatus
_TCpmIPv6FilterEntryRowStatus_Object = MibTableColumn
tCpmIPv6FilterEntryRowStatus = _TCpmIPv6FilterEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 2),
    _TCpmIPv6FilterEntryRowStatus_Type()
)
tCpmIPv6FilterEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryRowStatus.setStatus("current")
_TCpmIPv6FilterEntryLastChanged_Type = TimeStamp
_TCpmIPv6FilterEntryLastChanged_Object = MibTableColumn
tCpmIPv6FilterEntryLastChanged = _TCpmIPv6FilterEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 3),
    _TCpmIPv6FilterEntryLastChanged_Type()
)
tCpmIPv6FilterEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryLastChanged.setStatus("current")


class _TCpmIPv6FilterEntryLogId_Type(TFilterLogId):
    """Custom type tCpmIPv6FilterEntryLogId based on TFilterLogId"""
    defaultValue = 0


_TCpmIPv6FilterEntryLogId_Type.__name__ = "TFilterLogId"
_TCpmIPv6FilterEntryLogId_Object = MibTableColumn
tCpmIPv6FilterEntryLogId = _TCpmIPv6FilterEntryLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 4),
    _TCpmIPv6FilterEntryLogId_Type()
)
tCpmIPv6FilterEntryLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryLogId.setStatus("current")


class _TCpmIPv6FilterEntryDescription_Type(TItemDescription):
    """Custom type tCpmIPv6FilterEntryDescription based on TItemDescription"""
    defaultHexValue = ""


_TCpmIPv6FilterEntryDescription_Type.__name__ = "TItemDescription"
_TCpmIPv6FilterEntryDescription_Object = MibTableColumn
tCpmIPv6FilterEntryDescription = _TCpmIPv6FilterEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 5),
    _TCpmIPv6FilterEntryDescription_Type()
)
tCpmIPv6FilterEntryDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDescription.setStatus("current")


class _TCpmIPv6FilterEntryAction_Type(TCpmFilterActionOrDefault):
    """Custom type tCpmIPv6FilterEntryAction based on TCpmFilterActionOrDefault"""
    defaultValue = 1


_TCpmIPv6FilterEntryAction_Type.__name__ = "TCpmFilterActionOrDefault"
_TCpmIPv6FilterEntryAction_Object = MibTableColumn
tCpmIPv6FilterEntryAction = _TCpmIPv6FilterEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 6),
    _TCpmIPv6FilterEntryAction_Type()
)
tCpmIPv6FilterEntryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryAction.setStatus("current")


class _TCpmIPv6FilterEntryQueueId_Type(TCpmFilterQueueId):
    """Custom type tCpmIPv6FilterEntryQueueId based on TCpmFilterQueueId"""
    defaultValue = 0


_TCpmIPv6FilterEntryQueueId_Type.__name__ = "TCpmFilterQueueId"
_TCpmIPv6FilterEntryQueueId_Object = MibTableColumn
tCpmIPv6FilterEntryQueueId = _TCpmIPv6FilterEntryQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 7),
    _TCpmIPv6FilterEntryQueueId_Type()
)
tCpmIPv6FilterEntryQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryQueueId.setStatus("current")


class _TCpmIPv6FilterEntrySrcIPAddr_Type(InetAddressIPv6):
    """Custom type tCpmIPv6FilterEntrySrcIPAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TCpmIPv6FilterEntrySrcIPAddr_Type.__name__ = "InetAddressIPv6"
_TCpmIPv6FilterEntrySrcIPAddr_Object = MibTableColumn
tCpmIPv6FilterEntrySrcIPAddr = _TCpmIPv6FilterEntrySrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 8),
    _TCpmIPv6FilterEntrySrcIPAddr_Type()
)
tCpmIPv6FilterEntrySrcIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcIPAddr.setStatus("current")


class _TCpmIPv6FilterEntrySrcIPMask_Type(InetAddressPrefixLength):
    """Custom type tCpmIPv6FilterEntrySrcIPMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TCpmIPv6FilterEntrySrcIPMask_Type.__name__ = "InetAddressPrefixLength"
_TCpmIPv6FilterEntrySrcIPMask_Object = MibTableColumn
tCpmIPv6FilterEntrySrcIPMask = _TCpmIPv6FilterEntrySrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 9),
    _TCpmIPv6FilterEntrySrcIPMask_Type()
)
tCpmIPv6FilterEntrySrcIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcIPMask.setStatus("current")


class _TCpmIPv6FilterEntryDestIPAddr_Type(InetAddressIPv6):
    """Custom type tCpmIPv6FilterEntryDestIPAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TCpmIPv6FilterEntryDestIPAddr_Type.__name__ = "InetAddressIPv6"
_TCpmIPv6FilterEntryDestIPAddr_Object = MibTableColumn
tCpmIPv6FilterEntryDestIPAddr = _TCpmIPv6FilterEntryDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 10),
    _TCpmIPv6FilterEntryDestIPAddr_Type()
)
tCpmIPv6FilterEntryDestIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDestIPAddr.setStatus("current")


class _TCpmIPv6FilterEntryDestIPMask_Type(InetAddressPrefixLength):
    """Custom type tCpmIPv6FilterEntryDestIPMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TCpmIPv6FilterEntryDestIPMask_Type.__name__ = "InetAddressPrefixLength"
_TCpmIPv6FilterEntryDestIPMask_Object = MibTableColumn
tCpmIPv6FilterEntryDestIPMask = _TCpmIPv6FilterEntryDestIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 11),
    _TCpmIPv6FilterEntryDestIPMask_Type()
)
tCpmIPv6FilterEntryDestIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDestIPMask.setStatus("current")


class _TCpmIPv6FilterEntryNextHeader_Type(TIpProtocol):
    """Custom type tCpmIPv6FilterEntryNextHeader based on TIpProtocol"""
    defaultValue = -1


_TCpmIPv6FilterEntryNextHeader_Type.__name__ = "TIpProtocol"
_TCpmIPv6FilterEntryNextHeader_Object = MibTableColumn
tCpmIPv6FilterEntryNextHeader = _TCpmIPv6FilterEntryNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 12),
    _TCpmIPv6FilterEntryNextHeader_Type()
)
tCpmIPv6FilterEntryNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryNextHeader.setStatus("current")


class _TCpmIPv6FilterEntrySrcPort_Type(TTcpUdpPort):
    """Custom type tCpmIPv6FilterEntrySrcPort based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIPv6FilterEntrySrcPort_Type.__name__ = "TTcpUdpPort"
_TCpmIPv6FilterEntrySrcPort_Object = MibTableColumn
tCpmIPv6FilterEntrySrcPort = _TCpmIPv6FilterEntrySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 13),
    _TCpmIPv6FilterEntrySrcPort_Type()
)
tCpmIPv6FilterEntrySrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcPort.setStatus("current")


class _TCpmIPv6FilterEntrySrcPortMask_Type(Integer32):
    """Custom type tCpmIPv6FilterEntrySrcPortMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TCpmIPv6FilterEntrySrcPortMask_Type.__name__ = "Integer32"
_TCpmIPv6FilterEntrySrcPortMask_Object = MibTableColumn
tCpmIPv6FilterEntrySrcPortMask = _TCpmIPv6FilterEntrySrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 14),
    _TCpmIPv6FilterEntrySrcPortMask_Type()
)
tCpmIPv6FilterEntrySrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcPortMask.setStatus("current")


class _TCpmIPv6FilterEntryDestPort_Type(TTcpUdpPort):
    """Custom type tCpmIPv6FilterEntryDestPort based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIPv6FilterEntryDestPort_Type.__name__ = "TTcpUdpPort"
_TCpmIPv6FilterEntryDestPort_Object = MibTableColumn
tCpmIPv6FilterEntryDestPort = _TCpmIPv6FilterEntryDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 15),
    _TCpmIPv6FilterEntryDestPort_Type()
)
tCpmIPv6FilterEntryDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDestPort.setStatus("current")


class _TCpmIPv6FilterEntryDestPortMask_Type(Integer32):
    """Custom type tCpmIPv6FilterEntryDestPortMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TCpmIPv6FilterEntryDestPortMask_Type.__name__ = "Integer32"
_TCpmIPv6FilterEntryDestPortMask_Object = MibTableColumn
tCpmIPv6FilterEntryDestPortMask = _TCpmIPv6FilterEntryDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 16),
    _TCpmIPv6FilterEntryDestPortMask_Type()
)
tCpmIPv6FilterEntryDestPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDestPortMask.setStatus("current")


class _TCpmIPv6FilterEntryDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tCpmIPv6FilterEntryDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TCpmIPv6FilterEntryDSCP_Type.__name__ = "TDSCPNameOrEmpty"
_TCpmIPv6FilterEntryDSCP_Object = MibTableColumn
tCpmIPv6FilterEntryDSCP = _TCpmIPv6FilterEntryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 17),
    _TCpmIPv6FilterEntryDSCP_Type()
)
tCpmIPv6FilterEntryDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDSCP.setStatus("current")


class _TCpmIPv6FilterEntryTcpSyn_Type(TItemMatch):
    """Custom type tCpmIPv6FilterEntryTcpSyn based on TItemMatch"""
    defaultValue = 1


_TCpmIPv6FilterEntryTcpSyn_Type.__name__ = "TItemMatch"
_TCpmIPv6FilterEntryTcpSyn_Object = MibTableColumn
tCpmIPv6FilterEntryTcpSyn = _TCpmIPv6FilterEntryTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 23),
    _TCpmIPv6FilterEntryTcpSyn_Type()
)
tCpmIPv6FilterEntryTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryTcpSyn.setStatus("current")


class _TCpmIPv6FilterEntryTcpAck_Type(TItemMatch):
    """Custom type tCpmIPv6FilterEntryTcpAck based on TItemMatch"""
    defaultValue = 1


_TCpmIPv6FilterEntryTcpAck_Type.__name__ = "TItemMatch"
_TCpmIPv6FilterEntryTcpAck_Object = MibTableColumn
tCpmIPv6FilterEntryTcpAck = _TCpmIPv6FilterEntryTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 24),
    _TCpmIPv6FilterEntryTcpAck_Type()
)
tCpmIPv6FilterEntryTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryTcpAck.setStatus("current")


class _TCpmIPv6FilterEntryIcmpCode_Type(Integer32):
    """Custom type tCpmIPv6FilterEntryIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TCpmIPv6FilterEntryIcmpCode_Type.__name__ = "Integer32"
_TCpmIPv6FilterEntryIcmpCode_Object = MibTableColumn
tCpmIPv6FilterEntryIcmpCode = _TCpmIPv6FilterEntryIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 25),
    _TCpmIPv6FilterEntryIcmpCode_Type()
)
tCpmIPv6FilterEntryIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryIcmpCode.setStatus("current")


class _TCpmIPv6FilterEntryIcmpType_Type(Integer32):
    """Custom type tCpmIPv6FilterEntryIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_TCpmIPv6FilterEntryIcmpType_Type.__name__ = "Integer32"
_TCpmIPv6FilterEntryIcmpType_Object = MibTableColumn
tCpmIPv6FilterEntryIcmpType = _TCpmIPv6FilterEntryIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 26),
    _TCpmIPv6FilterEntryIcmpType_Type()
)
tCpmIPv6FilterEntryIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryIcmpType.setStatus("current")


class _TCpmIPv6FilterEntryVRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tCpmIPv6FilterEntryVRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TCpmIPv6FilterEntryVRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TCpmIPv6FilterEntryVRtrId_Object = MibTableColumn
tCpmIPv6FilterEntryVRtrId = _TCpmIPv6FilterEntryVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 27),
    _TCpmIPv6FilterEntryVRtrId_Type()
)
tCpmIPv6FilterEntryVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryVRtrId.setStatus("current")
_TCpmIPv6FilterEntryLogCreated_Type = TruthValue
_TCpmIPv6FilterEntryLogCreated_Object = MibTableColumn
tCpmIPv6FilterEntryLogCreated = _TCpmIPv6FilterEntryLogCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 28),
    _TCpmIPv6FilterEntryLogCreated_Type()
)
tCpmIPv6FilterEntryLogCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryLogCreated.setStatus("current")


class _TCpmIPv6FilterEntryFlowLabel_Type(IPv6FlowLabel):
    """Custom type tCpmIPv6FilterEntryFlowLabel based on IPv6FlowLabel"""
    defaultValue = -1


_TCpmIPv6FilterEntryFlowLabel_Type.__name__ = "IPv6FlowLabel"
_TCpmIPv6FilterEntryFlowLabel_Object = MibTableColumn
tCpmIPv6FilterEntryFlowLabel = _TCpmIPv6FilterEntryFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 29),
    _TCpmIPv6FilterEntryFlowLabel_Type()
)
tCpmIPv6FilterEntryFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryFlowLabel.setStatus("current")


class _TCpmIPv6FilterEntrySrcIpPfxList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIPv6FilterEntrySrcIpPfxList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIPv6FilterEntrySrcIpPfxList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIPv6FilterEntrySrcIpPfxList_Object = MibTableColumn
tCpmIPv6FilterEntrySrcIpPfxList = _TCpmIPv6FilterEntrySrcIpPfxList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 30),
    _TCpmIPv6FilterEntrySrcIpPfxList_Type()
)
tCpmIPv6FilterEntrySrcIpPfxList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcIpPfxList.setStatus("current")


class _TCpmIPv6FilterEntryDstIpPfxList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIPv6FilterEntryDstIpPfxList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIPv6FilterEntryDstIpPfxList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIPv6FilterEntryDstIpPfxList_Object = MibTableColumn
tCpmIPv6FilterEntryDstIpPfxList = _TCpmIPv6FilterEntryDstIpPfxList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 31),
    _TCpmIPv6FilterEntryDstIpPfxList_Type()
)
tCpmIPv6FilterEntryDstIpPfxList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDstIpPfxList.setStatus("current")


class _TCpmIPv6FilterEntrySrcPortHigh_Type(TTcpUdpPort):
    """Custom type tCpmIPv6FilterEntrySrcPortHigh based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIPv6FilterEntrySrcPortHigh_Type.__name__ = "TTcpUdpPort"
_TCpmIPv6FilterEntrySrcPortHigh_Object = MibTableColumn
tCpmIPv6FilterEntrySrcPortHigh = _TCpmIPv6FilterEntrySrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 32),
    _TCpmIPv6FilterEntrySrcPortHigh_Type()
)
tCpmIPv6FilterEntrySrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcPortHigh.setStatus("current")


class _TCpmIPv6FilterEntrySrcPortOper_Type(TCpmFilterPortOperator):
    """Custom type tCpmIPv6FilterEntrySrcPortOper based on TCpmFilterPortOperator"""
    defaultValue = 0


_TCpmIPv6FilterEntrySrcPortOper_Type.__name__ = "TCpmFilterPortOperator"
_TCpmIPv6FilterEntrySrcPortOper_Object = MibTableColumn
tCpmIPv6FilterEntrySrcPortOper = _TCpmIPv6FilterEntrySrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 33),
    _TCpmIPv6FilterEntrySrcPortOper_Type()
)
tCpmIPv6FilterEntrySrcPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcPortOper.setStatus("current")


class _TCpmIPv6FilterEntryDestPortHigh_Type(TTcpUdpPort):
    """Custom type tCpmIPv6FilterEntryDestPortHigh based on TTcpUdpPort"""
    defaultValue = 0


_TCpmIPv6FilterEntryDestPortHigh_Type.__name__ = "TTcpUdpPort"
_TCpmIPv6FilterEntryDestPortHigh_Object = MibTableColumn
tCpmIPv6FilterEntryDestPortHigh = _TCpmIPv6FilterEntryDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 34),
    _TCpmIPv6FilterEntryDestPortHigh_Type()
)
tCpmIPv6FilterEntryDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDestPortHigh.setStatus("current")


class _TCpmIPv6FilterEntryDestPortOper_Type(TCpmFilterPortOperator):
    """Custom type tCpmIPv6FilterEntryDestPortOper based on TCpmFilterPortOperator"""
    defaultValue = 0


_TCpmIPv6FilterEntryDestPortOper_Type.__name__ = "TCpmFilterPortOperator"
_TCpmIPv6FilterEntryDestPortOper_Object = MibTableColumn
tCpmIPv6FilterEntryDestPortOper = _TCpmIPv6FilterEntryDestPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 35),
    _TCpmIPv6FilterEntryDestPortOper_Type()
)
tCpmIPv6FilterEntryDestPortOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDestPortOper.setStatus("current")


class _TCpmIPv6FilterEntrySrcPortList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIPv6FilterEntrySrcPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIPv6FilterEntrySrcPortList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIPv6FilterEntrySrcPortList_Object = MibTableColumn
tCpmIPv6FilterEntrySrcPortList = _TCpmIPv6FilterEntrySrcPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 36),
    _TCpmIPv6FilterEntrySrcPortList_Type()
)
tCpmIPv6FilterEntrySrcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntrySrcPortList.setStatus("current")


class _TCpmIPv6FilterEntryDstPortList_Type(TNamedItemOrEmpty):
    """Custom type tCpmIPv6FilterEntryDstPortList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TCpmIPv6FilterEntryDstPortList_Type.__name__ = "TNamedItemOrEmpty"
_TCpmIPv6FilterEntryDstPortList_Object = MibTableColumn
tCpmIPv6FilterEntryDstPortList = _TCpmIPv6FilterEntryDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 37),
    _TCpmIPv6FilterEntryDstPortList_Type()
)
tCpmIPv6FilterEntryDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryDstPortList.setStatus("current")


class _TCpmIPv6FilterEntryPortSelector_Type(TFltrPortSelector):
    """Custom type tCpmIPv6FilterEntryPortSelector based on TFltrPortSelector"""
    defaultValue = 0


_TCpmIPv6FilterEntryPortSelector_Type.__name__ = "TFltrPortSelector"
_TCpmIPv6FilterEntryPortSelector_Object = MibTableColumn
tCpmIPv6FilterEntryPortSelector = _TCpmIPv6FilterEntryPortSelector_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 38),
    _TCpmIPv6FilterEntryPortSelector_Type()
)
tCpmIPv6FilterEntryPortSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryPortSelector.setStatus("current")


class _TCpmIPv6FilterEntryFragment_Type(TItemMatch):
    """Custom type tCpmIPv6FilterEntryFragment based on TItemMatch"""
    defaultValue = 1


_TCpmIPv6FilterEntryFragment_Type.__name__ = "TItemMatch"
_TCpmIPv6FilterEntryFragment_Object = MibTableColumn
tCpmIPv6FilterEntryFragment = _TCpmIPv6FilterEntryFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 39),
    _TCpmIPv6FilterEntryFragment_Type()
)
tCpmIPv6FilterEntryFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryFragment.setStatus("current")


class _TCpmIPv6FilterEntryHopByHopOpt_Type(TItemMatch):
    """Custom type tCpmIPv6FilterEntryHopByHopOpt based on TItemMatch"""
    defaultValue = 1


_TCpmIPv6FilterEntryHopByHopOpt_Type.__name__ = "TItemMatch"
_TCpmIPv6FilterEntryHopByHopOpt_Object = MibTableColumn
tCpmIPv6FilterEntryHopByHopOpt = _TCpmIPv6FilterEntryHopByHopOpt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 9, 1, 40),
    _TCpmIPv6FilterEntryHopByHopOpt_Type()
)
tCpmIPv6FilterEntryHopByHopOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmIPv6FilterEntryHopByHopOpt.setStatus("current")
_TCpmIPv6FilterStatsTable_Object = MibTable
tCpmIPv6FilterStatsTable = _TCpmIPv6FilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 10)
)
if mibBuilder.loadTexts:
    tCpmIPv6FilterStatsTable.setStatus("current")
_TCpmIPv6FilterStatsEntry_Object = MibTableRow
tCpmIPv6FilterStatsEntry = _TCpmIPv6FilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 10, 1)
)
tCpmIPv6FilterStatsEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryId"),
)
if mibBuilder.loadTexts:
    tCpmIPv6FilterStatsEntry.setStatus("current")
_TCpmIPv6FilterStatsDroppedPkts_Type = Counter64
_TCpmIPv6FilterStatsDroppedPkts_Object = MibTableColumn
tCpmIPv6FilterStatsDroppedPkts = _TCpmIPv6FilterStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 10, 1, 1),
    _TCpmIPv6FilterStatsDroppedPkts_Type()
)
tCpmIPv6FilterStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIPv6FilterStatsDroppedPkts.setStatus("current")
_TCpmIPv6FilterStatsForwardedPkts_Type = Counter64
_TCpmIPv6FilterStatsForwardedPkts_Object = MibTableColumn
tCpmIPv6FilterStatsForwardedPkts = _TCpmIPv6FilterStatsForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 10, 1, 2),
    _TCpmIPv6FilterStatsForwardedPkts_Type()
)
tCpmIPv6FilterStatsForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmIPv6FilterStatsForwardedPkts.setStatus("current")
_TmnxCpmProtPolTableLastChanged_Type = TimeStamp
_TmnxCpmProtPolTableLastChanged_Object = MibScalar
tmnxCpmProtPolTableLastChanged = _TmnxCpmProtPolTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 11),
    _TmnxCpmProtPolTableLastChanged_Type()
)
tmnxCpmProtPolTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtPolTableLastChanged.setStatus("current")
_TmnxCpmProtPolTable_Object = MibTable
tmnxCpmProtPolTable = _TmnxCpmProtPolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12)
)
if mibBuilder.loadTexts:
    tmnxCpmProtPolTable.setStatus("current")
_TmnxCpmProtPolEntry_Object = MibTableRow
tmnxCpmProtPolEntry = _TmnxCpmProtPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1)
)
tmnxCpmProtPolEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtPolEntry.setStatus("current")


class _TmnxCpmProtPolicyId_Type(TCpmProtPolicyID):
    """Custom type tmnxCpmProtPolicyId based on TCpmProtPolicyID"""
    subtypeSpec = TCpmProtPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxCpmProtPolicyId_Type.__name__ = "TCpmProtPolicyID"
_TmnxCpmProtPolicyId_Object = MibTableColumn
tmnxCpmProtPolicyId = _TmnxCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 1),
    _TmnxCpmProtPolicyId_Type()
)
tmnxCpmProtPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtPolicyId.setStatus("current")
_TmnxCpmProtPolRowStatus_Type = RowStatus
_TmnxCpmProtPolRowStatus_Object = MibTableColumn
tmnxCpmProtPolRowStatus = _TmnxCpmProtPolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 2),
    _TmnxCpmProtPolRowStatus_Type()
)
tmnxCpmProtPolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolRowStatus.setStatus("current")
_TmnxCpmProtPolLastChanged_Type = TimeStamp
_TmnxCpmProtPolLastChanged_Object = MibTableColumn
tmnxCpmProtPolLastChanged = _TmnxCpmProtPolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 3),
    _TmnxCpmProtPolLastChanged_Type()
)
tmnxCpmProtPolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtPolLastChanged.setStatus("current")


class _TmnxCpmProtPolDescription_Type(TItemDescription):
    """Custom type tmnxCpmProtPolDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxCpmProtPolDescription_Type.__name__ = "TItemDescription"
_TmnxCpmProtPolDescription_Object = MibTableColumn
tmnxCpmProtPolDescription = _TmnxCpmProtPolDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 4),
    _TmnxCpmProtPolDescription_Type()
)
tmnxCpmProtPolDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolDescription.setStatus("current")


class _TmnxCpmProtPolPerSrcRateLimit_Type(TmnxCpmPacketPolRateLimit):
    """Custom type tmnxCpmProtPolPerSrcRateLimit based on TmnxCpmPacketPolRateLimit"""
    defaultValue = -1


_TmnxCpmProtPolPerSrcRateLimit_Type.__name__ = "TmnxCpmPacketPolRateLimit"
_TmnxCpmProtPolPerSrcRateLimit_Object = MibTableColumn
tmnxCpmProtPolPerSrcRateLimit = _TmnxCpmProtPolPerSrcRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 5),
    _TmnxCpmProtPolPerSrcRateLimit_Type()
)
tmnxCpmProtPolPerSrcRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolPerSrcRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtPolPerSrcRateLimit.setUnits("packets per second")


class _TmnxCpmProtPolOverallRateLimit_Type(TmnxCpmPacketPolRateLimit):
    """Custom type tmnxCpmProtPolOverallRateLimit based on TmnxCpmPacketPolRateLimit"""
    defaultValue = -1


_TmnxCpmProtPolOverallRateLimit_Type.__name__ = "TmnxCpmPacketPolRateLimit"
_TmnxCpmProtPolOverallRateLimit_Object = MibTableColumn
tmnxCpmProtPolOverallRateLimit = _TmnxCpmProtPolOverallRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 6),
    _TmnxCpmProtPolOverallRateLimit_Type()
)
tmnxCpmProtPolOverallRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolOverallRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtPolOverallRateLimit.setUnits("packets per second")


class _TmnxCpmProtPolAlarm_Type(TruthValue):
    """Custom type tmnxCpmProtPolAlarm based on TruthValue"""
    defaultValue = 1


_TmnxCpmProtPolAlarm_Type.__name__ = "TruthValue"
_TmnxCpmProtPolAlarm_Object = MibTableColumn
tmnxCpmProtPolAlarm = _TmnxCpmProtPolAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 7),
    _TmnxCpmProtPolAlarm_Type()
)
tmnxCpmProtPolAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolAlarm.setStatus("current")


class _TmnxCpmProtPolOutProfileRate_Type(TmnxCpmPacketPolRateLimit):
    """Custom type tmnxCpmProtPolOutProfileRate based on TmnxCpmPacketPolRateLimit"""
    defaultValue = 3000


_TmnxCpmProtPolOutProfileRate_Type.__name__ = "TmnxCpmPacketPolRateLimit"
_TmnxCpmProtPolOutProfileRate_Object = MibTableColumn
tmnxCpmProtPolOutProfileRate = _TmnxCpmProtPolOutProfileRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 8),
    _TmnxCpmProtPolOutProfileRate_Type()
)
tmnxCpmProtPolOutProfileRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolOutProfileRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtPolOutProfileRate.setUnits("packets per second")


class _TmnxCpmProtPolLimDhcpCiAddrZero_Type(TruthValue):
    """Custom type tmnxCpmProtPolLimDhcpCiAddrZero based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtPolLimDhcpCiAddrZero_Type.__name__ = "TruthValue"
_TmnxCpmProtPolLimDhcpCiAddrZero_Object = MibTableColumn
tmnxCpmProtPolLimDhcpCiAddrZero = _TmnxCpmProtPolLimDhcpCiAddrZero_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 9),
    _TmnxCpmProtPolLimDhcpCiAddrZero_Type()
)
tmnxCpmProtPolLimDhcpCiAddrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolLimDhcpCiAddrZero.setStatus("current")


class _TmnxCpmProtPolOutProfRateLogEvnt_Type(TruthValue):
    """Custom type tmnxCpmProtPolOutProfRateLogEvnt based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtPolOutProfRateLogEvnt_Type.__name__ = "TruthValue"
_TmnxCpmProtPolOutProfRateLogEvnt_Object = MibTableColumn
tmnxCpmProtPolOutProfRateLogEvnt = _TmnxCpmProtPolOutProfRateLogEvnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 12, 1, 10),
    _TmnxCpmProtPolOutProfRateLogEvnt_Type()
)
tmnxCpmProtPolOutProfRateLogEvnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtPolOutProfRateLogEvnt.setStatus("current")


class _TmnxCpmProtDropUncfgdProtocolMsg_Type(TmnxAdminState):
    """Custom type tmnxCpmProtDropUncfgdProtocolMsg based on TmnxAdminState"""
    defaultValue = 3


_TmnxCpmProtDropUncfgdProtocolMsg_Type.__name__ = "TmnxAdminState"
_TmnxCpmProtDropUncfgdProtocolMsg_Object = MibScalar
tmnxCpmProtDropUncfgdProtocolMsg = _TmnxCpmProtDropUncfgdProtocolMsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 13),
    _TmnxCpmProtDropUncfgdProtocolMsg_Type()
)
tmnxCpmProtDropUncfgdProtocolMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmProtDropUncfgdProtocolMsg.setStatus("current")


class _TmnxCpmProtLinkRateLimit_Type(TmnxCpmPacketRateLimit):
    """Custom type tmnxCpmProtLinkRateLimit based on TmnxCpmPacketRateLimit"""
    defaultValue = 15000


_TmnxCpmProtLinkRateLimit_Type.__name__ = "TmnxCpmPacketRateLimit"
_TmnxCpmProtLinkRateLimit_Object = MibScalar
tmnxCpmProtLinkRateLimit = _TmnxCpmProtLinkRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 14),
    _TmnxCpmProtLinkRateLimit_Type()
)
tmnxCpmProtLinkRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmProtLinkRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtLinkRateLimit.setUnits("packets per second")
_TmnxCpmProtExcdTableLastChanged_Type = TimeStamp
_TmnxCpmProtExcdTableLastChanged_Object = MibScalar
tmnxCpmProtExcdTableLastChanged = _TmnxCpmProtExcdTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 15),
    _TmnxCpmProtExcdTableLastChanged_Type()
)
tmnxCpmProtExcdTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdTableLastChanged.setStatus("current")
_TmnxCpmProtExcdTable_Object = MibTable
tmnxCpmProtExcdTable = _TmnxCpmProtExcdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 16)
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdTable.setStatus("current")
_TmnxCpmProtExcdEntry_Object = MibTableRow
tmnxCpmProtExcdEntry = _TmnxCpmProtExcdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 16, 1)
)
tmnxCpmProtExcdEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdMac"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdEntry.setStatus("current")
_TmnxCpmProtExcdMac_Type = MacAddress
_TmnxCpmProtExcdMac_Object = MibTableColumn
tmnxCpmProtExcdMac = _TmnxCpmProtExcdMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 16, 1, 1),
    _TmnxCpmProtExcdMac_Type()
)
tmnxCpmProtExcdMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdMac.setStatus("current")
_TmnxCpmProtExcdPeriods_Type = Gauge32
_TmnxCpmProtExcdPeriods_Object = MibTableColumn
tmnxCpmProtExcdPeriods = _TmnxCpmProtExcdPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 16, 1, 2),
    _TmnxCpmProtExcdPeriods_Type()
)
tmnxCpmProtExcdPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdPeriods.setStatus("current")
_TmnxCpmProtExcdTimeStarted_Type = TimeStamp
_TmnxCpmProtExcdTimeStarted_Object = MibTableColumn
tmnxCpmProtExcdTimeStarted = _TmnxCpmProtExcdTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 16, 1, 3),
    _TmnxCpmProtExcdTimeStarted_Type()
)
tmnxCpmProtExcdTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdTimeStarted.setStatus("current")
_TmnxCpmProtExcdTime_Type = TimeStamp
_TmnxCpmProtExcdTime_Object = MibTableColumn
tmnxCpmProtExcdTime = _TmnxCpmProtExcdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 16, 1, 4),
    _TmnxCpmProtExcdTime_Type()
)
tmnxCpmProtExcdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdTime.setStatus("current")
_TmnxCpmProtViolPortTableLastChgd_Type = TimeStamp
_TmnxCpmProtViolPortTableLastChgd_Object = MibScalar
tmnxCpmProtViolPortTableLastChgd = _TmnxCpmProtViolPortTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 17),
    _TmnxCpmProtViolPortTableLastChgd_Type()
)
tmnxCpmProtViolPortTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortTableLastChgd.setStatus("current")
_TmnxCpmProtViolPortTable_Object = MibTable
tmnxCpmProtViolPortTable = _TmnxCpmProtViolPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18)
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortTable.setStatus("current")
_TmnxCpmProtViolPortEntry_Object = MibTableRow
tmnxCpmProtViolPortEntry = _TmnxCpmProtViolPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1)
)
tmnxCpmProtViolPortEntry.setIndexNames(
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortEntry.setStatus("current")
_TmnxCpmProtViolPortPeriods_Type = Gauge32
_TmnxCpmProtViolPortPeriods_Object = MibTableColumn
tmnxCpmProtViolPortPeriods = _TmnxCpmProtViolPortPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1, 1),
    _TmnxCpmProtViolPortPeriods_Type()
)
tmnxCpmProtViolPortPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortPeriods.setStatus("current")
_TmnxCpmProtViolPortTimeStarted_Type = TimeStamp
_TmnxCpmProtViolPortTimeStarted_Object = MibTableColumn
tmnxCpmProtViolPortTimeStarted = _TmnxCpmProtViolPortTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1, 2),
    _TmnxCpmProtViolPortTimeStarted_Type()
)
tmnxCpmProtViolPortTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortTimeStarted.setStatus("current")
_TmnxCpmProtViolPortTime_Type = TimeStamp
_TmnxCpmProtViolPortTime_Object = MibTableColumn
tmnxCpmProtViolPortTime = _TmnxCpmProtViolPortTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1, 3),
    _TmnxCpmProtViolPortTime_Type()
)
tmnxCpmProtViolPortTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortTime.setStatus("current")
_TmnxCpmProtViolPortAggPeriods_Type = Gauge32
_TmnxCpmProtViolPortAggPeriods_Object = MibTableColumn
tmnxCpmProtViolPortAggPeriods = _TmnxCpmProtViolPortAggPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1, 4),
    _TmnxCpmProtViolPortAggPeriods_Type()
)
tmnxCpmProtViolPortAggPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortAggPeriods.setStatus("current")
_TmnxCpmProtViolPortAggTimeStart_Type = TimeStamp
_TmnxCpmProtViolPortAggTimeStart_Object = MibTableColumn
tmnxCpmProtViolPortAggTimeStart = _TmnxCpmProtViolPortAggTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1, 5),
    _TmnxCpmProtViolPortAggTimeStart_Type()
)
tmnxCpmProtViolPortAggTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortAggTimeStart.setStatus("current")
_TmnxCpmProtViolPortAggTime_Type = TimeStamp
_TmnxCpmProtViolPortAggTime_Object = MibTableColumn
tmnxCpmProtViolPortAggTime = _TmnxCpmProtViolPortAggTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 18, 1, 6),
    _TmnxCpmProtViolPortAggTime_Type()
)
tmnxCpmProtViolPortAggTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortAggTime.setStatus("current")
_TmnxCpmProtViolIfTableLastChgd_Type = TimeStamp
_TmnxCpmProtViolIfTableLastChgd_Object = MibScalar
tmnxCpmProtViolIfTableLastChgd = _TmnxCpmProtViolIfTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 19),
    _TmnxCpmProtViolIfTableLastChgd_Type()
)
tmnxCpmProtViolIfTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfTableLastChgd.setStatus("current")
_TmnxCpmProtViolIfTable_Object = MibTable
tmnxCpmProtViolIfTable = _TmnxCpmProtViolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 20)
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfTable.setStatus("current")
_TmnxCpmProtViolIfEntry_Object = MibTableRow
tmnxCpmProtViolIfEntry = _TmnxCpmProtViolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 20, 1)
)
tmnxCpmProtViolIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfEntry.setStatus("current")
_TmnxCpmProtViolIfPeriods_Type = Gauge32
_TmnxCpmProtViolIfPeriods_Object = MibTableColumn
tmnxCpmProtViolIfPeriods = _TmnxCpmProtViolIfPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 20, 1, 1),
    _TmnxCpmProtViolIfPeriods_Type()
)
tmnxCpmProtViolIfPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfPeriods.setStatus("current")
_TmnxCpmProtViolIfTimeStarted_Type = TimeStamp
_TmnxCpmProtViolIfTimeStarted_Object = MibTableColumn
tmnxCpmProtViolIfTimeStarted = _TmnxCpmProtViolIfTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 20, 1, 2),
    _TmnxCpmProtViolIfTimeStarted_Type()
)
tmnxCpmProtViolIfTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfTimeStarted.setStatus("current")
_TmnxCpmProtViolIfTime_Type = TimeStamp
_TmnxCpmProtViolIfTime_Object = MibTableColumn
tmnxCpmProtViolIfTime = _TmnxCpmProtViolIfTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 20, 1, 3),
    _TmnxCpmProtViolIfTime_Type()
)
tmnxCpmProtViolIfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfTime.setStatus("current")
_TmnxCpmProtViolSapTableLastChgd_Type = TimeStamp
_TmnxCpmProtViolSapTableLastChgd_Object = MibScalar
tmnxCpmProtViolSapTableLastChgd = _TmnxCpmProtViolSapTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 21),
    _TmnxCpmProtViolSapTableLastChgd_Type()
)
tmnxCpmProtViolSapTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapTableLastChgd.setStatus("current")
_TmnxCpmProtViolSapTable_Object = MibTable
tmnxCpmProtViolSapTable = _TmnxCpmProtViolSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 22)
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapTable.setStatus("current")
_TmnxCpmProtViolSapEntry_Object = MibTableRow
tmnxCpmProtViolSapEntry = _TmnxCpmProtViolSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 22, 1)
)
tmnxCpmProtViolSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapEntry.setStatus("current")
_TmnxCpmProtViolSapPeriods_Type = Gauge32
_TmnxCpmProtViolSapPeriods_Object = MibTableColumn
tmnxCpmProtViolSapPeriods = _TmnxCpmProtViolSapPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 22, 1, 1),
    _TmnxCpmProtViolSapPeriods_Type()
)
tmnxCpmProtViolSapPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapPeriods.setStatus("current")
_TmnxCpmProtViolSapTimeStarted_Type = TimeStamp
_TmnxCpmProtViolSapTimeStarted_Object = MibTableColumn
tmnxCpmProtViolSapTimeStarted = _TmnxCpmProtViolSapTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 22, 1, 2),
    _TmnxCpmProtViolSapTimeStarted_Type()
)
tmnxCpmProtViolSapTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapTimeStarted.setStatus("current")
_TmnxCpmProtViolSapTime_Type = TimeStamp
_TmnxCpmProtViolSapTime_Object = MibTableColumn
tmnxCpmProtViolSapTime = _TmnxCpmProtViolSapTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 22, 1, 3),
    _TmnxCpmProtViolSapTime_Type()
)
tmnxCpmProtViolSapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapTime.setStatus("current")


class _TmnxCpmProtPortOverallRateLimit_Type(TmnxCpmPacketRateLimit):
    """Custom type tmnxCpmProtPortOverallRateLimit based on TmnxCpmPacketRateLimit"""
    defaultValue = -1


_TmnxCpmProtPortOverallRateLimit_Type.__name__ = "TmnxCpmPacketRateLimit"
_TmnxCpmProtPortOverallRateLimit_Object = MibScalar
tmnxCpmProtPortOverallRateLimit = _TmnxCpmProtPortOverallRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 23),
    _TmnxCpmProtPortOverallRateLimit_Type()
)
tmnxCpmProtPortOverallRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmProtPortOverallRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtPortOverallRateLimit.setUnits("packets per second")
_TmnxCpmProtDetectPeriod_Type = Unsigned32
_TmnxCpmProtDetectPeriod_Object = MibScalar
tmnxCpmProtDetectPeriod = _TmnxCpmProtDetectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 24),
    _TmnxCpmProtDetectPeriod_Type()
)
tmnxCpmProtDetectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtDetectPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtDetectPeriod.setUnits("100 milliseconds")
_TCpmMacFilterTable_Object = MibTable
tCpmMacFilterTable = _TCpmMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25)
)
if mibBuilder.loadTexts:
    tCpmMacFilterTable.setStatus("current")
_TCpmMacFilterEntry_Object = MibTableRow
tCpmMacFilterEntry = _TCpmMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1)
)
tCpmMacFilterEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryId"),
)
if mibBuilder.loadTexts:
    tCpmMacFilterEntry.setStatus("current")


class _TCpmMacFltrEntryId_Type(TEntryId):
    """Custom type tCpmMacFltrEntryId based on TEntryId"""
    subtypeSpec = TEntryId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_TCpmMacFltrEntryId_Type.__name__ = "TEntryId"
_TCpmMacFltrEntryId_Object = MibTableColumn
tCpmMacFltrEntryId = _TCpmMacFltrEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 1),
    _TCpmMacFltrEntryId_Type()
)
tCpmMacFltrEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryId.setStatus("current")
_TCpmMacFltrEntryRowStatus_Type = RowStatus
_TCpmMacFltrEntryRowStatus_Object = MibTableColumn
tCpmMacFltrEntryRowStatus = _TCpmMacFltrEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 2),
    _TCpmMacFltrEntryRowStatus_Type()
)
tCpmMacFltrEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryRowStatus.setStatus("current")
_TCpmMacFltrEntryLastChanged_Type = TimeStamp
_TCpmMacFltrEntryLastChanged_Object = MibTableColumn
tCpmMacFltrEntryLastChanged = _TCpmMacFltrEntryLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 3),
    _TCpmMacFltrEntryLastChanged_Type()
)
tCpmMacFltrEntryLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryLastChanged.setStatus("current")


class _TCpmMacFltrEntryLogId_Type(TFilterLogId):
    """Custom type tCpmMacFltrEntryLogId based on TFilterLogId"""
    defaultValue = 0


_TCpmMacFltrEntryLogId_Type.__name__ = "TFilterLogId"
_TCpmMacFltrEntryLogId_Object = MibTableColumn
tCpmMacFltrEntryLogId = _TCpmMacFltrEntryLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 4),
    _TCpmMacFltrEntryLogId_Type()
)
tCpmMacFltrEntryLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryLogId.setStatus("current")


class _TCpmMacFltrEntryDescription_Type(TItemDescription):
    """Custom type tCpmMacFltrEntryDescription based on TItemDescription"""
    defaultHexValue = ""


_TCpmMacFltrEntryDescription_Type.__name__ = "TItemDescription"
_TCpmMacFltrEntryDescription_Object = MibTableColumn
tCpmMacFltrEntryDescription = _TCpmMacFltrEntryDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 5),
    _TCpmMacFltrEntryDescription_Type()
)
tCpmMacFltrEntryDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDescription.setStatus("current")


class _TCpmMacFltrEntryAction_Type(TCpmFilterActionOrDefault):
    """Custom type tCpmMacFltrEntryAction based on TCpmFilterActionOrDefault"""
    defaultValue = 1


_TCpmMacFltrEntryAction_Type.__name__ = "TCpmFilterActionOrDefault"
_TCpmMacFltrEntryAction_Object = MibTableColumn
tCpmMacFltrEntryAction = _TCpmMacFltrEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 6),
    _TCpmMacFltrEntryAction_Type()
)
tCpmMacFltrEntryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryAction.setStatus("current")


class _TCpmMacFltrEntryQueueId_Type(TCpmFilterQueueId):
    """Custom type tCpmMacFltrEntryQueueId based on TCpmFilterQueueId"""
    defaultValue = 0


_TCpmMacFltrEntryQueueId_Type.__name__ = "TCpmFilterQueueId"
_TCpmMacFltrEntryQueueId_Object = MibTableColumn
tCpmMacFltrEntryQueueId = _TCpmMacFltrEntryQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 7),
    _TCpmMacFltrEntryQueueId_Type()
)
tCpmMacFltrEntryQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryQueueId.setStatus("current")


class _TCpmMacFltrEntryFrameType_Type(TmnxCpmMacFltrFrameType):
    """Custom type tCpmMacFltrEntryFrameType based on TmnxCpmMacFltrFrameType"""
    defaultValue = -1


_TCpmMacFltrEntryFrameType_Type.__name__ = "TmnxCpmMacFltrFrameType"
_TCpmMacFltrEntryFrameType_Object = MibTableColumn
tCpmMacFltrEntryFrameType = _TCpmMacFltrEntryFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 8),
    _TCpmMacFltrEntryFrameType_Type()
)
tCpmMacFltrEntryFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryFrameType.setStatus("current")


class _TCpmMacFltrEntrySvcId_Type(TmnxServId):
    """Custom type tCpmMacFltrEntrySvcId based on TmnxServId"""
    defaultValue = 0


_TCpmMacFltrEntrySvcId_Type.__name__ = "TmnxServId"
_TCpmMacFltrEntrySvcId_Object = MibTableColumn
tCpmMacFltrEntrySvcId = _TCpmMacFltrEntrySvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 9),
    _TCpmMacFltrEntrySvcId_Type()
)
tCpmMacFltrEntrySvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntrySvcId.setStatus("current")


class _TCpmMacFltrEntryDot1pValue_Type(Dot1PPriority):
    """Custom type tCpmMacFltrEntryDot1pValue based on Dot1PPriority"""
    defaultValue = -1


_TCpmMacFltrEntryDot1pValue_Type.__name__ = "Dot1PPriority"
_TCpmMacFltrEntryDot1pValue_Object = MibTableColumn
tCpmMacFltrEntryDot1pValue = _TCpmMacFltrEntryDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 10),
    _TCpmMacFltrEntryDot1pValue_Type()
)
tCpmMacFltrEntryDot1pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDot1pValue.setStatus("current")


class _TCpmMacFltrEntryDot1pMask_Type(Dot1PPriorityMask):
    """Custom type tCpmMacFltrEntryDot1pMask based on Dot1PPriorityMask"""
    defaultValue = 0


_TCpmMacFltrEntryDot1pMask_Type.__name__ = "Dot1PPriorityMask"
_TCpmMacFltrEntryDot1pMask_Object = MibTableColumn
tCpmMacFltrEntryDot1pMask = _TCpmMacFltrEntryDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 11),
    _TCpmMacFltrEntryDot1pMask_Type()
)
tCpmMacFltrEntryDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDot1pMask.setStatus("current")


class _TCpmMacFltrEntryDsap_Type(ServiceAccessPoint):
    """Custom type tCpmMacFltrEntryDsap based on ServiceAccessPoint"""
    defaultValue = -1


_TCpmMacFltrEntryDsap_Type.__name__ = "ServiceAccessPoint"
_TCpmMacFltrEntryDsap_Object = MibTableColumn
tCpmMacFltrEntryDsap = _TCpmMacFltrEntryDsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 12),
    _TCpmMacFltrEntryDsap_Type()
)
tCpmMacFltrEntryDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDsap.setStatus("current")


class _TCpmMacFltrEntryDsapMask_Type(ServiceAccessPoint):
    """Custom type tCpmMacFltrEntryDsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TCpmMacFltrEntryDsapMask_Type.__name__ = "ServiceAccessPoint"
_TCpmMacFltrEntryDsapMask_Object = MibTableColumn
tCpmMacFltrEntryDsapMask = _TCpmMacFltrEntryDsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 13),
    _TCpmMacFltrEntryDsapMask_Type()
)
tCpmMacFltrEntryDsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDsapMask.setStatus("current")


class _TCpmMacFltrEntrySrcMAC_Type(MacAddress):
    """Custom type tCpmMacFltrEntrySrcMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TCpmMacFltrEntrySrcMAC_Type.__name__ = "MacAddress"
_TCpmMacFltrEntrySrcMAC_Object = MibTableColumn
tCpmMacFltrEntrySrcMAC = _TCpmMacFltrEntrySrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 14),
    _TCpmMacFltrEntrySrcMAC_Type()
)
tCpmMacFltrEntrySrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntrySrcMAC.setStatus("current")


class _TCpmMacFltrEntrySrcMACMask_Type(MacAddress):
    """Custom type tCpmMacFltrEntrySrcMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TCpmMacFltrEntrySrcMACMask_Type.__name__ = "MacAddress"
_TCpmMacFltrEntrySrcMACMask_Object = MibTableColumn
tCpmMacFltrEntrySrcMACMask = _TCpmMacFltrEntrySrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 15),
    _TCpmMacFltrEntrySrcMACMask_Type()
)
tCpmMacFltrEntrySrcMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntrySrcMACMask.setStatus("current")


class _TCpmMacFltrEntryDstMAC_Type(MacAddress):
    """Custom type tCpmMacFltrEntryDstMAC based on MacAddress"""
    defaultHexValue = "000000000000"


_TCpmMacFltrEntryDstMAC_Type.__name__ = "MacAddress"
_TCpmMacFltrEntryDstMAC_Object = MibTableColumn
tCpmMacFltrEntryDstMAC = _TCpmMacFltrEntryDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 16),
    _TCpmMacFltrEntryDstMAC_Type()
)
tCpmMacFltrEntryDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDstMAC.setStatus("current")


class _TCpmMacFltrEntryDstMACMask_Type(MacAddress):
    """Custom type tCpmMacFltrEntryDstMACMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TCpmMacFltrEntryDstMACMask_Type.__name__ = "MacAddress"
_TCpmMacFltrEntryDstMACMask_Object = MibTableColumn
tCpmMacFltrEntryDstMACMask = _TCpmMacFltrEntryDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 17),
    _TCpmMacFltrEntryDstMACMask_Type()
)
tCpmMacFltrEntryDstMACMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryDstMACMask.setStatus("current")


class _TCpmMacFltrEntryEtherType_Type(Integer32):
    """Custom type tCpmMacFltrEntryEtherType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TCpmMacFltrEntryEtherType_Type.__name__ = "Integer32"
_TCpmMacFltrEntryEtherType_Object = MibTableColumn
tCpmMacFltrEntryEtherType = _TCpmMacFltrEntryEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 18),
    _TCpmMacFltrEntryEtherType_Type()
)
tCpmMacFltrEntryEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryEtherType.setStatus("current")


class _TCpmMacFltrEntrySsap_Type(ServiceAccessPoint):
    """Custom type tCpmMacFltrEntrySsap based on ServiceAccessPoint"""
    defaultValue = -1


_TCpmMacFltrEntrySsap_Type.__name__ = "ServiceAccessPoint"
_TCpmMacFltrEntrySsap_Object = MibTableColumn
tCpmMacFltrEntrySsap = _TCpmMacFltrEntrySsap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 21),
    _TCpmMacFltrEntrySsap_Type()
)
tCpmMacFltrEntrySsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntrySsap.setStatus("current")


class _TCpmMacFltrEntrySsapMask_Type(ServiceAccessPoint):
    """Custom type tCpmMacFltrEntrySsapMask based on ServiceAccessPoint"""
    defaultValue = -1


_TCpmMacFltrEntrySsapMask_Type.__name__ = "ServiceAccessPoint"
_TCpmMacFltrEntrySsapMask_Object = MibTableColumn
tCpmMacFltrEntrySsapMask = _TCpmMacFltrEntrySsapMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 22),
    _TCpmMacFltrEntrySsapMask_Type()
)
tCpmMacFltrEntrySsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntrySsapMask.setStatus("current")


class _TCpmMacFltrEntryCfmOpCodeOper_Type(TOperator):
    """Custom type tCpmMacFltrEntryCfmOpCodeOper based on TOperator"""
    defaultValue = 0


_TCpmMacFltrEntryCfmOpCodeOper_Type.__name__ = "TOperator"
_TCpmMacFltrEntryCfmOpCodeOper_Object = MibTableColumn
tCpmMacFltrEntryCfmOpCodeOper = _TCpmMacFltrEntryCfmOpCodeOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 23),
    _TCpmMacFltrEntryCfmOpCodeOper_Type()
)
tCpmMacFltrEntryCfmOpCodeOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryCfmOpCodeOper.setStatus("current")


class _TCpmMacFltrEntryCfmOpCodeValue1_Type(Unsigned32):
    """Custom type tCpmMacFltrEntryCfmOpCodeValue1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TCpmMacFltrEntryCfmOpCodeValue1_Type.__name__ = "Unsigned32"
_TCpmMacFltrEntryCfmOpCodeValue1_Object = MibTableColumn
tCpmMacFltrEntryCfmOpCodeValue1 = _TCpmMacFltrEntryCfmOpCodeValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 24),
    _TCpmMacFltrEntryCfmOpCodeValue1_Type()
)
tCpmMacFltrEntryCfmOpCodeValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryCfmOpCodeValue1.setStatus("current")


class _TCpmMacFltrEntryCfmOpCodeValue2_Type(Unsigned32):
    """Custom type tCpmMacFltrEntryCfmOpCodeValue2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TCpmMacFltrEntryCfmOpCodeValue2_Type.__name__ = "Unsigned32"
_TCpmMacFltrEntryCfmOpCodeValue2_Object = MibTableColumn
tCpmMacFltrEntryCfmOpCodeValue2 = _TCpmMacFltrEntryCfmOpCodeValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 25),
    _TCpmMacFltrEntryCfmOpCodeValue2_Type()
)
tCpmMacFltrEntryCfmOpCodeValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryCfmOpCodeValue2.setStatus("current")
_TCpmMacFltrEntryLogCreated_Type = TruthValue
_TCpmMacFltrEntryLogCreated_Object = MibTableColumn
tCpmMacFltrEntryLogCreated = _TCpmMacFltrEntryLogCreated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 25, 1, 26),
    _TCpmMacFltrEntryLogCreated_Type()
)
tCpmMacFltrEntryLogCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmMacFltrEntryLogCreated.setStatus("current")
_TCpmMacFilterStatsTable_Object = MibTable
tCpmMacFilterStatsTable = _TCpmMacFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 26)
)
if mibBuilder.loadTexts:
    tCpmMacFilterStatsTable.setStatus("current")
_TCpmMacFilterStatsEntry_Object = MibTableRow
tCpmMacFilterStatsEntry = _TCpmMacFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 26, 1)
)
tCpmMacFilterStatsEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryId"),
)
if mibBuilder.loadTexts:
    tCpmMacFilterStatsEntry.setStatus("current")
_TCpmMacFilterStatsDroppedPkts_Type = Counter64
_TCpmMacFilterStatsDroppedPkts_Object = MibTableColumn
tCpmMacFilterStatsDroppedPkts = _TCpmMacFilterStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 26, 1, 1),
    _TCpmMacFilterStatsDroppedPkts_Type()
)
tCpmMacFilterStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmMacFilterStatsDroppedPkts.setStatus("current")
_TCpmMacFilterStatsForwardedPkts_Type = Counter64
_TCpmMacFilterStatsForwardedPkts_Object = MibTableColumn
tCpmMacFilterStatsForwardedPkts = _TCpmMacFilterStatsForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 26, 1, 2),
    _TCpmMacFilterStatsForwardedPkts_Type()
)
tCpmMacFilterStatsForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmMacFilterStatsForwardedPkts.setStatus("current")


class _TmnxCpmProtAllowShamLinkPackets_Type(TruthValue):
    """Custom type tmnxCpmProtAllowShamLinkPackets based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtAllowShamLinkPackets_Type.__name__ = "TruthValue"
_TmnxCpmProtAllowShamLinkPackets_Object = MibScalar
tmnxCpmProtAllowShamLinkPackets = _TmnxCpmProtAllowShamLinkPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 27),
    _TmnxCpmProtAllowShamLinkPackets_Type()
)
tmnxCpmProtAllowShamLinkPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmProtAllowShamLinkPackets.setStatus("current")
_TmnxCpmProtViolVdoSvcTable_Object = MibTable
tmnxCpmProtViolVdoSvcTable = _TmnxCpmProtViolVdoSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28)
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcTable.setStatus("current")
_TmnxCpmProtViolVdoSvcEntry_Object = MibTableRow
tmnxCpmProtViolVdoSvcEntry = _TmnxCpmProtViolVdoSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1)
)
tmnxCpmProtViolVdoSvcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcCltAddrType"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcCltAddr"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcEntry.setStatus("current")
_TmnxCpmProtViolVdoSvcCltAddrType_Type = InetAddressType
_TmnxCpmProtViolVdoSvcCltAddrType_Object = MibTableColumn
tmnxCpmProtViolVdoSvcCltAddrType = _TmnxCpmProtViolVdoSvcCltAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1, 1),
    _TmnxCpmProtViolVdoSvcCltAddrType_Type()
)
tmnxCpmProtViolVdoSvcCltAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcCltAddrType.setStatus("current")


class _TmnxCpmProtViolVdoSvcCltAddr_Type(InetAddress):
    """Custom type tmnxCpmProtViolVdoSvcCltAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCpmProtViolVdoSvcCltAddr_Type.__name__ = "InetAddress"
_TmnxCpmProtViolVdoSvcCltAddr_Object = MibTableColumn
tmnxCpmProtViolVdoSvcCltAddr = _TmnxCpmProtViolVdoSvcCltAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1, 2),
    _TmnxCpmProtViolVdoSvcCltAddr_Type()
)
tmnxCpmProtViolVdoSvcCltAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcCltAddr.setStatus("current")
_TmnxCpmProtViolVdoSvcPeriods_Type = Gauge32
_TmnxCpmProtViolVdoSvcPeriods_Object = MibTableColumn
tmnxCpmProtViolVdoSvcPeriods = _TmnxCpmProtViolVdoSvcPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1, 3),
    _TmnxCpmProtViolVdoSvcPeriods_Type()
)
tmnxCpmProtViolVdoSvcPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcPeriods.setStatus("current")
_TmnxCpmProtViolVdoSvcTimeStarted_Type = TimeStamp
_TmnxCpmProtViolVdoSvcTimeStarted_Object = MibTableColumn
tmnxCpmProtViolVdoSvcTimeStarted = _TmnxCpmProtViolVdoSvcTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1, 4),
    _TmnxCpmProtViolVdoSvcTimeStarted_Type()
)
tmnxCpmProtViolVdoSvcTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcTimeStarted.setStatus("current")
_TmnxCpmProtViolVdoSvcTime_Type = TimeStamp
_TmnxCpmProtViolVdoSvcTime_Object = MibTableColumn
tmnxCpmProtViolVdoSvcTime = _TmnxCpmProtViolVdoSvcTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1, 5),
    _TmnxCpmProtViolVdoSvcTime_Type()
)
tmnxCpmProtViolVdoSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcTime.setStatus("current")
_TmnxCpmProtViolVdoSvcVrtrIfIndex_Type = InterfaceIndex
_TmnxCpmProtViolVdoSvcVrtrIfIndex_Object = MibTableColumn
tmnxCpmProtViolVdoSvcVrtrIfIndex = _TmnxCpmProtViolVdoSvcVrtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 28, 1, 6),
    _TmnxCpmProtViolVdoSvcVrtrIfIndex_Type()
)
tmnxCpmProtViolVdoSvcVrtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcVrtrIfIndex.setStatus("current")
_TmnxCpmProtViolVdoVrtrTable_Object = MibTable
tmnxCpmProtViolVdoVrtrTable = _TmnxCpmProtViolVdoVrtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29)
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrTable.setStatus("current")
_TmnxCpmProtViolVdoVrtrEntry_Object = MibTableRow
tmnxCpmProtViolVdoVrtrEntry = _TmnxCpmProtViolVdoVrtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1)
)
tmnxCpmProtViolVdoVrtrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrCltAdrType"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrCltAddr"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrEntry.setStatus("current")
_TmnxCpmProtViolVdoVrtrCltAdrType_Type = InetAddressType
_TmnxCpmProtViolVdoVrtrCltAdrType_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrCltAdrType = _TmnxCpmProtViolVdoVrtrCltAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 1),
    _TmnxCpmProtViolVdoVrtrCltAdrType_Type()
)
tmnxCpmProtViolVdoVrtrCltAdrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrCltAdrType.setStatus("current")


class _TmnxCpmProtViolVdoVrtrCltAddr_Type(InetAddress):
    """Custom type tmnxCpmProtViolVdoVrtrCltAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCpmProtViolVdoVrtrCltAddr_Type.__name__ = "InetAddress"
_TmnxCpmProtViolVdoVrtrCltAddr_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrCltAddr = _TmnxCpmProtViolVdoVrtrCltAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 2),
    _TmnxCpmProtViolVdoVrtrCltAddr_Type()
)
tmnxCpmProtViolVdoVrtrCltAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrCltAddr.setStatus("current")
_TmnxCpmProtViolVdoVrtrPeriods_Type = Gauge32
_TmnxCpmProtViolVdoVrtrPeriods_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrPeriods = _TmnxCpmProtViolVdoVrtrPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 3),
    _TmnxCpmProtViolVdoVrtrPeriods_Type()
)
tmnxCpmProtViolVdoVrtrPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrPeriods.setStatus("current")
_TmnxCpmProtViolVdoVrtrTimeStart_Type = TimeStamp
_TmnxCpmProtViolVdoVrtrTimeStart_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrTimeStart = _TmnxCpmProtViolVdoVrtrTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 4),
    _TmnxCpmProtViolVdoVrtrTimeStart_Type()
)
tmnxCpmProtViolVdoVrtrTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrTimeStart.setStatus("current")
_TmnxCpmProtViolVdoVrtrTime_Type = TimeStamp
_TmnxCpmProtViolVdoVrtrTime_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrTime = _TmnxCpmProtViolVdoVrtrTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 5),
    _TmnxCpmProtViolVdoVrtrTime_Type()
)
tmnxCpmProtViolVdoVrtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrTime.setStatus("current")
_TmnxCpmProtViolVdoVrtrSvcId_Type = TmnxServId
_TmnxCpmProtViolVdoVrtrSvcId_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrSvcId = _TmnxCpmProtViolVdoVrtrSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 6),
    _TmnxCpmProtViolVdoVrtrSvcId_Type()
)
tmnxCpmProtViolVdoVrtrSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrSvcId.setStatus("current")
_TmnxCpmProtViolVdoVrtrIfIndex_Type = InterfaceIndex
_TmnxCpmProtViolVdoVrtrIfIndex_Object = MibTableColumn
tmnxCpmProtViolVdoVrtrIfIndex = _TmnxCpmProtViolVdoVrtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 29, 1, 7),
    _TmnxCpmProtViolVdoVrtrIfIndex_Type()
)
tmnxCpmProtViolVdoVrtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrIfIndex.setStatus("current")
_TmnxCpmProtEthCfmPolTableLastChg_Type = TimeStamp
_TmnxCpmProtEthCfmPolTableLastChg_Object = MibScalar
tmnxCpmProtEthCfmPolTableLastChg = _TmnxCpmProtEthCfmPolTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 30),
    _TmnxCpmProtEthCfmPolTableLastChg_Type()
)
tmnxCpmProtEthCfmPolTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolTableLastChg.setStatus("current")
_TmnxCpmProtEthCfmPolTable_Object = MibTable
tmnxCpmProtEthCfmPolTable = _TmnxCpmProtEthCfmPolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31)
)
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolTable.setStatus("current")
_TmnxCpmProtEthCfmPolEntry_Object = MibTableRow
tmnxCpmProtEthCfmPolEntry = _TmnxCpmProtEthCfmPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1)
)
tmnxCpmProtEthCfmPolEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtPolicyId"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolEntryNum"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolEntry.setStatus("current")


class _TmnxCpmProtEthCfmPolEntryNum_Type(Unsigned32):
    """Custom type tmnxCpmProtEthCfmPolEntryNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxCpmProtEthCfmPolEntryNum_Type.__name__ = "Unsigned32"
_TmnxCpmProtEthCfmPolEntryNum_Object = MibTableColumn
tmnxCpmProtEthCfmPolEntryNum = _TmnxCpmProtEthCfmPolEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1, 1),
    _TmnxCpmProtEthCfmPolEntryNum_Type()
)
tmnxCpmProtEthCfmPolEntryNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolEntryNum.setStatus("current")
_TmnxCpmProtEthCfmPolRowStatus_Type = RowStatus
_TmnxCpmProtEthCfmPolRowStatus_Object = MibTableColumn
tmnxCpmProtEthCfmPolRowStatus = _TmnxCpmProtEthCfmPolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1, 2),
    _TmnxCpmProtEthCfmPolRowStatus_Type()
)
tmnxCpmProtEthCfmPolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolRowStatus.setStatus("current")
_TmnxCpmProtEthCfmPolLastChanged_Type = TimeStamp
_TmnxCpmProtEthCfmPolLastChanged_Object = MibTableColumn
tmnxCpmProtEthCfmPolLastChanged = _TmnxCpmProtEthCfmPolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1, 3),
    _TmnxCpmProtEthCfmPolLastChanged_Type()
)
tmnxCpmProtEthCfmPolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolLastChanged.setStatus("current")


class _TmnxCpmProtEthCfmPolLevelSet_Type(Bits):
    """Custom type tmnxCpmProtEthCfmPolLevelSet based on Bits"""
    namedValues = NamedValues(
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )

_TmnxCpmProtEthCfmPolLevelSet_Type.__name__ = "Bits"
_TmnxCpmProtEthCfmPolLevelSet_Object = MibTableColumn
tmnxCpmProtEthCfmPolLevelSet = _TmnxCpmProtEthCfmPolLevelSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1, 4),
    _TmnxCpmProtEthCfmPolLevelSet_Type()
)
tmnxCpmProtEthCfmPolLevelSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolLevelSet.setStatus("current")


class _TmnxCpmProtEthCfmPolOpCodeSet_Type(Bits):
    """Custom type tmnxCpmProtEthCfmPolOpCodeSet based on Bits"""
    namedValues = NamedValues(
        *(("opCode0", 0),
          ("opCode1", 1),
          ("opCode2", 2),
          ("opCode3", 3),
          ("opCode4", 4),
          ("opCode5", 5),
          ("opCode6", 6),
          ("opCode7", 7),
          ("opCode8", 8),
          ("opCode9", 9),
          ("opCode10", 10),
          ("opCode11", 11),
          ("opCode12", 12),
          ("opCode13", 13),
          ("opCode14", 14),
          ("opCode15", 15),
          ("opCode16", 16),
          ("opCode17", 17),
          ("opCode18", 18),
          ("opCode19", 19),
          ("opCode20", 20),
          ("opCode21", 21),
          ("opCode22", 22),
          ("opCode23", 23),
          ("opCode24", 24),
          ("opCode25", 25),
          ("opCode26", 26),
          ("opCode27", 27),
          ("opCode28", 28),
          ("opCode29", 29),
          ("opCode30", 30),
          ("opCode31", 31),
          ("opCode32", 32),
          ("opCode33", 33),
          ("opCode34", 34),
          ("opCode35", 35),
          ("opCode36", 36),
          ("opCode37", 37),
          ("opCode38", 38),
          ("opCode39", 39),
          ("opCode40", 40),
          ("opCode41", 41),
          ("opCode42", 42),
          ("opCode43", 43),
          ("opCode44", 44),
          ("opCode45", 45),
          ("opCode46", 46),
          ("opCode47", 47),
          ("opCode48", 48),
          ("opCode49", 49),
          ("opCode50", 50),
          ("opCode51", 51),
          ("opCode52", 52),
          ("opCode53", 53),
          ("opCode54", 54),
          ("opCode55", 55),
          ("opCode56", 56),
          ("opCode57", 57),
          ("opCode58", 58),
          ("opCode59", 59),
          ("opCode60", 60),
          ("opCode61", 61),
          ("opCode62", 62),
          ("opCode63", 63),
          ("opCode64", 64),
          ("opCode65", 65),
          ("opCode66", 66),
          ("opCode67", 67),
          ("opCode68", 68),
          ("opCode69", 69),
          ("opCode70", 70),
          ("opCode71", 71),
          ("opCode72", 72),
          ("opCode73", 73),
          ("opCode74", 74),
          ("opCode75", 75),
          ("opCode76", 76),
          ("opCode77", 77),
          ("opCode78", 78),
          ("opCode79", 79),
          ("opCode80", 80),
          ("opCode81", 81),
          ("opCode82", 82),
          ("opCode83", 83),
          ("opCode84", 84),
          ("opCode85", 85),
          ("opCode86", 86),
          ("opCode87", 87),
          ("opCode88", 88),
          ("opCode89", 89),
          ("opCode90", 90),
          ("opCode91", 91),
          ("opCode92", 92),
          ("opCode93", 93),
          ("opCode94", 94),
          ("opCode95", 95),
          ("opCode96", 96),
          ("opCode97", 97),
          ("opCode98", 98),
          ("opCode99", 99),
          ("opCode100", 100),
          ("opCode101", 101),
          ("opCode102", 102),
          ("opCode103", 103),
          ("opCode104", 104),
          ("opCode105", 105),
          ("opCode106", 106),
          ("opCode107", 107),
          ("opCode108", 108),
          ("opCode109", 109),
          ("opCode110", 110),
          ("opCode111", 111),
          ("opCode112", 112),
          ("opCode113", 113),
          ("opCode114", 114),
          ("opCode115", 115),
          ("opCode116", 116),
          ("opCode117", 117),
          ("opCode118", 118),
          ("opCode119", 119),
          ("opCode120", 120),
          ("opCode121", 121),
          ("opCode122", 122),
          ("opCode123", 123),
          ("opCode124", 124),
          ("opCode125", 125),
          ("opCode126", 126),
          ("opCode127", 127),
          ("opCode128", 128),
          ("opCode129", 129),
          ("opCode130", 130),
          ("opCode131", 131),
          ("opCode132", 132),
          ("opCode133", 133),
          ("opCode134", 134),
          ("opCode135", 135),
          ("opCode136", 136),
          ("opCode137", 137),
          ("opCode138", 138),
          ("opCode139", 139),
          ("opCode140", 140),
          ("opCode141", 141),
          ("opCode142", 142),
          ("opCode143", 143),
          ("opCode144", 144),
          ("opCode145", 145),
          ("opCode146", 146),
          ("opCode147", 147),
          ("opCode148", 148),
          ("opCode149", 149),
          ("opCode150", 150),
          ("opCode151", 151),
          ("opCode152", 152),
          ("opCode153", 153),
          ("opCode154", 154),
          ("opCode155", 155),
          ("opCode156", 156),
          ("opCode157", 157),
          ("opCode158", 158),
          ("opCode159", 159),
          ("opCode160", 160),
          ("opCode161", 161),
          ("opCode162", 162),
          ("opCode163", 163),
          ("opCode164", 164),
          ("opCode165", 165),
          ("opCode166", 166),
          ("opCode167", 167),
          ("opCode168", 168),
          ("opCode169", 169),
          ("opCode170", 170),
          ("opCode171", 171),
          ("opCode172", 172),
          ("opCode173", 173),
          ("opCode174", 174),
          ("opCode175", 175),
          ("opCode176", 176),
          ("opCode177", 177),
          ("opCode178", 178),
          ("opCode179", 179),
          ("opCode180", 180),
          ("opCode181", 181),
          ("opCode182", 182),
          ("opCode183", 183),
          ("opCode184", 184),
          ("opCode185", 185),
          ("opCode186", 186),
          ("opCode187", 187),
          ("opCode188", 188),
          ("opCode189", 189),
          ("opCode190", 190),
          ("opCode191", 191),
          ("opCode192", 192),
          ("opCode193", 193),
          ("opCode194", 194),
          ("opCode195", 195),
          ("opCode196", 196),
          ("opCode197", 197),
          ("opCode198", 198),
          ("opCode199", 199),
          ("opCode200", 200),
          ("opCode201", 201),
          ("opCode202", 202),
          ("opCode203", 203),
          ("opCode204", 204),
          ("opCode205", 205),
          ("opCode206", 206),
          ("opCode207", 207),
          ("opCode208", 208),
          ("opCode209", 209),
          ("opCode210", 210),
          ("opCode211", 211),
          ("opCode212", 212),
          ("opCode213", 213),
          ("opCode214", 214),
          ("opCode215", 215),
          ("opCode216", 216),
          ("opCode217", 217),
          ("opCode218", 218),
          ("opCode219", 219),
          ("opCode220", 220),
          ("opCode221", 221),
          ("opCode222", 222),
          ("opCode223", 223),
          ("opCode224", 224),
          ("opCode225", 225),
          ("opCode226", 226),
          ("opCode227", 227),
          ("opCode228", 228),
          ("opCode229", 229),
          ("opCode230", 230),
          ("opCode231", 231),
          ("opCode232", 232),
          ("opCode233", 233),
          ("opCode234", 234),
          ("opCode235", 235),
          ("opCode236", 236),
          ("opCode237", 237),
          ("opCode238", 238),
          ("opCode239", 239),
          ("opCode240", 240),
          ("opCode241", 241),
          ("opCode242", 242),
          ("opCode243", 243),
          ("opCode244", 244),
          ("opCode245", 245),
          ("opCode246", 246),
          ("opCode247", 247),
          ("opCode248", 248),
          ("opCode249", 249),
          ("opCode250", 250),
          ("opCode251", 251),
          ("opCode252", 252),
          ("opCode253", 253),
          ("opCode254", 254),
          ("opCode255", 255))
    )

_TmnxCpmProtEthCfmPolOpCodeSet_Type.__name__ = "Bits"
_TmnxCpmProtEthCfmPolOpCodeSet_Object = MibTableColumn
tmnxCpmProtEthCfmPolOpCodeSet = _TmnxCpmProtEthCfmPolOpCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1, 5),
    _TmnxCpmProtEthCfmPolOpCodeSet_Type()
)
tmnxCpmProtEthCfmPolOpCodeSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolOpCodeSet.setStatus("current")


class _TmnxCpmProtEthCfmPolRateLimit_Type(TmnxCpmPktPolRateLimitInclZero):
    """Custom type tmnxCpmProtEthCfmPolRateLimit based on TmnxCpmPktPolRateLimitInclZero"""
    defaultValue = -1


_TmnxCpmProtEthCfmPolRateLimit_Type.__name__ = "TmnxCpmPktPolRateLimitInclZero"
_TmnxCpmProtEthCfmPolRateLimit_Object = MibTableColumn
tmnxCpmProtEthCfmPolRateLimit = _TmnxCpmProtEthCfmPolRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 31, 1, 6),
    _TmnxCpmProtEthCfmPolRateLimit_Type()
)
tmnxCpmProtEthCfmPolRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolRateLimit.setUnits("packets per second")
_TmnxCpmProtViolSdpBindTblLastChg_Type = TimeStamp
_TmnxCpmProtViolSdpBindTblLastChg_Object = MibScalar
tmnxCpmProtViolSdpBindTblLastChg = _TmnxCpmProtViolSdpBindTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 32),
    _TmnxCpmProtViolSdpBindTblLastChg_Type()
)
tmnxCpmProtViolSdpBindTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindTblLastChg.setStatus("current")
_TmnxCpmProtViolSdpBindTable_Object = MibTable
tmnxCpmProtViolSdpBindTable = _TmnxCpmProtViolSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 33)
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindTable.setStatus("current")
_TmnxCpmProtViolSdpBindEntry_Object = MibTableRow
tmnxCpmProtViolSdpBindEntry = _TmnxCpmProtViolSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 33, 1)
)
tmnxCpmProtViolSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindEntry.setStatus("current")
_TmnxCpmProtViolSdpBindPeriods_Type = Counter32
_TmnxCpmProtViolSdpBindPeriods_Object = MibTableColumn
tmnxCpmProtViolSdpBindPeriods = _TmnxCpmProtViolSdpBindPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 33, 1, 1),
    _TmnxCpmProtViolSdpBindPeriods_Type()
)
tmnxCpmProtViolSdpBindPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindPeriods.setStatus("current")
_TmnxCpmProtViolSdpBindTimeStartd_Type = TimeStamp
_TmnxCpmProtViolSdpBindTimeStartd_Object = MibTableColumn
tmnxCpmProtViolSdpBindTimeStartd = _TmnxCpmProtViolSdpBindTimeStartd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 33, 1, 2),
    _TmnxCpmProtViolSdpBindTimeStartd_Type()
)
tmnxCpmProtViolSdpBindTimeStartd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindTimeStartd.setStatus("current")
_TmnxCpmProtViolSdpBindTime_Type = TimeStamp
_TmnxCpmProtViolSdpBindTime_Object = MibTableColumn
tmnxCpmProtViolSdpBindTime = _TmnxCpmProtViolSdpBindTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 33, 1, 3),
    _TmnxCpmProtViolSdpBindTime_Type()
)
tmnxCpmProtViolSdpBindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindTime.setStatus("current")
_TmnxCpmProtExcdSdpBindTblLastChg_Type = TimeStamp
_TmnxCpmProtExcdSdpBindTblLastChg_Object = MibScalar
tmnxCpmProtExcdSdpBindTblLastChg = _TmnxCpmProtExcdSdpBindTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 34),
    _TmnxCpmProtExcdSdpBindTblLastChg_Type()
)
tmnxCpmProtExcdSdpBindTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindTblLastChg.setStatus("current")
_TmnxCpmProtExcdSdpBindTable_Object = MibTable
tmnxCpmProtExcdSdpBindTable = _TmnxCpmProtExcdSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 35)
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindTable.setStatus("current")
_TmnxCpmProtExcdSdpBindEntry_Object = MibTableRow
tmnxCpmProtExcdSdpBindEntry = _TmnxCpmProtExcdSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 35, 1)
)
tmnxCpmProtExcdSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindMac"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEntry.setStatus("current")
_TmnxCpmProtExcdSdpBindMac_Type = MacAddress
_TmnxCpmProtExcdSdpBindMac_Object = MibTableColumn
tmnxCpmProtExcdSdpBindMac = _TmnxCpmProtExcdSdpBindMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 35, 1, 1),
    _TmnxCpmProtExcdSdpBindMac_Type()
)
tmnxCpmProtExcdSdpBindMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindMac.setStatus("current")
_TmnxCpmProtExcdSdpBindPeriods_Type = Counter32
_TmnxCpmProtExcdSdpBindPeriods_Object = MibTableColumn
tmnxCpmProtExcdSdpBindPeriods = _TmnxCpmProtExcdSdpBindPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 35, 1, 2),
    _TmnxCpmProtExcdSdpBindPeriods_Type()
)
tmnxCpmProtExcdSdpBindPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindPeriods.setStatus("current")
_TmnxCpmProtExcdSdpBindTimeStartd_Type = TimeStamp
_TmnxCpmProtExcdSdpBindTimeStartd_Object = MibTableColumn
tmnxCpmProtExcdSdpBindTimeStartd = _TmnxCpmProtExcdSdpBindTimeStartd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 35, 1, 3),
    _TmnxCpmProtExcdSdpBindTimeStartd_Type()
)
tmnxCpmProtExcdSdpBindTimeStartd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindTimeStartd.setStatus("current")
_TmnxCpmProtExcdSdpBindTime_Type = TimeStamp
_TmnxCpmProtExcdSdpBindTime_Object = MibTableColumn
tmnxCpmProtExcdSdpBindTime = _TmnxCpmProtExcdSdpBindTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 35, 1, 4),
    _TmnxCpmProtExcdSdpBindTime_Type()
)
tmnxCpmProtExcdSdpBindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindTime.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmTblLChg_Type = TimeStamp
_TmnxCpmProtExcdSdpBindEcmTblLChg_Object = MibScalar
tmnxCpmProtExcdSdpBindEcmTblLChg = _TmnxCpmProtExcdSdpBindEcmTblLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 36),
    _TmnxCpmProtExcdSdpBindEcmTblLChg_Type()
)
tmnxCpmProtExcdSdpBindEcmTblLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmTblLChg.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmTable_Object = MibTable
tmnxCpmProtExcdSdpBindEcmTable = _TmnxCpmProtExcdSdpBindEcmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37)
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmTable.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmEntry_Object = MibTableRow
tmnxCpmProtExcdSdpBindEcmEntry = _TmnxCpmProtExcdSdpBindEcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1)
)
tmnxCpmProtExcdSdpBindEcmEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmMac"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmLevel"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmOpCode"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmEntry.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmMac_Type = MacAddress
_TmnxCpmProtExcdSdpBindEcmMac_Object = MibTableColumn
tmnxCpmProtExcdSdpBindEcmMac = _TmnxCpmProtExcdSdpBindEcmMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1, 1),
    _TmnxCpmProtExcdSdpBindEcmMac_Type()
)
tmnxCpmProtExcdSdpBindEcmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmMac.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmLevel_Type = Dot1agCfmMDLevel
_TmnxCpmProtExcdSdpBindEcmLevel_Object = MibTableColumn
tmnxCpmProtExcdSdpBindEcmLevel = _TmnxCpmProtExcdSdpBindEcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1, 2),
    _TmnxCpmProtExcdSdpBindEcmLevel_Type()
)
tmnxCpmProtExcdSdpBindEcmLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmLevel.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmOpCode_Type = TmnxCpmProtEthCfmOpCode
_TmnxCpmProtExcdSdpBindEcmOpCode_Object = MibTableColumn
tmnxCpmProtExcdSdpBindEcmOpCode = _TmnxCpmProtExcdSdpBindEcmOpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1, 3),
    _TmnxCpmProtExcdSdpBindEcmOpCode_Type()
)
tmnxCpmProtExcdSdpBindEcmOpCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmOpCode.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmPeriods_Type = Counter32
_TmnxCpmProtExcdSdpBindEcmPeriods_Object = MibTableColumn
tmnxCpmProtExcdSdpBindEcmPeriods = _TmnxCpmProtExcdSdpBindEcmPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1, 4),
    _TmnxCpmProtExcdSdpBindEcmPeriods_Type()
)
tmnxCpmProtExcdSdpBindEcmPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmPeriods.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmStarted_Type = TimeStamp
_TmnxCpmProtExcdSdpBindEcmStarted_Object = MibTableColumn
tmnxCpmProtExcdSdpBindEcmStarted = _TmnxCpmProtExcdSdpBindEcmStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1, 5),
    _TmnxCpmProtExcdSdpBindEcmStarted_Type()
)
tmnxCpmProtExcdSdpBindEcmStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmStarted.setStatus("current")
_TmnxCpmProtExcdSdpBindEcmTime_Type = TimeStamp
_TmnxCpmProtExcdSdpBindEcmTime_Object = MibTableColumn
tmnxCpmProtExcdSdpBindEcmTime = _TmnxCpmProtExcdSdpBindEcmTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 37, 1, 6),
    _TmnxCpmProtExcdSdpBindEcmTime_Type()
)
tmnxCpmProtExcdSdpBindEcmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcmTime.setStatus("current")
_TmnxCpmProtExcdSapEcmTblLChg_Type = TimeStamp
_TmnxCpmProtExcdSapEcmTblLChg_Object = MibScalar
tmnxCpmProtExcdSapEcmTblLChg = _TmnxCpmProtExcdSapEcmTblLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 38),
    _TmnxCpmProtExcdSapEcmTblLChg_Type()
)
tmnxCpmProtExcdSapEcmTblLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmTblLChg.setStatus("current")
_TmnxCpmProtExcdSapEcmTable_Object = MibTable
tmnxCpmProtExcdSapEcmTable = _TmnxCpmProtExcdSapEcmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39)
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmTable.setStatus("current")
_TmnxCpmProtExcdSapEcmEntry_Object = MibTableRow
tmnxCpmProtExcdSapEcmEntry = _TmnxCpmProtExcdSapEcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1)
)
tmnxCpmProtExcdSapEcmEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmMac"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmLevel"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmOpCode"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmEntry.setStatus("current")
_TmnxCpmProtExcdSapEcmMac_Type = MacAddress
_TmnxCpmProtExcdSapEcmMac_Object = MibTableColumn
tmnxCpmProtExcdSapEcmMac = _TmnxCpmProtExcdSapEcmMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1, 1),
    _TmnxCpmProtExcdSapEcmMac_Type()
)
tmnxCpmProtExcdSapEcmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmMac.setStatus("current")
_TmnxCpmProtExcdSapEcmLevel_Type = Dot1agCfmMDLevel
_TmnxCpmProtExcdSapEcmLevel_Object = MibTableColumn
tmnxCpmProtExcdSapEcmLevel = _TmnxCpmProtExcdSapEcmLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1, 2),
    _TmnxCpmProtExcdSapEcmLevel_Type()
)
tmnxCpmProtExcdSapEcmLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmLevel.setStatus("current")
_TmnxCpmProtExcdSapEcmOpCode_Type = TmnxCpmProtEthCfmOpCode
_TmnxCpmProtExcdSapEcmOpCode_Object = MibTableColumn
tmnxCpmProtExcdSapEcmOpCode = _TmnxCpmProtExcdSapEcmOpCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1, 3),
    _TmnxCpmProtExcdSapEcmOpCode_Type()
)
tmnxCpmProtExcdSapEcmOpCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmOpCode.setStatus("current")
_TmnxCpmProtExcdSapEcmPeriods_Type = Counter32
_TmnxCpmProtExcdSapEcmPeriods_Object = MibTableColumn
tmnxCpmProtExcdSapEcmPeriods = _TmnxCpmProtExcdSapEcmPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1, 4),
    _TmnxCpmProtExcdSapEcmPeriods_Type()
)
tmnxCpmProtExcdSapEcmPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmPeriods.setStatus("current")
_TmnxCpmProtExcdSapEcmStarted_Type = TimeStamp
_TmnxCpmProtExcdSapEcmStarted_Object = MibTableColumn
tmnxCpmProtExcdSapEcmStarted = _TmnxCpmProtExcdSapEcmStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1, 5),
    _TmnxCpmProtExcdSapEcmStarted_Type()
)
tmnxCpmProtExcdSapEcmStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmStarted.setStatus("current")
_TmnxCpmProtExcdSapEcmTime_Type = TimeStamp
_TmnxCpmProtExcdSapEcmTime_Object = MibTableColumn
tmnxCpmProtExcdSapEcmTime = _TmnxCpmProtExcdSapEcmTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 39, 1, 6),
    _TmnxCpmProtExcdSapEcmTime_Type()
)
tmnxCpmProtExcdSapEcmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcmTime.setStatus("current")


class _TmnxCpmVprnNwExceptions_Type(TruthValue):
    """Custom type tmnxCpmVprnNwExceptions based on TruthValue"""
    defaultValue = 2


_TmnxCpmVprnNwExceptions_Type.__name__ = "TruthValue"
_TmnxCpmVprnNwExceptions_Object = MibScalar
tmnxCpmVprnNwExceptions = _TmnxCpmVprnNwExceptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 40),
    _TmnxCpmVprnNwExceptions_Type()
)
tmnxCpmVprnNwExceptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmVprnNwExceptions.setStatus("current")


class _TmnxCpmNumVprnNwExceptions_Type(Unsigned32):
    """Custom type tmnxCpmNumVprnNwExceptions based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxCpmNumVprnNwExceptions_Type.__name__ = "Unsigned32"
_TmnxCpmNumVprnNwExceptions_Object = MibScalar
tmnxCpmNumVprnNwExceptions = _TmnxCpmNumVprnNwExceptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 41),
    _TmnxCpmNumVprnNwExceptions_Type()
)
tmnxCpmNumVprnNwExceptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmNumVprnNwExceptions.setStatus("current")


class _TmnxCpmVprnNwExceptionsTime_Type(Unsigned32):
    """Custom type tmnxCpmVprnNwExceptionsTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxCpmVprnNwExceptionsTime_Type.__name__ = "Unsigned32"
_TmnxCpmVprnNwExceptionsTime_Object = MibScalar
tmnxCpmVprnNwExceptionsTime = _TmnxCpmVprnNwExceptionsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 42),
    _TmnxCpmVprnNwExceptionsTime_Type()
)
tmnxCpmVprnNwExceptionsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmVprnNwExceptionsTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxCpmVprnNwExceptionsTime.setUnits("seconds")
_TmnxCpmProtExcdSapIpTableLastChg_Type = TimeStamp
_TmnxCpmProtExcdSapIpTableLastChg_Object = MibScalar
tmnxCpmProtExcdSapIpTableLastChg = _TmnxCpmProtExcdSapIpTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 43),
    _TmnxCpmProtExcdSapIpTableLastChg_Type()
)
tmnxCpmProtExcdSapIpTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpTableLastChg.setStatus("current")
_TmnxCpmProtExcdSapIpTable_Object = MibTable
tmnxCpmProtExcdSapIpTable = _TmnxCpmProtExcdSapIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44)
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpTable.setStatus("current")
_TmnxCpmProtExcdSapIpEntry_Object = MibTableRow
tmnxCpmProtExcdSapIpEntry = _TmnxCpmProtExcdSapIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44, 1)
)
tmnxCpmProtExcdSapIpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpAddrType"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpEntry.setStatus("current")
_TmnxCpmProtExcdSapIpAddrType_Type = InetAddressType
_TmnxCpmProtExcdSapIpAddrType_Object = MibTableColumn
tmnxCpmProtExcdSapIpAddrType = _TmnxCpmProtExcdSapIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44, 1, 1),
    _TmnxCpmProtExcdSapIpAddrType_Type()
)
tmnxCpmProtExcdSapIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpAddrType.setStatus("current")


class _TmnxCpmProtExcdSapIpAddr_Type(InetAddress):
    """Custom type tmnxCpmProtExcdSapIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCpmProtExcdSapIpAddr_Type.__name__ = "InetAddress"
_TmnxCpmProtExcdSapIpAddr_Object = MibTableColumn
tmnxCpmProtExcdSapIpAddr = _TmnxCpmProtExcdSapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44, 1, 2),
    _TmnxCpmProtExcdSapIpAddr_Type()
)
tmnxCpmProtExcdSapIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpAddr.setStatus("current")
_TmnxCpmProtExcdSapIpPeriods_Type = Counter32
_TmnxCpmProtExcdSapIpPeriods_Object = MibTableColumn
tmnxCpmProtExcdSapIpPeriods = _TmnxCpmProtExcdSapIpPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44, 1, 3),
    _TmnxCpmProtExcdSapIpPeriods_Type()
)
tmnxCpmProtExcdSapIpPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpPeriods.setStatus("current")
_TmnxCpmProtExcdSapIpStarted_Type = TimeStamp
_TmnxCpmProtExcdSapIpStarted_Object = MibTableColumn
tmnxCpmProtExcdSapIpStarted = _TmnxCpmProtExcdSapIpStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44, 1, 4),
    _TmnxCpmProtExcdSapIpStarted_Type()
)
tmnxCpmProtExcdSapIpStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpStarted.setStatus("current")
_TmnxCpmProtExcdSapIpTime_Type = TimeStamp
_TmnxCpmProtExcdSapIpTime_Object = MibTableColumn
tmnxCpmProtExcdSapIpTime = _TmnxCpmProtExcdSapIpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 44, 1, 5),
    _TmnxCpmProtExcdSapIpTime_Type()
)
tmnxCpmProtExcdSapIpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpTime.setStatus("current")
_TmnxDCpuProtPolicyTblLstChg_Type = TimeStamp
_TmnxDCpuProtPolicyTblLstChg_Object = MibScalar
tmnxDCpuProtPolicyTblLstChg = _TmnxDCpuProtPolicyTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 45),
    _TmnxDCpuProtPolicyTblLstChg_Type()
)
tmnxDCpuProtPolicyTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyTblLstChg.setStatus("current")
_TmnxDCpuProtPolicyTable_Object = MibTable
tmnxDCpuProtPolicyTable = _TmnxDCpuProtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 46)
)
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyTable.setStatus("current")
_TmnxDCpuProtPolicyEntry_Object = MibTableRow
tmnxDCpuProtPolicyEntry = _TmnxDCpuProtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 46, 1)
)
tmnxDCpuProtPolicyEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyName"),
)
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyEntry.setStatus("current")
_TmnxDCpuProtPolicyName_Type = TNamedItem
_TmnxDCpuProtPolicyName_Object = MibTableColumn
tmnxDCpuProtPolicyName = _TmnxDCpuProtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 46, 1, 1),
    _TmnxDCpuProtPolicyName_Type()
)
tmnxDCpuProtPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyName.setStatus("current")
_TmnxDCpuProtPolicyRowStatus_Type = RowStatus
_TmnxDCpuProtPolicyRowStatus_Object = MibTableColumn
tmnxDCpuProtPolicyRowStatus = _TmnxDCpuProtPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 46, 1, 2),
    _TmnxDCpuProtPolicyRowStatus_Type()
)
tmnxDCpuProtPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyRowStatus.setStatus("current")
_TmnxDCpuProtPolicyLastMdfy_Type = TimeStamp
_TmnxDCpuProtPolicyLastMdfy_Object = MibTableColumn
tmnxDCpuProtPolicyLastMdfy = _TmnxDCpuProtPolicyLastMdfy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 46, 1, 3),
    _TmnxDCpuProtPolicyLastMdfy_Type()
)
tmnxDCpuProtPolicyLastMdfy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyLastMdfy.setStatus("current")


class _TmnxDCpuProtPolicyDescr_Type(TItemDescription):
    """Custom type tmnxDCpuProtPolicyDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxDCpuProtPolicyDescr_Type.__name__ = "TItemDescription"
_TmnxDCpuProtPolicyDescr_Object = MibTableColumn
tmnxDCpuProtPolicyDescr = _TmnxDCpuProtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 46, 1, 4),
    _TmnxDCpuProtPolicyDescr_Type()
)
tmnxDCpuProtPolicyDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtPolicyDescr.setStatus("current")
_TmnxDCpuProtStaticPlcrTblLstChg_Type = TimeStamp
_TmnxDCpuProtStaticPlcrTblLstChg_Object = MibScalar
tmnxDCpuProtStaticPlcrTblLstChg = _TmnxDCpuProtStaticPlcrTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 47),
    _TmnxDCpuProtStaticPlcrTblLstChg_Type()
)
tmnxDCpuProtStaticPlcrTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrTblLstChg.setStatus("current")
_TmnxDCpuProtStaticPlcrTable_Object = MibTable
tmnxDCpuProtStaticPlcrTable = _TmnxDCpuProtStaticPlcrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48)
)
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrTable.setStatus("current")
_TmnxDCpuProtStaticPlcrEntry_Object = MibTableRow
tmnxDCpuProtStaticPlcrEntry = _TmnxDCpuProtStaticPlcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1)
)
tmnxDCpuProtStaticPlcrEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrName"),
)
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrEntry.setStatus("current")
_TmnxDCpuProtStaticPlcrName_Type = TNamedItem
_TmnxDCpuProtStaticPlcrName_Object = MibTableColumn
tmnxDCpuProtStaticPlcrName = _TmnxDCpuProtStaticPlcrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 1),
    _TmnxDCpuProtStaticPlcrName_Type()
)
tmnxDCpuProtStaticPlcrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrName.setStatus("current")
_TmnxDCpuProtStaticPlcrRowStatus_Type = RowStatus
_TmnxDCpuProtStaticPlcrRowStatus_Object = MibTableColumn
tmnxDCpuProtStaticPlcrRowStatus = _TmnxDCpuProtStaticPlcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 2),
    _TmnxDCpuProtStaticPlcrRowStatus_Type()
)
tmnxDCpuProtStaticPlcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrRowStatus.setStatus("current")
_TmnxDCpuProtStaticPlcrLastMdfy_Type = TimeStamp
_TmnxDCpuProtStaticPlcrLastMdfy_Object = MibTableColumn
tmnxDCpuProtStaticPlcrLastMdfy = _TmnxDCpuProtStaticPlcrLastMdfy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 3),
    _TmnxDCpuProtStaticPlcrLastMdfy_Type()
)
tmnxDCpuProtStaticPlcrLastMdfy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrLastMdfy.setStatus("current")


class _TmnxDCpuProtStaticPlcrDescr_Type(TItemDescription):
    """Custom type tmnxDCpuProtStaticPlcrDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxDCpuProtStaticPlcrDescr_Type.__name__ = "TItemDescription"
_TmnxDCpuProtStaticPlcrDescr_Object = MibTableColumn
tmnxDCpuProtStaticPlcrDescr = _TmnxDCpuProtStaticPlcrDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 4),
    _TmnxDCpuProtStaticPlcrDescr_Type()
)
tmnxDCpuProtStaticPlcrDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrDescr.setStatus("current")


class _TmnxDCpuProtStaticPlcrPackets_Type(TmnxDistCpuProtPacketRateLimit):
    """Custom type tmnxDCpuProtStaticPlcrPackets based on TmnxDistCpuProtPacketRateLimit"""
    defaultValue = -1


_TmnxDCpuProtStaticPlcrPackets_Type.__name__ = "TmnxDistCpuProtPacketRateLimit"
_TmnxDCpuProtStaticPlcrPackets_Object = MibTableColumn
tmnxDCpuProtStaticPlcrPackets = _TmnxDCpuProtStaticPlcrPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 5),
    _TmnxDCpuProtStaticPlcrPackets_Type()
)
tmnxDCpuProtStaticPlcrPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrPackets.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrPackets.setUnits("packets per interval")


class _TmnxDCpuProtStaticPlcrWithin_Type(Unsigned32):
    """Custom type tmnxDCpuProtStaticPlcrWithin based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TmnxDCpuProtStaticPlcrWithin_Type.__name__ = "Unsigned32"
_TmnxDCpuProtStaticPlcrWithin_Object = MibTableColumn
tmnxDCpuProtStaticPlcrWithin = _TmnxDCpuProtStaticPlcrWithin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 6),
    _TmnxDCpuProtStaticPlcrWithin_Type()
)
tmnxDCpuProtStaticPlcrWithin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrWithin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrWithin.setUnits("seconds")


class _TmnxDCpuProtStaticPlcrInitDelay_Type(Unsigned32):
    """Custom type tmnxDCpuProtStaticPlcrInitDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxDCpuProtStaticPlcrInitDelay_Type.__name__ = "Unsigned32"
_TmnxDCpuProtStaticPlcrInitDelay_Object = MibTableColumn
tmnxDCpuProtStaticPlcrInitDelay = _TmnxDCpuProtStaticPlcrInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 7),
    _TmnxDCpuProtStaticPlcrInitDelay_Type()
)
tmnxDCpuProtStaticPlcrInitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrInitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrInitDelay.setUnits("packets")


class _TmnxDCpuProtStaticPlcrKbps_Type(TmnxDistCpuProtRate):
    """Custom type tmnxDCpuProtStaticPlcrKbps based on TmnxDistCpuProtRate"""
    defaultValue = -1


_TmnxDCpuProtStaticPlcrKbps_Type.__name__ = "TmnxDistCpuProtRate"
_TmnxDCpuProtStaticPlcrKbps_Object = MibTableColumn
tmnxDCpuProtStaticPlcrKbps = _TmnxDCpuProtStaticPlcrKbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 8),
    _TmnxDCpuProtStaticPlcrKbps_Type()
)
tmnxDCpuProtStaticPlcrKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrKbps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrKbps.setUnits("kilobits-per-second")


class _TmnxDCpuProtStaticPlcrMbs_Type(TmnxDistCpuProtBurstSize):
    """Custom type tmnxDCpuProtStaticPlcrMbs based on TmnxDistCpuProtBurstSize"""
    defaultValue = -1


_TmnxDCpuProtStaticPlcrMbs_Type.__name__ = "TmnxDistCpuProtBurstSize"
_TmnxDCpuProtStaticPlcrMbs_Object = MibTableColumn
tmnxDCpuProtStaticPlcrMbs = _TmnxDCpuProtStaticPlcrMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 9),
    _TmnxDCpuProtStaticPlcrMbs_Type()
)
tmnxDCpuProtStaticPlcrMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrMbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrMbs.setUnits("bytes")


class _TmnxDCpuProtStaticPlcrExdActn_Type(TmnxDistCpuProtAction):
    """Custom type tmnxDCpuProtStaticPlcrExdActn based on TmnxDistCpuProtAction"""
    defaultValue = 3


_TmnxDCpuProtStaticPlcrExdActn_Type.__name__ = "TmnxDistCpuProtAction"
_TmnxDCpuProtStaticPlcrExdActn_Object = MibTableColumn
tmnxDCpuProtStaticPlcrExdActn = _TmnxDCpuProtStaticPlcrExdActn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 10),
    _TmnxDCpuProtStaticPlcrExdActn_Type()
)
tmnxDCpuProtStaticPlcrExdActn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrExdActn.setStatus("current")


class _TmnxDCpuProtStaticPlcrExdHold_Type(TmnxDistCpuProtActionDuration):
    """Custom type tmnxDCpuProtStaticPlcrExdHold based on TmnxDistCpuProtActionDuration"""
    defaultValue = 0


_TmnxDCpuProtStaticPlcrExdHold_Type.__name__ = "TmnxDistCpuProtActionDuration"
_TmnxDCpuProtStaticPlcrExdHold_Object = MibTableColumn
tmnxDCpuProtStaticPlcrExdHold = _TmnxDCpuProtStaticPlcrExdHold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 11),
    _TmnxDCpuProtStaticPlcrExdHold_Type()
)
tmnxDCpuProtStaticPlcrExdHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrExdHold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrExdHold.setUnits("seconds")


class _TmnxDCpuProtStaticPlcrRateType_Type(TmnxDistCpuProtRateType):
    """Custom type tmnxDCpuProtStaticPlcrRateType based on TmnxDistCpuProtRateType"""
    defaultValue = 1


_TmnxDCpuProtStaticPlcrRateType_Type.__name__ = "TmnxDistCpuProtRateType"
_TmnxDCpuProtStaticPlcrRateType_Object = MibTableColumn
tmnxDCpuProtStaticPlcrRateType = _TmnxDCpuProtStaticPlcrRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 12),
    _TmnxDCpuProtStaticPlcrRateType_Type()
)
tmnxDCpuProtStaticPlcrRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrRateType.setStatus("current")


class _TmnxDCpuProtStaticPlcrDectnTime_Type(Unsigned32):
    """Custom type tmnxDCpuProtStaticPlcrDectnTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128000),
    )


_TmnxDCpuProtStaticPlcrDectnTime_Type.__name__ = "Unsigned32"
_TmnxDCpuProtStaticPlcrDectnTime_Object = MibTableColumn
tmnxDCpuProtStaticPlcrDectnTime = _TmnxDCpuProtStaticPlcrDectnTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 13),
    _TmnxDCpuProtStaticPlcrDectnTime_Type()
)
tmnxDCpuProtStaticPlcrDectnTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrDectnTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrDectnTime.setUnits("seconds")


class _TmnxDCpuProtStaticPlcrLogEvent_Type(TmnxDistCpuProtLogEventType):
    """Custom type tmnxDCpuProtStaticPlcrLogEvent based on TmnxDistCpuProtLogEventType"""
    defaultValue = 1


_TmnxDCpuProtStaticPlcrLogEvent_Type.__name__ = "TmnxDistCpuProtLogEventType"
_TmnxDCpuProtStaticPlcrLogEvent_Object = MibTableColumn
tmnxDCpuProtStaticPlcrLogEvent = _TmnxDCpuProtStaticPlcrLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 48, 1, 14),
    _TmnxDCpuProtStaticPlcrLogEvent_Type()
)
tmnxDCpuProtStaticPlcrLogEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtStaticPlcrLogEvent.setStatus("current")
_TmnxDCpuProtLocMonPlcrTblLstChg_Type = TimeStamp
_TmnxDCpuProtLocMonPlcrTblLstChg_Object = MibScalar
tmnxDCpuProtLocMonPlcrTblLstChg = _TmnxDCpuProtLocMonPlcrTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 49),
    _TmnxDCpuProtLocMonPlcrTblLstChg_Type()
)
tmnxDCpuProtLocMonPlcrTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrTblLstChg.setStatus("current")
_TmnxDCpuProtLocMonPlcrTable_Object = MibTable
tmnxDCpuProtLocMonPlcrTable = _TmnxDCpuProtLocMonPlcrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50)
)
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrTable.setStatus("current")
_TmnxDCpuProtLocMonPlcrEntry_Object = MibTableRow
tmnxDCpuProtLocMonPlcrEntry = _TmnxDCpuProtLocMonPlcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1)
)
tmnxDCpuProtLocMonPlcrEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrName"),
)
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrEntry.setStatus("current")
_TmnxDCpuProtLocMonPlcrName_Type = TNamedItem
_TmnxDCpuProtLocMonPlcrName_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrName = _TmnxDCpuProtLocMonPlcrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 1),
    _TmnxDCpuProtLocMonPlcrName_Type()
)
tmnxDCpuProtLocMonPlcrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrName.setStatus("current")
_TmnxDCpuProtLocMonPlcrRowStatus_Type = RowStatus
_TmnxDCpuProtLocMonPlcrRowStatus_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrRowStatus = _TmnxDCpuProtLocMonPlcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 2),
    _TmnxDCpuProtLocMonPlcrRowStatus_Type()
)
tmnxDCpuProtLocMonPlcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrRowStatus.setStatus("current")
_TmnxDCpuProtLocMonPlcrLastMdfy_Type = TimeStamp
_TmnxDCpuProtLocMonPlcrLastMdfy_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrLastMdfy = _TmnxDCpuProtLocMonPlcrLastMdfy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 3),
    _TmnxDCpuProtLocMonPlcrLastMdfy_Type()
)
tmnxDCpuProtLocMonPlcrLastMdfy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrLastMdfy.setStatus("current")


class _TmnxDCpuProtLocMonPlcrDescr_Type(TItemDescription):
    """Custom type tmnxDCpuProtLocMonPlcrDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxDCpuProtLocMonPlcrDescr_Type.__name__ = "TItemDescription"
_TmnxDCpuProtLocMonPlcrDescr_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrDescr = _TmnxDCpuProtLocMonPlcrDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 4),
    _TmnxDCpuProtLocMonPlcrDescr_Type()
)
tmnxDCpuProtLocMonPlcrDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrDescr.setStatus("current")


class _TmnxDCpuProtLocMonPlcrPackets_Type(TmnxDistCpuProtPacketRateLimit):
    """Custom type tmnxDCpuProtLocMonPlcrPackets based on TmnxDistCpuProtPacketRateLimit"""
    defaultValue = -1


_TmnxDCpuProtLocMonPlcrPackets_Type.__name__ = "TmnxDistCpuProtPacketRateLimit"
_TmnxDCpuProtLocMonPlcrPackets_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrPackets = _TmnxDCpuProtLocMonPlcrPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 5),
    _TmnxDCpuProtLocMonPlcrPackets_Type()
)
tmnxDCpuProtLocMonPlcrPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrPackets.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrPackets.setUnits("packets per interval")


class _TmnxDCpuProtLocMonPlcrWithin_Type(Unsigned32):
    """Custom type tmnxDCpuProtLocMonPlcrWithin based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TmnxDCpuProtLocMonPlcrWithin_Type.__name__ = "Unsigned32"
_TmnxDCpuProtLocMonPlcrWithin_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrWithin = _TmnxDCpuProtLocMonPlcrWithin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 6),
    _TmnxDCpuProtLocMonPlcrWithin_Type()
)
tmnxDCpuProtLocMonPlcrWithin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrWithin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrWithin.setUnits("seconds")


class _TmnxDCpuProtLocMonPlcrInitDelay_Type(Unsigned32):
    """Custom type tmnxDCpuProtLocMonPlcrInitDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxDCpuProtLocMonPlcrInitDelay_Type.__name__ = "Unsigned32"
_TmnxDCpuProtLocMonPlcrInitDelay_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrInitDelay = _TmnxDCpuProtLocMonPlcrInitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 7),
    _TmnxDCpuProtLocMonPlcrInitDelay_Type()
)
tmnxDCpuProtLocMonPlcrInitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrInitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrInitDelay.setUnits("packets")


class _TmnxDCpuProtLocMonPlcrKbps_Type(TmnxDistCpuProtRate):
    """Custom type tmnxDCpuProtLocMonPlcrKbps based on TmnxDistCpuProtRate"""
    defaultValue = -1


_TmnxDCpuProtLocMonPlcrKbps_Type.__name__ = "TmnxDistCpuProtRate"
_TmnxDCpuProtLocMonPlcrKbps_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrKbps = _TmnxDCpuProtLocMonPlcrKbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 8),
    _TmnxDCpuProtLocMonPlcrKbps_Type()
)
tmnxDCpuProtLocMonPlcrKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrKbps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrKbps.setUnits("kilobits-per-second")


class _TmnxDCpuProtLocMonPlcrMbs_Type(TmnxDistCpuProtBurstSize):
    """Custom type tmnxDCpuProtLocMonPlcrMbs based on TmnxDistCpuProtBurstSize"""
    defaultValue = -1


_TmnxDCpuProtLocMonPlcrMbs_Type.__name__ = "TmnxDistCpuProtBurstSize"
_TmnxDCpuProtLocMonPlcrMbs_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrMbs = _TmnxDCpuProtLocMonPlcrMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 9),
    _TmnxDCpuProtLocMonPlcrMbs_Type()
)
tmnxDCpuProtLocMonPlcrMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrMbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrMbs.setUnits("bytes")


class _TmnxDCpuProtLocMonPlcrExcdActn_Type(TmnxDistCpuProtAction):
    """Custom type tmnxDCpuProtLocMonPlcrExcdActn based on TmnxDistCpuProtAction"""
    defaultValue = 3


_TmnxDCpuProtLocMonPlcrExcdActn_Type.__name__ = "TmnxDistCpuProtAction"
_TmnxDCpuProtLocMonPlcrExcdActn_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrExcdActn = _TmnxDCpuProtLocMonPlcrExcdActn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 10),
    _TmnxDCpuProtLocMonPlcrExcdActn_Type()
)
tmnxDCpuProtLocMonPlcrExcdActn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrExcdActn.setStatus("current")


class _TmnxDCpuProtLocMonPlcrRateType_Type(TmnxDistCpuProtRateType):
    """Custom type tmnxDCpuProtLocMonPlcrRateType based on TmnxDistCpuProtRateType"""
    defaultValue = 1


_TmnxDCpuProtLocMonPlcrRateType_Type.__name__ = "TmnxDistCpuProtRateType"
_TmnxDCpuProtLocMonPlcrRateType_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrRateType = _TmnxDCpuProtLocMonPlcrRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 11),
    _TmnxDCpuProtLocMonPlcrRateType_Type()
)
tmnxDCpuProtLocMonPlcrRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrRateType.setStatus("current")


class _TmnxDCpuProtLocMonPlcrLogEvent_Type(TmnxDistCpuProtLogEventType):
    """Custom type tmnxDCpuProtLocMonPlcrLogEvent based on TmnxDistCpuProtLogEventType"""
    defaultValue = 1


_TmnxDCpuProtLocMonPlcrLogEvent_Type.__name__ = "TmnxDistCpuProtLogEventType"
_TmnxDCpuProtLocMonPlcrLogEvent_Object = MibTableColumn
tmnxDCpuProtLocMonPlcrLogEvent = _TmnxDCpuProtLocMonPlcrLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 50, 1, 12),
    _TmnxDCpuProtLocMonPlcrLogEvent_Type()
)
tmnxDCpuProtLocMonPlcrLogEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtLocMonPlcrLogEvent.setStatus("current")
_TmnxDCpuProtProtocolTblLstChg_Type = TimeStamp
_TmnxDCpuProtProtocolTblLstChg_Object = MibScalar
tmnxDCpuProtProtocolTblLstChg = _TmnxDCpuProtProtocolTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 51),
    _TmnxDCpuProtProtocolTblLstChg_Type()
)
tmnxDCpuProtProtocolTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolTblLstChg.setStatus("current")
_TmnxDCpuProtProtocolTable_Object = MibTable
tmnxDCpuProtProtocolTable = _TmnxDCpuProtProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52)
)
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolTable.setStatus("current")
_TmnxDCpuProtProtocolEntry_Object = MibTableRow
tmnxDCpuProtProtocolEntry = _TmnxDCpuProtProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1)
)
tmnxDCpuProtProtocolEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocol"),
)
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolEntry.setStatus("current")
_TmnxDCpuProtProtocol_Type = TmnxDistCpuProtProtocolId
_TmnxDCpuProtProtocol_Object = MibTableColumn
tmnxDCpuProtProtocol = _TmnxDCpuProtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 1),
    _TmnxDCpuProtProtocol_Type()
)
tmnxDCpuProtProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocol.setStatus("current")
_TmnxDCpuProtProtocolRowStatus_Type = RowStatus
_TmnxDCpuProtProtocolRowStatus_Object = MibTableColumn
tmnxDCpuProtProtocolRowStatus = _TmnxDCpuProtProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 2),
    _TmnxDCpuProtProtocolRowStatus_Type()
)
tmnxDCpuProtProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolRowStatus.setStatus("current")
_TmnxDCpuProtProtocolLastMdfy_Type = TimeStamp
_TmnxDCpuProtProtocolLastMdfy_Object = MibTableColumn
tmnxDCpuProtProtocolLastMdfy = _TmnxDCpuProtProtocolLastMdfy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 3),
    _TmnxDCpuProtProtocolLastMdfy_Type()
)
tmnxDCpuProtProtocolLastMdfy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolLastMdfy.setStatus("current")


class _TmnxDCpuProtProtocolEnforce_Type(TmnxDistCpuProtEnforceType):
    """Custom type tmnxDCpuProtProtocolEnforce based on TmnxDistCpuProtEnforceType"""
    defaultValue = 2


_TmnxDCpuProtProtocolEnforce_Type.__name__ = "TmnxDistCpuProtEnforceType"
_TmnxDCpuProtProtocolEnforce_Object = MibTableColumn
tmnxDCpuProtProtocolEnforce = _TmnxDCpuProtProtocolEnforce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 4),
    _TmnxDCpuProtProtocolEnforce_Type()
)
tmnxDCpuProtProtocolEnforce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolEnforce.setStatus("current")


class _TmnxDCpuProtProtocolEnfrcePolNme_Type(TNamedItem):
    """Custom type tmnxDCpuProtProtocolEnfrcePolNme based on TNamedItem"""
    defaultValue = OctetString("local-mon-bypass")


_TmnxDCpuProtProtocolEnfrcePolNme_Type.__name__ = "TNamedItem"
_TmnxDCpuProtProtocolEnfrcePolNme_Object = MibTableColumn
tmnxDCpuProtProtocolEnfrcePolNme = _TmnxDCpuProtProtocolEnfrcePolNme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 5),
    _TmnxDCpuProtProtocolEnfrcePolNme_Type()
)
tmnxDCpuProtProtocolEnfrcePolNme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolEnfrcePolNme.setStatus("current")


class _TmnxDCpuProtProtocolDynPackets_Type(TmnxDistCpuProtPacketRateLimit):
    """Custom type tmnxDCpuProtProtocolDynPackets based on TmnxDistCpuProtPacketRateLimit"""
    defaultValue = -1


_TmnxDCpuProtProtocolDynPackets_Type.__name__ = "TmnxDistCpuProtPacketRateLimit"
_TmnxDCpuProtProtocolDynPackets_Object = MibTableColumn
tmnxDCpuProtProtocolDynPackets = _TmnxDCpuProtProtocolDynPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 6),
    _TmnxDCpuProtProtocolDynPackets_Type()
)
tmnxDCpuProtProtocolDynPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynPackets.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynPackets.setUnits("packets per interval")


class _TmnxDCpuProtProtocolDynWithin_Type(Unsigned32):
    """Custom type tmnxDCpuProtProtocolDynWithin based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TmnxDCpuProtProtocolDynWithin_Type.__name__ = "Unsigned32"
_TmnxDCpuProtProtocolDynWithin_Object = MibTableColumn
tmnxDCpuProtProtocolDynWithin = _TmnxDCpuProtProtocolDynWithin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 7),
    _TmnxDCpuProtProtocolDynWithin_Type()
)
tmnxDCpuProtProtocolDynWithin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynWithin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynWithin.setUnits("seconds")


class _TmnxDCpuProtProtocolDynInitDly_Type(Unsigned32):
    """Custom type tmnxDCpuProtProtocolDynInitDly based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_TmnxDCpuProtProtocolDynInitDly_Type.__name__ = "Unsigned32"
_TmnxDCpuProtProtocolDynInitDly_Object = MibTableColumn
tmnxDCpuProtProtocolDynInitDly = _TmnxDCpuProtProtocolDynInitDly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 8),
    _TmnxDCpuProtProtocolDynInitDly_Type()
)
tmnxDCpuProtProtocolDynInitDly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynInitDly.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynInitDly.setUnits("packets")


class _TmnxDCpuProtProtocolDynKbps_Type(TmnxDistCpuProtRate):
    """Custom type tmnxDCpuProtProtocolDynKbps based on TmnxDistCpuProtRate"""
    defaultValue = -1


_TmnxDCpuProtProtocolDynKbps_Type.__name__ = "TmnxDistCpuProtRate"
_TmnxDCpuProtProtocolDynKbps_Object = MibTableColumn
tmnxDCpuProtProtocolDynKbps = _TmnxDCpuProtProtocolDynKbps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 9),
    _TmnxDCpuProtProtocolDynKbps_Type()
)
tmnxDCpuProtProtocolDynKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynKbps.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynKbps.setUnits("kilobits-per-second")


class _TmnxDCpuProtProtocolDynMbs_Type(TmnxDistCpuProtBurstSize):
    """Custom type tmnxDCpuProtProtocolDynMbs based on TmnxDistCpuProtBurstSize"""
    defaultValue = -1


_TmnxDCpuProtProtocolDynMbs_Type.__name__ = "TmnxDistCpuProtBurstSize"
_TmnxDCpuProtProtocolDynMbs_Object = MibTableColumn
tmnxDCpuProtProtocolDynMbs = _TmnxDCpuProtProtocolDynMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 10),
    _TmnxDCpuProtProtocolDynMbs_Type()
)
tmnxDCpuProtProtocolDynMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynMbs.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynMbs.setUnits("bytes")


class _TmnxDCpuProtProtocolDynDectnTime_Type(Unsigned32):
    """Custom type tmnxDCpuProtProtocolDynDectnTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128000),
    )


_TmnxDCpuProtProtocolDynDectnTime_Type.__name__ = "Unsigned32"
_TmnxDCpuProtProtocolDynDectnTime_Object = MibTableColumn
tmnxDCpuProtProtocolDynDectnTime = _TmnxDCpuProtProtocolDynDectnTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 11),
    _TmnxDCpuProtProtocolDynDectnTime_Type()
)
tmnxDCpuProtProtocolDynDectnTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynDectnTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynDectnTime.setUnits("seconds")


class _TmnxDCpuProtProtocolDynExdActn_Type(TmnxDistCpuProtAction):
    """Custom type tmnxDCpuProtProtocolDynExdActn based on TmnxDistCpuProtAction"""
    defaultValue = 3


_TmnxDCpuProtProtocolDynExdActn_Type.__name__ = "TmnxDistCpuProtAction"
_TmnxDCpuProtProtocolDynExdActn_Object = MibTableColumn
tmnxDCpuProtProtocolDynExdActn = _TmnxDCpuProtProtocolDynExdActn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 12),
    _TmnxDCpuProtProtocolDynExdActn_Type()
)
tmnxDCpuProtProtocolDynExdActn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynExdActn.setStatus("current")


class _TmnxDCpuProtProtocolDynExdHold_Type(TmnxDistCpuProtActionDuration):
    """Custom type tmnxDCpuProtProtocolDynExdHold based on TmnxDistCpuProtActionDuration"""
    defaultValue = 0


_TmnxDCpuProtProtocolDynExdHold_Type.__name__ = "TmnxDistCpuProtActionDuration"
_TmnxDCpuProtProtocolDynExdHold_Object = MibTableColumn
tmnxDCpuProtProtocolDynExdHold = _TmnxDCpuProtProtocolDynExdHold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 13),
    _TmnxDCpuProtProtocolDynExdHold_Type()
)
tmnxDCpuProtProtocolDynExdHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynExdHold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynExdHold.setUnits("seconds")


class _TmnxDCpuProtProtocolDynRateType_Type(TmnxDistCpuProtRateType):
    """Custom type tmnxDCpuProtProtocolDynRateType based on TmnxDistCpuProtRateType"""
    defaultValue = 1


_TmnxDCpuProtProtocolDynRateType_Type.__name__ = "TmnxDistCpuProtRateType"
_TmnxDCpuProtProtocolDynRateType_Object = MibTableColumn
tmnxDCpuProtProtocolDynRateType = _TmnxDCpuProtProtocolDynRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 14),
    _TmnxDCpuProtProtocolDynRateType_Type()
)
tmnxDCpuProtProtocolDynRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynRateType.setStatus("current")


class _TmnxDCpuProtProtocolDynLogEvent_Type(TmnxDistCpuProtLogEventType):
    """Custom type tmnxDCpuProtProtocolDynLogEvent based on TmnxDistCpuProtLogEventType"""
    defaultValue = 1


_TmnxDCpuProtProtocolDynLogEvent_Type.__name__ = "TmnxDistCpuProtLogEventType"
_TmnxDCpuProtProtocolDynLogEvent_Object = MibTableColumn
tmnxDCpuProtProtocolDynLogEvent = _TmnxDCpuProtProtocolDynLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 52, 1, 15),
    _TmnxDCpuProtProtocolDynLogEvent_Type()
)
tmnxDCpuProtProtocolDynLogEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDCpuProtProtocolDynLogEvent.setStatus("current")


class _TmnxCpmProtBlockPIMTunneled_Type(TruthValue):
    """Custom type tmnxCpmProtBlockPIMTunneled based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtBlockPIMTunneled_Type.__name__ = "TruthValue"
_TmnxCpmProtBlockPIMTunneled_Object = MibScalar
tmnxCpmProtBlockPIMTunneled = _TmnxCpmProtBlockPIMTunneled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 53),
    _TmnxCpmProtBlockPIMTunneled_Type()
)
tmnxCpmProtBlockPIMTunneled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmProtBlockPIMTunneled.setStatus("current")


class _TmnxCpmProtPortRateActionLowPrio_Type(TruthValue):
    """Custom type tmnxCpmProtPortRateActionLowPrio based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtPortRateActionLowPrio_Type.__name__ = "TruthValue"
_TmnxCpmProtPortRateActionLowPrio_Object = MibScalar
tmnxCpmProtPortRateActionLowPrio = _TmnxCpmProtPortRateActionLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 54),
    _TmnxCpmProtPortRateActionLowPrio_Type()
)
tmnxCpmProtPortRateActionLowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxCpmProtPortRateActionLowPrio.setStatus("current")


class _TmnxCpmProtIPSrcMonDhcp_Type(TruthValue):
    """Custom type tmnxCpmProtIPSrcMonDhcp based on TruthValue"""
    defaultValue = 1


_TmnxCpmProtIPSrcMonDhcp_Type.__name__ = "TruthValue"
_TmnxCpmProtIPSrcMonDhcp_Object = MibScalar
tmnxCpmProtIPSrcMonDhcp = _TmnxCpmProtIPSrcMonDhcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 55),
    _TmnxCpmProtIPSrcMonDhcp_Type()
)
tmnxCpmProtIPSrcMonDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtIPSrcMonDhcp.setStatus("current")


class _TmnxCpmProtIPSrcMonGtp_Type(TruthValue):
    """Custom type tmnxCpmProtIPSrcMonGtp based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtIPSrcMonGtp_Type.__name__ = "TruthValue"
_TmnxCpmProtIPSrcMonGtp_Object = MibScalar
tmnxCpmProtIPSrcMonGtp = _TmnxCpmProtIPSrcMonGtp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 56),
    _TmnxCpmProtIPSrcMonGtp_Type()
)
tmnxCpmProtIPSrcMonGtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtIPSrcMonGtp.setStatus("current")


class _TmnxCpmProtIPSrcMonIcmp_Type(TruthValue):
    """Custom type tmnxCpmProtIPSrcMonIcmp based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtIPSrcMonIcmp_Type.__name__ = "TruthValue"
_TmnxCpmProtIPSrcMonIcmp_Object = MibScalar
tmnxCpmProtIPSrcMonIcmp = _TmnxCpmProtIPSrcMonIcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 57),
    _TmnxCpmProtIPSrcMonIcmp_Type()
)
tmnxCpmProtIPSrcMonIcmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtIPSrcMonIcmp.setStatus("current")


class _TmnxCpmProtIPSrcMonIgmp_Type(TruthValue):
    """Custom type tmnxCpmProtIPSrcMonIgmp based on TruthValue"""
    defaultValue = 2


_TmnxCpmProtIPSrcMonIgmp_Type.__name__ = "TruthValue"
_TmnxCpmProtIPSrcMonIgmp_Object = MibScalar
tmnxCpmProtIPSrcMonIgmp = _TmnxCpmProtIPSrcMonIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 58),
    _TmnxCpmProtIPSrcMonIgmp_Type()
)
tmnxCpmProtIPSrcMonIgmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxCpmProtIPSrcMonIgmp.setStatus("current")
_TCpmProtOutProfViolIfTable_Object = MibTable
tCpmProtOutProfViolIfTable = _TCpmProtOutProfViolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 61)
)
if mibBuilder.loadTexts:
    tCpmProtOutProfViolIfTable.setStatus("current")
_TCpmProtOutProfViolIfEntry_Object = MibTableRow
tCpmProtOutProfViolIfEntry = _TCpmProtOutProfViolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 61, 1)
)
tCpmProtOutProfViolIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tCpmProtOutProfViolIfEntry.setStatus("current")
_TCpmProtOutProfViolIfPeriods_Type = Gauge32
_TCpmProtOutProfViolIfPeriods_Object = MibTableColumn
tCpmProtOutProfViolIfPeriods = _TCpmProtOutProfViolIfPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 61, 1, 1),
    _TCpmProtOutProfViolIfPeriods_Type()
)
tCpmProtOutProfViolIfPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolIfPeriods.setStatus("current")
_TCpmProtOutProfViolIfTimeStart_Type = TimeStamp
_TCpmProtOutProfViolIfTimeStart_Object = MibTableColumn
tCpmProtOutProfViolIfTimeStart = _TCpmProtOutProfViolIfTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 61, 1, 2),
    _TCpmProtOutProfViolIfTimeStart_Type()
)
tCpmProtOutProfViolIfTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolIfTimeStart.setStatus("current")
_TCpmProtOutProfViolIfTime_Type = TimeStamp
_TCpmProtOutProfViolIfTime_Object = MibTableColumn
tCpmProtOutProfViolIfTime = _TCpmProtOutProfViolIfTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 61, 1, 3),
    _TCpmProtOutProfViolIfTime_Type()
)
tCpmProtOutProfViolIfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolIfTime.setStatus("current")
_TCpmProtOutProfViolSapTable_Object = MibTable
tCpmProtOutProfViolSapTable = _TCpmProtOutProfViolSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 62)
)
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSapTable.setStatus("current")
_TCpmProtOutProfViolSapEntry_Object = MibTableRow
tCpmProtOutProfViolSapEntry = _TCpmProtOutProfViolSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 62, 1)
)
tCpmProtOutProfViolSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSapEntry.setStatus("current")
_TCpmProtOutProfViolSapPeriods_Type = Gauge32
_TCpmProtOutProfViolSapPeriods_Object = MibTableColumn
tCpmProtOutProfViolSapPeriods = _TCpmProtOutProfViolSapPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 62, 1, 1),
    _TCpmProtOutProfViolSapPeriods_Type()
)
tCpmProtOutProfViolSapPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSapPeriods.setStatus("current")
_TCpmProtOutProfViolSapTimeStart_Type = TimeStamp
_TCpmProtOutProfViolSapTimeStart_Object = MibTableColumn
tCpmProtOutProfViolSapTimeStart = _TCpmProtOutProfViolSapTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 62, 1, 2),
    _TCpmProtOutProfViolSapTimeStart_Type()
)
tCpmProtOutProfViolSapTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSapTimeStart.setStatus("current")
_TCpmProtOutProfViolSapTime_Type = TimeStamp
_TCpmProtOutProfViolSapTime_Object = MibTableColumn
tCpmProtOutProfViolSapTime = _TCpmProtOutProfViolSapTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 62, 1, 3),
    _TCpmProtOutProfViolSapTime_Type()
)
tCpmProtOutProfViolSapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSapTime.setStatus("current")
_TCpmProtOutProfViolSdpBindTable_Object = MibTable
tCpmProtOutProfViolSdpBindTable = _TCpmProtOutProfViolSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 63)
)
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSdpBindTable.setStatus("current")
_TCpmProtOutProfViolSdpBindEntry_Object = MibTableRow
tCpmProtOutProfViolSdpBindEntry = _TCpmProtOutProfViolSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 63, 1)
)
tCpmProtOutProfViolSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSdpBindEntry.setStatus("current")
_TCpmProtOutProfViolSdpBindPeriod_Type = Gauge32
_TCpmProtOutProfViolSdpBindPeriod_Object = MibTableColumn
tCpmProtOutProfViolSdpBindPeriod = _TCpmProtOutProfViolSdpBindPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 63, 1, 1),
    _TCpmProtOutProfViolSdpBindPeriod_Type()
)
tCpmProtOutProfViolSdpBindPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSdpBindPeriod.setStatus("current")
_TCpmProtOutProfViolSdpBindTmeStr_Type = TimeStamp
_TCpmProtOutProfViolSdpBindTmeStr_Object = MibTableColumn
tCpmProtOutProfViolSdpBindTmeStr = _TCpmProtOutProfViolSdpBindTmeStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 63, 1, 2),
    _TCpmProtOutProfViolSdpBindTmeStr_Type()
)
tCpmProtOutProfViolSdpBindTmeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSdpBindTmeStr.setStatus("current")
_TCpmProtOutProfViolSdpBindTime_Type = TimeStamp
_TCpmProtOutProfViolSdpBindTime_Object = MibTableColumn
tCpmProtOutProfViolSdpBindTime = _TCpmProtOutProfViolSdpBindTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 63, 1, 3),
    _TCpmProtOutProfViolSdpBindTime_Type()
)
tCpmProtOutProfViolSdpBindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tCpmProtOutProfViolSdpBindTime.setStatus("current")
_TmnxCpmProtExcdSdpBindIpTable_Object = MibTable
tmnxCpmProtExcdSdpBindIpTable = _TmnxCpmProtExcdSdpBindIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64)
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpTable.setStatus("current")
_TmnxCpmProtExcdSdpBindIpEntry_Object = MibTableRow
tmnxCpmProtExcdSdpBindIpEntry = _TmnxCpmProtExcdSdpBindIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64, 1)
)
tmnxCpmProtExcdSdpBindIpEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIpAddrType"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpEntry.setStatus("current")
_TmnxCpmProtExcdSdpBindIpAddrType_Type = InetAddressType
_TmnxCpmProtExcdSdpBindIpAddrType_Object = MibTableColumn
tmnxCpmProtExcdSdpBindIpAddrType = _TmnxCpmProtExcdSdpBindIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64, 1, 1),
    _TmnxCpmProtExcdSdpBindIpAddrType_Type()
)
tmnxCpmProtExcdSdpBindIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpAddrType.setStatus("current")


class _TmnxCpmProtExcdSdpBindIpAddr_Type(InetAddress):
    """Custom type tmnxCpmProtExcdSdpBindIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxCpmProtExcdSdpBindIpAddr_Type.__name__ = "InetAddress"
_TmnxCpmProtExcdSdpBindIpAddr_Object = MibTableColumn
tmnxCpmProtExcdSdpBindIpAddr = _TmnxCpmProtExcdSdpBindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64, 1, 2),
    _TmnxCpmProtExcdSdpBindIpAddr_Type()
)
tmnxCpmProtExcdSdpBindIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpAddr.setStatus("current")
_TmnxCpmProtExcdSdpBindIpPeriods_Type = Counter32
_TmnxCpmProtExcdSdpBindIpPeriods_Object = MibTableColumn
tmnxCpmProtExcdSdpBindIpPeriods = _TmnxCpmProtExcdSdpBindIpPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64, 1, 3),
    _TmnxCpmProtExcdSdpBindIpPeriods_Type()
)
tmnxCpmProtExcdSdpBindIpPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpPeriods.setStatus("current")
_TmnxCpmProtExcdSdpBindIpStarted_Type = TimeStamp
_TmnxCpmProtExcdSdpBindIpStarted_Object = MibTableColumn
tmnxCpmProtExcdSdpBindIpStarted = _TmnxCpmProtExcdSdpBindIpStarted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64, 1, 4),
    _TmnxCpmProtExcdSdpBindIpStarted_Type()
)
tmnxCpmProtExcdSdpBindIpStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpStarted.setStatus("current")
_TmnxCpmProtExcdSdpBindIpTime_Type = TimeStamp
_TmnxCpmProtExcdSdpBindIpTime_Object = MibTableColumn
tmnxCpmProtExcdSdpBindIpTime = _TmnxCpmProtExcdSdpBindIpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 9, 64, 1, 5),
    _TmnxCpmProtExcdSdpBindIpTime_Type()
)
tmnxCpmProtExcdSdpBindIpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIpTime.setStatus("current")
_TmnxPasswordHashObjs_ObjectIdentity = ObjectIdentity
tmnxPasswordHashObjs = _TmnxPasswordHashObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 10)
)


class _TmnxPassHashReadVersion_Type(Integer32):
    """Custom type tmnxPassHashReadVersion based on Integer32"""
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
        *(("all", 0),
          ("version1", 1),
          ("version2", 2))
    )


_TmnxPassHashReadVersion_Type.__name__ = "Integer32"
_TmnxPassHashReadVersion_Object = MibScalar
tmnxPassHashReadVersion = _TmnxPassHashReadVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 10, 1),
    _TmnxPassHashReadVersion_Type()
)
tmnxPassHashReadVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPassHashReadVersion.setStatus("current")


class _TmnxPassHashWriteVersion_Type(Integer32):
    """Custom type tmnxPassHashWriteVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TmnxPassHashWriteVersion_Type.__name__ = "Integer32"
_TmnxPassHashWriteVersion_Object = MibScalar
tmnxPassHashWriteVersion = _TmnxPassHashWriteVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 10, 2),
    _TmnxPassHashWriteVersion_Type()
)
tmnxPassHashWriteVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPassHashWriteVersion.setStatus("current")
_TmnxSSHServerObjs_ObjectIdentity = ObjectIdentity
tmnxSSHServerObjs = _TmnxSSHServerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 11)
)


class _TmnxSSHServerPreserveKey_Type(TruthValue):
    """Custom type tmnxSSHServerPreserveKey based on TruthValue"""
    defaultValue = 2


_TmnxSSHServerPreserveKey_Type.__name__ = "TruthValue"
_TmnxSSHServerPreserveKey_Object = MibScalar
tmnxSSHServerPreserveKey = _TmnxSSHServerPreserveKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 11, 1),
    _TmnxSSHServerPreserveKey_Type()
)
tmnxSSHServerPreserveKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSSHServerPreserveKey.setStatus("current")


class _TmnxSSHServerVersion_Type(Integer32):
    """Custom type tmnxSSHServerVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2),
          ("both", 3))
    )


_TmnxSSHServerVersion_Type.__name__ = "Integer32"
_TmnxSSHServerVersion_Object = MibScalar
tmnxSSHServerVersion = _TmnxSSHServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 11, 2),
    _TmnxSSHServerVersion_Type()
)
tmnxSSHServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSSHServerVersion.setStatus("current")
_TmnxSourceIPTable_Object = MibTable
tmnxSourceIPTable = _TmnxSourceIPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12)
)
if mibBuilder.loadTexts:
    tmnxSourceIPTable.setStatus("current")
_TmnxSourceIPEntry_Object = MibTableRow
tmnxSourceIPEntry = _TmnxSourceIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1)
)
tmnxSourceIPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxSourceIPProtoApp"),
)
if mibBuilder.loadTexts:
    tmnxSourceIPEntry.setStatus("current")


class _TmnxSourceIPProtoApp_Type(Integer32):
    """Custom type tmnxSourceIPProtoApp based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ftp", 2),
          ("ssh", 3),
          ("radius", 4),
          ("tacplus", 5),
          ("snmpTrap", 6),
          ("syslog", 7),
          ("icmpPing", 8),
          ("traceRoute", 9),
          ("dns", 10),
          ("sntp", 11),
          ("ntp", 12),
          ("cflowd", 13),
          ("telnet6", 14),
          ("ftp6", 15),
          ("radius6", 16),
          ("tacplus6", 17),
          ("snmpTrap6", 18),
          ("syslog6", 19),
          ("icmpPing6", 20),
          ("traceRoute6", 21),
          ("dns6", 22),
          ("ptp", 23),
          ("mcreporter", 24),
          ("cflowd6", 25),
          ("ntp6", 26),
          ("sFlow", 27),
          ("sFlow6", 28))
    )


_TmnxSourceIPProtoApp_Type.__name__ = "Integer32"
_TmnxSourceIPProtoApp_Object = MibTableColumn
tmnxSourceIPProtoApp = _TmnxSourceIPProtoApp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1, 2),
    _TmnxSourceIPProtoApp_Type()
)
tmnxSourceIPProtoApp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSourceIPProtoApp.setStatus("current")
_TmnxSourceIPRowStatus_Type = RowStatus
_TmnxSourceIPRowStatus_Object = MibTableColumn
tmnxSourceIPRowStatus = _TmnxSourceIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1, 3),
    _TmnxSourceIPRowStatus_Type()
)
tmnxSourceIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSourceIPRowStatus.setStatus("current")


class _TmnxSourceIPAddressType_Type(InetAddressType):
    """Custom type tmnxSourceIPAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxSourceIPAddressType_Type.__name__ = "InetAddressType"
_TmnxSourceIPAddressType_Object = MibTableColumn
tmnxSourceIPAddressType = _TmnxSourceIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1, 4),
    _TmnxSourceIPAddressType_Type()
)
tmnxSourceIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSourceIPAddressType.setStatus("current")


class _TmnxSourceIPAddress_Type(InetAddress):
    """Custom type tmnxSourceIPAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxSourceIPAddress_Type.__name__ = "InetAddress"
_TmnxSourceIPAddress_Object = MibTableColumn
tmnxSourceIPAddress = _TmnxSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1, 5),
    _TmnxSourceIPAddress_Type()
)
tmnxSourceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSourceIPAddress.setStatus("current")


class _TmnxSourceIPIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxSourceIPIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxSourceIPIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxSourceIPIfIndex_Object = MibTableColumn
tmnxSourceIPIfIndex = _TmnxSourceIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1, 6),
    _TmnxSourceIPIfIndex_Type()
)
tmnxSourceIPIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSourceIPIfIndex.setStatus("current")


class _TmnxSourceIPOperStatus_Type(Integer32):
    """Custom type tmnxSourceIPOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxSourceIPOperStatus_Type.__name__ = "Integer32"
_TmnxSourceIPOperStatus_Object = MibTableColumn
tmnxSourceIPOperStatus = _TmnxSourceIPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 12, 1, 7),
    _TmnxSourceIPOperStatus_Type()
)
tmnxSourceIPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSourceIPOperStatus.setStatus("current")
_TmnxUserTemplateTable_Object = MibTable
tmnxUserTemplateTable = _TmnxUserTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13)
)
if mibBuilder.loadTexts:
    tmnxUserTemplateTable.setStatus("current")
_TmnxUserTemplateEntry_Object = MibTableRow
tmnxUserTemplateEntry = _TmnxUserTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1)
)
tmnxUserTemplateEntry.setIndexNames(
    (1, "TIMETRA-SECURITY-MIB", "tmnxTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxUserTemplateEntry.setStatus("current")
_TmnxTemplateName_Type = TNamedItem
_TmnxTemplateName_Object = MibTableColumn
tmnxTemplateName = _TmnxTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1, 1),
    _TmnxTemplateName_Type()
)
tmnxTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTemplateName.setStatus("current")


class _TmnxTemplateAccess_Type(Bits):
    """Custom type tmnxTemplateAccess based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("console", 0),
          ("ftp", 1))
    )

_TmnxTemplateAccess_Type.__name__ = "Bits"
_TmnxTemplateAccess_Object = MibTableColumn
tmnxTemplateAccess = _TmnxTemplateAccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1, 2),
    _TmnxTemplateAccess_Type()
)
tmnxTemplateAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTemplateAccess.setStatus("current")


class _TmnxTemplateHomeDirectory_Type(DisplayString):
    """Custom type tmnxTemplateHomeDirectory based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TmnxTemplateHomeDirectory_Type.__name__ = "DisplayString"
_TmnxTemplateHomeDirectory_Object = MibTableColumn
tmnxTemplateHomeDirectory = _TmnxTemplateHomeDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1, 3),
    _TmnxTemplateHomeDirectory_Type()
)
tmnxTemplateHomeDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTemplateHomeDirectory.setStatus("current")


class _TmnxTemplateRestrictedToHome_Type(TruthValue):
    """Custom type tmnxTemplateRestrictedToHome based on TruthValue"""
    defaultValue = 2


_TmnxTemplateRestrictedToHome_Type.__name__ = "TruthValue"
_TmnxTemplateRestrictedToHome_Object = MibTableColumn
tmnxTemplateRestrictedToHome = _TmnxTemplateRestrictedToHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1, 4),
    _TmnxTemplateRestrictedToHome_Type()
)
tmnxTemplateRestrictedToHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTemplateRestrictedToHome.setStatus("current")


class _TmnxTemplateConsoleLoginExecFile_Type(DisplayString):
    """Custom type tmnxTemplateConsoleLoginExecFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TmnxTemplateConsoleLoginExecFile_Type.__name__ = "DisplayString"
_TmnxTemplateConsoleLoginExecFile_Object = MibTableColumn
tmnxTemplateConsoleLoginExecFile = _TmnxTemplateConsoleLoginExecFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1, 5),
    _TmnxTemplateConsoleLoginExecFile_Type()
)
tmnxTemplateConsoleLoginExecFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTemplateConsoleLoginExecFile.setStatus("current")


class _TmnxTemplateProfile_Type(TNamedItem):
    """Custom type tmnxTemplateProfile based on TNamedItem"""
    defaultValue = OctetString("default")


_TmnxTemplateProfile_Type.__name__ = "TNamedItem"
_TmnxTemplateProfile_Object = MibTableColumn
tmnxTemplateProfile = _TmnxTemplateProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 13, 1, 6),
    _TmnxTemplateProfile_Type()
)
tmnxTemplateProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTemplateProfile.setStatus("current")
_TmnxKeyChainTable_Object = MibTable
tmnxKeyChainTable = _TmnxKeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14)
)
if mibBuilder.loadTexts:
    tmnxKeyChainTable.setStatus("current")
_TmnxKeyChainEntry_Object = MibTableRow
tmnxKeyChainEntry = _TmnxKeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1)
)
tmnxKeyChainEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxKeyChainName"),
)
if mibBuilder.loadTexts:
    tmnxKeyChainEntry.setStatus("current")
_TmnxKeyChainName_Type = TNamedItem
_TmnxKeyChainName_Object = MibTableColumn
tmnxKeyChainName = _TmnxKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 1),
    _TmnxKeyChainName_Type()
)
tmnxKeyChainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxKeyChainName.setStatus("current")
_TmnxKeyChainRowStatus_Type = RowStatus
_TmnxKeyChainRowStatus_Object = MibTableColumn
tmnxKeyChainRowStatus = _TmnxKeyChainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 2),
    _TmnxKeyChainRowStatus_Type()
)
tmnxKeyChainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainRowStatus.setStatus("current")


class _TmnxKeyChainDescription_Type(TItemDescription):
    """Custom type tmnxKeyChainDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxKeyChainDescription_Type.__name__ = "TItemDescription"
_TmnxKeyChainDescription_Object = MibTableColumn
tmnxKeyChainDescription = _TmnxKeyChainDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 3),
    _TmnxKeyChainDescription_Type()
)
tmnxKeyChainDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainDescription.setStatus("current")


class _TmnxKeyChainSendTcpOptionNum_Type(TmnxKeyChainTcpOptionNum):
    """Custom type tmnxKeyChainSendTcpOptionNum based on TmnxKeyChainTcpOptionNum"""
    defaultValue = 2


_TmnxKeyChainSendTcpOptionNum_Type.__name__ = "TmnxKeyChainTcpOptionNum"
_TmnxKeyChainSendTcpOptionNum_Object = MibTableColumn
tmnxKeyChainSendTcpOptionNum = _TmnxKeyChainSendTcpOptionNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 4),
    _TmnxKeyChainSendTcpOptionNum_Type()
)
tmnxKeyChainSendTcpOptionNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainSendTcpOptionNum.setStatus("current")


class _TmnxKeyChainReceiveTcpOptionNum_Type(TmnxKeyChainTcpOptionNum):
    """Custom type tmnxKeyChainReceiveTcpOptionNum based on TmnxKeyChainTcpOptionNum"""
    defaultValue = 2


_TmnxKeyChainReceiveTcpOptionNum_Type.__name__ = "TmnxKeyChainTcpOptionNum"
_TmnxKeyChainReceiveTcpOptionNum_Object = MibTableColumn
tmnxKeyChainReceiveTcpOptionNum = _TmnxKeyChainReceiveTcpOptionNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 5),
    _TmnxKeyChainReceiveTcpOptionNum_Type()
)
tmnxKeyChainReceiveTcpOptionNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainReceiveTcpOptionNum.setStatus("current")


class _TmnxKeyChainAdminState_Type(TmnxAdminState):
    """Custom type tmnxKeyChainAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxKeyChainAdminState_Type.__name__ = "TmnxAdminState"
_TmnxKeyChainAdminState_Object = MibTableColumn
tmnxKeyChainAdminState = _TmnxKeyChainAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 6),
    _TmnxKeyChainAdminState_Type()
)
tmnxKeyChainAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainAdminState.setStatus("current")
_TmnxKeyChainOperState_Type = TmnxOperState
_TmnxKeyChainOperState_Object = MibTableColumn
tmnxKeyChainOperState = _TmnxKeyChainOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 7),
    _TmnxKeyChainOperState_Type()
)
tmnxKeyChainOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxKeyChainOperState.setStatus("current")


class _TmnxKeyChainExpired_Type(TruthValue):
    """Custom type tmnxKeyChainExpired based on TruthValue"""
    defaultValue = 2


_TmnxKeyChainExpired_Type.__name__ = "TruthValue"
_TmnxKeyChainExpired_Object = MibTableColumn
tmnxKeyChainExpired = _TmnxKeyChainExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 14, 1, 8),
    _TmnxKeyChainExpired_Type()
)
tmnxKeyChainExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxKeyChainExpired.setStatus("current")
_TmnxKeyChainKeyTable_Object = MibTable
tmnxKeyChainKeyTable = _TmnxKeyChainKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15)
)
if mibBuilder.loadTexts:
    tmnxKeyChainKeyTable.setStatus("current")
_TmnxKeyChainKeyEntry_Object = MibTableRow
tmnxKeyChainKeyEntry = _TmnxKeyChainKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1)
)
tmnxKeyChainKeyEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxKeyChainName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyDirection"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyID"),
)
if mibBuilder.loadTexts:
    tmnxKeyChainKeyEntry.setStatus("current")
_TmnxKeyChainKeyDirection_Type = TmnxKeyChainKeyDirection
_TmnxKeyChainKeyDirection_Object = MibTableColumn
tmnxKeyChainKeyDirection = _TmnxKeyChainKeyDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 1),
    _TmnxKeyChainKeyDirection_Type()
)
tmnxKeyChainKeyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyDirection.setStatus("current")


class _TmnxKeyChainKeyID_Type(Unsigned32):
    """Custom type tmnxKeyChainKeyID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_TmnxKeyChainKeyID_Type.__name__ = "Unsigned32"
_TmnxKeyChainKeyID_Object = MibTableColumn
tmnxKeyChainKeyID = _TmnxKeyChainKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 2),
    _TmnxKeyChainKeyID_Type()
)
tmnxKeyChainKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyID.setStatus("current")
_TmnxKeyChainKeyRowStatus_Type = RowStatus
_TmnxKeyChainKeyRowStatus_Object = MibTableColumn
tmnxKeyChainKeyRowStatus = _TmnxKeyChainKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 3),
    _TmnxKeyChainKeyRowStatus_Type()
)
tmnxKeyChainKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyRowStatus.setStatus("current")


class _TmnxKeyChainAuthenticationKey_Type(OctetString):
    """Custom type tmnxKeyChainAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxKeyChainAuthenticationKey_Type.__name__ = "OctetString"
_TmnxKeyChainAuthenticationKey_Object = MibTableColumn
tmnxKeyChainAuthenticationKey = _TmnxKeyChainAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 4),
    _TmnxKeyChainAuthenticationKey_Type()
)
tmnxKeyChainAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainAuthenticationKey.setStatus("current")
_TmnxKeyChainKeyAlgorithm_Type = TmnxKeyChainKeyAlgorithm
_TmnxKeyChainKeyAlgorithm_Object = MibTableColumn
tmnxKeyChainKeyAlgorithm = _TmnxKeyChainKeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 5),
    _TmnxKeyChainKeyAlgorithm_Type()
)
tmnxKeyChainKeyAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyAlgorithm.setStatus("current")


class _TmnxKeyChainKeyBeginTime_Type(DateAndTime):
    """Custom type tmnxKeyChainKeyBeginTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_TmnxKeyChainKeyBeginTime_Type.__name__ = "DateAndTime"
_TmnxKeyChainKeyBeginTime_Object = MibTableColumn
tmnxKeyChainKeyBeginTime = _TmnxKeyChainKeyBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 6),
    _TmnxKeyChainKeyBeginTime_Type()
)
tmnxKeyChainKeyBeginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyBeginTime.setStatus("current")


class _TmnxKeyChainKeyEndTime_Type(DateAndTime):
    """Custom type tmnxKeyChainKeyEndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_TmnxKeyChainKeyEndTime_Type.__name__ = "DateAndTime"
_TmnxKeyChainKeyEndTime_Object = MibTableColumn
tmnxKeyChainKeyEndTime = _TmnxKeyChainKeyEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 7),
    _TmnxKeyChainKeyEndTime_Type()
)
tmnxKeyChainKeyEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyEndTime.setStatus("current")


class _TmnxKeyChainKeyTolerance_Type(Unsigned32):
    """Custom type tmnxKeyChainKeyTolerance based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxKeyChainKeyTolerance_Type.__name__ = "Unsigned32"
_TmnxKeyChainKeyTolerance_Object = MibTableColumn
tmnxKeyChainKeyTolerance = _TmnxKeyChainKeyTolerance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 8),
    _TmnxKeyChainKeyTolerance_Type()
)
tmnxKeyChainKeyTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyTolerance.setUnits("seconds")


class _TmnxKeyChainKeyAdminState_Type(TmnxAdminState):
    """Custom type tmnxKeyChainKeyAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxKeyChainKeyAdminState_Type.__name__ = "TmnxAdminState"
_TmnxKeyChainKeyAdminState_Object = MibTableColumn
tmnxKeyChainKeyAdminState = _TmnxKeyChainKeyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 9),
    _TmnxKeyChainKeyAdminState_Type()
)
tmnxKeyChainKeyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyAdminState.setStatus("current")


class _TmnxKeyChainKeyOption_Type(TmnxKeyChainKeyOption):
    """Custom type tmnxKeyChainKeyOption based on TmnxKeyChainKeyOption"""
    defaultValue = 0


_TmnxKeyChainKeyOption_Type.__name__ = "TmnxKeyChainKeyOption"
_TmnxKeyChainKeyOption_Object = MibTableColumn
tmnxKeyChainKeyOption = _TmnxKeyChainKeyOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 15, 1, 10),
    _TmnxKeyChainKeyOption_Type()
)
tmnxKeyChainKeyOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxKeyChainKeyOption.setStatus("current")
_TmnxSecurityNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxSecurityNotificationObjs = _TmnxSecurityNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16)
)


class _TmnxKeyChainAuthFailReason_Type(Integer32):
    """Custom type tmnxKeyChainAuthFailReason based on Integer32"""
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
        *(("other", 1),
          ("noEnhAuthOptionRecvd", 2),
          ("invalidOptionLen", 3),
          ("mismatchRecvOption", 4),
          ("invalidKeyId", 5),
          ("digestMismatch", 6),
          ("mismatchAlgId", 7))
    )


_TmnxKeyChainAuthFailReason_Type.__name__ = "Integer32"
_TmnxKeyChainAuthFailReason_Object = MibScalar
tmnxKeyChainAuthFailReason = _TmnxKeyChainAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 1),
    _TmnxKeyChainAuthFailReason_Type()
)
tmnxKeyChainAuthFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxKeyChainAuthFailReason.setStatus("current")
_TmnxKeyChainAuthAddrType_Type = InetAddressType
_TmnxKeyChainAuthAddrType_Object = MibScalar
tmnxKeyChainAuthAddrType = _TmnxKeyChainAuthAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 2),
    _TmnxKeyChainAuthAddrType_Type()
)
tmnxKeyChainAuthAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxKeyChainAuthAddrType.setStatus("current")
_TmnxKeyChainAuthAddr_Type = InetAddress
_TmnxKeyChainAuthAddr_Object = MibScalar
tmnxKeyChainAuthAddr = _TmnxKeyChainAuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 3),
    _TmnxKeyChainAuthAddr_Type()
)
tmnxKeyChainAuthAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxKeyChainAuthAddr.setStatus("current")


class _TmnxMD5AuthFailReason_Type(Integer32):
    """Custom type tmnxMD5AuthFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("digestMismatch", 1)
    )


_TmnxMD5AuthFailReason_Type.__name__ = "Integer32"
_TmnxMD5AuthFailReason_Object = MibScalar
tmnxMD5AuthFailReason = _TmnxMD5AuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 4),
    _TmnxMD5AuthFailReason_Type()
)
tmnxMD5AuthFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMD5AuthFailReason.setStatus("current")
_TmnxMD5AuthAddrType_Type = InetAddressType
_TmnxMD5AuthAddrType_Object = MibScalar
tmnxMD5AuthAddrType = _TmnxMD5AuthAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 5),
    _TmnxMD5AuthAddrType_Type()
)
tmnxMD5AuthAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMD5AuthAddrType.setStatus("current")
_TmnxMD5AuthAddr_Type = InetAddress
_TmnxMD5AuthAddr_Object = MibScalar
tmnxMD5AuthAddr = _TmnxMD5AuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 6),
    _TmnxMD5AuthAddr_Type()
)
tmnxMD5AuthAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMD5AuthAddr.setStatus("current")


class _TmnxMD5AuthKey_Type(OctetString):
    """Custom type tmnxMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxMD5AuthKey_Type.__name__ = "OctetString"
_TmnxMD5AuthKey_Object = MibScalar
tmnxMD5AuthKey = _TmnxMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 7),
    _TmnxMD5AuthKey_Type()
)
tmnxMD5AuthKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMD5AuthKey.setStatus("current")


class _TmnxCpmProtPolId_Type(TCpmProtPolicyID):
    """Custom type tmnxCpmProtPolId based on TCpmProtPolicyID"""
    subtypeSpec = TCpmProtPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxCpmProtPolId_Type.__name__ = "TCpmProtPolicyID"
_TmnxCpmProtPolId_Object = MibScalar
tmnxCpmProtPolId = _TmnxCpmProtPolId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 8),
    _TmnxCpmProtPolId_Type()
)
tmnxCpmProtPolId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCpmProtPolId.setStatus("current")
_TmnxSecNotifFailureReason_Type = DisplayString
_TmnxSecNotifFailureReason_Object = MibScalar
tmnxSecNotifFailureReason = _TmnxSecNotifFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 9),
    _TmnxSecNotifFailureReason_Type()
)
tmnxSecNotifFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSecNotifFailureReason.setStatus("current")


class _TmnxSecNotifFile_Type(DisplayString):
    """Custom type tmnxSecNotifFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxSecNotifFile_Type.__name__ = "DisplayString"
_TmnxSecNotifFile_Object = MibScalar
tmnxSecNotifFile = _TmnxSecNotifFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 10),
    _TmnxSecNotifFile_Type()
)
tmnxSecNotifFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSecNotifFile.setStatus("current")
_TmnxSecNotifTunnelName_Type = TNamedItemOrEmpty
_TmnxSecNotifTunnelName_Object = MibScalar
tmnxSecNotifTunnelName = _TmnxSecNotifTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 11),
    _TmnxSecNotifTunnelName_Type()
)
tmnxSecNotifTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSecNotifTunnelName.setStatus("current")
_TmnxSecNotifCert_Type = DisplayString
_TmnxSecNotifCert_Object = MibScalar
tmnxSecNotifCert = _TmnxSecNotifCert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 12),
    _TmnxSecNotifCert_Type()
)
tmnxSecNotifCert.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSecNotifCert.setStatus("current")
_TmnxSecNotifOrigProtocol_Type = DisplayString
_TmnxSecNotifOrigProtocol_Object = MibScalar
tmnxSecNotifOrigProtocol = _TmnxSecNotifOrigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 16, 13),
    _TmnxSecNotifOrigProtocol_Type()
)
tmnxSecNotifOrigProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSecNotifOrigProtocol.setStatus("current")
_TmnxSecurityCpmProtNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxSecurityCpmProtNotificationObjs = _TmnxSecurityCpmProtNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 17)
)
_TmnxCpmProtViolMacAddress_Type = MacAddress
_TmnxCpmProtViolMacAddress_Object = MibScalar
tmnxCpmProtViolMacAddress = _TmnxCpmProtViolMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 17, 1),
    _TmnxCpmProtViolMacAddress_Type()
)
tmnxCpmProtViolMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCpmProtViolMacAddress.setStatus("current")
_TmnxCpmProtViolMacPeriods_Type = Gauge32
_TmnxCpmProtViolMacPeriods_Object = MibScalar
tmnxCpmProtViolMacPeriods = _TmnxCpmProtViolMacPeriods_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 17, 2),
    _TmnxCpmProtViolMacPeriods_Type()
)
tmnxCpmProtViolMacPeriods.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCpmProtViolMacPeriods.setStatus("current")


class _TmnxCpmProtViolExcdPktHexDump_Type(OctetString):
    """Custom type tmnxCpmProtViolExcdPktHexDump based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxCpmProtViolExcdPktHexDump_Type.__name__ = "OctetString"
_TmnxCpmProtViolExcdPktHexDump_Object = MibScalar
tmnxCpmProtViolExcdPktHexDump = _TmnxCpmProtViolExcdPktHexDump_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 17, 3),
    _TmnxCpmProtViolExcdPktHexDump_Type()
)
tmnxCpmProtViolExcdPktHexDump.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxCpmProtViolExcdPktHexDump.setStatus("current")
_TmnxPkiSecurityObjs_ObjectIdentity = ObjectIdentity
tmnxPkiSecurityObjs = _TmnxPkiSecurityObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18)
)


class _TmnxPkiMaxCertChainDepth_Type(Unsigned32):
    """Custom type tmnxPkiMaxCertChainDepth based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TmnxPkiMaxCertChainDepth_Type.__name__ = "Unsigned32"
_TmnxPkiMaxCertChainDepth_Object = MibScalar
tmnxPkiMaxCertChainDepth = _TmnxPkiMaxCertChainDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 1),
    _TmnxPkiMaxCertChainDepth_Type()
)
tmnxPkiMaxCertChainDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiMaxCertChainDepth.setStatus("current")
_TmnxPkiCAProfileTableLastChanged_Type = TimeStamp
_TmnxPkiCAProfileTableLastChanged_Object = MibScalar
tmnxPkiCAProfileTableLastChanged = _TmnxPkiCAProfileTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 2),
    _TmnxPkiCAProfileTableLastChanged_Type()
)
tmnxPkiCAProfileTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileTableLastChanged.setStatus("current")
_TmnxPkiCAProfileTable_Object = MibTable
tmnxPkiCAProfileTable = _TmnxPkiCAProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3)
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfileTable.setStatus("current")
_TmnxPkiCAProfileEntry_Object = MibTableRow
tmnxPkiCAProfileEntry = _TmnxPkiCAProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1)
)
tmnxPkiCAProfileEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxPkiCAProfile"),
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfileEntry.setStatus("current")
_TmnxPkiCAProfile_Type = TNamedItem
_TmnxPkiCAProfile_Object = MibTableColumn
tmnxPkiCAProfile = _TmnxPkiCAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 1),
    _TmnxPkiCAProfile_Type()
)
tmnxPkiCAProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPkiCAProfile.setStatus("current")
_TmnxPkiCAProfileRowStatus_Type = RowStatus
_TmnxPkiCAProfileRowStatus_Object = MibTableColumn
tmnxPkiCAProfileRowStatus = _TmnxPkiCAProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 2),
    _TmnxPkiCAProfileRowStatus_Type()
)
tmnxPkiCAProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileRowStatus.setStatus("current")
_TmnxPkiCAProfileLastChanged_Type = TimeStamp
_TmnxPkiCAProfileLastChanged_Object = MibTableColumn
tmnxPkiCAProfileLastChanged = _TmnxPkiCAProfileLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 3),
    _TmnxPkiCAProfileLastChanged_Type()
)
tmnxPkiCAProfileLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileLastChanged.setStatus("current")


class _TmnxPkiCAProfileDescr_Type(TItemDescription):
    """Custom type tmnxPkiCAProfileDescr based on TItemDescription"""
    defaultHexValue = ""


_TmnxPkiCAProfileDescr_Type.__name__ = "TItemDescription"
_TmnxPkiCAProfileDescr_Object = MibTableColumn
tmnxPkiCAProfileDescr = _TmnxPkiCAProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 4),
    _TmnxPkiCAProfileDescr_Type()
)
tmnxPkiCAProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileDescr.setStatus("current")


class _TmnxPkiCAProfileCRLFile_Type(DisplayString):
    """Custom type tmnxPkiCAProfileCRLFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxPkiCAProfileCRLFile_Type.__name__ = "DisplayString"
_TmnxPkiCAProfileCRLFile_Object = MibTableColumn
tmnxPkiCAProfileCRLFile = _TmnxPkiCAProfileCRLFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 5),
    _TmnxPkiCAProfileCRLFile_Type()
)
tmnxPkiCAProfileCRLFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileCRLFile.setStatus("current")


class _TmnxPkiCAProfileCertFile_Type(DisplayString):
    """Custom type tmnxPkiCAProfileCertFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxPkiCAProfileCertFile_Type.__name__ = "DisplayString"
_TmnxPkiCAProfileCertFile_Object = MibTableColumn
tmnxPkiCAProfileCertFile = _TmnxPkiCAProfileCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 6),
    _TmnxPkiCAProfileCertFile_Type()
)
tmnxPkiCAProfileCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileCertFile.setStatus("current")


class _TmnxPkiCAProfileAdminState_Type(TmnxAdminState):
    """Custom type tmnxPkiCAProfileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPkiCAProfileAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPkiCAProfileAdminState_Object = MibTableColumn
tmnxPkiCAProfileAdminState = _TmnxPkiCAProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 7),
    _TmnxPkiCAProfileAdminState_Type()
)
tmnxPkiCAProfileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileAdminState.setStatus("current")
_TmnxPkiCAProfileOperState_Type = TmnxOperState
_TmnxPkiCAProfileOperState_Object = MibTableColumn
tmnxPkiCAProfileOperState = _TmnxPkiCAProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 8),
    _TmnxPkiCAProfileOperState_Type()
)
tmnxPkiCAProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileOperState.setStatus("current")


class _TmnxPkiCAProfileOperFlags_Type(Bits):
    """Custom type tmnxPkiCAProfileOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("invalidCrl", 1),
          ("invalidCert", 2),
          ("invalidCmpv2SigningCert", 3))
    )

_TmnxPkiCAProfileOperFlags_Type.__name__ = "Bits"
_TmnxPkiCAProfileOperFlags_Object = MibTableColumn
tmnxPkiCAProfileOperFlags = _TmnxPkiCAProfileOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 9),
    _TmnxPkiCAProfileOperFlags_Type()
)
tmnxPkiCAProfileOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfileOperFlags.setStatus("current")


class _TmnxPkiCAProfOcspRespUrl_Type(DisplayString):
    """Custom type tmnxPkiCAProfOcspRespUrl based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxPkiCAProfOcspRespUrl_Type.__name__ = "DisplayString"
_TmnxPkiCAProfOcspRespUrl_Object = MibTableColumn
tmnxPkiCAProfOcspRespUrl = _TmnxPkiCAProfOcspRespUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 10),
    _TmnxPkiCAProfOcspRespUrl_Type()
)
tmnxPkiCAProfOcspRespUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfOcspRespUrl.setStatus("current")


class _TmnxPkiCAProfOcspSvcID_Type(TmnxServId):
    """Custom type tmnxPkiCAProfOcspSvcID based on TmnxServId"""
    defaultValue = 0


_TmnxPkiCAProfOcspSvcID_Type.__name__ = "TmnxServId"
_TmnxPkiCAProfOcspSvcID_Object = MibTableColumn
tmnxPkiCAProfOcspSvcID = _TmnxPkiCAProfOcspSvcID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 11),
    _TmnxPkiCAProfOcspSvcID_Type()
)
tmnxPkiCAProfOcspSvcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfOcspSvcID.setStatus("current")


class _TmnxPkiCAProfOcspVerifyCertFile_Type(DisplayString):
    """Custom type tmnxPkiCAProfOcspVerifyCertFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxPkiCAProfOcspVerifyCertFile_Type.__name__ = "DisplayString"
_TmnxPkiCAProfOcspVerifyCertFile_Object = MibTableColumn
tmnxPkiCAProfOcspVerifyCertFile = _TmnxPkiCAProfOcspVerifyCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 12),
    _TmnxPkiCAProfOcspVerifyCertFile_Type()
)
tmnxPkiCAProfOcspVerifyCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfOcspVerifyCertFile.setStatus("current")


class _TmnxPkiCAProfOcspVerifyCertCA_Type(TruthValue):
    """Custom type tmnxPkiCAProfOcspVerifyCertCA based on TruthValue"""
    defaultValue = 1


_TmnxPkiCAProfOcspVerifyCertCA_Type.__name__ = "TruthValue"
_TmnxPkiCAProfOcspVerifyCertCA_Object = MibTableColumn
tmnxPkiCAProfOcspVerifyCertCA = _TmnxPkiCAProfOcspVerifyCertCA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 13),
    _TmnxPkiCAProfOcspVerifyCertCA_Type()
)
tmnxPkiCAProfOcspVerifyCertCA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfOcspVerifyCertCA.setStatus("current")


class _TmnxPkiCAProfOcspVerifyCertOvr_Type(TruthValue):
    """Custom type tmnxPkiCAProfOcspVerifyCertOvr based on TruthValue"""
    defaultValue = 1


_TmnxPkiCAProfOcspVerifyCertOvr_Type.__name__ = "TruthValue"
_TmnxPkiCAProfOcspVerifyCertOvr_Object = MibTableColumn
tmnxPkiCAProfOcspVerifyCertOvr = _TmnxPkiCAProfOcspVerifyCertOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 14),
    _TmnxPkiCAProfOcspVerifyCertOvr_Type()
)
tmnxPkiCAProfOcspVerifyCertOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfOcspVerifyCertOvr.setStatus("current")


class _TmnxPkiCAProfCmpHttpTimeout_Type(Unsigned32):
    """Custom type tmnxPkiCAProfCmpHttpTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxPkiCAProfCmpHttpTimeout_Type.__name__ = "Unsigned32"
_TmnxPkiCAProfCmpHttpTimeout_Object = MibTableColumn
tmnxPkiCAProfCmpHttpTimeout = _TmnxPkiCAProfCmpHttpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 15),
    _TmnxPkiCAProfCmpHttpTimeout_Type()
)
tmnxPkiCAProfCmpHttpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpHttpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpHttpTimeout.setUnits("seconds")


class _TmnxPkiCAProfCmpUrl_Type(DisplayString):
    """Custom type tmnxPkiCAProfCmpUrl based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxPkiCAProfCmpUrl_Type.__name__ = "DisplayString"
_TmnxPkiCAProfCmpUrl_Object = MibTableColumn
tmnxPkiCAProfCmpUrl = _TmnxPkiCAProfCmpUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 16),
    _TmnxPkiCAProfCmpUrl_Type()
)
tmnxPkiCAProfCmpUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpUrl.setStatus("current")


class _TmnxPkiCAProfCmpSvcID_Type(TmnxServId):
    """Custom type tmnxPkiCAProfCmpSvcID based on TmnxServId"""
    defaultValue = 0


_TmnxPkiCAProfCmpSvcID_Type.__name__ = "TmnxServId"
_TmnxPkiCAProfCmpSvcID_Object = MibTableColumn
tmnxPkiCAProfCmpSvcID = _TmnxPkiCAProfCmpSvcID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 17),
    _TmnxPkiCAProfCmpSvcID_Type()
)
tmnxPkiCAProfCmpSvcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpSvcID.setStatus("current")


class _TmnxPkiCAProfCmpRespSignCert_Type(DisplayString):
    """Custom type tmnxPkiCAProfCmpRespSignCert based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxPkiCAProfCmpRespSignCert_Type.__name__ = "DisplayString"
_TmnxPkiCAProfCmpRespSignCert_Object = MibTableColumn
tmnxPkiCAProfCmpRespSignCert = _TmnxPkiCAProfCmpRespSignCert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 18),
    _TmnxPkiCAProfCmpRespSignCert_Type()
)
tmnxPkiCAProfCmpRespSignCert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpRespSignCert.setStatus("current")


class _TmnxPkiCAProfCmpAccUnprotErr_Type(TruthValue):
    """Custom type tmnxPkiCAProfCmpAccUnprotErr based on TruthValue"""
    defaultValue = 2


_TmnxPkiCAProfCmpAccUnprotErr_Type.__name__ = "TruthValue"
_TmnxPkiCAProfCmpAccUnprotErr_Object = MibTableColumn
tmnxPkiCAProfCmpAccUnprotErr = _TmnxPkiCAProfCmpAccUnprotErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 19),
    _TmnxPkiCAProfCmpAccUnprotErr_Type()
)
tmnxPkiCAProfCmpAccUnprotErr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpAccUnprotErr.setStatus("current")


class _TmnxPkiCAProfCmpAccUnprotPki_Type(TruthValue):
    """Custom type tmnxPkiCAProfCmpAccUnprotPki based on TruthValue"""
    defaultValue = 2


_TmnxPkiCAProfCmpAccUnprotPki_Type.__name__ = "TruthValue"
_TmnxPkiCAProfCmpAccUnprotPki_Object = MibTableColumn
tmnxPkiCAProfCmpAccUnprotPki = _TmnxPkiCAProfCmpAccUnprotPki_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 20),
    _TmnxPkiCAProfCmpAccUnprotPki_Type()
)
tmnxPkiCAProfCmpAccUnprotPki.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpAccUnprotPki.setStatus("current")


class _TmnxPkiCAProfCmpSameRecipNonce_Type(TruthValue):
    """Custom type tmnxPkiCAProfCmpSameRecipNonce based on TruthValue"""
    defaultValue = 2


_TmnxPkiCAProfCmpSameRecipNonce_Type.__name__ = "TruthValue"
_TmnxPkiCAProfCmpSameRecipNonce_Object = MibTableColumn
tmnxPkiCAProfCmpSameRecipNonce = _TmnxPkiCAProfCmpSameRecipNonce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 21),
    _TmnxPkiCAProfCmpSameRecipNonce_Type()
)
tmnxPkiCAProfCmpSameRecipNonce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpSameRecipNonce.setStatus("current")


class _TmnxPkiCAProfCmpAlSetSndrForIr_Type(TruthValue):
    """Custom type tmnxPkiCAProfCmpAlSetSndrForIr based on TruthValue"""
    defaultValue = 2


_TmnxPkiCAProfCmpAlSetSndrForIr_Type.__name__ = "TruthValue"
_TmnxPkiCAProfCmpAlSetSndrForIr_Object = MibTableColumn
tmnxPkiCAProfCmpAlSetSndrForIr = _TmnxPkiCAProfCmpAlSetSndrForIr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 22),
    _TmnxPkiCAProfCmpAlSetSndrForIr_Type()
)
tmnxPkiCAProfCmpAlSetSndrForIr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpAlSetSndrForIr.setStatus("current")


class _TmnxPkiCAProfCmpHttpVersion_Type(Integer32):
    """Custom type tmnxPkiCAProfCmpHttpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v10", 1),
          ("v11", 2))
    )


_TmnxPkiCAProfCmpHttpVersion_Type.__name__ = "Integer32"
_TmnxPkiCAProfCmpHttpVersion_Object = MibTableColumn
tmnxPkiCAProfCmpHttpVersion = _TmnxPkiCAProfCmpHttpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 23),
    _TmnxPkiCAProfCmpHttpVersion_Type()
)
tmnxPkiCAProfCmpHttpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpHttpVersion.setStatus("current")


class _TmnxPkiCAProfRevokeChk_Type(Integer32):
    """Custom type tmnxPkiCAProfRevokeChk based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crl", 1),
          ("crlOptional", 2))
    )


_TmnxPkiCAProfRevokeChk_Type.__name__ = "Integer32"
_TmnxPkiCAProfRevokeChk_Object = MibTableColumn
tmnxPkiCAProfRevokeChk = _TmnxPkiCAProfRevokeChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 3, 1, 24),
    _TmnxPkiCAProfRevokeChk_Type()
)
tmnxPkiCAProfRevokeChk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfRevokeChk.setStatus("current")
_TmnxPkiCAProfCmpKeyTblLastChgd_Type = TimeStamp
_TmnxPkiCAProfCmpKeyTblLastChgd_Object = MibScalar
tmnxPkiCAProfCmpKeyTblLastChgd = _TmnxPkiCAProfCmpKeyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 4),
    _TmnxPkiCAProfCmpKeyTblLastChgd_Type()
)
tmnxPkiCAProfCmpKeyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeyTblLastChgd.setStatus("current")
_TmnxPkiCAProfCmpKeyTable_Object = MibTable
tmnxPkiCAProfCmpKeyTable = _TmnxPkiCAProfCmpKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 5)
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeyTable.setStatus("current")
_TmnxPkiCAProfCmpKeyEntry_Object = MibTableRow
tmnxPkiCAProfCmpKeyEntry = _TmnxPkiCAProfCmpKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 5, 1)
)
tmnxPkiCAProfCmpKeyEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxPkiCAProfile"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpKeyRefnum"),
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeyEntry.setStatus("current")


class _TmnxPkiCAProfCmpKeyRefnum_Type(DisplayString):
    """Custom type tmnxPkiCAProfCmpKeyRefnum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxPkiCAProfCmpKeyRefnum_Type.__name__ = "DisplayString"
_TmnxPkiCAProfCmpKeyRefnum_Object = MibTableColumn
tmnxPkiCAProfCmpKeyRefnum = _TmnxPkiCAProfCmpKeyRefnum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 5, 1, 1),
    _TmnxPkiCAProfCmpKeyRefnum_Type()
)
tmnxPkiCAProfCmpKeyRefnum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeyRefnum.setStatus("current")
_TmnxPkiCAProfCmpKeyRowStatus_Type = RowStatus
_TmnxPkiCAProfCmpKeyRowStatus_Object = MibTableColumn
tmnxPkiCAProfCmpKeyRowStatus = _TmnxPkiCAProfCmpKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 5, 1, 2),
    _TmnxPkiCAProfCmpKeyRowStatus_Type()
)
tmnxPkiCAProfCmpKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeyRowStatus.setStatus("current")
_TmnxPkiCAProfCmpKeyLastChanged_Type = TimeStamp
_TmnxPkiCAProfCmpKeyLastChanged_Object = MibTableColumn
tmnxPkiCAProfCmpKeyLastChanged = _TmnxPkiCAProfCmpKeyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 5, 1, 3),
    _TmnxPkiCAProfCmpKeyLastChanged_Type()
)
tmnxPkiCAProfCmpKeyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeyLastChanged.setStatus("current")


class _TmnxPkiCAProfCmpKeySecret_Type(DisplayString):
    """Custom type tmnxPkiCAProfCmpKeySecret based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxPkiCAProfCmpKeySecret_Type.__name__ = "DisplayString"
_TmnxPkiCAProfCmpKeySecret_Object = MibTableColumn
tmnxPkiCAProfCmpKeySecret = _TmnxPkiCAProfCmpKeySecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 5, 1, 4),
    _TmnxPkiCAProfCmpKeySecret_Type()
)
tmnxPkiCAProfCmpKeySecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCAProfCmpKeySecret.setStatus("current")


class _TmnxPkiCertDisplayFormat_Type(Integer32):
    """Custom type tmnxPkiCertDisplayFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("utf8", 2))
    )


_TmnxPkiCertDisplayFormat_Type.__name__ = "Integer32"
_TmnxPkiCertDisplayFormat_Object = MibScalar
tmnxPkiCertDisplayFormat = _TmnxPkiCertDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 7),
    _TmnxPkiCertDisplayFormat_Type()
)
tmnxPkiCertDisplayFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPkiCertDisplayFormat.setStatus("current")
_TmnxPkiCAProfActnTable_Object = MibTable
tmnxPkiCAProfActnTable = _TmnxPkiCAProfActnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22)
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnTable.setStatus("current")
_TmnxPkiCAProfActnEntry_Object = MibTableRow
tmnxPkiCAProfActnEntry = _TmnxPkiCAProfActnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1)
)
tmnxPkiCAProfActnEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxPkiCAProfile"),
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnEntry.setStatus("current")


class _TmnxPkiCAProfActnType_Type(Integer32):
    """Custom type tmnxPkiCAProfActnType based on Integer32"""
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
        *(("initialRegistration", 1),
          ("certRequest", 2),
          ("keyUpdate", 3),
          ("poll", 4),
          ("clearRequest", 5),
          ("abortRequest", 6))
    )


_TmnxPkiCAProfActnType_Type.__name__ = "Integer32"
_TmnxPkiCAProfActnType_Object = MibTableColumn
tmnxPkiCAProfActnType = _TmnxPkiCAProfActnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 1),
    _TmnxPkiCAProfActnType_Type()
)
tmnxPkiCAProfActnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnType.setStatus("current")


class _TmnxPkiCAProfAction_Type(TmnxActionType):
    """Custom type tmnxPkiCAProfAction based on TmnxActionType"""
    defaultValue = 2


_TmnxPkiCAProfAction_Type.__name__ = "TmnxActionType"
_TmnxPkiCAProfAction_Object = MibTableColumn
tmnxPkiCAProfAction = _TmnxPkiCAProfAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 2),
    _TmnxPkiCAProfAction_Type()
)
tmnxPkiCAProfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfAction.setStatus("current")


class _TmnxPkiCAProfActnKey_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TmnxPkiCAProfActnKey_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnKey_Object = MibTableColumn
tmnxPkiCAProfActnKey = _TmnxPkiCAProfActnKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 3),
    _TmnxPkiCAProfActnKey_Type()
)
tmnxPkiCAProfActnKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnKey.setStatus("current")


class _TmnxPkiCAProfActnProtAlgPass_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnProtAlgPass based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxPkiCAProfActnProtAlgPass_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnProtAlgPass_Object = MibTableColumn
tmnxPkiCAProfActnProtAlgPass = _TmnxPkiCAProfActnProtAlgPass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 4),
    _TmnxPkiCAProfActnProtAlgPass_Type()
)
tmnxPkiCAProfActnProtAlgPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnProtAlgPass.setStatus("current")


class _TmnxPkiCAProfActnProtAlgRef_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnProtAlgRef based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxPkiCAProfActnProtAlgRef_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnProtAlgRef_Object = MibTableColumn
tmnxPkiCAProfActnProtAlgRef = _TmnxPkiCAProfActnProtAlgRef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 5),
    _TmnxPkiCAProfActnProtAlgRef_Type()
)
tmnxPkiCAProfActnProtAlgRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnProtAlgRef.setStatus("current")


class _TmnxPkiCAProfActnProtAlgSigCert_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnProtAlgSigCert based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TmnxPkiCAProfActnProtAlgSigCert_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnProtAlgSigCert_Object = MibTableColumn
tmnxPkiCAProfActnProtAlgSigCert = _TmnxPkiCAProfActnProtAlgSigCert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 6),
    _TmnxPkiCAProfActnProtAlgSigCert_Type()
)
tmnxPkiCAProfActnProtAlgSigCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnProtAlgSigCert.setStatus("current")


class _TmnxPkiCAProfActnProtAlgSigHash_Type(Integer32):
    """Custom type tmnxPkiCAProfActnProtAlgSigHash based on Integer32"""
    defaultValue = 3

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
        *(("null", 1),
          ("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("sha224", 7))
    )


_TmnxPkiCAProfActnProtAlgSigHash_Type.__name__ = "Integer32"
_TmnxPkiCAProfActnProtAlgSigHash_Object = MibTableColumn
tmnxPkiCAProfActnProtAlgSigHash = _TmnxPkiCAProfActnProtAlgSigHash_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 7),
    _TmnxPkiCAProfActnProtAlgSigHash_Type()
)
tmnxPkiCAProfActnProtAlgSigHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnProtAlgSigHash.setStatus("current")


class _TmnxPkiCAProfActnSubjectDn_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnSubjectDn based on DisplayString"""
    defaultHexValue = ""


_TmnxPkiCAProfActnSubjectDn_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnSubjectDn_Object = MibTableColumn
tmnxPkiCAProfActnSubjectDn = _TmnxPkiCAProfActnSubjectDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 8),
    _TmnxPkiCAProfActnSubjectDn_Type()
)
tmnxPkiCAProfActnSubjectDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnSubjectDn.setStatus("current")


class _TmnxPkiCAProfActnSaveAsFile_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnSaveAsFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_TmnxPkiCAProfActnSaveAsFile_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnSaveAsFile_Object = MibTableColumn
tmnxPkiCAProfActnSaveAsFile = _TmnxPkiCAProfActnSaveAsFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 9),
    _TmnxPkiCAProfActnSaveAsFile_Type()
)
tmnxPkiCAProfActnSaveAsFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnSaveAsFile.setStatus("current")


class _TmnxPkiCAProfActnNewKey_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnNewKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TmnxPkiCAProfActnNewKey_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnNewKey_Object = MibTableColumn
tmnxPkiCAProfActnNewKey = _TmnxPkiCAProfActnNewKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 10),
    _TmnxPkiCAProfActnNewKey_Type()
)
tmnxPkiCAProfActnNewKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnNewKey.setStatus("current")


class _TmnxPkiCAProfActnStatus_Type(Integer32):
    """Custom type tmnxPkiCAProfActnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processed", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_TmnxPkiCAProfActnStatus_Type.__name__ = "Integer32"
_TmnxPkiCAProfActnStatus_Object = MibTableColumn
tmnxPkiCAProfActnStatus = _TmnxPkiCAProfActnStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 11),
    _TmnxPkiCAProfActnStatus_Type()
)
tmnxPkiCAProfActnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnStatus.setStatus("current")
_TmnxPkiCAProfActnStatusString_Type = DisplayString
_TmnxPkiCAProfActnStatusString_Object = MibTableColumn
tmnxPkiCAProfActnStatusString = _TmnxPkiCAProfActnStatusString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 12),
    _TmnxPkiCAProfActnStatusString_Type()
)
tmnxPkiCAProfActnStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnStatusString.setStatus("current")


class _TmnxPkiCAProfActnStatusCode_Type(Integer32):
    """Custom type tmnxPkiCAProfActnStatusCode based on Integer32"""
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
        *(("none", 0),
          ("accepted", 1),
          ("grantedWithMods", 2),
          ("rejection", 3),
          ("waiting", 4),
          ("revocationWarning", 5),
          ("revocationNotification", 6),
          ("keyUpdateWarning", 7))
    )


_TmnxPkiCAProfActnStatusCode_Type.__name__ = "Integer32"
_TmnxPkiCAProfActnStatusCode_Object = MibTableColumn
tmnxPkiCAProfActnStatusCode = _TmnxPkiCAProfActnStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 13),
    _TmnxPkiCAProfActnStatusCode_Type()
)
tmnxPkiCAProfActnStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnStatusCode.setStatus("current")
_TmnxPkiCAProfActnOrigCmdTime_Type = DateAndTime
_TmnxPkiCAProfActnOrigCmdTime_Object = MibTableColumn
tmnxPkiCAProfActnOrigCmdTime = _TmnxPkiCAProfActnOrigCmdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 14),
    _TmnxPkiCAProfActnOrigCmdTime_Type()
)
tmnxPkiCAProfActnOrigCmdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnOrigCmdTime.setStatus("current")
_TmnxPkiCAProfActnLastCAResp_Type = DateAndTime
_TmnxPkiCAProfActnLastCAResp_Object = MibTableColumn
tmnxPkiCAProfActnLastCAResp = _TmnxPkiCAProfActnLastCAResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 15),
    _TmnxPkiCAProfActnLastCAResp_Type()
)
tmnxPkiCAProfActnLastCAResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnLastCAResp.setStatus("current")


class _TmnxPkiCAProfActnSendChain_Type(TruthValue):
    """Custom type tmnxPkiCAProfActnSendChain based on TruthValue"""
    defaultValue = 2


_TmnxPkiCAProfActnSendChain_Type.__name__ = "TruthValue"
_TmnxPkiCAProfActnSendChain_Object = MibTableColumn
tmnxPkiCAProfActnSendChain = _TmnxPkiCAProfActnSendChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 16),
    _TmnxPkiCAProfActnSendChain_Type()
)
tmnxPkiCAProfActnSendChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnSendChain.setStatus("current")


class _TmnxPkiCAProfActnSendChainCA_Type(TNamedItemOrEmpty):
    """Custom type tmnxPkiCAProfActnSendChainCA based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPkiCAProfActnSendChainCA_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPkiCAProfActnSendChainCA_Object = MibTableColumn
tmnxPkiCAProfActnSendChainCA = _TmnxPkiCAProfActnSendChainCA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 17),
    _TmnxPkiCAProfActnSendChainCA_Type()
)
tmnxPkiCAProfActnSendChainCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnSendChainCA.setStatus("current")


class _TmnxPkiCAProfActnProtKey_Type(DisplayString):
    """Custom type tmnxPkiCAProfActnProtKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TmnxPkiCAProfActnProtKey_Type.__name__ = "DisplayString"
_TmnxPkiCAProfActnProtKey_Object = MibTableColumn
tmnxPkiCAProfActnProtKey = _TmnxPkiCAProfActnProtKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 18, 22, 1, 18),
    _TmnxPkiCAProfActnProtKey_Type()
)
tmnxPkiCAProfActnProtKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnProtKey.setStatus("current")
_TmnxCertMgrStatsGroup_ObjectIdentity = ObjectIdentity
tmnxCertMgrStatsGroup = _TmnxCertMgrStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 19)
)
_TmnxCertMgrAuthFailed_Type = Counter32
_TmnxCertMgrAuthFailed_Object = MibScalar
tmnxCertMgrAuthFailed = _TmnxCertMgrAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 19, 1),
    _TmnxCertMgrAuthFailed_Type()
)
tmnxCertMgrAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCertMgrAuthFailed.setStatus("current")
_TmnxCertMgrAuthPassed_Type = Counter32
_TmnxCertMgrAuthPassed_Object = MibScalar
tmnxCertMgrAuthPassed = _TmnxCertMgrAuthPassed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 19, 2),
    _TmnxCertMgrAuthPassed_Type()
)
tmnxCertMgrAuthPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCertMgrAuthPassed.setStatus("current")
_TmnxCertMgrTotalAuth_Type = Counter32
_TmnxCertMgrTotalAuth_Object = MibScalar
tmnxCertMgrTotalAuth = _TmnxCertMgrTotalAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 19, 3),
    _TmnxCertMgrTotalAuth_Type()
)
tmnxCertMgrTotalAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCertMgrTotalAuth.setStatus("current")
_TmnxUserPublicKeyObjects_ObjectIdentity = ObjectIdentity
tmnxUserPublicKeyObjects = _TmnxUserPublicKeyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20)
)
_TmnxUserPublicKeyTable_Object = MibTable
tmnxUserPublicKeyTable = _TmnxUserPublicKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxUserPublicKeyTable.setStatus("current")
_TmnxUserPublicKeyEntry_Object = MibTableRow
tmnxUserPublicKeyEntry = _TmnxUserPublicKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20, 1, 1)
)
tmnxUserPublicKeyEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxUserName"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxUserPublicKeyNumber"),
)
if mibBuilder.loadTexts:
    tmnxUserPublicKeyEntry.setStatus("current")


class _TmnxUserPublicKeyNumber_Type(Unsigned32):
    """Custom type tmnxUserPublicKeyNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxUserPublicKeyNumber_Type.__name__ = "Unsigned32"
_TmnxUserPublicKeyNumber_Object = MibTableColumn
tmnxUserPublicKeyNumber = _TmnxUserPublicKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20, 1, 1, 1),
    _TmnxUserPublicKeyNumber_Type()
)
tmnxUserPublicKeyNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxUserPublicKeyNumber.setStatus("current")
_TmnxUserPublicKeyRowStatus_Type = RowStatus
_TmnxUserPublicKeyRowStatus_Object = MibTableColumn
tmnxUserPublicKeyRowStatus = _TmnxUserPublicKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20, 1, 1, 2),
    _TmnxUserPublicKeyRowStatus_Type()
)
tmnxUserPublicKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserPublicKeyRowStatus.setStatus("current")
_TmnxUserPublicKeyLastChanged_Type = TimeStamp
_TmnxUserPublicKeyLastChanged_Object = MibTableColumn
tmnxUserPublicKeyLastChanged = _TmnxUserPublicKeyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20, 1, 1, 3),
    _TmnxUserPublicKeyLastChanged_Type()
)
tmnxUserPublicKeyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxUserPublicKeyLastChanged.setStatus("current")


class _TmnxUserPublicKeyName_Type(DisplayString):
    """Custom type tmnxUserPublicKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxUserPublicKeyName_Type.__name__ = "DisplayString"
_TmnxUserPublicKeyName_Object = MibTableColumn
tmnxUserPublicKeyName = _TmnxUserPublicKeyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 20, 1, 1, 4),
    _TmnxUserPublicKeyName_Type()
)
tmnxUserPublicKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxUserPublicKeyName.setStatus("current")
_TmnxUserActionObjs_ObjectIdentity = ObjectIdentity
tmnxUserActionObjs = _TmnxUserActionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 21)
)
_TmnxUserActionUserName_Type = TNamedItemOrEmpty
_TmnxUserActionUserName_Object = MibScalar
tmnxUserActionUserName = _TmnxUserActionUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 21, 1),
    _TmnxUserActionUserName_Type()
)
tmnxUserActionUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxUserActionUserName.setStatus("current")
_TmnxUserActionUnlock_Type = TmnxActionType
_TmnxUserActionUnlock_Object = MibScalar
tmnxUserActionUnlock = _TmnxUserActionUnlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 21, 2),
    _TmnxUserActionUnlock_Type()
)
tmnxUserActionUnlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxUserActionUnlock.setStatus("current")
_TmnxUserActionClearPwdHistory_Type = TmnxActionType
_TmnxUserActionClearPwdHistory_Object = MibScalar
tmnxUserActionClearPwdHistory = _TmnxUserActionClearPwdHistory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 21, 3),
    _TmnxUserActionClearPwdHistory_Type()
)
tmnxUserActionClearPwdHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxUserActionClearPwdHistory.setStatus("current")
_TmnxTacPlusPrivLvlMapTable_Object = MibTable
tmnxTacPlusPrivLvlMapTable = _TmnxTacPlusPrivLvlMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 22)
)
if mibBuilder.loadTexts:
    tmnxTacPlusPrivLvlMapTable.setStatus("current")
_TmnxTacPlusPrivLvlMapEntry_Object = MibTableRow
tmnxTacPlusPrivLvlMapEntry = _TmnxTacPlusPrivLvlMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 22, 1)
)
tmnxTacPlusPrivLvlMapEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxTacPlusPrivLvlMapPrivLvl"),
)
if mibBuilder.loadTexts:
    tmnxTacPlusPrivLvlMapEntry.setStatus("current")


class _TmnxTacPlusPrivLvlMapPrivLvl_Type(Unsigned32):
    """Custom type tmnxTacPlusPrivLvlMapPrivLvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxTacPlusPrivLvlMapPrivLvl_Type.__name__ = "Unsigned32"
_TmnxTacPlusPrivLvlMapPrivLvl_Object = MibTableColumn
tmnxTacPlusPrivLvlMapPrivLvl = _TmnxTacPlusPrivLvlMapPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 22, 1, 1),
    _TmnxTacPlusPrivLvlMapPrivLvl_Type()
)
tmnxTacPlusPrivLvlMapPrivLvl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTacPlusPrivLvlMapPrivLvl.setStatus("current")
_TmnxTacPlusPrivLvlRowStatus_Type = RowStatus
_TmnxTacPlusPrivLvlRowStatus_Object = MibTableColumn
tmnxTacPlusPrivLvlRowStatus = _TmnxTacPlusPrivLvlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 22, 1, 2),
    _TmnxTacPlusPrivLvlRowStatus_Type()
)
tmnxTacPlusPrivLvlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusPrivLvlRowStatus.setStatus("current")
_TmnxTacPlusPrivLvlMapUserProfile_Type = TNamedItem
_TmnxTacPlusPrivLvlMapUserProfile_Object = MibTableColumn
tmnxTacPlusPrivLvlMapUserProfile = _TmnxTacPlusPrivLvlMapUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 22, 1, 3),
    _TmnxTacPlusPrivLvlMapUserProfile_Type()
)
tmnxTacPlusPrivLvlMapUserProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTacPlusPrivLvlMapUserProfile.setStatus("current")
_TmnxOcspCacheTable_Object = MibTable
tmnxOcspCacheTable = _TmnxOcspCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23)
)
if mibBuilder.loadTexts:
    tmnxOcspCacheTable.setStatus("current")
_TmnxOcspCacheEntry_Object = MibTableRow
tmnxOcspCacheEntry = _TmnxOcspCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23, 1)
)
tmnxOcspCacheEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxOcspCacheEntryId"),
)
if mibBuilder.loadTexts:
    tmnxOcspCacheEntry.setStatus("current")
_TmnxOcspCacheEntryId_Type = Integer32
_TmnxOcspCacheEntryId_Object = MibTableColumn
tmnxOcspCacheEntryId = _TmnxOcspCacheEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23, 1, 1),
    _TmnxOcspCacheEntryId_Type()
)
tmnxOcspCacheEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOcspCacheEntryId.setStatus("current")


class _TmnxOcspCacheCertSerial_Type(OctetString):
    """Custom type tmnxOcspCacheCertSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TmnxOcspCacheCertSerial_Type.__name__ = "OctetString"
_TmnxOcspCacheCertSerial_Object = MibTableColumn
tmnxOcspCacheCertSerial = _TmnxOcspCacheCertSerial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23, 1, 2),
    _TmnxOcspCacheCertSerial_Type()
)
tmnxOcspCacheCertSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOcspCacheCertSerial.setStatus("current")
_TmnxOcspCacheCertIssuer_Type = TLDisplayString
_TmnxOcspCacheCertIssuer_Object = MibTableColumn
tmnxOcspCacheCertIssuer = _TmnxOcspCacheCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23, 1, 3),
    _TmnxOcspCacheCertIssuer_Type()
)
tmnxOcspCacheCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOcspCacheCertIssuer.setStatus("current")
_TmnxOcspCacheExpiry_Type = Unsigned32
_TmnxOcspCacheExpiry_Object = MibTableColumn
tmnxOcspCacheExpiry = _TmnxOcspCacheExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23, 1, 4),
    _TmnxOcspCacheExpiry_Type()
)
tmnxOcspCacheExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOcspCacheExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOcspCacheExpiry.setUnits("seconds")


class _TmnxOcspCacheCertStatus_Type(Integer32):
    """Custom type tmnxOcspCacheCertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("valid", 0),
          ("revoked", 1))
    )


_TmnxOcspCacheCertStatus_Type.__name__ = "Integer32"
_TmnxOcspCacheCertStatus_Object = MibTableColumn
tmnxOcspCacheCertStatus = _TmnxOcspCacheCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 23, 1, 5),
    _TmnxOcspCacheCertStatus_Type()
)
tmnxOcspCacheCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOcspCacheCertStatus.setStatus("current")
_TmnxSecurityTech_ObjectIdentity = ObjectIdentity
tmnxSecurityTech = _TmnxSecurityTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 24)
)


class _TmnxSecurityTechSupportLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxSecurityTechSupportLocation based on TmnxDisplayStringURL"""
    defaultValue = OctetString("")


_TmnxSecurityTechSupportLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxSecurityTechSupportLocation_Object = MibScalar
tmnxSecurityTechSupportLocation = _TmnxSecurityTechSupportLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 24, 1),
    _TmnxSecurityTechSupportLocation_Type()
)
tmnxSecurityTechSupportLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSecurityTechSupportLocation.setStatus("current")
_TmnxSSHCipherTable_Object = MibTable
tmnxSSHCipherTable = _TmnxSSHCipherTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 25)
)
if mibBuilder.loadTexts:
    tmnxSSHCipherTable.setStatus("current")
_TmnxSSHCipherEntry_Object = MibTableRow
tmnxSSHCipherEntry = _TmnxSSHCipherEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 25, 1)
)
tmnxSSHCipherEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxSSHCipherProtocolVersion"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxSSHCipherNumber"),
)
if mibBuilder.loadTexts:
    tmnxSSHCipherEntry.setStatus("current")


class _TmnxSSHCipherProtocolVersion_Type(Integer32):
    """Custom type tmnxSSHCipherProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TmnxSSHCipherProtocolVersion_Type.__name__ = "Integer32"
_TmnxSSHCipherProtocolVersion_Object = MibTableColumn
tmnxSSHCipherProtocolVersion = _TmnxSSHCipherProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 25, 1, 1),
    _TmnxSSHCipherProtocolVersion_Type()
)
tmnxSSHCipherProtocolVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSSHCipherProtocolVersion.setStatus("current")
_TmnxSSHCipherNumber_Type = TSSHCipherNumber
_TmnxSSHCipherNumber_Object = MibTableColumn
tmnxSSHCipherNumber = _TmnxSSHCipherNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 25, 1, 2),
    _TmnxSSHCipherNumber_Type()
)
tmnxSSHCipherNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSSHCipherNumber.setStatus("current")


class _TmnxSSHCipherName_Type(DisplayString):
    """Custom type tmnxSSHCipherName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxSSHCipherName_Type.__name__ = "DisplayString"
_TmnxSSHCipherName_Object = MibTableColumn
tmnxSSHCipherName = _TmnxSSHCipherName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 25, 1, 3),
    _TmnxSSHCipherName_Type()
)
tmnxSSHCipherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSSHCipherName.setStatus("current")
_TmnxSSHServerCipherListTable_Object = MibTable
tmnxSSHServerCipherListTable = _TmnxSSHServerCipherListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 26)
)
if mibBuilder.loadTexts:
    tmnxSSHServerCipherListTable.setStatus("current")
_TmnxSSHServerCipherListEntry_Object = MibTableRow
tmnxSSHServerCipherListEntry = _TmnxSSHServerCipherListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 26, 1)
)
tmnxSSHServerCipherListEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxSSHCipherProtocolVersion"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxSSHServerCipherListIndex"),
)
if mibBuilder.loadTexts:
    tmnxSSHServerCipherListEntry.setStatus("current")


class _TmnxSSHServerCipherListIndex_Type(Integer32):
    """Custom type tmnxSSHServerCipherListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxSSHServerCipherListIndex_Type.__name__ = "Integer32"
_TmnxSSHServerCipherListIndex_Object = MibTableColumn
tmnxSSHServerCipherListIndex = _TmnxSSHServerCipherListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 26, 1, 1),
    _TmnxSSHServerCipherListIndex_Type()
)
tmnxSSHServerCipherListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSSHServerCipherListIndex.setStatus("current")
_TmnxSSHServerCipherListRowStatus_Type = RowStatus
_TmnxSSHServerCipherListRowStatus_Object = MibTableColumn
tmnxSSHServerCipherListRowStatus = _TmnxSSHServerCipherListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 26, 1, 2),
    _TmnxSSHServerCipherListRowStatus_Type()
)
tmnxSSHServerCipherListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSSHServerCipherListRowStatus.setStatus("current")


class _TmnxSSHServerCipherListNumber_Type(TSSHCipherNumber):
    """Custom type tmnxSSHServerCipherListNumber based on TSSHCipherNumber"""
    defaultValue = 0


_TmnxSSHServerCipherListNumber_Type.__name__ = "TSSHCipherNumber"
_TmnxSSHServerCipherListNumber_Object = MibTableColumn
tmnxSSHServerCipherListNumber = _TmnxSSHServerCipherListNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 26, 1, 3),
    _TmnxSSHServerCipherListNumber_Type()
)
tmnxSSHServerCipherListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSSHServerCipherListNumber.setStatus("current")
_TmnxSSHClientCipherListTable_Object = MibTable
tmnxSSHClientCipherListTable = _TmnxSSHClientCipherListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 27)
)
if mibBuilder.loadTexts:
    tmnxSSHClientCipherListTable.setStatus("current")
_TmnxSSHClientCipherListEntry_Object = MibTableRow
tmnxSSHClientCipherListEntry = _TmnxSSHClientCipherListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 27, 1)
)
tmnxSSHClientCipherListEntry.setIndexNames(
    (0, "TIMETRA-SECURITY-MIB", "tmnxSSHCipherProtocolVersion"),
    (0, "TIMETRA-SECURITY-MIB", "tmnxSSHClientCipherListIndex"),
)
if mibBuilder.loadTexts:
    tmnxSSHClientCipherListEntry.setStatus("current")


class _TmnxSSHClientCipherListIndex_Type(Integer32):
    """Custom type tmnxSSHClientCipherListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxSSHClientCipherListIndex_Type.__name__ = "Integer32"
_TmnxSSHClientCipherListIndex_Object = MibTableColumn
tmnxSSHClientCipherListIndex = _TmnxSSHClientCipherListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 27, 1, 1),
    _TmnxSSHClientCipherListIndex_Type()
)
tmnxSSHClientCipherListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSSHClientCipherListIndex.setStatus("current")
_TmnxSSHClientCipherListRowStatus_Type = RowStatus
_TmnxSSHClientCipherListRowStatus_Object = MibTableColumn
tmnxSSHClientCipherListRowStatus = _TmnxSSHClientCipherListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 27, 1, 2),
    _TmnxSSHClientCipherListRowStatus_Type()
)
tmnxSSHClientCipherListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSSHClientCipherListRowStatus.setStatus("current")


class _TmnxSSHClientCipherListNumber_Type(TSSHCipherNumber):
    """Custom type tmnxSSHClientCipherListNumber based on TSSHCipherNumber"""
    defaultValue = 0


_TmnxSSHClientCipherListNumber_Type.__name__ = "TSSHCipherNumber"
_TmnxSSHClientCipherListNumber_Object = MibTableColumn
tmnxSSHClientCipherListNumber = _TmnxSSHClientCipherListNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 22, 27, 1, 3),
    _TmnxSSHClientCipherListNumber_Type()
)
tmnxSSHClientCipherListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSSHClientCipherListNumber.setStatus("current")
_TmnxSecurityNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSecurityNotifyPrefix = _TmnxSecurityNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22)
)
_TmnxSecurityNotifications_ObjectIdentity = ObjectIdentity
tmnxSecurityNotifications = _TmnxSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0)
)

# Managed Objects groups

tmnxSecurityUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 1)
)
tmnxSecurityUserGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxUserProfileRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchString"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordEncrypted"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleLoginExecFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleCannotChangePswd"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleNewPswdAtLogin"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile1"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile2"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile3"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile4"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile5"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile6"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile7"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile8"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAttemptedLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserSuccessfulLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordChanged"))
)
if mibBuilder.loadTexts:
    tmnxSecurityUserGroup.setStatus("obsolete")

tmnxSecurityMafR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 6)
)
tmnxSecurityMafR2r1Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxMafRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafAdminState"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcIpAddr"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcIpMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcPortType"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcPortId"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchDestPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchProtocol"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchCount"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchRouter"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchLog"))
)
if mibBuilder.loadTexts:
    tmnxSecurityMafR2r1Group.setStatus("obsolete")

tmnxSecurityPasswordsR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 7)
)
tmnxSecurityPasswordsR2r1Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPasswordAging"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordMinLength"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordComplexity"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsCount"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsLockoutPeriod"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder1"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder2"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder3"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenExitOnReject"),
        ("TIMETRA-SECURITY-MIB", "tmnxAdminPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxAdminPasswordEncrypted"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordHealthCheck"))
)
if mibBuilder.loadTexts:
    tmnxSecurityPasswordsR2r1Group.setStatus("obsolete")

tmnxSecurityCpmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 11)
)
tmnxSecurityCpmGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmPerPeerQueuing"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmQueuesTotal"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmQueuesInUse"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmGroup.setStatus("current")

tmnxSecurityPasswordHashGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 12)
)
tmnxSecurityPasswordHashGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPassHashReadVersion"),
        ("TIMETRA-SECURITY-MIB", "tmnxPassHashWriteVersion"))
)
if mibBuilder.loadTexts:
    tmnxSecurityPasswordHashGroup.setStatus("current")

tmnxSecurityCpmIpFilterV3v0r2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 17)
)
tmnxSecurityCpmIpFilterV3v0r2Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmFilterQueueRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueAdminPIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueAdminCIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueCBS"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueMBS"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueReferences"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterAdminState"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLogId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDescription"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryQueueId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryProtocol"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDSCP"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryFragment"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryOptionPresent"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIPOptionValue"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIPOptionMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryMultipleOption"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryTcpSyn"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryTcpAck"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIcmpCode"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIcmpType"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryVRtrId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLogCreated"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterStatsDroppedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterStatsForwardedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileDropPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileFwdPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileDropOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileFwdOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileDropPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileFwdPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileDropOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileFwdOctets"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmIpFilterV3v0r2Group.setStatus("obsolete")

tmnxSecurityCpmIPv6FilterV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 18)
)
tmnxSecurityCpmIPv6FilterV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryLogId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDescription"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryQueueId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryNextHeader"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDSCP"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryTcpSyn"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryTcpAck"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryIcmpCode"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryIcmpType"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryVRtrId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryLogCreated"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryFlowLabel"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterStatsDroppedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterStatsForwardedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterAdminState"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmIPv6FilterV4v0Group.setStatus("obsolete")

tmnxSecurityServerCtlV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 19)
)
tmnxSecurityServerCtlV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxEnableServers"),
        ("TIMETRA-SECURITY-MIB", "tmnxTelnetServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxFTPServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTelnet6ServerOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSecurityServerCtlV4v0Group.setStatus("current")

tmnxSSHServerV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 20)
)
tmnxSSHServerV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSSHServerPreserveKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerVersion"))
)
if mibBuilder.loadTexts:
    tmnxSSHServerV4v0Group.setStatus("current")

tmnxSecuritySourceIpV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 21)
)
tmnxSecuritySourceIpV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSourceIPRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxSourceIPAddressType"),
        ("TIMETRA-SECURITY-MIB", "tmnxSourceIPAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxSourceIPIfIndex"),
        ("TIMETRA-SECURITY-MIB", "tmnxSourceIPOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSecuritySourceIpV4v0Group.setStatus("current")

tmnxSecurityRadiusV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 22)
)
tmnxSecurityRadiusV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxRadiusAdminStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusAccounting"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusAuthorization"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusRetryAttempts"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerSecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusConfigured"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEDiscovery"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEDiscoveryPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEDiscoveryInterval"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEForceDiscovery"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEForceDiscoverySvcId"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusAccountingPort"))
)
if mibBuilder.loadTexts:
    tmnxSecurityRadiusV4v0Group.setStatus("obsolete")

tmnxSecurityTacPlusV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 23)
)
tmnxSecurityTacPlusV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxTacPlusAdminStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerSecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAccounting"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAcctRecType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAuthorization"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusSingleConnection"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusConfigured"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacplusUseTemplate"))
)
if mibBuilder.loadTexts:
    tmnxSecurityTacPlusV4v0Group.setStatus("obsolete")

tmnxSecurityObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 24)
)
tmnxSecurityObsoleteGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxRadiusSourceAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusSourceAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEDiscovery"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEDiscoveryPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEDiscoveryInterval"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordComplexity"))
)
if mibBuilder.loadTexts:
    tmnxSecurityObsoleteGroup.setStatus("current")

tmnxSecurityUserV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 25)
)
tmnxSecurityUserV4v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxUserProfileRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchString"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordEncrypted"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleLoginExecFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleCannotChangePswd"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleNewPswdAtLogin"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile1"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile2"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile3"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile4"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile5"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile6"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile7"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile8"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAttemptedLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserSuccessfulLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateConsoleLoginExecFile"))
)
if mibBuilder.loadTexts:
    tmnxSecurityUserV4v0Group.setStatus("obsolete")

tmnxSecurityKeyChainV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 26)
)
tmnxSecurityKeyChainV5v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxKeyChainRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainReceiveTcpOptionNum"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainSendTcpOptionNum"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAdminState"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainOperState"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthenticationKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyAlgorithm"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyBeginTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyEndTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyTolerance"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyAdminState"))
)
if mibBuilder.loadTexts:
    tmnxSecurityKeyChainV5v0Group.setStatus("current")

tmnxSecurityRadiusV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 27)
)
tmnxSecurityRadiusV5v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxRadiusAdminStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusAccounting"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusAuthorization"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerSecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusRetryAttempts"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusConfigured"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEForceDiscovery"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusPEForceDiscoverySvcId"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusAccountingPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerInetAddressType"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusServerInetAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUseTemplate"))
)
if mibBuilder.loadTexts:
    tmnxSecurityRadiusV5v0Group.setStatus("current")

tmnxSecurityTacPlusV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 28)
)
tmnxSecurityTacPlusV5v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxTacPlusAdminStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerSecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAccounting"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAcctRecType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAuthorization"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusSingleConnection"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusConfigured"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacplusUseTemplate"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerInetAddressType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSecurityTacPlusV5v0Group.setStatus("obsolete")

tmnxSecurityCpmIpFilterV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 29)
)
tmnxSecurityCpmIpFilterV5v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmFilterQueueRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueAdminPIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueAdminCIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueCBS"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueMBS"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueReferences"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueOperPIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueOperCIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterAdminState"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLogId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDescription"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryQueueId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryProtocol"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDSCP"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryFragment"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryOptionPresent"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIPOptionValue"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIPOptionMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryMultipleOption"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryTcpSyn"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryTcpAck"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIcmpCode"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIcmpType"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryVRtrId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLogCreated"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterStatsDroppedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterStatsForwardedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileDropPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileFwdPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileDropOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileFwdOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileDropPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileFwdPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileDropOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileFwdOctets"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmIpFilterV5v0Group.setStatus("obsolete")

tmnxSecurityNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 31)
)
tmnxSecurityNotifyObjsGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthFailReason"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthAddrType"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthAddr"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNotifyObjsGroup.setStatus("current")

tmnxSecurityTacPlusV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 32)
)
tmnxSecurityTacPlusV6v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxTacPlusAdminStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerSecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAccounting"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAcctRecType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAuthorization"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusSingleConnection"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusConfigured"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacplusUseTemplate"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerInetAddressType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerInetAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerPort"))
)
if mibBuilder.loadTexts:
    tmnxSecurityTacPlusV6v0Group.setStatus("obsolete")

tmnxSecurityPasswordsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 33)
)
tmnxSecurityPasswordsV6v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPasswordAging"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordMinLength"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordComplexity"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsCount"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsLockoutPeriod"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder1"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder2"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder3"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenExitOnReject"),
        ("TIMETRA-SECURITY-MIB", "tmnxAdminPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxAdminPasswordEncrypted"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordHealthCheck"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordHealthCheckInterval"))
)
if mibBuilder.loadTexts:
    tmnxSecurityPasswordsV6v0Group.setStatus("obsolete")

tmnxSecurityMafV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 34)
)
tmnxSecurityMafV6v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxGenMafTableLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafIPMatchTableLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxGenMafLastModified"),
        ("TIMETRA-SECURITY-MIB", "tmnxGenMafRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxGenMafAdminState"),
        ("TIMETRA-SECURITY-MIB", "tmnxGenMafDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchSrcIpAddrType"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchSrcIpAddr"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchSrcIpMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchSrcPortType"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchSrcPortId"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchDestPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchProtNxtHdr"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchCount"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchRouter"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchFlowLabel"),
        ("TIMETRA-SECURITY-MIB", "tmnxIPMafMatchLog"))
)
if mibBuilder.loadTexts:
    tmnxSecurityMafV6v0Group.setStatus("current")

tmnxObsoletedObjectsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 35)
)
tmnxObsoletedObjectsV6v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxMafRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafAdminState"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcIpAddr"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcIpMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcPortType"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchSrcPortId"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchDestPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchProtocol"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchCount"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchRouter"),
        ("TIMETRA-SECURITY-MIB", "tmnxMafMatchLog"))
)
if mibBuilder.loadTexts:
    tmnxObsoletedObjectsV6v0Group.setStatus("current")

tmnxSecurityCpmProtectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 36)
)
tmnxSecurityCpmProtectGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolTableLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolPerSrcRateLimit"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolOverallRateLimit"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolAlarm"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolOutProfileRate"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtDropUncfgdProtocolMsg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtLinkRateLimit"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdTableLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdTimeStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortTableLastChgd"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortTimeStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortAggPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortAggTimeStart"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortAggTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIfTableLastChgd"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIfPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIfTimeStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIfTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSapTableLastChgd"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSapPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSapTimeStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSapTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPortOverallRateLimit"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtDetectPeriod"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmProtectGroup.setStatus("current")

tmnxSecurityLiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 37)
)
tmnxSecurityLiGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxUserProfileLi")
)
if mibBuilder.loadTexts:
    tmnxSecurityLiGroup.setStatus("current")

tmnxSecurityCpmProtNotificationObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 39)
)
tmnxSecurityCpmProtNotificationObjsGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolMacAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolMacPeriods"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmProtNotificationObjsGroup.setStatus("current")

tmnxSecurityCpmMacFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 40)
)
tmnxSecurityCpmMacFilterGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmMacFilterAdminState"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryLogId"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDescription"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryQueueId"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryFrameType"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntrySvcId"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDot1pValue"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDot1pMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDsap"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDsapMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntrySrcMAC"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntrySrcMACMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDstMAC"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryDstMACMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryEtherType"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntrySsap"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntrySsapMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryCfmOpCodeOper"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryCfmOpCodeValue1"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryCfmOpCodeValue2"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFltrEntryLogCreated"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFilterStatsDroppedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmMacFilterStatsForwardedPkts"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmMacFilterGroup.setStatus("current")

tmnxSecurityMafMacFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 41)
)
tmnxSecurityMafMacFilterGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxMafMacMatchTableLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchLog"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchFrameType"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSvcId"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDot1pValue"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDot1pMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDsap"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDsapMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSrcMAC"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSrcMACMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDstMAC"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchDstMACMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchEtherType"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSnapOui"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSnapPid"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSsap"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchSsapMask"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchCfmOpCodeOper"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchCfmOpCodeValue1"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchCfmOpCodeValue2"),
        ("TIMETRA-SECURITY-MIB", "tmnxMacMafMatchCount"))
)
if mibBuilder.loadTexts:
    tmnxSecurityMafMacFilterGroup.setStatus("current")

tmnxSecurityUserV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 42)
)
tmnxSecurityUserV6v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxUserProfileRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchString"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordEncrypted"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleLoginExecFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleCannotChangePswd"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleNewPswdAtLogin"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile1"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile2"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile3"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile4"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile5"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile6"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile7"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile8"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAttemptedLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserSuccessfulLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateConsoleLoginExecFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateProfile"))
)
if mibBuilder.loadTexts:
    tmnxSecurityUserV6v0Group.setStatus("obsolete")

tmnxSecurityRadiusAuthV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 43)
)
tmnxSecurityRadiusAuthV5v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxRadiusAuthAlgorithm")
)
if mibBuilder.loadTexts:
    tmnxSecurityRadiusAuthV5v0Group.setStatus("current")

tmnxSecurityV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 44)
)
tmnxSecurityV7v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtAllowShamLinkPackets"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcTimeStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcVrtrIfIndex"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrTimeStart"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrSvcId"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxSecurityV7v0Group.setStatus("current")

tmnxSecurityTacPlusV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 46)
)
tmnxSecurityTacPlusV8v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxTacPlusAdminStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerSecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerOperStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAccounting"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAcctRecType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusAuthorization"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusConfigured"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacplusUseTemplate"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerInetAddressType"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerInetAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusServerPort"))
)
if mibBuilder.loadTexts:
    tmnxSecurityTacPlusV8v0Group.setStatus("current")

tmnxObsoletedObjectsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 47)
)
tmnxObsoletedObjectsV8v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxTacPlusSingleConnection")
)
if mibBuilder.loadTexts:
    tmnxObsoletedObjectsV8v0Group.setStatus("current")

tmnxSecurityNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 48)
)
tmnxSecurityNotifyObjsV8v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxMD5AuthFailReason"),
        ("TIMETRA-SECURITY-MIB", "tmnxMD5AuthAddrType"),
        ("TIMETRA-SECURITY-MIB", "tmnxMD5AuthAddr"),
        ("TIMETRA-SECURITY-MIB", "tmnxMD5AuthKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolId"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNotifyObjsV8v0Group.setStatus("current")

tmnxCpmProtEthCfmPolV8v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 50)
)
tmnxCpmProtEthCfmPolV8v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolTableLastChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolLevelSet"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolOpCodeSet"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolRateLimit"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmTblLChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmTblLChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmTime"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtEthCfmPolV8v0Grp.setStatus("current")

tmnxCpmProtPolV8v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 51)
)
tmnxCpmProtPolV8v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBindTblLastChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBindPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBindTimeStartd"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBindTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindTblLastChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindTimeStartd"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindTime"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtPolV8v0Grp.setStatus("current")

tmnxSecPkiV9v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 53)
)
tmnxSecPkiV9v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileAdminState"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileCRLFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileCertFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileDescr"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileTableLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiMaxCertChainDepth"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileOperFlags"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileOperState"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertMgrAuthFailed"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertMgrAuthPassed"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertMgrTotalAuth"))
)
if mibBuilder.loadTexts:
    tmnxSecPkiV9v0Grp.setStatus("current")

tmnxSecurityNwExceptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 54)
)
tmnxSecurityNwExceptionsGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmVprnNwExceptions"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmNumVprnNwExceptions"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmVprnNwExceptionsTime"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNwExceptionsGroup.setStatus("current")

tmnxSecNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 56)
)
tmnxSecNotifyObjsV10v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecNotifCert"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFailureReason"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifTunnelName"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifyObjsV10v0Group.setStatus("current")

tmnxRadiusUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 57)
)
tmnxRadiusUserGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxRadiusUserAcctConnError"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserAcctRejRx"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserAcctReqTx"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserBindFail"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserLoginFail"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserLoginPass"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserMd5Fail"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserOpenFail"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserPending"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserRecvFail"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserReqRx"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserReqTx"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserSendFail"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserSendTimeout"))
)
if mibBuilder.loadTexts:
    tmnxRadiusUserGroup.setStatus("current")

tmnxCpmProtExcdSapIpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 58)
)
tmnxCpmProtExcdSapIpV9v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpTableLastChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolLimDhcpCiAddrZero"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIpV9v0Group.setStatus("current")

tmnxCpmFltrPrefixListV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 60)
)
tmnxCpmFltrPrefixListV10v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIpPrefixList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDstIpPrefixList"))
)
if mibBuilder.loadTexts:
    tmnxCpmFltrPrefixListV10v0Group.setStatus("obsolete")

tmnxRadiusUserExGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 61)
)
tmnxRadiusUserExGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserAccChallengePkt")
)
if mibBuilder.loadTexts:
    tmnxRadiusUserExGroup.setStatus("current")

tmnxSecurityUserActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 62)
)
tmnxSecurityUserActionGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxUserActionUserName"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserActionUnlock"))
)
if mibBuilder.loadTexts:
    tmnxSecurityUserActionGroup.setStatus("current")

tmnxCpmFltrPrefixListV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 63)
)
tmnxCpmFltrPrefixListV11v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIpPrefixList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDstIpPrefixList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcIpPfxList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDstIpPfxList"))
)
if mibBuilder.loadTexts:
    tmnxCpmFltrPrefixListV11v0Group.setStatus("current")

tmnxSecurityCpmIpFilterV11v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 64)
)
tmnxSecurityCpmIpFilterV11v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmFilterQueueRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueAdminPIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueAdminCIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueCBS"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueMBS"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueReferences"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueOperPIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQueueOperCIR"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterAdminState"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLogId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDescription"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryQueueId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryProtocol"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDSCP"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryFragment"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryOptionPresent"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIPOptionValue"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIPOptionMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryMultipleOption"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryTcpSyn"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryTcpAck"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIcmpCode"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryIcmpType"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryVRtrId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryLogCreated"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterStatsDroppedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterStatsForwardedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileDropPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileFwdPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileDropOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQInProfileFwdOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileDropPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileFwdPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileDropOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmFilterQOutProfileFwdOctets"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPortHigh"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPortOper"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPortHigh"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDestPortOper"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntrySrcPortList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryDstPortList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIpFilterEntryPortSelector"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmIpFilterV11v0Grp.setStatus("current")

tmnxSecurityCpmIPv6FltrV11v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 65)
)
tmnxSecurityCpmIPv6FltrV11v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryLogId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDescription"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryAction"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryQueueId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestIPAddr"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestIPMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryNextHeader"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestPort"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestPortMask"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDSCP"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryTcpSyn"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryTcpAck"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryIcmpCode"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryIcmpType"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryVRtrId"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryLogCreated"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryFlowLabel"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterStatsDroppedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterStatsForwardedPkts"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterAdminState"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPortHigh"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPortOper"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestPortHigh"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDestPortOper"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntrySrcPortList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryDstPortList"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryPortSelector"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryFragment"),
        ("TIMETRA-SECURITY-MIB", "tCpmIPv6FilterEntryHopByHopOpt"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmIPv6FltrV11v0Grp.setStatus("current")

tmnxDistCpuProtectionV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 66)
)
tmnxDistCpuProtectionV11v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyLastMdfy"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyDescr"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtPolicyTblLstChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrTblLstChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrLastMdfy"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrDescr"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrPackets"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrWithin"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrInitDelay"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrKbps"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrMbs"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrExdActn"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrExdHold"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrRateType"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrDectnTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtStaticPlcrLogEvent"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrTblLstChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrLastMdfy"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrDescr"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrPackets"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrWithin"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrInitDelay"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrKbps"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrMbs"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrExcdActn"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrRateType"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtLocMonPlcrLogEvent"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolTblLstChg"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolLastMdfy"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolEnforce"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolEnfrcePolNme"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynPackets"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynWithin"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynInitDly"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynKbps"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynMbs"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynDectnTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynExdActn"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynExdHold"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynRateType"),
        ("TIMETRA-SECURITY-MIB", "tmnxDCpuProtProtocolDynLogEvent"))
)
if mibBuilder.loadTexts:
    tmnxDistCpuProtectionV11v0Group.setStatus("current")

tmnxCAProfileV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 67)
)
tmnxCAProfileV11v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpAccUnprotErr"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpAccUnprotPki"),
        ("TIMETRA-SECURITY-MIB", "tmnxOcspCacheCertStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxOcspCacheExpiry"),
        ("TIMETRA-SECURITY-MIB", "tmnxOcspCacheCertIssuer"),
        ("TIMETRA-SECURITY-MIB", "tmnxOcspCacheCertSerial"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnOrigCmdTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnLastCAResp"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnType"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnProtKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnProtAlgPass"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnProtAlgRef"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnProtAlgSigCert"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnProtAlgSigHash"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnSubjectDn"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnSaveAsFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnNewKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatusString"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatusCode"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnSendChain"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnSendChainCA"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpRespSignCert"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfOcspRespUrl"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfOcspSvcID"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfOcspVerifyCertFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfOcspVerifyCertCA"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfOcspVerifyCertOvr"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpKeyRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpKeyLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpKeySecret"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpKeyTblLastChgd"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpHttpTimeout"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpUrl"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpSvcID"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpSameRecipNonce"))
)
if mibBuilder.loadTexts:
    tmnxCAProfileV11v0Group.setStatus("current")

tmnxRadiusUserExV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 68)
)
tmnxRadiusUserExV11v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxRadiusUserAuthAvgDelay"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserAcctAvgDelay"))
)
if mibBuilder.loadTexts:
    tmnxRadiusUserExV11v0Group.setStatus("current")

tmnxSecurityTacPlusV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 69)
)
tmnxSecurityTacPlusV11v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxTacPlusAuthorUsePrivLvl"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusEnableAdminPrivLvl"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusPrivLvlMapUserProfile"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusPrivLvlRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxTacPlusInteractiveAuthen"))
)
if mibBuilder.loadTexts:
    tmnxSecurityTacPlusV11v0Group.setStatus("current")

tmnxSecurityPasswordsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 70)
)
tmnxSecurityPasswordsV11v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxDynSvcPassword")
)
if mibBuilder.loadTexts:
    tmnxSecurityPasswordsV11v0Group.setStatus("obsolete")

tmnxCpmProtectionV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 72)
)
tmnxCpmProtectionV11v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxCpmProtBlockPIMTunneled")
)
if mibBuilder.loadTexts:
    tmnxCpmProtectionV11v0Group.setStatus("current")

tmnxSecurityCpmProtV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 73)
)
tmnxSecurityCpmProtV12v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtPortRateActionLowPrio"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtIPSrcMonDhcp"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolIfPeriods"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolIfTimeStart"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolIfTime"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSapPeriods"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSapTimeStart"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSapTime"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSdpBindPeriod"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSdpBindTmeStr"),
        ("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSdpBindTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIpPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIpStarted"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIpTime"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmProtV12v0Group.setStatus("current")

tmnxSecurityPasswordsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 74)
)
tmnxSecurityPasswordsV12v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPasswordAging"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordMinLength"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsCount"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAttemptsLockoutPeriod"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder1"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder2"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenOrder3"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAuthenExitOnReject"),
        ("TIMETRA-SECURITY-MIB", "tmnxAdminPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxAdminPasswordEncrypted"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordHealthCheck"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordHealthCheckInterval"),
        ("TIMETRA-SECURITY-MIB", "tmnxDynSvcPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordHistory"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordMinChange"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordMinAge"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordAllowUserName"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordMaxRepeatedChars"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordCreditsLowerCase"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordCreditsUpperCase"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordCreditsSpecialChar"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordCreditsNumeric"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordReqLowerCase"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordReqUpperCase"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordReqSpecialChar"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordReqNumeric"),
        ("TIMETRA-SECURITY-MIB", "tmnxPasswordReqNumCharClass"))
)
if mibBuilder.loadTexts:
    tmnxSecurityPasswordsV12v0Group.setStatus("current")

tmnxSecCpmProtNotifyObjsV12v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 76)
)
tmnxSecCpmProtNotifyObjsV12v0Grp.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump")
)
if mibBuilder.loadTexts:
    tmnxSecCpmProtNotifyObjsV12v0Grp.setStatus("current")

tmnxSecTechGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 77)
)
tmnxSecTechGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxSecurityTechSupportLocation")
)
if mibBuilder.loadTexts:
    tmnxSecTechGroup.setStatus("current")

tmnxSecurityUserV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 78)
)
tmnxSecurityUserV12v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxUserProfileRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileDefaultAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchDescription"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchAction"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserProfileMatchString"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPassword"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleLoginExecFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleCannotChangePswd"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleNewPswdAtLogin"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile1"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile2"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile3"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile4"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile5"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile6"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile7"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserConsoleMemberProfile8"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserAttemptedLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserSuccessfulLogins"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserActionClearPwdHistory"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateAccess"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateHomeDirectory"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateRestrictedToHome"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateConsoleLoginExecFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxTemplateProfile"))
)
if mibBuilder.loadTexts:
    tmnxSecurityUserV12v0Group.setStatus("current")

tmnxSecurityV12v0ObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 79)
)
tmnxSecurityV12v0ObsoletedGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxUserPasswordEncrypted")
)
if mibBuilder.loadTexts:
    tmnxSecurityV12v0ObsoletedGroup.setStatus("current")

tmnxSecurityNetconfV110Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 80)
)
tmnxSecurityNetconfV110Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxUserProfileNCKillSession")
)
if mibBuilder.loadTexts:
    tmnxSecurityNetconfV110Group.setStatus("current")

tCAProfCmpv2SetSndrV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 82)
)
tCAProfCmpv2SetSndrV11v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpAlSetSndrForIr")
)
if mibBuilder.loadTexts:
    tCAProfCmpv2SetSndrV11v0Group.setStatus("current")

tmnxSecurityKeyChainV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 83)
)
tmnxSecurityKeyChainV12v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxKeyChainExpired"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainKeyOption"))
)
if mibBuilder.loadTexts:
    tmnxSecurityKeyChainV12v0Group.setStatus("current")

tmnxSecurityPublicKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 84)
)
tmnxSecurityPublicKeyGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxUserPublicKeyRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPublicKeyLastChanged"),
        ("TIMETRA-SECURITY-MIB", "tmnxUserPublicKeyName"))
)
if mibBuilder.loadTexts:
    tmnxSecurityPublicKeyGroup.setStatus("current")

tCAProfCmpv2HttpVerV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 85)
)
tCAProfCmpv2HttpVerV12v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfCmpHttpVersion")
)
if mibBuilder.loadTexts:
    tCAProfCmpv2HttpVerV12v0Group.setStatus("current")

tmnxSecurityNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 86)
)
tmnxSecurityNotifyObjsV12v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxSecNotifOrigProtocol")
)
if mibBuilder.loadTexts:
    tmnxSecurityNotifyObjsV12v0Group.setStatus("current")

tmnxPkiCertDispFmtV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 88)
)
tmnxPkiCertDispFmtV12v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxPkiCertDisplayFormat")
)
if mibBuilder.loadTexts:
    tmnxPkiCertDispFmtV12v0Group.setStatus("current")

tmnxSecurityProfRateV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 89)
)
tmnxSecurityProfRateV12v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolOutProfRateLogEvnt")
)
if mibBuilder.loadTexts:
    tmnxSecurityProfRateV12v0Group.setStatus("current")

tmnxSecCpmProtProtocolV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 90)
)
tmnxSecCpmProtProtocolV12v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtIPSrcMonGtp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtIPSrcMonIcmp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtIPSrcMonIgmp"))
)
if mibBuilder.loadTexts:
    tmnxSecCpmProtProtocolV12v0Group.setStatus("current")

tmnxSecuritySSHCipherGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 91)
)
tmnxSecuritySSHCipherGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSSHCipherName"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerCipherListRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerCipherListNumber"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHClientCipherListRowStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHClientCipherListNumber"))
)
if mibBuilder.loadTexts:
    tmnxSecuritySSHCipherGroup.setStatus("current")

tmnxPkiCAProfRevokeChkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 92)
)
tmnxPkiCAProfRevokeChkGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfRevokeChk")
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfRevokeChkGroup.setStatus("current")


# Notification objects

tmnxSSHServerPreserveKeyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 1)
)
tmnxSSHServerPreserveKeyFail.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashHwIndex"),
        ("TIMETRA-CHASSIS-MIB", "tmnxCpmFlashOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxSSHServerPreserveKeyFail.setStatus(
        "current"
    )

tmnxKeyChainAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 2)
)
tmnxKeyChainAuthFailure.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxKeyChainReceiveTcpOptionNum"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthFailReason"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthAddrType"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthAddr"),
        ("TIMETRA-VRTR-MIB", "vRtrID"))
)
if mibBuilder.loadTexts:
    tmnxKeyChainAuthFailure.setStatus(
        "current"
    )

tmnxCpmProtViolPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 3)
)
tmnxCpmProtViolPort.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolPort.setStatus(
        "current"
    )

tmnxCpmProtViolPortAgg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 4)
)
tmnxCpmProtViolPortAgg.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortAggPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolPortAgg.setStatus(
        "current"
    )

tmnxCpmProtViolIf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 5)
)
tmnxCpmProtViolIf.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIfPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolIf.setStatus(
        "current"
    )

tmnxCpmProtViolSap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 6)
)
tmnxCpmProtViolSap.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSapPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSap.setStatus(
        "current"
    )

tmnxCpmProtViolMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 7)
)
tmnxCpmProtViolMac.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolMacAddress"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolMacPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolMac.setStatus(
        "current"
    )

tmnxCpmProtViolVdoSvcClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 8)
)
tmnxCpmProtViolVdoSvcClient.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoSvcClient.setStatus(
        "current"
    )

tmnxCpmProtViolVdoVrtrClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 9)
)
tmnxCpmProtViolVdoVrtrClient.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolVdoVrtrClient.setStatus(
        "current"
    )

tmnxMD5AuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 10)
)
tmnxMD5AuthFailure.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxMD5AuthKey"),
        ("TIMETRA-SECURITY-MIB", "tmnxMD5AuthFailReason"),
        ("TIMETRA-SECURITY-MIB", "tmnxMD5AuthAddrType"),
        ("TIMETRA-SECURITY-MIB", "tmnxMD5AuthAddr"),
        ("TIMETRA-VRTR-MIB", "vRtrID"))
)
if mibBuilder.loadTexts:
    tmnxMD5AuthFailure.setStatus(
        "current"
    )

tmnxCpmProtDefPolModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 11)
)
tmnxCpmProtDefPolModified.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolId")
)
if mibBuilder.loadTexts:
    tmnxCpmProtDefPolModified.setStatus(
        "current"
    )

tmnxCpmProtViolSdpBind = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 12)
)
tmnxCpmProtViolSdpBind.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBindPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBind.setStatus(
        "current"
    )

tmnxCpmProtExcdSdpBind = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 13)
)
tmnxCpmProtExcdSdpBind.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBind.setStatus(
        "current"
    )

tmnxCpmProtExcdSapEcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 14)
)
tmnxCpmProtExcdSapEcm.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcmPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapEcm.setStatus(
        "current"
    )

tmnxCpmProtExcdSdpBindEcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 15)
)
tmnxCpmProtExcdSdpBindEcm.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcmPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindEcm.setStatus(
        "current"
    )

tmnxPkiFileReadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 16)
)
tmnxPkiFileReadFailed.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecNotifFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxPkiFileReadFailed.setStatus(
        "current"
    )

tmnxPkiCertVerificationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 17)
)
tmnxPkiCertVerificationFailed.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecNotifTunnelName"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifCert"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxPkiCertVerificationFailed.setStatus(
        "current"
    )

tmnxCAProfileStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 18)
)
tmnxCAProfileStateChange.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileOperState"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxCAProfileStateChange.setStatus(
        "current"
    )

tmnxCpmProtExcdSapIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 19)
)
tmnxCpmProtExcdSapIp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSapIp.setStatus(
        "current"
    )

tmnxPkiCAProfActnStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 20)
)
tmnxPkiCAProfActnStatusChg.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnType"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatus"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatusString"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatusCode"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnOrigCmdTime"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnLastCAResp"))
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfActnStatusChg.setStatus(
        "current"
    )

tmnxCpmProtViolSapOutProf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 21)
)
tmnxCpmProtViolSapOutProf.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSapPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSapOutProf.setStatus(
        "current"
    )

tmnxCpmProtViolIfOutProf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 22)
)
tmnxCpmProtViolIfOutProf.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolIfPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolIfOutProf.setStatus(
        "current"
    )

tmnxCpmProtExcdSdpBindIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 23)
)
tmnxCpmProtExcdSdpBindIp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIpPeriods"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtExcdSdpBindIp.setStatus(
        "current"
    )

tmnxSecComputeCertChainFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 24)
)
tmnxSecComputeCertChainFailure.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecNotifFile"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxSecComputeCertChainFailure.setStatus(
        "current"
    )

tmnxCpmProtViolSdpBindOutProf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 25)
)
tmnxCpmProtViolSdpBindOutProf.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tCpmProtOutProfViolSdpBindPeriod"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolExcdPktHexDump"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtViolSdpBindOutProf.setStatus(
        "current"
    )

tmnxSecNotifKeyChainExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 26)
)
tmnxSecNotifKeyChainExpired.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxKeyChainExpired"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifOrigProtocol"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifKeyChainExpired.setStatus(
        "current"
    )

tmnxCAProfUpDueToRevokeChkCrlOpt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 22, 0, 27)
)
tmnxCAProfUpDueToRevokeChkCrlOpt.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfileOperState"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecNotifFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxCAProfUpDueToRevokeChkCrlOpt.setStatus(
        "current"
    )


# Notifications groups

tmnxSecurityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 14)
)
tmnxSecurityNotificationGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxSSHServerPreserveKeyFail")
)
if mibBuilder.loadTexts:
    tmnxSecurityNotificationGroup.setStatus(
        "obsolete"
    )

tmnxSecurityNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 30)
)
tmnxSecurityNotificationV5v0Group.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSSHServerPreserveKeyFail"),
        ("TIMETRA-SECURITY-MIB", "tmnxKeyChainAuthFailure"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNotificationV5v0Group.setStatus(
        "current"
    )

tmnxSecurityCpmProtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 38)
)
tmnxSecurityCpmProtNotificationGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPort"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolPortAgg"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIf"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSap"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolMac"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmProtNotificationGroup.setStatus(
        "current"
    )

tmnxSecurityCpmProtNotifyV7v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 45)
)
tmnxSecurityCpmProtNotifyV7v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoSvcClient"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolVdoVrtrClient"))
)
if mibBuilder.loadTexts:
    tmnxSecurityCpmProtNotifyV7v0Grp.setStatus(
        "current"
    )

tmnxSecurityNotificationV8v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 49)
)
tmnxSecurityNotificationV8v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxMD5AuthFailure"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtDefPolModified"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNotificationV8v0Grp.setStatus(
        "current"
    )

tmnxCpmProtPolNotifyV8v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 52)
)
tmnxCpmProtPolNotifyV8v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBind"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBind"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapEcm"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindEcm"))
)
if mibBuilder.loadTexts:
    tmnxCpmProtPolNotifyV8v0Grp.setStatus(
        "current"
    )

tmnxCertNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 55)
)
tmnxCertNotifyGroup.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxPkiFileReadFailed"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCertVerificationFailed"),
        ("TIMETRA-SECURITY-MIB", "tmnxCAProfileStateChange"))
)
if mibBuilder.loadTexts:
    tmnxCertNotifyGroup.setStatus(
        "current"
    )

tmnxCpmProtPolNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 59)
)
tmnxCpmProtPolNotifyV9v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIp")
)
if mibBuilder.loadTexts:
    tmnxCpmProtPolNotifyV9v0Group.setStatus(
        "current"
    )

tmnxPkiCAProfNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 71)
)
tmnxPkiCAProfNotifyV11v0Group.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfActnStatusChg")
)
if mibBuilder.loadTexts:
    tmnxPkiCAProfNotifyV11v0Group.setStatus(
        "current"
    )

tmnxSecCpmProtNotifyV12v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 75)
)
tmnxSecCpmProtNotifyV12v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSapOutProf"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolIfOutProf"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtViolSdpBindOutProf"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSdpBindIp"))
)
if mibBuilder.loadTexts:
    tmnxSecCpmProtNotifyV12v0Grp.setStatus(
        "current"
    )

tmnxChainSecurityNotifyObjsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 81)
)
tmnxChainSecurityNotifyObjsGroup.setObjects(
    ("TIMETRA-SECURITY-MIB", "tmnxSecComputeCertChainFailure")
)
if mibBuilder.loadTexts:
    tmnxChainSecurityNotifyObjsGroup.setStatus(
        "current"
    )

tmnxSecurityNotificationV12v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 2, 87)
)
tmnxSecurityNotificationV12v0Grp.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecNotifKeyChainExpired"),
        ("TIMETRA-SECURITY-MIB", "tmnxCAProfUpDueToRevokeChkCrlOpt"))
)
if mibBuilder.loadTexts:
    tmnxSecurityNotificationV12v0Grp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSecurity7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 5)
)
tmnxSecurity7450V4v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV3v0r2Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 6)
)
tmnxSecurity7750V4v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV3v0r2Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 7)
)
tmnxSecurity7450V5v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 8)
)
tmnxSecurity7750V5v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsR2r1Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 9)
)
tmnxSecurity7450V6v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 10)
)
tmnxSecurity7750V6v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 11)
)
tmnxSecurity7450V6v1Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 12)
)
tmnxSecurity7750V6v1Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 13)
)
tmnxSecurity7450V7v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 14)
)
tmnxSecurity7750V7v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotifyV7v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 15)
)
tmnxSecurity7450V8v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7710V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 16)
)
tmnxSecurity7710V8v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7710V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 17)
)
tmnxSecurity7750V8v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotifyV7v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 18)
)
tmnxSecurity7450V9v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7710V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 19)
)
tmnxSecurity7710V9v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7710V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 20)
)
tmnxSecurity7750V9v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotifyV7v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 21)
)
tmnxSecurity7450V10v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityUserActionGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertNotifyGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmFltrPrefixListV10v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecTechGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7450V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7710V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 22)
)
tmnxSecurity7710V10v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityUserActionGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertNotifyGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmFltrPrefixListV10v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecTechGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7710V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurity7750V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 23)
)
tmnxSecurity7750V10v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityUserActionGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FilterV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotifyV7v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertNotifyGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmFltrPrefixListV10v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecTechGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurity7750V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurityV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 24)
)
tmnxSecurityV11v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserActionGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV11v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FltrV11v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotifyV7v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertNotifyGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCAProfileV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmFltrPrefixListV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfNotifyV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxDistCpuProtectionV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtectionV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecTechGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNetconfV110Group"),
        ("TIMETRA-SECURITY-MIB", "tCAProfCmpv2SetSndrV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxSecurityV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxSecurityV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 22, 1, 25)
)
tmnxSecurityV12v0Compliance.setObjects(
      *(("TIMETRA-SECURITY-MIB", "tmnxSecurityUserV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityUserActionGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafV6v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordsV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityTacPlusV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityServerCtlV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPasswordHashGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIpFilterV11v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmIPv6FltrV11v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSSHServerV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySourceIpV4v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityKeyChainV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtectGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityLiGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotificationGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityMafMacFilterGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityRadiusAuthV5v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityV7v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtNotifyV7v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV8v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotifyObjsV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNotificationV12v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtEthCfmPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV8v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecPkiV9v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNwExceptionsGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxCertNotifyGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxRadiusUserExV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtExcdSapIpV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtPolNotifyV9v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCAProfileV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmFltrPrefixListV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfNotifyV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxDistCpuProtectionV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxCpmProtectionV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityCpmProtV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecCpmProtNotifyV12v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecCpmProtNotifyObjsV12v0Grp"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecTechGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityNetconfV110Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxChainSecurityNotifyObjsGroup"),
        ("TIMETRA-SECURITY-MIB", "tCAProfCmpv2SetSndrV11v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityPublicKeyGroup"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecuritySSHCipherGroup"),
        ("TIMETRA-SECURITY-MIB", "tCAProfCmpv2HttpVerV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCertDispFmtV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecurityProfRateV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxSecCpmProtProtocolV12v0Group"),
        ("TIMETRA-SECURITY-MIB", "tmnxPkiCAProfRevokeChkGroup"))
)
if mibBuilder.loadTexts:
    tmnxSecurityV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SECURITY-MIB",
    **{"TProfileAction": TProfileAction,
       "TmnxMafAction": TmnxMafAction,
       "TCpmFilterQueueId": TCpmFilterQueueId,
       "TCpmFilterActionOrDefault": TCpmFilterActionOrDefault,
       "TmnxKeyChainKeyDirection": TmnxKeyChainKeyDirection,
       "TmnxKeyChainKeyAlgorithm": TmnxKeyChainKeyAlgorithm,
       "TmnxKeyChainKeyOption": TmnxKeyChainKeyOption,
       "TmnxKeyChainTcpOptionNum": TmnxKeyChainTcpOptionNum,
       "TmnxMafType": TmnxMafType,
       "TmnxCpmPacketRateLimit": TmnxCpmPacketRateLimit,
       "TmnxCpmPacketPolRateLimit": TmnxCpmPacketPolRateLimit,
       "TmnxCpmPktPolRateLimitInclZero": TmnxCpmPktPolRateLimitInclZero,
       "TmnxCpmPacketRate": TmnxCpmPacketRate,
       "TmnxCpmProtEthCfmOpCode": TmnxCpmProtEthCfmOpCode,
       "TmnxMafMacFltrFrameType": TmnxMafMacFltrFrameType,
       "TmnxCpmMacFltrFrameType": TmnxCpmMacFltrFrameType,
       "TmnxSecRadiusServAlgorithm": TmnxSecRadiusServAlgorithm,
       "TCpmFilterPortOperator": TCpmFilterPortOperator,
       "TSSHCipherNumber": TSSHCipherNumber,
       "timetraSecurityMIBModule": timetraSecurityMIBModule,
       "tmnxSecurityConformance": tmnxSecurityConformance,
       "tmnxSecurityCompliances": tmnxSecurityCompliances,
       "tmnxSecurity7450V4v0Compliance": tmnxSecurity7450V4v0Compliance,
       "tmnxSecurity7750V4v0Compliance": tmnxSecurity7750V4v0Compliance,
       "tmnxSecurity7450V5v0Compliance": tmnxSecurity7450V5v0Compliance,
       "tmnxSecurity7750V5v0Compliance": tmnxSecurity7750V5v0Compliance,
       "tmnxSecurity7450V6v0Compliance": tmnxSecurity7450V6v0Compliance,
       "tmnxSecurity7750V6v0Compliance": tmnxSecurity7750V6v0Compliance,
       "tmnxSecurity7450V6v1Compliance": tmnxSecurity7450V6v1Compliance,
       "tmnxSecurity7750V6v1Compliance": tmnxSecurity7750V6v1Compliance,
       "tmnxSecurity7450V7v0Compliance": tmnxSecurity7450V7v0Compliance,
       "tmnxSecurity7750V7v0Compliance": tmnxSecurity7750V7v0Compliance,
       "tmnxSecurity7450V8v0Compliance": tmnxSecurity7450V8v0Compliance,
       "tmnxSecurity7710V8v0Compliance": tmnxSecurity7710V8v0Compliance,
       "tmnxSecurity7750V8v0Compliance": tmnxSecurity7750V8v0Compliance,
       "tmnxSecurity7450V9v0Compliance": tmnxSecurity7450V9v0Compliance,
       "tmnxSecurity7710V9v0Compliance": tmnxSecurity7710V9v0Compliance,
       "tmnxSecurity7750V9v0Compliance": tmnxSecurity7750V9v0Compliance,
       "tmnxSecurity7450V10v0Compliance": tmnxSecurity7450V10v0Compliance,
       "tmnxSecurity7710V10v0Compliance": tmnxSecurity7710V10v0Compliance,
       "tmnxSecurity7750V10v0Compliance": tmnxSecurity7750V10v0Compliance,
       "tmnxSecurityV11v0Compliance": tmnxSecurityV11v0Compliance,
       "tmnxSecurityV12v0Compliance": tmnxSecurityV12v0Compliance,
       "tmnxSecurityGroups": tmnxSecurityGroups,
       "tmnxSecurityUserGroup": tmnxSecurityUserGroup,
       "tmnxSecurityMafR2r1Group": tmnxSecurityMafR2r1Group,
       "tmnxSecurityPasswordsR2r1Group": tmnxSecurityPasswordsR2r1Group,
       "tmnxSecurityCpmGroup": tmnxSecurityCpmGroup,
       "tmnxSecurityPasswordHashGroup": tmnxSecurityPasswordHashGroup,
       "tmnxSecurityNotificationGroup": tmnxSecurityNotificationGroup,
       "tmnxSecurityCpmIpFilterV3v0r2Group": tmnxSecurityCpmIpFilterV3v0r2Group,
       "tmnxSecurityCpmIPv6FilterV4v0Group": tmnxSecurityCpmIPv6FilterV4v0Group,
       "tmnxSecurityServerCtlV4v0Group": tmnxSecurityServerCtlV4v0Group,
       "tmnxSSHServerV4v0Group": tmnxSSHServerV4v0Group,
       "tmnxSecuritySourceIpV4v0Group": tmnxSecuritySourceIpV4v0Group,
       "tmnxSecurityRadiusV4v0Group": tmnxSecurityRadiusV4v0Group,
       "tmnxSecurityTacPlusV4v0Group": tmnxSecurityTacPlusV4v0Group,
       "tmnxSecurityObsoleteGroup": tmnxSecurityObsoleteGroup,
       "tmnxSecurityUserV4v0Group": tmnxSecurityUserV4v0Group,
       "tmnxSecurityKeyChainV5v0Group": tmnxSecurityKeyChainV5v0Group,
       "tmnxSecurityRadiusV5v0Group": tmnxSecurityRadiusV5v0Group,
       "tmnxSecurityTacPlusV5v0Group": tmnxSecurityTacPlusV5v0Group,
       "tmnxSecurityCpmIpFilterV5v0Group": tmnxSecurityCpmIpFilterV5v0Group,
       "tmnxSecurityNotificationV5v0Group": tmnxSecurityNotificationV5v0Group,
       "tmnxSecurityNotifyObjsGroup": tmnxSecurityNotifyObjsGroup,
       "tmnxSecurityTacPlusV6v0Group": tmnxSecurityTacPlusV6v0Group,
       "tmnxSecurityPasswordsV6v0Group": tmnxSecurityPasswordsV6v0Group,
       "tmnxSecurityMafV6v0Group": tmnxSecurityMafV6v0Group,
       "tmnxObsoletedObjectsV6v0Group": tmnxObsoletedObjectsV6v0Group,
       "tmnxSecurityCpmProtectGroup": tmnxSecurityCpmProtectGroup,
       "tmnxSecurityLiGroup": tmnxSecurityLiGroup,
       "tmnxSecurityCpmProtNotificationGroup": tmnxSecurityCpmProtNotificationGroup,
       "tmnxSecurityCpmProtNotificationObjsGroup": tmnxSecurityCpmProtNotificationObjsGroup,
       "tmnxSecurityCpmMacFilterGroup": tmnxSecurityCpmMacFilterGroup,
       "tmnxSecurityMafMacFilterGroup": tmnxSecurityMafMacFilterGroup,
       "tmnxSecurityUserV6v0Group": tmnxSecurityUserV6v0Group,
       "tmnxSecurityRadiusAuthV5v0Group": tmnxSecurityRadiusAuthV5v0Group,
       "tmnxSecurityV7v0Group": tmnxSecurityV7v0Group,
       "tmnxSecurityCpmProtNotifyV7v0Grp": tmnxSecurityCpmProtNotifyV7v0Grp,
       "tmnxSecurityTacPlusV8v0Group": tmnxSecurityTacPlusV8v0Group,
       "tmnxObsoletedObjectsV8v0Group": tmnxObsoletedObjectsV8v0Group,
       "tmnxSecurityNotifyObjsV8v0Group": tmnxSecurityNotifyObjsV8v0Group,
       "tmnxSecurityNotificationV8v0Grp": tmnxSecurityNotificationV8v0Grp,
       "tmnxCpmProtEthCfmPolV8v0Grp": tmnxCpmProtEthCfmPolV8v0Grp,
       "tmnxCpmProtPolV8v0Grp": tmnxCpmProtPolV8v0Grp,
       "tmnxCpmProtPolNotifyV8v0Grp": tmnxCpmProtPolNotifyV8v0Grp,
       "tmnxSecPkiV9v0Grp": tmnxSecPkiV9v0Grp,
       "tmnxSecurityNwExceptionsGroup": tmnxSecurityNwExceptionsGroup,
       "tmnxCertNotifyGroup": tmnxCertNotifyGroup,
       "tmnxSecNotifyObjsV10v0Group": tmnxSecNotifyObjsV10v0Group,
       "tmnxRadiusUserGroup": tmnxRadiusUserGroup,
       "tmnxCpmProtExcdSapIpV9v0Group": tmnxCpmProtExcdSapIpV9v0Group,
       "tmnxCpmProtPolNotifyV9v0Group": tmnxCpmProtPolNotifyV9v0Group,
       "tmnxCpmFltrPrefixListV10v0Group": tmnxCpmFltrPrefixListV10v0Group,
       "tmnxRadiusUserExGroup": tmnxRadiusUserExGroup,
       "tmnxSecurityUserActionGroup": tmnxSecurityUserActionGroup,
       "tmnxCpmFltrPrefixListV11v0Group": tmnxCpmFltrPrefixListV11v0Group,
       "tmnxSecurityCpmIpFilterV11v0Grp": tmnxSecurityCpmIpFilterV11v0Grp,
       "tmnxSecurityCpmIPv6FltrV11v0Grp": tmnxSecurityCpmIPv6FltrV11v0Grp,
       "tmnxDistCpuProtectionV11v0Group": tmnxDistCpuProtectionV11v0Group,
       "tmnxCAProfileV11v0Group": tmnxCAProfileV11v0Group,
       "tmnxRadiusUserExV11v0Group": tmnxRadiusUserExV11v0Group,
       "tmnxSecurityTacPlusV11v0Group": tmnxSecurityTacPlusV11v0Group,
       "tmnxSecurityPasswordsV11v0Group": tmnxSecurityPasswordsV11v0Group,
       "tmnxPkiCAProfNotifyV11v0Group": tmnxPkiCAProfNotifyV11v0Group,
       "tmnxCpmProtectionV11v0Group": tmnxCpmProtectionV11v0Group,
       "tmnxSecurityCpmProtV12v0Group": tmnxSecurityCpmProtV12v0Group,
       "tmnxSecurityPasswordsV12v0Group": tmnxSecurityPasswordsV12v0Group,
       "tmnxSecCpmProtNotifyV12v0Grp": tmnxSecCpmProtNotifyV12v0Grp,
       "tmnxSecCpmProtNotifyObjsV12v0Grp": tmnxSecCpmProtNotifyObjsV12v0Grp,
       "tmnxSecTechGroup": tmnxSecTechGroup,
       "tmnxSecurityUserV12v0Group": tmnxSecurityUserV12v0Group,
       "tmnxSecurityV12v0ObsoletedGroup": tmnxSecurityV12v0ObsoletedGroup,
       "tmnxSecurityNetconfV110Group": tmnxSecurityNetconfV110Group,
       "tmnxChainSecurityNotifyObjsGroup": tmnxChainSecurityNotifyObjsGroup,
       "tCAProfCmpv2SetSndrV11v0Group": tCAProfCmpv2SetSndrV11v0Group,
       "tmnxSecurityKeyChainV12v0Group": tmnxSecurityKeyChainV12v0Group,
       "tmnxSecurityPublicKeyGroup": tmnxSecurityPublicKeyGroup,
       "tCAProfCmpv2HttpVerV12v0Group": tCAProfCmpv2HttpVerV12v0Group,
       "tmnxSecurityNotifyObjsV12v0Group": tmnxSecurityNotifyObjsV12v0Group,
       "tmnxSecurityNotificationV12v0Grp": tmnxSecurityNotificationV12v0Grp,
       "tmnxPkiCertDispFmtV12v0Group": tmnxPkiCertDispFmtV12v0Group,
       "tmnxSecurityProfRateV12v0Group": tmnxSecurityProfRateV12v0Group,
       "tmnxSecCpmProtProtocolV12v0Group": tmnxSecCpmProtProtocolV12v0Group,
       "tmnxSecuritySSHCipherGroup": tmnxSecuritySSHCipherGroup,
       "tmnxPkiCAProfRevokeChkGroup": tmnxPkiCAProfRevokeChkGroup,
       "tmnxSecurityObjects": tmnxSecurityObjects,
       "tmnxUserProfileTable": tmnxUserProfileTable,
       "tmnxUserProfileEntry": tmnxUserProfileEntry,
       "tmnxUserProfile": tmnxUserProfile,
       "tmnxUserProfileRowStatus": tmnxUserProfileRowStatus,
       "tmnxUserProfileDefaultAction": tmnxUserProfileDefaultAction,
       "tmnxUserProfileLi": tmnxUserProfileLi,
       "tmnxUserProfileNCKillSession": tmnxUserProfileNCKillSession,
       "tmnxUserProfileMatchTable": tmnxUserProfileMatchTable,
       "tmnxUserProfileMatchEntry": tmnxUserProfileMatchEntry,
       "tmnxUserProfileMatchId": tmnxUserProfileMatchId,
       "tmnxUserProfileMatchRowStatus": tmnxUserProfileMatchRowStatus,
       "tmnxUserProfileMatchDescription": tmnxUserProfileMatchDescription,
       "tmnxUserProfileMatchAction": tmnxUserProfileMatchAction,
       "tmnxUserProfileMatchString": tmnxUserProfileMatchString,
       "tmnxUserTable": tmnxUserTable,
       "tmnxUserEntry": tmnxUserEntry,
       "tmnxUserName": tmnxUserName,
       "tmnxUserRowStatus": tmnxUserRowStatus,
       "tmnxUserPassword": tmnxUserPassword,
       "tmnxUserPasswordEncrypted": tmnxUserPasswordEncrypted,
       "tmnxUserAccess": tmnxUserAccess,
       "tmnxUserHomeDirectory": tmnxUserHomeDirectory,
       "tmnxUserRestrictedToHome": tmnxUserRestrictedToHome,
       "tmnxUserConsoleLoginExecFile": tmnxUserConsoleLoginExecFile,
       "tmnxUserConsoleCannotChangePswd": tmnxUserConsoleCannotChangePswd,
       "tmnxUserConsoleNewPswdAtLogin": tmnxUserConsoleNewPswdAtLogin,
       "tmnxUserConsoleMemberProfile1": tmnxUserConsoleMemberProfile1,
       "tmnxUserConsoleMemberProfile2": tmnxUserConsoleMemberProfile2,
       "tmnxUserConsoleMemberProfile3": tmnxUserConsoleMemberProfile3,
       "tmnxUserConsoleMemberProfile4": tmnxUserConsoleMemberProfile4,
       "tmnxUserConsoleMemberProfile5": tmnxUserConsoleMemberProfile5,
       "tmnxUserConsoleMemberProfile6": tmnxUserConsoleMemberProfile6,
       "tmnxUserConsoleMemberProfile7": tmnxUserConsoleMemberProfile7,
       "tmnxUserConsoleMemberProfile8": tmnxUserConsoleMemberProfile8,
       "tmnxUserAttemptedLogins": tmnxUserAttemptedLogins,
       "tmnxUserSuccessfulLogins": tmnxUserSuccessfulLogins,
       "tmnxUserPasswordChanged": tmnxUserPasswordChanged,
       "tmnxMafObjs": tmnxMafObjs,
       "tmnxMafTable": tmnxMafTable,
       "tmnxMafEntry": tmnxMafEntry,
       "tmnxMafName": tmnxMafName,
       "tmnxMafRowStatus": tmnxMafRowStatus,
       "tmnxMafDefaultAction": tmnxMafDefaultAction,
       "tmnxMafAdminState": tmnxMafAdminState,
       "tmnxMafMatchTable": tmnxMafMatchTable,
       "tmnxMafMatchEntry": tmnxMafMatchEntry,
       "tmnxMafMatchIndex": tmnxMafMatchIndex,
       "tmnxMafMatchRowStatus": tmnxMafMatchRowStatus,
       "tmnxMafMatchLastChanged": tmnxMafMatchLastChanged,
       "tmnxMafMatchAction": tmnxMafMatchAction,
       "tmnxMafMatchDescription": tmnxMafMatchDescription,
       "tmnxMafMatchSrcIpAddr": tmnxMafMatchSrcIpAddr,
       "tmnxMafMatchSrcIpMask": tmnxMafMatchSrcIpMask,
       "tmnxMafMatchSrcPortType": tmnxMafMatchSrcPortType,
       "tmnxMafMatchSrcPortId": tmnxMafMatchSrcPortId,
       "tmnxMafMatchDestPort": tmnxMafMatchDestPort,
       "tmnxMafMatchDestPortMask": tmnxMafMatchDestPortMask,
       "tmnxMafMatchProtocol": tmnxMafMatchProtocol,
       "tmnxMafMatchCount": tmnxMafMatchCount,
       "tmnxMafMatchRouter": tmnxMafMatchRouter,
       "tmnxMafMatchLog": tmnxMafMatchLog,
       "tmnxGenMafTableLastChanged": tmnxGenMafTableLastChanged,
       "tmnxGenMafTable": tmnxGenMafTable,
       "tmnxGenMafEntry": tmnxGenMafEntry,
       "tmnxGenMafType": tmnxGenMafType,
       "tmnxGenMafName": tmnxGenMafName,
       "tmnxGenMafLastModified": tmnxGenMafLastModified,
       "tmnxGenMafRowStatus": tmnxGenMafRowStatus,
       "tmnxGenMafAdminState": tmnxGenMafAdminState,
       "tmnxGenMafDefaultAction": tmnxGenMafDefaultAction,
       "tmnxMafIPMatchTableLastChanged": tmnxMafIPMatchTableLastChanged,
       "tmnxIPMafMatchTable": tmnxIPMafMatchTable,
       "tmnxIPMafMatchEntry": tmnxIPMafMatchEntry,
       "tmnxIPMafMatchIndex": tmnxIPMafMatchIndex,
       "tmnxIPMafMatchRowStatus": tmnxIPMafMatchRowStatus,
       "tmnxIPMafMatchLastChanged": tmnxIPMafMatchLastChanged,
       "tmnxIPMafMatchAction": tmnxIPMafMatchAction,
       "tmnxIPMafMatchDescription": tmnxIPMafMatchDescription,
       "tmnxIPMafMatchSrcIpAddrType": tmnxIPMafMatchSrcIpAddrType,
       "tmnxIPMafMatchSrcIpAddr": tmnxIPMafMatchSrcIpAddr,
       "tmnxIPMafMatchSrcIpMask": tmnxIPMafMatchSrcIpMask,
       "tmnxIPMafMatchSrcPortType": tmnxIPMafMatchSrcPortType,
       "tmnxIPMafMatchSrcPortId": tmnxIPMafMatchSrcPortId,
       "tmnxIPMafMatchDestPort": tmnxIPMafMatchDestPort,
       "tmnxIPMafMatchDestPortMask": tmnxIPMafMatchDestPortMask,
       "tmnxIPMafMatchProtNxtHdr": tmnxIPMafMatchProtNxtHdr,
       "tmnxIPMafMatchCount": tmnxIPMafMatchCount,
       "tmnxIPMafMatchRouter": tmnxIPMafMatchRouter,
       "tmnxIPMafMatchFlowLabel": tmnxIPMafMatchFlowLabel,
       "tmnxIPMafMatchLog": tmnxIPMafMatchLog,
       "tmnxMafMacMatchTableLastChanged": tmnxMafMacMatchTableLastChanged,
       "tmnxMacMafMatchTable": tmnxMacMafMatchTable,
       "tmnxMacMafMatchEntry": tmnxMacMafMatchEntry,
       "tmnxMacMafMatchIndex": tmnxMacMafMatchIndex,
       "tmnxMacMafMatchRowStatus": tmnxMacMafMatchRowStatus,
       "tmnxMacMafMatchLastChanged": tmnxMacMafMatchLastChanged,
       "tmnxMacMafMatchAction": tmnxMacMafMatchAction,
       "tmnxMacMafMatchDescription": tmnxMacMafMatchDescription,
       "tmnxMacMafMatchLog": tmnxMacMafMatchLog,
       "tmnxMacMafMatchFrameType": tmnxMacMafMatchFrameType,
       "tmnxMacMafMatchSvcId": tmnxMacMafMatchSvcId,
       "tmnxMacMafMatchDot1pValue": tmnxMacMafMatchDot1pValue,
       "tmnxMacMafMatchDot1pMask": tmnxMacMafMatchDot1pMask,
       "tmnxMacMafMatchDsap": tmnxMacMafMatchDsap,
       "tmnxMacMafMatchDsapMask": tmnxMacMafMatchDsapMask,
       "tmnxMacMafMatchSrcMAC": tmnxMacMafMatchSrcMAC,
       "tmnxMacMafMatchSrcMACMask": tmnxMacMafMatchSrcMACMask,
       "tmnxMacMafMatchDstMAC": tmnxMacMafMatchDstMAC,
       "tmnxMacMafMatchDstMACMask": tmnxMacMafMatchDstMACMask,
       "tmnxMacMafMatchEtherType": tmnxMacMafMatchEtherType,
       "tmnxMacMafMatchSnapOui": tmnxMacMafMatchSnapOui,
       "tmnxMacMafMatchSnapPid": tmnxMacMafMatchSnapPid,
       "tmnxMacMafMatchSsap": tmnxMacMafMatchSsap,
       "tmnxMacMafMatchSsapMask": tmnxMacMafMatchSsapMask,
       "tmnxMacMafMatchCfmOpCodeOper": tmnxMacMafMatchCfmOpCodeOper,
       "tmnxMacMafMatchCfmOpCodeValue1": tmnxMacMafMatchCfmOpCodeValue1,
       "tmnxMacMafMatchCfmOpCodeValue2": tmnxMacMafMatchCfmOpCodeValue2,
       "tmnxMacMafMatchCount": tmnxMacMafMatchCount,
       "tmnxPasswordInfo": tmnxPasswordInfo,
       "tmnxPasswordAging": tmnxPasswordAging,
       "tmnxPasswordMinLength": tmnxPasswordMinLength,
       "tmnxPasswordComplexity": tmnxPasswordComplexity,
       "tmnxPasswordAttemptsCount": tmnxPasswordAttemptsCount,
       "tmnxPasswordAttemptsTime": tmnxPasswordAttemptsTime,
       "tmnxPasswordAttemptsLockoutPeriod": tmnxPasswordAttemptsLockoutPeriod,
       "tmnxPasswordAuthenOrder1": tmnxPasswordAuthenOrder1,
       "tmnxPasswordAuthenOrder2": tmnxPasswordAuthenOrder2,
       "tmnxPasswordAuthenOrder3": tmnxPasswordAuthenOrder3,
       "tmnxPasswordAuthenExitOnReject": tmnxPasswordAuthenExitOnReject,
       "tmnxAdminPassword": tmnxAdminPassword,
       "tmnxAdminPasswordEncrypted": tmnxAdminPasswordEncrypted,
       "tmnxPasswordHealthCheck": tmnxPasswordHealthCheck,
       "tmnxPasswordHealthCheckInterval": tmnxPasswordHealthCheckInterval,
       "tmnxDynSvcPassword": tmnxDynSvcPassword,
       "tmnxTacPlusEnableAdminPrivLvl": tmnxTacPlusEnableAdminPrivLvl,
       "tmnxPasswordHistory": tmnxPasswordHistory,
       "tmnxPasswordMinChange": tmnxPasswordMinChange,
       "tmnxPasswordMinAge": tmnxPasswordMinAge,
       "tmnxPasswordAllowUserName": tmnxPasswordAllowUserName,
       "tmnxPasswordMaxRepeatedChars": tmnxPasswordMaxRepeatedChars,
       "tmnxPasswordCreditsLowerCase": tmnxPasswordCreditsLowerCase,
       "tmnxPasswordCreditsUpperCase": tmnxPasswordCreditsUpperCase,
       "tmnxPasswordCreditsNumeric": tmnxPasswordCreditsNumeric,
       "tmnxPasswordCreditsSpecialChar": tmnxPasswordCreditsSpecialChar,
       "tmnxPasswordReqLowerCase": tmnxPasswordReqLowerCase,
       "tmnxPasswordReqUpperCase": tmnxPasswordReqUpperCase,
       "tmnxPasswordReqNumeric": tmnxPasswordReqNumeric,
       "tmnxPasswordReqSpecialChar": tmnxPasswordReqSpecialChar,
       "tmnxPasswordReqNumCharClass": tmnxPasswordReqNumCharClass,
       "tmnxRadiusInfo": tmnxRadiusInfo,
       "tmnxRadiusAdminStatus": tmnxRadiusAdminStatus,
       "tmnxRadiusAccounting": tmnxRadiusAccounting,
       "tmnxRadiusAuthorization": tmnxRadiusAuthorization,
       "tmnxRadiusRetryAttempts": tmnxRadiusRetryAttempts,
       "tmnxRadiusTimeout": tmnxRadiusTimeout,
       "tmnxRadiusPort": tmnxRadiusPort,
       "tmnxRadiusServerTable": tmnxRadiusServerTable,
       "tmnxRadiusServerEntry": tmnxRadiusServerEntry,
       "tmnxRadiusServerIndex": tmnxRadiusServerIndex,
       "tmnxRadiusServerAddress": tmnxRadiusServerAddress,
       "tmnxRadiusServerSecret": tmnxRadiusServerSecret,
       "tmnxRadiusServerOperStatus": tmnxRadiusServerOperStatus,
       "tmnxRadiusServerRowStatus": tmnxRadiusServerRowStatus,
       "tmnxRadiusServerInetAddressType": tmnxRadiusServerInetAddressType,
       "tmnxRadiusServerInetAddress": tmnxRadiusServerInetAddress,
       "tmnxRadiusSourceAddress": tmnxRadiusSourceAddress,
       "tmnxRadiusConfigured": tmnxRadiusConfigured,
       "tmnxRadiusPEDiscovery": tmnxRadiusPEDiscovery,
       "tmnxRadiusPEDiscoveryPassword": tmnxRadiusPEDiscoveryPassword,
       "tmnxRadiusPEDiscoveryInterval": tmnxRadiusPEDiscoveryInterval,
       "tmnxRadiusPEForceDiscovery": tmnxRadiusPEForceDiscovery,
       "tmnxRadiusPEForceDiscoverySvcId": tmnxRadiusPEForceDiscoverySvcId,
       "tmnxRadiusAccountingPort": tmnxRadiusAccountingPort,
       "tmnxRadiusUseTemplate": tmnxRadiusUseTemplate,
       "tmnxRadiusAuthAlgorithm": tmnxRadiusAuthAlgorithm,
       "tmnxRadiusUserStatsTable": tmnxRadiusUserStatsTable,
       "tmnxRadiusUserStatsEntry": tmnxRadiusUserStatsEntry,
       "tmnxRadiusPolicyName": tmnxRadiusPolicyName,
       "tmnxRadiusUserServerIndex": tmnxRadiusUserServerIndex,
       "tmnxRadiusUserReqTx": tmnxRadiusUserReqTx,
       "tmnxRadiusUserReqRx": tmnxRadiusUserReqRx,
       "tmnxRadiusUserOpenFail": tmnxRadiusUserOpenFail,
       "tmnxRadiusUserBindFail": tmnxRadiusUserBindFail,
       "tmnxRadiusUserSendFail": tmnxRadiusUserSendFail,
       "tmnxRadiusUserRecvFail": tmnxRadiusUserRecvFail,
       "tmnxRadiusUserSendTimeout": tmnxRadiusUserSendTimeout,
       "tmnxRadiusUserLoginPass": tmnxRadiusUserLoginPass,
       "tmnxRadiusUserLoginFail": tmnxRadiusUserLoginFail,
       "tmnxRadiusUserMd5Fail": tmnxRadiusUserMd5Fail,
       "tmnxRadiusUserPending": tmnxRadiusUserPending,
       "tmnxRadiusUserAcctReqTx": tmnxRadiusUserAcctReqTx,
       "tmnxRadiusUserAcctRejRx": tmnxRadiusUserAcctRejRx,
       "tmnxRadiusUserAcctConnError": tmnxRadiusUserAcctConnError,
       "tmnxRadiusUserAccChallengePkt": tmnxRadiusUserAccChallengePkt,
       "tmnxRadiusUserAuthAvgDelay": tmnxRadiusUserAuthAvgDelay,
       "tmnxRadiusUserAcctAvgDelay": tmnxRadiusUserAcctAvgDelay,
       "tmnxTacPlusInfo": tmnxTacPlusInfo,
       "tmnxTacPlusAdminStatus": tmnxTacPlusAdminStatus,
       "tmnxTacPlusTimeout": tmnxTacPlusTimeout,
       "tmnxTacPlusServerTable": tmnxTacPlusServerTable,
       "tmnxTacPlusServerEntry": tmnxTacPlusServerEntry,
       "tmnxTacPlusServerIndex": tmnxTacPlusServerIndex,
       "tmnxTacPlusServerAddress": tmnxTacPlusServerAddress,
       "tmnxTacPlusServerSecret": tmnxTacPlusServerSecret,
       "tmnxTacPlusServerRowStatus": tmnxTacPlusServerRowStatus,
       "tmnxTacPlusServerOperStatus": tmnxTacPlusServerOperStatus,
       "tmnxTacPlusServerInetAddressType": tmnxTacPlusServerInetAddressType,
       "tmnxTacPlusServerInetAddress": tmnxTacPlusServerInetAddress,
       "tmnxTacPlusServerPort": tmnxTacPlusServerPort,
       "tmnxTacPlusAccounting": tmnxTacPlusAccounting,
       "tmnxTacPlusAcctRecType": tmnxTacPlusAcctRecType,
       "tmnxTacPlusAuthorization": tmnxTacPlusAuthorization,
       "tmnxTacPlusSingleConnection": tmnxTacPlusSingleConnection,
       "tmnxTacPlusSourceAddress": tmnxTacPlusSourceAddress,
       "tmnxTacPlusConfigured": tmnxTacPlusConfigured,
       "tmnxTacplusUseTemplate": tmnxTacplusUseTemplate,
       "tmnxTacPlusInteractiveAuthen": tmnxTacPlusInteractiveAuthen,
       "tmnxTacPlusAuthorUsePrivLvl": tmnxTacPlusAuthorUsePrivLvl,
       "tmnxServerCtlObjs": tmnxServerCtlObjs,
       "tmnxEnableServers": tmnxEnableServers,
       "tmnxTelnetServerOperStatus": tmnxTelnetServerOperStatus,
       "tmnxSSHServerOperStatus": tmnxSSHServerOperStatus,
       "tmnxFTPServerOperStatus": tmnxFTPServerOperStatus,
       "tmnxTelnet6ServerOperStatus": tmnxTelnet6ServerOperStatus,
       "tmnxCpmSecurityObjs": tmnxCpmSecurityObjs,
       "tmnxCpmPerPeerQueuing": tmnxCpmPerPeerQueuing,
       "tmnxCpmQueuesTotal": tmnxCpmQueuesTotal,
       "tmnxCpmQueuesInUse": tmnxCpmQueuesInUse,
       "tCpmFilterQueueTable": tCpmFilterQueueTable,
       "tCpmFilterQueueEntry": tCpmFilterQueueEntry,
       "tCpmFilterQueueId": tCpmFilterQueueId,
       "tCpmFilterQueueRowStatus": tCpmFilterQueueRowStatus,
       "tCpmFilterQueueLastChanged": tCpmFilterQueueLastChanged,
       "tCpmFilterQueueAdminPIR": tCpmFilterQueueAdminPIR,
       "tCpmFilterQueueAdminCIR": tCpmFilterQueueAdminCIR,
       "tCpmFilterQueueCBS": tCpmFilterQueueCBS,
       "tCpmFilterQueueMBS": tCpmFilterQueueMBS,
       "tCpmFilterQueueReferences": tCpmFilterQueueReferences,
       "tCpmFilterQueueOperPIR": tCpmFilterQueueOperPIR,
       "tCpmFilterQueueOperCIR": tCpmFilterQueueOperCIR,
       "tmnxCpmHwFilterObjs": tmnxCpmHwFilterObjs,
       "tCpmFilterDefaultAction": tCpmFilterDefaultAction,
       "tCpmIpFilterAdminState": tCpmIpFilterAdminState,
       "tCpmIPv6FilterAdminState": tCpmIPv6FilterAdminState,
       "tCpmMacFilterAdminState": tCpmMacFilterAdminState,
       "tCpmIpFilterTable": tCpmIpFilterTable,
       "tCpmIpFilterEntry": tCpmIpFilterEntry,
       "tCpmIpFilterEntryId": tCpmIpFilterEntryId,
       "tCpmIpFilterEntryRowStatus": tCpmIpFilterEntryRowStatus,
       "tCpmIpFilterEntryLastChanged": tCpmIpFilterEntryLastChanged,
       "tCpmIpFilterEntryLogId": tCpmIpFilterEntryLogId,
       "tCpmIpFilterEntryDescription": tCpmIpFilterEntryDescription,
       "tCpmIpFilterEntryAction": tCpmIpFilterEntryAction,
       "tCpmIpFilterEntryQueueId": tCpmIpFilterEntryQueueId,
       "tCpmIpFilterEntrySrcIPAddr": tCpmIpFilterEntrySrcIPAddr,
       "tCpmIpFilterEntrySrcIPMask": tCpmIpFilterEntrySrcIPMask,
       "tCpmIpFilterEntryDestIPAddr": tCpmIpFilterEntryDestIPAddr,
       "tCpmIpFilterEntryDestIPMask": tCpmIpFilterEntryDestIPMask,
       "tCpmIpFilterEntryProtocol": tCpmIpFilterEntryProtocol,
       "tCpmIpFilterEntrySrcPort": tCpmIpFilterEntrySrcPort,
       "tCpmIpFilterEntrySrcPortMask": tCpmIpFilterEntrySrcPortMask,
       "tCpmIpFilterEntryDestPort": tCpmIpFilterEntryDestPort,
       "tCpmIpFilterEntryDestPortMask": tCpmIpFilterEntryDestPortMask,
       "tCpmIpFilterEntryDSCP": tCpmIpFilterEntryDSCP,
       "tCpmIpFilterEntryFragment": tCpmIpFilterEntryFragment,
       "tCpmIpFilterEntryOptionPresent": tCpmIpFilterEntryOptionPresent,
       "tCpmIpFilterEntryIPOptionValue": tCpmIpFilterEntryIPOptionValue,
       "tCpmIpFilterEntryIPOptionMask": tCpmIpFilterEntryIPOptionMask,
       "tCpmIpFilterEntryMultipleOption": tCpmIpFilterEntryMultipleOption,
       "tCpmIpFilterEntryTcpSyn": tCpmIpFilterEntryTcpSyn,
       "tCpmIpFilterEntryTcpAck": tCpmIpFilterEntryTcpAck,
       "tCpmIpFilterEntryIcmpCode": tCpmIpFilterEntryIcmpCode,
       "tCpmIpFilterEntryIcmpType": tCpmIpFilterEntryIcmpType,
       "tCpmIpFilterEntryVRtrId": tCpmIpFilterEntryVRtrId,
       "tCpmIpFilterEntryLogCreated": tCpmIpFilterEntryLogCreated,
       "tCpmIpFilterEntrySrcIpPrefixList": tCpmIpFilterEntrySrcIpPrefixList,
       "tCpmIpFilterEntryDstIpPrefixList": tCpmIpFilterEntryDstIpPrefixList,
       "tCpmIpFilterEntrySrcPortHigh": tCpmIpFilterEntrySrcPortHigh,
       "tCpmIpFilterEntrySrcPortOper": tCpmIpFilterEntrySrcPortOper,
       "tCpmIpFilterEntryDestPortHigh": tCpmIpFilterEntryDestPortHigh,
       "tCpmIpFilterEntryDestPortOper": tCpmIpFilterEntryDestPortOper,
       "tCpmIpFilterEntrySrcPortList": tCpmIpFilterEntrySrcPortList,
       "tCpmIpFilterEntryDstPortList": tCpmIpFilterEntryDstPortList,
       "tCpmIpFilterEntryPortSelector": tCpmIpFilterEntryPortSelector,
       "tCpmIpFilterStatsTable": tCpmIpFilterStatsTable,
       "tCpmIpFilterStatsEntry": tCpmIpFilterStatsEntry,
       "tCpmIpFilterStatsDroppedPkts": tCpmIpFilterStatsDroppedPkts,
       "tCpmIpFilterStatsForwardedPkts": tCpmIpFilterStatsForwardedPkts,
       "tCpmFilterQueueStatsTable": tCpmFilterQueueStatsTable,
       "tCpmFilterQueueStatsEntry": tCpmFilterQueueStatsEntry,
       "tCpmFilterQInProfileDropPkts": tCpmFilterQInProfileDropPkts,
       "tCpmFilterQInProfileFwdPkts": tCpmFilterQInProfileFwdPkts,
       "tCpmFilterQInProfileDropOctets": tCpmFilterQInProfileDropOctets,
       "tCpmFilterQInProfileFwdOctets": tCpmFilterQInProfileFwdOctets,
       "tCpmFilterQOutProfileDropPkts": tCpmFilterQOutProfileDropPkts,
       "tCpmFilterQOutProfileFwdPkts": tCpmFilterQOutProfileFwdPkts,
       "tCpmFilterQOutProfileDropOctets": tCpmFilterQOutProfileDropOctets,
       "tCpmFilterQOutProfileFwdOctets": tCpmFilterQOutProfileFwdOctets,
       "tCpmIPv6FilterTable": tCpmIPv6FilterTable,
       "tCpmIPv6FilterEntry": tCpmIPv6FilterEntry,
       "tCpmIPv6FilterEntryId": tCpmIPv6FilterEntryId,
       "tCpmIPv6FilterEntryRowStatus": tCpmIPv6FilterEntryRowStatus,
       "tCpmIPv6FilterEntryLastChanged": tCpmIPv6FilterEntryLastChanged,
       "tCpmIPv6FilterEntryLogId": tCpmIPv6FilterEntryLogId,
       "tCpmIPv6FilterEntryDescription": tCpmIPv6FilterEntryDescription,
       "tCpmIPv6FilterEntryAction": tCpmIPv6FilterEntryAction,
       "tCpmIPv6FilterEntryQueueId": tCpmIPv6FilterEntryQueueId,
       "tCpmIPv6FilterEntrySrcIPAddr": tCpmIPv6FilterEntrySrcIPAddr,
       "tCpmIPv6FilterEntrySrcIPMask": tCpmIPv6FilterEntrySrcIPMask,
       "tCpmIPv6FilterEntryDestIPAddr": tCpmIPv6FilterEntryDestIPAddr,
       "tCpmIPv6FilterEntryDestIPMask": tCpmIPv6FilterEntryDestIPMask,
       "tCpmIPv6FilterEntryNextHeader": tCpmIPv6FilterEntryNextHeader,
       "tCpmIPv6FilterEntrySrcPort": tCpmIPv6FilterEntrySrcPort,
       "tCpmIPv6FilterEntrySrcPortMask": tCpmIPv6FilterEntrySrcPortMask,
       "tCpmIPv6FilterEntryDestPort": tCpmIPv6FilterEntryDestPort,
       "tCpmIPv6FilterEntryDestPortMask": tCpmIPv6FilterEntryDestPortMask,
       "tCpmIPv6FilterEntryDSCP": tCpmIPv6FilterEntryDSCP,
       "tCpmIPv6FilterEntryTcpSyn": tCpmIPv6FilterEntryTcpSyn,
       "tCpmIPv6FilterEntryTcpAck": tCpmIPv6FilterEntryTcpAck,
       "tCpmIPv6FilterEntryIcmpCode": tCpmIPv6FilterEntryIcmpCode,
       "tCpmIPv6FilterEntryIcmpType": tCpmIPv6FilterEntryIcmpType,
       "tCpmIPv6FilterEntryVRtrId": tCpmIPv6FilterEntryVRtrId,
       "tCpmIPv6FilterEntryLogCreated": tCpmIPv6FilterEntryLogCreated,
       "tCpmIPv6FilterEntryFlowLabel": tCpmIPv6FilterEntryFlowLabel,
       "tCpmIPv6FilterEntrySrcIpPfxList": tCpmIPv6FilterEntrySrcIpPfxList,
       "tCpmIPv6FilterEntryDstIpPfxList": tCpmIPv6FilterEntryDstIpPfxList,
       "tCpmIPv6FilterEntrySrcPortHigh": tCpmIPv6FilterEntrySrcPortHigh,
       "tCpmIPv6FilterEntrySrcPortOper": tCpmIPv6FilterEntrySrcPortOper,
       "tCpmIPv6FilterEntryDestPortHigh": tCpmIPv6FilterEntryDestPortHigh,
       "tCpmIPv6FilterEntryDestPortOper": tCpmIPv6FilterEntryDestPortOper,
       "tCpmIPv6FilterEntrySrcPortList": tCpmIPv6FilterEntrySrcPortList,
       "tCpmIPv6FilterEntryDstPortList": tCpmIPv6FilterEntryDstPortList,
       "tCpmIPv6FilterEntryPortSelector": tCpmIPv6FilterEntryPortSelector,
       "tCpmIPv6FilterEntryFragment": tCpmIPv6FilterEntryFragment,
       "tCpmIPv6FilterEntryHopByHopOpt": tCpmIPv6FilterEntryHopByHopOpt,
       "tCpmIPv6FilterStatsTable": tCpmIPv6FilterStatsTable,
       "tCpmIPv6FilterStatsEntry": tCpmIPv6FilterStatsEntry,
       "tCpmIPv6FilterStatsDroppedPkts": tCpmIPv6FilterStatsDroppedPkts,
       "tCpmIPv6FilterStatsForwardedPkts": tCpmIPv6FilterStatsForwardedPkts,
       "tmnxCpmProtPolTableLastChanged": tmnxCpmProtPolTableLastChanged,
       "tmnxCpmProtPolTable": tmnxCpmProtPolTable,
       "tmnxCpmProtPolEntry": tmnxCpmProtPolEntry,
       "tmnxCpmProtPolicyId": tmnxCpmProtPolicyId,
       "tmnxCpmProtPolRowStatus": tmnxCpmProtPolRowStatus,
       "tmnxCpmProtPolLastChanged": tmnxCpmProtPolLastChanged,
       "tmnxCpmProtPolDescription": tmnxCpmProtPolDescription,
       "tmnxCpmProtPolPerSrcRateLimit": tmnxCpmProtPolPerSrcRateLimit,
       "tmnxCpmProtPolOverallRateLimit": tmnxCpmProtPolOverallRateLimit,
       "tmnxCpmProtPolAlarm": tmnxCpmProtPolAlarm,
       "tmnxCpmProtPolOutProfileRate": tmnxCpmProtPolOutProfileRate,
       "tmnxCpmProtPolLimDhcpCiAddrZero": tmnxCpmProtPolLimDhcpCiAddrZero,
       "tmnxCpmProtPolOutProfRateLogEvnt": tmnxCpmProtPolOutProfRateLogEvnt,
       "tmnxCpmProtDropUncfgdProtocolMsg": tmnxCpmProtDropUncfgdProtocolMsg,
       "tmnxCpmProtLinkRateLimit": tmnxCpmProtLinkRateLimit,
       "tmnxCpmProtExcdTableLastChanged": tmnxCpmProtExcdTableLastChanged,
       "tmnxCpmProtExcdTable": tmnxCpmProtExcdTable,
       "tmnxCpmProtExcdEntry": tmnxCpmProtExcdEntry,
       "tmnxCpmProtExcdMac": tmnxCpmProtExcdMac,
       "tmnxCpmProtExcdPeriods": tmnxCpmProtExcdPeriods,
       "tmnxCpmProtExcdTimeStarted": tmnxCpmProtExcdTimeStarted,
       "tmnxCpmProtExcdTime": tmnxCpmProtExcdTime,
       "tmnxCpmProtViolPortTableLastChgd": tmnxCpmProtViolPortTableLastChgd,
       "tmnxCpmProtViolPortTable": tmnxCpmProtViolPortTable,
       "tmnxCpmProtViolPortEntry": tmnxCpmProtViolPortEntry,
       "tmnxCpmProtViolPortPeriods": tmnxCpmProtViolPortPeriods,
       "tmnxCpmProtViolPortTimeStarted": tmnxCpmProtViolPortTimeStarted,
       "tmnxCpmProtViolPortTime": tmnxCpmProtViolPortTime,
       "tmnxCpmProtViolPortAggPeriods": tmnxCpmProtViolPortAggPeriods,
       "tmnxCpmProtViolPortAggTimeStart": tmnxCpmProtViolPortAggTimeStart,
       "tmnxCpmProtViolPortAggTime": tmnxCpmProtViolPortAggTime,
       "tmnxCpmProtViolIfTableLastChgd": tmnxCpmProtViolIfTableLastChgd,
       "tmnxCpmProtViolIfTable": tmnxCpmProtViolIfTable,
       "tmnxCpmProtViolIfEntry": tmnxCpmProtViolIfEntry,
       "tmnxCpmProtViolIfPeriods": tmnxCpmProtViolIfPeriods,
       "tmnxCpmProtViolIfTimeStarted": tmnxCpmProtViolIfTimeStarted,
       "tmnxCpmProtViolIfTime": tmnxCpmProtViolIfTime,
       "tmnxCpmProtViolSapTableLastChgd": tmnxCpmProtViolSapTableLastChgd,
       "tmnxCpmProtViolSapTable": tmnxCpmProtViolSapTable,
       "tmnxCpmProtViolSapEntry": tmnxCpmProtViolSapEntry,
       "tmnxCpmProtViolSapPeriods": tmnxCpmProtViolSapPeriods,
       "tmnxCpmProtViolSapTimeStarted": tmnxCpmProtViolSapTimeStarted,
       "tmnxCpmProtViolSapTime": tmnxCpmProtViolSapTime,
       "tmnxCpmProtPortOverallRateLimit": tmnxCpmProtPortOverallRateLimit,
       "tmnxCpmProtDetectPeriod": tmnxCpmProtDetectPeriod,
       "tCpmMacFilterTable": tCpmMacFilterTable,
       "tCpmMacFilterEntry": tCpmMacFilterEntry,
       "tCpmMacFltrEntryId": tCpmMacFltrEntryId,
       "tCpmMacFltrEntryRowStatus": tCpmMacFltrEntryRowStatus,
       "tCpmMacFltrEntryLastChanged": tCpmMacFltrEntryLastChanged,
       "tCpmMacFltrEntryLogId": tCpmMacFltrEntryLogId,
       "tCpmMacFltrEntryDescription": tCpmMacFltrEntryDescription,
       "tCpmMacFltrEntryAction": tCpmMacFltrEntryAction,
       "tCpmMacFltrEntryQueueId": tCpmMacFltrEntryQueueId,
       "tCpmMacFltrEntryFrameType": tCpmMacFltrEntryFrameType,
       "tCpmMacFltrEntrySvcId": tCpmMacFltrEntrySvcId,
       "tCpmMacFltrEntryDot1pValue": tCpmMacFltrEntryDot1pValue,
       "tCpmMacFltrEntryDot1pMask": tCpmMacFltrEntryDot1pMask,
       "tCpmMacFltrEntryDsap": tCpmMacFltrEntryDsap,
       "tCpmMacFltrEntryDsapMask": tCpmMacFltrEntryDsapMask,
       "tCpmMacFltrEntrySrcMAC": tCpmMacFltrEntrySrcMAC,
       "tCpmMacFltrEntrySrcMACMask": tCpmMacFltrEntrySrcMACMask,
       "tCpmMacFltrEntryDstMAC": tCpmMacFltrEntryDstMAC,
       "tCpmMacFltrEntryDstMACMask": tCpmMacFltrEntryDstMACMask,
       "tCpmMacFltrEntryEtherType": tCpmMacFltrEntryEtherType,
       "tCpmMacFltrEntrySsap": tCpmMacFltrEntrySsap,
       "tCpmMacFltrEntrySsapMask": tCpmMacFltrEntrySsapMask,
       "tCpmMacFltrEntryCfmOpCodeOper": tCpmMacFltrEntryCfmOpCodeOper,
       "tCpmMacFltrEntryCfmOpCodeValue1": tCpmMacFltrEntryCfmOpCodeValue1,
       "tCpmMacFltrEntryCfmOpCodeValue2": tCpmMacFltrEntryCfmOpCodeValue2,
       "tCpmMacFltrEntryLogCreated": tCpmMacFltrEntryLogCreated,
       "tCpmMacFilterStatsTable": tCpmMacFilterStatsTable,
       "tCpmMacFilterStatsEntry": tCpmMacFilterStatsEntry,
       "tCpmMacFilterStatsDroppedPkts": tCpmMacFilterStatsDroppedPkts,
       "tCpmMacFilterStatsForwardedPkts": tCpmMacFilterStatsForwardedPkts,
       "tmnxCpmProtAllowShamLinkPackets": tmnxCpmProtAllowShamLinkPackets,
       "tmnxCpmProtViolVdoSvcTable": tmnxCpmProtViolVdoSvcTable,
       "tmnxCpmProtViolVdoSvcEntry": tmnxCpmProtViolVdoSvcEntry,
       "tmnxCpmProtViolVdoSvcCltAddrType": tmnxCpmProtViolVdoSvcCltAddrType,
       "tmnxCpmProtViolVdoSvcCltAddr": tmnxCpmProtViolVdoSvcCltAddr,
       "tmnxCpmProtViolVdoSvcPeriods": tmnxCpmProtViolVdoSvcPeriods,
       "tmnxCpmProtViolVdoSvcTimeStarted": tmnxCpmProtViolVdoSvcTimeStarted,
       "tmnxCpmProtViolVdoSvcTime": tmnxCpmProtViolVdoSvcTime,
       "tmnxCpmProtViolVdoSvcVrtrIfIndex": tmnxCpmProtViolVdoSvcVrtrIfIndex,
       "tmnxCpmProtViolVdoVrtrTable": tmnxCpmProtViolVdoVrtrTable,
       "tmnxCpmProtViolVdoVrtrEntry": tmnxCpmProtViolVdoVrtrEntry,
       "tmnxCpmProtViolVdoVrtrCltAdrType": tmnxCpmProtViolVdoVrtrCltAdrType,
       "tmnxCpmProtViolVdoVrtrCltAddr": tmnxCpmProtViolVdoVrtrCltAddr,
       "tmnxCpmProtViolVdoVrtrPeriods": tmnxCpmProtViolVdoVrtrPeriods,
       "tmnxCpmProtViolVdoVrtrTimeStart": tmnxCpmProtViolVdoVrtrTimeStart,
       "tmnxCpmProtViolVdoVrtrTime": tmnxCpmProtViolVdoVrtrTime,
       "tmnxCpmProtViolVdoVrtrSvcId": tmnxCpmProtViolVdoVrtrSvcId,
       "tmnxCpmProtViolVdoVrtrIfIndex": tmnxCpmProtViolVdoVrtrIfIndex,
       "tmnxCpmProtEthCfmPolTableLastChg": tmnxCpmProtEthCfmPolTableLastChg,
       "tmnxCpmProtEthCfmPolTable": tmnxCpmProtEthCfmPolTable,
       "tmnxCpmProtEthCfmPolEntry": tmnxCpmProtEthCfmPolEntry,
       "tmnxCpmProtEthCfmPolEntryNum": tmnxCpmProtEthCfmPolEntryNum,
       "tmnxCpmProtEthCfmPolRowStatus": tmnxCpmProtEthCfmPolRowStatus,
       "tmnxCpmProtEthCfmPolLastChanged": tmnxCpmProtEthCfmPolLastChanged,
       "tmnxCpmProtEthCfmPolLevelSet": tmnxCpmProtEthCfmPolLevelSet,
       "tmnxCpmProtEthCfmPolOpCodeSet": tmnxCpmProtEthCfmPolOpCodeSet,
       "tmnxCpmProtEthCfmPolRateLimit": tmnxCpmProtEthCfmPolRateLimit,
       "tmnxCpmProtViolSdpBindTblLastChg": tmnxCpmProtViolSdpBindTblLastChg,
       "tmnxCpmProtViolSdpBindTable": tmnxCpmProtViolSdpBindTable,
       "tmnxCpmProtViolSdpBindEntry": tmnxCpmProtViolSdpBindEntry,
       "tmnxCpmProtViolSdpBindPeriods": tmnxCpmProtViolSdpBindPeriods,
       "tmnxCpmProtViolSdpBindTimeStartd": tmnxCpmProtViolSdpBindTimeStartd,
       "tmnxCpmProtViolSdpBindTime": tmnxCpmProtViolSdpBindTime,
       "tmnxCpmProtExcdSdpBindTblLastChg": tmnxCpmProtExcdSdpBindTblLastChg,
       "tmnxCpmProtExcdSdpBindTable": tmnxCpmProtExcdSdpBindTable,
       "tmnxCpmProtExcdSdpBindEntry": tmnxCpmProtExcdSdpBindEntry,
       "tmnxCpmProtExcdSdpBindMac": tmnxCpmProtExcdSdpBindMac,
       "tmnxCpmProtExcdSdpBindPeriods": tmnxCpmProtExcdSdpBindPeriods,
       "tmnxCpmProtExcdSdpBindTimeStartd": tmnxCpmProtExcdSdpBindTimeStartd,
       "tmnxCpmProtExcdSdpBindTime": tmnxCpmProtExcdSdpBindTime,
       "tmnxCpmProtExcdSdpBindEcmTblLChg": tmnxCpmProtExcdSdpBindEcmTblLChg,
       "tmnxCpmProtExcdSdpBindEcmTable": tmnxCpmProtExcdSdpBindEcmTable,
       "tmnxCpmProtExcdSdpBindEcmEntry": tmnxCpmProtExcdSdpBindEcmEntry,
       "tmnxCpmProtExcdSdpBindEcmMac": tmnxCpmProtExcdSdpBindEcmMac,
       "tmnxCpmProtExcdSdpBindEcmLevel": tmnxCpmProtExcdSdpBindEcmLevel,
       "tmnxCpmProtExcdSdpBindEcmOpCode": tmnxCpmProtExcdSdpBindEcmOpCode,
       "tmnxCpmProtExcdSdpBindEcmPeriods": tmnxCpmProtExcdSdpBindEcmPeriods,
       "tmnxCpmProtExcdSdpBindEcmStarted": tmnxCpmProtExcdSdpBindEcmStarted,
       "tmnxCpmProtExcdSdpBindEcmTime": tmnxCpmProtExcdSdpBindEcmTime,
       "tmnxCpmProtExcdSapEcmTblLChg": tmnxCpmProtExcdSapEcmTblLChg,
       "tmnxCpmProtExcdSapEcmTable": tmnxCpmProtExcdSapEcmTable,
       "tmnxCpmProtExcdSapEcmEntry": tmnxCpmProtExcdSapEcmEntry,
       "tmnxCpmProtExcdSapEcmMac": tmnxCpmProtExcdSapEcmMac,
       "tmnxCpmProtExcdSapEcmLevel": tmnxCpmProtExcdSapEcmLevel,
       "tmnxCpmProtExcdSapEcmOpCode": tmnxCpmProtExcdSapEcmOpCode,
       "tmnxCpmProtExcdSapEcmPeriods": tmnxCpmProtExcdSapEcmPeriods,
       "tmnxCpmProtExcdSapEcmStarted": tmnxCpmProtExcdSapEcmStarted,
       "tmnxCpmProtExcdSapEcmTime": tmnxCpmProtExcdSapEcmTime,
       "tmnxCpmVprnNwExceptions": tmnxCpmVprnNwExceptions,
       "tmnxCpmNumVprnNwExceptions": tmnxCpmNumVprnNwExceptions,
       "tmnxCpmVprnNwExceptionsTime": tmnxCpmVprnNwExceptionsTime,
       "tmnxCpmProtExcdSapIpTableLastChg": tmnxCpmProtExcdSapIpTableLastChg,
       "tmnxCpmProtExcdSapIpTable": tmnxCpmProtExcdSapIpTable,
       "tmnxCpmProtExcdSapIpEntry": tmnxCpmProtExcdSapIpEntry,
       "tmnxCpmProtExcdSapIpAddrType": tmnxCpmProtExcdSapIpAddrType,
       "tmnxCpmProtExcdSapIpAddr": tmnxCpmProtExcdSapIpAddr,
       "tmnxCpmProtExcdSapIpPeriods": tmnxCpmProtExcdSapIpPeriods,
       "tmnxCpmProtExcdSapIpStarted": tmnxCpmProtExcdSapIpStarted,
       "tmnxCpmProtExcdSapIpTime": tmnxCpmProtExcdSapIpTime,
       "tmnxDCpuProtPolicyTblLstChg": tmnxDCpuProtPolicyTblLstChg,
       "tmnxDCpuProtPolicyTable": tmnxDCpuProtPolicyTable,
       "tmnxDCpuProtPolicyEntry": tmnxDCpuProtPolicyEntry,
       "tmnxDCpuProtPolicyName": tmnxDCpuProtPolicyName,
       "tmnxDCpuProtPolicyRowStatus": tmnxDCpuProtPolicyRowStatus,
       "tmnxDCpuProtPolicyLastMdfy": tmnxDCpuProtPolicyLastMdfy,
       "tmnxDCpuProtPolicyDescr": tmnxDCpuProtPolicyDescr,
       "tmnxDCpuProtStaticPlcrTblLstChg": tmnxDCpuProtStaticPlcrTblLstChg,
       "tmnxDCpuProtStaticPlcrTable": tmnxDCpuProtStaticPlcrTable,
       "tmnxDCpuProtStaticPlcrEntry": tmnxDCpuProtStaticPlcrEntry,
       "tmnxDCpuProtStaticPlcrName": tmnxDCpuProtStaticPlcrName,
       "tmnxDCpuProtStaticPlcrRowStatus": tmnxDCpuProtStaticPlcrRowStatus,
       "tmnxDCpuProtStaticPlcrLastMdfy": tmnxDCpuProtStaticPlcrLastMdfy,
       "tmnxDCpuProtStaticPlcrDescr": tmnxDCpuProtStaticPlcrDescr,
       "tmnxDCpuProtStaticPlcrPackets": tmnxDCpuProtStaticPlcrPackets,
       "tmnxDCpuProtStaticPlcrWithin": tmnxDCpuProtStaticPlcrWithin,
       "tmnxDCpuProtStaticPlcrInitDelay": tmnxDCpuProtStaticPlcrInitDelay,
       "tmnxDCpuProtStaticPlcrKbps": tmnxDCpuProtStaticPlcrKbps,
       "tmnxDCpuProtStaticPlcrMbs": tmnxDCpuProtStaticPlcrMbs,
       "tmnxDCpuProtStaticPlcrExdActn": tmnxDCpuProtStaticPlcrExdActn,
       "tmnxDCpuProtStaticPlcrExdHold": tmnxDCpuProtStaticPlcrExdHold,
       "tmnxDCpuProtStaticPlcrRateType": tmnxDCpuProtStaticPlcrRateType,
       "tmnxDCpuProtStaticPlcrDectnTime": tmnxDCpuProtStaticPlcrDectnTime,
       "tmnxDCpuProtStaticPlcrLogEvent": tmnxDCpuProtStaticPlcrLogEvent,
       "tmnxDCpuProtLocMonPlcrTblLstChg": tmnxDCpuProtLocMonPlcrTblLstChg,
       "tmnxDCpuProtLocMonPlcrTable": tmnxDCpuProtLocMonPlcrTable,
       "tmnxDCpuProtLocMonPlcrEntry": tmnxDCpuProtLocMonPlcrEntry,
       "tmnxDCpuProtLocMonPlcrName": tmnxDCpuProtLocMonPlcrName,
       "tmnxDCpuProtLocMonPlcrRowStatus": tmnxDCpuProtLocMonPlcrRowStatus,
       "tmnxDCpuProtLocMonPlcrLastMdfy": tmnxDCpuProtLocMonPlcrLastMdfy,
       "tmnxDCpuProtLocMonPlcrDescr": tmnxDCpuProtLocMonPlcrDescr,
       "tmnxDCpuProtLocMonPlcrPackets": tmnxDCpuProtLocMonPlcrPackets,
       "tmnxDCpuProtLocMonPlcrWithin": tmnxDCpuProtLocMonPlcrWithin,
       "tmnxDCpuProtLocMonPlcrInitDelay": tmnxDCpuProtLocMonPlcrInitDelay,
       "tmnxDCpuProtLocMonPlcrKbps": tmnxDCpuProtLocMonPlcrKbps,
       "tmnxDCpuProtLocMonPlcrMbs": tmnxDCpuProtLocMonPlcrMbs,
       "tmnxDCpuProtLocMonPlcrExcdActn": tmnxDCpuProtLocMonPlcrExcdActn,
       "tmnxDCpuProtLocMonPlcrRateType": tmnxDCpuProtLocMonPlcrRateType,
       "tmnxDCpuProtLocMonPlcrLogEvent": tmnxDCpuProtLocMonPlcrLogEvent,
       "tmnxDCpuProtProtocolTblLstChg": tmnxDCpuProtProtocolTblLstChg,
       "tmnxDCpuProtProtocolTable": tmnxDCpuProtProtocolTable,
       "tmnxDCpuProtProtocolEntry": tmnxDCpuProtProtocolEntry,
       "tmnxDCpuProtProtocol": tmnxDCpuProtProtocol,
       "tmnxDCpuProtProtocolRowStatus": tmnxDCpuProtProtocolRowStatus,
       "tmnxDCpuProtProtocolLastMdfy": tmnxDCpuProtProtocolLastMdfy,
       "tmnxDCpuProtProtocolEnforce": tmnxDCpuProtProtocolEnforce,
       "tmnxDCpuProtProtocolEnfrcePolNme": tmnxDCpuProtProtocolEnfrcePolNme,
       "tmnxDCpuProtProtocolDynPackets": tmnxDCpuProtProtocolDynPackets,
       "tmnxDCpuProtProtocolDynWithin": tmnxDCpuProtProtocolDynWithin,
       "tmnxDCpuProtProtocolDynInitDly": tmnxDCpuProtProtocolDynInitDly,
       "tmnxDCpuProtProtocolDynKbps": tmnxDCpuProtProtocolDynKbps,
       "tmnxDCpuProtProtocolDynMbs": tmnxDCpuProtProtocolDynMbs,
       "tmnxDCpuProtProtocolDynDectnTime": tmnxDCpuProtProtocolDynDectnTime,
       "tmnxDCpuProtProtocolDynExdActn": tmnxDCpuProtProtocolDynExdActn,
       "tmnxDCpuProtProtocolDynExdHold": tmnxDCpuProtProtocolDynExdHold,
       "tmnxDCpuProtProtocolDynRateType": tmnxDCpuProtProtocolDynRateType,
       "tmnxDCpuProtProtocolDynLogEvent": tmnxDCpuProtProtocolDynLogEvent,
       "tmnxCpmProtBlockPIMTunneled": tmnxCpmProtBlockPIMTunneled,
       "tmnxCpmProtPortRateActionLowPrio": tmnxCpmProtPortRateActionLowPrio,
       "tmnxCpmProtIPSrcMonDhcp": tmnxCpmProtIPSrcMonDhcp,
       "tmnxCpmProtIPSrcMonGtp": tmnxCpmProtIPSrcMonGtp,
       "tmnxCpmProtIPSrcMonIcmp": tmnxCpmProtIPSrcMonIcmp,
       "tmnxCpmProtIPSrcMonIgmp": tmnxCpmProtIPSrcMonIgmp,
       "tCpmProtOutProfViolIfTable": tCpmProtOutProfViolIfTable,
       "tCpmProtOutProfViolIfEntry": tCpmProtOutProfViolIfEntry,
       "tCpmProtOutProfViolIfPeriods": tCpmProtOutProfViolIfPeriods,
       "tCpmProtOutProfViolIfTimeStart": tCpmProtOutProfViolIfTimeStart,
       "tCpmProtOutProfViolIfTime": tCpmProtOutProfViolIfTime,
       "tCpmProtOutProfViolSapTable": tCpmProtOutProfViolSapTable,
       "tCpmProtOutProfViolSapEntry": tCpmProtOutProfViolSapEntry,
       "tCpmProtOutProfViolSapPeriods": tCpmProtOutProfViolSapPeriods,
       "tCpmProtOutProfViolSapTimeStart": tCpmProtOutProfViolSapTimeStart,
       "tCpmProtOutProfViolSapTime": tCpmProtOutProfViolSapTime,
       "tCpmProtOutProfViolSdpBindTable": tCpmProtOutProfViolSdpBindTable,
       "tCpmProtOutProfViolSdpBindEntry": tCpmProtOutProfViolSdpBindEntry,
       "tCpmProtOutProfViolSdpBindPeriod": tCpmProtOutProfViolSdpBindPeriod,
       "tCpmProtOutProfViolSdpBindTmeStr": tCpmProtOutProfViolSdpBindTmeStr,
       "tCpmProtOutProfViolSdpBindTime": tCpmProtOutProfViolSdpBindTime,
       "tmnxCpmProtExcdSdpBindIpTable": tmnxCpmProtExcdSdpBindIpTable,
       "tmnxCpmProtExcdSdpBindIpEntry": tmnxCpmProtExcdSdpBindIpEntry,
       "tmnxCpmProtExcdSdpBindIpAddrType": tmnxCpmProtExcdSdpBindIpAddrType,
       "tmnxCpmProtExcdSdpBindIpAddr": tmnxCpmProtExcdSdpBindIpAddr,
       "tmnxCpmProtExcdSdpBindIpPeriods": tmnxCpmProtExcdSdpBindIpPeriods,
       "tmnxCpmProtExcdSdpBindIpStarted": tmnxCpmProtExcdSdpBindIpStarted,
       "tmnxCpmProtExcdSdpBindIpTime": tmnxCpmProtExcdSdpBindIpTime,
       "tmnxPasswordHashObjs": tmnxPasswordHashObjs,
       "tmnxPassHashReadVersion": tmnxPassHashReadVersion,
       "tmnxPassHashWriteVersion": tmnxPassHashWriteVersion,
       "tmnxSSHServerObjs": tmnxSSHServerObjs,
       "tmnxSSHServerPreserveKey": tmnxSSHServerPreserveKey,
       "tmnxSSHServerVersion": tmnxSSHServerVersion,
       "tmnxSourceIPTable": tmnxSourceIPTable,
       "tmnxSourceIPEntry": tmnxSourceIPEntry,
       "tmnxSourceIPProtoApp": tmnxSourceIPProtoApp,
       "tmnxSourceIPRowStatus": tmnxSourceIPRowStatus,
       "tmnxSourceIPAddressType": tmnxSourceIPAddressType,
       "tmnxSourceIPAddress": tmnxSourceIPAddress,
       "tmnxSourceIPIfIndex": tmnxSourceIPIfIndex,
       "tmnxSourceIPOperStatus": tmnxSourceIPOperStatus,
       "tmnxUserTemplateTable": tmnxUserTemplateTable,
       "tmnxUserTemplateEntry": tmnxUserTemplateEntry,
       "tmnxTemplateName": tmnxTemplateName,
       "tmnxTemplateAccess": tmnxTemplateAccess,
       "tmnxTemplateHomeDirectory": tmnxTemplateHomeDirectory,
       "tmnxTemplateRestrictedToHome": tmnxTemplateRestrictedToHome,
       "tmnxTemplateConsoleLoginExecFile": tmnxTemplateConsoleLoginExecFile,
       "tmnxTemplateProfile": tmnxTemplateProfile,
       "tmnxKeyChainTable": tmnxKeyChainTable,
       "tmnxKeyChainEntry": tmnxKeyChainEntry,
       "tmnxKeyChainName": tmnxKeyChainName,
       "tmnxKeyChainRowStatus": tmnxKeyChainRowStatus,
       "tmnxKeyChainDescription": tmnxKeyChainDescription,
       "tmnxKeyChainSendTcpOptionNum": tmnxKeyChainSendTcpOptionNum,
       "tmnxKeyChainReceiveTcpOptionNum": tmnxKeyChainReceiveTcpOptionNum,
       "tmnxKeyChainAdminState": tmnxKeyChainAdminState,
       "tmnxKeyChainOperState": tmnxKeyChainOperState,
       "tmnxKeyChainExpired": tmnxKeyChainExpired,
       "tmnxKeyChainKeyTable": tmnxKeyChainKeyTable,
       "tmnxKeyChainKeyEntry": tmnxKeyChainKeyEntry,
       "tmnxKeyChainKeyDirection": tmnxKeyChainKeyDirection,
       "tmnxKeyChainKeyID": tmnxKeyChainKeyID,
       "tmnxKeyChainKeyRowStatus": tmnxKeyChainKeyRowStatus,
       "tmnxKeyChainAuthenticationKey": tmnxKeyChainAuthenticationKey,
       "tmnxKeyChainKeyAlgorithm": tmnxKeyChainKeyAlgorithm,
       "tmnxKeyChainKeyBeginTime": tmnxKeyChainKeyBeginTime,
       "tmnxKeyChainKeyEndTime": tmnxKeyChainKeyEndTime,
       "tmnxKeyChainKeyTolerance": tmnxKeyChainKeyTolerance,
       "tmnxKeyChainKeyAdminState": tmnxKeyChainKeyAdminState,
       "tmnxKeyChainKeyOption": tmnxKeyChainKeyOption,
       "tmnxSecurityNotificationObjs": tmnxSecurityNotificationObjs,
       "tmnxKeyChainAuthFailReason": tmnxKeyChainAuthFailReason,
       "tmnxKeyChainAuthAddrType": tmnxKeyChainAuthAddrType,
       "tmnxKeyChainAuthAddr": tmnxKeyChainAuthAddr,
       "tmnxMD5AuthFailReason": tmnxMD5AuthFailReason,
       "tmnxMD5AuthAddrType": tmnxMD5AuthAddrType,
       "tmnxMD5AuthAddr": tmnxMD5AuthAddr,
       "tmnxMD5AuthKey": tmnxMD5AuthKey,
       "tmnxCpmProtPolId": tmnxCpmProtPolId,
       "tmnxSecNotifFailureReason": tmnxSecNotifFailureReason,
       "tmnxSecNotifFile": tmnxSecNotifFile,
       "tmnxSecNotifTunnelName": tmnxSecNotifTunnelName,
       "tmnxSecNotifCert": tmnxSecNotifCert,
       "tmnxSecNotifOrigProtocol": tmnxSecNotifOrigProtocol,
       "tmnxSecurityCpmProtNotificationObjs": tmnxSecurityCpmProtNotificationObjs,
       "tmnxCpmProtViolMacAddress": tmnxCpmProtViolMacAddress,
       "tmnxCpmProtViolMacPeriods": tmnxCpmProtViolMacPeriods,
       "tmnxCpmProtViolExcdPktHexDump": tmnxCpmProtViolExcdPktHexDump,
       "tmnxPkiSecurityObjs": tmnxPkiSecurityObjs,
       "tmnxPkiMaxCertChainDepth": tmnxPkiMaxCertChainDepth,
       "tmnxPkiCAProfileTableLastChanged": tmnxPkiCAProfileTableLastChanged,
       "tmnxPkiCAProfileTable": tmnxPkiCAProfileTable,
       "tmnxPkiCAProfileEntry": tmnxPkiCAProfileEntry,
       "tmnxPkiCAProfile": tmnxPkiCAProfile,
       "tmnxPkiCAProfileRowStatus": tmnxPkiCAProfileRowStatus,
       "tmnxPkiCAProfileLastChanged": tmnxPkiCAProfileLastChanged,
       "tmnxPkiCAProfileDescr": tmnxPkiCAProfileDescr,
       "tmnxPkiCAProfileCRLFile": tmnxPkiCAProfileCRLFile,
       "tmnxPkiCAProfileCertFile": tmnxPkiCAProfileCertFile,
       "tmnxPkiCAProfileAdminState": tmnxPkiCAProfileAdminState,
       "tmnxPkiCAProfileOperState": tmnxPkiCAProfileOperState,
       "tmnxPkiCAProfileOperFlags": tmnxPkiCAProfileOperFlags,
       "tmnxPkiCAProfOcspRespUrl": tmnxPkiCAProfOcspRespUrl,
       "tmnxPkiCAProfOcspSvcID": tmnxPkiCAProfOcspSvcID,
       "tmnxPkiCAProfOcspVerifyCertFile": tmnxPkiCAProfOcspVerifyCertFile,
       "tmnxPkiCAProfOcspVerifyCertCA": tmnxPkiCAProfOcspVerifyCertCA,
       "tmnxPkiCAProfOcspVerifyCertOvr": tmnxPkiCAProfOcspVerifyCertOvr,
       "tmnxPkiCAProfCmpHttpTimeout": tmnxPkiCAProfCmpHttpTimeout,
       "tmnxPkiCAProfCmpUrl": tmnxPkiCAProfCmpUrl,
       "tmnxPkiCAProfCmpSvcID": tmnxPkiCAProfCmpSvcID,
       "tmnxPkiCAProfCmpRespSignCert": tmnxPkiCAProfCmpRespSignCert,
       "tmnxPkiCAProfCmpAccUnprotErr": tmnxPkiCAProfCmpAccUnprotErr,
       "tmnxPkiCAProfCmpAccUnprotPki": tmnxPkiCAProfCmpAccUnprotPki,
       "tmnxPkiCAProfCmpSameRecipNonce": tmnxPkiCAProfCmpSameRecipNonce,
       "tmnxPkiCAProfCmpAlSetSndrForIr": tmnxPkiCAProfCmpAlSetSndrForIr,
       "tmnxPkiCAProfCmpHttpVersion": tmnxPkiCAProfCmpHttpVersion,
       "tmnxPkiCAProfRevokeChk": tmnxPkiCAProfRevokeChk,
       "tmnxPkiCAProfCmpKeyTblLastChgd": tmnxPkiCAProfCmpKeyTblLastChgd,
       "tmnxPkiCAProfCmpKeyTable": tmnxPkiCAProfCmpKeyTable,
       "tmnxPkiCAProfCmpKeyEntry": tmnxPkiCAProfCmpKeyEntry,
       "tmnxPkiCAProfCmpKeyRefnum": tmnxPkiCAProfCmpKeyRefnum,
       "tmnxPkiCAProfCmpKeyRowStatus": tmnxPkiCAProfCmpKeyRowStatus,
       "tmnxPkiCAProfCmpKeyLastChanged": tmnxPkiCAProfCmpKeyLastChanged,
       "tmnxPkiCAProfCmpKeySecret": tmnxPkiCAProfCmpKeySecret,
       "tmnxPkiCertDisplayFormat": tmnxPkiCertDisplayFormat,
       "tmnxPkiCAProfActnTable": tmnxPkiCAProfActnTable,
       "tmnxPkiCAProfActnEntry": tmnxPkiCAProfActnEntry,
       "tmnxPkiCAProfActnType": tmnxPkiCAProfActnType,
       "tmnxPkiCAProfAction": tmnxPkiCAProfAction,
       "tmnxPkiCAProfActnKey": tmnxPkiCAProfActnKey,
       "tmnxPkiCAProfActnProtAlgPass": tmnxPkiCAProfActnProtAlgPass,
       "tmnxPkiCAProfActnProtAlgRef": tmnxPkiCAProfActnProtAlgRef,
       "tmnxPkiCAProfActnProtAlgSigCert": tmnxPkiCAProfActnProtAlgSigCert,
       "tmnxPkiCAProfActnProtAlgSigHash": tmnxPkiCAProfActnProtAlgSigHash,
       "tmnxPkiCAProfActnSubjectDn": tmnxPkiCAProfActnSubjectDn,
       "tmnxPkiCAProfActnSaveAsFile": tmnxPkiCAProfActnSaveAsFile,
       "tmnxPkiCAProfActnNewKey": tmnxPkiCAProfActnNewKey,
       "tmnxPkiCAProfActnStatus": tmnxPkiCAProfActnStatus,
       "tmnxPkiCAProfActnStatusString": tmnxPkiCAProfActnStatusString,
       "tmnxPkiCAProfActnStatusCode": tmnxPkiCAProfActnStatusCode,
       "tmnxPkiCAProfActnOrigCmdTime": tmnxPkiCAProfActnOrigCmdTime,
       "tmnxPkiCAProfActnLastCAResp": tmnxPkiCAProfActnLastCAResp,
       "tmnxPkiCAProfActnSendChain": tmnxPkiCAProfActnSendChain,
       "tmnxPkiCAProfActnSendChainCA": tmnxPkiCAProfActnSendChainCA,
       "tmnxPkiCAProfActnProtKey": tmnxPkiCAProfActnProtKey,
       "tmnxCertMgrStatsGroup": tmnxCertMgrStatsGroup,
       "tmnxCertMgrAuthFailed": tmnxCertMgrAuthFailed,
       "tmnxCertMgrAuthPassed": tmnxCertMgrAuthPassed,
       "tmnxCertMgrTotalAuth": tmnxCertMgrTotalAuth,
       "tmnxUserPublicKeyObjects": tmnxUserPublicKeyObjects,
       "tmnxUserPublicKeyTable": tmnxUserPublicKeyTable,
       "tmnxUserPublicKeyEntry": tmnxUserPublicKeyEntry,
       "tmnxUserPublicKeyNumber": tmnxUserPublicKeyNumber,
       "tmnxUserPublicKeyRowStatus": tmnxUserPublicKeyRowStatus,
       "tmnxUserPublicKeyLastChanged": tmnxUserPublicKeyLastChanged,
       "tmnxUserPublicKeyName": tmnxUserPublicKeyName,
       "tmnxUserActionObjs": tmnxUserActionObjs,
       "tmnxUserActionUserName": tmnxUserActionUserName,
       "tmnxUserActionUnlock": tmnxUserActionUnlock,
       "tmnxUserActionClearPwdHistory": tmnxUserActionClearPwdHistory,
       "tmnxTacPlusPrivLvlMapTable": tmnxTacPlusPrivLvlMapTable,
       "tmnxTacPlusPrivLvlMapEntry": tmnxTacPlusPrivLvlMapEntry,
       "tmnxTacPlusPrivLvlMapPrivLvl": tmnxTacPlusPrivLvlMapPrivLvl,
       "tmnxTacPlusPrivLvlRowStatus": tmnxTacPlusPrivLvlRowStatus,
       "tmnxTacPlusPrivLvlMapUserProfile": tmnxTacPlusPrivLvlMapUserProfile,
       "tmnxOcspCacheTable": tmnxOcspCacheTable,
       "tmnxOcspCacheEntry": tmnxOcspCacheEntry,
       "tmnxOcspCacheEntryId": tmnxOcspCacheEntryId,
       "tmnxOcspCacheCertSerial": tmnxOcspCacheCertSerial,
       "tmnxOcspCacheCertIssuer": tmnxOcspCacheCertIssuer,
       "tmnxOcspCacheExpiry": tmnxOcspCacheExpiry,
       "tmnxOcspCacheCertStatus": tmnxOcspCacheCertStatus,
       "tmnxSecurityTech": tmnxSecurityTech,
       "tmnxSecurityTechSupportLocation": tmnxSecurityTechSupportLocation,
       "tmnxSSHCipherTable": tmnxSSHCipherTable,
       "tmnxSSHCipherEntry": tmnxSSHCipherEntry,
       "tmnxSSHCipherProtocolVersion": tmnxSSHCipherProtocolVersion,
       "tmnxSSHCipherNumber": tmnxSSHCipherNumber,
       "tmnxSSHCipherName": tmnxSSHCipherName,
       "tmnxSSHServerCipherListTable": tmnxSSHServerCipherListTable,
       "tmnxSSHServerCipherListEntry": tmnxSSHServerCipherListEntry,
       "tmnxSSHServerCipherListIndex": tmnxSSHServerCipherListIndex,
       "tmnxSSHServerCipherListRowStatus": tmnxSSHServerCipherListRowStatus,
       "tmnxSSHServerCipherListNumber": tmnxSSHServerCipherListNumber,
       "tmnxSSHClientCipherListTable": tmnxSSHClientCipherListTable,
       "tmnxSSHClientCipherListEntry": tmnxSSHClientCipherListEntry,
       "tmnxSSHClientCipherListIndex": tmnxSSHClientCipherListIndex,
       "tmnxSSHClientCipherListRowStatus": tmnxSSHClientCipherListRowStatus,
       "tmnxSSHClientCipherListNumber": tmnxSSHClientCipherListNumber,
       "tmnxSecurityNotifyPrefix": tmnxSecurityNotifyPrefix,
       "tmnxSecurityNotifications": tmnxSecurityNotifications,
       "tmnxSSHServerPreserveKeyFail": tmnxSSHServerPreserveKeyFail,
       "tmnxKeyChainAuthFailure": tmnxKeyChainAuthFailure,
       "tmnxCpmProtViolPort": tmnxCpmProtViolPort,
       "tmnxCpmProtViolPortAgg": tmnxCpmProtViolPortAgg,
       "tmnxCpmProtViolIf": tmnxCpmProtViolIf,
       "tmnxCpmProtViolSap": tmnxCpmProtViolSap,
       "tmnxCpmProtViolMac": tmnxCpmProtViolMac,
       "tmnxCpmProtViolVdoSvcClient": tmnxCpmProtViolVdoSvcClient,
       "tmnxCpmProtViolVdoVrtrClient": tmnxCpmProtViolVdoVrtrClient,
       "tmnxMD5AuthFailure": tmnxMD5AuthFailure,
       "tmnxCpmProtDefPolModified": tmnxCpmProtDefPolModified,
       "tmnxCpmProtViolSdpBind": tmnxCpmProtViolSdpBind,
       "tmnxCpmProtExcdSdpBind": tmnxCpmProtExcdSdpBind,
       "tmnxCpmProtExcdSapEcm": tmnxCpmProtExcdSapEcm,
       "tmnxCpmProtExcdSdpBindEcm": tmnxCpmProtExcdSdpBindEcm,
       "tmnxPkiFileReadFailed": tmnxPkiFileReadFailed,
       "tmnxPkiCertVerificationFailed": tmnxPkiCertVerificationFailed,
       "tmnxCAProfileStateChange": tmnxCAProfileStateChange,
       "tmnxCpmProtExcdSapIp": tmnxCpmProtExcdSapIp,
       "tmnxPkiCAProfActnStatusChg": tmnxPkiCAProfActnStatusChg,
       "tmnxCpmProtViolSapOutProf": tmnxCpmProtViolSapOutProf,
       "tmnxCpmProtViolIfOutProf": tmnxCpmProtViolIfOutProf,
       "tmnxCpmProtExcdSdpBindIp": tmnxCpmProtExcdSdpBindIp,
       "tmnxSecComputeCertChainFailure": tmnxSecComputeCertChainFailure,
       "tmnxCpmProtViolSdpBindOutProf": tmnxCpmProtViolSdpBindOutProf,
       "tmnxSecNotifKeyChainExpired": tmnxSecNotifKeyChainExpired,
       "tmnxCAProfUpDueToRevokeChkCrlOpt": tmnxCAProfUpDueToRevokeChkCrlOpt}
)
