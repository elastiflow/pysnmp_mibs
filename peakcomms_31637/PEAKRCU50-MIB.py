# SNMP MIB module (PEAKRCU50-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKRCU50-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(FaultType,
 OnlineOfflineType,
 RemoteLocalType,
 YesNoType,
 indvUnits) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "FaultType",
    "OnlineOfflineType",
    "RemoteLocalType",
    "YesNoType",
    "indvUnits")

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

peakRcu50Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009)
)
if mibBuilder.loadTexts:
    peakRcu50Module.setRevisions(
        ("2015-09-15 10:00",
         "2014-11-05 12:00",
         "2014-02-06 09:00",
         "2013-04-04 12:00",
         "2011-08-19 12:00",
         "2011-06-08 12:00",
         "2011-03-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rcu50AutoSwType(TextualConvention, Integer32):
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
        *(("unitA", 1),
          ("auto", 2),
          ("unitB", 3))
    )



class Rcu50BandType(TextualConvention, Integer32):
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
        *(("unitA", 1),
          ("unitB", 2),
          ("unknown", 3))
    )



class Rcu50AutoSwModeType(TextualConvention, Integer32):
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
        *(("alarms", 1),
          ("alarmsAndSignal", 2),
          ("signal", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Rcu50Type_Type = OctetString
_Rcu50Type_Object = MibScalar
rcu50Type = _Rcu50Type_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 1),
    _Rcu50Type_Type()
)
rcu50Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50Type.setStatus("current")


class _Rcu50SerialNo_Type(Integer32):
    """Custom type rcu50SerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rcu50SerialNo_Type.__name__ = "Integer32"
_Rcu50SerialNo_Object = MibScalar
rcu50SerialNo = _Rcu50SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 2),
    _Rcu50SerialNo_Type()
)
rcu50SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50SerialNo.setStatus("current")
_Rcu50SoftwareVersion_Type = OctetString
_Rcu50SoftwareVersion_Object = MibScalar
rcu50SoftwareVersion = _Rcu50SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 3),
    _Rcu50SoftwareVersion_Type()
)
rcu50SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50SoftwareVersion.setStatus("current")
_Rcu50Remote_Type = RemoteLocalType
_Rcu50Remote_Object = MibScalar
rcu50Remote = _Rcu50Remote_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 4),
    _Rcu50Remote_Type()
)
rcu50Remote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu50Remote.setStatus("current")
_Rcu50AutoSwitch_Type = Rcu50AutoSwType
_Rcu50AutoSwitch_Object = MibScalar
rcu50AutoSwitch = _Rcu50AutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 5),
    _Rcu50AutoSwitch_Type()
)
rcu50AutoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu50AutoSwitch.setStatus("current")
_Rcu50Band_Type = Rcu50BandType
_Rcu50Band_Object = MibScalar
rcu50Band = _Rcu50Band_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 6),
    _Rcu50Band_Type()
)
rcu50Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50Band.setStatus("current")
_Rcu50UnitA_Type = OnlineOfflineType
_Rcu50UnitA_Object = MibScalar
rcu50UnitA = _Rcu50UnitA_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 7),
    _Rcu50UnitA_Type()
)
rcu50UnitA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50UnitA.setStatus("current")
_Rcu50UnitB_Type = OnlineOfflineType
_Rcu50UnitB_Object = MibScalar
rcu50UnitB = _Rcu50UnitB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 8),
    _Rcu50UnitB_Type()
)
rcu50UnitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50UnitB.setStatus("current")
_Rcu50SummaryAlarm_Type = FaultType
_Rcu50SummaryAlarm_Object = MibScalar
rcu50SummaryAlarm = _Rcu50SummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 9),
    _Rcu50SummaryAlarm_Type()
)
rcu50SummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50SummaryAlarm.setStatus("current")
_UnitTable_Object = MibTable
unitTable = _UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10)
)
if mibBuilder.loadTexts:
    unitTable.setStatus("current")
_UnitTableEntry_Object = MibTableRow
unitTableEntry = _UnitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1)
)
unitTableEntry.setIndexNames(
    (0, "PEAKRCU50-MIB", "unitIndex"),
)
if mibBuilder.loadTexts:
    unitTableEntry.setStatus("current")


class _UnitIndex_Type(Integer32):
    """Custom type unitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UnitIndex_Type.__name__ = "Integer32"
_UnitIndex_Object = MibTableColumn
unitIndex = _UnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 1),
    _UnitIndex_Type()
)
unitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unitIndex.setStatus("current")
_UnitName_Type = OctetString
_UnitName_Object = MibTableColumn
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 2),
    _UnitName_Type()
)
unitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitName.setStatus("current")
_UnitLoCurrent_Type = FaultType
_UnitLoCurrent_Object = MibTableColumn
unitLoCurrent = _UnitLoCurrent_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 3),
    _UnitLoCurrent_Type()
)
unitLoCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitLoCurrent.setStatus("current")
_UnitHiCurrent_Type = FaultType
_UnitHiCurrent_Object = MibTableColumn
unitHiCurrent = _UnitHiCurrent_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 4),
    _UnitHiCurrent_Type()
)
unitHiCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitHiCurrent.setStatus("current")
_UnitAlarm_Type = FaultType
_UnitAlarm_Object = MibTableColumn
unitAlarm = _UnitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 5),
    _UnitAlarm_Type()
)
unitAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarm.setStatus("current")
_UnitSummaryAlarm_Type = FaultType
_UnitSummaryAlarm_Object = MibTableColumn
unitSummaryAlarm = _UnitSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 6),
    _UnitSummaryAlarm_Type()
)
unitSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSummaryAlarm.setStatus("current")
_UnitOnline_Type = OnlineOfflineType
_UnitOnline_Object = MibTableColumn
unitOnline = _UnitOnline_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 7),
    _UnitOnline_Type()
)
unitOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOnline.setStatus("current")
_UnitLoPower_Type = FaultType
_UnitLoPower_Object = MibTableColumn
unitLoPower = _UnitLoPower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 8),
    _UnitLoPower_Type()
)
unitLoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitLoPower.setStatus("current")
_UnitHiPower_Type = FaultType
_UnitHiPower_Object = MibTableColumn
unitHiPower = _UnitHiPower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 10, 1, 9),
    _UnitHiPower_Type()
)
unitHiPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitHiPower.setStatus("current")
_Rcu50HPAA_Type = FaultType
_Rcu50HPAA_Object = MibScalar
rcu50HPAA = _Rcu50HPAA_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 11),
    _Rcu50HPAA_Type()
)
rcu50HPAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50HPAA.setStatus("current")
_Rcu50HPAB_Type = FaultType
_Rcu50HPAB_Object = MibScalar
rcu50HPAB = _Rcu50HPAB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 12),
    _Rcu50HPAB_Type()
)
rcu50HPAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcu50HPAB.setStatus("current")
_Rcu50Reset_Type = YesNoType
_Rcu50Reset_Object = MibScalar
rcu50Reset = _Rcu50Reset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 13),
    _Rcu50Reset_Type()
)
rcu50Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu50Reset.setStatus("current")
_Rcu50AutoSwitchingMode_Type = Rcu50AutoSwModeType
_Rcu50AutoSwitchingMode_Object = MibScalar
rcu50AutoSwitchingMode = _Rcu50AutoSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 14),
    _Rcu50AutoSwitchingMode_Type()
)
rcu50AutoSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu50AutoSwitchingMode.setStatus("current")
_Rcu50LowPowerDelay_Type = OctetString
_Rcu50LowPowerDelay_Object = MibScalar
rcu50LowPowerDelay = _Rcu50LowPowerDelay_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 15),
    _Rcu50LowPowerDelay_Type()
)
rcu50LowPowerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu50LowPowerDelay.setStatus("current")
_Rcu50HighPowerDelay_Type = OctetString
_Rcu50HighPowerDelay_Object = MibScalar
rcu50HighPowerDelay = _Rcu50HighPowerDelay_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 16),
    _Rcu50HighPowerDelay_Type()
)
rcu50HighPowerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu50HighPowerDelay.setStatus("current")
_Rcu50ConvGroups_ObjectIdentity = ObjectIdentity
rcu50ConvGroups = _Rcu50ConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 110)
)
_Rcu50ConvConformance_ObjectIdentity = ObjectIdentity
rcu50ConvConformance = _Rcu50ConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 111)
)

# Managed Objects groups

rcu50CNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 110, 1)
)
rcu50CNFReqGrp.setObjects(
      *(("PEAKRCU50-MIB", "rcu50Type"),
        ("PEAKRCU50-MIB", "rcu50SerialNo"),
        ("PEAKRCU50-MIB", "rcu50SoftwareVersion"),
        ("PEAKRCU50-MIB", "rcu50Remote"),
        ("PEAKRCU50-MIB", "rcu50Band"),
        ("PEAKRCU50-MIB", "rcu50AutoSwitch"),
        ("PEAKRCU50-MIB", "rcu50UnitA"),
        ("PEAKRCU50-MIB", "rcu50UnitB"),
        ("PEAKRCU50-MIB", "rcu50SummaryAlarm"),
        ("PEAKRCU50-MIB", "rcu50Reset"))
)
if mibBuilder.loadTexts:
    rcu50CNFReqGrp.setStatus("current")

rcu50CNFUnitGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 110, 2)
)
rcu50CNFUnitGrp.setObjects(
      *(("PEAKRCU50-MIB", "unitName"),
        ("PEAKRCU50-MIB", "unitLoCurrent"),
        ("PEAKRCU50-MIB", "unitHiCurrent"),
        ("PEAKRCU50-MIB", "unitAlarm"),
        ("PEAKRCU50-MIB", "unitSummaryAlarm"),
        ("PEAKRCU50-MIB", "unitOnline"))
)
if mibBuilder.loadTexts:
    rcu50CNFUnitGrp.setStatus("current")

rcu50CNFHPAGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 110, 3)
)
rcu50CNFHPAGrp.setObjects(
      *(("PEAKRCU50-MIB", "rcu50HPAA"),
        ("PEAKRCU50-MIB", "rcu50HPAB"))
)
if mibBuilder.loadTexts:
    rcu50CNFHPAGrp.setStatus("current")

rcu50CNF10POGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 110, 4)
)
rcu50CNF10POGrp.setObjects(
      *(("PEAKRCU50-MIB", "unitName"),
        ("PEAKRCU50-MIB", "unitLoCurrent"),
        ("PEAKRCU50-MIB", "unitHiCurrent"),
        ("PEAKRCU50-MIB", "unitAlarm"),
        ("PEAKRCU50-MIB", "unitSummaryAlarm"),
        ("PEAKRCU50-MIB", "unitOnline"),
        ("PEAKRCU50-MIB", "unitLoPower"),
        ("PEAKRCU50-MIB", "unitHiPower"),
        ("PEAKRCU50-MIB", "rcu50AutoSwitchingMode"),
        ("PEAKRCU50-MIB", "rcu50LowPowerDelay"),
        ("PEAKRCU50-MIB", "rcu50HighPowerDelay"))
)
if mibBuilder.loadTexts:
    rcu50CNF10POGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rcu50CNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 6009, 111, 1)
)
rcu50CNFCompliance.setObjects(
      *(("PEAKRCU50-MIB", "rcu50CNFReqGrp"),
        ("PEAKRCU50-MIB", "rcu50CNFUnitGrp"),
        ("PEAKRCU50-MIB", "rcu50CNFHPAGrp"),
        ("PEAKRCU50-MIB", "rcu50CNF10POGrp"))
)
if mibBuilder.loadTexts:
    rcu50CNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKRCU50-MIB",
    **{"Rcu50AutoSwType": Rcu50AutoSwType,
       "Rcu50BandType": Rcu50BandType,
       "Rcu50AutoSwModeType": Rcu50AutoSwModeType,
       "peakRcu50Module": peakRcu50Module,
       "rcu50Type": rcu50Type,
       "rcu50SerialNo": rcu50SerialNo,
       "rcu50SoftwareVersion": rcu50SoftwareVersion,
       "rcu50Remote": rcu50Remote,
       "rcu50AutoSwitch": rcu50AutoSwitch,
       "rcu50Band": rcu50Band,
       "rcu50UnitA": rcu50UnitA,
       "rcu50UnitB": rcu50UnitB,
       "rcu50SummaryAlarm": rcu50SummaryAlarm,
       "unitTable": unitTable,
       "unitTableEntry": unitTableEntry,
       "unitIndex": unitIndex,
       "unitName": unitName,
       "unitLoCurrent": unitLoCurrent,
       "unitHiCurrent": unitHiCurrent,
       "unitAlarm": unitAlarm,
       "unitSummaryAlarm": unitSummaryAlarm,
       "unitOnline": unitOnline,
       "unitLoPower": unitLoPower,
       "unitHiPower": unitHiPower,
       "rcu50HPAA": rcu50HPAA,
       "rcu50HPAB": rcu50HPAB,
       "rcu50Reset": rcu50Reset,
       "rcu50AutoSwitchingMode": rcu50AutoSwitchingMode,
       "rcu50LowPowerDelay": rcu50LowPowerDelay,
       "rcu50HighPowerDelay": rcu50HighPowerDelay,
       "rcu50ConvGroups": rcu50ConvGroups,
       "rcu50CNFReqGrp": rcu50CNFReqGrp,
       "rcu50CNFUnitGrp": rcu50CNFUnitGrp,
       "rcu50CNFHPAGrp": rcu50CNFHPAGrp,
       "rcu50CNF10POGrp": rcu50CNF10POGrp,
       "rcu50ConvConformance": rcu50ConvConformance,
       "rcu50CNFCompliance": rcu50CNFCompliance}
)
