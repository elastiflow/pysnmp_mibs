# SNMP MIB module (A3COM-HUAWEI-LswPERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-LswPERFORMANCE-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:00:33 2025
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

(hwInternetProtocol,
 hwLocal,
 rmonExtend) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "hwInternetProtocol",
    "hwLocal",
    "rmonExtend")

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

(EntryStatus,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus")

(trapDestEntry,
 trapDestIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "trapDestEntry",
    "trapDestIndex")

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

performance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    performance.setRevisions(
        ("2003-03-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RmonExtendEventsV2_ObjectIdentity = ObjectIdentity
rmonExtendEventsV2 = _RmonExtendEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 0)
)
if mibBuilder.loadTexts:
    rmonExtendEventsV2.setStatus("current")
_PrialarmTable_Object = MibTable
prialarmTable = _PrialarmTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    prialarmTable.setStatus("current")
_PrialarmEntry_Object = MibTableRow
prialarmEntry = _PrialarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1)
)
prialarmEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmIndex"),
)
if mibBuilder.loadTexts:
    prialarmEntry.setStatus("current")


class _PrialarmIndex_Type(Integer32):
    """Custom type prialarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrialarmIndex_Type.__name__ = "Integer32"
_PrialarmIndex_Object = MibTableColumn
prialarmIndex = _PrialarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 1),
    _PrialarmIndex_Type()
)
prialarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prialarmIndex.setStatus("current")
_PrialarmInterval_Type = Integer32
_PrialarmInterval_Object = MibTableColumn
prialarmInterval = _PrialarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 2),
    _PrialarmInterval_Type()
)
prialarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmInterval.setStatus("current")
_PrialarmVariable_Type = DisplayString
_PrialarmVariable_Object = MibTableColumn
prialarmVariable = _PrialarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 3),
    _PrialarmVariable_Type()
)
prialarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmVariable.setStatus("current")
_PrialarmSympol_Type = DisplayString
_PrialarmSympol_Object = MibTableColumn
prialarmSympol = _PrialarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 4),
    _PrialarmSympol_Type()
)
prialarmSympol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmSympol.setStatus("current")


class _PrialarmSampleType_Type(Integer32):
    """Custom type prialarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2),
          ("speedValue", 3))
    )


_PrialarmSampleType_Type.__name__ = "Integer32"
_PrialarmSampleType_Object = MibTableColumn
prialarmSampleType = _PrialarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 5),
    _PrialarmSampleType_Type()
)
prialarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmSampleType.setStatus("current")
_PrialarmValue_Type = Integer32
_PrialarmValue_Object = MibTableColumn
prialarmValue = _PrialarmValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 6),
    _PrialarmValue_Type()
)
prialarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prialarmValue.setStatus("current")


class _PrialarmStartupAlarm_Type(Integer32):
    """Custom type prialarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("risingAlarm", 1),
          ("fallingAlarm", 2),
          ("risingOrFallingAlarm", 3))
    )


_PrialarmStartupAlarm_Type.__name__ = "Integer32"
_PrialarmStartupAlarm_Object = MibTableColumn
prialarmStartupAlarm = _PrialarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 7),
    _PrialarmStartupAlarm_Type()
)
prialarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmStartupAlarm.setStatus("current")
_PrialarmRisingThreshold_Type = Integer32
_PrialarmRisingThreshold_Object = MibTableColumn
prialarmRisingThreshold = _PrialarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 8),
    _PrialarmRisingThreshold_Type()
)
prialarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmRisingThreshold.setStatus("current")
_PrialarmFallingThreshold_Type = Integer32
_PrialarmFallingThreshold_Object = MibTableColumn
prialarmFallingThreshold = _PrialarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 9),
    _PrialarmFallingThreshold_Type()
)
prialarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmFallingThreshold.setStatus("current")


class _PrialarmRisingEventIndex_Type(Integer32):
    """Custom type prialarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrialarmRisingEventIndex_Type.__name__ = "Integer32"
_PrialarmRisingEventIndex_Object = MibTableColumn
prialarmRisingEventIndex = _PrialarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 10),
    _PrialarmRisingEventIndex_Type()
)
prialarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmRisingEventIndex.setStatus("current")


class _PrialarmFallingEventIndex_Type(Integer32):
    """Custom type prialarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrialarmFallingEventIndex_Type.__name__ = "Integer32"
_PrialarmFallingEventIndex_Object = MibTableColumn
prialarmFallingEventIndex = _PrialarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 11),
    _PrialarmFallingEventIndex_Type()
)
prialarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmFallingEventIndex.setStatus("current")
_PrialarmStatCycle_Type = Integer32
_PrialarmStatCycle_Object = MibTableColumn
prialarmStatCycle = _PrialarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 12),
    _PrialarmStatCycle_Type()
)
prialarmStatCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmStatCycle.setStatus("current")


class _PrialarmStatType_Type(Integer32):
    """Custom type prialarmStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forever", 1),
          ("during", 2))
    )


_PrialarmStatType_Type.__name__ = "Integer32"
_PrialarmStatType_Object = MibTableColumn
prialarmStatType = _PrialarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 13),
    _PrialarmStatType_Type()
)
prialarmStatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmStatType.setStatus("current")
_PrialarmOwner_Type = OwnerString
_PrialarmOwner_Object = MibTableColumn
prialarmOwner = _PrialarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 14),
    _PrialarmOwner_Type()
)
prialarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmOwner.setStatus("current")
_PrialarmStatus_Type = EntryStatus
_PrialarmStatus_Object = MibTableColumn
prialarmStatus = _PrialarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 4, 1, 1, 15),
    _PrialarmStatus_Type()
)
prialarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prialarmStatus.setStatus("current")
_HwrmonEnableTable_Object = MibTable
hwrmonEnableTable = _HwrmonEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    hwrmonEnableTable.setStatus("current")
_HwrmonEnableTableEntry_Object = MibTableRow
hwrmonEnableTableEntry = _HwrmonEnableTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 5, 1)
)
hwrmonEnableTableEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswPERFORMANCE-MIB", "hwrmonEnableIfIndex"),
)
if mibBuilder.loadTexts:
    hwrmonEnableTableEntry.setStatus("current")


class _HwrmonEnableIfIndex_Type(Integer32):
    """Custom type hwrmonEnableIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwrmonEnableIfIndex_Type.__name__ = "Integer32"
_HwrmonEnableIfIndex_Object = MibTableColumn
hwrmonEnableIfIndex = _HwrmonEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 5, 1, 1),
    _HwrmonEnableIfIndex_Type()
)
hwrmonEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwrmonEnableIfIndex.setStatus("current")


class _HwrmonEnableStatus_Type(Integer32):
    """Custom type hwrmonEnableStatus based on Integer32"""
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


_HwrmonEnableStatus_Type.__name__ = "Integer32"
_HwrmonEnableStatus_Object = MibTableColumn
hwrmonEnableStatus = _HwrmonEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 5, 1, 2),
    _HwrmonEnableStatus_Type()
)
hwrmonEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwrmonEnableStatus.setStatus("current")
_HwTrapDestTable_Object = MibTable
hwTrapDestTable = _HwTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    hwTrapDestTable.setStatus("current")
_HwTrapDestEntry_Object = MibTableRow
hwTrapDestEntry = _HwTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hwTrapDestEntry.setStatus("current")


class _HwTrapDestVersion_Type(Integer32):
    """Custom type hwTrapDestVersion based on Integer32"""
    defaultValue = 1

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
        *(("snmpv1", 1),
          ("snmpv2", 2),
          ("snmpv3andauthen", 3),
          ("snmpv3andnoauthen", 4),
          ("snmpv3andpriv", 5))
    )


_HwTrapDestVersion_Type.__name__ = "Integer32"
_HwTrapDestVersion_Object = MibTableColumn
hwTrapDestVersion = _HwTrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 6, 1, 1),
    _HwTrapDestVersion_Type()
)
hwTrapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrapDestVersion.setStatus("current")
trapDestEntry.registerAugmentions(
    ("A3COM-HUAWEI-LswPERFORMANCE-MIB",
     "hwTrapDestEntry")
)
hwTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())

# Managed Objects groups


# Notification objects

pririsingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 0, 1)
)
pririsingAlarm.setObjects(
      *(("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmIndex"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmSympol"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmSampleType"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmValue"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    pririsingAlarm.setStatus(
        "current"
    )

prifallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 4, 0, 2)
)
prifallingAlarm.setObjects(
      *(("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmIndex"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmSympol"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmSampleType"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmValue"),
        ("A3COM-HUAWEI-LswPERFORMANCE-MIB", "prialarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    prifallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswPERFORMANCE-MIB",
    **{"rmonExtendEventsV2": rmonExtendEventsV2,
       "pririsingAlarm": pririsingAlarm,
       "prifallingAlarm": prifallingAlarm,
       "performance": performance,
       "prialarmTable": prialarmTable,
       "prialarmEntry": prialarmEntry,
       "prialarmIndex": prialarmIndex,
       "prialarmInterval": prialarmInterval,
       "prialarmVariable": prialarmVariable,
       "prialarmSympol": prialarmSympol,
       "prialarmSampleType": prialarmSampleType,
       "prialarmValue": prialarmValue,
       "prialarmStartupAlarm": prialarmStartupAlarm,
       "prialarmRisingThreshold": prialarmRisingThreshold,
       "prialarmFallingThreshold": prialarmFallingThreshold,
       "prialarmRisingEventIndex": prialarmRisingEventIndex,
       "prialarmFallingEventIndex": prialarmFallingEventIndex,
       "prialarmStatCycle": prialarmStatCycle,
       "prialarmStatType": prialarmStatType,
       "prialarmOwner": prialarmOwner,
       "prialarmStatus": prialarmStatus,
       "hwrmonEnableTable": hwrmonEnableTable,
       "hwrmonEnableTableEntry": hwrmonEnableTableEntry,
       "hwrmonEnableIfIndex": hwrmonEnableIfIndex,
       "hwrmonEnableStatus": hwrmonEnableStatus,
       "hwTrapDestTable": hwTrapDestTable,
       "hwTrapDestEntry": hwTrapDestEntry,
       "hwTrapDestVersion": hwTrapDestVersion}
)
