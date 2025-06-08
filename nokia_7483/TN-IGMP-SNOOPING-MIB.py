# SNMP MIB module (TN-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-IGMP-SNOOPING-MIB.mib
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

(tnSapEncapValue,
 tnSapPortId) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapEncapValue",
    "tnSapPortId")

(SdpId,
 tnSvcId) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "SdpId",
    "tnSvcId")

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
    "TN-TC-MIB",
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

tnIgmpSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnIgmpSnoopingMIBModule.setRevisions(
        ("1912-12-05 00:00",
         "1912-09-01 00:00",
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnIgmpSnoopingObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingObjs = _TnIgmpSnoopingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24)
)
_TnIgmpSnoopingTlsObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingTlsObjs = _TnIgmpSnoopingTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1)
)
_TnTlsIgmpSnpgConfigTable_Object = MibTable
tnTlsIgmpSnpgConfigTable = _TnTlsIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgConfigTable.setStatus("current")
_TnTlsIgmpSnpgConfigEntry_Object = MibTableRow
tnTlsIgmpSnpgConfigEntry = _TnTlsIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1)
)
tnTlsIgmpSnpgConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgConfigEntry.setStatus("current")


class _TnTlsIgmpSnpgCfgAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tnTlsIgmpSnpgCfgAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnTlsIgmpSnpgCfgAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnTlsIgmpSnpgCfgAdminState_Object = MibTableColumn
tnTlsIgmpSnpgCfgAdminState = _TnTlsIgmpSnpgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 1),
    _TnTlsIgmpSnpgCfgAdminState_Type()
)
tnTlsIgmpSnpgCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgAdminState.setStatus("current")


class _TnTlsIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tnTlsIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnTlsIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TnTlsIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
tnTlsIgmpSnpgCfgGenQueryIntvl = _TnTlsIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 2),
    _TnTlsIgmpSnpgCfgGenQueryIntvl_Type()
)
tnTlsIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TnTlsIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tnTlsIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnTlsIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TnTlsIgmpSnpgCfgRobustCount_Object = MibTableColumn
tnTlsIgmpSnpgCfgRobustCount = _TnTlsIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 3),
    _TnTlsIgmpSnpgCfgRobustCount_Type()
)
tnTlsIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgRobustCount.setStatus("current")


class _TnTlsIgmpSnpgCfgReportSrcAddress_Type(IpAddress):
    """Custom type tnTlsIgmpSnpgCfgReportSrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnTlsIgmpSnpgCfgReportSrcAddress_Type.__name__ = "IpAddress"
_TnTlsIgmpSnpgCfgReportSrcAddress_Object = MibTableColumn
tnTlsIgmpSnpgCfgReportSrcAddress = _TnTlsIgmpSnpgCfgReportSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 4),
    _TnTlsIgmpSnpgCfgReportSrcAddress_Type()
)
tnTlsIgmpSnpgCfgReportSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgReportSrcAddress.setStatus("current")


class _TnTlsIgmpSnpgCfgMvrAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tnTlsIgmpSnpgCfgMvrAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnTlsIgmpSnpgCfgMvrAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnTlsIgmpSnpgCfgMvrAdminState_Object = MibTableColumn
tnTlsIgmpSnpgCfgMvrAdminState = _TnTlsIgmpSnpgCfgMvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 5),
    _TnTlsIgmpSnpgCfgMvrAdminState_Type()
)
tnTlsIgmpSnpgCfgMvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgMvrAdminState.setStatus("current")


class _TnTlsIgmpSnpgCfgMvrDescription_Type(TItemDescription):
    """Custom type tnTlsIgmpSnpgCfgMvrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TnTlsIgmpSnpgCfgMvrDescription_Type.__name__ = "TItemDescription"
_TnTlsIgmpSnpgCfgMvrDescription_Object = MibTableColumn
tnTlsIgmpSnpgCfgMvrDescription = _TnTlsIgmpSnpgCfgMvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 6),
    _TnTlsIgmpSnpgCfgMvrDescription_Type()
)
tnTlsIgmpSnpgCfgMvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgMvrDescription.setStatus("current")


class _TnTlsIgmpSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnTlsIgmpSnpgCfgMvrPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnTlsIgmpSnpgCfgMvrPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnTlsIgmpSnpgCfgMvrPolicy_Object = MibTableColumn
tnTlsIgmpSnpgCfgMvrPolicy = _TnTlsIgmpSnpgCfgMvrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 7),
    _TnTlsIgmpSnpgCfgMvrPolicy_Type()
)
tnTlsIgmpSnpgCfgMvrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgMvrPolicy.setStatus("current")


class _TnTlsIgmpSnpgCfgQuerySrcAddress_Type(IpAddress):
    """Custom type tnTlsIgmpSnpgCfgQuerySrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnTlsIgmpSnpgCfgQuerySrcAddress_Type.__name__ = "IpAddress"
_TnTlsIgmpSnpgCfgQuerySrcAddress_Object = MibTableColumn
tnTlsIgmpSnpgCfgQuerySrcAddress = _TnTlsIgmpSnpgCfgQuerySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 8),
    _TnTlsIgmpSnpgCfgQuerySrcAddress_Type()
)
tnTlsIgmpSnpgCfgQuerySrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgQuerySrcAddress.setStatus("current")


class _TnTlsIgmpSnpgCfgQuerySrcAddrType_Type(Integer32):
    """Custom type tnTlsIgmpSnpgCfgQuerySrcAddrType based on Integer32"""
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


_TnTlsIgmpSnpgCfgQuerySrcAddrType_Type.__name__ = "Integer32"
_TnTlsIgmpSnpgCfgQuerySrcAddrType_Object = MibTableColumn
tnTlsIgmpSnpgCfgQuerySrcAddrType = _TnTlsIgmpSnpgCfgQuerySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 9),
    _TnTlsIgmpSnpgCfgQuerySrcAddrType_Type()
)
tnTlsIgmpSnpgCfgQuerySrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgQuerySrcAddrType.setStatus("current")
_TnTlsIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_TnTlsIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
tnTlsIgmpSnpgCfgLastChangeTime = _TnTlsIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 10),
    _TnTlsIgmpSnpgCfgLastChangeTime_Type()
)
tnTlsIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgLastChangeTime.setStatus("current")
_TnTlsIgmpSnpgQuerierTable_Object = MibTable
tnTlsIgmpSnpgQuerierTable = _TnTlsIgmpSnpgQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierTable.setStatus("current")
_TnTlsIgmpSnpgQuerierEntry_Object = MibTableRow
tnTlsIgmpSnpgQuerierEntry = _TnTlsIgmpSnpgQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1)
)
tnTlsIgmpSnpgQuerierEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierEntry.setStatus("current")
_TnTlsIgmpSnpgQuerierVersion_Type = TmnxIgmpVersion
_TnTlsIgmpSnpgQuerierVersion_Object = MibTableColumn
tnTlsIgmpSnpgQuerierVersion = _TnTlsIgmpSnpgQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 1),
    _TnTlsIgmpSnpgQuerierVersion_Type()
)
tnTlsIgmpSnpgQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierVersion.setStatus("current")
_TnTlsIgmpSnpgQuerierAddress_Type = IpAddress
_TnTlsIgmpSnpgQuerierAddress_Object = MibTableColumn
tnTlsIgmpSnpgQuerierAddress = _TnTlsIgmpSnpgQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 2),
    _TnTlsIgmpSnpgQuerierAddress_Type()
)
tnTlsIgmpSnpgQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierAddress.setStatus("current")
_TnTlsIgmpSnpgQuerierLocale_Type = AlxIgmpSnpgLocation
_TnTlsIgmpSnpgQuerierLocale_Object = MibTableColumn
tnTlsIgmpSnpgQuerierLocale = _TnTlsIgmpSnpgQuerierLocale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 3),
    _TnTlsIgmpSnpgQuerierLocale_Type()
)
tnTlsIgmpSnpgQuerierLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierLocale.setStatus("current")
_TnTlsIgmpSnpgQuerierPortId_Type = TmnxPortID
_TnTlsIgmpSnpgQuerierPortId_Object = MibTableColumn
tnTlsIgmpSnpgQuerierPortId = _TnTlsIgmpSnpgQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 4),
    _TnTlsIgmpSnpgQuerierPortId_Type()
)
tnTlsIgmpSnpgQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierPortId.setStatus("current")
_TnTlsIgmpSnpgQuerierEncapValue_Type = TmnxEncapVal
_TnTlsIgmpSnpgQuerierEncapValue_Object = MibTableColumn
tnTlsIgmpSnpgQuerierEncapValue = _TnTlsIgmpSnpgQuerierEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 5),
    _TnTlsIgmpSnpgQuerierEncapValue_Type()
)
tnTlsIgmpSnpgQuerierEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierEncapValue.setStatus("current")
_TnTlsIgmpSnpgQuerierSdpId_Type = SdpId
_TnTlsIgmpSnpgQuerierSdpId_Object = MibTableColumn
tnTlsIgmpSnpgQuerierSdpId = _TnTlsIgmpSnpgQuerierSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 6),
    _TnTlsIgmpSnpgQuerierSdpId_Type()
)
tnTlsIgmpSnpgQuerierSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierSdpId.setStatus("current")
_TnTlsIgmpSnpgQuerierVcId_Type = TmnxVcIdOrNone
_TnTlsIgmpSnpgQuerierVcId_Object = MibTableColumn
tnTlsIgmpSnpgQuerierVcId = _TnTlsIgmpSnpgQuerierVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 7),
    _TnTlsIgmpSnpgQuerierVcId_Type()
)
tnTlsIgmpSnpgQuerierVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierVcId.setStatus("current")
_TnTlsIgmpSnpgQuerierUpTime_Type = TimeTicks
_TnTlsIgmpSnpgQuerierUpTime_Object = MibTableColumn
tnTlsIgmpSnpgQuerierUpTime = _TnTlsIgmpSnpgQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 8),
    _TnTlsIgmpSnpgQuerierUpTime_Type()
)
tnTlsIgmpSnpgQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierUpTime.setStatus("current")
_TnTlsIgmpSnpgQuerierExpiryTime_Type = Unsigned32
_TnTlsIgmpSnpgQuerierExpiryTime_Object = MibTableColumn
tnTlsIgmpSnpgQuerierExpiryTime = _TnTlsIgmpSnpgQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 9),
    _TnTlsIgmpSnpgQuerierExpiryTime_Type()
)
tnTlsIgmpSnpgQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierExpiryTime.setUnits("seconds")
_TnTlsIgmpSnpgQuerierGenQueryIntvl_Type = Unsigned32
_TnTlsIgmpSnpgQuerierGenQueryIntvl_Object = MibTableColumn
tnTlsIgmpSnpgQuerierGenQueryIntvl = _TnTlsIgmpSnpgQuerierGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 10),
    _TnTlsIgmpSnpgQuerierGenQueryIntvl_Type()
)
tnTlsIgmpSnpgQuerierGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenQueryIntvl.setUnits("seconds")
_TnTlsIgmpSnpgQuerierGenRespIntvl_Type = Unsigned32
_TnTlsIgmpSnpgQuerierGenRespIntvl_Object = MibTableColumn
tnTlsIgmpSnpgQuerierGenRespIntvl = _TnTlsIgmpSnpgQuerierGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 11),
    _TnTlsIgmpSnpgQuerierGenRespIntvl_Type()
)
tnTlsIgmpSnpgQuerierGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenRespIntvl.setUnits("deci-seconds")
_TnTlsIgmpSnpgQuerierRobustCount_Type = Unsigned32
_TnTlsIgmpSnpgQuerierRobustCount_Object = MibTableColumn
tnTlsIgmpSnpgQuerierRobustCount = _TnTlsIgmpSnpgQuerierRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 12),
    _TnTlsIgmpSnpgQuerierRobustCount_Type()
)
tnTlsIgmpSnpgQuerierRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierRobustCount.setStatus("current")
_TnTlsIgmpSnpgProxyGroupTable_Object = MibTable
tnTlsIgmpSnpgProxyGroupTable = _TnTlsIgmpSnpgProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupTable.setStatus("current")
_TnTlsIgmpSnpgProxyGroupEntry_Object = MibTableRow
tnTlsIgmpSnpgProxyGroupEntry = _TnTlsIgmpSnpgProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1)
)
tnTlsIgmpSnpgProxyGroupEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgProxyGroupAddress"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupEntry.setStatus("current")
_TnTlsIgmpSnpgProxyGroupAddress_Type = IpAddress
_TnTlsIgmpSnpgProxyGroupAddress_Object = MibTableColumn
tnTlsIgmpSnpgProxyGroupAddress = _TnTlsIgmpSnpgProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1, 1),
    _TnTlsIgmpSnpgProxyGroupAddress_Type()
)
tnTlsIgmpSnpgProxyGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupAddress.setStatus("current")
_TnTlsIgmpSnpgProxyGroupFilterMode_Type = TmnxIgmpGroupFilterMode
_TnTlsIgmpSnpgProxyGroupFilterMode_Object = MibTableColumn
tnTlsIgmpSnpgProxyGroupFilterMode = _TnTlsIgmpSnpgProxyGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1, 2),
    _TnTlsIgmpSnpgProxyGroupFilterMode_Type()
)
tnTlsIgmpSnpgProxyGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupFilterMode.setStatus("current")
_TnTlsIgmpSnpgProxyGroupUpTime_Type = TimeTicks
_TnTlsIgmpSnpgProxyGroupUpTime_Object = MibTableColumn
tnTlsIgmpSnpgProxyGroupUpTime = _TnTlsIgmpSnpgProxyGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1, 3),
    _TnTlsIgmpSnpgProxyGroupUpTime_Type()
)
tnTlsIgmpSnpgProxyGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupUpTime.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcTable_Object = MibTable
tnTlsIgmpSnpgProxyGrpSrcTable = _TnTlsIgmpSnpgProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcTable.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcEntry_Object = MibTableRow
tnTlsIgmpSnpgProxyGrpSrcEntry = _TnTlsIgmpSnpgProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4, 1)
)
tnTlsIgmpSnpgProxyGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgProxyGroupAddress"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcEntry.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcAddr_Type = IpAddress
_TnTlsIgmpSnpgProxyGrpSrcAddr_Object = MibTableColumn
tnTlsIgmpSnpgProxyGrpSrcAddr = _TnTlsIgmpSnpgProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4, 1, 1),
    _TnTlsIgmpSnpgProxyGrpSrcAddr_Type()
)
tnTlsIgmpSnpgProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcAddr.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcUpTime_Type = TimeTicks
_TnTlsIgmpSnpgProxyGrpSrcUpTime_Object = MibTableColumn
tnTlsIgmpSnpgProxyGrpSrcUpTime = _TnTlsIgmpSnpgProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4, 1, 2),
    _TnTlsIgmpSnpgProxyGrpSrcUpTime_Type()
)
tnTlsIgmpSnpgProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcUpTime.setStatus("current")
_TnTlsIgmpSnpgMRouterTable_Object = MibTable
tnTlsIgmpSnpgMRouterTable = _TnTlsIgmpSnpgMRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterTable.setStatus("current")
_TnTlsIgmpSnpgMRouterEntry_Object = MibTableRow
tnTlsIgmpSnpgMRouterEntry = _TnTlsIgmpSnpgMRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1)
)
tnTlsIgmpSnpgMRouterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgMRouterAddress"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterEntry.setStatus("current")
_TnTlsIgmpSnpgMRouterAddress_Type = IpAddress
_TnTlsIgmpSnpgMRouterAddress_Object = MibTableColumn
tnTlsIgmpSnpgMRouterAddress = _TnTlsIgmpSnpgMRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 1),
    _TnTlsIgmpSnpgMRouterAddress_Type()
)
tnTlsIgmpSnpgMRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterAddress.setStatus("current")
_TnTlsIgmpSnpgMRouterLocale_Type = AlxIgmpSnpgLocation
_TnTlsIgmpSnpgMRouterLocale_Object = MibTableColumn
tnTlsIgmpSnpgMRouterLocale = _TnTlsIgmpSnpgMRouterLocale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 2),
    _TnTlsIgmpSnpgMRouterLocale_Type()
)
tnTlsIgmpSnpgMRouterLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterLocale.setStatus("current")
_TnTlsIgmpSnpgMRouterPortId_Type = TmnxPortID
_TnTlsIgmpSnpgMRouterPortId_Object = MibTableColumn
tnTlsIgmpSnpgMRouterPortId = _TnTlsIgmpSnpgMRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 3),
    _TnTlsIgmpSnpgMRouterPortId_Type()
)
tnTlsIgmpSnpgMRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterPortId.setStatus("current")
_TnTlsIgmpSnpgMRouterEncapValue_Type = TmnxEncapVal
_TnTlsIgmpSnpgMRouterEncapValue_Object = MibTableColumn
tnTlsIgmpSnpgMRouterEncapValue = _TnTlsIgmpSnpgMRouterEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 4),
    _TnTlsIgmpSnpgMRouterEncapValue_Type()
)
tnTlsIgmpSnpgMRouterEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterEncapValue.setStatus("current")
_TnTlsIgmpSnpgMRouterSdpId_Type = SdpId
_TnTlsIgmpSnpgMRouterSdpId_Object = MibTableColumn
tnTlsIgmpSnpgMRouterSdpId = _TnTlsIgmpSnpgMRouterSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 5),
    _TnTlsIgmpSnpgMRouterSdpId_Type()
)
tnTlsIgmpSnpgMRouterSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterSdpId.setStatus("current")
_TnTlsIgmpSnpgMRouterVcId_Type = TmnxVcIdOrNone
_TnTlsIgmpSnpgMRouterVcId_Object = MibTableColumn
tnTlsIgmpSnpgMRouterVcId = _TnTlsIgmpSnpgMRouterVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 6),
    _TnTlsIgmpSnpgMRouterVcId_Type()
)
tnTlsIgmpSnpgMRouterVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterVcId.setStatus("current")
_TnTlsIgmpSnpgMRouterVersion_Type = TmnxIgmpVersion
_TnTlsIgmpSnpgMRouterVersion_Object = MibTableColumn
tnTlsIgmpSnpgMRouterVersion = _TnTlsIgmpSnpgMRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 7),
    _TnTlsIgmpSnpgMRouterVersion_Type()
)
tnTlsIgmpSnpgMRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterVersion.setStatus("current")
_TnTlsIgmpSnpgMRouterExpiryTime_Type = Unsigned32
_TnTlsIgmpSnpgMRouterExpiryTime_Object = MibTableColumn
tnTlsIgmpSnpgMRouterExpiryTime = _TnTlsIgmpSnpgMRouterExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 8),
    _TnTlsIgmpSnpgMRouterExpiryTime_Type()
)
tnTlsIgmpSnpgMRouterExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterExpiryTime.setUnits("seconds")
_TnTlsIgmpSnpgMRouterUpTime_Type = TimeTicks
_TnTlsIgmpSnpgMRouterUpTime_Object = MibTableColumn
tnTlsIgmpSnpgMRouterUpTime = _TnTlsIgmpSnpgMRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 9),
    _TnTlsIgmpSnpgMRouterUpTime_Type()
)
tnTlsIgmpSnpgMRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterUpTime.setStatus("current")
_TnTlsIgmpSnpgMRouterGenQueryIntvl_Type = Unsigned32
_TnTlsIgmpSnpgMRouterGenQueryIntvl_Object = MibTableColumn
tnTlsIgmpSnpgMRouterGenQueryIntvl = _TnTlsIgmpSnpgMRouterGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 10),
    _TnTlsIgmpSnpgMRouterGenQueryIntvl_Type()
)
tnTlsIgmpSnpgMRouterGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenQueryIntvl.setUnits("seconds")
_TnTlsIgmpSnpgMRouterGenRespIntvl_Type = Unsigned32
_TnTlsIgmpSnpgMRouterGenRespIntvl_Object = MibTableColumn
tnTlsIgmpSnpgMRouterGenRespIntvl = _TnTlsIgmpSnpgMRouterGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 11),
    _TnTlsIgmpSnpgMRouterGenRespIntvl_Type()
)
tnTlsIgmpSnpgMRouterGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenRespIntvl.setUnits("deci-seconds")
_TnTlsIgmpSnpgMRouterRobustCount_Type = Unsigned32
_TnTlsIgmpSnpgMRouterRobustCount_Object = MibTableColumn
tnTlsIgmpSnpgMRouterRobustCount = _TnTlsIgmpSnpgMRouterRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 12),
    _TnTlsIgmpSnpgMRouterRobustCount_Type()
)
tnTlsIgmpSnpgMRouterRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterRobustCount.setStatus("current")
_TnIgmpSnoopingTlsScalar1_Type = Unsigned32
_TnIgmpSnoopingTlsScalar1_Object = MibScalar
tnIgmpSnoopingTlsScalar1 = _TnIgmpSnoopingTlsScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 101),
    _TnIgmpSnoopingTlsScalar1_Type()
)
tnIgmpSnoopingTlsScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingTlsScalar1.setStatus("current")
_TnIgmpSnoopingTlsScalar2_Type = Unsigned32
_TnIgmpSnoopingTlsScalar2_Object = MibScalar
tnIgmpSnoopingTlsScalar2 = _TnIgmpSnoopingTlsScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 102),
    _TnIgmpSnoopingTlsScalar2_Type()
)
tnIgmpSnoopingTlsScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingTlsScalar2.setStatus("current")
_TnIgmpSnoopingSapObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingSapObjs = _TnIgmpSnoopingSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2)
)
_TnSapIgmpSnpgConfigTable_Object = MibTable
tnSapIgmpSnpgConfigTable = _TnSapIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgConfigTable.setStatus("current")
_TnSapIgmpSnpgConfigEntry_Object = MibTableRow
tnSapIgmpSnpgConfigEntry = _TnSapIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1)
)
tnSapIgmpSnpgConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgConfigEntry.setStatus("current")


class _TnSapIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnSapIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnSapIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnSapIgmpSnpgCfgImportPlcy_Object = MibTableColumn
tnSapIgmpSnpgCfgImportPlcy = _TnSapIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 1),
    _TnSapIgmpSnpgCfgImportPlcy_Type()
)
tnSapIgmpSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgImportPlcy.setStatus("current")


class _TnSapIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):
    """Custom type tnSapIgmpSnpgCfgFastLeave based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnSapIgmpSnpgCfgFastLeave_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnSapIgmpSnpgCfgFastLeave_Object = MibTableColumn
tnSapIgmpSnpgCfgFastLeave = _TnSapIgmpSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 2),
    _TnSapIgmpSnpgCfgFastLeave_Type()
)
tnSapIgmpSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgFastLeave.setStatus("current")


class _TnSapIgmpSnpgCfgMRouter_Type(TruthValue):
    """Custom type tnSapIgmpSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_TnSapIgmpSnpgCfgMRouter_Type.__name__ = "TruthValue"
_TnSapIgmpSnpgCfgMRouter_Object = MibTableColumn
tnSapIgmpSnpgCfgMRouter = _TnSapIgmpSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 3),
    _TnSapIgmpSnpgCfgMRouter_Type()
)
tnSapIgmpSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMRouter.setStatus("current")


class _TnSapIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):
    """Custom type tnSapIgmpSnpgCfgSendQueries based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnSapIgmpSnpgCfgSendQueries_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnSapIgmpSnpgCfgSendQueries_Object = MibTableColumn
tnSapIgmpSnpgCfgSendQueries = _TnSapIgmpSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 4),
    _TnSapIgmpSnpgCfgSendQueries_Type()
)
tnSapIgmpSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgSendQueries.setStatus("current")


class _TnSapIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_TnSapIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
tnSapIgmpSnpgCfgGenQueryIntvl = _TnSapIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 5),
    _TnSapIgmpSnpgCfgGenQueryIntvl_Type()
)
tnSapIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TnSapIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TnSapIgmpSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgQueryRespIntvl_Object = MibTableColumn
tnSapIgmpSnpgCfgQueryRespIntvl = _TnSapIgmpSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 6),
    _TnSapIgmpSnpgCfgQueryRespIntvl_Type()
)
tnSapIgmpSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgQueryRespIntvl.setUnits("seconds")


class _TnSapIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_TnSapIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgRobustCount_Object = MibTableColumn
tnSapIgmpSnpgCfgRobustCount = _TnSapIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 7),
    _TnSapIgmpSnpgCfgRobustCount_Type()
)
tnSapIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgRobustCount.setStatus("current")


class _TnSapIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TnSapIgmpSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgLastMembIntvl_Object = MibTableColumn
tnSapIgmpSnpgCfgLastMembIntvl = _TnSapIgmpSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 8),
    _TnSapIgmpSnpgCfgLastMembIntvl_Type()
)
tnSapIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _TnSapIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type tnSapIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_TnSapIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_TnSapIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
tnSapIgmpSnpgCfgMaxNbrGrps = _TnSapIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 9),
    _TnSapIgmpSnpgCfgMaxNbrGrps_Type()
)
tnSapIgmpSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMaxNbrGrps.setStatus("current")


class _TnSapIgmpSnpgCfgMvrFromVplsId_Type(TmnxServId):
    """Custom type tnSapIgmpSnpgCfgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_TnSapIgmpSnpgCfgMvrFromVplsId_Type.__name__ = "TmnxServId"
_TnSapIgmpSnpgCfgMvrFromVplsId_Object = MibTableColumn
tnSapIgmpSnpgCfgMvrFromVplsId = _TnSapIgmpSnpgCfgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 10),
    _TnSapIgmpSnpgCfgMvrFromVplsId_Type()
)
tnSapIgmpSnpgCfgMvrFromVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMvrFromVplsId.setStatus("current")


class _TnSapIgmpSnpgCfgMvrToSapPortId_Type(TmnxPortID):
    """Custom type tnSapIgmpSnpgCfgMvrToSapPortId based on TmnxPortID"""
    defaultValue = 0


_TnSapIgmpSnpgCfgMvrToSapPortId_Type.__name__ = "TmnxPortID"
_TnSapIgmpSnpgCfgMvrToSapPortId_Object = MibTableColumn
tnSapIgmpSnpgCfgMvrToSapPortId = _TnSapIgmpSnpgCfgMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 11),
    _TnSapIgmpSnpgCfgMvrToSapPortId_Type()
)
tnSapIgmpSnpgCfgMvrToSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMvrToSapPortId.setStatus("current")


class _TnSapIgmpSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):
    """Custom type tnSapIgmpSnpgCfgMvrToSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TnSapIgmpSnpgCfgMvrToSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TnSapIgmpSnpgCfgMvrToSapEncapVal_Object = MibTableColumn
tnSapIgmpSnpgCfgMvrToSapEncapVal = _TnSapIgmpSnpgCfgMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 12),
    _TnSapIgmpSnpgCfgMvrToSapEncapVal_Type()
)
tnSapIgmpSnpgCfgMvrToSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMvrToSapEncapVal.setStatus("current")


class _TnSapIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):
    """Custom type tnSapIgmpSnpgCfgVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_TnSapIgmpSnpgCfgVersion_Type.__name__ = "TmnxIgmpVersion"
_TnSapIgmpSnpgCfgVersion_Object = MibTableColumn
tnSapIgmpSnpgCfgVersion = _TnSapIgmpSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 13),
    _TnSapIgmpSnpgCfgVersion_Type()
)
tnSapIgmpSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgVersion.setStatus("current")


class _TnSapIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnSapIgmpSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnSapIgmpSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnSapIgmpSnpgCfgMcacPolicyName_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacPolicyName = _TnSapIgmpSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 14),
    _TnSapIgmpSnpgCfgMcacPolicyName_Type()
)
tnSapIgmpSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacPolicyName.setStatus("current")


class _TnSapIgmpSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type tnSapIgmpSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_TnSapIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_TnSapIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacUnconstBW = _TnSapIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 15),
    _TnSapIgmpSnpgCfgMcacUnconstBW_Type()
)
tnSapIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacUnconstBW.setUnits("kbps")


class _TnSapIgmpSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):
    """Custom type tnSapIgmpSnpgCfgMcacConstAdmSt based on TmnxAdminState"""
    defaultValue = 2


_TnSapIgmpSnpgCfgMcacConstAdmSt_Type.__name__ = "TmnxAdminState"
_TnSapIgmpSnpgCfgMcacConstAdmSt_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacConstAdmSt = _TnSapIgmpSnpgCfgMcacConstAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 16),
    _TnSapIgmpSnpgCfgMcacConstAdmSt_Type()
)
tnSapIgmpSnpgCfgMcacConstAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacConstAdmSt.setStatus("current")


class _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type tnSapIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacPrRsvMndBW = _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 17),
    _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
tnSapIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacinUseMandBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacinUseMandBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacinUseMandBw = _TnSapIgmpSnpgCfgMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 18),
    _TnSapIgmpSnpgCfgMcacinUseMandBw_Type()
)
tnSapIgmpSnpgCfgMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseMandBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacinUseOpnlBw = _TnSapIgmpSnpgCfgMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 19),
    _TnSapIgmpSnpgCfgMcacinUseOpnlBw_Type()
)
tnSapIgmpSnpgCfgMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseOpnlBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacAvailMandBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacAvailMandBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacAvailMandBw = _TnSapIgmpSnpgCfgMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 20),
    _TnSapIgmpSnpgCfgMcacAvailMandBw_Type()
)
tnSapIgmpSnpgCfgMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailMandBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacAvailOpnlBw = _TnSapIgmpSnpgCfgMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 21),
    _TnSapIgmpSnpgCfgMcacAvailOpnlBw_Type()
)
tnSapIgmpSnpgCfgMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailOpnlBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_TnSapIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacValInTrans = _TnSapIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 22),
    _TnSapIgmpSnpgCfgMcacValInTrans_Type()
)
tnSapIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacValInTrans.setStatus("current")
_TnSapIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_TnSapIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
tnSapIgmpSnpgCfgLastChangeTime = _TnSapIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 23),
    _TnSapIgmpSnpgCfgLastChangeTime_Type()
)
tnSapIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgLastChangeTime.setStatus("current")


class _TnSapIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgMaxNbrSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_TnSapIgmpSnpgCfgMaxNbrSrcs_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgMaxNbrSrcs_Object = MibTableColumn
tnSapIgmpSnpgCfgMaxNbrSrcs = _TnSapIgmpSnpgCfgMaxNbrSrcs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 24),
    _TnSapIgmpSnpgCfgMaxNbrSrcs_Type()
)
tnSapIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMaxNbrSrcs.setStatus("current")
_TnSapIgmpSnpgGroupTable_Object = MibTable
tnSapIgmpSnpgGroupTable = _TnSapIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGroupTable.setStatus("current")
_TnSapIgmpSnpgGroupEntry_Object = MibTableRow
tnSapIgmpSnpgGroupEntry = _TnSapIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1)
)
tnSapIgmpSnpgGroupEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGroupEntry.setStatus("current")
_TnSapIgmpSnpgGrpAddress_Type = IpAddress
_TnSapIgmpSnpgGrpAddress_Object = MibTableColumn
tnSapIgmpSnpgGrpAddress = _TnSapIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 1),
    _TnSapIgmpSnpgGrpAddress_Type()
)
tnSapIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpAddress.setStatus("current")
_TnSapIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_TnSapIgmpSnpgGrpType_Object = MibTableColumn
tnSapIgmpSnpgGrpType = _TnSapIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 2),
    _TnSapIgmpSnpgGrpType_Type()
)
tnSapIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpType.setStatus("current")
_TnSapIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_TnSapIgmpSnpgGrpFilterMode_Object = MibTableColumn
tnSapIgmpSnpgGrpFilterMode = _TnSapIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 3),
    _TnSapIgmpSnpgGrpFilterMode_Type()
)
tnSapIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpFilterMode.setStatus("current")
_TnSapIgmpSnpgGrpUpTime_Type = TimeTicks
_TnSapIgmpSnpgGrpUpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpUpTime = _TnSapIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 4),
    _TnSapIgmpSnpgGrpUpTime_Type()
)
tnSapIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpUpTime.setStatus("current")
_TnSapIgmpSnpgGrpExpiryTime_Type = Unsigned32
_TnSapIgmpSnpgGrpExpiryTime_Object = MibTableColumn
tnSapIgmpSnpgGrpExpiryTime = _TnSapIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 5),
    _TnSapIgmpSnpgGrpExpiryTime_Type()
)
tnSapIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpExpiryTime.setUnits("seconds")
_TnSapIgmpSnpgGrpCompatMode_Type = Unsigned32
_TnSapIgmpSnpgGrpCompatMode_Object = MibTableColumn
tnSapIgmpSnpgGrpCompatMode = _TnSapIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 6),
    _TnSapIgmpSnpgGrpCompatMode_Type()
)
tnSapIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpCompatMode.setStatus("current")
_TnSapIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_TnSapIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpV1HostExpTime = _TnSapIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 7),
    _TnSapIgmpSnpgGrpV1HostExpTime_Type()
)
tnSapIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_TnSapIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_TnSapIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpV2HostExpTime = _TnSapIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 8),
    _TnSapIgmpSnpgGrpV2HostExpTime_Type()
)
tnSapIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_TnSapIgmpSnpgGrpMvrFromVplsId_Type = TmnxServId
_TnSapIgmpSnpgGrpMvrFromVplsId_Object = MibTableColumn
tnSapIgmpSnpgGrpMvrFromVplsId = _TnSapIgmpSnpgGrpMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 9),
    _TnSapIgmpSnpgGrpMvrFromVplsId_Type()
)
tnSapIgmpSnpgGrpMvrFromVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpMvrFromVplsId.setStatus("current")
_TnSapIgmpSnpgGrpMvrToSapPortId_Type = TmnxPortID
_TnSapIgmpSnpgGrpMvrToSapPortId_Object = MibTableColumn
tnSapIgmpSnpgGrpMvrToSapPortId = _TnSapIgmpSnpgGrpMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 10),
    _TnSapIgmpSnpgGrpMvrToSapPortId_Type()
)
tnSapIgmpSnpgGrpMvrToSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpMvrToSapPortId.setStatus("current")
_TnSapIgmpSnpgGrpMvrToSapEncapVal_Type = TmnxEncapVal
_TnSapIgmpSnpgGrpMvrToSapEncapVal_Object = MibTableColumn
tnSapIgmpSnpgGrpMvrToSapEncapVal = _TnSapIgmpSnpgGrpMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 11),
    _TnSapIgmpSnpgGrpMvrToSapEncapVal_Type()
)
tnSapIgmpSnpgGrpMvrToSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpMvrToSapEncapVal.setStatus("current")
_TnSapIgmpSnpgGrpSrcTable_Object = MibTable
tnSapIgmpSnpgGrpSrcTable = _TnSapIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcTable.setStatus("current")
_TnSapIgmpSnpgGrpSrcEntry_Object = MibTableRow
tnSapIgmpSnpgGrpSrcEntry = _TnSapIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1)
)
tnSapIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgGrpAddress"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcEntry.setStatus("current")
_TnSapIgmpSnpgGrpSrcAddr_Type = IpAddress
_TnSapIgmpSnpgGrpSrcAddr_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcAddr = _TnSapIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 1),
    _TnSapIgmpSnpgGrpSrcAddr_Type()
)
tnSapIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcAddr.setStatus("current")
_TnSapIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_TnSapIgmpSnpgGrpSrcType_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcType = _TnSapIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 2),
    _TnSapIgmpSnpgGrpSrcType_Type()
)
tnSapIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcType.setStatus("current")
_TnSapIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_TnSapIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcUpTime = _TnSapIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 3),
    _TnSapIgmpSnpgGrpSrcUpTime_Type()
)
tnSapIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcUpTime.setStatus("current")
_TnSapIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_TnSapIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcExpiryTime = _TnSapIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 4),
    _TnSapIgmpSnpgGrpSrcExpiryTime_Type()
)
tnSapIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")
_TnSapIgmpSnpgStaticGrpSrcTable_Object = MibTable
tnSapIgmpSnpgStaticGrpSrcTable = _TnSapIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticGrpSrcTable.setStatus("current")
_TnSapIgmpSnpgStaticGrpSrcEntry_Object = MibTableRow
tnSapIgmpSnpgStaticGrpSrcEntry = _TnSapIgmpSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1)
)
tnSapIgmpSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgStaticGroupAddr"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticGrpSrcEntry.setStatus("current")
_TnSapIgmpSnpgStaticGroupAddr_Type = IpAddress
_TnSapIgmpSnpgStaticGroupAddr_Object = MibTableColumn
tnSapIgmpSnpgStaticGroupAddr = _TnSapIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 1),
    _TnSapIgmpSnpgStaticGroupAddr_Type()
)
tnSapIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticGroupAddr.setStatus("current")
_TnSapIgmpSnpgStaticSourceAddr_Type = IpAddress
_TnSapIgmpSnpgStaticSourceAddr_Object = MibTableColumn
tnSapIgmpSnpgStaticSourceAddr = _TnSapIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 2),
    _TnSapIgmpSnpgStaticSourceAddr_Type()
)
tnSapIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticSourceAddr.setStatus("current")
_TnSapIgmpSnpgStaticRowstatus_Type = RowStatus
_TnSapIgmpSnpgStaticRowstatus_Object = MibTableColumn
tnSapIgmpSnpgStaticRowstatus = _TnSapIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 3),
    _TnSapIgmpSnpgStaticRowstatus_Type()
)
tnSapIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticRowstatus.setStatus("current")
_TnSapIgmpSnpgStaticLastChangeTime_Type = TimeStamp
_TnSapIgmpSnpgStaticLastChangeTime_Object = MibTableColumn
tnSapIgmpSnpgStaticLastChangeTime = _TnSapIgmpSnpgStaticLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 4),
    _TnSapIgmpSnpgStaticLastChangeTime_Type()
)
tnSapIgmpSnpgStaticLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticLastChangeTime.setStatus("current")
_TnSapIgmpSnpgStatsTable_Object = MibTable
tnSapIgmpSnpgStatsTable = _TnSapIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStatsTable.setStatus("current")
_TnSapIgmpSnpgStatsEntry_Object = MibTableRow
tnSapIgmpSnpgStatsEntry = _TnSapIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1)
)
tnSapIgmpSnpgStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStatsEntry.setStatus("current")
_TnSapIgmpSnpgTxGenQueries_Type = Counter32
_TnSapIgmpSnpgTxGenQueries_Object = MibTableColumn
tnSapIgmpSnpgTxGenQueries = _TnSapIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 1),
    _TnSapIgmpSnpgTxGenQueries_Type()
)
tnSapIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxGenQueries.setStatus("current")
_TnSapIgmpSnpgTxGrpSpecQueries_Type = Counter32
_TnSapIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgTxGrpSpecQueries = _TnSapIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 2),
    _TnSapIgmpSnpgTxGrpSpecQueries_Type()
)
tnSapIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxGrpSpecQueries.setStatus("current")
_TnSapIgmpSnpgTxSrcSpecQueries_Type = Counter32
_TnSapIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgTxSrcSpecQueries = _TnSapIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 3),
    _TnSapIgmpSnpgTxSrcSpecQueries_Type()
)
tnSapIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxSrcSpecQueries.setStatus("current")
_TnSapIgmpSnpgTxV1Reports_Type = Counter32
_TnSapIgmpSnpgTxV1Reports_Object = MibTableColumn
tnSapIgmpSnpgTxV1Reports = _TnSapIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 4),
    _TnSapIgmpSnpgTxV1Reports_Type()
)
tnSapIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV1Reports.setStatus("current")
_TnSapIgmpSnpgTxV2Reports_Type = Counter32
_TnSapIgmpSnpgTxV2Reports_Object = MibTableColumn
tnSapIgmpSnpgTxV2Reports = _TnSapIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 5),
    _TnSapIgmpSnpgTxV2Reports_Type()
)
tnSapIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV2Reports.setStatus("current")
_TnSapIgmpSnpgTxV3Reports_Type = Counter32
_TnSapIgmpSnpgTxV3Reports_Object = MibTableColumn
tnSapIgmpSnpgTxV3Reports = _TnSapIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 6),
    _TnSapIgmpSnpgTxV3Reports_Type()
)
tnSapIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV3Reports.setStatus("current")
_TnSapIgmpSnpgTxV2Leaves_Type = Counter32
_TnSapIgmpSnpgTxV2Leaves_Object = MibTableColumn
tnSapIgmpSnpgTxV2Leaves = _TnSapIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 7),
    _TnSapIgmpSnpgTxV2Leaves_Type()
)
tnSapIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV2Leaves.setStatus("current")
_TnSapIgmpSnpgRxGenQueries_Type = Counter32
_TnSapIgmpSnpgRxGenQueries_Object = MibTableColumn
tnSapIgmpSnpgRxGenQueries = _TnSapIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 8),
    _TnSapIgmpSnpgRxGenQueries_Type()
)
tnSapIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxGenQueries.setStatus("current")
_TnSapIgmpSnpgRxGrpSpecQueries_Type = Counter32
_TnSapIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgRxGrpSpecQueries = _TnSapIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 9),
    _TnSapIgmpSnpgRxGrpSpecQueries_Type()
)
tnSapIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxGrpSpecQueries.setStatus("current")
_TnSapIgmpSnpgRxSrcSpecQueries_Type = Counter32
_TnSapIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgRxSrcSpecQueries = _TnSapIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 10),
    _TnSapIgmpSnpgRxSrcSpecQueries_Type()
)
tnSapIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxSrcSpecQueries.setStatus("current")
_TnSapIgmpSnpgRxV1Reports_Type = Counter32
_TnSapIgmpSnpgRxV1Reports_Object = MibTableColumn
tnSapIgmpSnpgRxV1Reports = _TnSapIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 11),
    _TnSapIgmpSnpgRxV1Reports_Type()
)
tnSapIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV1Reports.setStatus("current")
_TnSapIgmpSnpgRxV2Reports_Type = Counter32
_TnSapIgmpSnpgRxV2Reports_Object = MibTableColumn
tnSapIgmpSnpgRxV2Reports = _TnSapIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 12),
    _TnSapIgmpSnpgRxV2Reports_Type()
)
tnSapIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV2Reports.setStatus("current")
_TnSapIgmpSnpgRxV3Reports_Type = Counter32
_TnSapIgmpSnpgRxV3Reports_Object = MibTableColumn
tnSapIgmpSnpgRxV3Reports = _TnSapIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 13),
    _TnSapIgmpSnpgRxV3Reports_Type()
)
tnSapIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV3Reports.setStatus("current")
_TnSapIgmpSnpgRxV2Leaves_Type = Counter32
_TnSapIgmpSnpgRxV2Leaves_Object = MibTableColumn
tnSapIgmpSnpgRxV2Leaves = _TnSapIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 14),
    _TnSapIgmpSnpgRxV2Leaves_Type()
)
tnSapIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV2Leaves.setStatus("current")
_TnSapIgmpSnpgRxUnknownType_Type = Counter32
_TnSapIgmpSnpgRxUnknownType_Object = MibTableColumn
tnSapIgmpSnpgRxUnknownType = _TnSapIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 15),
    _TnSapIgmpSnpgRxUnknownType_Type()
)
tnSapIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxUnknownType.setStatus("current")
_TnSapIgmpSnpgFwdGenQueries_Type = Counter32
_TnSapIgmpSnpgFwdGenQueries_Object = MibTableColumn
tnSapIgmpSnpgFwdGenQueries = _TnSapIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 16),
    _TnSapIgmpSnpgFwdGenQueries_Type()
)
tnSapIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdGenQueries.setStatus("current")
_TnSapIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_TnSapIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgFwdGrpSpecQueries = _TnSapIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 17),
    _TnSapIgmpSnpgFwdGrpSpecQueries_Type()
)
tnSapIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_TnSapIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_TnSapIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgFwdSrcSpecQueries = _TnSapIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 18),
    _TnSapIgmpSnpgFwdSrcSpecQueries_Type()
)
tnSapIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_TnSapIgmpSnpgFwdV1Reports_Type = Counter32
_TnSapIgmpSnpgFwdV1Reports_Object = MibTableColumn
tnSapIgmpSnpgFwdV1Reports = _TnSapIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 19),
    _TnSapIgmpSnpgFwdV1Reports_Type()
)
tnSapIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV1Reports.setStatus("current")
_TnSapIgmpSnpgFwdV2Reports_Type = Counter32
_TnSapIgmpSnpgFwdV2Reports_Object = MibTableColumn
tnSapIgmpSnpgFwdV2Reports = _TnSapIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 20),
    _TnSapIgmpSnpgFwdV2Reports_Type()
)
tnSapIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV2Reports.setStatus("current")
_TnSapIgmpSnpgFwdV3Reports_Type = Counter32
_TnSapIgmpSnpgFwdV3Reports_Object = MibTableColumn
tnSapIgmpSnpgFwdV3Reports = _TnSapIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 21),
    _TnSapIgmpSnpgFwdV3Reports_Type()
)
tnSapIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV3Reports.setStatus("current")
_TnSapIgmpSnpgFwdV2Leaves_Type = Counter32
_TnSapIgmpSnpgFwdV2Leaves_Object = MibTableColumn
tnSapIgmpSnpgFwdV2Leaves = _TnSapIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 22),
    _TnSapIgmpSnpgFwdV2Leaves_Type()
)
tnSapIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV2Leaves.setStatus("current")
_TnSapIgmpSnpgFwdUnknownType_Type = Counter32
_TnSapIgmpSnpgFwdUnknownType_Object = MibTableColumn
tnSapIgmpSnpgFwdUnknownType = _TnSapIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 23),
    _TnSapIgmpSnpgFwdUnknownType_Type()
)
tnSapIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdUnknownType.setStatus("current")
_TnSapIgmpSnpgRxBadLenPkts_Type = Counter32
_TnSapIgmpSnpgRxBadLenPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadLenPkts = _TnSapIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 24),
    _TnSapIgmpSnpgRxBadLenPkts_Type()
)
tnSapIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadLenPkts.setStatus("current")
_TnSapIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_TnSapIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadIpChksmPkts = _TnSapIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 25),
    _TnSapIgmpSnpgRxBadIpChksmPkts_Type()
)
tnSapIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_TnSapIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_TnSapIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadIgmpChksmPkts = _TnSapIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 26),
    _TnSapIgmpSnpgRxBadIgmpChksmPkts_Type()
)
tnSapIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_TnSapIgmpSnpgRxBadEncodedPkts_Type = Counter32
_TnSapIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadEncodedPkts = _TnSapIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 27),
    _TnSapIgmpSnpgRxBadEncodedPkts_Type()
)
tnSapIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadEncodedPkts.setStatus("current")
_TnSapIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_TnSapIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
tnSapIgmpSnpgRxNoRtrAlertPkts = _TnSapIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 28),
    _TnSapIgmpSnpgRxNoRtrAlertPkts_Type()
)
tnSapIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_TnSapIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_TnSapIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
tnSapIgmpSnpgRxZeroSrcAdrPkts = _TnSapIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 29),
    _TnSapIgmpSnpgRxZeroSrcAdrPkts_Type()
)
tnSapIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_TnSapIgmpSnpgSendQueryCfgDrops_Type = Counter32
_TnSapIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
tnSapIgmpSnpgSendQueryCfgDrops = _TnSapIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 30),
    _TnSapIgmpSnpgSendQueryCfgDrops_Type()
)
tnSapIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgSendQueryCfgDrops.setStatus("current")
_TnSapIgmpSnpgImportPolicyDrops_Type = Counter32
_TnSapIgmpSnpgImportPolicyDrops_Object = MibTableColumn
tnSapIgmpSnpgImportPolicyDrops = _TnSapIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 31),
    _TnSapIgmpSnpgImportPolicyDrops_Type()
)
tnSapIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgImportPolicyDrops.setStatus("current")
_TnSapIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_TnSapIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
tnSapIgmpSnpgMaxNumGroupsDrops = _TnSapIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 32),
    _TnSapIgmpSnpgMaxNumGroupsDrops_Type()
)
tnSapIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_TnSapIgmpSnpgMvrFromVplsCfgDrops_Type = Counter32
_TnSapIgmpSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
tnSapIgmpSnpgMvrFromVplsCfgDrops = _TnSapIgmpSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 33),
    _TnSapIgmpSnpgMvrFromVplsCfgDrops_Type()
)
tnSapIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMvrFromVplsCfgDrops.setStatus("current")
_TnSapIgmpSnpgMvrToSapCfgDrops_Type = Counter32
_TnSapIgmpSnpgMvrToSapCfgDrops_Object = MibTableColumn
tnSapIgmpSnpgMvrToSapCfgDrops = _TnSapIgmpSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 34),
    _TnSapIgmpSnpgMvrToSapCfgDrops_Type()
)
tnSapIgmpSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMvrToSapCfgDrops.setStatus("current")
_TnSapIgmpSnpgRxWrongVersionPkts_Type = Counter32
_TnSapIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
tnSapIgmpSnpgRxWrongVersionPkts = _TnSapIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 35),
    _TnSapIgmpSnpgRxWrongVersionPkts_Type()
)
tnSapIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxWrongVersionPkts.setStatus("current")
_TnSapIgmpSnpgMcacPolicyDrops_Type = Counter32
_TnSapIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
tnSapIgmpSnpgMcacPolicyDrops = _TnSapIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 36),
    _TnSapIgmpSnpgMcacPolicyDrops_Type()
)
tnSapIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMcacPolicyDrops.setStatus("current")
_TnSapIgmpSnpgMcsFailures_Type = Counter32
_TnSapIgmpSnpgMcsFailures_Object = MibTableColumn
tnSapIgmpSnpgMcsFailures = _TnSapIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 37),
    _TnSapIgmpSnpgMcsFailures_Type()
)
tnSapIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMcsFailures.setStatus("current")
_TnSapIgmpSnpgRxLocalScopePkts_Type = Counter32
_TnSapIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
tnSapIgmpSnpgRxLocalScopePkts = _TnSapIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 38),
    _TnSapIgmpSnpgRxLocalScopePkts_Type()
)
tnSapIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxLocalScopePkts.setStatus("current")
_TnSapIgmpSnpgRxRsvdScopePkts_Type = Counter32
_TnSapIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
tnSapIgmpSnpgRxRsvdScopePkts = _TnSapIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 39),
    _TnSapIgmpSnpgRxRsvdScopePkts_Type()
)
tnSapIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxRsvdScopePkts.setStatus("current")
_TnSapIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_TnSapIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
tnSapIgmpSnpgMaxNumSourcesDrops = _TnSapIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 40),
    _TnSapIgmpSnpgMaxNumSourcesDrops_Type()
)
tnSapIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_TnIgmpSnoopingSapScalar1_Type = Unsigned32
_TnIgmpSnoopingSapScalar1_Object = MibScalar
tnIgmpSnoopingSapScalar1 = _TnIgmpSnoopingSapScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 101),
    _TnIgmpSnoopingSapScalar1_Type()
)
tnIgmpSnoopingSapScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingSapScalar1.setStatus("current")
_TnIgmpSnoopingSapScalar2_Type = Unsigned32
_TnIgmpSnoopingSapScalar2_Object = MibScalar
tnIgmpSnoopingSapScalar2 = _TnIgmpSnoopingSapScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 102),
    _TnIgmpSnoopingSapScalar2_Type()
)
tnIgmpSnoopingSapScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingSapScalar2.setStatus("current")
_TnIgmpSnoopingNotifyPrefix_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingNotifyPrefix = _TnIgmpSnoopingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 24)
)
_TnIgmpSnoopingSapPrefix_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingSapPrefix = _TnIgmpSnoopingSapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 24, 1)
)
_TnIgmpSnpgSapNotifications_ObjectIdentity = ObjectIdentity
tnIgmpSnpgSapNotifications = _TnIgmpSnpgSapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 24, 1, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-IGMP-SNOOPING-MIB",
    **{"AlxIgmpSnpgAdminState": AlxIgmpSnpgAdminState,
       "AlxIgmpSnpgLocation": AlxIgmpSnpgLocation,
       "tnIgmpSnoopingMIBModule": tnIgmpSnoopingMIBModule,
       "tnIgmpSnoopingObjs": tnIgmpSnoopingObjs,
       "tnIgmpSnoopingTlsObjs": tnIgmpSnoopingTlsObjs,
       "tnTlsIgmpSnpgConfigTable": tnTlsIgmpSnpgConfigTable,
       "tnTlsIgmpSnpgConfigEntry": tnTlsIgmpSnpgConfigEntry,
       "tnTlsIgmpSnpgCfgAdminState": tnTlsIgmpSnpgCfgAdminState,
       "tnTlsIgmpSnpgCfgGenQueryIntvl": tnTlsIgmpSnpgCfgGenQueryIntvl,
       "tnTlsIgmpSnpgCfgRobustCount": tnTlsIgmpSnpgCfgRobustCount,
       "tnTlsIgmpSnpgCfgReportSrcAddress": tnTlsIgmpSnpgCfgReportSrcAddress,
       "tnTlsIgmpSnpgCfgMvrAdminState": tnTlsIgmpSnpgCfgMvrAdminState,
       "tnTlsIgmpSnpgCfgMvrDescription": tnTlsIgmpSnpgCfgMvrDescription,
       "tnTlsIgmpSnpgCfgMvrPolicy": tnTlsIgmpSnpgCfgMvrPolicy,
       "tnTlsIgmpSnpgCfgQuerySrcAddress": tnTlsIgmpSnpgCfgQuerySrcAddress,
       "tnTlsIgmpSnpgCfgQuerySrcAddrType": tnTlsIgmpSnpgCfgQuerySrcAddrType,
       "tnTlsIgmpSnpgCfgLastChangeTime": tnTlsIgmpSnpgCfgLastChangeTime,
       "tnTlsIgmpSnpgQuerierTable": tnTlsIgmpSnpgQuerierTable,
       "tnTlsIgmpSnpgQuerierEntry": tnTlsIgmpSnpgQuerierEntry,
       "tnTlsIgmpSnpgQuerierVersion": tnTlsIgmpSnpgQuerierVersion,
       "tnTlsIgmpSnpgQuerierAddress": tnTlsIgmpSnpgQuerierAddress,
       "tnTlsIgmpSnpgQuerierLocale": tnTlsIgmpSnpgQuerierLocale,
       "tnTlsIgmpSnpgQuerierPortId": tnTlsIgmpSnpgQuerierPortId,
       "tnTlsIgmpSnpgQuerierEncapValue": tnTlsIgmpSnpgQuerierEncapValue,
       "tnTlsIgmpSnpgQuerierSdpId": tnTlsIgmpSnpgQuerierSdpId,
       "tnTlsIgmpSnpgQuerierVcId": tnTlsIgmpSnpgQuerierVcId,
       "tnTlsIgmpSnpgQuerierUpTime": tnTlsIgmpSnpgQuerierUpTime,
       "tnTlsIgmpSnpgQuerierExpiryTime": tnTlsIgmpSnpgQuerierExpiryTime,
       "tnTlsIgmpSnpgQuerierGenQueryIntvl": tnTlsIgmpSnpgQuerierGenQueryIntvl,
       "tnTlsIgmpSnpgQuerierGenRespIntvl": tnTlsIgmpSnpgQuerierGenRespIntvl,
       "tnTlsIgmpSnpgQuerierRobustCount": tnTlsIgmpSnpgQuerierRobustCount,
       "tnTlsIgmpSnpgProxyGroupTable": tnTlsIgmpSnpgProxyGroupTable,
       "tnTlsIgmpSnpgProxyGroupEntry": tnTlsIgmpSnpgProxyGroupEntry,
       "tnTlsIgmpSnpgProxyGroupAddress": tnTlsIgmpSnpgProxyGroupAddress,
       "tnTlsIgmpSnpgProxyGroupFilterMode": tnTlsIgmpSnpgProxyGroupFilterMode,
       "tnTlsIgmpSnpgProxyGroupUpTime": tnTlsIgmpSnpgProxyGroupUpTime,
       "tnTlsIgmpSnpgProxyGrpSrcTable": tnTlsIgmpSnpgProxyGrpSrcTable,
       "tnTlsIgmpSnpgProxyGrpSrcEntry": tnTlsIgmpSnpgProxyGrpSrcEntry,
       "tnTlsIgmpSnpgProxyGrpSrcAddr": tnTlsIgmpSnpgProxyGrpSrcAddr,
       "tnTlsIgmpSnpgProxyGrpSrcUpTime": tnTlsIgmpSnpgProxyGrpSrcUpTime,
       "tnTlsIgmpSnpgMRouterTable": tnTlsIgmpSnpgMRouterTable,
       "tnTlsIgmpSnpgMRouterEntry": tnTlsIgmpSnpgMRouterEntry,
       "tnTlsIgmpSnpgMRouterAddress": tnTlsIgmpSnpgMRouterAddress,
       "tnTlsIgmpSnpgMRouterLocale": tnTlsIgmpSnpgMRouterLocale,
       "tnTlsIgmpSnpgMRouterPortId": tnTlsIgmpSnpgMRouterPortId,
       "tnTlsIgmpSnpgMRouterEncapValue": tnTlsIgmpSnpgMRouterEncapValue,
       "tnTlsIgmpSnpgMRouterSdpId": tnTlsIgmpSnpgMRouterSdpId,
       "tnTlsIgmpSnpgMRouterVcId": tnTlsIgmpSnpgMRouterVcId,
       "tnTlsIgmpSnpgMRouterVersion": tnTlsIgmpSnpgMRouterVersion,
       "tnTlsIgmpSnpgMRouterExpiryTime": tnTlsIgmpSnpgMRouterExpiryTime,
       "tnTlsIgmpSnpgMRouterUpTime": tnTlsIgmpSnpgMRouterUpTime,
       "tnTlsIgmpSnpgMRouterGenQueryIntvl": tnTlsIgmpSnpgMRouterGenQueryIntvl,
       "tnTlsIgmpSnpgMRouterGenRespIntvl": tnTlsIgmpSnpgMRouterGenRespIntvl,
       "tnTlsIgmpSnpgMRouterRobustCount": tnTlsIgmpSnpgMRouterRobustCount,
       "tnIgmpSnoopingTlsScalar1": tnIgmpSnoopingTlsScalar1,
       "tnIgmpSnoopingTlsScalar2": tnIgmpSnoopingTlsScalar2,
       "tnIgmpSnoopingSapObjs": tnIgmpSnoopingSapObjs,
       "tnSapIgmpSnpgConfigTable": tnSapIgmpSnpgConfigTable,
       "tnSapIgmpSnpgConfigEntry": tnSapIgmpSnpgConfigEntry,
       "tnSapIgmpSnpgCfgImportPlcy": tnSapIgmpSnpgCfgImportPlcy,
       "tnSapIgmpSnpgCfgFastLeave": tnSapIgmpSnpgCfgFastLeave,
       "tnSapIgmpSnpgCfgMRouter": tnSapIgmpSnpgCfgMRouter,
       "tnSapIgmpSnpgCfgSendQueries": tnSapIgmpSnpgCfgSendQueries,
       "tnSapIgmpSnpgCfgGenQueryIntvl": tnSapIgmpSnpgCfgGenQueryIntvl,
       "tnSapIgmpSnpgCfgQueryRespIntvl": tnSapIgmpSnpgCfgQueryRespIntvl,
       "tnSapIgmpSnpgCfgRobustCount": tnSapIgmpSnpgCfgRobustCount,
       "tnSapIgmpSnpgCfgLastMembIntvl": tnSapIgmpSnpgCfgLastMembIntvl,
       "tnSapIgmpSnpgCfgMaxNbrGrps": tnSapIgmpSnpgCfgMaxNbrGrps,
       "tnSapIgmpSnpgCfgMvrFromVplsId": tnSapIgmpSnpgCfgMvrFromVplsId,
       "tnSapIgmpSnpgCfgMvrToSapPortId": tnSapIgmpSnpgCfgMvrToSapPortId,
       "tnSapIgmpSnpgCfgMvrToSapEncapVal": tnSapIgmpSnpgCfgMvrToSapEncapVal,
       "tnSapIgmpSnpgCfgVersion": tnSapIgmpSnpgCfgVersion,
       "tnSapIgmpSnpgCfgMcacPolicyName": tnSapIgmpSnpgCfgMcacPolicyName,
       "tnSapIgmpSnpgCfgMcacUnconstBW": tnSapIgmpSnpgCfgMcacUnconstBW,
       "tnSapIgmpSnpgCfgMcacConstAdmSt": tnSapIgmpSnpgCfgMcacConstAdmSt,
       "tnSapIgmpSnpgCfgMcacPrRsvMndBW": tnSapIgmpSnpgCfgMcacPrRsvMndBW,
       "tnSapIgmpSnpgCfgMcacinUseMandBw": tnSapIgmpSnpgCfgMcacinUseMandBw,
       "tnSapIgmpSnpgCfgMcacinUseOpnlBw": tnSapIgmpSnpgCfgMcacinUseOpnlBw,
       "tnSapIgmpSnpgCfgMcacAvailMandBw": tnSapIgmpSnpgCfgMcacAvailMandBw,
       "tnSapIgmpSnpgCfgMcacAvailOpnlBw": tnSapIgmpSnpgCfgMcacAvailOpnlBw,
       "tnSapIgmpSnpgCfgMcacValInTrans": tnSapIgmpSnpgCfgMcacValInTrans,
       "tnSapIgmpSnpgCfgLastChangeTime": tnSapIgmpSnpgCfgLastChangeTime,
       "tnSapIgmpSnpgCfgMaxNbrSrcs": tnSapIgmpSnpgCfgMaxNbrSrcs,
       "tnSapIgmpSnpgGroupTable": tnSapIgmpSnpgGroupTable,
       "tnSapIgmpSnpgGroupEntry": tnSapIgmpSnpgGroupEntry,
       "tnSapIgmpSnpgGrpAddress": tnSapIgmpSnpgGrpAddress,
       "tnSapIgmpSnpgGrpType": tnSapIgmpSnpgGrpType,
       "tnSapIgmpSnpgGrpFilterMode": tnSapIgmpSnpgGrpFilterMode,
       "tnSapIgmpSnpgGrpUpTime": tnSapIgmpSnpgGrpUpTime,
       "tnSapIgmpSnpgGrpExpiryTime": tnSapIgmpSnpgGrpExpiryTime,
       "tnSapIgmpSnpgGrpCompatMode": tnSapIgmpSnpgGrpCompatMode,
       "tnSapIgmpSnpgGrpV1HostExpTime": tnSapIgmpSnpgGrpV1HostExpTime,
       "tnSapIgmpSnpgGrpV2HostExpTime": tnSapIgmpSnpgGrpV2HostExpTime,
       "tnSapIgmpSnpgGrpMvrFromVplsId": tnSapIgmpSnpgGrpMvrFromVplsId,
       "tnSapIgmpSnpgGrpMvrToSapPortId": tnSapIgmpSnpgGrpMvrToSapPortId,
       "tnSapIgmpSnpgGrpMvrToSapEncapVal": tnSapIgmpSnpgGrpMvrToSapEncapVal,
       "tnSapIgmpSnpgGrpSrcTable": tnSapIgmpSnpgGrpSrcTable,
       "tnSapIgmpSnpgGrpSrcEntry": tnSapIgmpSnpgGrpSrcEntry,
       "tnSapIgmpSnpgGrpSrcAddr": tnSapIgmpSnpgGrpSrcAddr,
       "tnSapIgmpSnpgGrpSrcType": tnSapIgmpSnpgGrpSrcType,
       "tnSapIgmpSnpgGrpSrcUpTime": tnSapIgmpSnpgGrpSrcUpTime,
       "tnSapIgmpSnpgGrpSrcExpiryTime": tnSapIgmpSnpgGrpSrcExpiryTime,
       "tnSapIgmpSnpgStaticGrpSrcTable": tnSapIgmpSnpgStaticGrpSrcTable,
       "tnSapIgmpSnpgStaticGrpSrcEntry": tnSapIgmpSnpgStaticGrpSrcEntry,
       "tnSapIgmpSnpgStaticGroupAddr": tnSapIgmpSnpgStaticGroupAddr,
       "tnSapIgmpSnpgStaticSourceAddr": tnSapIgmpSnpgStaticSourceAddr,
       "tnSapIgmpSnpgStaticRowstatus": tnSapIgmpSnpgStaticRowstatus,
       "tnSapIgmpSnpgStaticLastChangeTime": tnSapIgmpSnpgStaticLastChangeTime,
       "tnSapIgmpSnpgStatsTable": tnSapIgmpSnpgStatsTable,
       "tnSapIgmpSnpgStatsEntry": tnSapIgmpSnpgStatsEntry,
       "tnSapIgmpSnpgTxGenQueries": tnSapIgmpSnpgTxGenQueries,
       "tnSapIgmpSnpgTxGrpSpecQueries": tnSapIgmpSnpgTxGrpSpecQueries,
       "tnSapIgmpSnpgTxSrcSpecQueries": tnSapIgmpSnpgTxSrcSpecQueries,
       "tnSapIgmpSnpgTxV1Reports": tnSapIgmpSnpgTxV1Reports,
       "tnSapIgmpSnpgTxV2Reports": tnSapIgmpSnpgTxV2Reports,
       "tnSapIgmpSnpgTxV3Reports": tnSapIgmpSnpgTxV3Reports,
       "tnSapIgmpSnpgTxV2Leaves": tnSapIgmpSnpgTxV2Leaves,
       "tnSapIgmpSnpgRxGenQueries": tnSapIgmpSnpgRxGenQueries,
       "tnSapIgmpSnpgRxGrpSpecQueries": tnSapIgmpSnpgRxGrpSpecQueries,
       "tnSapIgmpSnpgRxSrcSpecQueries": tnSapIgmpSnpgRxSrcSpecQueries,
       "tnSapIgmpSnpgRxV1Reports": tnSapIgmpSnpgRxV1Reports,
       "tnSapIgmpSnpgRxV2Reports": tnSapIgmpSnpgRxV2Reports,
       "tnSapIgmpSnpgRxV3Reports": tnSapIgmpSnpgRxV3Reports,
       "tnSapIgmpSnpgRxV2Leaves": tnSapIgmpSnpgRxV2Leaves,
       "tnSapIgmpSnpgRxUnknownType": tnSapIgmpSnpgRxUnknownType,
       "tnSapIgmpSnpgFwdGenQueries": tnSapIgmpSnpgFwdGenQueries,
       "tnSapIgmpSnpgFwdGrpSpecQueries": tnSapIgmpSnpgFwdGrpSpecQueries,
       "tnSapIgmpSnpgFwdSrcSpecQueries": tnSapIgmpSnpgFwdSrcSpecQueries,
       "tnSapIgmpSnpgFwdV1Reports": tnSapIgmpSnpgFwdV1Reports,
       "tnSapIgmpSnpgFwdV2Reports": tnSapIgmpSnpgFwdV2Reports,
       "tnSapIgmpSnpgFwdV3Reports": tnSapIgmpSnpgFwdV3Reports,
       "tnSapIgmpSnpgFwdV2Leaves": tnSapIgmpSnpgFwdV2Leaves,
       "tnSapIgmpSnpgFwdUnknownType": tnSapIgmpSnpgFwdUnknownType,
       "tnSapIgmpSnpgRxBadLenPkts": tnSapIgmpSnpgRxBadLenPkts,
       "tnSapIgmpSnpgRxBadIpChksmPkts": tnSapIgmpSnpgRxBadIpChksmPkts,
       "tnSapIgmpSnpgRxBadIgmpChksmPkts": tnSapIgmpSnpgRxBadIgmpChksmPkts,
       "tnSapIgmpSnpgRxBadEncodedPkts": tnSapIgmpSnpgRxBadEncodedPkts,
       "tnSapIgmpSnpgRxNoRtrAlertPkts": tnSapIgmpSnpgRxNoRtrAlertPkts,
       "tnSapIgmpSnpgRxZeroSrcAdrPkts": tnSapIgmpSnpgRxZeroSrcAdrPkts,
       "tnSapIgmpSnpgSendQueryCfgDrops": tnSapIgmpSnpgSendQueryCfgDrops,
       "tnSapIgmpSnpgImportPolicyDrops": tnSapIgmpSnpgImportPolicyDrops,
       "tnSapIgmpSnpgMaxNumGroupsDrops": tnSapIgmpSnpgMaxNumGroupsDrops,
       "tnSapIgmpSnpgMvrFromVplsCfgDrops": tnSapIgmpSnpgMvrFromVplsCfgDrops,
       "tnSapIgmpSnpgMvrToSapCfgDrops": tnSapIgmpSnpgMvrToSapCfgDrops,
       "tnSapIgmpSnpgRxWrongVersionPkts": tnSapIgmpSnpgRxWrongVersionPkts,
       "tnSapIgmpSnpgMcacPolicyDrops": tnSapIgmpSnpgMcacPolicyDrops,
       "tnSapIgmpSnpgMcsFailures": tnSapIgmpSnpgMcsFailures,
       "tnSapIgmpSnpgRxLocalScopePkts": tnSapIgmpSnpgRxLocalScopePkts,
       "tnSapIgmpSnpgRxRsvdScopePkts": tnSapIgmpSnpgRxRsvdScopePkts,
       "tnSapIgmpSnpgMaxNumSourcesDrops": tnSapIgmpSnpgMaxNumSourcesDrops,
       "tnIgmpSnoopingSapScalar1": tnIgmpSnoopingSapScalar1,
       "tnIgmpSnoopingSapScalar2": tnIgmpSnoopingSapScalar2,
       "tnIgmpSnoopingNotifyPrefix": tnIgmpSnoopingNotifyPrefix,
       "tnIgmpSnoopingSapPrefix": tnIgmpSnoopingSapPrefix,
       "tnIgmpSnpgSapNotifications": tnIgmpSnpgSapNotifications}
)
