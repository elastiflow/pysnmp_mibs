# SNMP MIB module (RUIJIE-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TIME-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15)
)
if mibBuilder.loadTexts:
    ruijieTimeMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieTimeMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTimeMIBObjects = _RuijieTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 1)
)
_RuijieClockDateAndTime_Type = DateAndTime
_RuijieClockDateAndTime_Object = MibScalar
ruijieClockDateAndTime = _RuijieClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 1, 1),
    _RuijieClockDateAndTime_Type()
)
ruijieClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClockDateAndTime.setStatus("current")


class _RuijieClockWeek_Type(Integer32):
    """Custom type ruijieClockWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RuijieClockWeek_Type.__name__ = "Integer32"
_RuijieClockWeek_Object = MibScalar
ruijieClockWeek = _RuijieClockWeek_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 1, 2),
    _RuijieClockWeek_Type()
)
ruijieClockWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClockWeek.setStatus("current")
_RuijieTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTimeRangeMIBObjects = _RuijieTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2)
)
_RuijieTimeRangeTable_Object = MibTable
ruijieTimeRangeTable = _RuijieTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieTimeRangeTable.setStatus("current")
_RuijieTimeRangeEntry_Object = MibTableRow
ruijieTimeRangeEntry = _RuijieTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 1, 1)
)
ruijieTimeRangeEntry.setIndexNames(
    (0, "RUIJIE-TIME-MIB", "ruijieTimeRangeName"),
)
if mibBuilder.loadTexts:
    ruijieTimeRangeEntry.setStatus("current")


class _RuijieTimeRangeName_Type(DisplayString):
    """Custom type ruijieTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieTimeRangeName_Type.__name__ = "DisplayString"
_RuijieTimeRangeName_Object = MibTableColumn
ruijieTimeRangeName = _RuijieTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 1, 1, 1),
    _RuijieTimeRangeName_Type()
)
ruijieTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieTimeRangeName.setStatus("current")


class _RuijieTimeRangePeriodRuijie_Type(DateAndTime):
    """Custom type ruijieTimeRangePeriodRuijie based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_RuijieTimeRangePeriodRuijie_Type.__name__ = "DateAndTime"
_RuijieTimeRangePeriodRuijie_Object = MibTableColumn
ruijieTimeRangePeriodRuijie = _RuijieTimeRangePeriodRuijie_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 1, 1, 2),
    _RuijieTimeRangePeriodRuijie_Type()
)
ruijieTimeRangePeriodRuijie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodRuijie.setStatus("current")


class _RuijieTimeRangePeriodEnd_Type(DateAndTime):
    """Custom type ruijieTimeRangePeriodEnd based on DateAndTime"""
    defaultHexValue = "9999123123595909"


_RuijieTimeRangePeriodEnd_Type.__name__ = "DateAndTime"
_RuijieTimeRangePeriodEnd_Object = MibTableColumn
ruijieTimeRangePeriodEnd = _RuijieTimeRangePeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 1, 1, 3),
    _RuijieTimeRangePeriodEnd_Type()
)
ruijieTimeRangePeriodEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodEnd.setStatus("current")
_RuijieTimeRangeRowStatus_Type = RowStatus
_RuijieTimeRangeRowStatus_Object = MibTableColumn
ruijieTimeRangeRowStatus = _RuijieTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 1, 1, 4),
    _RuijieTimeRangeRowStatus_Type()
)
ruijieTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangeRowStatus.setStatus("current")
_RuijieTimeRangePeriodicTable_Object = MibTable
ruijieTimeRangePeriodicTable = _RuijieTimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicTable.setStatus("current")
_RuijieTimeRangePeriodicEntry_Object = MibTableRow
ruijieTimeRangePeriodicEntry = _RuijieTimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1)
)
ruijieTimeRangePeriodicEntry.setIndexNames(
    (0, "RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicTRName"),
)
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicEntry.setStatus("current")


class _RuijieTimeRangePeriodicTRName_Type(DisplayString):
    """Custom type ruijieTimeRangePeriodicTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieTimeRangePeriodicTRName_Type.__name__ = "DisplayString"
_RuijieTimeRangePeriodicTRName_Object = MibTableColumn
ruijieTimeRangePeriodicTRName = _RuijieTimeRangePeriodicTRName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 1),
    _RuijieTimeRangePeriodicTRName_Type()
)
ruijieTimeRangePeriodicTRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicTRName.setStatus("current")


class _RuijieTimeRangePeriodicIndex_Type(Integer32):
    """Custom type ruijieTimeRangePeriodicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieTimeRangePeriodicIndex_Type.__name__ = "Integer32"
_RuijieTimeRangePeriodicIndex_Object = MibTableColumn
ruijieTimeRangePeriodicIndex = _RuijieTimeRangePeriodicIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 2),
    _RuijieTimeRangePeriodicIndex_Type()
)
ruijieTimeRangePeriodicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicIndex.setStatus("current")


class _RuijieTimeRangePeriodicType_Type(Integer32):
    """Custom type ruijieTimeRangePeriodicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed-segment", 1),
          ("unfixed-segment", 2))
    )


_RuijieTimeRangePeriodicType_Type.__name__ = "Integer32"
_RuijieTimeRangePeriodicType_Object = MibTableColumn
ruijieTimeRangePeriodicType = _RuijieTimeRangePeriodicType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 3),
    _RuijieTimeRangePeriodicType_Type()
)
ruijieTimeRangePeriodicType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicType.setStatus("current")


class _RuijieTimeRangePeriodicRuijieWeekDay_Type(OctetString):
    """Custom type ruijieTimeRangePeriodicRuijieWeekDay based on OctetString"""
    defaultHexValue = "fe"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RuijieTimeRangePeriodicRuijieWeekDay_Type.__name__ = "OctetString"
_RuijieTimeRangePeriodicRuijieWeekDay_Object = MibTableColumn
ruijieTimeRangePeriodicRuijieWeekDay = _RuijieTimeRangePeriodicRuijieWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 4),
    _RuijieTimeRangePeriodicRuijieWeekDay_Type()
)
ruijieTimeRangePeriodicRuijieWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicRuijieWeekDay.setStatus("current")


class _RuijieTimeRangePeriodicEndWeekDay_Type(Integer32):
    """Custom type ruijieTimeRangePeriodicEndWeekDay based on Integer32"""
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
        *(("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6),
          ("sunday", 7))
    )


_RuijieTimeRangePeriodicEndWeekDay_Type.__name__ = "Integer32"
_RuijieTimeRangePeriodicEndWeekDay_Object = MibTableColumn
ruijieTimeRangePeriodicEndWeekDay = _RuijieTimeRangePeriodicEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 5),
    _RuijieTimeRangePeriodicEndWeekDay_Type()
)
ruijieTimeRangePeriodicEndWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicEndWeekDay.setStatus("current")
_RuijieTimeRangePeriodicTimeOfDayRuijie_Type = DateAndTime
_RuijieTimeRangePeriodicTimeOfDayRuijie_Object = MibTableColumn
ruijieTimeRangePeriodicTimeOfDayRuijie = _RuijieTimeRangePeriodicTimeOfDayRuijie_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 6),
    _RuijieTimeRangePeriodicTimeOfDayRuijie_Type()
)
ruijieTimeRangePeriodicTimeOfDayRuijie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicTimeOfDayRuijie.setStatus("current")
_RuijieTimeRangePeriodicTimeOfDayEnd_Type = DateAndTime
_RuijieTimeRangePeriodicTimeOfDayEnd_Object = MibTableColumn
ruijieTimeRangePeriodicTimeOfDayEnd = _RuijieTimeRangePeriodicTimeOfDayEnd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 7),
    _RuijieTimeRangePeriodicTimeOfDayEnd_Type()
)
ruijieTimeRangePeriodicTimeOfDayEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicTimeOfDayEnd.setStatus("current")
_RuijieTimeRangePeriodicRowStatus_Type = RowStatus
_RuijieTimeRangePeriodicRowStatus_Object = MibTableColumn
ruijieTimeRangePeriodicRowStatus = _RuijieTimeRangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 2, 2, 1, 8),
    _RuijieTimeRangePeriodicRowStatus_Type()
)
ruijieTimeRangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTimeRangePeriodicRowStatus.setStatus("current")
_RuijieTimeMIBConformance_ObjectIdentity = ObjectIdentity
ruijieTimeMIBConformance = _RuijieTimeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 3)
)
_RuijieTimeMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieTimeMIBCompliances = _RuijieTimeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 3, 1)
)
_RuijieTimeMIBGroups_ObjectIdentity = ObjectIdentity
ruijieTimeMIBGroups = _RuijieTimeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 3, 2)
)

# Managed Objects groups

ruijieTimeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 3, 2, 1)
)
ruijieTimeMIBGroup.setObjects(
      *(("RUIJIE-TIME-MIB", "ruijieClockDateAndTime"),
        ("RUIJIE-TIME-MIB", "ruijieClockWeek"))
)
if mibBuilder.loadTexts:
    ruijieTimeMIBGroup.setStatus("current")

ruijieTimeRangeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 3, 2, 2)
)
ruijieTimeRangeMIBGroup.setObjects(
      *(("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicIndex"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicType"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicRuijieWeekDay"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicEndWeekDay"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicTimeOfDayRuijie"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicTimeOfDayEnd"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieTimeRangeMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieTimeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 15, 3, 1, 1)
)
ruijieTimeMIBCompliance.setObjects(
      *(("RUIJIE-TIME-MIB", "ruijieTimeMIBGroup"),
        ("RUIJIE-TIME-MIB", "ruijieTimeRangeMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieTimeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TIME-MIB",
    **{"ruijieTimeMIB": ruijieTimeMIB,
       "ruijieTimeMIBObjects": ruijieTimeMIBObjects,
       "ruijieClockDateAndTime": ruijieClockDateAndTime,
       "ruijieClockWeek": ruijieClockWeek,
       "ruijieTimeRangeMIBObjects": ruijieTimeRangeMIBObjects,
       "ruijieTimeRangeTable": ruijieTimeRangeTable,
       "ruijieTimeRangeEntry": ruijieTimeRangeEntry,
       "ruijieTimeRangeName": ruijieTimeRangeName,
       "ruijieTimeRangePeriodRuijie": ruijieTimeRangePeriodRuijie,
       "ruijieTimeRangePeriodEnd": ruijieTimeRangePeriodEnd,
       "ruijieTimeRangeRowStatus": ruijieTimeRangeRowStatus,
       "ruijieTimeRangePeriodicTable": ruijieTimeRangePeriodicTable,
       "ruijieTimeRangePeriodicEntry": ruijieTimeRangePeriodicEntry,
       "ruijieTimeRangePeriodicTRName": ruijieTimeRangePeriodicTRName,
       "ruijieTimeRangePeriodicIndex": ruijieTimeRangePeriodicIndex,
       "ruijieTimeRangePeriodicType": ruijieTimeRangePeriodicType,
       "ruijieTimeRangePeriodicRuijieWeekDay": ruijieTimeRangePeriodicRuijieWeekDay,
       "ruijieTimeRangePeriodicEndWeekDay": ruijieTimeRangePeriodicEndWeekDay,
       "ruijieTimeRangePeriodicTimeOfDayRuijie": ruijieTimeRangePeriodicTimeOfDayRuijie,
       "ruijieTimeRangePeriodicTimeOfDayEnd": ruijieTimeRangePeriodicTimeOfDayEnd,
       "ruijieTimeRangePeriodicRowStatus": ruijieTimeRangePeriodicRowStatus,
       "ruijieTimeMIBConformance": ruijieTimeMIBConformance,
       "ruijieTimeMIBCompliances": ruijieTimeMIBCompliances,
       "ruijieTimeMIBCompliance": ruijieTimeMIBCompliance,
       "ruijieTimeMIBGroups": ruijieTimeMIBGroups,
       "ruijieTimeMIBGroup": ruijieTimeMIBGroup,
       "ruijieTimeRangeMIBGroup": ruijieTimeRangeMIBGroup}
)
