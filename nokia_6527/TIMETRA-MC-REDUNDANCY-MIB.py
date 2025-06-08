# SNMP MIB module (TIMETRA-MC-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MC-REDUNDANCY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:47 2025
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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
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

(LAGInterfaceNumber,) = mibBuilder.importSymbols(
    "TIMETRA-LAG-MIB",
    "LAGInterfaceNumber")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(svcId,
 svcTlsInfoEntry) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId",
    "svcTlsInfoEntry")

(TmnxMobGwId,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MG-MIB",
    "TmnxMobGwId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxSrrpPriorityStep,
 TmnxTunnelGroupId,
 TmnxTunnelGroupIdOrZero,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxSrrpPriorityStep",
    "TmnxTunnelGroupId",
    "TmnxTunnelGroupIdOrZero",
    "TmnxVRtrID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraMcRedundancyMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 40)
)
if mibBuilder.loadTexts:
    timetraMcRedundancyMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2006-07-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMcsClientApp(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("igmp", 0),
          ("igmpSnooping", 1),
          ("subMgmtIpoe", 2),
          ("srrp", 3),
          ("mcRing", 4),
          ("mldSnooping", 5),
          ("dhcpServer", 6),
          ("subHostTrk", 7),
          ("subMgmtPppoe", 8),
          ("mcIpsec", 9),
          ("mld", 10),
          ("python", 11))
    )



class TmnxMcsAccessProtection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("srrp", 1)
    )



class TmnxMcRingOperState(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("shutdown", 2),
          ("configErr", 3),
          ("noPeer", 4),
          ("connected", 5),
          ("broken", 6),
          ("localBroken", 7),
          ("conflict", 8),
          ("testingRing", 9),
          ("halfBroken", 10),
          ("waitingForPeer", 11))
    )



class TmnxMcRingInbCtrlOperState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("connected", 2),
          ("broken", 3),
          ("testing", 4),
          ("peerDetectsDown", 5),
          ("notConfigured", 6))
    )



class TmnxMcRingNodeOperState(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notProvisioned", 2),
          ("configErr", 3),
          ("notTested", 4),
          ("testing", 5),
          ("connected", 6),
          ("disconnected", 7))
    )



class TmnxSrrpAssoBfdIntfSessOperState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("connected", 2),
          ("broken", 3),
          ("peerDetectsDown", 4),
          ("notConfigured", 5),
          ("noResources", 6))
    )



class TmnxMcRingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )



class TMcPeerIPsecTnlGrpMasterState(TextualConvention, Integer32):
    status = "current"
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
        *(("discovery", 1),
          ("notEligible", 2),
          ("eligible", 3),
          ("standby", 4),
          ("master", 5))
    )



class TMcPeerIPsecTnlGrpProtectionStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nominal", 1),
          ("notReady", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMcRedundancyConformance_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyConformance = _TmnxMcRedundancyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40)
)
_TmnxMcRedundancyCompliances_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyCompliances = _TmnxMcRedundancyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1)
)
_TmnxMcRedundancyGroups_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyGroups = _TmnxMcRedundancyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2)
)
_TmnxMcRedundancyNotifGroups_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyNotifGroups = _TmnxMcRedundancyNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3)
)
_TmnxMcMobRedundancyCompliances_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyCompliances = _TmnxMcMobRedundancyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 4)
)
_TmnxMcMobRedundancyGroups_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyGroups = _TmnxMcMobRedundancyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 5)
)
_TmnxMcMobRedundancyNotifyGroups_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyNotifyGroups = _TmnxMcMobRedundancyNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 6)
)
_TmnxMcRedundancy_ObjectIdentity = ObjectIdentity
tmnxMcRedundancy = _TmnxMcRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40)
)
_TmnxMcRedundancyObjs_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyObjs = _TmnxMcRedundancyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1)
)
_TmnxMcPeerTable_Object = MibTable
tmnxMcPeerTable = _TmnxMcPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMcPeerTable.setStatus("current")
_TmnxMcPeerEntry_Object = MibTableRow
tmnxMcPeerEntry = _TmnxMcPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1)
)
tmnxMcPeerEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerEntry.setStatus("current")
_TmnxMcPeerIpType_Type = InetAddressType
_TmnxMcPeerIpType_Object = MibTableColumn
tmnxMcPeerIpType = _TmnxMcPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 1),
    _TmnxMcPeerIpType_Type()
)
tmnxMcPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerIpType.setStatus("current")


class _TmnxMcPeerIpAddr_Type(InetAddress):
    """Custom type tmnxMcPeerIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcPeerIpAddr_Type.__name__ = "InetAddress"
_TmnxMcPeerIpAddr_Object = MibTableColumn
tmnxMcPeerIpAddr = _TmnxMcPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 2),
    _TmnxMcPeerIpAddr_Type()
)
tmnxMcPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerIpAddr.setStatus("current")
_TmnxMcPeerRowStatus_Type = RowStatus
_TmnxMcPeerRowStatus_Object = MibTableColumn
tmnxMcPeerRowStatus = _TmnxMcPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 3),
    _TmnxMcPeerRowStatus_Type()
)
tmnxMcPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerRowStatus.setStatus("current")


class _TmnxMcPeerDescription_Type(TItemDescription):
    """Custom type tmnxMcPeerDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxMcPeerDescription_Type.__name__ = "TItemDescription"
_TmnxMcPeerDescription_Object = MibTableColumn
tmnxMcPeerDescription = _TmnxMcPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 4),
    _TmnxMcPeerDescription_Type()
)
tmnxMcPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerDescription.setStatus("current")


class _TmnxMcPeerAuthKey_Type(OctetString):
    """Custom type tmnxMcPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMcPeerAuthKey_Type.__name__ = "OctetString"
_TmnxMcPeerAuthKey_Object = MibTableColumn
tmnxMcPeerAuthKey = _TmnxMcPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 5),
    _TmnxMcPeerAuthKey_Type()
)
tmnxMcPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerAuthKey.setStatus("current")


class _TmnxMcPeerSrcIpType_Type(InetAddressType):
    """Custom type tmnxMcPeerSrcIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcPeerSrcIpType_Type.__name__ = "InetAddressType"
_TmnxMcPeerSrcIpType_Object = MibTableColumn
tmnxMcPeerSrcIpType = _TmnxMcPeerSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 6),
    _TmnxMcPeerSrcIpType_Type()
)
tmnxMcPeerSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSrcIpType.setStatus("current")


class _TmnxMcPeerSrcIpAddr_Type(InetAddress):
    """Custom type tmnxMcPeerSrcIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMcPeerSrcIpAddr_Type.__name__ = "InetAddress"
_TmnxMcPeerSrcIpAddr_Object = MibTableColumn
tmnxMcPeerSrcIpAddr = _TmnxMcPeerSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 7),
    _TmnxMcPeerSrcIpAddr_Type()
)
tmnxMcPeerSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSrcIpAddr.setStatus("current")


class _TmnxMcPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcPeerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcPeerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcPeerAdminState_Object = MibTableColumn
tmnxMcPeerAdminState = _TmnxMcPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 8),
    _TmnxMcPeerAdminState_Type()
)
tmnxMcPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerAdminState.setStatus("current")
_TmnxMcPeerSrcIpOperType_Type = InetAddressType
_TmnxMcPeerSrcIpOperType_Object = MibTableColumn
tmnxMcPeerSrcIpOperType = _TmnxMcPeerSrcIpOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 9),
    _TmnxMcPeerSrcIpOperType_Type()
)
tmnxMcPeerSrcIpOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSrcIpOperType.setStatus("current")


class _TmnxMcPeerSrcIpOperAddr_Type(InetAddress):
    """Custom type tmnxMcPeerSrcIpOperAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMcPeerSrcIpOperAddr_Type.__name__ = "InetAddress"
_TmnxMcPeerSrcIpOperAddr_Object = MibTableColumn
tmnxMcPeerSrcIpOperAddr = _TmnxMcPeerSrcIpOperAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 10),
    _TmnxMcPeerSrcIpOperAddr_Type()
)
tmnxMcPeerSrcIpOperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSrcIpOperAddr.setStatus("current")
_TmnxMcPeerRingsOperState_Type = TmnxOperState
_TmnxMcPeerRingsOperState_Object = MibTableColumn
tmnxMcPeerRingsOperState = _TmnxMcPeerRingsOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 11),
    _TmnxMcPeerRingsOperState_Type()
)
tmnxMcPeerRingsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerRingsOperState.setStatus("current")


class _TmnxMcPeerName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPeerName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxMcPeerName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPeerName_Object = MibTableColumn
tmnxMcPeerName = _TmnxMcPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 12),
    _TmnxMcPeerName_Type()
)
tmnxMcPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerName.setStatus("current")


class _TmnxMcPeerWarmStandby_Type(TruthValue):
    """Custom type tmnxMcPeerWarmStandby based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerWarmStandby_Type.__name__ = "TruthValue"
_TmnxMcPeerWarmStandby_Object = MibTableColumn
tmnxMcPeerWarmStandby = _TmnxMcPeerWarmStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 15),
    _TmnxMcPeerWarmStandby_Type()
)
tmnxMcPeerWarmStandby.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerWarmStandby.setStatus("current")
_TmnxMcPeerRemoteWarmStandby_Type = TruthValue
_TmnxMcPeerRemoteWarmStandby_Object = MibTableColumn
tmnxMcPeerRemoteWarmStandby = _TmnxMcPeerRemoteWarmStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 1, 1, 16),
    _TmnxMcPeerRemoteWarmStandby_Type()
)
tmnxMcPeerRemoteWarmStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerRemoteWarmStandby.setStatus("current")
_TmnxMcPeerSyncTable_Object = MibTable
tmnxMcPeerSyncTable = _TmnxMcPeerSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncTable.setStatus("current")
_TmnxMcPeerSyncEntry_Object = MibTableRow
tmnxMcPeerSyncEntry = _TmnxMcPeerSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1)
)
tmnxMcPeerSyncEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncEntry.setStatus("current")
_TmnxMcPeerSyncRowStatus_Type = RowStatus
_TmnxMcPeerSyncRowStatus_Object = MibTableColumn
tmnxMcPeerSyncRowStatus = _TmnxMcPeerSyncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 1),
    _TmnxMcPeerSyncRowStatus_Type()
)
tmnxMcPeerSyncRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncRowStatus.setStatus("current")


class _TmnxMcPeerSyncIgmp_Type(TruthValue):
    """Custom type tmnxMcPeerSyncIgmp based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncIgmp_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncIgmp_Object = MibTableColumn
tmnxMcPeerSyncIgmp = _TmnxMcPeerSyncIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 2),
    _TmnxMcPeerSyncIgmp_Type()
)
tmnxMcPeerSyncIgmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncIgmp.setStatus("current")


class _TmnxMcPeerSyncIgmpSnooping_Type(TruthValue):
    """Custom type tmnxMcPeerSyncIgmpSnooping based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncIgmpSnooping_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncIgmpSnooping_Object = MibTableColumn
tmnxMcPeerSyncIgmpSnooping = _TmnxMcPeerSyncIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 3),
    _TmnxMcPeerSyncIgmpSnooping_Type()
)
tmnxMcPeerSyncIgmpSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncIgmpSnooping.setStatus("current")


class _TmnxMcPeerSyncSubMgmt_Type(TruthValue):
    """Custom type tmnxMcPeerSyncSubMgmt based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncSubMgmt_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncSubMgmt_Object = MibTableColumn
tmnxMcPeerSyncSubMgmt = _TmnxMcPeerSyncSubMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 4),
    _TmnxMcPeerSyncSubMgmt_Type()
)
tmnxMcPeerSyncSubMgmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncSubMgmt.setStatus("current")


class _TmnxMcPeerSyncSrrp_Type(TruthValue):
    """Custom type tmnxMcPeerSyncSrrp based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncSrrp_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncSrrp_Object = MibTableColumn
tmnxMcPeerSyncSrrp = _TmnxMcPeerSyncSrrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 5),
    _TmnxMcPeerSyncSrrp_Type()
)
tmnxMcPeerSyncSrrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncSrrp.setStatus("current")


class _TmnxMcPeerSyncAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcPeerSyncAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcPeerSyncAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcPeerSyncAdminState_Object = MibTableColumn
tmnxMcPeerSyncAdminState = _TmnxMcPeerSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 6),
    _TmnxMcPeerSyncAdminState_Type()
)
tmnxMcPeerSyncAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncAdminState.setStatus("current")
_TmnxMcPeerSyncOperState_Type = TmnxOperState
_TmnxMcPeerSyncOperState_Object = MibTableColumn
tmnxMcPeerSyncOperState = _TmnxMcPeerSyncOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 7),
    _TmnxMcPeerSyncOperState_Type()
)
tmnxMcPeerSyncOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncOperState.setStatus("current")


class _TmnxMcPeerSyncOperFlags_Type(Bits):
    """Custom type tmnxMcPeerSyncOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("syncAdminDown", 0),
          ("peerAdminDown", 1),
          ("connectionDown", 2),
          ("internalError", 3),
          ("mcsVersionMismatch", 4),
          ("platformMismatch", 5),
          ("appVersionMismatch", 6),
          ("appSupportMismatch", 7),
          ("omcrVersionMismatch", 8),
          ("omcrStandbyStandby", 9),
          ("omcrNumEntriesHigh", 10))
    )

_TmnxMcPeerSyncOperFlags_Type.__name__ = "Bits"
_TmnxMcPeerSyncOperFlags_Object = MibTableColumn
tmnxMcPeerSyncOperFlags = _TmnxMcPeerSyncOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 8),
    _TmnxMcPeerSyncOperFlags_Type()
)
tmnxMcPeerSyncOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncOperFlags.setStatus("current")


class _TmnxMcPeerSyncStatus_Type(Integer32):
    """Custom type tmnxMcPeerSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("syncInProgress", 2),
          ("outOfSync", 3))
    )


_TmnxMcPeerSyncStatus_Type.__name__ = "Integer32"
_TmnxMcPeerSyncStatus_Object = MibTableColumn
tmnxMcPeerSyncStatus = _TmnxMcPeerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 9),
    _TmnxMcPeerSyncStatus_Type()
)
tmnxMcPeerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncStatus.setStatus("current")
_TmnxMcPeerSyncLastSyncTime_Type = TimeStamp
_TmnxMcPeerSyncLastSyncTime_Object = MibTableColumn
tmnxMcPeerSyncLastSyncTime = _TmnxMcPeerSyncLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 10),
    _TmnxMcPeerSyncLastSyncTime_Type()
)
tmnxMcPeerSyncLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncLastSyncTime.setStatus("current")
_TmnxMcPeerSyncNumEntries_Type = Counter32
_TmnxMcPeerSyncNumEntries_Object = MibTableColumn
tmnxMcPeerSyncNumEntries = _TmnxMcPeerSyncNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 11),
    _TmnxMcPeerSyncNumEntries_Type()
)
tmnxMcPeerSyncNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncNumEntries.setStatus("current")
_TmnxMcPeerSyncLclDeletedEntries_Type = Counter32
_TmnxMcPeerSyncLclDeletedEntries_Object = MibTableColumn
tmnxMcPeerSyncLclDeletedEntries = _TmnxMcPeerSyncLclDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 12),
    _TmnxMcPeerSyncLclDeletedEntries_Type()
)
tmnxMcPeerSyncLclDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncLclDeletedEntries.setStatus("current")
_TmnxMcPeerSyncAlarmedEntries_Type = Counter32
_TmnxMcPeerSyncAlarmedEntries_Object = MibTableColumn
tmnxMcPeerSyncAlarmedEntries = _TmnxMcPeerSyncAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 13),
    _TmnxMcPeerSyncAlarmedEntries_Type()
)
tmnxMcPeerSyncAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncAlarmedEntries.setStatus("current")
_TmnxMcPeerSyncRemNumEntries_Type = Counter32
_TmnxMcPeerSyncRemNumEntries_Object = MibTableColumn
tmnxMcPeerSyncRemNumEntries = _TmnxMcPeerSyncRemNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 14),
    _TmnxMcPeerSyncRemNumEntries_Type()
)
tmnxMcPeerSyncRemNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncRemNumEntries.setStatus("current")
_TmnxMcPeerSyncRemLclDelEntries_Type = Counter32
_TmnxMcPeerSyncRemLclDelEntries_Object = MibTableColumn
tmnxMcPeerSyncRemLclDelEntries = _TmnxMcPeerSyncRemLclDelEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 15),
    _TmnxMcPeerSyncRemLclDelEntries_Type()
)
tmnxMcPeerSyncRemLclDelEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncRemLclDelEntries.setStatus("current")
_TmnxMcPeerSyncRemAlarmedEntries_Type = Counter32
_TmnxMcPeerSyncRemAlarmedEntries_Object = MibTableColumn
tmnxMcPeerSyncRemAlarmedEntries = _TmnxMcPeerSyncRemAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 16),
    _TmnxMcPeerSyncRemAlarmedEntries_Type()
)
tmnxMcPeerSyncRemAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncRemAlarmedEntries.setStatus("current")


class _TmnxMcPeerSyncMcRing_Type(TruthValue):
    """Custom type tmnxMcPeerSyncMcRing based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncMcRing_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncMcRing_Object = MibTableColumn
tmnxMcPeerSyncMcRing = _TmnxMcPeerSyncMcRing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 17),
    _TmnxMcPeerSyncMcRing_Type()
)
tmnxMcPeerSyncMcRing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncMcRing.setStatus("current")


class _TmnxMcPeerSyncMldSnooping_Type(TruthValue):
    """Custom type tmnxMcPeerSyncMldSnooping based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncMldSnooping_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncMldSnooping_Object = MibTableColumn
tmnxMcPeerSyncMldSnooping = _TmnxMcPeerSyncMldSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 18),
    _TmnxMcPeerSyncMldSnooping_Type()
)
tmnxMcPeerSyncMldSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncMldSnooping.setStatus("current")


class _TmnxMcPeerSyncDhcpServer_Type(TruthValue):
    """Custom type tmnxMcPeerSyncDhcpServer based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncDhcpServer_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncDhcpServer_Object = MibTableColumn
tmnxMcPeerSyncDhcpServer = _TmnxMcPeerSyncDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 19),
    _TmnxMcPeerSyncDhcpServer_Type()
)
tmnxMcPeerSyncDhcpServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncDhcpServer.setStatus("current")


class _TmnxMcPeerSyncSubHostTrk_Type(TruthValue):
    """Custom type tmnxMcPeerSyncSubHostTrk based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncSubHostTrk_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncSubHostTrk_Object = MibTableColumn
tmnxMcPeerSyncSubHostTrk = _TmnxMcPeerSyncSubHostTrk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 20),
    _TmnxMcPeerSyncSubHostTrk_Type()
)
tmnxMcPeerSyncSubHostTrk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncSubHostTrk.setStatus("current")


class _TmnxMcPeerSyncSubMgmtPppoe_Type(TruthValue):
    """Custom type tmnxMcPeerSyncSubMgmtPppoe based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncSubMgmtPppoe_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncSubMgmtPppoe_Object = MibTableColumn
tmnxMcPeerSyncSubMgmtPppoe = _TmnxMcPeerSyncSubMgmtPppoe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 21),
    _TmnxMcPeerSyncSubMgmtPppoe_Type()
)
tmnxMcPeerSyncSubMgmtPppoe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncSubMgmtPppoe.setStatus("current")


class _TmnxMcPeerSyncIpsec_Type(TruthValue):
    """Custom type tmnxMcPeerSyncIpsec based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncIpsec_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncIpsec_Object = MibTableColumn
tmnxMcPeerSyncIpsec = _TmnxMcPeerSyncIpsec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 22),
    _TmnxMcPeerSyncIpsec_Type()
)
tmnxMcPeerSyncIpsec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncIpsec.setStatus("current")


class _TmnxMcPeerSyncMobile_Type(TruthValue):
    """Custom type tmnxMcPeerSyncMobile based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncMobile_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncMobile_Object = MibTableColumn
tmnxMcPeerSyncMobile = _TmnxMcPeerSyncMobile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 25),
    _TmnxMcPeerSyncMobile_Type()
)
tmnxMcPeerSyncMobile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncMobile.setStatus("current")
_TmnxMcPeerSyncOmcrStandby_Type = Counter32
_TmnxMcPeerSyncOmcrStandby_Object = MibTableColumn
tmnxMcPeerSyncOmcrStandby = _TmnxMcPeerSyncOmcrStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 26),
    _TmnxMcPeerSyncOmcrStandby_Type()
)
tmnxMcPeerSyncOmcrStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncOmcrStandby.setStatus("current")
_TmnxMcPeerSyncOmcrAlarmed_Type = Counter32
_TmnxMcPeerSyncOmcrAlarmed_Object = MibTableColumn
tmnxMcPeerSyncOmcrAlarmed = _TmnxMcPeerSyncOmcrAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 27),
    _TmnxMcPeerSyncOmcrAlarmed_Type()
)
tmnxMcPeerSyncOmcrAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncOmcrAlarmed.setStatus("current")
_TmnxMcPeerSyncOmcrRemStandby_Type = Counter32
_TmnxMcPeerSyncOmcrRemStandby_Object = MibTableColumn
tmnxMcPeerSyncOmcrRemStandby = _TmnxMcPeerSyncOmcrRemStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 28),
    _TmnxMcPeerSyncOmcrRemStandby_Type()
)
tmnxMcPeerSyncOmcrRemStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncOmcrRemStandby.setStatus("current")
_TmnxMcPeerSyncOmcrRemAlarmed_Type = Counter32
_TmnxMcPeerSyncOmcrRemAlarmed_Object = MibTableColumn
tmnxMcPeerSyncOmcrRemAlarmed = _TmnxMcPeerSyncOmcrRemAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 29),
    _TmnxMcPeerSyncOmcrRemAlarmed_Type()
)
tmnxMcPeerSyncOmcrRemAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncOmcrRemAlarmed.setStatus("current")


class _TmnxMcPeerSyncMld_Type(TruthValue):
    """Custom type tmnxMcPeerSyncMld based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncMld_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncMld_Object = MibTableColumn
tmnxMcPeerSyncMld = _TmnxMcPeerSyncMld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 30),
    _TmnxMcPeerSyncMld_Type()
)
tmnxMcPeerSyncMld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncMld.setStatus("current")


class _TmnxMcPeerSyncPythonCache_Type(TruthValue):
    """Custom type tmnxMcPeerSyncPythonCache based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerSyncPythonCache_Type.__name__ = "TruthValue"
_TmnxMcPeerSyncPythonCache_Object = MibTableColumn
tmnxMcPeerSyncPythonCache = _TmnxMcPeerSyncPythonCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 2, 1, 31),
    _TmnxMcPeerSyncPythonCache_Type()
)
tmnxMcPeerSyncPythonCache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPythonCache.setStatus("current")
_TmnxMcPeerSyncPortTable_Object = MibTable
tmnxMcPeerSyncPortTable = _TmnxMcPeerSyncPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortTable.setStatus("current")
_TmnxMcPeerSyncPortEntry_Object = MibTableRow
tmnxMcPeerSyncPortEntry = _TmnxMcPeerSyncPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 3, 1)
)
tmnxMcPeerSyncPortEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortId"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEntry.setStatus("current")
_TmnxMcPeerSyncPortId_Type = TmnxPortID
_TmnxMcPeerSyncPortId_Object = MibTableColumn
tmnxMcPeerSyncPortId = _TmnxMcPeerSyncPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 3, 1, 1),
    _TmnxMcPeerSyncPortId_Type()
)
tmnxMcPeerSyncPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortId.setStatus("current")
_TmnxMcPeerSyncPortRowStatus_Type = RowStatus
_TmnxMcPeerSyncPortRowStatus_Object = MibTableColumn
tmnxMcPeerSyncPortRowStatus = _TmnxMcPeerSyncPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 3, 1, 2),
    _TmnxMcPeerSyncPortRowStatus_Type()
)
tmnxMcPeerSyncPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortRowStatus.setStatus("current")


class _TmnxMcPeerSyncPortSyncTag_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcPeerSyncPortSyncTag based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcPeerSyncPortSyncTag_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcPeerSyncPortSyncTag_Object = MibTableColumn
tmnxMcPeerSyncPortSyncTag = _TmnxMcPeerSyncPortSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 3, 1, 3),
    _TmnxMcPeerSyncPortSyncTag_Type()
)
tmnxMcPeerSyncPortSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortSyncTag.setStatus("current")
_TmnxMcPeerSyncPortEncapRangeTable_Object = MibTable
tmnxMcPeerSyncPortEncapRangeTable = _TmnxMcPeerSyncPortEncapRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapRangeTable.setStatus("current")
_TmnxMcPeerSyncPortEncapRangeEntry_Object = MibTableRow
tmnxMcPeerSyncPortEncapRangeEntry = _TmnxMcPeerSyncPortEncapRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4, 1)
)
tmnxMcPeerSyncPortEncapRangeEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortId"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapMin"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapMax"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapRangeEntry.setStatus("current")


class _TmnxMcPeerSyncPortEncapType_Type(Integer32):
    """Custom type tmnxMcPeerSyncPortEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1q", 1),
          ("qinq", 2))
    )


_TmnxMcPeerSyncPortEncapType_Type.__name__ = "Integer32"
_TmnxMcPeerSyncPortEncapType_Object = MibTableColumn
tmnxMcPeerSyncPortEncapType = _TmnxMcPeerSyncPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4, 1, 1),
    _TmnxMcPeerSyncPortEncapType_Type()
)
tmnxMcPeerSyncPortEncapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapType.setStatus("current")
_TmnxMcPeerSyncPortEncapMin_Type = TmnxEncapVal
_TmnxMcPeerSyncPortEncapMin_Object = MibTableColumn
tmnxMcPeerSyncPortEncapMin = _TmnxMcPeerSyncPortEncapMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4, 1, 2),
    _TmnxMcPeerSyncPortEncapMin_Type()
)
tmnxMcPeerSyncPortEncapMin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapMin.setStatus("current")
_TmnxMcPeerSyncPortEncapMax_Type = TmnxEncapVal
_TmnxMcPeerSyncPortEncapMax_Object = MibTableColumn
tmnxMcPeerSyncPortEncapMax = _TmnxMcPeerSyncPortEncapMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4, 1, 3),
    _TmnxMcPeerSyncPortEncapMax_Type()
)
tmnxMcPeerSyncPortEncapMax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapMax.setStatus("current")
_TmnxMcPeerSyncPortEncapRowStatus_Type = RowStatus
_TmnxMcPeerSyncPortEncapRowStatus_Object = MibTableColumn
tmnxMcPeerSyncPortEncapRowStatus = _TmnxMcPeerSyncPortEncapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4, 1, 4),
    _TmnxMcPeerSyncPortEncapRowStatus_Type()
)
tmnxMcPeerSyncPortEncapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapRowStatus.setStatus("current")
_TmnxMcPeerSyncPortEncapSyncTag_Type = TNamedItem
_TmnxMcPeerSyncPortEncapSyncTag_Object = MibTableColumn
tmnxMcPeerSyncPortEncapSyncTag = _TmnxMcPeerSyncPortEncapSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 4, 1, 5),
    _TmnxMcPeerSyncPortEncapSyncTag_Type()
)
tmnxMcPeerSyncPortEncapSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPortEncapSyncTag.setStatus("current")
_TmnxMcLagConfigTableLastChanged_Type = TimeStamp
_TmnxMcLagConfigTableLastChanged_Object = MibScalar
tmnxMcLagConfigTableLastChanged = _TmnxMcLagConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 5),
    _TmnxMcLagConfigTableLastChanged_Type()
)
tmnxMcLagConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigTableLastChanged.setStatus("current")
_TmnxMcLagConfigTable_Object = MibTable
tmnxMcLagConfigTable = _TmnxMcLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxMcLagConfigTable.setStatus("current")
_TmnxMcLagConfigEntry_Object = MibTableRow
tmnxMcLagConfigEntry = _TmnxMcLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1)
)
tmnxMcLagConfigEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcLagConfigEntry.setStatus("current")
_TmnxMcLagConfigPeerLastChanged_Type = TimeStamp
_TmnxMcLagConfigPeerLastChanged_Object = MibTableColumn
tmnxMcLagConfigPeerLastChanged = _TmnxMcLagConfigPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1, 1),
    _TmnxMcLagConfigPeerLastChanged_Type()
)
tmnxMcLagConfigPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigPeerLastChanged.setStatus("current")


class _TmnxMcLagConfigPeerAdminstate_Type(TmnxAdminState):
    """Custom type tmnxMcLagConfigPeerAdminstate based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcLagConfigPeerAdminstate_Type.__name__ = "TmnxAdminState"
_TmnxMcLagConfigPeerAdminstate_Object = MibTableColumn
tmnxMcLagConfigPeerAdminstate = _TmnxMcLagConfigPeerAdminstate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1, 2),
    _TmnxMcLagConfigPeerAdminstate_Type()
)
tmnxMcLagConfigPeerAdminstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcLagConfigPeerAdminstate.setStatus("current")


class _TmnxMcLagConfigKeepALiveIvl_Type(Unsigned32):
    """Custom type tmnxMcLagConfigKeepALiveIvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_TmnxMcLagConfigKeepALiveIvl_Type.__name__ = "Unsigned32"
_TmnxMcLagConfigKeepALiveIvl_Object = MibTableColumn
tmnxMcLagConfigKeepALiveIvl = _TmnxMcLagConfigKeepALiveIvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1, 3),
    _TmnxMcLagConfigKeepALiveIvl_Type()
)
tmnxMcLagConfigKeepALiveIvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcLagConfigKeepALiveIvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcLagConfigKeepALiveIvl.setUnits("deci-seconds")


class _TmnxMcLagConfigHoldOnNgbrFailure_Type(Unsigned32):
    """Custom type tmnxMcLagConfigHoldOnNgbrFailure based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 25),
    )


_TmnxMcLagConfigHoldOnNgbrFailure_Type.__name__ = "Unsigned32"
_TmnxMcLagConfigHoldOnNgbrFailure_Object = MibTableColumn
tmnxMcLagConfigHoldOnNgbrFailure = _TmnxMcLagConfigHoldOnNgbrFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1, 4),
    _TmnxMcLagConfigHoldOnNgbrFailure_Type()
)
tmnxMcLagConfigHoldOnNgbrFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcLagConfigHoldOnNgbrFailure.setStatus("current")


class _TmnxMcLagConfigOperState_Type(Integer32):
    """Custom type tmnxMcLagConfigOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inService", 0),
          ("outOfService", 1))
    )


_TmnxMcLagConfigOperState_Type.__name__ = "Integer32"
_TmnxMcLagConfigOperState_Object = MibTableColumn
tmnxMcLagConfigOperState = _TmnxMcLagConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1, 5),
    _TmnxMcLagConfigOperState_Type()
)
tmnxMcLagConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigOperState.setStatus("current")
_TmnxMcLagConfigPeerLastStateChge_Type = TimeStamp
_TmnxMcLagConfigPeerLastStateChge_Object = MibTableColumn
tmnxMcLagConfigPeerLastStateChge = _TmnxMcLagConfigPeerLastStateChge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 6, 1, 6),
    _TmnxMcLagConfigPeerLastStateChge_Type()
)
tmnxMcLagConfigPeerLastStateChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigPeerLastStateChge.setStatus("current")
_TmnxMcLagConfigLagTableLastChanged_Type = TimeStamp
_TmnxMcLagConfigLagTableLastChanged_Object = MibScalar
tmnxMcLagConfigLagTableLastChanged = _TmnxMcLagConfigLagTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 7),
    _TmnxMcLagConfigLagTableLastChanged_Type()
)
tmnxMcLagConfigLagTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagTableLastChanged.setStatus("current")
_TmnxMcLagConfigLagTable_Object = MibTable
tmnxMcLagConfigLagTable = _TmnxMcLagConfigLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagTable.setStatus("current")
_TmnxMcLagConfigLagEntry_Object = MibTableRow
tmnxMcLagConfigLagEntry = _TmnxMcLagConfigLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1)
)
tmnxMcLagConfigLagEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagId"),
)
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagEntry.setStatus("current")
_TmnxMcLagConfigLagId_Type = LAGInterfaceNumber
_TmnxMcLagConfigLagId_Object = MibTableColumn
tmnxMcLagConfigLagId = _TmnxMcLagConfigLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 1),
    _TmnxMcLagConfigLagId_Type()
)
tmnxMcLagConfigLagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagId.setStatus("current")
_TmnxMcLagConfigLagLastChanged_Type = TimeStamp
_TmnxMcLagConfigLagLastChanged_Object = MibTableColumn
tmnxMcLagConfigLagLastChanged = _TmnxMcLagConfigLagLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 2),
    _TmnxMcLagConfigLagLastChanged_Type()
)
tmnxMcLagConfigLagLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagLastChanged.setStatus("current")
_TmnxMcLagConfigLagRowStatus_Type = RowStatus
_TmnxMcLagConfigLagRowStatus_Object = MibTableColumn
tmnxMcLagConfigLagRowStatus = _TmnxMcLagConfigLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 3),
    _TmnxMcLagConfigLagRowStatus_Type()
)
tmnxMcLagConfigLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagRowStatus.setStatus("current")


class _TmnxMcLagConfigLaglacpKey_Type(Unsigned32):
    """Custom type tmnxMcLagConfigLaglacpKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxMcLagConfigLaglacpKey_Type.__name__ = "Unsigned32"
_TmnxMcLagConfigLaglacpKey_Object = MibTableColumn
tmnxMcLagConfigLaglacpKey = _TmnxMcLagConfigLaglacpKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 4),
    _TmnxMcLagConfigLaglacpKey_Type()
)
tmnxMcLagConfigLaglacpKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLaglacpKey.setStatus("current")


class _TmnxMcLagConfigLagSystemId_Type(OctetString):
    """Custom type tmnxMcLagConfigLagSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TmnxMcLagConfigLagSystemId_Type.__name__ = "OctetString"
_TmnxMcLagConfigLagSystemId_Object = MibTableColumn
tmnxMcLagConfigLagSystemId = _TmnxMcLagConfigLagSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 5),
    _TmnxMcLagConfigLagSystemId_Type()
)
tmnxMcLagConfigLagSystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagSystemId.setStatus("current")


class _TmnxMcLagConfigLagSystemPriority_Type(Unsigned32):
    """Custom type tmnxMcLagConfigLagSystemPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxMcLagConfigLagSystemPriority_Type.__name__ = "Unsigned32"
_TmnxMcLagConfigLagSystemPriority_Object = MibTableColumn
tmnxMcLagConfigLagSystemPriority = _TmnxMcLagConfigLagSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 6),
    _TmnxMcLagConfigLagSystemPriority_Type()
)
tmnxMcLagConfigLagSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagSystemPriority.setStatus("current")
_TmnxMcLagConfigLagRemoteLagId_Type = LAGInterfaceNumber
_TmnxMcLagConfigLagRemoteLagId_Object = MibTableColumn
tmnxMcLagConfigLagRemoteLagId = _TmnxMcLagConfigLagRemoteLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 7),
    _TmnxMcLagConfigLagRemoteLagId_Type()
)
tmnxMcLagConfigLagRemoteLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagRemoteLagId.setStatus("current")


class _TmnxMcLagConfigLagSrcBMacLSB_Type(Unsigned32):
    """Custom type tmnxMcLagConfigLagSrcBMacLSB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxMcLagConfigLagSrcBMacLSB_Type.__name__ = "Unsigned32"
_TmnxMcLagConfigLagSrcBMacLSB_Object = MibTableColumn
tmnxMcLagConfigLagSrcBMacLSB = _TmnxMcLagConfigLagSrcBMacLSB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 8),
    _TmnxMcLagConfigLagSrcBMacLSB_Type()
)
tmnxMcLagConfigLagSrcBMacLSB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagSrcBMacLSB.setStatus("current")
_TmnxMcLagConfigLagOperSrcBMacLSB_Type = Unsigned32
_TmnxMcLagConfigLagOperSrcBMacLSB_Object = MibTableColumn
tmnxMcLagConfigLagOperSrcBMacLSB = _TmnxMcLagConfigLagOperSrcBMacLSB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 8, 1, 9),
    _TmnxMcLagConfigLagOperSrcBMacLSB_Type()
)
tmnxMcLagConfigLagOperSrcBMacLSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagOperSrcBMacLSB.setStatus("current")
_TmnxSrrpOperTable_Object = MibTable
tmnxSrrpOperTable = _TmnxSrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxSrrpOperTable.setStatus("current")
_TmnxSrrpOperEntry_Object = MibTableRow
tmnxSrrpOperEntry = _TmnxSrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1)
)
tmnxSrrpOperEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperID"),
)
if mibBuilder.loadTexts:
    tmnxSrrpOperEntry.setStatus("current")
_TmnxSrrpOperID_Type = Unsigned32
_TmnxSrrpOperID_Object = MibTableColumn
tmnxSrrpOperID = _TmnxSrrpOperID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 1),
    _TmnxSrrpOperID_Type()
)
tmnxSrrpOperID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSrrpOperID.setStatus("current")
_TmnxSrrpOperRowStatus_Type = RowStatus
_TmnxSrrpOperRowStatus_Object = MibTableColumn
tmnxSrrpOperRowStatus = _TmnxSrrpOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 2),
    _TmnxSrrpOperRowStatus_Type()
)
tmnxSrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperRowStatus.setStatus("current")


class _TmnxSrrpOperDescription_Type(TItemDescription):
    """Custom type tmnxSrrpOperDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxSrrpOperDescription_Type.__name__ = "TItemDescription"
_TmnxSrrpOperDescription_Object = MibTableColumn
tmnxSrrpOperDescription = _TmnxSrrpOperDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 3),
    _TmnxSrrpOperDescription_Type()
)
tmnxSrrpOperDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperDescription.setStatus("current")


class _TmnxSrrpOperGwMac_Type(MacAddress):
    """Custom type tmnxSrrpOperGwMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxSrrpOperGwMac_Type.__name__ = "MacAddress"
_TmnxSrrpOperGwMac_Object = MibTableColumn
tmnxSrrpOperGwMac = _TmnxSrrpOperGwMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 4),
    _TmnxSrrpOperGwMac_Type()
)
tmnxSrrpOperGwMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperGwMac.setStatus("current")
_TmnxSrrpOperGwOperMac_Type = MacAddress
_TmnxSrrpOperGwOperMac_Object = MibTableColumn
tmnxSrrpOperGwOperMac = _TmnxSrrpOperGwOperMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 5),
    _TmnxSrrpOperGwOperMac_Type()
)
tmnxSrrpOperGwOperMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperGwOperMac.setStatus("current")


class _TmnxSrrpOperPriority_Type(Unsigned32):
    """Custom type tmnxSrrpOperPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxSrrpOperPriority_Type.__name__ = "Unsigned32"
_TmnxSrrpOperPriority_Object = MibTableColumn
tmnxSrrpOperPriority = _TmnxSrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 6),
    _TmnxSrrpOperPriority_Type()
)
tmnxSrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperPriority.setStatus("current")
_TmnxSrrpOperInUsePriority_Type = Unsigned32
_TmnxSrrpOperInUsePriority_Object = MibTableColumn
tmnxSrrpOperInUsePriority = _TmnxSrrpOperInUsePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 7),
    _TmnxSrrpOperInUsePriority_Type()
)
tmnxSrrpOperInUsePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperInUsePriority.setStatus("current")
_TmnxSrrpOperMasterPriority_Type = Unsigned32
_TmnxSrrpOperMasterPriority_Object = MibTableColumn
tmnxSrrpOperMasterPriority = _TmnxSrrpOperMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 8),
    _TmnxSrrpOperMasterPriority_Type()
)
tmnxSrrpOperMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperMasterPriority.setStatus("current")


class _TmnxSrrpOperKeepAliveInterval_Type(Unsigned32):
    """Custom type tmnxSrrpOperKeepAliveInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxSrrpOperKeepAliveInterval_Type.__name__ = "Unsigned32"
_TmnxSrrpOperKeepAliveInterval_Object = MibTableColumn
tmnxSrrpOperKeepAliveInterval = _TmnxSrrpOperKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 9),
    _TmnxSrrpOperKeepAliveInterval_Type()
)
tmnxSrrpOperKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSrrpOperKeepAliveInterval.setUnits("hundreds of milli-seconds")


class _TmnxSrrpOperMsgPathSapPortId_Type(TmnxPortID):
    """Custom type tmnxSrrpOperMsgPathSapPortId based on TmnxPortID"""
    defaultValue = 0


_TmnxSrrpOperMsgPathSapPortId_Type.__name__ = "TmnxPortID"
_TmnxSrrpOperMsgPathSapPortId_Object = MibTableColumn
tmnxSrrpOperMsgPathSapPortId = _TmnxSrrpOperMsgPathSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 10),
    _TmnxSrrpOperMsgPathSapPortId_Type()
)
tmnxSrrpOperMsgPathSapPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperMsgPathSapPortId.setStatus("current")


class _TmnxSrrpOperMsgPathSapEncapVal_Type(TmnxEncapVal):
    """Custom type tmnxSrrpOperMsgPathSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TmnxSrrpOperMsgPathSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TmnxSrrpOperMsgPathSapEncapVal_Object = MibTableColumn
tmnxSrrpOperMsgPathSapEncapVal = _TmnxSrrpOperMsgPathSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 11),
    _TmnxSrrpOperMsgPathSapEncapVal_Type()
)
tmnxSrrpOperMsgPathSapEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperMsgPathSapEncapVal.setStatus("current")


class _TmnxSrrpOperAdminState_Type(TmnxAdminState):
    """Custom type tmnxSrrpOperAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxSrrpOperAdminState_Type.__name__ = "TmnxAdminState"
_TmnxSrrpOperAdminState_Object = MibTableColumn
tmnxSrrpOperAdminState = _TmnxSrrpOperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 12),
    _TmnxSrrpOperAdminState_Type()
)
tmnxSrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperAdminState.setStatus("current")


class _TmnxSrrpOperState_Type(Integer32):
    """Custom type tmnxSrrpOperState based on Integer32"""
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
        *(("disabled", 0),
          ("initialize", 1),
          ("backupRouting", 2),
          ("backupShunt", 3),
          ("pendingRouting", 4),
          ("pendingShunt", 5),
          ("pendingMaster", 6),
          ("master", 7))
    )


_TmnxSrrpOperState_Type.__name__ = "Integer32"
_TmnxSrrpOperState_Object = MibTableColumn
tmnxSrrpOperState = _TmnxSrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 13),
    _TmnxSrrpOperState_Type()
)
tmnxSrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperState.setStatus("current")
_TmnxSrrpOperMasterSince_Type = TimeStamp
_TmnxSrrpOperMasterSince_Object = MibTableColumn
tmnxSrrpOperMasterSince = _TmnxSrrpOperMasterSince_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 14),
    _TmnxSrrpOperMasterSince_Type()
)
tmnxSrrpOperMasterSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperMasterSince.setStatus("current")


class _TmnxSrrpOperVrrpPolicy1_Type(Unsigned32):
    """Custom type tmnxSrrpOperVrrpPolicy1 based on Unsigned32"""
    defaultValue = 0


_TmnxSrrpOperVrrpPolicy1_Type.__name__ = "Unsigned32"
_TmnxSrrpOperVrrpPolicy1_Object = MibTableColumn
tmnxSrrpOperVrrpPolicy1 = _TmnxSrrpOperVrrpPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 15),
    _TmnxSrrpOperVrrpPolicy1_Type()
)
tmnxSrrpOperVrrpPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperVrrpPolicy1.setStatus("current")


class _TmnxSrrpOperVrrpPolicy2_Type(Unsigned32):
    """Custom type tmnxSrrpOperVrrpPolicy2 based on Unsigned32"""
    defaultValue = 0


_TmnxSrrpOperVrrpPolicy2_Type.__name__ = "Unsigned32"
_TmnxSrrpOperVrrpPolicy2_Object = MibTableColumn
tmnxSrrpOperVrrpPolicy2 = _TmnxSrrpOperVrrpPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 16),
    _TmnxSrrpOperVrrpPolicy2_Type()
)
tmnxSrrpOperVrrpPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperVrrpPolicy2.setStatus("current")


class _TmnxSrrpOperFlags_Type(Bits):
    """Custom type tmnxSrrpOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("subnetMismatch", 0),
          ("srrpIdMismatch", 1),
          ("sapMismatch", 2),
          ("sapTagMismatch", 3),
          ("redIfMismatch", 4),
          ("dualMaster", 5),
          ("dupSubIfAddr", 6))
    )

_TmnxSrrpOperFlags_Type.__name__ = "Bits"
_TmnxSrrpOperFlags_Object = MibTableColumn
tmnxSrrpOperFlags = _TmnxSrrpOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 17),
    _TmnxSrrpOperFlags_Type()
)
tmnxSrrpOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperFlags.setStatus("current")
_TmnxSrrpOperMasterDownInterval_Type = TimeInterval
_TmnxSrrpOperMasterDownInterval_Object = MibTableColumn
tmnxSrrpOperMasterDownInterval = _TmnxSrrpOperMasterDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 18),
    _TmnxSrrpOperMasterDownInterval_Type()
)
tmnxSrrpOperMasterDownInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperMasterDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSrrpOperMasterDownInterval.setUnits("milliseconds")
_TmnxSrrpOperMasterDownTimer_Type = TimeInterval
_TmnxSrrpOperMasterDownTimer_Object = MibTableColumn
tmnxSrrpOperMasterDownTimer = _TmnxSrrpOperMasterDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 19),
    _TmnxSrrpOperMasterDownTimer_Type()
)
tmnxSrrpOperMasterDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperMasterDownTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxSrrpOperMasterDownTimer.setUnits("milliseconds")


class _TmnxSrrpOperSendFibPopulation_Type(Integer32):
    """Custom type tmnxSrrpOperSendFibPopulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("outerTagOnly", 2))
    )


_TmnxSrrpOperSendFibPopulation_Type.__name__ = "Integer32"
_TmnxSrrpOperSendFibPopulation_Object = MibTableColumn
tmnxSrrpOperSendFibPopulation = _TmnxSrrpOperSendFibPopulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 20),
    _TmnxSrrpOperSendFibPopulation_Type()
)
tmnxSrrpOperSendFibPopulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperSendFibPopulation.setStatus("current")


class _TmnxSrrpOperPreempt_Type(TruthValue):
    """Custom type tmnxSrrpOperPreempt based on TruthValue"""
    defaultValue = 1


_TmnxSrrpOperPreempt_Type.__name__ = "TruthValue"
_TmnxSrrpOperPreempt_Object = MibTableColumn
tmnxSrrpOperPreempt = _TmnxSrrpOperPreempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 21),
    _TmnxSrrpOperPreempt_Type()
)
tmnxSrrpOperPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperPreempt.setStatus("current")


class _TmnxSrrpOperOneGarpPerSap_Type(TruthValue):
    """Custom type tmnxSrrpOperOneGarpPerSap based on TruthValue"""
    defaultValue = 2


_TmnxSrrpOperOneGarpPerSap_Type.__name__ = "TruthValue"
_TmnxSrrpOperOneGarpPerSap_Object = MibTableColumn
tmnxSrrpOperOneGarpPerSap = _TmnxSrrpOperOneGarpPerSap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 22),
    _TmnxSrrpOperOneGarpPerSap_Type()
)
tmnxSrrpOperOneGarpPerSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperOneGarpPerSap.setStatus("current")


class _TmnxSrrpOperMonitorOperGrp_Type(TNamedItemOrEmpty):
    """Custom type tmnxSrrpOperMonitorOperGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxSrrpOperMonitorOperGrp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxSrrpOperMonitorOperGrp_Object = MibTableColumn
tmnxSrrpOperMonitorOperGrp = _TmnxSrrpOperMonitorOperGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 23),
    _TmnxSrrpOperMonitorOperGrp_Type()
)
tmnxSrrpOperMonitorOperGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperMonitorOperGrp.setStatus("current")


class _TmnxSrrpOperPriorityStep_Type(TmnxSrrpPriorityStep):
    """Custom type tmnxSrrpOperPriorityStep based on TmnxSrrpPriorityStep"""
    defaultValue = 0


_TmnxSrrpOperPriorityStep_Type.__name__ = "TmnxSrrpPriorityStep"
_TmnxSrrpOperPriorityStep_Object = MibTableColumn
tmnxSrrpOperPriorityStep = _TmnxSrrpOperPriorityStep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 24),
    _TmnxSrrpOperPriorityStep_Type()
)
tmnxSrrpOperPriorityStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpOperPriorityStep.setStatus("current")


class _TmnxSrrpOperDownReason_Type(Integer32):
    """Custom type tmnxSrrpOperDownReason based on Integer32"""
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
        *(("unknown", 0),
          ("notActive", 1),
          ("adminDown", 2),
          ("ifDown", 3),
          ("invalidMac", 4),
          ("messageSapDown", 5))
    )


_TmnxSrrpOperDownReason_Type.__name__ = "Integer32"
_TmnxSrrpOperDownReason_Object = MibTableColumn
tmnxSrrpOperDownReason = _TmnxSrrpOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 9, 1, 27),
    _TmnxSrrpOperDownReason_Type()
)
tmnxSrrpOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpOperDownReason.setStatus("current")
_TmnxMcLagInfoLagTable_Object = MibTable
tmnxMcLagInfoLagTable = _TmnxMcLagInfoLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxMcLagInfoLagTable.setStatus("current")
_TmnxMcLagInfoLagEntry_Object = MibTableRow
tmnxMcLagInfoLagEntry = _TmnxMcLagInfoLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxMcLagInfoLagEntry.setStatus("current")
_TmnxMcLagActiveStandby_Type = TruthValue
_TmnxMcLagActiveStandby_Object = MibTableColumn
tmnxMcLagActiveStandby = _TmnxMcLagActiveStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1, 1),
    _TmnxMcLagActiveStandby_Type()
)
tmnxMcLagActiveStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagActiveStandby.setStatus("current")
_TmnxMcLagLacpIdInUse_Type = TruthValue
_TmnxMcLagLacpIdInUse_Object = MibTableColumn
tmnxMcLagLacpIdInUse = _TmnxMcLagLacpIdInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1, 2),
    _TmnxMcLagLacpIdInUse_Type()
)
tmnxMcLagLacpIdInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagLacpIdInUse.setStatus("current")
_TmnxMcLagExtendedTimeOut_Type = TruthValue
_TmnxMcLagExtendedTimeOut_Object = MibTableColumn
tmnxMcLagExtendedTimeOut = _TmnxMcLagExtendedTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1, 3),
    _TmnxMcLagExtendedTimeOut_Type()
)
tmnxMcLagExtendedTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagExtendedTimeOut.setStatus("current")
_TmnxMcLagSelectionLogic_Type = DisplayString
_TmnxMcLagSelectionLogic_Object = MibTableColumn
tmnxMcLagSelectionLogic = _TmnxMcLagSelectionLogic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1, 4),
    _TmnxMcLagSelectionLogic_Type()
)
tmnxMcLagSelectionLogic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagSelectionLogic.setStatus("current")
_TmnxMcLagConfigMismatchString_Type = DisplayString
_TmnxMcLagConfigMismatchString_Object = MibTableColumn
tmnxMcLagConfigMismatchString = _TmnxMcLagConfigMismatchString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1, 5),
    _TmnxMcLagConfigMismatchString_Type()
)
tmnxMcLagConfigMismatchString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigMismatchString.setStatus("current")


class _TmnxMcLagConfigMismatchFlags_Type(Bits):
    """Custom type tmnxMcLagConfigMismatchFlags based on Bits"""
    namedValues = NamedValues(
        *(("lagIsNotMultiChassis", 0),
          ("localRemoteLagIdMismatch", 1),
          ("lagSelectionCriteriaMismatch", 2),
          ("lagEncapsulationMismatch", 3),
          ("mcLacpkeyMismatch", 4),
          ("mcSystemPriorityMismatch", 5),
          ("mcSystemIdMismatch", 6))
    )

_TmnxMcLagConfigMismatchFlags_Type.__name__ = "Bits"
_TmnxMcLagConfigMismatchFlags_Object = MibTableColumn
tmnxMcLagConfigMismatchFlags = _TmnxMcLagConfigMismatchFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 10, 1, 6),
    _TmnxMcLagConfigMismatchFlags_Type()
)
tmnxMcLagConfigMismatchFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagConfigMismatchFlags.setStatus("current")
_TmnxMcsClientAppTable_Object = MibTable
tmnxMcsClientAppTable = _TmnxMcsClientAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxMcsClientAppTable.setStatus("current")
_TmnxMcsClientAppEntry_Object = MibTableRow
tmnxMcsClientAppEntry = _TmnxMcsClientAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1)
)
tmnxMcsClientAppEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientApplication"),
)
if mibBuilder.loadTexts:
    tmnxMcsClientAppEntry.setStatus("current")
_TmnxMcsClientApplication_Type = TmnxMcsClientApp
_TmnxMcsClientApplication_Object = MibTableColumn
tmnxMcsClientApplication = _TmnxMcsClientApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 1),
    _TmnxMcsClientApplication_Type()
)
tmnxMcsClientApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcsClientApplication.setStatus("current")
_TmnxMcsClientNumEntries_Type = Counter32
_TmnxMcsClientNumEntries_Object = MibTableColumn
tmnxMcsClientNumEntries = _TmnxMcsClientNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 2),
    _TmnxMcsClientNumEntries_Type()
)
tmnxMcsClientNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientNumEntries.setStatus("current")
_TmnxMcsClientLclDeletedEntries_Type = Counter32
_TmnxMcsClientLclDeletedEntries_Object = MibTableColumn
tmnxMcsClientLclDeletedEntries = _TmnxMcsClientLclDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 3),
    _TmnxMcsClientLclDeletedEntries_Type()
)
tmnxMcsClientLclDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientLclDeletedEntries.setStatus("current")
_TmnxMcsClientAlarmedEntries_Type = Counter32
_TmnxMcsClientAlarmedEntries_Object = MibTableColumn
tmnxMcsClientAlarmedEntries = _TmnxMcsClientAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 4),
    _TmnxMcsClientAlarmedEntries_Type()
)
tmnxMcsClientAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientAlarmedEntries.setStatus("current")
_TmnxMcsClientRemNumEntries_Type = Counter32
_TmnxMcsClientRemNumEntries_Object = MibTableColumn
tmnxMcsClientRemNumEntries = _TmnxMcsClientRemNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 5),
    _TmnxMcsClientRemNumEntries_Type()
)
tmnxMcsClientRemNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientRemNumEntries.setStatus("current")
_TmnxMcsClientRemLclDelEntries_Type = Counter32
_TmnxMcsClientRemLclDelEntries_Object = MibTableColumn
tmnxMcsClientRemLclDelEntries = _TmnxMcsClientRemLclDelEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 6),
    _TmnxMcsClientRemLclDelEntries_Type()
)
tmnxMcsClientRemLclDelEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientRemLclDelEntries.setStatus("current")
_TmnxMcsClientRemAlarmedEntries_Type = Counter32
_TmnxMcsClientRemAlarmedEntries_Object = MibTableColumn
tmnxMcsClientRemAlarmedEntries = _TmnxMcsClientRemAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 7),
    _TmnxMcsClientRemAlarmedEntries_Type()
)
tmnxMcsClientRemAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientRemAlarmedEntries.setStatus("current")
_TmnxMcsClientOmcrStandby_Type = Counter32
_TmnxMcsClientOmcrStandby_Object = MibTableColumn
tmnxMcsClientOmcrStandby = _TmnxMcsClientOmcrStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 8),
    _TmnxMcsClientOmcrStandby_Type()
)
tmnxMcsClientOmcrStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientOmcrStandby.setStatus("current")
_TmnxMcsClientOmcrAlarmed_Type = Counter32
_TmnxMcsClientOmcrAlarmed_Object = MibTableColumn
tmnxMcsClientOmcrAlarmed = _TmnxMcsClientOmcrAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 9),
    _TmnxMcsClientOmcrAlarmed_Type()
)
tmnxMcsClientOmcrAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientOmcrAlarmed.setStatus("current")
_TmnxMcsClientOmcrRemStandby_Type = Counter32
_TmnxMcsClientOmcrRemStandby_Object = MibTableColumn
tmnxMcsClientOmcrRemStandby = _TmnxMcsClientOmcrRemStandby_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 10),
    _TmnxMcsClientOmcrRemStandby_Type()
)
tmnxMcsClientOmcrRemStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientOmcrRemStandby.setStatus("current")
_TmnxMcsClientOmcrRemAlarmed_Type = Counter32
_TmnxMcsClientOmcrRemAlarmed_Object = MibTableColumn
tmnxMcsClientOmcrRemAlarmed = _TmnxMcsClientOmcrRemAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 11, 1, 11),
    _TmnxMcsClientOmcrRemAlarmed_Type()
)
tmnxMcsClientOmcrRemAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsClientOmcrRemAlarmed.setStatus("current")
_TmnxSrrpStatsTable_Object = MibTable
tmnxSrrpStatsTable = _TmnxSrrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxSrrpStatsTable.setStatus("current")
_TmnxSrrpStatsEntry_Object = MibTableRow
tmnxSrrpStatsEntry = _TmnxSrrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1)
)
tmnxSrrpStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperID"),
)
if mibBuilder.loadTexts:
    tmnxSrrpStatsEntry.setStatus("current")
_TmnxSrrpStatsBecomeMaster_Type = Counter32
_TmnxSrrpStatsBecomeMaster_Object = MibTableColumn
tmnxSrrpStatsBecomeMaster = _TmnxSrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 1),
    _TmnxSrrpStatsBecomeMaster_Type()
)
tmnxSrrpStatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsBecomeMaster.setStatus("current")
_TmnxSrrpStatsMasterChanges_Type = Counter32
_TmnxSrrpStatsMasterChanges_Object = MibTableColumn
tmnxSrrpStatsMasterChanges = _TmnxSrrpStatsMasterChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 2),
    _TmnxSrrpStatsMasterChanges_Type()
)
tmnxSrrpStatsMasterChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsMasterChanges.setStatus("current")
_TmnxSrrpStatsAdvSent_Type = Counter32
_TmnxSrrpStatsAdvSent_Object = MibTableColumn
tmnxSrrpStatsAdvSent = _TmnxSrrpStatsAdvSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 3),
    _TmnxSrrpStatsAdvSent_Type()
)
tmnxSrrpStatsAdvSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsAdvSent.setStatus("current")
_TmnxSrrpStatsAdvRcvd_Type = Counter32
_TmnxSrrpStatsAdvRcvd_Object = MibTableColumn
tmnxSrrpStatsAdvRcvd = _TmnxSrrpStatsAdvRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 4),
    _TmnxSrrpStatsAdvRcvd_Type()
)
tmnxSrrpStatsAdvRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsAdvRcvd.setStatus("current")
_TmnxSrrpStatsPriZeroPktsRcvd_Type = Counter32
_TmnxSrrpStatsPriZeroPktsRcvd_Object = MibTableColumn
tmnxSrrpStatsPriZeroPktsRcvd = _TmnxSrrpStatsPriZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 5),
    _TmnxSrrpStatsPriZeroPktsRcvd_Type()
)
tmnxSrrpStatsPriZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsPriZeroPktsRcvd.setStatus("current")
_TmnxSrrpStatsPriZeroPktsSent_Type = Counter32
_TmnxSrrpStatsPriZeroPktsSent_Object = MibTableColumn
tmnxSrrpStatsPriZeroPktsSent = _TmnxSrrpStatsPriZeroPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 6),
    _TmnxSrrpStatsPriZeroPktsSent_Type()
)
tmnxSrrpStatsPriZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsPriZeroPktsSent.setStatus("current")
_TmnxSrrpStatsPreemptEvents_Type = Counter32
_TmnxSrrpStatsPreemptEvents_Object = MibTableColumn
tmnxSrrpStatsPreemptEvents = _TmnxSrrpStatsPreemptEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 7),
    _TmnxSrrpStatsPreemptEvents_Type()
)
tmnxSrrpStatsPreemptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsPreemptEvents.setStatus("current")
_TmnxSrrpStatsPreemptedEvents_Type = Counter32
_TmnxSrrpStatsPreemptedEvents_Object = MibTableColumn
tmnxSrrpStatsPreemptedEvents = _TmnxSrrpStatsPreemptedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 8),
    _TmnxSrrpStatsPreemptedEvents_Type()
)
tmnxSrrpStatsPreemptedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsPreemptedEvents.setStatus("current")
_TmnxSrrpStatsAdvIntDiscards_Type = Counter32
_TmnxSrrpStatsAdvIntDiscards_Object = MibTableColumn
tmnxSrrpStatsAdvIntDiscards = _TmnxSrrpStatsAdvIntDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 9),
    _TmnxSrrpStatsAdvIntDiscards_Type()
)
tmnxSrrpStatsAdvIntDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsAdvIntDiscards.setStatus("current")
_TmnxSrrpStatsAdvIntErrors_Type = Counter32
_TmnxSrrpStatsAdvIntErrors_Object = MibTableColumn
tmnxSrrpStatsAdvIntErrors = _TmnxSrrpStatsAdvIntErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 10),
    _TmnxSrrpStatsAdvIntErrors_Type()
)
tmnxSrrpStatsAdvIntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsAdvIntErrors.setStatus("current")
_TmnxSrrpStatsBecomeBackupRouting_Type = Counter32
_TmnxSrrpStatsBecomeBackupRouting_Object = MibTableColumn
tmnxSrrpStatsBecomeBackupRouting = _TmnxSrrpStatsBecomeBackupRouting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 11),
    _TmnxSrrpStatsBecomeBackupRouting_Type()
)
tmnxSrrpStatsBecomeBackupRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsBecomeBackupRouting.setStatus("current")
_TmnxSrrpStatsBecomeBackupShunt_Type = Counter32
_TmnxSrrpStatsBecomeBackupShunt_Object = MibTableColumn
tmnxSrrpStatsBecomeBackupShunt = _TmnxSrrpStatsBecomeBackupShunt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 12),
    _TmnxSrrpStatsBecomeBackupShunt_Type()
)
tmnxSrrpStatsBecomeBackupShunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsBecomeBackupShunt.setStatus("current")
_TmnxSrrpStatsBecomeNonMaster_Type = Counter32
_TmnxSrrpStatsBecomeNonMaster_Object = MibTableColumn
tmnxSrrpStatsBecomeNonMaster = _TmnxSrrpStatsBecomeNonMaster_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 12, 1, 13),
    _TmnxSrrpStatsBecomeNonMaster_Type()
)
tmnxSrrpStatsBecomeNonMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpStatsBecomeNonMaster.setStatus("current")
_TmnxMcRingTableLastChanged_Type = TimeStamp
_TmnxMcRingTableLastChanged_Object = MibScalar
tmnxMcRingTableLastChanged = _TmnxMcRingTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 13),
    _TmnxMcRingTableLastChanged_Type()
)
tmnxMcRingTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingTableLastChanged.setStatus("current")
_TmnxMcRingTable_Object = MibTable
tmnxMcRingTable = _TmnxMcRingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxMcRingTable.setStatus("current")
_TmnxMcRingEntry_Object = MibTableRow
tmnxMcRingEntry = _TmnxMcRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1)
)
tmnxMcRingEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
)
if mibBuilder.loadTexts:
    tmnxMcRingEntry.setStatus("current")
_TmnxMcRingRowStatus_Type = RowStatus
_TmnxMcRingRowStatus_Object = MibTableColumn
tmnxMcRingRowStatus = _TmnxMcRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 1),
    _TmnxMcRingRowStatus_Type()
)
tmnxMcRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingRowStatus.setStatus("current")
_TmnxMcRingLastChanged_Type = TimeStamp
_TmnxMcRingLastChanged_Object = MibTableColumn
tmnxMcRingLastChanged = _TmnxMcRingLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 2),
    _TmnxMcRingLastChanged_Type()
)
tmnxMcRingLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingLastChanged.setStatus("current")


class _TmnxMcRingAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcRingAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcRingAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcRingAdminState_Object = MibTableColumn
tmnxMcRingAdminState = _TmnxMcRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 3),
    _TmnxMcRingAdminState_Type()
)
tmnxMcRingAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingAdminState.setStatus("current")


class _TmnxMcRingInbCtrlSvcId_Type(TmnxServId):
    """Custom type tmnxMcRingInbCtrlSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxMcRingInbCtrlSvcId_Type.__name__ = "TmnxServId"
_TmnxMcRingInbCtrlSvcId_Object = MibTableColumn
tmnxMcRingInbCtrlSvcId = _TmnxMcRingInbCtrlSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 4),
    _TmnxMcRingInbCtrlSvcId_Type()
)
tmnxMcRingInbCtrlSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlSvcId.setStatus("current")


class _TmnxMcRingInbCtrlIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcRingInbCtrlIfName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxMcRingInbCtrlIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcRingInbCtrlIfName_Object = MibTableColumn
tmnxMcRingInbCtrlIfName = _TmnxMcRingInbCtrlIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 5),
    _TmnxMcRingInbCtrlIfName_Type()
)
tmnxMcRingInbCtrlIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlIfName.setStatus("current")


class _TmnxMcRingInbCtrlDestIpType_Type(InetAddressType):
    """Custom type tmnxMcRingInbCtrlDestIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcRingInbCtrlDestIpType_Type.__name__ = "InetAddressType"
_TmnxMcRingInbCtrlDestIpType_Object = MibTableColumn
tmnxMcRingInbCtrlDestIpType = _TmnxMcRingInbCtrlDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 6),
    _TmnxMcRingInbCtrlDestIpType_Type()
)
tmnxMcRingInbCtrlDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlDestIpType.setStatus("current")


class _TmnxMcRingInbCtrlDestIp_Type(InetAddress):
    """Custom type tmnxMcRingInbCtrlDestIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcRingInbCtrlDestIp_Type.__name__ = "InetAddress"
_TmnxMcRingInbCtrlDestIp_Object = MibTableColumn
tmnxMcRingInbCtrlDestIp = _TmnxMcRingInbCtrlDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 7),
    _TmnxMcRingInbCtrlDestIp_Type()
)
tmnxMcRingInbCtrlDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlDestIp.setStatus("current")


class _TmnxMcRingVlanMap_Type(OctetString):
    """Custom type tmnxMcRingVlanMap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(512, 512),
    )


_TmnxMcRingVlanMap_Type.__name__ = "OctetString"
_TmnxMcRingVlanMap_Object = MibTableColumn
tmnxMcRingVlanMap = _TmnxMcRingVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 8),
    _TmnxMcRingVlanMap_Type()
)
tmnxMcRingVlanMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingVlanMap.setStatus("current")


class _TmnxMcRingVlanMapExcl_Type(OctetString):
    """Custom type tmnxMcRingVlanMapExcl based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(512, 512),
    )


_TmnxMcRingVlanMapExcl_Type.__name__ = "OctetString"
_TmnxMcRingVlanMapExcl_Object = MibTableColumn
tmnxMcRingVlanMapExcl = _TmnxMcRingVlanMapExcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 9),
    _TmnxMcRingVlanMapExcl_Type()
)
tmnxMcRingVlanMapExcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingVlanMapExcl.setStatus("current")


class _TmnxMcRingInbCtrlDbMax_Type(Unsigned32):
    """Custom type tmnxMcRingInbCtrlDbMax based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_TmnxMcRingInbCtrlDbMax_Type.__name__ = "Unsigned32"
_TmnxMcRingInbCtrlDbMax_Object = MibTableColumn
tmnxMcRingInbCtrlDbMax = _TmnxMcRingInbCtrlDbMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 20),
    _TmnxMcRingInbCtrlDbMax_Type()
)
tmnxMcRingInbCtrlDbMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlDbMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlDbMax.setUnits("seconds")


class _TmnxMcRingInbCtrlDbAdmin_Type(TmnxAdminState):
    """Custom type tmnxMcRingInbCtrlDbAdmin based on TmnxAdminState"""
    defaultValue = 2


_TmnxMcRingInbCtrlDbAdmin_Type.__name__ = "TmnxAdminState"
_TmnxMcRingInbCtrlDbAdmin_Object = MibTableColumn
tmnxMcRingInbCtrlDbAdmin = _TmnxMcRingInbCtrlDbAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 21),
    _TmnxMcRingInbCtrlDbAdmin_Type()
)
tmnxMcRingInbCtrlDbAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlDbAdmin.setStatus("current")


class _TmnxMcRingType_Type(TmnxMcRingType):
    """Custom type tmnxMcRingType based on TmnxMcRingType"""
    defaultValue = 1


_TmnxMcRingType_Type.__name__ = "TmnxMcRingType"
_TmnxMcRingType_Object = MibTableColumn
tmnxMcRingType = _TmnxMcRingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 14, 1, 22),
    _TmnxMcRingType_Type()
)
tmnxMcRingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingType.setStatus("current")
_TmnxMcRingInfoTableLastChanged_Type = TimeStamp
_TmnxMcRingInfoTableLastChanged_Object = MibScalar
tmnxMcRingInfoTableLastChanged = _TmnxMcRingInfoTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 15),
    _TmnxMcRingInfoTableLastChanged_Type()
)
tmnxMcRingInfoTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoTableLastChanged.setStatus("current")
_TmnxMcRingInfoTable_Object = MibTable
tmnxMcRingInfoTable = _TmnxMcRingInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxMcRingInfoTable.setStatus("current")
_TmnxMcRingInfoEntry_Object = MibTableRow
tmnxMcRingInfoEntry = _TmnxMcRingInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1)
)
if mibBuilder.loadTexts:
    tmnxMcRingInfoEntry.setStatus("current")
_TmnxMcRingInfoLastChanged_Type = TimeStamp
_TmnxMcRingInfoLastChanged_Object = MibTableColumn
tmnxMcRingInfoLastChanged = _TmnxMcRingInfoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 1),
    _TmnxMcRingInfoLastChanged_Type()
)
tmnxMcRingInfoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoLastChanged.setStatus("current")
_TmnxMcRingInfoOperState_Type = TmnxMcRingOperState
_TmnxMcRingInfoOperState_Object = MibTableColumn
tmnxMcRingInfoOperState = _TmnxMcRingInfoOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 2),
    _TmnxMcRingInfoOperState_Type()
)
tmnxMcRingInfoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoOperState.setStatus("current")


class _TmnxMcRingInfoFailureReason_Type(DisplayString):
    """Custom type tmnxMcRingInfoFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxMcRingInfoFailureReason_Type.__name__ = "DisplayString"
_TmnxMcRingInfoFailureReason_Object = MibTableColumn
tmnxMcRingInfoFailureReason = _TmnxMcRingInfoFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 3),
    _TmnxMcRingInfoFailureReason_Type()
)
tmnxMcRingInfoFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoFailureReason.setStatus("current")
_TmnxMcRingInfoInbCtrlOperState_Type = TmnxMcRingInbCtrlOperState
_TmnxMcRingInfoInbCtrlOperState_Object = MibTableColumn
tmnxMcRingInfoInbCtrlOperState = _TmnxMcRingInfoInbCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 4),
    _TmnxMcRingInfoInbCtrlOperState_Type()
)
tmnxMcRingInfoInbCtrlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlOperState.setStatus("current")
_TmnxMcRingInfoInbCtrlSrcIpType_Type = InetAddressType
_TmnxMcRingInfoInbCtrlSrcIpType_Object = MibTableColumn
tmnxMcRingInfoInbCtrlSrcIpType = _TmnxMcRingInfoInbCtrlSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 5),
    _TmnxMcRingInfoInbCtrlSrcIpType_Type()
)
tmnxMcRingInfoInbCtrlSrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlSrcIpType.setStatus("current")


class _TmnxMcRingInfoInbCtrlSrcIp_Type(InetAddress):
    """Custom type tmnxMcRingInfoInbCtrlSrcIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcRingInfoInbCtrlSrcIp_Type.__name__ = "InetAddress"
_TmnxMcRingInfoInbCtrlSrcIp_Object = MibTableColumn
tmnxMcRingInfoInbCtrlSrcIp = _TmnxMcRingInfoInbCtrlSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 6),
    _TmnxMcRingInfoInbCtrlSrcIp_Type()
)
tmnxMcRingInfoInbCtrlSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlSrcIp.setStatus("current")
_TmnxMcRingInfoInbCtrlDbStart_Type = TimeStamp
_TmnxMcRingInfoInbCtrlDbStart_Object = MibTableColumn
tmnxMcRingInfoInbCtrlDbStart = _TmnxMcRingInfoInbCtrlDbStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 7),
    _TmnxMcRingInfoInbCtrlDbStart_Type()
)
tmnxMcRingInfoInbCtrlDbStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlDbStart.setStatus("current")
_TmnxMcRingInfoInbCtrlDbTime_Type = TimeInterval
_TmnxMcRingInfoInbCtrlDbTime_Object = MibTableColumn
tmnxMcRingInfoInbCtrlDbTime = _TmnxMcRingInfoInbCtrlDbTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 8),
    _TmnxMcRingInfoInbCtrlDbTime_Type()
)
tmnxMcRingInfoInbCtrlDbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlDbTime.setStatus("current")
_TmnxMcRingInfoPortId_Type = TmnxPortID
_TmnxMcRingInfoPortId_Object = MibTableColumn
tmnxMcRingInfoPortId = _TmnxMcRingInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 9),
    _TmnxMcRingInfoPortId_Type()
)
tmnxMcRingInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoPortId.setStatus("current")


class _TmnxMcRingInfoVlanMap_Type(OctetString):
    """Custom type tmnxMcRingInfoVlanMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(512, 512),
    )


_TmnxMcRingInfoVlanMap_Type.__name__ = "OctetString"
_TmnxMcRingInfoVlanMap_Object = MibTableColumn
tmnxMcRingInfoVlanMap = _TmnxMcRingInfoVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 10),
    _TmnxMcRingInfoVlanMap_Type()
)
tmnxMcRingInfoVlanMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoVlanMap.setStatus("current")


class _TmnxMcRingInfoVlanMapExcl_Type(OctetString):
    """Custom type tmnxMcRingInfoVlanMapExcl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(512, 512),
    )


_TmnxMcRingInfoVlanMapExcl_Type.__name__ = "OctetString"
_TmnxMcRingInfoVlanMapExcl_Object = MibTableColumn
tmnxMcRingInfoVlanMapExcl = _TmnxMcRingInfoVlanMapExcl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 11),
    _TmnxMcRingInfoVlanMapExcl_Type()
)
tmnxMcRingInfoVlanMapExcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoVlanMapExcl.setStatus("current")
_TmnxMcRingInfoCtrlVlanMap_Type = TruthValue
_TmnxMcRingInfoCtrlVlanMap_Object = MibTableColumn
tmnxMcRingInfoCtrlVlanMap = _TmnxMcRingInfoCtrlVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 12),
    _TmnxMcRingInfoCtrlVlanMap_Type()
)
tmnxMcRingInfoCtrlVlanMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoCtrlVlanMap.setStatus("current")
_TmnxMcRingInfoInbCtrlDbGuard_Type = Unsigned32
_TmnxMcRingInfoInbCtrlDbGuard_Object = MibTableColumn
tmnxMcRingInfoInbCtrlDbGuard = _TmnxMcRingInfoInbCtrlDbGuard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 16, 1, 13),
    _TmnxMcRingInfoInbCtrlDbGuard_Type()
)
tmnxMcRingInfoInbCtrlDbGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlDbGuard.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcRingInfoInbCtrlDbGuard.setUnits("seconds")
_TmnxMcRingNodeTableLastChanged_Type = TimeStamp
_TmnxMcRingNodeTableLastChanged_Object = MibScalar
tmnxMcRingNodeTableLastChanged = _TmnxMcRingNodeTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 17),
    _TmnxMcRingNodeTableLastChanged_Type()
)
tmnxMcRingNodeTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeTableLastChanged.setStatus("current")
_TmnxMcRingNodeTable_Object = MibTable
tmnxMcRingNodeTable = _TmnxMcRingNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxMcRingNodeTable.setStatus("current")
_TmnxMcRingNodeEntry_Object = MibTableRow
tmnxMcRingNodeEntry = _TmnxMcRingNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1)
)
tmnxMcRingNodeEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeName"),
)
if mibBuilder.loadTexts:
    tmnxMcRingNodeEntry.setStatus("current")
_TmnxMcRingNodeName_Type = TNamedItem
_TmnxMcRingNodeName_Object = MibTableColumn
tmnxMcRingNodeName = _TmnxMcRingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 1),
    _TmnxMcRingNodeName_Type()
)
tmnxMcRingNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcRingNodeName.setStatus("current")
_TmnxMcRingNodeRowStatus_Type = RowStatus
_TmnxMcRingNodeRowStatus_Object = MibTableColumn
tmnxMcRingNodeRowStatus = _TmnxMcRingNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 2),
    _TmnxMcRingNodeRowStatus_Type()
)
tmnxMcRingNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRowStatus.setStatus("current")
_TmnxMcRingNodeLastChanged_Type = TimeStamp
_TmnxMcRingNodeLastChanged_Object = MibTableColumn
tmnxMcRingNodeLastChanged = _TmnxMcRingNodeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 3),
    _TmnxMcRingNodeLastChanged_Type()
)
tmnxMcRingNodeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeLastChanged.setStatus("current")


class _TmnxMcRingNodeRncvAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcRingNodeRncvAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcRingNodeRncvAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcRingNodeRncvAdminState_Object = MibTableColumn
tmnxMcRingNodeRncvAdminState = _TmnxMcRingNodeRncvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 4),
    _TmnxMcRingNodeRncvAdminState_Type()
)
tmnxMcRingNodeRncvAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvAdminState.setStatus("current")


class _TmnxMcRingNodeRncvSvcId_Type(TmnxServId):
    """Custom type tmnxMcRingNodeRncvSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxMcRingNodeRncvSvcId_Type.__name__ = "TmnxServId"
_TmnxMcRingNodeRncvSvcId_Object = MibTableColumn
tmnxMcRingNodeRncvSvcId = _TmnxMcRingNodeRncvSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 5),
    _TmnxMcRingNodeRncvSvcId_Type()
)
tmnxMcRingNodeRncvSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvSvcId.setStatus("current")


class _TmnxMcRingNodeRncvEncapValue_Type(TmnxEncapVal):
    """Custom type tmnxMcRingNodeRncvEncapValue based on TmnxEncapVal"""
    defaultValue = 0


_TmnxMcRingNodeRncvEncapValue_Type.__name__ = "TmnxEncapVal"
_TmnxMcRingNodeRncvEncapValue_Object = MibTableColumn
tmnxMcRingNodeRncvEncapValue = _TmnxMcRingNodeRncvEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 6),
    _TmnxMcRingNodeRncvEncapValue_Type()
)
tmnxMcRingNodeRncvEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvEncapValue.setStatus("current")


class _TmnxMcRingNodeRncvSrcIpType_Type(InetAddressType):
    """Custom type tmnxMcRingNodeRncvSrcIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcRingNodeRncvSrcIpType_Type.__name__ = "InetAddressType"
_TmnxMcRingNodeRncvSrcIpType_Object = MibTableColumn
tmnxMcRingNodeRncvSrcIpType = _TmnxMcRingNodeRncvSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 7),
    _TmnxMcRingNodeRncvSrcIpType_Type()
)
tmnxMcRingNodeRncvSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvSrcIpType.setStatus("current")


class _TmnxMcRingNodeRncvSrcIp_Type(InetAddress):
    """Custom type tmnxMcRingNodeRncvSrcIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcRingNodeRncvSrcIp_Type.__name__ = "InetAddress"
_TmnxMcRingNodeRncvSrcIp_Object = MibTableColumn
tmnxMcRingNodeRncvSrcIp = _TmnxMcRingNodeRncvSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 8),
    _TmnxMcRingNodeRncvSrcIp_Type()
)
tmnxMcRingNodeRncvSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvSrcIp.setStatus("current")


class _TmnxMcRingNodeRncvDestIpType_Type(InetAddressType):
    """Custom type tmnxMcRingNodeRncvDestIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcRingNodeRncvDestIpType_Type.__name__ = "InetAddressType"
_TmnxMcRingNodeRncvDestIpType_Object = MibTableColumn
tmnxMcRingNodeRncvDestIpType = _TmnxMcRingNodeRncvDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 9),
    _TmnxMcRingNodeRncvDestIpType_Type()
)
tmnxMcRingNodeRncvDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvDestIpType.setStatus("current")


class _TmnxMcRingNodeRncvDestIp_Type(InetAddress):
    """Custom type tmnxMcRingNodeRncvDestIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcRingNodeRncvDestIp_Type.__name__ = "InetAddress"
_TmnxMcRingNodeRncvDestIp_Object = MibTableColumn
tmnxMcRingNodeRncvDestIp = _TmnxMcRingNodeRncvDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 10),
    _TmnxMcRingNodeRncvDestIp_Type()
)
tmnxMcRingNodeRncvDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvDestIp.setStatus("current")


class _TmnxMcRingNodeRncvInterval_Type(Unsigned32):
    """Custom type tmnxMcRingNodeRncvInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_TmnxMcRingNodeRncvInterval_Type.__name__ = "Unsigned32"
_TmnxMcRingNodeRncvInterval_Object = MibTableColumn
tmnxMcRingNodeRncvInterval = _TmnxMcRingNodeRncvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 11),
    _TmnxMcRingNodeRncvInterval_Type()
)
tmnxMcRingNodeRncvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvInterval.setUnits("minutes")


class _TmnxMcRingNodeRncvSrcMac_Type(MacAddress):
    """Custom type tmnxMcRingNodeRncvSrcMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMcRingNodeRncvSrcMac_Type.__name__ = "MacAddress"
_TmnxMcRingNodeRncvSrcMac_Object = MibTableColumn
tmnxMcRingNodeRncvSrcMac = _TmnxMcRingNodeRncvSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 18, 1, 12),
    _TmnxMcRingNodeRncvSrcMac_Type()
)
tmnxMcRingNodeRncvSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcRingNodeRncvSrcMac.setStatus("current")
_TmnxMcRingNodeInfoTableLastChgd_Type = TimeStamp
_TmnxMcRingNodeInfoTableLastChgd_Object = MibScalar
tmnxMcRingNodeInfoTableLastChgd = _TmnxMcRingNodeInfoTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 19),
    _TmnxMcRingNodeInfoTableLastChgd_Type()
)
tmnxMcRingNodeInfoTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoTableLastChgd.setStatus("current")
_TmnxMcRingNodeInfoTable_Object = MibTable
tmnxMcRingNodeInfoTable = _TmnxMcRingNodeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoTable.setStatus("current")
_TmnxMcRingNodeInfoEntry_Object = MibTableRow
tmnxMcRingNodeInfoEntry = _TmnxMcRingNodeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20, 1)
)
tmnxMcRingNodeInfoEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeName"),
)
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoEntry.setStatus("current")
_TmnxMcRingNodeInfoLastChanged_Type = TimeStamp
_TmnxMcRingNodeInfoLastChanged_Object = MibTableColumn
tmnxMcRingNodeInfoLastChanged = _TmnxMcRingNodeInfoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20, 1, 1),
    _TmnxMcRingNodeInfoLastChanged_Type()
)
tmnxMcRingNodeInfoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoLastChanged.setStatus("current")
_TmnxMcRingNodeInfoLocOperState_Type = TmnxMcRingNodeOperState
_TmnxMcRingNodeInfoLocOperState_Object = MibTableColumn
tmnxMcRingNodeInfoLocOperState = _TmnxMcRingNodeInfoLocOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20, 1, 2),
    _TmnxMcRingNodeInfoLocOperState_Type()
)
tmnxMcRingNodeInfoLocOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoLocOperState.setStatus("current")
_TmnxMcRingNodeInfoRemOperState_Type = TmnxMcRingNodeOperState
_TmnxMcRingNodeInfoRemOperState_Object = MibTableColumn
tmnxMcRingNodeInfoRemOperState = _TmnxMcRingNodeInfoRemOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20, 1, 3),
    _TmnxMcRingNodeInfoRemOperState_Type()
)
tmnxMcRingNodeInfoRemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoRemOperState.setStatus("current")
_TmnxMcRingNodeInfoInUse_Type = TruthValue
_TmnxMcRingNodeInfoInUse_Object = MibTableColumn
tmnxMcRingNodeInfoInUse = _TmnxMcRingNodeInfoInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20, 1, 4),
    _TmnxMcRingNodeInfoInUse_Type()
)
tmnxMcRingNodeInfoInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoInUse.setStatus("current")


class _TmnxMcRingNodeInfoFailureReason_Type(DisplayString):
    """Custom type tmnxMcRingNodeInfoFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxMcRingNodeInfoFailureReason_Type.__name__ = "DisplayString"
_TmnxMcRingNodeInfoFailureReason_Object = MibTableColumn
tmnxMcRingNodeInfoFailureReason = _TmnxMcRingNodeInfoFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 20, 1, 5),
    _TmnxMcRingNodeInfoFailureReason_Type()
)
tmnxMcRingNodeInfoFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingNodeInfoFailureReason.setStatus("current")
_TmnxMcTlsCfgTableLastChanged_Type = TimeStamp
_TmnxMcTlsCfgTableLastChanged_Object = MibScalar
tmnxMcTlsCfgTableLastChanged = _TmnxMcTlsCfgTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 21),
    _TmnxMcTlsCfgTableLastChanged_Type()
)
tmnxMcTlsCfgTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcTlsCfgTableLastChanged.setStatus("current")
_TmnxMcTlsCfgTable_Object = MibTable
tmnxMcTlsCfgTable = _TmnxMcTlsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 22)
)
if mibBuilder.loadTexts:
    tmnxMcTlsCfgTable.setStatus("current")
_TmnxMcTlsCfgEntry_Object = MibTableRow
tmnxMcTlsCfgEntry = _TmnxMcTlsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 22, 1)
)
if mibBuilder.loadTexts:
    tmnxMcTlsCfgEntry.setStatus("current")
_TmnxMcTlsCfgLastChanged_Type = TimeStamp
_TmnxMcTlsCfgLastChanged_Object = MibTableColumn
tmnxMcTlsCfgLastChanged = _TmnxMcTlsCfgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 22, 1, 1),
    _TmnxMcTlsCfgLastChanged_Type()
)
tmnxMcTlsCfgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcTlsCfgLastChanged.setStatus("current")


class _TmnxMcTlsCfgDefGwIpType_Type(InetAddressType):
    """Custom type tmnxMcTlsCfgDefGwIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcTlsCfgDefGwIpType_Type.__name__ = "InetAddressType"
_TmnxMcTlsCfgDefGwIpType_Object = MibTableColumn
tmnxMcTlsCfgDefGwIpType = _TmnxMcTlsCfgDefGwIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 22, 1, 2),
    _TmnxMcTlsCfgDefGwIpType_Type()
)
tmnxMcTlsCfgDefGwIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcTlsCfgDefGwIpType.setStatus("current")


class _TmnxMcTlsCfgDefGwIp_Type(InetAddress):
    """Custom type tmnxMcTlsCfgDefGwIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcTlsCfgDefGwIp_Type.__name__ = "InetAddress"
_TmnxMcTlsCfgDefGwIp_Object = MibTableColumn
tmnxMcTlsCfgDefGwIp = _TmnxMcTlsCfgDefGwIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 22, 1, 3),
    _TmnxMcTlsCfgDefGwIp_Type()
)
tmnxMcTlsCfgDefGwIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcTlsCfgDefGwIp.setStatus("current")


class _TmnxMcTlsCfgDefGwMac_Type(MacAddress):
    """Custom type tmnxMcTlsCfgDefGwMac based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxMcTlsCfgDefGwMac_Type.__name__ = "MacAddress"
_TmnxMcTlsCfgDefGwMac_Object = MibTableColumn
tmnxMcTlsCfgDefGwMac = _TmnxMcTlsCfgDefGwMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 22, 1, 4),
    _TmnxMcTlsCfgDefGwMac_Type()
)
tmnxMcTlsCfgDefGwMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcTlsCfgDefGwMac.setStatus("current")
_TmnxMcEpipeSapTableLastChanged_Type = TimeStamp
_TmnxMcEpipeSapTableLastChanged_Object = MibScalar
tmnxMcEpipeSapTableLastChanged = _TmnxMcEpipeSapTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 23),
    _TmnxMcEpipeSapTableLastChanged_Type()
)
tmnxMcEpipeSapTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpipeSapTableLastChanged.setStatus("current")
_TmnxMcEpipeSapTable_Object = MibTable
tmnxMcEpipeSapTable = _TmnxMcEpipeSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 24)
)
if mibBuilder.loadTexts:
    tmnxMcEpipeSapTable.setStatus("current")
_TmnxMcEpipeSapEntry_Object = MibTableRow
tmnxMcEpipeSapEntry = _TmnxMcEpipeSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 24, 1)
)
tmnxMcEpipeSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxMcEpipeSapEntry.setStatus("current")
_TmnxMcEpipeSapRowStatus_Type = RowStatus
_TmnxMcEpipeSapRowStatus_Object = MibTableColumn
tmnxMcEpipeSapRowStatus = _TmnxMcEpipeSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 24, 1, 1),
    _TmnxMcEpipeSapRowStatus_Type()
)
tmnxMcEpipeSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcEpipeSapRowStatus.setStatus("current")
_TmnxMcEpipeSapLastChanged_Type = TimeStamp
_TmnxMcEpipeSapLastChanged_Object = MibTableColumn
tmnxMcEpipeSapLastChanged = _TmnxMcEpipeSapLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 24, 1, 2),
    _TmnxMcEpipeSapLastChanged_Type()
)
tmnxMcEpipeSapLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpipeSapLastChanged.setStatus("current")


class _TmnxMcEpipeSapRingNodeName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcEpipeSapRingNodeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcEpipeSapRingNodeName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcEpipeSapRingNodeName_Object = MibTableColumn
tmnxMcEpipeSapRingNodeName = _TmnxMcEpipeSapRingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 24, 1, 3),
    _TmnxMcEpipeSapRingNodeName_Type()
)
tmnxMcEpipeSapRingNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcEpipeSapRingNodeName.setStatus("current")
_TmnxMcsDhcpsObjs_ObjectIdentity = ObjectIdentity
tmnxMcsDhcpsObjs = _TmnxMcsDhcpsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25)
)
_TmnxMcsDhcpsTableLastChgd_Type = TimeStamp
_TmnxMcsDhcpsTableLastChgd_Object = MibScalar
tmnxMcsDhcpsTableLastChgd = _TmnxMcsDhcpsTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 1),
    _TmnxMcsDhcpsTableLastChgd_Type()
)
tmnxMcsDhcpsTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsTableLastChgd.setStatus("current")
_TmnxMcsDhcpsTable_Object = MibTable
tmnxMcsDhcpsTable = _TmnxMcsDhcpsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2)
)
if mibBuilder.loadTexts:
    tmnxMcsDhcpsTable.setStatus("current")
_TmnxMcsDhcpsEntry_Object = MibTableRow
tmnxMcsDhcpsEntry = _TmnxMcsDhcpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1)
)
tmnxMcsDhcpsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsRtrID"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsServerName"),
)
if mibBuilder.loadTexts:
    tmnxMcsDhcpsEntry.setStatus("current")
_TmnxMcsDhcpsRtrID_Type = TmnxVRtrID
_TmnxMcsDhcpsRtrID_Object = MibTableColumn
tmnxMcsDhcpsRtrID = _TmnxMcsDhcpsRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1, 1),
    _TmnxMcsDhcpsRtrID_Type()
)
tmnxMcsDhcpsRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsRtrID.setStatus("current")
_TmnxMcsDhcpsServerName_Type = TNamedItem
_TmnxMcsDhcpsServerName_Object = MibTableColumn
tmnxMcsDhcpsServerName = _TmnxMcsDhcpsServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1, 2),
    _TmnxMcsDhcpsServerName_Type()
)
tmnxMcsDhcpsServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsServerName.setStatus("current")
_TmnxMcsDhcpsRowStatus_Type = RowStatus
_TmnxMcsDhcpsRowStatus_Object = MibTableColumn
tmnxMcsDhcpsRowStatus = _TmnxMcsDhcpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1, 3),
    _TmnxMcsDhcpsRowStatus_Type()
)
tmnxMcsDhcpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsRowStatus.setStatus("current")


class _TmnxMcsDhcpsPeerIpType_Type(InetAddressType):
    """Custom type tmnxMcsDhcpsPeerIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcsDhcpsPeerIpType_Type.__name__ = "InetAddressType"
_TmnxMcsDhcpsPeerIpType_Object = MibTableColumn
tmnxMcsDhcpsPeerIpType = _TmnxMcsDhcpsPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1, 4),
    _TmnxMcsDhcpsPeerIpType_Type()
)
tmnxMcsDhcpsPeerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPeerIpType.setStatus("current")


class _TmnxMcsDhcpsPeerIpAddr_Type(InetAddress):
    """Custom type tmnxMcsDhcpsPeerIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcsDhcpsPeerIpAddr_Type.__name__ = "InetAddress"
_TmnxMcsDhcpsPeerIpAddr_Object = MibTableColumn
tmnxMcsDhcpsPeerIpAddr = _TmnxMcsDhcpsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1, 5),
    _TmnxMcsDhcpsPeerIpAddr_Type()
)
tmnxMcsDhcpsPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPeerIpAddr.setStatus("current")
_TmnxMcsDhcpsSyncTag_Type = TNamedItem
_TmnxMcsDhcpsSyncTag_Object = MibTableColumn
tmnxMcsDhcpsSyncTag = _TmnxMcsDhcpsSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 2, 1, 6),
    _TmnxMcsDhcpsSyncTag_Type()
)
tmnxMcsDhcpsSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsSyncTag.setStatus("current")
_TmnxMcsDhcpsPoolTableLastChgd_Type = TimeStamp
_TmnxMcsDhcpsPoolTableLastChgd_Object = MibScalar
tmnxMcsDhcpsPoolTableLastChgd = _TmnxMcsDhcpsPoolTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 3),
    _TmnxMcsDhcpsPoolTableLastChgd_Type()
)
tmnxMcsDhcpsPoolTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolTableLastChgd.setStatus("current")
_TmnxMcsDhcpsPoolTable_Object = MibTable
tmnxMcsDhcpsPoolTable = _TmnxMcsDhcpsPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4)
)
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolTable.setStatus("current")
_TmnxMcsDhcpsPoolEntry_Object = MibTableRow
tmnxMcsDhcpsPoolEntry = _TmnxMcsDhcpsPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4, 1)
)
tmnxMcsDhcpsPoolEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsRtrID"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsServerName"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPoolName"),
)
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolEntry.setStatus("current")
_TmnxMcsDhcpsPoolName_Type = TNamedItem
_TmnxMcsDhcpsPoolName_Object = MibTableColumn
tmnxMcsDhcpsPoolName = _TmnxMcsDhcpsPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4, 1, 1),
    _TmnxMcsDhcpsPoolName_Type()
)
tmnxMcsDhcpsPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolName.setStatus("current")
_TmnxMcsDhcpsPoolRowStatus_Type = RowStatus
_TmnxMcsDhcpsPoolRowStatus_Object = MibTableColumn
tmnxMcsDhcpsPoolRowStatus = _TmnxMcsDhcpsPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4, 1, 2),
    _TmnxMcsDhcpsPoolRowStatus_Type()
)
tmnxMcsDhcpsPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolRowStatus.setStatus("current")


class _TmnxMcsDhcpsPoolPeerIpType_Type(InetAddressType):
    """Custom type tmnxMcsDhcpsPoolPeerIpType based on InetAddressType"""
    defaultValue = 0


_TmnxMcsDhcpsPoolPeerIpType_Type.__name__ = "InetAddressType"
_TmnxMcsDhcpsPoolPeerIpType_Object = MibTableColumn
tmnxMcsDhcpsPoolPeerIpType = _TmnxMcsDhcpsPoolPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4, 1, 3),
    _TmnxMcsDhcpsPoolPeerIpType_Type()
)
tmnxMcsDhcpsPoolPeerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolPeerIpType.setStatus("current")


class _TmnxMcsDhcpsPoolPeerIpAddr_Type(InetAddress):
    """Custom type tmnxMcsDhcpsPoolPeerIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxMcsDhcpsPoolPeerIpAddr_Type.__name__ = "InetAddress"
_TmnxMcsDhcpsPoolPeerIpAddr_Object = MibTableColumn
tmnxMcsDhcpsPoolPeerIpAddr = _TmnxMcsDhcpsPoolPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4, 1, 4),
    _TmnxMcsDhcpsPoolPeerIpAddr_Type()
)
tmnxMcsDhcpsPoolPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolPeerIpAddr.setStatus("current")
_TmnxMcsDhcpsPoolSyncTag_Type = TNamedItem
_TmnxMcsDhcpsPoolSyncTag_Object = MibTableColumn
tmnxMcsDhcpsPoolSyncTag = _TmnxMcsDhcpsPoolSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 25, 4, 1, 5),
    _TmnxMcsDhcpsPoolSyncTag_Type()
)
tmnxMcsDhcpsPoolSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsDhcpsPoolSyncTag.setStatus("current")
_TmnxSrrpAssoBfdIntfTblLastChgd_Type = TimeStamp
_TmnxSrrpAssoBfdIntfTblLastChgd_Object = MibScalar
tmnxSrrpAssoBfdIntfTblLastChgd = _TmnxSrrpAssoBfdIntfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 26),
    _TmnxSrrpAssoBfdIntfTblLastChgd_Type()
)
tmnxSrrpAssoBfdIntfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfTblLastChgd.setStatus("current")
_TmnxSrrpAssoBfdIntfTable_Object = MibTable
tmnxSrrpAssoBfdIntfTable = _TmnxSrrpAssoBfdIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27)
)
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfTable.setStatus("current")
_TmnxSrrpAssoBfdIntfEntry_Object = MibTableRow
tmnxSrrpAssoBfdIntfEntry = _TmnxSrrpAssoBfdIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1)
)
tmnxSrrpAssoBfdIntfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperID"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfSvcId"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfIfName"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfDestIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfDestIp"),
)
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfEntry.setStatus("current")
_TmnxSrrpAssoBfdIntfSvcId_Type = TmnxServId
_TmnxSrrpAssoBfdIntfSvcId_Object = MibTableColumn
tmnxSrrpAssoBfdIntfSvcId = _TmnxSrrpAssoBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 1),
    _TmnxSrrpAssoBfdIntfSvcId_Type()
)
tmnxSrrpAssoBfdIntfSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfSvcId.setStatus("current")
_TmnxSrrpAssoBfdIntfIfName_Type = TNamedItem
_TmnxSrrpAssoBfdIntfIfName_Object = MibTableColumn
tmnxSrrpAssoBfdIntfIfName = _TmnxSrrpAssoBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 2),
    _TmnxSrrpAssoBfdIntfIfName_Type()
)
tmnxSrrpAssoBfdIntfIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfIfName.setStatus("current")
_TmnxSrrpAssoBfdIntfDestIpType_Type = InetAddressType
_TmnxSrrpAssoBfdIntfDestIpType_Object = MibTableColumn
tmnxSrrpAssoBfdIntfDestIpType = _TmnxSrrpAssoBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 3),
    _TmnxSrrpAssoBfdIntfDestIpType_Type()
)
tmnxSrrpAssoBfdIntfDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfDestIpType.setStatus("current")


class _TmnxSrrpAssoBfdIntfDestIp_Type(InetAddress):
    """Custom type tmnxSrrpAssoBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxSrrpAssoBfdIntfDestIp_Type.__name__ = "InetAddress"
_TmnxSrrpAssoBfdIntfDestIp_Object = MibTableColumn
tmnxSrrpAssoBfdIntfDestIp = _TmnxSrrpAssoBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 4),
    _TmnxSrrpAssoBfdIntfDestIp_Type()
)
tmnxSrrpAssoBfdIntfDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfDestIp.setStatus("current")
_TmnxSrrpAssoBfdIntfRowStatus_Type = RowStatus
_TmnxSrrpAssoBfdIntfRowStatus_Object = MibTableColumn
tmnxSrrpAssoBfdIntfRowStatus = _TmnxSrrpAssoBfdIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 5),
    _TmnxSrrpAssoBfdIntfRowStatus_Type()
)
tmnxSrrpAssoBfdIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfRowStatus.setStatus("current")
_TmnxSrrpAssoBfdIntfLastChanged_Type = TimeStamp
_TmnxSrrpAssoBfdIntfLastChanged_Object = MibTableColumn
tmnxSrrpAssoBfdIntfLastChanged = _TmnxSrrpAssoBfdIntfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 6),
    _TmnxSrrpAssoBfdIntfLastChanged_Type()
)
tmnxSrrpAssoBfdIntfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfLastChanged.setStatus("current")
_TmnxSrrpAssoBfdIntfSrcIpType_Type = InetAddressType
_TmnxSrrpAssoBfdIntfSrcIpType_Object = MibTableColumn
tmnxSrrpAssoBfdIntfSrcIpType = _TmnxSrrpAssoBfdIntfSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 7),
    _TmnxSrrpAssoBfdIntfSrcIpType_Type()
)
tmnxSrrpAssoBfdIntfSrcIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfSrcIpType.setStatus("current")


class _TmnxSrrpAssoBfdIntfSrcIp_Type(InetAddress):
    """Custom type tmnxSrrpAssoBfdIntfSrcIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxSrrpAssoBfdIntfSrcIp_Type.__name__ = "InetAddress"
_TmnxSrrpAssoBfdIntfSrcIp_Object = MibTableColumn
tmnxSrrpAssoBfdIntfSrcIp = _TmnxSrrpAssoBfdIntfSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 8),
    _TmnxSrrpAssoBfdIntfSrcIp_Type()
)
tmnxSrrpAssoBfdIntfSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfSrcIp.setStatus("current")
_TmnxSrrpAssoBfdIntfSessOperState_Type = TmnxSrrpAssoBfdIntfSessOperState
_TmnxSrrpAssoBfdIntfSessOperState_Object = MibTableColumn
tmnxSrrpAssoBfdIntfSessOperState = _TmnxSrrpAssoBfdIntfSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 27, 1, 9),
    _TmnxSrrpAssoBfdIntfSessOperState_Type()
)
tmnxSrrpAssoBfdIntfSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSrrpAssoBfdIntfSessOperState.setStatus("current")
_TmnxMcRingDbTableLastChanged_Type = TimeStamp
_TmnxMcRingDbTableLastChanged_Object = MibScalar
tmnxMcRingDbTableLastChanged = _TmnxMcRingDbTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 28),
    _TmnxMcRingDbTableLastChanged_Type()
)
tmnxMcRingDbTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingDbTableLastChanged.setStatus("current")
_TmnxMcRingDbTableSize_Type = Unsigned32
_TmnxMcRingDbTableSize_Object = MibScalar
tmnxMcRingDbTableSize = _TmnxMcRingDbTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 29),
    _TmnxMcRingDbTableSize_Type()
)
tmnxMcRingDbTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingDbTableSize.setStatus("current")
_TmnxMcRingDbTable_Object = MibTable
tmnxMcRingDbTable = _TmnxMcRingDbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 30)
)
if mibBuilder.loadTexts:
    tmnxMcRingDbTable.setStatus("current")
_TmnxMcRingDbEntry_Object = MibTableRow
tmnxMcRingDbEntry = _TmnxMcRingDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 30, 1)
)
tmnxMcRingDbEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingDbStart"),
)
if mibBuilder.loadTexts:
    tmnxMcRingDbEntry.setStatus("current")
_TmnxMcRingDbStart_Type = TimeStamp
_TmnxMcRingDbStart_Object = MibTableColumn
tmnxMcRingDbStart = _TmnxMcRingDbStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 30, 1, 1),
    _TmnxMcRingDbStart_Type()
)
tmnxMcRingDbStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcRingDbStart.setStatus("current")
_TmnxMcRingDbTime_Type = TimeInterval
_TmnxMcRingDbTime_Object = MibTableColumn
tmnxMcRingDbTime = _TmnxMcRingDbTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 30, 1, 2),
    _TmnxMcRingDbTime_Type()
)
tmnxMcRingDbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingDbTime.setStatus("current")
_TmnxMcRingDbOperState_Type = TmnxMcRingInbCtrlOperState
_TmnxMcRingDbOperState_Object = MibTableColumn
tmnxMcRingDbOperState = _TmnxMcRingDbOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 30, 1, 3),
    _TmnxMcRingDbOperState_Type()
)
tmnxMcRingDbOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcRingDbOperState.setStatus("current")
_TmnxMcL3RingSrrpTableLastChanged_Type = TimeStamp
_TmnxMcL3RingSrrpTableLastChanged_Object = MibScalar
tmnxMcL3RingSrrpTableLastChanged = _TmnxMcL3RingSrrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 31),
    _TmnxMcL3RingSrrpTableLastChanged_Type()
)
tmnxMcL3RingSrrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcL3RingSrrpTableLastChanged.setStatus("current")
_TmnxMcL3RingSrrpTable_Object = MibTable
tmnxMcL3RingSrrpTable = _TmnxMcL3RingSrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 32)
)
if mibBuilder.loadTexts:
    tmnxMcL3RingSrrpTable.setStatus("current")
_TmnxMcL3RingSrrpEntry_Object = MibTableRow
tmnxMcL3RingSrrpEntry = _TmnxMcL3RingSrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 32, 1)
)
tmnxMcL3RingSrrpEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperID"),
)
if mibBuilder.loadTexts:
    tmnxMcL3RingSrrpEntry.setStatus("current")
_TmnxMcL3RingSrrpRowStatus_Type = RowStatus
_TmnxMcL3RingSrrpRowStatus_Object = MibTableColumn
tmnxMcL3RingSrrpRowStatus = _TmnxMcL3RingSrrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 32, 1, 1),
    _TmnxMcL3RingSrrpRowStatus_Type()
)
tmnxMcL3RingSrrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcL3RingSrrpRowStatus.setStatus("current")
_TmnxMcL3RingSrrpLastChanged_Type = TimeStamp
_TmnxMcL3RingSrrpLastChanged_Object = MibTableColumn
tmnxMcL3RingSrrpLastChanged = _TmnxMcL3RingSrrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 32, 1, 2),
    _TmnxMcL3RingSrrpLastChanged_Type()
)
tmnxMcL3RingSrrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcL3RingSrrpLastChanged.setStatus("current")
_TmnxMcPeerEPTableLastChanged_Type = TimeStamp
_TmnxMcPeerEPTableLastChanged_Object = MibScalar
tmnxMcPeerEPTableLastChanged = _TmnxMcPeerEPTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 33),
    _TmnxMcPeerEPTableLastChanged_Type()
)
tmnxMcPeerEPTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerEPTableLastChanged.setStatus("current")
_TmnxMcPeerEPTable_Object = MibTable
tmnxMcPeerEPTable = _TmnxMcPeerEPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34)
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPTable.setStatus("current")
_TmnxMcPeerEPEntry_Object = MibTableRow
tmnxMcPeerEPEntry = _TmnxMcPeerEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1)
)
tmnxMcPeerEPEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPEntry.setStatus("current")
_TmnxMcPeerEPRowStatus_Type = RowStatus
_TmnxMcPeerEPRowStatus_Object = MibTableColumn
tmnxMcPeerEPRowStatus = _TmnxMcPeerEPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 1),
    _TmnxMcPeerEPRowStatus_Type()
)
tmnxMcPeerEPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPRowStatus.setStatus("current")
_TmnxMcPeerEPLastChanged_Type = TimeStamp
_TmnxMcPeerEPLastChanged_Object = MibTableColumn
tmnxMcPeerEPLastChanged = _TmnxMcPeerEPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 2),
    _TmnxMcPeerEPLastChanged_Type()
)
tmnxMcPeerEPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerEPLastChanged.setStatus("current")


class _TmnxMcPeerEPAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcPeerEPAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcPeerEPAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcPeerEPAdminState_Object = MibTableColumn
tmnxMcPeerEPAdminState = _TmnxMcPeerEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 3),
    _TmnxMcPeerEPAdminState_Type()
)
tmnxMcPeerEPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPAdminState.setStatus("current")


class _TmnxMcPeerEPSysPriority_Type(Unsigned32):
    """Custom type tmnxMcPeerEPSysPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxMcPeerEPSysPriority_Type.__name__ = "Unsigned32"
_TmnxMcPeerEPSysPriority_Object = MibTableColumn
tmnxMcPeerEPSysPriority = _TmnxMcPeerEPSysPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 4),
    _TmnxMcPeerEPSysPriority_Type()
)
tmnxMcPeerEPSysPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPSysPriority.setStatus("current")


class _TmnxMcPeerEPKeepAliveIntvl_Type(Unsigned32):
    """Custom type tmnxMcPeerEPKeepAliveIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_TmnxMcPeerEPKeepAliveIntvl_Type.__name__ = "Unsigned32"
_TmnxMcPeerEPKeepAliveIntvl_Object = MibTableColumn
tmnxMcPeerEPKeepAliveIntvl = _TmnxMcPeerEPKeepAliveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 5),
    _TmnxMcPeerEPKeepAliveIntvl_Type()
)
tmnxMcPeerEPKeepAliveIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPKeepAliveIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerEPKeepAliveIntvl.setUnits("deci-seconds")


class _TmnxMcPeerEPHoldOnNbrFail_Type(Unsigned32):
    """Custom type tmnxMcPeerEPHoldOnNbrFail based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 25),
    )


_TmnxMcPeerEPHoldOnNbrFail_Type.__name__ = "Unsigned32"
_TmnxMcPeerEPHoldOnNbrFail_Object = MibTableColumn
tmnxMcPeerEPHoldOnNbrFail = _TmnxMcPeerEPHoldOnNbrFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 6),
    _TmnxMcPeerEPHoldOnNbrFail_Type()
)
tmnxMcPeerEPHoldOnNbrFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPHoldOnNbrFail.setStatus("current")


class _TmnxMcPeerEPBootTimer_Type(Unsigned32):
    """Custom type tmnxMcPeerEPBootTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_TmnxMcPeerEPBootTimer_Type.__name__ = "Unsigned32"
_TmnxMcPeerEPBootTimer_Object = MibTableColumn
tmnxMcPeerEPBootTimer = _TmnxMcPeerEPBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 7),
    _TmnxMcPeerEPBootTimer_Type()
)
tmnxMcPeerEPBootTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPBootTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerEPBootTimer.setUnits("seconds")


class _TmnxMcPeerEPPassiveMode_Type(TmnxEnabledDisabled):
    """Custom type tmnxMcPeerEPPassiveMode based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMcPeerEPPassiveMode_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMcPeerEPPassiveMode_Object = MibTableColumn
tmnxMcPeerEPPassiveMode = _TmnxMcPeerEPPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 8),
    _TmnxMcPeerEPPassiveMode_Type()
)
tmnxMcPeerEPPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPPassiveMode.setStatus("current")


class _TmnxMcPeerEPBfd_Type(TmnxEnabledDisabled):
    """Custom type tmnxMcPeerEPBfd based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMcPeerEPBfd_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMcPeerEPBfd_Object = MibTableColumn
tmnxMcPeerEPBfd = _TmnxMcPeerEPBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 9),
    _TmnxMcPeerEPBfd_Type()
)
tmnxMcPeerEPBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerEPBfd.setStatus("current")


class _TmnxMcPeerEPOperState_Type(Integer32):
    """Custom type tmnxMcPeerEPOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inService", 0),
          ("outOfService", 1))
    )


_TmnxMcPeerEPOperState_Type.__name__ = "Integer32"
_TmnxMcPeerEPOperState_Object = MibTableColumn
tmnxMcPeerEPOperState = _TmnxMcPeerEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 10),
    _TmnxMcPeerEPOperState_Type()
)
tmnxMcPeerEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerEPOperState.setStatus("current")
_TmnxMcPeerEPPeerLastStateChge_Type = TimeStamp
_TmnxMcPeerEPPeerLastStateChge_Object = MibTableColumn
tmnxMcPeerEPPeerLastStateChge = _TmnxMcPeerEPPeerLastStateChge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 11),
    _TmnxMcPeerEPPeerLastStateChge_Type()
)
tmnxMcPeerEPPeerLastStateChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerEPPeerLastStateChge.setStatus("current")
_TmnxMcPeerEPPassiveModeOper_Type = TruthValue
_TmnxMcPeerEPPassiveModeOper_Object = MibTableColumn
tmnxMcPeerEPPassiveModeOper = _TmnxMcPeerEPPassiveModeOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 12),
    _TmnxMcPeerEPPassiveModeOper_Type()
)
tmnxMcPeerEPPassiveModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerEPPassiveModeOper.setStatus("current")
_TmnxMcPeerEPRefCount_Type = Unsigned32
_TmnxMcPeerEPRefCount_Object = MibTableColumn
tmnxMcPeerEPRefCount = _TmnxMcPeerEPRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 34, 1, 13),
    _TmnxMcPeerEPRefCount_Type()
)
tmnxMcPeerEPRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerEPRefCount.setStatus("current")
_TmnxMcRedBgpMultiHomeObjs_ObjectIdentity = ObjectIdentity
tmnxMcRedBgpMultiHomeObjs = _TmnxMcRedBgpMultiHomeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 35)
)


class _TmnxMcRedBgpMultiHomeBootTimer_Type(Integer32):
    """Custom type tmnxMcRedBgpMultiHomeBootTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxMcRedBgpMultiHomeBootTimer_Type.__name__ = "Integer32"
_TmnxMcRedBgpMultiHomeBootTimer_Object = MibScalar
tmnxMcRedBgpMultiHomeBootTimer = _TmnxMcRedBgpMultiHomeBootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 35, 1),
    _TmnxMcRedBgpMultiHomeBootTimer_Type()
)
tmnxMcRedBgpMultiHomeBootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcRedBgpMultiHomeBootTimer.setStatus("current")


class _TmnxMcRedBgpMultiHomeSiteTimer_Type(Integer32):
    """Custom type tmnxMcRedBgpMultiHomeSiteTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMcRedBgpMultiHomeSiteTimer_Type.__name__ = "Integer32"
_TmnxMcRedBgpMultiHomeSiteTimer_Object = MibScalar
tmnxMcRedBgpMultiHomeSiteTimer = _TmnxMcRedBgpMultiHomeSiteTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 35, 2),
    _TmnxMcRedBgpMultiHomeSiteTimer_Type()
)
tmnxMcRedBgpMultiHomeSiteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcRedBgpMultiHomeSiteTimer.setStatus("current")


class _TmnxMcRedBgpMHSiteMinDnTimer_Type(Integer32):
    """Custom type tmnxMcRedBgpMHSiteMinDnTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMcRedBgpMHSiteMinDnTimer_Type.__name__ = "Integer32"
_TmnxMcRedBgpMHSiteMinDnTimer_Object = MibScalar
tmnxMcRedBgpMHSiteMinDnTimer = _TmnxMcRedBgpMHSiteMinDnTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 35, 3),
    _TmnxMcRedBgpMHSiteMinDnTimer_Type()
)
tmnxMcRedBgpMHSiteMinDnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMcRedBgpMHSiteMinDnTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcRedBgpMHSiteMinDnTimer.setUnits("seconds")
_TmnxMcTlsSapTableLastChanged_Type = TimeStamp
_TmnxMcTlsSapTableLastChanged_Object = MibScalar
tmnxMcTlsSapTableLastChanged = _TmnxMcTlsSapTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 36),
    _TmnxMcTlsSapTableLastChanged_Type()
)
tmnxMcTlsSapTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcTlsSapTableLastChanged.setStatus("current")
_TmnxMcTlsSapTable_Object = MibTable
tmnxMcTlsSapTable = _TmnxMcTlsSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 37)
)
if mibBuilder.loadTexts:
    tmnxMcTlsSapTable.setStatus("current")
_TmnxMcTlsSapEntry_Object = MibTableRow
tmnxMcTlsSapEntry = _TmnxMcTlsSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 37, 1)
)
tmnxMcTlsSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxMcTlsSapEntry.setStatus("current")
_TmnxMcTlsSapRowStatus_Type = RowStatus
_TmnxMcTlsSapRowStatus_Object = MibTableColumn
tmnxMcTlsSapRowStatus = _TmnxMcTlsSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 37, 1, 1),
    _TmnxMcTlsSapRowStatus_Type()
)
tmnxMcTlsSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcTlsSapRowStatus.setStatus("current")
_TmnxMcTlsSapLastChanged_Type = TimeStamp
_TmnxMcTlsSapLastChanged_Object = MibTableColumn
tmnxMcTlsSapLastChanged = _TmnxMcTlsSapLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 37, 1, 2),
    _TmnxMcTlsSapLastChanged_Type()
)
tmnxMcTlsSapLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcTlsSapLastChanged.setStatus("current")


class _TmnxMcTlsSapRingNodeName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMcTlsSapRingNodeName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMcTlsSapRingNodeName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMcTlsSapRingNodeName_Object = MibTableColumn
tmnxMcTlsSapRingNodeName = _TmnxMcTlsSapRingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 37, 1, 3),
    _TmnxMcTlsSapRingNodeName_Type()
)
tmnxMcTlsSapRingNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcTlsSapRingNodeName.setStatus("current")
_TMcPeerIPsecTblLastChgd_Type = TimeStamp
_TMcPeerIPsecTblLastChgd_Object = MibScalar
tMcPeerIPsecTblLastChgd = _TMcPeerIPsecTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 38),
    _TMcPeerIPsecTblLastChgd_Type()
)
tMcPeerIPsecTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTblLastChgd.setStatus("current")
_TMcPeerIPsecTable_Object = MibTable
tMcPeerIPsecTable = _TMcPeerIPsecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39)
)
if mibBuilder.loadTexts:
    tMcPeerIPsecTable.setStatus("current")
_TMcPeerIPsecEntry_Object = MibTableRow
tMcPeerIPsecEntry = _TMcPeerIPsecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1)
)
tMcPeerIPsecEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tMcPeerIPsecEntry.setStatus("current")
_TMcPeerIPsecRowStatus_Type = RowStatus
_TMcPeerIPsecRowStatus_Object = MibTableColumn
tMcPeerIPsecRowStatus = _TMcPeerIPsecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 1),
    _TMcPeerIPsecRowStatus_Type()
)
tMcPeerIPsecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecRowStatus.setStatus("current")
_TMcPeerIPsecLastChgd_Type = TimeStamp
_TMcPeerIPsecLastChgd_Object = MibTableColumn
tMcPeerIPsecLastChgd = _TMcPeerIPsecLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 2),
    _TMcPeerIPsecLastChgd_Type()
)
tMcPeerIPsecLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecLastChgd.setStatus("current")


class _TMcPeerIPsecKeepAliveIntvl_Type(Unsigned32):
    """Custom type tMcPeerIPsecKeepAliveIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_TMcPeerIPsecKeepAliveIntvl_Type.__name__ = "Unsigned32"
_TMcPeerIPsecKeepAliveIntvl_Object = MibTableColumn
tMcPeerIPsecKeepAliveIntvl = _TMcPeerIPsecKeepAliveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 3),
    _TMcPeerIPsecKeepAliveIntvl_Type()
)
tMcPeerIPsecKeepAliveIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecKeepAliveIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tMcPeerIPsecKeepAliveIntvl.setUnits("deci-seconds")


class _TMcPeerIPsecHoldOnNgbrFail_Type(Unsigned32):
    """Custom type tMcPeerIPsecHoldOnNgbrFail based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 25),
    )


_TMcPeerIPsecHoldOnNgbrFail_Type.__name__ = "Unsigned32"
_TMcPeerIPsecHoldOnNgbrFail_Object = MibTableColumn
tMcPeerIPsecHoldOnNgbrFail = _TMcPeerIPsecHoldOnNgbrFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 4),
    _TMcPeerIPsecHoldOnNgbrFail_Type()
)
tMcPeerIPsecHoldOnNgbrFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecHoldOnNgbrFail.setStatus("current")


class _TMcPeerIPsecBfdEnableSvc_Type(TmnxServId):
    """Custom type tMcPeerIPsecBfdEnableSvc based on TmnxServId"""
    defaultValue = 0


_TMcPeerIPsecBfdEnableSvc_Type.__name__ = "TmnxServId"
_TMcPeerIPsecBfdEnableSvc_Object = MibTableColumn
tMcPeerIPsecBfdEnableSvc = _TMcPeerIPsecBfdEnableSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 5),
    _TMcPeerIPsecBfdEnableSvc_Type()
)
tMcPeerIPsecBfdEnableSvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecBfdEnableSvc.setStatus("current")


class _TMcPeerIPsecBfdIntfIfName_Type(TNamedItemOrEmpty):
    """Custom type tMcPeerIPsecBfdIntfIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TMcPeerIPsecBfdIntfIfName_Type.__name__ = "TNamedItemOrEmpty"
_TMcPeerIPsecBfdIntfIfName_Object = MibTableColumn
tMcPeerIPsecBfdIntfIfName = _TMcPeerIPsecBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 6),
    _TMcPeerIPsecBfdIntfIfName_Type()
)
tMcPeerIPsecBfdIntfIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecBfdIntfIfName.setStatus("current")


class _TMcPeerIPsecBfdIntfDestIpType_Type(InetAddressType):
    """Custom type tMcPeerIPsecBfdIntfDestIpType based on InetAddressType"""
    defaultValue = 0


_TMcPeerIPsecBfdIntfDestIpType_Type.__name__ = "InetAddressType"
_TMcPeerIPsecBfdIntfDestIpType_Object = MibTableColumn
tMcPeerIPsecBfdIntfDestIpType = _TMcPeerIPsecBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 7),
    _TMcPeerIPsecBfdIntfDestIpType_Type()
)
tMcPeerIPsecBfdIntfDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecBfdIntfDestIpType.setStatus("current")


class _TMcPeerIPsecBfdIntfDestIp_Type(InetAddress):
    """Custom type tMcPeerIPsecBfdIntfDestIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TMcPeerIPsecBfdIntfDestIp_Type.__name__ = "InetAddress"
_TMcPeerIPsecBfdIntfDestIp_Object = MibTableColumn
tMcPeerIPsecBfdIntfDestIp = _TMcPeerIPsecBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 8),
    _TMcPeerIPsecBfdIntfDestIp_Type()
)
tMcPeerIPsecBfdIntfDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecBfdIntfDestIp.setStatus("current")


class _TMcPeerIPsecDiscoveryIntvl_Type(Unsigned32):
    """Custom type tMcPeerIPsecDiscoveryIntvl based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TMcPeerIPsecDiscoveryIntvl_Type.__name__ = "Unsigned32"
_TMcPeerIPsecDiscoveryIntvl_Object = MibTableColumn
tMcPeerIPsecDiscoveryIntvl = _TMcPeerIPsecDiscoveryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 9),
    _TMcPeerIPsecDiscoveryIntvl_Type()
)
tMcPeerIPsecDiscoveryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecDiscoveryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tMcPeerIPsecDiscoveryIntvl.setUnits("seconds")


class _TMcPeerIPsecDiscoveryIntvlBoot_Type(Unsigned32):
    """Custom type tMcPeerIPsecDiscoveryIntvlBoot based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TMcPeerIPsecDiscoveryIntvlBoot_Type.__name__ = "Unsigned32"
_TMcPeerIPsecDiscoveryIntvlBoot_Object = MibTableColumn
tMcPeerIPsecDiscoveryIntvlBoot = _TMcPeerIPsecDiscoveryIntvlBoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 10),
    _TMcPeerIPsecDiscoveryIntvlBoot_Type()
)
tMcPeerIPsecDiscoveryIntvlBoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecDiscoveryIntvlBoot.setStatus("current")
if mibBuilder.loadTexts:
    tMcPeerIPsecDiscoveryIntvlBoot.setUnits("seconds")


class _TMcPeerIPsecBfdEnable_Type(TruthValue):
    """Custom type tMcPeerIPsecBfdEnable based on TruthValue"""
    defaultValue = 2


_TMcPeerIPsecBfdEnable_Type.__name__ = "TruthValue"
_TMcPeerIPsecBfdEnable_Object = MibTableColumn
tMcPeerIPsecBfdEnable = _TMcPeerIPsecBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 39, 1, 11),
    _TMcPeerIPsecBfdEnable_Type()
)
tMcPeerIPsecBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecBfdEnable.setStatus("current")
_TMcPeerIPsecTnlGrpTblLastChgd_Type = TimeStamp
_TMcPeerIPsecTnlGrpTblLastChgd_Object = MibScalar
tMcPeerIPsecTnlGrpTblLastChgd = _TMcPeerIPsecTnlGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 40),
    _TMcPeerIPsecTnlGrpTblLastChgd_Type()
)
tMcPeerIPsecTnlGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpTblLastChgd.setStatus("current")
_TMcPeerIPsecTnlGrpTable_Object = MibTable
tMcPeerIPsecTnlGrpTable = _TMcPeerIPsecTnlGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41)
)
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpTable.setStatus("current")
_TMcPeerIPsecTnlGrpEntry_Object = MibTableRow
tMcPeerIPsecTnlGrpEntry = _TMcPeerIPsecTnlGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1)
)
tMcPeerIPsecTnlGrpEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpId"),
)
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpEntry.setStatus("current")
_TMcPeerIPsecTnlGrpId_Type = TmnxTunnelGroupId
_TMcPeerIPsecTnlGrpId_Object = MibTableColumn
tMcPeerIPsecTnlGrpId = _TMcPeerIPsecTnlGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 1),
    _TMcPeerIPsecTnlGrpId_Type()
)
tMcPeerIPsecTnlGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpId.setStatus("current")
_TMcPeerIPsecTnlGrpRowStatus_Type = RowStatus
_TMcPeerIPsecTnlGrpRowStatus_Object = MibTableColumn
tMcPeerIPsecTnlGrpRowStatus = _TMcPeerIPsecTnlGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 2),
    _TMcPeerIPsecTnlGrpRowStatus_Type()
)
tMcPeerIPsecTnlGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpRowStatus.setStatus("current")
_TMcPeerIPsecTnlGrpLastChgd_Type = TimeStamp
_TMcPeerIPsecTnlGrpLastChgd_Object = MibTableColumn
tMcPeerIPsecTnlGrpLastChgd = _TMcPeerIPsecTnlGrpLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 3),
    _TMcPeerIPsecTnlGrpLastChgd_Type()
)
tMcPeerIPsecTnlGrpLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpLastChgd.setStatus("current")


class _TMcPeerIPsecTnlGrpPeerGrpId_Type(TmnxTunnelGroupIdOrZero):
    """Custom type tMcPeerIPsecTnlGrpPeerGrpId based on TmnxTunnelGroupIdOrZero"""
    defaultValue = 0


_TMcPeerIPsecTnlGrpPeerGrpId_Type.__name__ = "TmnxTunnelGroupIdOrZero"
_TMcPeerIPsecTnlGrpPeerGrpId_Object = MibTableColumn
tMcPeerIPsecTnlGrpPeerGrpId = _TMcPeerIPsecTnlGrpPeerGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 4),
    _TMcPeerIPsecTnlGrpPeerGrpId_Type()
)
tMcPeerIPsecTnlGrpPeerGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpPeerGrpId.setStatus("current")


class _TMcPeerIPsecTnlGrpPriority_Type(Unsigned32):
    """Custom type tMcPeerIPsecTnlGrpPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TMcPeerIPsecTnlGrpPriority_Type.__name__ = "Unsigned32"
_TMcPeerIPsecTnlGrpPriority_Object = MibTableColumn
tMcPeerIPsecTnlGrpPriority = _TMcPeerIPsecTnlGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 5),
    _TMcPeerIPsecTnlGrpPriority_Type()
)
tMcPeerIPsecTnlGrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpPriority.setStatus("current")


class _TMcPeerIPsecTnlGrpPreempt_Type(TruthValue):
    """Custom type tMcPeerIPsecTnlGrpPreempt based on TruthValue"""
    defaultValue = 2


_TMcPeerIPsecTnlGrpPreempt_Type.__name__ = "TruthValue"
_TMcPeerIPsecTnlGrpPreempt_Object = MibTableColumn
tMcPeerIPsecTnlGrpPreempt = _TMcPeerIPsecTnlGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 6),
    _TMcPeerIPsecTnlGrpPreempt_Type()
)
tMcPeerIPsecTnlGrpPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpPreempt.setStatus("current")


class _TMcPeerIPsecTnlGrpAdminState_Type(TmnxAdminState):
    """Custom type tMcPeerIPsecTnlGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TMcPeerIPsecTnlGrpAdminState_Type.__name__ = "TmnxAdminState"
_TMcPeerIPsecTnlGrpAdminState_Object = MibTableColumn
tMcPeerIPsecTnlGrpAdminState = _TMcPeerIPsecTnlGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 7),
    _TMcPeerIPsecTnlGrpAdminState_Type()
)
tMcPeerIPsecTnlGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpAdminState.setStatus("current")
_TMcPeerIPsecTnlGrpOperState_Type = TmnxOperState
_TMcPeerIPsecTnlGrpOperState_Object = MibTableColumn
tMcPeerIPsecTnlGrpOperState = _TMcPeerIPsecTnlGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 8),
    _TMcPeerIPsecTnlGrpOperState_Type()
)
tMcPeerIPsecTnlGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpOperState.setStatus("current")
_TMcPeerIPsecTnlGrpMasterState_Type = TMcPeerIPsecTnlGrpMasterState
_TMcPeerIPsecTnlGrpMasterState_Object = MibTableColumn
tMcPeerIPsecTnlGrpMasterState = _TMcPeerIPsecTnlGrpMasterState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 9),
    _TMcPeerIPsecTnlGrpMasterState_Type()
)
tMcPeerIPsecTnlGrpMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpMasterState.setStatus("current")


class _TMcPeerIPsecTnlGrpReason_Type(DisplayString):
    """Custom type tMcPeerIPsecTnlGrpReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TMcPeerIPsecTnlGrpReason_Type.__name__ = "DisplayString"
_TMcPeerIPsecTnlGrpReason_Object = MibTableColumn
tMcPeerIPsecTnlGrpReason = _TMcPeerIPsecTnlGrpReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 10),
    _TMcPeerIPsecTnlGrpReason_Type()
)
tMcPeerIPsecTnlGrpReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpReason.setStatus("current")


class _TMcPeerIPsecTnlGrpForceSwitch_Type(TmnxActionType):
    """Custom type tMcPeerIPsecTnlGrpForceSwitch based on TmnxActionType"""
    defaultValue = 2


_TMcPeerIPsecTnlGrpForceSwitch_Type.__name__ = "TmnxActionType"
_TMcPeerIPsecTnlGrpForceSwitch_Object = MibTableColumn
tMcPeerIPsecTnlGrpForceSwitch = _TMcPeerIPsecTnlGrpForceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 11),
    _TMcPeerIPsecTnlGrpForceSwitch_Type()
)
tMcPeerIPsecTnlGrpForceSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpForceSwitch.setStatus("current")
_TMcPeerIPsecTnlGrpProtectStatus_Type = TMcPeerIPsecTnlGrpProtectionStatus
_TMcPeerIPsecTnlGrpProtectStatus_Object = MibTableColumn
tMcPeerIPsecTnlGrpProtectStatus = _TMcPeerIPsecTnlGrpProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 12),
    _TMcPeerIPsecTnlGrpProtectStatus_Type()
)
tMcPeerIPsecTnlGrpProtectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpProtectStatus.setStatus("current")


class _TMcPeerIPsecTnlGrpForceSwitchTo_Type(Integer32):
    """Custom type tMcPeerIPsecTnlGrpForceSwitchTo based on Integer32"""
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
        *(("notSpecified", 0),
          ("toMaster", 1),
          ("toStandby", 2))
    )


_TMcPeerIPsecTnlGrpForceSwitchTo_Type.__name__ = "Integer32"
_TMcPeerIPsecTnlGrpForceSwitchTo_Object = MibTableColumn
tMcPeerIPsecTnlGrpForceSwitchTo = _TMcPeerIPsecTnlGrpForceSwitchTo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 41, 1, 13),
    _TMcPeerIPsecTnlGrpForceSwitchTo_Type()
)
tMcPeerIPsecTnlGrpForceSwitchTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpForceSwitchTo.setStatus("current")
_TmnxMcsTnlGrpTblLastChgd_Type = TimeStamp
_TmnxMcsTnlGrpTblLastChgd_Object = MibScalar
tmnxMcsTnlGrpTblLastChgd = _TmnxMcsTnlGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 42),
    _TmnxMcsTnlGrpTblLastChgd_Type()
)
tmnxMcsTnlGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsTnlGrpTblLastChgd.setStatus("current")
_TmnxMcsTnlGrpTable_Object = MibTable
tmnxMcsTnlGrpTable = _TmnxMcsTnlGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 43)
)
if mibBuilder.loadTexts:
    tmnxMcsTnlGrpTable.setStatus("current")
_TmnxMcsTnlGrpEntry_Object = MibTableRow
tmnxMcsTnlGrpEntry = _TmnxMcsTnlGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 43, 1)
)
tmnxMcsTnlGrpEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpId"),
)
if mibBuilder.loadTexts:
    tmnxMcsTnlGrpEntry.setStatus("current")
_TmnxMcsTnlGrpRowStatus_Type = RowStatus
_TmnxMcsTnlGrpRowStatus_Object = MibTableColumn
tmnxMcsTnlGrpRowStatus = _TmnxMcsTnlGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 43, 1, 1),
    _TmnxMcsTnlGrpRowStatus_Type()
)
tmnxMcsTnlGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsTnlGrpRowStatus.setStatus("current")
_TmnxMcsTnlGrpSyncTag_Type = TNamedItem
_TmnxMcsTnlGrpSyncTag_Object = MibTableColumn
tmnxMcsTnlGrpSyncTag = _TmnxMcsTnlGrpSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 43, 1, 2),
    _TmnxMcsTnlGrpSyncTag_Type()
)
tmnxMcsTnlGrpSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsTnlGrpSyncTag.setStatus("current")
_TMcPeerTnlGrpStatTable_Object = MibTable
tMcPeerTnlGrpStatTable = _TMcPeerTnlGrpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44)
)
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatTable.setStatus("current")
_TMcPeerTnlGrpStatEntry_Object = MibTableRow
tMcPeerTnlGrpStatEntry = _TMcPeerTnlGrpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1)
)
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatEntry.setStatus("current")
_TMcPeerTnlGrpStatDynInstalled_Type = Unsigned32
_TMcPeerTnlGrpStatDynInstalled_Object = MibTableColumn
tMcPeerTnlGrpStatDynInstalled = _TMcPeerTnlGrpStatDynInstalled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 1),
    _TMcPeerTnlGrpStatDynInstalled_Type()
)
tMcPeerTnlGrpStatDynInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatDynInstalled.setStatus("current")
_TMcPeerTnlGrpStatDynInstalling_Type = Unsigned32
_TMcPeerTnlGrpStatDynInstalling_Object = MibTableColumn
tMcPeerTnlGrpStatDynInstalling = _TMcPeerTnlGrpStatDynInstalling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 2),
    _TMcPeerTnlGrpStatDynInstalling_Type()
)
tMcPeerTnlGrpStatDynInstalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatDynInstalling.setStatus("current")
_TMcPeerTnlGrpStatDynAwaitConf_Type = Unsigned32
_TMcPeerTnlGrpStatDynAwaitConf_Object = MibTableColumn
tMcPeerTnlGrpStatDynAwaitConf = _TMcPeerTnlGrpStatDynAwaitConf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 3),
    _TMcPeerTnlGrpStatDynAwaitConf_Type()
)
tMcPeerTnlGrpStatDynAwaitConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatDynAwaitConf.setStatus("current")
_TMcPeerTnlGrpStatDynFailed_Type = Unsigned32
_TMcPeerTnlGrpStatDynFailed_Object = MibTableColumn
tMcPeerTnlGrpStatDynFailed = _TMcPeerTnlGrpStatDynFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 4),
    _TMcPeerTnlGrpStatDynFailed_Type()
)
tMcPeerTnlGrpStatDynFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatDynFailed.setStatus("current")
_TMcPeerTnlGrpStatInstalled_Type = Unsigned32
_TMcPeerTnlGrpStatInstalled_Object = MibTableColumn
tMcPeerTnlGrpStatInstalled = _TMcPeerTnlGrpStatInstalled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 5),
    _TMcPeerTnlGrpStatInstalled_Type()
)
tMcPeerTnlGrpStatInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatInstalled.setStatus("current")
_TMcPeerTnlGrpStatInstalling_Type = Unsigned32
_TMcPeerTnlGrpStatInstalling_Object = MibTableColumn
tMcPeerTnlGrpStatInstalling = _TMcPeerTnlGrpStatInstalling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 6),
    _TMcPeerTnlGrpStatInstalling_Type()
)
tMcPeerTnlGrpStatInstalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatInstalling.setStatus("current")
_TMcPeerTnlGrpStatAwaitConf_Type = Unsigned32
_TMcPeerTnlGrpStatAwaitConf_Object = MibTableColumn
tMcPeerTnlGrpStatAwaitConf = _TMcPeerTnlGrpStatAwaitConf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 7),
    _TMcPeerTnlGrpStatAwaitConf_Type()
)
tMcPeerTnlGrpStatAwaitConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatAwaitConf.setStatus("current")
_TMcPeerTnlGrpStatFailed_Type = Unsigned32
_TMcPeerTnlGrpStatFailed_Object = MibTableColumn
tMcPeerTnlGrpStatFailed = _TMcPeerTnlGrpStatFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 44, 1, 8),
    _TMcPeerTnlGrpStatFailed_Type()
)
tMcPeerTnlGrpStatFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcPeerTnlGrpStatFailed.setStatus("current")
_TmnxMcOmcrObjs_ObjectIdentity = ObjectIdentity
tmnxMcOmcrObjs = _TmnxMcOmcrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45)
)
_TmnxMcOmcrStatTable_Object = MibTable
tmnxMcOmcrStatTable = _TmnxMcOmcrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2)
)
if mibBuilder.loadTexts:
    tmnxMcOmcrStatTable.setStatus("current")
_TmnxMcOmcrStatEntry_Object = MibTableRow
tmnxMcOmcrStatEntry = _TmnxMcOmcrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1)
)
tmnxMcOmcrStatEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatClientApplication"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatAccessProtection"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatIndex"),
)
if mibBuilder.loadTexts:
    tmnxMcOmcrStatEntry.setStatus("current")
_TmnxMcOmcrStatClientApplication_Type = TmnxMcsClientApp
_TmnxMcOmcrStatClientApplication_Object = MibTableColumn
tmnxMcOmcrStatClientApplication = _TmnxMcOmcrStatClientApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1, 1),
    _TmnxMcOmcrStatClientApplication_Type()
)
tmnxMcOmcrStatClientApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcOmcrStatClientApplication.setStatus("current")
_TmnxMcOmcrStatAccessProtection_Type = TmnxMcsAccessProtection
_TmnxMcOmcrStatAccessProtection_Object = MibTableColumn
tmnxMcOmcrStatAccessProtection = _TmnxMcOmcrStatAccessProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1, 2),
    _TmnxMcOmcrStatAccessProtection_Type()
)
tmnxMcOmcrStatAccessProtection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcOmcrStatAccessProtection.setStatus("current")
_TmnxMcOmcrStatIndex_Type = Unsigned32
_TmnxMcOmcrStatIndex_Object = MibTableColumn
tmnxMcOmcrStatIndex = _TmnxMcOmcrStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1, 3),
    _TmnxMcOmcrStatIndex_Type()
)
tmnxMcOmcrStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcOmcrStatIndex.setStatus("current")


class _TmnxMcOmcrStatFailed_Type(Integer32):
    """Custom type tmnxMcOmcrStatFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAct", 0),
          ("yes", 1),
          ("no", 2))
    )


_TmnxMcOmcrStatFailed_Type.__name__ = "Integer32"
_TmnxMcOmcrStatFailed_Object = MibTableColumn
tmnxMcOmcrStatFailed = _TmnxMcOmcrStatFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1, 4),
    _TmnxMcOmcrStatFailed_Type()
)
tmnxMcOmcrStatFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcOmcrStatFailed.setStatus("current")


class _TmnxMcOmcrStatFailure_Type(DisplayString):
    """Custom type tmnxMcOmcrStatFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxMcOmcrStatFailure_Type.__name__ = "DisplayString"
_TmnxMcOmcrStatFailure_Object = MibTableColumn
tmnxMcOmcrStatFailure = _TmnxMcOmcrStatFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1, 5),
    _TmnxMcOmcrStatFailure_Type()
)
tmnxMcOmcrStatFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcOmcrStatFailure.setStatus("current")
_TmnxMcOmcrStatNumFailedEntries_Type = Gauge32
_TmnxMcOmcrStatNumFailedEntries_Object = MibTableColumn
tmnxMcOmcrStatNumFailedEntries = _TmnxMcOmcrStatNumFailedEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 45, 2, 1, 6),
    _TmnxMcOmcrStatNumFailedEntries_Type()
)
tmnxMcOmcrStatNumFailedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcOmcrStatNumFailedEntries.setStatus("current")
_TmnxMcsPythonObjs_ObjectIdentity = ObjectIdentity
tmnxMcsPythonObjs = _TmnxMcsPythonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47)
)
_TmnxMcsPyPlcyTableLastChgd_Type = TimeStamp
_TmnxMcsPyPlcyTableLastChgd_Object = MibScalar
tmnxMcsPyPlcyTableLastChgd = _TmnxMcsPyPlcyTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 1),
    _TmnxMcsPyPlcyTableLastChgd_Type()
)
tmnxMcsPyPlcyTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyTableLastChgd.setStatus("current")
_TmnxMcsPyPlcyTable_Object = MibTable
tmnxMcsPyPlcyTable = _TmnxMcsPyPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2)
)
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyTable.setStatus("current")
_TmnxMcsPyPlcyEntry_Object = MibTableRow
tmnxMcsPyPlcyEntry = _TmnxMcsPyPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2, 1)
)
tmnxMcsPyPlcyEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyEntry.setStatus("current")
_TmnxMcsPyPlcyName_Type = TNamedItem
_TmnxMcsPyPlcyName_Object = MibTableColumn
tmnxMcsPyPlcyName = _TmnxMcsPyPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2, 1, 1),
    _TmnxMcsPyPlcyName_Type()
)
tmnxMcsPyPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyName.setStatus("current")
_TmnxMcsPyPlcyRowStatus_Type = RowStatus
_TmnxMcsPyPlcyRowStatus_Object = MibTableColumn
tmnxMcsPyPlcyRowStatus = _TmnxMcsPyPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2, 1, 2),
    _TmnxMcsPyPlcyRowStatus_Type()
)
tmnxMcsPyPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyRowStatus.setStatus("current")


class _TmnxMcsPyPlcyPeerIpAddrType_Type(InetAddressType):
    """Custom type tmnxMcsPyPlcyPeerIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMcsPyPlcyPeerIpAddrType_Type.__name__ = "InetAddressType"
_TmnxMcsPyPlcyPeerIpAddrType_Object = MibTableColumn
tmnxMcsPyPlcyPeerIpAddrType = _TmnxMcsPyPlcyPeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2, 1, 3),
    _TmnxMcsPyPlcyPeerIpAddrType_Type()
)
tmnxMcsPyPlcyPeerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyPeerIpAddrType.setStatus("current")


class _TmnxMcsPyPlcyPeerIpAddr_Type(InetAddress):
    """Custom type tmnxMcsPyPlcyPeerIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMcsPyPlcyPeerIpAddr_Type.__name__ = "InetAddress"
_TmnxMcsPyPlcyPeerIpAddr_Object = MibTableColumn
tmnxMcsPyPlcyPeerIpAddr = _TmnxMcsPyPlcyPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2, 1, 4),
    _TmnxMcsPyPlcyPeerIpAddr_Type()
)
tmnxMcsPyPlcyPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyPeerIpAddr.setStatus("current")
_TmnxMcsPyPlcyMcsSyncTag_Type = TNamedItem
_TmnxMcsPyPlcyMcsSyncTag_Object = MibTableColumn
tmnxMcsPyPlcyMcsSyncTag = _TmnxMcsPyPlcyMcsSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 47, 2, 1, 5),
    _TmnxMcsPyPlcyMcsSyncTag_Type()
)
tmnxMcsPyPlcyMcsSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyMcsSyncTag.setStatus("current")
_TmnxMcsPyPlcyTableLastChanged_Type = TimeStamp
_TmnxMcsPyPlcyTableLastChanged_Object = MibScalar
tmnxMcsPyPlcyTableLastChanged = _TmnxMcsPyPlcyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 1, 48),
    _TmnxMcsPyPlcyTableLastChanged_Type()
)
tmnxMcsPyPlcyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcsPyPlcyTableLastChanged.setStatus("current")
_TmnxMcRedundancyStatsObjs_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyStatsObjs = _TmnxMcRedundancyStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2)
)
_TmnxMcLagStatsPktsRx_Type = Counter32
_TmnxMcLagStatsPktsRx_Object = MibScalar
tmnxMcLagStatsPktsRx = _TmnxMcLagStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 1),
    _TmnxMcLagStatsPktsRx_Type()
)
tmnxMcLagStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsRx.setStatus("current")
_TmnxMcLagStatsPktsRxKeepalive_Type = Counter32
_TmnxMcLagStatsPktsRxKeepalive_Object = MibScalar
tmnxMcLagStatsPktsRxKeepalive = _TmnxMcLagStatsPktsRxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 2),
    _TmnxMcLagStatsPktsRxKeepalive_Type()
)
tmnxMcLagStatsPktsRxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsRxKeepalive.setStatus("current")
_TmnxMcLagStatsPktsRxConfig_Type = Counter32
_TmnxMcLagStatsPktsRxConfig_Object = MibScalar
tmnxMcLagStatsPktsRxConfig = _TmnxMcLagStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 3),
    _TmnxMcLagStatsPktsRxConfig_Type()
)
tmnxMcLagStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsRxConfig.setStatus("current")
_TmnxMcLagStatsPktsRxPeerConfig_Type = Counter32
_TmnxMcLagStatsPktsRxPeerConfig_Object = MibScalar
tmnxMcLagStatsPktsRxPeerConfig = _TmnxMcLagStatsPktsRxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 4),
    _TmnxMcLagStatsPktsRxPeerConfig_Type()
)
tmnxMcLagStatsPktsRxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsRxPeerConfig.setStatus("current")
_TmnxMcLagStatsPktsRxState_Type = Counter32
_TmnxMcLagStatsPktsRxState_Object = MibScalar
tmnxMcLagStatsPktsRxState = _TmnxMcLagStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 5),
    _TmnxMcLagStatsPktsRxState_Type()
)
tmnxMcLagStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsRxState.setStatus("current")
_TmnxMcLagStatsDropPktKpaliveTask_Type = Counter32
_TmnxMcLagStatsDropPktKpaliveTask_Object = MibScalar
tmnxMcLagStatsDropPktKpaliveTask = _TmnxMcLagStatsDropPktKpaliveTask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 6),
    _TmnxMcLagStatsDropPktKpaliveTask_Type()
)
tmnxMcLagStatsDropPktKpaliveTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropPktKpaliveTask.setStatus("current")
_TmnxMcLagStatsDropPktTooShort_Type = Counter32
_TmnxMcLagStatsDropPktTooShort_Object = MibScalar
tmnxMcLagStatsDropPktTooShort = _TmnxMcLagStatsDropPktTooShort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 7),
    _TmnxMcLagStatsDropPktTooShort_Type()
)
tmnxMcLagStatsDropPktTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropPktTooShort.setStatus("current")
_TmnxMcLagStatsDropPktVerifyFaild_Type = Counter32
_TmnxMcLagStatsDropPktVerifyFaild_Object = MibScalar
tmnxMcLagStatsDropPktVerifyFaild = _TmnxMcLagStatsDropPktVerifyFaild_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 8),
    _TmnxMcLagStatsDropPktVerifyFaild_Type()
)
tmnxMcLagStatsDropPktVerifyFaild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropPktVerifyFaild.setStatus("current")
_TmnxMcLagStatsDropTlvInvalidSize_Type = Counter32
_TmnxMcLagStatsDropTlvInvalidSize_Object = MibScalar
tmnxMcLagStatsDropTlvInvalidSize = _TmnxMcLagStatsDropTlvInvalidSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 9),
    _TmnxMcLagStatsDropTlvInvalidSize_Type()
)
tmnxMcLagStatsDropTlvInvalidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropTlvInvalidSize.setStatus("current")
_TmnxMcLagStatsDropOutOfSeq_Type = Counter32
_TmnxMcLagStatsDropOutOfSeq_Object = MibScalar
tmnxMcLagStatsDropOutOfSeq = _TmnxMcLagStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 10),
    _TmnxMcLagStatsDropOutOfSeq_Type()
)
tmnxMcLagStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropOutOfSeq.setStatus("current")
_TmnxMcLagStatsDropUnknownTlv_Type = Counter32
_TmnxMcLagStatsDropUnknownTlv_Object = MibScalar
tmnxMcLagStatsDropUnknownTlv = _TmnxMcLagStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 11),
    _TmnxMcLagStatsDropUnknownTlv_Type()
)
tmnxMcLagStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropUnknownTlv.setStatus("current")
_TmnxMcLagStatsDropTlvInvldLagId_Type = Counter32
_TmnxMcLagStatsDropTlvInvldLagId_Object = MibScalar
tmnxMcLagStatsDropTlvInvldLagId = _TmnxMcLagStatsDropTlvInvldLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 12),
    _TmnxMcLagStatsDropTlvInvldLagId_Type()
)
tmnxMcLagStatsDropTlvInvldLagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropTlvInvldLagId.setStatus("current")
_TmnxMcLagStatsDropMD5_Type = Counter32
_TmnxMcLagStatsDropMD5_Object = MibScalar
tmnxMcLagStatsDropMD5 = _TmnxMcLagStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 13),
    _TmnxMcLagStatsDropMD5_Type()
)
tmnxMcLagStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropMD5.setStatus("current")
_TmnxMcLagStatsDropUnknownPeer_Type = Counter32
_TmnxMcLagStatsDropUnknownPeer_Object = MibScalar
tmnxMcLagStatsDropUnknownPeer = _TmnxMcLagStatsDropUnknownPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 14),
    _TmnxMcLagStatsDropUnknownPeer_Type()
)
tmnxMcLagStatsDropUnknownPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsDropUnknownPeer.setStatus("current")
_TmnxMcLagStatsPktsTx_Type = Counter32
_TmnxMcLagStatsPktsTx_Object = MibScalar
tmnxMcLagStatsPktsTx = _TmnxMcLagStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 15),
    _TmnxMcLagStatsPktsTx_Type()
)
tmnxMcLagStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsTx.setStatus("current")
_TmnxMcLagStatsPktsTxKeepalive_Type = Counter32
_TmnxMcLagStatsPktsTxKeepalive_Object = MibScalar
tmnxMcLagStatsPktsTxKeepalive = _TmnxMcLagStatsPktsTxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 16),
    _TmnxMcLagStatsPktsTxKeepalive_Type()
)
tmnxMcLagStatsPktsTxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsTxKeepalive.setStatus("current")
_TmnxMcLagStatsPktsTxConfig_Type = Counter32
_TmnxMcLagStatsPktsTxConfig_Object = MibScalar
tmnxMcLagStatsPktsTxConfig = _TmnxMcLagStatsPktsTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 17),
    _TmnxMcLagStatsPktsTxConfig_Type()
)
tmnxMcLagStatsPktsTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsTxConfig.setStatus("current")
_TmnxMcLagStatsPktsTxPeerConfig_Type = Counter32
_TmnxMcLagStatsPktsTxPeerConfig_Object = MibScalar
tmnxMcLagStatsPktsTxPeerConfig = _TmnxMcLagStatsPktsTxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 18),
    _TmnxMcLagStatsPktsTxPeerConfig_Type()
)
tmnxMcLagStatsPktsTxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsTxPeerConfig.setStatus("current")
_TmnxMcLagStatsPktsTxState_Type = Counter32
_TmnxMcLagStatsPktsTxState_Object = MibScalar
tmnxMcLagStatsPktsTxState = _TmnxMcLagStatsPktsTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 19),
    _TmnxMcLagStatsPktsTxState_Type()
)
tmnxMcLagStatsPktsTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsTxState.setStatus("current")
_TmnxMcLagStatsPktsTxFailed_Type = Counter32
_TmnxMcLagStatsPktsTxFailed_Object = MibScalar
tmnxMcLagStatsPktsTxFailed = _TmnxMcLagStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 20),
    _TmnxMcLagStatsPktsTxFailed_Type()
)
tmnxMcLagStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagStatsPktsTxFailed.setStatus("current")
_TmnxMcLagPeerStatsTable_Object = MibTable
tmnxMcLagPeerStatsTable = _TmnxMcLagPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21)
)
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsTable.setStatus("current")
_TmnxMcLagPeerStatsEntry_Object = MibTableRow
tmnxMcLagPeerStatsEntry = _TmnxMcLagPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1)
)
tmnxMcLagPeerStatsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsEntry.setStatus("current")
_TmnxMcLagPeerStatsPktsRx_Type = Counter32
_TmnxMcLagPeerStatsPktsRx_Object = MibTableColumn
tmnxMcLagPeerStatsPktsRx = _TmnxMcLagPeerStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 1),
    _TmnxMcLagPeerStatsPktsRx_Type()
)
tmnxMcLagPeerStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsRx.setStatus("current")
_TmnxMcLagPeerStatsPktsRxKpalive_Type = Counter32
_TmnxMcLagPeerStatsPktsRxKpalive_Object = MibTableColumn
tmnxMcLagPeerStatsPktsRxKpalive = _TmnxMcLagPeerStatsPktsRxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 2),
    _TmnxMcLagPeerStatsPktsRxKpalive_Type()
)
tmnxMcLagPeerStatsPktsRxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsRxKpalive.setStatus("current")
_TmnxMcLagPeerStatsPktsRxConfig_Type = Counter32
_TmnxMcLagPeerStatsPktsRxConfig_Object = MibTableColumn
tmnxMcLagPeerStatsPktsRxConfig = _TmnxMcLagPeerStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 3),
    _TmnxMcLagPeerStatsPktsRxConfig_Type()
)
tmnxMcLagPeerStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsRxConfig.setStatus("current")
_TmnxMcLagPeerStatsPktsRxPeerCfg_Type = Counter32
_TmnxMcLagPeerStatsPktsRxPeerCfg_Object = MibTableColumn
tmnxMcLagPeerStatsPktsRxPeerCfg = _TmnxMcLagPeerStatsPktsRxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 4),
    _TmnxMcLagPeerStatsPktsRxPeerCfg_Type()
)
tmnxMcLagPeerStatsPktsRxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsRxPeerCfg.setStatus("current")
_TmnxMcLagPeerStatsPktsRxState_Type = Counter32
_TmnxMcLagPeerStatsPktsRxState_Object = MibTableColumn
tmnxMcLagPeerStatsPktsRxState = _TmnxMcLagPeerStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 5),
    _TmnxMcLagPeerStatsPktsRxState_Type()
)
tmnxMcLagPeerStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsRxState.setStatus("current")
_TmnxMcLagPeerStatsDropStateDsbld_Type = Counter32
_TmnxMcLagPeerStatsDropStateDsbld_Object = MibTableColumn
tmnxMcLagPeerStatsDropStateDsbld = _TmnxMcLagPeerStatsDropStateDsbld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 6),
    _TmnxMcLagPeerStatsDropStateDsbld_Type()
)
tmnxMcLagPeerStatsDropStateDsbld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropStateDsbld.setStatus("current")
_TmnxMcLagPeerStatsDropPktTooShrt_Type = Counter32
_TmnxMcLagPeerStatsDropPktTooShrt_Object = MibTableColumn
tmnxMcLagPeerStatsDropPktTooShrt = _TmnxMcLagPeerStatsDropPktTooShrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 7),
    _TmnxMcLagPeerStatsDropPktTooShrt_Type()
)
tmnxMcLagPeerStatsDropPktTooShrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropPktTooShrt.setStatus("current")
_TmnxMcLagPeerStatsDropTlvInvldSz_Type = Counter32
_TmnxMcLagPeerStatsDropTlvInvldSz_Object = MibTableColumn
tmnxMcLagPeerStatsDropTlvInvldSz = _TmnxMcLagPeerStatsDropTlvInvldSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 8),
    _TmnxMcLagPeerStatsDropTlvInvldSz_Type()
)
tmnxMcLagPeerStatsDropTlvInvldSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropTlvInvldSz.setStatus("current")
_TmnxMcLagPeerStatsDropTlvInvldId_Type = Counter32
_TmnxMcLagPeerStatsDropTlvInvldId_Object = MibTableColumn
tmnxMcLagPeerStatsDropTlvInvldId = _TmnxMcLagPeerStatsDropTlvInvldId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 9),
    _TmnxMcLagPeerStatsDropTlvInvldId_Type()
)
tmnxMcLagPeerStatsDropTlvInvldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropTlvInvldId.setStatus("current")
_TmnxMcLagPeerStatsDropOutOfSeq_Type = Counter32
_TmnxMcLagPeerStatsDropOutOfSeq_Object = MibTableColumn
tmnxMcLagPeerStatsDropOutOfSeq = _TmnxMcLagPeerStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 10),
    _TmnxMcLagPeerStatsDropOutOfSeq_Type()
)
tmnxMcLagPeerStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropOutOfSeq.setStatus("current")
_TmnxMcLagPeerStatsDropUnknownTlv_Type = Counter32
_TmnxMcLagPeerStatsDropUnknownTlv_Object = MibTableColumn
tmnxMcLagPeerStatsDropUnknownTlv = _TmnxMcLagPeerStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 11),
    _TmnxMcLagPeerStatsDropUnknownTlv_Type()
)
tmnxMcLagPeerStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropUnknownTlv.setStatus("current")
_TmnxMcLagPeerStatsDropMD5_Type = Counter32
_TmnxMcLagPeerStatsDropMD5_Object = MibTableColumn
tmnxMcLagPeerStatsDropMD5 = _TmnxMcLagPeerStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 12),
    _TmnxMcLagPeerStatsDropMD5_Type()
)
tmnxMcLagPeerStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsDropMD5.setStatus("current")
_TmnxMcLagPeerStatsPktsTx_Type = Counter32
_TmnxMcLagPeerStatsPktsTx_Object = MibTableColumn
tmnxMcLagPeerStatsPktsTx = _TmnxMcLagPeerStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 13),
    _TmnxMcLagPeerStatsPktsTx_Type()
)
tmnxMcLagPeerStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsTx.setStatus("current")
_TmnxMcLagPeerStatsPktsTxKpalive_Type = Counter32
_TmnxMcLagPeerStatsPktsTxKpalive_Object = MibTableColumn
tmnxMcLagPeerStatsPktsTxKpalive = _TmnxMcLagPeerStatsPktsTxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 14),
    _TmnxMcLagPeerStatsPktsTxKpalive_Type()
)
tmnxMcLagPeerStatsPktsTxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsTxKpalive.setStatus("current")
_TmnxMcLagPeerStatsPktsTxPeerCfg_Type = Counter32
_TmnxMcLagPeerStatsPktsTxPeerCfg_Object = MibTableColumn
tmnxMcLagPeerStatsPktsTxPeerCfg = _TmnxMcLagPeerStatsPktsTxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 15),
    _TmnxMcLagPeerStatsPktsTxPeerCfg_Type()
)
tmnxMcLagPeerStatsPktsTxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsTxPeerCfg.setStatus("current")
_TmnxMcLagPeerStatsPktsTxFailed_Type = Counter32
_TmnxMcLagPeerStatsPktsTxFailed_Object = MibTableColumn
tmnxMcLagPeerStatsPktsTxFailed = _TmnxMcLagPeerStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 21, 1, 16),
    _TmnxMcLagPeerStatsPktsTxFailed_Type()
)
tmnxMcLagPeerStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagPeerStatsPktsTxFailed.setStatus("current")
_TmnxMcLagLagStatsTable_Object = MibTable
tmnxMcLagLagStatsTable = _TmnxMcLagLagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22)
)
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsTable.setStatus("current")
_TmnxMcLagLagStatsEntry_Object = MibTableRow
tmnxMcLagLagStatsEntry = _TmnxMcLagLagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22, 1)
)
tmnxMcLagLagStatsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagId"),
)
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsEntry.setStatus("current")
_TmnxMcLagLagStatsPktsRxConfig_Type = Counter32
_TmnxMcLagLagStatsPktsRxConfig_Object = MibTableColumn
tmnxMcLagLagStatsPktsRxConfig = _TmnxMcLagLagStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22, 1, 1),
    _TmnxMcLagLagStatsPktsRxConfig_Type()
)
tmnxMcLagLagStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsPktsRxConfig.setStatus("current")
_TmnxMcLagLagStatsPktsRxState_Type = Counter32
_TmnxMcLagLagStatsPktsRxState_Object = MibTableColumn
tmnxMcLagLagStatsPktsRxState = _TmnxMcLagLagStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22, 1, 2),
    _TmnxMcLagLagStatsPktsRxState_Type()
)
tmnxMcLagLagStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsPktsRxState.setStatus("current")
_TmnxMcLagLagStatsPktsTxConfig_Type = Counter32
_TmnxMcLagLagStatsPktsTxConfig_Object = MibTableColumn
tmnxMcLagLagStatsPktsTxConfig = _TmnxMcLagLagStatsPktsTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22, 1, 3),
    _TmnxMcLagLagStatsPktsTxConfig_Type()
)
tmnxMcLagLagStatsPktsTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsPktsTxConfig.setStatus("current")
_TmnxMcLagLagStatsPktsTxState_Type = Counter32
_TmnxMcLagLagStatsPktsTxState_Object = MibTableColumn
tmnxMcLagLagStatsPktsTxState = _TmnxMcLagLagStatsPktsTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22, 1, 4),
    _TmnxMcLagLagStatsPktsTxState_Type()
)
tmnxMcLagLagStatsPktsTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsPktsTxState.setStatus("current")
_TmnxMcLagLagStatsPktsTxFailed_Type = Counter32
_TmnxMcLagLagStatsPktsTxFailed_Object = MibTableColumn
tmnxMcLagLagStatsPktsTxFailed = _TmnxMcLagLagStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 22, 1, 5),
    _TmnxMcLagLagStatsPktsTxFailed_Type()
)
tmnxMcLagLagStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcLagLagStatsPktsTxFailed.setStatus("current")
_TmnxMcPeerSyncStatsTable_Object = MibTable
tmnxMcPeerSyncStatsTable = _TmnxMcPeerSyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23)
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncStatsTable.setStatus("current")
_TmnxMcPeerSyncStatsEntry_Object = MibTableRow
tmnxMcPeerSyncStatsEntry = _TmnxMcPeerSyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1)
)
tmnxMcPeerSyncStatsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncStatsEntry.setStatus("current")
_TmnxMcPeerSyncPktsTxAll_Type = Counter32
_TmnxMcPeerSyncPktsTxAll_Object = MibTableColumn
tmnxMcPeerSyncPktsTxAll = _TmnxMcPeerSyncPktsTxAll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 1),
    _TmnxMcPeerSyncPktsTxAll_Type()
)
tmnxMcPeerSyncPktsTxAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsTxAll.setStatus("current")
_TmnxMcPeerSyncPktsTxHello_Type = Counter32
_TmnxMcPeerSyncPktsTxHello_Object = MibTableColumn
tmnxMcPeerSyncPktsTxHello = _TmnxMcPeerSyncPktsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 2),
    _TmnxMcPeerSyncPktsTxHello_Type()
)
tmnxMcPeerSyncPktsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsTxHello.setStatus("current")
_TmnxMcPeerSyncPktsTxData_Type = Counter32
_TmnxMcPeerSyncPktsTxData_Object = MibTableColumn
tmnxMcPeerSyncPktsTxData = _TmnxMcPeerSyncPktsTxData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 3),
    _TmnxMcPeerSyncPktsTxData_Type()
)
tmnxMcPeerSyncPktsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsTxData.setStatus("current")
_TmnxMcPeerSyncPktsTxOther_Type = Counter32
_TmnxMcPeerSyncPktsTxOther_Object = MibTableColumn
tmnxMcPeerSyncPktsTxOther = _TmnxMcPeerSyncPktsTxOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 4),
    _TmnxMcPeerSyncPktsTxOther_Type()
)
tmnxMcPeerSyncPktsTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsTxOther.setStatus("current")
_TmnxMcPeerSyncPktsTxErr_Type = Counter32
_TmnxMcPeerSyncPktsTxErr_Object = MibTableColumn
tmnxMcPeerSyncPktsTxErr = _TmnxMcPeerSyncPktsTxErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 5),
    _TmnxMcPeerSyncPktsTxErr_Type()
)
tmnxMcPeerSyncPktsTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsTxErr.setStatus("current")
_TmnxMcPeerSyncPktsRxAll_Type = Counter32
_TmnxMcPeerSyncPktsRxAll_Object = MibTableColumn
tmnxMcPeerSyncPktsRxAll = _TmnxMcPeerSyncPktsRxAll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 6),
    _TmnxMcPeerSyncPktsRxAll_Type()
)
tmnxMcPeerSyncPktsRxAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxAll.setStatus("current")
_TmnxMcPeerSyncPktsRxHello_Type = Counter32
_TmnxMcPeerSyncPktsRxHello_Object = MibTableColumn
tmnxMcPeerSyncPktsRxHello = _TmnxMcPeerSyncPktsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 7),
    _TmnxMcPeerSyncPktsRxHello_Type()
)
tmnxMcPeerSyncPktsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxHello.setStatus("current")
_TmnxMcPeerSyncPktsRxData_Type = Counter32
_TmnxMcPeerSyncPktsRxData_Object = MibTableColumn
tmnxMcPeerSyncPktsRxData = _TmnxMcPeerSyncPktsRxData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 8),
    _TmnxMcPeerSyncPktsRxData_Type()
)
tmnxMcPeerSyncPktsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxData.setStatus("current")
_TmnxMcPeerSyncPktsRxOther_Type = Counter32
_TmnxMcPeerSyncPktsRxOther_Object = MibTableColumn
tmnxMcPeerSyncPktsRxOther = _TmnxMcPeerSyncPktsRxOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 9),
    _TmnxMcPeerSyncPktsRxOther_Type()
)
tmnxMcPeerSyncPktsRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxOther.setStatus("current")
_TmnxMcPeerSyncPktsRxErr_Type = Counter32
_TmnxMcPeerSyncPktsRxErr_Object = MibTableColumn
tmnxMcPeerSyncPktsRxErr = _TmnxMcPeerSyncPktsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 10),
    _TmnxMcPeerSyncPktsRxErr_Type()
)
tmnxMcPeerSyncPktsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxErr.setStatus("current")
_TmnxMcPeerSyncPktsRxErrHeader_Type = Counter32
_TmnxMcPeerSyncPktsRxErrHeader_Object = MibTableColumn
tmnxMcPeerSyncPktsRxErrHeader = _TmnxMcPeerSyncPktsRxErrHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 11),
    _TmnxMcPeerSyncPktsRxErrHeader_Type()
)
tmnxMcPeerSyncPktsRxErrHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxErrHeader.setStatus("current")
_TmnxMcPeerSyncPktsRxErrBody_Type = Counter32
_TmnxMcPeerSyncPktsRxErrBody_Object = MibTableColumn
tmnxMcPeerSyncPktsRxErrBody = _TmnxMcPeerSyncPktsRxErrBody_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 12),
    _TmnxMcPeerSyncPktsRxErrBody_Type()
)
tmnxMcPeerSyncPktsRxErrBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxErrBody.setStatus("current")
_TmnxMcPeerSyncPktsRxErrSeqNum_Type = Counter32
_TmnxMcPeerSyncPktsRxErrSeqNum_Object = MibTableColumn
tmnxMcPeerSyncPktsRxErrSeqNum = _TmnxMcPeerSyncPktsRxErrSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 23, 1, 13),
    _TmnxMcPeerSyncPktsRxErrSeqNum_Type()
)
tmnxMcPeerSyncPktsRxErrSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncPktsRxErrSeqNum.setStatus("current")
_TmnxMcrPeerStatsTableLastChanged_Type = TimeStamp
_TmnxMcrPeerStatsTableLastChanged_Object = MibScalar
tmnxMcrPeerStatsTableLastChanged = _TmnxMcrPeerStatsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 24),
    _TmnxMcrPeerStatsTableLastChanged_Type()
)
tmnxMcrPeerStatsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTableLastChanged.setStatus("current")
_TmnxMcrPeerStatsTable_Object = MibTable
tmnxMcrPeerStatsTable = _TmnxMcrPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25)
)
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTable.setStatus("current")
_TmnxMcrPeerStatsEntry_Object = MibTableRow
tmnxMcrPeerStatsEntry = _TmnxMcrPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1)
)
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsEntry.setStatus("current")
_TmnxMcrPeerStatsLastChanged_Type = TimeStamp
_TmnxMcrPeerStatsLastChanged_Object = MibTableColumn
tmnxMcrPeerStatsLastChanged = _TmnxMcrPeerStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 1),
    _TmnxMcrPeerStatsLastChanged_Type()
)
tmnxMcrPeerStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsLastChanged.setStatus("current")
_TmnxMcrPeerStatsRx_Type = Counter32
_TmnxMcrPeerStatsRx_Object = MibTableColumn
tmnxMcrPeerStatsRx = _TmnxMcrPeerStatsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 2),
    _TmnxMcrPeerStatsRx_Type()
)
tmnxMcrPeerStatsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsRx.setStatus("current")
_TmnxMcrPeerStatsRxMcsIdReq_Type = Counter32
_TmnxMcrPeerStatsRxMcsIdReq_Object = MibTableColumn
tmnxMcrPeerStatsRxMcsIdReq = _TmnxMcrPeerStatsRxMcsIdReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 3),
    _TmnxMcrPeerStatsRxMcsIdReq_Type()
)
tmnxMcrPeerStatsRxMcsIdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsRxMcsIdReq.setStatus("current")
_TmnxMcrPeerStatsRxMcsIdRsp_Type = Counter32
_TmnxMcrPeerStatsRxMcsIdRsp_Object = MibTableColumn
tmnxMcrPeerStatsRxMcsIdRsp = _TmnxMcrPeerStatsRxMcsIdRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 4),
    _TmnxMcrPeerStatsRxMcsIdRsp_Type()
)
tmnxMcrPeerStatsRxMcsIdRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsRxMcsIdRsp.setStatus("current")
_TmnxMcrPeerStatsRxRingExistsReq_Type = Counter32
_TmnxMcrPeerStatsRxRingExistsReq_Object = MibTableColumn
tmnxMcrPeerStatsRxRingExistsReq = _TmnxMcrPeerStatsRxRingExistsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 5),
    _TmnxMcrPeerStatsRxRingExistsReq_Type()
)
tmnxMcrPeerStatsRxRingExistsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsRxRingExistsReq.setStatus("current")
_TmnxMcrPeerStatsRxRingExistsRsp_Type = Counter32
_TmnxMcrPeerStatsRxRingExistsRsp_Object = MibTableColumn
tmnxMcrPeerStatsRxRingExistsRsp = _TmnxMcrPeerStatsRxRingExistsRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 6),
    _TmnxMcrPeerStatsRxRingExistsRsp_Type()
)
tmnxMcrPeerStatsRxRingExistsRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsRxRingExistsRsp.setStatus("current")
_TmnxMcrPeerStatsRxKeepAlive_Type = Counter32
_TmnxMcrPeerStatsRxKeepAlive_Object = MibTableColumn
tmnxMcrPeerStatsRxKeepAlive = _TmnxMcrPeerStatsRxKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 7),
    _TmnxMcrPeerStatsRxKeepAlive_Type()
)
tmnxMcrPeerStatsRxKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsRxKeepAlive.setStatus("current")
_TmnxMcrPeerStatsTx_Type = Counter32
_TmnxMcrPeerStatsTx_Object = MibTableColumn
tmnxMcrPeerStatsTx = _TmnxMcrPeerStatsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 8),
    _TmnxMcrPeerStatsTx_Type()
)
tmnxMcrPeerStatsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTx.setStatus("current")
_TmnxMcrPeerStatsTxMcsIdReq_Type = Counter32
_TmnxMcrPeerStatsTxMcsIdReq_Object = MibTableColumn
tmnxMcrPeerStatsTxMcsIdReq = _TmnxMcrPeerStatsTxMcsIdReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 9),
    _TmnxMcrPeerStatsTxMcsIdReq_Type()
)
tmnxMcrPeerStatsTxMcsIdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTxMcsIdReq.setStatus("current")
_TmnxMcrPeerStatsTxMcsIdRsp_Type = Counter32
_TmnxMcrPeerStatsTxMcsIdRsp_Object = MibTableColumn
tmnxMcrPeerStatsTxMcsIdRsp = _TmnxMcrPeerStatsTxMcsIdRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 10),
    _TmnxMcrPeerStatsTxMcsIdRsp_Type()
)
tmnxMcrPeerStatsTxMcsIdRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTxMcsIdRsp.setStatus("current")
_TmnxMcrPeerStatsTxRingExistsReq_Type = Counter32
_TmnxMcrPeerStatsTxRingExistsReq_Object = MibTableColumn
tmnxMcrPeerStatsTxRingExistsReq = _TmnxMcrPeerStatsTxRingExistsReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 11),
    _TmnxMcrPeerStatsTxRingExistsReq_Type()
)
tmnxMcrPeerStatsTxRingExistsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTxRingExistsReq.setStatus("current")
_TmnxMcrPeerStatsTxRingExistsRsp_Type = Counter32
_TmnxMcrPeerStatsTxRingExistsRsp_Object = MibTableColumn
tmnxMcrPeerStatsTxRingExistsRsp = _TmnxMcrPeerStatsTxRingExistsRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 12),
    _TmnxMcrPeerStatsTxRingExistsRsp_Type()
)
tmnxMcrPeerStatsTxRingExistsRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTxRingExistsRsp.setStatus("current")
_TmnxMcrPeerStatsTxKeepAlive_Type = Counter32
_TmnxMcrPeerStatsTxKeepAlive_Object = MibTableColumn
tmnxMcrPeerStatsTxKeepAlive = _TmnxMcrPeerStatsTxKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 25, 1, 13),
    _TmnxMcrPeerStatsTxKeepAlive_Type()
)
tmnxMcrPeerStatsTxKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrPeerStatsTxKeepAlive.setStatus("current")
_TmnxMcrRingStatsTableLastChanged_Type = TimeStamp
_TmnxMcrRingStatsTableLastChanged_Object = MibScalar
tmnxMcrRingStatsTableLastChanged = _TmnxMcrRingStatsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 26),
    _TmnxMcrRingStatsTableLastChanged_Type()
)
tmnxMcrRingStatsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsTableLastChanged.setStatus("current")
_TmnxMcrRingStatsTable_Object = MibTable
tmnxMcrRingStatsTable = _TmnxMcrRingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27)
)
if mibBuilder.loadTexts:
    tmnxMcrRingStatsTable.setStatus("current")
_TmnxMcrRingStatsEntry_Object = MibTableRow
tmnxMcrRingStatsEntry = _TmnxMcrRingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1)
)
if mibBuilder.loadTexts:
    tmnxMcrRingStatsEntry.setStatus("current")
_TmnxMcrRingStatsLastChanged_Type = TimeStamp
_TmnxMcrRingStatsLastChanged_Object = MibTableColumn
tmnxMcrRingStatsLastChanged = _TmnxMcrRingStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1, 1),
    _TmnxMcrRingStatsLastChanged_Type()
)
tmnxMcrRingStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsLastChanged.setStatus("current")
_TmnxMcrRingStatsRxSapsChanged_Type = Counter32
_TmnxMcrRingStatsRxSapsChanged_Object = MibTableColumn
tmnxMcrRingStatsRxSapsChanged = _TmnxMcrRingStatsRxSapsChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1, 2),
    _TmnxMcrRingStatsRxSapsChanged_Type()
)
tmnxMcrRingStatsRxSapsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsRxSapsChanged.setStatus("current")
_TmnxMcrRingStatsTxSapsChanged_Type = Counter32
_TmnxMcrRingStatsTxSapsChanged_Object = MibTableColumn
tmnxMcrRingStatsTxSapsChanged = _TmnxMcrRingStatsTxSapsChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1, 3),
    _TmnxMcrRingStatsTxSapsChanged_Type()
)
tmnxMcrRingStatsTxSapsChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsTxSapsChanged.setStatus("current")
_TmnxMcrRingStatsRxOpaqueDelivrd_Type = Counter32
_TmnxMcrRingStatsRxOpaqueDelivrd_Object = MibTableColumn
tmnxMcrRingStatsRxOpaqueDelivrd = _TmnxMcrRingStatsRxOpaqueDelivrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1, 4),
    _TmnxMcrRingStatsRxOpaqueDelivrd_Type()
)
tmnxMcrRingStatsRxOpaqueDelivrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsRxOpaqueDelivrd.setStatus("current")
_TmnxMcrRingStatsRxOpaqueNoDest_Type = Counter32
_TmnxMcrRingStatsRxOpaqueNoDest_Object = MibTableColumn
tmnxMcrRingStatsRxOpaqueNoDest = _TmnxMcrRingStatsRxOpaqueNoDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1, 5),
    _TmnxMcrRingStatsRxOpaqueNoDest_Type()
)
tmnxMcrRingStatsRxOpaqueNoDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsRxOpaqueNoDest.setStatus("current")
_TmnxMcrRingStatsTxOpaque_Type = Counter32
_TmnxMcrRingStatsTxOpaque_Object = MibTableColumn
tmnxMcrRingStatsTxOpaque = _TmnxMcrRingStatsTxOpaque_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 27, 1, 6),
    _TmnxMcrRingStatsTxOpaque_Type()
)
tmnxMcrRingStatsTxOpaque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingStatsTxOpaque.setStatus("current")
_TmnxMcrStatsRx_Type = Counter32
_TmnxMcrStatsRx_Object = MibScalar
tmnxMcrStatsRx = _TmnxMcrStatsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 28),
    _TmnxMcrStatsRx_Type()
)
tmnxMcrStatsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRx.setStatus("current")
_TmnxMcrStatsRxTooShort_Type = Counter32
_TmnxMcrStatsRxTooShort_Object = MibScalar
tmnxMcrStatsRxTooShort = _TmnxMcrStatsRxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 29),
    _TmnxMcrStatsRxTooShort_Type()
)
tmnxMcrStatsRxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxTooShort.setStatus("current")
_TmnxMcrStatsRxWrongAuth_Type = Counter32
_TmnxMcrStatsRxWrongAuth_Object = MibScalar
tmnxMcrStatsRxWrongAuth = _TmnxMcrStatsRxWrongAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 30),
    _TmnxMcrStatsRxWrongAuth_Type()
)
tmnxMcrStatsRxWrongAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxWrongAuth.setStatus("current")
_TmnxMcrStatsRxInvalidTlv_Type = Counter32
_TmnxMcrStatsRxInvalidTlv_Object = MibScalar
tmnxMcrStatsRxInvalidTlv = _TmnxMcrStatsRxInvalidTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 31),
    _TmnxMcrStatsRxInvalidTlv_Type()
)
tmnxMcrStatsRxInvalidTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxInvalidTlv.setStatus("current")
_TmnxMcrStatsRxIncomplete_Type = Counter32
_TmnxMcrStatsRxIncomplete_Object = MibScalar
tmnxMcrStatsRxIncomplete = _TmnxMcrStatsRxIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 32),
    _TmnxMcrStatsRxIncomplete_Type()
)
tmnxMcrStatsRxIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxIncomplete.setStatus("current")
_TmnxMcrStatsRxUnknownType_Type = Counter32
_TmnxMcrStatsRxUnknownType_Object = MibScalar
tmnxMcrStatsRxUnknownType = _TmnxMcrStatsRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 33),
    _TmnxMcrStatsRxUnknownType_Type()
)
tmnxMcrStatsRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxUnknownType.setStatus("current")
_TmnxMcrStatsRxUnknownPeer_Type = Counter32
_TmnxMcrStatsRxUnknownPeer_Object = MibScalar
tmnxMcrStatsRxUnknownPeer = _TmnxMcrStatsRxUnknownPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 34),
    _TmnxMcrStatsRxUnknownPeer_Type()
)
tmnxMcrStatsRxUnknownPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxUnknownPeer.setStatus("current")
_TmnxMcrStatsRxUnknownRing_Type = Counter32
_TmnxMcrStatsRxUnknownRing_Object = MibScalar
tmnxMcrStatsRxUnknownRing = _TmnxMcrStatsRxUnknownRing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 35),
    _TmnxMcrStatsRxUnknownRing_Type()
)
tmnxMcrStatsRxUnknownRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxUnknownRing.setStatus("current")
_TmnxMcrStatsRxUnknownRingNode_Type = Counter32
_TmnxMcrStatsRxUnknownRingNode_Object = MibScalar
tmnxMcrStatsRxUnknownRingNode = _TmnxMcrStatsRxUnknownRingNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 36),
    _TmnxMcrStatsRxUnknownRingNode_Type()
)
tmnxMcrStatsRxUnknownRingNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxUnknownRingNode.setStatus("current")
_TmnxMcrStatsRxDelivrdToPeer_Type = Counter32
_TmnxMcrStatsRxDelivrdToPeer_Object = MibScalar
tmnxMcrStatsRxDelivrdToPeer = _TmnxMcrStatsRxDelivrdToPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 37),
    _TmnxMcrStatsRxDelivrdToPeer_Type()
)
tmnxMcrStatsRxDelivrdToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxDelivrdToPeer.setStatus("current")
_TmnxMcrStatsRxDelivrdToRing_Type = Counter32
_TmnxMcrStatsRxDelivrdToRing_Object = MibScalar
tmnxMcrStatsRxDelivrdToRing = _TmnxMcrStatsRxDelivrdToRing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 38),
    _TmnxMcrStatsRxDelivrdToRing_Type()
)
tmnxMcrStatsRxDelivrdToRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxDelivrdToRing.setStatus("current")
_TmnxMcrStatsRxDelivrdToRingNode_Type = Counter32
_TmnxMcrStatsRxDelivrdToRingNode_Object = MibScalar
tmnxMcrStatsRxDelivrdToRingNode = _TmnxMcrStatsRxDelivrdToRingNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 39),
    _TmnxMcrStatsRxDelivrdToRingNode_Type()
)
tmnxMcrStatsRxDelivrdToRingNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsRxDelivrdToRingNode.setStatus("current")
_TmnxMcrStatsTx_Type = Counter32
_TmnxMcrStatsTx_Object = MibScalar
tmnxMcrStatsTx = _TmnxMcrStatsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 40),
    _TmnxMcrStatsTx_Type()
)
tmnxMcrStatsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsTx.setStatus("current")
_TmnxMcrStatsTxNoBuffer_Type = Counter32
_TmnxMcrStatsTxNoBuffer_Object = MibScalar
tmnxMcrStatsTxNoBuffer = _TmnxMcrStatsTxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 41),
    _TmnxMcrStatsTxNoBuffer_Type()
)
tmnxMcrStatsTxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsTxNoBuffer.setStatus("current")
_TmnxMcrStatsTxTransmitFailed_Type = Counter32
_TmnxMcrStatsTxTransmitFailed_Object = MibScalar
tmnxMcrStatsTxTransmitFailed = _TmnxMcrStatsTxTransmitFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 42),
    _TmnxMcrStatsTxTransmitFailed_Type()
)
tmnxMcrStatsTxTransmitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsTxTransmitFailed.setStatus("current")
_TmnxMcrStatsMissedConfigEvent_Type = Counter32
_TmnxMcrStatsMissedConfigEvent_Object = MibScalar
tmnxMcrStatsMissedConfigEvent = _TmnxMcrStatsMissedConfigEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 43),
    _TmnxMcrStatsMissedConfigEvent_Type()
)
tmnxMcrStatsMissedConfigEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsMissedConfigEvent.setStatus("current")
_TmnxMcrStatsMissedBfdEvent_Type = Counter32
_TmnxMcrStatsMissedBfdEvent_Object = MibScalar
tmnxMcrStatsMissedBfdEvent = _TmnxMcrStatsMissedBfdEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 44),
    _TmnxMcrStatsMissedBfdEvent_Type()
)
tmnxMcrStatsMissedBfdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsMissedBfdEvent.setStatus("current")
_TmnxMcrStatsTxUnknownDest_Type = Counter32
_TmnxMcrStatsTxUnknownDest_Object = MibScalar
tmnxMcrStatsTxUnknownDest = _TmnxMcrStatsTxUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 45),
    _TmnxMcrStatsTxUnknownDest_Type()
)
tmnxMcrStatsTxUnknownDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrStatsTxUnknownDest.setStatus("current")
_TmnxMcrRingNodeStatsTableLastChanged_Type = TimeStamp
_TmnxMcrRingNodeStatsTableLastChanged_Object = MibScalar
tmnxMcrRingNodeStatsTableLastChanged = _TmnxMcrRingNodeStatsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 46),
    _TmnxMcrRingNodeStatsTableLastChanged_Type()
)
tmnxMcrRingNodeStatsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsTableLastChanged.setStatus("current")
_TmnxMcrRingNodeStatsTable_Object = MibTable
tmnxMcrRingNodeStatsTable = _TmnxMcrRingNodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47)
)
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsTable.setStatus("current")
_TmnxMcrRingNodeStatsEntry_Object = MibTableRow
tmnxMcrRingNodeStatsEntry = _TmnxMcrRingNodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1)
)
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsEntry.setStatus("current")
_TmnxMcrRingNodeStatsLastChanged_Type = TimeStamp
_TmnxMcrRingNodeStatsLastChanged_Object = MibTableColumn
tmnxMcrRingNodeStatsLastChanged = _TmnxMcrRingNodeStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 1),
    _TmnxMcrRingNodeStatsLastChanged_Type()
)
tmnxMcrRingNodeStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsLastChanged.setStatus("current")
_TmnxMcrRingNodeStatsRxDetect_Type = Counter32
_TmnxMcrRingNodeStatsRxDetect_Object = MibTableColumn
tmnxMcrRingNodeStatsRxDetect = _TmnxMcrRingNodeStatsRxDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 2),
    _TmnxMcrRingNodeStatsRxDetect_Type()
)
tmnxMcrRingNodeStatsRxDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsRxDetect.setStatus("current")
_TmnxMcrRingNodeStatsRxDetectAck_Type = Counter32
_TmnxMcrRingNodeStatsRxDetectAck_Object = MibTableColumn
tmnxMcrRingNodeStatsRxDetectAck = _TmnxMcrRingNodeStatsRxDetectAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 3),
    _TmnxMcrRingNodeStatsRxDetectAck_Type()
)
tmnxMcrRingNodeStatsRxDetectAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsRxDetectAck.setStatus("current")
_TmnxMcrRingNodeStatsRncvRxResp_Type = Counter32
_TmnxMcrRingNodeStatsRncvRxResp_Object = MibTableColumn
tmnxMcrRingNodeStatsRncvRxResp = _TmnxMcrRingNodeStatsRncvRxResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 4),
    _TmnxMcrRingNodeStatsRncvRxResp_Type()
)
tmnxMcrRingNodeStatsRncvRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsRncvRxResp.setStatus("current")
_TmnxMcrRingNodeStatsTxDetect_Type = Counter32
_TmnxMcrRingNodeStatsTxDetect_Object = MibTableColumn
tmnxMcrRingNodeStatsTxDetect = _TmnxMcrRingNodeStatsTxDetect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 5),
    _TmnxMcrRingNodeStatsTxDetect_Type()
)
tmnxMcrRingNodeStatsTxDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsTxDetect.setStatus("current")
_TmnxMcrRingNodeStatsTxDetectAck_Type = Counter32
_TmnxMcrRingNodeStatsTxDetectAck_Object = MibTableColumn
tmnxMcrRingNodeStatsTxDetectAck = _TmnxMcrRingNodeStatsTxDetectAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 6),
    _TmnxMcrRingNodeStatsTxDetectAck_Type()
)
tmnxMcrRingNodeStatsTxDetectAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsTxDetectAck.setStatus("current")
_TmnxMcrRingNodeStatsRncvTxReq_Type = Counter32
_TmnxMcrRingNodeStatsRncvTxReq_Object = MibTableColumn
tmnxMcrRingNodeStatsRncvTxReq = _TmnxMcrRingNodeStatsRncvTxReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 7),
    _TmnxMcrRingNodeStatsRncvTxReq_Type()
)
tmnxMcrRingNodeStatsRncvTxReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsRncvTxReq.setStatus("current")
_TmnxMcrRingNodeStatsRncvRtTime_Type = TimeInterval
_TmnxMcrRingNodeStatsRncvRtTime_Object = MibTableColumn
tmnxMcrRingNodeStatsRncvRtTime = _TmnxMcrRingNodeStatsRncvRtTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 47, 1, 8),
    _TmnxMcrRingNodeStatsRncvRtTime_Type()
)
tmnxMcrRingNodeStatsRncvRtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcrRingNodeStatsRncvRtTime.setStatus("current")
_TmnxMcEPPeerStatsTable_Object = MibTable
tmnxMcEPPeerStatsTable = _TmnxMcEPPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48)
)
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsTable.setStatus("current")
_TmnxMcEPPeerStatsEntry_Object = MibTableRow
tmnxMcEPPeerStatsEntry = _TmnxMcEPPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1)
)
tmnxMcEPPeerStatsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsEntry.setStatus("current")
_TmnxMcEPPeerStatsPktsRx_Type = Counter32
_TmnxMcEPPeerStatsPktsRx_Object = MibTableColumn
tmnxMcEPPeerStatsPktsRx = _TmnxMcEPPeerStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 1),
    _TmnxMcEPPeerStatsPktsRx_Type()
)
tmnxMcEPPeerStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsRx.setStatus("current")
_TmnxMcEPPeerStatsPktsRxKpalive_Type = Counter32
_TmnxMcEPPeerStatsPktsRxKpalive_Object = MibTableColumn
tmnxMcEPPeerStatsPktsRxKpalive = _TmnxMcEPPeerStatsPktsRxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 2),
    _TmnxMcEPPeerStatsPktsRxKpalive_Type()
)
tmnxMcEPPeerStatsPktsRxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsRxKpalive.setStatus("current")
_TmnxMcEPPeerStatsPktsRxConfig_Type = Counter32
_TmnxMcEPPeerStatsPktsRxConfig_Object = MibTableColumn
tmnxMcEPPeerStatsPktsRxConfig = _TmnxMcEPPeerStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 3),
    _TmnxMcEPPeerStatsPktsRxConfig_Type()
)
tmnxMcEPPeerStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsRxConfig.setStatus("current")
_TmnxMcEPPeerStatsPktsRxPeerCfg_Type = Counter32
_TmnxMcEPPeerStatsPktsRxPeerCfg_Object = MibTableColumn
tmnxMcEPPeerStatsPktsRxPeerCfg = _TmnxMcEPPeerStatsPktsRxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 4),
    _TmnxMcEPPeerStatsPktsRxPeerCfg_Type()
)
tmnxMcEPPeerStatsPktsRxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsRxPeerCfg.setStatus("current")
_TmnxMcEPPeerStatsPktsRxState_Type = Counter32
_TmnxMcEPPeerStatsPktsRxState_Object = MibTableColumn
tmnxMcEPPeerStatsPktsRxState = _TmnxMcEPPeerStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 5),
    _TmnxMcEPPeerStatsPktsRxState_Type()
)
tmnxMcEPPeerStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsRxState.setStatus("current")
_TmnxMcEPPeerStatsDropStateDsbld_Type = Counter32
_TmnxMcEPPeerStatsDropStateDsbld_Object = MibTableColumn
tmnxMcEPPeerStatsDropStateDsbld = _TmnxMcEPPeerStatsDropStateDsbld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 6),
    _TmnxMcEPPeerStatsDropStateDsbld_Type()
)
tmnxMcEPPeerStatsDropStateDsbld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropStateDsbld.setStatus("current")
_TmnxMcEPPeerStatsDropPktTooShrt_Type = Counter32
_TmnxMcEPPeerStatsDropPktTooShrt_Object = MibTableColumn
tmnxMcEPPeerStatsDropPktTooShrt = _TmnxMcEPPeerStatsDropPktTooShrt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 7),
    _TmnxMcEPPeerStatsDropPktTooShrt_Type()
)
tmnxMcEPPeerStatsDropPktTooShrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropPktTooShrt.setStatus("current")
_TmnxMcEPPeerStatsDropTlvInvldSz_Type = Counter32
_TmnxMcEPPeerStatsDropTlvInvldSz_Object = MibTableColumn
tmnxMcEPPeerStatsDropTlvInvldSz = _TmnxMcEPPeerStatsDropTlvInvldSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 8),
    _TmnxMcEPPeerStatsDropTlvInvldSz_Type()
)
tmnxMcEPPeerStatsDropTlvInvldSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropTlvInvldSz.setStatus("current")
_TmnxMcEPPeerStatsDropTlvInvldId_Type = Counter32
_TmnxMcEPPeerStatsDropTlvInvldId_Object = MibTableColumn
tmnxMcEPPeerStatsDropTlvInvldId = _TmnxMcEPPeerStatsDropTlvInvldId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 9),
    _TmnxMcEPPeerStatsDropTlvInvldId_Type()
)
tmnxMcEPPeerStatsDropTlvInvldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropTlvInvldId.setStatus("current")
_TmnxMcEPPeerStatsDropOutOfSeq_Type = Counter32
_TmnxMcEPPeerStatsDropOutOfSeq_Object = MibTableColumn
tmnxMcEPPeerStatsDropOutOfSeq = _TmnxMcEPPeerStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 10),
    _TmnxMcEPPeerStatsDropOutOfSeq_Type()
)
tmnxMcEPPeerStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropOutOfSeq.setStatus("current")
_TmnxMcEPPeerStatsDropUnknownTlv_Type = Counter32
_TmnxMcEPPeerStatsDropUnknownTlv_Object = MibTableColumn
tmnxMcEPPeerStatsDropUnknownTlv = _TmnxMcEPPeerStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 11),
    _TmnxMcEPPeerStatsDropUnknownTlv_Type()
)
tmnxMcEPPeerStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropUnknownTlv.setStatus("current")
_TmnxMcEPPeerStatsDropMD5_Type = Counter32
_TmnxMcEPPeerStatsDropMD5_Object = MibTableColumn
tmnxMcEPPeerStatsDropMD5 = _TmnxMcEPPeerStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 12),
    _TmnxMcEPPeerStatsDropMD5_Type()
)
tmnxMcEPPeerStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropMD5.setStatus("current")
_TmnxMcEPPeerStatsPktsTx_Type = Counter32
_TmnxMcEPPeerStatsPktsTx_Object = MibTableColumn
tmnxMcEPPeerStatsPktsTx = _TmnxMcEPPeerStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 13),
    _TmnxMcEPPeerStatsPktsTx_Type()
)
tmnxMcEPPeerStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsTx.setStatus("current")
_TmnxMcEPPeerStatsPktsTxKpalive_Type = Counter32
_TmnxMcEPPeerStatsPktsTxKpalive_Object = MibTableColumn
tmnxMcEPPeerStatsPktsTxKpalive = _TmnxMcEPPeerStatsPktsTxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 14),
    _TmnxMcEPPeerStatsPktsTxKpalive_Type()
)
tmnxMcEPPeerStatsPktsTxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsTxKpalive.setStatus("current")
_TmnxMcEPPeerStatsPktsTxPeerCfg_Type = Counter32
_TmnxMcEPPeerStatsPktsTxPeerCfg_Object = MibTableColumn
tmnxMcEPPeerStatsPktsTxPeerCfg = _TmnxMcEPPeerStatsPktsTxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 15),
    _TmnxMcEPPeerStatsPktsTxPeerCfg_Type()
)
tmnxMcEPPeerStatsPktsTxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsTxPeerCfg.setStatus("current")
_TmnxMcEPPeerStatsPktsTxFailed_Type = Counter32
_TmnxMcEPPeerStatsPktsTxFailed_Object = MibTableColumn
tmnxMcEPPeerStatsPktsTxFailed = _TmnxMcEPPeerStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 16),
    _TmnxMcEPPeerStatsPktsTxFailed_Type()
)
tmnxMcEPPeerStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsPktsTxFailed.setStatus("current")
_TmnxMcEPPeerStatsDropEpNoPeer_Type = Counter32
_TmnxMcEPPeerStatsDropEpNoPeer_Object = MibTableColumn
tmnxMcEPPeerStatsDropEpNoPeer = _TmnxMcEPPeerStatsDropEpNoPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 48, 1, 17),
    _TmnxMcEPPeerStatsDropEpNoPeer_Type()
)
tmnxMcEPPeerStatsDropEpNoPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEPPeerStatsDropEpNoPeer.setStatus("current")
_TmnxMcEpGlobalStats_ObjectIdentity = ObjectIdentity
tmnxMcEpGlobalStats = _TmnxMcEpGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49)
)
_TmnxMcEpStatsPktsRx_Type = Counter32
_TmnxMcEpStatsPktsRx_Object = MibScalar
tmnxMcEpStatsPktsRx = _TmnxMcEpStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 1),
    _TmnxMcEpStatsPktsRx_Type()
)
tmnxMcEpStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsRx.setStatus("current")
_TmnxMcEpStatsPktsRxKeepalive_Type = Counter32
_TmnxMcEpStatsPktsRxKeepalive_Object = MibScalar
tmnxMcEpStatsPktsRxKeepalive = _TmnxMcEpStatsPktsRxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 2),
    _TmnxMcEpStatsPktsRxKeepalive_Type()
)
tmnxMcEpStatsPktsRxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsRxKeepalive.setStatus("current")
_TmnxMcEpStatsPktsRxConfig_Type = Counter32
_TmnxMcEpStatsPktsRxConfig_Object = MibScalar
tmnxMcEpStatsPktsRxConfig = _TmnxMcEpStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 3),
    _TmnxMcEpStatsPktsRxConfig_Type()
)
tmnxMcEpStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsRxConfig.setStatus("current")
_TmnxMcEpStatsPktsRxPeerConfig_Type = Counter32
_TmnxMcEpStatsPktsRxPeerConfig_Object = MibScalar
tmnxMcEpStatsPktsRxPeerConfig = _TmnxMcEpStatsPktsRxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 4),
    _TmnxMcEpStatsPktsRxPeerConfig_Type()
)
tmnxMcEpStatsPktsRxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsRxPeerConfig.setStatus("current")
_TmnxMcEpStatsPktsRxState_Type = Counter32
_TmnxMcEpStatsPktsRxState_Object = MibScalar
tmnxMcEpStatsPktsRxState = _TmnxMcEpStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 5),
    _TmnxMcEpStatsPktsRxState_Type()
)
tmnxMcEpStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsRxState.setStatus("current")
_TmnxMcEpStatsDropPktKpaliveTask_Type = Counter32
_TmnxMcEpStatsDropPktKpaliveTask_Object = MibScalar
tmnxMcEpStatsDropPktKpaliveTask = _TmnxMcEpStatsDropPktKpaliveTask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 6),
    _TmnxMcEpStatsDropPktKpaliveTask_Type()
)
tmnxMcEpStatsDropPktKpaliveTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropPktKpaliveTask.setStatus("current")
_TmnxMcEpStatsDropPktTooShort_Type = Counter32
_TmnxMcEpStatsDropPktTooShort_Object = MibScalar
tmnxMcEpStatsDropPktTooShort = _TmnxMcEpStatsDropPktTooShort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 7),
    _TmnxMcEpStatsDropPktTooShort_Type()
)
tmnxMcEpStatsDropPktTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropPktTooShort.setStatus("current")
_TmnxMcEpStatsDropPktVerifyFailed_Type = Counter32
_TmnxMcEpStatsDropPktVerifyFailed_Object = MibScalar
tmnxMcEpStatsDropPktVerifyFailed = _TmnxMcEpStatsDropPktVerifyFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 8),
    _TmnxMcEpStatsDropPktVerifyFailed_Type()
)
tmnxMcEpStatsDropPktVerifyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropPktVerifyFailed.setStatus("current")
_TmnxMcEpStatsDropTlvInvalidSize_Type = Counter32
_TmnxMcEpStatsDropTlvInvalidSize_Object = MibScalar
tmnxMcEpStatsDropTlvInvalidSize = _TmnxMcEpStatsDropTlvInvalidSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 9),
    _TmnxMcEpStatsDropTlvInvalidSize_Type()
)
tmnxMcEpStatsDropTlvInvalidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropTlvInvalidSize.setStatus("current")
_TmnxMcEpStatsDropOutOfSeq_Type = Counter32
_TmnxMcEpStatsDropOutOfSeq_Object = MibScalar
tmnxMcEpStatsDropOutOfSeq = _TmnxMcEpStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 10),
    _TmnxMcEpStatsDropOutOfSeq_Type()
)
tmnxMcEpStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropOutOfSeq.setStatus("current")
_TmnxMcEpStatsDropUnknownTlv_Type = Counter32
_TmnxMcEpStatsDropUnknownTlv_Object = MibScalar
tmnxMcEpStatsDropUnknownTlv = _TmnxMcEpStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 11),
    _TmnxMcEpStatsDropUnknownTlv_Type()
)
tmnxMcEpStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropUnknownTlv.setStatus("current")
_TmnxMcEpStatsDropTlvInvldEpId_Type = Counter32
_TmnxMcEpStatsDropTlvInvldEpId_Object = MibScalar
tmnxMcEpStatsDropTlvInvldEpId = _TmnxMcEpStatsDropTlvInvldEpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 12),
    _TmnxMcEpStatsDropTlvInvldEpId_Type()
)
tmnxMcEpStatsDropTlvInvldEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropTlvInvldEpId.setStatus("current")
_TmnxMcEpStatsDropMD5_Type = Counter32
_TmnxMcEpStatsDropMD5_Object = MibScalar
tmnxMcEpStatsDropMD5 = _TmnxMcEpStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 13),
    _TmnxMcEpStatsDropMD5_Type()
)
tmnxMcEpStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropMD5.setStatus("current")
_TmnxMcEpStatsDropUnknownPeer_Type = Counter32
_TmnxMcEpStatsDropUnknownPeer_Object = MibScalar
tmnxMcEpStatsDropUnknownPeer = _TmnxMcEpStatsDropUnknownPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 14),
    _TmnxMcEpStatsDropUnknownPeer_Type()
)
tmnxMcEpStatsDropUnknownPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropUnknownPeer.setStatus("current")
_TmnxMcEpStatsPktsTx_Type = Counter32
_TmnxMcEpStatsPktsTx_Object = MibScalar
tmnxMcEpStatsPktsTx = _TmnxMcEpStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 15),
    _TmnxMcEpStatsPktsTx_Type()
)
tmnxMcEpStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsTx.setStatus("current")
_TmnxMcEpStatsPktsTxKeepalive_Type = Counter32
_TmnxMcEpStatsPktsTxKeepalive_Object = MibScalar
tmnxMcEpStatsPktsTxKeepalive = _TmnxMcEpStatsPktsTxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 16),
    _TmnxMcEpStatsPktsTxKeepalive_Type()
)
tmnxMcEpStatsPktsTxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsTxKeepalive.setStatus("current")
_TmnxMcEpStatsPktsTxConfig_Type = Counter32
_TmnxMcEpStatsPktsTxConfig_Object = MibScalar
tmnxMcEpStatsPktsTxConfig = _TmnxMcEpStatsPktsTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 17),
    _TmnxMcEpStatsPktsTxConfig_Type()
)
tmnxMcEpStatsPktsTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsTxConfig.setStatus("current")
_TmnxMcEpStatsPktsTxPeerConfig_Type = Counter32
_TmnxMcEpStatsPktsTxPeerConfig_Object = MibScalar
tmnxMcEpStatsPktsTxPeerConfig = _TmnxMcEpStatsPktsTxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 18),
    _TmnxMcEpStatsPktsTxPeerConfig_Type()
)
tmnxMcEpStatsPktsTxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsTxPeerConfig.setStatus("current")
_TmnxMcEpStatsPktsTxState_Type = Counter32
_TmnxMcEpStatsPktsTxState_Object = MibScalar
tmnxMcEpStatsPktsTxState = _TmnxMcEpStatsPktsTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 19),
    _TmnxMcEpStatsPktsTxState_Type()
)
tmnxMcEpStatsPktsTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsTxState.setStatus("current")
_TmnxMcEpStatsPktsTxFailed_Type = Counter32
_TmnxMcEpStatsPktsTxFailed_Object = MibScalar
tmnxMcEpStatsPktsTxFailed = _TmnxMcEpStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 20),
    _TmnxMcEpStatsPktsTxFailed_Type()
)
tmnxMcEpStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsPktsTxFailed.setStatus("current")
_TmnxMcEpStatsDropEpNoPeer_Type = Counter32
_TmnxMcEpStatsDropEpNoPeer_Object = MibScalar
tmnxMcEpStatsDropEpNoPeer = _TmnxMcEpStatsDropEpNoPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 49, 21),
    _TmnxMcEpStatsDropEpNoPeer_Type()
)
tmnxMcEpStatsDropEpNoPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcEpStatsDropEpNoPeer.setStatus("current")
_TmnxMcWppPeerStatsTableLastCh_Type = TimeStamp
_TmnxMcWppPeerStatsTableLastCh_Object = MibScalar
tmnxMcWppPeerStatsTableLastCh = _TmnxMcWppPeerStatsTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 50),
    _TmnxMcWppPeerStatsTableLastCh_Type()
)
tmnxMcWppPeerStatsTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsTableLastCh.setStatus("current")
_TmnxMcWppPeerStatsTable_Object = MibTable
tmnxMcWppPeerStatsTable = _TmnxMcWppPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 51)
)
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsTable.setStatus("current")
_TmnxMcWppPeerStatsEntry_Object = MibTableRow
tmnxMcWppPeerStatsEntry = _TmnxMcWppPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 51, 1)
)
tmnxMcWppPeerStatsEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcWppPeerStatsInstance"),
)
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsEntry.setStatus("current")


class _TmnxMcWppPeerStatsInstance_Type(Unsigned32):
    """Custom type tmnxMcWppPeerStatsInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TmnxMcWppPeerStatsInstance_Type.__name__ = "Unsigned32"
_TmnxMcWppPeerStatsInstance_Object = MibTableColumn
tmnxMcWppPeerStatsInstance = _TmnxMcWppPeerStatsInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 51, 1, 1),
    _TmnxMcWppPeerStatsInstance_Type()
)
tmnxMcWppPeerStatsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsInstance.setStatus("current")
_TmnxMcWppPeerStatsLastChanged_Type = TimeStamp
_TmnxMcWppPeerStatsLastChanged_Object = MibTableColumn
tmnxMcWppPeerStatsLastChanged = _TmnxMcWppPeerStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 51, 1, 2),
    _TmnxMcWppPeerStatsLastChanged_Type()
)
tmnxMcWppPeerStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsLastChanged.setStatus("current")


class _TmnxMcWppPeerStatsName_Type(DisplayString):
    """Custom type tmnxMcWppPeerStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxMcWppPeerStatsName_Type.__name__ = "DisplayString"
_TmnxMcWppPeerStatsName_Object = MibTableColumn
tmnxMcWppPeerStatsName = _TmnxMcWppPeerStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 51, 1, 3),
    _TmnxMcWppPeerStatsName_Type()
)
tmnxMcWppPeerStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsName.setStatus("current")
_TmnxMcWppPeerStatsVal_Type = Counter32
_TmnxMcWppPeerStatsVal_Object = MibTableColumn
tmnxMcWppPeerStatsVal = _TmnxMcWppPeerStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 2, 51, 1, 4),
    _TmnxMcWppPeerStatsVal_Type()
)
tmnxMcWppPeerStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcWppPeerStatsVal.setStatus("current")
_TmnxMcRedundancyNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyNotifyObjs = _TmnxMcRedundancyNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3)
)
_TmnxMcPeerIpAddrTypeForNotify_Type = InetAddressType
_TmnxMcPeerIpAddrTypeForNotify_Object = MibScalar
tmnxMcPeerIpAddrTypeForNotify = _TmnxMcPeerIpAddrTypeForNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 1),
    _TmnxMcPeerIpAddrTypeForNotify_Type()
)
tmnxMcPeerIpAddrTypeForNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPeerIpAddrTypeForNotify.setStatus("current")
_TmnxMcPeerIpAddrForNotify_Type = InetAddress
_TmnxMcPeerIpAddrForNotify_Object = MibScalar
tmnxMcPeerIpAddrForNotify = _TmnxMcPeerIpAddrForNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 2),
    _TmnxMcPeerIpAddrForNotify_Type()
)
tmnxMcPeerIpAddrForNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPeerIpAddrForNotify.setStatus("current")
_TmnxMcPeerSyncClient_Type = TmnxMcsClientApp
_TmnxMcPeerSyncClient_Object = MibScalar
tmnxMcPeerSyncClient = _TmnxMcPeerSyncClient_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 3),
    _TmnxMcPeerSyncClient_Type()
)
tmnxMcPeerSyncClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPeerSyncClient.setStatus("current")
_TmnxMcRemoteGrpIfNameForNotify_Type = TNamedItem
_TmnxMcRemoteGrpIfNameForNotify_Object = MibScalar
tmnxMcRemoteGrpIfNameForNotify = _TmnxMcRemoteGrpIfNameForNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 4),
    _TmnxMcRemoteGrpIfNameForNotify_Type()
)
tmnxMcRemoteGrpIfNameForNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcRemoteGrpIfNameForNotify.setStatus("current")
_TmnxMcRemoteRedIfNameForNotify_Type = TNamedItem
_TmnxMcRemoteRedIfNameForNotify_Object = MibScalar
tmnxMcRemoteRedIfNameForNotify = _TmnxMcRemoteRedIfNameForNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 5),
    _TmnxMcRemoteRedIfNameForNotify_Type()
)
tmnxMcRemoteRedIfNameForNotify.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcRemoteRedIfNameForNotify.setStatus("current")
_TmnxMcRemoteSyncTag_Type = TNamedItem
_TmnxMcRemoteSyncTag_Object = MibScalar
tmnxMcRemoteSyncTag = _TmnxMcRemoteSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 6),
    _TmnxMcRemoteSyncTag_Type()
)
tmnxMcRemoteSyncTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcRemoteSyncTag.setStatus("current")


class _TmnxMcLagConfigLagIds_Type(OctetString):
    """Custom type tmnxMcLagConfigLagIds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25


_TmnxMcLagConfigLagIds_Type.__name__ = "OctetString"
_TmnxMcLagConfigLagIds_Object = MibScalar
tmnxMcLagConfigLagIds = _TmnxMcLagConfigLagIds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 7),
    _TmnxMcLagConfigLagIds_Type()
)
tmnxMcLagConfigLagIds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcLagConfigLagIds.setStatus("current")


class _TmnxMcPeerClockSkew_Type(Unsigned32):
    """Custom type tmnxMcPeerClockSkew based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxMcPeerClockSkew_Type.__name__ = "Unsigned32"
_TmnxMcPeerClockSkew_Object = MibScalar
tmnxMcPeerClockSkew = _TmnxMcPeerClockSkew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 8),
    _TmnxMcPeerClockSkew_Type()
)
tmnxMcPeerClockSkew.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPeerClockSkew.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerClockSkew.setUnits("seconds")
_TmnxSrrpNotifBfdIntfSvcId_Type = TmnxServId
_TmnxSrrpNotifBfdIntfSvcId_Object = MibScalar
tmnxSrrpNotifBfdIntfSvcId = _TmnxSrrpNotifBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 9),
    _TmnxSrrpNotifBfdIntfSvcId_Type()
)
tmnxSrrpNotifBfdIntfSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSrrpNotifBfdIntfSvcId.setStatus("current")
_TmnxSrrpNotifBfdIntfIfName_Type = TNamedItem
_TmnxSrrpNotifBfdIntfIfName_Object = MibScalar
tmnxSrrpNotifBfdIntfIfName = _TmnxSrrpNotifBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 10),
    _TmnxSrrpNotifBfdIntfIfName_Type()
)
tmnxSrrpNotifBfdIntfIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSrrpNotifBfdIntfIfName.setStatus("current")
_TmnxSrrpNotifBfdIntfDestIpType_Type = InetAddressType
_TmnxSrrpNotifBfdIntfDestIpType_Object = MibScalar
tmnxSrrpNotifBfdIntfDestIpType = _TmnxSrrpNotifBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 11),
    _TmnxSrrpNotifBfdIntfDestIpType_Type()
)
tmnxSrrpNotifBfdIntfDestIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSrrpNotifBfdIntfDestIpType.setStatus("current")


class _TmnxSrrpNotifBfdIntfDestIp_Type(InetAddress):
    """Custom type tmnxSrrpNotifBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxSrrpNotifBfdIntfDestIp_Type.__name__ = "InetAddress"
_TmnxSrrpNotifBfdIntfDestIp_Object = MibScalar
tmnxSrrpNotifBfdIntfDestIp = _TmnxSrrpNotifBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 12),
    _TmnxSrrpNotifBfdIntfDestIp_Type()
)
tmnxSrrpNotifBfdIntfDestIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSrrpNotifBfdIntfDestIp.setStatus("current")
_TmnxSrrpNotifBfdIntfSessState_Type = TmnxSrrpAssoBfdIntfSessOperState
_TmnxSrrpNotifBfdIntfSessState_Object = MibScalar
tmnxSrrpNotifBfdIntfSessState = _TmnxSrrpNotifBfdIntfSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 13),
    _TmnxSrrpNotifBfdIntfSessState_Type()
)
tmnxSrrpNotifBfdIntfSessState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSrrpNotifBfdIntfSessState.setStatus("current")


class _TmnxMcPeerEPBfdSessionOpenStatus_Type(Integer32):
    """Custom type tmnxMcPeerEPBfdSessionOpenStatus based on Integer32"""
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
        *(("ok", 0),
          ("invalidSrcAddr", 1),
          ("nonSysLoopbackIf", 2),
          ("clientUseSessionFail", 3),
          ("clientAppUseIfFail", 4))
    )


_TmnxMcPeerEPBfdSessionOpenStatus_Type.__name__ = "Integer32"
_TmnxMcPeerEPBfdSessionOpenStatus_Object = MibScalar
tmnxMcPeerEPBfdSessionOpenStatus = _TmnxMcPeerEPBfdSessionOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 14),
    _TmnxMcPeerEPBfdSessionOpenStatus_Type()
)
tmnxMcPeerEPBfdSessionOpenStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPeerEPBfdSessionOpenStatus.setStatus("current")


class _TmnxMcPeerEPPsvModeConfigState_Type(Integer32):
    """Custom type tmnxMcPeerEPPsvModeConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 1),
          ("mismatchResolved", 2))
    )


_TmnxMcPeerEPPsvModeConfigState_Type.__name__ = "Integer32"
_TmnxMcPeerEPPsvModeConfigState_Object = MibScalar
tmnxMcPeerEPPsvModeConfigState = _TmnxMcPeerEPPsvModeConfigState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 15),
    _TmnxMcPeerEPPsvModeConfigState_Type()
)
tmnxMcPeerEPPsvModeConfigState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcPeerEPPsvModeConfigState.setStatus("current")
_TMcPeerIPsecTnlGrpMasterStateOld_Type = TMcPeerIPsecTnlGrpMasterState
_TMcPeerIPsecTnlGrpMasterStateOld_Object = MibScalar
tMcPeerIPsecTnlGrpMasterStateOld = _TMcPeerIPsecTnlGrpMasterStateOld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 16),
    _TMcPeerIPsecTnlGrpMasterStateOld_Type()
)
tMcPeerIPsecTnlGrpMasterStateOld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpMasterStateOld.setStatus("current")
_TmnxMcNotifyNumber_Type = Unsigned32
_TmnxMcNotifyNumber_Object = MibScalar
tmnxMcNotifyNumber = _TmnxMcNotifyNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 3, 17),
    _TmnxMcNotifyNumber_Type()
)
tmnxMcNotifyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMcNotifyNumber.setStatus("current")
_TmnxMcMobRedundancyObjs_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyObjs = _TmnxMcMobRedundancyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4)
)
_TmnxMcPeerMobileTableLstChgd_Type = TimeStamp
_TmnxMcPeerMobileTableLstChgd_Object = MibScalar
tmnxMcPeerMobileTableLstChgd = _TmnxMcPeerMobileTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 1),
    _TmnxMcPeerMobileTableLstChgd_Type()
)
tmnxMcPeerMobileTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileTableLstChgd.setStatus("current")
_TmnxMcPeerMobileTable_Object = MibTable
tmnxMcPeerMobileTable = _TmnxMcPeerMobileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxMcPeerMobileTable.setStatus("current")
_TmnxMcPeerMobileEntry_Object = MibTableRow
tmnxMcPeerMobileEntry = _TmnxMcPeerMobileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1)
)
tmnxMcPeerMobileEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerMobileEntry.setStatus("current")
_TmnxMcPeerMobileRowStatus_Type = RowStatus
_TmnxMcPeerMobileRowStatus_Object = MibTableColumn
tmnxMcPeerMobileRowStatus = _TmnxMcPeerMobileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 1),
    _TmnxMcPeerMobileRowStatus_Type()
)
tmnxMcPeerMobileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileRowStatus.setStatus("current")


class _TmnxMcPeerMobileBFDEnable_Type(TruthValue):
    """Custom type tmnxMcPeerMobileBFDEnable based on TruthValue"""
    defaultValue = 2


_TmnxMcPeerMobileBFDEnable_Type.__name__ = "TruthValue"
_TmnxMcPeerMobileBFDEnable_Object = MibTableColumn
tmnxMcPeerMobileBFDEnable = _TmnxMcPeerMobileBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 2),
    _TmnxMcPeerMobileBFDEnable_Type()
)
tmnxMcPeerMobileBFDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileBFDEnable.setStatus("current")


class _TmnxMcPeerMobileRouteAdvHoldTmr_Type(Unsigned32):
    """Custom type tmnxMcPeerMobileRouteAdvHoldTmr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 5000),
    )


_TmnxMcPeerMobileRouteAdvHoldTmr_Type.__name__ = "Unsigned32"
_TmnxMcPeerMobileRouteAdvHoldTmr_Object = MibTableColumn
tmnxMcPeerMobileRouteAdvHoldTmr = _TmnxMcPeerMobileRouteAdvHoldTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 3),
    _TmnxMcPeerMobileRouteAdvHoldTmr_Type()
)
tmnxMcPeerMobileRouteAdvHoldTmr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileRouteAdvHoldTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileRouteAdvHoldTmr.setUnits("milliseconds")


class _TmnxMcPeerMobileHoldOnNbrFail_Type(Unsigned32):
    """Custom type tmnxMcPeerMobileHoldOnNbrFail based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 25),
    )


_TmnxMcPeerMobileHoldOnNbrFail_Type.__name__ = "Unsigned32"
_TmnxMcPeerMobileHoldOnNbrFail_Object = MibTableColumn
tmnxMcPeerMobileHoldOnNbrFail = _TmnxMcPeerMobileHoldOnNbrFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 4),
    _TmnxMcPeerMobileHoldOnNbrFail_Type()
)
tmnxMcPeerMobileHoldOnNbrFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileHoldOnNbrFail.setStatus("current")


class _TmnxMcPeerMobileKeepAlvIntvl_Type(Unsigned32):
    """Custom type tmnxMcPeerMobileKeepAlvIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_TmnxMcPeerMobileKeepAlvIntvl_Type.__name__ = "Unsigned32"
_TmnxMcPeerMobileKeepAlvIntvl_Object = MibTableColumn
tmnxMcPeerMobileKeepAlvIntvl = _TmnxMcPeerMobileKeepAlvIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 5),
    _TmnxMcPeerMobileKeepAlvIntvl_Type()
)
tmnxMcPeerMobileKeepAlvIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileKeepAlvIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileKeepAlvIntvl.setUnits("deci-seconds")


class _TmnxMcPeerMobileHoldDownTmr_Type(Unsigned32):
    """Custom type tmnxMcPeerMobileHoldDownTmr based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxMcPeerMobileHoldDownTmr_Type.__name__ = "Unsigned32"
_TmnxMcPeerMobileHoldDownTmr_Object = MibTableColumn
tmnxMcPeerMobileHoldDownTmr = _TmnxMcPeerMobileHoldDownTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 6),
    _TmnxMcPeerMobileHoldDownTmr_Type()
)
tmnxMcPeerMobileHoldDownTmr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileHoldDownTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileHoldDownTmr.setUnits("seconds")


class _TmnxMcPeerMobileAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcPeerMobileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcPeerMobileAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcPeerMobileAdminState_Object = MibTableColumn
tmnxMcPeerMobileAdminState = _TmnxMcPeerMobileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 7),
    _TmnxMcPeerMobileAdminState_Type()
)
tmnxMcPeerMobileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileAdminState.setStatus("current")
_TmnxMcPeerMobileLastChanged_Type = TimeStamp
_TmnxMcPeerMobileLastChanged_Object = MibTableColumn
tmnxMcPeerMobileLastChanged = _TmnxMcPeerMobileLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 8),
    _TmnxMcPeerMobileLastChanged_Type()
)
tmnxMcPeerMobileLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileLastChanged.setStatus("current")


class _TmnxMcPeerMobileMtu_Type(Unsigned32):
    """Custom type tmnxMcPeerMobileMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9212),
    )


_TmnxMcPeerMobileMtu_Type.__name__ = "Unsigned32"
_TmnxMcPeerMobileMtu_Object = MibTableColumn
tmnxMcPeerMobileMtu = _TmnxMcPeerMobileMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 2, 1, 9),
    _TmnxMcPeerMobileMtu_Type()
)
tmnxMcPeerMobileMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMtu.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMtu.setUnits("bytes")
_TmnxMcPeerMobileMGTableLstChgd_Type = TimeStamp
_TmnxMcPeerMobileMGTableLstChgd_Object = MibScalar
tmnxMcPeerMobileMGTableLstChgd = _TmnxMcPeerMobileMGTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 3),
    _TmnxMcPeerMobileMGTableLstChgd_Type()
)
tmnxMcPeerMobileMGTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGTableLstChgd.setStatus("current")
_TmnxMcPeerMobileMGTable_Object = MibTable
tmnxMcPeerMobileMGTable = _TmnxMcPeerMobileMGTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGTable.setStatus("current")
_TmnxMcPeerMobileMGEntry_Object = MibTableRow
tmnxMcPeerMobileMGEntry = _TmnxMcPeerMobileMGEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1)
)
tmnxMcPeerMobileMGEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGId"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGEntry.setStatus("current")
_TmnxMcPeerMobileMGRowStatus_Type = RowStatus
_TmnxMcPeerMobileMGRowStatus_Object = MibTableColumn
tmnxMcPeerMobileMGRowStatus = _TmnxMcPeerMobileMGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1, 1),
    _TmnxMcPeerMobileMGRowStatus_Type()
)
tmnxMcPeerMobileMGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRowStatus.setStatus("current")
_TmnxMcPeerMobileMGId_Type = TmnxMobGwId
_TmnxMcPeerMobileMGId_Object = MibTableColumn
tmnxMcPeerMobileMGId = _TmnxMcPeerMobileMGId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1, 2),
    _TmnxMcPeerMobileMGId_Type()
)
tmnxMcPeerMobileMGId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGId.setStatus("current")


class _TmnxMcPeerMobileMGRole_Type(Integer32):
    """Custom type tmnxMcPeerMobileMGRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_TmnxMcPeerMobileMGRole_Type.__name__ = "Integer32"
_TmnxMcPeerMobileMGRole_Object = MibTableColumn
tmnxMcPeerMobileMGRole = _TmnxMcPeerMobileMGRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1, 3),
    _TmnxMcPeerMobileMGRole_Type()
)
tmnxMcPeerMobileMGRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRole.setStatus("current")


class _TmnxMcPeerMobileMGRefPtTrigger_Type(Integer32):
    """Custom type tmnxMcPeerMobileMGRefPtTrigger based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_TmnxMcPeerMobileMGRefPtTrigger_Type.__name__ = "Integer32"
_TmnxMcPeerMobileMGRefPtTrigger_Object = MibTableColumn
tmnxMcPeerMobileMGRefPtTrigger = _TmnxMcPeerMobileMGRefPtTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1, 4),
    _TmnxMcPeerMobileMGRefPtTrigger_Type()
)
tmnxMcPeerMobileMGRefPtTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPtTrigger.setStatus("current")


class _TmnxMcPeerMobileMGAdminState_Type(TmnxAdminState):
    """Custom type tmnxMcPeerMobileMGAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMcPeerMobileMGAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMcPeerMobileMGAdminState_Object = MibTableColumn
tmnxMcPeerMobileMGAdminState = _TmnxMcPeerMobileMGAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1, 5),
    _TmnxMcPeerMobileMGAdminState_Type()
)
tmnxMcPeerMobileMGAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGAdminState.setStatus("current")
_TmnxMcPeerMobileMGLastChanged_Type = TimeStamp
_TmnxMcPeerMobileMGLastChanged_Object = MibTableColumn
tmnxMcPeerMobileMGLastChanged = _TmnxMcPeerMobileMGLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 4, 1, 6),
    _TmnxMcPeerMobileMGLastChanged_Type()
)
tmnxMcPeerMobileMGLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGLastChanged.setStatus("current")
_TmnxMcPeerMobMGRefPtTableLstChgd_Type = TimeStamp
_TmnxMcPeerMobMGRefPtTableLstChgd_Object = MibScalar
tmnxMcPeerMobMGRefPtTableLstChgd = _TmnxMcPeerMobMGRefPtTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 5),
    _TmnxMcPeerMobMGRefPtTableLstChgd_Type()
)
tmnxMcPeerMobMGRefPtTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerMobMGRefPtTableLstChgd.setStatus("current")
_TmnxMcPeerMobileMGRefPtTable_Object = MibTable
tmnxMcPeerMobileMGRefPtTable = _TmnxMcPeerMobileMGRefPtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPtTable.setStatus("current")
_TmnxMcPeerMobileMGRefPtEntry_Object = MibTableRow
tmnxMcPeerMobileMGRefPtEntry = _TmnxMcPeerMobileMGRefPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 6, 1)
)
tmnxMcPeerMobileMGRefPtEntry.setIndexNames(
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpType"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddr"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGId"),
    (0, "TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRefPt"),
)
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPtEntry.setStatus("current")
_TmnxMcPeerMobileMGRefPtRowStatus_Type = RowStatus
_TmnxMcPeerMobileMGRefPtRowStatus_Object = MibTableColumn
tmnxMcPeerMobileMGRefPtRowStatus = _TmnxMcPeerMobileMGRefPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 6, 1, 1),
    _TmnxMcPeerMobileMGRefPtRowStatus_Type()
)
tmnxMcPeerMobileMGRefPtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPtRowStatus.setStatus("current")


class _TmnxMcPeerMobileMGRefPt_Type(Integer32):
    """Custom type tmnxMcPeerMobileMGRefPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s11", 1),
          ("s1u", 2),
          ("s5s8", 3))
    )


_TmnxMcPeerMobileMGRefPt_Type.__name__ = "Integer32"
_TmnxMcPeerMobileMGRefPt_Object = MibTableColumn
tmnxMcPeerMobileMGRefPt = _TmnxMcPeerMobileMGRefPt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 6, 1, 2),
    _TmnxMcPeerMobileMGRefPt_Type()
)
tmnxMcPeerMobileMGRefPt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPt.setStatus("current")


class _TmnxMcPeerMobileMGRefPtPktCnt_Type(Unsigned32):
    """Custom type tmnxMcPeerMobileMGRefPtPktCnt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TmnxMcPeerMobileMGRefPtPktCnt_Type.__name__ = "Unsigned32"
_TmnxMcPeerMobileMGRefPtPktCnt_Object = MibTableColumn
tmnxMcPeerMobileMGRefPtPktCnt = _TmnxMcPeerMobileMGRefPtPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 6, 1, 3),
    _TmnxMcPeerMobileMGRefPtPktCnt_Type()
)
tmnxMcPeerMobileMGRefPtPktCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPtPktCnt.setStatus("current")
_TmnxMcPeerMobileMGRefPtLastChngd_Type = TimeStamp
_TmnxMcPeerMobileMGRefPtLastChngd_Object = MibTableColumn
tmnxMcPeerMobileMGRefPtLastChngd = _TmnxMcPeerMobileMGRefPtLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 4, 6, 1, 4),
    _TmnxMcPeerMobileMGRefPtLastChngd_Type()
)
tmnxMcPeerMobileMGRefPtLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMcPeerMobileMGRefPtLastChngd.setStatus("current")
_TmnxMcMobRedundancyStatsObjs_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyStatsObjs = _TmnxMcMobRedundancyStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 5)
)
_TmnxMcMobRedundancyNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyNotifyObjs = _TmnxMcMobRedundancyNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 40, 6)
)
_TmnxMcRedundancyNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyNotifyPrefix = _TmnxMcRedundancyNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40)
)
_TmnxMcRedundancyNotifications_ObjectIdentity = ObjectIdentity
tmnxMcRedundancyNotifications = _TmnxMcRedundancyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0)
)
_TmnxMcMobRedundancyNotifications_ObjectIdentity = ObjectIdentity
tmnxMcMobRedundancyNotifications = _TmnxMcMobRedundancyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 1)
)
tmnxMcLagConfigLagEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tmnxMcLagInfoLagEntry")
)
tmnxMcLagInfoLagEntry.setIndexNames(*tmnxMcLagConfigLagEntry.getIndexNames())
tmnxMcRingEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tmnxMcRingInfoEntry")
)
tmnxMcRingInfoEntry.setIndexNames(*tmnxMcRingEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tmnxMcTlsCfgEntry")
)
tmnxMcTlsCfgEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())
tMcPeerIPsecTnlGrpEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tMcPeerTnlGrpStatEntry")
)
tMcPeerTnlGrpStatEntry.setIndexNames(*tMcPeerIPsecTnlGrpEntry.getIndexNames())
tmnxMcPeerEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tmnxMcrPeerStatsEntry")
)
tmnxMcrPeerStatsEntry.setIndexNames(*tmnxMcPeerEntry.getIndexNames())
tmnxMcRingEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tmnxMcrRingStatsEntry")
)
tmnxMcrRingStatsEntry.setIndexNames(*tmnxMcRingEntry.getIndexNames())
tmnxMcRingNodeEntry.registerAugmentions(
    ("TIMETRA-MC-REDUNDANCY-MIB",
     "tmnxMcrRingNodeStatsEntry")
)
tmnxMcrRingNodeStatsEntry.setIndexNames(*tmnxMcRingNodeEntry.getIndexNames())

# Managed Objects groups

tmnxMcRedundancyV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 1)
)
tmnxMcRedundancyV5v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerDescription"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerAuthKey"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpOperType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpOperAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRingsOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIgmp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIgmpSnooping"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSubMgmt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSrrp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncLastSyncTime"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncLclDeletedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemLclDelEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxAll"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxHello"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxData"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxOther"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxErr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxAll"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxHello"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxData"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxOther"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrHeader"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrBody"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrSeqNum"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncClient"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientLclDeletedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemLclDelEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerAdminstate"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigKeepALiveIvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigHoldOnNgbrFailure"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLaglacpKey"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSystemId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSystemPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagRemoteLagId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagActiveStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLacpIdInUse"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagExtendedTimeOut"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagSelectionLogic"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchString"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagIds"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktKpaliveTask"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktTooShort"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktVerifyFaild"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropTlvInvalidSize"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropTlvInvldLagId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropUnknownPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropStateDsbld"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropPktTooShrt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropTlvInvldSz"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropTlvInvldId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxFailed"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyV5v0Group.setStatus("obsolete")

tmnxSrrpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 2)
)
tmnxSrrpV5v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperDescription"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperGwMac"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperGwOperMac"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperInUsePriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMasterPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperKeepAliveInterval"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMsgPathSapPortId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMsgPathSapEncapVal"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMasterSince"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperVrrpPolicy1"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperVrrpPolicy2"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMasterDownInterval"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMasterDownTimer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsBecomeMaster"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsMasterChanges"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsAdvSent"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsAdvRcvd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsPriZeroPktsSent"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsPriZeroPktsRcvd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsPreemptEvents"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsPreemptedEvents"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsAdvIntDiscards"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsAdvIntErrors"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsBecomeBackupRouting"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsBecomeBackupShunt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpStatsBecomeNonMaster"))
)
if mibBuilder.loadTexts:
    tmnxSrrpV5v0Group.setStatus("current")

tmnxMcRedundancyNotifyObjsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 3)
)
tmnxMcRedundancyNotifyObjsV5v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncClient"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteGrpIfNameForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteRedIfNameForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagIds"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerClockSkew"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyNotifyObjsV5v0Group.setStatus("current")

tmnxMcRingV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 4)
)
tmnxMcRingV6v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncMcRing"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlSvcId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlIfName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlDestIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlDestIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingVlanMap"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingVlanMapExcl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlDbMax"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlDbAdmin"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoFailureReason"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlSrcIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlDbStart"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlDbTime"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlDbGuard"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoPortId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoVlanMap"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoVlanMapExcl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoCtrlVlanMap"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvSvcId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvEncapValue"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvSrcIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvDestIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvDestIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvInterval"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeRncvSrcMac"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoTableLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoLocOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoRemOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoInUse"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoFailureReason"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsCfgTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsCfgLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsCfgDefGwIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsCfgDefGwIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsCfgDefGwMac"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpipeSapTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpipeSapRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpipeSapLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpipeSapRingNodeName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsRxMcsIdReq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsRxMcsIdRsp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsRxRingExistsReq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsRxRingExistsRsp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsRxKeepAlive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTxMcsIdReq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTxMcsIdRsp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTxRingExistsReq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTxRingExistsRsp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrPeerStatsTxKeepAlive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsRxSapsChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsTxSapsChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsRxOpaqueDelivrd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsRxOpaqueNoDest"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingStatsTxOpaque"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxTooShort"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxWrongAuth"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxInvalidTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxIncomplete"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxUnknownType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxUnknownPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxUnknownRing"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxUnknownRingNode"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxDelivrdToPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxDelivrdToRing"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsRxDelivrdToRingNode"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsTxNoBuffer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsTxTransmitFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsMissedConfigEvent"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsMissedBfdEvent"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrStatsTxUnknownDest"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsRxDetect"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsRxDetectAck"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsRncvRxResp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsTxDetect"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsTxDetectAck"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsRncvTxReq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcrRingNodeStatsRncvRtTime"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingDbTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingDbTableSize"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingDbTime"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingDbOperState"))
)
if mibBuilder.loadTexts:
    tmnxMcRingV6v0Group.setStatus("current")

tmnxMcPeerSyncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 5)
)
tmnxMcPeerSyncGroup.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncMldSnooping")
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncGroup.setStatus("current")

tmnxMcsDhcpsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 6)
)
tmnxMcsDhcpsV6v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsTableLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPeerIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPeerIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncDhcpServer"))
)
if mibBuilder.loadTexts:
    tmnxMcsDhcpsV6v0Group.setStatus("current")

tmnxMcRedundancyV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 7)
)
tmnxMcRedundancyV6v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerDescription"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerAuthKey"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpOperType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpOperAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRingsOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIgmp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIgmpSnooping"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSubMgmt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSrrp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncLastSyncTime"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncLclDeletedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemLclDelEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxAll"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxHello"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxData"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxOther"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxErr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxAll"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxHello"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxData"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxOther"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrHeader"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrBody"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrSeqNum"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientLclDeletedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemLclDelEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerAdminstate"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigKeepALiveIvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigHoldOnNgbrFailure"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerLastStateChge"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLaglacpKey"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSystemId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSystemPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagRemoteLagId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagActiveStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLacpIdInUse"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagExtendedTimeOut"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagSelectionLogic"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchString"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktKpaliveTask"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktTooShort"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktVerifyFaild"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropTlvInvalidSize"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropTlvInvldLagId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropUnknownPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropStateDsbld"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropPktTooShrt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropTlvInvldSz"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropTlvInvldId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxFailed"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyV6v0Group.setStatus("obsolete")

tmnxSrrpV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 8)
)
tmnxSrrpV6v1Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfTblLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfSrcIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpAssoBfdIntfSessOperState"))
)
if mibBuilder.loadTexts:
    tmnxSrrpV6v1Group.setStatus("current")

tmnxSrrpNotificationObjV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 9)
)
tmnxSrrpNotificationObjV6v1Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfSvcId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfIfName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfDestIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfDestIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfSessState"))
)
if mibBuilder.loadTexts:
    tmnxSrrpNotificationObjV6v1Group.setStatus("current")

tmnxMcL3RingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 10)
)
tmnxMcL3RingGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingSrrpLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingSrrpRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingSrrpTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMcL3RingGroup.setStatus("current")

tmnxMcPeerEPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 11)
)
tmnxMcPeerEPGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBootTimer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPHoldOnNbrFail"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPKeepAliveIntvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPassiveMode"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPassiveModeOper"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPRefCount"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPSysPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropPktTooShrt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropStateDsbld"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropTlvInvldId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropTlvInvldSz"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsRxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsRxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsTxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsPktsTxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEPPeerStatsDropEpNoPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPeerLastStateChge"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropEpNoPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropPktKpaliveTask"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropPktTooShort"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropPktVerifyFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropTlvInvalidSize"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropTlvInvldEpId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropUnknownPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsRxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsRxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsTxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsTxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcEpStatsPktsTxState"))
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPGroup.setStatus("current")

tmnxMcPeerEPNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 12)
)
tmnxMcPeerEPNotifyObjsV7v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfdSessionOpenStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPsvModeConfigState"))
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPNotifyObjsV7v0Group.setStatus("current")

tmnxMcsSubHostTrkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 13)
)
tmnxMcsSubHostTrkGroup.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSubHostTrk")
)
if mibBuilder.loadTexts:
    tmnxMcsSubHostTrkGroup.setStatus("current")

tmnxMcLagPbbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 14)
)
tmnxMcLagPbbGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSrcBMacLSB"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagOperSrcBMacLSB"))
)
if mibBuilder.loadTexts:
    tmnxMcLagPbbGroup.setStatus("current")

tmnxMcRedBgpMultiHomeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 15)
)
tmnxMcRedBgpMultiHomeGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeBootTimer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeSiteTimer"))
)
if mibBuilder.loadTexts:
    tmnxMcRedBgpMultiHomeGroup.setStatus("current")

tmnxMcTlsSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 16)
)
tmnxMcTlsSapGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapRingNodeName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMcTlsSapGroup.setStatus("current")

tmnxSrrpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 17)
)
tmnxSrrpV8v0Group.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperSendFibPopulation")
)
if mibBuilder.loadTexts:
    tmnxSrrpV8v0Group.setStatus("current")

tmnxSrrpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 18)
)
tmnxSrrpV9v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperMonitorOperGrp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperOneGarpPerSap"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperPreempt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperPriorityStep"))
)
if mibBuilder.loadTexts:
    tmnxSrrpV9v0Group.setStatus("current")

tmnxMcRedundancyV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 19)
)
tmnxMcRedundancyV9v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerDescription"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerAuthKey"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpOperType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpOperAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRingsOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIgmp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIgmpSnooping"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSubMgmt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSrrp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncLastSyncTime"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncLclDeletedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemLclDelEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncRemAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxAll"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxHello"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxData"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxOther"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsTxErr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxAll"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxHello"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxData"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxOther"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrHeader"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrBody"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPktsRxErrSeqNum"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientLclDeletedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemLclDelEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientRemAlarmedEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerAdminstate"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigKeepALiveIvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigHoldOnNgbrFailure"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigPeerLastStateChge"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagTableLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLaglacpKey"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSystemId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagSystemPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagRemoteLagId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagActiveStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLacpIdInUse"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagExtendedTimeOut"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagSelectionLogic"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchString"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktKpaliveTask"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktTooShort"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropPktVerifyFaild"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropTlvInvalidSize"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropTlvInvldLagId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsDropUnknownPeer"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxKeepalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxPeerConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropStateDsbld"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropPktTooShrt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropTlvInvldSz"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropTlvInvldId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropOutOfSeq"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropUnknownTlv"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsDropMD5"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTx"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxKpalive"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxPeerCfg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPeerStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsRxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsRxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxConfig"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagLagStatsPktsTxFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncSubMgmtPppoe"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyV9v0Group.setStatus("current")

tmnxMcRedundancyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 20)
)
tmnxMcRedundancyV10v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsTnlGrpTblLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsTnlGrpRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsTnlGrpSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncIpsec"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecDiscoveryIntvlBoot"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecDiscoveryIntvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecBfdEnable"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecBfdEnableSvc"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecBfdIntfDestIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecBfdIntfDestIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecBfdIntfIfName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpPeerGrpId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpPreempt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpPriority"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpTblLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpMasterState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpReason"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpForceSwitch"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecHoldOnNgbrFail"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecKeepAliveIntvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpProtectStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTblLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatDynInstalled"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatDynInstalling"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatDynAwaitConf"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatDynFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatInstalled"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatInstalling"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatAwaitConf"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerTnlGrpStatFailed"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyV10v0Group.setStatus("current")

tmnxMcsDhcpsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 21)
)
tmnxMcsDhcpsV11v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPoolTableLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPoolRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPoolPeerIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPoolPeerIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsPoolSyncTag"))
)
if mibBuilder.loadTexts:
    tmnxMcsDhcpsV11v0Group.setStatus("current")

tmnxMcPeerNotifyObjsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 22)
)
tmnxMcPeerNotifyObjsV10v0Group.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpMasterStateOld")
)
if mibBuilder.loadTexts:
    tmnxMcPeerNotifyObjsV10v0Group.setStatus("current")

tmnxMcPeerIPsecTnlGrpV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 23)
)
tmnxMcPeerIPsecTnlGrpV10v0Group.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpForceSwitchTo")
)
if mibBuilder.loadTexts:
    tmnxMcPeerIPsecTnlGrpV10v0Group.setStatus("current")

tmnxMcWarmStandbyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 24)
)
tmnxMcWarmStandbyGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerWarmStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRemoteWarmStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatFailure"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatNumFailedEntries"))
)
if mibBuilder.loadTexts:
    tmnxMcWarmStandbyGroup.setStatus("current")

tmnxMcRedundancyV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 25)
)
tmnxMcRedundancyV12v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcWppPeerStatsTableLastCh"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcWppPeerStatsLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcWppPeerStatsName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcWppPeerStatsVal"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOmcrStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOmcrAlarmed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOmcrRemStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncOmcrRemAlarmed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientOmcrStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientOmcrAlarmed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientOmcrRemStandby"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientOmcrRemAlarmed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncMld"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPythonCache"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyTableLastChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyPeerIpAddrType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyPeerIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyMcsSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsPyPlcyTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyV12v0Group.setStatus("current")

tmnxSrrpV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 26)
)
tmnxSrrpV10v0Group.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperDownReason")
)
if mibBuilder.loadTexts:
    tmnxSrrpV10v0Group.setStatus("current")

tmnxMcRedBgpMHSiteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 29)
)
tmnxMcRedBgpMHSiteGroup.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMHSiteMinDnTimer")
)
if mibBuilder.loadTexts:
    tmnxMcRedBgpMHSiteGroup.setStatus("current")

tmnxMcNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 2, 99)
)
tmnxMcNotifyObjsGroup.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcNotifyNumber")
)
if mibBuilder.loadTexts:
    tmnxMcNotifyObjsGroup.setStatus("current")

tmnxMcMobRedundancyV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 5, 1)
)
tmnxMcMobRedundancyV4v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRefPtPktCnt"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRole"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRefPtTrigger"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileBFDEnable"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileRouteAdvHoldTmr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileHoldOnNbrFail"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileKeepAlvIntvl"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileHoldDownTmr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRefPtRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileRowStatus"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncMobile"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileTableLstChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGTableLstChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobMGRefPtTableLstChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGAdminState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGLastChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMGRefPtLastChngd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerMobileMtu"))
)
if mibBuilder.loadTexts:
    tmnxMcMobRedundancyV4v0Group.setStatus("current")


# Notification objects

tmnxMcRedundancyPeerStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 1)
)
tmnxMcRedundancyPeerStateChanged.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigOperState")
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyPeerStateChanged.setStatus(
        "current"
    )

tmnxMcRedundancyMismatchDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 2)
)
tmnxMcRedundancyMismatchDetected.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchString")
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyMismatchDetected.setStatus(
        "current"
    )

tmnxMcRedundancyMismatchResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 3)
)
tmnxMcRedundancyMismatchResolved.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigMismatchString")
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyMismatchResolved.setStatus(
        "current"
    )

tmnxMcPeerSyncStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 4)
)
tmnxMcPeerSyncStatusChanged.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncStatus")
)
if mibBuilder.loadTexts:
    tmnxMcPeerSyncStatusChanged.setStatus(
        "current"
    )

tmnxMcSyncClientAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 5)
)
tmnxMcSyncClientAlarmRaised.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncClient"))
)
if mibBuilder.loadTexts:
    tmnxMcSyncClientAlarmRaised.setStatus(
        "current"
    )

tmnxMcSyncClientAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 6)
)
tmnxMcSyncClientAlarmCleared.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncClient"))
)
if mibBuilder.loadTexts:
    tmnxMcSyncClientAlarmCleared.setStatus(
        "current"
    )

tmnxSrrpSubnetMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 7)
)
tmnxSrrpSubnetMismatch.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpSubnetMismatch.setStatus(
        "current"
    )

tmnxSrrpSubnetMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 8)
)
tmnxSrrpSubnetMismatchCleared.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpSubnetMismatchCleared.setStatus(
        "current"
    )

tmnxSrrpInstanceIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 9)
)
tmnxSrrpInstanceIdMismatch.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpInstanceIdMismatch.setStatus(
        "current"
    )

tmnxSrrpSapMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 10)
)
tmnxSrrpSapMismatch.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteGrpIfNameForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpSapMismatch.setStatus(
        "current"
    )

tmnxSrrpSapTagMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 11)
)
tmnxSrrpSapTagMismatch.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncPortEncapSyncTag"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteGrpIfNameForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteSyncTag"))
)
if mibBuilder.loadTexts:
    tmnxSrrpSapTagMismatch.setStatus(
        "current"
    )

tmnxSrrpRedIfMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 12)
)
tmnxSrrpRedIfMismatch.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteGrpIfNameForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteRedIfNameForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpRedIfMismatch.setStatus(
        "current"
    )

tmnxSrrpDualMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 13)
)
tmnxSrrpDualMaster.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRemoteGrpIfNameForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpDualMaster.setStatus(
        "current"
    )

tmnxMcLagInfoLagChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 14)
)
tmnxMcLagInfoLagChanged.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagConfigLagIds"))
)
if mibBuilder.loadTexts:
    tmnxMcLagInfoLagChanged.setStatus(
        "current"
    )

tmnxSrrpSystemIpNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 15)
)
if mibBuilder.loadTexts:
    tmnxSrrpSystemIpNotSet.setStatus(
        "current"
    )

tmnxMcRingOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 16)
)
tmnxMcRingOperStateChanged.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoOperState")
)
if mibBuilder.loadTexts:
    tmnxMcRingOperStateChanged.setStatus(
        "current"
    )

tmnxMcRingInbCtrlOperStateChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 17)
)
tmnxMcRingInbCtrlOperStateChgd.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInfoInbCtrlOperState")
)
if mibBuilder.loadTexts:
    tmnxMcRingInbCtrlOperStateChgd.setStatus(
        "current"
    )

tmnxMcRingNodeLocOperStateChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 18)
)
tmnxMcRingNodeLocOperStateChgd.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoLocOperState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeInfoInUse"))
)
if mibBuilder.loadTexts:
    tmnxMcRingNodeLocOperStateChgd.setStatus(
        "current"
    )

tmnxMcSyncClockSkewRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 19)
)
tmnxMcSyncClockSkewRaised.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerClockSkew"))
)
if mibBuilder.loadTexts:
    tmnxMcSyncClockSkewRaised.setStatus(
        "current"
    )

tmnxMcSyncClockSkewCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 20)
)
tmnxMcSyncClockSkewCleared.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerClockSkew"))
)
if mibBuilder.loadTexts:
    tmnxMcSyncClockSkewCleared.setStatus(
        "current"
    )

tmnxSrrpDuplicateSubIfAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 21)
)
tmnxSrrpDuplicateSubIfAddress.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpDuplicateSubIfAddress.setStatus(
        "current"
    )

tmnxMcPeerRingsOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 22)
)
tmnxMcPeerRingsOperStateChanged.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRingsOperState")
)
if mibBuilder.loadTexts:
    tmnxMcPeerRingsOperStateChanged.setStatus(
        "current"
    )

tmnxSrrpTrapNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 23)
)
tmnxSrrpTrapNewMaster.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpTrapNewMaster.setStatus(
        "current"
    )

tmnxSrrpBecameBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 24)
)
tmnxSrrpBecameBackup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperFlags"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrTypeForNotify"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIpAddrForNotify"))
)
if mibBuilder.loadTexts:
    tmnxSrrpBecameBackup.setStatus(
        "current"
    )

tmnxSrrpBfdIntfSessStateChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 25)
)
tmnxSrrpBfdIntfSessStateChgd.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfSvcId"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfIfName"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfDestIpType"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfDestIp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifBfdIntfSessState"))
)
if mibBuilder.loadTexts:
    tmnxSrrpBfdIntfSessStateChgd.setStatus(
        "current"
    )

tmnxMcPeerEPBfdSessionOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 26)
)
tmnxMcPeerEPBfdSessionOpen.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfdSessionOpenStatus"))
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPBfdSessionOpen.setStatus(
        "current"
    )

tmnxMcPeerEPBfdSessionClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 27)
)
tmnxMcPeerEPBfdSessionClose.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPBfdSessionClose.setStatus(
        "current"
    )

tmnxMcPeerEPBfdSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 28)
)
tmnxMcPeerEPBfdSessionUp.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPBfdSessionUp.setStatus(
        "current"
    )

tmnxMcPeerEPBfdSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 29)
)
tmnxMcPeerEPBfdSessionDown.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPBfdSessionDown.setStatus(
        "current"
    )

tmnxMcPeerEPOperDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 30)
)
tmnxMcPeerEPOperDown.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPOperDown.setStatus(
        "current"
    )

tmnxMcPeerEPOperUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 31)
)
tmnxMcPeerEPOperUp.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr")
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPOperUp.setStatus(
        "current"
    )

tmnxMCEPSessionPsvModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 32)
)
tmnxMCEPSessionPsvModeEnabled.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPassiveMode"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPsvModeConfigState"))
)
if mibBuilder.loadTexts:
    tmnxMCEPSessionPsvModeEnabled.setStatus(
        "current"
    )

tmnxMCEPSessionPsvModeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 33)
)
tmnxMCEPSessionPsvModeDisabled.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSrcIpAddr"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPPassiveMode"))
)
if mibBuilder.loadTexts:
    tmnxMCEPSessionPsvModeDisabled.setStatus(
        "current"
    )

tMcPeerIPsecTnlGrpMasterStateChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 34)
)
tMcPeerIPsecTnlGrpMasterStateChg.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpMasterState"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpMasterStateOld"))
)
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpMasterStateChg.setStatus(
        "current"
    )

tMcPeerIPsecTnlGrpProtStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 35)
)
tMcPeerIPsecTnlGrpProtStatusChg.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpProtectStatus")
)
if mibBuilder.loadTexts:
    tMcPeerIPsecTnlGrpProtStatusChg.setStatus(
        "current"
    )

tmnxMcOmcrStatFailedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 37)
)
tmnxMcOmcrStatFailedChanged.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatFailed"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatFailure"))
)
if mibBuilder.loadTexts:
    tmnxMcOmcrStatFailedChanged.setStatus(
        "current"
    )

tmnxMcOmcrClientNumEntriesHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 38)
)
tmnxMcOmcrClientNumEntriesHigh.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsClientNumEntries"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcNotifyNumber"))
)
if mibBuilder.loadTexts:
    tmnxMcOmcrClientNumEntriesHigh.setStatus(
        "current"
    )

tmnxSrrpOperDownInvalidMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 39)
)
tmnxSrrpOperDownInvalidMac.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperState")
)
if mibBuilder.loadTexts:
    tmnxSrrpOperDownInvalidMac.setStatus(
        "current"
    )

tmnxSrrpOperDownInvalidMacClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 40, 0, 40)
)
tmnxSrrpOperDownInvalidMacClear.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperState")
)
if mibBuilder.loadTexts:
    tmnxSrrpOperDownInvalidMacClear.setStatus(
        "current"
    )


# Notifications groups

tmnxMcRedundancyV5v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 1)
)
tmnxMcRedundancyV5v0NotifGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyPeerStateChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyMismatchDetected"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyMismatchResolved"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncStatusChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcSyncClientAlarmRaised"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcSyncClientAlarmCleared"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpSubnetMismatch"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpSubnetMismatchCleared"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpInstanceIdMismatch"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpSapMismatch"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpSapTagMismatch"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpRedIfMismatch"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpDualMaster"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagInfoLagChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpSystemIpNotSet"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcSyncClockSkewRaised"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcSyncClockSkewCleared"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpDuplicateSubIfAddress"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancyV5v0NotifGroup.setStatus(
        "current"
    )

tmnxMcRingV6v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 2)
)
tmnxMcRingV6v0NotifGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingOperStateChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingInbCtrlOperStateChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingNodeLocOperStateChgd"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerRingsOperStateChanged"))
)
if mibBuilder.loadTexts:
    tmnxMcRingV6v0NotifGroup.setStatus(
        "current"
    )

tmnxMcRedundancySrrpNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 3)
)
tmnxMcRedundancySrrpNotifGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpTrapNewMaster"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpBecameBackup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancySrrpNotifGroup.setStatus(
        "current"
    )

tmnxSrrpNotifV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 4)
)
tmnxSrrpNotifV6v1Group.setObjects(
    ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpBfdIntfSessStateChgd")
)
if mibBuilder.loadTexts:
    tmnxSrrpNotifV6v1Group.setStatus(
        "current"
    )

tmnxMcPeerEPV7v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 5)
)
tmnxMcPeerEPV7v0NotifGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMCEPSessionPsvModeDisabled"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMCEPSessionPsvModeEnabled"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfdSessionClose"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfdSessionOpen"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfdSessionDown"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPBfdSessionUp"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPOperDown"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPOperUp"))
)
if mibBuilder.loadTexts:
    tmnxMcPeerEPV7v0NotifGroup.setStatus(
        "current"
    )

tmnxMcPeerV10v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 6)
)
tmnxMcPeerV10v0NotifGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpProtStatusChg"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tMcPeerIPsecTnlGrpMasterStateChg"))
)
if mibBuilder.loadTexts:
    tmnxMcPeerV10v0NotifGroup.setStatus(
        "current"
    )

tmnxMcOmcrNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 7)
)
tmnxMcOmcrNotifGroup.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrStatFailedChanged"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrClientNumEntriesHigh"))
)
if mibBuilder.loadTexts:
    tmnxMcOmcrNotifGroup.setStatus(
        "current"
    )

tmnxSrrpNotificationV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 3, 8)
)
tmnxSrrpNotificationV10v0Group.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperDownInvalidMac"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpOperDownInvalidMacClear"))
)
if mibBuilder.loadTexts:
    tmnxSrrpNotificationV10v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMcRedundancy7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 1)
)
tmnxMcRedundancy7750V5v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 2)
)
tmnxMcRedundancy7450V5v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7710V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 3)
)
tmnxMcRedundancy7710V5v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7710V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 4)
)
tmnxMcRedundancy7750V6v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7750V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 5)
)
tmnxMcRedundancy7450V6v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7710V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 6)
)
tmnxMcRedundancy7710V6v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7710V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7750V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 7)
)
tmnxMcRedundancy7750V6v1Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7750V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7710V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 8)
)
tmnxMcRedundancy7710V6v1Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7710V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 9)
)
tmnxMcRedundancy7450V7v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7750V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 10)
)
tmnxMcRedundancy7750V7v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7750V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7710V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 11)
)
tmnxMcRedundancy7710V7v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7710V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 12)
)
tmnxMcRedundancy7450V8v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7750V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 13)
)
tmnxMcRedundancy7750V8v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV8v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7750V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7710V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 14)
)
tmnxMcRedundancy7710V8v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7710V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7450V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 15)
)
tmnxMcRedundancy7450V9v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7450V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7750V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 16)
)
tmnxMcRedundancy7750V9v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV8v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7750V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedundancy7710V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 17)
)
tmnxMcRedundancy7710V9v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedundancy7710V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRed7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 18)
)
tmnxMcRed7450V10v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRed7450V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRed7750V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 19)
)
tmnxMcRed7750V10v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV8v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcMobRedundancyV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcRed7750V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRed7710V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 20)
)
tmnxMcRed7710V10v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRed7710V10v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRed7450V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 21)
)
tmnxMcRed7450V11v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRed7450V11v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRed7750V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 22)
)
tmnxMcRed7750V11v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV11v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV8v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcMobRedundancyV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMcRed7750V11v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRed7710V11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 23)
)
tmnxMcRed7710V11v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV11v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRed7710V11v0Compliance.setStatus(
        "obsolete"
    )

tmnxMcRedV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 40, 1, 24)
)
tmnxMcRedV12v0Compliance.setObjects(
      *(("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV12v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV5v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancySrrpNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotifV6v1Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerSyncGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedundancyV5v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRingV6v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV6v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsDhcpsV11v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcL3RingGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPNotifyObjsV7v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerEPV7v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcsSubHostTrkGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcLagPbbGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMultiHomeGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV8v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV9v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcTlsSapGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerNotifyObjsV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerV10v0NotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcPeerIPsecTnlGrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcMobRedundancyV4v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcWarmStandbyGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcOmcrNotifGroup"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxSrrpNotificationV10v0Group"),
        ("TIMETRA-MC-REDUNDANCY-MIB", "tmnxMcRedBgpMHSiteGroup"))
)
if mibBuilder.loadTexts:
    tmnxMcRedV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MC-REDUNDANCY-MIB",
    **{"TmnxMcsClientApp": TmnxMcsClientApp,
       "TmnxMcsAccessProtection": TmnxMcsAccessProtection,
       "TmnxMcRingOperState": TmnxMcRingOperState,
       "TmnxMcRingInbCtrlOperState": TmnxMcRingInbCtrlOperState,
       "TmnxMcRingNodeOperState": TmnxMcRingNodeOperState,
       "TmnxSrrpAssoBfdIntfSessOperState": TmnxSrrpAssoBfdIntfSessOperState,
       "TmnxMcRingType": TmnxMcRingType,
       "TMcPeerIPsecTnlGrpMasterState": TMcPeerIPsecTnlGrpMasterState,
       "TMcPeerIPsecTnlGrpProtectionStatus": TMcPeerIPsecTnlGrpProtectionStatus,
       "timetraMcRedundancyMIBModule": timetraMcRedundancyMIBModule,
       "tmnxMcRedundancyConformance": tmnxMcRedundancyConformance,
       "tmnxMcRedundancyCompliances": tmnxMcRedundancyCompliances,
       "tmnxMcRedundancy7750V5v0Compliance": tmnxMcRedundancy7750V5v0Compliance,
       "tmnxMcRedundancy7450V5v0Compliance": tmnxMcRedundancy7450V5v0Compliance,
       "tmnxMcRedundancy7710V5v0Compliance": tmnxMcRedundancy7710V5v0Compliance,
       "tmnxMcRedundancy7750V6v0Compliance": tmnxMcRedundancy7750V6v0Compliance,
       "tmnxMcRedundancy7450V6v0Compliance": tmnxMcRedundancy7450V6v0Compliance,
       "tmnxMcRedundancy7710V6v0Compliance": tmnxMcRedundancy7710V6v0Compliance,
       "tmnxMcRedundancy7750V6v1Compliance": tmnxMcRedundancy7750V6v1Compliance,
       "tmnxMcRedundancy7710V6v1Compliance": tmnxMcRedundancy7710V6v1Compliance,
       "tmnxMcRedundancy7450V7v0Compliance": tmnxMcRedundancy7450V7v0Compliance,
       "tmnxMcRedundancy7750V7v0Compliance": tmnxMcRedundancy7750V7v0Compliance,
       "tmnxMcRedundancy7710V7v0Compliance": tmnxMcRedundancy7710V7v0Compliance,
       "tmnxMcRedundancy7450V8v0Compliance": tmnxMcRedundancy7450V8v0Compliance,
       "tmnxMcRedundancy7750V8v0Compliance": tmnxMcRedundancy7750V8v0Compliance,
       "tmnxMcRedundancy7710V8v0Compliance": tmnxMcRedundancy7710V8v0Compliance,
       "tmnxMcRedundancy7450V9v0Compliance": tmnxMcRedundancy7450V9v0Compliance,
       "tmnxMcRedundancy7750V9v0Compliance": tmnxMcRedundancy7750V9v0Compliance,
       "tmnxMcRedundancy7710V9v0Compliance": tmnxMcRedundancy7710V9v0Compliance,
       "tmnxMcRed7450V10v0Compliance": tmnxMcRed7450V10v0Compliance,
       "tmnxMcRed7750V10v0Compliance": tmnxMcRed7750V10v0Compliance,
       "tmnxMcRed7710V10v0Compliance": tmnxMcRed7710V10v0Compliance,
       "tmnxMcRed7450V11v0Compliance": tmnxMcRed7450V11v0Compliance,
       "tmnxMcRed7750V11v0Compliance": tmnxMcRed7750V11v0Compliance,
       "tmnxMcRed7710V11v0Compliance": tmnxMcRed7710V11v0Compliance,
       "tmnxMcRedV12v0Compliance": tmnxMcRedV12v0Compliance,
       "tmnxMcRedundancyGroups": tmnxMcRedundancyGroups,
       "tmnxMcRedundancyV5v0Group": tmnxMcRedundancyV5v0Group,
       "tmnxSrrpV5v0Group": tmnxSrrpV5v0Group,
       "tmnxMcRedundancyNotifyObjsV5v0Group": tmnxMcRedundancyNotifyObjsV5v0Group,
       "tmnxMcRingV6v0Group": tmnxMcRingV6v0Group,
       "tmnxMcPeerSyncGroup": tmnxMcPeerSyncGroup,
       "tmnxMcsDhcpsV6v0Group": tmnxMcsDhcpsV6v0Group,
       "tmnxMcRedundancyV6v0Group": tmnxMcRedundancyV6v0Group,
       "tmnxSrrpV6v1Group": tmnxSrrpV6v1Group,
       "tmnxSrrpNotificationObjV6v1Group": tmnxSrrpNotificationObjV6v1Group,
       "tmnxMcL3RingGroup": tmnxMcL3RingGroup,
       "tmnxMcPeerEPGroup": tmnxMcPeerEPGroup,
       "tmnxMcPeerEPNotifyObjsV7v0Group": tmnxMcPeerEPNotifyObjsV7v0Group,
       "tmnxMcsSubHostTrkGroup": tmnxMcsSubHostTrkGroup,
       "tmnxMcLagPbbGroup": tmnxMcLagPbbGroup,
       "tmnxMcRedBgpMultiHomeGroup": tmnxMcRedBgpMultiHomeGroup,
       "tmnxMcTlsSapGroup": tmnxMcTlsSapGroup,
       "tmnxSrrpV8v0Group": tmnxSrrpV8v0Group,
       "tmnxSrrpV9v0Group": tmnxSrrpV9v0Group,
       "tmnxMcRedundancyV9v0Group": tmnxMcRedundancyV9v0Group,
       "tmnxMcRedundancyV10v0Group": tmnxMcRedundancyV10v0Group,
       "tmnxMcsDhcpsV11v0Group": tmnxMcsDhcpsV11v0Group,
       "tmnxMcPeerNotifyObjsV10v0Group": tmnxMcPeerNotifyObjsV10v0Group,
       "tmnxMcPeerIPsecTnlGrpV10v0Group": tmnxMcPeerIPsecTnlGrpV10v0Group,
       "tmnxMcWarmStandbyGroup": tmnxMcWarmStandbyGroup,
       "tmnxMcRedundancyV12v0Group": tmnxMcRedundancyV12v0Group,
       "tmnxSrrpV10v0Group": tmnxSrrpV10v0Group,
       "tmnxMcRedBgpMHSiteGroup": tmnxMcRedBgpMHSiteGroup,
       "tmnxMcNotifyObjsGroup": tmnxMcNotifyObjsGroup,
       "tmnxMcRedundancyNotifGroups": tmnxMcRedundancyNotifGroups,
       "tmnxMcRedundancyV5v0NotifGroup": tmnxMcRedundancyV5v0NotifGroup,
       "tmnxMcRingV6v0NotifGroup": tmnxMcRingV6v0NotifGroup,
       "tmnxMcRedundancySrrpNotifGroup": tmnxMcRedundancySrrpNotifGroup,
       "tmnxSrrpNotifV6v1Group": tmnxSrrpNotifV6v1Group,
       "tmnxMcPeerEPV7v0NotifGroup": tmnxMcPeerEPV7v0NotifGroup,
       "tmnxMcPeerV10v0NotifGroup": tmnxMcPeerV10v0NotifGroup,
       "tmnxMcOmcrNotifGroup": tmnxMcOmcrNotifGroup,
       "tmnxSrrpNotificationV10v0Group": tmnxSrrpNotificationV10v0Group,
       "tmnxMcMobRedundancyCompliances": tmnxMcMobRedundancyCompliances,
       "tmnxMcMobRedundancyGroups": tmnxMcMobRedundancyGroups,
       "tmnxMcMobRedundancyV4v0Group": tmnxMcMobRedundancyV4v0Group,
       "tmnxMcMobRedundancyNotifyGroups": tmnxMcMobRedundancyNotifyGroups,
       "tmnxMcRedundancy": tmnxMcRedundancy,
       "tmnxMcRedundancyObjs": tmnxMcRedundancyObjs,
       "tmnxMcPeerTable": tmnxMcPeerTable,
       "tmnxMcPeerEntry": tmnxMcPeerEntry,
       "tmnxMcPeerIpType": tmnxMcPeerIpType,
       "tmnxMcPeerIpAddr": tmnxMcPeerIpAddr,
       "tmnxMcPeerRowStatus": tmnxMcPeerRowStatus,
       "tmnxMcPeerDescription": tmnxMcPeerDescription,
       "tmnxMcPeerAuthKey": tmnxMcPeerAuthKey,
       "tmnxMcPeerSrcIpType": tmnxMcPeerSrcIpType,
       "tmnxMcPeerSrcIpAddr": tmnxMcPeerSrcIpAddr,
       "tmnxMcPeerAdminState": tmnxMcPeerAdminState,
       "tmnxMcPeerSrcIpOperType": tmnxMcPeerSrcIpOperType,
       "tmnxMcPeerSrcIpOperAddr": tmnxMcPeerSrcIpOperAddr,
       "tmnxMcPeerRingsOperState": tmnxMcPeerRingsOperState,
       "tmnxMcPeerName": tmnxMcPeerName,
       "tmnxMcPeerWarmStandby": tmnxMcPeerWarmStandby,
       "tmnxMcPeerRemoteWarmStandby": tmnxMcPeerRemoteWarmStandby,
       "tmnxMcPeerSyncTable": tmnxMcPeerSyncTable,
       "tmnxMcPeerSyncEntry": tmnxMcPeerSyncEntry,
       "tmnxMcPeerSyncRowStatus": tmnxMcPeerSyncRowStatus,
       "tmnxMcPeerSyncIgmp": tmnxMcPeerSyncIgmp,
       "tmnxMcPeerSyncIgmpSnooping": tmnxMcPeerSyncIgmpSnooping,
       "tmnxMcPeerSyncSubMgmt": tmnxMcPeerSyncSubMgmt,
       "tmnxMcPeerSyncSrrp": tmnxMcPeerSyncSrrp,
       "tmnxMcPeerSyncAdminState": tmnxMcPeerSyncAdminState,
       "tmnxMcPeerSyncOperState": tmnxMcPeerSyncOperState,
       "tmnxMcPeerSyncOperFlags": tmnxMcPeerSyncOperFlags,
       "tmnxMcPeerSyncStatus": tmnxMcPeerSyncStatus,
       "tmnxMcPeerSyncLastSyncTime": tmnxMcPeerSyncLastSyncTime,
       "tmnxMcPeerSyncNumEntries": tmnxMcPeerSyncNumEntries,
       "tmnxMcPeerSyncLclDeletedEntries": tmnxMcPeerSyncLclDeletedEntries,
       "tmnxMcPeerSyncAlarmedEntries": tmnxMcPeerSyncAlarmedEntries,
       "tmnxMcPeerSyncRemNumEntries": tmnxMcPeerSyncRemNumEntries,
       "tmnxMcPeerSyncRemLclDelEntries": tmnxMcPeerSyncRemLclDelEntries,
       "tmnxMcPeerSyncRemAlarmedEntries": tmnxMcPeerSyncRemAlarmedEntries,
       "tmnxMcPeerSyncMcRing": tmnxMcPeerSyncMcRing,
       "tmnxMcPeerSyncMldSnooping": tmnxMcPeerSyncMldSnooping,
       "tmnxMcPeerSyncDhcpServer": tmnxMcPeerSyncDhcpServer,
       "tmnxMcPeerSyncSubHostTrk": tmnxMcPeerSyncSubHostTrk,
       "tmnxMcPeerSyncSubMgmtPppoe": tmnxMcPeerSyncSubMgmtPppoe,
       "tmnxMcPeerSyncIpsec": tmnxMcPeerSyncIpsec,
       "tmnxMcPeerSyncMobile": tmnxMcPeerSyncMobile,
       "tmnxMcPeerSyncOmcrStandby": tmnxMcPeerSyncOmcrStandby,
       "tmnxMcPeerSyncOmcrAlarmed": tmnxMcPeerSyncOmcrAlarmed,
       "tmnxMcPeerSyncOmcrRemStandby": tmnxMcPeerSyncOmcrRemStandby,
       "tmnxMcPeerSyncOmcrRemAlarmed": tmnxMcPeerSyncOmcrRemAlarmed,
       "tmnxMcPeerSyncMld": tmnxMcPeerSyncMld,
       "tmnxMcPeerSyncPythonCache": tmnxMcPeerSyncPythonCache,
       "tmnxMcPeerSyncPortTable": tmnxMcPeerSyncPortTable,
       "tmnxMcPeerSyncPortEntry": tmnxMcPeerSyncPortEntry,
       "tmnxMcPeerSyncPortId": tmnxMcPeerSyncPortId,
       "tmnxMcPeerSyncPortRowStatus": tmnxMcPeerSyncPortRowStatus,
       "tmnxMcPeerSyncPortSyncTag": tmnxMcPeerSyncPortSyncTag,
       "tmnxMcPeerSyncPortEncapRangeTable": tmnxMcPeerSyncPortEncapRangeTable,
       "tmnxMcPeerSyncPortEncapRangeEntry": tmnxMcPeerSyncPortEncapRangeEntry,
       "tmnxMcPeerSyncPortEncapType": tmnxMcPeerSyncPortEncapType,
       "tmnxMcPeerSyncPortEncapMin": tmnxMcPeerSyncPortEncapMin,
       "tmnxMcPeerSyncPortEncapMax": tmnxMcPeerSyncPortEncapMax,
       "tmnxMcPeerSyncPortEncapRowStatus": tmnxMcPeerSyncPortEncapRowStatus,
       "tmnxMcPeerSyncPortEncapSyncTag": tmnxMcPeerSyncPortEncapSyncTag,
       "tmnxMcLagConfigTableLastChanged": tmnxMcLagConfigTableLastChanged,
       "tmnxMcLagConfigTable": tmnxMcLagConfigTable,
       "tmnxMcLagConfigEntry": tmnxMcLagConfigEntry,
       "tmnxMcLagConfigPeerLastChanged": tmnxMcLagConfigPeerLastChanged,
       "tmnxMcLagConfigPeerAdminstate": tmnxMcLagConfigPeerAdminstate,
       "tmnxMcLagConfigKeepALiveIvl": tmnxMcLagConfigKeepALiveIvl,
       "tmnxMcLagConfigHoldOnNgbrFailure": tmnxMcLagConfigHoldOnNgbrFailure,
       "tmnxMcLagConfigOperState": tmnxMcLagConfigOperState,
       "tmnxMcLagConfigPeerLastStateChge": tmnxMcLagConfigPeerLastStateChge,
       "tmnxMcLagConfigLagTableLastChanged": tmnxMcLagConfigLagTableLastChanged,
       "tmnxMcLagConfigLagTable": tmnxMcLagConfigLagTable,
       "tmnxMcLagConfigLagEntry": tmnxMcLagConfigLagEntry,
       "tmnxMcLagConfigLagId": tmnxMcLagConfigLagId,
       "tmnxMcLagConfigLagLastChanged": tmnxMcLagConfigLagLastChanged,
       "tmnxMcLagConfigLagRowStatus": tmnxMcLagConfigLagRowStatus,
       "tmnxMcLagConfigLaglacpKey": tmnxMcLagConfigLaglacpKey,
       "tmnxMcLagConfigLagSystemId": tmnxMcLagConfigLagSystemId,
       "tmnxMcLagConfigLagSystemPriority": tmnxMcLagConfigLagSystemPriority,
       "tmnxMcLagConfigLagRemoteLagId": tmnxMcLagConfigLagRemoteLagId,
       "tmnxMcLagConfigLagSrcBMacLSB": tmnxMcLagConfigLagSrcBMacLSB,
       "tmnxMcLagConfigLagOperSrcBMacLSB": tmnxMcLagConfigLagOperSrcBMacLSB,
       "tmnxSrrpOperTable": tmnxSrrpOperTable,
       "tmnxSrrpOperEntry": tmnxSrrpOperEntry,
       "tmnxSrrpOperID": tmnxSrrpOperID,
       "tmnxSrrpOperRowStatus": tmnxSrrpOperRowStatus,
       "tmnxSrrpOperDescription": tmnxSrrpOperDescription,
       "tmnxSrrpOperGwMac": tmnxSrrpOperGwMac,
       "tmnxSrrpOperGwOperMac": tmnxSrrpOperGwOperMac,
       "tmnxSrrpOperPriority": tmnxSrrpOperPriority,
       "tmnxSrrpOperInUsePriority": tmnxSrrpOperInUsePriority,
       "tmnxSrrpOperMasterPriority": tmnxSrrpOperMasterPriority,
       "tmnxSrrpOperKeepAliveInterval": tmnxSrrpOperKeepAliveInterval,
       "tmnxSrrpOperMsgPathSapPortId": tmnxSrrpOperMsgPathSapPortId,
       "tmnxSrrpOperMsgPathSapEncapVal": tmnxSrrpOperMsgPathSapEncapVal,
       "tmnxSrrpOperAdminState": tmnxSrrpOperAdminState,
       "tmnxSrrpOperState": tmnxSrrpOperState,
       "tmnxSrrpOperMasterSince": tmnxSrrpOperMasterSince,
       "tmnxSrrpOperVrrpPolicy1": tmnxSrrpOperVrrpPolicy1,
       "tmnxSrrpOperVrrpPolicy2": tmnxSrrpOperVrrpPolicy2,
       "tmnxSrrpOperFlags": tmnxSrrpOperFlags,
       "tmnxSrrpOperMasterDownInterval": tmnxSrrpOperMasterDownInterval,
       "tmnxSrrpOperMasterDownTimer": tmnxSrrpOperMasterDownTimer,
       "tmnxSrrpOperSendFibPopulation": tmnxSrrpOperSendFibPopulation,
       "tmnxSrrpOperPreempt": tmnxSrrpOperPreempt,
       "tmnxSrrpOperOneGarpPerSap": tmnxSrrpOperOneGarpPerSap,
       "tmnxSrrpOperMonitorOperGrp": tmnxSrrpOperMonitorOperGrp,
       "tmnxSrrpOperPriorityStep": tmnxSrrpOperPriorityStep,
       "tmnxSrrpOperDownReason": tmnxSrrpOperDownReason,
       "tmnxMcLagInfoLagTable": tmnxMcLagInfoLagTable,
       "tmnxMcLagInfoLagEntry": tmnxMcLagInfoLagEntry,
       "tmnxMcLagActiveStandby": tmnxMcLagActiveStandby,
       "tmnxMcLagLacpIdInUse": tmnxMcLagLacpIdInUse,
       "tmnxMcLagExtendedTimeOut": tmnxMcLagExtendedTimeOut,
       "tmnxMcLagSelectionLogic": tmnxMcLagSelectionLogic,
       "tmnxMcLagConfigMismatchString": tmnxMcLagConfigMismatchString,
       "tmnxMcLagConfigMismatchFlags": tmnxMcLagConfigMismatchFlags,
       "tmnxMcsClientAppTable": tmnxMcsClientAppTable,
       "tmnxMcsClientAppEntry": tmnxMcsClientAppEntry,
       "tmnxMcsClientApplication": tmnxMcsClientApplication,
       "tmnxMcsClientNumEntries": tmnxMcsClientNumEntries,
       "tmnxMcsClientLclDeletedEntries": tmnxMcsClientLclDeletedEntries,
       "tmnxMcsClientAlarmedEntries": tmnxMcsClientAlarmedEntries,
       "tmnxMcsClientRemNumEntries": tmnxMcsClientRemNumEntries,
       "tmnxMcsClientRemLclDelEntries": tmnxMcsClientRemLclDelEntries,
       "tmnxMcsClientRemAlarmedEntries": tmnxMcsClientRemAlarmedEntries,
       "tmnxMcsClientOmcrStandby": tmnxMcsClientOmcrStandby,
       "tmnxMcsClientOmcrAlarmed": tmnxMcsClientOmcrAlarmed,
       "tmnxMcsClientOmcrRemStandby": tmnxMcsClientOmcrRemStandby,
       "tmnxMcsClientOmcrRemAlarmed": tmnxMcsClientOmcrRemAlarmed,
       "tmnxSrrpStatsTable": tmnxSrrpStatsTable,
       "tmnxSrrpStatsEntry": tmnxSrrpStatsEntry,
       "tmnxSrrpStatsBecomeMaster": tmnxSrrpStatsBecomeMaster,
       "tmnxSrrpStatsMasterChanges": tmnxSrrpStatsMasterChanges,
       "tmnxSrrpStatsAdvSent": tmnxSrrpStatsAdvSent,
       "tmnxSrrpStatsAdvRcvd": tmnxSrrpStatsAdvRcvd,
       "tmnxSrrpStatsPriZeroPktsRcvd": tmnxSrrpStatsPriZeroPktsRcvd,
       "tmnxSrrpStatsPriZeroPktsSent": tmnxSrrpStatsPriZeroPktsSent,
       "tmnxSrrpStatsPreemptEvents": tmnxSrrpStatsPreemptEvents,
       "tmnxSrrpStatsPreemptedEvents": tmnxSrrpStatsPreemptedEvents,
       "tmnxSrrpStatsAdvIntDiscards": tmnxSrrpStatsAdvIntDiscards,
       "tmnxSrrpStatsAdvIntErrors": tmnxSrrpStatsAdvIntErrors,
       "tmnxSrrpStatsBecomeBackupRouting": tmnxSrrpStatsBecomeBackupRouting,
       "tmnxSrrpStatsBecomeBackupShunt": tmnxSrrpStatsBecomeBackupShunt,
       "tmnxSrrpStatsBecomeNonMaster": tmnxSrrpStatsBecomeNonMaster,
       "tmnxMcRingTableLastChanged": tmnxMcRingTableLastChanged,
       "tmnxMcRingTable": tmnxMcRingTable,
       "tmnxMcRingEntry": tmnxMcRingEntry,
       "tmnxMcRingRowStatus": tmnxMcRingRowStatus,
       "tmnxMcRingLastChanged": tmnxMcRingLastChanged,
       "tmnxMcRingAdminState": tmnxMcRingAdminState,
       "tmnxMcRingInbCtrlSvcId": tmnxMcRingInbCtrlSvcId,
       "tmnxMcRingInbCtrlIfName": tmnxMcRingInbCtrlIfName,
       "tmnxMcRingInbCtrlDestIpType": tmnxMcRingInbCtrlDestIpType,
       "tmnxMcRingInbCtrlDestIp": tmnxMcRingInbCtrlDestIp,
       "tmnxMcRingVlanMap": tmnxMcRingVlanMap,
       "tmnxMcRingVlanMapExcl": tmnxMcRingVlanMapExcl,
       "tmnxMcRingInbCtrlDbMax": tmnxMcRingInbCtrlDbMax,
       "tmnxMcRingInbCtrlDbAdmin": tmnxMcRingInbCtrlDbAdmin,
       "tmnxMcRingType": tmnxMcRingType,
       "tmnxMcRingInfoTableLastChanged": tmnxMcRingInfoTableLastChanged,
       "tmnxMcRingInfoTable": tmnxMcRingInfoTable,
       "tmnxMcRingInfoEntry": tmnxMcRingInfoEntry,
       "tmnxMcRingInfoLastChanged": tmnxMcRingInfoLastChanged,
       "tmnxMcRingInfoOperState": tmnxMcRingInfoOperState,
       "tmnxMcRingInfoFailureReason": tmnxMcRingInfoFailureReason,
       "tmnxMcRingInfoInbCtrlOperState": tmnxMcRingInfoInbCtrlOperState,
       "tmnxMcRingInfoInbCtrlSrcIpType": tmnxMcRingInfoInbCtrlSrcIpType,
       "tmnxMcRingInfoInbCtrlSrcIp": tmnxMcRingInfoInbCtrlSrcIp,
       "tmnxMcRingInfoInbCtrlDbStart": tmnxMcRingInfoInbCtrlDbStart,
       "tmnxMcRingInfoInbCtrlDbTime": tmnxMcRingInfoInbCtrlDbTime,
       "tmnxMcRingInfoPortId": tmnxMcRingInfoPortId,
       "tmnxMcRingInfoVlanMap": tmnxMcRingInfoVlanMap,
       "tmnxMcRingInfoVlanMapExcl": tmnxMcRingInfoVlanMapExcl,
       "tmnxMcRingInfoCtrlVlanMap": tmnxMcRingInfoCtrlVlanMap,
       "tmnxMcRingInfoInbCtrlDbGuard": tmnxMcRingInfoInbCtrlDbGuard,
       "tmnxMcRingNodeTableLastChanged": tmnxMcRingNodeTableLastChanged,
       "tmnxMcRingNodeTable": tmnxMcRingNodeTable,
       "tmnxMcRingNodeEntry": tmnxMcRingNodeEntry,
       "tmnxMcRingNodeName": tmnxMcRingNodeName,
       "tmnxMcRingNodeRowStatus": tmnxMcRingNodeRowStatus,
       "tmnxMcRingNodeLastChanged": tmnxMcRingNodeLastChanged,
       "tmnxMcRingNodeRncvAdminState": tmnxMcRingNodeRncvAdminState,
       "tmnxMcRingNodeRncvSvcId": tmnxMcRingNodeRncvSvcId,
       "tmnxMcRingNodeRncvEncapValue": tmnxMcRingNodeRncvEncapValue,
       "tmnxMcRingNodeRncvSrcIpType": tmnxMcRingNodeRncvSrcIpType,
       "tmnxMcRingNodeRncvSrcIp": tmnxMcRingNodeRncvSrcIp,
       "tmnxMcRingNodeRncvDestIpType": tmnxMcRingNodeRncvDestIpType,
       "tmnxMcRingNodeRncvDestIp": tmnxMcRingNodeRncvDestIp,
       "tmnxMcRingNodeRncvInterval": tmnxMcRingNodeRncvInterval,
       "tmnxMcRingNodeRncvSrcMac": tmnxMcRingNodeRncvSrcMac,
       "tmnxMcRingNodeInfoTableLastChgd": tmnxMcRingNodeInfoTableLastChgd,
       "tmnxMcRingNodeInfoTable": tmnxMcRingNodeInfoTable,
       "tmnxMcRingNodeInfoEntry": tmnxMcRingNodeInfoEntry,
       "tmnxMcRingNodeInfoLastChanged": tmnxMcRingNodeInfoLastChanged,
       "tmnxMcRingNodeInfoLocOperState": tmnxMcRingNodeInfoLocOperState,
       "tmnxMcRingNodeInfoRemOperState": tmnxMcRingNodeInfoRemOperState,
       "tmnxMcRingNodeInfoInUse": tmnxMcRingNodeInfoInUse,
       "tmnxMcRingNodeInfoFailureReason": tmnxMcRingNodeInfoFailureReason,
       "tmnxMcTlsCfgTableLastChanged": tmnxMcTlsCfgTableLastChanged,
       "tmnxMcTlsCfgTable": tmnxMcTlsCfgTable,
       "tmnxMcTlsCfgEntry": tmnxMcTlsCfgEntry,
       "tmnxMcTlsCfgLastChanged": tmnxMcTlsCfgLastChanged,
       "tmnxMcTlsCfgDefGwIpType": tmnxMcTlsCfgDefGwIpType,
       "tmnxMcTlsCfgDefGwIp": tmnxMcTlsCfgDefGwIp,
       "tmnxMcTlsCfgDefGwMac": tmnxMcTlsCfgDefGwMac,
       "tmnxMcEpipeSapTableLastChanged": tmnxMcEpipeSapTableLastChanged,
       "tmnxMcEpipeSapTable": tmnxMcEpipeSapTable,
       "tmnxMcEpipeSapEntry": tmnxMcEpipeSapEntry,
       "tmnxMcEpipeSapRowStatus": tmnxMcEpipeSapRowStatus,
       "tmnxMcEpipeSapLastChanged": tmnxMcEpipeSapLastChanged,
       "tmnxMcEpipeSapRingNodeName": tmnxMcEpipeSapRingNodeName,
       "tmnxMcsDhcpsObjs": tmnxMcsDhcpsObjs,
       "tmnxMcsDhcpsTableLastChgd": tmnxMcsDhcpsTableLastChgd,
       "tmnxMcsDhcpsTable": tmnxMcsDhcpsTable,
       "tmnxMcsDhcpsEntry": tmnxMcsDhcpsEntry,
       "tmnxMcsDhcpsRtrID": tmnxMcsDhcpsRtrID,
       "tmnxMcsDhcpsServerName": tmnxMcsDhcpsServerName,
       "tmnxMcsDhcpsRowStatus": tmnxMcsDhcpsRowStatus,
       "tmnxMcsDhcpsPeerIpType": tmnxMcsDhcpsPeerIpType,
       "tmnxMcsDhcpsPeerIpAddr": tmnxMcsDhcpsPeerIpAddr,
       "tmnxMcsDhcpsSyncTag": tmnxMcsDhcpsSyncTag,
       "tmnxMcsDhcpsPoolTableLastChgd": tmnxMcsDhcpsPoolTableLastChgd,
       "tmnxMcsDhcpsPoolTable": tmnxMcsDhcpsPoolTable,
       "tmnxMcsDhcpsPoolEntry": tmnxMcsDhcpsPoolEntry,
       "tmnxMcsDhcpsPoolName": tmnxMcsDhcpsPoolName,
       "tmnxMcsDhcpsPoolRowStatus": tmnxMcsDhcpsPoolRowStatus,
       "tmnxMcsDhcpsPoolPeerIpType": tmnxMcsDhcpsPoolPeerIpType,
       "tmnxMcsDhcpsPoolPeerIpAddr": tmnxMcsDhcpsPoolPeerIpAddr,
       "tmnxMcsDhcpsPoolSyncTag": tmnxMcsDhcpsPoolSyncTag,
       "tmnxSrrpAssoBfdIntfTblLastChgd": tmnxSrrpAssoBfdIntfTblLastChgd,
       "tmnxSrrpAssoBfdIntfTable": tmnxSrrpAssoBfdIntfTable,
       "tmnxSrrpAssoBfdIntfEntry": tmnxSrrpAssoBfdIntfEntry,
       "tmnxSrrpAssoBfdIntfSvcId": tmnxSrrpAssoBfdIntfSvcId,
       "tmnxSrrpAssoBfdIntfIfName": tmnxSrrpAssoBfdIntfIfName,
       "tmnxSrrpAssoBfdIntfDestIpType": tmnxSrrpAssoBfdIntfDestIpType,
       "tmnxSrrpAssoBfdIntfDestIp": tmnxSrrpAssoBfdIntfDestIp,
       "tmnxSrrpAssoBfdIntfRowStatus": tmnxSrrpAssoBfdIntfRowStatus,
       "tmnxSrrpAssoBfdIntfLastChanged": tmnxSrrpAssoBfdIntfLastChanged,
       "tmnxSrrpAssoBfdIntfSrcIpType": tmnxSrrpAssoBfdIntfSrcIpType,
       "tmnxSrrpAssoBfdIntfSrcIp": tmnxSrrpAssoBfdIntfSrcIp,
       "tmnxSrrpAssoBfdIntfSessOperState": tmnxSrrpAssoBfdIntfSessOperState,
       "tmnxMcRingDbTableLastChanged": tmnxMcRingDbTableLastChanged,
       "tmnxMcRingDbTableSize": tmnxMcRingDbTableSize,
       "tmnxMcRingDbTable": tmnxMcRingDbTable,
       "tmnxMcRingDbEntry": tmnxMcRingDbEntry,
       "tmnxMcRingDbStart": tmnxMcRingDbStart,
       "tmnxMcRingDbTime": tmnxMcRingDbTime,
       "tmnxMcRingDbOperState": tmnxMcRingDbOperState,
       "tmnxMcL3RingSrrpTableLastChanged": tmnxMcL3RingSrrpTableLastChanged,
       "tmnxMcL3RingSrrpTable": tmnxMcL3RingSrrpTable,
       "tmnxMcL3RingSrrpEntry": tmnxMcL3RingSrrpEntry,
       "tmnxMcL3RingSrrpRowStatus": tmnxMcL3RingSrrpRowStatus,
       "tmnxMcL3RingSrrpLastChanged": tmnxMcL3RingSrrpLastChanged,
       "tmnxMcPeerEPTableLastChanged": tmnxMcPeerEPTableLastChanged,
       "tmnxMcPeerEPTable": tmnxMcPeerEPTable,
       "tmnxMcPeerEPEntry": tmnxMcPeerEPEntry,
       "tmnxMcPeerEPRowStatus": tmnxMcPeerEPRowStatus,
       "tmnxMcPeerEPLastChanged": tmnxMcPeerEPLastChanged,
       "tmnxMcPeerEPAdminState": tmnxMcPeerEPAdminState,
       "tmnxMcPeerEPSysPriority": tmnxMcPeerEPSysPriority,
       "tmnxMcPeerEPKeepAliveIntvl": tmnxMcPeerEPKeepAliveIntvl,
       "tmnxMcPeerEPHoldOnNbrFail": tmnxMcPeerEPHoldOnNbrFail,
       "tmnxMcPeerEPBootTimer": tmnxMcPeerEPBootTimer,
       "tmnxMcPeerEPPassiveMode": tmnxMcPeerEPPassiveMode,
       "tmnxMcPeerEPBfd": tmnxMcPeerEPBfd,
       "tmnxMcPeerEPOperState": tmnxMcPeerEPOperState,
       "tmnxMcPeerEPPeerLastStateChge": tmnxMcPeerEPPeerLastStateChge,
       "tmnxMcPeerEPPassiveModeOper": tmnxMcPeerEPPassiveModeOper,
       "tmnxMcPeerEPRefCount": tmnxMcPeerEPRefCount,
       "tmnxMcRedBgpMultiHomeObjs": tmnxMcRedBgpMultiHomeObjs,
       "tmnxMcRedBgpMultiHomeBootTimer": tmnxMcRedBgpMultiHomeBootTimer,
       "tmnxMcRedBgpMultiHomeSiteTimer": tmnxMcRedBgpMultiHomeSiteTimer,
       "tmnxMcRedBgpMHSiteMinDnTimer": tmnxMcRedBgpMHSiteMinDnTimer,
       "tmnxMcTlsSapTableLastChanged": tmnxMcTlsSapTableLastChanged,
       "tmnxMcTlsSapTable": tmnxMcTlsSapTable,
       "tmnxMcTlsSapEntry": tmnxMcTlsSapEntry,
       "tmnxMcTlsSapRowStatus": tmnxMcTlsSapRowStatus,
       "tmnxMcTlsSapLastChanged": tmnxMcTlsSapLastChanged,
       "tmnxMcTlsSapRingNodeName": tmnxMcTlsSapRingNodeName,
       "tMcPeerIPsecTblLastChgd": tMcPeerIPsecTblLastChgd,
       "tMcPeerIPsecTable": tMcPeerIPsecTable,
       "tMcPeerIPsecEntry": tMcPeerIPsecEntry,
       "tMcPeerIPsecRowStatus": tMcPeerIPsecRowStatus,
       "tMcPeerIPsecLastChgd": tMcPeerIPsecLastChgd,
       "tMcPeerIPsecKeepAliveIntvl": tMcPeerIPsecKeepAliveIntvl,
       "tMcPeerIPsecHoldOnNgbrFail": tMcPeerIPsecHoldOnNgbrFail,
       "tMcPeerIPsecBfdEnableSvc": tMcPeerIPsecBfdEnableSvc,
       "tMcPeerIPsecBfdIntfIfName": tMcPeerIPsecBfdIntfIfName,
       "tMcPeerIPsecBfdIntfDestIpType": tMcPeerIPsecBfdIntfDestIpType,
       "tMcPeerIPsecBfdIntfDestIp": tMcPeerIPsecBfdIntfDestIp,
       "tMcPeerIPsecDiscoveryIntvl": tMcPeerIPsecDiscoveryIntvl,
       "tMcPeerIPsecDiscoveryIntvlBoot": tMcPeerIPsecDiscoveryIntvlBoot,
       "tMcPeerIPsecBfdEnable": tMcPeerIPsecBfdEnable,
       "tMcPeerIPsecTnlGrpTblLastChgd": tMcPeerIPsecTnlGrpTblLastChgd,
       "tMcPeerIPsecTnlGrpTable": tMcPeerIPsecTnlGrpTable,
       "tMcPeerIPsecTnlGrpEntry": tMcPeerIPsecTnlGrpEntry,
       "tMcPeerIPsecTnlGrpId": tMcPeerIPsecTnlGrpId,
       "tMcPeerIPsecTnlGrpRowStatus": tMcPeerIPsecTnlGrpRowStatus,
       "tMcPeerIPsecTnlGrpLastChgd": tMcPeerIPsecTnlGrpLastChgd,
       "tMcPeerIPsecTnlGrpPeerGrpId": tMcPeerIPsecTnlGrpPeerGrpId,
       "tMcPeerIPsecTnlGrpPriority": tMcPeerIPsecTnlGrpPriority,
       "tMcPeerIPsecTnlGrpPreempt": tMcPeerIPsecTnlGrpPreempt,
       "tMcPeerIPsecTnlGrpAdminState": tMcPeerIPsecTnlGrpAdminState,
       "tMcPeerIPsecTnlGrpOperState": tMcPeerIPsecTnlGrpOperState,
       "tMcPeerIPsecTnlGrpMasterState": tMcPeerIPsecTnlGrpMasterState,
       "tMcPeerIPsecTnlGrpReason": tMcPeerIPsecTnlGrpReason,
       "tMcPeerIPsecTnlGrpForceSwitch": tMcPeerIPsecTnlGrpForceSwitch,
       "tMcPeerIPsecTnlGrpProtectStatus": tMcPeerIPsecTnlGrpProtectStatus,
       "tMcPeerIPsecTnlGrpForceSwitchTo": tMcPeerIPsecTnlGrpForceSwitchTo,
       "tmnxMcsTnlGrpTblLastChgd": tmnxMcsTnlGrpTblLastChgd,
       "tmnxMcsTnlGrpTable": tmnxMcsTnlGrpTable,
       "tmnxMcsTnlGrpEntry": tmnxMcsTnlGrpEntry,
       "tmnxMcsTnlGrpRowStatus": tmnxMcsTnlGrpRowStatus,
       "tmnxMcsTnlGrpSyncTag": tmnxMcsTnlGrpSyncTag,
       "tMcPeerTnlGrpStatTable": tMcPeerTnlGrpStatTable,
       "tMcPeerTnlGrpStatEntry": tMcPeerTnlGrpStatEntry,
       "tMcPeerTnlGrpStatDynInstalled": tMcPeerTnlGrpStatDynInstalled,
       "tMcPeerTnlGrpStatDynInstalling": tMcPeerTnlGrpStatDynInstalling,
       "tMcPeerTnlGrpStatDynAwaitConf": tMcPeerTnlGrpStatDynAwaitConf,
       "tMcPeerTnlGrpStatDynFailed": tMcPeerTnlGrpStatDynFailed,
       "tMcPeerTnlGrpStatInstalled": tMcPeerTnlGrpStatInstalled,
       "tMcPeerTnlGrpStatInstalling": tMcPeerTnlGrpStatInstalling,
       "tMcPeerTnlGrpStatAwaitConf": tMcPeerTnlGrpStatAwaitConf,
       "tMcPeerTnlGrpStatFailed": tMcPeerTnlGrpStatFailed,
       "tmnxMcOmcrObjs": tmnxMcOmcrObjs,
       "tmnxMcOmcrStatTable": tmnxMcOmcrStatTable,
       "tmnxMcOmcrStatEntry": tmnxMcOmcrStatEntry,
       "tmnxMcOmcrStatClientApplication": tmnxMcOmcrStatClientApplication,
       "tmnxMcOmcrStatAccessProtection": tmnxMcOmcrStatAccessProtection,
       "tmnxMcOmcrStatIndex": tmnxMcOmcrStatIndex,
       "tmnxMcOmcrStatFailed": tmnxMcOmcrStatFailed,
       "tmnxMcOmcrStatFailure": tmnxMcOmcrStatFailure,
       "tmnxMcOmcrStatNumFailedEntries": tmnxMcOmcrStatNumFailedEntries,
       "tmnxMcsPythonObjs": tmnxMcsPythonObjs,
       "tmnxMcsPyPlcyTableLastChgd": tmnxMcsPyPlcyTableLastChgd,
       "tmnxMcsPyPlcyTable": tmnxMcsPyPlcyTable,
       "tmnxMcsPyPlcyEntry": tmnxMcsPyPlcyEntry,
       "tmnxMcsPyPlcyName": tmnxMcsPyPlcyName,
       "tmnxMcsPyPlcyRowStatus": tmnxMcsPyPlcyRowStatus,
       "tmnxMcsPyPlcyPeerIpAddrType": tmnxMcsPyPlcyPeerIpAddrType,
       "tmnxMcsPyPlcyPeerIpAddr": tmnxMcsPyPlcyPeerIpAddr,
       "tmnxMcsPyPlcyMcsSyncTag": tmnxMcsPyPlcyMcsSyncTag,
       "tmnxMcsPyPlcyTableLastChanged": tmnxMcsPyPlcyTableLastChanged,
       "tmnxMcRedundancyStatsObjs": tmnxMcRedundancyStatsObjs,
       "tmnxMcLagStatsPktsRx": tmnxMcLagStatsPktsRx,
       "tmnxMcLagStatsPktsRxKeepalive": tmnxMcLagStatsPktsRxKeepalive,
       "tmnxMcLagStatsPktsRxConfig": tmnxMcLagStatsPktsRxConfig,
       "tmnxMcLagStatsPktsRxPeerConfig": tmnxMcLagStatsPktsRxPeerConfig,
       "tmnxMcLagStatsPktsRxState": tmnxMcLagStatsPktsRxState,
       "tmnxMcLagStatsDropPktKpaliveTask": tmnxMcLagStatsDropPktKpaliveTask,
       "tmnxMcLagStatsDropPktTooShort": tmnxMcLagStatsDropPktTooShort,
       "tmnxMcLagStatsDropPktVerifyFaild": tmnxMcLagStatsDropPktVerifyFaild,
       "tmnxMcLagStatsDropTlvInvalidSize": tmnxMcLagStatsDropTlvInvalidSize,
       "tmnxMcLagStatsDropOutOfSeq": tmnxMcLagStatsDropOutOfSeq,
       "tmnxMcLagStatsDropUnknownTlv": tmnxMcLagStatsDropUnknownTlv,
       "tmnxMcLagStatsDropTlvInvldLagId": tmnxMcLagStatsDropTlvInvldLagId,
       "tmnxMcLagStatsDropMD5": tmnxMcLagStatsDropMD5,
       "tmnxMcLagStatsDropUnknownPeer": tmnxMcLagStatsDropUnknownPeer,
       "tmnxMcLagStatsPktsTx": tmnxMcLagStatsPktsTx,
       "tmnxMcLagStatsPktsTxKeepalive": tmnxMcLagStatsPktsTxKeepalive,
       "tmnxMcLagStatsPktsTxConfig": tmnxMcLagStatsPktsTxConfig,
       "tmnxMcLagStatsPktsTxPeerConfig": tmnxMcLagStatsPktsTxPeerConfig,
       "tmnxMcLagStatsPktsTxState": tmnxMcLagStatsPktsTxState,
       "tmnxMcLagStatsPktsTxFailed": tmnxMcLagStatsPktsTxFailed,
       "tmnxMcLagPeerStatsTable": tmnxMcLagPeerStatsTable,
       "tmnxMcLagPeerStatsEntry": tmnxMcLagPeerStatsEntry,
       "tmnxMcLagPeerStatsPktsRx": tmnxMcLagPeerStatsPktsRx,
       "tmnxMcLagPeerStatsPktsRxKpalive": tmnxMcLagPeerStatsPktsRxKpalive,
       "tmnxMcLagPeerStatsPktsRxConfig": tmnxMcLagPeerStatsPktsRxConfig,
       "tmnxMcLagPeerStatsPktsRxPeerCfg": tmnxMcLagPeerStatsPktsRxPeerCfg,
       "tmnxMcLagPeerStatsPktsRxState": tmnxMcLagPeerStatsPktsRxState,
       "tmnxMcLagPeerStatsDropStateDsbld": tmnxMcLagPeerStatsDropStateDsbld,
       "tmnxMcLagPeerStatsDropPktTooShrt": tmnxMcLagPeerStatsDropPktTooShrt,
       "tmnxMcLagPeerStatsDropTlvInvldSz": tmnxMcLagPeerStatsDropTlvInvldSz,
       "tmnxMcLagPeerStatsDropTlvInvldId": tmnxMcLagPeerStatsDropTlvInvldId,
       "tmnxMcLagPeerStatsDropOutOfSeq": tmnxMcLagPeerStatsDropOutOfSeq,
       "tmnxMcLagPeerStatsDropUnknownTlv": tmnxMcLagPeerStatsDropUnknownTlv,
       "tmnxMcLagPeerStatsDropMD5": tmnxMcLagPeerStatsDropMD5,
       "tmnxMcLagPeerStatsPktsTx": tmnxMcLagPeerStatsPktsTx,
       "tmnxMcLagPeerStatsPktsTxKpalive": tmnxMcLagPeerStatsPktsTxKpalive,
       "tmnxMcLagPeerStatsPktsTxPeerCfg": tmnxMcLagPeerStatsPktsTxPeerCfg,
       "tmnxMcLagPeerStatsPktsTxFailed": tmnxMcLagPeerStatsPktsTxFailed,
       "tmnxMcLagLagStatsTable": tmnxMcLagLagStatsTable,
       "tmnxMcLagLagStatsEntry": tmnxMcLagLagStatsEntry,
       "tmnxMcLagLagStatsPktsRxConfig": tmnxMcLagLagStatsPktsRxConfig,
       "tmnxMcLagLagStatsPktsRxState": tmnxMcLagLagStatsPktsRxState,
       "tmnxMcLagLagStatsPktsTxConfig": tmnxMcLagLagStatsPktsTxConfig,
       "tmnxMcLagLagStatsPktsTxState": tmnxMcLagLagStatsPktsTxState,
       "tmnxMcLagLagStatsPktsTxFailed": tmnxMcLagLagStatsPktsTxFailed,
       "tmnxMcPeerSyncStatsTable": tmnxMcPeerSyncStatsTable,
       "tmnxMcPeerSyncStatsEntry": tmnxMcPeerSyncStatsEntry,
       "tmnxMcPeerSyncPktsTxAll": tmnxMcPeerSyncPktsTxAll,
       "tmnxMcPeerSyncPktsTxHello": tmnxMcPeerSyncPktsTxHello,
       "tmnxMcPeerSyncPktsTxData": tmnxMcPeerSyncPktsTxData,
       "tmnxMcPeerSyncPktsTxOther": tmnxMcPeerSyncPktsTxOther,
       "tmnxMcPeerSyncPktsTxErr": tmnxMcPeerSyncPktsTxErr,
       "tmnxMcPeerSyncPktsRxAll": tmnxMcPeerSyncPktsRxAll,
       "tmnxMcPeerSyncPktsRxHello": tmnxMcPeerSyncPktsRxHello,
       "tmnxMcPeerSyncPktsRxData": tmnxMcPeerSyncPktsRxData,
       "tmnxMcPeerSyncPktsRxOther": tmnxMcPeerSyncPktsRxOther,
       "tmnxMcPeerSyncPktsRxErr": tmnxMcPeerSyncPktsRxErr,
       "tmnxMcPeerSyncPktsRxErrHeader": tmnxMcPeerSyncPktsRxErrHeader,
       "tmnxMcPeerSyncPktsRxErrBody": tmnxMcPeerSyncPktsRxErrBody,
       "tmnxMcPeerSyncPktsRxErrSeqNum": tmnxMcPeerSyncPktsRxErrSeqNum,
       "tmnxMcrPeerStatsTableLastChanged": tmnxMcrPeerStatsTableLastChanged,
       "tmnxMcrPeerStatsTable": tmnxMcrPeerStatsTable,
       "tmnxMcrPeerStatsEntry": tmnxMcrPeerStatsEntry,
       "tmnxMcrPeerStatsLastChanged": tmnxMcrPeerStatsLastChanged,
       "tmnxMcrPeerStatsRx": tmnxMcrPeerStatsRx,
       "tmnxMcrPeerStatsRxMcsIdReq": tmnxMcrPeerStatsRxMcsIdReq,
       "tmnxMcrPeerStatsRxMcsIdRsp": tmnxMcrPeerStatsRxMcsIdRsp,
       "tmnxMcrPeerStatsRxRingExistsReq": tmnxMcrPeerStatsRxRingExistsReq,
       "tmnxMcrPeerStatsRxRingExistsRsp": tmnxMcrPeerStatsRxRingExistsRsp,
       "tmnxMcrPeerStatsRxKeepAlive": tmnxMcrPeerStatsRxKeepAlive,
       "tmnxMcrPeerStatsTx": tmnxMcrPeerStatsTx,
       "tmnxMcrPeerStatsTxMcsIdReq": tmnxMcrPeerStatsTxMcsIdReq,
       "tmnxMcrPeerStatsTxMcsIdRsp": tmnxMcrPeerStatsTxMcsIdRsp,
       "tmnxMcrPeerStatsTxRingExistsReq": tmnxMcrPeerStatsTxRingExistsReq,
       "tmnxMcrPeerStatsTxRingExistsRsp": tmnxMcrPeerStatsTxRingExistsRsp,
       "tmnxMcrPeerStatsTxKeepAlive": tmnxMcrPeerStatsTxKeepAlive,
       "tmnxMcrRingStatsTableLastChanged": tmnxMcrRingStatsTableLastChanged,
       "tmnxMcrRingStatsTable": tmnxMcrRingStatsTable,
       "tmnxMcrRingStatsEntry": tmnxMcrRingStatsEntry,
       "tmnxMcrRingStatsLastChanged": tmnxMcrRingStatsLastChanged,
       "tmnxMcrRingStatsRxSapsChanged": tmnxMcrRingStatsRxSapsChanged,
       "tmnxMcrRingStatsTxSapsChanged": tmnxMcrRingStatsTxSapsChanged,
       "tmnxMcrRingStatsRxOpaqueDelivrd": tmnxMcrRingStatsRxOpaqueDelivrd,
       "tmnxMcrRingStatsRxOpaqueNoDest": tmnxMcrRingStatsRxOpaqueNoDest,
       "tmnxMcrRingStatsTxOpaque": tmnxMcrRingStatsTxOpaque,
       "tmnxMcrStatsRx": tmnxMcrStatsRx,
       "tmnxMcrStatsRxTooShort": tmnxMcrStatsRxTooShort,
       "tmnxMcrStatsRxWrongAuth": tmnxMcrStatsRxWrongAuth,
       "tmnxMcrStatsRxInvalidTlv": tmnxMcrStatsRxInvalidTlv,
       "tmnxMcrStatsRxIncomplete": tmnxMcrStatsRxIncomplete,
       "tmnxMcrStatsRxUnknownType": tmnxMcrStatsRxUnknownType,
       "tmnxMcrStatsRxUnknownPeer": tmnxMcrStatsRxUnknownPeer,
       "tmnxMcrStatsRxUnknownRing": tmnxMcrStatsRxUnknownRing,
       "tmnxMcrStatsRxUnknownRingNode": tmnxMcrStatsRxUnknownRingNode,
       "tmnxMcrStatsRxDelivrdToPeer": tmnxMcrStatsRxDelivrdToPeer,
       "tmnxMcrStatsRxDelivrdToRing": tmnxMcrStatsRxDelivrdToRing,
       "tmnxMcrStatsRxDelivrdToRingNode": tmnxMcrStatsRxDelivrdToRingNode,
       "tmnxMcrStatsTx": tmnxMcrStatsTx,
       "tmnxMcrStatsTxNoBuffer": tmnxMcrStatsTxNoBuffer,
       "tmnxMcrStatsTxTransmitFailed": tmnxMcrStatsTxTransmitFailed,
       "tmnxMcrStatsMissedConfigEvent": tmnxMcrStatsMissedConfigEvent,
       "tmnxMcrStatsMissedBfdEvent": tmnxMcrStatsMissedBfdEvent,
       "tmnxMcrStatsTxUnknownDest": tmnxMcrStatsTxUnknownDest,
       "tmnxMcrRingNodeStatsTableLastChanged": tmnxMcrRingNodeStatsTableLastChanged,
       "tmnxMcrRingNodeStatsTable": tmnxMcrRingNodeStatsTable,
       "tmnxMcrRingNodeStatsEntry": tmnxMcrRingNodeStatsEntry,
       "tmnxMcrRingNodeStatsLastChanged": tmnxMcrRingNodeStatsLastChanged,
       "tmnxMcrRingNodeStatsRxDetect": tmnxMcrRingNodeStatsRxDetect,
       "tmnxMcrRingNodeStatsRxDetectAck": tmnxMcrRingNodeStatsRxDetectAck,
       "tmnxMcrRingNodeStatsRncvRxResp": tmnxMcrRingNodeStatsRncvRxResp,
       "tmnxMcrRingNodeStatsTxDetect": tmnxMcrRingNodeStatsTxDetect,
       "tmnxMcrRingNodeStatsTxDetectAck": tmnxMcrRingNodeStatsTxDetectAck,
       "tmnxMcrRingNodeStatsRncvTxReq": tmnxMcrRingNodeStatsRncvTxReq,
       "tmnxMcrRingNodeStatsRncvRtTime": tmnxMcrRingNodeStatsRncvRtTime,
       "tmnxMcEPPeerStatsTable": tmnxMcEPPeerStatsTable,
       "tmnxMcEPPeerStatsEntry": tmnxMcEPPeerStatsEntry,
       "tmnxMcEPPeerStatsPktsRx": tmnxMcEPPeerStatsPktsRx,
       "tmnxMcEPPeerStatsPktsRxKpalive": tmnxMcEPPeerStatsPktsRxKpalive,
       "tmnxMcEPPeerStatsPktsRxConfig": tmnxMcEPPeerStatsPktsRxConfig,
       "tmnxMcEPPeerStatsPktsRxPeerCfg": tmnxMcEPPeerStatsPktsRxPeerCfg,
       "tmnxMcEPPeerStatsPktsRxState": tmnxMcEPPeerStatsPktsRxState,
       "tmnxMcEPPeerStatsDropStateDsbld": tmnxMcEPPeerStatsDropStateDsbld,
       "tmnxMcEPPeerStatsDropPktTooShrt": tmnxMcEPPeerStatsDropPktTooShrt,
       "tmnxMcEPPeerStatsDropTlvInvldSz": tmnxMcEPPeerStatsDropTlvInvldSz,
       "tmnxMcEPPeerStatsDropTlvInvldId": tmnxMcEPPeerStatsDropTlvInvldId,
       "tmnxMcEPPeerStatsDropOutOfSeq": tmnxMcEPPeerStatsDropOutOfSeq,
       "tmnxMcEPPeerStatsDropUnknownTlv": tmnxMcEPPeerStatsDropUnknownTlv,
       "tmnxMcEPPeerStatsDropMD5": tmnxMcEPPeerStatsDropMD5,
       "tmnxMcEPPeerStatsPktsTx": tmnxMcEPPeerStatsPktsTx,
       "tmnxMcEPPeerStatsPktsTxKpalive": tmnxMcEPPeerStatsPktsTxKpalive,
       "tmnxMcEPPeerStatsPktsTxPeerCfg": tmnxMcEPPeerStatsPktsTxPeerCfg,
       "tmnxMcEPPeerStatsPktsTxFailed": tmnxMcEPPeerStatsPktsTxFailed,
       "tmnxMcEPPeerStatsDropEpNoPeer": tmnxMcEPPeerStatsDropEpNoPeer,
       "tmnxMcEpGlobalStats": tmnxMcEpGlobalStats,
       "tmnxMcEpStatsPktsRx": tmnxMcEpStatsPktsRx,
       "tmnxMcEpStatsPktsRxKeepalive": tmnxMcEpStatsPktsRxKeepalive,
       "tmnxMcEpStatsPktsRxConfig": tmnxMcEpStatsPktsRxConfig,
       "tmnxMcEpStatsPktsRxPeerConfig": tmnxMcEpStatsPktsRxPeerConfig,
       "tmnxMcEpStatsPktsRxState": tmnxMcEpStatsPktsRxState,
       "tmnxMcEpStatsDropPktKpaliveTask": tmnxMcEpStatsDropPktKpaliveTask,
       "tmnxMcEpStatsDropPktTooShort": tmnxMcEpStatsDropPktTooShort,
       "tmnxMcEpStatsDropPktVerifyFailed": tmnxMcEpStatsDropPktVerifyFailed,
       "tmnxMcEpStatsDropTlvInvalidSize": tmnxMcEpStatsDropTlvInvalidSize,
       "tmnxMcEpStatsDropOutOfSeq": tmnxMcEpStatsDropOutOfSeq,
       "tmnxMcEpStatsDropUnknownTlv": tmnxMcEpStatsDropUnknownTlv,
       "tmnxMcEpStatsDropTlvInvldEpId": tmnxMcEpStatsDropTlvInvldEpId,
       "tmnxMcEpStatsDropMD5": tmnxMcEpStatsDropMD5,
       "tmnxMcEpStatsDropUnknownPeer": tmnxMcEpStatsDropUnknownPeer,
       "tmnxMcEpStatsPktsTx": tmnxMcEpStatsPktsTx,
       "tmnxMcEpStatsPktsTxKeepalive": tmnxMcEpStatsPktsTxKeepalive,
       "tmnxMcEpStatsPktsTxConfig": tmnxMcEpStatsPktsTxConfig,
       "tmnxMcEpStatsPktsTxPeerConfig": tmnxMcEpStatsPktsTxPeerConfig,
       "tmnxMcEpStatsPktsTxState": tmnxMcEpStatsPktsTxState,
       "tmnxMcEpStatsPktsTxFailed": tmnxMcEpStatsPktsTxFailed,
       "tmnxMcEpStatsDropEpNoPeer": tmnxMcEpStatsDropEpNoPeer,
       "tmnxMcWppPeerStatsTableLastCh": tmnxMcWppPeerStatsTableLastCh,
       "tmnxMcWppPeerStatsTable": tmnxMcWppPeerStatsTable,
       "tmnxMcWppPeerStatsEntry": tmnxMcWppPeerStatsEntry,
       "tmnxMcWppPeerStatsInstance": tmnxMcWppPeerStatsInstance,
       "tmnxMcWppPeerStatsLastChanged": tmnxMcWppPeerStatsLastChanged,
       "tmnxMcWppPeerStatsName": tmnxMcWppPeerStatsName,
       "tmnxMcWppPeerStatsVal": tmnxMcWppPeerStatsVal,
       "tmnxMcRedundancyNotifyObjs": tmnxMcRedundancyNotifyObjs,
       "tmnxMcPeerIpAddrTypeForNotify": tmnxMcPeerIpAddrTypeForNotify,
       "tmnxMcPeerIpAddrForNotify": tmnxMcPeerIpAddrForNotify,
       "tmnxMcPeerSyncClient": tmnxMcPeerSyncClient,
       "tmnxMcRemoteGrpIfNameForNotify": tmnxMcRemoteGrpIfNameForNotify,
       "tmnxMcRemoteRedIfNameForNotify": tmnxMcRemoteRedIfNameForNotify,
       "tmnxMcRemoteSyncTag": tmnxMcRemoteSyncTag,
       "tmnxMcLagConfigLagIds": tmnxMcLagConfigLagIds,
       "tmnxMcPeerClockSkew": tmnxMcPeerClockSkew,
       "tmnxSrrpNotifBfdIntfSvcId": tmnxSrrpNotifBfdIntfSvcId,
       "tmnxSrrpNotifBfdIntfIfName": tmnxSrrpNotifBfdIntfIfName,
       "tmnxSrrpNotifBfdIntfDestIpType": tmnxSrrpNotifBfdIntfDestIpType,
       "tmnxSrrpNotifBfdIntfDestIp": tmnxSrrpNotifBfdIntfDestIp,
       "tmnxSrrpNotifBfdIntfSessState": tmnxSrrpNotifBfdIntfSessState,
       "tmnxMcPeerEPBfdSessionOpenStatus": tmnxMcPeerEPBfdSessionOpenStatus,
       "tmnxMcPeerEPPsvModeConfigState": tmnxMcPeerEPPsvModeConfigState,
       "tMcPeerIPsecTnlGrpMasterStateOld": tMcPeerIPsecTnlGrpMasterStateOld,
       "tmnxMcNotifyNumber": tmnxMcNotifyNumber,
       "tmnxMcMobRedundancyObjs": tmnxMcMobRedundancyObjs,
       "tmnxMcPeerMobileTableLstChgd": tmnxMcPeerMobileTableLstChgd,
       "tmnxMcPeerMobileTable": tmnxMcPeerMobileTable,
       "tmnxMcPeerMobileEntry": tmnxMcPeerMobileEntry,
       "tmnxMcPeerMobileRowStatus": tmnxMcPeerMobileRowStatus,
       "tmnxMcPeerMobileBFDEnable": tmnxMcPeerMobileBFDEnable,
       "tmnxMcPeerMobileRouteAdvHoldTmr": tmnxMcPeerMobileRouteAdvHoldTmr,
       "tmnxMcPeerMobileHoldOnNbrFail": tmnxMcPeerMobileHoldOnNbrFail,
       "tmnxMcPeerMobileKeepAlvIntvl": tmnxMcPeerMobileKeepAlvIntvl,
       "tmnxMcPeerMobileHoldDownTmr": tmnxMcPeerMobileHoldDownTmr,
       "tmnxMcPeerMobileAdminState": tmnxMcPeerMobileAdminState,
       "tmnxMcPeerMobileLastChanged": tmnxMcPeerMobileLastChanged,
       "tmnxMcPeerMobileMtu": tmnxMcPeerMobileMtu,
       "tmnxMcPeerMobileMGTableLstChgd": tmnxMcPeerMobileMGTableLstChgd,
       "tmnxMcPeerMobileMGTable": tmnxMcPeerMobileMGTable,
       "tmnxMcPeerMobileMGEntry": tmnxMcPeerMobileMGEntry,
       "tmnxMcPeerMobileMGRowStatus": tmnxMcPeerMobileMGRowStatus,
       "tmnxMcPeerMobileMGId": tmnxMcPeerMobileMGId,
       "tmnxMcPeerMobileMGRole": tmnxMcPeerMobileMGRole,
       "tmnxMcPeerMobileMGRefPtTrigger": tmnxMcPeerMobileMGRefPtTrigger,
       "tmnxMcPeerMobileMGAdminState": tmnxMcPeerMobileMGAdminState,
       "tmnxMcPeerMobileMGLastChanged": tmnxMcPeerMobileMGLastChanged,
       "tmnxMcPeerMobMGRefPtTableLstChgd": tmnxMcPeerMobMGRefPtTableLstChgd,
       "tmnxMcPeerMobileMGRefPtTable": tmnxMcPeerMobileMGRefPtTable,
       "tmnxMcPeerMobileMGRefPtEntry": tmnxMcPeerMobileMGRefPtEntry,
       "tmnxMcPeerMobileMGRefPtRowStatus": tmnxMcPeerMobileMGRefPtRowStatus,
       "tmnxMcPeerMobileMGRefPt": tmnxMcPeerMobileMGRefPt,
       "tmnxMcPeerMobileMGRefPtPktCnt": tmnxMcPeerMobileMGRefPtPktCnt,
       "tmnxMcPeerMobileMGRefPtLastChngd": tmnxMcPeerMobileMGRefPtLastChngd,
       "tmnxMcMobRedundancyStatsObjs": tmnxMcMobRedundancyStatsObjs,
       "tmnxMcMobRedundancyNotifyObjs": tmnxMcMobRedundancyNotifyObjs,
       "tmnxMcRedundancyNotifyPrefix": tmnxMcRedundancyNotifyPrefix,
       "tmnxMcRedundancyNotifications": tmnxMcRedundancyNotifications,
       "tmnxMcRedundancyPeerStateChanged": tmnxMcRedundancyPeerStateChanged,
       "tmnxMcRedundancyMismatchDetected": tmnxMcRedundancyMismatchDetected,
       "tmnxMcRedundancyMismatchResolved": tmnxMcRedundancyMismatchResolved,
       "tmnxMcPeerSyncStatusChanged": tmnxMcPeerSyncStatusChanged,
       "tmnxMcSyncClientAlarmRaised": tmnxMcSyncClientAlarmRaised,
       "tmnxMcSyncClientAlarmCleared": tmnxMcSyncClientAlarmCleared,
       "tmnxSrrpSubnetMismatch": tmnxSrrpSubnetMismatch,
       "tmnxSrrpSubnetMismatchCleared": tmnxSrrpSubnetMismatchCleared,
       "tmnxSrrpInstanceIdMismatch": tmnxSrrpInstanceIdMismatch,
       "tmnxSrrpSapMismatch": tmnxSrrpSapMismatch,
       "tmnxSrrpSapTagMismatch": tmnxSrrpSapTagMismatch,
       "tmnxSrrpRedIfMismatch": tmnxSrrpRedIfMismatch,
       "tmnxSrrpDualMaster": tmnxSrrpDualMaster,
       "tmnxMcLagInfoLagChanged": tmnxMcLagInfoLagChanged,
       "tmnxSrrpSystemIpNotSet": tmnxSrrpSystemIpNotSet,
       "tmnxMcRingOperStateChanged": tmnxMcRingOperStateChanged,
       "tmnxMcRingInbCtrlOperStateChgd": tmnxMcRingInbCtrlOperStateChgd,
       "tmnxMcRingNodeLocOperStateChgd": tmnxMcRingNodeLocOperStateChgd,
       "tmnxMcSyncClockSkewRaised": tmnxMcSyncClockSkewRaised,
       "tmnxMcSyncClockSkewCleared": tmnxMcSyncClockSkewCleared,
       "tmnxSrrpDuplicateSubIfAddress": tmnxSrrpDuplicateSubIfAddress,
       "tmnxMcPeerRingsOperStateChanged": tmnxMcPeerRingsOperStateChanged,
       "tmnxSrrpTrapNewMaster": tmnxSrrpTrapNewMaster,
       "tmnxSrrpBecameBackup": tmnxSrrpBecameBackup,
       "tmnxSrrpBfdIntfSessStateChgd": tmnxSrrpBfdIntfSessStateChgd,
       "tmnxMcPeerEPBfdSessionOpen": tmnxMcPeerEPBfdSessionOpen,
       "tmnxMcPeerEPBfdSessionClose": tmnxMcPeerEPBfdSessionClose,
       "tmnxMcPeerEPBfdSessionUp": tmnxMcPeerEPBfdSessionUp,
       "tmnxMcPeerEPBfdSessionDown": tmnxMcPeerEPBfdSessionDown,
       "tmnxMcPeerEPOperDown": tmnxMcPeerEPOperDown,
       "tmnxMcPeerEPOperUp": tmnxMcPeerEPOperUp,
       "tmnxMCEPSessionPsvModeEnabled": tmnxMCEPSessionPsvModeEnabled,
       "tmnxMCEPSessionPsvModeDisabled": tmnxMCEPSessionPsvModeDisabled,
       "tMcPeerIPsecTnlGrpMasterStateChg": tMcPeerIPsecTnlGrpMasterStateChg,
       "tMcPeerIPsecTnlGrpProtStatusChg": tMcPeerIPsecTnlGrpProtStatusChg,
       "tmnxMcOmcrStatFailedChanged": tmnxMcOmcrStatFailedChanged,
       "tmnxMcOmcrClientNumEntriesHigh": tmnxMcOmcrClientNumEntriesHigh,
       "tmnxSrrpOperDownInvalidMac": tmnxSrrpOperDownInvalidMac,
       "tmnxSrrpOperDownInvalidMacClear": tmnxSrrpOperDownInvalidMacClear,
       "tmnxMcMobRedundancyNotifications": tmnxMcMobRedundancyNotifications}
)
