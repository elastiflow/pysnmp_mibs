# SNMP MIB module (DUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asaca_39081/DUX-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:35:24 2025
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

(asaca,) = mibBuilder.importSymbols(
    "ASACA-ENTERPRISE-MIB",
    "asaca")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class DuxAlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )



class DuxTrapMask(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("maskOff", 0),
          ("maskOn", 1))
    )



class DuxCaseType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("FRX1H", 0),
          ("FRX1F", 1),
          ("FRX2F", 3))
    )



class DuxRefInputStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("no-input", 1))
    )



class DuxSlotModuleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              101,
              102,
              103,
              105,
              106)
        )
    )
    namedValues = NamedValues(
        *(("NA", 0),
          ("dux100", 100),
          ("dux101", 101),
          ("dux102", 102),
          ("dux103", 103),
          ("dux105", 105),
          ("dux106", 106))
    )



# MIB Managed Objects in the order of their OIDs

_Dux_ObjectIdentity = ObjectIdentity
dux = _Dux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12)
)
_DuxTraps_ObjectIdentity = ObjectIdentity
duxTraps = _DuxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 2)
)
_DuxCase_ObjectIdentity = ObjectIdentity
duxCase = _DuxCase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 3)
)
_DuxCaseType_Type = DuxCaseType
_DuxCaseType_Object = MibScalar
duxCaseType = _DuxCaseType_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 3, 1),
    _DuxCaseType_Type()
)
duxCaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duxCaseType.setStatus("current")
_DuxPower_ObjectIdentity = ObjectIdentity
duxPower = _DuxPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4)
)
_DuxPowerTable_Object = MibTable
duxPowerTable = _DuxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 1)
)
if mibBuilder.loadTexts:
    duxPowerTable.setStatus("current")
_DuxPowerEntry_Object = MibTableRow
duxPowerEntry = _DuxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 1, 1)
)
duxPowerEntry.setIndexNames(
    (0, "DUX-MIB", "duxPowerIndex"),
)
if mibBuilder.loadTexts:
    duxPowerEntry.setStatus("current")


class _DuxPowerIndex_Type(Integer32):
    """Custom type duxPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DuxPowerIndex_Type.__name__ = "Integer32"
_DuxPowerIndex_Object = MibTableColumn
duxPowerIndex = _DuxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 1, 1, 1),
    _DuxPowerIndex_Type()
)
duxPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    duxPowerIndex.setStatus("current")
_DuxPowerStatus_Type = DuxAlarmStatus
_DuxPowerStatus_Object = MibTableColumn
duxPowerStatus = _DuxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 1, 1, 2),
    _DuxPowerStatus_Type()
)
duxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duxPowerStatus.setStatus("current")
_DuxPowerFanStatus_Type = DuxAlarmStatus
_DuxPowerFanStatus_Object = MibTableColumn
duxPowerFanStatus = _DuxPowerFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 1, 1, 3),
    _DuxPowerFanStatus_Type()
)
duxPowerFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duxPowerFanStatus.setStatus("current")
_DuxPowerTraps_ObjectIdentity = ObjectIdentity
duxPowerTraps = _DuxPowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 2)
)
_DuxPanelFan_ObjectIdentity = ObjectIdentity
duxPanelFan = _DuxPanelFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5)
)
_DuxPanelFanTable_Object = MibTable
duxPanelFanTable = _DuxPanelFanTable_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 1)
)
if mibBuilder.loadTexts:
    duxPanelFanTable.setStatus("current")
_DuxPanelFanEntry_Object = MibTableRow
duxPanelFanEntry = _DuxPanelFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 1, 1)
)
duxPanelFanEntry.setIndexNames(
    (0, "DUX-MIB", "duxPanelFanIndex"),
)
if mibBuilder.loadTexts:
    duxPanelFanEntry.setStatus("current")


class _DuxPanelFanIndex_Type(Integer32):
    """Custom type duxPanelFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DuxPanelFanIndex_Type.__name__ = "Integer32"
_DuxPanelFanIndex_Object = MibTableColumn
duxPanelFanIndex = _DuxPanelFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 1, 1, 1),
    _DuxPanelFanIndex_Type()
)
duxPanelFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    duxPanelFanIndex.setStatus("current")
_DuxPanelFanStatus_Type = DuxAlarmStatus
_DuxPanelFanStatus_Object = MibTableColumn
duxPanelFanStatus = _DuxPanelFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 1, 1, 2),
    _DuxPanelFanStatus_Type()
)
duxPanelFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duxPanelFanStatus.setStatus("current")
_DuxPanelFanTraps_ObjectIdentity = ObjectIdentity
duxPanelFanTraps = _DuxPanelFanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 2)
)
_DuxRefInput_ObjectIdentity = ObjectIdentity
duxRefInput = _DuxRefInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 6)
)
_DuxRefInputTable_Object = MibTable
duxRefInputTable = _DuxRefInputTable_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 6, 1)
)
if mibBuilder.loadTexts:
    duxRefInputTable.setStatus("current")
_DuxRefInputEntry_Object = MibTableRow
duxRefInputEntry = _DuxRefInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 6, 1, 1)
)
duxRefInputEntry.setIndexNames(
    (0, "DUX-MIB", "duxRefInputIndex"),
)
if mibBuilder.loadTexts:
    duxRefInputEntry.setStatus("current")


class _DuxRefInputIndex_Type(Integer32):
    """Custom type duxRefInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DuxRefInputIndex_Type.__name__ = "Integer32"
_DuxRefInputIndex_Object = MibTableColumn
duxRefInputIndex = _DuxRefInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 6, 1, 1, 1),
    _DuxRefInputIndex_Type()
)
duxRefInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    duxRefInputIndex.setStatus("current")
_DuxRefInputStatus_Type = DuxRefInputStatus
_DuxRefInputStatus_Object = MibTableColumn
duxRefInputStatus = _DuxRefInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 6, 1, 1, 2),
    _DuxRefInputStatus_Type()
)
duxRefInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duxRefInputStatus.setStatus("current")
_DuxSlot_ObjectIdentity = ObjectIdentity
duxSlot = _DuxSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 7)
)
_DuxSlotTable_Object = MibTable
duxSlotTable = _DuxSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 7, 1)
)
if mibBuilder.loadTexts:
    duxSlotTable.setStatus("current")
_DuxSlotEntry_Object = MibTableRow
duxSlotEntry = _DuxSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 7, 1, 1)
)
duxSlotEntry.setIndexNames(
    (0, "DUX-MIB", "duxSlotIndex"),
)
if mibBuilder.loadTexts:
    duxSlotEntry.setStatus("current")


class _DuxSlotIndex_Type(Integer32):
    """Custom type duxSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DuxSlotIndex_Type.__name__ = "Integer32"
_DuxSlotIndex_Object = MibTableColumn
duxSlotIndex = _DuxSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 7, 1, 1, 1),
    _DuxSlotIndex_Type()
)
duxSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    duxSlotIndex.setStatus("current")
_DuxSlotModuleType_Type = DuxSlotModuleType
_DuxSlotModuleType_Object = MibTableColumn
duxSlotModuleType = _DuxSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 7, 1, 1, 2),
    _DuxSlotModuleType_Type()
)
duxSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duxSlotModuleType.setStatus("current")

# Managed Objects groups


# Notification objects

duxStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 2, 1)
)
if mibBuilder.loadTexts:
    duxStartTrap.setStatus(
        "current"
    )

duxPowerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 2, 1)
)
duxPowerFailedTrap.setObjects(
      *(("DUX-MIB", "duxPowerIndex"),
        ("DUX-MIB", "duxPowerStatus"))
)
if mibBuilder.loadTexts:
    duxPowerFailedTrap.setStatus(
        "current"
    )

duxPowerRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 2, 2)
)
duxPowerRecoveredTrap.setObjects(
      *(("DUX-MIB", "duxPowerIndex"),
        ("DUX-MIB", "duxPowerStatus"))
)
if mibBuilder.loadTexts:
    duxPowerRecoveredTrap.setStatus(
        "current"
    )

duxPowerFanFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 2, 3)
)
duxPowerFanFailedTrap.setObjects(
      *(("DUX-MIB", "duxPowerIndex"),
        ("DUX-MIB", "duxPowerFanStatus"))
)
if mibBuilder.loadTexts:
    duxPowerFanFailedTrap.setStatus(
        "current"
    )

duxPowerFanRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 4, 2, 4)
)
duxPowerFanRecoveredTrap.setObjects(
      *(("DUX-MIB", "duxPowerIndex"),
        ("DUX-MIB", "duxPowerFanStatus"))
)
if mibBuilder.loadTexts:
    duxPowerFanRecoveredTrap.setStatus(
        "current"
    )

duxPanelFanFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 2, 1)
)
duxPanelFanFailedTrap.setObjects(
      *(("DUX-MIB", "duxPanelFanIndex"),
        ("DUX-MIB", "duxPanelFanStatus"))
)
if mibBuilder.loadTexts:
    duxPanelFanFailedTrap.setStatus(
        "current"
    )

duxPanelFanRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 5, 2, 2)
)
duxPanelFanRecoveredTrap.setObjects(
      *(("DUX-MIB", "duxPanelFanIndex"),
        ("DUX-MIB", "duxPanelFanStatus"))
)
if mibBuilder.loadTexts:
    duxPanelFanRecoveredTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DUX-MIB",
    **{"DuxAlarmStatus": DuxAlarmStatus,
       "DuxTrapMask": DuxTrapMask,
       "DuxCaseType": DuxCaseType,
       "DuxRefInputStatus": DuxRefInputStatus,
       "DuxSlotModuleType": DuxSlotModuleType,
       "dux": dux,
       "duxTraps": duxTraps,
       "duxStartTrap": duxStartTrap,
       "duxCase": duxCase,
       "duxCaseType": duxCaseType,
       "duxPower": duxPower,
       "duxPowerTable": duxPowerTable,
       "duxPowerEntry": duxPowerEntry,
       "duxPowerIndex": duxPowerIndex,
       "duxPowerStatus": duxPowerStatus,
       "duxPowerFanStatus": duxPowerFanStatus,
       "duxPowerTraps": duxPowerTraps,
       "duxPowerFailedTrap": duxPowerFailedTrap,
       "duxPowerRecoveredTrap": duxPowerRecoveredTrap,
       "duxPowerFanFailedTrap": duxPowerFanFailedTrap,
       "duxPowerFanRecoveredTrap": duxPowerFanRecoveredTrap,
       "duxPanelFan": duxPanelFan,
       "duxPanelFanTable": duxPanelFanTable,
       "duxPanelFanEntry": duxPanelFanEntry,
       "duxPanelFanIndex": duxPanelFanIndex,
       "duxPanelFanStatus": duxPanelFanStatus,
       "duxPanelFanTraps": duxPanelFanTraps,
       "duxPanelFanFailedTrap": duxPanelFanFailedTrap,
       "duxPanelFanRecoveredTrap": duxPanelFanRecoveredTrap,
       "duxRefInput": duxRefInput,
       "duxRefInputTable": duxRefInputTable,
       "duxRefInputEntry": duxRefInputEntry,
       "duxRefInputIndex": duxRefInputIndex,
       "duxRefInputStatus": duxRefInputStatus,
       "duxSlot": duxSlot,
       "duxSlotTable": duxSlotTable,
       "duxSlotEntry": duxSlotEntry,
       "duxSlotIndex": duxSlotIndex,
       "duxSlotModuleType": duxSlotModuleType}
)
