# SNMP MIB module (KENTIX-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kentix_37954/KENTIX-ROOT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:29 2025
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

kentix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37954)
)
if mibBuilder.loadTexts:
    kentix.setRevisions(
        ("2017-02-02 00:00",
         "2017-02-01 00:00")
    )


# Types definitions



class AlarmStatusEnumeration(Integer32):
    """Custom type AlarmStatusEnumeration based on Integer32"""
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
        *(("ok", 1),
          ("notApplicable", 2),
          ("other", 3),
          ("nonCritical", 4),
          ("critical", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Universal_ObjectIdentity = ObjectIdentity
universal = _Universal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 10)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1)
)
_AmbientInfoTable_Object = MibTable
ambientInfoTable = _AmbientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1)
)
if mibBuilder.loadTexts:
    ambientInfoTable.setStatus("current")
_AmbientInfoEntry_Object = MibTableRow
ambientInfoEntry = _AmbientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1)
)
ambientInfoEntry.setIndexNames(
    (0, "KENTIX-ROOT-MIB", "ambientInfoIndex"),
)
if mibBuilder.loadTexts:
    ambientInfoEntry.setStatus("current")


class _AmbientInfoIndex_Type(Integer32):
    """Custom type ambientInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AmbientInfoIndex_Type.__name__ = "Integer32"
_AmbientInfoIndex_Object = MibTableColumn
ambientInfoIndex = _AmbientInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1, 1),
    _AmbientInfoIndex_Type()
)
ambientInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ambientInfoIndex.setStatus("current")
_AmbientInfoName_Type = DisplayString
_AmbientInfoName_Object = MibTableColumn
ambientInfoName = _AmbientInfoName_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1, 2),
    _AmbientInfoName_Type()
)
ambientInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientInfoName.setStatus("current")


class _AmbientInfoTemperatureValue_Type(Integer32):
    """Custom type ambientInfoTemperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_AmbientInfoTemperatureValue_Type.__name__ = "Integer32"
_AmbientInfoTemperatureValue_Object = MibTableColumn
ambientInfoTemperatureValue = _AmbientInfoTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1, 3),
    _AmbientInfoTemperatureValue_Type()
)
ambientInfoTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientInfoTemperatureValue.setStatus("current")


class _AmbientInfoHumidityValue_Type(Gauge32):
    """Custom type ambientInfoHumidityValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AmbientInfoHumidityValue_Type.__name__ = "Gauge32"
_AmbientInfoHumidityValue_Object = MibTableColumn
ambientInfoHumidityValue = _AmbientInfoHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1, 4),
    _AmbientInfoHumidityValue_Type()
)
ambientInfoHumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientInfoHumidityValue.setStatus("current")


class _AmbientInfoDewPointValue_Type(Integer32):
    """Custom type ambientInfoDewPointValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_AmbientInfoDewPointValue_Type.__name__ = "Integer32"
_AmbientInfoDewPointValue_Object = MibTableColumn
ambientInfoDewPointValue = _AmbientInfoDewPointValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1, 5),
    _AmbientInfoDewPointValue_Type()
)
ambientInfoDewPointValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientInfoDewPointValue.setStatus("current")
_AmbientInfoState_Type = AlarmStatusEnumeration
_AmbientInfoState_Object = MibTableColumn
ambientInfoState = _AmbientInfoState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 1, 1, 6),
    _AmbientInfoState_Type()
)
ambientInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientInfoState.setStatus("current")
_Co2InfoTable_Object = MibTable
co2InfoTable = _Co2InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 2)
)
if mibBuilder.loadTexts:
    co2InfoTable.setStatus("current")
_Co2InfoEntry_Object = MibTableRow
co2InfoEntry = _Co2InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 2, 1)
)
co2InfoEntry.setIndexNames(
    (0, "KENTIX-ROOT-MIB", "co2InfoIndex"),
)
if mibBuilder.loadTexts:
    co2InfoEntry.setStatus("current")


class _Co2InfoIndex_Type(Integer32):
    """Custom type co2InfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Co2InfoIndex_Type.__name__ = "Integer32"
_Co2InfoIndex_Object = MibTableColumn
co2InfoIndex = _Co2InfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 2, 1, 1),
    _Co2InfoIndex_Type()
)
co2InfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    co2InfoIndex.setStatus("current")
_Co2InfoName_Type = DisplayString
_Co2InfoName_Object = MibTableColumn
co2InfoName = _Co2InfoName_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 2, 1, 2),
    _Co2InfoName_Type()
)
co2InfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2InfoName.setStatus("current")


class _Co2InfoValue_Type(Integer32):
    """Custom type co2InfoValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co2InfoValue_Type.__name__ = "Integer32"
_Co2InfoValue_Object = MibTableColumn
co2InfoValue = _Co2InfoValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 2, 1, 3),
    _Co2InfoValue_Type()
)
co2InfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2InfoValue.setStatus("current")
_Co2InfoState_Type = AlarmStatusEnumeration
_Co2InfoState_Object = MibTableColumn
co2InfoState = _Co2InfoState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 10, 2, 1, 4),
    _Co2InfoState_Type()
)
co2InfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co2InfoState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KENTIX-ROOT-MIB",
    **{"AlarmStatusEnumeration": AlarmStatusEnumeration,
       "kentix": kentix,
       "universal": universal,
       "hardware": hardware,
       "ambientInfoTable": ambientInfoTable,
       "ambientInfoEntry": ambientInfoEntry,
       "ambientInfoIndex": ambientInfoIndex,
       "ambientInfoName": ambientInfoName,
       "ambientInfoTemperatureValue": ambientInfoTemperatureValue,
       "ambientInfoHumidityValue": ambientInfoHumidityValue,
       "ambientInfoDewPointValue": ambientInfoDewPointValue,
       "ambientInfoState": ambientInfoState,
       "co2InfoTable": co2InfoTable,
       "co2InfoEntry": co2InfoEntry,
       "co2InfoIndex": co2InfoIndex,
       "co2InfoName": co2InfoName,
       "co2InfoValue": co2InfoValue,
       "co2InfoState": co2InfoState}
)
