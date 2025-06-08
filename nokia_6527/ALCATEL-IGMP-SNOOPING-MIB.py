# SNMP MIB module (ALCATEL-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALCATEL-IGMP-SNOOPING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:56:00 2025
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

(alcatelCommonMIBModules,
 alcatelConformance,
 alcatelNotifyPrefix,
 alcatelObjects) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "alcatelCommonMIBModules",
    "alcatelConformance",
    "alcatelNotifyPrefix",
    "alcatelObjects")

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
 TmnxIgmpGroupFilterMode,
 TmnxIgmpGroupType,
 TmnxIgmpVersion,
 TmnxPortID,
 TmnxServId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxIgmpGroupFilterMode",
    "TmnxIgmpGroupType",
    "TmnxIgmpVersion",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVcIdOrNone")


# MODULE-IDENTITY

alcatelIgmpSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    alcatelIgmpSnoopingMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1905-08-31 00:00",
         "1905-03-29 00:00",
         "1904-05-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlxIgmpSnpgAdminState(TextualConvention, Integer32):
    status = "current"
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



class AlxIgmpSnpgLocation(TextualConvention, Integer32):
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
        *(("sap", 1),
          ("sdp", 2),
          ("rvpls", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlxIgmpSnoopingConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingConformance = _AlxIgmpSnoopingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2)
)
_AlxIgmpSnoopingTlsConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsConformance = _AlxIgmpSnoopingTlsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1)
)
_AlxIgmpSnoopingTlsCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsCompliancs = _AlxIgmpSnoopingTlsCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1)
)
_AlxIgmpSnoopingTlsGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsGroups = _AlxIgmpSnoopingTlsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2)
)
_AlxIgmpSnoopingSapConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapConformance = _AlxIgmpSnoopingSapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2)
)
_AlxIgmpSnoopingSapCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapCompliancs = _AlxIgmpSnoopingSapCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1)
)
_AlxIgmpSnoopingSapGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapGroups = _AlxIgmpSnoopingSapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2)
)
_AlxIgmpSnoopingSdpBndConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndConformance = _AlxIgmpSnoopingSdpBndConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3)
)
_AlxIgmpSnoopingSdpBndCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndCompliancs = _AlxIgmpSnoopingSdpBndCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1)
)
_AlxIgmpSnoopingSdpBndGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndGroups = _AlxIgmpSnoopingSdpBndGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2)
)
_AlxIgmpSnoopingObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingObjs = _AlxIgmpSnoopingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2)
)
_AlxIgmpSnoopingTlsObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsObjs = _AlxIgmpSnoopingTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1)
)
_TlsIgmpSnpgConfigTable_Object = MibTable
tlsIgmpSnpgConfigTable = _TlsIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgConfigTable.setStatus("current")
_TlsIgmpSnpgConfigEntry_Object = MibTableRow
tlsIgmpSnpgConfigEntry = _TlsIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1)
)
tlsIgmpSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgConfigEntry.setStatus("current")


class _TlsIgmpSnpgCfgAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tlsIgmpSnpgCfgAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TlsIgmpSnpgCfgAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TlsIgmpSnpgCfgAdminState_Object = MibTableColumn
tlsIgmpSnpgCfgAdminState = _TlsIgmpSnpgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 1),
    _TlsIgmpSnpgCfgAdminState_Type()
)
tlsIgmpSnpgCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgAdminState.setStatus("current")


class _TlsIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tlsIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlsIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TlsIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
tlsIgmpSnpgCfgGenQueryIntvl = _TlsIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 2),
    _TlsIgmpSnpgCfgGenQueryIntvl_Type()
)
tlsIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TlsIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tlsIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TlsIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TlsIgmpSnpgCfgRobustCount_Object = MibTableColumn
tlsIgmpSnpgCfgRobustCount = _TlsIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 3),
    _TlsIgmpSnpgCfgRobustCount_Type()
)
tlsIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgRobustCount.setStatus("current")


class _TlsIgmpSnpgCfgReportSrcAddress_Type(IpAddress):
    """Custom type tlsIgmpSnpgCfgReportSrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TlsIgmpSnpgCfgReportSrcAddress_Type.__name__ = "IpAddress"
_TlsIgmpSnpgCfgReportSrcAddress_Object = MibTableColumn
tlsIgmpSnpgCfgReportSrcAddress = _TlsIgmpSnpgCfgReportSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 4),
    _TlsIgmpSnpgCfgReportSrcAddress_Type()
)
tlsIgmpSnpgCfgReportSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgReportSrcAddress.setStatus("current")


class _TlsIgmpSnpgCfgMvrAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tlsIgmpSnpgCfgMvrAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TlsIgmpSnpgCfgMvrAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TlsIgmpSnpgCfgMvrAdminState_Object = MibTableColumn
tlsIgmpSnpgCfgMvrAdminState = _TlsIgmpSnpgCfgMvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 5),
    _TlsIgmpSnpgCfgMvrAdminState_Type()
)
tlsIgmpSnpgCfgMvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgMvrAdminState.setStatus("current")


class _TlsIgmpSnpgCfgMvrDescription_Type(TItemDescription):
    """Custom type tlsIgmpSnpgCfgMvrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TlsIgmpSnpgCfgMvrDescription_Type.__name__ = "TItemDescription"
_TlsIgmpSnpgCfgMvrDescription_Object = MibTableColumn
tlsIgmpSnpgCfgMvrDescription = _TlsIgmpSnpgCfgMvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 6),
    _TlsIgmpSnpgCfgMvrDescription_Type()
)
tlsIgmpSnpgCfgMvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgMvrDescription.setStatus("current")


class _TlsIgmpSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tlsIgmpSnpgCfgMvrPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TlsIgmpSnpgCfgMvrPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TlsIgmpSnpgCfgMvrPolicy_Object = MibTableColumn
tlsIgmpSnpgCfgMvrPolicy = _TlsIgmpSnpgCfgMvrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 7),
    _TlsIgmpSnpgCfgMvrPolicy_Type()
)
tlsIgmpSnpgCfgMvrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgMvrPolicy.setStatus("current")


class _TlsIgmpSnpgCfgQuerySrcAddress_Type(IpAddress):
    """Custom type tlsIgmpSnpgCfgQuerySrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TlsIgmpSnpgCfgQuerySrcAddress_Type.__name__ = "IpAddress"
_TlsIgmpSnpgCfgQuerySrcAddress_Object = MibTableColumn
tlsIgmpSnpgCfgQuerySrcAddress = _TlsIgmpSnpgCfgQuerySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 8),
    _TlsIgmpSnpgCfgQuerySrcAddress_Type()
)
tlsIgmpSnpgCfgQuerySrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgQuerySrcAddress.setStatus("current")


class _TlsIgmpSnpgCfgQuerySrcAddrType_Type(Integer32):
    """Custom type tlsIgmpSnpgCfgQuerySrcAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("querySrcAddr", 1),
          ("systemIpAddr", 2))
    )


_TlsIgmpSnpgCfgQuerySrcAddrType_Type.__name__ = "Integer32"
_TlsIgmpSnpgCfgQuerySrcAddrType_Object = MibTableColumn
tlsIgmpSnpgCfgQuerySrcAddrType = _TlsIgmpSnpgCfgQuerySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 9),
    _TlsIgmpSnpgCfgQuerySrcAddrType_Type()
)
tlsIgmpSnpgCfgQuerySrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgQuerySrcAddrType.setStatus("current")
_TlsIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_TlsIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
tlsIgmpSnpgCfgLastChangeTime = _TlsIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 10),
    _TlsIgmpSnpgCfgLastChangeTime_Type()
)
tlsIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgLastChangeTime.setStatus("current")
_TlsIgmpSnpgQuerierTable_Object = MibTable
tlsIgmpSnpgQuerierTable = _TlsIgmpSnpgQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierTable.setStatus("current")
_TlsIgmpSnpgQuerierEntry_Object = MibTableRow
tlsIgmpSnpgQuerierEntry = _TlsIgmpSnpgQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1)
)
tlsIgmpSnpgQuerierEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierEntry.setStatus("current")
_TlsIgmpSnpgQuerierVersion_Type = TmnxIgmpVersion
_TlsIgmpSnpgQuerierVersion_Object = MibTableColumn
tlsIgmpSnpgQuerierVersion = _TlsIgmpSnpgQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 1),
    _TlsIgmpSnpgQuerierVersion_Type()
)
tlsIgmpSnpgQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVersion.setStatus("current")
_TlsIgmpSnpgQuerierAddress_Type = IpAddress
_TlsIgmpSnpgQuerierAddress_Object = MibTableColumn
tlsIgmpSnpgQuerierAddress = _TlsIgmpSnpgQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 2),
    _TlsIgmpSnpgQuerierAddress_Type()
)
tlsIgmpSnpgQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierAddress.setStatus("current")
_TlsIgmpSnpgQuerierLocale_Type = AlxIgmpSnpgLocation
_TlsIgmpSnpgQuerierLocale_Object = MibTableColumn
tlsIgmpSnpgQuerierLocale = _TlsIgmpSnpgQuerierLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 3),
    _TlsIgmpSnpgQuerierLocale_Type()
)
tlsIgmpSnpgQuerierLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierLocale.setStatus("current")
_TlsIgmpSnpgQuerierPortId_Type = TmnxPortID
_TlsIgmpSnpgQuerierPortId_Object = MibTableColumn
tlsIgmpSnpgQuerierPortId = _TlsIgmpSnpgQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 4),
    _TlsIgmpSnpgQuerierPortId_Type()
)
tlsIgmpSnpgQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierPortId.setStatus("current")
_TlsIgmpSnpgQuerierEncapValue_Type = TmnxEncapVal
_TlsIgmpSnpgQuerierEncapValue_Object = MibTableColumn
tlsIgmpSnpgQuerierEncapValue = _TlsIgmpSnpgQuerierEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 5),
    _TlsIgmpSnpgQuerierEncapValue_Type()
)
tlsIgmpSnpgQuerierEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierEncapValue.setStatus("current")
_TlsIgmpSnpgQuerierSdpId_Type = SdpId
_TlsIgmpSnpgQuerierSdpId_Object = MibTableColumn
tlsIgmpSnpgQuerierSdpId = _TlsIgmpSnpgQuerierSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 6),
    _TlsIgmpSnpgQuerierSdpId_Type()
)
tlsIgmpSnpgQuerierSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierSdpId.setStatus("current")
_TlsIgmpSnpgQuerierVcId_Type = TmnxVcIdOrNone
_TlsIgmpSnpgQuerierVcId_Object = MibTableColumn
tlsIgmpSnpgQuerierVcId = _TlsIgmpSnpgQuerierVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 7),
    _TlsIgmpSnpgQuerierVcId_Type()
)
tlsIgmpSnpgQuerierVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVcId.setStatus("current")
_TlsIgmpSnpgQuerierUpTime_Type = TimeTicks
_TlsIgmpSnpgQuerierUpTime_Object = MibTableColumn
tlsIgmpSnpgQuerierUpTime = _TlsIgmpSnpgQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 8),
    _TlsIgmpSnpgQuerierUpTime_Type()
)
tlsIgmpSnpgQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierUpTime.setStatus("current")
_TlsIgmpSnpgQuerierExpiryTime_Type = Unsigned32
_TlsIgmpSnpgQuerierExpiryTime_Object = MibTableColumn
tlsIgmpSnpgQuerierExpiryTime = _TlsIgmpSnpgQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 9),
    _TlsIgmpSnpgQuerierExpiryTime_Type()
)
tlsIgmpSnpgQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierExpiryTime.setUnits("seconds")
_TlsIgmpSnpgQuerierGenQueryIntvl_Type = Unsigned32
_TlsIgmpSnpgQuerierGenQueryIntvl_Object = MibTableColumn
tlsIgmpSnpgQuerierGenQueryIntvl = _TlsIgmpSnpgQuerierGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 10),
    _TlsIgmpSnpgQuerierGenQueryIntvl_Type()
)
tlsIgmpSnpgQuerierGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenQueryIntvl.setUnits("seconds")
_TlsIgmpSnpgQuerierGenRespIntvl_Type = Unsigned32
_TlsIgmpSnpgQuerierGenRespIntvl_Object = MibTableColumn
tlsIgmpSnpgQuerierGenRespIntvl = _TlsIgmpSnpgQuerierGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 11),
    _TlsIgmpSnpgQuerierGenRespIntvl_Type()
)
tlsIgmpSnpgQuerierGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenRespIntvl.setUnits("deci-seconds")
_TlsIgmpSnpgQuerierRobustCount_Type = Unsigned32
_TlsIgmpSnpgQuerierRobustCount_Object = MibTableColumn
tlsIgmpSnpgQuerierRobustCount = _TlsIgmpSnpgQuerierRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 12),
    _TlsIgmpSnpgQuerierRobustCount_Type()
)
tlsIgmpSnpgQuerierRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierRobustCount.setStatus("current")
_TlsIgmpSnpgQuerierVRtrId_Type = Unsigned32
_TlsIgmpSnpgQuerierVRtrId_Object = MibTableColumn
tlsIgmpSnpgQuerierVRtrId = _TlsIgmpSnpgQuerierVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 13),
    _TlsIgmpSnpgQuerierVRtrId_Type()
)
tlsIgmpSnpgQuerierVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVRtrId.setStatus("current")
_TlsIgmpSnpgQuerierIfIndex_Type = Unsigned32
_TlsIgmpSnpgQuerierIfIndex_Object = MibTableColumn
tlsIgmpSnpgQuerierIfIndex = _TlsIgmpSnpgQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 14),
    _TlsIgmpSnpgQuerierIfIndex_Type()
)
tlsIgmpSnpgQuerierIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierIfIndex.setStatus("current")
_TlsIgmpSnpgProxyGroupTable_Object = MibTable
tlsIgmpSnpgProxyGroupTable = _TlsIgmpSnpgProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupTable.setStatus("current")
_TlsIgmpSnpgProxyGroupEntry_Object = MibTableRow
tlsIgmpSnpgProxyGroupEntry = _TlsIgmpSnpgProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1)
)
tlsIgmpSnpgProxyGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupAddress"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupEntry.setStatus("current")
_TlsIgmpSnpgProxyGroupAddress_Type = IpAddress
_TlsIgmpSnpgProxyGroupAddress_Object = MibTableColumn
tlsIgmpSnpgProxyGroupAddress = _TlsIgmpSnpgProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1, 1),
    _TlsIgmpSnpgProxyGroupAddress_Type()
)
tlsIgmpSnpgProxyGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupAddress.setStatus("current")
_TlsIgmpSnpgProxyGroupFilterMode_Type = TmnxIgmpGroupFilterMode
_TlsIgmpSnpgProxyGroupFilterMode_Object = MibTableColumn
tlsIgmpSnpgProxyGroupFilterMode = _TlsIgmpSnpgProxyGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1, 2),
    _TlsIgmpSnpgProxyGroupFilterMode_Type()
)
tlsIgmpSnpgProxyGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupFilterMode.setStatus("current")
_TlsIgmpSnpgProxyGroupUpTime_Type = TimeTicks
_TlsIgmpSnpgProxyGroupUpTime_Object = MibTableColumn
tlsIgmpSnpgProxyGroupUpTime = _TlsIgmpSnpgProxyGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1, 3),
    _TlsIgmpSnpgProxyGroupUpTime_Type()
)
tlsIgmpSnpgProxyGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupUpTime.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcTable_Object = MibTable
tlsIgmpSnpgProxyGrpSrcTable = _TlsIgmpSnpgProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcTable.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcEntry_Object = MibTableRow
tlsIgmpSnpgProxyGrpSrcEntry = _TlsIgmpSnpgProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4, 1)
)
tlsIgmpSnpgProxyGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcEntry.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcAddr_Type = IpAddress
_TlsIgmpSnpgProxyGrpSrcAddr_Object = MibTableColumn
tlsIgmpSnpgProxyGrpSrcAddr = _TlsIgmpSnpgProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4, 1, 1),
    _TlsIgmpSnpgProxyGrpSrcAddr_Type()
)
tlsIgmpSnpgProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcAddr.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcUpTime_Type = TimeTicks
_TlsIgmpSnpgProxyGrpSrcUpTime_Object = MibTableColumn
tlsIgmpSnpgProxyGrpSrcUpTime = _TlsIgmpSnpgProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4, 1, 2),
    _TlsIgmpSnpgProxyGrpSrcUpTime_Type()
)
tlsIgmpSnpgProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcUpTime.setStatus("current")
_TlsIgmpSnpgMRouterTable_Object = MibTable
tlsIgmpSnpgMRouterTable = _TlsIgmpSnpgMRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterTable.setStatus("current")
_TlsIgmpSnpgMRouterEntry_Object = MibTableRow
tlsIgmpSnpgMRouterEntry = _TlsIgmpSnpgMRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1)
)
tlsIgmpSnpgMRouterEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterAddress"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterEntry.setStatus("current")
_TlsIgmpSnpgMRouterAddress_Type = IpAddress
_TlsIgmpSnpgMRouterAddress_Object = MibTableColumn
tlsIgmpSnpgMRouterAddress = _TlsIgmpSnpgMRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 1),
    _TlsIgmpSnpgMRouterAddress_Type()
)
tlsIgmpSnpgMRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterAddress.setStatus("current")
_TlsIgmpSnpgMRouterLocale_Type = AlxIgmpSnpgLocation
_TlsIgmpSnpgMRouterLocale_Object = MibTableColumn
tlsIgmpSnpgMRouterLocale = _TlsIgmpSnpgMRouterLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 2),
    _TlsIgmpSnpgMRouterLocale_Type()
)
tlsIgmpSnpgMRouterLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterLocale.setStatus("current")
_TlsIgmpSnpgMRouterPortId_Type = TmnxPortID
_TlsIgmpSnpgMRouterPortId_Object = MibTableColumn
tlsIgmpSnpgMRouterPortId = _TlsIgmpSnpgMRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 3),
    _TlsIgmpSnpgMRouterPortId_Type()
)
tlsIgmpSnpgMRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterPortId.setStatus("current")
_TlsIgmpSnpgMRouterEncapValue_Type = TmnxEncapVal
_TlsIgmpSnpgMRouterEncapValue_Object = MibTableColumn
tlsIgmpSnpgMRouterEncapValue = _TlsIgmpSnpgMRouterEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 4),
    _TlsIgmpSnpgMRouterEncapValue_Type()
)
tlsIgmpSnpgMRouterEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterEncapValue.setStatus("current")
_TlsIgmpSnpgMRouterSdpId_Type = SdpId
_TlsIgmpSnpgMRouterSdpId_Object = MibTableColumn
tlsIgmpSnpgMRouterSdpId = _TlsIgmpSnpgMRouterSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 5),
    _TlsIgmpSnpgMRouterSdpId_Type()
)
tlsIgmpSnpgMRouterSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterSdpId.setStatus("current")
_TlsIgmpSnpgMRouterVcId_Type = TmnxVcIdOrNone
_TlsIgmpSnpgMRouterVcId_Object = MibTableColumn
tlsIgmpSnpgMRouterVcId = _TlsIgmpSnpgMRouterVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 6),
    _TlsIgmpSnpgMRouterVcId_Type()
)
tlsIgmpSnpgMRouterVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVcId.setStatus("current")
_TlsIgmpSnpgMRouterVersion_Type = TmnxIgmpVersion
_TlsIgmpSnpgMRouterVersion_Object = MibTableColumn
tlsIgmpSnpgMRouterVersion = _TlsIgmpSnpgMRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 7),
    _TlsIgmpSnpgMRouterVersion_Type()
)
tlsIgmpSnpgMRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVersion.setStatus("current")
_TlsIgmpSnpgMRouterExpiryTime_Type = Unsigned32
_TlsIgmpSnpgMRouterExpiryTime_Object = MibTableColumn
tlsIgmpSnpgMRouterExpiryTime = _TlsIgmpSnpgMRouterExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 8),
    _TlsIgmpSnpgMRouterExpiryTime_Type()
)
tlsIgmpSnpgMRouterExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterExpiryTime.setUnits("seconds")
_TlsIgmpSnpgMRouterUpTime_Type = TimeTicks
_TlsIgmpSnpgMRouterUpTime_Object = MibTableColumn
tlsIgmpSnpgMRouterUpTime = _TlsIgmpSnpgMRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 9),
    _TlsIgmpSnpgMRouterUpTime_Type()
)
tlsIgmpSnpgMRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterUpTime.setStatus("current")
_TlsIgmpSnpgMRouterGenQueryIntvl_Type = Unsigned32
_TlsIgmpSnpgMRouterGenQueryIntvl_Object = MibTableColumn
tlsIgmpSnpgMRouterGenQueryIntvl = _TlsIgmpSnpgMRouterGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 10),
    _TlsIgmpSnpgMRouterGenQueryIntvl_Type()
)
tlsIgmpSnpgMRouterGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenQueryIntvl.setUnits("seconds")
_TlsIgmpSnpgMRouterGenRespIntvl_Type = Unsigned32
_TlsIgmpSnpgMRouterGenRespIntvl_Object = MibTableColumn
tlsIgmpSnpgMRouterGenRespIntvl = _TlsIgmpSnpgMRouterGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 11),
    _TlsIgmpSnpgMRouterGenRespIntvl_Type()
)
tlsIgmpSnpgMRouterGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenRespIntvl.setUnits("deci-seconds")
_TlsIgmpSnpgMRouterRobustCount_Type = Unsigned32
_TlsIgmpSnpgMRouterRobustCount_Object = MibTableColumn
tlsIgmpSnpgMRouterRobustCount = _TlsIgmpSnpgMRouterRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 12),
    _TlsIgmpSnpgMRouterRobustCount_Type()
)
tlsIgmpSnpgMRouterRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterRobustCount.setStatus("current")
_TlsIgmpSnpgMRouterVRtrId_Type = Unsigned32
_TlsIgmpSnpgMRouterVRtrId_Object = MibTableColumn
tlsIgmpSnpgMRouterVRtrId = _TlsIgmpSnpgMRouterVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 13),
    _TlsIgmpSnpgMRouterVRtrId_Type()
)
tlsIgmpSnpgMRouterVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVRtrId.setStatus("current")
_TlsIgmpSnpgMRouterIfIndex_Type = Unsigned32
_TlsIgmpSnpgMRouterIfIndex_Object = MibTableColumn
tlsIgmpSnpgMRouterIfIndex = _TlsIgmpSnpgMRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 14),
    _TlsIgmpSnpgMRouterIfIndex_Type()
)
tlsIgmpSnpgMRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterIfIndex.setStatus("current")
_AlxIgmpSnoopingSapObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapObjs = _AlxIgmpSnoopingSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2)
)
_SapIgmpSnpgConfigTable_Object = MibTable
sapIgmpSnpgConfigTable = _SapIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgConfigTable.setStatus("current")
_SapIgmpSnpgConfigEntry_Object = MibTableRow
sapIgmpSnpgConfigEntry = _SapIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1)
)
sapIgmpSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgConfigEntry.setStatus("current")


class _SapIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapIgmpSnpgCfgImportPlcy_Object = MibTableColumn
sapIgmpSnpgCfgImportPlcy = _SapIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 1),
    _SapIgmpSnpgCfgImportPlcy_Type()
)
sapIgmpSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgImportPlcy.setStatus("current")


class _SapIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):
    """Custom type sapIgmpSnpgCfgFastLeave based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SapIgmpSnpgCfgFastLeave_Type.__name__ = "AlxIgmpSnpgAdminState"
_SapIgmpSnpgCfgFastLeave_Object = MibTableColumn
sapIgmpSnpgCfgFastLeave = _SapIgmpSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 2),
    _SapIgmpSnpgCfgFastLeave_Type()
)
sapIgmpSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgFastLeave.setStatus("current")


class _SapIgmpSnpgCfgMRouter_Type(TruthValue):
    """Custom type sapIgmpSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SapIgmpSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SapIgmpSnpgCfgMRouter_Object = MibTableColumn
sapIgmpSnpgCfgMRouter = _SapIgmpSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 3),
    _SapIgmpSnpgCfgMRouter_Type()
)
sapIgmpSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMRouter.setStatus("current")


class _SapIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):
    """Custom type sapIgmpSnpgCfgSendQueries based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SapIgmpSnpgCfgSendQueries_Type.__name__ = "AlxIgmpSnpgAdminState"
_SapIgmpSnpgCfgSendQueries_Object = MibTableColumn
sapIgmpSnpgCfgSendQueries = _SapIgmpSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 4),
    _SapIgmpSnpgCfgSendQueries_Type()
)
sapIgmpSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgSendQueries.setStatus("current")


class _SapIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SapIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
sapIgmpSnpgCfgGenQueryIntvl = _SapIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 5),
    _SapIgmpSnpgCfgGenQueryIntvl_Type()
)
sapIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SapIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SapIgmpSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgQueryRespIntvl_Object = MibTableColumn
sapIgmpSnpgCfgQueryRespIntvl = _SapIgmpSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 6),
    _SapIgmpSnpgCfgQueryRespIntvl_Type()
)
sapIgmpSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SapIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SapIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgRobustCount_Object = MibTableColumn
sapIgmpSnpgCfgRobustCount = _SapIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 7),
    _SapIgmpSnpgCfgRobustCount_Type()
)
sapIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgRobustCount.setStatus("current")


class _SapIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SapIgmpSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgLastMembIntvl_Object = MibTableColumn
sapIgmpSnpgCfgLastMembIntvl = _SapIgmpSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 8),
    _SapIgmpSnpgCfgLastMembIntvl_Type()
)
sapIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _SapIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sapIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SapIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SapIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
sapIgmpSnpgCfgMaxNbrGrps = _SapIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 9),
    _SapIgmpSnpgCfgMaxNbrGrps_Type()
)
sapIgmpSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMaxNbrGrps.setStatus("current")


class _SapIgmpSnpgCfgMvrFromVplsId_Type(TmnxServId):
    """Custom type sapIgmpSnpgCfgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_SapIgmpSnpgCfgMvrFromVplsId_Type.__name__ = "TmnxServId"
_SapIgmpSnpgCfgMvrFromVplsId_Object = MibTableColumn
sapIgmpSnpgCfgMvrFromVplsId = _SapIgmpSnpgCfgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 10),
    _SapIgmpSnpgCfgMvrFromVplsId_Type()
)
sapIgmpSnpgCfgMvrFromVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMvrFromVplsId.setStatus("current")


class _SapIgmpSnpgCfgMvrToSapPortId_Type(TmnxPortID):
    """Custom type sapIgmpSnpgCfgMvrToSapPortId based on TmnxPortID"""
    defaultValue = 0


_SapIgmpSnpgCfgMvrToSapPortId_Type.__name__ = "TmnxPortID"
_SapIgmpSnpgCfgMvrToSapPortId_Object = MibTableColumn
sapIgmpSnpgCfgMvrToSapPortId = _SapIgmpSnpgCfgMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 11),
    _SapIgmpSnpgCfgMvrToSapPortId_Type()
)
sapIgmpSnpgCfgMvrToSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMvrToSapPortId.setStatus("current")


class _SapIgmpSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):
    """Custom type sapIgmpSnpgCfgMvrToSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_SapIgmpSnpgCfgMvrToSapEncapVal_Type.__name__ = "TmnxEncapVal"
_SapIgmpSnpgCfgMvrToSapEncapVal_Object = MibTableColumn
sapIgmpSnpgCfgMvrToSapEncapVal = _SapIgmpSnpgCfgMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 12),
    _SapIgmpSnpgCfgMvrToSapEncapVal_Type()
)
sapIgmpSnpgCfgMvrToSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMvrToSapEncapVal.setStatus("current")


class _SapIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):
    """Custom type sapIgmpSnpgCfgVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_SapIgmpSnpgCfgVersion_Type.__name__ = "TmnxIgmpVersion"
_SapIgmpSnpgCfgVersion_Object = MibTableColumn
sapIgmpSnpgCfgVersion = _SapIgmpSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 13),
    _SapIgmpSnpgCfgVersion_Type()
)
sapIgmpSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgVersion.setStatus("current")


class _SapIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapIgmpSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapIgmpSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapIgmpSnpgCfgMcacPolicyName_Object = MibTableColumn
sapIgmpSnpgCfgMcacPolicyName = _SapIgmpSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 14),
    _SapIgmpSnpgCfgMcacPolicyName_Type()
)
sapIgmpSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacPolicyName.setStatus("current")


class _SapIgmpSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sapIgmpSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SapIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SapIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
sapIgmpSnpgCfgMcacUnconstBW = _SapIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 15),
    _SapIgmpSnpgCfgMcacUnconstBW_Type()
)
sapIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacUnconstBW.setUnits("kbps")


class _SapIgmpSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):
    """Custom type sapIgmpSnpgCfgMcacConstAdmSt based on TmnxAdminState"""
    defaultValue = 2


_SapIgmpSnpgCfgMcacConstAdmSt_Type.__name__ = "TmnxAdminState"
_SapIgmpSnpgCfgMcacConstAdmSt_Object = MibTableColumn
sapIgmpSnpgCfgMcacConstAdmSt = _SapIgmpSnpgCfgMcacConstAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 16),
    _SapIgmpSnpgCfgMcacConstAdmSt_Type()
)
sapIgmpSnpgCfgMcacConstAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacConstAdmSt.setStatus("current")


class _SapIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sapIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SapIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SapIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sapIgmpSnpgCfgMcacPrRsvMndBW = _SapIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 17),
    _SapIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
sapIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kbps")
_SapIgmpSnpgCfgMcacinUseMandBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacinUseMandBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacinUseMandBw = _SapIgmpSnpgCfgMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 18),
    _SapIgmpSnpgCfgMcacinUseMandBw_Type()
)
sapIgmpSnpgCfgMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseMandBw.setUnits("kbps")
_SapIgmpSnpgCfgMcacinUseOpnlBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacinUseOpnlBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacinUseOpnlBw = _SapIgmpSnpgCfgMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 19),
    _SapIgmpSnpgCfgMcacinUseOpnlBw_Type()
)
sapIgmpSnpgCfgMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseOpnlBw.setUnits("kbps")
_SapIgmpSnpgCfgMcacAvailMandBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacAvailMandBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacAvailMandBw = _SapIgmpSnpgCfgMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 20),
    _SapIgmpSnpgCfgMcacAvailMandBw_Type()
)
sapIgmpSnpgCfgMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailMandBw.setUnits("kbps")
_SapIgmpSnpgCfgMcacAvailOpnlBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacAvailOpnlBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacAvailOpnlBw = _SapIgmpSnpgCfgMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 21),
    _SapIgmpSnpgCfgMcacAvailOpnlBw_Type()
)
sapIgmpSnpgCfgMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailOpnlBw.setUnits("kbps")
_SapIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_SapIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
sapIgmpSnpgCfgMcacValInTrans = _SapIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 22),
    _SapIgmpSnpgCfgMcacValInTrans_Type()
)
sapIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacValInTrans.setStatus("current")
_SapIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_SapIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
sapIgmpSnpgCfgLastChangeTime = _SapIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 23),
    _SapIgmpSnpgCfgLastChangeTime_Type()
)
sapIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgLastChangeTime.setStatus("current")


class _SapIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMaxNbrSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SapIgmpSnpgCfgMaxNbrSrcs_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMaxNbrSrcs_Object = MibTableColumn
sapIgmpSnpgCfgMaxNbrSrcs = _SapIgmpSnpgCfgMaxNbrSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 24),
    _SapIgmpSnpgCfgMaxNbrSrcs_Type()
)
sapIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMaxNbrSrcs.setStatus("current")


class _SapIgmpSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sapIgmpSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SapIgmpSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SapIgmpSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sapIgmpSnpgCfgDisRtrAlertChk = _SapIgmpSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 25),
    _SapIgmpSnpgCfgDisRtrAlertChk_Type()
)
sapIgmpSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgDisRtrAlertChk.setStatus("current")


class _SapIgmpSnpgCfgMaxNbrGrpSrcs_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMaxNbrGrpSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_SapIgmpSnpgCfgMaxNbrGrpSrcs_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMaxNbrGrpSrcs_Object = MibTableColumn
sapIgmpSnpgCfgMaxNbrGrpSrcs = _SapIgmpSnpgCfgMaxNbrGrpSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 26),
    _SapIgmpSnpgCfgMaxNbrGrpSrcs_Type()
)
sapIgmpSnpgCfgMaxNbrGrpSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMaxNbrGrpSrcs.setStatus("current")


class _SapIgmpSnpgCfgMcacUseLagPortWt_Type(TruthValue):
    """Custom type sapIgmpSnpgCfgMcacUseLagPortWt based on TruthValue"""
    defaultValue = 2


_SapIgmpSnpgCfgMcacUseLagPortWt_Type.__name__ = "TruthValue"
_SapIgmpSnpgCfgMcacUseLagPortWt_Object = MibTableColumn
sapIgmpSnpgCfgMcacUseLagPortWt = _SapIgmpSnpgCfgMcacUseLagPortWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 27),
    _SapIgmpSnpgCfgMcacUseLagPortWt_Type()
)
sapIgmpSnpgCfgMcacUseLagPortWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacUseLagPortWt.setStatus("current")
_SapIgmpSnpgGroupTable_Object = MibTable
sapIgmpSnpgGroupTable = _SapIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGroupTable.setStatus("current")
_SapIgmpSnpgGroupEntry_Object = MibTableRow
sapIgmpSnpgGroupEntry = _SapIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1)
)
sapIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGroupEntry.setStatus("current")
_SapIgmpSnpgGrpAddress_Type = IpAddress
_SapIgmpSnpgGrpAddress_Object = MibTableColumn
sapIgmpSnpgGrpAddress = _SapIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 1),
    _SapIgmpSnpgGrpAddress_Type()
)
sapIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpAddress.setStatus("current")
_SapIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_SapIgmpSnpgGrpType_Object = MibTableColumn
sapIgmpSnpgGrpType = _SapIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 2),
    _SapIgmpSnpgGrpType_Type()
)
sapIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpType.setStatus("current")
_SapIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_SapIgmpSnpgGrpFilterMode_Object = MibTableColumn
sapIgmpSnpgGrpFilterMode = _SapIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 3),
    _SapIgmpSnpgGrpFilterMode_Type()
)
sapIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpFilterMode.setStatus("current")
_SapIgmpSnpgGrpUpTime_Type = TimeTicks
_SapIgmpSnpgGrpUpTime_Object = MibTableColumn
sapIgmpSnpgGrpUpTime = _SapIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 4),
    _SapIgmpSnpgGrpUpTime_Type()
)
sapIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpUpTime.setStatus("current")
_SapIgmpSnpgGrpExpiryTime_Type = Unsigned32
_SapIgmpSnpgGrpExpiryTime_Object = MibTableColumn
sapIgmpSnpgGrpExpiryTime = _SapIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 5),
    _SapIgmpSnpgGrpExpiryTime_Type()
)
sapIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpExpiryTime.setUnits("seconds")
_SapIgmpSnpgGrpCompatMode_Type = Unsigned32
_SapIgmpSnpgGrpCompatMode_Object = MibTableColumn
sapIgmpSnpgGrpCompatMode = _SapIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 6),
    _SapIgmpSnpgGrpCompatMode_Type()
)
sapIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpCompatMode.setStatus("current")
_SapIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_SapIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
sapIgmpSnpgGrpV1HostExpTime = _SapIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 7),
    _SapIgmpSnpgGrpV1HostExpTime_Type()
)
sapIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_SapIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_SapIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
sapIgmpSnpgGrpV2HostExpTime = _SapIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 8),
    _SapIgmpSnpgGrpV2HostExpTime_Type()
)
sapIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_SapIgmpSnpgGrpMvrFromVplsId_Type = TmnxServId
_SapIgmpSnpgGrpMvrFromVplsId_Object = MibTableColumn
sapIgmpSnpgGrpMvrFromVplsId = _SapIgmpSnpgGrpMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 9),
    _SapIgmpSnpgGrpMvrFromVplsId_Type()
)
sapIgmpSnpgGrpMvrFromVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpMvrFromVplsId.setStatus("current")
_SapIgmpSnpgGrpMvrToSapPortId_Type = TmnxPortID
_SapIgmpSnpgGrpMvrToSapPortId_Object = MibTableColumn
sapIgmpSnpgGrpMvrToSapPortId = _SapIgmpSnpgGrpMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 10),
    _SapIgmpSnpgGrpMvrToSapPortId_Type()
)
sapIgmpSnpgGrpMvrToSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpMvrToSapPortId.setStatus("current")
_SapIgmpSnpgGrpMvrToSapEncapVal_Type = TmnxEncapVal
_SapIgmpSnpgGrpMvrToSapEncapVal_Object = MibTableColumn
sapIgmpSnpgGrpMvrToSapEncapVal = _SapIgmpSnpgGrpMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 11),
    _SapIgmpSnpgGrpMvrToSapEncapVal_Type()
)
sapIgmpSnpgGrpMvrToSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpMvrToSapEncapVal.setStatus("current")
_SapIgmpSnpgGrpSrcTable_Object = MibTable
sapIgmpSnpgGrpSrcTable = _SapIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcTable.setStatus("current")
_SapIgmpSnpgGrpSrcEntry_Object = MibTableRow
sapIgmpSnpgGrpSrcEntry = _SapIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1)
)
sapIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcEntry.setStatus("current")
_SapIgmpSnpgGrpSrcAddr_Type = IpAddress
_SapIgmpSnpgGrpSrcAddr_Object = MibTableColumn
sapIgmpSnpgGrpSrcAddr = _SapIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 1),
    _SapIgmpSnpgGrpSrcAddr_Type()
)
sapIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcAddr.setStatus("current")
_SapIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_SapIgmpSnpgGrpSrcType_Object = MibTableColumn
sapIgmpSnpgGrpSrcType = _SapIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 2),
    _SapIgmpSnpgGrpSrcType_Type()
)
sapIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcType.setStatus("current")
_SapIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_SapIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
sapIgmpSnpgGrpSrcUpTime = _SapIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 3),
    _SapIgmpSnpgGrpSrcUpTime_Type()
)
sapIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcUpTime.setStatus("current")
_SapIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_SapIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
sapIgmpSnpgGrpSrcExpiryTime = _SapIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 4),
    _SapIgmpSnpgGrpSrcExpiryTime_Type()
)
sapIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")
_SapIgmpSnpgStaticGrpSrcTable_Object = MibTable
sapIgmpSnpgStaticGrpSrcTable = _SapIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGrpSrcTable.setStatus("current")
_SapIgmpSnpgStaticGrpSrcEntry_Object = MibTableRow
sapIgmpSnpgStaticGrpSrcEntry = _SapIgmpSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1)
)
sapIgmpSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticGroupAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGrpSrcEntry.setStatus("current")
_SapIgmpSnpgStaticGroupAddr_Type = IpAddress
_SapIgmpSnpgStaticGroupAddr_Object = MibTableColumn
sapIgmpSnpgStaticGroupAddr = _SapIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 1),
    _SapIgmpSnpgStaticGroupAddr_Type()
)
sapIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGroupAddr.setStatus("current")
_SapIgmpSnpgStaticSourceAddr_Type = IpAddress
_SapIgmpSnpgStaticSourceAddr_Object = MibTableColumn
sapIgmpSnpgStaticSourceAddr = _SapIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 2),
    _SapIgmpSnpgStaticSourceAddr_Type()
)
sapIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticSourceAddr.setStatus("current")
_SapIgmpSnpgStaticRowstatus_Type = RowStatus
_SapIgmpSnpgStaticRowstatus_Object = MibTableColumn
sapIgmpSnpgStaticRowstatus = _SapIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 3),
    _SapIgmpSnpgStaticRowstatus_Type()
)
sapIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticRowstatus.setStatus("current")
_SapIgmpSnpgStaticLastChangeTime_Type = TimeStamp
_SapIgmpSnpgStaticLastChangeTime_Object = MibTableColumn
sapIgmpSnpgStaticLastChangeTime = _SapIgmpSnpgStaticLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 4),
    _SapIgmpSnpgStaticLastChangeTime_Type()
)
sapIgmpSnpgStaticLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticLastChangeTime.setStatus("current")
_SapIgmpSnpgStatsTable_Object = MibTable
sapIgmpSnpgStatsTable = _SapIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStatsTable.setStatus("current")
_SapIgmpSnpgStatsEntry_Object = MibTableRow
sapIgmpSnpgStatsEntry = _SapIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1)
)
sapIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStatsEntry.setStatus("current")
_SapIgmpSnpgTxGenQueries_Type = Counter32
_SapIgmpSnpgTxGenQueries_Object = MibTableColumn
sapIgmpSnpgTxGenQueries = _SapIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 1),
    _SapIgmpSnpgTxGenQueries_Type()
)
sapIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxGenQueries.setStatus("current")
_SapIgmpSnpgTxGrpSpecQueries_Type = Counter32
_SapIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
sapIgmpSnpgTxGrpSpecQueries = _SapIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 2),
    _SapIgmpSnpgTxGrpSpecQueries_Type()
)
sapIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxGrpSpecQueries.setStatus("current")
_SapIgmpSnpgTxSrcSpecQueries_Type = Counter32
_SapIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
sapIgmpSnpgTxSrcSpecQueries = _SapIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 3),
    _SapIgmpSnpgTxSrcSpecQueries_Type()
)
sapIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxSrcSpecQueries.setStatus("current")
_SapIgmpSnpgTxV1Reports_Type = Counter32
_SapIgmpSnpgTxV1Reports_Object = MibTableColumn
sapIgmpSnpgTxV1Reports = _SapIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 4),
    _SapIgmpSnpgTxV1Reports_Type()
)
sapIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV1Reports.setStatus("current")
_SapIgmpSnpgTxV2Reports_Type = Counter32
_SapIgmpSnpgTxV2Reports_Object = MibTableColumn
sapIgmpSnpgTxV2Reports = _SapIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 5),
    _SapIgmpSnpgTxV2Reports_Type()
)
sapIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV2Reports.setStatus("current")
_SapIgmpSnpgTxV3Reports_Type = Counter32
_SapIgmpSnpgTxV3Reports_Object = MibTableColumn
sapIgmpSnpgTxV3Reports = _SapIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 6),
    _SapIgmpSnpgTxV3Reports_Type()
)
sapIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV3Reports.setStatus("current")
_SapIgmpSnpgTxV2Leaves_Type = Counter32
_SapIgmpSnpgTxV2Leaves_Object = MibTableColumn
sapIgmpSnpgTxV2Leaves = _SapIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 7),
    _SapIgmpSnpgTxV2Leaves_Type()
)
sapIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV2Leaves.setStatus("current")
_SapIgmpSnpgRxGenQueries_Type = Counter32
_SapIgmpSnpgRxGenQueries_Object = MibTableColumn
sapIgmpSnpgRxGenQueries = _SapIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 8),
    _SapIgmpSnpgRxGenQueries_Type()
)
sapIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxGenQueries.setStatus("current")
_SapIgmpSnpgRxGrpSpecQueries_Type = Counter32
_SapIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
sapIgmpSnpgRxGrpSpecQueries = _SapIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 9),
    _SapIgmpSnpgRxGrpSpecQueries_Type()
)
sapIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxGrpSpecQueries.setStatus("current")
_SapIgmpSnpgRxSrcSpecQueries_Type = Counter32
_SapIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
sapIgmpSnpgRxSrcSpecQueries = _SapIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 10),
    _SapIgmpSnpgRxSrcSpecQueries_Type()
)
sapIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxSrcSpecQueries.setStatus("current")
_SapIgmpSnpgRxV1Reports_Type = Counter32
_SapIgmpSnpgRxV1Reports_Object = MibTableColumn
sapIgmpSnpgRxV1Reports = _SapIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 11),
    _SapIgmpSnpgRxV1Reports_Type()
)
sapIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV1Reports.setStatus("current")
_SapIgmpSnpgRxV2Reports_Type = Counter32
_SapIgmpSnpgRxV2Reports_Object = MibTableColumn
sapIgmpSnpgRxV2Reports = _SapIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 12),
    _SapIgmpSnpgRxV2Reports_Type()
)
sapIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV2Reports.setStatus("current")
_SapIgmpSnpgRxV3Reports_Type = Counter32
_SapIgmpSnpgRxV3Reports_Object = MibTableColumn
sapIgmpSnpgRxV3Reports = _SapIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 13),
    _SapIgmpSnpgRxV3Reports_Type()
)
sapIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV3Reports.setStatus("current")
_SapIgmpSnpgRxV2Leaves_Type = Counter32
_SapIgmpSnpgRxV2Leaves_Object = MibTableColumn
sapIgmpSnpgRxV2Leaves = _SapIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 14),
    _SapIgmpSnpgRxV2Leaves_Type()
)
sapIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV2Leaves.setStatus("current")
_SapIgmpSnpgRxUnknownType_Type = Counter32
_SapIgmpSnpgRxUnknownType_Object = MibTableColumn
sapIgmpSnpgRxUnknownType = _SapIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 15),
    _SapIgmpSnpgRxUnknownType_Type()
)
sapIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxUnknownType.setStatus("current")
_SapIgmpSnpgFwdGenQueries_Type = Counter32
_SapIgmpSnpgFwdGenQueries_Object = MibTableColumn
sapIgmpSnpgFwdGenQueries = _SapIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 16),
    _SapIgmpSnpgFwdGenQueries_Type()
)
sapIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdGenQueries.setStatus("current")
_SapIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_SapIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
sapIgmpSnpgFwdGrpSpecQueries = _SapIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 17),
    _SapIgmpSnpgFwdGrpSpecQueries_Type()
)
sapIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_SapIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_SapIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
sapIgmpSnpgFwdSrcSpecQueries = _SapIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 18),
    _SapIgmpSnpgFwdSrcSpecQueries_Type()
)
sapIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_SapIgmpSnpgFwdV1Reports_Type = Counter32
_SapIgmpSnpgFwdV1Reports_Object = MibTableColumn
sapIgmpSnpgFwdV1Reports = _SapIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 19),
    _SapIgmpSnpgFwdV1Reports_Type()
)
sapIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV1Reports.setStatus("current")
_SapIgmpSnpgFwdV2Reports_Type = Counter32
_SapIgmpSnpgFwdV2Reports_Object = MibTableColumn
sapIgmpSnpgFwdV2Reports = _SapIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 20),
    _SapIgmpSnpgFwdV2Reports_Type()
)
sapIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV2Reports.setStatus("current")
_SapIgmpSnpgFwdV3Reports_Type = Counter32
_SapIgmpSnpgFwdV3Reports_Object = MibTableColumn
sapIgmpSnpgFwdV3Reports = _SapIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 21),
    _SapIgmpSnpgFwdV3Reports_Type()
)
sapIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV3Reports.setStatus("current")
_SapIgmpSnpgFwdV2Leaves_Type = Counter32
_SapIgmpSnpgFwdV2Leaves_Object = MibTableColumn
sapIgmpSnpgFwdV2Leaves = _SapIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 22),
    _SapIgmpSnpgFwdV2Leaves_Type()
)
sapIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV2Leaves.setStatus("current")
_SapIgmpSnpgFwdUnknownType_Type = Counter32
_SapIgmpSnpgFwdUnknownType_Object = MibTableColumn
sapIgmpSnpgFwdUnknownType = _SapIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 23),
    _SapIgmpSnpgFwdUnknownType_Type()
)
sapIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdUnknownType.setStatus("current")
_SapIgmpSnpgRxBadLenPkts_Type = Counter32
_SapIgmpSnpgRxBadLenPkts_Object = MibTableColumn
sapIgmpSnpgRxBadLenPkts = _SapIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 24),
    _SapIgmpSnpgRxBadLenPkts_Type()
)
sapIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadLenPkts.setStatus("current")
_SapIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_SapIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
sapIgmpSnpgRxBadIpChksmPkts = _SapIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 25),
    _SapIgmpSnpgRxBadIpChksmPkts_Type()
)
sapIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_SapIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_SapIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
sapIgmpSnpgRxBadIgmpChksmPkts = _SapIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 26),
    _SapIgmpSnpgRxBadIgmpChksmPkts_Type()
)
sapIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_SapIgmpSnpgRxBadEncodedPkts_Type = Counter32
_SapIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
sapIgmpSnpgRxBadEncodedPkts = _SapIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 27),
    _SapIgmpSnpgRxBadEncodedPkts_Type()
)
sapIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadEncodedPkts.setStatus("current")
_SapIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_SapIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sapIgmpSnpgRxNoRtrAlertPkts = _SapIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 28),
    _SapIgmpSnpgRxNoRtrAlertPkts_Type()
)
sapIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_SapIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_SapIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sapIgmpSnpgRxZeroSrcAdrPkts = _SapIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 29),
    _SapIgmpSnpgRxZeroSrcAdrPkts_Type()
)
sapIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_SapIgmpSnpgSendQueryCfgDrops_Type = Counter32
_SapIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
sapIgmpSnpgSendQueryCfgDrops = _SapIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 30),
    _SapIgmpSnpgSendQueryCfgDrops_Type()
)
sapIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgSendQueryCfgDrops.setStatus("current")
_SapIgmpSnpgImportPolicyDrops_Type = Counter32
_SapIgmpSnpgImportPolicyDrops_Object = MibTableColumn
sapIgmpSnpgImportPolicyDrops = _SapIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 31),
    _SapIgmpSnpgImportPolicyDrops_Type()
)
sapIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgImportPolicyDrops.setStatus("current")
_SapIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_SapIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
sapIgmpSnpgMaxNumGroupsDrops = _SapIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 32),
    _SapIgmpSnpgMaxNumGroupsDrops_Type()
)
sapIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_SapIgmpSnpgMvrFromVplsCfgDrops_Type = Counter32
_SapIgmpSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
sapIgmpSnpgMvrFromVplsCfgDrops = _SapIgmpSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 33),
    _SapIgmpSnpgMvrFromVplsCfgDrops_Type()
)
sapIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMvrFromVplsCfgDrops.setStatus("current")
_SapIgmpSnpgMvrToSapCfgDrops_Type = Counter32
_SapIgmpSnpgMvrToSapCfgDrops_Object = MibTableColumn
sapIgmpSnpgMvrToSapCfgDrops = _SapIgmpSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 34),
    _SapIgmpSnpgMvrToSapCfgDrops_Type()
)
sapIgmpSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMvrToSapCfgDrops.setStatus("current")
_SapIgmpSnpgRxWrongVersionPkts_Type = Counter32
_SapIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
sapIgmpSnpgRxWrongVersionPkts = _SapIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 35),
    _SapIgmpSnpgRxWrongVersionPkts_Type()
)
sapIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxWrongVersionPkts.setStatus("current")
_SapIgmpSnpgMcacPolicyDrops_Type = Counter32
_SapIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
sapIgmpSnpgMcacPolicyDrops = _SapIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 36),
    _SapIgmpSnpgMcacPolicyDrops_Type()
)
sapIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacPolicyDrops.setStatus("current")
_SapIgmpSnpgMcsFailures_Type = Counter32
_SapIgmpSnpgMcsFailures_Object = MibTableColumn
sapIgmpSnpgMcsFailures = _SapIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 37),
    _SapIgmpSnpgMcsFailures_Type()
)
sapIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcsFailures.setStatus("current")
_SapIgmpSnpgRxLocalScopePkts_Type = Counter32
_SapIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
sapIgmpSnpgRxLocalScopePkts = _SapIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 38),
    _SapIgmpSnpgRxLocalScopePkts_Type()
)
sapIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxLocalScopePkts.setStatus("current")
_SapIgmpSnpgRxRsvdScopePkts_Type = Counter32
_SapIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
sapIgmpSnpgRxRsvdScopePkts = _SapIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 39),
    _SapIgmpSnpgRxRsvdScopePkts_Type()
)
sapIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxRsvdScopePkts.setStatus("current")
_SapIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_SapIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
sapIgmpSnpgMaxNumSourcesDrops = _SapIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 40),
    _SapIgmpSnpgMaxNumSourcesDrops_Type()
)
sapIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_SapIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_SapIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
sapIgmpSnpgMaxNumGrpSrcsDrops = _SapIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 41),
    _SapIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
sapIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_SapIgmpSnpgMcacLevelTable_Object = MibTable
sapIgmpSnpgMcacLevelTable = _SapIgmpSnpgMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLevelTable.setStatus("current")
_SapIgmpSnpgMcacLevelEntry_Object = MibTableRow
sapIgmpSnpgMcacLevelEntry = _SapIgmpSnpgMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1)
)
sapIgmpSnpgMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLevelEntry.setStatus("current")
_SapIgmpSnpgCfgMcacLevelRowStat_Type = RowStatus
_SapIgmpSnpgCfgMcacLevelRowStat_Object = MibTableColumn
sapIgmpSnpgCfgMcacLevelRowStat = _SapIgmpSnpgCfgMcacLevelRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1, 1),
    _SapIgmpSnpgCfgMcacLevelRowStat_Type()
)
sapIgmpSnpgCfgMcacLevelRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelRowStat.setStatus("current")


class _SapIgmpSnpgCfgMcacLevelBW_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_SapIgmpSnpgCfgMcacLevelBW_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMcacLevelBW_Object = MibTableColumn
sapIgmpSnpgCfgMcacLevelBW = _SapIgmpSnpgCfgMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1, 2),
    _SapIgmpSnpgCfgMcacLevelBW_Type()
)
sapIgmpSnpgCfgMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelBW.setUnits("kbps")
_SapIgmpSnpgCfgMcacLevelLastChngT_Type = TimeStamp
_SapIgmpSnpgCfgMcacLevelLastChngT_Object = MibTableColumn
sapIgmpSnpgCfgMcacLevelLastChngT = _SapIgmpSnpgCfgMcacLevelLastChngT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1, 3),
    _SapIgmpSnpgCfgMcacLevelLastChngT_Type()
)
sapIgmpSnpgCfgMcacLevelLastChngT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelLastChngT.setStatus("current")
_SapIgmpSnpgMcacLagTable_Object = MibTable
sapIgmpSnpgMcacLagTable = _SapIgmpSnpgMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLagTable.setStatus("current")
_SapIgmpSnpgMcacLagEntry_Object = MibTableRow
sapIgmpSnpgMcacLagEntry = _SapIgmpSnpgMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1)
)
sapIgmpSnpgMcacLagEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLagEntry.setStatus("current")
_SapIgmpSnpgCfgMcacLagRowStat_Type = RowStatus
_SapIgmpSnpgCfgMcacLagRowStat_Object = MibTableColumn
sapIgmpSnpgCfgMcacLagRowStat = _SapIgmpSnpgCfgMcacLagRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1, 1),
    _SapIgmpSnpgCfgMcacLagRowStat_Type()
)
sapIgmpSnpgCfgMcacLagRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLagRowStat.setStatus("current")


class _SapIgmpSnpgCfgMcacLagLevel_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SapIgmpSnpgCfgMcacLagLevel_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMcacLagLevel_Object = MibTableColumn
sapIgmpSnpgCfgMcacLagLevel = _SapIgmpSnpgCfgMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1, 2),
    _SapIgmpSnpgCfgMcacLagLevel_Type()
)
sapIgmpSnpgCfgMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLagLevel.setStatus("current")
_SapIgmpSnpgCfgMcacLagLastChangeT_Type = TimeStamp
_SapIgmpSnpgCfgMcacLagLastChangeT_Object = MibTableColumn
sapIgmpSnpgCfgMcacLagLastChangeT = _SapIgmpSnpgCfgMcacLagLastChangeT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1, 3),
    _SapIgmpSnpgCfgMcacLagLastChangeT_Type()
)
sapIgmpSnpgCfgMcacLagLastChangeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLagLastChangeT.setStatus("current")
_AlxIgmpSnoopingSdpBindObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBindObjs = _AlxIgmpSnoopingSdpBindObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3)
)
_SdpBindIgmpSnpgConfigTable_Object = MibTable
sdpBindIgmpSnpgConfigTable = _SdpBindIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgConfigTable.setStatus("current")
_SdpBindIgmpSnpgConfigEntry_Object = MibTableRow
sdpBindIgmpSnpgConfigEntry = _SdpBindIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1)
)
sdpBindIgmpSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgConfigEntry.setStatus("current")


class _SdpBndIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndIgmpSnpgCfgImportPlcy_Object = MibTableColumn
sdpBndIgmpSnpgCfgImportPlcy = _SdpBndIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 1),
    _SdpBndIgmpSnpgCfgImportPlcy_Type()
)
sdpBndIgmpSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgImportPlcy.setStatus("current")


class _SdpBndIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):
    """Custom type sdpBndIgmpSnpgCfgFastLeave based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgFastLeave_Type.__name__ = "AlxIgmpSnpgAdminState"
_SdpBndIgmpSnpgCfgFastLeave_Object = MibTableColumn
sdpBndIgmpSnpgCfgFastLeave = _SdpBndIgmpSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 2),
    _SdpBndIgmpSnpgCfgFastLeave_Type()
)
sdpBndIgmpSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgFastLeave.setStatus("current")


class _SdpBndIgmpSnpgCfgMRouter_Type(TruthValue):
    """Custom type sdpBndIgmpSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SdpBndIgmpSnpgCfgMRouter_Object = MibTableColumn
sdpBndIgmpSnpgCfgMRouter = _SdpBndIgmpSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 3),
    _SdpBndIgmpSnpgCfgMRouter_Type()
)
sdpBndIgmpSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMRouter.setStatus("current")


class _SdpBndIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):
    """Custom type sdpBndIgmpSnpgCfgSendQueries based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgSendQueries_Type.__name__ = "AlxIgmpSnpgAdminState"
_SdpBndIgmpSnpgCfgSendQueries_Object = MibTableColumn
sdpBndIgmpSnpgCfgSendQueries = _SdpBndIgmpSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 4),
    _SdpBndIgmpSnpgCfgSendQueries_Type()
)
sdpBndIgmpSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgSendQueries.setStatus("current")


class _SdpBndIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SdpBndIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
sdpBndIgmpSnpgCfgGenQueryIntvl = _SdpBndIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 5),
    _SdpBndIgmpSnpgCfgGenQueryIntvl_Type()
)
sdpBndIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SdpBndIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SdpBndIgmpSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgQueryRespIntvl_Object = MibTableColumn
sdpBndIgmpSnpgCfgQueryRespIntvl = _SdpBndIgmpSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 6),
    _SdpBndIgmpSnpgCfgQueryRespIntvl_Type()
)
sdpBndIgmpSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SdpBndIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SdpBndIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgRobustCount_Object = MibTableColumn
sdpBndIgmpSnpgCfgRobustCount = _SdpBndIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 7),
    _SdpBndIgmpSnpgCfgRobustCount_Type()
)
sdpBndIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgRobustCount.setStatus("current")


class _SdpBndIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SdpBndIgmpSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgLastMembIntvl_Object = MibTableColumn
sdpBndIgmpSnpgCfgLastMembIntvl = _SdpBndIgmpSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 8),
    _SdpBndIgmpSnpgCfgLastMembIntvl_Type()
)
sdpBndIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _SdpBndIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SdpBndIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrGrps = _SdpBndIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 9),
    _SdpBndIgmpSnpgCfgMaxNbrGrps_Type()
)
sdpBndIgmpSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrGrps.setStatus("current")


class _SdpBndIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):
    """Custom type sdpBndIgmpSnpgCfgVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_SdpBndIgmpSnpgCfgVersion_Type.__name__ = "TmnxIgmpVersion"
_SdpBndIgmpSnpgCfgVersion_Object = MibTableColumn
sdpBndIgmpSnpgCfgVersion = _SdpBndIgmpSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 10),
    _SdpBndIgmpSnpgCfgVersion_Type()
)
sdpBndIgmpSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgVersion.setStatus("current")


class _SdpBndIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndIgmpSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndIgmpSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndIgmpSnpgCfgMcacPolicyName_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacPolicyName = _SdpBndIgmpSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 11),
    _SdpBndIgmpSnpgCfgMcacPolicyName_Type()
)
sdpBndIgmpSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPolicyName.setStatus("current")


class _SdpBndIgmpSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacUnconstBW = _SdpBndIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 12),
    _SdpBndIgmpSnpgCfgMcacUnconstBW_Type()
)
sdpBndIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacUnconstBW.setUnits("kbps")


class _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacPrRsvMndBW = _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 13),
    _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseMndBw = _SdpBndIgmpSnpgCfgMcacinUseMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 14),
    _SdpBndIgmpSnpgCfgMcacinUseMndBw_Type()
)
sdpBndIgmpSnpgCfgMcacinUseMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseMndBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseOplBw = _SdpBndIgmpSnpgCfgMcacinUseOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 15),
    _SdpBndIgmpSnpgCfgMcacinUseOplBw_Type()
)
sdpBndIgmpSnpgCfgMcacinUseOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseOplBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailMndBw = _SdpBndIgmpSnpgCfgMcacAvailMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 16),
    _SdpBndIgmpSnpgCfgMcacAvailMndBw_Type()
)
sdpBndIgmpSnpgCfgMcacAvailMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailMndBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailOplBw = _SdpBndIgmpSnpgCfgMcacAvailOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 17),
    _SdpBndIgmpSnpgCfgMcacAvailOplBw_Type()
)
sdpBndIgmpSnpgCfgMcacAvailOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailOplBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_SdpBndIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacValInTrans = _SdpBndIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 18),
    _SdpBndIgmpSnpgCfgMcacValInTrans_Type()
)
sdpBndIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacValInTrans.setStatus("current")
_SdpBndIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_SdpBndIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
sdpBndIgmpSnpgCfgLastChangeTime = _SdpBndIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 19),
    _SdpBndIgmpSnpgCfgLastChangeTime_Type()
)
sdpBndIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastChangeTime.setStatus("current")


class _SdpBndIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SdpBndIgmpSnpgCfgMaxNbrSrcs_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgMaxNbrSrcs_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrSrcs = _SdpBndIgmpSnpgCfgMaxNbrSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 20),
    _SdpBndIgmpSnpgCfgMaxNbrSrcs_Type()
)
sdpBndIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrSrcs.setStatus("current")


class _SdpBndIgmpSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sdpBndIgmpSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SdpBndIgmpSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sdpBndIgmpSnpgCfgDisRtrAlertChk = _SdpBndIgmpSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 21),
    _SdpBndIgmpSnpgCfgDisRtrAlertChk_Type()
)
sdpBndIgmpSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgDisRtrAlertChk.setStatus("current")


class _SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrGrpSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrGrpSrcs = _SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 22),
    _SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Type()
)
sdpBndIgmpSnpgCfgMaxNbrGrpSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrGrpSrcs.setStatus("current")
_SdpBindIgmpSnpgGroupTable_Object = MibTable
sdpBindIgmpSnpgGroupTable = _SdpBindIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGroupTable.setStatus("current")
_SdpBindIgmpSnpgGroupEntry_Object = MibTableRow
sdpBindIgmpSnpgGroupEntry = _SdpBindIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1)
)
sdpBindIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGroupEntry.setStatus("current")
_SdpBndIgmpSnpgGrpAddress_Type = IpAddress
_SdpBndIgmpSnpgGrpAddress_Object = MibTableColumn
sdpBndIgmpSnpgGrpAddress = _SdpBndIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 1),
    _SdpBndIgmpSnpgGrpAddress_Type()
)
sdpBndIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpAddress.setStatus("current")
_SdpBndIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpType_Object = MibTableColumn
sdpBndIgmpSnpgGrpType = _SdpBndIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 2),
    _SdpBndIgmpSnpgGrpType_Type()
)
sdpBndIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpType.setStatus("current")
_SdpBndIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_SdpBndIgmpSnpgGrpFilterMode_Object = MibTableColumn
sdpBndIgmpSnpgGrpFilterMode = _SdpBndIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 3),
    _SdpBndIgmpSnpgGrpFilterMode_Type()
)
sdpBndIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpFilterMode.setStatus("current")
_SdpBndIgmpSnpgGrpUpTime_Type = TimeTicks
_SdpBndIgmpSnpgGrpUpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpUpTime = _SdpBndIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 4),
    _SdpBndIgmpSnpgGrpUpTime_Type()
)
sdpBndIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpUpTime.setStatus("current")
_SdpBndIgmpSnpgGrpExpiryTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpExpiryTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpExpiryTime = _SdpBndIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 5),
    _SdpBndIgmpSnpgGrpExpiryTime_Type()
)
sdpBndIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpExpiryTime.setUnits("seconds")
_SdpBndIgmpSnpgGrpCompatMode_Type = Unsigned32
_SdpBndIgmpSnpgGrpCompatMode_Object = MibTableColumn
sdpBndIgmpSnpgGrpCompatMode = _SdpBndIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 6),
    _SdpBndIgmpSnpgGrpCompatMode_Type()
)
sdpBndIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpCompatMode.setStatus("current")
_SdpBndIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpV1HostExpTime = _SdpBndIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 7),
    _SdpBndIgmpSnpgGrpV1HostExpTime_Type()
)
sdpBndIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_SdpBndIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpV2HostExpTime = _SdpBndIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 8),
    _SdpBndIgmpSnpgGrpV2HostExpTime_Type()
)
sdpBndIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_SdpBindIgmpSnpgGrpSrcTable_Object = MibTable
sdpBindIgmpSnpgGrpSrcTable = _SdpBindIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGrpSrcTable.setStatus("current")
_SdpBindIgmpSnpgGrpSrcEntry_Object = MibTableRow
sdpBindIgmpSnpgGrpSrcEntry = _SdpBindIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1)
)
sdpBindIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGrpSrcEntry.setStatus("current")
_SdpBndIgmpSnpgGrpSrcAddr_Type = IpAddress
_SdpBndIgmpSnpgGrpSrcAddr_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcAddr = _SdpBndIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 1),
    _SdpBndIgmpSnpgGrpSrcAddr_Type()
)
sdpBndIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcAddr.setStatus("current")
_SdpBndIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpSrcType_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcType = _SdpBndIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 2),
    _SdpBndIgmpSnpgGrpSrcType_Type()
)
sdpBndIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcType.setStatus("current")
_SdpBndIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_SdpBndIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcUpTime = _SdpBndIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 3),
    _SdpBndIgmpSnpgGrpSrcUpTime_Type()
)
sdpBndIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcUpTime.setStatus("current")
_SdpBndIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcExpiryTime = _SdpBndIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 4),
    _SdpBndIgmpSnpgGrpSrcExpiryTime_Type()
)
sdpBndIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")
_SdpBindIgmpSnpgStaticGrpSrcTable_Object = MibTable
sdpBindIgmpSnpgStaticGrpSrcTable = _SdpBindIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStaticGrpSrcTable.setStatus("current")
_SdpBindIgmpSnpgStatGrpSrcEntry_Object = MibTableRow
sdpBindIgmpSnpgStatGrpSrcEntry = _SdpBindIgmpSnpgStatGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1)
)
sdpBindIgmpSnpgStatGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticGroupAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStatGrpSrcEntry.setStatus("current")
_SdpBndIgmpSnpgStaticGroupAddr_Type = IpAddress
_SdpBndIgmpSnpgStaticGroupAddr_Object = MibTableColumn
sdpBndIgmpSnpgStaticGroupAddr = _SdpBndIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 1),
    _SdpBndIgmpSnpgStaticGroupAddr_Type()
)
sdpBndIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticGroupAddr.setStatus("current")
_SdpBndIgmpSnpgStaticSourceAddr_Type = IpAddress
_SdpBndIgmpSnpgStaticSourceAddr_Object = MibTableColumn
sdpBndIgmpSnpgStaticSourceAddr = _SdpBndIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 2),
    _SdpBndIgmpSnpgStaticSourceAddr_Type()
)
sdpBndIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticSourceAddr.setStatus("current")
_SdpBndIgmpSnpgStaticRowstatus_Type = RowStatus
_SdpBndIgmpSnpgStaticRowstatus_Object = MibTableColumn
sdpBndIgmpSnpgStaticRowstatus = _SdpBndIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 3),
    _SdpBndIgmpSnpgStaticRowstatus_Type()
)
sdpBndIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticRowstatus.setStatus("current")
_SdpBndIgmpSnpgStaticLastChange_Type = TimeStamp
_SdpBndIgmpSnpgStaticLastChange_Object = MibTableColumn
sdpBndIgmpSnpgStaticLastChange = _SdpBndIgmpSnpgStaticLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 4),
    _SdpBndIgmpSnpgStaticLastChange_Type()
)
sdpBndIgmpSnpgStaticLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticLastChange.setStatus("current")
_SdpBindIgmpSnpgStatsTable_Object = MibTable
sdpBindIgmpSnpgStatsTable = _SdpBindIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStatsTable.setStatus("current")
_SdpBindIgmpSnpgStatsEntry_Object = MibTableRow
sdpBindIgmpSnpgStatsEntry = _SdpBindIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1)
)
sdpBindIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStatsEntry.setStatus("current")
_SdpBndIgmpSnpgTxGenQueries_Type = Counter32
_SdpBndIgmpSnpgTxGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxGenQueries = _SdpBndIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 1),
    _SdpBndIgmpSnpgTxGenQueries_Type()
)
sdpBndIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxGenQueries.setStatus("current")
_SdpBndIgmpSnpgTxGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxGrpSpecQueries = _SdpBndIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 2),
    _SdpBndIgmpSnpgTxGrpSpecQueries_Type()
)
sdpBndIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgTxSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxSrcSpecQueries = _SdpBndIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 3),
    _SdpBndIgmpSnpgTxSrcSpecQueries_Type()
)
sdpBndIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgTxV1Reports_Type = Counter32
_SdpBndIgmpSnpgTxV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV1Reports = _SdpBndIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 4),
    _SdpBndIgmpSnpgTxV1Reports_Type()
)
sdpBndIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV1Reports.setStatus("current")
_SdpBndIgmpSnpgTxV2Reports_Type = Counter32
_SdpBndIgmpSnpgTxV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV2Reports = _SdpBndIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 5),
    _SdpBndIgmpSnpgTxV2Reports_Type()
)
sdpBndIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV2Reports.setStatus("current")
_SdpBndIgmpSnpgTxV3Reports_Type = Counter32
_SdpBndIgmpSnpgTxV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV3Reports = _SdpBndIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 6),
    _SdpBndIgmpSnpgTxV3Reports_Type()
)
sdpBndIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV3Reports.setStatus("current")
_SdpBndIgmpSnpgTxV2Leaves_Type = Counter32
_SdpBndIgmpSnpgTxV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgTxV2Leaves = _SdpBndIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 7),
    _SdpBndIgmpSnpgTxV2Leaves_Type()
)
sdpBndIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV2Leaves.setStatus("current")
_SdpBndIgmpSnpgRxGenQueries_Type = Counter32
_SdpBndIgmpSnpgRxGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxGenQueries = _SdpBndIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 8),
    _SdpBndIgmpSnpgRxGenQueries_Type()
)
sdpBndIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxGenQueries.setStatus("current")
_SdpBndIgmpSnpgRxGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxGrpSpecQueries = _SdpBndIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 9),
    _SdpBndIgmpSnpgRxGrpSpecQueries_Type()
)
sdpBndIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgRxSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxSrcSpecQueries = _SdpBndIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 10),
    _SdpBndIgmpSnpgRxSrcSpecQueries_Type()
)
sdpBndIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgRxV1Reports_Type = Counter32
_SdpBndIgmpSnpgRxV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV1Reports = _SdpBndIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 11),
    _SdpBndIgmpSnpgRxV1Reports_Type()
)
sdpBndIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV1Reports.setStatus("current")
_SdpBndIgmpSnpgRxV2Reports_Type = Counter32
_SdpBndIgmpSnpgRxV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV2Reports = _SdpBndIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 12),
    _SdpBndIgmpSnpgRxV2Reports_Type()
)
sdpBndIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV2Reports.setStatus("current")
_SdpBndIgmpSnpgRxV3Reports_Type = Counter32
_SdpBndIgmpSnpgRxV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV3Reports = _SdpBndIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 13),
    _SdpBndIgmpSnpgRxV3Reports_Type()
)
sdpBndIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV3Reports.setStatus("current")
_SdpBndIgmpSnpgRxV2Leaves_Type = Counter32
_SdpBndIgmpSnpgRxV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgRxV2Leaves = _SdpBndIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 14),
    _SdpBndIgmpSnpgRxV2Leaves_Type()
)
sdpBndIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV2Leaves.setStatus("current")
_SdpBndIgmpSnpgRxUnknownType_Type = Counter32
_SdpBndIgmpSnpgRxUnknownType_Object = MibTableColumn
sdpBndIgmpSnpgRxUnknownType = _SdpBndIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 15),
    _SdpBndIgmpSnpgRxUnknownType_Type()
)
sdpBndIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxUnknownType.setStatus("current")
_SdpBndIgmpSnpgFwdGenQueries_Type = Counter32
_SdpBndIgmpSnpgFwdGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdGenQueries = _SdpBndIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 16),
    _SdpBndIgmpSnpgFwdGenQueries_Type()
)
sdpBndIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdGenQueries.setStatus("current")
_SdpBndIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdGrpSpecQueries = _SdpBndIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 17),
    _SdpBndIgmpSnpgFwdGrpSpecQueries_Type()
)
sdpBndIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdSrcSpecQueries = _SdpBndIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 18),
    _SdpBndIgmpSnpgFwdSrcSpecQueries_Type()
)
sdpBndIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgFwdV1Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV1Reports = _SdpBndIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 19),
    _SdpBndIgmpSnpgFwdV1Reports_Type()
)
sdpBndIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV1Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV2Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV2Reports = _SdpBndIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 20),
    _SdpBndIgmpSnpgFwdV2Reports_Type()
)
sdpBndIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV2Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV3Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV3Reports = _SdpBndIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 21),
    _SdpBndIgmpSnpgFwdV3Reports_Type()
)
sdpBndIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV3Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV2Leaves_Type = Counter32
_SdpBndIgmpSnpgFwdV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgFwdV2Leaves = _SdpBndIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 22),
    _SdpBndIgmpSnpgFwdV2Leaves_Type()
)
sdpBndIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV2Leaves.setStatus("current")
_SdpBndIgmpSnpgFwdUnknownType_Type = Counter32
_SdpBndIgmpSnpgFwdUnknownType_Object = MibTableColumn
sdpBndIgmpSnpgFwdUnknownType = _SdpBndIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 23),
    _SdpBndIgmpSnpgFwdUnknownType_Type()
)
sdpBndIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdUnknownType.setStatus("current")
_SdpBndIgmpSnpgRxBadLenPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadLenPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadLenPkts = _SdpBndIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 24),
    _SdpBndIgmpSnpgRxBadLenPkts_Type()
)
sdpBndIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadLenPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadIpChksmPkts = _SdpBndIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 25),
    _SdpBndIgmpSnpgRxBadIpChksmPkts_Type()
)
sdpBndIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadIgmpChksmPkts = _SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 26),
    _SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type()
)
sdpBndIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadEncodedPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadEncodedPkts = _SdpBndIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 27),
    _SdpBndIgmpSnpgRxBadEncodedPkts_Type()
)
sdpBndIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadEncodedPkts.setStatus("current")
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxNoRtrAlertPkts = _SdpBndIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 28),
    _SdpBndIgmpSnpgRxNoRtrAlertPkts_Type()
)
sdpBndIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxZeroSrcAdrPkts = _SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 29),
    _SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type()
)
sdpBndIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_SdpBndIgmpSnpgSendQueryCfgDrops_Type = Counter32
_SdpBndIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
sdpBndIgmpSnpgSendQueryCfgDrops = _SdpBndIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 30),
    _SdpBndIgmpSnpgSendQueryCfgDrops_Type()
)
sdpBndIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgSendQueryCfgDrops.setStatus("current")
_SdpBndIgmpSnpgImportPolicyDrops_Type = Counter32
_SdpBndIgmpSnpgImportPolicyDrops_Object = MibTableColumn
sdpBndIgmpSnpgImportPolicyDrops = _SdpBndIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 31),
    _SdpBndIgmpSnpgImportPolicyDrops_Type()
)
sdpBndIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgImportPolicyDrops.setStatus("current")
_SdpBndIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumGroupsDrops = _SdpBndIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 32),
    _SdpBndIgmpSnpgMaxNumGroupsDrops_Type()
)
sdpBndIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_SdpBndIgmpSnpgRxWrongVersionPkts_Type = Counter32
_SdpBndIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxWrongVersionPkts = _SdpBndIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 33),
    _SdpBndIgmpSnpgRxWrongVersionPkts_Type()
)
sdpBndIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxWrongVersionPkts.setStatus("current")
_SdpBndIgmpSnpgMcacPolicyDrops_Type = Counter32
_SdpBndIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
sdpBndIgmpSnpgMcacPolicyDrops = _SdpBndIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 34),
    _SdpBndIgmpSnpgMcacPolicyDrops_Type()
)
sdpBndIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMcacPolicyDrops.setStatus("current")
_SdpBndIgmpSnpgRxLocalScopePkts_Type = Counter32
_SdpBndIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
sdpBndIgmpSnpgRxLocalScopePkts = _SdpBndIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 35),
    _SdpBndIgmpSnpgRxLocalScopePkts_Type()
)
sdpBndIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxLocalScopePkts.setStatus("current")
_SdpBndIgmpSnpgRxRsvdScopePkts_Type = Counter32
_SdpBndIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
sdpBndIgmpSnpgRxRsvdScopePkts = _SdpBndIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 36),
    _SdpBndIgmpSnpgRxRsvdScopePkts_Type()
)
sdpBndIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxRsvdScopePkts.setStatus("current")
_SdpBndIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumSourcesDrops = _SdpBndIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 37),
    _SdpBndIgmpSnpgMaxNumSourcesDrops_Type()
)
sdpBndIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumGrpSrcsDrops = _SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 38),
    _SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
sdpBndIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_AlxIgmpSnoopingNotificationObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingNotificationObjs = _AlxIgmpSnoopingNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4)
)
_AlxIgmpSnpgGroupAddress_Type = IpAddress
_AlxIgmpSnpgGroupAddress_Object = MibScalar
alxIgmpSnpgGroupAddress = _AlxIgmpSnpgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 1),
    _AlxIgmpSnpgGroupAddress_Type()
)
alxIgmpSnpgGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgGroupAddress.setStatus("current")
_AlxIgmpSnpgMcsFailureReason_Type = DisplayString
_AlxIgmpSnpgMcsFailureReason_Object = MibScalar
alxIgmpSnpgMcsFailureReason = _AlxIgmpSnpgMcsFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 2),
    _AlxIgmpSnpgMcsFailureReason_Type()
)
alxIgmpSnpgMcsFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgMcsFailureReason.setStatus("current")
_AlxIgmpSnpgSourceAddress_Type = IpAddress
_AlxIgmpSnpgSourceAddress_Object = MibScalar
alxIgmpSnpgSourceAddress = _AlxIgmpSnpgSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 3),
    _AlxIgmpSnpgSourceAddress_Type()
)
alxIgmpSnpgSourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgSourceAddress.setStatus("current")
_AlxIgmpSnpgDescription_Type = DisplayString
_AlxIgmpSnpgDescription_Object = MibScalar
alxIgmpSnpgDescription = _AlxIgmpSnpgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 4),
    _AlxIgmpSnpgDescription_Type()
)
alxIgmpSnpgDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgDescription.setStatus("current")
_AlxIgmpSnoopingTimeStampObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTimeStampObjs = _AlxIgmpSnoopingTimeStampObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5)
)
_TlsIgmpSnpgConfigTableLastChange_Type = TimeStamp
_TlsIgmpSnpgConfigTableLastChange_Object = MibScalar
tlsIgmpSnpgConfigTableLastChange = _TlsIgmpSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 1),
    _TlsIgmpSnpgConfigTableLastChange_Type()
)
tlsIgmpSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgConfigTableLastChange.setStatus("current")
_SapIgmpSnpgConfigTableLastChange_Type = TimeStamp
_SapIgmpSnpgConfigTableLastChange_Object = MibScalar
sapIgmpSnpgConfigTableLastChange = _SapIgmpSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 2),
    _SapIgmpSnpgConfigTableLastChange_Type()
)
sapIgmpSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgConfigTableLastChange.setStatus("current")
_SapIgmpSnpgStaticGrpSrcTablLstCh_Type = TimeStamp
_SapIgmpSnpgStaticGrpSrcTablLstCh_Object = MibScalar
sapIgmpSnpgStaticGrpSrcTablLstCh = _SapIgmpSnpgStaticGrpSrcTablLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 3),
    _SapIgmpSnpgStaticGrpSrcTablLstCh_Type()
)
sapIgmpSnpgStaticGrpSrcTablLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGrpSrcTablLstCh.setStatus("current")
_SapIgmpSnpgMcacLevelTableLstCh_Type = TimeStamp
_SapIgmpSnpgMcacLevelTableLstCh_Object = MibScalar
sapIgmpSnpgMcacLevelTableLstCh = _SapIgmpSnpgMcacLevelTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 4),
    _SapIgmpSnpgMcacLevelTableLstCh_Type()
)
sapIgmpSnpgMcacLevelTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLevelTableLstCh.setStatus("current")
_SapIgmpSnpgMcacLagTableLastChng_Type = TimeStamp
_SapIgmpSnpgMcacLagTableLastChng_Object = MibScalar
sapIgmpSnpgMcacLagTableLastChng = _SapIgmpSnpgMcacLagTableLastChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 5),
    _SapIgmpSnpgMcacLagTableLastChng_Type()
)
sapIgmpSnpgMcacLagTableLastChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLagTableLastChng.setStatus("current")
_SdpBindIgmpSnpgConfigTableLstCh_Type = TimeStamp
_SdpBindIgmpSnpgConfigTableLstCh_Object = MibScalar
sdpBindIgmpSnpgConfigTableLstCh = _SdpBindIgmpSnpgConfigTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 6),
    _SdpBindIgmpSnpgConfigTableLstCh_Type()
)
sdpBindIgmpSnpgConfigTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgConfigTableLstCh.setStatus("current")
_SdpBindIgmpSnpgStaticGrpSrcTblLC_Type = TimeStamp
_SdpBindIgmpSnpgStaticGrpSrcTblLC_Object = MibScalar
sdpBindIgmpSnpgStaticGrpSrcTblLC = _SdpBindIgmpSnpgStaticGrpSrcTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 7),
    _SdpBindIgmpSnpgStaticGrpSrcTblLC_Type()
)
sdpBindIgmpSnpgStaticGrpSrcTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStaticGrpSrcTblLC.setStatus("current")
_AlxIgmpSnoopingNotifyPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingNotifyPrefix = _AlxIgmpSnoopingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2)
)
_AlxIgmpSnoopingSapPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapPrefix = _AlxIgmpSnoopingSapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1)
)
_AlxIgmpSnpgSapNotifications_ObjectIdentity = ObjectIdentity
alxIgmpSnpgSapNotifications = _AlxIgmpSnpgSapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0)
)
_AlxIgmpSnoopingSdpBndPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndPrefix = _AlxIgmpSnoopingSdpBndPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2)
)
_AlxIgmpSnpgSdpBndNotifications_ObjectIdentity = ObjectIdentity
alxIgmpSnpgSdpBndNotifications = _AlxIgmpSnpgSdpBndNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0)
)

# Managed Objects groups

alxTlsIgmpSnpgConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 1)
)
alxTlsIgmpSnpgConfigV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgAdminState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgReportSrcAddress"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV3v0Group.setStatus("obsolete")

alxTlsIgmpSnpgQuerierV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 2)
)
alxTlsIgmpSnpgQuerierV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierLocale"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierSdpId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVcId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierGenRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVRtrId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierIfIndex"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgQuerierV3v0Group.setStatus("current")

alxTlsIgmpSnpgProxyV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 3)
)
alxTlsIgmpSnpgProxyV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGrpSrcUpTime"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgProxyV3v0Group.setStatus("current")

alxTlsIgmpSnpgMRouterV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 4)
)
alxTlsIgmpSnpgMRouterV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterLocale"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterSdpId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVcId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterGenRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVRtrId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterIfIndex"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgMRouterV3v0Group.setStatus("current")

alxTlsMvrConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 5)
)
alxTlsMvrConfigV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgMvrAdminState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgMvrDescription"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgMvrPolicy"))
)
if mibBuilder.loadTexts:
    alxTlsMvrConfigV3v0Group.setStatus("current")

alxTlsIgmpSnpgNotObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 6)
)
alxTlsIgmpSnpgNotObjV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotObjV5v0Group.setStatus("current")

alxTlsIgmpSnpgConfigV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 7)
)
alxTlsIgmpSnpgConfigV6v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgAdminState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgReportSrcAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgQuerySrcAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgQuerySrcAddrType"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV6v0Group.setStatus("current")

alxTlsIgmpSnpgTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 8)
)
alxTlsIgmpSnpgTimeStampGroup.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgConfigTableLastChange"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgTimeStampGroup.setStatus("current")

alxTlsIgmpSnpgNotifyObjsV6v1Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 9)
)
alxTlsIgmpSnpgNotifyObjsV6v1Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress")
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotifyObjsV6v1Grp.setStatus("current")

alxTlsIgmpSnpgNotifyObjsV12v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 10)
)
alxTlsIgmpSnpgNotifyObjsV12v0Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription")
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotifyObjsV12v0Grp.setStatus("current")

alxSapIgmpSnpgConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 1)
)
alxSapIgmpSnpgConfigV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrps"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV3v0Group.setStatus("obsolete")

alxSapIgmpSnpgGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 2)
)
alxSapIgmpSnpgGroupV3v0.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpV1HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpV2HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgGroupV3v0.setStatus("current")

alxSapIgmpSnpgStaticV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 3)
)
alxSapIgmpSnpgStaticV3v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticRowstatus")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStaticV3v0Group.setStatus("current")

alxSapIgmpSnpgStatsV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 4)
)
alxSapIgmpSnpgStatsV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGroupsDrops"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV3v0Group.setStatus("obsolete")

alxSapMvrV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 5)
)
alxSapMvrV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMvrFromVplsId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMvrToSapPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMvrToSapEncapVal"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpMvrFromVplsId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpMvrToSapPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpMvrToSapEncapVal"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMvrFromVplsCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMvrToSapCfgDrops"))
)
if mibBuilder.loadTexts:
    alxSapMvrV3v0Group.setStatus("current")

alxSapIgmpSnpgConfigV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 6)
)
alxSapIgmpSnpgConfigV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacUnconstBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacConstAdmSt"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLevelRowStat"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLevelBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLagRowStat"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLagLevel"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacPrRsvMndBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacinUseMandBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacinUseOpnlBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacAvailMandBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacAvailOpnlBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacValInTrans"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV5v0Group.setStatus("current")

alxSapIgmpSnpgStatsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 7)
)
alxSapIgmpSnpgStatsV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcsFailures"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV5v0Group.setStatus("obsolete")

alxSapIgmpSnpgTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 9)
)
alxSapIgmpSnpgTimeStampGroup.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLevelLastChngT"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLagLastChangeT"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgConfigTableLastChange"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticGrpSrcTablLstCh"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacLevelTableLstCh"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacLagTableLastChng"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgTimeStampGroup.setStatus("current")

alxSapIgmpSnpgStatsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 10)
)
alxSapIgmpSnpgStatsV6v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcsFailures"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV6v0Group.setStatus("current")

alxSapIgmpSnpgMaxSrcsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 11)
)
alxSapIgmpSnpgMaxSrcsV6v1Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumSourcesDrops"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgMaxSrcsV6v1Group.setStatus("current")

alxSapIgmpSnpgConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 13)
)
alxSapIgmpSnpgConfigV8v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgDisRtrAlertChk"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgDisRtrAlertChk"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV8v0Group.setStatus("current")

alxSapIgmpSnpgConfigV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 14)
)
alxSapIgmpSnpgConfigV11v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrpSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrpSrcs"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV11v0Group.setStatus("current")

alxSapIgmpSnpgStatsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 15)
)
alxSapIgmpSnpgStatsV11v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGrpSrcsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGrpSrcsDrops"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV11v0Group.setStatus("current")

alxSapIgmpSnpgConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 17)
)
alxSapIgmpSnpgConfigV12v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacUseLagPortWt")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV12v0Group.setStatus("current")

alxSdpBindIgmpSnpgConfV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 1)
)
alxSdpBindIgmpSnpgConfV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrps"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgConfV3v0Group.setStatus("obsolete")

alxSdpBindIgmpSnpgV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 2)
)
alxSdpBindIgmpSnpgV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpV1HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpV2HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgV3v0Group.setStatus("current")

alxSdpBindIgmpSnpgStatV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 3)
)
alxSdpBindIgmpSnpgStatV3v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticRowstatus")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatV3v0Group.setStatus("current")

alxSdpBindIgmpSnpgStatsV3v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 4)
)
alxSdpBindIgmpSnpgStatsV3v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGroupsDrops"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatsV3v0Grp.setStatus("obsolete")

alxSdpBindIgmpSnpgConfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 5)
)
alxSdpBindIgmpSnpgConfV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacUnconstBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacPrRsvMndBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacinUseMndBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacinUseOplBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacAvailMndBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacAvailOplBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacValInTrans"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgConfV5v0Group.setStatus("current")

alxSdpBindIgmpSnpgStatsV5v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 6)
)
alxSdpBindIgmpSnpgStatsV5v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMcacPolicyDrops"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatsV5v0Grp.setStatus("obsolete")

alxSdpBindIgmpSnpgTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 8)
)
alxSdpBindIgmpSnpgTimeStampGroup.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticLastChange"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBindIgmpSnpgConfigTableLstCh"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBindIgmpSnpgStaticGrpSrcTblLC"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgTimeStampGroup.setStatus("current")

alxSdpBindIgmpSnpgStatsV6v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 9)
)
alxSdpBindIgmpSnpgStatsV6v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatsV6v0Grp.setStatus("current")

alxSdpBindIgmpSnpgMaxSrcsV6v1Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 10)
)
alxSdpBindIgmpSnpgMaxSrcsV6v1Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumSourcesDrops"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgMaxSrcsV6v1Grp.setStatus("current")


# Notification objects

sapIgmpSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 1)
)
sapIgmpSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpLimitExceeded.setStatus(
        "current"
    )

sapIgmpSnpgMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 2)
)
sapIgmpSnpgMcacPlcyDropped.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacPlcyDropped.setStatus(
        "current"
    )

sapIgmpSnpgMcsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 3)
)
sapIgmpSnpgMcsFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcsFailure.setStatus(
        "current"
    )

sapIgmpSnpgSrcLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 4)
)
sapIgmpSnpgSrcLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgSrcLimitExceeded.setStatus(
        "current"
    )

sapIgmpSnpgGrpSrcLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 5)
)
sapIgmpSnpgGrpSrcLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrpSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcLimitExceeded.setStatus(
        "current"
    )

sdpBndIgmpSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 1)
)
sdpBndIgmpSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpLimitExceeded.setStatus(
        "current"
    )

sdpBndIgmpSnpgMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 2)
)
sdpBndIgmpSnpgMcacPlcyDropped.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMcacPlcyDropped.setStatus(
        "current"
    )

sdpBndIgmpSnpgSrcLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 3)
)
sdpBndIgmpSnpgSrcLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgSrcLimitExceeded.setStatus(
        "current"
    )

sdpBndIgmpSnpgGrpSrcLimitExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 4)
)
sdpBndIgmpSnpgGrpSrcLimitExceed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrpSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcLimitExceed.setStatus(
        "current"
    )


# Notifications groups

alxSapIgmpSnpgNotV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 8)
)
alxSapIgmpSnpgNotV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpLimitExceeded"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacPlcyDropped"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcsFailure"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgNotV5v0Group.setStatus(
        "current"
    )

alxSapIgmpSnpgMaxSrcsNotV6v1Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 12)
)
alxSapIgmpSnpgMaxSrcsNotV6v1Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSrcLimitExceeded")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgMaxSrcsNotV6v1Grp.setStatus(
        "current"
    )

alxSapIgmpSnpgMaxSrcsNotV11v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 16)
)
alxSapIgmpSnpgMaxSrcsNotV11v0Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcLimitExceeded")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgMaxSrcsNotV11v0Grp.setStatus(
        "current"
    )

alxSdpBindIgmpSnpgNotV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 7)
)
alxSdpBindIgmpSnpgNotV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpLimitExceeded"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMcacPlcyDropped"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgNotV5v0Group.setStatus(
        "current"
    )

alxSdpBindIgmpSnpgNotV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 12)
)
alxSdpBindIgmpSnpgNotV6v1Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSrcLimitExceeded")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgNotV6v1Group.setStatus(
        "current"
    )

alxSdpBindIgmpSnpgNotV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 13)
)
alxSdpBindIgmpSnpgNotV11v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcLimitExceed")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgNotV11v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alxIgmpSnoopingTlsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 1)
)
alxIgmpSnoopingTlsCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingTlsCompliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingTlsV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 2)
)
alxIgmpSnoopingTlsV5v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingTlsV5v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingTlsV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 3)
)
alxIgmpSnoopingTlsV6v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgTimeStampGroup"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingTlsV6v0Compliance.setStatus(
        "current"
    )

alxIgmpSnoopingSapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 1)
)
alxIgmpSnoopingSapCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapCompliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 2)
)
alxIgmpSnoopingSapV5v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV5v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 3)
)
alxIgmpSnoopingSapV6v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV6v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 4)
)
alxIgmpSnoopingSapV6v1Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV6v1Compliance.setStatus(
        "current"
    )

alxIgmpSnoopingSapV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 5)
)
alxIgmpSnoopingSapV8v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV8v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV11v0Complianc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 6)
)
alxIgmpSnoopingSapV11v0Complianc.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV11v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV11v0Complianc.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV12v0Complianc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 7)
)
alxIgmpSnoopingSapV12v0Complianc.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV12v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV12v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV11v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV12v0Complianc.setStatus(
        "current"
    )

alxIgmpSnoopingSdpBndCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 1)
)
alxIgmpSnoopingSdpBndCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV3v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndCompliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSdpBndV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 2)
)
alxIgmpSnoopingSdpBndV5v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV5v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndV5v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSdpBndV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 3)
)
alxIgmpSnoopingSdpBndV6v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndV6v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSdpBndV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 4)
)
alxIgmpSnoopingSdpBndV6v1Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV6v1Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndV6v1Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnpgSdpBndV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 5)
)
alxIgmpSnpgSdpBndV11v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV11v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgSdpBndV11v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IGMP-SNOOPING-MIB",
    **{"AlxIgmpSnpgAdminState": AlxIgmpSnpgAdminState,
       "AlxIgmpSnpgLocation": AlxIgmpSnpgLocation,
       "alcatelIgmpSnoopingMIBModule": alcatelIgmpSnoopingMIBModule,
       "alxIgmpSnoopingConformance": alxIgmpSnoopingConformance,
       "alxIgmpSnoopingTlsConformance": alxIgmpSnoopingTlsConformance,
       "alxIgmpSnoopingTlsCompliancs": alxIgmpSnoopingTlsCompliancs,
       "alxIgmpSnoopingTlsCompliance": alxIgmpSnoopingTlsCompliance,
       "alxIgmpSnoopingTlsV5v0Compliance": alxIgmpSnoopingTlsV5v0Compliance,
       "alxIgmpSnoopingTlsV6v0Compliance": alxIgmpSnoopingTlsV6v0Compliance,
       "alxIgmpSnoopingTlsGroups": alxIgmpSnoopingTlsGroups,
       "alxTlsIgmpSnpgConfigV3v0Group": alxTlsIgmpSnpgConfigV3v0Group,
       "alxTlsIgmpSnpgQuerierV3v0Group": alxTlsIgmpSnpgQuerierV3v0Group,
       "alxTlsIgmpSnpgProxyV3v0Group": alxTlsIgmpSnpgProxyV3v0Group,
       "alxTlsIgmpSnpgMRouterV3v0Group": alxTlsIgmpSnpgMRouterV3v0Group,
       "alxTlsMvrConfigV3v0Group": alxTlsMvrConfigV3v0Group,
       "alxTlsIgmpSnpgNotObjV5v0Group": alxTlsIgmpSnpgNotObjV5v0Group,
       "alxTlsIgmpSnpgConfigV6v0Group": alxTlsIgmpSnpgConfigV6v0Group,
       "alxTlsIgmpSnpgTimeStampGroup": alxTlsIgmpSnpgTimeStampGroup,
       "alxTlsIgmpSnpgNotifyObjsV6v1Grp": alxTlsIgmpSnpgNotifyObjsV6v1Grp,
       "alxTlsIgmpSnpgNotifyObjsV12v0Grp": alxTlsIgmpSnpgNotifyObjsV12v0Grp,
       "alxIgmpSnoopingSapConformance": alxIgmpSnoopingSapConformance,
       "alxIgmpSnoopingSapCompliancs": alxIgmpSnoopingSapCompliancs,
       "alxIgmpSnoopingSapCompliance": alxIgmpSnoopingSapCompliance,
       "alxIgmpSnoopingSapV5v0Compliance": alxIgmpSnoopingSapV5v0Compliance,
       "alxIgmpSnoopingSapV6v0Compliance": alxIgmpSnoopingSapV6v0Compliance,
       "alxIgmpSnoopingSapV6v1Compliance": alxIgmpSnoopingSapV6v1Compliance,
       "alxIgmpSnoopingSapV8v0Compliance": alxIgmpSnoopingSapV8v0Compliance,
       "alxIgmpSnoopingSapV11v0Complianc": alxIgmpSnoopingSapV11v0Complianc,
       "alxIgmpSnoopingSapV12v0Complianc": alxIgmpSnoopingSapV12v0Complianc,
       "alxIgmpSnoopingSapGroups": alxIgmpSnoopingSapGroups,
       "alxSapIgmpSnpgConfigV3v0Group": alxSapIgmpSnpgConfigV3v0Group,
       "alxSapIgmpSnpgGroupV3v0": alxSapIgmpSnpgGroupV3v0,
       "alxSapIgmpSnpgStaticV3v0Group": alxSapIgmpSnpgStaticV3v0Group,
       "alxSapIgmpSnpgStatsV3v0Group": alxSapIgmpSnpgStatsV3v0Group,
       "alxSapMvrV3v0Group": alxSapMvrV3v0Group,
       "alxSapIgmpSnpgConfigV5v0Group": alxSapIgmpSnpgConfigV5v0Group,
       "alxSapIgmpSnpgStatsV5v0Group": alxSapIgmpSnpgStatsV5v0Group,
       "alxSapIgmpSnpgNotV5v0Group": alxSapIgmpSnpgNotV5v0Group,
       "alxSapIgmpSnpgTimeStampGroup": alxSapIgmpSnpgTimeStampGroup,
       "alxSapIgmpSnpgStatsV6v0Group": alxSapIgmpSnpgStatsV6v0Group,
       "alxSapIgmpSnpgMaxSrcsV6v1Group": alxSapIgmpSnpgMaxSrcsV6v1Group,
       "alxSapIgmpSnpgMaxSrcsNotV6v1Grp": alxSapIgmpSnpgMaxSrcsNotV6v1Grp,
       "alxSapIgmpSnpgConfigV8v0Group": alxSapIgmpSnpgConfigV8v0Group,
       "alxSapIgmpSnpgConfigV11v0Group": alxSapIgmpSnpgConfigV11v0Group,
       "alxSapIgmpSnpgStatsV11v0Group": alxSapIgmpSnpgStatsV11v0Group,
       "alxSapIgmpSnpgMaxSrcsNotV11v0Grp": alxSapIgmpSnpgMaxSrcsNotV11v0Grp,
       "alxSapIgmpSnpgConfigV12v0Group": alxSapIgmpSnpgConfigV12v0Group,
       "alxIgmpSnoopingSdpBndConformance": alxIgmpSnoopingSdpBndConformance,
       "alxIgmpSnoopingSdpBndCompliancs": alxIgmpSnoopingSdpBndCompliancs,
       "alxIgmpSnoopingSdpBndCompliance": alxIgmpSnoopingSdpBndCompliance,
       "alxIgmpSnoopingSdpBndV5v0Compliance": alxIgmpSnoopingSdpBndV5v0Compliance,
       "alxIgmpSnoopingSdpBndV6v0Compliance": alxIgmpSnoopingSdpBndV6v0Compliance,
       "alxIgmpSnoopingSdpBndV6v1Compliance": alxIgmpSnoopingSdpBndV6v1Compliance,
       "alxIgmpSnpgSdpBndV11v0Compliance": alxIgmpSnpgSdpBndV11v0Compliance,
       "alxIgmpSnoopingSdpBndGroups": alxIgmpSnoopingSdpBndGroups,
       "alxSdpBindIgmpSnpgConfV3v0Group": alxSdpBindIgmpSnpgConfV3v0Group,
       "alxSdpBindIgmpSnpgV3v0Group": alxSdpBindIgmpSnpgV3v0Group,
       "alxSdpBindIgmpSnpgStatV3v0Group": alxSdpBindIgmpSnpgStatV3v0Group,
       "alxSdpBindIgmpSnpgStatsV3v0Grp": alxSdpBindIgmpSnpgStatsV3v0Grp,
       "alxSdpBindIgmpSnpgConfV5v0Group": alxSdpBindIgmpSnpgConfV5v0Group,
       "alxSdpBindIgmpSnpgStatsV5v0Grp": alxSdpBindIgmpSnpgStatsV5v0Grp,
       "alxSdpBindIgmpSnpgNotV5v0Group": alxSdpBindIgmpSnpgNotV5v0Group,
       "alxSdpBindIgmpSnpgTimeStampGroup": alxSdpBindIgmpSnpgTimeStampGroup,
       "alxSdpBindIgmpSnpgStatsV6v0Grp": alxSdpBindIgmpSnpgStatsV6v0Grp,
       "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp": alxSdpBindIgmpSnpgMaxSrcsV6v1Grp,
       "alxSdpBindIgmpSnpgNotV6v1Group": alxSdpBindIgmpSnpgNotV6v1Group,
       "alxSdpBindIgmpSnpgNotV11v0Group": alxSdpBindIgmpSnpgNotV11v0Group,
       "alxIgmpSnoopingObjs": alxIgmpSnoopingObjs,
       "alxIgmpSnoopingTlsObjs": alxIgmpSnoopingTlsObjs,
       "tlsIgmpSnpgConfigTable": tlsIgmpSnpgConfigTable,
       "tlsIgmpSnpgConfigEntry": tlsIgmpSnpgConfigEntry,
       "tlsIgmpSnpgCfgAdminState": tlsIgmpSnpgCfgAdminState,
       "tlsIgmpSnpgCfgGenQueryIntvl": tlsIgmpSnpgCfgGenQueryIntvl,
       "tlsIgmpSnpgCfgRobustCount": tlsIgmpSnpgCfgRobustCount,
       "tlsIgmpSnpgCfgReportSrcAddress": tlsIgmpSnpgCfgReportSrcAddress,
       "tlsIgmpSnpgCfgMvrAdminState": tlsIgmpSnpgCfgMvrAdminState,
       "tlsIgmpSnpgCfgMvrDescription": tlsIgmpSnpgCfgMvrDescription,
       "tlsIgmpSnpgCfgMvrPolicy": tlsIgmpSnpgCfgMvrPolicy,
       "tlsIgmpSnpgCfgQuerySrcAddress": tlsIgmpSnpgCfgQuerySrcAddress,
       "tlsIgmpSnpgCfgQuerySrcAddrType": tlsIgmpSnpgCfgQuerySrcAddrType,
       "tlsIgmpSnpgCfgLastChangeTime": tlsIgmpSnpgCfgLastChangeTime,
       "tlsIgmpSnpgQuerierTable": tlsIgmpSnpgQuerierTable,
       "tlsIgmpSnpgQuerierEntry": tlsIgmpSnpgQuerierEntry,
       "tlsIgmpSnpgQuerierVersion": tlsIgmpSnpgQuerierVersion,
       "tlsIgmpSnpgQuerierAddress": tlsIgmpSnpgQuerierAddress,
       "tlsIgmpSnpgQuerierLocale": tlsIgmpSnpgQuerierLocale,
       "tlsIgmpSnpgQuerierPortId": tlsIgmpSnpgQuerierPortId,
       "tlsIgmpSnpgQuerierEncapValue": tlsIgmpSnpgQuerierEncapValue,
       "tlsIgmpSnpgQuerierSdpId": tlsIgmpSnpgQuerierSdpId,
       "tlsIgmpSnpgQuerierVcId": tlsIgmpSnpgQuerierVcId,
       "tlsIgmpSnpgQuerierUpTime": tlsIgmpSnpgQuerierUpTime,
       "tlsIgmpSnpgQuerierExpiryTime": tlsIgmpSnpgQuerierExpiryTime,
       "tlsIgmpSnpgQuerierGenQueryIntvl": tlsIgmpSnpgQuerierGenQueryIntvl,
       "tlsIgmpSnpgQuerierGenRespIntvl": tlsIgmpSnpgQuerierGenRespIntvl,
       "tlsIgmpSnpgQuerierRobustCount": tlsIgmpSnpgQuerierRobustCount,
       "tlsIgmpSnpgQuerierVRtrId": tlsIgmpSnpgQuerierVRtrId,
       "tlsIgmpSnpgQuerierIfIndex": tlsIgmpSnpgQuerierIfIndex,
       "tlsIgmpSnpgProxyGroupTable": tlsIgmpSnpgProxyGroupTable,
       "tlsIgmpSnpgProxyGroupEntry": tlsIgmpSnpgProxyGroupEntry,
       "tlsIgmpSnpgProxyGroupAddress": tlsIgmpSnpgProxyGroupAddress,
       "tlsIgmpSnpgProxyGroupFilterMode": tlsIgmpSnpgProxyGroupFilterMode,
       "tlsIgmpSnpgProxyGroupUpTime": tlsIgmpSnpgProxyGroupUpTime,
       "tlsIgmpSnpgProxyGrpSrcTable": tlsIgmpSnpgProxyGrpSrcTable,
       "tlsIgmpSnpgProxyGrpSrcEntry": tlsIgmpSnpgProxyGrpSrcEntry,
       "tlsIgmpSnpgProxyGrpSrcAddr": tlsIgmpSnpgProxyGrpSrcAddr,
       "tlsIgmpSnpgProxyGrpSrcUpTime": tlsIgmpSnpgProxyGrpSrcUpTime,
       "tlsIgmpSnpgMRouterTable": tlsIgmpSnpgMRouterTable,
       "tlsIgmpSnpgMRouterEntry": tlsIgmpSnpgMRouterEntry,
       "tlsIgmpSnpgMRouterAddress": tlsIgmpSnpgMRouterAddress,
       "tlsIgmpSnpgMRouterLocale": tlsIgmpSnpgMRouterLocale,
       "tlsIgmpSnpgMRouterPortId": tlsIgmpSnpgMRouterPortId,
       "tlsIgmpSnpgMRouterEncapValue": tlsIgmpSnpgMRouterEncapValue,
       "tlsIgmpSnpgMRouterSdpId": tlsIgmpSnpgMRouterSdpId,
       "tlsIgmpSnpgMRouterVcId": tlsIgmpSnpgMRouterVcId,
       "tlsIgmpSnpgMRouterVersion": tlsIgmpSnpgMRouterVersion,
       "tlsIgmpSnpgMRouterExpiryTime": tlsIgmpSnpgMRouterExpiryTime,
       "tlsIgmpSnpgMRouterUpTime": tlsIgmpSnpgMRouterUpTime,
       "tlsIgmpSnpgMRouterGenQueryIntvl": tlsIgmpSnpgMRouterGenQueryIntvl,
       "tlsIgmpSnpgMRouterGenRespIntvl": tlsIgmpSnpgMRouterGenRespIntvl,
       "tlsIgmpSnpgMRouterRobustCount": tlsIgmpSnpgMRouterRobustCount,
       "tlsIgmpSnpgMRouterVRtrId": tlsIgmpSnpgMRouterVRtrId,
       "tlsIgmpSnpgMRouterIfIndex": tlsIgmpSnpgMRouterIfIndex,
       "alxIgmpSnoopingSapObjs": alxIgmpSnoopingSapObjs,
       "sapIgmpSnpgConfigTable": sapIgmpSnpgConfigTable,
       "sapIgmpSnpgConfigEntry": sapIgmpSnpgConfigEntry,
       "sapIgmpSnpgCfgImportPlcy": sapIgmpSnpgCfgImportPlcy,
       "sapIgmpSnpgCfgFastLeave": sapIgmpSnpgCfgFastLeave,
       "sapIgmpSnpgCfgMRouter": sapIgmpSnpgCfgMRouter,
       "sapIgmpSnpgCfgSendQueries": sapIgmpSnpgCfgSendQueries,
       "sapIgmpSnpgCfgGenQueryIntvl": sapIgmpSnpgCfgGenQueryIntvl,
       "sapIgmpSnpgCfgQueryRespIntvl": sapIgmpSnpgCfgQueryRespIntvl,
       "sapIgmpSnpgCfgRobustCount": sapIgmpSnpgCfgRobustCount,
       "sapIgmpSnpgCfgLastMembIntvl": sapIgmpSnpgCfgLastMembIntvl,
       "sapIgmpSnpgCfgMaxNbrGrps": sapIgmpSnpgCfgMaxNbrGrps,
       "sapIgmpSnpgCfgMvrFromVplsId": sapIgmpSnpgCfgMvrFromVplsId,
       "sapIgmpSnpgCfgMvrToSapPortId": sapIgmpSnpgCfgMvrToSapPortId,
       "sapIgmpSnpgCfgMvrToSapEncapVal": sapIgmpSnpgCfgMvrToSapEncapVal,
       "sapIgmpSnpgCfgVersion": sapIgmpSnpgCfgVersion,
       "sapIgmpSnpgCfgMcacPolicyName": sapIgmpSnpgCfgMcacPolicyName,
       "sapIgmpSnpgCfgMcacUnconstBW": sapIgmpSnpgCfgMcacUnconstBW,
       "sapIgmpSnpgCfgMcacConstAdmSt": sapIgmpSnpgCfgMcacConstAdmSt,
       "sapIgmpSnpgCfgMcacPrRsvMndBW": sapIgmpSnpgCfgMcacPrRsvMndBW,
       "sapIgmpSnpgCfgMcacinUseMandBw": sapIgmpSnpgCfgMcacinUseMandBw,
       "sapIgmpSnpgCfgMcacinUseOpnlBw": sapIgmpSnpgCfgMcacinUseOpnlBw,
       "sapIgmpSnpgCfgMcacAvailMandBw": sapIgmpSnpgCfgMcacAvailMandBw,
       "sapIgmpSnpgCfgMcacAvailOpnlBw": sapIgmpSnpgCfgMcacAvailOpnlBw,
       "sapIgmpSnpgCfgMcacValInTrans": sapIgmpSnpgCfgMcacValInTrans,
       "sapIgmpSnpgCfgLastChangeTime": sapIgmpSnpgCfgLastChangeTime,
       "sapIgmpSnpgCfgMaxNbrSrcs": sapIgmpSnpgCfgMaxNbrSrcs,
       "sapIgmpSnpgCfgDisRtrAlertChk": sapIgmpSnpgCfgDisRtrAlertChk,
       "sapIgmpSnpgCfgMaxNbrGrpSrcs": sapIgmpSnpgCfgMaxNbrGrpSrcs,
       "sapIgmpSnpgCfgMcacUseLagPortWt": sapIgmpSnpgCfgMcacUseLagPortWt,
       "sapIgmpSnpgGroupTable": sapIgmpSnpgGroupTable,
       "sapIgmpSnpgGroupEntry": sapIgmpSnpgGroupEntry,
       "sapIgmpSnpgGrpAddress": sapIgmpSnpgGrpAddress,
       "sapIgmpSnpgGrpType": sapIgmpSnpgGrpType,
       "sapIgmpSnpgGrpFilterMode": sapIgmpSnpgGrpFilterMode,
       "sapIgmpSnpgGrpUpTime": sapIgmpSnpgGrpUpTime,
       "sapIgmpSnpgGrpExpiryTime": sapIgmpSnpgGrpExpiryTime,
       "sapIgmpSnpgGrpCompatMode": sapIgmpSnpgGrpCompatMode,
       "sapIgmpSnpgGrpV1HostExpTime": sapIgmpSnpgGrpV1HostExpTime,
       "sapIgmpSnpgGrpV2HostExpTime": sapIgmpSnpgGrpV2HostExpTime,
       "sapIgmpSnpgGrpMvrFromVplsId": sapIgmpSnpgGrpMvrFromVplsId,
       "sapIgmpSnpgGrpMvrToSapPortId": sapIgmpSnpgGrpMvrToSapPortId,
       "sapIgmpSnpgGrpMvrToSapEncapVal": sapIgmpSnpgGrpMvrToSapEncapVal,
       "sapIgmpSnpgGrpSrcTable": sapIgmpSnpgGrpSrcTable,
       "sapIgmpSnpgGrpSrcEntry": sapIgmpSnpgGrpSrcEntry,
       "sapIgmpSnpgGrpSrcAddr": sapIgmpSnpgGrpSrcAddr,
       "sapIgmpSnpgGrpSrcType": sapIgmpSnpgGrpSrcType,
       "sapIgmpSnpgGrpSrcUpTime": sapIgmpSnpgGrpSrcUpTime,
       "sapIgmpSnpgGrpSrcExpiryTime": sapIgmpSnpgGrpSrcExpiryTime,
       "sapIgmpSnpgStaticGrpSrcTable": sapIgmpSnpgStaticGrpSrcTable,
       "sapIgmpSnpgStaticGrpSrcEntry": sapIgmpSnpgStaticGrpSrcEntry,
       "sapIgmpSnpgStaticGroupAddr": sapIgmpSnpgStaticGroupAddr,
       "sapIgmpSnpgStaticSourceAddr": sapIgmpSnpgStaticSourceAddr,
       "sapIgmpSnpgStaticRowstatus": sapIgmpSnpgStaticRowstatus,
       "sapIgmpSnpgStaticLastChangeTime": sapIgmpSnpgStaticLastChangeTime,
       "sapIgmpSnpgStatsTable": sapIgmpSnpgStatsTable,
       "sapIgmpSnpgStatsEntry": sapIgmpSnpgStatsEntry,
       "sapIgmpSnpgTxGenQueries": sapIgmpSnpgTxGenQueries,
       "sapIgmpSnpgTxGrpSpecQueries": sapIgmpSnpgTxGrpSpecQueries,
       "sapIgmpSnpgTxSrcSpecQueries": sapIgmpSnpgTxSrcSpecQueries,
       "sapIgmpSnpgTxV1Reports": sapIgmpSnpgTxV1Reports,
       "sapIgmpSnpgTxV2Reports": sapIgmpSnpgTxV2Reports,
       "sapIgmpSnpgTxV3Reports": sapIgmpSnpgTxV3Reports,
       "sapIgmpSnpgTxV2Leaves": sapIgmpSnpgTxV2Leaves,
       "sapIgmpSnpgRxGenQueries": sapIgmpSnpgRxGenQueries,
       "sapIgmpSnpgRxGrpSpecQueries": sapIgmpSnpgRxGrpSpecQueries,
       "sapIgmpSnpgRxSrcSpecQueries": sapIgmpSnpgRxSrcSpecQueries,
       "sapIgmpSnpgRxV1Reports": sapIgmpSnpgRxV1Reports,
       "sapIgmpSnpgRxV2Reports": sapIgmpSnpgRxV2Reports,
       "sapIgmpSnpgRxV3Reports": sapIgmpSnpgRxV3Reports,
       "sapIgmpSnpgRxV2Leaves": sapIgmpSnpgRxV2Leaves,
       "sapIgmpSnpgRxUnknownType": sapIgmpSnpgRxUnknownType,
       "sapIgmpSnpgFwdGenQueries": sapIgmpSnpgFwdGenQueries,
       "sapIgmpSnpgFwdGrpSpecQueries": sapIgmpSnpgFwdGrpSpecQueries,
       "sapIgmpSnpgFwdSrcSpecQueries": sapIgmpSnpgFwdSrcSpecQueries,
       "sapIgmpSnpgFwdV1Reports": sapIgmpSnpgFwdV1Reports,
       "sapIgmpSnpgFwdV2Reports": sapIgmpSnpgFwdV2Reports,
       "sapIgmpSnpgFwdV3Reports": sapIgmpSnpgFwdV3Reports,
       "sapIgmpSnpgFwdV2Leaves": sapIgmpSnpgFwdV2Leaves,
       "sapIgmpSnpgFwdUnknownType": sapIgmpSnpgFwdUnknownType,
       "sapIgmpSnpgRxBadLenPkts": sapIgmpSnpgRxBadLenPkts,
       "sapIgmpSnpgRxBadIpChksmPkts": sapIgmpSnpgRxBadIpChksmPkts,
       "sapIgmpSnpgRxBadIgmpChksmPkts": sapIgmpSnpgRxBadIgmpChksmPkts,
       "sapIgmpSnpgRxBadEncodedPkts": sapIgmpSnpgRxBadEncodedPkts,
       "sapIgmpSnpgRxNoRtrAlertPkts": sapIgmpSnpgRxNoRtrAlertPkts,
       "sapIgmpSnpgRxZeroSrcAdrPkts": sapIgmpSnpgRxZeroSrcAdrPkts,
       "sapIgmpSnpgSendQueryCfgDrops": sapIgmpSnpgSendQueryCfgDrops,
       "sapIgmpSnpgImportPolicyDrops": sapIgmpSnpgImportPolicyDrops,
       "sapIgmpSnpgMaxNumGroupsDrops": sapIgmpSnpgMaxNumGroupsDrops,
       "sapIgmpSnpgMvrFromVplsCfgDrops": sapIgmpSnpgMvrFromVplsCfgDrops,
       "sapIgmpSnpgMvrToSapCfgDrops": sapIgmpSnpgMvrToSapCfgDrops,
       "sapIgmpSnpgRxWrongVersionPkts": sapIgmpSnpgRxWrongVersionPkts,
       "sapIgmpSnpgMcacPolicyDrops": sapIgmpSnpgMcacPolicyDrops,
       "sapIgmpSnpgMcsFailures": sapIgmpSnpgMcsFailures,
       "sapIgmpSnpgRxLocalScopePkts": sapIgmpSnpgRxLocalScopePkts,
       "sapIgmpSnpgRxRsvdScopePkts": sapIgmpSnpgRxRsvdScopePkts,
       "sapIgmpSnpgMaxNumSourcesDrops": sapIgmpSnpgMaxNumSourcesDrops,
       "sapIgmpSnpgMaxNumGrpSrcsDrops": sapIgmpSnpgMaxNumGrpSrcsDrops,
       "sapIgmpSnpgMcacLevelTable": sapIgmpSnpgMcacLevelTable,
       "sapIgmpSnpgMcacLevelEntry": sapIgmpSnpgMcacLevelEntry,
       "sapIgmpSnpgCfgMcacLevelRowStat": sapIgmpSnpgCfgMcacLevelRowStat,
       "sapIgmpSnpgCfgMcacLevelBW": sapIgmpSnpgCfgMcacLevelBW,
       "sapIgmpSnpgCfgMcacLevelLastChngT": sapIgmpSnpgCfgMcacLevelLastChngT,
       "sapIgmpSnpgMcacLagTable": sapIgmpSnpgMcacLagTable,
       "sapIgmpSnpgMcacLagEntry": sapIgmpSnpgMcacLagEntry,
       "sapIgmpSnpgCfgMcacLagRowStat": sapIgmpSnpgCfgMcacLagRowStat,
       "sapIgmpSnpgCfgMcacLagLevel": sapIgmpSnpgCfgMcacLagLevel,
       "sapIgmpSnpgCfgMcacLagLastChangeT": sapIgmpSnpgCfgMcacLagLastChangeT,
       "alxIgmpSnoopingSdpBindObjs": alxIgmpSnoopingSdpBindObjs,
       "sdpBindIgmpSnpgConfigTable": sdpBindIgmpSnpgConfigTable,
       "sdpBindIgmpSnpgConfigEntry": sdpBindIgmpSnpgConfigEntry,
       "sdpBndIgmpSnpgCfgImportPlcy": sdpBndIgmpSnpgCfgImportPlcy,
       "sdpBndIgmpSnpgCfgFastLeave": sdpBndIgmpSnpgCfgFastLeave,
       "sdpBndIgmpSnpgCfgMRouter": sdpBndIgmpSnpgCfgMRouter,
       "sdpBndIgmpSnpgCfgSendQueries": sdpBndIgmpSnpgCfgSendQueries,
       "sdpBndIgmpSnpgCfgGenQueryIntvl": sdpBndIgmpSnpgCfgGenQueryIntvl,
       "sdpBndIgmpSnpgCfgQueryRespIntvl": sdpBndIgmpSnpgCfgQueryRespIntvl,
       "sdpBndIgmpSnpgCfgRobustCount": sdpBndIgmpSnpgCfgRobustCount,
       "sdpBndIgmpSnpgCfgLastMembIntvl": sdpBndIgmpSnpgCfgLastMembIntvl,
       "sdpBndIgmpSnpgCfgMaxNbrGrps": sdpBndIgmpSnpgCfgMaxNbrGrps,
       "sdpBndIgmpSnpgCfgVersion": sdpBndIgmpSnpgCfgVersion,
       "sdpBndIgmpSnpgCfgMcacPolicyName": sdpBndIgmpSnpgCfgMcacPolicyName,
       "sdpBndIgmpSnpgCfgMcacUnconstBW": sdpBndIgmpSnpgCfgMcacUnconstBW,
       "sdpBndIgmpSnpgCfgMcacPrRsvMndBW": sdpBndIgmpSnpgCfgMcacPrRsvMndBW,
       "sdpBndIgmpSnpgCfgMcacinUseMndBw": sdpBndIgmpSnpgCfgMcacinUseMndBw,
       "sdpBndIgmpSnpgCfgMcacinUseOplBw": sdpBndIgmpSnpgCfgMcacinUseOplBw,
       "sdpBndIgmpSnpgCfgMcacAvailMndBw": sdpBndIgmpSnpgCfgMcacAvailMndBw,
       "sdpBndIgmpSnpgCfgMcacAvailOplBw": sdpBndIgmpSnpgCfgMcacAvailOplBw,
       "sdpBndIgmpSnpgCfgMcacValInTrans": sdpBndIgmpSnpgCfgMcacValInTrans,
       "sdpBndIgmpSnpgCfgLastChangeTime": sdpBndIgmpSnpgCfgLastChangeTime,
       "sdpBndIgmpSnpgCfgMaxNbrSrcs": sdpBndIgmpSnpgCfgMaxNbrSrcs,
       "sdpBndIgmpSnpgCfgDisRtrAlertChk": sdpBndIgmpSnpgCfgDisRtrAlertChk,
       "sdpBndIgmpSnpgCfgMaxNbrGrpSrcs": sdpBndIgmpSnpgCfgMaxNbrGrpSrcs,
       "sdpBindIgmpSnpgGroupTable": sdpBindIgmpSnpgGroupTable,
       "sdpBindIgmpSnpgGroupEntry": sdpBindIgmpSnpgGroupEntry,
       "sdpBndIgmpSnpgGrpAddress": sdpBndIgmpSnpgGrpAddress,
       "sdpBndIgmpSnpgGrpType": sdpBndIgmpSnpgGrpType,
       "sdpBndIgmpSnpgGrpFilterMode": sdpBndIgmpSnpgGrpFilterMode,
       "sdpBndIgmpSnpgGrpUpTime": sdpBndIgmpSnpgGrpUpTime,
       "sdpBndIgmpSnpgGrpExpiryTime": sdpBndIgmpSnpgGrpExpiryTime,
       "sdpBndIgmpSnpgGrpCompatMode": sdpBndIgmpSnpgGrpCompatMode,
       "sdpBndIgmpSnpgGrpV1HostExpTime": sdpBndIgmpSnpgGrpV1HostExpTime,
       "sdpBndIgmpSnpgGrpV2HostExpTime": sdpBndIgmpSnpgGrpV2HostExpTime,
       "sdpBindIgmpSnpgGrpSrcTable": sdpBindIgmpSnpgGrpSrcTable,
       "sdpBindIgmpSnpgGrpSrcEntry": sdpBindIgmpSnpgGrpSrcEntry,
       "sdpBndIgmpSnpgGrpSrcAddr": sdpBndIgmpSnpgGrpSrcAddr,
       "sdpBndIgmpSnpgGrpSrcType": sdpBndIgmpSnpgGrpSrcType,
       "sdpBndIgmpSnpgGrpSrcUpTime": sdpBndIgmpSnpgGrpSrcUpTime,
       "sdpBndIgmpSnpgGrpSrcExpiryTime": sdpBndIgmpSnpgGrpSrcExpiryTime,
       "sdpBindIgmpSnpgStaticGrpSrcTable": sdpBindIgmpSnpgStaticGrpSrcTable,
       "sdpBindIgmpSnpgStatGrpSrcEntry": sdpBindIgmpSnpgStatGrpSrcEntry,
       "sdpBndIgmpSnpgStaticGroupAddr": sdpBndIgmpSnpgStaticGroupAddr,
       "sdpBndIgmpSnpgStaticSourceAddr": sdpBndIgmpSnpgStaticSourceAddr,
       "sdpBndIgmpSnpgStaticRowstatus": sdpBndIgmpSnpgStaticRowstatus,
       "sdpBndIgmpSnpgStaticLastChange": sdpBndIgmpSnpgStaticLastChange,
       "sdpBindIgmpSnpgStatsTable": sdpBindIgmpSnpgStatsTable,
       "sdpBindIgmpSnpgStatsEntry": sdpBindIgmpSnpgStatsEntry,
       "sdpBndIgmpSnpgTxGenQueries": sdpBndIgmpSnpgTxGenQueries,
       "sdpBndIgmpSnpgTxGrpSpecQueries": sdpBndIgmpSnpgTxGrpSpecQueries,
       "sdpBndIgmpSnpgTxSrcSpecQueries": sdpBndIgmpSnpgTxSrcSpecQueries,
       "sdpBndIgmpSnpgTxV1Reports": sdpBndIgmpSnpgTxV1Reports,
       "sdpBndIgmpSnpgTxV2Reports": sdpBndIgmpSnpgTxV2Reports,
       "sdpBndIgmpSnpgTxV3Reports": sdpBndIgmpSnpgTxV3Reports,
       "sdpBndIgmpSnpgTxV2Leaves": sdpBndIgmpSnpgTxV2Leaves,
       "sdpBndIgmpSnpgRxGenQueries": sdpBndIgmpSnpgRxGenQueries,
       "sdpBndIgmpSnpgRxGrpSpecQueries": sdpBndIgmpSnpgRxGrpSpecQueries,
       "sdpBndIgmpSnpgRxSrcSpecQueries": sdpBndIgmpSnpgRxSrcSpecQueries,
       "sdpBndIgmpSnpgRxV1Reports": sdpBndIgmpSnpgRxV1Reports,
       "sdpBndIgmpSnpgRxV2Reports": sdpBndIgmpSnpgRxV2Reports,
       "sdpBndIgmpSnpgRxV3Reports": sdpBndIgmpSnpgRxV3Reports,
       "sdpBndIgmpSnpgRxV2Leaves": sdpBndIgmpSnpgRxV2Leaves,
       "sdpBndIgmpSnpgRxUnknownType": sdpBndIgmpSnpgRxUnknownType,
       "sdpBndIgmpSnpgFwdGenQueries": sdpBndIgmpSnpgFwdGenQueries,
       "sdpBndIgmpSnpgFwdGrpSpecQueries": sdpBndIgmpSnpgFwdGrpSpecQueries,
       "sdpBndIgmpSnpgFwdSrcSpecQueries": sdpBndIgmpSnpgFwdSrcSpecQueries,
       "sdpBndIgmpSnpgFwdV1Reports": sdpBndIgmpSnpgFwdV1Reports,
       "sdpBndIgmpSnpgFwdV2Reports": sdpBndIgmpSnpgFwdV2Reports,
       "sdpBndIgmpSnpgFwdV3Reports": sdpBndIgmpSnpgFwdV3Reports,
       "sdpBndIgmpSnpgFwdV2Leaves": sdpBndIgmpSnpgFwdV2Leaves,
       "sdpBndIgmpSnpgFwdUnknownType": sdpBndIgmpSnpgFwdUnknownType,
       "sdpBndIgmpSnpgRxBadLenPkts": sdpBndIgmpSnpgRxBadLenPkts,
       "sdpBndIgmpSnpgRxBadIpChksmPkts": sdpBndIgmpSnpgRxBadIpChksmPkts,
       "sdpBndIgmpSnpgRxBadIgmpChksmPkts": sdpBndIgmpSnpgRxBadIgmpChksmPkts,
       "sdpBndIgmpSnpgRxBadEncodedPkts": sdpBndIgmpSnpgRxBadEncodedPkts,
       "sdpBndIgmpSnpgRxNoRtrAlertPkts": sdpBndIgmpSnpgRxNoRtrAlertPkts,
       "sdpBndIgmpSnpgRxZeroSrcAdrPkts": sdpBndIgmpSnpgRxZeroSrcAdrPkts,
       "sdpBndIgmpSnpgSendQueryCfgDrops": sdpBndIgmpSnpgSendQueryCfgDrops,
       "sdpBndIgmpSnpgImportPolicyDrops": sdpBndIgmpSnpgImportPolicyDrops,
       "sdpBndIgmpSnpgMaxNumGroupsDrops": sdpBndIgmpSnpgMaxNumGroupsDrops,
       "sdpBndIgmpSnpgRxWrongVersionPkts": sdpBndIgmpSnpgRxWrongVersionPkts,
       "sdpBndIgmpSnpgMcacPolicyDrops": sdpBndIgmpSnpgMcacPolicyDrops,
       "sdpBndIgmpSnpgRxLocalScopePkts": sdpBndIgmpSnpgRxLocalScopePkts,
       "sdpBndIgmpSnpgRxRsvdScopePkts": sdpBndIgmpSnpgRxRsvdScopePkts,
       "sdpBndIgmpSnpgMaxNumSourcesDrops": sdpBndIgmpSnpgMaxNumSourcesDrops,
       "sdpBndIgmpSnpgMaxNumGrpSrcsDrops": sdpBndIgmpSnpgMaxNumGrpSrcsDrops,
       "alxIgmpSnoopingNotificationObjs": alxIgmpSnoopingNotificationObjs,
       "alxIgmpSnpgGroupAddress": alxIgmpSnpgGroupAddress,
       "alxIgmpSnpgMcsFailureReason": alxIgmpSnpgMcsFailureReason,
       "alxIgmpSnpgSourceAddress": alxIgmpSnpgSourceAddress,
       "alxIgmpSnpgDescription": alxIgmpSnpgDescription,
       "alxIgmpSnoopingTimeStampObjs": alxIgmpSnoopingTimeStampObjs,
       "tlsIgmpSnpgConfigTableLastChange": tlsIgmpSnpgConfigTableLastChange,
       "sapIgmpSnpgConfigTableLastChange": sapIgmpSnpgConfigTableLastChange,
       "sapIgmpSnpgStaticGrpSrcTablLstCh": sapIgmpSnpgStaticGrpSrcTablLstCh,
       "sapIgmpSnpgMcacLevelTableLstCh": sapIgmpSnpgMcacLevelTableLstCh,
       "sapIgmpSnpgMcacLagTableLastChng": sapIgmpSnpgMcacLagTableLastChng,
       "sdpBindIgmpSnpgConfigTableLstCh": sdpBindIgmpSnpgConfigTableLstCh,
       "sdpBindIgmpSnpgStaticGrpSrcTblLC": sdpBindIgmpSnpgStaticGrpSrcTblLC,
       "alxIgmpSnoopingNotifyPrefix": alxIgmpSnoopingNotifyPrefix,
       "alxIgmpSnoopingSapPrefix": alxIgmpSnoopingSapPrefix,
       "alxIgmpSnpgSapNotifications": alxIgmpSnpgSapNotifications,
       "sapIgmpSnpgGrpLimitExceeded": sapIgmpSnpgGrpLimitExceeded,
       "sapIgmpSnpgMcacPlcyDropped": sapIgmpSnpgMcacPlcyDropped,
       "sapIgmpSnpgMcsFailure": sapIgmpSnpgMcsFailure,
       "sapIgmpSnpgSrcLimitExceeded": sapIgmpSnpgSrcLimitExceeded,
       "sapIgmpSnpgGrpSrcLimitExceeded": sapIgmpSnpgGrpSrcLimitExceeded,
       "alxIgmpSnoopingSdpBndPrefix": alxIgmpSnoopingSdpBndPrefix,
       "alxIgmpSnpgSdpBndNotifications": alxIgmpSnpgSdpBndNotifications,
       "sdpBndIgmpSnpgGrpLimitExceeded": sdpBndIgmpSnpgGrpLimitExceeded,
       "sdpBndIgmpSnpgMcacPlcyDropped": sdpBndIgmpSnpgMcacPlcyDropped,
       "sdpBndIgmpSnpgSrcLimitExceeded": sdpBndIgmpSnpgSrcLimitExceeded,
       "sdpBndIgmpSnpgGrpSrcLimitExceed": sdpBndIgmpSnpgGrpSrcLimitExceed}
)
