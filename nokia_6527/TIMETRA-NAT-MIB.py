# SNMP MIB module (TIMETRA-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-NAT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:37 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
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

(TmnxChassisIndexOrZero,
 TmnxSlotNumOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndexOrZero",
    "TmnxSlotNumOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

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

(tmnxSubInfoSubIdent,) = mibBuilder.importSymbols(
    "TIMETRA-SUBSCRIBER-MGMT-MIB",
    "tmnxSubInfoSubIdent")

(TFCSet,
 TIpProtocol,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxDisplayStringURL,
 TmnxEnabledDisabled,
 TmnxNatSubscriberType,
 TmnxOperState,
 TmnxSubRadServAlgorithm,
 TmnxSubRadiusAttrType,
 TmnxSubRadiusVendorId,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TFCSet",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxDisplayStringURL",
    "TmnxEnabledDisabled",
    "TmnxNatSubscriberType",
    "TmnxOperState",
    "TmnxSubRadServAlgorithm",
    "TmnxSubRadiusAttrType",
    "TmnxSubRadiusVendorId",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraNatMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 65)
)
if mibBuilder.loadTexts:
    timetraNatMIBModule.setRevisions(
        ("2014-02-01 00:00",
         "2012-08-01 00:00",
         "2011-02-01 00:00",
         "2009-07-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxNatAlgProtocols(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ftp", 0),
          ("rtsp", 1),
          ("sip", 2),
          ("pptp", 3))
    )


class TmnxNatFiltering(TextualConvention, Integer32):
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
        *(("endpointIndependent", 0),
          ("addressDependent", 1),
          ("addressAndPortDependent", 2))
    )



class TmnxNatFragmentIpMode(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("fragmentIpv6", 1),
          ("fragmentIpv6UnlessIpv4DfSet", 2))
    )



class TmnxNatFwdActionType(TextualConvention, Integer32):
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
        *(("create", 1),
          ("modify", 2),
          ("destroy", 3))
    )



class TmnxNatIsaGrpId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class TmnxNatIsaGrpIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class TmnxNatIsaMdaOperState(TextualConvention, Integer32):
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



class TmnxNatMode(TextualConvention, Integer32):
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
        *(("auto", 0),
          ("napt", 1),
          ("oneToOne", 2))
    )



class TmnxNatFwdEntryDescription(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxNatPlType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("largeScale", 1),
          ("l2Aware", 2),
          ("wlanGwAnchor", 3))
    )



class TmnxNatSubscriberIdString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxNatUsageLevel(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TmnxNatUsageStatsType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("hostsActive", 1),
          ("hostsPeak", 2),
          ("sessionsTcpCreated", 3),
          ("sessionsTcpDestroyed", 4),
          ("sessionsUdpCreated", 5),
          ("sessionsUdpDestroyed", 6),
          ("sessionsIcmpQueryCreated", 7),
          ("sessionsIcmpQueryDestroyed", 8),
          ("sessionsGreQueryCreated", 9),
          ("sessionsGreQueryDestroyed", 10))
    )



class TmnxNatWaterMark(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxNatConformance_ObjectIdentity = ObjectIdentity
tmnxNatConformance = _TmnxNatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65)
)
_TmnxNatCompliances_ObjectIdentity = ObjectIdentity
tmnxNatCompliances = _TmnxNatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1)
)
_TmnxNatGroups_ObjectIdentity = ObjectIdentity
tmnxNatGroups = _TmnxNatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2)
)
_TmnxNat_ObjectIdentity = ObjectIdentity
tmnxNat = _TmnxNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65)
)
_TmnxNatObjs_ObjectIdentity = ObjectIdentity
tmnxNatObjs = _TmnxNatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1)
)
_TmnxNatIsaObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaObjs = _TmnxNatIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1)
)
_TmnxNatIsaGrpObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaGrpObjs = _TmnxNatIsaGrpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1)
)
_TmnxNatIsaGrpTable_Object = MibTable
tmnxNatIsaGrpTable = _TmnxNatIsaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpTable.setStatus("current")
_TmnxNatIsaGrpEntry_Object = MibTableRow
tmnxNatIsaGrpEntry = _TmnxNatIsaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1)
)
tmnxNatIsaGrpEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpEntry.setStatus("current")
_TmnxNatIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatIsaGrpId_Object = MibTableColumn
tmnxNatIsaGrpId = _TmnxNatIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 1),
    _TmnxNatIsaGrpId_Type()
)
tmnxNatIsaGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpId.setStatus("current")
_TmnxNatIsaGrpRowStatus_Type = RowStatus
_TmnxNatIsaGrpRowStatus_Object = MibTableColumn
tmnxNatIsaGrpRowStatus = _TmnxNatIsaGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 2),
    _TmnxNatIsaGrpRowStatus_Type()
)
tmnxNatIsaGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpRowStatus.setStatus("current")
_TmnxNatIsaGrpLastMgmtChange_Type = TimeStamp
_TmnxNatIsaGrpLastMgmtChange_Object = MibTableColumn
tmnxNatIsaGrpLastMgmtChange = _TmnxNatIsaGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 3),
    _TmnxNatIsaGrpLastMgmtChange_Type()
)
tmnxNatIsaGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpLastMgmtChange.setStatus("current")


class _TmnxNatIsaGrpDescription_Type(TItemDescription):
    """Custom type tmnxNatIsaGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatIsaGrpDescription_Type.__name__ = "TItemDescription"
_TmnxNatIsaGrpDescription_Object = MibTableColumn
tmnxNatIsaGrpDescription = _TmnxNatIsaGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 4),
    _TmnxNatIsaGrpDescription_Type()
)
tmnxNatIsaGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpDescription.setStatus("current")


class _TmnxNatIsaGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatIsaGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatIsaGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatIsaGrpAdminState_Object = MibTableColumn
tmnxNatIsaGrpAdminState = _TmnxNatIsaGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 5),
    _TmnxNatIsaGrpAdminState_Type()
)
tmnxNatIsaGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpAdminState.setStatus("current")


class _TmnxNatIsaGrpActiveMdaLimit_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpActiveMdaLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxNatIsaGrpActiveMdaLimit_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpActiveMdaLimit_Object = MibTableColumn
tmnxNatIsaGrpActiveMdaLimit = _TmnxNatIsaGrpActiveMdaLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 6),
    _TmnxNatIsaGrpActiveMdaLimit_Type()
)
tmnxNatIsaGrpActiveMdaLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpActiveMdaLimit.setStatus("current")


class _TmnxNatIsaGrpSessionResvCount_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSessionResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6291456),
    )


_TmnxNatIsaGrpSessionResvCount_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSessionResvCount_Object = MibTableColumn
tmnxNatIsaGrpSessionResvCount = _TmnxNatIsaGrpSessionResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 7),
    _TmnxNatIsaGrpSessionResvCount_Type()
)
tmnxNatIsaGrpSessionResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSessionResvCount.setStatus("obsolete")


class _TmnxNatIsaGrpSessionWatermarkHi_Type(TmnxNatWaterMark):
    """Custom type tmnxNatIsaGrpSessionWatermarkHi based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatIsaGrpSessionWatermarkHi_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatIsaGrpSessionWatermarkHi_Object = MibTableColumn
tmnxNatIsaGrpSessionWatermarkHi = _TmnxNatIsaGrpSessionWatermarkHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 8),
    _TmnxNatIsaGrpSessionWatermarkHi_Type()
)
tmnxNatIsaGrpSessionWatermarkHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSessionWatermarkHi.setStatus("obsolete")


class _TmnxNatIsaGrpSessionWatermarkLo_Type(TmnxNatWaterMark):
    """Custom type tmnxNatIsaGrpSessionWatermarkLo based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatIsaGrpSessionWatermarkLo_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatIsaGrpSessionWatermarkLo_Object = MibTableColumn
tmnxNatIsaGrpSessionWatermarkLo = _TmnxNatIsaGrpSessionWatermarkLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 9),
    _TmnxNatIsaGrpSessionWatermarkLo_Type()
)
tmnxNatIsaGrpSessionWatermarkLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSessionWatermarkLo.setStatus("obsolete")
_TmnxNatIsaGrpOperState_Type = TmnxOperState
_TmnxNatIsaGrpOperState_Object = MibTableColumn
tmnxNatIsaGrpOperState = _TmnxNatIsaGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 50),
    _TmnxNatIsaGrpOperState_Type()
)
tmnxNatIsaGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpOperState.setStatus("current")
_TmnxNatIsaGrpDegraded_Type = TruthValue
_TmnxNatIsaGrpDegraded_Object = MibTableColumn
tmnxNatIsaGrpDegraded = _TmnxNatIsaGrpDegraded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 51),
    _TmnxNatIsaGrpDegraded_Type()
)
tmnxNatIsaGrpDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpDegraded.setStatus("current")
_TmnxNatGrpCfgTable_Object = MibTable
tmnxNatGrpCfgTable = _TmnxNatGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxNatGrpCfgTable.setStatus("current")
_TmnxNatGrpCfgEntry_Object = MibTableRow
tmnxNatGrpCfgEntry = _TmnxNatGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1)
)
tmnxNatGrpCfgEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatGrpCfgId"),
)
if mibBuilder.loadTexts:
    tmnxNatGrpCfgEntry.setStatus("current")
_TmnxNatGrpCfgId_Type = TmnxNatIsaGrpId
_TmnxNatGrpCfgId_Object = MibTableColumn
tmnxNatGrpCfgId = _TmnxNatGrpCfgId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 1),
    _TmnxNatGrpCfgId_Type()
)
tmnxNatGrpCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgId.setStatus("current")
_TmnxNatGrpCfgLastMgmtChange_Type = TimeStamp
_TmnxNatGrpCfgLastMgmtChange_Object = MibTableColumn
tmnxNatGrpCfgLastMgmtChange = _TmnxNatGrpCfgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 2),
    _TmnxNatGrpCfgLastMgmtChange_Type()
)
tmnxNatGrpCfgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLastMgmtChange.setStatus("current")


class _TmnxNatGrpCfgSessionResvCount_Type(Unsigned32):
    """Custom type tmnxNatGrpCfgSessionResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6291456),
    )


_TmnxNatGrpCfgSessionResvCount_Type.__name__ = "Unsigned32"
_TmnxNatGrpCfgSessionResvCount_Object = MibTableColumn
tmnxNatGrpCfgSessionResvCount = _TmnxNatGrpCfgSessionResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 3),
    _TmnxNatGrpCfgSessionResvCount_Type()
)
tmnxNatGrpCfgSessionResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionResvCount.setStatus("current")


class _TmnxNatGrpCfgSessionWatermarkHi_Type(TmnxNatWaterMark):
    """Custom type tmnxNatGrpCfgSessionWatermarkHi based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatGrpCfgSessionWatermarkHi_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatGrpCfgSessionWatermarkHi_Object = MibTableColumn
tmnxNatGrpCfgSessionWatermarkHi = _TmnxNatGrpCfgSessionWatermarkHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 4),
    _TmnxNatGrpCfgSessionWatermarkHi_Type()
)
tmnxNatGrpCfgSessionWatermarkHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionWatermarkHi.setStatus("current")


class _TmnxNatGrpCfgSessionWatermarkLo_Type(TmnxNatWaterMark):
    """Custom type tmnxNatGrpCfgSessionWatermarkLo based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatGrpCfgSessionWatermarkLo_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatGrpCfgSessionWatermarkLo_Object = MibTableColumn
tmnxNatGrpCfgSessionWatermarkLo = _TmnxNatGrpCfgSessionWatermarkLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 5),
    _TmnxNatGrpCfgSessionWatermarkLo_Type()
)
tmnxNatGrpCfgSessionWatermarkLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionWatermarkLo.setStatus("current")


class _TmnxNatGrpCfgAccountingPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatGrpCfgAccountingPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatGrpCfgAccountingPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatGrpCfgAccountingPlcy_Object = MibTableColumn
tmnxNatGrpCfgAccountingPlcy = _TmnxNatGrpCfgAccountingPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 6),
    _TmnxNatGrpCfgAccountingPlcy_Type()
)
tmnxNatGrpCfgAccountingPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgAccountingPlcy.setStatus("current")
_TmnxNatIsaMdaObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaMdaObjs = _TmnxNatIsaMdaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2)
)
_TmnxNatIsaMdaTable_Object = MibTable
tmnxNatIsaMdaTable = _TmnxNatIsaMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaTable.setStatus("current")
_TmnxNatIsaMdaEntry_Object = MibTableRow
tmnxNatIsaMdaEntry = _TmnxNatIsaMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1, 1)
)
tmnxNatIsaMdaEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaEntry.setStatus("current")
_TmnxNatIsaMdaRowStatus_Type = RowStatus
_TmnxNatIsaMdaRowStatus_Object = MibTableColumn
tmnxNatIsaMdaRowStatus = _TmnxNatIsaMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1, 1, 1),
    _TmnxNatIsaMdaRowStatus_Type()
)
tmnxNatIsaMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaRowStatus.setStatus("current")
_TmnxNatIsaMdaLastMgmtChange_Type = TimeStamp
_TmnxNatIsaMdaLastMgmtChange_Object = MibTableColumn
tmnxNatIsaMdaLastMgmtChange = _TmnxNatIsaMdaLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1, 1, 2),
    _TmnxNatIsaMdaLastMgmtChange_Type()
)
tmnxNatIsaMdaLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaLastMgmtChange.setStatus("current")
_TmnxNatIsaMdaStatObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaMdaStatObjs = _TmnxNatIsaMdaStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3)
)
_TmnxNatIsaMdaStatTable_Object = MibTable
tmnxNatIsaMdaStatTable = _TmnxNatIsaMdaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatTable.setStatus("current")
_TmnxNatIsaMdaStatEntry_Object = MibTableRow
tmnxNatIsaMdaStatEntry = _TmnxNatIsaMdaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatEntry.setStatus("current")
_TmnxNatIsaMdaStatOperState_Type = TmnxNatIsaMdaOperState
_TmnxNatIsaMdaStatOperState_Object = MibTableColumn
tmnxNatIsaMdaStatOperState = _TmnxNatIsaMdaStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1, 1, 1),
    _TmnxNatIsaMdaStatOperState_Type()
)
tmnxNatIsaMdaStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatOperState.setStatus("current")
_TmnxNatIsaMemberTable_Object = MibTable
tmnxNatIsaMemberTable = _TmnxNatIsaMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberTable.setStatus("current")
_TmnxNatIsaMemberEntry_Object = MibTableRow
tmnxNatIsaMemberEntry = _TmnxNatIsaMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1)
)
tmnxNatIsaMemberEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberEntry.setStatus("current")
_TmnxNatIsaMemberId_Type = Unsigned32
_TmnxNatIsaMemberId_Object = MibTableColumn
tmnxNatIsaMemberId = _TmnxNatIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 1),
    _TmnxNatIsaMemberId_Type()
)
tmnxNatIsaMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberId.setStatus("current")


class _TmnxNatIsaMemberMdaState_Type(Integer32):
    """Custom type tmnxNatIsaMemberMdaState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("needsReset", 3),
          ("resetting", 4),
          ("needsReconcile", 5),
          ("reconciling", 6),
          ("needsAudit", 7),
          ("auditing", 8))
    )


_TmnxNatIsaMemberMdaState_Type.__name__ = "Integer32"
_TmnxNatIsaMemberMdaState_Object = MibTableColumn
tmnxNatIsaMemberMdaState = _TmnxNatIsaMemberMdaState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 2),
    _TmnxNatIsaMemberMdaState_Type()
)
tmnxNatIsaMemberMdaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaState.setStatus("current")
_TmnxNatIsaMemberMdaChassisIndex_Type = TmnxChassisIndexOrZero
_TmnxNatIsaMemberMdaChassisIndex_Object = MibTableColumn
tmnxNatIsaMemberMdaChassisIndex = _TmnxNatIsaMemberMdaChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 3),
    _TmnxNatIsaMemberMdaChassisIndex_Type()
)
tmnxNatIsaMemberMdaChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaChassisIndex.setStatus("current")
_TmnxNatIsaMemberMdaCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxNatIsaMemberMdaCardSlotNum_Object = MibTableColumn
tmnxNatIsaMemberMdaCardSlotNum = _TmnxNatIsaMemberMdaCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 4),
    _TmnxNatIsaMemberMdaCardSlotNum_Type()
)
tmnxNatIsaMemberMdaCardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaCardSlotNum.setStatus("current")
_TmnxNatIsaMemberMdaSlotNum_Type = Unsigned32
_TmnxNatIsaMemberMdaSlotNum_Object = MibTableColumn
tmnxNatIsaMemberMdaSlotNum = _TmnxNatIsaMemberMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 5),
    _TmnxNatIsaMemberMdaSlotNum_Type()
)
tmnxNatIsaMemberMdaSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaSlotNum.setStatus("current")
_TmnxNatIsaMemberIpAddrReserved_Type = Gauge32
_TmnxNatIsaMemberIpAddrReserved_Object = MibTableColumn
tmnxNatIsaMemberIpAddrReserved = _TmnxNatIsaMemberIpAddrReserved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 6),
    _TmnxNatIsaMemberIpAddrReserved_Type()
)
tmnxNatIsaMemberIpAddrReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberIpAddrReserved.setStatus("current")
_TmnxNatIsaMemberBlocksReserved_Type = Gauge32
_TmnxNatIsaMemberBlocksReserved_Object = MibTableColumn
tmnxNatIsaMemberBlocksReserved = _TmnxNatIsaMemberBlocksReserved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 7),
    _TmnxNatIsaMemberBlocksReserved_Type()
)
tmnxNatIsaMemberBlocksReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberBlocksReserved.setStatus("current")
_TmnxNatIsaMemberSessionUsage_Type = TmnxNatUsageLevel
_TmnxNatIsaMemberSessionUsage_Object = MibTableColumn
tmnxNatIsaMemberSessionUsage = _TmnxNatIsaMemberSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 8),
    _TmnxNatIsaMemberSessionUsage_Type()
)
tmnxNatIsaMemberSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionUsage.setStatus("current")
_TmnxNatIsaMemberSessionUsageHi_Type = TruthValue
_TmnxNatIsaMemberSessionUsageHi_Object = MibTableColumn
tmnxNatIsaMemberSessionUsageHi = _TmnxNatIsaMemberSessionUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 9),
    _TmnxNatIsaMemberSessionUsageHi_Type()
)
tmnxNatIsaMemberSessionUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionUsageHi.setStatus("current")
_TmnxNatIsaMemberSessionsPrio_Type = Gauge32
_TmnxNatIsaMemberSessionsPrio_Object = MibTableColumn
tmnxNatIsaMemberSessionsPrio = _TmnxNatIsaMemberSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 10),
    _TmnxNatIsaMemberSessionsPrio_Type()
)
tmnxNatIsaMemberSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionsPrio.setStatus("current")
_TmnxNatIsaMemberStatsTable_Object = MibTable
tmnxNatIsaMemberStatsTable = _TmnxNatIsaMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsTable.setStatus("current")
_TmnxNatIsaMemberStatsEntry_Object = MibTableRow
tmnxNatIsaMemberStatsEntry = _TmnxNatIsaMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1)
)
tmnxNatIsaMemberStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsEntry.setStatus("current")


class _TmnxNatIsaMemberStatsType_Type(Unsigned32):
    """Custom type tmnxNatIsaMemberStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )


_TmnxNatIsaMemberStatsType_Type.__name__ = "Unsigned32"
_TmnxNatIsaMemberStatsType_Object = MibTableColumn
tmnxNatIsaMemberStatsType = _TmnxNatIsaMemberStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 1),
    _TmnxNatIsaMemberStatsType_Type()
)
tmnxNatIsaMemberStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsType.setStatus("current")


class _TmnxNatIsaMemberStatsName_Type(DisplayString):
    """Custom type tmnxNatIsaMemberStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatIsaMemberStatsName_Type.__name__ = "DisplayString"
_TmnxNatIsaMemberStatsName_Object = MibTableColumn
tmnxNatIsaMemberStatsName = _TmnxNatIsaMemberStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 2),
    _TmnxNatIsaMemberStatsName_Type()
)
tmnxNatIsaMemberStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsName.setStatus("current")
_TmnxNatIsaMemberStatsVal_Type = Counter32
_TmnxNatIsaMemberStatsVal_Object = MibTableColumn
tmnxNatIsaMemberStatsVal = _TmnxNatIsaMemberStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 3),
    _TmnxNatIsaMemberStatsVal_Type()
)
tmnxNatIsaMemberStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsVal.setStatus("current")
_TmnxNatIsaMemberStatsValHw_Type = Counter32
_TmnxNatIsaMemberStatsValHw_Object = MibTableColumn
tmnxNatIsaMemberStatsValHw = _TmnxNatIsaMemberStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 4),
    _TmnxNatIsaMemberStatsValHw_Type()
)
tmnxNatIsaMemberStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsValHw.setStatus("current")
_TmnxNatIsaMemberStatsValue_Type = Counter64
_TmnxNatIsaMemberStatsValue_Object = MibTableColumn
tmnxNatIsaMemberStatsValue = _TmnxNatIsaMemberStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 5),
    _TmnxNatIsaMemberStatsValue_Type()
)
tmnxNatIsaMemberStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsValue.setStatus("current")
_TmnxNatIsaResrcStatsTable_Object = MibTable
tmnxNatIsaResrcStatsTable = _TmnxNatIsaResrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsTable.setStatus("current")
_TmnxNatIsaResrcStatsEntry_Object = MibTableRow
tmnxNatIsaResrcStatsEntry = _TmnxNatIsaResrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1)
)
tmnxNatIsaResrcStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsEntry.setStatus("current")


class _TmnxNatIsaResrcStatsId_Type(Unsigned32):
    """Custom type tmnxNatIsaResrcStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_TmnxNatIsaResrcStatsId_Type.__name__ = "Unsigned32"
_TmnxNatIsaResrcStatsId_Object = MibTableColumn
tmnxNatIsaResrcStatsId = _TmnxNatIsaResrcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 1),
    _TmnxNatIsaResrcStatsId_Type()
)
tmnxNatIsaResrcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsId.setStatus("current")


class _TmnxNatIsaResrcStatsName_Type(DisplayString):
    """Custom type tmnxNatIsaResrcStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatIsaResrcStatsName_Type.__name__ = "DisplayString"
_TmnxNatIsaResrcStatsName_Object = MibTableColumn
tmnxNatIsaResrcStatsName = _TmnxNatIsaResrcStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 2),
    _TmnxNatIsaResrcStatsName_Type()
)
tmnxNatIsaResrcStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsName.setStatus("current")
_TmnxNatIsaResrcStatsValMax_Type = CounterBasedGauge64
_TmnxNatIsaResrcStatsValMax_Object = MibTableColumn
tmnxNatIsaResrcStatsValMax = _TmnxNatIsaResrcStatsValMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 3),
    _TmnxNatIsaResrcStatsValMax_Type()
)
tmnxNatIsaResrcStatsValMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValMax.setStatus("current")
_TmnxNatIsaResrcStatsValMaxLw_Type = Gauge32
_TmnxNatIsaResrcStatsValMaxLw_Object = MibTableColumn
tmnxNatIsaResrcStatsValMaxLw = _TmnxNatIsaResrcStatsValMaxLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 4),
    _TmnxNatIsaResrcStatsValMaxLw_Type()
)
tmnxNatIsaResrcStatsValMaxLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValMaxLw.setStatus("current")
_TmnxNatIsaResrcStatsValMaxHw_Type = Gauge32
_TmnxNatIsaResrcStatsValMaxHw_Object = MibTableColumn
tmnxNatIsaResrcStatsValMaxHw = _TmnxNatIsaResrcStatsValMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 5),
    _TmnxNatIsaResrcStatsValMaxHw_Type()
)
tmnxNatIsaResrcStatsValMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValMaxHw.setStatus("current")
_TmnxNatIsaResrcStatsVal_Type = CounterBasedGauge64
_TmnxNatIsaResrcStatsVal_Object = MibTableColumn
tmnxNatIsaResrcStatsVal = _TmnxNatIsaResrcStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 6),
    _TmnxNatIsaResrcStatsVal_Type()
)
tmnxNatIsaResrcStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsVal.setStatus("current")
_TmnxNatIsaResrcStatsValLw_Type = Gauge32
_TmnxNatIsaResrcStatsValLw_Object = MibTableColumn
tmnxNatIsaResrcStatsValLw = _TmnxNatIsaResrcStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 7),
    _TmnxNatIsaResrcStatsValLw_Type()
)
tmnxNatIsaResrcStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValLw.setStatus("current")
_TmnxNatIsaResrcStatsValHw_Type = Gauge32
_TmnxNatIsaResrcStatsValHw_Object = MibTableColumn
tmnxNatIsaResrcStatsValHw = _TmnxNatIsaResrcStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 8),
    _TmnxNatIsaResrcStatsValHw_Type()
)
tmnxNatIsaResrcStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValHw.setStatus("current")
_TmnxNatReassemblyStatsTable_Object = MibTable
tmnxNatReassemblyStatsTable = _TmnxNatReassemblyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsTable.setStatus("current")
_TmnxNatReassemblyStatsEntry_Object = MibTableRow
tmnxNatReassemblyStatsEntry = _TmnxNatReassemblyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1)
)
tmnxNatReassemblyStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsEntry.setStatus("current")


class _TmnxNatReassemblyStatsType_Type(Unsigned32):
    """Custom type tmnxNatReassemblyStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_TmnxNatReassemblyStatsType_Type.__name__ = "Unsigned32"
_TmnxNatReassemblyStatsType_Object = MibTableColumn
tmnxNatReassemblyStatsType = _TmnxNatReassemblyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 1),
    _TmnxNatReassemblyStatsType_Type()
)
tmnxNatReassemblyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsType.setStatus("current")


class _TmnxNatReassemblyStatsName_Type(DisplayString):
    """Custom type tmnxNatReassemblyStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatReassemblyStatsName_Type.__name__ = "DisplayString"
_TmnxNatReassemblyStatsName_Object = MibTableColumn
tmnxNatReassemblyStatsName = _TmnxNatReassemblyStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 2),
    _TmnxNatReassemblyStatsName_Type()
)
tmnxNatReassemblyStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsName.setStatus("current")
_TmnxNatReassemblyStatsVal_Type = Counter64
_TmnxNatReassemblyStatsVal_Object = MibTableColumn
tmnxNatReassemblyStatsVal = _TmnxNatReassemblyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 3),
    _TmnxNatReassemblyStatsVal_Type()
)
tmnxNatReassemblyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsVal.setStatus("current")
_TmnxNatReassemblyStatsValLw_Type = Counter32
_TmnxNatReassemblyStatsValLw_Object = MibTableColumn
tmnxNatReassemblyStatsValLw = _TmnxNatReassemblyStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 4),
    _TmnxNatReassemblyStatsValLw_Type()
)
tmnxNatReassemblyStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsValLw.setStatus("current")
_TmnxNatReassemblyStatsValHw_Type = Counter32
_TmnxNatReassemblyStatsValHw_Object = MibTableColumn
tmnxNatReassemblyStatsValHw = _TmnxNatReassemblyStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 5),
    _TmnxNatReassemblyStatsValHw_Type()
)
tmnxNatReassemblyStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsValHw.setStatus("current")
_TmnxNatPlcyObjs_ObjectIdentity = ObjectIdentity
tmnxNatPlcyObjs = _TmnxNatPlcyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2)
)
_TmnxNatPlcyTable_Object = MibTable
tmnxNatPlcyTable = _TmnxNatPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPlcyTable.setStatus("current")
_TmnxNatPlcyEntry_Object = MibTableRow
tmnxNatPlcyEntry = _TmnxNatPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1)
)
tmnxNatPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlcyEntry.setStatus("current")
_TmnxNatPlcyName_Type = TNamedItem
_TmnxNatPlcyName_Object = MibTableColumn
tmnxNatPlcyName = _TmnxNatPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 1),
    _TmnxNatPlcyName_Type()
)
tmnxNatPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlcyName.setStatus("current")
_TmnxNatPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatPlcyLastMgmtChange = _TmnxNatPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 2),
    _TmnxNatPlcyLastMgmtChange_Type()
)
tmnxNatPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyLastMgmtChange.setStatus("current")
_TmnxNatPlcyRowStatus_Type = RowStatus
_TmnxNatPlcyRowStatus_Object = MibTableColumn
tmnxNatPlcyRowStatus = _TmnxNatPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 3),
    _TmnxNatPlcyRowStatus_Type()
)
tmnxNatPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyRowStatus.setStatus("current")


class _TmnxNatPlcyDescription_Type(TItemDescription):
    """Custom type tmnxNatPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxNatPlcyDescription_Object = MibTableColumn
tmnxNatPlcyDescription = _TmnxNatPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 4),
    _TmnxNatPlcyDescription_Type()
)
tmnxNatPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDescription.setStatus("current")


class _TmnxNatPlcyPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlcyPool based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatPlcyPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlcyPool_Object = MibTableColumn
tmnxNatPlcyPool = _TmnxNatPlcyPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 5),
    _TmnxNatPlcyPool_Type()
)
tmnxNatPlcyPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPool.setStatus("current")


class _TmnxNatPlcyPoolVRtr_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPlcyPoolVRtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPlcyPoolVRtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPlcyPoolVRtr_Object = MibTableColumn
tmnxNatPlcyPoolVRtr = _TmnxNatPlcyPoolVRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 6),
    _TmnxNatPlcyPoolVRtr_Type()
)
tmnxNatPlcyPoolVRtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPoolVRtr.setStatus("current")


class _TmnxNatPlcyFiltering_Type(TmnxNatFiltering):
    """Custom type tmnxNatPlcyFiltering based on TmnxNatFiltering"""
    defaultValue = 0


_TmnxNatPlcyFiltering_Type.__name__ = "TmnxNatFiltering"
_TmnxNatPlcyFiltering_Object = MibTableColumn
tmnxNatPlcyFiltering = _TmnxNatPlcyFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 7),
    _TmnxNatPlcyFiltering_Type()
)
tmnxNatPlcyFiltering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyFiltering.setStatus("current")


class _TmnxNatPlcyPortResvCount_Type(Unsigned32):
    """Custom type tmnxNatPlcyPortResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_TmnxNatPlcyPortResvCount_Type.__name__ = "Unsigned32"
_TmnxNatPlcyPortResvCount_Object = MibTableColumn
tmnxNatPlcyPortResvCount = _TmnxNatPlcyPortResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 8),
    _TmnxNatPlcyPortResvCount_Type()
)
tmnxNatPlcyPortResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortResvCount.setStatus("current")


class _TmnxNatPlcyPortWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcyPortWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlcyPortWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcyPortWatermarkHigh_Object = MibTableColumn
tmnxNatPlcyPortWatermarkHigh = _TmnxNatPlcyPortWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 9),
    _TmnxNatPlcyPortWatermarkHigh_Type()
)
tmnxNatPlcyPortWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortWatermarkHigh.setStatus("current")


class _TmnxNatPlcyPortWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcyPortWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlcyPortWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcyPortWatermarkLow_Object = MibTableColumn
tmnxNatPlcyPortWatermarkLow = _TmnxNatPlcyPortWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 10),
    _TmnxNatPlcyPortWatermarkLow_Type()
)
tmnxNatPlcyPortWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortWatermarkLow.setStatus("current")


class _TmnxNatPlcySessionLimit_Type(Unsigned32):
    """Custom type tmnxNatPlcySessionLimit based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatPlcySessionLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlcySessionLimit_Object = MibTableColumn
tmnxNatPlcySessionLimit = _TmnxNatPlcySessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 11),
    _TmnxNatPlcySessionLimit_Type()
)
tmnxNatPlcySessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionLimit.setStatus("current")


class _TmnxNatPlcySessionResvCount_Type(Unsigned32):
    """Custom type tmnxNatPlcySessionResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_TmnxNatPlcySessionResvCount_Type.__name__ = "Unsigned32"
_TmnxNatPlcySessionResvCount_Object = MibTableColumn
tmnxNatPlcySessionResvCount = _TmnxNatPlcySessionResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 12),
    _TmnxNatPlcySessionResvCount_Type()
)
tmnxNatPlcySessionResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionResvCount.setStatus("current")


class _TmnxNatPlcySessionWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcySessionWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlcySessionWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcySessionWatermarkHigh_Object = MibTableColumn
tmnxNatPlcySessionWatermarkHigh = _TmnxNatPlcySessionWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 13),
    _TmnxNatPlcySessionWatermarkHigh_Type()
)
tmnxNatPlcySessionWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionWatermarkHigh.setStatus("current")


class _TmnxNatPlcySessionWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcySessionWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlcySessionWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcySessionWatermarkLow_Object = MibTableColumn
tmnxNatPlcySessionWatermarkLow = _TmnxNatPlcySessionWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 14),
    _TmnxNatPlcySessionWatermarkLow_Type()
)
tmnxNatPlcySessionWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionWatermarkLow.setStatus("current")


class _TmnxNatPlcyPrioSessionFcSet_Type(TFCSet):
    """Custom type tmnxNatPlcyPrioSessionFcSet based on TFCSet"""
    defaultBinValue = "0"


_TmnxNatPlcyPrioSessionFcSet_Type.__name__ = "TFCSet"
_TmnxNatPlcyPrioSessionFcSet_Object = MibTableColumn
tmnxNatPlcyPrioSessionFcSet = _TmnxNatPlcyPrioSessionFcSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 15),
    _TmnxNatPlcyPrioSessionFcSet_Type()
)
tmnxNatPlcyPrioSessionFcSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPrioSessionFcSet.setStatus("current")


class _TmnxNatPlcyToTcpEstab_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpEstab based on Unsigned32"""
    defaultValue = 7440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToTcpEstab_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpEstab_Object = MibTableColumn
tmnxNatPlcyToTcpEstab = _TmnxNatPlcyToTcpEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 16),
    _TmnxNatPlcyToTcpEstab_Type()
)
tmnxNatPlcyToTcpEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpEstab.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpEstab.setUnits("seconds")


class _TmnxNatPlcyToTcpTrans_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpTrans based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToTcpTrans_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpTrans_Object = MibTableColumn
tmnxNatPlcyToTcpTrans = _TmnxNatPlcyToTcpTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 17),
    _TmnxNatPlcyToTcpTrans_Type()
)
tmnxNatPlcyToTcpTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTrans.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTrans.setUnits("seconds")


class _TmnxNatPlcyToTcpSyn_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpSyn based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 86400),
    )


_TmnxNatPlcyToTcpSyn_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpSyn_Object = MibTableColumn
tmnxNatPlcyToTcpSyn = _TmnxNatPlcyToTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 18),
    _TmnxNatPlcyToTcpSyn_Type()
)
tmnxNatPlcyToTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpSyn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpSyn.setUnits("seconds")


class _TmnxNatPlcyToTcpTimeWait_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpTimeWait based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TmnxNatPlcyToTcpTimeWait_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpTimeWait_Object = MibTableColumn
tmnxNatPlcyToTcpTimeWait = _TmnxNatPlcyToTcpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 19),
    _TmnxNatPlcyToTcpTimeWait_Type()
)
tmnxNatPlcyToTcpTimeWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTimeWait.setUnits("seconds")


class _TmnxNatPlcyToUdp_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUdp based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToUdp_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUdp_Object = MibTableColumn
tmnxNatPlcyToUdp = _TmnxNatPlcyToUdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 20),
    _TmnxNatPlcyToUdp_Type()
)
tmnxNatPlcyToUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdp.setUnits("seconds")


class _TmnxNatPlcyToUdpInitial_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUdpInitial based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TmnxNatPlcyToUdpInitial_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUdpInitial_Object = MibTableColumn
tmnxNatPlcyToUdpInitial = _TmnxNatPlcyToUdpInitial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 21),
    _TmnxNatPlcyToUdpInitial_Type()
)
tmnxNatPlcyToUdpInitial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpInitial.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpInitial.setUnits("seconds")


class _TmnxNatPlcyToUdpDns_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUdpDns based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_TmnxNatPlcyToUdpDns_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUdpDns_Object = MibTableColumn
tmnxNatPlcyToUdpDns = _TmnxNatPlcyToUdpDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 22),
    _TmnxNatPlcyToUdpDns_Type()
)
tmnxNatPlcyToUdpDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpDns.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpDns.setUnits("seconds")


class _TmnxNatPlcyToIcmpQuery_Type(Unsigned32):
    """Custom type tmnxNatPlcyToIcmpQuery based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 240),
    )


_TmnxNatPlcyToIcmpQuery_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToIcmpQuery_Object = MibTableColumn
tmnxNatPlcyToIcmpQuery = _TmnxNatPlcyToIcmpQuery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 23),
    _TmnxNatPlcyToIcmpQuery_Type()
)
tmnxNatPlcyToIcmpQuery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToIcmpQuery.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToIcmpQuery.setUnits("seconds")


class _TmnxNatPlcyBlkLimit_Type(Unsigned32):
    """Custom type tmnxNatPlcyBlkLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_TmnxNatPlcyBlkLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlcyBlkLimit_Object = MibTableColumn
tmnxNatPlcyBlkLimit = _TmnxNatPlcyBlkLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 25),
    _TmnxNatPlcyBlkLimit_Type()
)
tmnxNatPlcyBlkLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyBlkLimit.setStatus("current")


class _TmnxNatPlcyToSip_Type(Unsigned32):
    """Custom type tmnxNatPlcyToSip based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2550),
    )


_TmnxNatPlcyToSip_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToSip_Object = MibTableColumn
tmnxNatPlcyToSip = _TmnxNatPlcyToSip_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 26),
    _TmnxNatPlcyToSip_Type()
)
tmnxNatPlcyToSip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSip.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSip.setUnits("seconds")


class _TmnxNatPlcyAlgEnable_Type(TmnxNatAlgProtocols):
    """Custom type tmnxNatPlcyAlgEnable based on TmnxNatAlgProtocols"""
    defaultBinValue = "1"


_TmnxNatPlcyAlgEnable_Type.__name__ = "TmnxNatAlgProtocols"
_TmnxNatPlcyAlgEnable_Object = MibTableColumn
tmnxNatPlcyAlgEnable = _TmnxNatPlcyAlgEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 27),
    _TmnxNatPlcyAlgEnable_Type()
)
tmnxNatPlcyAlgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyAlgEnable.setStatus("current")


class _TmnxNatPlcyPortFwdLimit_Type(Unsigned32):
    """Custom type tmnxNatPlcyPortFwdLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TmnxNatPlcyPortFwdLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlcyPortFwdLimit_Object = MibTableColumn
tmnxNatPlcyPortFwdLimit = _TmnxNatPlcyPortFwdLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 28),
    _TmnxNatPlcyPortFwdLimit_Type()
)
tmnxNatPlcyPortFwdLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortFwdLimit.setStatus("current")


class _TmnxNatPlcyUdpInboundRefresh_Type(TruthValue):
    """Custom type tmnxNatPlcyUdpInboundRefresh based on TruthValue"""
    defaultValue = 2


_TmnxNatPlcyUdpInboundRefresh_Type.__name__ = "TruthValue"
_TmnxNatPlcyUdpInboundRefresh_Object = MibTableColumn
tmnxNatPlcyUdpInboundRefresh = _TmnxNatPlcyUdpInboundRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 29),
    _TmnxNatPlcyUdpInboundRefresh_Type()
)
tmnxNatPlcyUdpInboundRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyUdpInboundRefresh.setStatus("current")


class _TmnxNatPlcyDestNatAddrType_Type(InetAddressType):
    """Custom type tmnxNatPlcyDestNatAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatPlcyDestNatAddrType_Type.__name__ = "InetAddressType"
_TmnxNatPlcyDestNatAddrType_Object = MibTableColumn
tmnxNatPlcyDestNatAddrType = _TmnxNatPlcyDestNatAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 30),
    _TmnxNatPlcyDestNatAddrType_Type()
)
tmnxNatPlcyDestNatAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDestNatAddrType.setStatus("current")


class _TmnxNatPlcyDestNatAddr_Type(InetAddress):
    """Custom type tmnxNatPlcyDestNatAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlcyDestNatAddr_Type.__name__ = "InetAddress"
_TmnxNatPlcyDestNatAddr_Object = MibTableColumn
tmnxNatPlcyDestNatAddr = _TmnxNatPlcyDestNatAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 31),
    _TmnxNatPlcyDestNatAddr_Type()
)
tmnxNatPlcyDestNatAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDestNatAddr.setStatus("current")


class _TmnxNatPlcyDestNatPort_Type(InetPortNumber):
    """Custom type tmnxNatPlcyDestNatPort based on InetPortNumber"""
    defaultValue = 0


_TmnxNatPlcyDestNatPort_Type.__name__ = "InetPortNumber"
_TmnxNatPlcyDestNatPort_Object = MibTableColumn
tmnxNatPlcyDestNatPort = _TmnxNatPlcyDestNatPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 32),
    _TmnxNatPlcyDestNatPort_Type()
)
tmnxNatPlcyDestNatPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDestNatPort.setStatus("current")


class _TmnxNatPlcyIpfixExpPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlcyIpfixExpPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatPlcyIpfixExpPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlcyIpfixExpPlcy_Object = MibTableColumn
tmnxNatPlcyIpfixExpPlcy = _TmnxNatPlcyIpfixExpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 40),
    _TmnxNatPlcyIpfixExpPlcy_Type()
)
tmnxNatPlcyIpfixExpPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyIpfixExpPlcy.setStatus("current")


class _TmnxNatPlcyTcpMssAdjust_Type(Unsigned32):
    """Custom type tmnxNatPlcyTcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_TmnxNatPlcyTcpMssAdjust_Type.__name__ = "Unsigned32"
_TmnxNatPlcyTcpMssAdjust_Object = MibTableColumn
tmnxNatPlcyTcpMssAdjust = _TmnxNatPlcyTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 41),
    _TmnxNatPlcyTcpMssAdjust_Type()
)
tmnxNatPlcyTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyTcpMssAdjust.setUnits("bytes")


class _TmnxNatPlcyToSubRetention_Type(Unsigned32):
    """Custom type tmnxNatPlcyToSubRetention based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TmnxNatPlcyToSubRetention_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToSubRetention_Object = MibTableColumn
tmnxNatPlcyToSubRetention = _TmnxNatPlcyToSubRetention_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 42),
    _TmnxNatPlcyToSubRetention_Type()
)
tmnxNatPlcyToSubRetention.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSubRetention.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSubRetention.setUnits("minutes")
_TmnxNatPlcyStatsTable_Object = MibTable
tmnxNatPlcyStatsTable = _TmnxNatPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsTable.setStatus("current")
_TmnxNatPlcyStatsEntry_Object = MibTableRow
tmnxNatPlcyStatsEntry = _TmnxNatPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1)
)
tmnxNatPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsEntry.setStatus("current")
_TmnxNatPlcyStatsType_Type = TmnxNatUsageStatsType
_TmnxNatPlcyStatsType_Object = MibTableColumn
tmnxNatPlcyStatsType = _TmnxNatPlcyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1, 1),
    _TmnxNatPlcyStatsType_Type()
)
tmnxNatPlcyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsType.setStatus("current")


class _TmnxNatPlcyStatsName_Type(DisplayString):
    """Custom type tmnxNatPlcyStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatPlcyStatsName_Type.__name__ = "DisplayString"
_TmnxNatPlcyStatsName_Object = MibTableColumn
tmnxNatPlcyStatsName = _TmnxNatPlcyStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1, 2),
    _TmnxNatPlcyStatsName_Type()
)
tmnxNatPlcyStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsName.setStatus("current")
_TmnxNatPlcyStatsVal_Type = Gauge32
_TmnxNatPlcyStatsVal_Object = MibTableColumn
tmnxNatPlcyStatsVal = _TmnxNatPlcyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1, 3),
    _TmnxNatPlcyStatsVal_Type()
)
tmnxNatPlcyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsVal.setStatus("current")
_TmnxNatVrtrObjs_ObjectIdentity = ObjectIdentity
tmnxNatVrtrObjs = _TmnxNatVrtrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3)
)
_TmnxNatVrtrTable_Object = MibTable
tmnxNatVrtrTable = _TmnxNatVrtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatVrtrTable.setStatus("current")
_TmnxNatVrtrEntry_Object = MibTableRow
tmnxNatVrtrEntry = _TmnxNatVrtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1)
)
tmnxNatVrtrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxNatVrtrEntry.setStatus("current")
_TmnxNatVrtrLastMgmtChange_Type = TimeStamp
_TmnxNatVrtrLastMgmtChange_Object = MibTableColumn
tmnxNatVrtrLastMgmtChange = _TmnxNatVrtrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 1),
    _TmnxNatVrtrLastMgmtChange_Type()
)
tmnxNatVrtrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrLastMgmtChange.setStatus("current")
_TmnxNatVrtrRowStatus_Type = RowStatus
_TmnxNatVrtrRowStatus_Object = MibTableColumn
tmnxNatVrtrRowStatus = _TmnxNatVrtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 2),
    _TmnxNatVrtrRowStatus_Type()
)
tmnxNatVrtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrRowStatus.setStatus("current")


class _TmnxNatVrtrInPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatVrtrInPolicy_Object = MibTableColumn
tmnxNatVrtrInPolicy = _TmnxNatVrtrInPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 3),
    _TmnxNatVrtrInPolicy_Type()
)
tmnxNatVrtrInPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInPolicy.setStatus("current")


class _TmnxNatVrtrInDsliteAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatVrtrInDsliteAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatVrtrInDsliteAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatVrtrInDsliteAdminState_Object = MibTableColumn
tmnxNatVrtrInDsliteAdminState = _TmnxNatVrtrInDsliteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 4),
    _TmnxNatVrtrInDsliteAdminState_Type()
)
tmnxNatVrtrInDsliteAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInDsliteAdminState.setStatus("current")


class _TmnxNatVrtrInDsliteSubPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatVrtrInDsliteSubPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 128

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
        ValueRangeConstraint(128, 128),
    )


_TmnxNatVrtrInDsliteSubPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatVrtrInDsliteSubPrefixLen_Object = MibTableColumn
tmnxNatVrtrInDsliteSubPrefixLen = _TmnxNatVrtrInDsliteSubPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 5),
    _TmnxNatVrtrInDsliteSubPrefixLen_Type()
)
tmnxNatVrtrInDsliteSubPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInDsliteSubPrefixLen.setStatus("current")


class _TmnxNatVrtrInRedPeerAddrType_Type(InetAddressType):
    """Custom type tmnxNatVrtrInRedPeerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatVrtrInRedPeerAddrType_Type.__name__ = "InetAddressType"
_TmnxNatVrtrInRedPeerAddrType_Object = MibTableColumn
tmnxNatVrtrInRedPeerAddrType = _TmnxNatVrtrInRedPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 10),
    _TmnxNatVrtrInRedPeerAddrType_Type()
)
tmnxNatVrtrInRedPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeerAddrType.setStatus("current")


class _TmnxNatVrtrInRedPeerAddr_Type(InetAddress):
    """Custom type tmnxNatVrtrInRedPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatVrtrInRedPeerAddr_Type.__name__ = "InetAddress"
_TmnxNatVrtrInRedPeerAddr_Object = MibTableColumn
tmnxNatVrtrInRedPeerAddr = _TmnxNatVrtrInRedPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 11),
    _TmnxNatVrtrInRedPeerAddr_Type()
)
tmnxNatVrtrInRedPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeerAddr.setStatus("current")


class _TmnxNatVrtrInRedSteerRtType_Type(InetAddressType):
    """Custom type tmnxNatVrtrInRedSteerRtType based on InetAddressType"""
    defaultValue = 0


_TmnxNatVrtrInRedSteerRtType_Type.__name__ = "InetAddressType"
_TmnxNatVrtrInRedSteerRtType_Object = MibTableColumn
tmnxNatVrtrInRedSteerRtType = _TmnxNatVrtrInRedSteerRtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 12),
    _TmnxNatVrtrInRedSteerRtType_Type()
)
tmnxNatVrtrInRedSteerRtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedSteerRtType.setStatus("current")


class _TmnxNatVrtrInRedSteerRt_Type(InetAddress):
    """Custom type tmnxNatVrtrInRedSteerRt based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatVrtrInRedSteerRt_Type.__name__ = "InetAddress"
_TmnxNatVrtrInRedSteerRt_Object = MibTableColumn
tmnxNatVrtrInRedSteerRt = _TmnxNatVrtrInRedSteerRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 13),
    _TmnxNatVrtrInRedSteerRt_Type()
)
tmnxNatVrtrInRedSteerRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedSteerRt.setStatus("current")


class _TmnxNatVrtrInRedSteerRtLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatVrtrInRedSteerRtLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatVrtrInRedSteerRtLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatVrtrInRedSteerRtLen_Object = MibTableColumn
tmnxNatVrtrInRedSteerRtLen = _TmnxNatVrtrInRedSteerRtLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 14),
    _TmnxNatVrtrInRedSteerRtLen_Type()
)
tmnxNatVrtrInRedSteerRtLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedSteerRtLen.setStatus("current")


class _TmnxNatVrtrOutMtu_Type(Unsigned32):
    """Custom type tmnxNatVrtrOutMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxNatVrtrOutMtu_Type.__name__ = "Unsigned32"
_TmnxNatVrtrOutMtu_Object = MibTableColumn
tmnxNatVrtrOutMtu = _TmnxNatVrtrOutMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 15),
    _TmnxNatVrtrOutMtu_Type()
)
tmnxNatVrtrOutMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutMtu.setStatus("current")


class _TmnxNatVrtrOutUpstreamIPFilterId_Type(TIPFilterID):
    """Custom type tmnxNatVrtrOutUpstreamIPFilterId based on TIPFilterID"""
    defaultValue = 0


_TmnxNatVrtrOutUpstreamIPFilterId_Type.__name__ = "TIPFilterID"
_TmnxNatVrtrOutUpstreamIPFilterId_Object = MibTableColumn
tmnxNatVrtrOutUpstreamIPFilterId = _TmnxNatVrtrOutUpstreamIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 16),
    _TmnxNatVrtrOutUpstreamIPFilterId_Type()
)
tmnxNatVrtrOutUpstreamIPFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutUpstreamIPFilterId.setStatus("current")


class _TmnxNatVrtrInMaxDetSubscrLimit_Type(Unsigned32):
    """Custom type tmnxNatVrtrInMaxDetSubscrLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32768),
    )


_TmnxNatVrtrInMaxDetSubscrLimit_Type.__name__ = "Unsigned32"
_TmnxNatVrtrInMaxDetSubscrLimit_Object = MibTableColumn
tmnxNatVrtrInMaxDetSubscrLimit = _TmnxNatVrtrInMaxDetSubscrLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 20),
    _TmnxNatVrtrInMaxDetSubscrLimit_Type()
)
tmnxNatVrtrInMaxDetSubscrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInMaxDetSubscrLimit.setStatus("current")


class _TmnxNatVrtrInMaxDetSubLimitDsl_Type(Unsigned32):
    """Custom type tmnxNatVrtrInMaxDetSubLimitDsl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32768),
    )


_TmnxNatVrtrInMaxDetSubLimitDsl_Type.__name__ = "Unsigned32"
_TmnxNatVrtrInMaxDetSubLimitDsl_Object = MibTableColumn
tmnxNatVrtrInMaxDetSubLimitDsl = _TmnxNatVrtrInMaxDetSubLimitDsl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 21),
    _TmnxNatVrtrInMaxDetSubLimitDsl_Type()
)
tmnxNatVrtrInMaxDetSubLimitDsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInMaxDetSubLimitDsl.setStatus("current")


class _TmnxNatVrtrOutDnstreamIPFilterId_Type(TIPFilterID):
    """Custom type tmnxNatVrtrOutDnstreamIPFilterId based on TIPFilterID"""
    defaultValue = 0


_TmnxNatVrtrOutDnstreamIPFilterId_Type.__name__ = "TIPFilterID"
_TmnxNatVrtrOutDnstreamIPFilterId_Object = MibTableColumn
tmnxNatVrtrOutDnstreamIPFilterId = _TmnxNatVrtrOutDnstreamIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 22),
    _TmnxNatVrtrOutDnstreamIPFilterId_Type()
)
tmnxNatVrtrOutDnstreamIPFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutDnstreamIPFilterId.setStatus("current")


class _TmnxNatVrtrInRedPeer6AddrType_Type(InetAddressType):
    """Custom type tmnxNatVrtrInRedPeer6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatVrtrInRedPeer6AddrType_Type.__name__ = "InetAddressType"
_TmnxNatVrtrInRedPeer6AddrType_Object = MibTableColumn
tmnxNatVrtrInRedPeer6AddrType = _TmnxNatVrtrInRedPeer6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 23),
    _TmnxNatVrtrInRedPeer6AddrType_Type()
)
tmnxNatVrtrInRedPeer6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeer6AddrType.setStatus("current")


class _TmnxNatVrtrInRedPeer6Addr_Type(InetAddress):
    """Custom type tmnxNatVrtrInRedPeer6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatVrtrInRedPeer6Addr_Type.__name__ = "InetAddress"
_TmnxNatVrtrInRedPeer6Addr_Object = MibTableColumn
tmnxNatVrtrInRedPeer6Addr = _TmnxNatVrtrInRedPeer6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 24),
    _TmnxNatVrtrInRedPeer6Addr_Type()
)
tmnxNatVrtrInRedPeer6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeer6Addr.setStatus("current")
_TmnxNatL2AwAddrTable_Object = MibTable
tmnxNatL2AwAddrTable = _TmnxNatL2AwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrTable.setStatus("current")
_TmnxNatL2AwAddrEntry_Object = MibTableRow
tmnxNatL2AwAddrEntry = _TmnxNatL2AwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1)
)
tmnxNatL2AwAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrEntry.setStatus("current")
_TmnxNatL2AwAddrType_Type = InetAddressType
_TmnxNatL2AwAddrType_Object = MibTableColumn
tmnxNatL2AwAddrType = _TmnxNatL2AwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 1),
    _TmnxNatL2AwAddrType_Type()
)
tmnxNatL2AwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrType.setStatus("current")


class _TmnxNatL2AwAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwAddr_Object = MibTableColumn
tmnxNatL2AwAddr = _TmnxNatL2AwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 2),
    _TmnxNatL2AwAddr_Type()
)
tmnxNatL2AwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddr.setStatus("current")


class _TmnxNatL2AwAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatL2AwAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxNatL2AwAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatL2AwAddrPrefixLen_Object = MibTableColumn
tmnxNatL2AwAddrPrefixLen = _TmnxNatL2AwAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 3),
    _TmnxNatL2AwAddrPrefixLen_Type()
)
tmnxNatL2AwAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrPrefixLen.setStatus("current")
_TmnxNatL2AwAddrRowStatus_Type = RowStatus
_TmnxNatL2AwAddrRowStatus_Object = MibTableColumn
tmnxNatL2AwAddrRowStatus = _TmnxNatL2AwAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 4),
    _TmnxNatL2AwAddrRowStatus_Type()
)
tmnxNatL2AwAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrRowStatus.setStatus("current")
_TmnxNatL2AwAddrLastMgmtChange_Type = TimeStamp
_TmnxNatL2AwAddrLastMgmtChange_Object = MibTableColumn
tmnxNatL2AwAddrLastMgmtChange = _TmnxNatL2AwAddrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 5),
    _TmnxNatL2AwAddrLastMgmtChange_Type()
)
tmnxNatL2AwAddrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrLastMgmtChange.setStatus("current")
_TmnxNat64Table_Object = MibTable
tmnxNat64Table = _TmnxNat64Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxNat64Table.setStatus("current")
_TmnxNat64Entry_Object = MibTableRow
tmnxNat64Entry = _TmnxNat64Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1)
)
tmnxNat64Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxNat64Entry.setStatus("current")
_TmnxNat64LastMgmtChange_Type = TimeStamp
_TmnxNat64LastMgmtChange_Object = MibTableColumn
tmnxNat64LastMgmtChange = _TmnxNat64LastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 1),
    _TmnxNat64LastMgmtChange_Type()
)
tmnxNat64LastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNat64LastMgmtChange.setStatus("current")
_TmnxNat64RowStatus_Type = RowStatus
_TmnxNat64RowStatus_Object = MibTableColumn
tmnxNat64RowStatus = _TmnxNat64RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 2),
    _TmnxNat64RowStatus_Type()
)
tmnxNat64RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64RowStatus.setStatus("current")


class _TmnxNat64InAdminState_Type(TmnxAdminState):
    """Custom type tmnxNat64InAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNat64InAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNat64InAdminState_Object = MibTableColumn
tmnxNat64InAdminState = _TmnxNat64InAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 3),
    _TmnxNat64InAdminState_Type()
)
tmnxNat64InAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InAdminState.setStatus("current")


class _TmnxNat64InSubPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNat64InSubPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 128

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
        ValueRangeConstraint(128, 128),
    )


_TmnxNat64InSubPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNat64InSubPrefixLen_Object = MibTableColumn
tmnxNat64InSubPrefixLen = _TmnxNat64InSubPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 4),
    _TmnxNat64InSubPrefixLen_Type()
)
tmnxNat64InSubPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InSubPrefixLen.setStatus("current")


class _TmnxNat64InPrefix_Type(InetAddressIPv6):
    """Custom type tmnxNat64InPrefix based on InetAddressIPv6"""
    defaultHexValue = "0064ff9b000000000000000000000000"


_TmnxNat64InPrefix_Type.__name__ = "InetAddressIPv6"
_TmnxNat64InPrefix_Object = MibTableColumn
tmnxNat64InPrefix = _TmnxNat64InPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 5),
    _TmnxNat64InPrefix_Type()
)
tmnxNat64InPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InPrefix.setStatus("current")


class _TmnxNat64InPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNat64InPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 96

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(96, 96),
    )


_TmnxNat64InPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNat64InPrefixLen_Object = MibTableColumn
tmnxNat64InPrefixLen = _TmnxNat64InPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 6),
    _TmnxNat64InPrefixLen_Type()
)
tmnxNat64InPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InPrefixLen.setStatus("current")


class _TmnxNat64InIpv6Mtu_Type(Unsigned32):
    """Custom type tmnxNat64InIpv6Mtu based on Unsigned32"""
    defaultValue = 1520

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 9212),
    )


_TmnxNat64InIpv6Mtu_Type.__name__ = "Unsigned32"
_TmnxNat64InIpv6Mtu_Object = MibTableColumn
tmnxNat64InIpv6Mtu = _TmnxNat64InIpv6Mtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 7),
    _TmnxNat64InIpv6Mtu_Type()
)
tmnxNat64InIpv6Mtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InIpv6Mtu.setStatus("current")


class _TmnxNat64InDropZeroIpv4Checksum_Type(TruthValue):
    """Custom type tmnxNat64InDropZeroIpv4Checksum based on TruthValue"""
    defaultValue = 2


_TmnxNat64InDropZeroIpv4Checksum_Type.__name__ = "TruthValue"
_TmnxNat64InDropZeroIpv4Checksum_Object = MibTableColumn
tmnxNat64InDropZeroIpv4Checksum = _TmnxNat64InDropZeroIpv4Checksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 8),
    _TmnxNat64InDropZeroIpv4Checksum_Type()
)
tmnxNat64InDropZeroIpv4Checksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InDropZeroIpv4Checksum.setStatus("current")


class _TmnxNat64InSetTos_Type(TruthValue):
    """Custom type tmnxNat64InSetTos based on TruthValue"""
    defaultValue = 2


_TmnxNat64InSetTos_Type.__name__ = "TruthValue"
_TmnxNat64InSetTos_Object = MibTableColumn
tmnxNat64InSetTos = _TmnxNat64InSetTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 9),
    _TmnxNat64InSetTos_Type()
)
tmnxNat64InSetTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InSetTos.setStatus("current")


class _TmnxNat64InTos_Type(Unsigned32):
    """Custom type tmnxNat64InTos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNat64InTos_Type.__name__ = "Unsigned32"
_TmnxNat64InTos_Object = MibTableColumn
tmnxNat64InTos = _TmnxNat64InTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 10),
    _TmnxNat64InTos_Type()
)
tmnxNat64InTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InTos.setStatus("current")


class _TmnxNat64InIgnoreTos_Type(TruthValue):
    """Custom type tmnxNat64InIgnoreTos based on TruthValue"""
    defaultValue = 2


_TmnxNat64InIgnoreTos_Type.__name__ = "TruthValue"
_TmnxNat64InIgnoreTos_Object = MibTableColumn
tmnxNat64InIgnoreTos = _TmnxNat64InIgnoreTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 11),
    _TmnxNat64InIgnoreTos_Type()
)
tmnxNat64InIgnoreTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InIgnoreTos.setStatus("current")


class _TmnxNat64InInsertIpv6FragHeader_Type(TruthValue):
    """Custom type tmnxNat64InInsertIpv6FragHeader based on TruthValue"""
    defaultValue = 2


_TmnxNat64InInsertIpv6FragHeader_Type.__name__ = "TruthValue"
_TmnxNat64InInsertIpv6FragHeader_Object = MibTableColumn
tmnxNat64InInsertIpv6FragHeader = _TmnxNat64InInsertIpv6FragHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 12),
    _TmnxNat64InInsertIpv6FragHeader_Type()
)
tmnxNat64InInsertIpv6FragHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InInsertIpv6FragHeader.setStatus("current")


class _TmnxNat64InFragmentIp_Type(TmnxNatFragmentIpMode):
    """Custom type tmnxNat64InFragmentIp based on TmnxNatFragmentIpMode"""
    defaultValue = 0


_TmnxNat64InFragmentIp_Type.__name__ = "TmnxNatFragmentIpMode"
_TmnxNat64InFragmentIp_Object = MibTableColumn
tmnxNat64InFragmentIp = _TmnxNat64InFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 15),
    _TmnxNat64InFragmentIp_Type()
)
tmnxNat64InFragmentIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InFragmentIp.setStatus("current")
_TmnxNatSubIdTable_Object = MibTable
tmnxNatSubIdTable = _TmnxNatSubIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxNatSubIdTable.setStatus("current")
_TmnxNatSubIdEntry_Object = MibTableRow
tmnxNatSubIdEntry = _TmnxNatSubIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxNatSubIdEntry.setStatus("current")
_TmnxNatSubIdLastMgmtChange_Type = TimeStamp
_TmnxNatSubIdLastMgmtChange_Object = MibTableColumn
tmnxNatSubIdLastMgmtChange = _TmnxNatSubIdLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 1),
    _TmnxNatSubIdLastMgmtChange_Type()
)
tmnxNatSubIdLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubIdLastMgmtChange.setStatus("current")


class _TmnxNatSubIdDescription_Type(TItemDescription):
    """Custom type tmnxNatSubIdDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatSubIdDescription_Type.__name__ = "TItemDescription"
_TmnxNatSubIdDescription_Object = MibTableColumn
tmnxNatSubIdDescription = _TmnxNatSubIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 2),
    _TmnxNatSubIdDescription_Type()
)
tmnxNatSubIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdDescription.setStatus("current")


class _TmnxNatSubIdAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatSubIdAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatSubIdAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatSubIdAdminState_Object = MibTableColumn
tmnxNatSubIdAdminState = _TmnxNatSubIdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 3),
    _TmnxNatSubIdAdminState_Type()
)
tmnxNatSubIdAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdAdminState.setStatus("current")


class _TmnxNatSubIdRadProxSrvRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatSubIdRadProxSrvRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatSubIdRadProxSrvRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatSubIdRadProxSrvRouter_Object = MibTableColumn
tmnxNatSubIdRadProxSrvRouter = _TmnxNatSubIdRadProxSrvRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 4),
    _TmnxNatSubIdRadProxSrvRouter_Type()
)
tmnxNatSubIdRadProxSrvRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadProxSrvRouter.setStatus("current")


class _TmnxNatSubIdRadProxSrvName_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatSubIdRadProxSrvName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatSubIdRadProxSrvName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatSubIdRadProxSrvName_Object = MibTableColumn
tmnxNatSubIdRadProxSrvName = _TmnxNatSubIdRadProxSrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 5),
    _TmnxNatSubIdRadProxSrvName_Type()
)
tmnxNatSubIdRadProxSrvName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadProxSrvName.setStatus("current")


class _TmnxNatSubIdRadiusAttributeType_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxNatSubIdRadiusAttributeType based on TmnxSubRadiusAttrType"""
    defaultValue = 11


_TmnxNatSubIdRadiusAttributeType_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxNatSubIdRadiusAttributeType_Object = MibTableColumn
tmnxNatSubIdRadiusAttributeType = _TmnxNatSubIdRadiusAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 6),
    _TmnxNatSubIdRadiusAttributeType_Type()
)
tmnxNatSubIdRadiusAttributeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadiusAttributeType.setStatus("current")


class _TmnxNatSubIdRadiusVendorId_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxNatSubIdRadiusVendorId based on TmnxSubRadiusVendorId"""
    defaultValue = 6527


_TmnxNatSubIdRadiusVendorId_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxNatSubIdRadiusVendorId_Object = MibTableColumn
tmnxNatSubIdRadiusVendorId = _TmnxNatSubIdRadiusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 7),
    _TmnxNatSubIdRadiusVendorId_Type()
)
tmnxNatSubIdRadiusVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadiusVendorId.setStatus("current")


class _TmnxNatSubIdDropUnidentified_Type(TruthValue):
    """Custom type tmnxNatSubIdDropUnidentified based on TruthValue"""
    defaultValue = 2


_TmnxNatSubIdDropUnidentified_Type.__name__ = "TruthValue"
_TmnxNatSubIdDropUnidentified_Object = MibTableColumn
tmnxNatSubIdDropUnidentified = _TmnxNatSubIdDropUnidentified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 8),
    _TmnxNatSubIdDropUnidentified_Type()
)
tmnxNatSubIdDropUnidentified.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdDropUnidentified.setStatus("current")
_TmnxNatDetPlcyTable_Object = MibTable
tmnxNatDetPlcyTable = _TmnxNatDetPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyTable.setStatus("current")
_TmnxNatDetPlcyEntry_Object = MibTableRow
tmnxNatDetPlcyEntry = _TmnxNatDetPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1)
)
tmnxNatDetPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcySubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyEntry.setStatus("current")
_TmnxNatDetPlcySubType_Type = TmnxNatSubscriberType
_TmnxNatDetPlcySubType_Object = MibTableColumn
tmnxNatDetPlcySubType = _TmnxNatDetPlcySubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 1),
    _TmnxNatDetPlcySubType_Type()
)
tmnxNatDetPlcySubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcySubType.setStatus("current")
_TmnxNatDetPlcyAddrType_Type = InetAddressType
_TmnxNatDetPlcyAddrType_Object = MibTableColumn
tmnxNatDetPlcyAddrType = _TmnxNatDetPlcyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 2),
    _TmnxNatDetPlcyAddrType_Type()
)
tmnxNatDetPlcyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAddrType.setStatus("current")


class _TmnxNatDetPlcyAddr_Type(InetAddress):
    """Custom type tmnxNatDetPlcyAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetPlcyAddr_Type.__name__ = "InetAddress"
_TmnxNatDetPlcyAddr_Object = MibTableColumn
tmnxNatDetPlcyAddr = _TmnxNatDetPlcyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 3),
    _TmnxNatDetPlcyAddr_Type()
)
tmnxNatDetPlcyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAddr.setStatus("current")


class _TmnxNatDetPlcyAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDetPlcyAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatDetPlcyAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDetPlcyAddrPrefixLength_Object = MibTableColumn
tmnxNatDetPlcyAddrPrefixLength = _TmnxNatDetPlcyAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 4),
    _TmnxNatDetPlcyAddrPrefixLength_Type()
)
tmnxNatDetPlcyAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAddrPrefixLength.setStatus("current")
_TmnxNatDetPlcyRowStatus_Type = RowStatus
_TmnxNatDetPlcyRowStatus_Object = MibTableColumn
tmnxNatDetPlcyRowStatus = _TmnxNatDetPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 5),
    _TmnxNatDetPlcyRowStatus_Type()
)
tmnxNatDetPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyRowStatus.setStatus("current")
_TmnxNatDetPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatDetPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatDetPlcyLastMgmtChange = _TmnxNatDetPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 6),
    _TmnxNatDetPlcyLastMgmtChange_Type()
)
tmnxNatDetPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyLastMgmtChange.setStatus("current")
_TmnxNatDetPlcyName_Type = TNamedItem
_TmnxNatDetPlcyName_Object = MibTableColumn
tmnxNatDetPlcyName = _TmnxNatDetPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 7),
    _TmnxNatDetPlcyName_Type()
)
tmnxNatDetPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyName.setStatus("current")


class _TmnxNatDetPlcyAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatDetPlcyAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatDetPlcyAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatDetPlcyAdminState_Object = MibTableColumn
tmnxNatDetPlcyAdminState = _TmnxNatDetPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 8),
    _TmnxNatDetPlcyAdminState_Type()
)
tmnxNatDetPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAdminState.setStatus("current")
_TmnxNatDetMapTable_Object = MibTable
tmnxNatDetMapTable = _TmnxNatDetMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxNatDetMapTable.setStatus("current")
_TmnxNatDetMapEntry_Object = MibTableRow
tmnxNatDetMapEntry = _TmnxNatDetMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1)
)
tmnxNatDetMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcySubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrPrefixLength"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMapInAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMapInStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMapInEnd"),
)
if mibBuilder.loadTexts:
    tmnxNatDetMapEntry.setStatus("current")
_TmnxNatDetMapInAddrType_Type = InetAddressType
_TmnxNatDetMapInAddrType_Object = MibTableColumn
tmnxNatDetMapInAddrType = _TmnxNatDetMapInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 1),
    _TmnxNatDetMapInAddrType_Type()
)
tmnxNatDetMapInAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMapInAddrType.setStatus("current")


class _TmnxNatDetMapInStart_Type(InetAddress):
    """Custom type tmnxNatDetMapInStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMapInStart_Type.__name__ = "InetAddress"
_TmnxNatDetMapInStart_Object = MibTableColumn
tmnxNatDetMapInStart = _TmnxNatDetMapInStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 2),
    _TmnxNatDetMapInStart_Type()
)
tmnxNatDetMapInStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMapInStart.setStatus("current")


class _TmnxNatDetMapInEnd_Type(InetAddress):
    """Custom type tmnxNatDetMapInEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMapInEnd_Type.__name__ = "InetAddress"
_TmnxNatDetMapInEnd_Object = MibTableColumn
tmnxNatDetMapInEnd = _TmnxNatDetMapInEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 3),
    _TmnxNatDetMapInEnd_Type()
)
tmnxNatDetMapInEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMapInEnd.setStatus("current")
_TmnxNatDetMapRowStatus_Type = RowStatus
_TmnxNatDetMapRowStatus_Object = MibTableColumn
tmnxNatDetMapRowStatus = _TmnxNatDetMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 4),
    _TmnxNatDetMapRowStatus_Type()
)
tmnxNatDetMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMapRowStatus.setStatus("current")
_TmnxNatDetMapLastCh_Type = TimeStamp
_TmnxNatDetMapLastCh_Object = MibTableColumn
tmnxNatDetMapLastCh = _TmnxNatDetMapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 5),
    _TmnxNatDetMapLastCh_Type()
)
tmnxNatDetMapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMapLastCh.setStatus("current")
_TmnxNatDetMapOutAddrType_Type = InetAddressType
_TmnxNatDetMapOutAddrType_Object = MibTableColumn
tmnxNatDetMapOutAddrType = _TmnxNatDetMapOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 6),
    _TmnxNatDetMapOutAddrType_Type()
)
tmnxNatDetMapOutAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMapOutAddrType.setStatus("current")


class _TmnxNatDetMapOutStart_Type(InetAddress):
    """Custom type tmnxNatDetMapOutStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMapOutStart_Type.__name__ = "InetAddress"
_TmnxNatDetMapOutStart_Object = MibTableColumn
tmnxNatDetMapOutStart = _TmnxNatDetMapOutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 7),
    _TmnxNatDetMapOutStart_Type()
)
tmnxNatDetMapOutStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMapOutStart.setStatus("current")
_TmnxNatPoolObjs_ObjectIdentity = ObjectIdentity
tmnxNatPoolObjs = _TmnxNatPoolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4)
)
_TmnxNatPlTable_Object = MibTable
tmnxNatPlTable = _TmnxNatPlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPlTable.setStatus("current")
_TmnxNatPlEntry_Object = MibTableRow
tmnxNatPlEntry = _TmnxNatPlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1)
)
tmnxNatPlEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlEntry.setStatus("current")
_TmnxNatPlName_Type = TNamedItem
_TmnxNatPlName_Object = MibTableColumn
tmnxNatPlName = _TmnxNatPlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 1),
    _TmnxNatPlName_Type()
)
tmnxNatPlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlName.setStatus("current")
_TmnxNatPlRowStatus_Type = RowStatus
_TmnxNatPlRowStatus_Object = MibTableColumn
tmnxNatPlRowStatus = _TmnxNatPlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 2),
    _TmnxNatPlRowStatus_Type()
)
tmnxNatPlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRowStatus.setStatus("current")
_TmnxNatPlLastMgmtChange_Type = TimeStamp
_TmnxNatPlLastMgmtChange_Object = MibTableColumn
tmnxNatPlLastMgmtChange = _TmnxNatPlLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 3),
    _TmnxNatPlLastMgmtChange_Type()
)
tmnxNatPlLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLastMgmtChange.setStatus("current")
_TmnxNatPlIsaGrp_Type = TmnxNatIsaGrpId
_TmnxNatPlIsaGrp_Object = MibTableColumn
tmnxNatPlIsaGrp = _TmnxNatPlIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 4),
    _TmnxNatPlIsaGrp_Type()
)
tmnxNatPlIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlIsaGrp.setStatus("current")
_TmnxNatPlType_Type = TmnxNatPlType
_TmnxNatPlType_Object = MibTableColumn
tmnxNatPlType = _TmnxNatPlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 5),
    _TmnxNatPlType_Type()
)
tmnxNatPlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlType.setStatus("current")


class _TmnxNatPlDescription_Type(TItemDescription):
    """Custom type tmnxNatPlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlDescription_Type.__name__ = "TItemDescription"
_TmnxNatPlDescription_Object = MibTableColumn
tmnxNatPlDescription = _TmnxNatPlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 6),
    _TmnxNatPlDescription_Type()
)
tmnxNatPlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlDescription.setStatus("current")


class _TmnxNatPlAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatPlAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatPlAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatPlAdminState_Object = MibTableColumn
tmnxNatPlAdminState = _TmnxNatPlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 7),
    _TmnxNatPlAdminState_Type()
)
tmnxNatPlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlAdminState.setStatus("current")


class _TmnxNatPlPortResvType_Type(Integer32):
    """Custom type tmnxNatPlPortResvType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ports", 1),
          ("blocks", 2))
    )


_TmnxNatPlPortResvType_Type.__name__ = "Integer32"
_TmnxNatPlPortResvType_Object = MibTableColumn
tmnxNatPlPortResvType = _TmnxNatPlPortResvType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 8),
    _TmnxNatPlPortResvType_Type()
)
tmnxNatPlPortResvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortResvType.setStatus("current")


class _TmnxNatPlPortResvVal_Type(Unsigned32):
    """Custom type tmnxNatPlPortResvVal based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatPlPortResvVal_Type.__name__ = "Unsigned32"
_TmnxNatPlPortResvVal_Object = MibTableColumn
tmnxNatPlPortResvVal = _TmnxNatPlPortResvVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 9),
    _TmnxNatPlPortResvVal_Type()
)
tmnxNatPlPortResvVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortResvVal.setStatus("current")


class _TmnxNatPlPortResvAllowPrivileged_Type(TruthValue):
    """Custom type tmnxNatPlPortResvAllowPrivileged based on TruthValue"""
    defaultValue = 2


_TmnxNatPlPortResvAllowPrivileged_Type.__name__ = "TruthValue"
_TmnxNatPlPortResvAllowPrivileged_Object = MibTableColumn
tmnxNatPlPortResvAllowPrivileged = _TmnxNatPlPortResvAllowPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 10),
    _TmnxNatPlPortResvAllowPrivileged_Type()
)
tmnxNatPlPortResvAllowPrivileged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortResvAllowPrivileged.setStatus("current")


class _TmnxNatPlWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlWatermarkHigh_Object = MibTableColumn
tmnxNatPlWatermarkHigh = _TmnxNatPlWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 11),
    _TmnxNatPlWatermarkHigh_Type()
)
tmnxNatPlWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlWatermarkHigh.setStatus("current")


class _TmnxNatPlWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlWatermarkLow_Object = MibTableColumn
tmnxNatPlWatermarkLow = _TmnxNatPlWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 12),
    _TmnxNatPlWatermarkLow_Type()
)
tmnxNatPlWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlWatermarkLow.setStatus("current")


class _TmnxNatPlMode_Type(TmnxNatMode):
    """Custom type tmnxNatPlMode based on TmnxNatMode"""
    defaultValue = 0


_TmnxNatPlMode_Type.__name__ = "TmnxNatMode"
_TmnxNatPlMode_Object = MibTableColumn
tmnxNatPlMode = _TmnxNatPlMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 13),
    _TmnxNatPlMode_Type()
)
tmnxNatPlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlMode.setStatus("current")


class _TmnxNatPlPortFwdRangeEnd_Type(Unsigned32):
    """Custom type tmnxNatPlPortFwdRangeEnd based on Unsigned32"""
    defaultValue = 1023

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1023, 65535),
    )


_TmnxNatPlPortFwdRangeEnd_Type.__name__ = "Unsigned32"
_TmnxNatPlPortFwdRangeEnd_Object = MibTableColumn
tmnxNatPlPortFwdRangeEnd = _TmnxNatPlPortFwdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 14),
    _TmnxNatPlPortFwdRangeEnd_Type()
)
tmnxNatPlPortFwdRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortFwdRangeEnd.setStatus("current")


class _TmnxNatPlPortFwdDynBlkResv_Type(Unsigned32):
    """Custom type tmnxNatPlPortFwdDynBlkResv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxNatPlPortFwdDynBlkResv_Type.__name__ = "Unsigned32"
_TmnxNatPlPortFwdDynBlkResv_Object = MibTableColumn
tmnxNatPlPortFwdDynBlkResv = _TmnxNatPlPortFwdDynBlkResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 16),
    _TmnxNatPlPortFwdDynBlkResv_Type()
)
tmnxNatPlPortFwdDynBlkResv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortFwdDynBlkResv.setStatus("current")
_TmnxNatPlOperMode_Type = TmnxNatMode
_TmnxNatPlOperMode_Object = MibTableColumn
tmnxNatPlOperMode = _TmnxNatPlOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 20),
    _TmnxNatPlOperMode_Type()
)
tmnxNatPlOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlOperMode.setStatus("current")
_TmnxNatPlRangeTable_Object = MibTable
tmnxNatPlRangeTable = _TmnxNatPlRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeTable.setStatus("current")
_TmnxNatPlRangeEntry_Object = MibTableRow
tmnxNatPlRangeEntry = _TmnxNatPlRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1)
)
tmnxNatPlRangeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeEnd"),
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeEntry.setStatus("current")
_TmnxNatPlRangeAddrType_Type = InetAddressType
_TmnxNatPlRangeAddrType_Object = MibTableColumn
tmnxNatPlRangeAddrType = _TmnxNatPlRangeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 1),
    _TmnxNatPlRangeAddrType_Type()
)
tmnxNatPlRangeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeAddrType.setStatus("current")


class _TmnxNatPlRangeStart_Type(InetAddress):
    """Custom type tmnxNatPlRangeStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlRangeStart_Type.__name__ = "InetAddress"
_TmnxNatPlRangeStart_Object = MibTableColumn
tmnxNatPlRangeStart = _TmnxNatPlRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 2),
    _TmnxNatPlRangeStart_Type()
)
tmnxNatPlRangeStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeStart.setStatus("current")


class _TmnxNatPlRangeEnd_Type(InetAddress):
    """Custom type tmnxNatPlRangeEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlRangeEnd_Type.__name__ = "InetAddress"
_TmnxNatPlRangeEnd_Object = MibTableColumn
tmnxNatPlRangeEnd = _TmnxNatPlRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 3),
    _TmnxNatPlRangeEnd_Type()
)
tmnxNatPlRangeEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeEnd.setStatus("current")
_TmnxNatPlRangeRowStatus_Type = RowStatus
_TmnxNatPlRangeRowStatus_Object = MibTableColumn
tmnxNatPlRangeRowStatus = _TmnxNatPlRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 4),
    _TmnxNatPlRangeRowStatus_Type()
)
tmnxNatPlRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeRowStatus.setStatus("current")
_TmnxNatPlRangeLastMgmtChange_Type = TimeStamp
_TmnxNatPlRangeLastMgmtChange_Object = MibTableColumn
tmnxNatPlRangeLastMgmtChange = _TmnxNatPlRangeLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 5),
    _TmnxNatPlRangeLastMgmtChange_Type()
)
tmnxNatPlRangeLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeLastMgmtChange.setStatus("current")


class _TmnxNatPlRangeDescription_Type(TItemDescription):
    """Custom type tmnxNatPlRangeDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlRangeDescription_Type.__name__ = "TItemDescription"
_TmnxNatPlRangeDescription_Object = MibTableColumn
tmnxNatPlRangeDescription = _TmnxNatPlRangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 6),
    _TmnxNatPlRangeDescription_Type()
)
tmnxNatPlRangeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeDescription.setStatus("current")


class _TmnxNatPlRangeAdminDrain_Type(TruthValue):
    """Custom type tmnxNatPlRangeAdminDrain based on TruthValue"""
    defaultValue = 2


_TmnxNatPlRangeAdminDrain_Type.__name__ = "TruthValue"
_TmnxNatPlRangeAdminDrain_Object = MibTableColumn
tmnxNatPlRangeAdminDrain = _TmnxNatPlRangeAdminDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 7),
    _TmnxNatPlRangeAdminDrain_Type()
)
tmnxNatPlRangeAdminDrain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeAdminDrain.setStatus("current")
_TmnxNatPlRangeNumAllocatedBlk_Type = Gauge32
_TmnxNatPlRangeNumAllocatedBlk_Object = MibTableColumn
tmnxNatPlRangeNumAllocatedBlk = _TmnxNatPlRangeNumAllocatedBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 8),
    _TmnxNatPlRangeNumAllocatedBlk_Type()
)
tmnxNatPlRangeNumAllocatedBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeNumAllocatedBlk.setStatus("obsolete")
_TmnxNatPlL2AwTable_Object = MibTable
tmnxNatPlL2AwTable = _TmnxNatPlL2AwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwTable.setStatus("current")
_TmnxNatPlL2AwEntry_Object = MibTableRow
tmnxNatPlL2AwEntry = _TmnxNatPlL2AwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1)
)
tmnxNatPlL2AwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwEntry.setStatus("current")
_TmnxNatPlL2AwBlockUsage_Type = TmnxNatUsageLevel
_TmnxNatPlL2AwBlockUsage_Object = MibTableColumn
tmnxNatPlL2AwBlockUsage = _TmnxNatPlL2AwBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 1),
    _TmnxNatPlL2AwBlockUsage_Type()
)
tmnxNatPlL2AwBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwBlockUsage.setStatus("current")
_TmnxNatPlL2AwBlockUsageHi_Type = TruthValue
_TmnxNatPlL2AwBlockUsageHi_Object = MibTableColumn
tmnxNatPlL2AwBlockUsageHi = _TmnxNatPlL2AwBlockUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 2),
    _TmnxNatPlL2AwBlockUsageHi_Type()
)
tmnxNatPlL2AwBlockUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwBlockUsageHi.setStatus("current")
_TmnxNatPlLsnMemberTable_Object = MibTable
tmnxNatPlLsnMemberTable = _TmnxNatPlLsnMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberTable.setStatus("current")
_TmnxNatPlLsnMemberEntry_Object = MibTableRow
tmnxNatPlLsnMemberEntry = _TmnxNatPlLsnMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1)
)
tmnxNatPlLsnMemberEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberEntry.setStatus("current")
_TmnxNatPlLsnMemberIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatPlLsnMemberIsaGrpId_Object = MibTableColumn
tmnxNatPlLsnMemberIsaGrpId = _TmnxNatPlLsnMemberIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 1),
    _TmnxNatPlLsnMemberIsaGrpId_Type()
)
tmnxNatPlLsnMemberIsaGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberIsaGrpId.setStatus("current")
_TmnxNatPlLsnMemberBlockUsage_Type = TmnxNatUsageLevel
_TmnxNatPlLsnMemberBlockUsage_Object = MibTableColumn
tmnxNatPlLsnMemberBlockUsage = _TmnxNatPlLsnMemberBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 2),
    _TmnxNatPlLsnMemberBlockUsage_Type()
)
tmnxNatPlLsnMemberBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberBlockUsage.setStatus("current")
_TmnxNatPlLsnMemberBlockUsageHi_Type = TruthValue
_TmnxNatPlLsnMemberBlockUsageHi_Object = MibTableColumn
tmnxNatPlLsnMemberBlockUsageHi = _TmnxNatPlLsnMemberBlockUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 3),
    _TmnxNatPlLsnMemberBlockUsageHi_Type()
)
tmnxNatPlLsnMemberBlockUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberBlockUsageHi.setStatus("current")
_TmnxNatBlkL2AwTable_Object = MibTable
tmnxNatBlkL2AwTable = _TmnxNatBlkL2AwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwTable.setStatus("current")
_TmnxNatBlkL2AwEntry_Object = MibTableRow
tmnxNatBlkL2AwEntry = _TmnxNatBlkL2AwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1)
)
tmnxNatBlkL2AwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStart"),
)
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwEntry.setStatus("current")
_TmnxNatBlkL2AwAddrType_Type = InetAddressType
_TmnxNatBlkL2AwAddrType_Object = MibTableColumn
tmnxNatBlkL2AwAddrType = _TmnxNatBlkL2AwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 1),
    _TmnxNatBlkL2AwAddrType_Type()
)
tmnxNatBlkL2AwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwAddrType.setStatus("current")


class _TmnxNatBlkL2AwAddr_Type(InetAddress):
    """Custom type tmnxNatBlkL2AwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatBlkL2AwAddr_Type.__name__ = "InetAddress"
_TmnxNatBlkL2AwAddr_Object = MibTableColumn
tmnxNatBlkL2AwAddr = _TmnxNatBlkL2AwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 2),
    _TmnxNatBlkL2AwAddr_Type()
)
tmnxNatBlkL2AwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwAddr.setStatus("current")
_TmnxNatBlkL2AwStart_Type = InetPortNumber
_TmnxNatBlkL2AwStart_Object = MibTableColumn
tmnxNatBlkL2AwStart = _TmnxNatBlkL2AwStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 3),
    _TmnxNatBlkL2AwStart_Type()
)
tmnxNatBlkL2AwStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwStart.setStatus("current")
_TmnxNatBlkL2AwEnd_Type = InetPortNumber
_TmnxNatBlkL2AwEnd_Object = MibTableColumn
tmnxNatBlkL2AwEnd = _TmnxNatBlkL2AwEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 4),
    _TmnxNatBlkL2AwEnd_Type()
)
tmnxNatBlkL2AwEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwEnd.setStatus("current")
_TmnxNatBlkL2AwPool_Type = TNamedItem
_TmnxNatBlkL2AwPool_Object = MibTableColumn
tmnxNatBlkL2AwPool = _TmnxNatBlkL2AwPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 5),
    _TmnxNatBlkL2AwPool_Type()
)
tmnxNatBlkL2AwPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwPool.setStatus("current")


class _TmnxNatBlkL2AwSubIdent_Type(DisplayString):
    """Custom type tmnxNatBlkL2AwSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatBlkL2AwSubIdent_Type.__name__ = "DisplayString"
_TmnxNatBlkL2AwSubIdent_Object = MibTableColumn
tmnxNatBlkL2AwSubIdent = _TmnxNatBlkL2AwSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 6),
    _TmnxNatBlkL2AwSubIdent_Type()
)
tmnxNatBlkL2AwSubIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwSubIdent.setStatus("current")
_TmnxNatBlkL2AwPolicy_Type = TNamedItemOrEmpty
_TmnxNatBlkL2AwPolicy_Object = MibTableColumn
tmnxNatBlkL2AwPolicy = _TmnxNatBlkL2AwPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 7),
    _TmnxNatBlkL2AwPolicy_Type()
)
tmnxNatBlkL2AwPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwPolicy.setStatus("current")


class _TmnxNatBlkL2AwStartDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatBlkL2AwStartDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatBlkL2AwStartDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatBlkL2AwStartDateAndTime_Object = MibTableColumn
tmnxNatBlkL2AwStartDateAndTime = _TmnxNatBlkL2AwStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 8),
    _TmnxNatBlkL2AwStartDateAndTime_Type()
)
tmnxNatBlkL2AwStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwStartDateAndTime.setStatus("current")
_TmnxNatBlkLsnTable_Object = MibTable
tmnxNatBlkLsnTable = _TmnxNatBlkLsnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxNatBlkLsnTable.setStatus("current")
_TmnxNatBlkLsnEntry_Object = MibTableRow
tmnxNatBlkLsnEntry = _TmnxNatBlkLsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1)
)
tmnxNatBlkLsnEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnStart"),
)
if mibBuilder.loadTexts:
    tmnxNatBlkLsnEntry.setStatus("current")
_TmnxNatBlkLsnAddrType_Type = InetAddressType
_TmnxNatBlkLsnAddrType_Object = MibTableColumn
tmnxNatBlkLsnAddrType = _TmnxNatBlkLsnAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 1),
    _TmnxNatBlkLsnAddrType_Type()
)
tmnxNatBlkLsnAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnAddrType.setStatus("current")


class _TmnxNatBlkLsnAddr_Type(InetAddress):
    """Custom type tmnxNatBlkLsnAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatBlkLsnAddr_Type.__name__ = "InetAddress"
_TmnxNatBlkLsnAddr_Object = MibTableColumn
tmnxNatBlkLsnAddr = _TmnxNatBlkLsnAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 2),
    _TmnxNatBlkLsnAddr_Type()
)
tmnxNatBlkLsnAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnAddr.setStatus("current")
_TmnxNatBlkLsnStart_Type = InetPortNumber
_TmnxNatBlkLsnStart_Object = MibTableColumn
tmnxNatBlkLsnStart = _TmnxNatBlkLsnStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 3),
    _TmnxNatBlkLsnStart_Type()
)
tmnxNatBlkLsnStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnStart.setStatus("current")
_TmnxNatBlkLsnEnd_Type = InetPortNumber
_TmnxNatBlkLsnEnd_Object = MibTableColumn
tmnxNatBlkLsnEnd = _TmnxNatBlkLsnEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 4),
    _TmnxNatBlkLsnEnd_Type()
)
tmnxNatBlkLsnEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnEnd.setStatus("current")
_TmnxNatBlkLsnPool_Type = TNamedItem
_TmnxNatBlkLsnPool_Object = MibTableColumn
tmnxNatBlkLsnPool = _TmnxNatBlkLsnPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 5),
    _TmnxNatBlkLsnPool_Type()
)
tmnxNatBlkLsnPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnPool.setStatus("current")
_TmnxNatBlkLsnSubId_Type = Unsigned32
_TmnxNatBlkLsnSubId_Object = MibTableColumn
tmnxNatBlkLsnSubId = _TmnxNatBlkLsnSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 6),
    _TmnxNatBlkLsnSubId_Type()
)
tmnxNatBlkLsnSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnSubId.setStatus("current")
_TmnxNatBlkLsnInsideVRtrID_Type = TmnxVRtrID
_TmnxNatBlkLsnInsideVRtrID_Object = MibTableColumn
tmnxNatBlkLsnInsideVRtrID = _TmnxNatBlkLsnInsideVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 7),
    _TmnxNatBlkLsnInsideVRtrID_Type()
)
tmnxNatBlkLsnInsideVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnInsideVRtrID.setStatus("current")
_TmnxNatBlkLsnInsideAddrType_Type = InetAddressType
_TmnxNatBlkLsnInsideAddrType_Object = MibTableColumn
tmnxNatBlkLsnInsideAddrType = _TmnxNatBlkLsnInsideAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 8),
    _TmnxNatBlkLsnInsideAddrType_Type()
)
tmnxNatBlkLsnInsideAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnInsideAddrType.setStatus("current")


class _TmnxNatBlkLsnInsideAddr_Type(InetAddress):
    """Custom type tmnxNatBlkLsnInsideAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatBlkLsnInsideAddr_Type.__name__ = "InetAddress"
_TmnxNatBlkLsnInsideAddr_Object = MibTableColumn
tmnxNatBlkLsnInsideAddr = _TmnxNatBlkLsnInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 9),
    _TmnxNatBlkLsnInsideAddr_Type()
)
tmnxNatBlkLsnInsideAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnInsideAddr.setStatus("current")
_TmnxNatBlkLsnPolicy_Type = TNamedItemOrEmpty
_TmnxNatBlkLsnPolicy_Object = MibTableColumn
tmnxNatBlkLsnPolicy = _TmnxNatBlkLsnPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 10),
    _TmnxNatBlkLsnPolicy_Type()
)
tmnxNatBlkLsnPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnPolicy.setStatus("current")


class _TmnxNatBlkLsnStartDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatBlkLsnStartDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatBlkLsnStartDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatBlkLsnStartDateAndTime_Object = MibTableColumn
tmnxNatBlkLsnStartDateAndTime = _TmnxNatBlkLsnStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 11),
    _TmnxNatBlkLsnStartDateAndTime_Type()
)
tmnxNatBlkLsnStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnStartDateAndTime.setStatus("current")
_TmnxNatPlLsnTable_Object = MibTable
tmnxNatPlLsnTable = _TmnxNatPlLsnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnTable.setStatus("current")
_TmnxNatPlLsnEntry_Object = MibTableRow
tmnxNatPlLsnEntry = _TmnxNatPlLsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1)
)
tmnxNatPlLsnEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnEntry.setStatus("current")


class _TmnxNatPlLsnSubscriberLimit_Type(Unsigned32):
    """Custom type tmnxNatPlLsnSubscriberLimit based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatPlLsnSubscriberLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnSubscriberLimit_Object = MibTableColumn
tmnxNatPlLsnSubscriberLimit = _TmnxNatPlLsnSubscriberLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 1),
    _TmnxNatPlLsnSubscriberLimit_Type()
)
tmnxNatPlLsnSubscriberLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnSubscriberLimit.setStatus("current")


class _TmnxNatPlLsnRedExpPrefixType_Type(InetAddressType):
    """Custom type tmnxNatPlLsnRedExpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxNatPlLsnRedExpPrefixType_Type.__name__ = "InetAddressType"
_TmnxNatPlLsnRedExpPrefixType_Object = MibTableColumn
tmnxNatPlLsnRedExpPrefixType = _TmnxNatPlLsnRedExpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 10),
    _TmnxNatPlLsnRedExpPrefixType_Type()
)
tmnxNatPlLsnRedExpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedExpPrefixType.setStatus("current")


class _TmnxNatPlLsnRedExpPrefix_Type(InetAddress):
    """Custom type tmnxNatPlLsnRedExpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlLsnRedExpPrefix_Type.__name__ = "InetAddress"
_TmnxNatPlLsnRedExpPrefix_Object = MibTableColumn
tmnxNatPlLsnRedExpPrefix = _TmnxNatPlLsnRedExpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 11),
    _TmnxNatPlLsnRedExpPrefix_Type()
)
tmnxNatPlLsnRedExpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedExpPrefix.setStatus("current")


class _TmnxNatPlLsnRedExpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatPlLsnRedExpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatPlLsnRedExpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatPlLsnRedExpPrefixLen_Object = MibTableColumn
tmnxNatPlLsnRedExpPrefixLen = _TmnxNatPlLsnRedExpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 12),
    _TmnxNatPlLsnRedExpPrefixLen_Type()
)
tmnxNatPlLsnRedExpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedExpPrefixLen.setStatus("current")


class _TmnxNatPlLsnRedMonPrefixType_Type(InetAddressType):
    """Custom type tmnxNatPlLsnRedMonPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxNatPlLsnRedMonPrefixType_Type.__name__ = "InetAddressType"
_TmnxNatPlLsnRedMonPrefixType_Object = MibTableColumn
tmnxNatPlLsnRedMonPrefixType = _TmnxNatPlLsnRedMonPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 13),
    _TmnxNatPlLsnRedMonPrefixType_Type()
)
tmnxNatPlLsnRedMonPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedMonPrefixType.setStatus("current")


class _TmnxNatPlLsnRedMonPrefix_Type(InetAddress):
    """Custom type tmnxNatPlLsnRedMonPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlLsnRedMonPrefix_Type.__name__ = "InetAddress"
_TmnxNatPlLsnRedMonPrefix_Object = MibTableColumn
tmnxNatPlLsnRedMonPrefix = _TmnxNatPlLsnRedMonPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 14),
    _TmnxNatPlLsnRedMonPrefix_Type()
)
tmnxNatPlLsnRedMonPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedMonPrefix.setStatus("current")


class _TmnxNatPlLsnRedMonPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatPlLsnRedMonPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatPlLsnRedMonPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatPlLsnRedMonPrefixLen_Object = MibTableColumn
tmnxNatPlLsnRedMonPrefixLen = _TmnxNatPlLsnRedMonPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 15),
    _TmnxNatPlLsnRedMonPrefixLen_Type()
)
tmnxNatPlLsnRedMonPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedMonPrefixLen.setStatus("current")
_TmnxNatPlLsnRedActive_Type = TruthValue
_TmnxNatPlLsnRedActive_Object = MibTableColumn
tmnxNatPlLsnRedActive = _TmnxNatPlLsnRedActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 16),
    _TmnxNatPlLsnRedActive_Type()
)
tmnxNatPlLsnRedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedActive.setStatus("current")


class _TmnxNatPlLsnDetPortResv_Type(Unsigned32):
    """Custom type tmnxNatPlLsnDetPortResv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxNatPlLsnDetPortResv_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnDetPortResv_Object = MibTableColumn
tmnxNatPlLsnDetPortResv = _TmnxNatPlLsnDetPortResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 20),
    _TmnxNatPlLsnDetPortResv_Type()
)
tmnxNatPlLsnDetPortResv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnDetPortResv.setStatus("current")


class _TmnxNatPlLsnRedAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatPlLsnRedAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatPlLsnRedAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatPlLsnRedAdminState_Object = MibTableColumn
tmnxNatPlLsnRedAdminState = _TmnxNatPlLsnRedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 21),
    _TmnxNatPlLsnRedAdminState_Type()
)
tmnxNatPlLsnRedAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedAdminState.setStatus("current")


class _TmnxNatPlLsnRedFollowPoolRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPlLsnRedFollowPoolRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPlLsnRedFollowPoolRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPlLsnRedFollowPoolRouter_Object = MibTableColumn
tmnxNatPlLsnRedFollowPoolRouter = _TmnxNatPlLsnRedFollowPoolRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 22),
    _TmnxNatPlLsnRedFollowPoolRouter_Type()
)
tmnxNatPlLsnRedFollowPoolRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedFollowPoolRouter.setStatus("current")


class _TmnxNatPlLsnRedFollowPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlLsnRedFollowPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlLsnRedFollowPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlLsnRedFollowPool_Object = MibTableColumn
tmnxNatPlLsnRedFollowPool = _TmnxNatPlLsnRedFollowPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 23),
    _TmnxNatPlLsnRedFollowPool_Type()
)
tmnxNatPlLsnRedFollowPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedFollowPool.setStatus("current")
_TmnxNatPlHistAction_ObjectIdentity = ObjectIdentity
tmnxNatPlHistAction = _TmnxNatPlHistAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8)
)
_TmnxNatPlHistActionVRtrId_Type = TmnxVRtrIDOrZero
_TmnxNatPlHistActionVRtrId_Object = MibScalar
tmnxNatPlHistActionVRtrId = _TmnxNatPlHistActionVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 1),
    _TmnxNatPlHistActionVRtrId_Type()
)
tmnxNatPlHistActionVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionVRtrId.setStatus("current")
_TmnxNatPlHistActionPoolName_Type = TNamedItemOrEmpty
_TmnxNatPlHistActionPoolName_Object = MibScalar
tmnxNatPlHistActionPoolName = _TmnxNatPlHistActionPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 2),
    _TmnxNatPlHistActionPoolName_Type()
)
tmnxNatPlHistActionPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionPoolName.setStatus("current")


class _TmnxNatPlHistActionBucketSize_Type(Unsigned32):
    """Custom type tmnxNatPlHistActionBucketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65536),
    )


_TmnxNatPlHistActionBucketSize_Type.__name__ = "Unsigned32"
_TmnxNatPlHistActionBucketSize_Object = MibScalar
tmnxNatPlHistActionBucketSize = _TmnxNatPlHistActionBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 3),
    _TmnxNatPlHistActionBucketSize_Type()
)
tmnxNatPlHistActionBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionBucketSize.setStatus("current")


class _TmnxNatPlHistActionNumBuckets_Type(Unsigned32):
    """Custom type tmnxNatPlHistActionNumBuckets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 50),
    )


_TmnxNatPlHistActionNumBuckets_Type.__name__ = "Unsigned32"
_TmnxNatPlHistActionNumBuckets_Object = MibScalar
tmnxNatPlHistActionNumBuckets = _TmnxNatPlHistActionNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 4),
    _TmnxNatPlHistActionNumBuckets_Type()
)
tmnxNatPlHistActionNumBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionNumBuckets.setStatus("current")
_TmnxNatPlHistActionGo_Type = TmnxActionType
_TmnxNatPlHistActionGo_Object = MibScalar
tmnxNatPlHistActionGo = _TmnxNatPlHistActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 5),
    _TmnxNatPlHistActionGo_Type()
)
tmnxNatPlHistActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionGo.setStatus("current")
_TmnxNatPlHistTable_Object = MibTable
tmnxNatPlHistTable = _TmnxNatPlHistTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9)
)
if mibBuilder.loadTexts:
    tmnxNatPlHistTable.setStatus("current")
_TmnxNatPlHistEntry_Object = MibTableRow
tmnxNatPlHistEntry = _TmnxNatPlHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1)
)
tmnxNatPlHistEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlHistIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatPlHistEntry.setStatus("current")
_TmnxNatPlHistIndex_Type = Unsigned32
_TmnxNatPlHistIndex_Object = MibTableColumn
tmnxNatPlHistIndex = _TmnxNatPlHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 1),
    _TmnxNatPlHistIndex_Type()
)
tmnxNatPlHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlHistIndex.setStatus("current")
_TmnxNatPlHistTimestamp_Type = TimeStamp
_TmnxNatPlHistTimestamp_Object = MibTableColumn
tmnxNatPlHistTimestamp = _TmnxNatPlHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 2),
    _TmnxNatPlHistTimestamp_Type()
)
tmnxNatPlHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistTimestamp.setStatus("current")
_TmnxNatPlHistVRtrID_Type = TmnxVRtrID
_TmnxNatPlHistVRtrID_Object = MibTableColumn
tmnxNatPlHistVRtrID = _TmnxNatPlHistVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 3),
    _TmnxNatPlHistVRtrID_Type()
)
tmnxNatPlHistVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistVRtrID.setStatus("current")
_TmnxNatPlHistPoolName_Type = TNamedItem
_TmnxNatPlHistPoolName_Object = MibTableColumn
tmnxNatPlHistPoolName = _TmnxNatPlHistPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 4),
    _TmnxNatPlHistPoolName_Type()
)
tmnxNatPlHistPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistPoolName.setStatus("current")
_TmnxNatPlHistBucketSize_Type = Unsigned32
_TmnxNatPlHistBucketSize_Object = MibTableColumn
tmnxNatPlHistBucketSize = _TmnxNatPlHistBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 5),
    _TmnxNatPlHistBucketSize_Type()
)
tmnxNatPlHistBucketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistBucketSize.setStatus("current")
_TmnxNatPlHistNumBuckets_Type = Unsigned32
_TmnxNatPlHistNumBuckets_Object = MibTableColumn
tmnxNatPlHistNumBuckets = _TmnxNatPlHistNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 6),
    _TmnxNatPlHistNumBuckets_Type()
)
tmnxNatPlHistNumBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistNumBuckets.setStatus("current")
_TmnxNatPlHistTcp_Type = Gauge32
_TmnxNatPlHistTcp_Object = MibTableColumn
tmnxNatPlHistTcp = _TmnxNatPlHistTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 7),
    _TmnxNatPlHistTcp_Type()
)
tmnxNatPlHistTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistTcp.setStatus("current")
_TmnxNatPlHistUdp_Type = Gauge32
_TmnxNatPlHistUdp_Object = MibTableColumn
tmnxNatPlHistUdp = _TmnxNatPlHistUdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 8),
    _TmnxNatPlHistUdp_Type()
)
tmnxNatPlHistUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistUdp.setStatus("current")
_TmnxNatPlHistIcmp_Type = Gauge32
_TmnxNatPlHistIcmp_Object = MibTableColumn
tmnxNatPlHistIcmp = _TmnxNatPlHistIcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 9),
    _TmnxNatPlHistIcmp_Type()
)
tmnxNatPlHistIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistIcmp.setStatus("current")
_TmnxNatPlRangeStatTable_Object = MibTable
tmnxNatPlRangeStatTable = _TmnxNatPlRangeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatTable.setStatus("current")
_TmnxNatPlRangeStatEntry_Object = MibTableRow
tmnxNatPlRangeStatEntry = _TmnxNatPlRangeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatEntry.setStatus("current")
_TmnxNatPlRangeStatNumAllocBlk_Type = Gauge32
_TmnxNatPlRangeStatNumAllocBlk_Object = MibTableColumn
tmnxNatPlRangeStatNumAllocBlk = _TmnxNatPlRangeStatNumAllocBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10, 1, 8),
    _TmnxNatPlRangeStatNumAllocBlk_Type()
)
tmnxNatPlRangeStatNumAllocBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatNumAllocBlk.setStatus("current")
_TmnxNatDestObjs_ObjectIdentity = ObjectIdentity
tmnxNatDestObjs = _TmnxNatDestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5)
)
_TmnxNatDestTable_Object = MibTable
tmnxNatDestTable = _TmnxNatDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxNatDestTable.setStatus("current")
_TmnxNatDestEntry_Object = MibTableRow
tmnxNatDestEntry = _TmnxNatDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1)
)
tmnxNatDestEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDestAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDestAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDestPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatDestEntry.setStatus("current")
_TmnxNatDestAddrType_Type = InetAddressType
_TmnxNatDestAddrType_Object = MibTableColumn
tmnxNatDestAddrType = _TmnxNatDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 1),
    _TmnxNatDestAddrType_Type()
)
tmnxNatDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDestAddrType.setStatus("current")


class _TmnxNatDestAddr_Type(InetAddress):
    """Custom type tmnxNatDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDestAddr_Type.__name__ = "InetAddress"
_TmnxNatDestAddr_Object = MibTableColumn
tmnxNatDestAddr = _TmnxNatDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 2),
    _TmnxNatDestAddr_Type()
)
tmnxNatDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDestAddr.setStatus("current")


class _TmnxNatDestPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDestPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatDestPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDestPrefixLen_Object = MibTableColumn
tmnxNatDestPrefixLen = _TmnxNatDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 3),
    _TmnxNatDestPrefixLen_Type()
)
tmnxNatDestPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDestPrefixLen.setStatus("current")
_TmnxNatDestRowStatus_Type = RowStatus
_TmnxNatDestRowStatus_Object = MibTableColumn
tmnxNatDestRowStatus = _TmnxNatDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 4),
    _TmnxNatDestRowStatus_Type()
)
tmnxNatDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDestRowStatus.setStatus("current")
_TmnxNatDestLastMgmtChange_Type = TimeStamp
_TmnxNatDestLastMgmtChange_Object = MibTableColumn
tmnxNatDestLastMgmtChange = _TmnxNatDestLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 5),
    _TmnxNatDestLastMgmtChange_Type()
)
tmnxNatDestLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDestLastMgmtChange.setStatus("current")


class _TmnxNatDestNatPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatDestNatPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatDestNatPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatDestNatPolicy_Object = MibTableColumn
tmnxNatDestNatPolicy = _TmnxNatDestNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 10),
    _TmnxNatDestNatPolicy_Type()
)
tmnxNatDestNatPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDestNatPolicy.setStatus("current")
_TmnxNatDsliteAddrTable_Object = MibTable
tmnxNatDsliteAddrTable = _TmnxNatDsliteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrTable.setStatus("current")
_TmnxNatDsliteAddrEntry_Object = MibTableRow
tmnxNatDsliteAddrEntry = _TmnxNatDsliteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1)
)
tmnxNatDsliteAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrEntry.setStatus("current")
_TmnxNatDsliteAddrType_Type = InetAddressType
_TmnxNatDsliteAddrType_Object = MibTableColumn
tmnxNatDsliteAddrType = _TmnxNatDsliteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 1),
    _TmnxNatDsliteAddrType_Type()
)
tmnxNatDsliteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrType.setStatus("current")


class _TmnxNatDsliteAddr_Type(InetAddress):
    """Custom type tmnxNatDsliteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDsliteAddr_Type.__name__ = "InetAddress"
_TmnxNatDsliteAddr_Object = MibTableColumn
tmnxNatDsliteAddr = _TmnxNatDsliteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 2),
    _TmnxNatDsliteAddr_Type()
)
tmnxNatDsliteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddr.setStatus("current")
_TmnxNatDsliteAddrRowStatus_Type = RowStatus
_TmnxNatDsliteAddrRowStatus_Object = MibTableColumn
tmnxNatDsliteAddrRowStatus = _TmnxNatDsliteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 4),
    _TmnxNatDsliteAddrRowStatus_Type()
)
tmnxNatDsliteAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrRowStatus.setStatus("current")
_TmnxNatDsliteAddrLastMgmtChange_Type = TimeStamp
_TmnxNatDsliteAddrLastMgmtChange_Object = MibTableColumn
tmnxNatDsliteAddrLastMgmtChange = _TmnxNatDsliteAddrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 5),
    _TmnxNatDsliteAddrLastMgmtChange_Type()
)
tmnxNatDsliteAddrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrLastMgmtChange.setStatus("current")


class _TmnxNatDsliteAddrTunnelMtu_Type(Unsigned32):
    """Custom type tmnxNatDsliteAddrTunnelMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9212),
    )


_TmnxNatDsliteAddrTunnelMtu_Type.__name__ = "Unsigned32"
_TmnxNatDsliteAddrTunnelMtu_Object = MibTableColumn
tmnxNatDsliteAddrTunnelMtu = _TmnxNatDsliteAddrTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 6),
    _TmnxNatDsliteAddrTunnelMtu_Type()
)
tmnxNatDsliteAddrTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrTunnelMtu.setStatus("current")


class _TmnxNatDsliteAddrFragmentIp_Type(TmnxNatFragmentIpMode):
    """Custom type tmnxNatDsliteAddrFragmentIp based on TmnxNatFragmentIpMode"""
    defaultValue = 0


_TmnxNatDsliteAddrFragmentIp_Type.__name__ = "TmnxNatFragmentIpMode"
_TmnxNatDsliteAddrFragmentIp_Object = MibTableColumn
tmnxNatDsliteAddrFragmentIp = _TmnxNatDsliteAddrFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 7),
    _TmnxNatDsliteAddrFragmentIp_Type()
)
tmnxNatDsliteAddrFragmentIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrFragmentIp.setStatus("current")
_TmnxNatSubObjs_ObjectIdentity = ObjectIdentity
tmnxNatSubObjs = _TmnxNatSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6)
)
_TmnxNatLsnHostTable_Object = MibTable
tmnxNatLsnHostTable = _TmnxNatLsnHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxNatLsnHostTable.setStatus("obsolete")
_TmnxNatLsnHostEntry_Object = MibTableRow
tmnxNatLsnHostEntry = _TmnxNatLsnHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1)
)
tmnxNatLsnHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnHostEntry.setStatus("obsolete")
_TmnxNatLsnHostAddrType_Type = InetAddressType
_TmnxNatLsnHostAddrType_Object = MibTableColumn
tmnxNatLsnHostAddrType = _TmnxNatLsnHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 1),
    _TmnxNatLsnHostAddrType_Type()
)
tmnxNatLsnHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnHostAddrType.setStatus("obsolete")


class _TmnxNatLsnHostAddr_Type(InetAddress):
    """Custom type tmnxNatLsnHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnHostAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnHostAddr_Object = MibTableColumn
tmnxNatLsnHostAddr = _TmnxNatLsnHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 2),
    _TmnxNatLsnHostAddr_Type()
)
tmnxNatLsnHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnHostAddr.setStatus("obsolete")
_TmnxNatLsnHostSubId_Type = Unsigned32
_TmnxNatLsnHostSubId_Object = MibTableColumn
tmnxNatLsnHostSubId = _TmnxNatLsnHostSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 3),
    _TmnxNatLsnHostSubId_Type()
)
tmnxNatLsnHostSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostSubId.setStatus("obsolete")
_TmnxNatLsnHostOutVRtrID_Type = TmnxVRtrID
_TmnxNatLsnHostOutVRtrID_Object = MibTableColumn
tmnxNatLsnHostOutVRtrID = _TmnxNatLsnHostOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 4),
    _TmnxNatLsnHostOutVRtrID_Type()
)
tmnxNatLsnHostOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostOutVRtrID.setStatus("obsolete")
_TmnxNatLsnHostOutAddrType_Type = InetAddressType
_TmnxNatLsnHostOutAddrType_Object = MibTableColumn
tmnxNatLsnHostOutAddrType = _TmnxNatLsnHostOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 5),
    _TmnxNatLsnHostOutAddrType_Type()
)
tmnxNatLsnHostOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostOutAddrType.setStatus("obsolete")


class _TmnxNatLsnHostOutAddr_Type(InetAddress):
    """Custom type tmnxNatLsnHostOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnHostOutAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnHostOutAddr_Object = MibTableColumn
tmnxNatLsnHostOutAddr = _TmnxNatLsnHostOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 6),
    _TmnxNatLsnHostOutAddr_Type()
)
tmnxNatLsnHostOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostOutAddr.setStatus("obsolete")
_TmnxNatLsnSubTable_Object = MibTable
tmnxNatLsnSubTable = _TmnxNatLsnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubTable.setStatus("obsolete")
_TmnxNatLsnSubEntry_Object = MibTableRow
tmnxNatLsnSubEntry = _TmnxNatLsnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1)
)
tmnxNatLsnSubEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubId"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubEntry.setStatus("obsolete")
_TmnxNatLsnSubId_Type = Unsigned32
_TmnxNatLsnSubId_Object = MibTableColumn
tmnxNatLsnSubId = _TmnxNatLsnSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 1),
    _TmnxNatLsnSubId_Type()
)
tmnxNatLsnSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubId.setStatus("obsolete")
_TmnxNatLsnSubPolicy_Type = TNamedItem
_TmnxNatLsnSubPolicy_Object = MibTableColumn
tmnxNatLsnSubPolicy = _TmnxNatLsnSubPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 2),
    _TmnxNatLsnSubPolicy_Type()
)
tmnxNatLsnSubPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPolicy.setStatus("obsolete")
_TmnxNatLsnSubIsaGrp_Type = TmnxNatIsaGrpIdOrZero
_TmnxNatLsnSubIsaGrp_Object = MibTableColumn
tmnxNatLsnSubIsaGrp = _TmnxNatLsnSubIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 3),
    _TmnxNatLsnSubIsaGrp_Type()
)
tmnxNatLsnSubIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubIsaGrp.setStatus("obsolete")
_TmnxNatLsnSubIsaMemberId_Type = Unsigned32
_TmnxNatLsnSubIsaMemberId_Object = MibTableColumn
tmnxNatLsnSubIsaMemberId = _TmnxNatLsnSubIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 4),
    _TmnxNatLsnSubIsaMemberId_Type()
)
tmnxNatLsnSubIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubIsaMemberId.setStatus("obsolete")
_TmnxNatLsnSubOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatLsnSubOutVRtrID_Object = MibTableColumn
tmnxNatLsnSubOutVRtrID = _TmnxNatLsnSubOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 5),
    _TmnxNatLsnSubOutVRtrID_Type()
)
tmnxNatLsnSubOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubOutVRtrID.setStatus("obsolete")
_TmnxNatLsnSubOutAddrType_Type = InetAddressType
_TmnxNatLsnSubOutAddrType_Object = MibTableColumn
tmnxNatLsnSubOutAddrType = _TmnxNatLsnSubOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 6),
    _TmnxNatLsnSubOutAddrType_Type()
)
tmnxNatLsnSubOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubOutAddrType.setStatus("obsolete")


class _TmnxNatLsnSubOutAddr_Type(InetAddress):
    """Custom type tmnxNatLsnSubOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnSubOutAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnSubOutAddr_Object = MibTableColumn
tmnxNatLsnSubOutAddr = _TmnxNatLsnSubOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 7),
    _TmnxNatLsnSubOutAddr_Type()
)
tmnxNatLsnSubOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubOutAddr.setStatus("obsolete")
_TmnxNatLsnSubIdStr_Type = TmnxNatSubscriberIdString
_TmnxNatLsnSubIdStr_Object = MibTableColumn
tmnxNatLsnSubIdStr = _TmnxNatLsnSubIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 8),
    _TmnxNatLsnSubIdStr_Type()
)
tmnxNatLsnSubIdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubIdStr.setStatus("obsolete")
_TmnxNatLsnSubStatTable_Object = MibTable
tmnxNatLsnSubStatTable = _TmnxNatLsnSubStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatTable.setStatus("obsolete")
_TmnxNatLsnSubStatEntry_Object = MibTableRow
tmnxNatLsnSubStatEntry = _TmnxNatLsnSubStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatEntry.setStatus("obsolete")
_TmnxNatLsnSubStatIcmpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatIcmpPortUsage_Object = MibTableColumn
tmnxNatLsnSubStatIcmpPortUsage = _TmnxNatLsnSubStatIcmpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 3),
    _TmnxNatLsnSubStatIcmpPortUsage_Type()
)
tmnxNatLsnSubStatIcmpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatIcmpPortUsage.setStatus("obsolete")
_TmnxNatLsnSubStatIcmpPortUsageHi_Type = TruthValue
_TmnxNatLsnSubStatIcmpPortUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatIcmpPortUsageHi = _TmnxNatLsnSubStatIcmpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 4),
    _TmnxNatLsnSubStatIcmpPortUsageHi_Type()
)
tmnxNatLsnSubStatIcmpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatIcmpPortUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatUdpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatUdpPortUsage_Object = MibTableColumn
tmnxNatLsnSubStatUdpPortUsage = _TmnxNatLsnSubStatUdpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 5),
    _TmnxNatLsnSubStatUdpPortUsage_Type()
)
tmnxNatLsnSubStatUdpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatUdpPortUsage.setStatus("obsolete")
_TmnxNatLsnSubStatUdpPortUsageHi_Type = TruthValue
_TmnxNatLsnSubStatUdpPortUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatUdpPortUsageHi = _TmnxNatLsnSubStatUdpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 6),
    _TmnxNatLsnSubStatUdpPortUsageHi_Type()
)
tmnxNatLsnSubStatUdpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatUdpPortUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatTcpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatTcpPortUsage_Object = MibTableColumn
tmnxNatLsnSubStatTcpPortUsage = _TmnxNatLsnSubStatTcpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 7),
    _TmnxNatLsnSubStatTcpPortUsage_Type()
)
tmnxNatLsnSubStatTcpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatTcpPortUsage.setStatus("obsolete")
_TmnxNatLsnSubStatTcpPortUsageHi_Type = TruthValue
_TmnxNatLsnSubStatTcpPortUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatTcpPortUsageHi = _TmnxNatLsnSubStatTcpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 8),
    _TmnxNatLsnSubStatTcpPortUsageHi_Type()
)
tmnxNatLsnSubStatTcpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatTcpPortUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatSessionUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatSessionUsage_Object = MibTableColumn
tmnxNatLsnSubStatSessionUsage = _TmnxNatLsnSubStatSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 9),
    _TmnxNatLsnSubStatSessionUsage_Type()
)
tmnxNatLsnSubStatSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionUsage.setStatus("obsolete")
_TmnxNatLsnSubStatSessionUsageHi_Type = TruthValue
_TmnxNatLsnSubStatSessionUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatSessionUsageHi = _TmnxNatLsnSubStatSessionUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 10),
    _TmnxNatLsnSubStatSessionUsageHi_Type()
)
tmnxNatLsnSubStatSessionUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatSessions_Type = Gauge32
_TmnxNatLsnSubStatSessions_Object = MibTableColumn
tmnxNatLsnSubStatSessions = _TmnxNatLsnSubStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 11),
    _TmnxNatLsnSubStatSessions_Type()
)
tmnxNatLsnSubStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessions.setStatus("obsolete")
_TmnxNatLsnSubStatSessionsPrio_Type = Gauge32
_TmnxNatLsnSubStatSessionsPrio_Object = MibTableColumn
tmnxNatLsnSubStatSessionsPrio = _TmnxNatLsnSubStatSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 12),
    _TmnxNatLsnSubStatSessionsPrio_Type()
)
tmnxNatLsnSubStatSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionsPrio.setStatus("obsolete")
_TmnxNatLsnSubStatSessionsPeak_Type = Gauge32
_TmnxNatLsnSubStatSessionsPeak_Object = MibTableColumn
tmnxNatLsnSubStatSessionsPeak = _TmnxNatLsnSubStatSessionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 13),
    _TmnxNatLsnSubStatSessionsPeak_Type()
)
tmnxNatLsnSubStatSessionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionsPeak.setStatus("obsolete")
_TmnxNatLsnSubBlkTable_Object = MibTable
tmnxNatLsnSubBlkTable = _TmnxNatLsnSubBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkTable.setStatus("current")
_TmnxNatLsnSubBlkEntry_Object = MibTableRow
tmnxNatLsnSubBlkEntry = _TmnxNatLsnSubBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4, 1)
)
tmnxNatLsnSubBlkEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnStart"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkEntry.setStatus("current")
_TmnxNatLsnSubBlkEnd_Type = InetPortNumber
_TmnxNatLsnSubBlkEnd_Object = MibTableColumn
tmnxNatLsnSubBlkEnd = _TmnxNatLsnSubBlkEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4, 1, 1),
    _TmnxNatLsnSubBlkEnd_Type()
)
tmnxNatLsnSubBlkEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkEnd.setStatus("current")
_TmnxNatLsnSubBlkPolicy_Type = TNamedItemOrEmpty
_TmnxNatLsnSubBlkPolicy_Object = MibTableColumn
tmnxNatLsnSubBlkPolicy = _TmnxNatLsnSubBlkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4, 1, 2),
    _TmnxNatLsnSubBlkPolicy_Type()
)
tmnxNatLsnSubBlkPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkPolicy.setStatus("current")
_TmnxNatDsliteSubTable_Object = MibTable
tmnxNatDsliteSubTable = _TmnxNatDsliteSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxNatDsliteSubTable.setStatus("obsolete")
_TmnxNatDsliteSubEntry_Object = MibTableRow
tmnxNatDsliteSubEntry = _TmnxNatDsliteSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1)
)
tmnxNatDsliteSubEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteSubAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteSubAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteSubAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNatDsliteSubEntry.setStatus("obsolete")
_TmnxNatDsliteSubAddrType_Type = InetAddressType
_TmnxNatDsliteSubAddrType_Object = MibTableColumn
tmnxNatDsliteSubAddrType = _TmnxNatDsliteSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 1),
    _TmnxNatDsliteSubAddrType_Type()
)
tmnxNatDsliteSubAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubAddrType.setStatus("obsolete")


class _TmnxNatDsliteSubAddr_Type(InetAddress):
    """Custom type tmnxNatDsliteSubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxNatDsliteSubAddr_Type.__name__ = "InetAddress"
_TmnxNatDsliteSubAddr_Object = MibTableColumn
tmnxNatDsliteSubAddr = _TmnxNatDsliteSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 2),
    _TmnxNatDsliteSubAddr_Type()
)
tmnxNatDsliteSubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubAddr.setStatus("obsolete")


class _TmnxNatDsliteSubAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDsliteSubAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatDsliteSubAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDsliteSubAddrPrefixLength_Object = MibTableColumn
tmnxNatDsliteSubAddrPrefixLength = _TmnxNatDsliteSubAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 3),
    _TmnxNatDsliteSubAddrPrefixLength_Type()
)
tmnxNatDsliteSubAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubAddrPrefixLength.setStatus("obsolete")
_TmnxNatDsliteSubId_Type = Unsigned32
_TmnxNatDsliteSubId_Object = MibTableColumn
tmnxNatDsliteSubId = _TmnxNatDsliteSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 4),
    _TmnxNatDsliteSubId_Type()
)
tmnxNatDsliteSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubId.setStatus("obsolete")
_TmnxNatL2AwHostTable_Object = MibTable
tmnxNatL2AwHostTable = _TmnxNatL2AwHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwHostTable.setStatus("current")
_TmnxNatL2AwHostEntry_Object = MibTableRow
tmnxNatL2AwHostEntry = _TmnxNatL2AwHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1)
)
tmnxNatL2AwHostEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwHostEntry.setStatus("current")
_TmnxNatL2AwHostAddrType_Type = InetAddressType
_TmnxNatL2AwHostAddrType_Object = MibTableColumn
tmnxNatL2AwHostAddrType = _TmnxNatL2AwHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 1),
    _TmnxNatL2AwHostAddrType_Type()
)
tmnxNatL2AwHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostAddrType.setStatus("current")


class _TmnxNatL2AwHostAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostAddr_Object = MibTableColumn
tmnxNatL2AwHostAddr = _TmnxNatL2AwHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 2),
    _TmnxNatL2AwHostAddr_Type()
)
tmnxNatL2AwHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostAddr.setStatus("current")
_TmnxNatL2AwHostOutVRtrID_Type = TmnxVRtrID
_TmnxNatL2AwHostOutVRtrID_Object = MibTableColumn
tmnxNatL2AwHostOutVRtrID = _TmnxNatL2AwHostOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 3),
    _TmnxNatL2AwHostOutVRtrID_Type()
)
tmnxNatL2AwHostOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutVRtrID.setStatus("current")
_TmnxNatL2AwHostOutAddrType_Type = InetAddressType
_TmnxNatL2AwHostOutAddrType_Object = MibTableColumn
tmnxNatL2AwHostOutAddrType = _TmnxNatL2AwHostOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 4),
    _TmnxNatL2AwHostOutAddrType_Type()
)
tmnxNatL2AwHostOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutAddrType.setStatus("current")


class _TmnxNatL2AwHostOutAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostOutAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostOutAddr_Object = MibTableColumn
tmnxNatL2AwHostOutAddr = _TmnxNatL2AwHostOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 5),
    _TmnxNatL2AwHostOutAddr_Type()
)
tmnxNatL2AwHostOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutAddr.setStatus("current")
_TmnxNatL2AwHostOutStart_Type = InetPortNumber
_TmnxNatL2AwHostOutStart_Object = MibTableColumn
tmnxNatL2AwHostOutStart = _TmnxNatL2AwHostOutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 6),
    _TmnxNatL2AwHostOutStart_Type()
)
tmnxNatL2AwHostOutStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutStart.setStatus("current")
_TmnxNatL2AwSubTable_Object = MibTable
tmnxNatL2AwSubTable = _TmnxNatL2AwSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubTable.setStatus("current")
_TmnxNatL2AwSubEntry_Object = MibTableRow
tmnxNatL2AwSubEntry = _TmnxNatL2AwSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1)
)
tmnxNatL2AwSubEntry.setIndexNames(
    (1, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubEntry.setStatus("current")
_TmnxNatL2AwSubPolicy_Type = TNamedItem
_TmnxNatL2AwSubPolicy_Object = MibTableColumn
tmnxNatL2AwSubPolicy = _TmnxNatL2AwSubPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 1),
    _TmnxNatL2AwSubPolicy_Type()
)
tmnxNatL2AwSubPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPolicy.setStatus("current")
_TmnxNatL2AwSubIsaGrp_Type = TmnxNatIsaGrpIdOrZero
_TmnxNatL2AwSubIsaGrp_Object = MibTableColumn
tmnxNatL2AwSubIsaGrp = _TmnxNatL2AwSubIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 2),
    _TmnxNatL2AwSubIsaGrp_Type()
)
tmnxNatL2AwSubIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubIsaGrp.setStatus("current")
_TmnxNatL2AwSubIsaMemberId_Type = Unsigned32
_TmnxNatL2AwSubIsaMemberId_Object = MibTableColumn
tmnxNatL2AwSubIsaMemberId = _TmnxNatL2AwSubIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 3),
    _TmnxNatL2AwSubIsaMemberId_Type()
)
tmnxNatL2AwSubIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubIsaMemberId.setStatus("current")
_TmnxNatL2AwSubOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatL2AwSubOutVRtrID_Object = MibTableColumn
tmnxNatL2AwSubOutVRtrID = _TmnxNatL2AwSubOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 4),
    _TmnxNatL2AwSubOutVRtrID_Type()
)
tmnxNatL2AwSubOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubOutVRtrID.setStatus("current")
_TmnxNatL2AwSubOutAddrType_Type = InetAddressType
_TmnxNatL2AwSubOutAddrType_Object = MibTableColumn
tmnxNatL2AwSubOutAddrType = _TmnxNatL2AwSubOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 5),
    _TmnxNatL2AwSubOutAddrType_Type()
)
tmnxNatL2AwSubOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubOutAddrType.setStatus("current")


class _TmnxNatL2AwSubOutAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwSubOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwSubOutAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwSubOutAddr_Object = MibTableColumn
tmnxNatL2AwSubOutAddr = _TmnxNatL2AwSubOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 6),
    _TmnxNatL2AwSubOutAddr_Type()
)
tmnxNatL2AwSubOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubOutAddr.setStatus("current")
_TmnxNatL2AwSubStatTable_Object = MibTable
tmnxNatL2AwSubStatTable = _TmnxNatL2AwSubStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatTable.setStatus("current")
_TmnxNatL2AwSubStatEntry_Object = MibTableRow
tmnxNatL2AwSubStatEntry = _TmnxNatL2AwSubStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatEntry.setStatus("current")
_TmnxNatL2AwSubStatIcmpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatIcmpPortUsage_Object = MibTableColumn
tmnxNatL2AwSubStatIcmpPortUsage = _TmnxNatL2AwSubStatIcmpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 3),
    _TmnxNatL2AwSubStatIcmpPortUsage_Type()
)
tmnxNatL2AwSubStatIcmpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatIcmpPortUsage.setStatus("current")
_TmnxNatL2AwSubStatIcmpPortUsageH_Type = TruthValue
_TmnxNatL2AwSubStatIcmpPortUsageH_Object = MibTableColumn
tmnxNatL2AwSubStatIcmpPortUsageH = _TmnxNatL2AwSubStatIcmpPortUsageH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 4),
    _TmnxNatL2AwSubStatIcmpPortUsageH_Type()
)
tmnxNatL2AwSubStatIcmpPortUsageH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatIcmpPortUsageH.setStatus("current")
_TmnxNatL2AwSubStatUdpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatUdpPortUsage_Object = MibTableColumn
tmnxNatL2AwSubStatUdpPortUsage = _TmnxNatL2AwSubStatUdpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 5),
    _TmnxNatL2AwSubStatUdpPortUsage_Type()
)
tmnxNatL2AwSubStatUdpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatUdpPortUsage.setStatus("current")
_TmnxNatL2AwSubStatUdpPortUsageHi_Type = TruthValue
_TmnxNatL2AwSubStatUdpPortUsageHi_Object = MibTableColumn
tmnxNatL2AwSubStatUdpPortUsageHi = _TmnxNatL2AwSubStatUdpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 6),
    _TmnxNatL2AwSubStatUdpPortUsageHi_Type()
)
tmnxNatL2AwSubStatUdpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatUdpPortUsageHi.setStatus("current")
_TmnxNatL2AwSubStatTcpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatTcpPortUsage_Object = MibTableColumn
tmnxNatL2AwSubStatTcpPortUsage = _TmnxNatL2AwSubStatTcpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 7),
    _TmnxNatL2AwSubStatTcpPortUsage_Type()
)
tmnxNatL2AwSubStatTcpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatTcpPortUsage.setStatus("current")
_TmnxNatL2AwSubStatTcpPortUsageHi_Type = TruthValue
_TmnxNatL2AwSubStatTcpPortUsageHi_Object = MibTableColumn
tmnxNatL2AwSubStatTcpPortUsageHi = _TmnxNatL2AwSubStatTcpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 8),
    _TmnxNatL2AwSubStatTcpPortUsageHi_Type()
)
tmnxNatL2AwSubStatTcpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatTcpPortUsageHi.setStatus("current")
_TmnxNatL2AwSubStatSessionUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatSessionUsage_Object = MibTableColumn
tmnxNatL2AwSubStatSessionUsage = _TmnxNatL2AwSubStatSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 9),
    _TmnxNatL2AwSubStatSessionUsage_Type()
)
tmnxNatL2AwSubStatSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionUsage.setStatus("current")
_TmnxNatL2AwSubStatSessionUsageHi_Type = TruthValue
_TmnxNatL2AwSubStatSessionUsageHi_Object = MibTableColumn
tmnxNatL2AwSubStatSessionUsageHi = _TmnxNatL2AwSubStatSessionUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 10),
    _TmnxNatL2AwSubStatSessionUsageHi_Type()
)
tmnxNatL2AwSubStatSessionUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionUsageHi.setStatus("current")
_TmnxNatL2AwSubStatSessions_Type = Gauge32
_TmnxNatL2AwSubStatSessions_Object = MibTableColumn
tmnxNatL2AwSubStatSessions = _TmnxNatL2AwSubStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 11),
    _TmnxNatL2AwSubStatSessions_Type()
)
tmnxNatL2AwSubStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessions.setStatus("current")
_TmnxNatL2AwSubStatSessionsPrio_Type = Gauge32
_TmnxNatL2AwSubStatSessionsPrio_Object = MibTableColumn
tmnxNatL2AwSubStatSessionsPrio = _TmnxNatL2AwSubStatSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 12),
    _TmnxNatL2AwSubStatSessionsPrio_Type()
)
tmnxNatL2AwSubStatSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionsPrio.setStatus("current")
_TmnxNatL2AwSubStatSessionsPeak_Type = Gauge32
_TmnxNatL2AwSubStatSessionsPeak_Object = MibTableColumn
tmnxNatL2AwSubStatSessionsPeak = _TmnxNatL2AwSubStatSessionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 13),
    _TmnxNatL2AwSubStatSessionsPeak_Type()
)
tmnxNatL2AwSubStatSessionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionsPeak.setStatus("current")
_TmnxNatL2AwSubBlkTable_Object = MibTable
tmnxNatL2AwSubBlkTable = _TmnxNatL2AwSubBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkTable.setStatus("current")
_TmnxNatL2AwSubBlkEntry_Object = MibTableRow
tmnxNatL2AwSubBlkEntry = _TmnxNatL2AwSubBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14, 1)
)
tmnxNatL2AwSubBlkEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStart"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkEntry.setStatus("current")
_TmnxNatL2AwSubBlkEnd_Type = InetPortNumber
_TmnxNatL2AwSubBlkEnd_Object = MibTableColumn
tmnxNatL2AwSubBlkEnd = _TmnxNatL2AwSubBlkEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14, 1, 1),
    _TmnxNatL2AwSubBlkEnd_Type()
)
tmnxNatL2AwSubBlkEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkEnd.setStatus("current")
_TmnxNat64SubTable_Object = MibTable
tmnxNat64SubTable = _TmnxNat64SubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15)
)
if mibBuilder.loadTexts:
    tmnxNat64SubTable.setStatus("obsolete")
_TmnxNat64SubEntry_Object = MibTableRow
tmnxNat64SubEntry = _TmnxNat64SubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1)
)
tmnxNat64SubEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNat64SubAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNat64SubAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNat64SubAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNat64SubEntry.setStatus("obsolete")
_TmnxNat64SubAddrType_Type = InetAddressType
_TmnxNat64SubAddrType_Object = MibTableColumn
tmnxNat64SubAddrType = _TmnxNat64SubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 1),
    _TmnxNat64SubAddrType_Type()
)
tmnxNat64SubAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNat64SubAddrType.setStatus("obsolete")


class _TmnxNat64SubAddr_Type(InetAddress):
    """Custom type tmnxNat64SubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxNat64SubAddr_Type.__name__ = "InetAddress"
_TmnxNat64SubAddr_Object = MibTableColumn
tmnxNat64SubAddr = _TmnxNat64SubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 2),
    _TmnxNat64SubAddr_Type()
)
tmnxNat64SubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNat64SubAddr.setStatus("obsolete")


class _TmnxNat64SubAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNat64SubAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNat64SubAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNat64SubAddrPrefixLength_Object = MibTableColumn
tmnxNat64SubAddrPrefixLength = _TmnxNat64SubAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 3),
    _TmnxNat64SubAddrPrefixLength_Type()
)
tmnxNat64SubAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNat64SubAddrPrefixLength.setStatus("obsolete")
_TmnxNat64SubId_Type = Unsigned32
_TmnxNat64SubId_Object = MibTableColumn
tmnxNat64SubId = _TmnxNat64SubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 4),
    _TmnxNat64SubId_Type()
)
tmnxNat64SubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNat64SubId.setStatus("obsolete")
_TmnxNatLsnSubscIdStrTable_Object = MibTable
tmnxNatLsnSubscIdStrTable = _TmnxNatLsnSubscIdStrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrTable.setStatus("current")
_TmnxNatLsnSubscIdStrEntry_Object = MibTableRow
tmnxNatLsnSubscIdStrEntry = _TmnxNatLsnSubscIdStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1)
)
tmnxNatLsnSubscIdStrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrType"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrEntry.setStatus("current")


class _TmnxNatLsnSubscIdStr_Type(TmnxNatSubscriberIdString):
    """Custom type tmnxNatLsnSubscIdStr based on TmnxNatSubscriberIdString"""
    subtypeSpec = TmnxNatSubscriberIdString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatLsnSubscIdStr_Type.__name__ = "TmnxNatSubscriberIdString"
_TmnxNatLsnSubscIdStr_Object = MibTableColumn
tmnxNatLsnSubscIdStr = _TmnxNatLsnSubscIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 1),
    _TmnxNatLsnSubscIdStr_Type()
)
tmnxNatLsnSubscIdStr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStr.setStatus("current")


class _TmnxNatLsnSubscIdStrType_Type(TmnxNatSubscriberType):
    """Custom type tmnxNatLsnSubscIdStrType based on TmnxNatSubscriberType"""
    subtypeSpec = TmnxNatSubscriberType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TmnxNatLsnSubscIdStrType_Type.__name__ = "TmnxNatSubscriberType"
_TmnxNatLsnSubscIdStrType_Object = MibTableColumn
tmnxNatLsnSubscIdStrType = _TmnxNatLsnSubscIdStrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 2),
    _TmnxNatLsnSubscIdStrType_Type()
)
tmnxNatLsnSubscIdStrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrType.setStatus("current")
_TmnxNatLsnSubscIdStrAddrType_Type = InetAddressType
_TmnxNatLsnSubscIdStrAddrType_Object = MibTableColumn
tmnxNatLsnSubscIdStrAddrType = _TmnxNatLsnSubscIdStrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 3),
    _TmnxNatLsnSubscIdStrAddrType_Type()
)
tmnxNatLsnSubscIdStrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrAddrType.setStatus("current")


class _TmnxNatLsnSubscIdStrAddr_Type(InetAddress):
    """Custom type tmnxNatLsnSubscIdStrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnSubscIdStrAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnSubscIdStrAddr_Object = MibTableColumn
tmnxNatLsnSubscIdStrAddr = _TmnxNatLsnSubscIdStrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 4),
    _TmnxNatLsnSubscIdStrAddr_Type()
)
tmnxNatLsnSubscIdStrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrAddr.setStatus("current")
_TmnxNatLsnSubscIdStrTimeStamp_Type = TimeStamp
_TmnxNatLsnSubscIdStrTimeStamp_Object = MibTableColumn
tmnxNatLsnSubscIdStrTimeStamp = _TmnxNatLsnSubscIdStrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 5),
    _TmnxNatLsnSubscIdStrTimeStamp_Type()
)
tmnxNatLsnSubscIdStrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrTimeStamp.setStatus("current")
_TmnxNatMapObjs_ObjectIdentity = ObjectIdentity
tmnxNatMapObjs = _TmnxNatMapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7)
)
_TmnxNatMapLsnHostTable_Object = MibTable
tmnxNatMapLsnHostTable = _TmnxNatMapLsnHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostTable.setStatus("obsolete")
_TmnxNatMapLsnHostEntry_Object = MibTableRow
tmnxNatMapLsnHostEntry = _TmnxNatMapLsnHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1)
)
tmnxNatMapLsnHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostEntry.setStatus("obsolete")
_TmnxNatMapLsnHostAddrType_Type = InetAddressType
_TmnxNatMapLsnHostAddrType_Object = MibTableColumn
tmnxNatMapLsnHostAddrType = _TmnxNatMapLsnHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 1),
    _TmnxNatMapLsnHostAddrType_Type()
)
tmnxNatMapLsnHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostAddrType.setStatus("obsolete")


class _TmnxNatMapLsnHostAddr_Type(InetAddress):
    """Custom type tmnxNatMapLsnHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapLsnHostAddr_Type.__name__ = "InetAddress"
_TmnxNatMapLsnHostAddr_Object = MibTableColumn
tmnxNatMapLsnHostAddr = _TmnxNatMapLsnHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 2),
    _TmnxNatMapLsnHostAddr_Type()
)
tmnxNatMapLsnHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostAddr.setStatus("obsolete")
_TmnxNatMapLsnHostRowStatus_Type = RowStatus
_TmnxNatMapLsnHostRowStatus_Object = MibTableColumn
tmnxNatMapLsnHostRowStatus = _TmnxNatMapLsnHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 3),
    _TmnxNatMapLsnHostRowStatus_Type()
)
tmnxNatMapLsnHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostRowStatus.setStatus("obsolete")
_TmnxNatMapLsnHostLastMgmtChange_Type = TimeStamp
_TmnxNatMapLsnHostLastMgmtChange_Object = MibTableColumn
tmnxNatMapLsnHostLastMgmtChange = _TmnxNatMapLsnHostLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 4),
    _TmnxNatMapLsnHostLastMgmtChange_Type()
)
tmnxNatMapLsnHostLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostLastMgmtChange.setStatus("obsolete")
_TmnxNatMapLsnHostAdminState_Type = TmnxAdminState
_TmnxNatMapLsnHostAdminState_Object = MibTableColumn
tmnxNatMapLsnHostAdminState = _TmnxNatMapLsnHostAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 5),
    _TmnxNatMapLsnHostAdminState_Type()
)
tmnxNatMapLsnHostAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostAdminState.setStatus("obsolete")
_TmnxNatMapLsnHostOutAddrType_Type = InetAddressType
_TmnxNatMapLsnHostOutAddrType_Object = MibTableColumn
tmnxNatMapLsnHostOutAddrType = _TmnxNatMapLsnHostOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 6),
    _TmnxNatMapLsnHostOutAddrType_Type()
)
tmnxNatMapLsnHostOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostOutAddrType.setStatus("obsolete")


class _TmnxNatMapLsnHostOutAddr_Type(InetAddress):
    """Custom type tmnxNatMapLsnHostOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapLsnHostOutAddr_Type.__name__ = "InetAddress"
_TmnxNatMapLsnHostOutAddr_Object = MibTableColumn
tmnxNatMapLsnHostOutAddr = _TmnxNatMapLsnHostOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 7),
    _TmnxNatMapLsnHostOutAddr_Type()
)
tmnxNatMapLsnHostOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostOutAddr.setStatus("obsolete")
_TmnxNatMapLsnHostOutVRtrID_Type = TmnxVRtrID
_TmnxNatMapLsnHostOutVRtrID_Object = MibTableColumn
tmnxNatMapLsnHostOutVRtrID = _TmnxNatMapLsnHostOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 8),
    _TmnxNatMapLsnHostOutVRtrID_Type()
)
tmnxNatMapLsnHostOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostOutVRtrID.setStatus("obsolete")
_TmnxNatMapTable_Object = MibTable
tmnxNatMapTable = _TmnxNatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2)
)
if mibBuilder.loadTexts:
    tmnxNatMapTable.setStatus("obsolete")
_TmnxNatMapEntry_Object = MibTableRow
tmnxNatMapEntry = _TmnxNatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1)
)
tmnxNatMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapPort"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapProtocol"),
)
if mibBuilder.loadTexts:
    tmnxNatMapEntry.setStatus("obsolete")
_TmnxNatMapAddrType_Type = InetAddressType
_TmnxNatMapAddrType_Object = MibTableColumn
tmnxNatMapAddrType = _TmnxNatMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 1),
    _TmnxNatMapAddrType_Type()
)
tmnxNatMapAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapAddrType.setStatus("obsolete")


class _TmnxNatMapAddr_Type(InetAddress):
    """Custom type tmnxNatMapAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapAddr_Type.__name__ = "InetAddress"
_TmnxNatMapAddr_Object = MibTableColumn
tmnxNatMapAddr = _TmnxNatMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 2),
    _TmnxNatMapAddr_Type()
)
tmnxNatMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapAddr.setStatus("obsolete")


class _TmnxNatMapPort_Type(Unsigned32):
    """Custom type tmnxNatMapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TmnxNatMapPort_Type.__name__ = "Unsigned32"
_TmnxNatMapPort_Object = MibTableColumn
tmnxNatMapPort = _TmnxNatMapPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 3),
    _TmnxNatMapPort_Type()
)
tmnxNatMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapPort.setStatus("obsolete")


class _TmnxNatMapProtocol_Type(TIpProtocol):
    """Custom type tmnxNatMapProtocol based on TIpProtocol"""
    subtypeSpec = TIpProtocol.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(17, 17),
    )


_TmnxNatMapProtocol_Type.__name__ = "TIpProtocol"
_TmnxNatMapProtocol_Object = MibTableColumn
tmnxNatMapProtocol = _TmnxNatMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 4),
    _TmnxNatMapProtocol_Type()
)
tmnxNatMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapProtocol.setStatus("obsolete")
_TmnxNatMapRowStatus_Type = RowStatus
_TmnxNatMapRowStatus_Object = MibTableColumn
tmnxNatMapRowStatus = _TmnxNatMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 5),
    _TmnxNatMapRowStatus_Type()
)
tmnxNatMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRowStatus.setStatus("obsolete")
_TmnxNatMapLastMgmtChange_Type = TimeStamp
_TmnxNatMapLastMgmtChange_Object = MibTableColumn
tmnxNatMapLastMgmtChange = _TmnxNatMapLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 6),
    _TmnxNatMapLastMgmtChange_Type()
)
tmnxNatMapLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLastMgmtChange.setStatus("obsolete")


class _TmnxNatMapOutPort_Type(Unsigned32):
    """Custom type tmnxNatMapOutPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TmnxNatMapOutPort_Type.__name__ = "Unsigned32"
_TmnxNatMapOutPort_Object = MibTableColumn
tmnxNatMapOutPort = _TmnxNatMapOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 7),
    _TmnxNatMapOutPort_Type()
)
tmnxNatMapOutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapOutPort.setStatus("obsolete")
_TmnxNatFwdObjs_ObjectIdentity = ObjectIdentity
tmnxNatFwdObjs = _TmnxNatFwdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8)
)
_TmnxNatFwdAction_ObjectIdentity = ObjectIdentity
tmnxNatFwdAction = _TmnxNatFwdAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1)
)
_TmnxNatFwdActionSubType_Type = TmnxNatPlType
_TmnxNatFwdActionSubType_Object = MibScalar
tmnxNatFwdActionSubType = _TmnxNatFwdActionSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 1),
    _TmnxNatFwdActionSubType_Type()
)
tmnxNatFwdActionSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionSubType.setStatus("current")
_TmnxNatFwdActionVRtrId_Type = TmnxVRtrID
_TmnxNatFwdActionVRtrId_Object = MibScalar
tmnxNatFwdActionVRtrId = _TmnxNatFwdActionVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 2),
    _TmnxNatFwdActionVRtrId_Type()
)
tmnxNatFwdActionVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionVRtrId.setStatus("current")


class _TmnxNatFwdActionAddrType_Type(InetAddressType):
    """Custom type tmnxNatFwdActionAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxNatFwdActionAddrType_Type.__name__ = "InetAddressType"
_TmnxNatFwdActionAddrType_Object = MibScalar
tmnxNatFwdActionAddrType = _TmnxNatFwdActionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 3),
    _TmnxNatFwdActionAddrType_Type()
)
tmnxNatFwdActionAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAddrType.setStatus("current")


class _TmnxNatFwdActionAddr_Type(InetAddress):
    """Custom type tmnxNatFwdActionAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdActionAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdActionAddr_Object = MibScalar
tmnxNatFwdActionAddr = _TmnxNatFwdActionAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 4),
    _TmnxNatFwdActionAddr_Type()
)
tmnxNatFwdActionAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAddr.setStatus("current")
_TmnxNatFwdActionB4Addr_Type = InetAddressIPv6
_TmnxNatFwdActionB4Addr_Object = MibScalar
tmnxNatFwdActionB4Addr = _TmnxNatFwdActionB4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 6),
    _TmnxNatFwdActionB4Addr_Type()
)
tmnxNatFwdActionB4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionB4Addr.setStatus("current")
_TmnxNatFwdActionAftrAddr_Type = InetAddressIPv6
_TmnxNatFwdActionAftrAddr_Object = MibScalar
tmnxNatFwdActionAftrAddr = _TmnxNatFwdActionAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 8),
    _TmnxNatFwdActionAftrAddr_Type()
)
tmnxNatFwdActionAftrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAftrAddr.setStatus("current")


class _TmnxNatFwdActionL2awSubscriberId_Type(DisplayString):
    """Custom type tmnxNatFwdActionL2awSubscriberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatFwdActionL2awSubscriberId_Type.__name__ = "DisplayString"
_TmnxNatFwdActionL2awSubscriberId_Object = MibScalar
tmnxNatFwdActionL2awSubscriberId = _TmnxNatFwdActionL2awSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 9),
    _TmnxNatFwdActionL2awSubscriberId_Type()
)
tmnxNatFwdActionL2awSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionL2awSubscriberId.setStatus("current")


class _TmnxNatFwdActionProtocol_Type(Unsigned32):
    """Custom type tmnxNatFwdActionProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwdActionProtocol_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionProtocol_Object = MibScalar
tmnxNatFwdActionProtocol = _TmnxNatFwdActionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 10),
    _TmnxNatFwdActionProtocol_Type()
)
tmnxNatFwdActionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionProtocol.setStatus("current")


class _TmnxNatFwdActionTimeOut_Type(Unsigned32):
    """Custom type tmnxNatFwdActionTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatFwdActionTimeOut_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionTimeOut_Object = MibScalar
tmnxNatFwdActionTimeOut = _TmnxNatFwdActionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 11),
    _TmnxNatFwdActionTimeOut_Type()
)
tmnxNatFwdActionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatFwdActionTimeOut.setUnits("seconds")


class _TmnxNatFwdActionPort_Type(Unsigned32):
    """Custom type tmnxNatFwdActionPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatFwdActionPort_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionPort_Object = MibScalar
tmnxNatFwdActionPort = _TmnxNatFwdActionPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 12),
    _TmnxNatFwdActionPort_Type()
)
tmnxNatFwdActionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionPort.setStatus("current")


class _TmnxNatFwdActionOutPort_Type(Unsigned32):
    """Custom type tmnxNatFwdActionOutPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatFwdActionOutPort_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionOutPort_Object = MibScalar
tmnxNatFwdActionOutPort = _TmnxNatFwdActionOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 13),
    _TmnxNatFwdActionOutPort_Type()
)
tmnxNatFwdActionOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionOutPort.setStatus("current")
_TmnxNatFwdActionOutAddr_Type = InetAddressIPv4
_TmnxNatFwdActionOutAddr_Object = MibScalar
tmnxNatFwdActionOutAddr = _TmnxNatFwdActionOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 15),
    _TmnxNatFwdActionOutAddr_Type()
)
tmnxNatFwdActionOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionOutAddr.setStatus("current")
_TmnxNatFwdActionType_Type = TmnxNatFwdActionType
_TmnxNatFwdActionType_Object = MibScalar
tmnxNatFwdActionType = _TmnxNatFwdActionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 16),
    _TmnxNatFwdActionType_Type()
)
tmnxNatFwdActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionType.setStatus("current")
_TmnxNatFwdActionGo_Type = TmnxActionType
_TmnxNatFwdActionGo_Object = MibScalar
tmnxNatFwdActionGo = _TmnxNatFwdActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 17),
    _TmnxNatFwdActionGo_Type()
)
tmnxNatFwdActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionGo.setStatus("current")
_TmnxNatFwdActionSuccessful_Type = TruthValue
_TmnxNatFwdActionSuccessful_Object = MibScalar
tmnxNatFwdActionSuccessful = _TmnxNatFwdActionSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 18),
    _TmnxNatFwdActionSuccessful_Type()
)
tmnxNatFwdActionSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdActionSuccessful.setStatus("current")
_TmnxNatFwdActionTime_Type = TimeStamp
_TmnxNatFwdActionTime_Object = MibScalar
tmnxNatFwdActionTime = _TmnxNatFwdActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 19),
    _TmnxNatFwdActionTime_Type()
)
tmnxNatFwdActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdActionTime.setStatus("current")
_TmnxNatFwdActionDescription_Type = TmnxNatFwdEntryDescription
_TmnxNatFwdActionDescription_Object = MibScalar
tmnxNatFwdActionDescription = _TmnxNatFwdActionDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 20),
    _TmnxNatFwdActionDescription_Type()
)
tmnxNatFwdActionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionDescription.setStatus("current")
_TmnxNatFwdActionNatPolicy_Type = TNamedItemOrEmpty
_TmnxNatFwdActionNatPolicy_Object = MibScalar
tmnxNatFwdActionNatPolicy = _TmnxNatFwdActionNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 21),
    _TmnxNatFwdActionNatPolicy_Type()
)
tmnxNatFwdActionNatPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionNatPolicy.setStatus("current")
_TmnxNatFwdTable_Object = MibTable
tmnxNatFwdTable = _TmnxNatFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5)
)
if mibBuilder.loadTexts:
    tmnxNatFwdTable.setStatus("obsolete")
_TmnxNatFwdEntry_Object = MibTableRow
tmnxNatFwdEntry = _TmnxNatFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1)
)
tmnxNatFwdEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdSubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2awSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdLsnVRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdLsnB4AddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdLsnB4Addr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdProtocol"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdPort"),
)
if mibBuilder.loadTexts:
    tmnxNatFwdEntry.setStatus("obsolete")
_TmnxNatFwdSubType_Type = TmnxNatSubscriberType
_TmnxNatFwdSubType_Object = MibTableColumn
tmnxNatFwdSubType = _TmnxNatFwdSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 1),
    _TmnxNatFwdSubType_Type()
)
tmnxNatFwdSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdSubType.setStatus("obsolete")


class _TmnxNatFwdL2awSubIdent_Type(DisplayString):
    """Custom type tmnxNatFwdL2awSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxNatFwdL2awSubIdent_Type.__name__ = "DisplayString"
_TmnxNatFwdL2awSubIdent_Object = MibTableColumn
tmnxNatFwdL2awSubIdent = _TmnxNatFwdL2awSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 2),
    _TmnxNatFwdL2awSubIdent_Type()
)
tmnxNatFwdL2awSubIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2awSubIdent.setStatus("obsolete")
_TmnxNatFwdLsnVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwdLsnVRtrID_Object = MibTableColumn
tmnxNatFwdLsnVRtrID = _TmnxNatFwdLsnVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 3),
    _TmnxNatFwdLsnVRtrID_Type()
)
tmnxNatFwdLsnVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnVRtrID.setStatus("obsolete")
_TmnxNatFwdLsnB4AddrType_Type = InetAddressType
_TmnxNatFwdLsnB4AddrType_Object = MibTableColumn
tmnxNatFwdLsnB4AddrType = _TmnxNatFwdLsnB4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 4),
    _TmnxNatFwdLsnB4AddrType_Type()
)
tmnxNatFwdLsnB4AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnB4AddrType.setStatus("obsolete")


class _TmnxNatFwdLsnB4Addr_Type(InetAddress):
    """Custom type tmnxNatFwdLsnB4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdLsnB4Addr_Type.__name__ = "InetAddress"
_TmnxNatFwdLsnB4Addr_Object = MibTableColumn
tmnxNatFwdLsnB4Addr = _TmnxNatFwdLsnB4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 5),
    _TmnxNatFwdLsnB4Addr_Type()
)
tmnxNatFwdLsnB4Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnB4Addr.setStatus("obsolete")
_TmnxNatFwdAddrType_Type = InetAddressType
_TmnxNatFwdAddrType_Object = MibTableColumn
tmnxNatFwdAddrType = _TmnxNatFwdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 6),
    _TmnxNatFwdAddrType_Type()
)
tmnxNatFwdAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdAddrType.setStatus("obsolete")


class _TmnxNatFwdAddr_Type(InetAddress):
    """Custom type tmnxNatFwdAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdAddr_Object = MibTableColumn
tmnxNatFwdAddr = _TmnxNatFwdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 7),
    _TmnxNatFwdAddr_Type()
)
tmnxNatFwdAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdAddr.setStatus("obsolete")


class _TmnxNatFwdProtocol_Type(Unsigned32):
    """Custom type tmnxNatFwdProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwdProtocol_Type.__name__ = "Unsigned32"
_TmnxNatFwdProtocol_Object = MibTableColumn
tmnxNatFwdProtocol = _TmnxNatFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 8),
    _TmnxNatFwdProtocol_Type()
)
tmnxNatFwdProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdProtocol.setStatus("obsolete")
_TmnxNatFwdPort_Type = InetPortNumber
_TmnxNatFwdPort_Object = MibTableColumn
tmnxNatFwdPort = _TmnxNatFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 9),
    _TmnxNatFwdPort_Type()
)
tmnxNatFwdPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdPort.setStatus("obsolete")
_TmnxNatFwdOutVRtrID_Type = TmnxVRtrID
_TmnxNatFwdOutVRtrID_Object = MibTableColumn
tmnxNatFwdOutVRtrID = _TmnxNatFwdOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 10),
    _TmnxNatFwdOutVRtrID_Type()
)
tmnxNatFwdOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutVRtrID.setStatus("obsolete")
_TmnxNatFwdOutAddrType_Type = InetAddressType
_TmnxNatFwdOutAddrType_Object = MibTableColumn
tmnxNatFwdOutAddrType = _TmnxNatFwdOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 11),
    _TmnxNatFwdOutAddrType_Type()
)
tmnxNatFwdOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutAddrType.setStatus("obsolete")


class _TmnxNatFwdOutAddr_Type(InetAddress):
    """Custom type tmnxNatFwdOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatFwdOutAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdOutAddr_Object = MibTableColumn
tmnxNatFwdOutAddr = _TmnxNatFwdOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 12),
    _TmnxNatFwdOutAddr_Type()
)
tmnxNatFwdOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutAddr.setStatus("obsolete")
_TmnxNatFwdOutPort_Type = InetPortNumber
_TmnxNatFwdOutPort_Object = MibTableColumn
tmnxNatFwdOutPort = _TmnxNatFwdOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 13),
    _TmnxNatFwdOutPort_Type()
)
tmnxNatFwdOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutPort.setStatus("obsolete")


class _TmnxNatFwdExpiryDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatFwdExpiryDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatFwdExpiryDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatFwdExpiryDateAndTime_Object = MibTableColumn
tmnxNatFwdExpiryDateAndTime = _TmnxNatFwdExpiryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 14),
    _TmnxNatFwdExpiryDateAndTime_Type()
)
tmnxNatFwdExpiryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdExpiryDateAndTime.setStatus("obsolete")
_TmnxNatFwdLsnAftrAddrType_Type = InetAddressType
_TmnxNatFwdLsnAftrAddrType_Object = MibTableColumn
tmnxNatFwdLsnAftrAddrType = _TmnxNatFwdLsnAftrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 15),
    _TmnxNatFwdLsnAftrAddrType_Type()
)
tmnxNatFwdLsnAftrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnAftrAddrType.setStatus("obsolete")


class _TmnxNatFwdLsnAftrAddr_Type(InetAddress):
    """Custom type tmnxNatFwdLsnAftrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdLsnAftrAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdLsnAftrAddr_Object = MibTableColumn
tmnxNatFwdLsnAftrAddr = _TmnxNatFwdLsnAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 16),
    _TmnxNatFwdLsnAftrAddr_Type()
)
tmnxNatFwdLsnAftrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnAftrAddr.setStatus("obsolete")
_TmnxNatFwdPersistKey_Type = Unsigned32
_TmnxNatFwdPersistKey_Object = MibTableColumn
tmnxNatFwdPersistKey = _TmnxNatFwdPersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 17),
    _TmnxNatFwdPersistKey_Type()
)
tmnxNatFwdPersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdPersistKey.setStatus("obsolete")
_TmnxNatFwdDescription_Type = TmnxNatFwdEntryDescription
_TmnxNatFwdDescription_Object = MibTableColumn
tmnxNatFwdDescription = _TmnxNatFwdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 18),
    _TmnxNatFwdDescription_Type()
)
tmnxNatFwdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdDescription.setStatus("obsolete")


class _TmnxNatFwdOrigin_Type(Integer32):
    """Custom type tmnxNatFwdOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_TmnxNatFwdOrigin_Type.__name__ = "Integer32"
_TmnxNatFwdOrigin_Object = MibTableColumn
tmnxNatFwdOrigin = _TmnxNatFwdOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 19),
    _TmnxNatFwdOrigin_Type()
)
tmnxNatFwdOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOrigin.setStatus("obsolete")
_TmnxNatFwd2Table_Object = MibTable
tmnxNatFwd2Table = _TmnxNatFwd2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6)
)
if mibBuilder.loadTexts:
    tmnxNatFwd2Table.setStatus("current")
_TmnxNatFwd2Entry_Object = MibTableRow
tmnxNatFwd2Entry = _TmnxNatFwd2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1)
)
tmnxNatFwd2Entry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2SubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2L2awSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2LsnVRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2LsnB4AddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2LsnB4Addr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2AddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2Addr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2Protocol"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2Port"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2NatPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatFwd2Entry.setStatus("current")
_TmnxNatFwd2SubType_Type = TmnxNatSubscriberType
_TmnxNatFwd2SubType_Object = MibTableColumn
tmnxNatFwd2SubType = _TmnxNatFwd2SubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 1),
    _TmnxNatFwd2SubType_Type()
)
tmnxNatFwd2SubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2SubType.setStatus("current")


class _TmnxNatFwd2L2awSubIdent_Type(DisplayString):
    """Custom type tmnxNatFwd2L2awSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxNatFwd2L2awSubIdent_Type.__name__ = "DisplayString"
_TmnxNatFwd2L2awSubIdent_Object = MibTableColumn
tmnxNatFwd2L2awSubIdent = _TmnxNatFwd2L2awSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 2),
    _TmnxNatFwd2L2awSubIdent_Type()
)
tmnxNatFwd2L2awSubIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2L2awSubIdent.setStatus("current")
_TmnxNatFwd2LsnVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwd2LsnVRtrID_Object = MibTableColumn
tmnxNatFwd2LsnVRtrID = _TmnxNatFwd2LsnVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 3),
    _TmnxNatFwd2LsnVRtrID_Type()
)
tmnxNatFwd2LsnVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnVRtrID.setStatus("current")
_TmnxNatFwd2LsnB4AddrType_Type = InetAddressType
_TmnxNatFwd2LsnB4AddrType_Object = MibTableColumn
tmnxNatFwd2LsnB4AddrType = _TmnxNatFwd2LsnB4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 4),
    _TmnxNatFwd2LsnB4AddrType_Type()
)
tmnxNatFwd2LsnB4AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnB4AddrType.setStatus("current")


class _TmnxNatFwd2LsnB4Addr_Type(InetAddress):
    """Custom type tmnxNatFwd2LsnB4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2LsnB4Addr_Type.__name__ = "InetAddress"
_TmnxNatFwd2LsnB4Addr_Object = MibTableColumn
tmnxNatFwd2LsnB4Addr = _TmnxNatFwd2LsnB4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 5),
    _TmnxNatFwd2LsnB4Addr_Type()
)
tmnxNatFwd2LsnB4Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnB4Addr.setStatus("current")
_TmnxNatFwd2AddrType_Type = InetAddressType
_TmnxNatFwd2AddrType_Object = MibTableColumn
tmnxNatFwd2AddrType = _TmnxNatFwd2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 6),
    _TmnxNatFwd2AddrType_Type()
)
tmnxNatFwd2AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2AddrType.setStatus("current")


class _TmnxNatFwd2Addr_Type(InetAddress):
    """Custom type tmnxNatFwd2Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2Addr_Type.__name__ = "InetAddress"
_TmnxNatFwd2Addr_Object = MibTableColumn
tmnxNatFwd2Addr = _TmnxNatFwd2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 7),
    _TmnxNatFwd2Addr_Type()
)
tmnxNatFwd2Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2Addr.setStatus("current")


class _TmnxNatFwd2Protocol_Type(Unsigned32):
    """Custom type tmnxNatFwd2Protocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwd2Protocol_Type.__name__ = "Unsigned32"
_TmnxNatFwd2Protocol_Object = MibTableColumn
tmnxNatFwd2Protocol = _TmnxNatFwd2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 8),
    _TmnxNatFwd2Protocol_Type()
)
tmnxNatFwd2Protocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2Protocol.setStatus("current")
_TmnxNatFwd2Port_Type = InetPortNumber
_TmnxNatFwd2Port_Object = MibTableColumn
tmnxNatFwd2Port = _TmnxNatFwd2Port_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 9),
    _TmnxNatFwd2Port_Type()
)
tmnxNatFwd2Port.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2Port.setStatus("current")
_TmnxNatFwd2NatPolicy_Type = TNamedItemOrEmpty
_TmnxNatFwd2NatPolicy_Object = MibTableColumn
tmnxNatFwd2NatPolicy = _TmnxNatFwd2NatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 10),
    _TmnxNatFwd2NatPolicy_Type()
)
tmnxNatFwd2NatPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2NatPolicy.setStatus("current")
_TmnxNatFwd2OutVRtrID_Type = TmnxVRtrID
_TmnxNatFwd2OutVRtrID_Object = MibTableColumn
tmnxNatFwd2OutVRtrID = _TmnxNatFwd2OutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 11),
    _TmnxNatFwd2OutVRtrID_Type()
)
tmnxNatFwd2OutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutVRtrID.setStatus("current")
_TmnxNatFwd2OutAddrType_Type = InetAddressType
_TmnxNatFwd2OutAddrType_Object = MibTableColumn
tmnxNatFwd2OutAddrType = _TmnxNatFwd2OutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 12),
    _TmnxNatFwd2OutAddrType_Type()
)
tmnxNatFwd2OutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutAddrType.setStatus("current")


class _TmnxNatFwd2OutAddr_Type(InetAddress):
    """Custom type tmnxNatFwd2OutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatFwd2OutAddr_Type.__name__ = "InetAddress"
_TmnxNatFwd2OutAddr_Object = MibTableColumn
tmnxNatFwd2OutAddr = _TmnxNatFwd2OutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 13),
    _TmnxNatFwd2OutAddr_Type()
)
tmnxNatFwd2OutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutAddr.setStatus("current")
_TmnxNatFwd2OutPort_Type = InetPortNumber
_TmnxNatFwd2OutPort_Object = MibTableColumn
tmnxNatFwd2OutPort = _TmnxNatFwd2OutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 14),
    _TmnxNatFwd2OutPort_Type()
)
tmnxNatFwd2OutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutPort.setStatus("current")


class _TmnxNatFwd2ExpiryDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatFwd2ExpiryDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatFwd2ExpiryDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatFwd2ExpiryDateAndTime_Object = MibTableColumn
tmnxNatFwd2ExpiryDateAndTime = _TmnxNatFwd2ExpiryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 15),
    _TmnxNatFwd2ExpiryDateAndTime_Type()
)
tmnxNatFwd2ExpiryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ExpiryDateAndTime.setStatus("current")
_TmnxNatFwd2LsnAftrAddrType_Type = InetAddressType
_TmnxNatFwd2LsnAftrAddrType_Object = MibTableColumn
tmnxNatFwd2LsnAftrAddrType = _TmnxNatFwd2LsnAftrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 16),
    _TmnxNatFwd2LsnAftrAddrType_Type()
)
tmnxNatFwd2LsnAftrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnAftrAddrType.setStatus("current")


class _TmnxNatFwd2LsnAftrAddr_Type(InetAddress):
    """Custom type tmnxNatFwd2LsnAftrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2LsnAftrAddr_Type.__name__ = "InetAddress"
_TmnxNatFwd2LsnAftrAddr_Object = MibTableColumn
tmnxNatFwd2LsnAftrAddr = _TmnxNatFwd2LsnAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 17),
    _TmnxNatFwd2LsnAftrAddr_Type()
)
tmnxNatFwd2LsnAftrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnAftrAddr.setStatus("current")
_TmnxNatFwd2PersistKey_Type = Unsigned32
_TmnxNatFwd2PersistKey_Object = MibTableColumn
tmnxNatFwd2PersistKey = _TmnxNatFwd2PersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 18),
    _TmnxNatFwd2PersistKey_Type()
)
tmnxNatFwd2PersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2PersistKey.setStatus("current")
_TmnxNatFwd2Description_Type = TmnxNatFwdEntryDescription
_TmnxNatFwd2Description_Object = MibTableColumn
tmnxNatFwd2Description = _TmnxNatFwd2Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 19),
    _TmnxNatFwd2Description_Type()
)
tmnxNatFwd2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2Description.setStatus("current")


class _TmnxNatFwd2Origin_Type(Integer32):
    """Custom type tmnxNatFwd2Origin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_TmnxNatFwd2Origin_Type.__name__ = "Integer32"
_TmnxNatFwd2Origin_Object = MibTableColumn
tmnxNatFwd2Origin = _TmnxNatFwd2Origin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 20),
    _TmnxNatFwd2Origin_Type()
)
tmnxNatFwd2Origin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2Origin.setStatus("current")
_TmnxNatAccObjs_ObjectIdentity = ObjectIdentity
tmnxNatAccObjs = _TmnxNatAccObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9)
)
_TmnxNatApTable_Object = MibTable
tmnxNatApTable = _TmnxNatApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxNatApTable.setStatus("obsolete")
_TmnxNatApEntry_Object = MibTableRow
tmnxNatApEntry = _TmnxNatApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1)
)
tmnxNatApEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatApName"),
)
if mibBuilder.loadTexts:
    tmnxNatApEntry.setStatus("obsolete")
_TmnxNatApName_Type = TNamedItem
_TmnxNatApName_Object = MibTableColumn
tmnxNatApName = _TmnxNatApName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 1),
    _TmnxNatApName_Type()
)
tmnxNatApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatApName.setStatus("obsolete")
_TmnxNatApLastMgmtChange_Type = TimeStamp
_TmnxNatApLastMgmtChange_Object = MibTableColumn
tmnxNatApLastMgmtChange = _TmnxNatApLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 2),
    _TmnxNatApLastMgmtChange_Type()
)
tmnxNatApLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApLastMgmtChange.setStatus("obsolete")
_TmnxNatApRowStatus_Type = RowStatus
_TmnxNatApRowStatus_Object = MibTableColumn
tmnxNatApRowStatus = _TmnxNatApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 3),
    _TmnxNatApRowStatus_Type()
)
tmnxNatApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApRowStatus.setStatus("obsolete")


class _TmnxNatApDescription_Type(TItemDescription):
    """Custom type tmnxNatApDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatApDescription_Type.__name__ = "TItemDescription"
_TmnxNatApDescription_Object = MibTableColumn
tmnxNatApDescription = _TmnxNatApDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 4),
    _TmnxNatApDescription_Type()
)
tmnxNatApDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApDescription.setStatus("obsolete")


class _TmnxNatApIncludeAttributes_Type(Bits):
    """Custom type tmnxNatApIncludeAttributes based on Bits"""
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
          ("subscriberData", 15))
    )

_TmnxNatApIncludeAttributes_Type.__name__ = "Bits"
_TmnxNatApIncludeAttributes_Object = MibTableColumn
tmnxNatApIncludeAttributes = _TmnxNatApIncludeAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 5),
    _TmnxNatApIncludeAttributes_Type()
)
tmnxNatApIncludeAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApIncludeAttributes.setStatus("obsolete")


class _TmnxNatApServersTimeout_Type(Unsigned32):
    """Custom type tmnxNatApServersTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxNatApServersTimeout_Type.__name__ = "Unsigned32"
_TmnxNatApServersTimeout_Object = MibTableColumn
tmnxNatApServersTimeout = _TmnxNatApServersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 100),
    _TmnxNatApServersTimeout_Type()
)
tmnxNatApServersTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxNatApServersTimeout.setUnits("seconds")


class _TmnxNatApServersRetry_Type(Unsigned32):
    """Custom type tmnxNatApServersRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxNatApServersRetry_Type.__name__ = "Unsigned32"
_TmnxNatApServersRetry_Object = MibTableColumn
tmnxNatApServersRetry = _TmnxNatApServersRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 101),
    _TmnxNatApServersRetry_Type()
)
tmnxNatApServersRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersRetry.setStatus("obsolete")


class _TmnxNatApServersVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatApServersVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatApServersVRtrID_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatApServersVRtrID_Object = MibTableColumn
tmnxNatApServersVRtrID = _TmnxNatApServersVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 102),
    _TmnxNatApServersVRtrID_Type()
)
tmnxNatApServersVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersVRtrID.setStatus("obsolete")


class _TmnxNatApServersSrcAddrType_Type(InetAddressType):
    """Custom type tmnxNatApServersSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatApServersSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxNatApServersSrcAddrType_Object = MibTableColumn
tmnxNatApServersSrcAddrType = _TmnxNatApServersSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 103),
    _TmnxNatApServersSrcAddrType_Type()
)
tmnxNatApServersSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersSrcAddrType.setStatus("obsolete")


class _TmnxNatApServersSrcAddrStart_Type(InetAddress):
    """Custom type tmnxNatApServersSrcAddrStart based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServersSrcAddrStart_Type.__name__ = "InetAddress"
_TmnxNatApServersSrcAddrStart_Object = MibTableColumn
tmnxNatApServersSrcAddrStart = _TmnxNatApServersSrcAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 104),
    _TmnxNatApServersSrcAddrStart_Type()
)
tmnxNatApServersSrcAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersSrcAddrStart.setStatus("obsolete")


class _TmnxNatApServersSrcAddrEnd_Type(InetAddress):
    """Custom type tmnxNatApServersSrcAddrEnd based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServersSrcAddrEnd_Type.__name__ = "InetAddress"
_TmnxNatApServersSrcAddrEnd_Object = MibTableColumn
tmnxNatApServersSrcAddrEnd = _TmnxNatApServersSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 105),
    _TmnxNatApServersSrcAddrEnd_Type()
)
tmnxNatApServersSrcAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersSrcAddrEnd.setStatus("obsolete")


class _TmnxNatApServersAlgorithm_Type(TmnxSubRadServAlgorithm):
    """Custom type tmnxNatApServersAlgorithm based on TmnxSubRadServAlgorithm"""
    defaultValue = 1

    subtypeSpec = TmnxSubRadServAlgorithm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("roundRobin", 2))
    )


_TmnxNatApServersAlgorithm_Type.__name__ = "TmnxSubRadServAlgorithm"
_TmnxNatApServersAlgorithm_Object = MibTableColumn
tmnxNatApServersAlgorithm = _TmnxNatApServersAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 106),
    _TmnxNatApServersAlgorithm_Type()
)
tmnxNatApServersAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersAlgorithm.setStatus("obsolete")
_TmnxNatApServTable_Object = MibTable
tmnxNatApServTable = _TmnxNatApServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxNatApServTable.setStatus("obsolete")
_TmnxNatApServEntry_Object = MibTableRow
tmnxNatApServEntry = _TmnxNatApServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1)
)
tmnxNatApServEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatApName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatApServIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatApServEntry.setStatus("obsolete")


class _TmnxNatApServIndex_Type(Unsigned32):
    """Custom type tmnxNatApServIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxNatApServIndex_Type.__name__ = "Unsigned32"
_TmnxNatApServIndex_Object = MibTableColumn
tmnxNatApServIndex = _TmnxNatApServIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 1),
    _TmnxNatApServIndex_Type()
)
tmnxNatApServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatApServIndex.setStatus("obsolete")
_TmnxNatApServRowStatus_Type = RowStatus
_TmnxNatApServRowStatus_Object = MibTableColumn
tmnxNatApServRowStatus = _TmnxNatApServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 2),
    _TmnxNatApServRowStatus_Type()
)
tmnxNatApServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServRowStatus.setStatus("obsolete")
_TmnxNatApServLastMgmtChange_Type = TimeStamp
_TmnxNatApServLastMgmtChange_Object = MibTableColumn
tmnxNatApServLastMgmtChange = _TmnxNatApServLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 3),
    _TmnxNatApServLastMgmtChange_Type()
)
tmnxNatApServLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServLastMgmtChange.setStatus("obsolete")
_TmnxNatApServAddrType_Type = InetAddressType
_TmnxNatApServAddrType_Object = MibTableColumn
tmnxNatApServAddrType = _TmnxNatApServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 5),
    _TmnxNatApServAddrType_Type()
)
tmnxNatApServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServAddrType.setStatus("obsolete")


class _TmnxNatApServAddr_Type(InetAddress):
    """Custom type tmnxNatApServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServAddr_Type.__name__ = "InetAddress"
_TmnxNatApServAddr_Object = MibTableColumn
tmnxNatApServAddr = _TmnxNatApServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 6),
    _TmnxNatApServAddr_Type()
)
tmnxNatApServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServAddr.setStatus("obsolete")


class _TmnxNatApServSecret_Type(DisplayString):
    """Custom type tmnxNatApServSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 20),
    )


_TmnxNatApServSecret_Type.__name__ = "DisplayString"
_TmnxNatApServSecret_Object = MibTableColumn
tmnxNatApServSecret = _TmnxNatApServSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 7),
    _TmnxNatApServSecret_Type()
)
tmnxNatApServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServSecret.setStatus("obsolete")


class _TmnxNatApServAcctPort_Type(Unsigned32):
    """Custom type tmnxNatApServAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatApServAcctPort_Type.__name__ = "Unsigned32"
_TmnxNatApServAcctPort_Object = MibTableColumn
tmnxNatApServAcctPort = _TmnxNatApServAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 8),
    _TmnxNatApServAcctPort_Type()
)
tmnxNatApServAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServAcctPort.setStatus("obsolete")
_TmnxNatApServStatTable_Object = MibTable
tmnxNatApServStatTable = _TmnxNatApServStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxNatApServStatTable.setStatus("obsolete")
_TmnxNatApServStatEntry_Object = MibTableRow
tmnxNatApServStatEntry = _TmnxNatApServStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1)
)
tmnxNatApServStatEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatApName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatApServIndex"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatApServStatEntry.setStatus("obsolete")
_TmnxNatApServStatSrcAddrType_Type = InetAddressType
_TmnxNatApServStatSrcAddrType_Object = MibTableColumn
tmnxNatApServStatSrcAddrType = _TmnxNatApServStatSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 1),
    _TmnxNatApServStatSrcAddrType_Type()
)
tmnxNatApServStatSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatSrcAddrType.setStatus("obsolete")


class _TmnxNatApServStatSrcAddr_Type(InetAddress):
    """Custom type tmnxNatApServStatSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServStatSrcAddr_Type.__name__ = "InetAddress"
_TmnxNatApServStatSrcAddr_Object = MibTableColumn
tmnxNatApServStatSrcAddr = _TmnxNatApServStatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 2),
    _TmnxNatApServStatSrcAddr_Type()
)
tmnxNatApServStatSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatSrcAddr.setStatus("obsolete")
_TmnxNatApServStatOperState_Type = TmnxOperState
_TmnxNatApServStatOperState_Object = MibTableColumn
tmnxNatApServStatOperState = _TmnxNatApServStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 3),
    _TmnxNatApServStatOperState_Type()
)
tmnxNatApServStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatOperState.setStatus("obsolete")
_TmnxNatApServStatTxRequests_Type = Counter32
_TmnxNatApServStatTxRequests_Object = MibTableColumn
tmnxNatApServStatTxRequests = _TmnxNatApServStatTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 4),
    _TmnxNatApServStatTxRequests_Type()
)
tmnxNatApServStatTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatTxRequests.setStatus("obsolete")
_TmnxNatApServStatReqTimeout_Type = Counter32
_TmnxNatApServStatReqTimeout_Object = MibTableColumn
tmnxNatApServStatReqTimeout = _TmnxNatApServStatReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 6),
    _TmnxNatApServStatReqTimeout_Type()
)
tmnxNatApServStatReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatReqTimeout.setStatus("obsolete")
_TmnxNatApServStatSendRetries_Type = Counter32
_TmnxNatApServStatSendRetries_Object = MibTableColumn
tmnxNatApServStatSendRetries = _TmnxNatApServStatSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 7),
    _TmnxNatApServStatSendRetries_Type()
)
tmnxNatApServStatSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatSendRetries.setStatus("obsolete")
_TmnxNatPcpObjs_ObjectIdentity = ObjectIdentity
tmnxNatPcpObjs = _TmnxNatPcpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10)
)
_TmnxNatPcpPlcyTable_Object = MibTable
tmnxNatPcpPlcyTable = _TmnxNatPcpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyTable.setStatus("current")
_TmnxNatPcpPlcyEntry_Object = MibTableRow
tmnxNatPcpPlcyEntry = _TmnxNatPcpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1)
)
tmnxNatPcpPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatPcpPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyEntry.setStatus("current")
_TmnxNatPcpPlcyName_Type = TNamedItem
_TmnxNatPcpPlcyName_Object = MibTableColumn
tmnxNatPcpPlcyName = _TmnxNatPcpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 1),
    _TmnxNatPcpPlcyName_Type()
)
tmnxNatPcpPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyName.setStatus("current")
_TmnxNatPcpPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatPcpPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatPcpPlcyLastMgmtChange = _TmnxNatPcpPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 2),
    _TmnxNatPcpPlcyLastMgmtChange_Type()
)
tmnxNatPcpPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyLastMgmtChange.setStatus("current")
_TmnxNatPcpPlcyRowStatus_Type = RowStatus
_TmnxNatPcpPlcyRowStatus_Object = MibTableColumn
tmnxNatPcpPlcyRowStatus = _TmnxNatPcpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 3),
    _TmnxNatPcpPlcyRowStatus_Type()
)
tmnxNatPcpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyRowStatus.setStatus("current")


class _TmnxNatPcpPlcyDescription_Type(TItemDescription):
    """Custom type tmnxNatPcpPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPcpPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxNatPcpPlcyDescription_Object = MibTableColumn
tmnxNatPcpPlcyDescription = _TmnxNatPcpPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 4),
    _TmnxNatPcpPlcyDescription_Type()
)
tmnxNatPcpPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyDescription.setStatus("current")


class _TmnxNatPcpPlcyOpcodes_Type(Bits):
    """Custom type tmnxNatPcpPlcyOpcodes based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("get", 0),
          ("map", 1),
          ("announce", 2))
    )

_TmnxNatPcpPlcyOpcodes_Type.__name__ = "Bits"
_TmnxNatPcpPlcyOpcodes_Object = MibTableColumn
tmnxNatPcpPlcyOpcodes = _TmnxNatPcpPlcyOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 5),
    _TmnxNatPcpPlcyOpcodes_Type()
)
tmnxNatPcpPlcyOpcodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyOpcodes.setStatus("current")


class _TmnxNatPcpPlcyOptions_Type(Bits):
    """Custom type tmnxNatPcpPlcyOptions based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("description", 0),
          ("next", 1),
          ("portReservation", 2),
          ("thirdParty", 3),
          ("preferFailure", 4))
    )

_TmnxNatPcpPlcyOptions_Type.__name__ = "Bits"
_TmnxNatPcpPlcyOptions_Object = MibTableColumn
tmnxNatPcpPlcyOptions = _TmnxNatPcpPlcyOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 6),
    _TmnxNatPcpPlcyOptions_Type()
)
tmnxNatPcpPlcyOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyOptions.setStatus("current")


class _TmnxNatPcpPlcyMinimumLifetime_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMinimumLifetime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86399),
    )


_TmnxNatPcpPlcyMinimumLifetime_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMinimumLifetime_Object = MibTableColumn
tmnxNatPcpPlcyMinimumLifetime = _TmnxNatPcpPlcyMinimumLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 7),
    _TmnxNatPcpPlcyMinimumLifetime_Type()
)
tmnxNatPcpPlcyMinimumLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMinimumLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMinimumLifetime.setUnits("seconds")


class _TmnxNatPcpPlcyMaximumLifetime_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMaximumLifetime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(61, 86400),
    )


_TmnxNatPcpPlcyMaximumLifetime_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMaximumLifetime_Object = MibTableColumn
tmnxNatPcpPlcyMaximumLifetime = _TmnxNatPcpPlcyMaximumLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 8),
    _TmnxNatPcpPlcyMaximumLifetime_Type()
)
tmnxNatPcpPlcyMaximumLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaximumLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaximumLifetime.setUnits("seconds")


class _TmnxNatPcpPlcyMaxDescriptionLen_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMaxDescriptionLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxNatPcpPlcyMaxDescriptionLen_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMaxDescriptionLen_Object = MibTableColumn
tmnxNatPcpPlcyMaxDescriptionLen = _TmnxNatPcpPlcyMaxDescriptionLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 9),
    _TmnxNatPcpPlcyMaxDescriptionLen_Type()
)
tmnxNatPcpPlcyMaxDescriptionLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaxDescriptionLen.setStatus("current")
_TmnxNatPcpSrvTable_Object = MibTable
tmnxNatPcpSrvTable = _TmnxNatPcpSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvTable.setStatus("current")
_TmnxNatPcpSrvEntry_Object = MibTableRow
tmnxNatPcpSrvEntry = _TmnxNatPcpSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1)
)
tmnxNatPcpSrvEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvName"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvEntry.setStatus("current")
_TmnxNatPcpSrvName_Type = TNamedItem
_TmnxNatPcpSrvName_Object = MibTableColumn
tmnxNatPcpSrvName = _TmnxNatPcpSrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 1),
    _TmnxNatPcpSrvName_Type()
)
tmnxNatPcpSrvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvName.setStatus("current")
_TmnxNatPcpSrvLastCh_Type = TimeStamp
_TmnxNatPcpSrvLastCh_Object = MibTableColumn
tmnxNatPcpSrvLastCh = _TmnxNatPcpSrvLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 2),
    _TmnxNatPcpSrvLastCh_Type()
)
tmnxNatPcpSrvLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvLastCh.setStatus("current")
_TmnxNatPcpSrvRowStatus_Type = RowStatus
_TmnxNatPcpSrvRowStatus_Object = MibTableColumn
tmnxNatPcpSrvRowStatus = _TmnxNatPcpSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 3),
    _TmnxNatPcpSrvRowStatus_Type()
)
tmnxNatPcpSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvRowStatus.setStatus("current")


class _TmnxNatPcpSrvAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatPcpSrvAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatPcpSrvAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatPcpSrvAdminState_Object = MibTableColumn
tmnxNatPcpSrvAdminState = _TmnxNatPcpSrvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 4),
    _TmnxNatPcpSrvAdminState_Type()
)
tmnxNatPcpSrvAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvAdminState.setStatus("current")


class _TmnxNatPcpSrvDescription_Type(TItemDescription):
    """Custom type tmnxNatPcpSrvDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPcpSrvDescription_Type.__name__ = "TItemDescription"
_TmnxNatPcpSrvDescription_Object = MibTableColumn
tmnxNatPcpSrvDescription = _TmnxNatPcpSrvDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 5),
    _TmnxNatPcpSrvDescription_Type()
)
tmnxNatPcpSrvDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvDescription.setStatus("current")


class _TmnxNatPcpSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPcpSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPcpSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPcpSrvPlcy_Object = MibTableColumn
tmnxNatPcpSrvPlcy = _TmnxNatPcpSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 6),
    _TmnxNatPcpSrvPlcy_Type()
)
tmnxNatPcpSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvPlcy.setStatus("current")


class _TmnxNatPcpSrvFwdInsideRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPcpSrvFwdInsideRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPcpSrvFwdInsideRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPcpSrvFwdInsideRouter_Object = MibTableColumn
tmnxNatPcpSrvFwdInsideRouter = _TmnxNatPcpSrvFwdInsideRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 7),
    _TmnxNatPcpSrvFwdInsideRouter_Type()
)
tmnxNatPcpSrvFwdInsideRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvFwdInsideRouter.setStatus("current")
_TmnxNatPcpSrvDsliteAftrAddr_Type = InetAddressIPv6
_TmnxNatPcpSrvDsliteAftrAddr_Object = MibTableColumn
tmnxNatPcpSrvDsliteAftrAddr = _TmnxNatPcpSrvDsliteAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 8),
    _TmnxNatPcpSrvDsliteAftrAddr_Type()
)
tmnxNatPcpSrvDsliteAftrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvDsliteAftrAddr.setStatus("current")
_TmnxNatPcpSrvState_Type = TmnxOperState
_TmnxNatPcpSrvState_Object = MibTableColumn
tmnxNatPcpSrvState = _TmnxNatPcpSrvState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 9),
    _TmnxNatPcpSrvState_Type()
)
tmnxNatPcpSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvState.setStatus("current")


class _TmnxNatPcpSrvStateDescription_Type(DisplayString):
    """Custom type tmnxNatPcpSrvStateDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxNatPcpSrvStateDescription_Type.__name__ = "DisplayString"
_TmnxNatPcpSrvStateDescription_Object = MibTableColumn
tmnxNatPcpSrvStateDescription = _TmnxNatPcpSrvStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 10),
    _TmnxNatPcpSrvStateDescription_Type()
)
tmnxNatPcpSrvStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvStateDescription.setStatus("current")


class _TmnxNatPcpSrvEpoch_Type(Unsigned32):
    """Custom type tmnxNatPcpSrvEpoch based on Unsigned32"""
    defaultValue = 0


_TmnxNatPcpSrvEpoch_Type.__name__ = "Unsigned32"
_TmnxNatPcpSrvEpoch_Object = MibTableColumn
tmnxNatPcpSrvEpoch = _TmnxNatPcpSrvEpoch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 11),
    _TmnxNatPcpSrvEpoch_Type()
)
tmnxNatPcpSrvEpoch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvEpoch.setStatus("current")
_TmnxNatPcpSrvIfTable_Object = MibTable
tmnxNatPcpSrvIfTable = _TmnxNatPcpSrvIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3)
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfTable.setStatus("current")
_TmnxNatPcpSrvIfEntry_Object = MibTableRow
tmnxNatPcpSrvIfEntry = _TmnxNatPcpSrvIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3, 1)
)
tmnxNatPcpSrvIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfEntry.setStatus("current")
_TmnxNatPcpSrvIfRowStatus_Type = RowStatus
_TmnxNatPcpSrvIfRowStatus_Object = MibTableColumn
tmnxNatPcpSrvIfRowStatus = _TmnxNatPcpSrvIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3, 1, 1),
    _TmnxNatPcpSrvIfRowStatus_Type()
)
tmnxNatPcpSrvIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfRowStatus.setStatus("current")
_TmnxNatPcpSrvIfLastCh_Type = TimeStamp
_TmnxNatPcpSrvIfLastCh_Object = MibTableColumn
tmnxNatPcpSrvIfLastCh = _TmnxNatPcpSrvIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3, 1, 2),
    _TmnxNatPcpSrvIfLastCh_Type()
)
tmnxNatPcpSrvIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfLastCh.setStatus("current")
_TmnxNatPcpSrvIfStatsTable_Object = MibTable
tmnxNatPcpSrvIfStatsTable = _TmnxNatPcpSrvIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4)
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsTable.setStatus("current")
_TmnxNatPcpSrvIfStatsEntry_Object = MibTableRow
tmnxNatPcpSrvIfStatsEntry = _TmnxNatPcpSrvIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1)
)
tmnxNatPcpSrvIfStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsEntry.setStatus("current")


class _TmnxNatPcpSrvIfStatsType_Type(Unsigned32):
    """Custom type tmnxNatPcpSrvIfStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 53),
    )


_TmnxNatPcpSrvIfStatsType_Type.__name__ = "Unsigned32"
_TmnxNatPcpSrvIfStatsType_Object = MibTableColumn
tmnxNatPcpSrvIfStatsType = _TmnxNatPcpSrvIfStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 1),
    _TmnxNatPcpSrvIfStatsType_Type()
)
tmnxNatPcpSrvIfStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsType.setStatus("current")


class _TmnxNatPcpSrvIfStatsName_Type(DisplayString):
    """Custom type tmnxNatPcpSrvIfStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 58),
    )


_TmnxNatPcpSrvIfStatsName_Type.__name__ = "DisplayString"
_TmnxNatPcpSrvIfStatsName_Object = MibTableColumn
tmnxNatPcpSrvIfStatsName = _TmnxNatPcpSrvIfStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 2),
    _TmnxNatPcpSrvIfStatsName_Type()
)
tmnxNatPcpSrvIfStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsName.setStatus("current")
_TmnxNatPcpSrvIfStatsValLw_Type = Counter32
_TmnxNatPcpSrvIfStatsValLw_Object = MibTableColumn
tmnxNatPcpSrvIfStatsValLw = _TmnxNatPcpSrvIfStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 3),
    _TmnxNatPcpSrvIfStatsValLw_Type()
)
tmnxNatPcpSrvIfStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsValLw.setStatus("current")
_TmnxNatPcpSrvIfStatsValHw_Type = Counter32
_TmnxNatPcpSrvIfStatsValHw_Object = MibTableColumn
tmnxNatPcpSrvIfStatsValHw = _TmnxNatPcpSrvIfStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 4),
    _TmnxNatPcpSrvIfStatsValHw_Type()
)
tmnxNatPcpSrvIfStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsValHw.setStatus("current")
_TmnxNatPcpSrvIfStatsVal_Type = Counter64
_TmnxNatPcpSrvIfStatsVal_Object = MibTableColumn
tmnxNatPcpSrvIfStatsVal = _TmnxNatPcpSrvIfStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 5),
    _TmnxNatPcpSrvIfStatsVal_Type()
)
tmnxNatPcpSrvIfStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsVal.setStatus("current")
_TmnxNatSubscIdObjs_ObjectIdentity = ObjectIdentity
tmnxNatSubscIdObjs = _TmnxNatSubscIdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11)
)
_TmnxNatSubscIdVendorTable_Object = MibTable
tmnxNatSubscIdVendorTable = _TmnxNatSubscIdVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorTable.setStatus("current")
_TmnxNatSubscIdVendorEntry_Object = MibTableRow
tmnxNatSubscIdVendorEntry = _TmnxNatSubscIdVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1)
)
tmnxNatSubscIdVendorEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorId"),
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorEntry.setStatus("current")
_TmnxNatSubscIdVendorId_Type = TmnxSubRadiusVendorId
_TmnxNatSubscIdVendorId_Object = MibTableColumn
tmnxNatSubscIdVendorId = _TmnxNatSubscIdVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1, 1),
    _TmnxNatSubscIdVendorId_Type()
)
tmnxNatSubscIdVendorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorId.setStatus("current")


class _TmnxNatSubscIdVendorStr_Type(DisplayString):
    """Custom type tmnxNatSubscIdVendorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatSubscIdVendorStr_Type.__name__ = "DisplayString"
_TmnxNatSubscIdVendorStr_Object = MibTableColumn
tmnxNatSubscIdVendorStr = _TmnxNatSubscIdVendorStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1, 2),
    _TmnxNatSubscIdVendorStr_Type()
)
tmnxNatSubscIdVendorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorStr.setStatus("current")
_TmnxNatSubscIdVendorDescription_Type = TItemDescription
_TmnxNatSubscIdVendorDescription_Object = MibTableColumn
tmnxNatSubscIdVendorDescription = _TmnxNatSubscIdVendorDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1, 3),
    _TmnxNatSubscIdVendorDescription_Type()
)
tmnxNatSubscIdVendorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorDescription.setStatus("current")
_TmnxNatSubscIdAttrTable_Object = MibTable
tmnxNatSubscIdAttrTable = _TmnxNatSubscIdAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2)
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrTable.setStatus("current")
_TmnxNatSubscIdAttrEntry_Object = MibTableRow
tmnxNatSubscIdAttrEntry = _TmnxNatSubscIdAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1)
)
tmnxNatSubscIdAttrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrType"),
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrEntry.setStatus("current")
_TmnxNatSubscIdAttrType_Type = TmnxSubRadiusAttrType
_TmnxNatSubscIdAttrType_Object = MibTableColumn
tmnxNatSubscIdAttrType = _TmnxNatSubscIdAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1, 1),
    _TmnxNatSubscIdAttrType_Type()
)
tmnxNatSubscIdAttrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrType.setStatus("current")


class _TmnxNatSubscIdAttrStr_Type(DisplayString):
    """Custom type tmnxNatSubscIdAttrStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatSubscIdAttrStr_Type.__name__ = "DisplayString"
_TmnxNatSubscIdAttrStr_Object = MibTableColumn
tmnxNatSubscIdAttrStr = _TmnxNatSubscIdAttrStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1, 2),
    _TmnxNatSubscIdAttrStr_Type()
)
tmnxNatSubscIdAttrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrStr.setStatus("current")
_TmnxNatSubscIdAttrDescription_Type = TItemDescription
_TmnxNatSubscIdAttrDescription_Object = MibTableColumn
tmnxNatSubscIdAttrDescription = _TmnxNatSubscIdAttrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1, 3),
    _TmnxNatSubscIdAttrDescription_Type()
)
tmnxNatSubscIdAttrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrDescription.setStatus("current")
_TmnxNatDetScriptObjs_ObjectIdentity = ObjectIdentity
tmnxNatDetScriptObjs = _TmnxNatDetScriptObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12)
)


class _TmnxNatDetScriptLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxNatDetScriptLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxNatDetScriptLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxNatDetScriptLocation_Object = MibScalar
tmnxNatDetScriptLocation = _TmnxNatDetScriptLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 1),
    _TmnxNatDetScriptLocation_Type()
)
tmnxNatDetScriptLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatDetScriptLocation.setStatus("current")
_TmnxNatDetScriptSaveNeeded_Type = TruthValue
_TmnxNatDetScriptSaveNeeded_Object = MibScalar
tmnxNatDetScriptSaveNeeded = _TmnxNatDetScriptSaveNeeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 2),
    _TmnxNatDetScriptSaveNeeded_Type()
)
tmnxNatDetScriptSaveNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSaveNeeded.setStatus("current")


class _TmnxNatDetScriptSave_Type(TmnxActionType):
    """Custom type tmnxNatDetScriptSave based on TmnxActionType"""
    defaultValue = 2


_TmnxNatDetScriptSave_Type.__name__ = "TmnxActionType"
_TmnxNatDetScriptSave_Object = MibScalar
tmnxNatDetScriptSave = _TmnxNatDetScriptSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 3),
    _TmnxNatDetScriptSave_Type()
)
tmnxNatDetScriptSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSave.setStatus("current")


class _TmnxNatDetScriptSaveResult_Type(Integer32):
    """Custom type tmnxNatDetScriptSaveResult based on Integer32"""
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
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_TmnxNatDetScriptSaveResult_Type.__name__ = "Integer32"
_TmnxNatDetScriptSaveResult_Object = MibScalar
tmnxNatDetScriptSaveResult = _TmnxNatDetScriptSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 4),
    _TmnxNatDetScriptSaveResult_Type()
)
tmnxNatDetScriptSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSaveResult.setStatus("current")


class _TmnxNatDetScriptSaveTime_Type(DateAndTime):
    """Custom type tmnxNatDetScriptSaveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatDetScriptSaveTime_Type.__name__ = "DateAndTime"
_TmnxNatDetScriptSaveTime_Object = MibScalar
tmnxNatDetScriptSaveTime = _TmnxNatDetScriptSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 5),
    _TmnxNatDetScriptSaveTime_Type()
)
tmnxNatDetScriptSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSaveTime.setStatus("current")
_TmnxNatQryObjs_ObjectIdentity = ObjectIdentity
tmnxNatQryObjs = _TmnxNatQryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13)
)
_TmnxNatQryLsnSubObjs_ObjectIdentity = ObjectIdentity
tmnxNatQryLsnSubObjs = _TmnxNatQryLsnSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1)
)
_TmnxNatQryLsnSubNextQryId_Type = Unsigned32
_TmnxNatQryLsnSubNextQryId_Object = MibScalar
tmnxNatQryLsnSubNextQryId = _TmnxNatQryLsnSubNextQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 1),
    _TmnxNatQryLsnSubNextQryId_Type()
)
tmnxNatQryLsnSubNextQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubNextQryId.setStatus("current")
_TmnxNatQryLsnSubTable_Object = MibTable
tmnxNatQryLsnSubTable = _TmnxNatQryLsnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubTable.setStatus("current")
_TmnxNatQryLsnSubEntry_Object = MibTableRow
tmnxNatQryLsnSubEntry = _TmnxNatQryLsnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1)
)
tmnxNatQryLsnSubEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubQryId"),
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubEntry.setStatus("current")
_TmnxNatQryLsnSubQryId_Type = Unsigned32
_TmnxNatQryLsnSubQryId_Object = MibTableColumn
tmnxNatQryLsnSubQryId = _TmnxNatQryLsnSubQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 1),
    _TmnxNatQryLsnSubQryId_Type()
)
tmnxNatQryLsnSubQryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubQryId.setStatus("current")
_TmnxNatQryLsnSubRowStatus_Type = RowStatus
_TmnxNatQryLsnSubRowStatus_Object = MibTableColumn
tmnxNatQryLsnSubRowStatus = _TmnxNatQryLsnSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 2),
    _TmnxNatQryLsnSubRowStatus_Type()
)
tmnxNatQryLsnSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubRowStatus.setStatus("current")


class _TmnxNatQryLsnSubResultType_Type(Integer32):
    """Custom type tmnxNatQryLsnSubResultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detail", 1),
          ("common", 2))
    )


_TmnxNatQryLsnSubResultType_Type.__name__ = "Integer32"
_TmnxNatQryLsnSubResultType_Object = MibTableColumn
tmnxNatQryLsnSubResultType = _TmnxNatQryLsnSubResultType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 3),
    _TmnxNatQryLsnSubResultType_Type()
)
tmnxNatQryLsnSubResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResultType.setStatus("current")


class _TmnxNatQryLsnSubWhereNatPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatQryLsnSubWhereNatPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatQryLsnSubWhereNatPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatQryLsnSubWhereNatPolicy_Object = MibTableColumn
tmnxNatQryLsnSubWhereNatPolicy = _TmnxNatQryLsnSubWhereNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 4),
    _TmnxNatQryLsnSubWhereNatPolicy_Type()
)
tmnxNatQryLsnSubWhereNatPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereNatPolicy.setStatus("current")


class _TmnxNatQryLsnSubWhereIsaGrp_Type(TmnxNatIsaGrpIdOrZero):
    """Custom type tmnxNatQryLsnSubWhereIsaGrp based on TmnxNatIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereIsaGrp_Type.__name__ = "TmnxNatIsaGrpIdOrZero"
_TmnxNatQryLsnSubWhereIsaGrp_Object = MibTableColumn
tmnxNatQryLsnSubWhereIsaGrp = _TmnxNatQryLsnSubWhereIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 5),
    _TmnxNatQryLsnSubWhereIsaGrp_Type()
)
tmnxNatQryLsnSubWhereIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereIsaGrp.setStatus("current")


class _TmnxNatQryLsnSubWhereMemberId_Type(Unsigned32):
    """Custom type tmnxNatQryLsnSubWhereMemberId based on Unsigned32"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereMemberId_Type.__name__ = "Unsigned32"
_TmnxNatQryLsnSubWhereMemberId_Object = MibTableColumn
tmnxNatQryLsnSubWhereMemberId = _TmnxNatQryLsnSubWhereMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 6),
    _TmnxNatQryLsnSubWhereMemberId_Type()
)
tmnxNatQryLsnSubWhereMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereMemberId.setStatus("current")


class _TmnxNatQryLsnSubWhereOutRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatQryLsnSubWhereOutRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereOutRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatQryLsnSubWhereOutRouter_Object = MibTableColumn
tmnxNatQryLsnSubWhereOutRouter = _TmnxNatQryLsnSubWhereOutRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 7),
    _TmnxNatQryLsnSubWhereOutRouter_Type()
)
tmnxNatQryLsnSubWhereOutRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereOutRouter.setStatus("current")


class _TmnxNatQryLsnSubWhereOutAddrType_Type(InetAddressType):
    """Custom type tmnxNatQryLsnSubWhereOutAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereOutAddrType_Type.__name__ = "InetAddressType"
_TmnxNatQryLsnSubWhereOutAddrType_Object = MibTableColumn
tmnxNatQryLsnSubWhereOutAddrType = _TmnxNatQryLsnSubWhereOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 8),
    _TmnxNatQryLsnSubWhereOutAddrType_Type()
)
tmnxNatQryLsnSubWhereOutAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereOutAddrType.setStatus("current")


class _TmnxNatQryLsnSubWhereOutAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubWhereOutAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubWhereOutAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubWhereOutAddr_Object = MibTableColumn
tmnxNatQryLsnSubWhereOutAddr = _TmnxNatQryLsnSubWhereOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 9),
    _TmnxNatQryLsnSubWhereOutAddr_Type()
)
tmnxNatQryLsnSubWhereOutAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereOutAddr.setStatus("current")


class _TmnxNatQryLsnSubWhereInSubType_Type(Integer32):
    """Custom type tmnxNatQryLsnSubWhereInSubType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TmnxNatQryLsnSubWhereInSubType_Type.__name__ = "Integer32"
_TmnxNatQryLsnSubWhereInSubType_Object = MibTableColumn
tmnxNatQryLsnSubWhereInSubType = _TmnxNatQryLsnSubWhereInSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 10),
    _TmnxNatQryLsnSubWhereInSubType_Type()
)
tmnxNatQryLsnSubWhereInSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInSubType.setStatus("current")


class _TmnxNatQryLsnSubWhereInRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatQryLsnSubWhereInRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereInRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatQryLsnSubWhereInRouter_Object = MibTableColumn
tmnxNatQryLsnSubWhereInRouter = _TmnxNatQryLsnSubWhereInRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 11),
    _TmnxNatQryLsnSubWhereInRouter_Type()
)
tmnxNatQryLsnSubWhereInRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInRouter.setStatus("current")


class _TmnxNatQryLsnSubWhereInAddrType_Type(InetAddressType):
    """Custom type tmnxNatQryLsnSubWhereInAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereInAddrType_Type.__name__ = "InetAddressType"
_TmnxNatQryLsnSubWhereInAddrType_Object = MibTableColumn
tmnxNatQryLsnSubWhereInAddrType = _TmnxNatQryLsnSubWhereInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 12),
    _TmnxNatQryLsnSubWhereInAddrType_Type()
)
tmnxNatQryLsnSubWhereInAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInAddrType.setStatus("current")


class _TmnxNatQryLsnSubWhereInAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubWhereInAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubWhereInAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubWhereInAddr_Object = MibTableColumn
tmnxNatQryLsnSubWhereInAddr = _TmnxNatQryLsnSubWhereInAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 13),
    _TmnxNatQryLsnSubWhereInAddr_Type()
)
tmnxNatQryLsnSubWhereInAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInAddr.setStatus("current")


class _TmnxNatQryLsnSubWhereInAddrPfxL_Type(InetAddressPrefixLength):
    """Custom type tmnxNatQryLsnSubWhereInAddrPfxL based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatQryLsnSubWhereInAddrPfxL_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatQryLsnSubWhereInAddrPfxL_Object = MibTableColumn
tmnxNatQryLsnSubWhereInAddrPfxL = _TmnxNatQryLsnSubWhereInAddrPfxL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 14),
    _TmnxNatQryLsnSubWhereInAddrPfxL_Type()
)
tmnxNatQryLsnSubWhereInAddrPfxL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInAddrPfxL.setStatus("current")


class _TmnxNatQryLsnSubWhereSubId_Type(Unsigned32):
    """Custom type tmnxNatQryLsnSubWhereSubId based on Unsigned32"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereSubId_Type.__name__ = "Unsigned32"
_TmnxNatQryLsnSubWhereSubId_Object = MibTableColumn
tmnxNatQryLsnSubWhereSubId = _TmnxNatQryLsnSubWhereSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 15),
    _TmnxNatQryLsnSubWhereSubId_Type()
)
tmnxNatQryLsnSubWhereSubId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereSubId.setStatus("current")
_TmnxNatQryLsnSubResTable_Object = MibTable
tmnxNatQryLsnSubResTable = _TmnxNatQryLsnSubResTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResTable.setStatus("current")
_TmnxNatQryLsnSubResEntry_Object = MibTableRow
tmnxNatQryLsnSubResEntry = _TmnxNatQryLsnSubResEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1)
)
tmnxNatQryLsnSubResEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubQryId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResEntry.setStatus("current")
_TmnxNatQryLsnSubResId_Type = Unsigned32
_TmnxNatQryLsnSubResId_Object = MibTableColumn
tmnxNatQryLsnSubResId = _TmnxNatQryLsnSubResId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 1),
    _TmnxNatQryLsnSubResId_Type()
)
tmnxNatQryLsnSubResId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResId.setStatus("current")
_TmnxNatQryLsnSubResPolicy_Type = TNamedItem
_TmnxNatQryLsnSubResPolicy_Object = MibTableColumn
tmnxNatQryLsnSubResPolicy = _TmnxNatQryLsnSubResPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 2),
    _TmnxNatQryLsnSubResPolicy_Type()
)
tmnxNatQryLsnSubResPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResPolicy.setStatus("current")
_TmnxNatQryLsnSubResIsaGrp_Type = TmnxNatIsaGrpIdOrZero
_TmnxNatQryLsnSubResIsaGrp_Object = MibTableColumn
tmnxNatQryLsnSubResIsaGrp = _TmnxNatQryLsnSubResIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 3),
    _TmnxNatQryLsnSubResIsaGrp_Type()
)
tmnxNatQryLsnSubResIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIsaGrp.setStatus("current")
_TmnxNatQryLsnSubResIsaMemberId_Type = Unsigned32
_TmnxNatQryLsnSubResIsaMemberId_Object = MibTableColumn
tmnxNatQryLsnSubResIsaMemberId = _TmnxNatQryLsnSubResIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 4),
    _TmnxNatQryLsnSubResIsaMemberId_Type()
)
tmnxNatQryLsnSubResIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIsaMemberId.setStatus("current")
_TmnxNatQryLsnSubResOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatQryLsnSubResOutVRtrID_Object = MibTableColumn
tmnxNatQryLsnSubResOutVRtrID = _TmnxNatQryLsnSubResOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 5),
    _TmnxNatQryLsnSubResOutVRtrID_Type()
)
tmnxNatQryLsnSubResOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResOutVRtrID.setStatus("current")
_TmnxNatQryLsnSubResOutAddrType_Type = InetAddressType
_TmnxNatQryLsnSubResOutAddrType_Object = MibTableColumn
tmnxNatQryLsnSubResOutAddrType = _TmnxNatQryLsnSubResOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 6),
    _TmnxNatQryLsnSubResOutAddrType_Type()
)
tmnxNatQryLsnSubResOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResOutAddrType.setStatus("current")


class _TmnxNatQryLsnSubResOutAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubResOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubResOutAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubResOutAddr_Object = MibTableColumn
tmnxNatQryLsnSubResOutAddr = _TmnxNatQryLsnSubResOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 7),
    _TmnxNatQryLsnSubResOutAddr_Type()
)
tmnxNatQryLsnSubResOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResOutAddr.setStatus("current")
_TmnxNatQryLsnSubResIdStr_Type = TmnxNatSubscriberIdString
_TmnxNatQryLsnSubResIdStr_Object = MibTableColumn
tmnxNatQryLsnSubResIdStr = _TmnxNatQryLsnSubResIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 8),
    _TmnxNatQryLsnSubResIdStr_Type()
)
tmnxNatQryLsnSubResIdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIdStr.setStatus("current")


class _TmnxNatQryLsnSubResInSubType_Type(Integer32):
    """Custom type tmnxNatQryLsnSubResInSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TmnxNatQryLsnSubResInSubType_Type.__name__ = "Integer32"
_TmnxNatQryLsnSubResInSubType_Object = MibTableColumn
tmnxNatQryLsnSubResInSubType = _TmnxNatQryLsnSubResInSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 9),
    _TmnxNatQryLsnSubResInSubType_Type()
)
tmnxNatQryLsnSubResInSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInSubType.setStatus("current")
_TmnxNatQryLsnSubResInRouter_Type = TmnxVRtrIDOrZero
_TmnxNatQryLsnSubResInRouter_Object = MibTableColumn
tmnxNatQryLsnSubResInRouter = _TmnxNatQryLsnSubResInRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 10),
    _TmnxNatQryLsnSubResInRouter_Type()
)
tmnxNatQryLsnSubResInRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInRouter.setStatus("current")
_TmnxNatQryLsnSubResInAddrType_Type = InetAddressType
_TmnxNatQryLsnSubResInAddrType_Object = MibTableColumn
tmnxNatQryLsnSubResInAddrType = _TmnxNatQryLsnSubResInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 11),
    _TmnxNatQryLsnSubResInAddrType_Type()
)
tmnxNatQryLsnSubResInAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInAddrType.setStatus("current")


class _TmnxNatQryLsnSubResInAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubResInAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubResInAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubResInAddr_Object = MibTableColumn
tmnxNatQryLsnSubResInAddr = _TmnxNatQryLsnSubResInAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 12),
    _TmnxNatQryLsnSubResInAddr_Type()
)
tmnxNatQryLsnSubResInAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInAddr.setStatus("current")
_TmnxNatQryLsnSubResInAddrPfxL_Type = InetAddressPrefixLength
_TmnxNatQryLsnSubResInAddrPfxL_Object = MibTableColumn
tmnxNatQryLsnSubResInAddrPfxL = _TmnxNatQryLsnSubResInAddrPfxL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 13),
    _TmnxNatQryLsnSubResInAddrPfxL_Type()
)
tmnxNatQryLsnSubResInAddrPfxL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInAddrPfxL.setStatus("current")
_TmnxNatQryLsnSubResIcmpPortUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResIcmpPortUsg_Object = MibTableColumn
tmnxNatQryLsnSubResIcmpPortUsg = _TmnxNatQryLsnSubResIcmpPortUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 100),
    _TmnxNatQryLsnSubResIcmpPortUsg_Type()
)
tmnxNatQryLsnSubResIcmpPortUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIcmpPortUsg.setStatus("current")
_TmnxNatQryLsnSubResIcmpPortUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResIcmpPortUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResIcmpPortUsgHi = _TmnxNatQryLsnSubResIcmpPortUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 101),
    _TmnxNatQryLsnSubResIcmpPortUsgHi_Type()
)
tmnxNatQryLsnSubResIcmpPortUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIcmpPortUsgHi.setStatus("current")
_TmnxNatQryLsnSubResUdpPortUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResUdpPortUsg_Object = MibTableColumn
tmnxNatQryLsnSubResUdpPortUsg = _TmnxNatQryLsnSubResUdpPortUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 102),
    _TmnxNatQryLsnSubResUdpPortUsg_Type()
)
tmnxNatQryLsnSubResUdpPortUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResUdpPortUsg.setStatus("current")
_TmnxNatQryLsnSubResUdpPortUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResUdpPortUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResUdpPortUsgHi = _TmnxNatQryLsnSubResUdpPortUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 103),
    _TmnxNatQryLsnSubResUdpPortUsgHi_Type()
)
tmnxNatQryLsnSubResUdpPortUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResUdpPortUsgHi.setStatus("current")
_TmnxNatQryLsnSubResTcpPortUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResTcpPortUsg_Object = MibTableColumn
tmnxNatQryLsnSubResTcpPortUsg = _TmnxNatQryLsnSubResTcpPortUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 104),
    _TmnxNatQryLsnSubResTcpPortUsg_Type()
)
tmnxNatQryLsnSubResTcpPortUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResTcpPortUsg.setStatus("current")
_TmnxNatQryLsnSubResTcpPortUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResTcpPortUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResTcpPortUsgHi = _TmnxNatQryLsnSubResTcpPortUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 105),
    _TmnxNatQryLsnSubResTcpPortUsgHi_Type()
)
tmnxNatQryLsnSubResTcpPortUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResTcpPortUsgHi.setStatus("current")
_TmnxNatQryLsnSubResSessionUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResSessionUsg_Object = MibTableColumn
tmnxNatQryLsnSubResSessionUsg = _TmnxNatQryLsnSubResSessionUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 106),
    _TmnxNatQryLsnSubResSessionUsg_Type()
)
tmnxNatQryLsnSubResSessionUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionUsg.setStatus("current")
_TmnxNatQryLsnSubResSessionUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResSessionUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResSessionUsgHi = _TmnxNatQryLsnSubResSessionUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 107),
    _TmnxNatQryLsnSubResSessionUsgHi_Type()
)
tmnxNatQryLsnSubResSessionUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionUsgHi.setStatus("current")
_TmnxNatQryLsnSubResSessions_Type = Gauge32
_TmnxNatQryLsnSubResSessions_Object = MibTableColumn
tmnxNatQryLsnSubResSessions = _TmnxNatQryLsnSubResSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 108),
    _TmnxNatQryLsnSubResSessions_Type()
)
tmnxNatQryLsnSubResSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessions.setStatus("current")
_TmnxNatQryLsnSubResSessionsPrio_Type = Gauge32
_TmnxNatQryLsnSubResSessionsPrio_Object = MibTableColumn
tmnxNatQryLsnSubResSessionsPrio = _TmnxNatQryLsnSubResSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 109),
    _TmnxNatQryLsnSubResSessionsPrio_Type()
)
tmnxNatQryLsnSubResSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionsPrio.setStatus("current")
_TmnxNatQryLsnSubResSessionsPeak_Type = Gauge32
_TmnxNatQryLsnSubResSessionsPeak_Object = MibTableColumn
tmnxNatQryLsnSubResSessionsPeak = _TmnxNatQryLsnSubResSessionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 110),
    _TmnxNatQryLsnSubResSessionsPeak_Type()
)
tmnxNatQryLsnSubResSessionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionsPeak.setStatus("current")
_TmnxNatIsaGrpTableLastCh_Type = TimeStamp
_TmnxNatIsaGrpTableLastCh_Object = MibScalar
tmnxNatIsaGrpTableLastCh = _TmnxNatIsaGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 100),
    _TmnxNatIsaGrpTableLastCh_Type()
)
tmnxNatIsaGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpTableLastCh.setStatus("current")
_TmnxNatIsaMdaTableLastCh_Type = TimeStamp
_TmnxNatIsaMdaTableLastCh_Object = MibScalar
tmnxNatIsaMdaTableLastCh = _TmnxNatIsaMdaTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 101),
    _TmnxNatIsaMdaTableLastCh_Type()
)
tmnxNatIsaMdaTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaTableLastCh.setStatus("current")
_TmnxNatIsaMdaStatTableLastCh_Type = TimeStamp
_TmnxNatIsaMdaStatTableLastCh_Object = MibScalar
tmnxNatIsaMdaStatTableLastCh = _TmnxNatIsaMdaStatTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 102),
    _TmnxNatIsaMdaStatTableLastCh_Type()
)
tmnxNatIsaMdaStatTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatTableLastCh.setStatus("current")
_TmnxNatPlcyTableLastCh_Type = TimeStamp
_TmnxNatPlcyTableLastCh_Object = MibScalar
tmnxNatPlcyTableLastCh = _TmnxNatPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 103),
    _TmnxNatPlcyTableLastCh_Type()
)
tmnxNatPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyTableLastCh.setStatus("current")
_TmnxNatVrtrTableLastCh_Type = TimeStamp
_TmnxNatVrtrTableLastCh_Object = MibScalar
tmnxNatVrtrTableLastCh = _TmnxNatVrtrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 104),
    _TmnxNatVrtrTableLastCh_Type()
)
tmnxNatVrtrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrTableLastCh.setStatus("current")
_TmnxNatL2AwAddrTableLastCh_Type = TimeStamp
_TmnxNatL2AwAddrTableLastCh_Object = MibScalar
tmnxNatL2AwAddrTableLastCh = _TmnxNatL2AwAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 105),
    _TmnxNatL2AwAddrTableLastCh_Type()
)
tmnxNatL2AwAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrTableLastCh.setStatus("current")
_TmnxNatPlTableLastCh_Type = TimeStamp
_TmnxNatPlTableLastCh_Object = MibScalar
tmnxNatPlTableLastCh = _TmnxNatPlTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 106),
    _TmnxNatPlTableLastCh_Type()
)
tmnxNatPlTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlTableLastCh.setStatus("current")
_TmnxNatPlRangeTableLastCh_Type = TimeStamp
_TmnxNatPlRangeTableLastCh_Object = MibScalar
tmnxNatPlRangeTableLastCh = _TmnxNatPlRangeTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 107),
    _TmnxNatPlRangeTableLastCh_Type()
)
tmnxNatPlRangeTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeTableLastCh.setStatus("current")
_TmnxNatDestTableLastCh_Type = TimeStamp
_TmnxNatDestTableLastCh_Object = MibScalar
tmnxNatDestTableLastCh = _TmnxNatDestTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 108),
    _TmnxNatDestTableLastCh_Type()
)
tmnxNatDestTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDestTableLastCh.setStatus("current")
_TmnxNatMapLsnHostTableLastCh_Type = TimeStamp
_TmnxNatMapLsnHostTableLastCh_Object = MibScalar
tmnxNatMapLsnHostTableLastCh = _TmnxNatMapLsnHostTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 109),
    _TmnxNatMapLsnHostTableLastCh_Type()
)
tmnxNatMapLsnHostTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostTableLastCh.setStatus("obsolete")
_TmnxNatMapTableLastCh_Type = TimeStamp
_TmnxNatMapTableLastCh_Object = MibScalar
tmnxNatMapTableLastCh = _TmnxNatMapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 110),
    _TmnxNatMapTableLastCh_Type()
)
tmnxNatMapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapTableLastCh.setStatus("obsolete")
_TmnxNatDsliteAddrTableLastCh_Type = TimeStamp
_TmnxNatDsliteAddrTableLastCh_Object = MibScalar
tmnxNatDsliteAddrTableLastCh = _TmnxNatDsliteAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 111),
    _TmnxNatDsliteAddrTableLastCh_Type()
)
tmnxNatDsliteAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrTableLastCh.setStatus("current")
_TmnxNatApTableLastCh_Type = TimeStamp
_TmnxNatApTableLastCh_Object = MibScalar
tmnxNatApTableLastCh = _TmnxNatApTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 112),
    _TmnxNatApTableLastCh_Type()
)
tmnxNatApTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApTableLastCh.setStatus("obsolete")
_TmnxNatApServTableLastCh_Type = TimeStamp
_TmnxNatApServTableLastCh_Object = MibScalar
tmnxNatApServTableLastCh = _TmnxNatApServTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 113),
    _TmnxNatApServTableLastCh_Type()
)
tmnxNatApServTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServTableLastCh.setStatus("obsolete")
_TmnxNat64TableLastCh_Type = TimeStamp
_TmnxNat64TableLastCh_Object = MibScalar
tmnxNat64TableLastCh = _TmnxNat64TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 115),
    _TmnxNat64TableLastCh_Type()
)
tmnxNat64TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNat64TableLastCh.setStatus("current")
_TmnxNatGrpCfgTableLastCh_Type = TimeStamp
_TmnxNatGrpCfgTableLastCh_Object = MibScalar
tmnxNatGrpCfgTableLastCh = _TmnxNatGrpCfgTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 116),
    _TmnxNatGrpCfgTableLastCh_Type()
)
tmnxNatGrpCfgTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgTableLastCh.setStatus("current")
_TmnxNatSubIdTableLastCh_Type = TimeStamp
_TmnxNatSubIdTableLastCh_Object = MibScalar
tmnxNatSubIdTableLastCh = _TmnxNatSubIdTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 117),
    _TmnxNatSubIdTableLastCh_Type()
)
tmnxNatSubIdTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubIdTableLastCh.setStatus("current")
_TmnxNatPcpPlcyTableLastCh_Type = TimeStamp
_TmnxNatPcpPlcyTableLastCh_Object = MibScalar
tmnxNatPcpPlcyTableLastCh = _TmnxNatPcpPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 118),
    _TmnxNatPcpPlcyTableLastCh_Type()
)
tmnxNatPcpPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyTableLastCh.setStatus("current")
_TmnxNatPcpSrvTableLastCh_Type = TimeStamp
_TmnxNatPcpSrvTableLastCh_Object = MibScalar
tmnxNatPcpSrvTableLastCh = _TmnxNatPcpSrvTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 119),
    _TmnxNatPcpSrvTableLastCh_Type()
)
tmnxNatPcpSrvTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvTableLastCh.setStatus("current")
_TmnxNatPcpSrvIfTableLastCh_Type = TimeStamp
_TmnxNatPcpSrvIfTableLastCh_Object = MibScalar
tmnxNatPcpSrvIfTableLastCh = _TmnxNatPcpSrvIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 121),
    _TmnxNatPcpSrvIfTableLastCh_Type()
)
tmnxNatPcpSrvIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfTableLastCh.setStatus("current")
_TmnxNatDetPlcyTableLastCh_Type = TimeStamp
_TmnxNatDetPlcyTableLastCh_Object = MibScalar
tmnxNatDetPlcyTableLastCh = _TmnxNatDetPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 122),
    _TmnxNatDetPlcyTableLastCh_Type()
)
tmnxNatDetPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyTableLastCh.setStatus("current")
_TmnxNatDetMapTableLastCh_Type = TimeStamp
_TmnxNatDetMapTableLastCh_Object = MibScalar
tmnxNatDetMapTableLastCh = _TmnxNatDetMapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 123),
    _TmnxNatDetMapTableLastCh_Type()
)
tmnxNatDetMapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMapTableLastCh.setStatus("current")
_TmnxNatResourceProblem_Type = TruthValue
_TmnxNatResourceProblem_Object = MibScalar
tmnxNatResourceProblem = _TmnxNatResourceProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 200),
    _TmnxNatResourceProblem_Type()
)
tmnxNatResourceProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatResourceProblem.setStatus("current")
_TmnxNatLsnSubscIdCount_Type = Gauge32
_TmnxNatLsnSubscIdCount_Object = MibScalar
tmnxNatLsnSubscIdCount = _TmnxNatLsnSubscIdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 201),
    _TmnxNatLsnSubscIdCount_Type()
)
tmnxNatLsnSubscIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdCount.setStatus("current")
_TmnxNatQryLsnSubMaxQryId_Type = Unsigned32
_TmnxNatQryLsnSubMaxQryId_Object = MibScalar
tmnxNatQryLsnSubMaxQryId = _TmnxNatQryLsnSubMaxQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 202),
    _TmnxNatQryLsnSubMaxQryId_Type()
)
tmnxNatQryLsnSubMaxQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubMaxQryId.setStatus("current")
_TmnxNatNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxNatNotificationObjs = _TmnxNatNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2)
)


class _TmnxNatNotifyDescription_Type(DisplayString):
    """Custom type tmnxNatNotifyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxNatNotifyDescription_Type.__name__ = "DisplayString"
_TmnxNatNotifyDescription_Object = MibScalar
tmnxNatNotifyDescription = _TmnxNatNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 1),
    _TmnxNatNotifyDescription_Type()
)
tmnxNatNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyDescription.setStatus("current")
_TmnxNatNotifyOutsideVRtrID_Type = TmnxVRtrID
_TmnxNatNotifyOutsideVRtrID_Object = MibScalar
tmnxNatNotifyOutsideVRtrID = _TmnxNatNotifyOutsideVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 2),
    _TmnxNatNotifyOutsideVRtrID_Type()
)
tmnxNatNotifyOutsideVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideVRtrID.setStatus("current")
_TmnxNatNotifyInsideVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatNotifyInsideVRtrID_Object = MibScalar
tmnxNatNotifyInsideVRtrID = _TmnxNatNotifyInsideVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 3),
    _TmnxNatNotifyInsideVRtrID_Type()
)
tmnxNatNotifyInsideVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideVRtrID.setStatus("current")
_TmnxNatNotifyOutsideAddrType_Type = InetAddressType
_TmnxNatNotifyOutsideAddrType_Object = MibScalar
tmnxNatNotifyOutsideAddrType = _TmnxNatNotifyOutsideAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 4),
    _TmnxNatNotifyOutsideAddrType_Type()
)
tmnxNatNotifyOutsideAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideAddrType.setStatus("current")


class _TmnxNatNotifyOutsideAddr_Type(InetAddress):
    """Custom type tmnxNatNotifyOutsideAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatNotifyOutsideAddr_Type.__name__ = "InetAddress"
_TmnxNatNotifyOutsideAddr_Object = MibScalar
tmnxNatNotifyOutsideAddr = _TmnxNatNotifyOutsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 5),
    _TmnxNatNotifyOutsideAddr_Type()
)
tmnxNatNotifyOutsideAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideAddr.setStatus("current")
_TmnxNatNotifyInsideAddrType_Type = InetAddressType
_TmnxNatNotifyInsideAddrType_Object = MibScalar
tmnxNatNotifyInsideAddrType = _TmnxNatNotifyInsideAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 6),
    _TmnxNatNotifyInsideAddrType_Type()
)
tmnxNatNotifyInsideAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideAddrType.setStatus("current")


class _TmnxNatNotifyInsideAddr_Type(InetAddress):
    """Custom type tmnxNatNotifyInsideAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatNotifyInsideAddr_Type.__name__ = "InetAddress"
_TmnxNatNotifyInsideAddr_Object = MibScalar
tmnxNatNotifyInsideAddr = _TmnxNatNotifyInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 7),
    _TmnxNatNotifyInsideAddr_Type()
)
tmnxNatNotifyInsideAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideAddr.setStatus("current")
_TmnxNatNotifyPort_Type = InetPortNumber
_TmnxNatNotifyPort_Object = MibScalar
tmnxNatNotifyPort = _TmnxNatNotifyPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 8),
    _TmnxNatNotifyPort_Type()
)
tmnxNatNotifyPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPort.setStatus("current")
_TmnxNatNotifyPort2_Type = InetPortNumber
_TmnxNatNotifyPort2_Object = MibScalar
tmnxNatNotifyPort2 = _TmnxNatNotifyPort2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 9),
    _TmnxNatNotifyPort2_Type()
)
tmnxNatNotifyPort2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPort2.setStatus("current")


class _TmnxNatNotifyDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatNotifyDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatNotifyDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatNotifyDateAndTime_Object = MibScalar
tmnxNatNotifyDateAndTime = _TmnxNatNotifyDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 10),
    _TmnxNatNotifyDateAndTime_Type()
)
tmnxNatNotifyDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyDateAndTime.setStatus("current")
_TmnxNatNotifyTruthValue_Type = TruthValue
_TmnxNatNotifyTruthValue_Object = MibScalar
tmnxNatNotifyTruthValue = _TmnxNatNotifyTruthValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 11),
    _TmnxNatNotifyTruthValue_Type()
)
tmnxNatNotifyTruthValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyTruthValue.setStatus("current")
_TmnxNatNotifyLsnSubId_Type = Unsigned32
_TmnxNatNotifyLsnSubId_Object = MibScalar
tmnxNatNotifyLsnSubId = _TmnxNatNotifyLsnSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 13),
    _TmnxNatNotifyLsnSubId_Type()
)
tmnxNatNotifyLsnSubId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyLsnSubId.setStatus("current")


class _TmnxNatNotifyL2AwSubIdent_Type(DisplayString):
    """Custom type tmnxNatNotifyL2AwSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatNotifyL2AwSubIdent_Type.__name__ = "DisplayString"
_TmnxNatNotifyL2AwSubIdent_Object = MibScalar
tmnxNatNotifyL2AwSubIdent = _TmnxNatNotifyL2AwSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 14),
    _TmnxNatNotifyL2AwSubIdent_Type()
)
tmnxNatNotifyL2AwSubIdent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyL2AwSubIdent.setStatus("current")
_TmnxNatNotifyOutsideEndAddrType_Type = InetAddressType
_TmnxNatNotifyOutsideEndAddrType_Object = MibScalar
tmnxNatNotifyOutsideEndAddrType = _TmnxNatNotifyOutsideEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 15),
    _TmnxNatNotifyOutsideEndAddrType_Type()
)
tmnxNatNotifyOutsideEndAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideEndAddrType.setStatus("current")


class _TmnxNatNotifyOutsideEndAddr_Type(InetAddress):
    """Custom type tmnxNatNotifyOutsideEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatNotifyOutsideEndAddr_Type.__name__ = "InetAddress"
_TmnxNatNotifyOutsideEndAddr_Object = MibScalar
tmnxNatNotifyOutsideEndAddr = _TmnxNatNotifyOutsideEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 16),
    _TmnxNatNotifyOutsideEndAddr_Type()
)
tmnxNatNotifyOutsideEndAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideEndAddr.setStatus("current")
_TmnxNatNotifyPlSeqNum_Type = Counter64
_TmnxNatNotifyPlSeqNum_Object = MibScalar
tmnxNatNotifyPlSeqNum = _TmnxNatNotifyPlSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 17),
    _TmnxNatNotifyPlSeqNum_Type()
)
tmnxNatNotifyPlSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPlSeqNum.setStatus("current")
_TmnxNatNotifySubscriberType_Type = TmnxNatSubscriberType
_TmnxNatNotifySubscriberType_Object = MibScalar
tmnxNatNotifySubscriberType = _TmnxNatNotifySubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 20),
    _TmnxNatNotifySubscriberType_Type()
)
tmnxNatNotifySubscriberType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifySubscriberType.setStatus("current")
_TmnxNatNotifyMdaChassisIndex_Type = TmnxChassisIndexOrZero
_TmnxNatNotifyMdaChassisIndex_Object = MibScalar
tmnxNatNotifyMdaChassisIndex = _TmnxNatNotifyMdaChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 21),
    _TmnxNatNotifyMdaChassisIndex_Type()
)
tmnxNatNotifyMdaChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMdaChassisIndex.setStatus("current")
_TmnxNatNotifyMdaCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxNatNotifyMdaCardSlotNum_Object = MibScalar
tmnxNatNotifyMdaCardSlotNum = _TmnxNatNotifyMdaCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 22),
    _TmnxNatNotifyMdaCardSlotNum_Type()
)
tmnxNatNotifyMdaCardSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMdaCardSlotNum.setStatus("current")
_TmnxNatNotifyMdaSlotNum_Type = Unsigned32
_TmnxNatNotifyMdaSlotNum_Object = MibScalar
tmnxNatNotifyMdaSlotNum = _TmnxNatNotifyMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 23),
    _TmnxNatNotifyMdaSlotNum_Type()
)
tmnxNatNotifyMdaSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMdaSlotNum.setStatus("current")
_TmnxNatNotifyCounter_Type = Counter64
_TmnxNatNotifyCounter_Object = MibScalar
tmnxNatNotifyCounter = _TmnxNatNotifyCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 24),
    _TmnxNatNotifyCounter_Type()
)
tmnxNatNotifyCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyCounter.setStatus("current")
_TmnxNatNotifyNumber_Type = Unsigned32
_TmnxNatNotifyNumber_Object = MibScalar
tmnxNatNotifyNumber = _TmnxNatNotifyNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 25),
    _TmnxNatNotifyNumber_Type()
)
tmnxNatNotifyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyNumber.setStatus("current")


class _TmnxNatNotifyInsideAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatNotifyInsideAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatNotifyInsideAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatNotifyInsideAddrPrefixLen_Object = MibScalar
tmnxNatNotifyInsideAddrPrefixLen = _TmnxNatNotifyInsideAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 26),
    _TmnxNatNotifyInsideAddrPrefixLen_Type()
)
tmnxNatNotifyInsideAddrPrefixLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideAddrPrefixLen.setStatus("current")
_TmnxNatNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxNatNotifyPrefix = _TmnxNatNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65)
)
_TmnxNatNotifications_ObjectIdentity = ObjectIdentity
tmnxNatNotifications = _TmnxNatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0)
)
tmnxNatIsaMdaEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatIsaMdaStatEntry")
)
tmnxNatIsaMdaStatEntry.setIndexNames(*tmnxNatIsaMdaEntry.getIndexNames())
tmnxNatVrtrEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatSubIdEntry")
)
tmnxNatSubIdEntry.setIndexNames(*tmnxNatVrtrEntry.getIndexNames())
tmnxNatPlRangeEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatPlRangeStatEntry")
)
tmnxNatPlRangeStatEntry.setIndexNames(*tmnxNatPlRangeEntry.getIndexNames())
tmnxNatLsnSubEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatLsnSubStatEntry")
)
tmnxNatLsnSubStatEntry.setIndexNames(*tmnxNatLsnSubEntry.getIndexNames())
tmnxNatL2AwSubEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatL2AwSubStatEntry")
)
tmnxNatL2AwSubStatEntry.setIndexNames(*tmnxNatL2AwSubEntry.getIndexNames())

# Managed Objects groups

tmnxNatIsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 1)
)
tmnxNatIsaGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpActiveMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaGroup.setStatus("obsolete")

tmnxNatIsaStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 2)
)
tmnxNatIsaStatGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberIpAddrReserved"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberBlocksReserved"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblem"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatGroup.setStatus("current")

tmnxNatPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 3)
)
tmnxNatPlcyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPoolVRtr"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyFiltering"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPrioSessionFcSet"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpEstab"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpTrans"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpSyn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpTimeWait"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUdp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUdpInitial"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUdpDns"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToIcmpQuery"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyGroup.setStatus("current")

tmnxNatPlcyStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 4)
)
tmnxNatPlcyStatGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyStatGroup.setStatus("current")

tmnxNatVrtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 5)
)
tmnxNatVrtrGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInPolicy"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrGroup.setStatus("current")

tmnxNatPlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 6)
)
tmnxNatPlGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvAllowPrivileged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeAdminDrain"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeNumAllocatedBlk"))
)
if mibBuilder.loadTexts:
    tmnxNatPlGroup.setStatus("obsolete")

tmnxNatDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 7)
)
tmnxNatDestGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDestTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatDestGroup.setStatus("current")

tmnxNatL2AwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 8)
)
tmnxNatL2AwGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsageH"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubBlkEnd"))
)
if mibBuilder.loadTexts:
    tmnxNatL2AwGroup.setStatus("current")

tmnxNatLsnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 9)
)
tmnxNatLsnGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkEnd"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnGroup.setStatus("obsolete")

tmnxNatMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 10)
)
tmnxNatMapGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapOutPort"))
)
if mibBuilder.loadTexts:
    tmnxNatMapGroup.setStatus("obsolete")

tmnxNatLsnV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 15)
)
tmnxNatLsnV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnSubscriberLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyBlkLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTunnelMtu"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnV9v0Group.setStatus("obsolete")

tmnxNatVrtrV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 16)
)
tmnxNatVrtrV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInDsliteAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInDsliteSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutMtu"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrV9v0Group.setStatus("current")

tmnxNatPlcyV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 17)
)
tmnxNatPlcyV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyToSip"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyAlgEnable"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortFwdLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyUdpInboundRefresh"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV9v0Group.setStatus("current")

tmnxNatFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 18)
)
tmnxNatFwdGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdPersistKey"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdGroup.setStatus("obsolete")

tmnxNatPlV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 19)
)
tmnxNatPlV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdRangeEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlOperMode"))
)
if mibBuilder.loadTexts:
    tmnxNatPlV9v0Group.setStatus("obsolete")

tmnxNatRedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 20)
)
tmnxNatRedGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeerAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeerAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeer6AddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeer6Addr"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedSteerRtType"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedSteerRt"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedSteerRtLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedExpPrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedExpPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedExpPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedMonPrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedMonPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedMonPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActive"))
)
if mibBuilder.loadTexts:
    tmnxNatRedGroup.setStatus("current")

tmnxNatDestNatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 21)
)
tmnxNatDestNatGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyDestNatAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyDestNatAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyDestNatPort"))
)
if mibBuilder.loadTexts:
    tmnxNatDestNatGroup.setStatus("current")

tmnxNatPlcyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 22)
)
tmnxNatPlcyV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyIpfixExpPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyTcpMssAdjust"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToSubRetention"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV10v0Group.setStatus("current")

tmnxNatIsaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 23)
)
tmnxNatIsaV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpActiveMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaV10v0Group.setStatus("obsolete")

tmnxNatAccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 24)
)
tmnxNatAccGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgAccountingPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatApTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatApIncludeAttributes"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersRetry"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersAlgorithm"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServSecret"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAcctPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatTxRequests"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatReqTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSendRetries"))
)
if mibBuilder.loadTexts:
    tmnxNatAccGroup.setStatus("obsolete")

tmnxNatWlanGwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 25)
)
tmnxNatWlanGwGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionWatermarkHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionWatermarkLo"))
)
if mibBuilder.loadTexts:
    tmnxNatWlanGwGroup.setStatus("current")

tmnxNat64Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 26)
)
tmnxNat64Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNat64TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNat64LastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNat64RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIpv6Mtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InDropZeroIpv4Checksum"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSetTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIgnoreTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InInsertIpv6FragHeader"),
        ("TIMETRA-NAT-MIB", "tmnxNat64SubId"))
)
if mibBuilder.loadTexts:
    tmnxNat64Group.setStatus("obsolete")

tmnxNatLsnSubIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 27)
)
tmnxNatLsnSubIdentGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatSubIdTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvName"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusAttributeType"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusVendorId"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDropUnidentified"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrTimeStamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdCount"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIdentGroup.setStatus("obsolete")

tmnxNatPcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 28)
)
tmnxNatPcpGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdActionDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyOpcodes"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyOptions"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMinimumLifetime"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMaximumLifetime"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMaxDescriptionLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvFwdInsideRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvDsliteAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvEpoch"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsValHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxNatPcpGroup.setStatus("current")

tmnxNatIsaStatV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 29)
)
tmnxNatIsaStatV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsValHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValMax"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValMaxLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValMaxHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValHw"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatV10v0Group.setStatus("current")

tmnxNatDeterministicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 30)
)
tmnxNatDeterministicGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInMaxDetSubscrLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInMaxDetSubLimitDsl"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyName"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnDetPortResv"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptLocation"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveNeeded"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSave"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveResult"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveTime"))
)
if mibBuilder.loadTexts:
    tmnxNatDeterministicGroup.setStatus("current")

tmnxNatVrtrIPFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 31)
)
tmnxNatVrtrIPFilterGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutUpstreamIPFilterId")
)
if mibBuilder.loadTexts:
    tmnxNatVrtrIPFilterGroup.setStatus("current")

tmnxNatPlV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 32)
)
tmnxNatPlV11v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvAllowPrivileged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeAdminDrain"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdRangeEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlOperMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdDynBlkResv"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionVRtrId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionBucketSize"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionNumBuckets"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionGo"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistTimestamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistBucketSize"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistNumBuckets"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistTcp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistUdp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistIcmp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeStatNumAllocBlk"))
)
if mibBuilder.loadTexts:
    tmnxNatPlV11v0Group.setStatus("current")

tmnxNatAccV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 33)
)
tmnxNatAccV11v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgAccountingPlcy")
)
if mibBuilder.loadTexts:
    tmnxNatAccV11v0Group.setStatus("current")

tmnxNatIsaStatV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 34)
)
tmnxNatIsaStatV11v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsValHw"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatV11v0Group.setStatus("current")

tmnxNatFragmentIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 35)
)
tmnxNatFragmentIpGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrFragmentIp"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InFragmentIp"))
)
if mibBuilder.loadTexts:
    tmnxNatFragmentIpGroup.setStatus("current")

tmnxNatMultiPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 36)
)
tmnxNatMultiPlcyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDestNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedFollowPoolRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedFollowPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubNextQryId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubMaxQryId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResultType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInSubType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInAddrPfxL"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInSubType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInAddrPfxL"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2ExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2PersistKey"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Description"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Origin"))
)
if mibBuilder.loadTexts:
    tmnxNatMultiPlcyGroup.setStatus("current")

tmnxNatIsaV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 37)
)
tmnxNatIsaV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpActiveMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaV12v0Group.setStatus("current")

tmnxNatQryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 38)
)
tmnxNatQryGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubNextQryId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPeak"))
)
if mibBuilder.loadTexts:
    tmnxNatQryGroup.setStatus("current")

tmnxNatVrtrIPFilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 39)
)
tmnxNatVrtrIPFilterV12v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnstreamIPFilterId")
)
if mibBuilder.loadTexts:
    tmnxNatVrtrIPFilterV12v0Group.setStatus("current")

tmnxNatFwd2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 40)
)
tmnxNatFwd2Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdActionSubType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionVRtrId"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionB4Addr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionL2awSubscriberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionProtocol"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionTimeOut"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionGo"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionSuccessful"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionTime"))
)
if mibBuilder.loadTexts:
    tmnxNatFwd2Group.setStatus("current")

tmnxNatLsnV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 41)
)
tmnxNatLsnV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnSubscriberLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyBlkLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTunnelMtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNat64LastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNat64RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIpv6Mtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InDropZeroIpv4Checksum"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSetTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIgnoreTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InInsertIpv6FragHeader"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnV12v0Group.setStatus("current")

tmnxNatLsnSubIdentV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 42)
)
tmnxNatLsnSubIdentV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatSubIdTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvName"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusAttributeType"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusVendorId"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDropUnidentified"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrTimeStamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdCount"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIdentV12v0Group.setStatus("current")

tmnxNatObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 98)
)
tmnxNatObsoleteGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSessionResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSessionWatermarkHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSessionWatermarkLo"),
        ("TIMETRA-NAT-MIB", "tmnxNatApTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatApIncludeAttributes"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersRetry"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersAlgorithm"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServSecret"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAcctPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatTxRequests"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatReqTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSendRetries"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeNumAllocatedBlk"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdPersistKey"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNat64SubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdStr"))
)
if mibBuilder.loadTexts:
    tmnxNatObsoleteGroup.setStatus("current")

tmnxNatNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 99)
)
tmnxNatNotifyObjsGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort2"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyCounter"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyNumber"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrPrefixLen"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxNatPlL2AwBlockUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 1)
)
tmnxNatPlL2AwBlockUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwBlockUsageHigh.setStatus(
        "current"
    )

tmnxNatIsaMemberSessionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 2)
)
tmnxNatIsaMemberSessionUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionUsageHigh.setStatus(
        "current"
    )

tmnxNatPlLsnMemberBlockUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 3)
)
tmnxNatPlLsnMemberBlockUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberBlockUsageHigh.setStatus(
        "current"
    )

tmnxNatLsnSubIcmpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 4)
)
tmnxNatLsnSubIcmpPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIcmpPortUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatLsnSubUdpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 5)
)
tmnxNatLsnSubUdpPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubUdpPortUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatLsnSubTcpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 6)
)
tmnxNatLsnSubTcpPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubTcpPortUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatL2AwSubIcmpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 7)
)
tmnxNatL2AwSubIcmpPortUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsageH")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubIcmpPortUsageHigh.setStatus(
        "current"
    )

tmnxNatL2AwSubUdpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 8)
)
tmnxNatL2AwSubUdpPortUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubUdpPortUsageHigh.setStatus(
        "current"
    )

tmnxNatL2AwSubTcpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 9)
)
tmnxNatL2AwSubTcpPortUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubTcpPortUsageHigh.setStatus(
        "current"
    )

tmnxNatL2AwSubSessionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 10)
)
tmnxNatL2AwSubSessionUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubSessionUsageHigh.setStatus(
        "current"
    )

tmnxNatLsnSubSessionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 11)
)
tmnxNatLsnSubSessionUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubSessionUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatPlBlockAllocationLsn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 12)
)
tmnxNatPlBlockAllocationLsn.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort2"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyNumber"))
)
if mibBuilder.loadTexts:
    tmnxNatPlBlockAllocationLsn.setStatus(
        "current"
    )

tmnxNatPlBlockAllocationL2Aw = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 13)
)
tmnxNatPlBlockAllocationL2Aw.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort2"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatPlBlockAllocationL2Aw.setStatus(
        "current"
    )

tmnxNatResourceProblemDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 14)
)
tmnxNatResourceProblemDetected.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatResourceProblem")
)
if mibBuilder.loadTexts:
    tmnxNatResourceProblemDetected.setStatus(
        "current"
    )

tmnxNatResourceProblemCause = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 15)
)
tmnxNatResourceProblemCause.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxNatResourceProblemCause.setStatus(
        "current"
    )

tmnxNatPlAddrFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 16)
)
tmnxNatPlAddrFree.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatPlAddrFree.setStatus(
        "current"
    )

tmnxNatPlLsnRedActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 17)
)
tmnxNatPlLsnRedActiveChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedActiveChanged.setStatus(
        "current"
    )

tmnxNatPcpSrvStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 18)
)
tmnxNatPcpSrvStateChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPcpSrvState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvStateChanged.setStatus(
        "current"
    )

tmnxNatFwdEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 19)
)
tmnxNatFwdEntryAdded.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdEntryAdded.setStatus(
        "obsolete"
    )

tmnxNatMdaActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 20)
)
tmnxNatMdaActive.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"))
)
if mibBuilder.loadTexts:
    tmnxNatMdaActive.setStatus(
        "current"
    )

tmnxNatLsnSubBlksFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 21)
)
tmnxNatLsnSubBlksFree.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyNumber"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlksFree.setStatus(
        "current"
    )

tmnxNatDetPlcyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 22)
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyChanged.setStatus(
        "current"
    )

tmnxNatMdaDetectsLoadSharingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 23)
)
tmnxNatMdaDetectsLoadSharingErr.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyCounter"))
)
if mibBuilder.loadTexts:
    tmnxNatMdaDetectsLoadSharingErr.setStatus(
        "current"
    )

tmnxNatIsaGrpOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 24)
)
tmnxNatIsaGrpOperStateChanged.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState")
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpOperStateChanged.setStatus(
        "current"
    )

tmnxNatIsaGrpIsDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 25)
)
tmnxNatIsaGrpIsDegraded.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDegraded")
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpIsDegraded.setStatus(
        "current"
    )

tmnxNatLsnSubIcmpPortUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 26)
)
tmnxNatLsnSubIcmpPortUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIcmpPortUsgHigh.setStatus(
        "current"
    )

tmnxNatLsnSubUdpPortUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 27)
)
tmnxNatLsnSubUdpPortUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubUdpPortUsgHigh.setStatus(
        "current"
    )

tmnxNatLsnSubTcpPortUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 28)
)
tmnxNatLsnSubTcpPortUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubTcpPortUsgHigh.setStatus(
        "current"
    )

tmnxNatLsnSubSessionUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 29)
)
tmnxNatLsnSubSessionUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubSessionUsgHigh.setStatus(
        "current"
    )

tmnxNatInAddrPrefixBlksFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 30)
)
tmnxNatInAddrPrefixBlksFree.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatInAddrPrefixBlksFree.setStatus(
        "current"
    )

tmnxNatFwd2EntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 31)
)
tmnxNatFwd2EntryAdded.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwd2OutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Origin"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatFwd2EntryAdded.setStatus(
        "current"
    )


# Notifications groups

tmnxNatNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 100)
)
tmnxNatNotifyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyGroup.setStatus(
        "obsolete"
    )

tmnxNatNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 101)
)
tmnxNatNotifyV9v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV9v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 102)
)
tmnxNatNotifyV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdEntryAdded"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV10v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 103)
)
tmnxNatNotifyV11v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV11v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 104)
)
tmnxNatNotifyV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2EntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpIsDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatInAddrPrefixBlksFree"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV12v0Group.setStatus(
        "current"
    )

tmnxNatObsoletedNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 150)
)
tmnxNatObsoletedNotifyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdEntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsageHigh"))
)
if mibBuilder.loadTexts:
    tmnxNatObsoletedNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxNatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 1)
)
tmnxNatCompliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatCompliance.setStatus(
        "obsolete"
    )

tmnxNatStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 2)
)
tmnxNatStatCompliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatStatCompliance.setStatus(
        "current"
    )

tmnxNatNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 3)
)
tmnxNatNotifyCompliance.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxNatV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 4)
)
tmnxNatV9v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestNatGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 5)
)
tmnxNatNotifyV9v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 6)
)
tmnxNatV10v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNat64Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 7)
)
tmnxNatNotifyV10v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 8)
)
tmnxNatV11v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNat64Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 9)
)
tmnxNatNotifyV11v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 10)
)
tmnxNatV12v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV12v0Compliance.setStatus(
        "current"
    )

tmnxNatNotifyV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 11)
)
tmnxNatNotifyV12v0Compliance.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyV12v0Group")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-NAT-MIB",
    **{"TmnxNatAlgProtocols": TmnxNatAlgProtocols,
       "TmnxNatFiltering": TmnxNatFiltering,
       "TmnxNatFragmentIpMode": TmnxNatFragmentIpMode,
       "TmnxNatFwdActionType": TmnxNatFwdActionType,
       "TmnxNatIsaGrpId": TmnxNatIsaGrpId,
       "TmnxNatIsaGrpIdOrZero": TmnxNatIsaGrpIdOrZero,
       "TmnxNatIsaMdaOperState": TmnxNatIsaMdaOperState,
       "TmnxNatMode": TmnxNatMode,
       "TmnxNatFwdEntryDescription": TmnxNatFwdEntryDescription,
       "TmnxNatPlType": TmnxNatPlType,
       "TmnxNatSubscriberIdString": TmnxNatSubscriberIdString,
       "TmnxNatUsageLevel": TmnxNatUsageLevel,
       "TmnxNatUsageStatsType": TmnxNatUsageStatsType,
       "TmnxNatWaterMark": TmnxNatWaterMark,
       "timetraNatMIBModule": timetraNatMIBModule,
       "tmnxNatConformance": tmnxNatConformance,
       "tmnxNatCompliances": tmnxNatCompliances,
       "tmnxNatCompliance": tmnxNatCompliance,
       "tmnxNatStatCompliance": tmnxNatStatCompliance,
       "tmnxNatNotifyCompliance": tmnxNatNotifyCompliance,
       "tmnxNatV9v0Compliance": tmnxNatV9v0Compliance,
       "tmnxNatNotifyV9v0Compliance": tmnxNatNotifyV9v0Compliance,
       "tmnxNatV10v0Compliance": tmnxNatV10v0Compliance,
       "tmnxNatNotifyV10v0Compliance": tmnxNatNotifyV10v0Compliance,
       "tmnxNatV11v0Compliance": tmnxNatV11v0Compliance,
       "tmnxNatNotifyV11v0Compliance": tmnxNatNotifyV11v0Compliance,
       "tmnxNatV12v0Compliance": tmnxNatV12v0Compliance,
       "tmnxNatNotifyV12v0Compliance": tmnxNatNotifyV12v0Compliance,
       "tmnxNatGroups": tmnxNatGroups,
       "tmnxNatIsaGroup": tmnxNatIsaGroup,
       "tmnxNatIsaStatGroup": tmnxNatIsaStatGroup,
       "tmnxNatPlcyGroup": tmnxNatPlcyGroup,
       "tmnxNatPlcyStatGroup": tmnxNatPlcyStatGroup,
       "tmnxNatVrtrGroup": tmnxNatVrtrGroup,
       "tmnxNatPlGroup": tmnxNatPlGroup,
       "tmnxNatDestGroup": tmnxNatDestGroup,
       "tmnxNatL2AwGroup": tmnxNatL2AwGroup,
       "tmnxNatLsnGroup": tmnxNatLsnGroup,
       "tmnxNatMapGroup": tmnxNatMapGroup,
       "tmnxNatLsnV9v0Group": tmnxNatLsnV9v0Group,
       "tmnxNatVrtrV9v0Group": tmnxNatVrtrV9v0Group,
       "tmnxNatPlcyV9v0Group": tmnxNatPlcyV9v0Group,
       "tmnxNatFwdGroup": tmnxNatFwdGroup,
       "tmnxNatPlV9v0Group": tmnxNatPlV9v0Group,
       "tmnxNatRedGroup": tmnxNatRedGroup,
       "tmnxNatDestNatGroup": tmnxNatDestNatGroup,
       "tmnxNatPlcyV10v0Group": tmnxNatPlcyV10v0Group,
       "tmnxNatIsaV10v0Group": tmnxNatIsaV10v0Group,
       "tmnxNatAccGroup": tmnxNatAccGroup,
       "tmnxNatWlanGwGroup": tmnxNatWlanGwGroup,
       "tmnxNat64Group": tmnxNat64Group,
       "tmnxNatLsnSubIdentGroup": tmnxNatLsnSubIdentGroup,
       "tmnxNatPcpGroup": tmnxNatPcpGroup,
       "tmnxNatIsaStatV10v0Group": tmnxNatIsaStatV10v0Group,
       "tmnxNatDeterministicGroup": tmnxNatDeterministicGroup,
       "tmnxNatVrtrIPFilterGroup": tmnxNatVrtrIPFilterGroup,
       "tmnxNatPlV11v0Group": tmnxNatPlV11v0Group,
       "tmnxNatAccV11v0Group": tmnxNatAccV11v0Group,
       "tmnxNatIsaStatV11v0Group": tmnxNatIsaStatV11v0Group,
       "tmnxNatFragmentIpGroup": tmnxNatFragmentIpGroup,
       "tmnxNatMultiPlcyGroup": tmnxNatMultiPlcyGroup,
       "tmnxNatIsaV12v0Group": tmnxNatIsaV12v0Group,
       "tmnxNatQryGroup": tmnxNatQryGroup,
       "tmnxNatVrtrIPFilterV12v0Group": tmnxNatVrtrIPFilterV12v0Group,
       "tmnxNatFwd2Group": tmnxNatFwd2Group,
       "tmnxNatLsnV12v0Group": tmnxNatLsnV12v0Group,
       "tmnxNatLsnSubIdentV12v0Group": tmnxNatLsnSubIdentV12v0Group,
       "tmnxNatObsoleteGroup": tmnxNatObsoleteGroup,
       "tmnxNatNotifyObjsGroup": tmnxNatNotifyObjsGroup,
       "tmnxNatNotifyGroup": tmnxNatNotifyGroup,
       "tmnxNatNotifyV9v0Group": tmnxNatNotifyV9v0Group,
       "tmnxNatNotifyV10v0Group": tmnxNatNotifyV10v0Group,
       "tmnxNatNotifyV11v0Group": tmnxNatNotifyV11v0Group,
       "tmnxNatNotifyV12v0Group": tmnxNatNotifyV12v0Group,
       "tmnxNatObsoletedNotifyGroup": tmnxNatObsoletedNotifyGroup,
       "tmnxNat": tmnxNat,
       "tmnxNatObjs": tmnxNatObjs,
       "tmnxNatIsaObjs": tmnxNatIsaObjs,
       "tmnxNatIsaGrpObjs": tmnxNatIsaGrpObjs,
       "tmnxNatIsaGrpTable": tmnxNatIsaGrpTable,
       "tmnxNatIsaGrpEntry": tmnxNatIsaGrpEntry,
       "tmnxNatIsaGrpId": tmnxNatIsaGrpId,
       "tmnxNatIsaGrpRowStatus": tmnxNatIsaGrpRowStatus,
       "tmnxNatIsaGrpLastMgmtChange": tmnxNatIsaGrpLastMgmtChange,
       "tmnxNatIsaGrpDescription": tmnxNatIsaGrpDescription,
       "tmnxNatIsaGrpAdminState": tmnxNatIsaGrpAdminState,
       "tmnxNatIsaGrpActiveMdaLimit": tmnxNatIsaGrpActiveMdaLimit,
       "tmnxNatIsaGrpSessionResvCount": tmnxNatIsaGrpSessionResvCount,
       "tmnxNatIsaGrpSessionWatermarkHi": tmnxNatIsaGrpSessionWatermarkHi,
       "tmnxNatIsaGrpSessionWatermarkLo": tmnxNatIsaGrpSessionWatermarkLo,
       "tmnxNatIsaGrpOperState": tmnxNatIsaGrpOperState,
       "tmnxNatIsaGrpDegraded": tmnxNatIsaGrpDegraded,
       "tmnxNatGrpCfgTable": tmnxNatGrpCfgTable,
       "tmnxNatGrpCfgEntry": tmnxNatGrpCfgEntry,
       "tmnxNatGrpCfgId": tmnxNatGrpCfgId,
       "tmnxNatGrpCfgLastMgmtChange": tmnxNatGrpCfgLastMgmtChange,
       "tmnxNatGrpCfgSessionResvCount": tmnxNatGrpCfgSessionResvCount,
       "tmnxNatGrpCfgSessionWatermarkHi": tmnxNatGrpCfgSessionWatermarkHi,
       "tmnxNatGrpCfgSessionWatermarkLo": tmnxNatGrpCfgSessionWatermarkLo,
       "tmnxNatGrpCfgAccountingPlcy": tmnxNatGrpCfgAccountingPlcy,
       "tmnxNatIsaMdaObjs": tmnxNatIsaMdaObjs,
       "tmnxNatIsaMdaTable": tmnxNatIsaMdaTable,
       "tmnxNatIsaMdaEntry": tmnxNatIsaMdaEntry,
       "tmnxNatIsaMdaRowStatus": tmnxNatIsaMdaRowStatus,
       "tmnxNatIsaMdaLastMgmtChange": tmnxNatIsaMdaLastMgmtChange,
       "tmnxNatIsaMdaStatObjs": tmnxNatIsaMdaStatObjs,
       "tmnxNatIsaMdaStatTable": tmnxNatIsaMdaStatTable,
       "tmnxNatIsaMdaStatEntry": tmnxNatIsaMdaStatEntry,
       "tmnxNatIsaMdaStatOperState": tmnxNatIsaMdaStatOperState,
       "tmnxNatIsaMemberTable": tmnxNatIsaMemberTable,
       "tmnxNatIsaMemberEntry": tmnxNatIsaMemberEntry,
       "tmnxNatIsaMemberId": tmnxNatIsaMemberId,
       "tmnxNatIsaMemberMdaState": tmnxNatIsaMemberMdaState,
       "tmnxNatIsaMemberMdaChassisIndex": tmnxNatIsaMemberMdaChassisIndex,
       "tmnxNatIsaMemberMdaCardSlotNum": tmnxNatIsaMemberMdaCardSlotNum,
       "tmnxNatIsaMemberMdaSlotNum": tmnxNatIsaMemberMdaSlotNum,
       "tmnxNatIsaMemberIpAddrReserved": tmnxNatIsaMemberIpAddrReserved,
       "tmnxNatIsaMemberBlocksReserved": tmnxNatIsaMemberBlocksReserved,
       "tmnxNatIsaMemberSessionUsage": tmnxNatIsaMemberSessionUsage,
       "tmnxNatIsaMemberSessionUsageHi": tmnxNatIsaMemberSessionUsageHi,
       "tmnxNatIsaMemberSessionsPrio": tmnxNatIsaMemberSessionsPrio,
       "tmnxNatIsaMemberStatsTable": tmnxNatIsaMemberStatsTable,
       "tmnxNatIsaMemberStatsEntry": tmnxNatIsaMemberStatsEntry,
       "tmnxNatIsaMemberStatsType": tmnxNatIsaMemberStatsType,
       "tmnxNatIsaMemberStatsName": tmnxNatIsaMemberStatsName,
       "tmnxNatIsaMemberStatsVal": tmnxNatIsaMemberStatsVal,
       "tmnxNatIsaMemberStatsValHw": tmnxNatIsaMemberStatsValHw,
       "tmnxNatIsaMemberStatsValue": tmnxNatIsaMemberStatsValue,
       "tmnxNatIsaResrcStatsTable": tmnxNatIsaResrcStatsTable,
       "tmnxNatIsaResrcStatsEntry": tmnxNatIsaResrcStatsEntry,
       "tmnxNatIsaResrcStatsId": tmnxNatIsaResrcStatsId,
       "tmnxNatIsaResrcStatsName": tmnxNatIsaResrcStatsName,
       "tmnxNatIsaResrcStatsValMax": tmnxNatIsaResrcStatsValMax,
       "tmnxNatIsaResrcStatsValMaxLw": tmnxNatIsaResrcStatsValMaxLw,
       "tmnxNatIsaResrcStatsValMaxHw": tmnxNatIsaResrcStatsValMaxHw,
       "tmnxNatIsaResrcStatsVal": tmnxNatIsaResrcStatsVal,
       "tmnxNatIsaResrcStatsValLw": tmnxNatIsaResrcStatsValLw,
       "tmnxNatIsaResrcStatsValHw": tmnxNatIsaResrcStatsValHw,
       "tmnxNatReassemblyStatsTable": tmnxNatReassemblyStatsTable,
       "tmnxNatReassemblyStatsEntry": tmnxNatReassemblyStatsEntry,
       "tmnxNatReassemblyStatsType": tmnxNatReassemblyStatsType,
       "tmnxNatReassemblyStatsName": tmnxNatReassemblyStatsName,
       "tmnxNatReassemblyStatsVal": tmnxNatReassemblyStatsVal,
       "tmnxNatReassemblyStatsValLw": tmnxNatReassemblyStatsValLw,
       "tmnxNatReassemblyStatsValHw": tmnxNatReassemblyStatsValHw,
       "tmnxNatPlcyObjs": tmnxNatPlcyObjs,
       "tmnxNatPlcyTable": tmnxNatPlcyTable,
       "tmnxNatPlcyEntry": tmnxNatPlcyEntry,
       "tmnxNatPlcyName": tmnxNatPlcyName,
       "tmnxNatPlcyLastMgmtChange": tmnxNatPlcyLastMgmtChange,
       "tmnxNatPlcyRowStatus": tmnxNatPlcyRowStatus,
       "tmnxNatPlcyDescription": tmnxNatPlcyDescription,
       "tmnxNatPlcyPool": tmnxNatPlcyPool,
       "tmnxNatPlcyPoolVRtr": tmnxNatPlcyPoolVRtr,
       "tmnxNatPlcyFiltering": tmnxNatPlcyFiltering,
       "tmnxNatPlcyPortResvCount": tmnxNatPlcyPortResvCount,
       "tmnxNatPlcyPortWatermarkHigh": tmnxNatPlcyPortWatermarkHigh,
       "tmnxNatPlcyPortWatermarkLow": tmnxNatPlcyPortWatermarkLow,
       "tmnxNatPlcySessionLimit": tmnxNatPlcySessionLimit,
       "tmnxNatPlcySessionResvCount": tmnxNatPlcySessionResvCount,
       "tmnxNatPlcySessionWatermarkHigh": tmnxNatPlcySessionWatermarkHigh,
       "tmnxNatPlcySessionWatermarkLow": tmnxNatPlcySessionWatermarkLow,
       "tmnxNatPlcyPrioSessionFcSet": tmnxNatPlcyPrioSessionFcSet,
       "tmnxNatPlcyToTcpEstab": tmnxNatPlcyToTcpEstab,
       "tmnxNatPlcyToTcpTrans": tmnxNatPlcyToTcpTrans,
       "tmnxNatPlcyToTcpSyn": tmnxNatPlcyToTcpSyn,
       "tmnxNatPlcyToTcpTimeWait": tmnxNatPlcyToTcpTimeWait,
       "tmnxNatPlcyToUdp": tmnxNatPlcyToUdp,
       "tmnxNatPlcyToUdpInitial": tmnxNatPlcyToUdpInitial,
       "tmnxNatPlcyToUdpDns": tmnxNatPlcyToUdpDns,
       "tmnxNatPlcyToIcmpQuery": tmnxNatPlcyToIcmpQuery,
       "tmnxNatPlcyBlkLimit": tmnxNatPlcyBlkLimit,
       "tmnxNatPlcyToSip": tmnxNatPlcyToSip,
       "tmnxNatPlcyAlgEnable": tmnxNatPlcyAlgEnable,
       "tmnxNatPlcyPortFwdLimit": tmnxNatPlcyPortFwdLimit,
       "tmnxNatPlcyUdpInboundRefresh": tmnxNatPlcyUdpInboundRefresh,
       "tmnxNatPlcyDestNatAddrType": tmnxNatPlcyDestNatAddrType,
       "tmnxNatPlcyDestNatAddr": tmnxNatPlcyDestNatAddr,
       "tmnxNatPlcyDestNatPort": tmnxNatPlcyDestNatPort,
       "tmnxNatPlcyIpfixExpPlcy": tmnxNatPlcyIpfixExpPlcy,
       "tmnxNatPlcyTcpMssAdjust": tmnxNatPlcyTcpMssAdjust,
       "tmnxNatPlcyToSubRetention": tmnxNatPlcyToSubRetention,
       "tmnxNatPlcyStatsTable": tmnxNatPlcyStatsTable,
       "tmnxNatPlcyStatsEntry": tmnxNatPlcyStatsEntry,
       "tmnxNatPlcyStatsType": tmnxNatPlcyStatsType,
       "tmnxNatPlcyStatsName": tmnxNatPlcyStatsName,
       "tmnxNatPlcyStatsVal": tmnxNatPlcyStatsVal,
       "tmnxNatVrtrObjs": tmnxNatVrtrObjs,
       "tmnxNatVrtrTable": tmnxNatVrtrTable,
       "tmnxNatVrtrEntry": tmnxNatVrtrEntry,
       "tmnxNatVrtrLastMgmtChange": tmnxNatVrtrLastMgmtChange,
       "tmnxNatVrtrRowStatus": tmnxNatVrtrRowStatus,
       "tmnxNatVrtrInPolicy": tmnxNatVrtrInPolicy,
       "tmnxNatVrtrInDsliteAdminState": tmnxNatVrtrInDsliteAdminState,
       "tmnxNatVrtrInDsliteSubPrefixLen": tmnxNatVrtrInDsliteSubPrefixLen,
       "tmnxNatVrtrInRedPeerAddrType": tmnxNatVrtrInRedPeerAddrType,
       "tmnxNatVrtrInRedPeerAddr": tmnxNatVrtrInRedPeerAddr,
       "tmnxNatVrtrInRedSteerRtType": tmnxNatVrtrInRedSteerRtType,
       "tmnxNatVrtrInRedSteerRt": tmnxNatVrtrInRedSteerRt,
       "tmnxNatVrtrInRedSteerRtLen": tmnxNatVrtrInRedSteerRtLen,
       "tmnxNatVrtrOutMtu": tmnxNatVrtrOutMtu,
       "tmnxNatVrtrOutUpstreamIPFilterId": tmnxNatVrtrOutUpstreamIPFilterId,
       "tmnxNatVrtrInMaxDetSubscrLimit": tmnxNatVrtrInMaxDetSubscrLimit,
       "tmnxNatVrtrInMaxDetSubLimitDsl": tmnxNatVrtrInMaxDetSubLimitDsl,
       "tmnxNatVrtrOutDnstreamIPFilterId": tmnxNatVrtrOutDnstreamIPFilterId,
       "tmnxNatVrtrInRedPeer6AddrType": tmnxNatVrtrInRedPeer6AddrType,
       "tmnxNatVrtrInRedPeer6Addr": tmnxNatVrtrInRedPeer6Addr,
       "tmnxNatL2AwAddrTable": tmnxNatL2AwAddrTable,
       "tmnxNatL2AwAddrEntry": tmnxNatL2AwAddrEntry,
       "tmnxNatL2AwAddrType": tmnxNatL2AwAddrType,
       "tmnxNatL2AwAddr": tmnxNatL2AwAddr,
       "tmnxNatL2AwAddrPrefixLen": tmnxNatL2AwAddrPrefixLen,
       "tmnxNatL2AwAddrRowStatus": tmnxNatL2AwAddrRowStatus,
       "tmnxNatL2AwAddrLastMgmtChange": tmnxNatL2AwAddrLastMgmtChange,
       "tmnxNat64Table": tmnxNat64Table,
       "tmnxNat64Entry": tmnxNat64Entry,
       "tmnxNat64LastMgmtChange": tmnxNat64LastMgmtChange,
       "tmnxNat64RowStatus": tmnxNat64RowStatus,
       "tmnxNat64InAdminState": tmnxNat64InAdminState,
       "tmnxNat64InSubPrefixLen": tmnxNat64InSubPrefixLen,
       "tmnxNat64InPrefix": tmnxNat64InPrefix,
       "tmnxNat64InPrefixLen": tmnxNat64InPrefixLen,
       "tmnxNat64InIpv6Mtu": tmnxNat64InIpv6Mtu,
       "tmnxNat64InDropZeroIpv4Checksum": tmnxNat64InDropZeroIpv4Checksum,
       "tmnxNat64InSetTos": tmnxNat64InSetTos,
       "tmnxNat64InTos": tmnxNat64InTos,
       "tmnxNat64InIgnoreTos": tmnxNat64InIgnoreTos,
       "tmnxNat64InInsertIpv6FragHeader": tmnxNat64InInsertIpv6FragHeader,
       "tmnxNat64InFragmentIp": tmnxNat64InFragmentIp,
       "tmnxNatSubIdTable": tmnxNatSubIdTable,
       "tmnxNatSubIdEntry": tmnxNatSubIdEntry,
       "tmnxNatSubIdLastMgmtChange": tmnxNatSubIdLastMgmtChange,
       "tmnxNatSubIdDescription": tmnxNatSubIdDescription,
       "tmnxNatSubIdAdminState": tmnxNatSubIdAdminState,
       "tmnxNatSubIdRadProxSrvRouter": tmnxNatSubIdRadProxSrvRouter,
       "tmnxNatSubIdRadProxSrvName": tmnxNatSubIdRadProxSrvName,
       "tmnxNatSubIdRadiusAttributeType": tmnxNatSubIdRadiusAttributeType,
       "tmnxNatSubIdRadiusVendorId": tmnxNatSubIdRadiusVendorId,
       "tmnxNatSubIdDropUnidentified": tmnxNatSubIdDropUnidentified,
       "tmnxNatDetPlcyTable": tmnxNatDetPlcyTable,
       "tmnxNatDetPlcyEntry": tmnxNatDetPlcyEntry,
       "tmnxNatDetPlcySubType": tmnxNatDetPlcySubType,
       "tmnxNatDetPlcyAddrType": tmnxNatDetPlcyAddrType,
       "tmnxNatDetPlcyAddr": tmnxNatDetPlcyAddr,
       "tmnxNatDetPlcyAddrPrefixLength": tmnxNatDetPlcyAddrPrefixLength,
       "tmnxNatDetPlcyRowStatus": tmnxNatDetPlcyRowStatus,
       "tmnxNatDetPlcyLastMgmtChange": tmnxNatDetPlcyLastMgmtChange,
       "tmnxNatDetPlcyName": tmnxNatDetPlcyName,
       "tmnxNatDetPlcyAdminState": tmnxNatDetPlcyAdminState,
       "tmnxNatDetMapTable": tmnxNatDetMapTable,
       "tmnxNatDetMapEntry": tmnxNatDetMapEntry,
       "tmnxNatDetMapInAddrType": tmnxNatDetMapInAddrType,
       "tmnxNatDetMapInStart": tmnxNatDetMapInStart,
       "tmnxNatDetMapInEnd": tmnxNatDetMapInEnd,
       "tmnxNatDetMapRowStatus": tmnxNatDetMapRowStatus,
       "tmnxNatDetMapLastCh": tmnxNatDetMapLastCh,
       "tmnxNatDetMapOutAddrType": tmnxNatDetMapOutAddrType,
       "tmnxNatDetMapOutStart": tmnxNatDetMapOutStart,
       "tmnxNatPoolObjs": tmnxNatPoolObjs,
       "tmnxNatPlTable": tmnxNatPlTable,
       "tmnxNatPlEntry": tmnxNatPlEntry,
       "tmnxNatPlName": tmnxNatPlName,
       "tmnxNatPlRowStatus": tmnxNatPlRowStatus,
       "tmnxNatPlLastMgmtChange": tmnxNatPlLastMgmtChange,
       "tmnxNatPlIsaGrp": tmnxNatPlIsaGrp,
       "tmnxNatPlType": tmnxNatPlType,
       "tmnxNatPlDescription": tmnxNatPlDescription,
       "tmnxNatPlAdminState": tmnxNatPlAdminState,
       "tmnxNatPlPortResvType": tmnxNatPlPortResvType,
       "tmnxNatPlPortResvVal": tmnxNatPlPortResvVal,
       "tmnxNatPlPortResvAllowPrivileged": tmnxNatPlPortResvAllowPrivileged,
       "tmnxNatPlWatermarkHigh": tmnxNatPlWatermarkHigh,
       "tmnxNatPlWatermarkLow": tmnxNatPlWatermarkLow,
       "tmnxNatPlMode": tmnxNatPlMode,
       "tmnxNatPlPortFwdRangeEnd": tmnxNatPlPortFwdRangeEnd,
       "tmnxNatPlPortFwdDynBlkResv": tmnxNatPlPortFwdDynBlkResv,
       "tmnxNatPlOperMode": tmnxNatPlOperMode,
       "tmnxNatPlRangeTable": tmnxNatPlRangeTable,
       "tmnxNatPlRangeEntry": tmnxNatPlRangeEntry,
       "tmnxNatPlRangeAddrType": tmnxNatPlRangeAddrType,
       "tmnxNatPlRangeStart": tmnxNatPlRangeStart,
       "tmnxNatPlRangeEnd": tmnxNatPlRangeEnd,
       "tmnxNatPlRangeRowStatus": tmnxNatPlRangeRowStatus,
       "tmnxNatPlRangeLastMgmtChange": tmnxNatPlRangeLastMgmtChange,
       "tmnxNatPlRangeDescription": tmnxNatPlRangeDescription,
       "tmnxNatPlRangeAdminDrain": tmnxNatPlRangeAdminDrain,
       "tmnxNatPlRangeNumAllocatedBlk": tmnxNatPlRangeNumAllocatedBlk,
       "tmnxNatPlL2AwTable": tmnxNatPlL2AwTable,
       "tmnxNatPlL2AwEntry": tmnxNatPlL2AwEntry,
       "tmnxNatPlL2AwBlockUsage": tmnxNatPlL2AwBlockUsage,
       "tmnxNatPlL2AwBlockUsageHi": tmnxNatPlL2AwBlockUsageHi,
       "tmnxNatPlLsnMemberTable": tmnxNatPlLsnMemberTable,
       "tmnxNatPlLsnMemberEntry": tmnxNatPlLsnMemberEntry,
       "tmnxNatPlLsnMemberIsaGrpId": tmnxNatPlLsnMemberIsaGrpId,
       "tmnxNatPlLsnMemberBlockUsage": tmnxNatPlLsnMemberBlockUsage,
       "tmnxNatPlLsnMemberBlockUsageHi": tmnxNatPlLsnMemberBlockUsageHi,
       "tmnxNatBlkL2AwTable": tmnxNatBlkL2AwTable,
       "tmnxNatBlkL2AwEntry": tmnxNatBlkL2AwEntry,
       "tmnxNatBlkL2AwAddrType": tmnxNatBlkL2AwAddrType,
       "tmnxNatBlkL2AwAddr": tmnxNatBlkL2AwAddr,
       "tmnxNatBlkL2AwStart": tmnxNatBlkL2AwStart,
       "tmnxNatBlkL2AwEnd": tmnxNatBlkL2AwEnd,
       "tmnxNatBlkL2AwPool": tmnxNatBlkL2AwPool,
       "tmnxNatBlkL2AwSubIdent": tmnxNatBlkL2AwSubIdent,
       "tmnxNatBlkL2AwPolicy": tmnxNatBlkL2AwPolicy,
       "tmnxNatBlkL2AwStartDateAndTime": tmnxNatBlkL2AwStartDateAndTime,
       "tmnxNatBlkLsnTable": tmnxNatBlkLsnTable,
       "tmnxNatBlkLsnEntry": tmnxNatBlkLsnEntry,
       "tmnxNatBlkLsnAddrType": tmnxNatBlkLsnAddrType,
       "tmnxNatBlkLsnAddr": tmnxNatBlkLsnAddr,
       "tmnxNatBlkLsnStart": tmnxNatBlkLsnStart,
       "tmnxNatBlkLsnEnd": tmnxNatBlkLsnEnd,
       "tmnxNatBlkLsnPool": tmnxNatBlkLsnPool,
       "tmnxNatBlkLsnSubId": tmnxNatBlkLsnSubId,
       "tmnxNatBlkLsnInsideVRtrID": tmnxNatBlkLsnInsideVRtrID,
       "tmnxNatBlkLsnInsideAddrType": tmnxNatBlkLsnInsideAddrType,
       "tmnxNatBlkLsnInsideAddr": tmnxNatBlkLsnInsideAddr,
       "tmnxNatBlkLsnPolicy": tmnxNatBlkLsnPolicy,
       "tmnxNatBlkLsnStartDateAndTime": tmnxNatBlkLsnStartDateAndTime,
       "tmnxNatPlLsnTable": tmnxNatPlLsnTable,
       "tmnxNatPlLsnEntry": tmnxNatPlLsnEntry,
       "tmnxNatPlLsnSubscriberLimit": tmnxNatPlLsnSubscriberLimit,
       "tmnxNatPlLsnRedExpPrefixType": tmnxNatPlLsnRedExpPrefixType,
       "tmnxNatPlLsnRedExpPrefix": tmnxNatPlLsnRedExpPrefix,
       "tmnxNatPlLsnRedExpPrefixLen": tmnxNatPlLsnRedExpPrefixLen,
       "tmnxNatPlLsnRedMonPrefixType": tmnxNatPlLsnRedMonPrefixType,
       "tmnxNatPlLsnRedMonPrefix": tmnxNatPlLsnRedMonPrefix,
       "tmnxNatPlLsnRedMonPrefixLen": tmnxNatPlLsnRedMonPrefixLen,
       "tmnxNatPlLsnRedActive": tmnxNatPlLsnRedActive,
       "tmnxNatPlLsnDetPortResv": tmnxNatPlLsnDetPortResv,
       "tmnxNatPlLsnRedAdminState": tmnxNatPlLsnRedAdminState,
       "tmnxNatPlLsnRedFollowPoolRouter": tmnxNatPlLsnRedFollowPoolRouter,
       "tmnxNatPlLsnRedFollowPool": tmnxNatPlLsnRedFollowPool,
       "tmnxNatPlHistAction": tmnxNatPlHistAction,
       "tmnxNatPlHistActionVRtrId": tmnxNatPlHistActionVRtrId,
       "tmnxNatPlHistActionPoolName": tmnxNatPlHistActionPoolName,
       "tmnxNatPlHistActionBucketSize": tmnxNatPlHistActionBucketSize,
       "tmnxNatPlHistActionNumBuckets": tmnxNatPlHistActionNumBuckets,
       "tmnxNatPlHistActionGo": tmnxNatPlHistActionGo,
       "tmnxNatPlHistTable": tmnxNatPlHistTable,
       "tmnxNatPlHistEntry": tmnxNatPlHistEntry,
       "tmnxNatPlHistIndex": tmnxNatPlHistIndex,
       "tmnxNatPlHistTimestamp": tmnxNatPlHistTimestamp,
       "tmnxNatPlHistVRtrID": tmnxNatPlHistVRtrID,
       "tmnxNatPlHistPoolName": tmnxNatPlHistPoolName,
       "tmnxNatPlHistBucketSize": tmnxNatPlHistBucketSize,
       "tmnxNatPlHistNumBuckets": tmnxNatPlHistNumBuckets,
       "tmnxNatPlHistTcp": tmnxNatPlHistTcp,
       "tmnxNatPlHistUdp": tmnxNatPlHistUdp,
       "tmnxNatPlHistIcmp": tmnxNatPlHistIcmp,
       "tmnxNatPlRangeStatTable": tmnxNatPlRangeStatTable,
       "tmnxNatPlRangeStatEntry": tmnxNatPlRangeStatEntry,
       "tmnxNatPlRangeStatNumAllocBlk": tmnxNatPlRangeStatNumAllocBlk,
       "tmnxNatDestObjs": tmnxNatDestObjs,
       "tmnxNatDestTable": tmnxNatDestTable,
       "tmnxNatDestEntry": tmnxNatDestEntry,
       "tmnxNatDestAddrType": tmnxNatDestAddrType,
       "tmnxNatDestAddr": tmnxNatDestAddr,
       "tmnxNatDestPrefixLen": tmnxNatDestPrefixLen,
       "tmnxNatDestRowStatus": tmnxNatDestRowStatus,
       "tmnxNatDestLastMgmtChange": tmnxNatDestLastMgmtChange,
       "tmnxNatDestNatPolicy": tmnxNatDestNatPolicy,
       "tmnxNatDsliteAddrTable": tmnxNatDsliteAddrTable,
       "tmnxNatDsliteAddrEntry": tmnxNatDsliteAddrEntry,
       "tmnxNatDsliteAddrType": tmnxNatDsliteAddrType,
       "tmnxNatDsliteAddr": tmnxNatDsliteAddr,
       "tmnxNatDsliteAddrRowStatus": tmnxNatDsliteAddrRowStatus,
       "tmnxNatDsliteAddrLastMgmtChange": tmnxNatDsliteAddrLastMgmtChange,
       "tmnxNatDsliteAddrTunnelMtu": tmnxNatDsliteAddrTunnelMtu,
       "tmnxNatDsliteAddrFragmentIp": tmnxNatDsliteAddrFragmentIp,
       "tmnxNatSubObjs": tmnxNatSubObjs,
       "tmnxNatLsnHostTable": tmnxNatLsnHostTable,
       "tmnxNatLsnHostEntry": tmnxNatLsnHostEntry,
       "tmnxNatLsnHostAddrType": tmnxNatLsnHostAddrType,
       "tmnxNatLsnHostAddr": tmnxNatLsnHostAddr,
       "tmnxNatLsnHostSubId": tmnxNatLsnHostSubId,
       "tmnxNatLsnHostOutVRtrID": tmnxNatLsnHostOutVRtrID,
       "tmnxNatLsnHostOutAddrType": tmnxNatLsnHostOutAddrType,
       "tmnxNatLsnHostOutAddr": tmnxNatLsnHostOutAddr,
       "tmnxNatLsnSubTable": tmnxNatLsnSubTable,
       "tmnxNatLsnSubEntry": tmnxNatLsnSubEntry,
       "tmnxNatLsnSubId": tmnxNatLsnSubId,
       "tmnxNatLsnSubPolicy": tmnxNatLsnSubPolicy,
       "tmnxNatLsnSubIsaGrp": tmnxNatLsnSubIsaGrp,
       "tmnxNatLsnSubIsaMemberId": tmnxNatLsnSubIsaMemberId,
       "tmnxNatLsnSubOutVRtrID": tmnxNatLsnSubOutVRtrID,
       "tmnxNatLsnSubOutAddrType": tmnxNatLsnSubOutAddrType,
       "tmnxNatLsnSubOutAddr": tmnxNatLsnSubOutAddr,
       "tmnxNatLsnSubIdStr": tmnxNatLsnSubIdStr,
       "tmnxNatLsnSubStatTable": tmnxNatLsnSubStatTable,
       "tmnxNatLsnSubStatEntry": tmnxNatLsnSubStatEntry,
       "tmnxNatLsnSubStatIcmpPortUsage": tmnxNatLsnSubStatIcmpPortUsage,
       "tmnxNatLsnSubStatIcmpPortUsageHi": tmnxNatLsnSubStatIcmpPortUsageHi,
       "tmnxNatLsnSubStatUdpPortUsage": tmnxNatLsnSubStatUdpPortUsage,
       "tmnxNatLsnSubStatUdpPortUsageHi": tmnxNatLsnSubStatUdpPortUsageHi,
       "tmnxNatLsnSubStatTcpPortUsage": tmnxNatLsnSubStatTcpPortUsage,
       "tmnxNatLsnSubStatTcpPortUsageHi": tmnxNatLsnSubStatTcpPortUsageHi,
       "tmnxNatLsnSubStatSessionUsage": tmnxNatLsnSubStatSessionUsage,
       "tmnxNatLsnSubStatSessionUsageHi": tmnxNatLsnSubStatSessionUsageHi,
       "tmnxNatLsnSubStatSessions": tmnxNatLsnSubStatSessions,
       "tmnxNatLsnSubStatSessionsPrio": tmnxNatLsnSubStatSessionsPrio,
       "tmnxNatLsnSubStatSessionsPeak": tmnxNatLsnSubStatSessionsPeak,
       "tmnxNatLsnSubBlkTable": tmnxNatLsnSubBlkTable,
       "tmnxNatLsnSubBlkEntry": tmnxNatLsnSubBlkEntry,
       "tmnxNatLsnSubBlkEnd": tmnxNatLsnSubBlkEnd,
       "tmnxNatLsnSubBlkPolicy": tmnxNatLsnSubBlkPolicy,
       "tmnxNatDsliteSubTable": tmnxNatDsliteSubTable,
       "tmnxNatDsliteSubEntry": tmnxNatDsliteSubEntry,
       "tmnxNatDsliteSubAddrType": tmnxNatDsliteSubAddrType,
       "tmnxNatDsliteSubAddr": tmnxNatDsliteSubAddr,
       "tmnxNatDsliteSubAddrPrefixLength": tmnxNatDsliteSubAddrPrefixLength,
       "tmnxNatDsliteSubId": tmnxNatDsliteSubId,
       "tmnxNatL2AwHostTable": tmnxNatL2AwHostTable,
       "tmnxNatL2AwHostEntry": tmnxNatL2AwHostEntry,
       "tmnxNatL2AwHostAddrType": tmnxNatL2AwHostAddrType,
       "tmnxNatL2AwHostAddr": tmnxNatL2AwHostAddr,
       "tmnxNatL2AwHostOutVRtrID": tmnxNatL2AwHostOutVRtrID,
       "tmnxNatL2AwHostOutAddrType": tmnxNatL2AwHostOutAddrType,
       "tmnxNatL2AwHostOutAddr": tmnxNatL2AwHostOutAddr,
       "tmnxNatL2AwHostOutStart": tmnxNatL2AwHostOutStart,
       "tmnxNatL2AwSubTable": tmnxNatL2AwSubTable,
       "tmnxNatL2AwSubEntry": tmnxNatL2AwSubEntry,
       "tmnxNatL2AwSubPolicy": tmnxNatL2AwSubPolicy,
       "tmnxNatL2AwSubIsaGrp": tmnxNatL2AwSubIsaGrp,
       "tmnxNatL2AwSubIsaMemberId": tmnxNatL2AwSubIsaMemberId,
       "tmnxNatL2AwSubOutVRtrID": tmnxNatL2AwSubOutVRtrID,
       "tmnxNatL2AwSubOutAddrType": tmnxNatL2AwSubOutAddrType,
       "tmnxNatL2AwSubOutAddr": tmnxNatL2AwSubOutAddr,
       "tmnxNatL2AwSubStatTable": tmnxNatL2AwSubStatTable,
       "tmnxNatL2AwSubStatEntry": tmnxNatL2AwSubStatEntry,
       "tmnxNatL2AwSubStatIcmpPortUsage": tmnxNatL2AwSubStatIcmpPortUsage,
       "tmnxNatL2AwSubStatIcmpPortUsageH": tmnxNatL2AwSubStatIcmpPortUsageH,
       "tmnxNatL2AwSubStatUdpPortUsage": tmnxNatL2AwSubStatUdpPortUsage,
       "tmnxNatL2AwSubStatUdpPortUsageHi": tmnxNatL2AwSubStatUdpPortUsageHi,
       "tmnxNatL2AwSubStatTcpPortUsage": tmnxNatL2AwSubStatTcpPortUsage,
       "tmnxNatL2AwSubStatTcpPortUsageHi": tmnxNatL2AwSubStatTcpPortUsageHi,
       "tmnxNatL2AwSubStatSessionUsage": tmnxNatL2AwSubStatSessionUsage,
       "tmnxNatL2AwSubStatSessionUsageHi": tmnxNatL2AwSubStatSessionUsageHi,
       "tmnxNatL2AwSubStatSessions": tmnxNatL2AwSubStatSessions,
       "tmnxNatL2AwSubStatSessionsPrio": tmnxNatL2AwSubStatSessionsPrio,
       "tmnxNatL2AwSubStatSessionsPeak": tmnxNatL2AwSubStatSessionsPeak,
       "tmnxNatL2AwSubBlkTable": tmnxNatL2AwSubBlkTable,
       "tmnxNatL2AwSubBlkEntry": tmnxNatL2AwSubBlkEntry,
       "tmnxNatL2AwSubBlkEnd": tmnxNatL2AwSubBlkEnd,
       "tmnxNat64SubTable": tmnxNat64SubTable,
       "tmnxNat64SubEntry": tmnxNat64SubEntry,
       "tmnxNat64SubAddrType": tmnxNat64SubAddrType,
       "tmnxNat64SubAddr": tmnxNat64SubAddr,
       "tmnxNat64SubAddrPrefixLength": tmnxNat64SubAddrPrefixLength,
       "tmnxNat64SubId": tmnxNat64SubId,
       "tmnxNatLsnSubscIdStrTable": tmnxNatLsnSubscIdStrTable,
       "tmnxNatLsnSubscIdStrEntry": tmnxNatLsnSubscIdStrEntry,
       "tmnxNatLsnSubscIdStr": tmnxNatLsnSubscIdStr,
       "tmnxNatLsnSubscIdStrType": tmnxNatLsnSubscIdStrType,
       "tmnxNatLsnSubscIdStrAddrType": tmnxNatLsnSubscIdStrAddrType,
       "tmnxNatLsnSubscIdStrAddr": tmnxNatLsnSubscIdStrAddr,
       "tmnxNatLsnSubscIdStrTimeStamp": tmnxNatLsnSubscIdStrTimeStamp,
       "tmnxNatMapObjs": tmnxNatMapObjs,
       "tmnxNatMapLsnHostTable": tmnxNatMapLsnHostTable,
       "tmnxNatMapLsnHostEntry": tmnxNatMapLsnHostEntry,
       "tmnxNatMapLsnHostAddrType": tmnxNatMapLsnHostAddrType,
       "tmnxNatMapLsnHostAddr": tmnxNatMapLsnHostAddr,
       "tmnxNatMapLsnHostRowStatus": tmnxNatMapLsnHostRowStatus,
       "tmnxNatMapLsnHostLastMgmtChange": tmnxNatMapLsnHostLastMgmtChange,
       "tmnxNatMapLsnHostAdminState": tmnxNatMapLsnHostAdminState,
       "tmnxNatMapLsnHostOutAddrType": tmnxNatMapLsnHostOutAddrType,
       "tmnxNatMapLsnHostOutAddr": tmnxNatMapLsnHostOutAddr,
       "tmnxNatMapLsnHostOutVRtrID": tmnxNatMapLsnHostOutVRtrID,
       "tmnxNatMapTable": tmnxNatMapTable,
       "tmnxNatMapEntry": tmnxNatMapEntry,
       "tmnxNatMapAddrType": tmnxNatMapAddrType,
       "tmnxNatMapAddr": tmnxNatMapAddr,
       "tmnxNatMapPort": tmnxNatMapPort,
       "tmnxNatMapProtocol": tmnxNatMapProtocol,
       "tmnxNatMapRowStatus": tmnxNatMapRowStatus,
       "tmnxNatMapLastMgmtChange": tmnxNatMapLastMgmtChange,
       "tmnxNatMapOutPort": tmnxNatMapOutPort,
       "tmnxNatFwdObjs": tmnxNatFwdObjs,
       "tmnxNatFwdAction": tmnxNatFwdAction,
       "tmnxNatFwdActionSubType": tmnxNatFwdActionSubType,
       "tmnxNatFwdActionVRtrId": tmnxNatFwdActionVRtrId,
       "tmnxNatFwdActionAddrType": tmnxNatFwdActionAddrType,
       "tmnxNatFwdActionAddr": tmnxNatFwdActionAddr,
       "tmnxNatFwdActionB4Addr": tmnxNatFwdActionB4Addr,
       "tmnxNatFwdActionAftrAddr": tmnxNatFwdActionAftrAddr,
       "tmnxNatFwdActionL2awSubscriberId": tmnxNatFwdActionL2awSubscriberId,
       "tmnxNatFwdActionProtocol": tmnxNatFwdActionProtocol,
       "tmnxNatFwdActionTimeOut": tmnxNatFwdActionTimeOut,
       "tmnxNatFwdActionPort": tmnxNatFwdActionPort,
       "tmnxNatFwdActionOutPort": tmnxNatFwdActionOutPort,
       "tmnxNatFwdActionOutAddr": tmnxNatFwdActionOutAddr,
       "tmnxNatFwdActionType": tmnxNatFwdActionType,
       "tmnxNatFwdActionGo": tmnxNatFwdActionGo,
       "tmnxNatFwdActionSuccessful": tmnxNatFwdActionSuccessful,
       "tmnxNatFwdActionTime": tmnxNatFwdActionTime,
       "tmnxNatFwdActionDescription": tmnxNatFwdActionDescription,
       "tmnxNatFwdActionNatPolicy": tmnxNatFwdActionNatPolicy,
       "tmnxNatFwdTable": tmnxNatFwdTable,
       "tmnxNatFwdEntry": tmnxNatFwdEntry,
       "tmnxNatFwdSubType": tmnxNatFwdSubType,
       "tmnxNatFwdL2awSubIdent": tmnxNatFwdL2awSubIdent,
       "tmnxNatFwdLsnVRtrID": tmnxNatFwdLsnVRtrID,
       "tmnxNatFwdLsnB4AddrType": tmnxNatFwdLsnB4AddrType,
       "tmnxNatFwdLsnB4Addr": tmnxNatFwdLsnB4Addr,
       "tmnxNatFwdAddrType": tmnxNatFwdAddrType,
       "tmnxNatFwdAddr": tmnxNatFwdAddr,
       "tmnxNatFwdProtocol": tmnxNatFwdProtocol,
       "tmnxNatFwdPort": tmnxNatFwdPort,
       "tmnxNatFwdOutVRtrID": tmnxNatFwdOutVRtrID,
       "tmnxNatFwdOutAddrType": tmnxNatFwdOutAddrType,
       "tmnxNatFwdOutAddr": tmnxNatFwdOutAddr,
       "tmnxNatFwdOutPort": tmnxNatFwdOutPort,
       "tmnxNatFwdExpiryDateAndTime": tmnxNatFwdExpiryDateAndTime,
       "tmnxNatFwdLsnAftrAddrType": tmnxNatFwdLsnAftrAddrType,
       "tmnxNatFwdLsnAftrAddr": tmnxNatFwdLsnAftrAddr,
       "tmnxNatFwdPersistKey": tmnxNatFwdPersistKey,
       "tmnxNatFwdDescription": tmnxNatFwdDescription,
       "tmnxNatFwdOrigin": tmnxNatFwdOrigin,
       "tmnxNatFwd2Table": tmnxNatFwd2Table,
       "tmnxNatFwd2Entry": tmnxNatFwd2Entry,
       "tmnxNatFwd2SubType": tmnxNatFwd2SubType,
       "tmnxNatFwd2L2awSubIdent": tmnxNatFwd2L2awSubIdent,
       "tmnxNatFwd2LsnVRtrID": tmnxNatFwd2LsnVRtrID,
       "tmnxNatFwd2LsnB4AddrType": tmnxNatFwd2LsnB4AddrType,
       "tmnxNatFwd2LsnB4Addr": tmnxNatFwd2LsnB4Addr,
       "tmnxNatFwd2AddrType": tmnxNatFwd2AddrType,
       "tmnxNatFwd2Addr": tmnxNatFwd2Addr,
       "tmnxNatFwd2Protocol": tmnxNatFwd2Protocol,
       "tmnxNatFwd2Port": tmnxNatFwd2Port,
       "tmnxNatFwd2NatPolicy": tmnxNatFwd2NatPolicy,
       "tmnxNatFwd2OutVRtrID": tmnxNatFwd2OutVRtrID,
       "tmnxNatFwd2OutAddrType": tmnxNatFwd2OutAddrType,
       "tmnxNatFwd2OutAddr": tmnxNatFwd2OutAddr,
       "tmnxNatFwd2OutPort": tmnxNatFwd2OutPort,
       "tmnxNatFwd2ExpiryDateAndTime": tmnxNatFwd2ExpiryDateAndTime,
       "tmnxNatFwd2LsnAftrAddrType": tmnxNatFwd2LsnAftrAddrType,
       "tmnxNatFwd2LsnAftrAddr": tmnxNatFwd2LsnAftrAddr,
       "tmnxNatFwd2PersistKey": tmnxNatFwd2PersistKey,
       "tmnxNatFwd2Description": tmnxNatFwd2Description,
       "tmnxNatFwd2Origin": tmnxNatFwd2Origin,
       "tmnxNatAccObjs": tmnxNatAccObjs,
       "tmnxNatApTable": tmnxNatApTable,
       "tmnxNatApEntry": tmnxNatApEntry,
       "tmnxNatApName": tmnxNatApName,
       "tmnxNatApLastMgmtChange": tmnxNatApLastMgmtChange,
       "tmnxNatApRowStatus": tmnxNatApRowStatus,
       "tmnxNatApDescription": tmnxNatApDescription,
       "tmnxNatApIncludeAttributes": tmnxNatApIncludeAttributes,
       "tmnxNatApServersTimeout": tmnxNatApServersTimeout,
       "tmnxNatApServersRetry": tmnxNatApServersRetry,
       "tmnxNatApServersVRtrID": tmnxNatApServersVRtrID,
       "tmnxNatApServersSrcAddrType": tmnxNatApServersSrcAddrType,
       "tmnxNatApServersSrcAddrStart": tmnxNatApServersSrcAddrStart,
       "tmnxNatApServersSrcAddrEnd": tmnxNatApServersSrcAddrEnd,
       "tmnxNatApServersAlgorithm": tmnxNatApServersAlgorithm,
       "tmnxNatApServTable": tmnxNatApServTable,
       "tmnxNatApServEntry": tmnxNatApServEntry,
       "tmnxNatApServIndex": tmnxNatApServIndex,
       "tmnxNatApServRowStatus": tmnxNatApServRowStatus,
       "tmnxNatApServLastMgmtChange": tmnxNatApServLastMgmtChange,
       "tmnxNatApServAddrType": tmnxNatApServAddrType,
       "tmnxNatApServAddr": tmnxNatApServAddr,
       "tmnxNatApServSecret": tmnxNatApServSecret,
       "tmnxNatApServAcctPort": tmnxNatApServAcctPort,
       "tmnxNatApServStatTable": tmnxNatApServStatTable,
       "tmnxNatApServStatEntry": tmnxNatApServStatEntry,
       "tmnxNatApServStatSrcAddrType": tmnxNatApServStatSrcAddrType,
       "tmnxNatApServStatSrcAddr": tmnxNatApServStatSrcAddr,
       "tmnxNatApServStatOperState": tmnxNatApServStatOperState,
       "tmnxNatApServStatTxRequests": tmnxNatApServStatTxRequests,
       "tmnxNatApServStatReqTimeout": tmnxNatApServStatReqTimeout,
       "tmnxNatApServStatSendRetries": tmnxNatApServStatSendRetries,
       "tmnxNatPcpObjs": tmnxNatPcpObjs,
       "tmnxNatPcpPlcyTable": tmnxNatPcpPlcyTable,
       "tmnxNatPcpPlcyEntry": tmnxNatPcpPlcyEntry,
       "tmnxNatPcpPlcyName": tmnxNatPcpPlcyName,
       "tmnxNatPcpPlcyLastMgmtChange": tmnxNatPcpPlcyLastMgmtChange,
       "tmnxNatPcpPlcyRowStatus": tmnxNatPcpPlcyRowStatus,
       "tmnxNatPcpPlcyDescription": tmnxNatPcpPlcyDescription,
       "tmnxNatPcpPlcyOpcodes": tmnxNatPcpPlcyOpcodes,
       "tmnxNatPcpPlcyOptions": tmnxNatPcpPlcyOptions,
       "tmnxNatPcpPlcyMinimumLifetime": tmnxNatPcpPlcyMinimumLifetime,
       "tmnxNatPcpPlcyMaximumLifetime": tmnxNatPcpPlcyMaximumLifetime,
       "tmnxNatPcpPlcyMaxDescriptionLen": tmnxNatPcpPlcyMaxDescriptionLen,
       "tmnxNatPcpSrvTable": tmnxNatPcpSrvTable,
       "tmnxNatPcpSrvEntry": tmnxNatPcpSrvEntry,
       "tmnxNatPcpSrvName": tmnxNatPcpSrvName,
       "tmnxNatPcpSrvLastCh": tmnxNatPcpSrvLastCh,
       "tmnxNatPcpSrvRowStatus": tmnxNatPcpSrvRowStatus,
       "tmnxNatPcpSrvAdminState": tmnxNatPcpSrvAdminState,
       "tmnxNatPcpSrvDescription": tmnxNatPcpSrvDescription,
       "tmnxNatPcpSrvPlcy": tmnxNatPcpSrvPlcy,
       "tmnxNatPcpSrvFwdInsideRouter": tmnxNatPcpSrvFwdInsideRouter,
       "tmnxNatPcpSrvDsliteAftrAddr": tmnxNatPcpSrvDsliteAftrAddr,
       "tmnxNatPcpSrvState": tmnxNatPcpSrvState,
       "tmnxNatPcpSrvStateDescription": tmnxNatPcpSrvStateDescription,
       "tmnxNatPcpSrvEpoch": tmnxNatPcpSrvEpoch,
       "tmnxNatPcpSrvIfTable": tmnxNatPcpSrvIfTable,
       "tmnxNatPcpSrvIfEntry": tmnxNatPcpSrvIfEntry,
       "tmnxNatPcpSrvIfRowStatus": tmnxNatPcpSrvIfRowStatus,
       "tmnxNatPcpSrvIfLastCh": tmnxNatPcpSrvIfLastCh,
       "tmnxNatPcpSrvIfStatsTable": tmnxNatPcpSrvIfStatsTable,
       "tmnxNatPcpSrvIfStatsEntry": tmnxNatPcpSrvIfStatsEntry,
       "tmnxNatPcpSrvIfStatsType": tmnxNatPcpSrvIfStatsType,
       "tmnxNatPcpSrvIfStatsName": tmnxNatPcpSrvIfStatsName,
       "tmnxNatPcpSrvIfStatsValLw": tmnxNatPcpSrvIfStatsValLw,
       "tmnxNatPcpSrvIfStatsValHw": tmnxNatPcpSrvIfStatsValHw,
       "tmnxNatPcpSrvIfStatsVal": tmnxNatPcpSrvIfStatsVal,
       "tmnxNatSubscIdObjs": tmnxNatSubscIdObjs,
       "tmnxNatSubscIdVendorTable": tmnxNatSubscIdVendorTable,
       "tmnxNatSubscIdVendorEntry": tmnxNatSubscIdVendorEntry,
       "tmnxNatSubscIdVendorId": tmnxNatSubscIdVendorId,
       "tmnxNatSubscIdVendorStr": tmnxNatSubscIdVendorStr,
       "tmnxNatSubscIdVendorDescription": tmnxNatSubscIdVendorDescription,
       "tmnxNatSubscIdAttrTable": tmnxNatSubscIdAttrTable,
       "tmnxNatSubscIdAttrEntry": tmnxNatSubscIdAttrEntry,
       "tmnxNatSubscIdAttrType": tmnxNatSubscIdAttrType,
       "tmnxNatSubscIdAttrStr": tmnxNatSubscIdAttrStr,
       "tmnxNatSubscIdAttrDescription": tmnxNatSubscIdAttrDescription,
       "tmnxNatDetScriptObjs": tmnxNatDetScriptObjs,
       "tmnxNatDetScriptLocation": tmnxNatDetScriptLocation,
       "tmnxNatDetScriptSaveNeeded": tmnxNatDetScriptSaveNeeded,
       "tmnxNatDetScriptSave": tmnxNatDetScriptSave,
       "tmnxNatDetScriptSaveResult": tmnxNatDetScriptSaveResult,
       "tmnxNatDetScriptSaveTime": tmnxNatDetScriptSaveTime,
       "tmnxNatQryObjs": tmnxNatQryObjs,
       "tmnxNatQryLsnSubObjs": tmnxNatQryLsnSubObjs,
       "tmnxNatQryLsnSubNextQryId": tmnxNatQryLsnSubNextQryId,
       "tmnxNatQryLsnSubTable": tmnxNatQryLsnSubTable,
       "tmnxNatQryLsnSubEntry": tmnxNatQryLsnSubEntry,
       "tmnxNatQryLsnSubQryId": tmnxNatQryLsnSubQryId,
       "tmnxNatQryLsnSubRowStatus": tmnxNatQryLsnSubRowStatus,
       "tmnxNatQryLsnSubResultType": tmnxNatQryLsnSubResultType,
       "tmnxNatQryLsnSubWhereNatPolicy": tmnxNatQryLsnSubWhereNatPolicy,
       "tmnxNatQryLsnSubWhereIsaGrp": tmnxNatQryLsnSubWhereIsaGrp,
       "tmnxNatQryLsnSubWhereMemberId": tmnxNatQryLsnSubWhereMemberId,
       "tmnxNatQryLsnSubWhereOutRouter": tmnxNatQryLsnSubWhereOutRouter,
       "tmnxNatQryLsnSubWhereOutAddrType": tmnxNatQryLsnSubWhereOutAddrType,
       "tmnxNatQryLsnSubWhereOutAddr": tmnxNatQryLsnSubWhereOutAddr,
       "tmnxNatQryLsnSubWhereInSubType": tmnxNatQryLsnSubWhereInSubType,
       "tmnxNatQryLsnSubWhereInRouter": tmnxNatQryLsnSubWhereInRouter,
       "tmnxNatQryLsnSubWhereInAddrType": tmnxNatQryLsnSubWhereInAddrType,
       "tmnxNatQryLsnSubWhereInAddr": tmnxNatQryLsnSubWhereInAddr,
       "tmnxNatQryLsnSubWhereInAddrPfxL": tmnxNatQryLsnSubWhereInAddrPfxL,
       "tmnxNatQryLsnSubWhereSubId": tmnxNatQryLsnSubWhereSubId,
       "tmnxNatQryLsnSubResTable": tmnxNatQryLsnSubResTable,
       "tmnxNatQryLsnSubResEntry": tmnxNatQryLsnSubResEntry,
       "tmnxNatQryLsnSubResId": tmnxNatQryLsnSubResId,
       "tmnxNatQryLsnSubResPolicy": tmnxNatQryLsnSubResPolicy,
       "tmnxNatQryLsnSubResIsaGrp": tmnxNatQryLsnSubResIsaGrp,
       "tmnxNatQryLsnSubResIsaMemberId": tmnxNatQryLsnSubResIsaMemberId,
       "tmnxNatQryLsnSubResOutVRtrID": tmnxNatQryLsnSubResOutVRtrID,
       "tmnxNatQryLsnSubResOutAddrType": tmnxNatQryLsnSubResOutAddrType,
       "tmnxNatQryLsnSubResOutAddr": tmnxNatQryLsnSubResOutAddr,
       "tmnxNatQryLsnSubResIdStr": tmnxNatQryLsnSubResIdStr,
       "tmnxNatQryLsnSubResInSubType": tmnxNatQryLsnSubResInSubType,
       "tmnxNatQryLsnSubResInRouter": tmnxNatQryLsnSubResInRouter,
       "tmnxNatQryLsnSubResInAddrType": tmnxNatQryLsnSubResInAddrType,
       "tmnxNatQryLsnSubResInAddr": tmnxNatQryLsnSubResInAddr,
       "tmnxNatQryLsnSubResInAddrPfxL": tmnxNatQryLsnSubResInAddrPfxL,
       "tmnxNatQryLsnSubResIcmpPortUsg": tmnxNatQryLsnSubResIcmpPortUsg,
       "tmnxNatQryLsnSubResIcmpPortUsgHi": tmnxNatQryLsnSubResIcmpPortUsgHi,
       "tmnxNatQryLsnSubResUdpPortUsg": tmnxNatQryLsnSubResUdpPortUsg,
       "tmnxNatQryLsnSubResUdpPortUsgHi": tmnxNatQryLsnSubResUdpPortUsgHi,
       "tmnxNatQryLsnSubResTcpPortUsg": tmnxNatQryLsnSubResTcpPortUsg,
       "tmnxNatQryLsnSubResTcpPortUsgHi": tmnxNatQryLsnSubResTcpPortUsgHi,
       "tmnxNatQryLsnSubResSessionUsg": tmnxNatQryLsnSubResSessionUsg,
       "tmnxNatQryLsnSubResSessionUsgHi": tmnxNatQryLsnSubResSessionUsgHi,
       "tmnxNatQryLsnSubResSessions": tmnxNatQryLsnSubResSessions,
       "tmnxNatQryLsnSubResSessionsPrio": tmnxNatQryLsnSubResSessionsPrio,
       "tmnxNatQryLsnSubResSessionsPeak": tmnxNatQryLsnSubResSessionsPeak,
       "tmnxNatIsaGrpTableLastCh": tmnxNatIsaGrpTableLastCh,
       "tmnxNatIsaMdaTableLastCh": tmnxNatIsaMdaTableLastCh,
       "tmnxNatIsaMdaStatTableLastCh": tmnxNatIsaMdaStatTableLastCh,
       "tmnxNatPlcyTableLastCh": tmnxNatPlcyTableLastCh,
       "tmnxNatVrtrTableLastCh": tmnxNatVrtrTableLastCh,
       "tmnxNatL2AwAddrTableLastCh": tmnxNatL2AwAddrTableLastCh,
       "tmnxNatPlTableLastCh": tmnxNatPlTableLastCh,
       "tmnxNatPlRangeTableLastCh": tmnxNatPlRangeTableLastCh,
       "tmnxNatDestTableLastCh": tmnxNatDestTableLastCh,
       "tmnxNatMapLsnHostTableLastCh": tmnxNatMapLsnHostTableLastCh,
       "tmnxNatMapTableLastCh": tmnxNatMapTableLastCh,
       "tmnxNatDsliteAddrTableLastCh": tmnxNatDsliteAddrTableLastCh,
       "tmnxNatApTableLastCh": tmnxNatApTableLastCh,
       "tmnxNatApServTableLastCh": tmnxNatApServTableLastCh,
       "tmnxNat64TableLastCh": tmnxNat64TableLastCh,
       "tmnxNatGrpCfgTableLastCh": tmnxNatGrpCfgTableLastCh,
       "tmnxNatSubIdTableLastCh": tmnxNatSubIdTableLastCh,
       "tmnxNatPcpPlcyTableLastCh": tmnxNatPcpPlcyTableLastCh,
       "tmnxNatPcpSrvTableLastCh": tmnxNatPcpSrvTableLastCh,
       "tmnxNatPcpSrvIfTableLastCh": tmnxNatPcpSrvIfTableLastCh,
       "tmnxNatDetPlcyTableLastCh": tmnxNatDetPlcyTableLastCh,
       "tmnxNatDetMapTableLastCh": tmnxNatDetMapTableLastCh,
       "tmnxNatResourceProblem": tmnxNatResourceProblem,
       "tmnxNatLsnSubscIdCount": tmnxNatLsnSubscIdCount,
       "tmnxNatQryLsnSubMaxQryId": tmnxNatQryLsnSubMaxQryId,
       "tmnxNatNotificationObjs": tmnxNatNotificationObjs,
       "tmnxNatNotifyDescription": tmnxNatNotifyDescription,
       "tmnxNatNotifyOutsideVRtrID": tmnxNatNotifyOutsideVRtrID,
       "tmnxNatNotifyInsideVRtrID": tmnxNatNotifyInsideVRtrID,
       "tmnxNatNotifyOutsideAddrType": tmnxNatNotifyOutsideAddrType,
       "tmnxNatNotifyOutsideAddr": tmnxNatNotifyOutsideAddr,
       "tmnxNatNotifyInsideAddrType": tmnxNatNotifyInsideAddrType,
       "tmnxNatNotifyInsideAddr": tmnxNatNotifyInsideAddr,
       "tmnxNatNotifyPort": tmnxNatNotifyPort,
       "tmnxNatNotifyPort2": tmnxNatNotifyPort2,
       "tmnxNatNotifyDateAndTime": tmnxNatNotifyDateAndTime,
       "tmnxNatNotifyTruthValue": tmnxNatNotifyTruthValue,
       "tmnxNatNotifyLsnSubId": tmnxNatNotifyLsnSubId,
       "tmnxNatNotifyL2AwSubIdent": tmnxNatNotifyL2AwSubIdent,
       "tmnxNatNotifyOutsideEndAddrType": tmnxNatNotifyOutsideEndAddrType,
       "tmnxNatNotifyOutsideEndAddr": tmnxNatNotifyOutsideEndAddr,
       "tmnxNatNotifyPlSeqNum": tmnxNatNotifyPlSeqNum,
       "tmnxNatNotifySubscriberType": tmnxNatNotifySubscriberType,
       "tmnxNatNotifyMdaChassisIndex": tmnxNatNotifyMdaChassisIndex,
       "tmnxNatNotifyMdaCardSlotNum": tmnxNatNotifyMdaCardSlotNum,
       "tmnxNatNotifyMdaSlotNum": tmnxNatNotifyMdaSlotNum,
       "tmnxNatNotifyCounter": tmnxNatNotifyCounter,
       "tmnxNatNotifyNumber": tmnxNatNotifyNumber,
       "tmnxNatNotifyInsideAddrPrefixLen": tmnxNatNotifyInsideAddrPrefixLen,
       "tmnxNatNotifyPrefix": tmnxNatNotifyPrefix,
       "tmnxNatNotifications": tmnxNatNotifications,
       "tmnxNatPlL2AwBlockUsageHigh": tmnxNatPlL2AwBlockUsageHigh,
       "tmnxNatIsaMemberSessionUsageHigh": tmnxNatIsaMemberSessionUsageHigh,
       "tmnxNatPlLsnMemberBlockUsageHigh": tmnxNatPlLsnMemberBlockUsageHigh,
       "tmnxNatLsnSubIcmpPortUsageHigh": tmnxNatLsnSubIcmpPortUsageHigh,
       "tmnxNatLsnSubUdpPortUsageHigh": tmnxNatLsnSubUdpPortUsageHigh,
       "tmnxNatLsnSubTcpPortUsageHigh": tmnxNatLsnSubTcpPortUsageHigh,
       "tmnxNatL2AwSubIcmpPortUsageHigh": tmnxNatL2AwSubIcmpPortUsageHigh,
       "tmnxNatL2AwSubUdpPortUsageHigh": tmnxNatL2AwSubUdpPortUsageHigh,
       "tmnxNatL2AwSubTcpPortUsageHigh": tmnxNatL2AwSubTcpPortUsageHigh,
       "tmnxNatL2AwSubSessionUsageHigh": tmnxNatL2AwSubSessionUsageHigh,
       "tmnxNatLsnSubSessionUsageHigh": tmnxNatLsnSubSessionUsageHigh,
       "tmnxNatPlBlockAllocationLsn": tmnxNatPlBlockAllocationLsn,
       "tmnxNatPlBlockAllocationL2Aw": tmnxNatPlBlockAllocationL2Aw,
       "tmnxNatResourceProblemDetected": tmnxNatResourceProblemDetected,
       "tmnxNatResourceProblemCause": tmnxNatResourceProblemCause,
       "tmnxNatPlAddrFree": tmnxNatPlAddrFree,
       "tmnxNatPlLsnRedActiveChanged": tmnxNatPlLsnRedActiveChanged,
       "tmnxNatPcpSrvStateChanged": tmnxNatPcpSrvStateChanged,
       "tmnxNatFwdEntryAdded": tmnxNatFwdEntryAdded,
       "tmnxNatMdaActive": tmnxNatMdaActive,
       "tmnxNatLsnSubBlksFree": tmnxNatLsnSubBlksFree,
       "tmnxNatDetPlcyChanged": tmnxNatDetPlcyChanged,
       "tmnxNatMdaDetectsLoadSharingErr": tmnxNatMdaDetectsLoadSharingErr,
       "tmnxNatIsaGrpOperStateChanged": tmnxNatIsaGrpOperStateChanged,
       "tmnxNatIsaGrpIsDegraded": tmnxNatIsaGrpIsDegraded,
       "tmnxNatLsnSubIcmpPortUsgHigh": tmnxNatLsnSubIcmpPortUsgHigh,
       "tmnxNatLsnSubUdpPortUsgHigh": tmnxNatLsnSubUdpPortUsgHigh,
       "tmnxNatLsnSubTcpPortUsgHigh": tmnxNatLsnSubTcpPortUsgHigh,
       "tmnxNatLsnSubSessionUsgHigh": tmnxNatLsnSubSessionUsgHigh,
       "tmnxNatInAddrPrefixBlksFree": tmnxNatInAddrPrefixBlksFree,
       "tmnxNatFwd2EntryAdded": tmnxNatFwd2EntryAdded}
)
