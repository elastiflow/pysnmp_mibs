# SNMP MIB module (LIEBERT-GP-FLEXIBLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_476/LIEBERT-GP-FLEXIBLE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:21:43 2025
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

(lgpFlexible,
 liebertFlexibleModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpFlexible",
    "liebertFlexibleModuleReg")

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

liebertGlobalProductsFlexibleModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 10, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsFlexibleModule.setRevisions(
        ("2013-05-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpFlexibleTableCount_Type = Unsigned32
_LgpFlexibleTableCount_Object = MibScalar
lgpFlexibleTableCount = _LgpFlexibleTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 10),
    _LgpFlexibleTableCount_Type()
)
lgpFlexibleTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpFlexibleTableCount.setUnits("Count")
_LgpFlexibleBasicTable_Object = MibTable
lgpFlexibleBasicTable = _LgpFlexibleBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20)
)
if mibBuilder.loadTexts:
    lgpFlexibleBasicTable.setStatus("current")
_LgpFlexibleBasicEntry_Object = MibTableRow
lgpFlexibleBasicEntry = _LgpFlexibleBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1)
)
lgpFlexibleBasicEntry.setIndexNames(
    (1, "LIEBERT-GP-FLEXIBLE-MIB", "lgpFlexibleEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpFlexibleBasicEntry.setStatus("current")
_LgpFlexibleEntryIndex_Type = ObjectIdentifier
_LgpFlexibleEntryIndex_Object = MibTableColumn
lgpFlexibleEntryIndex = _LgpFlexibleEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 1),
    _LgpFlexibleEntryIndex_Type()
)
lgpFlexibleEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpFlexibleEntryIndex.setStatus("current")
_LgpFlexibleEntryDataLabel_Type = DisplayString
_LgpFlexibleEntryDataLabel_Object = MibTableColumn
lgpFlexibleEntryDataLabel = _LgpFlexibleEntryDataLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 10),
    _LgpFlexibleEntryDataLabel_Type()
)
lgpFlexibleEntryDataLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDataLabel.setStatus("current")
_LgpFlexibleEntryValue_Type = DisplayString
_LgpFlexibleEntryValue_Object = MibTableColumn
lgpFlexibleEntryValue = _LgpFlexibleEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 20),
    _LgpFlexibleEntryValue_Type()
)
lgpFlexibleEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpFlexibleEntryValue.setStatus("current")
_LgpFlexibleEntryUnitsOfMeasure_Type = DisplayString
_LgpFlexibleEntryUnitsOfMeasure_Object = MibTableColumn
lgpFlexibleEntryUnitsOfMeasure = _LgpFlexibleEntryUnitsOfMeasure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 30),
    _LgpFlexibleEntryUnitsOfMeasure_Type()
)
lgpFlexibleEntryUnitsOfMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryUnitsOfMeasure.setStatus("current")
_LgpFlexibleExtendedTable_Object = MibTable
lgpFlexibleExtendedTable = _LgpFlexibleExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30)
)
if mibBuilder.loadTexts:
    lgpFlexibleExtendedTable.setStatus("current")
_LgpFlexibleExtendedEntry_Object = MibTableRow
lgpFlexibleExtendedEntry = _LgpFlexibleExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1)
)
if mibBuilder.loadTexts:
    lgpFlexibleExtendedEntry.setStatus("current")
_LgpFlexibleEntryIntegerValue_Type = Integer32
_LgpFlexibleEntryIntegerValue_Object = MibTableColumn
lgpFlexibleEntryIntegerValue = _LgpFlexibleEntryIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 10),
    _LgpFlexibleEntryIntegerValue_Type()
)
lgpFlexibleEntryIntegerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpFlexibleEntryIntegerValue.setStatus("current")
_LgpFlexibleEntryUnsignedIntegerValue_Type = Unsigned32
_LgpFlexibleEntryUnsignedIntegerValue_Object = MibTableColumn
lgpFlexibleEntryUnsignedIntegerValue = _LgpFlexibleEntryUnsignedIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 20),
    _LgpFlexibleEntryUnsignedIntegerValue_Type()
)
lgpFlexibleEntryUnsignedIntegerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpFlexibleEntryUnsignedIntegerValue.setStatus("current")
_LgpFlexibleEntryDecimalPosition_Type = Unsigned32
_LgpFlexibleEntryDecimalPosition_Object = MibTableColumn
lgpFlexibleEntryDecimalPosition = _LgpFlexibleEntryDecimalPosition_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 30),
    _LgpFlexibleEntryDecimalPosition_Type()
)
lgpFlexibleEntryDecimalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDecimalPosition.setStatus("current")


class _LgpFlexibleEntryDataType_Type(Integer32):
    """Custom type lgpFlexibleEntryDataType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("int16", 1),
          ("uint16", 2),
          ("int32", 3),
          ("uint32", 4),
          ("text", 5),
          ("enum", 6),
          ("event16", 7),
          ("event32", 8),
          ("ipv4", 9),
          ("time32", 10))
    )


_LgpFlexibleEntryDataType_Type.__name__ = "Integer32"
_LgpFlexibleEntryDataType_Object = MibTableColumn
lgpFlexibleEntryDataType = _LgpFlexibleEntryDataType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 40),
    _LgpFlexibleEntryDataType_Type()
)
lgpFlexibleEntryDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDataType.setStatus("current")


class _LgpFlexibleEntryAccessibility_Type(Integer32):
    """Custom type lgpFlexibleEntryAccessibility based on Integer32"""
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
        *(("not-specified", 0),
          ("readonly", 1),
          ("writeonly", 2),
          ("readwrite", 3))
    )


_LgpFlexibleEntryAccessibility_Type.__name__ = "Integer32"
_LgpFlexibleEntryAccessibility_Object = MibTableColumn
lgpFlexibleEntryAccessibility = _LgpFlexibleEntryAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 50),
    _LgpFlexibleEntryAccessibility_Type()
)
lgpFlexibleEntryAccessibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryAccessibility.setStatus("current")


class _LgpFlexibleEntryUnitsOfMeasureEnum_Type(Integer32):
    """Custom type lgpFlexibleEntryUnitsOfMeasureEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              4097,
              4098,
              4099,
              4100,
              4101,
              4102,
              4103,
              4104,
              4105,
              4106,
              4107,
              4108,
              4109,
              4110,
              4111,
              4112,
              4113,
              4114,
              4115,
              4116,
              4117,
              4118,
              4119,
              4120,
              4121,
              4122,
              4123,
              4124,
              4125,
              4126,
              4127,
              4128,
              4129,
              4130,
              4131,
              4132,
              4133,
              4134,
              4135,
              4136,
              4137,
              4138,
              4139,
              4140,
              4141,
              4142,
              4143,
              4144,
              4145,
              4146,
              4147,
              4148,
              4149,
              4150,
              4151,
              4152,
              4153,
              4154,
              4155,
              4156,
              4157,
              4158,
              4159,
              4160,
              4161,
              4162,
              4163,
              4164,
              4165,
              4166,
              4167,
              4168,
              4169,
              4170,
              4171,
              4172,
              4173,
              4174,
              4175,
              4176,
              4177,
              4178)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("milliSeconds", 4096),
          ("seconds", 4097),
          ("minutes", 4098),
          ("hours", 4099),
          ("voltsAcRms", 4100),
          ("milliVoltsAcRms", 4101),
          ("voltsDc", 4102),
          ("milliVoltsDc", 4103),
          ("voltsPeak", 4104),
          ("voltsPeakToPeak", 4105),
          ("ampsAcRms", 4106),
          ("milliAmpsAcRms", 4107),
          ("ampsDc", 4108),
          ("milliAmpsDc", 4109),
          ("voltAmps", 4110),
          ("kiloVoltAmps", 4111),
          ("voltAmpsReactive", 4112),
          ("kVAReactive", 4113),
          ("watts", 4114),
          ("kiloWatts", 4115),
          ("wattHours", 4116),
          ("kiloWattHour", 4117),
          ("ampDcHours", 4118),
          ("hertz", 4119),
          ("milliHertz", 4120),
          ("kiloHertz", 4121),
          ("megaHertz", 4122),
          ("gigaHertz", 4123),
          ("percent", 4124),
          ("degC", 4125),
          ("degCDelta", 4126),
          ("degF", 4127),
          ("degFDelta", 4128),
          ("psi", 4129),
          ("pascal", 4130),
          ("psia", 4131),
          ("relativeHumidity", 4132),
          ("thd", 4133),
          ("days", 4134),
          ("phase", 4135),
          ("microOhms", 4136),
          ("milliOhms", 4137),
          ("ohms", 4138),
          ("kiloOhms", 4139),
          ("megaOhms", 4140),
          ("bars", 4141),
          ("rpm", 4142),
          ("bytes", 4143),
          ("kilobytes", 4144),
          ("megabytes", 4145),
          ("gigabytes", 4146),
          ("terabytes", 4147),
          ("voltAmpHours", 4148),
          ("kiloVoltAmpHours", 4149),
          ("vaReactiveHours", 4150),
          ("kVAReactiveHours", 4151),
          ("meter", 4152),
          ("feet", 4153),
          ("cms", 4154),
          ("cmh", 4155),
          ("cfs", 4156),
          ("cfm", 4157),
          ("lpm", 4158),
          ("gpmUk", 4159),
          ("gpmUs", 4160),
          ("absoluteHumidity", 4161),
          ("kilograms", 4162),
          ("cubicMeters", 4163),
          ("btu", 4164),
          ("torrs", 4165),
          ("millitorrs", 4166),
          ("pounds", 4167),
          ("mps", 4168),
          ("fpm", 4169),
          ("liter", 4170),
          ("gallonUs", 4171),
          ("gallonUk", 4172),
          ("lps", 4173),
          ("mho", 4174),
          ("siemensCm", 4175),
          ("weeks", 4176),
          ("inWC", 4177),
          ("btuHours", 4178))
    )


_LgpFlexibleEntryUnitsOfMeasureEnum_Type.__name__ = "Integer32"
_LgpFlexibleEntryUnitsOfMeasureEnum_Object = MibTableColumn
lgpFlexibleEntryUnitsOfMeasureEnum = _LgpFlexibleEntryUnitsOfMeasureEnum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 60),
    _LgpFlexibleEntryUnitsOfMeasureEnum_Type()
)
lgpFlexibleEntryUnitsOfMeasureEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryUnitsOfMeasureEnum.setStatus("current")
_LgpFlexibleEntryDataDescription_Type = DisplayString
_LgpFlexibleEntryDataDescription_Object = MibTableColumn
lgpFlexibleEntryDataDescription = _LgpFlexibleEntryDataDescription_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 70),
    _LgpFlexibleEntryDataDescription_Type()
)
lgpFlexibleEntryDataDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDataDescription.setStatus("current")
lgpFlexibleBasicEntry.registerAugmentions(
    ("LIEBERT-GP-FLEXIBLE-MIB",
     "lgpFlexibleExtendedEntry")
)
lgpFlexibleExtendedEntry.setIndexNames(*lgpFlexibleBasicEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-FLEXIBLE-MIB",
    **{"liebertGlobalProductsFlexibleModule": liebertGlobalProductsFlexibleModule,
       "lgpFlexibleTableCount": lgpFlexibleTableCount,
       "lgpFlexibleBasicTable": lgpFlexibleBasicTable,
       "lgpFlexibleBasicEntry": lgpFlexibleBasicEntry,
       "lgpFlexibleEntryIndex": lgpFlexibleEntryIndex,
       "lgpFlexibleEntryDataLabel": lgpFlexibleEntryDataLabel,
       "lgpFlexibleEntryValue": lgpFlexibleEntryValue,
       "lgpFlexibleEntryUnitsOfMeasure": lgpFlexibleEntryUnitsOfMeasure,
       "lgpFlexibleExtendedTable": lgpFlexibleExtendedTable,
       "lgpFlexibleExtendedEntry": lgpFlexibleExtendedEntry,
       "lgpFlexibleEntryIntegerValue": lgpFlexibleEntryIntegerValue,
       "lgpFlexibleEntryUnsignedIntegerValue": lgpFlexibleEntryUnsignedIntegerValue,
       "lgpFlexibleEntryDecimalPosition": lgpFlexibleEntryDecimalPosition,
       "lgpFlexibleEntryDataType": lgpFlexibleEntryDataType,
       "lgpFlexibleEntryAccessibility": lgpFlexibleEntryAccessibility,
       "lgpFlexibleEntryUnitsOfMeasureEnum": lgpFlexibleEntryUnitsOfMeasureEnum,
       "lgpFlexibleEntryDataDescription": lgpFlexibleEntryDataDescription}
)
