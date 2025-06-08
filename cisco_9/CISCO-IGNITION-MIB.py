# SNMP MIB module (CISCO-IGNITION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IGNITION-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:28 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIgnitionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061)
)
if mibBuilder.loadTexts:
    ciscoIgnitionMIB.setRevisions(
        ("2023-06-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IgnitionStatus(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bootloader", 0),
          ("powerOn", 1),
          ("lowDelay", 2),
          ("offDelay", 3),
          ("highDelay", 4),
          ("onDelay", 5),
          ("monitor", 6),
          ("sleep", 7),
          ("unknown", 8))
    )



# MIB Managed Objects in the order of their OIDs

_IpmMIBStatus_ObjectIdentity = ObjectIdentity
ipmMIBStatus = _IpmMIBStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0)
)
_IpmIgnitionStatusTable_Object = MibTable
ipmIgnitionStatusTable = _IpmIgnitionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1)
)
if mibBuilder.loadTexts:
    ipmIgnitionStatusTable.setStatus("current")
_IpmIgnitionStatusEntry_Object = MibTableRow
ipmIgnitionStatusEntry = _IpmIgnitionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1)
)
ipmIgnitionStatusEntry.setIndexNames(
    (0, "CISCO-IGNITION-MIB", "ipmIgnitionStatusIndex"),
)
if mibBuilder.loadTexts:
    ipmIgnitionStatusEntry.setStatus("current")
_IpmIgnitionStatusIndex_Type = Integer32
_IpmIgnitionStatusIndex_Object = MibTableColumn
ipmIgnitionStatusIndex = _IpmIgnitionStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 1),
    _IpmIgnitionStatusIndex_Type()
)
ipmIgnitionStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIgnitionStatusIndex.setStatus("current")
_IpmIgnitionManagement_Type = TruthValue
_IpmIgnitionManagement_Object = MibTableColumn
ipmIgnitionManagement = _IpmIgnitionManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 2),
    _IpmIgnitionManagement_Type()
)
ipmIgnitionManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIgnitionManagement.setStatus("current")
_IpmInputVoltage_Type = Unsigned32
_IpmInputVoltage_Object = MibTableColumn
ipmInputVoltage = _IpmInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 3),
    _IpmInputVoltage_Type()
)
ipmInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmInputVoltage.setStatus("current")
_IpmIgnitionStatus_Type = IgnitionStatus
_IpmIgnitionStatus_Object = MibTableColumn
ipmIgnitionStatus = _IpmIgnitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 4),
    _IpmIgnitionStatus_Type()
)
ipmIgnitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIgnitionStatus.setStatus("current")
_IpmIgnitionSense_Type = TruthValue
_IpmIgnitionSense_Object = MibTableColumn
ipmIgnitionSense = _IpmIgnitionSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 5),
    _IpmIgnitionSense_Type()
)
ipmIgnitionSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIgnitionSense.setStatus("current")
_IpmShutdownTimer_Type = Unsigned32
_IpmShutdownTimer_Object = MibTableColumn
ipmShutdownTimer = _IpmShutdownTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 6),
    _IpmShutdownTimer_Type()
)
ipmShutdownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmShutdownTimer.setStatus("current")
_IpmConfigBattery_Type = Integer32
_IpmConfigBattery_Object = MibTableColumn
ipmConfigBattery = _IpmConfigBattery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 0, 1, 1, 7),
    _IpmConfigBattery_Type()
)
ipmConfigBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmConfigBattery.setStatus("current")
_IpmMIBThreshold_ObjectIdentity = ObjectIdentity
ipmMIBThreshold = _IpmMIBThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1)
)
_IpmIgnitionThresholdTable_Object = MibTable
ipmIgnitionThresholdTable = _IpmIgnitionThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1)
)
if mibBuilder.loadTexts:
    ipmIgnitionThresholdTable.setStatus("current")
_IpmIgnitionThresholdEntry_Object = MibTableRow
ipmIgnitionThresholdEntry = _IpmIgnitionThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1)
)
ipmIgnitionThresholdEntry.setIndexNames(
    (0, "CISCO-IGNITION-MIB", "ipmIgnitionThresholdIndex"),
)
if mibBuilder.loadTexts:
    ipmIgnitionThresholdEntry.setStatus("current")
_IpmIgnitionThresholdIndex_Type = Integer32
_IpmIgnitionThresholdIndex_Object = MibTableColumn
ipmIgnitionThresholdIndex = _IpmIgnitionThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 1),
    _IpmIgnitionThresholdIndex_Type()
)
ipmIgnitionThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIgnitionThresholdIndex.setStatus("current")
_IpmUndervoltage_Type = Unsigned32
_IpmUndervoltage_Object = MibTableColumn
ipmUndervoltage = _IpmUndervoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 2),
    _IpmUndervoltage_Type()
)
ipmUndervoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmUndervoltage.setStatus("current")
_IpmOvervoltage_Type = Unsigned32
_IpmOvervoltage_Object = MibTableColumn
ipmOvervoltage = _IpmOvervoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 3),
    _IpmOvervoltage_Type()
)
ipmOvervoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmOvervoltage.setStatus("current")
_IpmSenseOn_Type = Unsigned32
_IpmSenseOn_Object = MibTableColumn
ipmSenseOn = _IpmSenseOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 4),
    _IpmSenseOn_Type()
)
ipmSenseOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmSenseOn.setStatus("current")
_IpmSenseOff_Type = Unsigned32
_IpmSenseOff_Object = MibTableColumn
ipmSenseOff = _IpmSenseOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 5),
    _IpmSenseOff_Type()
)
ipmSenseOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmSenseOff.setStatus("current")
_IpmUndervoltageTimer_Type = Unsigned32
_IpmUndervoltageTimer_Object = MibTableColumn
ipmUndervoltageTimer = _IpmUndervoltageTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 6),
    _IpmUndervoltageTimer_Type()
)
ipmUndervoltageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmUndervoltageTimer.setStatus("current")
_IpmOvervoltageTimer_Type = Unsigned32
_IpmOvervoltageTimer_Object = MibTableColumn
ipmOvervoltageTimer = _IpmOvervoltageTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 7),
    _IpmOvervoltageTimer_Type()
)
ipmOvervoltageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmOvervoltageTimer.setStatus("current")
_IpmIgnitionOffTimer_Type = Unsigned32
_IpmIgnitionOffTimer_Object = MibTableColumn
ipmIgnitionOffTimer = _IpmIgnitionOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 1, 1, 1, 8),
    _IpmIgnitionOffTimer_Type()
)
ipmIgnitionOffTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmIgnitionOffTimer.setStatus("current")
_IpmMIBConform_ObjectIdentity = ObjectIdentity
ipmMIBConform = _IpmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 2)
)
_IpmMIBCompliance_ObjectIdentity = ObjectIdentity
ipmMIBCompliance = _IpmMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 2, 1)
)
_IpmMIBGroups_ObjectIdentity = ObjectIdentity
ipmMIBGroups = _IpmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 2, 2)
)

# Managed Objects groups

ipmIgnitionStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 2, 2, 1)
)
ipmIgnitionStatusMIBGroup.setObjects(
      *(("CISCO-IGNITION-MIB", "ipmIgnitionManagement"),
        ("CISCO-IGNITION-MIB", "ipmInputVoltage"),
        ("CISCO-IGNITION-MIB", "ipmIgnitionStatus"),
        ("CISCO-IGNITION-MIB", "ipmIgnitionSense"),
        ("CISCO-IGNITION-MIB", "ipmShutdownTimer"),
        ("CISCO-IGNITION-MIB", "ipmConfigBattery"))
)
if mibBuilder.loadTexts:
    ipmIgnitionStatusMIBGroup.setStatus("current")

ipmIgnitionThresholdMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 2, 2, 2)
)
ipmIgnitionThresholdMIBGroup.setObjects(
      *(("CISCO-IGNITION-MIB", "ipmUndervoltage"),
        ("CISCO-IGNITION-MIB", "ipmOvervoltage"),
        ("CISCO-IGNITION-MIB", "ipmSenseOn"),
        ("CISCO-IGNITION-MIB", "ipmSenseOff"),
        ("CISCO-IGNITION-MIB", "ipmUndervoltageTimer"),
        ("CISCO-IGNITION-MIB", "ipmOvervoltageTimer"),
        ("CISCO-IGNITION-MIB", "ipmIgnitionOffTimer"))
)
if mibBuilder.loadTexts:
    ipmIgnitionThresholdMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipmMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1061, 2, 1, 1)
)
ipmMIBCompliances.setObjects(
      *(("CISCO-IGNITION-MIB", "ipmIgnitionStatusMIBGroup"),
        ("CISCO-IGNITION-MIB", "ipmIgnitionThresholdMIBGroup"))
)
if mibBuilder.loadTexts:
    ipmMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IGNITION-MIB",
    **{"IgnitionStatus": IgnitionStatus,
       "ciscoIgnitionMIB": ciscoIgnitionMIB,
       "ipmMIBStatus": ipmMIBStatus,
       "ipmIgnitionStatusTable": ipmIgnitionStatusTable,
       "ipmIgnitionStatusEntry": ipmIgnitionStatusEntry,
       "ipmIgnitionStatusIndex": ipmIgnitionStatusIndex,
       "ipmIgnitionManagement": ipmIgnitionManagement,
       "ipmInputVoltage": ipmInputVoltage,
       "ipmIgnitionStatus": ipmIgnitionStatus,
       "ipmIgnitionSense": ipmIgnitionSense,
       "ipmShutdownTimer": ipmShutdownTimer,
       "ipmConfigBattery": ipmConfigBattery,
       "ipmMIBThreshold": ipmMIBThreshold,
       "ipmIgnitionThresholdTable": ipmIgnitionThresholdTable,
       "ipmIgnitionThresholdEntry": ipmIgnitionThresholdEntry,
       "ipmIgnitionThresholdIndex": ipmIgnitionThresholdIndex,
       "ipmUndervoltage": ipmUndervoltage,
       "ipmOvervoltage": ipmOvervoltage,
       "ipmSenseOn": ipmSenseOn,
       "ipmSenseOff": ipmSenseOff,
       "ipmUndervoltageTimer": ipmUndervoltageTimer,
       "ipmOvervoltageTimer": ipmOvervoltageTimer,
       "ipmIgnitionOffTimer": ipmIgnitionOffTimer,
       "ipmMIBConform": ipmMIBConform,
       "ipmMIBCompliance": ipmMIBCompliance,
       "ipmMIBCompliances": ipmMIBCompliances,
       "ipmMIBGroups": ipmMIBGroups,
       "ipmIgnitionStatusMIBGroup": ipmIgnitionStatusMIBGroup,
       "ipmIgnitionThresholdMIBGroup": ipmIgnitionThresholdMIBGroup}
)
