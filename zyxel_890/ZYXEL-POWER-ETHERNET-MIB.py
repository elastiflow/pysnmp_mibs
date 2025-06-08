# SNMP MIB module (ZYXEL-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-POWER-ETHERNET-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:36:30 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPoeSetup_ObjectIdentity = ObjectIdentity
zyxelPoeSetup = _ZyxelPoeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1)
)


class _ZyPoeMode_Type(Integer32):
    """Custom type zyPoeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("consumption", 0),
          ("classification", 1))
    )


_ZyPoeMode_Type.__name__ = "Integer32"
_ZyPoeMode_Object = MibScalar
zyPoeMode = _ZyPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 1),
    _ZyPoeMode_Type()
)
zyPoeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoeMode.setStatus("current")
_ZyxelPoePsePortTable_Object = MibTable
zyxelPoePsePortTable = _ZyxelPoePsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelPoePsePortTable.setStatus("current")
_ZyxelPoePsePortEntry_Object = MibTableRow
zyxelPoePsePortEntry = _ZyxelPoePsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1)
)
zyxelPoePsePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPoePsePortEntry.setStatus("current")
_ZyPoePsePortMaxPower_Type = Integer32
_ZyPoePsePortMaxPower_Object = MibTableColumn
zyPoePsePortMaxPower = _ZyPoePsePortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1, 1),
    _ZyPoePsePortMaxPower_Type()
)
zyPoePsePortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePsePortMaxPower.setStatus("current")


class _ZyPoePsePowerUp_Type(Integer32):
    """Custom type zyPoePsePowerUp based on Integer32"""
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
        *(("ieee802dot3af", 0),
          ("legacy", 1),
          ("preIeee802dot3at", 2),
          ("ieee802dot3at", 3))
    )


_ZyPoePsePowerUp_Type.__name__ = "Integer32"
_ZyPoePsePowerUp_Object = MibTableColumn
zyPoePsePowerUp = _ZyPoePsePowerUp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1, 2),
    _ZyPoePsePowerUp_Type()
)
zyPoePsePowerUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePsePowerUp.setStatus("current")
_ZyPoePsePortTimeRange_Type = DisplayString
_ZyPoePsePortTimeRange_Object = MibTableColumn
zyPoePsePortTimeRange = _ZyPoePsePortTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1, 3),
    _ZyPoePsePortTimeRange_Type()
)
zyPoePsePortTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePsePortTimeRange.setStatus("current")
_ZyPoePseWideRangeDetection_Type = EnabledStatus
_ZyPoePseWideRangeDetection_Object = MibTableColumn
zyPoePseWideRangeDetection = _ZyPoePseWideRangeDetection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1, 4),
    _ZyPoePseWideRangeDetection_Type()
)
zyPoePseWideRangeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePseWideRangeDetection.setStatus("current")
_ZyPoePreAllocate_Type = EnabledStatus
_ZyPoePreAllocate_Object = MibScalar
zyPoePreAllocate = _ZyPoePreAllocate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 3),
    _ZyPoePreAllocate_Type()
)
zyPoePreAllocate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePreAllocate.setStatus("current")
_ZyPoeDualDetection_Type = EnabledStatus
_ZyPoeDualDetection_Object = MibScalar
zyPoeDualDetection = _ZyPoeDualDetection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 4),
    _ZyPoeDualDetection_Type()
)
zyPoeDualDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoeDualDetection.setStatus("current")
_ZyPoePowerSequenceDelay_Type = EnabledStatus
_ZyPoePowerSequenceDelay_Object = MibScalar
zyPoePowerSequenceDelay = _ZyPoePowerSequenceDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 5),
    _ZyPoePowerSequenceDelay_Type()
)
zyPoePowerSequenceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePowerSequenceDelay.setStatus("current")
_ZyxelPoePsePortTimeRangeTable_Object = MibTable
zyxelPoePsePortTimeRangeTable = _ZyxelPoePsePortTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelPoePsePortTimeRangeTable.setStatus("current")
_ZyxelPoePsePortTimeRangeEntry_Object = MibTableRow
zyxelPoePsePortTimeRangeEntry = _ZyxelPoePsePortTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 6, 1)
)
zyxelPoePsePortTimeRangeEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-POWER-ETHERNET-MIB", "zyxelPoePsePortTimeRangeName"),
)
if mibBuilder.loadTexts:
    zyxelPoePsePortTimeRangeEntry.setStatus("current")
_ZyPoePsePortTimeRangeName_Type = DisplayString
_ZyPoePsePortTimeRangeName_Object = MibTableColumn
zyPoePsePortTimeRangeName = _ZyPoePsePortTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 6, 1, 1),
    _ZyPoePsePortTimeRangeName_Type()
)
zyPoePsePortTimeRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPoePsePortTimeRangeName.setStatus("current")
_ZyPoePsePortTimeRangeRowStatus_Type = RowStatus
_ZyPoePsePortTimeRangeRowStatus_Object = MibTableColumn
zyPoePsePortTimeRangeRowStatus = _ZyPoePsePortTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 6, 1, 2),
    _ZyPoePsePortTimeRangeRowStatus_Type()
)
zyPoePsePortTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyPoePsePortTimeRangeRowStatus.setStatus("current")
_ZyxelPoeStatus_ObjectIdentity = ObjectIdentity
zyxelPoeStatus = _ZyxelPoeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2)
)
_ZyxelPoePsePortInfoTable_Object = MibTable
zyxelPoePsePortInfoTable = _ZyxelPoePsePortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelPoePsePortInfoTable.setStatus("current")
_ZyxelPoePsePortInfoEntry_Object = MibTableRow
zyxelPoePsePortInfoEntry = _ZyxelPoePsePortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1)
)
zyxelPoePsePortInfoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPoePsePortInfoEntry.setStatus("current")
_ZyPoePsePortInfoPowerConsumption_Type = Integer32
_ZyPoePsePortInfoPowerConsumption_Object = MibTableColumn
zyPoePsePortInfoPowerConsumption = _ZyPoePsePortInfoPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1, 1),
    _ZyPoePsePortInfoPowerConsumption_Type()
)
zyPoePsePortInfoPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPoePsePortInfoPowerConsumption.setStatus("current")


class _ZyPoePsePortTimeRangeState_Type(Integer32):
    """Custom type zyPoePsePortTimeRangeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("in", 1),
          ("out", 2))
    )


_ZyPoePsePortTimeRangeState_Type.__name__ = "Integer32"
_ZyPoePsePortTimeRangeState_Object = MibTableColumn
zyPoePsePortTimeRangeState = _ZyPoePsePortTimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1, 2),
    _ZyPoePsePortTimeRangeState_Type()
)
zyPoePsePortTimeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPoePsePortTimeRangeState.setStatus("current")
_ZyPoePsePortTimeRangeInProfile_Type = DisplayString
_ZyPoePsePortTimeRangeInProfile_Object = MibTableColumn
zyPoePsePortTimeRangeInProfile = _ZyPoePsePortTimeRangeInProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1, 3),
    _ZyPoePsePortTimeRangeInProfile_Type()
)
zyPoePsePortTimeRangeInProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPoePsePortTimeRangeInProfile.setStatus("current")
_ZyxelPoeTrapInfoObject_ObjectIdentity = ObjectIdentity
zyxelPoeTrapInfoObject = _ZyxelPoeTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 3)
)


class _ZyPoeTrapPsePowerSupplyFailedReason_Type(Integer32):
    """Custom type zyPoeTrapPsePowerSupplyFailedReason based on Integer32"""
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
        *(("internalPowerSupplyForPoeFailed", 0),
          ("rpsForPoeFailed", 1),
          ("rpsFanFailed", 2),
          ("rpsOverTemperature", 3))
    )


_ZyPoeTrapPsePowerSupplyFailedReason_Type.__name__ = "Integer32"
_ZyPoeTrapPsePowerSupplyFailedReason_Object = MibScalar
zyPoeTrapPsePowerSupplyFailedReason = _ZyPoeTrapPsePowerSupplyFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 3, 1),
    _ZyPoeTrapPsePowerSupplyFailedReason_Type()
)
zyPoeTrapPsePowerSupplyFailedReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPoeTrapPsePowerSupplyFailedReason.setStatus("current")
_ZyxelPoeNotifications_ObjectIdentity = ObjectIdentity
zyxelPoeNotifications = _ZyxelPoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4)
)

# Managed Objects groups


# Notification objects

zyPoePowerPortOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 1)
)
zyPoePowerPortOverload.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverload.setStatus(
        "current"
    )

zyPoePowerPortShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 2)
)
zyPoePowerPortShortCircuit.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortShortCircuit.setStatus(
        "current"
    )

zyPoePowerPortOverSystemBudget = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 3)
)
zyPoePowerPortOverSystemBudget.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverSystemBudget.setStatus(
        "current"
    )

zyPoePsePowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 4)
)
zyPoePsePowerSupplyFailed.setObjects(
    ("ZYXEL-POWER-ETHERNET-MIB", "zyPoeTrapPsePowerSupplyFailedReason")
)
if mibBuilder.loadTexts:
    zyPoePsePowerSupplyFailed.setStatus(
        "current"
    )

zyPoePowerPortOverloadRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 5)
)
zyPoePowerPortOverloadRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverloadRecovered.setStatus(
        "current"
    )

zyPoePowerPortShortCircuitRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 6)
)
zyPoePowerPortShortCircuitRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortShortCircuitRecovered.setStatus(
        "current"
    )

zyPoePowerPortOverSystemBudgetRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 7)
)
zyPoePowerPortOverSystemBudgetRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverSystemBudgetRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-POWER-ETHERNET-MIB",
    **{"zyxelPoe": zyxelPoe,
       "zyxelPoeSetup": zyxelPoeSetup,
       "zyPoeMode": zyPoeMode,
       "zyxelPoePsePortTable": zyxelPoePsePortTable,
       "zyxelPoePsePortEntry": zyxelPoePsePortEntry,
       "zyPoePsePortMaxPower": zyPoePsePortMaxPower,
       "zyPoePsePowerUp": zyPoePsePowerUp,
       "zyPoePsePortTimeRange": zyPoePsePortTimeRange,
       "zyPoePseWideRangeDetection": zyPoePseWideRangeDetection,
       "zyPoePreAllocate": zyPoePreAllocate,
       "zyPoeDualDetection": zyPoeDualDetection,
       "zyPoePowerSequenceDelay": zyPoePowerSequenceDelay,
       "zyxelPoePsePortTimeRangeTable": zyxelPoePsePortTimeRangeTable,
       "zyxelPoePsePortTimeRangeEntry": zyxelPoePsePortTimeRangeEntry,
       "zyPoePsePortTimeRangeName": zyPoePsePortTimeRangeName,
       "zyPoePsePortTimeRangeRowStatus": zyPoePsePortTimeRangeRowStatus,
       "zyxelPoeStatus": zyxelPoeStatus,
       "zyxelPoePsePortInfoTable": zyxelPoePsePortInfoTable,
       "zyxelPoePsePortInfoEntry": zyxelPoePsePortInfoEntry,
       "zyPoePsePortInfoPowerConsumption": zyPoePsePortInfoPowerConsumption,
       "zyPoePsePortTimeRangeState": zyPoePsePortTimeRangeState,
       "zyPoePsePortTimeRangeInProfile": zyPoePsePortTimeRangeInProfile,
       "zyxelPoeTrapInfoObject": zyxelPoeTrapInfoObject,
       "zyPoeTrapPsePowerSupplyFailedReason": zyPoeTrapPsePowerSupplyFailedReason,
       "zyxelPoeNotifications": zyxelPoeNotifications,
       "zyPoePowerPortOverload": zyPoePowerPortOverload,
       "zyPoePowerPortShortCircuit": zyPoePowerPortShortCircuit,
       "zyPoePowerPortOverSystemBudget": zyPoePowerPortOverSystemBudget,
       "zyPoePsePowerSupplyFailed": zyPoePsePowerSupplyFailed,
       "zyPoePowerPortOverloadRecovered": zyPoePowerPortOverloadRecovered,
       "zyPoePowerPortShortCircuitRecovered": zyPoePowerPortShortCircuitRecovered,
       "zyPoePowerPortOverSystemBudgetRecovered": zyPoePowerPortOverSystemBudgetRecovered}
)
