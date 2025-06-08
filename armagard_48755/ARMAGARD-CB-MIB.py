# SNMP MIB module (ARMAGARD-CB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/armagard_48755/ARMAGARD-CB-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:30:06 2025
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

(armagardCB,
 armagardProductsMIB) = mibBuilder.importSymbols(
    "ARMAGARD-PRODUCTS-MIB",
    "armagardCB",
    "armagardProductsMIB")

(armagardMIBGroups,) = mibBuilder.importSymbols(
    "ARMAGARD-SMI",
    "armagardMIBGroups")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

armagardProductsCB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48755, 2, 1, 1)
)
if mibBuilder.loadTexts:
    armagardProductsCB.setRevisions(
        ("2016-10-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArmagardCBInfo_ObjectIdentity = ObjectIdentity
armagardCBInfo = _ArmagardCBInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 0)
)
_ArmagardCBFirmwareVersion_Type = DisplayString
_ArmagardCBFirmwareVersion_Object = MibScalar
armagardCBFirmwareVersion = _ArmagardCBFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 0, 1),
    _ArmagardCBFirmwareVersion_Type()
)
armagardCBFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBFirmwareVersion.setStatus("current")


class _ArmagardCBFirmwareVersionVal_Type(Integer32):
    """Custom type armagardCBFirmwareVersionVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ArmagardCBFirmwareVersionVal_Type.__name__ = "Integer32"
_ArmagardCBFirmwareVersionVal_Object = MibScalar
armagardCBFirmwareVersionVal = _ArmagardCBFirmwareVersionVal_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 0, 2),
    _ArmagardCBFirmwareVersionVal_Type()
)
armagardCBFirmwareVersionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBFirmwareVersionVal.setStatus("current")
_ArmagardCBStatus_ObjectIdentity = ObjectIdentity
armagardCBStatus = _ArmagardCBStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 1)
)


class _ArmagardCBFanStatus_Type(Integer32):
    """Custom type armagardCBFanStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ArmagardCBFanStatus_Type.__name__ = "Integer32"
_ArmagardCBFanStatus_Object = MibScalar
armagardCBFanStatus = _ArmagardCBFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 1, 1),
    _ArmagardCBFanStatus_Type()
)
armagardCBFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBFanStatus.setStatus("current")


class _ArmagardCBHeaterStatus_Type(Integer32):
    """Custom type armagardCBHeaterStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ArmagardCBHeaterStatus_Type.__name__ = "Integer32"
_ArmagardCBHeaterStatus_Object = MibScalar
armagardCBHeaterStatus = _ArmagardCBHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 1, 2),
    _ArmagardCBHeaterStatus_Type()
)
armagardCBHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBHeaterStatus.setStatus("current")


class _ArmagardCBMediaStatus_Type(Integer32):
    """Custom type armagardCBMediaStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ArmagardCBMediaStatus_Type.__name__ = "Integer32"
_ArmagardCBMediaStatus_Object = MibScalar
armagardCBMediaStatus = _ArmagardCBMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 1, 3),
    _ArmagardCBMediaStatus_Type()
)
armagardCBMediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBMediaStatus.setStatus("current")


class _ArmagardCBTVStatus_Type(Integer32):
    """Custom type armagardCBTVStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ArmagardCBTVStatus_Type.__name__ = "Integer32"
_ArmagardCBTVStatus_Object = MibScalar
armagardCBTVStatus = _ArmagardCBTVStatus_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 1, 4),
    _ArmagardCBTVStatus_Type()
)
armagardCBTVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBTVStatus.setStatus("current")
_ArmagardCBTemps_ObjectIdentity = ObjectIdentity
armagardCBTemps = _ArmagardCBTemps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 2)
)


class _ArmagardCBOnboardTemperature_Type(Integer32):
    """Custom type armagardCBOnboardTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ArmagardCBOnboardTemperature_Type.__name__ = "Integer32"
_ArmagardCBOnboardTemperature_Object = MibScalar
armagardCBOnboardTemperature = _ArmagardCBOnboardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 2, 1),
    _ArmagardCBOnboardTemperature_Type()
)
armagardCBOnboardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBOnboardTemperature.setStatus("current")


class _ArmagardCBOffboardTemperature_Type(Integer32):
    """Custom type armagardCBOffboardTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ArmagardCBOffboardTemperature_Type.__name__ = "Integer32"
_ArmagardCBOffboardTemperature_Object = MibScalar
armagardCBOffboardTemperature = _ArmagardCBOffboardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 2, 2),
    _ArmagardCBOffboardTemperature_Type()
)
armagardCBOffboardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBOffboardTemperature.setStatus("current")
_ArmagardCBSpeeds_ObjectIdentity = ObjectIdentity
armagardCBSpeeds = _ArmagardCBSpeeds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 3)
)


class _ArmagardCBFanSpeed1_Type(Integer32):
    """Custom type armagardCBFanSpeed1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ArmagardCBFanSpeed1_Type.__name__ = "Integer32"
_ArmagardCBFanSpeed1_Object = MibScalar
armagardCBFanSpeed1 = _ArmagardCBFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 3, 1),
    _ArmagardCBFanSpeed1_Type()
)
armagardCBFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBFanSpeed1.setStatus("current")


class _ArmagardCBFanSpeed2_Type(Integer32):
    """Custom type armagardCBFanSpeed2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ArmagardCBFanSpeed2_Type.__name__ = "Integer32"
_ArmagardCBFanSpeed2_Object = MibScalar
armagardCBFanSpeed2 = _ArmagardCBFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 48755, 1, 1, 3, 2),
    _ArmagardCBFanSpeed2_Type()
)
armagardCBFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armagardCBFanSpeed2.setStatus("current")

# Managed Objects groups

armagardInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48755, 9, 2, 1)
)
armagardInfoGroup.setObjects(
      *(("ARMAGARD-CB-MIB", "armagardCBFirmwareVersion"),
        ("ARMAGARD-CB-MIB", "armagardCBFirmwareVersionVal"))
)
if mibBuilder.loadTexts:
    armagardInfoGroup.setStatus("current")

armagardStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48755, 9, 2, 2)
)
armagardStatusGroup.setObjects(
      *(("ARMAGARD-CB-MIB", "armagardCBFanStatus"),
        ("ARMAGARD-CB-MIB", "armagardCBHeaterStatus"),
        ("ARMAGARD-CB-MIB", "armagardCBMediaStatus"),
        ("ARMAGARD-CB-MIB", "armagardCBTVStatus"))
)
if mibBuilder.loadTexts:
    armagardStatusGroup.setStatus("current")

armagardTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48755, 9, 2, 3)
)
armagardTemperatureGroup.setObjects(
      *(("ARMAGARD-CB-MIB", "armagardCBOnboardTemperature"),
        ("ARMAGARD-CB-MIB", "armagardCBOffboardTemperature"))
)
if mibBuilder.loadTexts:
    armagardTemperatureGroup.setStatus("current")

armagardSpeedsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48755, 9, 2, 4)
)
armagardSpeedsGroup.setObjects(
      *(("ARMAGARD-CB-MIB", "armagardCBFanSpeed1"),
        ("ARMAGARD-CB-MIB", "armagardCBFanSpeed2"))
)
if mibBuilder.loadTexts:
    armagardSpeedsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARMAGARD-CB-MIB",
    **{"armagardCBInfo": armagardCBInfo,
       "armagardCBFirmwareVersion": armagardCBFirmwareVersion,
       "armagardCBFirmwareVersionVal": armagardCBFirmwareVersionVal,
       "armagardCBStatus": armagardCBStatus,
       "armagardCBFanStatus": armagardCBFanStatus,
       "armagardCBHeaterStatus": armagardCBHeaterStatus,
       "armagardCBMediaStatus": armagardCBMediaStatus,
       "armagardCBTVStatus": armagardCBTVStatus,
       "armagardCBTemps": armagardCBTemps,
       "armagardCBOnboardTemperature": armagardCBOnboardTemperature,
       "armagardCBOffboardTemperature": armagardCBOffboardTemperature,
       "armagardCBSpeeds": armagardCBSpeeds,
       "armagardCBFanSpeed1": armagardCBFanSpeed1,
       "armagardCBFanSpeed2": armagardCBFanSpeed2,
       "armagardProductsCB": armagardProductsCB,
       "armagardInfoGroup": armagardInfoGroup,
       "armagardStatusGroup": armagardStatusGroup,
       "armagardTemperatureGroup": armagardTemperatureGroup,
       "armagardSpeedsGroup": armagardSpeedsGroup}
)
