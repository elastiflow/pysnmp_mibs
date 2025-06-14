# SNMP MIB module (COFFEE-POT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/COFFEE-POT-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:24:51 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TimeInterval,
 TimeStamp,
 TimeTicks,
 Unsigned32,
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "TimeInterval",
    "TimeStamp",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

coffee = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 132)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PotName_Type(DisplayString):
    """Custom type potName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PotName_Type.__name__ = "DisplayString"
_PotName_Object = MibScalar
potName = _PotName_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 1),
    _PotName_Type()
)
potName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potName.setStatus("current")
_PotCapacity_Type = Integer32
_PotCapacity_Object = MibScalar
potCapacity = _PotCapacity_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 2),
    _PotCapacity_Type()
)
potCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potCapacity.setStatus("current")


class _PotType_Type(Integer32):
    """Custom type potType based on Integer32"""
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
        *(("automatic-drip", 1),
          ("percolator", 2),
          ("french-press", 3),
          ("espresso", 4))
    )


_PotType_Type.__name__ = "Integer32"
_PotType_Object = MibScalar
potType = _PotType_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 3),
    _PotType_Type()
)
potType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potType.setStatus("current")


class _PotLocation_Type(DisplayString):
    """Custom type potLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PotLocation_Type.__name__ = "DisplayString"
_PotLocation_Object = MibScalar
potLocation = _PotLocation_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 4),
    _PotLocation_Type()
)
potLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potLocation.setStatus("current")
_PotMonitor_ObjectIdentity = ObjectIdentity
potMonitor = _PotMonitor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 132, 6)
)


class _PotOperStatus_Type(Integer32):
    """Custom type potOperStatus based on Integer32"""
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
        *(("off", 1),
          ("brewing", 2),
          ("holding", 3),
          ("other", 4),
          ("waiting", 5))
    )


_PotOperStatus_Type.__name__ = "Integer32"
_PotOperStatus_Object = MibScalar
potOperStatus = _PotOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 6, 1),
    _PotOperStatus_Type()
)
potOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potOperStatus.setStatus("current")
_PotLevel_Type = Integer32
_PotLevel_Object = MibScalar
potLevel = _PotLevel_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 6, 2),
    _PotLevel_Type()
)
potLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potLevel.setStatus("current")


class _PotMetric_Type(Integer32):
    """Custom type potMetric based on Integer32"""
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
        *(("espresso", 1),
          ("demi-tasse", 2),
          ("cup", 3),
          ("mug", 4),
          ("bucket", 5))
    )


_PotMetric_Type.__name__ = "Integer32"
_PotMetric_Object = MibScalar
potMetric = _PotMetric_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 6, 3),
    _PotMetric_Type()
)
potMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potMetric.setStatus("current")
_PotStartTime_Type = Integer32
_PotStartTime_Object = MibScalar
potStartTime = _PotStartTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 6, 4),
    _PotStartTime_Type()
)
potStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potStartTime.setStatus("current")
_LastStartTime_Type = TimeInterval
_LastStartTime_Object = MibScalar
lastStartTime = _LastStartTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 6, 5),
    _LastStartTime_Type()
)
lastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastStartTime.setStatus("current")
_PotTemperature_Type = Integer32
_PotTemperature_Object = MibScalar
potTemperature = _PotTemperature_Object(
    (1, 3, 6, 1, 2, 1, 10, 132, 6, 6),
    _PotTemperature_Type()
)
potTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potTemperature.setStatus("current")
if mibBuilder.loadTexts:
    potTemperature.setUnits("degrees Centigrade")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COFFEE-POT-MIB",
    **{"coffee": coffee,
       "potName": potName,
       "potCapacity": potCapacity,
       "potType": potType,
       "potLocation": potLocation,
       "potMonitor": potMonitor,
       "potOperStatus": potOperStatus,
       "potLevel": potLevel,
       "potMetric": potMetric,
       "potStartTime": potStartTime,
       "lastStartTime": lastStartTime,
       "potTemperature": potTemperature}
)
