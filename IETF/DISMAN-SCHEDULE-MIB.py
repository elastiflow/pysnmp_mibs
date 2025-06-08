# SNMP MIB module (DISMAN-SCHEDULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/DISMAN-SCHEDULE-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:29:12 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

schedMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 63)
)
if mibBuilder.loadTexts:
    schedMIB.setRevisions(
        ("2002-01-07 00:00",
         "1998-11-17 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpPduErrorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("noResponse", -1),
          ("noError", 0),
          ("tooBig", 1),
          ("noSuchName", 2),
          ("badValue", 3),
          ("readOnly", 4),
          ("genErr", 5),
          ("noAccess", 6),
          ("wrongType", 7),
          ("wrongLength", 8),
          ("wrongEncoding", 9),
          ("wrongValue", 10),
          ("noCreation", 11),
          ("inconsistentValue", 12),
          ("resourceUnavailable", 13),
          ("commitFailed", 14),
          ("undoFailed", 15),
          ("authorizationError", 16),
          ("notWritable", 17),
          ("inconsistentName", 18))
    )



# MIB Managed Objects in the order of their OIDs

_SchedObjects_ObjectIdentity = ObjectIdentity
schedObjects = _SchedObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 63, 1)
)


class _SchedLocalTime_Type(DateAndTime):
    """Custom type schedLocalTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixedLength = 11


_SchedLocalTime_Type.__name__ = "DateAndTime"
_SchedLocalTime_Object = MibScalar
schedLocalTime = _SchedLocalTime_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 1),
    _SchedLocalTime_Type()
)
schedLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedLocalTime.setStatus("current")
_SchedTable_Object = MibTable
schedTable = _SchedTable_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2)
)
if mibBuilder.loadTexts:
    schedTable.setStatus("current")
_SchedEntry_Object = MibTableRow
schedEntry = _SchedEntry_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1)
)
schedEntry.setIndexNames(
    (0, "DISMAN-SCHEDULE-MIB", "schedOwner"),
    (0, "DISMAN-SCHEDULE-MIB", "schedName"),
)
if mibBuilder.loadTexts:
    schedEntry.setStatus("current")


class _SchedOwner_Type(SnmpAdminString):
    """Custom type schedOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SchedOwner_Type.__name__ = "SnmpAdminString"
_SchedOwner_Object = MibTableColumn
schedOwner = _SchedOwner_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 1),
    _SchedOwner_Type()
)
schedOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schedOwner.setStatus("current")


class _SchedName_Type(SnmpAdminString):
    """Custom type schedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SchedName_Type.__name__ = "SnmpAdminString"
_SchedName_Object = MibTableColumn
schedName = _SchedName_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 2),
    _SchedName_Type()
)
schedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schedName.setStatus("current")


class _SchedDescr_Type(SnmpAdminString):
    """Custom type schedDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_SchedDescr_Type.__name__ = "SnmpAdminString"
_SchedDescr_Object = MibTableColumn
schedDescr = _SchedDescr_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 3),
    _SchedDescr_Type()
)
schedDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedDescr.setStatus("current")


class _SchedInterval_Type(Unsigned32):
    """Custom type schedInterval based on Unsigned32"""
    defaultValue = 0


_SchedInterval_Type.__name__ = "Unsigned32"
_SchedInterval_Object = MibTableColumn
schedInterval = _SchedInterval_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 4),
    _SchedInterval_Type()
)
schedInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedInterval.setStatus("current")
if mibBuilder.loadTexts:
    schedInterval.setUnits("seconds")


class _SchedWeekDay_Type(Bits):
    """Custom type schedWeekDay based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )

_SchedWeekDay_Type.__name__ = "Bits"
_SchedWeekDay_Object = MibTableColumn
schedWeekDay = _SchedWeekDay_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 5),
    _SchedWeekDay_Type()
)
schedWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedWeekDay.setStatus("current")


class _SchedMonth_Type(Bits):
    """Custom type schedMonth based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )

_SchedMonth_Type.__name__ = "Bits"
_SchedMonth_Object = MibTableColumn
schedMonth = _SchedMonth_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 6),
    _SchedMonth_Type()
)
schedMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedMonth.setStatus("current")


class _SchedDay_Type(Bits):
    """Custom type schedDay based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("d1", 0),
          ("d2", 1),
          ("d3", 2),
          ("d4", 3),
          ("d5", 4),
          ("d6", 5),
          ("d7", 6),
          ("d8", 7),
          ("d9", 8),
          ("d10", 9),
          ("d11", 10),
          ("d12", 11),
          ("d13", 12),
          ("d14", 13),
          ("d15", 14),
          ("d16", 15),
          ("d17", 16),
          ("d18", 17),
          ("d19", 18),
          ("d20", 19),
          ("d21", 20),
          ("d22", 21),
          ("d23", 22),
          ("d24", 23),
          ("d25", 24),
          ("d26", 25),
          ("d27", 26),
          ("d28", 27),
          ("d29", 28),
          ("d30", 29),
          ("d31", 30),
          ("r1", 31),
          ("r2", 32),
          ("r3", 33),
          ("r4", 34),
          ("r5", 35),
          ("r6", 36),
          ("r7", 37),
          ("r8", 38),
          ("r9", 39),
          ("r10", 40),
          ("r11", 41),
          ("r12", 42),
          ("r13", 43),
          ("r14", 44),
          ("r15", 45),
          ("r16", 46),
          ("r17", 47),
          ("r18", 48),
          ("r19", 49),
          ("r20", 50),
          ("r21", 51),
          ("r22", 52),
          ("r23", 53),
          ("r24", 54),
          ("r25", 55),
          ("r26", 56),
          ("r27", 57),
          ("r28", 58),
          ("r29", 59),
          ("r30", 60),
          ("r31", 61))
    )

_SchedDay_Type.__name__ = "Bits"
_SchedDay_Object = MibTableColumn
schedDay = _SchedDay_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 7),
    _SchedDay_Type()
)
schedDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedDay.setStatus("current")


class _SchedHour_Type(Bits):
    """Custom type schedHour based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("h0", 0),
          ("h1", 1),
          ("h2", 2),
          ("h3", 3),
          ("h4", 4),
          ("h5", 5),
          ("h6", 6),
          ("h7", 7),
          ("h8", 8),
          ("h9", 9),
          ("h10", 10),
          ("h11", 11),
          ("h12", 12),
          ("h13", 13),
          ("h14", 14),
          ("h15", 15),
          ("h16", 16),
          ("h17", 17),
          ("h18", 18),
          ("h19", 19),
          ("h20", 20),
          ("h21", 21),
          ("h22", 22),
          ("h23", 23))
    )

_SchedHour_Type.__name__ = "Bits"
_SchedHour_Object = MibTableColumn
schedHour = _SchedHour_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 8),
    _SchedHour_Type()
)
schedHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedHour.setStatus("current")


class _SchedMinute_Type(Bits):
    """Custom type schedMinute based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("m0", 0),
          ("m1", 1),
          ("m2", 2),
          ("m3", 3),
          ("m4", 4),
          ("m5", 5),
          ("m6", 6),
          ("m7", 7),
          ("m8", 8),
          ("m9", 9),
          ("m10", 10),
          ("m11", 11),
          ("m12", 12),
          ("m13", 13),
          ("m14", 14),
          ("m15", 15),
          ("m16", 16),
          ("m17", 17),
          ("m18", 18),
          ("m19", 19),
          ("m20", 20),
          ("m21", 21),
          ("m22", 22),
          ("m23", 23),
          ("m24", 24),
          ("m25", 25),
          ("m26", 26),
          ("m27", 27),
          ("m28", 28),
          ("m29", 29),
          ("m30", 30),
          ("m31", 31),
          ("m32", 32),
          ("m33", 33),
          ("m34", 34),
          ("m35", 35),
          ("m36", 36),
          ("m37", 37),
          ("m38", 38),
          ("m39", 39),
          ("m40", 40),
          ("m41", 41),
          ("m42", 42),
          ("m43", 43),
          ("m44", 44),
          ("m45", 45),
          ("m46", 46),
          ("m47", 47),
          ("m48", 48),
          ("m49", 49),
          ("m50", 50),
          ("m51", 51),
          ("m52", 52),
          ("m53", 53),
          ("m54", 54),
          ("m55", 55),
          ("m56", 56),
          ("m57", 57),
          ("m58", 58),
          ("m59", 59))
    )

_SchedMinute_Type.__name__ = "Bits"
_SchedMinute_Object = MibTableColumn
schedMinute = _SchedMinute_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 9),
    _SchedMinute_Type()
)
schedMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedMinute.setStatus("current")


class _SchedContextName_Type(SnmpAdminString):
    """Custom type schedContextName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SchedContextName_Type.__name__ = "SnmpAdminString"
_SchedContextName_Object = MibTableColumn
schedContextName = _SchedContextName_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 10),
    _SchedContextName_Type()
)
schedContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedContextName.setStatus("current")


class _SchedVariable_Type(VariablePointer):
    """Custom type schedVariable based on VariablePointer"""
    defaultValue = (0, 0)


_SchedVariable_Type.__name__ = "VariablePointer"
_SchedVariable_Object = MibTableColumn
schedVariable = _SchedVariable_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 11),
    _SchedVariable_Type()
)
schedVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedVariable.setStatus("current")


class _SchedValue_Type(Integer32):
    """Custom type schedValue based on Integer32"""
    defaultValue = 0


_SchedValue_Type.__name__ = "Integer32"
_SchedValue_Object = MibTableColumn
schedValue = _SchedValue_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 12),
    _SchedValue_Type()
)
schedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedValue.setStatus("current")


class _SchedType_Type(Integer32):
    """Custom type schedType based on Integer32"""
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
        *(("periodic", 1),
          ("calendar", 2),
          ("oneshot", 3))
    )


_SchedType_Type.__name__ = "Integer32"
_SchedType_Object = MibTableColumn
schedType = _SchedType_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 13),
    _SchedType_Type()
)
schedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedType.setStatus("current")


class _SchedAdminStatus_Type(Integer32):
    """Custom type schedAdminStatus based on Integer32"""
    defaultValue = 2

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


_SchedAdminStatus_Type.__name__ = "Integer32"
_SchedAdminStatus_Object = MibTableColumn
schedAdminStatus = _SchedAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 14),
    _SchedAdminStatus_Type()
)
schedAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedAdminStatus.setStatus("current")


class _SchedOperStatus_Type(Integer32):
    """Custom type schedOperStatus based on Integer32"""
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
          ("finished", 3))
    )


_SchedOperStatus_Type.__name__ = "Integer32"
_SchedOperStatus_Object = MibTableColumn
schedOperStatus = _SchedOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 15),
    _SchedOperStatus_Type()
)
schedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedOperStatus.setStatus("current")
_SchedFailures_Type = Counter32
_SchedFailures_Object = MibTableColumn
schedFailures = _SchedFailures_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 16),
    _SchedFailures_Type()
)
schedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedFailures.setStatus("current")


class _SchedLastFailure_Type(SnmpPduErrorStatus):
    """Custom type schedLastFailure based on SnmpPduErrorStatus"""
    defaultValue = 0


_SchedLastFailure_Type.__name__ = "SnmpPduErrorStatus"
_SchedLastFailure_Object = MibTableColumn
schedLastFailure = _SchedLastFailure_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 17),
    _SchedLastFailure_Type()
)
schedLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedLastFailure.setStatus("current")


class _SchedLastFailed_Type(DateAndTime):
    """Custom type schedLastFailed based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SchedLastFailed_Type.__name__ = "DateAndTime"
_SchedLastFailed_Object = MibTableColumn
schedLastFailed = _SchedLastFailed_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 18),
    _SchedLastFailed_Type()
)
schedLastFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedLastFailed.setStatus("current")


class _SchedStorageType_Type(StorageType):
    """Custom type schedStorageType based on StorageType"""
    defaultValue = 2


_SchedStorageType_Type.__name__ = "StorageType"
_SchedStorageType_Object = MibTableColumn
schedStorageType = _SchedStorageType_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 19),
    _SchedStorageType_Type()
)
schedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedStorageType.setStatus("current")
_SchedRowStatus_Type = RowStatus
_SchedRowStatus_Object = MibTableColumn
schedRowStatus = _SchedRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 20),
    _SchedRowStatus_Type()
)
schedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedRowStatus.setStatus("current")
_SchedTriggers_Type = Counter32
_SchedTriggers_Object = MibTableColumn
schedTriggers = _SchedTriggers_Object(
    (1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 21),
    _SchedTriggers_Type()
)
schedTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedTriggers.setStatus("current")
_SchedNotifications_ObjectIdentity = ObjectIdentity
schedNotifications = _SchedNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 63, 2)
)
_SchedTraps_ObjectIdentity = ObjectIdentity
schedTraps = _SchedTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 63, 2, 0)
)
_SchedConformance_ObjectIdentity = ObjectIdentity
schedConformance = _SchedConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 63, 3)
)
_SchedCompliances_ObjectIdentity = ObjectIdentity
schedCompliances = _SchedCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 63, 3, 1)
)
_SchedGroups_ObjectIdentity = ObjectIdentity
schedGroups = _SchedGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 63, 3, 2)
)

# Managed Objects groups

schedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 63, 3, 2, 1)
)
schedGroup.setObjects(
      *(("DISMAN-SCHEDULE-MIB", "schedDescr"),
        ("DISMAN-SCHEDULE-MIB", "schedInterval"),
        ("DISMAN-SCHEDULE-MIB", "schedContextName"),
        ("DISMAN-SCHEDULE-MIB", "schedVariable"),
        ("DISMAN-SCHEDULE-MIB", "schedValue"),
        ("DISMAN-SCHEDULE-MIB", "schedType"),
        ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"),
        ("DISMAN-SCHEDULE-MIB", "schedOperStatus"),
        ("DISMAN-SCHEDULE-MIB", "schedFailures"),
        ("DISMAN-SCHEDULE-MIB", "schedLastFailure"),
        ("DISMAN-SCHEDULE-MIB", "schedLastFailed"),
        ("DISMAN-SCHEDULE-MIB", "schedStorageType"),
        ("DISMAN-SCHEDULE-MIB", "schedRowStatus"))
)
if mibBuilder.loadTexts:
    schedGroup.setStatus("deprecated")

schedCalendarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 63, 3, 2, 2)
)
schedCalendarGroup.setObjects(
      *(("DISMAN-SCHEDULE-MIB", "schedLocalTime"),
        ("DISMAN-SCHEDULE-MIB", "schedWeekDay"),
        ("DISMAN-SCHEDULE-MIB", "schedMonth"),
        ("DISMAN-SCHEDULE-MIB", "schedDay"),
        ("DISMAN-SCHEDULE-MIB", "schedHour"),
        ("DISMAN-SCHEDULE-MIB", "schedMinute"))
)
if mibBuilder.loadTexts:
    schedCalendarGroup.setStatus("current")

schedGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 63, 3, 2, 4)
)
schedGroup2.setObjects(
      *(("DISMAN-SCHEDULE-MIB", "schedDescr"),
        ("DISMAN-SCHEDULE-MIB", "schedInterval"),
        ("DISMAN-SCHEDULE-MIB", "schedContextName"),
        ("DISMAN-SCHEDULE-MIB", "schedVariable"),
        ("DISMAN-SCHEDULE-MIB", "schedValue"),
        ("DISMAN-SCHEDULE-MIB", "schedType"),
        ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"),
        ("DISMAN-SCHEDULE-MIB", "schedOperStatus"),
        ("DISMAN-SCHEDULE-MIB", "schedFailures"),
        ("DISMAN-SCHEDULE-MIB", "schedLastFailure"),
        ("DISMAN-SCHEDULE-MIB", "schedLastFailed"),
        ("DISMAN-SCHEDULE-MIB", "schedStorageType"),
        ("DISMAN-SCHEDULE-MIB", "schedRowStatus"),
        ("DISMAN-SCHEDULE-MIB", "schedTriggers"))
)
if mibBuilder.loadTexts:
    schedGroup2.setStatus("current")


# Notification objects

schedActionFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 63, 2, 0, 1)
)
schedActionFailure.setObjects(
      *(("DISMAN-SCHEDULE-MIB", "schedLastFailure"),
        ("DISMAN-SCHEDULE-MIB", "schedLastFailed"))
)
if mibBuilder.loadTexts:
    schedActionFailure.setStatus(
        "current"
    )


# Notifications groups

schedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 63, 3, 2, 3)
)
schedNotificationsGroup.setObjects(
    ("DISMAN-SCHEDULE-MIB", "schedActionFailure")
)
if mibBuilder.loadTexts:
    schedNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

schedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 63, 3, 1, 1)
)
schedCompliance.setObjects(
      *(("DISMAN-SCHEDULE-MIB", "schedGroup"),
        ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"),
        ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))
)
if mibBuilder.loadTexts:
    schedCompliance.setStatus(
        "deprecated"
    )

schedCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 63, 3, 1, 2)
)
schedCompliance2.setObjects(
      *(("DISMAN-SCHEDULE-MIB", "schedGroup2"),
        ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"),
        ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))
)
if mibBuilder.loadTexts:
    schedCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-SCHEDULE-MIB",
    **{"SnmpPduErrorStatus": SnmpPduErrorStatus,
       "schedMIB": schedMIB,
       "schedObjects": schedObjects,
       "schedLocalTime": schedLocalTime,
       "schedTable": schedTable,
       "schedEntry": schedEntry,
       "schedOwner": schedOwner,
       "schedName": schedName,
       "schedDescr": schedDescr,
       "schedInterval": schedInterval,
       "schedWeekDay": schedWeekDay,
       "schedMonth": schedMonth,
       "schedDay": schedDay,
       "schedHour": schedHour,
       "schedMinute": schedMinute,
       "schedContextName": schedContextName,
       "schedVariable": schedVariable,
       "schedValue": schedValue,
       "schedType": schedType,
       "schedAdminStatus": schedAdminStatus,
       "schedOperStatus": schedOperStatus,
       "schedFailures": schedFailures,
       "schedLastFailure": schedLastFailure,
       "schedLastFailed": schedLastFailed,
       "schedStorageType": schedStorageType,
       "schedRowStatus": schedRowStatus,
       "schedTriggers": schedTriggers,
       "schedNotifications": schedNotifications,
       "schedTraps": schedTraps,
       "schedActionFailure": schedActionFailure,
       "schedConformance": schedConformance,
       "schedCompliances": schedCompliances,
       "schedCompliance": schedCompliance,
       "schedCompliance2": schedCompliance2,
       "schedGroups": schedGroups,
       "schedGroup": schedGroup,
       "schedCalendarGroup": schedCalendarGroup,
       "schedNotificationsGroup": schedNotificationsGroup,
       "schedGroup2": schedGroup2}
)
