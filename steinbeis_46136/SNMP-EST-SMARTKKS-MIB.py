# SNMP MIB module (SNMP-EST-SMARTKKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/steinbeis_46136/SNMP-EST-SMARTKKS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:03:21 2025
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

steinbeisESTsmartKKS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46136)
)
if mibBuilder.loadTexts:
    steinbeisESTsmartKKS.setRevisions(
        ("2016-04-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KksParameters_ObjectIdentity = ObjectIdentity
kksParameters = _KksParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1)
)
_ParameterData_ObjectIdentity = ObjectIdentity
parameterData = _ParameterData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1, 1)
)
_DeviceBusmaster_ObjectIdentity = ObjectIdentity
deviceBusmaster = _DeviceBusmaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1, 1, 1)
)
_DeviceMeasure_ObjectIdentity = ObjectIdentity
deviceMeasure = _DeviceMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1, 1, 8)
)
_DevicePowerSupply_ObjectIdentity = ObjectIdentity
devicePowerSupply = _DevicePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1, 1, 16)
)
_DeviceBusGateway_ObjectIdentity = ObjectIdentity
deviceBusGateway = _DeviceBusGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1, 1, 32)
)
_DeviceSystemHandler_ObjectIdentity = ObjectIdentity
deviceSystemHandler = _DeviceSystemHandler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 1, 1, 238)
)
_KksTables_ObjectIdentity = ObjectIdentity
kksTables = _KksTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2)
)
_TableDescriptors_ObjectIdentity = ObjectIdentity
tableDescriptors = _TableDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 1)
)
_TableUtilities_ObjectIdentity = ObjectIdentity
tableUtilities = _TableUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 2)
)
_TableData_ObjectIdentity = ObjectIdentity
tableData = _TableData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 5)
)
_DataTimeTriggers_ObjectIdentity = ObjectIdentity
dataTimeTriggers = _DataTimeTriggers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 5, 1)
)
_DataEventContacts_ObjectIdentity = ObjectIdentity
dataEventContacts = _DataEventContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 5, 2)
)
_DataEventLog_ObjectIdentity = ObjectIdentity
dataEventLog = _DataEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 5, 3)
)
_DataPendingEvents_ObjectIdentity = ObjectIdentity
dataPendingEvents = _DataPendingEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 2, 5, 4)
)
_KksEvents_ObjectIdentity = ObjectIdentity
kksEvents = _KksEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3)
)
_EventDescriptor_ObjectIdentity = ObjectIdentity
eventDescriptor = _EventDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1)
)
_EventBusmaster_ObjectIdentity = ObjectIdentity
eventBusmaster = _EventBusmaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1, 1)
)
_EventMeasure_ObjectIdentity = ObjectIdentity
eventMeasure = _EventMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1, 8)
)
_EventPowerSupply_ObjectIdentity = ObjectIdentity
eventPowerSupply = _EventPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1, 16)
)
_EventBusGateway_ObjectIdentity = ObjectIdentity
eventBusGateway = _EventBusGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1, 32)
)
_EventSystemHandler_ObjectIdentity = ObjectIdentity
eventSystemHandler = _EventSystemHandler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1, 238)
)
_EventClass_ObjectIdentity = ObjectIdentity
eventClass = _EventClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 1, 238, 238)
)
_EventUtilities_ObjectIdentity = ObjectIdentity
eventUtilities = _EventUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 2)
)
_EventData_ObjectIdentity = ObjectIdentity
eventData = _EventData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5)
)
_EventDataTable_Object = MibTable
eventDataTable = _EventDataTable_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1)
)
if mibBuilder.loadTexts:
    eventDataTable.setStatus("current")
_EventDataTableEntry_Object = MibTableRow
eventDataTableEntry = _EventDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1, 1)
)
eventDataTableEntry.setIndexNames(
    (0, "SNMP-EST-SMARTKKS-MIB", "eventTableID"),
)
if mibBuilder.loadTexts:
    eventDataTableEntry.setStatus("current")
_EventTableID_Type = Integer32
_EventTableID_Object = MibTableColumn
eventTableID = _EventTableID_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1, 1, 1),
    _EventTableID_Type()
)
eventTableID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTableID.setStatus("current")


class _EventID_Type(OctetString):
    """Custom type eventID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_EventID_Type.__name__ = "OctetString"
_EventID_Object = MibTableColumn
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1, 1, 2),
    _EventID_Type()
)
eventID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventID.setStatus("current")
_EventPriority_Type = Integer32
_EventPriority_Object = MibTableColumn
eventPriority = _EventPriority_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1, 1, 3),
    _EventPriority_Type()
)
eventPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventPriority.setStatus("current")


class _EventInfo_Type(OctetString):
    """Custom type eventInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EventInfo_Type.__name__ = "OctetString"
_EventInfo_Object = MibTableColumn
eventInfo = _EventInfo_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1, 1, 4),
    _EventInfo_Type()
)
eventInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventInfo.setStatus("current")


class _EventTime_Type(OctetString):
    """Custom type eventTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EventTime_Type.__name__ = "OctetString"
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 46136, 3, 5, 1, 1, 5),
    _EventTime_Type()
)
eventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-EST-SMARTKKS-MIB",
    **{"steinbeisESTsmartKKS": steinbeisESTsmartKKS,
       "kksParameters": kksParameters,
       "parameterData": parameterData,
       "deviceBusmaster": deviceBusmaster,
       "deviceMeasure": deviceMeasure,
       "devicePowerSupply": devicePowerSupply,
       "deviceBusGateway": deviceBusGateway,
       "deviceSystemHandler": deviceSystemHandler,
       "kksTables": kksTables,
       "tableDescriptors": tableDescriptors,
       "tableUtilities": tableUtilities,
       "tableData": tableData,
       "dataTimeTriggers": dataTimeTriggers,
       "dataEventContacts": dataEventContacts,
       "dataEventLog": dataEventLog,
       "dataPendingEvents": dataPendingEvents,
       "kksEvents": kksEvents,
       "eventDescriptor": eventDescriptor,
       "eventBusmaster": eventBusmaster,
       "eventMeasure": eventMeasure,
       "eventPowerSupply": eventPowerSupply,
       "eventBusGateway": eventBusGateway,
       "eventSystemHandler": eventSystemHandler,
       "eventClass": eventClass,
       "eventUtilities": eventUtilities,
       "eventData": eventData,
       "eventDataTable": eventDataTable,
       "eventDataTableEntry": eventDataTableEntry,
       "eventTableID": eventTableID,
       "eventID": eventID,
       "eventPriority": eventPriority,
       "eventInfo": eventInfo,
       "eventTime": eventTime}
)
