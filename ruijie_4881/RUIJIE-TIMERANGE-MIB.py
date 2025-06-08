# SNMP MIB module (RUIJIE-TIMERANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TIMERANGE-MIB.mib
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieTrsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144)
)
if mibBuilder.loadTexts:
    ruijieTrsMIB.setRevisions(
        ("2015-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieTrsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTrsMIBObjects = _RuijieTrsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1)
)
_RuijieTRTable_Object = MibTable
ruijieTRTable = _RuijieTRTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieTRTable.setStatus("current")
_RuijieTREntry_Object = MibTableRow
ruijieTREntry = _RuijieTREntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 1, 1)
)
ruijieTREntry.setIndexNames(
    (0, "RUIJIE-TIMERANGE-MIB", "ruijieTRName"),
)
if mibBuilder.loadTexts:
    ruijieTREntry.setStatus("current")


class _RuijieTRName_Type(DisplayString):
    """Custom type ruijieTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieTRName_Type.__name__ = "DisplayString"
_RuijieTRName_Object = MibTableColumn
ruijieTRName = _RuijieTRName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 1, 1, 1),
    _RuijieTRName_Type()
)
ruijieTRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTRName.setStatus("current")


class _RuijieAbsTRStr_Type(DisplayString):
    """Custom type ruijieAbsTRStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieAbsTRStr_Type.__name__ = "DisplayString"
_RuijieAbsTRStr_Object = MibTableColumn
ruijieAbsTRStr = _RuijieAbsTRStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 1, 1, 2),
    _RuijieAbsTRStr_Type()
)
ruijieAbsTRStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieAbsTRStr.setStatus("current")
_RuijieTRIndex_Type = Integer32
_RuijieTRIndex_Object = MibTableColumn
ruijieTRIndex = _RuijieTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 1, 1, 3),
    _RuijieTRIndex_Type()
)
ruijieTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTRIndex.setStatus("current")


class _RuijieTRMode_Type(Integer32):
    """Custom type ruijieTRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tr-add", 1),
          ("tr-del", 2))
    )


_RuijieTRMode_Type.__name__ = "Integer32"
_RuijieTRMode_Object = MibTableColumn
ruijieTRMode = _RuijieTRMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 1, 1, 4),
    _RuijieTRMode_Type()
)
ruijieTRMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieTRMode.setStatus("current")
_RuijieTRPeriTable_Object = MibTable
ruijieTRPeriTable = _RuijieTRPeriTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieTRPeriTable.setStatus("current")
_RuijieTRPeriEntry_Object = MibTableRow
ruijieTRPeriEntry = _RuijieTRPeriEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 3, 1)
)
ruijieTRPeriEntry.setIndexNames(
    (0, "RUIJIE-TIMERANGE-MIB", "ruijiePeriTRName"),
    (0, "RUIJIE-TIMERANGE-MIB", "ruijiePeriTRStr"),
)
if mibBuilder.loadTexts:
    ruijieTRPeriEntry.setStatus("current")


class _RuijiePeriTRName_Type(DisplayString):
    """Custom type ruijiePeriTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijiePeriTRName_Type.__name__ = "DisplayString"
_RuijiePeriTRName_Object = MibTableColumn
ruijiePeriTRName = _RuijiePeriTRName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 3, 1, 1),
    _RuijiePeriTRName_Type()
)
ruijiePeriTRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePeriTRName.setStatus("current")


class _RuijiePeriTRStr_Type(DisplayString):
    """Custom type ruijiePeriTRStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuijiePeriTRStr_Type.__name__ = "DisplayString"
_RuijiePeriTRStr_Object = MibTableColumn
ruijiePeriTRStr = _RuijiePeriTRStr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 3, 1, 2),
    _RuijiePeriTRStr_Type()
)
ruijiePeriTRStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePeriTRStr.setStatus("current")
_RuijiePeriTRIndex_Type = Integer32
_RuijiePeriTRIndex_Object = MibTableColumn
ruijiePeriTRIndex = _RuijiePeriTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 3, 1, 3),
    _RuijiePeriTRIndex_Type()
)
ruijiePeriTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePeriTRIndex.setStatus("current")


class _RuijiePeriTRMode_Type(Integer32):
    """Custom type ruijiePeriTRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("periodic-add", 1),
          ("periodic-del", 2))
    )


_RuijiePeriTRMode_Type.__name__ = "Integer32"
_RuijiePeriTRMode_Object = MibTableColumn
ruijiePeriTRMode = _RuijiePeriTRMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 144, 1, 3, 1, 4),
    _RuijiePeriTRMode_Type()
)
ruijiePeriTRMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePeriTRMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TIMERANGE-MIB",
    **{"ruijieTrsMIB": ruijieTrsMIB,
       "ruijieTrsMIBObjects": ruijieTrsMIBObjects,
       "ruijieTRTable": ruijieTRTable,
       "ruijieTREntry": ruijieTREntry,
       "ruijieTRName": ruijieTRName,
       "ruijieAbsTRStr": ruijieAbsTRStr,
       "ruijieTRIndex": ruijieTRIndex,
       "ruijieTRMode": ruijieTRMode,
       "ruijieTRPeriTable": ruijieTRPeriTable,
       "ruijieTRPeriEntry": ruijieTRPeriEntry,
       "ruijiePeriTRName": ruijiePeriTRName,
       "ruijiePeriTRStr": ruijiePeriTRStr,
       "ruijiePeriTRIndex": ruijiePeriTRIndex,
       "ruijiePeriTRMode": ruijiePeriTRMode}
)
