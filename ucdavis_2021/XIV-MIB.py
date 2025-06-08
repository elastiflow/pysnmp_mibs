# SNMP MIB module (XIV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ucdavis_2021/XIV-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:49:14 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(ucdavis,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdavis")


# MODULE-IDENTITY

xivMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77)
)
if mibBuilder.loadTexts:
    xivMIB.setRevisions(
        ("2009-10-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_XivMachine_ObjectIdentity = ObjectIdentity
xivMachine = _XivMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1)
)
_XivStatus_ObjectIdentity = ObjectIdentity
xivStatus = _XivStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1)
)
_XivGlobalStatus_ObjectIdentity = ObjectIdentity
xivGlobalStatus = _XivGlobalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1)
)


class _XivMachineStatus_Type(OctetString):
    """Custom type xivMachineStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XivMachineStatus_Type.__name__ = "OctetString"
_XivMachineStatus_Object = MibScalar
xivMachineStatus = _XivMachineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1, 1),
    _XivMachineStatus_Type()
)
xivMachineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivMachineStatus.setStatus("current")
_XivFailedDisks_Type = Integer32
_XivFailedDisks_Object = MibScalar
xivFailedDisks = _XivFailedDisks_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1, 2),
    _XivFailedDisks_Type()
)
xivFailedDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivFailedDisks.setStatus("current")
_XivUtilizationSoft_Type = Gauge32
_XivUtilizationSoft_Object = MibScalar
xivUtilizationSoft = _XivUtilizationSoft_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1, 3),
    _XivUtilizationSoft_Type()
)
xivUtilizationSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivUtilizationSoft.setStatus("current")
_XivUtilizationHard_Type = Gauge32
_XivUtilizationHard_Object = MibScalar
xivUtilizationHard = _XivUtilizationHard_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1, 4),
    _XivUtilizationHard_Type()
)
xivUtilizationHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivUtilizationHard.setStatus("current")
_XivFreeSpaceSoft_Type = Integer32
_XivFreeSpaceSoft_Object = MibScalar
xivFreeSpaceSoft = _XivFreeSpaceSoft_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1, 5),
    _XivFreeSpaceSoft_Type()
)
xivFreeSpaceSoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivFreeSpaceSoft.setStatus("current")
_XivFreeSpaceHard_Type = Integer32
_XivFreeSpaceHard_Object = MibScalar
xivFreeSpaceHard = _XivFreeSpaceHard_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 1, 6),
    _XivFreeSpaceHard_Type()
)
xivFreeSpaceHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivFreeSpaceHard.setStatus("current")
_XivInterfaces_ObjectIdentity = ObjectIdentity
xivInterfaces = _XivInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2)
)
_XivIfTable_Object = MibTable
xivIfTable = _XivIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xivIfTable.setStatus("current")
_XivIfEntry_Object = MibTableRow
xivIfEntry = _XivIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2, 1, 1)
)
xivIfEntry.setIndexNames(
    (0, "XIV-MIB", "xivIfIndex"),
)
if mibBuilder.loadTexts:
    xivIfEntry.setStatus("current")
_XivIfIndex_Type = InterfaceIndex
_XivIfIndex_Object = MibTableColumn
xivIfIndex = _XivIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2, 1, 1, 1),
    _XivIfIndex_Type()
)
xivIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xivIfIndex.setStatus("current")
_XivIfIOPS_Type = Gauge32
_XivIfIOPS_Object = MibTableColumn
xivIfIOPS = _XivIfIOPS_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2, 1, 1, 2),
    _XivIfIOPS_Type()
)
xivIfIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivIfIOPS.setStatus("current")


class _XivIfStatus_Type(OctetString):
    """Custom type xivIfStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XivIfStatus_Type.__name__ = "OctetString"
_XivIfStatus_Object = MibTableColumn
xivIfStatus = _XivIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2, 1, 1, 3),
    _XivIfStatus_Type()
)
xivIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivIfStatus.setStatus("current")
_XivEventTrapInfo_ObjectIdentity = ObjectIdentity
xivEventTrapInfo = _XivEventTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 2)
)
_XivEventTrap_ObjectIdentity = ObjectIdentity
xivEventTrap = _XivEventTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 2, 0)
)
_XivEvents_ObjectIdentity = ObjectIdentity
xivEvents = _XivEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3)
)
_XivEventTable_Object = MibTable
xivEventTable = _XivEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xivEventTable.setStatus("current")
_XivEventEntry_Object = MibTableRow
xivEventEntry = _XivEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1)
)
xivEventEntry.setIndexNames(
    (0, "XIV-MIB", "xivEventIndex"),
)
if mibBuilder.loadTexts:
    xivEventEntry.setStatus("current")


class _XivEventIndex_Type(Integer32):
    """Custom type xivEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_XivEventIndex_Type.__name__ = "Integer32"
_XivEventIndex_Object = MibTableColumn
xivEventIndex = _XivEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1, 1),
    _XivEventIndex_Type()
)
xivEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xivEventIndex.setStatus("current")


class _XivEventCode_Type(DisplayString):
    """Custom type xivEventCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XivEventCode_Type.__name__ = "DisplayString"
_XivEventCode_Object = MibTableColumn
xivEventCode = _XivEventCode_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1, 2),
    _XivEventCode_Type()
)
xivEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivEventCode.setStatus("current")


class _XivEventTime_Type(DisplayString):
    """Custom type xivEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_XivEventTime_Type.__name__ = "DisplayString"
_XivEventTime_Object = MibTableColumn
xivEventTime = _XivEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1, 3),
    _XivEventTime_Type()
)
xivEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivEventTime.setStatus("current")
_XivEventDescription_Type = DisplayString
_XivEventDescription_Object = MibTableColumn
xivEventDescription = _XivEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1, 4),
    _XivEventDescription_Type()
)
xivEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivEventDescription.setStatus("current")


class _XivEventSeverity_Type(Integer32):
    """Custom type xivEventSeverity based on Integer32"""
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
        *(("informational", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_XivEventSeverity_Type.__name__ = "Integer32"
_XivEventSeverity_Object = MibTableColumn
xivEventSeverity = _XivEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1, 5),
    _XivEventSeverity_Type()
)
xivEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivEventSeverity.setStatus("current")
_XivEventTroubleshooting_Type = DisplayString
_XivEventTroubleshooting_Object = MibTableColumn
xivEventTroubleshooting = _XivEventTroubleshooting_Object(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 1, 1, 6),
    _XivEventTroubleshooting_Type()
)
xivEventTroubleshooting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xivEventTroubleshooting.setStatus("current")

# Managed Objects groups

xivInterfacesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 2, 100)
)
xivInterfacesGroup.setObjects(
      *(("XIV-MIB", "xivIfStatus"),
        ("XIV-MIB", "xivIfIOPS"))
)
if mibBuilder.loadTexts:
    xivInterfacesGroup.setStatus("current")

xivStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 1, 100)
)
xivStatusGroup.setObjects(
      *(("XIV-MIB", "xivMachineStatus"),
        ("XIV-MIB", "xivFreeSpaceSoft"),
        ("XIV-MIB", "xivFreeSpaceHard"),
        ("XIV-MIB", "xivFailedDisks"),
        ("XIV-MIB", "xivUtilizationSoft"),
        ("XIV-MIB", "xivUtilizationHard"))
)
if mibBuilder.loadTexts:
    xivStatusGroup.setStatus("current")

xivEventTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 2, 100)
)
xivEventTrapGroup.setObjects(
      *(("XIV-MIB", "xivEventCode"),
        ("XIV-MIB", "xivEventTime"),
        ("XIV-MIB", "xivEventDescription"),
        ("XIV-MIB", "xivEventSeverity"),
        ("XIV-MIB", "xivEventTroubleshooting"))
)
if mibBuilder.loadTexts:
    xivEventTrapGroup.setStatus("current")

xivEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 3, 100)
)
xivEventsGroup.setObjects(
      *(("XIV-MIB", "xivEventCode"),
        ("XIV-MIB", "xivEventTime"),
        ("XIV-MIB", "xivEventDescription"),
        ("XIV-MIB", "xivEventSeverity"),
        ("XIV-MIB", "xivEventTroubleshooting"))
)
if mibBuilder.loadTexts:
    xivEventsGroup.setStatus("current")


# Notification objects

xivTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    xivTrap.setStatus(
        "current"
    )


# Notifications groups

xivEventTrapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2021, 77, 1, 2, 101)
)
xivEventTrapNotificationGroup.setObjects(
    ("XIV-MIB", "xivTrap")
)
if mibBuilder.loadTexts:
    xivEventTrapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

xivCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2021, 77, 100)
)
xivCompliance.setObjects(
      *(("XIV-MIB", "xivStatusGroup"),
        ("XIV-MIB", "xivInterfacesGroup"),
        ("XIV-MIB", "xivEventsGroup"),
        ("XIV-MIB", "xivEventTrapGroup"),
        ("XIV-MIB", "xivEventTrapNotificationGroup"))
)
if mibBuilder.loadTexts:
    xivCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XIV-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "xivMIB": xivMIB,
       "xivMachine": xivMachine,
       "xivStatus": xivStatus,
       "xivGlobalStatus": xivGlobalStatus,
       "xivMachineStatus": xivMachineStatus,
       "xivFailedDisks": xivFailedDisks,
       "xivUtilizationSoft": xivUtilizationSoft,
       "xivUtilizationHard": xivUtilizationHard,
       "xivFreeSpaceSoft": xivFreeSpaceSoft,
       "xivFreeSpaceHard": xivFreeSpaceHard,
       "xivInterfaces": xivInterfaces,
       "xivIfTable": xivIfTable,
       "xivIfEntry": xivIfEntry,
       "xivIfIndex": xivIfIndex,
       "xivIfIOPS": xivIfIOPS,
       "xivIfStatus": xivIfStatus,
       "xivInterfacesGroup": xivInterfacesGroup,
       "xivStatusGroup": xivStatusGroup,
       "xivEventTrapInfo": xivEventTrapInfo,
       "xivEventTrap": xivEventTrap,
       "xivTrap": xivTrap,
       "xivEventTrapGroup": xivEventTrapGroup,
       "xivEventTrapNotificationGroup": xivEventTrapNotificationGroup,
       "xivEvents": xivEvents,
       "xivEventTable": xivEventTable,
       "xivEventEntry": xivEventEntry,
       "xivEventIndex": xivEventIndex,
       "xivEventCode": xivEventCode,
       "xivEventTime": xivEventTime,
       "xivEventDescription": xivEventDescription,
       "xivEventSeverity": xivEventSeverity,
       "xivEventTroubleshooting": xivEventTroubleshooting,
       "xivEventsGroup": xivEventsGroup,
       "xivCompliance": xivCompliance}
)
