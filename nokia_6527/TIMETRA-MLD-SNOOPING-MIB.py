# SNMP MIB module (TIMETRA-MLD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MLD-SNOOPING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:36 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
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

(tmnxMcacLagPortsDown,
 tmnxMcacLevelId) = mibBuilder.importSymbols(
    "TIMETRA-MCAST-CAC-MIB",
    "tmnxMcacLagPortsDown",
    "tmnxMcacLevelId")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(sdpBindId,) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindId")

(SdpId,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId",
    "svcId")

(TItemDescription,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxMldGroupFilterMode,
 TmnxMldGroupType,
 TmnxMldVersion,
 TmnxPortID,
 TmnxServId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxMldGroupFilterMode",
    "TmnxMldGroupType",
    "TmnxMldVersion",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVcIdOrNone")


# MODULE-IDENTITY

timetraMldSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 45)
)
if mibBuilder.loadTexts:
    timetraMldSnoopingMIBModule.setRevisions(
        ("2008-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMldSnpgLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxMldSnoopingConformance_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingConformance = _TmnxMldSnoopingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45)
)
_TmnxMldSnoopingCompliances_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingCompliances = _TmnxMldSnoopingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1)
)
_TmnxMldSnoopingGroups_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingGroups = _TmnxMldSnoopingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2)
)
_TmnxMldSnoopingObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingObjs = _TmnxMldSnoopingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45)
)
_TmnxMldSnoopingTlsObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingTlsObjs = _TmnxMldSnoopingTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1)
)
_TlsMldSnpgConfigTableLastChange_Type = TimeStamp
_TlsMldSnpgConfigTableLastChange_Object = MibScalar
tlsMldSnpgConfigTableLastChange = _TlsMldSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 1),
    _TlsMldSnpgConfigTableLastChange_Type()
)
tlsMldSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgConfigTableLastChange.setStatus("current")
_TlsMldSnpgConfigTable_Object = MibTable
tlsMldSnpgConfigTable = _TlsMldSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2)
)
if mibBuilder.loadTexts:
    tlsMldSnpgConfigTable.setStatus("current")
_TlsMldSnpgConfigEntry_Object = MibTableRow
tlsMldSnpgConfigEntry = _TlsMldSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1)
)
tlsMldSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgConfigEntry.setStatus("current")
_TlsMldSnpgCfgLastChangeTime_Type = TimeStamp
_TlsMldSnpgCfgLastChangeTime_Object = MibTableColumn
tlsMldSnpgCfgLastChangeTime = _TlsMldSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 1),
    _TlsMldSnpgCfgLastChangeTime_Type()
)
tlsMldSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgLastChangeTime.setStatus("current")


class _TlsMldSnpgCfgAdminState_Type(TmnxAdminState):
    """Custom type tlsMldSnpgCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TlsMldSnpgCfgAdminState_Type.__name__ = "TmnxAdminState"
_TlsMldSnpgCfgAdminState_Object = MibTableColumn
tlsMldSnpgCfgAdminState = _TlsMldSnpgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 2),
    _TlsMldSnpgCfgAdminState_Type()
)
tlsMldSnpgCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgAdminState.setStatus("current")


class _TlsMldSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tlsMldSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlsMldSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TlsMldSnpgCfgGenQueryIntvl_Object = MibTableColumn
tlsMldSnpgCfgGenQueryIntvl = _TlsMldSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 3),
    _TlsMldSnpgCfgGenQueryIntvl_Type()
)
tlsMldSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TlsMldSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tlsMldSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TlsMldSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TlsMldSnpgCfgRobustCount_Object = MibTableColumn
tlsMldSnpgCfgRobustCount = _TlsMldSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 4),
    _TlsMldSnpgCfgRobustCount_Type()
)
tlsMldSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgRobustCount.setStatus("current")


class _TlsMldSnpgCfgReportSrcAddrType_Type(InetAddressType):
    """Custom type tlsMldSnpgCfgReportSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TlsMldSnpgCfgReportSrcAddrType_Type.__name__ = "InetAddressType"
_TlsMldSnpgCfgReportSrcAddrType_Object = MibTableColumn
tlsMldSnpgCfgReportSrcAddrType = _TlsMldSnpgCfgReportSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 5),
    _TlsMldSnpgCfgReportSrcAddrType_Type()
)
tlsMldSnpgCfgReportSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgReportSrcAddrType.setStatus("current")


class _TlsMldSnpgCfgReportSrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgCfgReportSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgCfgReportSrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgCfgReportSrcAddr_Object = MibTableColumn
tlsMldSnpgCfgReportSrcAddr = _TlsMldSnpgCfgReportSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 6),
    _TlsMldSnpgCfgReportSrcAddr_Type()
)
tlsMldSnpgCfgReportSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgReportSrcAddr.setStatus("current")


class _TlsMldSnpgCfgQuerySrcAddrType_Type(InetAddressType):
    """Custom type tlsMldSnpgCfgQuerySrcAddrType based on InetAddressType"""
    defaultValue = 0


_TlsMldSnpgCfgQuerySrcAddrType_Type.__name__ = "InetAddressType"
_TlsMldSnpgCfgQuerySrcAddrType_Object = MibTableColumn
tlsMldSnpgCfgQuerySrcAddrType = _TlsMldSnpgCfgQuerySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 7),
    _TlsMldSnpgCfgQuerySrcAddrType_Type()
)
tlsMldSnpgCfgQuerySrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgQuerySrcAddrType.setStatus("current")


class _TlsMldSnpgCfgQuerySrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgCfgQuerySrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgCfgQuerySrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgCfgQuerySrcAddr_Object = MibTableColumn
tlsMldSnpgCfgQuerySrcAddr = _TlsMldSnpgCfgQuerySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 8),
    _TlsMldSnpgCfgQuerySrcAddr_Type()
)
tlsMldSnpgCfgQuerySrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgQuerySrcAddr.setStatus("current")


class _TlsMldSnpgCfgMvrAdminState_Type(TmnxAdminState):
    """Custom type tlsMldSnpgCfgMvrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TlsMldSnpgCfgMvrAdminState_Type.__name__ = "TmnxAdminState"
_TlsMldSnpgCfgMvrAdminState_Object = MibTableColumn
tlsMldSnpgCfgMvrAdminState = _TlsMldSnpgCfgMvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 9),
    _TlsMldSnpgCfgMvrAdminState_Type()
)
tlsMldSnpgCfgMvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgMvrAdminState.setStatus("current")


class _TlsMldSnpgCfgMvrDescription_Type(TItemDescription):
    """Custom type tlsMldSnpgCfgMvrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TlsMldSnpgCfgMvrDescription_Type.__name__ = "TItemDescription"
_TlsMldSnpgCfgMvrDescription_Object = MibTableColumn
tlsMldSnpgCfgMvrDescription = _TlsMldSnpgCfgMvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 10),
    _TlsMldSnpgCfgMvrDescription_Type()
)
tlsMldSnpgCfgMvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgMvrDescription.setStatus("current")


class _TlsMldSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tlsMldSnpgCfgMvrPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TlsMldSnpgCfgMvrPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TlsMldSnpgCfgMvrPolicy_Object = MibTableColumn
tlsMldSnpgCfgMvrPolicy = _TlsMldSnpgCfgMvrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 11),
    _TlsMldSnpgCfgMvrPolicy_Type()
)
tlsMldSnpgCfgMvrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgMvrPolicy.setStatus("current")
_TlsMldSnpgQuerierTable_Object = MibTable
tlsMldSnpgQuerierTable = _TlsMldSnpgQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3)
)
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierTable.setStatus("current")
_TlsMldSnpgQuerierEntry_Object = MibTableRow
tlsMldSnpgQuerierEntry = _TlsMldSnpgQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1)
)
tlsMldSnpgQuerierEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierEntry.setStatus("current")
_TlsMldSnpgQuerierVersion_Type = TmnxMldVersion
_TlsMldSnpgQuerierVersion_Object = MibTableColumn
tlsMldSnpgQuerierVersion = _TlsMldSnpgQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 1),
    _TlsMldSnpgQuerierVersion_Type()
)
tlsMldSnpgQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVersion.setStatus("current")
_TlsMldSnpgQuerierAddressType_Type = InetAddressType
_TlsMldSnpgQuerierAddressType_Object = MibTableColumn
tlsMldSnpgQuerierAddressType = _TlsMldSnpgQuerierAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 2),
    _TlsMldSnpgQuerierAddressType_Type()
)
tlsMldSnpgQuerierAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierAddressType.setStatus("current")


class _TlsMldSnpgQuerierAddress_Type(InetAddress):
    """Custom type tlsMldSnpgQuerierAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgQuerierAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgQuerierAddress_Object = MibTableColumn
tlsMldSnpgQuerierAddress = _TlsMldSnpgQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 3),
    _TlsMldSnpgQuerierAddress_Type()
)
tlsMldSnpgQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierAddress.setStatus("current")
_TlsMldSnpgQuerierLocale_Type = TmnxMldSnpgLocation
_TlsMldSnpgQuerierLocale_Object = MibTableColumn
tlsMldSnpgQuerierLocale = _TlsMldSnpgQuerierLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 4),
    _TlsMldSnpgQuerierLocale_Type()
)
tlsMldSnpgQuerierLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierLocale.setStatus("current")
_TlsMldSnpgQuerierPortId_Type = TmnxPortID
_TlsMldSnpgQuerierPortId_Object = MibTableColumn
tlsMldSnpgQuerierPortId = _TlsMldSnpgQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 5),
    _TlsMldSnpgQuerierPortId_Type()
)
tlsMldSnpgQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierPortId.setStatus("current")
_TlsMldSnpgQuerierEncapValue_Type = TmnxEncapVal
_TlsMldSnpgQuerierEncapValue_Object = MibTableColumn
tlsMldSnpgQuerierEncapValue = _TlsMldSnpgQuerierEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 6),
    _TlsMldSnpgQuerierEncapValue_Type()
)
tlsMldSnpgQuerierEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierEncapValue.setStatus("current")
_TlsMldSnpgQuerierSdpId_Type = SdpId
_TlsMldSnpgQuerierSdpId_Object = MibTableColumn
tlsMldSnpgQuerierSdpId = _TlsMldSnpgQuerierSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 7),
    _TlsMldSnpgQuerierSdpId_Type()
)
tlsMldSnpgQuerierSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierSdpId.setStatus("current")
_TlsMldSnpgQuerierVcId_Type = TmnxVcIdOrNone
_TlsMldSnpgQuerierVcId_Object = MibTableColumn
tlsMldSnpgQuerierVcId = _TlsMldSnpgQuerierVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 8),
    _TlsMldSnpgQuerierVcId_Type()
)
tlsMldSnpgQuerierVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVcId.setStatus("current")
_TlsMldSnpgQuerierUpTime_Type = TimeTicks
_TlsMldSnpgQuerierUpTime_Object = MibTableColumn
tlsMldSnpgQuerierUpTime = _TlsMldSnpgQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 9),
    _TlsMldSnpgQuerierUpTime_Type()
)
tlsMldSnpgQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierUpTime.setStatus("current")
_TlsMldSnpgQuerierExpiryTime_Type = Unsigned32
_TlsMldSnpgQuerierExpiryTime_Object = MibTableColumn
tlsMldSnpgQuerierExpiryTime = _TlsMldSnpgQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 10),
    _TlsMldSnpgQuerierExpiryTime_Type()
)
tlsMldSnpgQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierExpiryTime.setUnits("seconds")
_TlsMldSnpgQuerierGenQueryIntvl_Type = Unsigned32
_TlsMldSnpgQuerierGenQueryIntvl_Object = MibTableColumn
tlsMldSnpgQuerierGenQueryIntvl = _TlsMldSnpgQuerierGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 11),
    _TlsMldSnpgQuerierGenQueryIntvl_Type()
)
tlsMldSnpgQuerierGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenQueryIntvl.setUnits("seconds")
_TlsMldSnpgQuerierGenRespIntvl_Type = Unsigned32
_TlsMldSnpgQuerierGenRespIntvl_Object = MibTableColumn
tlsMldSnpgQuerierGenRespIntvl = _TlsMldSnpgQuerierGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 12),
    _TlsMldSnpgQuerierGenRespIntvl_Type()
)
tlsMldSnpgQuerierGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenRespIntvl.setUnits("deci-seconds")
_TlsMldSnpgQuerierRobustCount_Type = Unsigned32
_TlsMldSnpgQuerierRobustCount_Object = MibTableColumn
tlsMldSnpgQuerierRobustCount = _TlsMldSnpgQuerierRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 13),
    _TlsMldSnpgQuerierRobustCount_Type()
)
tlsMldSnpgQuerierRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierRobustCount.setStatus("current")
_TlsMldSnpgProxyGroupTable_Object = MibTable
tlsMldSnpgProxyGroupTable = _TlsMldSnpgProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4)
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupTable.setStatus("current")
_TlsMldSnpgProxyGroupEntry_Object = MibTableRow
tlsMldSnpgProxyGroupEntry = _TlsMldSnpgProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1)
)
tlsMldSnpgProxyGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddress"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupEntry.setStatus("current")
_TlsMldSnpgProxyGroupAddressType_Type = InetAddressType
_TlsMldSnpgProxyGroupAddressType_Object = MibTableColumn
tlsMldSnpgProxyGroupAddressType = _TlsMldSnpgProxyGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 1),
    _TlsMldSnpgProxyGroupAddressType_Type()
)
tlsMldSnpgProxyGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupAddressType.setStatus("current")


class _TlsMldSnpgProxyGroupAddress_Type(InetAddress):
    """Custom type tlsMldSnpgProxyGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgProxyGroupAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgProxyGroupAddress_Object = MibTableColumn
tlsMldSnpgProxyGroupAddress = _TlsMldSnpgProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 2),
    _TlsMldSnpgProxyGroupAddress_Type()
)
tlsMldSnpgProxyGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupAddress.setStatus("current")
_TlsMldSnpgProxyGroupFilterMode_Type = TmnxMldGroupFilterMode
_TlsMldSnpgProxyGroupFilterMode_Object = MibTableColumn
tlsMldSnpgProxyGroupFilterMode = _TlsMldSnpgProxyGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 3),
    _TlsMldSnpgProxyGroupFilterMode_Type()
)
tlsMldSnpgProxyGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupFilterMode.setStatus("current")
_TlsMldSnpgProxyGroupUpTime_Type = TimeTicks
_TlsMldSnpgProxyGroupUpTime_Object = MibTableColumn
tlsMldSnpgProxyGroupUpTime = _TlsMldSnpgProxyGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 4),
    _TlsMldSnpgProxyGroupUpTime_Type()
)
tlsMldSnpgProxyGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupUpTime.setStatus("current")
_TlsMldSnpgProxyGrpSrcTable_Object = MibTable
tlsMldSnpgProxyGrpSrcTable = _TlsMldSnpgProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5)
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcTable.setStatus("current")
_TlsMldSnpgProxyGrpSrcEntry_Object = MibTableRow
tlsMldSnpgProxyGrpSrcEntry = _TlsMldSnpgProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1)
)
tlsMldSnpgProxyGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGrpSrcAddrTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcEntry.setStatus("current")
_TlsMldSnpgProxyGrpSrcAddrTp_Type = InetAddressType
_TlsMldSnpgProxyGrpSrcAddrTp_Object = MibTableColumn
tlsMldSnpgProxyGrpSrcAddrTp = _TlsMldSnpgProxyGrpSrcAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1, 1),
    _TlsMldSnpgProxyGrpSrcAddrTp_Type()
)
tlsMldSnpgProxyGrpSrcAddrTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcAddrTp.setStatus("current")


class _TlsMldSnpgProxyGrpSrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgProxyGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgProxyGrpSrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgProxyGrpSrcAddr_Object = MibTableColumn
tlsMldSnpgProxyGrpSrcAddr = _TlsMldSnpgProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1, 2),
    _TlsMldSnpgProxyGrpSrcAddr_Type()
)
tlsMldSnpgProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcAddr.setStatus("current")
_TlsMldSnpgProxyGrpSrcUpTime_Type = TimeTicks
_TlsMldSnpgProxyGrpSrcUpTime_Object = MibTableColumn
tlsMldSnpgProxyGrpSrcUpTime = _TlsMldSnpgProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1, 3),
    _TlsMldSnpgProxyGrpSrcUpTime_Type()
)
tlsMldSnpgProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcUpTime.setStatus("current")
_TlsMldSnpgMRouterTable_Object = MibTable
tlsMldSnpgMRouterTable = _TlsMldSnpgMRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6)
)
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterTable.setStatus("current")
_TlsMldSnpgMRouterEntry_Object = MibTableRow
tlsMldSnpgMRouterEntry = _TlsMldSnpgMRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1)
)
tlsMldSnpgMRouterEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterAddress"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterEntry.setStatus("current")
_TlsMldSnpgMRouterAddressType_Type = InetAddressType
_TlsMldSnpgMRouterAddressType_Object = MibTableColumn
tlsMldSnpgMRouterAddressType = _TlsMldSnpgMRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 1),
    _TlsMldSnpgMRouterAddressType_Type()
)
tlsMldSnpgMRouterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterAddressType.setStatus("current")


class _TlsMldSnpgMRouterAddress_Type(InetAddress):
    """Custom type tlsMldSnpgMRouterAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgMRouterAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgMRouterAddress_Object = MibTableColumn
tlsMldSnpgMRouterAddress = _TlsMldSnpgMRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 2),
    _TlsMldSnpgMRouterAddress_Type()
)
tlsMldSnpgMRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterAddress.setStatus("current")
_TlsMldSnpgMRouterLocale_Type = TmnxMldSnpgLocation
_TlsMldSnpgMRouterLocale_Object = MibTableColumn
tlsMldSnpgMRouterLocale = _TlsMldSnpgMRouterLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 3),
    _TlsMldSnpgMRouterLocale_Type()
)
tlsMldSnpgMRouterLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterLocale.setStatus("current")
_TlsMldSnpgMRouterPortId_Type = TmnxPortID
_TlsMldSnpgMRouterPortId_Object = MibTableColumn
tlsMldSnpgMRouterPortId = _TlsMldSnpgMRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 4),
    _TlsMldSnpgMRouterPortId_Type()
)
tlsMldSnpgMRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterPortId.setStatus("current")
_TlsMldSnpgMRouterEncapValue_Type = TmnxEncapVal
_TlsMldSnpgMRouterEncapValue_Object = MibTableColumn
tlsMldSnpgMRouterEncapValue = _TlsMldSnpgMRouterEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 5),
    _TlsMldSnpgMRouterEncapValue_Type()
)
tlsMldSnpgMRouterEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterEncapValue.setStatus("current")
_TlsMldSnpgMRouterSdpId_Type = SdpId
_TlsMldSnpgMRouterSdpId_Object = MibTableColumn
tlsMldSnpgMRouterSdpId = _TlsMldSnpgMRouterSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 6),
    _TlsMldSnpgMRouterSdpId_Type()
)
tlsMldSnpgMRouterSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterSdpId.setStatus("current")
_TlsMldSnpgMRouterVcId_Type = TmnxVcIdOrNone
_TlsMldSnpgMRouterVcId_Object = MibTableColumn
tlsMldSnpgMRouterVcId = _TlsMldSnpgMRouterVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 7),
    _TlsMldSnpgMRouterVcId_Type()
)
tlsMldSnpgMRouterVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVcId.setStatus("current")
_TlsMldSnpgMRouterVersion_Type = TmnxMldVersion
_TlsMldSnpgMRouterVersion_Object = MibTableColumn
tlsMldSnpgMRouterVersion = _TlsMldSnpgMRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 8),
    _TlsMldSnpgMRouterVersion_Type()
)
tlsMldSnpgMRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVersion.setStatus("current")
_TlsMldSnpgMRouterExpiryTime_Type = Unsigned32
_TlsMldSnpgMRouterExpiryTime_Object = MibTableColumn
tlsMldSnpgMRouterExpiryTime = _TlsMldSnpgMRouterExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 9),
    _TlsMldSnpgMRouterExpiryTime_Type()
)
tlsMldSnpgMRouterExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterExpiryTime.setUnits("seconds")
_TlsMldSnpgMRouterUpTime_Type = TimeTicks
_TlsMldSnpgMRouterUpTime_Object = MibTableColumn
tlsMldSnpgMRouterUpTime = _TlsMldSnpgMRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 10),
    _TlsMldSnpgMRouterUpTime_Type()
)
tlsMldSnpgMRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterUpTime.setStatus("current")
_TlsMldSnpgMRouterGenQueryIntvl_Type = Unsigned32
_TlsMldSnpgMRouterGenQueryIntvl_Object = MibTableColumn
tlsMldSnpgMRouterGenQueryIntvl = _TlsMldSnpgMRouterGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 11),
    _TlsMldSnpgMRouterGenQueryIntvl_Type()
)
tlsMldSnpgMRouterGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenQueryIntvl.setUnits("seconds")
_TlsMldSnpgMRouterGenRespIntvl_Type = Unsigned32
_TlsMldSnpgMRouterGenRespIntvl_Object = MibTableColumn
tlsMldSnpgMRouterGenRespIntvl = _TlsMldSnpgMRouterGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 12),
    _TlsMldSnpgMRouterGenRespIntvl_Type()
)
tlsMldSnpgMRouterGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenRespIntvl.setUnits("deci-seconds")
_TlsMldSnpgMRouterRobustCount_Type = Unsigned32
_TlsMldSnpgMRouterRobustCount_Object = MibTableColumn
tlsMldSnpgMRouterRobustCount = _TlsMldSnpgMRouterRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 13),
    _TlsMldSnpgMRouterRobustCount_Type()
)
tlsMldSnpgMRouterRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterRobustCount.setStatus("current")
_TmnxMldSnoopingSapObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSapObjs = _TmnxMldSnoopingSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2)
)
_SapMldSnpgConfigTableLastChange_Type = TimeStamp
_SapMldSnpgConfigTableLastChange_Object = MibScalar
sapMldSnpgConfigTableLastChange = _SapMldSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 1),
    _SapMldSnpgConfigTableLastChange_Type()
)
sapMldSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgConfigTableLastChange.setStatus("current")
_SapMldSnpgConfigTable_Object = MibTable
sapMldSnpgConfigTable = _SapMldSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2)
)
if mibBuilder.loadTexts:
    sapMldSnpgConfigTable.setStatus("current")
_SapMldSnpgConfigEntry_Object = MibTableRow
sapMldSnpgConfigEntry = _SapMldSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1)
)
sapMldSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapMldSnpgConfigEntry.setStatus("current")
_SapMldSnpgCfgLastChangeTime_Type = TimeStamp
_SapMldSnpgCfgLastChangeTime_Object = MibTableColumn
sapMldSnpgCfgLastChangeTime = _SapMldSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 1),
    _SapMldSnpgCfgLastChangeTime_Type()
)
sapMldSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgLastChangeTime.setStatus("current")


class _SapMldSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapMldSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapMldSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapMldSnpgCfgImportPlcy_Object = MibTableColumn
sapMldSnpgCfgImportPlcy = _SapMldSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 2),
    _SapMldSnpgCfgImportPlcy_Type()
)
sapMldSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgImportPlcy.setStatus("current")


class _SapMldSnpgCfgFastLeave_Type(TmnxAdminState):
    """Custom type sapMldSnpgCfgFastLeave based on TmnxAdminState"""
    defaultValue = 3


_SapMldSnpgCfgFastLeave_Type.__name__ = "TmnxAdminState"
_SapMldSnpgCfgFastLeave_Object = MibTableColumn
sapMldSnpgCfgFastLeave = _SapMldSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 3),
    _SapMldSnpgCfgFastLeave_Type()
)
sapMldSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgFastLeave.setStatus("current")


class _SapMldSnpgCfgMRouter_Type(TruthValue):
    """Custom type sapMldSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SapMldSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SapMldSnpgCfgMRouter_Object = MibTableColumn
sapMldSnpgCfgMRouter = _SapMldSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 4),
    _SapMldSnpgCfgMRouter_Type()
)
sapMldSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMRouter.setStatus("current")


class _SapMldSnpgCfgSendQueries_Type(TmnxAdminState):
    """Custom type sapMldSnpgCfgSendQueries based on TmnxAdminState"""
    defaultValue = 3


_SapMldSnpgCfgSendQueries_Type.__name__ = "TmnxAdminState"
_SapMldSnpgCfgSendQueries_Object = MibTableColumn
sapMldSnpgCfgSendQueries = _SapMldSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 5),
    _SapMldSnpgCfgSendQueries_Type()
)
sapMldSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgSendQueries.setStatus("current")


class _SapMldSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sapMldSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SapMldSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgGenQueryIntvl_Object = MibTableColumn
sapMldSnpgCfgGenQueryIntvl = _SapMldSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 6),
    _SapMldSnpgCfgGenQueryIntvl_Type()
)
sapMldSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SapMldSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sapMldSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SapMldSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgQueryRespIntvl_Object = MibTableColumn
sapMldSnpgCfgQueryRespIntvl = _SapMldSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 7),
    _SapMldSnpgCfgQueryRespIntvl_Type()
)
sapMldSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SapMldSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sapMldSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SapMldSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgRobustCount_Object = MibTableColumn
sapMldSnpgCfgRobustCount = _SapMldSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 8),
    _SapMldSnpgCfgRobustCount_Type()
)
sapMldSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgRobustCount.setStatus("current")


class _SapMldSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sapMldSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SapMldSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgLastMembIntvl_Object = MibTableColumn
sapMldSnpgCfgLastMembIntvl = _SapMldSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 9),
    _SapMldSnpgCfgLastMembIntvl_Type()
)
sapMldSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _SapMldSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sapMldSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SapMldSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SapMldSnpgCfgMaxNbrGrps_Object = MibTableColumn
sapMldSnpgCfgMaxNbrGrps = _SapMldSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 10),
    _SapMldSnpgCfgMaxNbrGrps_Type()
)
sapMldSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMaxNbrGrps.setStatus("current")


class _SapMldSnpgCfgMvrFromVplsId_Type(TmnxServId):
    """Custom type sapMldSnpgCfgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_SapMldSnpgCfgMvrFromVplsId_Type.__name__ = "TmnxServId"
_SapMldSnpgCfgMvrFromVplsId_Object = MibTableColumn
sapMldSnpgCfgMvrFromVplsId = _SapMldSnpgCfgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 11),
    _SapMldSnpgCfgMvrFromVplsId_Type()
)
sapMldSnpgCfgMvrFromVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMvrFromVplsId.setStatus("current")


class _SapMldSnpgCfgMvrToSapPortId_Type(TmnxPortID):
    """Custom type sapMldSnpgCfgMvrToSapPortId based on TmnxPortID"""
    defaultValue = 0


_SapMldSnpgCfgMvrToSapPortId_Type.__name__ = "TmnxPortID"
_SapMldSnpgCfgMvrToSapPortId_Object = MibTableColumn
sapMldSnpgCfgMvrToSapPortId = _SapMldSnpgCfgMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 12),
    _SapMldSnpgCfgMvrToSapPortId_Type()
)
sapMldSnpgCfgMvrToSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMvrToSapPortId.setStatus("current")


class _SapMldSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):
    """Custom type sapMldSnpgCfgMvrToSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_SapMldSnpgCfgMvrToSapEncapVal_Type.__name__ = "TmnxEncapVal"
_SapMldSnpgCfgMvrToSapEncapVal_Object = MibTableColumn
sapMldSnpgCfgMvrToSapEncapVal = _SapMldSnpgCfgMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 13),
    _SapMldSnpgCfgMvrToSapEncapVal_Type()
)
sapMldSnpgCfgMvrToSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMvrToSapEncapVal.setStatus("current")


class _SapMldSnpgCfgVersion_Type(TmnxMldVersion):
    """Custom type sapMldSnpgCfgVersion based on TmnxMldVersion"""
    defaultValue = 2


_SapMldSnpgCfgVersion_Type.__name__ = "TmnxMldVersion"
_SapMldSnpgCfgVersion_Object = MibTableColumn
sapMldSnpgCfgVersion = _SapMldSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 14),
    _SapMldSnpgCfgVersion_Type()
)
sapMldSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgVersion.setStatus("current")


class _SapMldSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sapMldSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SapMldSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SapMldSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sapMldSnpgCfgDisRtrAlertChk = _SapMldSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 15),
    _SapMldSnpgCfgDisRtrAlertChk_Type()
)
sapMldSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgDisRtrAlertChk.setStatus("current")


class _SapMldSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapMldSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapMldSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapMldSnpgCfgMcacPolicyName_Object = MibTableColumn
sapMldSnpgCfgMcacPolicyName = _SapMldSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 16),
    _SapMldSnpgCfgMcacPolicyName_Type()
)
sapMldSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacPolicyName.setStatus("current")


class _SapMldSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sapMldSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SapMldSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SapMldSnpgCfgMcacUnconstBW_Object = MibTableColumn
sapMldSnpgCfgMcacUnconstBW = _SapMldSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 17),
    _SapMldSnpgCfgMcacUnconstBW_Type()
)
sapMldSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacUnconstBW.setUnits("kbps")


class _SapMldSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sapMldSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SapMldSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SapMldSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sapMldSnpgCfgMcacPrRsvMndBW = _SapMldSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 18),
    _SapMldSnpgCfgMcacPrRsvMndBW_Type()
)
sapMldSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacPrRsvMndBW.setUnits("kbps")


class _SapMldSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):
    """Custom type sapMldSnpgCfgMcacConstAdmSt based on TmnxAdminState"""
    defaultValue = 2


_SapMldSnpgCfgMcacConstAdmSt_Type.__name__ = "TmnxAdminState"
_SapMldSnpgCfgMcacConstAdmSt_Object = MibTableColumn
sapMldSnpgCfgMcacConstAdmSt = _SapMldSnpgCfgMcacConstAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 19),
    _SapMldSnpgCfgMcacConstAdmSt_Type()
)
sapMldSnpgCfgMcacConstAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacConstAdmSt.setStatus("current")
_SapMldSnpgCfgMcacinUseMandBw_Type = Unsigned32
_SapMldSnpgCfgMcacinUseMandBw_Object = MibTableColumn
sapMldSnpgCfgMcacinUseMandBw = _SapMldSnpgCfgMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 20),
    _SapMldSnpgCfgMcacinUseMandBw_Type()
)
sapMldSnpgCfgMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseMandBw.setUnits("kbps")
_SapMldSnpgCfgMcacinUseOpnlBw_Type = Unsigned32
_SapMldSnpgCfgMcacinUseOpnlBw_Object = MibTableColumn
sapMldSnpgCfgMcacinUseOpnlBw = _SapMldSnpgCfgMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 21),
    _SapMldSnpgCfgMcacinUseOpnlBw_Type()
)
sapMldSnpgCfgMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseOpnlBw.setUnits("kbps")
_SapMldSnpgCfgMcacAvailMandBw_Type = Unsigned32
_SapMldSnpgCfgMcacAvailMandBw_Object = MibTableColumn
sapMldSnpgCfgMcacAvailMandBw = _SapMldSnpgCfgMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 22),
    _SapMldSnpgCfgMcacAvailMandBw_Type()
)
sapMldSnpgCfgMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailMandBw.setUnits("kbps")
_SapMldSnpgCfgMcacAvailOpnlBw_Type = Unsigned32
_SapMldSnpgCfgMcacAvailOpnlBw_Object = MibTableColumn
sapMldSnpgCfgMcacAvailOpnlBw = _SapMldSnpgCfgMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 23),
    _SapMldSnpgCfgMcacAvailOpnlBw_Type()
)
sapMldSnpgCfgMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailOpnlBw.setUnits("kbps")
_SapMldSnpgCfgMcacValInTrans_Type = TruthValue
_SapMldSnpgCfgMcacValInTrans_Object = MibTableColumn
sapMldSnpgCfgMcacValInTrans = _SapMldSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 24),
    _SapMldSnpgCfgMcacValInTrans_Type()
)
sapMldSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacValInTrans.setStatus("current")


class _SapMldSnpgCfgMcacUseLagPortWt_Type(TruthValue):
    """Custom type sapMldSnpgCfgMcacUseLagPortWt based on TruthValue"""
    defaultValue = 2


_SapMldSnpgCfgMcacUseLagPortWt_Type.__name__ = "TruthValue"
_SapMldSnpgCfgMcacUseLagPortWt_Object = MibTableColumn
sapMldSnpgCfgMcacUseLagPortWt = _SapMldSnpgCfgMcacUseLagPortWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 25),
    _SapMldSnpgCfgMcacUseLagPortWt_Type()
)
sapMldSnpgCfgMcacUseLagPortWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacUseLagPortWt.setStatus("current")
_SapMldSnpgGroupTable_Object = MibTable
sapMldSnpgGroupTable = _SapMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3)
)
if mibBuilder.loadTexts:
    sapMldSnpgGroupTable.setStatus("current")
_SapMldSnpgGroupEntry_Object = MibTableRow
sapMldSnpgGroupEntry = _SapMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1)
)
sapMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sapMldSnpgGroupEntry.setStatus("current")
_SapMldSnpgGrpAddressType_Type = InetAddressType
_SapMldSnpgGrpAddressType_Object = MibTableColumn
sapMldSnpgGrpAddressType = _SapMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 1),
    _SapMldSnpgGrpAddressType_Type()
)
sapMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpAddressType.setStatus("current")


class _SapMldSnpgGrpAddress_Type(InetAddress):
    """Custom type sapMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_SapMldSnpgGrpAddress_Object = MibTableColumn
sapMldSnpgGrpAddress = _SapMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 2),
    _SapMldSnpgGrpAddress_Type()
)
sapMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpAddress.setStatus("current")
_SapMldSnpgGrpType_Type = TmnxMldGroupType
_SapMldSnpgGrpType_Object = MibTableColumn
sapMldSnpgGrpType = _SapMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 3),
    _SapMldSnpgGrpType_Type()
)
sapMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpType.setStatus("current")
_SapMldSnpgGrpFilterMode_Type = TmnxMldGroupFilterMode
_SapMldSnpgGrpFilterMode_Object = MibTableColumn
sapMldSnpgGrpFilterMode = _SapMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 4),
    _SapMldSnpgGrpFilterMode_Type()
)
sapMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpFilterMode.setStatus("current")
_SapMldSnpgGrpUpTime_Type = TimeTicks
_SapMldSnpgGrpUpTime_Object = MibTableColumn
sapMldSnpgGrpUpTime = _SapMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 5),
    _SapMldSnpgGrpUpTime_Type()
)
sapMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpUpTime.setStatus("current")
_SapMldSnpgGrpExpiryTime_Type = Unsigned32
_SapMldSnpgGrpExpiryTime_Object = MibTableColumn
sapMldSnpgGrpExpiryTime = _SapMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 6),
    _SapMldSnpgGrpExpiryTime_Type()
)
sapMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgGrpExpiryTime.setUnits("seconds")
_SapMldSnpgGrpCompatMode_Type = Unsigned32
_SapMldSnpgGrpCompatMode_Object = MibTableColumn
sapMldSnpgGrpCompatMode = _SapMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 7),
    _SapMldSnpgGrpCompatMode_Type()
)
sapMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpCompatMode.setStatus("current")
_SapMldSnpgGrpV1HostExpTime_Type = Unsigned32
_SapMldSnpgGrpV1HostExpTime_Object = MibTableColumn
sapMldSnpgGrpV1HostExpTime = _SapMldSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 8),
    _SapMldSnpgGrpV1HostExpTime_Type()
)
sapMldSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgGrpV1HostExpTime.setUnits("seconds")
_SapMldSnpgGrpMvrFromVplsId_Type = TmnxServId
_SapMldSnpgGrpMvrFromVplsId_Object = MibTableColumn
sapMldSnpgGrpMvrFromVplsId = _SapMldSnpgGrpMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 9),
    _SapMldSnpgGrpMvrFromVplsId_Type()
)
sapMldSnpgGrpMvrFromVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpMvrFromVplsId.setStatus("current")
_SapMldSnpgGrpMvrToSapPortId_Type = TmnxPortID
_SapMldSnpgGrpMvrToSapPortId_Object = MibTableColumn
sapMldSnpgGrpMvrToSapPortId = _SapMldSnpgGrpMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 10),
    _SapMldSnpgGrpMvrToSapPortId_Type()
)
sapMldSnpgGrpMvrToSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpMvrToSapPortId.setStatus("current")
_SapMldSnpgGrpMvrToSapEncapVal_Type = TmnxEncapVal
_SapMldSnpgGrpMvrToSapEncapVal_Object = MibTableColumn
sapMldSnpgGrpMvrToSapEncapVal = _SapMldSnpgGrpMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 11),
    _SapMldSnpgGrpMvrToSapEncapVal_Type()
)
sapMldSnpgGrpMvrToSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpMvrToSapEncapVal.setStatus("current")
_SapMldSnpgGrpSrcTable_Object = MibTable
sapMldSnpgGrpSrcTable = _SapMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4)
)
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcTable.setStatus("current")
_SapMldSnpgGrpSrcEntry_Object = MibTableRow
sapMldSnpgGrpSrcEntry = _SapMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1)
)
sapMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcEntry.setStatus("current")
_SapMldSnpgGrpSrcAddrType_Type = InetAddressType
_SapMldSnpgGrpSrcAddrType_Object = MibTableColumn
sapMldSnpgGrpSrcAddrType = _SapMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 1),
    _SapMldSnpgGrpSrcAddrType_Type()
)
sapMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcAddrType.setStatus("current")


class _SapMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type sapMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_SapMldSnpgGrpSrcAddr_Object = MibTableColumn
sapMldSnpgGrpSrcAddr = _SapMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 2),
    _SapMldSnpgGrpSrcAddr_Type()
)
sapMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcAddr.setStatus("current")
_SapMldSnpgGrpSrcType_Type = TmnxMldGroupType
_SapMldSnpgGrpSrcType_Object = MibTableColumn
sapMldSnpgGrpSrcType = _SapMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 3),
    _SapMldSnpgGrpSrcType_Type()
)
sapMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcType.setStatus("current")
_SapMldSnpgGrpSrcUpTime_Type = TimeTicks
_SapMldSnpgGrpSrcUpTime_Object = MibTableColumn
sapMldSnpgGrpSrcUpTime = _SapMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 4),
    _SapMldSnpgGrpSrcUpTime_Type()
)
sapMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcUpTime.setStatus("current")
_SapMldSnpgGrpSrcExpiryTime_Type = Unsigned32
_SapMldSnpgGrpSrcExpiryTime_Object = MibTableColumn
sapMldSnpgGrpSrcExpiryTime = _SapMldSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 5),
    _SapMldSnpgGrpSrcExpiryTime_Type()
)
sapMldSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcExpiryTime.setUnits("seconds")
_SapMldSnpgStaticGrpSrcTableLstCh_Type = TimeStamp
_SapMldSnpgStaticGrpSrcTableLstCh_Object = MibScalar
sapMldSnpgStaticGrpSrcTableLstCh = _SapMldSnpgStaticGrpSrcTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 5),
    _SapMldSnpgStaticGrpSrcTableLstCh_Type()
)
sapMldSnpgStaticGrpSrcTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgStaticGrpSrcTableLstCh.setStatus("current")
_SapMldSnpgStaticGrpSrcTable_Object = MibTable
sapMldSnpgStaticGrpSrcTable = _SapMldSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6)
)
if mibBuilder.loadTexts:
    sapMldSnpgStaticGrpSrcTable.setStatus("current")
_SapMldSnpgStaticGrpSrcEntry_Object = MibTableRow
sapMldSnpgStaticGrpSrcEntry = _SapMldSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1)
)
sapMldSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticGroupAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticGroupAddr"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticSourceAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sapMldSnpgStaticGrpSrcEntry.setStatus("current")
_SapMldSnpgStaticGroupAddrType_Type = InetAddressType
_SapMldSnpgStaticGroupAddrType_Object = MibTableColumn
sapMldSnpgStaticGroupAddrType = _SapMldSnpgStaticGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 1),
    _SapMldSnpgStaticGroupAddrType_Type()
)
sapMldSnpgStaticGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticGroupAddrType.setStatus("current")


class _SapMldSnpgStaticGroupAddr_Type(InetAddress):
    """Custom type sapMldSnpgStaticGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgStaticGroupAddr_Type.__name__ = "InetAddress"
_SapMldSnpgStaticGroupAddr_Object = MibTableColumn
sapMldSnpgStaticGroupAddr = _SapMldSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 2),
    _SapMldSnpgStaticGroupAddr_Type()
)
sapMldSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticGroupAddr.setStatus("current")
_SapMldSnpgStaticSourceAddrType_Type = InetAddressType
_SapMldSnpgStaticSourceAddrType_Object = MibTableColumn
sapMldSnpgStaticSourceAddrType = _SapMldSnpgStaticSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 3),
    _SapMldSnpgStaticSourceAddrType_Type()
)
sapMldSnpgStaticSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticSourceAddrType.setStatus("current")


class _SapMldSnpgStaticSourceAddr_Type(InetAddress):
    """Custom type sapMldSnpgStaticSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgStaticSourceAddr_Type.__name__ = "InetAddress"
_SapMldSnpgStaticSourceAddr_Object = MibTableColumn
sapMldSnpgStaticSourceAddr = _SapMldSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 4),
    _SapMldSnpgStaticSourceAddr_Type()
)
sapMldSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticSourceAddr.setStatus("current")
_SapMldSnpgStaticRowstatus_Type = RowStatus
_SapMldSnpgStaticRowstatus_Object = MibTableColumn
sapMldSnpgStaticRowstatus = _SapMldSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 5),
    _SapMldSnpgStaticRowstatus_Type()
)
sapMldSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgStaticRowstatus.setStatus("current")
_SapMldSnpgStaticLastChangeTime_Type = TimeStamp
_SapMldSnpgStaticLastChangeTime_Object = MibTableColumn
sapMldSnpgStaticLastChangeTime = _SapMldSnpgStaticLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 6),
    _SapMldSnpgStaticLastChangeTime_Type()
)
sapMldSnpgStaticLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgStaticLastChangeTime.setStatus("current")
_SapMldSnpgStatsTable_Object = MibTable
sapMldSnpgStatsTable = _SapMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7)
)
if mibBuilder.loadTexts:
    sapMldSnpgStatsTable.setStatus("current")
_SapMldSnpgStatsEntry_Object = MibTableRow
sapMldSnpgStatsEntry = _SapMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1)
)
sapMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapMldSnpgStatsEntry.setStatus("current")
_SapMldSnpgTxGenQueries_Type = Counter32
_SapMldSnpgTxGenQueries_Object = MibTableColumn
sapMldSnpgTxGenQueries = _SapMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 1),
    _SapMldSnpgTxGenQueries_Type()
)
sapMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxGenQueries.setStatus("current")
_SapMldSnpgTxGrpSpecQueries_Type = Counter32
_SapMldSnpgTxGrpSpecQueries_Object = MibTableColumn
sapMldSnpgTxGrpSpecQueries = _SapMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 2),
    _SapMldSnpgTxGrpSpecQueries_Type()
)
sapMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxGrpSpecQueries.setStatus("current")
_SapMldSnpgTxSrcSpecQueries_Type = Counter32
_SapMldSnpgTxSrcSpecQueries_Object = MibTableColumn
sapMldSnpgTxSrcSpecQueries = _SapMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 3),
    _SapMldSnpgTxSrcSpecQueries_Type()
)
sapMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxSrcSpecQueries.setStatus("current")
_SapMldSnpgTxV1Reports_Type = Counter32
_SapMldSnpgTxV1Reports_Object = MibTableColumn
sapMldSnpgTxV1Reports = _SapMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 4),
    _SapMldSnpgTxV1Reports_Type()
)
sapMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxV1Reports.setStatus("current")
_SapMldSnpgTxV2Reports_Type = Counter32
_SapMldSnpgTxV2Reports_Object = MibTableColumn
sapMldSnpgTxV2Reports = _SapMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 5),
    _SapMldSnpgTxV2Reports_Type()
)
sapMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxV2Reports.setStatus("current")
_SapMldSnpgTxV1Leaves_Type = Counter32
_SapMldSnpgTxV1Leaves_Object = MibTableColumn
sapMldSnpgTxV1Leaves = _SapMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 6),
    _SapMldSnpgTxV1Leaves_Type()
)
sapMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxV1Leaves.setStatus("current")
_SapMldSnpgRxGenQueries_Type = Counter32
_SapMldSnpgRxGenQueries_Object = MibTableColumn
sapMldSnpgRxGenQueries = _SapMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 7),
    _SapMldSnpgRxGenQueries_Type()
)
sapMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxGenQueries.setStatus("current")
_SapMldSnpgRxGrpSpecQueries_Type = Counter32
_SapMldSnpgRxGrpSpecQueries_Object = MibTableColumn
sapMldSnpgRxGrpSpecQueries = _SapMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 8),
    _SapMldSnpgRxGrpSpecQueries_Type()
)
sapMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxGrpSpecQueries.setStatus("current")
_SapMldSnpgRxSrcSpecQueries_Type = Counter32
_SapMldSnpgRxSrcSpecQueries_Object = MibTableColumn
sapMldSnpgRxSrcSpecQueries = _SapMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 9),
    _SapMldSnpgRxSrcSpecQueries_Type()
)
sapMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxSrcSpecQueries.setStatus("current")
_SapMldSnpgRxV1Reports_Type = Counter32
_SapMldSnpgRxV1Reports_Object = MibTableColumn
sapMldSnpgRxV1Reports = _SapMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 10),
    _SapMldSnpgRxV1Reports_Type()
)
sapMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxV1Reports.setStatus("current")
_SapMldSnpgRxV2Reports_Type = Counter32
_SapMldSnpgRxV2Reports_Object = MibTableColumn
sapMldSnpgRxV2Reports = _SapMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 11),
    _SapMldSnpgRxV2Reports_Type()
)
sapMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxV2Reports.setStatus("current")
_SapMldSnpgRxV1Leaves_Type = Counter32
_SapMldSnpgRxV1Leaves_Object = MibTableColumn
sapMldSnpgRxV1Leaves = _SapMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 12),
    _SapMldSnpgRxV1Leaves_Type()
)
sapMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxV1Leaves.setStatus("current")
_SapMldSnpgRxUnknownType_Type = Counter32
_SapMldSnpgRxUnknownType_Object = MibTableColumn
sapMldSnpgRxUnknownType = _SapMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 13),
    _SapMldSnpgRxUnknownType_Type()
)
sapMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxUnknownType.setStatus("current")
_SapMldSnpgFwdGenQueries_Type = Counter32
_SapMldSnpgFwdGenQueries_Object = MibTableColumn
sapMldSnpgFwdGenQueries = _SapMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 14),
    _SapMldSnpgFwdGenQueries_Type()
)
sapMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdGenQueries.setStatus("current")
_SapMldSnpgFwdGrpSpecQueries_Type = Counter32
_SapMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
sapMldSnpgFwdGrpSpecQueries = _SapMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 15),
    _SapMldSnpgFwdGrpSpecQueries_Type()
)
sapMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdGrpSpecQueries.setStatus("current")
_SapMldSnpgFwdSrcSpecQueries_Type = Counter32
_SapMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
sapMldSnpgFwdSrcSpecQueries = _SapMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 16),
    _SapMldSnpgFwdSrcSpecQueries_Type()
)
sapMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdSrcSpecQueries.setStatus("current")
_SapMldSnpgFwdV1Reports_Type = Counter32
_SapMldSnpgFwdV1Reports_Object = MibTableColumn
sapMldSnpgFwdV1Reports = _SapMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 17),
    _SapMldSnpgFwdV1Reports_Type()
)
sapMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdV1Reports.setStatus("current")
_SapMldSnpgFwdV2Reports_Type = Counter32
_SapMldSnpgFwdV2Reports_Object = MibTableColumn
sapMldSnpgFwdV2Reports = _SapMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 18),
    _SapMldSnpgFwdV2Reports_Type()
)
sapMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdV2Reports.setStatus("current")
_SapMldSnpgFwdV1Leaves_Type = Counter32
_SapMldSnpgFwdV1Leaves_Object = MibTableColumn
sapMldSnpgFwdV1Leaves = _SapMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 19),
    _SapMldSnpgFwdV1Leaves_Type()
)
sapMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdV1Leaves.setStatus("current")
_SapMldSnpgFwdUnknownType_Type = Counter32
_SapMldSnpgFwdUnknownType_Object = MibTableColumn
sapMldSnpgFwdUnknownType = _SapMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 20),
    _SapMldSnpgFwdUnknownType_Type()
)
sapMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdUnknownType.setStatus("current")
_SapMldSnpgRxBadLenPkts_Type = Counter32
_SapMldSnpgRxBadLenPkts_Object = MibTableColumn
sapMldSnpgRxBadLenPkts = _SapMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 21),
    _SapMldSnpgRxBadLenPkts_Type()
)
sapMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxBadLenPkts.setStatus("current")
_SapMldSnpgRxBadMldChksmPkts_Type = Counter32
_SapMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
sapMldSnpgRxBadMldChksmPkts = _SapMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 22),
    _SapMldSnpgRxBadMldChksmPkts_Type()
)
sapMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxBadMldChksmPkts.setStatus("current")
_SapMldSnpgRxBadEncodedPkts_Type = Counter32
_SapMldSnpgRxBadEncodedPkts_Object = MibTableColumn
sapMldSnpgRxBadEncodedPkts = _SapMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 23),
    _SapMldSnpgRxBadEncodedPkts_Type()
)
sapMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxBadEncodedPkts.setStatus("current")
_SapMldSnpgRxNoRtrAlertPkts_Type = Counter32
_SapMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sapMldSnpgRxNoRtrAlertPkts = _SapMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 24),
    _SapMldSnpgRxNoRtrAlertPkts_Type()
)
sapMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxNoRtrAlertPkts.setStatus("current")
_SapMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_SapMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sapMldSnpgRxZeroSrcAdrPkts = _SapMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 25),
    _SapMldSnpgRxZeroSrcAdrPkts_Type()
)
sapMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_SapMldSnpgSendQueryCfgDrops_Type = Counter32
_SapMldSnpgSendQueryCfgDrops_Object = MibTableColumn
sapMldSnpgSendQueryCfgDrops = _SapMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 26),
    _SapMldSnpgSendQueryCfgDrops_Type()
)
sapMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgSendQueryCfgDrops.setStatus("current")
_SapMldSnpgImportPolicyDrops_Type = Counter32
_SapMldSnpgImportPolicyDrops_Object = MibTableColumn
sapMldSnpgImportPolicyDrops = _SapMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 27),
    _SapMldSnpgImportPolicyDrops_Type()
)
sapMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgImportPolicyDrops.setStatus("current")
_SapMldSnpgMaxNumGroupsDrops_Type = Counter32
_SapMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
sapMldSnpgMaxNumGroupsDrops = _SapMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 28),
    _SapMldSnpgMaxNumGroupsDrops_Type()
)
sapMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMaxNumGroupsDrops.setStatus("current")
_SapMldSnpgMvrFromVplsCfgDrops_Type = Counter32
_SapMldSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
sapMldSnpgMvrFromVplsCfgDrops = _SapMldSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 29),
    _SapMldSnpgMvrFromVplsCfgDrops_Type()
)
sapMldSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMvrFromVplsCfgDrops.setStatus("current")
_SapMldSnpgMvrToSapCfgDrops_Type = Counter32
_SapMldSnpgMvrToSapCfgDrops_Object = MibTableColumn
sapMldSnpgMvrToSapCfgDrops = _SapMldSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 30),
    _SapMldSnpgMvrToSapCfgDrops_Type()
)
sapMldSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMvrToSapCfgDrops.setStatus("current")
_SapMldSnpgRxWrongVersionPkts_Type = Counter32
_SapMldSnpgRxWrongVersionPkts_Object = MibTableColumn
sapMldSnpgRxWrongVersionPkts = _SapMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 31),
    _SapMldSnpgRxWrongVersionPkts_Type()
)
sapMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxWrongVersionPkts.setStatus("current")
_SapMldSnpgMcsFailures_Type = Counter32
_SapMldSnpgMcsFailures_Object = MibTableColumn
sapMldSnpgMcsFailures = _SapMldSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 32),
    _SapMldSnpgMcsFailures_Type()
)
sapMldSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMcsFailures.setStatus("current")
_SapMldSnpgRxLocalScopePkts_Type = Counter32
_SapMldSnpgRxLocalScopePkts_Object = MibTableColumn
sapMldSnpgRxLocalScopePkts = _SapMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 33),
    _SapMldSnpgRxLocalScopePkts_Type()
)
sapMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxLocalScopePkts.setStatus("current")
_SapMldSnpgRxRsvdScopePkts_Type = Counter32
_SapMldSnpgRxRsvdScopePkts_Object = MibTableColumn
sapMldSnpgRxRsvdScopePkts = _SapMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 34),
    _SapMldSnpgRxRsvdScopePkts_Type()
)
sapMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxRsvdScopePkts.setStatus("current")
_SapMldSnpgMcacPolicyDrops_Type = Counter32
_SapMldSnpgMcacPolicyDrops_Object = MibTableColumn
sapMldSnpgMcacPolicyDrops = _SapMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 35),
    _SapMldSnpgMcacPolicyDrops_Type()
)
sapMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMcacPolicyDrops.setStatus("current")
_SapMldSnpgMcacLevelTable_Object = MibTable
sapMldSnpgMcacLevelTable = _SapMldSnpgMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8)
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLevelTable.setStatus("current")
_SapMldSnpgMcacLevelEntry_Object = MibTableRow
sapMldSnpgMcacLevelEntry = _SapMldSnpgMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1)
)
sapMldSnpgMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLevelEntry.setStatus("current")
_SapMldSnpgCfgMcacLevelRowStat_Type = RowStatus
_SapMldSnpgCfgMcacLevelRowStat_Object = MibTableColumn
sapMldSnpgCfgMcacLevelRowStat = _SapMldSnpgCfgMcacLevelRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1, 1),
    _SapMldSnpgCfgMcacLevelRowStat_Type()
)
sapMldSnpgCfgMcacLevelRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelRowStat.setStatus("current")


class _SapMldSnpgCfgMcacLevelBW_Type(Unsigned32):
    """Custom type sapMldSnpgCfgMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_SapMldSnpgCfgMcacLevelBW_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgMcacLevelBW_Object = MibTableColumn
sapMldSnpgCfgMcacLevelBW = _SapMldSnpgCfgMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1, 2),
    _SapMldSnpgCfgMcacLevelBW_Type()
)
sapMldSnpgCfgMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelBW.setUnits("kbps")
_SapMldSnpgCfgMcacLevelLastChngT_Type = TimeStamp
_SapMldSnpgCfgMcacLevelLastChngT_Object = MibTableColumn
sapMldSnpgCfgMcacLevelLastChngT = _SapMldSnpgCfgMcacLevelLastChngT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1, 3),
    _SapMldSnpgCfgMcacLevelLastChngT_Type()
)
sapMldSnpgCfgMcacLevelLastChngT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelLastChngT.setStatus("current")
_SapMldSnpgMcacLagTable_Object = MibTable
sapMldSnpgMcacLagTable = _SapMldSnpgMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9)
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLagTable.setStatus("current")
_SapMldSnpgMcacLagEntry_Object = MibTableRow
sapMldSnpgMcacLagEntry = _SapMldSnpgMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1)
)
sapMldSnpgMcacLagEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLagEntry.setStatus("current")
_SapMldSnpgCfgMcacLagRowStat_Type = RowStatus
_SapMldSnpgCfgMcacLagRowStat_Object = MibTableColumn
sapMldSnpgCfgMcacLagRowStat = _SapMldSnpgCfgMcacLagRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1, 1),
    _SapMldSnpgCfgMcacLagRowStat_Type()
)
sapMldSnpgCfgMcacLagRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLagRowStat.setStatus("current")


class _SapMldSnpgCfgMcacLagLevel_Type(Unsigned32):
    """Custom type sapMldSnpgCfgMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SapMldSnpgCfgMcacLagLevel_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgMcacLagLevel_Object = MibTableColumn
sapMldSnpgCfgMcacLagLevel = _SapMldSnpgCfgMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1, 2),
    _SapMldSnpgCfgMcacLagLevel_Type()
)
sapMldSnpgCfgMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLagLevel.setStatus("current")
_SapMldSnpgCfgMcacLagLastChangeT_Type = TimeStamp
_SapMldSnpgCfgMcacLagLastChangeT_Object = MibTableColumn
sapMldSnpgCfgMcacLagLastChangeT = _SapMldSnpgCfgMcacLagLastChangeT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1, 3),
    _SapMldSnpgCfgMcacLagLastChangeT_Type()
)
sapMldSnpgCfgMcacLagLastChangeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLagLastChangeT.setStatus("current")
_TmnxMldSnoopingSdpBindObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSdpBindObjs = _TmnxMldSnoopingSdpBindObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3)
)
_SdpBindMldSnpgConfigTableLastCh_Type = TimeStamp
_SdpBindMldSnpgConfigTableLastCh_Object = MibScalar
sdpBindMldSnpgConfigTableLastCh = _SdpBindMldSnpgConfigTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 1),
    _SdpBindMldSnpgConfigTableLastCh_Type()
)
sdpBindMldSnpgConfigTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMldSnpgConfigTableLastCh.setStatus("current")
_SdpBindMldSnpgConfigTable_Object = MibTable
sdpBindMldSnpgConfigTable = _SdpBindMldSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgConfigTable.setStatus("current")
_SdpBindMldSnpgConfigEntry_Object = MibTableRow
sdpBindMldSnpgConfigEntry = _SdpBindMldSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1)
)
sdpBindMldSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgConfigEntry.setStatus("current")
_SdpBndMldSnpgCfgLastChangeTime_Type = TimeStamp
_SdpBndMldSnpgCfgLastChangeTime_Object = MibTableColumn
sdpBndMldSnpgCfgLastChangeTime = _SdpBndMldSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 1),
    _SdpBndMldSnpgCfgLastChangeTime_Type()
)
sdpBndMldSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgLastChangeTime.setStatus("current")


class _SdpBndMldSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndMldSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndMldSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndMldSnpgCfgImportPlcy_Object = MibTableColumn
sdpBndMldSnpgCfgImportPlcy = _SdpBndMldSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 2),
    _SdpBndMldSnpgCfgImportPlcy_Type()
)
sdpBndMldSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgImportPlcy.setStatus("current")


class _SdpBndMldSnpgCfgFastLeave_Type(TmnxAdminState):
    """Custom type sdpBndMldSnpgCfgFastLeave based on TmnxAdminState"""
    defaultValue = 3


_SdpBndMldSnpgCfgFastLeave_Type.__name__ = "TmnxAdminState"
_SdpBndMldSnpgCfgFastLeave_Object = MibTableColumn
sdpBndMldSnpgCfgFastLeave = _SdpBndMldSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 3),
    _SdpBndMldSnpgCfgFastLeave_Type()
)
sdpBndMldSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgFastLeave.setStatus("current")


class _SdpBndMldSnpgCfgMRouter_Type(TruthValue):
    """Custom type sdpBndMldSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SdpBndMldSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SdpBndMldSnpgCfgMRouter_Object = MibTableColumn
sdpBndMldSnpgCfgMRouter = _SdpBndMldSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 4),
    _SdpBndMldSnpgCfgMRouter_Type()
)
sdpBndMldSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMRouter.setStatus("current")


class _SdpBndMldSnpgCfgSendQueries_Type(TmnxAdminState):
    """Custom type sdpBndMldSnpgCfgSendQueries based on TmnxAdminState"""
    defaultValue = 3


_SdpBndMldSnpgCfgSendQueries_Type.__name__ = "TmnxAdminState"
_SdpBndMldSnpgCfgSendQueries_Object = MibTableColumn
sdpBndMldSnpgCfgSendQueries = _SdpBndMldSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 5),
    _SdpBndMldSnpgCfgSendQueries_Type()
)
sdpBndMldSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgSendQueries.setStatus("current")


class _SdpBndMldSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SdpBndMldSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgGenQueryIntvl_Object = MibTableColumn
sdpBndMldSnpgCfgGenQueryIntvl = _SdpBndMldSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 6),
    _SdpBndMldSnpgCfgGenQueryIntvl_Type()
)
sdpBndMldSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SdpBndMldSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SdpBndMldSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgQueryRespIntvl_Object = MibTableColumn
sdpBndMldSnpgCfgQueryRespIntvl = _SdpBndMldSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 7),
    _SdpBndMldSnpgCfgQueryRespIntvl_Type()
)
sdpBndMldSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SdpBndMldSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SdpBndMldSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgRobustCount_Object = MibTableColumn
sdpBndMldSnpgCfgRobustCount = _SdpBndMldSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 8),
    _SdpBndMldSnpgCfgRobustCount_Type()
)
sdpBndMldSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgRobustCount.setStatus("current")


class _SdpBndMldSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SdpBndMldSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgLastMembIntvl_Object = MibTableColumn
sdpBndMldSnpgCfgLastMembIntvl = _SdpBndMldSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 9),
    _SdpBndMldSnpgCfgLastMembIntvl_Type()
)
sdpBndMldSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _SdpBndMldSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sdpBndMldSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SdpBndMldSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SdpBndMldSnpgCfgMaxNbrGrps_Object = MibTableColumn
sdpBndMldSnpgCfgMaxNbrGrps = _SdpBndMldSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 10),
    _SdpBndMldSnpgCfgMaxNbrGrps_Type()
)
sdpBndMldSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMaxNbrGrps.setStatus("current")


class _SdpBndMldSnpgCfgVersion_Type(TmnxMldVersion):
    """Custom type sdpBndMldSnpgCfgVersion based on TmnxMldVersion"""
    defaultValue = 2


_SdpBndMldSnpgCfgVersion_Type.__name__ = "TmnxMldVersion"
_SdpBndMldSnpgCfgVersion_Object = MibTableColumn
sdpBndMldSnpgCfgVersion = _SdpBndMldSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 11),
    _SdpBndMldSnpgCfgVersion_Type()
)
sdpBndMldSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgVersion.setStatus("current")


class _SdpBndMldSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sdpBndMldSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SdpBndMldSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SdpBndMldSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sdpBndMldSnpgCfgDisRtrAlertChk = _SdpBndMldSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 12),
    _SdpBndMldSnpgCfgDisRtrAlertChk_Type()
)
sdpBndMldSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgDisRtrAlertChk.setStatus("current")


class _SdpBndMldSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndMldSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndMldSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndMldSnpgCfgMcacPolicyName_Object = MibTableColumn
sdpBndMldSnpgCfgMcacPolicyName = _SdpBndMldSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 13),
    _SdpBndMldSnpgCfgMcacPolicyName_Type()
)
sdpBndMldSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacPolicyName.setStatus("current")


class _SdpBndMldSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sdpBndMldSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndMldSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SdpBndMldSnpgCfgMcacUnconstBW_Object = MibTableColumn
sdpBndMldSnpgCfgMcacUnconstBW = _SdpBndMldSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 14),
    _SdpBndMldSnpgCfgMcacUnconstBW_Type()
)
sdpBndMldSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacUnconstBW.setUnits("kbps")


class _SdpBndMldSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sdpBndMldSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndMldSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SdpBndMldSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sdpBndMldSnpgCfgMcacPrRsvMndBW = _SdpBndMldSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 15),
    _SdpBndMldSnpgCfgMcacPrRsvMndBW_Type()
)
sdpBndMldSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacPrRsvMndBW.setUnits("kbps")
_SdpBndMldSnpgCfgMcacinUseMndBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacinUseMndBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacinUseMndBw = _SdpBndMldSnpgCfgMcacinUseMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 16),
    _SdpBndMldSnpgCfgMcacinUseMndBw_Type()
)
sdpBndMldSnpgCfgMcacinUseMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseMndBw.setUnits("kbps")
_SdpBndMldSnpgCfgMcacinUseOplBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacinUseOplBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacinUseOplBw = _SdpBndMldSnpgCfgMcacinUseOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 17),
    _SdpBndMldSnpgCfgMcacinUseOplBw_Type()
)
sdpBndMldSnpgCfgMcacinUseOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseOplBw.setUnits("kbps")
_SdpBndMldSnpgCfgMcacAvailMndBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacAvailMndBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacAvailMndBw = _SdpBndMldSnpgCfgMcacAvailMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 18),
    _SdpBndMldSnpgCfgMcacAvailMndBw_Type()
)
sdpBndMldSnpgCfgMcacAvailMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailMndBw.setUnits("kbps")
_SdpBndMldSnpgCfgMcacAvailOplBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacAvailOplBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacAvailOplBw = _SdpBndMldSnpgCfgMcacAvailOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 19),
    _SdpBndMldSnpgCfgMcacAvailOplBw_Type()
)
sdpBndMldSnpgCfgMcacAvailOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailOplBw.setUnits("kbps")
_SdpBndMldSnpgCfgMcacValInTrans_Type = TruthValue
_SdpBndMldSnpgCfgMcacValInTrans_Object = MibTableColumn
sdpBndMldSnpgCfgMcacValInTrans = _SdpBndMldSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 20),
    _SdpBndMldSnpgCfgMcacValInTrans_Type()
)
sdpBndMldSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacValInTrans.setStatus("current")
_SdpBindMldSnpgGroupTable_Object = MibTable
sdpBindMldSnpgGroupTable = _SdpBindMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGroupTable.setStatus("current")
_SdpBindMldSnpgGroupEntry_Object = MibTableRow
sdpBindMldSnpgGroupEntry = _SdpBindMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1)
)
sdpBindMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGroupEntry.setStatus("current")
_SdpBndMldSnpgGrpAddressType_Type = InetAddressType
_SdpBndMldSnpgGrpAddressType_Object = MibTableColumn
sdpBndMldSnpgGrpAddressType = _SdpBndMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 1),
    _SdpBndMldSnpgGrpAddressType_Type()
)
sdpBndMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpAddressType.setStatus("current")


class _SdpBndMldSnpgGrpAddress_Type(InetAddress):
    """Custom type sdpBndMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_SdpBndMldSnpgGrpAddress_Object = MibTableColumn
sdpBndMldSnpgGrpAddress = _SdpBndMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 2),
    _SdpBndMldSnpgGrpAddress_Type()
)
sdpBndMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpAddress.setStatus("current")
_SdpBndMldSnpgGrpType_Type = TmnxMldGroupType
_SdpBndMldSnpgGrpType_Object = MibTableColumn
sdpBndMldSnpgGrpType = _SdpBndMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 3),
    _SdpBndMldSnpgGrpType_Type()
)
sdpBndMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpType.setStatus("current")
_SdpBndMldSnpgGrpFilterMode_Type = TmnxMldGroupFilterMode
_SdpBndMldSnpgGrpFilterMode_Object = MibTableColumn
sdpBndMldSnpgGrpFilterMode = _SdpBndMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 4),
    _SdpBndMldSnpgGrpFilterMode_Type()
)
sdpBndMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpFilterMode.setStatus("current")
_SdpBndMldSnpgGrpUpTime_Type = TimeTicks
_SdpBndMldSnpgGrpUpTime_Object = MibTableColumn
sdpBndMldSnpgGrpUpTime = _SdpBndMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 5),
    _SdpBndMldSnpgGrpUpTime_Type()
)
sdpBndMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpUpTime.setStatus("current")
_SdpBndMldSnpgGrpExpiryTime_Type = Unsigned32
_SdpBndMldSnpgGrpExpiryTime_Object = MibTableColumn
sdpBndMldSnpgGrpExpiryTime = _SdpBndMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 6),
    _SdpBndMldSnpgGrpExpiryTime_Type()
)
sdpBndMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpExpiryTime.setUnits("seconds")
_SdpBndMldSnpgGrpCompatMode_Type = Unsigned32
_SdpBndMldSnpgGrpCompatMode_Object = MibTableColumn
sdpBndMldSnpgGrpCompatMode = _SdpBndMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 7),
    _SdpBndMldSnpgGrpCompatMode_Type()
)
sdpBndMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpCompatMode.setStatus("current")
_SdpBndMldSnpgGrpV1HostExpTime_Type = Unsigned32
_SdpBndMldSnpgGrpV1HostExpTime_Object = MibTableColumn
sdpBndMldSnpgGrpV1HostExpTime = _SdpBndMldSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 8),
    _SdpBndMldSnpgGrpV1HostExpTime_Type()
)
sdpBndMldSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpV1HostExpTime.setUnits("seconds")
_SdpBindMldSnpgGrpSrcTable_Object = MibTable
sdpBindMldSnpgGrpSrcTable = _SdpBindMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGrpSrcTable.setStatus("current")
_SdpBindMldSnpgGrpSrcEntry_Object = MibTableRow
sdpBindMldSnpgGrpSrcEntry = _SdpBindMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1)
)
sdpBindMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGrpSrcEntry.setStatus("current")
_SdpBndMldSnpgGrpSrcAddrType_Type = InetAddressType
_SdpBndMldSnpgGrpSrcAddrType_Object = MibTableColumn
sdpBndMldSnpgGrpSrcAddrType = _SdpBndMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 1),
    _SdpBndMldSnpgGrpSrcAddrType_Type()
)
sdpBndMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcAddrType.setStatus("current")


class _SdpBndMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type sdpBndMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_SdpBndMldSnpgGrpSrcAddr_Object = MibTableColumn
sdpBndMldSnpgGrpSrcAddr = _SdpBndMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 2),
    _SdpBndMldSnpgGrpSrcAddr_Type()
)
sdpBndMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcAddr.setStatus("current")
_SdpBndMldSnpgGrpSrcType_Type = TmnxMldGroupType
_SdpBndMldSnpgGrpSrcType_Object = MibTableColumn
sdpBndMldSnpgGrpSrcType = _SdpBndMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 3),
    _SdpBndMldSnpgGrpSrcType_Type()
)
sdpBndMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcType.setStatus("current")
_SdpBndMldSnpgGrpSrcUpTime_Type = TimeTicks
_SdpBndMldSnpgGrpSrcUpTime_Object = MibTableColumn
sdpBndMldSnpgGrpSrcUpTime = _SdpBndMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 4),
    _SdpBndMldSnpgGrpSrcUpTime_Type()
)
sdpBndMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcUpTime.setStatus("current")
_SdpBndMldSnpgGrpSrcExpiryTime_Type = Unsigned32
_SdpBndMldSnpgGrpSrcExpiryTime_Object = MibTableColumn
sdpBndMldSnpgGrpSrcExpiryTime = _SdpBndMldSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 5),
    _SdpBndMldSnpgGrpSrcExpiryTime_Type()
)
sdpBndMldSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcExpiryTime.setUnits("seconds")
_SdpBindMldSnpgStatGrpSrcTblLstCh_Type = TimeStamp
_SdpBindMldSnpgStatGrpSrcTblLstCh_Object = MibScalar
sdpBindMldSnpgStatGrpSrcTblLstCh = _SdpBindMldSnpgStatGrpSrcTblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 5),
    _SdpBindMldSnpgStatGrpSrcTblLstCh_Type()
)
sdpBindMldSnpgStatGrpSrcTblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatGrpSrcTblLstCh.setStatus("current")
_SdpBindMldSnpgStatGrpSrcTable_Object = MibTable
sdpBindMldSnpgStatGrpSrcTable = _SdpBindMldSnpgStatGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatGrpSrcTable.setStatus("current")
_SdpBindMldSnpgStatGrpSrcEntry_Object = MibTableRow
sdpBindMldSnpgStatGrpSrcEntry = _SdpBindMldSnpgStatGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1)
)
sdpBindMldSnpgStatGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticGroupAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticGroupAddr"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticSourceAddrTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatGrpSrcEntry.setStatus("current")
_SdpBndMldSnpgStaticGroupAddrType_Type = InetAddressType
_SdpBndMldSnpgStaticGroupAddrType_Object = MibTableColumn
sdpBndMldSnpgStaticGroupAddrType = _SdpBndMldSnpgStaticGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 1),
    _SdpBndMldSnpgStaticGroupAddrType_Type()
)
sdpBndMldSnpgStaticGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticGroupAddrType.setStatus("current")


class _SdpBndMldSnpgStaticGroupAddr_Type(InetAddress):
    """Custom type sdpBndMldSnpgStaticGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgStaticGroupAddr_Type.__name__ = "InetAddress"
_SdpBndMldSnpgStaticGroupAddr_Object = MibTableColumn
sdpBndMldSnpgStaticGroupAddr = _SdpBndMldSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 2),
    _SdpBndMldSnpgStaticGroupAddr_Type()
)
sdpBndMldSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticGroupAddr.setStatus("current")
_SdpBndMldSnpgStaticSourceAddrTp_Type = InetAddressType
_SdpBndMldSnpgStaticSourceAddrTp_Object = MibTableColumn
sdpBndMldSnpgStaticSourceAddrTp = _SdpBndMldSnpgStaticSourceAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 3),
    _SdpBndMldSnpgStaticSourceAddrTp_Type()
)
sdpBndMldSnpgStaticSourceAddrTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticSourceAddrTp.setStatus("current")


class _SdpBndMldSnpgStaticSourceAddr_Type(InetAddress):
    """Custom type sdpBndMldSnpgStaticSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgStaticSourceAddr_Type.__name__ = "InetAddress"
_SdpBndMldSnpgStaticSourceAddr_Object = MibTableColumn
sdpBndMldSnpgStaticSourceAddr = _SdpBndMldSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 4),
    _SdpBndMldSnpgStaticSourceAddr_Type()
)
sdpBndMldSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticSourceAddr.setStatus("current")
_SdpBndMldSnpgStaticRowstatus_Type = RowStatus
_SdpBndMldSnpgStaticRowstatus_Object = MibTableColumn
sdpBndMldSnpgStaticRowstatus = _SdpBndMldSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 5),
    _SdpBndMldSnpgStaticRowstatus_Type()
)
sdpBndMldSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticRowstatus.setStatus("current")
_SdpBndMldSnpgStaticLastChange_Type = TimeStamp
_SdpBndMldSnpgStaticLastChange_Object = MibTableColumn
sdpBndMldSnpgStaticLastChange = _SdpBndMldSnpgStaticLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 6),
    _SdpBndMldSnpgStaticLastChange_Type()
)
sdpBndMldSnpgStaticLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticLastChange.setStatus("current")
_SdpBindMldSnpgStatsTable_Object = MibTable
sdpBindMldSnpgStatsTable = _SdpBindMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatsTable.setStatus("current")
_SdpBindMldSnpgStatsEntry_Object = MibTableRow
sdpBindMldSnpgStatsEntry = _SdpBindMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1)
)
sdpBindMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatsEntry.setStatus("current")
_SdpBndMldSnpgTxGenQueries_Type = Counter32
_SdpBndMldSnpgTxGenQueries_Object = MibTableColumn
sdpBndMldSnpgTxGenQueries = _SdpBndMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 1),
    _SdpBndMldSnpgTxGenQueries_Type()
)
sdpBndMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxGenQueries.setStatus("current")
_SdpBndMldSnpgTxGrpSpecQueries_Type = Counter32
_SdpBndMldSnpgTxGrpSpecQueries_Object = MibTableColumn
sdpBndMldSnpgTxGrpSpecQueries = _SdpBndMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 2),
    _SdpBndMldSnpgTxGrpSpecQueries_Type()
)
sdpBndMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxGrpSpecQueries.setStatus("current")
_SdpBndMldSnpgTxSrcSpecQueries_Type = Counter32
_SdpBndMldSnpgTxSrcSpecQueries_Object = MibTableColumn
sdpBndMldSnpgTxSrcSpecQueries = _SdpBndMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 3),
    _SdpBndMldSnpgTxSrcSpecQueries_Type()
)
sdpBndMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxSrcSpecQueries.setStatus("current")
_SdpBndMldSnpgTxV1Reports_Type = Counter32
_SdpBndMldSnpgTxV1Reports_Object = MibTableColumn
sdpBndMldSnpgTxV1Reports = _SdpBndMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 4),
    _SdpBndMldSnpgTxV1Reports_Type()
)
sdpBndMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxV1Reports.setStatus("current")
_SdpBndMldSnpgTxV2Reports_Type = Counter32
_SdpBndMldSnpgTxV2Reports_Object = MibTableColumn
sdpBndMldSnpgTxV2Reports = _SdpBndMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 5),
    _SdpBndMldSnpgTxV2Reports_Type()
)
sdpBndMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxV2Reports.setStatus("current")
_SdpBndMldSnpgTxV1Leaves_Type = Counter32
_SdpBndMldSnpgTxV1Leaves_Object = MibTableColumn
sdpBndMldSnpgTxV1Leaves = _SdpBndMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 6),
    _SdpBndMldSnpgTxV1Leaves_Type()
)
sdpBndMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxV1Leaves.setStatus("current")
_SdpBndMldSnpgRxGenQueries_Type = Counter32
_SdpBndMldSnpgRxGenQueries_Object = MibTableColumn
sdpBndMldSnpgRxGenQueries = _SdpBndMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 7),
    _SdpBndMldSnpgRxGenQueries_Type()
)
sdpBndMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxGenQueries.setStatus("current")
_SdpBndMldSnpgRxGrpSpecQueries_Type = Counter32
_SdpBndMldSnpgRxGrpSpecQueries_Object = MibTableColumn
sdpBndMldSnpgRxGrpSpecQueries = _SdpBndMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 8),
    _SdpBndMldSnpgRxGrpSpecQueries_Type()
)
sdpBndMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxGrpSpecQueries.setStatus("current")
_SdpBndMldSnpgRxSrcSpecQueries_Type = Counter32
_SdpBndMldSnpgRxSrcSpecQueries_Object = MibTableColumn
sdpBndMldSnpgRxSrcSpecQueries = _SdpBndMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 9),
    _SdpBndMldSnpgRxSrcSpecQueries_Type()
)
sdpBndMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxSrcSpecQueries.setStatus("current")
_SdpBndMldSnpgRxV1Reports_Type = Counter32
_SdpBndMldSnpgRxV1Reports_Object = MibTableColumn
sdpBndMldSnpgRxV1Reports = _SdpBndMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 10),
    _SdpBndMldSnpgRxV1Reports_Type()
)
sdpBndMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxV1Reports.setStatus("current")
_SdpBndMldSnpgRxV2Reports_Type = Counter32
_SdpBndMldSnpgRxV2Reports_Object = MibTableColumn
sdpBndMldSnpgRxV2Reports = _SdpBndMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 11),
    _SdpBndMldSnpgRxV2Reports_Type()
)
sdpBndMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxV2Reports.setStatus("current")
_SdpBndMldSnpgRxV1Leaves_Type = Counter32
_SdpBndMldSnpgRxV1Leaves_Object = MibTableColumn
sdpBndMldSnpgRxV1Leaves = _SdpBndMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 12),
    _SdpBndMldSnpgRxV1Leaves_Type()
)
sdpBndMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxV1Leaves.setStatus("current")
_SdpBndMldSnpgRxUnknownType_Type = Counter32
_SdpBndMldSnpgRxUnknownType_Object = MibTableColumn
sdpBndMldSnpgRxUnknownType = _SdpBndMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 13),
    _SdpBndMldSnpgRxUnknownType_Type()
)
sdpBndMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxUnknownType.setStatus("current")
_SdpBndMldSnpgFwdGenQueries_Type = Counter32
_SdpBndMldSnpgFwdGenQueries_Object = MibTableColumn
sdpBndMldSnpgFwdGenQueries = _SdpBndMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 14),
    _SdpBndMldSnpgFwdGenQueries_Type()
)
sdpBndMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdGenQueries.setStatus("current")
_SdpBndMldSnpgFwdGrpSpecQueries_Type = Counter32
_SdpBndMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
sdpBndMldSnpgFwdGrpSpecQueries = _SdpBndMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 15),
    _SdpBndMldSnpgFwdGrpSpecQueries_Type()
)
sdpBndMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdGrpSpecQueries.setStatus("current")
_SdpBndMldSnpgFwdSrcSpecQueries_Type = Counter32
_SdpBndMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
sdpBndMldSnpgFwdSrcSpecQueries = _SdpBndMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 16),
    _SdpBndMldSnpgFwdSrcSpecQueries_Type()
)
sdpBndMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdSrcSpecQueries.setStatus("current")
_SdpBndMldSnpgFwdV1Reports_Type = Counter32
_SdpBndMldSnpgFwdV1Reports_Object = MibTableColumn
sdpBndMldSnpgFwdV1Reports = _SdpBndMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 17),
    _SdpBndMldSnpgFwdV1Reports_Type()
)
sdpBndMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdV1Reports.setStatus("current")
_SdpBndMldSnpgFwdV2Reports_Type = Counter32
_SdpBndMldSnpgFwdV2Reports_Object = MibTableColumn
sdpBndMldSnpgFwdV2Reports = _SdpBndMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 18),
    _SdpBndMldSnpgFwdV2Reports_Type()
)
sdpBndMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdV2Reports.setStatus("current")
_SdpBndMldSnpgFwdV1Leaves_Type = Counter32
_SdpBndMldSnpgFwdV1Leaves_Object = MibTableColumn
sdpBndMldSnpgFwdV1Leaves = _SdpBndMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 19),
    _SdpBndMldSnpgFwdV1Leaves_Type()
)
sdpBndMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdV1Leaves.setStatus("current")
_SdpBndMldSnpgFwdUnknownType_Type = Counter32
_SdpBndMldSnpgFwdUnknownType_Object = MibTableColumn
sdpBndMldSnpgFwdUnknownType = _SdpBndMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 20),
    _SdpBndMldSnpgFwdUnknownType_Type()
)
sdpBndMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdUnknownType.setStatus("current")
_SdpBndMldSnpgRxBadLenPkts_Type = Counter32
_SdpBndMldSnpgRxBadLenPkts_Object = MibTableColumn
sdpBndMldSnpgRxBadLenPkts = _SdpBndMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 21),
    _SdpBndMldSnpgRxBadLenPkts_Type()
)
sdpBndMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxBadLenPkts.setStatus("current")
_SdpBndMldSnpgRxBadMldChksmPkts_Type = Counter32
_SdpBndMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
sdpBndMldSnpgRxBadMldChksmPkts = _SdpBndMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 22),
    _SdpBndMldSnpgRxBadMldChksmPkts_Type()
)
sdpBndMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxBadMldChksmPkts.setStatus("current")
_SdpBndMldSnpgRxBadEncodedPkts_Type = Counter32
_SdpBndMldSnpgRxBadEncodedPkts_Object = MibTableColumn
sdpBndMldSnpgRxBadEncodedPkts = _SdpBndMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 23),
    _SdpBndMldSnpgRxBadEncodedPkts_Type()
)
sdpBndMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxBadEncodedPkts.setStatus("current")
_SdpBndMldSnpgRxNoRtrAlertPkts_Type = Counter32
_SdpBndMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sdpBndMldSnpgRxNoRtrAlertPkts = _SdpBndMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 24),
    _SdpBndMldSnpgRxNoRtrAlertPkts_Type()
)
sdpBndMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxNoRtrAlertPkts.setStatus("current")
_SdpBndMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_SdpBndMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sdpBndMldSnpgRxZeroSrcAdrPkts = _SdpBndMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 25),
    _SdpBndMldSnpgRxZeroSrcAdrPkts_Type()
)
sdpBndMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_SdpBndMldSnpgSendQueryCfgDrops_Type = Counter32
_SdpBndMldSnpgSendQueryCfgDrops_Object = MibTableColumn
sdpBndMldSnpgSendQueryCfgDrops = _SdpBndMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 26),
    _SdpBndMldSnpgSendQueryCfgDrops_Type()
)
sdpBndMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgSendQueryCfgDrops.setStatus("current")
_SdpBndMldSnpgImportPolicyDrops_Type = Counter32
_SdpBndMldSnpgImportPolicyDrops_Object = MibTableColumn
sdpBndMldSnpgImportPolicyDrops = _SdpBndMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 27),
    _SdpBndMldSnpgImportPolicyDrops_Type()
)
sdpBndMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgImportPolicyDrops.setStatus("current")
_SdpBndMldSnpgMaxNumGroupsDrops_Type = Counter32
_SdpBndMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
sdpBndMldSnpgMaxNumGroupsDrops = _SdpBndMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 28),
    _SdpBndMldSnpgMaxNumGroupsDrops_Type()
)
sdpBndMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgMaxNumGroupsDrops.setStatus("current")
_SdpBndMldSnpgRxWrongVersionPkts_Type = Counter32
_SdpBndMldSnpgRxWrongVersionPkts_Object = MibTableColumn
sdpBndMldSnpgRxWrongVersionPkts = _SdpBndMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 29),
    _SdpBndMldSnpgRxWrongVersionPkts_Type()
)
sdpBndMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxWrongVersionPkts.setStatus("current")
_SdpBndMldSnpgRxLocalScopePkts_Type = Counter32
_SdpBndMldSnpgRxLocalScopePkts_Object = MibTableColumn
sdpBndMldSnpgRxLocalScopePkts = _SdpBndMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 30),
    _SdpBndMldSnpgRxLocalScopePkts_Type()
)
sdpBndMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxLocalScopePkts.setStatus("current")
_SdpBndMldSnpgRxRsvdScopePkts_Type = Counter32
_SdpBndMldSnpgRxRsvdScopePkts_Object = MibTableColumn
sdpBndMldSnpgRxRsvdScopePkts = _SdpBndMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 31),
    _SdpBndMldSnpgRxRsvdScopePkts_Type()
)
sdpBndMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxRsvdScopePkts.setStatus("current")
_SdpBndMldSnpgMcacPolicyDrops_Type = Counter32
_SdpBndMldSnpgMcacPolicyDrops_Object = MibTableColumn
sdpBndMldSnpgMcacPolicyDrops = _SdpBndMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 32),
    _SdpBndMldSnpgMcacPolicyDrops_Type()
)
sdpBndMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgMcacPolicyDrops.setStatus("current")
_TmnxMldSnoopingNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingNotificationObjs = _TmnxMldSnoopingNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4)
)
_TmnxMldSnpgGroupAddressType_Type = InetAddressType
_TmnxMldSnpgGroupAddressType_Object = MibScalar
tmnxMldSnpgGroupAddressType = _TmnxMldSnpgGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4, 1),
    _TmnxMldSnpgGroupAddressType_Type()
)
tmnxMldSnpgGroupAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMldSnpgGroupAddressType.setStatus("current")


class _TmnxMldSnpgGroupAddress_Type(InetAddress):
    """Custom type tmnxMldSnpgGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMldSnpgGroupAddress_Type.__name__ = "InetAddress"
_TmnxMldSnpgGroupAddress_Object = MibScalar
tmnxMldSnpgGroupAddress = _TmnxMldSnpgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4, 2),
    _TmnxMldSnpgGroupAddress_Type()
)
tmnxMldSnpgGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMldSnpgGroupAddress.setStatus("current")
_TmnxMldSnpgMcsFailureReason_Type = DisplayString
_TmnxMldSnpgMcsFailureReason_Object = MibScalar
tmnxMldSnpgMcsFailureReason = _TmnxMldSnpgMcsFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4, 3),
    _TmnxMldSnpgMcsFailureReason_Type()
)
tmnxMldSnpgMcsFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMldSnpgMcsFailureReason.setStatus("current")
_TmnxMldSnoopingNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingNotifyPrefix = _TmnxMldSnoopingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45)
)
_TmnxMldSnoopingSapPrefix_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSapPrefix = _TmnxMldSnoopingSapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1)
)
_TmnxMldSnpgSapNotifications_ObjectIdentity = ObjectIdentity
tmnxMldSnpgSapNotifications = _TmnxMldSnpgSapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1, 0)
)
_TmnxMldSnoopingSdpBndPrefix_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSdpBndPrefix = _TmnxMldSnoopingSdpBndPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 2)
)
_TmnxMldSnpgSdpBndNotifications_ObjectIdentity = ObjectIdentity
tmnxMldSnpgSdpBndNotifications = _TmnxMldSnpgSdpBndNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 2, 0)
)

# Managed Objects groups

tmnxMldSnpgConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 1)
)
tmnxMldSnpgConfigGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgConfigTableLastChange"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgAdminState"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgRobustCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgReportSrcAddrType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgReportSrcAddr"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgQuerySrcAddrType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgQuerySrcAddr"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgConfigTableLastChange"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgImportPlcy"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgFastLeave"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMRouter"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgSendQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgQueryRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgRobustCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgLastMembIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgVersion"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBindMldSnpgConfigTableLastCh"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgImportPlcy"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgFastLeave"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMRouter"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgSendQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgQueryRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgRobustCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgLastMembIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgVersion"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigGroup.setStatus("current")

tmnxMldSnpgQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 2)
)
tmnxMldSnpgQuerierGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVersion"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierLocale"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierSdpId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVcId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierGenRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierRobustCount"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgQuerierGroup.setStatus("current")

tmnxMldSnpgProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 3)
)
tmnxMldSnpgProxyGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGrpSrcUpTime"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgProxyGroup.setStatus("current")

tmnxMldSnpgMRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 4)
)
tmnxMldSnpgMRouterGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterLocale"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterSdpId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVcId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVersion"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterGenRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterRobustCount"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgMRouterGroup.setStatus("current")

tmnxMldMvrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 5)
)
tmnxMldMvrGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgMvrAdminState"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgMvrDescription"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgMvrPolicy"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMvrFromVplsId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMvrToSapPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMvrToSapEncapVal"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpMvrFromVplsId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpMvrToSapPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpMvrToSapEncapVal"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMvrFromVplsCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMvrToSapCfgDrops"))
)
if mibBuilder.loadTexts:
    tmnxMldMvrGroup.setStatus("current")

tmnxMldSnpgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 6)
)
tmnxMldSnpgGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpV1HostExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpV1HostExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgGroup.setStatus("current")

tmnxMldSnpgStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 7)
)
tmnxMldSnpgStaticGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticGrpSrcTableLstCh"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticRowstatus"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBindMldSnpgStatGrpSrcTblLstCh"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticRowstatus"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticLastChange"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStaticGroup.setStatus("current")

tmnxMldSnpgStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 8)
)
tmnxMldSnpgStatsGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMcsFailures"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxRsvdScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStatsGroup.setStatus("current")

tmnxMldSnpgNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 9)
)
tmnxMldSnpgNotifyObjsGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgNotifyObjsGroup.setStatus("current")

tmnxMldSnpgConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 11)
)
tmnxMldSnpgConfigV8v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgDisRtrAlertChk"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgDisRtrAlertChk"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigV8v0Group.setStatus("current")

tmnxMldSnpgConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 12)
)
tmnxMldSnpgConfigV12v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacPolicyName"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacUnconstBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacPrRsvMndBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacinUseMndBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacinUseOplBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacAvailMndBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacAvailOplBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacValInTrans"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacPolicyName"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacUnconstBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacPrRsvMndBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacConstAdmSt"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacinUseMandBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacinUseOpnlBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacAvailMandBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacAvailOpnlBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacValInTrans"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacUseLagPortWt"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLevelRowStat"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLevelBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLevelLastChngT"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLagRowStat"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLagLevel"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLagLastChangeT"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigV12v0Group.setStatus("current")

tmnxMldSnpgStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 13)
)
tmnxMldSnpgStatsV12v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgMcacPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMcacPolicyDrops"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStatsV12v0Group.setStatus("current")


# Notification objects

sapMldSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1, 0, 1)
)
sapMldSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sapMldSnpgGrpLimitExceeded.setStatus(
        "current"
    )

sapMldSnpgMcsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1, 0, 2)
)
sapMldSnpgMcsFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    sapMldSnpgMcsFailure.setStatus(
        "current"
    )

sdpBndMldSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 2, 0, 1)
)
sdpBndMldSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpLimitExceeded.setStatus(
        "current"
    )


# Notifications groups

tmnxMldSnpgNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 10)
)
tmnxMldSnpgNotifyGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpLimitExceeded"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMcsFailure"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpLimitExceeded"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMldSnoopingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 1)
)
tmnxMldSnoopingCompliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingCompliance.setStatus(
        "current"
    )

tmnxMldSnoopingV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 2)
)
tmnxMldSnoopingV8v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMldSnoopingV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 3)
)
tmnxMldSnoopingV12v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MLD-SNOOPING-MIB",
    **{"TmnxMldSnpgLocation": TmnxMldSnpgLocation,
       "timetraMldSnoopingMIBModule": timetraMldSnoopingMIBModule,
       "tmnxMldSnoopingConformance": tmnxMldSnoopingConformance,
       "tmnxMldSnoopingCompliances": tmnxMldSnoopingCompliances,
       "tmnxMldSnoopingCompliance": tmnxMldSnoopingCompliance,
       "tmnxMldSnoopingV8v0Compliance": tmnxMldSnoopingV8v0Compliance,
       "tmnxMldSnoopingV12v0Compliance": tmnxMldSnoopingV12v0Compliance,
       "tmnxMldSnoopingGroups": tmnxMldSnoopingGroups,
       "tmnxMldSnpgConfigGroup": tmnxMldSnpgConfigGroup,
       "tmnxMldSnpgQuerierGroup": tmnxMldSnpgQuerierGroup,
       "tmnxMldSnpgProxyGroup": tmnxMldSnpgProxyGroup,
       "tmnxMldSnpgMRouterGroup": tmnxMldSnpgMRouterGroup,
       "tmnxMldMvrGroup": tmnxMldMvrGroup,
       "tmnxMldSnpgGroup": tmnxMldSnpgGroup,
       "tmnxMldSnpgStaticGroup": tmnxMldSnpgStaticGroup,
       "tmnxMldSnpgStatsGroup": tmnxMldSnpgStatsGroup,
       "tmnxMldSnpgNotifyObjsGroup": tmnxMldSnpgNotifyObjsGroup,
       "tmnxMldSnpgNotifyGroup": tmnxMldSnpgNotifyGroup,
       "tmnxMldSnpgConfigV8v0Group": tmnxMldSnpgConfigV8v0Group,
       "tmnxMldSnpgConfigV12v0Group": tmnxMldSnpgConfigV12v0Group,
       "tmnxMldSnpgStatsV12v0Group": tmnxMldSnpgStatsV12v0Group,
       "tmnxMldSnoopingObjs": tmnxMldSnoopingObjs,
       "tmnxMldSnoopingTlsObjs": tmnxMldSnoopingTlsObjs,
       "tlsMldSnpgConfigTableLastChange": tlsMldSnpgConfigTableLastChange,
       "tlsMldSnpgConfigTable": tlsMldSnpgConfigTable,
       "tlsMldSnpgConfigEntry": tlsMldSnpgConfigEntry,
       "tlsMldSnpgCfgLastChangeTime": tlsMldSnpgCfgLastChangeTime,
       "tlsMldSnpgCfgAdminState": tlsMldSnpgCfgAdminState,
       "tlsMldSnpgCfgGenQueryIntvl": tlsMldSnpgCfgGenQueryIntvl,
       "tlsMldSnpgCfgRobustCount": tlsMldSnpgCfgRobustCount,
       "tlsMldSnpgCfgReportSrcAddrType": tlsMldSnpgCfgReportSrcAddrType,
       "tlsMldSnpgCfgReportSrcAddr": tlsMldSnpgCfgReportSrcAddr,
       "tlsMldSnpgCfgQuerySrcAddrType": tlsMldSnpgCfgQuerySrcAddrType,
       "tlsMldSnpgCfgQuerySrcAddr": tlsMldSnpgCfgQuerySrcAddr,
       "tlsMldSnpgCfgMvrAdminState": tlsMldSnpgCfgMvrAdminState,
       "tlsMldSnpgCfgMvrDescription": tlsMldSnpgCfgMvrDescription,
       "tlsMldSnpgCfgMvrPolicy": tlsMldSnpgCfgMvrPolicy,
       "tlsMldSnpgQuerierTable": tlsMldSnpgQuerierTable,
       "tlsMldSnpgQuerierEntry": tlsMldSnpgQuerierEntry,
       "tlsMldSnpgQuerierVersion": tlsMldSnpgQuerierVersion,
       "tlsMldSnpgQuerierAddressType": tlsMldSnpgQuerierAddressType,
       "tlsMldSnpgQuerierAddress": tlsMldSnpgQuerierAddress,
       "tlsMldSnpgQuerierLocale": tlsMldSnpgQuerierLocale,
       "tlsMldSnpgQuerierPortId": tlsMldSnpgQuerierPortId,
       "tlsMldSnpgQuerierEncapValue": tlsMldSnpgQuerierEncapValue,
       "tlsMldSnpgQuerierSdpId": tlsMldSnpgQuerierSdpId,
       "tlsMldSnpgQuerierVcId": tlsMldSnpgQuerierVcId,
       "tlsMldSnpgQuerierUpTime": tlsMldSnpgQuerierUpTime,
       "tlsMldSnpgQuerierExpiryTime": tlsMldSnpgQuerierExpiryTime,
       "tlsMldSnpgQuerierGenQueryIntvl": tlsMldSnpgQuerierGenQueryIntvl,
       "tlsMldSnpgQuerierGenRespIntvl": tlsMldSnpgQuerierGenRespIntvl,
       "tlsMldSnpgQuerierRobustCount": tlsMldSnpgQuerierRobustCount,
       "tlsMldSnpgProxyGroupTable": tlsMldSnpgProxyGroupTable,
       "tlsMldSnpgProxyGroupEntry": tlsMldSnpgProxyGroupEntry,
       "tlsMldSnpgProxyGroupAddressType": tlsMldSnpgProxyGroupAddressType,
       "tlsMldSnpgProxyGroupAddress": tlsMldSnpgProxyGroupAddress,
       "tlsMldSnpgProxyGroupFilterMode": tlsMldSnpgProxyGroupFilterMode,
       "tlsMldSnpgProxyGroupUpTime": tlsMldSnpgProxyGroupUpTime,
       "tlsMldSnpgProxyGrpSrcTable": tlsMldSnpgProxyGrpSrcTable,
       "tlsMldSnpgProxyGrpSrcEntry": tlsMldSnpgProxyGrpSrcEntry,
       "tlsMldSnpgProxyGrpSrcAddrTp": tlsMldSnpgProxyGrpSrcAddrTp,
       "tlsMldSnpgProxyGrpSrcAddr": tlsMldSnpgProxyGrpSrcAddr,
       "tlsMldSnpgProxyGrpSrcUpTime": tlsMldSnpgProxyGrpSrcUpTime,
       "tlsMldSnpgMRouterTable": tlsMldSnpgMRouterTable,
       "tlsMldSnpgMRouterEntry": tlsMldSnpgMRouterEntry,
       "tlsMldSnpgMRouterAddressType": tlsMldSnpgMRouterAddressType,
       "tlsMldSnpgMRouterAddress": tlsMldSnpgMRouterAddress,
       "tlsMldSnpgMRouterLocale": tlsMldSnpgMRouterLocale,
       "tlsMldSnpgMRouterPortId": tlsMldSnpgMRouterPortId,
       "tlsMldSnpgMRouterEncapValue": tlsMldSnpgMRouterEncapValue,
       "tlsMldSnpgMRouterSdpId": tlsMldSnpgMRouterSdpId,
       "tlsMldSnpgMRouterVcId": tlsMldSnpgMRouterVcId,
       "tlsMldSnpgMRouterVersion": tlsMldSnpgMRouterVersion,
       "tlsMldSnpgMRouterExpiryTime": tlsMldSnpgMRouterExpiryTime,
       "tlsMldSnpgMRouterUpTime": tlsMldSnpgMRouterUpTime,
       "tlsMldSnpgMRouterGenQueryIntvl": tlsMldSnpgMRouterGenQueryIntvl,
       "tlsMldSnpgMRouterGenRespIntvl": tlsMldSnpgMRouterGenRespIntvl,
       "tlsMldSnpgMRouterRobustCount": tlsMldSnpgMRouterRobustCount,
       "tmnxMldSnoopingSapObjs": tmnxMldSnoopingSapObjs,
       "sapMldSnpgConfigTableLastChange": sapMldSnpgConfigTableLastChange,
       "sapMldSnpgConfigTable": sapMldSnpgConfigTable,
       "sapMldSnpgConfigEntry": sapMldSnpgConfigEntry,
       "sapMldSnpgCfgLastChangeTime": sapMldSnpgCfgLastChangeTime,
       "sapMldSnpgCfgImportPlcy": sapMldSnpgCfgImportPlcy,
       "sapMldSnpgCfgFastLeave": sapMldSnpgCfgFastLeave,
       "sapMldSnpgCfgMRouter": sapMldSnpgCfgMRouter,
       "sapMldSnpgCfgSendQueries": sapMldSnpgCfgSendQueries,
       "sapMldSnpgCfgGenQueryIntvl": sapMldSnpgCfgGenQueryIntvl,
       "sapMldSnpgCfgQueryRespIntvl": sapMldSnpgCfgQueryRespIntvl,
       "sapMldSnpgCfgRobustCount": sapMldSnpgCfgRobustCount,
       "sapMldSnpgCfgLastMembIntvl": sapMldSnpgCfgLastMembIntvl,
       "sapMldSnpgCfgMaxNbrGrps": sapMldSnpgCfgMaxNbrGrps,
       "sapMldSnpgCfgMvrFromVplsId": sapMldSnpgCfgMvrFromVplsId,
       "sapMldSnpgCfgMvrToSapPortId": sapMldSnpgCfgMvrToSapPortId,
       "sapMldSnpgCfgMvrToSapEncapVal": sapMldSnpgCfgMvrToSapEncapVal,
       "sapMldSnpgCfgVersion": sapMldSnpgCfgVersion,
       "sapMldSnpgCfgDisRtrAlertChk": sapMldSnpgCfgDisRtrAlertChk,
       "sapMldSnpgCfgMcacPolicyName": sapMldSnpgCfgMcacPolicyName,
       "sapMldSnpgCfgMcacUnconstBW": sapMldSnpgCfgMcacUnconstBW,
       "sapMldSnpgCfgMcacPrRsvMndBW": sapMldSnpgCfgMcacPrRsvMndBW,
       "sapMldSnpgCfgMcacConstAdmSt": sapMldSnpgCfgMcacConstAdmSt,
       "sapMldSnpgCfgMcacinUseMandBw": sapMldSnpgCfgMcacinUseMandBw,
       "sapMldSnpgCfgMcacinUseOpnlBw": sapMldSnpgCfgMcacinUseOpnlBw,
       "sapMldSnpgCfgMcacAvailMandBw": sapMldSnpgCfgMcacAvailMandBw,
       "sapMldSnpgCfgMcacAvailOpnlBw": sapMldSnpgCfgMcacAvailOpnlBw,
       "sapMldSnpgCfgMcacValInTrans": sapMldSnpgCfgMcacValInTrans,
       "sapMldSnpgCfgMcacUseLagPortWt": sapMldSnpgCfgMcacUseLagPortWt,
       "sapMldSnpgGroupTable": sapMldSnpgGroupTable,
       "sapMldSnpgGroupEntry": sapMldSnpgGroupEntry,
       "sapMldSnpgGrpAddressType": sapMldSnpgGrpAddressType,
       "sapMldSnpgGrpAddress": sapMldSnpgGrpAddress,
       "sapMldSnpgGrpType": sapMldSnpgGrpType,
       "sapMldSnpgGrpFilterMode": sapMldSnpgGrpFilterMode,
       "sapMldSnpgGrpUpTime": sapMldSnpgGrpUpTime,
       "sapMldSnpgGrpExpiryTime": sapMldSnpgGrpExpiryTime,
       "sapMldSnpgGrpCompatMode": sapMldSnpgGrpCompatMode,
       "sapMldSnpgGrpV1HostExpTime": sapMldSnpgGrpV1HostExpTime,
       "sapMldSnpgGrpMvrFromVplsId": sapMldSnpgGrpMvrFromVplsId,
       "sapMldSnpgGrpMvrToSapPortId": sapMldSnpgGrpMvrToSapPortId,
       "sapMldSnpgGrpMvrToSapEncapVal": sapMldSnpgGrpMvrToSapEncapVal,
       "sapMldSnpgGrpSrcTable": sapMldSnpgGrpSrcTable,
       "sapMldSnpgGrpSrcEntry": sapMldSnpgGrpSrcEntry,
       "sapMldSnpgGrpSrcAddrType": sapMldSnpgGrpSrcAddrType,
       "sapMldSnpgGrpSrcAddr": sapMldSnpgGrpSrcAddr,
       "sapMldSnpgGrpSrcType": sapMldSnpgGrpSrcType,
       "sapMldSnpgGrpSrcUpTime": sapMldSnpgGrpSrcUpTime,
       "sapMldSnpgGrpSrcExpiryTime": sapMldSnpgGrpSrcExpiryTime,
       "sapMldSnpgStaticGrpSrcTableLstCh": sapMldSnpgStaticGrpSrcTableLstCh,
       "sapMldSnpgStaticGrpSrcTable": sapMldSnpgStaticGrpSrcTable,
       "sapMldSnpgStaticGrpSrcEntry": sapMldSnpgStaticGrpSrcEntry,
       "sapMldSnpgStaticGroupAddrType": sapMldSnpgStaticGroupAddrType,
       "sapMldSnpgStaticGroupAddr": sapMldSnpgStaticGroupAddr,
       "sapMldSnpgStaticSourceAddrType": sapMldSnpgStaticSourceAddrType,
       "sapMldSnpgStaticSourceAddr": sapMldSnpgStaticSourceAddr,
       "sapMldSnpgStaticRowstatus": sapMldSnpgStaticRowstatus,
       "sapMldSnpgStaticLastChangeTime": sapMldSnpgStaticLastChangeTime,
       "sapMldSnpgStatsTable": sapMldSnpgStatsTable,
       "sapMldSnpgStatsEntry": sapMldSnpgStatsEntry,
       "sapMldSnpgTxGenQueries": sapMldSnpgTxGenQueries,
       "sapMldSnpgTxGrpSpecQueries": sapMldSnpgTxGrpSpecQueries,
       "sapMldSnpgTxSrcSpecQueries": sapMldSnpgTxSrcSpecQueries,
       "sapMldSnpgTxV1Reports": sapMldSnpgTxV1Reports,
       "sapMldSnpgTxV2Reports": sapMldSnpgTxV2Reports,
       "sapMldSnpgTxV1Leaves": sapMldSnpgTxV1Leaves,
       "sapMldSnpgRxGenQueries": sapMldSnpgRxGenQueries,
       "sapMldSnpgRxGrpSpecQueries": sapMldSnpgRxGrpSpecQueries,
       "sapMldSnpgRxSrcSpecQueries": sapMldSnpgRxSrcSpecQueries,
       "sapMldSnpgRxV1Reports": sapMldSnpgRxV1Reports,
       "sapMldSnpgRxV2Reports": sapMldSnpgRxV2Reports,
       "sapMldSnpgRxV1Leaves": sapMldSnpgRxV1Leaves,
       "sapMldSnpgRxUnknownType": sapMldSnpgRxUnknownType,
       "sapMldSnpgFwdGenQueries": sapMldSnpgFwdGenQueries,
       "sapMldSnpgFwdGrpSpecQueries": sapMldSnpgFwdGrpSpecQueries,
       "sapMldSnpgFwdSrcSpecQueries": sapMldSnpgFwdSrcSpecQueries,
       "sapMldSnpgFwdV1Reports": sapMldSnpgFwdV1Reports,
       "sapMldSnpgFwdV2Reports": sapMldSnpgFwdV2Reports,
       "sapMldSnpgFwdV1Leaves": sapMldSnpgFwdV1Leaves,
       "sapMldSnpgFwdUnknownType": sapMldSnpgFwdUnknownType,
       "sapMldSnpgRxBadLenPkts": sapMldSnpgRxBadLenPkts,
       "sapMldSnpgRxBadMldChksmPkts": sapMldSnpgRxBadMldChksmPkts,
       "sapMldSnpgRxBadEncodedPkts": sapMldSnpgRxBadEncodedPkts,
       "sapMldSnpgRxNoRtrAlertPkts": sapMldSnpgRxNoRtrAlertPkts,
       "sapMldSnpgRxZeroSrcAdrPkts": sapMldSnpgRxZeroSrcAdrPkts,
       "sapMldSnpgSendQueryCfgDrops": sapMldSnpgSendQueryCfgDrops,
       "sapMldSnpgImportPolicyDrops": sapMldSnpgImportPolicyDrops,
       "sapMldSnpgMaxNumGroupsDrops": sapMldSnpgMaxNumGroupsDrops,
       "sapMldSnpgMvrFromVplsCfgDrops": sapMldSnpgMvrFromVplsCfgDrops,
       "sapMldSnpgMvrToSapCfgDrops": sapMldSnpgMvrToSapCfgDrops,
       "sapMldSnpgRxWrongVersionPkts": sapMldSnpgRxWrongVersionPkts,
       "sapMldSnpgMcsFailures": sapMldSnpgMcsFailures,
       "sapMldSnpgRxLocalScopePkts": sapMldSnpgRxLocalScopePkts,
       "sapMldSnpgRxRsvdScopePkts": sapMldSnpgRxRsvdScopePkts,
       "sapMldSnpgMcacPolicyDrops": sapMldSnpgMcacPolicyDrops,
       "sapMldSnpgMcacLevelTable": sapMldSnpgMcacLevelTable,
       "sapMldSnpgMcacLevelEntry": sapMldSnpgMcacLevelEntry,
       "sapMldSnpgCfgMcacLevelRowStat": sapMldSnpgCfgMcacLevelRowStat,
       "sapMldSnpgCfgMcacLevelBW": sapMldSnpgCfgMcacLevelBW,
       "sapMldSnpgCfgMcacLevelLastChngT": sapMldSnpgCfgMcacLevelLastChngT,
       "sapMldSnpgMcacLagTable": sapMldSnpgMcacLagTable,
       "sapMldSnpgMcacLagEntry": sapMldSnpgMcacLagEntry,
       "sapMldSnpgCfgMcacLagRowStat": sapMldSnpgCfgMcacLagRowStat,
       "sapMldSnpgCfgMcacLagLevel": sapMldSnpgCfgMcacLagLevel,
       "sapMldSnpgCfgMcacLagLastChangeT": sapMldSnpgCfgMcacLagLastChangeT,
       "tmnxMldSnoopingSdpBindObjs": tmnxMldSnoopingSdpBindObjs,
       "sdpBindMldSnpgConfigTableLastCh": sdpBindMldSnpgConfigTableLastCh,
       "sdpBindMldSnpgConfigTable": sdpBindMldSnpgConfigTable,
       "sdpBindMldSnpgConfigEntry": sdpBindMldSnpgConfigEntry,
       "sdpBndMldSnpgCfgLastChangeTime": sdpBndMldSnpgCfgLastChangeTime,
       "sdpBndMldSnpgCfgImportPlcy": sdpBndMldSnpgCfgImportPlcy,
       "sdpBndMldSnpgCfgFastLeave": sdpBndMldSnpgCfgFastLeave,
       "sdpBndMldSnpgCfgMRouter": sdpBndMldSnpgCfgMRouter,
       "sdpBndMldSnpgCfgSendQueries": sdpBndMldSnpgCfgSendQueries,
       "sdpBndMldSnpgCfgGenQueryIntvl": sdpBndMldSnpgCfgGenQueryIntvl,
       "sdpBndMldSnpgCfgQueryRespIntvl": sdpBndMldSnpgCfgQueryRespIntvl,
       "sdpBndMldSnpgCfgRobustCount": sdpBndMldSnpgCfgRobustCount,
       "sdpBndMldSnpgCfgLastMembIntvl": sdpBndMldSnpgCfgLastMembIntvl,
       "sdpBndMldSnpgCfgMaxNbrGrps": sdpBndMldSnpgCfgMaxNbrGrps,
       "sdpBndMldSnpgCfgVersion": sdpBndMldSnpgCfgVersion,
       "sdpBndMldSnpgCfgDisRtrAlertChk": sdpBndMldSnpgCfgDisRtrAlertChk,
       "sdpBndMldSnpgCfgMcacPolicyName": sdpBndMldSnpgCfgMcacPolicyName,
       "sdpBndMldSnpgCfgMcacUnconstBW": sdpBndMldSnpgCfgMcacUnconstBW,
       "sdpBndMldSnpgCfgMcacPrRsvMndBW": sdpBndMldSnpgCfgMcacPrRsvMndBW,
       "sdpBndMldSnpgCfgMcacinUseMndBw": sdpBndMldSnpgCfgMcacinUseMndBw,
       "sdpBndMldSnpgCfgMcacinUseOplBw": sdpBndMldSnpgCfgMcacinUseOplBw,
       "sdpBndMldSnpgCfgMcacAvailMndBw": sdpBndMldSnpgCfgMcacAvailMndBw,
       "sdpBndMldSnpgCfgMcacAvailOplBw": sdpBndMldSnpgCfgMcacAvailOplBw,
       "sdpBndMldSnpgCfgMcacValInTrans": sdpBndMldSnpgCfgMcacValInTrans,
       "sdpBindMldSnpgGroupTable": sdpBindMldSnpgGroupTable,
       "sdpBindMldSnpgGroupEntry": sdpBindMldSnpgGroupEntry,
       "sdpBndMldSnpgGrpAddressType": sdpBndMldSnpgGrpAddressType,
       "sdpBndMldSnpgGrpAddress": sdpBndMldSnpgGrpAddress,
       "sdpBndMldSnpgGrpType": sdpBndMldSnpgGrpType,
       "sdpBndMldSnpgGrpFilterMode": sdpBndMldSnpgGrpFilterMode,
       "sdpBndMldSnpgGrpUpTime": sdpBndMldSnpgGrpUpTime,
       "sdpBndMldSnpgGrpExpiryTime": sdpBndMldSnpgGrpExpiryTime,
       "sdpBndMldSnpgGrpCompatMode": sdpBndMldSnpgGrpCompatMode,
       "sdpBndMldSnpgGrpV1HostExpTime": sdpBndMldSnpgGrpV1HostExpTime,
       "sdpBindMldSnpgGrpSrcTable": sdpBindMldSnpgGrpSrcTable,
       "sdpBindMldSnpgGrpSrcEntry": sdpBindMldSnpgGrpSrcEntry,
       "sdpBndMldSnpgGrpSrcAddrType": sdpBndMldSnpgGrpSrcAddrType,
       "sdpBndMldSnpgGrpSrcAddr": sdpBndMldSnpgGrpSrcAddr,
       "sdpBndMldSnpgGrpSrcType": sdpBndMldSnpgGrpSrcType,
       "sdpBndMldSnpgGrpSrcUpTime": sdpBndMldSnpgGrpSrcUpTime,
       "sdpBndMldSnpgGrpSrcExpiryTime": sdpBndMldSnpgGrpSrcExpiryTime,
       "sdpBindMldSnpgStatGrpSrcTblLstCh": sdpBindMldSnpgStatGrpSrcTblLstCh,
       "sdpBindMldSnpgStatGrpSrcTable": sdpBindMldSnpgStatGrpSrcTable,
       "sdpBindMldSnpgStatGrpSrcEntry": sdpBindMldSnpgStatGrpSrcEntry,
       "sdpBndMldSnpgStaticGroupAddrType": sdpBndMldSnpgStaticGroupAddrType,
       "sdpBndMldSnpgStaticGroupAddr": sdpBndMldSnpgStaticGroupAddr,
       "sdpBndMldSnpgStaticSourceAddrTp": sdpBndMldSnpgStaticSourceAddrTp,
       "sdpBndMldSnpgStaticSourceAddr": sdpBndMldSnpgStaticSourceAddr,
       "sdpBndMldSnpgStaticRowstatus": sdpBndMldSnpgStaticRowstatus,
       "sdpBndMldSnpgStaticLastChange": sdpBndMldSnpgStaticLastChange,
       "sdpBindMldSnpgStatsTable": sdpBindMldSnpgStatsTable,
       "sdpBindMldSnpgStatsEntry": sdpBindMldSnpgStatsEntry,
       "sdpBndMldSnpgTxGenQueries": sdpBndMldSnpgTxGenQueries,
       "sdpBndMldSnpgTxGrpSpecQueries": sdpBndMldSnpgTxGrpSpecQueries,
       "sdpBndMldSnpgTxSrcSpecQueries": sdpBndMldSnpgTxSrcSpecQueries,
       "sdpBndMldSnpgTxV1Reports": sdpBndMldSnpgTxV1Reports,
       "sdpBndMldSnpgTxV2Reports": sdpBndMldSnpgTxV2Reports,
       "sdpBndMldSnpgTxV1Leaves": sdpBndMldSnpgTxV1Leaves,
       "sdpBndMldSnpgRxGenQueries": sdpBndMldSnpgRxGenQueries,
       "sdpBndMldSnpgRxGrpSpecQueries": sdpBndMldSnpgRxGrpSpecQueries,
       "sdpBndMldSnpgRxSrcSpecQueries": sdpBndMldSnpgRxSrcSpecQueries,
       "sdpBndMldSnpgRxV1Reports": sdpBndMldSnpgRxV1Reports,
       "sdpBndMldSnpgRxV2Reports": sdpBndMldSnpgRxV2Reports,
       "sdpBndMldSnpgRxV1Leaves": sdpBndMldSnpgRxV1Leaves,
       "sdpBndMldSnpgRxUnknownType": sdpBndMldSnpgRxUnknownType,
       "sdpBndMldSnpgFwdGenQueries": sdpBndMldSnpgFwdGenQueries,
       "sdpBndMldSnpgFwdGrpSpecQueries": sdpBndMldSnpgFwdGrpSpecQueries,
       "sdpBndMldSnpgFwdSrcSpecQueries": sdpBndMldSnpgFwdSrcSpecQueries,
       "sdpBndMldSnpgFwdV1Reports": sdpBndMldSnpgFwdV1Reports,
       "sdpBndMldSnpgFwdV2Reports": sdpBndMldSnpgFwdV2Reports,
       "sdpBndMldSnpgFwdV1Leaves": sdpBndMldSnpgFwdV1Leaves,
       "sdpBndMldSnpgFwdUnknownType": sdpBndMldSnpgFwdUnknownType,
       "sdpBndMldSnpgRxBadLenPkts": sdpBndMldSnpgRxBadLenPkts,
       "sdpBndMldSnpgRxBadMldChksmPkts": sdpBndMldSnpgRxBadMldChksmPkts,
       "sdpBndMldSnpgRxBadEncodedPkts": sdpBndMldSnpgRxBadEncodedPkts,
       "sdpBndMldSnpgRxNoRtrAlertPkts": sdpBndMldSnpgRxNoRtrAlertPkts,
       "sdpBndMldSnpgRxZeroSrcAdrPkts": sdpBndMldSnpgRxZeroSrcAdrPkts,
       "sdpBndMldSnpgSendQueryCfgDrops": sdpBndMldSnpgSendQueryCfgDrops,
       "sdpBndMldSnpgImportPolicyDrops": sdpBndMldSnpgImportPolicyDrops,
       "sdpBndMldSnpgMaxNumGroupsDrops": sdpBndMldSnpgMaxNumGroupsDrops,
       "sdpBndMldSnpgRxWrongVersionPkts": sdpBndMldSnpgRxWrongVersionPkts,
       "sdpBndMldSnpgRxLocalScopePkts": sdpBndMldSnpgRxLocalScopePkts,
       "sdpBndMldSnpgRxRsvdScopePkts": sdpBndMldSnpgRxRsvdScopePkts,
       "sdpBndMldSnpgMcacPolicyDrops": sdpBndMldSnpgMcacPolicyDrops,
       "tmnxMldSnoopingNotificationObjs": tmnxMldSnoopingNotificationObjs,
       "tmnxMldSnpgGroupAddressType": tmnxMldSnpgGroupAddressType,
       "tmnxMldSnpgGroupAddress": tmnxMldSnpgGroupAddress,
       "tmnxMldSnpgMcsFailureReason": tmnxMldSnpgMcsFailureReason,
       "tmnxMldSnoopingNotifyPrefix": tmnxMldSnoopingNotifyPrefix,
       "tmnxMldSnoopingSapPrefix": tmnxMldSnoopingSapPrefix,
       "tmnxMldSnpgSapNotifications": tmnxMldSnpgSapNotifications,
       "sapMldSnpgGrpLimitExceeded": sapMldSnpgGrpLimitExceeded,
       "sapMldSnpgMcsFailure": sapMldSnpgMcsFailure,
       "tmnxMldSnoopingSdpBndPrefix": tmnxMldSnoopingSdpBndPrefix,
       "tmnxMldSnpgSdpBndNotifications": tmnxMldSnpgSdpBndNotifications,
       "sdpBndMldSnpgGrpLimitExceeded": sdpBndMldSnpgGrpLimitExceeded}
)
