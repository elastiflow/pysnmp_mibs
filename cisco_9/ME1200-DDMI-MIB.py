# SNMP MIB module (ME1200-DDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-DDMI-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200InterfaceIndex) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200DdmiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121)
)
if mibBuilder.loadTexts:
    me1200DdmiMib.setRevisions(
        ("2016-05-23 00:00",
         "2014-06-30 00:00",
         "2014-05-16 00:00",
         "2014-05-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200DdmiSfpTransceiver(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("notSupported", 1),
          ("sfp100FX", 2),
          ("sfp1000BaseT", 7),
          ("sfp1000BaseCx", 8),
          ("sfp1000BaseSx", 9),
          ("sfp1000BaseLx", 10),
          ("sfp1000BaseX", 11),
          ("sfp2G5", 12),
          ("sfp5G", 13),
          ("sfp10G", 14))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200DdmiMibObjects_ObjectIdentity = ObjectIdentity
me1200DdmiMibObjects = _Me1200DdmiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1)
)
_Me1200DdmiConfig_ObjectIdentity = ObjectIdentity
me1200DdmiConfig = _Me1200DdmiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 2)
)
_Me1200DdmiConfigGlobals_ObjectIdentity = ObjectIdentity
me1200DdmiConfigGlobals = _Me1200DdmiConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 2, 1)
)
_Me1200DdmiConfigGlobalsMode_Type = TruthValue
_Me1200DdmiConfigGlobalsMode_Object = MibScalar
me1200DdmiConfigGlobalsMode = _Me1200DdmiConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 2, 1, 1),
    _Me1200DdmiConfigGlobalsMode_Type()
)
me1200DdmiConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DdmiConfigGlobalsMode.setStatus("current")
_Me1200DdmiStatus_ObjectIdentity = ObjectIdentity
me1200DdmiStatus = _Me1200DdmiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3)
)
_Me1200DdmiStatusInterfaceTable_Object = MibTable
me1200DdmiStatusInterfaceTable = _Me1200DdmiStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceTable.setStatus("current")
_Me1200DdmiStatusInterfaceEntry_Object = MibTableRow
me1200DdmiStatusInterfaceEntry = _Me1200DdmiStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1)
)
me1200DdmiStatusInterfaceEntry.setIndexNames(
    (0, "ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceEntry.setStatus("current")
_Me1200DdmiStatusInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200DdmiStatusInterfaceIfIndex_Object = MibTableColumn
me1200DdmiStatusInterfaceIfIndex = _Me1200DdmiStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1),
    _Me1200DdmiStatusInterfaceIfIndex_Type()
)
me1200DdmiStatusInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceIfIndex.setStatus("current")
_Me1200DdmiStatusInterfaceA0Supported_Type = TruthValue
_Me1200DdmiStatusInterfaceA0Supported_Object = MibTableColumn
me1200DdmiStatusInterfaceA0Supported = _Me1200DdmiStatusInterfaceA0Supported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 2),
    _Me1200DdmiStatusInterfaceA0Supported_Type()
)
me1200DdmiStatusInterfaceA0Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0Supported.setStatus("current")
_Me1200DdmiStatusInterfaceA0SfpDetected_Type = TruthValue
_Me1200DdmiStatusInterfaceA0SfpDetected_Object = MibTableColumn
me1200DdmiStatusInterfaceA0SfpDetected = _Me1200DdmiStatusInterfaceA0SfpDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 3),
    _Me1200DdmiStatusInterfaceA0SfpDetected_Type()
)
me1200DdmiStatusInterfaceA0SfpDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0SfpDetected.setStatus("current")


class _Me1200DdmiStatusInterfaceA0Vendor_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA0Vendor based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA0Vendor_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA0Vendor_Object = MibTableColumn
me1200DdmiStatusInterfaceA0Vendor = _Me1200DdmiStatusInterfaceA0Vendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 4),
    _Me1200DdmiStatusInterfaceA0Vendor_Type()
)
me1200DdmiStatusInterfaceA0Vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0Vendor.setStatus("current")


class _Me1200DdmiStatusInterfaceA0PartNumber_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA0PartNumber based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA0PartNumber_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA0PartNumber_Object = MibTableColumn
me1200DdmiStatusInterfaceA0PartNumber = _Me1200DdmiStatusInterfaceA0PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 5),
    _Me1200DdmiStatusInterfaceA0PartNumber_Type()
)
me1200DdmiStatusInterfaceA0PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0PartNumber.setStatus("current")


class _Me1200DdmiStatusInterfaceA0SerialNumber_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA0SerialNumber based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA0SerialNumber_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA0SerialNumber_Object = MibTableColumn
me1200DdmiStatusInterfaceA0SerialNumber = _Me1200DdmiStatusInterfaceA0SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 6),
    _Me1200DdmiStatusInterfaceA0SerialNumber_Type()
)
me1200DdmiStatusInterfaceA0SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0SerialNumber.setStatus("current")


class _Me1200DdmiStatusInterfaceA0Revision_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA0Revision based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA0Revision_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA0Revision_Object = MibTableColumn
me1200DdmiStatusInterfaceA0Revision = _Me1200DdmiStatusInterfaceA0Revision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 7),
    _Me1200DdmiStatusInterfaceA0Revision_Type()
)
me1200DdmiStatusInterfaceA0Revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0Revision.setStatus("current")


class _Me1200DdmiStatusInterfaceA0DateCode_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA0DateCode based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA0DateCode_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA0DateCode_Object = MibTableColumn
me1200DdmiStatusInterfaceA0DateCode = _Me1200DdmiStatusInterfaceA0DateCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 8),
    _Me1200DdmiStatusInterfaceA0DateCode_Type()
)
me1200DdmiStatusInterfaceA0DateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0DateCode.setStatus("current")
_Me1200DdmiStatusInterfaceA0SfpType_Type = ME1200DdmiSfpTransceiver
_Me1200DdmiStatusInterfaceA0SfpType_Object = MibTableColumn
me1200DdmiStatusInterfaceA0SfpType = _Me1200DdmiStatusInterfaceA0SfpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 9),
    _Me1200DdmiStatusInterfaceA0SfpType_Type()
)
me1200DdmiStatusInterfaceA0SfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA0SfpType.setStatus("current")
_Me1200DdmiStatusInterfaceA2Supported_Type = TruthValue
_Me1200DdmiStatusInterfaceA2Supported_Object = MibTableColumn
me1200DdmiStatusInterfaceA2Supported = _Me1200DdmiStatusInterfaceA2Supported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1002),
    _Me1200DdmiStatusInterfaceA2Supported_Type()
)
me1200DdmiStatusInterfaceA2Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2Supported.setStatus("current")


class _Me1200DdmiStatusInterfaceA2CurrentTemperature_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2CurrentTemperature based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2CurrentTemperature_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2CurrentTemperature_Object = MibTableColumn
me1200DdmiStatusInterfaceA2CurrentTemperature = _Me1200DdmiStatusInterfaceA2CurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1003),
    _Me1200DdmiStatusInterfaceA2CurrentTemperature_Type()
)
me1200DdmiStatusInterfaceA2CurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2CurrentTemperature.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold = _Me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1004),
    _Me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold = _Me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1005),
    _Me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold = _Me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1006),
    _Me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold = _Me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1007),
    _Me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2CurrentVoltage_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2CurrentVoltage based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2CurrentVoltage_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2CurrentVoltage_Object = MibTableColumn
me1200DdmiStatusInterfaceA2CurrentVoltage = _Me1200DdmiStatusInterfaceA2CurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1008),
    _Me1200DdmiStatusInterfaceA2CurrentVoltage_Type()
)
me1200DdmiStatusInterfaceA2CurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2CurrentVoltage.setStatus("current")


class _Me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold = _Me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1009),
    _Me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold = _Me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1010),
    _Me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold = _Me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1011),
    _Me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold = _Me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1012),
    _Me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2CurrentTxBias_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2CurrentTxBias based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2CurrentTxBias_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2CurrentTxBias_Object = MibTableColumn
me1200DdmiStatusInterfaceA2CurrentTxBias = _Me1200DdmiStatusInterfaceA2CurrentTxBias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1013),
    _Me1200DdmiStatusInterfaceA2CurrentTxBias_Type()
)
me1200DdmiStatusInterfaceA2CurrentTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2CurrentTxBias.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold = _Me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1014),
    _Me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold = _Me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1015),
    _Me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold = _Me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1016),
    _Me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold = _Me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1017),
    _Me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2CurrentTxPower_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2CurrentTxPower based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2CurrentTxPower_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2CurrentTxPower_Object = MibTableColumn
me1200DdmiStatusInterfaceA2CurrentTxPower = _Me1200DdmiStatusInterfaceA2CurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1018),
    _Me1200DdmiStatusInterfaceA2CurrentTxPower_Type()
)
me1200DdmiStatusInterfaceA2CurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2CurrentTxPower.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold = _Me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1019),
    _Me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold = _Me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1020),
    _Me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold = _Me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1021),
    _Me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold = _Me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1022),
    _Me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2CurrentRxPower_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2CurrentRxPower based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2CurrentRxPower_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2CurrentRxPower_Object = MibTableColumn
me1200DdmiStatusInterfaceA2CurrentRxPower = _Me1200DdmiStatusInterfaceA2CurrentRxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1023),
    _Me1200DdmiStatusInterfaceA2CurrentRxPower_Type()
)
me1200DdmiStatusInterfaceA2CurrentRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2CurrentRxPower.setStatus("current")


class _Me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold = _Me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1024),
    _Me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold = _Me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1025),
    _Me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold_Type()
)
me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold = _Me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1026),
    _Me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold.setStatus("current")


class _Me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold_Type(ME1200DisplayString):
    """Custom type me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold_Type.__name__ = "ME1200DisplayString"
_Me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold_Object = MibTableColumn
me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold = _Me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 3, 2, 1, 1027),
    _Me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold_Type()
)
me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold.setStatus("current")
_Me1200DdmiNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200DdmiNotificationPrefix = _Me1200DdmiNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 4)
)
_Me1200DdmitNotification_ObjectIdentity = ObjectIdentity
me1200DdmitNotification = _Me1200DdmitNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 4, 0)
)
_Me1200DdmiMibConformance_ObjectIdentity = ObjectIdentity
me1200DdmiMibConformance = _Me1200DdmiMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2)
)
_Me1200DdmiMibCompliances_ObjectIdentity = ObjectIdentity
me1200DdmiMibCompliances = _Me1200DdmiMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2, 1)
)
_Me1200DdmiMibGroups_ObjectIdentity = ObjectIdentity
me1200DdmiMibGroups = _Me1200DdmiMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2, 2)
)

# Managed Objects groups

me1200DdmiConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2, 2, 1)
)
me1200DdmiConfigGlobalsInfoGroup.setObjects(
    ("ME1200-DDMI-MIB", "me1200DdmiConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    me1200DdmiConfigGlobalsInfoGroup.setStatus("current")

me1200DdmiStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2, 2, 2)
)
me1200DdmiStatusInterfaceTableInfoGroup.setObjects(
      *(("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0Supported"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0SfpDetected"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0Vendor"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0PartNumber"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0SerialNumber"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0Revision"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0DateCode"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0SfpType"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2Supported"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2CurrentTemperature"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2CurrentVoltage"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2CurrentTxBias"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2CurrentTxPower"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2CurrentRxPower"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold"))
)
if mibBuilder.loadTexts:
    me1200DdmiStatusInterfaceTableInfoGroup.setStatus("current")


# Notification objects

me1200DdmiNotificationSFPErrorType = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 1, 4, 0, 1)
)
me1200DdmiNotificationSFPErrorType.setObjects(
    ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceA0SfpType")
)
if mibBuilder.loadTexts:
    me1200DdmiNotificationSFPErrorType.setStatus(
        "current"
    )


# Notifications groups

me1200DdmiNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2, 2, 3)
)
me1200DdmiNotificationInfoGroup.setObjects(
    ("ME1200-DDMI-MIB", "me1200DdmiNotificationSFPErrorType")
)
if mibBuilder.loadTexts:
    me1200DdmiNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200DdmiMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 121, 2, 1, 1)
)
me1200DdmiMibCompliance.setObjects(
      *(("ME1200-DDMI-MIB", "me1200DdmiConfigGlobalsInfoGroup"),
        ("ME1200-DDMI-MIB", "me1200DdmiStatusInterfaceTableInfoGroup"),
        ("ME1200-DDMI-MIB", "me1200DdmiNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200DdmiMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-DDMI-MIB",
    **{"ME1200DdmiSfpTransceiver": ME1200DdmiSfpTransceiver,
       "me1200DdmiMib": me1200DdmiMib,
       "me1200DdmiMibObjects": me1200DdmiMibObjects,
       "me1200DdmiConfig": me1200DdmiConfig,
       "me1200DdmiConfigGlobals": me1200DdmiConfigGlobals,
       "me1200DdmiConfigGlobalsMode": me1200DdmiConfigGlobalsMode,
       "me1200DdmiStatus": me1200DdmiStatus,
       "me1200DdmiStatusInterfaceTable": me1200DdmiStatusInterfaceTable,
       "me1200DdmiStatusInterfaceEntry": me1200DdmiStatusInterfaceEntry,
       "me1200DdmiStatusInterfaceIfIndex": me1200DdmiStatusInterfaceIfIndex,
       "me1200DdmiStatusInterfaceA0Supported": me1200DdmiStatusInterfaceA0Supported,
       "me1200DdmiStatusInterfaceA0SfpDetected": me1200DdmiStatusInterfaceA0SfpDetected,
       "me1200DdmiStatusInterfaceA0Vendor": me1200DdmiStatusInterfaceA0Vendor,
       "me1200DdmiStatusInterfaceA0PartNumber": me1200DdmiStatusInterfaceA0PartNumber,
       "me1200DdmiStatusInterfaceA0SerialNumber": me1200DdmiStatusInterfaceA0SerialNumber,
       "me1200DdmiStatusInterfaceA0Revision": me1200DdmiStatusInterfaceA0Revision,
       "me1200DdmiStatusInterfaceA0DateCode": me1200DdmiStatusInterfaceA0DateCode,
       "me1200DdmiStatusInterfaceA0SfpType": me1200DdmiStatusInterfaceA0SfpType,
       "me1200DdmiStatusInterfaceA2Supported": me1200DdmiStatusInterfaceA2Supported,
       "me1200DdmiStatusInterfaceA2CurrentTemperature": me1200DdmiStatusInterfaceA2CurrentTemperature,
       "me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold": me1200DdmiStatusInterfaceA2TemperatureHighAlarmThreshold,
       "me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold": me1200DdmiStatusInterfaceA2TemperatureLowAlarmThreshold,
       "me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold": me1200DdmiStatusInterfaceA2TemperatureHighWarnThreshold,
       "me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold": me1200DdmiStatusInterfaceA2TemperatureLowWarnThreshold,
       "me1200DdmiStatusInterfaceA2CurrentVoltage": me1200DdmiStatusInterfaceA2CurrentVoltage,
       "me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold": me1200DdmiStatusInterfaceA2VoltageHighAlarmThreshold,
       "me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold": me1200DdmiStatusInterfaceA2VoltageLowAlarmThreshold,
       "me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold": me1200DdmiStatusInterfaceA2VoltageHighWarnThreshold,
       "me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold": me1200DdmiStatusInterfaceA2VoltageLowWarnThreshold,
       "me1200DdmiStatusInterfaceA2CurrentTxBias": me1200DdmiStatusInterfaceA2CurrentTxBias,
       "me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold": me1200DdmiStatusInterfaceA2TxBiasHighAlarmThreshold,
       "me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold": me1200DdmiStatusInterfaceA2TxBiasLowAlarmThreshold,
       "me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold": me1200DdmiStatusInterfaceA2TxBiasHighWarnThreshold,
       "me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold": me1200DdmiStatusInterfaceA2TxBiasLowWarnThreshold,
       "me1200DdmiStatusInterfaceA2CurrentTxPower": me1200DdmiStatusInterfaceA2CurrentTxPower,
       "me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold": me1200DdmiStatusInterfaceA2TxPowerHighAlarmThreshold,
       "me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold": me1200DdmiStatusInterfaceA2TxPowerLowAlarmThreshold,
       "me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold": me1200DdmiStatusInterfaceA2TxPowerHighWarnThreshold,
       "me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold": me1200DdmiStatusInterfaceA2TxPowerLowWarnThreshold,
       "me1200DdmiStatusInterfaceA2CurrentRxPower": me1200DdmiStatusInterfaceA2CurrentRxPower,
       "me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold": me1200DdmiStatusInterfaceA2RxPowerHighAlarmThreshold,
       "me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold": me1200DdmiStatusInterfaceA2RxPowerLowAlarmThreshold,
       "me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold": me1200DdmiStatusInterfaceA2RxPowerHighWarnThreshold,
       "me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold": me1200DdmiStatusInterfaceA2RxPowerLowWarnThreshold,
       "me1200DdmiNotificationPrefix": me1200DdmiNotificationPrefix,
       "me1200DdmitNotification": me1200DdmitNotification,
       "me1200DdmiNotificationSFPErrorType": me1200DdmiNotificationSFPErrorType,
       "me1200DdmiMibConformance": me1200DdmiMibConformance,
       "me1200DdmiMibCompliances": me1200DdmiMibCompliances,
       "me1200DdmiMibCompliance": me1200DdmiMibCompliance,
       "me1200DdmiMibGroups": me1200DdmiMibGroups,
       "me1200DdmiConfigGlobalsInfoGroup": me1200DdmiConfigGlobalsInfoGroup,
       "me1200DdmiStatusInterfaceTableInfoGroup": me1200DdmiStatusInterfaceTableInfoGroup,
       "me1200DdmiNotificationInfoGroup": me1200DdmiNotificationInfoGroup}
)
