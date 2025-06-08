# SNMP MIB module (ME1200-LOOP-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-LOOP-PROTECTION-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200InterfaceIndex,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex")

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

me1200LoopProtectionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91)
)
if mibBuilder.loadTexts:
    me1200LoopProtectionMib.setRevisions(
        ("2016-04-27 00:00",
         "2014-03-11 00:00",
         "2014-02-10 00:00",
         "2014-01-29 00:00",
         "2014-01-27 00:00",
         "2014-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200LoopProtectionAction(TextualConvention, Integer32):
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
        *(("shutdown", 0),
          ("shutdownAndLogEvent", 1),
          ("logEvent", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200LoopProtectionObjects_ObjectIdentity = ObjectIdentity
me1200LoopProtectionObjects = _Me1200LoopProtectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1)
)
_Me1200LoopProtectionConfig_ObjectIdentity = ObjectIdentity
me1200LoopProtectionConfig = _Me1200LoopProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2)
)
_Me1200LoopProtectionGlobals_ObjectIdentity = ObjectIdentity
me1200LoopProtectionGlobals = _Me1200LoopProtectionGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 1)
)
_Me1200LoopProtectionGlobalsEnabled_Type = TruthValue
_Me1200LoopProtectionGlobalsEnabled_Object = MibScalar
me1200LoopProtectionGlobalsEnabled = _Me1200LoopProtectionGlobalsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 1, 1),
    _Me1200LoopProtectionGlobalsEnabled_Type()
)
me1200LoopProtectionGlobalsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LoopProtectionGlobalsEnabled.setStatus("current")
_Me1200LoopProtectionGlobalsTransmitInterval_Type = Integer32
_Me1200LoopProtectionGlobalsTransmitInterval_Object = MibScalar
me1200LoopProtectionGlobalsTransmitInterval = _Me1200LoopProtectionGlobalsTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 1, 2),
    _Me1200LoopProtectionGlobalsTransmitInterval_Type()
)
me1200LoopProtectionGlobalsTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LoopProtectionGlobalsTransmitInterval.setStatus("current")
_Me1200LoopProtectionGlobalsShutdownPeriod_Type = Integer32
_Me1200LoopProtectionGlobalsShutdownPeriod_Object = MibScalar
me1200LoopProtectionGlobalsShutdownPeriod = _Me1200LoopProtectionGlobalsShutdownPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 1, 3),
    _Me1200LoopProtectionGlobalsShutdownPeriod_Type()
)
me1200LoopProtectionGlobalsShutdownPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LoopProtectionGlobalsShutdownPeriod.setStatus("current")
_Me1200LoopProtectionConfigInterface_ObjectIdentity = ObjectIdentity
me1200LoopProtectionConfigInterface = _Me1200LoopProtectionConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2)
)
_Me1200LoopProtectionInterfaceParamTable_Object = MibTable
me1200LoopProtectionInterfaceParamTable = _Me1200LoopProtectionInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamTable.setStatus("current")
_Me1200LoopProtectionInterfaceParamEntry_Object = MibTableRow
me1200LoopProtectionInterfaceParamEntry = _Me1200LoopProtectionInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2, 1, 1)
)
me1200LoopProtectionInterfaceParamEntry.setIndexNames(
    (0, "ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceParamIfIndex"),
)
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamEntry.setStatus("current")
_Me1200LoopProtectionInterfaceParamIfIndex_Type = ME1200InterfaceIndex
_Me1200LoopProtectionInterfaceParamIfIndex_Object = MibTableColumn
me1200LoopProtectionInterfaceParamIfIndex = _Me1200LoopProtectionInterfaceParamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2, 1, 1, 1),
    _Me1200LoopProtectionInterfaceParamIfIndex_Type()
)
me1200LoopProtectionInterfaceParamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamIfIndex.setStatus("current")
_Me1200LoopProtectionInterfaceParamEnabled_Type = TruthValue
_Me1200LoopProtectionInterfaceParamEnabled_Object = MibTableColumn
me1200LoopProtectionInterfaceParamEnabled = _Me1200LoopProtectionInterfaceParamEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2, 1, 1, 2),
    _Me1200LoopProtectionInterfaceParamEnabled_Type()
)
me1200LoopProtectionInterfaceParamEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamEnabled.setStatus("current")
_Me1200LoopProtectionInterfaceParamAction_Type = ME1200LoopProtectionAction
_Me1200LoopProtectionInterfaceParamAction_Object = MibTableColumn
me1200LoopProtectionInterfaceParamAction = _Me1200LoopProtectionInterfaceParamAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2, 1, 1, 3),
    _Me1200LoopProtectionInterfaceParamAction_Type()
)
me1200LoopProtectionInterfaceParamAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamAction.setStatus("current")
_Me1200LoopProtectionInterfaceParamTransmit_Type = TruthValue
_Me1200LoopProtectionInterfaceParamTransmit_Object = MibTableColumn
me1200LoopProtectionInterfaceParamTransmit = _Me1200LoopProtectionInterfaceParamTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 2, 2, 1, 1, 4),
    _Me1200LoopProtectionInterfaceParamTransmit_Type()
)
me1200LoopProtectionInterfaceParamTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamTransmit.setStatus("current")
_Me1200LoopProtectionStatus_ObjectIdentity = ObjectIdentity
me1200LoopProtectionStatus = _Me1200LoopProtectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3)
)
_Me1200LoopProtectionStatusInterface_ObjectIdentity = ObjectIdentity
me1200LoopProtectionStatusInterface = _Me1200LoopProtectionStatusInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2)
)
_Me1200LoopProtectionInterfaceStatusTable_Object = MibTable
me1200LoopProtectionInterfaceStatusTable = _Me1200LoopProtectionInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusTable.setStatus("current")
_Me1200LoopProtectionInterfaceStatusEntry_Object = MibTableRow
me1200LoopProtectionInterfaceStatusEntry = _Me1200LoopProtectionInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1, 1)
)
me1200LoopProtectionInterfaceStatusEntry.setIndexNames(
    (0, "ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusIfIndex"),
)
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusEntry.setStatus("current")
_Me1200LoopProtectionInterfaceStatusIfIndex_Type = ME1200InterfaceIndex
_Me1200LoopProtectionInterfaceStatusIfIndex_Object = MibTableColumn
me1200LoopProtectionInterfaceStatusIfIndex = _Me1200LoopProtectionInterfaceStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1, 1, 1),
    _Me1200LoopProtectionInterfaceStatusIfIndex_Type()
)
me1200LoopProtectionInterfaceStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusIfIndex.setStatus("current")
_Me1200LoopProtectionInterfaceStatusDisabled_Type = TruthValue
_Me1200LoopProtectionInterfaceStatusDisabled_Object = MibTableColumn
me1200LoopProtectionInterfaceStatusDisabled = _Me1200LoopProtectionInterfaceStatusDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1, 1, 2),
    _Me1200LoopProtectionInterfaceStatusDisabled_Type()
)
me1200LoopProtectionInterfaceStatusDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusDisabled.setStatus("current")
_Me1200LoopProtectionInterfaceStatusLoopDetected_Type = TruthValue
_Me1200LoopProtectionInterfaceStatusLoopDetected_Object = MibTableColumn
me1200LoopProtectionInterfaceStatusLoopDetected = _Me1200LoopProtectionInterfaceStatusLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1, 1, 3),
    _Me1200LoopProtectionInterfaceStatusLoopDetected_Type()
)
me1200LoopProtectionInterfaceStatusLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusLoopDetected.setStatus("current")
_Me1200LoopProtectionInterfaceStatusLoopCount_Type = Unsigned32
_Me1200LoopProtectionInterfaceStatusLoopCount_Object = MibTableColumn
me1200LoopProtectionInterfaceStatusLoopCount = _Me1200LoopProtectionInterfaceStatusLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1, 1, 4),
    _Me1200LoopProtectionInterfaceStatusLoopCount_Type()
)
me1200LoopProtectionInterfaceStatusLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusLoopCount.setStatus("current")
_Me1200LoopProtectionInterfaceStatusLastLoop_Type = Integer32
_Me1200LoopProtectionInterfaceStatusLastLoop_Object = MibTableColumn
me1200LoopProtectionInterfaceStatusLastLoop = _Me1200LoopProtectionInterfaceStatusLastLoop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 3, 2, 1, 1, 5),
    _Me1200LoopProtectionInterfaceStatusLastLoop_Type()
)
me1200LoopProtectionInterfaceStatusLastLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusLastLoop.setStatus("current")
_Me1200LoopProtectionNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200LoopProtectionNotificationPrefix = _Me1200LoopProtectionNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 4)
)
_Me1200LoopProtectionNotification_ObjectIdentity = ObjectIdentity
me1200LoopProtectionNotification = _Me1200LoopProtectionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 4, 0)
)
_Me1200LoopProtectionMibConformance_ObjectIdentity = ObjectIdentity
me1200LoopProtectionMibConformance = _Me1200LoopProtectionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2)
)
_Me1200LoopProtectionMibCompliances_ObjectIdentity = ObjectIdentity
me1200LoopProtectionMibCompliances = _Me1200LoopProtectionMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 1)
)
_Me1200LoopProtectionMibGroups_ObjectIdentity = ObjectIdentity
me1200LoopProtectionMibGroups = _Me1200LoopProtectionMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 2)
)

# Managed Objects groups

me1200LoopProtectionGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 2, 1)
)
me1200LoopProtectionGlobalsInfoGroup.setObjects(
      *(("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionGlobalsEnabled"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionGlobalsTransmitInterval"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionGlobalsShutdownPeriod"))
)
if mibBuilder.loadTexts:
    me1200LoopProtectionGlobalsInfoGroup.setStatus("current")

me1200LoopProtectionInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 2, 2)
)
me1200LoopProtectionInterfaceParamTableInfoGroup.setObjects(
      *(("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceParamEnabled"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceParamAction"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceParamTransmit"))
)
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceParamTableInfoGroup.setStatus("current")

me1200LoopProtectionInterfaceStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 2, 3)
)
me1200LoopProtectionInterfaceStatusTableInfoGroup.setObjects(
      *(("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusDisabled"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusLoopDetected"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusLoopCount"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusLastLoop"))
)
if mibBuilder.loadTexts:
    me1200LoopProtectionInterfaceStatusTableInfoGroup.setStatus("current")


# Notification objects

me1200LoopProtectionNotificationLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 1, 4, 0, 1)
)
me1200LoopProtectionNotificationLoopDetected.setObjects(
      *(("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusLoopCount"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusLastLoop"))
)
if mibBuilder.loadTexts:
    me1200LoopProtectionNotificationLoopDetected.setStatus(
        "current"
    )


# Notifications groups

me1200LoopProtectionNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 2, 4)
)
me1200LoopProtectionNotificationInfoGroup.setObjects(
    ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionNotificationLoopDetected")
)
if mibBuilder.loadTexts:
    me1200LoopProtectionNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200LoopProtectionMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 91, 2, 1, 1)
)
me1200LoopProtectionMibCompliance.setObjects(
      *(("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionGlobalsInfoGroup"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceParamTableInfoGroup"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionInterfaceStatusTableInfoGroup"),
        ("ME1200-LOOP-PROTECTION-MIB", "me1200LoopProtectionNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200LoopProtectionMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-LOOP-PROTECTION-MIB",
    **{"ME1200LoopProtectionAction": ME1200LoopProtectionAction,
       "me1200LoopProtectionMib": me1200LoopProtectionMib,
       "me1200LoopProtectionObjects": me1200LoopProtectionObjects,
       "me1200LoopProtectionConfig": me1200LoopProtectionConfig,
       "me1200LoopProtectionGlobals": me1200LoopProtectionGlobals,
       "me1200LoopProtectionGlobalsEnabled": me1200LoopProtectionGlobalsEnabled,
       "me1200LoopProtectionGlobalsTransmitInterval": me1200LoopProtectionGlobalsTransmitInterval,
       "me1200LoopProtectionGlobalsShutdownPeriod": me1200LoopProtectionGlobalsShutdownPeriod,
       "me1200LoopProtectionConfigInterface": me1200LoopProtectionConfigInterface,
       "me1200LoopProtectionInterfaceParamTable": me1200LoopProtectionInterfaceParamTable,
       "me1200LoopProtectionInterfaceParamEntry": me1200LoopProtectionInterfaceParamEntry,
       "me1200LoopProtectionInterfaceParamIfIndex": me1200LoopProtectionInterfaceParamIfIndex,
       "me1200LoopProtectionInterfaceParamEnabled": me1200LoopProtectionInterfaceParamEnabled,
       "me1200LoopProtectionInterfaceParamAction": me1200LoopProtectionInterfaceParamAction,
       "me1200LoopProtectionInterfaceParamTransmit": me1200LoopProtectionInterfaceParamTransmit,
       "me1200LoopProtectionStatus": me1200LoopProtectionStatus,
       "me1200LoopProtectionStatusInterface": me1200LoopProtectionStatusInterface,
       "me1200LoopProtectionInterfaceStatusTable": me1200LoopProtectionInterfaceStatusTable,
       "me1200LoopProtectionInterfaceStatusEntry": me1200LoopProtectionInterfaceStatusEntry,
       "me1200LoopProtectionInterfaceStatusIfIndex": me1200LoopProtectionInterfaceStatusIfIndex,
       "me1200LoopProtectionInterfaceStatusDisabled": me1200LoopProtectionInterfaceStatusDisabled,
       "me1200LoopProtectionInterfaceStatusLoopDetected": me1200LoopProtectionInterfaceStatusLoopDetected,
       "me1200LoopProtectionInterfaceStatusLoopCount": me1200LoopProtectionInterfaceStatusLoopCount,
       "me1200LoopProtectionInterfaceStatusLastLoop": me1200LoopProtectionInterfaceStatusLastLoop,
       "me1200LoopProtectionNotificationPrefix": me1200LoopProtectionNotificationPrefix,
       "me1200LoopProtectionNotification": me1200LoopProtectionNotification,
       "me1200LoopProtectionNotificationLoopDetected": me1200LoopProtectionNotificationLoopDetected,
       "me1200LoopProtectionMibConformance": me1200LoopProtectionMibConformance,
       "me1200LoopProtectionMibCompliances": me1200LoopProtectionMibCompliances,
       "me1200LoopProtectionMibCompliance": me1200LoopProtectionMibCompliance,
       "me1200LoopProtectionMibGroups": me1200LoopProtectionMibGroups,
       "me1200LoopProtectionGlobalsInfoGroup": me1200LoopProtectionGlobalsInfoGroup,
       "me1200LoopProtectionInterfaceParamTableInfoGroup": me1200LoopProtectionInterfaceParamTableInfoGroup,
       "me1200LoopProtectionInterfaceStatusTableInfoGroup": me1200LoopProtectionInterfaceStatusTableInfoGroup,
       "me1200LoopProtectionNotificationInfoGroup": me1200LoopProtectionNotificationInfoGroup}
)
