# SNMP MIB module (SCHNEIDER-ELECTRIC-BCPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/schneider_3833/SCHNEIDER-ELECTRIC-BCPM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:06:19 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

schneiderBcpmModuleID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 3)
)
if mibBuilder.loadTexts:
    schneiderBcpmModuleID.setRevisions(
        ("2013-12-17 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ThousandthsInt32(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class TenthsInt32(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class TenthsCounter64(TextualConvention, Counter64):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_SchneiderElectric_ObjectIdentity = ObjectIdentity
schneiderElectric = _SchneiderElectric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833)
)
_SchneiderEnergy_ObjectIdentity = ObjectIdentity
schneiderEnergy = _SchneiderEnergy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1)
)
_Bcpm_ObjectIdentity = ObjectIdentity
bcpm = _Bcpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30)
)
_Panels_ObjectIdentity = ObjectIdentity
panels = _Panels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1)
)
_Panel1_ObjectIdentity = ObjectIdentity
panel1 = _Panel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1)
)
_P1Alarms_ObjectIdentity = ObjectIdentity
p1Alarms = _P1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1)
)
_P1Traps_ObjectIdentity = ObjectIdentity
p1Traps = _P1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 0)
)
_P1GlobalAlarmStatus_ObjectIdentity = ObjectIdentity
p1GlobalAlarmStatus = _P1GlobalAlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1)
)


class _P1GlobalLatchingAlarmStatus_Type(Bits):
    """Custom type p1GlobalLatchingAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("p1GlobalLatchingAlarmStatusHighHighCurrent", 0),
          ("p1GlobalLatchingAlarmStatusHighCurrent", 1),
          ("p1GlobalLatchingAlarmStatusLowCurrent", 2),
          ("p1GlobalLatchingAlarmStatusLowLowCurrent", 3),
          ("p1GlobalLatchingAlarmStatusAlarmOff", 4),
          ("p1GlobalLatchingAlarmStatusHighVoltage", 8),
          ("p1GlobalLatchingAlarmStatusLowVoltage", 9))
    )

_P1GlobalLatchingAlarmStatus_Type.__name__ = "Bits"
_P1GlobalLatchingAlarmStatus_Object = MibScalar
p1GlobalLatchingAlarmStatus = _P1GlobalLatchingAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 1),
    _P1GlobalLatchingAlarmStatus_Type()
)
p1GlobalLatchingAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalLatchingAlarmStatus.setStatus("current")


class _P1GlobalNonLatchingAlarmStatus_Type(Bits):
    """Custom type p1GlobalNonLatchingAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("p1GlobalNonLatchingAlarmStatusHighCurrent", 0),
          ("p1GlobalNonLatchingAlarmStatusLowCurrent", 1),
          ("p1GlobalNonLatchingAlarmStatusHighVoltage", 8),
          ("p1GlobalNonLatchingAlarmStatusLowVoltage", 9))
    )

_P1GlobalNonLatchingAlarmStatus_Type.__name__ = "Bits"
_P1GlobalNonLatchingAlarmStatus_Object = MibScalar
p1GlobalNonLatchingAlarmStatus = _P1GlobalNonLatchingAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 2),
    _P1GlobalNonLatchingAlarmStatus_Type()
)
p1GlobalNonLatchingAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalNonLatchingAlarmStatus.setStatus("current")


class _P1GlobalMostRecentLatchingChannel_Type(Unsigned32):
    """Custom type p1GlobalMostRecentLatchingChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 46),
    )


_P1GlobalMostRecentLatchingChannel_Type.__name__ = "Unsigned32"
_P1GlobalMostRecentLatchingChannel_Object = MibScalar
p1GlobalMostRecentLatchingChannel = _P1GlobalMostRecentLatchingChannel_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 3),
    _P1GlobalMostRecentLatchingChannel_Type()
)
p1GlobalMostRecentLatchingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalMostRecentLatchingChannel.setStatus("current")


class _P1GlobalMostRecentNonLatchingChannel_Type(Unsigned32):
    """Custom type p1GlobalMostRecentNonLatchingChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 46),
    )


_P1GlobalMostRecentNonLatchingChannel_Type.__name__ = "Unsigned32"
_P1GlobalMostRecentNonLatchingChannel_Object = MibScalar
p1GlobalMostRecentNonLatchingChannel = _P1GlobalMostRecentNonLatchingChannel_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 4),
    _P1GlobalMostRecentNonLatchingChannel_Type()
)
p1GlobalMostRecentNonLatchingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalMostRecentNonLatchingChannel.setStatus("current")
_P1TotalLatchingChannelsInAlarm_Type = Unsigned32
_P1TotalLatchingChannelsInAlarm_Object = MibScalar
p1TotalLatchingChannelsInAlarm = _P1TotalLatchingChannelsInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 5),
    _P1TotalLatchingChannelsInAlarm_Type()
)
p1TotalLatchingChannelsInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1TotalLatchingChannelsInAlarm.setStatus("current")
_P1TotalNonLatchingChannelsInAlarm_Type = Unsigned32
_P1TotalNonLatchingChannelsInAlarm_Object = MibScalar
p1TotalNonLatchingChannelsInAlarm = _P1TotalNonLatchingChannelsInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 6),
    _P1TotalNonLatchingChannelsInAlarm_Type()
)
p1TotalNonLatchingChannelsInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1TotalNonLatchingChannelsInAlarm.setStatus("current")


class _P1DeviceHealth_Type(Bits):
    """Custom type p1DeviceHealth based on Bits"""
    namedValues = NamedValues(
        *(("p1DeviceHealthReservedBit0", 0),
          ("p1DeviceHealthPhaseAFrequencyOutRange", 1),
          ("p1DeviceHealthPhaseAVoltageClipping", 2),
          ("p1DeviceHealthPhaseBVoltageClipping", 3),
          ("p1DeviceHealthPhaseCVoltageClipping", 4),
          ("p1DeviceHealthCurrentClipping", 5),
          ("p1DeviceHealthStripConnectionError", 8),
          ("p1DeviceHealthCurrentOnlyModel", 13),
          ("p1DeviceHealthAuxPowerModel", 14),
          ("p1DeviceHealthBranchPowerModel", 15))
    )

_P1DeviceHealth_Type.__name__ = "Bits"
_P1DeviceHealth_Object = MibScalar
p1DeviceHealth = _P1DeviceHealth_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 1, 7),
    _P1DeviceHealth_Type()
)
p1DeviceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1DeviceHealth.setStatus("current")
_P1GlobalAlarmCounters_ObjectIdentity = ObjectIdentity
p1GlobalAlarmCounters = _P1GlobalAlarmCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2)
)


class _P1GlobalHighHighLatchingAlarmCount_Type(Unsigned32):
    """Custom type p1GlobalHighHighLatchingAlarmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1GlobalHighHighLatchingAlarmCount_Type.__name__ = "Unsigned32"
_P1GlobalHighHighLatchingAlarmCount_Object = MibScalar
p1GlobalHighHighLatchingAlarmCount = _P1GlobalHighHighLatchingAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2, 1),
    _P1GlobalHighHighLatchingAlarmCount_Type()
)
p1GlobalHighHighLatchingAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalHighHighLatchingAlarmCount.setStatus("current")


class _P1GlobalHighLatchingAlarmCount_Type(Unsigned32):
    """Custom type p1GlobalHighLatchingAlarmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1GlobalHighLatchingAlarmCount_Type.__name__ = "Unsigned32"
_P1GlobalHighLatchingAlarmCount_Object = MibScalar
p1GlobalHighLatchingAlarmCount = _P1GlobalHighLatchingAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2, 2),
    _P1GlobalHighLatchingAlarmCount_Type()
)
p1GlobalHighLatchingAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalHighLatchingAlarmCount.setStatus("current")


class _P1GlobalLowLatchingAlarmCount_Type(Unsigned32):
    """Custom type p1GlobalLowLatchingAlarmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1GlobalLowLatchingAlarmCount_Type.__name__ = "Unsigned32"
_P1GlobalLowLatchingAlarmCount_Object = MibScalar
p1GlobalLowLatchingAlarmCount = _P1GlobalLowLatchingAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2, 3),
    _P1GlobalLowLatchingAlarmCount_Type()
)
p1GlobalLowLatchingAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalLowLatchingAlarmCount.setStatus("current")


class _P1GlobalLowLowLatchingAlarmCount_Type(Unsigned32):
    """Custom type p1GlobalLowLowLatchingAlarmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1GlobalLowLowLatchingAlarmCount_Type.__name__ = "Unsigned32"
_P1GlobalLowLowLatchingAlarmCount_Object = MibScalar
p1GlobalLowLowLatchingAlarmCount = _P1GlobalLowLowLatchingAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2, 4),
    _P1GlobalLowLowLatchingAlarmCount_Type()
)
p1GlobalLowLowLatchingAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalLowLowLatchingAlarmCount.setStatus("current")


class _P1GlobalOffStateLatchingAlarmCount_Type(Unsigned32):
    """Custom type p1GlobalOffStateLatchingAlarmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1GlobalOffStateLatchingAlarmCount_Type.__name__ = "Unsigned32"
_P1GlobalOffStateLatchingAlarmCount_Object = MibScalar
p1GlobalOffStateLatchingAlarmCount = _P1GlobalOffStateLatchingAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2, 5),
    _P1GlobalOffStateLatchingAlarmCount_Type()
)
p1GlobalOffStateLatchingAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1GlobalOffStateLatchingAlarmCount.setStatus("current")


class _P1PowerUpCount_Type(Unsigned32):
    """Custom type p1PowerUpCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1PowerUpCount_Type.__name__ = "Unsigned32"
_P1PowerUpCount_Object = MibScalar
p1PowerUpCount = _P1PowerUpCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 2, 6),
    _P1PowerUpCount_Type()
)
p1PowerUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1PowerUpCount.setStatus("current")
_P1AuxVoltageAndCurrentAlarmTable_Object = MibTable
p1AuxVoltageAndCurrentAlarmTable = _P1AuxVoltageAndCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    p1AuxVoltageAndCurrentAlarmTable.setStatus("current")
_P1AuxVoltageAndCurrentAlarmEntry_Object = MibTableRow
p1AuxVoltageAndCurrentAlarmEntry = _P1AuxVoltageAndCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1)
)
p1AuxVoltageAndCurrentAlarmEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxAlarmIndex"),
)
if mibBuilder.loadTexts:
    p1AuxVoltageAndCurrentAlarmEntry.setStatus("current")


class _P1AuxAlarmIndex_Type(Unsigned32):
    """Custom type p1AuxAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_P1AuxAlarmIndex_Type.__name__ = "Unsigned32"
_P1AuxAlarmIndex_Object = MibTableColumn
p1AuxAlarmIndex = _P1AuxAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 1),
    _P1AuxAlarmIndex_Type()
)
p1AuxAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1AuxAlarmIndex.setStatus("current")


class _P1AuxAlarmPhase_Type(Unsigned32):
    """Custom type p1AuxAlarmPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_P1AuxAlarmPhase_Type.__name__ = "Unsigned32"
_P1AuxAlarmPhase_Object = MibTableColumn
p1AuxAlarmPhase = _P1AuxAlarmPhase_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 2),
    _P1AuxAlarmPhase_Type()
)
p1AuxAlarmPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxAlarmPhase.setStatus("current")


class _P1VoltagePhaseAlarmStatus_Type(Bits):
    """Custom type p1VoltagePhaseAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("p1VoltagePhaseAlarmStatusHighLatching", 0),
          ("p1VoltagePhaseAlarmStatusLowLatching", 1),
          ("p1VoltagePhaseAlarmStatusHighNonLatching", 8),
          ("p1VoltagePhaseAlarmStatusLowNonLatching", 9))
    )

_P1VoltagePhaseAlarmStatus_Type.__name__ = "Bits"
_P1VoltagePhaseAlarmStatus_Object = MibTableColumn
p1VoltagePhaseAlarmStatus = _P1VoltagePhaseAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 3),
    _P1VoltagePhaseAlarmStatus_Type()
)
p1VoltagePhaseAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1VoltagePhaseAlarmStatus.setStatus("current")


class _P1AuxCurrentAlarmStatus_Type(Bits):
    """Custom type p1AuxCurrentAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("p1AuxCurrentAlarmStatusHighHighAmp", 0),
          ("p1AuxCurrentAlarmStatusHighAmp", 1),
          ("p1AuxCurrentAlarmStatusLowAmp", 2),
          ("p1AuxCurrentAlarmStatusLowLowAmp", 3),
          ("p1AuxCurrentAlarmStatusAlarmOff", 4),
          ("p1AuxCurrentAlarmStatusHighVolt", 8),
          ("p1AuxCurrentAlarmStatusLowVolt", 9))
    )

_P1AuxCurrentAlarmStatus_Type.__name__ = "Bits"
_P1AuxCurrentAlarmStatus_Object = MibTableColumn
p1AuxCurrentAlarmStatus = _P1AuxCurrentAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 4),
    _P1AuxCurrentAlarmStatus_Type()
)
p1AuxCurrentAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxCurrentAlarmStatus.setStatus("current")
_P1AuxHighHighAlarmCount_Type = Counter32
_P1AuxHighHighAlarmCount_Object = MibTableColumn
p1AuxHighHighAlarmCount = _P1AuxHighHighAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 5),
    _P1AuxHighHighAlarmCount_Type()
)
p1AuxHighHighAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxHighHighAlarmCount.setStatus("current")
_P1AuxHighAlarmCount_Type = Counter32
_P1AuxHighAlarmCount_Object = MibTableColumn
p1AuxHighAlarmCount = _P1AuxHighAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 6),
    _P1AuxHighAlarmCount_Type()
)
p1AuxHighAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxHighAlarmCount.setStatus("current")
_P1AuxLowAlarmCount_Type = Counter32
_P1AuxLowAlarmCount_Object = MibTableColumn
p1AuxLowAlarmCount = _P1AuxLowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 7),
    _P1AuxLowAlarmCount_Type()
)
p1AuxLowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxLowAlarmCount.setStatus("current")
_P1AuxLowLowAlarmCount_Type = Counter32
_P1AuxLowLowAlarmCount_Object = MibTableColumn
p1AuxLowLowAlarmCount = _P1AuxLowLowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 8),
    _P1AuxLowLowAlarmCount_Type()
)
p1AuxLowLowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxLowLowAlarmCount.setStatus("current")
_P1AuxOffStateAlarmCount_Type = Counter32
_P1AuxOffStateAlarmCount_Object = MibTableColumn
p1AuxOffStateAlarmCount = _P1AuxOffStateAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 3, 1, 9),
    _P1AuxOffStateAlarmCount_Type()
)
p1AuxOffStateAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxOffStateAlarmCount.setStatus("current")
_P1BranchCurrentAlarmTable_Object = MibTable
p1BranchCurrentAlarmTable = _P1BranchCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    p1BranchCurrentAlarmTable.setStatus("current")
_P1BranchCurrentAlarmEntry_Object = MibTableRow
p1BranchCurrentAlarmEntry = _P1BranchCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1)
)
p1BranchCurrentAlarmEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchAlarmIndex"),
)
if mibBuilder.loadTexts:
    p1BranchCurrentAlarmEntry.setStatus("current")


class _P1BranchAlarmIndex_Type(Unsigned32):
    """Custom type p1BranchAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_P1BranchAlarmIndex_Type.__name__ = "Unsigned32"
_P1BranchAlarmIndex_Object = MibTableColumn
p1BranchAlarmIndex = _P1BranchAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 1),
    _P1BranchAlarmIndex_Type()
)
p1BranchAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1BranchAlarmIndex.setStatus("current")


class _P1BranchAlarmNumber_Type(Unsigned32):
    """Custom type p1BranchAlarmNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_P1BranchAlarmNumber_Type.__name__ = "Unsigned32"
_P1BranchAlarmNumber_Object = MibTableColumn
p1BranchAlarmNumber = _P1BranchAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 2),
    _P1BranchAlarmNumber_Type()
)
p1BranchAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchAlarmNumber.setStatus("current")


class _P1BranchCurrentAlarmStatus_Type(Bits):
    """Custom type p1BranchCurrentAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("p1BranchCurrentAlarmStatusHighHighLatching", 0),
          ("p1BranchCurrentAlarmStatusHighLatching", 1),
          ("p1BranchCurrentAlarmStatusLowLatching", 2),
          ("p1BranchCurrentAlarmStatusLowLowLatching", 3),
          ("p1BranchCurrentAlarmStatusAlarmOff", 4),
          ("p1BranchCurrentAlarmStatusHighNonLatching", 8),
          ("p1BranchCurrentAlarmStatusLowNonLatching", 9))
    )

_P1BranchCurrentAlarmStatus_Type.__name__ = "Bits"
_P1BranchCurrentAlarmStatus_Object = MibTableColumn
p1BranchCurrentAlarmStatus = _P1BranchCurrentAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 3),
    _P1BranchCurrentAlarmStatus_Type()
)
p1BranchCurrentAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchCurrentAlarmStatus.setStatus("current")
_P1BranchHighHighAlarmCount_Type = Counter32
_P1BranchHighHighAlarmCount_Object = MibTableColumn
p1BranchHighHighAlarmCount = _P1BranchHighHighAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 4),
    _P1BranchHighHighAlarmCount_Type()
)
p1BranchHighHighAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchHighHighAlarmCount.setStatus("current")
_P1BranchHighAlarmCount_Type = Counter32
_P1BranchHighAlarmCount_Object = MibTableColumn
p1BranchHighAlarmCount = _P1BranchHighAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 5),
    _P1BranchHighAlarmCount_Type()
)
p1BranchHighAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchHighAlarmCount.setStatus("current")
_P1BranchLowAlarmCount_Type = Counter32
_P1BranchLowAlarmCount_Object = MibTableColumn
p1BranchLowAlarmCount = _P1BranchLowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 6),
    _P1BranchLowAlarmCount_Type()
)
p1BranchLowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchLowAlarmCount.setStatus("current")
_P1BranchLowLowAlarmCount_Type = Counter32
_P1BranchLowLowAlarmCount_Object = MibTableColumn
p1BranchLowLowAlarmCount = _P1BranchLowLowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 7),
    _P1BranchLowLowAlarmCount_Type()
)
p1BranchLowLowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchLowLowAlarmCount.setStatus("current")
_P1BranchOffStateAlarmCount_Type = Counter32
_P1BranchOffStateAlarmCount_Object = MibTableColumn
p1BranchOffStateAlarmCount = _P1BranchOffStateAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 4, 1, 8),
    _P1BranchOffStateAlarmCount_Type()
)
p1BranchOffStateAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchOffStateAlarmCount.setStatus("current")
_P1VoltageInputs_ObjectIdentity = ObjectIdentity
p1VoltageInputs = _P1VoltageInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2)
)
_P1VoltageAverages_ObjectIdentity = ObjectIdentity
p1VoltageAverages = _P1VoltageAverages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 1)
)
_P1VoltsLineLine3PhaseAve_Type = ThousandthsInt32
_P1VoltsLineLine3PhaseAve_Object = MibScalar
p1VoltsLineLine3PhaseAve = _P1VoltsLineLine3PhaseAve_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 1, 1),
    _P1VoltsLineLine3PhaseAve_Type()
)
p1VoltsLineLine3PhaseAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1VoltsLineLine3PhaseAve.setStatus("current")
if mibBuilder.loadTexts:
    p1VoltsLineLine3PhaseAve.setUnits("V")
_P1VoltsLineNeutral3PhaseAve_Type = ThousandthsInt32
_P1VoltsLineNeutral3PhaseAve_Object = MibScalar
p1VoltsLineNeutral3PhaseAve = _P1VoltsLineNeutral3PhaseAve_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 1, 2),
    _P1VoltsLineNeutral3PhaseAve_Type()
)
p1VoltsLineNeutral3PhaseAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1VoltsLineNeutral3PhaseAve.setStatus("current")
if mibBuilder.loadTexts:
    p1VoltsLineNeutral3PhaseAve.setUnits("V")
_P1Frequency_Type = ThousandthsInt32
_P1Frequency_Object = MibScalar
p1Frequency = _P1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 1, 3),
    _P1Frequency_Type()
)
p1Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1Frequency.setStatus("current")
if mibBuilder.loadTexts:
    p1Frequency.setUnits("Hz")
_P1VoltagePhaseTable_Object = MibTable
p1VoltagePhaseTable = _P1VoltagePhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    p1VoltagePhaseTable.setStatus("current")
_P1VoltagePhaseEntry_Object = MibTableRow
p1VoltagePhaseEntry = _P1VoltagePhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 2, 1)
)
p1VoltagePhaseEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltagePhaseIndex"),
)
if mibBuilder.loadTexts:
    p1VoltagePhaseEntry.setStatus("current")


class _P1VoltagePhaseIndex_Type(Unsigned32):
    """Custom type p1VoltagePhaseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_P1VoltagePhaseIndex_Type.__name__ = "Unsigned32"
_P1VoltagePhaseIndex_Object = MibTableColumn
p1VoltagePhaseIndex = _P1VoltagePhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 2, 1, 1),
    _P1VoltagePhaseIndex_Type()
)
p1VoltagePhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1VoltagePhaseIndex.setStatus("current")
_P1VoltsLineToLine_Type = ThousandthsInt32
_P1VoltsLineToLine_Object = MibTableColumn
p1VoltsLineToLine = _P1VoltsLineToLine_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 2, 1, 2),
    _P1VoltsLineToLine_Type()
)
p1VoltsLineToLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1VoltsLineToLine.setStatus("current")
if mibBuilder.loadTexts:
    p1VoltsLineToLine.setUnits("V")
_P1VoltsLineToNeutral_Type = ThousandthsInt32
_P1VoltsLineToNeutral_Object = MibTableColumn
p1VoltsLineToNeutral = _P1VoltsLineToNeutral_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 2, 1, 3),
    _P1VoltsLineToNeutral_Type()
)
p1VoltsLineToNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1VoltsLineToNeutral.setStatus("current")
if mibBuilder.loadTexts:
    p1VoltsLineToNeutral.setUnits("V")
_P1VoltsPhaseAngle_Type = ThousandthsInt32
_P1VoltsPhaseAngle_Object = MibTableColumn
p1VoltsPhaseAngle = _P1VoltsPhaseAngle_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 2, 2, 1, 4),
    _P1VoltsPhaseAngle_Type()
)
p1VoltsPhaseAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1VoltsPhaseAngle.setStatus("current")
if mibBuilder.loadTexts:
    p1VoltsPhaseAngle.setUnits("V")
_P1AuxiliaryInputs_ObjectIdentity = ObjectIdentity
p1AuxiliaryInputs = _P1AuxiliaryInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3)
)
_P1Aux3PhaseTotals_ObjectIdentity = ObjectIdentity
p1Aux3PhaseTotals = _P1Aux3PhaseTotals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1)
)
_P1AuxTotalRealEnergy_Type = TenthsCounter64
_P1AuxTotalRealEnergy_Object = MibScalar
p1AuxTotalRealEnergy = _P1AuxTotalRealEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 1),
    _P1AuxTotalRealEnergy_Type()
)
p1AuxTotalRealEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxTotalRealEnergy.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxTotalRealEnergy.setUnits("Wh")
_P1AuxTotalRealPower_Type = Integer32
_P1AuxTotalRealPower_Object = MibScalar
p1AuxTotalRealPower = _P1AuxTotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 2),
    _P1AuxTotalRealPower_Type()
)
p1AuxTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxTotalRealPower.setUnits("W")
_P1AuxTotalApparentPower_Type = Integer32
_P1AuxTotalApparentPower_Object = MibScalar
p1AuxTotalApparentPower = _P1AuxTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 3),
    _P1AuxTotalApparentPower_Type()
)
p1AuxTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxTotalApparentPower.setUnits("VA")
_P1AuxAveragePowerFactor_Type = ThousandthsInt32
_P1AuxAveragePowerFactor_Object = MibScalar
p1AuxAveragePowerFactor = _P1AuxAveragePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 4),
    _P1AuxAveragePowerFactor_Type()
)
p1AuxAveragePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxAveragePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxAveragePowerFactor.setUnits("%")
_P1AuxAverageCurrent_Type = ThousandthsInt32
_P1AuxAverageCurrent_Object = MibScalar
p1AuxAverageCurrent = _P1AuxAverageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 5),
    _P1AuxAverageCurrent_Type()
)
p1AuxAverageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxAverageCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxAverageCurrent.setUnits("A")
_P1AuxPresentTotalRealPowerDemand_Type = Integer32
_P1AuxPresentTotalRealPowerDemand_Object = MibScalar
p1AuxPresentTotalRealPowerDemand = _P1AuxPresentTotalRealPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 6),
    _P1AuxPresentTotalRealPowerDemand_Type()
)
p1AuxPresentTotalRealPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxPresentTotalRealPowerDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxPresentTotalRealPowerDemand.setUnits("W")
_P1AuxTotalRealEnergySnapShot_Type = TenthsCounter64
_P1AuxTotalRealEnergySnapShot_Object = MibScalar
p1AuxTotalRealEnergySnapShot = _P1AuxTotalRealEnergySnapShot_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 7),
    _P1AuxTotalRealEnergySnapShot_Type()
)
p1AuxTotalRealEnergySnapShot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxTotalRealEnergySnapShot.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxTotalRealEnergySnapShot.setUnits("Wh")
_P1AuxMaximumTotalRealPowerDemand_Type = ThousandthsInt32
_P1AuxMaximumTotalRealPowerDemand_Object = MibScalar
p1AuxMaximumTotalRealPowerDemand = _P1AuxMaximumTotalRealPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 8),
    _P1AuxMaximumTotalRealPowerDemand_Type()
)
p1AuxMaximumTotalRealPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxMaximumTotalRealPowerDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxMaximumTotalRealPowerDemand.setUnits("A")
_P1AuxMaximumTotalRealPower_Type = ThousandthsInt32
_P1AuxMaximumTotalRealPower_Object = MibScalar
p1AuxMaximumTotalRealPower = _P1AuxMaximumTotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 9),
    _P1AuxMaximumTotalRealPower_Type()
)
p1AuxMaximumTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxMaximumTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxMaximumTotalRealPower.setUnits("A")


class _P1AuxReset_Type(Integer32):
    """Custom type p1AuxReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10203,
              29877)
        )
    )
    namedValues = NamedValues(
        *(("clearKWh", 10203),
          ("clearMaxCurrentKW", 29877))
    )


_P1AuxReset_Type.__name__ = "Integer32"
_P1AuxReset_Object = MibScalar
p1AuxReset = _P1AuxReset_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 1, 10),
    _P1AuxReset_Type()
)
p1AuxReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1AuxReset.setStatus("current")
_P1AuxPhaseTable_Object = MibTable
p1AuxPhaseTable = _P1AuxPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    p1AuxPhaseTable.setStatus("current")
_P1AuxPhaseEntry_Object = MibTableRow
p1AuxPhaseEntry = _P1AuxPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1)
)
p1AuxPhaseEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchNumberIndex"),
)
if mibBuilder.loadTexts:
    p1AuxPhaseEntry.setStatus("current")


class _P1AuxPhaseIndex_Type(Unsigned32):
    """Custom type p1AuxPhaseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_P1AuxPhaseIndex_Type.__name__ = "Unsigned32"
_P1AuxPhaseIndex_Object = MibTableColumn
p1AuxPhaseIndex = _P1AuxPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 1),
    _P1AuxPhaseIndex_Type()
)
p1AuxPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1AuxPhaseIndex.setStatus("current")
_P1AuxRealPower_Type = Integer32
_P1AuxRealPower_Object = MibTableColumn
p1AuxRealPower = _P1AuxRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 2),
    _P1AuxRealPower_Type()
)
p1AuxRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxRealPower.setUnits("W")
_P1AuxApparentPower_Type = Integer32
_P1AuxApparentPower_Object = MibTableColumn
p1AuxApparentPower = _P1AuxApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 3),
    _P1AuxApparentPower_Type()
)
p1AuxApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxApparentPower.setUnits("VA")
_P1AuxPowerFactor_Type = ThousandthsInt32
_P1AuxPowerFactor_Object = MibTableColumn
p1AuxPowerFactor = _P1AuxPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 4),
    _P1AuxPowerFactor_Type()
)
p1AuxPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxPowerFactor.setUnits("%")
_P1AuxCurrent_Type = ThousandthsInt32
_P1AuxCurrent_Object = MibTableColumn
p1AuxCurrent = _P1AuxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 5),
    _P1AuxCurrent_Type()
)
p1AuxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxCurrent.setUnits("A")
_P1AuxCurrentAngle_Type = ThousandthsInt32
_P1AuxCurrentAngle_Object = MibTableColumn
p1AuxCurrentAngle = _P1AuxCurrentAngle_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 6),
    _P1AuxCurrentAngle_Type()
)
p1AuxCurrentAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxCurrentAngle.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxCurrentAngle.setUnits("D")
_P1AuxPresentCurrentDemand_Type = ThousandthsInt32
_P1AuxPresentCurrentDemand_Object = MibTableColumn
p1AuxPresentCurrentDemand = _P1AuxPresentCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 7),
    _P1AuxPresentCurrentDemand_Type()
)
p1AuxPresentCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxPresentCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxPresentCurrentDemand.setUnits("A")
_P1AuxMaximumCurrentDemand_Type = ThousandthsInt32
_P1AuxMaximumCurrentDemand_Object = MibTableColumn
p1AuxMaximumCurrentDemand = _P1AuxMaximumCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 8),
    _P1AuxMaximumCurrentDemand_Type()
)
p1AuxMaximumCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxMaximumCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxMaximumCurrentDemand.setUnits("A")
_P1AuxMaximumCurrent_Type = ThousandthsInt32
_P1AuxMaximumCurrent_Object = MibTableColumn
p1AuxMaximumCurrent = _P1AuxMaximumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 3, 2, 1, 9),
    _P1AuxMaximumCurrent_Type()
)
p1AuxMaximumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1AuxMaximumCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxMaximumCurrent.setUnits("A")
_P1BranchInputs_ObjectIdentity = ObjectIdentity
p1BranchInputs = _P1BranchInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4)
)
_P1BranchTable_Object = MibTable
p1BranchTable = _P1BranchTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    p1BranchTable.setStatus("current")
_P1BranchEntry_Object = MibTableRow
p1BranchEntry = _P1BranchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1)
)
p1BranchEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchNumberIndex"),
)
if mibBuilder.loadTexts:
    p1BranchEntry.setStatus("current")


class _P1BranchNumberIndex_Type(Unsigned32):
    """Custom type p1BranchNumberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_P1BranchNumberIndex_Type.__name__ = "Unsigned32"
_P1BranchNumberIndex_Object = MibTableColumn
p1BranchNumberIndex = _P1BranchNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 1),
    _P1BranchNumberIndex_Type()
)
p1BranchNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1BranchNumberIndex.setStatus("current")
_P1BranchRealEnergy_Type = TenthsCounter64
_P1BranchRealEnergy_Object = MibTableColumn
p1BranchRealEnergy = _P1BranchRealEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 2),
    _P1BranchRealEnergy_Type()
)
p1BranchRealEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchRealEnergy.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchRealEnergy.setUnits("Wh")
_P1BranchRealPower_Type = Integer32
_P1BranchRealPower_Object = MibTableColumn
p1BranchRealPower = _P1BranchRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 3),
    _P1BranchRealPower_Type()
)
p1BranchRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchRealPower.setUnits("W")
_P1BranchApparentPower_Type = Integer32
_P1BranchApparentPower_Object = MibTableColumn
p1BranchApparentPower = _P1BranchApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 4),
    _P1BranchApparentPower_Type()
)
p1BranchApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchApparentPower.setUnits("VA")
_P1BranchPowerFactor_Type = ThousandthsInt32
_P1BranchPowerFactor_Object = MibTableColumn
p1BranchPowerFactor = _P1BranchPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 5),
    _P1BranchPowerFactor_Type()
)
p1BranchPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchPowerFactor.setUnits("%")
_P1BranchCurrent_Type = ThousandthsInt32
_P1BranchCurrent_Object = MibTableColumn
p1BranchCurrent = _P1BranchCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 6),
    _P1BranchCurrent_Type()
)
p1BranchCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchCurrent.setUnits("A")
_P1BranchCurrentAngle_Type = ThousandthsInt32
_P1BranchCurrentAngle_Object = MibTableColumn
p1BranchCurrentAngle = _P1BranchCurrentAngle_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 7),
    _P1BranchCurrentAngle_Type()
)
p1BranchCurrentAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchCurrentAngle.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchCurrentAngle.setUnits("D")
_P1BranchPresentCurrentDemand_Type = ThousandthsInt32
_P1BranchPresentCurrentDemand_Object = MibTableColumn
p1BranchPresentCurrentDemand = _P1BranchPresentCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 8),
    _P1BranchPresentCurrentDemand_Type()
)
p1BranchPresentCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchPresentCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchPresentCurrentDemand.setUnits("A")
_P1BranchPresentRealPowerDemand_Type = Integer32
_P1BranchPresentRealPowerDemand_Object = MibTableColumn
p1BranchPresentRealPowerDemand = _P1BranchPresentRealPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 9),
    _P1BranchPresentRealPowerDemand_Type()
)
p1BranchPresentRealPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchPresentRealPowerDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchPresentRealPowerDemand.setUnits("W")
_P1BranchMaximumCurrentDemand_Type = ThousandthsInt32
_P1BranchMaximumCurrentDemand_Object = MibTableColumn
p1BranchMaximumCurrentDemand = _P1BranchMaximumCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 10),
    _P1BranchMaximumCurrentDemand_Type()
)
p1BranchMaximumCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchMaximumCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchMaximumCurrentDemand.setUnits("A")
_P1BranchMaximumRealPowerDemand_Type = Integer32
_P1BranchMaximumRealPowerDemand_Object = MibTableColumn
p1BranchMaximumRealPowerDemand = _P1BranchMaximumRealPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 11),
    _P1BranchMaximumRealPowerDemand_Type()
)
p1BranchMaximumRealPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchMaximumRealPowerDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchMaximumRealPowerDemand.setUnits("W")
_P1BranchRealEnergySnapShot_Type = TenthsCounter64
_P1BranchRealEnergySnapShot_Object = MibTableColumn
p1BranchRealEnergySnapShot = _P1BranchRealEnergySnapShot_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 12),
    _P1BranchRealEnergySnapShot_Type()
)
p1BranchRealEnergySnapShot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchRealEnergySnapShot.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchRealEnergySnapShot.setUnits("Wh")
_P1BranchMaximumCurrent_Type = ThousandthsInt32
_P1BranchMaximumCurrent_Object = MibTableColumn
p1BranchMaximumCurrent = _P1BranchMaximumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 13),
    _P1BranchMaximumCurrent_Type()
)
p1BranchMaximumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchMaximumCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchMaximumCurrent.setUnits("A")
_P1BranchMaximumRealPower_Type = Integer32
_P1BranchMaximumRealPower_Object = MibTableColumn
p1BranchMaximumRealPower = _P1BranchMaximumRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 14),
    _P1BranchMaximumRealPower_Type()
)
p1BranchMaximumRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1BranchMaximumRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchMaximumRealPower.setUnits("W")


class _P1BranchReset_Type(Integer32):
    """Custom type p1BranchReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10203,
              29877)
        )
    )
    namedValues = NamedValues(
        *(("clearKWh", 10203),
          ("clearMaxCurrentKW", 29877))
    )


_P1BranchReset_Type.__name__ = "Integer32"
_P1BranchReset_Object = MibTableColumn
p1BranchReset = _P1BranchReset_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 4, 1, 1, 15),
    _P1BranchReset_Type()
)
p1BranchReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1BranchReset.setStatus("current")
_P1LogicalCircuits_ObjectIdentity = ObjectIdentity
p1LogicalCircuits = _P1LogicalCircuits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5)
)
_P1LogicalCircuitTable_Object = MibTable
p1LogicalCircuitTable = _P1LogicalCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    p1LogicalCircuitTable.setStatus("current")
_P1LogicalCircuitEntry_Object = MibTableRow
p1LogicalCircuitEntry = _P1LogicalCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1)
)
p1LogicalCircuitEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitIndex"),
)
if mibBuilder.loadTexts:
    p1LogicalCircuitEntry.setStatus("current")


class _P1LogicalCircuitIndex_Type(Unsigned32):
    """Custom type p1LogicalCircuitIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 46),
    )


_P1LogicalCircuitIndex_Type.__name__ = "Unsigned32"
_P1LogicalCircuitIndex_Object = MibTableColumn
p1LogicalCircuitIndex = _P1LogicalCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 1),
    _P1LogicalCircuitIndex_Type()
)
p1LogicalCircuitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1LogicalCircuitIndex.setStatus("current")
_P1LogicalCircuitRealEnergy_Type = TenthsCounter64
_P1LogicalCircuitRealEnergy_Object = MibTableColumn
p1LogicalCircuitRealEnergy = _P1LogicalCircuitRealEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 2),
    _P1LogicalCircuitRealEnergy_Type()
)
p1LogicalCircuitRealEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitRealEnergy.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitRealEnergy.setUnits("Wh")
_P1LogicalCircuitRealPower_Type = Integer32
_P1LogicalCircuitRealPower_Object = MibTableColumn
p1LogicalCircuitRealPower = _P1LogicalCircuitRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 3),
    _P1LogicalCircuitRealPower_Type()
)
p1LogicalCircuitRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitRealPower.setUnits("W")
_P1LogicalCircuitApparentPower_Type = Integer32
_P1LogicalCircuitApparentPower_Object = MibTableColumn
p1LogicalCircuitApparentPower = _P1LogicalCircuitApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 4),
    _P1LogicalCircuitApparentPower_Type()
)
p1LogicalCircuitApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitApparentPower.setUnits("VA")
_P1LogicalCircuitPowerFactor_Type = ThousandthsInt32
_P1LogicalCircuitPowerFactor_Object = MibTableColumn
p1LogicalCircuitPowerFactor = _P1LogicalCircuitPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 5),
    _P1LogicalCircuitPowerFactor_Type()
)
p1LogicalCircuitPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitPowerFactor.setUnits("%")
_P1LogicalCircuitCurrent_Type = ThousandthsInt32
_P1LogicalCircuitCurrent_Object = MibTableColumn
p1LogicalCircuitCurrent = _P1LogicalCircuitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 6),
    _P1LogicalCircuitCurrent_Type()
)
p1LogicalCircuitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitCurrent.setUnits("A")
_P1LogicalCircuitPresentRealPowerDemand_Type = Integer32
_P1LogicalCircuitPresentRealPowerDemand_Object = MibTableColumn
p1LogicalCircuitPresentRealPowerDemand = _P1LogicalCircuitPresentRealPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 7),
    _P1LogicalCircuitPresentRealPowerDemand_Type()
)
p1LogicalCircuitPresentRealPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitPresentRealPowerDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitPresentRealPowerDemand.setUnits("W")
_P1LogicalCircuitPresentCurrentDemand_Type = ThousandthsInt32
_P1LogicalCircuitPresentCurrentDemand_Object = MibTableColumn
p1LogicalCircuitPresentCurrentDemand = _P1LogicalCircuitPresentCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 8),
    _P1LogicalCircuitPresentCurrentDemand_Type()
)
p1LogicalCircuitPresentCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitPresentCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitPresentCurrentDemand.setUnits("A")
_P1LogicalCircuitMaximumRealPowerDemand_Type = Integer32
_P1LogicalCircuitMaximumRealPowerDemand_Object = MibTableColumn
p1LogicalCircuitMaximumRealPowerDemand = _P1LogicalCircuitMaximumRealPowerDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 9),
    _P1LogicalCircuitMaximumRealPowerDemand_Type()
)
p1LogicalCircuitMaximumRealPowerDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumRealPowerDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumRealPowerDemand.setUnits("W")
_P1LogicalCircuitMaximumCurrentDemand_Type = ThousandthsInt32
_P1LogicalCircuitMaximumCurrentDemand_Object = MibTableColumn
p1LogicalCircuitMaximumCurrentDemand = _P1LogicalCircuitMaximumCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 10),
    _P1LogicalCircuitMaximumCurrentDemand_Type()
)
p1LogicalCircuitMaximumCurrentDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumCurrentDemand.setUnits("A")
_P1LogicalCircuitMaximumRealPower_Type = Integer32
_P1LogicalCircuitMaximumRealPower_Object = MibTableColumn
p1LogicalCircuitMaximumRealPower = _P1LogicalCircuitMaximumRealPower_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 11),
    _P1LogicalCircuitMaximumRealPower_Type()
)
p1LogicalCircuitMaximumRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumRealPower.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumRealPower.setUnits("W")
_P1LogicalCircuitMaximumCurrent_Type = ThousandthsInt32
_P1LogicalCircuitMaximumCurrent_Object = MibTableColumn
p1LogicalCircuitMaximumCurrent = _P1LogicalCircuitMaximumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 12),
    _P1LogicalCircuitMaximumCurrent_Type()
)
p1LogicalCircuitMaximumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumCurrent.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitMaximumCurrent.setUnits("A")
_P1LogicalCircuitSnapshotRealEnergy_Type = TenthsCounter64
_P1LogicalCircuitSnapshotRealEnergy_Object = MibTableColumn
p1LogicalCircuitSnapshotRealEnergy = _P1LogicalCircuitSnapshotRealEnergy_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 13),
    _P1LogicalCircuitSnapshotRealEnergy_Type()
)
p1LogicalCircuitSnapshotRealEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitSnapshotRealEnergy.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitSnapshotRealEnergy.setUnits("Wh")
_P1LogicalCircuitLineLineVoltage_Type = ThousandthsInt32
_P1LogicalCircuitLineLineVoltage_Object = MibTableColumn
p1LogicalCircuitLineLineVoltage = _P1LogicalCircuitLineLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 14),
    _P1LogicalCircuitLineLineVoltage_Type()
)
p1LogicalCircuitLineLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitLineLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitLineLineVoltage.setUnits("V")
_P1LogicalCircuitLineNeutralVoltage_Type = ThousandthsInt32
_P1LogicalCircuitLineNeutralVoltage_Object = MibTableColumn
p1LogicalCircuitLineNeutralVoltage = _P1LogicalCircuitLineNeutralVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 15),
    _P1LogicalCircuitLineNeutralVoltage_Type()
)
p1LogicalCircuitLineNeutralVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitLineNeutralVoltage.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitLineNeutralVoltage.setUnits("V")
_P1LogicalCircuitFrequency_Type = ThousandthsInt32
_P1LogicalCircuitFrequency_Object = MibTableColumn
p1LogicalCircuitFrequency = _P1LogicalCircuitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 16),
    _P1LogicalCircuitFrequency_Type()
)
p1LogicalCircuitFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitFrequency.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitFrequency.setUnits("Hz")


class _P1LogicalCircuitLatchingAlarm_Type(Bits):
    """Custom type p1LogicalCircuitLatchingAlarm based on Bits"""
    namedValues = NamedValues(
        *(("p1LogicalCircuitLatchingAlarmHighHighCurrent", 0),
          ("p1LogicalCircuitLatchingAlarmHighCurrent", 1),
          ("p1LogicalCircuitLatchingAlarmLowCurrent", 2),
          ("p1LogicalCircuitLatchingAlarmLowLowCurrent", 3),
          ("p1LogicalCircuitLatchingAlarmAlarmOff", 4),
          ("p1LogicalCircuitLatchingAlarmHighVolt", 8),
          ("p1LogicalCircuitLatchingAlarmLowVolt", 9))
    )

_P1LogicalCircuitLatchingAlarm_Type.__name__ = "Bits"
_P1LogicalCircuitLatchingAlarm_Object = MibTableColumn
p1LogicalCircuitLatchingAlarm = _P1LogicalCircuitLatchingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 17),
    _P1LogicalCircuitLatchingAlarm_Type()
)
p1LogicalCircuitLatchingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitLatchingAlarm.setStatus("current")


class _P1LogicalCircuitNonLatchingAlarm_Type(Bits):
    """Custom type p1LogicalCircuitNonLatchingAlarm based on Bits"""
    namedValues = NamedValues(
        *(("p1LogicalCircuitNonLatchingAlarmHighCurrent", 0),
          ("p1LogicalCircuitNonLatchingAlarmLowCurrent", 1),
          ("p1LogicalCircuitNonLatchingAlarmHighVolt", 8),
          ("p1LogicalCircuitNonLatchingAlarmLowVolt", 9))
    )

_P1LogicalCircuitNonLatchingAlarm_Type.__name__ = "Bits"
_P1LogicalCircuitNonLatchingAlarm_Object = MibTableColumn
p1LogicalCircuitNonLatchingAlarm = _P1LogicalCircuitNonLatchingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 18),
    _P1LogicalCircuitNonLatchingAlarm_Type()
)
p1LogicalCircuitNonLatchingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitNonLatchingAlarm.setStatus("current")


class _P1LogicalCircuitReset_Type(Integer32):
    """Custom type p1LogicalCircuitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10203,
              20097,
              26012,
              26013,
              29877,
              31010)
        )
    )
    namedValues = NamedValues(
        *(("clearKWh", 10203),
          ("clearMaxDemand", 20097),
          ("beginDemandSubInt", 26012),
          ("resetDemand", 26013),
          ("clearMaxCurrentKW", 29877),
          ("resetLatchingAlarms", 31010))
    )


_P1LogicalCircuitReset_Type.__name__ = "Integer32"
_P1LogicalCircuitReset_Object = MibTableColumn
p1LogicalCircuitReset = _P1LogicalCircuitReset_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 19),
    _P1LogicalCircuitReset_Type()
)
p1LogicalCircuitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LogicalCircuitReset.setStatus("current")
_P1LogicalCircuitBranchAssignment1_Type = Unsigned32
_P1LogicalCircuitBranchAssignment1_Object = MibTableColumn
p1LogicalCircuitBranchAssignment1 = _P1LogicalCircuitBranchAssignment1_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 20),
    _P1LogicalCircuitBranchAssignment1_Type()
)
p1LogicalCircuitBranchAssignment1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitBranchAssignment1.setStatus("current")
_P1LogicalCircuitBranchAssignment2_Type = Unsigned32
_P1LogicalCircuitBranchAssignment2_Object = MibTableColumn
p1LogicalCircuitBranchAssignment2 = _P1LogicalCircuitBranchAssignment2_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 21),
    _P1LogicalCircuitBranchAssignment2_Type()
)
p1LogicalCircuitBranchAssignment2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitBranchAssignment2.setStatus("current")
_P1LogicalCircuitBranchAssignment3_Type = Unsigned32
_P1LogicalCircuitBranchAssignment3_Object = MibTableColumn
p1LogicalCircuitBranchAssignment3 = _P1LogicalCircuitBranchAssignment3_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 22),
    _P1LogicalCircuitBranchAssignment3_Type()
)
p1LogicalCircuitBranchAssignment3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitBranchAssignment3.setStatus("current")
_P1LogicalCircuitCtSize_Type = Unsigned32
_P1LogicalCircuitCtSize_Object = MibTableColumn
p1LogicalCircuitCtSize = _P1LogicalCircuitCtSize_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 23),
    _P1LogicalCircuitCtSize_Type()
)
p1LogicalCircuitCtSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitCtSize.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitCtSize.setUnits("A")
_P1LogicalCircuitBreakerSize_Type = Unsigned32
_P1LogicalCircuitBreakerSize_Object = MibTableColumn
p1LogicalCircuitBreakerSize = _P1LogicalCircuitBreakerSize_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 5, 1, 1, 24),
    _P1LogicalCircuitBreakerSize_Type()
)
p1LogicalCircuitBreakerSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1LogicalCircuitBreakerSize.setStatus("current")
if mibBuilder.loadTexts:
    p1LogicalCircuitBreakerSize.setUnits("A")
_P1Configuration_ObjectIdentity = ObjectIdentity
p1Configuration = _P1Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6)
)
_P1ProductInformation_ObjectIdentity = ObjectIdentity
p1ProductInformation = _P1ProductInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 1)
)
_P1SerialNumber_Type = Unsigned32
_P1SerialNumber_Object = MibScalar
p1SerialNumber = _P1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 1, 1),
    _P1SerialNumber_Type()
)
p1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1SerialNumber.setStatus("current")
_P1FirmwareRevision_Type = Unsigned32
_P1FirmwareRevision_Object = MibScalar
p1FirmwareRevision = _P1FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 1, 2),
    _P1FirmwareRevision_Type()
)
p1FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1FirmwareRevision.setStatus("current")


class _P1DeviceID_Type(Integer32):
    """Custom type p1DeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15170,
              15171,
              15172)
        )
    )
    namedValues = NamedValues(
        *(("e30modelC", 15170),
          ("e30modelB", 15171),
          ("e30modelA", 15172))
    )


_P1DeviceID_Type.__name__ = "Integer32"
_P1DeviceID_Object = MibScalar
p1DeviceID = _P1DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 1, 3),
    _P1DeviceID_Type()
)
p1DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1DeviceID.setStatus("current")


class _P1ProductID_Type(Bits):
    """Custom type p1ProductID based on Bits"""
    namedValues = NamedValues(
        *(("p1ProductIDSolidCore", 0),
          ("p1ProductIDSplitCore", 1))
    )

_P1ProductID_Type.__name__ = "Bits"
_P1ProductID_Object = MibScalar
p1ProductID = _P1ProductID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 1, 4),
    _P1ProductID_Type()
)
p1ProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1ProductID.setStatus("current")


class _P1LocationString_Type(DisplayString):
    """Custom type p1LocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_P1LocationString_Type.__name__ = "DisplayString"
_P1LocationString_Object = MibScalar
p1LocationString = _P1LocationString_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 1, 5),
    _P1LocationString_Type()
)
p1LocationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LocationString.setStatus("current")


class _P1GlobalResets_Type(Integer32):
    """Custom type p1GlobalResets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10203,
              20097,
              26012,
              26013,
              29877,
              31010)
        )
    )
    namedValues = NamedValues(
        *(("clearAllKWh", 10203),
          ("clearAllMaxDemand", 20097),
          ("beginNewDemandSubInt", 26012),
          ("resetDemand", 26013),
          ("clearAllMaxCurrentKW", 29877),
          ("resetAllLatchingAlarms", 31010))
    )


_P1GlobalResets_Type.__name__ = "Integer32"
_P1GlobalResets_Object = MibScalar
p1GlobalResets = _P1GlobalResets_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 2),
    _P1GlobalResets_Type()
)
p1GlobalResets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1GlobalResets.setStatus("current")
_P1Setup_ObjectIdentity = ObjectIdentity
p1Setup = _P1Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 3)
)


class _P1PanelConfiguration_Type(Integer32):
    """Custom type p1PanelConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p1PanelConfigurationTopFeedDoubleRow", 0),
          ("p1PanelConfigurationBottomFeedDoubleRow", 1),
          ("p1PanelConfigurationSingleRowSequential", 2),
          ("p1PanelConfigurationSingleRowOddEven", 3))
    )


_P1PanelConfiguration_Type.__name__ = "Integer32"
_P1PanelConfiguration_Object = MibScalar
p1PanelConfiguration = _P1PanelConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 3, 1),
    _P1PanelConfiguration_Type()
)
p1PanelConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1PanelConfiguration.setStatus("current")


class _P1NumSubIntervalsPerDemandInterval_Type(Unsigned32):
    """Custom type p1NumSubIntervalsPerDemandInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_P1NumSubIntervalsPerDemandInterval_Type.__name__ = "Unsigned32"
_P1NumSubIntervalsPerDemandInterval_Object = MibScalar
p1NumSubIntervalsPerDemandInterval = _P1NumSubIntervalsPerDemandInterval_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 3, 2),
    _P1NumSubIntervalsPerDemandInterval_Type()
)
p1NumSubIntervalsPerDemandInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1NumSubIntervalsPerDemandInterval.setStatus("current")


class _P1SubIntervalSeconds_Type(Unsigned32):
    """Custom type p1SubIntervalSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1SubIntervalSeconds_Type.__name__ = "Unsigned32"
_P1SubIntervalSeconds_Object = MibScalar
p1SubIntervalSeconds = _P1SubIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 3, 3),
    _P1SubIntervalSeconds_Type()
)
p1SubIntervalSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1SubIntervalSeconds.setStatus("current")


class _P1UserDefinedSettings_Type(Bits):
    """Custom type p1UserDefinedSettings based on Bits"""
    namedValues = NamedValues(
        *(("p1EnableUserCTtoVoltagePhaseAssignment", 0),
          ("p1CurrentAngleVoltagePhaseRelative", 1),
          ("p1EnableSignedPower", 2),
          ("p1EnableSignedPowerFactor", 3),
          ("p1EnableLogicalCircuitsByTypeArrays", 4),
          ("p1DisablePanel2", 5),
          ("p1EnableVector2PhaseVAandPFcalc", 6),
          ("p1EnableRTCDemandSync", 7))
    )

_P1UserDefinedSettings_Type.__name__ = "Bits"
_P1UserDefinedSettings_Object = MibScalar
p1UserDefinedSettings = _P1UserDefinedSettings_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 3, 4),
    _P1UserDefinedSettings_Type()
)
p1UserDefinedSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1UserDefinedSettings.setStatus("current")
_P1AuxConfiguratonTable_Object = MibTable
p1AuxConfiguratonTable = _P1AuxConfiguratonTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    p1AuxConfiguratonTable.setStatus("current")
_P1AuxConfiguratonEntry_Object = MibTableRow
p1AuxConfiguratonEntry = _P1AuxConfiguratonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4, 1)
)
p1AuxConfiguratonEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxConfiguratonIndex"),
)
if mibBuilder.loadTexts:
    p1AuxConfiguratonEntry.setStatus("current")


class _P1AuxConfiguratonIndex_Type(Unsigned32):
    """Custom type p1AuxConfiguratonIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_P1AuxConfiguratonIndex_Type.__name__ = "Unsigned32"
_P1AuxConfiguratonIndex_Object = MibTableColumn
p1AuxConfiguratonIndex = _P1AuxConfiguratonIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4, 1, 1),
    _P1AuxConfiguratonIndex_Type()
)
p1AuxConfiguratonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1AuxConfiguratonIndex.setStatus("current")


class _P1AuxCTSize_Type(Unsigned32):
    """Custom type p1AuxCTSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1AuxCTSize_Type.__name__ = "Unsigned32"
_P1AuxCTSize_Object = MibTableColumn
p1AuxCTSize = _P1AuxCTSize_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4, 1, 2),
    _P1AuxCTSize_Type()
)
p1AuxCTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1AuxCTSize.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxCTSize.setUnits("A")


class _P1AuxBreakerSize_Type(Unsigned32):
    """Custom type p1AuxBreakerSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1AuxBreakerSize_Type.__name__ = "Unsigned32"
_P1AuxBreakerSize_Object = MibTableColumn
p1AuxBreakerSize = _P1AuxBreakerSize_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4, 1, 3),
    _P1AuxBreakerSize_Type()
)
p1AuxBreakerSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1AuxBreakerSize.setStatus("current")
if mibBuilder.loadTexts:
    p1AuxBreakerSize.setUnits("A")


class _P1AuxToVoltagePhaseAssignment_Type(Unsigned32):
    """Custom type p1AuxToVoltagePhaseAssignment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_P1AuxToVoltagePhaseAssignment_Type.__name__ = "Unsigned32"
_P1AuxToVoltagePhaseAssignment_Object = MibTableColumn
p1AuxToVoltagePhaseAssignment = _P1AuxToVoltagePhaseAssignment_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4, 1, 4),
    _P1AuxToVoltagePhaseAssignment_Type()
)
p1AuxToVoltagePhaseAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1AuxToVoltagePhaseAssignment.setStatus("current")


class _P1AuxToCircuitAssignment_Type(Unsigned32):
    """Custom type p1AuxToCircuitAssignment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 46),
    )


_P1AuxToCircuitAssignment_Type.__name__ = "Unsigned32"
_P1AuxToCircuitAssignment_Object = MibTableColumn
p1AuxToCircuitAssignment = _P1AuxToCircuitAssignment_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 4, 1, 5),
    _P1AuxToCircuitAssignment_Type()
)
p1AuxToCircuitAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1AuxToCircuitAssignment.setStatus("current")
_P1BranchConfiguratonTable_Object = MibTable
p1BranchConfiguratonTable = _P1BranchConfiguratonTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    p1BranchConfiguratonTable.setStatus("current")
_P1BranchConfiguratonEntry_Object = MibTableRow
p1BranchConfiguratonEntry = _P1BranchConfiguratonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5, 1)
)
p1BranchConfiguratonEntry.setIndexNames(
    (0, "SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchConfiguratonIndex"),
)
if mibBuilder.loadTexts:
    p1BranchConfiguratonEntry.setStatus("current")


class _P1BranchConfiguratonIndex_Type(Unsigned32):
    """Custom type p1BranchConfiguratonIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_P1BranchConfiguratonIndex_Type.__name__ = "Unsigned32"
_P1BranchConfiguratonIndex_Object = MibTableColumn
p1BranchConfiguratonIndex = _P1BranchConfiguratonIndex_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5, 1, 1),
    _P1BranchConfiguratonIndex_Type()
)
p1BranchConfiguratonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p1BranchConfiguratonIndex.setStatus("current")


class _P1BranchCTSize_Type(Unsigned32):
    """Custom type p1BranchCTSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1BranchCTSize_Type.__name__ = "Unsigned32"
_P1BranchCTSize_Object = MibTableColumn
p1BranchCTSize = _P1BranchCTSize_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5, 1, 2),
    _P1BranchCTSize_Type()
)
p1BranchCTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1BranchCTSize.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchCTSize.setUnits("A")


class _P1BranchBreakerSize_Type(Unsigned32):
    """Custom type p1BranchBreakerSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1BranchBreakerSize_Type.__name__ = "Unsigned32"
_P1BranchBreakerSize_Object = MibTableColumn
p1BranchBreakerSize = _P1BranchBreakerSize_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5, 1, 3),
    _P1BranchBreakerSize_Type()
)
p1BranchBreakerSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1BranchBreakerSize.setStatus("current")
if mibBuilder.loadTexts:
    p1BranchBreakerSize.setUnits("A")


class _P1BranchToVoltagePhaseAssignment_Type(Unsigned32):
    """Custom type p1BranchToVoltagePhaseAssignment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_P1BranchToVoltagePhaseAssignment_Type.__name__ = "Unsigned32"
_P1BranchToVoltagePhaseAssignment_Object = MibTableColumn
p1BranchToVoltagePhaseAssignment = _P1BranchToVoltagePhaseAssignment_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5, 1, 4),
    _P1BranchToVoltagePhaseAssignment_Type()
)
p1BranchToVoltagePhaseAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1BranchToVoltagePhaseAssignment.setStatus("current")


class _P1BranchToCircuitAssignment_Type(Unsigned32):
    """Custom type p1BranchToCircuitAssignment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 42),
    )


_P1BranchToCircuitAssignment_Type.__name__ = "Unsigned32"
_P1BranchToCircuitAssignment_Object = MibTableColumn
p1BranchToCircuitAssignment = _P1BranchToCircuitAssignment_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 5, 1, 5),
    _P1BranchToCircuitAssignment_Type()
)
p1BranchToCircuitAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1BranchToCircuitAssignment.setStatus("current")
_P1AlarmConfiguration_ObjectIdentity = ObjectIdentity
p1AlarmConfiguration = _P1AlarmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6)
)
_P1AlarmTimeDelays_ObjectIdentity = ObjectIdentity
p1AlarmTimeDelays = _P1AlarmTimeDelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1)
)


class _P1OverVoltageTimeDelay_Type(Unsigned32):
    """Custom type p1OverVoltageTimeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1OverVoltageTimeDelay_Type.__name__ = "Unsigned32"
_P1OverVoltageTimeDelay_Object = MibScalar
p1OverVoltageTimeDelay = _P1OverVoltageTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 1),
    _P1OverVoltageTimeDelay_Type()
)
p1OverVoltageTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1OverVoltageTimeDelay.setStatus("current")
if mibBuilder.loadTexts:
    p1OverVoltageTimeDelay.setUnits("S")


class _P1UnderVoltageTimeDelay_Type(Unsigned32):
    """Custom type p1UnderVoltageTimeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1UnderVoltageTimeDelay_Type.__name__ = "Unsigned32"
_P1UnderVoltageTimeDelay_Object = MibScalar
p1UnderVoltageTimeDelay = _P1UnderVoltageTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 2),
    _P1UnderVoltageTimeDelay_Type()
)
p1UnderVoltageTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1UnderVoltageTimeDelay.setStatus("current")
if mibBuilder.loadTexts:
    p1UnderVoltageTimeDelay.setUnits("S")


class _P1HighHighLatchingAlarmTimeDelay_Type(Unsigned32):
    """Custom type p1HighHighLatchingAlarmTimeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1HighHighLatchingAlarmTimeDelay_Type.__name__ = "Unsigned32"
_P1HighHighLatchingAlarmTimeDelay_Object = MibScalar
p1HighHighLatchingAlarmTimeDelay = _P1HighHighLatchingAlarmTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 3),
    _P1HighHighLatchingAlarmTimeDelay_Type()
)
p1HighHighLatchingAlarmTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1HighHighLatchingAlarmTimeDelay.setStatus("current")
if mibBuilder.loadTexts:
    p1HighHighLatchingAlarmTimeDelay.setUnits("S")


class _P1HighLatchingAlarmTimeDelay_Type(Unsigned32):
    """Custom type p1HighLatchingAlarmTimeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1HighLatchingAlarmTimeDelay_Type.__name__ = "Unsigned32"
_P1HighLatchingAlarmTimeDelay_Object = MibScalar
p1HighLatchingAlarmTimeDelay = _P1HighLatchingAlarmTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 4),
    _P1HighLatchingAlarmTimeDelay_Type()
)
p1HighLatchingAlarmTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1HighLatchingAlarmTimeDelay.setStatus("current")
if mibBuilder.loadTexts:
    p1HighLatchingAlarmTimeDelay.setUnits("S")


class _P1LowLatchingAlarmTimeDelay_Type(Unsigned32):
    """Custom type p1LowLatchingAlarmTimeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1LowLatchingAlarmTimeDelay_Type.__name__ = "Unsigned32"
_P1LowLatchingAlarmTimeDelay_Object = MibScalar
p1LowLatchingAlarmTimeDelay = _P1LowLatchingAlarmTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 5),
    _P1LowLatchingAlarmTimeDelay_Type()
)
p1LowLatchingAlarmTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LowLatchingAlarmTimeDelay.setStatus("current")
if mibBuilder.loadTexts:
    p1LowLatchingAlarmTimeDelay.setUnits("S")


class _P1LowLowLatchingAlarmTimeDelay_Type(Unsigned32):
    """Custom type p1LowLowLatchingAlarmTimeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1LowLowLatchingAlarmTimeDelay_Type.__name__ = "Unsigned32"
_P1LowLowLatchingAlarmTimeDelay_Object = MibScalar
p1LowLowLatchingAlarmTimeDelay = _P1LowLowLatchingAlarmTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 6),
    _P1LowLowLatchingAlarmTimeDelay_Type()
)
p1LowLowLatchingAlarmTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LowLowLatchingAlarmTimeDelay.setStatus("current")
if mibBuilder.loadTexts:
    p1LowLowLatchingAlarmTimeDelay.setUnits("S")


class _P1LatchingAlarmOnTime_Type(Unsigned32):
    """Custom type p1LatchingAlarmOnTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1LatchingAlarmOnTime_Type.__name__ = "Unsigned32"
_P1LatchingAlarmOnTime_Object = MibScalar
p1LatchingAlarmOnTime = _P1LatchingAlarmOnTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 7),
    _P1LatchingAlarmOnTime_Type()
)
p1LatchingAlarmOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LatchingAlarmOnTime.setStatus("current")
if mibBuilder.loadTexts:
    p1LatchingAlarmOnTime.setUnits("S")


class _P1LatchingAlarmOffTime_Type(Unsigned32):
    """Custom type p1LatchingAlarmOffTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1LatchingAlarmOffTime_Type.__name__ = "Unsigned32"
_P1LatchingAlarmOffTime_Object = MibScalar
p1LatchingAlarmOffTime = _P1LatchingAlarmOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 1, 8),
    _P1LatchingAlarmOffTime_Type()
)
p1LatchingAlarmOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LatchingAlarmOffTime.setStatus("current")
if mibBuilder.loadTexts:
    p1LatchingAlarmOffTime.setUnits("S")
_P1AlarmThresholds_ObjectIdentity = ObjectIdentity
p1AlarmThresholds = _P1AlarmThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2)
)


class _P1OverVoltageThreshold_Type(Unsigned32):
    """Custom type p1OverVoltageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1OverVoltageThreshold_Type.__name__ = "Unsigned32"
_P1OverVoltageThreshold_Object = MibScalar
p1OverVoltageThreshold = _P1OverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 1),
    _P1OverVoltageThreshold_Type()
)
p1OverVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1OverVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1OverVoltageThreshold.setUnits("V")


class _P1UnderVoltageThreshold_Type(Unsigned32):
    """Custom type p1UnderVoltageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_P1UnderVoltageThreshold_Type.__name__ = "Unsigned32"
_P1UnderVoltageThreshold_Object = MibScalar
p1UnderVoltageThreshold = _P1UnderVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 2),
    _P1UnderVoltageThreshold_Type()
)
p1UnderVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1UnderVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1UnderVoltageThreshold.setUnits("V")
_P1VoltageHysteresisThreshold_Type = TenthsInt32
_P1VoltageHysteresisThreshold_Object = MibScalar
p1VoltageHysteresisThreshold = _P1VoltageHysteresisThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 3),
    _P1VoltageHysteresisThreshold_Type()
)
p1VoltageHysteresisThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1VoltageHysteresisThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1VoltageHysteresisThreshold.setUnits("%")
_P1HighHighLatchingAlarmThreshold_Type = TenthsInt32
_P1HighHighLatchingAlarmThreshold_Object = MibScalar
p1HighHighLatchingAlarmThreshold = _P1HighHighLatchingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 4),
    _P1HighHighLatchingAlarmThreshold_Type()
)
p1HighHighLatchingAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1HighHighLatchingAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1HighHighLatchingAlarmThreshold.setUnits("%")
_P1HighLatchingAlarmThreshold_Type = TenthsInt32
_P1HighLatchingAlarmThreshold_Object = MibScalar
p1HighLatchingAlarmThreshold = _P1HighLatchingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 5),
    _P1HighLatchingAlarmThreshold_Type()
)
p1HighLatchingAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1HighLatchingAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1HighLatchingAlarmThreshold.setUnits("%")
_P1LowLatchingAlarmThreshold_Type = TenthsInt32
_P1LowLatchingAlarmThreshold_Object = MibScalar
p1LowLatchingAlarmThreshold = _P1LowLatchingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 6),
    _P1LowLatchingAlarmThreshold_Type()
)
p1LowLatchingAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LowLatchingAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1LowLatchingAlarmThreshold.setUnits("%")
_P1LowLowLatchingAlarmThreshold_Type = TenthsInt32
_P1LowLowLatchingAlarmThreshold_Object = MibScalar
p1LowLowLatchingAlarmThreshold = _P1LowLowLatchingAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 7),
    _P1LowLowLatchingAlarmThreshold_Type()
)
p1LowLowLatchingAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1LowLowLatchingAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1LowLowLatchingAlarmThreshold.setUnits("%")
_P1NonLatchingHighThreshold_Type = TenthsInt32
_P1NonLatchingHighThreshold_Object = MibScalar
p1NonLatchingHighThreshold = _P1NonLatchingHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 8),
    _P1NonLatchingHighThreshold_Type()
)
p1NonLatchingHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1NonLatchingHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1NonLatchingHighThreshold.setUnits("%")
_P1NonLatchingLowThreshold_Type = TenthsInt32
_P1NonLatchingLowThreshold_Object = MibScalar
p1NonLatchingLowThreshold = _P1NonLatchingLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 9),
    _P1NonLatchingLowThreshold_Type()
)
p1NonLatchingLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1NonLatchingLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1NonLatchingLowThreshold.setUnits("%")
_P1NonLatchingHysteresisThreshold_Type = TenthsInt32
_P1NonLatchingHysteresisThreshold_Object = MibScalar
p1NonLatchingHysteresisThreshold = _P1NonLatchingHysteresisThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 6, 2, 10),
    _P1NonLatchingHysteresisThreshold_Type()
)
p1NonLatchingHysteresisThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1NonLatchingHysteresisThreshold.setStatus("current")
if mibBuilder.loadTexts:
    p1NonLatchingHysteresisThreshold.setUnits("%")
_P1RealTimeClock_ObjectIdentity = ObjectIdentity
p1RealTimeClock = _P1RealTimeClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7)
)
_P1PresentTime_ObjectIdentity = ObjectIdentity
p1PresentTime = _P1PresentTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 1)
)
_P1PresentYear_Type = Unsigned32
_P1PresentYear_Object = MibScalar
p1PresentYear = _P1PresentYear_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 1, 1),
    _P1PresentYear_Type()
)
p1PresentYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1PresentYear.setStatus("current")
_P1PresentDayMonth_Type = Unsigned32
_P1PresentDayMonth_Object = MibScalar
p1PresentDayMonth = _P1PresentDayMonth_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 1, 2),
    _P1PresentDayMonth_Type()
)
p1PresentDayMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1PresentDayMonth.setStatus("current")
_P1PresentHourMinute_Type = Unsigned32
_P1PresentHourMinute_Object = MibScalar
p1PresentHourMinute = _P1PresentHourMinute_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 1, 3),
    _P1PresentHourMinute_Type()
)
p1PresentHourMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1PresentHourMinute.setStatus("current")
_P1PresentMilliSeconds_Type = Unsigned32
_P1PresentMilliSeconds_Object = MibScalar
p1PresentMilliSeconds = _P1PresentMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 1, 4),
    _P1PresentMilliSeconds_Type()
)
p1PresentMilliSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p1PresentMilliSeconds.setStatus("current")
_P1SnapShotTime_ObjectIdentity = ObjectIdentity
p1SnapShotTime = _P1SnapShotTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 2)
)
_P1SnapShotYear_Type = Unsigned32
_P1SnapShotYear_Object = MibScalar
p1SnapShotYear = _P1SnapShotYear_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 2, 1),
    _P1SnapShotYear_Type()
)
p1SnapShotYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1SnapShotYear.setStatus("current")
_P1SnapShotDayMonth_Type = Unsigned32
_P1SnapShotDayMonth_Object = MibScalar
p1SnapShotDayMonth = _P1SnapShotDayMonth_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 2, 2),
    _P1SnapShotDayMonth_Type()
)
p1SnapShotDayMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1SnapShotDayMonth.setStatus("current")
_P1SnapShotHourMinute_Type = Unsigned32
_P1SnapShotHourMinute_Object = MibScalar
p1SnapShotHourMinute = _P1SnapShotHourMinute_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 2, 3),
    _P1SnapShotHourMinute_Type()
)
p1SnapShotHourMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1SnapShotHourMinute.setStatus("current")
_P1SnapShotMilliSeconds_Type = Unsigned32
_P1SnapShotMilliSeconds_Object = MibScalar
p1SnapShotMilliSeconds = _P1SnapShotMilliSeconds_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 6, 7, 2, 4),
    _P1SnapShotMilliSeconds_Type()
)
p1SnapShotMilliSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1SnapShotMilliSeconds.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2)
)
_P1ConformanceGroups_ObjectIdentity = ObjectIdentity
p1ConformanceGroups = _P1ConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1)
)

# Managed Objects groups

p1AlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 2)
)
p1AlarmGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalLatchingAlarmStatus"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalNonLatchingAlarmStatus"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalMostRecentLatchingChannel"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalMostRecentNonLatchingChannel"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1TotalLatchingChannelsInAlarm"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1TotalNonLatchingChannelsInAlarm"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1DeviceHealth"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalHighHighLatchingAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalHighLatchingAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalLowLatchingAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalLowLowLatchingAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalOffStateLatchingAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1PowerUpCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxAlarmPhase"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltagePhaseAlarmStatus"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxCurrentAlarmStatus"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxHighHighAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxHighAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxLowAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxLowLowAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxOffStateAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchAlarmNumber"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchCurrentAlarmStatus"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchHighHighAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchHighAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchLowAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchLowLowAlarmCount"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchOffStateAlarmCount"))
)
if mibBuilder.loadTexts:
    p1AlarmGroup.setStatus("current")

p1VoltageInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 3)
)
p1VoltageInputGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltsLineLine3PhaseAve"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltsLineNeutral3PhaseAve"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1Frequency"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltsLineToLine"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltsLineToNeutral"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltsPhaseAngle"))
)
if mibBuilder.loadTexts:
    p1VoltageInputGroup.setStatus("current")

p1AuxiliaryInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 4)
)
p1AuxiliaryInputGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxTotalRealEnergy"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxTotalRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxTotalApparentPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxAveragePowerFactor"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxAverageCurrent"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxPresentTotalRealPowerDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxTotalRealEnergySnapShot"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxMaximumTotalRealPowerDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxMaximumTotalRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxReset"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxApparentPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxPowerFactor"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxCurrent"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxCurrentAngle"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxPresentCurrentDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxMaximumCurrentDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxMaximumCurrent"))
)
if mibBuilder.loadTexts:
    p1AuxiliaryInputGroup.setStatus("current")

p1BranchInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 5)
)
p1BranchInputGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchRealEnergy"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchApparentPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchPowerFactor"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchCurrent"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchCurrentAngle"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchPresentCurrentDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchPresentRealPowerDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchMaximumCurrentDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchMaximumRealPowerDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchRealEnergySnapShot"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchMaximumCurrent"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchMaximumRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchReset"))
)
if mibBuilder.loadTexts:
    p1BranchInputGroup.setStatus("current")

p1LogicalCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 6)
)
p1LogicalCircuitGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitRealEnergy"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitApparentPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitPowerFactor"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitCurrent"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitPresentRealPowerDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitPresentCurrentDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitMaximumRealPowerDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitMaximumCurrentDemand"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitMaximumRealPower"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitMaximumCurrent"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitSnapshotRealEnergy"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitLineLineVoltage"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitLineNeutralVoltage"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitFrequency"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitLatchingAlarm"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitNonLatchingAlarm"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitReset"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitBranchAssignment1"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitBranchAssignment2"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitBranchAssignment3"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitCtSize"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LogicalCircuitBreakerSize"))
)
if mibBuilder.loadTexts:
    p1LogicalCircuitGroup.setStatus("current")

p1ConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 7)
)
p1ConfigurationGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1SerialNumber"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1FirmwareRevision"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1DeviceID"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1ProductID"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LocationString"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalResets"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1PanelConfiguration"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1NumSubIntervalsPerDemandInterval"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1SubIntervalSeconds"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1UserDefinedSettings"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxCTSize"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxBreakerSize"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxToVoltagePhaseAssignment"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxToCircuitAssignment"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchCTSize"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchBreakerSize"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchToVoltagePhaseAssignment"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchToCircuitAssignment"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1OverVoltageTimeDelay"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1UnderVoltageTimeDelay"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1HighHighLatchingAlarmTimeDelay"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1HighLatchingAlarmTimeDelay"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LowLatchingAlarmTimeDelay"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LowLowLatchingAlarmTimeDelay"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LatchingAlarmOnTime"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LatchingAlarmOffTime"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1OverVoltageThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1UnderVoltageThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltageHysteresisThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1HighHighLatchingAlarmThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1HighLatchingAlarmThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LowLatchingAlarmThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1LowLowLatchingAlarmThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1NonLatchingHighThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1NonLatchingLowThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1NonLatchingHysteresisThreshold"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1PresentYear"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1PresentDayMonth"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1PresentHourMinute"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1PresentMilliSeconds"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1SnapShotYear"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1SnapShotDayMonth"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1SnapShotHourMinute"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1SnapShotMilliSeconds"))
)
if mibBuilder.loadTexts:
    p1ConfigurationGroup.setStatus("current")


# Notification objects

p1GlobalLatchingAlarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 0, 1)
)
p1GlobalLatchingAlarmStatusTrap.setObjects(
    ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalLatchingAlarmStatus")
)
if mibBuilder.loadTexts:
    p1GlobalLatchingAlarmStatusTrap.setStatus(
        "current"
    )

p1GlobalNonLatchingAlarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 0, 2)
)
p1GlobalNonLatchingAlarmStatusTrap.setObjects(
    ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalLatchingAlarmStatus")
)
if mibBuilder.loadTexts:
    p1GlobalNonLatchingAlarmStatusTrap.setStatus(
        "current"
    )

p1VoltagePhaseAlarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 0, 3)
)
p1VoltagePhaseAlarmStatusTrap.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxAlarmPhase"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltagePhaseAlarmStatus"))
)
if mibBuilder.loadTexts:
    p1VoltagePhaseAlarmStatusTrap.setStatus(
        "current"
    )

p1AuxCurrentAlarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 0, 4)
)
p1AuxCurrentAlarmStatusTrap.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxAlarmPhase"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxCurrentAlarmStatus"))
)
if mibBuilder.loadTexts:
    p1AuxCurrentAlarmStatusTrap.setStatus(
        "current"
    )

p1BranchCurrentAlarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 1, 1, 1, 0, 5)
)
p1BranchCurrentAlarmStatusTrap.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchAlarmNumber"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchCurrentAlarmStatus"))
)
if mibBuilder.loadTexts:
    p1BranchCurrentAlarmStatusTrap.setStatus(
        "current"
    )


# Notifications groups

p1TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3833, 1, 30, 2, 2, 1, 1)
)
p1TrapGroup.setObjects(
      *(("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalLatchingAlarmStatusTrap"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1GlobalNonLatchingAlarmStatusTrap"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1VoltagePhaseAlarmStatusTrap"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1AuxCurrentAlarmStatusTrap"),
        ("SCHNEIDER-ELECTRIC-BCPM-MIB", "p1BranchCurrentAlarmStatusTrap"))
)
if mibBuilder.loadTexts:
    p1TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCHNEIDER-ELECTRIC-BCPM-MIB",
    **{"ThousandthsInt32": ThousandthsInt32,
       "TenthsInt32": TenthsInt32,
       "TenthsCounter64": TenthsCounter64,
       "schneiderElectric": schneiderElectric,
       "schneiderEnergy": schneiderEnergy,
       "bcpm": bcpm,
       "panels": panels,
       "panel1": panel1,
       "p1Alarms": p1Alarms,
       "p1Traps": p1Traps,
       "p1GlobalLatchingAlarmStatusTrap": p1GlobalLatchingAlarmStatusTrap,
       "p1GlobalNonLatchingAlarmStatusTrap": p1GlobalNonLatchingAlarmStatusTrap,
       "p1VoltagePhaseAlarmStatusTrap": p1VoltagePhaseAlarmStatusTrap,
       "p1AuxCurrentAlarmStatusTrap": p1AuxCurrentAlarmStatusTrap,
       "p1BranchCurrentAlarmStatusTrap": p1BranchCurrentAlarmStatusTrap,
       "p1GlobalAlarmStatus": p1GlobalAlarmStatus,
       "p1GlobalLatchingAlarmStatus": p1GlobalLatchingAlarmStatus,
       "p1GlobalNonLatchingAlarmStatus": p1GlobalNonLatchingAlarmStatus,
       "p1GlobalMostRecentLatchingChannel": p1GlobalMostRecentLatchingChannel,
       "p1GlobalMostRecentNonLatchingChannel": p1GlobalMostRecentNonLatchingChannel,
       "p1TotalLatchingChannelsInAlarm": p1TotalLatchingChannelsInAlarm,
       "p1TotalNonLatchingChannelsInAlarm": p1TotalNonLatchingChannelsInAlarm,
       "p1DeviceHealth": p1DeviceHealth,
       "p1GlobalAlarmCounters": p1GlobalAlarmCounters,
       "p1GlobalHighHighLatchingAlarmCount": p1GlobalHighHighLatchingAlarmCount,
       "p1GlobalHighLatchingAlarmCount": p1GlobalHighLatchingAlarmCount,
       "p1GlobalLowLatchingAlarmCount": p1GlobalLowLatchingAlarmCount,
       "p1GlobalLowLowLatchingAlarmCount": p1GlobalLowLowLatchingAlarmCount,
       "p1GlobalOffStateLatchingAlarmCount": p1GlobalOffStateLatchingAlarmCount,
       "p1PowerUpCount": p1PowerUpCount,
       "p1AuxVoltageAndCurrentAlarmTable": p1AuxVoltageAndCurrentAlarmTable,
       "p1AuxVoltageAndCurrentAlarmEntry": p1AuxVoltageAndCurrentAlarmEntry,
       "p1AuxAlarmIndex": p1AuxAlarmIndex,
       "p1AuxAlarmPhase": p1AuxAlarmPhase,
       "p1VoltagePhaseAlarmStatus": p1VoltagePhaseAlarmStatus,
       "p1AuxCurrentAlarmStatus": p1AuxCurrentAlarmStatus,
       "p1AuxHighHighAlarmCount": p1AuxHighHighAlarmCount,
       "p1AuxHighAlarmCount": p1AuxHighAlarmCount,
       "p1AuxLowAlarmCount": p1AuxLowAlarmCount,
       "p1AuxLowLowAlarmCount": p1AuxLowLowAlarmCount,
       "p1AuxOffStateAlarmCount": p1AuxOffStateAlarmCount,
       "p1BranchCurrentAlarmTable": p1BranchCurrentAlarmTable,
       "p1BranchCurrentAlarmEntry": p1BranchCurrentAlarmEntry,
       "p1BranchAlarmIndex": p1BranchAlarmIndex,
       "p1BranchAlarmNumber": p1BranchAlarmNumber,
       "p1BranchCurrentAlarmStatus": p1BranchCurrentAlarmStatus,
       "p1BranchHighHighAlarmCount": p1BranchHighHighAlarmCount,
       "p1BranchHighAlarmCount": p1BranchHighAlarmCount,
       "p1BranchLowAlarmCount": p1BranchLowAlarmCount,
       "p1BranchLowLowAlarmCount": p1BranchLowLowAlarmCount,
       "p1BranchOffStateAlarmCount": p1BranchOffStateAlarmCount,
       "p1VoltageInputs": p1VoltageInputs,
       "p1VoltageAverages": p1VoltageAverages,
       "p1VoltsLineLine3PhaseAve": p1VoltsLineLine3PhaseAve,
       "p1VoltsLineNeutral3PhaseAve": p1VoltsLineNeutral3PhaseAve,
       "p1Frequency": p1Frequency,
       "p1VoltagePhaseTable": p1VoltagePhaseTable,
       "p1VoltagePhaseEntry": p1VoltagePhaseEntry,
       "p1VoltagePhaseIndex": p1VoltagePhaseIndex,
       "p1VoltsLineToLine": p1VoltsLineToLine,
       "p1VoltsLineToNeutral": p1VoltsLineToNeutral,
       "p1VoltsPhaseAngle": p1VoltsPhaseAngle,
       "p1AuxiliaryInputs": p1AuxiliaryInputs,
       "p1Aux3PhaseTotals": p1Aux3PhaseTotals,
       "p1AuxTotalRealEnergy": p1AuxTotalRealEnergy,
       "p1AuxTotalRealPower": p1AuxTotalRealPower,
       "p1AuxTotalApparentPower": p1AuxTotalApparentPower,
       "p1AuxAveragePowerFactor": p1AuxAveragePowerFactor,
       "p1AuxAverageCurrent": p1AuxAverageCurrent,
       "p1AuxPresentTotalRealPowerDemand": p1AuxPresentTotalRealPowerDemand,
       "p1AuxTotalRealEnergySnapShot": p1AuxTotalRealEnergySnapShot,
       "p1AuxMaximumTotalRealPowerDemand": p1AuxMaximumTotalRealPowerDemand,
       "p1AuxMaximumTotalRealPower": p1AuxMaximumTotalRealPower,
       "p1AuxReset": p1AuxReset,
       "p1AuxPhaseTable": p1AuxPhaseTable,
       "p1AuxPhaseEntry": p1AuxPhaseEntry,
       "p1AuxPhaseIndex": p1AuxPhaseIndex,
       "p1AuxRealPower": p1AuxRealPower,
       "p1AuxApparentPower": p1AuxApparentPower,
       "p1AuxPowerFactor": p1AuxPowerFactor,
       "p1AuxCurrent": p1AuxCurrent,
       "p1AuxCurrentAngle": p1AuxCurrentAngle,
       "p1AuxPresentCurrentDemand": p1AuxPresentCurrentDemand,
       "p1AuxMaximumCurrentDemand": p1AuxMaximumCurrentDemand,
       "p1AuxMaximumCurrent": p1AuxMaximumCurrent,
       "p1BranchInputs": p1BranchInputs,
       "p1BranchTable": p1BranchTable,
       "p1BranchEntry": p1BranchEntry,
       "p1BranchNumberIndex": p1BranchNumberIndex,
       "p1BranchRealEnergy": p1BranchRealEnergy,
       "p1BranchRealPower": p1BranchRealPower,
       "p1BranchApparentPower": p1BranchApparentPower,
       "p1BranchPowerFactor": p1BranchPowerFactor,
       "p1BranchCurrent": p1BranchCurrent,
       "p1BranchCurrentAngle": p1BranchCurrentAngle,
       "p1BranchPresentCurrentDemand": p1BranchPresentCurrentDemand,
       "p1BranchPresentRealPowerDemand": p1BranchPresentRealPowerDemand,
       "p1BranchMaximumCurrentDemand": p1BranchMaximumCurrentDemand,
       "p1BranchMaximumRealPowerDemand": p1BranchMaximumRealPowerDemand,
       "p1BranchRealEnergySnapShot": p1BranchRealEnergySnapShot,
       "p1BranchMaximumCurrent": p1BranchMaximumCurrent,
       "p1BranchMaximumRealPower": p1BranchMaximumRealPower,
       "p1BranchReset": p1BranchReset,
       "p1LogicalCircuits": p1LogicalCircuits,
       "p1LogicalCircuitTable": p1LogicalCircuitTable,
       "p1LogicalCircuitEntry": p1LogicalCircuitEntry,
       "p1LogicalCircuitIndex": p1LogicalCircuitIndex,
       "p1LogicalCircuitRealEnergy": p1LogicalCircuitRealEnergy,
       "p1LogicalCircuitRealPower": p1LogicalCircuitRealPower,
       "p1LogicalCircuitApparentPower": p1LogicalCircuitApparentPower,
       "p1LogicalCircuitPowerFactor": p1LogicalCircuitPowerFactor,
       "p1LogicalCircuitCurrent": p1LogicalCircuitCurrent,
       "p1LogicalCircuitPresentRealPowerDemand": p1LogicalCircuitPresentRealPowerDemand,
       "p1LogicalCircuitPresentCurrentDemand": p1LogicalCircuitPresentCurrentDemand,
       "p1LogicalCircuitMaximumRealPowerDemand": p1LogicalCircuitMaximumRealPowerDemand,
       "p1LogicalCircuitMaximumCurrentDemand": p1LogicalCircuitMaximumCurrentDemand,
       "p1LogicalCircuitMaximumRealPower": p1LogicalCircuitMaximumRealPower,
       "p1LogicalCircuitMaximumCurrent": p1LogicalCircuitMaximumCurrent,
       "p1LogicalCircuitSnapshotRealEnergy": p1LogicalCircuitSnapshotRealEnergy,
       "p1LogicalCircuitLineLineVoltage": p1LogicalCircuitLineLineVoltage,
       "p1LogicalCircuitLineNeutralVoltage": p1LogicalCircuitLineNeutralVoltage,
       "p1LogicalCircuitFrequency": p1LogicalCircuitFrequency,
       "p1LogicalCircuitLatchingAlarm": p1LogicalCircuitLatchingAlarm,
       "p1LogicalCircuitNonLatchingAlarm": p1LogicalCircuitNonLatchingAlarm,
       "p1LogicalCircuitReset": p1LogicalCircuitReset,
       "p1LogicalCircuitBranchAssignment1": p1LogicalCircuitBranchAssignment1,
       "p1LogicalCircuitBranchAssignment2": p1LogicalCircuitBranchAssignment2,
       "p1LogicalCircuitBranchAssignment3": p1LogicalCircuitBranchAssignment3,
       "p1LogicalCircuitCtSize": p1LogicalCircuitCtSize,
       "p1LogicalCircuitBreakerSize": p1LogicalCircuitBreakerSize,
       "p1Configuration": p1Configuration,
       "p1ProductInformation": p1ProductInformation,
       "p1SerialNumber": p1SerialNumber,
       "p1FirmwareRevision": p1FirmwareRevision,
       "p1DeviceID": p1DeviceID,
       "p1ProductID": p1ProductID,
       "p1LocationString": p1LocationString,
       "p1GlobalResets": p1GlobalResets,
       "p1Setup": p1Setup,
       "p1PanelConfiguration": p1PanelConfiguration,
       "p1NumSubIntervalsPerDemandInterval": p1NumSubIntervalsPerDemandInterval,
       "p1SubIntervalSeconds": p1SubIntervalSeconds,
       "p1UserDefinedSettings": p1UserDefinedSettings,
       "p1AuxConfiguratonTable": p1AuxConfiguratonTable,
       "p1AuxConfiguratonEntry": p1AuxConfiguratonEntry,
       "p1AuxConfiguratonIndex": p1AuxConfiguratonIndex,
       "p1AuxCTSize": p1AuxCTSize,
       "p1AuxBreakerSize": p1AuxBreakerSize,
       "p1AuxToVoltagePhaseAssignment": p1AuxToVoltagePhaseAssignment,
       "p1AuxToCircuitAssignment": p1AuxToCircuitAssignment,
       "p1BranchConfiguratonTable": p1BranchConfiguratonTable,
       "p1BranchConfiguratonEntry": p1BranchConfiguratonEntry,
       "p1BranchConfiguratonIndex": p1BranchConfiguratonIndex,
       "p1BranchCTSize": p1BranchCTSize,
       "p1BranchBreakerSize": p1BranchBreakerSize,
       "p1BranchToVoltagePhaseAssignment": p1BranchToVoltagePhaseAssignment,
       "p1BranchToCircuitAssignment": p1BranchToCircuitAssignment,
       "p1AlarmConfiguration": p1AlarmConfiguration,
       "p1AlarmTimeDelays": p1AlarmTimeDelays,
       "p1OverVoltageTimeDelay": p1OverVoltageTimeDelay,
       "p1UnderVoltageTimeDelay": p1UnderVoltageTimeDelay,
       "p1HighHighLatchingAlarmTimeDelay": p1HighHighLatchingAlarmTimeDelay,
       "p1HighLatchingAlarmTimeDelay": p1HighLatchingAlarmTimeDelay,
       "p1LowLatchingAlarmTimeDelay": p1LowLatchingAlarmTimeDelay,
       "p1LowLowLatchingAlarmTimeDelay": p1LowLowLatchingAlarmTimeDelay,
       "p1LatchingAlarmOnTime": p1LatchingAlarmOnTime,
       "p1LatchingAlarmOffTime": p1LatchingAlarmOffTime,
       "p1AlarmThresholds": p1AlarmThresholds,
       "p1OverVoltageThreshold": p1OverVoltageThreshold,
       "p1UnderVoltageThreshold": p1UnderVoltageThreshold,
       "p1VoltageHysteresisThreshold": p1VoltageHysteresisThreshold,
       "p1HighHighLatchingAlarmThreshold": p1HighHighLatchingAlarmThreshold,
       "p1HighLatchingAlarmThreshold": p1HighLatchingAlarmThreshold,
       "p1LowLatchingAlarmThreshold": p1LowLatchingAlarmThreshold,
       "p1LowLowLatchingAlarmThreshold": p1LowLowLatchingAlarmThreshold,
       "p1NonLatchingHighThreshold": p1NonLatchingHighThreshold,
       "p1NonLatchingLowThreshold": p1NonLatchingLowThreshold,
       "p1NonLatchingHysteresisThreshold": p1NonLatchingHysteresisThreshold,
       "p1RealTimeClock": p1RealTimeClock,
       "p1PresentTime": p1PresentTime,
       "p1PresentYear": p1PresentYear,
       "p1PresentDayMonth": p1PresentDayMonth,
       "p1PresentHourMinute": p1PresentHourMinute,
       "p1PresentMilliSeconds": p1PresentMilliSeconds,
       "p1SnapShotTime": p1SnapShotTime,
       "p1SnapShotYear": p1SnapShotYear,
       "p1SnapShotDayMonth": p1SnapShotDayMonth,
       "p1SnapShotHourMinute": p1SnapShotHourMinute,
       "p1SnapShotMilliSeconds": p1SnapShotMilliSeconds,
       "conformance": conformance,
       "compliances": compliances,
       "groups": groups,
       "p1ConformanceGroups": p1ConformanceGroups,
       "p1TrapGroup": p1TrapGroup,
       "p1AlarmGroup": p1AlarmGroup,
       "p1VoltageInputGroup": p1VoltageInputGroup,
       "p1AuxiliaryInputGroup": p1AuxiliaryInputGroup,
       "p1BranchInputGroup": p1BranchInputGroup,
       "p1LogicalCircuitGroup": p1LogicalCircuitGroup,
       "p1ConfigurationGroup": p1ConfigurationGroup,
       "schneiderBcpmModuleID": schneiderBcpmModuleID}
)
