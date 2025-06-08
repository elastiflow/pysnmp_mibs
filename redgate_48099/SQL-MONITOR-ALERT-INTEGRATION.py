# SNMP MIB module (SQL-MONITOR-ALERT-INTEGRATION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/redgate_48099/SQL-MONITOR-ALERT-INTEGRATION.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:54 2025
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Redgate_ObjectIdentity = ObjectIdentity
redgate = _Redgate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48099)
)
_SqlMonitor_ObjectIdentity = ObjectIdentity
sqlMonitor = _SqlMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48099, 1)
)
_AlertIntegration_ObjectIdentity = ObjectIdentity
alertIntegration = _AlertIntegration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1)
)
_AlertId_Type = DisplayString
_AlertId_Object = MibScalar
alertId = _AlertId_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 1),
    _AlertId_Type()
)
alertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertId.setStatus("current")
_AlertType_Type = DisplayString
_AlertType_Object = MibScalar
alertType = _AlertType_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 2),
    _AlertType_Type()
)
alertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertType.setStatus("current")
_AlertDescription_Type = DisplayString
_AlertDescription_Object = MibScalar
alertDescription = _AlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 3),
    _AlertDescription_Type()
)
alertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertDescription.setStatus("current")
_EventTime_Type = DisplayString
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 4),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_CurrentSeverity_Type = DisplayString
_CurrentSeverity_Object = MibScalar
currentSeverity = _CurrentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 5),
    _CurrentSeverity_Type()
)
currentSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSeverity.setStatus("current")
_TargetObject_Type = DisplayString
_TargetObject_Object = MibScalar
targetObject = _TargetObject_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 6),
    _TargetObject_Type()
)
targetObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetObject.setStatus("current")
_DetailsUrl_Type = DisplayString
_DetailsUrl_Object = MibScalar
detailsUrl = _DetailsUrl_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 7),
    _DetailsUrl_Type()
)
detailsUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detailsUrl.setStatus("current")
_StatusChangeType_Type = DisplayString
_StatusChangeType_Object = MibScalar
statusChangeType = _StatusChangeType_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 8),
    _StatusChangeType_Type()
)
statusChangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusChangeType.setStatus("current")
_PreviousWorstSeverity_Type = DisplayString
_PreviousWorstSeverity_Object = MibScalar
previousWorstSeverity = _PreviousWorstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 48099, 1, 1, 9),
    _PreviousWorstSeverity_Type()
)
previousWorstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    previousWorstSeverity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SQL-MONITOR-ALERT-INTEGRATION",
    **{"redgate": redgate,
       "sqlMonitor": sqlMonitor,
       "alertIntegration": alertIntegration,
       "alertId": alertId,
       "alertType": alertType,
       "alertDescription": alertDescription,
       "eventTime": eventTime,
       "currentSeverity": currentSeverity,
       "targetObject": targetObject,
       "detailsUrl": detailsUrl,
       "statusChangeType": statusChangeType,
       "previousWorstSeverity": previousWorstSeverity}
)
