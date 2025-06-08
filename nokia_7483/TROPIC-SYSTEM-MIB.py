# SNMP MIB module (TROPIC-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TnSwitchID,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TnSwitchID")

(tnSystemMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSystemMIB",
    "tnSystemModules")

(tnNetIfIndex,) = mibBuilder.importSymbols(
    "TROPIC-L1SERVICE-MIB",
    "tnNetIfIndex")

(AluWdmCardCapacity,
 AluWdmEnabledDisabled,
 AluWdmTransferProtocol,
 TnCommand,
 TropicResetType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmCardCapacity",
    "AluWdmEnabledDisabled",
    "AluWdmTransferProtocol",
    "TnCommand",
    "TropicResetType")


# MODULE-IDENTITY

tnSystemMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSystemMibModule.setRevisions(
        ("2008-02-16 12:00",
         "2008-04-05 12:00",
         "2008-05-29 12:00",
         "2008-10-10 12:00",
         "2008-10-14 12:00",
         "2009-02-27 12:00",
         "2009-03-03 12:00",
         "2009-04-07 12:00",
         "2009-04-07 12:00",
         "2009-04-28 12:00",
         "2009-04-30 12:00",
         "2009-05-05 12:00",
         "2009-07-22 12:00",
         "2010-01-07 12:00",
         "2010-01-11 12:00",
         "2010-06-22 12:00",
         "2010-10-18 12:00",
         "2010-11-11 12:00",
         "2011-03-15 12:00",
         "2011-03-17 12:00",
         "2011-03-28 12:00",
         "2011-04-25 12:00",
         "2011-05-23 12:00",
         "2011-06-03 12:00",
         "2011-06-21 12:00",
         "2011-08-12 12:00",
         "2011-09-30 12:00",
         "2011-10-24 12:00",
         "2012-01-12 12:00",
         "2012-02-16 12:00",
         "2012-05-18 12:00",
         "2013-01-16 12:00",
         "2013-01-20 12:00",
         "2013-01-31 12:00",
         "2013-03-06 12:00",
         "2013-03-20 12:00",
         "2012-04-17 12:00",
         "2013-04-19 12:00",
         "2013-11-20 12:00",
         "2014-02-26 12:00",
         "2014-03-04 12:00",
         "2014-03-30 12:00",
         "2014-04-23 12:00",
         "2015-02-20 12:00",
         "2015-07-13 12:00",
         "2015-07-12 12:00",
         "2015-09-16 12:00",
         "2015-09-30 12:00",
         "2015-11-17 12:00",
         "2015-12-03 12:00",
         "2015-12-10 12:00",
         "2015-12-17 12:00",
         "2016-01-27 12:00",
         "2016-02-01 12:00",
         "2016-02-26 12:00",
         "2016-03-02 12:00",
         "2016-03-04 12:00",
         "2016-03-30 12:00",
         "2016-04-01 12:00",
         "2016-06-15 12:00",
         "2016-06-23 12:00",
         "2016-07-25 12:00",
         "2016-07-29 12:00",
         "2016-09-09 12:00",
         "2016-09-09 12:00",
         "2016-09-27 12:00",
         "2016-10-20 12:00",
         "2016-11-07 12:00",
         "2016-11-16 12:00",
         "2016-11-18 12:00",
         "2016-11-22 12:00",
         "2016-11-28 12:00",
         "2016-11-29 12:00",
         "2016-12-05 12:00",
         "2016-12-21 12:00",
         "2016-12-28 12:00",
         "2017-01-13 12:00",
         "2017-01-20 12:00",
         "2017-01-27 12:00",
         "2017-02-03 12:00",
         "2017-02-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicSysTimingReferenceQuality(TextualConvention, Integer32):
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("prs", 2),
          ("stu", 3),
          ("st2", 4),
          ("tnc", 5),
          ("st3e", 6),
          ("st3", 7),
          ("smc", 8),
          ("st4", 9),
          ("dus", 10),
          ("prc", 11),
          ("ssua", 12),
          ("ssub", 13),
          ("sec", 14),
          ("dnu", 15))
    )



class TropicSysTimingReferenceTimingMode(TextualConvention, Integer32):
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
          ("external", 2),
          ("line", 3),
          ("through", 4),
          ("loop", 5),
          ("local", 6))
    )



class AluWdmSslOperationStatus(TextualConvention, Integer32):
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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("none", 4))
    )



class AluWdmTransferStatus(TextualConvention, Integer32):
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
        *(("none", 1),
          ("completed", 2),
          ("inProgress", 3),
          ("failure", 4),
          ("failTimeout", 5))
    )



class AluWdmOcsLinkStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("notConnected", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnSystemConf_ObjectIdentity = ObjectIdentity
tnSystemConf = _TnSystemConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1)
)
_TnSystemGroups_ObjectIdentity = ObjectIdentity
tnSystemGroups = _TnSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1)
)
_TnSystemCompliances_ObjectIdentity = ObjectIdentity
tnSystemCompliances = _TnSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 2)
)
_TnSystemObjs_ObjectIdentity = ObjectIdentity
tnSystemObjs = _TnSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2)
)
_TnSysBasics_ObjectIdentity = ObjectIdentity
tnSysBasics = _TnSysBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1)
)


class _TnSysDescr_Type(SnmpAdminString):
    """Custom type tnSysDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysDescr_Type.__name__ = "SnmpAdminString"
_TnSysDescr_Object = MibScalar
tnSysDescr = _TnSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 1),
    _TnSysDescr_Type()
)
tnSysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDescr.setStatus("current")


class _TnSysTelnetPort_Type(Unsigned32):
    """Custom type tnSysTelnetPort based on Unsigned32"""
    defaultValue = 23

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysTelnetPort_Type.__name__ = "Unsigned32"
_TnSysTelnetPort_Object = MibScalar
tnSysTelnetPort = _TnSysTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 2),
    _TnSysTelnetPort_Type()
)
tnSysTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTelnetPort.setStatus("current")


class _TnSysHttpPort_Type(Unsigned32):
    """Custom type tnSysHttpPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSysHttpPort_Type.__name__ = "Unsigned32"
_TnSysHttpPort_Object = MibScalar
tnSysHttpPort = _TnSysHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 3),
    _TnSysHttpPort_Type()
)
tnSysHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysHttpPort.setStatus("current")
_TnSysDateAndTime_Type = DateAndTime
_TnSysDateAndTime_Object = MibScalar
tnSysDateAndTime = _TnSysDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 4),
    _TnSysDateAndTime_Type()
)
tnSysDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDateAndTime.setStatus("current")


class _TnSysReset_Type(TropicResetType):
    """Custom type tnSysReset based on TropicResetType"""
    defaultValue = 1


_TnSysReset_Type.__name__ = "TropicResetType"
_TnSysReset_Object = MibScalar
tnSysReset = _TnSysReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 5),
    _TnSysReset_Type()
)
tnSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysReset.setStatus("current")


class _TnSysMIBVersion_Type(SnmpAdminString):
    """Custom type tnSysMIBVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysMIBVersion_Type.__name__ = "SnmpAdminString"
_TnSysMIBVersion_Object = MibScalar
tnSysMIBVersion = _TnSysMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 6),
    _TnSysMIBVersion_Type()
)
tnSysMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysMIBVersion.setStatus("current")


class _TnSysRingID_Type(Unsigned32):
    """Custom type tnSysRingID based on Unsigned32"""
    defaultValue = 0


_TnSysRingID_Type.__name__ = "Unsigned32"
_TnSysRingID_Object = MibScalar
tnSysRingID = _TnSysRingID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 7),
    _TnSysRingID_Type()
)
tnSysRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRingID.setStatus("current")


class _TnSysNetworkElementID_Type(Unsigned32):
    """Custom type tnSysNetworkElementID based on Unsigned32"""
    defaultValue = 0


_TnSysNetworkElementID_Type.__name__ = "Unsigned32"
_TnSysNetworkElementID_Object = MibScalar
tnSysNetworkElementID = _TnSysNetworkElementID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 8),
    _TnSysNetworkElementID_Type()
)
tnSysNetworkElementID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNetworkElementID.setStatus("current")


class _TnSysAINSDebounceTime_Type(Unsigned32):
    """Custom type tnSysAINSDebounceTime based on Unsigned32"""
    defaultValue = 600


_TnSysAINSDebounceTime_Type.__name__ = "Unsigned32"
_TnSysAINSDebounceTime_Object = MibScalar
tnSysAINSDebounceTime = _TnSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 9),
    _TnSysAINSDebounceTime_Type()
)
tnSysAINSDebounceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysAINSDebounceTime.setUnits("seconds")


class _TnSysSonetSdhMode_Type(Integer32):
    """Custom type tnSysSonetSdhMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2))
    )


_TnSysSonetSdhMode_Type.__name__ = "Integer32"
_TnSysSonetSdhMode_Object = MibScalar
tnSysSonetSdhMode = _TnSysSonetSdhMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 10),
    _TnSysSonetSdhMode_Type()
)
tnSysSonetSdhMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSonetSdhMode.setStatus("current")


class _TnSysAlarmReportingControl_Type(Integer32):
    """Custom type tnSysAlarmReportingControl based on Integer32"""
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
        *(("unknown", 1),
          ("released", 2),
          ("indefiniteInhibition", 3))
    )


_TnSysAlarmReportingControl_Type.__name__ = "Integer32"
_TnSysAlarmReportingControl_Object = MibScalar
tnSysAlarmReportingControl = _TnSysAlarmReportingControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 11),
    _TnSysAlarmReportingControl_Type()
)
tnSysAlarmReportingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAlarmReportingControl.setStatus("current")


class _TnSysWavelengthTrackerWaveKeySpace_Type(Unsigned32):
    """Custom type tnSysWavelengthTrackerWaveKeySpace based on Unsigned32"""
    defaultValue = 0


_TnSysWavelengthTrackerWaveKeySpace_Type.__name__ = "Unsigned32"
_TnSysWavelengthTrackerWaveKeySpace_Object = MibScalar
tnSysWavelengthTrackerWaveKeySpace = _TnSysWavelengthTrackerWaveKeySpace_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 12),
    _TnSysWavelengthTrackerWaveKeySpace_Type()
)
tnSysWavelengthTrackerWaveKeySpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysWavelengthTrackerWaveKeySpace.setStatus("current")


class _TnSysSecureMode_Type(Integer32):
    """Custom type tnSysSecureMode based on Integer32"""
    defaultValue = 2

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
        *(("unknown", 1),
          ("nonSecure", 2),
          ("secure", 3),
          ("fips", 4),
          ("anssi", 5))
    )


_TnSysSecureMode_Type.__name__ = "Integer32"
_TnSysSecureMode_Object = MibScalar
tnSysSecureMode = _TnSysSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 13),
    _TnSysSecureMode_Type()
)
tnSysSecureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSecureMode.setStatus("current")


class _TnSysExtendedTemperatureRange_Type(TruthValue):
    """Custom type tnSysExtendedTemperatureRange based on TruthValue"""
    defaultValue = 1


_TnSysExtendedTemperatureRange_Type.__name__ = "TruthValue"
_TnSysExtendedTemperatureRange_Object = MibScalar
tnSysExtendedTemperatureRange = _TnSysExtendedTemperatureRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 16),
    _TnSysExtendedTemperatureRange_Type()
)
tnSysExtendedTemperatureRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysExtendedTemperatureRange.setStatus("current")


class _TnSysTemperatureInCelsius_Type(TruthValue):
    """Custom type tnSysTemperatureInCelsius based on TruthValue"""
    defaultValue = 1


_TnSysTemperatureInCelsius_Type.__name__ = "TruthValue"
_TnSysTemperatureInCelsius_Object = MibScalar
tnSysTemperatureInCelsius = _TnSysTemperatureInCelsius_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 17),
    _TnSysTemperatureInCelsius_Type()
)
tnSysTemperatureInCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTemperatureInCelsius.setStatus("current")


class _TnSysName_Type(SnmpAdminString):
    """Custom type tnSysName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysName_Type.__name__ = "SnmpAdminString"
_TnSysName_Object = MibScalar
tnSysName = _TnSysName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 18),
    _TnSysName_Type()
)
tnSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysName.setStatus("current")


class _TnSysEquipmentControllerCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysEquipmentControllerCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysEquipmentControllerCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysEquipmentControllerCapacity_Object = MibScalar
tnSysEquipmentControllerCapacity = _TnSysEquipmentControllerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 19),
    _TnSysEquipmentControllerCapacity_Type()
)
tnSysEquipmentControllerCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysEquipmentControllerCapacity.setStatus("current")


class _TnSysFirstLevelControllerCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysFirstLevelControllerCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysFirstLevelControllerCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysFirstLevelControllerCapacity_Object = MibScalar
tnSysFirstLevelControllerCapacity = _TnSysFirstLevelControllerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 20),
    _TnSysFirstLevelControllerCapacity_Type()
)
tnSysFirstLevelControllerCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFirstLevelControllerCapacity.setStatus("current")


class _TnSysMatrix0CompactCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysMatrix0CompactCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysMatrix0CompactCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysMatrix0CompactCapacity_Object = MibScalar
tnSysMatrix0CompactCapacity = _TnSysMatrix0CompactCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 21),
    _TnSysMatrix0CompactCapacity_Type()
)
tnSysMatrix0CompactCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysMatrix0CompactCapacity.setStatus("current")


class _TnSysUniversalMatrixFirstLevelControllerCapacity_Type(AluWdmCardCapacity):
    """Custom type tnSysUniversalMatrixFirstLevelControllerCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnSysUniversalMatrixFirstLevelControllerCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnSysUniversalMatrixFirstLevelControllerCapacity_Object = MibScalar
tnSysUniversalMatrixFirstLevelControllerCapacity = _TnSysUniversalMatrixFirstLevelControllerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 22),
    _TnSysUniversalMatrixFirstLevelControllerCapacity_Type()
)
tnSysUniversalMatrixFirstLevelControllerCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysUniversalMatrixFirstLevelControllerCapacity.setStatus("current")


class _TnSysTimeOffsetTimeZone_Type(SnmpAdminString):
    """Custom type tnSysTimeOffsetTimeZone based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysTimeOffsetTimeZone_Type.__name__ = "SnmpAdminString"
_TnSysTimeOffsetTimeZone_Object = MibScalar
tnSysTimeOffsetTimeZone = _TnSysTimeOffsetTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 23),
    _TnSysTimeOffsetTimeZone_Type()
)
tnSysTimeOffsetTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimeOffsetTimeZone.setStatus("current")
_TnSysSwitchId_Type = TnSwitchID
_TnSysSwitchId_Object = MibScalar
tnSysSwitchId = _TnSysSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 26),
    _TnSysSwitchId_Type()
)
tnSysSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysSwitchId.setStatus("current")


class _TnSysFipsSquelchMode_Type(Integer32):
    """Custom type tnSysFipsSquelchMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonFips", 1),
          ("fips", 2))
    )


_TnSysFipsSquelchMode_Type.__name__ = "Integer32"
_TnSysFipsSquelchMode_Object = MibScalar
tnSysFipsSquelchMode = _TnSysFipsSquelchMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 27),
    _TnSysFipsSquelchMode_Type()
)
tnSysFipsSquelchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFipsSquelchMode.setStatus("current")


class _TnSysOtdrListOfFileNames_Type(SnmpAdminString):
    """Custom type tnSysOtdrListOfFileNames based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2047),
    )


_TnSysOtdrListOfFileNames_Type.__name__ = "SnmpAdminString"
_TnSysOtdrListOfFileNames_Object = MibScalar
tnSysOtdrListOfFileNames = _TnSysOtdrListOfFileNames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 28),
    _TnSysOtdrListOfFileNames_Type()
)
tnSysOtdrListOfFileNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrListOfFileNames.setStatus("current")
_TnSysOtdrFileCounts_Type = Unsigned32
_TnSysOtdrFileCounts_Object = MibScalar
tnSysOtdrFileCounts = _TnSysOtdrFileCounts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 29),
    _TnSysOtdrFileCounts_Type()
)
tnSysOtdrFileCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrFileCounts.setStatus("current")


class _TnSysAltitude_Type(Unsigned32):
    """Custom type tnSysAltitude based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_TnSysAltitude_Type.__name__ = "Unsigned32"
_TnSysAltitude_Object = MibScalar
tnSysAltitude = _TnSysAltitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 30),
    _TnSysAltitude_Type()
)
tnSysAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAltitude.setStatus("current")
if mibBuilder.loadTexts:
    tnSysAltitude.setUnits("meters")


class _TnSysThermalShutdownAutotimer_Type(Integer32):
    """Custom type tnSysThermalShutdownAutotimer based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_TnSysThermalShutdownAutotimer_Type.__name__ = "Integer32"
_TnSysThermalShutdownAutotimer_Object = MibScalar
tnSysThermalShutdownAutotimer = _TnSysThermalShutdownAutotimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 31),
    _TnSysThermalShutdownAutotimer_Type()
)
tnSysThermalShutdownAutotimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysThermalShutdownAutotimer.setStatus("current")
if mibBuilder.loadTexts:
    tnSysThermalShutdownAutotimer.setUnits("seconds")


class _TnSysDisplayShelfLabel_Type(TruthValue):
    """Custom type tnSysDisplayShelfLabel based on TruthValue"""
    defaultValue = 2


_TnSysDisplayShelfLabel_Type.__name__ = "TruthValue"
_TnSysDisplayShelfLabel_Object = MibScalar
tnSysDisplayShelfLabel = _TnSysDisplayShelfLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 32),
    _TnSysDisplayShelfLabel_Type()
)
tnSysDisplayShelfLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDisplayShelfLabel.setStatus("current")


class _TnSysPMFineGranularityControl_Type(Integer32):
    """Custom type tnSysPMFineGranularityControl based on Integer32"""
    defaultValue = 2

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


_TnSysPMFineGranularityControl_Type.__name__ = "Integer32"
_TnSysPMFineGranularityControl_Object = MibScalar
tnSysPMFineGranularityControl = _TnSysPMFineGranularityControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 33),
    _TnSysPMFineGranularityControl_Type()
)
tnSysPMFineGranularityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPMFineGranularityControl.setStatus("current")


class _TnSysFmRead_Type(TruthValue):
    """Custom type tnSysFmRead based on TruthValue"""
    defaultValue = 2


_TnSysFmRead_Type.__name__ = "TruthValue"
_TnSysFmRead_Object = MibScalar
tnSysFmRead = _TnSysFmRead_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 34),
    _TnSysFmRead_Type()
)
tnSysFmRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFmRead.setStatus("current")


class _TnSysPMStreamingServerControl_Type(Integer32):
    """Custom type tnSysPMStreamingServerControl based on Integer32"""
    defaultValue = 2

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


_TnSysPMStreamingServerControl_Type.__name__ = "Integer32"
_TnSysPMStreamingServerControl_Object = MibScalar
tnSysPMStreamingServerControl = _TnSysPMStreamingServerControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 35),
    _TnSysPMStreamingServerControl_Type()
)
tnSysPMStreamingServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPMStreamingServerControl.setStatus("current")


class _TnSysSlotMigrationControl_Type(Integer32):
    """Custom type tnSysSlotMigrationControl based on Integer32"""
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
        *(("noCmd", 1),
          ("activate", 2),
          ("clear", 3))
    )


_TnSysSlotMigrationControl_Type.__name__ = "Integer32"
_TnSysSlotMigrationControl_Object = MibScalar
tnSysSlotMigrationControl = _TnSysSlotMigrationControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 36),
    _TnSysSlotMigrationControl_Type()
)
tnSysSlotMigrationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSlotMigrationControl.setStatus("current")


class _TnSysFlexGridClusterOcsAddDropEnabled_Type(TruthValue):
    """Custom type tnSysFlexGridClusterOcsAddDropEnabled based on TruthValue"""
    defaultValue = 2


_TnSysFlexGridClusterOcsAddDropEnabled_Type.__name__ = "TruthValue"
_TnSysFlexGridClusterOcsAddDropEnabled_Object = MibScalar
tnSysFlexGridClusterOcsAddDropEnabled = _TnSysFlexGridClusterOcsAddDropEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 37),
    _TnSysFlexGridClusterOcsAddDropEnabled_Type()
)
tnSysFlexGridClusterOcsAddDropEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFlexGridClusterOcsAddDropEnabled.setStatus("current")


class _TnSysFilterCheckTime_Type(Unsigned32):
    """Custom type tnSysFilterCheckTime based on Unsigned32"""
    defaultValue = 0


_TnSysFilterCheckTime_Type.__name__ = "Unsigned32"
_TnSysFilterCheckTime_Object = MibScalar
tnSysFilterCheckTime = _TnSysFilterCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 38),
    _TnSysFilterCheckTime_Type()
)
tnSysFilterCheckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFilterCheckTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysFilterCheckTime.setUnits("seconds")


class _TnSysCNLinkPhysicalIfIndex_Type(SnmpAdminString):
    """Custom type tnSysCNLinkPhysicalIfIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 168),
    )


_TnSysCNLinkPhysicalIfIndex_Type.__name__ = "SnmpAdminString"
_TnSysCNLinkPhysicalIfIndex_Object = MibScalar
tnSysCNLinkPhysicalIfIndex = _TnSysCNLinkPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 1, 39),
    _TnSysCNLinkPhysicalIfIndex_Type()
)
tnSysCNLinkPhysicalIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysCNLinkPhysicalIfIndex.setStatus("current")
_TnSysControlNetwork_ObjectIdentity = ObjectIdentity
tnSysControlNetwork = _TnSysControlNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2)
)
_TnSysIpAddress_Type = IpAddress
_TnSysIpAddress_Object = MibScalar
tnSysIpAddress = _TnSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 1),
    _TnSysIpAddress_Type()
)
tnSysIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAddress.setStatus("current")
_TnSysSubnetMask_Type = IpAddress
_TnSysSubnetMask_Object = MibScalar
tnSysSubnetMask = _TnSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 2),
    _TnSysSubnetMask_Type()
)
tnSysSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSubnetMask.setStatus("current")
_TnSysConfiguredIpAddress_Type = IpAddress
_TnSysConfiguredIpAddress_Object = MibScalar
tnSysConfiguredIpAddress = _TnSysConfiguredIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 3),
    _TnSysConfiguredIpAddress_Type()
)
tnSysConfiguredIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredIpAddress.setStatus("current")
_TnSysConfiguredSubnetMask_Type = IpAddress
_TnSysConfiguredSubnetMask_Object = MibScalar
tnSysConfiguredSubnetMask = _TnSysConfiguredSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 4),
    _TnSysConfiguredSubnetMask_Type()
)
tnSysConfiguredSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSubnetMask.setStatus("current")


class _TnSysConfiguredSnmpSource_Type(TruthValue):
    """Custom type tnSysConfiguredSnmpSource based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredSnmpSource_Type.__name__ = "TruthValue"
_TnSysConfiguredSnmpSource_Object = MibScalar
tnSysConfiguredSnmpSource = _TnSysConfiguredSnmpSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 5),
    _TnSysConfiguredSnmpSource_Type()
)
tnSysConfiguredSnmpSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSnmpSource.setStatus("current")
_TnSysConfiguredOcsIpAddress_Type = IpAddress
_TnSysConfiguredOcsIpAddress_Object = MibScalar
tnSysConfiguredOcsIpAddress = _TnSysConfiguredOcsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 6),
    _TnSysConfiguredOcsIpAddress_Type()
)
tnSysConfiguredOcsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredOcsIpAddress.setStatus("current")
_TnSysConfiguredOcs2IpAddress_Type = IpAddress
_TnSysConfiguredOcs2IpAddress_Object = MibScalar
tnSysConfiguredOcs2IpAddress = _TnSysConfiguredOcs2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 7),
    _TnSysConfiguredOcs2IpAddress_Type()
)
tnSysConfiguredOcs2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredOcs2IpAddress.setStatus("current")
_TnSysConfiguredOcs3IpAddress_Type = IpAddress
_TnSysConfiguredOcs3IpAddress_Object = MibScalar
tnSysConfiguredOcs3IpAddress = _TnSysConfiguredOcs3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 8),
    _TnSysConfiguredOcs3IpAddress_Type()
)
tnSysConfiguredOcs3IpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysConfiguredOcs3IpAddress.setStatus("current")
_TnSysOcs1LinkStatus_Type = AluWdmOcsLinkStatus
_TnSysOcs1LinkStatus_Object = MibScalar
tnSysOcs1LinkStatus = _TnSysOcs1LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 9),
    _TnSysOcs1LinkStatus_Type()
)
tnSysOcs1LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOcs1LinkStatus.setStatus("current")
_TnSysOcs2LinkStatus_Type = AluWdmOcsLinkStatus
_TnSysOcs2LinkStatus_Object = MibScalar
tnSysOcs2LinkStatus = _TnSysOcs2LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 10),
    _TnSysOcs2LinkStatus_Type()
)
tnSysOcs2LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOcs2LinkStatus.setStatus("current")
_TnSysOcs3LinkStatus_Type = AluWdmOcsLinkStatus
_TnSysOcs3LinkStatus_Object = MibScalar
tnSysOcs3LinkStatus = _TnSysOcs3LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 11),
    _TnSysOcs3LinkStatus_Type()
)
tnSysOcs3LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOcs3LinkStatus.setStatus("current")


class _TnSysConfiguredRadiusSource_Type(TruthValue):
    """Custom type tnSysConfiguredRadiusSource based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredRadiusSource_Type.__name__ = "TruthValue"
_TnSysConfiguredRadiusSource_Object = MibScalar
tnSysConfiguredRadiusSource = _TnSysConfiguredRadiusSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 12),
    _TnSysConfiguredRadiusSource_Type()
)
tnSysConfiguredRadiusSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredRadiusSource.setStatus("current")
_TnSysConfiguredLoopbackIp1_Type = IpAddress
_TnSysConfiguredLoopbackIp1_Object = MibScalar
tnSysConfiguredLoopbackIp1 = _TnSysConfiguredLoopbackIp1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 13),
    _TnSysConfiguredLoopbackIp1_Type()
)
tnSysConfiguredLoopbackIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredLoopbackIp1.setStatus("current")
_TnSysConfiguredLoopbackIp1SubnetMask_Type = IpAddress
_TnSysConfiguredLoopbackIp1SubnetMask_Object = MibScalar
tnSysConfiguredLoopbackIp1SubnetMask = _TnSysConfiguredLoopbackIp1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 14),
    _TnSysConfiguredLoopbackIp1SubnetMask_Type()
)
tnSysConfiguredLoopbackIp1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredLoopbackIp1SubnetMask.setStatus("current")


class _TnSysConfiguredSnmpSource1_Type(TruthValue):
    """Custom type tnSysConfiguredSnmpSource1 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredSnmpSource1_Type.__name__ = "TruthValue"
_TnSysConfiguredSnmpSource1_Object = MibScalar
tnSysConfiguredSnmpSource1 = _TnSysConfiguredSnmpSource1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 15),
    _TnSysConfiguredSnmpSource1_Type()
)
tnSysConfiguredSnmpSource1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSnmpSource1.setStatus("current")


class _TnSysConfiguredRadiusSource1_Type(TruthValue):
    """Custom type tnSysConfiguredRadiusSource1 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredRadiusSource1_Type.__name__ = "TruthValue"
_TnSysConfiguredRadiusSource1_Object = MibScalar
tnSysConfiguredRadiusSource1 = _TnSysConfiguredRadiusSource1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 16),
    _TnSysConfiguredRadiusSource1_Type()
)
tnSysConfiguredRadiusSource1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredRadiusSource1.setStatus("current")
_TnSysLoopbackIpAddress1_Type = IpAddress
_TnSysLoopbackIpAddress1_Object = MibScalar
tnSysLoopbackIpAddress1 = _TnSysLoopbackIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 17),
    _TnSysLoopbackIpAddress1_Type()
)
tnSysLoopbackIpAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLoopbackIpAddress1.setStatus("current")
_TnSysLoopbackIp1SubnetMask_Type = IpAddress
_TnSysLoopbackIp1SubnetMask_Object = MibScalar
tnSysLoopbackIp1SubnetMask = _TnSysLoopbackIp1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 18),
    _TnSysLoopbackIp1SubnetMask_Type()
)
tnSysLoopbackIp1SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLoopbackIp1SubnetMask.setStatus("current")


class _TnSysConfiguredInetAddressType_Type(InetAddressType):
    """Custom type tnSysConfiguredInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysConfiguredInetAddressType_Type.__name__ = "InetAddressType"
_TnSysConfiguredInetAddressType_Object = MibScalar
tnSysConfiguredInetAddressType = _TnSysConfiguredInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 19),
    _TnSysConfiguredInetAddressType_Type()
)
tnSysConfiguredInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredInetAddressType.setStatus("current")


class _TnSysConfiguredInetAddress_Type(InetAddress):
    """Custom type tnSysConfiguredInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysConfiguredInetAddress_Type.__name__ = "InetAddress"
_TnSysConfiguredInetAddress_Object = MibScalar
tnSysConfiguredInetAddress = _TnSysConfiguredInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 20),
    _TnSysConfiguredInetAddress_Type()
)
tnSysConfiguredInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredInetAddress.setStatus("current")


class _TnSysConfiguredPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tnSysConfiguredPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TnSysConfiguredPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TnSysConfiguredPrefixLength_Object = MibScalar
tnSysConfiguredPrefixLength = _TnSysConfiguredPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 21),
    _TnSysConfiguredPrefixLength_Type()
)
tnSysConfiguredPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysConfiguredPrefixLength.setStatus("current")


class _TnSysOcsIp1Password_Type(SnmpAdminString):
    """Custom type tnSysOcsIp1Password based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOcsIp1Password_Type.__name__ = "SnmpAdminString"
_TnSysOcsIp1Password_Object = MibScalar
tnSysOcsIp1Password = _TnSysOcsIp1Password_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 22),
    _TnSysOcsIp1Password_Type()
)
tnSysOcsIp1Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcsIp1Password.setStatus("current")


class _TnSysOcsIp2Password_Type(SnmpAdminString):
    """Custom type tnSysOcsIp2Password based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOcsIp2Password_Type.__name__ = "SnmpAdminString"
_TnSysOcsIp2Password_Object = MibScalar
tnSysOcsIp2Password = _TnSysOcsIp2Password_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 23),
    _TnSysOcsIp2Password_Type()
)
tnSysOcsIp2Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcsIp2Password.setStatus("current")


class _TnSysOcsIp3Password_Type(SnmpAdminString):
    """Custom type tnSysOcsIp3Password based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOcsIp3Password_Type.__name__ = "SnmpAdminString"
_TnSysOcsIp3Password_Object = MibScalar
tnSysOcsIp3Password = _TnSysOcsIp3Password_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 24),
    _TnSysOcsIp3Password_Type()
)
tnSysOcsIp3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOcsIp3Password.setStatus("current")


class _TnSysConfiguredSnmpSourceIPv6_Type(TruthValue):
    """Custom type tnSysConfiguredSnmpSourceIPv6 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredSnmpSourceIPv6_Type.__name__ = "TruthValue"
_TnSysConfiguredSnmpSourceIPv6_Object = MibScalar
tnSysConfiguredSnmpSourceIPv6 = _TnSysConfiguredSnmpSourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 25),
    _TnSysConfiguredSnmpSourceIPv6_Type()
)
tnSysConfiguredSnmpSourceIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredSnmpSourceIPv6.setStatus("current")


class _TnSysConfiguredRadiusSourceIPv6_Type(TruthValue):
    """Custom type tnSysConfiguredRadiusSourceIPv6 based on TruthValue"""
    defaultValue = 2


_TnSysConfiguredRadiusSourceIPv6_Type.__name__ = "TruthValue"
_TnSysConfiguredRadiusSourceIPv6_Object = MibScalar
tnSysConfiguredRadiusSourceIPv6 = _TnSysConfiguredRadiusSourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 2, 26),
    _TnSysConfiguredRadiusSourceIPv6_Type()
)
tnSysConfiguredRadiusSourceIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysConfiguredRadiusSourceIPv6.setStatus("current")
_TnSysRedundancy_ObjectIdentity = ObjectIdentity
tnSysRedundancy = _TnSysRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3)
)


class _TnSysRedundancyDbSynchState_Type(Integer32):
    """Custom type tnSysRedundancyDbSynchState based on Integer32"""
    defaultValue = 1

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
        *(("notSynched", 1),
          ("synched", 2),
          ("synching", 3),
          ("unSynchable", 4),
          ("synchFailure", 5),
          ("schemaTesting", 6))
    )


_TnSysRedundancyDbSynchState_Type.__name__ = "Integer32"
_TnSysRedundancyDbSynchState_Object = MibScalar
tnSysRedundancyDbSynchState = _TnSysRedundancyDbSynchState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 1),
    _TnSysRedundancyDbSynchState_Type()
)
tnSysRedundancyDbSynchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyDbSynchState.setStatus("current")


class _TnSysRedundancyDbResynch_Type(TnCommand):
    """Custom type tnSysRedundancyDbResynch based on TnCommand"""
    defaultValue = 1


_TnSysRedundancyDbResynch_Type.__name__ = "TnCommand"
_TnSysRedundancyDbResynch_Object = MibScalar
tnSysRedundancyDbResynch = _TnSysRedundancyDbResynch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 2),
    _TnSysRedundancyDbResynch_Type()
)
tnSysRedundancyDbResynch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRedundancyDbResynch.setStatus("current")


class _TnSysRedundancyDbAudit_Type(TnCommand):
    """Custom type tnSysRedundancyDbAudit based on TnCommand"""
    defaultValue = 1


_TnSysRedundancyDbAudit_Type.__name__ = "TnCommand"
_TnSysRedundancyDbAudit_Object = MibScalar
tnSysRedundancyDbAudit = _TnSysRedundancyDbAudit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 3),
    _TnSysRedundancyDbAudit_Type()
)
tnSysRedundancyDbAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRedundancyDbAudit.setStatus("current")


class _TnSysRedundancyDbClear_Type(Integer32):
    """Custom type tnSysRedundancyDbClear based on Integer32"""
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
        *(("noCmd", 1),
          ("execute", 2),
          ("executeAndClearSonetSdhMode", 3))
    )


_TnSysRedundancyDbClear_Type.__name__ = "Integer32"
_TnSysRedundancyDbClear_Object = MibScalar
tnSysRedundancyDbClear = _TnSysRedundancyDbClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 4),
    _TnSysRedundancyDbClear_Type()
)
tnSysRedundancyDbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRedundancyDbClear.setStatus("current")


class _TnSysRedundancyActiveCCSlot_Type(Unsigned32):
    """Custom type tnSysRedundancyActiveCCSlot based on Unsigned32"""
    defaultValue = 1


_TnSysRedundancyActiveCCSlot_Type.__name__ = "Unsigned32"
_TnSysRedundancyActiveCCSlot_Object = MibScalar
tnSysRedundancyActiveCCSlot = _TnSysRedundancyActiveCCSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 5),
    _TnSysRedundancyActiveCCSlot_Type()
)
tnSysRedundancyActiveCCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyActiveCCSlot.setStatus("current")


class _TnSysRedundancyDbInvalid_Type(TruthValue):
    """Custom type tnSysRedundancyDbInvalid based on TruthValue"""
    defaultValue = 2


_TnSysRedundancyDbInvalid_Type.__name__ = "TruthValue"
_TnSysRedundancyDbInvalid_Object = MibScalar
tnSysRedundancyDbInvalid = _TnSysRedundancyDbInvalid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 6),
    _TnSysRedundancyDbInvalid_Type()
)
tnSysRedundancyDbInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyDbInvalid.setStatus("current")


class _TnSysRedundancyMateCCReadyToProtect_Type(TruthValue):
    """Custom type tnSysRedundancyMateCCReadyToProtect based on TruthValue"""
    defaultValue = 2


_TnSysRedundancyMateCCReadyToProtect_Type.__name__ = "TruthValue"
_TnSysRedundancyMateCCReadyToProtect_Object = MibScalar
tnSysRedundancyMateCCReadyToProtect = _TnSysRedundancyMateCCReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 3, 7),
    _TnSysRedundancyMateCCReadyToProtect_Type()
)
tnSysRedundancyMateCCReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysRedundancyMateCCReadyToProtect.setStatus("current")
_TnSysDiscovery_ObjectIdentity = ObjectIdentity
tnSysDiscovery = _TnSysDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4)
)


class _TnSysDiscoveryFilename_Type(SnmpAdminString):
    """Custom type tnSysDiscoveryFilename based on SnmpAdminString"""
    defaultValue = OctetString("./remote-file")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysDiscoveryFilename_Type.__name__ = "SnmpAdminString"
_TnSysDiscoveryFilename_Object = MibScalar
tnSysDiscoveryFilename = _TnSysDiscoveryFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 2),
    _TnSysDiscoveryFilename_Type()
)
tnSysDiscoveryFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryFilename.setStatus("current")


class _TnSysDiscoveryMask_Type(Bits):
    """Custom type tnSysDiscoveryMask based on Bits"""
    namedValues = NamedValues(
        *(("stage1", 0),
          ("stage2", 1),
          ("stage3", 2),
          ("stage4", 3),
          ("stage5", 4),
          ("stage6", 5),
          ("stage7", 6))
    )

_TnSysDiscoveryMask_Type.__name__ = "Bits"
_TnSysDiscoveryMask_Object = MibScalar
tnSysDiscoveryMask = _TnSysDiscoveryMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 3),
    _TnSysDiscoveryMask_Type()
)
tnSysDiscoveryMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryMask.setStatus("current")


class _TnSysDiscoveryControl_Type(Integer32):
    """Custom type tnSysDiscoveryControl based on Integer32"""
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
        *(("noCmd", 1),
          ("start", 2),
          ("abort", 3))
    )


_TnSysDiscoveryControl_Type.__name__ = "Integer32"
_TnSysDiscoveryControl_Object = MibScalar
tnSysDiscoveryControl = _TnSysDiscoveryControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 4),
    _TnSysDiscoveryControl_Type()
)
tnSysDiscoveryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryControl.setStatus("current")


class _TnSysDiscoveryStatus_Type(Integer32):
    """Custom type tnSysDiscoveryStatus based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnSysDiscoveryStatus_Type.__name__ = "Integer32"
_TnSysDiscoveryStatus_Object = MibScalar
tnSysDiscoveryStatus = _TnSysDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 5),
    _TnSysDiscoveryStatus_Type()
)
tnSysDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDiscoveryStatus.setStatus("current")


class _TnSysDiscoveryErrorCode_Type(Integer32):
    """Custom type tnSysDiscoveryErrorCode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("unknown", 2),
          ("timeout", 3),
          ("serverError", 4),
          ("networkError", 5),
          ("fileSystemError", 6),
          ("statsBinsRolled", 7))
    )


_TnSysDiscoveryErrorCode_Type.__name__ = "Integer32"
_TnSysDiscoveryErrorCode_Object = MibScalar
tnSysDiscoveryErrorCode = _TnSysDiscoveryErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 6),
    _TnSysDiscoveryErrorCode_Type()
)
tnSysDiscoveryErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDiscoveryErrorCode.setStatus("current")


class _TnSysDiscoveryBinnedStatsInterval_Type(Unsigned32):
    """Custom type tnSysDiscoveryBinnedStatsInterval based on Unsigned32"""
    defaultValue = 0


_TnSysDiscoveryBinnedStatsInterval_Type.__name__ = "Unsigned32"
_TnSysDiscoveryBinnedStatsInterval_Object = MibScalar
tnSysDiscoveryBinnedStatsInterval = _TnSysDiscoveryBinnedStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 8),
    _TnSysDiscoveryBinnedStatsInterval_Type()
)
tnSysDiscoveryBinnedStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryBinnedStatsInterval.setStatus("current")


class _TnSysDiscoveryBinnedStatsBin_Type(Unsigned32):
    """Custom type tnSysDiscoveryBinnedStatsBin based on Unsigned32"""
    defaultValue = 0


_TnSysDiscoveryBinnedStatsBin_Type.__name__ = "Unsigned32"
_TnSysDiscoveryBinnedStatsBin_Object = MibScalar
tnSysDiscoveryBinnedStatsBin = _TnSysDiscoveryBinnedStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 9),
    _TnSysDiscoveryBinnedStatsBin_Type()
)
tnSysDiscoveryBinnedStatsBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryBinnedStatsBin.setStatus("current")


class _TnSysDiscoveryServerProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysDiscoveryServerProtocol based on AluWdmTransferProtocol"""
    defaultValue = 3


_TnSysDiscoveryServerProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysDiscoveryServerProtocol_Object = MibScalar
tnSysDiscoveryServerProtocol = _TnSysDiscoveryServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 10),
    _TnSysDiscoveryServerProtocol_Type()
)
tnSysDiscoveryServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerProtocol.setStatus("current")
_TnSysDiscoveryServerIp_Type = IpAddress
_TnSysDiscoveryServerIp_Object = MibScalar
tnSysDiscoveryServerIp = _TnSysDiscoveryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 11),
    _TnSysDiscoveryServerIp_Type()
)
tnSysDiscoveryServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerIp.setStatus("current")


class _TnSysDiscoveryServerUserId_Type(SnmpAdminString):
    """Custom type tnSysDiscoveryServerUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysDiscoveryServerUserId_Type.__name__ = "SnmpAdminString"
_TnSysDiscoveryServerUserId_Object = MibScalar
tnSysDiscoveryServerUserId = _TnSysDiscoveryServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 12),
    _TnSysDiscoveryServerUserId_Type()
)
tnSysDiscoveryServerUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerUserId.setStatus("current")


class _TnSysDiscoveryServerPassword_Type(SnmpAdminString):
    """Custom type tnSysDiscoveryServerPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysDiscoveryServerPassword_Type.__name__ = "SnmpAdminString"
_TnSysDiscoveryServerPassword_Object = MibScalar
tnSysDiscoveryServerPassword = _TnSysDiscoveryServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 13),
    _TnSysDiscoveryServerPassword_Type()
)
tnSysDiscoveryServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerPassword.setStatus("current")


class _TnSysDiscoveryServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysDiscoveryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysDiscoveryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysDiscoveryServerInetAddressType_Object = MibScalar
tnSysDiscoveryServerInetAddressType = _TnSysDiscoveryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 14),
    _TnSysDiscoveryServerInetAddressType_Type()
)
tnSysDiscoveryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerInetAddressType.setStatus("current")


class _TnSysDiscoveryServerInetAddress_Type(InetAddress):
    """Custom type tnSysDiscoveryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysDiscoveryServerInetAddress_Type.__name__ = "InetAddress"
_TnSysDiscoveryServerInetAddress_Object = MibScalar
tnSysDiscoveryServerInetAddress = _TnSysDiscoveryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 4, 15),
    _TnSysDiscoveryServerInetAddress_Type()
)
tnSysDiscoveryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDiscoveryServerInetAddress.setStatus("current")
_TnSysLogging_ObjectIdentity = ObjectIdentity
tnSysLogging = _TnSysLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 5)
)


class _TnSysLoggingCLI_Type(Bits):
    """Custom type tnSysLoggingCLI based on Bits"""
    namedValues = NamedValues(
        *(("disableAllLogging", 0),
          ("level1Read", 1),
          ("level1Write", 2),
          ("level2Read", 3),
          ("level2Write", 4),
          ("level3Read", 5),
          ("level3Write", 6),
          ("level4Read", 7),
          ("level4Write", 8),
          ("level5Read", 9),
          ("level5Write", 10),
          ("level6Read", 11),
          ("level6Write", 12))
    )

_TnSysLoggingCLI_Type.__name__ = "Bits"
_TnSysLoggingCLI_Object = MibScalar
tnSysLoggingCLI = _TnSysLoggingCLI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 5, 1),
    _TnSysLoggingCLI_Type()
)
tnSysLoggingCLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLoggingCLI.setStatus("current")


class _TnSysLoggingSNMP_Type(Bits):
    """Custom type tnSysLoggingSNMP based on Bits"""
    namedValues = NamedValues(
        *(("disableAllLogging", 0),
          ("level1Read", 1),
          ("level1Write", 2),
          ("level2Read", 3),
          ("level2Write", 4),
          ("level3Read", 5),
          ("level3Write", 6),
          ("level4Read", 7),
          ("level4Write", 8),
          ("level5Read", 9),
          ("level5Write", 10),
          ("level6Read", 11),
          ("level6Write", 12))
    )

_TnSysLoggingSNMP_Type.__name__ = "Bits"
_TnSysLoggingSNMP_Object = MibScalar
tnSysLoggingSNMP = _TnSysLoggingSNMP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 5, 2),
    _TnSysLoggingSNMP_Type()
)
tnSysLoggingSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLoggingSNMP.setStatus("current")
_TnSysBackupAndRestore_ObjectIdentity = ObjectIdentity
tnSysBackupAndRestore = _TnSysBackupAndRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6)
)


class _TnSysBackupAndRestoreCommand_Type(Integer32):
    """Custom type tnSysBackupAndRestoreCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("backupToRemote", 2),
          ("restoreFromRemote", 3),
          ("restoreForceFromRemote", 4))
    )


_TnSysBackupAndRestoreCommand_Type.__name__ = "Integer32"
_TnSysBackupAndRestoreCommand_Object = MibScalar
tnSysBackupAndRestoreCommand = _TnSysBackupAndRestoreCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 1),
    _TnSysBackupAndRestoreCommand_Type()
)
tnSysBackupAndRestoreCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreCommand.setStatus("current")
_TnSysBackupAndRestoreRemoteHostIp_Type = IpAddress
_TnSysBackupAndRestoreRemoteHostIp_Object = MibScalar
tnSysBackupAndRestoreRemoteHostIp = _TnSysBackupAndRestoreRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 2),
    _TnSysBackupAndRestoreRemoteHostIp_Type()
)
tnSysBackupAndRestoreRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemoteHostIp.setStatus("current")


class _TnSysBackupAndRestoreRemotePath_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysBackupAndRestoreRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreRemotePath_Object = MibScalar
tnSysBackupAndRestoreRemotePath = _TnSysBackupAndRestoreRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 3),
    _TnSysBackupAndRestoreRemotePath_Type()
)
tnSysBackupAndRestoreRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemotePath.setStatus("current")


class _TnSysBackupAndRestoreStatus_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreStatus based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysBackupAndRestoreStatus_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreStatus_Object = MibScalar
tnSysBackupAndRestoreStatus = _TnSysBackupAndRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 4),
    _TnSysBackupAndRestoreStatus_Type()
)
tnSysBackupAndRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreStatus.setStatus("current")


class _TnSysBackupAndRestoreLastBackupFilename_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreLastBackupFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysBackupAndRestoreLastBackupFilename_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreLastBackupFilename_Object = MibScalar
tnSysBackupAndRestoreLastBackupFilename = _TnSysBackupAndRestoreLastBackupFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 5),
    _TnSysBackupAndRestoreLastBackupFilename_Type()
)
tnSysBackupAndRestoreLastBackupFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastBackupFilename.setStatus("current")


class _TnSysBackupAndRestoreLastCommand_Type(Integer32):
    """Custom type tnSysBackupAndRestoreLastCommand based on Integer32"""
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
        *(("noCommand", 1),
          ("unknown", 2),
          ("backupToRemote", 3),
          ("restoreFromRemote", 4))
    )


_TnSysBackupAndRestoreLastCommand_Type.__name__ = "Integer32"
_TnSysBackupAndRestoreLastCommand_Object = MibScalar
tnSysBackupAndRestoreLastCommand = _TnSysBackupAndRestoreLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 6),
    _TnSysBackupAndRestoreLastCommand_Type()
)
tnSysBackupAndRestoreLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastCommand.setStatus("current")


class _TnSysBackupAndRestorePercentCompleted_Type(Unsigned32):
    """Custom type tnSysBackupAndRestorePercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysBackupAndRestorePercentCompleted_Type.__name__ = "Unsigned32"
_TnSysBackupAndRestorePercentCompleted_Object = MibScalar
tnSysBackupAndRestorePercentCompleted = _TnSysBackupAndRestorePercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 7),
    _TnSysBackupAndRestorePercentCompleted_Type()
)
tnSysBackupAndRestorePercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestorePercentCompleted.setStatus("current")


class _TnSysBackupAndRestoreLastBackupFileTimeStamp_Type(Unsigned32):
    """Custom type tnSysBackupAndRestoreLastBackupFileTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysBackupAndRestoreLastBackupFileTimeStamp_Type.__name__ = "Unsigned32"
_TnSysBackupAndRestoreLastBackupFileTimeStamp_Object = MibScalar
tnSysBackupAndRestoreLastBackupFileTimeStamp = _TnSysBackupAndRestoreLastBackupFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 8),
    _TnSysBackupAndRestoreLastBackupFileTimeStamp_Type()
)
tnSysBackupAndRestoreLastBackupFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastBackupFileTimeStamp.setStatus("current")


class _TnSysBackupAndRestoreProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysBackupAndRestoreProtocol based on AluWdmTransferProtocol"""
    defaultValue = 3


_TnSysBackupAndRestoreProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysBackupAndRestoreProtocol_Object = MibScalar
tnSysBackupAndRestoreProtocol = _TnSysBackupAndRestoreProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 9),
    _TnSysBackupAndRestoreProtocol_Type()
)
tnSysBackupAndRestoreProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreProtocol.setStatus("current")


class _TnSysBackupAndRestoreUserId_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysBackupAndRestoreUserId_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreUserId_Object = MibScalar
tnSysBackupAndRestoreUserId = _TnSysBackupAndRestoreUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 10),
    _TnSysBackupAndRestoreUserId_Type()
)
tnSysBackupAndRestoreUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreUserId.setStatus("current")


class _TnSysBackupAndRestorePassword_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestorePassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysBackupAndRestorePassword_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestorePassword_Object = MibScalar
tnSysBackupAndRestorePassword = _TnSysBackupAndRestorePassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 11),
    _TnSysBackupAndRestorePassword_Type()
)
tnSysBackupAndRestorePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestorePassword.setStatus("current")


class _TnSysBackupAndRestoreLastBackupFileCrc_Type(SnmpAdminString):
    """Custom type tnSysBackupAndRestoreLastBackupFileCrc based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysBackupAndRestoreLastBackupFileCrc_Type.__name__ = "SnmpAdminString"
_TnSysBackupAndRestoreLastBackupFileCrc_Object = MibScalar
tnSysBackupAndRestoreLastBackupFileCrc = _TnSysBackupAndRestoreLastBackupFileCrc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 12),
    _TnSysBackupAndRestoreLastBackupFileCrc_Type()
)
tnSysBackupAndRestoreLastBackupFileCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreLastBackupFileCrc.setStatus("current")


class _TnSysBackupAndRestoreRemoteHostInetAddressType_Type(InetAddressType):
    """Custom type tnSysBackupAndRestoreRemoteHostInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysBackupAndRestoreRemoteHostInetAddressType_Type.__name__ = "InetAddressType"
_TnSysBackupAndRestoreRemoteHostInetAddressType_Object = MibScalar
tnSysBackupAndRestoreRemoteHostInetAddressType = _TnSysBackupAndRestoreRemoteHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 14),
    _TnSysBackupAndRestoreRemoteHostInetAddressType_Type()
)
tnSysBackupAndRestoreRemoteHostInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemoteHostInetAddressType.setStatus("current")


class _TnSysBackupAndRestoreRemoteHostInetAddress_Type(InetAddress):
    """Custom type tnSysBackupAndRestoreRemoteHostInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysBackupAndRestoreRemoteHostInetAddress_Type.__name__ = "InetAddress"
_TnSysBackupAndRestoreRemoteHostInetAddress_Object = MibScalar
tnSysBackupAndRestoreRemoteHostInetAddress = _TnSysBackupAndRestoreRemoteHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 6, 15),
    _TnSysBackupAndRestoreRemoteHostInetAddress_Type()
)
tnSysBackupAndRestoreRemoteHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysBackupAndRestoreRemoteHostInetAddress.setStatus("current")
_TnSysNtp_ObjectIdentity = ObjectIdentity
tnSysNtp = _TnSysNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7)
)


class _TnSysNtpEnable_Type(TruthValue):
    """Custom type tnSysNtpEnable based on TruthValue"""
    defaultValue = 2


_TnSysNtpEnable_Type.__name__ = "TruthValue"
_TnSysNtpEnable_Object = MibScalar
tnSysNtpEnable = _TnSysNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 1),
    _TnSysNtpEnable_Type()
)
tnSysNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpEnable.setStatus("current")


class _TnSysNtpSynched_Type(TruthValue):
    """Custom type tnSysNtpSynched based on TruthValue"""
    defaultValue = 2


_TnSysNtpSynched_Type.__name__ = "TruthValue"
_TnSysNtpSynched_Object = MibScalar
tnSysNtpSynched = _TnSysNtpSynched_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 8),
    _TnSysNtpSynched_Type()
)
tnSysNtpSynched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpSynched.setStatus("current")
_TnSysNtpServerCurrentIpAddress_Type = IpAddress
_TnSysNtpServerCurrentIpAddress_Object = MibScalar
tnSysNtpServerCurrentIpAddress = _TnSysNtpServerCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 9),
    _TnSysNtpServerCurrentIpAddress_Type()
)
tnSysNtpServerCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerCurrentIpAddress.setStatus("current")
_TnSysNtpDriftString_Type = OctetString
_TnSysNtpDriftString_Object = MibScalar
tnSysNtpDriftString = _TnSysNtpDriftString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 11),
    _TnSysNtpDriftString_Type()
)
tnSysNtpDriftString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpDriftString.setStatus("current")
_TnSysNtpTimeOffsetString_Type = OctetString
_TnSysNtpTimeOffsetString_Object = MibScalar
tnSysNtpTimeOffsetString = _TnSysNtpTimeOffsetString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 12),
    _TnSysNtpTimeOffsetString_Type()
)
tnSysNtpTimeOffsetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpTimeOffsetString.setStatus("current")


class _TnSysNtpClockMode_Type(Integer32):
    """Custom type tnSysNtpClockMode based on Integer32"""
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
        *(("freeRun", 1),
          ("holdOver", 2),
          ("sync", 3),
          ("syncRed", 4))
    )


_TnSysNtpClockMode_Type.__name__ = "Integer32"
_TnSysNtpClockMode_Object = MibScalar
tnSysNtpClockMode = _TnSysNtpClockMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 13),
    _TnSysNtpClockMode_Type()
)
tnSysNtpClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpClockMode.setStatus("current")


class _TnSysNtpServerCurrentInetAddressType_Type(InetAddressType):
    """Custom type tnSysNtpServerCurrentInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysNtpServerCurrentInetAddressType_Type.__name__ = "InetAddressType"
_TnSysNtpServerCurrentInetAddressType_Object = MibScalar
tnSysNtpServerCurrentInetAddressType = _TnSysNtpServerCurrentInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 14),
    _TnSysNtpServerCurrentInetAddressType_Type()
)
tnSysNtpServerCurrentInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpServerCurrentInetAddressType.setStatus("current")


class _TnSysNtpServerCurrentInetAddress_Type(InetAddress):
    """Custom type tnSysNtpServerCurrentInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysNtpServerCurrentInetAddress_Type.__name__ = "InetAddress"
_TnSysNtpServerCurrentInetAddress_Object = MibScalar
tnSysNtpServerCurrentInetAddress = _TnSysNtpServerCurrentInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 7, 15),
    _TnSysNtpServerCurrentInetAddress_Type()
)
tnSysNtpServerCurrentInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpServerCurrentInetAddress.setStatus("current")
_TnSysNtpServers_ObjectIdentity = ObjectIdentity
tnSysNtpServers = _TnSysNtpServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8)
)
_TnSysNtpServerTable_Object = MibTable
tnSysNtpServerTable = _TnSysNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    tnSysNtpServerTable.setStatus("current")
_TnSysNtpServerEntry_Object = MibTableRow
tnSysNtpServerEntry = _TnSysNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1)
)
tnSysNtpServerEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNtpServerIndex"),
)
if mibBuilder.loadTexts:
    tnSysNtpServerEntry.setStatus("current")


class _TnSysNtpServerIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnSysNtpServerIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerIndex_Object = MibTableColumn
tnSysNtpServerIndex = _TnSysNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 1),
    _TnSysNtpServerIndex_Type()
)
tnSysNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNtpServerIndex.setStatus("current")
_TnSysNtpServerIpAddress_Type = IpAddress
_TnSysNtpServerIpAddress_Object = MibTableColumn
tnSysNtpServerIpAddress = _TnSysNtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 2),
    _TnSysNtpServerIpAddress_Type()
)
tnSysNtpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerIpAddress.setStatus("current")
_TnSysNtpServerRowStatus_Type = RowStatus
_TnSysNtpServerRowStatus_Object = MibTableColumn
tnSysNtpServerRowStatus = _TnSysNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 3),
    _TnSysNtpServerRowStatus_Type()
)
tnSysNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerRowStatus.setStatus("current")


class _TnSysNtpServerKeyIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysNtpServerKeyIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerKeyIndex_Object = MibTableColumn
tnSysNtpServerKeyIndex = _TnSysNtpServerKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 4),
    _TnSysNtpServerKeyIndex_Type()
)
tnSysNtpServerKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerKeyIndex.setStatus("current")


class _TnSysNtpServerInetAddress_Type(InetAddress):
    """Custom type tnSysNtpServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysNtpServerInetAddress_Type.__name__ = "InetAddress"
_TnSysNtpServerInetAddress_Object = MibTableColumn
tnSysNtpServerInetAddress = _TnSysNtpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 5),
    _TnSysNtpServerInetAddress_Type()
)
tnSysNtpServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpServerInetAddress.setStatus("current")


class _TnSysNtpServerInetAddressType_Type(InetAddressType):
    """Custom type tnSysNtpServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysNtpServerInetAddressType_Type.__name__ = "InetAddressType"
_TnSysNtpServerInetAddressType_Object = MibTableColumn
tnSysNtpServerInetAddressType = _TnSysNtpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 8, 1, 1, 6),
    _TnSysNtpServerInetAddressType_Type()
)
tnSysNtpServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysNtpServerInetAddressType.setStatus("current")
_TnSnmpTargetAddresses_ObjectIdentity = ObjectIdentity
tnSnmpTargetAddresses = _TnSnmpTargetAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9)
)
_TnSnmpTargetAddrTable_Object = MibTable
tnSnmpTargetAddrTable = _TnSnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tnSnmpTargetAddrTable.setStatus("current")
_TnSnmpTargetAddrEntry_Object = MibTableRow
tnSnmpTargetAddrEntry = _TnSnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tnSnmpTargetAddrEntry.setStatus("current")
_TnSnmpTargetAddrNmsStationGroupId_Type = Unsigned32
_TnSnmpTargetAddrNmsStationGroupId_Object = MibTableColumn
tnSnmpTargetAddrNmsStationGroupId = _TnSnmpTargetAddrNmsStationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1, 1),
    _TnSnmpTargetAddrNmsStationGroupId_Type()
)
tnSnmpTargetAddrNmsStationGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSnmpTargetAddrNmsStationGroupId.setStatus("current")


class _TnSnmpTargetAddrTrapGroupId_Type(Integer32):
    """Custom type tnSnmpTargetAddrTrapGroupId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOtherData", 1),
          ("pmData", 2))
    )


_TnSnmpTargetAddrTrapGroupId_Type.__name__ = "Integer32"
_TnSnmpTargetAddrTrapGroupId_Object = MibTableColumn
tnSnmpTargetAddrTrapGroupId = _TnSnmpTargetAddrTrapGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 9, 1, 1, 2),
    _TnSnmpTargetAddrTrapGroupId_Type()
)
tnSnmpTargetAddrTrapGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSnmpTargetAddrTrapGroupId.setStatus("current")
_TnSyslog_ObjectIdentity = ObjectIdentity
tnSyslog = _TnSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10)
)
_TnSyslogIpAddress_Type = IpAddress
_TnSyslogIpAddress_Object = MibScalar
tnSyslogIpAddress = _TnSyslogIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 1),
    _TnSyslogIpAddress_Type()
)
tnSyslogIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogIpAddress.setStatus("current")


class _TnSyslogPort_Type(Unsigned32):
    """Custom type tnSyslogPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnSyslogPort_Type.__name__ = "Unsigned32"
_TnSyslogPort_Object = MibScalar
tnSyslogPort = _TnSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 2),
    _TnSyslogPort_Type()
)
tnSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogPort.setStatus("current")


class _TnSyslogFacility_Type(Integer32):
    """Custom type tnSyslogFacility based on Integer32"""
    defaultValue = 13

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
              20)
        )
    )
    namedValues = NamedValues(
        *(("kern", 1),
          ("user", 2),
          ("mail", 3),
          ("daemon", 4),
          ("auth", 5),
          ("syslog", 6),
          ("lpr", 7),
          ("news", 8),
          ("uucp", 9),
          ("cron", 10),
          ("authPriv", 11),
          ("ftp", 12),
          ("local0", 13),
          ("local1", 14),
          ("local2", 15),
          ("local3", 16),
          ("local4", 17),
          ("local5", 18),
          ("local6", 19),
          ("local7", 20))
    )


_TnSyslogFacility_Type.__name__ = "Integer32"
_TnSyslogFacility_Object = MibScalar
tnSyslogFacility = _TnSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 3),
    _TnSyslogFacility_Type()
)
tnSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogFacility.setStatus("current")


class _TnSyslogPriority_Type(Integer32):
    """Custom type tnSyslogPriority based on Integer32"""
    defaultValue = 8

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
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )


_TnSyslogPriority_Type.__name__ = "Integer32"
_TnSyslogPriority_Object = MibScalar
tnSyslogPriority = _TnSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 4),
    _TnSyslogPriority_Type()
)
tnSyslogPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogPriority.setStatus("current")


class _TnSyslogEnabled_Type(TruthValue):
    """Custom type tnSyslogEnabled based on TruthValue"""
    defaultValue = 2


_TnSyslogEnabled_Type.__name__ = "TruthValue"
_TnSyslogEnabled_Object = MibScalar
tnSyslogEnabled = _TnSyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 5),
    _TnSyslogEnabled_Type()
)
tnSyslogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogEnabled.setStatus("current")


class _TnSyslogInetAddress_Type(InetAddress):
    """Custom type tnSyslogInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSyslogInetAddress_Type.__name__ = "InetAddress"
_TnSyslogInetAddress_Object = MibScalar
tnSyslogInetAddress = _TnSyslogInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 6),
    _TnSyslogInetAddress_Type()
)
tnSyslogInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogInetAddress.setStatus("current")


class _TnSyslogInetAddressType_Type(InetAddressType):
    """Custom type tnSyslogInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSyslogInetAddressType_Type.__name__ = "InetAddressType"
_TnSyslogInetAddressType_Object = MibScalar
tnSyslogInetAddressType = _TnSyslogInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 10, 7),
    _TnSyslogInetAddressType_Type()
)
tnSyslogInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyslogInetAddressType.setStatus("current")
_TnSysTiming_ObjectIdentity = ObjectIdentity
tnSysTiming = _TnSysTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11)
)


class _TnSysTimingPrimaryReference_Type(Unsigned32):
    """Custom type tnSysTimingPrimaryReference based on Unsigned32"""
    defaultValue = 0


_TnSysTimingPrimaryReference_Type.__name__ = "Unsigned32"
_TnSysTimingPrimaryReference_Object = MibScalar
tnSysTimingPrimaryReference = _TnSysTimingPrimaryReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 1),
    _TnSysTimingPrimaryReference_Type()
)
tnSysTimingPrimaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReference.setStatus("current")


class _TnSysTimingSecondaryReference_Type(Unsigned32):
    """Custom type tnSysTimingSecondaryReference based on Unsigned32"""
    defaultValue = 0


_TnSysTimingSecondaryReference_Type.__name__ = "Unsigned32"
_TnSysTimingSecondaryReference_Object = MibScalar
tnSysTimingSecondaryReference = _TnSysTimingSecondaryReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 2),
    _TnSysTimingSecondaryReference_Type()
)
tnSysTimingSecondaryReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReference.setStatus("current")


class _TnSysTimingLastSwitchTime_Type(Unsigned32):
    """Custom type tnSysTimingLastSwitchTime based on Unsigned32"""
    defaultValue = 0


_TnSysTimingLastSwitchTime_Type.__name__ = "Unsigned32"
_TnSysTimingLastSwitchTime_Object = MibScalar
tnSysTimingLastSwitchTime = _TnSysTimingLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 3),
    _TnSysTimingLastSwitchTime_Type()
)
tnSysTimingLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingLastSwitchTime.setStatus("current")


class _TnSysTimingControl_Type(Integer32):
    """Custom type tnSysTimingControl based on Integer32"""
    defaultValue = 6

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
        *(("noCmd", 1),
          ("forceToPrimary", 2),
          ("forceToSecondary", 3),
          ("manualToPrimary", 4),
          ("manualToSecondary", 5),
          ("clear", 6))
    )


_TnSysTimingControl_Type.__name__ = "Integer32"
_TnSysTimingControl_Object = MibScalar
tnSysTimingControl = _TnSysTimingControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 4),
    _TnSysTimingControl_Type()
)
tnSysTimingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingControl.setStatus("current")


class _TnSysTimingPrimaryReferenceStatus_Type(Integer32):
    """Custom type tnSysTimingPrimaryReferenceStatus based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("manual", 3),
          ("forced", 4),
          ("failed", 5),
          ("failedLOS", 6),
          ("failedLOF", 7),
          ("failedLOC", 8),
          ("failedFreqOffset", 9),
          ("failedAIS", 10),
          ("failedSSM", 11),
          ("qualifying", 12))
    )


_TnSysTimingPrimaryReferenceStatus_Type.__name__ = "Integer32"
_TnSysTimingPrimaryReferenceStatus_Object = MibScalar
tnSysTimingPrimaryReferenceStatus = _TnSysTimingPrimaryReferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 5),
    _TnSysTimingPrimaryReferenceStatus_Type()
)
tnSysTimingPrimaryReferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReferenceStatus.setStatus("current")


class _TnSysTimingSecondaryReferenceStatus_Type(Integer32):
    """Custom type tnSysTimingSecondaryReferenceStatus based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("manual", 3),
          ("forced", 4),
          ("failed", 5),
          ("failedLOS", 6),
          ("failedLOF", 7),
          ("failedLOC", 8),
          ("failedFreqOffset", 9),
          ("failedAIS", 10),
          ("failedSSM", 11),
          ("qualifying", 12))
    )


_TnSysTimingSecondaryReferenceStatus_Type.__name__ = "Integer32"
_TnSysTimingSecondaryReferenceStatus_Object = MibScalar
tnSysTimingSecondaryReferenceStatus = _TnSysTimingSecondaryReferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 6),
    _TnSysTimingSecondaryReferenceStatus_Type()
)
tnSysTimingSecondaryReferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReferenceStatus.setStatus("current")


class _TnSysTimingPrimaryReferenceQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingPrimaryReferenceQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingPrimaryReferenceQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingPrimaryReferenceQuality_Object = MibScalar
tnSysTimingPrimaryReferenceQuality = _TnSysTimingPrimaryReferenceQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 7),
    _TnSysTimingPrimaryReferenceQuality_Type()
)
tnSysTimingPrimaryReferenceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReferenceQuality.setStatus("current")


class _TnSysTimingSecondaryReferenceQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingSecondaryReferenceQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingSecondaryReferenceQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingSecondaryReferenceQuality_Object = MibScalar
tnSysTimingSecondaryReferenceQuality = _TnSysTimingSecondaryReferenceQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 8),
    _TnSysTimingSecondaryReferenceQuality_Type()
)
tnSysTimingSecondaryReferenceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReferenceQuality.setStatus("current")


class _TnSysTimingPrimaryReferenceTimingMode_Type(TropicSysTimingReferenceTimingMode):
    """Custom type tnSysTimingPrimaryReferenceTimingMode based on TropicSysTimingReferenceTimingMode"""
    defaultValue = 1


_TnSysTimingPrimaryReferenceTimingMode_Type.__name__ = "TropicSysTimingReferenceTimingMode"
_TnSysTimingPrimaryReferenceTimingMode_Object = MibScalar
tnSysTimingPrimaryReferenceTimingMode = _TnSysTimingPrimaryReferenceTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 9),
    _TnSysTimingPrimaryReferenceTimingMode_Type()
)
tnSysTimingPrimaryReferenceTimingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingPrimaryReferenceTimingMode.setStatus("current")


class _TnSysTimingSecondaryReferenceTimingMode_Type(TropicSysTimingReferenceTimingMode):
    """Custom type tnSysTimingSecondaryReferenceTimingMode based on TropicSysTimingReferenceTimingMode"""
    defaultValue = 1


_TnSysTimingSecondaryReferenceTimingMode_Type.__name__ = "TropicSysTimingReferenceTimingMode"
_TnSysTimingSecondaryReferenceTimingMode_Object = MibScalar
tnSysTimingSecondaryReferenceTimingMode = _TnSysTimingSecondaryReferenceTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 10),
    _TnSysTimingSecondaryReferenceTimingMode_Type()
)
tnSysTimingSecondaryReferenceTimingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingSecondaryReferenceTimingMode.setStatus("current")


class _TnSysTimingActiveReference_Type(Integer32):
    """Custom type tnSysTimingActiveReference based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_TnSysTimingActiveReference_Type.__name__ = "Integer32"
_TnSysTimingActiveReference_Object = MibScalar
tnSysTimingActiveReference = _TnSysTimingActiveReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 11),
    _TnSysTimingActiveReference_Type()
)
tnSysTimingActiveReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingActiveReference.setStatus("current")


class _TnSysTimingClockingMode_Type(Integer32):
    """Custom type tnSysTimingClockingMode based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("normal", 2),
          ("fastStart", 3),
          ("holdOver", 4),
          ("freeRun", 5))
    )


_TnSysTimingClockingMode_Type.__name__ = "Integer32"
_TnSysTimingClockingMode_Object = MibScalar
tnSysTimingClockingMode = _TnSysTimingClockingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 12),
    _TnSysTimingClockingMode_Type()
)
tnSysTimingClockingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingClockingMode.setStatus("current")


class _TnSysTimingSwitchingMode_Type(Integer32):
    """Custom type tnSysTimingSwitchingMode based on Integer32"""
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
        *(("unknown", 1),
          ("revertive", 2),
          ("nonRevertive", 3))
    )


_TnSysTimingSwitchingMode_Type.__name__ = "Integer32"
_TnSysTimingSwitchingMode_Object = MibScalar
tnSysTimingSwitchingMode = _TnSysTimingSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 13),
    _TnSysTimingSwitchingMode_Type()
)
tnSysTimingSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingSwitchingMode.setStatus("current")


class _TnSysTimingFreeRunSuppressAlarms_Type(TruthValue):
    """Custom type tnSysTimingFreeRunSuppressAlarms based on TruthValue"""
    defaultValue = 2


_TnSysTimingFreeRunSuppressAlarms_Type.__name__ = "TruthValue"
_TnSysTimingFreeRunSuppressAlarms_Object = MibScalar
tnSysTimingFreeRunSuppressAlarms = _TnSysTimingFreeRunSuppressAlarms_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 14),
    _TnSysTimingFreeRunSuppressAlarms_Type()
)
tnSysTimingFreeRunSuppressAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingFreeRunSuppressAlarms.setStatus("current")


class _TnSysTimingDs1FramingMode_Type(Integer32):
    """Custom type tnSysTimingDs1FramingMode based on Integer32"""
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
        *(("unknown", 1),
          ("sf", 2),
          ("esf", 3))
    )


_TnSysTimingDs1FramingMode_Type.__name__ = "Integer32"
_TnSysTimingDs1FramingMode_Object = MibScalar
tnSysTimingDs1FramingMode = _TnSysTimingDs1FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 15),
    _TnSysTimingDs1FramingMode_Type()
)
tnSysTimingDs1FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingDs1FramingMode.setStatus("current")


class _TnSysTimingDs1LineCoding_Type(Integer32):
    """Custom type tnSysTimingDs1LineCoding based on Integer32"""
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
        *(("unknown", 1),
          ("ami", 2),
          ("b8zs", 3))
    )


_TnSysTimingDs1LineCoding_Type.__name__ = "Integer32"
_TnSysTimingDs1LineCoding_Object = MibScalar
tnSysTimingDs1LineCoding = _TnSysTimingDs1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 16),
    _TnSysTimingDs1LineCoding_Type()
)
tnSysTimingDs1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingDs1LineCoding.setStatus("current")


class _TnSysTimingDs1SsmProcessing_Type(AluWdmEnabledDisabled):
    """Custom type tnSysTimingDs1SsmProcessing based on AluWdmEnabledDisabled"""
    defaultValue = 1


_TnSysTimingDs1SsmProcessing_Type.__name__ = "AluWdmEnabledDisabled"
_TnSysTimingDs1SsmProcessing_Object = MibScalar
tnSysTimingDs1SsmProcessing = _TnSysTimingDs1SsmProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 17),
    _TnSysTimingDs1SsmProcessing_Type()
)
tnSysTimingDs1SsmProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingDs1SsmProcessing.setStatus("current")


class _TnSysTimingBitsAClockQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingBitsAClockQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingBitsAClockQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingBitsAClockQuality_Object = MibScalar
tnSysTimingBitsAClockQuality = _TnSysTimingBitsAClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 18),
    _TnSysTimingBitsAClockQuality_Type()
)
tnSysTimingBitsAClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingBitsAClockQuality.setStatus("current")


class _TnSysTimingBitsBClockQuality_Type(TropicSysTimingReferenceQuality):
    """Custom type tnSysTimingBitsBClockQuality based on TropicSysTimingReferenceQuality"""
    defaultValue = 1


_TnSysTimingBitsBClockQuality_Type.__name__ = "TropicSysTimingReferenceQuality"
_TnSysTimingBitsBClockQuality_Object = MibScalar
tnSysTimingBitsBClockQuality = _TnSysTimingBitsBClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 19),
    _TnSysTimingBitsBClockQuality_Type()
)
tnSysTimingBitsBClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingBitsBClockQuality.setStatus("current")


class _TnSysTimingActiveLineTimingCable_Type(Integer32):
    """Custom type tnSysTimingActiveLineTimingCable based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("notApplicable", 2),
          ("none", 3),
          ("a", 4),
          ("b", 5))
    )


_TnSysTimingActiveLineTimingCable_Type.__name__ = "Integer32"
_TnSysTimingActiveLineTimingCable_Object = MibScalar
tnSysTimingActiveLineTimingCable = _TnSysTimingActiveLineTimingCable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 20),
    _TnSysTimingActiveLineTimingCable_Type()
)
tnSysTimingActiveLineTimingCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingActiveLineTimingCable.setStatus("current")


class _TnSysTimingBitSourceType_Type(Integer32):
    """Custom type tnSysTimingBitSourceType based on Integer32"""
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
        *(("unknown", 1),
          ("ds1", 2),
          ("e1", 3))
    )


_TnSysTimingBitSourceType_Type.__name__ = "Integer32"
_TnSysTimingBitSourceType_Object = MibScalar
tnSysTimingBitSourceType = _TnSysTimingBitSourceType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 21),
    _TnSysTimingBitSourceType_Type()
)
tnSysTimingBitSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTimingBitSourceType.setStatus("current")


class _TnSysTimingBitsAModuleType_Type(Integer32):
    """Custom type tnSysTimingBitsAModuleType based on Integer32"""
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
        *(("unknown", 1),
          ("ds1", 2),
          ("e1", 3))
    )


_TnSysTimingBitsAModuleType_Type.__name__ = "Integer32"
_TnSysTimingBitsAModuleType_Object = MibScalar
tnSysTimingBitsAModuleType = _TnSysTimingBitsAModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 22),
    _TnSysTimingBitsAModuleType_Type()
)
tnSysTimingBitsAModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingBitsAModuleType.setStatus("current")


class _TnSysTimingBitsBModuleType_Type(Integer32):
    """Custom type tnSysTimingBitsBModuleType based on Integer32"""
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
        *(("unknown", 1),
          ("ds1", 2),
          ("e1", 3))
    )


_TnSysTimingBitsBModuleType_Type.__name__ = "Integer32"
_TnSysTimingBitsBModuleType_Object = MibScalar
tnSysTimingBitsBModuleType = _TnSysTimingBitsBModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 11, 23),
    _TnSysTimingBitsBModuleType_Type()
)
tnSysTimingBitsBModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTimingBitsBModuleType.setStatus("current")
_TnSysFeatures_ObjectIdentity = ObjectIdentity
tnSysFeatures = _TnSysFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12)
)


class _TnSysFeatureAutoTopology_Type(TruthValue):
    """Custom type tnSysFeatureAutoTopology based on TruthValue"""
    defaultValue = 2


_TnSysFeatureAutoTopology_Type.__name__ = "TruthValue"
_TnSysFeatureAutoTopology_Object = MibScalar
tnSysFeatureAutoTopology = _TnSysFeatureAutoTopology_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 3),
    _TnSysFeatureAutoTopology_Type()
)
tnSysFeatureAutoTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureAutoTopology.setStatus("current")


class _TnSysFeaturePauseFlowControl_Type(Integer32):
    """Custom type tnSysFeaturePauseFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("negotiated", 2))
    )


_TnSysFeaturePauseFlowControl_Type.__name__ = "Integer32"
_TnSysFeaturePauseFlowControl_Object = MibScalar
tnSysFeaturePauseFlowControl = _TnSysFeaturePauseFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 4),
    _TnSysFeaturePauseFlowControl_Type()
)
tnSysFeaturePauseFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeaturePauseFlowControl.setStatus("current")


class _TnSysFeatureIpUtilitiesRestricted_Type(TruthValue):
    """Custom type tnSysFeatureIpUtilitiesRestricted based on TruthValue"""
    defaultValue = 2


_TnSysFeatureIpUtilitiesRestricted_Type.__name__ = "TruthValue"
_TnSysFeatureIpUtilitiesRestricted_Object = MibScalar
tnSysFeatureIpUtilitiesRestricted = _TnSysFeatureIpUtilitiesRestricted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 5),
    _TnSysFeatureIpUtilitiesRestricted_Type()
)
tnSysFeatureIpUtilitiesRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureIpUtilitiesRestricted.setStatus("current")


class _TnSysFeatureFastServiceSetup_Type(TruthValue):
    """Custom type tnSysFeatureFastServiceSetup based on TruthValue"""
    defaultValue = 2


_TnSysFeatureFastServiceSetup_Type.__name__ = "TruthValue"
_TnSysFeatureFastServiceSetup_Object = MibScalar
tnSysFeatureFastServiceSetup = _TnSysFeatureFastServiceSetup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 12, 6),
    _TnSysFeatureFastServiceSetup_Type()
)
tnSysFeatureFastServiceSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFeatureFastServiceSetup.setStatus("current")
_TnSysFaultCorrelation_ObjectIdentity = ObjectIdentity
tnSysFaultCorrelation = _TnSysFaultCorrelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 13)
)
_TnSysFaultCorrelationTransientSuppression_Type = AluWdmEnabledDisabled
_TnSysFaultCorrelationTransientSuppression_Object = MibScalar
tnSysFaultCorrelationTransientSuppression = _TnSysFaultCorrelationTransientSuppression_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 13, 1),
    _TnSysFaultCorrelationTransientSuppression_Type()
)
tnSysFaultCorrelationTransientSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFaultCorrelationTransientSuppression.setStatus("current")
_TnSysErrorHandling_ObjectIdentity = ObjectIdentity
tnSysErrorHandling = _TnSysErrorHandling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 14)
)


class _TnSysSetRequestErrorMessage_Type(SnmpAdminString):
    """Custom type tnSysSetRequestErrorMessage based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysSetRequestErrorMessage_Type.__name__ = "SnmpAdminString"
_TnSysSetRequestErrorMessage_Object = MibScalar
tnSysSetRequestErrorMessage = _TnSysSetRequestErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 14, 1),
    _TnSysSetRequestErrorMessage_Type()
)
tnSysSetRequestErrorMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSetRequestErrorMessage.setStatus("current")
_TnSysSecurity_ObjectIdentity = ObjectIdentity
tnSysSecurity = _TnSysSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15)
)


class _TnSysSecurityMode_Type(Integer32):
    """Custom type tnSysSecurityMode based on Integer32"""
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
        *(("normal", 1),
          ("encrypted", 2),
          ("fips", 3),
          ("anssi", 4))
    )


_TnSysSecurityMode_Type.__name__ = "Integer32"
_TnSysSecurityMode_Object = MibScalar
tnSysSecurityMode = _TnSysSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 1),
    _TnSysSecurityMode_Type()
)
tnSysSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSecurityMode.setStatus("current")
_TnSysSsh_ObjectIdentity = ObjectIdentity
tnSysSsh = _TnSysSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2)
)


class _TnSysSshKeyType_Type(Integer32):
    """Custom type tnSysSshKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dsa", 1)
    )


_TnSysSshKeyType_Type.__name__ = "Integer32"
_TnSysSshKeyType_Object = MibScalar
tnSysSshKeyType = _TnSysSshKeyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 1),
    _TnSysSshKeyType_Type()
)
tnSysSshKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshKeyType.setStatus("current")


class _TnSysSshKeyModulus_Type(Unsigned32):
    """Custom type tnSysSshKeyModulus based on Unsigned32"""
    defaultValue = 1024


_TnSysSshKeyModulus_Type.__name__ = "Unsigned32"
_TnSysSshKeyModulus_Object = MibScalar
tnSysSshKeyModulus = _TnSysSshKeyModulus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 2),
    _TnSysSshKeyModulus_Type()
)
tnSysSshKeyModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshKeyModulus.setStatus("current")


class _TnSysSshPublicKey_Type(OctetString):
    """Custom type tnSysSshPublicKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_TnSysSshPublicKey_Type.__name__ = "OctetString"
_TnSysSshPublicKey_Object = MibScalar
tnSysSshPublicKey = _TnSysSshPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 3),
    _TnSysSshPublicKey_Type()
)
tnSysSshPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSshPublicKey.setStatus("current")


class _TnSysSshKeyCommand_Type(Integer32):
    """Custom type tnSysSshKeyCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("generate", 2),
          ("delete", 3))
    )


_TnSysSshKeyCommand_Type.__name__ = "Integer32"
_TnSysSshKeyCommand_Object = MibScalar
tnSysSshKeyCommand = _TnSysSshKeyCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 4),
    _TnSysSshKeyCommand_Type()
)
tnSysSshKeyCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSshKeyCommand.setStatus("current")


class _TnSysSshKeyGenerationStatus_Type(Integer32):
    """Custom type tnSysSshKeyGenerationStatus based on Integer32"""
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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3))
    )


_TnSysSshKeyGenerationStatus_Type.__name__ = "Integer32"
_TnSysSshKeyGenerationStatus_Object = MibScalar
tnSysSshKeyGenerationStatus = _TnSysSshKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 2, 5),
    _TnSysSshKeyGenerationStatus_Type()
)
tnSysSshKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSshKeyGenerationStatus.setStatus("current")
_TnSysSsl_ObjectIdentity = ObjectIdentity
tnSysSsl = _TnSysSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3)
)


class _TnSysSslKeyType_Type(Integer32):
    """Custom type tnSysSslKeyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 1),
          ("rsa", 2))
    )


_TnSysSslKeyType_Type.__name__ = "Integer32"
_TnSysSslKeyType_Object = MibScalar
tnSysSslKeyType = _TnSysSslKeyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 1),
    _TnSysSslKeyType_Type()
)
tnSysSslKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslKeyType.setStatus("current")


class _TnSysSslKeyModulus_Type(Unsigned32):
    """Custom type tnSysSslKeyModulus based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_TnSysSslKeyModulus_Type.__name__ = "Unsigned32"
_TnSysSslKeyModulus_Object = MibScalar
tnSysSslKeyModulus = _TnSysSslKeyModulus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 2),
    _TnSysSslKeyModulus_Type()
)
tnSysSslKeyModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslKeyModulus.setStatus("current")


class _TnSysSslPublicKey_Type(OctetString):
    """Custom type tnSysSslPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_TnSysSslPublicKey_Type.__name__ = "OctetString"
_TnSysSslPublicKey_Object = MibScalar
tnSysSslPublicKey = _TnSysSslPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 3),
    _TnSysSslPublicKey_Type()
)
tnSysSslPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslPublicKey.setStatus("current")


class _TnSysSslKeyCommand_Type(Integer32):
    """Custom type tnSysSslKeyCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("generate", 2))
    )


_TnSysSslKeyCommand_Type.__name__ = "Integer32"
_TnSysSslKeyCommand_Object = MibScalar
tnSysSslKeyCommand = _TnSysSslKeyCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 4),
    _TnSysSslKeyCommand_Type()
)
tnSysSslKeyCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslKeyCommand.setStatus("current")


class _TnSysSslKeyGenerationStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslKeyGenerationStatus based on AluWdmSslOperationStatus"""
    defaultValue = 1


_TnSysSslKeyGenerationStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslKeyGenerationStatus_Object = MibScalar
tnSysSslKeyGenerationStatus = _TnSysSslKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 5),
    _TnSysSslKeyGenerationStatus_Type()
)
tnSysSslKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslKeyGenerationStatus.setStatus("current")


class _TnSysSslCertTransferCommand_Type(Integer32):
    """Custom type tnSysSslCertTransferCommand based on Integer32"""
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
        *(("noCmd", 1),
          ("uploadReq", 2),
          ("downloadCert", 3))
    )


_TnSysSslCertTransferCommand_Type.__name__ = "Integer32"
_TnSysSslCertTransferCommand_Object = MibScalar
tnSysSslCertTransferCommand = _TnSysSslCertTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 6),
    _TnSysSslCertTransferCommand_Type()
)
tnSysSslCertTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferCommand.setStatus("current")


class _TnSysSslCertTransferProtocol_Type(Integer32):
    """Custom type tnSysSslCertTransferProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_TnSysSslCertTransferProtocol_Type.__name__ = "Integer32"
_TnSysSslCertTransferProtocol_Object = MibScalar
tnSysSslCertTransferProtocol = _TnSysSslCertTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 8),
    _TnSysSslCertTransferProtocol_Type()
)
tnSysSslCertTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferProtocol.setStatus("current")
_TnSysSslCertTransferRemoteIp_Type = IpAddress
_TnSysSslCertTransferRemoteIp_Object = MibScalar
tnSysSslCertTransferRemoteIp = _TnSysSslCertTransferRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 9),
    _TnSysSslCertTransferRemoteIp_Type()
)
tnSysSslCertTransferRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemoteIp.setStatus("current")


class _TnSysSslCertTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysSslCertTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysSslCertTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysSslCertTransferRemotePath_Object = MibScalar
tnSysSslCertTransferRemotePath = _TnSysSslCertTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 10),
    _TnSysSslCertTransferRemotePath_Type()
)
tnSysSslCertTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemotePath.setStatus("current")


class _TnSysSslCertTransferRemoteUserId_Type(SnmpAdminString):
    """Custom type tnSysSslCertTransferRemoteUserId based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysSslCertTransferRemoteUserId_Type.__name__ = "SnmpAdminString"
_TnSysSslCertTransferRemoteUserId_Object = MibScalar
tnSysSslCertTransferRemoteUserId = _TnSysSslCertTransferRemoteUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 11),
    _TnSysSslCertTransferRemoteUserId_Type()
)
tnSysSslCertTransferRemoteUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemoteUserId.setStatus("current")


class _TnSysSslCertTransferRemotePassword_Type(SnmpAdminString):
    """Custom type tnSysSslCertTransferRemotePassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysSslCertTransferRemotePassword_Type.__name__ = "SnmpAdminString"
_TnSysSslCertTransferRemotePassword_Object = MibScalar
tnSysSslCertTransferRemotePassword = _TnSysSslCertTransferRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 12),
    _TnSysSslCertTransferRemotePassword_Type()
)
tnSysSslCertTransferRemotePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertTransferRemotePassword.setStatus("current")


class _TnSysSslCsrCommand_Type(Integer32):
    """Custom type tnSysSslCsrCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("generate", 2))
    )


_TnSysSslCsrCommand_Type.__name__ = "Integer32"
_TnSysSslCsrCommand_Object = MibScalar
tnSysSslCsrCommand = _TnSysSslCsrCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 13),
    _TnSysSslCsrCommand_Type()
)
tnSysSslCsrCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrCommand.setStatus("current")


class _TnSysSslCsrCountry_Type(SnmpAdminString):
    """Custom type tnSysSslCsrCountry based on SnmpAdminString"""
    defaultValue = OctetString("IT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TnSysSslCsrCountry_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrCountry_Object = MibScalar
tnSysSslCsrCountry = _TnSysSslCsrCountry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 14),
    _TnSysSslCsrCountry_Type()
)
tnSysSslCsrCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrCountry.setStatus("current")


class _TnSysSslCsrState_Type(SnmpAdminString):
    """Custom type tnSysSslCsrState based on SnmpAdminString"""
    defaultValue = OctetString("Italy")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysSslCsrState_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrState_Object = MibScalar
tnSysSslCsrState = _TnSysSslCsrState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 15),
    _TnSysSslCsrState_Type()
)
tnSysSslCsrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrState.setStatus("current")


class _TnSysSslCsrLocality_Type(SnmpAdminString):
    """Custom type tnSysSslCsrLocality based on SnmpAdminString"""
    defaultValue = OctetString("Milan")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysSslCsrLocality_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrLocality_Object = MibScalar
tnSysSslCsrLocality = _TnSysSslCsrLocality_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 16),
    _TnSysSslCsrLocality_Type()
)
tnSysSslCsrLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrLocality.setStatus("current")


class _TnSysSslCsrOrganization_Type(SnmpAdminString):
    """Custom type tnSysSslCsrOrganization based on SnmpAdminString"""
    defaultValue = OctetString("Nokia")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysSslCsrOrganization_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrOrganization_Object = MibScalar
tnSysSslCsrOrganization = _TnSysSslCsrOrganization_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 17),
    _TnSysSslCsrOrganization_Type()
)
tnSysSslCsrOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrOrganization.setStatus("current")


class _TnSysSslCsrOrganizationUnit_Type(SnmpAdminString):
    """Custom type tnSysSslCsrOrganizationUnit based on SnmpAdminString"""
    defaultValue = OctetString("Optics Division")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysSslCsrOrganizationUnit_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrOrganizationUnit_Object = MibScalar
tnSysSslCsrOrganizationUnit = _TnSysSslCsrOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 18),
    _TnSysSslCsrOrganizationUnit_Type()
)
tnSysSslCsrOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrOrganizationUnit.setStatus("current")


class _TnSysSslCsrCommonName_Type(SnmpAdminString):
    """Custom type tnSysSslCsrCommonName based on SnmpAdminString"""
    defaultValue = OctetString("1830 Domain")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnSysSslCsrCommonName_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrCommonName_Object = MibScalar
tnSysSslCsrCommonName = _TnSysSslCsrCommonName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 19),
    _TnSysSslCsrCommonName_Type()
)
tnSysSslCsrCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrCommonName.setStatus("current")


class _TnSysSslCsrEmailAddress_Type(SnmpAdminString):
    """Custom type tnSysSslCsrEmailAddress based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysSslCsrEmailAddress_Type.__name__ = "SnmpAdminString"
_TnSysSslCsrEmailAddress_Object = MibScalar
tnSysSslCsrEmailAddress = _TnSysSslCsrEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 20),
    _TnSysSslCsrEmailAddress_Type()
)
tnSysSslCsrEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCsrEmailAddress.setStatus("current")


class _TnSysSslCertCommand_Type(Integer32):
    """Custom type tnSysSslCertCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("install", 2))
    )


_TnSysSslCertCommand_Type.__name__ = "Integer32"
_TnSysSslCertCommand_Object = MibScalar
tnSysSslCertCommand = _TnSysSslCertCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 21),
    _TnSysSslCertCommand_Type()
)
tnSysSslCertCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysSslCertCommand.setStatus("current")


class _TnSysSslCertSignatureAlgorithm_Type(SnmpAdminString):
    """Custom type tnSysSslCertSignatureAlgorithm based on SnmpAdminString"""
    defaultValue = OctetString("md5WithRSAEncryption")


_TnSysSslCertSignatureAlgorithm_Type.__name__ = "SnmpAdminString"
_TnSysSslCertSignatureAlgorithm_Object = MibScalar
tnSysSslCertSignatureAlgorithm = _TnSysSslCertSignatureAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 22),
    _TnSysSslCertSignatureAlgorithm_Type()
)
tnSysSslCertSignatureAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertSignatureAlgorithm.setStatus("current")


class _TnSysSslCertValidity_Type(SnmpAdminString):
    """Custom type tnSysSslCertValidity based on SnmpAdminString"""
    defaultValue = OctetString("Apr 14 06:03:04 2011 GMT - Apr 11 06:03:04 2021 GMT")


_TnSysSslCertValidity_Type.__name__ = "SnmpAdminString"
_TnSysSslCertValidity_Object = MibScalar
tnSysSslCertValidity = _TnSysSslCertValidity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 23),
    _TnSysSslCertValidity_Type()
)
tnSysSslCertValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertValidity.setStatus("current")


class _TnSysSslCsrUploadStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslCsrUploadStatus based on AluWdmSslOperationStatus"""
    defaultValue = 4


_TnSysSslCsrUploadStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslCsrUploadStatus_Object = MibScalar
tnSysSslCsrUploadStatus = _TnSysSslCsrUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 24),
    _TnSysSslCsrUploadStatus_Type()
)
tnSysSslCsrUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCsrUploadStatus.setStatus("current")


class _TnSysSslCertDownloadStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslCertDownloadStatus based on AluWdmSslOperationStatus"""
    defaultValue = 4


_TnSysSslCertDownloadStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslCertDownloadStatus_Object = MibScalar
tnSysSslCertDownloadStatus = _TnSysSslCertDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 25),
    _TnSysSslCertDownloadStatus_Type()
)
tnSysSslCertDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertDownloadStatus.setStatus("current")


class _TnSysSslCertInstallStatus_Type(AluWdmSslOperationStatus):
    """Custom type tnSysSslCertInstallStatus based on AluWdmSslOperationStatus"""
    defaultValue = 1


_TnSysSslCertInstallStatus_Type.__name__ = "AluWdmSslOperationStatus"
_TnSysSslCertInstallStatus_Object = MibScalar
tnSysSslCertInstallStatus = _TnSysSslCertInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 26),
    _TnSysSslCertInstallStatus_Type()
)
tnSysSslCertInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCertInstallStatus.setStatus("current")


class _TnSysSslCsrGenerationStatus_Type(Integer32):
    """Custom type tnSysSslCsrGenerationStatus based on Integer32"""
    defaultValue = 4

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
        *(("completed", 1),
          ("inProgress", 2),
          ("failed", 3),
          ("none", 4),
          ("editing", 5))
    )


_TnSysSslCsrGenerationStatus_Type.__name__ = "Integer32"
_TnSysSslCsrGenerationStatus_Object = MibScalar
tnSysSslCsrGenerationStatus = _TnSysSslCsrGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 3, 27),
    _TnSysSslCsrGenerationStatus_Type()
)
tnSysSslCsrGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysSslCsrGenerationStatus.setStatus("current")
_TnSysKey_ObjectIdentity = ObjectIdentity
tnSysKey = _TnSysKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4)
)
_TnSshKeyAttributeTotal_Type = Integer32
_TnSshKeyAttributeTotal_Object = MibScalar
tnSshKeyAttributeTotal = _TnSshKeyAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 1),
    _TnSshKeyAttributeTotal_Type()
)
tnSshKeyAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshKeyAttributeTotal.setStatus("current")
_TnSshKeyTable_Object = MibTable
tnSshKeyTable = _TnSshKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2)
)
if mibBuilder.loadTexts:
    tnSshKeyTable.setStatus("current")
_TnSshKeyEntry_Object = MibTableRow
tnSshKeyEntry = _TnSshKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1)
)
tnSshKeyEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSshKeyTypeIndex"),
)
if mibBuilder.loadTexts:
    tnSshKeyEntry.setStatus("current")


class _TnSshKeyTypeIndex_Type(Integer32):
    """Custom type tnSshKeyTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 1),
          ("rsa", 2))
    )


_TnSshKeyTypeIndex_Type.__name__ = "Integer32"
_TnSshKeyTypeIndex_Object = MibTableColumn
tnSshKeyTypeIndex = _TnSshKeyTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 1),
    _TnSshKeyTypeIndex_Type()
)
tnSshKeyTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSshKeyTypeIndex.setStatus("current")


class _TnSshPublicKey_Type(OctetString):
    """Custom type tnSshPublicKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_TnSshPublicKey_Type.__name__ = "OctetString"
_TnSshPublicKey_Object = MibTableColumn
tnSshPublicKey = _TnSshPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 15, 4, 2, 1, 2),
    _TnSshPublicKey_Type()
)
tnSshPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSshPublicKey.setStatus("current")
_TnSysTransferLog_ObjectIdentity = ObjectIdentity
tnSysTransferLog = _TnSysTransferLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16)
)


class _TnSysTransferLogCommand_Type(Integer32):
    """Custom type tnSysTransferLogCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysTransferLogCommand_Type.__name__ = "Integer32"
_TnSysTransferLogCommand_Object = MibScalar
tnSysTransferLogCommand = _TnSysTransferLogCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 1),
    _TnSysTransferLogCommand_Type()
)
tnSysTransferLogCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogCommand.setStatus("current")
_TnSysTransferLogRemoteHostIp_Type = IpAddress
_TnSysTransferLogRemoteHostIp_Object = MibScalar
tnSysTransferLogRemoteHostIp = _TnSysTransferLogRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 2),
    _TnSysTransferLogRemoteHostIp_Type()
)
tnSysTransferLogRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemoteHostIp.setStatus("current")


class _TnSysTransferLogRemotePath_Type(SnmpAdminString):
    """Custom type tnSysTransferLogRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysTransferLogRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogRemotePath_Object = MibScalar
tnSysTransferLogRemotePath = _TnSysTransferLogRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 3),
    _TnSysTransferLogRemotePath_Type()
)
tnSysTransferLogRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemotePath.setStatus("current")


class _TnSysTransferLogType_Type(Integer32):
    """Custom type tnSysTransferLogType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("snmp", 2),
          ("ual", 3),
          ("alarm", 4),
          ("user", 5),
          ("secu", 6),
          ("other", 7),
          ("ualPartial", 8))
    )


_TnSysTransferLogType_Type.__name__ = "Integer32"
_TnSysTransferLogType_Object = MibScalar
tnSysTransferLogType = _TnSysTransferLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 4),
    _TnSysTransferLogType_Type()
)
tnSysTransferLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogType.setStatus("current")


class _TnSysTransferLogStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysTransferLogStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysTransferLogStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysTransferLogStatus_Object = MibScalar
tnSysTransferLogStatus = _TnSysTransferLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 5),
    _TnSysTransferLogStatus_Type()
)
tnSysTransferLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogStatus.setStatus("current")


class _TnSysTransferLogLastLogFilename_Type(SnmpAdminString):
    """Custom type tnSysTransferLogLastLogFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysTransferLogLastLogFilename_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogLastLogFilename_Object = MibScalar
tnSysTransferLogLastLogFilename = _TnSysTransferLogLastLogFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 6),
    _TnSysTransferLogLastLogFilename_Type()
)
tnSysTransferLogLastLogFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogLastLogFilename.setStatus("current")


class _TnSysTransferLogLastCommand_Type(Integer32):
    """Custom type tnSysTransferLogLastCommand based on Integer32"""
    defaultValue = 1

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
        *(("noCommand", 1),
          ("unknown", 2),
          ("ual", 3),
          ("snmp", 4),
          ("ualPartial", 5))
    )


_TnSysTransferLogLastCommand_Type.__name__ = "Integer32"
_TnSysTransferLogLastCommand_Object = MibScalar
tnSysTransferLogLastCommand = _TnSysTransferLogLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 7),
    _TnSysTransferLogLastCommand_Type()
)
tnSysTransferLogLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogLastCommand.setStatus("current")


class _TnSysTransferLogLastFileTimeStamp_Type(Unsigned32):
    """Custom type tnSysTransferLogLastFileTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysTransferLogLastFileTimeStamp_Type.__name__ = "Unsigned32"
_TnSysTransferLogLastFileTimeStamp_Object = MibScalar
tnSysTransferLogLastFileTimeStamp = _TnSysTransferLogLastFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 8),
    _TnSysTransferLogLastFileTimeStamp_Type()
)
tnSysTransferLogLastFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTransferLogLastFileTimeStamp.setStatus("current")


class _TnSysTransferLogProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysTransferLogProtocol based on AluWdmTransferProtocol"""
    defaultValue = 1


_TnSysTransferLogProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysTransferLogProtocol_Object = MibScalar
tnSysTransferLogProtocol = _TnSysTransferLogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 9),
    _TnSysTransferLogProtocol_Type()
)
tnSysTransferLogProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogProtocol.setStatus("current")


class _TnSysTransferLogUserId_Type(SnmpAdminString):
    """Custom type tnSysTransferLogUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysTransferLogUserId_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogUserId_Object = MibScalar
tnSysTransferLogUserId = _TnSysTransferLogUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 10),
    _TnSysTransferLogUserId_Type()
)
tnSysTransferLogUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogUserId.setStatus("current")


class _TnSysTransferLogPassword_Type(SnmpAdminString):
    """Custom type tnSysTransferLogPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysTransferLogPassword_Type.__name__ = "SnmpAdminString"
_TnSysTransferLogPassword_Object = MibScalar
tnSysTransferLogPassword = _TnSysTransferLogPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 11),
    _TnSysTransferLogPassword_Type()
)
tnSysTransferLogPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogPassword.setStatus("current")


class _TnSysTransferLogWindowStart_Type(Unsigned32):
    """Custom type tnSysTransferLogWindowStart based on Unsigned32"""
    defaultValue = 0


_TnSysTransferLogWindowStart_Type.__name__ = "Unsigned32"
_TnSysTransferLogWindowStart_Object = MibScalar
tnSysTransferLogWindowStart = _TnSysTransferLogWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 12),
    _TnSysTransferLogWindowStart_Type()
)
tnSysTransferLogWindowStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogWindowStart.setStatus("current")


class _TnSysTransferLogWindowStop_Type(Unsigned32):
    """Custom type tnSysTransferLogWindowStop based on Unsigned32"""
    defaultValue = 0


_TnSysTransferLogWindowStop_Type.__name__ = "Unsigned32"
_TnSysTransferLogWindowStop_Object = MibScalar
tnSysTransferLogWindowStop = _TnSysTransferLogWindowStop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 13),
    _TnSysTransferLogWindowStop_Type()
)
tnSysTransferLogWindowStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogWindowStop.setStatus("current")


class _TnSysTransferLogRemoteHostInetAddressType_Type(InetAddressType):
    """Custom type tnSysTransferLogRemoteHostInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysTransferLogRemoteHostInetAddressType_Type.__name__ = "InetAddressType"
_TnSysTransferLogRemoteHostInetAddressType_Object = MibScalar
tnSysTransferLogRemoteHostInetAddressType = _TnSysTransferLogRemoteHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 14),
    _TnSysTransferLogRemoteHostInetAddressType_Type()
)
tnSysTransferLogRemoteHostInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemoteHostInetAddressType.setStatus("current")


class _TnSysTransferLogRemoteHostInetAddress_Type(InetAddress):
    """Custom type tnSysTransferLogRemoteHostInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysTransferLogRemoteHostInetAddress_Type.__name__ = "InetAddress"
_TnSysTransferLogRemoteHostInetAddress_Object = MibScalar
tnSysTransferLogRemoteHostInetAddress = _TnSysTransferLogRemoteHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 16, 15),
    _TnSysTransferLogRemoteHostInetAddress_Type()
)
tnSysTransferLogRemoteHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysTransferLogRemoteHostInetAddress.setStatus("current")
_TnSysAccessControlList_ObjectIdentity = ObjectIdentity
tnSysAccessControlList = _TnSysAccessControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17)
)
_TnSysIpAclSysDefault_ObjectIdentity = ObjectIdentity
tnSysIpAclSysDefault = _TnSysIpAclSysDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1)
)


class _TnSysIpAclRxAction_Type(Integer32):
    """Custom type tnSysIpAclRxAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclRxAction_Type.__name__ = "Integer32"
_TnSysIpAclRxAction_Object = MibScalar
tnSysIpAclRxAction = _TnSysIpAclRxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 1),
    _TnSysIpAclRxAction_Type()
)
tnSysIpAclRxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclRxAction.setStatus("current")


class _TnSysIpAclTxAction_Type(Integer32):
    """Custom type tnSysIpAclTxAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclTxAction_Type.__name__ = "Integer32"
_TnSysIpAclTxAction_Object = MibScalar
tnSysIpAclTxAction = _TnSysIpAclTxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 2),
    _TnSysIpAclTxAction_Type()
)
tnSysIpAclTxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclTxAction.setStatus("current")


class _TnSysIpAclSnmpCfgEnable_Type(TruthValue):
    """Custom type tnSysIpAclSnmpCfgEnable based on TruthValue"""
    defaultValue = 2


_TnSysIpAclSnmpCfgEnable_Type.__name__ = "TruthValue"
_TnSysIpAclSnmpCfgEnable_Object = MibScalar
tnSysIpAclSnmpCfgEnable = _TnSysIpAclSnmpCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 3),
    _TnSysIpAclSnmpCfgEnable_Type()
)
tnSysIpAclSnmpCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclSnmpCfgEnable.setStatus("current")


class _TnSysIpAclCfgRestoreToDefault_Type(TruthValue):
    """Custom type tnSysIpAclCfgRestoreToDefault based on TruthValue"""
    defaultValue = 2


_TnSysIpAclCfgRestoreToDefault_Type.__name__ = "TruthValue"
_TnSysIpAclCfgRestoreToDefault_Object = MibScalar
tnSysIpAclCfgRestoreToDefault = _TnSysIpAclCfgRestoreToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 1, 4),
    _TnSysIpAclCfgRestoreToDefault_Type()
)
tnSysIpAclCfgRestoreToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclCfgRestoreToDefault.setStatus("current")
_TnSysIpAclPatternAttributeTotal_Type = Integer32
_TnSysIpAclPatternAttributeTotal_Object = MibScalar
tnSysIpAclPatternAttributeTotal = _TnSysIpAclPatternAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 2),
    _TnSysIpAclPatternAttributeTotal_Type()
)
tnSysIpAclPatternAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclPatternAttributeTotal.setStatus("current")
_TnSysIpAclPatternTable_Object = MibTable
tnSysIpAclPatternTable = _TnSysIpAclPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternTable.setStatus("current")
_TnSysIpAclPatternEntry_Object = MibTableRow
tnSysIpAclPatternEntry = _TnSysIpAclPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1)
)
tnSysIpAclPatternEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclPatternID"),
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternEntry.setStatus("current")


class _TnSysIpAclPatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclPatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclPatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclPatternID_Object = MibTableColumn
tnSysIpAclPatternID = _TnSysIpAclPatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 1),
    _TnSysIpAclPatternID_Type()
)
tnSysIpAclPatternID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclPatternID.setStatus("current")


class _TnSysIpAclPatternAction_Type(Integer32):
    """Custom type tnSysIpAclPatternAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclPatternAction_Type.__name__ = "Integer32"
_TnSysIpAclPatternAction_Object = MibTableColumn
tnSysIpAclPatternAction = _TnSysIpAclPatternAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 2),
    _TnSysIpAclPatternAction_Type()
)
tnSysIpAclPatternAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternAction.setStatus("current")


class _TnSysIpAclPatternICMPERROR_Type(TruthValue):
    """Custom type tnSysIpAclPatternICMPERROR based on TruthValue"""
    defaultValue = 2


_TnSysIpAclPatternICMPERROR_Type.__name__ = "TruthValue"
_TnSysIpAclPatternICMPERROR_Object = MibTableColumn
tnSysIpAclPatternICMPERROR = _TnSysIpAclPatternICMPERROR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 3),
    _TnSysIpAclPatternICMPERROR_Type()
)
tnSysIpAclPatternICMPERROR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternICMPERROR.setStatus("current")
_TnSysIpAclPatternSrcAddr_Type = IpAddress
_TnSysIpAclPatternSrcAddr_Object = MibTableColumn
tnSysIpAclPatternSrcAddr = _TnSysIpAclPatternSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 4),
    _TnSysIpAclPatternSrcAddr_Type()
)
tnSysIpAclPatternSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcAddr.setStatus("current")


class _TnSysIpAclPatternSrcPrefix_Type(IpAddress):
    """Custom type tnSysIpAclPatternSrcPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysIpAclPatternSrcPrefix_Type.__name__ = "IpAddress"
_TnSysIpAclPatternSrcPrefix_Object = MibTableColumn
tnSysIpAclPatternSrcPrefix = _TnSysIpAclPatternSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 5),
    _TnSysIpAclPatternSrcPrefix_Type()
)
tnSysIpAclPatternSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcPrefix.setStatus("current")
_TnSysIpAclPatternDestAddr_Type = IpAddress
_TnSysIpAclPatternDestAddr_Object = MibTableColumn
tnSysIpAclPatternDestAddr = _TnSysIpAclPatternDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 6),
    _TnSysIpAclPatternDestAddr_Type()
)
tnSysIpAclPatternDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestAddr.setStatus("current")


class _TnSysIpAclPatternDestPrefix_Type(IpAddress):
    """Custom type tnSysIpAclPatternDestPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_TnSysIpAclPatternDestPrefix_Type.__name__ = "IpAddress"
_TnSysIpAclPatternDestPrefix_Object = MibTableColumn
tnSysIpAclPatternDestPrefix = _TnSysIpAclPatternDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 7),
    _TnSysIpAclPatternDestPrefix_Type()
)
tnSysIpAclPatternDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestPrefix.setStatus("current")


class _TnSysIpAclPatternDestPort_Type(Integer32):
    """Custom type tnSysIpAclPatternDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclPatternDestPort_Type.__name__ = "Integer32"
_TnSysIpAclPatternDestPort_Object = MibTableColumn
tnSysIpAclPatternDestPort = _TnSysIpAclPatternDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 8),
    _TnSysIpAclPatternDestPort_Type()
)
tnSysIpAclPatternDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternDestPort.setStatus("current")
_TnSysIpAclPatternIpProtocol_Type = OctetString
_TnSysIpAclPatternIpProtocol_Object = MibTableColumn
tnSysIpAclPatternIpProtocol = _TnSysIpAclPatternIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 9),
    _TnSysIpAclPatternIpProtocol_Type()
)
tnSysIpAclPatternIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIpProtocol.setStatus("current")


class _TnSysIpAclPatternIpFragment_Type(TruthValue):
    """Custom type tnSysIpAclPatternIpFragment based on TruthValue"""
    defaultValue = 2


_TnSysIpAclPatternIpFragment_Type.__name__ = "TruthValue"
_TnSysIpAclPatternIpFragment_Object = MibTableColumn
tnSysIpAclPatternIpFragment = _TnSysIpAclPatternIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 10),
    _TnSysIpAclPatternIpFragment_Type()
)
tnSysIpAclPatternIpFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIpFragment.setStatus("current")


class _TnSysIpAclPatternIcmpType_Type(Integer32):
    """Custom type tnSysIpAclPatternIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclPatternIcmpType_Type.__name__ = "Integer32"
_TnSysIpAclPatternIcmpType_Object = MibTableColumn
tnSysIpAclPatternIcmpType = _TnSysIpAclPatternIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 11),
    _TnSysIpAclPatternIcmpType_Type()
)
tnSysIpAclPatternIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIcmpType.setStatus("current")


class _TnSysIpAclPatternIcmpCode_Type(Integer32):
    """Custom type tnSysIpAclPatternIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclPatternIcmpCode_Type.__name__ = "Integer32"
_TnSysIpAclPatternIcmpCode_Object = MibTableColumn
tnSysIpAclPatternIcmpCode = _TnSysIpAclPatternIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 12),
    _TnSysIpAclPatternIcmpCode_Type()
)
tnSysIpAclPatternIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternIcmpCode.setStatus("current")
_TnSysIpAclPatternTcpEstablish_Type = TruthValue
_TnSysIpAclPatternTcpEstablish_Object = MibTableColumn
tnSysIpAclPatternTcpEstablish = _TnSysIpAclPatternTcpEstablish_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 13),
    _TnSysIpAclPatternTcpEstablish_Type()
)
tnSysIpAclPatternTcpEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternTcpEstablish.setStatus("current")
_TnSysIpAclPatternRowStatus_Type = RowStatus
_TnSysIpAclPatternRowStatus_Object = MibTableColumn
tnSysIpAclPatternRowStatus = _TnSysIpAclPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 14),
    _TnSysIpAclPatternRowStatus_Type()
)
tnSysIpAclPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternRowStatus.setStatus("current")


class _TnSysIpAclPatternSrcPort_Type(Integer32):
    """Custom type tnSysIpAclPatternSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclPatternSrcPort_Type.__name__ = "Integer32"
_TnSysIpAclPatternSrcPort_Object = MibTableColumn
tnSysIpAclPatternSrcPort = _TnSysIpAclPatternSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 15),
    _TnSysIpAclPatternSrcPort_Type()
)
tnSysIpAclPatternSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSrcPort.setStatus("current")
_TnSysIpAclPatternSystemDefault_Type = TruthValue
_TnSysIpAclPatternSystemDefault_Object = MibTableColumn
tnSysIpAclPatternSystemDefault = _TnSysIpAclPatternSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 3, 1, 16),
    _TnSysIpAclPatternSystemDefault_Type()
)
tnSysIpAclPatternSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclPatternSystemDefault.setStatus("current")
_TnSysIpAclFilterAttributeTotal_Type = Integer32
_TnSysIpAclFilterAttributeTotal_Object = MibScalar
tnSysIpAclFilterAttributeTotal = _TnSysIpAclFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 4),
    _TnSysIpAclFilterAttributeTotal_Type()
)
tnSysIpAclFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclFilterAttributeTotal.setStatus("current")
_TnSysIpAclFilterTable_Object = MibTable
tnSysIpAclFilterTable = _TnSysIpAclFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5)
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterTable.setStatus("current")
_TnSysIpAclFilterEntry_Object = MibTableRow
tnSysIpAclFilterEntry = _TnSysIpAclFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1)
)
tnSysIpAclFilterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclFilterID"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclFilterPatternIndex"),
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterEntry.setStatus("current")


class _TnSysIpAclFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclFilterID_Object = MibTableColumn
tnSysIpAclFilterID = _TnSysIpAclFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 1),
    _TnSysIpAclFilterID_Type()
)
tnSysIpAclFilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclFilterID.setStatus("current")


class _TnSysIpAclFilterPatternIndex_Type(Integer32):
    """Custom type tnSysIpAclFilterPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnSysIpAclFilterPatternIndex_Type.__name__ = "Integer32"
_TnSysIpAclFilterPatternIndex_Object = MibTableColumn
tnSysIpAclFilterPatternIndex = _TnSysIpAclFilterPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 2),
    _TnSysIpAclFilterPatternIndex_Type()
)
tnSysIpAclFilterPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclFilterPatternIndex.setStatus("current")


class _TnSysIpAclFilterPatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclFilterPatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclFilterPatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclFilterPatternID_Object = MibTableColumn
tnSysIpAclFilterPatternID = _TnSysIpAclFilterPatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 3),
    _TnSysIpAclFilterPatternID_Type()
)
tnSysIpAclFilterPatternID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclFilterPatternID.setStatus("current")
_TnSysIpAclFilterStatCount_Type = Counter32
_TnSysIpAclFilterStatCount_Object = MibTableColumn
tnSysIpAclFilterStatCount = _TnSysIpAclFilterStatCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 4),
    _TnSysIpAclFilterStatCount_Type()
)
tnSysIpAclFilterStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclFilterStatCount.setStatus("current")
_TnSysIpAclFilterRowStatus_Type = RowStatus
_TnSysIpAclFilterRowStatus_Object = MibTableColumn
tnSysIpAclFilterRowStatus = _TnSysIpAclFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 5),
    _TnSysIpAclFilterRowStatus_Type()
)
tnSysIpAclFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclFilterRowStatus.setStatus("current")
_TnSysIpAclFilterSystemDefault_Type = TruthValue
_TnSysIpAclFilterSystemDefault_Object = MibTableColumn
tnSysIpAclFilterSystemDefault = _TnSysIpAclFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 5, 1, 6),
    _TnSysIpAclFilterSystemDefault_Type()
)
tnSysIpAclFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclFilterSystemDefault.setStatus("current")
_TnSysIpAclInterfaceAttributeTotal_Type = Integer32
_TnSysIpAclInterfaceAttributeTotal_Object = MibScalar
tnSysIpAclInterfaceAttributeTotal = _TnSysIpAclInterfaceAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 6),
    _TnSysIpAclInterfaceAttributeTotal_Type()
)
tnSysIpAclInterfaceAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceAttributeTotal.setStatus("current")
_TnSysIpAclInterfaceTable_Object = MibTable
tnSysIpAclInterfaceTable = _TnSysIpAclInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7)
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceTable.setStatus("current")
_TnSysIpAclInterfaceEntry_Object = MibTableRow
tnSysIpAclInterfaceEntry = _TnSysIpAclInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1)
)
tnSysIpAclInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceEntry.setStatus("current")


class _TnSysIpAclInterfaceFilterDir_Type(Integer32):
    """Custom type tnSysIpAclInterfaceFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclInterfaceFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclInterfaceFilterDir_Object = MibTableColumn
tnSysIpAclInterfaceFilterDir = _TnSysIpAclInterfaceFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 1),
    _TnSysIpAclInterfaceFilterDir_Type()
)
tnSysIpAclInterfaceFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterDir.setStatus("current")


class _TnSysIpAclInterfaceFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclInterfaceFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclInterfaceFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclInterfaceFilterID_Object = MibTableColumn
tnSysIpAclInterfaceFilterID = _TnSysIpAclInterfaceFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 2),
    _TnSysIpAclInterfaceFilterID_Type()
)
tnSysIpAclInterfaceFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterID.setStatus("current")


class _TnSysIpAclInterfaceFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclInterfaceFilterEnable based on Integer32"""
    defaultValue = 2

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


_TnSysIpAclInterfaceFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclInterfaceFilterEnable_Object = MibTableColumn
tnSysIpAclInterfaceFilterEnable = _TnSysIpAclInterfaceFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 3),
    _TnSysIpAclInterfaceFilterEnable_Type()
)
tnSysIpAclInterfaceFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterEnable.setStatus("current")
_TnSysIpAclInterfaceFilterRowStatus_Type = RowStatus
_TnSysIpAclInterfaceFilterRowStatus_Object = MibTableColumn
tnSysIpAclInterfaceFilterRowStatus = _TnSysIpAclInterfaceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 4),
    _TnSysIpAclInterfaceFilterRowStatus_Type()
)
tnSysIpAclInterfaceFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceFilterRowStatus.setStatus("current")
_TnSysIpAclInterfaceSystemDefault_Type = TruthValue
_TnSysIpAclInterfaceSystemDefault_Object = MibTableColumn
tnSysIpAclInterfaceSystemDefault = _TnSysIpAclInterfaceSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 7, 1, 5),
    _TnSysIpAclInterfaceSystemDefault_Type()
)
tnSysIpAclInterfaceSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceSystemDefault.setStatus("current")
_TnSysIpAclNetIfFilterAttributeTotal_Type = Integer32
_TnSysIpAclNetIfFilterAttributeTotal_Object = MibScalar
tnSysIpAclNetIfFilterAttributeTotal = _TnSysIpAclNetIfFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 8),
    _TnSysIpAclNetIfFilterAttributeTotal_Type()
)
tnSysIpAclNetIfFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterAttributeTotal.setStatus("current")
_TnSysIpAclNetIfFilterTable_Object = MibTable
tnSysIpAclNetIfFilterTable = _TnSysIpAclNetIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9)
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterTable.setStatus("current")
_TnSysIpAclNetIfFilterEntry_Object = MibTableRow
tnSysIpAclNetIfFilterEntry = _TnSysIpAclNetIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1)
)
tnSysIpAclNetIfFilterEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterEntry.setStatus("current")


class _TnSysIpAclNetIfFilterDir_Type(Integer32):
    """Custom type tnSysIpAclNetIfFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclNetIfFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclNetIfFilterDir_Object = MibTableColumn
tnSysIpAclNetIfFilterDir = _TnSysIpAclNetIfFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 1),
    _TnSysIpAclNetIfFilterDir_Type()
)
tnSysIpAclNetIfFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterDir.setStatus("current")
_TnSysIpAclNetIfFilterRowStatus_Type = RowStatus
_TnSysIpAclNetIfFilterRowStatus_Object = MibTableColumn
tnSysIpAclNetIfFilterRowStatus = _TnSysIpAclNetIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 2),
    _TnSysIpAclNetIfFilterRowStatus_Type()
)
tnSysIpAclNetIfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterRowStatus.setStatus("current")


class _TnSysIpAclNetIfFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclNetIfFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclNetIfFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclNetIfFilterID_Object = MibTableColumn
tnSysIpAclNetIfFilterID = _TnSysIpAclNetIfFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 3),
    _TnSysIpAclNetIfFilterID_Type()
)
tnSysIpAclNetIfFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterID.setStatus("current")


class _TnSysIpAclNetIfFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclNetIfFilterEnable based on Integer32"""
    defaultValue = 2

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


_TnSysIpAclNetIfFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclNetIfFilterEnable_Object = MibTableColumn
tnSysIpAclNetIfFilterEnable = _TnSysIpAclNetIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 4),
    _TnSysIpAclNetIfFilterEnable_Type()
)
tnSysIpAclNetIfFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterEnable.setStatus("current")
_TnSysIpAclNetIfFilterSystemDefault_Type = TruthValue
_TnSysIpAclNetIfFilterSystemDefault_Object = MibTableColumn
tnSysIpAclNetIfFilterSystemDefault = _TnSysIpAclNetIfFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 9, 1, 5),
    _TnSysIpAclNetIfFilterSystemDefault_Type()
)
tnSysIpAclNetIfFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterSystemDefault.setStatus("current")
_TnSysIpAclIpv6PatternAttributeTotal_Type = Integer32
_TnSysIpAclIpv6PatternAttributeTotal_Object = MibScalar
tnSysIpAclIpv6PatternAttributeTotal = _TnSysIpAclIpv6PatternAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 10),
    _TnSysIpAclIpv6PatternAttributeTotal_Type()
)
tnSysIpAclIpv6PatternAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternAttributeTotal.setStatus("current")
_TnSysIpAclIpv6PatternTable_Object = MibTable
tnSysIpAclIpv6PatternTable = _TnSysIpAclIpv6PatternTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11)
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternTable.setStatus("current")
_TnSysIpAclIpv6PatternEntry_Object = MibTableRow
tnSysIpAclIpv6PatternEntry = _TnSysIpAclIpv6PatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1)
)
tnSysIpAclIpv6PatternEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6PatternID"),
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternEntry.setStatus("current")


class _TnSysIpAclIpv6PatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6PatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclIpv6PatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6PatternID_Object = MibTableColumn
tnSysIpAclIpv6PatternID = _TnSysIpAclIpv6PatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 1),
    _TnSysIpAclIpv6PatternID_Type()
)
tnSysIpAclIpv6PatternID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternID.setStatus("current")


class _TnSysIpAclIpv6PatternAction_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclIpv6PatternAction_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternAction_Object = MibTableColumn
tnSysIpAclIpv6PatternAction = _TnSysIpAclIpv6PatternAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 2),
    _TnSysIpAclIpv6PatternAction_Type()
)
tnSysIpAclIpv6PatternAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternAction.setStatus("current")


class _TnSysIpAclIpv6PatternICMPV6ERROR_Type(TruthValue):
    """Custom type tnSysIpAclIpv6PatternICMPV6ERROR based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6PatternICMPV6ERROR_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6PatternICMPV6ERROR_Object = MibTableColumn
tnSysIpAclIpv6PatternICMPV6ERROR = _TnSysIpAclIpv6PatternICMPV6ERROR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 3),
    _TnSysIpAclIpv6PatternICMPV6ERROR_Type()
)
tnSysIpAclIpv6PatternICMPV6ERROR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternICMPV6ERROR.setStatus("current")
_TnSysIpAclIpv6PatternSrcAddr_Type = InetAddressIPv6
_TnSysIpAclIpv6PatternSrcAddr_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcAddr = _TnSysIpAclIpv6PatternSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 4),
    _TnSysIpAclIpv6PatternSrcAddr_Type()
)
tnSysIpAclIpv6PatternSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcAddr.setStatus("current")
_TnSysIpAclIpv6PatternSrcPrefixLen_Type = InetAddressPrefixLength
_TnSysIpAclIpv6PatternSrcPrefixLen_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcPrefixLen = _TnSysIpAclIpv6PatternSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 5),
    _TnSysIpAclIpv6PatternSrcPrefixLen_Type()
)
tnSysIpAclIpv6PatternSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcPrefixLen.setStatus("current")
_TnSysIpAclIpv6PatternDestAddr_Type = InetAddressIPv6
_TnSysIpAclIpv6PatternDestAddr_Object = MibTableColumn
tnSysIpAclIpv6PatternDestAddr = _TnSysIpAclIpv6PatternDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 6),
    _TnSysIpAclIpv6PatternDestAddr_Type()
)
tnSysIpAclIpv6PatternDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestAddr.setStatus("current")
_TnSysIpAclIpv6PatternDestPrefixLen_Type = InetAddressPrefixLength
_TnSysIpAclIpv6PatternDestPrefixLen_Object = MibTableColumn
tnSysIpAclIpv6PatternDestPrefixLen = _TnSysIpAclIpv6PatternDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 7),
    _TnSysIpAclIpv6PatternDestPrefixLen_Type()
)
tnSysIpAclIpv6PatternDestPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestPrefixLen.setStatus("current")
_TnSysIpAclIpv6PatternIpProtocol_Type = OctetString
_TnSysIpAclIpv6PatternIpProtocol_Object = MibTableColumn
tnSysIpAclIpv6PatternIpProtocol = _TnSysIpAclIpv6PatternIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 8),
    _TnSysIpAclIpv6PatternIpProtocol_Type()
)
tnSysIpAclIpv6PatternIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIpProtocol.setStatus("current")


class _TnSysIpAclIpv6PatternIcmpType_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclIpv6PatternIcmpType_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternIcmpType_Object = MibTableColumn
tnSysIpAclIpv6PatternIcmpType = _TnSysIpAclIpv6PatternIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 9),
    _TnSysIpAclIpv6PatternIcmpType_Type()
)
tnSysIpAclIpv6PatternIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIcmpType.setStatus("current")


class _TnSysIpAclIpv6PatternIcmpCode_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnSysIpAclIpv6PatternIcmpCode_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternIcmpCode_Object = MibTableColumn
tnSysIpAclIpv6PatternIcmpCode = _TnSysIpAclIpv6PatternIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 10),
    _TnSysIpAclIpv6PatternIcmpCode_Type()
)
tnSysIpAclIpv6PatternIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIcmpCode.setStatus("current")


class _TnSysIpAclIpv6PatternSrcPort_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclIpv6PatternSrcPort_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternSrcPort_Object = MibTableColumn
tnSysIpAclIpv6PatternSrcPort = _TnSysIpAclIpv6PatternSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 11),
    _TnSysIpAclIpv6PatternSrcPort_Type()
)
tnSysIpAclIpv6PatternSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSrcPort.setStatus("current")


class _TnSysIpAclIpv6PatternDestPort_Type(Integer32):
    """Custom type tnSysIpAclIpv6PatternDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysIpAclIpv6PatternDestPort_Type.__name__ = "Integer32"
_TnSysIpAclIpv6PatternDestPort_Object = MibTableColumn
tnSysIpAclIpv6PatternDestPort = _TnSysIpAclIpv6PatternDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 12),
    _TnSysIpAclIpv6PatternDestPort_Type()
)
tnSysIpAclIpv6PatternDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternDestPort.setStatus("current")


class _TnSysIpAclIpv6PatternIpFragment_Type(TruthValue):
    """Custom type tnSysIpAclIpv6PatternIpFragment based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6PatternIpFragment_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6PatternIpFragment_Object = MibTableColumn
tnSysIpAclIpv6PatternIpFragment = _TnSysIpAclIpv6PatternIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 13),
    _TnSysIpAclIpv6PatternIpFragment_Type()
)
tnSysIpAclIpv6PatternIpFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternIpFragment.setStatus("current")
_TnSysIpAclIpv6PatternTcpEstablish_Type = TruthValue
_TnSysIpAclIpv6PatternTcpEstablish_Object = MibTableColumn
tnSysIpAclIpv6PatternTcpEstablish = _TnSysIpAclIpv6PatternTcpEstablish_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 14),
    _TnSysIpAclIpv6PatternTcpEstablish_Type()
)
tnSysIpAclIpv6PatternTcpEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternTcpEstablish.setStatus("current")
_TnSysIpAclIpv6PatternSystemDefault_Type = TruthValue
_TnSysIpAclIpv6PatternSystemDefault_Object = MibTableColumn
tnSysIpAclIpv6PatternSystemDefault = _TnSysIpAclIpv6PatternSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 15),
    _TnSysIpAclIpv6PatternSystemDefault_Type()
)
tnSysIpAclIpv6PatternSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternSystemDefault.setStatus("current")
_TnSysIpAclIpv6PatternRowStatus_Type = RowStatus
_TnSysIpAclIpv6PatternRowStatus_Object = MibTableColumn
tnSysIpAclIpv6PatternRowStatus = _TnSysIpAclIpv6PatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 11, 1, 16),
    _TnSysIpAclIpv6PatternRowStatus_Type()
)
tnSysIpAclIpv6PatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6PatternRowStatus.setStatus("current")
_TnSysIpAclIpv6FilterAttributeTotal_Type = Integer32
_TnSysIpAclIpv6FilterAttributeTotal_Object = MibScalar
tnSysIpAclIpv6FilterAttributeTotal = _TnSysIpAclIpv6FilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 12),
    _TnSysIpAclIpv6FilterAttributeTotal_Type()
)
tnSysIpAclIpv6FilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterAttributeTotal.setStatus("current")
_TnSysIpAclIpv6FilterTable_Object = MibTable
tnSysIpAclIpv6FilterTable = _TnSysIpAclIpv6FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13)
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterTable.setStatus("current")
_TnSysIpAclIpv6FilterEntry_Object = MibTableRow
tnSysIpAclIpv6FilterEntry = _TnSysIpAclIpv6FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1)
)
tnSysIpAclIpv6FilterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterID"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6FilterPatternIndex"),
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterEntry.setStatus("current")


class _TnSysIpAclIpv6FilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6FilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_TnSysIpAclIpv6FilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6FilterID_Object = MibTableColumn
tnSysIpAclIpv6FilterID = _TnSysIpAclIpv6FilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 1),
    _TnSysIpAclIpv6FilterID_Type()
)
tnSysIpAclIpv6FilterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterID.setStatus("current")


class _TnSysIpAclIpv6FilterPatternIndex_Type(Integer32):
    """Custom type tnSysIpAclIpv6FilterPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnSysIpAclIpv6FilterPatternIndex_Type.__name__ = "Integer32"
_TnSysIpAclIpv6FilterPatternIndex_Object = MibTableColumn
tnSysIpAclIpv6FilterPatternIndex = _TnSysIpAclIpv6FilterPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 2),
    _TnSysIpAclIpv6FilterPatternIndex_Type()
)
tnSysIpAclIpv6FilterPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterPatternIndex.setStatus("current")


class _TnSysIpAclIpv6FilterPatternID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6FilterPatternID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclIpv6FilterPatternID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6FilterPatternID_Object = MibTableColumn
tnSysIpAclIpv6FilterPatternID = _TnSysIpAclIpv6FilterPatternID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 3),
    _TnSysIpAclIpv6FilterPatternID_Type()
)
tnSysIpAclIpv6FilterPatternID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterPatternID.setStatus("current")
_TnSysIpAclIpv6FilterStatCount_Type = Counter32
_TnSysIpAclIpv6FilterStatCount_Object = MibTableColumn
tnSysIpAclIpv6FilterStatCount = _TnSysIpAclIpv6FilterStatCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 4),
    _TnSysIpAclIpv6FilterStatCount_Type()
)
tnSysIpAclIpv6FilterStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterStatCount.setStatus("current")
_TnSysIpAclIpv6FilterRowStatus_Type = RowStatus
_TnSysIpAclIpv6FilterRowStatus_Object = MibTableColumn
tnSysIpAclIpv6FilterRowStatus = _TnSysIpAclIpv6FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 5),
    _TnSysIpAclIpv6FilterRowStatus_Type()
)
tnSysIpAclIpv6FilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterRowStatus.setStatus("current")
_TnSysIpAclIpv6FilterSystemDefault_Type = TruthValue
_TnSysIpAclIpv6FilterSystemDefault_Object = MibTableColumn
tnSysIpAclIpv6FilterSystemDefault = _TnSysIpAclIpv6FilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 13, 1, 6),
    _TnSysIpAclIpv6FilterSystemDefault_Type()
)
tnSysIpAclIpv6FilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6FilterSystemDefault.setStatus("current")
_TnSysIpAclIpv6InterfaceAttributeTotal_Type = Integer32
_TnSysIpAclIpv6InterfaceAttributeTotal_Object = MibScalar
tnSysIpAclIpv6InterfaceAttributeTotal = _TnSysIpAclIpv6InterfaceAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 14),
    _TnSysIpAclIpv6InterfaceAttributeTotal_Type()
)
tnSysIpAclIpv6InterfaceAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceAttributeTotal.setStatus("current")
_TnSysIpAclIpv6InterfaceTable_Object = MibTable
tnSysIpAclIpv6InterfaceTable = _TnSysIpAclIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15)
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceTable.setStatus("current")
_TnSysIpAclIpv6InterfaceEntry_Object = MibTableRow
tnSysIpAclIpv6InterfaceEntry = _TnSysIpAclIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1)
)
tnSysIpAclIpv6InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6InterfaceFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceEntry.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterDir_Type(Integer32):
    """Custom type tnSysIpAclIpv6InterfaceFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpAclIpv6InterfaceFilterDir_Type.__name__ = "Integer32"
_TnSysIpAclIpv6InterfaceFilterDir_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterDir = _TnSysIpAclIpv6InterfaceFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 1),
    _TnSysIpAclIpv6InterfaceFilterDir_Type()
)
tnSysIpAclIpv6InterfaceFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterDir.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpAclIpv6InterfaceFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpAclIpv6InterfaceFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpAclIpv6InterfaceFilterID_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterID = _TnSysIpAclIpv6InterfaceFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 2),
    _TnSysIpAclIpv6InterfaceFilterID_Type()
)
tnSysIpAclIpv6InterfaceFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterID.setStatus("current")


class _TnSysIpAclIpv6InterfaceFilterEnable_Type(Integer32):
    """Custom type tnSysIpAclIpv6InterfaceFilterEnable based on Integer32"""
    defaultValue = 2

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


_TnSysIpAclIpv6InterfaceFilterEnable_Type.__name__ = "Integer32"
_TnSysIpAclIpv6InterfaceFilterEnable_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterEnable = _TnSysIpAclIpv6InterfaceFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 3),
    _TnSysIpAclIpv6InterfaceFilterEnable_Type()
)
tnSysIpAclIpv6InterfaceFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterEnable.setStatus("current")
_TnSysIpAclIpv6InterfaceFilterRowStatus_Type = RowStatus
_TnSysIpAclIpv6InterfaceFilterRowStatus_Object = MibTableColumn
tnSysIpAclIpv6InterfaceFilterRowStatus = _TnSysIpAclIpv6InterfaceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 4),
    _TnSysIpAclIpv6InterfaceFilterRowStatus_Type()
)
tnSysIpAclIpv6InterfaceFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceFilterRowStatus.setStatus("current")
_TnSysIpAclIpv6InterfaceSystemDefault_Type = TruthValue
_TnSysIpAclIpv6InterfaceSystemDefault_Object = MibTableColumn
tnSysIpAclIpv6InterfaceSystemDefault = _TnSysIpAclIpv6InterfaceSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 15, 1, 5),
    _TnSysIpAclIpv6InterfaceSystemDefault_Type()
)
tnSysIpAclIpv6InterfaceSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6InterfaceSystemDefault.setStatus("current")
_TnSysIpv6AclNetIfFilterAttributeTotal_Type = Integer32
_TnSysIpv6AclNetIfFilterAttributeTotal_Object = MibScalar
tnSysIpv6AclNetIfFilterAttributeTotal = _TnSysIpv6AclNetIfFilterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 16),
    _TnSysIpv6AclNetIfFilterAttributeTotal_Type()
)
tnSysIpv6AclNetIfFilterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterAttributeTotal.setStatus("current")
_TnSysIpv6AclNetIfFilterTable_Object = MibTable
tnSysIpv6AclNetIfFilterTable = _TnSysIpv6AclNetIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17)
)
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterTable.setStatus("current")
_TnSysIpv6AclNetIfFilterEntry_Object = MibTableRow
tnSysIpv6AclNetIfFilterEntry = _TnSysIpv6AclNetIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1)
)
tnSysIpv6AclNetIfFilterEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-SYSTEM-MIB", "tnSysIpv6AclNetIfFilterDir"),
)
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterEntry.setStatus("current")


class _TnSysIpv6AclNetIfFilterDir_Type(Integer32):
    """Custom type tnSysIpv6AclNetIfFilterDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_TnSysIpv6AclNetIfFilterDir_Type.__name__ = "Integer32"
_TnSysIpv6AclNetIfFilterDir_Object = MibTableColumn
tnSysIpv6AclNetIfFilterDir = _TnSysIpv6AclNetIfFilterDir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 1),
    _TnSysIpv6AclNetIfFilterDir_Type()
)
tnSysIpv6AclNetIfFilterDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterDir.setStatus("current")
_TnSysIpv6AclNetIfFilterRowStatus_Type = RowStatus
_TnSysIpv6AclNetIfFilterRowStatus_Object = MibTableColumn
tnSysIpv6AclNetIfFilterRowStatus = _TnSysIpv6AclNetIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 2),
    _TnSysIpv6AclNetIfFilterRowStatus_Type()
)
tnSysIpv6AclNetIfFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterRowStatus.setStatus("current")


class _TnSysIpv6AclNetIfFilterID_Type(SnmpAdminString):
    """Custom type tnSysIpv6AclNetIfFilterID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnSysIpv6AclNetIfFilterID_Type.__name__ = "SnmpAdminString"
_TnSysIpv6AclNetIfFilterID_Object = MibTableColumn
tnSysIpv6AclNetIfFilterID = _TnSysIpv6AclNetIfFilterID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 3),
    _TnSysIpv6AclNetIfFilterID_Type()
)
tnSysIpv6AclNetIfFilterID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterID.setStatus("current")


class _TnSysIpv6AclNetIfFilterEnable_Type(Integer32):
    """Custom type tnSysIpv6AclNetIfFilterEnable based on Integer32"""
    defaultValue = 2

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


_TnSysIpv6AclNetIfFilterEnable_Type.__name__ = "Integer32"
_TnSysIpv6AclNetIfFilterEnable_Object = MibTableColumn
tnSysIpv6AclNetIfFilterEnable = _TnSysIpv6AclNetIfFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 4),
    _TnSysIpv6AclNetIfFilterEnable_Type()
)
tnSysIpv6AclNetIfFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterEnable.setStatus("current")
_TnSysIpv6AclNetIfFilterSystemDefault_Type = TruthValue
_TnSysIpv6AclNetIfFilterSystemDefault_Object = MibTableColumn
tnSysIpv6AclNetIfFilterSystemDefault = _TnSysIpv6AclNetIfFilterSystemDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 17, 17, 1, 5),
    _TnSysIpv6AclNetIfFilterSystemDefault_Type()
)
tnSysIpv6AclNetIfFilterSystemDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysIpv6AclNetIfFilterSystemDefault.setStatus("current")
_TnSysNtpServerIdStats_ObjectIdentity = ObjectIdentity
tnSysNtpServerIdStats = _TnSysNtpServerIdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18)
)
_TnSysNtpServerIdStatsTable_Object = MibTable
tnSysNtpServerIdStatsTable = _TnSysNtpServerIdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsTable.setStatus("current")
_TnSysNtpServerIdStatsEntry_Object = MibTableRow
tnSysNtpServerIdStatsEntry = _TnSysNtpServerIdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1)
)
tnSysNtpServerIdStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsIndex"),
)
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsEntry.setStatus("current")


class _TnSysNtpServerIdStatsIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerIdStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TnSysNtpServerIdStatsIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerIdStatsIndex_Object = MibTableColumn
tnSysNtpServerIdStatsIndex = _TnSysNtpServerIdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 1),
    _TnSysNtpServerIdStatsIndex_Type()
)
tnSysNtpServerIdStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsIndex.setStatus("current")


class _TnSysNtpServerIdStatsSelect_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsSelect based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TnSysNtpServerIdStatsSelect_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsSelect_Object = MibTableColumn
tnSysNtpServerIdStatsSelect = _TnSysNtpServerIdStatsSelect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 2),
    _TnSysNtpServerIdStatsSelect_Type()
)
tnSysNtpServerIdStatsSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsSelect.setStatus("current")


class _TnSysNtpServerIdStatsIp_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsIp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TnSysNtpServerIdStatsIp_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsIp_Object = MibTableColumn
tnSysNtpServerIdStatsIp = _TnSysNtpServerIdStatsIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 3),
    _TnSysNtpServerIdStatsIp_Type()
)
tnSysNtpServerIdStatsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsIp.setStatus("current")


class _TnSysNtpServerIdStatsRefId_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsRefId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TnSysNtpServerIdStatsRefId_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsRefId_Object = MibTableColumn
tnSysNtpServerIdStatsRefId = _TnSysNtpServerIdStatsRefId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 4),
    _TnSysNtpServerIdStatsRefId_Type()
)
tnSysNtpServerIdStatsRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsRefId.setStatus("current")


class _TnSysNtpServerIdStatsStrtm_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsStrtm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TnSysNtpServerIdStatsStrtm_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsStrtm_Object = MibTableColumn
tnSysNtpServerIdStatsStrtm = _TnSysNtpServerIdStatsStrtm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 5),
    _TnSysNtpServerIdStatsStrtm_Type()
)
tnSysNtpServerIdStatsStrtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsStrtm.setStatus("current")


class _TnSysNtpServerIdStatsClockType_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsClockType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_TnSysNtpServerIdStatsClockType_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsClockType_Object = MibTableColumn
tnSysNtpServerIdStatsClockType = _TnSysNtpServerIdStatsClockType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 6),
    _TnSysNtpServerIdStatsClockType_Type()
)
tnSysNtpServerIdStatsClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsClockType.setStatus("current")


class _TnSysNtpServerIdStatsPoll_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsPoll based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TnSysNtpServerIdStatsPoll_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsPoll_Object = MibTableColumn
tnSysNtpServerIdStatsPoll = _TnSysNtpServerIdStatsPoll_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 7),
    _TnSysNtpServerIdStatsPoll_Type()
)
tnSysNtpServerIdStatsPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsPoll.setStatus("current")


class _TnSysNtpServerIdStatsReach_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsReach based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_TnSysNtpServerIdStatsReach_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsReach_Object = MibTableColumn
tnSysNtpServerIdStatsReach = _TnSysNtpServerIdStatsReach_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 8),
    _TnSysNtpServerIdStatsReach_Type()
)
tnSysNtpServerIdStatsReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsReach.setStatus("current")


class _TnSysNtpServerIdStatsDelay_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsDelay based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnSysNtpServerIdStatsDelay_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsDelay_Object = MibTableColumn
tnSysNtpServerIdStatsDelay = _TnSysNtpServerIdStatsDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 9),
    _TnSysNtpServerIdStatsDelay_Type()
)
tnSysNtpServerIdStatsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsDelay.setStatus("current")


class _TnSysNtpServerIdStatsOffset_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsOffset based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnSysNtpServerIdStatsOffset_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsOffset_Object = MibTableColumn
tnSysNtpServerIdStatsOffset = _TnSysNtpServerIdStatsOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 10),
    _TnSysNtpServerIdStatsOffset_Type()
)
tnSysNtpServerIdStatsOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsOffset.setStatus("current")


class _TnSysNtpServerIdStatsJitter_Type(SnmpAdminString):
    """Custom type tnSysNtpServerIdStatsJitter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TnSysNtpServerIdStatsJitter_Type.__name__ = "SnmpAdminString"
_TnSysNtpServerIdStatsJitter_Object = MibTableColumn
tnSysNtpServerIdStatsJitter = _TnSysNtpServerIdStatsJitter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 11),
    _TnSysNtpServerIdStatsJitter_Type()
)
tnSysNtpServerIdStatsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsJitter.setStatus("current")
_TnSysNtpServerIdStatsKeyIndex_Type = Unsigned32
_TnSysNtpServerIdStatsKeyIndex_Object = MibTableColumn
tnSysNtpServerIdStatsKeyIndex = _TnSysNtpServerIdStatsKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 18, 1, 1, 12),
    _TnSysNtpServerIdStatsKeyIndex_Type()
)
tnSysNtpServerIdStatsKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsKeyIndex.setStatus("current")
_TnSysFtpServer_ObjectIdentity = ObjectIdentity
tnSysFtpServer = _TnSysFtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19)
)


class _TnSysFtpServerEnabled_Type(TruthValue):
    """Custom type tnSysFtpServerEnabled based on TruthValue"""
    defaultValue = 2


_TnSysFtpServerEnabled_Type.__name__ = "TruthValue"
_TnSysFtpServerEnabled_Object = MibScalar
tnSysFtpServerEnabled = _TnSysFtpServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19, 1),
    _TnSysFtpServerEnabled_Type()
)
tnSysFtpServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFtpServerEnabled.setStatus("current")


class _TnSysFtpServerUserId_Type(SnmpAdminString):
    """Custom type tnSysFtpServerUserId based on SnmpAdminString"""
    defaultValue = OctetString("UserSWNE")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysFtpServerUserId_Type.__name__ = "SnmpAdminString"
_TnSysFtpServerUserId_Object = MibScalar
tnSysFtpServerUserId = _TnSysFtpServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19, 2),
    _TnSysFtpServerUserId_Type()
)
tnSysFtpServerUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysFtpServerUserId.setStatus("current")


class _TnSysFtpServerPassword_Type(SnmpAdminString):
    """Custom type tnSysFtpServerPassword based on SnmpAdminString"""
    defaultValue = OctetString("********")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysFtpServerPassword_Type.__name__ = "SnmpAdminString"
_TnSysFtpServerPassword_Object = MibScalar
tnSysFtpServerPassword = _TnSysFtpServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 19, 3),
    _TnSysFtpServerPassword_Type()
)
tnSysFtpServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysFtpServerPassword.setStatus("current")
_TnSysNtpServerAuthentication_ObjectIdentity = ObjectIdentity
tnSysNtpServerAuthentication = _TnSysNtpServerAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20)
)
_TnSysNtpServerAuthenticationAttributeTotal_Type = Integer32
_TnSysNtpServerAuthenticationAttributeTotal_Object = MibScalar
tnSysNtpServerAuthenticationAttributeTotal = _TnSysNtpServerAuthenticationAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 1),
    _TnSysNtpServerAuthenticationAttributeTotal_Type()
)
tnSysNtpServerAuthenticationAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationAttributeTotal.setStatus("current")
_TnSysNtpServerAuthenticationTable_Object = MibTable
tnSysNtpServerAuthenticationTable = _TnSysNtpServerAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationTable.setStatus("current")
_TnSysNtpServerAuthenticationEntry_Object = MibTableRow
tnSysNtpServerAuthenticationEntry = _TnSysNtpServerAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1)
)
tnSysNtpServerAuthenticationEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationKeyIndex"),
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationEntry.setStatus("current")


class _TnSysNtpServerAuthenticationKeyIndex_Type(Unsigned32):
    """Custom type tnSysNtpServerAuthenticationKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnSysNtpServerAuthenticationKeyIndex_Type.__name__ = "Unsigned32"
_TnSysNtpServerAuthenticationKeyIndex_Object = MibTableColumn
tnSysNtpServerAuthenticationKeyIndex = _TnSysNtpServerAuthenticationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 1),
    _TnSysNtpServerAuthenticationKeyIndex_Type()
)
tnSysNtpServerAuthenticationKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationKeyIndex.setStatus("current")


class _TnSysNtpServerAuthenticationRowStatus_Type(RowStatus):
    """Custom type tnSysNtpServerAuthenticationRowStatus based on RowStatus"""
    defaultValue = 6


_TnSysNtpServerAuthenticationRowStatus_Type.__name__ = "RowStatus"
_TnSysNtpServerAuthenticationRowStatus_Object = MibTableColumn
tnSysNtpServerAuthenticationRowStatus = _TnSysNtpServerAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 2),
    _TnSysNtpServerAuthenticationRowStatus_Type()
)
tnSysNtpServerAuthenticationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationRowStatus.setStatus("current")


class _TnSysNtpServerAuthenticationKeyType_Type(Integer32):
    """Custom type tnSysNtpServerAuthenticationKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sha1", 1),
          ("md5", 2))
    )


_TnSysNtpServerAuthenticationKeyType_Type.__name__ = "Integer32"
_TnSysNtpServerAuthenticationKeyType_Object = MibTableColumn
tnSysNtpServerAuthenticationKeyType = _TnSysNtpServerAuthenticationKeyType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 3),
    _TnSysNtpServerAuthenticationKeyType_Type()
)
tnSysNtpServerAuthenticationKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationKeyType.setStatus("current")


class _TnSysNtpServerAuthenticationKey_Type(OctetString):
    """Custom type tnSysNtpServerAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_TnSysNtpServerAuthenticationKey_Type.__name__ = "OctetString"
_TnSysNtpServerAuthenticationKey_Object = MibTableColumn
tnSysNtpServerAuthenticationKey = _TnSysNtpServerAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 20, 2, 1, 4),
    _TnSysNtpServerAuthenticationKey_Type()
)
tnSysNtpServerAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationKey.setStatus("current")
_TnNeDiscovery_ObjectIdentity = ObjectIdentity
tnNeDiscovery = _TnNeDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21)
)
_TnNeDiscoveryAttributeTotal_Type = Integer32
_TnNeDiscoveryAttributeTotal_Object = MibScalar
tnNeDiscoveryAttributeTotal = _TnNeDiscoveryAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 1),
    _TnNeDiscoveryAttributeTotal_Type()
)
tnNeDiscoveryAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryAttributeTotal.setStatus("current")
_TnNeDiscoveryTable_Object = MibTable
tnNeDiscoveryTable = _TnNeDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    tnNeDiscoveryTable.setStatus("current")
_TnNeDiscoveryEntry_Object = MibTableRow
tnNeDiscoveryEntry = _TnNeDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1)
)
tnNeDiscoveryEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnNeDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    tnNeDiscoveryEntry.setStatus("current")


class _TnNeDiscoveryIndex_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_TnNeDiscoveryIndex_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryIndex_Object = MibTableColumn
tnNeDiscoveryIndex = _TnNeDiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 1),
    _TnNeDiscoveryIndex_Type()
)
tnNeDiscoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNeDiscoveryIndex.setStatus("current")


class _TnNeDiscoveryFilename_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryFilename based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnNeDiscoveryFilename_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryFilename_Object = MibTableColumn
tnNeDiscoveryFilename = _TnNeDiscoveryFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 2),
    _TnNeDiscoveryFilename_Type()
)
tnNeDiscoveryFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryFilename.setStatus("current")


class _TnNeDiscoveryControl_Type(Integer32):
    """Custom type tnNeDiscoveryControl based on Integer32"""
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
        *(("noCmd", 1),
          ("start", 2),
          ("abort", 3))
    )


_TnNeDiscoveryControl_Type.__name__ = "Integer32"
_TnNeDiscoveryControl_Object = MibTableColumn
tnNeDiscoveryControl = _TnNeDiscoveryControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 3),
    _TnNeDiscoveryControl_Type()
)
tnNeDiscoveryControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryControl.setStatus("current")


class _TnNeDiscoveryStatus_Type(Integer32):
    """Custom type tnNeDiscoveryStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnNeDiscoveryStatus_Type.__name__ = "Integer32"
_TnNeDiscoveryStatus_Object = MibTableColumn
tnNeDiscoveryStatus = _TnNeDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 4),
    _TnNeDiscoveryStatus_Type()
)
tnNeDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryStatus.setStatus("current")


class _TnNeDiscoveryErrorCode_Type(Integer32):
    """Custom type tnNeDiscoveryErrorCode based on Integer32"""
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
        *(("noError", 1),
          ("unknown", 2),
          ("timeout", 3),
          ("serverError", 4),
          ("networkError", 5),
          ("fileSystemError", 6),
          ("systemNotReady", 7))
    )


_TnNeDiscoveryErrorCode_Type.__name__ = "Integer32"
_TnNeDiscoveryErrorCode_Object = MibTableColumn
tnNeDiscoveryErrorCode = _TnNeDiscoveryErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 5),
    _TnNeDiscoveryErrorCode_Type()
)
tnNeDiscoveryErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNeDiscoveryErrorCode.setStatus("current")
_TnNeDiscoveryServerIp_Type = IpAddress
_TnNeDiscoveryServerIp_Object = MibTableColumn
tnNeDiscoveryServerIp = _TnNeDiscoveryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 6),
    _TnNeDiscoveryServerIp_Type()
)
tnNeDiscoveryServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerIp.setStatus("current")
_TnNeDiscoveryServerProtocol_Type = AluWdmTransferProtocol
_TnNeDiscoveryServerProtocol_Object = MibTableColumn
tnNeDiscoveryServerProtocol = _TnNeDiscoveryServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 7),
    _TnNeDiscoveryServerProtocol_Type()
)
tnNeDiscoveryServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerProtocol.setStatus("current")


class _TnNeDiscoveryServerUserId_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TnNeDiscoveryServerUserId_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryServerUserId_Object = MibTableColumn
tnNeDiscoveryServerUserId = _TnNeDiscoveryServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 8),
    _TnNeDiscoveryServerUserId_Type()
)
tnNeDiscoveryServerUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerUserId.setStatus("current")


class _TnNeDiscoveryServerPassword_Type(SnmpAdminString):
    """Custom type tnNeDiscoveryServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TnNeDiscoveryServerPassword_Type.__name__ = "SnmpAdminString"
_TnNeDiscoveryServerPassword_Object = MibTableColumn
tnNeDiscoveryServerPassword = _TnNeDiscoveryServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 9),
    _TnNeDiscoveryServerPassword_Type()
)
tnNeDiscoveryServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerPassword.setStatus("current")
_TnNeDiscoveryServerTimeOut_Type = Integer32
_TnNeDiscoveryServerTimeOut_Object = MibTableColumn
tnNeDiscoveryServerTimeOut = _TnNeDiscoveryServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 10),
    _TnNeDiscoveryServerTimeOut_Type()
)
tnNeDiscoveryServerTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerTimeOut.setStatus("current")
_TnNeDiscoveryRowStatus_Type = RowStatus
_TnNeDiscoveryRowStatus_Object = MibTableColumn
tnNeDiscoveryRowStatus = _TnNeDiscoveryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 11),
    _TnNeDiscoveryRowStatus_Type()
)
tnNeDiscoveryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnNeDiscoveryRowStatus.setStatus("current")


class _TnNeDiscoveryServerInetAddressType_Type(InetAddressType):
    """Custom type tnNeDiscoveryServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnNeDiscoveryServerInetAddressType_Type.__name__ = "InetAddressType"
_TnNeDiscoveryServerInetAddressType_Object = MibTableColumn
tnNeDiscoveryServerInetAddressType = _TnNeDiscoveryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 12),
    _TnNeDiscoveryServerInetAddressType_Type()
)
tnNeDiscoveryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerInetAddressType.setStatus("current")


class _TnNeDiscoveryServerInetAddress_Type(InetAddress):
    """Custom type tnNeDiscoveryServerInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnNeDiscoveryServerInetAddress_Type.__name__ = "InetAddress"
_TnNeDiscoveryServerInetAddress_Object = MibTableColumn
tnNeDiscoveryServerInetAddress = _TnNeDiscoveryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 21, 2, 1, 13),
    _TnNeDiscoveryServerInetAddress_Type()
)
tnNeDiscoveryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnNeDiscoveryServerInetAddress.setStatus("current")
_TnSysOtdrScan_ObjectIdentity = ObjectIdentity
tnSysOtdrScan = _TnSysOtdrScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22)
)
_TnSysOtdrScanSystemProfile_ObjectIdentity = ObjectIdentity
tnSysOtdrScanSystemProfile = _TnSysOtdrScanSystemProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1)
)
_TnSysOtdrScanSystemProfileAttributeTotal_Type = Integer32
_TnSysOtdrScanSystemProfileAttributeTotal_Object = MibScalar
tnSysOtdrScanSystemProfileAttributeTotal = _TnSysOtdrScanSystemProfileAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 1),
    _TnSysOtdrScanSystemProfileAttributeTotal_Type()
)
tnSysOtdrScanSystemProfileAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileAttributeTotal.setStatus("current")
_TnSysOtdrScanSystemProfileTable_Object = MibTable
tnSysOtdrScanSystemProfileTable = _TnSysOtdrScanSystemProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2)
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileTable.setStatus("current")
_TnSysOtdrScanSystemProfileEntry_Object = MibTableRow
tnSysOtdrScanSystemProfileEntry = _TnSysOtdrScanSystemProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1)
)
tnSysOtdrScanSystemProfileEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileId"),
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileEntry.setStatus("current")


class _TnSysOtdrScanSystemProfileId_Type(Integer32):
    """Custom type tnSysOtdrScanSystemProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnSysOtdrScanSystemProfileId_Type.__name__ = "Integer32"
_TnSysOtdrScanSystemProfileId_Object = MibTableColumn
tnSysOtdrScanSystemProfileId = _TnSysOtdrScanSystemProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 1),
    _TnSysOtdrScanSystemProfileId_Type()
)
tnSysOtdrScanSystemProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileId.setStatus("current")


class _TnSysOtdrScanSystemProfileDescription_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanSystemProfileDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TnSysOtdrScanSystemProfileDescription_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanSystemProfileDescription_Object = MibTableColumn
tnSysOtdrScanSystemProfileDescription = _TnSysOtdrScanSystemProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 2),
    _TnSysOtdrScanSystemProfileDescription_Type()
)
tnSysOtdrScanSystemProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileDescription.setStatus("current")


class _TnSysOtdrScanSystemProfileWaveLength_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileWaveLength based on Unsigned32"""
    defaultValue = 1610


_TnSysOtdrScanSystemProfileWaveLength_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileWaveLength_Object = MibTableColumn
tnSysOtdrScanSystemProfileWaveLength = _TnSysOtdrScanSystemProfileWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 3),
    _TnSysOtdrScanSystemProfileWaveLength_Type()
)
tnSysOtdrScanSystemProfileWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileWaveLength.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileWaveLength.setUnits("nanometers")


class _TnSysOtdrScanSystemProfilePulseLength_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfilePulseLength based on Unsigned32"""
    defaultValue = 300


_TnSysOtdrScanSystemProfilePulseLength_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfilePulseLength_Object = MibTableColumn
tnSysOtdrScanSystemProfilePulseLength = _TnSysOtdrScanSystemProfilePulseLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 4),
    _TnSysOtdrScanSystemProfilePulseLength_Type()
)
tnSysOtdrScanSystemProfilePulseLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfilePulseLength.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfilePulseLength.setUnits("nanoseconds")


class _TnSysOtdrScanSystemProfileRange_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileRange based on Unsigned32"""
    defaultValue = 160000


_TnSysOtdrScanSystemProfileRange_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileRange_Object = MibTableColumn
tnSysOtdrScanSystemProfileRange = _TnSysOtdrScanSystemProfileRange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 5),
    _TnSysOtdrScanSystemProfileRange_Type()
)
tnSysOtdrScanSystemProfileRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileRange.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileRange.setUnits("meters")


class _TnSysOtdrScanSystemProfileResolution_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileResolution based on Unsigned32"""
    defaultValue = 2500


_TnSysOtdrScanSystemProfileResolution_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileResolution_Object = MibTableColumn
tnSysOtdrScanSystemProfileResolution = _TnSysOtdrScanSystemProfileResolution_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 6),
    _TnSysOtdrScanSystemProfileResolution_Type()
)
tnSysOtdrScanSystemProfileResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileResolution.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileResolution.setUnits("millimeters")


class _TnSysOtdrScanSystemProfileAvgTime_Type(Unsigned32):
    """Custom type tnSysOtdrScanSystemProfileAvgTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_TnSysOtdrScanSystemProfileAvgTime_Type.__name__ = "Unsigned32"
_TnSysOtdrScanSystemProfileAvgTime_Object = MibTableColumn
tnSysOtdrScanSystemProfileAvgTime = _TnSysOtdrScanSystemProfileAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 1, 2, 1, 7),
    _TnSysOtdrScanSystemProfileAvgTime_Type()
)
tnSysOtdrScanSystemProfileAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileAvgTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileAvgTime.setUnits("seconds")
_TnSysOtdrScanTransfer_ObjectIdentity = ObjectIdentity
tnSysOtdrScanTransfer = _TnSysOtdrScanTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2)
)
_TnSysOtdrScanTransferRemoteHostIp_Type = IpAddress
_TnSysOtdrScanTransferRemoteHostIp_Object = MibScalar
tnSysOtdrScanTransferRemoteHostIp = _TnSysOtdrScanTransferRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 1),
    _TnSysOtdrScanTransferRemoteHostIp_Type()
)
tnSysOtdrScanTransferRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferRemoteHostIp.setStatus("current")


class _TnSysOtdrScanTransferCommand_Type(Integer32):
    """Custom type tnSysOtdrScanTransferCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysOtdrScanTransferCommand_Type.__name__ = "Integer32"
_TnSysOtdrScanTransferCommand_Object = MibScalar
tnSysOtdrScanTransferCommand = _TnSysOtdrScanTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 2),
    _TnSysOtdrScanTransferCommand_Type()
)
tnSysOtdrScanTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferCommand.setStatus("current")


class _TnSysOtdrScanTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOtdrScanTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferRemotePath_Object = MibScalar
tnSysOtdrScanTransferRemotePath = _TnSysOtdrScanTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 3),
    _TnSysOtdrScanTransferRemotePath_Type()
)
tnSysOtdrScanTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferRemotePath.setStatus("current")


class _TnSysOtdrScanTransferStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysOtdrScanTransferStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysOtdrScanTransferStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysOtdrScanTransferStatus_Object = MibScalar
tnSysOtdrScanTransferStatus = _TnSysOtdrScanTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 4),
    _TnSysOtdrScanTransferStatus_Type()
)
tnSysOtdrScanTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferStatus.setStatus("current")


class _TnSysOtdrScanTransferFilename_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferFilename based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysOtdrScanTransferFilename_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferFilename_Object = MibScalar
tnSysOtdrScanTransferFilename = _TnSysOtdrScanTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 5),
    _TnSysOtdrScanTransferFilename_Type()
)
tnSysOtdrScanTransferFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferFilename.setStatus("current")


class _TnSysOtdrScanTransferProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysOtdrScanTransferProtocol based on AluWdmTransferProtocol"""
    defaultValue = 1


_TnSysOtdrScanTransferProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysOtdrScanTransferProtocol_Object = MibScalar
tnSysOtdrScanTransferProtocol = _TnSysOtdrScanTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 6),
    _TnSysOtdrScanTransferProtocol_Type()
)
tnSysOtdrScanTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferProtocol.setStatus("current")


class _TnSysOtdrScanTransferUserId_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysOtdrScanTransferUserId_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferUserId_Object = MibScalar
tnSysOtdrScanTransferUserId = _TnSysOtdrScanTransferUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 7),
    _TnSysOtdrScanTransferUserId_Type()
)
tnSysOtdrScanTransferUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferUserId.setStatus("current")


class _TnSysOtdrScanTransferPassword_Type(SnmpAdminString):
    """Custom type tnSysOtdrScanTransferPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysOtdrScanTransferPassword_Type.__name__ = "SnmpAdminString"
_TnSysOtdrScanTransferPassword_Object = MibScalar
tnSysOtdrScanTransferPassword = _TnSysOtdrScanTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 8),
    _TnSysOtdrScanTransferPassword_Type()
)
tnSysOtdrScanTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferPassword.setStatus("current")


class _TnSysOtdrScanTransferInetAddressType_Type(InetAddressType):
    """Custom type tnSysOtdrScanTransferInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysOtdrScanTransferInetAddressType_Type.__name__ = "InetAddressType"
_TnSysOtdrScanTransferInetAddressType_Object = MibScalar
tnSysOtdrScanTransferInetAddressType = _TnSysOtdrScanTransferInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 9),
    _TnSysOtdrScanTransferInetAddressType_Type()
)
tnSysOtdrScanTransferInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferInetAddressType.setStatus("current")


class _TnSysOtdrScanTransferInetAddress_Type(InetAddress):
    """Custom type tnSysOtdrScanTransferInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysOtdrScanTransferInetAddress_Type.__name__ = "InetAddress"
_TnSysOtdrScanTransferInetAddress_Object = MibScalar
tnSysOtdrScanTransferInetAddress = _TnSysOtdrScanTransferInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 22, 2, 10),
    _TnSysOtdrScanTransferInetAddress_Type()
)
tnSysOtdrScanTransferInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferInetAddress.setStatus("current")
_TnClusterObjs_ObjectIdentity = ObjectIdentity
tnClusterObjs = _TnClusterObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23)
)
_TnClusterTable_Object = MibTable
tnClusterTable = _TnClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1)
)
if mibBuilder.loadTexts:
    tnClusterTable.setStatus("current")
_TnClusterEntry_Object = MibTableRow
tnClusterEntry = _TnClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1)
)
tnClusterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnClusterFarEndNode"),
)
if mibBuilder.loadTexts:
    tnClusterEntry.setStatus("current")
_TnClusterRowStatus_Type = RowStatus
_TnClusterRowStatus_Object = MibTableColumn
tnClusterRowStatus = _TnClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 1),
    _TnClusterRowStatus_Type()
)
tnClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterRowStatus.setStatus("current")
_TnClusterFarEndNode_Type = OctetString
_TnClusterFarEndNode_Object = MibTableColumn
tnClusterFarEndNode = _TnClusterFarEndNode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 2),
    _TnClusterFarEndNode_Type()
)
tnClusterFarEndNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnClusterFarEndNode.setStatus("current")
_TnClusterIpAddress_Type = IpAddress
_TnClusterIpAddress_Object = MibTableColumn
tnClusterIpAddress = _TnClusterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 3),
    _TnClusterIpAddress_Type()
)
tnClusterIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterIpAddress.setStatus("current")


class _TnClusterlinkStatus_Type(Integer32):
    """Custom type tnClusterlinkStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_TnClusterlinkStatus_Type.__name__ = "Integer32"
_TnClusterlinkStatus_Object = MibTableColumn
tnClusterlinkStatus = _TnClusterlinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 4),
    _TnClusterlinkStatus_Type()
)
tnClusterlinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnClusterlinkStatus.setStatus("current")


class _TnClusterInetAddressType_Type(InetAddressType):
    """Custom type tnClusterInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnClusterInetAddressType_Type.__name__ = "InetAddressType"
_TnClusterInetAddressType_Object = MibTableColumn
tnClusterInetAddressType = _TnClusterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 5),
    _TnClusterInetAddressType_Type()
)
tnClusterInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnClusterInetAddressType.setStatus("current")


class _TnClusterInetAddress_Type(InetAddress):
    """Custom type tnClusterInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnClusterInetAddress_Type.__name__ = "InetAddress"
_TnClusterInetAddress_Object = MibTableColumn
tnClusterInetAddress = _TnClusterInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 23, 1, 1, 6),
    _TnClusterInetAddress_Type()
)
tnClusterInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnClusterInetAddress.setStatus("current")
_TnSysPmFetchBulk_ObjectIdentity = ObjectIdentity
tnSysPmFetchBulk = _TnSysPmFetchBulk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24)
)


class _TnSysPmFetchBulkStart_Type(TnCommand):
    """Custom type tnSysPmFetchBulkStart based on TnCommand"""
    defaultValue = 1


_TnSysPmFetchBulkStart_Type.__name__ = "TnCommand"
_TnSysPmFetchBulkStart_Object = MibScalar
tnSysPmFetchBulkStart = _TnSysPmFetchBulkStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 1),
    _TnSysPmFetchBulkStart_Type()
)
tnSysPmFetchBulkStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkStart.setStatus("current")


class _TnSysPmFetchBulkStatus_Type(Integer32):
    """Custom type tnSysPmFetchBulkStatus based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("inProgress", 2),
          ("completedSuccessfully", 3),
          ("failed", 4),
          ("aborted", 5))
    )


_TnSysPmFetchBulkStatus_Type.__name__ = "Integer32"
_TnSysPmFetchBulkStatus_Object = MibScalar
tnSysPmFetchBulkStatus = _TnSysPmFetchBulkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 2),
    _TnSysPmFetchBulkStatus_Type()
)
tnSysPmFetchBulkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkStatus.setStatus("current")
_TnSysPmFetchBulkRemoteHostIp_Type = IpAddress
_TnSysPmFetchBulkRemoteHostIp_Object = MibScalar
tnSysPmFetchBulkRemoteHostIp = _TnSysPmFetchBulkRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 3),
    _TnSysPmFetchBulkRemoteHostIp_Type()
)
tnSysPmFetchBulkRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkRemoteHostIp.setStatus("current")


class _TnSysPmFetchBulkUserId_Type(SnmpAdminString):
    """Custom type tnSysPmFetchBulkUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysPmFetchBulkUserId_Type.__name__ = "SnmpAdminString"
_TnSysPmFetchBulkUserId_Object = MibScalar
tnSysPmFetchBulkUserId = _TnSysPmFetchBulkUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 4),
    _TnSysPmFetchBulkUserId_Type()
)
tnSysPmFetchBulkUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkUserId.setStatus("current")


class _TnSysPmFetchBulkPassword_Type(SnmpAdminString):
    """Custom type tnSysPmFetchBulkPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysPmFetchBulkPassword_Type.__name__ = "SnmpAdminString"
_TnSysPmFetchBulkPassword_Object = MibScalar
tnSysPmFetchBulkPassword = _TnSysPmFetchBulkPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 5),
    _TnSysPmFetchBulkPassword_Type()
)
tnSysPmFetchBulkPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkPassword.setStatus("current")


class _TnSysPmFetchBulkRemotePath_Type(SnmpAdminString):
    """Custom type tnSysPmFetchBulkRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysPmFetchBulkRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysPmFetchBulkRemotePath_Object = MibScalar
tnSysPmFetchBulkRemotePath = _TnSysPmFetchBulkRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 6),
    _TnSysPmFetchBulkRemotePath_Type()
)
tnSysPmFetchBulkRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkRemotePath.setStatus("current")


class _TnSysPmFetchBulkStatsInterval_Type(Unsigned32):
    """Custom type tnSysPmFetchBulkStatsInterval based on Unsigned32"""
    defaultValue = 0


_TnSysPmFetchBulkStatsInterval_Type.__name__ = "Unsigned32"
_TnSysPmFetchBulkStatsInterval_Object = MibScalar
tnSysPmFetchBulkStatsInterval = _TnSysPmFetchBulkStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 7),
    _TnSysPmFetchBulkStatsInterval_Type()
)
tnSysPmFetchBulkStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkStatsInterval.setStatus("current")


class _TnSysPmFetchBulkBinnedStatsBin_Type(Unsigned32):
    """Custom type tnSysPmFetchBulkBinnedStatsBin based on Unsigned32"""
    defaultValue = 0


_TnSysPmFetchBulkBinnedStatsBin_Type.__name__ = "Unsigned32"
_TnSysPmFetchBulkBinnedStatsBin_Object = MibScalar
tnSysPmFetchBulkBinnedStatsBin = _TnSysPmFetchBulkBinnedStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 8),
    _TnSysPmFetchBulkBinnedStatsBin_Type()
)
tnSysPmFetchBulkBinnedStatsBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkBinnedStatsBin.setStatus("current")


class _TnSysPmFetchBulkShelfNum_Type(Integer32):
    """Custom type tnSysPmFetchBulkShelfNum based on Integer32"""
    defaultValue = 1


_TnSysPmFetchBulkShelfNum_Type.__name__ = "Integer32"
_TnSysPmFetchBulkShelfNum_Object = MibScalar
tnSysPmFetchBulkShelfNum = _TnSysPmFetchBulkShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 24, 9),
    _TnSysPmFetchBulkShelfNum_Type()
)
tnSysPmFetchBulkShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysPmFetchBulkShelfNum.setStatus("current")
_TnSysDebugTransfer_ObjectIdentity = ObjectIdentity
tnSysDebugTransfer = _TnSysDebugTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25)
)
_TnSysDebugTransferRemoteHostIp_Type = IpAddress
_TnSysDebugTransferRemoteHostIp_Object = MibScalar
tnSysDebugTransferRemoteHostIp = _TnSysDebugTransferRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 1),
    _TnSysDebugTransferRemoteHostIp_Type()
)
tnSysDebugTransferRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemoteHostIp.setStatus("current")


class _TnSysDebugTransferCommand_Type(Integer32):
    """Custom type tnSysDebugTransferCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferToRfs", 2))
    )


_TnSysDebugTransferCommand_Type.__name__ = "Integer32"
_TnSysDebugTransferCommand_Object = MibScalar
tnSysDebugTransferCommand = _TnSysDebugTransferCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 2),
    _TnSysDebugTransferCommand_Type()
)
tnSysDebugTransferCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferCommand.setStatus("current")


class _TnSysDebugTransferRemotePath_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysDebugTransferRemotePath_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferRemotePath_Object = MibScalar
tnSysDebugTransferRemotePath = _TnSysDebugTransferRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 3),
    _TnSysDebugTransferRemotePath_Type()
)
tnSysDebugTransferRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemotePath.setStatus("current")


class _TnSysDebugTransferStatus_Type(AluWdmTransferStatus):
    """Custom type tnSysDebugTransferStatus based on AluWdmTransferStatus"""
    defaultValue = 1


_TnSysDebugTransferStatus_Type.__name__ = "AluWdmTransferStatus"
_TnSysDebugTransferStatus_Object = MibScalar
tnSysDebugTransferStatus = _TnSysDebugTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 4),
    _TnSysDebugTransferStatus_Type()
)
tnSysDebugTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferStatus.setStatus("current")


class _TnSysDebugTransferProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysDebugTransferProtocol based on AluWdmTransferProtocol"""
    defaultValue = 1


_TnSysDebugTransferProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysDebugTransferProtocol_Object = MibScalar
tnSysDebugTransferProtocol = _TnSysDebugTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 5),
    _TnSysDebugTransferProtocol_Type()
)
tnSysDebugTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferProtocol.setStatus("current")


class _TnSysDebugTransferUserId_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysDebugTransferUserId_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferUserId_Object = MibScalar
tnSysDebugTransferUserId = _TnSysDebugTransferUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 6),
    _TnSysDebugTransferUserId_Type()
)
tnSysDebugTransferUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferUserId.setStatus("current")


class _TnSysDebugTransferPassword_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnSysDebugTransferPassword_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferPassword_Object = MibScalar
tnSysDebugTransferPassword = _TnSysDebugTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 7),
    _TnSysDebugTransferPassword_Type()
)
tnSysDebugTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferPassword.setStatus("current")


class _TnSysDebugTransferFilename_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferFilename based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysDebugTransferFilename_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferFilename_Object = MibScalar
tnSysDebugTransferFilename = _TnSysDebugTransferFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 8),
    _TnSysDebugTransferFilename_Type()
)
tnSysDebugTransferFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferFilename.setStatus("current")


class _TnSysDebugTransferRecentSuccessFile_Type(SnmpAdminString):
    """Custom type tnSysDebugTransferRecentSuccessFile based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysDebugTransferRecentSuccessFile_Type.__name__ = "SnmpAdminString"
_TnSysDebugTransferRecentSuccessFile_Object = MibScalar
tnSysDebugTransferRecentSuccessFile = _TnSysDebugTransferRecentSuccessFile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 9),
    _TnSysDebugTransferRecentSuccessFile_Type()
)
tnSysDebugTransferRecentSuccessFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferRecentSuccessFile.setStatus("current")


class _TnSysDebugTransferTimestamp_Type(Unsigned32):
    """Custom type tnSysDebugTransferTimestamp based on Unsigned32"""
    defaultValue = 0


_TnSysDebugTransferTimestamp_Type.__name__ = "Unsigned32"
_TnSysDebugTransferTimestamp_Object = MibScalar
tnSysDebugTransferTimestamp = _TnSysDebugTransferTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 10),
    _TnSysDebugTransferTimestamp_Type()
)
tnSysDebugTransferTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferTimestamp.setStatus("current")


class _TnSysDebugTransferShelfNum_Type(Integer32):
    """Custom type tnSysDebugTransferShelfNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TnSysDebugTransferShelfNum_Type.__name__ = "Integer32"
_TnSysDebugTransferShelfNum_Object = MibScalar
tnSysDebugTransferShelfNum = _TnSysDebugTransferShelfNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 11),
    _TnSysDebugTransferShelfNum_Type()
)
tnSysDebugTransferShelfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferShelfNum.setStatus("current")


class _TnSysDebugTransferPercentCompleted_Type(Unsigned32):
    """Custom type tnSysDebugTransferPercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysDebugTransferPercentCompleted_Type.__name__ = "Unsigned32"
_TnSysDebugTransferPercentCompleted_Object = MibScalar
tnSysDebugTransferPercentCompleted = _TnSysDebugTransferPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 12),
    _TnSysDebugTransferPercentCompleted_Type()
)
tnSysDebugTransferPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysDebugTransferPercentCompleted.setStatus("current")


class _TnSysDebugTransferRemoteInetAddress_Type(InetAddress):
    """Custom type tnSysDebugTransferRemoteInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysDebugTransferRemoteInetAddress_Type.__name__ = "InetAddress"
_TnSysDebugTransferRemoteInetAddress_Object = MibScalar
tnSysDebugTransferRemoteInetAddress = _TnSysDebugTransferRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 14),
    _TnSysDebugTransferRemoteInetAddress_Type()
)
tnSysDebugTransferRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemoteInetAddress.setStatus("current")


class _TnSysDebugTransferRemoteInetAddressType_Type(InetAddressType):
    """Custom type tnSysDebugTransferRemoteInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysDebugTransferRemoteInetAddressType_Type.__name__ = "InetAddressType"
_TnSysDebugTransferRemoteInetAddressType_Object = MibScalar
tnSysDebugTransferRemoteInetAddressType = _TnSysDebugTransferRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 25, 15),
    _TnSysDebugTransferRemoteInetAddressType_Type()
)
tnSysDebugTransferRemoteInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDebugTransferRemoteInetAddressType.setStatus("current")
_TnSysLicenseInv_ObjectIdentity = ObjectIdentity
tnSysLicenseInv = _TnSysLicenseInv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26)
)
_TnSysLicenseInvPathIp_Type = IpAddress
_TnSysLicenseInvPathIp_Object = MibScalar
tnSysLicenseInvPathIp = _TnSysLicenseInvPathIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 1),
    _TnSysLicenseInvPathIp_Type()
)
tnSysLicenseInvPathIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPathIp.setStatus("current")


class _TnSysLicenseInvFile_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvFile based on SnmpAdminString"""
    defaultValue = OctetString("./LicenseInv-file")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysLicenseInvFile_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvFile_Object = MibScalar
tnSysLicenseInvFile = _TnSysLicenseInvFile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 2),
    _TnSysLicenseInvFile_Type()
)
tnSysLicenseInvFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvFile.setStatus("current")


class _TnSysLicenseInvProtocol_Type(AluWdmTransferProtocol):
    """Custom type tnSysLicenseInvProtocol based on AluWdmTransferProtocol"""
    defaultValue = 3


_TnSysLicenseInvProtocol_Type.__name__ = "AluWdmTransferProtocol"
_TnSysLicenseInvProtocol_Object = MibScalar
tnSysLicenseInvProtocol = _TnSysLicenseInvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 3),
    _TnSysLicenseInvProtocol_Type()
)
tnSysLicenseInvProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvProtocol.setStatus("current")


class _TnSysLicenseInvUserId_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvUserId based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseInvUserId_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvUserId_Object = MibScalar
tnSysLicenseInvUserId = _TnSysLicenseInvUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 4),
    _TnSysLicenseInvUserId_Type()
)
tnSysLicenseInvUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvUserId.setStatus("current")


class _TnSysLicenseInvPassword_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvPassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseInvPassword_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvPassword_Object = MibScalar
tnSysLicenseInvPassword = _TnSysLicenseInvPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 5),
    _TnSysLicenseInvPassword_Type()
)
tnSysLicenseInvPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPassword.setStatus("current")


class _TnSysLicenseInvFileUploadOper_Type(TruthValue):
    """Custom type tnSysLicenseInvFileUploadOper based on TruthValue"""
    defaultValue = 2


_TnSysLicenseInvFileUploadOper_Type.__name__ = "TruthValue"
_TnSysLicenseInvFileUploadOper_Object = MibScalar
tnSysLicenseInvFileUploadOper = _TnSysLicenseInvFileUploadOper_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 6),
    _TnSysLicenseInvFileUploadOper_Type()
)
tnSysLicenseInvFileUploadOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvFileUploadOper.setStatus("current")


class _TnSysLicenseInvPathInetAddressType_Type(InetAddressType):
    """Custom type tnSysLicenseInvPathInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnSysLicenseInvPathInetAddressType_Type.__name__ = "InetAddressType"
_TnSysLicenseInvPathInetAddressType_Object = MibScalar
tnSysLicenseInvPathInetAddressType = _TnSysLicenseInvPathInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 7),
    _TnSysLicenseInvPathInetAddressType_Type()
)
tnSysLicenseInvPathInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPathInetAddressType.setStatus("current")


class _TnSysLicenseInvPathInetAddress_Type(InetAddress):
    """Custom type tnSysLicenseInvPathInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnSysLicenseInvPathInetAddress_Type.__name__ = "InetAddress"
_TnSysLicenseInvPathInetAddress_Object = MibScalar
tnSysLicenseInvPathInetAddress = _TnSysLicenseInvPathInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 8),
    _TnSysLicenseInvPathInetAddress_Type()
)
tnSysLicenseInvPathInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLicenseInvPathInetAddress.setStatus("current")


class _TnSysLicenseInvLastOperPercentCompleted_Type(Unsigned32):
    """Custom type tnSysLicenseInvLastOperPercentCompleted based on Unsigned32"""
    defaultValue = 0


_TnSysLicenseInvLastOperPercentCompleted_Type.__name__ = "Unsigned32"
_TnSysLicenseInvLastOperPercentCompleted_Object = MibScalar
tnSysLicenseInvLastOperPercentCompleted = _TnSysLicenseInvLastOperPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 9),
    _TnSysLicenseInvLastOperPercentCompleted_Type()
)
tnSysLicenseInvLastOperPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvLastOperPercentCompleted.setStatus("current")


class _TnSysLicenseInvLastUploadFileName_Type(SnmpAdminString):
    """Custom type tnSysLicenseInvLastUploadFileName based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnSysLicenseInvLastUploadFileName_Type.__name__ = "SnmpAdminString"
_TnSysLicenseInvLastUploadFileName_Object = MibScalar
tnSysLicenseInvLastUploadFileName = _TnSysLicenseInvLastUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 10),
    _TnSysLicenseInvLastUploadFileName_Type()
)
tnSysLicenseInvLastUploadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvLastUploadFileName.setStatus("current")


class _TnSysLicenseInvFileLastUploadStatus_Type(Integer32):
    """Custom type tnSysLicenseInvFileLastUploadStatus based on Integer32"""
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
        *(("success", 1),
          ("failure", 2),
          ("none", 3))
    )


_TnSysLicenseInvFileLastUploadStatus_Type.__name__ = "Integer32"
_TnSysLicenseInvFileLastUploadStatus_Object = MibScalar
tnSysLicenseInvFileLastUploadStatus = _TnSysLicenseInvFileLastUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 11),
    _TnSysLicenseInvFileLastUploadStatus_Type()
)
tnSysLicenseInvFileLastUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvFileLastUploadStatus.setStatus("current")


class _TnSysLicenseInvFileLastUploadTimeStamp_Type(Unsigned32):
    """Custom type tnSysLicenseInvFileLastUploadTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnSysLicenseInvFileLastUploadTimeStamp_Type.__name__ = "Unsigned32"
_TnSysLicenseInvFileLastUploadTimeStamp_Object = MibScalar
tnSysLicenseInvFileLastUploadTimeStamp = _TnSysLicenseInvFileLastUploadTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 26, 12),
    _TnSysLicenseInvFileLastUploadTimeStamp_Type()
)
tnSysLicenseInvFileLastUploadTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLicenseInvFileLastUploadTimeStamp.setStatus("current")
_TnSysDataDump_ObjectIdentity = ObjectIdentity
tnSysDataDump = _TnSysDataDump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 27)
)


class _TnSysDataDumpInfo_Type(Integer32):
    """Custom type tnSysDataDumpInfo based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("defectInfo", 2),
          ("provisionInfo", 3),
          ("transmissioninfo", 4),
          ("xcominfo", 5))
    )


_TnSysDataDumpInfo_Type.__name__ = "Integer32"
_TnSysDataDumpInfo_Object = MibScalar
tnSysDataDumpInfo = _TnSysDataDumpInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 27, 1),
    _TnSysDataDumpInfo_Type()
)
tnSysDataDumpInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysDataDumpInfo.setStatus("current")
_TnSysLinux_ObjectIdentity = ObjectIdentity
tnSysLinux = _TnSysLinux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28)
)


class _TnSysLinuxRootUserId_Type(SnmpAdminString):
    """Custom type tnSysLinuxRootUserId based on SnmpAdminString"""
    defaultValue = OctetString("root")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnSysLinuxRootUserId_Type.__name__ = "SnmpAdminString"
_TnSysLinuxRootUserId_Object = MibScalar
tnSysLinuxRootUserId = _TnSysLinuxRootUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 1),
    _TnSysLinuxRootUserId_Type()
)
tnSysLinuxRootUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserId.setStatus("current")


class _TnSysLinuxRootUserPassword_Type(SnmpAdminString):
    """Custom type tnSysLinuxRootUserPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysLinuxRootUserPassword_Type.__name__ = "SnmpAdminString"
_TnSysLinuxRootUserPassword_Object = MibScalar
tnSysLinuxRootUserPassword = _TnSysLinuxRootUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 2),
    _TnSysLinuxRootUserPassword_Type()
)
tnSysLinuxRootUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxRootUserPassword.setStatus("current")


class _TnSysLinuxApplUserId_Type(SnmpAdminString):
    """Custom type tnSysLinuxApplUserId based on SnmpAdminString"""
    defaultValue = OctetString("appl")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnSysLinuxApplUserId_Type.__name__ = "SnmpAdminString"
_TnSysLinuxApplUserId_Object = MibScalar
tnSysLinuxApplUserId = _TnSysLinuxApplUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 3),
    _TnSysLinuxApplUserId_Type()
)
tnSysLinuxApplUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysLinuxApplUserId.setStatus("current")


class _TnSysLinuxApplUserPassword_Type(SnmpAdminString):
    """Custom type tnSysLinuxApplUserPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysLinuxApplUserPassword_Type.__name__ = "SnmpAdminString"
_TnSysLinuxApplUserPassword_Object = MibScalar
tnSysLinuxApplUserPassword = _TnSysLinuxApplUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 28, 4),
    _TnSysLinuxApplUserPassword_Type()
)
tnSysLinuxApplUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLinuxApplUserPassword.setStatus("current")
_TnSysIpAclIpv6SysDefault_ObjectIdentity = ObjectIdentity
tnSysIpAclIpv6SysDefault = _TnSysIpAclIpv6SysDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29)
)


class _TnSysIpAclIpv6RxAction_Type(Integer32):
    """Custom type tnSysIpAclIpv6RxAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclIpv6RxAction_Type.__name__ = "Integer32"
_TnSysIpAclIpv6RxAction_Object = MibScalar
tnSysIpAclIpv6RxAction = _TnSysIpAclIpv6RxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 1),
    _TnSysIpAclIpv6RxAction_Type()
)
tnSysIpAclIpv6RxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6RxAction.setStatus("current")


class _TnSysIpAclIpv6TxAction_Type(Integer32):
    """Custom type tnSysIpAclIpv6TxAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("block", 2))
    )


_TnSysIpAclIpv6TxAction_Type.__name__ = "Integer32"
_TnSysIpAclIpv6TxAction_Object = MibScalar
tnSysIpAclIpv6TxAction = _TnSysIpAclIpv6TxAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 2),
    _TnSysIpAclIpv6TxAction_Type()
)
tnSysIpAclIpv6TxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6TxAction.setStatus("current")


class _TnSysIpAclIpv6SnmpCfgEnable_Type(TruthValue):
    """Custom type tnSysIpAclIpv6SnmpCfgEnable based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6SnmpCfgEnable_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6SnmpCfgEnable_Object = MibScalar
tnSysIpAclIpv6SnmpCfgEnable = _TnSysIpAclIpv6SnmpCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 3),
    _TnSysIpAclIpv6SnmpCfgEnable_Type()
)
tnSysIpAclIpv6SnmpCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6SnmpCfgEnable.setStatus("current")


class _TnSysIpAclIpv6CfgRestoreToDefault_Type(TruthValue):
    """Custom type tnSysIpAclIpv6CfgRestoreToDefault based on TruthValue"""
    defaultValue = 2


_TnSysIpAclIpv6CfgRestoreToDefault_Type.__name__ = "TruthValue"
_TnSysIpAclIpv6CfgRestoreToDefault_Object = MibScalar
tnSysIpAclIpv6CfgRestoreToDefault = _TnSysIpAclIpv6CfgRestoreToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 2, 29, 4),
    _TnSysIpAclIpv6CfgRestoreToDefault_Type()
)
tnSysIpAclIpv6CfgRestoreToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysIpAclIpv6CfgRestoreToDefault.setStatus("current")
snmpTargetAddrEntry.registerAugmentions(
    ("TROPIC-SYSTEM-MIB",
     "tnSnmpTargetAddrEntry")
)
tnSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups

tnSystemBasicsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 1)
)
tnSystemBasicsGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDescr"),
        ("TROPIC-SYSTEM-MIB", "tnSysTelnetPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysHttpPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysDateAndTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysReset"),
        ("TROPIC-SYSTEM-MIB", "tnSysMIBVersion"),
        ("TROPIC-SYSTEM-MIB", "tnSysRingID"),
        ("TROPIC-SYSTEM-MIB", "tnSysNetworkElementID"),
        ("TROPIC-SYSTEM-MIB", "tnSysAINSDebounceTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysSonetSdhMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysAlarmReportingControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysWavelengthTrackerWaveKeySpace"),
        ("TROPIC-SYSTEM-MIB", "tnSysSecureMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysExtendedTemperatureRange"),
        ("TROPIC-SYSTEM-MIB", "tnSysTemperatureInCelsius"),
        ("TROPIC-SYSTEM-MIB", "tnSysName"),
        ("TROPIC-SYSTEM-MIB", "tnSysEquipmentControllerCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysFirstLevelControllerCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysMatrix0CompactCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysUniversalMatrixFirstLevelControllerCapacity"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimeOffsetTimeZone"),
        ("TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
        ("TROPIC-SYSTEM-MIB", "tnSysFipsSquelchMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrListOfFileNames"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrFileCounts"),
        ("TROPIC-SYSTEM-MIB", "tnSysAltitude"),
        ("TROPIC-SYSTEM-MIB", "tnSysThermalShutdownAutotimer"),
        ("TROPIC-SYSTEM-MIB", "tnSysDisplayShelfLabel"),
        ("TROPIC-SYSTEM-MIB", "tnSysPMFineGranularityControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysFmRead"),
        ("TROPIC-SYSTEM-MIB", "tnSysPMStreamingServerControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysSlotMigrationControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysFlexGridClusterOcsAddDropEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysFilterCheckTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysCNLinkPhysicalIfIndex"))
)
if mibBuilder.loadTexts:
    tnSystemBasicsGroup.setStatus("current")

tnSystemControlNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 2)
)
tnSystemControlNetworkGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysSubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSnmpSource"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredOcsIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredOcs2IpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredOcs3IpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcs1LinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcs2LinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcs3LinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredRadiusSource"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredLoopbackIp1"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredLoopbackIp1SubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSnmpSource1"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredRadiusSource1"),
        ("TROPIC-SYSTEM-MIB", "tnSysLoopbackIpAddress1"),
        ("TROPIC-SYSTEM-MIB", "tnSysLoopbackIp1SubnetMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredPrefixLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcsIp1Password"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcsIp2Password"),
        ("TROPIC-SYSTEM-MIB", "tnSysOcsIp3Password"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredSnmpSourceIPv6"),
        ("TROPIC-SYSTEM-MIB", "tnSysConfiguredRadiusSourceIPv6"))
)
if mibBuilder.loadTexts:
    tnSystemControlNetworkGroup.setStatus("current")

tnSystemRedundancyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 3)
)
tnSystemRedundancyGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbSynchState"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbResynch"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbAudit"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbClear"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyActiveCCSlot"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyDbInvalid"),
        ("TROPIC-SYSTEM-MIB", "tnSysRedundancyMateCCReadyToProtect"))
)
if mibBuilder.loadTexts:
    tnSystemRedundancyGroup.setStatus("current")

tnSystemDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 4)
)
tnSystemDiscoveryGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDiscoveryFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryMask"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryErrorCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryBinnedStatsInterval"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryBinnedStatsBin"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysDiscoveryServerInetAddress"))
)
if mibBuilder.loadTexts:
    tnSystemDiscoveryGroup.setStatus("current")

tnSystemLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 5)
)
tnSystemLoggingGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLoggingCLI"),
        ("TROPIC-SYSTEM-MIB", "tnSysLoggingSNMP"))
)
if mibBuilder.loadTexts:
    tnSystemLoggingGroup.setStatus("current")

tnSystemBackupAndRestoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 6)
)
tnSystemBackupAndRestoreGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastBackupFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestorePercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastBackupFileTimeStamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestorePassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreLastBackupFileCrc"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemoteHostInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysBackupAndRestoreRemoteHostInetAddress"))
)
if mibBuilder.loadTexts:
    tnSystemBackupAndRestoreGroup.setStatus("current")

tnSysNtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 7)
)
tnSysNtpGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpSynched"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerCurrentIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpDriftString"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpTimeOffsetString"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpClockMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerCurrentInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerCurrentInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysNtpGroup.setStatus("current")

tnSysNtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 8)
)
tnSysNtpServerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpServerIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerKeyIndex"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerInetAddressType"))
)
if mibBuilder.loadTexts:
    tnSysNtpServerGroup.setStatus("current")

tnSnmpTargetAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 9)
)
tnSnmpTargetAddressGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddrNmsStationGroupId"),
        ("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddrTrapGroupId"))
)
if mibBuilder.loadTexts:
    tnSnmpTargetAddressGroup.setStatus("current")

tnSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 10)
)
tnSyslogGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSyslogIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogPort"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogFacility"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogPriority"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogInetAddressType"))
)
if mibBuilder.loadTexts:
    tnSyslogGroup.setStatus("current")

tnSysTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 11)
)
tnSysTimingGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReference"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReference"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingLastSwitchTime"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReferenceStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReferenceStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReferenceQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReferenceQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingPrimaryReferenceTimingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSecondaryReferenceTimingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingActiveReference"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingClockingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingSwitchingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingFreeRunSuppressAlarms"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingDs1FramingMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingDs1LineCoding"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingDs1SsmProcessing"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsAClockQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsBClockQuality"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingActiveLineTimingCable"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitSourceType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsAModuleType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingBitsBModuleType"))
)
if mibBuilder.loadTexts:
    tnSysTimingGroup.setStatus("current")

tnSysFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 12)
)
tnSysFeaturesGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysFeatureAutoTopology"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeaturePauseFlowControl"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeatureIpUtilitiesRestricted"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeatureFastServiceSetup"))
)
if mibBuilder.loadTexts:
    tnSysFeaturesGroup.setStatus("current")

tnSysFaultCorrelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 13)
)
tnSysFaultCorrelationGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysFaultCorrelationTransientSuppression")
)
if mibBuilder.loadTexts:
    tnSysFaultCorrelationGroup.setStatus("current")

tnSysErrorHandlingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 14)
)
tnSysErrorHandlingGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysSetRequestErrorMessage")
)
if mibBuilder.loadTexts:
    tnSysErrorHandlingGroup.setStatus("current")

tnSysSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 15)
)
tnSysSecurityGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysSecurityMode"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyType"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyModulus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshPublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSshKeyGenerationStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyType"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyModulus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslPublicKey"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslKeyGenerationStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemoteIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemoteUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertTransferRemotePassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrCountry"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrState"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrLocality"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrOrganization"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrOrganizationUnit"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrCommonName"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrEmailAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertSignatureAlgorithm"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertValidity"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrUploadStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertDownloadStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCertInstallStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysSslCsrGenerationStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSshKeyTypeIndex"),
        ("TROPIC-SYSTEM-MIB", "tnSshPublicKey"))
)
if mibBuilder.loadTexts:
    tnSysSecurityGroup.setStatus("current")

tnSysTransferLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 16)
)
tnSysTransferLogGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysTransferLogCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogLastLogFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogLastCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogLastFileTimeStamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogWindowStart"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogWindowStop"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemoteHostInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogRemoteHostInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysTransferLogGroup.setStatus("current")

tnSysIpAclSysDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 17)
)
tnSysIpAclSysDefaultGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclRxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclTxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSnmpCfgEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclCfgRestoreToDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclSysDefaultGroup.setStatus("current")

tnSysIpAclPatternScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 18)
)
tnSysIpAclPatternScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternScalarsGroup.setStatus("current")

tnSysIpAclPatternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 19)
)
tnSysIpAclPatternGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternICMPERROR"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcPrefix"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestAddr"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestPrefix"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternDestPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIpProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIpFragment"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIcmpType"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternIcmpCode"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternTcpEstablish"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSrcPort"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclPatternGroup.setStatus("current")

tnSysIpAclFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 20)
)
tnSysIpAclFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterScalarsGroup.setStatus("current")

tnSysIpAclFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 21)
)
tnSysIpAclFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterPatternID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterStatCount"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclFilterGroup.setStatus("current")

tnSysIpAclInterfaceScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 22)
)
tnSysIpAclInterfaceScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceScalarsGroup.setStatus("current")

tnSysIpAclInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 23)
)
tnSysIpAclInterfaceGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclInterfaceGroup.setStatus("current")

tnSysNtpServerIdStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 24)
)
tnSysNtpServerIdStatsGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsSelect"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsRefId"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsStrtm"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsClockType"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsPoll"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsReach"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsDelay"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsOffset"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsJitter"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsKeyIndex"))
)
if mibBuilder.loadTexts:
    tnSysNtpServerIdStatsGroup.setStatus("current")

tnSysFtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 25)
)
tnSysFtpServerGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysFtpServerEnabled"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpServerPassword"))
)
if mibBuilder.loadTexts:
    tnSysFtpServerGroup.setStatus("current")

tnSysNtpServerAuthenticationScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 26)
)
tnSysNtpServerAuthenticationScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationScalarsGroup.setStatus("current")

tnSysNtpServerAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 27)
)
tnSysNtpServerAuthenticationGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationKeyType"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationKey"))
)
if mibBuilder.loadTexts:
    tnSysNtpServerAuthenticationGroup.setStatus("current")

tnSysIpAclNetIfFilterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 28)
)
tnSysIpAclNetIfFilterScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterScalarsGroup.setStatus("current")

tnSysIpAclNetIfFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 29)
)
tnSysIpAclNetIfFilterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterID"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterSystemDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclNetIfFilterGroup.setStatus("current")

tnNeDiscoveryScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 30)
)
tnNeDiscoveryScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryAttributeTotal")
)
if mibBuilder.loadTexts:
    tnNeDiscoveryScalarsGroup.setStatus("current")

tnNeDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 31)
)
tnNeDiscoveryGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnNeDiscoveryFilename"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryControl"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryStatus"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryErrorCode"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerIp"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerUserId"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerPassword"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerTimeOut"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryServerInetAddress"))
)
if mibBuilder.loadTexts:
    tnNeDiscoveryGroup.setStatus("current")

tnSysOtdrScanSystemProfileScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 32)
)
tnSysOtdrScanSystemProfileScalarsGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileScalarsGroup.setStatus("current")

tnSysOtdrScanSystemProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 33)
)
tnSysOtdrScanSystemProfileGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileDescription"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileWaveLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfilePulseLength"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileRange"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileResolution"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileAvgTime"))
)
if mibBuilder.loadTexts:
    tnSysOtdrScanSystemProfileGroup.setStatus("current")

tnSysOtdrScanTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 34)
)
tnSysOtdrScanTransferGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysOtdrScanTransferGroup.setStatus("current")

tnClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 35)
)
tnClusterGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnClusterRowStatus"),
        ("TROPIC-SYSTEM-MIB", "tnClusterFarEndNode"),
        ("TROPIC-SYSTEM-MIB", "tnClusterIpAddress"),
        ("TROPIC-SYSTEM-MIB", "tnClusterlinkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnClusterInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnClusterInetAddress"))
)
if mibBuilder.loadTexts:
    tnClusterGroup.setStatus("current")

tnSysPmFetchBulkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 36)
)
tnSysPmFetchBulkGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkStart"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkStatsInterval"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkBinnedStatsBin"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkShelfNum"))
)
if mibBuilder.loadTexts:
    tnSysPmFetchBulkGroup.setStatus("current")

tnSysDebugTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 37)
)
tnSysDebugTransferGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemoteHostIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferCommand"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemotePath"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferFilename"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRecentSuccessFile"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferTimestamp"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferShelfNum"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferPercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemoteInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferRemoteInetAddress"))
)
if mibBuilder.loadTexts:
    tnSysDebugTransferGroup.setStatus("current")

tnSysLicenseInvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 38)
)
tnSysLicenseInvGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPathIp"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFile"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvProtocol"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFileUploadOper"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPathInetAddressType"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvPathInetAddress"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvLastOperPercentCompleted"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvLastUploadFileName"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFileLastUploadStatus"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvFileLastUploadTimeStamp"))
)
if mibBuilder.loadTexts:
    tnSysLicenseInvGroup.setStatus("current")

tnSysDataDumpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 39)
)
tnSysDataDumpInfoGroup.setObjects(
    ("TROPIC-SYSTEM-MIB", "tnSysDataDumpInfo")
)
if mibBuilder.loadTexts:
    tnSysDataDumpInfoGroup.setStatus("current")

tnSysLinuxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 40)
)
tnSysLinuxGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxRootUserPassword"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxApplUserId"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxApplUserPassword"))
)
if mibBuilder.loadTexts:
    tnSysLinuxGroup.setStatus("current")

tnSysIpAclIpv6SysDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 1, 41)
)
tnSysIpAclIpv6SysDefaultGroup.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6RxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6TxAction"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6SnmpCfgEnable"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6CfgRestoreToDefault"))
)
if mibBuilder.loadTexts:
    tnSysIpAclIpv6SysDefaultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1, 1, 2, 1)
)
tnSystemCompliance.setObjects(
      *(("TROPIC-SYSTEM-MIB", "tnSystemBasicsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemControlNetworkGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemRedundancyGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemDiscoveryGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemLoggingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSystemBackupAndRestoreGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSnmpTargetAddressGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSyslogGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysTimingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysFeaturesGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysErrorHandlingGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysSecurityGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysTransferLogGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclSysDefaultGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclPatternGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclInterfaceGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerIdStatsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysFtpServerGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysNtpServerAuthenticationGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclNetIfFilterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnNeDiscoveryGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileScalarsGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanSystemProfileGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysOtdrScanTransferGroup"),
        ("TROPIC-SYSTEM-MIB", "tnClusterGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysPmFetchBulkGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysDebugTransferGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysLicenseInvGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysDataDumpInfoGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysLinuxGroup"),
        ("TROPIC-SYSTEM-MIB", "tnSysIpAclIpv6SysDefaultGroup"))
)
if mibBuilder.loadTexts:
    tnSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SYSTEM-MIB",
    **{"TropicSysTimingReferenceQuality": TropicSysTimingReferenceQuality,
       "TropicSysTimingReferenceTimingMode": TropicSysTimingReferenceTimingMode,
       "AluWdmSslOperationStatus": AluWdmSslOperationStatus,
       "AluWdmTransferStatus": AluWdmTransferStatus,
       "AluWdmOcsLinkStatus": AluWdmOcsLinkStatus,
       "tnSystemMibModule": tnSystemMibModule,
       "tnSystemConf": tnSystemConf,
       "tnSystemGroups": tnSystemGroups,
       "tnSystemBasicsGroup": tnSystemBasicsGroup,
       "tnSystemControlNetworkGroup": tnSystemControlNetworkGroup,
       "tnSystemRedundancyGroup": tnSystemRedundancyGroup,
       "tnSystemDiscoveryGroup": tnSystemDiscoveryGroup,
       "tnSystemLoggingGroup": tnSystemLoggingGroup,
       "tnSystemBackupAndRestoreGroup": tnSystemBackupAndRestoreGroup,
       "tnSysNtpGroup": tnSysNtpGroup,
       "tnSysNtpServerGroup": tnSysNtpServerGroup,
       "tnSnmpTargetAddressGroup": tnSnmpTargetAddressGroup,
       "tnSyslogGroup": tnSyslogGroup,
       "tnSysTimingGroup": tnSysTimingGroup,
       "tnSysFeaturesGroup": tnSysFeaturesGroup,
       "tnSysFaultCorrelationGroup": tnSysFaultCorrelationGroup,
       "tnSysErrorHandlingGroup": tnSysErrorHandlingGroup,
       "tnSysSecurityGroup": tnSysSecurityGroup,
       "tnSysTransferLogGroup": tnSysTransferLogGroup,
       "tnSysIpAclSysDefaultGroup": tnSysIpAclSysDefaultGroup,
       "tnSysIpAclPatternScalarsGroup": tnSysIpAclPatternScalarsGroup,
       "tnSysIpAclPatternGroup": tnSysIpAclPatternGroup,
       "tnSysIpAclFilterScalarsGroup": tnSysIpAclFilterScalarsGroup,
       "tnSysIpAclFilterGroup": tnSysIpAclFilterGroup,
       "tnSysIpAclInterfaceScalarsGroup": tnSysIpAclInterfaceScalarsGroup,
       "tnSysIpAclInterfaceGroup": tnSysIpAclInterfaceGroup,
       "tnSysNtpServerIdStatsGroup": tnSysNtpServerIdStatsGroup,
       "tnSysFtpServerGroup": tnSysFtpServerGroup,
       "tnSysNtpServerAuthenticationScalarsGroup": tnSysNtpServerAuthenticationScalarsGroup,
       "tnSysNtpServerAuthenticationGroup": tnSysNtpServerAuthenticationGroup,
       "tnSysIpAclNetIfFilterScalarsGroup": tnSysIpAclNetIfFilterScalarsGroup,
       "tnSysIpAclNetIfFilterGroup": tnSysIpAclNetIfFilterGroup,
       "tnNeDiscoveryScalarsGroup": tnNeDiscoveryScalarsGroup,
       "tnNeDiscoveryGroup": tnNeDiscoveryGroup,
       "tnSysOtdrScanSystemProfileScalarsGroup": tnSysOtdrScanSystemProfileScalarsGroup,
       "tnSysOtdrScanSystemProfileGroup": tnSysOtdrScanSystemProfileGroup,
       "tnSysOtdrScanTransferGroup": tnSysOtdrScanTransferGroup,
       "tnClusterGroup": tnClusterGroup,
       "tnSysPmFetchBulkGroup": tnSysPmFetchBulkGroup,
       "tnSysDebugTransferGroup": tnSysDebugTransferGroup,
       "tnSysLicenseInvGroup": tnSysLicenseInvGroup,
       "tnSysDataDumpInfoGroup": tnSysDataDumpInfoGroup,
       "tnSysLinuxGroup": tnSysLinuxGroup,
       "tnSysIpAclIpv6SysDefaultGroup": tnSysIpAclIpv6SysDefaultGroup,
       "tnSystemCompliances": tnSystemCompliances,
       "tnSystemCompliance": tnSystemCompliance,
       "tnSystemObjs": tnSystemObjs,
       "tnSysBasics": tnSysBasics,
       "tnSysDescr": tnSysDescr,
       "tnSysTelnetPort": tnSysTelnetPort,
       "tnSysHttpPort": tnSysHttpPort,
       "tnSysDateAndTime": tnSysDateAndTime,
       "tnSysReset": tnSysReset,
       "tnSysMIBVersion": tnSysMIBVersion,
       "tnSysRingID": tnSysRingID,
       "tnSysNetworkElementID": tnSysNetworkElementID,
       "tnSysAINSDebounceTime": tnSysAINSDebounceTime,
       "tnSysSonetSdhMode": tnSysSonetSdhMode,
       "tnSysAlarmReportingControl": tnSysAlarmReportingControl,
       "tnSysWavelengthTrackerWaveKeySpace": tnSysWavelengthTrackerWaveKeySpace,
       "tnSysSecureMode": tnSysSecureMode,
       "tnSysExtendedTemperatureRange": tnSysExtendedTemperatureRange,
       "tnSysTemperatureInCelsius": tnSysTemperatureInCelsius,
       "tnSysName": tnSysName,
       "tnSysEquipmentControllerCapacity": tnSysEquipmentControllerCapacity,
       "tnSysFirstLevelControllerCapacity": tnSysFirstLevelControllerCapacity,
       "tnSysMatrix0CompactCapacity": tnSysMatrix0CompactCapacity,
       "tnSysUniversalMatrixFirstLevelControllerCapacity": tnSysUniversalMatrixFirstLevelControllerCapacity,
       "tnSysTimeOffsetTimeZone": tnSysTimeOffsetTimeZone,
       "tnSysSwitchId": tnSysSwitchId,
       "tnSysFipsSquelchMode": tnSysFipsSquelchMode,
       "tnSysOtdrListOfFileNames": tnSysOtdrListOfFileNames,
       "tnSysOtdrFileCounts": tnSysOtdrFileCounts,
       "tnSysAltitude": tnSysAltitude,
       "tnSysThermalShutdownAutotimer": tnSysThermalShutdownAutotimer,
       "tnSysDisplayShelfLabel": tnSysDisplayShelfLabel,
       "tnSysPMFineGranularityControl": tnSysPMFineGranularityControl,
       "tnSysFmRead": tnSysFmRead,
       "tnSysPMStreamingServerControl": tnSysPMStreamingServerControl,
       "tnSysSlotMigrationControl": tnSysSlotMigrationControl,
       "tnSysFlexGridClusterOcsAddDropEnabled": tnSysFlexGridClusterOcsAddDropEnabled,
       "tnSysFilterCheckTime": tnSysFilterCheckTime,
       "tnSysCNLinkPhysicalIfIndex": tnSysCNLinkPhysicalIfIndex,
       "tnSysControlNetwork": tnSysControlNetwork,
       "tnSysIpAddress": tnSysIpAddress,
       "tnSysSubnetMask": tnSysSubnetMask,
       "tnSysConfiguredIpAddress": tnSysConfiguredIpAddress,
       "tnSysConfiguredSubnetMask": tnSysConfiguredSubnetMask,
       "tnSysConfiguredSnmpSource": tnSysConfiguredSnmpSource,
       "tnSysConfiguredOcsIpAddress": tnSysConfiguredOcsIpAddress,
       "tnSysConfiguredOcs2IpAddress": tnSysConfiguredOcs2IpAddress,
       "tnSysConfiguredOcs3IpAddress": tnSysConfiguredOcs3IpAddress,
       "tnSysOcs1LinkStatus": tnSysOcs1LinkStatus,
       "tnSysOcs2LinkStatus": tnSysOcs2LinkStatus,
       "tnSysOcs3LinkStatus": tnSysOcs3LinkStatus,
       "tnSysConfiguredRadiusSource": tnSysConfiguredRadiusSource,
       "tnSysConfiguredLoopbackIp1": tnSysConfiguredLoopbackIp1,
       "tnSysConfiguredLoopbackIp1SubnetMask": tnSysConfiguredLoopbackIp1SubnetMask,
       "tnSysConfiguredSnmpSource1": tnSysConfiguredSnmpSource1,
       "tnSysConfiguredRadiusSource1": tnSysConfiguredRadiusSource1,
       "tnSysLoopbackIpAddress1": tnSysLoopbackIpAddress1,
       "tnSysLoopbackIp1SubnetMask": tnSysLoopbackIp1SubnetMask,
       "tnSysConfiguredInetAddressType": tnSysConfiguredInetAddressType,
       "tnSysConfiguredInetAddress": tnSysConfiguredInetAddress,
       "tnSysConfiguredPrefixLength": tnSysConfiguredPrefixLength,
       "tnSysOcsIp1Password": tnSysOcsIp1Password,
       "tnSysOcsIp2Password": tnSysOcsIp2Password,
       "tnSysOcsIp3Password": tnSysOcsIp3Password,
       "tnSysConfiguredSnmpSourceIPv6": tnSysConfiguredSnmpSourceIPv6,
       "tnSysConfiguredRadiusSourceIPv6": tnSysConfiguredRadiusSourceIPv6,
       "tnSysRedundancy": tnSysRedundancy,
       "tnSysRedundancyDbSynchState": tnSysRedundancyDbSynchState,
       "tnSysRedundancyDbResynch": tnSysRedundancyDbResynch,
       "tnSysRedundancyDbAudit": tnSysRedundancyDbAudit,
       "tnSysRedundancyDbClear": tnSysRedundancyDbClear,
       "tnSysRedundancyActiveCCSlot": tnSysRedundancyActiveCCSlot,
       "tnSysRedundancyDbInvalid": tnSysRedundancyDbInvalid,
       "tnSysRedundancyMateCCReadyToProtect": tnSysRedundancyMateCCReadyToProtect,
       "tnSysDiscovery": tnSysDiscovery,
       "tnSysDiscoveryFilename": tnSysDiscoveryFilename,
       "tnSysDiscoveryMask": tnSysDiscoveryMask,
       "tnSysDiscoveryControl": tnSysDiscoveryControl,
       "tnSysDiscoveryStatus": tnSysDiscoveryStatus,
       "tnSysDiscoveryErrorCode": tnSysDiscoveryErrorCode,
       "tnSysDiscoveryBinnedStatsInterval": tnSysDiscoveryBinnedStatsInterval,
       "tnSysDiscoveryBinnedStatsBin": tnSysDiscoveryBinnedStatsBin,
       "tnSysDiscoveryServerProtocol": tnSysDiscoveryServerProtocol,
       "tnSysDiscoveryServerIp": tnSysDiscoveryServerIp,
       "tnSysDiscoveryServerUserId": tnSysDiscoveryServerUserId,
       "tnSysDiscoveryServerPassword": tnSysDiscoveryServerPassword,
       "tnSysDiscoveryServerInetAddressType": tnSysDiscoveryServerInetAddressType,
       "tnSysDiscoveryServerInetAddress": tnSysDiscoveryServerInetAddress,
       "tnSysLogging": tnSysLogging,
       "tnSysLoggingCLI": tnSysLoggingCLI,
       "tnSysLoggingSNMP": tnSysLoggingSNMP,
       "tnSysBackupAndRestore": tnSysBackupAndRestore,
       "tnSysBackupAndRestoreCommand": tnSysBackupAndRestoreCommand,
       "tnSysBackupAndRestoreRemoteHostIp": tnSysBackupAndRestoreRemoteHostIp,
       "tnSysBackupAndRestoreRemotePath": tnSysBackupAndRestoreRemotePath,
       "tnSysBackupAndRestoreStatus": tnSysBackupAndRestoreStatus,
       "tnSysBackupAndRestoreLastBackupFilename": tnSysBackupAndRestoreLastBackupFilename,
       "tnSysBackupAndRestoreLastCommand": tnSysBackupAndRestoreLastCommand,
       "tnSysBackupAndRestorePercentCompleted": tnSysBackupAndRestorePercentCompleted,
       "tnSysBackupAndRestoreLastBackupFileTimeStamp": tnSysBackupAndRestoreLastBackupFileTimeStamp,
       "tnSysBackupAndRestoreProtocol": tnSysBackupAndRestoreProtocol,
       "tnSysBackupAndRestoreUserId": tnSysBackupAndRestoreUserId,
       "tnSysBackupAndRestorePassword": tnSysBackupAndRestorePassword,
       "tnSysBackupAndRestoreLastBackupFileCrc": tnSysBackupAndRestoreLastBackupFileCrc,
       "tnSysBackupAndRestoreRemoteHostInetAddressType": tnSysBackupAndRestoreRemoteHostInetAddressType,
       "tnSysBackupAndRestoreRemoteHostInetAddress": tnSysBackupAndRestoreRemoteHostInetAddress,
       "tnSysNtp": tnSysNtp,
       "tnSysNtpEnable": tnSysNtpEnable,
       "tnSysNtpSynched": tnSysNtpSynched,
       "tnSysNtpServerCurrentIpAddress": tnSysNtpServerCurrentIpAddress,
       "tnSysNtpDriftString": tnSysNtpDriftString,
       "tnSysNtpTimeOffsetString": tnSysNtpTimeOffsetString,
       "tnSysNtpClockMode": tnSysNtpClockMode,
       "tnSysNtpServerCurrentInetAddressType": tnSysNtpServerCurrentInetAddressType,
       "tnSysNtpServerCurrentInetAddress": tnSysNtpServerCurrentInetAddress,
       "tnSysNtpServers": tnSysNtpServers,
       "tnSysNtpServerTable": tnSysNtpServerTable,
       "tnSysNtpServerEntry": tnSysNtpServerEntry,
       "tnSysNtpServerIndex": tnSysNtpServerIndex,
       "tnSysNtpServerIpAddress": tnSysNtpServerIpAddress,
       "tnSysNtpServerRowStatus": tnSysNtpServerRowStatus,
       "tnSysNtpServerKeyIndex": tnSysNtpServerKeyIndex,
       "tnSysNtpServerInetAddress": tnSysNtpServerInetAddress,
       "tnSysNtpServerInetAddressType": tnSysNtpServerInetAddressType,
       "tnSnmpTargetAddresses": tnSnmpTargetAddresses,
       "tnSnmpTargetAddrTable": tnSnmpTargetAddrTable,
       "tnSnmpTargetAddrEntry": tnSnmpTargetAddrEntry,
       "tnSnmpTargetAddrNmsStationGroupId": tnSnmpTargetAddrNmsStationGroupId,
       "tnSnmpTargetAddrTrapGroupId": tnSnmpTargetAddrTrapGroupId,
       "tnSyslog": tnSyslog,
       "tnSyslogIpAddress": tnSyslogIpAddress,
       "tnSyslogPort": tnSyslogPort,
       "tnSyslogFacility": tnSyslogFacility,
       "tnSyslogPriority": tnSyslogPriority,
       "tnSyslogEnabled": tnSyslogEnabled,
       "tnSyslogInetAddress": tnSyslogInetAddress,
       "tnSyslogInetAddressType": tnSyslogInetAddressType,
       "tnSysTiming": tnSysTiming,
       "tnSysTimingPrimaryReference": tnSysTimingPrimaryReference,
       "tnSysTimingSecondaryReference": tnSysTimingSecondaryReference,
       "tnSysTimingLastSwitchTime": tnSysTimingLastSwitchTime,
       "tnSysTimingControl": tnSysTimingControl,
       "tnSysTimingPrimaryReferenceStatus": tnSysTimingPrimaryReferenceStatus,
       "tnSysTimingSecondaryReferenceStatus": tnSysTimingSecondaryReferenceStatus,
       "tnSysTimingPrimaryReferenceQuality": tnSysTimingPrimaryReferenceQuality,
       "tnSysTimingSecondaryReferenceQuality": tnSysTimingSecondaryReferenceQuality,
       "tnSysTimingPrimaryReferenceTimingMode": tnSysTimingPrimaryReferenceTimingMode,
       "tnSysTimingSecondaryReferenceTimingMode": tnSysTimingSecondaryReferenceTimingMode,
       "tnSysTimingActiveReference": tnSysTimingActiveReference,
       "tnSysTimingClockingMode": tnSysTimingClockingMode,
       "tnSysTimingSwitchingMode": tnSysTimingSwitchingMode,
       "tnSysTimingFreeRunSuppressAlarms": tnSysTimingFreeRunSuppressAlarms,
       "tnSysTimingDs1FramingMode": tnSysTimingDs1FramingMode,
       "tnSysTimingDs1LineCoding": tnSysTimingDs1LineCoding,
       "tnSysTimingDs1SsmProcessing": tnSysTimingDs1SsmProcessing,
       "tnSysTimingBitsAClockQuality": tnSysTimingBitsAClockQuality,
       "tnSysTimingBitsBClockQuality": tnSysTimingBitsBClockQuality,
       "tnSysTimingActiveLineTimingCable": tnSysTimingActiveLineTimingCable,
       "tnSysTimingBitSourceType": tnSysTimingBitSourceType,
       "tnSysTimingBitsAModuleType": tnSysTimingBitsAModuleType,
       "tnSysTimingBitsBModuleType": tnSysTimingBitsBModuleType,
       "tnSysFeatures": tnSysFeatures,
       "tnSysFeatureAutoTopology": tnSysFeatureAutoTopology,
       "tnSysFeaturePauseFlowControl": tnSysFeaturePauseFlowControl,
       "tnSysFeatureIpUtilitiesRestricted": tnSysFeatureIpUtilitiesRestricted,
       "tnSysFeatureFastServiceSetup": tnSysFeatureFastServiceSetup,
       "tnSysFaultCorrelation": tnSysFaultCorrelation,
       "tnSysFaultCorrelationTransientSuppression": tnSysFaultCorrelationTransientSuppression,
       "tnSysErrorHandling": tnSysErrorHandling,
       "tnSysSetRequestErrorMessage": tnSysSetRequestErrorMessage,
       "tnSysSecurity": tnSysSecurity,
       "tnSysSecurityMode": tnSysSecurityMode,
       "tnSysSsh": tnSysSsh,
       "tnSysSshKeyType": tnSysSshKeyType,
       "tnSysSshKeyModulus": tnSysSshKeyModulus,
       "tnSysSshPublicKey": tnSysSshPublicKey,
       "tnSysSshKeyCommand": tnSysSshKeyCommand,
       "tnSysSshKeyGenerationStatus": tnSysSshKeyGenerationStatus,
       "tnSysSsl": tnSysSsl,
       "tnSysSslKeyType": tnSysSslKeyType,
       "tnSysSslKeyModulus": tnSysSslKeyModulus,
       "tnSysSslPublicKey": tnSysSslPublicKey,
       "tnSysSslKeyCommand": tnSysSslKeyCommand,
       "tnSysSslKeyGenerationStatus": tnSysSslKeyGenerationStatus,
       "tnSysSslCertTransferCommand": tnSysSslCertTransferCommand,
       "tnSysSslCertTransferProtocol": tnSysSslCertTransferProtocol,
       "tnSysSslCertTransferRemoteIp": tnSysSslCertTransferRemoteIp,
       "tnSysSslCertTransferRemotePath": tnSysSslCertTransferRemotePath,
       "tnSysSslCertTransferRemoteUserId": tnSysSslCertTransferRemoteUserId,
       "tnSysSslCertTransferRemotePassword": tnSysSslCertTransferRemotePassword,
       "tnSysSslCsrCommand": tnSysSslCsrCommand,
       "tnSysSslCsrCountry": tnSysSslCsrCountry,
       "tnSysSslCsrState": tnSysSslCsrState,
       "tnSysSslCsrLocality": tnSysSslCsrLocality,
       "tnSysSslCsrOrganization": tnSysSslCsrOrganization,
       "tnSysSslCsrOrganizationUnit": tnSysSslCsrOrganizationUnit,
       "tnSysSslCsrCommonName": tnSysSslCsrCommonName,
       "tnSysSslCsrEmailAddress": tnSysSslCsrEmailAddress,
       "tnSysSslCertCommand": tnSysSslCertCommand,
       "tnSysSslCertSignatureAlgorithm": tnSysSslCertSignatureAlgorithm,
       "tnSysSslCertValidity": tnSysSslCertValidity,
       "tnSysSslCsrUploadStatus": tnSysSslCsrUploadStatus,
       "tnSysSslCertDownloadStatus": tnSysSslCertDownloadStatus,
       "tnSysSslCertInstallStatus": tnSysSslCertInstallStatus,
       "tnSysSslCsrGenerationStatus": tnSysSslCsrGenerationStatus,
       "tnSysKey": tnSysKey,
       "tnSshKeyAttributeTotal": tnSshKeyAttributeTotal,
       "tnSshKeyTable": tnSshKeyTable,
       "tnSshKeyEntry": tnSshKeyEntry,
       "tnSshKeyTypeIndex": tnSshKeyTypeIndex,
       "tnSshPublicKey": tnSshPublicKey,
       "tnSysTransferLog": tnSysTransferLog,
       "tnSysTransferLogCommand": tnSysTransferLogCommand,
       "tnSysTransferLogRemoteHostIp": tnSysTransferLogRemoteHostIp,
       "tnSysTransferLogRemotePath": tnSysTransferLogRemotePath,
       "tnSysTransferLogType": tnSysTransferLogType,
       "tnSysTransferLogStatus": tnSysTransferLogStatus,
       "tnSysTransferLogLastLogFilename": tnSysTransferLogLastLogFilename,
       "tnSysTransferLogLastCommand": tnSysTransferLogLastCommand,
       "tnSysTransferLogLastFileTimeStamp": tnSysTransferLogLastFileTimeStamp,
       "tnSysTransferLogProtocol": tnSysTransferLogProtocol,
       "tnSysTransferLogUserId": tnSysTransferLogUserId,
       "tnSysTransferLogPassword": tnSysTransferLogPassword,
       "tnSysTransferLogWindowStart": tnSysTransferLogWindowStart,
       "tnSysTransferLogWindowStop": tnSysTransferLogWindowStop,
       "tnSysTransferLogRemoteHostInetAddressType": tnSysTransferLogRemoteHostInetAddressType,
       "tnSysTransferLogRemoteHostInetAddress": tnSysTransferLogRemoteHostInetAddress,
       "tnSysAccessControlList": tnSysAccessControlList,
       "tnSysIpAclSysDefault": tnSysIpAclSysDefault,
       "tnSysIpAclRxAction": tnSysIpAclRxAction,
       "tnSysIpAclTxAction": tnSysIpAclTxAction,
       "tnSysIpAclSnmpCfgEnable": tnSysIpAclSnmpCfgEnable,
       "tnSysIpAclCfgRestoreToDefault": tnSysIpAclCfgRestoreToDefault,
       "tnSysIpAclPatternAttributeTotal": tnSysIpAclPatternAttributeTotal,
       "tnSysIpAclPatternTable": tnSysIpAclPatternTable,
       "tnSysIpAclPatternEntry": tnSysIpAclPatternEntry,
       "tnSysIpAclPatternID": tnSysIpAclPatternID,
       "tnSysIpAclPatternAction": tnSysIpAclPatternAction,
       "tnSysIpAclPatternICMPERROR": tnSysIpAclPatternICMPERROR,
       "tnSysIpAclPatternSrcAddr": tnSysIpAclPatternSrcAddr,
       "tnSysIpAclPatternSrcPrefix": tnSysIpAclPatternSrcPrefix,
       "tnSysIpAclPatternDestAddr": tnSysIpAclPatternDestAddr,
       "tnSysIpAclPatternDestPrefix": tnSysIpAclPatternDestPrefix,
       "tnSysIpAclPatternDestPort": tnSysIpAclPatternDestPort,
       "tnSysIpAclPatternIpProtocol": tnSysIpAclPatternIpProtocol,
       "tnSysIpAclPatternIpFragment": tnSysIpAclPatternIpFragment,
       "tnSysIpAclPatternIcmpType": tnSysIpAclPatternIcmpType,
       "tnSysIpAclPatternIcmpCode": tnSysIpAclPatternIcmpCode,
       "tnSysIpAclPatternTcpEstablish": tnSysIpAclPatternTcpEstablish,
       "tnSysIpAclPatternRowStatus": tnSysIpAclPatternRowStatus,
       "tnSysIpAclPatternSrcPort": tnSysIpAclPatternSrcPort,
       "tnSysIpAclPatternSystemDefault": tnSysIpAclPatternSystemDefault,
       "tnSysIpAclFilterAttributeTotal": tnSysIpAclFilterAttributeTotal,
       "tnSysIpAclFilterTable": tnSysIpAclFilterTable,
       "tnSysIpAclFilterEntry": tnSysIpAclFilterEntry,
       "tnSysIpAclFilterID": tnSysIpAclFilterID,
       "tnSysIpAclFilterPatternIndex": tnSysIpAclFilterPatternIndex,
       "tnSysIpAclFilterPatternID": tnSysIpAclFilterPatternID,
       "tnSysIpAclFilterStatCount": tnSysIpAclFilterStatCount,
       "tnSysIpAclFilterRowStatus": tnSysIpAclFilterRowStatus,
       "tnSysIpAclFilterSystemDefault": tnSysIpAclFilterSystemDefault,
       "tnSysIpAclInterfaceAttributeTotal": tnSysIpAclInterfaceAttributeTotal,
       "tnSysIpAclInterfaceTable": tnSysIpAclInterfaceTable,
       "tnSysIpAclInterfaceEntry": tnSysIpAclInterfaceEntry,
       "tnSysIpAclInterfaceFilterDir": tnSysIpAclInterfaceFilterDir,
       "tnSysIpAclInterfaceFilterID": tnSysIpAclInterfaceFilterID,
       "tnSysIpAclInterfaceFilterEnable": tnSysIpAclInterfaceFilterEnable,
       "tnSysIpAclInterfaceFilterRowStatus": tnSysIpAclInterfaceFilterRowStatus,
       "tnSysIpAclInterfaceSystemDefault": tnSysIpAclInterfaceSystemDefault,
       "tnSysIpAclNetIfFilterAttributeTotal": tnSysIpAclNetIfFilterAttributeTotal,
       "tnSysIpAclNetIfFilterTable": tnSysIpAclNetIfFilterTable,
       "tnSysIpAclNetIfFilterEntry": tnSysIpAclNetIfFilterEntry,
       "tnSysIpAclNetIfFilterDir": tnSysIpAclNetIfFilterDir,
       "tnSysIpAclNetIfFilterRowStatus": tnSysIpAclNetIfFilterRowStatus,
       "tnSysIpAclNetIfFilterID": tnSysIpAclNetIfFilterID,
       "tnSysIpAclNetIfFilterEnable": tnSysIpAclNetIfFilterEnable,
       "tnSysIpAclNetIfFilterSystemDefault": tnSysIpAclNetIfFilterSystemDefault,
       "tnSysIpAclIpv6PatternAttributeTotal": tnSysIpAclIpv6PatternAttributeTotal,
       "tnSysIpAclIpv6PatternTable": tnSysIpAclIpv6PatternTable,
       "tnSysIpAclIpv6PatternEntry": tnSysIpAclIpv6PatternEntry,
       "tnSysIpAclIpv6PatternID": tnSysIpAclIpv6PatternID,
       "tnSysIpAclIpv6PatternAction": tnSysIpAclIpv6PatternAction,
       "tnSysIpAclIpv6PatternICMPV6ERROR": tnSysIpAclIpv6PatternICMPV6ERROR,
       "tnSysIpAclIpv6PatternSrcAddr": tnSysIpAclIpv6PatternSrcAddr,
       "tnSysIpAclIpv6PatternSrcPrefixLen": tnSysIpAclIpv6PatternSrcPrefixLen,
       "tnSysIpAclIpv6PatternDestAddr": tnSysIpAclIpv6PatternDestAddr,
       "tnSysIpAclIpv6PatternDestPrefixLen": tnSysIpAclIpv6PatternDestPrefixLen,
       "tnSysIpAclIpv6PatternIpProtocol": tnSysIpAclIpv6PatternIpProtocol,
       "tnSysIpAclIpv6PatternIcmpType": tnSysIpAclIpv6PatternIcmpType,
       "tnSysIpAclIpv6PatternIcmpCode": tnSysIpAclIpv6PatternIcmpCode,
       "tnSysIpAclIpv6PatternSrcPort": tnSysIpAclIpv6PatternSrcPort,
       "tnSysIpAclIpv6PatternDestPort": tnSysIpAclIpv6PatternDestPort,
       "tnSysIpAclIpv6PatternIpFragment": tnSysIpAclIpv6PatternIpFragment,
       "tnSysIpAclIpv6PatternTcpEstablish": tnSysIpAclIpv6PatternTcpEstablish,
       "tnSysIpAclIpv6PatternSystemDefault": tnSysIpAclIpv6PatternSystemDefault,
       "tnSysIpAclIpv6PatternRowStatus": tnSysIpAclIpv6PatternRowStatus,
       "tnSysIpAclIpv6FilterAttributeTotal": tnSysIpAclIpv6FilterAttributeTotal,
       "tnSysIpAclIpv6FilterTable": tnSysIpAclIpv6FilterTable,
       "tnSysIpAclIpv6FilterEntry": tnSysIpAclIpv6FilterEntry,
       "tnSysIpAclIpv6FilterID": tnSysIpAclIpv6FilterID,
       "tnSysIpAclIpv6FilterPatternIndex": tnSysIpAclIpv6FilterPatternIndex,
       "tnSysIpAclIpv6FilterPatternID": tnSysIpAclIpv6FilterPatternID,
       "tnSysIpAclIpv6FilterStatCount": tnSysIpAclIpv6FilterStatCount,
       "tnSysIpAclIpv6FilterRowStatus": tnSysIpAclIpv6FilterRowStatus,
       "tnSysIpAclIpv6FilterSystemDefault": tnSysIpAclIpv6FilterSystemDefault,
       "tnSysIpAclIpv6InterfaceAttributeTotal": tnSysIpAclIpv6InterfaceAttributeTotal,
       "tnSysIpAclIpv6InterfaceTable": tnSysIpAclIpv6InterfaceTable,
       "tnSysIpAclIpv6InterfaceEntry": tnSysIpAclIpv6InterfaceEntry,
       "tnSysIpAclIpv6InterfaceFilterDir": tnSysIpAclIpv6InterfaceFilterDir,
       "tnSysIpAclIpv6InterfaceFilterID": tnSysIpAclIpv6InterfaceFilterID,
       "tnSysIpAclIpv6InterfaceFilterEnable": tnSysIpAclIpv6InterfaceFilterEnable,
       "tnSysIpAclIpv6InterfaceFilterRowStatus": tnSysIpAclIpv6InterfaceFilterRowStatus,
       "tnSysIpAclIpv6InterfaceSystemDefault": tnSysIpAclIpv6InterfaceSystemDefault,
       "tnSysIpv6AclNetIfFilterAttributeTotal": tnSysIpv6AclNetIfFilterAttributeTotal,
       "tnSysIpv6AclNetIfFilterTable": tnSysIpv6AclNetIfFilterTable,
       "tnSysIpv6AclNetIfFilterEntry": tnSysIpv6AclNetIfFilterEntry,
       "tnSysIpv6AclNetIfFilterDir": tnSysIpv6AclNetIfFilterDir,
       "tnSysIpv6AclNetIfFilterRowStatus": tnSysIpv6AclNetIfFilterRowStatus,
       "tnSysIpv6AclNetIfFilterID": tnSysIpv6AclNetIfFilterID,
       "tnSysIpv6AclNetIfFilterEnable": tnSysIpv6AclNetIfFilterEnable,
       "tnSysIpv6AclNetIfFilterSystemDefault": tnSysIpv6AclNetIfFilterSystemDefault,
       "tnSysNtpServerIdStats": tnSysNtpServerIdStats,
       "tnSysNtpServerIdStatsTable": tnSysNtpServerIdStatsTable,
       "tnSysNtpServerIdStatsEntry": tnSysNtpServerIdStatsEntry,
       "tnSysNtpServerIdStatsIndex": tnSysNtpServerIdStatsIndex,
       "tnSysNtpServerIdStatsSelect": tnSysNtpServerIdStatsSelect,
       "tnSysNtpServerIdStatsIp": tnSysNtpServerIdStatsIp,
       "tnSysNtpServerIdStatsRefId": tnSysNtpServerIdStatsRefId,
       "tnSysNtpServerIdStatsStrtm": tnSysNtpServerIdStatsStrtm,
       "tnSysNtpServerIdStatsClockType": tnSysNtpServerIdStatsClockType,
       "tnSysNtpServerIdStatsPoll": tnSysNtpServerIdStatsPoll,
       "tnSysNtpServerIdStatsReach": tnSysNtpServerIdStatsReach,
       "tnSysNtpServerIdStatsDelay": tnSysNtpServerIdStatsDelay,
       "tnSysNtpServerIdStatsOffset": tnSysNtpServerIdStatsOffset,
       "tnSysNtpServerIdStatsJitter": tnSysNtpServerIdStatsJitter,
       "tnSysNtpServerIdStatsKeyIndex": tnSysNtpServerIdStatsKeyIndex,
       "tnSysFtpServer": tnSysFtpServer,
       "tnSysFtpServerEnabled": tnSysFtpServerEnabled,
       "tnSysFtpServerUserId": tnSysFtpServerUserId,
       "tnSysFtpServerPassword": tnSysFtpServerPassword,
       "tnSysNtpServerAuthentication": tnSysNtpServerAuthentication,
       "tnSysNtpServerAuthenticationAttributeTotal": tnSysNtpServerAuthenticationAttributeTotal,
       "tnSysNtpServerAuthenticationTable": tnSysNtpServerAuthenticationTable,
       "tnSysNtpServerAuthenticationEntry": tnSysNtpServerAuthenticationEntry,
       "tnSysNtpServerAuthenticationKeyIndex": tnSysNtpServerAuthenticationKeyIndex,
       "tnSysNtpServerAuthenticationRowStatus": tnSysNtpServerAuthenticationRowStatus,
       "tnSysNtpServerAuthenticationKeyType": tnSysNtpServerAuthenticationKeyType,
       "tnSysNtpServerAuthenticationKey": tnSysNtpServerAuthenticationKey,
       "tnNeDiscovery": tnNeDiscovery,
       "tnNeDiscoveryAttributeTotal": tnNeDiscoveryAttributeTotal,
       "tnNeDiscoveryTable": tnNeDiscoveryTable,
       "tnNeDiscoveryEntry": tnNeDiscoveryEntry,
       "tnNeDiscoveryIndex": tnNeDiscoveryIndex,
       "tnNeDiscoveryFilename": tnNeDiscoveryFilename,
       "tnNeDiscoveryControl": tnNeDiscoveryControl,
       "tnNeDiscoveryStatus": tnNeDiscoveryStatus,
       "tnNeDiscoveryErrorCode": tnNeDiscoveryErrorCode,
       "tnNeDiscoveryServerIp": tnNeDiscoveryServerIp,
       "tnNeDiscoveryServerProtocol": tnNeDiscoveryServerProtocol,
       "tnNeDiscoveryServerUserId": tnNeDiscoveryServerUserId,
       "tnNeDiscoveryServerPassword": tnNeDiscoveryServerPassword,
       "tnNeDiscoveryServerTimeOut": tnNeDiscoveryServerTimeOut,
       "tnNeDiscoveryRowStatus": tnNeDiscoveryRowStatus,
       "tnNeDiscoveryServerInetAddressType": tnNeDiscoveryServerInetAddressType,
       "tnNeDiscoveryServerInetAddress": tnNeDiscoveryServerInetAddress,
       "tnSysOtdrScan": tnSysOtdrScan,
       "tnSysOtdrScanSystemProfile": tnSysOtdrScanSystemProfile,
       "tnSysOtdrScanSystemProfileAttributeTotal": tnSysOtdrScanSystemProfileAttributeTotal,
       "tnSysOtdrScanSystemProfileTable": tnSysOtdrScanSystemProfileTable,
       "tnSysOtdrScanSystemProfileEntry": tnSysOtdrScanSystemProfileEntry,
       "tnSysOtdrScanSystemProfileId": tnSysOtdrScanSystemProfileId,
       "tnSysOtdrScanSystemProfileDescription": tnSysOtdrScanSystemProfileDescription,
       "tnSysOtdrScanSystemProfileWaveLength": tnSysOtdrScanSystemProfileWaveLength,
       "tnSysOtdrScanSystemProfilePulseLength": tnSysOtdrScanSystemProfilePulseLength,
       "tnSysOtdrScanSystemProfileRange": tnSysOtdrScanSystemProfileRange,
       "tnSysOtdrScanSystemProfileResolution": tnSysOtdrScanSystemProfileResolution,
       "tnSysOtdrScanSystemProfileAvgTime": tnSysOtdrScanSystemProfileAvgTime,
       "tnSysOtdrScanTransfer": tnSysOtdrScanTransfer,
       "tnSysOtdrScanTransferRemoteHostIp": tnSysOtdrScanTransferRemoteHostIp,
       "tnSysOtdrScanTransferCommand": tnSysOtdrScanTransferCommand,
       "tnSysOtdrScanTransferRemotePath": tnSysOtdrScanTransferRemotePath,
       "tnSysOtdrScanTransferStatus": tnSysOtdrScanTransferStatus,
       "tnSysOtdrScanTransferFilename": tnSysOtdrScanTransferFilename,
       "tnSysOtdrScanTransferProtocol": tnSysOtdrScanTransferProtocol,
       "tnSysOtdrScanTransferUserId": tnSysOtdrScanTransferUserId,
       "tnSysOtdrScanTransferPassword": tnSysOtdrScanTransferPassword,
       "tnSysOtdrScanTransferInetAddressType": tnSysOtdrScanTransferInetAddressType,
       "tnSysOtdrScanTransferInetAddress": tnSysOtdrScanTransferInetAddress,
       "tnClusterObjs": tnClusterObjs,
       "tnClusterTable": tnClusterTable,
       "tnClusterEntry": tnClusterEntry,
       "tnClusterRowStatus": tnClusterRowStatus,
       "tnClusterFarEndNode": tnClusterFarEndNode,
       "tnClusterIpAddress": tnClusterIpAddress,
       "tnClusterlinkStatus": tnClusterlinkStatus,
       "tnClusterInetAddressType": tnClusterInetAddressType,
       "tnClusterInetAddress": tnClusterInetAddress,
       "tnSysPmFetchBulk": tnSysPmFetchBulk,
       "tnSysPmFetchBulkStart": tnSysPmFetchBulkStart,
       "tnSysPmFetchBulkStatus": tnSysPmFetchBulkStatus,
       "tnSysPmFetchBulkRemoteHostIp": tnSysPmFetchBulkRemoteHostIp,
       "tnSysPmFetchBulkUserId": tnSysPmFetchBulkUserId,
       "tnSysPmFetchBulkPassword": tnSysPmFetchBulkPassword,
       "tnSysPmFetchBulkRemotePath": tnSysPmFetchBulkRemotePath,
       "tnSysPmFetchBulkStatsInterval": tnSysPmFetchBulkStatsInterval,
       "tnSysPmFetchBulkBinnedStatsBin": tnSysPmFetchBulkBinnedStatsBin,
       "tnSysPmFetchBulkShelfNum": tnSysPmFetchBulkShelfNum,
       "tnSysDebugTransfer": tnSysDebugTransfer,
       "tnSysDebugTransferRemoteHostIp": tnSysDebugTransferRemoteHostIp,
       "tnSysDebugTransferCommand": tnSysDebugTransferCommand,
       "tnSysDebugTransferRemotePath": tnSysDebugTransferRemotePath,
       "tnSysDebugTransferStatus": tnSysDebugTransferStatus,
       "tnSysDebugTransferProtocol": tnSysDebugTransferProtocol,
       "tnSysDebugTransferUserId": tnSysDebugTransferUserId,
       "tnSysDebugTransferPassword": tnSysDebugTransferPassword,
       "tnSysDebugTransferFilename": tnSysDebugTransferFilename,
       "tnSysDebugTransferRecentSuccessFile": tnSysDebugTransferRecentSuccessFile,
       "tnSysDebugTransferTimestamp": tnSysDebugTransferTimestamp,
       "tnSysDebugTransferShelfNum": tnSysDebugTransferShelfNum,
       "tnSysDebugTransferPercentCompleted": tnSysDebugTransferPercentCompleted,
       "tnSysDebugTransferRemoteInetAddress": tnSysDebugTransferRemoteInetAddress,
       "tnSysDebugTransferRemoteInetAddressType": tnSysDebugTransferRemoteInetAddressType,
       "tnSysLicenseInv": tnSysLicenseInv,
       "tnSysLicenseInvPathIp": tnSysLicenseInvPathIp,
       "tnSysLicenseInvFile": tnSysLicenseInvFile,
       "tnSysLicenseInvProtocol": tnSysLicenseInvProtocol,
       "tnSysLicenseInvUserId": tnSysLicenseInvUserId,
       "tnSysLicenseInvPassword": tnSysLicenseInvPassword,
       "tnSysLicenseInvFileUploadOper": tnSysLicenseInvFileUploadOper,
       "tnSysLicenseInvPathInetAddressType": tnSysLicenseInvPathInetAddressType,
       "tnSysLicenseInvPathInetAddress": tnSysLicenseInvPathInetAddress,
       "tnSysLicenseInvLastOperPercentCompleted": tnSysLicenseInvLastOperPercentCompleted,
       "tnSysLicenseInvLastUploadFileName": tnSysLicenseInvLastUploadFileName,
       "tnSysLicenseInvFileLastUploadStatus": tnSysLicenseInvFileLastUploadStatus,
       "tnSysLicenseInvFileLastUploadTimeStamp": tnSysLicenseInvFileLastUploadTimeStamp,
       "tnSysDataDump": tnSysDataDump,
       "tnSysDataDumpInfo": tnSysDataDumpInfo,
       "tnSysLinux": tnSysLinux,
       "tnSysLinuxRootUserId": tnSysLinuxRootUserId,
       "tnSysLinuxRootUserPassword": tnSysLinuxRootUserPassword,
       "tnSysLinuxApplUserId": tnSysLinuxApplUserId,
       "tnSysLinuxApplUserPassword": tnSysLinuxApplUserPassword,
       "tnSysIpAclIpv6SysDefault": tnSysIpAclIpv6SysDefault,
       "tnSysIpAclIpv6RxAction": tnSysIpAclIpv6RxAction,
       "tnSysIpAclIpv6TxAction": tnSysIpAclIpv6TxAction,
       "tnSysIpAclIpv6SnmpCfgEnable": tnSysIpAclIpv6SnmpCfgEnable,
       "tnSysIpAclIpv6CfgRestoreToDefault": tnSysIpAclIpv6CfgRestoreToDefault}
)
