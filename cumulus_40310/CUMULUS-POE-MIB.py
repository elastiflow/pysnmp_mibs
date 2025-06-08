# SNMP MIB module (CUMULUS-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cumulus_40310/CUMULUS-POE-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:08:37 2025
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

(cumulusMib,) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "cumulusMib")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

poeMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 3)
)
if mibBuilder.loadTexts:
    poeMIBObjects.setRevisions(
        ("2016-07-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_PoeSystemValues_ObjectIdentity = ObjectIdentity
poeSystemValues = _PoeSystemValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 3, 1)
)
_PoeTotalSystemPower_Type = MilliValue
_PoeTotalSystemPower_Object = MibScalar
poeTotalSystemPower = _PoeTotalSystemPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 1, 1),
    _PoeTotalSystemPower_Type()
)
poeTotalSystemPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeTotalSystemPower.setStatus("current")
if mibBuilder.loadTexts:
    poeTotalSystemPower.setUnits("milliwatts")
_PoeTotalUsedPower_Type = MilliValue
_PoeTotalUsedPower_Object = MibScalar
poeTotalUsedPower = _PoeTotalUsedPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 1, 2),
    _PoeTotalUsedPower_Type()
)
poeTotalUsedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeTotalUsedPower.setStatus("current")
if mibBuilder.loadTexts:
    poeTotalUsedPower.setUnits("milliwatts")
_PoeTotalAvailablePower_Type = MilliValue
_PoeTotalAvailablePower_Object = MibScalar
poeTotalAvailablePower = _PoeTotalAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 1, 3),
    _PoeTotalAvailablePower_Type()
)
poeTotalAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeTotalAvailablePower.setStatus("current")
if mibBuilder.loadTexts:
    poeTotalAvailablePower.setUnits("milliwatts")
_PoeLastUpdateTime_Type = TimeStamp
_PoeLastUpdateTime_Object = MibScalar
poeLastUpdateTime = _PoeLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 1, 4),
    _PoeLastUpdateTime_Type()
)
poeLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeLastUpdateTime.setStatus("current")
_PoeObjectsTable_Object = MibTable
poeObjectsTable = _PoeObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2)
)
if mibBuilder.loadTexts:
    poeObjectsTable.setStatus("current")
_PoeObjectsEntry_Object = MibTableRow
poeObjectsEntry = _PoeObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1)
)
poeObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    poeObjectsEntry.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 1),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2),
          ("critical", 3))
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 2),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPriority.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ieee802Dot3af", 2),
          ("ieee802Dot3at", 3),
          ("legacy", 4),
          ("highpower", 5),
          ("invalid", 6),
          ("ieee802Dot3afat", 7))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortStatus_Type(Integer32):
    """Custom type portStatus based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("searching", 3),
          ("connected", 4),
          ("powerdenied", 5),
          ("fault", 6))
    )


_PortStatus_Type.__name__ = "Integer32"
_PortStatus_Object = MibTableColumn
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 4),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatus.setStatus("current")


class _PortClass_Type(Integer32):
    """Custom type portClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("verylowpower", 1),
          ("lowpower", 2),
          ("midpower", 3),
          ("highpower", 4))
    )


_PortClass_Type.__name__ = "Integer32"
_PortClass_Object = MibTableColumn
portClass = _PortClass_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 5),
    _PortClass_Type()
)
portClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portClass.setStatus("current")


class _PortFourPairModeEnabled_Type(Integer32):
    """Custom type portFourPairModeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_PortFourPairModeEnabled_Type.__name__ = "Integer32"
_PortFourPairModeEnabled_Object = MibTableColumn
portFourPairModeEnabled = _PortFourPairModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 6),
    _PortFourPairModeEnabled_Type()
)
portFourPairModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFourPairModeEnabled.setStatus("current")
_PortVoltage_Type = MilliValue
_PortVoltage_Object = MibTableColumn
portVoltage = _PortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 7),
    _PortVoltage_Type()
)
portVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVoltage.setStatus("current")
if mibBuilder.loadTexts:
    portVoltage.setUnits("millivolts")
_PortCurrent_Type = MilliValue
_PortCurrent_Object = MibTableColumn
portCurrent = _PortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 8),
    _PortCurrent_Type()
)
portCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCurrent.setStatus("current")
if mibBuilder.loadTexts:
    portCurrent.setUnits("milliamps")
_PortPower_Type = MilliValue
_PortPower_Object = MibTableColumn
portPower = _PortPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 9),
    _PortPower_Type()
)
portPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPower.setStatus("current")
if mibBuilder.loadTexts:
    portPower.setUnits("milliwatts")
_PortMaxPower_Type = MilliValue
_PortMaxPower_Object = MibTableColumn
portMaxPower = _PortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 10),
    _PortMaxPower_Type()
)
portMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    portMaxPower.setUnits("milliwatts")
_PortAllocatedPower_Type = MilliValue
_PortAllocatedPower_Object = MibTableColumn
portAllocatedPower = _PortAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 11),
    _PortAllocatedPower_Type()
)
portAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllocatedPower.setStatus("current")
if mibBuilder.loadTexts:
    portAllocatedPower.setUnits("milliwatts")
_LldpRequestedPower_Type = MilliValue
_LldpRequestedPower_Object = MibTableColumn
lldpRequestedPower = _LldpRequestedPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 12),
    _LldpRequestedPower_Type()
)
lldpRequestedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRequestedPower.setStatus("current")
if mibBuilder.loadTexts:
    lldpRequestedPower.setUnits("milliwatts")
_LldpAllocatedPower_Type = MilliValue
_LldpAllocatedPower_Object = MibTableColumn
lldpAllocatedPower = _LldpAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 40310, 3, 2, 1, 13),
    _LldpAllocatedPower_Type()
)
lldpAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpAllocatedPower.setStatus("current")
if mibBuilder.loadTexts:
    lldpAllocatedPower.setUnits("milliwatts")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-POE-MIB",
    **{"MilliValue": MilliValue,
       "poeMIBObjects": poeMIBObjects,
       "poeSystemValues": poeSystemValues,
       "poeTotalSystemPower": poeTotalSystemPower,
       "poeTotalUsedPower": poeTotalUsedPower,
       "poeTotalAvailablePower": poeTotalAvailablePower,
       "poeLastUpdateTime": poeLastUpdateTime,
       "poeObjectsTable": poeObjectsTable,
       "poeObjectsEntry": poeObjectsEntry,
       "portName": portName,
       "portPriority": portPriority,
       "portType": portType,
       "portStatus": portStatus,
       "portClass": portClass,
       "portFourPairModeEnabled": portFourPairModeEnabled,
       "portVoltage": portVoltage,
       "portCurrent": portCurrent,
       "portPower": portPower,
       "portMaxPower": portMaxPower,
       "portAllocatedPower": portAllocatedPower,
       "lldpRequestedPower": lldpRequestedPower,
       "lldpAllocatedPower": lldpAllocatedPower}
)
