# SNMP MIB module (PS-POWERSHIELD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/powershield_35154/PS-POWERSHIELD-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:09 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

psPowerShield = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35154)
)
if mibBuilder.loadTexts:
    psPowerShield.setRevisions(
        ("2010-06-10 01:08",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PsB1001_ObjectIdentity = ObjectIdentity
psB1001 = _PsB1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001)
)
_PsNotificationsObjects_ObjectIdentity = ObjectIdentity
psNotificationsObjects = _PsNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1)
)


class _PsAlarmTimeStamp_Type(OctetString):
    """Custom type psAlarmTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixed_length = 13


_PsAlarmTimeStamp_Type.__name__ = "OctetString"
_PsAlarmTimeStamp_Object = MibScalar
psAlarmTimeStamp = _PsAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 11),
    _PsAlarmTimeStamp_Type()
)
psAlarmTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmTimeStamp.setStatus("current")


class _PsAlarmCatagory_Type(Integer32):
    """Custom type psAlarmCatagory based on Integer32"""
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
        *(("notTriggered", 1),
          ("lowLimitExceeded", 2),
          ("highLimitExceeded", 3),
          ("lowLimitExceededInDischarge", 4),
          ("highLimitDischarge", 5),
          ("lowLimitExceededInCharge", 6),
          ("highLimitCharge", 7))
    )


_PsAlarmCatagory_Type.__name__ = "Integer32"
_PsAlarmCatagory_Object = MibScalar
psAlarmCatagory = _PsAlarmCatagory_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 12),
    _PsAlarmCatagory_Type()
)
psAlarmCatagory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmCatagory.setStatus("current")


class _PsAlarmChannel_Type(Integer32):
    """Custom type psAlarmChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PsAlarmChannel_Type.__name__ = "Integer32"
_PsAlarmChannel_Object = MibScalar
psAlarmChannel = _PsAlarmChannel_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 13),
    _PsAlarmChannel_Type()
)
psAlarmChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmChannel.setStatus("current")


class _PsAlarmString_Type(Integer32):
    """Custom type psAlarmString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PsAlarmString_Type.__name__ = "Integer32"
_PsAlarmString_Object = MibScalar
psAlarmString = _PsAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 14),
    _PsAlarmString_Type()
)
psAlarmString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmString.setStatus("current")


class _PsAlarmMonitor_Type(Integer32):
    """Custom type psAlarmMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("master", 0),
          ("slave1", 1),
          ("slave2", 2),
          ("slave3", 3),
          ("slave4", 4),
          ("slave5", 5),
          ("slave6", 6),
          ("slave7", 7),
          ("slave8", 8),
          ("slave9", 9),
          ("slave10", 10),
          ("slave11", 11),
          ("slave12", 12),
          ("slave13", 13),
          ("slave14", 14),
          ("slave15", 15))
    )


_PsAlarmMonitor_Type.__name__ = "Integer32"
_PsAlarmMonitor_Object = MibScalar
psAlarmMonitor = _PsAlarmMonitor_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 15),
    _PsAlarmMonitor_Type()
)
psAlarmMonitor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmMonitor.setStatus("current")


class _PsAlarmMonoblockMinimum_Type(Integer32):
    """Custom type psAlarmMonoblockMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_PsAlarmMonoblockMinimum_Type.__name__ = "Integer32"
_PsAlarmMonoblockMinimum_Object = MibScalar
psAlarmMonoblockMinimum = _PsAlarmMonoblockMinimum_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 16),
    _PsAlarmMonoblockMinimum_Type()
)
psAlarmMonoblockMinimum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmMonoblockMinimum.setStatus("current")


class _PsAlarmMonoblockMaximum_Type(Integer32):
    """Custom type psAlarmMonoblockMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_PsAlarmMonoblockMaximum_Type.__name__ = "Integer32"
_PsAlarmMonoblockMaximum_Object = MibScalar
psAlarmMonoblockMaximum = _PsAlarmMonoblockMaximum_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 17),
    _PsAlarmMonoblockMaximum_Type()
)
psAlarmMonoblockMaximum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmMonoblockMaximum.setStatus("current")


class _PsAlarmMinimum_Type(Integer32):
    """Custom type psAlarmMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PsAlarmMinimum_Type.__name__ = "Integer32"
_PsAlarmMinimum_Object = MibScalar
psAlarmMinimum = _PsAlarmMinimum_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 18),
    _PsAlarmMinimum_Type()
)
psAlarmMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmMinimum.setStatus("current")


class _PsAlarmMaximum_Type(Integer32):
    """Custom type psAlarmMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PsAlarmMaximum_Type.__name__ = "Integer32"
_PsAlarmMaximum_Object = MibScalar
psAlarmMaximum = _PsAlarmMaximum_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 19),
    _PsAlarmMaximum_Type()
)
psAlarmMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmMaximum.setStatus("current")


class _PsAlarmInputNumber_Type(Integer32):
    """Custom type psAlarmInputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PsAlarmInputNumber_Type.__name__ = "Integer32"
_PsAlarmInputNumber_Object = MibScalar
psAlarmInputNumber = _PsAlarmInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 20),
    _PsAlarmInputNumber_Type()
)
psAlarmInputNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmInputNumber.setStatus("current")


class _PsAlarmInputState_Type(Integer32):
    """Custom type psAlarmInputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PsAlarmInputState_Type.__name__ = "Integer32"
_PsAlarmInputState_Object = MibScalar
psAlarmInputState = _PsAlarmInputState_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 1, 21),
    _PsAlarmInputState_Type()
)
psAlarmInputState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psAlarmInputState.setStatus("current")
_PsNotifications_ObjectIdentity = ObjectIdentity
psNotifications = _PsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2)
)
_PsNotificationsPrefix_ObjectIdentity = ObjectIdentity
psNotificationsPrefix = _PsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0)
)
_PsStrings_ObjectIdentity = ObjectIdentity
psStrings = _PsStrings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3)
)
_PsStringTable_Object = MibTable
psStringTable = _PsStringTable_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1)
)
if mibBuilder.loadTexts:
    psStringTable.setStatus("current")
_PsStringEntry_Object = MibTableRow
psStringEntry = _PsStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1)
)
psStringEntry.setIndexNames(
    (0, "PS-POWERSHIELD-MIB", "psStringNumber"),
)
if mibBuilder.loadTexts:
    psStringEntry.setStatus("current")


class _PsStringNumber_Type(Integer32):
    """Custom type psStringNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PsStringNumber_Type.__name__ = "Integer32"
_PsStringNumber_Object = MibTableColumn
psStringNumber = _PsStringNumber_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 1),
    _PsStringNumber_Type()
)
psStringNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psStringNumber.setStatus("current")


class _PsStringFirstMonoblock_Type(Integer32):
    """Custom type psStringFirstMonoblock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1280),
    )


_PsStringFirstMonoblock_Type.__name__ = "Integer32"
_PsStringFirstMonoblock_Object = MibTableColumn
psStringFirstMonoblock = _PsStringFirstMonoblock_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 2),
    _PsStringFirstMonoblock_Type()
)
psStringFirstMonoblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringFirstMonoblock.setStatus("current")


class _PsStringLastMonoblock_Type(Integer32):
    """Custom type psStringLastMonoblock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1280),
    )


_PsStringLastMonoblock_Type.__name__ = "Integer32"
_PsStringLastMonoblock_Object = MibTableColumn
psStringLastMonoblock = _PsStringLastMonoblock_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 3),
    _PsStringLastMonoblock_Type()
)
psStringLastMonoblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringLastMonoblock.setStatus("current")


class _PsStringState_Type(OctetString):
    """Custom type psStringState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PsStringState_Type.__name__ = "OctetString"
_PsStringState_Object = MibTableColumn
psStringState = _PsStringState_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 4),
    _PsStringState_Type()
)
psStringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringState.setStatus("current")


class _PsStringVoltage_Type(Integer32):
    """Custom type psStringVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PsStringVoltage_Type.__name__ = "Integer32"
_PsStringVoltage_Object = MibTableColumn
psStringVoltage = _PsStringVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 5),
    _PsStringVoltage_Type()
)
psStringVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringVoltage.setStatus("current")


class _PsStringTemperature_Type(Integer32):
    """Custom type psStringTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsStringTemperature_Type.__name__ = "Integer32"
_PsStringTemperature_Object = MibTableColumn
psStringTemperature = _PsStringTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 6),
    _PsStringTemperature_Type()
)
psStringTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringTemperature.setStatus("current")


class _PsStringCurrent_Type(Integer32):
    """Custom type psStringCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsStringCurrent_Type.__name__ = "Integer32"
_PsStringCurrent_Object = MibTableColumn
psStringCurrent = _PsStringCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 7),
    _PsStringCurrent_Type()
)
psStringCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringCurrent.setStatus("current")


class _PsStringTimestamp_Type(OctetString):
    """Custom type psStringTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PsStringTimestamp_Type.__name__ = "OctetString"
_PsStringTimestamp_Object = MibTableColumn
psStringTimestamp = _PsStringTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 3, 1, 1, 8),
    _PsStringTimestamp_Type()
)
psStringTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringTimestamp.setStatus("current")
_PsMonoblocks_ObjectIdentity = ObjectIdentity
psMonoblocks = _PsMonoblocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4)
)
_PsMonoblockTable_Object = MibTable
psMonoblockTable = _PsMonoblockTable_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1)
)
if mibBuilder.loadTexts:
    psMonoblockTable.setStatus("current")
_PsMonoblockEntry_Object = MibTableRow
psMonoblockEntry = _PsMonoblockEntry_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1)
)
psMonoblockEntry.setIndexNames(
    (0, "PS-POWERSHIELD-MIB", "psMonoblockNumber"),
)
if mibBuilder.loadTexts:
    psMonoblockEntry.setStatus("current")


class _PsMonoblockNumber_Type(Integer32):
    """Custom type psMonoblockNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1280),
    )


_PsMonoblockNumber_Type.__name__ = "Integer32"
_PsMonoblockNumber_Object = MibTableColumn
psMonoblockNumber = _PsMonoblockNumber_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1, 1),
    _PsMonoblockNumber_Type()
)
psMonoblockNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psMonoblockNumber.setStatus("current")


class _PsMonoblockOwner_Type(Integer32):
    """Custom type psMonoblockOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1280),
    )


_PsMonoblockOwner_Type.__name__ = "Integer32"
_PsMonoblockOwner_Object = MibTableColumn
psMonoblockOwner = _PsMonoblockOwner_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1, 2),
    _PsMonoblockOwner_Type()
)
psMonoblockOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMonoblockOwner.setStatus("current")


class _PsMonoblockVoltage_Type(Integer32):
    """Custom type psMonoblockVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsMonoblockVoltage_Type.__name__ = "Integer32"
_PsMonoblockVoltage_Object = MibTableColumn
psMonoblockVoltage = _PsMonoblockVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1, 3),
    _PsMonoblockVoltage_Type()
)
psMonoblockVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMonoblockVoltage.setStatus("current")


class _PsMonoblockTemperature_Type(Integer32):
    """Custom type psMonoblockTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsMonoblockTemperature_Type.__name__ = "Integer32"
_PsMonoblockTemperature_Object = MibTableColumn
psMonoblockTemperature = _PsMonoblockTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1, 4),
    _PsMonoblockTemperature_Type()
)
psMonoblockTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMonoblockTemperature.setStatus("current")


class _PsMonoblockImpedance_Type(Integer32):
    """Custom type psMonoblockImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PsMonoblockImpedance_Type.__name__ = "Integer32"
_PsMonoblockImpedance_Object = MibTableColumn
psMonoblockImpedance = _PsMonoblockImpedance_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1, 5),
    _PsMonoblockImpedance_Type()
)
psMonoblockImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMonoblockImpedance.setStatus("current")


class _PsMonoblockTimestamp_Type(OctetString):
    """Custom type psMonoblockTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PsMonoblockTimestamp_Type.__name__ = "OctetString"
_PsMonoblockTimestamp_Object = MibTableColumn
psMonoblockTimestamp = _PsMonoblockTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 4, 1, 1, 6),
    _PsMonoblockTimestamp_Type()
)
psMonoblockTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMonoblockTimestamp.setStatus("current")
_PsDebuggingObjects_ObjectIdentity = ObjectIdentity
psDebuggingObjects = _PsDebuggingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5)
)


class _PsDebuggingTimeouts_Type(Integer32):
    """Custom type psDebuggingTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingTimeouts_Type.__name__ = "Integer32"
_PsDebuggingTimeouts_Object = MibScalar
psDebuggingTimeouts = _PsDebuggingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 1),
    _PsDebuggingTimeouts_Type()
)
psDebuggingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingTimeouts.setStatus("current")


class _PsDebuggingOverflows_Type(Integer32):
    """Custom type psDebuggingOverflows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingOverflows_Type.__name__ = "Integer32"
_PsDebuggingOverflows_Object = MibScalar
psDebuggingOverflows = _PsDebuggingOverflows_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 2),
    _PsDebuggingOverflows_Type()
)
psDebuggingOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingOverflows.setStatus("current")


class _PsDebuggingRequests_Type(Integer32):
    """Custom type psDebuggingRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingRequests_Type.__name__ = "Integer32"
_PsDebuggingRequests_Object = MibScalar
psDebuggingRequests = _PsDebuggingRequests_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 3),
    _PsDebuggingRequests_Type()
)
psDebuggingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingRequests.setStatus("current")


class _PsDebuggingResponses_Type(Integer32):
    """Custom type psDebuggingResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingResponses_Type.__name__ = "Integer32"
_PsDebuggingResponses_Object = MibScalar
psDebuggingResponses = _PsDebuggingResponses_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 4),
    _PsDebuggingResponses_Type()
)
psDebuggingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingResponses.setStatus("current")


class _PsDebuggingValid_Type(Integer32):
    """Custom type psDebuggingValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingValid_Type.__name__ = "Integer32"
_PsDebuggingValid_Object = MibScalar
psDebuggingValid = _PsDebuggingValid_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 5),
    _PsDebuggingValid_Type()
)
psDebuggingValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingValid.setStatus("current")


class _PsDebuggingInvalid_Type(Integer32):
    """Custom type psDebuggingInvalid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingInvalid_Type.__name__ = "Integer32"
_PsDebuggingInvalid_Object = MibScalar
psDebuggingInvalid = _PsDebuggingInvalid_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 6),
    _PsDebuggingInvalid_Type()
)
psDebuggingInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingInvalid.setStatus("current")


class _PsDebuggingRetries_Type(Integer32):
    """Custom type psDebuggingRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsDebuggingRetries_Type.__name__ = "Integer32"
_PsDebuggingRetries_Object = MibScalar
psDebuggingRetries = _PsDebuggingRetries_Object(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 5, 7),
    _PsDebuggingRetries_Type()
)
psDebuggingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDebuggingRetries.setStatus("current")

# Managed Objects groups


# Notification objects

psAlarmMonoblockChargeDischarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 1)
)
psAlarmMonoblockChargeDischarge.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmChannel"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmMonoblockChargeDischarge.setStatus(
        "current"
    )

psAlarmMonoblockFloat = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 2)
)
psAlarmMonoblockFloat.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmChannel"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmMonoblockFloat.setStatus(
        "current"
    )

psAlarmMonoblockVoltageVariation = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 3)
)
psAlarmMonoblockVoltageVariation.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMaximum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmMonoblockVoltageVariation.setStatus(
        "current"
    )

psAlarmMonoblockVoltageIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 4)
)
psAlarmMonoblockVoltageIdle.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmMonoblockVoltageIdle.setStatus(
        "current"
    )

psAlarmStringVoltageChargeDischarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 5)
)
psAlarmStringVoltageChargeDischarge.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmStringVoltageChargeDischarge.setStatus(
        "current"
    )

psAlarmStringVoltageFloat = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 6)
)
psAlarmStringVoltageFloat.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmStringVoltageFloat.setStatus(
        "current"
    )

psAlarmChargeCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 7)
)
psAlarmChargeCurrent.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmChannel"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmChargeCurrent.setStatus(
        "current"
    )

psAlarmDischargeCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 8)
)
psAlarmDischargeCurrent.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmChannel"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmDischargeCurrent.setStatus(
        "current"
    )

psAlarmFloatCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 9)
)
psAlarmFloatCurrent.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmChannel"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmFloatCurrent.setStatus(
        "current"
    )

psAlarmStringModeCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 10)
)
psAlarmStringModeCharge.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"))
)
if mibBuilder.loadTexts:
    psAlarmStringModeCharge.setStatus(
        "current"
    )

psAlarmStringModeDischarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 11)
)
psAlarmStringModeDischarge.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"))
)
if mibBuilder.loadTexts:
    psAlarmStringModeDischarge.setStatus(
        "current"
    )

psAlarmStringModeFloat = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 12)
)
psAlarmStringModeFloat.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"))
)
if mibBuilder.loadTexts:
    psAlarmStringModeFloat.setStatus(
        "current"
    )

psAlarmStringModeIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 13)
)
psAlarmStringModeIdle.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"))
)
if mibBuilder.loadTexts:
    psAlarmStringModeIdle.setStatus(
        "current"
    )

psAlarmModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 14)
)
psAlarmModuleFailure.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"))
)
if mibBuilder.loadTexts:
    psAlarmModuleFailure.setStatus(
        "current"
    )

psAlarmMonitorOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 15)
)
psAlarmMonitorOffline.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"))
)
if mibBuilder.loadTexts:
    psAlarmMonitorOffline.setStatus(
        "current"
    )

psAlarmMemoryFormat = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 16)
)
psAlarmMemoryFormat.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"))
)
if mibBuilder.loadTexts:
    psAlarmMemoryFormat.setStatus(
        "current"
    )

psAlarmMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 17)
)
psAlarmMemoryLow.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"))
)
if mibBuilder.loadTexts:
    psAlarmMemoryLow.setStatus(
        "current"
    )

psAlarmMemoryFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 18)
)
psAlarmMemoryFull.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"))
)
if mibBuilder.loadTexts:
    psAlarmMemoryFull.setStatus(
        "current"
    )

psAlarmLongTermMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 19)
)
psAlarmLongTermMemoryLow.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"))
)
if mibBuilder.loadTexts:
    psAlarmLongTermMemoryLow.setStatus(
        "current"
    )

psAlarmLongTermMemoryFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 20)
)
psAlarmLongTermMemoryFull.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"))
)
if mibBuilder.loadTexts:
    psAlarmLongTermMemoryFull.setStatus(
        "current"
    )

psAlarmTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 21)
)
psAlarmTemperature.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmChannel"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmTemperature.setStatus(
        "current"
    )

psAlarmMonoblockPostTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 22)
)
psAlarmMonoblockPostTemperature.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmMonoblockPostTemperature.setStatus(
        "current"
    )

psAlarmMonoblockTemperatureVariation = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 23)
)
psAlarmMonoblockTemperatureVariation.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmMonoblockTemperatureVariation.setStatus(
        "current"
    )

psAlarmMonitoredMains = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 24)
)
psAlarmMonitoredMains.setObjects(
    ("PS-POWERSHIELD-MIB", "psAlarmTimeStamp")
)
if mibBuilder.loadTexts:
    psAlarmMonitoredMains.setStatus(
        "current"
    )

psAlarmCommsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 25)
)
psAlarmCommsNotification.setObjects(
    ("PS-POWERSHIELD-MIB", "psAlarmTimeStamp")
)
if mibBuilder.loadTexts:
    psAlarmCommsNotification.setStatus(
        "current"
    )

psAlarmBaselineImpedanceExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 26)
)
psAlarmBaselineImpedanceExceeded.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmBaselineImpedanceExceeded.setStatus(
        "current"
    )

psAlarmStringVarianceImpedanceExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 27)
)
psAlarmStringVarianceImpedanceExceeded.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmTimeStamp"),
        ("PS-POWERSHIELD-MIB", "psAlarmCatagory"),
        ("PS-POWERSHIELD-MIB", "psAlarmString"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonitor"),
        ("PS-POWERSHIELD-MIB", "psAlarmMonoblockMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMinimum"),
        ("PS-POWERSHIELD-MIB", "psAlarmMaximum"))
)
if mibBuilder.loadTexts:
    psAlarmStringVarianceImpedanceExceeded.setStatus(
        "current"
    )

psAlarmInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 35154, 1001, 2, 0, 28)
)
psAlarmInput.setObjects(
      *(("PS-POWERSHIELD-MIB", "psAlarmInputNumber"),
        ("PS-POWERSHIELD-MIB", "psAlarmInputState"))
)
if mibBuilder.loadTexts:
    psAlarmInput.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PS-POWERSHIELD-MIB",
    **{"psPowerShield": psPowerShield,
       "psB1001": psB1001,
       "psNotificationsObjects": psNotificationsObjects,
       "psAlarmTimeStamp": psAlarmTimeStamp,
       "psAlarmCatagory": psAlarmCatagory,
       "psAlarmChannel": psAlarmChannel,
       "psAlarmString": psAlarmString,
       "psAlarmMonitor": psAlarmMonitor,
       "psAlarmMonoblockMinimum": psAlarmMonoblockMinimum,
       "psAlarmMonoblockMaximum": psAlarmMonoblockMaximum,
       "psAlarmMinimum": psAlarmMinimum,
       "psAlarmMaximum": psAlarmMaximum,
       "psAlarmInputNumber": psAlarmInputNumber,
       "psAlarmInputState": psAlarmInputState,
       "psNotifications": psNotifications,
       "psNotificationsPrefix": psNotificationsPrefix,
       "psAlarmMonoblockChargeDischarge": psAlarmMonoblockChargeDischarge,
       "psAlarmMonoblockFloat": psAlarmMonoblockFloat,
       "psAlarmMonoblockVoltageVariation": psAlarmMonoblockVoltageVariation,
       "psAlarmMonoblockVoltageIdle": psAlarmMonoblockVoltageIdle,
       "psAlarmStringVoltageChargeDischarge": psAlarmStringVoltageChargeDischarge,
       "psAlarmStringVoltageFloat": psAlarmStringVoltageFloat,
       "psAlarmChargeCurrent": psAlarmChargeCurrent,
       "psAlarmDischargeCurrent": psAlarmDischargeCurrent,
       "psAlarmFloatCurrent": psAlarmFloatCurrent,
       "psAlarmStringModeCharge": psAlarmStringModeCharge,
       "psAlarmStringModeDischarge": psAlarmStringModeDischarge,
       "psAlarmStringModeFloat": psAlarmStringModeFloat,
       "psAlarmStringModeIdle": psAlarmStringModeIdle,
       "psAlarmModuleFailure": psAlarmModuleFailure,
       "psAlarmMonitorOffline": psAlarmMonitorOffline,
       "psAlarmMemoryFormat": psAlarmMemoryFormat,
       "psAlarmMemoryLow": psAlarmMemoryLow,
       "psAlarmMemoryFull": psAlarmMemoryFull,
       "psAlarmLongTermMemoryLow": psAlarmLongTermMemoryLow,
       "psAlarmLongTermMemoryFull": psAlarmLongTermMemoryFull,
       "psAlarmTemperature": psAlarmTemperature,
       "psAlarmMonoblockPostTemperature": psAlarmMonoblockPostTemperature,
       "psAlarmMonoblockTemperatureVariation": psAlarmMonoblockTemperatureVariation,
       "psAlarmMonitoredMains": psAlarmMonitoredMains,
       "psAlarmCommsNotification": psAlarmCommsNotification,
       "psAlarmBaselineImpedanceExceeded": psAlarmBaselineImpedanceExceeded,
       "psAlarmStringVarianceImpedanceExceeded": psAlarmStringVarianceImpedanceExceeded,
       "psAlarmInput": psAlarmInput,
       "psStrings": psStrings,
       "psStringTable": psStringTable,
       "psStringEntry": psStringEntry,
       "psStringNumber": psStringNumber,
       "psStringFirstMonoblock": psStringFirstMonoblock,
       "psStringLastMonoblock": psStringLastMonoblock,
       "psStringState": psStringState,
       "psStringVoltage": psStringVoltage,
       "psStringTemperature": psStringTemperature,
       "psStringCurrent": psStringCurrent,
       "psStringTimestamp": psStringTimestamp,
       "psMonoblocks": psMonoblocks,
       "psMonoblockTable": psMonoblockTable,
       "psMonoblockEntry": psMonoblockEntry,
       "psMonoblockNumber": psMonoblockNumber,
       "psMonoblockOwner": psMonoblockOwner,
       "psMonoblockVoltage": psMonoblockVoltage,
       "psMonoblockTemperature": psMonoblockTemperature,
       "psMonoblockImpedance": psMonoblockImpedance,
       "psMonoblockTimestamp": psMonoblockTimestamp,
       "psDebuggingObjects": psDebuggingObjects,
       "psDebuggingTimeouts": psDebuggingTimeouts,
       "psDebuggingOverflows": psDebuggingOverflows,
       "psDebuggingRequests": psDebuggingRequests,
       "psDebuggingResponses": psDebuggingResponses,
       "psDebuggingValid": psDebuggingValid,
       "psDebuggingInvalid": psDebuggingInvalid,
       "psDebuggingRetries": psDebuggingRetries}
)
