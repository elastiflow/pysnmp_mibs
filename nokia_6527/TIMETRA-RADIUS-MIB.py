# SNMP MIB module (TIMETRA-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-RADIUS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
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

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxAuthPassword,
 TmnxDisplayStringURL,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxRadiusPendingReqLimit,
 TmnxRadiusServerOperState,
 TmnxSubRadServAlgorithm,
 TmnxSubRadiusAttrType,
 TmnxSubRadiusVendorId,
 TmnxVRtrID,
 TmnxVRtrIDOrZero,
 TmnxWlanGwIsaGrpIdOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxAuthPassword",
    "TmnxDisplayStringURL",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxRadiusPendingReqLimit",
    "TmnxRadiusServerOperState",
    "TmnxSubRadServAlgorithm",
    "TmnxSubRadiusAttrType",
    "TmnxSubRadiusVendorId",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero",
    "TmnxWlanGwIsaGrpIdOrZero")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraRadiusMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 79)
)
if mibBuilder.loadTexts:
    timetraRadiusMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-08-01 00:00",
         "2012-02-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxAuthSecret(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TmnxRadMatchString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class TmnxRadiusAcctStatusType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1),
          ("interimUpdate", 2),
          ("accountingOn", 3),
          ("accountingOff", 4))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxRadProxConformance_ObjectIdentity = ObjectIdentity
tmnxRadProxConformance = _TmnxRadProxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79)
)
_TmnxRadProxCompliances_ObjectIdentity = ObjectIdentity
tmnxRadProxCompliances = _TmnxRadProxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 1)
)
_TmnxRadProxGroups_ObjectIdentity = ObjectIdentity
tmnxRadProxGroups = _TmnxRadProxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2)
)
_TmnxRadius_ObjectIdentity = ObjectIdentity
tmnxRadius = _TmnxRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79)
)
_TmnxRadiusObjs_ObjectIdentity = ObjectIdentity
tmnxRadiusObjs = _TmnxRadiusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1)
)
_TmnxRadProxSrvObjs_ObjectIdentity = ObjectIdentity
tmnxRadProxSrvObjs = _TmnxRadProxSrvObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1)
)
_TmnxRadProxSrvTable_Object = MibTable
tmnxRadProxSrvTable = _TmnxRadProxSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvTable.setStatus("current")
_TmnxRadProxSrvEntry_Object = MibTableRow
tmnxRadProxSrvEntry = _TmnxRadProxSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1)
)
tmnxRadProxSrvEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvName"),
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvEntry.setStatus("current")
_TmnxRadProxSrvName_Type = TNamedItem
_TmnxRadProxSrvName_Object = MibTableColumn
tmnxRadProxSrvName = _TmnxRadProxSrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 1),
    _TmnxRadProxSrvName_Type()
)
tmnxRadProxSrvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadProxSrvName.setStatus("current")
_TmnxRadProxSrvLastCh_Type = TimeStamp
_TmnxRadProxSrvLastCh_Object = MibTableColumn
tmnxRadProxSrvLastCh = _TmnxRadProxSrvLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 2),
    _TmnxRadProxSrvLastCh_Type()
)
tmnxRadProxSrvLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLastCh.setStatus("current")
_TmnxRadProxSrvRowStatus_Type = RowStatus
_TmnxRadProxSrvRowStatus_Object = MibTableColumn
tmnxRadProxSrvRowStatus = _TmnxRadProxSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 3),
    _TmnxRadProxSrvRowStatus_Type()
)
tmnxRadProxSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvRowStatus.setStatus("current")


class _TmnxRadProxSrvPurpose_Type(Bits):
    """Custom type tmnxRadProxSrvPurpose based on Bits"""
    namedValues = NamedValues(
        *(("accounting", 0),
          ("authentication", 1))
    )

_TmnxRadProxSrvPurpose_Type.__name__ = "Bits"
_TmnxRadProxSrvPurpose_Object = MibTableColumn
tmnxRadProxSrvPurpose = _TmnxRadProxSrvPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 4),
    _TmnxRadProxSrvPurpose_Type()
)
tmnxRadProxSrvPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvPurpose.setStatus("current")


class _TmnxRadProxSrvAdminState_Type(TmnxAdminState):
    """Custom type tmnxRadProxSrvAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxRadProxSrvAdminState_Type.__name__ = "TmnxAdminState"
_TmnxRadProxSrvAdminState_Object = MibTableColumn
tmnxRadProxSrvAdminState = _TmnxRadProxSrvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 5),
    _TmnxRadProxSrvAdminState_Type()
)
tmnxRadProxSrvAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvAdminState.setStatus("current")


class _TmnxRadProxSrvDescription_Type(TItemDescription):
    """Custom type tmnxRadProxSrvDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadProxSrvDescription_Type.__name__ = "TItemDescription"
_TmnxRadProxSrvDescription_Object = MibTableColumn
tmnxRadProxSrvDescription = _TmnxRadProxSrvDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 6),
    _TmnxRadProxSrvDescription_Type()
)
tmnxRadProxSrvDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvDescription.setStatus("current")


class _TmnxRadProxSrvSecret_Type(TmnxAuthSecret):
    """Custom type tmnxRadProxSrvSecret based on TmnxAuthSecret"""
    defaultValue = OctetString("")


_TmnxRadProxSrvSecret_Type.__name__ = "TmnxAuthSecret"
_TmnxRadProxSrvSecret_Object = MibTableColumn
tmnxRadProxSrvSecret = _TmnxRadProxSrvSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 7),
    _TmnxRadProxSrvSecret_Type()
)
tmnxRadProxSrvSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvSecret.setStatus("current")


class _TmnxRadProxSrvDefAuthSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadProxSrvDefAuthSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadProxSrvDefAuthSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadProxSrvDefAuthSrvPlcy_Object = MibTableColumn
tmnxRadProxSrvDefAuthSrvPlcy = _TmnxRadProxSrvDefAuthSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 8),
    _TmnxRadProxSrvDefAuthSrvPlcy_Type()
)
tmnxRadProxSrvDefAuthSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvDefAuthSrvPlcy.setStatus("current")


class _TmnxRadProxSrvDefAccSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadProxSrvDefAccSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadProxSrvDefAccSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadProxSrvDefAccSrvPlcy_Object = MibTableColumn
tmnxRadProxSrvDefAccSrvPlcy = _TmnxRadProxSrvDefAccSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 9),
    _TmnxRadProxSrvDefAccSrvPlcy_Type()
)
tmnxRadProxSrvDefAccSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvDefAccSrvPlcy.setStatus("current")


class _TmnxRadProxSrvCaching_Type(TmnxEnabledDisabled):
    """Custom type tmnxRadProxSrvCaching based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxRadProxSrvCaching_Type.__name__ = "TmnxEnabledDisabled"
_TmnxRadProxSrvCaching_Object = MibTableColumn
tmnxRadProxSrvCaching = _TmnxRadProxSrvCaching_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 10),
    _TmnxRadProxSrvCaching_Type()
)
tmnxRadProxSrvCaching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCaching.setStatus("current")


class _TmnxRadProxSrvCacheKeyPktType_Type(Integer32):
    """Custom type tmnxRadProxSrvCacheKeyPktType based on Integer32"""
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
          ("accessRequest", 1),
          ("accessAccept", 2))
    )


_TmnxRadProxSrvCacheKeyPktType_Type.__name__ = "Integer32"
_TmnxRadProxSrvCacheKeyPktType_Object = MibTableColumn
tmnxRadProxSrvCacheKeyPktType = _TmnxRadProxSrvCacheKeyPktType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 11),
    _TmnxRadProxSrvCacheKeyPktType_Type()
)
tmnxRadProxSrvCacheKeyPktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheKeyPktType.setStatus("current")


class _TmnxRadProxSrvCacheKeyAttrType_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxRadProxSrvCacheKeyAttrType based on TmnxSubRadiusAttrType"""
    defaultValue = 0


_TmnxRadProxSrvCacheKeyAttrType_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxRadProxSrvCacheKeyAttrType_Object = MibTableColumn
tmnxRadProxSrvCacheKeyAttrType = _TmnxRadProxSrvCacheKeyAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 12),
    _TmnxRadProxSrvCacheKeyAttrType_Type()
)
tmnxRadProxSrvCacheKeyAttrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheKeyAttrType.setStatus("current")


class _TmnxRadProxSrvCacheKeyVendorId_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxRadProxSrvCacheKeyVendorId based on TmnxSubRadiusVendorId"""
    defaultValue = 0


_TmnxRadProxSrvCacheKeyVendorId_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxRadProxSrvCacheKeyVendorId_Object = MibTableColumn
tmnxRadProxSrvCacheKeyVendorId = _TmnxRadProxSrvCacheKeyVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 13),
    _TmnxRadProxSrvCacheKeyVendorId_Type()
)
tmnxRadProxSrvCacheKeyVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheKeyVendorId.setStatus("current")


class _TmnxRadProxSrvCacheTimeout_Type(Unsigned32):
    """Custom type tmnxRadProxSrvCacheTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_TmnxRadProxSrvCacheTimeout_Type.__name__ = "Unsigned32"
_TmnxRadProxSrvCacheTimeout_Object = MibTableColumn
tmnxRadProxSrvCacheTimeout = _TmnxRadProxSrvCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 14),
    _TmnxRadProxSrvCacheTimeout_Type()
)
tmnxRadProxSrvCacheTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTimeout.setUnits("seconds")


class _TmnxRadProxSrvCacheTrackAcct_Type(TmnxRadiusAcctStatusType):
    """Custom type tmnxRadProxSrvCacheTrackAcct based on TmnxRadiusAcctStatusType"""
    defaultHexValue = "00"


_TmnxRadProxSrvCacheTrackAcct_Type.__name__ = "TmnxRadiusAcctStatusType"
_TmnxRadProxSrvCacheTrackAcct_Object = MibTableColumn
tmnxRadProxSrvCacheTrackAcct = _TmnxRadProxSrvCacheTrackAcct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 15),
    _TmnxRadProxSrvCacheTrackAcct_Type()
)
tmnxRadProxSrvCacheTrackAcct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTrackAcct.setStatus("current")


class _TmnxRadProxSrvSendAcctResponse_Type(TruthValue):
    """Custom type tmnxRadProxSrvSendAcctResponse based on TruthValue"""
    defaultValue = 2


_TmnxRadProxSrvSendAcctResponse_Type.__name__ = "TruthValue"
_TmnxRadProxSrvSendAcctResponse_Object = MibTableColumn
tmnxRadProxSrvSendAcctResponse = _TmnxRadProxSrvSendAcctResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 16),
    _TmnxRadProxSrvSendAcctResponse_Type()
)
tmnxRadProxSrvSendAcctResponse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvSendAcctResponse.setStatus("current")


class _TmnxRadProxSrvLoadBalanceKey_Type(Integer32):
    """Custom type tmnxRadProxSrvLoadBalanceKey based on Integer32"""
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
          ("sourceIpUdp", 1),
          ("attributes", 2))
    )


_TmnxRadProxSrvLoadBalanceKey_Type.__name__ = "Integer32"
_TmnxRadProxSrvLoadBalanceKey_Object = MibTableColumn
tmnxRadProxSrvLoadBalanceKey = _TmnxRadProxSrvLoadBalanceKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 17),
    _TmnxRadProxSrvLoadBalanceKey_Type()
)
tmnxRadProxSrvLoadBalanceKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBalanceKey.setStatus("current")


class _TmnxRadProxSrvLoadBAttr1_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxRadProxSrvLoadBAttr1 based on TmnxSubRadiusAttrType"""
    defaultValue = 0


_TmnxRadProxSrvLoadBAttr1_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxRadProxSrvLoadBAttr1_Object = MibTableColumn
tmnxRadProxSrvLoadBAttr1 = _TmnxRadProxSrvLoadBAttr1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 18),
    _TmnxRadProxSrvLoadBAttr1_Type()
)
tmnxRadProxSrvLoadBAttr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBAttr1.setStatus("current")


class _TmnxRadProxSrvLoadBVendorId1_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxRadProxSrvLoadBVendorId1 based on TmnxSubRadiusVendorId"""
    defaultValue = 0


_TmnxRadProxSrvLoadBVendorId1_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxRadProxSrvLoadBVendorId1_Object = MibTableColumn
tmnxRadProxSrvLoadBVendorId1 = _TmnxRadProxSrvLoadBVendorId1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 19),
    _TmnxRadProxSrvLoadBVendorId1_Type()
)
tmnxRadProxSrvLoadBVendorId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBVendorId1.setStatus("current")


class _TmnxRadProxSrvLoadBAttr2_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxRadProxSrvLoadBAttr2 based on TmnxSubRadiusAttrType"""
    defaultValue = 0


_TmnxRadProxSrvLoadBAttr2_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxRadProxSrvLoadBAttr2_Object = MibTableColumn
tmnxRadProxSrvLoadBAttr2 = _TmnxRadProxSrvLoadBAttr2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 20),
    _TmnxRadProxSrvLoadBAttr2_Type()
)
tmnxRadProxSrvLoadBAttr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBAttr2.setStatus("current")


class _TmnxRadProxSrvLoadBVendorId2_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxRadProxSrvLoadBVendorId2 based on TmnxSubRadiusVendorId"""
    defaultValue = 0


_TmnxRadProxSrvLoadBVendorId2_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxRadProxSrvLoadBVendorId2_Object = MibTableColumn
tmnxRadProxSrvLoadBVendorId2 = _TmnxRadProxSrvLoadBVendorId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 21),
    _TmnxRadProxSrvLoadBVendorId2_Type()
)
tmnxRadProxSrvLoadBVendorId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBVendorId2.setStatus("current")


class _TmnxRadProxSrvLoadBAttr3_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxRadProxSrvLoadBAttr3 based on TmnxSubRadiusAttrType"""
    defaultValue = 0


_TmnxRadProxSrvLoadBAttr3_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxRadProxSrvLoadBAttr3_Object = MibTableColumn
tmnxRadProxSrvLoadBAttr3 = _TmnxRadProxSrvLoadBAttr3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 22),
    _TmnxRadProxSrvLoadBAttr3_Type()
)
tmnxRadProxSrvLoadBAttr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBAttr3.setStatus("current")


class _TmnxRadProxSrvLoadBVendorId3_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxRadProxSrvLoadBVendorId3 based on TmnxSubRadiusVendorId"""
    defaultValue = 0


_TmnxRadProxSrvLoadBVendorId3_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxRadProxSrvLoadBVendorId3_Object = MibTableColumn
tmnxRadProxSrvLoadBVendorId3 = _TmnxRadProxSrvLoadBVendorId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 23),
    _TmnxRadProxSrvLoadBVendorId3_Type()
)
tmnxRadProxSrvLoadBVendorId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBVendorId3.setStatus("current")


class _TmnxRadProxSrvLoadBAttr4_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxRadProxSrvLoadBAttr4 based on TmnxSubRadiusAttrType"""
    defaultValue = 0


_TmnxRadProxSrvLoadBAttr4_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxRadProxSrvLoadBAttr4_Object = MibTableColumn
tmnxRadProxSrvLoadBAttr4 = _TmnxRadProxSrvLoadBAttr4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 24),
    _TmnxRadProxSrvLoadBAttr4_Type()
)
tmnxRadProxSrvLoadBAttr4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBAttr4.setStatus("current")


class _TmnxRadProxSrvLoadBVendorId4_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxRadProxSrvLoadBVendorId4 based on TmnxSubRadiusVendorId"""
    defaultValue = 0


_TmnxRadProxSrvLoadBVendorId4_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxRadProxSrvLoadBVendorId4_Object = MibTableColumn
tmnxRadProxSrvLoadBVendorId4 = _TmnxRadProxSrvLoadBVendorId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 25),
    _TmnxRadProxSrvLoadBVendorId4_Type()
)
tmnxRadProxSrvLoadBVendorId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBVendorId4.setStatus("current")


class _TmnxRadProxSrvLoadBAttr5_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxRadProxSrvLoadBAttr5 based on TmnxSubRadiusAttrType"""
    defaultValue = 0


_TmnxRadProxSrvLoadBAttr5_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxRadProxSrvLoadBAttr5_Object = MibTableColumn
tmnxRadProxSrvLoadBAttr5 = _TmnxRadProxSrvLoadBAttr5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 26),
    _TmnxRadProxSrvLoadBAttr5_Type()
)
tmnxRadProxSrvLoadBAttr5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBAttr5.setStatus("current")


class _TmnxRadProxSrvLoadBVendorId5_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxRadProxSrvLoadBVendorId5 based on TmnxSubRadiusVendorId"""
    defaultValue = 0


_TmnxRadProxSrvLoadBVendorId5_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxRadProxSrvLoadBVendorId5_Object = MibTableColumn
tmnxRadProxSrvLoadBVendorId5 = _TmnxRadProxSrvLoadBVendorId5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 27),
    _TmnxRadProxSrvLoadBVendorId5_Type()
)
tmnxRadProxSrvLoadBVendorId5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvLoadBVendorId5.setStatus("current")


class _TmnxRadProxSrvCacheTrackAuth_Type(Bits):
    """Custom type tmnxRadProxSrvCacheTrackAuth based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        ("accept", 0)
    )

_TmnxRadProxSrvCacheTrackAuth_Type.__name__ = "Bits"
_TmnxRadProxSrvCacheTrackAuth_Object = MibTableColumn
tmnxRadProxSrvCacheTrackAuth = _TmnxRadProxSrvCacheTrackAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 28),
    _TmnxRadProxSrvCacheTrackAuth_Type()
)
tmnxRadProxSrvCacheTrackAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTrackAuth.setStatus("current")


class _TmnxRadProxSrvWlanGwGroup_Type(TmnxWlanGwIsaGrpIdOrZero):
    """Custom type tmnxRadProxSrvWlanGwGroup based on TmnxWlanGwIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxRadProxSrvWlanGwGroup_Type.__name__ = "TmnxWlanGwIsaGrpIdOrZero"
_TmnxRadProxSrvWlanGwGroup_Object = MibTableColumn
tmnxRadProxSrvWlanGwGroup = _TmnxRadProxSrvWlanGwGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 35),
    _TmnxRadProxSrvWlanGwGroup_Type()
)
tmnxRadProxSrvWlanGwGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvWlanGwGroup.setStatus("current")


class _TmnxRadProxSrvPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadProxSrvPythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadProxSrvPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadProxSrvPythonPolicy_Object = MibTableColumn
tmnxRadProxSrvPythonPolicy = _TmnxRadProxSrvPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 36),
    _TmnxRadProxSrvPythonPolicy_Type()
)
tmnxRadProxSrvPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvPythonPolicy.setStatus("current")


class _TmnxRadProxSrvCacheTrkDelHoldT_Type(Unsigned32):
    """Custom type tmnxRadProxSrvCacheTrkDelHoldT based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TmnxRadProxSrvCacheTrkDelHoldT_Type.__name__ = "Unsigned32"
_TmnxRadProxSrvCacheTrkDelHoldT_Object = MibTableColumn
tmnxRadProxSrvCacheTrkDelHoldT = _TmnxRadProxSrvCacheTrkDelHoldT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 1, 1, 37),
    _TmnxRadProxSrvCacheTrkDelHoldT_Type()
)
tmnxRadProxSrvCacheTrkDelHoldT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTrkDelHoldT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTrkDelHoldT.setUnits("seconds")
_TmnxRadPSStatusTable_Object = MibTable
tmnxRadPSStatusTable = _TmnxRadPSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxRadPSStatusTable.setStatus("current")
_TmnxRadPSStatusEntry_Object = MibTableRow
tmnxRadPSStatusEntry = _TmnxRadPSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxRadPSStatusEntry.setStatus("current")
_TmnxRadPSStatusCacheEntries_Type = Gauge32
_TmnxRadPSStatusCacheEntries_Object = MibTableColumn
tmnxRadPSStatusCacheEntries = _TmnxRadPSStatusCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 2, 1, 1),
    _TmnxRadPSStatusCacheEntries_Type()
)
tmnxRadPSStatusCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatusCacheEntries.setStatus("current")
_TmnxRadPSStatusCacheEntriesReg_Type = Gauge32
_TmnxRadPSStatusCacheEntriesReg_Object = MibTableColumn
tmnxRadPSStatusCacheEntriesReg = _TmnxRadPSStatusCacheEntriesReg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 2, 1, 2),
    _TmnxRadPSStatusCacheEntriesReg_Type()
)
tmnxRadPSStatusCacheEntriesReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatusCacheEntriesReg.setStatus("current")
_TmnxRadPSStatsTable_Object = MibTable
tmnxRadPSStatsTable = _TmnxRadPSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxRadPSStatsTable.setStatus("current")
_TmnxRadPSStatsEntry_Object = MibTableRow
tmnxRadPSStatsEntry = _TmnxRadPSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxRadPSStatsEntry.setStatus("current")
_TmnxRadPSStatsRxPacket_Type = Counter32
_TmnxRadPSStatsRxPacket_Object = MibTableColumn
tmnxRadPSStatsRxPacket = _TmnxRadPSStatsRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 1),
    _TmnxRadPSStatsRxPacket_Type()
)
tmnxRadPSStatsRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxPacket.setStatus("current")
_TmnxRadPSStatsRxAuthRequest_Type = Counter32
_TmnxRadPSStatsRxAuthRequest_Object = MibTableColumn
tmnxRadPSStatsRxAuthRequest = _TmnxRadPSStatsRxAuthRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 2),
    _TmnxRadPSStatsRxAuthRequest_Type()
)
tmnxRadPSStatsRxAuthRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxAuthRequest.setStatus("current")
_TmnxRadPSStatsRxAcctRequest_Type = Counter32
_TmnxRadPSStatsRxAcctRequest_Object = MibTableColumn
tmnxRadPSStatsRxAcctRequest = _TmnxRadPSStatsRxAcctRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 3),
    _TmnxRadPSStatsRxAcctRequest_Type()
)
tmnxRadPSStatsRxAcctRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxAcctRequest.setStatus("current")
_TmnxRadPSStatsRxDropped_Type = Counter32
_TmnxRadPSStatsRxDropped_Object = MibTableColumn
tmnxRadPSStatsRxDropped = _TmnxRadPSStatsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 4),
    _TmnxRadPSStatsRxDropped_Type()
)
tmnxRadPSStatsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxDropped.setStatus("current")
_TmnxRadPSStatsRxRetransmit_Type = Counter32
_TmnxRadPSStatsRxRetransmit_Object = MibTableColumn
tmnxRadPSStatsRxRetransmit = _TmnxRadPSStatsRxRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 5),
    _TmnxRadPSStatsRxRetransmit_Type()
)
tmnxRadPSStatsRxRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxRetransmit.setStatus("current")
_TmnxRadPSStatsRxAdminDown_Type = Counter32
_TmnxRadPSStatsRxAdminDown_Object = MibTableColumn
tmnxRadPSStatsRxAdminDown = _TmnxRadPSStatsRxAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 6),
    _TmnxRadPSStatsRxAdminDown_Type()
)
tmnxRadPSStatsRxAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxAdminDown.setStatus("current")
_TmnxRadPSStatsRxNoAaaPol_Type = Counter32
_TmnxRadPSStatsRxNoAaaPol_Object = MibTableColumn
tmnxRadPSStatsRxNoAaaPol = _TmnxRadPSStatsRxNoAaaPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 7),
    _TmnxRadPSStatsRxNoAaaPol_Type()
)
tmnxRadPSStatsRxNoAaaPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxNoAaaPol.setStatus("current")
_TmnxRadPSStatsRxNoLoadBKey_Type = Counter32
_TmnxRadPSStatsRxNoLoadBKey_Object = MibTableColumn
tmnxRadPSStatsRxNoLoadBKey = _TmnxRadPSStatsRxNoLoadBKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 8),
    _TmnxRadPSStatsRxNoLoadBKey_Type()
)
tmnxRadPSStatsRxNoLoadBKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxNoLoadBKey.setStatus("current")
_TmnxRadPSStatsRxInvLen_Type = Counter32
_TmnxRadPSStatsRxInvLen_Object = MibTableColumn
tmnxRadPSStatsRxInvLen = _TmnxRadPSStatsRxInvLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 9),
    _TmnxRadPSStatsRxInvLen_Type()
)
tmnxRadPSStatsRxInvLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvLen.setStatus("current")
_TmnxRadPSStatsRxInvCode_Type = Counter32
_TmnxRadPSStatsRxInvCode_Object = MibTableColumn
tmnxRadPSStatsRxInvCode = _TmnxRadPSStatsRxInvCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 10),
    _TmnxRadPSStatsRxInvCode_Type()
)
tmnxRadPSStatsRxInvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvCode.setStatus("current")
_TmnxRadPSStatsRxInvAttr_Type = Counter32
_TmnxRadPSStatsRxInvAttr_Object = MibTableColumn
tmnxRadPSStatsRxInvAttr = _TmnxRadPSStatsRxInvAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 11),
    _TmnxRadPSStatsRxInvAttr_Type()
)
tmnxRadPSStatsRxInvAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvAttr.setStatus("current")
_TmnxRadPSStatsRxInvUserName_Type = Counter32
_TmnxRadPSStatsRxInvUserName_Object = MibTableColumn
tmnxRadPSStatsRxInvUserName = _TmnxRadPSStatsRxInvUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 12),
    _TmnxRadPSStatsRxInvUserName_Type()
)
tmnxRadPSStatsRxInvUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvUserName.setStatus("current")
_TmnxRadPSStatsRxInvPassword_Type = Counter32
_TmnxRadPSStatsRxInvPassword_Object = MibTableColumn
tmnxRadPSStatsRxInvPassword = _TmnxRadPSStatsRxInvPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 13),
    _TmnxRadPSStatsRxInvPassword_Type()
)
tmnxRadPSStatsRxInvPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvPassword.setStatus("current")
_TmnxRadPSStatsRxInvAcctStatusTyp_Type = Counter32
_TmnxRadPSStatsRxInvAcctStatusTyp_Object = MibTableColumn
tmnxRadPSStatsRxInvAcctStatusTyp = _TmnxRadPSStatsRxInvAcctStatusTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 14),
    _TmnxRadPSStatsRxInvAcctStatusTyp_Type()
)
tmnxRadPSStatsRxInvAcctStatusTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvAcctStatusTyp.setStatus("current")
_TmnxRadPSStatsRxNoAcctStatusTyp_Type = Counter32
_TmnxRadPSStatsRxNoAcctStatusTyp_Object = MibTableColumn
tmnxRadPSStatsRxNoAcctStatusTyp = _TmnxRadPSStatsRxNoAcctStatusTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 15),
    _TmnxRadPSStatsRxNoAcctStatusTyp_Type()
)
tmnxRadPSStatsRxNoAcctStatusTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxNoAcctStatusTyp.setStatus("current")
_TmnxRadPSStatsRxInvAcctAuth_Type = Counter32
_TmnxRadPSStatsRxInvAcctAuth_Object = MibTableColumn
tmnxRadPSStatsRxInvAcctAuth = _TmnxRadPSStatsRxInvAcctAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 16),
    _TmnxRadPSStatsRxInvAcctAuth_Type()
)
tmnxRadPSStatsRxInvAcctAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvAcctAuth.setStatus("current")
_TmnxRadPSStatsRxInvMsgAuth_Type = Counter32
_TmnxRadPSStatsRxInvMsgAuth_Object = MibTableColumn
tmnxRadPSStatsRxInvMsgAuth = _TmnxRadPSStatsRxInvMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 17),
    _TmnxRadPSStatsRxInvMsgAuth_Type()
)
tmnxRadPSStatsRxInvMsgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxInvMsgAuth.setStatus("current")
_TmnxRadPSStatsRxNoMemory_Type = Counter32
_TmnxRadPSStatsRxNoMemory_Object = MibTableColumn
tmnxRadPSStatsRxNoMemory = _TmnxRadPSStatsRxNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 18),
    _TmnxRadPSStatsRxNoMemory_Type()
)
tmnxRadPSStatsRxNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxNoMemory.setStatus("current")
_TmnxRadPSStatsRxUserOverload_Type = Counter32
_TmnxRadPSStatsRxUserOverload_Object = MibTableColumn
tmnxRadPSStatsRxUserOverload = _TmnxRadPSStatsRxUserOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 19),
    _TmnxRadPSStatsRxUserOverload_Type()
)
tmnxRadPSStatsRxUserOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxUserOverload.setStatus("current")
_TmnxRadPSStatsTxAuthAck_Type = Counter32
_TmnxRadPSStatsTxAuthAck_Object = MibTableColumn
tmnxRadPSStatsTxAuthAck = _TmnxRadPSStatsTxAuthAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 20),
    _TmnxRadPSStatsTxAuthAck_Type()
)
tmnxRadPSStatsTxAuthAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxAuthAck.setStatus("current")
_TmnxRadPSStatsTxAuthReject_Type = Counter32
_TmnxRadPSStatsTxAuthReject_Object = MibTableColumn
tmnxRadPSStatsTxAuthReject = _TmnxRadPSStatsTxAuthReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 21),
    _TmnxRadPSStatsTxAuthReject_Type()
)
tmnxRadPSStatsTxAuthReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxAuthReject.setStatus("current")
_TmnxRadPSStatsTxAuthChallenge_Type = Counter32
_TmnxRadPSStatsTxAuthChallenge_Object = MibTableColumn
tmnxRadPSStatsTxAuthChallenge = _TmnxRadPSStatsTxAuthChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 22),
    _TmnxRadPSStatsTxAuthChallenge_Type()
)
tmnxRadPSStatsTxAuthChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxAuthChallenge.setStatus("current")
_TmnxRadPSStatsTxAcctResponse_Type = Counter32
_TmnxRadPSStatsTxAcctResponse_Object = MibTableColumn
tmnxRadPSStatsTxAcctResponse = _TmnxRadPSStatsTxAcctResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 23),
    _TmnxRadPSStatsTxAcctResponse_Type()
)
tmnxRadPSStatsTxAcctResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxAcctResponse.setStatus("current")
_TmnxRadPSStatsTxDropped_Type = Counter32
_TmnxRadPSStatsTxDropped_Object = MibTableColumn
tmnxRadPSStatsTxDropped = _TmnxRadPSStatsTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 24),
    _TmnxRadPSStatsTxDropped_Type()
)
tmnxRadPSStatsTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxDropped.setStatus("current")
_TmnxRadPSStatsTxCacheNoKey_Type = Counter32
_TmnxRadPSStatsTxCacheNoKey_Object = MibTableColumn
tmnxRadPSStatsTxCacheNoKey = _TmnxRadPSStatsTxCacheNoKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 25),
    _TmnxRadPSStatsTxCacheNoKey_Type()
)
tmnxRadPSStatsTxCacheNoKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxCacheNoKey.setStatus("current")
_TmnxRadPSStatsTxCacheKeyTooLong_Type = Counter32
_TmnxRadPSStatsTxCacheKeyTooLong_Object = MibTableColumn
tmnxRadPSStatsTxCacheKeyTooLong = _TmnxRadPSStatsTxCacheKeyTooLong_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 26),
    _TmnxRadPSStatsTxCacheKeyTooLong_Type()
)
tmnxRadPSStatsTxCacheKeyTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxCacheKeyTooLong.setStatus("current")
_TmnxRadPSStatsTxCacheAttrTooLong_Type = Counter32
_TmnxRadPSStatsTxCacheAttrTooLong_Object = MibTableColumn
tmnxRadPSStatsTxCacheAttrTooLong = _TmnxRadPSStatsTxCacheAttrTooLong_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 27),
    _TmnxRadPSStatsTxCacheAttrTooLong_Type()
)
tmnxRadPSStatsTxCacheAttrTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxCacheAttrTooLong.setStatus("current")
_TmnxRadPSStatsTxCacheMaxEntries_Type = Counter32
_TmnxRadPSStatsTxCacheMaxEntries_Object = MibTableColumn
tmnxRadPSStatsTxCacheMaxEntries = _TmnxRadPSStatsTxCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 28),
    _TmnxRadPSStatsTxCacheMaxEntries_Type()
)
tmnxRadPSStatsTxCacheMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxCacheMaxEntries.setStatus("current")
_TmnxRadPSStatsTxNoMemory_Type = Counter32
_TmnxRadPSStatsTxNoMemory_Object = MibTableColumn
tmnxRadPSStatsTxNoMemory = _TmnxRadPSStatsTxNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 29),
    _TmnxRadPSStatsTxNoMemory_Type()
)
tmnxRadPSStatsTxNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxNoMemory.setStatus("current")
_TmnxRadPSStatsTxServerTimeout_Type = Counter32
_TmnxRadPSStatsTxServerTimeout_Object = MibTableColumn
tmnxRadPSStatsTxServerTimeout = _TmnxRadPSStatsTxServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 30),
    _TmnxRadPSStatsTxServerTimeout_Type()
)
tmnxRadPSStatsTxServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxServerTimeout.setStatus("current")
_TmnxRadPSStatsTxServerAuthFail_Type = Counter32
_TmnxRadPSStatsTxServerAuthFail_Object = MibTableColumn
tmnxRadPSStatsTxServerAuthFail = _TmnxRadPSStatsTxServerAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 31),
    _TmnxRadPSStatsTxServerAuthFail_Type()
)
tmnxRadPSStatsTxServerAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxServerAuthFail.setStatus("current")
_TmnxRadPSStatsTxServerInvCode_Type = Counter32
_TmnxRadPSStatsTxServerInvCode_Object = MibTableColumn
tmnxRadPSStatsTxServerInvCode = _TmnxRadPSStatsTxServerInvCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 32),
    _TmnxRadPSStatsTxServerInvCode_Type()
)
tmnxRadPSStatsTxServerInvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxServerInvCode.setStatus("current")
_TmnxRadPSStatsTxServerInvAttr_Type = Counter32
_TmnxRadPSStatsTxServerInvAttr_Object = MibTableColumn
tmnxRadPSStatsTxServerInvAttr = _TmnxRadPSStatsTxServerInvAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 33),
    _TmnxRadPSStatsTxServerInvAttr_Type()
)
tmnxRadPSStatsTxServerInvAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxServerInvAttr.setStatus("current")
_TmnxRadPSStatsTxUserOverload_Type = Counter32
_TmnxRadPSStatsTxUserOverload_Object = MibTableColumn
tmnxRadPSStatsTxUserOverload = _TmnxRadPSStatsTxUserOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 34),
    _TmnxRadPSStatsTxUserOverload_Type()
)
tmnxRadPSStatsTxUserOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxUserOverload.setStatus("current")
_TmnxRadPSStatsTxNoRadiusServer_Type = Counter32
_TmnxRadPSStatsTxNoRadiusServer_Object = MibTableColumn
tmnxRadPSStatsTxNoRadiusServer = _TmnxRadPSStatsTxNoRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 35),
    _TmnxRadPSStatsTxNoRadiusServer_Type()
)
tmnxRadPSStatsTxNoRadiusServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxNoRadiusServer.setStatus("current")
_TmnxRadPSStatsTxSendFailure_Type = Counter32
_TmnxRadPSStatsTxSendFailure_Object = MibTableColumn
tmnxRadPSStatsTxSendFailure = _TmnxRadPSStatsTxSendFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 36),
    _TmnxRadPSStatsTxSendFailure_Type()
)
tmnxRadPSStatsTxSendFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxSendFailure.setStatus("current")
_TmnxRadPSStatsRxDroppedByPython_Type = Counter32
_TmnxRadPSStatsRxDroppedByPython_Object = MibTableColumn
tmnxRadPSStatsRxDroppedByPython = _TmnxRadPSStatsRxDroppedByPython_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 37),
    _TmnxRadPSStatsRxDroppedByPython_Type()
)
tmnxRadPSStatsRxDroppedByPython.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsRxDroppedByPython.setStatus("current")
_TmnxRadPSStatsTxDroppedByPython_Type = Counter32
_TmnxRadPSStatsTxDroppedByPython_Object = MibTableColumn
tmnxRadPSStatsTxDroppedByPython = _TmnxRadPSStatsTxDroppedByPython_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 3, 1, 38),
    _TmnxRadPSStatsTxDroppedByPython_Type()
)
tmnxRadPSStatsTxDroppedByPython.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadPSStatsTxDroppedByPython.setStatus("current")
_TmnxRadProxSrvIfTable_Object = MibTable
tmnxRadProxSrvIfTable = _TmnxRadProxSrvIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvIfTable.setStatus("current")
_TmnxRadProxSrvIfEntry_Object = MibTableRow
tmnxRadProxSrvIfEntry = _TmnxRadProxSrvIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 4, 1)
)
tmnxRadProxSrvIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvIfEntry.setStatus("current")
_TmnxRadProxSrvIfRowStatus_Type = RowStatus
_TmnxRadProxSrvIfRowStatus_Object = MibTableColumn
tmnxRadProxSrvIfRowStatus = _TmnxRadProxSrvIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 4, 1, 1),
    _TmnxRadProxSrvIfRowStatus_Type()
)
tmnxRadProxSrvIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxSrvIfRowStatus.setStatus("current")
_TmnxRadProxSrvIfLastCh_Type = TimeStamp
_TmnxRadProxSrvIfLastCh_Object = MibTableColumn
tmnxRadProxSrvIfLastCh = _TmnxRadProxSrvIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 4, 1, 2),
    _TmnxRadProxSrvIfLastCh_Type()
)
tmnxRadProxSrvIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvIfLastCh.setStatus("current")
_TmnxRadProxUsrToRspTable_Object = MibTable
tmnxRadProxUsrToRspTable = _TmnxRadProxUsrToRspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspTable.setStatus("current")
_TmnxRadProxUsrToRspEntry_Object = MibTableRow
tmnxRadProxUsrToRspEntry = _TmnxRadProxUsrToRspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1)
)
tmnxRadProxUsrToRspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspIndex"),
)
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspEntry.setStatus("current")


class _TmnxRadProxUsrToRspIndex_Type(Unsigned32):
    """Custom type tmnxRadProxUsrToRspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxRadProxUsrToRspIndex_Type.__name__ = "Unsigned32"
_TmnxRadProxUsrToRspIndex_Object = MibTableColumn
tmnxRadProxUsrToRspIndex = _TmnxRadProxUsrToRspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1, 1),
    _TmnxRadProxUsrToRspIndex_Type()
)
tmnxRadProxUsrToRspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspIndex.setStatus("current")
_TmnxRadProxUsrToRspRowStatus_Type = RowStatus
_TmnxRadProxUsrToRspRowStatus_Object = MibTableColumn
tmnxRadProxUsrToRspRowStatus = _TmnxRadProxUsrToRspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1, 2),
    _TmnxRadProxUsrToRspRowStatus_Type()
)
tmnxRadProxUsrToRspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspRowStatus.setStatus("current")
_TmnxRadProxUsrToRspLastCh_Type = TimeStamp
_TmnxRadProxUsrToRspLastCh_Object = MibTableColumn
tmnxRadProxUsrToRspLastCh = _TmnxRadProxUsrToRspLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1, 3),
    _TmnxRadProxUsrToRspLastCh_Type()
)
tmnxRadProxUsrToRspLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspLastCh.setStatus("current")


class _TmnxRadProxUsrToRspMatchString_Type(TmnxRadMatchString):
    """Custom type tmnxRadProxUsrToRspMatchString based on TmnxRadMatchString"""
    subtypeSpec = TmnxRadMatchString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TmnxRadProxUsrToRspMatchString_Type.__name__ = "TmnxRadMatchString"
_TmnxRadProxUsrToRspMatchString_Object = MibTableColumn
tmnxRadProxUsrToRspMatchString = _TmnxRadProxUsrToRspMatchString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1, 4),
    _TmnxRadProxUsrToRspMatchString_Type()
)
tmnxRadProxUsrToRspMatchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspMatchString.setStatus("current")
_TmnxRadProxUsrToRspAuthSrvPlcy_Type = TNamedItemOrEmpty
_TmnxRadProxUsrToRspAuthSrvPlcy_Object = MibTableColumn
tmnxRadProxUsrToRspAuthSrvPlcy = _TmnxRadProxUsrToRspAuthSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1, 5),
    _TmnxRadProxUsrToRspAuthSrvPlcy_Type()
)
tmnxRadProxUsrToRspAuthSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspAuthSrvPlcy.setStatus("current")
_TmnxRadProxUsrToRspAccSrvPlcy_Type = TNamedItemOrEmpty
_TmnxRadProxUsrToRspAccSrvPlcy_Object = MibTableColumn
tmnxRadProxUsrToRspAccSrvPlcy = _TmnxRadProxUsrToRspAccSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 5, 1, 6),
    _TmnxRadProxUsrToRspAccSrvPlcy_Type()
)
tmnxRadProxUsrToRspAccSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspAccSrvPlcy.setStatus("current")
_TmnxRadProxSrvCacheTable_Object = MibTable
tmnxRadProxSrvCacheTable = _TmnxRadProxSrvCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTable.setStatus("current")
_TmnxRadProxSrvCacheEntry_Object = MibTableRow
tmnxRadProxSrvCacheEntry = _TmnxRadProxSrvCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1)
)
tmnxRadProxSrvCacheEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKey"),
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheEntry.setStatus("current")


class _TmnxRadProxSrvCacheKey_Type(OctetString):
    """Custom type tmnxRadProxSrvCacheKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxRadProxSrvCacheKey_Type.__name__ = "OctetString"
_TmnxRadProxSrvCacheKey_Object = MibTableColumn
tmnxRadProxSrvCacheKey = _TmnxRadProxSrvCacheKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 1),
    _TmnxRadProxSrvCacheKey_Type()
)
tmnxRadProxSrvCacheKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheKey.setStatus("current")
_TmnxRadProxSrvCacheAge_Type = TimeInterval
_TmnxRadProxSrvCacheAge_Object = MibTableColumn
tmnxRadProxSrvCacheAge = _TmnxRadProxSrvCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 2),
    _TmnxRadProxSrvCacheAge_Type()
)
tmnxRadProxSrvCacheAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheAge.setStatus("current")
_TmnxRadProxSrvCacheTimeLeft_Type = TimeInterval
_TmnxRadProxSrvCacheTimeLeft_Object = MibTableColumn
tmnxRadProxSrvCacheTimeLeft = _TmnxRadProxSrvCacheTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 3),
    _TmnxRadProxSrvCacheTimeLeft_Type()
)
tmnxRadProxSrvCacheTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheTimeLeft.setStatus("current")
_TmnxRadProxSrvCacheRequestLength_Type = Unsigned32
_TmnxRadProxSrvCacheRequestLength_Object = MibTableColumn
tmnxRadProxSrvCacheRequestLength = _TmnxRadProxSrvCacheRequestLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 4),
    _TmnxRadProxSrvCacheRequestLength_Type()
)
tmnxRadProxSrvCacheRequestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheRequestLength.setStatus("current")
_TmnxRadProxSrvCacheAcceptLength_Type = Unsigned32
_TmnxRadProxSrvCacheAcceptLength_Object = MibTableColumn
tmnxRadProxSrvCacheAcceptLength = _TmnxRadProxSrvCacheAcceptLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 5),
    _TmnxRadProxSrvCacheAcceptLength_Type()
)
tmnxRadProxSrvCacheAcceptLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheAcceptLength.setStatus("current")
_TmnxRadProxSrvCacheRegistered_Type = TruthValue
_TmnxRadProxSrvCacheRegistered_Object = MibTableColumn
tmnxRadProxSrvCacheRegistered = _TmnxRadProxSrvCacheRegistered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 6),
    _TmnxRadProxSrvCacheRegistered_Type()
)
tmnxRadProxSrvCacheRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheRegistered.setStatus("current")
_TmnxRadProxSrvCacheNasIpAddrTyp_Type = InetAddressType
_TmnxRadProxSrvCacheNasIpAddrTyp_Object = MibTableColumn
tmnxRadProxSrvCacheNasIpAddrTyp = _TmnxRadProxSrvCacheNasIpAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 7),
    _TmnxRadProxSrvCacheNasIpAddrTyp_Type()
)
tmnxRadProxSrvCacheNasIpAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheNasIpAddrTyp.setStatus("current")


class _TmnxRadProxSrvCacheNasIpAddr_Type(InetAddress):
    """Custom type tmnxRadProxSrvCacheNasIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxRadProxSrvCacheNasIpAddr_Type.__name__ = "InetAddress"
_TmnxRadProxSrvCacheNasIpAddr_Object = MibTableColumn
tmnxRadProxSrvCacheNasIpAddr = _TmnxRadProxSrvCacheNasIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 8),
    _TmnxRadProxSrvCacheNasIpAddr_Type()
)
tmnxRadProxSrvCacheNasIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheNasIpAddr.setStatus("current")
_TmnxRadProxSrvCacheNasIp6AddrTyp_Type = InetAddressType
_TmnxRadProxSrvCacheNasIp6AddrTyp_Object = MibTableColumn
tmnxRadProxSrvCacheNasIp6AddrTyp = _TmnxRadProxSrvCacheNasIp6AddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 9),
    _TmnxRadProxSrvCacheNasIp6AddrTyp_Type()
)
tmnxRadProxSrvCacheNasIp6AddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheNasIp6AddrTyp.setStatus("current")


class _TmnxRadProxSrvCacheNasIp6Addr_Type(InetAddress):
    """Custom type tmnxRadProxSrvCacheNasIp6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadProxSrvCacheNasIp6Addr_Type.__name__ = "InetAddress"
_TmnxRadProxSrvCacheNasIp6Addr_Object = MibTableColumn
tmnxRadProxSrvCacheNasIp6Addr = _TmnxRadProxSrvCacheNasIp6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 10),
    _TmnxRadProxSrvCacheNasIp6Addr_Type()
)
tmnxRadProxSrvCacheNasIp6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheNasIp6Addr.setStatus("current")


class _TmnxRadProxSrvCacheCalldStation_Type(OctetString):
    """Custom type tmnxRadProxSrvCacheCalldStation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxRadProxSrvCacheCalldStation_Type.__name__ = "OctetString"
_TmnxRadProxSrvCacheCalldStation_Object = MibTableColumn
tmnxRadProxSrvCacheCalldStation = _TmnxRadProxSrvCacheCalldStation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 6, 1, 11),
    _TmnxRadProxSrvCacheCalldStation_Type()
)
tmnxRadProxSrvCacheCalldStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvCacheCalldStation.setStatus("current")
_TmnxRadPSWlanGwTable_Object = MibTable
tmnxRadPSWlanGwTable = _TmnxRadPSWlanGwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwTable.setStatus("current")
_TmnxRadPSWlanGwEntry_Object = MibTableRow
tmnxRadPSWlanGwEntry = _TmnxRadPSWlanGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8, 1)
)
tmnxRadPSWlanGwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvName"),
)
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwEntry.setStatus("current")
_TmnxRadPSWlanGwLastCh_Type = TimeStamp
_TmnxRadPSWlanGwLastCh_Object = MibTableColumn
tmnxRadPSWlanGwLastCh = _TmnxRadPSWlanGwLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8, 1, 1),
    _TmnxRadPSWlanGwLastCh_Type()
)
tmnxRadPSWlanGwLastCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwLastCh.setStatus("current")


class _TmnxRadPSWlanGwIpv4AddrType_Type(InetAddressType):
    """Custom type tmnxRadPSWlanGwIpv4AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxRadPSWlanGwIpv4AddrType_Type.__name__ = "InetAddressType"
_TmnxRadPSWlanGwIpv4AddrType_Object = MibTableColumn
tmnxRadPSWlanGwIpv4AddrType = _TmnxRadPSWlanGwIpv4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8, 1, 2),
    _TmnxRadPSWlanGwIpv4AddrType_Type()
)
tmnxRadPSWlanGwIpv4AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwIpv4AddrType.setStatus("current")


class _TmnxRadPSWlanGwIpv4Addr_Type(InetAddress):
    """Custom type tmnxRadPSWlanGwIpv4Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxRadPSWlanGwIpv4Addr_Type.__name__ = "InetAddress"
_TmnxRadPSWlanGwIpv4Addr_Object = MibTableColumn
tmnxRadPSWlanGwIpv4Addr = _TmnxRadPSWlanGwIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8, 1, 3),
    _TmnxRadPSWlanGwIpv4Addr_Type()
)
tmnxRadPSWlanGwIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwIpv4Addr.setStatus("current")


class _TmnxRadPSWlanGwIpv6AddrType_Type(InetAddressType):
    """Custom type tmnxRadPSWlanGwIpv6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxRadPSWlanGwIpv6AddrType_Type.__name__ = "InetAddressType"
_TmnxRadPSWlanGwIpv6AddrType_Object = MibTableColumn
tmnxRadPSWlanGwIpv6AddrType = _TmnxRadPSWlanGwIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8, 1, 4),
    _TmnxRadPSWlanGwIpv6AddrType_Type()
)
tmnxRadPSWlanGwIpv6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwIpv6AddrType.setStatus("current")


class _TmnxRadPSWlanGwIpv6Addr_Type(InetAddress):
    """Custom type tmnxRadPSWlanGwIpv6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadPSWlanGwIpv6Addr_Type.__name__ = "InetAddress"
_TmnxRadPSWlanGwIpv6Addr_Object = MibTableColumn
tmnxRadPSWlanGwIpv6Addr = _TmnxRadPSWlanGwIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 1, 8, 1, 5),
    _TmnxRadPSWlanGwIpv6Addr_Type()
)
tmnxRadPSWlanGwIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadPSWlanGwIpv6Addr.setStatus("current")
_TmnxRadSrvObjs_ObjectIdentity = ObjectIdentity
tmnxRadSrvObjs = _TmnxRadSrvObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2)
)
_TmnxRadServTable_Object = MibTable
tmnxRadServTable = _TmnxRadServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxRadServTable.setStatus("current")
_TmnxRadServEntry_Object = MibTableRow
tmnxRadServEntry = _TmnxRadServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1)
)
tmnxRadServEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-RADIUS-MIB", "tmnxRadServName"),
)
if mibBuilder.loadTexts:
    tmnxRadServEntry.setStatus("current")
_TmnxRadServName_Type = TNamedItem
_TmnxRadServName_Object = MibTableColumn
tmnxRadServName = _TmnxRadServName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 1),
    _TmnxRadServName_Type()
)
tmnxRadServName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadServName.setStatus("current")
_TmnxRadServLastCh_Type = TimeStamp
_TmnxRadServLastCh_Object = MibTableColumn
tmnxRadServLastCh = _TmnxRadServLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 2),
    _TmnxRadServLastCh_Type()
)
tmnxRadServLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadServLastCh.setStatus("current")
_TmnxRadServRowStatus_Type = RowStatus
_TmnxRadServRowStatus_Object = MibTableColumn
tmnxRadServRowStatus = _TmnxRadServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 3),
    _TmnxRadServRowStatus_Type()
)
tmnxRadServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServRowStatus.setStatus("current")
_TmnxRadServAddrType_Type = InetAddressType
_TmnxRadServAddrType_Object = MibTableColumn
tmnxRadServAddrType = _TmnxRadServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 4),
    _TmnxRadServAddrType_Type()
)
tmnxRadServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServAddrType.setStatus("current")


class _TmnxRadServAddr_Type(InetAddress):
    """Custom type tmnxRadServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadServAddr_Type.__name__ = "InetAddress"
_TmnxRadServAddr_Object = MibTableColumn
tmnxRadServAddr = _TmnxRadServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 5),
    _TmnxRadServAddr_Type()
)
tmnxRadServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServAddr.setStatus("current")


class _TmnxRadServPort_Type(Unsigned32):
    """Custom type tmnxRadServPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadServPort_Type.__name__ = "Unsigned32"
_TmnxRadServPort_Object = MibTableColumn
tmnxRadServPort = _TmnxRadServPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 6),
    _TmnxRadServPort_Type()
)
tmnxRadServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServPort.setStatus("obsolete")
_TmnxRadServSecret_Type = TmnxAuthSecret
_TmnxRadServSecret_Object = MibTableColumn
tmnxRadServSecret = _TmnxRadServSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 7),
    _TmnxRadServSecret_Type()
)
tmnxRadServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServSecret.setStatus("current")


class _TmnxRadServDescription_Type(TItemDescription):
    """Custom type tmnxRadServDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadServDescription_Type.__name__ = "TItemDescription"
_TmnxRadServDescription_Object = MibTableColumn
tmnxRadServDescription = _TmnxRadServDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 8),
    _TmnxRadServDescription_Type()
)
tmnxRadServDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServDescription.setStatus("current")


class _TmnxRadServAcceptCoa_Type(TruthValue):
    """Custom type tmnxRadServAcceptCoa based on TruthValue"""
    defaultValue = 2


_TmnxRadServAcceptCoa_Type.__name__ = "TruthValue"
_TmnxRadServAcceptCoa_Object = MibTableColumn
tmnxRadServAcceptCoa = _TmnxRadServAcceptCoa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 9),
    _TmnxRadServAcceptCoa_Type()
)
tmnxRadServAcceptCoa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServAcceptCoa.setStatus("current")


class _TmnxRadServCoaScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadServCoaScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadServCoaScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadServCoaScriptPlcy_Object = MibTableColumn
tmnxRadServCoaScriptPlcy = _TmnxRadServCoaScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 10),
    _TmnxRadServCoaScriptPlcy_Type()
)
tmnxRadServCoaScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServCoaScriptPlcy.setStatus("current")


class _TmnxRadServPndRqLimit_Type(TmnxRadiusPendingReqLimit):
    """Custom type tmnxRadServPndRqLimit based on TmnxRadiusPendingReqLimit"""
    defaultValue = 4096


_TmnxRadServPndRqLimit_Type.__name__ = "TmnxRadiusPendingReqLimit"
_TmnxRadServPndRqLimit_Object = MibTableColumn
tmnxRadServPndRqLimit = _TmnxRadServPndRqLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 11),
    _TmnxRadServPndRqLimit_Type()
)
tmnxRadServPndRqLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServPndRqLimit.setStatus("current")


class _TmnxRadServAuthPort_Type(Unsigned32):
    """Custom type tmnxRadServAuthPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadServAuthPort_Type.__name__ = "Unsigned32"
_TmnxRadServAuthPort_Object = MibTableColumn
tmnxRadServAuthPort = _TmnxRadServAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 12),
    _TmnxRadServAuthPort_Type()
)
tmnxRadServAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServAuthPort.setStatus("current")


class _TmnxRadServAcctPort_Type(Unsigned32):
    """Custom type tmnxRadServAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadServAcctPort_Type.__name__ = "Unsigned32"
_TmnxRadServAcctPort_Object = MibTableColumn
tmnxRadServAcctPort = _TmnxRadServAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 13),
    _TmnxRadServAcctPort_Type()
)
tmnxRadServAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServAcctPort.setStatus("current")


class _TmnxRadServPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadServPythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadServPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadServPythonPolicy_Object = MibTableColumn
tmnxRadServPythonPolicy = _TmnxRadServPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 1, 1, 14),
    _TmnxRadServPythonPolicy_Type()
)
tmnxRadServPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadServPythonPolicy.setStatus("current")
_TmnxRadSrvPlcyTable_Object = MibTable
tmnxRadSrvPlcyTable = _TmnxRadSrvPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyTable.setStatus("current")
_TmnxRadSrvPlcyEntry_Object = MibTableRow
tmnxRadSrvPlcyEntry = _TmnxRadSrvPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1)
)
tmnxRadSrvPlcyEntry.setIndexNames(
    (1, "TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyEntry.setStatus("current")
_TmnxRadSrvPlcyName_Type = TNamedItem
_TmnxRadSrvPlcyName_Object = MibTableColumn
tmnxRadSrvPlcyName = _TmnxRadSrvPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 1),
    _TmnxRadSrvPlcyName_Type()
)
tmnxRadSrvPlcyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyName.setStatus("current")
_TmnxRadSrvPlcyRowStatus_Type = RowStatus
_TmnxRadSrvPlcyRowStatus_Object = MibTableColumn
tmnxRadSrvPlcyRowStatus = _TmnxRadSrvPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 2),
    _TmnxRadSrvPlcyRowStatus_Type()
)
tmnxRadSrvPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyRowStatus.setStatus("current")
_TmnxRadSrvPlcyLastCh_Type = TimeStamp
_TmnxRadSrvPlcyLastCh_Object = MibTableColumn
tmnxRadSrvPlcyLastCh = _TmnxRadSrvPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 3),
    _TmnxRadSrvPlcyLastCh_Type()
)
tmnxRadSrvPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyLastCh.setStatus("current")


class _TmnxRadSrvPlcyDescription_Type(TItemDescription):
    """Custom type tmnxRadSrvPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxRadSrvPlcyDescription_Object = MibTableColumn
tmnxRadSrvPlcyDescription = _TmnxRadSrvPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 4),
    _TmnxRadSrvPlcyDescription_Type()
)
tmnxRadSrvPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyDescription.setStatus("current")


class _TmnxRadSrvPlcyTimeout_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 340),
    )


_TmnxRadSrvPlcyTimeout_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyTimeout_Object = MibTableColumn
tmnxRadSrvPlcyTimeout = _TmnxRadSrvPlcyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 100),
    _TmnxRadSrvPlcyTimeout_Type()
)
tmnxRadSrvPlcyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyTimeout.setUnits("seconds")


class _TmnxRadSrvPlcyRetry_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TmnxRadSrvPlcyRetry_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyRetry_Object = MibTableColumn
tmnxRadSrvPlcyRetry = _TmnxRadSrvPlcyRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 101),
    _TmnxRadSrvPlcyRetry_Type()
)
tmnxRadSrvPlcyRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyRetry.setStatus("current")


class _TmnxRadSrvPlcyDownTime_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyDownTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_TmnxRadSrvPlcyDownTime_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyDownTime_Object = MibTableColumn
tmnxRadSrvPlcyDownTime = _TmnxRadSrvPlcyDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 102),
    _TmnxRadSrvPlcyDownTime_Type()
)
tmnxRadSrvPlcyDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyDownTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyDownTime.setUnits("seconds")


class _TmnxRadSrvPlcyRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxRadSrvPlcyRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxRadSrvPlcyRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxRadSrvPlcyRouter_Object = MibTableColumn
tmnxRadSrvPlcyRouter = _TmnxRadSrvPlcyRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 103),
    _TmnxRadSrvPlcyRouter_Type()
)
tmnxRadSrvPlcyRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyRouter.setStatus("current")


class _TmnxRadSrvPlcySrcAddrType_Type(InetAddressType):
    """Custom type tmnxRadSrvPlcySrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxRadSrvPlcySrcAddrType_Type.__name__ = "InetAddressType"
_TmnxRadSrvPlcySrcAddrType_Object = MibTableColumn
tmnxRadSrvPlcySrcAddrType = _TmnxRadSrvPlcySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 104),
    _TmnxRadSrvPlcySrcAddrType_Type()
)
tmnxRadSrvPlcySrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrcAddrType.setStatus("current")


class _TmnxRadSrvPlcySrcAddr_Type(InetAddress):
    """Custom type tmnxRadSrvPlcySrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadSrvPlcySrcAddr_Type.__name__ = "InetAddress"
_TmnxRadSrvPlcySrcAddr_Object = MibTableColumn
tmnxRadSrvPlcySrcAddr = _TmnxRadSrvPlcySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 105),
    _TmnxRadSrvPlcySrcAddr_Type()
)
tmnxRadSrvPlcySrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrcAddr.setStatus("current")


class _TmnxRadSrvPlcyAlgorithm_Type(TmnxSubRadServAlgorithm):
    """Custom type tmnxRadSrvPlcyAlgorithm based on TmnxSubRadServAlgorithm"""
    defaultValue = 1


_TmnxRadSrvPlcyAlgorithm_Type.__name__ = "TmnxSubRadServAlgorithm"
_TmnxRadSrvPlcyAlgorithm_Object = MibTableColumn
tmnxRadSrvPlcyAlgorithm = _TmnxRadSrvPlcyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 106),
    _TmnxRadSrvPlcyAlgorithm_Type()
)
tmnxRadSrvPlcyAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAlgorithm.setStatus("current")


class _TmnxRadSrvPlcyRequestScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadSrvPlcyRequestScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyRequestScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadSrvPlcyRequestScriptPlcy_Object = MibTableColumn
tmnxRadSrvPlcyRequestScriptPlcy = _TmnxRadSrvPlcyRequestScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 107),
    _TmnxRadSrvPlcyRequestScriptPlcy_Type()
)
tmnxRadSrvPlcyRequestScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyRequestScriptPlcy.setStatus("obsolete")


class _TmnxRadSrvPlcyAcceptScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadSrvPlcyAcceptScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyAcceptScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadSrvPlcyAcceptScriptPlcy_Object = MibTableColumn
tmnxRadSrvPlcyAcceptScriptPlcy = _TmnxRadSrvPlcyAcceptScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 108),
    _TmnxRadSrvPlcyAcceptScriptPlcy_Type()
)
tmnxRadSrvPlcyAcceptScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcceptScriptPlcy.setStatus("current")


class _TmnxRadSrvPlcyBlockedState_Type(Integer32):
    """Custom type tmnxRadSrvPlcyBlockedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notBlocked", 0),
          ("blocked", 1))
    )


_TmnxRadSrvPlcyBlockedState_Type.__name__ = "Integer32"
_TmnxRadSrvPlcyBlockedState_Object = MibTableColumn
tmnxRadSrvPlcyBlockedState = _TmnxRadSrvPlcyBlockedState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 109),
    _TmnxRadSrvPlcyBlockedState_Type()
)
tmnxRadSrvPlcyBlockedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyBlockedState.setStatus("current")


class _TmnxRadSrvPlcyAcctReqScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadSrvPlcyAcctReqScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyAcctReqScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadSrvPlcyAcctReqScriptPlcy_Object = MibTableColumn
tmnxRadSrvPlcyAcctReqScriptPlcy = _TmnxRadSrvPlcyAcctReqScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 110),
    _TmnxRadSrvPlcyAcctReqScriptPlcy_Type()
)
tmnxRadSrvPlcyAcctReqScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctReqScriptPlcy.setStatus("current")


class _TmnxRadSrvPlcyAuthReqScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadSrvPlcyAuthReqScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyAuthReqScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadSrvPlcyAuthReqScriptPlcy_Object = MibTableColumn
tmnxRadSrvPlcyAuthReqScriptPlcy = _TmnxRadSrvPlcyAuthReqScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 111),
    _TmnxRadSrvPlcyAuthReqScriptPlcy_Type()
)
tmnxRadSrvPlcyAuthReqScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAuthReqScriptPlcy.setStatus("current")


class _TmnxRadSrvPlcyAcctInterimMinItvl_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctInterimMinItvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxRadSrvPlcyAcctInterimMinItvl_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctInterimMinItvl_Object = MibTableColumn
tmnxRadSrvPlcyAcctInterimMinItvl = _TmnxRadSrvPlcyAcctInterimMinItvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 112),
    _TmnxRadSrvPlcyAcctInterimMinItvl_Type()
)
tmnxRadSrvPlcyAcctInterimMinItvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctInterimMinItvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctInterimMinItvl.setUnits("seconds")


class _TmnxRadSrvPlcyAcctInterimMaxItvl_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctInterimMaxItvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxRadSrvPlcyAcctInterimMaxItvl_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctInterimMaxItvl_Object = MibTableColumn
tmnxRadSrvPlcyAcctInterimMaxItvl = _TmnxRadSrvPlcyAcctInterimMaxItvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 113),
    _TmnxRadSrvPlcyAcctInterimMaxItvl_Type()
)
tmnxRadSrvPlcyAcctInterimMaxItvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctInterimMaxItvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctInterimMaxItvl.setUnits("seconds")


class _TmnxRadSrvPlcyAcctInterimlifetim_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctInterimlifetim based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_TmnxRadSrvPlcyAcctInterimlifetim_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctInterimlifetim_Object = MibTableColumn
tmnxRadSrvPlcyAcctInterimlifetim = _TmnxRadSrvPlcyAcctInterimlifetim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 114),
    _TmnxRadSrvPlcyAcctInterimlifetim_Type()
)
tmnxRadSrvPlcyAcctInterimlifetim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctInterimlifetim.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctInterimlifetim.setUnits("hours")


class _TmnxRadSrvPlcyAcctStopMinItvl_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctStopMinItvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxRadSrvPlcyAcctStopMinItvl_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctStopMinItvl_Object = MibTableColumn
tmnxRadSrvPlcyAcctStopMinItvl = _TmnxRadSrvPlcyAcctStopMinItvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 115),
    _TmnxRadSrvPlcyAcctStopMinItvl_Type()
)
tmnxRadSrvPlcyAcctStopMinItvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctStopMinItvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctStopMinItvl.setUnits("seconds")


class _TmnxRadSrvPlcyAcctStopMaxItvl_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctStopMaxItvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TmnxRadSrvPlcyAcctStopMaxItvl_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctStopMaxItvl_Object = MibTableColumn
tmnxRadSrvPlcyAcctStopMaxItvl = _TmnxRadSrvPlcyAcctStopMaxItvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 116),
    _TmnxRadSrvPlcyAcctStopMaxItvl_Type()
)
tmnxRadSrvPlcyAcctStopMaxItvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctStopMaxItvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctStopMaxItvl.setUnits("seconds")


class _TmnxRadSrvPlcyAcctStoplifetim_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctStoplifetim based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_TmnxRadSrvPlcyAcctStoplifetim_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctStoplifetim_Object = MibTableColumn
tmnxRadSrvPlcyAcctStoplifetim = _TmnxRadSrvPlcyAcctStoplifetim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 117),
    _TmnxRadSrvPlcyAcctStoplifetim_Type()
)
tmnxRadSrvPlcyAcctStoplifetim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctStoplifetim.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctStoplifetim.setUnits("hours")


class _TmnxRadSrvPlcyPythonPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadSrvPlcyPythonPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyPythonPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadSrvPlcyPythonPolicy_Object = MibTableColumn
tmnxRadSrvPlcyPythonPolicy = _TmnxRadSrvPlcyPythonPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 118),
    _TmnxRadSrvPlcyPythonPolicy_Type()
)
tmnxRadSrvPlcyPythonPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyPythonPolicy.setStatus("current")


class _TmnxRadSrvPlcyIpv6SrcAddrType_Type(InetAddressType):
    """Custom type tmnxRadSrvPlcyIpv6SrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxRadSrvPlcyIpv6SrcAddrType_Type.__name__ = "InetAddressType"
_TmnxRadSrvPlcyIpv6SrcAddrType_Object = MibTableColumn
tmnxRadSrvPlcyIpv6SrcAddrType = _TmnxRadSrvPlcyIpv6SrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 119),
    _TmnxRadSrvPlcyIpv6SrcAddrType_Type()
)
tmnxRadSrvPlcyIpv6SrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyIpv6SrcAddrType.setStatus("current")


class _TmnxRadSrvPlcyIpv6SrcAddr_Type(InetAddress):
    """Custom type tmnxRadSrvPlcyIpv6SrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadSrvPlcyIpv6SrcAddr_Type.__name__ = "InetAddress"
_TmnxRadSrvPlcyIpv6SrcAddr_Object = MibTableColumn
tmnxRadSrvPlcyIpv6SrcAddr = _TmnxRadSrvPlcyIpv6SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 2, 1, 120),
    _TmnxRadSrvPlcyIpv6SrcAddr_Type()
)
tmnxRadSrvPlcyIpv6SrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyIpv6SrcAddr.setStatus("current")
_TmnxRadSrvPlcyStatsTable_Object = MibTable
tmnxRadSrvPlcyStatsTable = _TmnxRadSrvPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsTable.setStatus("current")
_TmnxRadSrvPlcyStatsEntry_Object = MibTableRow
tmnxRadSrvPlcyStatsEntry = _TmnxRadSrvPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsEntry.setStatus("current")
_TmnxRadSrvPlcyStatsTxRequests_Type = Counter32
_TmnxRadSrvPlcyStatsTxRequests_Object = MibTableColumn
tmnxRadSrvPlcyStatsTxRequests = _TmnxRadSrvPlcyStatsTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 1),
    _TmnxRadSrvPlcyStatsTxRequests_Type()
)
tmnxRadSrvPlcyStatsTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsTxRequests.setStatus("current")
_TmnxRadSrvPlcyStatsRxResponses_Type = Counter32
_TmnxRadSrvPlcyStatsRxResponses_Object = MibTableColumn
tmnxRadSrvPlcyStatsRxResponses = _TmnxRadSrvPlcyStatsRxResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 2),
    _TmnxRadSrvPlcyStatsRxResponses_Type()
)
tmnxRadSrvPlcyStatsRxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsRxResponses.setStatus("current")
_TmnxRadSrvPlcyStatsReqTimeout_Type = Counter32
_TmnxRadSrvPlcyStatsReqTimeout_Object = MibTableColumn
tmnxRadSrvPlcyStatsReqTimeout = _TmnxRadSrvPlcyStatsReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 3),
    _TmnxRadSrvPlcyStatsReqTimeout_Type()
)
tmnxRadSrvPlcyStatsReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsReqTimeout.setStatus("current")
_TmnxRadSrvPlcyStatsReqSendFail_Type = Counter32
_TmnxRadSrvPlcyStatsReqSendFail_Object = MibTableColumn
tmnxRadSrvPlcyStatsReqSendFail = _TmnxRadSrvPlcyStatsReqSendFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 4),
    _TmnxRadSrvPlcyStatsReqSendFail_Type()
)
tmnxRadSrvPlcyStatsReqSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsReqSendFail.setStatus("current")
_TmnxRadSrvPlcyStatsReqSendRetry_Type = Counter32
_TmnxRadSrvPlcyStatsReqSendRetry_Object = MibTableColumn
tmnxRadSrvPlcyStatsReqSendRetry = _TmnxRadSrvPlcyStatsReqSendRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 5),
    _TmnxRadSrvPlcyStatsReqSendRetry_Type()
)
tmnxRadSrvPlcyStatsReqSendRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsReqSendRetry.setStatus("current")
_TmnxRadSrvPlcyStatsReqRejected_Type = Counter32
_TmnxRadSrvPlcyStatsReqRejected_Object = MibTableColumn
tmnxRadSrvPlcyStatsReqRejected = _TmnxRadSrvPlcyStatsReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 6),
    _TmnxRadSrvPlcyStatsReqRejected_Type()
)
tmnxRadSrvPlcyStatsReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsReqRejected.setStatus("current")
_TmnxRadSrvPlcyStatsAuthFailed_Type = Counter32
_TmnxRadSrvPlcyStatsAuthFailed_Object = MibTableColumn
tmnxRadSrvPlcyStatsAuthFailed = _TmnxRadSrvPlcyStatsAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 7),
    _TmnxRadSrvPlcyStatsAuthFailed_Type()
)
tmnxRadSrvPlcyStatsAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsAuthFailed.setStatus("current")


class _TmnxRadSrvPlcyStatsRejectRatio_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyStatsRejectRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxRadSrvPlcyStatsRejectRatio_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyStatsRejectRatio_Object = MibTableColumn
tmnxRadSrvPlcyStatsRejectRatio = _TmnxRadSrvPlcyStatsRejectRatio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 8),
    _TmnxRadSrvPlcyStatsRejectRatio_Type()
)
tmnxRadSrvPlcyStatsRejectRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsRejectRatio.setStatus("current")
_TmnxRadSrvPlcyStatsAcctFailed_Type = Counter32
_TmnxRadSrvPlcyStatsAcctFailed_Object = MibTableColumn
tmnxRadSrvPlcyStatsAcctFailed = _TmnxRadSrvPlcyStatsAcctFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 9),
    _TmnxRadSrvPlcyStatsAcctFailed_Type()
)
tmnxRadSrvPlcyStatsAcctFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsAcctFailed.setStatus("current")


class _TmnxRadSrvPlcyStatsSuccessRatio_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyStatsSuccessRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxRadSrvPlcyStatsSuccessRatio_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyStatsSuccessRatio_Object = MibTableColumn
tmnxRadSrvPlcyStatsSuccessRatio = _TmnxRadSrvPlcyStatsSuccessRatio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 10),
    _TmnxRadSrvPlcyStatsSuccessRatio_Type()
)
tmnxRadSrvPlcyStatsSuccessRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsSuccessRatio.setStatus("current")


class _TmnxRadSrvPlcyStatsFailureRatio_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyStatsFailureRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxRadSrvPlcyStatsFailureRatio_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyStatsFailureRatio_Object = MibTableColumn
tmnxRadSrvPlcyStatsFailureRatio = _TmnxRadSrvPlcyStatsFailureRatio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 3, 1, 11),
    _TmnxRadSrvPlcyStatsFailureRatio_Type()
)
tmnxRadSrvPlcyStatsFailureRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyStatsFailureRatio.setStatus("current")
_TmnxRadSrvPlcySrvTable_Object = MibTable
tmnxRadSrvPlcySrvTable = _TmnxRadSrvPlcySrvTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvTable.setStatus("current")
_TmnxRadSrvPlcySrvEntry_Object = MibTableRow
tmnxRadSrvPlcySrvEntry = _TmnxRadSrvPlcySrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1)
)
tmnxRadSrvPlcySrvEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvIndex"),
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvEntry.setStatus("current")


class _TmnxRadSrvPlcySrvIndex_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcySrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxRadSrvPlcySrvIndex_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcySrvIndex_Object = MibTableColumn
tmnxRadSrvPlcySrvIndex = _TmnxRadSrvPlcySrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 1),
    _TmnxRadSrvPlcySrvIndex_Type()
)
tmnxRadSrvPlcySrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvIndex.setStatus("current")
_TmnxRadSrvPlcySrvRowStatus_Type = RowStatus
_TmnxRadSrvPlcySrvRowStatus_Object = MibTableColumn
tmnxRadSrvPlcySrvRowStatus = _TmnxRadSrvPlcySrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 2),
    _TmnxRadSrvPlcySrvRowStatus_Type()
)
tmnxRadSrvPlcySrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvRowStatus.setStatus("current")
_TmnxRadSrvPlcySrvLastCh_Type = TimeStamp
_TmnxRadSrvPlcySrvLastCh_Object = MibTableColumn
tmnxRadSrvPlcySrvLastCh = _TmnxRadSrvPlcySrvLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 3),
    _TmnxRadSrvPlcySrvLastCh_Type()
)
tmnxRadSrvPlcySrvLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvLastCh.setStatus("current")
_TmnxRadSrvPlcySrvName_Type = TNamedItem
_TmnxRadSrvPlcySrvName_Object = MibTableColumn
tmnxRadSrvPlcySrvName = _TmnxRadSrvPlcySrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 4),
    _TmnxRadSrvPlcySrvName_Type()
)
tmnxRadSrvPlcySrvName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvName.setStatus("current")
_TmnxRadSrvPlcySrvOperState_Type = TmnxRadiusServerOperState
_TmnxRadSrvPlcySrvOperState_Object = MibTableColumn
tmnxRadSrvPlcySrvOperState = _TmnxRadSrvPlcySrvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 5),
    _TmnxRadSrvPlcySrvOperState_Type()
)
tmnxRadSrvPlcySrvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvOperState.setStatus("current")
_TmnxRadSrvPlcySrvOutTime_Type = Counter32
_TmnxRadSrvPlcySrvOutTime_Object = MibTableColumn
tmnxRadSrvPlcySrvOutTime = _TmnxRadSrvPlcySrvOutTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 6),
    _TmnxRadSrvPlcySrvOutTime_Type()
)
tmnxRadSrvPlcySrvOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvOutTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvOutTime.setUnits("seconds")
_TmnxRadSrvPlcySrvOvrldTime_Type = Counter32
_TmnxRadSrvPlcySrvOvrldTime_Object = MibTableColumn
tmnxRadSrvPlcySrvOvrldTime = _TmnxRadSrvPlcySrvOvrldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 4, 1, 7),
    _TmnxRadSrvPlcySrvOvrldTime_Type()
)
tmnxRadSrvPlcySrvOvrldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvOvrldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvOvrldTime.setUnits("seconds")
_TmnxRadSrvStatsTable_Object = MibTable
tmnxRadSrvStatsTable = _TmnxRadSrvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxRadSrvStatsTable.setStatus("current")
_TmnxRadSrvStatsEntry_Object = MibTableRow
tmnxRadSrvStatsEntry = _TmnxRadSrvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxRadSrvStatsEntry.setStatus("current")
_TmnxRadSrvStatsTxRequests_Type = Counter32
_TmnxRadSrvStatsTxRequests_Object = MibTableColumn
tmnxRadSrvStatsTxRequests = _TmnxRadSrvStatsTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 1),
    _TmnxRadSrvStatsTxRequests_Type()
)
tmnxRadSrvStatsTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsTxRequests.setStatus("current")
_TmnxRadSrvStatsRxResponses_Type = Counter32
_TmnxRadSrvStatsRxResponses_Object = MibTableColumn
tmnxRadSrvStatsRxResponses = _TmnxRadSrvStatsRxResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 2),
    _TmnxRadSrvStatsRxResponses_Type()
)
tmnxRadSrvStatsRxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsRxResponses.setStatus("current")
_TmnxRadSrvStatsReqTimeout_Type = Counter32
_TmnxRadSrvStatsReqTimeout_Object = MibTableColumn
tmnxRadSrvStatsReqTimeout = _TmnxRadSrvStatsReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 3),
    _TmnxRadSrvStatsReqTimeout_Type()
)
tmnxRadSrvStatsReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsReqTimeout.setStatus("current")
_TmnxRadSrvStatsReqSendFailure_Type = Counter32
_TmnxRadSrvStatsReqSendFailure_Object = MibTableColumn
tmnxRadSrvStatsReqSendFailure = _TmnxRadSrvStatsReqSendFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 4),
    _TmnxRadSrvStatsReqSendFailure_Type()
)
tmnxRadSrvStatsReqSendFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsReqSendFailure.setStatus("current")
_TmnxRadSrvStatsReqOvrldSendFail_Type = Counter32
_TmnxRadSrvStatsReqOvrldSendFail_Object = MibTableColumn
tmnxRadSrvStatsReqOvrldSendFail = _TmnxRadSrvStatsReqOvrldSendFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 5),
    _TmnxRadSrvStatsReqOvrldSendFail_Type()
)
tmnxRadSrvStatsReqOvrldSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsReqOvrldSendFail.setStatus("current")
_TmnxRadSrvStatsReqPending_Type = Counter32
_TmnxRadSrvStatsReqPending_Object = MibTableColumn
tmnxRadSrvStatsReqPending = _TmnxRadSrvStatsReqPending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 6),
    _TmnxRadSrvStatsReqPending_Type()
)
tmnxRadSrvStatsReqPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsReqPending.setStatus("current")
_TmnxRadSrvStatsRespInvAuth_Type = Counter32
_TmnxRadSrvStatsRespInvAuth_Object = MibTableColumn
tmnxRadSrvStatsRespInvAuth = _TmnxRadSrvStatsRespInvAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 7),
    _TmnxRadSrvStatsRespInvAuth_Type()
)
tmnxRadSrvStatsRespInvAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsRespInvAuth.setStatus("current")
_TmnxRadSrvStatsRespInvMsgAuth_Type = Counter32
_TmnxRadSrvStatsRespInvMsgAuth_Object = MibTableColumn
tmnxRadSrvStatsRespInvMsgAuth = _TmnxRadSrvStatsRespInvMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 8),
    _TmnxRadSrvStatsRespInvMsgAuth_Type()
)
tmnxRadSrvStatsRespInvMsgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsRespInvMsgAuth.setStatus("current")
_TmnxRadSrvStatsAuthFailed_Type = Counter32
_TmnxRadSrvStatsAuthFailed_Object = MibTableColumn
tmnxRadSrvStatsAuthFailed = _TmnxRadSrvStatsAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 9),
    _TmnxRadSrvStatsAuthFailed_Type()
)
tmnxRadSrvStatsAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAuthFailed.setStatus("current")
_TmnxRadSrvStatsAcctFailed_Type = Counter32
_TmnxRadSrvStatsAcctFailed_Object = MibTableColumn
tmnxRadSrvStatsAcctFailed = _TmnxRadSrvStatsAcctFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 10),
    _TmnxRadSrvStatsAcctFailed_Type()
)
tmnxRadSrvStatsAcctFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAcctFailed.setStatus("current")
_TmnxRadSrvStatsAuthAvgDelay10_Type = Gauge32
_TmnxRadSrvStatsAuthAvgDelay10_Object = MibTableColumn
tmnxRadSrvStatsAuthAvgDelay10 = _TmnxRadSrvStatsAuthAvgDelay10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 11),
    _TmnxRadSrvStatsAuthAvgDelay10_Type()
)
tmnxRadSrvStatsAuthAvgDelay10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAuthAvgDelay10.setStatus("current")
_TmnxRadSrvStatsAuthAvgDelay100_Type = Gauge32
_TmnxRadSrvStatsAuthAvgDelay100_Object = MibTableColumn
tmnxRadSrvStatsAuthAvgDelay100 = _TmnxRadSrvStatsAuthAvgDelay100_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 12),
    _TmnxRadSrvStatsAuthAvgDelay100_Type()
)
tmnxRadSrvStatsAuthAvgDelay100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAuthAvgDelay100.setStatus("current")
_TmnxRadSrvStatsAuthAvgDelay1000_Type = Gauge32
_TmnxRadSrvStatsAuthAvgDelay1000_Object = MibTableColumn
tmnxRadSrvStatsAuthAvgDelay1000 = _TmnxRadSrvStatsAuthAvgDelay1000_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 13),
    _TmnxRadSrvStatsAuthAvgDelay1000_Type()
)
tmnxRadSrvStatsAuthAvgDelay1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAuthAvgDelay1000.setStatus("current")
_TmnxRadSrvStatsAuthAvgDelay10000_Type = Gauge32
_TmnxRadSrvStatsAuthAvgDelay10000_Object = MibTableColumn
tmnxRadSrvStatsAuthAvgDelay10000 = _TmnxRadSrvStatsAuthAvgDelay10000_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 14),
    _TmnxRadSrvStatsAuthAvgDelay10000_Type()
)
tmnxRadSrvStatsAuthAvgDelay10000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAuthAvgDelay10000.setStatus("current")
_TmnxRadSrvStatsAcctAvgDelay10_Type = Gauge32
_TmnxRadSrvStatsAcctAvgDelay10_Object = MibTableColumn
tmnxRadSrvStatsAcctAvgDelay10 = _TmnxRadSrvStatsAcctAvgDelay10_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 15),
    _TmnxRadSrvStatsAcctAvgDelay10_Type()
)
tmnxRadSrvStatsAcctAvgDelay10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAcctAvgDelay10.setStatus("current")
_TmnxRadSrvStatsAcctAvgDelay100_Type = Gauge32
_TmnxRadSrvStatsAcctAvgDelay100_Object = MibTableColumn
tmnxRadSrvStatsAcctAvgDelay100 = _TmnxRadSrvStatsAcctAvgDelay100_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 16),
    _TmnxRadSrvStatsAcctAvgDelay100_Type()
)
tmnxRadSrvStatsAcctAvgDelay100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAcctAvgDelay100.setStatus("current")
_TmnxRadSrvStatsAcctAvgDelay1000_Type = Gauge32
_TmnxRadSrvStatsAcctAvgDelay1000_Object = MibTableColumn
tmnxRadSrvStatsAcctAvgDelay1000 = _TmnxRadSrvStatsAcctAvgDelay1000_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 17),
    _TmnxRadSrvStatsAcctAvgDelay1000_Type()
)
tmnxRadSrvStatsAcctAvgDelay1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAcctAvgDelay1000.setStatus("current")
_TmnxRadSrvStatsAcctAvgDelay10000_Type = Gauge32
_TmnxRadSrvStatsAcctAvgDelay10000_Object = MibTableColumn
tmnxRadSrvStatsAcctAvgDelay10000 = _TmnxRadSrvStatsAcctAvgDelay10000_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 5, 1, 18),
    _TmnxRadSrvStatsAcctAvgDelay10000_Type()
)
tmnxRadSrvStatsAcctAvgDelay10000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvStatsAcctAvgDelay10000.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffTable_Object = MibTable
tmnxRadSrvPlcyAcctOnOffTable = _TmnxRadSrvPlcyAcctOnOffTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffTable.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffEntry_Object = MibTableRow
tmnxRadSrvPlcyAcctOnOffEntry = _TmnxRadSrvPlcyAcctOnOffEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffEntry.setStatus("current")
_TmnxRadSrvPlcyAcctLastChange_Type = TimeStamp
_TmnxRadSrvPlcyAcctLastChange_Object = MibTableColumn
tmnxRadSrvPlcyAcctLastChange = _TmnxRadSrvPlcyAcctLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 1),
    _TmnxRadSrvPlcyAcctLastChange_Type()
)
tmnxRadSrvPlcyAcctLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctLastChange.setStatus("current")


class _TmnxRadSrvPlcyAcctOnOffAdminSt_Type(Integer32):
    """Custom type tmnxRadSrvPlcyAcctOnOffAdminSt based on Integer32"""
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
        *(("disabled", 0),
          ("enabled", 1),
          ("enabledStateChange", 2),
          ("enabledMonitoring", 3))
    )


_TmnxRadSrvPlcyAcctOnOffAdminSt_Type.__name__ = "Integer32"
_TmnxRadSrvPlcyAcctOnOffAdminSt_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffAdminSt = _TmnxRadSrvPlcyAcctOnOffAdminSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 2),
    _TmnxRadSrvPlcyAcctOnOffAdminSt_Type()
)
tmnxRadSrvPlcyAcctOnOffAdminSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffAdminSt.setStatus("current")


class _TmnxRadSrvPlcyAcctOnOffOperState_Type(Integer32):
    """Custom type tmnxRadSrvPlcyAcctOnOffOperState based on Integer32"""
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
        *(("notApplicable", 0),
          ("off", 1),
          ("offNoResponse", 2),
          ("on", 3),
          ("sendingAcctOn", 4),
          ("sendingAcctOff", 5))
    )


_TmnxRadSrvPlcyAcctOnOffOperState_Type.__name__ = "Integer32"
_TmnxRadSrvPlcyAcctOnOffOperState_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffOperState = _TmnxRadSrvPlcyAcctOnOffOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 3),
    _TmnxRadSrvPlcyAcctOnOffOperState_Type()
)
tmnxRadSrvPlcyAcctOnOffOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffOperState.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffSessionId_Type = DisplayString
_TmnxRadSrvPlcyAcctOnOffSessionId_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffSessionId = _TmnxRadSrvPlcyAcctOnOffSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 4),
    _TmnxRadSrvPlcyAcctOnOffSessionId_Type()
)
tmnxRadSrvPlcyAcctOnOffSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffSessionId.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffStateChng_Type = TimeStamp
_TmnxRadSrvPlcyAcctOnOffStateChng_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffStateChng = _TmnxRadSrvPlcyAcctOnOffStateChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 5),
    _TmnxRadSrvPlcyAcctOnOffStateChng_Type()
)
tmnxRadSrvPlcyAcctOnOffStateChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffStateChng.setStatus("current")


class _TmnxRadSrvPlcyAcctPerformAction_Type(Integer32):
    """Custom type tmnxRadSrvPlcyAcctPerformAction based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("acctOn", 1),
          ("acctOnForce", 2),
          ("acctOff", 3),
          ("acctOffForce", 4))
    )


_TmnxRadSrvPlcyAcctPerformAction_Type.__name__ = "Integer32"
_TmnxRadSrvPlcyAcctPerformAction_Object = MibTableColumn
tmnxRadSrvPlcyAcctPerformAction = _TmnxRadSrvPlcyAcctPerformAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 6),
    _TmnxRadSrvPlcyAcctPerformAction_Type()
)
tmnxRadSrvPlcyAcctPerformAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctPerformAction.setStatus("current")


class _TmnxRadSrvPlcyAcctmAcctOffCause_Type(Unsigned32):
    """Custom type tmnxRadSrvPlcyAcctmAcctOffCause based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxRadSrvPlcyAcctmAcctOffCause_Type.__name__ = "Unsigned32"
_TmnxRadSrvPlcyAcctmAcctOffCause_Object = MibTableColumn
tmnxRadSrvPlcyAcctmAcctOffCause = _TmnxRadSrvPlcyAcctmAcctOffCause_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 7),
    _TmnxRadSrvPlcyAcctmAcctOffCause_Type()
)
tmnxRadSrvPlcyAcctmAcctOffCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctmAcctOffCause.setStatus("current")


class _TmnxRadSrvPlcyAcctOnOffTrigger_Type(Integer32):
    """Custom type tmnxRadSrvPlcyAcctOnOffTrigger based on Integer32"""
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
        *(("notApplicable", 0),
          ("startUp", 1),
          ("tools", 2),
          ("toolsForced", 3),
          ("reboot", 4),
          ("group", 5))
    )


_TmnxRadSrvPlcyAcctOnOffTrigger_Type.__name__ = "Integer32"
_TmnxRadSrvPlcyAcctOnOffTrigger_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffTrigger = _TmnxRadSrvPlcyAcctOnOffTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 8),
    _TmnxRadSrvPlcyAcctOnOffTrigger_Type()
)
tmnxRadSrvPlcyAcctOnOffTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffTrigger.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffSrvName_Type = TNamedItemOrEmpty
_TmnxRadSrvPlcyAcctOnOffSrvName_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffSrvName = _TmnxRadSrvPlcyAcctOnOffSrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 9),
    _TmnxRadSrvPlcyAcctOnOffSrvName_Type()
)
tmnxRadSrvPlcyAcctOnOffSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffSrvName.setStatus("current")


class _TmnxRadSrvPlcyAcctOnOffGroup_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadSrvPlcyAcctOnOffGroup based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyAcctOnOffGroup_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadSrvPlcyAcctOnOffGroup_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffGroup = _TmnxRadSrvPlcyAcctOnOffGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 10),
    _TmnxRadSrvPlcyAcctOnOffGroup_Type()
)
tmnxRadSrvPlcyAcctOnOffGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGroup.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffRetryCnt_Type = Unsigned32
_TmnxRadSrvPlcyAcctOnOffRetryCnt_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffRetryCnt = _TmnxRadSrvPlcyAcctOnOffRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 6, 1, 11),
    _TmnxRadSrvPlcyAcctOnOffRetryCnt_Type()
)
tmnxRadSrvPlcyAcctOnOffRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffRetryCnt.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffGrpTable_Object = MibTable
tmnxRadSrvPlcyAcctOnOffGrpTable = _TmnxRadSrvPlcyAcctOnOffGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpTable.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffGrpEntry_Object = MibTableRow
tmnxRadSrvPlcyAcctOnOffGrpEntry = _TmnxRadSrvPlcyAcctOnOffGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 7, 1)
)
tmnxRadSrvPlcyAcctOnOffGrpEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffGrpName"),
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpEntry.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffGrpName_Type = TNamedItem
_TmnxRadSrvPlcyAcctOnOffGrpName_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffGrpName = _TmnxRadSrvPlcyAcctOnOffGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 7, 1, 1),
    _TmnxRadSrvPlcyAcctOnOffGrpName_Type()
)
tmnxRadSrvPlcyAcctOnOffGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpName.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffGrpRowSt_Type = RowStatus
_TmnxRadSrvPlcyAcctOnOffGrpRowSt_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffGrpRowSt = _TmnxRadSrvPlcyAcctOnOffGrpRowSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 7, 1, 2),
    _TmnxRadSrvPlcyAcctOnOffGrpRowSt_Type()
)
tmnxRadSrvPlcyAcctOnOffGrpRowSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpRowSt.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffGrpLastCh_Type = TimeStamp
_TmnxRadSrvPlcyAcctOnOffGrpLastCh_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffGrpLastCh = _TmnxRadSrvPlcyAcctOnOffGrpLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 7, 1, 3),
    _TmnxRadSrvPlcyAcctOnOffGrpLastCh_Type()
)
tmnxRadSrvPlcyAcctOnOffGrpLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpLastCh.setStatus("current")


class _TmnxRadSrvPlcyAcctOnOffGrpDescr_Type(TItemDescription):
    """Custom type tmnxRadSrvPlcyAcctOnOffGrpDescr based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadSrvPlcyAcctOnOffGrpDescr_Type.__name__ = "TItemDescription"
_TmnxRadSrvPlcyAcctOnOffGrpDescr_Object = MibTableColumn
tmnxRadSrvPlcyAcctOnOffGrpDescr = _TmnxRadSrvPlcyAcctOnOffGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 7, 1, 4),
    _TmnxRadSrvPlcyAcctOnOffGrpDescr_Type()
)
tmnxRadSrvPlcyAcctOnOffGrpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpDescr.setStatus("current")
_TmnxRadSrvPlcyMsgBufStatsTable_Object = MibTable
tmnxRadSrvPlcyMsgBufStatsTable = _TmnxRadSrvPlcyMsgBufStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyMsgBufStatsTable.setStatus("current")
_TmnxRadSrvPlcyMsgBufStatsEntry_Object = MibTableRow
tmnxRadSrvPlcyMsgBufStatsEntry = _TmnxRadSrvPlcyMsgBufStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyMsgBufStatsEntry.setStatus("current")
_TmnxRadSrvPlcyNbrAcctStopBuf_Type = Counter32
_TmnxRadSrvPlcyNbrAcctStopBuf_Object = MibTableColumn
tmnxRadSrvPlcyNbrAcctStopBuf = _TmnxRadSrvPlcyNbrAcctStopBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1, 1),
    _TmnxRadSrvPlcyNbrAcctStopBuf_Type()
)
tmnxRadSrvPlcyNbrAcctStopBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyNbrAcctStopBuf.setStatus("current")
_TmnxRadSrvPlcyNbrAcctInterimBuf_Type = Counter32
_TmnxRadSrvPlcyNbrAcctInterimBuf_Object = MibTableColumn
tmnxRadSrvPlcyNbrAcctInterimBuf = _TmnxRadSrvPlcyNbrAcctInterimBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1, 2),
    _TmnxRadSrvPlcyNbrAcctInterimBuf_Type()
)
tmnxRadSrvPlcyNbrAcctInterimBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyNbrAcctInterimBuf.setStatus("current")
_TmnxRadSrvPlcyNbrAcctStopDrop_Type = Counter32
_TmnxRadSrvPlcyNbrAcctStopDrop_Object = MibTableColumn
tmnxRadSrvPlcyNbrAcctStopDrop = _TmnxRadSrvPlcyNbrAcctStopDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1, 3),
    _TmnxRadSrvPlcyNbrAcctStopDrop_Type()
)
tmnxRadSrvPlcyNbrAcctStopDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyNbrAcctStopDrop.setStatus("current")
_TmnxRadSrvPlcyNbrAcctInterimDrop_Type = Counter32
_TmnxRadSrvPlcyNbrAcctInterimDrop_Object = MibTableColumn
tmnxRadSrvPlcyNbrAcctInterimDrop = _TmnxRadSrvPlcyNbrAcctInterimDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1, 4),
    _TmnxRadSrvPlcyNbrAcctInterimDrop_Type()
)
tmnxRadSrvPlcyNbrAcctInterimDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyNbrAcctInterimDrop.setStatus("current")
_TmnxRadSrvPlcyLastBufClean_Type = TimeStamp
_TmnxRadSrvPlcyLastBufClean_Object = MibTableColumn
tmnxRadSrvPlcyLastBufClean = _TmnxRadSrvPlcyLastBufClean_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1, 5),
    _TmnxRadSrvPlcyLastBufClean_Type()
)
tmnxRadSrvPlcyLastBufClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyLastBufClean.setStatus("current")
_TmnxRadSrvPlcyLastBufStatsClean_Type = TimeStamp
_TmnxRadSrvPlcyLastBufStatsClean_Object = MibTableColumn
tmnxRadSrvPlcyLastBufStatsClean = _TmnxRadSrvPlcyLastBufStatsClean_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 2, 8, 1, 6),
    _TmnxRadSrvPlcyLastBufStatsClean_Type()
)
tmnxRadSrvPlcyLastBufStatsClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyLastBufStatsClean.setStatus("current")
_TmnxRadScriptPlcyObjs_ObjectIdentity = ObjectIdentity
tmnxRadScriptPlcyObjs = _TmnxRadScriptPlcyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3)
)
_TmnxRadScriptPlcyTable_Object = MibTable
tmnxRadScriptPlcyTable = _TmnxRadScriptPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyTable.setStatus("current")
_TmnxRadScriptPlcyEntry_Object = MibTableRow
tmnxRadScriptPlcyEntry = _TmnxRadScriptPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1)
)
tmnxRadScriptPlcyEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyEntry.setStatus("current")
_TmnxRadScriptPlcyName_Type = TNamedItem
_TmnxRadScriptPlcyName_Object = MibTableColumn
tmnxRadScriptPlcyName = _TmnxRadScriptPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 1),
    _TmnxRadScriptPlcyName_Type()
)
tmnxRadScriptPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyName.setStatus("current")
_TmnxRadScriptPlcyRowStatus_Type = RowStatus
_TmnxRadScriptPlcyRowStatus_Object = MibTableColumn
tmnxRadScriptPlcyRowStatus = _TmnxRadScriptPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 2),
    _TmnxRadScriptPlcyRowStatus_Type()
)
tmnxRadScriptPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyRowStatus.setStatus("current")
_TmnxRadScriptPlcyLastCh_Type = TimeStamp
_TmnxRadScriptPlcyLastCh_Object = MibTableColumn
tmnxRadScriptPlcyLastCh = _TmnxRadScriptPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 3),
    _TmnxRadScriptPlcyLastCh_Type()
)
tmnxRadScriptPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyLastCh.setStatus("current")


class _TmnxRadScriptPlcyDescription_Type(TItemDescription):
    """Custom type tmnxRadScriptPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadScriptPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxRadScriptPlcyDescription_Object = MibTableColumn
tmnxRadScriptPlcyDescription = _TmnxRadScriptPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 4),
    _TmnxRadScriptPlcyDescription_Type()
)
tmnxRadScriptPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyDescription.setStatus("current")


class _TmnxRadScriptPlcyOnFail_Type(Integer32):
    """Custom type tmnxRadScriptPlcyOnFail based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 1),
          ("drop", 2))
    )


_TmnxRadScriptPlcyOnFail_Type.__name__ = "Integer32"
_TmnxRadScriptPlcyOnFail_Object = MibTableColumn
tmnxRadScriptPlcyOnFail = _TmnxRadScriptPlcyOnFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 5),
    _TmnxRadScriptPlcyOnFail_Type()
)
tmnxRadScriptPlcyOnFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyOnFail.setStatus("current")


class _TmnxRadScriptPlcyPriURL_Type(TmnxDisplayStringURL):
    """Custom type tmnxRadScriptPlcyPriURL based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxRadScriptPlcyPriURL_Type.__name__ = "TmnxDisplayStringURL"
_TmnxRadScriptPlcyPriURL_Object = MibTableColumn
tmnxRadScriptPlcyPriURL = _TmnxRadScriptPlcyPriURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 6),
    _TmnxRadScriptPlcyPriURL_Type()
)
tmnxRadScriptPlcyPriURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyPriURL.setStatus("current")


class _TmnxRadScriptPlcyPriAdminState_Type(TmnxAdminState):
    """Custom type tmnxRadScriptPlcyPriAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxRadScriptPlcyPriAdminState_Type.__name__ = "TmnxAdminState"
_TmnxRadScriptPlcyPriAdminState_Object = MibTableColumn
tmnxRadScriptPlcyPriAdminState = _TmnxRadScriptPlcyPriAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 7),
    _TmnxRadScriptPlcyPriAdminState_Type()
)
tmnxRadScriptPlcyPriAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyPriAdminState.setStatus("current")
_TmnxRadScriptPlcyPriOperState_Type = TmnxOperState
_TmnxRadScriptPlcyPriOperState_Object = MibTableColumn
tmnxRadScriptPlcyPriOperState = _TmnxRadScriptPlcyPriOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 8),
    _TmnxRadScriptPlcyPriOperState_Type()
)
tmnxRadScriptPlcyPriOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyPriOperState.setStatus("current")


class _TmnxRadScriptPlcySecURL_Type(TmnxDisplayStringURL):
    """Custom type tmnxRadScriptPlcySecURL based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxRadScriptPlcySecURL_Type.__name__ = "TmnxDisplayStringURL"
_TmnxRadScriptPlcySecURL_Object = MibTableColumn
tmnxRadScriptPlcySecURL = _TmnxRadScriptPlcySecURL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 9),
    _TmnxRadScriptPlcySecURL_Type()
)
tmnxRadScriptPlcySecURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcySecURL.setStatus("current")


class _TmnxRadScriptPlcySecAdminState_Type(TmnxAdminState):
    """Custom type tmnxRadScriptPlcySecAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxRadScriptPlcySecAdminState_Type.__name__ = "TmnxAdminState"
_TmnxRadScriptPlcySecAdminState_Object = MibTableColumn
tmnxRadScriptPlcySecAdminState = _TmnxRadScriptPlcySecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 10),
    _TmnxRadScriptPlcySecAdminState_Type()
)
tmnxRadScriptPlcySecAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcySecAdminState.setStatus("current")
_TmnxRadScriptPlcySecOperState_Type = TmnxOperState
_TmnxRadScriptPlcySecOperState_Object = MibTableColumn
tmnxRadScriptPlcySecOperState = _TmnxRadScriptPlcySecOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 3, 1, 1, 11),
    _TmnxRadScriptPlcySecOperState_Type()
)
tmnxRadScriptPlcySecOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcySecOperState.setStatus("current")
_TmnxRadRouteDownlObjs_ObjectIdentity = ObjectIdentity
tmnxRadRouteDownlObjs = _TmnxRadRouteDownlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4)
)
_TmnxRadRouteDownlTable_Object = MibTable
tmnxRadRouteDownlTable = _TmnxRadRouteDownlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxRadRouteDownlTable.setStatus("current")
_TmnxRadRouteDownlEntry_Object = MibTableRow
tmnxRadRouteDownlEntry = _TmnxRadRouteDownlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1)
)
tmnxRadRouteDownlEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlName"),
)
if mibBuilder.loadTexts:
    tmnxRadRouteDownlEntry.setStatus("current")
_TmnxRadRouteDownlName_Type = TNamedItem
_TmnxRadRouteDownlName_Object = MibTableColumn
tmnxRadRouteDownlName = _TmnxRadRouteDownlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 1),
    _TmnxRadRouteDownlName_Type()
)
tmnxRadRouteDownlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlName.setStatus("current")
_TmnxRadRouteDownlRowStatus_Type = RowStatus
_TmnxRadRouteDownlRowStatus_Object = MibTableColumn
tmnxRadRouteDownlRowStatus = _TmnxRadRouteDownlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 2),
    _TmnxRadRouteDownlRowStatus_Type()
)
tmnxRadRouteDownlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlRowStatus.setStatus("current")
_TmnxRadRouteDownlLastCh_Type = TimeStamp
_TmnxRadRouteDownlLastCh_Object = MibTableColumn
tmnxRadRouteDownlLastCh = _TmnxRadRouteDownlLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 3),
    _TmnxRadRouteDownlLastCh_Type()
)
tmnxRadRouteDownlLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlLastCh.setStatus("current")


class _TmnxRadRouteDownlDescription_Type(TItemDescription):
    """Custom type tmnxRadRouteDownlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadRouteDownlDescription_Type.__name__ = "TItemDescription"
_TmnxRadRouteDownlDescription_Object = MibTableColumn
tmnxRadRouteDownlDescription = _TmnxRadRouteDownlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 4),
    _TmnxRadRouteDownlDescription_Type()
)
tmnxRadRouteDownlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlDescription.setStatus("current")


class _TmnxRadRouteDownlAdminState_Type(TmnxAdminState):
    """Custom type tmnxRadRouteDownlAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxRadRouteDownlAdminState_Type.__name__ = "TmnxAdminState"
_TmnxRadRouteDownlAdminState_Object = MibTableColumn
tmnxRadRouteDownlAdminState = _TmnxRadRouteDownlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 5),
    _TmnxRadRouteDownlAdminState_Type()
)
tmnxRadRouteDownlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlAdminState.setStatus("current")


class _TmnxRadRouteDownlRadServPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadRouteDownlRadServPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadRouteDownlRadServPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadRouteDownlRadServPlcy_Object = MibTableColumn
tmnxRadRouteDownlRadServPlcy = _TmnxRadRouteDownlRadServPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 6),
    _TmnxRadRouteDownlRadServPlcy_Type()
)
tmnxRadRouteDownlRadServPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlRadServPlcy.setStatus("current")


class _TmnxRadRouteDownlDownloadIntvl_Type(Unsigned32):
    """Custom type tmnxRadRouteDownlDownloadIntvl based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_TmnxRadRouteDownlDownloadIntvl_Type.__name__ = "Unsigned32"
_TmnxRadRouteDownlDownloadIntvl_Object = MibTableColumn
tmnxRadRouteDownlDownloadIntvl = _TmnxRadRouteDownlDownloadIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 7),
    _TmnxRadRouteDownlDownloadIntvl_Type()
)
tmnxRadRouteDownlDownloadIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlDownloadIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlDownloadIntvl.setUnits("minutes")


class _TmnxRadRouteDownlMinRetryIntvl_Type(Unsigned32):
    """Custom type tmnxRadRouteDownlMinRetryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_TmnxRadRouteDownlMinRetryIntvl_Type.__name__ = "Unsigned32"
_TmnxRadRouteDownlMinRetryIntvl_Object = MibTableColumn
tmnxRadRouteDownlMinRetryIntvl = _TmnxRadRouteDownlMinRetryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 8),
    _TmnxRadRouteDownlMinRetryIntvl_Type()
)
tmnxRadRouteDownlMinRetryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlMinRetryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlMinRetryIntvl.setUnits("minutes")


class _TmnxRadRouteDownlMaxRetryIntvl_Type(Unsigned32):
    """Custom type tmnxRadRouteDownlMaxRetryIntvl based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_TmnxRadRouteDownlMaxRetryIntvl_Type.__name__ = "Unsigned32"
_TmnxRadRouteDownlMaxRetryIntvl_Object = MibTableColumn
tmnxRadRouteDownlMaxRetryIntvl = _TmnxRadRouteDownlMaxRetryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 9),
    _TmnxRadRouteDownlMaxRetryIntvl_Type()
)
tmnxRadRouteDownlMaxRetryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlMaxRetryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlMaxRetryIntvl.setUnits("minutes")


class _TmnxRadRouteDownlDefaultMetric_Type(Unsigned32):
    """Custom type tmnxRadRouteDownlDefaultMetric based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TmnxRadRouteDownlDefaultMetric_Type.__name__ = "Unsigned32"
_TmnxRadRouteDownlDefaultMetric_Object = MibTableColumn
tmnxRadRouteDownlDefaultMetric = _TmnxRadRouteDownlDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 10),
    _TmnxRadRouteDownlDefaultMetric_Type()
)
tmnxRadRouteDownlDefaultMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlDefaultMetric.setStatus("current")


class _TmnxRadRouteDownlDefaultTag_Type(Unsigned32):
    """Custom type tmnxRadRouteDownlDefaultTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxRadRouteDownlDefaultTag_Type.__name__ = "Unsigned32"
_TmnxRadRouteDownlDefaultTag_Object = MibTableColumn
tmnxRadRouteDownlDefaultTag = _TmnxRadRouteDownlDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 11),
    _TmnxRadRouteDownlDefaultTag_Type()
)
tmnxRadRouteDownlDefaultTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlDefaultTag.setStatus("current")


class _TmnxRadRouteDownlMaxRoutes_Type(Unsigned32):
    """Custom type tmnxRadRouteDownlMaxRoutes based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000),
    )


_TmnxRadRouteDownlMaxRoutes_Type.__name__ = "Unsigned32"
_TmnxRadRouteDownlMaxRoutes_Object = MibTableColumn
tmnxRadRouteDownlMaxRoutes = _TmnxRadRouteDownlMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 12),
    _TmnxRadRouteDownlMaxRoutes_Type()
)
tmnxRadRouteDownlMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlMaxRoutes.setStatus("current")


class _TmnxRadRouteDownlBaseUserName_Type(TNamedItemOrEmpty):
    """Custom type tmnxRadRouteDownlBaseUserName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRadRouteDownlBaseUserName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRadRouteDownlBaseUserName_Object = MibTableColumn
tmnxRadRouteDownlBaseUserName = _TmnxRadRouteDownlBaseUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 13),
    _TmnxRadRouteDownlBaseUserName_Type()
)
tmnxRadRouteDownlBaseUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlBaseUserName.setStatus("current")


class _TmnxRadRouteDownlPassword_Type(DisplayString):
    """Custom type tmnxRadRouteDownlPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxRadRouteDownlPassword_Type.__name__ = "DisplayString"
_TmnxRadRouteDownlPassword_Object = MibTableColumn
tmnxRadRouteDownlPassword = _TmnxRadRouteDownlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 1, 1, 14),
    _TmnxRadRouteDownlPassword_Type()
)
tmnxRadRouteDownlPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlPassword.setStatus("current")
_TmnxRadRDStatsTable_Object = MibTable
tmnxRadRDStatsTable = _TmnxRadRDStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxRadRDStatsTable.setStatus("current")
_TmnxRadRDStatsEntry_Object = MibTableRow
tmnxRadRDStatsEntry = _TmnxRadRDStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxRadRDStatsEntry.setStatus("current")
_TmnxRadRDStatsRxLastAccessReject_Type = TimeStamp
_TmnxRadRDStatsRxLastAccessReject_Object = MibTableColumn
tmnxRadRDStatsRxLastAccessReject = _TmnxRadRDStatsRxLastAccessReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 1),
    _TmnxRadRDStatsRxLastAccessReject_Type()
)
tmnxRadRDStatsRxLastAccessReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRxLastAccessReject.setStatus("current")
_TmnxRadRDStatsRxLastAccessAccept_Type = TimeStamp
_TmnxRadRDStatsRxLastAccessAccept_Object = MibTableColumn
tmnxRadRDStatsRxLastAccessAccept = _TmnxRadRDStatsRxLastAccessAccept_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 2),
    _TmnxRadRDStatsRxLastAccessAccept_Type()
)
tmnxRadRDStatsRxLastAccessAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRxLastAccessAccept.setStatus("current")
_TmnxRadRDStatsTxLastAccessReq_Type = TimeStamp
_TmnxRadRDStatsTxLastAccessReq_Object = MibTableColumn
tmnxRadRDStatsTxLastAccessReq = _TmnxRadRDStatsTxLastAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 3),
    _TmnxRadRDStatsTxLastAccessReq_Type()
)
tmnxRadRDStatsTxLastAccessReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsTxLastAccessReq.setStatus("current")
_TmnxRadRDStatsTxLastAccReqRetry_Type = TimeStamp
_TmnxRadRDStatsTxLastAccReqRetry_Object = MibTableColumn
tmnxRadRDStatsTxLastAccReqRetry = _TmnxRadRDStatsTxLastAccReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 4),
    _TmnxRadRDStatsTxLastAccReqRetry_Type()
)
tmnxRadRDStatsTxLastAccReqRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsTxLastAccReqRetry.setStatus("current")
_TmnxRadRDStatsRemainingDownlTime_Type = TimeInterval
_TmnxRadRDStatsRemainingDownlTime_Object = MibTableColumn
tmnxRadRDStatsRemainingDownlTime = _TmnxRadRDStatsRemainingDownlTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 5),
    _TmnxRadRDStatsRemainingDownlTime_Type()
)
tmnxRadRDStatsRemainingDownlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRemainingDownlTime.setStatus("current")
_TmnxRadRDStatsRemainingRetryTime_Type = TimeInterval
_TmnxRadRDStatsRemainingRetryTime_Object = MibTableColumn
tmnxRadRDStatsRemainingRetryTime = _TmnxRadRDStatsRemainingRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 6),
    _TmnxRadRDStatsRemainingRetryTime_Type()
)
tmnxRadRDStatsRemainingRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRemainingRetryTime.setStatus("current")
_TmnxRadRDStatsRoutesReceived_Type = Counter32
_TmnxRadRDStatsRoutesReceived_Object = MibTableColumn
tmnxRadRDStatsRoutesReceived = _TmnxRadRDStatsRoutesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 7),
    _TmnxRadRDStatsRoutesReceived_Type()
)
tmnxRadRDStatsRoutesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRoutesReceived.setStatus("current")
_TmnxRadRDStatsRxAccessReject_Type = Counter32
_TmnxRadRDStatsRxAccessReject_Object = MibTableColumn
tmnxRadRDStatsRxAccessReject = _TmnxRadRDStatsRxAccessReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 8),
    _TmnxRadRDStatsRxAccessReject_Type()
)
tmnxRadRDStatsRxAccessReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRxAccessReject.setStatus("current")
_TmnxRadRDStatsRxAccessAccept_Type = Counter32
_TmnxRadRDStatsRxAccessAccept_Object = MibTableColumn
tmnxRadRDStatsRxAccessAccept = _TmnxRadRDStatsRxAccessAccept_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 9),
    _TmnxRadRDStatsRxAccessAccept_Type()
)
tmnxRadRDStatsRxAccessAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRxAccessAccept.setStatus("current")
_TmnxRadRDStatsRxAccessAcceptDrop_Type = Counter32
_TmnxRadRDStatsRxAccessAcceptDrop_Object = MibTableColumn
tmnxRadRDStatsRxAccessAcceptDrop = _TmnxRadRDStatsRxAccessAcceptDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 10),
    _TmnxRadRDStatsRxAccessAcceptDrop_Type()
)
tmnxRadRDStatsRxAccessAcceptDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRxAccessAcceptDrop.setStatus("current")
_TmnxRadRDStatsTxAccessRequest_Type = Counter32
_TmnxRadRDStatsTxAccessRequest_Object = MibTableColumn
tmnxRadRDStatsTxAccessRequest = _TmnxRadRDStatsTxAccessRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 11),
    _TmnxRadRDStatsTxAccessRequest_Type()
)
tmnxRadRDStatsTxAccessRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsTxAccessRequest.setStatus("current")
_TmnxRadRDStatsTxAccessReqRetry_Type = Counter32
_TmnxRadRDStatsTxAccessReqRetry_Object = MibTableColumn
tmnxRadRDStatsTxAccessReqRetry = _TmnxRadRDStatsTxAccessReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 12),
    _TmnxRadRDStatsTxAccessReqRetry_Type()
)
tmnxRadRDStatsTxAccessReqRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsTxAccessReqRetry.setStatus("current")
_TmnxRadRDStatsDownloads_Type = Counter32
_TmnxRadRDStatsDownloads_Object = MibTableColumn
tmnxRadRDStatsDownloads = _TmnxRadRDStatsDownloads_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 13),
    _TmnxRadRDStatsDownloads_Type()
)
tmnxRadRDStatsDownloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsDownloads.setStatus("current")
_TmnxRadRDStatsRtmFailures_Type = Counter32
_TmnxRadRDStatsRtmFailures_Object = MibTableColumn
tmnxRadRDStatsRtmFailures = _TmnxRadRDStatsRtmFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 4, 2, 1, 14),
    _TmnxRadRDStatsRtmFailures_Type()
)
tmnxRadRDStatsRtmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRDStatsRtmFailures.setStatus("current")
_TmnxRadSysCfgObjs_ObjectIdentity = ObjectIdentity
tmnxRadSysCfgObjs = _TmnxRadSysCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 5)
)


class _TmnxRadSysCfgCoAPort_Type(InetPortNumber):
    """Custom type tmnxRadSysCfgCoAPort based on InetPortNumber"""
    defaultValue = 3799

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1647, 1647),
        ValueRangeConstraint(1700, 1700),
        ValueRangeConstraint(1812, 1812),
        ValueRangeConstraint(3799, 3799),
    )


_TmnxRadSysCfgCoAPort_Type.__name__ = "InetPortNumber"
_TmnxRadSysCfgCoAPort_Object = MibScalar
tmnxRadSysCfgCoAPort = _TmnxRadSysCfgCoAPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 5, 1),
    _TmnxRadSysCfgCoAPort_Type()
)
tmnxRadSysCfgCoAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRadSysCfgCoAPort.setStatus("current")
_TmnxRadIsaObjs_ObjectIdentity = ObjectIdentity
tmnxRadIsaObjs = _TmnxRadIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6)
)
_TmnxRadIsaPlcyTable_Object = MibTable
tmnxRadIsaPlcyTable = _TmnxRadIsaPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyTable.setStatus("current")
_TmnxRadIsaPlcyEntry_Object = MibTableRow
tmnxRadIsaPlcyEntry = _TmnxRadIsaPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1)
)
tmnxRadIsaPlcyEntry.setIndexNames(
    (1, "TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyEntry.setStatus("current")
_TmnxRadIsaPlcyName_Type = TNamedItem
_TmnxRadIsaPlcyName_Object = MibTableColumn
tmnxRadIsaPlcyName = _TmnxRadIsaPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 1),
    _TmnxRadIsaPlcyName_Type()
)
tmnxRadIsaPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyName.setStatus("current")
_TmnxRadIsaPlcyRowStatus_Type = RowStatus
_TmnxRadIsaPlcyRowStatus_Object = MibTableColumn
tmnxRadIsaPlcyRowStatus = _TmnxRadIsaPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 2),
    _TmnxRadIsaPlcyRowStatus_Type()
)
tmnxRadIsaPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyRowStatus.setStatus("current")
_TmnxRadIsaPlcyLastCh_Type = TimeStamp
_TmnxRadIsaPlcyLastCh_Object = MibTableColumn
tmnxRadIsaPlcyLastCh = _TmnxRadIsaPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 3),
    _TmnxRadIsaPlcyLastCh_Type()
)
tmnxRadIsaPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyLastCh.setStatus("current")


class _TmnxRadIsaPlcyDescription_Type(TItemDescription):
    """Custom type tmnxRadIsaPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRadIsaPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxRadIsaPlcyDescription_Object = MibTableColumn
tmnxRadIsaPlcyDescription = _TmnxRadIsaPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 4),
    _TmnxRadIsaPlcyDescription_Type()
)
tmnxRadIsaPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyDescription.setStatus("current")


class _TmnxRadIsaPlcyPassword_Type(TmnxAuthPassword):
    """Custom type tmnxRadIsaPlcyPassword based on TmnxAuthPassword"""
    defaultValue = OctetString("")

    subtypeSpec = TmnxAuthPassword.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TmnxRadIsaPlcyPassword_Type.__name__ = "TmnxAuthPassword"
_TmnxRadIsaPlcyPassword_Object = MibTableColumn
tmnxRadIsaPlcyPassword = _TmnxRadIsaPlcyPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 5),
    _TmnxRadIsaPlcyPassword_Type()
)
tmnxRadIsaPlcyPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyPassword.setStatus("current")


class _TmnxRadIsaPlcyAuthInclAttr_Type(Bits):
    """Custom type tmnxRadIsaPlcyAuthInclAttr based on Bits"""
    defaultBinValue = "0000000000001"

    namedValues = NamedValues(
        *(("circuitId", 0),
          ("remoteId", 1),
          ("nasPortId", 2),
          ("nasIdentifier", 3),
          ("dhcpVendorClassId", 4),
          ("macAddress", 5),
          ("callingStationId", 6),
          ("calledStationId", 7),
          ("dhcpOptions", 8),
          ("nasPortType", 9),
          ("wifiSsidVlan", 10),
          ("framedIpAddr", 11),
          ("nasIpAddress", 12),
          ("nasPort", 13))
    )

_TmnxRadIsaPlcyAuthInclAttr_Type.__name__ = "Bits"
_TmnxRadIsaPlcyAuthInclAttr_Object = MibTableColumn
tmnxRadIsaPlcyAuthInclAttr = _TmnxRadIsaPlcyAuthInclAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 6),
    _TmnxRadIsaPlcyAuthInclAttr_Type()
)
tmnxRadIsaPlcyAuthInclAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyAuthInclAttr.setStatus("current")


class _TmnxRadIsaPlcyAcctInclAttr_Type(Bits):
    """Custom type tmnxRadIsaPlcyAcctInclAttr based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("framedIpAddr", 0),
          ("nasIdentifier", 1),
          ("natSubscriberString", 2),
          ("userName", 3),
          ("insideServiceId", 4),
          ("outsideServiceId", 5),
          ("outsideIp", 6),
          ("portRangeBlock", 7),
          ("hardwareTimestamp", 8),
          ("releaseReason", 9),
          ("multiSessionId", 10),
          ("frameCounters", 11),
          ("octetCounters", 12),
          ("sessionTime", 13),
          ("calledStationId", 14),
          ("subscriberData", 15),
          ("framedIpNetmask", 16),
          ("circuitId", 17),
          ("remoteId", 18),
          ("dhcpOptions", 19),
          ("dhcpVendorClassId", 20),
          ("macAddress", 21),
          ("nasPortId", 22),
          ("nasPortType", 23),
          ("callingStationId", 24),
          ("subscriberId", 25),
          ("acctTriggerReason", 26),
          ("ueCreationType", 27),
          ("wifiRssi", 28),
          ("acctDelayTime", 29),
          ("wifiSsidVlan", 30),
          ("nasIpAddress", 31),
          ("nasPort", 32),
          ("class", 33))
    )

_TmnxRadIsaPlcyAcctInclAttr_Type.__name__ = "Bits"
_TmnxRadIsaPlcyAcctInclAttr_Object = MibTableColumn
tmnxRadIsaPlcyAcctInclAttr = _TmnxRadIsaPlcyAcctInclAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 7),
    _TmnxRadIsaPlcyAcctInclAttr_Type()
)
tmnxRadIsaPlcyAcctInclAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyAcctInclAttr.setStatus("current")


class _TmnxRadIsaPlcyUserNameFormat_Type(Integer32):
    """Custom type tmnxRadIsaPlcyUserNameFormat based on Integer32"""
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
        *(("mac", 1),
          ("macIp", 2),
          ("dhcpVendor", 3),
          ("circuitId", 4))
    )


_TmnxRadIsaPlcyUserNameFormat_Type.__name__ = "Integer32"
_TmnxRadIsaPlcyUserNameFormat_Object = MibTableColumn
tmnxRadIsaPlcyUserNameFormat = _TmnxRadIsaPlcyUserNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 8),
    _TmnxRadIsaPlcyUserNameFormat_Type()
)
tmnxRadIsaPlcyUserNameFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyUserNameFormat.setStatus("current")


class _TmnxRadIsaPlcyUserNameMacFormat_Type(Integer32):
    """Custom type tmnxRadIsaPlcyUserNameMacFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alu", 1),
          ("ieee", 2))
    )


_TmnxRadIsaPlcyUserNameMacFormat_Type.__name__ = "Integer32"
_TmnxRadIsaPlcyUserNameMacFormat_Object = MibTableColumn
tmnxRadIsaPlcyUserNameMacFormat = _TmnxRadIsaPlcyUserNameMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 9),
    _TmnxRadIsaPlcyUserNameMacFormat_Type()
)
tmnxRadIsaPlcyUserNameMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyUserNameMacFormat.setStatus("current")


class _TmnxRadIsaPlcyNasIpAddressOrigin_Type(Integer32):
    """Custom type tmnxRadIsaPlcyNasIpAddressOrigin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("systemIp", 0),
          ("isaIp", 1))
    )


_TmnxRadIsaPlcyNasIpAddressOrigin_Type.__name__ = "Integer32"
_TmnxRadIsaPlcyNasIpAddressOrigin_Object = MibTableColumn
tmnxRadIsaPlcyNasIpAddressOrigin = _TmnxRadIsaPlcyNasIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 10),
    _TmnxRadIsaPlcyNasIpAddressOrigin_Type()
)
tmnxRadIsaPlcyNasIpAddressOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyNasIpAddressOrigin.setStatus("current")


class _TmnxRadIsaPlcySrvTimeout_Type(Unsigned32):
    """Custom type tmnxRadIsaPlcySrvTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxRadIsaPlcySrvTimeout_Type.__name__ = "Unsigned32"
_TmnxRadIsaPlcySrvTimeout_Object = MibTableColumn
tmnxRadIsaPlcySrvTimeout = _TmnxRadIsaPlcySrvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 100),
    _TmnxRadIsaPlcySrvTimeout_Type()
)
tmnxRadIsaPlcySrvTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvTimeout.setUnits("seconds")


class _TmnxRadIsaPlcySrvRetry_Type(Unsigned32):
    """Custom type tmnxRadIsaPlcySrvRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxRadIsaPlcySrvRetry_Type.__name__ = "Unsigned32"
_TmnxRadIsaPlcySrvRetry_Object = MibTableColumn
tmnxRadIsaPlcySrvRetry = _TmnxRadIsaPlcySrvRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 101),
    _TmnxRadIsaPlcySrvRetry_Type()
)
tmnxRadIsaPlcySrvRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvRetry.setStatus("current")


class _TmnxRadIsaPlcySrvVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxRadIsaPlcySrvVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxRadIsaPlcySrvVRtrID_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxRadIsaPlcySrvVRtrID_Object = MibTableColumn
tmnxRadIsaPlcySrvVRtrID = _TmnxRadIsaPlcySrvVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 102),
    _TmnxRadIsaPlcySrvVRtrID_Type()
)
tmnxRadIsaPlcySrvVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvVRtrID.setStatus("current")


class _TmnxRadIsaPlcySrvSrcAddrType_Type(InetAddressType):
    """Custom type tmnxRadIsaPlcySrvSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxRadIsaPlcySrvSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxRadIsaPlcySrvSrcAddrType_Object = MibTableColumn
tmnxRadIsaPlcySrvSrcAddrType = _TmnxRadIsaPlcySrvSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 103),
    _TmnxRadIsaPlcySrvSrcAddrType_Type()
)
tmnxRadIsaPlcySrvSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvSrcAddrType.setStatus("current")


class _TmnxRadIsaPlcySrvSrcAddrStart_Type(InetAddress):
    """Custom type tmnxRadIsaPlcySrvSrcAddrStart based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadIsaPlcySrvSrcAddrStart_Type.__name__ = "InetAddress"
_TmnxRadIsaPlcySrvSrcAddrStart_Object = MibTableColumn
tmnxRadIsaPlcySrvSrcAddrStart = _TmnxRadIsaPlcySrvSrcAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 104),
    _TmnxRadIsaPlcySrvSrcAddrStart_Type()
)
tmnxRadIsaPlcySrvSrcAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvSrcAddrStart.setStatus("current")


class _TmnxRadIsaPlcySrvSrcAddrEnd_Type(InetAddress):
    """Custom type tmnxRadIsaPlcySrvSrcAddrEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadIsaPlcySrvSrcAddrEnd_Type.__name__ = "InetAddress"
_TmnxRadIsaPlcySrvSrcAddrEnd_Object = MibTableColumn
tmnxRadIsaPlcySrvSrcAddrEnd = _TmnxRadIsaPlcySrvSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 105),
    _TmnxRadIsaPlcySrvSrcAddrEnd_Type()
)
tmnxRadIsaPlcySrvSrcAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvSrcAddrEnd.setStatus("current")


class _TmnxRadIsaPlcySrvAlgorithm_Type(TmnxSubRadServAlgorithm):
    """Custom type tmnxRadIsaPlcySrvAlgorithm based on TmnxSubRadServAlgorithm"""
    defaultValue = 1


_TmnxRadIsaPlcySrvAlgorithm_Type.__name__ = "TmnxSubRadServAlgorithm"
_TmnxRadIsaPlcySrvAlgorithm_Object = MibTableColumn
tmnxRadIsaPlcySrvAlgorithm = _TmnxRadIsaPlcySrvAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 1, 1, 106),
    _TmnxRadIsaPlcySrvAlgorithm_Type()
)
tmnxRadIsaPlcySrvAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcySrvAlgorithm.setStatus("current")
_TmnxRadIsaSrvTable_Object = MibTable
tmnxRadIsaSrvTable = _TmnxRadIsaSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxRadIsaSrvTable.setStatus("current")
_TmnxRadIsaSrvEntry_Object = MibTableRow
tmnxRadIsaSrvEntry = _TmnxRadIsaSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1)
)
tmnxRadIsaSrvEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvIndex"),
)
if mibBuilder.loadTexts:
    tmnxRadIsaSrvEntry.setStatus("current")


class _TmnxRadIsaSrvIndex_Type(Unsigned32):
    """Custom type tmnxRadIsaSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxRadIsaSrvIndex_Type.__name__ = "Unsigned32"
_TmnxRadIsaSrvIndex_Object = MibTableColumn
tmnxRadIsaSrvIndex = _TmnxRadIsaSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 1),
    _TmnxRadIsaSrvIndex_Type()
)
tmnxRadIsaSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvIndex.setStatus("current")
_TmnxRadIsaSrvRowStatus_Type = RowStatus
_TmnxRadIsaSrvRowStatus_Object = MibTableColumn
tmnxRadIsaSrvRowStatus = _TmnxRadIsaSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 2),
    _TmnxRadIsaSrvRowStatus_Type()
)
tmnxRadIsaSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvRowStatus.setStatus("current")
_TmnxRadIsaSrvLastMgmtChange_Type = TimeStamp
_TmnxRadIsaSrvLastMgmtChange_Object = MibTableColumn
tmnxRadIsaSrvLastMgmtChange = _TmnxRadIsaSrvLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 3),
    _TmnxRadIsaSrvLastMgmtChange_Type()
)
tmnxRadIsaSrvLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvLastMgmtChange.setStatus("current")


class _TmnxRadIsaSrvAdminState_Type(TmnxEnabledDisabled):
    """Custom type tmnxRadIsaSrvAdminState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxRadIsaSrvAdminState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxRadIsaSrvAdminState_Object = MibTableColumn
tmnxRadIsaSrvAdminState = _TmnxRadIsaSrvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 4),
    _TmnxRadIsaSrvAdminState_Type()
)
tmnxRadIsaSrvAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvAdminState.setStatus("current")


class _TmnxRadIsaSrvAddrType_Type(InetAddressType):
    """Custom type tmnxRadIsaSrvAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxRadIsaSrvAddrType_Type.__name__ = "InetAddressType"
_TmnxRadIsaSrvAddrType_Object = MibTableColumn
tmnxRadIsaSrvAddrType = _TmnxRadIsaSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 5),
    _TmnxRadIsaSrvAddrType_Type()
)
tmnxRadIsaSrvAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvAddrType.setStatus("current")


class _TmnxRadIsaSrvAddr_Type(InetAddress):
    """Custom type tmnxRadIsaSrvAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadIsaSrvAddr_Type.__name__ = "InetAddress"
_TmnxRadIsaSrvAddr_Object = MibTableColumn
tmnxRadIsaSrvAddr = _TmnxRadIsaSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 6),
    _TmnxRadIsaSrvAddr_Type()
)
tmnxRadIsaSrvAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvAddr.setStatus("current")
_TmnxRadIsaSrvSecret_Type = TmnxAuthSecret
_TmnxRadIsaSrvSecret_Object = MibTableColumn
tmnxRadIsaSrvSecret = _TmnxRadIsaSrvSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 7),
    _TmnxRadIsaSrvSecret_Type()
)
tmnxRadIsaSrvSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvSecret.setStatus("current")


class _TmnxRadIsaSrvPurpose_Type(Bits):
    """Custom type tmnxRadIsaSrvPurpose based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("accounting", 0),
          ("authentication", 1),
          ("coa", 2))
    )

_TmnxRadIsaSrvPurpose_Type.__name__ = "Bits"
_TmnxRadIsaSrvPurpose_Object = MibTableColumn
tmnxRadIsaSrvPurpose = _TmnxRadIsaSrvPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 8),
    _TmnxRadIsaSrvPurpose_Type()
)
tmnxRadIsaSrvPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvPurpose.setStatus("current")


class _TmnxRadIsaSrvAcctPort_Type(Unsigned32):
    """Custom type tmnxRadIsaSrvAcctPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadIsaSrvAcctPort_Type.__name__ = "Unsigned32"
_TmnxRadIsaSrvAcctPort_Object = MibTableColumn
tmnxRadIsaSrvAcctPort = _TmnxRadIsaSrvAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 9),
    _TmnxRadIsaSrvAcctPort_Type()
)
tmnxRadIsaSrvAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvAcctPort.setStatus("current")


class _TmnxRadIsaSrvAuthPort_Type(Unsigned32):
    """Custom type tmnxRadIsaSrvAuthPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadIsaSrvAuthPort_Type.__name__ = "Unsigned32"
_TmnxRadIsaSrvAuthPort_Object = MibTableColumn
tmnxRadIsaSrvAuthPort = _TmnxRadIsaSrvAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 10),
    _TmnxRadIsaSrvAuthPort_Type()
)
tmnxRadIsaSrvAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvAuthPort.setStatus("current")


class _TmnxRadIsaSrvCoaPort_Type(Unsigned32):
    """Custom type tmnxRadIsaSrvCoaPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_TmnxRadIsaSrvCoaPort_Type.__name__ = "Unsigned32"
_TmnxRadIsaSrvCoaPort_Object = MibTableColumn
tmnxRadIsaSrvCoaPort = _TmnxRadIsaSrvCoaPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 2, 1, 11),
    _TmnxRadIsaSrvCoaPort_Type()
)
tmnxRadIsaSrvCoaPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvCoaPort.setStatus("current")
_TmnxRadIsaSrvStatTable_Object = MibTable
tmnxRadIsaSrvStatTable = _TmnxRadIsaSrvStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatTable.setStatus("current")
_TmnxRadIsaSrvStatEntry_Object = MibTableRow
tmnxRadIsaSrvStatEntry = _TmnxRadIsaSrvStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3, 1)
)
tmnxRadIsaSrvStatEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvIndex"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatGrpId"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatMemberId"),
)
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatEntry.setStatus("current")
_TmnxRadIsaSrvStatGrpId_Type = Unsigned32
_TmnxRadIsaSrvStatGrpId_Object = MibTableColumn
tmnxRadIsaSrvStatGrpId = _TmnxRadIsaSrvStatGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3, 1, 1),
    _TmnxRadIsaSrvStatGrpId_Type()
)
tmnxRadIsaSrvStatGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatGrpId.setStatus("current")
_TmnxRadIsaSrvStatMemberId_Type = Unsigned32
_TmnxRadIsaSrvStatMemberId_Object = MibTableColumn
tmnxRadIsaSrvStatMemberId = _TmnxRadIsaSrvStatMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3, 1, 2),
    _TmnxRadIsaSrvStatMemberId_Type()
)
tmnxRadIsaSrvStatMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatMemberId.setStatus("current")
_TmnxRadIsaSrvStatSrcAddrType_Type = InetAddressType
_TmnxRadIsaSrvStatSrcAddrType_Object = MibTableColumn
tmnxRadIsaSrvStatSrcAddrType = _TmnxRadIsaSrvStatSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3, 1, 3),
    _TmnxRadIsaSrvStatSrcAddrType_Type()
)
tmnxRadIsaSrvStatSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatSrcAddrType.setStatus("current")


class _TmnxRadIsaSrvStatSrcAddr_Type(InetAddress):
    """Custom type tmnxRadIsaSrvStatSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadIsaSrvStatSrcAddr_Type.__name__ = "InetAddress"
_TmnxRadIsaSrvStatSrcAddr_Object = MibTableColumn
tmnxRadIsaSrvStatSrcAddr = _TmnxRadIsaSrvStatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3, 1, 4),
    _TmnxRadIsaSrvStatSrcAddr_Type()
)
tmnxRadIsaSrvStatSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatSrcAddr.setStatus("current")


class _TmnxRadIsaSrvStatPurposeUp_Type(Bits):
    """Custom type tmnxRadIsaSrvStatPurposeUp based on Bits"""
    namedValues = NamedValues(
        *(("accounting", 0),
          ("authentication", 1),
          ("coa", 2))
    )

_TmnxRadIsaSrvStatPurposeUp_Type.__name__ = "Bits"
_TmnxRadIsaSrvStatPurposeUp_Object = MibTableColumn
tmnxRadIsaSrvStatPurposeUp = _TmnxRadIsaSrvStatPurposeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 3, 1, 9),
    _TmnxRadIsaSrvStatPurposeUp_Type()
)
tmnxRadIsaSrvStatPurposeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatPurposeUp.setStatus("current")
_TmnxRadIsaSrvStatsTable_Object = MibTable
tmnxRadIsaSrvStatsTable = _TmnxRadIsaSrvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatsTable.setStatus("current")
_TmnxRadIsaSrvStatsEntry_Object = MibTableRow
tmnxRadIsaSrvStatsEntry = _TmnxRadIsaSrvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 4, 1)
)
tmnxRadIsaSrvStatsEntry.setIndexNames(
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvIndex"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatGrpId"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatMemberId"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatsType"),
)
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatsEntry.setStatus("current")


class _TmnxRadIsaSrvStatsType_Type(Unsigned32):
    """Custom type tmnxRadIsaSrvStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_TmnxRadIsaSrvStatsType_Type.__name__ = "Unsigned32"
_TmnxRadIsaSrvStatsType_Object = MibTableColumn
tmnxRadIsaSrvStatsType = _TmnxRadIsaSrvStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 4, 1, 1),
    _TmnxRadIsaSrvStatsType_Type()
)
tmnxRadIsaSrvStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatsType.setStatus("current")


class _TmnxRadIsaSrvStatsName_Type(DisplayString):
    """Custom type tmnxRadIsaSrvStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxRadIsaSrvStatsName_Type.__name__ = "DisplayString"
_TmnxRadIsaSrvStatsName_Object = MibTableColumn
tmnxRadIsaSrvStatsName = _TmnxRadIsaSrvStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 4, 1, 2),
    _TmnxRadIsaSrvStatsName_Type()
)
tmnxRadIsaSrvStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatsName.setStatus("current")
_TmnxRadIsaSrvStatsValue_Type = Counter32
_TmnxRadIsaSrvStatsValue_Object = MibTableColumn
tmnxRadIsaSrvStatsValue = _TmnxRadIsaSrvStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 4, 1, 3),
    _TmnxRadIsaSrvStatsValue_Type()
)
tmnxRadIsaSrvStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvStatsValue.setStatus("current")
_TmnxRadIsaPSStatsTable_Object = MibTable
tmnxRadIsaPSStatsTable = _TmnxRadIsaPSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTable.setStatus("current")
_TmnxRadIsaPSStatsEntry_Object = MibTableRow
tmnxRadIsaPSStatsEntry = _TmnxRadIsaPSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1)
)
tmnxRadIsaPSStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadProxSrvName"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatGrpId"),
    (0, "TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatMemberId"),
)
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsEntry.setStatus("current")
_TmnxRadIsaPSStatsRxPacket_Type = Counter32
_TmnxRadIsaPSStatsRxPacket_Object = MibTableColumn
tmnxRadIsaPSStatsRxPacket = _TmnxRadIsaPSStatsRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 1),
    _TmnxRadIsaPSStatsRxPacket_Type()
)
tmnxRadIsaPSStatsRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxPacket.setStatus("current")
_TmnxRadIsaPSStatsRxAuthRequest_Type = Counter32
_TmnxRadIsaPSStatsRxAuthRequest_Object = MibTableColumn
tmnxRadIsaPSStatsRxAuthRequest = _TmnxRadIsaPSStatsRxAuthRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 2),
    _TmnxRadIsaPSStatsRxAuthRequest_Type()
)
tmnxRadIsaPSStatsRxAuthRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxAuthRequest.setStatus("current")
_TmnxRadIsaPSStatsRxAcctRequest_Type = Counter32
_TmnxRadIsaPSStatsRxAcctRequest_Object = MibTableColumn
tmnxRadIsaPSStatsRxAcctRequest = _TmnxRadIsaPSStatsRxAcctRequest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 3),
    _TmnxRadIsaPSStatsRxAcctRequest_Type()
)
tmnxRadIsaPSStatsRxAcctRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxAcctRequest.setStatus("current")
_TmnxRadIsaPSStatsRxDropped_Type = Counter32
_TmnxRadIsaPSStatsRxDropped_Object = MibTableColumn
tmnxRadIsaPSStatsRxDropped = _TmnxRadIsaPSStatsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 4),
    _TmnxRadIsaPSStatsRxDropped_Type()
)
tmnxRadIsaPSStatsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxDropped.setStatus("current")
_TmnxRadIsaPSStatsRxRetransmit_Type = Counter32
_TmnxRadIsaPSStatsRxRetransmit_Object = MibTableColumn
tmnxRadIsaPSStatsRxRetransmit = _TmnxRadIsaPSStatsRxRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 5),
    _TmnxRadIsaPSStatsRxRetransmit_Type()
)
tmnxRadIsaPSStatsRxRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxRetransmit.setStatus("current")
_TmnxRadIsaPSStatsRxWrongPurpose_Type = Counter32
_TmnxRadIsaPSStatsRxWrongPurpose_Object = MibTableColumn
tmnxRadIsaPSStatsRxWrongPurpose = _TmnxRadIsaPSStatsRxWrongPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 6),
    _TmnxRadIsaPSStatsRxWrongPurpose_Type()
)
tmnxRadIsaPSStatsRxWrongPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxWrongPurpose.setStatus("current")
_TmnxRadIsaPSStatsRxCacheNoUeMac_Type = Counter32
_TmnxRadIsaPSStatsRxCacheNoUeMac_Object = MibTableColumn
tmnxRadIsaPSStatsRxCacheNoUeMac = _TmnxRadIsaPSStatsRxCacheNoUeMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 7),
    _TmnxRadIsaPSStatsRxCacheNoUeMac_Type()
)
tmnxRadIsaPSStatsRxCacheNoUeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxCacheNoUeMac.setStatus("current")
_TmnxRadIsaPSStatsRxClientCtxtLim_Type = Counter32
_TmnxRadIsaPSStatsRxClientCtxtLim_Object = MibTableColumn
tmnxRadIsaPSStatsRxClientCtxtLim = _TmnxRadIsaPSStatsRxClientCtxtLim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 8),
    _TmnxRadIsaPSStatsRxClientCtxtLim_Type()
)
tmnxRadIsaPSStatsRxClientCtxtLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxClientCtxtLim.setStatus("current")
_TmnxRadIsaPSStatsRxNoAaaPol_Type = Counter32
_TmnxRadIsaPSStatsRxNoAaaPol_Object = MibTableColumn
tmnxRadIsaPSStatsRxNoAaaPol = _TmnxRadIsaPSStatsRxNoAaaPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 9),
    _TmnxRadIsaPSStatsRxNoAaaPol_Type()
)
tmnxRadIsaPSStatsRxNoAaaPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxNoAaaPol.setStatus("current")
_TmnxRadIsaPSStatsRxInvAttr_Type = Counter32
_TmnxRadIsaPSStatsRxInvAttr_Object = MibTableColumn
tmnxRadIsaPSStatsRxInvAttr = _TmnxRadIsaPSStatsRxInvAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 10),
    _TmnxRadIsaPSStatsRxInvAttr_Type()
)
tmnxRadIsaPSStatsRxInvAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxInvAttr.setStatus("current")
_TmnxRadIsaPSStatsRxInvPassword_Type = Counter32
_TmnxRadIsaPSStatsRxInvPassword_Object = MibTableColumn
tmnxRadIsaPSStatsRxInvPassword = _TmnxRadIsaPSStatsRxInvPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 11),
    _TmnxRadIsaPSStatsRxInvPassword_Type()
)
tmnxRadIsaPSStatsRxInvPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxInvPassword.setStatus("current")
_TmnxRadIsaPSStatsRxInvAcctStatus_Type = Counter32
_TmnxRadIsaPSStatsRxInvAcctStatus_Object = MibTableColumn
tmnxRadIsaPSStatsRxInvAcctStatus = _TmnxRadIsaPSStatsRxInvAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 12),
    _TmnxRadIsaPSStatsRxInvAcctStatus_Type()
)
tmnxRadIsaPSStatsRxInvAcctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxInvAcctStatus.setStatus("current")
_TmnxRadIsaPSStatsRxNoAcctStatus_Type = Counter32
_TmnxRadIsaPSStatsRxNoAcctStatus_Object = MibTableColumn
tmnxRadIsaPSStatsRxNoAcctStatus = _TmnxRadIsaPSStatsRxNoAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 13),
    _TmnxRadIsaPSStatsRxNoAcctStatus_Type()
)
tmnxRadIsaPSStatsRxNoAcctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxNoAcctStatus.setStatus("current")
_TmnxRadIsaPSStatsRxInvAcctAuth_Type = Counter32
_TmnxRadIsaPSStatsRxInvAcctAuth_Object = MibTableColumn
tmnxRadIsaPSStatsRxInvAcctAuth = _TmnxRadIsaPSStatsRxInvAcctAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 14),
    _TmnxRadIsaPSStatsRxInvAcctAuth_Type()
)
tmnxRadIsaPSStatsRxInvAcctAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxInvAcctAuth.setStatus("current")
_TmnxRadIsaPSStatsRxInvMsgAuth_Type = Counter32
_TmnxRadIsaPSStatsRxInvMsgAuth_Object = MibTableColumn
tmnxRadIsaPSStatsRxInvMsgAuth = _TmnxRadIsaPSStatsRxInvMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 15),
    _TmnxRadIsaPSStatsRxInvMsgAuth_Type()
)
tmnxRadIsaPSStatsRxInvMsgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxInvMsgAuth.setStatus("current")
_TmnxRadIsaPSStatsRxMgmtOverload_Type = Counter32
_TmnxRadIsaPSStatsRxMgmtOverload_Object = MibTableColumn
tmnxRadIsaPSStatsRxMgmtOverload = _TmnxRadIsaPSStatsRxMgmtOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 16),
    _TmnxRadIsaPSStatsRxMgmtOverload_Type()
)
tmnxRadIsaPSStatsRxMgmtOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsRxMgmtOverload.setStatus("current")
_TmnxRadIsaPSStatsTxAuthAck_Type = Counter32
_TmnxRadIsaPSStatsTxAuthAck_Object = MibTableColumn
tmnxRadIsaPSStatsTxAuthAck = _TmnxRadIsaPSStatsTxAuthAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 17),
    _TmnxRadIsaPSStatsTxAuthAck_Type()
)
tmnxRadIsaPSStatsTxAuthAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxAuthAck.setStatus("current")
_TmnxRadIsaPSStatsTxAuthReject_Type = Counter32
_TmnxRadIsaPSStatsTxAuthReject_Object = MibTableColumn
tmnxRadIsaPSStatsTxAuthReject = _TmnxRadIsaPSStatsTxAuthReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 18),
    _TmnxRadIsaPSStatsTxAuthReject_Type()
)
tmnxRadIsaPSStatsTxAuthReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxAuthReject.setStatus("current")
_TmnxRadIsaPSStatsTxAuthChallenge_Type = Counter32
_TmnxRadIsaPSStatsTxAuthChallenge_Object = MibTableColumn
tmnxRadIsaPSStatsTxAuthChallenge = _TmnxRadIsaPSStatsTxAuthChallenge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 19),
    _TmnxRadIsaPSStatsTxAuthChallenge_Type()
)
tmnxRadIsaPSStatsTxAuthChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxAuthChallenge.setStatus("current")
_TmnxRadIsaPSStatsTxAcctResponse_Type = Counter32
_TmnxRadIsaPSStatsTxAcctResponse_Object = MibTableColumn
tmnxRadIsaPSStatsTxAcctResponse = _TmnxRadIsaPSStatsTxAcctResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 20),
    _TmnxRadIsaPSStatsTxAcctResponse_Type()
)
tmnxRadIsaPSStatsTxAcctResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxAcctResponse.setStatus("current")
_TmnxRadIsaPSStatsTxDropped_Type = Counter32
_TmnxRadIsaPSStatsTxDropped_Object = MibTableColumn
tmnxRadIsaPSStatsTxDropped = _TmnxRadIsaPSStatsTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 21),
    _TmnxRadIsaPSStatsTxDropped_Type()
)
tmnxRadIsaPSStatsTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxDropped.setStatus("current")
_TmnxRadIsaPSStatsTxSrvTimeout_Type = Counter32
_TmnxRadIsaPSStatsTxSrvTimeout_Object = MibTableColumn
tmnxRadIsaPSStatsTxSrvTimeout = _TmnxRadIsaPSStatsTxSrvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 22),
    _TmnxRadIsaPSStatsTxSrvTimeout_Type()
)
tmnxRadIsaPSStatsTxSrvTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxSrvTimeout.setStatus("current")
_TmnxRadIsaPSStatsTxSrvInvAuth_Type = Counter32
_TmnxRadIsaPSStatsTxSrvInvAuth_Object = MibTableColumn
tmnxRadIsaPSStatsTxSrvInvAuth = _TmnxRadIsaPSStatsTxSrvInvAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 23),
    _TmnxRadIsaPSStatsTxSrvInvAuth_Type()
)
tmnxRadIsaPSStatsTxSrvInvAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxSrvInvAuth.setStatus("current")
_TmnxRadIsaPSStatsTxSrvInvMsgAuth_Type = Counter32
_TmnxRadIsaPSStatsTxSrvInvMsgAuth_Object = MibTableColumn
tmnxRadIsaPSStatsTxSrvInvMsgAuth = _TmnxRadIsaPSStatsTxSrvInvMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 24),
    _TmnxRadIsaPSStatsTxSrvInvMsgAuth_Type()
)
tmnxRadIsaPSStatsTxSrvInvMsgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxSrvInvMsgAuth.setStatus("current")
_TmnxRadIsaPSStatsTxSrvInvAttr_Type = Counter32
_TmnxRadIsaPSStatsTxSrvInvAttr_Object = MibTableColumn
tmnxRadIsaPSStatsTxSrvInvAttr = _TmnxRadIsaPSStatsTxSrvInvAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 25),
    _TmnxRadIsaPSStatsTxSrvInvAttr_Type()
)
tmnxRadIsaPSStatsTxSrvInvAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxSrvInvAttr.setStatus("current")
_TmnxRadIsaPSStatsTxSendFailure_Type = Counter32
_TmnxRadIsaPSStatsTxSendFailure_Object = MibTableColumn
tmnxRadIsaPSStatsTxSendFailure = _TmnxRadIsaPSStatsTxSendFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 6, 5, 1, 26),
    _TmnxRadIsaPSStatsTxSendFailure_Type()
)
tmnxRadIsaPSStatsTxSendFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPSStatsTxSendFailure.setStatus("current")
_TmnxRadProxSrvTableCh_Type = TimeStamp
_TmnxRadProxSrvTableCh_Object = MibScalar
tmnxRadProxSrvTableCh = _TmnxRadProxSrvTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 100),
    _TmnxRadProxSrvTableCh_Type()
)
tmnxRadProxSrvTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvTableCh.setStatus("current")
_TmnxRadProxSrvIfTableCh_Type = TimeStamp
_TmnxRadProxSrvIfTableCh_Object = MibScalar
tmnxRadProxSrvIfTableCh = _TmnxRadProxSrvIfTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 101),
    _TmnxRadProxSrvIfTableCh_Type()
)
tmnxRadProxSrvIfTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxSrvIfTableCh.setStatus("current")
_TmnxRadProxUsrToRspTableCh_Type = TimeStamp
_TmnxRadProxUsrToRspTableCh_Object = MibScalar
tmnxRadProxUsrToRspTableCh = _TmnxRadProxUsrToRspTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 102),
    _TmnxRadProxUsrToRspTableCh_Type()
)
tmnxRadProxUsrToRspTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadProxUsrToRspTableCh.setStatus("current")
_TmnxRadServTableCh_Type = TimeStamp
_TmnxRadServTableCh_Object = MibScalar
tmnxRadServTableCh = _TmnxRadServTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 120),
    _TmnxRadServTableCh_Type()
)
tmnxRadServTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadServTableCh.setStatus("current")
_TmnxRadSrvPlcyTableCh_Type = TimeStamp
_TmnxRadSrvPlcyTableCh_Object = MibScalar
tmnxRadSrvPlcyTableCh = _TmnxRadSrvPlcyTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 121),
    _TmnxRadSrvPlcyTableCh_Type()
)
tmnxRadSrvPlcyTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyTableCh.setStatus("current")
_TmnxRadSrvPlcySrvTableCh_Type = TimeStamp
_TmnxRadSrvPlcySrvTableCh_Object = MibScalar
tmnxRadSrvPlcySrvTableCh = _TmnxRadSrvPlcySrvTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 122),
    _TmnxRadSrvPlcySrvTableCh_Type()
)
tmnxRadSrvPlcySrvTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvTableCh.setStatus("current")
_TmnxRadScriptPlcyTableCh_Type = TimeStamp
_TmnxRadScriptPlcyTableCh_Object = MibScalar
tmnxRadScriptPlcyTableCh = _TmnxRadScriptPlcyTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 123),
    _TmnxRadScriptPlcyTableCh_Type()
)
tmnxRadScriptPlcyTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyTableCh.setStatus("current")
_TmnxRadRouteDownlTableCh_Type = TimeStamp
_TmnxRadRouteDownlTableCh_Object = MibScalar
tmnxRadRouteDownlTableCh = _TmnxRadRouteDownlTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 124),
    _TmnxRadRouteDownlTableCh_Type()
)
tmnxRadRouteDownlTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlTableCh.setStatus("current")
_TmnxRadSysCfgObjsCh_Type = TimeStamp
_TmnxRadSysCfgObjsCh_Object = MibScalar
tmnxRadSysCfgObjsCh = _TmnxRadSysCfgObjsCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 125),
    _TmnxRadSysCfgObjsCh_Type()
)
tmnxRadSysCfgObjsCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSysCfgObjsCh.setStatus("current")
_TmnxRadIsaPlcyTableCh_Type = TimeStamp
_TmnxRadIsaPlcyTableCh_Object = MibScalar
tmnxRadIsaPlcyTableCh = _TmnxRadIsaPlcyTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 126),
    _TmnxRadIsaPlcyTableCh_Type()
)
tmnxRadIsaPlcyTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaPlcyTableCh.setStatus("current")
_TmnxRadIsaSrvTableCh_Type = TimeStamp
_TmnxRadIsaSrvTableCh_Object = MibScalar
tmnxRadIsaSrvTableCh = _TmnxRadIsaSrvTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 127),
    _TmnxRadIsaSrvTableCh_Type()
)
tmnxRadIsaSrvTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadIsaSrvTableCh.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffTableCh_Type = TimeStamp
_TmnxRadSrvPlcyAcctOnOffTableCh_Object = MibScalar
tmnxRadSrvPlcyAcctOnOffTableCh = _TmnxRadSrvPlcyAcctOnOffTableCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 128),
    _TmnxRadSrvPlcyAcctOnOffTableCh_Type()
)
tmnxRadSrvPlcyAcctOnOffTableCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffTableCh.setStatus("current")
_TmnxRadSrvPlcyAcctOnOffGrpTbleCh_Type = TimeStamp
_TmnxRadSrvPlcyAcctOnOffGrpTbleCh_Object = MibScalar
tmnxRadSrvPlcyAcctOnOffGrpTbleCh = _TmnxRadSrvPlcyAcctOnOffGrpTbleCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 1, 129),
    _TmnxRadSrvPlcyAcctOnOffGrpTbleCh_Type()
)
tmnxRadSrvPlcyAcctOnOffGrpTbleCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffGrpTbleCh.setStatus("current")
_TmnxRadiusNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxRadiusNotificationObjects = _TmnxRadiusNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 2)
)
_TmnxRadiusNotifyAddrType_Type = InetAddressType
_TmnxRadiusNotifyAddrType_Object = MibScalar
tmnxRadiusNotifyAddrType = _TmnxRadiusNotifyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 2, 1),
    _TmnxRadiusNotifyAddrType_Type()
)
tmnxRadiusNotifyAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRadiusNotifyAddrType.setStatus("current")


class _TmnxRadiusNotifyAddr_Type(InetAddress):
    """Custom type tmnxRadiusNotifyAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxRadiusNotifyAddr_Type.__name__ = "InetAddress"
_TmnxRadiusNotifyAddr_Object = MibScalar
tmnxRadiusNotifyAddr = _TmnxRadiusNotifyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 2, 2),
    _TmnxRadiusNotifyAddr_Type()
)
tmnxRadiusNotifyAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRadiusNotifyAddr.setStatus("current")
_TmnxRadiusAdditionalInfo_Type = DisplayString
_TmnxRadiusAdditionalInfo_Object = MibScalar
tmnxRadiusAdditionalInfo = _TmnxRadiusAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 2, 3),
    _TmnxRadiusAdditionalInfo_Type()
)
tmnxRadiusAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRadiusAdditionalInfo.setStatus("current")


class _TmnxRadRouteDownlFailedReason_Type(Integer32):
    """Custom type tmnxRadRouteDownlFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("parsing-radius-attr-failed", 1),
          ("max-routes-reached", 2),
          ("rtm-update-failed", 3))
    )


_TmnxRadRouteDownlFailedReason_Type.__name__ = "Integer32"
_TmnxRadRouteDownlFailedReason_Object = MibScalar
tmnxRadRouteDownlFailedReason = _TmnxRadRouteDownlFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 79, 2, 4),
    _TmnxRadRouteDownlFailedReason_Type()
)
tmnxRadRouteDownlFailedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxRadRouteDownlFailedReason.setStatus("current")
_TmnxRadProxNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxRadProxNotifyPrefix = _TmnxRadProxNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 79)
)
_TmnxRadProxNotifications_ObjectIdentity = ObjectIdentity
tmnxRadProxNotifications = _TmnxRadProxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 79, 0)
)
tmnxRadProxSrvEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadPSStatusEntry")
)
tmnxRadPSStatusEntry.setIndexNames(*tmnxRadProxSrvEntry.getIndexNames())
tmnxRadProxSrvEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadPSStatsEntry")
)
tmnxRadPSStatsEntry.setIndexNames(*tmnxRadProxSrvEntry.getIndexNames())
tmnxRadSrvPlcyEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadSrvPlcyStatsEntry")
)
tmnxRadSrvPlcyStatsEntry.setIndexNames(*tmnxRadSrvPlcyEntry.getIndexNames())
tmnxRadSrvPlcySrvEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadSrvStatsEntry")
)
tmnxRadSrvStatsEntry.setIndexNames(*tmnxRadSrvPlcySrvEntry.getIndexNames())
tmnxRadSrvPlcyEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadSrvPlcyAcctOnOffEntry")
)
tmnxRadSrvPlcyAcctOnOffEntry.setIndexNames(*tmnxRadSrvPlcyEntry.getIndexNames())
tmnxRadSrvPlcyEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadSrvPlcyMsgBufStatsEntry")
)
tmnxRadSrvPlcyMsgBufStatsEntry.setIndexNames(*tmnxRadSrvPlcyEntry.getIndexNames())
tmnxRadRouteDownlEntry.registerAugmentions(
    ("TIMETRA-RADIUS-MIB",
     "tmnxRadRDStatsEntry")
)
tmnxRadRDStatsEntry.setIndexNames(*tmnxRadRouteDownlEntry.getIndexNames())

# Managed Objects groups

tmnxRadProxSrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 1)
)
tmnxRadProxSrvGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvPurpose"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvAdminState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvSecret"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvDefAuthSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvDefAccSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCaching"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKeyPktType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKeyAttrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKeyVendorId"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTrackAcct"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvSendAcctResponse"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBalanceKey"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr1"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId1"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr2"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId2"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr3"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId3"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr4"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId4"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr5"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId5"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatusCacheEntries"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatusCacheEntriesReg"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxPacket"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxAuthRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxAcctRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxDropped"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxRetransmit"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxAdminDown"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoAaaPol"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoLoadBKey"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvLen"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvCode"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvUserName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvPassword"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvAcctStatusTyp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoAcctStatusTyp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvAcctAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvMsgAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoMemory"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxUserOverload"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAuthAck"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAuthReject"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAuthChallenge"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAcctResponse"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxDropped"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheNoKey"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheKeyTooLong"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheAttrTooLong"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheMaxEntries"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxNoMemory"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerAuthFail"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerInvCode"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerInvAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxUserOverload"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxNoRadiusServer"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxSendFailure"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvIfTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvIfRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvIfLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspMatchString"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspAuthSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspAccSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheAge"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTimeLeft"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheRequestLength"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheAcceptLength"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheRegistered"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServSecret"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAcceptCoa"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServCoaScriptPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServPndRqLimit"))
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvGroup.setStatus("obsolete")

tmnxRadServGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 2)
)
tmnxRadServGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyRetry"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyDownTime"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyRouter"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrcAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrcAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAlgorithm"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsTxRequests"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsRxResponses"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsReqTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsReqSendFail"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsReqSendRetry"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsReqRejected"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvOperState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvOutTime"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvOvrldTime"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsTxRequests"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsRxResponses"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsReqTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsReqSendFailure"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsReqOvrldSendFail"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsReqPending"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsRespInvAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsRespInvMsgAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyRequestScriptPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcceptScriptPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSysCfgCoAPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSysCfgObjsCh"))
)
if mibBuilder.loadTexts:
    tmnxRadServGroup.setStatus("current")

tmnxRadScriptPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 3)
)
tmnxRadScriptPlcyGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyOnFail"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyPriURL"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyPriAdminState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyPriOperState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcySecURL"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcySecAdminState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcySecOperState"))
)
if mibBuilder.loadTexts:
    tmnxRadScriptPlcyGroup.setStatus("current")

tmnxRadRouteDownlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 4)
)
tmnxRadRouteDownlGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlAdminState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlRadServPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlDownloadIntvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlMinRetryIntvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlMaxRetryIntvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlDefaultMetric"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlDefaultTag"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlMaxRoutes"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlBaseUserName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlPassword"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRxLastAccessReject"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRxLastAccessAccept"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsTxLastAccessReq"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsTxLastAccReqRetry"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRemainingDownlTime"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRemainingRetryTime"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRoutesReceived"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRxAccessReject"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRxAccessAccept"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRxAccessAcceptDrop"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsTxAccessRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsTxAccessReqRetry"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsDownloads"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRDStatsRtmFailures"))
)
if mibBuilder.loadTexts:
    tmnxRadRouteDownlGroup.setStatus("current")

tmnxRadIsaAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 5)
)
tmnxRadIsaAuthGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyPassword"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyAuthInclAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyAcctInclAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyUserNameFormat"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyUserNameMacFormat"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcyNasIpAddressOrigin"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvRetry"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvVRtrID"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvSrcAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvSrcAddrStart"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvSrcAddrEnd"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPlcySrvAlgorithm"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvLastMgmtChange"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvAdminState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvSecret"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvPurpose"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvAcctPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvAuthPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvCoaPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatSrcAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatSrcAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatPurposeUp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatsName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaSrvStatsValue"))
)
if mibBuilder.loadTexts:
    tmnxRadIsaAuthGroup.setStatus("current")

tmnxRadSrvPlcyAcctOnOffV11v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 6)
)
tmnxRadSrvPlcyAcctOnOffV11v0Grp.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctLastChange"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffAdminSt"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffOperState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffSessionId"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffStateChng"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyBlockedState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctPerformAction"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctmAcctOffCause"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffTrigger"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffSrvName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffRetryCnt"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctReqScriptPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAuthReqScriptPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffGrpRowSt"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffGrpLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffGrpDescr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffGrpTbleCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctInterimMinItvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctInterimMaxItvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctInterimlifetim"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctStopMinItvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctStopMaxItvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctStoplifetim"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyNbrAcctStopBuf"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyNbrAcctInterimBuf"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyNbrAcctStopDrop"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyNbrAcctInterimDrop"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyLastBufClean"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyLastBufStatsClean"))
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcyAcctOnOffV11v0Grp.setStatus("current")

tmnxRadiusObsoletedV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 7)
)
tmnxRadiusObsoletedV11v0Group.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadServPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyRequestScriptPlcy"))
)
if mibBuilder.loadTexts:
    tmnxRadiusObsoletedV11v0Group.setStatus("current")

tmnxRadProxSrvV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 8)
)
tmnxRadProxSrvV11v0Group.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvPurpose"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvAdminState"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvSecret"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvDefAuthSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvDefAccSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCaching"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKeyPktType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKeyAttrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheKeyVendorId"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTrackAcct"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvSendAcctResponse"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBalanceKey"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr1"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId1"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr2"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId2"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr3"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId3"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr4"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId4"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBAttr5"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvLoadBVendorId5"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatusCacheEntries"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatusCacheEntriesReg"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxPacket"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxAuthRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxAcctRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxDropped"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxRetransmit"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxAdminDown"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoAaaPol"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoLoadBKey"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvLen"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvCode"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvUserName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvPassword"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvAcctStatusTyp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoAcctStatusTyp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvAcctAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxInvMsgAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxNoMemory"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxUserOverload"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAuthAck"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAuthReject"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAuthChallenge"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxAcctResponse"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxDropped"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheNoKey"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheKeyTooLong"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheAttrTooLong"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxCacheMaxEntries"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxNoMemory"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerAuthFail"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerInvCode"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxServerInvAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxUserOverload"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxNoRadiusServer"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxSendFailure"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvIfTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvIfRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvIfLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspMatchString"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspAuthSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxUsrToRspAccSrvPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheAge"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTimeLeft"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheRequestLength"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheAcceptLength"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheRegistered"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServTableCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServRowStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServSecret"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServDescription"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAcceptCoa"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServCoaScriptPlcy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServPndRqLimit"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAuthPort"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServAcctPort"))
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvV11v0Group.setStatus("current")

tmnxRadServV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 9)
)
tmnxRadServV11v0Group.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsAuthFailed"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsRejectRatio"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsAcctFailed"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsSuccessRatio"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyStatsFailureRatio"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAuthFailed"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAcctFailed"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAuthAvgDelay10"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAuthAvgDelay100"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAuthAvgDelay1000"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAuthAvgDelay10000"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAcctAvgDelay10"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAcctAvgDelay100"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAcctAvgDelay1000"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvStatsAcctAvgDelay10000"))
)
if mibBuilder.loadTexts:
    tmnxRadServV11v0Group.setStatus("current")

tmnxRadProxSrvV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 10)
)
tmnxRadProxSrvV12v0Group.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTrackAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheTrkDelHoldT"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheNasIpAddrTyp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheNasIpAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheNasIp6AddrTyp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheNasIp6Addr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvCacheCalldStation"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvWlanGwGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSWlanGwLastCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSWlanGwIpv4AddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSWlanGwIpv4Addr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSWlanGwIpv6AddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSWlanGwIpv6Addr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxPacket"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxAuthRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxAcctRequest"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxDropped"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxRetransmit"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxWrongPurpose"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxCacheNoUeMac"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxClientCtxtLim"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxNoAaaPol"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxInvAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxInvPassword"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxInvAcctStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxNoAcctStatus"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxInvAcctAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxInvMsgAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsRxMgmtOverload"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxAuthAck"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxAuthReject"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxAuthChallenge"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxAcctResponse"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxDropped"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxSrvTimeout"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxSrvInvAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxSrvInvMsgAuth"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxSrvInvAttr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaPSStatsTxSendFailure"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyPythonPolicy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvPythonPolicy"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsRxDroppedByPython"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadPSStatsTxDroppedByPython"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServPythonPolicy"))
)
if mibBuilder.loadTexts:
    tmnxRadProxSrvV12v0Group.setStatus("current")

tmnxRadServIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 11)
)
tmnxRadServIpv6Group.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyIpv6SrcAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyIpv6SrcAddr"))
)
if mibBuilder.loadTexts:
    tmnxRadServIpv6Group.setStatus("current")

tmnxRadiusNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 99)
)
tmnxRadiusNotifyObjsGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlFailedReason"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tmnxRadiusNotifyObjsGroup.setStatus("obsolete")

tmnxRadiusV11v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 102)
)
tmnxRadiusV11v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlFailedReason"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusAdditionalInfo"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyName"))
)
if mibBuilder.loadTexts:
    tmnxRadiusV11v0NotifyObjsGroup.setStatus("current")


# Notification objects

tmnxRadSrvPlcySrvOperStateCh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 79, 0, 1)
)
tmnxRadSrvPlcySrvOperStateCh.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyAddrType"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyAddr"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvOperState"))
)
if mibBuilder.loadTexts:
    tmnxRadSrvPlcySrvOperStateCh.setStatus(
        "current"
    )

tmnxRadRouteDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 79, 0, 2)
)
tmnxRadRouteDownloadFailed.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlDownloadIntvl"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlFailedReason"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tmnxRadRouteDownloadFailed.setStatus(
        "current"
    )

tmnxRadAcctOnOngoing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 79, 0, 3)
)
tmnxRadAcctOnOngoing.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyName"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffRetryCnt"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadiusAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tmnxRadAcctOnOngoing.setStatus(
        "current"
    )


# Notifications groups

tmnxRadiusNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 100)
)
tmnxRadiusNotifyGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvOperStateCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownloadFailed"))
)
if mibBuilder.loadTexts:
    tmnxRadiusNotifyGroup.setStatus(
        "obsolete"
    )

tmnxRadiusV11v0NotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 2, 101)
)
tmnxRadiusV11v0NotifyGroup.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcySrvOperStateCh"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownloadFailed"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadAcctOnOngoing"))
)
if mibBuilder.loadTexts:
    tmnxRadiusV11v0NotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxRadProxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 1, 1)
)
tmnxRadProxCompliance.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlGroup"))
)
if mibBuilder.loadTexts:
    tmnxRadProxCompliance.setStatus(
        "obsolete"
    )

tmnxRadiusNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 1, 2)
)
tmnxRadiusNotifyCompliance.setObjects(
    ("TIMETRA-RADIUS-MIB", "tmnxRadiusNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxRadiusNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxRadProxV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 1, 3)
)
tmnxRadProxV11v0Compliance.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvV11v0Group"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServV11v0Group"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaAuthGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffV11v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxRadProxV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxRadiusV11v0NotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 1, 4)
)
tmnxRadiusV11v0NotifyCompliance.setObjects(
    ("TIMETRA-RADIUS-MIB", "tmnxRadiusV11v0NotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxRadiusV11v0NotifyCompliance.setStatus(
        "current"
    )

tmnxRadProxV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 79, 1, 5)
)
tmnxRadProxV12v0Compliance.setObjects(
      *(("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvV11v0Group"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadProxSrvV12v0Group"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServV11v0Group"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadScriptPlcyGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadRouteDownlGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadIsaAuthGroup"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadSrvPlcyAcctOnOffV11v0Grp"),
        ("TIMETRA-RADIUS-MIB", "tmnxRadServIpv6Group"))
)
if mibBuilder.loadTexts:
    tmnxRadProxV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-RADIUS-MIB",
    **{"TmnxAuthSecret": TmnxAuthSecret,
       "TmnxRadMatchString": TmnxRadMatchString,
       "TmnxRadiusAcctStatusType": TmnxRadiusAcctStatusType,
       "timetraRadiusMIBModule": timetraRadiusMIBModule,
       "tmnxRadProxConformance": tmnxRadProxConformance,
       "tmnxRadProxCompliances": tmnxRadProxCompliances,
       "tmnxRadProxCompliance": tmnxRadProxCompliance,
       "tmnxRadiusNotifyCompliance": tmnxRadiusNotifyCompliance,
       "tmnxRadProxV11v0Compliance": tmnxRadProxV11v0Compliance,
       "tmnxRadiusV11v0NotifyCompliance": tmnxRadiusV11v0NotifyCompliance,
       "tmnxRadProxV12v0Compliance": tmnxRadProxV12v0Compliance,
       "tmnxRadProxGroups": tmnxRadProxGroups,
       "tmnxRadProxSrvGroup": tmnxRadProxSrvGroup,
       "tmnxRadServGroup": tmnxRadServGroup,
       "tmnxRadScriptPlcyGroup": tmnxRadScriptPlcyGroup,
       "tmnxRadRouteDownlGroup": tmnxRadRouteDownlGroup,
       "tmnxRadIsaAuthGroup": tmnxRadIsaAuthGroup,
       "tmnxRadSrvPlcyAcctOnOffV11v0Grp": tmnxRadSrvPlcyAcctOnOffV11v0Grp,
       "tmnxRadiusObsoletedV11v0Group": tmnxRadiusObsoletedV11v0Group,
       "tmnxRadProxSrvV11v0Group": tmnxRadProxSrvV11v0Group,
       "tmnxRadServV11v0Group": tmnxRadServV11v0Group,
       "tmnxRadProxSrvV12v0Group": tmnxRadProxSrvV12v0Group,
       "tmnxRadServIpv6Group": tmnxRadServIpv6Group,
       "tmnxRadiusNotifyObjsGroup": tmnxRadiusNotifyObjsGroup,
       "tmnxRadiusNotifyGroup": tmnxRadiusNotifyGroup,
       "tmnxRadiusV11v0NotifyGroup": tmnxRadiusV11v0NotifyGroup,
       "tmnxRadiusV11v0NotifyObjsGroup": tmnxRadiusV11v0NotifyObjsGroup,
       "tmnxRadius": tmnxRadius,
       "tmnxRadiusObjs": tmnxRadiusObjs,
       "tmnxRadProxSrvObjs": tmnxRadProxSrvObjs,
       "tmnxRadProxSrvTable": tmnxRadProxSrvTable,
       "tmnxRadProxSrvEntry": tmnxRadProxSrvEntry,
       "tmnxRadProxSrvName": tmnxRadProxSrvName,
       "tmnxRadProxSrvLastCh": tmnxRadProxSrvLastCh,
       "tmnxRadProxSrvRowStatus": tmnxRadProxSrvRowStatus,
       "tmnxRadProxSrvPurpose": tmnxRadProxSrvPurpose,
       "tmnxRadProxSrvAdminState": tmnxRadProxSrvAdminState,
       "tmnxRadProxSrvDescription": tmnxRadProxSrvDescription,
       "tmnxRadProxSrvSecret": tmnxRadProxSrvSecret,
       "tmnxRadProxSrvDefAuthSrvPlcy": tmnxRadProxSrvDefAuthSrvPlcy,
       "tmnxRadProxSrvDefAccSrvPlcy": tmnxRadProxSrvDefAccSrvPlcy,
       "tmnxRadProxSrvCaching": tmnxRadProxSrvCaching,
       "tmnxRadProxSrvCacheKeyPktType": tmnxRadProxSrvCacheKeyPktType,
       "tmnxRadProxSrvCacheKeyAttrType": tmnxRadProxSrvCacheKeyAttrType,
       "tmnxRadProxSrvCacheKeyVendorId": tmnxRadProxSrvCacheKeyVendorId,
       "tmnxRadProxSrvCacheTimeout": tmnxRadProxSrvCacheTimeout,
       "tmnxRadProxSrvCacheTrackAcct": tmnxRadProxSrvCacheTrackAcct,
       "tmnxRadProxSrvSendAcctResponse": tmnxRadProxSrvSendAcctResponse,
       "tmnxRadProxSrvLoadBalanceKey": tmnxRadProxSrvLoadBalanceKey,
       "tmnxRadProxSrvLoadBAttr1": tmnxRadProxSrvLoadBAttr1,
       "tmnxRadProxSrvLoadBVendorId1": tmnxRadProxSrvLoadBVendorId1,
       "tmnxRadProxSrvLoadBAttr2": tmnxRadProxSrvLoadBAttr2,
       "tmnxRadProxSrvLoadBVendorId2": tmnxRadProxSrvLoadBVendorId2,
       "tmnxRadProxSrvLoadBAttr3": tmnxRadProxSrvLoadBAttr3,
       "tmnxRadProxSrvLoadBVendorId3": tmnxRadProxSrvLoadBVendorId3,
       "tmnxRadProxSrvLoadBAttr4": tmnxRadProxSrvLoadBAttr4,
       "tmnxRadProxSrvLoadBVendorId4": tmnxRadProxSrvLoadBVendorId4,
       "tmnxRadProxSrvLoadBAttr5": tmnxRadProxSrvLoadBAttr5,
       "tmnxRadProxSrvLoadBVendorId5": tmnxRadProxSrvLoadBVendorId5,
       "tmnxRadProxSrvCacheTrackAuth": tmnxRadProxSrvCacheTrackAuth,
       "tmnxRadProxSrvWlanGwGroup": tmnxRadProxSrvWlanGwGroup,
       "tmnxRadProxSrvPythonPolicy": tmnxRadProxSrvPythonPolicy,
       "tmnxRadProxSrvCacheTrkDelHoldT": tmnxRadProxSrvCacheTrkDelHoldT,
       "tmnxRadPSStatusTable": tmnxRadPSStatusTable,
       "tmnxRadPSStatusEntry": tmnxRadPSStatusEntry,
       "tmnxRadPSStatusCacheEntries": tmnxRadPSStatusCacheEntries,
       "tmnxRadPSStatusCacheEntriesReg": tmnxRadPSStatusCacheEntriesReg,
       "tmnxRadPSStatsTable": tmnxRadPSStatsTable,
       "tmnxRadPSStatsEntry": tmnxRadPSStatsEntry,
       "tmnxRadPSStatsRxPacket": tmnxRadPSStatsRxPacket,
       "tmnxRadPSStatsRxAuthRequest": tmnxRadPSStatsRxAuthRequest,
       "tmnxRadPSStatsRxAcctRequest": tmnxRadPSStatsRxAcctRequest,
       "tmnxRadPSStatsRxDropped": tmnxRadPSStatsRxDropped,
       "tmnxRadPSStatsRxRetransmit": tmnxRadPSStatsRxRetransmit,
       "tmnxRadPSStatsRxAdminDown": tmnxRadPSStatsRxAdminDown,
       "tmnxRadPSStatsRxNoAaaPol": tmnxRadPSStatsRxNoAaaPol,
       "tmnxRadPSStatsRxNoLoadBKey": tmnxRadPSStatsRxNoLoadBKey,
       "tmnxRadPSStatsRxInvLen": tmnxRadPSStatsRxInvLen,
       "tmnxRadPSStatsRxInvCode": tmnxRadPSStatsRxInvCode,
       "tmnxRadPSStatsRxInvAttr": tmnxRadPSStatsRxInvAttr,
       "tmnxRadPSStatsRxInvUserName": tmnxRadPSStatsRxInvUserName,
       "tmnxRadPSStatsRxInvPassword": tmnxRadPSStatsRxInvPassword,
       "tmnxRadPSStatsRxInvAcctStatusTyp": tmnxRadPSStatsRxInvAcctStatusTyp,
       "tmnxRadPSStatsRxNoAcctStatusTyp": tmnxRadPSStatsRxNoAcctStatusTyp,
       "tmnxRadPSStatsRxInvAcctAuth": tmnxRadPSStatsRxInvAcctAuth,
       "tmnxRadPSStatsRxInvMsgAuth": tmnxRadPSStatsRxInvMsgAuth,
       "tmnxRadPSStatsRxNoMemory": tmnxRadPSStatsRxNoMemory,
       "tmnxRadPSStatsRxUserOverload": tmnxRadPSStatsRxUserOverload,
       "tmnxRadPSStatsTxAuthAck": tmnxRadPSStatsTxAuthAck,
       "tmnxRadPSStatsTxAuthReject": tmnxRadPSStatsTxAuthReject,
       "tmnxRadPSStatsTxAuthChallenge": tmnxRadPSStatsTxAuthChallenge,
       "tmnxRadPSStatsTxAcctResponse": tmnxRadPSStatsTxAcctResponse,
       "tmnxRadPSStatsTxDropped": tmnxRadPSStatsTxDropped,
       "tmnxRadPSStatsTxCacheNoKey": tmnxRadPSStatsTxCacheNoKey,
       "tmnxRadPSStatsTxCacheKeyTooLong": tmnxRadPSStatsTxCacheKeyTooLong,
       "tmnxRadPSStatsTxCacheAttrTooLong": tmnxRadPSStatsTxCacheAttrTooLong,
       "tmnxRadPSStatsTxCacheMaxEntries": tmnxRadPSStatsTxCacheMaxEntries,
       "tmnxRadPSStatsTxNoMemory": tmnxRadPSStatsTxNoMemory,
       "tmnxRadPSStatsTxServerTimeout": tmnxRadPSStatsTxServerTimeout,
       "tmnxRadPSStatsTxServerAuthFail": tmnxRadPSStatsTxServerAuthFail,
       "tmnxRadPSStatsTxServerInvCode": tmnxRadPSStatsTxServerInvCode,
       "tmnxRadPSStatsTxServerInvAttr": tmnxRadPSStatsTxServerInvAttr,
       "tmnxRadPSStatsTxUserOverload": tmnxRadPSStatsTxUserOverload,
       "tmnxRadPSStatsTxNoRadiusServer": tmnxRadPSStatsTxNoRadiusServer,
       "tmnxRadPSStatsTxSendFailure": tmnxRadPSStatsTxSendFailure,
       "tmnxRadPSStatsRxDroppedByPython": tmnxRadPSStatsRxDroppedByPython,
       "tmnxRadPSStatsTxDroppedByPython": tmnxRadPSStatsTxDroppedByPython,
       "tmnxRadProxSrvIfTable": tmnxRadProxSrvIfTable,
       "tmnxRadProxSrvIfEntry": tmnxRadProxSrvIfEntry,
       "tmnxRadProxSrvIfRowStatus": tmnxRadProxSrvIfRowStatus,
       "tmnxRadProxSrvIfLastCh": tmnxRadProxSrvIfLastCh,
       "tmnxRadProxUsrToRspTable": tmnxRadProxUsrToRspTable,
       "tmnxRadProxUsrToRspEntry": tmnxRadProxUsrToRspEntry,
       "tmnxRadProxUsrToRspIndex": tmnxRadProxUsrToRspIndex,
       "tmnxRadProxUsrToRspRowStatus": tmnxRadProxUsrToRspRowStatus,
       "tmnxRadProxUsrToRspLastCh": tmnxRadProxUsrToRspLastCh,
       "tmnxRadProxUsrToRspMatchString": tmnxRadProxUsrToRspMatchString,
       "tmnxRadProxUsrToRspAuthSrvPlcy": tmnxRadProxUsrToRspAuthSrvPlcy,
       "tmnxRadProxUsrToRspAccSrvPlcy": tmnxRadProxUsrToRspAccSrvPlcy,
       "tmnxRadProxSrvCacheTable": tmnxRadProxSrvCacheTable,
       "tmnxRadProxSrvCacheEntry": tmnxRadProxSrvCacheEntry,
       "tmnxRadProxSrvCacheKey": tmnxRadProxSrvCacheKey,
       "tmnxRadProxSrvCacheAge": tmnxRadProxSrvCacheAge,
       "tmnxRadProxSrvCacheTimeLeft": tmnxRadProxSrvCacheTimeLeft,
       "tmnxRadProxSrvCacheRequestLength": tmnxRadProxSrvCacheRequestLength,
       "tmnxRadProxSrvCacheAcceptLength": tmnxRadProxSrvCacheAcceptLength,
       "tmnxRadProxSrvCacheRegistered": tmnxRadProxSrvCacheRegistered,
       "tmnxRadProxSrvCacheNasIpAddrTyp": tmnxRadProxSrvCacheNasIpAddrTyp,
       "tmnxRadProxSrvCacheNasIpAddr": tmnxRadProxSrvCacheNasIpAddr,
       "tmnxRadProxSrvCacheNasIp6AddrTyp": tmnxRadProxSrvCacheNasIp6AddrTyp,
       "tmnxRadProxSrvCacheNasIp6Addr": tmnxRadProxSrvCacheNasIp6Addr,
       "tmnxRadProxSrvCacheCalldStation": tmnxRadProxSrvCacheCalldStation,
       "tmnxRadPSWlanGwTable": tmnxRadPSWlanGwTable,
       "tmnxRadPSWlanGwEntry": tmnxRadPSWlanGwEntry,
       "tmnxRadPSWlanGwLastCh": tmnxRadPSWlanGwLastCh,
       "tmnxRadPSWlanGwIpv4AddrType": tmnxRadPSWlanGwIpv4AddrType,
       "tmnxRadPSWlanGwIpv4Addr": tmnxRadPSWlanGwIpv4Addr,
       "tmnxRadPSWlanGwIpv6AddrType": tmnxRadPSWlanGwIpv6AddrType,
       "tmnxRadPSWlanGwIpv6Addr": tmnxRadPSWlanGwIpv6Addr,
       "tmnxRadSrvObjs": tmnxRadSrvObjs,
       "tmnxRadServTable": tmnxRadServTable,
       "tmnxRadServEntry": tmnxRadServEntry,
       "tmnxRadServName": tmnxRadServName,
       "tmnxRadServLastCh": tmnxRadServLastCh,
       "tmnxRadServRowStatus": tmnxRadServRowStatus,
       "tmnxRadServAddrType": tmnxRadServAddrType,
       "tmnxRadServAddr": tmnxRadServAddr,
       "tmnxRadServPort": tmnxRadServPort,
       "tmnxRadServSecret": tmnxRadServSecret,
       "tmnxRadServDescription": tmnxRadServDescription,
       "tmnxRadServAcceptCoa": tmnxRadServAcceptCoa,
       "tmnxRadServCoaScriptPlcy": tmnxRadServCoaScriptPlcy,
       "tmnxRadServPndRqLimit": tmnxRadServPndRqLimit,
       "tmnxRadServAuthPort": tmnxRadServAuthPort,
       "tmnxRadServAcctPort": tmnxRadServAcctPort,
       "tmnxRadServPythonPolicy": tmnxRadServPythonPolicy,
       "tmnxRadSrvPlcyTable": tmnxRadSrvPlcyTable,
       "tmnxRadSrvPlcyEntry": tmnxRadSrvPlcyEntry,
       "tmnxRadSrvPlcyName": tmnxRadSrvPlcyName,
       "tmnxRadSrvPlcyRowStatus": tmnxRadSrvPlcyRowStatus,
       "tmnxRadSrvPlcyLastCh": tmnxRadSrvPlcyLastCh,
       "tmnxRadSrvPlcyDescription": tmnxRadSrvPlcyDescription,
       "tmnxRadSrvPlcyTimeout": tmnxRadSrvPlcyTimeout,
       "tmnxRadSrvPlcyRetry": tmnxRadSrvPlcyRetry,
       "tmnxRadSrvPlcyDownTime": tmnxRadSrvPlcyDownTime,
       "tmnxRadSrvPlcyRouter": tmnxRadSrvPlcyRouter,
       "tmnxRadSrvPlcySrcAddrType": tmnxRadSrvPlcySrcAddrType,
       "tmnxRadSrvPlcySrcAddr": tmnxRadSrvPlcySrcAddr,
       "tmnxRadSrvPlcyAlgorithm": tmnxRadSrvPlcyAlgorithm,
       "tmnxRadSrvPlcyRequestScriptPlcy": tmnxRadSrvPlcyRequestScriptPlcy,
       "tmnxRadSrvPlcyAcceptScriptPlcy": tmnxRadSrvPlcyAcceptScriptPlcy,
       "tmnxRadSrvPlcyBlockedState": tmnxRadSrvPlcyBlockedState,
       "tmnxRadSrvPlcyAcctReqScriptPlcy": tmnxRadSrvPlcyAcctReqScriptPlcy,
       "tmnxRadSrvPlcyAuthReqScriptPlcy": tmnxRadSrvPlcyAuthReqScriptPlcy,
       "tmnxRadSrvPlcyAcctInterimMinItvl": tmnxRadSrvPlcyAcctInterimMinItvl,
       "tmnxRadSrvPlcyAcctInterimMaxItvl": tmnxRadSrvPlcyAcctInterimMaxItvl,
       "tmnxRadSrvPlcyAcctInterimlifetim": tmnxRadSrvPlcyAcctInterimlifetim,
       "tmnxRadSrvPlcyAcctStopMinItvl": tmnxRadSrvPlcyAcctStopMinItvl,
       "tmnxRadSrvPlcyAcctStopMaxItvl": tmnxRadSrvPlcyAcctStopMaxItvl,
       "tmnxRadSrvPlcyAcctStoplifetim": tmnxRadSrvPlcyAcctStoplifetim,
       "tmnxRadSrvPlcyPythonPolicy": tmnxRadSrvPlcyPythonPolicy,
       "tmnxRadSrvPlcyIpv6SrcAddrType": tmnxRadSrvPlcyIpv6SrcAddrType,
       "tmnxRadSrvPlcyIpv6SrcAddr": tmnxRadSrvPlcyIpv6SrcAddr,
       "tmnxRadSrvPlcyStatsTable": tmnxRadSrvPlcyStatsTable,
       "tmnxRadSrvPlcyStatsEntry": tmnxRadSrvPlcyStatsEntry,
       "tmnxRadSrvPlcyStatsTxRequests": tmnxRadSrvPlcyStatsTxRequests,
       "tmnxRadSrvPlcyStatsRxResponses": tmnxRadSrvPlcyStatsRxResponses,
       "tmnxRadSrvPlcyStatsReqTimeout": tmnxRadSrvPlcyStatsReqTimeout,
       "tmnxRadSrvPlcyStatsReqSendFail": tmnxRadSrvPlcyStatsReqSendFail,
       "tmnxRadSrvPlcyStatsReqSendRetry": tmnxRadSrvPlcyStatsReqSendRetry,
       "tmnxRadSrvPlcyStatsReqRejected": tmnxRadSrvPlcyStatsReqRejected,
       "tmnxRadSrvPlcyStatsAuthFailed": tmnxRadSrvPlcyStatsAuthFailed,
       "tmnxRadSrvPlcyStatsRejectRatio": tmnxRadSrvPlcyStatsRejectRatio,
       "tmnxRadSrvPlcyStatsAcctFailed": tmnxRadSrvPlcyStatsAcctFailed,
       "tmnxRadSrvPlcyStatsSuccessRatio": tmnxRadSrvPlcyStatsSuccessRatio,
       "tmnxRadSrvPlcyStatsFailureRatio": tmnxRadSrvPlcyStatsFailureRatio,
       "tmnxRadSrvPlcySrvTable": tmnxRadSrvPlcySrvTable,
       "tmnxRadSrvPlcySrvEntry": tmnxRadSrvPlcySrvEntry,
       "tmnxRadSrvPlcySrvIndex": tmnxRadSrvPlcySrvIndex,
       "tmnxRadSrvPlcySrvRowStatus": tmnxRadSrvPlcySrvRowStatus,
       "tmnxRadSrvPlcySrvLastCh": tmnxRadSrvPlcySrvLastCh,
       "tmnxRadSrvPlcySrvName": tmnxRadSrvPlcySrvName,
       "tmnxRadSrvPlcySrvOperState": tmnxRadSrvPlcySrvOperState,
       "tmnxRadSrvPlcySrvOutTime": tmnxRadSrvPlcySrvOutTime,
       "tmnxRadSrvPlcySrvOvrldTime": tmnxRadSrvPlcySrvOvrldTime,
       "tmnxRadSrvStatsTable": tmnxRadSrvStatsTable,
       "tmnxRadSrvStatsEntry": tmnxRadSrvStatsEntry,
       "tmnxRadSrvStatsTxRequests": tmnxRadSrvStatsTxRequests,
       "tmnxRadSrvStatsRxResponses": tmnxRadSrvStatsRxResponses,
       "tmnxRadSrvStatsReqTimeout": tmnxRadSrvStatsReqTimeout,
       "tmnxRadSrvStatsReqSendFailure": tmnxRadSrvStatsReqSendFailure,
       "tmnxRadSrvStatsReqOvrldSendFail": tmnxRadSrvStatsReqOvrldSendFail,
       "tmnxRadSrvStatsReqPending": tmnxRadSrvStatsReqPending,
       "tmnxRadSrvStatsRespInvAuth": tmnxRadSrvStatsRespInvAuth,
       "tmnxRadSrvStatsRespInvMsgAuth": tmnxRadSrvStatsRespInvMsgAuth,
       "tmnxRadSrvStatsAuthFailed": tmnxRadSrvStatsAuthFailed,
       "tmnxRadSrvStatsAcctFailed": tmnxRadSrvStatsAcctFailed,
       "tmnxRadSrvStatsAuthAvgDelay10": tmnxRadSrvStatsAuthAvgDelay10,
       "tmnxRadSrvStatsAuthAvgDelay100": tmnxRadSrvStatsAuthAvgDelay100,
       "tmnxRadSrvStatsAuthAvgDelay1000": tmnxRadSrvStatsAuthAvgDelay1000,
       "tmnxRadSrvStatsAuthAvgDelay10000": tmnxRadSrvStatsAuthAvgDelay10000,
       "tmnxRadSrvStatsAcctAvgDelay10": tmnxRadSrvStatsAcctAvgDelay10,
       "tmnxRadSrvStatsAcctAvgDelay100": tmnxRadSrvStatsAcctAvgDelay100,
       "tmnxRadSrvStatsAcctAvgDelay1000": tmnxRadSrvStatsAcctAvgDelay1000,
       "tmnxRadSrvStatsAcctAvgDelay10000": tmnxRadSrvStatsAcctAvgDelay10000,
       "tmnxRadSrvPlcyAcctOnOffTable": tmnxRadSrvPlcyAcctOnOffTable,
       "tmnxRadSrvPlcyAcctOnOffEntry": tmnxRadSrvPlcyAcctOnOffEntry,
       "tmnxRadSrvPlcyAcctLastChange": tmnxRadSrvPlcyAcctLastChange,
       "tmnxRadSrvPlcyAcctOnOffAdminSt": tmnxRadSrvPlcyAcctOnOffAdminSt,
       "tmnxRadSrvPlcyAcctOnOffOperState": tmnxRadSrvPlcyAcctOnOffOperState,
       "tmnxRadSrvPlcyAcctOnOffSessionId": tmnxRadSrvPlcyAcctOnOffSessionId,
       "tmnxRadSrvPlcyAcctOnOffStateChng": tmnxRadSrvPlcyAcctOnOffStateChng,
       "tmnxRadSrvPlcyAcctPerformAction": tmnxRadSrvPlcyAcctPerformAction,
       "tmnxRadSrvPlcyAcctmAcctOffCause": tmnxRadSrvPlcyAcctmAcctOffCause,
       "tmnxRadSrvPlcyAcctOnOffTrigger": tmnxRadSrvPlcyAcctOnOffTrigger,
       "tmnxRadSrvPlcyAcctOnOffSrvName": tmnxRadSrvPlcyAcctOnOffSrvName,
       "tmnxRadSrvPlcyAcctOnOffGroup": tmnxRadSrvPlcyAcctOnOffGroup,
       "tmnxRadSrvPlcyAcctOnOffRetryCnt": tmnxRadSrvPlcyAcctOnOffRetryCnt,
       "tmnxRadSrvPlcyAcctOnOffGrpTable": tmnxRadSrvPlcyAcctOnOffGrpTable,
       "tmnxRadSrvPlcyAcctOnOffGrpEntry": tmnxRadSrvPlcyAcctOnOffGrpEntry,
       "tmnxRadSrvPlcyAcctOnOffGrpName": tmnxRadSrvPlcyAcctOnOffGrpName,
       "tmnxRadSrvPlcyAcctOnOffGrpRowSt": tmnxRadSrvPlcyAcctOnOffGrpRowSt,
       "tmnxRadSrvPlcyAcctOnOffGrpLastCh": tmnxRadSrvPlcyAcctOnOffGrpLastCh,
       "tmnxRadSrvPlcyAcctOnOffGrpDescr": tmnxRadSrvPlcyAcctOnOffGrpDescr,
       "tmnxRadSrvPlcyMsgBufStatsTable": tmnxRadSrvPlcyMsgBufStatsTable,
       "tmnxRadSrvPlcyMsgBufStatsEntry": tmnxRadSrvPlcyMsgBufStatsEntry,
       "tmnxRadSrvPlcyNbrAcctStopBuf": tmnxRadSrvPlcyNbrAcctStopBuf,
       "tmnxRadSrvPlcyNbrAcctInterimBuf": tmnxRadSrvPlcyNbrAcctInterimBuf,
       "tmnxRadSrvPlcyNbrAcctStopDrop": tmnxRadSrvPlcyNbrAcctStopDrop,
       "tmnxRadSrvPlcyNbrAcctInterimDrop": tmnxRadSrvPlcyNbrAcctInterimDrop,
       "tmnxRadSrvPlcyLastBufClean": tmnxRadSrvPlcyLastBufClean,
       "tmnxRadSrvPlcyLastBufStatsClean": tmnxRadSrvPlcyLastBufStatsClean,
       "tmnxRadScriptPlcyObjs": tmnxRadScriptPlcyObjs,
       "tmnxRadScriptPlcyTable": tmnxRadScriptPlcyTable,
       "tmnxRadScriptPlcyEntry": tmnxRadScriptPlcyEntry,
       "tmnxRadScriptPlcyName": tmnxRadScriptPlcyName,
       "tmnxRadScriptPlcyRowStatus": tmnxRadScriptPlcyRowStatus,
       "tmnxRadScriptPlcyLastCh": tmnxRadScriptPlcyLastCh,
       "tmnxRadScriptPlcyDescription": tmnxRadScriptPlcyDescription,
       "tmnxRadScriptPlcyOnFail": tmnxRadScriptPlcyOnFail,
       "tmnxRadScriptPlcyPriURL": tmnxRadScriptPlcyPriURL,
       "tmnxRadScriptPlcyPriAdminState": tmnxRadScriptPlcyPriAdminState,
       "tmnxRadScriptPlcyPriOperState": tmnxRadScriptPlcyPriOperState,
       "tmnxRadScriptPlcySecURL": tmnxRadScriptPlcySecURL,
       "tmnxRadScriptPlcySecAdminState": tmnxRadScriptPlcySecAdminState,
       "tmnxRadScriptPlcySecOperState": tmnxRadScriptPlcySecOperState,
       "tmnxRadRouteDownlObjs": tmnxRadRouteDownlObjs,
       "tmnxRadRouteDownlTable": tmnxRadRouteDownlTable,
       "tmnxRadRouteDownlEntry": tmnxRadRouteDownlEntry,
       "tmnxRadRouteDownlName": tmnxRadRouteDownlName,
       "tmnxRadRouteDownlRowStatus": tmnxRadRouteDownlRowStatus,
       "tmnxRadRouteDownlLastCh": tmnxRadRouteDownlLastCh,
       "tmnxRadRouteDownlDescription": tmnxRadRouteDownlDescription,
       "tmnxRadRouteDownlAdminState": tmnxRadRouteDownlAdminState,
       "tmnxRadRouteDownlRadServPlcy": tmnxRadRouteDownlRadServPlcy,
       "tmnxRadRouteDownlDownloadIntvl": tmnxRadRouteDownlDownloadIntvl,
       "tmnxRadRouteDownlMinRetryIntvl": tmnxRadRouteDownlMinRetryIntvl,
       "tmnxRadRouteDownlMaxRetryIntvl": tmnxRadRouteDownlMaxRetryIntvl,
       "tmnxRadRouteDownlDefaultMetric": tmnxRadRouteDownlDefaultMetric,
       "tmnxRadRouteDownlDefaultTag": tmnxRadRouteDownlDefaultTag,
       "tmnxRadRouteDownlMaxRoutes": tmnxRadRouteDownlMaxRoutes,
       "tmnxRadRouteDownlBaseUserName": tmnxRadRouteDownlBaseUserName,
       "tmnxRadRouteDownlPassword": tmnxRadRouteDownlPassword,
       "tmnxRadRDStatsTable": tmnxRadRDStatsTable,
       "tmnxRadRDStatsEntry": tmnxRadRDStatsEntry,
       "tmnxRadRDStatsRxLastAccessReject": tmnxRadRDStatsRxLastAccessReject,
       "tmnxRadRDStatsRxLastAccessAccept": tmnxRadRDStatsRxLastAccessAccept,
       "tmnxRadRDStatsTxLastAccessReq": tmnxRadRDStatsTxLastAccessReq,
       "tmnxRadRDStatsTxLastAccReqRetry": tmnxRadRDStatsTxLastAccReqRetry,
       "tmnxRadRDStatsRemainingDownlTime": tmnxRadRDStatsRemainingDownlTime,
       "tmnxRadRDStatsRemainingRetryTime": tmnxRadRDStatsRemainingRetryTime,
       "tmnxRadRDStatsRoutesReceived": tmnxRadRDStatsRoutesReceived,
       "tmnxRadRDStatsRxAccessReject": tmnxRadRDStatsRxAccessReject,
       "tmnxRadRDStatsRxAccessAccept": tmnxRadRDStatsRxAccessAccept,
       "tmnxRadRDStatsRxAccessAcceptDrop": tmnxRadRDStatsRxAccessAcceptDrop,
       "tmnxRadRDStatsTxAccessRequest": tmnxRadRDStatsTxAccessRequest,
       "tmnxRadRDStatsTxAccessReqRetry": tmnxRadRDStatsTxAccessReqRetry,
       "tmnxRadRDStatsDownloads": tmnxRadRDStatsDownloads,
       "tmnxRadRDStatsRtmFailures": tmnxRadRDStatsRtmFailures,
       "tmnxRadSysCfgObjs": tmnxRadSysCfgObjs,
       "tmnxRadSysCfgCoAPort": tmnxRadSysCfgCoAPort,
       "tmnxRadIsaObjs": tmnxRadIsaObjs,
       "tmnxRadIsaPlcyTable": tmnxRadIsaPlcyTable,
       "tmnxRadIsaPlcyEntry": tmnxRadIsaPlcyEntry,
       "tmnxRadIsaPlcyName": tmnxRadIsaPlcyName,
       "tmnxRadIsaPlcyRowStatus": tmnxRadIsaPlcyRowStatus,
       "tmnxRadIsaPlcyLastCh": tmnxRadIsaPlcyLastCh,
       "tmnxRadIsaPlcyDescription": tmnxRadIsaPlcyDescription,
       "tmnxRadIsaPlcyPassword": tmnxRadIsaPlcyPassword,
       "tmnxRadIsaPlcyAuthInclAttr": tmnxRadIsaPlcyAuthInclAttr,
       "tmnxRadIsaPlcyAcctInclAttr": tmnxRadIsaPlcyAcctInclAttr,
       "tmnxRadIsaPlcyUserNameFormat": tmnxRadIsaPlcyUserNameFormat,
       "tmnxRadIsaPlcyUserNameMacFormat": tmnxRadIsaPlcyUserNameMacFormat,
       "tmnxRadIsaPlcyNasIpAddressOrigin": tmnxRadIsaPlcyNasIpAddressOrigin,
       "tmnxRadIsaPlcySrvTimeout": tmnxRadIsaPlcySrvTimeout,
       "tmnxRadIsaPlcySrvRetry": tmnxRadIsaPlcySrvRetry,
       "tmnxRadIsaPlcySrvVRtrID": tmnxRadIsaPlcySrvVRtrID,
       "tmnxRadIsaPlcySrvSrcAddrType": tmnxRadIsaPlcySrvSrcAddrType,
       "tmnxRadIsaPlcySrvSrcAddrStart": tmnxRadIsaPlcySrvSrcAddrStart,
       "tmnxRadIsaPlcySrvSrcAddrEnd": tmnxRadIsaPlcySrvSrcAddrEnd,
       "tmnxRadIsaPlcySrvAlgorithm": tmnxRadIsaPlcySrvAlgorithm,
       "tmnxRadIsaSrvTable": tmnxRadIsaSrvTable,
       "tmnxRadIsaSrvEntry": tmnxRadIsaSrvEntry,
       "tmnxRadIsaSrvIndex": tmnxRadIsaSrvIndex,
       "tmnxRadIsaSrvRowStatus": tmnxRadIsaSrvRowStatus,
       "tmnxRadIsaSrvLastMgmtChange": tmnxRadIsaSrvLastMgmtChange,
       "tmnxRadIsaSrvAdminState": tmnxRadIsaSrvAdminState,
       "tmnxRadIsaSrvAddrType": tmnxRadIsaSrvAddrType,
       "tmnxRadIsaSrvAddr": tmnxRadIsaSrvAddr,
       "tmnxRadIsaSrvSecret": tmnxRadIsaSrvSecret,
       "tmnxRadIsaSrvPurpose": tmnxRadIsaSrvPurpose,
       "tmnxRadIsaSrvAcctPort": tmnxRadIsaSrvAcctPort,
       "tmnxRadIsaSrvAuthPort": tmnxRadIsaSrvAuthPort,
       "tmnxRadIsaSrvCoaPort": tmnxRadIsaSrvCoaPort,
       "tmnxRadIsaSrvStatTable": tmnxRadIsaSrvStatTable,
       "tmnxRadIsaSrvStatEntry": tmnxRadIsaSrvStatEntry,
       "tmnxRadIsaSrvStatGrpId": tmnxRadIsaSrvStatGrpId,
       "tmnxRadIsaSrvStatMemberId": tmnxRadIsaSrvStatMemberId,
       "tmnxRadIsaSrvStatSrcAddrType": tmnxRadIsaSrvStatSrcAddrType,
       "tmnxRadIsaSrvStatSrcAddr": tmnxRadIsaSrvStatSrcAddr,
       "tmnxRadIsaSrvStatPurposeUp": tmnxRadIsaSrvStatPurposeUp,
       "tmnxRadIsaSrvStatsTable": tmnxRadIsaSrvStatsTable,
       "tmnxRadIsaSrvStatsEntry": tmnxRadIsaSrvStatsEntry,
       "tmnxRadIsaSrvStatsType": tmnxRadIsaSrvStatsType,
       "tmnxRadIsaSrvStatsName": tmnxRadIsaSrvStatsName,
       "tmnxRadIsaSrvStatsValue": tmnxRadIsaSrvStatsValue,
       "tmnxRadIsaPSStatsTable": tmnxRadIsaPSStatsTable,
       "tmnxRadIsaPSStatsEntry": tmnxRadIsaPSStatsEntry,
       "tmnxRadIsaPSStatsRxPacket": tmnxRadIsaPSStatsRxPacket,
       "tmnxRadIsaPSStatsRxAuthRequest": tmnxRadIsaPSStatsRxAuthRequest,
       "tmnxRadIsaPSStatsRxAcctRequest": tmnxRadIsaPSStatsRxAcctRequest,
       "tmnxRadIsaPSStatsRxDropped": tmnxRadIsaPSStatsRxDropped,
       "tmnxRadIsaPSStatsRxRetransmit": tmnxRadIsaPSStatsRxRetransmit,
       "tmnxRadIsaPSStatsRxWrongPurpose": tmnxRadIsaPSStatsRxWrongPurpose,
       "tmnxRadIsaPSStatsRxCacheNoUeMac": tmnxRadIsaPSStatsRxCacheNoUeMac,
       "tmnxRadIsaPSStatsRxClientCtxtLim": tmnxRadIsaPSStatsRxClientCtxtLim,
       "tmnxRadIsaPSStatsRxNoAaaPol": tmnxRadIsaPSStatsRxNoAaaPol,
       "tmnxRadIsaPSStatsRxInvAttr": tmnxRadIsaPSStatsRxInvAttr,
       "tmnxRadIsaPSStatsRxInvPassword": tmnxRadIsaPSStatsRxInvPassword,
       "tmnxRadIsaPSStatsRxInvAcctStatus": tmnxRadIsaPSStatsRxInvAcctStatus,
       "tmnxRadIsaPSStatsRxNoAcctStatus": tmnxRadIsaPSStatsRxNoAcctStatus,
       "tmnxRadIsaPSStatsRxInvAcctAuth": tmnxRadIsaPSStatsRxInvAcctAuth,
       "tmnxRadIsaPSStatsRxInvMsgAuth": tmnxRadIsaPSStatsRxInvMsgAuth,
       "tmnxRadIsaPSStatsRxMgmtOverload": tmnxRadIsaPSStatsRxMgmtOverload,
       "tmnxRadIsaPSStatsTxAuthAck": tmnxRadIsaPSStatsTxAuthAck,
       "tmnxRadIsaPSStatsTxAuthReject": tmnxRadIsaPSStatsTxAuthReject,
       "tmnxRadIsaPSStatsTxAuthChallenge": tmnxRadIsaPSStatsTxAuthChallenge,
       "tmnxRadIsaPSStatsTxAcctResponse": tmnxRadIsaPSStatsTxAcctResponse,
       "tmnxRadIsaPSStatsTxDropped": tmnxRadIsaPSStatsTxDropped,
       "tmnxRadIsaPSStatsTxSrvTimeout": tmnxRadIsaPSStatsTxSrvTimeout,
       "tmnxRadIsaPSStatsTxSrvInvAuth": tmnxRadIsaPSStatsTxSrvInvAuth,
       "tmnxRadIsaPSStatsTxSrvInvMsgAuth": tmnxRadIsaPSStatsTxSrvInvMsgAuth,
       "tmnxRadIsaPSStatsTxSrvInvAttr": tmnxRadIsaPSStatsTxSrvInvAttr,
       "tmnxRadIsaPSStatsTxSendFailure": tmnxRadIsaPSStatsTxSendFailure,
       "tmnxRadProxSrvTableCh": tmnxRadProxSrvTableCh,
       "tmnxRadProxSrvIfTableCh": tmnxRadProxSrvIfTableCh,
       "tmnxRadProxUsrToRspTableCh": tmnxRadProxUsrToRspTableCh,
       "tmnxRadServTableCh": tmnxRadServTableCh,
       "tmnxRadSrvPlcyTableCh": tmnxRadSrvPlcyTableCh,
       "tmnxRadSrvPlcySrvTableCh": tmnxRadSrvPlcySrvTableCh,
       "tmnxRadScriptPlcyTableCh": tmnxRadScriptPlcyTableCh,
       "tmnxRadRouteDownlTableCh": tmnxRadRouteDownlTableCh,
       "tmnxRadSysCfgObjsCh": tmnxRadSysCfgObjsCh,
       "tmnxRadIsaPlcyTableCh": tmnxRadIsaPlcyTableCh,
       "tmnxRadIsaSrvTableCh": tmnxRadIsaSrvTableCh,
       "tmnxRadSrvPlcyAcctOnOffTableCh": tmnxRadSrvPlcyAcctOnOffTableCh,
       "tmnxRadSrvPlcyAcctOnOffGrpTbleCh": tmnxRadSrvPlcyAcctOnOffGrpTbleCh,
       "tmnxRadiusNotificationObjects": tmnxRadiusNotificationObjects,
       "tmnxRadiusNotifyAddrType": tmnxRadiusNotifyAddrType,
       "tmnxRadiusNotifyAddr": tmnxRadiusNotifyAddr,
       "tmnxRadiusAdditionalInfo": tmnxRadiusAdditionalInfo,
       "tmnxRadRouteDownlFailedReason": tmnxRadRouteDownlFailedReason,
       "tmnxRadProxNotifyPrefix": tmnxRadProxNotifyPrefix,
       "tmnxRadProxNotifications": tmnxRadProxNotifications,
       "tmnxRadSrvPlcySrvOperStateCh": tmnxRadSrvPlcySrvOperStateCh,
       "tmnxRadRouteDownloadFailed": tmnxRadRouteDownloadFailed,
       "tmnxRadAcctOnOngoing": tmnxRadAcctOnOngoing}
)
