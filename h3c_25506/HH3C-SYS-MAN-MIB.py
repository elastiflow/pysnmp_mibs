# SNMP MIB module (HH3C-SYS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-SYS-MAN-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:43:37 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(SnmpTagList,
 SnmpTagValue) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagList",
    "SnmpTagValue")

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


# MODULE-IDENTITY

hh3cSystemMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cSystemMan.setRevisions(
        ("2004-04-08 13:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSystemManMIBObjects_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBObjects = _Hh3cSystemManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1)
)
_Hh3cSysClock_ObjectIdentity = ObjectIdentity
hh3cSysClock = _Hh3cSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1)
)
_Hh3cSysLocalClock_Type = DateAndTime
_Hh3cSysLocalClock_Object = MibScalar
hh3cSysLocalClock = _Hh3cSysLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 1),
    _Hh3cSysLocalClock_Type()
)
hh3cSysLocalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysLocalClock.setStatus("current")
_Hh3cSysSummerTime_ObjectIdentity = ObjectIdentity
hh3cSysSummerTime = _Hh3cSysSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2)
)


class _Hh3cSysSummerTimeEnable_Type(Integer32):
    """Custom type hh3cSysSummerTimeEnable based on Integer32"""
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


_Hh3cSysSummerTimeEnable_Type.__name__ = "Integer32"
_Hh3cSysSummerTimeEnable_Object = MibScalar
hh3cSysSummerTimeEnable = _Hh3cSysSummerTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 1),
    _Hh3cSysSummerTimeEnable_Type()
)
hh3cSysSummerTimeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeEnable.setStatus("current")


class _Hh3cSysSummerTimeZone_Type(DisplayString):
    """Custom type hh3cSysSummerTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysSummerTimeZone_Type.__name__ = "DisplayString"
_Hh3cSysSummerTimeZone_Object = MibScalar
hh3cSysSummerTimeZone = _Hh3cSysSummerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 2),
    _Hh3cSysSummerTimeZone_Type()
)
hh3cSysSummerTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeZone.setStatus("current")


class _Hh3cSysSummerTimeMethod_Type(Integer32):
    """Custom type hh3cSysSummerTimeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneOff", 1),
          ("repeating", 2))
    )


_Hh3cSysSummerTimeMethod_Type.__name__ = "Integer32"
_Hh3cSysSummerTimeMethod_Object = MibScalar
hh3cSysSummerTimeMethod = _Hh3cSysSummerTimeMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 3),
    _Hh3cSysSummerTimeMethod_Type()
)
hh3cSysSummerTimeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeMethod.setStatus("current")


class _Hh3cSysSummerTimeStart_Type(DateAndTime):
    """Custom type hh3cSysSummerTimeStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Hh3cSysSummerTimeStart_Type.__name__ = "DateAndTime"
_Hh3cSysSummerTimeStart_Object = MibScalar
hh3cSysSummerTimeStart = _Hh3cSysSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 4),
    _Hh3cSysSummerTimeStart_Type()
)
hh3cSysSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeStart.setStatus("current")


class _Hh3cSysSummerTimeEnd_Type(DateAndTime):
    """Custom type hh3cSysSummerTimeEnd based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Hh3cSysSummerTimeEnd_Type.__name__ = "DateAndTime"
_Hh3cSysSummerTimeEnd_Object = MibScalar
hh3cSysSummerTimeEnd = _Hh3cSysSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 5),
    _Hh3cSysSummerTimeEnd_Type()
)
hh3cSysSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeEnd.setStatus("current")


class _Hh3cSysSummerTimeOffset_Type(Integer32):
    """Custom type hh3cSysSummerTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_Hh3cSysSummerTimeOffset_Type.__name__ = "Integer32"
_Hh3cSysSummerTimeOffset_Object = MibScalar
hh3cSysSummerTimeOffset = _Hh3cSysSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 6),
    _Hh3cSysSummerTimeOffset_Type()
)
hh3cSysSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeOffset.setStatus("current")


class _Hh3cSysLocalClockString_Type(OctetString):
    """Custom type hh3cSysLocalClockString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 24),
    )


_Hh3cSysLocalClockString_Type.__name__ = "OctetString"
_Hh3cSysLocalClockString_Object = MibScalar
hh3cSysLocalClockString = _Hh3cSysLocalClockString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 3),
    _Hh3cSysLocalClockString_Type()
)
hh3cSysLocalClockString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysLocalClockString.setStatus("current")
_Hh3cSysCurrent_ObjectIdentity = ObjectIdentity
hh3cSysCurrent = _Hh3cSysCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2)
)
_Hh3cSysCurTable_Object = MibTable
hh3cSysCurTable = _Hh3cSysCurTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSysCurTable.setStatus("current")
_Hh3cSysCurEntry_Object = MibTableRow
hh3cSysCurEntry = _Hh3cSysCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1)
)
hh3cSysCurEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysCurEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysCurEntry.setStatus("current")


class _Hh3cSysCurEntPhysicalIndex_Type(Integer32):
    """Custom type hh3cSysCurEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCurEntPhysicalIndex_Type.__name__ = "Integer32"
_Hh3cSysCurEntPhysicalIndex_Object = MibTableColumn
hh3cSysCurEntPhysicalIndex = _Hh3cSysCurEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 1),
    _Hh3cSysCurEntPhysicalIndex_Type()
)
hh3cSysCurEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysCurEntPhysicalIndex.setStatus("current")


class _Hh3cSysCurCFGFileIndex_Type(Integer32):
    """Custom type hh3cSysCurCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCurCFGFileIndex_Type.__name__ = "Integer32"
_Hh3cSysCurCFGFileIndex_Object = MibTableColumn
hh3cSysCurCFGFileIndex = _Hh3cSysCurCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 2),
    _Hh3cSysCurCFGFileIndex_Type()
)
hh3cSysCurCFGFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurCFGFileIndex.setStatus("current")


class _Hh3cSysCurImageIndex_Type(Integer32):
    """Custom type hh3cSysCurImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCurImageIndex_Type.__name__ = "Integer32"
_Hh3cSysCurImageIndex_Object = MibTableColumn
hh3cSysCurImageIndex = _Hh3cSysCurImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 3),
    _Hh3cSysCurImageIndex_Type()
)
hh3cSysCurImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurImageIndex.setStatus("current")


class _Hh3cSysCurBtmFileName_Type(OctetString):
    """Custom type hh3cSysCurBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cSysCurBtmFileName_Type.__name__ = "OctetString"
_Hh3cSysCurBtmFileName_Object = MibTableColumn
hh3cSysCurBtmFileName = _Hh3cSysCurBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 4),
    _Hh3cSysCurBtmFileName_Type()
)
hh3cSysCurBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurBtmFileName.setStatus("current")


class _Hh3cSysCurUpdateBtmFileName_Type(OctetString):
    """Custom type hh3cSysCurUpdateBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cSysCurUpdateBtmFileName_Type.__name__ = "OctetString"
_Hh3cSysCurUpdateBtmFileName_Object = MibTableColumn
hh3cSysCurUpdateBtmFileName = _Hh3cSysCurUpdateBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 5),
    _Hh3cSysCurUpdateBtmFileName_Type()
)
hh3cSysCurUpdateBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurUpdateBtmFileName.setStatus("current")
_Hh3cSysReload_ObjectIdentity = ObjectIdentity
hh3cSysReload = _Hh3cSysReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3)
)


class _Hh3cSysReloadSchedule_Type(Integer32):
    """Custom type hh3cSysReloadSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadSchedule_Type.__name__ = "Integer32"
_Hh3cSysReloadSchedule_Object = MibScalar
hh3cSysReloadSchedule = _Hh3cSysReloadSchedule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 1),
    _Hh3cSysReloadSchedule_Type()
)
hh3cSysReloadSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysReloadSchedule.setStatus("current")


class _Hh3cSysReloadAction_Type(Integer32):
    """Custom type hh3cSysReloadAction based on Integer32"""
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
        *(("reloadUnavailable", 1),
          ("reloadOnSchedule", 2),
          ("reloadAtOnce", 3),
          ("reloadCancel", 4))
    )


_Hh3cSysReloadAction_Type.__name__ = "Integer32"
_Hh3cSysReloadAction_Object = MibScalar
hh3cSysReloadAction = _Hh3cSysReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 2),
    _Hh3cSysReloadAction_Type()
)
hh3cSysReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysReloadAction.setStatus("current")
_Hh3cSysReloadScheduleTable_Object = MibTable
hh3cSysReloadScheduleTable = _Hh3cSysReloadScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleTable.setStatus("current")
_Hh3cSysReloadScheduleEntry_Object = MibTableRow
hh3cSysReloadScheduleEntry = _Hh3cSysReloadScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1)
)
hh3cSysReloadScheduleEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleEntry.setStatus("current")


class _Hh3cSysReloadScheduleIndex_Type(Integer32):
    """Custom type hh3cSysReloadScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysReloadScheduleIndex_Type.__name__ = "Integer32"
_Hh3cSysReloadScheduleIndex_Object = MibTableColumn
hh3cSysReloadScheduleIndex = _Hh3cSysReloadScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 1),
    _Hh3cSysReloadScheduleIndex_Type()
)
hh3cSysReloadScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleIndex.setStatus("current")


class _Hh3cSysReloadEntity_Type(Integer32):
    """Custom type hh3cSysReloadEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadEntity_Type.__name__ = "Integer32"
_Hh3cSysReloadEntity_Object = MibTableColumn
hh3cSysReloadEntity = _Hh3cSysReloadEntity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 2),
    _Hh3cSysReloadEntity_Type()
)
hh3cSysReloadEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadEntity.setStatus("current")


class _Hh3cSysReloadCfgFile_Type(Integer32):
    """Custom type hh3cSysReloadCfgFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadCfgFile_Type.__name__ = "Integer32"
_Hh3cSysReloadCfgFile_Object = MibTableColumn
hh3cSysReloadCfgFile = _Hh3cSysReloadCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 3),
    _Hh3cSysReloadCfgFile_Type()
)
hh3cSysReloadCfgFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadCfgFile.setStatus("current")


class _Hh3cSysReloadImage_Type(Integer32):
    """Custom type hh3cSysReloadImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadImage_Type.__name__ = "Integer32"
_Hh3cSysReloadImage_Object = MibTableColumn
hh3cSysReloadImage = _Hh3cSysReloadImage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 4),
    _Hh3cSysReloadImage_Type()
)
hh3cSysReloadImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadImage.setStatus("current")


class _Hh3cSysReloadReason_Type(DisplayString):
    """Custom type hh3cSysReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysReloadReason_Type.__name__ = "DisplayString"
_Hh3cSysReloadReason_Object = MibTableColumn
hh3cSysReloadReason = _Hh3cSysReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 5),
    _Hh3cSysReloadReason_Type()
)
hh3cSysReloadReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadReason.setStatus("current")


class _Hh3cSysReloadScheduleTime_Type(DateAndTime):
    """Custom type hh3cSysReloadScheduleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Hh3cSysReloadScheduleTime_Type.__name__ = "DateAndTime"
_Hh3cSysReloadScheduleTime_Object = MibTableColumn
hh3cSysReloadScheduleTime = _Hh3cSysReloadScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 6),
    _Hh3cSysReloadScheduleTime_Type()
)
hh3cSysReloadScheduleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleTime.setStatus("current")
_Hh3cSysReloadRowStatus_Type = RowStatus
_Hh3cSysReloadRowStatus_Object = MibTableColumn
hh3cSysReloadRowStatus = _Hh3cSysReloadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 7),
    _Hh3cSysReloadRowStatus_Type()
)
hh3cSysReloadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadRowStatus.setStatus("current")
_Hh3cSysReloadScheduleTagList_Type = SnmpTagList
_Hh3cSysReloadScheduleTagList_Object = MibTableColumn
hh3cSysReloadScheduleTagList = _Hh3cSysReloadScheduleTagList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 8),
    _Hh3cSysReloadScheduleTagList_Type()
)
hh3cSysReloadScheduleTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleTagList.setStatus("current")
_Hh3cSysReloadTag_Type = SnmpTagValue
_Hh3cSysReloadTag_Object = MibScalar
hh3cSysReloadTag = _Hh3cSysReloadTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 4),
    _Hh3cSysReloadTag_Type()
)
hh3cSysReloadTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysReloadTag.setStatus("current")
_Hh3cSysImage_ObjectIdentity = ObjectIdentity
hh3cSysImage = _Hh3cSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4)
)


class _Hh3cSysImageNum_Type(Integer32):
    """Custom type hh3cSysImageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysImageNum_Type.__name__ = "Integer32"
_Hh3cSysImageNum_Object = MibScalar
hh3cSysImageNum = _Hh3cSysImageNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 1),
    _Hh3cSysImageNum_Type()
)
hh3cSysImageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageNum.setStatus("current")
_Hh3cSysImageTable_Object = MibTable
hh3cSysImageTable = _Hh3cSysImageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cSysImageTable.setStatus("current")
_Hh3cSysImageEntry_Object = MibTableRow
hh3cSysImageEntry = _Hh3cSysImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1)
)
hh3cSysImageEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysImageIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysImageEntry.setStatus("current")


class _Hh3cSysImageIndex_Type(Integer32):
    """Custom type hh3cSysImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysImageIndex_Type.__name__ = "Integer32"
_Hh3cSysImageIndex_Object = MibTableColumn
hh3cSysImageIndex = _Hh3cSysImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 1),
    _Hh3cSysImageIndex_Type()
)
hh3cSysImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysImageIndex.setStatus("current")


class _Hh3cSysImageName_Type(DisplayString):
    """Custom type hh3cSysImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysImageName_Type.__name__ = "DisplayString"
_Hh3cSysImageName_Object = MibTableColumn
hh3cSysImageName = _Hh3cSysImageName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 2),
    _Hh3cSysImageName_Type()
)
hh3cSysImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageName.setStatus("current")


class _Hh3cSysImageSize_Type(Integer32):
    """Custom type hh3cSysImageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysImageSize_Type.__name__ = "Integer32"
_Hh3cSysImageSize_Object = MibTableColumn
hh3cSysImageSize = _Hh3cSysImageSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 3),
    _Hh3cSysImageSize_Type()
)
hh3cSysImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageSize.setStatus("current")


class _Hh3cSysImageLocation_Type(DisplayString):
    """Custom type hh3cSysImageLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysImageLocation_Type.__name__ = "DisplayString"
_Hh3cSysImageLocation_Object = MibTableColumn
hh3cSysImageLocation = _Hh3cSysImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 4),
    _Hh3cSysImageLocation_Type()
)
hh3cSysImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageLocation.setStatus("current")


class _Hh3cSysImageType_Type(Integer32):
    """Custom type hh3cSysImageType based on Integer32"""
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
        *(("main", 1),
          ("backup", 2),
          ("none", 3),
          ("secure", 4),
          ("main-backup", 5),
          ("main-secure", 6),
          ("backup-secure", 7),
          ("main-backup-secure", 8))
    )


_Hh3cSysImageType_Type.__name__ = "Integer32"
_Hh3cSysImageType_Object = MibTableColumn
hh3cSysImageType = _Hh3cSysImageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 5),
    _Hh3cSysImageType_Type()
)
hh3cSysImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysImageType.setStatus("current")
_Hh3cSysCFGFile_ObjectIdentity = ObjectIdentity
hh3cSysCFGFile = _Hh3cSysCFGFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5)
)


class _Hh3cSysCFGFileNum_Type(Integer32):
    """Custom type hh3cSysCFGFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCFGFileNum_Type.__name__ = "Integer32"
_Hh3cSysCFGFileNum_Object = MibScalar
hh3cSysCFGFileNum = _Hh3cSysCFGFileNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 1),
    _Hh3cSysCFGFileNum_Type()
)
hh3cSysCFGFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileNum.setStatus("current")
_Hh3cSysCFGFileTable_Object = MibTable
hh3cSysCFGFileTable = _Hh3cSysCFGFileTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cSysCFGFileTable.setStatus("current")
_Hh3cSysCFGFileEntry_Object = MibTableRow
hh3cSysCFGFileEntry = _Hh3cSysCFGFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1)
)
hh3cSysCFGFileEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysCFGFileIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysCFGFileEntry.setStatus("current")


class _Hh3cSysCFGFileIndex_Type(Integer32):
    """Custom type hh3cSysCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCFGFileIndex_Type.__name__ = "Integer32"
_Hh3cSysCFGFileIndex_Object = MibTableColumn
hh3cSysCFGFileIndex = _Hh3cSysCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 1),
    _Hh3cSysCFGFileIndex_Type()
)
hh3cSysCFGFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysCFGFileIndex.setStatus("current")


class _Hh3cSysCFGFileName_Type(DisplayString):
    """Custom type hh3cSysCFGFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysCFGFileName_Type.__name__ = "DisplayString"
_Hh3cSysCFGFileName_Object = MibTableColumn
hh3cSysCFGFileName = _Hh3cSysCFGFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 2),
    _Hh3cSysCFGFileName_Type()
)
hh3cSysCFGFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileName.setStatus("current")


class _Hh3cSysCFGFileSize_Type(Integer32):
    """Custom type hh3cSysCFGFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysCFGFileSize_Type.__name__ = "Integer32"
_Hh3cSysCFGFileSize_Object = MibTableColumn
hh3cSysCFGFileSize = _Hh3cSysCFGFileSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 3),
    _Hh3cSysCFGFileSize_Type()
)
hh3cSysCFGFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileSize.setStatus("current")


class _Hh3cSysCFGFileLocation_Type(DisplayString):
    """Custom type hh3cSysCFGFileLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysCFGFileLocation_Type.__name__ = "DisplayString"
_Hh3cSysCFGFileLocation_Object = MibTableColumn
hh3cSysCFGFileLocation = _Hh3cSysCFGFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 4),
    _Hh3cSysCFGFileLocation_Type()
)
hh3cSysCFGFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileLocation.setStatus("current")
_Hh3cSysBtmFile_ObjectIdentity = ObjectIdentity
hh3cSysBtmFile = _Hh3cSysBtmFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6)
)
_Hh3cSysBtmFileLoad_ObjectIdentity = ObjectIdentity
hh3cSysBtmFileLoad = _Hh3cSysBtmFileLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 1)
)
_Hh3cSysBtmLoadMaxNumber_Type = Integer32
_Hh3cSysBtmLoadMaxNumber_Object = MibScalar
hh3cSysBtmLoadMaxNumber = _Hh3cSysBtmLoadMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 1, 1),
    _Hh3cSysBtmLoadMaxNumber_Type()
)
hh3cSysBtmLoadMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBtmLoadMaxNumber.setStatus("current")
_Hh3cSysBtmLoadTable_Object = MibTable
hh3cSysBtmLoadTable = _Hh3cSysBtmLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cSysBtmLoadTable.setStatus("current")
_Hh3cSysBtmLoadEntry_Object = MibTableRow
hh3cSysBtmLoadEntry = _Hh3cSysBtmLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1)
)
hh3cSysBtmLoadEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysBtmLoadIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysBtmLoadEntry.setStatus("current")


class _Hh3cSysBtmLoadIndex_Type(Integer32):
    """Custom type hh3cSysBtmLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysBtmLoadIndex_Type.__name__ = "Integer32"
_Hh3cSysBtmLoadIndex_Object = MibTableColumn
hh3cSysBtmLoadIndex = _Hh3cSysBtmLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 1),
    _Hh3cSysBtmLoadIndex_Type()
)
hh3cSysBtmLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysBtmLoadIndex.setStatus("current")


class _Hh3cSysBtmFileName_Type(OctetString):
    """Custom type hh3cSysBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cSysBtmFileName_Type.__name__ = "OctetString"
_Hh3cSysBtmFileName_Object = MibTableColumn
hh3cSysBtmFileName = _Hh3cSysBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 2),
    _Hh3cSysBtmFileName_Type()
)
hh3cSysBtmFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBtmFileName.setStatus("current")


class _Hh3cSysBtmFileType_Type(Integer32):
    """Custom type hh3cSysBtmFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("none", 2))
    )


_Hh3cSysBtmFileType_Type.__name__ = "Integer32"
_Hh3cSysBtmFileType_Object = MibTableColumn
hh3cSysBtmFileType = _Hh3cSysBtmFileType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 3),
    _Hh3cSysBtmFileType_Type()
)
hh3cSysBtmFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBtmFileType.setStatus("current")
_Hh3cSysBtmRowStatus_Type = RowStatus
_Hh3cSysBtmRowStatus_Object = MibTableColumn
hh3cSysBtmRowStatus = _Hh3cSysBtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 4),
    _Hh3cSysBtmRowStatus_Type()
)
hh3cSysBtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBtmRowStatus.setStatus("current")


class _Hh3cSysBtmErrorStatus_Type(Integer32):
    """Custom type hh3cSysBtmErrorStatus based on Integer32"""
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
        *(("invalidFile", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_Hh3cSysBtmErrorStatus_Type.__name__ = "Integer32"
_Hh3cSysBtmErrorStatus_Object = MibTableColumn
hh3cSysBtmErrorStatus = _Hh3cSysBtmErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 5),
    _Hh3cSysBtmErrorStatus_Type()
)
hh3cSysBtmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBtmErrorStatus.setStatus("current")
_Hh3cSysBtmLoadTime_Type = TimeTicks
_Hh3cSysBtmLoadTime_Object = MibTableColumn
hh3cSysBtmLoadTime = _Hh3cSysBtmLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 6),
    _Hh3cSysBtmLoadTime_Type()
)
hh3cSysBtmLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBtmLoadTime.setStatus("current")
_Hh3cSysPackage_ObjectIdentity = ObjectIdentity
hh3cSysPackage = _Hh3cSysPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7)
)


class _Hh3cSysPackageNum_Type(Integer32):
    """Custom type hh3cSysPackageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysPackageNum_Type.__name__ = "Integer32"
_Hh3cSysPackageNum_Object = MibScalar
hh3cSysPackageNum = _Hh3cSysPackageNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 1),
    _Hh3cSysPackageNum_Type()
)
hh3cSysPackageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageNum.setStatus("current")
_Hh3cSysPackageTable_Object = MibTable
hh3cSysPackageTable = _Hh3cSysPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hh3cSysPackageTable.setStatus("current")
_Hh3cSysPackageEntry_Object = MibTableRow
hh3cSysPackageEntry = _Hh3cSysPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1)
)
hh3cSysPackageEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysPackageIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysPackageEntry.setStatus("current")


class _Hh3cSysPackageIndex_Type(Integer32):
    """Custom type hh3cSysPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysPackageIndex_Type.__name__ = "Integer32"
_Hh3cSysPackageIndex_Object = MibTableColumn
hh3cSysPackageIndex = _Hh3cSysPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 1),
    _Hh3cSysPackageIndex_Type()
)
hh3cSysPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysPackageIndex.setStatus("current")


class _Hh3cSysPackageName_Type(DisplayString):
    """Custom type hh3cSysPackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysPackageName_Type.__name__ = "DisplayString"
_Hh3cSysPackageName_Object = MibTableColumn
hh3cSysPackageName = _Hh3cSysPackageName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 2),
    _Hh3cSysPackageName_Type()
)
hh3cSysPackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageName.setStatus("current")


class _Hh3cSysPackageSize_Type(Unsigned32):
    """Custom type hh3cSysPackageSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSysPackageSize_Type.__name__ = "Unsigned32"
_Hh3cSysPackageSize_Object = MibTableColumn
hh3cSysPackageSize = _Hh3cSysPackageSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 3),
    _Hh3cSysPackageSize_Type()
)
hh3cSysPackageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageSize.setStatus("current")


class _Hh3cSysPackageLocation_Type(DisplayString):
    """Custom type hh3cSysPackageLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysPackageLocation_Type.__name__ = "DisplayString"
_Hh3cSysPackageLocation_Object = MibTableColumn
hh3cSysPackageLocation = _Hh3cSysPackageLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 4),
    _Hh3cSysPackageLocation_Type()
)
hh3cSysPackageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageLocation.setStatus("current")


class _Hh3cSysPackageType_Type(Integer32):
    """Custom type hh3cSysPackageType based on Integer32"""
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
        *(("boot", 1),
          ("system", 2),
          ("feature", 3),
          ("patch", 4))
    )


_Hh3cSysPackageType_Type.__name__ = "Integer32"
_Hh3cSysPackageType_Object = MibTableColumn
hh3cSysPackageType = _Hh3cSysPackageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 5),
    _Hh3cSysPackageType_Type()
)
hh3cSysPackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageType.setStatus("current")


class _Hh3cSysPackageAttribute_Type(Integer32):
    """Custom type hh3cSysPackageAttribute based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3),
          ("primarySecondary", 4))
    )


_Hh3cSysPackageAttribute_Type.__name__ = "Integer32"
_Hh3cSysPackageAttribute_Object = MibTableColumn
hh3cSysPackageAttribute = _Hh3cSysPackageAttribute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 6),
    _Hh3cSysPackageAttribute_Type()
)
hh3cSysPackageAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysPackageAttribute.setStatus("current")


class _Hh3cSysPackageStatus_Type(Integer32):
    """Custom type hh3cSysPackageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hh3cSysPackageStatus_Type.__name__ = "Integer32"
_Hh3cSysPackageStatus_Object = MibTableColumn
hh3cSysPackageStatus = _Hh3cSysPackageStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 7),
    _Hh3cSysPackageStatus_Type()
)
hh3cSysPackageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageStatus.setStatus("current")


class _Hh3cSysPackageDescription_Type(DisplayString):
    """Custom type hh3cSysPackageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysPackageDescription_Type.__name__ = "DisplayString"
_Hh3cSysPackageDescription_Object = MibTableColumn
hh3cSysPackageDescription = _Hh3cSysPackageDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 8),
    _Hh3cSysPackageDescription_Type()
)
hh3cSysPackageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageDescription.setStatus("current")


class _Hh3cSysPackageFeature_Type(DisplayString):
    """Custom type hh3cSysPackageFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysPackageFeature_Type.__name__ = "DisplayString"
_Hh3cSysPackageFeature_Object = MibTableColumn
hh3cSysPackageFeature = _Hh3cSysPackageFeature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 9),
    _Hh3cSysPackageFeature_Type()
)
hh3cSysPackageFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageFeature.setStatus("current")


class _Hh3cSysPackageVersion_Type(DisplayString):
    """Custom type hh3cSysPackageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysPackageVersion_Type.__name__ = "DisplayString"
_Hh3cSysPackageVersion_Object = MibTableColumn
hh3cSysPackageVersion = _Hh3cSysPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 10),
    _Hh3cSysPackageVersion_Type()
)
hh3cSysPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageVersion.setStatus("current")


class _Hh3cSysPackageLoadAttribute_Type(Integer32):
    """Custom type hh3cSysPackageLoadAttribute based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3),
          ("primarySecondary", 4))
    )


_Hh3cSysPackageLoadAttribute_Type.__name__ = "Integer32"
_Hh3cSysPackageLoadAttribute_Object = MibTableColumn
hh3cSysPackageLoadAttribute = _Hh3cSysPackageLoadAttribute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 11),
    _Hh3cSysPackageLoadAttribute_Type()
)
hh3cSysPackageLoadAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysPackageLoadAttribute.setStatus("current")


class _Hh3cSysPackageModel_Type(DisplayString):
    """Custom type hh3cSysPackageModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cSysPackageModel_Type.__name__ = "DisplayString"
_Hh3cSysPackageModel_Object = MibTableColumn
hh3cSysPackageModel = _Hh3cSysPackageModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 2, 1, 12),
    _Hh3cSysPackageModel_Type()
)
hh3cSysPackageModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageModel.setStatus("current")


class _Hh3cSysPackageOperateEntryLimit_Type(Integer32):
    """Custom type hh3cSysPackageOperateEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysPackageOperateEntryLimit_Type.__name__ = "Integer32"
_Hh3cSysPackageOperateEntryLimit_Object = MibScalar
hh3cSysPackageOperateEntryLimit = _Hh3cSysPackageOperateEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 3),
    _Hh3cSysPackageOperateEntryLimit_Type()
)
hh3cSysPackageOperateEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysPackageOperateEntryLimit.setStatus("current")
_Hh3cSysPackageOperateTable_Object = MibTable
hh3cSysPackageOperateTable = _Hh3cSysPackageOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4)
)
if mibBuilder.loadTexts:
    hh3cSysPackageOperateTable.setStatus("current")
_Hh3cSysPackageOperateEntry_Object = MibTableRow
hh3cSysPackageOperateEntry = _Hh3cSysPackageOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4, 1)
)
hh3cSysPackageOperateEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysPackageOperateIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysPackageOperateEntry.setStatus("current")


class _Hh3cSysPackageOperateIndex_Type(Integer32):
    """Custom type hh3cSysPackageOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysPackageOperateIndex_Type.__name__ = "Integer32"
_Hh3cSysPackageOperateIndex_Object = MibTableColumn
hh3cSysPackageOperateIndex = _Hh3cSysPackageOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4, 1, 1),
    _Hh3cSysPackageOperateIndex_Type()
)
hh3cSysPackageOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysPackageOperateIndex.setStatus("current")


class _Hh3cSysPackageOperatePackIndex_Type(Integer32):
    """Custom type hh3cSysPackageOperatePackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysPackageOperatePackIndex_Type.__name__ = "Integer32"
_Hh3cSysPackageOperatePackIndex_Object = MibTableColumn
hh3cSysPackageOperatePackIndex = _Hh3cSysPackageOperatePackIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4, 1, 2),
    _Hh3cSysPackageOperatePackIndex_Type()
)
hh3cSysPackageOperatePackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysPackageOperatePackIndex.setStatus("current")


class _Hh3cSysPackageOperateStatus_Type(Integer32):
    """Custom type hh3cSysPackageOperateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hh3cSysPackageOperateStatus_Type.__name__ = "Integer32"
_Hh3cSysPackageOperateStatus_Object = MibTableColumn
hh3cSysPackageOperateStatus = _Hh3cSysPackageOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4, 1, 3),
    _Hh3cSysPackageOperateStatus_Type()
)
hh3cSysPackageOperateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysPackageOperateStatus.setStatus("current")
_Hh3cSysPackageOperateRowStatus_Type = RowStatus
_Hh3cSysPackageOperateRowStatus_Object = MibTableColumn
hh3cSysPackageOperateRowStatus = _Hh3cSysPackageOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4, 1, 4),
    _Hh3cSysPackageOperateRowStatus_Type()
)
hh3cSysPackageOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysPackageOperateRowStatus.setStatus("current")


class _Hh3cSysPackageOperateResult_Type(Integer32):
    """Custom type hh3cSysPackageOperateResult based on Integer32"""
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
        *(("opInProgress", 1),
          ("opSuccess", 2),
          ("opUnknownFailure", 3),
          ("opInvalidFile", 4),
          ("opNotSupport", 5))
    )


_Hh3cSysPackageOperateResult_Type.__name__ = "Integer32"
_Hh3cSysPackageOperateResult_Object = MibTableColumn
hh3cSysPackageOperateResult = _Hh3cSysPackageOperateResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 7, 4, 1, 5),
    _Hh3cSysPackageOperateResult_Type()
)
hh3cSysPackageOperateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysPackageOperateResult.setStatus("current")
_Hh3cSysIpeFile_ObjectIdentity = ObjectIdentity
hh3cSysIpeFile = _Hh3cSysIpeFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8)
)


class _Hh3cSysIpeFileNum_Type(Integer32):
    """Custom type hh3cSysIpeFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysIpeFileNum_Type.__name__ = "Integer32"
_Hh3cSysIpeFileNum_Object = MibScalar
hh3cSysIpeFileNum = _Hh3cSysIpeFileNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 1),
    _Hh3cSysIpeFileNum_Type()
)
hh3cSysIpeFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpeFileNum.setStatus("current")
_Hh3cSysIpeFileTable_Object = MibTable
hh3cSysIpeFileTable = _Hh3cSysIpeFileTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    hh3cSysIpeFileTable.setStatus("current")
_Hh3cSysIpeFileEntry_Object = MibTableRow
hh3cSysIpeFileEntry = _Hh3cSysIpeFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2, 1)
)
hh3cSysIpeFileEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysIpeFileIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysIpeFileEntry.setStatus("current")


class _Hh3cSysIpeFileIndex_Type(Integer32):
    """Custom type hh3cSysIpeFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysIpeFileIndex_Type.__name__ = "Integer32"
_Hh3cSysIpeFileIndex_Object = MibTableColumn
hh3cSysIpeFileIndex = _Hh3cSysIpeFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2, 1, 1),
    _Hh3cSysIpeFileIndex_Type()
)
hh3cSysIpeFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysIpeFileIndex.setStatus("current")


class _Hh3cSysIpeFileName_Type(DisplayString):
    """Custom type hh3cSysIpeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysIpeFileName_Type.__name__ = "DisplayString"
_Hh3cSysIpeFileName_Object = MibTableColumn
hh3cSysIpeFileName = _Hh3cSysIpeFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2, 1, 2),
    _Hh3cSysIpeFileName_Type()
)
hh3cSysIpeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpeFileName.setStatus("current")


class _Hh3cSysIpeFileSize_Type(Unsigned32):
    """Custom type hh3cSysIpeFileSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSysIpeFileSize_Type.__name__ = "Unsigned32"
_Hh3cSysIpeFileSize_Object = MibTableColumn
hh3cSysIpeFileSize = _Hh3cSysIpeFileSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2, 1, 3),
    _Hh3cSysIpeFileSize_Type()
)
hh3cSysIpeFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpeFileSize.setStatus("current")


class _Hh3cSysIpeFileLocation_Type(DisplayString):
    """Custom type hh3cSysIpeFileLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysIpeFileLocation_Type.__name__ = "DisplayString"
_Hh3cSysIpeFileLocation_Object = MibTableColumn
hh3cSysIpeFileLocation = _Hh3cSysIpeFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2, 1, 4),
    _Hh3cSysIpeFileLocation_Type()
)
hh3cSysIpeFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpeFileLocation.setStatus("current")
_Hh3cSysIpeFileModel_Type = SnmpTagList
_Hh3cSysIpeFileModel_Object = MibTableColumn
hh3cSysIpeFileModel = _Hh3cSysIpeFileModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 2, 1, 5),
    _Hh3cSysIpeFileModel_Type()
)
hh3cSysIpeFileModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpeFileModel.setStatus("current")
_Hh3cSysIpePackageTable_Object = MibTable
hh3cSysIpePackageTable = _Hh3cSysIpePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cSysIpePackageTable.setStatus("current")
_Hh3cSysIpePackageEntry_Object = MibTableRow
hh3cSysIpePackageEntry = _Hh3cSysIpePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1)
)
hh3cSysIpePackageEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysIpeFileIndex"),
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysIpePackageIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysIpePackageEntry.setStatus("current")


class _Hh3cSysIpePackageIndex_Type(Integer32):
    """Custom type hh3cSysIpePackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysIpePackageIndex_Type.__name__ = "Integer32"
_Hh3cSysIpePackageIndex_Object = MibTableColumn
hh3cSysIpePackageIndex = _Hh3cSysIpePackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 1),
    _Hh3cSysIpePackageIndex_Type()
)
hh3cSysIpePackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysIpePackageIndex.setStatus("current")


class _Hh3cSysIpePackageName_Type(DisplayString):
    """Custom type hh3cSysIpePackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysIpePackageName_Type.__name__ = "DisplayString"
_Hh3cSysIpePackageName_Object = MibTableColumn
hh3cSysIpePackageName = _Hh3cSysIpePackageName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 2),
    _Hh3cSysIpePackageName_Type()
)
hh3cSysIpePackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageName.setStatus("current")


class _Hh3cSysIpePackageSize_Type(Unsigned32):
    """Custom type hh3cSysIpePackageSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSysIpePackageSize_Type.__name__ = "Unsigned32"
_Hh3cSysIpePackageSize_Object = MibTableColumn
hh3cSysIpePackageSize = _Hh3cSysIpePackageSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 3),
    _Hh3cSysIpePackageSize_Type()
)
hh3cSysIpePackageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageSize.setStatus("current")


class _Hh3cSysIpePackageType_Type(Integer32):
    """Custom type hh3cSysIpePackageType based on Integer32"""
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
        *(("boot", 1),
          ("system", 2),
          ("feature", 3),
          ("patch", 4))
    )


_Hh3cSysIpePackageType_Type.__name__ = "Integer32"
_Hh3cSysIpePackageType_Object = MibTableColumn
hh3cSysIpePackageType = _Hh3cSysIpePackageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 4),
    _Hh3cSysIpePackageType_Type()
)
hh3cSysIpePackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageType.setStatus("current")


class _Hh3cSysIpePackageDescription_Type(DisplayString):
    """Custom type hh3cSysIpePackageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysIpePackageDescription_Type.__name__ = "DisplayString"
_Hh3cSysIpePackageDescription_Object = MibTableColumn
hh3cSysIpePackageDescription = _Hh3cSysIpePackageDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 5),
    _Hh3cSysIpePackageDescription_Type()
)
hh3cSysIpePackageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageDescription.setStatus("current")


class _Hh3cSysIpePackageFeature_Type(DisplayString):
    """Custom type hh3cSysIpePackageFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysIpePackageFeature_Type.__name__ = "DisplayString"
_Hh3cSysIpePackageFeature_Object = MibTableColumn
hh3cSysIpePackageFeature = _Hh3cSysIpePackageFeature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 6),
    _Hh3cSysIpePackageFeature_Type()
)
hh3cSysIpePackageFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageFeature.setStatus("current")


class _Hh3cSysIpePackageVersion_Type(DisplayString):
    """Custom type hh3cSysIpePackageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysIpePackageVersion_Type.__name__ = "DisplayString"
_Hh3cSysIpePackageVersion_Object = MibTableColumn
hh3cSysIpePackageVersion = _Hh3cSysIpePackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 7),
    _Hh3cSysIpePackageVersion_Type()
)
hh3cSysIpePackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageVersion.setStatus("current")


class _Hh3cSysIpePackageModel_Type(DisplayString):
    """Custom type hh3cSysIpePackageModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cSysIpePackageModel_Type.__name__ = "DisplayString"
_Hh3cSysIpePackageModel_Object = MibTableColumn
hh3cSysIpePackageModel = _Hh3cSysIpePackageModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 3, 1, 8),
    _Hh3cSysIpePackageModel_Type()
)
hh3cSysIpePackageModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpePackageModel.setStatus("current")
_Hh3cSysIpeFileOperateTable_Object = MibTable
hh3cSysIpeFileOperateTable = _Hh3cSysIpeFileOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4)
)
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateTable.setStatus("current")
_Hh3cSysIpeFileOperateEntry_Object = MibTableRow
hh3cSysIpeFileOperateEntry = _Hh3cSysIpeFileOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4, 1)
)
hh3cSysIpeFileOperateEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysIpeFileOperateIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateEntry.setStatus("current")


class _Hh3cSysIpeFileOperateIndex_Type(Integer32):
    """Custom type hh3cSysIpeFileOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysIpeFileOperateIndex_Type.__name__ = "Integer32"
_Hh3cSysIpeFileOperateIndex_Object = MibTableColumn
hh3cSysIpeFileOperateIndex = _Hh3cSysIpeFileOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4, 1, 1),
    _Hh3cSysIpeFileOperateIndex_Type()
)
hh3cSysIpeFileOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateIndex.setStatus("current")


class _Hh3cSysIpeFileOperateFileIndex_Type(Integer32):
    """Custom type hh3cSysIpeFileOperateFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysIpeFileOperateFileIndex_Type.__name__ = "Integer32"
_Hh3cSysIpeFileOperateFileIndex_Object = MibTableColumn
hh3cSysIpeFileOperateFileIndex = _Hh3cSysIpeFileOperateFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4, 1, 2),
    _Hh3cSysIpeFileOperateFileIndex_Type()
)
hh3cSysIpeFileOperateFileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateFileIndex.setStatus("current")


class _Hh3cSysIpeFileOperateAttribute_Type(Integer32):
    """Custom type hh3cSysIpeFileOperateAttribute based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3),
          ("primarySecondary", 4))
    )


_Hh3cSysIpeFileOperateAttribute_Type.__name__ = "Integer32"
_Hh3cSysIpeFileOperateAttribute_Object = MibTableColumn
hh3cSysIpeFileOperateAttribute = _Hh3cSysIpeFileOperateAttribute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4, 1, 3),
    _Hh3cSysIpeFileOperateAttribute_Type()
)
hh3cSysIpeFileOperateAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateAttribute.setStatus("current")
_Hh3cSysIpeFileOperateRowStatus_Type = RowStatus
_Hh3cSysIpeFileOperateRowStatus_Object = MibTableColumn
hh3cSysIpeFileOperateRowStatus = _Hh3cSysIpeFileOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4, 1, 4),
    _Hh3cSysIpeFileOperateRowStatus_Type()
)
hh3cSysIpeFileOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateRowStatus.setStatus("current")


class _Hh3cSysIpeFileOperateResult_Type(Integer32):
    """Custom type hh3cSysIpeFileOperateResult based on Integer32"""
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
        *(("opInProgress", 1),
          ("opSuccess", 2),
          ("opUnknownFailure", 3),
          ("opInvalidFile", 4),
          ("opDeviceFull", 5),
          ("opFileOpenError", 6))
    )


_Hh3cSysIpeFileOperateResult_Type.__name__ = "Integer32"
_Hh3cSysIpeFileOperateResult_Object = MibTableColumn
hh3cSysIpeFileOperateResult = _Hh3cSysIpeFileOperateResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 8, 4, 1, 5),
    _Hh3cSysIpeFileOperateResult_Type()
)
hh3cSysIpeFileOperateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysIpeFileOperateResult.setStatus("current")
_Hh3cSysSetBootImage_ObjectIdentity = ObjectIdentity
hh3cSysSetBootImage = _Hh3cSysSetBootImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9)
)
_Hh3cSysSetBootImageOp_ObjectIdentity = ObjectIdentity
hh3cSysSetBootImageOp = _Hh3cSysSetBootImageOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 1)
)


class _Hh3cSysSetBootImageAction_Type(Integer32):
    """Custom type hh3cSysSetBootImageAction based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("done", 2),
          ("bootLoadPrimary", 3),
          ("bootLoadSecondary", 4),
          ("bootLoadPrimarySecondary", 5),
          ("bootPrimary", 6),
          ("bootSecondary", 7),
          ("bootPrimarySecondary", 8),
          ("loadPrimary", 9),
          ("loadSecondary", 10),
          ("loadPrimarySecondary", 11))
    )


_Hh3cSysSetBootImageAction_Type.__name__ = "Integer32"
_Hh3cSysSetBootImageAction_Object = MibScalar
hh3cSysSetBootImageAction = _Hh3cSysSetBootImageAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 1, 1),
    _Hh3cSysSetBootImageAction_Type()
)
hh3cSysSetBootImageAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageAction.setStatus("current")


class _Hh3cSysSetBootImageFileOverWrite_Type(TruthValue):
    """Custom type hh3cSysSetBootImageFileOverWrite based on TruthValue"""
    defaultValue = 2


_Hh3cSysSetBootImageFileOverWrite_Type.__name__ = "TruthValue"
_Hh3cSysSetBootImageFileOverWrite_Object = MibScalar
hh3cSysSetBootImageFileOverWrite = _Hh3cSysSetBootImageFileOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 1, 2),
    _Hh3cSysSetBootImageFileOverWrite_Type()
)
hh3cSysSetBootImageFileOverWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageFileOverWrite.setStatus("current")


class _Hh3cSysSetBootImageRemoveIpeFile_Type(TruthValue):
    """Custom type hh3cSysSetBootImageRemoveIpeFile based on TruthValue"""
    defaultValue = 2


_Hh3cSysSetBootImageRemoveIpeFile_Type.__name__ = "TruthValue"
_Hh3cSysSetBootImageRemoveIpeFile_Object = MibScalar
hh3cSysSetBootImageRemoveIpeFile = _Hh3cSysSetBootImageRemoveIpeFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 1, 3),
    _Hh3cSysSetBootImageRemoveIpeFile_Type()
)
hh3cSysSetBootImageRemoveIpeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageRemoveIpeFile.setStatus("current")


class _Hh3cSysSetBootImageStatus_Type(Integer32):
    """Custom type hh3cSysSetBootImageStatus based on Integer32"""
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
        *(("none", 1),
          ("doing", 2),
          ("success", 3),
          ("failed", 4))
    )


_Hh3cSysSetBootImageStatus_Type.__name__ = "Integer32"
_Hh3cSysSetBootImageStatus_Object = MibScalar
hh3cSysSetBootImageStatus = _Hh3cSysSetBootImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 1, 4),
    _Hh3cSysSetBootImageStatus_Type()
)
hh3cSysSetBootImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageStatus.setStatus("current")


class _Hh3cSysSetBootImageFailedReason_Type(DisplayString):
    """Custom type hh3cSysSetBootImageFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysSetBootImageFailedReason_Type.__name__ = "DisplayString"
_Hh3cSysSetBootImageFailedReason_Object = MibScalar
hh3cSysSetBootImageFailedReason = _Hh3cSysSetBootImageFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 1, 5),
    _Hh3cSysSetBootImageFailedReason_Type()
)
hh3cSysSetBootImageFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageFailedReason.setStatus("current")
_Hh3cSysBootPackageTable_Object = MibTable
hh3cSysBootPackageTable = _Hh3cSysBootPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hh3cSysBootPackageTable.setStatus("current")
_Hh3cSysBootPackageEntry_Object = MibTableRow
hh3cSysBootPackageEntry = _Hh3cSysBootPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 2, 1)
)
hh3cSysBootPackageEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysBootPackageIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysBootPackageEntry.setStatus("current")


class _Hh3cSysBootPackageIndex_Type(Integer32):
    """Custom type hh3cSysBootPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysBootPackageIndex_Type.__name__ = "Integer32"
_Hh3cSysBootPackageIndex_Object = MibTableColumn
hh3cSysBootPackageIndex = _Hh3cSysBootPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 2, 1, 1),
    _Hh3cSysBootPackageIndex_Type()
)
hh3cSysBootPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysBootPackageIndex.setStatus("current")
_Hh3cSysBootPackageRowStatus_Type = RowStatus
_Hh3cSysBootPackageRowStatus_Object = MibTableColumn
hh3cSysBootPackageRowStatus = _Hh3cSysBootPackageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 2, 1, 2),
    _Hh3cSysBootPackageRowStatus_Type()
)
hh3cSysBootPackageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBootPackageRowStatus.setStatus("current")
_Hh3cSysBootIpeTable_Object = MibTable
hh3cSysBootIpeTable = _Hh3cSysBootIpeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 3)
)
if mibBuilder.loadTexts:
    hh3cSysBootIpeTable.setStatus("current")
_Hh3cSysBootIpeEntry_Object = MibTableRow
hh3cSysBootIpeEntry = _Hh3cSysBootIpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 3, 1)
)
hh3cSysBootIpeEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysBootIpeIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysBootIpeEntry.setStatus("current")


class _Hh3cSysBootIpeIndex_Type(Integer32):
    """Custom type hh3cSysBootIpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysBootIpeIndex_Type.__name__ = "Integer32"
_Hh3cSysBootIpeIndex_Object = MibTableColumn
hh3cSysBootIpeIndex = _Hh3cSysBootIpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 3, 1, 1),
    _Hh3cSysBootIpeIndex_Type()
)
hh3cSysBootIpeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysBootIpeIndex.setStatus("current")
_Hh3cSysBootIpeRowStatus_Type = RowStatus
_Hh3cSysBootIpeRowStatus_Object = MibTableColumn
hh3cSysBootIpeRowStatus = _Hh3cSysBootIpeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 3, 1, 2),
    _Hh3cSysBootIpeRowStatus_Type()
)
hh3cSysBootIpeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBootIpeRowStatus.setStatus("current")
_Hh3cSysSetBootImageResultTable_Object = MibTable
hh3cSysSetBootImageResultTable = _Hh3cSysSetBootImageResultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 4)
)
if mibBuilder.loadTexts:
    hh3cSysSetBootImageResultTable.setStatus("current")
_Hh3cSysSetBootImageResultEntry_Object = MibTableRow
hh3cSysSetBootImageResultEntry = _Hh3cSysSetBootImageResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 4, 1)
)
hh3cSysSetBootImageResultEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysSetBootImageResultIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysSetBootImageResultEntry.setStatus("current")


class _Hh3cSysSetBootImageResultIndex_Type(Integer32):
    """Custom type hh3cSysSetBootImageResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSysSetBootImageResultIndex_Type.__name__ = "Integer32"
_Hh3cSysSetBootImageResultIndex_Object = MibTableColumn
hh3cSysSetBootImageResultIndex = _Hh3cSysSetBootImageResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 4, 1, 1),
    _Hh3cSysSetBootImageResultIndex_Type()
)
hh3cSysSetBootImageResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageResultIndex.setStatus("current")


class _Hh3cSysSetBootImageResultStatusOfEachCard_Type(Integer32):
    """Custom type hh3cSysSetBootImageResultStatusOfEachCard based on Integer32"""
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
        *(("none", 1),
          ("doing", 2),
          ("success", 3),
          ("failed", 4))
    )


_Hh3cSysSetBootImageResultStatusOfEachCard_Type.__name__ = "Integer32"
_Hh3cSysSetBootImageResultStatusOfEachCard_Object = MibTableColumn
hh3cSysSetBootImageResultStatusOfEachCard = _Hh3cSysSetBootImageResultStatusOfEachCard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 4, 1, 2),
    _Hh3cSysSetBootImageResultStatusOfEachCard_Type()
)
hh3cSysSetBootImageResultStatusOfEachCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageResultStatusOfEachCard.setStatus("current")


class _Hh3cSysSetBootImageFailedReasonOfEachCard_Type(DisplayString):
    """Custom type hh3cSysSetBootImageFailedReasonOfEachCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysSetBootImageFailedReasonOfEachCard_Type.__name__ = "DisplayString"
_Hh3cSysSetBootImageFailedReasonOfEachCard_Object = MibTableColumn
hh3cSysSetBootImageFailedReasonOfEachCard = _Hh3cSysSetBootImageFailedReasonOfEachCard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 9, 4, 1, 3),
    _Hh3cSysSetBootImageFailedReasonOfEachCard_Type()
)
hh3cSysSetBootImageFailedReasonOfEachCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSetBootImageFailedReasonOfEachCard.setStatus("current")
_Hh3cSystemManMIBNotifications_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBNotifications = _Hh3cSystemManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2)
)
_Hh3cSystemManMIBConformance_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBConformance = _Hh3cSystemManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3)
)
_Hh3cSystemManMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBCompliances = _Hh3cSystemManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 1)
)
_Hh3cSystemManMIBGroups_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBGroups = _Hh3cSystemManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2)
)

# Managed Objects groups

hh3cSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 1)
)
hh3cSysClockGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysLocalClock"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeEnable"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeZone"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeMethod"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeStart"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeEnd"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeOffset"))
)
if mibBuilder.loadTexts:
    hh3cSysClockGroup.setStatus("current")

hh3cSysReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 2)
)
hh3cSysReloadGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysReloadSchedule"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadAction"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadImage"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadCfgFile"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadReason"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleTagList"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadTag"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleTime"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadEntity"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cSysReloadGroup.setStatus("current")

hh3cSysImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 3)
)
hh3cSysImageGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysImageNum"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageSize"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageLocation"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageType"))
)
if mibBuilder.loadTexts:
    hh3cSysImageGroup.setStatus("current")

hh3cSysCFGFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 4)
)
hh3cSysCFGFileGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileNum"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileSize"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileLocation"))
)
if mibBuilder.loadTexts:
    hh3cSysCFGFileGroup.setStatus("current")

hh3cSysCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 5)
)
hh3cSysCurGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysCurCFGFileIndex"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCurImageIndex"))
)
if mibBuilder.loadTexts:
    hh3cSysCurGroup.setStatus("current")

hh3cSystemBtmLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 7)
)
hh3cSystemBtmLoadGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysCurBtmFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCurUpdateBtmFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmLoadMaxNumber"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmFileType"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmRowStatus"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmErrorStatus"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmLoadTime"))
)
if mibBuilder.loadTexts:
    hh3cSystemBtmLoadGroup.setStatus("current")


# Notification objects

hh3cSysClockChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2, 1)
)
hh3cSysClockChangedNotification.setObjects(
    ("HH3C-SYS-MAN-MIB", "hh3cSysLocalClock")
)
if mibBuilder.loadTexts:
    hh3cSysClockChangedNotification.setStatus(
        "current"
    )

hh3cSysReloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2, 2)
)
hh3cSysReloadNotification.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysReloadImage"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadCfgFile"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadReason"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleTime"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadAction"))
)
if mibBuilder.loadTexts:
    hh3cSysReloadNotification.setStatus(
        "current"
    )

hh3cSysStartUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2, 3)
)
hh3cSysStartUpNotification.setObjects(
    ("HH3C-SYS-MAN-MIB", "hh3cSysImageType")
)
if mibBuilder.loadTexts:
    hh3cSysStartUpNotification.setStatus(
        "current"
    )


# Notifications groups

hh3cSystemManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 6)
)
hh3cSystemManNotificationGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysClockChangedNotification"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadNotification"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysStartUpNotification"))
)
if mibBuilder.loadTexts:
    hh3cSystemManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cSystemManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 1, 1)
)
hh3cSystemManMIBCompliance.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysClockGroup"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadGroup"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageGroup"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileGroup"),
        ("HH3C-SYS-MAN-MIB", "hh3cSystemManNotificationGroup"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCurGroup"),
        ("HH3C-SYS-MAN-MIB", "hh3cSystemBtmLoadGroup"))
)
if mibBuilder.loadTexts:
    hh3cSystemManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SYS-MAN-MIB",
    **{"hh3cSystemMan": hh3cSystemMan,
       "hh3cSystemManMIBObjects": hh3cSystemManMIBObjects,
       "hh3cSysClock": hh3cSysClock,
       "hh3cSysLocalClock": hh3cSysLocalClock,
       "hh3cSysSummerTime": hh3cSysSummerTime,
       "hh3cSysSummerTimeEnable": hh3cSysSummerTimeEnable,
       "hh3cSysSummerTimeZone": hh3cSysSummerTimeZone,
       "hh3cSysSummerTimeMethod": hh3cSysSummerTimeMethod,
       "hh3cSysSummerTimeStart": hh3cSysSummerTimeStart,
       "hh3cSysSummerTimeEnd": hh3cSysSummerTimeEnd,
       "hh3cSysSummerTimeOffset": hh3cSysSummerTimeOffset,
       "hh3cSysLocalClockString": hh3cSysLocalClockString,
       "hh3cSysCurrent": hh3cSysCurrent,
       "hh3cSysCurTable": hh3cSysCurTable,
       "hh3cSysCurEntry": hh3cSysCurEntry,
       "hh3cSysCurEntPhysicalIndex": hh3cSysCurEntPhysicalIndex,
       "hh3cSysCurCFGFileIndex": hh3cSysCurCFGFileIndex,
       "hh3cSysCurImageIndex": hh3cSysCurImageIndex,
       "hh3cSysCurBtmFileName": hh3cSysCurBtmFileName,
       "hh3cSysCurUpdateBtmFileName": hh3cSysCurUpdateBtmFileName,
       "hh3cSysReload": hh3cSysReload,
       "hh3cSysReloadSchedule": hh3cSysReloadSchedule,
       "hh3cSysReloadAction": hh3cSysReloadAction,
       "hh3cSysReloadScheduleTable": hh3cSysReloadScheduleTable,
       "hh3cSysReloadScheduleEntry": hh3cSysReloadScheduleEntry,
       "hh3cSysReloadScheduleIndex": hh3cSysReloadScheduleIndex,
       "hh3cSysReloadEntity": hh3cSysReloadEntity,
       "hh3cSysReloadCfgFile": hh3cSysReloadCfgFile,
       "hh3cSysReloadImage": hh3cSysReloadImage,
       "hh3cSysReloadReason": hh3cSysReloadReason,
       "hh3cSysReloadScheduleTime": hh3cSysReloadScheduleTime,
       "hh3cSysReloadRowStatus": hh3cSysReloadRowStatus,
       "hh3cSysReloadScheduleTagList": hh3cSysReloadScheduleTagList,
       "hh3cSysReloadTag": hh3cSysReloadTag,
       "hh3cSysImage": hh3cSysImage,
       "hh3cSysImageNum": hh3cSysImageNum,
       "hh3cSysImageTable": hh3cSysImageTable,
       "hh3cSysImageEntry": hh3cSysImageEntry,
       "hh3cSysImageIndex": hh3cSysImageIndex,
       "hh3cSysImageName": hh3cSysImageName,
       "hh3cSysImageSize": hh3cSysImageSize,
       "hh3cSysImageLocation": hh3cSysImageLocation,
       "hh3cSysImageType": hh3cSysImageType,
       "hh3cSysCFGFile": hh3cSysCFGFile,
       "hh3cSysCFGFileNum": hh3cSysCFGFileNum,
       "hh3cSysCFGFileTable": hh3cSysCFGFileTable,
       "hh3cSysCFGFileEntry": hh3cSysCFGFileEntry,
       "hh3cSysCFGFileIndex": hh3cSysCFGFileIndex,
       "hh3cSysCFGFileName": hh3cSysCFGFileName,
       "hh3cSysCFGFileSize": hh3cSysCFGFileSize,
       "hh3cSysCFGFileLocation": hh3cSysCFGFileLocation,
       "hh3cSysBtmFile": hh3cSysBtmFile,
       "hh3cSysBtmFileLoad": hh3cSysBtmFileLoad,
       "hh3cSysBtmLoadMaxNumber": hh3cSysBtmLoadMaxNumber,
       "hh3cSysBtmLoadTable": hh3cSysBtmLoadTable,
       "hh3cSysBtmLoadEntry": hh3cSysBtmLoadEntry,
       "hh3cSysBtmLoadIndex": hh3cSysBtmLoadIndex,
       "hh3cSysBtmFileName": hh3cSysBtmFileName,
       "hh3cSysBtmFileType": hh3cSysBtmFileType,
       "hh3cSysBtmRowStatus": hh3cSysBtmRowStatus,
       "hh3cSysBtmErrorStatus": hh3cSysBtmErrorStatus,
       "hh3cSysBtmLoadTime": hh3cSysBtmLoadTime,
       "hh3cSysPackage": hh3cSysPackage,
       "hh3cSysPackageNum": hh3cSysPackageNum,
       "hh3cSysPackageTable": hh3cSysPackageTable,
       "hh3cSysPackageEntry": hh3cSysPackageEntry,
       "hh3cSysPackageIndex": hh3cSysPackageIndex,
       "hh3cSysPackageName": hh3cSysPackageName,
       "hh3cSysPackageSize": hh3cSysPackageSize,
       "hh3cSysPackageLocation": hh3cSysPackageLocation,
       "hh3cSysPackageType": hh3cSysPackageType,
       "hh3cSysPackageAttribute": hh3cSysPackageAttribute,
       "hh3cSysPackageStatus": hh3cSysPackageStatus,
       "hh3cSysPackageDescription": hh3cSysPackageDescription,
       "hh3cSysPackageFeature": hh3cSysPackageFeature,
       "hh3cSysPackageVersion": hh3cSysPackageVersion,
       "hh3cSysPackageLoadAttribute": hh3cSysPackageLoadAttribute,
       "hh3cSysPackageModel": hh3cSysPackageModel,
       "hh3cSysPackageOperateEntryLimit": hh3cSysPackageOperateEntryLimit,
       "hh3cSysPackageOperateTable": hh3cSysPackageOperateTable,
       "hh3cSysPackageOperateEntry": hh3cSysPackageOperateEntry,
       "hh3cSysPackageOperateIndex": hh3cSysPackageOperateIndex,
       "hh3cSysPackageOperatePackIndex": hh3cSysPackageOperatePackIndex,
       "hh3cSysPackageOperateStatus": hh3cSysPackageOperateStatus,
       "hh3cSysPackageOperateRowStatus": hh3cSysPackageOperateRowStatus,
       "hh3cSysPackageOperateResult": hh3cSysPackageOperateResult,
       "hh3cSysIpeFile": hh3cSysIpeFile,
       "hh3cSysIpeFileNum": hh3cSysIpeFileNum,
       "hh3cSysIpeFileTable": hh3cSysIpeFileTable,
       "hh3cSysIpeFileEntry": hh3cSysIpeFileEntry,
       "hh3cSysIpeFileIndex": hh3cSysIpeFileIndex,
       "hh3cSysIpeFileName": hh3cSysIpeFileName,
       "hh3cSysIpeFileSize": hh3cSysIpeFileSize,
       "hh3cSysIpeFileLocation": hh3cSysIpeFileLocation,
       "hh3cSysIpeFileModel": hh3cSysIpeFileModel,
       "hh3cSysIpePackageTable": hh3cSysIpePackageTable,
       "hh3cSysIpePackageEntry": hh3cSysIpePackageEntry,
       "hh3cSysIpePackageIndex": hh3cSysIpePackageIndex,
       "hh3cSysIpePackageName": hh3cSysIpePackageName,
       "hh3cSysIpePackageSize": hh3cSysIpePackageSize,
       "hh3cSysIpePackageType": hh3cSysIpePackageType,
       "hh3cSysIpePackageDescription": hh3cSysIpePackageDescription,
       "hh3cSysIpePackageFeature": hh3cSysIpePackageFeature,
       "hh3cSysIpePackageVersion": hh3cSysIpePackageVersion,
       "hh3cSysIpePackageModel": hh3cSysIpePackageModel,
       "hh3cSysIpeFileOperateTable": hh3cSysIpeFileOperateTable,
       "hh3cSysIpeFileOperateEntry": hh3cSysIpeFileOperateEntry,
       "hh3cSysIpeFileOperateIndex": hh3cSysIpeFileOperateIndex,
       "hh3cSysIpeFileOperateFileIndex": hh3cSysIpeFileOperateFileIndex,
       "hh3cSysIpeFileOperateAttribute": hh3cSysIpeFileOperateAttribute,
       "hh3cSysIpeFileOperateRowStatus": hh3cSysIpeFileOperateRowStatus,
       "hh3cSysIpeFileOperateResult": hh3cSysIpeFileOperateResult,
       "hh3cSysSetBootImage": hh3cSysSetBootImage,
       "hh3cSysSetBootImageOp": hh3cSysSetBootImageOp,
       "hh3cSysSetBootImageAction": hh3cSysSetBootImageAction,
       "hh3cSysSetBootImageFileOverWrite": hh3cSysSetBootImageFileOverWrite,
       "hh3cSysSetBootImageRemoveIpeFile": hh3cSysSetBootImageRemoveIpeFile,
       "hh3cSysSetBootImageStatus": hh3cSysSetBootImageStatus,
       "hh3cSysSetBootImageFailedReason": hh3cSysSetBootImageFailedReason,
       "hh3cSysBootPackageTable": hh3cSysBootPackageTable,
       "hh3cSysBootPackageEntry": hh3cSysBootPackageEntry,
       "hh3cSysBootPackageIndex": hh3cSysBootPackageIndex,
       "hh3cSysBootPackageRowStatus": hh3cSysBootPackageRowStatus,
       "hh3cSysBootIpeTable": hh3cSysBootIpeTable,
       "hh3cSysBootIpeEntry": hh3cSysBootIpeEntry,
       "hh3cSysBootIpeIndex": hh3cSysBootIpeIndex,
       "hh3cSysBootIpeRowStatus": hh3cSysBootIpeRowStatus,
       "hh3cSysSetBootImageResultTable": hh3cSysSetBootImageResultTable,
       "hh3cSysSetBootImageResultEntry": hh3cSysSetBootImageResultEntry,
       "hh3cSysSetBootImageResultIndex": hh3cSysSetBootImageResultIndex,
       "hh3cSysSetBootImageResultStatusOfEachCard": hh3cSysSetBootImageResultStatusOfEachCard,
       "hh3cSysSetBootImageFailedReasonOfEachCard": hh3cSysSetBootImageFailedReasonOfEachCard,
       "hh3cSystemManMIBNotifications": hh3cSystemManMIBNotifications,
       "hh3cSysClockChangedNotification": hh3cSysClockChangedNotification,
       "hh3cSysReloadNotification": hh3cSysReloadNotification,
       "hh3cSysStartUpNotification": hh3cSysStartUpNotification,
       "hh3cSystemManMIBConformance": hh3cSystemManMIBConformance,
       "hh3cSystemManMIBCompliances": hh3cSystemManMIBCompliances,
       "hh3cSystemManMIBCompliance": hh3cSystemManMIBCompliance,
       "hh3cSystemManMIBGroups": hh3cSystemManMIBGroups,
       "hh3cSysClockGroup": hh3cSysClockGroup,
       "hh3cSysReloadGroup": hh3cSysReloadGroup,
       "hh3cSysImageGroup": hh3cSysImageGroup,
       "hh3cSysCFGFileGroup": hh3cSysCFGFileGroup,
       "hh3cSysCurGroup": hh3cSysCurGroup,
       "hh3cSystemManNotificationGroup": hh3cSystemManNotificationGroup,
       "hh3cSystemBtmLoadGroup": hh3cSystemBtmLoadGroup}
)
