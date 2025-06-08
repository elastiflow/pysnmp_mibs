# SNMP MIB module (TN-MC-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-MC-REDUNDANCY-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(LAGInterfaceNumber,) = mibBuilder.importSymbols(
    "TN-LAG-MIB",
    "LAGInterfaceNumber")

(tnSapEncapValue,
 tnSapPortId) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapEncapValue",
    "tnSapPortId")

(tnSvcId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "tnSvcId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrID")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnMcRedundancyMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 40)
)
if mibBuilder.loadTexts:
    tnMcRedundancyMIBModule.setRevisions(
        ("1912-11-28 00:00",)
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
              8)
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
          ("subMgmtPppoe", 8))
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



# MIB Managed Objects in the order of their OIDs

_TnMcRedundancy_ObjectIdentity = ObjectIdentity
tnMcRedundancy = _TnMcRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40)
)
_TnMcRedundancyObjs_ObjectIdentity = ObjectIdentity
tnMcRedundancyObjs = _TnMcRedundancyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1)
)
_TnMcPeerTable_Object = MibTable
tnMcPeerTable = _TnMcPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    tnMcPeerTable.setStatus("current")
_TnMcPeerEntry_Object = MibTableRow
tnMcPeerEntry = _TnMcPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1)
)
tnMcPeerEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tnMcPeerEntry.setStatus("current")
_TnMcPeerIpType_Type = InetAddressType
_TnMcPeerIpType_Object = MibTableColumn
tnMcPeerIpType = _TnMcPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 1),
    _TnMcPeerIpType_Type()
)
tnMcPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcPeerIpType.setStatus("current")
_TnMcPeerIpAddr_Type = InetAddress
_TnMcPeerIpAddr_Object = MibTableColumn
tnMcPeerIpAddr = _TnMcPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 2),
    _TnMcPeerIpAddr_Type()
)
tnMcPeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcPeerIpAddr.setStatus("current")
_TnMcPeerRowStatus_Type = RowStatus
_TnMcPeerRowStatus_Object = MibTableColumn
tnMcPeerRowStatus = _TnMcPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 3),
    _TnMcPeerRowStatus_Type()
)
tnMcPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerRowStatus.setStatus("current")


class _TnMcPeerDescription_Type(TItemDescription):
    """Custom type tnMcPeerDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TnMcPeerDescription_Type.__name__ = "TItemDescription"
_TnMcPeerDescription_Object = MibTableColumn
tnMcPeerDescription = _TnMcPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 4),
    _TnMcPeerDescription_Type()
)
tnMcPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerDescription.setStatus("current")


class _TnMcPeerAuthKey_Type(OctetString):
    """Custom type tnMcPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnMcPeerAuthKey_Type.__name__ = "OctetString"
_TnMcPeerAuthKey_Object = MibTableColumn
tnMcPeerAuthKey = _TnMcPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 5),
    _TnMcPeerAuthKey_Type()
)
tnMcPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerAuthKey.setStatus("current")


class _TnMcPeerSrcIpType_Type(InetAddressType):
    """Custom type tnMcPeerSrcIpType based on InetAddressType"""
    defaultValue = 0


_TnMcPeerSrcIpType_Type.__name__ = "InetAddressType"
_TnMcPeerSrcIpType_Object = MibTableColumn
tnMcPeerSrcIpType = _TnMcPeerSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 6),
    _TnMcPeerSrcIpType_Type()
)
tnMcPeerSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSrcIpType.setStatus("current")


class _TnMcPeerSrcIpAddr_Type(InetAddress):
    """Custom type tnMcPeerSrcIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TnMcPeerSrcIpAddr_Type.__name__ = "InetAddress"
_TnMcPeerSrcIpAddr_Object = MibTableColumn
tnMcPeerSrcIpAddr = _TnMcPeerSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 7),
    _TnMcPeerSrcIpAddr_Type()
)
tnMcPeerSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSrcIpAddr.setStatus("current")


class _TnMcPeerAdminState_Type(TmnxAdminState):
    """Custom type tnMcPeerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TnMcPeerAdminState_Type.__name__ = "TmnxAdminState"
_TnMcPeerAdminState_Object = MibTableColumn
tnMcPeerAdminState = _TnMcPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 8),
    _TnMcPeerAdminState_Type()
)
tnMcPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerAdminState.setStatus("current")
_TnMcPeerSrcIpOperType_Type = InetAddressType
_TnMcPeerSrcIpOperType_Object = MibTableColumn
tnMcPeerSrcIpOperType = _TnMcPeerSrcIpOperType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 9),
    _TnMcPeerSrcIpOperType_Type()
)
tnMcPeerSrcIpOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSrcIpOperType.setStatus("current")


class _TnMcPeerSrcIpOperAddr_Type(InetAddress):
    """Custom type tnMcPeerSrcIpOperAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TnMcPeerSrcIpOperAddr_Type.__name__ = "InetAddress"
_TnMcPeerSrcIpOperAddr_Object = MibTableColumn
tnMcPeerSrcIpOperAddr = _TnMcPeerSrcIpOperAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 10),
    _TnMcPeerSrcIpOperAddr_Type()
)
tnMcPeerSrcIpOperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSrcIpOperAddr.setStatus("current")
_TnMcPeerRingsOperState_Type = TmnxOperState
_TnMcPeerRingsOperState_Object = MibTableColumn
tnMcPeerRingsOperState = _TnMcPeerRingsOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 11),
    _TnMcPeerRingsOperState_Type()
)
tnMcPeerRingsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerRingsOperState.setStatus("current")


class _TnMcPeerName_Type(TNamedItemOrEmpty):
    """Custom type tnMcPeerName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TnMcPeerName_Type.__name__ = "TNamedItemOrEmpty"
_TnMcPeerName_Object = MibTableColumn
tnMcPeerName = _TnMcPeerName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 1, 1, 12),
    _TnMcPeerName_Type()
)
tnMcPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerName.setStatus("current")
_TnMcPeerSyncTable_Object = MibTable
tnMcPeerSyncTable = _TnMcPeerSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    tnMcPeerSyncTable.setStatus("current")
_TnMcPeerSyncEntry_Object = MibTableRow
tnMcPeerSyncEntry = _TnMcPeerSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1)
)
tnMcPeerSyncEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tnMcPeerSyncEntry.setStatus("current")
_TnMcPeerSyncRowStatus_Type = RowStatus
_TnMcPeerSyncRowStatus_Object = MibTableColumn
tnMcPeerSyncRowStatus = _TnMcPeerSyncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 1),
    _TnMcPeerSyncRowStatus_Type()
)
tnMcPeerSyncRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncRowStatus.setStatus("current")


class _TnMcPeerSyncIgmp_Type(TruthValue):
    """Custom type tnMcPeerSyncIgmp based on TruthValue"""
    defaultValue = 2


_TnMcPeerSyncIgmp_Type.__name__ = "TruthValue"
_TnMcPeerSyncIgmp_Object = MibTableColumn
tnMcPeerSyncIgmp = _TnMcPeerSyncIgmp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 2),
    _TnMcPeerSyncIgmp_Type()
)
tnMcPeerSyncIgmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncIgmp.setStatus("current")


class _TnMcPeerSyncIgmpSnooping_Type(TruthValue):
    """Custom type tnMcPeerSyncIgmpSnooping based on TruthValue"""
    defaultValue = 2


_TnMcPeerSyncIgmpSnooping_Type.__name__ = "TruthValue"
_TnMcPeerSyncIgmpSnooping_Object = MibTableColumn
tnMcPeerSyncIgmpSnooping = _TnMcPeerSyncIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 3),
    _TnMcPeerSyncIgmpSnooping_Type()
)
tnMcPeerSyncIgmpSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncIgmpSnooping.setStatus("current")


class _TnMcPeerSyncSubMgmt_Type(TruthValue):
    """Custom type tnMcPeerSyncSubMgmt based on TruthValue"""
    defaultValue = 2


_TnMcPeerSyncSubMgmt_Type.__name__ = "TruthValue"
_TnMcPeerSyncSubMgmt_Object = MibTableColumn
tnMcPeerSyncSubMgmt = _TnMcPeerSyncSubMgmt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 4),
    _TnMcPeerSyncSubMgmt_Type()
)
tnMcPeerSyncSubMgmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncSubMgmt.setStatus("current")


class _TnMcPeerSyncSrrp_Type(TruthValue):
    """Custom type tnMcPeerSyncSrrp based on TruthValue"""
    defaultValue = 2


_TnMcPeerSyncSrrp_Type.__name__ = "TruthValue"
_TnMcPeerSyncSrrp_Object = MibTableColumn
tnMcPeerSyncSrrp = _TnMcPeerSyncSrrp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 5),
    _TnMcPeerSyncSrrp_Type()
)
tnMcPeerSyncSrrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncSrrp.setStatus("current")


class _TnMcPeerSyncAdminState_Type(TmnxAdminState):
    """Custom type tnMcPeerSyncAdminState based on TmnxAdminState"""
    defaultValue = 3


_TnMcPeerSyncAdminState_Type.__name__ = "TmnxAdminState"
_TnMcPeerSyncAdminState_Object = MibTableColumn
tnMcPeerSyncAdminState = _TnMcPeerSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 6),
    _TnMcPeerSyncAdminState_Type()
)
tnMcPeerSyncAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncAdminState.setStatus("current")
_TnMcPeerSyncOperState_Type = TmnxOperState
_TnMcPeerSyncOperState_Object = MibTableColumn
tnMcPeerSyncOperState = _TnMcPeerSyncOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 7),
    _TnMcPeerSyncOperState_Type()
)
tnMcPeerSyncOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncOperState.setStatus("current")


class _TnMcPeerSyncOperFlags_Type(Bits):
    """Custom type tnMcPeerSyncOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("syncAdminDown", 0),
          ("peerAdminDown", 1),
          ("connectionDown", 2),
          ("internalError", 3),
          ("mcsVersionMismatch", 4),
          ("platformMismatch", 5),
          ("appVersionMismatch", 6),
          ("appSupportMismatch", 7))
    )

_TnMcPeerSyncOperFlags_Type.__name__ = "Bits"
_TnMcPeerSyncOperFlags_Object = MibTableColumn
tnMcPeerSyncOperFlags = _TnMcPeerSyncOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 8),
    _TnMcPeerSyncOperFlags_Type()
)
tnMcPeerSyncOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncOperFlags.setStatus("current")


class _TnMcPeerSyncStatus_Type(Integer32):
    """Custom type tnMcPeerSyncStatus based on Integer32"""
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


_TnMcPeerSyncStatus_Type.__name__ = "Integer32"
_TnMcPeerSyncStatus_Object = MibTableColumn
tnMcPeerSyncStatus = _TnMcPeerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 9),
    _TnMcPeerSyncStatus_Type()
)
tnMcPeerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncStatus.setStatus("current")
_TnMcPeerSyncLastSyncTime_Type = TimeStamp
_TnMcPeerSyncLastSyncTime_Object = MibTableColumn
tnMcPeerSyncLastSyncTime = _TnMcPeerSyncLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 10),
    _TnMcPeerSyncLastSyncTime_Type()
)
tnMcPeerSyncLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncLastSyncTime.setStatus("current")
_TnMcPeerSyncNumEntries_Type = Counter32
_TnMcPeerSyncNumEntries_Object = MibTableColumn
tnMcPeerSyncNumEntries = _TnMcPeerSyncNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 11),
    _TnMcPeerSyncNumEntries_Type()
)
tnMcPeerSyncNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncNumEntries.setStatus("current")
_TnMcPeerSyncLclDeletedEntries_Type = Counter32
_TnMcPeerSyncLclDeletedEntries_Object = MibTableColumn
tnMcPeerSyncLclDeletedEntries = _TnMcPeerSyncLclDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 12),
    _TnMcPeerSyncLclDeletedEntries_Type()
)
tnMcPeerSyncLclDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncLclDeletedEntries.setStatus("current")
_TnMcPeerSyncAlarmedEntries_Type = Counter32
_TnMcPeerSyncAlarmedEntries_Object = MibTableColumn
tnMcPeerSyncAlarmedEntries = _TnMcPeerSyncAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 13),
    _TnMcPeerSyncAlarmedEntries_Type()
)
tnMcPeerSyncAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncAlarmedEntries.setStatus("current")
_TnMcPeerSyncRemNumEntries_Type = Counter32
_TnMcPeerSyncRemNumEntries_Object = MibTableColumn
tnMcPeerSyncRemNumEntries = _TnMcPeerSyncRemNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 14),
    _TnMcPeerSyncRemNumEntries_Type()
)
tnMcPeerSyncRemNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncRemNumEntries.setStatus("current")
_TnMcPeerSyncRemLclDelEntries_Type = Counter32
_TnMcPeerSyncRemLclDelEntries_Object = MibTableColumn
tnMcPeerSyncRemLclDelEntries = _TnMcPeerSyncRemLclDelEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 15),
    _TnMcPeerSyncRemLclDelEntries_Type()
)
tnMcPeerSyncRemLclDelEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncRemLclDelEntries.setStatus("current")
_TnMcPeerSyncRemAlarmedEntries_Type = Counter32
_TnMcPeerSyncRemAlarmedEntries_Object = MibTableColumn
tnMcPeerSyncRemAlarmedEntries = _TnMcPeerSyncRemAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 2, 1, 16),
    _TnMcPeerSyncRemAlarmedEntries_Type()
)
tnMcPeerSyncRemAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncRemAlarmedEntries.setStatus("current")
_TnMcPeerSyncPortTable_Object = MibTable
tnMcPeerSyncPortTable = _TnMcPeerSyncPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 3)
)
if mibBuilder.loadTexts:
    tnMcPeerSyncPortTable.setStatus("current")
_TnMcPeerSyncPortEntry_Object = MibTableRow
tnMcPeerSyncPortEntry = _TnMcPeerSyncPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 3, 1)
)
tnMcPeerSyncPortEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerSyncPortId"),
)
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEntry.setStatus("current")
_TnMcPeerSyncPortId_Type = TmnxPortID
_TnMcPeerSyncPortId_Object = MibTableColumn
tnMcPeerSyncPortId = _TnMcPeerSyncPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 3, 1, 1),
    _TnMcPeerSyncPortId_Type()
)
tnMcPeerSyncPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortId.setStatus("current")
_TnMcPeerSyncPortRowStatus_Type = RowStatus
_TnMcPeerSyncPortRowStatus_Object = MibTableColumn
tnMcPeerSyncPortRowStatus = _TnMcPeerSyncPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 3, 1, 2),
    _TnMcPeerSyncPortRowStatus_Type()
)
tnMcPeerSyncPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortRowStatus.setStatus("current")


class _TnMcPeerSyncPortSyncTag_Type(TNamedItemOrEmpty):
    """Custom type tnMcPeerSyncPortSyncTag based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnMcPeerSyncPortSyncTag_Type.__name__ = "TNamedItemOrEmpty"
_TnMcPeerSyncPortSyncTag_Object = MibTableColumn
tnMcPeerSyncPortSyncTag = _TnMcPeerSyncPortSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 3, 1, 3),
    _TnMcPeerSyncPortSyncTag_Type()
)
tnMcPeerSyncPortSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortSyncTag.setStatus("current")
_TnMcPeerSyncPortEncapRangeTable_Object = MibTable
tnMcPeerSyncPortEncapRangeTable = _TnMcPeerSyncPortEncapRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4)
)
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapRangeTable.setStatus("current")
_TnMcPeerSyncPortEncapRangeEntry_Object = MibTableRow
tnMcPeerSyncPortEncapRangeEntry = _TnMcPeerSyncPortEncapRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4, 1)
)
tnMcPeerSyncPortEncapRangeEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerSyncPortId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerSyncPortEncapType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerSyncPortEncapMin"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerSyncPortEncapMax"),
)
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapRangeEntry.setStatus("current")


class _TnMcPeerSyncPortEncapType_Type(Integer32):
    """Custom type tnMcPeerSyncPortEncapType based on Integer32"""
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


_TnMcPeerSyncPortEncapType_Type.__name__ = "Integer32"
_TnMcPeerSyncPortEncapType_Object = MibTableColumn
tnMcPeerSyncPortEncapType = _TnMcPeerSyncPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4, 1, 1),
    _TnMcPeerSyncPortEncapType_Type()
)
tnMcPeerSyncPortEncapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapType.setStatus("current")
_TnMcPeerSyncPortEncapMin_Type = TmnxEncapVal
_TnMcPeerSyncPortEncapMin_Object = MibTableColumn
tnMcPeerSyncPortEncapMin = _TnMcPeerSyncPortEncapMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4, 1, 2),
    _TnMcPeerSyncPortEncapMin_Type()
)
tnMcPeerSyncPortEncapMin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapMin.setStatus("current")
_TnMcPeerSyncPortEncapMax_Type = TmnxEncapVal
_TnMcPeerSyncPortEncapMax_Object = MibTableColumn
tnMcPeerSyncPortEncapMax = _TnMcPeerSyncPortEncapMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4, 1, 3),
    _TnMcPeerSyncPortEncapMax_Type()
)
tnMcPeerSyncPortEncapMax.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapMax.setStatus("current")
_TnMcPeerSyncPortEncapRowStatus_Type = RowStatus
_TnMcPeerSyncPortEncapRowStatus_Object = MibTableColumn
tnMcPeerSyncPortEncapRowStatus = _TnMcPeerSyncPortEncapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4, 1, 4),
    _TnMcPeerSyncPortEncapRowStatus_Type()
)
tnMcPeerSyncPortEncapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapRowStatus.setStatus("current")
_TnMcPeerSyncPortEncapSyncTag_Type = TNamedItem
_TnMcPeerSyncPortEncapSyncTag_Object = MibTableColumn
tnMcPeerSyncPortEncapSyncTag = _TnMcPeerSyncPortEncapSyncTag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 4, 1, 5),
    _TnMcPeerSyncPortEncapSyncTag_Type()
)
tnMcPeerSyncPortEncapSyncTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcPeerSyncPortEncapSyncTag.setStatus("current")
_TnMcLagConfigTableLastChanged_Type = TimeStamp
_TnMcLagConfigTableLastChanged_Object = MibScalar
tnMcLagConfigTableLastChanged = _TnMcLagConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 5),
    _TnMcLagConfigTableLastChanged_Type()
)
tnMcLagConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigTableLastChanged.setStatus("current")
_TnMcLagConfigTable_Object = MibTable
tnMcLagConfigTable = _TnMcLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6)
)
if mibBuilder.loadTexts:
    tnMcLagConfigTable.setStatus("current")
_TnMcLagConfigEntry_Object = MibTableRow
tnMcLagConfigEntry = _TnMcLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1)
)
tnMcLagConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tnMcLagConfigEntry.setStatus("current")
_TnMcLagConfigPeerLastChanged_Type = TimeStamp
_TnMcLagConfigPeerLastChanged_Object = MibTableColumn
tnMcLagConfigPeerLastChanged = _TnMcLagConfigPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1, 1),
    _TnMcLagConfigPeerLastChanged_Type()
)
tnMcLagConfigPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigPeerLastChanged.setStatus("current")


class _TnMcLagConfigPeerAdminstate_Type(TmnxAdminState):
    """Custom type tnMcLagConfigPeerAdminstate based on TmnxAdminState"""
    defaultValue = 3


_TnMcLagConfigPeerAdminstate_Type.__name__ = "TmnxAdminState"
_TnMcLagConfigPeerAdminstate_Object = MibTableColumn
tnMcLagConfigPeerAdminstate = _TnMcLagConfigPeerAdminstate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1, 2),
    _TnMcLagConfigPeerAdminstate_Type()
)
tnMcLagConfigPeerAdminstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMcLagConfigPeerAdminstate.setStatus("current")


class _TnMcLagConfigKeepALiveIvl_Type(Unsigned32):
    """Custom type tnMcLagConfigKeepALiveIvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_TnMcLagConfigKeepALiveIvl_Type.__name__ = "Unsigned32"
_TnMcLagConfigKeepALiveIvl_Object = MibTableColumn
tnMcLagConfigKeepALiveIvl = _TnMcLagConfigKeepALiveIvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1, 3),
    _TnMcLagConfigKeepALiveIvl_Type()
)
tnMcLagConfigKeepALiveIvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMcLagConfigKeepALiveIvl.setStatus("current")
if mibBuilder.loadTexts:
    tnMcLagConfigKeepALiveIvl.setUnits("deci-seconds")


class _TnMcLagConfigHoldOnNgbrFailure_Type(Unsigned32):
    """Custom type tnMcLagConfigHoldOnNgbrFailure based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 25),
    )


_TnMcLagConfigHoldOnNgbrFailure_Type.__name__ = "Unsigned32"
_TnMcLagConfigHoldOnNgbrFailure_Object = MibTableColumn
tnMcLagConfigHoldOnNgbrFailure = _TnMcLagConfigHoldOnNgbrFailure_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1, 4),
    _TnMcLagConfigHoldOnNgbrFailure_Type()
)
tnMcLagConfigHoldOnNgbrFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMcLagConfigHoldOnNgbrFailure.setStatus("current")


class _TnMcLagConfigOperState_Type(Integer32):
    """Custom type tnMcLagConfigOperState based on Integer32"""
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


_TnMcLagConfigOperState_Type.__name__ = "Integer32"
_TnMcLagConfigOperState_Object = MibTableColumn
tnMcLagConfigOperState = _TnMcLagConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1, 5),
    _TnMcLagConfigOperState_Type()
)
tnMcLagConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigOperState.setStatus("current")
_TnMcLagConfigPeerLastStateChge_Type = TimeStamp
_TnMcLagConfigPeerLastStateChge_Object = MibTableColumn
tnMcLagConfigPeerLastStateChge = _TnMcLagConfigPeerLastStateChge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 6, 1, 6),
    _TnMcLagConfigPeerLastStateChge_Type()
)
tnMcLagConfigPeerLastStateChge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigPeerLastStateChge.setStatus("current")
_TnMcLagConfigLagTableLastChanged_Type = TimeStamp
_TnMcLagConfigLagTableLastChanged_Object = MibScalar
tnMcLagConfigLagTableLastChanged = _TnMcLagConfigLagTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 7),
    _TnMcLagConfigLagTableLastChanged_Type()
)
tnMcLagConfigLagTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigLagTableLastChanged.setStatus("current")
_TnMcLagConfigLagTable_Object = MibTable
tnMcLagConfigLagTable = _TnMcLagConfigLagTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8)
)
if mibBuilder.loadTexts:
    tnMcLagConfigLagTable.setStatus("current")
_TnMcLagConfigLagEntry_Object = MibTableRow
tnMcLagConfigLagEntry = _TnMcLagConfigLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1)
)
tnMcLagConfigLagEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcLagConfigLagId"),
)
if mibBuilder.loadTexts:
    tnMcLagConfigLagEntry.setStatus("current")
_TnMcLagConfigLagId_Type = LAGInterfaceNumber
_TnMcLagConfigLagId_Object = MibTableColumn
tnMcLagConfigLagId = _TnMcLagConfigLagId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 1),
    _TnMcLagConfigLagId_Type()
)
tnMcLagConfigLagId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcLagConfigLagId.setStatus("current")
_TnMcLagConfigLagLastChanged_Type = TimeStamp
_TnMcLagConfigLagLastChanged_Object = MibTableColumn
tnMcLagConfigLagLastChanged = _TnMcLagConfigLagLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 2),
    _TnMcLagConfigLagLastChanged_Type()
)
tnMcLagConfigLagLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigLagLastChanged.setStatus("current")
_TnMcLagConfigLagRowStatus_Type = RowStatus
_TnMcLagConfigLagRowStatus_Object = MibTableColumn
tnMcLagConfigLagRowStatus = _TnMcLagConfigLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 3),
    _TnMcLagConfigLagRowStatus_Type()
)
tnMcLagConfigLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLagRowStatus.setStatus("current")


class _TnMcLagConfigLaglacpKey_Type(Unsigned32):
    """Custom type tnMcLagConfigLaglacpKey based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnMcLagConfigLaglacpKey_Type.__name__ = "Unsigned32"
_TnMcLagConfigLaglacpKey_Object = MibTableColumn
tnMcLagConfigLaglacpKey = _TnMcLagConfigLaglacpKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 4),
    _TnMcLagConfigLaglacpKey_Type()
)
tnMcLagConfigLaglacpKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLaglacpKey.setStatus("current")


class _TnMcLagConfigLagSystemId_Type(OctetString):
    """Custom type tnMcLagConfigLagSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TnMcLagConfigLagSystemId_Type.__name__ = "OctetString"
_TnMcLagConfigLagSystemId_Object = MibTableColumn
tnMcLagConfigLagSystemId = _TnMcLagConfigLagSystemId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 5),
    _TnMcLagConfigLagSystemId_Type()
)
tnMcLagConfigLagSystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLagSystemId.setStatus("current")


class _TnMcLagConfigLagSystemPriority_Type(Unsigned32):
    """Custom type tnMcLagConfigLagSystemPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnMcLagConfigLagSystemPriority_Type.__name__ = "Unsigned32"
_TnMcLagConfigLagSystemPriority_Object = MibTableColumn
tnMcLagConfigLagSystemPriority = _TnMcLagConfigLagSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 6),
    _TnMcLagConfigLagSystemPriority_Type()
)
tnMcLagConfigLagSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLagSystemPriority.setStatus("current")
_TnMcLagConfigLagRemoteLagId_Type = LAGInterfaceNumber
_TnMcLagConfigLagRemoteLagId_Object = MibTableColumn
tnMcLagConfigLagRemoteLagId = _TnMcLagConfigLagRemoteLagId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 7),
    _TnMcLagConfigLagRemoteLagId_Type()
)
tnMcLagConfigLagRemoteLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLagRemoteLagId.setStatus("current")


class _TnMcLagConfigLagSrcBMacLSB_Type(Unsigned32):
    """Custom type tnMcLagConfigLagSrcBMacLSB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TnMcLagConfigLagSrcBMacLSB_Type.__name__ = "Unsigned32"
_TnMcLagConfigLagSrcBMacLSB_Object = MibTableColumn
tnMcLagConfigLagSrcBMacLSB = _TnMcLagConfigLagSrcBMacLSB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 8),
    _TnMcLagConfigLagSrcBMacLSB_Type()
)
tnMcLagConfigLagSrcBMacLSB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLagSrcBMacLSB.setStatus("current")
_TnMcLagConfigLagOperSrcBMacLSB_Type = Unsigned32
_TnMcLagConfigLagOperSrcBMacLSB_Object = MibTableColumn
tnMcLagConfigLagOperSrcBMacLSB = _TnMcLagConfigLagOperSrcBMacLSB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 9),
    _TnMcLagConfigLagOperSrcBMacLSB_Type()
)
tnMcLagConfigLagOperSrcBMacLSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigLagOperSrcBMacLSB.setStatus("current")


class _TnMcLagConfigLagFlushEthRingOnActive_Type(TmnxEnabledDisabled):
    """Custom type tnMcLagConfigLagFlushEthRingOnActive based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnMcLagConfigLagFlushEthRingOnActive_Type.__name__ = "TmnxEnabledDisabled"
_TnMcLagConfigLagFlushEthRingOnActive_Object = MibTableColumn
tnMcLagConfigLagFlushEthRingOnActive = _TnMcLagConfigLagFlushEthRingOnActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 8, 1, 10),
    _TnMcLagConfigLagFlushEthRingOnActive_Type()
)
tnMcLagConfigLagFlushEthRingOnActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcLagConfigLagFlushEthRingOnActive.setStatus("current")
_TnMcLagInfoLagTable_Object = MibTable
tnMcLagInfoLagTable = _TnMcLagInfoLagTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10)
)
if mibBuilder.loadTexts:
    tnMcLagInfoLagTable.setStatus("current")
_TnMcLagInfoLagEntry_Object = MibTableRow
tnMcLagInfoLagEntry = _TnMcLagInfoLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tnMcLagInfoLagEntry.setStatus("current")
_TnMcLagActiveStandby_Type = TruthValue
_TnMcLagActiveStandby_Object = MibTableColumn
tnMcLagActiveStandby = _TnMcLagActiveStandby_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1, 1),
    _TnMcLagActiveStandby_Type()
)
tnMcLagActiveStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagActiveStandby.setStatus("current")
_TnMcLagLacpIdInUse_Type = TruthValue
_TnMcLagLacpIdInUse_Object = MibTableColumn
tnMcLagLacpIdInUse = _TnMcLagLacpIdInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1, 2),
    _TnMcLagLacpIdInUse_Type()
)
tnMcLagLacpIdInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagLacpIdInUse.setStatus("current")
_TnMcLagExtendedTimeOut_Type = TruthValue
_TnMcLagExtendedTimeOut_Object = MibTableColumn
tnMcLagExtendedTimeOut = _TnMcLagExtendedTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1, 3),
    _TnMcLagExtendedTimeOut_Type()
)
tnMcLagExtendedTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagExtendedTimeOut.setStatus("current")
_TnMcLagSelectionLogic_Type = DisplayString
_TnMcLagSelectionLogic_Object = MibTableColumn
tnMcLagSelectionLogic = _TnMcLagSelectionLogic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1, 4),
    _TnMcLagSelectionLogic_Type()
)
tnMcLagSelectionLogic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagSelectionLogic.setStatus("current")
_TnMcLagConfigMismatchString_Type = DisplayString
_TnMcLagConfigMismatchString_Object = MibTableColumn
tnMcLagConfigMismatchString = _TnMcLagConfigMismatchString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1, 5),
    _TnMcLagConfigMismatchString_Type()
)
tnMcLagConfigMismatchString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigMismatchString.setStatus("current")


class _TnMcLagConfigMismatchFlags_Type(Bits):
    """Custom type tnMcLagConfigMismatchFlags based on Bits"""
    namedValues = NamedValues(
        *(("lagIsNotMultiChassis", 0),
          ("localRemoteLagIdMismatch", 1),
          ("lagSelectionCriteriaMismatch", 2),
          ("lagEncapsulationMismatch", 3),
          ("mcLacpkeyMismatch", 4),
          ("mcSystemPriorityMismatch", 5),
          ("mcSystemIdMismatch", 6))
    )

_TnMcLagConfigMismatchFlags_Type.__name__ = "Bits"
_TnMcLagConfigMismatchFlags_Object = MibTableColumn
tnMcLagConfigMismatchFlags = _TnMcLagConfigMismatchFlags_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 10, 1, 6),
    _TnMcLagConfigMismatchFlags_Type()
)
tnMcLagConfigMismatchFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagConfigMismatchFlags.setStatus("current")
_TnMcsClientAppTable_Object = MibTable
tnMcsClientAppTable = _TnMcsClientAppTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11)
)
if mibBuilder.loadTexts:
    tnMcsClientAppTable.setStatus("current")
_TnMcsClientAppEntry_Object = MibTableRow
tnMcsClientAppEntry = _TnMcsClientAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1)
)
tnMcsClientAppEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcsClientApplication"),
)
if mibBuilder.loadTexts:
    tnMcsClientAppEntry.setStatus("current")
_TnMcsClientApplication_Type = TmnxMcsClientApp
_TnMcsClientApplication_Object = MibTableColumn
tnMcsClientApplication = _TnMcsClientApplication_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 1),
    _TnMcsClientApplication_Type()
)
tnMcsClientApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcsClientApplication.setStatus("current")
_TnMcsClientNumEntries_Type = Counter32
_TnMcsClientNumEntries_Object = MibTableColumn
tnMcsClientNumEntries = _TnMcsClientNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 2),
    _TnMcsClientNumEntries_Type()
)
tnMcsClientNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcsClientNumEntries.setStatus("current")
_TnMcsClientLclDeletedEntries_Type = Counter32
_TnMcsClientLclDeletedEntries_Object = MibTableColumn
tnMcsClientLclDeletedEntries = _TnMcsClientLclDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 3),
    _TnMcsClientLclDeletedEntries_Type()
)
tnMcsClientLclDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcsClientLclDeletedEntries.setStatus("current")
_TnMcsClientAlarmedEntries_Type = Counter32
_TnMcsClientAlarmedEntries_Object = MibTableColumn
tnMcsClientAlarmedEntries = _TnMcsClientAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 4),
    _TnMcsClientAlarmedEntries_Type()
)
tnMcsClientAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcsClientAlarmedEntries.setStatus("current")
_TnMcsClientRemNumEntries_Type = Counter32
_TnMcsClientRemNumEntries_Object = MibTableColumn
tnMcsClientRemNumEntries = _TnMcsClientRemNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 5),
    _TnMcsClientRemNumEntries_Type()
)
tnMcsClientRemNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcsClientRemNumEntries.setStatus("current")
_TnMcsClientRemLclDelEntries_Type = Counter32
_TnMcsClientRemLclDelEntries_Object = MibTableColumn
tnMcsClientRemLclDelEntries = _TnMcsClientRemLclDelEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 6),
    _TnMcsClientRemLclDelEntries_Type()
)
tnMcsClientRemLclDelEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcsClientRemLclDelEntries.setStatus("current")
_TnMcsClientRemAlarmedEntries_Type = Counter32
_TnMcsClientRemAlarmedEntries_Object = MibTableColumn
tnMcsClientRemAlarmedEntries = _TnMcsClientRemAlarmedEntries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 11, 1, 7),
    _TnMcsClientRemAlarmedEntries_Type()
)
tnMcsClientRemAlarmedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcsClientRemAlarmedEntries.setStatus("current")
_TnMcDomainTable_Object = MibTable
tnMcDomainTable = _TnMcDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91)
)
if mibBuilder.loadTexts:
    tnMcDomainTable.setStatus("current")
_TnMcDomainEntry_Object = MibTableRow
tnMcDomainEntry = _TnMcDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1)
)
tnMcDomainEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcDomainId"),
)
if mibBuilder.loadTexts:
    tnMcDomainEntry.setStatus("current")


class _TnMcDomainId_Type(Integer32):
    """Custom type tnMcDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 250),
    )


_TnMcDomainId_Type.__name__ = "Integer32"
_TnMcDomainId_Object = MibTableColumn
tnMcDomainId = _TnMcDomainId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 1),
    _TnMcDomainId_Type()
)
tnMcDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMcDomainId.setStatus("current")
_TnMcDomainRowStatus_Type = RowStatus
_TnMcDomainRowStatus_Object = MibTableColumn
tnMcDomainRowStatus = _TnMcDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 2),
    _TnMcDomainRowStatus_Type()
)
tnMcDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcDomainRowStatus.setStatus("current")


class _TnMcDomainDescription_Type(TItemDescription):
    """Custom type tnMcDomainDescription based on TItemDescription"""
    defaultHexValue = ""


_TnMcDomainDescription_Type.__name__ = "TItemDescription"
_TnMcDomainDescription_Object = MibTableColumn
tnMcDomainDescription = _TnMcDomainDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 3),
    _TnMcDomainDescription_Type()
)
tnMcDomainDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcDomainDescription.setStatus("current")


class _TnMcDomainSrcIpType_Type(InetAddressType):
    """Custom type tnMcDomainSrcIpType based on InetAddressType"""
    defaultValue = 0


_TnMcDomainSrcIpType_Type.__name__ = "InetAddressType"
_TnMcDomainSrcIpType_Object = MibTableColumn
tnMcDomainSrcIpType = _TnMcDomainSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 4),
    _TnMcDomainSrcIpType_Type()
)
tnMcDomainSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcDomainSrcIpType.setStatus("current")


class _TnMcDomainSrcIpAddr_Type(InetAddress):
    """Custom type tnMcDomainSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TnMcDomainSrcIpAddr_Type.__name__ = "InetAddress"
_TnMcDomainSrcIpAddr_Object = MibTableColumn
tnMcDomainSrcIpAddr = _TnMcDomainSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 5),
    _TnMcDomainSrcIpAddr_Type()
)
tnMcDomainSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcDomainSrcIpAddr.setStatus("current")


class _TnMcDomainSrcIpMask_Type(InetAddressPrefixLength):
    """Custom type tnMcDomainSrcIpMask based on InetAddressPrefixLength"""
    defaultValue = 24


_TnMcDomainSrcIpMask_Type.__name__ = "InetAddressPrefixLength"
_TnMcDomainSrcIpMask_Object = MibTableColumn
tnMcDomainSrcIpMask = _TnMcDomainSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 6),
    _TnMcDomainSrcIpMask_Type()
)
tnMcDomainSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcDomainSrcIpMask.setStatus("current")


class _TnMcDomainSvcName_Type(TNamedItemOrEmpty):
    """Custom type tnMcDomainSvcName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TnMcDomainSvcName_Type.__name__ = "TNamedItemOrEmpty"
_TnMcDomainSvcName_Object = MibTableColumn
tnMcDomainSvcName = _TnMcDomainSvcName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 1, 91, 1, 7),
    _TnMcDomainSvcName_Type()
)
tnMcDomainSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMcDomainSvcName.setStatus("current")
_TnMcRedundancyStatsObjs_ObjectIdentity = ObjectIdentity
tnMcRedundancyStatsObjs = _TnMcRedundancyStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2)
)
_TnMcLagGlobalStatsTable_Object = MibTable
tnMcLagGlobalStatsTable = _TnMcLagGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20)
)
if mibBuilder.loadTexts:
    tnMcLagGlobalStatsTable.setStatus("current")
_TnMcLagGlobalStatsEntry_Object = MibTableRow
tnMcLagGlobalStatsEntry = _TnMcLagGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1)
)
tnMcLagGlobalStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnMcLagGlobalStatsEntry.setStatus("current")
_TnMcLagStatsPktsRx_Type = Counter32
_TnMcLagStatsPktsRx_Object = MibTableColumn
tnMcLagStatsPktsRx = _TnMcLagStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 1),
    _TnMcLagStatsPktsRx_Type()
)
tnMcLagStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsRx.setStatus("current")
_TnMcLagStatsPktsRxKeepalive_Type = Counter32
_TnMcLagStatsPktsRxKeepalive_Object = MibTableColumn
tnMcLagStatsPktsRxKeepalive = _TnMcLagStatsPktsRxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 2),
    _TnMcLagStatsPktsRxKeepalive_Type()
)
tnMcLagStatsPktsRxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsRxKeepalive.setStatus("current")
_TnMcLagStatsPktsRxConfig_Type = Counter32
_TnMcLagStatsPktsRxConfig_Object = MibTableColumn
tnMcLagStatsPktsRxConfig = _TnMcLagStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 3),
    _TnMcLagStatsPktsRxConfig_Type()
)
tnMcLagStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsRxConfig.setStatus("current")
_TnMcLagStatsPktsRxPeerConfig_Type = Counter32
_TnMcLagStatsPktsRxPeerConfig_Object = MibTableColumn
tnMcLagStatsPktsRxPeerConfig = _TnMcLagStatsPktsRxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 4),
    _TnMcLagStatsPktsRxPeerConfig_Type()
)
tnMcLagStatsPktsRxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsRxPeerConfig.setStatus("current")
_TnMcLagStatsPktsRxState_Type = Counter32
_TnMcLagStatsPktsRxState_Object = MibTableColumn
tnMcLagStatsPktsRxState = _TnMcLagStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 5),
    _TnMcLagStatsPktsRxState_Type()
)
tnMcLagStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsRxState.setStatus("current")
_TnMcLagStatsDropPktKpaliveTask_Type = Counter32
_TnMcLagStatsDropPktKpaliveTask_Object = MibTableColumn
tnMcLagStatsDropPktKpaliveTask = _TnMcLagStatsDropPktKpaliveTask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 6),
    _TnMcLagStatsDropPktKpaliveTask_Type()
)
tnMcLagStatsDropPktKpaliveTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropPktKpaliveTask.setStatus("current")
_TnMcLagStatsDropPktTooShort_Type = Counter32
_TnMcLagStatsDropPktTooShort_Object = MibTableColumn
tnMcLagStatsDropPktTooShort = _TnMcLagStatsDropPktTooShort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 7),
    _TnMcLagStatsDropPktTooShort_Type()
)
tnMcLagStatsDropPktTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropPktTooShort.setStatus("current")
_TnMcLagStatsDropPktVerifyFaild_Type = Counter32
_TnMcLagStatsDropPktVerifyFaild_Object = MibTableColumn
tnMcLagStatsDropPktVerifyFaild = _TnMcLagStatsDropPktVerifyFaild_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 8),
    _TnMcLagStatsDropPktVerifyFaild_Type()
)
tnMcLagStatsDropPktVerifyFaild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropPktVerifyFaild.setStatus("current")
_TnMcLagStatsDropTlvInvalidSize_Type = Counter32
_TnMcLagStatsDropTlvInvalidSize_Object = MibTableColumn
tnMcLagStatsDropTlvInvalidSize = _TnMcLagStatsDropTlvInvalidSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 9),
    _TnMcLagStatsDropTlvInvalidSize_Type()
)
tnMcLagStatsDropTlvInvalidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropTlvInvalidSize.setStatus("current")
_TnMcLagStatsDropOutOfSeq_Type = Counter32
_TnMcLagStatsDropOutOfSeq_Object = MibTableColumn
tnMcLagStatsDropOutOfSeq = _TnMcLagStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 10),
    _TnMcLagStatsDropOutOfSeq_Type()
)
tnMcLagStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropOutOfSeq.setStatus("current")
_TnMcLagStatsDropUnknownTlv_Type = Counter32
_TnMcLagStatsDropUnknownTlv_Object = MibTableColumn
tnMcLagStatsDropUnknownTlv = _TnMcLagStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 11),
    _TnMcLagStatsDropUnknownTlv_Type()
)
tnMcLagStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropUnknownTlv.setStatus("current")
_TnMcLagStatsDropTlvInvldLagId_Type = Counter32
_TnMcLagStatsDropTlvInvldLagId_Object = MibTableColumn
tnMcLagStatsDropTlvInvldLagId = _TnMcLagStatsDropTlvInvldLagId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 12),
    _TnMcLagStatsDropTlvInvldLagId_Type()
)
tnMcLagStatsDropTlvInvldLagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropTlvInvldLagId.setStatus("current")
_TnMcLagStatsDropMD5_Type = Counter32
_TnMcLagStatsDropMD5_Object = MibTableColumn
tnMcLagStatsDropMD5 = _TnMcLagStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 13),
    _TnMcLagStatsDropMD5_Type()
)
tnMcLagStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropMD5.setStatus("current")
_TnMcLagStatsDropUnknownPeer_Type = Counter32
_TnMcLagStatsDropUnknownPeer_Object = MibTableColumn
tnMcLagStatsDropUnknownPeer = _TnMcLagStatsDropUnknownPeer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 14),
    _TnMcLagStatsDropUnknownPeer_Type()
)
tnMcLagStatsDropUnknownPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsDropUnknownPeer.setStatus("current")
_TnMcLagStatsPktsTx_Type = Counter32
_TnMcLagStatsPktsTx_Object = MibTableColumn
tnMcLagStatsPktsTx = _TnMcLagStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 15),
    _TnMcLagStatsPktsTx_Type()
)
tnMcLagStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsTx.setStatus("current")
_TnMcLagStatsPktsTxKeepalive_Type = Counter32
_TnMcLagStatsPktsTxKeepalive_Object = MibTableColumn
tnMcLagStatsPktsTxKeepalive = _TnMcLagStatsPktsTxKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 16),
    _TnMcLagStatsPktsTxKeepalive_Type()
)
tnMcLagStatsPktsTxKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsTxKeepalive.setStatus("current")
_TnMcLagStatsPktsTxConfig_Type = Counter32
_TnMcLagStatsPktsTxConfig_Object = MibTableColumn
tnMcLagStatsPktsTxConfig = _TnMcLagStatsPktsTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 17),
    _TnMcLagStatsPktsTxConfig_Type()
)
tnMcLagStatsPktsTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsTxConfig.setStatus("current")
_TnMcLagStatsPktsTxPeerConfig_Type = Counter32
_TnMcLagStatsPktsTxPeerConfig_Object = MibTableColumn
tnMcLagStatsPktsTxPeerConfig = _TnMcLagStatsPktsTxPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 18),
    _TnMcLagStatsPktsTxPeerConfig_Type()
)
tnMcLagStatsPktsTxPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsTxPeerConfig.setStatus("current")
_TnMcLagStatsPktsTxState_Type = Counter32
_TnMcLagStatsPktsTxState_Object = MibTableColumn
tnMcLagStatsPktsTxState = _TnMcLagStatsPktsTxState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 19),
    _TnMcLagStatsPktsTxState_Type()
)
tnMcLagStatsPktsTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsTxState.setStatus("current")
_TnMcLagStatsPktsTxFailed_Type = Counter32
_TnMcLagStatsPktsTxFailed_Object = MibTableColumn
tnMcLagStatsPktsTxFailed = _TnMcLagStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 20, 1, 20),
    _TnMcLagStatsPktsTxFailed_Type()
)
tnMcLagStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagStatsPktsTxFailed.setStatus("current")
_TnMcLagPeerStatsTable_Object = MibTable
tnMcLagPeerStatsTable = _TnMcLagPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21)
)
if mibBuilder.loadTexts:
    tnMcLagPeerStatsTable.setStatus("current")
_TnMcLagPeerStatsEntry_Object = MibTableRow
tnMcLagPeerStatsEntry = _TnMcLagPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1)
)
tnMcLagPeerStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tnMcLagPeerStatsEntry.setStatus("current")
_TnMcLagPeerStatsPktsRx_Type = Counter32
_TnMcLagPeerStatsPktsRx_Object = MibTableColumn
tnMcLagPeerStatsPktsRx = _TnMcLagPeerStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 1),
    _TnMcLagPeerStatsPktsRx_Type()
)
tnMcLagPeerStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsRx.setStatus("current")
_TnMcLagPeerStatsPktsRxKpalive_Type = Counter32
_TnMcLagPeerStatsPktsRxKpalive_Object = MibTableColumn
tnMcLagPeerStatsPktsRxKpalive = _TnMcLagPeerStatsPktsRxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 2),
    _TnMcLagPeerStatsPktsRxKpalive_Type()
)
tnMcLagPeerStatsPktsRxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsRxKpalive.setStatus("current")
_TnMcLagPeerStatsPktsRxConfig_Type = Counter32
_TnMcLagPeerStatsPktsRxConfig_Object = MibTableColumn
tnMcLagPeerStatsPktsRxConfig = _TnMcLagPeerStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 3),
    _TnMcLagPeerStatsPktsRxConfig_Type()
)
tnMcLagPeerStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsRxConfig.setStatus("current")
_TnMcLagPeerStatsPktsRxPeerCfg_Type = Counter32
_TnMcLagPeerStatsPktsRxPeerCfg_Object = MibTableColumn
tnMcLagPeerStatsPktsRxPeerCfg = _TnMcLagPeerStatsPktsRxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 4),
    _TnMcLagPeerStatsPktsRxPeerCfg_Type()
)
tnMcLagPeerStatsPktsRxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsRxPeerCfg.setStatus("current")
_TnMcLagPeerStatsPktsRxState_Type = Counter32
_TnMcLagPeerStatsPktsRxState_Object = MibTableColumn
tnMcLagPeerStatsPktsRxState = _TnMcLagPeerStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 5),
    _TnMcLagPeerStatsPktsRxState_Type()
)
tnMcLagPeerStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsRxState.setStatus("current")
_TnMcLagPeerStatsDropStateDsbld_Type = Counter32
_TnMcLagPeerStatsDropStateDsbld_Object = MibTableColumn
tnMcLagPeerStatsDropStateDsbld = _TnMcLagPeerStatsDropStateDsbld_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 6),
    _TnMcLagPeerStatsDropStateDsbld_Type()
)
tnMcLagPeerStatsDropStateDsbld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropStateDsbld.setStatus("current")
_TnMcLagPeerStatsDropPktTooShrt_Type = Counter32
_TnMcLagPeerStatsDropPktTooShrt_Object = MibTableColumn
tnMcLagPeerStatsDropPktTooShrt = _TnMcLagPeerStatsDropPktTooShrt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 7),
    _TnMcLagPeerStatsDropPktTooShrt_Type()
)
tnMcLagPeerStatsDropPktTooShrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropPktTooShrt.setStatus("current")
_TnMcLagPeerStatsDropTlvInvldSz_Type = Counter32
_TnMcLagPeerStatsDropTlvInvldSz_Object = MibTableColumn
tnMcLagPeerStatsDropTlvInvldSz = _TnMcLagPeerStatsDropTlvInvldSz_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 8),
    _TnMcLagPeerStatsDropTlvInvldSz_Type()
)
tnMcLagPeerStatsDropTlvInvldSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropTlvInvldSz.setStatus("current")
_TnMcLagPeerStatsDropTlvInvldId_Type = Counter32
_TnMcLagPeerStatsDropTlvInvldId_Object = MibTableColumn
tnMcLagPeerStatsDropTlvInvldId = _TnMcLagPeerStatsDropTlvInvldId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 9),
    _TnMcLagPeerStatsDropTlvInvldId_Type()
)
tnMcLagPeerStatsDropTlvInvldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropTlvInvldId.setStatus("current")
_TnMcLagPeerStatsDropOutOfSeq_Type = Counter32
_TnMcLagPeerStatsDropOutOfSeq_Object = MibTableColumn
tnMcLagPeerStatsDropOutOfSeq = _TnMcLagPeerStatsDropOutOfSeq_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 10),
    _TnMcLagPeerStatsDropOutOfSeq_Type()
)
tnMcLagPeerStatsDropOutOfSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropOutOfSeq.setStatus("current")
_TnMcLagPeerStatsDropUnknownTlv_Type = Counter32
_TnMcLagPeerStatsDropUnknownTlv_Object = MibTableColumn
tnMcLagPeerStatsDropUnknownTlv = _TnMcLagPeerStatsDropUnknownTlv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 11),
    _TnMcLagPeerStatsDropUnknownTlv_Type()
)
tnMcLagPeerStatsDropUnknownTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropUnknownTlv.setStatus("current")
_TnMcLagPeerStatsDropMD5_Type = Counter32
_TnMcLagPeerStatsDropMD5_Object = MibTableColumn
tnMcLagPeerStatsDropMD5 = _TnMcLagPeerStatsDropMD5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 12),
    _TnMcLagPeerStatsDropMD5_Type()
)
tnMcLagPeerStatsDropMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsDropMD5.setStatus("current")
_TnMcLagPeerStatsPktsTx_Type = Counter32
_TnMcLagPeerStatsPktsTx_Object = MibTableColumn
tnMcLagPeerStatsPktsTx = _TnMcLagPeerStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 13),
    _TnMcLagPeerStatsPktsTx_Type()
)
tnMcLagPeerStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsTx.setStatus("current")
_TnMcLagPeerStatsPktsTxKpalive_Type = Counter32
_TnMcLagPeerStatsPktsTxKpalive_Object = MibTableColumn
tnMcLagPeerStatsPktsTxKpalive = _TnMcLagPeerStatsPktsTxKpalive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 14),
    _TnMcLagPeerStatsPktsTxKpalive_Type()
)
tnMcLagPeerStatsPktsTxKpalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsTxKpalive.setStatus("current")
_TnMcLagPeerStatsPktsTxPeerCfg_Type = Counter32
_TnMcLagPeerStatsPktsTxPeerCfg_Object = MibTableColumn
tnMcLagPeerStatsPktsTxPeerCfg = _TnMcLagPeerStatsPktsTxPeerCfg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 15),
    _TnMcLagPeerStatsPktsTxPeerCfg_Type()
)
tnMcLagPeerStatsPktsTxPeerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsTxPeerCfg.setStatus("current")
_TnMcLagPeerStatsPktsTxFailed_Type = Counter32
_TnMcLagPeerStatsPktsTxFailed_Object = MibTableColumn
tnMcLagPeerStatsPktsTxFailed = _TnMcLagPeerStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 21, 1, 16),
    _TnMcLagPeerStatsPktsTxFailed_Type()
)
tnMcLagPeerStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagPeerStatsPktsTxFailed.setStatus("current")
_TnMcLagLagStatsTable_Object = MibTable
tnMcLagLagStatsTable = _TnMcLagLagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22)
)
if mibBuilder.loadTexts:
    tnMcLagLagStatsTable.setStatus("current")
_TnMcLagLagStatsEntry_Object = MibTableRow
tnMcLagLagStatsEntry = _TnMcLagLagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22, 1)
)
tnMcLagLagStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcLagConfigLagId"),
)
if mibBuilder.loadTexts:
    tnMcLagLagStatsEntry.setStatus("current")
_TnMcLagLagStatsPktsRxConfig_Type = Counter32
_TnMcLagLagStatsPktsRxConfig_Object = MibTableColumn
tnMcLagLagStatsPktsRxConfig = _TnMcLagLagStatsPktsRxConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22, 1, 1),
    _TnMcLagLagStatsPktsRxConfig_Type()
)
tnMcLagLagStatsPktsRxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagLagStatsPktsRxConfig.setStatus("current")
_TnMcLagLagStatsPktsRxState_Type = Counter32
_TnMcLagLagStatsPktsRxState_Object = MibTableColumn
tnMcLagLagStatsPktsRxState = _TnMcLagLagStatsPktsRxState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22, 1, 2),
    _TnMcLagLagStatsPktsRxState_Type()
)
tnMcLagLagStatsPktsRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagLagStatsPktsRxState.setStatus("current")
_TnMcLagLagStatsPktsTxConfig_Type = Counter32
_TnMcLagLagStatsPktsTxConfig_Object = MibTableColumn
tnMcLagLagStatsPktsTxConfig = _TnMcLagLagStatsPktsTxConfig_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22, 1, 3),
    _TnMcLagLagStatsPktsTxConfig_Type()
)
tnMcLagLagStatsPktsTxConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagLagStatsPktsTxConfig.setStatus("current")
_TnMcLagLagStatsPktsTxState_Type = Counter32
_TnMcLagLagStatsPktsTxState_Object = MibTableColumn
tnMcLagLagStatsPktsTxState = _TnMcLagLagStatsPktsTxState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22, 1, 4),
    _TnMcLagLagStatsPktsTxState_Type()
)
tnMcLagLagStatsPktsTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagLagStatsPktsTxState.setStatus("current")
_TnMcLagLagStatsPktsTxFailed_Type = Counter32
_TnMcLagLagStatsPktsTxFailed_Object = MibTableColumn
tnMcLagLagStatsPktsTxFailed = _TnMcLagLagStatsPktsTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 22, 1, 5),
    _TnMcLagLagStatsPktsTxFailed_Type()
)
tnMcLagLagStatsPktsTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcLagLagStatsPktsTxFailed.setStatus("current")
_TnMcPeerSyncStatsTable_Object = MibTable
tnMcPeerSyncStatsTable = _TnMcPeerSyncStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23)
)
if mibBuilder.loadTexts:
    tnMcPeerSyncStatsTable.setStatus("current")
_TnMcPeerSyncStatsEntry_Object = MibTableRow
tnMcPeerSyncStatsEntry = _TnMcPeerSyncStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1)
)
tnMcPeerSyncStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpType"),
    (0, "TN-MC-REDUNDANCY-MIB", "tnMcPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tnMcPeerSyncStatsEntry.setStatus("current")
_TnMcPeerSyncPktsTxAll_Type = Counter32
_TnMcPeerSyncPktsTxAll_Object = MibTableColumn
tnMcPeerSyncPktsTxAll = _TnMcPeerSyncPktsTxAll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 1),
    _TnMcPeerSyncPktsTxAll_Type()
)
tnMcPeerSyncPktsTxAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsTxAll.setStatus("current")
_TnMcPeerSyncPktsTxHello_Type = Counter32
_TnMcPeerSyncPktsTxHello_Object = MibTableColumn
tnMcPeerSyncPktsTxHello = _TnMcPeerSyncPktsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 2),
    _TnMcPeerSyncPktsTxHello_Type()
)
tnMcPeerSyncPktsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsTxHello.setStatus("current")
_TnMcPeerSyncPktsTxData_Type = Counter32
_TnMcPeerSyncPktsTxData_Object = MibTableColumn
tnMcPeerSyncPktsTxData = _TnMcPeerSyncPktsTxData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 3),
    _TnMcPeerSyncPktsTxData_Type()
)
tnMcPeerSyncPktsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsTxData.setStatus("current")
_TnMcPeerSyncPktsTxOther_Type = Counter32
_TnMcPeerSyncPktsTxOther_Object = MibTableColumn
tnMcPeerSyncPktsTxOther = _TnMcPeerSyncPktsTxOther_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 4),
    _TnMcPeerSyncPktsTxOther_Type()
)
tnMcPeerSyncPktsTxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsTxOther.setStatus("current")
_TnMcPeerSyncPktsTxErr_Type = Counter32
_TnMcPeerSyncPktsTxErr_Object = MibTableColumn
tnMcPeerSyncPktsTxErr = _TnMcPeerSyncPktsTxErr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 5),
    _TnMcPeerSyncPktsTxErr_Type()
)
tnMcPeerSyncPktsTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsTxErr.setStatus("current")
_TnMcPeerSyncPktsRxAll_Type = Counter32
_TnMcPeerSyncPktsRxAll_Object = MibTableColumn
tnMcPeerSyncPktsRxAll = _TnMcPeerSyncPktsRxAll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 6),
    _TnMcPeerSyncPktsRxAll_Type()
)
tnMcPeerSyncPktsRxAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxAll.setStatus("current")
_TnMcPeerSyncPktsRxHello_Type = Counter32
_TnMcPeerSyncPktsRxHello_Object = MibTableColumn
tnMcPeerSyncPktsRxHello = _TnMcPeerSyncPktsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 7),
    _TnMcPeerSyncPktsRxHello_Type()
)
tnMcPeerSyncPktsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxHello.setStatus("current")
_TnMcPeerSyncPktsRxData_Type = Counter32
_TnMcPeerSyncPktsRxData_Object = MibTableColumn
tnMcPeerSyncPktsRxData = _TnMcPeerSyncPktsRxData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 8),
    _TnMcPeerSyncPktsRxData_Type()
)
tnMcPeerSyncPktsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxData.setStatus("current")
_TnMcPeerSyncPktsRxOther_Type = Counter32
_TnMcPeerSyncPktsRxOther_Object = MibTableColumn
tnMcPeerSyncPktsRxOther = _TnMcPeerSyncPktsRxOther_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 9),
    _TnMcPeerSyncPktsRxOther_Type()
)
tnMcPeerSyncPktsRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxOther.setStatus("current")
_TnMcPeerSyncPktsRxErr_Type = Counter32
_TnMcPeerSyncPktsRxErr_Object = MibTableColumn
tnMcPeerSyncPktsRxErr = _TnMcPeerSyncPktsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 10),
    _TnMcPeerSyncPktsRxErr_Type()
)
tnMcPeerSyncPktsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxErr.setStatus("current")
_TnMcPeerSyncPktsRxErrHeader_Type = Counter32
_TnMcPeerSyncPktsRxErrHeader_Object = MibTableColumn
tnMcPeerSyncPktsRxErrHeader = _TnMcPeerSyncPktsRxErrHeader_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 11),
    _TnMcPeerSyncPktsRxErrHeader_Type()
)
tnMcPeerSyncPktsRxErrHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxErrHeader.setStatus("current")
_TnMcPeerSyncPktsRxErrBody_Type = Counter32
_TnMcPeerSyncPktsRxErrBody_Object = MibTableColumn
tnMcPeerSyncPktsRxErrBody = _TnMcPeerSyncPktsRxErrBody_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 12),
    _TnMcPeerSyncPktsRxErrBody_Type()
)
tnMcPeerSyncPktsRxErrBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxErrBody.setStatus("current")
_TnMcPeerSyncPktsRxErrSeqNum_Type = Counter32
_TnMcPeerSyncPktsRxErrSeqNum_Object = MibTableColumn
tnMcPeerSyncPktsRxErrSeqNum = _TnMcPeerSyncPktsRxErrSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 23, 1, 13),
    _TnMcPeerSyncPktsRxErrSeqNum_Type()
)
tnMcPeerSyncPktsRxErrSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcPeerSyncPktsRxErrSeqNum.setStatus("current")
_TnMcRedundancyStatsScalar1_Type = Unsigned32
_TnMcRedundancyStatsScalar1_Object = MibScalar
tnMcRedundancyStatsScalar1 = _TnMcRedundancyStatsScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 101),
    _TnMcRedundancyStatsScalar1_Type()
)
tnMcRedundancyStatsScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcRedundancyStatsScalar1.setStatus("current")
_TnMcRedundancyStatsScalar2_Type = Unsigned32
_TnMcRedundancyStatsScalar2_Object = MibScalar
tnMcRedundancyStatsScalar2 = _TnMcRedundancyStatsScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 40, 2, 102),
    _TnMcRedundancyStatsScalar2_Type()
)
tnMcRedundancyStatsScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMcRedundancyStatsScalar2.setStatus("current")
tnMcLagConfigLagEntry.registerAugmentions(
    ("TN-MC-REDUNDANCY-MIB",
     "tnMcLagInfoLagEntry")
)
tnMcLagInfoLagEntry.setIndexNames(*tnMcLagConfigLagEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MC-REDUNDANCY-MIB",
    **{"TmnxMcsClientApp": TmnxMcsClientApp,
       "TmnxMcRingOperState": TmnxMcRingOperState,
       "TmnxMcRingInbCtrlOperState": TmnxMcRingInbCtrlOperState,
       "TmnxMcRingNodeOperState": TmnxMcRingNodeOperState,
       "TmnxSrrpAssoBfdIntfSessOperState": TmnxSrrpAssoBfdIntfSessOperState,
       "TmnxMcRingType": TmnxMcRingType,
       "tnMcRedundancyMIBModule": tnMcRedundancyMIBModule,
       "tnMcRedundancy": tnMcRedundancy,
       "tnMcRedundancyObjs": tnMcRedundancyObjs,
       "tnMcPeerTable": tnMcPeerTable,
       "tnMcPeerEntry": tnMcPeerEntry,
       "tnMcPeerIpType": tnMcPeerIpType,
       "tnMcPeerIpAddr": tnMcPeerIpAddr,
       "tnMcPeerRowStatus": tnMcPeerRowStatus,
       "tnMcPeerDescription": tnMcPeerDescription,
       "tnMcPeerAuthKey": tnMcPeerAuthKey,
       "tnMcPeerSrcIpType": tnMcPeerSrcIpType,
       "tnMcPeerSrcIpAddr": tnMcPeerSrcIpAddr,
       "tnMcPeerAdminState": tnMcPeerAdminState,
       "tnMcPeerSrcIpOperType": tnMcPeerSrcIpOperType,
       "tnMcPeerSrcIpOperAddr": tnMcPeerSrcIpOperAddr,
       "tnMcPeerRingsOperState": tnMcPeerRingsOperState,
       "tnMcPeerName": tnMcPeerName,
       "tnMcPeerSyncTable": tnMcPeerSyncTable,
       "tnMcPeerSyncEntry": tnMcPeerSyncEntry,
       "tnMcPeerSyncRowStatus": tnMcPeerSyncRowStatus,
       "tnMcPeerSyncIgmp": tnMcPeerSyncIgmp,
       "tnMcPeerSyncIgmpSnooping": tnMcPeerSyncIgmpSnooping,
       "tnMcPeerSyncSubMgmt": tnMcPeerSyncSubMgmt,
       "tnMcPeerSyncSrrp": tnMcPeerSyncSrrp,
       "tnMcPeerSyncAdminState": tnMcPeerSyncAdminState,
       "tnMcPeerSyncOperState": tnMcPeerSyncOperState,
       "tnMcPeerSyncOperFlags": tnMcPeerSyncOperFlags,
       "tnMcPeerSyncStatus": tnMcPeerSyncStatus,
       "tnMcPeerSyncLastSyncTime": tnMcPeerSyncLastSyncTime,
       "tnMcPeerSyncNumEntries": tnMcPeerSyncNumEntries,
       "tnMcPeerSyncLclDeletedEntries": tnMcPeerSyncLclDeletedEntries,
       "tnMcPeerSyncAlarmedEntries": tnMcPeerSyncAlarmedEntries,
       "tnMcPeerSyncRemNumEntries": tnMcPeerSyncRemNumEntries,
       "tnMcPeerSyncRemLclDelEntries": tnMcPeerSyncRemLclDelEntries,
       "tnMcPeerSyncRemAlarmedEntries": tnMcPeerSyncRemAlarmedEntries,
       "tnMcPeerSyncPortTable": tnMcPeerSyncPortTable,
       "tnMcPeerSyncPortEntry": tnMcPeerSyncPortEntry,
       "tnMcPeerSyncPortId": tnMcPeerSyncPortId,
       "tnMcPeerSyncPortRowStatus": tnMcPeerSyncPortRowStatus,
       "tnMcPeerSyncPortSyncTag": tnMcPeerSyncPortSyncTag,
       "tnMcPeerSyncPortEncapRangeTable": tnMcPeerSyncPortEncapRangeTable,
       "tnMcPeerSyncPortEncapRangeEntry": tnMcPeerSyncPortEncapRangeEntry,
       "tnMcPeerSyncPortEncapType": tnMcPeerSyncPortEncapType,
       "tnMcPeerSyncPortEncapMin": tnMcPeerSyncPortEncapMin,
       "tnMcPeerSyncPortEncapMax": tnMcPeerSyncPortEncapMax,
       "tnMcPeerSyncPortEncapRowStatus": tnMcPeerSyncPortEncapRowStatus,
       "tnMcPeerSyncPortEncapSyncTag": tnMcPeerSyncPortEncapSyncTag,
       "tnMcLagConfigTableLastChanged": tnMcLagConfigTableLastChanged,
       "tnMcLagConfigTable": tnMcLagConfigTable,
       "tnMcLagConfigEntry": tnMcLagConfigEntry,
       "tnMcLagConfigPeerLastChanged": tnMcLagConfigPeerLastChanged,
       "tnMcLagConfigPeerAdminstate": tnMcLagConfigPeerAdminstate,
       "tnMcLagConfigKeepALiveIvl": tnMcLagConfigKeepALiveIvl,
       "tnMcLagConfigHoldOnNgbrFailure": tnMcLagConfigHoldOnNgbrFailure,
       "tnMcLagConfigOperState": tnMcLagConfigOperState,
       "tnMcLagConfigPeerLastStateChge": tnMcLagConfigPeerLastStateChge,
       "tnMcLagConfigLagTableLastChanged": tnMcLagConfigLagTableLastChanged,
       "tnMcLagConfigLagTable": tnMcLagConfigLagTable,
       "tnMcLagConfigLagEntry": tnMcLagConfigLagEntry,
       "tnMcLagConfigLagId": tnMcLagConfigLagId,
       "tnMcLagConfigLagLastChanged": tnMcLagConfigLagLastChanged,
       "tnMcLagConfigLagRowStatus": tnMcLagConfigLagRowStatus,
       "tnMcLagConfigLaglacpKey": tnMcLagConfigLaglacpKey,
       "tnMcLagConfigLagSystemId": tnMcLagConfigLagSystemId,
       "tnMcLagConfigLagSystemPriority": tnMcLagConfigLagSystemPriority,
       "tnMcLagConfigLagRemoteLagId": tnMcLagConfigLagRemoteLagId,
       "tnMcLagConfigLagSrcBMacLSB": tnMcLagConfigLagSrcBMacLSB,
       "tnMcLagConfigLagOperSrcBMacLSB": tnMcLagConfigLagOperSrcBMacLSB,
       "tnMcLagConfigLagFlushEthRingOnActive": tnMcLagConfigLagFlushEthRingOnActive,
       "tnMcLagInfoLagTable": tnMcLagInfoLagTable,
       "tnMcLagInfoLagEntry": tnMcLagInfoLagEntry,
       "tnMcLagActiveStandby": tnMcLagActiveStandby,
       "tnMcLagLacpIdInUse": tnMcLagLacpIdInUse,
       "tnMcLagExtendedTimeOut": tnMcLagExtendedTimeOut,
       "tnMcLagSelectionLogic": tnMcLagSelectionLogic,
       "tnMcLagConfigMismatchString": tnMcLagConfigMismatchString,
       "tnMcLagConfigMismatchFlags": tnMcLagConfigMismatchFlags,
       "tnMcsClientAppTable": tnMcsClientAppTable,
       "tnMcsClientAppEntry": tnMcsClientAppEntry,
       "tnMcsClientApplication": tnMcsClientApplication,
       "tnMcsClientNumEntries": tnMcsClientNumEntries,
       "tnMcsClientLclDeletedEntries": tnMcsClientLclDeletedEntries,
       "tnMcsClientAlarmedEntries": tnMcsClientAlarmedEntries,
       "tnMcsClientRemNumEntries": tnMcsClientRemNumEntries,
       "tnMcsClientRemLclDelEntries": tnMcsClientRemLclDelEntries,
       "tnMcsClientRemAlarmedEntries": tnMcsClientRemAlarmedEntries,
       "tnMcDomainTable": tnMcDomainTable,
       "tnMcDomainEntry": tnMcDomainEntry,
       "tnMcDomainId": tnMcDomainId,
       "tnMcDomainRowStatus": tnMcDomainRowStatus,
       "tnMcDomainDescription": tnMcDomainDescription,
       "tnMcDomainSrcIpType": tnMcDomainSrcIpType,
       "tnMcDomainSrcIpAddr": tnMcDomainSrcIpAddr,
       "tnMcDomainSrcIpMask": tnMcDomainSrcIpMask,
       "tnMcDomainSvcName": tnMcDomainSvcName,
       "tnMcRedundancyStatsObjs": tnMcRedundancyStatsObjs,
       "tnMcLagGlobalStatsTable": tnMcLagGlobalStatsTable,
       "tnMcLagGlobalStatsEntry": tnMcLagGlobalStatsEntry,
       "tnMcLagStatsPktsRx": tnMcLagStatsPktsRx,
       "tnMcLagStatsPktsRxKeepalive": tnMcLagStatsPktsRxKeepalive,
       "tnMcLagStatsPktsRxConfig": tnMcLagStatsPktsRxConfig,
       "tnMcLagStatsPktsRxPeerConfig": tnMcLagStatsPktsRxPeerConfig,
       "tnMcLagStatsPktsRxState": tnMcLagStatsPktsRxState,
       "tnMcLagStatsDropPktKpaliveTask": tnMcLagStatsDropPktKpaliveTask,
       "tnMcLagStatsDropPktTooShort": tnMcLagStatsDropPktTooShort,
       "tnMcLagStatsDropPktVerifyFaild": tnMcLagStatsDropPktVerifyFaild,
       "tnMcLagStatsDropTlvInvalidSize": tnMcLagStatsDropTlvInvalidSize,
       "tnMcLagStatsDropOutOfSeq": tnMcLagStatsDropOutOfSeq,
       "tnMcLagStatsDropUnknownTlv": tnMcLagStatsDropUnknownTlv,
       "tnMcLagStatsDropTlvInvldLagId": tnMcLagStatsDropTlvInvldLagId,
       "tnMcLagStatsDropMD5": tnMcLagStatsDropMD5,
       "tnMcLagStatsDropUnknownPeer": tnMcLagStatsDropUnknownPeer,
       "tnMcLagStatsPktsTx": tnMcLagStatsPktsTx,
       "tnMcLagStatsPktsTxKeepalive": tnMcLagStatsPktsTxKeepalive,
       "tnMcLagStatsPktsTxConfig": tnMcLagStatsPktsTxConfig,
       "tnMcLagStatsPktsTxPeerConfig": tnMcLagStatsPktsTxPeerConfig,
       "tnMcLagStatsPktsTxState": tnMcLagStatsPktsTxState,
       "tnMcLagStatsPktsTxFailed": tnMcLagStatsPktsTxFailed,
       "tnMcLagPeerStatsTable": tnMcLagPeerStatsTable,
       "tnMcLagPeerStatsEntry": tnMcLagPeerStatsEntry,
       "tnMcLagPeerStatsPktsRx": tnMcLagPeerStatsPktsRx,
       "tnMcLagPeerStatsPktsRxKpalive": tnMcLagPeerStatsPktsRxKpalive,
       "tnMcLagPeerStatsPktsRxConfig": tnMcLagPeerStatsPktsRxConfig,
       "tnMcLagPeerStatsPktsRxPeerCfg": tnMcLagPeerStatsPktsRxPeerCfg,
       "tnMcLagPeerStatsPktsRxState": tnMcLagPeerStatsPktsRxState,
       "tnMcLagPeerStatsDropStateDsbld": tnMcLagPeerStatsDropStateDsbld,
       "tnMcLagPeerStatsDropPktTooShrt": tnMcLagPeerStatsDropPktTooShrt,
       "tnMcLagPeerStatsDropTlvInvldSz": tnMcLagPeerStatsDropTlvInvldSz,
       "tnMcLagPeerStatsDropTlvInvldId": tnMcLagPeerStatsDropTlvInvldId,
       "tnMcLagPeerStatsDropOutOfSeq": tnMcLagPeerStatsDropOutOfSeq,
       "tnMcLagPeerStatsDropUnknownTlv": tnMcLagPeerStatsDropUnknownTlv,
       "tnMcLagPeerStatsDropMD5": tnMcLagPeerStatsDropMD5,
       "tnMcLagPeerStatsPktsTx": tnMcLagPeerStatsPktsTx,
       "tnMcLagPeerStatsPktsTxKpalive": tnMcLagPeerStatsPktsTxKpalive,
       "tnMcLagPeerStatsPktsTxPeerCfg": tnMcLagPeerStatsPktsTxPeerCfg,
       "tnMcLagPeerStatsPktsTxFailed": tnMcLagPeerStatsPktsTxFailed,
       "tnMcLagLagStatsTable": tnMcLagLagStatsTable,
       "tnMcLagLagStatsEntry": tnMcLagLagStatsEntry,
       "tnMcLagLagStatsPktsRxConfig": tnMcLagLagStatsPktsRxConfig,
       "tnMcLagLagStatsPktsRxState": tnMcLagLagStatsPktsRxState,
       "tnMcLagLagStatsPktsTxConfig": tnMcLagLagStatsPktsTxConfig,
       "tnMcLagLagStatsPktsTxState": tnMcLagLagStatsPktsTxState,
       "tnMcLagLagStatsPktsTxFailed": tnMcLagLagStatsPktsTxFailed,
       "tnMcPeerSyncStatsTable": tnMcPeerSyncStatsTable,
       "tnMcPeerSyncStatsEntry": tnMcPeerSyncStatsEntry,
       "tnMcPeerSyncPktsTxAll": tnMcPeerSyncPktsTxAll,
       "tnMcPeerSyncPktsTxHello": tnMcPeerSyncPktsTxHello,
       "tnMcPeerSyncPktsTxData": tnMcPeerSyncPktsTxData,
       "tnMcPeerSyncPktsTxOther": tnMcPeerSyncPktsTxOther,
       "tnMcPeerSyncPktsTxErr": tnMcPeerSyncPktsTxErr,
       "tnMcPeerSyncPktsRxAll": tnMcPeerSyncPktsRxAll,
       "tnMcPeerSyncPktsRxHello": tnMcPeerSyncPktsRxHello,
       "tnMcPeerSyncPktsRxData": tnMcPeerSyncPktsRxData,
       "tnMcPeerSyncPktsRxOther": tnMcPeerSyncPktsRxOther,
       "tnMcPeerSyncPktsRxErr": tnMcPeerSyncPktsRxErr,
       "tnMcPeerSyncPktsRxErrHeader": tnMcPeerSyncPktsRxErrHeader,
       "tnMcPeerSyncPktsRxErrBody": tnMcPeerSyncPktsRxErrBody,
       "tnMcPeerSyncPktsRxErrSeqNum": tnMcPeerSyncPktsRxErrSeqNum,
       "tnMcRedundancyStatsScalar1": tnMcRedundancyStatsScalar1,
       "tnMcRedundancyStatsScalar2": tnMcRedundancyStatsScalar2}
)
