# SNMP MIB module (DUX105-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asaca_39081/DUX105-MIB.mib
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

dux105 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dux105InputFormat(TextualConvention, Integer32):
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



class Dux105OutputFormat(TextualConvention, Integer32):
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



class Dux105OperationMode(TextualConvention, Integer32):
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
        *(("down-converter", 0),
          ("4k-data-structure-converter", 1),
          ("hd-bypass-mode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Dux105Table_Object = MibTable
dux105Table = _Dux105Table_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1)
)
if mibBuilder.loadTexts:
    dux105Table.setStatus("current")
_Dux105Entry_Object = MibTableRow
dux105Entry = _Dux105Entry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1)
)
dux105Entry.setIndexNames(
    (0, "DUX105-MIB", "dux105Index"),
)
if mibBuilder.loadTexts:
    dux105Entry.setStatus("current")


class _Dux105Index_Type(Integer32):
    """Custom type dux105Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dux105Index_Type.__name__ = "Integer32"
_Dux105Index_Object = MibTableColumn
dux105Index = _Dux105Index_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 1),
    _Dux105Index_Type()
)
dux105Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dux105Index.setStatus("current")
_Dux105OperationMode_Type = Dux105OperationMode
_Dux105OperationMode_Object = MibTableColumn
dux105OperationMode = _Dux105OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 2),
    _Dux105OperationMode_Type()
)
dux105OperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux105OperationMode.setStatus("current")
_Dux105InputFormat_Type = Dux105InputFormat
_Dux105InputFormat_Object = MibScalar
dux105InputFormat = _Dux105InputFormat_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 3),
    _Dux105InputFormat_Type()
)
dux105InputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux105InputFormat.setStatus("current")
_Dux105OutputFormat_Type = Dux105OutputFormat
_Dux105OutputFormat_Object = MibTableColumn
dux105OutputFormat = _Dux105OutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 4),
    _Dux105OutputFormat_Type()
)
dux105OutputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux105OutputFormat.setStatus("current")
_Dux105FpgaTemperature_Type = Integer32
_Dux105FpgaTemperature_Object = MibTableColumn
dux105FpgaTemperature = _Dux105FpgaTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 5),
    _Dux105FpgaTemperature_Type()
)
dux105FpgaTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux105FpgaTemperature.setStatus("current")
_Dux105BoardTemperature_Type = Integer32
_Dux105BoardTemperature_Object = MibTableColumn
dux105BoardTemperature = _Dux105BoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 6),
    _Dux105BoardTemperature_Type()
)
dux105BoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux105BoardTemperature.setStatus("current")
_Dux105WdtStatus_Type = DuxAlarmStatus
_Dux105WdtStatus_Object = MibTableColumn
dux105WdtStatus = _Dux105WdtStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 1, 1, 7),
    _Dux105WdtStatus_Type()
)
dux105WdtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux105WdtStatus.setStatus("current")
_Dux105Traps_ObjectIdentity = ObjectIdentity
dux105Traps = _Dux105Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2)
)

# Managed Objects groups


# Notification objects

dux105InputInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 1)
)
dux105InputInvalidTrap.setObjects(
      *(("DUX105-MIB", "dux105Index"),
        ("DUX105-MIB", "dux105InputFormat"))
)
if mibBuilder.loadTexts:
    dux105InputInvalidTrap.setStatus(
        "current"
    )

dux105InputValidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 2)
)
dux105InputValidTrap.setObjects(
      *(("DUX105-MIB", "dux105Index"),
        ("DUX105-MIB", "dux105InputFormat"))
)
if mibBuilder.loadTexts:
    dux105InputValidTrap.setStatus(
        "current"
    )

dux105BoardTemperatureOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 3)
)
dux105BoardTemperatureOverTrap.setObjects(
      *(("DUX105-MIB", "dux105Index"),
        ("DUX105-MIB", "dux105BoardTemperature"))
)
if mibBuilder.loadTexts:
    dux105BoardTemperatureOverTrap.setStatus(
        "current"
    )

dux105BoardTemperatureNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 4)
)
dux105BoardTemperatureNormalTrap.setObjects(
      *(("DUX105-MIB", "dux105Index"),
        ("DUX105-MIB", "dux105BoardTemperature"))
)
if mibBuilder.loadTexts:
    dux105BoardTemperatureNormalTrap.setStatus(
        "current"
    )

dux105OutputUnlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 5)
)
dux105OutputUnlockedTrap.setObjects(
    ("DUX105-MIB", "dux105Index")
)
if mibBuilder.loadTexts:
    dux105OutputUnlockedTrap.setStatus(
        "current"
    )

dux105OutputLockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 6)
)
dux105OutputLockedTrap.setObjects(
    ("DUX105-MIB", "dux105Index")
)
if mibBuilder.loadTexts:
    dux105OutputLockedTrap.setStatus(
        "current"
    )

dux105WdtFailedTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 7)
)
dux105WdtFailedTraps.setObjects(
      *(("DUX105-MIB", "dux105Index"),
        ("DUX105-MIB", "dux105WdtStatus"))
)
if mibBuilder.loadTexts:
    dux105WdtFailedTraps.setStatus(
        "current"
    )

dux105WdtNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 8)
)
dux105WdtNormalTrap.setObjects(
      *(("DUX105-MIB", "dux105Index"),
        ("DUX105-MIB", "dux105WdtStatus"))
)
if mibBuilder.loadTexts:
    dux105WdtNormalTrap.setStatus(
        "current"
    )

dux105Input2SampleInterleaveLinkOrderInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 9)
)
dux105Input2SampleInterleaveLinkOrderInvalidTrap.setObjects(
    ("DUX105-MIB", "dux105Index")
)
if mibBuilder.loadTexts:
    dux105Input2SampleInterleaveLinkOrderInvalidTrap.setStatus(
        "current"
    )

dux105Input2SampleInterleaveLinkOrderNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 105, 2, 10)
)
dux105Input2SampleInterleaveLinkOrderNormalTrap.setObjects(
    ("DUX105-MIB", "dux105Index")
)
if mibBuilder.loadTexts:
    dux105Input2SampleInterleaveLinkOrderNormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DUX105-MIB",
    **{"Dux105InputFormat": Dux105InputFormat,
       "Dux105OutputFormat": Dux105OutputFormat,
       "Dux105OperationMode": Dux105OperationMode,
       "dux105": dux105,
       "dux105Table": dux105Table,
       "dux105Entry": dux105Entry,
       "dux105Index": dux105Index,
       "dux105OperationMode": dux105OperationMode,
       "dux105InputFormat": dux105InputFormat,
       "dux105OutputFormat": dux105OutputFormat,
       "dux105FpgaTemperature": dux105FpgaTemperature,
       "dux105BoardTemperature": dux105BoardTemperature,
       "dux105WdtStatus": dux105WdtStatus,
       "dux105Traps": dux105Traps,
       "dux105InputInvalidTrap": dux105InputInvalidTrap,
       "dux105InputValidTrap": dux105InputValidTrap,
       "dux105BoardTemperatureOverTrap": dux105BoardTemperatureOverTrap,
       "dux105BoardTemperatureNormalTrap": dux105BoardTemperatureNormalTrap,
       "dux105OutputUnlockedTrap": dux105OutputUnlockedTrap,
       "dux105OutputLockedTrap": dux105OutputLockedTrap,
       "dux105WdtFailedTraps": dux105WdtFailedTraps,
       "dux105WdtNormalTrap": dux105WdtNormalTrap,
       "dux105Input2SampleInterleaveLinkOrderInvalidTrap": dux105Input2SampleInterleaveLinkOrderInvalidTrap,
       "dux105Input2SampleInterleaveLinkOrderNormalTrap": dux105Input2SampleInterleaveLinkOrderNormalTrap}
)
