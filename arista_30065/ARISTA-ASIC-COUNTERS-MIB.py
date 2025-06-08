# SNMP MIB module (ARISTA-ASIC-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-ASIC-COUNTERS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:35 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

aristaAsicCountersMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29)
)
if mibBuilder.loadTexts:
    aristaAsicCountersMIB.setRevisions(
        ("2021-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaAsicCountersMibNotifications_ObjectIdentity = ObjectIdentity
aristaAsicCountersMibNotifications = _AristaAsicCountersMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 0)
)
_AristaAsicCountersMibObjects_ObjectIdentity = ObjectIdentity
aristaAsicCountersMibObjects = _AristaAsicCountersMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1)
)


class _AristaAsicInternalDropStatsRatesSupported_Type(Bits):
    """Custom type aristaAsicInternalDropStatsRatesSupported based on Bits"""
    namedValues = NamedValues(
        *(("last1Min", 0),
          ("last10Min", 1),
          ("last1Hr", 2),
          ("last1Day", 3),
          ("last1Week", 4))
    )

_AristaAsicInternalDropStatsRatesSupported_Type.__name__ = "Bits"
_AristaAsicInternalDropStatsRatesSupported_Object = MibScalar
aristaAsicInternalDropStatsRatesSupported = _AristaAsicInternalDropStatsRatesSupported_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 1),
    _AristaAsicInternalDropStatsRatesSupported_Type()
)
aristaAsicInternalDropStatsRatesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsRatesSupported.setStatus("current")
_AristaAsicInternalDropStatsTable_Object = MibTable
aristaAsicInternalDropStatsTable = _AristaAsicInternalDropStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2)
)
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsTable.setStatus("current")
_AristaAsicInternalDropStatsEntry_Object = MibTableRow
aristaAsicInternalDropStatsEntry = _AristaAsicInternalDropStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1)
)
aristaAsicInternalDropStatsEntry.setIndexNames(
    (0, "ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStatsChipName"),
    (0, "ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStatsCounterName"),
)
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsEntry.setStatus("current")


class _AristaAsicInternalDropStatsChipName_Type(DisplayString):
    """Custom type aristaAsicInternalDropStatsChipName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AristaAsicInternalDropStatsChipName_Type.__name__ = "DisplayString"
_AristaAsicInternalDropStatsChipName_Object = MibTableColumn
aristaAsicInternalDropStatsChipName = _AristaAsicInternalDropStatsChipName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 1),
    _AristaAsicInternalDropStatsChipName_Type()
)
aristaAsicInternalDropStatsChipName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsChipName.setStatus("current")


class _AristaAsicInternalDropStatsCounterName_Type(DisplayString):
    """Custom type aristaAsicInternalDropStatsCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AristaAsicInternalDropStatsCounterName_Type.__name__ = "DisplayString"
_AristaAsicInternalDropStatsCounterName_Object = MibTableColumn
aristaAsicInternalDropStatsCounterName = _AristaAsicInternalDropStatsCounterName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 2),
    _AristaAsicInternalDropStatsCounterName_Type()
)
aristaAsicInternalDropStatsCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsCounterName.setStatus("current")
_AristaAsicInternalDropStatsCount_Type = Counter64
_AristaAsicInternalDropStatsCount_Object = MibTableColumn
aristaAsicInternalDropStatsCount = _AristaAsicInternalDropStatsCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 3),
    _AristaAsicInternalDropStatsCount_Type()
)
aristaAsicInternalDropStatsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsCount.setStatus("current")
_AristaAsicInternalDropStats1Min_Type = CounterBasedGauge64
_AristaAsicInternalDropStats1Min_Object = MibTableColumn
aristaAsicInternalDropStats1Min = _AristaAsicInternalDropStats1Min_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 4),
    _AristaAsicInternalDropStats1Min_Type()
)
aristaAsicInternalDropStats1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStats1Min.setStatus("current")
_AristaAsicInternalDropStats10Min_Type = CounterBasedGauge64
_AristaAsicInternalDropStats10Min_Object = MibTableColumn
aristaAsicInternalDropStats10Min = _AristaAsicInternalDropStats10Min_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 5),
    _AristaAsicInternalDropStats10Min_Type()
)
aristaAsicInternalDropStats10Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStats10Min.setStatus("current")
_AristaAsicInternalDropStats1Hr_Type = CounterBasedGauge64
_AristaAsicInternalDropStats1Hr_Object = MibTableColumn
aristaAsicInternalDropStats1Hr = _AristaAsicInternalDropStats1Hr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 6),
    _AristaAsicInternalDropStats1Hr_Type()
)
aristaAsicInternalDropStats1Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStats1Hr.setStatus("current")
_AristaAsicInternalDropStats1Day_Type = CounterBasedGauge64
_AristaAsicInternalDropStats1Day_Object = MibTableColumn
aristaAsicInternalDropStats1Day = _AristaAsicInternalDropStats1Day_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 7),
    _AristaAsicInternalDropStats1Day_Type()
)
aristaAsicInternalDropStats1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStats1Day.setStatus("current")
_AristaAsicInternalDropStats1Week_Type = CounterBasedGauge64
_AristaAsicInternalDropStats1Week_Object = MibTableColumn
aristaAsicInternalDropStats1Week = _AristaAsicInternalDropStats1Week_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 8),
    _AristaAsicInternalDropStats1Week_Type()
)
aristaAsicInternalDropStats1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStats1Week.setStatus("current")
_AristaAsicInternalDropStatsFirstTime_Type = TimeStamp
_AristaAsicInternalDropStatsFirstTime_Object = MibTableColumn
aristaAsicInternalDropStatsFirstTime = _AristaAsicInternalDropStatsFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 9),
    _AristaAsicInternalDropStatsFirstTime_Type()
)
aristaAsicInternalDropStatsFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsFirstTime.setStatus("current")
_AristaAsicInternalDropStatsLastTime_Type = TimeStamp
_AristaAsicInternalDropStatsLastTime_Object = MibTableColumn
aristaAsicInternalDropStatsLastTime = _AristaAsicInternalDropStatsLastTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 1, 2, 1, 10),
    _AristaAsicInternalDropStatsLastTime_Type()
)
aristaAsicInternalDropStatsLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaAsicInternalDropStatsLastTime.setStatus("current")
_AristaAsicCountersMibConformance_ObjectIdentity = ObjectIdentity
aristaAsicCountersMibConformance = _AristaAsicCountersMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 2)
)
_AristaAsicCountersMibCompliances_ObjectIdentity = ObjectIdentity
aristaAsicCountersMibCompliances = _AristaAsicCountersMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 2, 1)
)
_AristaAsicCountersMibGroups_ObjectIdentity = ObjectIdentity
aristaAsicCountersMibGroups = _AristaAsicCountersMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 2, 2)
)

# Managed Objects groups

aristaAsicCountersMibDropScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 2, 2, 1)
)
aristaAsicCountersMibDropScalarGroup.setObjects(
    ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStatsRatesSupported")
)
if mibBuilder.loadTexts:
    aristaAsicCountersMibDropScalarGroup.setStatus("current")

aristaAsicCountersMibDropTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 2, 2, 2)
)
aristaAsicCountersMibDropTableGroup.setObjects(
      *(("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStatsCount"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStats1Min"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStats10Min"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStats1Hr"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStats1Day"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStats1Week"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStatsFirstTime"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicInternalDropStatsLastTime"))
)
if mibBuilder.loadTexts:
    aristaAsicCountersMibDropTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaAsicCountersMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 29, 2, 1, 1)
)
aristaAsicCountersMibCompliance.setObjects(
      *(("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicCountersMibDropScalarGroup"),
        ("ARISTA-ASIC-COUNTERS-MIB", "aristaAsicCountersMibDropTableGroup"))
)
if mibBuilder.loadTexts:
    aristaAsicCountersMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-ASIC-COUNTERS-MIB",
    **{"aristaAsicCountersMIB": aristaAsicCountersMIB,
       "aristaAsicCountersMibNotifications": aristaAsicCountersMibNotifications,
       "aristaAsicCountersMibObjects": aristaAsicCountersMibObjects,
       "aristaAsicInternalDropStatsRatesSupported": aristaAsicInternalDropStatsRatesSupported,
       "aristaAsicInternalDropStatsTable": aristaAsicInternalDropStatsTable,
       "aristaAsicInternalDropStatsEntry": aristaAsicInternalDropStatsEntry,
       "aristaAsicInternalDropStatsChipName": aristaAsicInternalDropStatsChipName,
       "aristaAsicInternalDropStatsCounterName": aristaAsicInternalDropStatsCounterName,
       "aristaAsicInternalDropStatsCount": aristaAsicInternalDropStatsCount,
       "aristaAsicInternalDropStats1Min": aristaAsicInternalDropStats1Min,
       "aristaAsicInternalDropStats10Min": aristaAsicInternalDropStats10Min,
       "aristaAsicInternalDropStats1Hr": aristaAsicInternalDropStats1Hr,
       "aristaAsicInternalDropStats1Day": aristaAsicInternalDropStats1Day,
       "aristaAsicInternalDropStats1Week": aristaAsicInternalDropStats1Week,
       "aristaAsicInternalDropStatsFirstTime": aristaAsicInternalDropStatsFirstTime,
       "aristaAsicInternalDropStatsLastTime": aristaAsicInternalDropStatsLastTime,
       "aristaAsicCountersMibConformance": aristaAsicCountersMibConformance,
       "aristaAsicCountersMibCompliances": aristaAsicCountersMibCompliances,
       "aristaAsicCountersMibCompliance": aristaAsicCountersMibCompliance,
       "aristaAsicCountersMibGroups": aristaAsicCountersMibGroups,
       "aristaAsicCountersMibDropScalarGroup": aristaAsicCountersMibDropScalarGroup,
       "aristaAsicCountersMibDropTableGroup": aristaAsicCountersMibDropTableGroup}
)
