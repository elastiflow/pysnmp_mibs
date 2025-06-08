# SNMP MIB module (DUX106-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asaca_39081/DUX106-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:35:25 2025
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

(DuxAlarmStatus,
 DuxTrapMask,
 dux) = mibBuilder.importSymbols(
    "DUX-MIB",
    "DuxAlarmStatus",
    "DuxTrapMask",
    "dux")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dux106 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dux106InputFormat(TextualConvention, Integer32):
    status = "current"
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
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("3840x2160p59", 0),
          ("4096x2160p59", 1),
          ("3840x2160p50", 2),
          ("4096x2160p50", 3),
          ("3840x2160PsF29", 4),
          ("4096x2160PsF29", 5),
          ("3840x2160PsF23", 6),
          ("4096x2160PsF23", 7),
          ("1920x1080i59", 8),
          ("1920x1080i50", 9),
          ("1920x1080PsF29", 10),
          ("1920x1080PsF23", 11),
          ("no-signal", 100),
          ("unknown", 101))
    )



class Dux106OutputFormat(TextualConvention, Integer32):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("3840x2160p59", 0),
          ("4096x2160p59", 1),
          ("3840x2160p50", 2),
          ("4096x2160p50", 3),
          ("3840x2160PsF29", 4),
          ("4096x2160PsF29", 5),
          ("3840x2160PsF23", 6),
          ("4096x2160PsF23", 7),
          ("1920x1080i59", 8),
          ("1920x1080i50", 9),
          ("1920x1080PsF29", 10),
          ("1920x1080PsF23", 11))
    )



class Dux106OperationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up-converter", 0),
          ("4k-data-structure-converter", 1),
          ("hd-bypass-mode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Dux106Table_Object = MibTable
dux106Table = _Dux106Table_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1)
)
if mibBuilder.loadTexts:
    dux106Table.setStatus("current")
_Dux106Entry_Object = MibTableRow
dux106Entry = _Dux106Entry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1)
)
dux106Entry.setIndexNames(
    (0, "DUX106-MIB", "dux106Index"),
)
if mibBuilder.loadTexts:
    dux106Entry.setStatus("current")


class _Dux106Index_Type(Integer32):
    """Custom type dux106Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dux106Index_Type.__name__ = "Integer32"
_Dux106Index_Object = MibTableColumn
dux106Index = _Dux106Index_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 1),
    _Dux106Index_Type()
)
dux106Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dux106Index.setStatus("current")
_Dux106OperationMode_Type = Dux106OperationMode
_Dux106OperationMode_Object = MibTableColumn
dux106OperationMode = _Dux106OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 2),
    _Dux106OperationMode_Type()
)
dux106OperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux106OperationMode.setStatus("current")
_Dux106InputFormat_Type = Dux106InputFormat
_Dux106InputFormat_Object = MibScalar
dux106InputFormat = _Dux106InputFormat_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 3),
    _Dux106InputFormat_Type()
)
dux106InputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux106InputFormat.setStatus("current")
_Dux106OutputFormat_Type = Dux106OutputFormat
_Dux106OutputFormat_Object = MibTableColumn
dux106OutputFormat = _Dux106OutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 4),
    _Dux106OutputFormat_Type()
)
dux106OutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux106OutputFormat.setStatus("current")
_Dux106FpgaTemperature_Type = Integer32
_Dux106FpgaTemperature_Object = MibTableColumn
dux106FpgaTemperature = _Dux106FpgaTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 5),
    _Dux106FpgaTemperature_Type()
)
dux106FpgaTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux106FpgaTemperature.setStatus("current")
_Dux106BoardTemperature_Type = Integer32
_Dux106BoardTemperature_Object = MibTableColumn
dux106BoardTemperature = _Dux106BoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 6),
    _Dux106BoardTemperature_Type()
)
dux106BoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux106BoardTemperature.setStatus("current")
_Dux106WdtStatus_Type = DuxAlarmStatus
_Dux106WdtStatus_Object = MibTableColumn
dux106WdtStatus = _Dux106WdtStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 1, 1, 7),
    _Dux106WdtStatus_Type()
)
dux106WdtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux106WdtStatus.setStatus("current")
_Dux106Traps_ObjectIdentity = ObjectIdentity
dux106Traps = _Dux106Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2)
)

# Managed Objects groups


# Notification objects

dux106InputInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 1)
)
dux106InputInvalidTrap.setObjects(
      *(("DUX106-MIB", "dux106Index"),
        ("DUX106-MIB", "dux106InputFormat"))
)
if mibBuilder.loadTexts:
    dux106InputInvalidTrap.setStatus(
        "current"
    )

dux106InputValidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 2)
)
dux106InputValidTrap.setObjects(
      *(("DUX106-MIB", "dux106Index"),
        ("DUX106-MIB", "dux106InputFormat"))
)
if mibBuilder.loadTexts:
    dux106InputValidTrap.setStatus(
        "current"
    )

dux106BoardTemperatureOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 3)
)
dux106BoardTemperatureOverTrap.setObjects(
      *(("DUX106-MIB", "dux106Index"),
        ("DUX106-MIB", "dux106BoardTemperature"))
)
if mibBuilder.loadTexts:
    dux106BoardTemperatureOverTrap.setStatus(
        "current"
    )

dux106BoardTemperatureNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 4)
)
dux106BoardTemperatureNormalTrap.setObjects(
      *(("DUX106-MIB", "dux106Index"),
        ("DUX106-MIB", "dux106BoardTemperature"))
)
if mibBuilder.loadTexts:
    dux106BoardTemperatureNormalTrap.setStatus(
        "current"
    )

dux106OutputUnlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 5)
)
dux106OutputUnlockedTrap.setObjects(
    ("DUX106-MIB", "dux106Index")
)
if mibBuilder.loadTexts:
    dux106OutputUnlockedTrap.setStatus(
        "current"
    )

dux106OutputLockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 6)
)
dux106OutputLockedTrap.setObjects(
    ("DUX106-MIB", "dux106Index")
)
if mibBuilder.loadTexts:
    dux106OutputLockedTrap.setStatus(
        "current"
    )

dux106WdtFailedTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 7)
)
dux106WdtFailedTraps.setObjects(
      *(("DUX106-MIB", "dux106Index"),
        ("DUX106-MIB", "dux106WdtStatus"))
)
if mibBuilder.loadTexts:
    dux106WdtFailedTraps.setStatus(
        "current"
    )

dux106WdtNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 106, 2, 8)
)
dux106WdtNormalTrap.setObjects(
      *(("DUX106-MIB", "dux106Index"),
        ("DUX106-MIB", "dux106WdtStatus"))
)
if mibBuilder.loadTexts:
    dux106WdtNormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DUX106-MIB",
    **{"Dux106InputFormat": Dux106InputFormat,
       "Dux106OutputFormat": Dux106OutputFormat,
       "Dux106OperationMode": Dux106OperationMode,
       "dux106": dux106,
       "dux106Table": dux106Table,
       "dux106Entry": dux106Entry,
       "dux106Index": dux106Index,
       "dux106OperationMode": dux106OperationMode,
       "dux106InputFormat": dux106InputFormat,
       "dux106OutputFormat": dux106OutputFormat,
       "dux106FpgaTemperature": dux106FpgaTemperature,
       "dux106BoardTemperature": dux106BoardTemperature,
       "dux106WdtStatus": dux106WdtStatus,
       "dux106Traps": dux106Traps,
       "dux106InputInvalidTrap": dux106InputInvalidTrap,
       "dux106InputValidTrap": dux106InputValidTrap,
       "dux106BoardTemperatureOverTrap": dux106BoardTemperatureOverTrap,
       "dux106BoardTemperatureNormalTrap": dux106BoardTemperatureNormalTrap,
       "dux106OutputUnlockedTrap": dux106OutputUnlockedTrap,
       "dux106OutputLockedTrap": dux106OutputLockedTrap,
       "dux106WdtFailedTraps": dux106WdtFailedTraps,
       "dux106WdtNormalTrap": dux106WdtNormalTrap}
)
