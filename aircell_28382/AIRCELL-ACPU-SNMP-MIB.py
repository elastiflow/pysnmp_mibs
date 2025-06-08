# SNMP MIB module (AIRCELL-ACPU-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aircell_28382/AIRCELL-ACPU-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:18:40 2025
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aircellLLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28382)
)
if mibBuilder.loadTexts:
    aircellLLC.setRevisions(
        ("2012-06-18 22:14",
         "2012-05-18 22:14",
         "2012-05-03 17:30",
         "2012-01-05 06:30",
         "2011-11-02 06:30",
         "2011-01-03 23:07",
         "2010-04-06 23:00",
         "2007-08-08 22:27")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AircellABS_ObjectIdentity = ObjectIdentity
aircellABS = _AircellABS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1)
)
_AircellABSConfig_ObjectIdentity = ObjectIdentity
aircellABSConfig = _AircellABSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1)
)
_AbsControlConfig_ObjectIdentity = ObjectIdentity
absControlConfig = _AbsControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1)
)
_WiredHandsetTable_Object = MibTable
wiredHandsetTable = _WiredHandsetTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wiredHandsetTable.setStatus("current")
_WiredHandsetEntry_Object = MibTableRow
wiredHandsetEntry = _WiredHandsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 1, 1)
)
wiredHandsetEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "wiredHandsetIndex"),
)
if mibBuilder.loadTexts:
    wiredHandsetEntry.setStatus("current")


class _WiredHandsetIndex_Type(Integer32):
    """Custom type wiredHandsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WiredHandsetIndex_Type.__name__ = "Integer32"
_WiredHandsetIndex_Object = MibTableColumn
wiredHandsetIndex = _WiredHandsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 1, 1, 1),
    _WiredHandsetIndex_Type()
)
wiredHandsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wiredHandsetIndex.setStatus("current")


class _WiredHandsetAdminStatus_Type(Integer32):
    """Custom type wiredHandsetAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_WiredHandsetAdminStatus_Type.__name__ = "Integer32"
_WiredHandsetAdminStatus_Object = MibTableColumn
wiredHandsetAdminStatus = _WiredHandsetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 1, 1, 2),
    _WiredHandsetAdminStatus_Type()
)
wiredHandsetAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wiredHandsetAdminStatus.setStatus("current")


class _WiredHandsetOperStatus_Type(Integer32):
    """Custom type wiredHandsetOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_WiredHandsetOperStatus_Type.__name__ = "Integer32"
_WiredHandsetOperStatus_Object = MibTableColumn
wiredHandsetOperStatus = _WiredHandsetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 1, 1, 3),
    _WiredHandsetOperStatus_Type()
)
wiredHandsetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wiredHandsetOperStatus.setStatus("current")
_WiredHandsetRowStatus_Type = RowStatus
_WiredHandsetRowStatus_Object = MibTableColumn
wiredHandsetRowStatus = _WiredHandsetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 1, 1, 4),
    _WiredHandsetRowStatus_Type()
)
wiredHandsetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wiredHandsetRowStatus.setStatus("current")


class _AbsSystemReset_Type(Integer32):
    """Custom type absSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_AbsSystemReset_Type.__name__ = "Integer32"
_AbsSystemReset_Object = MibScalar
absSystemReset = _AbsSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 2),
    _AbsSystemReset_Type()
)
absSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absSystemReset.setStatus("current")


class _AbsSystemMode_Type(Integer32):
    """Custom type absSystemMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autonomous", 0),
          ("operational", 1),
          ("maintenance", 2))
    )


_AbsSystemMode_Type.__name__ = "Integer32"
_AbsSystemMode_Object = MibScalar
absSystemMode = _AbsSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 3),
    _AbsSystemMode_Type()
)
absSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absSystemMode.setStatus("current")


class _AbsSoftwareApplyTime_Type(Integer32):
    """Custom type absSoftwareApplyTime based on Integer32"""
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
        *(("reset", 1),
          ("gate", 2),
          ("hold", 3))
    )


_AbsSoftwareApplyTime_Type.__name__ = "Integer32"
_AbsSoftwareApplyTime_Object = MibScalar
absSoftwareApplyTime = _AbsSoftwareApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 4),
    _AbsSoftwareApplyTime_Type()
)
absSoftwareApplyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absSoftwareApplyTime.setStatus("obsolete")


class _AbsSoftwareBackoutTime_Type(Integer32):
    """Custom type absSoftwareBackoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("gate", 2),
          ("null", 3))
    )


_AbsSoftwareBackoutTime_Type.__name__ = "Integer32"
_AbsSoftwareBackoutTime_Object = MibScalar
absSoftwareBackoutTime = _AbsSoftwareBackoutTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 5),
    _AbsSoftwareBackoutTime_Type()
)
absSoftwareBackoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absSoftwareBackoutTime.setStatus("obsolete")


class _AbsDisablePortal_Type(Integer32):
    """Custom type absDisablePortal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("passenger", 2),
          ("none", 3))
    )


_AbsDisablePortal_Type.__name__ = "Integer32"
_AbsDisablePortal_Object = MibScalar
absDisablePortal = _AbsDisablePortal_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 6),
    _AbsDisablePortal_Type()
)
absDisablePortal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absDisablePortal.setStatus("current")


class _AbsSystemBlockATGAccess_Type(Integer32):
    """Custom type absSystemBlockATGAccess based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("passenger", 2),
          ("none", 3))
    )


_AbsSystemBlockATGAccess_Type.__name__ = "Integer32"
_AbsSystemBlockATGAccess_Object = MibScalar
absSystemBlockATGAccess = _AbsSystemBlockATGAccess_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 7),
    _AbsSystemBlockATGAccess_Type()
)
absSystemBlockATGAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absSystemBlockATGAccess.setStatus("current")


class _AbsAcpuLoggingLevels_Type(Integer32):
    """Custom type absAcpuLoggingLevels based on Integer32"""
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
        *(("all", 1),
          ("off", 2),
          ("debug", 3),
          ("error", 4),
          ("fatal", 5),
          ("info", 6),
          ("trace", 7),
          ("warn", 8))
    )


_AbsAcpuLoggingLevels_Type.__name__ = "Integer32"
_AbsAcpuLoggingLevels_Object = MibScalar
absAcpuLoggingLevels = _AbsAcpuLoggingLevels_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 8),
    _AbsAcpuLoggingLevels_Type()
)
absAcpuLoggingLevels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAcpuLoggingLevels.setStatus("current")


class _AbsCWAPLoggingLevels_Type(Integer32):
    """Custom type absCWAPLoggingLevels based on Integer32"""
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
        *(("emergencies", 1),
          ("alerts", 2),
          ("critical", 3),
          ("errors", 4),
          ("warnings", 5),
          ("notifications", 6),
          ("informational", 7),
          ("debugging", 8),
          ("none", 9))
    )


_AbsCWAPLoggingLevels_Type.__name__ = "Integer32"
_AbsCWAPLoggingLevels_Object = MibScalar
absCWAPLoggingLevels = _AbsCWAPLoggingLevels_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 9),
    _AbsCWAPLoggingLevels_Type()
)
absCWAPLoggingLevels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCWAPLoggingLevels.setStatus("current")


class _AbsAircardRawLogging_Type(Integer32):
    """Custom type absAircardRawLogging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AbsAircardRawLogging_Type.__name__ = "Integer32"
_AbsAircardRawLogging_Object = MibScalar
absAircardRawLogging = _AbsAircardRawLogging_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 10),
    _AbsAircardRawLogging_Type()
)
absAircardRawLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAircardRawLogging.setStatus("obsolete")


class _AbsAircardSendRawLogs_Type(Integer32):
    """Custom type absAircardSendRawLogs based on Integer32"""
    defaultValue = 2

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
        *(("atg", 1),
          ("tm", 2),
          ("all", 3),
          ("none", 4))
    )


_AbsAircardSendRawLogs_Type.__name__ = "Integer32"
_AbsAircardSendRawLogs_Object = MibScalar
absAircardSendRawLogs = _AbsAircardSendRawLogs_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 11),
    _AbsAircardSendRawLogs_Type()
)
absAircardSendRawLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAircardSendRawLogs.setStatus("obsolete")


class _AbsAircardRawLogStatemachine_Type(Integer32):
    """Custom type absAircardRawLogStatemachine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AbsAircardRawLogStatemachine_Type.__name__ = "Integer32"
_AbsAircardRawLogStatemachine_Object = MibScalar
absAircardRawLogStatemachine = _AbsAircardRawLogStatemachine_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 12),
    _AbsAircardRawLogStatemachine_Type()
)
absAircardRawLogStatemachine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAircardRawLogStatemachine.setStatus("obsolete")


class _AbsAircardEnableLogs_Type(Integer32):
    """Custom type absAircardEnableLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AbsAircardEnableLogs_Type.__name__ = "Integer32"
_AbsAircardEnableLogs_Object = MibScalar
absAircardEnableLogs = _AbsAircardEnableLogs_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 13),
    _AbsAircardEnableLogs_Type()
)
absAircardEnableLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAircardEnableLogs.setStatus("current")


class _AbsMediaLoaderPortAdminState_Type(Integer32):
    """Custom type absMediaLoaderPortAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AbsMediaLoaderPortAdminState_Type.__name__ = "Integer32"
_AbsMediaLoaderPortAdminState_Object = MibScalar
absMediaLoaderPortAdminState = _AbsMediaLoaderPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 14),
    _AbsMediaLoaderPortAdminState_Type()
)
absMediaLoaderPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absMediaLoaderPortAdminState.setStatus("obsolete")


class _AcpuFWLStatus_Type(Integer32):
    """Custom type acpuFWLStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AcpuFWLStatus_Type.__name__ = "Integer32"
_AcpuFWLStatus_Object = MibScalar
acpuFWLStatus = _AcpuFWLStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 15),
    _AcpuFWLStatus_Type()
)
acpuFWLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuFWLStatus.setStatus("obsolete")


class _AcpuIPSIDSStatus_Type(Integer32):
    """Custom type acpuIPSIDSStatus based on Integer32"""
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
        *(("enableIPS", 1),
          ("enableIDS", 2),
          ("disableSnort", 3))
    )


_AcpuIPSIDSStatus_Type.__name__ = "Integer32"
_AcpuIPSIDSStatus_Object = MibScalar
acpuIPSIDSStatus = _AcpuIPSIDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 16),
    _AcpuIPSIDSStatus_Type()
)
acpuIPSIDSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuIPSIDSStatus.setStatus("current")
_WirelessHandsetTable_Object = MibTable
wirelessHandsetTable = _WirelessHandsetTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    wirelessHandsetTable.setStatus("current")
_WirelessHandsetEntry_Object = MibTableRow
wirelessHandsetEntry = _WirelessHandsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 17, 1)
)
wirelessHandsetEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "wirelessHandsetIndex"),
)
if mibBuilder.loadTexts:
    wirelessHandsetEntry.setStatus("current")


class _WirelessHandsetIndex_Type(Integer32):
    """Custom type wirelessHandsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WirelessHandsetIndex_Type.__name__ = "Integer32"
_WirelessHandsetIndex_Object = MibTableColumn
wirelessHandsetIndex = _WirelessHandsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 17, 1, 1),
    _WirelessHandsetIndex_Type()
)
wirelessHandsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wirelessHandsetIndex.setStatus("current")


class _WirelessHandsetAdminStatus_Type(Integer32):
    """Custom type wirelessHandsetAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_WirelessHandsetAdminStatus_Type.__name__ = "Integer32"
_WirelessHandsetAdminStatus_Object = MibTableColumn
wirelessHandsetAdminStatus = _WirelessHandsetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 17, 1, 2),
    _WirelessHandsetAdminStatus_Type()
)
wirelessHandsetAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wirelessHandsetAdminStatus.setStatus("current")


class _WirelessHandsetOperStatus_Type(Integer32):
    """Custom type wirelessHandsetOperStatus based on Integer32"""
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


_WirelessHandsetOperStatus_Type.__name__ = "Integer32"
_WirelessHandsetOperStatus_Object = MibTableColumn
wirelessHandsetOperStatus = _WirelessHandsetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 17, 1, 3),
    _WirelessHandsetOperStatus_Type()
)
wirelessHandsetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessHandsetOperStatus.setStatus("current")
_WirelessHandsetRowStatus_Type = RowStatus
_WirelessHandsetRowStatus_Object = MibTableColumn
wirelessHandsetRowStatus = _WirelessHandsetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 17, 1, 4),
    _WirelessHandsetRowStatus_Type()
)
wirelessHandsetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wirelessHandsetRowStatus.setStatus("current")
_WapTable_Object = MibTable
wapTable = _WapTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    wapTable.setStatus("current")
_WapEntry_Object = MibTableRow
wapEntry = _WapEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1)
)
wapEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "wapIndex"),
)
if mibBuilder.loadTexts:
    wapEntry.setStatus("current")


class _WapIndex_Type(Integer32):
    """Custom type wapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WapIndex_Type.__name__ = "Integer32"
_WapIndex_Object = MibTableColumn
wapIndex = _WapIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 1),
    _WapIndex_Type()
)
wapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wapIndex.setStatus("current")


class _WapAdminStatus11A_Type(Integer32):
    """Custom type wapAdminStatus11A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_WapAdminStatus11A_Type.__name__ = "Integer32"
_WapAdminStatus11A_Object = MibTableColumn
wapAdminStatus11A = _WapAdminStatus11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 2),
    _WapAdminStatus11A_Type()
)
wapAdminStatus11A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wapAdminStatus11A.setStatus("current")


class _WapAdminStatus11B_Type(Integer32):
    """Custom type wapAdminStatus11B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_WapAdminStatus11B_Type.__name__ = "Integer32"
_WapAdminStatus11B_Object = MibTableColumn
wapAdminStatus11B = _WapAdminStatus11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 3),
    _WapAdminStatus11B_Type()
)
wapAdminStatus11B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wapAdminStatus11B.setStatus("current")


class _WapOperStatus11A_Type(Integer32):
    """Custom type wapOperStatus11A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_WapOperStatus11A_Type.__name__ = "Integer32"
_WapOperStatus11A_Object = MibTableColumn
wapOperStatus11A = _WapOperStatus11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 4),
    _WapOperStatus11A_Type()
)
wapOperStatus11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapOperStatus11A.setStatus("current")


class _WapOperStatus11B_Type(Integer32):
    """Custom type wapOperStatus11B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_WapOperStatus11B_Type.__name__ = "Integer32"
_WapOperStatus11B_Object = MibTableColumn
wapOperStatus11B = _WapOperStatus11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 5),
    _WapOperStatus11B_Type()
)
wapOperStatus11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapOperStatus11B.setStatus("current")
_WapActiveWirelessClients11A_Type = Integer32
_WapActiveWirelessClients11A_Object = MibTableColumn
wapActiveWirelessClients11A = _WapActiveWirelessClients11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 6),
    _WapActiveWirelessClients11A_Type()
)
wapActiveWirelessClients11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapActiveWirelessClients11A.setStatus("current")
_WapActiveWirelessClients11B_Type = Integer32
_WapActiveWirelessClients11B_Object = MibTableColumn
wapActiveWirelessClients11B = _WapActiveWirelessClients11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 7),
    _WapActiveWirelessClients11B_Type()
)
wapActiveWirelessClients11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapActiveWirelessClients11B.setStatus("current")
_WapRadioLinkRate11A_Type = Counter64
_WapRadioLinkRate11A_Object = MibTableColumn
wapRadioLinkRate11A = _WapRadioLinkRate11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 8),
    _WapRadioLinkRate11A_Type()
)
wapRadioLinkRate11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioLinkRate11A.setStatus("current")
_WapRadioLinkRate11B_Type = Counter64
_WapRadioLinkRate11B_Object = MibTableColumn
wapRadioLinkRate11B = _WapRadioLinkRate11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 9),
    _WapRadioLinkRate11B_Type()
)
wapRadioLinkRate11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioLinkRate11B.setStatus("current")
_WapRadioInPackets11A_Type = Counter64
_WapRadioInPackets11A_Object = MibTableColumn
wapRadioInPackets11A = _WapRadioInPackets11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 10),
    _WapRadioInPackets11A_Type()
)
wapRadioInPackets11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioInPackets11A.setStatus("current")
_WapRadioInPackets11B_Type = Counter64
_WapRadioInPackets11B_Object = MibTableColumn
wapRadioInPackets11B = _WapRadioInPackets11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 11),
    _WapRadioInPackets11B_Type()
)
wapRadioInPackets11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioInPackets11B.setStatus("current")
_WapRadioOutPackets11A_Type = Counter64
_WapRadioOutPackets11A_Object = MibTableColumn
wapRadioOutPackets11A = _WapRadioOutPackets11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 12),
    _WapRadioOutPackets11A_Type()
)
wapRadioOutPackets11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioOutPackets11A.setStatus("current")
_WapRadioOutPackets11B_Type = Counter64
_WapRadioOutPackets11B_Object = MibTableColumn
wapRadioOutPackets11B = _WapRadioOutPackets11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 13),
    _WapRadioOutPackets11B_Type()
)
wapRadioOutPackets11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioOutPackets11B.setStatus("current")
_WapRadioPortDuplexity11A_Type = Integer32
_WapRadioPortDuplexity11A_Object = MibTableColumn
wapRadioPortDuplexity11A = _WapRadioPortDuplexity11A_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 14),
    _WapRadioPortDuplexity11A_Type()
)
wapRadioPortDuplexity11A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioPortDuplexity11A.setStatus("current")
_WapRadioPortDuplexity11B_Type = Integer32
_WapRadioPortDuplexity11B_Object = MibTableColumn
wapRadioPortDuplexity11B = _WapRadioPortDuplexity11B_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 15),
    _WapRadioPortDuplexity11B_Type()
)
wapRadioPortDuplexity11B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRadioPortDuplexity11B.setStatus("current")
_WapPowerOpState_Type = Integer32
_WapPowerOpState_Object = MibTableColumn
wapPowerOpState = _WapPowerOpState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 18, 1, 16),
    _WapPowerOpState_Type()
)
wapPowerOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapPowerOpState.setStatus("current")


class _AcpuQosStatus_Type(Integer32):
    """Custom type acpuQosStatus based on Integer32"""
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
        *(("locked", 1),
          ("unlocked", 2),
          ("marking", 3))
    )


_AcpuQosStatus_Type.__name__ = "Integer32"
_AcpuQosStatus_Object = MibScalar
acpuQosStatus = _AcpuQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 19),
    _AcpuQosStatus_Type()
)
acpuQosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuQosStatus.setStatus("current")
_AcpuDot11SsidTable_Object = MibTable
acpuDot11SsidTable = _AcpuDot11SsidTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 20)
)
if mibBuilder.loadTexts:
    acpuDot11SsidTable.setStatus("current")
_AcpuDot11SsidEntry_Object = MibTableRow
acpuDot11SsidEntry = _AcpuDot11SsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 20, 1)
)
acpuDot11SsidEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "acpuDot11SsidIndex"),
)
if mibBuilder.loadTexts:
    acpuDot11SsidEntry.setStatus("current")


class _AcpuDot11SsidIndex_Type(Integer32):
    """Custom type acpuDot11SsidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AcpuDot11SsidIndex_Type.__name__ = "Integer32"
_AcpuDot11SsidIndex_Object = MibTableColumn
acpuDot11SsidIndex = _AcpuDot11SsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 20, 1, 1),
    _AcpuDot11SsidIndex_Type()
)
acpuDot11SsidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpuDot11SsidIndex.setStatus("current")
_AcpuDot11SsidVlanName_Type = DisplayString
_AcpuDot11SsidVlanName_Object = MibTableColumn
acpuDot11SsidVlanName = _AcpuDot11SsidVlanName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 20, 1, 2),
    _AcpuDot11SsidVlanName_Type()
)
acpuDot11SsidVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuDot11SsidVlanName.setStatus("current")


class _AcpuDot11SsidMbssidBroadcast_Type(Integer32):
    """Custom type acpuDot11SsidMbssidBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AcpuDot11SsidMbssidBroadcast_Type.__name__ = "Integer32"
_AcpuDot11SsidMbssidBroadcast_Object = MibTableColumn
acpuDot11SsidMbssidBroadcast = _AcpuDot11SsidMbssidBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 20, 1, 3),
    _AcpuDot11SsidMbssidBroadcast_Type()
)
acpuDot11SsidMbssidBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuDot11SsidMbssidBroadcast.setStatus("current")
_AcpuDot11VlanSecurityTable_Object = MibTable
acpuDot11VlanSecurityTable = _AcpuDot11VlanSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityTable.setStatus("current")
_AcpuDot11VlanSecurityEntry_Object = MibTableRow
acpuDot11VlanSecurityEntry = _AcpuDot11VlanSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21, 1)
)
acpuDot11VlanSecurityEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "acpuDot11VlanSecurityVlanId"),
)
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityEntry.setStatus("current")


class _AcpuDot11VlanSecurityVlanId_Type(Integer32):
    """Custom type acpuDot11VlanSecurityVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AcpuDot11VlanSecurityVlanId_Type.__name__ = "Integer32"
_AcpuDot11VlanSecurityVlanId_Object = MibTableColumn
acpuDot11VlanSecurityVlanId = _AcpuDot11VlanSecurityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21, 1, 1),
    _AcpuDot11VlanSecurityVlanId_Type()
)
acpuDot11VlanSecurityVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityVlanId.setStatus("current")
_AcpuDot11VlanSecurityVlanName_Type = DisplayString
_AcpuDot11VlanSecurityVlanName_Object = MibTableColumn
acpuDot11VlanSecurityVlanName = _AcpuDot11VlanSecurityVlanName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21, 1, 2),
    _AcpuDot11VlanSecurityVlanName_Type()
)
acpuDot11VlanSecurityVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityVlanName.setStatus("current")
_AcpuDot11VlanSecurityWpaPsk_Type = DisplayString
_AcpuDot11VlanSecurityWpaPsk_Object = MibTableColumn
acpuDot11VlanSecurityWpaPsk = _AcpuDot11VlanSecurityWpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21, 1, 3),
    _AcpuDot11VlanSecurityWpaPsk_Type()
)
acpuDot11VlanSecurityWpaPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityWpaPsk.setStatus("current")


class _AcpuDot11VlanSecurityStatus_Type(Integer32):
    """Custom type acpuDot11VlanSecurityStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AcpuDot11VlanSecurityStatus_Type.__name__ = "Integer32"
_AcpuDot11VlanSecurityStatus_Object = MibTableColumn
acpuDot11VlanSecurityStatus = _AcpuDot11VlanSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21, 1, 4),
    _AcpuDot11VlanSecurityStatus_Type()
)
acpuDot11VlanSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityStatus.setStatus("current")
_AcpuDot11VlanSecurityRowStatus_Type = RowStatus
_AcpuDot11VlanSecurityRowStatus_Object = MibTableColumn
acpuDot11VlanSecurityRowStatus = _AcpuDot11VlanSecurityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 1, 21, 1, 5),
    _AcpuDot11VlanSecurityRowStatus_Type()
)
acpuDot11VlanSecurityRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuDot11VlanSecurityRowStatus.setStatus("current")
_AbsSystemInfo_ObjectIdentity = ObjectIdentity
absSystemInfo = _AbsSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2)
)


class _AbsOperationalStatus_Type(Integer32):
    """Custom type absOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AbsOperationalStatus_Type.__name__ = "Integer32"
_AbsOperationalStatus_Object = MibScalar
absOperationalStatus = _AbsOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 1),
    _AbsOperationalStatus_Type()
)
absOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absOperationalStatus.setStatus("current")


class _AcpuOperationalStatus_Type(Integer32):
    """Custom type acpuOperationalStatus based on Integer32"""
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


_AcpuOperationalStatus_Type.__name__ = "Integer32"
_AcpuOperationalStatus_Object = MibScalar
acpuOperationalStatus = _AcpuOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 2),
    _AcpuOperationalStatus_Type()
)
acpuOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuOperationalStatus.setStatus("current")


class _AacuAtgModemOpStatus_Type(Integer32):
    """Custom type aacuAtgModemOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AacuAtgModemOpStatus_Type.__name__ = "Integer32"
_AacuAtgModemOpStatus_Object = MibScalar
aacuAtgModemOpStatus = _AacuAtgModemOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 3),
    _AacuAtgModemOpStatus_Type()
)
aacuAtgModemOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacuAtgModemOpStatus.setStatus("current")


class _AcpuAtgModemLinkStatus_Type(Integer32):
    """Custom type acpuAtgModemLinkStatus based on Integer32"""
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


_AcpuAtgModemLinkStatus_Type.__name__ = "Integer32"
_AcpuAtgModemLinkStatus_Object = MibScalar
acpuAtgModemLinkStatus = _AcpuAtgModemLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 4),
    _AcpuAtgModemLinkStatus_Type()
)
acpuAtgModemLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuAtgModemLinkStatus.setStatus("current")


class _AacuTerrModemOpStatus_Type(Integer32):
    """Custom type aacuTerrModemOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AacuTerrModemOpStatus_Type.__name__ = "Integer32"
_AacuTerrModemOpStatus_Object = MibScalar
aacuTerrModemOpStatus = _AacuTerrModemOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 5),
    _AacuTerrModemOpStatus_Type()
)
aacuTerrModemOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacuTerrModemOpStatus.setStatus("current")


class _AcpuTerrModemLinkStatus_Type(Integer32):
    """Custom type acpuTerrModemLinkStatus based on Integer32"""
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


_AcpuTerrModemLinkStatus_Type.__name__ = "Integer32"
_AcpuTerrModemLinkStatus_Object = MibScalar
acpuTerrModemLinkStatus = _AcpuTerrModemLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 6),
    _AcpuTerrModemLinkStatus_Type()
)
acpuTerrModemLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuTerrModemLinkStatus.setStatus("current")


class _AacuAuxCardOperationalStatus_Type(Integer32):
    """Custom type aacuAuxCardOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AacuAuxCardOperationalStatus_Type.__name__ = "Integer32"
_AacuAuxCardOperationalStatus_Object = MibScalar
aacuAuxCardOperationalStatus = _AacuAuxCardOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 7),
    _AacuAuxCardOperationalStatus_Type()
)
aacuAuxCardOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacuAuxCardOperationalStatus.setStatus("current")


class _AcpugpsHealthStatus_Type(Integer32):
    """Custom type acpugpsHealthStatus based on Integer32"""
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


_AcpugpsHealthStatus_Type.__name__ = "Integer32"
_AcpugpsHealthStatus_Object = MibScalar
acpugpsHealthStatus = _AcpugpsHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 8),
    _AcpugpsHealthStatus_Type()
)
acpugpsHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsHealthStatus.setStatus("current")


class _PassurHealthStatus_Type(Integer32):
    """Custom type passurHealthStatus based on Integer32"""
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


_PassurHealthStatus_Type.__name__ = "Integer32"
_PassurHealthStatus_Object = MibScalar
passurHealthStatus = _PassurHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 9),
    _PassurHealthStatus_Type()
)
passurHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurHealthStatus.setStatus("current")
_AcpuAltitude_Type = DisplayString
_AcpuAltitude_Object = MibScalar
acpuAltitude = _AcpuAltitude_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 10),
    _AcpuAltitude_Type()
)
acpuAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuAltitude.setStatus("current")
if mibBuilder.loadTexts:
    acpuAltitude.setUnits("Meters")


class _CwapType_Type(Integer32):
    """Custom type cwapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("cisco", 1),
          ("meru", 2))
    )


_CwapType_Type.__name__ = "Integer32"
_CwapType_Object = MibScalar
cwapType = _CwapType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 11),
    _CwapType_Type()
)
cwapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwapType.setStatus("current")


class _MeruControllerOperationalStatus_Type(Integer32):
    """Custom type meruControllerOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_MeruControllerOperationalStatus_Type.__name__ = "Integer32"
_MeruControllerOperationalStatus_Object = MibScalar
meruControllerOperationalStatus = _MeruControllerOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 12),
    _MeruControllerOperationalStatus_Type()
)
meruControllerOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meruControllerOperationalStatus.setStatus("current")


class _AcpuVenturiTunnelModeAdminStatus_Type(Integer32):
    """Custom type acpuVenturiTunnelModeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AcpuVenturiTunnelModeAdminStatus_Type.__name__ = "Integer32"
_AcpuVenturiTunnelModeAdminStatus_Object = MibScalar
acpuVenturiTunnelModeAdminStatus = _AcpuVenturiTunnelModeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 13),
    _AcpuVenturiTunnelModeAdminStatus_Type()
)
acpuVenturiTunnelModeAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuVenturiTunnelModeAdminStatus.setStatus("current")


class _AcpuVenturiClientStatus_Type(Integer32):
    """Custom type acpuVenturiClientStatus based on Integer32"""
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


_AcpuVenturiClientStatus_Type.__name__ = "Integer32"
_AcpuVenturiClientStatus_Object = MibScalar
acpuVenturiClientStatus = _AcpuVenturiClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 14),
    _AcpuVenturiClientStatus_Type()
)
acpuVenturiClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuVenturiClientStatus.setStatus("current")


class _AcpuVenturiTunnelStatus_Type(Integer32):
    """Custom type acpuVenturiTunnelStatus based on Integer32"""
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


_AcpuVenturiTunnelStatus_Type.__name__ = "Integer32"
_AcpuVenturiTunnelStatus_Object = MibScalar
acpuVenturiTunnelStatus = _AcpuVenturiTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 15),
    _AcpuVenturiTunnelStatus_Type()
)
acpuVenturiTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuVenturiTunnelStatus.setStatus("current")


class _Acpu429HealthStatus_Type(Integer32):
    """Custom type acpu429HealthStatus based on Integer32"""
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


_Acpu429HealthStatus_Type.__name__ = "Integer32"
_Acpu429HealthStatus_Object = MibScalar
acpu429HealthStatus = _Acpu429HealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 2, 27),
    _Acpu429HealthStatus_Type()
)
acpu429HealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpu429HealthStatus.setStatus("current")
_AbsControlData_ObjectIdentity = ObjectIdentity
absControlData = _AbsControlData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3)
)
_AbsPositionData_ObjectIdentity = ObjectIdentity
absPositionData = _AbsPositionData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1)
)
_AcpugpsLatitude_Type = DisplayString
_AcpugpsLatitude_Object = MibScalar
acpugpsLatitude = _AcpugpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 1),
    _AcpugpsLatitude_Type()
)
acpugpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsLatitude.setStatus("current")
if mibBuilder.loadTexts:
    acpugpsLatitude.setUnits("Degrees")
_AcpugpsLongitude_Type = DisplayString
_AcpugpsLongitude_Object = MibScalar
acpugpsLongitude = _AcpugpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 2),
    _AcpugpsLongitude_Type()
)
acpugpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsLongitude.setStatus("current")
if mibBuilder.loadTexts:
    acpugpsLongitude.setUnits("Degrees")
_AcpugpsAltitude_Type = DisplayString
_AcpugpsAltitude_Object = MibScalar
acpugpsAltitude = _AcpugpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 3),
    _AcpugpsAltitude_Type()
)
acpugpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsAltitude.setStatus("current")
if mibBuilder.loadTexts:
    acpugpsAltitude.setUnits("Meters")
_AcpugpsHorVelocity_Type = DisplayString
_AcpugpsHorVelocity_Object = MibScalar
acpugpsHorVelocity = _AcpugpsHorVelocity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 4),
    _AcpugpsHorVelocity_Type()
)
acpugpsHorVelocity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsHorVelocity.setStatus("current")
if mibBuilder.loadTexts:
    acpugpsHorVelocity.setUnits("Meters/Sec")
_AcpugpsVerVelocity_Type = DisplayString
_AcpugpsVerVelocity_Object = MibScalar
acpugpsVerVelocity = _AcpugpsVerVelocity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 5),
    _AcpugpsVerVelocity_Type()
)
acpugpsVerVelocity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsVerVelocity.setStatus("current")
if mibBuilder.loadTexts:
    acpugpsVerVelocity.setUnits("Meters/Sec")
_AcpugpsUTCTime_Type = DisplayString
_AcpugpsUTCTime_Object = MibScalar
acpugpsUTCTime = _AcpugpsUTCTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 6),
    _AcpugpsUTCTime_Type()
)
acpugpsUTCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsUTCTime.setStatus("current")
_AcpugpsLocalTime_Type = DisplayString
_AcpugpsLocalTime_Object = MibScalar
acpugpsLocalTime = _AcpugpsLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 7),
    _AcpugpsLocalTime_Type()
)
acpugpsLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsLocalTime.setStatus("deprecated")
_AcpugpsLocalZoneHourOffset_Type = Integer32
_AcpugpsLocalZoneHourOffset_Object = MibScalar
acpugpsLocalZoneHourOffset = _AcpugpsLocalZoneHourOffset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 8),
    _AcpugpsLocalZoneHourOffset_Type()
)
acpugpsLocalZoneHourOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsLocalZoneHourOffset.setStatus("deprecated")
_AcpugpsLocalZoneMinutesOffset_Type = Integer32
_AcpugpsLocalZoneMinutesOffset_Object = MibScalar
acpugpsLocalZoneMinutesOffset = _AcpugpsLocalZoneMinutesOffset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 9),
    _AcpugpsLocalZoneMinutesOffset_Type()
)
acpugpsLocalZoneMinutesOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsLocalZoneMinutesOffset.setStatus("deprecated")
_AcpugpsNumOfGPSSat_Type = Integer32
_AcpugpsNumOfGPSSat_Object = MibScalar
acpugpsNumOfGPSSat = _AcpugpsNumOfGPSSat_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 10),
    _AcpugpsNumOfGPSSat_Type()
)
acpugpsNumOfGPSSat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpugpsNumOfGPSSat.setStatus("current")
_Acpu429PitchAngle_Type = DisplayString
_Acpu429PitchAngle_Object = MibScalar
acpu429PitchAngle = _Acpu429PitchAngle_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 11),
    _Acpu429PitchAngle_Type()
)
acpu429PitchAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpu429PitchAngle.setStatus("current")
_Acpu429RollAngle_Type = DisplayString
_Acpu429RollAngle_Object = MibScalar
acpu429RollAngle = _Acpu429RollAngle_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 12),
    _Acpu429RollAngle_Type()
)
acpu429RollAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpu429RollAngle.setStatus("current")
_Acpu429TrackAngle_Type = DisplayString
_Acpu429TrackAngle_Object = MibScalar
acpu429TrackAngle = _Acpu429TrackAngle_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 1, 13),
    _Acpu429TrackAngle_Type()
)
acpu429TrackAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpu429TrackAngle.setStatus("current")
_AbsFlightInfo_ObjectIdentity = ObjectIdentity
absFlightInfo = _AbsFlightInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2)
)
_PassurFlightNumber_Type = DisplayString
_PassurFlightNumber_Object = MibScalar
passurFlightNumber = _PassurFlightNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 1),
    _PassurFlightNumber_Type()
)
passurFlightNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurFlightNumber.setStatus("current")
_PassurDepartureUTCTime_Type = DisplayString
_PassurDepartureUTCTime_Object = MibScalar
passurDepartureUTCTime = _PassurDepartureUTCTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 2),
    _PassurDepartureUTCTime_Type()
)
passurDepartureUTCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurDepartureUTCTime.setStatus("current")
_PassurDepartureLocalTime_Type = DisplayString
_PassurDepartureLocalTime_Object = MibScalar
passurDepartureLocalTime = _PassurDepartureLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 3),
    _PassurDepartureLocalTime_Type()
)
passurDepartureLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurDepartureLocalTime.setStatus("current")
_PassurArrivalUTCTime_Type = DisplayString
_PassurArrivalUTCTime_Object = MibScalar
passurArrivalUTCTime = _PassurArrivalUTCTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 4),
    _PassurArrivalUTCTime_Type()
)
passurArrivalUTCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurArrivalUTCTime.setStatus("current")
_PassurArrivalLocalTime_Type = DisplayString
_PassurArrivalLocalTime_Object = MibScalar
passurArrivalLocalTime = _PassurArrivalLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 5),
    _PassurArrivalLocalTime_Type()
)
passurArrivalLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurArrivalLocalTime.setStatus("current")
_PassurEstimatedArrivalUTCTime_Type = DisplayString
_PassurEstimatedArrivalUTCTime_Object = MibScalar
passurEstimatedArrivalUTCTime = _PassurEstimatedArrivalUTCTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 6),
    _PassurEstimatedArrivalUTCTime_Type()
)
passurEstimatedArrivalUTCTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurEstimatedArrivalUTCTime.setStatus("current")
_PassurEstimatedArrivalLocalTime_Type = DisplayString
_PassurEstimatedArrivalLocalTime_Object = MibScalar
passurEstimatedArrivalLocalTime = _PassurEstimatedArrivalLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 7),
    _PassurEstimatedArrivalLocalTime_Type()
)
passurEstimatedArrivalLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurEstimatedArrivalLocalTime.setStatus("current")
_PassurDepartureCity_Type = DisplayString
_PassurDepartureCity_Object = MibScalar
passurDepartureCity = _PassurDepartureCity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 8),
    _PassurDepartureCity_Type()
)
passurDepartureCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurDepartureCity.setStatus("current")
_PassurDepartureAirport_Type = DisplayString
_PassurDepartureAirport_Object = MibScalar
passurDepartureAirport = _PassurDepartureAirport_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 9),
    _PassurDepartureAirport_Type()
)
passurDepartureAirport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurDepartureAirport.setStatus("current")
_PassurDestinationCity_Type = DisplayString
_PassurDestinationCity_Object = MibScalar
passurDestinationCity = _PassurDestinationCity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 10),
    _PassurDestinationCity_Type()
)
passurDestinationCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurDestinationCity.setStatus("current")
_PassurDestinationAirport_Type = DisplayString
_PassurDestinationAirport_Object = MibScalar
passurDestinationAirport = _PassurDestinationAirport_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 11),
    _PassurDestinationAirport_Type()
)
passurDestinationAirport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurDestinationAirport.setStatus("current")
_PassurFlightRouteWayPoints_Type = DisplayString
_PassurFlightRouteWayPoints_Object = MibScalar
passurFlightRouteWayPoints = _PassurFlightRouteWayPoints_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 12),
    _PassurFlightRouteWayPoints_Type()
)
passurFlightRouteWayPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passurFlightRouteWayPoints.setStatus("current")
_AbsTotalClientCount_Type = Integer32
_AbsTotalClientCount_Object = MibScalar
absTotalClientCount = _AbsTotalClientCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 13),
    _AbsTotalClientCount_Type()
)
absTotalClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absTotalClientCount.setStatus("current")
_AbsAtgClientCount_Type = Integer32
_AbsAtgClientCount_Object = MibScalar
absAtgClientCount = _AbsAtgClientCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 14),
    _AbsAtgClientCount_Type()
)
absAtgClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAtgClientCount.setStatus("current")
_AbsAircardSectorID_Type = OctetString
_AbsAircardSectorID_Object = MibScalar
absAircardSectorID = _AbsAircardSectorID_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 15),
    _AbsAircardSectorID_Type()
)
absAircardSectorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardSectorID.setStatus("current")
_AbsPeakFLRate_Type = Integer32
_AbsPeakFLRate_Object = MibScalar
absPeakFLRate = _AbsPeakFLRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 16),
    _AbsPeakFLRate_Type()
)
absPeakFLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absPeakFLRate.setStatus("current")
_AbsAverageFLRate_Type = Integer32
_AbsAverageFLRate_Object = MibScalar
absAverageFLRate = _AbsAverageFLRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 17),
    _AbsAverageFLRate_Type()
)
absAverageFLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAverageFLRate.setStatus("current")
_AbsPeakRLRate_Type = Integer32
_AbsPeakRLRate_Object = MibScalar
absPeakRLRate = _AbsPeakRLRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 18),
    _AbsPeakRLRate_Type()
)
absPeakRLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absPeakRLRate.setStatus("current")
_AbsAverageRLRate_Type = Integer32
_AbsAverageRLRate_Object = MibScalar
absAverageRLRate = _AbsAverageRLRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 19),
    _AbsAverageRLRate_Type()
)
absAverageRLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAverageRLRate.setStatus("current")
_AbsAircardRx0AGC_Type = Integer32
_AbsAircardRx0AGC_Object = MibScalar
absAircardRx0AGC = _AbsAircardRx0AGC_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 20),
    _AbsAircardRx0AGC_Type()
)
absAircardRx0AGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardRx0AGC.setStatus("current")
_AbsAircardTxAGC_Type = Integer32
_AbsAircardTxAGC_Object = MibScalar
absAircardTxAGC = _AbsAircardTxAGC_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 21),
    _AbsAircardTxAGC_Type()
)
absAircardTxAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardTxAGC.setStatus("current")
_AbsAircardRx1AGC_Type = Integer32
_AbsAircardRx1AGC_Object = MibScalar
absAircardRx1AGC = _AbsAircardRx1AGC_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 22),
    _AbsAircardRx1AGC_Type()
)
absAircardRx1AGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardRx1AGC.setStatus("current")
_AbsAircardSignalStrength_Type = OctetString
_AbsAircardSignalStrength_Object = MibScalar
absAircardSignalStrength = _AbsAircardSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 23),
    _AbsAircardSignalStrength_Type()
)
absAircardSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardSignalStrength.setStatus("current")
_AbsAircardPilotPN_Type = Integer32
_AbsAircardPilotPN_Object = MibScalar
absAircardPilotPN = _AbsAircardPilotPN_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 24),
    _AbsAircardPilotPN_Type()
)
absAircardPilotPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardPilotPN.setStatus("obsolete")
_AbsAircardPNOffset_Type = Integer32
_AbsAircardPNOffset_Object = MibScalar
absAircardPNOffset = _AbsAircardPNOffset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 25),
    _AbsAircardPNOffset_Type()
)
absAircardPNOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardPNOffset.setStatus("current")
_AbsAircardPilotPNASP_Type = OctetString
_AbsAircardPilotPNASP_Object = MibScalar
absAircardPilotPNASP = _AbsAircardPilotPNASP_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 26),
    _AbsAircardPilotPNASP_Type()
)
absAircardPilotPNASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardPilotPNASP.setStatus("current")


class _AbsAircardPilotStrength_Type(Integer32):
    """Custom type absAircardPilotStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AbsAircardPilotStrength_Type.__name__ = "Integer32"
_AbsAircardPilotStrength_Object = MibScalar
absAircardPilotStrength = _AbsAircardPilotStrength_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 27),
    _AbsAircardPilotStrength_Type()
)
absAircardPilotStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAircardPilotStrength.setStatus("obsolete")
_AbsTotalActiveClientCount_Type = Integer32
_AbsTotalActiveClientCount_Object = MibScalar
absTotalActiveClientCount = _AbsTotalActiveClientCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 28),
    _AbsTotalActiveClientCount_Type()
)
absTotalActiveClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absTotalActiveClientCount.setStatus("current")
_AbsKUSignalStrength_Type = Integer32
_AbsKUSignalStrength_Object = MibScalar
absKUSignalStrength = _AbsKUSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 48),
    _AbsKUSignalStrength_Type()
)
absKUSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absKUSignalStrength.setStatus("current")
_AbsAcmuOperStatus_Type = Integer32
_AbsAcmuOperStatus_Object = MibScalar
absAcmuOperStatus = _AbsAcmuOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 49),
    _AbsAcmuOperStatus_Type()
)
absAcmuOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcmuOperStatus.setStatus("current")
_AbsKULinkStatus_Type = Integer32
_AbsKULinkStatus_Object = MibScalar
absKULinkStatus = _AbsKULinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 50),
    _AbsKULinkStatus_Type()
)
absKULinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absKULinkStatus.setStatus("current")
_AbsOvtTunnelStatus_Type = Integer32
_AbsOvtTunnelStatus_Object = MibScalar
absOvtTunnelStatus = _AbsOvtTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 51),
    _AbsOvtTunnelStatus_Type()
)
absOvtTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absOvtTunnelStatus.setStatus("current")
_AbsSBBOperStatus_Type = Integer32
_AbsSBBOperStatus_Object = MibScalar
absSBBOperStatus = _AbsSBBOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 52),
    _AbsSBBOperStatus_Type()
)
absSBBOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absSBBOperStatus.setStatus("current")
_AbsSBBLinkStatus_Type = Integer32
_AbsSBBLinkStatus_Object = MibScalar
absSBBLinkStatus = _AbsSBBLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 53),
    _AbsSBBLinkStatus_Type()
)
absSBBLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absSBBLinkStatus.setStatus("current")
_AbsSBBSignalStrength_Type = OctetString
_AbsSBBSignalStrength_Object = MibScalar
absSBBSignalStrength = _AbsSBBSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 54),
    _AbsSBBSignalStrength_Type()
)
absSBBSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absSBBSignalStrength.setStatus("current")
_SbbPacketErrorRate_Type = OctetString
_SbbPacketErrorRate_Object = MibScalar
sbbPacketErrorRate = _SbbPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 2, 55),
    _SbbPacketErrorRate_Type()
)
sbbPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbbPacketErrorRate.setStatus("current")
_AbsAircraftIdData_ObjectIdentity = ObjectIdentity
absAircraftIdData = _AbsAircraftIdData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3)
)
_AircraftTailNum_Type = DisplayString
_AircraftTailNum_Object = MibScalar
aircraftTailNum = _AircraftTailNum_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 1),
    _AircraftTailNum_Type()
)
aircraftTailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aircraftTailNum.setStatus("current")
_AircraftType_Type = DisplayString
_AircraftType_Object = MibScalar
aircraftType = _AircraftType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 2),
    _AircraftType_Type()
)
aircraftType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aircraftType.setStatus("current")
_AirlineName_Type = DisplayString
_AirlineName_Object = MibScalar
airlineName = _AirlineName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 3),
    _AirlineName_Type()
)
airlineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airlineName.setStatus("current")
_WapCount_Type = Integer32
_WapCount_Object = MibScalar
wapCount = _WapCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 4),
    _WapCount_Type()
)
wapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapCount.setStatus("current")
_WirelessHandsetCount_Type = Integer32
_WirelessHandsetCount_Object = MibScalar
wirelessHandsetCount = _WirelessHandsetCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 5),
    _WirelessHandsetCount_Type()
)
wirelessHandsetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessHandsetCount.setStatus("current")
_WiredHandsetCount_Type = Integer32
_WiredHandsetCount_Object = MibScalar
wiredHandsetCount = _WiredHandsetCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 6),
    _WiredHandsetCount_Type()
)
wiredHandsetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wiredHandsetCount.setStatus("current")
_AbsSoftwareVersion_Type = DisplayString
_AbsSoftwareVersion_Object = MibScalar
absSoftwareVersion = _AbsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 7),
    _AbsSoftwareVersion_Type()
)
absSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absSoftwareVersion.setStatus("current")


class _AbsArinc429Support_Type(Integer32):
    """Custom type absArinc429Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AbsArinc429Support_Type.__name__ = "Integer32"
_AbsArinc429Support_Object = MibScalar
absArinc429Support = _AbsArinc429Support_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 3, 3, 10),
    _AbsArinc429Support_Type()
)
absArinc429Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absArinc429Support.setStatus("current")
_AbsLRUDetails_ObjectIdentity = ObjectIdentity
absLRUDetails = _AbsLRUDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4)
)
_AcpuInfo_Type = DisplayString
_AcpuInfo_Object = MibScalar
acpuInfo = _AcpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 1),
    _AcpuInfo_Type()
)
acpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuInfo.setStatus("current")
_AbsWhitelistVersion_Type = DisplayString
_AbsWhitelistVersion_Object = MibScalar
absWhitelistVersion = _AbsWhitelistVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 2),
    _AbsWhitelistVersion_Type()
)
absWhitelistVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absWhitelistVersion.setStatus("current")
_AbpVersion_Type = DisplayString
_AbpVersion_Object = MibScalar
abpVersion = _AbpVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 3),
    _AbpVersion_Type()
)
abpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abpVersion.setStatus("current")
_AircardInfo_Type = DisplayString
_AircardInfo_Object = MibScalar
aircardInfo = _AircardInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 4),
    _AircardInfo_Type()
)
aircardInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aircardInfo.setStatus("current")
_AuxcardInfo_Type = DisplayString
_AuxcardInfo_Object = MibScalar
auxcardInfo = _AuxcardInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 5),
    _AuxcardInfo_Type()
)
auxcardInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxcardInfo.setStatus("current")
_AcpuBios_Type = DisplayString
_AcpuBios_Object = MibScalar
acpuBios = _AcpuBios_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 6),
    _AcpuBios_Type()
)
acpuBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuBios.setStatus("current")
_AircardEsn_Type = DisplayString
_AircardEsn_Object = MibScalar
aircardEsn = _AircardEsn_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 7),
    _AircardEsn_Type()
)
aircardEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aircardEsn.setStatus("current")
_AcpuHardwareSerialNumber_Type = DisplayString
_AcpuHardwareSerialNumber_Object = MibScalar
acpuHardwareSerialNumber = _AcpuHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 8),
    _AcpuHardwareSerialNumber_Type()
)
acpuHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuHardwareSerialNumber.setStatus("current")
_AacuHardwareSerialNumber_Type = DisplayString
_AacuHardwareSerialNumber_Object = MibScalar
aacuHardwareSerialNumber = _AacuHardwareSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 9),
    _AacuHardwareSerialNumber_Type()
)
aacuHardwareSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aacuHardwareSerialNumber.setStatus("current")
_MeruControllerInfo_Type = DisplayString
_MeruControllerInfo_Object = MibScalar
meruControllerInfo = _MeruControllerInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 10),
    _MeruControllerInfo_Type()
)
meruControllerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meruControllerInfo.setStatus("current")
_VenturiInfo_Type = DisplayString
_VenturiInfo_Object = MibScalar
venturiInfo = _VenturiInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 11),
    _VenturiInfo_Type()
)
venturiInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    venturiInfo.setStatus("current")
_Cwap1Info_Type = DisplayString
_Cwap1Info_Object = MibScalar
cwap1Info = _Cwap1Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 12),
    _Cwap1Info_Type()
)
cwap1Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap1Info.setStatus("current")
_Cwap2Info_Type = DisplayString
_Cwap2Info_Object = MibScalar
cwap2Info = _Cwap2Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 13),
    _Cwap2Info_Type()
)
cwap2Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap2Info.setStatus("current")
_Cwap3Info_Type = DisplayString
_Cwap3Info_Object = MibScalar
cwap3Info = _Cwap3Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 14),
    _Cwap3Info_Type()
)
cwap3Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap3Info.setStatus("current")
_Cwap4Info_Type = DisplayString
_Cwap4Info_Object = MibScalar
cwap4Info = _Cwap4Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 15),
    _Cwap4Info_Type()
)
cwap4Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap4Info.setStatus("current")
_Cwap5Info_Type = DisplayString
_Cwap5Info_Object = MibScalar
cwap5Info = _Cwap5Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 16),
    _Cwap5Info_Type()
)
cwap5Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap5Info.setStatus("current")
_Cwap6Info_Type = DisplayString
_Cwap6Info_Object = MibScalar
cwap6Info = _Cwap6Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 17),
    _Cwap6Info_Type()
)
cwap6Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap6Info.setStatus("current")
_Cwap7Info_Type = DisplayString
_Cwap7Info_Object = MibScalar
cwap7Info = _Cwap7Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 18),
    _Cwap7Info_Type()
)
cwap7Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap7Info.setStatus("current")
_Cwap8Info_Type = DisplayString
_Cwap8Info_Object = MibScalar
cwap8Info = _Cwap8Info_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 19),
    _Cwap8Info_Type()
)
cwap8Info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwap8Info.setStatus("current")
_SatelliteSupport_Type = DisplayString
_SatelliteSupport_Object = MibScalar
satelliteSupport = _SatelliteSupport_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 20),
    _SatelliteSupport_Type()
)
satelliteSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteSupport.setStatus("current")
_WeightonWheelsSupport_Type = DisplayString
_WeightonWheelsSupport_Object = MibScalar
weightonWheelsSupport = _WeightonWheelsSupport_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 4, 21),
    _WeightonWheelsSupport_Type()
)
weightonWheelsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    weightonWheelsSupport.setStatus("current")
_AbsSoftwareConfig_ObjectIdentity = ObjectIdentity
absSoftwareConfig = _AbsSoftwareConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5)
)
_AbsBundleConfig_ObjectIdentity = ObjectIdentity
absBundleConfig = _AbsBundleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1)
)
_AbsCompatibleBundle_Type = DisplayString
_AbsCompatibleBundle_Object = MibScalar
absCompatibleBundle = _AbsCompatibleBundle_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 1),
    _AbsCompatibleBundle_Type()
)
absCompatibleBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCompatibleBundle.setStatus("current")
_AbsActivationBundle_Type = DisplayString
_AbsActivationBundle_Object = MibScalar
absActivationBundle = _AbsActivationBundle_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 2),
    _AbsActivationBundle_Type()
)
absActivationBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absActivationBundle.setStatus("current")


class _ActivateABSBundle_Type(Integer32):
    """Custom type activateABSBundle based on Integer32"""
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
        *(("unKnown", 1),
          ("compatibleBundle", 2),
          ("activationBundle", 3),
          ("runningBundle", 4))
    )


_ActivateABSBundle_Type.__name__ = "Integer32"
_ActivateABSBundle_Object = MibScalar
activateABSBundle = _ActivateABSBundle_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 3),
    _ActivateABSBundle_Type()
)
activateABSBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activateABSBundle.setStatus("current")


class _AbsBundleDownloadStatus_Type(Integer32):
    """Custom type absBundleDownloadStatus based on Integer32"""
    defaultValue = 1

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
        *(("unInitialized", 1),
          ("preLoadingInProgress", 2),
          ("preLoadingFailed", 3),
          ("compatibleBundleInProgress", 4),
          ("compatibleBundleCompleted", 5),
          ("compatibleBundleFailed", 6),
          ("activationBundleInProgress", 7),
          ("activationBundleCompleted", 8),
          ("activationBundleFailed", 9))
    )


_AbsBundleDownloadStatus_Type.__name__ = "Integer32"
_AbsBundleDownloadStatus_Object = MibScalar
absBundleDownloadStatus = _AbsBundleDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 4),
    _AbsBundleDownloadStatus_Type()
)
absBundleDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absBundleDownloadStatus.setStatus("current")
_AbsBundleDownloadAbortInfo_Type = DisplayString
_AbsBundleDownloadAbortInfo_Object = MibScalar
absBundleDownloadAbortInfo = _AbsBundleDownloadAbortInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 5),
    _AbsBundleDownloadAbortInfo_Type()
)
absBundleDownloadAbortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absBundleDownloadAbortInfo.setStatus("current")


class _AbsBundleActivationStatus_Type(Integer32):
    """Custom type absBundleActivationStatus based on Integer32"""
    defaultValue = 1

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
        *(("unInitialized", 1),
          ("activationRequestQueued", 2),
          ("queuedActivationRequestCleared", 3),
          ("preActivationInProgress", 4),
          ("preActivationFailed", 5),
          ("compatibleBundleInProgress", 6),
          ("compatibleBundleCompleted", 7),
          ("compatibleBundleFailed", 8),
          ("activationBundleInProgress", 9),
          ("activationBundleCompleted", 10),
          ("activationBundleFailed", 11))
    )


_AbsBundleActivationStatus_Type.__name__ = "Integer32"
_AbsBundleActivationStatus_Object = MibScalar
absBundleActivationStatus = _AbsBundleActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 6),
    _AbsBundleActivationStatus_Type()
)
absBundleActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absBundleActivationStatus.setStatus("current")
_AbsBundleActivationAbortInfo_Type = DisplayString
_AbsBundleActivationAbortInfo_Object = MibScalar
absBundleActivationAbortInfo = _AbsBundleActivationAbortInfo_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 1, 5, 1, 7),
    _AbsBundleActivationAbortInfo_Type()
)
absBundleActivationAbortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absBundleActivationAbortInfo.setStatus("current")
_AircellACPU_ObjectIdentity = ObjectIdentity
aircellACPU = _AircellACPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2)
)
_AcpuEthernetPort_ObjectIdentity = ObjectIdentity
acpuEthernetPort = _AcpuEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1)
)


class _AcpuEthernetPortState_Type(Integer32):
    """Custom type acpuEthernetPortState based on Integer32"""
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


_AcpuEthernetPortState_Type.__name__ = "Integer32"
_AcpuEthernetPortState_Object = MibScalar
acpuEthernetPortState = _AcpuEthernetPortState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 1),
    _AcpuEthernetPortState_Type()
)
acpuEthernetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortState.setStatus("current")
_AcpuEthernetPortLinkRate_Type = Integer32
_AcpuEthernetPortLinkRate_Object = MibScalar
acpuEthernetPortLinkRate = _AcpuEthernetPortLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 2),
    _AcpuEthernetPortLinkRate_Type()
)
acpuEthernetPortLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortLinkRate.setStatus("current")
_AcpuEthernetPortDuplexity_Type = Integer32
_AcpuEthernetPortDuplexity_Object = MibScalar
acpuEthernetPortDuplexity = _AcpuEthernetPortDuplexity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 3),
    _AcpuEthernetPortDuplexity_Type()
)
acpuEthernetPortDuplexity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortDuplexity.setStatus("current")
_AcpuEthernetPortRxCrcErrFrameCnt_Type = Counter64
_AcpuEthernetPortRxCrcErrFrameCnt_Object = MibScalar
acpuEthernetPortRxCrcErrFrameCnt = _AcpuEthernetPortRxCrcErrFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 4),
    _AcpuEthernetPortRxCrcErrFrameCnt_Type()
)
acpuEthernetPortRxCrcErrFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortRxCrcErrFrameCnt.setStatus("current")
_AcpuEthernetVlanTable_Object = MibTable
acpuEthernetVlanTable = _AcpuEthernetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    acpuEthernetVlanTable.setStatus("current")
_AcpuEthernetVlanEntry_Object = MibTableRow
acpuEthernetVlanEntry = _AcpuEthernetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1)
)
acpuEthernetVlanEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "acpuEthernetVlanID"),
)
if mibBuilder.loadTexts:
    acpuEthernetVlanEntry.setStatus("current")


class _AcpuEthernetVlanID_Type(Integer32):
    """Custom type acpuEthernetVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcpuEthernetVlanID_Type.__name__ = "Integer32"
_AcpuEthernetVlanID_Object = MibTableColumn
acpuEthernetVlanID = _AcpuEthernetVlanID_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1, 1),
    _AcpuEthernetVlanID_Type()
)
acpuEthernetVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpuEthernetVlanID.setStatus("current")


class _AcpuEthernetVlanState_Type(Integer32):
    """Custom type acpuEthernetVlanState based on Integer32"""
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


_AcpuEthernetVlanState_Type.__name__ = "Integer32"
_AcpuEthernetVlanState_Object = MibTableColumn
acpuEthernetVlanState = _AcpuEthernetVlanState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1, 2),
    _AcpuEthernetVlanState_Type()
)
acpuEthernetVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetVlanState.setStatus("current")
_AcpuEthernetVlanIpAddr_Type = IpAddress
_AcpuEthernetVlanIpAddr_Object = MibTableColumn
acpuEthernetVlanIpAddr = _AcpuEthernetVlanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1, 3),
    _AcpuEthernetVlanIpAddr_Type()
)
acpuEthernetVlanIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetVlanIpAddr.setStatus("current")
_AcpuEthernetVlanNetMask_Type = IpAddress
_AcpuEthernetVlanNetMask_Object = MibTableColumn
acpuEthernetVlanNetMask = _AcpuEthernetVlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1, 4),
    _AcpuEthernetVlanNetMask_Type()
)
acpuEthernetVlanNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetVlanNetMask.setStatus("current")
_AcpuEthernetVlanPorts_Type = Integer32
_AcpuEthernetVlanPorts_Object = MibTableColumn
acpuEthernetVlanPorts = _AcpuEthernetVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1, 5),
    _AcpuEthernetVlanPorts_Type()
)
acpuEthernetVlanPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acpuEthernetVlanPorts.setStatus("current")
_AcpuEthernetVlanRowStatus_Type = RowStatus
_AcpuEthernetVlanRowStatus_Object = MibTableColumn
acpuEthernetVlanRowStatus = _AcpuEthernetVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 5, 1, 6),
    _AcpuEthernetVlanRowStatus_Type()
)
acpuEthernetVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acpuEthernetVlanRowStatus.setStatus("current")
_AcpuEthernetPortVlanTable_Object = MibTable
acpuEthernetPortVlanTable = _AcpuEthernetPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    acpuEthernetPortVlanTable.setStatus("current")
_AcpuEthernetPortVlanEntry_Object = MibTableRow
acpuEthernetPortVlanEntry = _AcpuEthernetPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6, 1)
)
acpuEthernetPortVlanEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortIndex"),
    (0, "AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortVlanID"),
)
if mibBuilder.loadTexts:
    acpuEthernetPortVlanEntry.setStatus("current")


class _AcpuEthernetPortIndex_Type(Integer32):
    """Custom type acpuEthernetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcpuEthernetPortIndex_Type.__name__ = "Integer32"
_AcpuEthernetPortIndex_Object = MibTableColumn
acpuEthernetPortIndex = _AcpuEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6, 1, 1),
    _AcpuEthernetPortIndex_Type()
)
acpuEthernetPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acpuEthernetPortIndex.setStatus("current")


class _AcpuEthernetPortVlanID_Type(Integer32):
    """Custom type acpuEthernetPortVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcpuEthernetPortVlanID_Type.__name__ = "Integer32"
_AcpuEthernetPortVlanID_Object = MibTableColumn
acpuEthernetPortVlanID = _AcpuEthernetPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6, 1, 2),
    _AcpuEthernetPortVlanID_Type()
)
acpuEthernetPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortVlanID.setStatus("current")
_AcpuEthernetPortVlanTxOctets_Type = Counter64
_AcpuEthernetPortVlanTxOctets_Object = MibTableColumn
acpuEthernetPortVlanTxOctets = _AcpuEthernetPortVlanTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6, 1, 3),
    _AcpuEthernetPortVlanTxOctets_Type()
)
acpuEthernetPortVlanTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortVlanTxOctets.setStatus("current")
_AcpuEthernetPortVlanRxOctets_Type = Counter64
_AcpuEthernetPortVlanRxOctets_Object = MibTableColumn
acpuEthernetPortVlanRxOctets = _AcpuEthernetPortVlanRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6, 1, 4),
    _AcpuEthernetPortVlanRxOctets_Type()
)
acpuEthernetPortVlanRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuEthernetPortVlanRxOctets.setStatus("current")
_AcpuEthernetPortVlanRowStatus_Type = RowStatus
_AcpuEthernetPortVlanRowStatus_Object = MibTableColumn
acpuEthernetPortVlanRowStatus = _AcpuEthernetPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 1, 6, 1, 5),
    _AcpuEthernetPortVlanRowStatus_Type()
)
acpuEthernetPortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acpuEthernetPortVlanRowStatus.setStatus("current")
_EgcControl_ObjectIdentity = ObjectIdentity
egcControl = _EgcControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2)
)


class _EgcOperStatus_Type(Integer32):
    """Custom type egcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EgcOperStatus_Type.__name__ = "Integer32"
_EgcOperStatus_Object = MibScalar
egcOperStatus = _EgcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 1),
    _EgcOperStatus_Type()
)
egcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcOperStatus.setStatus("current")


class _EgcDeviceReset_Type(Integer32):
    """Custom type egcDeviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetdevice", 1)
    )


_EgcDeviceReset_Type.__name__ = "Integer32"
_EgcDeviceReset_Object = MibScalar
egcDeviceReset = _EgcDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 2),
    _EgcDeviceReset_Type()
)
egcDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egcDeviceReset.setStatus("current")
_EgcPortTable_Object = MibTable
egcPortTable = _EgcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    egcPortTable.setStatus("current")
_EgcPortEntry_Object = MibTableRow
egcPortEntry = _EgcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1)
)
egcPortEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "egcPortIndex"),
)
if mibBuilder.loadTexts:
    egcPortEntry.setStatus("current")


class _EgcPortIndex_Type(Integer32):
    """Custom type egcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EgcPortIndex_Type.__name__ = "Integer32"
_EgcPortIndex_Object = MibTableColumn
egcPortIndex = _EgcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 1),
    _EgcPortIndex_Type()
)
egcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortIndex.setStatus("current")


class _EgcPortDescr_Type(DisplayString):
    """Custom type egcPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgcPortDescr_Type.__name__ = "DisplayString"
_EgcPortDescr_Object = MibTableColumn
egcPortDescr = _EgcPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 2),
    _EgcPortDescr_Type()
)
egcPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortDescr.setStatus("current")


class _EgcPortDuplexity_Type(Integer32):
    """Custom type egcPortDuplexity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_EgcPortDuplexity_Type.__name__ = "Integer32"
_EgcPortDuplexity_Object = MibTableColumn
egcPortDuplexity = _EgcPortDuplexity_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 3),
    _EgcPortDuplexity_Type()
)
egcPortDuplexity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortDuplexity.setStatus("current")
_EgcPortLinkRate_Type = Counter64
_EgcPortLinkRate_Object = MibTableColumn
egcPortLinkRate = _EgcPortLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 4),
    _EgcPortLinkRate_Type()
)
egcPortLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortLinkRate.setStatus("current")


class _EgcPortAdminStatus_Type(Integer32):
    """Custom type egcPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_EgcPortAdminStatus_Type.__name__ = "Integer32"
_EgcPortAdminStatus_Object = MibTableColumn
egcPortAdminStatus = _EgcPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 5),
    _EgcPortAdminStatus_Type()
)
egcPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    egcPortAdminStatus.setStatus("current")


class _EgcPortOperStatus_Type(Integer32):
    """Custom type egcPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("degraded", 3))
    )


_EgcPortOperStatus_Type.__name__ = "Integer32"
_EgcPortOperStatus_Object = MibTableColumn
egcPortOperStatus = _EgcPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 6),
    _EgcPortOperStatus_Type()
)
egcPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortOperStatus.setStatus("current")
_EgcPortInOctets_Type = Counter64
_EgcPortInOctets_Object = MibTableColumn
egcPortInOctets = _EgcPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 7),
    _EgcPortInOctets_Type()
)
egcPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortInOctets.setStatus("current")
_EgcPortOutOctets_Type = Counter64
_EgcPortOutOctets_Object = MibTableColumn
egcPortOutOctets = _EgcPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 8),
    _EgcPortOutOctets_Type()
)
egcPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortOutOctets.setStatus("current")
_EgcPortRxCrcErrFrameCount_Type = Counter64
_EgcPortRxCrcErrFrameCount_Object = MibTableColumn
egcPortRxCrcErrFrameCount = _EgcPortRxCrcErrFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 3, 1, 9),
    _EgcPortRxCrcErrFrameCount_Type()
)
egcPortRxCrcErrFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortRxCrcErrFrameCount.setStatus("current")
_EgcVlanTable_Object = MibTable
egcVlanTable = _EgcVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    egcVlanTable.setStatus("current")
_EgcVlanEntry_Object = MibTableRow
egcVlanEntry = _EgcVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4, 1)
)
egcVlanEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "egcPortVlanID"),
)
if mibBuilder.loadTexts:
    egcVlanEntry.setStatus("current")


class _EgcPortVlanID_Type(Integer32):
    """Custom type egcPortVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EgcPortVlanID_Type.__name__ = "Integer32"
_EgcPortVlanID_Object = MibTableColumn
egcPortVlanID = _EgcPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4, 1, 1),
    _EgcPortVlanID_Type()
)
egcPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortVlanID.setStatus("current")


class _EgcVlanState_Type(Integer32):
    """Custom type egcVlanState based on Integer32"""
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


_EgcVlanState_Type.__name__ = "Integer32"
_EgcVlanState_Object = MibTableColumn
egcVlanState = _EgcVlanState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4, 1, 2),
    _EgcVlanState_Type()
)
egcVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcVlanState.setStatus("current")
_EgcVlanIpAddr_Type = IpAddress
_EgcVlanIpAddr_Object = MibTableColumn
egcVlanIpAddr = _EgcVlanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4, 1, 3),
    _EgcVlanIpAddr_Type()
)
egcVlanIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcVlanIpAddr.setStatus("current")
_EgcVlanNetMask_Type = IpAddress
_EgcVlanNetMask_Object = MibTableColumn
egcVlanNetMask = _EgcVlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4, 1, 4),
    _EgcVlanNetMask_Type()
)
egcVlanNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcVlanNetMask.setStatus("current")
_EgcVlanPorts_Type = PortList
_EgcVlanPorts_Object = MibTableColumn
egcVlanPorts = _EgcVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 4, 1, 5),
    _EgcVlanPorts_Type()
)
egcVlanPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    egcVlanPorts.setStatus("current")
_EgcPortVlanTable_Object = MibTable
egcPortVlanTable = _EgcPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    egcPortVlanTable.setStatus("current")
_EgcPortVlanEntry_Object = MibTableRow
egcPortVlanEntry = _EgcPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 5, 1)
)
egcPortVlanEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "egcPortIndex"),
    (0, "AIRCELL-ACPU-SNMP-MIB", "egcPortVlanID"),
)
if mibBuilder.loadTexts:
    egcPortVlanEntry.setStatus("current")
_EgcPortVlanTxOctets_Type = Counter64
_EgcPortVlanTxOctets_Object = MibTableColumn
egcPortVlanTxOctets = _EgcPortVlanTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 5, 1, 1),
    _EgcPortVlanTxOctets_Type()
)
egcPortVlanTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortVlanTxOctets.setStatus("current")
_EgcPortVlanRxOctets_Type = Counter64
_EgcPortVlanRxOctets_Object = MibTableColumn
egcPortVlanRxOctets = _EgcPortVlanRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 2, 5, 1, 2),
    _EgcPortVlanRxOctets_Type()
)
egcPortVlanRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egcPortVlanRxOctets.setStatus("current")
_AcpuNetworkInfo_ObjectIdentity = ObjectIdentity
acpuNetworkInfo = _AcpuNetworkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3)
)
_AcpuSimpleIp_Type = IpAddress
_AcpuSimpleIp_Object = MibScalar
acpuSimpleIp = _AcpuSimpleIp_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 1),
    _AcpuSimpleIp_Type()
)
acpuSimpleIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSimpleIp.setStatus("current")
_AcpuPrimaryDNSAddr_Type = IpAddress
_AcpuPrimaryDNSAddr_Object = MibScalar
acpuPrimaryDNSAddr = _AcpuPrimaryDNSAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 2),
    _AcpuPrimaryDNSAddr_Type()
)
acpuPrimaryDNSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuPrimaryDNSAddr.setStatus("current")
_AcpuSecondaryDNSAddr_Type = IpAddress
_AcpuSecondaryDNSAddr_Object = MibScalar
acpuSecondaryDNSAddr = _AcpuSecondaryDNSAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 3),
    _AcpuSecondaryDNSAddr_Type()
)
acpuSecondaryDNSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSecondaryDNSAddr.setStatus("current")
_AcpuWiFiAAASrvAddr_Type = IpAddress
_AcpuWiFiAAASrvAddr_Object = MibScalar
acpuWiFiAAASrvAddr = _AcpuWiFiAAASrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 4),
    _AcpuWiFiAAASrvAddr_Type()
)
acpuWiFiAAASrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuWiFiAAASrvAddr.setStatus("current")
_AcpuPriABSDataSrvAddr_Type = IpAddress
_AcpuPriABSDataSrvAddr_Object = MibScalar
acpuPriABSDataSrvAddr = _AcpuPriABSDataSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 5),
    _AcpuPriABSDataSrvAddr_Type()
)
acpuPriABSDataSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuPriABSDataSrvAddr.setStatus("current")
_AcpuSecABSDataSrvAddr_Type = IpAddress
_AcpuSecABSDataSrvAddr_Object = MibScalar
acpuSecABSDataSrvAddr = _AcpuSecABSDataSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 6),
    _AcpuSecABSDataSrvAddr_Type()
)
acpuSecABSDataSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSecABSDataSrvAddr.setStatus("current")
_AcpuNetCoolServerAddr_Type = IpAddress
_AcpuNetCoolServerAddr_Object = MibScalar
acpuNetCoolServerAddr = _AcpuNetCoolServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 7),
    _AcpuNetCoolServerAddr_Type()
)
acpuNetCoolServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuNetCoolServerAddr.setStatus("current")
_AcpuTIBCOPASSURAddr_Type = IpAddress
_AcpuTIBCOPASSURAddr_Object = MibScalar
acpuTIBCOPASSURAddr = _AcpuTIBCOPASSURAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 8),
    _AcpuTIBCOPASSURAddr_Type()
)
acpuTIBCOPASSURAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuTIBCOPASSURAddr.setStatus("obsolete")
_AcpuVOIPServerAddr_Type = IpAddress
_AcpuVOIPServerAddr_Object = MibScalar
acpuVOIPServerAddr = _AcpuVOIPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 3, 9),
    _AcpuVOIPServerAddr_Type()
)
acpuVOIPServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuVOIPServerAddr.setStatus("current")
_AcpuSnortInfo_ObjectIdentity = ObjectIdentity
acpuSnortInfo = _AcpuSnortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4)
)
_AcpuSnortSrcIp_Type = IpAddress
_AcpuSnortSrcIp_Object = MibScalar
acpuSnortSrcIp = _AcpuSnortSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 1),
    _AcpuSnortSrcIp_Type()
)
acpuSnortSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortSrcIp.setStatus("current")
_AcpuSnortDstIp_Type = IpAddress
_AcpuSnortDstIp_Object = MibScalar
acpuSnortDstIp = _AcpuSnortDstIp_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 2),
    _AcpuSnortDstIp_Type()
)
acpuSnortDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortDstIp.setStatus("current")


class _AcpuSnortSrcPort_Type(Integer32):
    """Custom type acpuSnortSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcpuSnortSrcPort_Type.__name__ = "Integer32"
_AcpuSnortSrcPort_Object = MibScalar
acpuSnortSrcPort = _AcpuSnortSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 3),
    _AcpuSnortSrcPort_Type()
)
acpuSnortSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortSrcPort.setStatus("current")


class _AcpuSnortDstPort_Type(Integer32):
    """Custom type acpuSnortDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcpuSnortDstPort_Type.__name__ = "Integer32"
_AcpuSnortDstPort_Object = MibScalar
acpuSnortDstPort = _AcpuSnortDstPort_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 4),
    _AcpuSnortDstPort_Type()
)
acpuSnortDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortDstPort.setStatus("current")
_AcpuSnortProtocol_Type = DisplayString
_AcpuSnortProtocol_Object = MibScalar
acpuSnortProtocol = _AcpuSnortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 5),
    _AcpuSnortProtocol_Type()
)
acpuSnortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortProtocol.setStatus("current")
_AcpuSnortTime_Type = DisplayString
_AcpuSnortTime_Object = MibScalar
acpuSnortTime = _AcpuSnortTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 6),
    _AcpuSnortTime_Type()
)
acpuSnortTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortTime.setStatus("current")
_AcpuSnortMessage_Type = DisplayString
_AcpuSnortMessage_Object = MibScalar
acpuSnortMessage = _AcpuSnortMessage_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 2, 4, 7),
    _AcpuSnortMessage_Type()
)
acpuSnortMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpuSnortMessage.setStatus("current")
_AircellAACU_ObjectIdentity = ObjectIdentity
aircellAACU = _AircellAACU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 3)
)
_AircellCHandset_ObjectIdentity = ObjectIdentity
aircellCHandset = _AircellCHandset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 4)
)
_AircellFDHandset_ObjectIdentity = ObjectIdentity
aircellFDHandset = _AircellFDHandset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 5)
)
_AircellGroup_ObjectIdentity = ObjectIdentity
aircellGroup = _AircellGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6)
)
_AircellVideoService_ObjectIdentity = ObjectIdentity
aircellVideoService = _AircellVideoService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7)
)
_AbsContentLoader_ObjectIdentity = ObjectIdentity
absContentLoader = _AbsContentLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1)
)


class _AbsAcpuCldOperStatus_Type(Integer32):
    """Custom type absAcpuCldOperStatus based on Integer32"""
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


_AbsAcpuCldOperStatus_Type.__name__ = "Integer32"
_AbsAcpuCldOperStatus_Object = MibScalar
absAcpuCldOperStatus = _AbsAcpuCldOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 1),
    _AbsAcpuCldOperStatus_Type()
)
absAcpuCldOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcpuCldOperStatus.setStatus("current")


class _AbsAcpuCldUsbAdminStatus_Type(Integer32):
    """Custom type absAcpuCldUsbAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_AbsAcpuCldUsbAdminStatus_Type.__name__ = "Integer32"
_AbsAcpuCldUsbAdminStatus_Object = MibScalar
absAcpuCldUsbAdminStatus = _AbsAcpuCldUsbAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 2),
    _AbsAcpuCldUsbAdminStatus_Type()
)
absAcpuCldUsbAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAcpuCldUsbAdminStatus.setStatus("current")
_AbsCldUsbTable_Object = MibTable
absCldUsbTable = _AbsCldUsbTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    absCldUsbTable.setStatus("current")
_AbsCldUsbEntry_Object = MibTableRow
absCldUsbEntry = _AbsCldUsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 3, 1)
)
absCldUsbEntry.setIndexNames(
    (0, "AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbSlotNumber"),
)
if mibBuilder.loadTexts:
    absCldUsbEntry.setStatus("current")


class _AbsAcpuCldUsbSlotNumber_Type(Integer32):
    """Custom type absAcpuCldUsbSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AbsAcpuCldUsbSlotNumber_Type.__name__ = "Integer32"
_AbsAcpuCldUsbSlotNumber_Object = MibTableColumn
absAcpuCldUsbSlotNumber = _AbsAcpuCldUsbSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 3, 1, 1),
    _AbsAcpuCldUsbSlotNumber_Type()
)
absAcpuCldUsbSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcpuCldUsbSlotNumber.setStatus("current")
_AbsAcpuCldUsbSerialNumber_Type = DisplayString
_AbsAcpuCldUsbSerialNumber_Object = MibTableColumn
absAcpuCldUsbSerialNumber = _AbsAcpuCldUsbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 3, 1, 2),
    _AbsAcpuCldUsbSerialNumber_Type()
)
absAcpuCldUsbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcpuCldUsbSerialNumber.setStatus("current")
_AbsAcpuCldUsbMountPath_Type = DisplayString
_AbsAcpuCldUsbMountPath_Object = MibTableColumn
absAcpuCldUsbMountPath = _AbsAcpuCldUsbMountPath_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 3, 1, 3),
    _AbsAcpuCldUsbMountPath_Type()
)
absAcpuCldUsbMountPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcpuCldUsbMountPath.setStatus("current")


class _AbsAcpuCldUsbStatus_Type(Integer32):
    """Custom type absAcpuCldUsbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("unknown", 3))
    )


_AbsAcpuCldUsbStatus_Type.__name__ = "Integer32"
_AbsAcpuCldUsbStatus_Object = MibTableColumn
absAcpuCldUsbStatus = _AbsAcpuCldUsbStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 1, 3, 1, 4),
    _AbsAcpuCldUsbStatus_Type()
)
absAcpuCldUsbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcpuCldUsbStatus.setStatus("current")
_AbsContentManager_ObjectIdentity = ObjectIdentity
absContentManager = _AbsContentManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 2)
)


class _AbsVSMOperStatus_Type(Integer32):
    """Custom type absVSMOperStatus based on Integer32"""
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


_AbsVSMOperStatus_Type.__name__ = "Integer32"
_AbsVSMOperStatus_Object = MibScalar
absVSMOperStatus = _AbsVSMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 2, 1),
    _AbsVSMOperStatus_Type()
)
absVSMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absVSMOperStatus.setStatus("current")


class _AbsVSMAdminStatus_Type(Integer32):
    """Custom type absVSMAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AbsVSMAdminStatus_Type.__name__ = "Integer32"
_AbsVSMAdminStatus_Object = MibScalar
absVSMAdminStatus = _AbsVSMAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 2, 2),
    _AbsVSMAdminStatus_Type()
)
absVSMAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absVSMAdminStatus.setStatus("current")


class _AbsCMOperStatus_Type(Integer32):
    """Custom type absCMOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AbsCMOperStatus_Type.__name__ = "Integer32"
_AbsCMOperStatus_Object = MibScalar
absCMOperStatus = _AbsCMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 2, 3),
    _AbsCMOperStatus_Type()
)
absCMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCMOperStatus.setStatus("current")
_AbsAcpuBatchVersion_Type = DisplayString
_AbsAcpuBatchVersion_Object = MibScalar
absAcpuBatchVersion = _AbsAcpuBatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 2, 4),
    _AbsAcpuBatchVersion_Type()
)
absAcpuBatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absAcpuBatchVersion.setStatus("current")
_AbsContentServer_ObjectIdentity = ObjectIdentity
absContentServer = _AbsContentServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3)
)


class _AbsFlushSquidCache_Type(Integer32):
    """Custom type absFlushSquidCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noFlushSquidCache", 0),
          ("flushSquidCache", 1))
    )


_AbsFlushSquidCache_Type.__name__ = "Integer32"
_AbsFlushSquidCache_Object = MibScalar
absFlushSquidCache = _AbsFlushSquidCache_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 1),
    _AbsFlushSquidCache_Type()
)
absFlushSquidCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absFlushSquidCache.setStatus("current")


class _AbsCSOperStatus_Type(Integer32):
    """Custom type absCSOperStatus based on Integer32"""
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


_AbsCSOperStatus_Type.__name__ = "Integer32"
_AbsCSOperStatus_Object = MibScalar
absCSOperStatus = _AbsCSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 2),
    _AbsCSOperStatus_Type()
)
absCSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCSOperStatus.setStatus("current")
_AbsActiveVideoClients_Type = Integer32
_AbsActiveVideoClients_Object = MibScalar
absActiveVideoClients = _AbsActiveVideoClients_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 3),
    _AbsActiveVideoClients_Type()
)
absActiveVideoClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absActiveVideoClients.setStatus("current")
_AbsActiveVideoDownloads_Type = Integer32
_AbsActiveVideoDownloads_Object = MibScalar
absActiveVideoDownloads = _AbsActiveVideoDownloads_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 4),
    _AbsActiveVideoDownloads_Type()
)
absActiveVideoDownloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absActiveVideoDownloads.setStatus("current")
_AbsCSTxBytes_Type = Integer32
_AbsCSTxBytes_Object = MibScalar
absCSTxBytes = _AbsCSTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 5),
    _AbsCSTxBytes_Type()
)
absCSTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCSTxBytes.setStatus("current")


class _AbsVideoServiceState_Type(Integer32):
    """Custom type absVideoServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AbsVideoServiceState_Type.__name__ = "Integer32"
_AbsVideoServiceState_Object = MibScalar
absVideoServiceState = _AbsVideoServiceState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 6),
    _AbsVideoServiceState_Type()
)
absVideoServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absVideoServiceState.setStatus("current")


class _AbsAcpuVQosOperStatus_Type(Integer32):
    """Custom type absAcpuVQosOperStatus based on Integer32"""
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


_AbsAcpuVQosOperStatus_Type.__name__ = "Integer32"
_AbsAcpuVQosOperStatus_Object = MibScalar
absAcpuVQosOperStatus = _AbsAcpuVQosOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 7),
    _AbsAcpuVQosOperStatus_Type()
)
absAcpuVQosOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAcpuVQosOperStatus.setStatus("current")


class _AbsAcpuVQosCsVcOperStatus_Type(Integer32):
    """Custom type absAcpuVQosCsVcOperStatus based on Integer32"""
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


_AbsAcpuVQosCsVcOperStatus_Type.__name__ = "Integer32"
_AbsAcpuVQosCsVcOperStatus_Object = MibScalar
absAcpuVQosCsVcOperStatus = _AbsAcpuVQosCsVcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 8),
    _AbsAcpuVQosCsVcOperStatus_Type()
)
absAcpuVQosCsVcOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAcpuVQosCsVcOperStatus.setStatus("current")


class _AbsAcpuVQosCsgHttpOperStatus_Type(Integer32):
    """Custom type absAcpuVQosCsgHttpOperStatus based on Integer32"""
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


_AbsAcpuVQosCsgHttpOperStatus_Type.__name__ = "Integer32"
_AbsAcpuVQosCsgHttpOperStatus_Object = MibScalar
absAcpuVQosCsgHttpOperStatus = _AbsAcpuVQosCsgHttpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 9),
    _AbsAcpuVQosCsgHttpOperStatus_Type()
)
absAcpuVQosCsgHttpOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAcpuVQosCsgHttpOperStatus.setStatus("current")


class _AbsAcpuVQosClCmOperStatus_Type(Integer32):
    """Custom type absAcpuVQosClCmOperStatus based on Integer32"""
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


_AbsAcpuVQosClCmOperStatus_Type.__name__ = "Integer32"
_AbsAcpuVQosClCmOperStatus_Object = MibScalar
absAcpuVQosClCmOperStatus = _AbsAcpuVQosClCmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 7, 3, 10),
    _AbsAcpuVQosClCmOperStatus_Type()
)
absAcpuVQosClCmOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAcpuVQosClCmOperStatus.setStatus("current")

# Managed Objects groups

snmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28382, 1, 6, 1)
)
snmpGroup.setObjects(
      *(("AIRCELL-ACPU-SNMP-MIB", "wapAdminStatus11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapAdminStatus11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapOperStatus11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapOperStatus11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapActiveWirelessClients11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapActiveWirelessClients11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioLinkRate11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioLinkRate11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioInPackets11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioInPackets11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioOutPackets11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioOutPackets11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioPortDuplexity11A"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapRadioPortDuplexity11B"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapPowerOpState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuDot11SsidVlanName"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuDot11SsidMbssidBroadcast"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuDot11VlanSecurityVlanName"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuDot11VlanSecurityWpaPsk"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuDot11VlanSecurityStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuDot11VlanSecurityRowStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "wapCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcDeviceReset"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortDescr"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortDuplexity"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortLinkRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortInOctets"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortOutOctets"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcVlanIpAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcVlanNetMask"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcVlanPorts"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcVlanState"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortVlanTxOctets"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortVlanRxOctets"),
        ("AIRCELL-ACPU-SNMP-MIB", "egcPortRxCrcErrFrameCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortLinkRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortDuplexity"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetVlanState"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetVlanIpAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetVlanNetMask"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetVlanPorts"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortVlanRxOctets"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortVlanTxOctets"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortRxCrcErrFrameCnt"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSimpleIp"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuPrimaryDNSAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSecondaryDNSAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "wiredHandsetAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSystemReset"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSystemMode"),
        ("AIRCELL-ACPU-SNMP-MIB", "absDisablePortal"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuLoggingLevels"),
        ("AIRCELL-ACPU-SNMP-MIB", "absCWAPLoggingLevels"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSoftwareApplyTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSoftwareBackoutTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSystemBlockATGAccess"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardRawLogging"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardSendRawLogs"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardRawLogStatemachine"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardEnableLogs"),
        ("AIRCELL-ACPU-SNMP-MIB", "absMediaLoaderPortAdminState"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardSectorID"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuFWLStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuIPSIDSStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuQosStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "wirelessHandsetAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "wirelessHandsetOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "wirelessHandsetRowStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "aacuAtgModemOpStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "aacuTerrModemOpStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "aacuAuxCardOperationalStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsHealthStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortVlanRowStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetVlanRowStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuEthernetPortState"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurHealthStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLatitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLongitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsAltitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsHorVelocity"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsVerVelocity"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsUTCTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLocalTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLocalZoneHourOffset"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsLocalZoneMinutesOffset"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpugpsNumOfGPSSat"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVOIPServerAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuNetCoolServerAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuTIBCOPASSURAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuAtgModemLinkStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuTerrModemLinkStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSecABSDataSrvAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuPriABSDataSrvAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuWiFiAAASrvAddr"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuAltitude"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVenturiTunnelModeAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVenturiClientStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuVenturiTunnelStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftTailNum"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircraftType"),
        ("AIRCELL-ACPU-SNMP-MIB", "airlineName"),
        ("AIRCELL-ACPU-SNMP-MIB", "wirelessHandsetCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "wiredHandsetOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "wiredHandsetRowStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "wiredHandsetCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSoftwareVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurFlightNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurDepartureUTCTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurDepartureLocalTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurArrivalUTCTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurArrivalLocalTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurEstimatedArrivalUTCTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurEstimatedArrivalLocalTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurDepartureCity"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurDepartureAirport"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurDestinationCity"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurDestinationAirport"),
        ("AIRCELL-ACPU-SNMP-MIB", "passurFlightRouteWayPoints"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAtgClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "absPeakFLRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAverageFLRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "absPeakRLRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAverageRLRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardRx0AGC"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardTxAGC"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardRx1AGC"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardSignalStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardPilotPN"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardPNOffset"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardPilotPNASP"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAircardPilotStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "absTotalActiveClientCount"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortSrcIp"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortDstIp"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortSrcPort"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortDstPort"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortProtocol"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortTime"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuSnortMessage"),
        ("AIRCELL-ACPU-SNMP-MIB", "absCompatibleBundle"),
        ("AIRCELL-ACPU-SNMP-MIB", "absActivationBundle"),
        ("AIRCELL-ACPU-SNMP-MIB", "activateABSBundle"),
        ("AIRCELL-ACPU-SNMP-MIB", "absBundleActivationStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absBundleDownloadStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absBundleDownloadAbortInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "absBundleActivationAbortInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbSlotNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbSerialNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbMountPath"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuCldUsbStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absVSMOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absVSMAdminStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absCMOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuBatchVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "absFlushSquidCache"),
        ("AIRCELL-ACPU-SNMP-MIB", "absCSOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absActiveVideoClients"),
        ("AIRCELL-ACPU-SNMP-MIB", "absActiveVideoDownloads"),
        ("AIRCELL-ACPU-SNMP-MIB", "absCSTxBytes"),
        ("AIRCELL-ACPU-SNMP-MIB", "absVideoServiceState"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuVQosOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuVQosCsVcOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuVQosCsgHttpOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absAcpuVQosClCmOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "absWhitelistVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "abpVersion"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircardInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "auxcardInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuBios"),
        ("AIRCELL-ACPU-SNMP-MIB", "aircardEsn"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpuHardwareSerialNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "aacuHardwareSerialNumber"),
        ("AIRCELL-ACPU-SNMP-MIB", "meruControllerInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "venturiInfo"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap1Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap2Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap3Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap4Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap5Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap6Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap7Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "cwap8Info"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpu429PitchAngle"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpu429RollAngle"),
        ("AIRCELL-ACPU-SNMP-MIB", "acpu429TrackAngle"),
        ("AIRCELL-ACPU-SNMP-MIB", "absArinc429Support"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSBBSignalStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "sbbPacketErrorRate"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSBBOperStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "absSBBLinkStatus"),
        ("AIRCELL-ACPU-SNMP-MIB", "satelliteSupport"),
        ("AIRCELL-ACPU-SNMP-MIB", "weightonWheelsSupport"),
        ("AIRCELL-ACPU-SNMP-MIB", "absKUSignalStrength"),
        ("AIRCELL-ACPU-SNMP-MIB", "absKULinkStatus"))
)
if mibBuilder.loadTexts:
    snmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRCELL-ACPU-SNMP-MIB",
    **{"PortList": PortList,
       "aircellLLC": aircellLLC,
       "aircellABS": aircellABS,
       "aircellABSConfig": aircellABSConfig,
       "absControlConfig": absControlConfig,
       "wiredHandsetTable": wiredHandsetTable,
       "wiredHandsetEntry": wiredHandsetEntry,
       "wiredHandsetIndex": wiredHandsetIndex,
       "wiredHandsetAdminStatus": wiredHandsetAdminStatus,
       "wiredHandsetOperStatus": wiredHandsetOperStatus,
       "wiredHandsetRowStatus": wiredHandsetRowStatus,
       "absSystemReset": absSystemReset,
       "absSystemMode": absSystemMode,
       "absSoftwareApplyTime": absSoftwareApplyTime,
       "absSoftwareBackoutTime": absSoftwareBackoutTime,
       "absDisablePortal": absDisablePortal,
       "absSystemBlockATGAccess": absSystemBlockATGAccess,
       "absAcpuLoggingLevels": absAcpuLoggingLevels,
       "absCWAPLoggingLevels": absCWAPLoggingLevels,
       "absAircardRawLogging": absAircardRawLogging,
       "absAircardSendRawLogs": absAircardSendRawLogs,
       "absAircardRawLogStatemachine": absAircardRawLogStatemachine,
       "absAircardEnableLogs": absAircardEnableLogs,
       "absMediaLoaderPortAdminState": absMediaLoaderPortAdminState,
       "acpuFWLStatus": acpuFWLStatus,
       "acpuIPSIDSStatus": acpuIPSIDSStatus,
       "wirelessHandsetTable": wirelessHandsetTable,
       "wirelessHandsetEntry": wirelessHandsetEntry,
       "wirelessHandsetIndex": wirelessHandsetIndex,
       "wirelessHandsetAdminStatus": wirelessHandsetAdminStatus,
       "wirelessHandsetOperStatus": wirelessHandsetOperStatus,
       "wirelessHandsetRowStatus": wirelessHandsetRowStatus,
       "wapTable": wapTable,
       "wapEntry": wapEntry,
       "wapIndex": wapIndex,
       "wapAdminStatus11A": wapAdminStatus11A,
       "wapAdminStatus11B": wapAdminStatus11B,
       "wapOperStatus11A": wapOperStatus11A,
       "wapOperStatus11B": wapOperStatus11B,
       "wapActiveWirelessClients11A": wapActiveWirelessClients11A,
       "wapActiveWirelessClients11B": wapActiveWirelessClients11B,
       "wapRadioLinkRate11A": wapRadioLinkRate11A,
       "wapRadioLinkRate11B": wapRadioLinkRate11B,
       "wapRadioInPackets11A": wapRadioInPackets11A,
       "wapRadioInPackets11B": wapRadioInPackets11B,
       "wapRadioOutPackets11A": wapRadioOutPackets11A,
       "wapRadioOutPackets11B": wapRadioOutPackets11B,
       "wapRadioPortDuplexity11A": wapRadioPortDuplexity11A,
       "wapRadioPortDuplexity11B": wapRadioPortDuplexity11B,
       "wapPowerOpState": wapPowerOpState,
       "acpuQosStatus": acpuQosStatus,
       "acpuDot11SsidTable": acpuDot11SsidTable,
       "acpuDot11SsidEntry": acpuDot11SsidEntry,
       "acpuDot11SsidIndex": acpuDot11SsidIndex,
       "acpuDot11SsidVlanName": acpuDot11SsidVlanName,
       "acpuDot11SsidMbssidBroadcast": acpuDot11SsidMbssidBroadcast,
       "acpuDot11VlanSecurityTable": acpuDot11VlanSecurityTable,
       "acpuDot11VlanSecurityEntry": acpuDot11VlanSecurityEntry,
       "acpuDot11VlanSecurityVlanId": acpuDot11VlanSecurityVlanId,
       "acpuDot11VlanSecurityVlanName": acpuDot11VlanSecurityVlanName,
       "acpuDot11VlanSecurityWpaPsk": acpuDot11VlanSecurityWpaPsk,
       "acpuDot11VlanSecurityStatus": acpuDot11VlanSecurityStatus,
       "acpuDot11VlanSecurityRowStatus": acpuDot11VlanSecurityRowStatus,
       "absSystemInfo": absSystemInfo,
       "absOperationalStatus": absOperationalStatus,
       "acpuOperationalStatus": acpuOperationalStatus,
       "aacuAtgModemOpStatus": aacuAtgModemOpStatus,
       "acpuAtgModemLinkStatus": acpuAtgModemLinkStatus,
       "aacuTerrModemOpStatus": aacuTerrModemOpStatus,
       "acpuTerrModemLinkStatus": acpuTerrModemLinkStatus,
       "aacuAuxCardOperationalStatus": aacuAuxCardOperationalStatus,
       "acpugpsHealthStatus": acpugpsHealthStatus,
       "passurHealthStatus": passurHealthStatus,
       "acpuAltitude": acpuAltitude,
       "cwapType": cwapType,
       "meruControllerOperationalStatus": meruControllerOperationalStatus,
       "acpuVenturiTunnelModeAdminStatus": acpuVenturiTunnelModeAdminStatus,
       "acpuVenturiClientStatus": acpuVenturiClientStatus,
       "acpuVenturiTunnelStatus": acpuVenturiTunnelStatus,
       "acpu429HealthStatus": acpu429HealthStatus,
       "absControlData": absControlData,
       "absPositionData": absPositionData,
       "acpugpsLatitude": acpugpsLatitude,
       "acpugpsLongitude": acpugpsLongitude,
       "acpugpsAltitude": acpugpsAltitude,
       "acpugpsHorVelocity": acpugpsHorVelocity,
       "acpugpsVerVelocity": acpugpsVerVelocity,
       "acpugpsUTCTime": acpugpsUTCTime,
       "acpugpsLocalTime": acpugpsLocalTime,
       "acpugpsLocalZoneHourOffset": acpugpsLocalZoneHourOffset,
       "acpugpsLocalZoneMinutesOffset": acpugpsLocalZoneMinutesOffset,
       "acpugpsNumOfGPSSat": acpugpsNumOfGPSSat,
       "acpu429PitchAngle": acpu429PitchAngle,
       "acpu429RollAngle": acpu429RollAngle,
       "acpu429TrackAngle": acpu429TrackAngle,
       "absFlightInfo": absFlightInfo,
       "passurFlightNumber": passurFlightNumber,
       "passurDepartureUTCTime": passurDepartureUTCTime,
       "passurDepartureLocalTime": passurDepartureLocalTime,
       "passurArrivalUTCTime": passurArrivalUTCTime,
       "passurArrivalLocalTime": passurArrivalLocalTime,
       "passurEstimatedArrivalUTCTime": passurEstimatedArrivalUTCTime,
       "passurEstimatedArrivalLocalTime": passurEstimatedArrivalLocalTime,
       "passurDepartureCity": passurDepartureCity,
       "passurDepartureAirport": passurDepartureAirport,
       "passurDestinationCity": passurDestinationCity,
       "passurDestinationAirport": passurDestinationAirport,
       "passurFlightRouteWayPoints": passurFlightRouteWayPoints,
       "absTotalClientCount": absTotalClientCount,
       "absAtgClientCount": absAtgClientCount,
       "absAircardSectorID": absAircardSectorID,
       "absPeakFLRate": absPeakFLRate,
       "absAverageFLRate": absAverageFLRate,
       "absPeakRLRate": absPeakRLRate,
       "absAverageRLRate": absAverageRLRate,
       "absAircardRx0AGC": absAircardRx0AGC,
       "absAircardTxAGC": absAircardTxAGC,
       "absAircardRx1AGC": absAircardRx1AGC,
       "absAircardSignalStrength": absAircardSignalStrength,
       "absAircardPilotPN": absAircardPilotPN,
       "absAircardPNOffset": absAircardPNOffset,
       "absAircardPilotPNASP": absAircardPilotPNASP,
       "absAircardPilotStrength": absAircardPilotStrength,
       "absTotalActiveClientCount": absTotalActiveClientCount,
       "absKUSignalStrength": absKUSignalStrength,
       "absAcmuOperStatus": absAcmuOperStatus,
       "absKULinkStatus": absKULinkStatus,
       "absOvtTunnelStatus": absOvtTunnelStatus,
       "absSBBOperStatus": absSBBOperStatus,
       "absSBBLinkStatus": absSBBLinkStatus,
       "absSBBSignalStrength": absSBBSignalStrength,
       "sbbPacketErrorRate": sbbPacketErrorRate,
       "absAircraftIdData": absAircraftIdData,
       "aircraftTailNum": aircraftTailNum,
       "aircraftType": aircraftType,
       "airlineName": airlineName,
       "wapCount": wapCount,
       "wirelessHandsetCount": wirelessHandsetCount,
       "wiredHandsetCount": wiredHandsetCount,
       "absSoftwareVersion": absSoftwareVersion,
       "absArinc429Support": absArinc429Support,
       "absLRUDetails": absLRUDetails,
       "acpuInfo": acpuInfo,
       "absWhitelistVersion": absWhitelistVersion,
       "abpVersion": abpVersion,
       "aircardInfo": aircardInfo,
       "auxcardInfo": auxcardInfo,
       "acpuBios": acpuBios,
       "aircardEsn": aircardEsn,
       "acpuHardwareSerialNumber": acpuHardwareSerialNumber,
       "aacuHardwareSerialNumber": aacuHardwareSerialNumber,
       "meruControllerInfo": meruControllerInfo,
       "venturiInfo": venturiInfo,
       "cwap1Info": cwap1Info,
       "cwap2Info": cwap2Info,
       "cwap3Info": cwap3Info,
       "cwap4Info": cwap4Info,
       "cwap5Info": cwap5Info,
       "cwap6Info": cwap6Info,
       "cwap7Info": cwap7Info,
       "cwap8Info": cwap8Info,
       "satelliteSupport": satelliteSupport,
       "weightonWheelsSupport": weightonWheelsSupport,
       "absSoftwareConfig": absSoftwareConfig,
       "absBundleConfig": absBundleConfig,
       "absCompatibleBundle": absCompatibleBundle,
       "absActivationBundle": absActivationBundle,
       "activateABSBundle": activateABSBundle,
       "absBundleDownloadStatus": absBundleDownloadStatus,
       "absBundleDownloadAbortInfo": absBundleDownloadAbortInfo,
       "absBundleActivationStatus": absBundleActivationStatus,
       "absBundleActivationAbortInfo": absBundleActivationAbortInfo,
       "aircellACPU": aircellACPU,
       "acpuEthernetPort": acpuEthernetPort,
       "acpuEthernetPortState": acpuEthernetPortState,
       "acpuEthernetPortLinkRate": acpuEthernetPortLinkRate,
       "acpuEthernetPortDuplexity": acpuEthernetPortDuplexity,
       "acpuEthernetPortRxCrcErrFrameCnt": acpuEthernetPortRxCrcErrFrameCnt,
       "acpuEthernetVlanTable": acpuEthernetVlanTable,
       "acpuEthernetVlanEntry": acpuEthernetVlanEntry,
       "acpuEthernetVlanID": acpuEthernetVlanID,
       "acpuEthernetVlanState": acpuEthernetVlanState,
       "acpuEthernetVlanIpAddr": acpuEthernetVlanIpAddr,
       "acpuEthernetVlanNetMask": acpuEthernetVlanNetMask,
       "acpuEthernetVlanPorts": acpuEthernetVlanPorts,
       "acpuEthernetVlanRowStatus": acpuEthernetVlanRowStatus,
       "acpuEthernetPortVlanTable": acpuEthernetPortVlanTable,
       "acpuEthernetPortVlanEntry": acpuEthernetPortVlanEntry,
       "acpuEthernetPortIndex": acpuEthernetPortIndex,
       "acpuEthernetPortVlanID": acpuEthernetPortVlanID,
       "acpuEthernetPortVlanTxOctets": acpuEthernetPortVlanTxOctets,
       "acpuEthernetPortVlanRxOctets": acpuEthernetPortVlanRxOctets,
       "acpuEthernetPortVlanRowStatus": acpuEthernetPortVlanRowStatus,
       "egcControl": egcControl,
       "egcOperStatus": egcOperStatus,
       "egcDeviceReset": egcDeviceReset,
       "egcPortTable": egcPortTable,
       "egcPortEntry": egcPortEntry,
       "egcPortIndex": egcPortIndex,
       "egcPortDescr": egcPortDescr,
       "egcPortDuplexity": egcPortDuplexity,
       "egcPortLinkRate": egcPortLinkRate,
       "egcPortAdminStatus": egcPortAdminStatus,
       "egcPortOperStatus": egcPortOperStatus,
       "egcPortInOctets": egcPortInOctets,
       "egcPortOutOctets": egcPortOutOctets,
       "egcPortRxCrcErrFrameCount": egcPortRxCrcErrFrameCount,
       "egcVlanTable": egcVlanTable,
       "egcVlanEntry": egcVlanEntry,
       "egcPortVlanID": egcPortVlanID,
       "egcVlanState": egcVlanState,
       "egcVlanIpAddr": egcVlanIpAddr,
       "egcVlanNetMask": egcVlanNetMask,
       "egcVlanPorts": egcVlanPorts,
       "egcPortVlanTable": egcPortVlanTable,
       "egcPortVlanEntry": egcPortVlanEntry,
       "egcPortVlanTxOctets": egcPortVlanTxOctets,
       "egcPortVlanRxOctets": egcPortVlanRxOctets,
       "acpuNetworkInfo": acpuNetworkInfo,
       "acpuSimpleIp": acpuSimpleIp,
       "acpuPrimaryDNSAddr": acpuPrimaryDNSAddr,
       "acpuSecondaryDNSAddr": acpuSecondaryDNSAddr,
       "acpuWiFiAAASrvAddr": acpuWiFiAAASrvAddr,
       "acpuPriABSDataSrvAddr": acpuPriABSDataSrvAddr,
       "acpuSecABSDataSrvAddr": acpuSecABSDataSrvAddr,
       "acpuNetCoolServerAddr": acpuNetCoolServerAddr,
       "acpuTIBCOPASSURAddr": acpuTIBCOPASSURAddr,
       "acpuVOIPServerAddr": acpuVOIPServerAddr,
       "acpuSnortInfo": acpuSnortInfo,
       "acpuSnortSrcIp": acpuSnortSrcIp,
       "acpuSnortDstIp": acpuSnortDstIp,
       "acpuSnortSrcPort": acpuSnortSrcPort,
       "acpuSnortDstPort": acpuSnortDstPort,
       "acpuSnortProtocol": acpuSnortProtocol,
       "acpuSnortTime": acpuSnortTime,
       "acpuSnortMessage": acpuSnortMessage,
       "aircellAACU": aircellAACU,
       "aircellCHandset": aircellCHandset,
       "aircellFDHandset": aircellFDHandset,
       "aircellGroup": aircellGroup,
       "snmpGroup": snmpGroup,
       "aircellVideoService": aircellVideoService,
       "absContentLoader": absContentLoader,
       "absAcpuCldOperStatus": absAcpuCldOperStatus,
       "absAcpuCldUsbAdminStatus": absAcpuCldUsbAdminStatus,
       "absCldUsbTable": absCldUsbTable,
       "absCldUsbEntry": absCldUsbEntry,
       "absAcpuCldUsbSlotNumber": absAcpuCldUsbSlotNumber,
       "absAcpuCldUsbSerialNumber": absAcpuCldUsbSerialNumber,
       "absAcpuCldUsbMountPath": absAcpuCldUsbMountPath,
       "absAcpuCldUsbStatus": absAcpuCldUsbStatus,
       "absContentManager": absContentManager,
       "absVSMOperStatus": absVSMOperStatus,
       "absVSMAdminStatus": absVSMAdminStatus,
       "absCMOperStatus": absCMOperStatus,
       "absAcpuBatchVersion": absAcpuBatchVersion,
       "absContentServer": absContentServer,
       "absFlushSquidCache": absFlushSquidCache,
       "absCSOperStatus": absCSOperStatus,
       "absActiveVideoClients": absActiveVideoClients,
       "absActiveVideoDownloads": absActiveVideoDownloads,
       "absCSTxBytes": absCSTxBytes,
       "absVideoServiceState": absVideoServiceState,
       "absAcpuVQosOperStatus": absAcpuVQosOperStatus,
       "absAcpuVQosCsVcOperStatus": absAcpuVQosCsVcOperStatus,
       "absAcpuVQosCsgHttpOperStatus": absAcpuVQosCsgHttpOperStatus,
       "absAcpuVQosClCmOperStatus": absAcpuVQosClCmOperStatus}
)
